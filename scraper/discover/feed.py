"""RSS/Atom feed discovery tier."""

from __future__ import annotations

import time

import feedparser

from ..config import SourceConfig, normalize_url
from ..fetch import Fetcher


def _iso(struct: time.struct_time | None) -> str | None:
    if struct is None:
        return None
    return time.strftime("%Y-%m-%dT%H:%M:%SZ", struct)


def discover_feed(fetcher: Fetcher, source: SourceConfig):
    from . import Discovered

    if not source.feed:
        return []
    resp = fetcher.get(source.feed, interval=source.rate_limit_seconds)
    parsed = feedparser.parse(resp.content)
    out = []
    for entry in parsed.entries:
        link = entry.get("link")
        if not link:
            continue
        url = normalize_url(link)
        if not source.url_allowed(url):
            continue
        date = _iso(entry.get("published_parsed") or entry.get("updated_parsed"))
        out.append(Discovered(url=url, date_hint=date, title_hint=entry.get("title")))
    return out
