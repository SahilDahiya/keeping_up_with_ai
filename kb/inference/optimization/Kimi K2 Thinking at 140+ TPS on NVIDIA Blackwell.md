---
title: Kimi K2 Thinking at 140+ TPS on NVIDIA Blackwell
topic: inference
subtopic: optimization
secondary_topics:
- models/reasoning
summary: Explains Kimi K2 Thinking serving at high throughput on NVIDIA Blackwell
  hardware.
source: baseten
url: https://www.baseten.co/blog/kimi-k2-thinking-at-140-tps-on-nvidia-blackwell/
author: Abu Qader; Tri Dao; Philip Kiely
published: '2025-11-12'
fetched: '2026-07-11T04:06:50Z'
classifier: codex
taxonomy_rev: 1
words: 1714
content_sha256: 72e8e3ac86e4fe29b480261f8610f1bb6f1b8581c110adcc68add7c7fd4da4c8
triage: keep
skip_reason: null
---

# Kimi K2 Thinking at 140+ TPS on NVIDIA Blackwell

![Kimi K2 Thinking 140+ TPS](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1762914952-kimi-k2-thinking.png%3Fauto%3Dformat%26fit%3Dcrop%26h%3D630%26w%3D1200&w=3840&q=100)

We launched our [Model API for Kimi K2 Thinking](https://www.baseten.co/library/kimi-k2-thinking/) and are the best-performing provider on [Artificial Analysis](https://artificialanalysis.ai/models/kimi-k2-thinking/providers) with a 300 millisecond time to first token and 140+ tokens per second.

This blog post details the model performance work we did to get there. Using the Baseten Inference Stack, we run Kimi K2 Thinking on a single 8xB200 node in NVFP4 with a mixture of Tensor Parallelism and Expert Parallelism plus KV-aware routing for high hit rates on KV cache re-use.

Today, we launched a [Model API for Kimi K2 Thinking](https://www.baseten.co/library/kimi-k2-thinking/) and achieved state of the art latency as measured by [Artificial Analysis](https://artificialanalysis.ai/models/kimi-k2-thinking/providers).

![Baseten runs Kimi K2 Thinking with the lowest latency per independent benchmarks from Artificial Analysis](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1762915990-image-11-10-25-at-5-04-pm-1.jpeg%3Fauto%3Dformat%26w%3D1200&w=3840&q=75) Baseten runs Kimi K2 Thinking with the lowest latency per independent benchmarks from Artificial Analysis

Baseten runs Kimi K2 Thinking with the lowest latency per independent benchmarks from Artificial AnalysisKimi K2 Thinking is the smartest open-source model ever. With benchmark scores competitive with models like GPT-5 and Claude Sonnet 4.5, the new Kimi model is useful for everything from agents to coding to creative writing.

![Kimi K2 Thinking eliminated the intelligence gap between closed and open-source models (image from Artificial Analysis).](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1762915563-image2.png%3Fauto%3Dformat%26w%3D1200&w=3840&q=75) Kimi K2 Thinking eliminated the intelligence gap between closed and open-source models (image from Artificial Analysis).

Kimi K2 Thinking eliminated the intelligence gap between closed and open-source models (image from Artificial Analysis).While it’s just as smart as leading closed models, Kimi K2 Thinking is faster and cheaper. With the [Baseten Inference Stack](https://www.baseten.co/resources/guide/the-baseten-inference-stack/), Kimi K2 Thinking is faster than ChatGPT on GPT-5 with Thinking end-to-end on the same prompt.

![Kimi K2 Thinking is faster than GPT-5 with Thinking enabled and you get to see the reasoning trace.](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fimage.mux.com%2Fz01Ps0200RepgPKW3kCnzUM3dOvn1TrQu100%2Fthumbnail.jpg&w=3840&q=75)

Building this high-performance inference service for Kimi K2 Thinking was not easy. At one trillion parameters, Kimi K2 is the largest family of open-source models. Fortunately, Kimi K2 Thinking has a similar architecture to other Kimi K2 models, which is a variant of DeepSeek V3. Accordingly, we were able to re-use a good deal of the performance work we did for the predecessor Kimi and DeepSeek APIs.

To run build a high-performance API for Kimi K2 Thinking, we used our [Baseten Inference Stack](https://www.baseten.co/resources/guide/the-baseten-inference-stack/) to provide:

- Robust support for inference on NVIDIA Blackwell B200 GPUs
- NVFP4 quantization for model weights (versus original INT4 quantization)
- A low-latency parallelism configuration within our inference engine
- KV cache-aware request routing for high KV cache re-use rates

This post details the technical work required to get these running together in production.

## NVIDIA Blackwell compatibility with INT4 to NVFP4 conversion

To achieve speeds of over 100 tokens per second, we need to use the most powerful GPU architecture available: NVIDIA Blackwell. With eight B200 GPUs, we can comfortably fit the trillion-parameter Kimi model in a four-bit number format with plenty of memory left over for the KV cache.

However, Kimi K2 Thinking is optimized for previous-generation Hopper GPUs. Blackwell GPUs are not available in China due to export restrictions, so labs like Moonshot AI (the makers of Kimi) target Hopper instead.

This is most evident in the model’s native INT4 quantization. Ordinarily, INT4 is not suitable for production use. However, Kimi K2 Thinking was created using [quantization-aware training](https://developer.nvidia.com/blog/fine-tuning-gpt-oss-for-accuracy-and-performance-with-quantization-aware-training/) during the post training phase, which computes the scales and trains the weights together to ensure that the final converged weights are already quantized.

To use NVIDIA Blackwell GPUs, we need a different 4-bit data format: NVFP4. NVFP4 is a new microscaling data format with excellent performance and accuracy on Blackwell GPUs.

![Floating point data formats use sign, exponent, and mantissa bits, while integers use sign and value bits.](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1762915762-chartas.png%3Fauto%3Dformat%26w%3D1200&w=3840&q=75) Floating point data formats use sign, exponent, and mantissa bits, while integers use sign and value bits.

Floating point data formats use sign, exponent, and mantissa bits, while integers use sign and value bits.There isn’t much prior art on converting weights from INT4 to NVFP4 directly. Instead, we made a round trip through BF16, first de-quantizing the weights to 16 bits, then running our ordinary quantization script to get back down to 4 bits in NVFP4.

The first step, dequantizing from INT4 to BF16, uses the [compressed-tensors](https://github.com/vllm-project/compressed-tensors) library to apply scale factors and convert weights from 4-bit integers to 16-bit floating-point numbers. This is a long and compute-intensive process which takes a few hours (you can skip it by using third-party BF16 weights like [this release from the team at Unsloth](https://huggingface.co/unsloth/Kimi-K2-Thinking-BF16)).

From BF16, we were able to follow our ordinary process of converting BF16 to NVFP4 using [NVIDIA TensorRT Model Optimizer](https://github.com/NVIDIA/TensorRT-Model-Optimizer). We [use NVFP4 versus other 4-bit formats](https://www.youtube.com/watch?v=9_v-HBLHfFk) thanks to its increased precision from a dual scale factor and its deep support in Blackwell Tensor Cores.

While NVFP4 is overall a more precise data format than INT4, switching does not enhance quality as the INT4 quantization was performed during training. There is no way to recover the information that was lost to compression during training.

## Higher TPS with Tensor Parallelism

Once we had the weights in a usable data format, we configured our proprietary inference engine to run the model on a full 8xB200 node.

Using all eight of these GPUs effectively requires model parallelism. The model is split across the GPUs, which then communicate with each other over NVLink and NVSwitch interconnects during inference. NVLink, while high bandwidth, is slower than VRAM, so parallelism strategies should minimize the amount of GPU-to-GPU communication required.

There are three parallelism strategies to consider for a model like Kimi K2 Thinking:

- **Pipeline Parallelism (PP):**Splits a model's layers across multiple GPUs, creating a sequential pipeline where each GPU processes its layers before passing the active request to the next GPU.
- **Tensor Parallelism (TP):**Shards individual tensors and their operations within layers across multiple GPUs, enabling parallel execution of large matrix computations for a single layer.
- **Expert Parallelism (EP):**Distributes whole experts for MoE models into each GPU, where each GPU contains multiple experts.

The Baseten Inference Stack supports all of these forms of parallelism (and several more), as well as mixing and matching parallelism strategies within a single engine.

![The Baseten Runtime blends tensor parallelism and expert parallelism along with other parallelism techniques to serve large models efficiently](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1756261963-diagram-3-4.png%3Fauto%3Dformat%26w%3D1200&w=3840&q=75) The Baseten Runtime blends tensor parallelism and expert parallelism along with other parallelism techniques to serve large models efficiently

The Baseten Runtime blends tensor parallelism and expert parallelism along with other parallelism techniques to serve large models efficientlyGiven the size of Kimi K2 Thinking, some inference setups would require [multi-node inference](https://www.baseten.co/blog/how-multi-node-inference-works-llms-deepseek-r1/), or more than 8 GPUs. These setups use PP and/or EP across nodes to maximize throughput and to send less data across relatively InfiniBand node-to-node connections, which are much lower bandwidth than NVLink.

As we’re operating within a single node of B200 GPUs with fast NVLink and NVSwitch interconnect, we configured our model APIs to use a mixture of TP and EP to achieve a more optimal balance between latency and throughput.

## Lower TTFT with KV cache re-use

Thinking models like Kimi K2 are built for the most difficult tasks in AI – code generation, agentic tool use, and processing long-context queries. With 1T parameters, prefill on Kimi K2 Thinking is expensive, so KV cache re-use is a key tactic for achieving our industry-best TTFT of 300 milliseconds.

![Baseten has the lowest time to first token as measured by Artificial Analysis](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1762915912-image-36.png%3Fauto%3Dformat%26w%3D1200&w=3840&q=75) Baseten has the lowest time to first token as measured by Artificial Analysis

Baseten has the lowest time to first token as measured by Artificial AnalysisThese use cases lend themselves to repeat requests with the same context. For example, an agentic framework making 200 consecutive tool calls (an advertised capability of this model) would re-send the same data and same context with every request, or a coding assistant might ask multiple questions of the same codebase.

In these cases, the KV cache – a set of keys and values generated during inference to cache the results of the attention equation – can be re-used from request to request. Re-using the KV cache dramatically improves the time to first token as it lets the inference engine skip some or all of the prefill stage where the model builds the KV cache for the first time.

To accommodate the high traffic to our model APIs, we use multiple replicas of the model to serve users. But this KV cache re-use technique only works if the request lands on a replica that has a match in its cache for the contents of the request.

![Description: KV-aware routing sends requests to replicas that already have relevant context cached, saving time by avoiding redundant prefill computation.](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1763057468-kvroutingchart.png%3Fauto%3Dformat%26w%3D1200&w=3840&q=75) KV-aware routing sends requests to replicas that already have relevant context cached, saving time by avoiding redundant prefill computation.

KV-aware routing sends requests to replicas that already have relevant context cached, saving time by avoiding redundant prefill computation.As part of the Baseten Inference Stack, we’ve worked closely with NVIDIA engineers as early adopters of tools from [NVIDIA Dynamo](https://www.baseten.co/blog/how-baseten-achieved-2x-faster-inference-with-nvidia-dynamo/) for orchestration, including KV-aware request routing. This method improves upon traditional round-robin or load-only routing by sending requests to replicas that have prefix matches already stored in their KV cache.

With KV-aware routing, we see high cache hit rates, which helps with both benchmark performance and, more importantly, observed performance for end users with common use cases like agentic tool use, code generation, and multi-turn long-context chat.

## Kimi K2 Thinking in production

Getting a model live in production is the first step, not the finish line. After we launched our [best-in-class inference endpoint for GPT OSS](https://www.baseten.co/blog/sota-performance-for-gpt-oss-120b-on-nvidia-gpus/), we followed it up with [substantial performance improvements](https://www.baseten.co/blog/how-we-made-the-fastest-gpt-oss-on-nvidia-gpus-60-percent-faster/). We plan to do the same with Kimi K2 Thinking, starting with adding speculation and rolling out some improvements to our overall inference stack.

After getting this high-performance API up to test, we’ll add a few features to the model to add its functionality including structured outputs and thinking block parsing. And with this deployment, we’ll also keep a close eye on quality, including [tool calling performance](https://www.baseten.co/blog/tool-calling-in-inference/). Each model has its own nuances, and Kimi K2 Thinking promises to be a fantastic model when served accurately, reliably, and performantly.

Deploy [Kimi K2 Thinking on our Model APIs](https://www.baseten.co/library/kimi-k2-thinking/) to get started building with industry-best speed and capacity today.
