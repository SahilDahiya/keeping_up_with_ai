---
title: 'Open Model Inference Speed: Artificial Analysis Benchmarks | Fireworks'
kind: blog
topic: null
subtopic: null
secondary_topics: []
summary: null
triage: null
skip_reason: null
source: fireworks
url: https://fireworks.ai/blog/open-model-inference-speed-benchmarks
author: null
published: '2026-01-27'
fetched: '2026-10-23T06:11:15Z'
classifier: null
taxonomy_rev: 2
words: 325
content_sha256: f0cfd7734c4577e47f9e951eb8b7feb1a4f8c24c1009ce8216385f8065ac59ec
---

# Open Model Inference Speed: Artificial Analysis Benchmarks | Fireworks

[Kimi K2.5](https://fireworks.ai/blog/kimi-k2p5) just dropped yesterday and is available Day 0 on Fireworks! As open models get more powerful and agentic, low latency enables complex, multi-step AI agents to be usable in real-time. **Fireworks is fastest across the top open models among GPU-based providers, as benchmarked by Artificial Analysis.** Get the top speed you need, tailored for your use case, only with Fireworks.

Stay tuned as our engineering team continues to optimize the performance!

## Unlocking Peak Performance: Fireworks Customization Engine and Infrastructure

Fireworks’ customization engine and virtual cloud infrastructure are engineered to deliver best-in-class performance for developers. We’ve built the following advanced capabilities to enhance speed as seen in the benchmarks, and across multiple different usecases:

FireOptimizer maximizes performance by optimizing three core dimensions:

- **Deployment Shape:** Enables strategic GPU selection
- **Sharding Strategy:** provides advanced parallelism techniques.
- **Scheduling:** Expertly balancing Time-to-First-Token (TTFT) with overall throughput.

This ensures your hardware is precisely right-sized to meet the specific Service Level Agreements (SLAs) of your application.

- **Speculative Decoding: Accelerate Latency-Sensitive Applications**

For applications where latency is critical, such as code assistance and agentic reasoning, Fireworks leverages speculative decoding. This process employs a smaller “draft” model to anticipate token sequences, which the larger “target” model then validates in parallel. This methodology achieves a significant 2x to 3x speedup in generation without sacrificing the superior output quality of the main model.

- **Custom Kernels for Optimized Virtual Cloud Infrastructure**

To extract the maximum possible speed and efficiency from NVIDIA Blackwell GPU hardware, our engineering team developed customized kernels, ensuring optimal performance and fully leveraging the power of the underlying GPU architecture.

Together, these proprietary advancements ensure Fireworks delivers the unrivaled speed confirmed by independent Artificial Analysis benchmarks across the industry’s best open-source models. To further improve performance, you can leverage our Fine Tuning platform, to bring your own data to tailor your workload to your usecase. Get started [today](https://app.fireworks.ai/signup) or [contact us](https://fireworks.ai/contact) for help with your application.
