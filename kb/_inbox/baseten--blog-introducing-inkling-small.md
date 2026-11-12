---
title: 'Introducing Inkling-Small: small and mighty multimodal AI'
kind: blog
topic: null
subtopic: null
secondary_topics: []
summary: null
triage: null
skip_reason: null
source: baseten
url: https://www.baseten.co/blog/introducing-inkling-small
author: Albert Lee
published: '2026-09-23'
fetched: '2026-11-12T06:15:26Z'
classifier: null
taxonomy_rev: 2
words: 615
content_sha256: 0f04d13853a268352addcf0d321e9be4bfb08f746965146a75e8685ce831b100
---

# Introducing Inkling-Small: small and mighty multimodal AI

AI models
# Introducing Inkling-Small: small and mighty multimodal AI

Thinking Machines’ new Inkling-Small is now available on Baseten.


- Authors
- Date
- September 23, 2026

TLDR

Thinking Machines’ new Inkling-Small is now available on Baseten via Model APIs and Dedicated Inference. It retains the powerful multimodal capabilities and 1M-token context window of the original Inkling, but with a significantly smaller footprint that delivers reduced deployment costs and faster inference.

Thinking Machines' Inkling-Small is now available on Baseten through [Model APIs](https://app.baseten.co/model-apis/inkling-small) and [Dedicated Inference](https://www.baseten.co/library/inkling-small/), and it runs on NVIDIA accelerated infrastructure.

Earlier this month, [we launched Inkling on Baseten](https://www.baseten.co/blog/meet-inkling-thinking-machines-labs-new-model/#built-for-breadth-efficient-by-design). Inkling is a highly knowledgeable, open-weight multimodal foundation model that combines broad reasoning capabilities, long context, and efficient sparse inference, making it a flexible base for customized AI applications.

Inkling-Small retains Inkling’s compelling model characteristics, while providing faster inference and lower cost due to its smaller footprint.

At roughly one-quarter the size of Inkling, Inkling-Small leverages a sparse Mixture-of-Experts (MoE) architecture to deliver exceptional efficiency. This architecture significantly lowers VRAM requirements, which not only reduces deployment costs and allows for use on fewer GPUs, but also provides ample headroom for faster inference.

| Parameters | Inkling-Small | Inkling | 
|---|---|---|
| Total Parameters | 276B | 975B | 
| Active Parameters | 12B | 41B | 
| VRAM Required (NVFP4) | 180 GB | 600 GB | 

Inkling-Small compromises nothing in versatility, maintaining the same multimodal capabilities as Inkling. It natively processes text, image, and audio inputs and supports a 1M token context window. This makes it an ideal drop-in replacement, ensuring your applications gain the benefits of increased efficiency while preserving full reasoning and multimodal power.

| Column A | Inkling-Small | Inkling | 
|---|---|---|
| Context Length | 1M tokens | 1M tokens | 
| Text Input | ✔️ | ✔️ | 
| Image Input | ✔️ | ✔️ | 
| Audio Input | ✔️ | ✔️ | 
| Text Output | ✔️ | ✔️ | 

Inkling-Small delivers comparable performance to Inkling across reasoning, coding, vision, audio, and safety. While individual benchmark scores fluctuate slightly, the aggregate performance of Inkling-Small remains remarkably consistent with Inkling. In fact, Inkling-Small slightly outperforms Inkling across several benchmarks, demonstrating that choosing a smaller model does not require a compromise on intelligence.

| Category | Benchmark | What it measures | Inkling-Small | Inkling | 
|---|---|---|---|---|
| Reasoning | GPQA Diamond | Graduate-level scientific reasoning | 89.5% | 87.9% | 
| Coding | SWE-bench Verified | Resolving real software issues | 80.2% | 77.6% | 
| Math | AIME 2026 | Competition mathematics | 95.5% | 97.1% | 
| Vision | MMMU Pro | Multidisciplinary visual reasoning | 74.0% | 73.5% | 
| Audio | VoiceBench | Spoken-language understanding | 90.1% | 91.4% | 
| Safety | StrongReject | Resistance to harmful requests | 98.4 | 99.1% | 

Inkling-Small builds on the open-weight heritage of Inkling, offering the same level of control over your AI stack. Baseten operationalizes this flexibility, abstracting away infrastructure complexity. By using Baseten, you gain a managed environment that handles the heavy lifting, allowing you to focus entirely on your application.

By leveraging Baseten’s infrastructure, you can:

- Scale with demand: Automatically add or remove model replicas as traffic patterns shift.
- Accelerate deployment: Utilize the Baseten Delivery Network for 2–3× faster cold starts, ensuring your Inkling-Small replicas are ready instantly.
- Maintain reliability: Stay available across clouds with Baseten’s multi-cloud capacity management, ensuring your application remains online even if specific cloud resources become constrained.

Access Inkling-Small through Baseten [Model APIs](https://app.baseten.co/model-apis/inkling-small) or reach out to deploy via [Dedicated Inference](https://www.baseten.co/library/inkling-small/). Get started with Inkling-Small today and experience high-performance, efficient multimodal AI on your own terms.
