---
title: Dollars per token considered harmful
topic: infra-platform
subtopic: cost
secondary_topics:
- inference/serving
summary: Critiques dollars-per-token as an inference cost metric and explains why
  workload shape, latency, and utilization matter more.
source: modal
url: https://modal.com/blog/dollars-per-token-considered-harmful
author: null
published: '2025-07-16'
fetched: '2026-07-11T04:28:32Z'
classifier: codex
taxonomy_rev: 1
words: 1198
content_sha256: ff1e64055b12bc632cfbf6fe7ebe0bf1d0e81f47bda7dccf6181d849026b45d9
triage: keep
skip_reason: null
---

# Dollars per token considered harmful

[Back](https://modal.com/blog)

# Dollars per token considered harmful

[Charles Frye](https://twitter.com/charles_irl)

It is no secret that open source, self-hosted large language model inference has grown up in the shadow of proprietary services, like the APIs provided by OpenAI, Anthropic, and Alphabet.

What is less obvious is that the choices and priorities of those providers have shaped the expectations and discourse of the field in ways that are actively harmful to the inevitable move away from them.

One of the most pernicious of these subtle influences is in the pricing model: “dollars per token”.

### When you serve your own language model inference, you must think in terms of dollars per request, not dollars per token.

Here’s why:

- you are running language model inference in service of a language model application, and
- the users of your application don’t care about tokens, they care about requests, and therefore
- so should you.

## You are running language model inference in service of a language model application.

The API providers are running language model inference *as a service*. Running that service incurs costs which they recoup,
ideally but optionally plus a profit margin, by charging their users.

These costs roughly scale with the sizes of requests (both inputs and outputs).
These sizes are measured in complex non-linear transformations of Unicode bytes called *tokens*, rather than something sensible like bytes or characters,
due to contemporary model architecture skill issues.

Because token counts and costs scale together and sit at the boundary between the API and the people who build on it, they make for a good pricing mechanism: count tokens, charge dollars.

But when teams run their own language model inference, they are generally not running inference as a service. Instead, they have built some application of language models, like a support chatbot or an AI boyfriend or a meme coin shill, and they want to support that application at reduced cost, with more control, and/or with tighter data governance.

## The users of your application don’t care about tokens, they care about requests.

When the users of your B2B dog-sitting marketplace sit down to ask your chatbot whether pit bulls cost extra, they aren’t counting tokens. Introducing usage-based per-token billing will confuse and anger them. They aren’t thinking about language models at all! They are thinking about asking for help and getting it.

This is a *request*, part of a user workflow that they pay you to help complete.
As your application grows and more users hit your chatbot to inquire regarding per-breed pricing, the number of requests will scale, and so will your costs.

## So should you.

These requests are a key part of the boundary between you and your users, just as tokens are for the boundary between developers and LLM API providers. As the engineer of the LLM engine that supports the service for your users, tokens are part of your internal reasoning, but they are secondary.

Let’s consider a few questions that come up when evaluating LLM self-hosting and see why a per-request framing is so helpful.

*What latency is acceptable? Can I hit that latency?*

Well, how quickly do users need a response to a request? Once you have that, you can ask how many tokens are in a typical request and response.
Get those numbers, then compare them to published results for time-to-first-token and inter-token latency using a tool like our [LLM Engine Advisor](https://modal.com/llm-almanac/advisor) — or run the benchmarks yourself using our framework, [ stopwatch](https://github.com/modal-labs/stopwatch).

If you just think in terms of aggregate “tokens per second”, you can’t get meaningful numbers for latency estimation.

*How many replicas do we need to serve our traffic?*

Well, how many requests does a user make per second, and how many users are online at once?
(Note: that’s probably variable, so you’ll need to think about [managing your GPU allocation](https://modal.com/blog/gpu-utilization-guide) too!).
That will give you an estimate of the requests per second you need to serve.

For a given latency target on these queries, a single replica of your LLM engine will be able to serve a certain number of concurrent requests. The aggregate load of requests is then split among your replicas.

Again, if you think of your workload in terms of aggregate “tokens per second”, without considering requests, you’ll be unable to properly understand the load a single replica can handle.

Put simply: tokens cannot be arbitrarily split among replicas. Requests can. At best, you can be token-count-aware when routing requests.

*How much will this cost me?*

When you’re hosting your own LLM inference, you are paying for compute.

Costs for compute are measured in dollars over time — even for on-premises deployments, where capital costs are amortized over useful lifespans, on top of the time-denominated operating expenses that fully define costs in cloud deployments.

So once you’ve done the work to determine the number of requests you can support per replica while hitting your latency requirements and the number of replicas you need, you’re ready to determine the cost! You just take the dollars per second per replica offered by your compute provider times the number of replicas you need to get a total in terms of dollars per second to serve the workload.

### Dollars ÷ seconds = dollars ÷ seconds ÷ replicas × replicas

Tokens are, quite literally, no longer part of the equation.

*Is the cost worth it?*

This final question, typically the most important question teams face when considering whether to build their own LLM inference, is best considered with no regard at all to tokens.

When costs are framed in dollars per request, the end user perspective is brought back to the center, where it belongs, and conversations are elevated to the level where engineering can act in concert with product, design, and revenue.

Is $1 per request “worth it”? Yes, if satisfying those requests leads to a >1% increase in conversion rate for users with a life-time-value of $100! Is 10¢ per request “worth it”? No, if your users make 1k requests a month but only pay you $20!

Introducing the sizes of requests (denominated in tokens) into this discussion adds an extra dimension of variation that’s pure nuisance.
It’s the concern of an organization selling language model inference *per se*, not one building an application of language models or a system that includes that application.
And the dominance of those organizations, especially the ones selling proprietary models, is how we’ve ended up with this confused approach.

## If you’d like to keep your dollars per request down while taking language model inference into your own hands, try Modal.

We learned these lessons working with a variety of teams that are taking advantage of advances in open weights language models and open source language model inference engines
to build high-throughput, low-latency, low-cost, high-control LLM applications on our serverless infrastructure platform, [Modal](https://modal.com/).

If you’d like to read more about running your own language model inference,
check out the [executive summary of our LLM engine benchmarks](https://modal.com/llm-almanac/summary) or [dive into those benchmark results directly](https://modal.com/llm-almanac/advisor).
If you’re interested in more hard-won insights gained helping teams break free of “AI from an API”,
check out [our guide to thinking about GPU costs and optimizations](https://modal.com/blog/gpu-utilization-guide).
