---
title: 'FireAttention V4: Industry-Leading Latency and Cost Efficiency with FP4'
topic: inference
subtopic: quantization
secondary_topics: []
summary: Covers FP4 and B200-focused FireAttention V4 optimizations for latency and
  cost-efficient serving.
source: fireworks
url: https://fireworks.ai/blog/fireattention-v4-fp4-b200
author: null
published: '2025-05-28'
fetched: '2026-07-11T04:14:43Z'
classifier: codex
taxonomy_rev: 1
words: 934
content_sha256: c111fcc8293ba69265d99887fe966002d00ef292b752beeb032bd20f57aec4ad
triage: keep
skip_reason: null
---

# FireAttention V4: Industry-Leading Latency and Cost Efficiency with FP4

Today, we’re announcing we've achieved industry-leading speeds of >250 tokens/second on NVIDIA B200 GPUs using our latest FireAttention V4 inference engine.

FireAttention V4 achieves top-tier latency, throughput and cost efficiency, as measured by independent benchmarks, by leveraging FP4 (and specifically NVFP4) as the optimal precision for Blackwell architecture, just as FP16 was for Ampere and FP8 for Hopper.

B200 deployments using FireAttention V4 with FP4 are now available to enterprise customers who need the best latency, throughput and cost-efficiency. [Contact us](https://fireworks.ai/company/contact-us) or reach out to your Fireworks representative.

NVIDIA Blackwell architecture is the first GPU generation to enable hardware-native micro-scaling support. While it has many micro-scaling modes, namely NVFP4, MXFP4, MXFP6 and MXFP8 , NVFP4 is the most interesting option. The reason is that unlike MXFP6 and MXFP8 modes, it has 2x FLOPs throughput and needs ~1.5x-2x less memory reads. Additionally, unlike MXFP4, it offers significantly better quality, according to our tests. We attribute the drop in quality with MXFP4 to less granular scales (block size 32 vs 16) and the fact that NVFP4 allows the use of mantissa from FP8-based scales, which seems more important for small block sizes.

Every GPU architecture comes with a “highest ROI” precision. For Ampere it’s FP16, for Hopper - FP8 and for Blackwell - NVFP4. While it’s possible, e.g. to run FP8 models on Blackwell, it doesn’t make as much sense from the price-to-performance standpoint. Theoretical FLOPS and memory bandwidth increased ~2x from Hopper to Blackwell, which means that the actual end-to-end performance for FP8 LLMs is improved about ~1.5-1.7x due to other performance overhead. Given the scarce hardware availability for B200 GPUs and higher pricing, it makes it less appealing for running FP8 workloads.

Overall, we are pleasantly surprised by the quality the NVFP4 format delivers. Hats off to NVIDIA! (see Quality Analysis for details below).

Thus in our tests, we’ve primarily focused on NVFP4 precision on Blackwell and FP8 precision on Hopper.

We’ve fully revamped our backend implementation to provide efficient support for FP4 precision. Optimized versions of gemm, grouped gemm, and attention kernels need to be written from scratch as previous Hopper operations rely on 9.0a architecture, which can’t be executed on Blackwell. The “a” in CUDA architecture target name signifies that the instructions aren’t forward-compatible. New TensorCore Gen 5 instructions have to be used instead.

We ran our performance benchmarks on [DeepSeek V3 0324](https://huggingface.co/deepseek-ai/DeepSeek-V3-0324) as a frontier, non-reasoning OSS model. For our performance data, we benchmarked cutting-edge GPU hardware supporting FP8 and FP4 modes running on the most performant OSS inference engines.

We choose H200 for FP8 precision on [SGLang](https://github.com/sgl-project/sglang) and B200 for FP4 precision on [TRT-LLM](https://github.com/NVIDIA/TensorRT-LLM). We compare these setups against FireAttention running on B200. We deployed the most common setup, running on 8 GPUs with NVLink.

Our benchmark setup disables speculation support (“MTP” in DeepSeek model). While speculation greatly improves inference performance of DeepSeek V3, it’d benefit all measured configurations in a similar way. Speculation success being very prompt-dependent makes it hard to compare across implementations.

We were not able to fully validate TRT-LLM FP4 performance on B200 due to [setup complexity](https://semianalysis.com/2025/05/23/amd-vs-nvidia-inference-benchmark-who-wins-performance-cost-per-million-tokens/). We are working with NVIDIA on this and will revisit benchmarks once setup issues are resolved and/or NIM containers become available.

In order to do ‘apples-to-apples’ comparisons on quality benchmarks, we need to re-run exactly the same benchmarks against different LLM implementations, as the exact prompt used during benchmarking and the strategy to extract results can affect the final accuracy metrics quite a bit.

We wrote before about our approach to [evaluate quantization model quality](https://fireworks.ai/blog/fireworks-quantization) using KL-divergence. Unfortunately, not all LLM implementations return log probabilities in the response. This makes it impossible to run KLD tests. Thus, we can only rely on benchmarks with enough data points like MMLU and MMLU Pro (with over 10K examples they provide a statistically significant measurement). We ran MMLU in a 5-shot non-CoT mode, which is not suited for thinking models like R1.

Here are our key findings on FP4 quality:

- •FireAttention V4 outperforms TRT-LLM by a significant margin
- •MMLU Pro has much more discriminative power for frontier models compared to MMLU, especially when evaluating quantization quality
- •Reasoning models recover quality through the longer thinking phase

While FP4 precision provides a good quality/throughput tradeoff (especially for R1 reasoning model), it does have a quality drop. Luckily, with fine-tuning, model quality can be fully recovered using Quantization-Aware Training (QAT). We [wrote on this topic before](https://fireworks.ai/blog/fine-tuning-deepseek-models). This time, we will explore how the same idea applies to FP4 models.

To demonstrate the effectiveness of our QAT implementation for FP4, we utilized the [text-to-SQL dataset](https://huggingface.co/datasets/b-mc2/sql-create-context) to fine-tune on 10,000 rows and evaluate on 1,000 rows. We used the DeepSeek V2 Lite Chat model. This model serves as a good proxy for DeepSeek V3/R1, as it is a MoE model with a similar architecture, albeit much smaller in size.

We first measured the baseline without QAT: fine-tuning happens using LoRA in bfloat16, then LoRA is merged into the base model, which is then quantized to the precision used in serving (FP8 or FP4). Without QAT the quality is significantly degraded. We also observe that FP8 QAT outperforms FP4 QAT. This is expected as during training, FP8 QAT converges faster (it has more precision and dynamic range at its disposal).

Fortunately, we don’t need to sacrifice model quality when using FP4. With training on more data, both QAT precisions converge to the same final eval loss.

B200 deployments using FireAttention V4 with FP4 are now available to enterprise customers who need top-tier latency, throughput and cost-efficiency. [Contact us](https://fireworks.ai/company/contact-us) or reach out to your Fireworks representative.
