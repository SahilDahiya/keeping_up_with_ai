---
title: How to improve your golden datasets with human review
topic: evals-observability
subtopic: testing
secondary_topics: []
summary: Explains how human review improves golden datasets for evals by correcting
  labels, surfacing ambiguity, and tightening quality standards.
source: braintrust
url: https://www.braintrust.dev/blog/human-review-golden-datasets
author: Braintrust Team
published: '2026-05-21'
fetched: '2026-07-11T04:32:43Z'
classifier: codex
taxonomy_rev: 1
words: 1576
content_sha256: 31264af3d167000596ce92c86dcacced546f4c970a00ae53c99fb4d1f0037839
---

# How to improve your golden datasets with human review

21 May 2026Ornella Altunyan9 min

When you're building an eval workflow, it's easy to forget that human expertise is one of the most important inputs. If you don't have some validation of what good looks like for your AI product, then it's impossible to judge whether the quality of what you're building improved or regressed, because you have nothing authoritative to compare outputs against.

Identifying that information and integrating it into your eval workflow usually requires domain knowledge, policy expertise, and customer expectations that aren't fully captured by prompts, heuristics, or model confidence. This is where [human review](https://www.braintrust.dev/docs/annotate/human-review) comes in.

The goal of adding human review to your eval process is to turn your production traces into [golden datasets](https://www.braintrust.dev/docs/annotate/datasets) that are updated over time, and that can help tune your scorers as your data changes. The flow looks something like this.

Capture behavior

Label with expertise

Score in evals

Ship, fix, or block

With human review, this flow can help you build a dataset you can run in CI, a dashboard you monitor over time, and a queue that keeps feeding new edge cases back into the dataset.

At any real production scale, you can't get to the labeling step by browsing every trace yourself. The traces need to be categorized first, by failure mode, intent, sentiment, and so on, so a reviewer can focus on patterns instead of individual events. [Topics](https://www.braintrust.dev/docs/observe/topics) does that automatically, clustering production traces into named categories and persisting those classifications as SQL-queryable labels on every trace. Human review then layers on top, applying expertise to confirm the right output on each pattern Topics has surfaced.

`expected` and why it mattersThe `expected` value is how you can specify a "correct" answer that reflects human expertise outside of whatever model you're using or AI product you're building. Knowing the output you want the model to produce allows you to improve your scorers as you get more production data.

When writing `expected` values, you'll need to:

- Include the full response the model should produce, or the specific value you want returned.
- Make sure format, tone, schema, citations, and safety behavior align with what your app expects in production.
- Use deterministic targets, like "return JSON with keys X/Y/Z" which is easier to score than "a helpful answer."
- If a single trace exercises multiple behaviors, consider splitting into multiple dataset rows so each has a crisp `expected`.

It's important to keep `expected` clean. Any supporting details or source material should be stored in metadata or reference fields, rather than `expected` itself. The same goes for the context needed to justify why your `expected` value is correct. This keeps `expected` comparable across reviewers and makes the scoring signal clearer.

The workflow of applying human review to your eval process should follow a pattern that takes traces, puts them into a dataset, and then tests against the `expected` value from the human review.

First, the human reviewer picks a "bad" or "interesting" trace that's worth digging into. In most cases this will be a notable failure, an edge case, or a representative example from a Topics cluster. The reviewer will then copy the trace into a target dataset. This could be an existing golden dataset, a regression suite, or something similar. Finally, the reviewer fills in the `expected` value, based on their subject matter expertise, past experience, or familiarity with the business' ground truth. Essentially, this is the answer the model should have produced.

The quality bar for human reviewers should be high. If you can't confidently write the `expected` from available sources, it's better to consult additional subject matter experts rather than guessing. If there are multiple outputs that could be "right," or if the ground truth is complex enough to warrant different correct outputs, you may need to narrow the task and make it more specific, or encode acceptable variance in your scorer, like a [rubric-based judge](https://www.braintrust.dev/docs/evaluate/llm-as-a-judge).

To start configuring human review in Braintrust, you'll need to define a clear rubric at the project level. In your Braintrust **Project**, go to **Settings**, then **Human review**, and define the review scores you want captured.

Pick field types that match the judgment you need:

- **Pass/fail**for the fastest decisions and cleanest metrics (for example,- `is_correct`,- `needs_fix`).
- **Categorical**fields when you want a consistent taxonomy (for example,- `failure_type = hallucination | retrieval_miss | tool_misuse | policy | formatting`).
- **Continuous sliders**for subjective dimensions (for example,- `helpfulness`,- `tone`, or- `groundedness`on a 1 to 5 scale).
- **Freeform text**fields for- `notes`or rationale.

It's best to keep the rubric short at first, and only expand once reviewers are consistent, since long rubrics reduce throughput and increase inconsistency. To make the rubric usable in practice, add short definitions and examples directly in the field descriptions (what "good" and "bad" look like), and ensure each field maps to an action. For example, `needs_fix` should drive triage and ownership, and `failure_type` should map to a playbook or a responsible team.

Once the rubric exists, use review queues and assignments to route traces to the right subject matter experts. When you flag spans or logs for review from **Logs/Traces**, you can either assign them directly to a specific reviewer or leave them unassigned within a shared queue. Topics labels are a useful filter for routing, since you can send all traces tagged with a given failure mode or task category to the team that owns that area. This queue structure lets you maintain a clean operating rhythm.

A triage queue that quickly decides "ignore vs. needs review vs. duplicate" will help you tackle critical issues fast. When Topics is in place, this triage step often becomes about confirming or refining the labels Topics has already applied, rather than starting from zero. An SME queue that fills in ground truth fields like `expected` and `is_correct` will make sure that real-world expertise is being applied rigorously. A calibration queue where multiple reviewers periodically score the same items will keep the rubric aligned.

After traces have been reviewed initially through these queues, treat human review scores as the primary lever for curation. You can filter reviewed logs by Topics labels and human review scores to find the examples you want to "promote" into datasets. From the filtered set, add these "promoted" traces or spans to a golden dataset of durable test cases. Once promoted, run experiments against this dataset after changes, continuously add new failures, periodically prune duplicates and stale cases, and gradually convert recurring human review patterns into automated scorers so human effort stays focused on the ambiguous and novel.

Braintrust also supports [custom trace views](https://www.braintrust.dev/docs/annotate/custom-views) for capturing reviewer judgment that doesn't fit cleanly into an `expected` value. Custom trace views are embeddable React components that re-render raw traces into persona-specific review interfaces. Instead of navigating nested spans and raw JSON, reviewers see the inputs, outputs, tool calls, retrieved context, and business metadata relevant to their workflow.

Pairing custom trace views with human review lets you expose annotation affordances that a structured rubric can't express. Reviewers can apply corrections, labels, and notes directly from the interface, with those annotations written back to span metadata as queryable signals for filtering logs, curating datasets, triggering [online scorers](https://www.braintrust.dev/docs/evaluate/score-online), and regression testing. Teams typically build distinct interfaces for different reviewer personas, so each group sees only the context it needs to evaluate traces effectively.

Once you've set up human review and have enough results that meet the `expected` value, you can turn this human-reviewed ground truth into scalable, automated evaluation.

For objective checks, this often starts with heuristic scorers (exact match, regex, diffs, and schema validation) that catch clear regressions cheaply and deterministically. For more subjective dimensions you can introduce [LLM-as-judge scorers](https://www.braintrust.dev/docs/evaluate/llm-as-a-judge) that follow the same rubric language your reviewers use. Over time, it becomes especially valuable to track judge and human alignment and calibrate prompts or thresholds when they drift, which will help keep automated scoring honest as your product and data evolve.

As the dataset grows with real labeled failures, your scorers become more meaningful and regressions become easier to catch. Reviewed production failures become test cases, scorers turn those cases into metrics, and experiments and CI runs tell you whether a change improved things or broke something.

Over time, human review moves from being the primary evaluation mechanism to being a source of high-quality training signal applied to datasets and scorers that are being automatically generated by an existing eval workflow.

Though human review eventually moves towards after-the-fact quality control, you'll need to remain vigilant and avoid anti-patterns that can undermine the flywheel.

The most common anti-pattern is copying traces into a dataset but leaving `expected` blank. In that case you've saved an example, but haven't supplied a clear ground truth to check against, so the row can't function as a reliable regression test and the dataset won't strengthen your scoring signal over time.

Another issue is mixing reference material, context, or rationale directly into `expected`. That makes `expected` harder to compare across reviewers and across time, and often leads to noisy scoring because two "correct" outputs may differ only in the extra explanatory content. Keep `expected` as the clean target output, and put supporting material in metadata or separate notes fields.

Finally, avoid deferring the review workflow design. If you wait to define the rubric, ownership, and review cadence "until later," you'll accumulate lots of interesting traces but won't have a consistent labeling process that turns them into actionable test cases and scorer improvements.
