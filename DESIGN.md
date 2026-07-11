# AI Engineering Blog Scraper — Design

**Goal:** keep up with the AI engineering world by continuously scraping a curated set of
blogs, backfilling their archives, and indexing everything into a plain-file knowledge base
that an agent can research the same way it researches a codebase (grep, glob, read).

Two workloads, one pipeline:

1. **Backfill** — one-time (per source) crawl of the full archive, back to the oldest post.
2. **Update** — cheap, frequent incremental runs (daily) that pick up only new/changed posts.

---

## 1. Guiding principles

- **Feeds and sitemaps first, HTML scraping last.** Most of these blogs expose RSS/Atom
  feeds (great for incremental updates) and/or `sitemap.xml` (great for backfill, includes
  `lastmod` dates). HTML parsing is brittle and only used as a fallback.
- **Config-driven, not code-per-site.** One generic engine + a `sources.yaml` registry.
  Adding blog #17 should be a 5-line YAML edit, not a new module.
- **Self-healing discovery.** At runtime the scraper autodiscovers feeds
  (`<link rel="alternate">`, common paths like `/feed`, `/rss/`, `/atom.xml`, `/feed.xml`,
  then `robots.txt` → sitemap). Per-source overrides in YAML only pin what autodiscovery
  can't find.
- **Idempotent and resumable.** Every run can be killed and restarted. State is keyed by
  canonical URL; already-fetched, unchanged articles are never re-downloaded
  (conditional GET with ETag/Last-Modified, plus content hashing).
- **The knowledge base is the product.** Plain markdown with YAML frontmatter + small
  index files. No database required to *read* it — an agent with file tools is the query
  engine. (Structured indexes exist alongside for programmatic use.)
- **Polite.** Respect `robots.txt`, per-domain rate limits (~1 request / 2s), exponential
  backoff on 429/5xx, honest User-Agent, and every stored article keeps full source
  attribution. Public content only.

---

## 2. Architecture

```
                ┌────────────────────────────────────────────────┐
 sources.yaml ─▶│ 1. DISCOVER   feed / sitemap / html-index      │─▶ article URLs + dates
                └────────────────────────────────────────────────┘
                ┌────────────────────────────────────────────────┐
   state.db  ─▶ │ 2. PLAN       diff against seen set            │─▶ fetch queue
                └────────────────────────────────────────────────┘
                ┌────────────────────────────────────────────────┐
                │ 3. FETCH      rate-limited httpx; Playwright   │─▶ raw HTML
                │               fallback for JS-rendered sites   │
                └────────────────────────────────────────────────┘
                ┌────────────────────────────────────────────────┐
                │ 4. EXTRACT    trafilatura → markdown + metadata│─▶ article record
                └────────────────────────────────────────────────┘
                ┌────────────────────────────────────────────────┐
                │ 5. STORE      kb/ file tree + frontmatter      │
                │ 6. INDEX      per-source index.md, catalog.jsonl│
                └────────────────────────────────────────────────┘
```

### 2.1 Discover

Per source, tiered — first tier that works wins; results are merged for backfill:

| Tier | Mechanism | Used for | Notes |
|------|-----------|----------|-------|
| 1 | RSS/Atom feed | updates (+ recent backfill) | Cheapest; usually only last 10–50 posts |
| 2 | `sitemap.xml` | backfill + weekly safety net | Full history, `lastmod` timestamps; filter URLs by blog path prefix (e.g. `/blog/`) |
| 3 | HTML index pagination | last resort | Paginate the listing page, collect article links via CSS selector; Playwright if listing is client-rendered |

The discovery result is a list of `(url, published_hint, lastmod_hint)` tuples. Feeds also
provide title/summary hints that are carried forward.

### 2.2 Plan

Diff discovered URLs against `state.db` (SQLite):

- unknown URL → fetch
- known URL with newer `lastmod` than stored → re-fetch (article was updated)
- otherwise skip

`state.db` schema (single table): `url_canonical (pk), source, first_seen, last_fetched,
etag, last_modified, content_sha256, kb_path, status`.
SQLite is scraper-internal bookkeeping only — the knowledge base never depends on it.

### 2.3 Fetch

- `httpx` with HTTP/2, per-domain token bucket (default 1 req / 2s, configurable per source),
  retries with exponential backoff + jitter, 20s timeout.
- Conditional GET (`If-None-Match` / `If-Modified-Since`) on re-fetches.
- **JS-rendered / bot-protected sites** (expected: sierra.ai, anthropic.com, possibly
  baseten.co, fireworks.ai): mark `render: playwright` in `sources.yaml`; a headless
  Chromium fetches the page and returns settled DOM HTML. Playwright is the exception
  path, not the default — sitemap-discovered URLs often serve static HTML even when the
  index page doesn't.
- Raw HTML is cached to `cache/raw/<sha of url>.html` during a run so extraction can be
  re-run without re-fetching while iterating on the extractor.

### 2.4 Extract

- Primary: **trafilatura** (best-in-class boilerplate removal, outputs markdown, pulls
  title/author/date/description from meta tags and JSON-LD).
- Metadata merge order: JSON-LD / OpenGraph meta → feed entry hints → URL patterns
  (many blogs put dates in slugs) → trafilatura guesses.
- Per-source CSS selector overrides in YAML for the rare site trafilatura mangles.
- Quality gate: reject extractions under ~400 chars or missing a title → flag in run
  report instead of writing junk into the KB.
- Code blocks matter for this audience — verify fenced code survives extraction per
  source during rollout; fall back to targeted `<article>`-subtree conversion
  (html→markdown via markdownify on a selector) where trafilatura drops them.

### 2.5 Store — knowledge base layout

One markdown file per article. Flat, predictable, greppable:

```
kb/
  CLAUDE.md                      # tells research agents how this KB is organized
  catalog.jsonl                  # 1 line per article: {source, url, date, title, path, tags, words}
  <source-slug>/                 # e.g. anthropic-engineering/, simon-willison/
    index.md                     # reverse-chron table: date | title | relative path
    2026/
      2026-05-14--how-we-built-x.md
    2025/
      ...
```

Article file format:

```markdown
---
source: anthropic-engineering
url: https://www.anthropic.com/engineering/how-we-built-x
title: "How we built X"
author: "..."
published: 2026-05-14
fetched: 2026-07-11T04:20:00Z
tags: [agents, evals]
words: 2140
content_sha256: ab12…
---

# How we built X

...clean markdown body, code blocks preserved...
```

- Filename: `YYYY-MM-DD--<slug>.md` (slug from URL; date `0000-00-00` prefix replaced by
  `undated/` folder if truly unknown — rare).
- Images are **not** downloaded (text KB); image URLs remain as absolute links in the
  markdown.
- `index.md` and `catalog.jsonl` are regenerated from frontmatter after every run
  (derived data, never hand-edited).
- The whole `kb/` tree is committed to git → history, diffs of updated articles, and free
  sync/backup. If volume ever becomes a problem (Simon Willison alone is thousands of
  posts), `kb/` moves to its own repo or a git-lfs/object-store setup — layout unchanged.

### 2.6 Index / research layer

Phase 1 deliberately keeps this minimal, because agents are already good at
grep-and-read over well-organized markdown:

- `kb/CLAUDE.md` — explains layout, frontmatter schema, and research recipes
  ("newest posts: head each source's index.md"; "topic search: grep -ril across kb/").
- `catalog.jsonl` — one JSON object per article for programmatic filtering
  (`jq 'select(.tags[]=="inference")' `).

Phase 3 (optional, only if grep proves insufficient): SQLite FTS5 full-text index and/or
local embeddings for semantic search — built *from* the markdown, always regenerable.

---

## 3. Source registry

`sources.yaml` — the single place sites are defined. Shape:

```yaml
defaults:
  rate_limit_seconds: 2
  render: http            # http | playwright

sources:
  - slug: anthropic-engineering
    name: Anthropic Engineering
    home: https://www.anthropic.com/engineering
    include_prefixes: ["/engineering/"]
    discovery: [feed, sitemap]        # tiers to try, in order
    render: playwright                # expected bot protection
    tags: [agents, llm-vendors]

  - slug: latent-space
    name: Latent Space
    home: https://www.latent.space/
    feed: https://www.latent.space/feed   # pinned override (Substack)
    discovery: [feed, sitemap]
    tags: [podcast, newsletter]
```

Expected mechanism per source (educated defaults — **autodiscovery verifies each at
first run**, and the run report flags any source where discovery found nothing):

| Source | Platform (expected) | Update path | Backfill path | Render |
|---|---|---|---|---|
| sierra.ai/blog/engineering | Next.js custom | sitemap | sitemap | playwright likely |
| cresta.com/blog | WordPress | `/feed/` | wp-sitemap | http |
| baseten.co/blog | Next.js/headless CMS | sitemap | sitemap | maybe |
| anthropic.com/engineering | Next.js custom | sitemap | sitemap | playwright likely |
| developers.openai.com/blog | custom | rss (autodiscover) | sitemap | http |
| blog.cloudflare.com/tag/ai/ | Ghost | `/tag/ai/rss/` | tag pagination | http |
| fireworks.ai/blog | Next.js | sitemap | sitemap | maybe |
| together.ai/blog | Webflow-ish | sitemap | sitemap | http |
| modal.com/blog | custom | sitemap | sitemap | http |
| braintrust.dev/blog | Next.js | sitemap | sitemap | maybe |
| langfuse.com/blog | Nextra | autodiscover | sitemap | http |
| blog.langchain.com | Ghost | `/rss/` | sitemap | http |
| arize.com/blog | WordPress | `/blog/feed/` | wp-sitemap | http |
| simonwillison.net | Django (custom) | `/atom/everything/` | archive pages / sitemap | http |
| huyenchip.com/blog | Jekyll | `/feed.xml` | sitemap | http |
| latent.space | Substack | `/feed` | `/archive` + sitemap | http |

Notes:
- **Cloudflare tag feed** covers only the AI tag, as requested — not the whole firehose.
- **Simon Willison** is high-volume (posts + link blog + TILs). Start with everything;
  a `min_words` or entry-type filter per source is a knob in YAML if it drowns the KB.
- **Latent Space** is Substack: feed covers essays and podcast episodes (episode pages
  include full show notes, which extract fine).

---

## 4. CLI & scheduling

```
scraper discover [--source SLUG]     # dry-run: show what each tier finds, verify config
scraper backfill [--source SLUG] [--since 2020-01-01]
scraper update   [--source SLUG]     # feeds + state diff; the daily job
scraper reindex                      # rebuild index.md + catalog.jsonl from frontmatter
scraper report                       # last-run stats: new / updated / failed per source
```

- **Daily update** via cron or a GitHub Actions workflow (`schedule:`) that runs
  `scraper update`, commits new KB files, and pushes. Weekly job re-runs sitemap
  discovery as a safety net for posts that never hit a feed.
- Backfill is run once per source, oldest-first, resumable (state.db).
- Run report lists per-source counts and **loudly flags** empty discovery or extraction
  failures — silent staleness is the main failure mode for a "keep up with X" system,
  so a source producing zero items for N consecutive runs is an error, not a no-op.

---

## 5. Tech stack

Python 3.12. Small, boring dependencies:

| Concern | Choice |
|---|---|
| HTTP | `httpx` (HTTP/2, async) |
| Feeds | `feedparser` |
| Sitemaps / robots | `usp`-style parsing via stdlib + `httpx` (tiny custom module) |
| Extraction | `trafilatura` (+ `markdownify` fallback) |
| HTML parsing | `selectolax` |
| JS rendering | `playwright` (chromium), only for `render: playwright` sources |
| State | `sqlite3` (stdlib) |
| Config | `PyYAML` + `pydantic` models |
| CLI | `typer` |

Repo layout:

```
scraper/
  __main__.py        # typer CLI
  config.py          # sources.yaml loading + pydantic models
  discover/          # feed.py, sitemap.py, htmlindex.py
  fetch.py           # rate limiting, retries, conditional GET, playwright bridge
  extract.py         # trafilatura pipeline + per-source overrides
  store.py           # kb/ writer: frontmatter, slugs, layout
  index.py           # index.md + catalog.jsonl generation
  state.py           # sqlite wrapper
sources.yaml
kb/                  # the knowledge base (committed)
tests/               # extraction fixtures: saved HTML → expected markdown, per source
```

---

## 6. Phased plan

1. **Phase 1 — MVP (feeds + sitemaps, http-only).** Engine + `sources.yaml` + KB writer
   + indexes. Onboard the ~12 sources that don't need JS rendering. Daily update job.
2. **Phase 2 — Backfill + hard sites.** Sitemap backfill for all sources; Playwright
   path for the Next.js/bot-protected ones; extraction-quality passes (code blocks,
   authors) per source; `scraper report`.
3. **Phase 3 — Research ergonomics (optional).** FTS5 index, per-week digest generation
   ("what's new this week across the KB"), embeddings if grep ever falls short.

---

## 7. Risks & open questions

- **Bot protection (Cloudflare/Vercel challenges)** on anthropic.com and others may block
  plain HTTP; Playwright with a real Chromium usually passes, but if a source hard-blocks,
  the fallback is feed-only coverage for it (accept shallow history) — flagged in the run
  report either way.
- **This remote environment's network policy currently blocks all 16 blog domains**
  (CONNECT 403 at the proxy — verified during design). Implementation and the scheduled
  job need either an updated environment network policy, GitHub Actions, or a local run.
  The design assumes nothing about where it runs.
- **Feed history depth varies** — backfill must not rely on feeds; sitemap is the
  authority for the past.
- **KB size in git**: full backfill of simonwillison.net is likely 10k+ files. Decide at
  Phase 2 whether to cap backfill depth per source (e.g. `--since 2022-01-01`) or split
  `kb/` into its own repo.
- **Content updates**: re-fetching everything to detect silent edits is wasteful; we rely
  on sitemap `lastmod` + feed `updated`, accepting that some silent edits are missed.
```
