---
title: How to double tokens per second for Llama 3 with Medusa
topic: inference
subtopic: speculative-decoding
secondary_topics:
- models/reasoning
summary: Explains Medusa-style speculative heads for increasing Llama 3 tokens per
  second.
source: baseten
url: https://www.baseten.co/blog/how-to-double-tokens-per-second-for-llama-3-with-medusa/
author: Abu Qader; Philip Kiely
published: '2024-08-20'
fetched: '2026-07-11T04:09:09Z'
classifier: codex
taxonomy_rev: 1
words: 1531
content_sha256: e671aca5e6c79be0dc1dc55fb55e1288243c9af4db73911187953a312398e170
triage: keep
skip_reason: null
---

# How to double tokens per second for Llama 3 with Medusa

![Double Llama TPS with Medusa](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1747438977-llama-medusa.png%3Fauto%3Dformat%26fit%3Dcrop%26h%3D630%26w%3D1200&w=3840&q=100)

Medusa, a method for generating multiple tokens per forward pass during LLM inference, can double the tokens per second of an LLM deployment. After training and validating Medusa heads, which are additional decoding heads grafted onto the base model, Medusa can be used in production by deploying the modified LLM using TensorRT-LLM.

Everyone wants more tokens per second for their LLMs. There are reliable ways to make inference faster, like using an H100 GPU or TensorRT-LLM. Then there are techniques like quantization that are increasingly robust, but you have to be careful not to ruin model output quality in pursuit of speed.

After these kinds of fundamental optimizations are in place, more speed requires implementing cutting-edge inference techniques and managing the tradeoffs that come with them. One such technique is Medusa.

![How Medusa inference generates and uses draft tokens](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1723581904-mermaid-diagram-2024-07-19-135654.png%3Fauto%3Dformat%26w%3D1200&w=3840&q=75) How Medusa inference generates and uses draft tokens

How Medusa inference generates and uses draft tokens[Medusa](https://arxiv.org/abs/2401.10774) is a method for generating multiple tokens per forward pass of an LLM. By creating and validating multiple candidate continuations in parallel, Medusa improves the efficiency of memory-bound autoregressive inference steps by leveraging idle compute to generate more potential tokens. Medusa is similar to speculative decoding, but grafts extra decoding heads onto the model itself rather than relying on a smaller draft model to generate candidate tokens.

We’ve successfully used Medusa in production by:

- Training original Medusa heads for Llama 3 8B.
- Validating output quality with MMLU benchmark scores.
- Running the Medusa-optimized model with TensorRT-LLM.

In our production deployment, we observe a **94% to 122% increase in tokens per second** depending on the subject matter of the query versus an otherwise equivalent deployment without Medusa.

In this article, we’ll provide a high-level introduction to Medusa. Then, we’ll review benchmarks to show how much Medusa can accelerate LLM inference and discuss considerations for using Medusa in production.

## What inference bottleneck does Medusa address?

LLM inference is autoregressive. Every time a token is generated in a forward pass, it’s sent back along with the prompt and all previous tokens for the next forward pass through the model. Each forward pass creates one new token.

Before generating output tokens, the LLM must first process all input tokens. This is called “prefill” and is compute-bound because it’s a highly parallelized step where the tokens are being processed concurrently. So more compute power (FLOPS) means faster prefill and a shorter time to first token.

However, the autoregressive token generation beyond the first token is memory-bound. Now, the FLOPS of a GPU is not the bottleneck. Instead, the VRAM bandwidth, expressed in gigabytes per second, is the limiting factor. Tokens can only be generated as fast as the model weights can be read from memory.

Read our [guide to LLM inference and performance](https://www.baseten.co/blog/llm-transformer-inference-guide/) for the math behind compute and memory bottlenecks.

Given that inference is a memory-bound process, one thing that would make the LLM much faster is if we could do more with our idle compute resources each time we load model weights from memory.

## What is Medusa?

[Medusa](https://arxiv.org/abs/2401.10774) is an optimization technique for LLM inference that introduces compute parallelism to the memory-bound autoregressive token generation step. Medusa uses idle compute resources during inference to get you more tokens every time you read model weights, reducing the impact of VRAM bandwidth as an inference bottleneck.

While an ordinary LLM generates only one token per forward pass, Medusa allows LLMs to create multiple draft tokens (generally 3) per forward pass. Medusa is a new speculative sampling technique that differs from traditional speculative decoding in that it does not require a secondary draft model.

### How speculative decoding with draft models works

Speculative decoding relies on two key facts:

- It’s faster to verify if a token is correct than it is to generate a token.
- Most tokens are fairly unsurprising.

This means that a smaller, less powerful model will often generate the same next token as a larger, more powerful one. And when it doesn’t, it’s fast to catch the error and only then take the time to run a forward pass of the larger, slower model.

Speculative decoding works by using a small model, called a draft model, to predict the next token that the main model would yield. These draft models are quite efficient, often in the hundreds of millions of parameters, while the main model may have tens of billions of parameters.

When successful, speculative decoding massively improves model performance because many tokens are generated by the smaller model. Meanwhile, accuracy is preserved because the most important or surprising tokens are generated by the larger model when the smaller model falls short.

However, speculative decoding has its limitations. Beyond the complexity of operating two models simultaneously, you’re now more limited in the batch size that you can process due to higher memory usage. Small batch sizes are great for first-token latency and per-client tokens per second, but reduce the overall throughput of your GPU, driving up cost per million tokens. Medusa provides the same benefits as traditional speculative decoding while avoiding these downsides.

### How Medusa heads work

Medusa is another method for generating and verifying draft tokens. Rather than selecting a draft model to run alongside the main model, Medusa works by fine-tuning the main model to add multiple decoding heads. Each decoding head is responsible for creating a token during each forward pass.

Today, we add on the order of three Medusa heads to an LLM during fine-tuning. The base model produces a token each pass, and each head generates a sequential draft token. With three Medusa heads, four tokens are created per forward pass.

Medusa heads are neural nets that are grafted onto the base model and sit on top of the weights and activations. Unlike traditional speculative decoding, Medusa modifies the model architecture during the fine-tuning process. Just like you can’t use a Llama 3 LoRA with Mistral, you can’t re-use Medusa heads model-to-model; they must be fine-tuned on a per-model basis.

Given enough compute overhead, Medusa does not massively constrain batch sizes and does not require orchestrating multiple models. Medusa is [supported by serving frameworks like TensorRT-LLM](https://nvidia.github.io/TensorRT-LLM/speculative_decoding.html#medusa) and is suitable for production use (after careful validation of a successful fine-tune).

### Tree attention for draft token verification

Generating draft tokens is great, but they still need to be verified. Verifying a token, much like prefill, is much faster than generating a token because it’s a parallelizable compute-bound process in which you do not need to capture and store activations in memory.

Token verification uses an efficient tree-based attention algorithm to evaluate the logits generated for a token. A logit represents the likelihood that the base model considers this draft token as the best possible continuation in a sequence, rather than directly indicating the draft token's correctness. If the logit is below a certain threshold, the draft token is flagged as incorrect.

When a draft token is wrong, the error must be corrected. The base model will produce the correct token instead in a future forward pass.

Of course, if every draft token is wrong, then Medusa would actually make inference slower. How often tokens need to be correct to make the technique worthwhile varies based on how long it takes to generate a token and how long it takes to verify a token. Generally, the longer generation takes, and the faster verification is, the more benefits you’ll see from Medusa.

Because accuracy matters for Medusa’s performance impact, the improvements in performance vary by topic.

## Medusa performance benchmarks

The performance gains you get from Medusa depend on:

- What base model you choose.
- How accurate the Medusa heads are for the relevant topics.
- What hardware you run inference on.
- What other optimization techniques, like quantization, you use.

In a benchmark, we saw double the tokens per second running Llama 3 8B Instruct on an A100 in FP16 with no other major optimizations in place. The exact improvement varied by topic.

![Llama TPS with Medusa (green) vs base (blue) per topic.](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1723582061-comparison-of-tps-between-llama-3-baseline-and-medusa.png%3Fauto%3Dformat%26w%3D1200&w=3840&q=75) Llama 3 8B Tokens per Second with Medusa (green) vs base (blue) per topic.

Llama 3 8B Tokens per Second with Medusa (green) vs base (blue) per topic.## Using a Medusa-optimized LLM in production

Speculative sampling techniques like Medusa are still relatively new research and should be validated carefully before deployment to production. But when more general methods like TensorRT-LLM engine optimization and post-training quantization aren’t getting the results you need, advanced methods like Medusa are worth considering.

Before deploying a model with Medusa to production, rigorously validate output quality with both manual checks and comparative benchmarks like MMLU alongside traditional latency and throughput benchmarks.

Medusa is compatible with a wide range of engines (vLLM, TensorRT-LLM, etc.), precisions (FP16, INT8, FP8, etc.), and GPUs. This is important because the best performance comes from a context-driven combination of multiple approaches to optimization.

For high performance implementations of open source, fine-tuned, and custom generative AI models of any size and modality, [talk to us](https://www.baseten.co/talk-to-us/) to get connected to model performance experts who can deploy your models on reliable and secure autoscaling infrastructure.
