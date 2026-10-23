---
title: 'Supervised Fine Tuning V2: Faster SFT on More Models | Fireworks'
kind: blog
topic: null
subtopic: null
secondary_topics: []
summary: null
triage: null
skip_reason: null
source: fireworks
url: https://fireworks.ai/blog/supervised-fine-tuning-v2
author: null
published: '2025-06-13'
fetched: '2026-10-23T06:14:48Z'
classifier: null
taxonomy_rev: 2
words: 716
content_sha256: 087ff3b9cdcaa12ee8d55af2e1d85edb9a193023ebb78fd90a440b707a392ad6
---

# Supervised Fine Tuning V2: Faster SFT on More Models | Fireworks

At Fireworks, we believe models and data are core assets for any company. If you’re building a vertical product, owning both your data and your models is key to delivering a premium user experience and creating strong product differentiation.

Data and models should form a self-improving loop: a better model powers a better product, a better product attracts more users, and more users generate more data to improve the model further. This is what we call the data flywheel.

You likely already have strong GTM and engineering teams to accelerate growth. Fireworks can help you close the loop by turning your data into a high-quality, customized model, and potentially, an even better product. We’re excited to unveil **Supervised Fine Tuning V2,** the next generation of our supervised fine-tuning service, designed to do just that.

V2 is not just an upgrade of our original fine-tuning service, it is a complete rewrite to deliver both better quality and faster training speed. Along with the beta release of our [Reinforcement Fine Tuning platform](https://fireworks.ai/blog/reinforcement-fine-tuning) we announced earlier this week, this provides you with another tool in your toolbox to adapt models to your specific use case and data.

Let’s dive into the new features and enhancements that we’re introducing with SFT V2.

## New Capabilities

### More Models

Our fine-tuning capabilities have expanded to include a broad range of models. This now encompasses the Qwen 2/2.5/3 series, Phi 4, Gemma 3, the Llama family, as well as leading open-source MoE models like [Deepseek R1](https://fireworks.ai/models/fireworks/deepseek-r1) and V3, including, of course, any fine-tuned variants of those models! For a comprehensive view of all supported tunable models, please refer to our Model Library: [Model Library](https://app.fireworks.ai/models?filter=All%20Models).

![Models available on SFTv2 Models available on SFTv2](https://fireworks.ai/_next/image?url=https%3A%2F%2Fcdn.sanity.io%2Fimages%2Fpv37i0yn%2Fhorizon%2Fdab2bbe0b2fc4607a374b86b892e34f71ae7f793-1080x1080.png%3Fauto%3Dformat&w=3840&q=75)

### Longer Context Length

We’ve really cranked things up with optimized kernels and smart memory handling, now we can handle training with context lengths all the way up to 131K. Basically, this means continued training for our models at their full context length.

![Robot on an assembly line Robot on an assembly line](https://fireworks.ai/_next/image?url=https%3A%2F%2Fcdn.sanity.io%2Fimages%2Fpv37i0yn%2Fhorizon%2Fda248ac23411191c7ab83c46f40e7c8485ab5a03-1344x768.jpg%3Fauto%3Dformat&w=3840&q=75)

### Quantization Aware Training

To ensure optimal inference quality, both FP4 and FP8 quantization-aware training options are supported. You no longer have to sacrifice quality for speed. As shown below, both FP8 QAT and FP4 QAT reduce evaluation loss compared to not using QAT, and both are able to converge to minimal evaluation loss after further training.

### Training with Multi-token Prediction

On DeepSeek V3/R1 models, we additionally support MTP (multi-token prediction) similar to what was described in the [DeepSeek V3](https://fireworks.ai/models/fireworks/deepseek-v3) paper to achieve potentially lower loss, and simultaneously adapt the MTP layer to achieve 3X generation speed when used as speculator at inference time.

### Multi-turn Function Calling

Supervised Fine Tuning V2 also supports multi-turn function calling fine tuning with vLLM compatible format, where you supply the list of tools and have intermediate tool calls in the chat messages.

`jsonCopy`
123456789

As shown in our [RFT blogpost](https://fireworks.ai/blog/reinforcement-fine-tuning), the powerful combination of SFT and RFT helps deliver a model that surpasses SOTA closed model.

## Faster speeds

Supervised Fine Tuning V2 boasts training speeds twice as fast as V1, thanks to numerous optimizations in training infrastructure. To illustrate, fine-tuning a [Qwen 72B](https://fireworks.ai/models/fireworks/qwen2-72b-instruct) model on 1 million tokens can be achieved in under 10 minutes. Ongoing optimizations are continuously being added to further accelerate training.

![Faster speeds with SFT Faster speeds with SFT](https://fireworks.ai/_next/image?url=https%3A%2F%2Fcdn.sanity.io%2Fimages%2Fpv37i0yn%2Fhorizon%2F30a37d08ed3bd701c02af4cfae6a4db8f17d97c8-1536x1024.png%3Fauto%3Dformat&w=3840&q=75)

While by default, a fine-tuning job will use a single GPU, you can now optionally enable turbo mode with the `--turbo` flag on non-Deepseek models to accelerate training using multiple GPUs to make your training jobs complete even faster.

### Multi-LoRA

For early prototyping and experimentation workflows, we encourage you to take advantage of [Multi-LoRA](https://docs.fireworks.ai/fine-tuning/multi-lora), which allows you to load up to 100 LoRA addons onto a single base model deployment. This increases utilization of your deployment and saves you from cold-start times when testing several fine-tuned variants of the same model.

![Multi-Lora Multi-Lora](https://fireworks.ai/_next/image?url=https%3A%2F%2Fcdn.sanity.io%2Fimages%2Fpv37i0yn%2Fhorizon%2F40476f11f08b6c0a5a5bc8703e58d737af1c00f8-643x511.png%3Fauto%3Dformat&w=3840&q=75)

## Getting Started

Supervised Fine Tuning is key to unlocking the power of your data to achieve unrivaled quality over your data and use case. With SFT v2, you now have access to a wider array of models, more powerful tuning techniques, and faster speeds to help you iterate quickly.

To get started, please check out our [docs](https://docs.fireworks.ai/fine-tuning/fine-tuning-models) and [API reference](https://docs.fireworks.ai/api-reference/create-supervised-fine-tuning-job).
