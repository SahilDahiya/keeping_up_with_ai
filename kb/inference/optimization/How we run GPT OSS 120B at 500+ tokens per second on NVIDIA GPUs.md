---
title: How we run GPT OSS 120B at 500+ tokens per second on NVIDIA GPUs
kind: blog
topic: inference
subtopic: optimization
secondary_topics: []
summary: Baseten's day-zero optimization of OpenAI's gpt-oss-120b spanned benchmarking
  across TensorRT-LLM, vLLM, and SGLang and ensuring Hopper/Blackwell compatibility,
  reaching the top public latency/throughput numbers on OpenRouter by launch day and
  adding 100 more tokens/sec of throughput in the time it took to write the post.
triage: null
skip_reason: null
source: baseten
url: https://www.baseten.co/blog/sota-performance-for-gpt-oss-120b-on-nvidia-gpus
author: Amir Haghighat
published: '2025-08-06'
fetched: '2026-11-12T06:10:14Z'
classifier: claude
taxonomy_rev: 2
words: 846
content_sha256: 52e1ee2152149b06b0b518bfcb840b1ad2882d4b367570238e8a7974b4ddc2cd
---

# How we run GPT OSS 120B at 500+ tokens per second on NVIDIA GPUs

Model performance
# How we run GPT OSS 120B at 500+ tokens per second on NVIDIA GPUs

How we optimized GPT OSS 120B for state-of-the-art latency and throughput on launch day.


- Authors
- Date
- August 6, 2025

TLDR

Day zero model performance optimization work is a mix of experimentation, bug fixing, and benchmarking guided by intuition and experience. This writeup outlines the process we followed to achieve SOTA latency and throughput for GPT OSS 120B on NVIDIA GPUs at launch with the Baseten Inference Stack.

**Update**: we've [made our GPT OSS implementation even faster](https://www.baseten.co/blog/how-we-made-the-fastest-gpt-oss-on-nvidia-gpus-60-percent-faster/), reaching speeds of over 650 tokens per second on Artificial Analysis and higher on OpenRouter.

The day an open source model like OpenAI’s new gpt-oss-120b is released, we race to make the model as performant as possible for our customers. As a [launch partner](https://openai.com/index/introducing-gpt-oss/) for OpenAI’s first open-source LLM since 2019, we wanted to give developers a great experience with the new LLMs.

By the end of launch day, we were the clear leader running on NVIDIA GPUs for both latency and throughput per public data from real-world use on [OpenRouter](https://openrouter.ai/openai/gpt-oss-120b).

Optimizing performance on a new model is a substantial engineering challenge. Thanks to our flexible [inference stack](https://www.baseten.co/resources/guide/the-baseten-inference-stack/) and the collective expertise of our model performance engineering team, we are able to roll out performance improvements by the hour on new models.

In fact, in the time it took to write this blog post, we added another 100 tokens per second while maintaining 100% uptime.

Model performance efforts included:

- Testing and benchmarking across inference frameworks (TensorRT-LLM, vLLM, and SGLang)
- Ensuring compatibility with Hopper and Blackwell GPU architectures
- Integrating with key pieces of our inference stack, including NVIDIA Dynamo
- Layering in our favorite performance optimizations, like KV cache-aware routing and speculative decoding with Eagle

Below are the steps we took to achieve our goal of SOTA performance with full context window support.

The first step is running baseline inference however possible. Running inference on a model requires support at the inference framework, hardware architecture, and model server level.

Inspired by GPUs, we parallelized this effort across multiple engineers. One engineer tried vLLM, another SGLang, and a third worked on TensorRT-LLM. We were able to quickly get TensorRT-LLM working, which was fortunate as it is usually the most performant inference framework for LLMs. In most cases, we use an overnight or dev build rather than a full release, as inference framework maintainers are simultaneously working on supporting the new model.

With TensorRT-LLM, it was important to serve the model on both Hopper and Blackwell architectures to support widely-available H100 GPUs and access the speed of B200 GPUs for our public model APIs.

One key tenet of the Baseten Inference Runtime is flexibility. This is especially useful when serving new models with novel architectures. Navigating, and when necessary updating, the support matrix across the entire stack requires the ability to swap between tools quickly.

Whenever a new model architecture is released, there will be subtle bugs and issues when integrating it into existing frameworks. The GPT OSS release added multiple new technologies, including [Harmony](https://cookbook.openai.com/articles/openai-harmony), a new response format.

A large part of our engineering work was iteratively fixing bugs and testing models for both speed and correctness. Where we could, we [contributed back to open source](https://github.com/openai/harmony/pull/13) with the fixes that worked for us.

Thanks to the hard work of open source maintainers worldwide, there are multiple excellent options for running GPT OSS, and bugs are getting identified and fixed quickly.

While OpenAI advertises that GPT OSS 120B can be run on a single H100 GPU, optimized deployments parallelize the model across 4 or 8 GPUs for improved performance and throughput. There are two parallelism approaches worth considering for this model: Tensor Parallelism and Expert Parallelism.

We found that Tensor Parallelism offered better latency, while Expert Parallelism offered better system throughput. As we are prioritizing latency, we selected Tensor Parallelism.

Additionally, we adopted the TensorRT-LLM MoE Backend, which is supported on Blackwell but not Hopper. This backend adds improved CUDA kernels that outperform the previous Triton backend. For more details on server configuration, see [NVIDIA’s TensorRT-LLM documentation for GPT OSS optimization](https://github.com/NVIDIA/TensorRT-LLM/blob/main/docs/source/blogs/tech_blog/blog9_Deploying_GPT_OSS_on_TRTLLM.md).

These first-pass performance improvements achieved SOTA latency and throughput, but there is a lot more headroom to improve performance on GPT OSS 120B.

One exciting update we’re working on is adding speculative decoding. Speculative decoding uses a smaller “draft” model to guess at future tokens, which are then validated by the target model. We’re big fans of Eagle 3 for speculation, but our inference stack supports 10+ algorithms to ensure that we can pick the right fit for each model and workload.

If this kind of performance optimization work sounds exciting to you, we’re [actively hiring for model performance engineers](https://www.baseten.co/resources/careers/). But for most AI engineering teams, this kind of performance optimization work shouldn’t stand in the way of testing new models in your product. Whether you’re looking for [GPT OSS 120B](https://www.baseten.co/library/gpt-oss-120b/) or any open-source or custom model, [get in touch with us](https://www.baseten.co/talk-to-us/) for help optimizing your latency and throughput!
