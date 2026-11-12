---
title: Why GPU utilization matters for model inference
kind: blog
topic: inference
subtopic: optimization
secondary_topics: []
summary: Explains GPU utilization (compute, memory, bandwidth usage) as the key lever
  for serving cost, since higher utilization per GPU reduces the instance count needed
  for a given traffic level.
triage: null
skip_reason: null
source: baseten
url: https://www.baseten.co/blog/why-gpu-utilization-matters-for-model-inference
author: Marius Killinger
published: '2024-02-20'
fetched: '2026-11-12T06:11:54Z'
classifier: claude
taxonomy_rev: 2
words: 848
content_sha256: c9f642e7e02a23d461e1c5f0b398d1d4a324ba751fb0c5f175c5958093cda51a
---

# Why GPU utilization matters for model inference

Model performance
# Why GPU utilization matters for model inference

Save money on high-traffic model inference workloads by increasing GPU utilization to maximize performance per dollar for LLMs, SDXL, Whisper, and more.


- Authors
- Date
- February 20, 2024

TLDR

When you’re using GPUs for model inference, you want the most performance per dollar possible. Understanding utilization is key for this — a high GPU utilization means fewer GPUs are needed to serve high-traffic workloads. There are some levers you can use to improve utilization, like larger batch sizes and model engines optimized for serving. You can measure the impact of these changes in each model’s “Metrics” tab in your Baseten workspace.

GPU utilization is the measure of how much of a GPU’s resources are in use at any given time during a workload. When running ML models, we want to maximize GPU utilization to decrease the cost of serving high-traffic model endpoints. If you get more performance from each GPU, you’re able to serve the same traffic with fewer GPUs, saving on model hosting costs.

Imagine you’re at the office with your entire team — let’s say 12 people. You all need to get to an event across town, so you book some Ubers. If you pack in 4 people per car, you only need to call 3 cars. But if only 2 or 3 people get in each car, you’ll need more — potentially spending twice as much.

Just like this rideshare metaphor only makes sense with a large group of people, GPU utilization becomes important with higher-traffic workloads. When you’re serving so many requests to your model that you have to spin up additional instances to handle the load, you want to make sure that each instance that you’re paying for is doing as much work as possible.

There are three main stats to consider for GPU utilization:

- Compute usage: what percentage of the time is a GPU running a kernel vs sitting idle?
- Memory usage: what amount of the GPU’s VRAM is active during inference?
- Memory bandwidth usage: how much of the available bandwidth is being used to send data to the compute cores?

When we talk about improving GPU utilization for LLMs, we almost always mean increasing compute usage. This is because memory bandwidth is generally the bottleneck on inference speed and compute capacity might be left on the table. While overall VRAM capacity caps the model size and number of concurrent prompts, it’s generally not the usage number we’re trying to increase.

Some parts of running a model are compute bound, meaning that the bottleneck for performance is how fast the GPU can calculate values. One compute-bound process is the prefill phase of an LLM, where the model is processing the full prompt to create the first token of its response.

But [most parts of LLM inference are memory bound](https://www.baseten.co/blog/llm-transformer-inference-guide/). After the first token, the bulk of the generation process for LLMs is memory bound, meaning that the bandwidth on the GPU’s VRAM is the limiting factor in how quickly tokens (or images, transcriptions, audio files, etc) can be generated.

Given that most LLM inference is memory transfer bound, we look for strategies to increase compute utilization so that we can run more calculations per byte of memory accessed.

Generally, you increase GPU utilization by increasing batch sizes during inference. The batch size determines how many user inputs are processed concurrently in the LLM. A larger batch size lets a model use more compute resources even when memory bound. Every model weight read from VRAM is applied to more outputs at once, increasing the amount of compute you can use per byte of bandwidth.

Increasing batch size increases throughput, which is the measure of how many requests a GPU instance can handle per second. However, increasing throughput generally makes latency worse, meaning users have to wait longer to get model output. It’s important to manage this tradeoff when trying to maximize utilization.

Once you have high utilization across multiple instances, it’s worth considering a switch to a more powerful GPU type. For example, [switching from A100 to H100](https://www.baseten.co/blog/unlocking-the-full-power-of-nvidia-h100-gpus-for-ml-inference-with-tensorrt/) can save 20-45% on workloads with high utilization and enough traffic to require multiple A100 GPUs.

To extend our rideshare metaphor, switching to H100 is like getting Uber XL rides for your group of 12 — at 6 passengers to a car, you only need two cars, saving more money even if XL rides are slightly more expensive.

In your Baseten workspace, you can see the GPU utilization across compute and VRAM capacity (not bandwidth) for each deployed model. These charts align by timestamp with charts for traffic and autoscaling, so you can see exactly how real-world usage affects utilization.

As you adjust model optimizations and batch sizing, use these metrics to see the impact of each change on GPU utilization.

To learn more about maximizing your performance on GPUs, check out:

- Docs on setting concurrency for your model server.
- Guides to performance metrics for [LLMs](https://www.baseten.co/blog/understanding-performance-benchmarks-for-llm-inference/) and [image generation models](https://www.baseten.co/blog/how-to-benchmark-image-generation-models-like-stable-diffusion-xl/).
- Benchmarks for [optimizing H100 performance with TensorRT](https://www.baseten.co/blog/unlocking-the-full-power-of-nvidia-h100-gpus-for-ml-inference-with-tensorrt/).
