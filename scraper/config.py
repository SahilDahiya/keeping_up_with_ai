"""Load sources.yaml and kb/taxonomy.yaml into typed config objects."""

from __future__ import annotations

import re
from pathlib import Path
from typing import Literal
from urllib.parse import urlsplit, urlunsplit, parse_qsl, urlencode

import yaml
from pydantic import BaseModel, Field

REPO_ROOT = Path(__file__).resolve().parent.parent
SOURCES_PATH = REPO_ROOT / "sources.yaml"
KB_ROOT = REPO_ROOT / "kb"
TAXONOMY_PATH = KB_ROOT / "taxonomy.yaml"
INBOX_DIR = KB_ROOT / "_inbox"
STATE_PATH = REPO_ROOT / "state.db"       # local cache; rebuildable from STATE_JSONL_PATH
STATE_JSONL_PATH = REPO_ROOT / "state.jsonl"  # committed source of truth (git-friendly)
CACHE_DIR = REPO_ROOT / "cache" / "raw"

# Tracking params stripped during URL normalization.
_TRACKING_PARAMS = re.compile(r"^(utm_|ref$|ref_|source$|fbclid|gclid)")


class SourceConfig(BaseModel):
    slug: str
    name: str
    home: str
    feed: str | None = None
    sitemap: str | None = None
    discovery: list[Literal["feed", "sitemap", "hf", "shopify"]] = Field(default_factory=lambda: ["feed", "sitemap"])
    # Hugging Face only: the approved tag allowlist. Empty => ingest nothing.
    hf_tags: list[str] = Field(default_factory=list)
    include_prefixes: list[str] = Field(default_factory=list)
    include_regex: str | None = None
    exclude_regex: str | None = None
    rate_limit_seconds: float = 2.0
    min_words: int = 0
    # Trust the discovery date (feed/sitemap) over the page-extracted date. Set for
    # sources where trafilatura misreads the date — e.g. Shopify serves a constant
    # template date in the body that would otherwise win.
    prefer_hint_date: bool = False
    # Site chrome to strip from the end of an extracted title, e.g. " - Shopify"
    # (trafilatura reads the HTML <title>, which often carries a site suffix).
    title_suffix: str | None = None
    since: str | None = None  # ISO date floor for backfill
    tags: list[str] = Field(default_factory=list)

    def url_allowed(self, url: str) -> bool:
        """Path-based filter: is this URL an article we want from this source?"""
        path = urlsplit(url).path or "/"
        if self.include_prefixes and not any(path.startswith(p) for p in self.include_prefixes):
            return False
        if self.include_regex and not re.search(self.include_regex, path):
            return False
        if self.exclude_regex and re.search(self.exclude_regex, path):
            return False
        # Never treat the listing/home page itself as an article.
        home_path = urlsplit(self.home).path.rstrip("/")
        if path.rstrip("/") in ("", home_path):
            return False
        return True


def load_sources(path: Path = SOURCES_PATH) -> list[SourceConfig]:
    raw = yaml.safe_load(path.read_text())
    defaults = raw.get("defaults", {})
    sources = []
    for entry in raw["sources"]:
        merged = {**defaults, **entry}
        sources.append(SourceConfig(**merged))
    return sources


def get_source(slug: str, path: Path = SOURCES_PATH) -> SourceConfig:
    for s in load_sources(path):
        if s.slug == slug:
            return s
    raise KeyError(f"unknown source: {slug}")


def load_taxonomy(path: Path = TAXONOMY_PATH) -> dict[str, list[str]]:
    raw = yaml.safe_load(path.read_text())
    return {topic: list(subs or []) for topic, subs in raw["topics"].items()}


def taxonomy_rev(path: Path = TAXONOMY_PATH) -> int:
    raw = yaml.safe_load(path.read_text())
    return int(raw.get("rev", 1))


def normalize_url(url: str) -> str:
    """Canonical form used as the state-db key: strip fragment + tracking params."""
    parts = urlsplit(url.strip())
    query = [(k, v) for k, v in parse_qsl(parts.query) if not _TRACKING_PARAMS.match(k)]
    return urlunsplit((
        parts.scheme.lower(),
        parts.netloc.lower(),
        parts.path,
        urlencode(query),
        "",  # drop fragment
    ))
