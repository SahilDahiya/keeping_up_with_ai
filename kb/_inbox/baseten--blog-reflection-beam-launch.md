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
url: https://www.baseten.co/blog/reflection-beam-launch
author: Chloe Florit
published: '2026-10-16'
fetched: '2026-11-12T06:08:58Z'
classifier: null
taxonomy_rev: 2
words: 431
content_sha256: 692b1dc630dedbf4663a8d60487e88264e8461950da5d6faa0243880331b2ad6
---

# Beam: Efficient reasoning for coding and agentic workloads

AI models
# Beam: Efficient reasoning for coding and agentic workloads

Beam is now available on Baseten. Reflection’s 501B open-weight MoE model is built for efficient reasoning in coding and agentic workflows, with 1M context.


- Authors
- Date
- October 16, 2026

TLDR

Today, we’re proud to support Reflection by bringing Beam, its first open-weight model, to the Baseten Platform with day-0 support. Beam is available now through Baseten Model APIs and Dedicated Inference. Here’s a closer look at its capabilities and approach to efficient reasoning.

Beam is an autoregressive transformer model that accepts text inputs and generates text outputs (mainly in English). It has a mixture-of-experts (MoE) architecture with 501B total parameters, 23B active parameters per token, and a context window of up to 1 million tokens.

Beam is the first in a new family of models from Reflection, with multilingual and multimodal capabilities planned for future releases. Beam is designed for developers and researchers building coding and agentic systems, as well as enterprises that want to customize and run their own models. It works out of the box with the runtimes, frameworks, coding harnesses, and tools developers already use.

Reflection’s evaluations show strong performance across coding, agentic, reasoning, and STEM benchmarks:

| Category | Benchmark | What it measures | Beam score | 
|---|---|---|---|
| Reasoning | GPQA Diamond | Graduate-level scientific reasoning | 90.5% | 
| Coding | SWE-bench Verified | Resolving real software issues | 80.9% | 
| Math | AIME 2026 | Competition mathematics | 97.8% | 
| Agentic | Terminal-Bench 2.1 | Completing tasks in a command-line environment | 80.1% | 
| Tool calling | MCP Atlas | Using real-world tools via MCP servers | 78.7% | 

Reflection trained Beam to solve coding and agentic tasks and use fewer tokens to reach a successful result. The goal is to reduce the cost of these workloads. Reinforcement learning (RL) was a major part of Beam’s training.

Reflection used longer RL rollouts so Beam could practice solving tasks over multiple steps, using tools and adjusting its approach based on feedback. Reflection rewarded successful solutions during training and applied a length penalty to discourage unnecessary tokens. In short, longer rollouts let Beam work through complex tasks, while the length penalty encouraged it to do so with fewer tokens.

Users can also adjust Beam’s reasoning effort parameter: lower settings favor shorter responses, and higher settings allow more reasoning to improve performance on demanding tasks.

You can use Beam today through [Baseten Model APIs](https://www.baseten.co/api/draft-mode/?url=/library/beam/&token=qea4cap5quz.MQJ1ebc) and [Dedicated Inference](https://www.baseten.co/api/draft-mode/?url=/library/beam/&token=qea4cap5quz.MQJ1ebc). Build coding and agentic systems that solve complex tasks without wasting tokens.
