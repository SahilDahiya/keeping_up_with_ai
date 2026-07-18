---
title: 'Claude Code Pricing: Plans, API Costs, and How To Lower Your Bill'
kind: blog
topic: null
subtopic: null
secondary_topics: []
summary: null
triage: null
skip_reason: null
source: fireworks
url: https://fireworks.ai/blog/claude-code-pricing
author: null
published: '2026-04-23'
fetched: '2026-07-18T06:38:19Z'
classifier: null
taxonomy_rev: 2
words: 2257
content_sha256: 409cd532316de9d7e3fcd2a4736a98454079cb7999c705cf185d313d64ab8c38
---

# Claude Code Pricing: Plans, API Costs, and How To Lower Your Bill

- What are the current Claude Code plans for Pro, Max, Team, Enterprise, and API usage?
- How does Claude API pricing work for input, output, cache, and batch rates?
- What drives Claude Code spend toward $150 to $250 per developer per month?
- How does Claude Code separate the coding tool from the model endpoint?
- How do Fireworks-hosted models compare to Claude on Artificial Analysis?
- How should teams evaluate model quality and total task cost?
- How do you route Claude Code, OpenCode, or another harness through Fireworks?
- How to keep Claude Code and use FireConnect
- How to use OpenCode, Cline or another harness with the OpenAI-compatible API
- Which Fireworks model is best to use with Claude Code?
- Is a lower-cost model layer worth it for your Claude Code bill?

If you are developing software professionally in 2026, there is a good chance you have used Claude Code. There’s an even better chance that your token consumption has increased at least 3x in the past year. With that, developers globally are now paying close attention to the cost of said token usage. Claude Code costs depend on how a developer accesses it. Pro, Max, and Team subscriptions include usage within plan limits. API users pay by token, while Enterprise combines a seat price with usage-based charges.

For API and Enterprise deployments, the selected model has a direct effect on cost. While Anthropic models are the default, Fireworks-hosted open-weight models such as [GLM 5.2](https://fireworks.ai/models/fireworks/glm-5p2), [Kimi K2.7 Code](https://fireworks.ai/models/fireworks/kimi-k2p7-code), and [MiniMax M3](https://fireworks.ai/models/fireworks/minimax-m3) are also accessible, and have lower per-token rates than Fable, Opus 4.8, or Sonnet 5. Many open-weight models have also narrowed the gap on agentic coding evaluations, although benchmark scores do not guarantee equivalent results on a particular repository.

Claude Code provides the coding interface and agent loop. Its configured model endpoint supplies the model behavior behind that interface. Fireworks supports two ways to test a lower-cost model layer:

- •**Keep Claude Code**: use[FireConnect](https://docs.fireworks.ai/ecosystem/fireconnect/overview)to route supported Claude Code model calls through Fireworks’ Anthropic-compatible endpoint. The CLI remains familiar, but model behavior, tool support, latency, and output quality can change.
- •**Use an OpenAI-compatible coding harness**: connect[OpenCode](https://opencode.ai/),[Cursor](https://cursor.com/),[Cline](https://cline.bot/),[Aider](https://github.com/Aider-AI/aider), or another compatible harness to Fireworks’ OpenAI-compatible API.

Evaluate either path with real repository tasks before standardizing. Compare completion rate, model spend, latency, retries, and human repair time rather than relying on token rates alone.

Anthropic offers subscription, usage-credit, and API-based ways to pay for Claude Code. The relevant cost model depends on the account and authentication method.

| Path | Current pricing (July 2026) | What it means for Claude Code | 
|---|---|---|
| Free | $0 | Anthropic's free tier supports Claude chat features. Claude Code requires a paid plan. | 
| Pro | $17/month (billed annually) | The first individual plan that includes Claude Code. Usage is included in the subscription, subject to plan limits. | 
| Max 5x / Max 20x | $100/month or $200/month | Includes Claude Code with 5x or 20x more usage than Pro, subject to plan limits. | 
| Team Standard | $20/seat/month (billed annually); 5-seat minimum | Includes Claude Code and Claude Cowork. Usage draws from rolling session and weekly allowances shared across Claude products. | 
| Team Premium | $100/seat/month (billed annually); 5-seat minimum | Includes 5x more usage than a Standard seat, subject to rolling session and weekly allowances. | 
| Enterprise | $20/seat plus usage at API rates | Includes Claude Code and Cowork, spend controls, governance, audit logs, and custom data retention. Usage cost varies by model and task. | 
| API usage | Model-specific input, output, cache, and tool costs | Claude Code usage authenticated through the API is billed by consumption. | 

For Pro and Max subscribers, usage is included within plan limits, so the dollar estimate shown by `/usage` is not a direct billing figure. The command still shows plan bars, activity statistics, and a breakdown of token usage. Subscription users who enable additional usage credits can incur charges after reaching their included allowance. API and Enterprise usage is priced according to model consumption.

Anthropic’s [Claude Code cost documentation](https://code.claude.com/docs/en/costs) reports an enterprise average of about $13 per active developer per day, or $150 to $250 per month. However, actual spend varies with the model, codebase size, context length, tool calls, subagents, automation, and parallel sessions.

[Claude API pricing](https://platform.claude.com/docs/en/about-claude/pricing) charges separately for base input, cache writes, cache hits, and output. Current list prices per million tokens are:

| Model | Base input | 5-minute cache write | 1-hour cache write | Cache hit | Output | 
|---|---|---|---|---|---|
| Fable 5 | $10 | $12.50 | $20 | $1 | $50 | 
| Opus 4.8 | $5 | $6.25 | $10 | $0.50 | $25 | 
| Sonnet 5 through August 31, 2026 | $2 | $2.50 | $4 | $0.20 | $10 | 
| Sonnet 5 starting September 1, 2026 | $3 | $3.75 | $6 | $0.30 | $15 | 
| Haiku 4.5 | $1 | $1.25 | $2 | $0.10 | $5 | 

Prompt caching charges 1.25 times the base input rate for a five-minute cache write and twice the base rate for a one-hour write. Reading cached content costs 10% of the base input rate. According to Anthropic, caching pays off after one cache read with the five-minute duration or after two reads with the one-hour duration.

Anthropic's [Batch API](https://platform.claude.com/docs/en/about-claude/pricing#batch-processing) discounts input and output tokens by 50% for eligible asynchronous workloads. Prompt-caching charges can still apply to batch requests, so teams should account for cache writes and reads separately from the discounted input and output rates.

Context size still controls much of the bill. Tool-heavy workflows add definitions, results, logs, diffs, and test output to each request. Extended thinking is also billed as output. If you’ve been using Anthropic models for a while, keep in mind that [Sonnet 5's newer tokenizer](https://platform.claude.com/docs/en/about-claude/models/whats-new-sonnet-5#new-tokenizer) produces approximately 30% more tokens than Sonnet 4.6 for the same text, with the exact increase depending on the workload. When trying to estimate potential costs, measure token use against representative repositories rather than extrapolating from a short prompt.

The $150 to $250 range comes from Anthropic's [enterprise deployment data](https://code.claude.com/docs/en/costs), not from the price of a typical Pro, Max, or Team subscription. Four variables account for much of the difference between a light pilot and a high-usage deployment:

- •**Model selection:**output from Fable or Opus costs more than output from Sonnet or Haiku.
- •**Context size:**repository files, instructions, tool definitions, logs, diffs, and test results can be resent across multiple turns.
- •**Task length:**long-running agents create more model calls, tool loops, and output tokens.
- •**Concurrency:**subagents and agent teams run separate context windows, so token use grows with the number of active instances and their runtime.

A change in the default model or effort level can change expected spend without a plan-price increase. A rollout budget should therefore track seat cost, model rate, repeated context, parallel agents, and tool payloads separately. Use a pilot to establish completion rate and cost per completed task before expanding access.

Claude Code manages the interface, repository context, tool loop, and session, while the configured endpoint supplies the model response that determines the next action. Routing the CLI to another provider can preserve the interface while changing model behavior behind it.

Fireworks exposes an [OpenAI-compatible endpoint](https://docs.fireworks.ai/getting-started/quickstart) at `https://api.fireworks.ai/inference/v1` and an [Anthropic-compatible endpoint](https://docs.fireworks.ai/ecosystem/fireconnect/claude-code) at `https://api.fireworks.ai/inference`. Configuration covers the endpoint, authentication, and model mapping. Before rollout, validate tool compatibility, context handling, caching, latency, and output quality against representative tasks.

Artificial Analysis publishes independent benchmarks across proprietary and open-weight models: the [Intelligence Index](https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index) covers broad reasoning, and the [Coding Index](https://artificialanalysis.ai/models/capabilities/coding) covers software-engineering performance. Fireworks-hosted open models run at materially lower token rates than Anthropic API models on [Fireworks serverless](https://docs.fireworks.ai/serverless/pricing).

| Model | Intelligence Index | Coding Index | Input / cached / output per MTok | 
|---|---|---|---|
| [Claude Fable 5](https://artificialanalysis.ai/models/claude-fable-5) | 60 | 76.5 | $10 / $1 / $50 | 
| [Claude Opus 4.8](https://artificialanalysis.ai/models/claude-opus-4-8) | 55.7 | 74.3 | $5 / $0.50 / $25 | 
| [Claude Sonnet 5](https://artificialanalysis.ai/models/claude-sonnet-5) | 53.0 | 72 | $2 / $0.20 / $10* | 
| [GLM 5.2](https://fireworks.ai/models/fireworks/glm-5p2) | 51.1 | 68.8 | $1.40 / $0.14 / $4.40 | 
| [Kimi K2.7 Code](https://fireworks.ai/models/fireworks/kimi-k2p7-code) | 41.9 | 60.8 | $0.95 / $0.19 / $4 | 
| [MiniMax M3](https://fireworks.ai/models/fireworks/minimax-m3) | 44.4 | 58.6 | $0.30 / $0.06 / $1.20 | 

Sonnet 5 introductory pricing runs through August 31, 2026. Rates increase to $3 input, $0.30 cached hit, and $15 output on September 1.

GLM 5.2 is the closest open-weight model to Claude models according to Artificial Analysis. Kimi K2.7 Code and MiniMax M3 trade larger score differences for lower token rates. Treat these scores as signals rather than proof of how these models will perform on a specific codebase.

Start with the [Artificial Analysis Coding Agent Index](https://artificialanalysis.ai/agents/coding-agents), which combines DeepSWE, Terminal-Bench v2, and SWE-Atlas-QnA results. Then run the same repository tasks through the strongest candidates and the current Claude default.

Track completed tasks, failed tool calls, retries, latency, repeated context, output tokens, and human repair time. A lower token rate only produces a lower total task cost when the model completes the work with an acceptable number of retries and corrections.

After choosing a model, use the current [Fireworks serverless pricing page](https://docs.fireworks.ai/serverless/pricing) to budget model-specific input, cached-input, and output rates. Keep repeated repository context cacheable where possible. For large asynchronous workloads, [Fireworks Batch API](https://docs.fireworks.ai/guides/batch-inference) reduces input and output prices by an additional 50%. Batch API is recommended for asynchronous work such as evals, migrations, and large refactors.

Teams can route Claude Code through [FireConnect](https://docs.fireworks.ai/ecosystem/fireconnect/overview), or route OpenCode, Cline, Aider, and other OpenAI-compatible coding tools through Fireworks’ OpenAI-compatible API.

[FireConnect](https://docs.fireworks.ai/ecosystem/fireconnect/claude-code) configures Claude Code to use Fireworks’ Anthropic-compatible endpoint and maps Claude model aliases to Fireworks models or routers.

- Install Claude Code and FireConnect.
- Authenticate with `fireconnect login`, or provide a Fireworks key when enabling the integration.
- Run `fireconnect claude on`.
- Restart Claude Code, start a new session, or use `/model`so the updated mapping takes effect.
- Run `fireconnect claude status`to inspect the active endpoint, model aliases, and Fireworks rates.

FireConnect stores the API key in the operating system keychain when available and uses `apiKeyHelper` to retrieve it at runtime. It also backs up the previous provider settings so `fireconnect claude off` can restore them.

Defaults can change between FireConnect releases. Use `fireconnect claude model list` to see callable serverless models and `fireconnect claude model select` to update the main, Opus, Fable, Sonnet, Haiku, or subagent slot. Claude Code may display Anthropic list-price estimates for aliased models, so use FireConnect status, the model list, or the Fireworks billing dashboard for actual Fireworks rates.

Anthropic compatibility does not guarantee support for every Anthropic-specific field or server-side tool. Validate the tools and settings your repository depends on before wider deployment.

For OpenCode, Cursor, Cline, Aider, or any other coding tool that accepts OpenAI-compatible configuration, the setup is manual but covers the same three parts:

- Set the base URL to `https://api.fireworks.ai/inference/v1`.
- Set the API key to your Fireworks key.
- Set the model ID in the format your tool expects.

Once configured, run the same repository task across two or three candidates and compare completion, latency, cache behavior, and total cost.

- •Cline: OpenAI Compatible, Base URL, API Key, Model.
- •Aider: `OPENAI_API_BASE`,`OPENAI_API_KEY`,`aider --model openai/<model-name>`.

Use benchmarks to create a shortlist, then verify each candidate against the repository and tools it will handle. As of July 2026, we recommend evaluating the following:

- •**GLM 5.2:**start here when benchmark performance is the main selection criterion among the three Fireworks-hosted models compared above.
- •**Kimi K2.7 Code:**test it for coding-focused workloads where its lower output rate offsets the benchmark difference.
- •**MiniMax M3:**include it when multimodal input is required or when a primary constraint is minimizing token cost

Keep a frontier Claude model in the evaluation set for hard debugging, complex refactors, and ambiguous requirements. Compare models on completed tasks and repair time, not only benchmark scores or token rates. Route a workload to a lower-cost model only when it clears the required quality threshold with acceptable latency and retries.

Claude Code's pricing is both high and layered: subscription tiers, per-token API rates, separate cache and batch charges, and a tokenizer change that quietly inflates token counts. Collectively, these compound and sit between you and a predictable bill. The complexity is exactly why the model layer is worth evaluating as a way to increase both savings and predictability. Many Fireworks customers have already run that test in production. A few noteworthy examples:

- Gumloop moved an internal production agent from Opus 4.8 to GLM-5.2 on Fireworks and saw [up to 72% cost savings](https://fireworks.ai/blog/gumloop)with no change in user experience.
- In Fireworks' research with [Harvey on the Legal Agent Benchmark](https://fireworks.ai/blog/open-source-agents-frontier-advisors), an open-source GLM 5.1 setup matched or beat Claude Opus on all-pass tasks at roughly 40% of the end-to-end Opus cost ($368 versus $954), and a[follow-up study](https://fireworks.ai/blog/frontier-open-source-worker-with-closed-source-advisor)generalized the pattern across coding, terminal, and legal benchmarks at 19% to 67% lower cost.

While open-source software is nearly always the most budget-friendly path, AI engineering teams understand that those savings are only worth it when an open model clears the quality bar on your repository, so it is critical validate performance on representative set of tasks or workflows. When it does clear the bar, keeping Claude Code and routing through [FireConnect](https://docs.fireworks.ai/ecosystem/fireconnect/overview) produces a significantly lower monthly bill while allowing developers to continue using the harness and daily workflows they’re already used to.
