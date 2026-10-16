---
title: Announcing NVIDIA Nemotron 3.5 Super VL on Baseten
kind: blog
topic: models
subtopic: releases
secondary_topics:
- inference/quantization
- agents/tool-use
summary: Baseten announces NVIDIA Nemotron 3.5 Super VL, a 120B-parameter MoE model
  (12B active) adding a vision encoder to the Nemotron 3 Super hybrid Mamba-Transformer
  architecture, with multi-token prediction and NVFP4 KV-cache quantization; it scores
  a 1190 Elo on GDPval versus 493 for the text-only predecessor.
triage: null
skip_reason: null
source: baseten
url: https://www.baseten.co/blog/nvidia-nemotron-35-super-vl-launch/
author: Albert Lee; Kenzie Amack
published: '2026-10-15'
fetched: '2026-10-16T06:10:07Z'
classifier: claude
taxonomy_rev: 2
words: 639
content_sha256: d478d0fc0650316f28781501a23bad79e26401da258fb982a7b8240c84b3c63a
---

# Announcing NVIDIA Nemotron 3.5 Super VL on Baseten

### Published

![Nemotron 3.5 Super VL is now available on Baseten](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1791914325-model_release_2x.png%3Fauto%3Dformat%26fit%3Dcrop%26h%3D630%26w%3D1200&w=3840&q=100)

There is increasing demand for agents to work with visual information in documents, and we have seen an industry-wide trend where multimodal input is becoming a standard feature across model size classes. 

This brings us to NVIDIA’s latest open model release: [Nemotron 3.5 Super VL](https://www.baseten.co/library/nemotron-35-super-vl/), which is now available on Baseten. The open multimodal model brings visual understanding, reasoning, and tool use together for applications that work with documents, images, interfaces, and video. Developers can start evaluating it for inference on Baseten (both Dedicated and Model APIs) and use Training (Baseten Loops) to customize the model for their own workloads starting today.

If your agent needs to read documents, interpret application screens, or analyze video, [NVIDIA Nemotron 3.5 Super VL](https://blogs.nvidia.com/blog/nemotron-3-5-super-vl/) combines visual understanding, reasoning, and tool use in one model.

What Super VL brings to your application:

- **Native visual understanding:** Read documents, images, application screens and video, including information that gets lost when you extract text alone
- **Reasoning and tool use:** Use visual context to decide what to do next and generate tool calls that your application can execute
- **Customization and control:** Adapt the open model to your data and workflows with the [Baseten Loops SDK](https://docs.baseten.co/loops/overview)

These features make Nemotron 3.5 Super VL well-suited for customer service, document intelligence, enterprise productivity, and web research use cases.

## Bringing vision to the Nemotron Open Models family

Nemotron 3.5 Super VL builds on the [Nemotron 3 Super](https://www.baseten.co/blog/introducing-nemotron-3-super/#latent-moe-architecture) architecture with a 120B-parameter Mixture-of-Experts model that activates 12B parameters per token.

Its hybrid Mamba-Transformer architecture supports long-context processing, while multi-token prediction (MTP) helps accelerate generation. NVFP4 KV cache quantization is designed to reduce memory requirements for long-context inference.

The addition of a vision encoder lets the model work with visual inputs alongside text. That means an agent can inspect a document layout, interpret a screenshot or analyze a video clip, then use what it finds to reason about the next step.

On Baseten, developers can evaluate Super VL using NVFP4 weights on NVIDIA Blackwell GPUs and explore customization through Baseten Training.

## Strong reasoning performance alongside multimodal capabilities

Adding visual input doesn’t mean giving up text reasoning performance. In NVIDIA’s reported evaluations, Nemotron 3.5 Super VL scores higher than Nemotron 3 Super on three text-oriented benchmarks shown below, covering professional tasks, scientific coding, and graduate-level science questions.

On GDPval, Nemotron 3.5 Super VL earns an Elo rating of 1190, compared with 493 for Nemotron 3 Super. It also scores higher on SciCode and GPQA-diamond, demonstrating improved performance on scientific reasoning tasks. These results are useful when choosing a model for applications that combine visual inputs with reasoning.

## Adapt Nemotron 3.5 Super VL to your unique data on day 0

Training support for Nemotron 3.5 Super VL dropped day 0 on [Baseten Loops](https://docs.baseten.co/loops/overview). Loops is Baseten’s managed product for supervised fine-tuning and reinforcement learning. Your training loop is a Python script that calls the Loops SDK. Baseten provisions and operates the sharing, distributed training, parallelisms, and GPU clusters behind it, so there’s no training infrastructure for your team to stand up.

Super VL joins Nemotron 3 Super and Nemotron 3 Ultra on Loops. Teams already training those can switch base models without changing tools. When a run finishes, you can deploy the trained checkpoint on Baseten and serve it from the same platform you trained on.

## Build with Nemotron 3.5 Super VL on Baseten

[Evaluate Nemotron 3.5 Super VL](https://app.baseten.co/model-apis/nvidia/NVIDIA-Nemotron-3.5-Super-VL-120B-A12B) on your own images, documents, or application screenshots with Baseten's Model API. Measure how well it understands your inputs, how reliably it generates the outputs your application needs, and whether its latency fits your workflow.

From there, connect it to your application’s tools and explore customization with [Baseten Loops](https://docs.baseten.co/loops/overview) to post-train the model on your data, tools, and policies.
