---
title: 'Introducing Step 3.7 Flash: multimodal reasoning at scale'
kind: blog
topic: null
subtopic: null
secondary_topics: []
summary: null
triage: null
skip_reason: null
source: baseten
url: https://www.baseten.co/blog/introducing-step-37-flash-multimodal-reasoning/
author: Albert Lee
published: '2026-07-14'
fetched: '2026-07-14T06:43:36Z'
classifier: null
taxonomy_rev: 1
words: 588
content_sha256: 9188c5c9e8be2878c35a58cacbebb902f3cd4d45329d74bcddc6c838e3e5b624
---

# Introducing Step 3.7 Flash: multimodal reasoning at scale

![Step 3.7 Flash](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1783911336-step-3-7-flash-model-release.png%3Fauto%3Dformat%26fit%3Dcrop%26h%3D630%26w%3D1200&w=3840&q=100)

StepFun's Step 3.7 Flash, a 198-billion-parameter sparse MoE vision-language model, is now available in the Baseten Model Library in a hardware-efficient configuration (lower cost per token, smoother autoscaling).

We're excited to welcome StepFun to the Baseten Model Library! StepFun is doing incredible work building frontier-scale foundation models across text, vision, audio, and reasoning.

Step 3.7 Flash is StepFun’s debut model in our library, and we can't wait to see how teams use it.

## Why Step 3.7 Flash matters

Step 3.7 Flash is StepFun's flagship multimodal reasoning model. Here's what makes it stand out:

- **Efficient architecture:**A highly efficient, sparse MoE architecture (198B total parameters / 11B activated parameters). Of its 198 billion parameters, only 11 billion activate per token. Think of it as a large team where each request is handled by a small, specialized subset of experts, so most of the "brainpower" stays at rest.
- **Multimodal input:**Native image and video input, meaning you won't need to juggle separate models for visual tasks.
- **Long context window:**A generous 256k token context window to handle your larger inputs, such as large codebases.
- **Flexible reasoning:**Versatile reasoning capabilities at low, medium, and high levels, suited for supporting agentic workflows like coding and tool calling.

## What can you do with Step 3.7 Flash?

The unique combination of multimodal input, a long context window, and flexible reasoning unlocks a world of creative use cases. Here are a few that StepFun showcases:

Excited to try it for yourself? Getting started is easier than you might think with [Baseten](https://app.baseten.co/deploy/baseten/step-3.7-flash).

## Lowering cost and simplifying deployment

FP8 quantization means the model fits in 198 GB, so we can serve it on 4×H100s instead of 8×H200s . This makes Step 3.7 Flash cheaper, easier to deploy, and still with plenty of headroom for production traffic.

The [official vLLM recipe for deploying Step 3.7 Flash](https://recipes.vllm.ai/stepfun-ai/Step-3.7-Flash?variant=fp8) lists 8xH200s or 8xB200s as the hardware prerequisite. In the Baseten deployment from our Model Library, we're using **4×H100s**, substantially less expensive per token and more readily available than the larger configs.

How did we know it was possible to use a smaller instance? The FP8-quantized version of Step 3.7 Flash shrinks each weight from 16 bits to 8 bits, cutting memory requirements roughly in half ([learn more about FP8 quantization](https://www.baseten.co/blog/fp8-efficient-model-inference-with-8-bit-floating-point-numbers/) and [how we quantize without sacrificing quality](https://www.baseten.co/resources/guide/the-baseten-inference-stack/#optional-quantization)). As a result, the model weights alone require only 198 GB of memory. The 8×H200s and 8×B200s configs provide 1,128 GB and 1,536 GB of that memory respectively, far beyond what the quantized model needs.

But is ~122 GB of remaining memory enough to serve production traffic? Yes, for three reasons:

- **Mixture-of-experts (MoE) architecture**: Activates only 11 billion parameters (out of 198 billion) per token. Think of it as a large team where each request is handled by a small, specialized subset of experts.
- **Hybrid attention:**Keeps the memory footprint from growing much, even as conversations get longer (- [learn more here](https://magazine.sebastianraschka.com/i/191674053/7-hybrid-attention)).
- **Speculative decoding:**Predicts several tokens ahead in a single step and then verifies them in parallel (- [learn more here](https://www.baseten.co/blog/a-quick-introduction-to-speculative-decoding/#speculative-decoding-napkin-math)). Correct predictions are essentially "free," boosting throughput without quality loss.

Together, these mean 4×H100s not only fit the model, but have enough headroom for production workloads.

## Get started with Step 3.7 Flash

Step 3.7 Flash is available in the Baseten Model Library as a Dedicated Inference deployment. [Click here to deploy Step 3.7 Flash now!](https://app.baseten.co/deploy/baseten/step-3.7-flash)

Once deployed, [generate an API Key](https://docs.baseten.co/organization/api-keys), and follow [StepFun's quickstart guide](https://platform.stepfun.ai/docs/en/guides/models/step-3.7-flash-quickstart) to start processing image, video, and text inputs.
