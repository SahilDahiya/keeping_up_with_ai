---
title: 'Introducing the Baseten Delivery Network: Fast cold starts for big models'
topic: infra-platform
subtopic: deployment
secondary_topics:
- inference/serving
summary: Introduces the Baseten Delivery Network for reducing cold starts when serving
  large models.
source: baseten
url: https://www.baseten.co/blog/baseten-delivery-network-fast-cold-starts-big-models/
author: Stephen Day; Kazuyoshi Kato; Gregory Kofman; Rachel Rapp
published: '2026-03-19'
fetched: '2026-07-11T04:05:57Z'
classifier: codex
taxonomy_rev: 1
words: 1625
content_sha256: 1a6382f8092c3092250f35d7d30620a2d437c9f0f99813bea7fccf559b56ac4c
triage: keep
skip_reason: null
---

# Introducing the Baseten Delivery Network: Fast cold starts for big models

![Introducing the Baseten Delivery Network: Fast cold starts for big models](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1773939402-bdn-thumbnail.png%3Fauto%3Dformat%26fit%3Dcrop%26h%3D630%26w%3D1200&w=3840&q=100)

Today we're launching the Baseten Delivery Network (BDN), built from the ground up to eliminate cold start bottlenecks for large models at scale. BDN delivers 2–3x faster cold starts through multi-tier caching and single-flight downloads that prevent thundering herd issues during burst scaling. BDN is now available to all organizations on Baseten!

Everybody hates cold starts. In an ideal world, cold start time would be instantaneous; in practice, it can take anywhere from seconds to hours, depending on your infrastructure and model. Spiky traffic, large models, and upstream dependencies only make scale-up times longer and more complicated to resolve.

Today, we're announcing the Baseten Delivery Network (BDN): a solution built from the ground up to address cold start issues for large models at scale. In practice, we see 2-3x faster cold starts compared to alternative solutions for customers scaling models with 10s to 100s of billions of parameters.

BDN is integrated into the [Baseten Inference Stack](https://www.baseten.co/resources/guide/the-baseten-inference-stack/), and is available today to any customer on Baseten.

## What makes cold starts so difficult to solve?

A cold start is everything that happens between "a new replica is requested" and "that replica is ready to serve traffic." Cold starts are difficult to solve for because they actually encompass ~6 different steps:

- **Hardware provisioning:**Before anything else, a node has to be available. We handle provisioning across a global pool of GPUs with our- [Multi-cloud Capacity Manager (MCM)](https://www.baseten.co/blog/how-we-built-multi-cloud-capacity-management/)— we won’t go into the details of provisioning here.
- **Scheduling:**Once hardware is available, the Kubernetes scheduler assigns your pod to a node. For most deployments this is fast, a few seconds at most.
- **Image pull:**Before your model runs, the container image has to land on the node. Inference images are large (typically multiple GB), but this problem is largely solved with proper image caching and loading techniques.
- **Weight download:**This is where things can get expensive, especially for large models. Your model weights have to be transferred from wherever they're stored to the node's local disk. For frontier-scale models, this can easily be 100s of GB of weights.
- **Container startup:**Once the image is pulled and weights are available, the container process starts. Framework initialization, CUDA context setup, configuration loading — this is typically fast, on the order of seconds, and largely fixed by your runtime choices.
- **Model load:**The inference engine (e.g., vLLM, TensorRT-LLM, or SGLang) loads weights from disk into GPU memory, initializes the KV cache, and potentially compiles CUDA graphs. This phase is largely determined by model size and engine configuration. It's an important optimization target, but one that lives in the engine layer vs. infrastructure.

![The cold start process includes 6 steps (including hardware provisioning). Downloading model weights (step 3) is one of the most expensive in the series.](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1773938800-diagram1.png%3Fauto%3Dformat%26w%3D1200&w=3840&q=75) The cold start process includes 6 steps (including hardware provisioning). Downloading model weights (step 3) is one of the most expensive in the series.

The cold start process includes 6 steps (including hardware provisioning). Downloading model weights (step 3) is one of the most expensive in the series.Of these phases, hardware provisioning and weight download can be the most variable. Weight download specifically is almost entirely a function of where weights live, how fast you can read them, and whether 1 pod or 500 pods are trying to do the same thing simultaneously.

For large models, weight download can dominate total cold start time and degrade sharply under load conditions for spikey traffic. This is what BDN is built for.

## Why weight loading breaks down at scale

The naive approach to weight loading is simple. When a pod needs weights, it pulls them from upstream storage: Hugging Face, S3, GCS.

There are three problems with this approach.

### Slow weight pulls

A 70B parameter model can carry over 100GB of weights; many frontier models are easily 100s of GB. Pulling that volume from remote storage on every scale-up means replicas spend most of their cold start time waiting for a network transfer to finish from wherever they happen to live upstream.

### Upstream fragility

When your weight download depends on a third-party service, their uptime becomes your uptime. A model hub outage, a rate limit, an expired credential, or a throttled bucket can make it impossible to download weights, leaving your pods unable to start.

### The thundering herd 

When your autoscaler spins up 50 or 100 replicas simultaneously (which is exactly what happens during a traffic burst or a new model rollout), every one of those pods races to the same upstream source for the same hundreds of gigabytes of data at the same time.

Object storage has bandwidth limits and rate limits. This becomes a traffic jam: replicas fight each other for download bandwidth, and load times spike from minutes to potentially hours.

![Thundering herd vs. single-flight download](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1773880058-diagram-2-11.png%3Fauto%3Dformat%26w%3D1200&w=3840&q=75) Single-flight download (left) vs. thundering herd (right). On the left, a single coordinator node pulls once from object storage, then fans data out to four pods cleanly; on the right, 50–100 pods simultaneously fire individual requests at the same object storage source, saturating bandwidth and turning the download into a traffic jam.

Single-flight download (left) vs. thundering herd (right). On the left, a single coordinator node pulls once from object storage, then fans data out to four pods cleanly; on the right, 50–100 pods simultaneously fire individual requests at the same object storage source, saturating bandwidth and turning the download into a traffic jam.## Why common solutions don't fully solve weight loading for cold starts

Several approaches have emerged to address these issues. They target the symptoms, not the problem.

The most common pattern is to put a caching layer between your pods and your upstream object storage. Downloads get faster because frequently used weights live on faster local storage rather than being sent over the network every time. But two problems persist.

First, you still have to deal with the thundering herd problem. If 100 pods on 20 nodes all request the same model simultaneously, and your cache processes them independently, this can still cause contention.

Second, there's the question of what happens on the first pull. If you’re still fetching weights from upstream object storage, you still have a dependency on its availability, bandwidth limits, and rate limits.

Aside from these issues, it can be hard to gauge the impact of solutions that take this approach without a lot of context on the specific infrastructure setup and model. Metrics like “aggregate cluster throughput” can be produced arbitrarily and will be entirely determined by factors such as cluster size, networking, model size, and other factors.

## The Baseten Delivery Network: Fast cold starts at scale

BDN is specifically built to ensure a fast and consistent experience in cases where most solutions break down: large models scaling rapidly. BDN is built around three structural choices that, together, eliminate the weight-loading issues described above.

**1: BDN owns the source.** 

Weights are mirrored to your infrastructure at push time, so your deployments have no runtime dependency on upstream services. Third-party outages and rate limits are decoupled from your scale-up path. (Weight mirrors can only be accessed by model deployments, not users. For security-sensitive use cases, we can enable private buckets for weight storage.)

**2: BDN uses a multi-tier cache, colocated with your workload.** 

Rather than pulling weights across a network hop at startup, BDN keeps weights close to where they’re consumed. There are three cache tiers, each faster than the last:

- Tier 1: Local node cache. Once a model has been pulled to a node, it lives on fast local NVMe storage. Any subsequent pod on that node gets the weights from a local disk read, no network involved.
- Tier 2: Peer cache. If a neighboring node in the cluster already has the weights, BDN serves them over the fast in-cluster network.
- Tier 3: Mirrored origin. On a true cache miss — a model that hasn't been seen in the cluster yet — BDN fetches from the mirrored storage using parallel byte-range downloads for high throughput.

These tiers are designed to ensure that weights are always delivered from the fastest available source.

**3: Weight downloads are single-flight.** 

When many replicas start simultaneously, BDN ensures only one weight fetch is triggered per file, not one per pod.

At the node level, all pods waiting on the same model share a single download. At the cluster level, consistent hashing assigns ownership of each model file to a specific cache node, so even when dozens of nodes are cold-starting simultaneously, each file has exactly one node responsible for fetching it from origin. (In other words: no more thundering herd).

The outcome: cold starts that are 2–3x faster across the board, with the largest gains precisely in the burst-scale scenarios — high replica counts, large models, rapid rollouts — where the problem is most painful. User experience is consistent whether you're going from 1 replica to 10 or from 10 to 1,000.

## Solving for the full inference loop

BDN is built to distribute any content across model serving infrastructure, not just model weights. The same architecture accelerates container images, training checkpoints, and any model or deployment artifact.

As you iterate through the train-evaluate-deploy loop, BDN makes every handoff faster: finishing a fine-tuning run and deploying the resulting checkpoint, building a new engine for a different hardware target, scaling up a freshly promoted model version. You get faster cold starts immediately, and compounding returns throughout the entire model and deployment lifecycle.

BDN is available for all customers on [Baseten Cloud](https://www.baseten.co/deployments/baseten-cloud/) today. If you have any specific questions about how BDN works or how it can improve your scale-up times, [reach out](https://www.baseten.co/talk-to-us/) to talk to our engineers.
