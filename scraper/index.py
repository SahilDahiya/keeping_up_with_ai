"""Regenerate derived indexes from article frontmatter.

Everything here is derived data: per-topic index.md, _sources/ views, catalog.jsonl.
Never hand-edited; safe to rebuild from scratch on every run.
"""

from __future__ import annotations

import json
from pathlib import Path

from .config import KB_ROOT, load_taxonomy
from .store import parse_frontmatter


def _collect(taxonomy: dict[str, list[str]]) -> list[dict]:
    records = []
    dirs = [KB_ROOT / t for t in taxonomy] + [KB_ROOT / "unclassified"]
    for d in dirs:
        if not d.exists():
            continue
        for path in sorted(d.rglob("*.md")):
            if path.name == "index.md":
                continue
            fm, _ = parse_frontmatter(path.read_text())
            fm["_path"] = path.relative_to(KB_ROOT).as_posix()
            records.append(fm)
    return records


def _sort_key(rec: dict) -> str:
    return str(rec.get("published") or "0000-00-00")


def _entry(rec: dict, *, from_dir: Path) -> str:
    rel = Path(KB_ROOT, rec["_path"]).relative_to(from_dir, walk_up=True).as_posix()
    date = rec.get("published") or "undated"
    marker = "**[Paper]** " if rec.get("kind") == "paper" else ""
    line = (f"- **{date}** — {marker}[{rec['title']}](<{rel}>) · "
            f"`{rec.get('subtopic') or '—'}` · {rec['source']}")
    if rec.get("summary"):
        line += f"\n  {rec['summary']}"
    return line


def rebuild_indexes() -> dict[str, int]:
    taxonomy = load_taxonomy()
    records = _collect(taxonomy)
    stats = {"articles": len(records), "topics": 0, "sources": 0}

    # Per-topic index.md
    for topic in list(taxonomy) + ["unclassified"]:
        topic_dir = KB_ROOT / topic
        native = [r for r in records if r["_path"].startswith(f"{topic}/")]
        also = [
            r for r in records
            if any(str(s).split("/")[0] == topic for s in (r.get("secondary_topics") or []))
        ]
        if not native and not also:
            if (topic_dir / "index.md").exists():
                (topic_dir / "index.md").unlink()
            continue
        lines = [f"# {topic}", "", f"{len(native)} articles.", ""]
        for rec in sorted(native, key=_sort_key, reverse=True):
            lines.append(_entry(rec, from_dir=topic_dir))
        if also:
            lines += ["", "## Also relevant (filed elsewhere)", ""]
            for rec in sorted(also, key=_sort_key, reverse=True):
                lines.append(_entry(rec, from_dir=topic_dir))
        topic_dir.mkdir(parents=True, exist_ok=True)
        (topic_dir / "index.md").write_text("\n".join(lines) + "\n")
        stats["topics"] += 1

    # Per-source views
    sources_dir = KB_ROOT / "_sources"
    sources_dir.mkdir(parents=True, exist_ok=True)
    for old in sources_dir.glob("*.md"):
        old.unlink()
    by_source: dict[str, list[dict]] = {}
    for rec in records:
        by_source.setdefault(rec["source"], []).append(rec)
    for source, recs in sorted(by_source.items()):
        lines = [f"# {source}", "", f"{len(recs)} articles.", ""]
        for rec in sorted(recs, key=_sort_key, reverse=True):
            lines.append(_entry(rec, from_dir=sources_dir))
        (sources_dir / f"{source}.md").write_text("\n".join(lines) + "\n")
        stats["sources"] += 1

    # catalog.jsonl
    with (KB_ROOT / "catalog.jsonl").open("w") as f:
        for rec in sorted(records, key=_sort_key, reverse=True):
            f.write(json.dumps({
                "topic": rec.get("topic"),
                "subtopic": rec.get("subtopic"),
                "secondary_topics": rec.get("secondary_topics") or [],
                "kind": rec.get("kind", "blog"),
                "source": rec["source"],
                "url": rec.get("url"),
                "date": rec.get("published"),
                "title": rec["title"],
                "path": rec["_path"],
                "summary": rec.get("summary"),
                "words": rec.get("words"),
                **({"arxiv_id": rec["arxiv_id"]} if rec.get("arxiv_id") else {}),
            }, ensure_ascii=False) + "\n")

    return stats
