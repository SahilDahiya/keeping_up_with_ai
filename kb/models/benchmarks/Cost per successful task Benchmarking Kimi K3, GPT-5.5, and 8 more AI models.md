---
title: 'Cost per successful task: Benchmarking Kimi K3, GPT-5.5, and 8 more AI models'
kind: blog
topic: models
subtopic: benchmarks
secondary_topics:
- evals-observability/benchmark-design
summary: Arize and Fireworks benchmark 10 models (Kimi K3, K2.6, GPT-5.5, GPT-5, Claude
  Sonnet 5, GLM-5.2, DeepSeek V4 Pro, gpt-oss-120b, two Gemini variants) across 40
  agent tasks and 2,400 runs, arguing cost-per-successful-task (spend across all attempts
  / successes) is the metric that matters, not token price — gpt-oss-120b wins on
  cost-per-success despite a 33% pass rate.
triage: null
skip_reason: null
source: arize
url: https://arize.com/blog/cost-per-successful-task-ai-model-benchmark
author: Laurie Voss
published: '2026-07-23'
fetched: '2026-07-24T06:50:05Z'
classifier: claude
taxonomy_rev: 2
words: 3261
content_sha256: 162126166fd371f8884065bbd9ad959dd3aa3ad850c74a90f72e8ab241f2fccd
---

# Cost per successful task: Benchmarking Kimi K3, GPT-5.5, and 8 more AI models

**Arize and  Fireworks tested 10 open and closed models (including the soon to be open-weights Kimi K3) on 40 real agent tasks and 2,400 runs, measuring pass rates, retries, coverage, and cost per successful task.**

This is an experiment from Fireworks and Arize, built around one question: when you’re choosing a model to get real work done, what should you actually optimize? The reflex is to pick a side by label, open or closed, cost effective or frontier. We ran ten models from four providers against real command-line tasks and measured not the price of tokens but the price of *finishing the job*, and the labels turned out to be the wrong axis. What separated the models was [cost per successful task](https://arize.com/blog/why-ai-token-costs-dont-tell-you-if-your-ai-is-working/).

The question matters more every month, because the economics of inference are shifting. The first few years of the LLM era ran on [heavily subsidized pricing](https://arize.com/blog/ai-model-subsidies-ending-llm-inference-costs/), set to capture market share rather than to cover cost. That era is ending (a shift [I’ve written about before](https://arize.com/blog/ai-model-subsidies-ending-llm-inference-costs/)). When you pay the full cost of inference, the gap between a model that looks cost effective on a pricing page and a model that is actually cost effective to get work done becomes the difference between a product that pencils out and one that doesn’t.

** Cost per token is an infrastructure metric. Cost per successful task is a productivity metric.** The second one is what teams should optimize.

By cost per successful task we mean everything a model spent across every attempt, including the runs that failed, retried, or timed out, divided by the number of times it actually completed the task:

![Cost per successful task formula: total spend across all attempts divided by successful runs.](https://arize.com/wp-content/uploads/2026/07/image1-3.png)

[Token price](https://arize.com/blog/why-ai-token-costs-dont-tell-you-if-your-ai-is-working/) can’t see retries, [failed tool calls](https://arize.com/blog/how-to-evaluate-tool-calling-agents/), malformed outputs, judge calls, or runs that grind to a limit and never finish. Cost per successful task sees all of it. Here is what it showed across **2,400 runs: 40 tasks, 10 models, 6 trials each.**

**AI model benchmark results: cost per successful task across 10 models**

| Model | Provider | Pass rate | Mean $/attempt | $/successful task | Retry tax | 
|---|---|---|---|---|---|
| gpt-oss-120b | Fireworks (open) | 33% | $0.018 | $0.054 | 3.0× | 
| gemini-3.1-flash-lite | 40% | $0.026 | $0.063 | 2.5× | |
| Kimi K2.6 | Fireworks (open) | 42% | $0.163 | $0.384 | 2.4× | 
| GLM-5.2 | Fireworks (open) | 42% | $0.208 | $0.500 | 2.4× | 
| DeepSeek V4 Pro | Fireworks (open) | 39% | $0.230 | $0.588 | 2.6× | 
| GPT-5.5 | OpenAI (frontier) | 67% | $0.424 | $0.636 | 1.5× | 
| Kimi K3 | Fireworks (open) | 66% | $0.441 | $0.670 | 1.5x | 
| GPT-5 | OpenAI | 41% | $0.317 | $0.769 | 2.4× | 
| Claude Sonnet 5 | Anthropic | 49% | $0.494 | $1.014 | 2.1× | 
| gemini-3.5-flash | 23% | $0.288 | $1.233 | 4.3× | 

**Note:** We did not test GPT-5.6 sol in this benchmark. The results below reflect only the 10 models listed and should not be interpreted as a direct comparison with GPT-5.6 Sol.

**The most cost effective model per successful task is an open one, and it has the worst pass rate in the study.** `gpt-oss-120b` finishes a task for $0.054 while passing only 33% of the time, roughly **12× lower cost per success than GPT-5.5** and **23× more cost effective than gemini-3.5-flash**. The “retry tax” column is that hidden cost in one number, the attempts needed per success. Even paying that tax, cost effective model economics win handily.

**Where the frontier premium actually goes**

Aggregates hide the most actionable result in the study. Split the same runs by task difficulty:

| Model | easy | medium | hard | 
|---|---|---|---|
| gpt-oss-120b | 65% | 32% | 14% | 
| gemini-3.1-flash-lite | 69% | 48% | 8% | 
| Kimi K2.6 | 73% | 43% | 21% | 
| GPT-5.5 | 69% | 75% | 51% | 
| Kimi K3 | 100% | 72% | 32% | 

*Pass rate by task difficulty.*

**On easy tasks, the frontier premium buys you nothing at all.** GPT-5.5 passes 69% of easy tasks. Kimi K2.6 passes 73% of them, and `gpt-oss-120b` passes 65% at roughly a twenty-fourth of the cost per attempt. Paying frontier prices for easy work doesn’t make financial sense.

**On hard tasks, only the top tier even competes.** The most cost-effective models fall far; solving the hardest problems takes a frontier-class model, open or closed. And retrying is no substitute: a model that cannot do a task does not learn it on the fourth attempt, it just bills you four times. This is the one place routing cannot save you money. You have to pay for capability.

**But “frontier-class” is not one thing.** GPT-5.5 (closed) and Kimi K3 (soon to be open, currently via [Kimi.com](http://Kimi.co)) finished the study in a near-tie, 67% and 66% success at $0.64 and $0.67 per successful task, and yet they’re good at opposite work. K3 solved every easy task in the study, all six trials of all of them, where GPT-5.5 slipped to 69%. On the hardest tasks they swap: GPT-5.5 51%, K3 32%. Same tier, same price, same overall success, opposite strengths, one open and one closed. The only way to know which fits your workload is to measure it on your workload.

**Why the most cost-effective model is not a drop-in replacement**

Cost per success and *coverage* are different questions. Counting tasks a model solves **reliably** (4 of 6 trials or better):

- `gpt-oss-120b`:- **8 of 40**
- GPT-5.5: **25 of 40**
- Kimi K3: **26 of 40**

`gpt-oss-120b` is more cost effective per success partly *because* it only wins the tasks it can win. If you swap your frontier model for it wholesale, your bill collapses and so does the set of things your product can do.

This is where the labels first break down, and it isn’t the last. The two most efficient models per success are `gpt-oss-120b` (open) and `gemini-3.1-flash-lite` (closed), a hair apart at $0.054 and $0.063. At the other end, the two strongest models are GPT-5.5 (closed) and Kimi K3 (open), in a dead heat. Open and closed, side by side, at both ends of the range. The real axis is not open versus closed. It is small-and-cost-effective-with-retries versus large-and-expensive, and which one you want depends entirely on the task in front of you.

So using a frontier model overpays for easy tasks, but using a smaller model may leave you with no solution at all. **The right response to this is routing: send easy tasks to the cost effective model, and harder tasks to the frontier.** We’ll talk about how to do that in a moment.

**How we benchmarked 10 AI models across 2,400 runs**

We ran real tasks from [Terminal-Bench](https://www.tbench.ai), a benchmark of genuine command-line jobs (e.g. convert this file, debug this program, crack this hash, solve this puzzle), each shipping its own Docker environment and its own test script. Then we built a small, [fully instrumented agent](https://arize.com/blog/what-is-an-agent-harness-why-harnesses-are-replacing-agent-frameworks/) to attempt them.

The setup, end to end:

- **A thin agent, so cost reflects the model.**One tool (run a bash command in the task’s container) in a plain loop. No elaborate scaffolding to muddy the attribution. Whatever a run costs, the model earned it.
- **Model-agnostic by design.**Every model in the table runs through one code path via OpenAI-compatible APIs: Fireworks, OpenAI, Anthropic, and Google. Adding a model is a config line: a base URL, a model id, a price.
- **Honest, deterministic grading.**After the agent finishes, we run the task’s- *own*test suite inside the container. All tests pass or the task failed. The agent never sees the tests, so it can’t game them.
- **Two guardrails.**A token budget (the primary, fairness-preserving cutoff) and a generous wall-clock timeout (a safety net). A run that hits either is recorded as a failure with that reason, kept distinct from a genuine wrong answer, so the success count stays honest.
- **Full tracing to Arize AX.**Every run emits an- [OpenInference trace](https://arize.com/docs/ax/concepts/otel-openinference/overview): a root agent span with nested LLM and- [tool-call spans](https://arize.com/blog/how-to-evaluate-tool-calling-agents/), token counts, latency, and a clear error status when something goes wrong. This is what let us see- *where*the money went, not just how much.

![Benchmark study setup: 40 Terminal-Bench tasks, 10 models, and 6 trials per task-model cell, fully traced to Arize AX.](https://arize.com/wp-content/uploads/2026/07/image2-2.png)

[Arize AX](https://arize.com/products/ax/).

**40 tasks × 10 models × 6 trials = 2,400 runs**, $626 of API spend. Every one of the 400 task-model cells has exactly 6 trials, which puts the 95% confidence interval on a pass rate at about ±6 points. That is enough to rank models by cost per success with confidence. It is not enough to split hairs between neighbors: Kimi K2.6 and GLM-5.5 are a coin flip apart, and we would not report one as beating the other.

**How AI model routing reduces cost per successful task **

If the frontier premium is wasted on easy work and essential on hard work, the obvious move is to stop buying one model for both. We simulated that over the real runs.

| Policy | Reliably solves | $/successful task | 
|---|---|---|
| `gpt-oss-120b`alone | 8/40 | $0.054 | 
| GPT-5.5 alone (best single model) | 25/40 | $0.636 | 
| Oracle routing(the most cost effective model that reliably solves each task) | 34/40 | $0.228 | 
| Escalation(`gpt-oss`→`flash-lite`→ Kimi 2.6 → GPT-5.5, stop on first pass) | 32.3/40 | $0.525 | 
| Naive escalation through all 10 models | 34.5/40 | $1.319 | 

Three things fall out of this:

**Routing beats the best single model on both axes at once.** Oracle routing solves 36% more tasks than GPT-5.5 alone at roughly a third of the cost per success. It needs hindsight to pick the right model per task, so treat it as the ceiling on what good routing buys rather than a policy you can deploy.

**Escalation is the deployable version, and it still wins on both axes.** Try the most cost effective model, escalate on failure, stop on the first pass: $0.525 per success while solving more tasks than the frontier model alone, because most work gets done by a model costing under three cents an attempt and only the genuinely hard tasks ever reach the expensive rung.

**A bad escalation ladder is worse than no routing at all.** Naively escalating through all 10 models costs $1.319 per success, worse than every single model in the study. You pay the entire ladder on the roughly six tasks nobody solves, and you pay poor-value rungs on the way past. Designing your ladder carefully is essential.

**When should an AI agent escalate to a frontier model?**

There’s an obvious objection to everything above. “Escalate on failure” assumes you can tell that a run failed. Our benchmark gets that for free, because every Terminal-Bench task ships its own test suite. Most production systems don’t. Here’s how to do it in production:

**Often you don’t need to detect failure at all.** The difficulty table above is already a routing policy, and it needs no runtime verification of anything. Measure once, [offline](https://arize.com/docs/ax/develop/datasets-and-experiments), which class of work each model handles, then route by the class of the incoming request. “Simple requests to the more efficient model, complex ones to the frontier” needs a classifier, not a verifier. Escalation is the outcome-driven version of routing; routing by task class is the version you can ship without an oracle.

**More work is verifiable than people assume.** A few example questions you should ask: Does the code compile? Do its tests pass? Does the JSON parse and does it validate against the schema? Does the SQL run and did the API call come back non-error? And do the cited quotes actually appear in the source document? Checking an answer is usually more cost effective than producing one. Wherever a low-cost deterministic check exists, escalation is deployable today, and a lot of [agentic work](https://arize.com/glossary/agent/) is exactly this shape.

**When there’s no verifier, escalate on distress rather than on failure.** You don’t need to know the right answer to notice a run going badly. Recall that 91% of Gemini-3.5-flash’s failures were budget exhaustion: a model out of its depth churns, and churn is visible while it’s happening. Tool calls exiting non-zero, the same command repeated three times, a run costing five times the median for its task type: all of these are live signals, none of them require ground truth, and all of them are sitting in the [traces](https://arize.com/glossary/trace/) you get from Arize.

**But the failure that actually costs you is the silent one.** A `test_failed` run finishes confidently, every span green, every command clean, and the answer simply wrong. No distress signal fires, because from the inside nothing went wrong. For those you need a real check: a verifier, an [LLM judge](https://arize.com/blog/how-to-build-llm-as-a-judge-evaluators-that-hold-up-in-production/) (whose calls are a genuine cost and belong in the same accounting), or a downstream signal like a thumbs-down, a retry, or a support ticket. There is no free lunch here, and a routing story that pretends otherwise is one you’ll pay for later.

But if you genuinely cannot tell success from failure anywhere in your system, model selection is not your biggest problem: you’re shipping something you can’t evaluate. Cost per successful task forces you to define what success means through rigorous evaluations, which is something you should have been shipping anyway.

**Are frontier AI models always more reliable? **

It’s tempting to treat the expensive model as the “just works” option. The traces say otherwise.

- On **csv-to-parquet**, a trivially easy “convert this file” task, GPT-5.5 passed only**3 of 6 trials**.
- The single most expensive success in the entire study was **Claude Sonnet 5 solving a cryptanalysis task for $1.35**, twenty-five times what`gpt-oss-120b`charges for an average success.
- `gemini-3.5-flash`is the cautionary tale of the whole study.- **91% of its failures (168 of 184) were the token cap**: it spirals, burns its entire budget, and produces nothing. Meanwhile its own smaller sibling,- `flash-lite`, is the second most cost effective model per success in the field. Such different results from close model siblings is why you need- [evaluations](https://arize.com/glossary/evaluations/).

**How AI tracing exposes hidden model costs**

Aggregates tell you *that* the low cost models are efficient. [Traces](https://arize.com/glossary/trace/) tell you *why*, and traces are where the “invisible” costs become visible. Because every run is traced to Arize AX with tool-call and token detail, each failure carries its own explanation:

- `token_cap`:- [tool calls](https://arize.com/blog/how-to-evaluate-tool-calling-agents/)going nowhere. This is the real cost of a model that’s out of its depth, and it is exactly what a token-price benchmark hides. It is also 91% of what gemini-3.5-flash did.
- `test_failed`:- [root span](https://arize.com/docs/ax/observe/tracing-concepts/what-are-traces)is red. That “everything worked except the outcome” signature is a- *silent failure*, the most expensive kind, because in production nothing would have alerted you. This is what GPT-5.5’s csv-to-parquet failures look like.
- **Tool-call friction:**commands that exit non-zero light up red in the trace, so you can see the exact step where a run started to struggle and how many attempts it burned recovering.

A per-token benchmark gives you one number and no recourse. Traces turn a failed run into a diagnosis: which model failed, at which step, at what cost, and whether it failed loudly or silently. That is the difference between knowing your costs and being able to *do something* about them.

*(A note on judge costs: we graded with each task’s own  deterministic tests, so there was no LLM-as-a-Judge overhead here. In systems that use LLM-as-a-Judge for evaluation, those judge calls are another real, recurring cost, and the same cost-per-successful-task accounting is needed.)*

**A word on the developer experience**

Fireworks made the model side effortless. It’s OpenAI-compatible API meant its open models ran through the same code path as every other provider we tested ([Fireworks offers easy-to-follow documentation on this](https://docs.fireworks.ai/tools-sdks/openai-compatibility)), differing only by a base URL and a model id. Adding GLM-5.2 to a study that already had `gpt-oss-120b` was a config line, not an integration project.

For a comparison study that’s a convenience. For a production [routing layer](https://arize.com/blog/3-production-patterns-ai-agents-how-to-evaluate-each-one/) it’s critical: “send this task to the lowest cost and most capable model, escalate if it fails” is only realistic when the rungs of your ladder are interchangeable at the API level. The breadth of strong open models on one platform is what makes the cost effective end of that ladder possible at all, and as the numbers above show, the low-cost end is where most of your tasks should be getting done.

**Measure it yourself**

[The full harness](https://github.com/Arize-ai/fireworks-cost-benchmark) (the agent, the Docker task runner, the grading, the guardrails, the Arize AX instrumentation, the routing analysis, and the results from this study) is available to run and extend. The recipe is portable to your own tasks:

- Run a representative set of your real tasks, several trials each, across the models you’re considering. Include tasks that are too hard for the low-cost models; that’s where the interesting part of the curve is.
- Grade each run the way your product actually defines success.
- Count *all*the spend, divide by the successes, and read the traces on the failures. Report coverage next to cost, always.
- Route accordingly, and re-measure, because models and prices both move.

**The takeaway**

Token price is an infrastructure metric. It’s useful for capacity planning and almost useless for designing your production stack. Cost per successful task is the productivity metric, and when you measure it end to end across 2,400 runs, the picture the pricing pages paint flips:

- Cost per successful task can diverge from token price by more than an order of magnitude, and it inverts the ranking the pricing pages give you.
- The open-versus-closed label predicts nothing that matters here. The two most efficient models were one open and one closed; the two strongest were one closed and one open, GPT-5.5 and the open-weights Kimi K3, in a dead heat. Buy capability and price, not a camp.
- The frontier premium is worth nothing on easy work and decisive on hard work, so route by difficulty instead of buying one model for every job.
- Routing beats every single-model strategy on cost and coverage at once, but only with a deliberate ladder. A bad escalation ladder is worse than none.
- Coverage and cost are different questions: the cost-effective model reliably solved 8 of 40 tasks, the frontier tier 25 to 26. Report both.
- The traces made every hidden cost, including silent failures and the model that burned its whole budget 91% of the time it failed, impossible to miss.

Optimize for cost per successful task, match each rung of your stack to the model that actually fits it (regardless of who built it or what it costs per token), keep a capable model in reserve for the hard tail, and instrument everything. That’s not just the more cost-effective stack; it’s the one you can reason about.

*Study: 40 Terminal-Bench tasks × 10 models × 6 trials (2,400 runs, $626 of API spend), graded by each task’s own test suite, fully traced to Arize AX. Every task-model cell has 6 trials; pass rates carry roughly a ±6 point 95% confidence interval. Prices as of July 2026. Results are directional, not a leaderboard score: 40 of Terminal-Bench’s ~240 tasks, chosen to sit in the band where some models pass and some fail. Claude Sonnet 5 is billed at its standard rate, not its introductory rate. *
