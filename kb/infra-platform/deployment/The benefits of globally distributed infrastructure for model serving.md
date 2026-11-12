---
title: The benefits of globally distributed infrastructure for model serving
kind: blog
topic: infra-platform
subtopic: deployment
secondary_topics: []
summary: Explains how multi-cloud and multi-region model-serving architecture improves
  GPU availability, cost (via per-provider pricing arbitrage), redundancy against
  provider outages, and latency, citing Baseten's own provider-agnostic routing.
triage: null
skip_reason: null
source: baseten
url: https://www.baseten.co/blog/the-benefits-of-globally-distributed-infrastructure-for-ml-model-serving
author: Phil Howes
published: '2024-03-01'
fetched: '2026-11-12T06:11:58Z'
classifier: claude
taxonomy_rev: 2
words: 611
content_sha256: 506b9bf1c3e24bc32a1435fd5f19b760b6e1819743c91fc981d0ac9553e3c1fa
---

# The benefits of globally distributed infrastructure for model serving

Infrastructure
# The benefits of globally distributed infrastructure for model serving

Multi-cloud and multi-region infrastructure for model serving provides availability, redundancy, lower latency, cost savings, and data residency compliance.


- Authors
- Date
- March 1, 2024

Directly optimizing an ML model is essential for high-performance inference, but the infrastructure used to serve that optimized model can have just as much — or even more — impact on how the model performs end-to-end in production. At Baseten, we abstract away infrastructure decisions to make compute a fungible resource, but under the hood we run globally distributed infrastructure across cloud providers and geographic regions.

Globally distributed infrastructure should be both:

- **Multi-cloud**: Running workloads on multiple cloud providers (e.g. AWS, GCP) via a unifying abstraction.
- **Multi-region**: Running workloads across multiple regions within a given cloud provider (e.g. us-east-1, us-west-1) and routing traffic appropriately.

Let’s dive into the benefits that multi-cloud, multi-region model serving infrastructure offers across availability, cost, redundancy, latency, and compliance.

Everyone from startups to enterprises has grappled with the difficulty of securing the GPUs required for model training and inference workloads. With a multi-cloud architecture, you get access to GPUs from multiple providers, increasing GPU availability.

Beyond raw availability, different cloud providers offer different GPUs. For example, AWS doesn’t offer L4 GPUs, while GCP lacks A10 GPUs. Picking the right GPU is an essential part of optimizing model cost-performance tradeoffs, and being able to run your workload across multiple cloud providers gives you access to the widest range of GPU options.

Cloud providers have different pricing for GPU-backed instances. With a multi-cloud architecture, you can run workloads where they make the most financial sense.

At Baseten, we use our provider-agnostic architecture to leverage multiple cloud service providers. We’re able to make competitive compute commits that give us access to better per-unit pricing and pass those savings on to our customers.

When any major cloud provider has downtime, whole swaths of the internet go down with it. But multi-cloud and multi-region infrastructure lets you sidestep downtime by shifting workloads to regions with capacity. Moving a workload across regions or even cloud providers is not trivial — building a practice of non-emergency migrations as part of the ordinary course of operating distributed infrastructure builds essential processes to handle any emergency migrations due to outages.

A huge amount of model performance optimization work is dedicated to [reducing latency during ML inference](https://www.baseten.co/blog/40-faster-stable-diffusion-xl-inference-with-nvidia-tensorrt/). But if the GPU running the optimized model is in California and the end user is in Australia, there will be unacceptable user-facing latency no matter how fast the model itself can run.

Multi-region infrastructure allows you to locate your servers near your users, reducing network latency. And co-locating ML inference servers in the same region as other pieces of your backend infrastructure offers further latency reductions.

Some customers, markets, and workloads require that their data stay in a certain geographic region for legal and compliance reasons. This is called “data residency.” With multi-region infrastructure, you can provide data residency compliance to users worldwide.

At Baseten, we can specify constraints on region and cloud provider for customers with strong data residency requirements.

At Baseten, we abstract away the complexities of operating multi-cloud, multi-region ML model serving infrastructure, leaving you with the benefits of availability, redundancy, cost savings, lower latency, and data residency compliance without the headache of operating workloads on multiple platforms.

Deploy an open source model from our [model library](https://www.baseten.co/library) or [your own custom model](https://truss.baseten.co) today to access optimized inference on a wide range of GPUs. And if you’re interested in region-specific deployments to meet latency, data residency, or compliance needs, [get in touch](mailto:support@baseten.co) and we’ll be happy to help.
