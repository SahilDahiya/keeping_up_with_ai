---
title: How we built the fastest GLM-5 on Artificial Analysis
kind: blog
topic: inference
subtopic: speculative-decoding
secondary_topics:
- models/architectures
summary: Details reaching 200+ TPS on the 744B-parameter (40B active) GLM-5 via a
  low-overhead MTP speculative decoding engine, MoE dispatch kernels tuned to its
  deep-narrow architecture, and custom kernels exploiting DeepSeek Sparse Attention.
triage: null
skip_reason: null
source: baseten
url: https://www.baseten.co/blog/how-we-built-the-fastest-glm-5-on-artificial-analysis
author: Madison Kanna
published: '2026-03-04'
fetched: '2026-11-12T06:16:18Z'
classifier: claude
taxonomy_rev: 2
words: 1008
content_sha256: 3965306ef6d41053b7279fc0c9fe1fee375934b5dd7679b03f3d81ab4f8839b7
---

# How we built the fastest GLM-5 on Artificial Analysis

Research
# How we built the fastest GLM-5 on Artificial Analysis

We achieved 200+ tokens per second on GLM-5.


- Authors
- Date
- March 4, 2026

TLDR

Using our low-overhead speculative decoding engine for Multi-Token Prediction (MTP), optimized MoE routing kernels, and inference kernels purpose-built for DeepSeek Sparse Attention (DSA), we achieved 200+ tokens per second on GLM-5 as independently benchmarked by Artificial Analysis.

Today, [Artificial Analysis](https://artificialanalysis.ai) benchmarked our [Model API for GLM-5](https://www.baseten.co/library/glm-5/) and we achieved state-of-the-art results for both time to first token (TTFT) and tokens per second (TPS).

*\[Artificial Analysis benchmark screenshot: 200+ TPS, \~200ms TTFT, fastest on the leaderboard\]*

GLM-5 is Z.ai's latest open-weight flagship is 744B total parameters, 40B active per forward pass, trained on 28.5T tokens, and released under MIT. It is currently the most capable open-source model in the world on coding and agentic benchmarks: 77.8 on SWE-bench Verified, 92.7% on AIME 2026, and #1 among open models on Vending Bench 2.

As a reasoning model, GLM-5 generates a thinking sequence before its final answer, trading more inference compute for better quality. That makes tokens per second the single most important number for production deployments, the thinking sequence is often longer than the final response, and users feel every millisecond of it.

To run GLM-5 at leading speed, we use:

- The [Baseten Inference Stack](https://www.baseten.co/resources/guide/the-baseten-inference-stack/) with baseline optimizations including KV-aware routing.
- Optimized MoE dispatch kernels, tuned to GLM-5's distinctive deeper-but-narrower architecture.
- Custom kernels that exploit DeepSeek Sparse Attention to cut KV cache cost at long context.
- A low-overhead MTP speculative decoding engine built into the Baseten inference stack.

GLM-5 shares its MoE lineage with DeepSeek V3, but Z.ai made a deliberate architectural trade that defines the GLM series: more layers, smaller hidden size. It's deeper but not as wide.

That choice has real consequences at inference time. Deeper means more inter-layer data movement and tighter scheduling constraints per forward pass. A narrower hidden size changes the per-layer compute footprint, and standard MoE kernels profiled against DeepSeek V3's dimensions don't land in their optimal operating regime on GLM-5. Getting peak utilization requires tuning to the actual shape of the model.

GLM-5 also integrates DeepSeek Sparse Attention (DSA) for the first time in the GLM family, which changes the KV cache profile significantly. And on the speculative decoding side, GLM-5 ships with native Multi-Token Prediction heads, meaning there's no need to train or host a separate draft model.

Each of these three design choices required its own optimization on our stack.

In a Mixture of Experts model, MoE dispatch, routing tokens to the right experts and gathering results — is one of the most performance-sensitive parts of the forward pass. The efficiency of that dispatch depends heavily on the hidden dimension and layer count of the model.

GLM-5's profile diverges meaningfully from DeepSeek V3: the narrower hidden size changes the arithmetic intensity of expert computation, and the additional layers compound the cost of any per-layer inefficiency. Generic MoE kernels leave performance on the table here.

Our inference stack includes optimized MoE kernels that are profiled and tuned to GLM-5's specific architecture. This means better GPU utilization per expert call, lower dispatch overhead per layer, and across hundreds of layers.

GLM-5 is the first GLM model to integrate DeepSeek Sparse Attention. DSA sparsifies attention across the sequence, dramatically reducing KV cache footprint at long context while preserving the full 200K context window. For the agentic workloads GLM-5 is designed for: multi-turn tool use, large codebases, extended agent sessions. This is one of the most consequential architectural decisions in the model.

The catch is that standard attention kernels don't exploit the sparsity pattern. A naive implementation falls back to dense attention paths and gives up most of the memory benefit. To unlock DSA's full value, the inference stack has to be explicitly aware of the sparse structure.

Our kernels are built to exploit the DSA pattern directly. The result is that long-context requests stay fast and memory-efficient, which means larger batch sizes, better throughput under load, and a better experience for users running GLM-5 in the kinds of deep agentic workflows it was built for.

Speculative decoding is the most effective way to improve tokens per second without sacrificing quality. The basic principle: generate candidate tokens cheaply with a draft model, then verify them in parallel with the target model. When the target accepts the draft tokens, you get multiple tokens for the cost of one forward pass.

For a model as large as GLM-5, the typical challenge is that there's no smaller model in the same family to use as a draft, and training a custom speculator takes time. GLM-5 sidesteps this entirely by shipping with native Multi-Token Prediction (MTP) heads built directly into the model architecture. The draft tokens come from the same model, with minimal added weight.

Minimal overhead is the key phrase. MTP speculation is only effective if the host-side cost of managing draft tokens doesn't eat into the throughput gains. Our speculative decoding engine is purpose-built for low overhead on MTP: it tightly integrates draft scheduling into the inference loop, keeps host-side coordination lightweight, and achieves high token acceptance rates across the diverse workloads such as code generation, long-horizon reasoning, and agentic tool use that GLM-5 is optimized for.

For a reasoning model that can generate tens of thousands of thinking tokens before a final answer, higher TPS translates directly and linearly into faster end-to-end response time.

*\[Chart: ????\]*

Achieving great benchmark results feels great, but we judge our work by what it enables customers to build.

GLM-5 is purpose-built for complex systems engineering and long-horizon agentic tasks. At 77.8 on SWE-bench Verified it approaches Claude Opus 4.5 on software engineering — and at 200+ tokens per second on Baseten, GLM-5-based applications run significantly faster than Claude while remaining fully open-weight under MIT.

Whether you're running autonomous coding agents, building multi-step tool-use pipelines, or shipping anything that requires frontier-grade intelligence at production speed, try [GLM-5 on Baseten](https://www.baseten.co/library/glm-5/) for industry-leading throughput on the world's most capable open model.
