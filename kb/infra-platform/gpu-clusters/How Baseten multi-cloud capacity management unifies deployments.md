---
title: How Baseten multi-cloud capacity management unifies deployments
topic: infra-platform
subtopic: gpu-clusters
secondary_topics: []
summary: Explains multi-cloud capacity management for unifying cloud, self-hosted,
  and hybrid inference deployments.
source: baseten
url: https://www.baseten.co/blog/how-baseten-multi-cloud-capacity-management-mcm-powers-cloud-self-hosted-and-hybr/
author: Rachel Rapp; Amir Haghighat
published: '2025-06-09'
fetched: '2026-07-11T04:08:00Z'
classifier: codex
taxonomy_rev: 1
words: 1125
content_sha256: 9a346b9971e5b5e948340832ea5c3bad898bf0edafff5bdbacb7aceeac612b36
triage: keep
skip_reason: null
---

# How Baseten multi-cloud capacity management unifies deployments

![Baseten multi-cloud capacity management](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1749508224-text-template-1.png%3Fauto%3Dformat%26fit%3Dcrop%26h%3D630%26w%3D1200&w=3840&q=100)

**Baseten's MCM system** is a unified control layer that provisions and scales thousands of GPUs across 20+ clouds and regions. Three deployment modes share the same inference stack:

- **Baseten Cloud**– fully managed, multi-cloud scale and latency optimisation.
- **Self-hosted**– the full stack inside your VPC for strict data, security, or customization needs.
- **Hybrid**– run core workloads self-hosted and burst to Baseten Cloud on demand.

Delivers 99.99 % uptime, lowest-possible latency, data-residency compliance (SOC 2 Type II, HIPAA, GDPR) and freedom from vendor lock-in.

At Baseten, we operate one of the most complex inference infrastructures in production today—thousands of GPUs distributed across 20+ cloud providers and multiple regions globally. This scale exposed fundamental limitations in traditional deployment approaches: single points of failure, regional and cloud-specific capacity constraints, and the operational nightmare of managing heterogeneous cloud environments.

We built our multi-cloud management (MCM) system to address these problems for our diverse customer base. Our MCM system is a set of automation, tools, and practices designed to manage compute across different cloud service providers (CSPs) from a single pane of glass. It comprises the core of the Baseten Inference Stack. We've used it for the past two years to power production workloads for Abridge, Writer, Patreon, and hundreds of others.

![Description: Baseten supports Cloud, Self-hosted, and Hybrid deployments with Multi-cloud Capacity Management (MCM) for cloud-agnostic provisioning, orchestration, and scaling of resources.](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1749508393-overall_infra_diagram.png%3Fauto%3Dformat%26w%3D1200&w=3840&q=75) Baseten supports Cloud, Self-hosted, and Hybrid deployments with Multi-cloud Capacity Management (MCM) for cloud-agnostic provisioning, orchestration, and scaling of resources.

Baseten supports Cloud, Self-hosted, and Hybrid deployments with Multi-cloud Capacity Management (MCM) for cloud-agnostic provisioning, orchestration, and scaling of resources.We designed the MCM system for maximum flexibility, enabling customers to run in our cloud, their cloud, or a combination of both. This gives our customers a huge advantage in quickly accessing the latest hardware and using their existing GPU fleets. In addition, it enables them to rapidly bring compute online when a capacity crunch occurs, regardless of their deployment type.

With our MCM system, we deliver customers a unique level of service featuring:

- High uptime (99.99%) through - __active-active reliability__
- The lowest possible latency through flexible compute allocation
- Data residency and sovereignty requirements
- SOC 2 Type II, HIPAA, and GDPR compliance

Below, we break down the details of the Baseten Cloud, Self-hosted, and Hybrid deployment options, how our MCM system powers them, and when to use each.

## Baseten Cloud: Fully-managed inference 

Unlike single-cloud solutions, Baseten Cloud was built from the ground up to run seamlessly across clouds, delivering consistent performance regardless of CSP, region, or workload-specific requirements. Our MCM system enables us to provision and manage compute globally across any hyperscaler or neocloud. This allows customers to avoid vendor lock-in while optimizing for latency, GPU availability, and cost.

By default, we never store model inputs, outputs, or weights to ensure security and compliance. Caching weights is optional, and you can permanently erase them at any time. Our [ geography-based routing](https://www.baseten.co/resources/guide/the-baseten-inference-stack/#intelligent-request-routing) enables compliance with data sovereignty laws (we can constrain deployments to specific regions to meet data residency requirements), and all requests are sent directly to workload planes without going through any intermediary control plane.

![Baseten Cloud is fully managed with limitless scale, making it the fastest path to performant, reliable, and cost-efficient production inference.](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1749508476-cloud.png%3Fauto%3Dformat%26w%3D1200&w=3840&q=75) Baseten Cloud is fully managed with limitless scale, making it the fastest path to performant, reliable, and cost-efficient production inference.

Baseten Cloud is fully managed with limitless scale, making it the fastest path to performant, reliable, and cost-efficient production inference.## Baseten Self-hosted: Fast inference with full control 

Since our MCM system sits at the foundation of our Cloud, our resource provisioning and management capabilities work identically whether resources reside in our cloud or yours. This makes Baseten Self-hosted (launched in early 2024) a natural extension of our existing infrastructure.

For teams with strict data security, privacy, or infrastructure requirements, Baseten Self-hosted provides full access to our platform within your own cloud environment. You get all the advantages of the Baseten Inference Stack—kernel and runtime performance, routing, autoscaling, and observability—while maintaining complete control over your data, compute, and networking.

Self-hosting ensures that no data ever leaves your environment. You know exactly where your data is processed, how it flows, and who has access. Inputs and outputs never get stored or shared, offering extra peace of mind for teams working with sensitive IP or regulated workloads.

Choose Baseten Self-hosted when you need to:

- Comply with strict customer, industry, or in-house compliance requirements
- Fully customize your infrastructure
- Maximally utilize existing cloud credits or commitments

![Baseten Self-hosted provides full access to the Baseten Inference Stack while maintaining complete control over your data, compute, and networking.](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1749508511-self-hosted.png%3Fauto%3Dformat%26w%3D1200&w=3840&q=75) Baseten Self-hosted provides full access to the Baseten Inference Stack while maintaining complete control over your data, compute, and networking.

Baseten Self-hosted provides full access to the Baseten Inference Stack while maintaining complete control over your data, compute, and networking.## Baseten Hybrid: Full control with flex capacity

While some teams require self-hosting for data residency or stringent compliance requirements, self-hosting alone often can’t accommodate traffic bursts. This results in a trade-off between control and flexibility that becomes difficult to manage without over-provisioning.

Baseten Hybrid removes this constraint by combining self-hosted control with optional, elastic spillover to Baseten Cloud. You define where your workloads run: whether entirely in your cloud, or with dynamic routing to Baseten Cloud when demand spikes.

For customers with large pre-existing cloud commitments, Baseten Hybrid allows you to utilize your commitments while retaining access to on-demand flex capacity. And (of course) it’s also powered by the Baseten Inference Stack for high performance, reliability, and cost-efficiency.

Our customers use Baseten Hybrid to:

- Self-host sensitive workloads
- Spend down existing cloud commitments
- Unlock dynamic autoscaling with on-demand flex compute

![Baseten Hybrid lets you self-host sensitive workloads with on-demand flex capacity on Baseten Cloud to meet extra demand.](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1749508536-hybrid.png%3Fauto%3Dformat%26w%3D1200&w=3840&q=75) Baseten Hybrid lets you self-host sensitive workloads with on-demand flex capacity on Baseten Cloud to meet extra demand.

Baseten Hybrid lets you self-host sensitive workloads with on-demand flex capacity on Baseten Cloud to meet extra demand.## Comparing deployment options: Cloud vs. Self-hosted vs. Hybrid

Consistently achieving demanding targets for latency, throughput, uptime, and cost in production requires a holistic view of inference across applied performance research and distributed infrastructure. Our MCM system and the Baseten Inference Stack give you all of these capabilities out of the box, while leaving you with full visibility and control over how your deployments are configured—across our cloud or yours.

If you’re wondering whether you should self-host, use a managed solution, or something in between, you can [ talk to our engineers](https://www.baseten.co/talk-to-us/) about which deployment option makes the most sense for your workloads.
