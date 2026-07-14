---
title: A quick introduction to speculative decoding
topic: inference
subtopic: speculative-decoding
secondary_topics:
- models/reasoning
summary: Introduces speculative decoding and the draft-target model pattern for lower
  LLM inference latency.
source: baseten
url: https://www.baseten.co/blog/a-quick-introduction-to-speculative-decoding/
author: Pankaj Gupta; Justin Yi; Philip Kiely
published: '2024-12-19'
fetched: '2026-07-11T04:08:39Z'
classifier: codex
taxonomy_rev: 1
words: 1214
content_sha256: 33454eccf34c4e0fe2ef03ee71f5c97b68dad4b98f560e5bc7cb90a3482b621a
triage: keep
skip_reason: null
---

# A quick introduction to speculative decoding

![Intro to Speculative Decoding](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1747434711-intro-spec-dec.png%3Fauto%3Dformat%26fit%3Dcrop%26h%3D630%26w%3D1200&w=3840&q=100)

Speculative decoding is an inference optimization technique designed to improve the latency of LLM inference by coordinating two models on a single model server: a larger target model (e.g. Llama 70B) and a smaller draft model (e.g. Llama 8B).

One of our main goals for LLM performance optimization is to reduce latency; we want our models to run as fast as possible. LLM latency has two parts:

- **Time to first token (TTFT)**: the time it takes to generate the first token.
- **Time per output token (TPOT)**: the time between subsequent token generations (also known as inter-token latency). A low TPOT means a high tokens per second.

The fundamental drag on inter-token latency is the autoregressive nature of LLM inference. To generate a single token, the model needs to consider every token in the input and every output token generated so far. This results in a very expensive forward pass through the model.

Speculative decoding offers the possibility of getting more tokens out of each of these expensive forward passes. With speculative decoding, the smaller “draft” model generates potential output tokens, which our larger original “target” model can either accept or reject during its own token generation process. If our draft model is accurate enough at generating acceptable tokens, this guess-and-check process can speed up inference.

## Speculative decoding napkin math

![In the speculative decoding core loop, draft tokens are generated, a prefix is accepted, and the target model generates an additional token](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1734626136-specdec.png%3Fauto%3Dformat%26w%3D1200&w=3840&q=75) In the speculative decoding core loop, draft tokens are generated, a prefix is accepted, and the target model generates an additional token

In the speculative decoding core loop, draft tokens are generated, a prefix is accepted, and the target model generates an additional tokenImagine we’re running a large LLM and our TPOT (after the first token) during inference is 10 milliseconds. But we also have a smaller version of the LLM that can generate a token in 1 millisecond.

Speculative decoding is the process of coordinating the large LLM (the target model) and the smaller LLM (the draft model) on the same GPU to combine the quality of the large model with the speed of the small model.

If, during the inference process:

- The draft model generates 4 draft tokens (4ms)
- The target model takes a moment to validate the tokens (1ms)
- The target model generates its own token (10 ms)

As long as we are able to accept 2 draft tokens on average, we’ll yield 3 tokens (2 draft tokens + 1 target token) per 15-second inference step, for a TPOT of 5 ms – twice as fast as the large model alone which took 10 ms per token.

## Step-by-step speculative decoding

End-to-end, speculative decoding works in this sequence:

- The model server receives user input.
- The target model processes the input and generates the first output token.
- The target model sends the full set of tokens (the input + the first output token) to the draft model and asks for a few draft tokens back.
- The draft model runs ordinary inference steps to generate the requested tokens.
- The draft model sends the generated tokens to the target model, which may: - Accept the tokens and use them as output.
- Reject the tokens and discard them.

- Regardless of whether draft tokens are accepted or rejected, the target model completes its autoregressive inference step and generates one additional token.
- After this process, the model server loops back to step 4 and passes these new tokens into the draft model along with the existing input and output tokens.
- Once the output sequence terminates, the model server stops generating tokens.

There is plenty that can go wrong within this loop, but also plenty of opportunities for us to add additional features and optimizations.

## Limitations of speculative decoding

We’ll talk about batch size in depth soon, but it matters because with speculative decoding, both the draft and target model run on the same GPU or GPU cluster. The two models share VRAM, but maintain their own separate KV caches. While this setup is compatible with in-flight batching, speculative decoding isn’t as useful with high batch sizes. Instead, it’s more useful when we have spare compute capacity, as is the case when running long input sequences through large models.

In addition to latency, our model performance efforts for LLM inference also prioritize throughput and quality. Our speculative decoding implementation only supports rejection sampling, which guarantees that the output tokens returned will be exactly the same as what the unmodified target model would generate. This ensures that quality is unaffected by speculative decoding.

However, speculative decoding limits a model server’s throughput.

Speculative decoding performance suffers with larger batch sizes, and batching is essential for high throughput. While there are strategies we used to address this limitation, it’s important to understand that the latency improvements offered by speculative decoding do reduce maximum system throughput, ultimately resulting in higher per-token inference costs as more hardware is required to serve the same traffic.

## What makes a good speculative decoding setup?

There are three things that can make speculative decoding even faster:

- **Generate and validate draft tokens faster**: carefully select an appropriate draft model.
- **Generate better draft tokens**: consider fine-tuning draft models for well-scoped use cases to improve token acceptance rates.
- **Reduce orchestration overhead**: ensure that the draft and target models both have the resources they need to run efficiently at all times.

Draft model selection is generally limited to the same model family as the target model, as the LLMs need to use the same tokenizer to be compatible. Additionally, you want the draft model to represent the same token distribution as the target model. Finding that just-right size where the model is fast enough to give a real speed boost but competent enough to yield acceptable tokens requires experimentation.

To increase draft model token acceptance rate even further, fine-tuning the draft model on a custom dataset of target model requests and responses can help. In our testing, we saw a 15% improvement in acceptance rate on a fine-tuned draft model. As speculative decoding is a lossless optimization, you want the draft model to be a copycat of the target model and produce the same output as often as possible.

## When is speculative decoding useful?

Speculative decoding is a latency optimization that works best for large models and small batch sizes. A great example of this is code generation, where you want to use a large, powerful model to generate long chunks of code, and you care about latency as you type.

Running at a low batch size isn’t great for GPU utilization and thus total cost of operation, but there are cases where speculative decoding is useful:

- When you must meet latency SLAs for large models.
- When your batch size is already limited by large models and long contexts taking up GPU memory.

In these cases, it makes sense to take advantage of spare compute to improve latency.

## How can I use speculative decoding in production?

We’ve integrated speculative decoding into our TensorRT-LLM Engine builder! [Check out the launch blog](https://www.baseten.co/blog/speculative-decoding-engine-builder-integration/) to get started or [read the engineering deep dive](https://www.baseten.co/blog/how-we-built-production-ready-speculative-decoding-with-tensorrt-llm/) for more details.
