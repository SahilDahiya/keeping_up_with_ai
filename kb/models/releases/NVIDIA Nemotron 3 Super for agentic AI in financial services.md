---
title: NVIDIA Nemotron 3 Super for agentic AI in financial services
kind: blog
topic: models
subtopic: releases
secondary_topics: []
summary: Covers NVIDIA Nemotron 3 Super, a 120B hybrid Mamba-Transformer MoE model
  with 12B active parameters, multi-token prediction, and leading scores on AIME 2025,
  SWE-Bench Verified/Multilingual, terminal-bench, and RULER, aimed at multi-agent
  financial-services workloads.
triage: null
skip_reason: null
source: baseten
url: https://www.baseten.co/blog/introducing-nemotron-3-super
author: Rachel Rapp
published: '2026-03-11'
fetched: '2026-11-12T06:11:06Z'
classifier: claude
taxonomy_rev: 2
words: 1095
content_sha256: caad4fcfe1d7d4abc8b79fdff30067d4602ea8deb6b8a78cb6238772951d229e
---

# NVIDIA Nemotron 3 Super for agentic AI in financial services

AI models
# NVIDIA Nemotron 3 Super for agentic AI in financial services

Day-zero support for NVIDIA Nemotron 3 Super, a 120B hybrid MoE model with 12B active params, 1M token context, and over 50% faster token generation.


- Authors
- Date
- March 11, 2026

TLDR

NVIDIA Nemotron 3 Super is a 120B hybrid mixture-of-experts model with 12B active parameters per forward pass. It delivers over 50% faster token generation than comparable models in the landscape and leads benchmarks across AIME 2025, SWE-Bench Verified, terminal-bench, and RULER. Nemotron 3 Super balances accuracy and efficiency for multi-agent workloads and is completely open-source, making it particularly useful for sensitive, complex financial service applications. We’re excited to be a launch partner with day-0 support for NVIDIA Nemotron 3 Super, powered by the Baseten Inference Stack. You can try it here.

As GenAI applications move towards multi-agent systems—retrievers, planners, tool executors, and verifiers working in concert—their infrastructure demands change. Communication overhead, context drift, and inference calls scale with agent count.

Open models give you more control over these demands: customize behavior for domain-specific tasks, tune your agentic system for orchestration efficiency, and deploy on single-tenant or self-hosted infrastructure to meet compliance requirements. For applications like financial services running sensitive workloads, these are often hard requirements.

That’s what Nemotron 3 Super is built for: open weights, open training data, and open recipes for full control.

Open models need to be high-quality — and fast — to be useful. In terms of quality, Nemotron 3 Super achieves leading results across relevant benchmarks for agentic reasoning tasks, including:

- [**AIME 2025:**](https://artificialanalysis.ai/evaluations/aime-2025) leading math reasoning accuracy
- **terminal-bench:** agentic coding and command execution
- **SWE-Bench Verified and Multilingual:** software engineering task completion
- [**RULER**](https://github.com/NVIDIA/RULER): long-context retrieval and reasoning across extended inputs

At the same time, Nemotron 3 Super generates tokens over 50% faster than comparable models, driven by its hybrid Mamba-Transformer architecture and multi-token prediction (more on both below). For multi-agent systems running dozens of concurrent agents, this difference can compound in terms of speed (user experience) and compute costs.

Nemotron 3 Super uses a hybrid Mamba-Transformer architecture combined with Mixture-of-experts routing. A few design choices are worth understanding in detail.

In a standard mixture-of-experts (MoE) model, each token is routed to a small subset of experts (i.e., specialized subnetworks) that process it and return a result. The tradeoff is that routing tokens between experts in full-dimensional token space is expensive: you're moving large vectors around, which adds memory and communication overhead.

Nemotron 3 Super’s latent MoE architecture adds a step to decrease this overhead. Before routing, each token is projected to a smaller latent representation for expert routing and computation, then back to the full token space. Because the routing and computation happen in a lower dimension, you can afford to consult more experts per token without paying the usual cost. That’s how Nemotron 3 Super consults 4 experts at the cost of 1.

Multi-token prediction (MTP) predicts several tokens simultaneously in a single forward pass. Ablation studies from [NVIDIA's Nemotron paper](https://arxiv.org/abs/2512.20856) show \~97% acceptance on the first two predicted tokens, meaning the speculation almost always holds. This accelerates long-form generation significantly — particularly relevant for financial workflows generating structured outputs like loan summaries, risk assessments, or audit reports.

NVFP4 training uses NVIDIA's 4-bit floating point format, trained on Blackwell architecture. Peak FP4 throughput on GB300 is 3x higher than FP8. Sensitive layers (like Mamba output projections and MTP projections) are kept at higher precision (BF16 or MXFP8) to prevent information loss.

This gives you the speed of 4-bit quantization without meaningful accuracy degradation.

1M token context length lets agents retain full conversation histories, maintain plan state across multi-step workflows, and feed entire document sets into a single RAG pipeline call. Cross-document reasoning (like comparing loan applications, regulatory filings, or transaction records across long time horizons) becomes tractable.

Standard transformer attention scales KV cache linearly with sequence length — at 1M tokens, that becomes a memory problem. Mamba layers avoid this entirely by compressing sequence state into a fixed-size representation, keeping memory overhead constant regardless of context length.

Nemotron 3 Super is one of three Nemotron 3 models, each a different size and targeting a different point on the accuracy-efficiency curve.

**Parameters: 30B total, 3B active**

[Nano](https://www.baseten.co/blog/nvidia-nemotron-3-nano/) is the most compute-efficient model in the family. With 3B active parameters, it delivers 4x the throughput of Nemotron 2 Nano and is optimized for high-volume, targeted tasks: summarization, retrieval, classification, and routing.

In a multi-agent pipeline, Nano works well as the high-frequency worker — handling intermediate steps without becoming a bottleneck. Use Nano when you need to run many agents at scale, and the task doesn't require deep reasoning.

**Parameters: 120B total, 12B active**

Super is the right choice for agents that need to combine multiple inputs, reason across steps, and call tools reliably. It's explicitly optimized to run many collaborating agents simultaneously.

Use Super as the coordination and reasoning layer in multi-agent pipelines; the model that routes, plans, and synthesizes before delegating routine work to Nano. For most financial services agentic applications — fraud detection, loan underwriting, compliance triage — Super is the right starting point.

**Parameters: Not yet known** 

Ultra will be the high-end reasoning engine for tasks that require deep analysis, long-horizon planning, or strategic decision-making.

Designed to handle only the most demanding tasks in a pipeline and delegate routine work to Super or Nano, Nemotron 3 Ultra’s release is expected in early 2026 (soon after NVIDIA’s [flagship paper](https://arxiv.org/abs/2512.20856) on Nemotron 3). Plan to use Ultra when maximum reasoning depth matters more than throughput.

Nemotron 3 Super is useful for:

- **Loan processing:** Feed mortgage applications, pay stubs, tax documents, and bank statements into a single 1M token context window.
- **Fraud detection:** Long context means the model can reason over full transaction histories, paired with strong pattern recognition from multi-environment RL training that can help detect anomalies.
- **Cybersecurity and compliance:** Strong tool-calling and instruction-following capabilities make Super well-suited to security operations workflows, like triaging vulnerability reports or correlating threat signals across data sources.
- **Multi-agent orchestration:** Nemotron 3 Super is explicitly designed to coordinate many collaborating agents simultaneously. For financial services pipelines where a routing agent hands off to specialized sub-agents, it can effectively act as the intelligence layer in the middle.

We’re thrilled to be day-0 launch partners for Nemotron 3 Super, which can be used immediately as a [Model API on Baseten](https://www.baseten.co/library/nvidia-nemotron-super/). We also offer single-tenant and self-hosted deployments for financial service orgs and enterprises with strict compliance requirements; [reach out](https://www.baseten.co/talk-to-us/) to talk to our engineers.
