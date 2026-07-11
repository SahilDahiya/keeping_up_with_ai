---
title: How multi-node inference works for massive LLMs like DeepSeek-R1
topic: inference
subtopic: serving
secondary_topics:
- infra-platform/gpu-clusters
summary: Explains multi-node inference for very large LLMs such as DeepSeek-R1.
source: baseten
url: https://www.baseten.co/blog/how-multi-node-inference-works-llms-deepseek-r1/
author: Phil Howes; Philip Kiely
published: '2025-02-13'
fetched: '2026-07-11T04:08:25Z'
classifier: codex
taxonomy_rev: 1
words: 1470
content_sha256: 5bfc7746e1618415b94d24c1529f88a8526a12ea18d2e8cd496877f48cbbe39e
triage: keep
skip_reason: null
---

# How multi-node inference works for massive LLMs like DeepSeek-R1

![Multi-node inference](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1747428601-deepseek-multi-node.png%3Fauto%3Dformat%26fit%3Dcrop%26h%3D630%26w%3D1200&w=3840&q=100)

What do you do when you have a model like DeepSeek-R1 that’s too big to fit into an 8xH100 GPU node? Multi-node inference lets you recruit more than eight GPUs to serve a single model, but introduces new infrastructure and model performance challenges. At Baseten, we’ve built production-ready multi-node inference, and in this blog we’ll cover the key technical knowledge for understanding how it works.

If you want to run [DeepSeek-R1](https://www.baseten.co/library/deepseek-r1/) on H100 GPUs, you will very quickly encounter a major problem: even a full-size 8xH100 node does not have enough memory to run the model.

![DeepSeek weights are too large to fit in a single 8xH100 node](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1739470290-carbon-60.png%3Fauto%3Dformat%26w%3D1200&w=3840&q=75) DeepSeek weights are too large to fit in a single 8xH100 node

DeepSeek weights are too large to fit in a single 8xH100 nodeTo run LLM inference in production, your model serving instance must have enough VRAM to not only load the model weights but also store the KV cache and activations – in this case, hundreds of gigabytes of headroom on top of DeepSeek-R1’s massive 671GB of model weights.

Combining two H100 nodes – totaling 16 H100 GPUs – gets us 1280 GB of VRAM, plenty to run the model. H100 GPUs offer a great balance of performance and cost with increasing worldwide availability. Updating our math from above, we can see that a multi-node H100 instance will let us [serve DeepSeek-R1 in production](https://www.baseten.co/blog/private-secure-deepseek-r1-in-production-in-us-eu-data-centers/).

![DeepSeek-R1 runs in production on 16 H100 GPUs in a multi-node configuration](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1739470336-carbon-58.png%3Fauto%3Dformat%26w%3D1200&w=3840&q=75) DeepSeek-R1 runs in production on 16 H100 GPUs in a multi-node configuration

DeepSeek-R1 runs in production on 16 H100 GPUs in a multi-node configurationOn paper, this math looks great. But getting multi-node inference running in production is another story. Multi-node inference combines problems from two separate domains:

- **Infrastructure**: How do you ensure that the GPU nodes you provision have sufficient interconnects and establish consistent multi-cloud abstractions?
- **Model performance**: How do you make sure your LLM takes full advantage of these GPU resources for low-latency, high-throughput inference?

At Baseten, we can run our customers’ mission-critical workloads on multi-node model serving instances across multiple regions and cloud providers. In this blog post, we’ll break down everything you need to know from an infrastructure and model performance perspective to understand the potential that multi-node inference offers for serving models like [DeepSeek-R1](https://www.baseten.co/library/deepseek-r1/).

## From single-node to multi-node infrastructure

At the hardware level, the nodes we provision for inference typically consist of eight GPUs contained in a chassis. The GPUs have a PCIe or SXM connection to the chassis – Baseten exclusively uses the higher-performance SXM GPUs – while the chassis contains hardware for GPU-to-GPU communication and external networking.

![A high-bandwidth interconnect like InfiniBand connects two 8xH100 GPU nodes for inference.](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1739407200-image.png%3Fauto%3Dformat%26w%3D1200&w=3840&q=75) A high-bandwidth interconnect like InfiniBand connects two 8xH100 GPU nodes for inference.

A high-bandwidth interconnect like InfiniBand connects two 8xH100 GPU nodes for inference.The gold standard for an H100 node is the [NVIDIA DGX H100](https://www.nvidia.com/en-gb/data-center/dgx-h100/). However, many cloud providers instead buy GPUs directly and build their chassis in-house or order it from a third-party vendor to save on cost and customize it to their needs. It’s important to review the exact specs of the H100 nodes you’re using before setting up multi-node inference, as there is variation from provider to provider in the chassis, networking hardware, and auxiliary components.

### How GPUs communicate within a node

Within a single node, H100 GPUs communicate via two mechanisms: NVLink and NVSwitch.

NVLink and NVSwitch work together within a node to coordinate the eight GPUs during inference. During each forward pass through the model, tasks are split up, executed in parallel, and then the results are merged together.

### How GPUs communicate between nodes

With limited exceptions – like the [NVIDIA DGX SuperPOD](https://www.nvidia.com/en-us/data-center/dgx-superpod/) – NVLink and NVSwitch are limited to a single node of 8 H100s. We need another mechanism for communication between nodes.

For inter-node communication, the node’s chassis contains multiple Network Interface Cards (NICs), including:

- A lower-bandwidth VPC connection, likely Ethernet, for general networking.
- A high-bandwidth connection for inter-node communication.

Depending on the provider, this high-bandwidth NIC could implement a custom solution or follow a standard like InfiniBand. Like NVLink allows point-to-point communication between GPUs, InfiniBand and similar interconnects provide high-bandwidth network connections suitable for performant cross-node GPU-to-GPU communication.

Even the fastest node-to-node interconnects will be slower than intra-node NVLink. While H100 GPUs have a 900 GB/s bidirectional NVLink within the node, InfiniBand varies from 200 to 800 GB/s. However, the main bottleneck on inference speed (as measured by inter-token latency) is generally VRAM bandwidth, which is 3.35 TB/s on H100 GPUs.

If InfiniBand and NVLink are slower than VRAM, why aren’t they the bottleneck on inference speed? On each forward pass, many gigabytes of model weights are read from VRAM. Much less data passes along GPU-to-GPU and node-to-node interconnects to orchestrate parallel inference. While these interconnects have a lower bandwidth than VRAM, the relative volume of data means that VRAM remains the bottleneck.

Interconnect bandwidth still matters, but with an awareness of our hardware topology, we can parallelize model inference between nodes and GPUs for efficient performance across nodes.

## Maximizing model performance across multi-node instances

Leveraging multiple GPUs to serve LLMs requires some form of model parallelism, or splitting the model among multiple GPUs. This remains true for multi-node inference, but with even more GPUs to split the model across, how we choose to parallelize the model becomes even more important.

### Tensor parallelism for multi-node inference

The most common form of model parallelism for LLM inference is tensor parallelism, though mixture-of-experts models like DeepSeek-R1 can take advantage of new options like expert parallelism.

Tensor parallelism works by splitting the LLM weights across multiple GPUs. Working together, these GPUs can run models that are too large for one GPU to run alone. Additionally, Tensor parallelism accelerates inference overall, resulting in lower latencies and higher throughput.

![Tensor parallelism distributes model weights across GPUs during inference for large models.](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1739407125-image.png%3Fauto%3Dformat%26w%3D1200&w=3840&q=75) Tensor parallelism distributes model weights across GPUs during inference for large models.

Tensor parallelism distributes model weights across GPUs during inference for large models.For transformers-based LLMs, this process involves splitting the large model weights matrices across multiple GPUs, and then combining the computed results. Tensor parallelism works for a wide range of LLMs, but for DeepSeek-R1 and DeepSeek-V3, there is another option: expert parallelism.

### Expert parallelism for DeepSeek models

DeepSeek-R1 and DeepSeek-V3 are Mixture of Experts (MoE) models, a unique architecture that splits the model weights into distinct groups (“experts”) and calls only a subset of the weights based on the prompt. In DeepSeek’s case, there are 256 experts with 37B active parameters per inference request.

MoE reduces hardware requirements for low-throughput model serving, like running a single request at a time on a home computer. However, for production-grade model inference, we batch multiple requests together to maximize throughput. Because of this batching, we need enough VRAM to load every expert (all 671B parameters), as each request in a batch may activate different experts.

Fortunately, there is a way to take advantage of the MoE architecture for batched, high-throughput workloads. As an alternative to tensor parallelism, [expert parallelism](https://nvidia.github.io/TensorRT-LLM/advanced/expert-parallelism.html) distributes the model’s experts across the GPUs in the instance. For DeepSeek-R1 on a 16xH100 multi-node instance, each H100 GPU hosts 16 experts.

![For Mixture of Experts models, we have an additional parallelism option, expert parallelism, where each GPU holds a few experts in their entirety.](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1739407083-image.png%3Fauto%3Dformat%26w%3D1200&w=3840&q=75) For Mixture of Experts models, we have an additional parallelism option, expert parallelism, where each GPU holds a few experts in their entirety.

For Mixture of Experts models, we have an additional parallelism option, expert parallelism, where each GPU holds a few experts in their entirety.While Tensor parallelism puts an equal portion of each expert in each GPU, expert parallelism puts an equal number of whole experts in each GPU.

## Multi-node inference in production

Setting up multi-node inference in production has two key challenges. First, you have to provision GPUs with high-bandwidth interconnects between nodes. This requires consistent abstractions on top of varied networking hardware across providers. Then, you need to ensure that hardware topology is not a bottleneck to model performance by using optimizations like tensor or expert parallelism.

But the effort is worthwhile: multi-node inference lets you serve frontier models like DeepSeek-R1 on H100 GPUs, which are more widely available than [their larger H200 counterparts](https://www.baseten.co/blog/evaluating-nvidia-h200-gpus-for-llm-inference/) that run DeepSeek-R1 within a single node.

Additionally, multi-node inference supports connecting more than two H100 GPU nodes for running even larger model deployments with higher VRAM requirements.

Running the [world’s largest open-source LLMs like DeepSeek-R1](https://www.baseten.co/platform/models/deepseek/) in production requires a blend of applied model performance research and distributed GPU infrastructure. [Talk to us for help deploying DeepSeek models](https://www.baseten.co/talk-to-us/deepseek/) or other multi-node inference projects on production-ready infrastructure – in our cloud or yours.
