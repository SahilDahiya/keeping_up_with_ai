---
title: How we built the new fastest API for GLM-5.2
kind: blog
topic: inference
subtopic: optimization
secondary_topics: []
summary: Baseten details how it doubled GLM-5.2 API throughput to 601 tok/s (per Artificial
  Analysis) by launching a separate low-latency "fast" API that swaps Attention Data
  Parallelism for Tensor and Expert Parallelism and sharply cuts max batch size, alongside
  scheduler tuning, NVFP4 weights, and an updated speculative-decoding profile on
  the same NVIDIA B200 GPUs.
triage: null
skip_reason: null
source: baseten
url: https://www.baseten.co/blog/how-we-built-the-new-fastest-api-for-glm-52/
author: Alex Korte; Magdy Saleh; Tri Dao; Anant Desai; Bryce Dubayah; Abu Qader; Philip
  Kiely
published: '2026-07-26'
fetched: '2026-07-26T06:54:10Z'
classifier: claude
taxonomy_rev: 2
words: 588
content_sha256: 8a40198857c9a2b337fd99baac696466479b577862823e17ef6ed1c44401d67b
---

# How we built the new fastest API for GLM-5.2

![Baseten’s GLM-5.2 API is benchmarked at 601 tokens per second on Artificial Analysis, higher than any competing API](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1785033897-newblogheaderglm52.png%3Fauto%3Dformat%26fit%3Dcrop%26h%3D630%26w%3D1200&w=3840&q=100)

A month ago, GLM-5.2 was released. As part of our day-zero support, [we built the fastest API in the world for GLM-5.2](https://www.baseten.co/blog/how-we-built-the-worlds-fastest-api-for-glm-52/), with peak speeds of 280 tokens per second and average speeds around 100 tokens per second. Today, our GLM-5.2 [as benchmarked by Artificial Analysis](https://artificialanalysis.ai/models/glm-5-2/providers) shows more than double the performance of the launch-day API. We find that our improved API performance shows up in both benchmarks and real-world usage.

![Baseten’s GLM-5.2 API achieves leading performance across both TTFT and TPS](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1785033914-artificialanalysis-ai_models_glm-5-2_providers-5.png%3Fauto%3Dformat%26w%3D1200&w=3840&q=75) Baseten’s GLM-5.2 API achieves leading performance across both TTFT and TPS

Baseten’s GLM-5.2 API achieves leading performance across both TTFT and TPSAs models like GLM-5.2 demonstrate sustained popularity in the market, we deepen our investment in model-specific optimization work to unlock better latency and throughput for our users. In addition to improving our GLM-5.2 API, we built another API for the model: [GLM-5.2-Fast](https://www.baseten.co/library/glm-52-fast/).

Some performance work benefits both APIs. Over the past month, we have optimized the scheduler, slightly increasing throughput, as well as rolled out improved NVFP4 weights and an updated speculative decoding profile. We’ve also fixed bugs on both quality and performance in our inference engine and throughout the stack.

For the fast API, we focused on reducing latency for coding and agents. Inference engineering offers multiple opportunities to trade off along the pareto frontier between latency and throughput. Based on a strong signal from the market that there is willingness to pay for more performance, Baseten’s model performance team revisited configuration options across parallelism, batching, and caching to push the system as far toward latency as possible. There were two changes that made the largest impact:

- While the general API uses Attention Data Parallelism (ADP) to improve throughput, the fast API solely uses Tensor and Expert Parallelism with configs selected for latency. 
- A substantial reduction in max batch size means fewer requests are competing for resources. 

This fast API runs on the same NVIDIA B200 GPUs as the general API. However, because the performance optimizations trade off throughput to improve latency, input and output token prices are 50% higher on the fast API.

This performance work shows up in the latest benchmarks from Artificial Analysis, measured at approximately 7:00 PM Pacific Time on Saturday, July 25, 2026.

![Baseten’s Model API achieves the fastest end-to-end response time in the industry](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1785033969-artificialanalysis-ai_models_glm-5-2_providers-3.png%3Fauto%3Dformat%26w%3D1200&w=3840&q=75) Baseten’s Model API achieves the fastest end-to-end response time in the industry

Baseten’s Model API achieves the fastest end-to-end response time in the industry![On pure output speed, Baseten’s GLM-5.2 API achieves SOTA speeds](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1785034000-image1.png%3Fauto%3Dformat%26w%3D1200&w=3840&q=75) On pure output speed, Baseten’s GLM-5.2 API achieves SOTA speeds

On pure output speed, Baseten’s GLM-5.2 API achieves SOTA speedsLLM performance varies substantially based on the amount of traffic in a system, the pattern of said traffic, and the input and output sequence lengths. We’ve received positive feedback from the market around our API’s leading performance in real-world usage, not just benchmarks. For reference, the Artificial Analysis benchmark sends prompts of approximately 10,000 input tokens to generate responses of approximately 1,000 output tokens.

We’re not done optimizing the performance of GLM-5.2. We have plans to roll out another improvement to our speculative decoding algorithm shortly. We’re also learning a lot from the process of building an API for Kimi K3, and we look forward to applying these learnings back to other open models like GLM-5.2.

The new fast API for GLM-5.2 is publicly available on Baseten. Try it today at [baseten.co/library/glm-52-fast/](https://www.baseten.co/library/glm-52-fast/).
