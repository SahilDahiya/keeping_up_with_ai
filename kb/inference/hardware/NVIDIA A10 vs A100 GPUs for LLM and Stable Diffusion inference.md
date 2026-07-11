---
title: NVIDIA A10 vs A100 GPUs for LLM and Stable Diffusion inference
topic: inference
subtopic: hardware
secondary_topics:
- infra-platform/cost
summary: Compares NVIDIA A10 and A100 GPUs for LLM and Stable Diffusion inference
  workloads.
source: baseten
url: https://www.baseten.co/blog/nvidia-a10-vs-a100-gpus-for-llm-and-stable-diffusion-inference/
author: Philip Kiely
published: '2023-09-15'
fetched: '2026-07-11T04:10:42Z'
classifier: codex
taxonomy_rev: 1
words: 1712
content_sha256: 773ff33cc7c531d2288d9923d3ce26f1ff504810a0529afd967f943a536c3601
triage: keep
skip_reason: null
---

# NVIDIA A10 vs A100 GPUs for LLM and Stable Diffusion inference

![A10 vs A100](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1747610169-a10-a100.png%3Fauto%3Dformat%26fit%3Dcrop%26h%3D630%26w%3D1200&w=3840&q=100)

When you’re deploying a new ML model, it can be hard to decide which GPU you need for inference. You want a GPU that is capable of running your model, but don’t want to overspend on a more powerful card than you need. This article compares two popular choices—NVIDIA’s A10 and A100 GPUs—for model inference and discusses the option of using multi-GPU instances for larger models. For smaller models, see our comparison of the [NVIDIA T4 vs NVIDIA A10 GPUs](https://www.baseten.co/blog/comparing-nvidia-gpus-for-ai-t4-vs-a10/).

NVIDIA’s A10 and A100 GPUs power all kinds of model inference workloads, from LLMs to audio transcription to image generation. The A10 is a cost-effective choice capable of running many recent models, while the A100 is an inference powerhouse for large models.

When picking between the A10 and A100 for your model inference tasks, consider your requirements for latency, throughput, and model size, as well as your budget. And you aren’t limited to just a single GPU. You can run models that are too big for one A100 by combining multiple A100s in a single instance, and you can save money on some large model inference tasks by splitting them over multiple A10s.

This guide will help you make the right tradeoff between inference time and cost when picking GPUs for your model inference workload.

## About Ampere GPUs

The “A” in A10 and A100 means that these GPUs are built on NVIDIA’s [Ampere microarchitecture](https://en.wikipedia.org/wiki/Ampere_(microarchitecture)).

Ampere, named for physicist André-Marie Ampère, is a microarchitecture by NVIDIA that succeeds their previous [Turing microarchitecture](https://en.wikipedia.org/wiki/Turing_(microarchitecture)). The Ampere microarchitecture was first released in 2020 and powers the [RTX 3000 series of consumer GPUs](https://en.wikipedia.org/wiki/GeForce_30_series), headlined by the GeForce RTX 3090 Ti.

But its impact is even greater in the datacenter. There are six datacenter GPUs based on Ampere:

- NVIDIA A2
- NVIDIA A10
- NVIDIA A16
- NVIDIA A30
- NVIDIA A40
- NVIDIA A100 (which comes in a 40 and 80 GiB version)

Of those GPUs, the A10 and A100 are most commonly used for model inference, along with the A10G, [an AWS-specific variant of the A10 that's interchangeable for most model inference tasks](https://www.baseten.co/blog/nvidia-a10-vs-a10g-for-ml-model-inference/). We’ll compare the standard A10 and the 80-gigabyte A100 in this article.

## A10 vs A100: Specs

Both GPUs have a long spec sheet, but a few key pieces of information let us understand the difference in performance between an A10 and A100 for ML inference.

The most important factor for ML inference, FP16 Tensor Core performance, shows the A100 as more than twice as capable as the A10, with 312 teraFLOPS (a teraFLOP is a trillion floating point operations per second). The A100 also has over three times the VRAM, which is essential for working with large models.

### Core count and core type

The A100’s elevated performance comes from its high [Tensor Core](https://www.nvidia.com/en-us/data-center/tensor-cores/) count.

[CUDA cores](https://developer.nvidia.com/cuda-faq#Hardware) are the standard cores in a GPU. The A10 actually has more CUDA cores than the A100, which corresponds to its higher base FP32 performance. But for ML inference, Tensor Cores are more important.

Ampere cards feature third-generation Tensor Cores. These cores specialize in matrix multiplication, which is one of the most computationally expensive parts of ML inference. The A100 has 50% more Tensor Cores than the A10, which gives it a major boost in model inference.

Ray tracing (RT) cores aren’t used for most ML inference tasks. They’re more often used for rendering-oriented workloads using engines like Blender, Unreal Engine, and Unity. The A100 is optimized for ML inference and other HPC tasks, so it doesn’t have any RT cores.

### VRAM and memory type

VRAM, or video random access memory, is the memory on board a GPU that it can use to store data for calculations. VRAM is often a bottleneck for model invocation; you need enough VRAM to load the model weights and handle inference.

The A10 has 24GiB of DDR6 VRAM. Meanwhile, the A100 comes in 2 versions: 40GiB and 80GiB. Both A100 versions use HBM2, a faster memory architecture than DDR6. The A100s have larger memory busses and more bandwidth than the A10s thanks to the HBM2 architecture. HBM2 is more expensive to produce, so it’s limited to these flagship GPUs.

Baseten offers A100s with 80GiB of VRAM as that’s more commonly needed for model inference.

## A10 vs A100: Performance

Specs look great, but how do they translate to real-world tasks? We benchmarked model inference for popular models like Llama 2 and [Stable Diffusion](https://www.baseten.co/library/stable-diffusion/) on both the A10 and A100 to see how they perform in actual use cases.

All models in these examples are running in float-16 (fp16). This is often called “half precision” and means that the GPUs are doing calculations on 16-bit floating point numbers, which saves substantial time and memory vs doing calculations in full precision (float-32).

### Llama 2 inference

Llama 2 is an open-source large language model by Meta that comes in 3 sizes: 7 billion, 13 billion, and 70 billion parameters. Larger sizes of the model yield better results, but require more VRAM to operate the model.

A good rule of thumb is that a large language model needs two gigabytes of VRAM for every billion parameters when running in fp16, plus some overhead for running inference and handling input and output. Thus, Llama 2 models have the following hardware requirements:

The A100 GPU lets you run larger models, and for models that exceed its 80-gigabyte VRAM capacity, you can use multiple GPUs in a single instance to run the model.

### Stable Diffusion inference

Stable Diffusion fits on both the A10 and A100 as the A10’s 24 GiB of VRAM is enough to run model inference. So if it fits on an A10, why would you want to run it on the more expensive A100?

The A100 isn’t just bigger, it’s also faster. After [optimizing Stable Diffusion inference](https://www.baseten.co/blog/sdxl-inference-in-under-2-seconds-the-ultimate-guide-to-stable-diffusion-optimiza/), the model runs about twice as fast on an A100 as on an A10.

![Inference time for 50 steps of Stable Diffusion: 1.77 seconds on the A10, 0.89 seconds on the A100](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1694809176-frame-1995.png%3Fauto%3Dformat%26w%3D1200&w=3840&q=75) Stable Diffusion inference: A10 vs A100

Stable Diffusion inference: A10 vs A100So if it’s absolutely essential that an image is generated as fast as possible, deploying on an A100 will give you the fastest inference time for individual requests.

## A10 vs A100: Price

While the A100 is bigger and faster than the A10, it’s also far more expensive to use. At $0.10240 per minute, Baseten’s A100 instance is five times as expensive as the cheapest A10-equipped instance (at $0.02012 per minute).

If faster inference time is absolutely critical, you can run smaller models like Stable Diffusion on an A100 to get quicker results. But the cost adds up fast. So if your main concern is throughput—the number of images created per unit of time, rather than the amount of time it takes to create each image—you’ll be better off scaling horizontally to multiple instances, each with an A10. With Baseten, you get autoscaling infrastructure with every model deployment to make this horizontal scaling automatic.

### Calculating model throughput

Let’s say you need a throughput of 1,000 images per minute from Stable Diffusion, but how many seconds each image takes to generate doesn’t matter as much. Making a lot of simplifying assumptions that wouldn’t be present in the real world — consistent traffic patterns, negligible network latency, etc — you’ll get about 34 images per minute from an A10 instance, meaning you’ll get your desired throughput with 30 instances at about $0.60/minute ($0.02012 per minute per instance times 30 instances).

Meanwhile on A100s, you’ll only need 15 instances making 67 images a minute, but with each instance costing 5 times as much, the total throughput costs about $1.54/minute ($0.10240 per minute per instance times 15 instances), or about 2.5 times as much.

![Cost of throughput for 1,000 Stable Diffusion images per minute: $0.60 per minute on the A10, $1.54 per minute on the A100](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1694809258-frame-1996.png%3Fauto%3Dformat%26w%3D1200&w=3840&q=75) Cost of throughput for Stable Diffusion: A10 vs A100

Cost of throughput for Stable Diffusion: A10 vs A100Unless the time to generate each image is critical, scaling horizontally with A10s can give you more cost-effective throughput than using A100s for many use cases.

Managing multiple replicas for model inference can be a big headache, so Baseten offers [autoscaling features](https://www.baseten.co/blog/model-autoscaling-features-on-baseten/) to make scaling up for throughput easy and maintenance-free.

## Multiple A10s vs one A100

A10s can also help you scale vertically, creating larger instances to run bigger models. Let’s say you want to run a model that’s too big to fit on an A10, such as [Llama-2-chat 13B](https://github.com/basetenlabs/truss-examples/tree/main/llama/llama-2-13b-chat). You have another option besides just spinning up an expensive A100-backed instance.

Instead, you have the option to run the model on a single instance with multiple A10s. Combined, 2 A10s have 48 GiB of VRAM, more than enough for the 13-billion-parameter model. And an instance with 2 A10s costs $0.05672 per minute, or just over half the cost of a single A100.

Of course, inference is still going to be faster on an A100. Using multiple A10s in an instance lets you run inference on larger models, but it doesn’t make inference any faster. The option to use multiple A10s instead of an A100 lets you trade off between speed and cost based on your use case and budget.

Baseten offers multi-GPU instances with up to 8 A10s or 8 A100s.

## Which GPU is right for you?

The A100 is no doubt a powerful card and the only choice for some ML inference tasks. But the A10, especially with multiple in a single instance, offer a cost-effective alternative for many workloads. Ultimately, the choice comes down to your needs and budget.

And if the A10 and A100 are both excessive for your use case, here’s a [breakdown of the A10 vs the smaller T4 GPU](https://www.baseten.co/blog/comparing-nvidia-gpus-for-ai-t4-vs-a10/), which can save you money vs the A10 on less-demanding inference tasks.

There's also the A10G, an AWS-specific variant of the A10. While the cards have different stats, [they're interchangeable for most model inference tasks](https://www.baseten.co/blog/nvidia-a10-vs-a10g-for-ml-model-inference/).

For cost estimates on different GPUs, check out [Baseten’s pricing page](https://www.baseten.co/pricing) and use our handy calculator to estimate monthly spend from pay-per-minute GPU pricing. And we’re always around at [support@baseten.co](mailto:support@baseten.co) to help you find the best hardware for your ML inference needs.
