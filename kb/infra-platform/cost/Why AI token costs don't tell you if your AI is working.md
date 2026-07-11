---
title: Why AI token costs don't tell you if your AI is working
topic: infra-platform
subtopic: cost
secondary_topics:
- evals-observability/evaluation
summary: Explains why token cost alone is an incomplete production metric and how
  quality, latency, and outcomes must be measured together.
source: arize
url: https://arize.com/blog/why-ai-token-costs-dont-tell-you-if-your-ai-is-working/
author: Laurie Voss
published: '2026-06-19'
fetched: '2026-07-11T04:56:49Z'
classifier: codex
taxonomy_rev: 1
words: 1693
content_sha256: 4689554d649917da4c7c97f5385c67a0c01c1d8deca42f42b40e74a70c82e23e
---

# Why AI token costs don't tell you if your AI is working

In April, Uber’s CTO disclosed that the company had burned through its entire 2026 AI coding budget in four months. Uber’s president and COO, Andrew Macdonald, called it a “head-exploding moment,” and on the Rapid Response podcast he put his finger on why: he could not connect rising Claude Code usage to anything shipped. “Maybe implicitly there’s more that is getting shipped,” he said, “but it’s [very hard to draw a line](https://fortune.com/2026/05/26/uber-coo-ai-spending-tokens-claude-code/) between one of those stats and ‘okay, now we’re actually producing like 25% more useful consumer features'”.

That’s a huge problem for all of tech in an era of exploding AI usage. Spend is counted in tokens, but value shows up as shipped features, resolved tickets, accepted changes. Nobody has shown those two numbers move together, and at Uber they couldn’t: [token consumption](https://arize.com/docs/ax/observe/dashboards/token-counting) climbed for months while the line to delivered value stayed, in the COO’s own account, impossible to draw. **When your cost metric and your value metric don’t correlate, watching the cost metric tells you almost nothing about whether the spend is working.**

So measure something else. Instead of tracking [token spend](https://arize.com/docs/ax/instrument/track-costs), track [cost per outcome](https://arize.com/blog/data-fabric-querying-agent-traces-in-bigquery/): dollars per resolved ticket, per accepted PR, per shipped feature. That number tells you what you actually want to know. It is also much harder to get, because no API bills you in it and most teams have no way to compute it. Getting it is the real work, and the rest of this post is about why you need to, and how.

**But first: what is cost per outcome?**

Cost per outcome measures AI spend against successful results rather than token consumption. Examples include cost per resolved support ticket, cost per accepted pull request, cost per passing test, or cost per shipped feature. Unlike token usage, cost per outcome directly connects AI spending to delivered value.

**Tokens are getting cheaper**

The first half of the confusion is that per-token prices are collapsing, and have been for years.

![Model price at launch, 2023 to 2026](https://arize.com/wp-content/uploads/2026/06/model-price-at-launch-2023-2026.png)

When GPT-4 launched in early 2023 it cost about $60 per million output tokens. GPT-4 Turbo halved that. GPT-4o halved it again. By late 2024 DeepSeek V3 was [under $1.50](https://intuitionlabs.ai/articles/llm-api-pricing-comparison-2025), and in May 2026 DeepSeek made its V4-Pro pricing [permanent at $0.435 input and $0.87 output](https://www.bloomberg.com/news/articles/2026-05-23/deepseek-to-make-permanent-75-discount-on-flagship-ai-model) per million tokens, a model scoring within a fraction of a point of Claude Opus 4.7 on SWE-bench Verified at roughly a thirtieth of the per-output-token price.

A scatter of launch prices slopes down and to the right, but it understates the trend, because it mixes premium and budget models at each date. The better way to measure is to hold capability constant and ask what a fixed level of performance costs over time. Epoch AI did exactly that across six benchmarks and found the price to reach a given performance milestone has [fallen between 9x and 900x per year](https://epoch.ai/data-insights/llm-inference-price-trends), depending on the milestone. The cut is not a temporary subsidy either: DeepSeek attributes its pricing to genuinely lower serving cost per token from compressed attention and aggressive caching, not money lit on fire to buy share.

If your bill were simply a function of the per-token price, this would be a story about budgets shrinking every quarter, but it isn’t.

**But your inference bill keeps rising**

The reason is that consumption is growing faster than price is falling, and it’s not close.

The reason why is that [tokens per task](https://arize.com/docs/ax/observe/tracing/view-and-manage-traces) are exploding. Cursor’s Spring 2026 data shows the ratio of input to output tokens [climbing from about 4.5x in January to a peak above 13x in April](https://cursor.com/insights) as agents pull ever more context before they act. Agent sessions are getting deeper, and Anthropic’s Opus 4.8 shipped with Dynamic Workflows that fan out into parallel subagents, where a single instruction can consume what used to be a week of an engineer’s quota. Anthropic made a point of noting Opus 4.8 uses [15% fewer turns and 35% fewer output tokens](https://artificialanalysis.ai/articles/claude-opus-4-8-analysis-and-benchmarks) than its predecessor on agentic work, which tells you the per-task trend was alarming enough that efficiency became a headline feature. Looking further out, Goldman Sachs estimates agentic AI could drive a [24-fold increase in token consumption by 2030](https://fortune.com/2026/05/22/microsoft-ai-cost-problem-tokens-agents/). **You’re getting better outcomes, but it’s costing more.**

The aggregate already shows it. OpenRouter, the multi-model routing layer, reported that weekly token volume [grew from 5 trillion to 25 trillion over six months](https://openrouter.ai/announcements/series-b), a fivefold jump it attributes to enterprises moving from experiments into production. Per-token prices fell over that same window. There are simply far more tokens flowing per unit of work, and consumption growth is outrunning price decline by a wide margin.

This is not one company’s mistake. Gergely Orosz’s 2026 survey of software engineers found that developers using AI tools heavily routinely [hit usage limits, after which their employers have to pay more](https://newsletter.pragmaticengineer.com/p/the-impact-of-ai-on-software-engineers-2026), that engineering leaders responsible for budgets are broadly worried about where costs are heading, and that the trajectory is widely seen as unsustainable, propped up for now by vendor subsidies.

So companies are reaching for the only lever they can see: a cap. Pricing across the tooling market has fragmented into [credits, tokens, quotas, premium requests, and daily caps](https://www.nxcode.io/resources/news/ai-coding-tools-pricing-comparison-2026), and even Anthropic’s own consumer Claude Code plans meter access in messages per rolling window. Capping spend controls the bill, but it is a blunt instrument: it limits tokens without any idea whether those tokens were producing value or being wasted. You throttle the good work and the wasteful work in equal measure, because the token count cannot tell them apart. **The cap is what you build when tokens are the only number you have.**

**The fix is cost per outcome**

The way out is to change the denominator. Stop dividing cost by tokens and start dividing it by outcomes.

Cursor’s own data shows why this works. Across model families, the cost per agent request varies by nearly 9x. But the [cost per accepted line](https://arize.com/blog/what-we-learned-testing-7-models-under-the-same-agent-harness/) of code varies by [only about 7x](https://cursor.com/insights). The gap shrinks because the pricier models get more of their output accepted by developers, so their higher per-request cost is spread across more code that actually survives into the codebase. Measured per request, an expensive model looks expensive. Measured per accepted line, the unit that reflects real work delivered, some of that premium is earned back, and the ranking of which model is the better buy can flip. Cost per accepted line is one version of it; cost per resolved ticket, per passing test, and per shipped feature are the same idea pointed at whatever your team produces. **The shift in what you measure gives you actionable visibility.**

A whole category of vendors has already moved here, because their customers forced it. Sierra bills per resolved customer interaction, not per conversation and not per seat, and is blunt about why seat-based rivals cannot follow: [the more effective their agent becomes, the fewer seats their clients need](https://sierra.ai/blog/outcome-based-pricing-for-ai-agents), so their revenue model fights their own product. Intercom’s Fin agent charges [$0.99 per outcome](https://fin.ai/pricing), billed only when it resolves an issue or completes a handoff, with escalations explicitly not billed. Decagon, Lorikeet, Zendesk, and others price the same way. The market is converging on outcome-denominated billing because customers stopped accepting usage as a proxy for value.

There is a reason this changes decisions rather than just tidying up the accounting. A resolved support interaction costs pennies in compute, while the value of that resolution, a $5 to $15 human ticket avoided or a subscriber retained, [dwarfs it](https://www.getmonetizely.com/agents/sierra-ai). Per-token cost cannot see that ratio. Cost per outcome on the other hand is exactly what you need: **it’s the number that tells you whether to spend more or spend less**.

**Evals are how you get there**

Outcome-based pricing works for a support vendor because “resolved” is observable: the customer confirms it or stops asking. For most internal agent work, the outcome is not handed to you. Did the agent’s PR actually fix the bug, or just pass the one test it wrote? Did the research agent’s summary hold up, or quietly invent a citation? You cannot divide cost by an outcome you are not measuring, and measuring outcomes for non-trivial agent work is itself an evaluation problem.

That is the work that cost per outcome demands:

- **Capture every agent run as a trace,**so the tokens spent are attributable to a specific task and the steps it took, not just to a user or a billing month.
- **Evaluate whether each run actually succeeded,**using graded checks, LLM-as-judge where appropriate, and outcome labels tied to what the task was for, so that “success” is a measured value and not an assumption.
- **Divide spend by measured success,**so you have a real cost per outcome for each kind of work. That single number is what tells you whether the investment is paying off, and it is what lets you act: justify the spend, cut what isn’t working, or route a class of work to the model that is cheapest per resolved outcome, which is frequently not the one that is cheapest per token.

This is precisely what an observability and evaluation layer is for, and it is where [Arize AX](https://arize.com/docs/ax) fits. AX captures agent traces, attaches evals to them so each run carries a pass or fail tied to a real outcome, and turns the result into a cost-per-outcome number you can put in front of finance and stand behind. None of that requires a new pricing model from your providers. It requires measuring the thing you actually care about, then dividing by it.

The per-token price war will keep producing headlines about intelligence too cheap to meter. It’s real, but it’s also entirely beside the point. The question every team is actually trying to answer is whether the money going into AI is coming back out as something worth more than it cost. Token spend cannot answer that. Cost per outcome can. The teams that come out ahead over the next year are the ones who can say, to the dollar, what they are getting for what they spend. You will not know if AI is working for you until you can.
