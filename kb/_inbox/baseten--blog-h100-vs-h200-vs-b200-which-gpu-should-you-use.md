---
title: 'H100 vs. H200 vs. B200: which GPU should you use?'
kind: blog
topic: null
subtopic: null
secondary_topics: []
summary: null
triage: null
skip_reason: null
source: baseten
url: https://www.baseten.co/blog/h100-vs-h200-vs-b200-which-gpu-should-you-use
author: Chloe Florit
published: '2026-07-02'
fetched: '2026-11-12T06:07:50Z'
classifier: null
taxonomy_rev: 2
words: 1383
content_sha256: 81e27e0f19144a5a614fb403d3141f3045eb3898c078ae38bf54dab30e6c76a8
---

# H100 vs. H200 vs. B200: which GPU should you use?

Infrastructure
# H100 vs. H200 vs. B200: which GPU should you use?

H100, H200, and B200 GPUs each make different tradeoffs in memory, compute, and cost. Learn which one fits your model size, traffic, and budget.


- Authors
- Date
- July 2, 2026

TLDR

H100, H200, and B200 GPUs each offer different tradeoffs in memory, compute, and cost for AI inference. The right GPU depends on your model size, traffic volume, and budget: H100 with MIG is cost-effective for smaller models and sporadic traffic, H200 can run very large models like DeepSeek-R1 on a single node, and B200's FP4 support and higher memory bandwidth make it the best choice for high-throughput production inference at scale.

LLMs. Voice AI. Agentic pipelines. Every high-performance AI workload runs on a GPU, and the one you choose determines your model’s latency, throughput, and cost. We want to help you find which GPU (H100, H200, B200) is best for your use case. Here’s how they compare.

We exclusively use SXM GPUs for their higher memory bandwidth compared to PCIe, which speeds up inference. SXM connects GPUs directly over NVLink (\~900 GB/s) with higher power limits, so GPUs run faster. PCIe relies on a slower, shared link (\~10x slower GPU-to-GPU) with less power, which can reduce throughput, especially for large models split across multiple GPUs.

| GPU | H100 SXM | H200 SXM | B200 SXM | 
|---|---|---|---|
| Architecture | Hopper | Hopper | Blackwell | 
| Memory | 80 GB HBM3, 3.35 TB/s | 141 GB HBM3e, 4.8 TB/s | 180 GB HBM3e, 8 TB/s | 
| VRAM, 8x node | 640 GB | 1,128 GB | 1,440 GB | 
| FP4 Compute (Dense) | N/A | N/A | 144 PFLOPS | 
| FP8 Compute (Dense) | 7,916 TFLOPS | 7,916 TFLOPS | 72 PFLOPS | 
| FP16 Compute (Dense) | 3,958 TFLOPS | 3,958 TFLOPS | 9 PFLOPS | 
| Power (TDP) | 700W | 700W | 1,000W | 

*Note: Inference runs without sparsity.* 

A GPU node is a physical server with CPUs, system RAM, local storage, networking, and one or more GPUs. A node typically has 8 GPUs because many setups for inference and training (e.g., tensor parallelism, data parallelism) split cleanly across 2, 4, or 8 GPUs. Tensor parallelism splits computations (large matrix multiplies) across multiple GPUs. Data parallelism copies the full model onto each GPU and splits batches across GPUs (typically requests for inference and data for training).

When you shard model weights across 8 GPUs, the total node VRAM determines which model you can fit.

Across the three nodes:

- H100 SXM (8x), 640 GB: fits mid-to-large models
- H200 SXM (8x), 1,128 GB: fits very large models; more long-context headroom
- B200 SXM (8x), 1,440 GB: most headroom of the three

Here's a concrete example: [GLM 5.2](https://www.baseten.co/library/glm-52/) at 744B parameters requires roughly 755 GB of weights in FP8 alone, which is over what a single H100 node can hold. H200 and B200 nodes can fit the model on a single node with memory left over for KV cache, activations, and other overhead. More room for KV cache allows for longer context windows at the same batch size (number of requests processed during inference).

NVLink is what makes those 8 GPUs behave like one big one rather than 8 separate ones. During inference, NVLink increases the speed at which weights and activations move between GPUs, which matters most when running large models that span multiple GPUs.

If you’re running smaller models, Multi-Instance GPU (MIG) physically partitions one GPU into up to 7 isolated slices, each with its own memory and compute. Each fractional GPU can run in parallel on an independent model server, which means you can serve multiple smaller models on a single GPU or split one GPU across tenants. A fractional H100, for example, can match or beat the performance of a full A100 GPU at a lower cost. Strong use cases for MIG include very small embedding models (\<3B params) and voice-in/voice-out models.

However, MIGs aren’t a fit for everything: large models (at Mixtral 8x7B-scale and above) or workloads needing big batch sizes (e.g., a large number of training samples) still need a full GPU.

To increase throughput for these large models, the NVIDIA Blackwell architecture introduced NVFP4, a 4-bit floating-point format that's more memory-efficient and faster than FP8. Blackwell's Tensor Cores can perform more operations per second on 4-bit numbers, so the GPU spends less time waiting on memory and more time computing.

Blackwell’s 2nd-gen Transformer Engine can switch between FP4, FP8, and FP16 per layer, which preserves accuracy where it matters and ensures minimal quality loss. FP4 cuts weight memory by up to \~3.5x vs. FP16. That freed memory can go toward the KV cache and longer context.

FP4 on B200 means you can run larger models on fewer GPUs or serve more context per GPU on models you’re already running.

In addition to optimizing FP precision, high-throughput inference also depends on how efficiently data moves from the HBM (High Bandwidth Memory). Before async programming, the GPU had to wait for HBM to finish loading data into on-chip GPU memory (shared memory/registers/L2) before each compute step could start. The hardware would be idle for a significant part of the inference cycle.

Async programming changes that by overlapping loading and computing. The next chunk of data loads while the current chunk is still being computed on.

In the Hopper architecture, the GPU has dedicated hardware (Tensor Memory Accelerator) to handle loading the data so that threads (tiny workers within the GPU) can focus on compute instead of moving data around.

The Blackwell architecture takes this further with Tensor Memory (TMEM), a space on the GPU that holds the running totals of a matrix multiplication. This way, less time is spent waiting for data.

To put this into practice, [TensorRT-LLM](https://docs.baseten.co/examples/tensorrt-llm) selects which kernel and which async programming strategy actually runs, depending on the Hopper or Blackwell architecture.

You should pick the GPU that matches your model size, traffic volume, and budget.

H100 is great for:

- Embedding, speech-to-text, and text-to-speech models.
- Small-to-mid models or multi-tenant serving with MIG.
- Low or sporadic traffic, where cost outweighs B200's throughput gains.

H200 is great for:

- Training large models that need maximum memory.
- Running a large model at moderate scale.

B200 is great for:

- LLMs, image generation, and video generation.
- High-throughput production inference at scale, especially with TensorRT-LLM.
- Running models in FP4 without compromising output quality.

**When is the price premium for B200 worth it?** 

When you're running high-traffic production inference and GPU usage is consistently high. At low or sporadic traffic, you're paying for throughput you're not using. At scale, B200's memory bandwidth and FP4 support mean you're serving more requests per GPU, which can make the per-token cost competitive with H100 even at a higher list price.

**What is MIG and when should I use it?**

MIG (Multi-Instance GPU) physically partitions a single GPU into up to seven isolated slices, each with its own memory and compute. It's the right fit when your model doesn't need a full GPU: smaller models, low-traffic deployments, or multi-tenant serving. It's not a fit for large models or workloads that need big batch sizes.

**Does FP4 hurt model quality?**

It depends on the model and use case. FP4 is a [more aggressive quantization](https://docs.baseten.co/engines/performance-concepts/quantization-guide) than FP8, so there's a higher risk of accuracy degradation on tasks sensitive to numerical precision. Blackwell's Transformer Engine mitigates this by switching between FP4, FP8, and FP16 per layer, which preserves precision where the model needs it most. In practice, for most production inference workloads the quality tradeoff is acceptable.

**Should I go multi-node or upgrade to H200/B200?**

If your model fits on a single H200 or B200 node, that's almost always the simpler and cheaper path. Only go [multi-node](https://www.baseten.co/blog/how-multi-node-inference-works-llms-deepseek-r1/) when the model genuinely can't fit on a single node at the precision level you need.

**Which GPU is best for training vs inference?**

All three GPUs (H100, H200, B200) can be used for both training and inference. H100 is commonly used for training and cost-sensitive inference, H200 is preferred for large-model training due to memory capacity, and B200 is optimized for high-throughput inference but can also be used for large-scale training workloads.
