"""HTML -> clean markdown + metadata via trafilatura."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timedelta, timezone

import trafilatura

MIN_BODY_CHARS = 400

# --- Date plausibility -------------------------------------------------------
# trafilatura infers a publication date from the page, and it will happily lift a
# stray year out of body prose. A 2026 Cresta post about word error rate came back
# as 1997-08-15, because the article discussed WER's history. A silently wrong date
# is worse than no date: it sorts the article to the bottom of every index and it
# makes any date-based rule (e.g. a pre-2023 cutoff) delete the wrong things.
#
# So an extracted date outside a plausible window is treated as a failed guess, and
# we fall back to the date the *feed or sitemap* reported — which is structured data,
# not prose, and is therefore trustworthy.
#
# Floor: no blog in sources.yaml existed before this. It is deliberately well below
# the oldest real post (chip-huyen, 2020) so it only ever catches garbage.
# This applies to SCRAPED BLOGS ONLY. arXiv papers get their date from the arXiv API
# and bypass this entirely — which matters, because e.g. Adam (2014) is legitimately
# older than this floor.
MIN_PLAUSIBLE_YEAR = 2015

# The ceiling is computed from today, NOT hardcoded, so this does not break on a
# year rollover — a post published tomorrow still passes.
#
# NOTE (review in 2027): MIN_PLAUSIBLE_YEAR is the one judgment call here. It is a
# static floor and will not break anything on its own, but revisit it as the corpus
# ages — if the KB stops wanting pre-2020 content, raise it so bad extractions are
# caught earlier rather than sneaking through as "old but plausible".
MAX_FUTURE_DAYS = 2  # tolerate timezone skew / posts dated slightly ahead


def plausible_date(date: str | None) -> bool:
    """Is this ISO date a believable publication date, or a bad extraction?"""
    if not date:
        return False
    try:
        parsed = datetime.strptime(date[:10], "%Y-%m-%d").date()
    except ValueError:
        return False
    today = datetime.now(timezone.utc).date()
    return (parsed.year >= MIN_PLAUSIBLE_YEAR
            and parsed <= today + timedelta(days=MAX_FUTURE_DAYS))


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
                    date_hint: str | None = None, min_words: int = 0,
                    prefer_hint_date: bool = False, title_suffix: str | None = None) -> Article:
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
    if title_suffix and title.rstrip().endswith(title_suffix):
        title = title.rstrip()[: -len(title_suffix)].rstrip(" -|·—")

    words = len(body.split())
    if min_words and words < min_words:
        raise TooShallow(f"below min_words ({words} < {min_words})")

    # Prefer the page-extracted date (usually the most accurate) unless the source is
    # flagged prefer_hint_date, in which case the feed/sitemap date wins — some sites
    # serve a constant template date in the body that trafilatura misreads. Either way
    # only a plausible date is kept; if neither is believable, publish no date.
    extracted = meta.date if meta else None
    hint = date_hint[:10] if date_hint else None
    order = (hint, extracted) if prefer_hint_date else (extracted, hint)
    published = next((d for d in order if plausible_date(d)), None)
    return Article(
        url=url,
        title=title.strip(),
        body_md=body.strip(),
        author=(meta.author if meta else None),
        published=published,
        description=(meta.description if meta else None),
        words=words,
    )
