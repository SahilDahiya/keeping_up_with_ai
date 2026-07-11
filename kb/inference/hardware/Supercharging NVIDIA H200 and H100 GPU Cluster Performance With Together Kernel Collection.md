---
title: Supercharging NVIDIA H200 and H100 GPU Cluster Performance With Together Kernel
  Collection
topic: inference
subtopic: hardware
secondary_topics:
- infra-platform/gpu-clusters
summary: Shows how kernel work improves H200 and H100 GPU cluster performance.
source: together
url: https://www.together.ai/blog/nvidia-h200-and-h100-gpu-cluster-performance-together-kernel-collection
author: Together AI
published: '2024-09-05'
fetched: '2026-07-11T04:24:50Z'
classifier: codex
taxonomy_rev: 1
words: 1798
content_sha256: 4ec92a0683cceb0f6285ffeb36a6df5d048f5324bc3b81760b46c74554c042a2
triage: keep
skip_reason: null
---

# Supercharging NVIDIA H200 and H100 GPU Cluster Performance With Together Kernel Collection

At Together AI, we're shaping the future of artificial intelligence by integrating cutting-edge research into an end to end platform covering the full AI lifecycle: training, fine-tuning, and inference. Today, we're excited to announce that the **NVIDIA H200 Tensor Core GPU** will soon be available in our [Together GPU Clusters](https://www.together.ai/gpu-clusters?utm_campaign=forge-h200&utm_source=TKC-announcement&utm_medium=blog). These clusters will be equipped with our custom-built Together Kernel Collection (TKC), an optimized kernel stack that significantly accelerates common AI operations. Compared against the PyTorch implementations that most researchers currently use, TKC offers up to 24% speedup for operators used frequently in training, and up to 75% speedup for the fundamental operation used in FP8 inference.

With TKC, Together H100 and H200 GPU Clusters enable you to reduce GPU hours resulting in cost efficiencies and allowing faster time to market.

Together's infrastructure is purpose-built for the entire generative AI lifecycle, offering up to 4x lower total cost of ownership (TCO) compared to hyperscalers. Our GPU Clusters deliver industry-leading performance with 99.9% reliability, thanks to [rigorous acceptance testing](https://www.together.ai/blog/a-practitioners-guide-to-testing-and-running-large-gpu-clusters-for-training-generative-ai-models) we've developed and successfully implemented across clusters containing thousands of GPUs.

Whether you're scaling frontier models, building custom enterprise models, [fine-tuning Llama](https://www.together.ai/blog/meta-llama-3-1), or developing new AI applications, Together's GPU Clusters combined with TKC deliver unparalleled performance, accuracy, and efficiency.

**Reserve your high-performance H200 GPU Cluster today****. **Existing and new H100 customers will receive priority access to the new hardware.


*"Using Together AI's GPU Clusters has been a game-changer for Linum.ai. The incredible speed and scalability allowed us to efficiently train our text-to-video diffusion models, enabling us to bring our vision of democratizing animation to life faster than we ever imagined."*

*- Sahil Chopra and Manu Chopra, Founders, Linum*

## Together Kernel Collection: Enabling maximum hardware utilization and performance

Together AI is a leader in AI systems research, with a particular focus on optimized kernels like [FlashAttention](https://www.together.ai/blog/flashattention-3) that make today's frontier LLMs possible. We're continuing this practice with the Together Kernel Collection (TKC) – our fastest implementations of widely-used layers in AI models, packaged into clean interfaces that are natively compatible with PyTorch. TKC accelerates some of the most common operations in AI training (10% faster) and inference (75% faster).

TKC is the best of our research team's work, and we rely on these tools in production for training and inference every day. Kernels in TKC have been tested for state-of-the-art performance, and we're excited for our customers to benefit from this work. Going forward, all Together GPU Clusters – H200 or H100 – will feature the Together Kernel Collection right out of the box.

**Training**

For training, one of the most widely used kernels in TKC is our optimized MLP (multi-layer perceptron), with SwiGLU activation. This layer accounts for the majority of runtime in most architectures, around 70% for a typical Transformer such as Llama-3. This layer is already extensively optimized by vendor libraries (e.g., cuBLAS) and deep learning frameworks (e.g. PyTorch). And yet, our specialized kernel is 22-24% faster than the common implementation using cuBLAS and PyTorch eager mode. Compared to the best baseline that we know of (cuBLAS and torch compile), TKC is still 10% faster, reaching up to 810 TFLOPS (82% of theoretical max) on H100 SXM5. This could translate to up to 5-10% faster LLM inference (time to first token) or LLM training.

![__wf_reserved_inherit](https://cdn.prod.website-files.com/69654e88dce9154b5f12070c/69a6af2e30acb03601f3202d_699e0b14b5c04b8ed13f782e_66d9f79fbad1a4fd54048ccc_66d9f78e54ba3873e3ee4c2a_together-kernel-collection-training-performance.png)

**Inference**

Together has built a robust stack of FP8 kernels to power our Turbo model families. FP8 is still treated as experimental in many open-source libraries, but our research team has worked with FP8 since it was introduced in the Hopper architecture. Our battle-tested FP8 inference kernels deliver more than 75% speedup over base PyTorch.

![__wf_reserved_inherit](https://cdn.prod.website-files.com/69654e88dce9154b5f12070c/69a6af2e30acb03601f32029_699e0b14b5c04b8ed13f7827_66d9f79fbad1a4fd54048ccf_66d9f798f205974f301029da_together-kernel-collection-inference-performance.png)

Unlike the large matrix-matrix multiplications seen in training, inference involves mostly skinny matrix operations, where the input tensor is much smaller than the weight tensor. These problems are largely memory-bound instead of compute-bound, and the tuning process is accordingly different. Traditional wisdom in kernel optimization, such as "focus on tensor core utilization", does not always apply. Instead, we focus on efficient quantization and compression, optimized memory access patterns, and fusion wherever possible.


**Native PyTorch compatibility**

TKC is fully integrated with PyTorch, making it easy to use as native operators in frameworks like torch.compile. This integration allows AI developers to leverage TKC's optimizations as easily as any other PyTorch function. In many cases, integrating TKC can be as simple as changing some import statements.

**Production-level testing**

TKC undergoes rigorous testing to meet production-level standards. This testing guarantees that the kernels are not only high-performing but also reliable and stable for real-world applications.


## The NVIDIA H200: Supercharging AI and HPC Workloads

The NVIDIA H200 Tensor Core GPU, built on the advanced Hopper architecture, is designed to excel in both AI and high-performance computing (HPC) workloads.

**Faster Performance with Larger, Faster Memory**

According to NVIDIA's published results, the H200 provides 40% faster inference performance on Llama 2 13B, and 90% faster performance on Llama 2 70B, demonstrating the GPU's significant improvement in handling large-scale language models.

With 141GB of HBM3e memory and 4.8TB/s of memory bandwidth, it offers nearly double the capacity and 1.4X of the bandwidth of its predecessor, the H100. This substantial memory and bandwidth allow the H200 to handle even the most data-intensive applications with ease, minimizing bottlenecks and enabling real-time processing of vast datasets — critical for high-throughput, low-latency AI tasks like generative AI and large language models (LLMs) training and inference.

**Comparing H200 vs H100 Performance**

![__wf_reserved_inherit](https://cdn.prod.website-files.com/69654e88dce9154b5f12070c/69a6af2e30acb03601f32022_699e0b14b5c04b8ed13f782a_66d9ef5d27b8509347e5f49f_66d9ef4c661756cd51fdee67_together-kernel-collection-inference-performance.png)

**Performance on Various Models**

| Benchmark | Server | Offline |
|---|---|---|
| Llama 2 70B | 32,790 token/s | 34,864 token/s |
| Mixtral 8x7B | 57,177 token/s | 59,022 token/s |
| GPT-J | 19,243 token/s | 20,086 token/s |
| Stable Diffusion XL | 16.78 queries/s | 17.42 samples/s |
| DLRM v2 99% | 585,208 queries/s | 637,342 samples/s |
| DLRM v2 99.9% | 370,083 queries/s | 390,953 samples/s |
| ResNet-50 v1.5 | 632,229 queries/s | 756,960 samples/s |
| BERT 99% | 57,609 queries/s | 73,310 samples/s |
| BERT 99.9% | 51,212 queries/s | 63,950 samples/s |
| RetinaNet | 13,604 queries/s | 14,439 samples/s |
| 3D U-Net | Not part of benchmark | 54.71 samples/s |

*Source: **NVIDIA MLPerf Inference v4.1 data center results*

**High-Performance Interconnectivity with SXM Form Factor, Infiniband, and NVLink**

Together GPU Clusters with NVIDIA H200 GPUs leverage the SXM form factor, providing a direct connection to the motherboard for higher bandwidth and faster data transfer. H200 SXM GPUs support NVIDIA's NVLink and NVSwitch technologies, enabling ultra-high-speed communication between GPUs within the same node. When combined with NVIDIA Quantum-2 3200Gb/s InfiniBand Networking for node-to-node connectivity, these technologies allow hundreds or even thousands of H200 GPUs to be interconnected as one cohesive computing fabric. This setup is ideal for large-scale AI training and HPC workloads, where efficient inter-GPU communication is critical for performance and scalability.


## Let's Build AI Together

Here at Together we are uniquely committed to AI's progress – and to customer success.

**Massive Savings**

Together AI's infrastructure is designed to be cost-effective, offering up to 75% savings compared with cloud providers such as AWS. If you're training a large model or running inference on hundreds or thousands of GPUs, the savings can easily add up to millions of dollars annually.

**Flexible Commitments**

At Together AI, we know well that each phase of the AI development lifecycle has its own unique infrastructure requirements. During the pre-training and fine-tuning phases, you might need a large number of GPUs to handle computationally intensive workloads. As you transition to serving the model for inference, your GPU needs may decrease, perhaps considerably — at least until your application goes viral, and you suddenly need more GPUs than ever before.

That's why we offer flexible commitment options, from one month to five years, ensuring the right resources at every stage.

It's also important to note that you can repurpose your Together GPU Clusters as your AI initiatives progress – moving seamlessly from training to serving customers with the best performance, accuracy, and efficiency, using [Together Inference Engine 2.0](https://www.together.ai/blog/together-inference-engine-2).

**Reliability You Can Trust**

Our GPU clusters are designed with reliability in mind, backed by a 99.9% uptime SLA. [We conduct rigorous acceptance testing](https://www.together.ai/blog/a-practitioners-guide-to-testing-and-running-large-gpu-clusters-for-training-generative-ai-models) to ensure that our infrastructure can handle even the most demanding AI workloads.

**White Glove Service**

When you choose Together AI, you gain access to our industry-leading White Glove Service. Our team of experts provides end-to-end support, from cluster setup to ongoing maintenance. We ensure your AI models are always running at peak performance, with dedicated support managers and advanced observability tools at your disposal.


## Flexible Cluster Deployment Options: Slurm, Kubernetes, or Bare Metal

We understand that different AI projects have different needs. That's why we offer flexible deployment options for Together GPU Clusters, allowing you to choose the setup that best suits your specific requirements.

**Slurm: High-Performance Workload Management**

Slurm is a robust and scalable workload manager that allows you to efficiently schedule and manage your AI jobs across clusters. With Slurm, you can optimize resource allocation, manage job queues, and ensure that your AI workloads are executed with maximum efficiency. This option is ideal for organizations running large-scale AI projects that require sophisticated job scheduling and resource management.[Using Slurm with Together](https://docs.together.ai/docs/cluster-setup) is straightforward and easy to get started. Simply SSH into your cluster, submit jobs, and you're on your way.

**Kubernetes: Containerized AI Workloads**

For those looking to deploy AI workloads in a containerized environment, Together AI offers Kubernetes. Kubernetes allows you to manage and orchestrate your containers across our GPU Clusters, providing flexibility and scalability for AI projects. This setup is particularly beneficial for teams that need to scale up or down quickly and want to maintain a high level of control over their environment.

**Bare Metal with Ubuntu: Direct Access for Power Users**

For AI practitioners with particularly unique needs, who prefer full control of their software stack, Together AI offers bare metal clusters running Ubuntu. This option provides the ultimate in flexibility and performance, allowing you to configure your environment exactly as you need it. Whether you're running custom AI models, conducting high-performance computing, or experimenting with novel architectures, the bare metal option gives you the freedom to push your AI research to new heights.


## Accelerating the Full AI Lifecycle With an Integrated Platform

Together AI supports the entire AI lifecycle — from training to inference—with NVIDIA H200 GPU Clusters and the Together Kernel Collection (TKC) providing unparalleled acceleration. Our platform is designed to optimize performance, reduce costs, and ensure reliability at every stage. Whether you're refining models or scaling them in production, we provide the tools and support needed to accelerate your AI journey.

[ Request early access to your Together GPU Cluster](https://www.together.ai/forms/gpu-cluster-requests?utm_campaign=forge-h200&utm_source=TKC-announcement&utm_medium=blog) and take the next step in your AI journey with the industry's best-in-class infrastructure.
