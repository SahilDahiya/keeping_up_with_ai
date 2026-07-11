---
title: 'ParallelKernelBench: Frontier LLMs can''t write fast multi-GPU kernels (yet)'
topic: evals-observability
subtopic: evaluation
secondary_topics:
- inference/hardware
summary: Introduces ParallelKernelBench for measuring whether frontier LLMs can write
  fast multi-GPU kernels.
source: together
url: https://www.together.ai/blog/parallelkernelbench
author: Willy Chan; Nathan Paek; Simon Guo; Simran Arora; Daniel Y Fu
published: '2026-06-23'
fetched: '2026-07-11T04:18:54Z'
classifier: codex
taxonomy_rev: 1
words: 1579
content_sha256: 16685e8b7504b3130eba689c319eca9af6bb7c43d80e991f8c5a7cdfb932dcb2
triage: keep
skip_reason: null
---

# ParallelKernelBench: Frontier LLMs can't write fast multi-GPU kernels (yet)

![](https://cdn.prod.website-files.com/69654e88dce9154b5f12070c/6a2a4b7ff73790a61796c50c_20260610_PKB_1200x744.jpg)

Summary

LLMs have gotten surprisingly good at writing GPU kernels** [1][2][3]**, but almost all current benchmarks measuring that progress are single-GPU. In production, communication is often the bottleneck: communication overhead can account for over 20% of inference latency

**, and that gap keeps widening as compute scales faster than interconnect bandwidth.**

[4][ ParallelKernelBench](https://www.alphaxiv.org/abs/2606.parallel-kernel-bench) (PKB) offers a benchmark and evaluation framework for multi-GPU kernel generation and includes 87 problems from real codebases where the task is replacing PyTorch + NCCL with a CUDA kernel that moves data directly over NVLink. We tested frontier coding models such as GPT-5.5, Gemini 3 Pro, Opus 4.7, and others. The evaluation revealed significant performance gaps across the board: under a third of problems were solved correctly, and fewer than a quarter of those beat the naive baseline.

We'll cover why they fail, what the patterns look like, and a few cases where models surprisingly produced kernels faster than anything publicly available, including one for [NVIDIA NeMo-RL's GRPO training loop](https://github.com/NVIDIA-NeMo/RL/tree/main), which has no prior optimized public reference.

## Why multi-GPU is different from single-GPU kernel generation

LLMs have made progress on GPU kernel generation, but that progress has mostly been measured on a single GPU. Production AI workloads no longer fit that frame: they span multiple GPUs, and performance is increasingly shaped by communication rather than just local compute and memory. That shift makes multi-GPU kernel generation a different problem in three ways:

- **The design space expands combinatorially.**Practitioners compose tensor, expert, data, context, and sequence parallelism to fit the hardware, and each composition creates a different communication pattern.
- **The performance model changes.**A single-GPU roofline is built around compute and memory bandwidth. In multi-GPU code, the bottleneck is often the interconnect.
- **Multi-GPU kernel generation introduces a critical new design choice:**how to move data between GPUs — through the copy engine, TMA, SM load/store, or NVLS — and whether to fuse that movement with compute.

## ParallelKernelBench

We built PKB to test whether models can move beyond pure `torch.dist` and actually write production multi-GPU kernels. Each problem starts from a standard PyTorch + NCCL implementation and a description of the hardware topology. The model then has to replace that reference with a CUDA kernel that communicates directly across GPUs using symmetric memory.

To make sure the 87 problems cover the real space of production parallelism types, we built them from a taxonomy of distributed workloads. First, we identified the major ways models get sharded — tensor, context, data, expert, sequence, and FSDP/ZeRO — along with the communication patterns each one creates. Then we chose 87 problems to cover that space taken from the codebases of systems like [Megatron-LM](https://github.com/nvidia/megatron-lm), [DeepSpeed](https://github.com/deepspeedai/deepspeed), [DeepEP](https://github.com/deepseek-ai/DeepEP), [TensorRT-LLM](https://github.com/NVIDIA/TensorRT-LLM), [NeMo-RL](https://github.com/nvidia-nemo/rl), as well as a long tail of non-LLM workloads: GNN routing, distributed FFTs, Gaussian splatting, etc. Another benefit is that because PKB references are written in standard PyTorch + NCCL, the benchmark is not tied to any single, particular hardware generation. Instead, it is designed to naturally evolve alongside next-generation hardware architectures.

Before evaluating models, we first checked whether the PyTorch + NCCL baselines leave real headroom. A communication-aware roofline says yes: most PKB problems are bottlenecked by NVLink, and the baselines run far below the hardware ceiling. So the next question is simple: can models close that gap?

## How frontier models do on PKB

**Not well.** In the zero-shot setting, the best model solves 28 of 87 problems, and only 22 of those solutions are faster than the PyTorch + NCCL baseline. Sampling three attempts improves the best result to 36 correct solutions and 27 faster-than-baseline solutions, but fast1@3 still tops out at 31%.

The successes are concentrated in familiar patterns: collective primitives, tensor-parallel GEMMs, and Ulysses-style context parallelism, which splits the sequence dimension across attention heads using all-to-all communication. These are the parts of the multi-GPU stack most visible in open-source code, so models likely have stronger priors for them.

The failures suggest a deeper issue than CUDA syntax. Weaker models often fail to compile, but stronger reasoning models frequently produce kernels that compile and return incorrect results. The hard part is reasoning about rank coordination, data partitioning, and collective ordering.

Generated kernels also use a very narrow set of communication mechanisms. Most rely on copy engines or SM load/store instructions, while more specialized mechanisms such as TMA and NVLS are almost absent. In many cases, models do not choose the mechanism needed for peak performance. We attribute this to a combination of data scarcity and hardware complexity: newer primitives like TMA and NVLS require navigating intricate, hardware-specific abstractions, such as asynchronous copy descriptors or newer NVLink topologies, where models lack strong priors. That leaves a large gap between “working” distributed kernels and genuinely optimized ones (a clear target for future work!)

The natural next step is to give the model the same feedback loop a human kernel writer would use. We wrapped Gemini 3 Pro in an [agentic harness](https://github.com/SWE-agent/mini-swe-agent) with access to the repository, a terminal, compiler output, correctness tests, speed measurements, and its previous attempts. Instead of producing one kernel and stopping, the model could compile, run the benchmark, inspect failures, and revise.

This helped, but the practical gains are modest. Gemini 3 Pro improved from 24 correct solutions in the single-shot setting to 35 out of 87, with 26 kernels beating the PyTorch + NCCL baseline. The gains came from fixing syntax errors, shape mistakes, and simple runtime bugs. After roughly 20 refinement steps, performance plateaued. Feedback helps models debug distributed kernels, but the remaining failures highlight a much bigger gap: an inability to reason about rank coordination, communication ordering, and the optimal choice of GPU-to-GPU transfer mechanisms.

## Net new kernels

Beyond speedups on standard collectives, single-shot generation occasionally surfaces genuinely new high-performance kernels for workloads with no optimized public reference. This capability offers a preview of the broader potential for AI-driven optimization; wins are not limited to Transformers, as models can do well on state-space models, genomic pipelines, and multimodal RL loops — domains where specialized kernels remain largely unoptimized compared to mainstream LLM stacks.

Below are three examples, each replacing NCCL collectives with fused symmetric-memory kernels that move data directly over NVLink. Each was verified for correctness over 4 H100 GPUs and 100 randomized runs; speed measurements follow the benchmarking methodology in [ThunderKittens 2.0](https://hazyresearch.stanford.edu/blog/2026-02-19-tk-2)[[5]](https://nathanjpaek.github.io/parallel-kernel-bench/#ref-thunderkittens)(bitwise-identical inputs, L2-aware input groups, 500 warmup iterations, and 100 back-to-back profiling iterations).

### NeMo vocab-parallel log-prob with top-*k*/top-*p* filtering (Gemini 3 Pro)

A core step in NVIDIA NeMo-RL's GRPO training loop: compute vocabulary-sharded log-probabilities under a top-*k*/top-*p* filtered distribution. The PyTorch + NCCL baseline gathers the full vocabulary across ranks before filtering; the generated kernel skips those collectives entirely, using symmetric memory to permute shards inline while fusing log-softmax, token extraction, and target gather into a single warp-shuffle reduction.

*M*∈ {1024, 2048, 4096, 8192, 16384}. Config: 4 ranks,

*B*= 1,

*V*= 32,000 (8,000 local vocab per rank), top-

*k*= 10, top-

*p*= 0.9.

### Hyena forward context parallelism (GPT-5.5)

The context-parallel forward pass for the Hyena operator, where FFT convolution needs sequence-global context. The reference alternates between sequence- and channel-sharded layouts via repeated `all_to_all` calls; the generated kernel packs inputs into one symmetric allocation and streams remote slices over NVLink, computing gating and reindexing in a unified pass. Notably, performance degrades at longer sequence lengths.

*l*∈ {1024, 2048, 8192, 16384} on 4 GPUs. Correctness and speed measured over 100 trials.

### SAM 3 all-gathered mask IoU suppression (GPT-5.5)

Cross-GPU duplicate suppression for SAM 3 video segmentation: after each frame, ranks compare predicted regions via intersection-over-union and zero out overlapping masks. The baseline uses variable-length `all_gather` collectives plus a dense matmul; the generated solution collapses this into a pipeline of symmetric-memory kernels that bitpack masks and compute pairwise overlap with hardware popcount.

## Further research

PKB is intentionally scoped to intra-node NVLink today. The natural extensions are inter-node fabrics — RoCE, InfiniBand — where the device-side API landscape is younger, and other accelerators and topologies like TPUs. We'd also like to know whether higher-level abstractions help or hurt: PKB already accepts [Triton](https://triton-lang.org/main/index.html) and [ParallelKittens](https://hazyresearch.stanford.edu/blog/2025-11-17-pk) solutions, and emerging interfaces like NCCL GIN and NVSHMEM are worth studying as targets. Expanding support to these paradigms will encourage further research into how AI agents navigate diverse programming models and hardware abstractions.

The broader goal is a concrete target for the harder problem behind all of this: LLM systems that can autonomously optimize and manage large-scale distributed infrastructure. For infrastructure custom-built for language model training and inference, achieving this autonomy could ultimately bridge the gap to AI agents capable of handling their own end-to-end research engineering.

We're releasing PKB as an open benchmark to push on that. If you want to dig in or contribute problems — especially inter-node ones — we'd love to hear from you. Feel free to email **willychan2022@gmail.com** or **npaek@together.ai**!

## References

- Standard Kernel. [Reimagining Kernel Generation at the PTX Layer: An LLM System Learning from DSLs to Outperform Them](https://standardkernel.com/blog/reimagining-kernel-generation-at-the-ptx-layer-learning-from-and-outperforming-dsls/). Standard Kernel Blog, April 2026.
- Robert Tjarko Lange, Qi Sun, Aaditya Prasad, Maxence Faldor, Yujin Tang, and David Ha. [Towards Robust Agentic CUDA Kernel Benchmarking, Verification, and Optimization](https://arxiv.org/abs/2509.14279). arXiv:2509.14279, 2025.
- Carlo Baronio, Pietro Marsella, Ben Pan, Simon Guo, and Silas Alberti. [Kevin: Multi-Turn RL for Generating CUDA Kernels](https://arxiv.org/abs/2507.11948). arXiv:2507.11948, 2025.
- Raja Gond, Nipun Kwatra, and Ramachandran Ramjee. [TokenWeave: Efficient Compute-Communication Overlap for Distributed LLM Inference](https://arxiv.org/abs/2505.11329). arXiv:2505.11329, 2026.
- Stuart Sul and Chris Ré. [ThunderKittens 2.0: Even Faster Kernels for Your GPUs](https://hazyresearch.stanford.edu/blog/2026-02-19-tk-2). Hazy Research, February 2026.
