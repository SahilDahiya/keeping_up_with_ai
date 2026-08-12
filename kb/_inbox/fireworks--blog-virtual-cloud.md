---
title: Build for Scale with Fireworks Virtual Cloud (GA)
kind: blog
topic: null
subtopic: null
secondary_topics: []
summary: null
triage: null
skip_reason: null
source: fireworks
url: https://fireworks.ai/blog/virtual-cloud
author: null
published: '2025-06-16'
fetched: '2026-08-12T06:30:05Z'
classifier: null
taxonomy_rev: 2
words: 1052
content_sha256: 26fc11a35f9a22f6f31908f935c6fdf201c24d4fb56662e2ecefa9b0cda67ca1
---

# Build for Scale with Fireworks Virtual Cloud (GA)

Anyone who has run a production application at scale knows the impact that performance and reliability has on product success. For AI applications, the challenge is often to successfully operate a fleet of GPUs that handles scaled, globally distributed traffic, potentially in the midst of unprecedented growth.

A few factors make managing bare-metal GPU deployments on your own difficult:

- •Differences and peculiarities of individual GPU clouds
- •Failover and disaster recovery
- •Global replication
- •Hardware failures and degradations

Ultimately, these distract your team from what matters: building winning product experiences for users. That’s why today we’re excited to announce the GA of the **Fireworks Virtual Cloud**, a platform that abstracts away the complexity of managing GPU deployments, handling hardware failures, and scaling workloads across a global fleet.

Launching with over 18 global regions across 8 cloud providers, including support for BYOC, Fireworks Virtual Cloud lets you build for scale from Day 1. To get started with Fireworks Virtual Cloud, [contact us](https://fireworks.ai/contact).

As of June 2025, **Fireworks processes 5 trillion+ tokens every day at 100,000+ requests/s**. For reference, this is roughly the same as the number of search queries Google processes per second

We enable this through our hardware fleet that spans 8 different cloud providers over 18 different regions. Working with multiple providers allows Fireworks to provide high-availability access to hardware when our customers need it. For security-sensitive enterprise workloads, we also support BYOC.

Fireworks offers a wide variety of compute architectures from NVIDIA and AMD. We consistently strive to deliver the latest GPU generation to customers quickly and enable optimal performance across the entire stack. For example, we were among the first providers to bring up [AMD MI300X last year](https://fireworks.ai/blog/fireattention-v3). We also offer older generations of accelerators that can strike a better performance/$ tradeoff for some workloads.

We’re excited to offer the latest generation of NVIDIA B200s GPUs on Fireworks as of May 2025. Blackwell GPUs offer native support for float4 precision which allows unmatched speed and cost efficiency. Using float4 without quality regression requires additional tuning, now automatically provided by FireOptimizer. See the [B200 announcement blog post](https://fireworks.ai/blog/fireattention-v4-fp4-b200) for more details.

Thanks to the latest hardware and end-to-end stack optimization Fireworks is able to offer groundbreaking speeds, for example over 250 token/s for [DeepSeek V3](https://fireworks.ai/models/fireworks/deepseek-v3) and R1 models.

We previously shared how [Fireworks 3D Optimizer](https://fireworks.ai/blog/3d-fireoptimizer) considers your specific workload characteristics and tunes our proprietary inference engine across the dimensions of speed, quality, and cost.

Additionally, each workload might have unique constraints determining its scheduling:

- •**Geographic locality** - to place the GPUs close to the users across the globe
- •**Autoscaling or fixed scheduling** – to account for varying traffic patterns
- •**Compliance and security requirements** – that may limit permitted regions
- •**Disaster resilience** - spreading workload across multiple regions and availability jobs to provide uninterrupted service in case of underlying outages.

Fireworks Virtual Cloud Scheduler lets you specify these requirements and automatically arranges resources to satisfy these constraints.

GenAI workloads have complicated performance characteristics. At Fireworks we co-design our inference stack for optimal speed and efficiency at every level, from GPU kernels all the way to routing traffic across the globe.

For example, an interesting property of many workloads we run is **heterogeneity**. Reinforcement fine-tuning, for instance, consists of alternating phases of policy rollouts (inference-like workload) and policy updates (training-like workload). Similarly, LLM inference consists of prompt processing (GPU compute bound) and token generation (memory bandwidth bound). We can exploit this heterogeneity through **disaggregation**. Each part of the workload can be configured and scaled independently, allowing our scheduler to achieve higher efficiency.

Another example is [prompt caching](https://docs.fireworks.ai/guides/prompt-caching). Caching KVs for prompts is one of the most fundamental and critical optimizations to high-performance LLM inference. While conceptually simple, it can be deceptively difficult to optimize when running in large-scale, distributed inference. The system has to balance load on two dimensions: individual component load and locality of the existing precomputed KV cache entries (at region, cluster and node level). At Fireworks we implemented a multi-tiered caching and traffic routing system to maximize the cache hit rate in such real-world scenarios. Even under diverse workload conditions, we often see cache hit rates between 60-90% (or equivalently, 3-10x savings on prompt processing).

Running any hardware at scale involves dealing with failures on a regular basis. GPUs in particular are prone to failure due to any number of reasons: disappearing from the system (“falling off the bus”), overheating (leading to lower performance), memory corruption (leading to strange crashes), etc.

The [Llama 3 paper](https://arxiv.org/abs/2407.21783) reports 99.95% reliability for a single GPU on a given day, or only 83% reliability over the course of a year. While in practice we observe worse baseline up-times, even taking the generous estimates means a deployment running on 100 GPUs will experience some failure every 20 days, and a deployment running on 1000 GPUs will experience some failure every other day!

Fireworks Virtual Cloud hides this complexity by proactively monitoring GPU and node health. If an unexpected failure does occur, Fireworks automatically re-provisions capacity and moves your workloads to healthy hardware to minimize downtime. And, our multi-region capability allows customers to create high-availability deployments that protect against geographically-correlated outages.

For maximum data security, Fireworks enables you to bring GPU hardware running on your own cloud infrastructure through our hybrid bring-your-own-cloud offering. We enable you to run the Fireworks inference engine inside your own VPC, so you get all the benefits of Fireworks while ensuring data never leaves your secure environment.

Our BYOC offering is perfect for customers who:

- •Need to host sensitive workloads
- •Have existing commitments for GPUs
- •Want maximum transparency and control over the hosting environment

The Fireworks Virtual Cloud seamlessly integrates with your cloud environment, so deploying your workloads is just as easy as using our fully hosted solution. We also enable running in a hybrid mode as well, where some more sensitive workloads may run in your self-hosted environment while others may run on Fireworks cloud.

At Fireworks, we believe that AI teams should be able to build for scale without worrying about scale. With Fireworks Virtual Cloud, you now have access to a highly-available global fleet of GPUs, optimized for your workload, fully managed and running on state-of-the-art hardware.

[Contact us](https://fireworks.ai/contact) to explore how Fireworks Virtual Cloud can support your needs.
