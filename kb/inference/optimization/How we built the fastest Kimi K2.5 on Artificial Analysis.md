---
title: How we built the fastest Kimi K2.5 on Artificial Analysis
topic: inference
subtopic: optimization
secondary_topics:
- models/reasoning
summary: Explains optimizations behind fast Kimi K2.5 serving on Artificial Analysis.
source: baseten
url: https://www.baseten.co/blog/how-we-built-the-fastest-kimi-k2-5-on-artificial-analysis/
author: Tri Dao; Michael Feil; Abu Qader; Philip Kiely
published: '2026-02-11'
fetched: '2026-07-11T04:06:14Z'
classifier: codex
taxonomy_rev: 1
words: 929
content_sha256: a359d4923d5b81e73bcbf062463ea628af2ffa4f1b563d0994268b8c8a4a69ea
triage: keep
skip_reason: null
---

# How we built the fastest Kimi K2.5 on Artificial Analysis

![kimi k2.5](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1773096546-kimi-k25_blog.png%3Fauto%3Dformat%26fit%3Dcrop%26h%3D630%26w%3D1200&w=3840&q=100)

Using a custom-built EAGLE-3 speculator model trained on a corpus of hidden states from running Kimi K2.5 against synthetic queries, along with an in-house INT4 to NVFP4 conversion to unlock inference on Blackwell, we achieved 340+ tokens per second on Kimi K2.5 as independently benchmarked by Artificial Analysis.

Today, [Artificial Analysis](https://artificialanalysis.ai/models/kimi-k2-5/providers) benchmarked our [Model API for Kimi K2.5](https://www.baseten.co/library/kimi-k25/) and we achieved state of the art results for both time to first token (TTFT) and tokens per second (TPS).

![At 340+ tokens per second, our Kimi K2.5 inference is by far the fastest on Artificial Analysis (measured Feb 10, 2026).](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1770822884-hazmsghaaaiztqt.jpeg%3Fauto%3Dformat%26w%3D1200&w=3840&q=75) At 340+ tokens per second, our Kimi K2.5 inference is by far the fastest on Artificial Analysis (measured Feb 10, 2026).

At 340+ tokens per second, our Kimi K2.5 inference is by far the fastest on Artificial Analysis (measured Feb 10, 2026).Kimi K2.5 is a frontier-grade open model with one trillion parameters, making it the largest mainstream open model currently on the market. As a reasoning model, Kimi K2.5 generates a thinking sequence before its final answer, trading off more inference compute for better quality.

Thus, inference optimization is critical for using Kimi K2.5 in production. To run Kimi K2.5, we use:

- [The Baseten Inference Stack](https://www.baseten.co/resources/guide/the-baseten-inference-stack/)with baseline optimizations including KV-aware routing.
- NVFP4 weights (converted from INT4) to unlock inference on NVIDIA Blackwell GPUs.
- A custom-built speculator using EAGLE-3 trained on Kimi K2.5 output for a corpus of synthetic queries.

Together, these optimizations provide leading performance on both first-token and inter-token latency on one of the most demanding open models released to date.

### Unlocking Blackwell inference with NVFP4

We consistently see excellent results with NVIDIA Blackwell GPUs for model APIs, but to use these GPUs to their fullest potential, we need to quantize the model weights to NVFP4, which helps with both latency and throughput.

Kimi K2.5 is already a 4-bit model via quantization-aware training. This is necessary to run such a large model on today’s hardware while leaving room for reasonable batch sizing and KV cache use. This means it should be possible to run in NVFP4 with little to no quality loss.

However, Kimi K2.5 weights are released in INT4, not NVFP4. This is because Kimi models target Hopper-based systems like H200 GPUs rather than Blackwell-based systems like B200 GPUs.

There is no direct path from INT4 to NVFP4. We decompressed the INT4 to bf16 on the fly, and re-calibrated the architecture with [ModelOpt](https://github.com/NVIDIA/Model-Optimizer), using a custom created calibration dataset to ensure that model quality remained excellent on benchmarks that closely reflect the real-world usage patterns of Kimi K2.5 users.

### Increasing TPS with EAGLE 3 speculation

As a reasoning model, the most important thing for fast Kimi K2.5 in real-world use cases is higher tokens per second. The best way to improve TPS losslessly for a model like Kimi K2.5 is via speculative decoding.

![High tokens per second affects end-to-end response time more for reasoning models, which must generate a thinking sequence before returning a final answer.](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1770822941-screenshot-2026-02-10-at-9-47-00-pm.png%3Fauto%3Dformat%26w%3D1200&w=3840&q=75) High tokens per second affects end-to-end response time more for reasoning models, which must generate a thinking sequence before returning a final answer.

High tokens per second affects end-to-end response time more for reasoning models, which must generate a thinking sequence before returning a final answer.Ordinary draft-target speculative decoding is a poor fit for Kimi K2.5. The model is very large, so there are few resources available on the inference system to run a second model, and there isn’t a good speculator model as there are no smaller models in the same family.

Instead, we use a custom-trained speculator model with an EAGLE-3 architecture. This model weighs in around a billion parameters, making it lightweight to run alongside Kimi K2.5, and it provides excellent draft token acceptance rates that far exceed any off-the-shelf draft model.

EAGLE-based draft models are trained on hidden states from the target model. This teaches them to predict what token the target model is going to produce. To create our draft model for Kimi K2.5, we:

- Selected datasets of synthetic queries that match our anticipated use cases for Kimi K2.5, such as code generation, scientific questions, and mix of multilingual problems.
- Ran inference on a basic deployment of Kimi K2.5 across the queries, returning hidden states for each query.
- With the combined dataset, we - [ran a training job](https://www.baseten.co/products/training/)to generate the EAGLE-3 model using- [DeepSpeed](https://github.com/deepspeedai/DeepSpeed)as a training framework.

Speculative decoding performance gains depend on two factors: token acceptance rate and draft model overhead. By running this custom EAGLE-3 model on our inference stack, which has optimizations that minimize host overhead when running draft models, we achieved both high acceptance rates and low overhead, resulting in the 340+ TPS speeds reported in the benchmarks.

### Building with the world’s fastest Kimi K2.5

Achieving great benchmark results feels great, but we judge our work by what it enables our customers to build.

Kimi K2.5 is a popular choice for code generation on platforms like [OpenCode](https://opencode.ai/) and for agentic tasks, including as a [replacement for Claude Opus in OpenClaw](https://www.baseten.co/blog/openclaw-kimi-k2-5-on-baseten-frontier-agent-performance-with-oss/) for 8x cheaper agents. Now, at over 340 tokens per second, Kimi K2.5-based applications also run 4.5x faster than Claude.

![Kimi K2.5 is 8x cheaper and 4.5x faster than Claude Opus](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1770826607-baseten-vs-claude-opus-pricing.png%3Fauto%3Dformat%26w%3D1200&w=3840&q=75) Kimi K2.5 is 8x cheaper and 4.5x faster than Claude Opus

Kimi K2.5 is 8x cheaper and 4.5x faster than Claude OpusWhether you’re generating code, shipping agents, or building anything else that requires affordable, fast frontier intelligence, try [Kimi K2.5 on Baseten](https://www.baseten.co/library/kimi-k25/) for industry-leading speed on the world’s largest open LLM.
