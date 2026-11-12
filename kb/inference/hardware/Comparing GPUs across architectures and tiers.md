---
title: Comparing GPUs across architectures and tiers
kind: blog
topic: inference
subtopic: hardware
secondary_topics: []
summary: Explains how to compare datacenter GPUs across generations using core type
  (CUDA/Tensor/RT), FLOPS, VRAM, and TDP rather than marketing generation names.
triage: null
skip_reason: null
source: baseten
url: https://www.baseten.co/blog/comparing-gpus-across-architectures-and-tiers
author: Philip Kiely
published: '2023-05-22'
fetched: '2026-11-12T06:11:14Z'
classifier: claude
taxonomy_rev: 2
words: 833
content_sha256: fc400c77f66326c1cada2d83fca0c17db7a322f7117c39c932dc7d7c7197b94c
---

# Comparing GPUs across architectures and tiers

Infrastructure
# Comparing GPUs across architectures and tiers

So what are reliable metrics for comparing GPUs across architectures and tiers? We’ll consider core count, FLOPS, VRAM, and TDP.


- Authors
- Date
- May 22, 2023

TLDR

Advertising for GPUs is designed to drive excitement and demand year after year. But as the industry evolves, certain benchmarks remain consistent from generation to generation. This guide helps you make fair comparisons between graphics cards based on your real-world needs.

Datacenter GPUs remain relevant for years — there are still K80s running production workloads today — while the terms used to market the cards change over time as NVIDIA highlights the advantages of each new series of GPUs.

So what are reliable metrics for comparing GPUs across architectures and tiers to decide which one is the most cost-effective way to run your workload? We’ll consider core count, FLOPS, VRAM, and TDP.

The graphics cards you analyze might have several different types of cores:

- **CUDA cores**: the most general-purpose cores for a wide variety of computing tasks.
- **Tensor cores:** optimized for certain machine learning calculations.
- **Ray-tracing (RT) cores:** more important for gaming than most ML, these cores specialize in simulating the behavior of light.

Raw core count is a good signal, but it isn’t the whole story. Different cards have different types of cores — some have more tensor cores, others have more CUDA cores — and cards on newer architectures may also have new generations of some types of core. A proper comparison requires a more standardized metric: FLOPS.

FLOPS stands for Floating Point Operations Per Second and is the critical measure of GPU performance.

There’s a complicating factor, though. GPU performance is measured at various precisions. Precision is the size of each number in a calculation, from 8-bit integers to 64-bit double precision floating point values.

Computations on higher-precision number formats take more processing power. But that’s where Tensor cores come into play. Tensor cores can do mixed-precision computation, where they use a lower precision for most calculations then validate the results at a higher precision. Compare FLOPS at the same precision on the same core type for a proper apples-to-apples comparison between GPUs.

For example, at the highest precision (FP64), NVIDIA’s top-shelf A100 GPU reaches 9.7 teraFLOPS on standard CUDA cores, but its Tensor cores double that performance at the same precision with 19.7 teraFLOPS.

Lower precisions result in higher FLOPS counts. For example, here’s a comparison of compute power for the A10 and A100 GPUs at different precisions.

| Precision | A10 Tensor Core | A100 80GB Tensor Core | 
|---|---|---|
| FP32 | 62.5 teraFLOPS | 156 teraFLOPS | 
| FP16 | 125 teraFLOPS | 312 teraFLOPS | 
| INT8 | 250 teraFLOPS | 624 teraFLOPS | 

Comparison of operations per second on A10 and A100 at different precisions

[VRAM](https://en.wikipedia.org/wiki/Video_random-access_memory) (Video Random Access Memory) is a graphics card’s onboard memory. VRAM is to GPUs as RAM is to CPUs. It stores data like model weights for rapid access during computations like model inference.

The most important factor for model serving is the amount of VRAM that a GPU has. For fast invocation, model weights must be stored in VRAM, so VRAM capacity limits model size.

Not all VRAM is equivalent. There are three other factors to consider:

- **Bus size** measures the amount of data that can be transferred to and from VRAM at once. A larger bus is helpful for loading model weights faster.
- **Clock speed** measures how fast the VRAM can process data, with higher clock speeds resulting in faster memory reads and writes.
- **GDDR** and **HBM** are two different types of VRAM. HBM (High Bandwidth Memory) generally provides higher bandwidth with less power but costs more to manufacture than GDDR (Graphic Double Data Rate) memory. Recent 100-tier cards like the A100 and H100 use HBM.

To add a wrinkle, not all GPUs of the same tier have the same amount of VRAM. For example, the A100 comes in 40GB and 80GB versions. So before provisioning a GPU, make sure it has the right amount of VRAM to run your model.

TDP stands for Thermal Design Power, and it refers to the maximum number of Watts of electricity that a GPU is designed to draw while running. Higher-tier cards generally have a larger TDP than lower-tier cards, but it’s not a perfect correlation.

Datacenters price GPU compute time based on a variety of factors, but a card’s TDP is one of them. Electricity costs money, and it also generates heat, which costs even more money to get rid of. So cards with a higher TDP have a higher operating cost, which will affect the price you pay as an end user for compute time.

There have been two dozen datacenter GPUs released in the last decade. Here’s a [complete table of specs for datacenter GPUs](https://en.wikipedia.org/wiki/List_of_Nvidia_graphics_processing_units#Data_Center_GPUs).

Or, focus your search with our breakdown of [NVIDIA’s T4 vs A10 GPUs](https://www.baseten.co/blog/comparing-nvidia-gpus-for-ai-t4-vs-a10/), two popular cards for model serving.
