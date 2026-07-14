---
title: How we built the world’s fastest API for GLM-5.2
topic: inference
subtopic: optimization
secondary_topics: []
summary: Engineering writeup on building a high-speed GLM-5.2 API.
source: baseten
url: https://www.baseten.co/blog/how-we-built-the-worlds-fastest-api-for-glm-52/
author: Alex Korte; Magdy Saleh; Tri Dao; Anant Desai; Bryce Dubayah; Abu Qader; Philip
  Kiely
published: '2026-06-23'
fetched: '2026-07-11T04:05:01Z'
classifier: codex
taxonomy_rev: 1
words: 1639
content_sha256: 4f6a8dbc67c4b1fcbcc05e1a270b7db3ddbf88d798f058e584382b66989104f8
triage: keep
skip_reason: null
---

# How we built the world’s fastest API for GLM-5.2

![GLM-5.2 at 280+ TPS](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1782168463-glm-52.png%3Fauto%3Dformat%26fit%3Dcrop%26h%3D630%26w%3D1200&w=3840&q=100)

We built the world’s fastest API for GLM-5.2, achieving over 280 TPS as measured by Artificial Analysis. This leading performance is thanks to a suite of performance optimizations across the Baseten Inference Stack, including our optimized runtime engine, NVFP4 on NVIDIA Blackwell, KV-aware routing and PD disaggregation with NVIDIA Dynamo, and Multi-Token Prediction heads for speculation.

[GLM-5.2](https://www.baseten.co/library/glm-52/) is the biggest news in open models since DeepSeek-R1.

![Tech leaders are embracing GLM-5.2 as a new high water mark of frontier intelligence on open models](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1782168800-tweets_blog-1.png%3Fauto%3Dformat%26w%3D1200&w=3840&q=75) Tech leaders are embracing GLM-5.2 as a new high water mark of frontier intelligence on open models

Tech leaders are embracing GLM-5.2 as a new high water mark of frontier intelligence on open modelsIt’s easy to see why. GLM-5.2 delivers comparable performance to GPT 5.5 and Opus 4.8 at a fraction of the cost, generally 70-80% less expensive on a pure token basis (use our [calculator to estimate savings for your workload](https://www.baseten.co/resources/calculator/)).

But a model has to be more than just smart and inexpensive. To be useful in production, a model needs to be fast, reliable, and available at scale. Delivering on the promise of frontier open intelligence requires exceptional inference.

Accordingly, we built the world’s fastest API for GLM-5.2, currently serving over 280 tokens per second as measured by Artificial Analysis.

![GLM-5.2 runs at SOTA speeds on Baseten model APIs, measured by Artificial Analysis June 22, 2026](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1782172027-image-72.png%3Fauto%3Dformat%26w%3D1200&w=3840&q=75) GLM-5.2 runs at SOTA speeds on Baseten model APIs, measured by Artificial Analysis June 22, 2026

GLM-5.2 runs at SOTA speeds on Baseten model APIs, measured by Artificial Analysis June 22, 2026We achieved this performance by leveraging a number of techniques across the entire inference process by:

- Updating our custom inference engine to implement shared DSA for the GLM-5.2 architecture.
- Running and calibrating an in-house NVFP4 quantization from the original FP8 weights that demonstrates equivalent quality on agentic benchmarks like BFCL.
- Ensuring high KV cache hit rates via KV-aware routing built with NVIDIA Dynamo tools for lower prefill burden and improved TTFT on requests with repeated prefixes.
- Achieving a 2x higher TPS for observed workload shapes by running disaggregated inference built with the NVIDIA Dynamo toolkit.
- Improving TPS further via speculation by implementing support for GLM-5.2 Multi-Token Prediction heads.

You can experience this performance for yourself with [GLM-5.2 on Baseten Model APIs](https://www.baseten.co/library/glm-52/). We also have GLM-5.2 available as a dedicated deployment for high-volume workloads.

![Notion offers GLM-5.2 via Baseten](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1782169196-image8.png%3Fauto%3Dformat%26w%3D1200&w=3840&q=75) Notion offers GLM-5.2 via Baseten

Notion offers GLM-5.2 via Baseten## GLM-5.2 Overview

[GLM-5.2 by Z.ai](https://z.ai/blog/glm-5.2) is a 744B parameter frontier LLM that excels at agentic tasks (especially coding) and supports up to a 1 million token context window. It uses a similar architecture to its predecessor, GLM-5.1: mixture of experts (40B active parameters), non-thinking and thinking modes, and a fully open MIT license. While GLM-5.2 shares a lot in common with GLM-5.1, it now uses shared DSA weights, which we implemented support for in our customized runtime engine.

![GLM-5.2 offers frontier performance across tasks. Image from Z AI.](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1782169236-20260617-012836.webp%3Fauto%3Dformat%26w%3D1200&w=3840&q=75) GLM-5.2 offers frontier performance across tasks. Image from Z AI.

GLM-5.2 offers frontier performance across tasks. Image from Z AI.GLM-5.2 has great benchmark scores, but by now AI builders know that there is more to a model’s utility than its performance on standard evals. In practice, GLM-5.2 meets or exceeds the capabilities suggested by its benchmarks. It's a genuinely great model for writing code, operating agents, and other frontier language model tasks.

## High-quality NVFP4 quantization for Blackwell GPUs

We run our model APIs on NVIDIA Blackwell GPUs with a customized inference engine within the [Baseten Inference Stack](https://www.baseten.co/resources/guide/the-baseten-inference-stack/). The selected runtime uses NVFP4 weights for maximum performance. From the original FP8 weights, we performed an in-house quantization to NVFP4 using NVIDIA ModelOpt. NVFP4 is a 4-bit floating point data format by NVIDIA that uses dual scale factors to retain high dynamic range and preserve model quality.

In our calibration and testing of the quantized model, we focused on ensuring that GLM-5.2 performs faithfully on common patterns for agents. On the BFCL function calling benchmark, we observed roughly equivalent performance between the native FP8 weights and our NVFP4 quantization, with scores across runs within the margin of error for the benchmark.

NVFP4 quantization improves performance on both time to first token and tokens per second by unlocking faster tensor cores and reducing burden on VRAM bandwidth.

![Performance is excellent across both TTFT and TPS, measured by Artificial Analysis June 22, 2026](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1782172161-image-74.png%3Fauto%3Dformat%26w%3D1200&w=3840&q=75) Performance is excellent across both TTFT and TPS, measured by Artificial Analysis June 22, 2026

Performance is excellent across both TTFT and TPS, measured by Artificial Analysis June 22, 2026## Cache-aware routing with NVIDIA Dynamo

GLM-5.2 is particularly well suited for long context requests and complex agentic tasks. These workloads generally have very long input sequences. By re-using KV cache between requests, we can skip expensive prefill for shared sequences.

We generally talk about KV cache re-use in the context of time to first token (TTFT). However, reasoning models like GLM-5.2 generally care more about time to first answer token (TTFAT), which combines TTFT with some TPS for the reasoning sequence.

![Time to First Answer Token for GLM-5.2, measured by Artificial Analysis June 22, 2026](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1782172207-image-73.png%3Fauto%3Dformat%26w%3D1200&w=3840&q=75) Time to First Answer Token for GLM-5.2, measured by Artificial Analysis June 22, 2026

Time to First Answer Token for GLM-5.2, measured by Artificial Analysis June 22, 2026This chart shows that of the 7.9 second average to generate the first answer token, 7.1 of those seconds were spent generating reasoning tokens versus only 0.8 seconds spent processing the input sequence.

Still, bringing the TTFT down to 800 ms is important for the overall responsiveness and throughput of the system. In large-scale production deployments, KV cache is split across various independent replicas. We use tools from NVIDIA Dynamo to route incoming requests.

![Description: KV-aware routing sends requests to replicas that already have relevant context cached, saving time by avoiding redundant prefill computation.](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1763057468-kvroutingchart.png%3Fauto%3Dformat%26w%3D1200&w=3840&q=75) KV-aware routing sends requests to replicas that already have relevant context cached, saving time by avoiding redundant prefill computation.

KV-aware routing sends requests to replicas that already have relevant context cached, saving time by avoiding redundant prefill computation.Exact cache hit rates on a multi-tenant API depend on the exact traffic profile at any given time. Thus far, we’re observing high hit rates across fairly heterogeneous traffic, which reduces load on prefill and improves end-to-end performance.

## Prefill-decode disaggregation with NVIDIA Dynamo

One of the highest-impact optimizations we made to our performance is disaggregating prefill and decode for GLM-5.2.

There are two distinct phases of LLM inference:

- **Prefill:**The compute-bound process that processes the input sequence, builds the KV cache, and generates the first output token. Prefill performance determines TTFT.
- **Decode:**The memory-bound process of generating subsequent output tokens. Decode performance determines TPS.

Traditionally, a single GPU node handles both prefill and decode. With disaggregation, these workloads are run on separate engines. This provides several benefits:

- Prefill and decode run independently without competing for resources
- We can allocate unequal resources between prefill and decode as needed (generally, we provision more prefill engines than decode engines)
- The inference engines running prefill and decode can run with different configurations optimized for the demands of their specific piece of the inference pipeline.

KV cache is still re-used whenever possible, meaning that prefill workers are only used to process novel input sequences.

![Disaggregated inference uses separate prefill and decode workers](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1782169626-disaggregation.png%3Fauto%3Dformat%26w%3D1200&w=3840&q=75) Disaggregated inference uses separate prefill and decode workers

Disaggregated inference uses separate prefill and decode workersMuch of the challenge in implementing PD disaggregation is in reliable, low-overhead communication between and orchestration of the prefill and decode engines. NVIDIA Dynamo provides a developer toolkit for implementing essential components of disaggregation:

- A prefill queue to hold requests when all prefill engines are saturated.
- Robust support for conditional disaggregation, with prefill routing based on configurable thresholds for input sequence lengths after prefix cache and prefill queue size.
- Efficient NIXL-based KV transfer from prefill to decode engines with a kernel to transpose KV blocks between layouts when the engines have different TP configurations.

In head-to-head benchmarks between aggregated and disaggregated deployments of GLM-5.2, we observed 2x higher tokens per second on disaggregated inference.

## Higher TPS with Multi-Token Prediction

GLM-5.2 shipped with an improved Multi-Token Prediction (MTP) layer that reduces the cost of generating draft tokens and increases the acceptance rate of these tokens.

As a review, MTP is one of several methods for speculation. Speculation is the process of generating more than one token per forward pass through the model with the goal of improving TPS. Thanks to the verification step in all algorithms, speculation methods are lossless performance optimizations.

Using these MTP layers to generate draft tokens, we tested a variety of sequence lengths to find the right balance between generating long sequences and maintaining high acceptance rates. We’ve done [a lot of work on MTP over the last few months](https://www.baseten.co/blog/boosting-mtp-acceptance-rates-in-baseten-speculation-engine/), and there is still headroom to unlock in the speculation we’re using for GLM-5.2.

## Running GLM-5.2 in production

The natural question when looking at these kinds of benchmark results is whether or not the same performance can actually be maintained in production.

In fact, not only can we deliver this performance in production, but we can achieve even better workload-specific performance for large-scale dedicated deployments of GLM-5.2. Levers include:

- Using task-specific speculators trained on input and output sequences representative of expected production data.
- Achieving more consistent cache hits from single-tenant traffic.
- Tuning disaggregation configuration to match the ratio of prefill and decode engines to traffic profile.
- Configuring parallelism and batching settings to achieve desired tradeoff between latency and throughput.

[Get in touch with our team](https://www.baseten.co/talk-to-us/) for dedicated deployments of GLM-5.2, or get started testing the model today with our [model API](https://www.baseten.co/library/glm-52/).
