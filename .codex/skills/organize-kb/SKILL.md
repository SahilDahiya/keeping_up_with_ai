---
name: organize-kb
description: Classify scraped articles waiting in kb/_inbox/ into the topic tree and rebuild indexes. Use after running `scraper update` or `scraper backfill`, or whenever kb/_inbox/ has pending files.
---

# Organize the knowledge base inbox with Codex

The scraper stages extracted articles in `kb/_inbox/` with classification
frontmatter left blank. Triage low-signal items out first, fill in classification
fields for the articles worth keeping, then let the CLI handle filing, validation,
and index regeneration.

## Steps

1. Read `kb/taxonomy.yaml`. Use only topics/subtopics defined there.
2. List `kb/_inbox/*.md`. If empty, report that and stop.
3. Process articles in batches of about 50-100 unless the user asks otherwise.
   Title, frontmatter, and the first 40-80 lines are usually enough; read deeper
   when ambiguous.
4. Triage each file before classification. Keep only durable AI engineering content:
   agents, evals, observability, inference, model behavior, RAG, prompt/context
   engineering, production architecture, deployment, security, cost, reliability, or
   concrete implementation case studies.
5. Skip junk with `.venv/bin/scraper skip PATH --reason REASON`. Valid reasons are
   `archive-page`, `promotion`, `company-news`, `release-note-lite`, `event-list`,
   `thought-leadership-lite`, `duplicate`, `too-shallow`, and `off-topic`.
6. Skip:
   - archive/category/tag/listing pages
   - pure funding, hiring, awards, certifications, or partnership announcements
   - generic product announcements without technical detail
   - release notes that only list UI/product changes
   - event/conference listicles
   - broad AI ethics/business commentary without engineering takeaways
7. For each kept file:
   - Decide the primary `topic` and `subtopic` by what the article is fundamentally
     about.
   - Pick 0-2 `secondary_topics` in `topic/subtopic` form.
   - Write a concrete 1-2 sentence `summary`.
   - Set `classifier: codex`.
   - Leave all other frontmatter untouched.
8. Run `.venv/bin/scraper file --all`. It validates frontmatter, moves classified
   files into `kb/<topic>/<subtopic>/`, updates `state.db`, and rebuilds indexes.
9. Fix any rejected files and rerun `.venv/bin/scraper file --all`.
10. Verify with `.venv/bin/scraper report` and an inbox count.

## Judgment guidance

- Choose the primary topic by the core contribution, not every mentioned concept.
- Use secondary topics only when a researcher in that topic would genuinely want the
  article.
- A release or announcement is worth filing only if it contains engineering substance:
  architecture, evals, model behavior, infrastructure, API design, reliability,
  security, cost, or concrete production lessons.
- Truly unrelated or unclassifiable articles go to `topic: unclassified`,
  `subtopic: null`, with the reason in `summary`.
- If many articles do not fit the taxonomy, finish the batch with the best available
  labels and suggest a taxonomy change separately.
