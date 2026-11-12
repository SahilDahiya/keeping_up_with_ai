---
title: Baseten brings AI video to life on Nebius
kind: blog
topic: inference
subtopic: serving
secondary_topics:
- infra-platform/gpu-clusters
summary: 'Describes the serving architecture for a custom text-to-video system on
  Nebius capacity: modality-specific kernels, kernel fusion, request prioritization,
  topology-aware multi-node parallelism, and SLA-aware autoscaling for predictable
  P90/P99 latency.'
triage: null
skip_reason: null
source: baseten
url: https://www.baseten.co/blog/ai-video-nebius-baseten-inference-stack
author: Mike Bilodeau
published: '2025-10-06'
fetched: '2026-11-12T06:10:34Z'
classifier: claude
taxonomy_rev: 2
words: 853
content_sha256: eca37fd1745ca172e761b206f8f126c88e71cab1cecb711c7cd0758e9a6d31ac
---

# Baseten brings AI video to life on Nebius

Infrastructure
# Baseten brings AI video to life on Nebius

Video generation workloads are long-running, consume a lot of memory, and require stable scaling. Baseten and Nebius deliver the infrastructure they demand.


- Authors
- Date
- October 6, 2025

TLDR

Baseten runs a custom text-to-video system on Nebius using the Baseten Inference Stack. The Inference Runtime uses custom modality-specific kernels, kernel fusion, attention kernels, continuous batching, request prioritization, and topology-aware parallelism. The Inference-optimized Infrastructure provides intelligent request routing, geo-aware load balancing, SLA-aware autoscaling, and fast cold starts, plus active-active reliability and multi-cloud capacity management. The outcome: predictable P90/P99 latency, high utilization, and stable uptime on Nebius capacity.

Text-to-video is not a simple extension of another modality. It's a complex workload that runs longer, stresses memory, and can create scaling challenges due to large requests demanding up to an entire node. Users notice slight shifts in latency and quality. The only way to meet that bar in production is to treat performance, reliability, and cost as one system.

The [Baseten Inference Stack](https://www.baseten.co/resources/guide/the-baseten-inference-stack/) provides the primitives to do this cleanly, then lets us place that system on  Nebius, so capacity is where we need it when demand spikes.

We start by looking at the Model Runtime. For video generation, we select modality-specific kernels that understand image and video execution patterns. We rely on custom kernels that are optimized for the memory patterns that video workloads demand. Kernel fusion helps us fuse smaller operations, and we use specific attention kernels that balance quantization and quality specifically for video workloads. Asynchronous compute helps the device stay busy rather than waiting on each launch.

We use request prioritization to prevent long-running generations from pushing up tail latency, allowing urgent requests to move ahead in the queue. When the model spans multiple devices, we apply topology-aware parallelism and scale to multi-node inference, while minimizing communication overhead. The net effect is steady step time and higher effective frames per GPU second.

Performance only matters if we can deliver it every hour of the day. The Inference-optimized Infrastructure is the other half of the stack, and it is where Nebius shows up.

Intelligent request routing directs work to replicas that have processed the user's workload and have cached elements, to reduce time-to-output and reduce redundant computation. Geo-aware load balancing keeps traffic close to users and in Nebius regions with sufficient headroom. Autoscaling expands capacity when traffic rises and contracts when it falls. Policies are SLA-aware and are paired with fast cold starts, so new replicas contribute within the SLO, not after the spike has passed. In multi-stage systems, we use independent component scaling so that no single step becomes the bottleneck.

Reliability is continuous rather than reactive. We operate with active-active reliability and cross-cloud orchestration, ensuring that a zone or provider event does not result in user impact. [Multi-cloud Capacity Management](https://www.baseten.co/blog/how-we-built-multi-cloud-capacity-management/) treats Nebius as a first-class pool within a single control plane. That gives us elasticity for launches and a clean way to manage cost when traffic normalizes.

Text-to-video often benefits from interactive or streaming behavior. The stack supports protocol flexibility across HTTPS, WebSockets, and gRPC. That lets us stream progress and control long-running requests without bolting on a side channel. The same traffic paths are used in staging and production, which ensures consistent behavior across environments.

Production success is measured, not assumed. We track total request latency and per-step denoising times with P90/P99 targets. We monitor utilization to avoid overprovisioning during regular periods and under-provisioning during bursts, and alerting is aligned with these goals, so actions are tied to impact. When a change in weights or parameters shifts behavior, the runtime and the control plane surface it quickly, and the autoscaler adapts.

Ingress receives the request. Intelligent request routing selects a Nebius region with geo-aware load balancing, ensuring optimal performance. The request is directed to pre-warmed replicas running the modality-specific runtime. Continuous batching and request prioritization maintain the latency envelope while custom kernels and asynchronous compute execute the denoise loop.

Autoscaling evaluates live signals with SLA-aware policies and adjusts Nebius capacity using fast cold starts. If additional headroom is required, our Multi-cloud Capacity Management system enables capacity to be scaled across providers without requiring application changes.

Nebius provides large GPU pools and low-friction capacity growth. The Baseten Inference Stack converts that capacity into consistent latency and reliable throughput. The runtime raises raw performance through custom kernels, kernel fusion, and modality-specific runtimes. The infrastructure layer turns that performance into a property of the service through intelligent request routing, geo-aware load balancing, autoscaling, fast cold starts, and active-active reliability. The result is a text-to-video system that delivers the same experience at noon on a Tuesday and during a creator surge on a Saturday night.

Shipping video generation is a systems challenge. The Baseten Inference Stack provides the runtime and control plane to solve it. Nebius gives us the capacity to scale it. Together, we achieve predictable P90/P99 latency, strong utilization, and uptime that remains steady as traffic fluctuates. That is what turns a demo into a product.

Experience Baseten Inference for yourself and [apply](https://www.baseten.co/talk-to-us/fall-into-inference/) to receive up to $10k in credits!
