---
title: Innovative Solutions Rebuilds Enterprise Services Delivery with Fireworks
kind: blog
topic: null
subtopic: null
secondary_topics: []
summary: null
triage: null
skip_reason: null
source: fireworks
url: https://fireworks.ai/blog/innovative-solutions
author: null
published: '2026-05-05'
fetched: '2026-08-12T06:29:12Z'
classifier: null
taxonomy_rev: 2
words: 1282
content_sha256: 1447a0cd9f1621e93cf29b253919cd77ad9ab0419e421a46428c68a81bc1f2f9
---

# Innovative Solutions Rebuilds Enterprise Services Delivery with Fireworks

Innovative Solutions, a Tier 1 AWS Premier Partner delivering hundreds of AI-driven services engagements annually, hit a structural scaling constraint as inference costs and delivery complexity increased together.

AI inference became the dominant cost driver in the business, limiting margin expansion and operational flexibility at scale. To address this, the company moved its DarcyIQ platform to Fireworks as its primary inference layer. This reduced model integration overhead, stabilized multi-model execution, and made costs predictable.

This was not a tooling change. It was a redesign of services economics around AI systems. The result was a shift from linear delivery models to parallel, agent-driven execution across sales, scoping, and delivery.

- •Contract cycles reduced from 30–45 days to ~3 days
- •Delivery throughput doubled across engineering and PM teams
- •AI inference shifted from linear cost growth to predictable, controllable economics
- •Multi-agent execution scaled to 4–10B tokens per month, doubling month over month

Innovative Solutions is an AWS Premier Tier Partner helping enterprises and mid-market teams design and deploy AI systems at scale. As engagement volume increased, the team built DarcyIQ to streamline how proposals, technical documentation, and delivery artifacts were generated.

What began as an internal productivity tool evolved into a core execution layer for services delivery, later expanding into a commercial platform used by agencies, GSIs, and ISVs.

Today, DarcyIQ sits at the center of how the company delivers AI-enabled services.

CTO Travis Rehl has led the shift toward agentic delivery systems designed to increase throughput without proportional headcount growth.

As the business scaled, two issues emerged simultaneously.

Consultants and engineers managed multiple concurrent engagements, creating constant context switching across customers, tools, and models. Coordination overhead increased faster than capacity, limiting throughput even as demand grew.

As Travis put it, “Our number one COGS is AI cost. Our costs were keeping up with our acquisitions”.

Contracting and scoping cycles typically took 30–45 days from first meeting to signed agreement, slowing revenue realization and delaying delivery start. With the business doubling month over month, inference spend scaled directly with usage, eliminating operating leverage.

At scale, this meant growth no longer translated into margin expansion.

Three constraints defined the problem:

Every model change required engineering effort, validation, and deployment coordination, especially when working across rapidly evolving frontier models like GLM-5 and Kimi K2.5.

Inference costs increased directly with usage, preventing margin expansion at scale.

Significant engineering time was spent on scoping, documentation, and proposal generation instead of differentiated delivery.

As the company moved toward multi-agent workflows, inference density increased and cost predictability became critical.

At this point, scaling required architectural change, not optimization.

As Innovative Solutions evaluated inference providers including Baseten, the core requirement wasn’t just performance or cost. It was operational:

They needed a system that could handle constant model changes without slowing teams down in operation.

As they rotated between models like GLM-5 and Kimi K2.5, every change introduced validation work, engineering overhead, and deployment delays.

Fireworks removed that friction. As Travis described, “Fireworks won simply because it worked consistently. Whenever we deploy any model, it works the first time. No tuning, no fiddling. That mattered to us, because we change models all the time. What I don’t want is to get stuck in a 3-week development cycle trying to make a model work.”

In a system where models are constantly changing, consistency at deployment becomes a scaling constraint.

That moment clarified the decision. Stability and zero-friction deployment weren’t nice-to-haves. They were requirements for scaling a multi-agent system in production.

Within 1-2 weeks of initial deployment, **90% of Anthropic inference spend had been migrated to Fireworks**, making it the default inference layer for DarcyIQ.

Once Fireworks was in place, the scaling behavior changed.

Instead of costs rising directly with usage, inference became predictable even as workloads expanded:

- •**4–10B tokens per month**
- •Doubling month over month
- •Increasingly multi-agent workloads

This shifted DarcyIQ from a constrained system into a production-grade execution.

With Fireworks as the inference layer, DarcyIQ evolved from a productivity tool into a multi-agent execution system that operates across the full services lifecycle, from first customer interaction to delivery. These capabilities depended on high-performance, stable inference that could support real-time generation, rapid model iteration, and sustained multi-agent workloads at scale.

Customer conversations are converted directly into structured scopes, proposals, and contracts in real time.

Instead of manually assembling documents across tools, teams generate decision-ready outputs immediately after a call, compressing deal cycles from 30–45 days to ~3 days and increasing close rates.

As Travis noted: “As soon as you meet a customer, if you can get them paperwork right there, they’re more likely to sign than if you wait two weeks.”

Each engagement becomes structured data that feeds future execution. Approved scopes, edits, and outcomes are captured as signals, allowing the system to improve how work is defined, priced, and delivered over time. This replaces one-off scoping with a continuously learning system that standardizes quality while adapting to new requirements.

Contracts, proposals, and delivery artifacts are generated from structured inputs using reusable templates and embedded business logic.

This eliminates repetitive manual work across sales and delivery teams, reduces inconsistency, and ensures outputs align with brand, pricing, and operational standards.

Structured scopes become machine-readable context that can be executed directly by agent systems.

Instead of translating requirements into tasks across tools, multiple agents operate in parallel on delivery workflows, using shared context to coordinate execution. Where delivery was previously serialized across teams and tools, **6–10 agents now execute work in parallel per project**, increasing engineering capacity from 2–4 projects per engineer to ~10 and driving **2–3x throughput gains across delivery teams without quality loss.**

This removes coordination overhead and enables teams to scale output without proportional increases in headcount.

With Fireworks powering inference, the delivery model shifted in a few important ways:

- •Contract cycles dropped from **30–45 days to 3 days**
- •Engineers and PMs throughput doubled
- •Delivery output increased without proportional headcount growth
- •~90% of model spend migrated to Fireworks within ~1.5 weeks
- •Scaled to **4–10B tokens per month** , doubling month over month

Most importantly, delivery stopped behaving like a linear services process and started behaving like a parallel execution system.

Fireworks enabled production-scale agentic delivery by providing:

- •Stable inference across rapidly changing model environments
- •Zero-tuning deployment for production workloads
- •Predictable performance at high token volumes
- •A cost structure that supports multi-agent execution

Without this, multi-agent systems would not have been economically viable at production scale.

DarcyIQ now runs as a continuously running system with thousands executing concurrently across scoping, contracting, and delivery.

This shifts the core constraint from model capability to unit economics of persistent agent workloads.

Historically:

- •AI pricing was per interaction
- •Workloads were session-based
- •Costs scaled linearly with users

Today:

- •Agents run continuously
- •Workloads are system-level
- •Inference consumption is persistent and distributed

As Travis explained, “We’re spending a ton of time around the unit economics of multi-agent systems. Fireworks has given us the flexibility to update, improve, and evolve our pricing models for our customers as new agentic capabilities come to market.”

Under CTO Travis Rehl, Innovative Solutions has transformed DarcyIQ into a full agentic delivery system for enterprise services.

By partnering with Fireworks, the company removed the infrastructure and economic constraints that previously limited scale, unlocking a new operating model where:

- •Contract cycles compress from weeks to days
- •Delivery is powered by parallel agent systems
- •Scoping and execution continuously improve through learning loops
- •Unit economics are driven by inference efficiency, not human throughput

What began as a consulting workflow is now a continuously operating, AI-native execution engine built for the next era of enterprise services.
