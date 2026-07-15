"""Shopify Engineering discovery — one topic, isolated via the sitemap.

Shopify Engineering has no usable RSS, and its topic pages are a React Router SPA:
the article list is not in the initial HTML but in the loader-data endpoint the app
fetches (`<topic-url>.data`, a turbo-stream blob). That blob is not clean JSON, but it
does contain the topic's article slugs as bare strings.

The site's flat sitemap.xml lists every article as `/<slug>` with an authoritative
`<lastmod>` — but with no topic information, so it cannot isolate AI/ML on its own.

So we intersect the two: slugs that appear in the topic's `.data` AND in the sitemap are
this topic's articles, and the sitemap supplies their canonical URL and date. That keeps
us scoped to the one requested topic (AI/ML) rather than the whole engineering blog, and
it is resilient to junk tokens in the turbo-stream — a token only counts if the sitemap
agrees it is a real article.
"""

from __future__ import annotations

import re

from ..config import SourceConfig, normalize_url
from ..fetch import Fetcher, FetchError

# Slug-shaped tokens: lowercase, hyphenated, ≥5 chars (skips "ai", "the", css ids).
_SLUG_TOKEN = re.compile(r'"([a-z0-9][a-z0-9-]{4,})"')
_SITEMAP_ENTRY = re.compile(
    r"<loc>https?://[^/]+/([a-z0-9-]+)</loc>(?:\s*<lastmod>([0-9-]+))?"
)
# Sitemap slugs that are sections/utility pages, not articles.
_NON_ARTICLE = {"topics", "authors", "sitemap", "install", "settings",
                "translations", "hack-days", "blog"}


def _sitemap_slugs(fetcher: Fetcher, sitemap_url: str, interval: float) -> dict[str, str | None]:
    try:
        resp = fetcher.get(sitemap_url, interval=interval)
    except FetchError:
        return {}
    slugs: dict[str, str | None] = {}
    for slug, lastmod in _SITEMAP_ENTRY.findall(resp.text):
        if slug not in _NON_ARTICLE:
            slugs.setdefault(slug, lastmod or None)
    return slugs


def discover_shopify(fetcher: Fetcher, source: SourceConfig):
    from . import Discovered

    if not source.sitemap:
        return []
    site = _sitemap_slugs(fetcher, source.sitemap, source.rate_limit_seconds)
    if not site:
        return []

    # The topic's loader-data endpoint: React Router serves it at "<path>.data".
    try:
        data = fetcher.get(source.home.rstrip("/") + ".data", interval=source.rate_limit_seconds)
    except FetchError:
        return []

    topic_slugs = set(_SLUG_TOKEN.findall(data.text))
    out = []
    for slug in sorted(topic_slugs & site.keys()):
        url = normalize_url(f"{source.home.split('/topics/')[0].rstrip('/')}/{slug}")
        if not source.url_allowed(url):
            continue
        out.append(Discovered(url=url, date_hint=site[slug]))
    return out
