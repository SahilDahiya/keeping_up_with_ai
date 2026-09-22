---
title: Qwen 3.7 Plus is now live on Fireworks
kind: blog
topic: null
subtopic: null
secondary_topics: []
summary: null
triage: null
skip_reason: null
source: fireworks
url: https://fireworks.ai/blog/qwen-3p7-plus
author: null
published: '2026-06-12'
fetched: '2026-09-22T06:11:58Z'
classifier: null
taxonomy_rev: 2
words: 1102
content_sha256: 42713d5f24b820f9fe8508d65a687502553f8e7e963d1ef6b4dfc934e6276250
---

# Qwen 3.7 Plus is now live on Fireworks

Why is this news? A handful of other services listed Qwen 3.7 within hours of Alibaba's June 1st announcement, and that [launch announcement](https://x.com/Alibaba_Qwen/status/2061506641120641494) was viewed nearly half a million times. This one is different: Alibaba has partnered directly with Fireworks to host and serve the Qwen 3.7 Plus weights on Fireworks infrastructure. There's as much to say about how it's being served as its stellar benchmarks.

To paraphrase the Qwen team's own framing: 3.7 Plus is not a chat model. It is an agent model. It sees the interface, it thinks, it writes code, and takes actions through both GUI or CLI. Verify results, and repeat the loop. Launch materials include an 11-hour app-development session with 10,000+ lines of code and 1,000+ agent calls. That type of workload shape, with long-running loops full of screenshots, tool calls, and cached context, is exactly the type of workload where a frontier-grade inference stack matters.

One practical detail for agent builders: the Qwen team recommends preserving thinking across turns for agentic tasks, and Fireworks supports it. Pass `reasoning_content` back in your assistant messages and set `reasoning_history="preserved"`, and the model keeps its reasoning from previous turns. Working examples are in the [reasoning guide](https://docs.fireworks.ai/guides/reasoning). There are certainly use cases where a long-horizon workflow is not necessary, and setting to `reasoning_history="disabled"` will likewise reduce unnecessary tokens.

Qwen 3.7 Plus is a frontier multimodal model. It understands images as well as text, and supports both thinking and non-thinking modes: request reasoning when the task needs it, skip it when it does not, same as any other hybrid-reasoning model.

Qwen 3.7 Plus is now on [serverless](https://docs.fireworks.ai/serverless/overview): pay per token, no infrastructure to manage, no cold starts. The facts are in the card below. Qwen 3.7 Max is coming soon; [talk to us](https://fireworks.ai/contact) if you want early access.

|  | Model Specs | 
|---|---|
| Model ID | accounts/fireworks/models/qwen3p7-plus | 
| Modalities | Text + image input, text output | 
| Reasoning | Thinking and non-thinking, selectable per request | 
| Context window | 262k tokens. | 
| Serverless Pricing | $0.50 / 1M input · $0.10 / 1M cached input · $3.00 / 1M output | 
| Batch | 50% below serverless pricing, results within 24h | 
| Training | limited availability, contact us if interested. | 
| Weight export | Not available (licensed weights; tuned models serve on Fireworks). | 
| APIs | OpenAI-compatible and Anthropic-compatible | 


On pricing: routed listings may quote lower numbers, and that is fine. Fireworks is the path for teams that want Qwen 3.7 Plus on Fireworks-operated infrastructure, under Fireworks data handling and SLAs, and at the speed, latency, and throughput that AI natives have come to expect.

There are two ways an API can deliver tokens from Qwen 3.7 Plus: __API routers__ and __inference providers__.

An API router receives your request and forwards it to an inference provider (e.g official Alibaba API), which then runs the inference. Routers are generally useful because they provide convenience: a single API key, many models, fallback options, and consolidated billing. Genuinely useful.

An inference provider runs the model directly. **Fireworks is an inference provider.** When you call our API, your request is processed on our infrastructure by our inference engine using weights we host. We do not forward your traffic to another endpoint. Ever.

As an inference provider, we make commitments about latency (we control the full serving path), data governance (e.g our [zero data retention policy](https://docs.fireworks.ai/guides/security_compliance/data_handling)), and reliability (our 99.9% uptime SLA). For additional details, we've written a longer piece on [the differences between inference providers and API routers,](https://fireworks.ai/blog/inference-providers-vs-api-routers) and the implications for each.

Hosting closed-weight models is not new territory for us. We have meaningful experience serving proprietary model weights under license for [hundreds of enterprise customers like Cursor and Notion](https://fireworks.ai/customers). What makes the Qwen 3.7 Plus program relatively novel is that we're making such a model available to all developers in the Fireworks community. Alibaba has licensed Fireworks to host and serve these weights directly, which means you get independent inference infrastructure, not a proxy, with all the performance and data handling properties that entails.

Qwen earned its position the open way: by [HuggingFace download data analyzed by Interconnects](https://www.interconnects.ai/p/8-plots-that-explain-the-state-of), Qwen has become one of the default open model families for local inference, reasoning, and multimodal workloads. Qwen 3.7 is the most capable release in that lineage, on a different distribution path: the Plus weights are not on HuggingFace. They are licensed, and Fireworks serves them independently under that license.

We want to be direct about that distinction rather than blur it. If you build on open-weights Qwen models, we serve those too, on the same stack. Qwen’s 8B parameter models remain among the most popular small models for fine-tuning on the [Fireworks training platform](https://fireworks.ai/training).

Benchmark tables are sticker specs: necessary, not sufficient. The full tables are in [Qwen's launch post](https://x.com/Alibaba_Qwen/status/2061506641120641494), but three results stand out. Qwen 3.7 Plus with thinking enabled matches the flagship Max on AIME 2025 (14/15) at roughly three times the speed. End-to-end throughput is 3.55× faster than Qwen 3.6 Plus. And on coding-agent tasks, early results show strong generalization across multi-file development, debugging, and issue-resolution workflows.

- •**Playground:** Take it for a quick spin in the browser here:[https://app.fireworks.ai/playground?model=?model=accounts/fireworks/models/qwen-3p7plus](https://app.fireworks.ai/playground?model=?model=accounts/fireworks/models/qwen-3p7plus)
- •**Serverless** : pay per token, with[prompt caching](https://docs.fireworks.ai/guides/prompt-caching) on by default (cached input tokens are $0.10 vs. $0.50, an 80% discount) and[rate limits that grow with your usage](https://docs.fireworks.ai/serverless/rate-limits) instead of fixed subscription tiers.
- •**Better yet, drop it into your preferred coding agent**

Fireworks ships an [Anthropic-compatible API](https://docs.fireworks.ai/tools-sdks/anthropic-compatibility) alongside the OpenAI-compatible one, so Qwen 3.7 Plus works in the harness you already use. These are the same harnesses Alibaba's own tooling targets; the difference is what runs underneath.

**Claude Code**: one command via [FireConnect](https://github.com/fw-ai/fireconnect).

`pythonCopy`
123

Prefer not to pipe curl into bash? The manual `settings.json` path is in the [integration guide](https://docs.fireworks.ai/ecosystem/integrations/claude-code).

**OpenCode**: `/connect → fireworks.ai → /models` 

Anything else with custom endpoints:

- •OpenAI-compatible at `https://api.fireworks.ai/inference/v1`
- •Anthropic-compatible at `https://api.fireworks.ai/inference`

Qwen 3.7 Plus is available on serverless now via the Fireworks API, on the same Fireworks fleet that processes over 30 trillion tokens every day.

Support for fine-tuning may be [available on-request](https://fireworks.ai/contact). Availability of the larger flagship variant, Qwen 3.7 Max will likewise be coming soon. For early-access, please reach out.

Pricing is highly attractive coming in 5-15x cheaper than leading close-source models.

| Token Type | Price per 1M | 
|---|---|
| Input | $0.40 | 
| Output | $1.60 | 
| Cache hit | $0.08 | 

[→](https://fireworks.ai/models/fireworks/minimax-m3)[Start building with Qwen 3.7 Plus today](https://fireworks.ai/models/fireworks/qwen3p7-plus) [←](https://fireworks.ai/models/fireworks/minimax-m3)

Questions? Join our [Discord](https://discord.gg/fireworks-ai) or [contact us](https://fireworks.ai/contact) to schedule a meeting with our solutions team.
