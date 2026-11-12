---
title: How we built the fastest Kimi K2.5 on Artificial Analysis
kind: blog
topic: inference
subtopic: speculative-decoding
secondary_topics: []
summary: Details reaching 340+ TPS on the 1T-parameter Kimi K2.5 using a custom EAGLE-3
  speculator trained on hidden states from synthetic queries plus an INT4-to-NVFP4
  conversion to unlock NVIDIA Blackwell inference.
triage: null
skip_reason: null
source: baseten
url: https://www.baseten.co/blog/how-we-built-the-fastest-kimi-k2-5-on-artificial-analysis
author: Tri Dao
published: '2026-02-11'
fetched: '2026-11-12T06:11:00Z'
classifier: claude
taxonomy_rev: 2
words: 791
content_sha256: c13ae3c39bf99e429515bfd0d4a4429eb04cf2c4c152e31f07c18b8aebeab001
---

# How we built the fastest Kimi K2.5 on Artificial Analysis

Model performance
# How we built the fastest Kimi K2.5 on Artificial Analysis

Using a custom-built EAGLE-3 speculator model along with an in-house INT4 to NVFP4 conversion, we achieved 340+ tokens per second on Kimi K2.5.


- Authors
- Date
- February 11, 2026

TLDR

Using a custom-built EAGLE-3 speculator model trained on a corpus of hidden states from running Kimi K2.5 against synthetic queries, along with an in-house INT4 to NVFP4 conversion to unlock inference on Blackwell, we achieved 340+ tokens per second on Kimi K2.5 as independently benchmarked by Artificial Analysis.

Today, [Artificial Analysis](https://artificialanalysis.ai/models/kimi-k2-5/providers) benchmarked our Model API for Kimi K2.5 and we achieved state of the art results for both time to first token (TTFT) and tokens per second (TPS).

Kimi K2.5 is a frontier-grade open model with one trillion parameters, making it the largest mainstream open model currently on the market. As a reasoning model, Kimi K2.5 generates a thinking sequence before its final answer, trading off more inference compute for better quality.

Thus, inference optimization is critical for using Kimi K2.5 in production. To run Kimi K2.5, we use:

- [The Baseten Inference Stack](https://www.baseten.co/resources/guide/the-baseten-inference-stack/) with baseline optimizations including KV-aware routing.
- NVFP4 weights (converted from INT4) to unlock inference on NVIDIA Blackwell GPUs.
- A custom-built speculator using EAGLE-3 trained on Kimi K2.5 output for a corpus of synthetic queries.

Together, these optimizations provide leading performance on both first-token and inter-token latency on one of the most demanding open models released to date.

We consistently see excellent results with NVIDIA Blackwell GPUs for model APIs, but to use these GPUs to their fullest potential, we need to quantize the model weights to NVFP4, which helps with both latency and throughput.

Kimi K2.5 is already a 4-bit model via quantization-aware training. This is necessary to run such a large model on today’s hardware while leaving room for reasonable batch sizing and KV cache use. This means it should be possible to run in NVFP4 with little to no quality loss.

However, Kimi K2.5 weights are released in INT4, not NVFP4. This is because Kimi models target Hopper-based systems like H200 GPUs rather than Blackwell-based systems like B200 GPUs.

There is no direct path from INT4 to NVFP4. We decompressed the INT4 to bf16 on the fly, and re-calibrated the architecture with [ModelOpt](https://github.com/NVIDIA/Model-Optimizer), using a custom created calibration dataset to ensure that model quality remained excellent on benchmarks that closely reflect the real-world usage patterns of Kimi K2.5 users.

As a reasoning model, the most important thing for fast Kimi K2.5 in real-world use cases is higher tokens per second. The best way to improve TPS losslessly for a model like Kimi K2.5 is via speculative decoding.

Ordinary draft-target speculative decoding is a poor fit for Kimi K2.5. The model is very large, so there are few resources available on the inference system to run a second model, and there isn’t a good speculator model as there are no smaller models in the same family.

Instead, we use a custom-trained speculator model with an EAGLE-3 architecture. This model weighs in around a billion parameters, making it lightweight to run alongside Kimi K2.5, and it provides excellent draft token acceptance rates that far exceed any off-the-shelf draft model.

EAGLE-based draft models are trained on hidden states from the target model. This teaches them to predict what token the target model is going to produce. To create our draft model for Kimi K2.5, we:

1. Selected datasets of synthetic queries that match our anticipated use cases for Kimi K2.5, such as code generation, scientific questions, and mix of multilingual problems.
2. Ran inference on a basic deployment of Kimi K2.5 across the queries, returning hidden states for each query.
3. With the combined dataset, we [ran a training job](https://www.baseten.co/products/training/) to generate the EAGLE-3 model using [DeepSpeed](https://github.com/deepspeedai/DeepSpeed) as a training framework.

Speculative decoding performance gains depend on two factors: token acceptance rate and draft model overhead. By running this custom EAGLE-3 model on our inference stack, which has optimizations that minimize host overhead when running draft models, we achieved both high acceptance rates and low overhead, resulting in the 340+ TPS speeds reported in the benchmarks.

Achieving great benchmark results feels great, but we judge our work by what it enables our customers to build.

Kimi K2.5 is a popular choice for code generation on platforms like [OpenCode](https://opencode.ai/) and for agentic tasks, including as a [replacement for Claude Opus in OpenClaw](https://www.baseten.co/blog/openclaw-kimi-k2-5-on-baseten-frontier-agent-performance-with-oss/) for 8x cheaper agents. Now, at over 340 tokens per second, Kimi K2.5-based applications also run 4.5x faster than Claude.

Whether you’re generating code, shipping agents, or building anything else that requires affordable, fast frontier intelligence, try [Kimi K2.5 on Baseten](https://www.baseten.co/library/kimi-k25/) for industry-leading speed on the world’s largest open LLM.
