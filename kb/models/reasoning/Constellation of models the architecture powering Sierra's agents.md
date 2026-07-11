---
title: 'Constellation of models: the architecture powering Sierra''s agents'
topic: models
subtopic: reasoning
secondary_topics:
- agents/planning
- inference/serving
summary: Describes a constellation-of-models architecture for powering agents, combining
  multiple models and routing behavior around task needs.
source: sierra
url: https://sierra.ai/blog/constellation-of-models
author: Thiaga Rajan
published: '2026-05-12'
fetched: '2026-07-11T03:51:46Z'
classifier: codex
taxonomy_rev: 1
words: 790
content_sha256: 8c039b9b3a17fc01e66a044fd879774b432e71b44c6c5ffad2e3500ea8f5f4ab
---

# Constellation of models: the architecture powering Sierra's agents

# Constellation of models: the architecture powering Sierra's agents

“Which large language model does Sierra use?” is one of the most common questions we’re asked by businesses looking to improve their customer experience with AI. But like LEGO sets, you can’t build a great agent using a single type of building block. That’s why agents built on Sierra are assembled using 15+ frontier, open-weight, and proprietary models, depending on the job to be done.

In this constellation-of-models approach, every piece is selected for what it does best, and then orchestrated so that the whole becomes greater than the sum of the parts. The result: multifaceted agents that are fast, effective, and on‑brand no matter what they’re doing — without you having to hand-pick the models, or micromanage their wiring.

## Selecting the right model for the job

AI agents are sophisticated software that can reason and take action — everything from recommending a specific product or service, authenticating a caller, processing a return, troubleshooting a technical issue, or saving a subscriber who intends to cancel.

Different tasks place very different demands on an agent. For example, some require:

- **Low-latency tool calling and decision-making**— for simpler tasks like order management, inventory status, or product lookups, the instructions tend to be more straightforward, and the models we pick satisfy tighter latency constraints for natural-sounding voice conversations.
- **High-precision classification**— certain tasks require a nuanced and highly consistent classification of behavior, for example when identifying suspicious user behavior.
- **Long-context reasoning**— where the agent needs to read, process, and remember large amounts of information — complex policies, dense technical information — and follow instructions carefully, without missing or inventing details.
- **Pitch-perfect tone**— so the agent sounds warm, conversational, and on-brand, especially in tricky or sensitive moments.

No single model meets the unique constraints of every task. Models that shine at reasoning often degrade significantly when forced to produce a quicker response. Similarly, models that are great at generating human-like responses can struggle when overloaded with longer context. Utilizing one model for everything forces unnatural trade-offs — speed vs. accuracy vs. tone — that ultimately lead to lower-quality agents.

Sierra solves these challenges by breaking agent behavior down into tasks and picking the best model for each specific job to be done. That means running task-specific evaluations, spotting gaps where current models fall short, and investing in fine-tuned models where off-the-shelf models fail to meet our constraints.

## Designed for a moving frontier

Sierra’s Agent OS is built around modular task abstractions that isolate responsibilities, with the orchestration and routing handled automatically under the hood by the platform. So instead of writing monolithic agents, you compose them from cleanly separated capabilities — retrieval, classification, tools, policies, and tone. Certain tasks get more “agency”, greater room to reason, reflect, and use tools. This level of agency is enabled by employing supervisors to enforce guardrails, policies, and quality checks.

A key benefit of this organization is that agents built on Sierra automatically improve as frontier models improve. Our higher-agency tasks benefit greatly from improved reasoning, tool-calling, and instruction-following. Most agents improve over time with little more than a prompt tweak. As models advance, some tasks naturally become redundant, and new ones emerge to take their place.

Prompting differs across model families, and Sierra’s modular architecture makes it easy to update high-value, low-risk tasks without forcing changes to sensitive guardrails. This lets you adopt new models faster and more safely — so you get the benefits of progress without the usual risk.

## Reliability and uptime

Sierra provides built-in redundancy across model providers for mission-critical tasks. We continuously monitor model health and performance — tracking latency, error rates, and timeouts. When a provider starts to degrade, our automated routing seamlessly fails over to healthier, equivalent models so your agents keep running smoothly.

The result is an inference layer that stays resilient even if a single model or provider goes down, delivering the right balance of speed, accuracy, and quality for the most demanding agents.

## You define the agent, Sierra makes it real

With Sierra, you define how your agent should behave — its policies, tools, guardrails, knowledge, and brand and tone. We translate that into a production-ready agent built from composable tasks, backed by supervisors, and powered by a constellation of models continually optimized for your use case. The result is a reliable, best-in-class agent — and the confidence that as models evolve, your agents get better too.

That’s the promise of Sierra’s approach: a system modular enough to adopt breakthroughs quickly, disciplined enough to protect quality, and pragmatic enough to meet real-world reliability demands. You define what great looks like — and we make sure the right pieces snap together to deliver it.
