---
title: How to optimize LLM inference speed and reduce costs in production
kind: blog
topic: null
subtopic: null
secondary_topics: []
summary: null
triage: null
skip_reason: null
source: baseten
url: https://www.baseten.co/blog/how-to-optimize-llm-inference-speed-and-reduce-costs-in-production/
author: Chloe Florit
published: '2026-07-23'
fetched: '2026-07-23T06:49:51Z'
classifier: null
taxonomy_rev: 2
words: 2050
content_sha256: 56917e74acf8d53d721573bcd78628c508b425c78b4058f0d34ec87bec153a60
---

# How to optimize LLM inference speed and reduce costs in production

![LLM inference optimizations](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1783455244-baseten-blog-2026-thumbnails-6.png%3Fauto%3Dformat%26fit%3Dcrop%26h%3D630%26w%3D1200&w=3840&q=100)

LLM inference costs too much and responds too slowly when GPUs sit idle, repeat work, and move too much data. This post covers some of the most popular techniques to optimize inference: continuous batching, speculative decoding, KV cache reuse, quantization, smarter routing, and more.

Your model isn’t slow. Your inference is. A properly optimized model will outperform a frontier model that isn’t.

[LLM inference](https://www.baseten.co/blog/llm-transformer-inference-guide/) has two main phases: prefill, when the model processes the prompt, and decode, when it generates the response one token at a time. In this post, we’ll cover techniques used to optimize both phases to improve latency, throughput, and cost when [running AI models in production](https://www.baseten.co/products/dedicated-inference/).

**1. Continuous batching **

A batch is a group of requests processed together on the GPU at the same time. Batching matters because GPUs are built to handle multiple computations from different requests in parallel.

During one decode iteration, the GPU generates one token for every active request in the batch. The problem with traditional batching is that the server waits for every request in the batch to finish before accepting new ones. You can’t add requests mid-batch.

[Continuous batching](https://www.baseten.co/blog/continuous-vs-dynamic-batching-for-ai-inference/) fixes this. At each iteration, the GPU processes all active requests together. When a new request arrives, the GPU generates new tokens for each request with no wait time. 

- Iterations 1-20: GPU processes requests [A,B]. Each request gets one token per iteration. 
- Iteration 21: Request C joins. GPU processes [A, B, C]. 

The result is faster response times and reduced queuing latency.

**2. Speculative decoding **

During the decode step, tokens are typically generated one by one. [Speculative decoding](https://www.baseten.co/blog/a-quick-introduction-to-speculative-decoding/) lets you generate multiple candidate tokens in advance with a smaller model and then verifies them all in a single pass of the main, larger model. Verification is cheaper than generation because the target model can verify all of the draft tokens in parallel. If the target model generated those same tokens itself, it would have to do so sequentially, one token at a time. 

If most of the draft tokens are accepted, the system produces multiple tokens for a single target-model pass, which reduces latency and increases throughput (tokens per second).

Here are the main speculative decoding techniques:

**Draft-target speculative decoding** 

Draft-target speculative decoding** **is when a smaller draft model “guesses” several tokens ahead and a full target model then verifies those guesses. Correct guesses are accepted in order. When the target model disagrees with a guess, it replaces that token with its own choice, discards the remaining draft tokens, and the draft model starts guessing again from there.

![Draft-target speculative decoding](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1783454257-1752685208-diagram-1-2.webp%3Fauto%3Dformat%26w%3D1200&w=3840&q=75) Draft-target speculative decoding

Draft-target speculative decoding**Medusa**

Medusa adds several prediction heads on top of the LLM. Each head independently predicts a future token position, such as token +1, token +2, or token +3. Then the full transformer verifies all guesses at once. The added heads are lightweight because they are simple linear projections: they take the model’s hidden state (the model’s internal representation of the latest token and the context before it) and apply a learned matrix multiplication to produce token predictions. They don’t include the attention, memory, or multi-step reasoning of full transformer layers.

**EAGLE-3**

EAGLE-3 is a small 1-2 layer transformer that you add on top of the LLM. It cheaply drafts several tokens ahead. Unlike Medusa, EAGLE’s small transformers generate tokens one at a time, so its drafts are more coherent and accurate. EAGLE-3 is still much cheaper than running the full model because its draft module has far fewer layers than the target LLM.

**N-gram speculation**

N-gram speculation is a lightweight speculative decoding technique that speeds up generation by reusing repeated patterns from the prompt or prior output. Instead of using a separate draft model, it checks whether the tokens being generated match a sequence that appeared earlier. If so, it proposes the tokens that followed that earlier sequence. The target model verifies the guess, keeps the matching tokens, and discards the rest. It works best for repetitive or structured outputs like code, JSON, templates, or repeated phrasing, and is less useful for open-ended reasoning or explanations.

Speculative decoding works best at low batch sizes because there's spare compute. At large batch sizes, the GPU is already busy serving all the requests, so there's no spare compute (tensor cores) and speculation would have to fight for that same compute (to run the draft model and verify multiple tokens per request), which can hurt throughput.

**3. KV cache optimizations**

“Keys” help the model figure out which words to pay attention to, and “values” determine what information gets added to a word's meaning based on the context. Together, they are cached as the “KV cache”.

- **KV cache-aware routing**: automatically routes requests to replicas* that have the necessary context cached, which eliminates redundant prefill compute. This is especially useful for shared prompts, like system messages or few-shot examples.- [NVIDIA Dynamo](https://www.baseten.co/blog/how-baseten-achieved-2x-faster-inference-with-nvidia-dynamo/)uses this approach natively.
- **CPU offloading**: moves unused cache blocks to CPU RAM to reduce GPU memory pressure.

*Note: A replica is an instance (copy) of a model running on one or more GPUs.*

**4. Quantization**

Quantization makes a model smaller and faster by storing its weights in a lower-precision format, which can help reduce LLM inference cost for memory-bound workloads.

Model weights are stored in VRAM (high-bandwidth memory attached to the GPU). During inference, the GPU has to move those weights from VRAM into its compute units (e.g., registers or shared memory) to perform calculations.

If you cut the weight size, you cut the bytes you must fetch by ~2x or ~4x. For example, FP16 uses 2 bytes per weight, while FP8 uses 1 byte, and FP4 uses 0.5 bytes.

A sign, mantissa, and exponent make up a floating-point number. The sign says if the number is positive or negative, the mantissa holds the actual numbers in binary, and the exponent moves the decimal point.

![Visualizing FP16, FP8, and FP4 precisions](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1783454398-llm-inference-optimizations-graph2-060726.png%3Fauto%3Dformat%26w%3D1200&w=3840&q=75) Visualizing FP16, FP8, and FP4 precisions

Visualizing FP16, FP8, and FP4 precisionsComputations are also faster because the hardware can do more matrix multiplications in parallel.

There are three main quantization methods:

**Mixed-precision quantization**

Mixed-precision quantization examines the distribution of activation values across layers to find outliers. During quantization, a few extreme activation values can widen the quantization range enough that many ordinary values get rounded to the same bucket, losing precision the model relies on. With mixed-precision quantization, layers with large activation outliers are quantized more conservatively (or left at higher precision), while more uniform layers can go to a lower precision. This preserves output quality while still cutting overall memory and compute costs.


**Rotation-based** quantization

Rotation-based quantization rotates weights and activations (and in some methods, the [KV cache](https://www.baseten.co/blog/i-spent-31-hours-on-the-math-behind-turboquant-so-you-dont-have-to/#kv-cache-the-problem)) before quantization. Rather than removing outliers, the rotation spreads the large values across many embedding dimensions instead of concentrating them in a few, which produces a smoother distribution that’s easier to quantize. 


**Curvature-based quantization**

Curvature-based** **quantization measures how sensitive each weight is to rounding error: how much a small change to that weight would affect the model’s output. Some weights can be rounded aggressively with almost no effect on accuracy. Others are highly sensitive: even a tiny rounding error meaningfully changes the model’s behavior, so those weights are quantized more carefully.

Quantization is validated against benchmarks to ensure no meaningful loss in accuracy versus the unquantized model. Baseten compares the quantized model to the full-precision baseline, and if quality drops, we adjust the quantization strategy or keep sensitive layers at higher precision.

**5. Kernel optimizations **

A kernel is a function executed on a GPU to perform many parallel computations at once. Kernels run every operation in a model, from matrix multiplications to activation functions, so kernel efficiency directly impacts throughput.

- **Kernel fusion**combines multiple operations (e.g., matrix multiplication, bias addition, activation functions) into one GPU kernel. This prevents expensive global-memory reads/writes of large intermediate tensors.
- **Attention kernels**are GPU kernels that compute the attention operation. They are specialized for specific workloads like prefill (prompt processing) vs decode (generating tokens).
- **Asynchronous compute**overlaps memory and computation: while the GPU processes one block of data, it’s already loading the next one into the fast shared memory.
- **PDL**(programmatic dependent launch) removes the CPU from kernel scheduling. Kernel A queues kernel B directly on the GPU, so the moment A finishes, B starts. No CPU round trip is required, reducing launch latency between dependent kernels

**6. Intelligent request routing **

- **Geo-aware load balancing**: sends requests to geographically close GPUs so the data doesn’t need to travel as far through multiple network hops.
- **LoRA-aware routing:**LoRAs

**7. Topology-aware parallelism **

Tensor parallelism (TP) and expert parallelism (EP) can be used during both prefill and decode to help reduce communication overhead and improve serving efficiency. TP primarily lowers latency, while EP primarily increases throughput.

**Tensor Parallelism** splits computations across multiple GPUs, then exchanges shards (slices) of the result to assemble the full output for the next layer. NVLink tightly connects the GPUs to quickly read/copy shards from other GPUs’ VRAM. 

**Expert parallelism**: in mixture-of-experts (MoE) models, the network is divided into many independent feedforward subnetworks (experts) that can be distributed across GPUs. Each input token is routed to a small number of experts, keeping compute per forward pass low. 

![Expert parallelism during prefill](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1783454650-llm-inference-optimizations-060726.png%3Fauto%3Dformat%26w%3D1200&w=3840&q=75) Expert parallelism during prefill

Expert parallelism during prefill**8. Disaggregated prefill and decode phases **

LLM inference has two phases:

- Prefill: processes the prompt and builds the initial Key-Value (KV) cache. 
- Decode: generates the answer one token at a time using the KV cache. 

Prefill and decode have different GPU needs: prefill is compute-bound, and decode is memory-bandwidth bound. When both phases run on the same GPU, a large prefill request can stall ongoing decode, which can spike latency for users.

Disaggregating prefill and decode by running each phase on separate GPUs reduces latency.

It also allows us to run different optimization settings for prefill and decode. For example, we can use tensor parallelism for prefill and data parallelism for decode. This works better than one configuration for both. In addition, some workloads are more prefill heavy or more decode heavy. Disaggregating allows us to scale prefill and decode separately.

**Which **LLM inference optimization **techniques should you choose for your workload? **

No single optimization helps lower inference cost and latency on its own. Most production systems stack several at once (quantization, speculative decoding, and KV cache reuse are a common baseline). The right combination depends on which phase is limiting you: prefill is usually compute-bound, where kernel fusion, attention kernels, and disaggregating prefill onto its own GPUs help most. Decode is usually memory-bandwidth bound, where quantization, speculative decoding, and KV cache reuse make a bigger difference.

Make sure to [measure where your bottleneck is](https://www.baseten.co/blog/ai-model-performance-metrics-explained/) before choosing the right optimization techniques. 

**FAQ **

**What is the difference between prefill and decode?**

LLM inference has two phases. Prefill processes the input prompt and builds the KV cache, while decode generates the response one token at a time using that cache. Prefill is compute-bound, whereas decode is usually limited by GPU memory bandwidth.

**Which LLM inference optimization has the biggest impact?**

There's no single best optimization, but continuous batching, KV cache reuse, quantization, and optimized attention kernels typically provide the largest performance gains with the least engineering effort. The right combination depends on your model, hardware, traffic patterns, and latency goals.

**When should you use quantization for LLM inference?  **

You should use quantization when model weights are too large, inference is memory-bandwidth constrained, or serving costs are too high. Lower-precision formats like FP8 or FP4 reduce how much data the GPU needs to move from memory, which can improve throughput and lower cost. The tradeoff is that quantization can affect model quality, so teams should benchmark latency, cost, and accuracy before deploying it in production.

**What is the difference between throughput and latency in LLM inference?  **

Latency measures how long a single request takes to return a response, while throughput measures how much work the system can complete over time, often in tokens per second. Some optimizations improve both, [but there can be tradeoffs](https://www.baseten.co/blog/ai-model-performance-metrics-explained/). For example, larger batches may increase throughput by keeping GPUs full, but they can also increase latency if requests wait too long in a queue.
