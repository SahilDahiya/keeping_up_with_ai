---
title: MAI-Thinking-1 is coming to Baseten
kind: blog
topic: null
subtopic: null
secondary_topics: []
summary: null
triage: null
skip_reason: null
source: baseten
url: https://www.baseten.co/blog/mai-thinking-1
author: Marylise Tauzia
published: '2026-06-02'
fetched: '2026-11-12T06:14:54Z'
classifier: null
taxonomy_rev: 2
words: 744
content_sha256: 8bb2c2d31f13cade5122201ed3f4eab880af9886e8e95fcba3dfc6ee44a97387
---

# MAI-Thinking-1 is coming to Baseten

AI models
# MAI-Thinking-1 is coming to Baseten

Giving control back to our customers who want to own their intelligence


- Authors
- Date
- June 2, 2026

TLDR

Today, Baseten and Microsoft AI (MAI) are announcing that MAI-Thinking-1 is coming to Baseten. MAI-Thinking-1 is Microsoft AI’s new flagship reasoning model built for AI teams who are done compromising between capability and control. MAI-Thinking-1 is a commercial-grade model with clean data lineage and post-training customization options. It is unique because it sits at a new point in the AI landscape: between open-source models which give you full control but require you to own the full stack, and closed proprietary models that you can fine-tune to your use case but that live on the lab’s infrastructure, under their terms and subject to their roadmap.

The current AI market offers two flavors of models, each with a fundamental catch:

1. Open-source models give you the freedom to customize them to your special use case but they come with the burden of serving infrastructure, optimization, security, and ongoing maintenance. In addition, they often come with concerns about cleanliness of the data that was used to train those models.
2. On the other hand, closed proprietary models give you a managed API, that enables you to customize their model to your use case but the tradeoffs are significant: the lab can often see your data, can train on your usage, and they control your roadmap. When they deprecate a model or change their terms, your application changes with it which makes you a customer of someone else's intelligence layer.

Microsoft AI built MAI-Thinking-1 and is partnering with Baseten to occupy the space in between. We give you the control and data integrity of open-source customized models, with the managed infrastructure and enterprise guarantees of a closed model.

Key characteristics of MAI-Thinking-1 include:

- Clean data: MAI-Thinking-1 was trained from the ground up on curated, high-integrity data with zero distillation from third-party models. You get access to data lineage that is clean, auditable, and commercially safe. And for enterprises operating in regulated industries or with strict IP policies, this matters enormously as you can reason about what went into the model in a way you simply can't with distilled data.
- Commercial grade by design: MAI-Thinking-1 was designed to be commercial grade from the ground up which means that Microsoft will keep their eyes completely off your model. Your fine-tuning data, your feedback signals and your domain adaptations will not go back to Microsoft. Your intelligence stays yours.
- Efficiency built in: MAI-Thinking-1 is a mid-sized model architected for efficiency, with 35B active parameters. The result is a strong return on tokens. It offers meaningful capability at a cost curve that makes production deployment viable at scale.

MAI-Thinking-1 can be shaped to the specific vocabulary, reasoning patterns and edge cases of your workflow and we are offering you customization paths depending on what works best for your team. Baseten will have access to MAI-Thinking-1’s model weights to enable optimization and customization. Baseten will operate the models in a highly secure, enterprise-grade environment. Fine-tuning will be available on these weights through Baseten for all our customers.

And this structure matters. When other closed-model providers offer fine-tuning APIs, your checkpoint still lives on their infrastructure, under their terms, subject to their roadmap. One deprecation notice and your customization is at risk. With MAI-Thinking-1 on Baseten, the fine-tuned checkpoint is yours to control, the distribution channel is independent from the model creator, and Microsoft has no visibility into what you build on top.

In order to support your fine-tuning needs, Baseten recently released [Loops](https://www.baseten.co/blog/introducing-the-baseten-loops-sdk/): Baseten's training SDK built for iterative, production-quality post-training workflows. It supports long-sequence fine-tuning, reinforcement learning from human feedback, and async RL pipelines without pipeline stalls. You define the training logic and Loops will handle the infrastructure. And a single command enables you to deploy your checkpoint directly to the Baseten inference stack.

Baseten and Microsoft are partnering to ensure that AI-enabled businesses can stay in business because they can own their intelligence rather than rent it indefinitely from a lab whose incentives may not align with theirs. We are building together a frontier ecosystem where the businesses building on AI stay in control of what they've built.

MAI-Thinking-1 will be available on Baseten soon. If you are interested in testing it, submit an application for early access from our [model library page](https://www.baseten.co/library/mai-thinking-1/) and we will be in touch!
