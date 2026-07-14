---
title: How to benchmark image generation models like Stable Diffusion XL
topic: evals-observability
subtopic: benchmark-design
secondary_topics:
- models/multimodal
summary: Explains how to benchmark image-generation models with attention to quality,
  latency, and reproducibility.
source: baseten
url: https://www.baseten.co/blog/how-to-benchmark-image-generation-models-like-stable-diffusion-xl/
author: Philip Kiely
published: '2024-01-31'
fetched: '2026-07-11T04:10:15Z'
classifier: codex
taxonomy_rev: 1
words: 1395
content_sha256: 9d24cfbe0aa435916f7c8f579caa28fdc9e54b6c93c28d996b7929f1213b1fcd
triage: keep
skip_reason: null
---

# How to benchmark image generation models like Stable Diffusion XL

![Benchmarking SDXL](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1747529546-bench-sdxl.png%3Fauto%3Dformat%26fit%3Dcrop%26h%3D630%26w%3D1200&w=3840&q=100)

Before using a model like Stable Diffusion XL to generate images in your application, you’ll want to see some performance benchmarks to get key information about how fast your model can create images, how many images it can create at that speed, and how much it costs to operate. In this post, we’ll cover how to set up a benchmark that gives you the information you need on model performance.

Text-to-image models like [Stable Diffusion XL (SDXL)](https://www.baseten.co/library/stable-diffusion-xl/) generate detailed, accurate images from simple text prompts. When you integrate SDXL into an end-user application, you’ll have performance requirements for model inference.

However, there’s no one number for SDXL inference that gives you everything you need to know. Instead, performance benchmarking is about measuring the tradeoffs between latency, throughput, and cost.

Figuring out the right performance metrics to use for SDXL is like figuring out the fastest way to get from one place to another — simple, once you’ve built in enough constraints. Asking “what’s the fastest way to get to the Empire State Building” depends on any number of factors. But once you know the full situation, you can say that the fastest way for two people to get from the Central Park Zoo to the Empire State Building is a taxi down fifth, or the fastest way for fifty people to get there from Brooklyn is by taking the subway.

“Asking the right question is half the answer” — usually attributed to Aristotle — definitely applies here. If you want to benchmark SDXL performance, figuring out the exact configuration that matches your real-world requirements sets you up for success.

## Standardizing your benchmark

There are a lot of factors that determine how long it takes for SDXL to create an image. The first step to running a real performance benchmark is figuring out exactly what configuration best represents the real-world use that you’re testing for.

### Hardware and model serving engine

When you sit down to create a benchmark, you probably have a couple of headline factors in mind:

- GPU — choice of hardware has a massive impact on performance and cost.
- Model server — optimized implementations using tools like TensorRT-LLM can deliver big performance boosts in some cases.

But in addition to these explicit variables, there are plenty of other considerations for getting a relevant and accurate benchmark.

### Model configuration

The first step is determining the exact specifications of the model that you want to get performance metrics for, including:

- Version, variant and size — performance varies across different models, so make sure you know exactly which “Stable Diffusion” you’re running.
- Specialized implementation — a model like SDXL Turbo is massively faster than ordinary SDXL but doesn’t always generate the highest-quality images.
- Image generation pipeline — are you just taking a prompt and making an image, or do you have an entire pipeline including steps like a ControlNet?

### Input and output

Equally important is determining exactly what you want to do with the model: what inputs are you providing, and what outputs are you expecting? For Stable Diffusion models, there are three settings to watch:

- Number of inference steps — this is the main factor in how long the image generation process takes. More inference steps means a more detailed picture but a longer run time.
- Image resolution and aspect ratio — it’s faster to generate a 512x512 pixel image than a full-resolution 1024x1024 picture.
- Prompt — perhaps surprisingly, the impact of different prompts on generation time should be negligible as long as the prompt is under SDXL’s 75-token (~300-character) limit.

Inference step count and image resolution are two primary drivers of image generation time. Where you draw the line depends on your use case — 20 or 30 steps are fine where speed matters more, 50 or more steps help when quality is the main objective.

![SDXL image quality at different inference step counts](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1705955599-sdxl-5.png%3Fauto%3Dformat%26w%3D1200&w=3840&q=75)

### Concurrency and network

When you run your model on real production infrastructure, there are even more factors that affect performance, but also additional levers you can use to improve it. Make sure you account for:

- Concurrency settings and batch size — how many images are you generating at once?
- End-to-end latency versus inference time — to what extent do you want to include variables like network speed in your measurements?
- Cold start times — do you need to measure performance on both warm and cold nodes?
- Methodology — are you measuring across averages (mean, median) or worst case scenarios like p99?

Combined, answering these questions seems like a lot of work to set up a benchmark. But this up-front effort pays off by making sure that you’re only looking at performance numbers that actually match what you’ll experience in production.

## Picking performance metrics

Once you know exactly what you’re measuring, it’s time to figure out how to measure it. Performance benchmarking generally comes down to some combination of latency, throughput, and cost.

### Measuring latency

Latency is the amount of time from receiving a prompt to generating an image. Latency makes the application feel fast to a single user.

Your metric for latency is **total generation time** on a per-image basis. Depending on how you configure your benchmark, this may be an end-to-end time including network overhead, or just a measure of the time model inference takes within the container.

Reducing the number of inference steps is the main way to speed up image generation and reduce latency. However, this can reduce the accuracy and detail of the output images. You can also sacrifice quality for latency by reducing the image resolution that you generate.

However, there are certain optimizations that have a minor impact on output quality while delivering big improvements on image generation speed. Here is some of our [work on optimizing SDXL inference](https://www.baseten.co/blog/40-faster-stable-diffusion-xl-inference-with-nvidia-tensorrt/).

### Measuring throughput

Throughput is the number of images you can generate in a given amount of time. Throughput makes the application stay fast as you get a large number of users.

For SDXL, you’re looking at **images per minute** (or requests per minute) on a single GPU or across your entire deployment with multiple replicas.

If each individual image is created faster, that does increase throughput. But bigger throughput gains come from batching and concurrency. By creating several images at the same time, you’re using more of a GPU’s resources, increasing the number of images you’re able to create in total. However, this often comes at the expense of latency as each individual request has added overhead from the batching process.

### Measuring cost

Cost is pretty self-explanatory: it’s the price of operating the model for your application. Keeping costs under control is critical as you scale.

The main metric for SDXL is **cost per image**. Multiply that by how many images you need per day, and you have a good sense of the overall cost of operating the model for your application. It isn’t a perfect equation because cold start times and idle times affect spend, but it’s a strong estimate especially if traffic patterns are relatively stable.

On a given GPU, increasing throughput decreases cost per image until the GPU is fully utilized. As GPU resources are billed by the minute, if you can get more images out of the same GPU, the cost of each image goes down. So if your latency is better than needed and you want to save on cost, try increasing concurrency to improve throughput and save money.

## Defining your Stable Diffusion benchmark

Defining a performance benchmark takes more than picking a GPU type and model serving framework. You need to carefully specify factors from image resolution and inference steps to concurrency and network overhead.

But once these variables are determined, your performance benchmarks can help you make informed tradeoffs between latency, throughput, and cost. If you aren’t satisfied with performance across these axes, revisit your configuration to see where there’s flexibility. We’ve written about [getting SDXL generation below 2 seconds on an A100](https://www.baseten.co/blog/sdxl-inference-in-under-2-seconds-the-ultimate-guide-to-stable-diffusion-optimiza/) and [even faster inference with TensorRT on an H100 GPU](https://www.baseten.co/blog/40-faster-stable-diffusion-xl-inference-with-nvidia-tensorrt/) — the approaches used in these articles are great for improving image generation time. 

If you’re looking to maximize performance for Stable Diffusion XL or any ML model for any combination of latency, throughput, and cost, we’re here to help at [support@baseten.co](mailto:support@baseten.co).
