"""sitemap.xml discovery tier (handles sitemap-index recursion)."""

from __future__ import annotations

import xml.etree.ElementTree as ET

from ..config import SourceConfig, normalize_url
from ..fetch import Fetcher, FetchError

_NS = "{http://www.sitemaps.org/schemas/sitemap/0.9}"
_MAX_CHILD_SITEMAPS = 50


def _parse(content: bytes) -> ET.Element | None:
    try:
        return ET.fromstring(content)
    except ET.ParseError:
        return None


def discover_sitemap(fetcher: Fetcher, source: SourceConfig, *, _url: str | None = None, _depth: int = 0):
    from . import Discovered

    url = _url or source.sitemap
    if not url or _depth > 2:
        return []
    try:
        resp = fetcher.get(url, interval=source.rate_limit_seconds)
    except FetchError:
        return []
    root = _parse(resp.content)
    if root is None:
        return []

    out = []
    if root.tag == f"{_NS}sitemapindex":
        children = root.findall(f"{_NS}sitemap/{_NS}loc")[:_MAX_CHILD_SITEMAPS]
        for loc in children:
            out.extend(discover_sitemap(fetcher, source, _url=loc.text.strip(), _depth=_depth + 1))
        return out

    for node in root.findall(f"{_NS}url"):
        loc = node.find(f"{_NS}loc")
        if loc is None or not loc.text:
            continue
        u = normalize_url(loc.text)
        if not source.url_allowed(u):
            continue
        lastmod_node = node.find(f"{_NS}lastmod")
        lastmod = lastmod_node.text.strip() if lastmod_node is not None and lastmod_node.text else None
        out.append(Discovered(url=u, date_hint=lastmod))
    return out
