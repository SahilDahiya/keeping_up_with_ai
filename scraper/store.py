"""KB writer: inbox staging, frontmatter, title filenames, filing into the topic tree."""

from __future__ import annotations

import hashlib
import re
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlsplit

import yaml

from .config import INBOX_DIR, KB_ROOT, taxonomy_rev
from .extract import Article

_ILLEGAL = re.compile(r'[/\\:*?"<>|\x00-\x1f]')
_MAX_STEM = 150


# ---------------------------------------------------------------- frontmatter

def parse_frontmatter(text: str) -> tuple[dict, str]:
    if not text.startswith("---\n"):
        raise ValueError("missing frontmatter")
    _, fm, body = text.split("---\n", 2)
    return yaml.safe_load(fm), body.lstrip("\n")


def dump_frontmatter(fm: dict, body: str) -> str:
    header = yaml.safe_dump(fm, default_flow_style=False, allow_unicode=True, sort_keys=False)
    return f"---\n{header}---\n\n{body.rstrip()}\n"


# --------------------------------------------------------------------- inbox

def _inbox_name(source_slug: str, url: str) -> str:
    path = urlsplit(url).path.strip("/").replace("/", "-") or "index"
    stem = f"{source_slug}--{path}"[:_MAX_STEM]
    return f"{stem}.md"


def content_hash(body_md: str) -> str:
    return hashlib.sha256(body_md.encode()).hexdigest()


def write_inbox(source_slug: str, article: Article, *, kind: str = "blog",
                extra: dict | None = None, body_md: str | None = None) -> Path:
    """Stage an extracted item; classification fields are left for the agent.

    `kind` is "blog" (scraped from a source in sources.yaml) or "paper" (an arXiv link
    the user explicitly queued). `extra` carries kind-specific frontmatter, e.g. a
    paper's arxiv_id / authors / categories.
    """
    INBOX_DIR.mkdir(parents=True, exist_ok=True)
    body = body_md if body_md is not None else article.body_md
    fm = {
        "title": article.title,
        "kind": kind,
        "topic": None,
        "subtopic": None,
        "secondary_topics": [],
        "summary": None,
        "triage": None,
        "skip_reason": None,
        "source": source_slug,
        "url": article.url,
        "author": article.author,
        "published": article.published,
        "fetched": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "classifier": None,
        "taxonomy_rev": taxonomy_rev(),
        "words": article.words,
        "content_sha256": content_hash(body),
        **(extra or {}),
    }
    path = INBOX_DIR / _inbox_name(source_slug, article.url)
    path.write_text(dump_frontmatter(fm, f"# {article.title}\n\n{body}"))
    return path


def update_filed_body(kb_path: Path, article: Article) -> None:
    """Upstream edit to an already-filed article: refresh body, keep classification."""
    fm, _ = parse_frontmatter(kb_path.read_text())
    fm["fetched"] = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    fm["words"] = article.words
    fm["content_sha256"] = content_hash(article.body_md)
    kb_path.write_text(dump_frontmatter(fm, f"# {article.title}\n\n{article.body_md}"))


# -------------------------------------------------------------------- filing

PAPER_PREFIX = "[Paper] "


def sanitize_title(title: str) -> str:
    stem = _ILLEGAL.sub("", title)
    stem = re.sub(r"\s+", " ", stem).strip().rstrip(". ")
    return stem[:_MAX_STEM].rstrip(". ") or "untitled"


def filename_stem(fm: dict) -> str:
    """Filename stem for an article: its title, prefixed '[Paper] ' for arXiv papers.

    The prefix makes papers obvious in the file tree and greppable/globbable
    ('kb/**/[Paper] *.md') without opening frontmatter.
    """
    stem = sanitize_title(fm["title"])
    return f"{PAPER_PREFIX}{stem}" if fm.get("kind") == "paper" else stem


class FilingError(Exception):
    pass


def file_article(inbox_path: Path, taxonomy: dict[str, list[str]]) -> Path:
    """Validate classification frontmatter and move an inbox file into the topic tree."""
    fm, body = parse_frontmatter(inbox_path.read_text())
    topic, subtopic = fm.get("topic"), fm.get("subtopic")

    if topic == "unclassified":
        dest_dir = KB_ROOT / "unclassified"
    elif topic in taxonomy:
        if subtopic not in taxonomy[topic]:
            raise FilingError(f"{inbox_path.name}: subtopic {subtopic!r} not in taxonomy[{topic}]")
        dest_dir = KB_ROOT / topic / subtopic
    else:
        raise FilingError(f"{inbox_path.name}: topic {topic!r} not in taxonomy (or 'unclassified')")

    for sec in fm.get("secondary_topics") or []:
        sec_topic, _, sec_sub = str(sec).partition("/")
        if sec_topic not in taxonomy or (sec_sub and sec_sub not in taxonomy[sec_topic]):
            raise FilingError(f"{inbox_path.name}: bad secondary topic {sec!r}")

    if not fm.get("summary"):
        raise FilingError(f"{inbox_path.name}: summary is required")

    dest_dir.mkdir(parents=True, exist_ok=True)
    stem = filename_stem(fm)
    dest = dest_dir / f"{stem}.md"
    if dest.exists() and parse_frontmatter(dest.read_text())[0].get("url") != fm.get("url"):
        dest = dest_dir / f"{stem} ({fm['source']}).md"
    if dest.exists() and parse_frontmatter(dest.read_text())[0].get("url") != fm.get("url"):
        year = str(fm.get("published") or "undated")[:4]
        dest = dest_dir / f"{stem} ({fm['source']}, {year}).md"

    dest.write_text(dump_frontmatter(fm, body))
    inbox_path.unlink()
    return dest
