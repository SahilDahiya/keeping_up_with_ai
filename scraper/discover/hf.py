"""Hugging Face blog discovery — gated on an approved tag list.

HF has no per-tag RSS (its one feed is the whole blog), and the listing pages are
JS-rendered. But the page ships its data as a JSON blob in the Svelte component's
`data-props` attribute, so no headless browser is needed — we read the JSON directly.

Each post in that JSON carries its own `tags` array, which lets us enforce the gate
on the *listing* data: a post is only ever fetched if it actually carries one of the
approved tags in `sources.yaml`. HF publishes a lot the KB does not want (community
submissions, partnerships, cv/audio/robotics), so this tier is opt-in by tag, never
a firehose.
"""

from __future__ import annotations

import html
import json
import re
from urllib.parse import urljoin

from ..config import SourceConfig, normalize_url
from ..fetch import Fetcher, FetchError

HF_ROOT = "https://huggingface.co"
HF_BLOG = f"{HF_ROOT}/blog"
MAX_PAGES = 60  # backstop; ~14 posts/page, so this is far beyond any real tag

_PROPS = re.compile(r'data-target="Articles"[^>]*data-props="([^"]+)"')


def _page_props(fetcher: Fetcher, url: str, interval: float) -> dict | None:
    try:
        resp = fetcher.get(url, interval=interval)
    except FetchError:
        return None
    m = _PROPS.search(resp.text)
    if not m:
        return None
    try:
        return json.loads(html.unescape(m.group(1)))
    except json.JSONDecodeError:
        return None


def discover_hf(fetcher: Fetcher, source: SourceConfig):
    from . import Discovered

    approved = set(source.hf_tags)
    if not approved:
        return []  # no approved tags => ingest nothing. The gate is the point.

    found: dict[str, Discovered] = {}
    for tag in sorted(approved):
        for page in range(MAX_PAGES):
            props = _page_props(fetcher, f"{HF_BLOG}?tag={tag}&p={page}",
                                source.rate_limit_seconds)
            if not props:
                break
            posts = props.get("allBlogs") or []
            for post in posts:
                # Re-check the gate against the post's own tags, not just the page we
                # asked for — belt and braces if HF ever changes tag-page semantics.
                if not (set(post.get("tags") or []) & approved):
                    continue
                slug = post.get("slug")
                href = post.get("url") or (f"/blog/{slug}" if slug else None)
                if not href:
                    continue
                url = normalize_url(urljoin(HF_ROOT, href))
                if not source.url_allowed(url):
                    continue
                found[url] = Discovered(
                    url=url,
                    date_hint=post.get("publishedAt"),
                    title_hint=post.get("title"),
                )
            total = props.get("numTotalItems") or 0
            per_page = props.get("numItemsPerPage") or len(posts) or 1
            if not posts or (page + 1) * per_page >= total:
                break
    return list(found.values())
