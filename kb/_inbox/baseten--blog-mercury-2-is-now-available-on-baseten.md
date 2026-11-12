---
title: Mercury 2, the first reasoning diffusion LLM, is now on Baseten
kind: blog
topic: null
subtopic: null
secondary_topics: []
summary: null
triage: null
skip_reason: null
source: baseten
url: https://www.baseten.co/blog/mercury-2-is-now-available-on-baseten
author: Kumar Chellapilla
published: '2026-06-11'
fetched: '2026-11-12T06:15:00Z'
classifier: null
taxonomy_rev: 2
words: 1264
content_sha256: 20162c06dd8d0b60356f0e663190252640955e73575e2d72e86a3da7de3c69f0
---

# Mercury 2, the first reasoning diffusion LLM, is now on Baseten

AI models
# Mercury 2, the first reasoning diffusion LLM, is now on Baseten

Inception's Mercury 2 is the fastest reasoning LLM, 5-10x faster than leading speed-optimized models at comparable quality.


- Authors
- Date
- June 11, 2026

TLDR

Inception's Mercury 2 is now live on Baseten, making us the first inference platform to deliver production-grade diffusion LLMs (dLLMs) to developers. Mercury 2 runs over 1,000 tokens per second on widely-deployed NVIDIA GPUs, at less than half the cost, with comparable quality to Haiku and GPT-5 mini. It delivers real-time speed that used to require specialized hardware, with no custom chips and no lock-in. Customers like Augment Code are already running it in production, cutting costs by 90% and latency by 82% on critical workloads.

Traditional autoregressive LLMs generate tokens one at a time. Each token depends on the one before it, so generation is sequential by design, with a hard ceiling on speed. Over time, clever workarounds have been built, like speculative decoding and multi-head architectures, to predict several tokens at once. But these are inference-time patches on a model that's still autoregressive underneath. They ease the bottleneck without removing it.

Diffusion takes a different path. Our partner, [Inception](https://www.inceptionlabs.ai/), is one of the leading labs building here, and instead of patching the constraint, dLLMs remove it. Rather than committing to one token at a time, it drafts the full output and refines it over several parallel passes, using the whole sequence to improve each part. Because this is built into how the model is trained and run, the speed is coming from the model itself, not a decoding optimization layered on top. It also opens a far richer design space, with more headroom for improvements ahead.


This isn't a marginal improvement. Augment Code, one of the first teams to run Mercury 2 in production on Baseten, cut costs by 90% and latency by 82% on a core part of their coding agent. And the gains aren't limited to coding: [diffusion's speed](https://www.inceptionlabs.ai/blog/introducing-mercury-2) opens up use cases that were previously very hard to serve, from real-time voice agents to sub-second tool routing and token-efficient subagents.

*"Our goal at Inception is to fundamentally redefine the economics and performance of LLMs so that they become more useful. Creating breakthrough architectures like dLLMs is only half the battle. Bringing them to market requires an equally innovative infrastructure partner. Baseten has built the gold standard for inference. Partnering with them to serve and optimize the model on NVIDIA hardware means our customers get the raw, parallel speed of Mercury 2 paired with the robust isolation, global scale, and compliance that enterprise production demands."*


Mercury 2 is Inception's flagship model and can generate over 1,000 tok/sec, speeds previously only possible with specialized AI inference chips.

At its core, Baseten's job is to make it easy for customers to run inference efficiently at scale, regardless of the architecture they use.

When we started to work with Inception, we quickly realized that there was a good fit. Mercury 2 is a model that enterprise teams are actively routing production traffic to for its speed, quality and cost effectiveness. Inception needed an inference partner that could handle enterprise-scale reliability, compliance requirements, observability, and customer isolation, and Baseten was a good match for that.

*"What excites me most about Inception is that they aren't just innovating on paper, they’ve built a high-performance architecture that enterprise teams are successfully routing production traffic to today. Diffusion LLMs present unique infrastructure challenges, and by combining Inception's breakthrough models with Baseten's enterprise-scale reliability, compliance, and isolation, we're making it seamless for developers to deploy these incredibly fast models into production."* 


Baseten is the infrastructure layer powering Inception’s Mercury API. Rather than building and operating their own inference platform, Inception routes customer traffic through Baseten, giving them enterprise-grade reliability and a growing set of platform capabilities without the operational burden.

The deployment runs across NVIDIA GPUs including Hopper H100, Blackwell, etc. Because Mercury 2 delivers its speed at the model level, it doesn't depend on scarce specialized hardware; it runs on the widely available NVIDIA hardware enterprises already use, and it gets faster as those GPUs do. Baseten provisions always-on capacity with burst scaling support, which enables Inception to absorb traffic spikes without over-provisioning for steady-state load.

Key platform capabilities Inception relies on include:

- [Baseten Frontier Gateway](https://www.baseten.co/products/frontier-gateway/) for rate limiting per customer, request prioritization, and API routing
- Metrics and observability
- Autoscaling with configurable cron-based burst windows for peak traffic periods

Blackwell GPU cluster provisioned for voice and ultra-latency-sensitive workloads, targeting 150ms-250ms p50 end-to-end latencies

Augment Code is an AI-powered platform for enterprise software development, and they are one of the first teams running Mercury 2 in production on Baseten. Their use case is a good illustration of where diffusion LLMs shine.

Augment's coding agents accumulate large context windows over the course of a session. When that context gets too large, the system needs to compress it so it summarizes the decisions made, files touched, issues unresolved, and next steps. This is called context compaction, and it's a hard problem to solve as it requires long-context understanding, fidelity, structured output generation, and low latency at the same time.

The standard approach to address this challenge would be to use a frontier model for compaction, but it’s expensive and slow. That’s why Augment Code looked for alternatives and decided to try routing compaction to Mercury 2 as a dedicated subagent.

*"Building the best AI coding agent means using the right models for the right jobs. With Inception's Mercury 2 running on Baseten, we are able to take an unconventional approach to context compaction that cut our costs by 90% and reduced latency by 82%. Mercury 2 gives us the speed and quality we needed. Baseten provides the inference platform to deploy it across our customers."* 


The results worth highlighting include:

- An 82% reduction in compaction latency, which is a direct outcome of the difference between a coding agent that interrupts your flow and one that doesn't. Even more notable was that the compaction step dropped from \~150 seconds to \~27 seconds and became fast enough to be invisible.
- A 90% reduction in cost, which was the result of decoupling compaction from their primary frontier model. By switching to Mercury 2 on Baseten, Augment Code stopped paying premium prices for a task that didn't require premium intelligence, as Mercury 2 provides enough reasoning quality at a fraction of the cost.
- When it comes to MCP server tool search, Mercury 2 returns summaries in under a second, which is the difference between seamless and sluggish when your agent is deciding which tool to call next.

The important takeaway from what Augment Code has been able to accomplish with Mercury 2 is that not every call in your pipeline deserves your most expensive model.

As modern AI applications are increasingly becoming multi-model systems, the part that reasons over your user's intent might need Claude, but the parts that route, compress, search, and summarize need to be fast, cost-efficient, and intelligent enough. That's what Inception Labs unlocks, and Mercury 2 is purpose-built for that layer. Inception is helping you optimize your AI applications and agentic workflows so latency can feel instant while cost is manageable at scale.

[Mercury 2 is available now](https://www.baseten.co/talk-to-us/inception-mercury-2/) on Baseten. If you're building a multi-agent system, coding tool, voice application, or anything where you're currently routing all traffic to a single expensive model, Mercury is worth testing. We are currently running free POCs so if you are interested, you can submit an application [here](https://www.baseten.co/talk-to-us/inception-mercury-2/).
