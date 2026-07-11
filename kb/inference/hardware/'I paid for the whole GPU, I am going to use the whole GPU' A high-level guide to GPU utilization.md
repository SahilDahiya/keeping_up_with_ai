---
title: '''I paid for the whole GPU, I am going to use the whole GPU'': A high-level
  guide to GPU utilization'
topic: inference
subtopic: hardware
secondary_topics:
- infra-platform/cost
summary: Guide to GPU utilization for AI workloads, covering bottlenecks, throughput,
  batching, and cost-aware usage.
source: modal
url: https://modal.com/blog/gpu-utilization-guide
author: null
published: '2025-02-24'
fetched: '2026-07-11T04:29:13Z'
classifier: codex
taxonomy_rev: 1
words: 3012
content_sha256: 2b86eeea1e67d2037d9caf327d28df8ff19af2a812d9548c936c09ecb8529993
triage: keep
skip_reason: null
---

# 'I paid for the whole GPU, I am going to use the whole GPU': A high-level guide to GPU utilization

[Back](https://modal.com/blog)

# 'I paid for the whole GPU, I am going to use the whole GPU': A high-level guide to GPU utilization

[Charles Frye](https://twitter.com/charles_irl)

![A t-shirt that says 'I paid for the whole speedometer, I am going to use the whole speedometer'](https://modal-cdn.com/blog-gpu-utilization-whole-speedometer.webp)



Graphics Processing Units, or GPUs, are the hottest mathematical co-processor since the [FM synthesis chips that shaped the sounds of the late 1900s](https://old.reddit.com/r/chiptunes/comments/qc0zl5/why_did_fm_synthesis_take_so_long_to_take_off/hhemu2v/).

Like all co-processors, they are chosen when the performance of more flexible commodity hardware, like an x86 Central Processing Unit (CPU), is insufficient. GPUs are in particular [designed for problems](https://modal.com/gpu-glossary/device-hardware/streaming-multiprocessor) where CPUs cannot achieve the desired throughput of mathematical operations (in particular, matrix multiplications).

But GPUs are not cheap: high performance can command a high price.

Combined together, the high price, performance sensitivity, and throughput-orientation of GPU applications mean that a large number of engineers and technical leaders find themselves concerned with *GPU utilization* of some form or another — “we’re paying a lot, so we’d better be using what we’re paying for”.

At Modal, we have our own GPU utilization challenges to solve and we help our users solve theirs. We’ve noticed that the term “GPU utilization” gets used to mean very different things by people solving problems at different parts of the stack. So we put together this article to share our framework for thinking about GPU utilization across the stack and the tips and tricks we’ve learned along the way.

In particular, we’ll talk about three very different things that all get called “GPU utilization”:

- [GPU Allocation Utilization](https://modal.com#what-is-gpu-allocation-utilization), the fraction of your GPUs that are running application code,
- [GPU Kernel Utilization](https://modal.com#what-is-gpu-kernel-utilization), the fraction of time your application is running code on GPUs, and
- [Model FLOP/s Utilization](https://modal.com#what-is-model-flops-utilization-mfu), the fraction of the GPUs’ theoretical arithmetic bandwidth your application is using to run models.

We’ll specifically focus on neural network inference workloads — neural networks because they are workload generating the most demand right now and inference because, unlike training, inference is a revenue center not a cost center. We’re betting on the revenue center.

## What is utilization?

### Utilization = Output achieved ÷ Capacity paid for

*Utilization* relates the available capacity of a system to that system’s output.

In throughput-oriented systems like GPU applications, the capacity paid for is often a *bandwidth* (e.g. the arithmetic bandwidth) and the output achieved is then a *throughput* (e.g. floating point operations per second, FLOP/s).

Because it is a ratio, utilization is unitless. That means **there are actually many GPU-related quantities you might call “GPU utilization”**, leaving off the implicit units of the capacity and output. These different quantities range across orders of magnitude of time and across different organizational capacities (e.g. procurement, DevOps, and low-level performance engineering).

## What is GPU Allocation Utilization?

### GPU Allocation Utilization = GPU-seconds running application code ÷ GPU-seconds paid for

First, consider the number of GPUs that you have allocated — whether that is fixed GPU capacity on-premise in your basement (or data center) or it is rented capacity in a cloud data center (or many people’s basements) — across a period of time.

We use the term *GPU Allocation Utilization* for the fraction of those GPU-seconds during which you were running application code. This is the highest-level notion of “GPU utilization”.

There are two key limits on GPU Allocation Utilization: economic and developer-operational.

The economic limits on GPU Allocation Utilization rise from combined technical and market limitations. Purchasing, commissioning, decomissioning, and selling GPUs cannot be done as quickly as the output demanded by the application changes (on the scale of seconds or minutes).

Of course, as for other hardware we are blessed with highly-virtualized data center platforms (“clouds”) where we can virtually allocate and de-allocate GPU capacity. Even there, however, existing pricing models and demand that exceeds supply leave providers dictating terms, like multi-month or multi-year commitments, which limit achievable utilization for a given quality-of-service.

### With a fixed, over-provisioned GPU allocation, utilization is low

Modal helps organizations solve this problem. We aggregate GPU demand across consumers and GPU supply across providers to improve GPU allocation efficiency.

But GPU Allocation Utilization isn’t just about the GPU-seconds paid for, it’s about the GPU-seconds spent running application code.

That’s where the DevOps limits on GPU Allocation Utilization come in. Even in a fully liquid GPU market, there is latency between the time at which a GPU is purchased or rented and the time at which the GPU is running useful work — time to configure operating systems, perform health checks, copy over application code, etc. Absent the ability to precisely predict future demand at timescales greater than that latency, this leads to reduced GPU Allocation Utilization, reduced quality-of-service, or both!

### If allocation is slow, utilization and QoS suffer

To achieve high GPU Allocation Utilization and meet quality-of-service goals, allocation and spin-up to application code needs to be fast enough to respond to increases in demand.

### With fast, automatic allocation, utilization and QoS can both be high

This is one of the core problems solved by Modal. We manage a large multi-cloud GPU fleet, benefitting from economies of scale to unlock better engineering solutions and concentration of measure to improve predictability of demand. We [built a custom container stack (in Rust btw)](https://www.youtube.com/watch?v=3jJ1GhGkLY0) to reduce the latency from non-application code and system configuration. And users’ workloads spin up faster because the serverless runtime for that container execution system frames user workloads in terms of application code, not virtual machine maintenance. That allows us to skip the repetitive, undifferentiated work required to create virtual machines. That unlocks novel engineering optimizations for us, like [memory snapshotting and restoration](https://modal.com/blog/mem-snapshots), and it just-so-happens to make application engineering easier for our users.

## What level of GPU Allocation Utilization can I expect to achieve?

The existing numbers are sobering. According to the [State of AI Infrastructure at Scale 2024 report](https://ai-infrastructure.org/the-state-of-ai-infrastructure-at-scale-2024/), the majority of organizations achieve less than 70% GPU Allocation Utilization *when running at peak demand* — to say nothing of aggregate utilization. This is true even of sophisticated players, like the former [Banana serverless GPU platform](https://www.banana.dev/blog/sunset), which operated at an aggregate utilization of around 20%.

With Modal, users can achieve GPU Allocation Utilization in excess of 90% — in aggregate, not just at peak.

If that interests you, check out our [docs](https://modal.com/docs) and our [pricing page](https://modal.com/pricing).

If it doesn’t, read on for more about the software engineering required to get the most out of your GPUs — on Modal or elsewhere.

## What is GPU Kernel Utilization?

### GPU Kernel Utilization = GPU-seconds running kernels ÷ GPU-seconds paid for

Just because an allocated GPU is running application code doesn’t mean it is running code *on the GPU.* The term of art for “code that runs on the GPU” in the popular [CUDA programming model](https://modal.com/gpu-glossary/device-software/cuda-programming-model) for GPUs is “kernel”, and so we call the fraction of time we spend running code on the GPU the *GPU Kernel Utilization*.

This utilization metric is reported by, among others, the beloved [ nvidia-smi command line tool](https://modal.com/gpu-glossary/host-software/nvidia-smi) wrapping

[NVIDIA’s Management Library](https://modal.com/gpu-glossary/host-software/nvml)for their GPU hardware, and so it is commonly checked and cited. We

[expose it to our users](https://modal.com/docs/guide/gpu-metrics)under the name that library uses, “GPU utilization”. Note that this name can be slightly misleading, since this metric does not care whether the code we’re running on the GPU is exercising the hardware’s actual capacity.

An application that is achieving low GPU Allocation Utilization is necessarily going to achieve low GPU Kernel Utilization, so long as you consider all GPU-seconds being paid for: a unit not running application code can’t run kernels.

Why else might you achieve low GPU Kernel Utilization? In particular, what patterns will show up as low kernel utilization per GPU?

First, there might be lots of work to do that supports your application but doesn’t use the GPU, like moving input or output data via network or disk, downloading the many gigabytes of weights of a foundation model, or writing logs.

These tasks can be sped up by usual means — judicious application of lazy and eager loading, parallelization, increased bandwidth for non-GPU components like networks, and deleting more code [YAGN](https://martinfowler.com/bliki/Yagni.html).

Second, the CPU might not be providing work to the GPU quickly enough. A typical GPU-accelerated program is, like a high-performance network application, a dance of concurrency between the CPU executing logic about what work must be done and specialized, but dumb, hardware that can actually do the work. For example, when multiplying two matrices, the popular PyTorch library needs to determine the shapes and types of those two matrices and then lookup the appropriate kernel — somewhat akin to a JIT database query optimizer selecting a physical operator mid-execution. If you are unable to complete this work before the GPU finishes its previous task, the GPU will idle. We’ll call this class of issue “host overhead”.

Often, resolving host overhead is a matter of re-writing the host logic — preventing slow host work (like logging in Python) from blocking the host work that drives the GPU. But at the scale of milliseconds per task step, Python starts to become incapable of keeping up, and at the scale of microseconds per task step, the latency required to schedule kernels onto the GPU via [the CUDA C++ APIs and driver](https://modal.com/gpu-glossary/host-software/cuda-runtime-api) begins to bottleneck.

In both cases, there are two basic optimizations. First, multiple kernels can be launched at once [using CUDA Graphs](https://pytorch.org/blog/accelerating-pytorch-with-cuda-graphs/), which essentially convert a sequence of kernel launches into a DAG that only needs to be launched once. Second, the application can aggregate more work for the GPU to complete for a given unit of host work — for example by [batching](https://modal.com/docs/guide/dynamic-batching) requests together — to improve utilization with a possible penalty to latency.

Code regions with low GPU Kernel Utilization can be identified from application traces, like those produced by the [PyTorch Profiler](https://modal.com/docs/examples/torch_profiling). Specifically, any period of time where all CUDA streams are empty is a period of zero GPU Kernel Utilization, and so applications with low GPU Kernel Utilization have largely empty CUDA streams in their traces, like the one below. These periods of quiescence need to be correlated to activity on the host to determine which parts of the application code are leading to the bottleneck. GPU application profilers and trace viewers generally support this, e.g. by showing kernel launch dependencies, like the arrow in the trace below.

![A trace of a PyTorch application with low GPU Kernel Utilization](https://modal-public-assets.s3.amazonaws.com/tmpx_2c9bl5_c5aa7ab0.webp)



[our documentation](https://modal.com/docs/examples/torch_profiling).

## What level of GPU Kernel Utilization can I hope to achieve?

GPU Kernel Utilization is the closest metric in this article to the better-known CPU utilization. CPU utilization tracks the fraction of CPU cycles during which instructions were being executed on behalf of your program (as opposed to the CPU idling or running other programs).

However, for CPU utilization, hitting 90%+ is often bad, even a trigger for alerts. But we want to and can achieve that level of GPU Kernel Utilization!

Fundamentally, this is downstream of the greater predictability of many GPU applications. Running a transactional database replica at 90% CPU utilization baseline risks degraded quality-of-service if query patterns or quantity change. Typical GPU applications have much less variability — for a database analogue, imagine repeatedly running only one basic sequential scan aggregation query, but with slightly different parameters each time — and so have more controllable quality-of-service.

## What is Model FLOP/s Utilization (MFU)?

### Model FLOP/s Utilization = Model FLOP/s throughput achieved ÷ FLOP/s bandwidth paid for

At some galaxy-brained, CEO-math level, expenditures on GPUs are really expenditures on floating point operation bandwidth, and so the deepest and most fundamental utilization metric to measure is the ratio of that bandwidth to the throughput achieved.

This metric is known as *MFU*, which either means “Maximum” or “Model” FLOP/s Utilization, depending on who you ask. We go with “Model”, since it’s more common.

Instances that aren’t running application code or that aren’t running GPU kernels cannot achieve a high MFU, so low GPU Allocation Utilization or low GPU Kernel Utilization imply low Model FLOP/s Utilization.

However, high utilization at these more abstract levels does not imply high MFU.

First, as an implementation detail, communication between GPUs is frequently implemented via GPU kernels. This communication, like most communication in distributed systems, is subject to faults (hardware fault, programmer fault, [shark attack fault](https://slate.com/technology/2014/08/shark-attacks-threaten-google-s-undersea-internet-cables-video.html)), which frequently manifest as deadlock. From the perspective of GPU Kernel Utilization, a system that is deadlocked in the middle of running a communication kernel is fully utilized (!), but it is completing no useful work. We like to catch this particular issue by monitoring [GPU power draw and heat](https://modal.com/docs/guide/gpu-metrics). More generally, optimizing communication is critical for achieving high MFU, especially for workloads that spread a single task across multiple nodes.

Second, floating point computation is just one of the things a GPU must do to complete a task. The most important other task is moving data. Computation can only occur on data stored inside of the [register file](https://modal.com/gpu-glossary/device-hardware/register-file) of the GPU’s [streaming multiprocessors](https://modal.com/gpu-glossary/device-hardware/streaming-multiprocessor), which each store less than a megabyte, while foundation models are measured in gigabytes. The data to which a computation applies must generally be moved from a slower, larger area of the [memory hierarchy](https://modal.com/gpu-glossary/device-software/memory-hierarchy). The [bandwidth of this memory](https://modal.com/gpu-glossary/device-hardware/gpu-ram) is generally many times lower than the device’s FLOP/s bandwidth, especially in recent generations. The ratio of an algorithm’s FLOP/s throughput to its byte/s throughput is called the arithmetic intensity.

Bottlenecking on memory is a particular challenge in latency-sensitive foundation model inference workloads, where the arithmetic intensity is low (perhaps a few FLOPs per byte). Besides algorithmic rewrites to increase arithmetic intensity, like [the online softmax in Flash Attention](https://arxiv.org/abs/2205.14135), the primary generic strategy is [batching](https://modal.com/docs/guide/dynamic-batching) more work together, which increases FLOPs executed more than memory bytes moved for most neural network inference workloads, but generally adds per-task latency.

Finally, GPU kernels must be carefully written to achieve high MFU. [This public worklog by Si Boehm](https://siboehm.com/articles/22/CUDA-MMM) gives a flavor for the effort required to reach state-of-the-art for a single kernel. Even that worklog stops short of truly maximizing MFU, since it tackles a problem that can’t make use of the fastest elements of contemporary GPUs, the [Tensor Cores](https://modal.com/gpu-glossary/device-hardware/tensor-core), and writing kernels that can saturate Tensor Cores is even more challenging — see [this worklog from Pranjal Shankhdhar](https://cudaforfun.substack.com/p/outperforming-cublas-on-h100-a-worklog). For this reason, most teams use high-quality open source kernels through libraries like CuBLAS or frameworks like PyTorch and vLLM.

The achieved FLOP/s and memory throughput of a GPU application can be monitored using the [NVIDIA Data Center GPU Management tool](https://docs.nvidia.com/datacenter/dcgm/latest/user-guide/feature-overview.html#profiling-metrics), `dcgm`. The metrics prefixed with `DCGM_FI_PROF` are generally relevant. In particular, the `DCGM_FI_PROF_DRAM_ACTIVE` metric measures the utilization of the DRAM-to-SRAM memory bandwidth. The `DCGM_FI_PROF_PIPE_TENSOR_ACTIVE` metric measures the utilization of the Tensor Cores that provide the maximum FLOP/s bandwidth. This isn’t identical to MFU for subtle reasons covered well in Stas Bekman’s guide [here](https://github.com/stas00/ml-engineering/blob/master/training/performance/README.md#mfu-vs-hfu).

## What level of Model FLOP/s Utilization can I hope to achieve?

First, let’s note that measuring Model FLOP/s Utilization is tricky. The theoretical bandwidth can be read from manufacturer datasheets — but watch for asterisks like “with sparsity”. The achieved model throughput, on the other hand, can be hard to measure, in particular since some FLOPs might be spent on other computations, like activation recomputation in training. For that reason, it is often done based on pen-and-paper analysis of the algorithm and with approximate, “napkin” math.

The state-of-the-art for MFU in training is achieved by the foundation model teams at leading organizations like OpenAI, Google, and Meta. Of these, Meta is the most open and reports an MFU of 38 - 41% when training [the LLaMA 3 405B model](https://arxiv.org/abs/2407.21783). The more recent DeepSeek-v3 training run by DeepSeek achieved around 20-30% MFU (there’s no official number) [using GPUs with tighter communication bottlenecks](https://semianalysis.com/2025/01/31/deepseek-debates/).

Much of the shortfall is due to the need for inter-node communication in large training jobs, which creates bandwidth constraints that aren’t present in inference applications. For inference workloads, MFU might reach higher, closer to the [70% - 80% MFU achieved by raw matrix multiplications](https://github.com/stas00/ml-engineering/tree/master/compute/accelerator#maximum-achievable-flops), but we aren’t aware of any published results from large-scale deployments. Let us know if we missed them!

For context, it’s also helpful to consider the equivalent of MFU for a job running on a CPU. For concreteness, consider the [One Billion Row Challenge](https://github.com/gunnarmorling/1brc), which led teams around the world to competitively optimize a large-scale aggregation problem on CPUs. This problem requires three floating point operations per row on one billion rows, and so has a total FLOP count of 3 billion. The leading results finished in about one second, and so achieved a FLOP/s throughput of about 3 billion. If we assume that the hardware used for the challenge, eight cores out of a [32 core AMD EPYC 7502P](https://www.hetzner.com/dedicated-rootserver/ax161) machine which can run at 3.35 GHz, is capable of issuing one FLOP per cycle, then the FLOP/s bandwidth is ~26 billion, for an MFU of ~10%. However, that CPU has [AVX2 SIMD vector instructions](https://en.wikipedia.org/wiki/Advanced_Vector_Extensions) with a lane width of 256 and so, assuming it can issue 16 FLOPs/cycle per core, the FLOP/s bandwidth is actually ~420 billion, leading to an MFU of under 1%.

## How can I improve my GPU utilization?

If you’re not using [Modal](https://modal.com/), that’s a great place to start! Especially for GPU Allocation Utilization.

Besides that, we recommend that if you want to improve your GPU utilization, you dive deeper into GPU-based computing.

We wrote a [GPU Glossary](https://modal.com/gpu-glossary) to collect together our definitions of the most important terms in one place, complete with links to some of our favorite resources for learning more. Try starting there!

Among those resources, a few stand out, like [this talk by Horace He](https://www.youtube.com/watch?v=139UPjoq7Kw&t=1236s), of the PyTorch team, and [this dense blog post](https://blog.codingconfessions.com/p/gpu-computing) by Abhinav Upadhyay of Coding Confessions. We also highly recommend the [ML Engineering Open Book](https://github.com/stas00/ml-engineering/) by Stas Bekman for deep dives and useful snippets all across the stack.

*We’d like to thank  Mark Saroufim of PyTorch & the GPU_MODE Discord (join it!) and Erik Dunteman of Pig for comments on a draft of this post.*
