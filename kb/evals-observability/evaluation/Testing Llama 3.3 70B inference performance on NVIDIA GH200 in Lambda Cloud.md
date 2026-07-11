---
title: Testing Llama 3.3 70B inference performance on NVIDIA GH200 in Lambda Cloud
topic: evals-observability
subtopic: evaluation
secondary_topics:
- inference/hardware
summary: Tests Llama 3.3 70B inference performance on NVIDIA GH200 and discusses benchmark
  results.
source: baseten
url: https://www.baseten.co/blog/testing-llama-inference-performance-nvidia-gh200-lambda-cloud/
author: Pankaj Gupta; Philip Kiely
published: '2025-02-07'
fetched: '2026-07-11T04:08:27Z'
classifier: codex
taxonomy_rev: 1
words: 1086
content_sha256: 72b09c7f5c2dfd8e73b74d53c31e06e65e47133bb96f27b8c941d12a1905f370
triage: keep
skip_reason: null
---

# Testing Llama 3.3 70B inference performance on NVIDIA GH200 in Lambda Cloud

![Testing GH200 GPUs](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1747428642-gh200-gpus.png%3Fauto%3Dformat%26fit%3Dcrop%26h%3D630%26w%3D1200&w=3840&q=100)

The NVIDIA [GH200 Grace Hopper™ Superchip](https://www.nvidia.com/en-us/data-center/grace-hopper-superchip/) is a unique and interesting offering within NVIDIA’s datacenter hardware lineup. The NVIDIA Grace Hopper architecture combines an [NVIDIA Hopper](https://www.nvidia.com/en-us/data-center/technologies/hopper-architecture/) GPU with an ARM CPU via a high-bandwidth interconnect called NVLink-C2C. This is a similar architecture to the [Grace Blackwell Superchip in GB200 NVL72](https://www.nvidia.com/en-us/data-center/gb200-nvl72/).

![Product image: NVIDIA GH200 Superchip](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1738948353-hpc-corp-blog-grace-hopper-1280x680-3034121.jpg%3Fauto%3Dformat%26w%3D1200&w=3840&q=75) The NVIDIA GH200 provides a high-bandwidth connection between GPU and CPU resources.

The NVIDIA GH200 provides a high-bandwidth connection between GPU and CPU resources.This GPU-plus-CPU architecture is promising for [AI inference ](https://www.baseten.co/blog/ai-inference-explained/)workloads that require extremely large KV cache allocations. We leveraged a GH200 instance from our friends at [Lambda](https://lambdalabs.com/) to test how this architecture translates to real-world performance.

In this article, we’ll break down what makes the GH200 architecture interesting, what potential it has for high-performance inference, and the results from our early experiments serving Llama 3.3 70B on the 96GB GH200.

## GH200 vs H100 and H200

The GH200 Superchip has the exact same compute profile as the [NVIDIA H100 GPU](https://www.nvidia.com/en-us/data-center/h100/) and [NVIDIA H200 GPU](https://www.nvidia.com/en-us/data-center/h200/) and has [two different memory profiles](https://resources.nvidia.com/en-us-data-center-overview/grace-hopper-superchip-datasheet-partner) available:

However, the GH200 has the ARM CPU with a fast interconnect. While a server built around an H100 GPU has up to 64 GB/s in one-way bandwidth between the GPU and CPU, the GH200 Superchip has up to a 450 GB/s interconnect in each direction between its onboard CPU and GPU.

Thanks to this high-speed interconnect on GH200, it’s feasible to offload parts of the KV cache in the abundant CPU memory rather than the limited GPU memory during inference.

## GH200 for model serving

GH200s offer theoretical advantages over H100 GPUs on both phases of LLM inference:

- Prefill, which generates the first token, is often compute-bound. While the GH200 doesn’t offer any extra compute, offloading the KV cache to abundant CPU memory offers extra space for prefill optimizations like prefix caching and KV cache re-use.
- Generation, which creates all subsequent tokens, is often memory-bound. The GH200 offers a higher memory bandwidth than the H100, improving generation speeds.

However, the H100 and H200 GPUs can be assembled in nodes of 8 GPUs connected via low latency NVLink and NVSwitch to serve extremely large models like [Llama 405B](https://www.baseten.co/library/llama-3-1-405b-instruct/) on H100s or [DeepSeek-V3](https://www.baseten.co/library/deepseek-v3/) on H200s. Meanwhile, the GH200 is available as a single node or a dual node, called GH200 NVL2 that fully connects two GH200 Superchips with NVLink. Hence for our experiments we chose the [Llama 3.3 70B](https://www.baseten.co/library/llama-3-3-70b-instruct/) model which can fit on a single 96GB GH200 Superchip.

![Results for nvidia-smi on our GH200 instance](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1738948576-image1.png%3Fauto%3Dformat%26w%3D1200&w=3840&q=75) Results for nvidia-smi on our GH200 instance

Results for nvidia-smi on our GH200 instance## Experiment: Llama 3.3 70B on a single 96GB GH200 GPU

We generally serve Llama 3.3 70B on a 2xH100 GPU instance in FP8, or a 4xH100 instance when FP16 is necessary. But is it possible to serve the model on a single GPU?

In FP8, Llama 3.3 70B requires 70 gigabytes of VRAM to load the weights. Quantizing to INT4 is possible, but that generally results in a substantial loss in quality as measured by perplexity. Sticking with FP8, we only have 10GB of VRAM left on an 80GB H100 or 27GB left on the 96GB GH200. While this is enough space to store active KV cache for some workloads, it doesn’t leave much room for KV cache re-use.

Serving Llama 3.3 70B on GH200 allows us to take advantage of the benefits of the superchip’s unique architecture. While the active KV cache stays on the 27GB of available memory during inference, we can store additional KV cache data on CPU memory to re-use and use for prefill, unlocking these optimizations while running inference on a single GH200 Superchip.

### Inference setup

We tested Llama 3.3 70B in FP8 on a single H100 GPU instance as a baseline and GH200 to see what improvements we’d get from KV cache re-use. While this isn’t necessarily a configuration you’d use in production, it does give useful insights into the GH200 Superchip’s capabilities.

We built an optimized inference engine for both hardware options using our [TensorRT-LLM Engine Builder](https://www.baseten.co/blog/automatic-llm-optimization-with-tensorrt-llm-engine-builder/).

### Benchmark setup

While we used TensorRT-LLM to build the inference engines, we used SGLang’s benchmarking tool to gather performance data as it has a built-in KV cache re-use test.

For the inference sample, we ran the ShareGPT benchmark to simulate standard chat data. We ran our server with a batch size of 32 and configured our benchmark for full utilization.

### Benchmark results

In our testing, the GH200 Superchip outperformed the H100 GPU by 32%. The GH200 Superchip only has 21% higher VRAM bandwidth and an identical compute profile – the rest of the performance gains came from having access to a larger KV cache.

![Relative throughput for Llama 3.3 70B on ShareGPT benchmark for NVIDIA H100 and GH200](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1738948615-image2.png%3Fauto%3Dformat%26w%3D1200&w=3840&q=75) Relative throughput for Llama 3.3 70B on ShareGPT benchmark for NVIDIA H100 and GH200

Relative throughput for Llama 3.3 70B on ShareGPT benchmark for NVIDIA H100 and GH200The performance gain varies by input and output sequence length. We used the ShareGPT benchmark to ensure this testing blends a range of realistic sequence lengths to simulate actual traffic, so our results may differ from other benchmarks. To check specific sequence lengths, see [results from NVIDIA’s testing on KV cache offload performance](https://developer.nvidia.com/blog/nvidia-gh200-superchip-accelerates-inference-by-2x-in-multiturn-interactions-with-llama-models/), which found that the performance gain increased as the input sequence length grew.

These benchmarks were designed to explore the unique capabilities of the GH200 Superchip rather than to perfectly simulate production use. In future experiments, we anticipate more robust performance from upgrading to the GH200 NVL2 and testing use cases with significant prompt caching requirements.

## Conclusion: LLM serving on NVIDIA GH200

NVIDIA GH200 is an interesting processor with advantages over x86-based H100 GPUs for both prefill and generation in LLM inference. With an optimized engine, you can run high-throughput deployments of models that wouldn’t fit on a standalone GPU with the same VRAM profile. The same architecture that connects the CPU with the GPU via NVLINK-C2C powers the GB200 Grace Blackwell Superchip, which promises to be extremely powerful for model inference and supports multi-node NVLink for serving larger models.

Hopper GPUs offer several excellent options for model serving in addition to the GH200, including our daily-driver [H100 GPUs](https://www.baseten.co/blog/unlocking-the-full-power-of-nvidia-h100-gpus-for-ml-inference-with-tensorrt/) and [H100 with MIG Slices](https://www.baseten.co/blog/using-fractional-h100-gpus-for-efficient-model-serving/) for high-performance inference on smaller models, and [H200 GPUs](https://www.baseten.co/blog/evaluating-nvidia-h200-gpus-for-llm-inference/) for extremely large models like [DeepSeek-R1](https://www.baseten.co/blog/private-secure-deepseek-r1-in-production-in-us-eu-data-centers/).

For help selecting the best GPU hardware and inference optimizations for your model serving workload, [contact our engineering team](https://www.baseten.co/talk-to-us/) today!
