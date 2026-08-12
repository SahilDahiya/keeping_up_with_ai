---
title: Fireworks Dev Day 2025 Wrapped
kind: blog
topic: null
subtopic: null
secondary_topics: []
summary: null
triage: null
skip_reason: null
source: fireworks
url: https://fireworks.ai/blog/fireworks-ai-dev-day-2025
author: null
published: '2025-05-29'
fetched: '2026-08-12T06:29:08Z'
classifier: null
taxonomy_rev: 2
words: 886
content_sha256: 9b5ab8a1cf4b04ea6751d53e3badfeefdd0451bd88568f802d8d2f771c3338a2
---

# Fireworks Dev Day 2025 Wrapped

Yesterday (May 28th), we hosted our very first Fireworks DevDay, and what an incredible day it turned out to be. Set against the vibrant backdrop of San Francisco, we brought together some of the brightest minds in AI and hundreds of developers who are pushing the boundaries of what’s possible with open-source models. It wasn’t just an event, it was a celebration of progress, speed, and the collective ambition to reimagine what AI can do in production.

Our keynote fireside chats were raw, insightful, and deeply inspiring. They weren’t just high-level vision talks, they were grounded in real engineering challenges and solutions.

- •**Sarah Sachs (Head of AI Engineering, Notion)** shared how her team is making fast, thoughtful decisions about model size and latency to create delightful user experiences in Notion AI.

- •**Adarsh H. (Co-founder, CTO, Mercor)** revealed how their recruiting agents are outperforming closed models on niche tasks, a powerful proof point for the promise of open weights.

- •**Tony Wu (VP of AI, Perplexity)** walked us through how deep research agents can be built entirely with open-source models, without compromising on quality or relevance.

- •**Malte Ubl (CTO, Vercel)** spoke about crafting a feedback loop that enables rapid iteration and a smooth coding UX in Vercel's latest AI features.

At Fireworks, we believe developers should have the power to explore, iterate, and ship without waiting on infrastructure. We launched several powerful updates to help make that vision real.

- •[**Experiment Platform (GA)**](https://app.fireworks.ai/models) : Iteration bottlenecks kill momentum. Our new Experiment Platform, now generally available, provides immediate access to 1000s of models, removes GPU access hurdles and gives developers the freedom to run experiments instantly. It's available in both multi-tenant and enterprise single-tenant setups, so you can build fast, whether you're an indie hacker or an AI platform team at a Fortune 500 company.
- •[**Build SDK (Beta)**](https://docs.fireworks.ai/tools-sdks/python-client/sdk-introduction) : For teams that want to move programmatically, we launched the Build SDK. With just a few lines of code, you can trigger fine-tuning jobs, run evaluations, deploy to inference, and scale up or down as needed.

- •[**Supervised Fine-Tuning v2**](https://docs.fireworks.ai/fine-tuning/fine-tuning-models) : We’ve made significant enhancements to supervised fine-tuning, supporting longer context lengths, quantization-aware training and faster training. This updates make Fireworks the easiest place to fine-tune large models like Llama and DeepSeek for high-quality performance at scale.
- •[**Reinforcement Fine-Tuning (Beta)**](https://docs.fireworks.ai/fine-tuning/reinforcement-fine-tuning-models) : Fireworks is making the power of reinforcement learning accessible to all developers.. Use reinforcement learning to make deep changes to model behavior by specifying evaluations. We support composable pipelines that allow you to start with supervised tuning, layer in reward-based tuning, and evaluate using custom metrics. Our reward-kit SDK and test-run interface help you easily build, and utilize reward functions without the friction.

- •**Vision Platform Enhancements:** We now support leading multimodal models like Qwen2.5-VL, Llama4 Maverick, and Phi-3.5 Vision. Fireworks’ proprietary serving stack provides fast, efficient inference for these models and lets you compose vision and text models for advanced, reasoning-intensive use cases
- •**(Beta) Voice Agent Platform** : Fireworks is offering voice agents with real-time latency, proprietary quality improvements and simple implementation through one provider. Voice agents include:
  - •**Fireworks ASR** , which outperforms industry leaders against our tests on clean and noisy data.
  - •**Fireworks TTS** , with realistic, steerable voices.
  - •**Fireworks Voice Agents platform** launching bringing together Fireworks ASR, LLM, TTS in an easy-to-use, customizable interface
- •

- •[**Global Virtual Cloud**](https://app.fireworks.ai/dashboard/deployments/create) : Running GPUs at scale is notoriously brittle. Every provider has quirks, and staying resilient takes work. Fireworks abstracts GPU infrastructure across 8 major clouds, both hyperscalers and neoclouds, giving you one consistent interface. Choose from 18 regions worldwide, including EMEA and Asia, to get compute close to your users. For customers with stringent security needs, Fireworks can deploy directly into your VPC, ensuring compliance with enterprise-grade data and infrastructure requirements.

- •**3-D Optimizer (v2)** : We demoed our intelligent tuning engine that balances**quality, speed, and cost** . 3-D Optimizer automatically identifies the pareto frontier for your workload, and lets you choose what matters most, whether it's faster responses, better completions, or lower costs.

- •**B200 + FP4 Inference** : We announced support for**NVIDIA B200s** in dedicated deployments. B200 enables peak throughput up to**300 tokens/sec** for DeepSeek models. Coupled with**FP4 quantization-aware training** , we now match closed model inference quality with open models, at a fraction of the cost. We’ve already seen**3-4x faster throughput** in production pilots.

We’re powering [DeepSeek V3](https://fireworks.ai/models/fireworks/deepseek-v3) with 264 tokens/second on B200, placing us as the industry leader for output speed and cost-efficiency, [based on benchmarks by Artificial Analysis.](https://artificialanalysis.ai/models/deepseek-v3-0324/providers#output-speed-over-time-deepseek-v3-mar-25-providers)

Use new virtual cloud features directly when [deploying](https://app.fireworks.ai/dashboard/deployments/create) or contact us more enterprise features

Fireworks DevDay wasn’t just a celebration, it was a commitment to supporting builders with the fastest, most flexible infrastructure for open AI development.

If you’re building AI agents, tuning foundation models, or pushing into multimodal territory, we’re building the platform to support you.

Workshops, new model drops, expanded agentic tooling, it’s all coming.

Want to start building today? [Explore what’s new at](https://fireworks.ai/) [fireworks.ai](https://fireworks.ai/)

Stay tuned for more updates and details about our demos.

Follow us on [LinkedIn](https://www.linkedin.com/company/fireworks-ai) or X to receive all of our latest updates 💜

**Notes:** Some announcements are available only through early access. Reach out to your Fireworks representative or aisrinivasan@fireworks.ai  if you'd like early access
