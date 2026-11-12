---
title: Announcing NVIDIA Nemotron 3.5 Super VL on Baseten
kind: blog
topic: null
subtopic: null
secondary_topics: []
summary: null
triage: null
skip_reason: null
source: baseten
url: https://www.baseten.co/blog/nvidia-nemotron-35-super-vl-launch
author: Albert Lee
published: '2026-10-15'
fetched: '2026-11-12T06:08:56Z'
classifier: null
taxonomy_rev: 2
words: 704
content_sha256: 9faa385c2bee332889f49711a64b26d3c5a37723c4b3ea524167c7f2e08e7b1e
---

# Announcing NVIDIA Nemotron 3.5 Super VL on Baseten

AI models
# Announcing NVIDIA Nemotron 3.5 Super VL on Baseten

Nemotron 3.5 Super VL is now on Baseten. It is an open 120B-A12B MoE model built for agent workflows across text, images, and video.


- Authors
- Date
- October 15, 2026

TLDR

There is increasing demand for agents to work with visual information in documents, and we have seen an industry-wide trend where multimodal input is becoming a standard feature across model size classes. This brings us to NVIDIA’s latest open model release: Nemotron 3.5 Super VL, which is now available on Baseten. The open multimodal model brings visual understanding, reasoning, and tool use together for applications that work with documents, images, interfaces, and video. Developers can start evaluating it for inference on Baseten (both Dedicated and Model APIs) and use Training (Baseten Loops) to customize the model for their own workloads starting today.

If your agent needs to read documents, interpret application screens, or analyze video, [NVIDIA Nemotron 3.5 Super VL](https://blogs.nvidia.com/blog/nemotron-3-5-super-vl/) combines visual understanding, reasoning, and tool use in one model.

What Super VL brings to your application:

- **Native visual understanding:** Read documents, images, application screens and video, including information that gets lost when you extract text alone
- **Reasoning and tool use:** Use visual context to decide what to do next and generate tool calls that your application can execute
- **Customization and control:** Adapt the open model to your data and workflows with the [Baseten Loops SDK](https://docs.baseten.co/loops/overview)

These features make Nemotron 3.5 Super VL well-suited for customer service, document intelligence, enterprise productivity, and web research use cases.

Nemotron 3.5 Super VL builds on the [Nemotron 3 Super](https://www.baseten.co/blog/introducing-nemotron-3-super/#latent-moe-architecture) architecture with a 120B-parameter Mixture-of-Experts model that activates 12B parameters per token.

Its hybrid Mamba-Transformer architecture supports long-context processing, while multi-token prediction (MTP) helps accelerate generation. NVFP4 KV cache quantization is designed to reduce memory requirements for long-context inference.

The addition of a vision encoder lets the model work with visual inputs alongside text. That means an agent can inspect a document layout, interpret a screenshot or analyze a video clip, then use what it finds to reason about the next step.

On Baseten, developers can evaluate Super VL using NVFP4 weights on NVIDIA Blackwell GPUs and explore customization through Baseten Training.

Adding visual input doesn’t mean giving up text reasoning performance. In NVIDIA’s reported evaluations, Nemotron 3.5 Super VL scores higher than Nemotron 3 Super on three text-oriented benchmarks shown below, covering professional tasks, scientific coding, and graduate-level science questions.

| Benchmark | What it measures | Metric | Nemotron 3.5 Super VL | Nemotron 3 Super | 
|---|---|---|---|---|
| GDPVal AA V2.1 | Completing multi-step tasks in professional work | Elo rating | 1190 | 493 | 
| SciCode | Writing code to solve science problems | Accuracy (%) | 47.3 | 40.8 | 
| GPQA-diamond | Answering graduate-level science questions | Accuracy (%) | 90.8 | 79.4 | 

On GDPval, Nemotron 3.5 Super VL earns an Elo rating of 1190, compared with 493 for Nemotron 3 Super. It also scores higher on SciCode and GPQA-diamond, demonstrating improved performance on scientific reasoning tasks. These results are useful when choosing a model for applications that combine visual inputs with reasoning.

Training support for Nemotron 3.5 Super VL dropped day 0 on [Baseten Loops](https://docs.baseten.co/loops/overview). Loops is Baseten’s managed product for supervised fine-tuning and reinforcement learning. Your training loop is a Python script that calls the Loops SDK. Baseten provisions and operates the sharing, distributed training, parallelisms, and GPU clusters behind it, so there’s no training infrastructure for your team to stand up.

Super VL joins Nemotron 3 Super and Nemotron 3 Ultra on Loops. Teams already training those can switch base models without changing tools. When a run finishes, you can deploy the trained checkpoint on Baseten and serve it from the same platform you trained on.

[Evaluate Nemotron 3.5 Super VL](https://app.baseten.co/model-apis/nvidia/NVIDIA-Nemotron-3.5-Super-VL-120B-A12B) on your own images, documents, or application screenshots with Baseten's Model API. Measure how well it understands your inputs, how reliably it generates the outputs your application needs, and whether its latency fits your workflow.

From there, connect it to your application’s tools and explore customization with [Baseten Loops](https://docs.baseten.co/loops/overview) to post-train the model on your data, tools, and policies.
