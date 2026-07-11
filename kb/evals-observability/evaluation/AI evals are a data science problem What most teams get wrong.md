---
title: 'AI evals are a data science problem: What most teams get wrong'
topic: evals-observability
subtopic: evaluation
secondary_topics: []
summary: Argues that AI evaluation is a data science workflow requiring careful labeling,
  slices, standards, and failure analysis rather than a simple dashboard metric.
source: arize
url: https://arize.com/blog/ai-evals-are-a-data-science-problem-what-most-teams-get-wrong/
author: Sara Verdi
published: '2026-06-30'
fetched: '2026-07-11T04:41:44Z'
classifier: codex
taxonomy_rev: 1
words: 1800
content_sha256: 4b598bb762259b545615fd44d7ea23f2d56ace165950d1f686bd19e4595a6480
---

# AI evals are a data science problem: What most teams get wrong

**Hamel Husain teaches evals, audits AI codebases, and literally wrote the course on it. Here’s what we took away from his talk at  Arize Observe 2026.**

If you’ve shipped an AI application recently, you’ve probably felt this: your eval dashboard is green, but something in production still feels off. You’re not sure what’s broken, your metrics aren’t telling you, and the fixes you’re trying don’t seem to stick.

This is where data science needs to come back into AI engineering.

**The return of the data scientist in AI engineering**

The hardest problems in agent engineering are now evaluation problems, and most teams are trying to solve them without the skill set that actually works.

[Harness engineering](https://arize.com/blog/what-is-an-agent-harness-why-harnesses-are-replacing-agent-frameworks/) is pulling data science skills back to the center of AI engineering through looking at real data, designing metrics that map to failures, validating judges against human labels, and running experiments you can trust. That loop (observe, evaluate, improve) is the same [AI improvement loop](https://arize.com/glossary/ai-improvement-loop) evals and observability exist to power.

In this post, we’ll turn that argument into a workflow for two audiences: developers who need to instrument and debug AI systems, and PMs who need to decide what quality means, which failures matter most, and when a change is safe to ship.

**Use traces as the starting point for evals**

Think about OpenAI’s write-up on harness engineering—the scaffolding like unit tests, skills, and markdown files that kept Codex on track while it built complex software over months.

Most teams read the headline and stop there. But the part people skip matters most: logs, metrics, and traces exposed to the coding agent so it could tell when it introduced a regression.

When an agent can read [traces and metrics](https://arize.com/blog/improve-ai-agents-traces-evals-harness/), it has the raw material for the same quality loop your team needs: what input came in, which retrieval or tool steps ran, what the model saw, what it returned, and where the result diverged from the expected product behavior. For a developer, that means instrumenting the system so failures are debuggable. For a PM, it means ensuring the trace exposes the context required to judge the outcome.

The [evaluation harness](https://arize.com/blog/what-is-an-evaluation-harness/) framing names the same idea for measurement: infrastructure that decides what gets evaluated, runs the scoring, and routes results into the [AI improvement loop](https://arize.com/glossary/ai-improvement-loop). We built our [eval harness comparison](https://arize.com/blog/the-best-eval-harness-for-production-ai-a-comparison/) to help teams see how different approaches stack up in production.

**A key takeaway**: before adding another generic score, make sure your harness captures enough context to answer “what failed?” and “who can judge it?” At minimum, log the user request, retrieved context, tool calls and arguments, tool results, final output, relevant metadata, and the product outcome you care about.

**The field regressed to evaluating on vibes**

Four years ago, before “AI engineering” was the label, the work looked more like classic applied machine learning: examine data in notebooks, build visualizations, align metrics with human judgment before trusting a dashboard number.

Today, a lot of the field runs on vibes. “Seems correct” passes for validation. Evals often mean asking a model if it did a good job, with no rigor behind the question. Metrics get installed from a library because a paper used them once, not because they measure a failure your system actually has.

That shows up most clearly in retrieval and evals—the corners of the stack that still feel like data science. Social feeds declare evals or RAG dead on a regular cadence. People fear what they don’t understand; such declarations are not evidence that measurement stopped mattering. [RAG evaluation](https://arize.com/blog/rag-evaluation-complete-guide-2026/) still starts the same way: trace review, failure clustering, and metrics tied to real retrieval and generation failures.

**Start with failure modes, not metric libraries**

Generic scores like hallucination, toxicity, helpfulness, and coherence can be useful guardrails, but they rarely diagnose the domain-specific failures that block a launch. A support agent may fail because it skipped escalation. A healthcare intake assistant may fail because it asked for information in the wrong order. A coding agent may fail because it fixed the symptom but broke a regression test. Those failures need named, testable evals.

Start by reviewing a small, representative sample of traces. For each example, write a plain-language note about what went wrong. Then cluster those notes into failure modes and choose the one or two failures with the highest product impact. That is the metric backlog.

Turn each priority failure into an evaluator with a narrow question: “Did the agent escalate when confidence was low?” “Did the answer cite a source that supports the claim?” “Did the tool call include the required customer ID?” Narrow, binary evals are easier to trust, easier to debug, and easier for PMs to connect to launch criteria.

The takeaway: build intuition before you automate judgment.

**Validate LLM judges like classifiers**

Another common pitfall: deploying an [LLM-as-a-judge](https://arize.com/docs/ax/evaluate/evaluators/llm-as-a-judge) from a prompt template and trusting the score because it looks authoritative.

Most teams just use an LLM judge and generate a score — a Likert scale from one to five. But a data scientist would never do this. You’d say, “We’re going to treat this like a classifier.” You have a black box producing a prediction, and you want to align it with human labels so you can see if this estimator is reliable.

Use the same discipline you would use for a classifier: create a labeled dataset, split it into train/dev/test partitions, tune the judge prompt on the training/dev examples, and keep the test set untouched until you need an honest read. Track performance by slice, not just overall score, so you can see where the judge fails.

For imbalanced failures, accuracy is a trap. A judge can look 95% accurate while missing most of the rare failures that create support tickets or compliance risk. Report precision, recall, and a confusion matrix, then inspect the disagreements with humans before you trust the judge in production.

This is where observability and evaluation need to meet. Traces tell you what happened. Human labels define what good means. Validated evaluators let you monitor that definition over time and catch regressions as traffic, prompts, tools, and retrieval data change.

**Pro tip:** At Arize, we built our [LLM-as-a-judge production guide](https://arize.com/blog/how-to-build-llm-as-a-judge-evaluators-that-hold-up-in-production/) around this same loop: pull representative examples, annotate with labels your team actually uses, run the judge, inspect disagreements in Phoenix, tighten criteria, log results back to traces. Observability shows what happened; evaluation tells you whether it was good enough.

**Design test sets around expected failures**

Synthetic data should start from hypotheses, not volume. Pick dimensions that represent real risk: feature, scenario, persona, locale, policy constraint, data freshness, tool availability, or adversarial user behavior. Then generate examples that exercise those dimensions and clean the set the way you would clean any other evaluation dataset.

(We walk through that curation step in our guide on [creating and validating synthetic datasets](https://arize.com/blog/creating-and-validating-synthetic-datasets-for-llm-evaluation-experimentation/)—synthetic volume is useless without [dataset curation](https://arize.com/glossary/dataset-curation) discipline.)

Metric design should be just as simple. Avoid bundling an entire rubric into one judge or treating a 3.7 as an obvious ship/no-ship signal. [Binary evals](https://arize.com/blog/testing-binary-vs-score-llm-evals-on-the-latest-models/) are often the right default: pass or fail, aligned to an actionable failure mode.

**PMs and domain experts should label your evals, not engineers**

Engineers can build the labeling workflow, but they should not be the only people deciding what good looks like. PMs and domain experts are closest to user expectations, policy requirements, brand voice, and business tradeoffs. Their job is to turn product judgment into examples, labels, and rubrics the system can use.

Even the rubric itself isn’t as stable as teams assume. [Research on criteria drift](https://arxiv.org/abs/2404.12272) by Shreya Shankar and colleagues found that people refine what they want significantly after reviewing traces. The rubric is an output of error analysis, not a prerequisite for it. You can’t write it completely before you look at data.

That raises the obvious question: if labeling is this involved, can you just automate it? Can you just get Claude to do it? No. Claude can’t read your mind. Claude doesn’t know what good and bad is.

LLMs can help pre-label obvious cases, summarize disagreement patterns, and draft candidate rubrics. They cannot decide your taste, risk tolerance, or customer promise for you.

**Remember:** [keep humans-in-the-loop](https://arize.com/glossary/human-in-the-loop) until the judge is validated against the people whose judgment matters.

**Common anti-patterns to fix before you trust the dashboard**

A rapid-fire list of pitfalls worth turning into a checklist: cosine similarity and BLEU scores applied where they don’t belong, poorly written judge prompts, annotators forced to read raw JSON instead of a purpose-built labeling UI, uncalibrated scores on dashboards, judges overfit to a single data partition, and sampling plans that don’t represent production traffic.

Then there are the dashboards with 50 metrics, half of them generic—a problem that predated LLMs and has only gotten worse. [LLM evaluation in production](https://arize.com/blog/llm-evaluation-in-production/) is where these mistakes compound: offline green scores that never get validated against live traffic.

Every one of these has a data science analogue and practical fix:

| AI engineering activity | Data science corollary |
|---|---|
| Trace review and error analysis | Exploratory data analysis |
| Aligning evals to business outcomes | Metric design |
| Validating LLM judges | Model evaluation |
| Curated test sets and synthetic data | Experimental design |
| Trace logging and monitoring | Production ML operations |

That experimental mindset—measure, change, verify, repeat—is the [agent feedback loop](https://arize.com/glossary/agent-feedback-loop) evals exist to serve. It’s the same pattern we describe in [our post on going from production traces to better agents](https://arize.com/blog/from-production-traces-to-better-ai-agents-automating-the-llmops-feedback-loop/).

**Key takeaway:** For developers, make AI behavior observable enough to debug. For PMs, translate product quality into labeled examples, release gates, and regression monitors. The shared loop is simple: inspect examples, name the failure, write the eval, validate the evaluator, ship the change, and watch for regressions.

**Where to start**

If you are auditing an existing eval stack, start with the smallest loop that can change a product decision. Pull 50 recent traces, label them with a PM or domain expert, cluster the failures, pick one high-impact failure mode, and write a binary eval for it. Then validate that eval against human labels before putting it on a dashboard.

From there, connect the loop to your tooling: inspect traces in Phoenix or AX, run evaluators against representative examples, review disagreements, and log evaluator results back to production traces. Keep the CTA focused on one next action instead of sending readers into a link farm.

The real message is not that developers need to become data scientists or that PMs need to learn every ML metric. It’s that AI product teams need the data science loop: look at real examples, define quality with humans, validate automated judgments, and use evidence instead of vibes to decide what to build next.

*Watch the full talk from Arize Observe 2026 on* *YouTube**.*
