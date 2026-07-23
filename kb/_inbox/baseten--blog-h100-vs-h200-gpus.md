---
title: H100 vs. H200 GPUs
kind: blog
topic: null
subtopic: null
secondary_topics: []
summary: null
triage: null
skip_reason: null
source: baseten
url: https://www.baseten.co/blog/h100-vs-h200-gpus/
author: Chloe Florit
published: '2026-07-23'
fetched: '2026-07-23T06:49:53Z'
classifier: null
taxonomy_rev: 2
words: 1017
content_sha256: 3f42de45e29bb74c3fc4fc2374bbca3dd93167680010c09da37aa71b89f1eab4
---

# H100 vs. H200 GPUs

![H100 vs. H200](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1783019358-baseten-blog-2026-thumbnails-5.png%3Fauto%3Dformat%26fit%3Dcrop%26h%3D630%26w%3D1200&w=3840&q=100)

The H100 GPU is a cost-effective choice for small-to-mid-sized models and lower or sporadic traffic. H200’s larger HBM3e memory and higher memory bandwidth make it better suited for very large models, long-context inference, and workloads that need more KV cache headroom. In this post, we’ll compare H100 and H200 specs, explain how node-level VRAM affects model fit, and cover techniques like MIG and async programming that help improve throughput, reduce cost, and minimize latency.

Inference is critical to AI workflows like agentic coding, chatbots, and intelligent search. H100 and H200 GPUs are built to power these applications, but they have different strengths. We want to help you find which GPU (H100, H200) is best for your use case. Here’s how they compare.

**Comparing hardware specs **

We exclusively use SXM GPUs for their higher memory bandwidth compared to PCIe, which speeds up inference. SXM connects GPUs directly over NVLink (~900 GB/s) with higher power limits, so GPUs run faster. PCIe relies on a slower, shared link (~10x slower GPU-to-GPU) with less power, which can reduce throughput, especially for large models split across multiple GPUs.

*Note: Inference runs without sparsity. *

**VRAM on an 8x node: what it means for model size **

A GPU node is a physical server with CPUs, system RAM, local storage, networking, and one or more GPUs. A node typically has 8 GPUs because many setups for inference and training (e.g., tensor parallelism, data parallelism) split cleanly across 2, 4, or 8 GPUs. Tensor parallelism splits computations (large matrix multiplies) across multiple GPUs. Data parallelism copies the full model onto each GPU and splits batches across GPUs (typically requests for inference and data for training).

When you shard model weights across 8 GPUs, the total node VRAM determines which model you can fit.

Across the three nodes:

- H100 SXM (8x), 640 GB: fits mid-to-large models 
- H200 SXM (8x), 1,128 GB: fits very large models; more long-context headroom 

Here's a concrete example: GLM 5.2 at 744B parameters requires roughly 755 GB of weights in FP8 alone, which is over what a single H100 node can hold. H200 nodes can fit the model on a single node with memory left over for KV cache, activations, and other overhead. More room for KV cache allows for longer context windows at the same batch size (number of requests processed during inference).

NVLink is what makes those 8 GPUs behave like one big one rather than 8 separate ones. During inference, NVLink increases the speed at which weights and activations move between GPUs, which matters most when running large models that span multiple GPUs.

**MIG: bringing frontier hardware to small models**

If you’re running smaller models, Multi-Instance GPU (MIG) physically partitions one GPU into up to 7 isolated slices, each with its own memory and compute. Each fractional GPU can run in parallel on an independent model server, which means you can serve multiple smaller models on a single GPU or split one GPU across tenants. A fractional H100, for example, can match or beat the performance of a full A100 GPU at a lower cost. Strong use cases for MIG include very small embedding models (<3B params) and voice-in/voice-out models.

However, MIGs aren’t a fit for everything: large models (at Mixtral 8x7B-scale and above) or workloads needing big batch sizes (e.g. a large number of training samples) still need a full GPU.

**Async programming: how to keep GPUs from waiting **

To increase throughput for these large models, GPUs use async programming. Before async programming, the GPU had to wait for HBM to finish loading data into on-chip GPU memory (shared memory/registers/L2) before each compute step could start. The hardware would be idle for a significant part of the inference cycle.

Async programming changes that by overlapping loading and computing. The next chunk of data loads while the current chunk is still being processed.

In the Hopper Architecture, the GPU has dedicated hardware (Tensor Memory Accelerator) to handle loading the data so that threads (tiny workers within the GPU) could focus on compute instead of moving data around.

**Suggested models for use case **

You should pick the GPU that matches your model size, traffic volume, and budget.

H100 is great for:

- Embedding, speech-to-text, and text-to-speech models. 
- Small-to-mid models or multi-tenant serving with MIG. 
- Low or sporadic traffic, - [where cost outweighs B200's throughput gains](https://www.baseten.co/blog/h100-vs-h200-vs-b200-which-gpu-should-you-use/).

H200 is great for:

- Training large models that need maximum memory. 
- Running a large model at moderate scale. 

**FAQ **

**Why does GPU memory bandwidth matter for AI inference?**

Memory bandwidth determines how quickly a GPU can move data between high-bandwidth memory (HBM) and its compute cores. For large language models, faster memory bandwidth helps keep the GPU fed with data, reducing bottlenecks during inference. While the H100 and H200 offer the same peak compute performance, the H200's higher memory bandwidth can improve performance for memory-intensive workloads, especially large models and long-context inference.

**Why does GPU memory matter for large language models?**

GPU memory determines whether a model can fit entirely on a GPU node and how much memory remains for KV cache, activations, and runtime overhead. More available VRAM also allows longer context windows and higher batch sizes without reducing performance. For large foundation models, memory is often the primary limiting factor.

**Which GPU is better for AI inference: H100 or H200?**

It depends on your model size. The H100 is an excellent choice for embeddings, speech models, small-to-medium LLMs, and multi-tenant inference with MIG. The H200 is better for serving very large language models that require more GPU memory or longer context windows because it can keep more model weights and KV cache on a single node.

**What is MIG and when should I use it?**

MIG (Multi-Instance GPU) physically partitions a single GPU into up to seven isolated slices, each with its own memory and compute. It's the right fit when your model doesn't need a full GPU: smaller models, low-traffic deployments, or multi-tenant serving. It's not a fit for large models or workloads that need big batch sizes.
