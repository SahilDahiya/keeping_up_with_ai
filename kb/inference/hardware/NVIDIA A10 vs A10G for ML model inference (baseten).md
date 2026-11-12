---
title: NVIDIA A10 vs A10G for ML model inference
kind: blog
topic: inference
subtopic: hardware
secondary_topics: []
summary: Compares NVIDIA's A10 and AWS's A10G GPU variants for ML inference, showing
  their tensor-compute vs CUDA-core spec differences but near-equivalence for memory-bound
  inference workloads like 7B-parameter LLMs.
triage: null
skip_reason: null
source: baseten
url: https://www.baseten.co/blog/nvidia-a10-vs-a10g-for-ml-model-inference
author: Philip Kiely
published: '2023-11-28'
fetched: '2026-11-12T06:11:40Z'
classifier: claude
taxonomy_rev: 2
words: 1300
content_sha256: a50b431bfb6b24eeb25bf8b92ef3ea6bea724f42eee4fb77da88a8a85ff7856b
---

# NVIDIA A10 vs A10G for ML model inference

Infrastructure
# NVIDIA A10 vs A10G for ML model inference

The A10, an Ampere-series GPU, excels in tasks like running 7B parameter LLMs. AWS's A10G variant, similar in GPU memory & bandwidth, is mostly interchangeable.


- Authors
- Date
- November 28, 2023

TLDR

The A10 is an Ampere-series datacenter GPU well-suited to many model inference tasks, such as running seven billion parameter LLMs. However, AWS users run those same workloads on the A10G, a variant of the graphics card created specifically for AWS. The A10 and A10G have somewhat different specs — most notably around tensor compute — but are interchangeable for most model inference tasks because they share the same GPU memory and bandwidth, and most model inference is memory bound.

The [NVIDIA A10 GPU](https://www.nvidia.com/content/dam/en-zz/Solutions/Data-Center/a10/pdf/a10-datasheet.pdf) is an Ampere-series datacenter graphics card that is popular for common ML inference tasks from running seven billion parameter LLMs to models like Whisper and Stable Diffusion XL.

However, you won’t find any A10s on AWS. Instead, [AWS has a special variant, the A10G](https://d1.awsstatic.com/product-marketing/ec2/NVIDIA_AWS_A10G_DataSheet_FINAL_02_17_2022.pdf), which [powers their G5 instances](https://aws.amazon.com/ec2/instance-types/g5/). While the A10G is similar to the A10, it isn’t exactly the same card. The two cards have some different specs — the A10 prioritizes tensor compute, while the A10G has a higher CUDA core performance — but share the same GPU memory and bandwidth.

The A10 and A10G are interchangeable for most model inference tasks. However, this isn’t obvious from their spec sheet. In this article, we’ll discover what differences exist between the cards and prove why they’re often equivalent for model inference.

The A10 and A10G, while similar, are optimized for different workloads, and that’s reflected in the stat sheet. However, as we’ll see, the cards perform similarly for most model inference tasks despite what look like major differences in key specs.

| Spec | A10 | A10G | 
|---|---|---|
| FP32 | 31.2 TF | 35 TF | 
| TF32 Tensor Core | 62.5 TF | 35 TF | 
| BFLOAT16 Tensor Core | 125 TF | 70 TF | 
| FP16 Tensor Core | 125 TF | 70 TF | 
| INT8 Tensor Core | 250 TOPS | 140 TOPS | 
| INT4 Tensor Core | 500 TOPS | 280 TOPS | 
| RT Cores | 72 | 80 | 
| GPU Memory | 24 GB GDDR6 | 24 GB GDDR6 | 
| GPU Memory Bandwidth | 600 GB/s | 600 GB/s | 
| Form Factor | 1-slot FHFL | 2-slot FHFL | 
| Max TDP Power | 150W | 300W | 

The A10 and A10G share the same GPU memory stats: 24 gigabytes of GDDR6 VRAM with a memory bandwidth of 600 gigabytes per second. Despite slight differences in core counts and form factor, the shared VRAM stats show that the A10 and A10G are closely related cards.

One difference immediately jumps out when reviewing the stat sheets: the A10G has remarkably lower tensor core compute for every level of precision, from FP32 to INT4. On the other hand, the A10G offers a slight edge in non-tensor-core FP32 compute.

At face value, this seems like a major disadvantage for the A10G. After all, most ML inference happens on tensor cores, and often in FP16 for LLMs and models like Stable Diffusion. There, the standard A10 boasts 125 TF of compute, while the A10G only has 70 TF.

However, for most workflows, this compute difference isn’t actually a meaningful factor for inference speed. Most ML model inference for LLMs and similar is memory bound, not compute bound. This means that the limiting factor on how quickly model results are generated is the time it takes to load from and save to memory during inference.

Thus, the A10 and A10G have similar performance for most model inference tasks, which we’ll prove below.

As we established above, the A10 and A10G have the same GPU memory and bandwidth, but different compute power for Tensor Cores.

What does this mean for LLM inference? In [our recent guide to LLM inference](https://www.baseten.co/blog/llm-transformer-inference-guide/), we:

- Calculated an ops:byte ratio to determine how many compute operations a given GPU is capable of doing for each byte of memory it accesses.
- Calculated the arithmetic intensity of a given LLM’s attention function to determine how much compute is required to run the model.
- Compared the ops:byte ratio to the arithmetic intensity to determine if a given model’s inference is compute bound or memory bound.

These computations are summarized below for both the A10 and A10G GPUs versus Llama 2 7B, which will have similar values to most other 7 billion parameter LLMs:

html

```
ops_to_byteA10
    = compute_bw / memory_bw 
    = 125 TF / 600 GB/S  
    = 208.3 ops / byte
ops_to_byteA10G
    = compute_bw / memory_bw 
    = 70 TF / 600 GB/S  
    = 116.6 ops / byte
arithmetic_intensity (Llama 2 7B, Single-Headed Attention Operation)
    ~= total compute / total memory movement
    = 4d(N^2) + 3N^2 ops / 8N^2 + 8Nd bytes
    = 62 ops/byte
```
The arithmetic intensity of Llama 2 7B (and similar models) is just over half the ops:byte ratio for the A10G, meaning that inference is still memory bound, just as it is for the A10.

There may be some models for which inference is compute bound, but this pattern holds true for most popular models: LLM inference tends to be memory bound, so performance is comparable between the A10 and A10G.

One place where the A10 may offer better performance is in batched inference. Batching multiple requests to the model in a single pass allows more efficient use of memory, increasing the arithmetic intensity of the model. For batched inference, the higher ops:byte ratio of the A10 can allow it to process larger batches than the A10G.

From these results, we can somewhat extrapolate to compare other GPUs with 24 GB of VRAM. We’ll look at the [datacenter-grade L4](https://images.nvidia.com/aem-dam/Solutions/Data-Center/l4/nvidia-ada-gpu-architecture-whitepaper-v2.1.pdf), the [workstation-oriented A5000](https://nvdam.widen.net/s/wrqrqt75vh/nvidia-rtx-a5000-datasheet), and the [consumer-grade RTX 3090 Ti](https://images.nvidia.com/aem-dam/Solutions/geforce/ada/nvidia-ada-gpu-architecture.pdf). The newer RTX 4090 has similar memory stats for model inference, but the RTX 3090 Ti is a better comparison to the A10 because it also uses the Ampere microarchitecture.

| Spec | A10 | A10G | L4 | A5000 | RTX 3090 Ti | 
|---|---|---|---|---|---|
| Cloud provider | Microsoft & Oracle | Amazon |  | CoreWeave | Local computer | 
| FP32 compute | 31.2 TF | 35 TF | 30.3 TF | 27.77 TF | 40 TF | 
| FP16 tensor core | 125 TF | 70 TF | 121 TF | 111.1 TF | 160 TF | 
| GPU memory | 24 GB | 24 GB | 24 GB | 24 GB | 24 GB | 
| GPU memory bandwidth | 600 GB/s | 600 GB/s | 300 GB/s | 768 GB/s | 1008 GB/s | 
| Ops:byte ratio FP16 | 208.3 ops:byte | 116.6 ops:byte | 403.2 ops:byte | 144.6 ops:byte | 158.7 ops:byte | 

Across all datacenter, workstation, and consumer cards analyzed, the pattern holds: LLM inference is memory bound as the cards’ ops:byte ratios exceed the arithmetic intensity (62 ops:byte for Llama 2 7B). Thus, memory bandwidth will have a higher impact on inference speed than tensor core compute.

When picking a GPU for model inference, the most important factor is making sure that your chosen card has enough VRAM to run the model. For example, if you’re running a 7 billion parameter LLM, you’ll pick whatever GPU is available on your cloud provider that has 24 GB of VRAM.

If you’re using a platform like Baseten that gives you access to multiple cloud providers, you might face a choice between GPUs, like the A10 vs the A10G. While the cards’ performance should be similar for most workloads, you can [calculate the bottlenecks in inference](https://www.baseten.co/blog/llm-transformer-inference-guide/) for your specific use case to make sure you’re making the best possible selection.
