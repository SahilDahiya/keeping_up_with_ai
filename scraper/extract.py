"""HTML -> clean markdown + metadata via trafilatura."""

from __future__ import annotations

from dataclasses import dataclass

import trafilatura

MIN_BODY_CHARS = 400


@dataclass
class Article:
    url: str
    title: str
    body_md: str
    author: str | None
    published: str | None  # ISO date
    description: str | None
    words: int


class ExtractionError(Exception):
    """Extraction genuinely failed — worth retrying on a later run."""


class TooShallow(ExtractionError):
    """Article is real but below the source's `min_words` floor.

    This is a deliberate config filter, not a failure: the page will never grow.
    Callers record it as an intentional skip so it is not re-fetched every run.
    """


def extract_article(html: str, url: str, *, title_hint: str | None = None,
                    date_hint: str | None = None, min_words: int = 0) -> Article:
    body = trafilatura.extract(
        html,
        url=url,
        output_format="markdown",
        include_formatting=True,
        include_links=True,
        include_images=True,
        include_tables=True,
        favor_recall=True,
    )
    meta = trafilatura.extract_metadata(html, default_url=url)

    title = (meta.title if meta else None) or title_hint
    if not body or len(body) < MIN_BODY_CHARS:
        raise ExtractionError(f"body too short ({len(body or '')} chars)")
    if not title:
        raise ExtractionError("no title found")

    words = len(body.split())
    if min_words and words < min_words:
        raise TooShallow(f"below min_words ({words} < {min_words})")

    published = (meta.date if meta else None) or (date_hint[:10] if date_hint else None)
    return Article(
        url=url,
        title=title.strip(),
        body_md=body.strip(),
        author=(meta.author if meta else None),
        published=published,
        description=(meta.description if meta else None),
        words=words,
    )
