---
title: Control plane vs workload plane in model serving infrastructure
topic: infra-platform
subtopic: deployment
secondary_topics:
- inference/serving
summary: Explains the control-plane/workload-plane split in model serving infrastructure.
source: baseten
url: https://www.baseten.co/blog/control-plane-vs-workload-plane-in-model-serving-infrastructure/
author: Colin McGrath; Matt Howard; Philip Kiely
published: '2024-05-30'
fetched: '2026-07-11T04:09:39Z'
classifier: codex
taxonomy_rev: 1
words: 909
content_sha256: 63e81f1c9f66d7e74219b347b6a872abedad6555caa4debf02825ed4e7f1b06b
triage: keep
skip_reason: null
---

# Control plane vs workload plane in model serving infrastructure

![Control plane vs workload plane](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1747441283-control-vs-workload.png%3Fauto%3Dformat%26fit%3Dcrop%26h%3D630%26w%3D1200&w=3840&q=100)

Building worldwide multi-cloud AI model serving infrastructure requires powerful-but-flexible abstractions. One of the core abstractions in Baseten’s infra architecture is the idea of a **control plane** and **workload planes**. Both the control and workload planes are Kubernetes clusters, but they follow a strict separation of concerns:

- The - **control plane**is a single Kubernetes cluster that serves as the backend for Baseten’s user interface and model management API endpoints. It’s also responsible for building model serving images, deploying them to the workload planes, and balancing load across workload planes.
- The - **workload planes**are collections of GPU resources for running model inference. These clusters can be set up in arbitrary cloud environments and regions so long as they have GPU availability.

The general idea of separating data from control or workers from a centralized decision maker is nothing new. Google’s [API design spec](https://google.aip.dev/111) describes a management plane and a data plane. [Networking routers](https://www.cloudflare.com/learning/network-layer/what-is-the-control-plane) have a control plane and data plane. Within a cluster, [Kubernetes](https://kubernetes.io/docs/concepts/overview/components/) has a control plane and worker nodes. Our design follows these patterns by separating some data and tasks into workload planes while centralizing oversight in the control plane.

![Architecture diagram for Baseten's multicluster model serving infra.](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1717026320-image3.png%3Fauto%3Dformat%26w%3D1200&w=3840&q=75) Architecture diagram for Baseten's multicluster model serving infra.

Architecture diagram for Baseten's multicluster model serving infra.In this architecture overview, we show how this common pattern expands to enable multi-cloud, multi-region model serving infrastructure and support single-tenant and self-hosted model inference workloads.

## Why separate control and workload planes

Before we dive into architecture, let’s discuss motivation. Why not just run everything in one big cluster?

A multicluster architecture with multiple workload planes solves several customer and operational challenges:

- **Regional preference and colocation:**to meet regional latency requirements and comply with data residency laws.
- **GPU availability:**by spreading workloads across regions and clouds, we’re able to get better pricing and more GPUs.
- **Self-hosted model inference:**by deploying workload planes within customers’ VPCs for security, control, and access to reserved instances.
- **Scaling with customer demand**: to meet the inference needs of hundreds of customers without facing cluster size restrictions.

And we can do all of this without replicating the compute and maintenance overhead of operating a new control plane for each workload plane deployment. Instead, the single centralized control plane orchestrates workload planes across regions, cloud providers, and cloud accounts.

## Control plane resources and responsibilities

The control plane is a specially managed Kubernetes cluster with four primary responsibilities:

- Maintaining a unified global view of the entire system and balancing inference load effectively across workload planes.
- Centralizing metrics and logging data from workload planes and handling communication between workload planes.
- Building model images on deployment and storing them in our registry.
- Serving as the backend for Baseten’s user interface and model management API.

In other words, the control plane is a central management system responsible for almost everything except actually running model inference. The control plane doesn’t handle inputs or outputs from model inference. This separation of concerns reduces the attack surface of the control plane, increasing the security of the entire system.

## Workload plane resources and responsibilities

Workload planes are commodity Kubernetes clusters that are lightweight and cloud-agnostic. Workload planes are responsible for:

- Running model inference on dedicated GPUs.
- Pulling container images from the registry for model deployment.
- Balancing load, concurrency, and scale per model within the workload plane.
- Receiving state and configuration changes (such as max replica count) from the control plane and sending metrics up to the control plane.

Workload planes run a custom version of Knative serving to deploy and scale models within the Kubernetes cluster. While workload planes don’t have the system-wide responsibility of the control plane, they are responsible for operating their workloads in a balanced, efficient manner.

One challenge for workload planes is loading container images from a registry. Workload planes use a pull-through cache to reduce cold start times. Then, the local Knative load balancer makes local auto-scaling decisions within specified parameters.

## Workload planes are not fungible

We want to treat the workload planes in as standardized a manner as possible. The control plane should be agnostic toward workload planes. But it must still be aware of each workload plane’s unique capabilities for accurate global load balancing.

Workload planes are commoditized, but not fully fungible. Each GPU cluster is affected by cloud-specific and region-specific factors, including:

- GPU type, capacity, and availability (e.g. only some regions have H100 GPUs)
- Datacenter location, which matters for both latency and data residency compliance
- Hardware cost, which varies by cloud and region
- Special configurations for data security, residency, and compliance requirements

These variables, especially configurations for data security, also apply when setting up self-hosted workload planes.

## Control and workload planes in action

Building multi-region, multi-cloud AI model serving infrastructure is complicated. Different clouds and regions have varying capabilities and GPU availability as well as subtle differences in how they operate.

Using the “control and workload plane” abstraction doesn’t remove that complexity. But the separation of concerns allows each workload plane to adjust to the specific environment it’s running in while the control plane optimizes the system globally. This unlocks benefits from reducing latency in regions like Australia to simplifying the setup of self-hosted model inference.

Learn more about [the benefits of globally distributed model serving infrastructure](https://www.baseten.co/blog/the-benefits-of-globally-distributed-infrastructure-for-ml-model-serving/) or [get in touch to discuss](https://www.baseten.co/talk-to-us/) your model serving infra needs.
