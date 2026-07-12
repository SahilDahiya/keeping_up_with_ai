# Codex instructions for this repo

## Project shape

This repo builds a plain-file AI engineering knowledge base from a curated set of
blogs. The Python scraper discovers, fetches, and extracts articles into
`kb/_inbox/`; a coding agent then classifies those staged markdown files into the
topic tree under `kb/`.

Important files:

- `sources.yaml` defines source blogs and URL filters.
- `kb/taxonomy.yaml` is the only allowed topic/subtopic tree.
- `kb/_inbox/*.md` are scraped but not yet filed.
- `kb/<topic>/<subtopic>/*.md` are filed articles.
- `kb/catalog.jsonl`, `kb/_sources/*.md`, and `kb/**/index.md` are generated.
- `state.db`, `cache/`, `.venv/`, and `uv.lock` are local state and ignored.

## Commands

Prefer the repo virtualenv when present:

```bash
.venv/bin/scraper report
.venv/bin/scraper discover --source anthropic-engineering
.venv/bin/scraper update --source openai-devs --limit 5
.venv/bin/scraper backfill --source modal --limit 20
.venv/bin/scraper skip kb/_inbox/example.md --reason too-shallow
.venv/bin/scraper skip --pattern 'arize--blog-category-*.md' --reason archive-page
.venv/bin/scraper file --all
.venv/bin/scraper reindex
```

If `.venv/bin/scraper` is unavailable, use `uv run scraper ...`.

Before a broad scrape, check for an existing scraper process and run a small
`--source`/`--limit` command first. Broad backfills can create thousands of files.

## Organizing `kb/_inbox`

When the user asks to organize, classify, file, or clean the KB inbox, act as the
triage and classification stage:

1. Read `kb/taxonomy.yaml`. Use only topics/subtopics defined there.
2. List pending files with `find kb/_inbox -maxdepth 1 -type f -name '*.md'`.
3. Process in batches of about 50-100 files unless the user asks for a specific
   size. For each article, title/frontmatter plus the first 40-80 lines is usually
   enough; read deeper only when ambiguous.
4. Triage first. File only articles with durable AI engineering value:
   - agents, evals, observability, inference, model behavior, RAG, prompt/context
     engineering
   - production architecture, deployment, security, cost, reliability
   - concrete case studies with implementation lessons
5. Skip low-signal items before classification:
   - archive/category/tag/listing pages
   - pure funding, hiring, awards, certifications, or partnership announcements
   - generic product announcements without technical detail
   - release notes that only list UI/product changes
   - event/conference listicles
   - broad AI ethics/business commentary without engineering takeaways
   - duplicate, off-topic, or too-shallow pages
6. Use `.venv/bin/scraper skip PATH --reason REASON` for skipped items. Valid reasons
   are `archive-page`, `promotion`, `company-news`, `release-note-lite`, `event-list`,
   `thought-leadership-lite`, `duplicate`, `too-shallow`, and `off-topic`.
7. For articles that survive triage, edit only classification frontmatter:
   - `topic`
   - `subtopic`
   - `secondary_topics`
   - `summary`
   - `classifier`
8. Set `classifier: codex` for classifications done by Codex. Leave existing
   `classifier: claude` values alone unless reclassifying that article.
9. Run `.venv/bin/scraper file --all` after each batch. It validates the taxonomy,
   moves valid articles into `kb/<topic>/<subtopic>/`, updates `state.db`, and
   rebuilds indexes if anything was filed.
10. Fix rejected files and rerun the command.
11. Verify with `.venv/bin/scraper report` and an inbox count.

Classification judgment:

- Choose the primary topic by what the article is fundamentally about, not by every
  concept it mentions.
- Use 0-2 `secondary_topics` in `topic/subtopic` form, only for genuinely useful
  cross-references.
- Write concrete 1-2 sentence summaries. Avoid generic summaries like "Discusses AI."
- A release or announcement is worth filing only if it contains engineering substance:
  architecture, evals, model behavior, infrastructure, API design, reliability,
  security, cost, or concrete production lessons.
- If an article is truly unrelated or unclassifiable, use `topic: unclassified`,
  `subtopic: null`, and explain why in `summary`.

Do not hand-edit generated indexes or `catalog.jsonl`; run `scraper reindex`.
Do not claim the inbox is clear unless `kb/_inbox/` is empty and `scraper report`
matches.

## Code changes

Keep scraper changes small and config-driven. Prefer improving `sources.yaml` filters
over adding site-specific code. Use structured parsers and the existing helper APIs
instead of ad hoc text processing where possible.

When changing scraper behavior, run a narrow command such as:

```bash
.venv/bin/scraper discover --source openai-devs
.venv/bin/scraper update --source openai-devs --limit 2
```

Use broader runs only when the user asks for them.
