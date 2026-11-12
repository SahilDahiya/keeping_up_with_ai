---
title: Modal becomes a gVisor maintainer
kind: blog
topic: product-engineering
subtopic: security
secondary_topics:
- agents/computer-use
- infra-platform/gpu-clusters
summary: Modal becomes a gVisor maintainer as Google donates it to CNCF; details gVisor's
  Sentry application-kernel architecture, its nvproxy GPU ioctl proxy, ~25ms sandbox
  boot with 12MB overhead, and GPU-memory checkpoint/restore, run across 40 million
  containers/day including AI coding agent sandboxes.
triage: null
skip_reason: null
source: modal
url: https://modal.com/blog/modal-gvisor-maintainer
author: Ayush Ranjan; Luis Capelo
published: '2026-11-11'
fetched: '2026-11-12T06:16:45Z'
classifier: claude
taxonomy_rev: 2
words: 2061
content_sha256: 6ba4ea5dce335244a72b21db1b86b97325ed04eae99cd4f1af856f0582adb8a6
---

# Modal becomes a gVisor maintainer

This week at KubeCon in Salt Lake City, [Google is donating gVisor](https://gvisor.dev/blog/2026/10/02/gvisor-cncf/), including its name and trademarks, to the [Cloud Native Computing Foundation (CNCF)](https://www.cncf.io/), and the project is moving to a maintainer-led governance model. [Modal is one of three companies, alongside Ant Group and Tines, that have committed to join gVisor’s maintainers](https://cloud.google.com/blog/products/containers-kubernetes/open-infrastructure-for-autonomous-agents-comes-to-cncf), with OpenAI, Tencent and NVIDIA continuing their contributions.

[gVisor has been the major container runtime at Modal since the beginning](https://x.com/bernhardsson/status/1708929516955930699). We wanted a secure container runtime which provided GPU support, with stronger guarantees than [runc](https://github.com/opencontainers/runc) (the default runtime in the industry); and ever since we have been committed to making gVisor the safest and highest-performance runtime for AI workloads in the market.

We launch upwards of 40 million gVisor containers a day. That includes GPU inference, multi-node training, AI coding agents, sandboxes and more.

So here’s why we bet on gVisor, what we’ve built into it, and where we think it should go next.

## gVisor in one paragraph

On Linux, ordinary containers share the host kernel. Every system call your code makes lands in the same kernel that runs everyone else’s code, so a single kernel bug or vulnerability can let code escape a container and compromise the machine. gVisor adds a separate application kernel, called the [Sentry](https://gvisor.dev/docs/architecture_guide/intro/), written in Go between the container and the host. The Sentry implements the Linux system call interface itself and asks the host for only a small, filtered set of operations. Your program sees Linux. The host sees one well-behaved process.

gVisor’s security comes in layers. The first layer is the Sentry itself: it handles every system call the app makes with its own implementation, so the app never talks to the host kernel. The second layer assumes the first might fail. The Sentry, in turn, is hardened with the same Linux primitives that protect ordinary containers. Namespaces give it a private view of processes, networking and mounts. `pivot_root` leaves it with an empty root filesystem. cgroups cap the CPU and memory it can use and the devices it can reach. A tight seccomp filter allows only the few host system calls the Sentry needs, and validates many of their arguments. To reach the host, an attacker has to break the Sentry and then break out of that hardening as well.

gVisor doesn’t need hardware virtualization, which allows it to run on any Linux machine. That includes the cloud VMs where nested virtualization is unavailable or slow, and the bare-metal GPU servers that make up much of our fleet across dozens of cloud providers. Compared with plain containers (aka runc), it gives us a real security boundary between tenants.

## Why Modal runs on gVisor

The foundation of Modal is a custom container runtime that allows for the scale and performance our customers have come to expect. As an infrastructure provider, we run other people’s code, a lot of it, from a lot of people, on shared machines, scaling from [zero to a million sandboxes in a minute](https://modal.com/blog/scaling-to-1-million-concurrent-sandboxes-in-seconds). But we also have to keep all that code isolated, giving us a fairly demanding set of requirements:

- **Multi-tenancy needs a real boundary.** A shared host kernel is not an acceptable boundary when the code might have been written a minute ago by a model someone prompted.
- **GPUs have to just work.** gVisor’s nvproxy lets a sandboxed process use NVIDIA GPUs through a proxy that understands and validates the driver’s ioctl interface, instead of exposing the raw driver to the container. GPU memory and compute stay native.
- **Startup has to be fast.** gVisor can boot a sandbox in about 25 ms with only 12 MB of memory overhead.
- **State has to be portable.** gVisor can checkpoint an entire sandbox (every process, file and socket, and with [cuda-checkpoint](https://github.com/NVIDIA/cuda-checkpoint), GPU memory too) and restore it on another machine. That’s the foundation of [Modal memory snapshots](https://modal.com/blog/mem-snapshots) and [GPU memory snapshots](https://modal.com/blog/gpu-mem-snapshots).
- **It has to run everywhere we do.** No nested virtualization and no custom host kernel, so the same sandbox runs on every cloud and every bare-metal box we buy.

Google’s announcement describes Modal as [one of the few providers selling general-purpose gVisor-powered compute](https://gvisor.dev/blog/2026/10/02/gvisor-cncf/). We think that’s about to change, and the CNCF move is a big part of why.

## By the numbers

![gVisor at Modal scale](https://modal-cdn.com/cdnbot/gvisor-stats9pkafac4_2decebe0.webp) 

Modal has been a contributor to gVisor since 2023, and we’ve significantly ramped up pushing upstream since then. This year we built a team around it to better support our customers’ needs.

## What we’ve built, and sent upstream

Our customers give us plenty to work on in gVisor. A new GPU to support, a profiler to get running, a few more GB/s to squeeze out of shared memory. We do that work and send the changes upstream. Modal publishes the vast majority of its patches as open source, and we’re committing more engineering time to the project as we join its maintainers.

### GPUs: keeping nvproxy in step with NVIDIA

nvproxy is the part of gVisor that makes GPUs work. It has to understand every ioctl call the NVIDIA user-space driver sends to the kernel driver, and NVIDIA changes that interface with driver releases. We’ve upstreamed:

- **New GPUs and drivers.** Support for new NVIDIA driver releases as they ship, and the missing pieces for newer GPUs such as Blackwell and the RTX PRO 6000.
- **Multi-GPU workloads.** GPUs in the same server can talk to each other directly over NVLink, including the NVLink features NCCL uses on large H100 and H200 servers. Processes can share GPU memory with each other, which NCCL relies on to move data between GPUs on the same machine. With CUDA MPS, several processes can share one GPU efficiently.
- **Graphics, simulation and video.** Vulkan and headless OpenGL rendering, plus NVIDIA’s hardware video encoders and decoders. That covers robotics simulators like MuJoCo and NVIDIA Omniverse, and GPU video pipelines in FFmpeg.
- **Monitoring.** `nvidia-smi` and NVIDIA’s DCGM monitoring tools work inside the sandbox, including per-process GPU utilization.
- **Profiling and debugging.** NVIDIA Nsight Systems and Nsight Compute, hardware tracing on Blackwell GPUs, and GPU core dumps for debugging kernels that crash.
- **GPUDirect RDMA.** GPU memory can be handed straight to the network card, so data moves between GPUs on different machines without a detour through the CPU. This is what let us run [ModelExpress](https://github.com/ai-dynamo/modelexpress) in gVisor (more in the RDMA section below).

The result is that a wide variety of complex and niche GPU workloads now run in gVisor.

### RDMA: multi-node training inside the sandbox

When we were building multi-node support, gVisor didn’t support RDMA—so we added it and upstreamed the changes. Multi-node training, where GPUs on different machines exchange gradients over InfiniBand, RoCE, or EFA, previously had to run outside the sandbox. We built **rdmaproxy**, a new gVisor device proxy for the RDMA verbs interface, modeled on nvproxy. The container gets the NIC’s real data path, and gVisor validates the control path.

- Supports NVIDIA ConnectX (InfiniBand and RoCE) and AWS EFA.
- Builds an RDMA sysfs topology inside the sandbox, so NCCL pairs each GPU with the right NIC.
- Handles UCX-based data planes as well as NCCL.
- Reaches about 99% of native bus bandwidth in NCCL all-reduce benchmarks.

This is what let us take [Modal Clusters to general availability](https://modal.com/blog/modal-clusters-generally-available) with multi-node jobs running in gVisor.

### Snapshots: restoring GPU state in seconds

Modal [memory snapshots](https://modal.com/docs/guide/memory-snapshots) use gVisor’s checkpoint/restore to capture a container after it has loaded its model, then restore that state on new machines in seconds. About 670k gVisor containers are restored from a snapshot each day.

### Filesystem and memory performance

I/O performance has been a long-standing problem in gVisor. AI workloads often hit those paths, so a lot of our recent upstream work is there. Some examples:

- **PyTorch DataLoader over shared memory:** recycling huge pages in gVisor’s memory allocator took one batch-passing benchmark from 2.9 to 22 GB/s (about 8x) while keeping memory use flat.
- **Filesystems:** we optimized gVisor tmpfs, which made SQLite 2.7x faster. We’ve also submitted a series of overlayfs optimizations that reduce file data copy-up on common paths.

### More software, out of the box

gVisor implements the Linux interface itself, so every app that runs on Modal is also a test of how complete that implementation is. Our customers run a huge variety of software. When they bring something new, we make sure it runs well in gVisor and send the change upstream. Some recent additions:

- Databases: ClickHouse runs in gVisor sandboxes, including the atomic file swaps it uses to manage its tables.
- JavaScript: Bun apps, like the OpenCode coding agent, work with Modal memory snapshots.
- Desktop apps: apps built on Qt 5.15 run in gVisor.
- Cloud storage: Mountpoint for Amazon S3 can mount an S3 bucket as a folder inside a sandbox and write to it in large, fast chunks.
- Everyday tools: top and htop show real CPU usage inside a sandbox.
- CPU inference: math libraries like oneDNN, which PyTorch uses on CPUs, can use the processor’s fast bfloat16 and int8 instructions.
- Large codebases: sandboxes stay lean even after tools scan millions of files, which coding agents do constantly.

## Our vision for gVisor

We think gVisor should become the default way to run untrusted code on Linux, and especially the default isolation layer for AI compute. Here’s what that takes:

1. **Secure by default and fast enough to forget about.** Isolation shouldn’t be a tax you weigh against performance. That means near-native I/O, and moving the performance work that providers like us have carried in our own forks into upstream.
2. **Every accelerator, on day one.** New NVIDIA drivers and GPUs should work in gVisor the day they ship.
3. **Sandbox density.** Leverage gVisor’s resource efficiency to build very economical sandboxes which can handle a wide variety of agentic tasks.
4. **Portable state.** Snapshot anything (CPU, one GPU, many GPUs) and restore it anywhere.
5. **Open and multi-vendor.** Neutral governance makes it safe for many companies to invest, and that investment is what makes the rest of this list happen.

## What’s next

We want gVisor to be the safest way to run Linux programs but also one that solves many performance issues affecting the AI industry today. Here are some of the projects we are working on:

- **Multi-GPU memory snapshots.** Today, Modal can snapshot programs running on a single GPU. We’re extending that to models that span several GPUs. In early tests, large models come back several times faster than a normal cold start. This is coming to Modal soon as an experimental feature.
- **GPUDirect Storage.** GPUs can read data straight from fast storage into their own memory, skipping the usual detour through the CPU. It’s the quickest way to get a large model’s weights onto a GPU, and we’re bringing it to gVisor.
- **Inference servers that start in seconds.** Most of an inference server’s startup goes to loading model weights and warming up. We want to warm a server up once, set its weights aside, and take a small multi-GPU snapshot of everything else, including compiled kernels, CUDA graphs and KV cache memory. A new replica then restores that snapshot and streams its weights straight into GPU memory, from storage with GPUDirect Storage or from other GPUs over RDMA, so even very large models can be serving in under a minute.
- **Cloud gaming and remote desktops.** We want a GPU sandbox to be able to run a whole desktop: a display server on the NVIDIA driver, games and 3D apps drawing to it, and the screen captured on the GPU and streamed to the player over the network. That includes Windows games running through Steam’s Proton.
- **Smaller slices of a GPU.** MIG and vGPU support in nvproxy.
- **Grace Blackwell GPU support.**
- **Kernel module-based optimizations for gVisor.**

## Check it out!

- **Try it:** Modal Functions and [Modal Sandbox](https://modal.com/docs/guide/sandbox) (with `runtime="gvisor"`) run on gVisor.
- **Contribute:** [github.com/google/gvisor](https://github.com/google/gvisor)
- **Join us:** [we’re hiring](https://jobs.ashbyhq.com/modal/6195f552-ca6f-4540-b7f6-e7e6054e47ad) engineers who want to work on kernels, runtimes and GPUs.

## Thanks

Thanks to the gVisor team at Google for building something worth donating and for doing the hard work of handing it over well. Special thanks to Etienne Perot, Jing Chen, Steve Silva, Jago Macleod and Drew Bradstock for driving the CNCF donation.
