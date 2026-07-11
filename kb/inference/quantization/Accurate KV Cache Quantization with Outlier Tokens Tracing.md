---
title: Accurate KV Cache Quantization with Outlier Tokens Tracing
topic: inference
subtopic: quantization
secondary_topics:
- inference/optimization
summary: Summarizes research on KV-cache quantization with outlier token tracing to
  reduce LLM inference memory cost while preserving output quality.
source: arize
url: https://arize.com/blog/accurate-kv-cache-quantization-with-outlier-tokens-tracing/
author: Jason Lopatecki
published: '2025-06-05'
fetched: '2026-07-11T04:52:25Z'
classifier: codex
taxonomy_rev: 1
words: 840
content_sha256: d9380bb9c9e81e114df9be9c0020cc0ed98e0061276da301abdccc5b758c2fc9
---

# Accurate KV Cache Quantization with Outlier Tokens Tracing

Deploying large language models (LLMs) at scale is expensive—especially during inference. One of the biggest memory and performance bottlenecks? The KV Cache.

In a new research paper, Accurate KV Cache Quantization with Outlier Tokens Tracing (OTT), researchers propose a smarter way to compress the KV Cache while preserving model quality. The result: up to 6.4× memory savings and 2.3× faster LLM inference, with minimal accuracy trade-offs.

If you’re working on LLM deployment, model acceleration, or quantization, this technique is something to take note of.

## Watch

## Listen

## Dive in

## Summary: Accurate KV Cache Quantization with Outlier Tokens Tracing

This paper introduces a method to enhance the efficiency of Large Language Model (LLM) inference by addressing the memory and computational challenges associated with the Key-Value (KV) cache. The authors identify that standard quantization techniques often falter due to “outlier tokens”—tokens with atypically small Key vector magnitudes—that disproportionately affect quantization accuracy.

To mitigate this, they propose the Outlier Tokens Tracing (OTT) method, which dynamically detects and excludes these outlier tokens from quantization during decoding, preserving their full-precision representations. This selective approach significantly improves quantization accuracy, achieving up to a 6.4× reduction in memory usage and a 2.3× increase in inference throughput under 2-bit quantization, all while maintaining high model performance. The OTT method is tuning-free and compatible with existing inference engines, making it a practical solution for deploying LLMs in resource-constrained environments.

### Why the KV Cache Matters in LLM Inference

During autoregressive generation, transformer-based models use attention mechanisms that require storing Key and Value vectors from every past token. Instead of recomputing these at every step, the model caches them—hence the KV Cache.

While this speeds up inference (from O(n²) to O(n)), the downside is growing memory usage with sequence length and batch size. This limits parallelism, throughput, and device compatibility, especially for long-form generation tasks. That’s where KV Cache quantization comes in.

### The Challenge With KV Cache Quantization

Quantization maps high-precision floating-point data (e.g., FP16 or FP32) into smaller integer formats (e.g., INT8, INT4, or even INT2), dramatically shrinking the model’s memory footprint.

Quantizing model weights is now standard practice, but quantizing intermediate states like the KV Cache is far trickier. That’s because these tensors are dynamic and data-dependent, and traditional quantization assumes token vectors are statistically similar.

But real-world tokens vary. A lot.

### The Outlier Problem: Small Keys, Big Headaches

Some tokens—especially rare words or symbols—produce outlier Key vectors with significantly smaller magnitudes than the rest. These “outlier tokens” can skew quantization ranges, leading to larger quantization errors for all tokens in a channel.

This degrades attention scores and hurts downstream generation quality—especially on long sequences or code-heavy inputs.

### Outlier Tokens Tracing (OTT): A Smart Quantization Strategy

OTT introduces a simple but powerful idea: identify and exclude problematic tokens from quantization. Here’s how it works:

#### Step 1: Quantization Stage

- KV Cache is processed in groups of G tokens.
- Tokens with lowest Key magnitudes are added to an outlier pool, stored in full precision.
- These outliers are excluded from quantization, and their values are replaced with the group mean (to avoid distorting quantization stats).
- The outlier pool is fixed-size; evicted tokens go into a secondary store.

### Step 2: Decoding Stage

At inference time, the attention mechanism combines:

- Quantized KV Cache (main group),
- Recent full-precision tokens,
- Full-precision outliers from the pool.

Attention scores are computed across all three, using fused GPU-friendly kernels for efficiency.

## Results: Compression Without Compromise

Key Benefits of OTT:

- Memory Usage: Up to 6.4× reduction in KV Cache storage
- Throughput: Up to 2.3× faster LLM inference
- Accuracy: Comparable or even superior to FP16 on standard benchmarks (MMLU, GSM8K, HumanEval)

OTT consistently outperforms prior methods like KIVI on long-form inputs, without requiring any tuning.

Bonus Insight: A small outlier pool (e.g. a few hundred tokens) is enough to recover most of the lost precision. That makes OTT especially efficient.

### When OTT Works Best—and Its Limits

Great for:

- Long-form generation (e.g., summarization, coding)
- Memory-constrained environments (edge, mobile, embedded)
- Scenarios where LLM inference cost and speed matter

Watch Out For:

- Short sequences: Outliers are rare, so benefits shrink.
- Very large contexts: You may need to tune the outlier pool size.
- Extreme quantization (e.g., 2-bit): Some accuracy degradation may remain.
- Tiny batch sizes: Quantization overhead may outweigh gains.

### Practical Takeaways

- OTT is tuning-free and inference-ready. No retraining or model surgery required.
- It works with common inference frameworks that support quantization.
- It’s particularly useful for scaling LLMs in production or deploying to low-power devices.
- It shows that not all tokens are created equal—and treating them that way can unlock real performance gains.

## Final Thoughts

Outlier Tokens Tracing (OTT) demonstrates that intelligent token selection during quantization can dramatically improve LLM efficiency—without sacrificing accuracy. For teams working on LLM optimization, edge deployment, or cost-efficient inference, this is one paper to pay attention to.

Smarter quantization = faster, leaner, and still accurate LLMs.
