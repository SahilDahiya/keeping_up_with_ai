"""arXiv paper ingestion — **gated on an explicit human-provided reading list**.

This module has NO discovery tier, by design. It never queries arXiv listings, RSS,
"recent", "trending", or any recommendation source. The only way a paper enters the
knowledge base is if its link appears in `papers.txt`, which a human edits.

That gate is the whole point: blogs are a firehose we filter, papers are a curated
shelf. If you are tempted to add automatic paper discovery here, don't — put the link
in papers.txt instead.
"""

from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path

import feedparser

from .config import REPO_ROOT
from .extract import Article, ExtractionError
from .fetch import Fetcher, FetchError

PAPERS_LIST = REPO_ROOT / "papers.txt"
ARXIV_API = "http://export.arxiv.org/api/query?id_list={id}"
ARXIV_HTML = "https://arxiv.org/html/{id}"
ARXIV_PDF = "https://arxiv.org/pdf/{id}"
ARXIV_INTERVAL = 3.0  # arXiv asks for ~1 request per 3s
MAX_PDF_PAGES = 60    # guard against 200-page appendix monsters

# A real paper is never this short. arXiv serves an HTML page even for papers it has
# not actually rendered, and trafilatura then returns only nav chrome ("Why HTML?",
# "Report Issue"). Anything under this is a failed extraction, not a short paper —
# fall through to the PDF.
MIN_FULLTEXT_WORDS = 500

# Accepts: 2501.12345, arxiv.org/abs/2501.12345v2, /pdf/..., ar5iv/alphaxiv mirrors,
# and old-style IDs like cs/0112017 or hep-th/9901001.
_ARXIV_ID = re.compile(
    r"(?:arxiv\.org|ar5iv\.(?:org|labs\.arxiv\.org)|alphaxiv\.org|huggingface\.co/papers)"
    r"/(?:abs/|pdf/|html/|papers/)?(?P<id>\d{4}\.\d{4,5}|[a-z-]+(?:\.[A-Z]{2})?/\d{7})"
    r"|^(?P<bare>\d{4}\.\d{4,5})$",
    re.IGNORECASE,
)


class NotAnArxivLink(ValueError):
    pass


@dataclass
class Paper:
    arxiv_id: str
    title: str
    abstract: str
    authors: list[str]
    published: str          # ISO date of v1
    updated: str | None
    categories: list[str]
    comment: str | None
    fulltext_md: str | None
    fulltext_source: str    # "html" | "pdf" | "none" — how the body text was obtained


# PDF text arrives as hard-wrapped lines with hyphenated breaks and page furniture.
_PAGE_NUM = re.compile(r"^\s*\d{1,3}\s*$")
_HYPHEN_BREAK = re.compile(r"(\w)-\n(\w)")
_HARD_WRAP = re.compile(r"(?<![.:;!?])\n(?=[a-z(])")


def _pdf_to_markdown(data: bytes) -> str | None:
    """Extract readable text from an arXiv PDF.

    This is a fallback, not a parser: it recovers the prose (which is what an agent
    researches over) and accepts that equations, figures, and column layout degrade.
    """
    from io import BytesIO

    from pypdf import PdfReader

    try:
        reader = PdfReader(BytesIO(data))
    except Exception:
        return None

    chunks = []
    for page in reader.pages[:MAX_PDF_PAGES]:
        try:
            text = page.extract_text() or ""
        except Exception:
            continue
        lines = [ln for ln in text.splitlines() if not _PAGE_NUM.match(ln)]
        chunks.append("\n".join(lines))

    text = "\n\n".join(chunks)
    text = _HYPHEN_BREAK.sub(r"\1\2", text)   # re-join words split across a line break
    text = _HARD_WRAP.sub(" ", text)          # unwrap mid-sentence line breaks
    text = re.sub(r"\n{3,}", "\n\n", text).strip()
    truncated = len(reader.pages) > MAX_PDF_PAGES
    if truncated:
        text += f"\n\n_[truncated: first {MAX_PDF_PAGES} of {len(reader.pages)} pages]_"
    return text or None


def parse_arxiv_id(link: str) -> str:
    """Normalize any arXiv-ish URL (or bare ID) to a canonical, version-less ID."""
    link = link.strip()
    m = _ARXIV_ID.search(link)
    if not m:
        raise NotAnArxivLink(f"not an arXiv link: {link!r}")
    raw = m.group("id") or m.group("bare")
    return re.sub(r"v\d+$", "", raw)  # drop version: v1/v2 are the same paper


def canonical_url(arxiv_id: str) -> str:
    return f"https://arxiv.org/abs/{arxiv_id}"


def read_list(path: Path = PAPERS_LIST) -> list[str]:
    """The gate: every arXiv ID we are allowed to ingest, and nothing else."""
    if not path.exists():
        return []
    ids: list[str] = []
    for line in path.read_text().splitlines():
        line = line.split("#", 1)[0].strip()
        if not line:
            continue
        try:
            ids.append(parse_arxiv_id(line))
        except NotAnArxivLink:
            continue  # reported by the caller via `scraper papers --check`
        # dedupe while preserving order
    return list(dict.fromkeys(ids))


def bad_lines(path: Path = PAPERS_LIST) -> list[str]:
    if not path.exists():
        return []
    bad = []
    for line in path.read_text().splitlines():
        stripped = line.split("#", 1)[0].strip()
        if not stripped:
            continue
        try:
            parse_arxiv_id(stripped)
        except NotAnArxivLink:
            bad.append(stripped)
    return bad


def fetch_paper(fetcher: Fetcher, arxiv_id: str) -> Paper:
    """Metadata + abstract from the arXiv API; full text when an HTML rendering exists."""
    resp = fetcher.get(ARXIV_API.format(id=arxiv_id), interval=ARXIV_INTERVAL)
    feed = feedparser.parse(resp.content)
    if not feed.entries:
        raise ExtractionError(f"arXiv returned no entry for {arxiv_id}")
    e = feed.entries[0]
    if getattr(e, "title", "").strip() == "Error":
        raise ExtractionError(f"arXiv error for {arxiv_id}: {getattr(e, 'summary', '')[:120]}")

    # Body text, best source first. HTML is cleanest (real headings, tables, links);
    # PDF is the fallback for the many papers arXiv never rendered to HTML.
    fulltext, source = None, "none"
    try:
        html = fetcher.get(ARXIV_HTML.format(id=arxiv_id), interval=ARXIV_INTERVAL)
        if "html" in html.headers.get("content-type", ""):
            import trafilatura
            fulltext = trafilatura.extract(
                html.text, url=ARXIV_HTML.format(id=arxiv_id), output_format="markdown",
                include_formatting=True, include_tables=True, include_links=True,
            )
            if fulltext and len(fulltext.split()) >= MIN_FULLTEXT_WORDS:
                source = "html"
            else:
                fulltext = None  # nav chrome, not a paper — try the PDF
    except FetchError:
        pass

    if not fulltext:
        try:
            pdf = fetcher.get(ARXIV_PDF.format(id=arxiv_id), interval=ARXIV_INTERVAL)
            if "pdf" in pdf.headers.get("content-type", ""):
                text = _pdf_to_markdown(pdf.content)
                if text and len(text.split()) >= MIN_FULLTEXT_WORDS:
                    fulltext, source = text, "pdf"
        except FetchError:
            pass  # abstract-only; still worth having in the KB

    return Paper(
        arxiv_id=arxiv_id,
        title=re.sub(r"\s+", " ", e.title).strip(),
        abstract=re.sub(r"\s+", " ", e.summary).strip(),
        authors=[a.name for a in getattr(e, "authors", [])],
        published=e.published[:10],
        updated=getattr(e, "updated", "")[:10] or None,
        categories=[t["term"] for t in getattr(e, "tags", [])],
        comment=getattr(e, "arxiv_comment", None),
        fulltext_md=fulltext,
        fulltext_source=source,
    )


def to_article(paper: Paper) -> tuple[Article, dict, str]:
    """Render a Paper into the (Article, extra_frontmatter, body) shape write_inbox wants."""
    parts = [f"**Authors:** {', '.join(paper.authors) or 'unknown'}",
             f"**arXiv:** [{paper.arxiv_id}]({canonical_url(paper.arxiv_id)}) · "
             f"{', '.join(paper.categories)}"]
    if paper.comment:
        parts.append(f"**Comment:** {paper.comment}")
    parts += ["", "## Abstract", "", paper.abstract]
    if paper.fulltext_md:
        parts += ["", "---", "", paper.fulltext_md]
    body = "\n".join(parts)

    article = Article(
        url=canonical_url(paper.arxiv_id),
        title=paper.title,
        body_md=body,
        author=", ".join(paper.authors[:8]) + (" et al." if len(paper.authors) > 8 else ""),
        published=paper.published,
        description=paper.abstract[:300],
        words=len(body.split()),
    )
    extra = {
        "arxiv_id": paper.arxiv_id,
        "categories": paper.categories,
        "fulltext": paper.fulltext_source,  # html | pdf | none
        "updated": paper.updated,
    }
    return article, extra, body
