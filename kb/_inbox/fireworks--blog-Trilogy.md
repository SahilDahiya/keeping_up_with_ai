---
title: Trilogy Validates Open-Weight AI Models for Enterprise Workloads with Fireworks
kind: blog
topic: null
subtopic: null
secondary_topics: []
summary: null
triage: null
skip_reason: null
source: fireworks
url: https://fireworks.ai/blog/Trilogy
author: null
published: '2026-06-01'
fetched: '2026-08-12T06:29:35Z'
classifier: null
taxonomy_rev: 2
words: 1159
content_sha256: 7879a18f90bc2ea8b4535db8559935f6356093d2205fb23636e0c4039f07a6fb
---

# Trilogy Validates Open-Weight AI Models for Enterprise Workloads with Fireworks

[Trilogy’s AI Center of Excellence](https://ai-coe.trilogy.com/) (AI COE), overseeing hundreds of portfolio companies, faced escalating AI infrastructure costs and operational constraints as large-scale AI adoption expanded across engineering teams.

As usage scaled, rate limits, usage caps, and infrastructure variability increasingly shaped how AI could be deployed in production workflows, creating friction for both experimentation and operational use.

To address this, Trilogy evaluated open-weight models and began adopting Fireworks as a primary inference infrastructure layer for evaluation and early production workloads. This enabled a shift from fragmented model experimentation to standardized evaluation and production-grade testing of open-weight models across enterprise workloads.

The result was a transition from cost-constrained AI adoption to scalable, predictable multi-agent execution systems operating at billion-token scale within internal workloads.

- •Standardized open-weight model usage across AI Center of Excellence workflows
- •Enabled billion-token scale workloads within internal systems
- •Enabled **billion-token class agentic workflows** via systems like OpenSymphony
- •Enabled open-weight model inference at **~1/5 the cost of proprietary systems** for comparable workloads
- •Reduced impact of hourly, weekly, and monthly rate limits on workloads
- •Shifted from experimentation to production-scale inference evaluation for enterprise AI

Trilogy’s AI COE supports hundreds of portfolio companies, each with distinct workflows, tooling requirements, and levels of AI maturity.

As AI adoption expanded, the team needed to consolidate experimentation, reduce duplicated effort, and standardize access to high-performance inference infrastructure.

This created demand for a consistent inference layer that could support a wide range of workloads across teams.

As usage scaled, two structural constraints emerged that shaped how AI could be used across systems:

First, proprietary model usage introduced linear cost scaling, limiting how far AI could expand as it became embedded across more workflows and portfolio companies.

Second, operational constraints such as rate limits, usage caps, and variability in availability began impacting developer experience across both experimental and production workloads.

As VP of Trilogy AI Center of Excellence Leonardo Gonzalez noted, “We’ve been very heavy users of Anthropic and OpenAI, like extremely large accounts. Cost was quite prohibitive as adoption increased across the portfolio companies… teams were running into budget constraints.”

At the same time, open-weight models began reaching performance parity with proprietary systems at significantly lower cost: “Open models in the last few months have now reached parity with proprietary models at an order of magnitude less pricing.”

Together, these shifts created a clear inflection point where the existing stack no longer scaled with demand.

Trilogy evaluated multiple inference providers as part of its open-weight infrastructure strategy, including Cerebras and OpenRouter, to support early experimentation and production-adjacent workloads.

Cerebras provided high-performance inference but introduced constraints around flexibility and integration at scale. OpenRouter enabled broad model access but lacked the consistency, reliability, and enterprise controls required for production use, particularly around privacy and operational stability.

Fireworks initially entered through integration into existing agent workflows, including Kimi-class models used within internal agent harnesses and custom routing layers. This allowed teams to directly evaluate emerging open-weight models without major infrastructure changes, while benchmarking performance, latency, and cost tradeoffs across providers.

Early usage centered on structured evaluation and testing, where teams ran models through internal benchmarking workflows inside these agent systems.

As Leonardo described, “I was plugging it into different agent harnesses and I even developed a shim to be able to specify using Fireworks as a provider…”

As experimentation expanded, system-level constraints became more visible, including rate limiting and throughput bottlenecks: “I was severely rate limited because of high demand… one of the mitigations suggested was to get a Fireworks API key.”

This friction point led to Fireworks becoming the primary inference provider for evaluation and pilot workloads, and broader internal usage over time.

Once adopted, Fireworks became the primary inference layer for internal evaluation and early production experimentation across the AI Center of Excellence.

Teams used Fireworks to run structured model evaluations across emerging open-weight models, iterate on agent workflows, and validate performance across latency, quality, and cost within a unified inference environment rather than fragmented provider setups.

This shifted model evaluation into a repeatable workflow where teams could move from testing to comparison and production evaluation without reconfiguring infrastructure. Model evaluation cycles that previously required separate setup and coordination were reduced to configuration-level changes, enabling faster iteration across teams.

Key capabilities included:

- •Deployment of open-weight models without infrastructure overhead
- •Rapid switching across evolving open-model variants
- •Stable inference under high token throughput workloads
- •Direct path from evaluation to production-grade testing

As Leonardo put it, “I could spin up a custom deployment, run evals, and immediately see whether a model was worth production consideration.”

This fundamentally changed the workflow from infrastructure-heavy integration work to a lightweight evaluation loop, significantly accelerating experimentation across teams.

Over time, Fireworks became the primary inference layer for internal deployment testing and early production workloads.

With Fireworks as the inference layer, Trilogy began running high-volume, multi-step agentic workflows across internal systems.

A key example is [**OpenSymphony**](https://opensymphony.dev/), an internal work orchestration system inspired by emerging patterns in agent-based software engineering.

OpenSymphony is a multi-agent system that decomposes engineering work into iterative planning, execution, and validation cycles. It enables:

- •Parallelized execution across multiple agents
- •Automated bug detection and reduction of technical debt
- •High-quality software outputs in significantly reduced timeframes

These workflows rely on sustained high-volume inference, which Fireworks supports through stable execution across distributed agent systems.

Open-weight models reached a level of capability that made them viable for production workloads, shifting the primary constraint from model quality to infrastructure execution at scale.

For enterprise use, the remaining requirements centered on consistent performance, control over data handling, and the ability to operate across diverse deployment environments.

Fireworks provided the inference layer to operationalize this shift, enabling teams to run open-weight models reliably in production-grade systems without re-architecting existing workflows.

With Fireworks powering inference across internal workloads, OpenSymphony workloads achieved a **93.6% prompt cache hit rate** and **more than 12K cached prompt tokens per second** under active production conditions, demonstrating how Fireworks' cache pricing and performance support token-intensive multi-agent workflows at scale.

These workloads also demonstrated sustained execution of long-context agent workflows, with observed performance reaching approximately **150 tokens per second** and **75K tokens per request** in active production environments.

Through this evaluation and early production usage, Trilogy has been able to:

- •Standardize inference across internal evaluation and production workflows
- •Enable billion-token-class agentic workloads through systems such as OpenSymphony
- •Reduce friction between model evaluation and deployment within internal workflows
- •Enable consistent, high-throughput execution across distributed teams
- •Transition from isolated experimentation to a shared inference layer across internal teams

AI systems evolved from isolated experiments into a shared inference layer supporting evaluation, testing, and production-scale agentic workloads.

Through Fireworks, Trilogy unified open-weight model usage across internal teams and supported portfolio workflows, enabling a shift from constrained experimentation to production-scale agentic systems operating at enterprise scale.

As Leonardo summarized, “Fireworks has enabled the exploration and adoption of open-weight models on an enterprise scale.”
