---
title: 'Speed, Python: Pick Two. How CUDA Graphs Enable Fast Python Code for Deep
  Learning'
topic: inference
subtopic: kernels
secondary_topics: []
summary: Explains how CUDA Graphs reduce Python overhead for fast deep-learning execution.
source: fireworks
url: https://fireworks.ai/blog/speed-python-pick-two-how-cuda-graphs-enable-fast-python-code-for-deep-learning
author: null
published: '2023-08-29'
fetched: '2026-07-11T04:18:16Z'
classifier: codex
taxonomy_rev: 1
words: 2933
content_sha256: 5974623dbc8e36cd60d39b6e3d34060a15e1331a4e2897a942d62df13988b483
triage: keep
skip_reason: null
---

# Speed, Python: Pick Two. How CUDA Graphs Enable Fast Python Code for Deep Learning

- Keeping Modern GPUs Busy: CPU/GPU Overlap
- CPU Overheads — Where Does All The Time Go?
- Feed the (GPU) Beast: Optimizing for CPU Overheads
- CUDA Graphs
- LLM Inference + CUDA graphs
- Real-World CUDA Graphs: LLaMA v2 Inference
- LLaMA2–7B + CUDA Graph Inference Performance Results
- CUDA Graphs in the Fireworks Inference Platform
- Conclusion
- Appendix

This is the second in a series of technical blog posts about the techniques we use for optimization of the high-performance [Fireworks Gen AI Platform](https://fireworks.ai/). See also the previous post about [Multi-Query Attention](https://fireworks.ai/blog/multi-query-attention-is-all-you-need-db072e758055).

*This post explores how the explosion in GPU speed over the past several years has changed the landscape of performance optimization for deep learning workloads. We examine how the host CPU has become a bottleneck due to this trend and review several techniques for mitigating this. We highlight one technique — CUDA graphs — that balances performance with usability. We examine the effect of CUDA graphs on Large Language Model (LLM) inference workloads and show a* **2.3x speedup on a LLaMAv2–7B inference workload**.*We show that the* *Fireworks Inference Platform**uses CUDA graphs and other aggressive machine and service optimizations to provide best-in-class speed and efficiency for LLM serving.*

Contemporary deep learning programs are most often written in the Python language using PyTorch as a framework. PyTorch is fundamentally simple: a collection of pre-optimized [Tensor](https://pytorch.org/tutorials/beginner/examples_tensor/polynomial_tensor.html#:~:text=PyTorch%3A%20Tensors,-A%20third%20order&text=A%20PyTorch%20Tensor%20is%20basically,used%20for%20arbitrary%20numeric%20computation.) operations that the user calls from a Python program. On the other hand, PyTorch has historically provided high performance for deep learning workloads, as described in the PyTorch [paper](https://arxiv.org/abs/1912.01703). A key idea introduced in the PyTorch paper is the idea of **CPU/GPU overlap**: the CPU program dispatches work (kernels) for the GPU to execute, and so long as the CPU program runs faster than the GPU work, high performance is achieved.

*A large batch-size training run with high CPU/GPU overlap*

However, the claims made in the paper about CPU/GPU overlap have become less true over time as GPU speeds have increased at a breakneck pace. Let's examine floating point performance and memory bandwidth for GPU architectures over time:

- •[GP100 (as evaluated in the PyTorch paper)](https://www.nvidia.com/content/dam/en-zz/Solutions/design-visualization/productspage/quadro/quadro-desktop/quadro-pascal-gp100-data-sheet-us-nv-704562-r1.pdf)(2016) has 21[TFLOPS](https://en.wikipedia.org/wiki/FLOPS)half-precision and 730 GB/s memory bandwidth
- •[V100](https://images.nvidia.com/content/technologies/volta/pdf/tesla-volta-v100-datasheet-letter-fnl-web.pdf)(2017) has 112 TFLOPS half-precision (TensorCores) and 900 GB/s memory bandwidth
- •[A100](https://www.nvidia.com/content/dam/en-zz/Solutions/Data-Center/a100/pdf/nvidia-a100-datasheet-us-nvidia-1758950-r4-web.pdf)(2020) has 312 TFLOPS half-precision (TensorCores) and 1600–2000 GB/s memory bandwidth
- •[H100](https://resources.nvidia.com/en-us-tensor-core/nvidia-tensor-core-gpu-datasheet%5C)(2022) 989 TFLOPs half-precision (TensorCores) and 3350 GB/s memory bandwidth

NVIDIA GPU Performance Over Time

GPU half-precision floating point performance has increased **47x** and memory bandwidth has increased **4.6x** since the PyTorch paper was written. This speedup has profound implications on the ability of the CPU to stay ahead of the GPU and deliver maximum performance for deep learning workloads.

What exactly is the CPU doing when you run a PyTorch program? Several layers of overhead exist.

First, a PyTorch program has user-written logic that must be executed on the CPU. This logic includes metaprogramming, i.e. defining the structure of the network in Python code based on the hyperparameters. The simplest example of this is a loop over network layers. The best practice when writing PyTorch programs is to push this logic into Module construction so that this overhead is not incurred during model execution. Nonetheless, metaprogramming overheads still exist at runtime in most PyTorch programs.

Second, when calling PyTorch operations, several decisions must be made about which compute kernel to call on the device (GPU) based on properties like the device/dtype of the operands or whether [autograd](https://pytorch.org/tutorials/beginner/blitz/autograd_tutorial.html) recording is enabled. These decisions are made by a component called the [dispatcher](http://blog.ezyang.com/2020/09/lets-talk-about-the-pytorch-dispatcher/) running on the CPU. Although the dispatcher is written as highly-optimized C++, its execution still contributes to runtime overhead while executing a PyTorch program.

Third, GPU memory allocation contributes to runtime overhead. PyTorch uses a sophisticated [caching memory allocator](https://pytorch.org/docs/stable/notes/cuda.html#memory-management) to alleviate much of this overhead, but runtime performance may still be negatively affected by allocator activities on the CPU when executing programs with small operations.

Finally, CUDA itself has overheads in the driver and kernel launch paths, which can slow down the CPU execution of the program.

As GPUs get faster, CPU overheads become more of a problem when executing deep learning programs. Several techniques and tools have emerged to solve this problem.

*A batch-size 1 inference run on a HuggingFace Transformers model with very poor CPU/GPU overlap*

[HuggingFace Transformers](https://huggingface.co/docs/transformers/index) is a ubiquitous codebase for language models based on the [Transformer](https://arxiv.org/abs/1706.03762) architecture. However, in practice, Transformers is not highly optimized for inference, as the Python code is written in a way that maximizes flexibility but incurs significant CPU overhead. On the other end of the spectrum is [FasterTransformer](https://github.com/NVIDIA/FasterTransformer) (FT), written in highly optimized C++ to maximize performance. In practice, FT's optimized C++ code is quite hard to work with, slowing down the development of new features or adding new model architectures (e.g. [LLaMA](https://research.facebook.com/publications/llama-open-and-efficient-foundation-language-models/) models are [not officially supported](https://github.com/NVIDIA/FasterTransformer/issues/506)).

Another approach to performance optimization is automatic code transformation via compilation. [Apache TVM](https://tvm.apache.org/) is an early example of this approach, which provided an end-to-end stack that compiled a high-level representation of a neural network down to native machine code (e.g. on GPU). However, converting from a flexible PyTorch program to TVM's high-level representation is non-trivial, especially when a program contains control flow (loops, branches) implemented in Python or when a program involves distributed operations. Dynamic shapes (Tensor shapes that change at runtime) introduce additional complications.

A newer approach is `[torch.compile](https://pytorch.org/tutorials/intermediate/torch_compile_tutorial.html)`, as released with PyTorch 2.0. `torch.compile` improves upon the usability of existing compilation stacks with [TorchDynamo](https://pytorch.org/docs/stable/dynamo/index.html), a new front-end that automatically analyzes the Python bytecode of the program to extract sections of the program that can be compiled. However, this approach is not fool-proof, as arbitrary Python code can introduce *graph breaks*, which deoptimize the code and cause host-device synchronization. Additionally, `torch.compile`'s support for dynamic shapes and distributed operations is still in development, and without it, the applicability of `torch.compile` to LLM inference workloads is limited. Further, support for arbitrary memory layout management and mutation as used in the [PagedAttention](https://vllm.ai/) approach is generally not supported by contemporary deep learning compilers. See the Appendix for details about our experiments with `torch.compile` on LLM inference.

*Approaches to performance optimization represent various trade-offs between flexibility and speed*

Each of the approaches presented has different trade-offs; However, we'd like to highlight one option that we believe balances usability and performance: CUDA graphs.

In CUDA 10, NVIDIA introduced a feature called [CUDA graphs](https://developer.nvidia.com/blog/cuda-graphs/). CUDA graphs provide a way to record the GPU kernels invoked by a program into a graph data structure and later replay the kernels stored in that graph without incurring the original program's CPU overhead. This approach can help improve the performance of a GPU program where a specific sequence of operations is called many times. In other words, the graph representation can be said to be a **specialized** representation of the program down to kernel dispatch, i.e. the sequence of kernels and the arguments used at trace time (including pointers to Tensor memory) are “baked in” to the graph. Thus, care is needed when recording a CUDA graph to ensure that kernel arguments remain the same across runs.

On top of the CUDA graph API, PyTorch introduced [support](https://pytorch.org/blog/accelerating-pytorch-with-cuda-graphs/) for CUDA graphs from the Python API. The PyTorch CUDA graph API provides additional support for managing PyTorch allocator state to ensure the stability of Tensor allocations (and thus Tensor pointers) across runs.

CUDA graphs address all sources of CPU overhead highlighted above: user-written logic, PyTorch dispatcher logic, memory allocation overhead, and GPU driver/kernel overhead. In addition, the CUDA graphs API in PyTorch is relatively unintrusive so long as you can ensure that your program (or part of your program) conforms to a few [constraints](https://pytorch.org/docs/master/notes/cuda.html#constraints). This leads to easier to write and maintain code written in Python rather than in messy, optimized C++.

When running inference on a decoder LLM (such as the GPT family of models), there are two computation phases: a **prefill** phase that consumes the prompt and an **incremental generation** phase that generates output tokens one by one. Given a high enough batch size or input length, prefill operates on a sufficiently high number of tokens in parallel that GPU performance is the bottleneck and CPU overheads do not impact performance. On the other hand, incremental generation is always executed with sequence length 1 and it is often executed with a small batch size (even 1), e.g. for interactive use cases. Thus, incremental generation can be limited by the CPU speed and thus is a good candidate for CUDA graphs.

Recall that CUDA graphs have several constraints, including a requirement for fixed shapes. Incremental generation has a fixed sequence length and can be run with a fixed batch size. However, the attention computation operates on the tokens processed so far, meaning this dimension increases by one with each step. These processed sequences are stored in a [KV-cache](https://fireworks.ai/blog/multi-query-attention-is-all-you-need-db072e758055#bf4d). Here we present a code sample demonstrating incremental attention with KV-caching (reproduced from this blog [post](https://fireworks.ai/blog/multi-query-attention-is-all-you-need-db072e758055)):

12345678910111213141516171819202122

While both the regular attention mechanism and the [PagedAttention](https://vllm.ai/) scheme undergo shape changes over iterations, the latter provides a unique advantage when integrating with CUDA graphs. From the perspective of kernel arguments, PagedAttention provides a level of indirection for Tensor addresses. The base pointers to the K and V caches remain consistent across iterations and are safe to preserve as kernel arguments. The set of cache locations the kernel operates on is stored in a buffer with a fixed location in GPU memory, and thus, pointers to specific K and V locations can be computed entirely within the kernel. As a result, the entire computation within the incremental generation step can be soundly recorded into a CUDA graph. To keep track of page mapping, PagedAttention uses a varying-size Tensor called `block_tables`, which would naïvely present issues for CUDA graphs. However, this Tensor can be cheaply padded since its elements are relatively small indices. A subset of the `block_tables` tensor is then used on each invocation. This design not only aligns well with the flexibility offered by PyTorch's coding environment, but it also ensures a runtime that's either equivalent or superior to FasterTransformers, all while maintaining code simplicity.

Since CUDA graphs are shape-specialized, special care must be taken when handling a changing batch size at runtime. When using CUDA graphs for multiple batch sizes, it's best to trace a separate graph for each batch size and dispatch to the appropriate one during runtime.

PyTorch's CUDA graphs support using a [memory pool](https://pytorch.org/docs/stable/notes/cuda.html#graph-memory-management) to encapsulate allocations used during trace time and use them (and crucially, their pointers) during runtime. When compiling for multiple batch sizes, instead of giving each graph its own memory pool, a single shared memory pool can be used. By compiling graphs in decreasing order of batch size, memory from the shared pool is reused, as smaller allocations can be serviced by larger allocated buffers from a previous iteration. This way, multiple batch sizes are supported without using excessive GPU memory.

To demonstrate applying CUDA graphs in a real-world scenario, we modify the source code of the [LLaMA2](https://github.com/facebookresearch/llama) code as released by Meta research. A full diff can be found [here](https://github.com/fw-ai/llama-cuda-graph-example/commit/d8003f59af8893837ec9834c705cfd0035d3ad37). The changes required to enable CUDA graphs are rather minimal, consisting of some changes to how attention is implemented in the model and some infrastructural additions in the generation routines.

For modifications to attention, we modify the KV-cache handling to take the indices in which to write new values in a CUDA Tensor rather than a Python integer. We also modify attention to compute over the max sequence length but only compute softmax over the sequence positions <= the current time step. The changes are as follows:

*Modifications made to attention to support CUDA graphs*

To support this change, we refactor the generation of KV-cache indices and the attention mask. We generate the KV cache indices as a CUDA Tensor. We also augment mask generation to mask out sequence positions up to max_seq_len, in addition to traditional causal masking:

1234567891011

Note that these changes are correct but rather inefficient, as we compute attention over more sequence positions than we need to (up to `max_seq_len`). The PagedAttention approach addresses this issue, pushing KV-cache management into the kernels themselves while avoiding unnecessary computation. However, we show that even with this naïve approach, CUDA graphs present significant performance advantages over stock PyTorch code.

The infrastructure needed to compile the model for CUDA graphs in incremental generation is fairly simple and close to the examples in the PyTorch [documentation](https://pytorch.org/blog/accelerating-pytorch-with-cuda-graphs/#api-example). Some special care is taken to cache static inputs and outputs for further invocation, but otherwise, the code is [straightforward](https://github.com/fw-ai/llama-cuda-graph-example/blob/d8003f59af8893837ec9834c705cfd0035d3ad37/llama/generation.py#L111-L135):

1234567891011121314151617181920212223242526

We'd also like to shout out Bram Wasti's technique for easy CUDA graph application via a Python [decorator](https://twitter.com/bwasti/status/1694769457489481812). Although this is not applicable in our non-trivial LLM inference case, this approach may still be applicable in many other cases, e.g. image model inference or training with fixed sizes.

We test the above approach for compiling LLaMA-2 with the 7B model variant under `batch_size=1` inference conditions. We implement a benchmark [harness](https://github.com/fw-ai/llama-cuda-graph-example/commit/d8003f59af8893837ec9834c705cfd0035d3ad37#diff-4ead05c4053ddcb00e0038dcf342af9021f87146b8a29f67248719bc3c8d1566) to measure inference performance with CUDA graphs disabled and enabled, respectively. We test on a single NVIDIA A100-SXM4–80GB GPU. We find that without CUDA graphs, LLaMA-7B inference executes at **30 tokens/sec**, but with CUDA graphs enabled it executes at **69 tokens/sec** for a **2.3x speedup**.

We find that this speedup is entirely explained by CPU overhead reduction. The baseline run is dominated by CPU execution — GPU compute kernels are waiting for the CPU to dispatch them. This can be seen from a performance profile:

Overall Timeline of Execution for Non-CUDA Graph Model

Detail View of Timeline of Execution for Non-CUDA Graph Model

In this timeline, the GPU (bottom timeline) spends most of its time idle, waiting for the CPU (top timeline) to issue work. On the other hand, CUDA graph execution shows tight kernel dispatch behavior, running long sequences of kernels at once:

Overall Timeline of Execution for Non-CUDA Graph Model

Detail View of Timeline of Execution for Non-CUDA Graph Model

In this timeline, the GPU is consistently performing work, as the CPU overhead has been skipped.

The [Fireworks Inference Platform](https://fireworks.ai/) makes heavy use of CUDA graphs for all served models. We apply CUDA graphs and numerous other techniques (including [multi-query attention](https://fireworks.ai/blog/multi-query-attention-is-all-you-need-db072e758055) and others) to provide the best inference performance in the industry. We support a growing number of [models](https://fireworks.ai/models), including those in the LLaMA and StarCoder families, all with CUDA graphs and aggressive optimizations applied. Our Python-centric codebase with CUDA graphs allows us to get good performance while still retaining the flexibility and speed of development. This allows us to be on the cutting edge of AI development, e.g., enabling the latest models like Code Llama just [hours after their release](https://twitter.com/thefireworksai/status/1694799170396442873?s=20).

[Try out models on our platform](https://fireworks.ai/models) today for free to see what kind of performance we can deliver for Large Language Models in your product.

In conclusion, the substantial advancements in GPU speed in recent years have significantly altered the field of performance optimization for deep learning workloads. As a result, the host CPU has emerged as a bottleneck in processing. To address this, we evaluated several techniques, with CUDA graphs being a method that combines significant performance improvement with code flexibility and usability. After studying the impacts of CUDA graphs on Large Language Model workloads, we conclude that it presents a compelling solution for performance optimization in the face of rapid GPU improvement and we use it extensively in the [Fireworks Generative AI Platform](https://fireworks.ai/).

While applying CUDA graphs is easier than rewriting an entire model in C++, it still requires a lot of care. New compilation techniques in PyTorch 2.0 (`torch.compile`) aim to simplify and automate this process in the long run. When invoked with `[mode='reduce-overhead'](https://pytorch.org/get-started/pytorch-2.0/#user-experience)`, `torch.compile` tries to apply CUDA graphs to the extracted graphs of PyTorch operations. Today, this technique works well on smaller programs or [computer vision models](https://huggingface.co/docs/transformers/main/perf_torch_compile). We ran into issues applying it to the reference Llama code used in this post:

- •Graph capture failed with `torch.inference_mode`annotations, but worked when replaced by`torch.no_grad`(which, however, doesn't optimize away all bookkeeping)
- •The LLaMA reference code uses tensor parallelism via explicit distributed operations in [fairscale](https://github.com/facebookresearch/fairscale). They introduce graph breaks and eliminate any benefits from compilation. For evaluation, we removed distributed support, thus limiting applicability to a single GPU. Note that distributed collectives are[supported](https://pytorch.org/blog/accelerating-pytorch-with-cuda-graphs/#nccl-support-for-cuda-graphs)with CUDA graphs on their own.
- •Positional embeddings in the LLaMA codebase are computed using complex numbers. As of stable PyTorch 2.0.1, they can't be captured by compilation. After switching to the latest PyTorch 2.1 nightly, which includes [the fix](https://github.com/pytorch/pytorch/pull/96297), the capture succeeds but torchinductor still generates warnings about the quality of compiled kernels potentially being not optimal.
- •Beyond the LLaMA reference codebase, custom operations like PagedAttention require additional handling to be capturable by `torch.compile`.

After applying the above changes to the repo (see the [full diff](https://github.com/facebookresearch/llama/commit/ddf596e0ce57e6e6a612b3e89799e41f9dfa9dfe)), we could run `torch.compile` successfully in a non-distributed setup for the LLaMA-7B model. Inference speed matches manual CUDA Graph application exactly at 69 token/s for batch size 1 on A100. Based on the profiler, the entire generation step gets wrapped in a single CUDA graph invocation. Interestingly, a few fusions from torchinductor don't seem to change inference speed. Though `torch.compile` provides similar performance benefits for non-distributed cases, the warm-up time for compilation is about 3 minutes, compared to sub-second initialization time for explicit CUDA graphs. We tried making `torch.compile` skip fused kernel generation and only apply CUDA graphs using `backend='cudagraphs'`, but it errored out.

`torch.compile` may be a viable solution for LLM inference in the future, but for now, these optimizations require specific expertise that is not yet sufficiently automated.
