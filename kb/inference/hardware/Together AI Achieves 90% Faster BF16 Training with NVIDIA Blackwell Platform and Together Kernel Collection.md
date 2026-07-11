---
title: Together AI Achieves 90% Faster BF16 Training with NVIDIA Blackwell Platform
  and Together Kernel Collection
topic: inference
subtopic: hardware
secondary_topics:
- models/fine-tuning
summary: Describes Blackwell BF16 training acceleration with the Together Kernel Collection.
source: together
url: https://www.together.ai/blog/nvidia-hgx-b200-with-together-kernel-collection
author: Together AI
published: '2025-02-13'
fetched: '2026-07-11T04:24:52Z'
classifier: codex
taxonomy_rev: 1
words: 1361
content_sha256: 1f93ba08d621453103519847011973523548c0225c6a2fc6ecac9d57caaf9c1b
triage: keep
skip_reason: null
---

# Together AI Achieves 90% Faster BF16 Training with NVIDIA Blackwell Platform and Together Kernel Collection

Today we are announcing immediate access to [Together GPU Clusters](https://www.together.ai/gpu-clusters) accelerated by the [NVIDIA Blackwell](https://www.nvidia.com/en-us/data-center/technologies/blackwell-architecture/) platform, and an accompanying AI acceleration stack optimized for the latest GPU architecture.

Together GPU Clusters featuring [NVIDIA HGX B200](https://www.together.ai/nvidia-hgx-b200) are turbocharged with Together Kernel Collection to deliver unprecedented performance: 90% faster training than NVIDIA HGX H100, achieving 15,200 tokens/second/node on a training run for a 70B parameter model.

Our research team has achieved these incredible speed-ups by leveraging NVIDIA Blackwell’s advanced features using the open-source ThunderKittens framework. We developed custom FP8 kernels that take full advantage of Blackwell’s 5th-generation [NVIDIA Tensor Cores](https://www.nvidia.com/en-us/data-center/tensor-cores/) and dedicated on-chip memory to produce attention kernels that run 1.8x faster than FlashAttention-3.

In an exclusive launch program, we're offering eight pioneering AI teams the opportunity to test drive dedicated HGX B200 nodes and collaborate directly with NVIDIA engineers and Together AI researchers to accelerate their AI workloads. This collaboration combines Together AI's kernel optimization expertise with NVIDIA's latest accelerated computing platform innovations, setting new benchmarks for AI training and inference efficiency (up to 4X faster Llama-2-70B in [MLPerf Inference v4.1](https://developer.nvidia.com/blog/nvidia-blackwell-platform-sets-new-llm-inference-records-in-mlperf-inference-v4-1/)).

{{custom-cta-1}}


We are deploying tens of thousands of NVIDIA HGX B200 servers and [GB200 NVL72](https://www.together.ai/nvidia-gb200-nvl72) rack-scale solutions with NVIDIA Quantum-2 InfiniBand networking – including the [36K+ GPU GB200 NVL72 cluster](https://www.together.ai/blog/nvidia-gb200-together-gpu-cluster-36k) we announced previously. All Together GPU Clusters feature the highest-performance NVIDIA NVLink within a node and NVIDIA Quantum-2 InfiniBand networking across nodes, providing the scale and performance needed to build and deploy the next generation of AI reasoning models and agents.

Our team is eager to work hand in hand with yours, forging the frontier of AI, together.

*"Together AI optimizes every layer of the AI stack to fully take advantage of advances in GPU architecture, like NVIDIA Blackwell. We write custom kernels to maximize both speed and scalability, and we’re particularly excited about the new microscaling data format to speed up model inference and the new Tensor Cores to optimize training. By combining Together Kernel Collection with NVIDIA Blackwell, we’re not just accelerating workloads — we’re redefining what efficient AI training and inference looks like at scale."* - Tri Dao, Together AI Chief Scientist and FlashAttention creator

**Together Kernel Collection and NVIDIA HGX B200: 90% Faster Training than NVIDIA HGX H100 Performance with BF16 Precision**

To benchmark the performance of [Together GPU Clusters](https://www.together.ai/gpu-clusters) with NVIDIA HGX B200, we tested the training speed of a 70B parameter Llama-architecture model, using an optimized version of [TorchTitan](https://github.com/pytorch/torchtitan) combined with the Together Kernel Collection (TKC). The result?

🚀 A 90% improvement in training throughput over NVIDIA HGX H100.

Compared to optimized software running on the previous generation of accelerators, which processed 8,080 tokens/second (BF16) per NVIDIA HGX H100, we reached 15,264 tokens/second/GPU with NVIDIA HGX B200 — a 90% jump in training speed!

![](https://cdn.prod.website-files.com/69654e88dce9154b5f12070c/699e0b15c27d8ee7be02ed35_67ad4e50925f89ab8e4d59f8_AD_4nXd19Grs2AxTpDj3Z3woX8g5BUxxpRcuT2v5Gjp_VHgm0Z3_8GMx9LjjleVW0h4MCdzZfTstDSbmJO5EJEmy_JQIfx9kDM0srb0RKWLXs50pn6uMVmJKkOxcrddvppB4lCm9EE3FhsIuBRrTQCZzLWk.png)

By leveraging state-of-the-art distributed training algorithms and hardware-aware optimizations, Together AI ensures that AI teams can train massive models faster and more efficiently. And, with additional software optimizations coming soon, performance will only get faster from here on out.

**Optimizing Together Kernel Collection for NVIDIA Blackwell Platform**

At Together AI, our goal is to accelerate AI by optimizing every layer of the AI stack – and that’s why we invest significant research and development resources towards the creation of high-performance kernels. Kernels are the core software programs that run on GPUs, performing critical AI computations such as attention mechanisms and matrix multiplications. By developing optimized kernels, we unlock faster training and inference speeds, reducing costs and improving efficiency.

With the introduction of the NVIDIA Blackwell platform, we now have access to novel hardware features that allow us to push AI performance further than ever before. These include:

- 5th-generation Tensor Cores – Compute matrix multiplication 2x faster than on NVIDIA Hopper.
- On-chip Tensor Memory – Adds an extra memory layer for deeper pipelines, keeping Tensor Cores fully utilized.
- Peer CTA Groups – Enables coordination among paired warps for larger and more efficient matrix operations.
- MXFP8, MXFP6, and MXFP4 Precision Format – Boosts memory bandwidth utilization for inference workloads and doubles the tensor core throughput.

To take advantage of Blackwell’s hardware features, Together AI leverages open-source frameworks such as [NVIDIA CUTLASS](https://github.com/NVIDIA/cutlass), [Triton](https://github.com/triton-lang/triton), and [ThunderKittens](https://github.com/HazyResearch/ThunderKittens). These frameworks simplify the development of high-performance kernels by using a tile-based abstraction, which efficiently maps key matrix operations onto Tensor Cores — specialized matrix multiplication units that account for over 98% of available FLOPs on NVIDIA GPUs.

In this section, to showcase kernel development velocity on NVIDIA Blackwell platform, we use ThunderKittens, an open-source kernel framework that is a joint-effort between Stanford researchers and Together AI. This framework ensures compatibility with new hardware generations, making it easy to utilize NVIDIA Blackwell. Through our ongoing collaboration with NVIDIA and Stanford researchers, ThunderKittens now supports the Blackwell architecture.

Using ThunderKittens, we have been able to rapidly develop a [FP8 kernel](https://github.com/HazyResearch/ThunderKittens/tree/blackwell/kernels/matmul/FP8_B200) for NVIDIA HGX B200 in under two weeks, writing fewer than 200 lines of code. This kernel already matches the performance of [NVIDIA cuBLAS](https://developer.nvidia.com/cublas) GEMM kernels while achieving more than 2x speedup over H100 FP8 GEMMs.

![Bar chart comparing FP8 GEMM performance in TFLOPS for cuBLAS H100, cuBLAS B200, and ThunderKittens B200.](https://cdn.prod.website-files.com/69654e88dce9154b5f12070c/699e0b15c27d8ee7be02ed38_67ad4e508e4540bb28bc1ee1_AD_4nXcj4mbk-uj_tlAQF5aNMjyVCdlVitESiSZNEIimwn5Bbhzdo1NlbuYChAXCUPl3N2UJnRSeMvxH4f0Lhk3DsyAruJGOsyUGcQxvgdeI7Euk8VmKHtB7dfYoqEbmQjLXVP-3YvVuOeJ7ywow_W2Sq-s.png)

At Together AI, we are committed to pushing AI performance to new heights through optimized software and hardware integration. If you’d like to read more in-depth technical details regarding how we used all the new Blackwell Platform hardware features to build new kernels, including new attention kernels 1.8x faster than FlashAttention-3, FP4 GEMMs, and more, stay tuned for a blog post regarding our collaboration with our research partners at Stanford. Together AI will continue to push the frontier of generative AI training and inference performance, extracting the highest performance from the platform.

**Together AI Uses NVIDIA Blackwell Platform **

Together GPU Clusters follow the latest NVIDIA Blackwell platform reference architectures including 1.8TB/s NVLink and NVLink Switch, 3.2TB/s Quantum-2 InfiniBand networking, NVIDIA ConnectX-7 HCAs, GPU direct fast storage, and an optimized software stack that accelerates training workloads.

NVIDIA Blackwell is a big step up in GPU architecture, purpose-built for the era of trillion-parameter reasoning models and massive-scale AI workloads. With innovations like 5th-generation Tensor Cores, advanced memory hierarchies, and improved energy efficiency, the Blackwell platform delivers massive performance gains over previous architectures.

NVIDIA HGX B200 represents a major leap in AI compute power, featuring:

- Up to 1.4TB of HBM3E memory per node (8 GPUs) to fit the largest models.
- Fifth-generation NVLink interconnect, enabling high-speed multi-GPU scaling with a total aggregate bandwidth of 14.4TB/s.
- Optimized for FP8, FP6, and FP4, pushing efficiency in both training and inference workloads.

The NVIDIA GB200 NVL72 rack-scale platform extends this even further, featuring:

- Liquid-cooled, rack-scale solutions capable of scaling to up to 110,000 GPUs.
- Fifth-generation NVLink across 72 NVIDIA Blackwell GPUs and 36 NVIDIA Grace CPUs.
- Fifth-generation NVLink enables 130TB/s of GPU bandwidth in one 72-GPU NVLink domain.
- NVIDIA Quantum-2 InfiniBand networking.

**Test Drive Together AI Powered by the NVIDIA Blackwell Platform**

To celebrate NVIDIA Blackwell's arrival, and to help customers understand the performance gains from these new GPUs and Together Kernel Collection, we’re inviting AI teams to apply for a **free accelerated test drive** of [Together GPU Clusters](http://together.ai/gpu-clusters) powered by NVIDIA HGX B200 and NVIDIA GB200 NVL72.

🏎️ How the Together AI test drive of NVIDIA Blackwell platform works:

- 8 selected teams will receive free access to a NVIDIA HGX B200 node (8 GPUs) for one week.
- Together AI researchers and NVIDIA engineers will work hand-in-hand with you to optimize your model’s performance on Blackwell.
- Selected teams will have the opportunity to share their performance gains as case studies — highlighting their breakthroughs with NVIDIA HGX B200 and Together Kernel Collection.

📢 [ Apply for a free accelerated test drive](http://together.ai/b200-early-access) to be among the first to harness the Together Kernel Collection with NVIDIA Blackwell – and take your AI training and inference to a whole new gear.

{{custom-cta-2}}

Get your free week on a dedicated NVIDIA HGX B200 GPU Cluster starting March 1. Work with NVIDIA and Together AI Reseaarch teams to optimize performance.

Request a free test drive of Together GPU Clusters, accelerated by NVIDIA Blackwell GPUs.
