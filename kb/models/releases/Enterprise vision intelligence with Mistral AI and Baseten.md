---
title: Enterprise vision intelligence with Mistral AI and Baseten
kind: blog
topic: models
subtopic: releases
secondary_topics: []
summary: Mistral AI's Mistral Large 3 (675B MoE vision-language model, Apache 2.0)
  plus the 3B/8B/14B Ministral family, with a 256k context window and vision input
  aimed at KYC document verification, structured extraction, and visual QA use cases.
triage: null
skip_reason: null
source: baseten
url: https://www.baseten.co/blog/enterprise-vision-intelligence-with-mistral-ai-and-baseten
author: Philip Kiely
published: '2025-12-02'
fetched: '2026-11-12T06:10:46Z'
classifier: claude
taxonomy_rev: 2
words: 721
content_sha256: 1e4081366db53e4064209b10d81a1d8d67614fe40f9d72b57d5738a5a239b786
---

# Enterprise vision intelligence with Mistral AI and Baseten

AI engineering
# Enterprise vision intelligence with Mistral AI and Baseten

Mistral 3 is Mistral AI's new open model, licensed for commercial use under Apache 2.0, built for daily tasks in the enterprise with vision input capabilities.


- Authors
- Date
- December 2, 2025

TLDR

Mistral AI launched a new family of open models: Mistral 3, a 675B-parameter MoE vision-language model, along with Ministral models at 3B, 8B, and 14B sizes. These new open models are licensed for commercial use under Apache 2.0 and are strong daily drivers for enterprises and companies in regulated industries looking for frontier intelligence from a trusted lab. With Baseten, enterprises can deploy Mistral AI models at scale with leading performance and efficiency.

[Mistral Large 3 675B Instruct 2512](https://huggingface.co/mistralai/Mistral-Large-3-675B-Instruct-2512) is a new multimodal open model by Mistral AI. With an Apache 2.0 license permitting commercial use, Mistral Large 3 is a new foundation model for enterprises to build on and adapt to handle vision-language use cases.

Mistral Large 3 has vision input capabilities, making it useful for:

- **KYC (Know Your Customer):** Automating identity verification with images of ID cards with Mistral Large 3’s visual processing capabilities.
- **Structured Document Extraction:** Converting non-standard PDFs, invoices, and handwritten forms into structured JSON. Mistral Large 3’s instruction-following capabilities make it superior for adhering to rigid output schemas.
- **Visual QA:** Deploying a fine-tuned Ministral model to spot defects in real time thanks to low-latency inference on Ministral models.
- **Insurance Claims Processing:** Analyzing photos of vehicle or property damage to generate initial repair estimates.
- **Content Moderation:** Protecting platforms by automatically detecting and filtering unsafe user-generated images at scale.

Additionally, the model supports tool calling and JSON output, making it a great daily driver for all forms of agentic AI in the enterprise. Mistral Large 3 is built for long context processing (256k-token context window) with rigorous adherence to the system prompt and support for dozens of languages including English, French, Spanish, German, Italian, Portuguese, Dutch, Chinese, Japanese, Korean, and Arabic.

Baseten is offering [dedicated deployments for Mistral Large 3 2512](https://www.baseten.co/library/mistral-large-3-2512/) on NVIDIA Blackwell B200 GPUs as part of our [enterprise inference platform](https://www.baseten.co/enterprise/).

With Mistral AI, every engineer can access frontier open intelligence with the consistency and reliability that enterprises demand in AI workloads. This release continues a consistent pattern that has emerged in the ecosystem between closed and open models:

- Closed models continuously improve, delivering new frontiers in intelligence that unlock new capabilities for AI-powered products.
- Open models cross the gap fast, enabling the same capabilities with lower costs and latencies.
- Many companies fine-tune open models to cross the gap sooner or even exceed closed models in domain-specific tasks.

As new capabilities became possible — voice agents, customer-support copilots, AI IDEs, code assistants — companies first build with closed models, then transition to open models for cost, latency, control, and specialization. This pattern has repeated across every vertical, from healthcare to financial services to technology.

Mistral Large 3 is a new foundation for the next step in this cycle. Mistral Large 3 can reliably handle complex tasks across document processing, content moderation, agentic systems, and more, clearing the path for enterprises to deploy open models at scale on products that were previously limited to closed models.

In addition to the main Mistral Large 3, Mistral AI also released a [new Ministral 3 collection](https://huggingface.co/collections/mistralai/ministral-3) of models at 3B, 8B, and 14B parameters.

These models, while capable out of the box, are a great base for post-training for specific workloads. With [Baseten Training](https://www.baseten.co/blog/baseten-training-is-ga/), you can use SFT and RL to adapt Ministral 3 models to your data and tasks.

Mistral Large 3 is an incredibly promising new foundation model for enterprise. But to use it in production, your deployments need to be fast, reliable, and scalable.

Mistral Large 3 runs best on an 8xB200 setup, using a full node of NVIDIA Blackwell B200 GPUs to store the model’s 675 billion parameters in FP8 or NVFP4. As Mistral AI points out in the model card, “due to its large size and architecture, the model can be challenging to deploy efficiently with constrained resources or at scale.”

Baseten [solves those challenges for the enterprise](https://www.baseten.co/enterprise/) with best-in-class [model performance](https://www.baseten.co/platform/model-performance/), [multi-cloud capacity management](https://www.baseten.co/blog/how-we-built-multi-cloud-capacity-management/#what-is-mcm-isnt-it-just-another-multi-cloud-solution), and [self-hosted inference](https://www.baseten.co/deployments/baseten-self-hosted/). Get started with [dedicated deployments for Mistral Large 3 2512](https://www.baseten.co/library/mistral-large-3-2512/) on Baseten today.
