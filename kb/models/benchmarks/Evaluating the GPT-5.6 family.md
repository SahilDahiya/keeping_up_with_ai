---
title: Evaluating the GPT-5.6 family
topic: models
subtopic: benchmarks
secondary_topics:
- evals-observability/evaluation
summary: Evaluates the GPT-5.6 model family and presents a decision map for choosing
  models based on quality, cost, and task requirements.
source: braintrust
url: https://www.braintrust.dev/blog/gpt56-decision-map
author: Braintrust Team
published: '2026-07-10'
fetched: '2026-07-11T04:32:35Z'
classifier: codex
taxonomy_rev: 1
words: 1962
content_sha256: b3a975ab596dbac3f090149b2a14f45ef931195aee7dbde71a13e826206463ed
---

# Evaluating the GPT-5.6 family

10 July 2026Izzy Hurley11 min

The [GPT-5.6 family](https://openai.com/index/gpt-5-6/) launched yesterday with three models. Sol is the flagship, Terra is the general-purpose middle, and Luna is the fast, cheap one. It also arrives with strong scores on agentic benchmarks. For your work, which one is good enough, and how little can you pay for it?

This eval answers that question directly. I ran the GPT-5.6 family, plus Anthropic's Fable, Opus 4.8, and Sonnet 5, on a set of small, exact, machine-checkable tasks. Then I broke results down by task type and difficulty and turned them into a decision map you can route against.

| Dimension | Value |
|---|---|
| Models tested | GPT-5.6 Sol, Terra, Luna; Anthropic Fable, Opus 4.8, Sonnet 5 (with GPT-5.5 as a baseline) |
| Dataset | 225 procedurally generated, code-graded tasks (no public-benchmark contamination) |
| Task families | `arithmetic`,`symbolic_rules`,`data_transform`(75 tasks each) |
| Difficulty | `easy`/`medium`/`hard`, 25 tasks per family × difficulty |
| Runs per task | 3 independent attempts per model |
| Scoring | Exact match against the expected answer, checked by code, with no partial credit |
| What I report | Solve rate (how often the model gets it exactly right) and cost per call, with confidence intervals [1](https://www.braintrust.dev/blog/gpt56-decision-map#ref-1) |

Every task has one correct, machine-checkable answer. Scoring is deliberately strict. A model that reasons correctly but wraps the answer in the wrong format still fails, because production systems consume model output directly. 1 I report both raw solve rate and correct answers per dollar, so you can tell the

This eval isolates the small, exact operations agents lean on constantly, like arithmetic, following an ordered set of rules, and reshaping structured data into a required format. These are the steps where one wrong number or a single missing field can break a downstream pipeline.

| Task family | What it measures | Example |
|---|---|---|
| `arithmetic` | Multi-step number crunching with exact outputs | Reconcile multi-channel inventory and return `{total, spread, leader}` |
| `symbolic_rules` | Following an ordered set of transformations exactly | Apply a rewrite program to a string and return the exact result |
| `data_transform` | Parsing input, applying business logic, emitting structured output | Turn a row set into a nested JSON decision object |

One caveat is worth stating up front. The labels "easy," "medium," and "hard" describe how I *built* the tasks, not a guarantee that scores fall in that order. Arithmetic is the clearest exception below.

![Cost vs quality, OpenAI vs Anthropic](https://www.braintrust.dev/blog/img/gpt56-decision-map/cost_quality_quadrant.png)


Within the GPT-5.6 family, Sol and Terra are nearly tied, both around 83% overall, while Luna trails at about 68%. 1 Anthropic's models look weaker on the headline number (Sonnet 5 63%, Opus 55%, Fable 41%).

That gap is almost entirely refusals rather than wrong answers. On this task style Fable, Opus 4.8, and Sonnet 5 often stop with a refusal instead of attempting the work, and on the attempts they do complete they rank much higher, with Fable the most accurate model in the whole field. The refusal section near the end has the full breakdown.

![Reliability by difficulty, by family](https://www.braintrust.dev/blog/img/gpt56-decision-map/crossover_curves.png) Strengths cluster by task type. Sol is strong nearly everywhere, Terra stays close behind, and Luna holds up well on data transforms but falls off on symbolic rules.

Strengths cluster by task type. Sol is strong nearly everywhere, Terra stays close behind, and Luna holds up well on data transforms but falls off on symbolic rules.

The task *type* matters as much as the difficulty, and the model strengths cluster by task type. Sol is strong nearly everywhere, Terra stays close behind, and Luna holds up well on data transforms but falls off on symbolic rules.

- Data transforms are the most forgiving. Even Luna stays strong (87–100%) at every difficulty, so cheaper models are safe here.
- Symbolic rules are the hardest to route. Only Sol stays reliable across the board (95–97%); Terra plateaus in the mid-80s and Luna falls apart on the hardest tier. If exact rule-following matters, go straight to Sol.
- Arithmetic breaks the expected difficulty order. Every model does *best*on the medium tier and*worse*on "easy." The "easy" arithmetic tasks are multi-field reconciliations where one missing field fails the whole answer. They are straightforward to construct but hard to execute.[3](https://www.braintrust.dev/blog/gpt56-decision-map#ref-3)

![Model choice matters most on hard problems](https://www.braintrust.dev/blog/img/gpt56-decision-map/model_spread.png)


On easy tasks the models bunch together and the choice barely matters. On hard tasks the gap between best and worst blows open. Picking the right model matters most where the work is hardest.

![Overall correct rate by model](https://www.braintrust.dev/blog/img/gpt56-decision-map/reliability_bars.png)


The family-level results show data transforms are nearly solved for the OpenAI models, symbolic rules pull them apart, and the Anthropic rows are dragged down by refusals rather than by wrong answers.

![The cross-vendor decision map](https://www.braintrust.dev/blog/img/gpt56-decision-map/decision_map.png)


For each task type and difficulty, the map shows the cheapest model that clears a 90% reliability bar (hatched cells mean *no* model got there):

- For data transforms, Luna is the cost-optimal default on easy and medium work, stepping up to Terra only at hard.
- For arithmetic, Luna clears the bar at medium, but nobody clears it on the easy-reconciliation or hard cells. Plan for retries there.
- For symbolic rules, only Sol clears the bar, at every difficulty. This is the one place you should reach straight for the flagship.

Explore the interactive cost-quality chart →

![Latency vs quality](https://www.braintrust.dev/blog/img/gpt56-decision-map/cross_vendor_latency_vs_quality.png)


Cost isn't the only budget. Luna and Terra respond in about 5 seconds; Sol takes closer to 9. 4 For latency-sensitive paths, Terra is the standout, with essentially Sol's quality at roughly 60% of the wait.

![Model effects, holding task type and difficulty constant](https://www.braintrust.dev/blog/img/gpt56-decision-map/mixed_effects_forest.png)


I fit a statistical model to check the visual read. Terra is not meaningfully worse than Sol, and the difference is within the noise. 5 On tasks like these, reaching for Sol often buys latency headroom rather than accuracy. As I discuss below, that is a statement about decomposed subtasks rather than the long-horizon planning Sol is built for. The same model confirms that data transforms are far easier than the other families. It also shows that my

`easy` / `medium` / `hard` labels, while they track ![Where Anthropic models refuse](https://www.braintrust.dev/blog/img/gpt56-decision-map/anthropic_refusal_rate.png)


Anthropic's low headline scores are mostly refusals rather than wrong answers. Fable produced a usable answer only 44% of the time (298 of 675 calls). The rest were overwhelmingly hard refusals. 368 calls stopped with `stop_reason="refusal"`, every one tagged `stop_details.category="cyber"`, and a further 9 came back empty, for 377 non-answers in total. They piled up almost entirely on symbolic-rules tasks (222 of 225 got no answer) and arithmetic (152); data transforms were barely touched (3).

![Correct rate rises sharply once refusals are excluded](https://www.braintrust.dev/blog/img/gpt56-decision-map/anthropic_correct_excl_refusals.png)


Set the refusals aside and the ranking flips at the top. On the attempts it completed, Fable was the most accurate model in the entire field (92%). Opus and Sonnet rise sharply too.

![The refusal penalty grows with difficulty](https://www.braintrust.dev/blog/img/gpt56-decision-map/anthropic_correct_by_tier_excl_refusals.png)


The low Anthropic scores reflect how often these models refuse this style of task. When they do attempt it, they handle the work well. I haven't pinned down the exact trigger, but the refusals cluster so tightly on synthetic string-rewrite prompts that it looks like a safety classifier reacting to *how the tasks are phrased*, rather than to anything risky. The tasks contain no real security content.

| Workload | Default | Escalate when |
|---|---|---|
| Data transform (easy / medium) | Luna | Hard tier, nested schemas, or strict quotas: Terra |
| Data transform (hard) | Terra | Misses are costly: Sol |
| Arithmetic (medium) | Luna | No escalation needed |
| Arithmetic (easy reconciliation / hard) | Sol + retries | Nobody clears 90%; budget retries or accept misses |
| Symbolic rules (any difficulty) | Sol | No escalation needed; Terra and Luna sit below the bar |
| Latency-sensitive, general work | Terra | Statistically tied with Sol, at ~60% of the latency |

Treat this as a starting policy to tune against your own reliability bar, latency budget, and retry strategy. The right call depends on how expensive a single miss is in your pipeline.

- The dataset is code-graded but synthetic. It is contamination-resistant, but it is not real production traffic.
- It measures the building blocks agents rely on, not long-horizon planning, tool use, or real repository editing.
- Exact-match scoring can penalize formatting slips that stronger schemas or retries would fix.
- Difficulty labels describe construction, not guaranteed empirical difficulty.
- Refusal behavior is sensitive to prompt wording and can shift with model updates.
- Cost and latency rankings depend on observed usage and current list prices.

This eval speaks to structured, verifiable-answer work: exact arithmetic, rule-following, deterministic transforms, and the cost/latency/reliability tradeoffs among them. It does not measure open-ended writing, multimodal reasoning, or taste.

Most importantly, these are decomposed, single-shot tasks, not long-horizon work. Each task is one self-contained step with a single checkable answer. That is deliberate. It isolates the building blocks that agents are made of. It also means the eval rewards the setting where cheaper models shine, and it cannot see the thing a flagship is built for. As the *planning* or *orchestration* model driving a complex, multi-step workflow, where early mistakes compound across turns, context has to be carried, and the model has to decide *what to do next*, I would expect Sol to separate from Terra and Luna in ways this eval does not capture.

The strong Terra and Luna results show they are excellent at decomposed subtasks, though they are not interchangeable with Sol for agentic planning. The most likely production pattern is a split, where Sol acts as the planner that decomposes the work, with Terra or Luna executing the subtasks it hands off. That is the setting this eval measures directly.

Use this eval as a template for routing your own workflow across the GPT-5.6 family. Build a small dataset, set a reliability bar, and compare quality, latency, and cost in Braintrust.

If you want to evaluate model routing on your own workloads, [try Braintrust](https://www.braintrust.dev/signup) or [book a demo](https://www.braintrust.dev/contact).

1 "Solve rate" is the share of individual attempts that
exactly match the expected answer (I use the `answer_correct_extracted` scorer,
which pulls the answer out of surrounding prose before checking it), averaged
over the 3 attempts per task: 75 attempts per family × difficulty cell, 675 per
model. Refusals and malformed outputs count as failures. Every rate carries a
95% Wilson confidence interval; this is a mean-over-attempts rate, not a "best
of 3."

2 Cost is observed input/output token counts times each
provider's published API list price at run time; no prompt caching or retries in
the priced path. Efficiency ("correct answers per dollar") is solve rate divided
by mean cost per call, so a model can't look efficient by refusing cheaply.

3 In the same regression, `data_transform` is far easier
than `arithmetic` (odds ratio ≈ 161) and `symbolic_rules` is harder (≈ 0.59).
The medium tier scores *higher* than easy (odds ratio ≈ 2.3), which is the
statistical signature of the "easy" arithmetic reconciliation tasks being harder
than their label suggests.

4 Mean end-to-end latency per call: Luna 5.0s, Terra 5.4s,
Fable 8.4s, Opus 8.7s, Sol 8.8s, Sonnet 5 11.3s. "Answered-only" accuracy (used
in the refusal section) recomputes the solve rate over the non-refused attempts.

5 From a mixed-effects logistic regression of correctness
on model, task family, and difficulty (with a random effect per task). Relative
to Sol, Terra's odds ratio is 0.86 with a 95% CI of [0.65, 1.12]. The interval
crosses 1, so the two are not statistically distinguishable. Luna, Sonnet 5,
Opus 4.8, and Fable all land well below Sol (odds ratios ≈ 0.19, 0.12, 0.06, and
0.01 respectively).
