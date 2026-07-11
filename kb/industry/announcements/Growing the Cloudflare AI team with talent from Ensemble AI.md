---
title: Growing the Cloudflare AI team with talent from Ensemble AI
topic: industry
subtopic: announcements
secondary_topics:
- inference/optimization
summary: Ensemble AI's team joins Cloudflare's Workers AI to improve inference economics,
  bringing NdLinear — a drop-in linear-layer replacement operating on multidimensional
  activations to cut parameters and compute — and NdLinear-LoRA for parameter-efficient
  fine-tuning, complementing Infire and Unweight.
source: cloudflare-ai
url: https://blog.cloudflare.com/ensemble-ai-talent-joins-cloudflare/
author: Alex Reneau
published: '2026-06-15'
fetched: '2026-07-11T04:12:56Z'
classifier: claude
taxonomy_rev: 1
words: 685
content_sha256: 0ad6fa9222e8eb0d54388990bac6f88b15780cdf151e8b9a516d68739c6231f8
---

# Growing the Cloudflare AI team with talent from Ensemble AI

Today, we’re excited to share that key members of the team at Ensemble AI are joining Cloudflare to help accelerate our work in AI infrastructure and make it easier for developers to run powerful AI models efficiently at scale.

Ensemble AI, founded in 2023 in San Francisco, has spent the last few years focused on one of the most important challenges in AI: making large models faster, smaller, and more cost-effective to serve, without sacrificing quality. The team has developed new approaches to model compression and efficient inference that are designed to reduce the memory, compute, and deployment overhead of large language models and multimodal architectures.

As AI becomes a core part of how developers build applications, the economics of inference matter more than ever. Models are getting larger; workloads are becoming more dynamic. And customers increasingly expect AI to be available everywhere: globally distributed, fast, reliable, and affordable. Bringing the Ensemble AI team into Cloudflare strengthens our ability to make that possible.

The team at Ensemble AI has focused on preserving the structure inside modern AI models while reducing the cost of running them. Instead of treating model efficiency as only a [ quantization](https://www.cloudflare.com/learning/ai/what-is-quantization/) or hardware problem, Ensemble has explored new model building blocks that can make neural networks more compact and efficient at the architectural level.

A core part of this work is [ NdLinear](https://github.com/ensemble-core/ndlinear), a drop-in replacement for standard linear layers in transformer models that operates directly on multidimensional activations rather than flattening structure away. This enables models to preserve meaningful axes, such as heads, channels, spatial dimensions, or other structured representations, while reducing parameter count and compute. Ensemble has also developed NdLinear-LoRA, an efficient adaptation method designed to reduce the trainable parameters required for fine-tuning large models.

These approaches complement other efficiency techniques, including quantization and vector quantization. Together, they point toward a future where developers can run capable AI models with substantially lower memory, compute, and cost requirements.

Cloudflare Workers AI gives developers access to serverless GPU-powered inference on Cloudflare’s global network. As developers build more AI-native applications, the ability to serve models efficiently becomes a critical part of the platform.

Inference cost is one of the biggest barriers to scaling AI applications. Every improvement in model size, memory footprint, throughput, and GPU utilization can make AI more accessible to developers and more economical for customers. This is especially important as AI workloads expand beyond simple text generation into agents, multimodal models, personalization, fine-tuning, retrieval, and reinforcement learning.

We are deepening our investment in the core machine learning capabilities needed to make Workers AI faster, more flexible, and more cost-efficient. This builds on top of our existing work on improving model efficiency, including our inference engine [ Infire](https://blog.cloudflare.com/cloudflares-most-efficient-ai-inference-engine/), tensor compression techniques like

[, and our](https://blog.cloudflare.com/unweight-tensor-compression/)

__Unweight__[. The team will focus on improving the economics of serving large language models and other advanced AI architectures, with an emphasis on model efficiency, GPU utilization, and scalable deployment.](https://blog.cloudflare.com/high-performance-llms/)

__platform for running extra large language models__AI infrastructure is entering a new phase. Developers no longer need only access to models; they need infrastructure that can run models reliably, affordably, and close to users. They need the ability to experiment with different model sizes, fine-tuning approaches, and deployment patterns without being blocked by cost or operational complexity.

Cloudflare is uniquely positioned to help solve this. Our global network, developer platform, and serverless architecture give us the foundation to bring AI closer to where applications already run. The Workers AI Machine Learning Engineering team will help us improve the efficiency layer underneath that experience.

By combining Cloudflare’s global infrastructure with Ensemble’s work in model compression and efficient architectures, we can continue building a platform where developers can deploy AI applications with lower cost, better performance, and less operational overhead.

Together, we will continue building the infrastructure needed to make AI more efficient, accessible, and useful for developers everywhere. Our goal is simple: help developers run powerful AI workloads at global scale while improving the economics of inference across the Cloudflare platform. If you want to join us in our mission, check out [ our careers page](https://www.cloudflare.com/careers/jobs/).
