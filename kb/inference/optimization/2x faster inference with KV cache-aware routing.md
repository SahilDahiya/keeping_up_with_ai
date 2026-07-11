---
title: 2x faster inference with KV cache-aware routing
topic: inference
subtopic: optimization
secondary_topics:
- inference/serving
summary: Describes 2x faster inference through KV-cache-aware routing with NVIDIA
  Dynamo.
source: baseten
url: https://www.baseten.co/blog/how-baseten-achieved-2x-faster-inference-with-nvidia-dynamo/
author: Abu Qader; Michael Feil; Rachel Rapp
published: '2025-10-16'
fetched: '2026-07-11T04:07:08Z'
classifier: codex
taxonomy_rev: 1
words: 930
content_sha256: ac25d4aaf4ca3602d6d7ba94693bf46ba56a35be0d40b1b3c53b90b6fe6a93cd
triage: keep
skip_reason: null
---

# 2x faster inference with KV cache-aware routing

![2x faster inference with Nvidia Dynamo](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1760421464-dynamo_blog-header_image.png%3Fauto%3Dformat%26fit%3Dcrop%26h%3D630%26w%3D1200&w=3840&q=100)

At Baseten, we collaborate closely with NVIDIA to push the boundaries of model performance. When NVIDIA releases new tooling, our model performance team immediately starts testing it out, measuring the potential gains against our current stack and battle-hardening new features for production.


Often, NVIDIA releases updates as a result of this work: our engineers submit pull requests to their open-source GitHub repositories, making things more robust and secure for production use cases. This symbiosis is what brought us to quickly adopt [ NVIDIA Dynamo](https://github.com/ai-dynamo/dynamo), NVIDIA’s newest open-source inference framework.

## How Baseten uses NVIDIA Dynamo

NVIDIA Dynamo is built for large-scale LLM serving across distributed GPU clusters with high throughput and low latency. It includes features like disaggregated prefill and decode steps, KV cache-aware routing,  [KV cache-offload to storage](https://docs.nvidia.com/dynamo/latest/architecture/kvbm_intro.html), an [SLA-based planner](https://github.com/ai-dynamo/dynamo/blob/main/docs/architecture/sla_planner.md) for autoscaling, and dynamic GPU scheduling. Across all models, we’ve seen huge performance improvements by using Dynamo’s KV cache-aware routing—those benefits are what this blog focuses on. 

The KV cache stores a model’s previously computed key/value states for past tokens, so it can reuse them instead of recomputing them with each new request. This speeds up inference, especially for long-context generation. KV cache-aware routing (NVIDIA also calls this “LLM-aware request routing”) makes sure that incoming requests are sent to the model replicas with previously stored context.

## How KV-aware routing works

The NVIDIA Dynamo LLM Aware Router manages KV cache across large GPU fleets in multinode and disaggregated inference deployments and supports different inference backends like SGLang, TensorRT-LLM, and vLLM. Hashing incoming requests and organizing them in a Radix Tree enables scalable tracking of cache locations in distributed environments.

When new inference requests arrive, the LLM Aware Router calculates an overlap score between the request and the KV cache blocks already active across all GPUs in the cluster. Based on this overlap and the current distribution of GPU workload, it routes requests to the most suitable workers, minimizing KV cache recomputation while maintaining balanced load across the cluster.

Unlike round-robin or purely load-based routing, this method improves overall system performance by considering cache hit rate and workload balance, ensuring efficient request handling and reducing resource bottlenecks.

![Description: KV-aware routing sends requests to replicas that already have relevant context cached, saving time by avoiding redundant prefill computation.](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1763057468-kvroutingchart.png%3Fauto%3Dformat%26w%3D1200&w=3840&q=75) KV-aware routing sends requests to replicas that already have relevant context cached, saving time by avoiding redundant prefill computation.

KV-aware routing sends requests to replicas that already have relevant context cached, saving time by avoiding redundant prefill computation.For instance, if you use one of our [Model APIs](https://www.baseten.co/products/model-apis/) to chat with [DeepSeek R1](https://www.baseten.co/library/deepseek-r1/), new requests (new inputs to the model) will be routed to the replica that has the most optimal combination of KV cache overlap and GPU load. We love that Dynamo also lets us easily add custom routing logic, so we can use a mix between KV routing and round-robin routing as it best suits the model and use case. 

KV-aware routing is especially useful for large models with long context windows, like in code generation use cases with long-context requests. Relevant models here are [GLM](https://www.baseten.co/library/family/glm/), [Kimi](https://www.baseten.co/library/family/kimi/), [MiniMax](https://www.baseten.co/library/publisher/minimax/), [DeepSeek, ](https://www.baseten.co/library/family/deepseek/)and [Qwen](https://www.baseten.co/library/family/qwen/).

## Qwen3 Coder benchmarks with KV routing

Qwen3 Coder 480B A35B is a popular LLM in the Qwen model family optimized for tasks like code writing, debugging, and tool use. With a native context window of 262K tokens, it has one of the largest context windows that users actively use to process large code bases.

To show the impact of NVIDIA Dynamo’s KV cache-aware routing, we conducted a high-load stress test with long inputs (~50k tokens on average) and outputs (~1k tokens on average), toggling KV routing on and off (in the latter case, the routing is random). We see a significant performance improvement in terms of time to first token (TTFT, measured in milliseconds) and time per output token (TPOT, also measured in milliseconds): KV routing results in a 34% reduction in TPOT and 50% reduction in TTFT on average.

![Qwen3 480B Coder Latency](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1760419786-qwen3-480b-coder-latency-lower-is-better.png%3Fauto%3Dformat%26w%3D1200&w=3840&q=75) Description: KV routing results in a 34% reduction in TPOT and 50% reduction in TTFT on average with an 89% hit rate across four replicas.

Description: KV routing results in a 34% reduction in TPOT and 50% reduction in TTFT on average with an 89% hit rate across four replicas.Because some benchmarks can be point-in-time, we ran an additional benchmark by shadowing real production traffic — with a measurable impact on the client side — [from OpenRouter](https://openrouter.ai/qwen/qwen3-235b-a22b-2507?sort=latency). We saw similar results: a 48% decrease in P95 latency with KV cache-aware routing, and a 49% decrease in P99 latency.

![Qwen3 480B Coder OpenRouter TTFT](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1760419882-qwen3-480b-coder-openrouter-ttft-lower-is-better.png%3Fauto%3Dformat%26w%3D1200&w=3840&q=75) Description: We see a 48% decrease in P95 latency when KV cache-aware routing is turned on, and a 49% decrease in P99 latency.

Description: We see a 48% decrease in P95 latency when KV cache-aware routing is turned on, and a 49% decrease in P99 latency.Reductions in latency (and recalculations of the KV cache for repeat requests) mean GPUs are freed up more quickly to serve new requests, affecting overall throughput. We also see 61% more requests processed per second (RPS) and a 62% increase in output tokens per second (TPS) overall.

![Qwen3 480B Coder Throughput (sec)](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1760718844-qwen3-480b-coder-throughput-higher-is-better-2.png%3Fauto%3Dformat%26w%3D1200&w=3840&q=75) Qwen3 480B Coder Throughput (sec)

Qwen3 480B Coder Throughput (sec)## Looking forward

We are continually deepening our usage of NVIDIA tooling. Looking forward, we’re benchmarking the impact of Dynamo features like KV cache offloading and transfer to expand context lengths, and to improve resource utilization, concurrency, and throughput.

[Check out](https://www.baseten.co/products/model-apis/) our Model APIs for an easy introduction to Baseten.
