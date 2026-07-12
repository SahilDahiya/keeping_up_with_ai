---
title: Day zero benchmarks for Qwen 3 with SGLang on Baseten
topic: models
subtopic: benchmarks
secondary_topics:
- inference/serving
summary: Provides day-zero Qwen 3 benchmarks with SGLang and discusses serving-performance
  implications.
source: baseten
url: https://www.baseten.co/blog/day-zero-benchmarks-for-qwen-3-with-sglang-on-baseten/
author: Yineng Zhang; Michael Feil; Philip Kiely
published: '2025-04-29'
fetched: '2026-07-11T04:08:11Z'
classifier: codex
taxonomy_rev: 1
words: 1406
content_sha256: f7a1f9d92abfb3571b20b455450579b45e32ba860b365d2908a82c23a602de15
triage: keep
skip_reason: null
---

# Day zero benchmarks for Qwen 3 with SGLang on Baseten

![Qwen + SGLang](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1747688555-qwen-3.png%3Fauto%3Dformat%26fit%3Dcrop%26h%3D630%26w%3D1200&w=3840&q=100)

Qwen 3, a new family of open-source LLMs by Alibaba, introduces Qwen 3 235B, a state-of-the-art reasoning model that rivals DeepSeek-R1 but requires a quarter of the hardware resources to run in production. Using SGLang, an open source fast inference framework, we were able to optimize and deploy Qwen 3 in production for customers within minutes of the weights dropping on Hugging Face.

[Qwen 3](https://qwenlm.github.io/blog/qwen3/) introduced eight new open-source LLMs, including Qwen 3 235B, a state-of-the-art reasoning model that requires only 4 H100 GPUs for inference. That’s a quarter of the hardware needed for DeepSeek-R1, making Qwen 3 235B a highly cost-efficient reasoning model.

[Qwen 3 235B](https://www.baseten.co/library/qwen-3-235b/) is useful for everything from agentic workflows to reasoning chat to code generation, while the [smaller models](https://www.baseten.co/library/qwen-3-32b/) in the family are great when workloads need to be fast and inexpensive, like code completion. Qwen 3 compares favorably on public benchmarks with models like OpenAI-o1 and OpenAI-o3-mini while staying competitive with much larger frontier models like DeepSeek-R1 and Gemini 2.5 Pro. When we spot-checked our implementation with the `gsm8k` benchmark, we found that Qwen 3 scored within a margin of error of DeepSeek-R1.

![Alibaba published benchmark results for Qwen showing competitive performance vs much larger leading models](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1747688724-qwen3-235a22-1.jpg%3Fauto%3Dformat%26w%3D1200&w=3840&q=75) Alibaba published benchmark results for Qwen showing competitive performance vs much larger leading models

Alibaba published benchmark results for Qwen showing competitive performance vs much larger leading modelsTo take full advantage of the model’s efficient performance in production, we need to serve the model with low latency and high throughput. That’s where [SGLang](https://github.com/sgl-project/sglang), an open-source fast inference framework for LLMs, comes in. SGLang core maintainers worked closely with Qwen engineers to ensure day-zero support for the new family of models.

With SGLang, we were able to get production-ready performance the moment the Qwen 3 model weights were made public. However, as with any new model, there is plenty of support to add to improve performance even further.

In this piece, we’ll outline the architecture of the newest Qwen models, day zero performance benchmarks with SGLang, tips for running Qwen effectively, and avenues for future improvement to performance.

## Qwen 3 Mixture of Experts architecture

Qwen 3 235B uses a Mixture of Experts (MoE) architecture with 128 experts and 8 experts per token for a total of 22 billion active parameters per token. To serve this model across multiple GPUs, we use different sharding strategies for the attention layer and sparse MoE layer:

- **Attention**runs with Tensor Parallelism (TP) across available GPUs.- Qwen 3 uses GQA attention, which is like Llama 3 but unlike DeepSeek-V3/R1.
- We can re-use all of the serving optimizations originally developed for Llama 3.
- The QKV weights and outputs are shared across all GPUs, while computation is distributed on a per-KV-head basis.

- **Sparse MoE**runs with Expert Parallelism (EP) across all available GPUs.- Qwen 3 closely follows the DeepSeek-V3/R1 router-expert design.
- Experts are partitioned along the expert dimension for efficiency, resulting in 16 experts per GPU in TP8 or 32 per GPU in TP4.
- The routing layer is small and is replicated across each GPU to minimize communication overhead – recomputation is cheaper than communication here even under heavy load.


SGLang automatically splits the model appropriately using the `--tp` argument to specify the number of GPUs to use for inference.

![Qwen 3 235B runs with a mixture of tensor parallelism and expert parallelism strategies](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1747688696-image1.png%3Fauto%3Dformat%26w%3D1200&w=3840&q=75) Qwen 3 235B runs with a mixture of tensor parallelism and expert parallelism strategies

Qwen 3 235B runs with a mixture of tensor parallelism and expert parallelism strategiesAt launch, Qwen 3 235B was available in both FP8 and BF16 precisions. For Hopper GPUs like the H100, each precision supported one parallel serving strategy:

- FP8, the quantized version, is served in TP4 across four GPUs
- BF16 is served in TP8 across a full node of eight GPUs as shown in the diagram above

We generally recommend running in FP8 as it offers nearly identical quality at a much lower cost. SGLang also has [a TP8 implementation for the FP8 quantized model](https://github.com/sgl-project/sglang/pull/5917), offering even better performance by doubling the hardware used.

## Qwen 3 performance benchmarks

On day zero, Qwen 3 235B achieves very usable performance with SGLang. Future optimizations like Blackwell support, speculative decoding, and TP8 for FP8 quantization will unlock even further gains.

Qwen 3 performance benchmarks depend materially on batch size. Smaller batches reduce latency but increase the effective cost per token by lowering throughput. Alternatively, high concurrency is great for low-cost latency-insensitive batch workloads.

![SGLang benchmarks for Qwen 3 235B, batch size 32, 04/29/2025](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1747688664-group-2085661061.png%3Fauto%3Dformat%26w%3D1200&w=3840&q=75) SGLang benchmarks for Qwen 3 235B, batch size 32, 04/29/2025

SGLang benchmarks for Qwen 3 235B, batch size 32, 04/29/2025With a batch size of 32, which balances latency with throughput, we observed:

- ~250 milliseconds median time-to-first token
- ~45 tokens per second per user
- ~1,400 tokens per second total throughput, including prefill

For requests with 1,000 input and output tokens on H200 GPUs. By going down to a batch size of 1, you can improve latency to ~75 tokens per second per user, or you can triple throughput to ~4,600 total tokens per second with a batch size of 384.

Another major factor in how well the model performs on variable production traffic is how quickly new replicas can be scaled up to handle traffic spikes. For Qwen 3, which is well over 200 gigabytes of files even in FP8, we used our in-house cold start optimizations to cut model weight load times by nearly 50%.

![With cold start optimizations, Qwen 3 weights load in 230 seconds vs 435 seconds](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1747688608-output-12.png%3Fauto%3Dformat%26w%3D1200&w=3840&q=75) With cold start optimizations, Qwen 3 weights load in 230 seconds vs 435 seconds

With cold start optimizations, Qwen 3 weights load in 230 seconds vs 435 secondsWe’re working on even more improvements to our cold starts, which we’re excited to share more about soon.

## Qwen 3 inference tips and tricks

Regardless of how you run Qwen, there are a few tips that improve performance and output quality.

### Vary temperature between thinking modes

Qwen 3 is a “hybrid thinking” model, meaning that reasoning can be turned on and off on a request-by-request basis. By default, Qwen 3 enables reasoning to match DeepSeek-R1 and OpenAI’s o-series models.

When using each mode, Qwen’s authors recommend slightly adjusting parameters like temperature for best results.

Additionally, they warn against using greedy decoding in reasoning mode as it can lead to worse performance and endless repetition.

### Take advantage of agentic capabilities

Qwen 3 is a great choice for building agents thanks to its advanced tool-calling capabilities. As one of the first foundation models released in the MCP era, Qwen 3 offers strong support for MCP-style tools as well as ordinary function calling.

With SGLang, you get full support for agentic capabilities via function calling using the OpenAI client SDK in any language.

### Use the entire context window

With a 32K-token context window (up to 128K with sliding attention), Qwen 3 does not attempt to meet recent models like Llama 4 Scout on ultra-long context window claims. However, the Qwen team emphasized the usability of their context window, both for parsing detailed inputs and generating long output reasoning sequences.

For reasoning inference, it’s recommended to set the output `max_tokens` to the full 32,768 tokens even if you don’t expect to need that many as it gives the model space to think.

## Qwen 3 in production

Qwen 3 235B proves you don’t need a massive budget to unlock frontier performance in reasoning. Together with the smaller models, Qwen 3 is useful for everything from agents and chat to code generation and completion and stays competitive with much larger models on benchmarks. And with SGLang, it was ready for production from the moment the weights hit Hugging Face.

However, there’s a lot more coming to make Qwen 3 faster. Adding support for Blackwell GPUs like the B200, as well as TP8 support for the quantized model, will accelerate inference by effectively leveraging substantially more hardware resources. Further optimizations like speculative decoding are possible thanks to the numerous small models in the Qwen family. And both the core maintainers and the broader community are working on improving SGLang’s base performance and support for new research.

You can get started building with Qwen 3 today with ready-to-use deployments of the large MoE model [Qwen 3 235B](https://www.baseten.co/library/qwen-3-235b/) or the smaller dense model [Qwen 3 32B](https://www.baseten.co/library/qwen-3-32b/).
