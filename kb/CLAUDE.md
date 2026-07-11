# Knowledge base: AI engineering blogs

This directory is a research knowledge base of articles scraped from ~16 AI engineering
blogs (Anthropic, OpenAI devs, LangChain, Simon Willison, Latent Space, …). Everything
is plain markdown with YAML frontmatter — research it with grep/glob/read.

## Layout

- `<topic>/<subtopic>/<Article Title>.md` — one file per article, filed by **primary
  topic**. The topic tree is defined in `taxonomy.yaml`.
- `<topic>/index.md` — reverse-chron survey of that topic with one-line summaries,
  plus an "Also relevant" section for articles filed elsewhere whose
  `secondary_topics` point here. **Start topic research here.**
- `_sources/<source>.md` — reverse-chron view of everything from one blog.
- `catalog.jsonl` — one JSON object per article
  (`topic, subtopic, secondary_topics, source, url, date, title, path, summary, words`).
  Use for programmatic queries: `jq 'select(.topic=="agents")' catalog.jsonl`.
- `_inbox/` — scraped but not yet classified. Not part of the researched KB;
  cleared by Codex using `AGENTS.md` or by Claude Code's `/organize-kb` skill.
- `unclassified/` — articles the classifier wasn't confident about.

## Frontmatter schema

`title, topic, subtopic, secondary_topics (list of "topic/subtopic"), summary, source,
url, author, published (ISO date), fetched, classifier, taxonomy_rev, words,
content_sha256`

## Research recipes

- What's new in a topic → head `<topic>/index.md` (already reverse-chron).
- Everything one blog said → `_sources/<slug>.md`.
- Cross-topic keyword search → `grep -ril "keyword" kb/ --include="*.md"`.
- Time-bounded queries → `jq 'select(.date >= "2026-01-01")' catalog.jsonl`.
- Always cite the `url` from frontmatter when quoting an article.

## Rules

- `index.md` files, `_sources/`, and `catalog.jsonl` are **generated** — never
  hand-edit; run `scraper reindex` after any manual file move.
- If an article looks misfiled, fix its `topic`/`subtopic` frontmatter, move the file
  to the matching folder, and run `scraper reindex`.
