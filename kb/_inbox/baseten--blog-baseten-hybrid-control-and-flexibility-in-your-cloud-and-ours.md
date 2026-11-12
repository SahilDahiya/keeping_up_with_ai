---
title: 'Introducing Baseten Hybrid: control and flexibility in your cloud and ours'
kind: blog
topic: null
subtopic: null
secondary_topics: []
summary: null
triage: null
skip_reason: null
source: baseten
url: https://www.baseten.co/blog/baseten-hybrid-control-and-flexibility-in-your-cloud-and-ours
author: Phil Howes
published: '2024-09-26'
fetched: '2026-11-12T06:09:12Z'
classifier: null
taxonomy_rev: 2
words: 835
content_sha256: 5f89951fcd5833da589742bd9fb3c08916438e5efdf676baa298fab7351f9dd2
---

# Introducing Baseten Hybrid: control and flexibility in your cloud and ours

News
# Introducing Baseten Hybrid: control and flexibility in your cloud and ours

Baseten Hybrid is a multi-cloud solution that enables you to run inference in your cloud—with optional spillover into ours.


- Authors
- Date
- September 26, 2024

TLDR

With Baseten Hybrid, you can run sensitive workloads in your own VPC with flex compute available on-demand on Baseten Cloud. As part of our launch of Baseten Hybrid early access, we're offering special pricing from now until the end of October for companies looking to scale on their own VPC: deploy self-hosted workloads at a flat rate of $25K per region, with no additional fees for GPU utilization. Get in touch to learn more!

We’re excited to introduce early access to Baseten Hybrid, a multi-cloud solution that enables you to run inference in your cloud—with the ability to add flex capacity in ours.

We’ve seen it time and again: AI builders want to self-host some of their workloads for compliance reasons, but when traffic picks up, they need access to additional compute. With Baseten Hybrid, you have complete control over your policies and workloads while gaining true cloud elasticity: seamlessly spill over to Baseten Cloud, with zero engineering effort required.

Whether you’re using your cloud credits or negotiating your GPU commits with different cloud providers, you can bring them to Baseten while gaining the performance, scalability, and security we excel in.

No other solution on the market offers this level of multi-cloud flexibility.

Baseten Hybrid combines our two solutions for ML inference: [Self-hosted](https://www.baseten.co/blog/baseten-self-hosted/) and [Cloud](https://www.baseten.co/pricing/). Keep sensitive workloads securely on your own cloud to meet specific data residency requirements or fully utilize in-house resources. When you need extra compute, effortlessly spill over to ours. Specify regions to reduce latency and meet compliance, and do it all with zero effort to make your workloads compliant with different platforms.

Many companies label their multi-cloud solutions as "hybrid," but in reality, they just shuffle all of your workloads between public cloud providers. Instead of waiting for enough compute to run everything on one cloud, we dynamically distribute your workloads across any available capacity. You get true cloud elasticity and agnosticism, with zero time investment required; our infra takes care of that.

Gain full support and management from our team of expert engineers, with zero-downtime deployments and no-disruption infrastructure updates. Eliminate vendor lock-in while utilizing your existing GPU allocation, spend commit, and credits with cloud providers like AWS and GCP.

Gain early access to Baseten Hybrid for:

- **Meeting specific security needs.** Self-host workloads according to strict data residency requirements, IP protection, requirements from customers, or regulations that mandate that inference be run on your cloud.
- **Multi-cloud elasticity and spillover.** Enjoy the same experience of Baseten Cloud, while defining which workloads run where. Use your GPUs whenever compute is available, and spill over to our compute to maintain SLAs during traffic spikes.
- **Spend down cloud commits and avoid vendor lock-in.** Our multi-cloud solution enables enterprises to flexibly use any cloud vendor while utilizing existing GPU allocation, spend commit, and credits.
- **Blazing-fast inference.** Our ML infra is optimized for ultra-low-latency inference with elastic scale. We use the best inference optimization techniques (including TensorRT/TensorRT-LLM and vLLM) and model serving tooling, with instance- and network-level improvements for blazing-fast cold starts and end-to-end latency.
- **Compound AI systems.** Baseten Self-hosted works with any setup, including [compound AI](https://www.baseten.co/blog/introducing-baseten-chains/). Build modular, scalable, efficient pipelines using multiple models and processing steps, while optimizing GPU utilization and reducing latency.

Baseten Hybrid combines the best of Baseten Self-hosted and Baseten Cloud:

| Feature | Baseten Hybrid | Baseten Self-hosted | Baseten Cloud | 
|---|---|---|---|
| Data control | Full data control in your VPC; managed data security on Baseten Cloud | Full data control | Managed data security | 
| Performance optimization | SOTA on-chip model performance and low network latency | SOTA on-chip model performance and low network latency | SOTA on-chip model performance and low network latency | 
| Scalability | High, tailored scalability with flex capacity on Baseten Cloud | High, tailored scalability | Highly scalable, elastic compute | 
| Security and compliance | Adhere to custom policies or lean on our SOC 2 Type II and HIPAA compliance | Adhere to custom organizational policies | SOC 2 Type II certified and HIPAA compliant | 
| Utilization of existing cloud resources | Use credits or commits | Use credits or commits | Spend down existing cloud commits | 

For a more detailed comparison, check out [our guide](https://www.baseten.co/resources/guide/choosing-a-hosting-option-for-ai-model-inference/) to choosing the right deployment option for your inference workloads.

Our mission is to support companies with highly performant, reliable, and secure AI infrastructure customized to their needs. We built Baseten Hybrid to enable you to do inference in your own cloud and meet stringent security requirements—without compromising on performance. Future-proof your infrastructure against traffic bursts and maintain SLAs without additional capital expenditure.

If we can help you meet your security and compliance needs while providing necessary resources, scalability, and performance, [get in touch](https://www.baseten.co/talk-to-us/?ref=/)!
