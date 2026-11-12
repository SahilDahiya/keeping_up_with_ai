---
title: Open source alternatives for machine learning models
kind: blog
topic: null
subtopic: null
secondary_topics: []
summary: null
triage: null
skip_reason: null
source: baseten
url: https://www.baseten.co/blog/open-source-alternatives-for-machine-learning-models
author: Varun Shenoy
published: '2023-11-21'
fetched: '2026-11-12T06:11:34Z'
classifier: null
taxonomy_rev: 2
words: 1162
content_sha256: c42995577d9258007e930c7f0f4ac3ddf93d6d4828d6b5e79fa526fbe2a630d9
---

# Open source alternatives for machine learning models

AI engineering
# Open source alternatives for machine learning models

Building on top of open source models gives you access to a wide range of capabilities that you would otherwise lack from a black box endpoint provider.


- Authors
- Date
- November 21, 2023

TLDR

Using open source ML models for your generative AI applications gives you a level of control, customization, reliability, and security not provided by proprietary model APIs. And paying for the hardware used for inference directly gives you more control over your spend while saving money at scale with optimized usage. While there are many open source models to pick from, we selected a few models whose capabilities line up well with popular closed source models, such as replacing GPT with Mistral.

Think of ML models like different types of engines, each suited for a particular use case. For example, a sports car’s engine is optimized for speed and acceleration, while a tractor’s engine prioritizes torque and fuel efficiency.

Similarly, with open source models, developers can choose the model architecture that is best suited for their needs, rather than being limited to a one-size-fits-all proprietary model.

Every benefit of using open source models on dedicated hardware is downstream of the full control you get over your model’s inputs, outputs, and environment. You can fully customize your model and model server for specific use cases.

Using open source models directly also protects you from “model shift,” where endpoint providers change the underlying model, sometimes with little or no notice. Updated models often behave differently than their predecessors, breaking prompt engineering and output parsing.

When you own your model, you decide if and when it changes and exactly how its API endpoint behaves.

Optimization is about tradeoffs. When you control your own model and infrastructure, you can make those tradeoffs based on your use case rather than accepting one vendor’s best approximation of everyone’s needs.

If you need to reduce latency, you can try specialized backend servers like vLLM, KV caching, speculative decoding, and of course using a more powerful GPU. On the other hand, if you have a latency-tolerant use case, you can batch multiple requests together to improve throughput and ensure you’re making the most of your compute resources. And if cost is a concern, quantizing your model reduces the model size, letting you make bigger batches or use smaller, less expensive GPUs.

These optimizations come from being able to do [inference math for your GPU and model](https://www.baseten.co/blog/llm-transformer-inference-guide/) so that you know exactly where bottlenecks exist during inference.

Switching to a dedicated deployment of an open source model insulates you from a class of “noisy neighbors” problems that pop up when using shared resources.

In shared-endpoint environments, multiple customers use the same hardware resources. When a “noisy neighbor” customer overuses resources, it can degrade performance for your workload.

On the other hand, when you host your own models on dedicated hardware, you replace variability with stability. You get more consistent SLAs, more control over your [model status](https://status.baseten.co/), and insight into performance metrics.

Crucially, dedicated infrastructure also shrinks your application’s attack surface and reduces the chance of data leakage, as there are fewer parties who can access the data. This enables better [regulatory compliance](https://www.baseten.co/blog/how-we-achieved-soc-2-and-hipaa-compliance-as-an-early-stage-company/).

With open source models, developers pay for the hardware resources directly. This provides more predictable costs compared to proprietary API services that charge per API request or per token.

When paying per API request or per token, costs can wildly fluctuate based on usage. Billing can spike if sudden load comes in. With open source models, you can cap your costs without losing the ability to scale up in response to user demand.

Autoscaling infrastructure for ML models lets you estimate expected request volume and provision the hardware accordingly, then automatically scale up and down within the configured limits in response to traffic. This limits your costs while ensuring reliability.

The granular pricing of API services encourages limiting usage to control costs. With open source models, the focus shifts to fully utilizing available hardware resources and configuring autoscaling to match traffic. The break-even point depends on factors like request volume, batch size, resource utilization, API pricing model. But for many realistic usage scenarios, open source models become cheaper at scale.

The biggest benefit — and sometimes the biggest drawback — of open source is the sheer number of models that are publicly available. There are new models being released every day, and sometimes evaluations seem to be mostly based on \~vibes\~. From our experiences, here are some of the best open source models that you can deploy right now for common use cases.

If you’re using models like GPT or Claude, there are great open source alternatives. Large language models are one of the most actively developed categories of open source models, and there are multiple model families to choose from.

Three leading families of open-source LLMs are [DeepSeek](https://www.baseten.co/library/family/deepseek/), [Llama](https://www.baseten.co/library/family/llama/), and [Qwen](https://www.baseten.co/library/family/qwen/). Larger models offer higher output quality but require larger, [more expensive GPUs for inference](https://www.baseten.co/blog/how-multi-node-inference-works-llms-deepseek-r1/). But small models like Gemma 3 still offer strong performance for specific tasks like data extraction.

Open source LLMs come in a few different variants. There are base models, which are designed for evaluation and fine-tuning, and instruct or chat-tuned models, which provide a conversational output similar to ChatGPT. You’ll most likely want instruct/chat-tuned models for building user-facing products.

Where open source LLMs also shine is the variety of models designed for specific tasks, like Qwen Code, a family of models optimized for code generation.

Deploy [Llama 3.3 70B](https://www.baseten.co/library/llama-3-3-70b-instruct/) from the model library.

The often-overlooked category of [text embedding models](https://www.baseten.co/blog/the-best-open-source-embedding-models/) are essential for many production use cases for LLMs — especially around giving LLMs information that isn’t in their training data.

When working with the GPT APIs, the `text-embedding-3` model fills that role. For open source, you have a number of models to choose from, but [BAAI's open model family](https://www.baseten.co/library/bge-embedding-icl/) matches OpenAI in both context window size and benchmark scores.

One important note: text embeddings are not compatible from model to model. If you switch to a new model, you’ll need to re-generate embeddings for the corpus you query against.

Deploy [BAAI bge-en-icl](https://www.baseten.co/library/bge-embedding-icl/) from the model library.

Whisper is one of OpenAI’s open-source models, which means you can still use the same model for audio transcription tasks while getting the performance, cost, and security benefits of running it on dedicated hardware.

Deploy Whisper from the model library.

There are a number of open source alternatives to the Audio API, like Orpheus TTS and Sesame. Text to speech models vary in their capabilities across languages, voices, and background sounds, but experimenting with these models is a lot of fun!

Deploy [Orpheus TTS](https://www.baseten.co/library/orpheus-tts/) from the model library.

Open source ML models can improve the security, reliability, performance, and cost of your generative AI applications.

If you’re ready to try open source models, get started with our [checklist for switching to open source](https://www.baseten.co/blog/a-checklist-for-switching-to-open-source-ml-models/). And we’re always here to help at [support@baseten.co](mailto:support@baseten.co).
