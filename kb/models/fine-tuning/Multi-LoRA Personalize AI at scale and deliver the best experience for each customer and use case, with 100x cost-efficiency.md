---
title: 'Multi-LoRA: Personalize AI at scale and deliver the best experience for each
  customer and use case, with 100x cost-efficiency'
topic: models
subtopic: fine-tuning
secondary_topics:
- inference/serving
summary: Explains Multi-LoRA serving for personalized models at scale with better
  cost efficiency.
source: fireworks
url: https://fireworks.ai/blog/multi-lora
author: null
published: '2024-09-18'
fetched: '2026-07-11T04:13:32Z'
classifier: codex
taxonomy_rev: 1
words: 1155
content_sha256: 9c96544c0082146aa174756ce78d549dfc96dfe236eb40124d31c8c2d30daaad
triage: keep
skip_reason: null
---

# Multi-LoRA: Personalize AI at scale and deliver the best experience for each customer and use case, with 100x cost-efficiency

At Fireworks, we know how important it is for you to deliver the best product experiences to your users. Today, we’re excited to spotlight **Multi-LoRA**, a [FireOptimizer](https://fireworks.ai/blog/fireoptimizer) capability that customers have used to personalize AI at scale and deliver the best experience for each customer and use case.

**Why it matters:** Personalized experiences are critical to driving greater usage, retention and customer satisfaction for your product. Before Multi-LoRA, if you had many users, user segments or use cases to personalize for, deploying hundreds of fine-tuned models on separate GPUs would be prohibitively expensive. With Multi-LoRA, you can now deliver personalized experiences across thousands of users and use cases, without scaling your costs! 🚀

**Multi-LoRA benefits:**

- •**Fine-tune and serve hundreds of personalized LoRA models**at the same cost as a single base model, which is just $0.2/1M tokens for Llama3.1 8B
- •**100x cost-efficiency**compared to serving 100 fine-tuned models without Multi-LoRA on other platforms with per-GPU pricing
- •**Convenient deployment**on on Fireworks On-Demand and Reserved for larger workloads.

**Multi-LoRA is part of FireOptimizer**, our adaptation engine designed to customize and enhance AI model performance for your unique use cases and workload. FireOptimizer capabilities include [Adaptive Speculative Execution](https://fireworks.ai/blog/fireoptimizer), that enables up to 3x latency improvements, [Customizable Quantization](https://fireworks.ai/blog/fireworks-quantization), to precisely balance speed and quality, and [LoRA Fine-Tuning](https://fireworks.ai/blog/fine-tune-launch) to customize and improve model performance.

Companies often serve thousands of customers across multiple use cases, and want to deliver personalized experiences for each customer. [ Low-Rank Adaptation (LoRA)](https://arxiv.org/abs/2106.09685) is a popular fine-tuning technique to customize and improve model performance, by updating only a small subset of model parameters.

**Multi-LoRA** takes LoRA to the next level, by allowing you to serve hundreds of fine-tuned LoRAs on a single base model, simultaneously, at the same inference cost as a single base model. No matter what your deployment shape or configuration, you’ll pay the same price as the base model, whether your deployment serves just one or hundreds of fine-tuned LoRAs.

**Cresta, a leader in AI-powered solutions for contact centers, uses Multi-LoRA to personalize their Knowledge Assist feature for each individual customer.** This enabled their customers’ contact center agents to resolve queries more quickly and accurately. They deployed 1000s of LoRAs on top of a single Mixtral/Mistral-based Ocean model cluster, at 100x lower cost compared with the previous GPT-4 setup (at the time of deployment in December 2023). Read more about Cresta’s innovations in personalizing AI with Multi-LoRA [here](https://cresta.com/blog/how-ocean-1-enhancements-beat-gpt-4-in-powering-knowledge-assist/).

"Fireworks' Multi-LoRA capabilities align with Cresta's strategy to deploy custom AI through fine-tuning cutting-edge base models. It helps unleash the potential of AI on private enterprise data." - Tim Shi, Co-Founder and CTO of Cresta

Companies often experiment with 100s of fine-tuned models in order to determine the best user experience, with multiple engineers and engineering teams experimenting simultaneously on different use cases. The most promising variants are then deployed into production for A/B testing.

Coordinating AI model experimentation across teams is challenging - teams need to be able to work in parallel, while still being efficient with compute resources as well as managing changing models and fluctuating traffic patterns.

Multi-LoRA offers an elegant solution: teams can create LoRA fine-tunes for each experiment, benefiting from the compute efficiency of utilizing the same base model, increased velocity in training and deploying LoRA fine-tunes, and easier onboarding and offboarding of experimental fine-tuned models. Companies can periodically ‘merge’ the most successful experiments by combining datasets and hyperparameter findings.

**Inference prices are the same as a single base model, even when serving hundreds of fine-tuned models**

Multi-LoRA makes it feasible to serve hundreds of fine-tuned models at the same cost as base model inference.

We believe this speed and cost efficiency unlocks personalization at scale. If you have many users, user segments or use cases to personalize for, deploying each fine-tuned model on a separate GPU would be prohibitively expensive. With Multi-LoRA, you can personalize AI at scale, without scaling your costs.

Multi-LoRA is also competitive in throughput and speed: you can serve hundreds of fine-tuned models, at inference speeds and throughput that approach 90% of base model performance.

[Scott Kramer](https://www.linkedin.com/in/scott-kramer-eng/), former Head of ML at Amplitude, helps businesses leverage their proprietary data to fine-tune and deploy models using Fireworks. Scott's clients find it easier and more cost-effective to deploy with Fireworks, compared to other platforms like AWS. Scott also teaches a fine-tuning course for developers, leveraging Fireworks as a key platform for learning.

“Using Fireworks, clients with limited AI expertise can successfully maintain and improve the solutions I provide. Additionally, students in my course are able to complete real-world fine-tuning projects, dedicating just a few hours per week to the process.” - Scott Kramer, CEO of Brainiac Labs, ex-Head of ML at Amplitude.

At Fireworks, we offer our own LoRA tuning service via Firectl CLI, with a REST API coming soon. However, you can also tune LoRAs using any tool or platform of your choice, and upload and deploy your LoRAs on Fireworks. Follow our documentation to [fine-tune](https://docs.fireworks.ai/fine-tuning/fine-tuning-models) as well as [upload and deploy](https://docs.fireworks.ai/models/deploying) models on Fireworks.

Once tuned, there are two main deployment options on Fireworks:

- **On-demand deployments are a great option for scaling companies:**On-demand offers the option of reserving private GPUs for better reliability, speed, increased model choice, and lower costs at higher volumes. There’s no software installation and no long-term commitment. You can get started in seconds, you only pay for the time your GPUs are in use, and you only need to pay for one set of GPUs even if you are serving hundreds of LoRAs. Learn more- [here](https://fireworks.ai/blog/why-gpus-on-demand).
- **Enterprise reserved deployments are the best option for high-volume workloads:**You can reserve GPUs for set periods of time, with custom pricing, SLAs, guaranteed support and fully configurable hardware and software optimized for your workload by the Fireworks team. Contact Sales- [here](https://fireworks.ai/company/contact-us).

And for even faster inference at high volumes, you can merge a LoRA into the base model and deploy the merged models on our on-demand or enterprise reserved deployments.

At Fireworks, we’ve built first class support for LoRA serving in our proprietary [FireAttention](https://fireworks.ai/blog/fire-attention-serving-open-source-models-4x-faster-than-vllm-by-quantizing-with-no-tradeoffs) inference stack. We optimized Multi-LoRA serving through **Cross-Model Continuous Batching**, which enables processing requests from multiple LoRAs simultaneously on the same base model and dynamically adjusts batch sizes to maximize GPU utilization. We also use **Dynamic Loading** of LoRA adapters with caching, to ensure that the number of supported LoRAs is not constrained by GPU memory and new models can be added or taken down within seconds.

Ready to experience the power of Multi-LoRA and FireOptimizer? Here's how to get started:

- •**Fine-Tune LoRAs**: Follow our[step-by-step guide](https://docs.fireworks.ai/fine-tuning/fine-tuning-models)to create your first LoRA.
- •**Deploy Your Model**: Follow our[deployment guide](https://docs.fireworks.ai/models/deploying)to quickly deploy your fine-tuned model.
- •**Join Our Community**: Join our[Discord channel](https://discord.gg/fireworks-ai)to connect with other developers and the Fireworks team
- •**Contact us:**[Reach out](https://fireworks.ai/contact)to discuss how we can help you leverage the power of Multi-LoRA and FireOptimizer for your specific use case.

We can’t wait to see what you build!
