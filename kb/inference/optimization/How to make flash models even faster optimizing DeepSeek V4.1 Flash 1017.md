---
title: 'How to make flash models even faster: optimizing DeepSeek V4.1 Flash 1017'
kind: blog
topic: inference
subtopic: optimization
secondary_topics: []
summary: Details optimizing 80+ kernels for the 552B-parameter DeepSeek V4.1 Flash
  MoE using kernel fusion, Programmatic Dependent Launch, and host-loop minimization,
  reaching 991 output tokens/s on Artificial Analysis.
triage: null
skip_reason: null
source: baseten
url: https://www.baseten.co/blog/how-to-make-flash-models-even-faster-optimizing-deepseek-v41-flash-1017-fast
author: Alex Korte
published: '2026-11-10'
fetched: '2026-11-12T06:06:46Z'
classifier: claude
taxonomy_rev: 2
words: 1795
content_sha256: 346b08b306250083b57d6cfd9444cbfb3cac683aefcc193c560f199e84d17d6d
---

# How to make flash models even faster: optimizing DeepSeek V4.1 Flash 1017

Model performance
# How to make flash models even faster: optimizing DeepSeek V4.1 Flash 1017

We applied techniques like kernel fusion, Programmatic Dependent Launch (PDL), host loop minimization to optimize a cost-effective and high quality open model.


- Authors
- Date
- November 10, 2026

TLDR

Many models are now orders of magnitude better than humans at kernel work. Profiling, rewriting, and benchmarking are well-defined and verifiable, making this the ideal task for an agent to hill-climb. We used our internal harness to optimize 80+ kernels and bottlenecks for DeepSeek V4.1 Flash 1017 to create the Fast variant. The model is on Artificial Analysis at 991 output tokens/s and the lowest time per task (Parento frontier). This post shares how we applied techniques like kernel fusion, Programmatic Dependent Launch (PDL), and host loop minimization.

Flash models now dominate the low-cost Pareto frontier.

These mid-sized models deliver fast, affordable intelligence suitable for most development work. For example, DeepSeek V4.1 Flash 1017 at native precision is a 552B-parameter MoE, with 8B active during prefill and 16B active during decode, but scores 32 on the new Artificial Analysis V5.0 Index, the same score as GLM-5.3. And it does so at approximately ⅓ the cost and 4x the speed of the larger model.

This makes flash models perfectly suited for the execution and implementation subagents that handle token-heavy, multi-turn tasks that main agents running on the most powerful, costly models can delegate to. And with the end of tokenmaxxing leaderboards and cost per task now central to every enterprise’s evaluation of agents and models, flash variants are the balanced choice for quality and economics.

Figure 1. DeepSeek V4.1 Flash 1017 staked its claim at launch to a spot on the Pareto frontier of price and intelligence.

Further, the harness can magnify the cost-effectiveness of a model. In [Cline’s testing,](https://x.com/cline/status/2111434657732640792https://x.com/cline/status/2111434657732640792) this new DeepSeek flash model outperformed 5.6 Sol on Terminal-Bench 4.0 while being \~17x cheaper.

But what if flash models could be even faster and more optimized than how they come out-of-the-box? We believe that in order to fully realize the potential and promise of flash models, the inference infrastructure behind them needs to be optimized for the demands and constraints around a model’s size, architecture, and usage patterns. And that’s what we did for this DeepSeek model.

We previously shared our [high-level approach to inference engineering for day-zero performance](https://www.baseten.co/blog/how-we-built-the-new-fastest-api-for-glm-52) on open models, covering techniques like KV-aware routing, P/D disaggregation, and speculative decoding. This article details three new optimizations that are closest to the hardware layer: kernel fusion, Programmatic Dependent Launch (PDL), and host loop minimization. We plan on releasing open-source work around each of these topics soon.

CUDA is NVIDIA’s platform for writing code that runs on their GPUs. A user-defined function in CUDA is called a kernel. Any inference system uses many kernels, which execute code for steps like matrix multiplication and addition in parallel on GPUs. Frontier LLMs are extremely good at writing kernels because kernel performance is a well-defined, verifiable task. At Baseten, we’ve been experimenting with building custom agents and harnesses specifically for writing fast kernels, with [promising results](https://www.baseten.co/blog/agentic-kernels-in-production).

However, the speed of the kernel itself is not always the bottleneck. If one kernel’s output is another kernel’s input, that data takes an unnecessary round trip through VRAM:

1. Kernel A writes its results to memory to store results
2. Kernel B reads those results from memory to continue computation

Kernel fusion is a technique for combining two or more kernels together to avoid this round trip as well as fix overhead costs from kernel launches. In a fused kernel, intermediate results stay in fast on-chip memory. Given that a forward pass through any LLM with a modern transformer architecture requires running many kernels, fusion is an important technique for inference optimization.

Let us look at a simple example: QK-norm. Without fusion, the chain of small kernels is: normalize Q, normalize K, then apply RoPE to each. Q and K go through VRAM between every step. But the fused version reads Q and K once, then normalizes and applies RoPE to both, then finally writes out the final tensors.

A more complex example is the Mixture of Experts (MoE) layer found in most frontier open models today. A fused MoE kernel combines routing tokens to their experts (the scatter), the expert linear projections, the activation, and the gather, all into a single function. We engineered an improved fused router kernel, which ultimately also decreases decode time by 2.7ms. To do this, we first sampled the model to get outputs within its distribution. Then, we ran our internal kernel harness for fusion and attempted to maintain the same numerical precision while shaving down latency.

A third example of a fused kernel that pertains most to DeepSeek V4.1 Flash 1017 is the mHC (Manifold-Constrained Hyper-Connection) kernel.

You can think of a Hyper-Connection as a richer, more complex form of residual connections. Instead of forcing all layers into one stream, there are multiple streams with learned pre/post mappings to increase expressivity via sharing and mixing. However, the increased diversification can lead to training instability and challenges while scaling.

As a solution, mHC was introduced earlier this year; it constrains the residual mixing by projecting the connection space into a specific manifold. This manifold keeps the stream stable, which removes a source of vanishing/exploding gradients. Our team improved on the open-source megakernel for mHC in DeepInfer for lower latency at batch size 1 and increased speed by 30%. These examples are 3 of the 80+ kernels that we iterated on, which in aggregate sum to a non-trivial increase in performance.

Although kernel fusion lowers the number of total launches and I/O time, the decode step still involves running hundreds of them in a particular, serial order. This is because kernels later in the timeline often depend on data produced by earlier kernels. As a result, not all kernels can be parallelized in CUDA streams. But is there anything we could do to reduce the idle time and increase utilization in the activity timeline?

The answer turns out to be yes, with PDL (Programmatic Dependent Launch). Usually, kernel B can’t start in the timeline until kernel A has fully finished and flushed its results to memory, which creates a gap where B’s blocks are being scheduled and A’s last stragglers are draining.

However, almost all kernels have a preamble section that handles zeroing buffers and prefetching or loading weights from the VRAM into on-chip memory. Specifically, kernel A signals via `cudaTriggerProgrammaticLaunchCompletion()` that kernel B may launch. B runs independent work that does not depend on A’s output, then blocks via `cudaGridDependencySynchronize()` until A’s results are available in global memory.

The tight interleaving of kernel execution allows us to maximize the utilization of timelines without compromising the quality of the results. As an example, NVIDIA previously cited an expanded PDL implementation as one of the reasons behind its 2.8x Blackwell throughput gains on DeepSeek-R1, where it lowered launch latencies and increased throughput across interactivity levels.

The overlap between kernels on B200s (Blackwell) is grid-granular. B’s blocks can start, but the dependent part of B waits for *every* thread block of A to flush its results to global memory. In contrast, Vera Rubin makes the dependency finer-grained. A consumer thread block can begin its dependent work as soon as the data it needs has landed, rather than waiting on the whole grid. The reduced wait time converts to lower kernel-to-kernel latency. Generally, by understanding the model architecture deeply for open models, you can focus on turning on PDL in the parts that involve heavy weight reading to maximize overlap of execution.

Back to the mHC kernel we optimized in the previous fusion section, it is also a good place for PDL. Take one projection inside an mHC block: it requires both the mHC fixed weights and the residual x from the previous kernel (fused all-reduce + post-processing kernel). Using PDL, a CTA (threadblock) can prefetch its slice of the mHC weights (the learned hc\_fn) into L2 without depending on the residual stream completing first. Ultimately, PDL improves tokens per second in long sequential decode loops that are representative of agentic workloads and is a second lever we push on extensively.

While kernel fusion and PDL both optimize the schedule on the GPU, the CPU can also bottleneck computation and performance. The host loop is a CPU-side control loop that manages the workload on the GPU: preparing inputs and launching each kernel. Because launches are asynchronous, the CPU should run ahead of the GPU, leaving a backlog of pending work. However, when the GPU gets ahead and has no work, the host loop becomes the thing limiting output.

In SGLang (which serves DeepSeek V4.1 Flash), the Python scheduler is the host loop. And because Python is slow, kernels often finish before the scheduler has had time to queue the subsequent ones. This is not an issue for larger models because their kernels take longer to run, but on Flash models with fewer active parameters on fast hardware, the scheduler constrains throughput.

We tackled this problem by leaning into CUDA graphs. CUDA graphs allow you to record a sequence of GPU operations and play the entire sequence through a single launch on the host without drivers validating each individual kernel launch.

During inference, decode is simple because every step has the same shape, a fixed number of tokens per sequence, with only batch size varying, so we can capture the whole pass in a single CUDA graph per batch size. However, prefill is harder because input lengths are user-determined. This means the computation has points where the host needs to intervene (chunk boundaries, padding, building attention metadata).

For the prefill case, we turned on breakable CUDA graphs in SGLang. Instead of scheduling hundreds of kernels one by one, kernels can be grouped into a minimal set of graphs that reduces the number of launches required. Overall, this shaves off the per-kernel launch cost from the Python scheduler’s critical path, eliminating GPU idling between kernel launches that is especially felt on flash models.

To serve Flash models at their full potential means eliminating inefficiencies at every layer of the inference stack. For DeepSeek V4.1 Flash, the levers closest to the hardware were fusing and creating kernels, launching them with maximum overlap through PDL, and cutting the work a Python scheduler has to do per step with a minimal set of CUDA graphs.

The broader engineering lesson is that a deep understanding of the model and GPU architecture, coupled with agent horsepower that can optimize on the variables closest to the hardware, is the recipe for serving highly intelligent tokens at the lowest possible cost and latency.

Try [DeepSeek-V4.1-Flash 1017 Fast](https://www.baseten.co/library/deepseek-v41-flash-1017-fast) on Baseten Model APIs today.
