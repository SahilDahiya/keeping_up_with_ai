"""Article-URL discovery: feed and sitemap tiers."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass
class Discovered:
    url: str
    date_hint: str | None = None  # ISO date/datetime string if the tier provided one
    title_hint: str | None = None


from .feed import discover_feed  # noqa: E402
from .sitemap import discover_sitemap  # noqa: E402

__all__ = ["Discovered", "discover_feed", "discover_sitemap"]
