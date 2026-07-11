# Knowledge base instructions for Codex

This directory is a research knowledge base of AI engineering articles. Everything is
plain markdown with YAML frontmatter.

## Layout

- `<topic>/<subtopic>/<Article Title>.md` is one filed article.
- `taxonomy.yaml` defines the allowed topic tree.
- `_inbox/` contains scraped articles waiting for classification.
- `_sources/*.md`, `catalog.jsonl`, and `*/index.md` are generated from frontmatter.
- `unclassified/` is the holding area for articles that do not fit the taxonomy.

## Research

Start with topic indexes for browsing and use `catalog.jsonl` for programmatic
filtering. Cite the source `url` from article frontmatter when quoting or summarizing
an article for a user.

Useful commands:

```bash
rg -n "keyword" kb --glob '*.md'
jq 'select(.topic=="agents")' kb/catalog.jsonl
jq 'select(.date >= "2026-01-01")' kb/catalog.jsonl
```

## Classification

For files in `_inbox/`, follow the root `AGENTS.md` organizing workflow. Use only
topics/subtopics from `taxonomy.yaml`.

Triage before classification. Skip archive pages, promotions, low-detail release
notes, company-news posts, event listicles, broad business commentary, duplicates,
off-topic pages, and too-shallow pages with:

```bash
.venv/bin/scraper skip <inbox-file> --reason <reason>
```

For kept articles, set `classifier: codex`, then run:

```bash
.venv/bin/scraper file --all
```

Never hand-edit generated indexes or `catalog.jsonl`; run `.venv/bin/scraper reindex`
after manual article moves or frontmatter fixes.
