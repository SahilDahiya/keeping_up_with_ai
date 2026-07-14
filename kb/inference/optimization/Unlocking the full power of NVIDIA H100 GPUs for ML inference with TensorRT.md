---
title: Unlocking the full power of NVIDIA H100 GPUs for ML inference with TensorRT
topic: inference
subtopic: optimization
secondary_topics: []
summary: Shows how TensorRT unlocks H100 performance for model inference.
source: baseten
url: https://www.baseten.co/blog/unlocking-the-full-power-of-nvidia-h100-gpus-for-ml-inference-with-tensorrt/
author: Pankaj Gupta; Philip Kiely
published: '2024-02-06'
fetched: '2026-07-11T04:10:11Z'
classifier: codex
taxonomy_rev: 1
words: 1636
content_sha256: 22d6da7878274670023090ad29a089d9d6845d498845ef015253885eca31ca9e
triage: keep
skip_reason: null
---

# Unlocking the full power of NVIDIA H100 GPUs for ML inference with TensorRT

![H100 w/ TensorRT-LLM](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1747529468-h100-trt.png%3Fauto%3Dformat%26fit%3Dcrop%26h%3D630%26w%3D1200&w=3840&q=100)

NVIDIA’s H100 GPUs are the most powerful processors on the market. But running inference on ML models takes more than raw power. To get the fastest time to first token, highest tokens per second, and lowest total generation time for LLMs and models like Stable Diffusion XL, we turn to TensorRT, a model serving engine by NVIDIA. By serving models optimized with TensorRT on H100 GPUs, we unlock substantial cost savings over A100 workloads and outstanding performance benchmarks for both latency and throughput.

Deploying ML models on NVIDIA H100 GPUs offers the lowest latency and highest bandwidth inference for LLMs, image generation models, and other demanding ML workloads. But getting the maximum performance from these GPUs takes more than just loading in a model and running inference.

We’ve benchmarked inference for an LLM (Mistral 7B in fp16) and an image model (Stable Diffusion XL) using NVIDIA’s TensorRT and TensorRT-LLM model serving engines. Using these tools, we’ve achieved two to three times better throughput than A100s at equal or better latency.

Baseten is the first to offer model inference on H100 GPUs. Because H100s can double or triple an A100’s throughput, switching to H100s offers a 18 to 45 percent improvement in price to performance versus equivalent A100 workloads at current prices when using TensorRT and TensorRT-LLM.

Out of the box, H100 GPUs have substantial advantages for model inference:

- 3.35 TB/s of memory bandwidth on 80GB of VRAM — 1.6x more than the A100.
- 989.5 teraFLOPs of fp16 tensor compute — more than 3x better than the A100.
- New features and optimizations from the NVIDIA Hopper architecture.

But running inference with TensorRT/TensorRT-LLM yielded even bigger improvements over the A100 than the stat sheet would suggest:

- Double the throughput vs A100 (total generated tokens per second) and a 2x improvement in latency (time to first token, perceived tokens per second) with a constant batch size for Mistral 7B.
- Triple the throughput vs A100 (total generated tokens per second) and constant latency (time to first token, perceived tokens per second) at increased batch sizes for Mistral 7B.
- Similar results for Stable Diffusion XL, with 30-step inference taking as little as one and a half seconds.

In this report, we’ll review our benchmarks for Mistral 7B and Stable Diffusion XL and discuss why TensorRT/TensorRT-LLM offer such excellent performance for model inference on H100 GPUs.

## Why TensorRT and TensorRT-LLM improve H100 inference

The H100 isn’t just an A100 with more cores and faster memory. It uses NVIDIA’s [Hopper](https://en.wikipedia.org/wiki/Hopper_(microarchitecture)) architecture, named for US navy rear admiral Grace Hopper. The Hopper architecture is the datacenter-oriented sibling of NVIDIA’s [Lovelace](https://en.wikipedia.org/wiki/Ada_Lovelace_(microarchitecture)) architecture, which powers consumer GPUs like the RTX 4090 and smaller datacenter-grade GPUs like the [L4](https://www.baseten.co/resources/changelog/nvidia-l4-gpus-now-generally-available-on-baseten/).

The Hopper architecture offers a wide array of new features to complement larger core counts, bandwidth, and caches. Diving [deeper into the architecture](https://developer.nvidia.com/blog/nvidia-hopper-architecture-in-depth/) reveals optimizations like thread block clusters, distributed shared memory, asynchronous execution, a new tensor memory accelerator, and dozens more. These optimizations are designed to give the H100 an additional edge in ML inference, among other workloads.

Not every model uses every feature. That’s where TensorRT comes in. TensorRT is a toolkit for model inference optimization. It’s built by NVIDIA, so takes full advantage of the new features in the H100 GPU. With TensorRT, you build model-specific engines that optimize individual model layers and CUDA instructions to maximize performance. This unlocks a bigger increase in inference performance than raw stats can account for alone.

## Better throughput from higher memory bandwidth

The main measure for LLM inference, tokens per second (TPS), describes how quickly the model can output text. [This inference phase is memory bound](https://www.baseten.co/blog/llm-transformer-inference-guide/), so the H100’s increased memory bandwidth is essential.

There are three variants of H100s. We exclusively use SXM H100s, which offer much better performance than PCIe variants thanks to their higher memory bandwidth. Similarly, from the A100s available, we only use best-in-class 80GB SXM A100s, which have the highest bandwidth — we’re making an apples-to-apples comparison.

These H100 GPUs have 3.35 TB/s of memory bandwidth, while the equivalent A100s have just 2.039 TB/s of memory bandwidth, meaning the H100s have approximately 1.64 times the memory bandwidth of the A100.

This increased memory bandwidth has a direct impact on an LLM’s performance. There are [two metrics](https://www.baseten.co/blog/understanding-performance-benchmarks-for-llm-inference/) that we look at when benchmarking tokens per second:

- Perceived TPS — how many tokens an individual user gets per second in response to their prompt. This is a latency metric, 50 TPS is a decent threshold for chat.
- Total generated TPS — how many tokens the model generates per second across its entire batch of requests. This is a throughput metric, you want this to be as high as possible to get the most performance per dollar from your GPU.

As detailed in the table below, both perceived tokens per second and total generated tokens per second of an H100 are approximately double the performance of an A100, keeping batch size constant and testing 300 input tokens with 1000 output tokens. The measured performance is better than expected — we’d only expect 64% better performance from increased memory bandwidth — thanks to the optimizations provided by TensorRT-LLM.

## Faster time to first token from better Tensor compute

The [prefill phase of LLM inference](https://developer.nvidia.com/blog/mastering-llm-techniques-inference-optimization/) is unique because it’s compute bound. In prefill, the model takes the entire set of input tokens and uses it to generate the first output token. Doing this operation requires a lot of tensor compute power but relatively little memory access, so in this case it’s the H100’s 989.5 teraFLOPS of fp16 tensor compute that give the H100 its edge.

We pay extra attention to how fast the prefill phase completes because it directly informs time to first token — an essential metric for latency. Time to first token is the measure of how fast the LLM starts responding with streaming output. A fast time to first token means a snappy user experience.

Comparing H100 to A100 prefill times, we see that H100 prefill is consistently 2-3x faster than A100 across all batch sizes. This was measured with 300 input tokens and will vary based on input sequence length, but the relative speedup of the H100 should remain similar across most sequence lengths.

Time to first token also depends on factors like network speed, but we can observe from this table that H100s dramatically improve prefill performance, which corresponds directly to faster time to first token.

## 3x better throughput from constant latency

The “free” improvement in perceived tokens per second and time to first token alongside 2x higher throughput can be great for some use cases. But if you’re already satisfied with the performance of your model, you can save even more on cost by increasing batch sizes to get more throughput from the same hardware — in some cases 3x or more.

To see how, let’s take a look at a combined table of the above benchmarks.

Say you’re running Mistral 7B on an A100 with a goal of maximizing throughput while still supporting strong latency numbers:

- 50 perceived tokens per second per request
- Time to first token under 1 second

What batch size should you pick on an A100 and H100? Let’s look at a simplified table of relevant values:

From the table, we see that:

- On an A100, a batch size of 32 achieves your latency target with a total throughput of 1,771 tokens per second.
- If you keep the batch size the same when switching to H100, you get double the throughput.
- If you instead increase the batch size to 64 when switching to H100, you get triple the throughput while staying under your latency target.

Factors like input and output sequence lengths and model-specific performance quirks can somewhat alter these values, but the H100 gives you more room to increase throughput if you’re willing to accept lower gains on latency. This results in substantial performance-per-dollar improvements: in this case 45% with triple the throughput.

## Faster inference for Stable Diffusion XL

These performance gains aren’t limited to large language models. TensorRT also supports models like Stable Diffusion XL (SDXL), which see similar performance improvements from H100s.

[SDXL inference](https://www.baseten.co/blog/how-to-benchmark-image-generation-models-like-stable-diffusion-xl/) benefits from both increased compute and increased memory bandwidth. For 30 steps of SDXL with TensorRT and a batch size of 1, we see:

- H100: 1.478 seconds latency, 0.68 images/second throughput
- A100: 2.742 seconds latency, 0.36 images/second throughput
- A10G: 8.16 seconds latency, 0.12 images/second throughput

Out of the box, you’re again getting nearly double the performance on both latency and throughput. Like with LLMs, you can trade off latency and throughput to a degree by increasing batch sizes for SDXL inference.

See our [deep dive into SDXL inference with TensorRT](https://www.baseten.co/blog/40-faster-stable-diffusion-xl-inference-with-nvidia-tensorrt/) for complete benchmarks.

## Save 18 to 45 percent by switching A100 workloads to H100s

We’re offering optimized model inference on H100 GPUs at $9.984/hour. We offer instances with 1, 2, 4, or 8 H100 GPUs to handle even the largest models, and can run both open source and custom models on TensorRT/TensorRT-LLM to take full advantage of the H100’s compute power.

The H100 offers 2x to 3x better performance than the A100 for model inference, but costs only 62% more per hour. This means that switching to H100s offers substantial savings on workloads that require multiple A100-backed instances:

- Save about 18% with 2x throughput and get lower latency for free
- Save as much as 45% with 3x throughput and get comparable latency

To deploy Mistral 7B, [Mixtral 8x7B](https://www.baseten.co/library/mixtral-8x7b-instruct/), [Stable Diffusion XL](https://www.baseten.co/library/stable-diffusion-xl/), or any other open source or custom model on H100 GPUs, [get in touch and tell us about your use case](https://share.hsforms.com/110ZOAIthRo6IgZXjfPE6tQd5zj5) — we’d love to help you take full advantage of these incredible GPUs.
