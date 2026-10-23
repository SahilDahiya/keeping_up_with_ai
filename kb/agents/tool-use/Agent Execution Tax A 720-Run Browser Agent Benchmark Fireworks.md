---
title: 'Agent Execution Tax: A 720-Run Browser Agent Benchmark | Fireworks'
kind: blog
topic: agents
subtopic: tool-use
secondary_topics:
- evals-observability/benchmark-design
summary: 'A 720-run browser-agent benchmark across four LLMs finds that execution
  reliability, not reasoning quality, drives failures: one model wasted nearly 1-in-5
  calls on malformed JSON retries, defined as a 22.9% ''Agent Execution Tax'' versus
  0% for the best model.'
triage: null
skip_reason: null
source: fireworks
url: https://fireworks.ai/blog/agent-execution-tax-browser-agent-benchmark
author: null
published: '2026-05-20'
fetched: '2026-10-23T06:13:44Z'
classifier: claude
taxonomy_rev: 2
words: 4177
content_sha256: 2f9449b394c88a8526af39d69075fc342c285c99afd7b8d5f6e24cf346fb4381
---

# Agent Execution Tax: A 720-Run Browser Agent Benchmark | Fireworks

### What 720 browser agent runs revealed about the real bottleneck in agentic AI.

Foundation models keep getting smarter. They ace reasoning benchmarks, write fluent code, and pass professional exams. Yet when you put them inside an agent loop, where they must observe a webpage, decide what to do, and output a structured action ten times in a row, they fail roughly half the time.

We ran 720 browser automation tasks across four LLMs to find out why. The answer was not intelligence. It was execution: **one model wasted nearly 1 in 5 LLM calls on malformed JSON that had to be retried.** That single reliability gap cascaded into higher latency, inflated cost, and lower task success, even though the model’s raw reasoning capability was competitive.

We call this overhead the **Agent Execution Tax**: the ratio of wasted inference to productive inference. For the worst-performing model in our benchmark, that tax was 22.9%. For the best, it was zero.

In agent systems, reliability compounds harder than intelligence. The models that won were not the ones with the best reasoning scores. They were the ones that reliably did what they were told, every time, in the format they were asked for.

In production, that reliability is shaped not just by the model itself, but by the inference infrastructure serving it: structured output consistency, latency predictability, and stable execution under repeated agent loops.

At 10,000 agent tasks per day, a modest production volume, the execution overhead of the worst-performing model costs over $40,000 per year in inference that produces no value. A model that looks cheaper per token can cost significantly more per outcome once retries, failures, and inflated call counts are factored in.

**Scope.** This is a text-only browser agent benchmark. Results measure structured output reliability and step efficiency in a multi-step agent loop — not general model intelligence, reasoning ability, or multimodal capability. See Scope of This Benchmark below for the full scope statement.

## Deployment Readiness Scorecard

If you are evaluating models for an agent deployment, here is how they map to production constraints.

**One-line summary per model:**

- **GLM-5:** Best accuracy, highest cost. Use for compliance workflows, research automation, and tasks where errors carry downstream consequences.
- **MiniMax M2.5:** Best value. Default choice for scaled production workloads. The $40k/year waste calculation makes it the economically dominant option at volume.
- **Kimi K2.5:** Best speed, zero execution overhead. Use for customer-facing agents, live demos, and any workflow where response latency affects user trust.

## The Agent Execution Tax

A browser agent task looks simple from the outside: go to Amazon, search for a product, extract the price. Under the hood, it is a multi-step loop:

`observe page → LLM generates action (as JSON) → execute action → observe new page → repeat`

A typical task takes 10 steps. Each step is an LLM call that must return valid structured output: a JSON object specifying which element to click, what text to type, or what data to extract. If the JSON is malformed, the framework retries. And that retry is invisible: it does not show up in task success rates or reasoning benchmarks. It only surfaces as inflated call counts, latency, and cost once you instrument the engine itself.

### Definition

`Agent Execution Tax = (total_inference_calls − productive_calls) / productive_calls`

**Productive calls** are those that returned valid structured output on the first attempt. The tax measures how much additional inference you pay, relative to the useful work done. Every percentage point is money spent on inference that delivers nothing.

Note the denominator: this is not the same as the raw retry rate (retries / total calls). An 18.6% retry rate translates to a 22.9% execution tax because the denominator shrinks when you remove the wasted calls.

### Applied to Our Data

Measured on instrumented runs (90 tasks per model). Zero parse failures (exhausted retries) recorded across all models.

For every dollar of productive inference Gemini produces, you pay an additional 23 cents in waste. Kimi’s tax is zero.

(Note: the hero Execution Tax bar chart at the top of the article is the canonical visual for this section; do not duplicate it here. The table above carries the exact numbers for citation.)

### How the Tax Compounds

The tax is not a single cost. It stacks across three dimensions:

1. **Token tax.** Wasted tokens on malformed responses, plus the full input context re-sent on every retry. Gemini averaged 15,482 input tokens per step; each retry re-sends that entire context for zero productive output.
2. **Latency tax.** Each retry adds a full LLM round-trip (\~2.5s at Gemini’s p50), roughly 12 seconds of dead time per task.
3. **Cascade tax.** A retry at step 8 can desync the agent’s internal state, causing downstream steps to misinterpret the page and fail. Hardest to measure; most dangerous at scale.

### Generalised Formulas

`Expected retries per task = n_steps × retry_rate / (1 − retry_rate)`

Token overhead per task   = expected\_retries × (avg\_input\_tokens + avg\_output\_tokens)

Latency overhead per task = expected\_retries × avg\_call\_latency

For a 10-step task with Gemini’s 18.6% retry rate: \~2.3 expected retries, \~36,500 wasted tokens, and \~5.7 seconds of dead time per task.

## Structured Output Reliability: The Root Cause

Execution tax is the lens. Structured output reliability is what drives it and is one of the most underreported bottlenecks in production agents.

### The Data

Gemini 2.5 Flash produced invalid structured output on **nearly 1 in 5 LLM calls**. The three Fireworks models combined: 18 retries across 2,564 calls (0.7%).

### Why This Matters More Than You Think

In a 10-step agent task, the probability that at least one step requires a retry:

- Gemini (18.6% per call): **86.7%**
- MiniMax (1.6% per call): 14.9%
- Kimi (0.0% per call): 0%

With Gemini, 87% of tasks experience at least one parse retry. This is not an edge case; it is the default experience. Gemini averaged 14.7 LLM calls per task versus \~10 for the Fireworks models: the extra \~4.7 calls are almost entirely retries and the downstream steps they force.

### Reliability-Adjusted Accuracy

Raw task accuracy tells you how often the agent succeeds. It does not account for the cost of getting there. A compound metric, **Reliability-Adjusted Accuracy**, discounts task success by execution overhead:

`Reliability-Adjusted Accuracy = Task Success Rate × (1 − Execution Tax)`

The gap between Gemini’s raw accuracy (45.0%) and its reliability-adjusted accuracy (34.7%) is the clearest illustration of the execution tax: over a third of Gemini’s operational capacity is consumed by execution overhead. The Fireworks models barely move.

### Why Nobody Measures This

The parse retry happens inside the LLM engine, before the agent framework ever sees the result. Unless you instrument the engine, retries are invisible. Static benchmarks (MMLU, HumanEval, ARC) measure model intelligence in isolation; they do not measure whether a model can sustain structured output compliance across a multi-step loop. **Parse retry rate should be a first-class metric in every agent benchmark.**

Prior work has documented adjacent findings. The original [**WebVoyager paper**](https://arxiv.org/abs/2401.13919) (He et al., 2024) introduced the benchmark we use here and established the framing that end-to-end web agent performance is a distinct measurement from static model evaluation. [**AgentBench**](https://arxiv.org/abs/2308.03688) (Liu et al., 2024) evaluated LLMs across eight agent environments and found large gaps between model-capability scores and task-completion rates in multi-step loops, reinforcing that agent-specific reliability metrics — not MMLU rank — should drive procurement decisions. [**SWE-bench**](https://arxiv.org/abs/2310.06770) (Jimenez et al., 2024) extended the same observation to software-engineering agents: models that top reasoning leaderboards resolve only a small fraction of real GitHub issues, because sustained structured execution across long tool-use loops is not what static evals measure.

## What This Looks Like in Practice

**Task:** “Find all Uniqlo locations in Chicago, IL.” (Google Maps, from the WebVoyager benchmark)

Both models received the same task, the same browser environment, and the same starting URL.

**At a glance:**

Both models found the answer. One did it in 51 seconds with 12 clean calls. The other took 98 seconds and made 25 calls to accomplish 16 steps. The difference was not reasoning ability; it was execution overhead.

**Kimi K2.5: 12 steps, 0 retries**

Every call produced valid JSON on the first attempt.

**Gemini 2.5 Flash: 16 steps, 9 retries (25 total LLM calls)**

Gemini took 16 actions but made 25 LLM calls. Nine returned malformed responses and were silently discarded. From the framework’s perspective, each step appears to succeed; the retries are invisible inside the inference layer.

**What a parse retry looks like at the protocol level**

At each step, the agent must return a structured JSON object:

`{`

"state": {

"previous\_goal\_status": "success",

"previous\_goal\_eval": "Clicked the back button successfully.",

"page\_summary": "Google Maps showing search results for Uniqlo in Chicago.",

"relevant\_interactions": \[{"id": "B3", "reason": "Next page button"}\],

"memory": "Found one Uniqlo on State Street. Need to find all locations.",

"next\_goal": "Click Next page to see if there are more results."

},

"action": {

"type": "click",

"element\_id": "B3"

}

}

When the response fails to match this schema (missing a required field, invalid action type, markdown fences around the JSON), the framework catches the validation error and sends back a correction message:

`Error parsing LLM response: [{'type': 'missing', 'loc': ('state', 'memory'),`

'msg': 'Field required', 'input': {...}}\], retrying

The model then receives the full context again plus the error, and regenerates. Each regeneration costs a full inference call: input tokens (the entire conversation history) plus output tokens. At Gemini’s context sizes, a single retry adds roughly 12,000–16,000 tokens and 2–3 seconds of latency. Across 9 retries, that is \~20–25 seconds of dead inference time in one task.

Gemini’s 98s breaks down roughly as \~40s browser operations, \~37s productive inference, and \~21s retry inference. Kimi’s 51s has no retry segment at all. That is the Execution Tax made visible at the level of a single task.

## How We Measured This

[Notte](https://github.com/nottelabs/notte) is an open-source, model-agnostic browser agent framework. Change the model string, and the same agent pipeline runs identically across providers. This makes it an ideal testbed for isolating model behaviour from framework effects.

### The Setup

- **Task suite:** [WebVoyager](https://github.com/MinorJerry/WebVoyager), 60 multi-step browser tasks across 15 real websites (Amazon, GitHub, Google Flights, [Booking.com](http://booking.com/), ArXiv, Coursera, ESPN, BBC News, and more).
- **Runs:** Each model ran every task 3 times (180 runs per model, **720 total**) to control for website variability and non-determinism.
- **Instrumentation:** Per-call LLM latency, parse retry counts, parse failure counts, and token usage captured for every run.

### The Models

All three open-weight models were served by **Fireworks’ serverless inference**; Gemini 2.5 Flash was served by OpenRouter as a proprietary baseline. No dedicated deployments, no custom infrastructure — standard pay-per-token APIs throughout, the way most developers actually use these models.

Results therefore reflect both model behaviour and production-serving characteristics under a real multi-step agent workload, including latency consistency and structured-output reliability at the inference layer.

### Scope of This Benchmark

**This benchmark measures structured output reliability and step efficiency in a text-only browser agent loop. It is not a general comparison of model intelligence, reasoning ability, or multimodal capability.** Readers evaluating models for other use cases — chat assistants, code generation, standalone multimodal tasks — should not extrapolate directly from these findings. The rankings, cost-per-outcome figures, and execution tax values below apply specifically to the text-only agent setting.

Within that scope: all models were tested text-only (no screenshots) to ensure a fair comparison, since only 1 of the 3 Fireworks models supports vision. This puts Gemini 2.5 Flash at a structural disadvantage, because Notte’s production pipeline is built around Gemini’s multimodal capabilities. We address this directly in the results, but the punchline is that even restoring Gemini’s vision advantage (which boosts it to 53% in separate testing) does not change the outcome.

All models used identical settings: `temperature=0.0`, `max_steps=20`, `response_format=json_object` (non-strict mode). An independent LLM judge evaluated task success across all models. Full configuration details are in Appendix B.

The same model-agnostic framework used across these 720 runs used [Notte](https://notte.cc/). Reproducibility steps in Appendix A.

All results reflect the publicly available model versions and infrastructure configurations available during the March 2026 test window.

## Cost Per Successful Task > Token Pricing

Token pricing tells you what you pay per unit of inference. Cost per successful task tells you what you pay per unit of value. The gap between them is driven by retry waste, step efficiency, and task success rate, all of which token pricing ignores.

180 runs per model (720 total). Parse retry rate measured on instrumented runs (90 per model).

On a per-token basis, Gemini ($0.30/$2.50) looks cheaper than Kimi ($0.60/$3.00) and GLM ($1.00/$3.20). On a per-outcome basis, **MiniMax M2.5 is 2.3x cheaper than Gemini per successful task** while being 12.5 percentage points more accurate. The same pattern makes GLM-5 a premium-but-defensible choice and leaves Gemini economically unattractive despite its sticker price.

**Where the tokens actually go (per-task averages, recomputed from v2 instrumented runs):**

Gemini spends roughly **36,800 tokens per task on inference that is billed and thrown away** — nearly one in five tokens produces zero value. The three Fireworks models combined waste under 3,000 tokens per task.

## Inference Latency: The Compounding Story

Per-call latency is only half the picture. Factor in retry-inflated call counts, and the end-to-end story flips.

Gemini’s p50 latency (2,476ms) looks competitive with Kimi’s (2,145ms): only 15% slower per call. But Gemini makes \~14.7 calls per task versus Kimi’s \~10.2:

`Gemini: 14.7 calls × 2,476ms = 36.4s of LLM time`

Kimi:   10.2 calls × 2,145ms = 21.9s of LLM time

Gemini spends **66% more time in LLM inference** per task, not because it is slower per call, but because it makes more calls.

Agent deployments should evaluate inference infrastructure alongside model quality. Low tail-latency variance, stable structured-output serving, and predictable retry behavior materially affect end-to-end agent cost and responsiveness once systems operate at production scale.

The p95/p50 spread across all models (1.8–2.3x) is tight, indicating predictable tail latencies from Fireworks’ serverless infrastructure. That matters because retry amplification compounds unpredictability quickly in production agent systems: small variances at the inference layer become magnified across multi-step loops. In practice, agent reliability depends not just on the model, but on the serving layer’s ability to sustain low-variance inference across thousands of sequential calls.

**Time budget per average task (recomputed from v2 per-call latency arrays):**

Browser time is roughly equivalent across models (\~40–45s). Productive LLM time scales with per-call latency. The distinctive segment is retry LLM time: Gemini spends a full 7.1 seconds per average task on inference that will be discarded. Kimi spends zero.

## What the Fireworks Serving Layer Contributes

Two findings in this benchmark are properties of the serving layer, not of the models being served.

**Tight tail-latency variance across heterogeneous architectures.** Three Fireworks-served models with very different designs — Kimi K2.5 (32B active, 1T MoE), GLM-5 (40B active, 700B MoE), and MiniMax M2.5 (228.7B MoE) — all delivered p95/p50 spreads inside 1.9–2.3×. Across 90 tasks and thousands of inference calls per model, no Fireworks model produced a long-tail outlier. Tail-latency consistency across heterogeneous architectures is a serving-stack property: the model determines mean latency, but the stack determines whether that mean is the typical case or the lucky one.

**Retry recovery stayed stable across the Fireworks lineup.** When the Fireworks-served models did retry — 18 times across 2,564 calls combined — every retry recovered cleanly; none spiralled into the retry-exhaustion failure mode. That depends on structured-output handling that stays consistent under correction loops: even when the first output is malformed, the resend produces something the framework can parse. The difference between an invisible 2-second tax and a task-killing failure sits at the serving layer.

“The model determines capability; the serving layer determines whether that capability survives a multi-step loop.”

## Per-Site Analysis: Where the Thesis Holds or Breaks

The aggregate numbers support the execution-tax thesis. The site-level breakdown stress-tests it: if execution reliability is the real bottleneck, we should see the Fireworks models win on sites that demand compounded correctness across many steps, and we should see everyone struggle where visual parsing dominates.

### Universal Success

**Cambridge Dictionary** (100% across all models), **Wolfram Alpha** (83–100%), **ESPN** (83–100%). Clean DOMs, clear information hierarchies, minimal dynamic content. These tasks validate baseline agent competence; they are not where models differentiate.

### Universal Failure

**Allrecipes** (0–17%), **Google Search** (0–8%). Heavy dynamic loading, recipe card layouts, and deceptively complex DOMs with interleaved ads and knowledge panels. Both likely require vision to solve reliably. Execution tax is irrelevant here; the limiting factor is parsing the page at all.

### The Differentiators

These sites reveal genuine capability gaps and carry the core proof weight of the benchmark.

GLM-5 and MiniMax M2.5 dominate, but along different axes. GLM-5 wins where depth matters (Google Maps, HuggingFace, Coursera): structured data extraction and multi-step reasoning. MiniMax M2.5 wins where interaction matters (Booking, Amazon, GitHub): form flows and dynamic navigation. The split maps directly to their training — GLM-5 as a general reasoning model, MiniMax M2.5 as the only model in the lineup with RL-based agent training across real-world environments. The execution-tax story is consistent with both: wherever tasks compound across many steps, models with clean structured output and efficient step counts pull ahead, regardless of raw token intelligence.

### Gemini’s One Win: Google Flights

Gemini leads on exactly one website: Google Flights (83% vs 58–75%). Notably, a Google property. Whether the advantage comes from training data familiarity, an optimised DOM structure aligned with Gemini’s text representation, or simply good fortune on these specific tasks is unclear. But it is the only site where Gemini outperforms all three Fireworks models.

## What This Means for AI Procurement

When evaluating foundation models for an agent deployment, three metrics should drive the decision. Three should not.

**Use these:**

- **Cost per successful task** (not cost per token): captures retry waste, step efficiency, and success rate in a single number
- **Parse retry rate** (or execution tax): reveals how much of your inference budget is wasted on malformed outputs before you ever see a result
- **Reliability-Adjusted Accuracy**: combines task success with execution reliability into a single production-representative score
- **Infrastructure consistency under load**: predictable latency, retry handling, and structured-output stability become increasingly important as agent systems scale from demos to production workloads

**Do not lead with these:**

- **Token pricing**: Gemini is cheaper per token than Kimi; it is 2.3x more expensive per outcome
- **Benchmark reasoning scores**: MMLU and HumanEval do not measure structured output compliance across a multi-step loop

### Procurement Scorecard

MiniMax M2.5 occupies the dominant position for most production workloads: highest accuracy, lowest cost per outcome, negligible execution overhead. GLM-5 is the choice where accuracy on complex tasks is non-negotiable. Kimi K2.5 is the choice where real-time responsiveness matters most.

## Model Profiles: Three Models, Three Strategies

### GLM-5: The Reasoning Powerhouse

**57.1% accuracy | 6.3s avg LLM latency | $0.217/successful task | 0.6% execution tax**

Highest accuracy on sites requiring multi-step reasoning: Google Maps (100%), HuggingFace (100%), BBC News (100%), ArXiv (77%), Coursera (67%). Trades speed for depth; longer per call, fewer mistakes on complex tasks.

**Best for:** Batch and background workloads where accuracy matters more than latency. High-reliability pipelines where incorrect outputs carry downstream consequences: data extraction, compliance workflows, research automation.

### MiniMax M2.5: The Best Value

**57.5% accuracy | 3.7s avg LLM latency | $0.062/successful task | 1.6% execution tax**

Matches GLM-5’s accuracy at less than one-third the cost per successful task. Strongest on Amazon (88%), Google Maps (100%), Booking (33%, the only model to consistently complete booking flows), GitHub (39%), and ArXiv (86%). The only model in the lineup with RL-based agent training: it solves tasks in the fewest steps (9.8 avg) and takes the most direct paths.

**Best for:** Cost-sensitive production workloads at high volume. The default choice for most scaled deployments; the 2.3x cost advantage over Gemini per successful task compounds significantly across thousands of daily tasks.

### Kimi K2.5: Fastest Inference in This Benchmark

**49.7% accuracy | 2.3s avg LLM latency | $0.167/successful task | 0.0% execution tax**

Fastest inference (p50: 2,145ms), lowest token consumption, and zero parse retries across 852 calls. Competitive across the board with ESPN (100%), Cambridge Dictionary (100%), HuggingFace (75%), and ArXiv (57%). Fireworks’ infrastructure and [quality validation pipeline and work on Kimi K2.5](https://fireworks.ai/blog/quality-first-with-kimi-k2p5) are designed around sustained production inference behavior, not just benchmark throughput, which becomes especially important in long-running agent loops where retry amplification compounds quickly.

**Best for:** Real-time agent applications where users watch the agent act. Customer-facing automation, live demos, and interactive workflows where perceived responsiveness affects user trust.

## The Vision Question

All results above are text-only. We also ran a supplementary vision experiment with Gemini 2.5 Flash:

Vision gives a meaningful accuracy boost (+6pp) at the cost of \~15s per task. Biggest gains on visually complex sites: GitHub (+34pp), ESPN (+33pp), Coursera (+23pp).

**The critical point:** Even with Gemini’s vision advantage fully restored (53%), MiniMax M2.5’s text-only score (57.5%) still beats it. Vision narrows the gap but does not close it, and the Fireworks models have not yet had the opportunity to use vision themselves.

### Kimi K2.5 Vision: Infrastructure Constraint, Not Model Limitation

We attempted to run Kimi K2.5 with vision enabled to make the multimodal comparison symmetric across the Fireworks lineup. **87 of 90 tasks timed out on Fireworks’ serverless GPU infrastructure; only 3 completed.** The 3 that did complete ran cleanly — the model is capable; serverless capacity was not sized for sustained vision workloads at benchmark scale during our test window.

This is explicitly an infrastructure limitation, not a model limitation. A dedicated deployment — which Fireworks offers for production customers — would resolve it. We flag it directly here rather than omit it because the Fireworks-side vision comparison is incomplete for this round, and any interpretation of the text-only results should account for that gap. A follow-up benchmark on dedicated vision capacity is on the roadmap.

## Closing

**The bottleneck in agentic AI is not intelligence alone. It is execution across the full stack.**

Reliable agents require more than strong models: they require inference infrastructure that can sustain low-latency, structured, repeatable execution under production workloads.

The Agent Execution Tax — the hidden overhead of malformed outputs, wasted retries, and inflated call counts — is the gap between what models can do and what they reliably deliver in production. For the proprietary baseline in our benchmark, that tax consumed nearly a quarter of all inference. For the best open-weight models on Fireworks, it was effectively zero.

This is not a fixed property of proprietary versus open models. It is an engineering problem, solvable with the right models, infrastructure, and training data. The base capabilities are measured. The training data — hundreds of successful trajectories generated by this benchmark itself — is ready. A follow-up post will report the results of fine-tuning the top-performing open model on that data.

For organisations evaluating agentic AI at scale, execution reliability should gate how accuracy is interpreted across procurement decisions, infrastructure design, and deployment strategy.

**The serving layer matters as much as the model.** Low-variance tail latency across architectures, sustained structured-output stability under repeated correction loops, and retry-safe handling that contains malformed outputs without exhausting the budget — the three properties Fireworks demonstrated across the 720 runs in this benchmark.

## Appendix

### A. Reproducibility

This benchmark is fully reproducible. All models use serverless inference (no dedicated deployments), and the task suite is public.

**Requirements:**

- A Fireworks API key ([fireworks.ai](https://fireworks.ai/))
- An OpenRouter API key (for Gemini baseline + evaluator)
- The Notte framework (`pip install notte-agent`)

**To run:**

`# Example: run Kimi K2.5 on the WebVoyager benchmark`

uv run pytest packages/notte-eval/src/notte\_eval/webvoyager/test\_run.py \\

--task\_dir "webvoyager/webvoyager\_simple.jsonl" \\

--model "fireworks\_ai/accounts/fireworks/models/kimi-k2p5" \\

--n\_runs 3 --use\_vision false --headless true --max\_steps 20 -v

Full instructions, code changes, and analysis scripts are documented in [`fireworks/FIREWORKS_BENCHMARK.md`](https://file+.vscode-resource.vscode-cdn.net/Users/sam/Documents/github-notte/notte1.1/_benchmarks/fireworks/FIREWORKS_BENCHMARK.md).

### B. Benchmark Configuration

### C. Evaluator Methodology

The WebVoyager evaluator uses Gemini 2.5 Flash as an LLM judge. This is the same model as the proprietary baseline, which creates a theoretical risk that the judge may favour outputs resembling its own reasoning style. We accept this trade-off because: (a) the evaluator judges task outcomes (did the agent reach the correct answer?), not reasoning style; (b) the judge sees only the final answer and screenshot, not intermediate reasoning chains; and (c) changing the evaluator would break comparability with Notte’s existing benchmark results.

Critically, this risk cuts in the direction that would weaken our thesis, not strengthen it: any same-judge bias would inflate Gemini’s scores, not suppress them — yet Gemini still finished last on every reliability-adjusted metric in this benchmark. The result holds in the direction least favourable to our argument.

### D. Full Per-Site Breakdown (Numeric Reference)

### E. Data Files

Each task directory contains per-run output JSONs (with full step traces, token counts, and logs), screenshots, and error tracebacks where applicable. Batch 2 (`*_v2`) directories include instrumented logs with per-call LLM latency, parse retry counts, and parse failure counts.

Benchmark conducted by [Notte](https://www.notte.cc/). All models tested on their publicly available serverless API endpoints. Pricing as of March 2026.
