---
title: How we built the fastest GLM 5 API
topic: inference
subtopic: optimization
secondary_topics:
- inference/serving
summary: Explains serving optimizations used to build a fast GLM 5 API.
source: baseten
url: https://www.baseten.co/blog/how-we-built-the-fastest-glm-5-api/
author: Tri Dao; Philip Kiely; Madison Kanna
published: '2026-03-06'
fetched: '2026-07-11T04:06:05Z'
classifier: codex
taxonomy_rev: 1
words: 904
content_sha256: f892e3549c1c28a248cd71f05dd61880963206d64c9de9745b956a9512fa5fa3
triage: keep
skip_reason: null
---

# How we built the fastest GLM 5 API

![GLM-5](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1773096546-glm-5_blog.png%3Fauto%3Dformat%26fit%3Dcrop%26h%3D630%26w%3D1200&w=3840&q=100)

Using our low-overhead speculative decoding engine for Multi-Token Prediction (MTP), optimized MoE routing kernels, and inference kernels purpose-built for DeepSeek Sparse Attention (DSA), we achieved 186+ tokens per second on GLM-5 as independently benchmarked by Artificial Analysis.

Today,[  Artificial Analysis](https://artificialanalysis.ai) benchmarked our Model API for GLM-5, and we achieved state-of-the-art results for both time to first token (TTFT) and tokens per second (TPS).

![Video](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fimage.mux.com%2FOxJHhqeb02FA6NTm4JIsqzGO01Z302Y6sMZ%2Fthumbnail.jpg&w=3840&q=75)

GLM-5 is [ Z.ai](https://huggingface.co/zai-org)'s latest open-weight flagship model. GLM-5 is more than twice the size of its predecessor GLM-4.7 and uses a MoE (mixture of experts) architecture where only a subset of the model activates for any given token. In other words, parameters are in specialized expert layers that activate selectively depending on what the model is processing. 

It's useful for both code generation and agentic reasoning tasks. It ranks #1 among open-source models on Vending Bench 2. Built by Andon Labs, this benchmark tasks a model with running a simulated vending machine business over the course of a year to measure whether a model can stay coherent and make good decisions over a long time horizon.

![At 186+ tokens per second, our GLM-5 inference is by far the fastest on Artificial Analysis](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1772758664-output-speed-5-mar-26-1.png%3Fauto%3Dformat%26w%3D1200&w=3840&q=75) At 186+ tokens per second, our GLM-5 inference is by far the fastest on Artificial Analysis

At 186+ tokens per second, our GLM-5 inference is by far the fastest on Artificial AnalysisTo achieve the leading TTFT and TPS results for GLM-5, we served the model using the Baseten Inference Stack with the following techniques:

- Custom kernels for efficient DeepSeek Sparse Attention
- Low-overhead MTP speculation engine
- Optimization for Blackwell inference via NVFP4 quantization

This post describes the specifics of each optimization.

## Custom kernels that exploit DeepSeek Sparse Attention 

To optimize GLM-5, we use custom kernels that exploit DeepSeek Sparse Attention (DSA) to cut KV cache cost at long context.

The DeepSeek AI team invented DSA as an optimization to reduce the cost of a long context prefill by using a lighting indexer. The lighting indexer is trained on the main model and used to identify the top-K most important tokens, then performs sparse attention only on those.

The indexer must scan every token in the sequence to compute which K tokens to select. At shorter context lengths, this scanning overhead dominates, and the sparse attention has a longer prefill time than full attention. There are a few ways we sped this up:

- If the sequence length is less than K, we can skip the indexer and run standard full attention.
- For longer sequences, optimizing the indexer code path itself.

With the indexer mechanism, although the main multi-head attention can be performed in FP8, other large and important projections need to be performed in high precision to preserve quality. The numerical tolerance is much lower compared to other parts of the model. We overlap and fuse operations through the indexer code path to minimize the cost of these high-precision projections.

## A low-overhead MTP speculative decoding engine

LLMs are trained with an autoregressive pattern, meaning they generate the next token based on all previous tokens. Every new token requires a full forward pass through the model. This is a slow process. Speculative decoding is one of the most powerful techniques for speeding up this part of inference. With speculative decoding, a small draft model predicts the next N tokens and then verifies all those guesses in a single batch in a single forward pass. Because of this, with a good draft head, we can speed up inference by TPS by N+1 times, in the best-case scenario.

In speculative decoding, when the target model verifies the draft tokens, it checks each one against what it would have generated. If the draft token matches closely, it “accepts” it. Acceptance rate is the percentage of draft tokens that have passed this check. The particular type of speculative decoding we used to optimize GLM-5 is multi-token prediction, where the draft mechanism is built into the main model during training, leading to greater acceptance.

An often-overlooked aspect of speculative decoding is the minimization of overhead. A naive implementation would run the draft model separately from the main model, incurring host overhead during verification and sampling. At Baseten, we [ run both the draft model and the target model as one big model](https://www.baseten.co/blog/boosting-mtp-acceptance-rates-in-baseten-speculation-engine/). By doing so, the overhead is essentially zero, other than when you predict wrong draft tokens. All of our existing optimizations can be stacked on top of this optimization for a multiplicative lift to TPS. 

## The Baseten Inference Stack 

![Baseten has the lowest time to first token as measured by Artificial Analysis](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1772758631-artificialanalysis-ai_models_glm-5_providers_latency-time-to-first-token-1.png%3Fauto%3Dformat%26w%3D1200&w=3840&q=75) Baseten has the lowest time to first token as measured by Artificial Analysis

Baseten has the lowest time to first token as measured by Artificial Analysis[ Baseten Inference Stack](https://www.baseten.co/resources/guide/the-baseten-inference-stack/) with baseline optimizations, including

[. We also optimized MoE (mixture of experts) dispatch kernels, hand-tuned to GLM-5 through profiling, and](https://www.baseten.co/resources/guide/the-baseten-inference-stack/#kv-cache-aware-routing)

__KV-aware routing__[.](https://www.baseten.co/blog/how-we-built-the-fastest-kimi-k2-5-on-artificial-analysis/#unlocking-blackwell-inference-with-nvfp4)

__quantized the model weights to NVFP4 for Blackwell compatibility__These are similar optimizations to what we used to achieve leading performance on other models like [ Kimi K2.5](https://www.baseten.co/blog/how-we-built-the-fastest-kimi-k2-5-on-artificial-analysis/) and

[.](https://www.baseten.co/blog/sota-performance-for-gpt-oss-120b-on-nvidia-gpus/)

__GPT OSS 120B__**Building with GLM-5**

GLM-5 is purpose-built for complex systems engineering and long-horizon agentic tasks. Whether you're running autonomous coding agents, building multi-step tool-use pipelines, or shipping anything that requires frontier-grade intelligence at production speed, try [GLM-5](https://www.baseten.co/library/glm-5/) on Baseten for industry-leading throughput on one of the world's most capable open-source models.
