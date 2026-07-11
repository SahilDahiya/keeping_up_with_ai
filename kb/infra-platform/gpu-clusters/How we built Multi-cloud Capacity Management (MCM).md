---
title: How we built Multi-cloud Capacity Management (MCM)
topic: infra-platform
subtopic: gpu-clusters
secondary_topics:
- infra-platform/deployment
summary: Engineering writeup on building multi-cloud capacity management for inference
  infrastructure.
source: baseten
url: https://www.baseten.co/blog/how-we-built-multi-cloud-capacity-management/
author: William Lau; Colin McGrath; Phil Howes; Rachel Rapp
published: '2025-06-23'
fetched: '2026-07-11T04:07:54Z'
classifier: codex
taxonomy_rev: 1
words: 2159
content_sha256: 2c52c0f5887c6f12db8b783d4f0b221e068dec30e756fb3b6176b5afb4c92a13
triage: keep
skip_reason: null
---

# How we built Multi-cloud Capacity Management (MCM)

![Building multi-cloud capacity management at Baseten](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1750705195-announcement-important-text-template-3-1.png%3Fauto%3Dformat%26fit%3Dcrop%26h%3D630%26w%3D1200&w=3840&q=100)

To meet the demands of our customers' mission-critical workloads, we built Multi-cloud Capacity Management (MCM): a globally consistent orchestration layer that unifies GPUs across 20+ clouds and regions into one elastic, fungible GPU pool. MCM handles autoscaling, failover, and latency-aware routing—eliminating single points of failure and unlocking scarce GPU SKUs.

Today, we run models across 20+ clouds and dozens of regions worldwide to meet our customers' growing workload demands. But raw capacity alone isn’t enough—compute across providers and regions is inherently siloed, leaving it vulnerable to cloud failures and capacity constraints. To deliver the high uptime and reliable performance our customers expect, we had to unify the GPUs we run on.

That’s why we built Multi-cloud Capacity Management (MCM). MCM makes siloed compute completely fungible: different clusters, regions, and cloud providers become one elastic, universal cloud. It took over six months of engineering work from our entire infrastructure team to build, but the results set a completely new standard for how AI infrastructure operates.

![MCM makes siloed compute completely fungible. Different clusters, regions, and cloud providers become one elastic, universal cloud.](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1750760829-diagram-1-1.png%3Fauto%3Dformat%26w%3D1200&w=3840&q=75) MCM makes siloed compute completely fungible. Different clusters, regions, and cloud providers become one elastic, universal cloud.

MCM makes siloed compute completely fungible. Different clusters, regions, and cloud providers become one elastic, universal cloud.We’ve since been using MCM for our customers like [Bland](https://www.bland.ai/), [Abridge](https://www.abridge.com/), and [Writer](https://writer.com/) to:

- Power massive horizontal scale, balancing latency-aware resource allocation with global compute availability
- Recover model deployments to different clouds within minutes of cloud provider and hardware failures
- Unlock capacity for hard-to-get GPUs, like B200s

We wrote this blog to explain what exactly MCM is, how we built it, and how we believe it changes the expectations of what AI infrastructure does moving forward. We’ve said it before: every company is becoming an AI company. This level of flexible compute usage is non-negotiable for ensuring consistent performance, high uptime, and low costs for companies scaling AI products.

## What is MCM? Isn’t it just another “multi-cloud” solution?

Infrastructure providers have been saying they offer “multi-cloud” solutions for over a decade. The reality is that most of them just have siloed compute within each of their different clouds. There’s no way to use inter-cloud compute fluidly, and moving workloads across clouds is a tedious, error-prone process.

MCM unifies clouds, transforming siloed GPUs into a global resource pool regardless of cloud service provider (CSP) or region. Put more technically: MCM is a multi-region, multi-provider bin packing tool, which treats distinct pools of compute as fungible with each other. It brings the local power of Kubernetes to a global view, enabling self-healing and global scheduling.

We use MCM to route traffic across 20+ clouds and dozens of regions, optimizing for the closest resources while ensuring uptime. An H100 in us-east-1 on AWS becomes equivalent to an H100 in us-west4 on GCP.

![MCM can scale up model replicas across different clusters, regions, and clouds, treating them as one global, fungible resource pool.](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1750705391-image1.png%3Fauto%3Dformat%26w%3D1200&w=3840&q=75) MCM can scale up model replicas across different clusters, regions, and clouds, treating them as one global, fungible resource pool.

MCM can scale up model replicas across different clusters, regions, and clouds, treating them as one global, fungible resource pool. MCM [powers each of our deployment options](https://www.baseten.co/blog/how-baseten-multi-cloud-capacity-management-mcm-powers-cloud-self-hosted-and-hybr/): Baseten Cloud, Self-hosted, and Hybrid. The routing system behind MCM dynamically matches workloads to capacity based on:

- Geographical distance (placing workloads closest to end users for the lowest latency)
- Priority (regions in order of company preference)
- Customer constraints (compliance, IP)

That’s why when cloud providers have major outages, our inference—and our customers— remain unaffected. If a certain cloud or region goes down (or runs out of capacity), we just scale workloads out of it.

## Life before MCM: manual, rigid model deployments

Before we built MCM, our infrastructure looked a lot like everyone else’s. We ran workloads within single clusters by default. Even though we had a ton of capacity, it was spread across isolated resource pools (clusters and clouds). This created a bin packing problem:

- What workloads could we colocate?
- What did peak loads look like?
- And when would migrations be needed?

![These two workloads can be colocated at minimum load. But if they reach maximum load (without MCM), one would need to be migrated to another cluster with sufficient resources.](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1750705434-image2.png%3Fauto%3Dformat%26w%3D1200&w=3840&q=75) These two workloads can be colocated at minimum load. But if they reach maximum load (without MCM), one would need to be migrated to another cluster with sufficient resources.

These two workloads can be colocated at minimum load. But if they reach maximum load (without MCM), one would need to be migrated to another cluster with sufficient resources.When our customers needed to scale, we had two options:

- Add capacity to their existing cluster (adds latency)
- Or migrate their workloads to a different cluster or region (lengthy, tedious)

Manually moving workloads created operational overhead, but it was unavoidable when hardware or clouds went down, or workloads outscaled the clusters they were on. That’s why so many inference providers lock customers into fixed capacity instead of offering GPUs on demand.

After dealing with so many single points of failure (clusters, regions, or clouds that went down for any reason), capacity constraints, and orchestration headaches, we built MCM to power our autoscaling experience. MCM unlocked the ability to scale and failover on demand, endlessly.

## How we built MCM

To build MCM, we had to answer the question: **which workload should be assigned to which cluster at a specific point in time? **

It took our entire infrastructure team over six months of dedicated work to build MCM. We designed it from the ground up to support real-time, global capacity management. At the core of MCM is a globally consistent orchestration layer built on top of Kubernetes.

Traditional Kubernetes assumes a tight latency envelope between nodes (<10 ms). Since that model breaks down over long distances, we built a global scheduler that aggregates state across clusters, makes globally optimal decisions, and delegates those to local Kubernetes clusters for execution.

The system architecture follows a hub-and-spoke model:

- The - **global control plane**receives real-time event streams from every workload plane
- Each - **workload plane**reports capacity, utilization, and traffic demand
- The control plane makes real-time placement decisions based on this data

![MCM is built as a hub-and-spoke model, with a centralized global control plane that receives data from and delegates tasks to workload planes across different clouds.](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1750705508-image5.png%3Fauto%3Dformat%26w%3D1200&w=3840&q=75) MCM is built as a hub-and-spoke model, with a centralized global control plane that receives data from and delegates tasks to workload planes across different clouds.

MCM is built as a hub-and-spoke model, with a centralized global control plane that receives data from and delegates tasks to workload planes across different clouds.MCM determines in real time where workloads should live as they scale up, taking into account the traffic demands on each cluster. The result is hardware that’s completely fungible, no matter the cloud, cluster, or region it’s located in.

### Making performance consistent across clouds

Building an abstraction that treats global capacity as completely fungible needs a global routing system to support it. Because resources have different physical distances to end users, model performance will vary slightly based on where replicas live.

We implemented different measures to [make routing more intelligent](https://www.baseten.co/resources/guide/the-baseten-inference-stack/#intelligent-request-routing) and keep latency low, but ultimately, having enough capacity to meet demand will always be more important than geographical proximity. It’s the difference between a few added milliseconds of latency versus a product going offline.

### Ensuring compliance for sensitive workloads

Some of our customers have strict requirements to keep workloads in specific regions or within a particular cloud provider due to data residency, regulatory, or internal policy constraints.

To support these scenarios, we built MCM to support **region-locking and provider-locking** at the deployment level. These constraints are manually encoded for each customer and strictly enforced by the global scheduler. That means if a workload needs to stay in us-central1, MCM will never route it elsewhere.

### Building deep partnerships with cloud providers 

A large part of MCM's success relies on our cloud partnerships. We partner with 20+ cloud providers in dozens of regions globally to unlock almost unlimited capacity for our customers.

When sourcing compute, you often want to get the largest cluster possible (better economies of scale) while ensuring high utilization (using what you pay for). By pooling compute, we can unlock economies of scale while also ensuring high utilization for all customers.

Given MCM makes compute fungible, we have much more flexibility to adapt to new GPUs and geographies, and can be first-to-market with our cloud partners. Through these partnerships, we’ve taken teams that never purchased capacity through a CSP before and scaled them to 100s of nodes in under a week. Our close partnerships with cloud providers enable virtually unlimited scalability, reliability, and cost efficiency for our customers.

![Workloads at max scale with and without MCM.](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1750705498-image3.png%3Fauto%3Dformat%26w%3D1200&w=3840&q=75) Workloads at max scale with and without MCM. Without MCM, workloads must run on clusters with sufficient dedicated capacity or be migrated to ones that do. MCM enables optimal resource utilization without requiring workload migration, as model replicas can scale across clusters, regions, and clouds.

Workloads at max scale with and without MCM. Without MCM, workloads must run on clusters with sufficient dedicated capacity or be migrated to ones that do. MCM enables optimal resource utilization without requiring workload migration, as model replicas can scale across clusters, regions, and clouds.## MCM in production: Powering enterprises and startups alike

We’ve been using MCM for years to support our customers like [Writer](https://writer.com/), [Abridge](https://www.abridge.com/), and [Bland](https://www.bland.ai/). We run our customers’ mission-critical workloads, so if their models go down, so do their products. MCM enables our customers to leverage capacity around the world with a single API and zero management overhead, powering:

- High availability (four nines uptime)
- Reliably low latency
- Massive, elastic scale

We’ve seen the benefits time and again. When entire clouds go offline (this happens more often than you’d think), MCM scales replicas elsewhere and reroutes traffic within minutes, at least 6x faster than it takes to manually accommodate resources. This leads to significantly less downtime than single-provider, single-region solutions.

While MCM can be useful for any workload, we’ve especially seen value for use cases with:

- High uptime requirements
- Global user bases
- Large-scale, real-time operations
- Reliance on cutting-edge, hard-to-get GPUs with limited capacity

In our experience, enterprises value the ease of management for multiple data centers, unlimited horizontal scaling, and high uptime. Most early-stage companies haven’t encountered these problems yet, but they also have strong use cases for MCM, as they want to build reliable products that can accommodate bursty traffic.

## Should you build your own MCM solution?

If you didn’t just jump to this point in the blog, then by now you’ve probably gotten the message: unlocking multi-cloud capacity is important. So, should everyone start building similar solutions for their own use cases?

Inference providers: yes. Otherwise: no.

Building MCM took over six months of dedicated engineering work to ship when we built it early in 2024, and we had already unblocked a lot of challenges—like building a robust autoscaler, relationships with different cloud providers, and negotiating access to global compute resources. And MCM continues to evolve.

Even if you take it for granted that you can pool resources across clouds, you’ll still have to deal with:

- High-throughput, real-time event streaming and recomputation logic (real-time algorithms working with other real-time algorithms)
- Ensuring the actual system state remains consistent with decisions made (did you make the right decision, and did it actually get executed)
- Building systems that can reliably handle huge amounts of data without corruption or loss along the way

We think a product like MCM is essential for any inference provider that wants to be competitive. That said, while AI builders should definitely care about what MCM unlocks, it’s so high-stakes and resource-intensive that we wouldn’t recommend trying to recreate it in-house.

## The future of AI infrastructure will take MCM for granted

Model inference is core to product experience. The old way of thinking about infrastructure—pick a provider, deploy to a region, hope for the best—doesn’t scale with today’s massive AI workloads.

GPU availability is constrained. Regions go down. SKUs shift. And traffic bursts.

When we show people how we run thousands of GPUs in production across multiple clouds—and that the compute across those clouds is all completely fungible—they get excited. Uptime is a default, and capacity is unlimited. When systems and hardware fail, MCM provides the ability to quickly (and effortlessly) recover.

We believe MCM is where AI infrastructure is going, and will be taken as a given. There’s no other way to power the reliability, performance, and cost efficiency that AI-native products require.

If you want more details on how you can do multi-cloud inference with MCM, [reach out](https://www.baseten.co/talk-to-us/).
