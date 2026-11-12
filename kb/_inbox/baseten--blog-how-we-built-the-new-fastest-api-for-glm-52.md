---
title: How we built the new fastest API for GLM-5.2
kind: blog
topic: null
subtopic: null
secondary_topics: []
summary: null
triage: null
skip_reason: null
source: baseten
url: https://www.baseten.co/blog/how-we-built-the-new-fastest-api-for-glm-52
author: Alex Korte
published: '2026-07-25'
fetched: '2026-11-12T06:08:10Z'
classifier: null
taxonomy_rev: 2
words: 509
content_sha256: e65ed27f6860190515329f5b4a581aa1e0eb6b32bb0844f9e48f5cbe31457f55
---

# How we built the new fastest API for GLM-5.2

Model performance
# How we built the new fastest API for GLM-5.2

Baseten’s GLM-5.2 API shows state-of-the-art TTFT and TPS on both third-party benchmarks and real-world usage.


- Authors
- Date
- July 25, 2026

A month ago, GLM-5.2 was released. As part of our day-zero support, [we built the fastest API in the world for GLM-5.2](https://www.baseten.co/blog/how-we-built-the-worlds-fastest-api-for-glm-52/), with peak speeds of 280 tokens per second and average speeds around 100 tokens per second. Today, our GLM-5.2 [as benchmarked by Artificial Analysis](https://artificialanalysis.ai/models/glm-5-2/providers) shows more than double the performance of the launch-day API. We find that our improved API performance shows up in both benchmarks and real-world usage.

As models like GLM-5.2 demonstrate sustained popularity in the market, we deepen our investment in model-specific optimization work to unlock better latency and throughput for our users. In addition to improving our GLM-5.2 API, we built another API for the model: [GLM-5.2-Fast](https://www.baseten.co/library/glm-52-fast/).

Some performance work benefits both APIs. Over the past month, we have optimized the scheduler, slightly increasing throughput, as well as rolled out improved NVFP4 weights and an updated speculative decoding profile. We’ve also fixed bugs on both quality and performance in our inference engine and throughout the stack.

For the fast API, we focused on reducing latency for coding and agents. Inference engineering offers multiple opportunities to trade off along the pareto frontier between latency and throughput. Based on a strong signal from the market that there is willingness to pay for more performance, Baseten’s model performance team revisited configuration options across parallelism, batching, and caching to push the system as far toward latency as possible. There were two changes that made the largest impact:

- While the general API uses Attention Data Parallelism (ADP) to improve throughput, the fast API solely uses Tensor and Expert Parallelism with configs selected for latency.
- A substantial reduction in max batch size means fewer requests are competing for resources.

This fast API runs on the same NVIDIA B200 GPUs as the general API. However, because the performance optimizations trade off throughput to improve latency, input and output token prices are 50% higher on the fast API.

This performance work shows up in the latest benchmarks from Artificial Analysis, measured at approximately 7:00 PM Pacific Time on Saturday, July 25, 2026.

LLM performance varies substantially based on the amount of traffic in a system, the pattern of said traffic, and the input and output sequence lengths. We’ve received positive feedback from the market around our API’s leading performance in real-world usage, not just benchmarks. For reference, the Artificial Analysis benchmark sends prompts of approximately 10,000 input tokens to generate responses of approximately 1,000 output tokens.

We’re not done optimizing the performance of GLM-5.2. We have plans to roll out another improvement to our speculative decoding algorithm shortly. We’re also learning a lot from the process of building an API for Kimi K3, and we look forward to applying these learnings back to other open models like GLM-5.2.

The new fast API for GLM-5.2 is publicly available on Baseten. Try it today at [baseten.co/library/glm-52-fast/](https://www.baseten.co/library/glm-52-fast/).
