---
title: 'Introducing Baseten Embeddings Inference: The fastest embeddings solution
  available'
kind: blog
topic: inference
subtopic: serving
secondary_topics:
- rag-retrieval/embeddings
summary: Describes Baseten Embeddings Inference (BEI), a serving engine for embedding/reranker/classifier
  models tuned for both high-concurrency batch throughput and low-latency single queries,
  claiming 2x throughput and 10% lower latency than prior solutions.
triage: null
skip_reason: null
source: baseten
url: https://www.baseten.co/blog/introducing-baseten-embeddings-inference-bei
author: Michael Feil
published: '2025-03-27'
fetched: '2026-11-12T06:09:48Z'
classifier: claude
taxonomy_rev: 2
words: 754
content_sha256: a39d2762b5ddb65ec0ad4026f34d752454a72e4594f740fece8c4882ee521249
---

# Introducing Baseten Embeddings Inference: The fastest embeddings solution available

News
# Introducing Baseten Embeddings Inference: The fastest embeddings solution available

Baseten Embeddings Inference (BEI) delivers 2x higher throughput and 10% lower latency for production embedding, reranker and classification models at scale.


- Authors
- Date
- March 27, 2025

TLDR

Baseten Embeddings Inference (BEI) is the most performant embeddings inference solution for high-throughput, low-latency production workloads. With over 2x higher throughput and 10% lower latency than previous industry standards, BEI powers embedding, reranker, and classifier inference for rapid responses even under heavy load. If you need high-performance inference for your embeddings workloads, reach out to talk to our engineers!

From search and retrieval applications to agents and recommender systems, rapid responses are a must-have for an excellent user experience. Companies building products that leverage embeddings in production need to ensure fast and reliable model performance, whether you’re processing an entire database worth of documents or handling 100,000 user requests.

We’re excited to announce Baseten Embeddings Inference (BEI), the fastest embeddings inference on the market, to provide users with the highest-throughput and lowest-latency embeddings inference at scale. With over 2x higher throughput and 10% lower latency than the next-best solution, BEI provides optimized inference performance out of the box for embedding, reranker, and classification models.

BEI is tailored specifically for the needs of embedding workloads, which often receive high numbers of requests and require low latency for individual queries. Coupled with our optimized cold starts, elastic horizontal scale, and five nines uptime, you can use BEI with open-source, custom, or fine-tuned models or as part of compound AI systems for fast, reliable inference in production.

In this post, we’ll look at performance benchmarks and common use cases suited for BEI. If you’re looking for fast, reliable, and cost-efficient production inference for your embeddings use case (or anything else), you can reach out [here](https://www.baseten.co/talk-to-us/) to talk with our engineers.

After working with AI builders who are shipping embeddings pipelines to millions of users across the globe, we saw the need for a more performant inference solution. Other solutions on the market focus on scale (an inherent aspect of our infrastructure) or accuracy at the model level, and simply fall short in terms of throughput and latency. That’s why we built BEI.

To optimize BEI and benchmark it against other toolsets, we focused on two metrics:

- **High concurrency:** If I send 100,000 requests, how many can BEI handle per second?
- **Rapid single responses:** If a single user is asking one question, what latency will they experience?

High throughput helps embeddings pipelines scale efficiently, whether you’re performing searches for thousands of users, storing millions of documents in a database, or providing content recommendations in real time. Low latency ensures that each individual query is processed quickly, meeting or exceeding service SLAs with a best-in-class user experience.

In terms of throughput, BEI can process 2x more requests per second compared to TEI, the next-best solution, and 9x more than Ollama, which was the least performant toolkit we assessed.

We also found that it’s over 10% (1.12x) faster than TEI for single queries.

BEI’s performance boosts aren’t an artifact of using more powerful hardware. BEI is even more memory-efficient than other toolkits, meaning you can run it on smaller instance types while still getting superior performance.

If you’re interested in how we built BEI to have higher throughput, lower latency, and a lower memory footprint than other solutions, check out our [technical deep dive](https://www.baseten.co/blog/how-we-built-high-throughput-embedding-inference-with-tensorrt-llm/).

BEI is completely plug-and-play and works as an integrated part of our optimized [TensorRT-LLM Engine Builder](https://docs.baseten.co/examples/bei). Bring any model—open-source, custom, or fine-tuned—and get optimized model performance out of the box.

BEI can optimize model performance for use cases like:

- Large-scale search systems (in any industry)
- RAG (embedding and reranking)
- Recommender systems
- Reward modeling
- Agents
- Content classification
- Compound AI systems
- Synthetic data generation

You can use BEI on [Baseten Cloud](https://www.baseten.co/deployments/baseten-cloud/), or as part of [self-hosted](https://www.baseten.co/deployments/baseten-self-hosted/) or [hybrid](https://www.baseten.co/deployments/baseten-hybrid/) deployments.

Baseten exists to provide our customers with the most performant, reliable, and cost-efficient inference solutions for their mission-critical workloads. Unlike other solutions on the market, BEI doesn’t just provide accurate embeddings on scalable infrastructure. BEI provides the highest throughput and lowest latency at the most efficient footprint, giving you fast, reliable, cost-efficient results at infinite scale.

If you’re running [embeddings models](https://www.baseten.co/resources/guide/high-performance-embedding-model-inference/) or compound AI systems at scale, [reach out](https://www.baseten.co/talk-to-us/) to learn how our engineers can optimize your workloads. In the meantime, you can also check out our [technical deep dive](https://www.baseten.co/blog/how-we-built-high-throughput-embedding-inference-with-tensorrt-llm/) on how we optimized BEI, or our [docs](https://docs.baseten.co/examples/bei)!
