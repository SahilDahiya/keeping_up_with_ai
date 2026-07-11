---
title: Open-source LLM training is a mess. Here is how it all works.
topic: models
subtopic: fine-tuning
secondary_topics:
- infra-platform/gpu-clusters
summary: Explains the moving pieces of open-source LLM training, including data, trainers,
  infrastructure, and evaluation.
source: baseten
url: https://www.baseten.co/blog/open-source-llm-training-is-a-mess-here-is-how-it-all-works/
author: Paras Stefanopoulos
published: '2026-03-31'
fetched: '2026-07-11T04:05:47Z'
classifier: codex
taxonomy_rev: 1
words: 3523
content_sha256: d5a861413db242f1ad18027512451107b92f067e82760094e4a0eac9f71643fd
triage: keep
skip_reason: null
---

# Open-source LLM training is a mess. Here is how it all works.

![1](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1774921430-green-dark-1.jpg%3Fauto%3Dformat%26fit%3Dcrop%26h%3D630%26w%3D1200&w=3840&q=100)

There are too many libraries in the open-source LLM training ecosystem, and nobody tells you which ones actually matter, or how they relate.

A little about myself: I joined Parsed as the CTO/founding engineer, where we trained custom models for customers. We have since been acquired by Baseten, where we continue to expand. It has been my job to ensure our researchers can **reliably** train what they want, whenever they want.

All that to say, I’ve trudged through the pain of entering this field from the outside. Initially, I felt flooded with a billion different libraries. It felt like everyone just had this pre-requisite knowledge because they matured technically alongside the development of the repos. However, for people coming into the space, it’s very unclear what the responsibilities of the different repos are and how they fit together.

The point of this post is to provide the information I wish I had when starting. This post maps the components of the modern open-source LLM training: what each one does, what it depends on, and when you'd reach for one over another.

The stack has four layers:

- **Systems:**GPU runtime, communication, kernel authoring
- **Core runtime:**PyTorch, checkpoint formats
- **Training:**model definitions, performance primitives, scaling frameworks, adaptation
- **Inference:**serving runtimes, deployment optimization

![landscape](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1774922609-diagram.png%3Fauto%3Dformat%26w%3D1200&w=3840&q=75)

I assume we’re using NVIDIA GPUs. The ecosystem just hasn't been focused on alternatives; there are flickers of light (i.e., tinygrad), but they have not yet filtered through to the mainstream market.I will also preface that all of these libraries are constantly evolving. This overview is a snapshot in time, and between writing and posting, I may be out of date with the evolution of many packages. If I've gotten something wrong (likely), please let me know 💚

## Systems layer

These are the components below PyTorch. You rarely interact with them directly, but they are the lowest level, leading to machine code running on the hardware.

![systems](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1774922738-systems-layer.png%3Fauto%3Dformat%26w%3D1200&w=3840&q=75)

**Compute Unified Device Architecture (CUDA)**

- The GPU runtime + an extension of C++ which allows you to control all things GPU.
- All tensor computation on NVIDIA hardware goes through CUDA.
- PyTorch, cuBLAS, NCCL all sit on top of CUDA

**cuBLAS (CUDA Basic Linear Algebra Subprograms)**

- NVIDIA's dense linear algebra library
- A library of common operations implemented in CUDA, i.e. General Matrix Multiply (GEMM)
- Transformers are dominated by GEMM operations
- Alternatives exist like Nvidia’s CUTLASS, these are not mentioned in this post for brevity.

**NVIDIA Collective Communications Library (NCCL)**

- Library used to coordinate distributed GPU workloads
- Implements AllReduce, AllGather, ReduceScatter — the collectives that underly every distributed training strategy
- These are also just highly optimized kernels written in CUDA
- DeepSpeed, PyTorch FSDP2, Megatron, all use NCCL to coordinate the transfer of data between GPUs

**NVLink and InfiniBand**

- **NVLink:**high-bandwidth interconnect between GPUs within a node (900 GB/s bidirectional on Hopper)
- **InfiniBand:**high-bandwidth interconnect between nodes
- The ratio of compute speed to interconnect bandwidth determines whether a parallelism strategy is communication-bound

- Python Domain Specific Language (DSL) for writing GPU kernels. Your triton code ends up as PTX, which is GPU-level assembly code (CUDA compiles to this too)
- People use Triton to write kernels in an easier-way than straight CUDA or CUTLASS.
- flash-linear-attention is a collection of kernels for optimized linear attention, written in Triton.

## Core runtime

- Nearly every package in this post builds on, wraps, patches, or exports into PyTorch
- Tensors, autograd, optimizers, CUDA integration, distributed primitives
- PyTorch lets you describe the calculations required for your model, it can then execute these operations efficiently on a GPU (or supported accelerator)

Two PyTorch-native features worth calling out:

- **FSDP / FSDP2**
- **DTensor and DeviceMesh**

FSDP2 is awesome and makes multi-gpu distributed training easy. We speak more about FSDP2 and other parallelism options later.

- Just a file format, designed by HuggingFace. It has pretty much become the de facto standard for storing model weights.
- Used by Transformers, vLLM, SGLang, TensorRT-LLM, Megatron-Bridge

## Training stack

**WTF are Transformers, they're everywhere!**

Imagine if every research group maintained its own git repo to describe its unique model architectures. There would be a slew of custom implementations, config formats, and checkpoint layouts.

At a high level, Transformers gives the ecosystem one place to put and one way to represent:

- **Architecture specs**(the PyTorch modules for a model family)
- **Configuration**(given an architecture, how many layers are in the 4B version, what is the hidden dimension?)
- **Tokenizers / processors**

![stack](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1774923178-training-stack.png%3Fauto%3Dformat%26w%3D1200&w=3840&q=75)

When a new transformer drops, the research lab (or a third party) will commit the specification (architecture + tokenizers), written in PyTorch, in the transformers repo.

If you go to the *config.json* within a model's files, you will find the *model_type* key. This will map to the architecture implementations in transformers. For example, for [Qwen3.5-9B](https://huggingface.co/Qwen/Qwen3.5-9B/tree/main) we can find the spec and its variants [here](https://github.com/huggingface/transformers/tree/main/src/transformers/models/qwen3_5).

Other libraries can then either use these implementations directly, or try to wrap them/hook into them to patch in changes. For some, they can map from these reference implementations to optimized implementations (Megatron-Bridge converts to and from Megatron).

**Transformers** also has a simple training loop, which can be used to run SFT and links into DeepSpeed and Accelerate. This ecosystem (along with TRL, a more sophisticated RL training loop owned by HF) is referred to as the “HuggingFace Stack”.

**Performance primitives**

This is the layer people gesture at with phrases like *kernel magic* or *fused ops*. These libraries let us speed up our transformers by integrating below the model definition layer. They usually integrate in one of two ways:

- **Backend selection:**the framework exposes a standard interface for something like attention, then dispatches to an optimized implementation such as FlashAttention.
- **Module substitution:**the framework swaps in optimized drop-in replacements for standard layers like Linear, LayerNorm, or attention blocks.

So the model spec remains mostly the same, but key operations dispatch to more optimized kernels, which are provided by these libraries.

![kernels](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1774923448-performance-primitives.png%3Fauto%3Dformat%26w%3D1200&w=3840&q=75)

There isn’t a neat dependency chain here. It’s more like a library of interchangeable performance optimizations. The model framework defines the order of computations that need to be done, and where possible, it can hand off expensive parts to a specialised kernel from one of these libraries.Here are some I’ve interacted with the most:

- Fused attention kernel: computes attention in tiled blocks without materializing the full N×N attention matrix
- Memory cost drops from quadratic to linear in sequence length
- Throughput improves by reducing memory bandwidth pressure
- Dependency of almost everything in this post that runs a transformer

- Fused kernels for linear attention variants: RetNet, GLA, HGRN, RWKV-style architectures
- The FlashAttention equivalent for sub-quadratic attention mechanisms
- Only relevant if you're working with that family of models (more popular now especially as the recent Qwen3.5 models have linear attention)

- NVIDIA's library for FP8 mixed-precision training on Hopper GPUs
- Automatically manages FP8 scaling factors: determines which operations can safely run in FP8, handles dynamic range, falls back to higher precision where needed
- Hardware-generation-dependent: central on Hopper (H100/H200), largely irrelevant on Ampere (A100) where FP8 isn't available
- Megatron and TensorRT-LLM depend on it heavily

## Scaling frameworks

These scaling frameworks all solve the same problem. Fitting big models on hardware is hard. We need to cut them up in different ways (sharding) to spread the load across many GPUs/TPUs. The techniques we use to cut these models up are referred to as “Parallelisms”.

I will cover some of the popular repos which help implement these parallelisms. Here is a high level overview of the related repos I’ll be covering.

![pytorch](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1774923530-scaling-frameworks.png%3Fauto%3Dformat%26w%3D1200&w=3840&q=75)

I like to think of Megatron as a library of highly optimized LLM building blocks. They'll have an expert router module, attention module, gated delta net module, dense FFN module, etc. All of these can support a mix of the different parallelism techniques and have been written with that in mind.

Megatron-Bridge takes a Transformers model spec, and reconstructs it using components from this Megatron library. I’ve found the final Megatron-ified model really reliable and to work great at scale!

DeepSpeed takes a different approach: it generally keeps the Transformers model structure and shards it via runtime wrapping/patching.

The Megatron code paths are the most stress-tested and, in my experience, more reliable than DeepSpeed and PyTorch FSDP2. Part of that is Megatron’s large engineering investment, and we’re lucky to work closely with that team at Baseten. Many labs also use Megatron for large-scale research training.

So in a nutshell, my mental model for Megatron:

- Library of LLM building blocks
- Stress tested implementations of many parallelisms, allowing us to be explicit about the trade-off between compute and IO
- Transformer-Engine is completely separate to - **Transformers**. Megatron lets us optionally use Transformer-Engine to add kernels for efficient FP8 training.

To go from training on one GPU to training on 16 GPUs across 2 machines, you'd normally have to manually do a bunch of setup. None if it is conceptually hard, however, it is 50-100 lines of setup-specific code you don’t want to worry about.

Accelerate just abstracts that away. You call *accelerator.prepare(model, optimizer, dataloader)* and it handles wrapping, placement, and sharding based on a config file.

- Does - **not**implement any distributed communication primitives — it calls- **PyTorch's**distributed APIs, which call NCCL
- It's a configuration and orchestration layer: decides - *what*to set up, delegates to PyTorch/NCCL to do it

I think of this as the “OG” implementation of LLM sharding. DeepSpeed popularized ZeRO-style sharding, and PyTorch later brought similar ideas into native FSDP/FSDP2. DeepSpeed offers a few different “levels” of sharding, which can be thought of as:

- ZeRO-1: shard optimizer states across GPUs
- ZeRO-2: shard optimizer states + gradients
- ZeRO-3: shard optimizer states + gradients + parameters

**How they relate:**

Accelerate and DeepSpeed are independent. DeepSpeed runs standalone via *deepspeed.initialize()*. But Accelerate has a DeepSpeed integration: you can use Accelerate as the launcher and config layer for DeepSpeed, so you call *accelerator.prepare()* and it sets up the DeepSpeed engine under the hood.

- Reference implementation for large-scale training using only native PyTorch APIs
- Built on PyTorch primitives: FSDP2, DTensor, DeviceMesh, PyTorch Tensor Parallel, torch.compile
- Implements 3D parallelism (data + tensor + pipeline) with no external distributed runtime

I found this a bit confusing; Megatron and DeepSpeed are both also built on top of PyTorch. So what makes TorchTitan different?

PyTorch now has native sharded/model-parallel primitives that overlap with capabilities people historically reached for DeepSpeed to get. TorchTitan is a reference as to how to build a training library on top of these primitives.

TorchTitan is very much in its building phase. Due to this, I find even simple training runs can be broken in hard-to-debug ways. For example, my experience exploding gradients after 1k steps with MoEs, or this fun case where we would OOM during the backward pass because of a bug in handling FSDP + activation checkpointing:

![oom](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1774923653-heltz8zbmaeerw.jpeg%3Fauto%3Dformat%26w%3D1200&w=3840&q=75)

I find Megatron more fleshed out and reliable. Although, I hope PyTorch's primitives take over and democratize reliable-distributed training.

**DeepSpeed and PyTorch FSDP2 vs Megatron**

DeepSpeed and PyTorch FSDP2 implement a similar idea of sharing the model weights across all GPUs. Each GPU runs a data sample in parallel and they share weights to each other on an as needed basis. Megatron's parallelisms are more opinionated and give more levers to the user about how to optimize the compute/memory IO trade-off.

As I alluded to before, DeepSpeed was the OG ZeRO-style LLM sharding implementation. Then PyTorch introduced FSDP, and later FSDP2 as its newer iteration. FSDP1 had some rough edges; FSDP2 is much better and still improving.

**Recommended Resources**

There are a million blogs explaining implementations but my favorite for TP/FSDP is[How To Scale Your Model > Training](https://jax-ml.github.io/scaling-book/training/). The recent NVIDIA paper[Scalable Training of Mixture-of-Experts Models with Megatron Core](https://arxiv.org/abs/2603.07685)is an amazing overview of the more complex Megatron levers. It's very verbose, so strap in, but it's a great reference.

**Training loops and orchestrators**

A point that isn't obvious from the dependency graph: many libraries in this stack ship their own “training loop” implementation. When I refer to training loop, I mean the code that handles:

- Data loading
- Calling forward , backward, optimizer.step(), etc. in the right order
- Saving checkpoints + Observability

Basically, the orchestration layer, that wires together all of these upstream repos we have discussed and runs your training job.This is a quick lay of the land, and by no means exhaustive. Like other parts of this blog, I am missing many (most notably, TRL, I just haven't used it instead of VeRL).

![loops](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1774924416-hedp15vacaas2fj.jpeg%3Fauto%3Dformat%26w%3D1200&w=3840&q=75)

- Often used by training loops, but doesn’t ship a training loop itself, however, is worth a mention due to its popularity
- Injects trainable adapters (LoRA, QLoRA, IA3) while freezing base model weights
- Only adapter parameters train, dramatically reducing memory and compute
- Can be used - *within*whatever training loop you're running, if they support it

- HuggingFace's built-in training loop, lives inside the Transformers library
- Handles epochs, batching, evaluation, logging, checkpointing, and callbacks
- Uses Accelerate and DeepSpeed under the hood for distributed models
- For many fine-tuning tasks, this is the only training loop you need, but it's opinionated and tied to the HF ecosystem
- Within the HuggingFace stack, the default is usually this or - [TRL](https://github.com/huggingface/trl)(more fully featured and offers RL orchestration)

- Training orchestration written by ModelScope/Alibaba
- Key difference from Transformers Trainer: lets you swap training backends (HF stack vs Megatron stack)
- Coordinates SFT, RLHF, evaluation, - [inference](https://www.baseten.co/blog/ai-inference-explained/), and model export
- Massive dependency list incl. Transformers, Accelerate, DeepSpeed, Megatron, PEFT, vLLM, SGLang
- Similar to VeRL but the way I conceptually think about the difference is that more engineering time has been spent making sure ms-swift is solid for SFT specifically

**RL training: VeRL, Prime-RL, and others**

I will preface, there are many libraries which are different perspectives on RL. I have only covered a few here but some notable mentions are: [SkyRL](https://github.com/NovaSky-AI/SkyRL), [PipelineRL](https://github.com/ServiceNow/PipelineRL), [Slime](https://github.com/THUDM/slime), [TRL](https://github.com/huggingface/trl), [Miles](https://github.com/radixark/miles).

RL introduces a fundamentally different training topology. In standard SFT, you have one model and one training loop. In RL training (PPO, GRPO, etc.), you typically need:

- A - **policy model**being trained (forward + backward), with weights periodically synced to an inference engine for rollout generation
- A - **reward model**scoring each rollout
- A - **critic model**estimating expected future reward per token (PPO only, GRPO drops this)

RL-scaling is a new frontier and we are seeing compute dedicated to inference grow relative to compute spent on training (actual forward/backwards steps). As a result, most of training is bottlenecked by inference, especially as task time horizon grows.

**Time spent on inference >> training**

As we are producing so many tokens, we defer this to an actual inference engine like vLLM.

The typical GRPO async-RL loop looks like:

- Collect a batch of samples
- Pass them through the inference engine & generate a respective batch of rollouts
- Score these rollouts
- Pass the scored rollouts to the training server
- Forward & back prop the transformer, then step the optimizer to update the weights
- Transfer the updated weights back to the inference server
- Repeat

This is why RL frameworks depend on both training backends (DeepSpeed, Megatron) and inference engines (vLLM, SGLang).

[ VeRL ](https://github.com/verl-project/verl)(from ByteDance)

- RL post-training framework, open-source implementation of the - [HybridFlow paper](https://github.com/verl-project/verl)
- Supports FSDP2, and Megatron training backends; vLLM, SGLang, TensorRT-LLM, and HF Transformers for rollout generation I've only ever tested the vLLM code paths
- Integrates Megatron-Bridge for checkpoint conversion, supports LoRA/PEFT
- Much like ms-swift, has a massive support matrix for different backends and techniques.

[ Prime-RL ](https://github.com/PrimeIntellect-ai/prime-rl)(from PrimeIntellect)

- RL training framework focused on scalable, distributed RLHF/GRPO workflows
- Similar topology: training loop + inference engine + weight syncing
- Uses PyTorch FSDP2 for training, vLLM for generation
- Where VeRL takes a model spec from Transformers and applies appropriate wrapping to get it training, Prime-RL implements the models themselves. TorchTitan style, which gives more flexibility but also higher risk of implementation mistakes and bugs.
- Can see their paper - [here](https://openreview.net/pdf?id=yk3ICpEbv8)!

The common pattern across all RL frameworks: they sit on top of the same training and inference components described in this post, but add a coordination layer that manages the interaction between training and generation.

When to generate, when to train, how to sync weights, scheduling GPU resources all while maintaining correctness is the hard part that these frameworks solve.

## Inference stacks

Serving LLMs is a distinct engineering problem from open-source LLM training. Philip Kiely from Baseten released [Inference Engineering](https://www.baseten.com/inference-engineering), which is a great reference for all things inference. The bottleneck shifts from compute to memory bandwidth (autoregressive decoding is memory-bound), and the key concerns become latency, throughput, batching efficiency, and KV cache management.

![inference stacks](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1774924540-hedsgk-bcaajccb.jpeg%3Fauto%3Dformat%26w%3D1200&w=3840&q=75)

- High-throughput serving runtime, most widely deployed open-source LLM serving engine
- Core contribution: PagedAttention, manages KV cache memory in non-contiguous blocks (like virtual memory paging), reducing memory waste from fragmentation
- Also implements continuous batching, speculative decoding, prefix caching, multi-LoRA serving
- PyTorch-based, supports a wide range of model architectures out of the box

- Serving engine with strengths in structured generation and KV cache reuse
- Core contribution: RadixAttention, organizes KV cache as a radix tree indexed by token prefixes, enabling automatic cache sharing across requests with common prefixes
- Frontend DSL for composing LLM calls with control flow, branching, and parallelism
- Well-suited for agent-style workloads with multiple chained model calls per request

- Originally a compiled inference engine: takes a model, applies graph-level optimizations (layer fusion, kernel selection, FP8 calibration, memory planning), produces a static execution plan for specific GPU hardware
- Has since migrated to a PyTorch-first frontend, but performance still comes from NVIDIA's kernel stack: fused ops, FP8 via Transformer Engine, custom CUDA kernels
- vLLM and SGLang are fully dynamic PyTorch runtimes by comparison
- Dynamo is a disaggregated serving framework: separates pre fill and decode across GPU pools, routes requests to workers most likely to have KV cache already computed
- The combination of these two are a pain to get running, but widely considered as the highest performance - [inference stack](https://www.baseten.co/resources/guide/the-baseten-inference-stack/)publicly available. See SemiAnalysis’ inference benchmarks

- NVIDIA's toolkit for preparing models for deployment
- Quantization (INT8, INT4, FP8), sparsity (structured/unstructured pruning), distillation, calibration
- Output is an optimized model, which can then be run with TensorRT-LLM, vLLM, or SGLang

**When to use the different inference runtimes (imo)**

This is entirely my opinion and is skewed by my experience.

vLLM and SGLang are pretty similar. I have felt that vLLM has had fewer bugs and more day-zero support for getting models up and running. vLLM has become my standard for use during RL. Just the most out-of-the-box and reliable.

TensorRT-LLM is the super-optimized, best-performing inference stack. If deploying for a production use case at scale (not for RL loops), this is your best bet.

## A brief map of open-source LLM training

![training](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1774924587-heebesubgaakl9u.jpeg%3Fauto%3Dformat%26w%3D1200&w=3840&q=75) By no means exhaustive. These categories have many other repos which could be here. I just tried to cover the most important and ones I interact with on a daily basis.

By no means exhaustive. These categories have many other repos which could be here. I just tried to cover the most important and ones I interact with on a daily basis.## Training stacks internally at Baseten

At Baseten, the Post Training engineering team has been developing our in-house packages to reduce dependency on many of these open-source LLM training offerings. However, it is common we reach for things when the time calls for it.

There has been some noise on X recently acknowledging how broken things are and we have certainly felt it. Workshop Labs [experienced](https://x.com/WorkshopLabs/status/2031151606691950875) this first hand.

There is a movement toward plain PyTorch implementations of models and home-rolled/TorchTitan inspired parallelism implementations. We have veered away from this until these packages stabilize. We are instead building on top of Megatron.

We are ensuring that our codebases take the necessary precautions so we can be flexible with our training backend and swap out Megatron if needed.

Megatron is currently the most stable and reliable, but is at risk of not being nimble enough/giving the developer enough control of the model internals.

We have a team of applied researchers who need to train models across a variety of techniques. They want to be able to train:

- Any model
- Any sequence length
- SFT, RL and everything in between (QAT, distillation, its variants + new techniques as they come out)
- Arbitrary PEFT techniques
- At scale when compute permits

This support matrix is huge, and so having a bulletproof open-source LLM training stack is paramount. When a researcher kicks off a training job, they can't be left wondering if the gradient update is bugged because of certain interactions in their config.

We're solving this, along with a slew of other interesting problems related to distributed training. If this sounds interesting to you please reach out, we're [hiring](https://www.baseten.co/resources/careers/) 💚
