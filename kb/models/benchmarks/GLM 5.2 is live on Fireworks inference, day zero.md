---
title: GLM 5.2 is live on Fireworks inference, day zero.
kind: blog
topic: models
subtopic: benchmarks
secondary_topics:
- inference/serving
summary: Independently reproduces Z.ai's GLM 5.2 launch benchmarks on Fireworks' own
  GPUs and inference engine (91.4% GPQA-Diamond vs the reported 91.2%), and explains
  the difference between running an inference-provider-hosted model directly versus
  via an API router.
triage: null
skip_reason: null
source: fireworks
url: https://fireworks.ai/blog/glm-5p2
author: null
published: '2026-06-16'
fetched: '2026-09-22T06:10:54Z'
classifier: claude
taxonomy_rev: 2
words: 1036
content_sha256: 234eb5e8d3930fa95df45cc9868f13b529c650bb57ec47b1ea51d826c0211eae
---

# GLM 5.2 is live on Fireworks inference, day zero.

Z.ai, formerly known as Zhipu, is one of China's "six tigers" of AI. Founded way back in 2019, it became the first of the group to go public in early 2026, listing in Hong Kong as the world's first large-model stock. Today [Z.ai](http://z.ai) released GLM 5.2, its newest flagship, built for long-horizon tasks on a solid 1M-token context. The launch came with detailed benchmarks positioning GLM 5.2 as the strongest open-source model for coding, closing much of the gap to the closed frontier.

Launch-day benchmarks tend to come with an asterisk. Every provider runs them on its own infrastructure and harness, which is why cross-model comparisons are always contentious. We saw plenty of social activity this past weekend deliberating on GLM 5.2 versus Kimi K2.7 Code. As a leading inference and training platform, the Fireworks POV is that the best coding model is the one that fits your workload. AI natives at the frontier truly understand and rely on their own evals, not simply what comes from a vendor chart or social feeds.

Nevertheless, by Z.ai's published results, GLM 5.2 takes back the crown as the strongest open-source model on pure coding benchmarks and the highest-ranked open model on its long-horizon evals.

We did not take Z.ai's numbers on faith, and you should not take ours on faith either. We ran our own validation on Fireworks GPUs, through the Fireworks inference engine:

- •On GPQA-Diamond, GLM 5.2 scores **91.4% running on Fireworks' own engine and GPUs** (181/198, high reasoning), validating Z.ai's reported**91.2%** .

This isn't a number we forwarded from someone else's endpoint. We ran the open weights on our stack and reproduced frontier-level reasoning independently.

There are two ways an API hands you tokens from GLM 5.2. A router forwards your request to someone else's endpoint, often the model maker's own API: convenient, one key, many models, and the right call for plenty of workloads.

[Fireworks is not a router](https://fireworks.ai/blog/inference-providers-vs-api-routers). Your request runs on Fireworks infrastructure, through the Fireworks inference engine, on weights hosted in-house. The traffic is never forwarded anywhere. Ever. That buys you a fully controlled serving path, a zero-data-retention policy, and an uptime SLA. Same model, run by us, measured by us, served end to end.

GLM 5.2 is a coding-first model built for agents that run for a long time, and its headline feature is a solid 1M-token context window.

Long-horizon is where the frontier is now contested. Developers no longer babysit one task at a time; they keep several projects running at once, and throughput depends on how long an agent can work unattended. A model that needs a human nudge every two minutes lets you build one thing at a time. A model you can leave for two hours, or a full day, enables the proverbial 10x or 100x engineer. Maintaining quality for such long-horizon tasks is increasingly where the frontier of AI is being contested, and it’s easier said than done. From the [Z.ai technical blog](https://z.ai/blog/glm-5.2):

A 1M context is easy to claim, but much harder to keep reliable under real engineering pressure.

This is ultimately an infrastructure problem: pushing context to 1M moves the bottleneck off compute and onto KV-cache capacity, kernel overhead, and CPU-side scheduling. A 1M window is only worth anything if it stays coherent at hour six of an autonomous run, holding a repository, its tests, and a long trace of tool calls without degrading under load. Keeping it reliable under that pressure is what the Fireworks inference stack is built for, and it is where model quality and serving quality compound: the cost that matters is not the per-token rate, it is the completed task.

GLM may have only burst into the frontier conversation in late 2025, but teams that already lean on GLM 5.1 for production workloads are ready for the latest flagship:

"We've been using GLM 5.1 as our workhorse model for DarcyIQ since April 2026 and have been incredibly happy with the model intelligence, stability and speed provided by Fireworks. We're excited to bring GLM 5.2 to all DarcyIQ customers today." 

-Travis Rehl, CTO, Innovative Solutions

GLM 5.2 ships under an MIT license: commercial use, modification, redistribution, no copyleft strings, and no regional limits. It is the latest in a fast run of open releases in the past week, alongside new flagships from Kimi, Qwen, DeepSeek, and MiniMax.

As US policy sharpens its scrutiny of frontier models and continues to suck oxygen out of the twittersphere, the open-weight ecosystem keeps shipping. GLM 5.2 is now live on Fireworks for everyone, devs and LLM researchers alike.

Public benchmarks, Z.ai's and ours included, answer a general question, not yours. A leaderboard winner can still lose on your codebase, your prompts, and your latency budget. The reliable way to choose is to test candidates on the work you actually ship, then keep the one that wins.

That is the layer we are building toward: first-party evals at the application level, plus fine-tuning. Our training platform reaches general availability soon, and in the meantime we are working with customers in preview who want early access. If you want a head start, reach out through our [training preview](https://fireworks.ai/contact-training).

- •**Playground:** Take it for a quick spin in the browser here:[https://app.fireworks.ai/playground?model=?accounts/](<https://app.fireworks.ai/playground?model=?model=accounts/fireworks/models/glm-5p2 >)[fireworks/models/glm-5p2](<https://app.fireworks.ai/playground?model=?model=accounts/fireworks/models/glm-5p2 >)
- •**Serverless** : pay per token, with[prompt caching](https://docs.fireworks.ai/guides/prompt-caching) on by default (cached input tokens are $0.26 vs. $1.40, an 80% discount) and[rate limits that grow with your usage](https://docs.fireworks.ai/serverless/rate-limits) instead of fixed subscription tiers.
- •**Better yet, drop it into your preferred coding agent**

Fireworks ships an [Anthropic-compatible API](https://docs.fireworks.ai/tools-sdks/anthropic-compatibility) alongside the OpenAI-compatible one, so just plug it into the harness you already use.

**Claude Code**: one command via [FireConnect](https://github.com/fw-ai/fireconnect).

`bashCopy`
123

Prefer not to pipe curl into bash? The manual `settings.json` path is in the [integration guide](https://docs.fireworks.ai/ecosystem/integrations/claude-code).

**OpenCode**: `/connect → fireworks.ai → /models` 

Anything else with custom endpoints:

- •**Model id:** accounts/fireworks/models/glm-5p2
- •**OpenAI-compatible:**`https://api.fireworks.ai/inference/v1`
- •**Anthropic-compatible:**`https://api.fireworks.ai/inference`

| Token Type | Price per 1M | 
|---|---|
| Input | $1.40 | 
| Output | $4.40 | 
| Cache hit | $0.26 | 

Try it out today. Fast and Priority tier will be coming soon as described in the [serverless docs](https://docs.fireworks.ai/guides/serverless-products).

[>> Start building with GLM 5.2 here <<](https://fireworks.ai/models/fireworks/glm-5p2)

Questions? Join our [Discord](https://discord.gg/fireworks-ai) or [contact us](https://fireworks.ai/contact).
