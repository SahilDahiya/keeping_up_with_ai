---
title: Muse Spark Open, an open-weight model for coding agents
kind: blog
topic: models
subtopic: releases
secondary_topics:
- inference/quantization
- agents/tool-use
summary: Baseten covers Meta's Muse Spark Open, an 816B-parameter (42.7B active) omnimodal
  MoE coding-agent model, detailing its compressed MoE block and hybrid global/local
  attention (46 local 2048-token sliding-window layers vs. 16 global layers) that
  cuts KV-cache memory 3.7x at 128K context, plus the NVFP4 checkpoint that shrinks
  weights from 1.6TB to 540GB for single-node serving.
triage: null
skip_reason: null
source: baseten
url: https://www.baseten.co/blog/muse-spark-open-launch/
author: Albert Lee; Pavel Belevich; Marylise Tauzia
published: '2026-10-15'
fetched: '2026-10-16T06:10:05Z'
classifier: claude
taxonomy_rev: 2
words: 1252
content_sha256: 861b71725e986da8da4350ccda9e7a5808587499b1c646ba87816ec0403a8971
---

# Muse Spark Open, an open-weight model for coding agents

### Published

![Muse Spark Open, an open-weight model designed for coding agents](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1792085241-model-releases-1.png%3Fauto%3Dformat%26fit%3Dcrop%26h%3D630%26w%3D1200&w=3840&q=100)

Today, Meta released the weights for Muse Spark Open, an 816B-parameter open-weight omnimodal MoE model co-trained with Muse Code for coding agent workflows. Its compressed MoE block and hybrid global/local attention cut inter-GPU traffic and KV cache memory for long agent sessions. It is the most capable US open-weights model to date.

Muse Spark Open is available now on Baseten Model APIs and Dedicated Inference, served in NVFP4.

Meta released the weights for Muse Spark Open, and the open-weight release is available day 0 on Baseten Model APIs and Dedicated Inference. It is the most capable US open-weights model to date.

Muse Spark Open has:

- 816B total parameters with 42.7B active during inference,
- a 1M token context window, and
- omnimodal input (text, image, video, audio), with text output.

Muse Spark Open was co-trained with Muse Code and is specifically designed for coding agent workflows. Its omnimodal input also enables developer workflows that text-only models can’t. For agents that support image, video, or audio input, you can take advantage of:

- **Screenshot-driven UI debugging:** The agent compares a screenshot of the rendered page against a design mockup or bug report image and fixes the layout code directly.
- **Video reproduction to test case:** You record a screen capture of a bug. The agent watches it, extracts the steps, and writes a reproduction script or end-to-end test.
- **Voice-driven pair programming:** You steer the agent by talking and typing at the same time, with audio taken as direct input rather than being transcribed first.

## Competitive performance for coding agents

In addition to Muse Code, Muse Spark Open can integrate with third-party coding agents such as [OpenCode](https://opencode.ai/docs/), [Pi](https://pi.dev/docs/latest), and [Deep Agents Code](https://docs.langchain.com/oss/deepagents/code/overview). Based on [reported benchmark scores](https://developer.meta.com/ai/models/muse-spark-1-2/) from Meta, Muse Spark Open is competitive with models from other frontier labs on agentic coding and knowledge work.

On the agentic coding benchmarks, each current model was tested with its own lab's coding agent (Muse Spark with Muse Code, Claude Opus 5 with Claude Code, GPT-5.6 Terra with Codex) rather than a shared harness, so the scores reflect how each model performs in the tooling it was built for.

![Meta benchmarked Muse Spark Open against models from frontier labs. The comparison set includes each lab's flagship model, but it excludes the top-tier models above them (Claude Fable 5.1, GPT-6 Astra).](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1789506693-screenshot-2026-09-15-at-2-11-16-pm.png%3Fauto%3Dformat%26w%3D1200&w=3840&q=75) Meta benchmarked Muse Spark Open against models from frontier labs. The comparison set includes each lab's flagship model, but it excludes the top-tier models above them (Claude Fable 5.1, GPT-6 Astra).

*Source: https://developer.meta.com/ai/models/muse-spark-1-2/*

In routine agent loops (running commands, reading output, fixing what breaks), Muse Spark Open should feel close to the flagship closed models. On large, multi-file changes across many steps, expect it to need more guidance or retries than Claude Opus 5 or GPT-5.6 Terra, while holding up well against Grok 4.5 and Gemini 3.6 Flash. When an agent has to write up its work, it beats every model in the chart except Opus 5.

## A model architecture designed for agents

Coding agent workflows demand both high throughput for iterative reasoning loops and memory efficiency for long context tracking. To address these requirements, Muse Spark Open utilizes specific model architecture designs:

- A compressed Mixture-of-Experts (MoE) block that boosts throughput by reducing parameter footprint and inter-GPU traffic.
- A hybrid global/local attention schedule that shrinks KV-cache memory overhead by 3.7x at long context.

### Improved throughput performance with compressed MoE block

Coding agents read context, reason, generate, and re-read the result in a tight loop, requiring high throughput from the model. Running background subagents in parallel further pushes that throughput requirement.

To boost throughput capacity, Muse Spark Open uses a compressed mixture-of-experts (MoE) block. A shared pooler compresses the input vector before passing it to the experts, whose combined output is projected back to the original dimension by a shared unpooler. The router, which selects experts for each token, still reads the full-width vector.

![Compressed MoE adds a shared pooler before the experts and a shared unpooler after the experts' outputs are combined.](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1789668654-meta-muse_diagram-1.png%3Fauto%3Dformat%26w%3D1200&w=3840&q=75) Compressed MoE adds a shared pooler before the experts and a shared unpooler after the experts' outputs are combined.

Operating on this compressed vector:

- Halves each expert's parameters, shrinking total model size by roughly 800B parameters compared to an uncompressed design.
- Frees GPU memory for larger KV caches and concurrent sequences.
- Reduces inter-GPU traffic in the MoE layer to directly boost throughput.

### Serving long contexts efficiently with global/local attention

Coding agents accumulate context on every step as they build up task traces, reasoning, and large parts of a codebase. Every token in that context takes up GPU memory as KV cache, and in a conventional model, every layer keeps its own KV cache.

To manage GPU memory usage, Muse Spark Open uses a hybrid attention schedule. Of its 62 layers, there are 46 local attention layers that use a 2048-token sliding window with rotary position embeddings (RoPEs) to track word order. Additionally, there are 16 global attention layers that see the full sequence with no positional encoding (NoPE), relying on the word order information already captured by earlier layers.

**Conventional architecture vs. hybrid attention schedule**

![Muse Spark Open interleaves 46 local-attention layers with 16 global-attention layers, reducing KV-cache memory from 31 GiB to 8.4 GiB per sequence at 128K context, a typical agent working set. The savings grow with context length.](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1792015852-meta-muse_diagram-3.png%3Fauto%3Dformat%26w%3D1200&w=3840&q=75) Muse Spark Open interleaves 46 local-attention layers with 16 global-attention layers, reducing KV-cache memory from 31 GiB to 8.4 GiB per sequence at 128K context, a typical agent working set. The savings grow with context length.

Each local attention layer only tracks the most recent 2048 tokens, and its stored KV cache data from earlier tokens can be overwritten. Full context from the old tokens isn’t forgotten by the model and is instead preserved in the KV cache of the global attention layers. This design caps the KV cache of local attention layers, reducing KV cache memory usage by roughly 3.7x at 128K token context compared to models with only global attention layers.

## From architecture to inference optimization

A key serving-time cost for agent workloads is the memory footprint of the model weights, which caps how many agent sessions fit on a node. Baseten’s Muse Spark Open Model API addresses this by serving the NVFP4 checkpoint, which cuts the weight footprint by roughly two-thirds and frees memory for KV cache.

In the NVFP4 checkpoint, expert weights are stored in 4-bit, and full bf16 is used only where precision matters most: the attention weights and the experts in the first and last layers. This reduces the model weight size from roughly 1.6 TB to 540 GB. The full model fits on a single 4×GB300 node, avoiding multi-node interconnect for both weights and KV cache. The freed memory goes to KV cache, letting more concurrent agent sessions run on each node and increasing throughput.

## Start using Muse Spark Open

Muse Spark Open is available now on Baseten Model APIs. The endpoint is OpenAI-compatible, so you can [connect your coding agent](https://docs.baseten.co/inference/model-apis/coding-agents#agent-harnesses) and point it at Muse Spark Open without changing your harness. We serve NVFP4 weights which are optimized for Blackwell, and tool calling, reasoning output, and the full 1M context window are supported.

For teams running agents at scale, we also offer Dedicated Inference deployments with reserved capacity. [Reach out](https://www.baseten.co/talk-to-us/?model=muse-spark-12) to talk with our engineers about your workload’s specific needs.
