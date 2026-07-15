---
title: 'How to measure AI productivity: From LLM token costs to business value with
  Arize AX'
kind: blog
topic: evals-observability
subtopic: evaluation
secondary_topics:
- infra-platform/cost
summary: Argues token/prompt/LOC counts don't measure AI productivity (citing METR's
  finding that developers were 19% slower with AI while feeling 20% faster) and proposes
  a five-dimension framework, built on a shared correlation_id tagging contract, that
  joins traced AI work to outcomes like merged non-reverted PRs via Arize AX.
triage: null
skip_reason: null
source: arize
url: https://arize.com/blog/how-to-measure-ai-productivity-llm-cost-business-value/
author: Duncan McKinnon; Jitendra Yadav
published: '2026-07-14'
fetched: '2026-07-15T06:44:31Z'
classifier: claude
taxonomy_rev: 2
words: 1739
content_sha256: 5632ea150dbabbc35295eb030ae78430e184c7c157bedcc1b361fc2940e20ab1
---

# How to measure AI productivity: From LLM token costs to business value with Arize AX

*Co-Authored by Duncan McKinnon, AI Forward Deployed Engineer & Jitendra Yadav.*

**AI productivity is best measured by connecting AI usage to validated downstream outcomes.** Tokens, prompts, and generated lines show activity, but they do not prove value. A better measurement model tracks the cost of AI work, scores the quality and task success of that work, then joins each trace to outcomes such as merged PRs, resolved tickets, customer conversions, or avoided support effort.

The hard part is the join: AI activity lives in model and tracing telemetry, while business outcomes live in GitHub, Jira, CRM, product analytics, and support systems. Without a shared correlation ID, teams can report usage but not value.

Companies measure AI productivity in two ways: activity metrics that are both easy to collect and easy to misread (tokens consumed, prompts sent, lines generated), and outcome metrics that actually reflect value but require connecting AI usage to what happened downstream (a pull request merged and held, a ticket resolved and not reopened, a customer task completed). Almost everyone reports the first, but almost no one can produce the second.

That gap is now the defining problem of enterprise AI. [MIT’s 2025 GenAI Divide study](https://fortune.com/2025/08/18/mit-report-95-percent-generative-ai-pilots-at-companies-failing-cfo) found roughly 95% of enterprise generative-AI pilots deliver no measurable business impact and the cause is organizational, not technological: companies cannot connect AI to their workflows or measure what it returns. Spending has no such problem scaling. In a [Tangoe/Vanson Bourne survey](https://www.tangoe.com/news/genai-and-ai-drive-cloud-expenses-30-higher-and-72-say-spending-is-unmanageable/) of 500 IT and finance leaders, 72% called GenAI-driven cloud spending “unmanageable” as usage-based costs climbed. The bill scales effortlessly. The evidence of value does not.

## TL;DR

- Activity is not productivity. Tokens, prompts, and generated lines measure motion, not value.
- The feeling of productivity is not the measurement of it. In a controlled trial, developers using AI were slower while certain they were faster.
- Frameworks such as DX Core 4 treat productivity as multiple linked dimensions. For AI, use five: speed, effectiveness, quality, business impact, and efficiency.
- Arize AX puts cost and value on the same trace, then ties both to the real downstream outcome.
- **Want to try for yourself?**Arize provides an open source tracing solution for coding harnesses.- [Explore it on GitHub](https://github.com/Arize-ai/coding-harness-tracing).

## Why token usage is not a reliable AI productivity metric

The easiest AI metrics to collect have become the most deceptive. Industry estimates put AI-assisted code at roughly 40% of new code in professional workflows. Lines of code measure the model’s verbosity, not the engineer’s value; commit and PR counts climb simply because assistants make pushing more trivial. And more output is not better output: [GitClear](https://www.gitclear.com/coding_on_copilot_data_shows_ais_downward_pressure_on_code_quality/) finds code churn, lines reverted or rewritten within two weeks, approaching double its pre-AI baseline (from roughly 3.3% toward 7%+), while the [2024 DORA report](https://cloud.google.com/blog/products/devops-sre/announcing-the-2024-dora-report) estimated that for every 25% increase in AI adoption, delivery stability fell 7.2% and throughput fell 1.5%. The deepest version of the trap is perception itself. In a [2025 randomized controlled trial](https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/), METR found experienced open-source developers were 19% slower on real tasks with early-2025 AI tools while estimating they had been about 20% faster. The most influential AI productivity metric in most organizations is a feeling, and the best evidence says that feeling is unreliable. METR’s later work suggests newer tools can shift that result, but the perception gap is the durable lesson: you cannot manage what you only feel. The only correction is objective measurement. ![](https://arize.com/wp-content/uploads/2026/07/current_state_clean_1.gif)


## The five dimensions of AI productivity measurement

Handing leadership a single AI productivity number is how programs end up optimizing the wrong thing. Productivity is better measured across five dimensions. The first four map closely to DX Core 4’s speed, effectiveness, quality, and business-impact categories; efficiency adds the AI-specific denominator of token and dollar cost.

Efficiency is not a DX Core 4 label, but it is the denominator that keeps the other four honest. Held together, these resist gaming. Output without quality is just churn, and impact without efficiency is value bought at a loss. Measured as a vector, productivity becomes a portfolio: what to scale, what to fix, what to retire. DX Core 4 also makes an important fairness point: speed metrics like diffs per engineer should be reported at the **team** level, never tied to individual performance reviews. Outcome-based AI metrics inherit that protection when the score only moves on work that merges, resolves, and holds.

## How to measure AI productivity objectively with Arize AX

Start with one workflow, one validated outcome, and one guardrail. For example: a merged PR that is not reverted within a defined window, with change-failure rate as the guardrail.

- **Tag the work:**Add a stable attribution contract to every trace and span:- `team_id`,- `feature_id`,- `workflow_id`, model,- `prompt_version`,- `cost_usd`, and- `correlation_id`. This is the raw material- [Agent Studio](https://arize.com/docs/ax/agents/agent-studio)works from; it runs agent workers, bound to a tracing project, in interactive sessions or scheduled automations, so investigations and fixes stay grounded in the same tagged traces.
- **Score the work:**Use deterministic checks where possible, then calibrated LLM judges or human review for nuanced criteria such as task success, faithfulness, trajectory quality, and failure modes.- [Agent-as-a-Judge](https://arize.com/docs/ax/evaluate/agent-as-a-judge)(currently in closed Enterprise beta) runs each evaluation as a Claude Code agent in a sandbox: rather than mapping a fixed prompt to fixed columns, you describe the scoring criteria in plain language, and the agent reads the actual spans and trace context for the task window before scoring. That makes it a better fit for nuanced calls, trajectory quality, multi-step reasoning, and whether a goal was actually met than a single-shot LLM judge.
- **Join the work to outcomes:**Connect traces to GitHub, Jira, CRM, analytics, or support systems so AI work can be tied to merged PRs, resolved tickets, customer actions, or revenue events. Quality and efficiency are readable in the trace; business impact lives in those external systems. Use the same- `correlation_id`in the trace and the system of record, or join on it in a warehouse. A coding session can then link to the PR it produced and whether that PR merged and held. That’s the difference between “the agent generated 40 PRs” and “the agent contributed to 31 that merged and survived in production.”
- **Roll up cost against value:**Report cost per validated outcome by team, feature, workflow, or agent deployment, combining the attribution from step 1, the quality signal from step 2, and the real-world outcome from step 3. Show outcome volume and quality guardrails beside the ratio.

### How this works for coding agents and production AI features

**For coding agents**, track cost per merged, non-reverted PR, median cycle time, task-success rate, and rework or churn, each tied to code that shipped and stayed. A team can then test the productivity claim with data instead of the perception METR showed we can’t trust. **For production AI features**, the metric stops being cost per call and becomes cost per successfully resolved request, with quality, latency, and a product outcome such as conversion, deflection, or task completion attached.

## How to measure AI productivity without employee surveillance

Objective does not mean intrusive. Default reporting to the team, feature, workflow, or agent deployment level; do not use these metrics for individual performance reviews. That is why DX Core 4 reports speed at the team level, to prevent gaming and individual surveillance. Collect user_id only when it is necessary for debugging or product analytics, with access controls and retention limits. Outcome-based metrics carry that protection inherently: no one gains by generating more tokens when the score only moves on work that merges, resolves, and holds. The data shows where to invest and where to expand AI tooling, not who to watch.

## From AI usage metrics to business value

The productivity conversation stops running on anecdote and perception. Cost and value sit on the same trace; output is scored for quality, not counted; AI work is tied to the outcomes it produced. Leadership can see what the investment returns, and engineers can prove their tooling produces durable value. That measurement layer is the difference between programs that scale and those quietly shut down in the next budget cycle. ![](https://arize.com/wp-content/uploads/2026/07/reference_arch_clean_3.gif) Put together, the pieces answer a single question: what did this token actually produce? The graphic reads top to bottom, and it starts where the trouble starts, with why that question is so hard to answer today. The trouble is three disconnected silos—finance tracks dollars spent, engineering tracks tokens and prompts, and product runs surveys and goes on gut feel. Because none of them share a key, the numbers never join up, and that disconnect is why roughly 95% of GenAI pilots can’t show measurable ROI. Arize AX closes the gap in four stages over the same traces:

 Put together, the pieces answer a single question: what did this token actually produce? The graphic reads top to bottom, and it starts where the trouble starts, with why that question is so hard to answer today. The trouble is three disconnected silos—finance tracks dollars spent, engineering tracks tokens and prompts, and product runs surveys and goes on gut feel. Because none of them share a key, the numbers never join up, and that disconnect is why roughly 95% of GenAI pilots can’t show measurable ROI. Arize AX closes the gap in four stages over the same traces:

- **Instrument:**captures spans via OpenInference / OTel, carrying a tagging contract that stamps each one with the metadata attribution needs:- `feature`,- `team`,- `user_id`, and- `correlation_id`.
- **Evaluate:**scores each trace for quality, task success, and faithfulness, online and offline, with human annotation in the loop.
- **Join:**links each trace to a real outcome in GitHub, Jira, or your CRM and stamps it with an impact label, so “value” becomes a result instead of a proxy.
- **Attribute:**weighs cost against value and rolls it up by engineer, team, and feature, surfacing the cost-vs-value quadrant, scorecards, and alerts.

Followed end to end, a single unit of work travels the full path: tokens spent → trace captured → tagged → quality scored → outcome joined → cost ÷ value → decision. Two dependencies decide whether any of this holds:

- **The tagging contract makes every roll-up possible. Attribution is only ever a group-by on metadata that already lives on the span.**
- **The correlation id**makes business impact knowable. The same identifier has to sit on both the trace and the outcome, or value stays an estimate forever.

Get those two right and the rest is mostly plumbing.
