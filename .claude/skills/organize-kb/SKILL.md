---
name: organize-kb
description: Classify scraped articles waiting in kb/_inbox/ into the topic tree and rebuild indexes. Use after running `scraper update` or `scraper backfill`, or whenever kb/_inbox/ has pending files.
---

# Organize the knowledge base inbox

You are the classification stage of the kb-scraper pipeline (see DESIGN.md §2.5). The
scraper has staged extracted articles in `kb/_inbox/` with classification frontmatter
left blank. Your job: fill it in, then let the CLI do the mechanical filing.

## Steps

1. Read `kb/taxonomy.yaml`. You may ONLY use topics/subtopics defined there.
2. List `kb/_inbox/*.md`. If empty, report that and stop.
3. For each file (batch your reads — title + first ~40 lines is usually enough):
   - Decide the **primary topic + subtopic**: what is this article *fundamentally
     about*, not what does it mention. An article on evaluating multi-agent systems is
     `agents/multi-agent` with secondary `evals-observability/evaluation`, unless
     evaluation methodology is its core contribution.
   - Pick 0–2 `secondary_topics` (format `"topic/subtopic"`), conservatively: only
     topics whose researcher would genuinely want this article.
   - Write a 1–2 sentence `summary` — concrete and specific ("Benchmarks INT8 vs FP8
     quantization on H100s for Llama-70B serving"), never generic ("Discusses AI
     trends").
   - Edit the file's frontmatter: set `topic`, `subtopic`, `secondary_topics`,
     `summary`, and `classifier: claude` (leave everything else untouched).
   - Marketing fluff / pure product announcements with no engineering content: still
     classify (usually `industry/announcements`) — the KB filters by summary quality,
     not by exclusion.
   - Genuinely unsure between topics? Pick the best fit — cross-references make wrong
     folders cheap. Truly unclassifiable (not AI/engineering related at all): set
     `topic: unclassified`, `subtopic: null`, and say why in the summary.
4. Run `.venv/bin/scraper file --all` — it validates your frontmatter against the
   taxonomy, moves files into `kb/<topic>/<subtopic>/<Title>.md`, and rebuilds indexes.
   Fix anything it rejects and re-run.
5. Verify: `kb/_inbox/` empty, `.venv/bin/scraper report` clean.
6. Commit everything (`kb/` changes) with a message like
   `KB: classify N articles (M sources)` and push.

## Judgment guidance

- The taxonomy is in `kb/taxonomy.yaml`; if many articles genuinely fit no subtopic,
  note that in your final report and suggest a taxonomy addition — do NOT invent
  labels inline.
- Batch efficiency: for large backfills, process ~50–100 files per pass; classify from
  title + skim, only read deeply when ambiguous.
