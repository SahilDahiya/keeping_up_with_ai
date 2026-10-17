---
title: 'Beam: Efficient reasoning for coding and agentic workloads'
kind: blog
topic: null
subtopic: null
secondary_topics: []
summary: null
triage: null
skip_reason: null
source: baseten
url: https://www.baseten.co/blog/reflection-beam-launch/
author: Chloe Florit
published: '2026-10-16'
fetched: '2026-10-17T06:08:35Z'
classifier: null
taxonomy_rev: 2
words: 336
content_sha256: 093061839371bf417cc05609eaaa23d9aa4015d7fc17b6d667b5e8c4b3ee9437
---

# Beam: Efficient reasoning for coding and agentic workloads

### Published

![Beam](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1792157570-model-release.png%3Fauto%3Dformat%26fit%3Dcrop%26h%3D630%26w%3D1200&w=3840&q=100)

Today, we’re proud to support Reflection by bringing Beam, its first open-weight model, to the Baseten Platform with day-0 support.

Beam is [available now](https://www.baseten.co/library/beam/) through Baseten Model APIs and Dedicated Inference. Here’s a closer look at its capabilities and approach to efficient reasoning.

Beam is an autoregressive transformer model that accepts text inputs and generates text outputs (mainly in English). It has a mixture-of-experts (MoE) architecture with 501B total parameters, 23B active parameters per token, and a context window of up to 1 million tokens.

Beam is the first in a new family of models from Reflection, with multilingual and multimodal capabilities planned for future releases. Beam is designed for developers and researchers building coding and agentic systems, as well as enterprises that want to customize and run their own models. It works out of the box with the runtimes, frameworks, coding harnesses, and tools developers already use.

## **Efficient reasoning for coding and agentic workloads**

Reflection’s evaluations show strong performance across coding, agentic, reasoning, and STEM benchmarks:

![Agentic coding performance](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1792120072-agentic-coding-performance.png%3Fauto%3Dformat%26w%3D1200&w=3840&q=75) Agentic coding performance

![Reasoning performance](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1792158058-reasoning.png%3Fauto%3Dformat%26w%3D1200&w=3840&q=75) Reasoning performance

*Source: https://reflection.ai/blog/introducing-beam*

Reflection trained Beam to solve coding and agentic tasks and use fewer tokens to reach a successful result. The goal is to reduce the cost of these workloads. Reinforcement learning (RL) was a major part of Beam’s training.

Reflection used longer RL rollouts so Beam could practice solving tasks over multiple steps, using tools and adjusting its approach based on feedback. Reflection rewarded successful solutions during training and applied a length penalty to discourage unnecessary tokens. In short, longer rollouts let Beam work through complex tasks, while the length penalty encouraged it to do so with fewer tokens.

Users can also adjust Beam’s reasoning effort parameter: lower settings favor shorter responses, and higher settings allow more reasoning to improve performance on demanding tasks.

## Start using Beam on Baseten 

You can use Beam today through [Baseten Model APIs](https://www.baseten.co/api/draft-mode/?url=/library/beam/&token=qea4cap5quz.MQJ1ebc) and [Dedicated Inference](https://www.baseten.co/api/draft-mode/?url=/library/beam/&token=qea4cap5quz.MQJ1ebc). Build coding and agentic systems that solve complex tasks without wasting tokens.
