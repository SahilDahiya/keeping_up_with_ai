---
title: Continuous vs dynamic batching for AI inference
topic: inference
subtopic: optimization
secondary_topics:
- inference/serving
summary: Compares continuous and dynamic batching for inference serving and their
  latency-throughput tradeoffs.
source: baseten
url: https://www.baseten.co/blog/continuous-vs-dynamic-batching-for-ai-inference/
author: Matt Howard; Philip Kiely
published: '2024-04-05'
fetched: '2026-07-11T04:09:47Z'
classifier: codex
taxonomy_rev: 1
words: 1499
content_sha256: 8f02cef1cf96a59fddea92892299abbd220b943ac9257c1f6cf12e49fe30c792
triage: keep
skip_reason: null
---

# Continuous vs dynamic batching for AI inference

![Continuous vs Dynamic batching](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1747527053-continue-vs-dynamic.png%3Fauto%3Dformat%26fit%3Dcrop%26h%3D630%26w%3D1200&w=3840&q=100)

When using AI models in production, batching makes good use of GPU resources by processing multiple requests to a model simultaneously. But different methods for batching are appropriate in different cases. To maximize throughput of AI inference, use continuous batching for most LLM deployments and dynamic batching for most other models.

Batch inference is essential for serving LLMs and other generative models in production. If you only run one request at a time through a GPU, most of its capacity is sitting idle. Running multiple inputs through the model simultaneously uses more of the GPU’s resources to massively increase the throughput of your model deployment. However, it’s important to choose the right strategy for batch inference to make sure your model still performs well on other important metrics like latency.

There are four ways inference requests can be batched on a GPU:

- No batching: each request is processed one at a time.
- Static batching: requests are placed in batches that are run when full.
- Dynamic batching: requests are placed in batches as they’re received and batches run once full or once enough time has elapsed since the first request.
- Continuous batching: requests are processed token-by-token, with new requests getting processed as older requests finish and free up space on the GPU.

Batching method depends on model architecture and modality. In production, you’ll generally want continuous batching for LLMs and dynamic batching for most other generative models.

In this article, we’ll examine the different methods for batching inference requests to AI models and the suitable uses for each approach. We’ll limit our discussion to batch inference on the GPU itself (there are other [opportunities to add concurrency](https://docs.baseten.co/performance/concurrency) in an end-to-end system) with a goal of maximizing the utilization of GPU resources.

## Naive implementation for basic testing

The most naive implementation of any model server has no batching. Every request is processed individually in the order that it’s received.

If you spin up a quick service with, say, FastAPI and PyTorch, you won’t get batching out of the box. That’s fine for basic development and testing, but wastes valuable GPU resources in production.

Without batching, most of the GPU capacity on the model serving instance is idle. Imagine a road full of cars where every car has only its driver, no passengers. Most cars can fit at least four people, so a lot of capacity is going unused. This is exactly what’s happening on your GPU.

## Static batching for scheduled load

Static batching is the simplest method for batching requests. But it can increase latency substantially, limiting its use cases.

When running inference on an LLM, or many other ML models, your bottleneck is the memory bandwidth used to load model weights. Model weights are much bigger than the activations (which are the "state" of a request mid-processing), so when loading a single layer of weights into the GPU's cache, you want to share that cost across processing many independent sets of activations. This gets you much better throughput than loading one layer of weights and computing it on one activation at a time.

If running each request individually is like everyone driving their own car, batching is like a bus. If the bus operates on static batching, the driver waits for the bus to fill entirely, then drives off to the destination. This ensures that the bus is full every time it goes through its route. Similarly, static batching for model inference waits until a set number of requests has been received, then runs a single batch to process the requests simultaneously.

Static batching is most appropriate when latency isn’t an issue, like processing a huge corpus of documents on a daily cadence. Static batching pushes the complexity of orchestrating requests elsewhere in the system. Using static batching requires a well-managed queue of requests to feed the model and a method for accepting model output in large chunks.

## Dynamic batching for AI inference in production

Static batching works well for daily jobs or behind-the-scenes processing. But for latency-sensitive production deployments, like generating images in response to user input, static batching won’t cut it.

Returning to our bus analogy, imagine being the first person getting on the bus on a slow day. If you have to wait for the entire bus to fill up before you leave, you’ll be waiting a long time. But what if the driver started a timer when the first passenger got on the bus, and left when the bus was full or the timer ran out, whichever happens first. This way, you’re guaranteed to only wait a few minutes maximum.

Dynamic batching works the same way. You set up dynamic batching with:

- A preset maximum batch size, which you hope to reach before kicking off each run.
- A window to wait after receiving the first request before running a partial batch.

In the diagram below, we can see how dynamic batching results in shorter wait times when there is less traffic.

![Dynamic batching runs batches once full or once a maximum time has elapsed, improving latency versus static batching while maintaining throughput in high-traffic periods.](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1712337076-frame-2030.png%3Fauto%3Dformat%26w%3D1200&w=3840&q=75) Dynamic batching runs batches once full or once a maximum time has elapsed, improving latency versus static batching while maintaining throughput in high-traffic periods.

Dynamic batching runs batches once full or once a maximum time has elapsed, improving latency versus static batching while maintaining throughput in high-traffic periods.Let’s say you set up your model server with a batch size of 16 requests and a window of 100 milliseconds. When the server receives its first request, it will:

- Receive 15 more requests in under 100 milliseconds and immediately run a full batch, or
- Receive fewer than 15 requests and run a partial batch once 100 milliseconds passes.

Dynamic batching is great for live traffic on models like [Stable Diffusion XL](https://www.baseten.co/library/stable-diffusion-xl/), where each inference request takes about the same amount of time. The right settings for your specific deployment depend on traffic patterns and latency requirements, but dynamic batching gives you flexibility across a wide range of options.

## Continuous batching for LLM inference in production

While dynamic batching is great for modalities like image generation where each output takes about the same amount of time to create, we can do even better for LLMs with continuous batching.

LLMs create a sequence of tokens as output. These output sequences will vary in length – the model could be answering a simple question or performing a detailed analysis with step-by-step reasoning. If you use a dynamic batching approach, each batch of requests is going to need to wait for the longest output to finish before the next batch can begin. This leaves GPU resources idle.

Continuous batching works at the token level rather than at the request level. The bottleneck in [AI inference](https://www.baseten.co/blog/ai-inference-explained/) is loading model weights. So for continuous batching, the model server loads each layer of the model sequentially and applies it to the next token of each request. In continuous batching, the same model weights could be used to generate the fifth token of one response and the eighty-fifth token of another.

In the bus example, continuous batching is similar to how bus routes work in the real world. As the driver goes through the route, passengers ride the bus for different amounts of time. When one passenger reaches their destination, that opens up a seat for a new passenger.

![Continuous batching improves GPU utilization over dynamic batching by eliminating the idle time waiting for the longest response of each batch to finish.](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1712337158-frame-2029.png%3Fauto%3Dformat%26w%3D1200&w=3840&q=75) Continuous batching improves GPU utilization over dynamic batching by eliminating the idle time waiting for the longest response of each batch to finish.

Continuous batching improves GPU utilization over dynamic batching by eliminating the idle time waiting for the longest response of each batch to finish.One complication with continuous batching is that it takes a lot longer to generate the first token of a response than each subsequent token. This relies on a process called prefill, which is actually compute bound. But over the course of an entire request, next token prediction is the most expensive part, so it’s the part we focus on optimizing with continuous batching.

Like with dynamic batching, you need to configure continuous batching based on your anticipated traffic patterns. You need to specify:

- Maximum batch size: how many requests the model can process at once.
- Anticipated sequence shapes: how many tokens the input and output sequences are expected to contain.

Continuous batching is implemented at the inference server layer. Model servers like TGI and VLLM offer continuous batching, while TensorRT-LLM uses “in-flight batching” to essentially the same effect.

Thanks to continuous batching, you can massively increase the throughput of your LLM deployments while still hitting ambitious latency targets. Read more about the tradeoffs between batch size and latency in our [guide to LLM benchmarking](https://www.baseten.co/blog/understanding-performance-benchmarks-for-llm-inference/), or see a concrete example in our [benchmarking results for Mistral 7B](https://www.baseten.co/blog/benchmarking-fast-mistral-7b-inference/).
