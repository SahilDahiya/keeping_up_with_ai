---
title: 2x faster inference with KV cache-aware routing
kind: blog
topic: null
subtopic: null
secondary_topics: []
summary: null
triage: null
skip_reason: null
source: baseten
url: https://www.baseten.co/blog/how-baseten-achieved-2x-faster-inference-with-nvidia-dynamo
author: Abu Qader
published: '2025-10-16'
fetched: '2026-11-12T06:14:04Z'
classifier: null
taxonomy_rev: 2
words: 738
content_sha256: 2a8d0a80ee94dff917a2dc2616357f6e0bcebf60208ca442c2a30721f98936ff
---

# 2x faster inference with KV cache-aware routing

Model performance
# 2x faster inference with KV cache-aware routing

KV cache-aware routing is part of the Baseten Inference Stack's optimized infrastructure. With it, we often see 2x faster TTFT in production.


- Authors
- Date
- October 16, 2025

TLDR

At Baseten, we collaborate closely with NVIDIA to push the boundaries of model performance. When NVIDIA releases new tooling, our model performance team immediately starts testing it out, measuring the potential gains against our current stack and battle-hardening new features for production. Often, NVIDIA releases updates as a result of this work: our engineers submit pull requests to their open-source GitHub repositories, making things more robust and secure for production use cases. This symbiosis is what brought us to quickly adopt NVIDIA Dynamo, NVIDIA’s newest open-source inference framework.

NVIDIA Dynamo is built for large-scale LLM serving across distributed GPU clusters with high throughput and low latency. It includes features like disaggregated prefill and decode steps, KV cache-aware routing,  [KV cache-offload to storage](https://docs.nvidia.com/dynamo/latest/architecture/kvbm_intro.html), an [SLA-based planner](https://github.com/ai-dynamo/dynamo/blob/main/docs/architecture/sla_planner.md) for autoscaling, and dynamic GPU scheduling. Across all models, we’ve seen huge performance improvements by using Dynamo’s KV cache-aware routing—those benefits are what this blog focuses on.

The KV cache stores a model’s previously computed key/value states for past tokens, so it can reuse them instead of recomputing them with each new request. This speeds up inference, especially for long-context generation. KV cache-aware routing (NVIDIA also calls this “LLM-aware request routing”) makes sure that incoming requests are sent to the model replicas with previously stored context.

The NVIDIA Dynamo LLM Aware Router manages KV cache across large GPU fleets in multinode and disaggregated inference deployments and supports different inference backends like SGLang, TensorRT-LLM, and vLLM. Hashing incoming requests and organizing them in a Radix Tree enables scalable tracking of cache locations in distributed environments.

When new inference requests arrive, the LLM Aware Router calculates an overlap score between the request and the KV cache blocks already active across all GPUs in the cluster. Based on this overlap and the current distribution of GPU workload, it routes requests to the most suitable workers, minimizing KV cache recomputation while maintaining balanced load across the cluster.

Unlike round-robin or purely load-based routing, this method improves overall system performance by considering cache hit rate and workload balance, ensuring efficient request handling and reducing resource bottlenecks.

For instance, if you use one of our [Model APIs](https://www.baseten.co/products/model-apis/) to chat with [DeepSeek R1](https://www.baseten.co/library/deepseek-r1/), new requests (new inputs to the model) will be routed to the replica that has the most optimal combination of KV cache overlap and GPU load. We love that Dynamo also lets us easily add custom routing logic, so we can use a mix between KV routing and round-robin routing as it best suits the model and use case.

Qwen3 Coder 480B A35B is a popular LLM in the Qwen model family optimized for tasks like code writing, debugging, and tool use. With a native context window of 262K tokens, it has one of the largest context windows that users actively use to process large code bases.

To show the impact of NVIDIA Dynamo’s KV cache-aware routing, we conducted a high-load stress test with long inputs (\~50k tokens on average) and outputs (\~1k tokens on average), toggling KV routing on and off (in the latter case, the routing is random). We see a significant performance improvement in terms of time to first token (TTFT, measured in milliseconds) and time per output token (TPOT, also measured in milliseconds): KV routing results in a 34% reduction in TPOT and 50% reduction in TTFT on average.

Because some benchmarks can be point-in-time, we ran an additional benchmark by shadowing real production traffic — with a measurable impact on the client side — [from OpenRouter](https://openrouter.ai/qwen/qwen3-235b-a22b-2507?sort=latency). We saw similar results: a 48% decrease in P95 latency with KV cache-aware routing, and a 49% decrease in P99 latency.

Reductions in latency (and recalculations of the KV cache for repeat requests) mean GPUs are freed up more quickly to serve new requests, affecting overall throughput. We also see 61% more requests processed per second (RPS) and a 62% increase in output tokens per second (TPS) overall.

We are continually deepening our usage of NVIDIA tooling. Looking forward, we’re benchmarking the impact of Dynamo features like KV cache offloading and transfer to expand context lengths, and to improve resource utilization, concurrency, and throughput.

[Check out](https://www.baseten.co/products/model-apis/) our Model APIs for an easy introduction to Baseten.
