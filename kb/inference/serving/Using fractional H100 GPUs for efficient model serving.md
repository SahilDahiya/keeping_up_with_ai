---
title: Using fractional H100 GPUs for efficient model serving
topic: inference
subtopic: serving
secondary_topics:
- infra-platform/cost
summary: Explains fractional H100 usage for efficient model serving and better GPU
  utilization.
source: baseten
url: https://www.baseten.co/blog/using-fractional-h100-gpus-for-efficient-model-serving/
author: Matt Howard; Vlad Shulman; Pankaj Gupta; Philip Kiely
published: '2024-03-28'
fetched: '2026-07-11T04:09:49Z'
classifier: codex
taxonomy_rev: 1
words: 1101
content_sha256: 523ddfbd941ecf934687470f45d09fb3c6e2b34f7b3938b4f8805516ac8d6556
triage: keep
skip_reason: null
---

# Using fractional H100 GPUs for efficient model serving

![H100 MIGs](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1747527094-h100-mig.png%3Fauto%3Dformat%26fit%3Dcrop%26h%3D630%26w%3D1200&w=3840&q=100)

NVIDIA A100 and H100 GPUs offer high-performance inference for ML models. We want to get the most performance possible given available hardware, so we’ve begun using a feature of H100 GPUs that allows us to split a single physical GPU across two model serving instances. These instances often meet or exceed the performance of A100 GPUs at a 20% lower cost.

NVIDIA H100 GPUs support [Multi-Instance GPU (MIG)](https://www.nvidia.com/en-us/technologies/multi-instance-gpu/), which lets us serve models on fractional GPUs. We can get two H100 MIG models serving instances per H100 GPU, each with about half of the power of a full GPU. Splitting H100 GPUs into two parts allows for more flexibility in hardware choice for model inference.

H100 MIG model serving instances offer several advantages for inference versus using A100 GPUs:

- Equal or better performance to A100 GPUs for workloads optimized with TensorRT at a 20% lower list price.
- Support for FP8, which expands options for quantizing models.
- Increased flexibility and availability of GPUs across cloud providers and regions.

This guide breaks down how MIG works, what specs a fractional H100 GPUs offer, and what performance to expect serving models on H100 MIG-based instances.

## How Multi-Instance GPUs work

MIG was introduced with NVIDIA’s Ampere architecture and is also supported on Hopper and Blackwell. MIG which enables splitting the GPU into multiple fractional GPUs, each of which can run an independent model server.

Fractional GPUs are assembled from physical slices of compute and memory from the GPU:

- 7 compute slices that evenly divide the streaming multiprocessors on the chip.
- 8 memory slices that evenly divide the VRAM on the chip.

At first, 7 compute slices seems strange. It’s not due to any reserved compute for overhead, rather, it’s due to the fact that the H100 GPU has 140 streaming multiprocessors (SMs), which are evenly distributed into 7 slices, each with 20 SMs. There are also 7 NVDEC and JPEG image decoders in an H100 GPU; one of each is allocated per slice. Memory is more straightforward: each of the 8 memory slices has 10 GB of VRAM and an eighth of the GPU’s total memory bandwidth.

There are [19 different profiles on H100 GPUs](https://docs.nvidia.com/datacenter/tesla/mig-user-guide/index.html#h100-profiles), meaning that you can divide the card up in 19 different configurations, but we use a single profile which splits the card into two MIG 3g.40gb instances.

The 3g.40gb name means that the instance has three compute slices and forty gigabytes of VRAM. We chose this specific profile for its usefulness in model serving and its close approximation of the performance of an A100 GPU.

## H100 MIG vs A100 specs

The fractional H100 GPUs that we use have three-sevenths the compute and half of the memory of a full H100 GPU. But how do those specs compare to A100 GPUs?

Compared to the 80GB SXM A100 (the most powerful A100 variant — we use this one for model inference), the fractional H100 GPU (also SXM) has stronger compute but worse memory bandwidth.

In summary, versus an A100 GPU an H100 MIG has:

- 36% higher compute on supported precisions.
- Support for FP8 precision.
- 18% lower memory bandwidth on half the memory.

But there’s more to performance than raw specs. On the surface level, it would seem that higher compute would help with prefill (and in turn time to first token) for LLMs, but the lower memory bandwidth would limit speed as [most parts of LLM inference are memory bound](https://www.baseten.co/blog/llm-transformer-inference-guide/). However, we serve high-performance models with TensorRT, which utilizes the architectural advantages of H100 GPUs, even when using H100 MIG. This results in equal or better performance on H100 MIG versus A100 GPUs for many models despite the memory bandwidth limitations.

## H100 MIG vs A100 performance

A fractional H100 GPU with 3 of 7 SM slices and a 40GB VRAM allocation met or slightly exceeded the performance on an A100 GPU in our benchmarks for models served with TensorRT and TensorRT-LLM.

### Stable Diffusion XL performance

For 30 steps of [SDXL optimized with TensorRT](https://www.baseten.co/blog/40-faster-stable-diffusion-xl-inference-with-nvidia-tensorrt/), we found that performance was nearly equivalent between an H100 MIG and an A100 GPU.

The difference in observed generation time — less than 100 milliseconds — is within the expected run-to-run variance of this kind of benchmark. We expect the fractional H100 GPUs to have equivalent performance to A100 GPUs for SDXL workloads.

### Mistral 7B performance

For a benchmark of Mistral 7B running in FP16 with 300 input tokens and 1000 output tokens at a batch size of 32, we observed that an H100 MIG offered slight advantages over an A100 GPU in both throughput and latency.

Thanks to TensorRT-LLM, the H100 MIG demonstrated 20% lower latency and 6% higher total throughput than the A100 GPU. The long prefill time — when the LLM is calculating the first token of output — is due to the relatively large input sequence. Prefill, and thus time to first token, will be much faster with shorter chat-style inputs and outputs.

The H100 GPU also supports FP8, which A100 GPUs do not support. Running smaller LLMs like [Mistral 7B in FP8 can provide lower latency and higher throughput](https://www.baseten.co/blog/33-faster-llm-inference-with-fp8-quantization/) with a near-zero loss in quality. Using FP8 can boost H100 MIG performance to further exceed the A100 GPU’s capabilities.

## When to use fractional H100 GPUs

Model serving instances backed by fractional H100 GPUs are available on Baseten at a 20% lower list price than comparable instances using A100 GPUs. A fractional H100 GPU can match or exceed the performance of an A100 GPU for ML inference, offering a meaningful improvement in performance per dollar for many workloads.

H100 MIG instances are great for:

- Optimizing high-throughput deployments of smaller models like Mistral 7B and - [SDXL](https://www.baseten.co/library/stable-diffusion-xl/).
- Running models in - [FP8 for faster performance without compromising output quality](https://www.baseten.co/blog/fp8-efficient-model-inference-with-8-bit-floating-point-numbers/).
- Fine-grained autoscaling by increasing and decreasing capacity with half of a GPU at a time.

However, H100 MIG instances aren’t a good fit for:

- Running inference on large models like - [Mixtral 8x7B](https://www.baseten.co/library/mixtral-8x7b-instruct/)which require a lot of VRAM.
- Building model servers with large batch sizes to trade off some latency for extra throughput.
- Serving unoptimized model implementations that can’t take advantage of the H100’s architectural features.

In these cases, an instance backed by an A100 or a full H100 GPU would be a better fit.

To get started serving models on fractional H100 GPUs, select the [H100 MIG instance type](https://www.baseten.co/resources/changelog/fractional-nvidia-h100-gpus/) when deploying your model or [get in touch to discuss optimizing models](https://share.hsforms.com/1KA0AbEkrRayrwUSfFS1Eswd5zj5) with TensorRT to take full advantage of H100 MIG for model serving.
