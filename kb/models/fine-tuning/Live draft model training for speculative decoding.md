---
title: Live draft model training for speculative decoding
topic: models
subtopic: fine-tuning
secondary_topics:
- inference/optimization
summary: Describes live draft-model training for speculative decoding systems.
source: baseten
url: https://www.baseten.co/blog/live-draft-model-training-for-speculative-decoding/
author: Mahmoud Hassan
published: '2026-06-25'
fetched: '2026-07-11T04:04:57Z'
classifier: codex
taxonomy_rev: 1
words: 870
content_sha256: 029e01e9a462a742f5ef0d70a6668285d080f4458596cc978ddab62f8716dbfa
triage: keep
skip_reason: null
---

# Live draft model training for speculative decoding

![Live draft model training for speculative decoding](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1782395640-baseten-blog-2026-thumbnails-11.png%3Fauto%3Dformat%26fit%3Dcrop%26h%3D630%26w%3D1200&w=3840&q=100)

Draft models, such as [EAGLE-3](https://www.baseten.co/blog/how-to-train-custom-eagle-3-heads-for-speculative-decoding/) and [DFlash](https://www.baseten.co/blog/dflash-faster-llm-inference/), have become a widely adopted technique for accelerating large language model (LLM) inference, leading to 2-3x higher throughput and lower latency. However, keeping these draft models aligned with diverse base models and dynamic traffic patterns remains a significant engineering challenge.

We built a distributed training pipeline to address this. The pipeline extracts hidden states directly from live inference and uses them to train the draft model on the fly, eliminating the need to store data offline.

Where rolled out, it has produced a **median increase in accept rate of 20%**, with some constrained traffic patterns seeing **100%+ increases**. These gains translate directly into larger speculative decoding speedups and better serving efficiency.

**Eliminating traditional bottlenecks**

Traditional approaches to training draft models are bottlenecked by several pain points:

- **Storage overhead:**Saving hidden states for offline training is infeasible at production volumes. A single sample on Kimi K2 can exceed 2GB, and full draft training requires millions of them.
- **Compute bottlenecks:**Generating the hidden states required for draft model inputs can be prohibitively expensive, particularly for massive models operating at long context lengths.
- **Alignment drift:**Fine-tuning or reinforcement learning (RL) on the base model often degrades the draft model's accept rate unless it is retrained alongside it.
- **Data compliance:**Storing data for offline training can be difficult in zero data retention (ZDR) environments.

To overcome each of these bottlenecks, we built a distributed training pipeline that uses real-time hidden states directly from inference to train draft models on the fly, while adding minimal overhead to the serving path.

This architecture bypasses the need for data storage entirely. It has significantly reduced the time required to train draft models for new base models, while also allowing those models to continuously adapt to custom traffic.

Where incorporated, we observed a median accept rate increase of 20%, with some constrained traffic patterns seeing a 100%+ increase in accept length, leading to even faster SpecDec in production and more efficient workloads.

**Engineering draft model training for minimal overhead**

![Inference and training nodes run in parallel across a distributed cluster.](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1782399206-speculator-diagram_kb-update_62426-1.png%3Fauto%3Dformat%26w%3D1200&w=3840&q=75) Inference and training nodes run in parallel across a distributed cluster. Raw data is streamed from the inference process directly to the training aggregator, eliminating the need for data storage. Hidden states flow through CUDA-IPC double buffering into pageable memory via mmap, keeping memory overhead minimal. The architecture scales horizontally across both data-parallel and context-parallel dimensions, so draft model training happens continuously alongside live inference without competing for resources.

Inference and training nodes run in parallel across a distributed cluster. Raw data is streamed from the inference process directly to the training aggregator, eliminating the need for data storage. Hidden states flow through CUDA-IPC double buffering into pageable memory via mmap, keeping memory overhead minimal. The architecture scales horizontally across both data-parallel and context-parallel dimensions, so draft model training happens continuously alongside live inference without competing for resources.### Optimizing the inference path: GPU execution, memory, and networking

We built the training pipeline natively within the [Baseten Inference Stack](https://www.baseten.co/resources/guide/the-baseten-inference-stack/) as part of our [Speculation Engine](https://www.baseten.co/resources/guide/the-baseten-inference-stack/#baseten-speculation-engine), so it runs directly on top of the same highly optimized inference engine that powers our serving path. This was essential, since the system needed to continuously extract training data without slowing down inference. The training pipeline is fully compatible with our existing performance features, including single-CUDA graphs and the overlap scheduler.

To avoid latency spikes during inference, we offload all network communication and data buffering to a dedicated background process. Paired with careful CUDA event synchronization on the overlap scheduler loop, this allows us to continuously extract hidden states without stalling the main execution thread.

To save memory, the inference side sends unfiltered iteration data, which is only aggregated on the receiver side. The added space usage is proportional to `max_num_tokens_per_iter`, **not** `max_sequence_length`, which preserves valuable space for long context inference.

### Optimizing the training path

On the training side, we completely decoupled the data loaders from the core training loop. The pipeline uses `mmap`-backed arrays to buffer training data directly into paged memory.

Similar to the inference side, the added GPU and pinned memory usage is proportional to `max_num_tokens_per_iter`, which preserves valuable space for the training process. Instead of materializing full request data in device or pinned memory, the full request is assembled in pageable memory and only pinned just before it enters the training loop.

### Additional tools for infrastructure handling

We also want to highlight a few frameworks that we used in this project:

- **UCXX:**Moving large tensors between nodes requires specialized networking infrastructure. We used UCXX Python bindings to handle asynchronous RDMA transfers efficiently.
- **Trio (structured concurrency):**At the scale of tens or hundreds of nodes, hardware failures and preemptions are part of normal operation. We used- [Trio](https://github.com/python-trio/trio)to build retry and recovery paths that contain those failures, preventing a few dropped nodes or transient network failures from disrupting inference. Furthermore, we integrated Trio's guest loop mode with PyTorch synchronization points such as- `torch.cuda.synchronize()`to run an async loop without creating new threads, thereby minimizing GIL contention.

If you want to leverage live draft model training for your inference workloads, [reach out](https://www.baseten.co/talk-to-us/) to talk to our engineers.
