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
| 3 | HTML index pagination | last resort | Paginate the listing page, collect article links via CSS selector. Currently needed by **exactly one source (modal.com, for deep backfill only)** — every other source is fully covered by tiers 1–2. |

The discovery result is a list of `(url, published_hint, lastmod_hint)` tuples. Feeds also
provide title/summary hints that are carried forward.

**Verified coverage (2026-07-10):** all 16 sources are reachable via tier 1 and/or tier 2
(see §3 table). 10 expose an RSS/Atom feed; 15 expose a sitemap; modal.com is the sole
feed-only source. Tier 3 is therefore a Phase-2 nicety, not a Phase-1 dependency.

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
    sitemap: https://www.anthropic.com/sitemap.xml   # verified; no feed exposed
    include_prefixes: ["/engineering/"]
    discovery: [sitemap]              # tiers to try, in order
    tags: [agents, llm-vendors]       # render defaults to http (no JS needed)

  - slug: latent-space
    name: Latent Space
    home: https://www.latent.space/
    feed: https://www.latent.space/feed   # pinned override (Substack)
    discovery: [feed, sitemap]
    tags: [podcast, newsletter]
```

Mechanism per source — **verified 2026-07-10** by probing each site (feed autodiscovery,
`robots.txt` → sitemap, and common feed paths). All URLs below returned `200` with an
XML content-type. The run report still flags any source where discovery later returns
nothing (feeds move, sites get redesigned).

| Source | Update feed (verified) | Backfill (verified) | Filter needed | Render |
|---|---|---|---|---|
| sierra.ai/blog/engineering | `sierra.ai/rss.xml` | `sierra.ai/sitemap.xml` | **yes** — feed is site-wide; keep `/blog/` (engineering subset, see note) | http |
| cresta.com/blog | — (none exposed) | `cresta.com/sitemap.xml` | **yes** — multilingual `urlset`; keep `/blog/`, drop `/es`, `/de` & hreflang dupes | http |
| baseten.co/blog | — (none exposed) | `www.baseten.co/sitemap.xml` | keep `/blog/` prefix | http |
| anthropic.com/engineering | — (none exposed) | `www.anthropic.com/sitemap.xml` (**25** `/engineering/` URLs) | keep `/engineering/` | http ✓ (no JS needed) |
| developers.openai.com/blog | `developers.openai.com/rss.xml` | `developers.openai.com/sitemap-index.xml` | keep `/blog/` | http |
| blog.cloudflare.com/tag/ai/ | `blog.cloudflare.com/tag/ai/rss` | tag feed pagination (`/tag/ai/rss` + `?page=`) | AI tag only (by design) | http |
| fireworks.ai/blog | — (none exposed) | `fireworks.ai/sitemap.xml` | keep `/blog/` | http |
| together.ai/blog | `www.together.ai/blog/rss.xml` | `www.together.ai/sitemap.xml` | keep `/blog/` | http |
| modal.com/blog | `modal.com/blog/atom.xml` | **feed only — no sitemap** (see note) | — | http |
| braintrust.dev/blog | — (none exposed) | `www.braintrust.dev/sitemap.xml` | keep `/blog/` | http |
| langfuse.com/blog | — (none exposed) | `langfuse.com/sitemap.xml` | keep `/blog/` | http |
| blog.langchain.com | `blog.langchain.com/rss.xml` | `blog.langchain.com/sitemap.xml` (Ghost `sitemap-posts.xml`) | — | http |
| arize.com/blog | `arize.com/feed/` | `arize.com/sitemap_index.xml` (WP) | keep `/blog/` | http |
| simonwillison.net | `simonwillison.net/atom/everything/` | `simonwillison.net/sitemap.xml` (**16,746 URLs**) | see note | http |
| huyenchip.com/blog | `huyenchip.com/feed.xml` | `huyenchip.com/sitemap.xml` | keep `/blog/` | http |
| latent.space | `www.latent.space/feed` | `www.latent.space/sitemap.xml` | — | http |

Notes:
- **No Playwright is needed for any of the 16.** Discovery relies entirely on XML
  feeds/sitemaps (served as static XML), and article HTML for the "custom Next.js" sites
  (sierra, anthropic, baseten, fireworks, braintrust) fetched over plain HTTP returned
  full server-rendered content in spot checks. `render: playwright` stays in the config
  schema as a per-source escape hatch, but ships **off**. Re-evaluate only if a specific
  source's extraction comes back empty.
- **6 of 16 expose no update feed** (cresta, baseten, anthropic, fireworks, braintrust,
  langfuse). For these, "update" = re-fetch the sitemap and diff against `state.db` using
  `lastmod`. Sitemaps are cheap (one request) so a daily sitemap diff is fine; these
  sources simply skip the feed tier.
- **Feeds are excerpt-only.** Verified: `blog.langchain.com/rss.xml` has no
  `content:encoded`. So the pipeline **always fetches the full article page** and never
  stores the feed body — feeds are used only as a URL+date discovery source, same role as
  sitemaps. (Where a feed *does* carry full content, that's a free bonus we can use to skip
  a fetch, but the design never depends on it.)
- **modal.com is the one weak spot:** no sitemap (`/sitemap.xml` → 404), only
  `/blog/atom.xml` which carries just recent posts. Update coverage is fine; **deep
  backfill isn't possible from the feed alone.** Phase-2 fallback for modal only: paginate
  the `/blog` HTML index for older links. Accept shallow history until then.
- **sierra** `rss.xml` is the whole company blog, not just engineering. The `/blog/engineering`
  URL the user gave is a *view*, not a separate path — individual posts live at
  `/blog/<slug>`. Start by keeping all `/blog/` posts (the blog is small and AI-focused);
  if non-engineering marketing posts intrude, add a per-source category/keyword filter.
- **cresta** sitemap includes `/es`, `/de` locale trees and `hreflang` alternate entries.
  Filter to canonical English `/blog/` URLs and de-dupe.
- **Cloudflare** tag feed covers only the AI tag, as requested — not the whole firehose.
  Backfill uses the paginated tag RSS rather than the site-wide sitemap.
- **Simon Willison** is very high-volume — the sitemap lists **16,746 URLs** (blog posts +
  link-blog "blogmarks" + quotations + TILs). This one source would dominate the KB.
  Decision for Phase 1: ingest **`/YYYY/` blog entries + TILs only** via a URL-pattern
  filter, and/or `--since 2023-01-01`, skipping the link-blog firehose. Both are YAML knobs.
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
   + indexes. Onboard **all 16 sources** — verified reachable over plain HTTP with no JS
   rendering — using the feed/sitemap URLs in §3. Daily update job. (simonwillison.net
   ingests filtered/`--since`-bounded; modal.com is feed-depth-limited.)
2. **Phase 2 — Deep backfill + quality.** Full sitemap backfill; modal.com HTML-index
   pagination (the one tier-3 case); extraction-quality passes (code blocks, authors)
   per source; `scraper report`.
3. **Phase 3 — Research ergonomics (optional).** FTS5 index, per-week digest generation
   ("what's new this week across the KB"), embeddings if grep ever falls short.

---

## 7. Risks & open questions

- **Bot protection** — *not observed on any of the 16 as of 2026-07-10.* All feeds,
  sitemaps, and spot-checked article pages returned `200` over plain HTTP. Risk is future
  drift (a site adds a Cloudflare/Vercel challenge); mitigation is the `render: playwright`
  per-source escape hatch already in the schema, flagged by the run report if a fetch
  starts coming back empty.
- **Environment / runtime networking.** Earlier design work ran in a sandbox whose proxy
  blocked these domains (CONNECT 403); the current dev machine reaches all 16 fine. The
  scheduled job still needs egress to these domains wherever it runs — GitHub Actions
  (unrestricted egress) is the recommended host for the daily job. The design assumes
  nothing about where it runs.
- **Feed history depth varies / 6 sources have no feed** — backfill must not rely on
  feeds; the sitemap is the authority for the past. modal.com has neither a deep feed nor
  a sitemap (tier-3 pagination in Phase 2).
- **KB size in git**: simonwillison.net's sitemap alone is **16,746 URLs**. Phase 1 ships
  a URL-pattern + `--since` filter for it (blog posts + TILs, not the link-blog). Revisit
  at Phase 2 whether the whole `kb/` tree should split into its own repo / git-lfs.
- **Content updates**: re-fetching everything to detect silent edits is wasteful; we rely
  on sitemap `lastmod` + feed `updated`, accepting that some silent edits are missed.
```
