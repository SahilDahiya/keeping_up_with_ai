---
title: Fireworks AI
kind: blog
topic: models
subtopic: reinforcement-learning
secondary_topics:
- inference/optimization
summary: Cursor's Composer 2, built on Kimi 2.5, is trained via continual pretraining
  and large-scale RL on long-horizon software engineering tasks; Fireworks provides
  distributed rollout/inference infra across 3-4 clusters with compressed weight sync,
  hitting 61.3 CursorBench and 6-10x lower inference cost than comparable frontier
  coding models.
triage: null
skip_reason: null
source: fireworks
url: https://fireworks.ai/blog/Cursor-Composer-2
author: null
published: '2026-06-26'
fetched: '2026-08-12T06:30:53Z'
classifier: claude
taxonomy_rev: 2
words: 1040
content_sha256: 03dd8d137182c235578cf6bcb9600fba5e053ce597c3c10efc66b435a96a8dab
---

# Fireworks AI

Cursor set out to build a coding model optimized for one environment: software engineering inside Cursor. Rather than relying solely on general-purpose foundation models, the team combined continual pre-training, large-scale reinforcement learning, and production feedback loops to create a specialized model that improves through real developer workflows.

Composer 2 builds on Kimi 2.5 and is trained on long-horizon software engineering tasks including tool use, debugging, terminal execution, and multi-file code edits. The result is frontier-level coding performance while remaining significantly more cost-efficient and reliable than larger general-purpose models ([Composer 2 Technical Report](https://cursor.com/resources/Composer2.pdf?)).

As these training loops scaled, reinforcement learning stopped being just a modeling technique and became an infrastructure problem. Each rollout is effectively a full development session, requiring fast inference, consistent execution environments, and frequent synchronization of large model states across distributed clusters. Training stability, environment fidelity, and rollout throughput all became first-order system constraints ([Frontier RL Blog](https://fireworks.ai/blog/frontier-rl-is-cheaper-than-you-think?utm_content=429440746&utm_medium=social&utm_source=linkedin&hss_channel=lcp-91174981)).

Fireworks provides the inference layer that makes these RL loops practical. It powers distributed rollout and inference infrastructure across multiple clusters, enabling Cursor to run large-scale reinforcement learning without building and operating a dedicated inference stack internally. This lets the team focus on improving model behavior rather than scaling low-level systems. This builds on an earlier collaboration focused on high-performance inference for coding workloads ([Fireworks x Cursor](https://fireworks.ai/blog/cursor)).

- •**Frontier coding performance**
  - •**CursorBench: 61.3**
  - •**Terminal-Bench: 61.7**
  - •**SWE-bench Multilingual: 73.7**
- •
- •**6–10x lower inference cost** vs comparable frontier coding models
- •**Distributed reinforcement learning across 3–4 global clusters**
- •Compressed weight synchronization instead of full model transfers
- •Production inference reused during training to accelerate RL runs

"We have finite engineers like everybody else. We would prefer to have engineers make training more efficient and more precise rather than spin up an inference effort." 

- Federico Cassano, Research Lead, Cursor

Cursor’s optimization target is a single environment: software engineering inside Cursor.

That constraint changes the learning problem. Instead of spreading capacity across broad general-purpose capability, Composer 2 focuses on the workflows developers actually run: editing repositories, debugging failures, executing terminal commands, and completing multi-step tool interactions.

The base model (Kimi 2.5) provides general coding ability, but most gains come from post-training. Cursor combines continual mid-training on code with reinforcement learning over full software engineering sessions.

Each training run is a full development trajectory: long-horizon debugging, tool calls, environment feedback, and iterative code changes.

This is where the distinction becomes operational: Mid-training teaches the model to write code. Reinforcement learning teaches it to write correct code inside a real system.

As Federico Cassano puts it,

"Mid-training teaches the model to write code. Reinforcement learning teaches it to write correct code."

This shift is what turns a strong coding model into a reliable coding agent, and it introduces a new set of constraints around environment fidelity, rollout scale, and distributed infrastructure design.

As RL expanded, it became clear that model quality and infrastructure quality were tightly coupled.

Each rollout behaves like a full engineering session, with tool execution, terminal commands, file edits, and evaluation before any weight update occurs. That means RL performance depends not just on the model, but on how faithfully the environment mirrors production.

Small mismatches matter. Models can exploit gaps between training and production behavior, optimizing for reward signals rather than real correctness.

In practice, this turns RL into an environment fidelity problem as much as a learning problem.

The Cursor team observed this directly: when environments are imperfect, models learn shortcuts that break in production. RL does not just optimize behavior, it amplifies whatever signal the system provides.

This is why infrastructure becomes inseparable from model performance.

Fireworks provides the inference and rollout layer that allows Cursor to scale RL without building a dedicated inference system.

Instead of centralizing training in a single massive cluster, **Cursor runs RL across 3–4 distributed global clusters unified through Fireworks infrastructure**.

Key capabilities include:

- •Cross-region model updates with ~98%+ optimization in transfer size
- •Minutes-level synchronization staleness across clusters
- •Stable rollout fleets for large-scale MoE models
- •Low-latency inference during training and evaluation loops
- •Production inference reused as part of RL sampling and rollout execution

Model synchronization is handled through compressed weight updates rather than full parameter transfers, reducing overhead while maintaining consistency across regions.

This makes it possible to treat inference capacity as a shared resource between production and training, accelerating RL cycles without separate infrastructure investment.

Composer is not just trained with reinforcement learning. RL is used as a mechanism for shaping real product behavior.

This produces measurable improvements in:

- •Multi-step reasoning over long coding sessions
- •Terminal and tool execution success rates
- •Best-of-K and average performance across tasks
- •Stability across extended agent workflows

Rather than treating RL as a research loop, Cursor operationalized it as part of the system that defines product quality.

Composer delivers frontier-level coding performance with materially lower cost and higher operational efficiency.

| Benchmark | Score | 
|---|---|
| CursorBench | 61.3 | 
| Terminal-Bench | 61.7 | 
| SWE-bench Multilingual | 73.7 | 

- •**6–10x lower inference cost** vs comparable frontier models
- •Faster iteration cycles in training and deployment
- •Reduced dependency on centralized hyperscaler training clusters
- •Improved reliability in long-horizon agent workflows
- •Production systems directly contribute to training throughput

Early internal and community evaluations show Composer competing with or exceeding leading proprietary coding models in terminal-style and agentic tasks.

Composer reflects a broader shift in how AI systems are built:

**Inference → Intelligence**

Models improve through interaction, not just scaling.

**Static → Continuous systems** 

Behavior is shaped by real-world feedback loops.

**General models → Environment-specific models**

Performance comes from tight coupling to a single domain.

**Centralized training → Distributed RL systems**

Learning happens across globally distributed infrastructure.

This validates a deeper shift: the next advantage in AI is not just model choice, but ownership of the post-training loop.

Cursor demonstrates that frontier coding performance is increasingly a function of reinforcement learning systems, not just model scale.

Fireworks enables this shift by making large-scale RL and inference infrastructure practical, distributed, and cost-efficient.

The result is a new category of system: models that continuously improve inside the environments where they are used.

Owning that loop is becoming the defining advantage in AI systems.
