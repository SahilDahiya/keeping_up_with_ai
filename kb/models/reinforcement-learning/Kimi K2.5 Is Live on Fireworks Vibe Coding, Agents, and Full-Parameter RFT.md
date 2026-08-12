---
title: 'Kimi K2.5 Is Live on Fireworks: Vibe Coding, Agents, and Full-Parameter RFT'
kind: blog
topic: models
subtopic: reinforcement-learning
secondary_topics:
- inference/serving
summary: Fireworks' full-parameter RL tuning preview for Kimi K2.5 exposes Tinker-API-compatible
  low-level primitives (forward, forward_backward, optimizer_step) while handling
  distributed training, cross-region trainer/sampler deployment with seamless weight
  transfer, and customizable GRPO/reward-shaping loss.
triage: null
skip_reason: null
source: fireworks
url: https://fireworks.ai/blog/kimi-k2p5
author: null
published: '2026-01-26'
fetched: '2026-08-12T06:29:55Z'
classifier: claude
taxonomy_rev: 2
words: 560
content_sha256: e1975094faa5e9c463e63c1cc716acacbeb683a8bef2ddfa4c0365e3f054f2ef
---

# Kimi K2.5 Is Live on Fireworks: Vibe Coding, Agents, and Full-Parameter RFT

[Kimi K2.5](https://fireworks.ai/models/fireworks/kimi-k2p5) is Moonshot AI’s flagship agentic model and a new SOTA open model. It unifies vision and text, thinking and non-thinking modes, and multi-agent execution into one model.

We are launching Day-0 support for Kimi K2.5. Fireworks offers the fastest endpoint for all Kimi K2 series models as well as fine tuning for Kimi K2 models. Additionally, we now offer a **full parameter RL tuning** **private preview** for Kimi K2.5, enabling application builders to fine tune the SOTA OSS VLM model for use cases like vibe coding and agentic workflows. Sign up for the full parameter RL tuning waitlist [here](https://fireworks.ai/full-param-rft).

Kimi K2.5 demonstrates that open source models are now surpassing their closed-source counterparts. The chart provides more details on the multiple benchmarks where Kimi K2.5 achieves SOTA results, including for Agents (HLE Full, BrowseComp, and Deepsearch) and for Vision (OmniDoc Bench 1.5).

Below is an in-depth look at its core application areas, highlighting the advanced nature across multiple multimodal agent use cases.

Kimi K2.5 is a multimodal model supporting image and video understanding. For text-only processing, developers can use the Kimi K2 model series including [Kimi K2 Thinking](https://fireworks.ai/models/fireworks/kimi-k2-thinking) and [Kimi K2 0905](https://fireworks.ai/models/fireworks/kimi-k2-instruct-0905).

Fireworks now supports full parameter RL tuning for Kimi K2.5 in private preview, allowing product developers to customize the model to their specific product use cases and exceed the quality of closed models. For companies already tuning models with LoRA, full parameter fine tuning offers an additional lever to get the best model quality. Signup for the waitlist [here](https://fireworks.ai/full-param-rft).

We are launching full parameter RL fine-tuning for Kimi K2.5 with Tinker API compatibility. Researchers get low-level compute primitives—`forward, forward_backward, optimizer_step, save_weight`—while we handle the distributed training infrastructure.

- •**Tinker API Compatible** : Same interface researchers already use for LoRA and SFT, now extended to full parameter training. Existing Tinker integrations can switch to full parameter mode with minimal code changes.
- •**Cross-Region RL Training** : Support trainer and sampler deployments in different regions. Fireworks RL model format enables seamless weight transfer between regions without customers managing cross-region data pipelines. This is critical for global teams where training data, model providers, and inference endpoints span multiple cloud regions.
- •**Customizable Loss** : Customers can implement their own GRPO/reward shaping logic on their side. This keeps our API surface minimal and lets world-class researchers maintain full control over their RL algorithms.

Global teams can train in one region and hot-load checkpoints into inference deployments elsewhere without managing cross-region weight transfers manually, allowing them to scale up their training to saturate the whole data center. The Fireworks RL trainer + model format handles all the serialization, compression, and ledger bookkeeping.

Fireworks offers the fastest endpoint for all Kimi K2.5 and Kimi K2 series models. Fireworks achieves up to 200 Tokens/s on Kimi K2.5. Data from Artificial Analysis’ independent benchmarks shows that Fireworks consistently provides best-in-class performance for Moonshot’s Kimi Models, including Kimi K2 Thinking and Kimi K2 0905. Outperforming the next closest GPU inference provider by up to 75%. Faster speed is essential for real-time user experience, application productivity, and operational efficiency.Stay tuned as our engineering team continues to optimize the performance. Stay tuned as our engineering team continues to optimize the performance.

12345678910111213141516171819202122232425262728293031323334353637

Fireworks enables users to control the reasoning behavior of the Kimi K2.5 model and inspect its reasoning history for greater transparency. [Click here](https://docs.fireworks.ai/guides/reasoning) for more details.
