---
title: 'FireAttention V3: Enabling AMD as a viable alternative for GPU inference'
topic: inference
subtopic: hardware
secondary_topics: []
summary: Describes FireAttention V3 and optimizations that make AMD GPUs more viable
  for inference workloads.
source: fireworks
url: https://fireworks.ai/blog/fireattention-v3
author: null
published: '2024-10-15'
fetched: '2026-07-11T04:15:02Z'
classifier: codex
taxonomy_rev: 1
words: 1848
content_sha256: c423b55ff7671fbefa4e153f9f9181808cbbfc8a51cee70b9e6fc0dd32f0c76c
triage: keep
skip_reason: null
---

# FireAttention V3: Enabling AMD as a viable alternative for GPU inference

This post is the continuation of our FireAttention blog series: [FireAttention V1](https://fireworks.ai/blog/fire-attention-serving-open-source-models-4x-faster-than-vllm-by-quantizing-with-no-tradeoffs) and [FireAttention V2](https://fireworks.ai/blog/fireattention-v2-long-context-inference) . This time we are going to focus on a different GPU hardware, namely [AMD MI300 GPU](https://www.amd.com/en/products/accelerators/instinct/mi300.html).

While spec-wise it looks quite superior to [NVIDIA H100 GPU](https://resources.nvidia.com/en-us-tensor-core/nvidia-tensor-core-gpu-datasheet) we never know how it’s going to perform in real-world LLM inference settings until we run benchmarks, which represent practical LLM usage.

Fireworks has been using AMD MI300 hardware in production since the launch of [LLaMA 405b](https://fireworks.ai/blog/introducing-llama3-1-405b-on-fireworks). In this post we are going to go over the work which made it happen.

FireAttention V3 is an AMD-specific implementation for Fireworks LLM. When measured on 8 MI300 GPUs vs other leading LLM implementations (NIM Containers on H100 and AMD vLLM on MI300) it achieves **1.4x improvement for the average RPS @ 8 secs metric for LLaMA 8B** model and **1.8x improvement for the average RPS @ 10 secs for LLaMA 70B** model. In some low-latency scenarios RPS improvement can reach **up to ~3x for NIM** and **up to ~5.5x for AMD vLLM**. It even **improves minimal achievable latency for LLaMA 8B model by 1.6x**.

To tell the truth, we were pleasantly surprised at how smooth it was to port our proprietary stack to ROCm and get to functional parity - i.e. all functionality working correctly. We leveraged [PyTorch’s official ROCm support](https://pytorch.org/blog/pytorch-for-amd-rocm-platform-now-available-as-python-package/), which matured a lot over the past few years. For custom CUDA code, with the exception of advanced APIs, most of API calls are [supported on ROCm](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/index.html) and are converted automatically when running the hipify utility.

That said, automatic porting falls short when the best performance is needed.

Although there are few [HIP porting guides](https://rocm.docs.amd.com/projects/HIP/en/docs-5.7.1/user_guide/hip_porting_guide.html), we’ve decided to emphasize some LLM-specific performance gotchas, some of which are not widely covered. Also, most of the HIP porting guides are written by AMD themselves, while AMD is not incentivized to cover AMD performance issues, while we being a neutral third-party can do a more unbiased analysis.

Warp size is 64 on AMD vs 32 on NVIDIA. There are still 4 SIMDs (same as 4 schedulers on NVIDIA SMs), and there are still 32 shared memory banks, each 32 bits wide (this makes bank conflicts a bit trickier to reason about).

Number of SMs (aka Compute Units) is significantly larger: 304 (MI300) vs 113 (H100), but shared memory is way smaller: 64 KB (shared memory) + 32 KB (L1) on MI300 vs 256 combined shared memory + L1 on H100. HBM is much larger: 192 GBs vs 80 GBs.

We find **theoretical FLOPs and memory bandwidth numbers to be almost useless**. They provide only the upper limit, while achievable numbers can be practically very different. Thus it’s extremely important to benchmark the actual operations.

**Flops-heavy gemms are inferior to NVIDIA** [cuBLAS](https://docs.nvidia.com/cuda/cublas/) / [CUTLASS](https://github.com/NVIDIA/cutlass). It’s also [reported by other parties for BF16](https://github.com/stas00/ml-engineering/blob/master/compute/accelerator/README.md#maximum-achievable-matmul-flops-comparison-table). We see a similar difference for FP8: ~1.2 PFLOPs MI300 vs ~1.5 PFLOPs H100.

We attribute this inferiority to the suboptimal power management based on the new [Smart Shift technology](https://community.amd.com/t5/corporate/how-amd-is-advancing-the-30x25-energy-efficiency-goal-in-high/ba-p/650223) . We hope that it can be improved in the upcoming firmware upgrades. Curious readers can just compare performance of gemms with real data vs just zeros. On MI300, this difference reaches up to 2x, while much less on H100. [Gritty details are here](https://www.thonking.ai/p/strangely-matrix-multiplications).

**Memory bandwidth is  higher on MI300**. Although we can’t quite reach advertised numbers (likely due to the fact that we use NPS 1 partitioning and there are 2 HBM banks per XSD), achieved memory bandwidth on MI300 is still better vs H100.

bfloat16 types: `__nv_bfloat16` vs `__hip_bfloat16` (and other vector types), float8 types: `__nv_fp8_e4m3` vs `__hip_fp8_e4m3_fnuz` (and other vector types) are not covered by the hipify utility and have to be taken care by a programmer.

Although cooperative groups API is partially supported, the most important reductions operations are not. Thus it’s better not to use cooperative groups API for portable code and prefer more narrowly targeted portable libraries like [NVIDIA CUB](https://nvidia.github.io/cccl/cub/) vs [hipCUB](https://github.com/ROCm/hipCUB)

Note, these types are different: [NVIDIA FP8](https://arxiv.org/pdf/2209.05433) vs [AMD FP8](https://arxiv.org/pdf/2206.02915.pdf) . This practically means that max is 448 (nvidia) vs 240 (amd). At the same time we found that AMD fp8 numerics typically yield a bit better accuracy according to our [quantization evaluation benchmarks](https://fireworks.ai/blog/fireworks-quantization) (although this difference is quite negligible compared to other differences, like whether to use FP8 for QKV matrix, whether to use channel scaling etc).

[hipBLASLt](https://github.com/ROCm/hipBLASLt) is the ‘state-of-the-art’ library for matrix multiplications. It supports both fp16 and fp8 compute (including mixed precision). Although grouped gemms are supported, fp8 currently only works over mixed precision (hence only fp16 compute). This makes **MoE models currently non-competitive on AMD**. We are looking forward to hipBLASLt library to support fp8 compute for grouped gemms.

Kernel-level LLMs optimization is mostly about two operations: matmuls and attention (which in turn is a specialized fused matmul). To achieve the best performance, we had to re-write our attention kernel from scratch. The reason is that performant versions of attention have to rely on matrix core ops (tensor core on NVIDIA), while shapes and element swizzling formats are totally different on AMD. Although there is async copy support on AMD, there is no TMA yet. Combined with quite different shared memory size, all these differences lead to totally different design choices.

Fireworks excels at providing cost-effective low-latency solutions for high traffic use cases. We picked two quite common cases both demanding low latencies while requiring to handle high volume of requests per second (RPS).

We are running all models in fp8 precision (weights, activations and kv-caches) to ensure that we fully utilize GPU compute capabilities.

There are many LLM implementations for NVIDIA hardware. To keep the highest baseline we chose to compare against [NIM Containers](https://docs.nvidia.com/nim/large-language-models/latest/introduction.html), which is based on [TensorRT LLM](https://github.com/NVIDIA/TensorRT-LLM), one of the most performant OSS libraries. Unlike TensorRT LLM, which is notoriously hard to build and run, NIM is a breeze to get started with. Using containers also precludes the possibility of misconfiguring TensorRT LLM.

There is not much of a choice for AMD, with [AMD’s fork of vLLM](https://github.com/ROCm/vllm) being the only viable high-performance solution. We also use [pre-built containers](https://hub.docker.com/r/powderluv/vllm_dev_channel) with [the recommended performance settings](https://github.com/powderluv/vllm-docs/tree/main?tab=readme-ov-file#vllm-performance-settings) to achieve optimal performance.

Because we target high RPS cases, we benchmark on 8 GPUs. We chose the flagship H100 for NVIDIA and MI300 for AMD. Although H200 is also on the market, its availability (especially on public clouds) is quite sparse and requires quite some $$ premium.

To ensure that we evaluate all possible configurations for both NIM and AMD vLLM, we shard models on 1, 2, 4 and 8 GPUs. To get the final throughput numbers, we multiply resulting RPS by 8, 4, 2 and 1 respectively.

For Fireworks LLM, we use two modes (both geared towards lower latencies): first one is to achieve higher throughput (we call it ‘fw throughput optimized’ mode) and the second one is to achieve lower latencies (we call it ‘fw latency optimized’ mode).

During benchmarks, we’ve disabled any data-dependent optimization techniques like speculative decoding and prompt caching.

We will introduce two new metrics to more objectively measure LLM performance under low latency constraints.

*Minimum achievable latency.*

This metric measures the “speed of light” i.e. how fast a given LLM implementation can perform, when cost is not an issue. This is typically measured at the lowest batch size, i.e. 1.

** Average RPS @ given latency threshold**.

This measures throughput i.e. requests per second, which can be achieved under a certain latency threshold. Just choosing a single threshold value produces a very biased metric. Thus we compute an average of RPS values: we vary latency from the minimum achievable up to the given threshold, computing corresponding RPS and calculating the average of RPS values in the end.

When reporting the metrics above we report an improvement i.e. a ratio of metric values from two different LLM implementations.

The first use case involves medium LLaMA 3.1 70B models with 8000 input and 256 output tokens.

As H100 has only 80 GBs of HBM, we can’t fit the model on a single GPU (thus we don’t have ‘nim 1x8’ mode).

We then pick the best performing modes for throughput and latency regimes and compare them to Fireworks LLM. Throughput regime has latency threshold of 20 secs while latency regime is much lower of 10 secs.

Summary of results:

| Average RPS improvement (Fireworks vs NIM, vLLM) | Minimum latency improvement (Fireworks vs NIM, vLLM) | |
|---|---|---|
| Throughput | 1.3x at 20 secs | 1.1x |
| Latency | 1.8x at 10 secs | 1x |

It’s easy to see that Fireworks LLM has a large improvement over NIM / AMD vLLM in both throughput and latency modes we’ve defined (purple-shaded areas). In some low-latency cases (e.g. ~6 secs cutoff), Fireworks LLM gets **up to ~3x improvement over NIM** and **~5.5x RPS improvement over AMD vLLM**.

It’s also easy to see that NIM has a bit of an edge over AMD vLLM (green-shaded areas).

The second use case involves a small LLaMA 3.1 8B model. Because of model size, it’s quite affordable to have a larger context. Here we choose 30000 tokens. We keep the same amount of 256 output tokens.

Although the 8B model can be sharded on 4 and 8 H100 GPUs, NVIDIA intentionally doesn’t provide so-called ‘profiles’ for more then 2 GPUs. We surmise that the reason for this is that it’s quite inefficient to run tensor parallelism for such a small model on 4 and 8 GPUs. We can easily see that for ‘vllm 4x2’ and ‘vllm 8’ modes.

We then pick the best performing modes for throughput and latency regimes and compare them to Fireworks LLM. Similar to the 70B model, we set throughput mode threshold to 8 secs and latency mode threshold to much lower 4 seconds.

Summary of results:

| Average RPS improvement (Fireworks vs NIM, vLLM) | Minimum latency improvement (Fireworks vs NIM, vLLM) | |
|---|---|---|
| Throughput | 1.4x at 8 secs | 1.6x |
| Latency | ∞ at 4 secs | 1.6x |

Fireworks LLM outperforms both NIM and AMD vLLM by a wide margin in the low-latency mode, as they are not able to meet the minimum threshold of 4 seconds. Fireworks LLM also has an edge in the throughput mode.

Similar to the 70B model, NIM Containers are quite superior to AMD vLLM.

Our analysis clearly shows that AMD has provided the GPU LLM inference market with a viable alternative for the first time: MI300 cards, which deliver state-of-the-art results. To reach these results, advanced inference optimizations are still needed, which are currently present only in Fireworks LLM.

At the same time, while memory bandwidth-demanding use cases perform quite well, flops-bound or MoE use cases still call for improvement on AMD hardware.

Performance results in this post do not include either speculative decoding or prompt caching from [FireOptimizer](https://fireworks.ai/blog/fireoptimizer) , which further improve latency and throughput. If you have a demanding gen AI production use case and you want to get the best performance results while maintaining cost efficiency on both NVIDIA and AMD hardware, [reach out to us](https://fireworks.ai/company/contact-us).
