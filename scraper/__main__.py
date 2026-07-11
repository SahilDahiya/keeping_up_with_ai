"""kb-scraper CLI."""

from __future__ import annotations

from pathlib import Path
from typing import Optional

import typer

from .config import INBOX_DIR, load_sources, get_source, load_taxonomy, SourceConfig
from .discover import Discovered, discover_feed, discover_sitemap
from .extract import ExtractionError, extract_article
from .fetch import Fetcher, FetchError
from .index import rebuild_indexes
from .state import State
from .store import (
    FilingError,
    content_hash,
    file_article,
    parse_frontmatter,
    update_filed_body,
    write_inbox,
)

app = typer.Typer(no_args_is_help=True, add_completion=False)

_TIERS = {"feed": discover_feed, "sitemap": discover_sitemap}
_SKIP_REASONS = {
    "archive-page",
    "promotion",
    "company-news",
    "release-note-lite",
    "event-list",
    "thought-leadership-lite",
    "duplicate",
    "too-shallow",
    "off-topic",
}


def _sources(slug: Optional[str]) -> list[SourceConfig]:
    return [get_source(slug)] if slug else load_sources()


def _dedupe(items: list[Discovered]) -> list[Discovered]:
    seen: dict[str, Discovered] = {}
    for d in items:
        if d.url not in seen or (d.date_hint and not seen[d.url].date_hint):
            seen[d.url] = d
    return list(seen.values())


def _classified_inbox_targets() -> list[Path]:
    """Inbox files with classification work started; untouched null-frontmatter files wait."""
    targets: list[Path] = []
    for candidate in sorted(INBOX_DIR.glob("*.md")):
        try:
            fm, _ = parse_frontmatter(candidate.read_text())
        except Exception:
            targets.append(candidate)
            continue
        if any(fm.get(key) not in (None, "") for key in ("topic", "summary", "classifier")):
            targets.append(candidate)
    return targets


def _skip_targets(path: Optional[Path], pattern: Optional[str]) -> list[Path]:
    if path and pattern:
        raise typer.BadParameter("pass either PATH or --pattern, not both")
    if path:
        return [path]
    if pattern:
        base = Path(".") if "/" in pattern else INBOX_DIR
        return sorted(base.glob(pattern))
    return []


def _repo_root() -> Path:
    return Path(__file__).resolve().parent.parent


def _process(source: SourceConfig, discovered: list[Discovered], fetcher: Fetcher,
             state: State, *, limit: Optional[int], since: Optional[str]) -> dict:
    stats = {"discovered": len(discovered), "new": 0, "updated": 0, "skipped": 0, "failed": 0}
    if since:
        discovered = [d for d in discovered if d.date_hint is None or d.date_hint[:10] >= since]
    todo = [d for d in discovered if state.needs_fetch(d.url, d.date_hint)]
    if limit:
        todo = todo[:limit]
    stats["skipped"] = stats["discovered"] - len(todo)

    for d in todo:
        if not fetcher.allowed_by_robots(d.url):
            typer.echo(f"  robots-disallowed: {d.url}")
            state.mark(d.url, source.slug, "skipped")
            continue
        try:
            resp = fetcher.get(d.url, interval=source.rate_limit_seconds)
            article = extract_article(resp.text, d.url, title_hint=d.title_hint,
                                      date_hint=d.date_hint, min_words=source.min_words)
        except (FetchError, ExtractionError) as e:
            typer.echo(f"  FAIL {d.url}: {e}")
            state.mark(d.url, source.slug, "failed")
            stats["failed"] += 1
            continue

        row = state.get(d.url)
        sha = content_hash(article.body_md)
        if row and row["content_sha256"] == sha:
            state.record_fetched(d.url, source.slug, sha256=sha, etag=resp.headers.get("etag"),
                                 last_modified=d.date_hint, status=row["status"], kb_path=row["kb_path"])
            continue
        if row and row["status"] == "filed" and row["kb_path"]:
            kb_file = Path(__file__).resolve().parent.parent / row["kb_path"]
            if kb_file.exists():
                update_filed_body(kb_file, article)
                state.record_fetched(d.url, source.slug, sha256=sha, etag=resp.headers.get("etag"),
                                     last_modified=d.date_hint, status="filed", kb_path=row["kb_path"])
                stats["updated"] += 1
                typer.echo(f"  updated: {row['kb_path']}")
                continue
        path = write_inbox(source.slug, article)
        state.record_fetched(d.url, source.slug, sha256=sha, etag=resp.headers.get("etag"),
                             last_modified=d.date_hint, status="inbox")
        stats["new"] += 1
        typer.echo(f"  inbox: {path.name}")
    return stats


@app.command()
def discover(source: Optional[str] = typer.Option(None, "--source")):
    """Dry run: show what each discovery tier finds per source."""
    fetcher = Fetcher()
    for src in _sources(source):
        typer.echo(f"{src.slug}:")
        for tier in src.discovery:
            found = _TIERS[tier](fetcher, src)
            dated = sum(1 for d in found if d.date_hint)
            typer.echo(f"  {tier}: {len(found)} urls ({dated} with dates)")


@app.command()
def update(source: Optional[str] = typer.Option(None, "--source"),
           limit: Optional[int] = typer.Option(None, "--limit")):
    """Incremental run: first working discovery tier, diff against state, stage to kb/_inbox/."""
    fetcher, state = Fetcher(), State()
    for src in _sources(source):
        typer.echo(f"== {src.slug}")
        discovered: list[Discovered] = []
        for tier in src.discovery:
            try:
                discovered = _TIERS[tier](fetcher, src)
            except Exception as e:  # a broken tier must not kill the multi-source run
                typer.echo(f"  {tier} discovery failed: {e}")
                discovered = []
            if discovered:
                break
        stats = _process(src, _dedupe(discovered), fetcher, state, limit=limit, since=None)
        typer.echo(f"  {stats}")


@app.command()
def backfill(source: Optional[str] = typer.Option(None, "--source"),
             since: Optional[str] = typer.Option(None, "--since", help="ISO date floor"),
             limit: Optional[int] = typer.Option(None, "--limit")):
    """Deep run: merge all discovery tiers, stage everything unseen to kb/_inbox/."""
    fetcher, state = Fetcher(), State()
    for src in _sources(source):
        typer.echo(f"== {src.slug}")
        discovered: list[Discovered] = []
        for tier in src.discovery:
            try:
                discovered.extend(_TIERS[tier](fetcher, src))
            except Exception as e:
                typer.echo(f"  {tier} discovery failed: {e}")
        stats = _process(src, _dedupe(discovered), fetcher, state,
                         limit=limit, since=since or src.since)
        typer.echo(f"  {stats}")


@app.command()
def file(path: Optional[Path] = typer.Argument(None),
         all: bool = typer.Option(False, "--all", help="file every classified inbox item")):
    """Validate classification frontmatter and move inbox item(s) into the topic tree."""
    taxonomy = load_taxonomy()
    state = State()
    targets = _classified_inbox_targets() if all else [path] if path else []
    if not targets:
        typer.echo("nothing to file (pass a path or --all)")
        raise typer.Exit(1)
    filed = errors = 0
    for target in targets:
        try:
            dest = file_article(target, taxonomy)
        except FilingError as e:
            typer.echo(f"  SKIP {e}")
            errors += 1
            continue
        fm, _ = parse_frontmatter(dest.read_text())
        repo_root = Path(__file__).resolve().parent.parent
        state.mark(fm["url"], fm["source"], "filed", kb_path=dest.relative_to(repo_root).as_posix())
        typer.echo(f"  filed: {dest.relative_to(repo_root)}")
        filed += 1
    typer.echo(f"{filed} filed, {errors} skipped")
    if filed:
        stats = rebuild_indexes()
        typer.echo(f"reindexed: {stats}")


@app.command()
def skip(path: Optional[Path] = typer.Argument(None),
         reason: str = typer.Option(..., "--reason", "-r", help="Why this item is junk"),
         pattern: Optional[str] = typer.Option(None, "--pattern", "-p",
                                               help="Inbox glob, e.g. 'arize--blog-category-*.md'")):
    """Remove junk inbox/filed item(s), mark their URLs skipped, and preserve a skip reason."""
    if reason not in _SKIP_REASONS:
        allowed = ", ".join(sorted(_SKIP_REASONS))
        raise typer.BadParameter(f"unknown reason {reason!r}; allowed: {allowed}")
    targets = _skip_targets(path, pattern)
    if not targets:
        typer.echo("nothing to skip (pass a path or --pattern)")
        raise typer.Exit(1)

    state = State()
    skipped = errors = filed_removed = 0
    repo_root = _repo_root()
    for target in targets:
        try:
            fm, _ = parse_frontmatter(target.read_text())
            url, source = fm["url"], fm["source"]
        except Exception as e:
            typer.echo(f"  SKIP-ERROR {target}: {e}")
            errors += 1
            continue
        state.mark(url, source, "skipped", skip_reason=reason)
        try:
            rel_parts = target.resolve().relative_to(repo_root).parts
        except ValueError:
            rel_parts = ()
        if rel_parts and rel_parts[0] == "kb" and "_inbox" not in rel_parts:
            filed_removed += 1
        target.unlink()
        typer.echo(f"  skipped: {target.name} ({reason})")
        skipped += 1
    typer.echo(f"{skipped} skipped, {errors} errors")
    if filed_removed:
        stats = rebuild_indexes()
        typer.echo(f"reindexed: {stats}")


@app.command()
def reindex():
    """Rebuild per-topic index.md files, _sources/ views, and catalog.jsonl."""
    typer.echo(f"reindexed: {rebuild_indexes()}")


@app.command()
def report():
    """Per-source status counts + inbox backlog."""
    state = State()
    for row in state.counts():
        typer.echo(f"{row['source']:28s} {row['status']:8s} {row['n']}")
    pending = len(list(INBOX_DIR.glob("*.md"))) if INBOX_DIR.exists() else 0
    typer.echo(f"\ninbox pending: {pending}")
    if pending:
        typer.echo(f"classified ready to file: {len(_classified_inbox_targets())}")
        typer.echo("→ ask Codex to organize the KB inbox, or run Claude Code's /organize-kb skill")
    skip_counts = state.skip_counts()
    if skip_counts:
        typer.echo("\nskip reasons:")
        for row in skip_counts:
            typer.echo(f"{row['reason']:24s} {row['n']}")


if __name__ == "__main__":
    app()
