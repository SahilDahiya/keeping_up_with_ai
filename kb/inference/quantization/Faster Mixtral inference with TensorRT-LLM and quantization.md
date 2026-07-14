---
title: Faster Mixtral inference with TensorRT-LLM and quantization
topic: inference
subtopic: quantization
secondary_topics: []
summary: Shows how TensorRT-LLM and quantization improve Mixtral inference performance.
source: baseten
url: https://www.baseten.co/blog/faster-mixtral-inference-with-tensorrt-llm-and-quantization/
author: Pankaj Gupta; Timur Abishev; Philip Kiely
published: '2023-12-22'
fetched: '2026-07-11T04:10:19Z'
classifier: codex
taxonomy_rev: 1
words: 1567
content_sha256: 2252359eb1d9932742d800122b7a65eda340309f216eb6235701d7141734c8b6
triage: keep
skip_reason: null
---

# Faster Mixtral inference with TensorRT-LLM and quantization

![Faster Mixtral inference](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1747529643-mixtral.png%3Fauto%3Dformat%26fit%3Dcrop%26h%3D630%26w%3D1200&w=3840&q=100)

[Mixtral 8x7B](https://mistral.ai/news/mixtral-of-experts/) is an LLM with a mixture of experts architecture that produces results that compare favorably with Llama 2 70B and GPT-3.5 while using fewer parameters and enabling faster inference. By using TensorRT-LLM and quantizing the model to int8, we can achieve important performance milestones while using only a single A100 GPU.

In our initial exploration of Mixtral performance, we had three preliminary goals:

- Get time to first token below 200 milliseconds, an important threshold for real-time chat applications.
- Get above 50 perceived tokens per second, enough for all but the fastest readers.
- Save on cost by running the model on a single A100.

While we’re certainly going to invest more in Mixtral performance, we’ve accomplished each of those goals. On a single A100 GPU, an `int8` quantization of Mixtral on TensorRT-LLM demonstrated a 127ms time to first token and 81 perceived tokens per second in our tests. These numbers can vary substantially based on testing parameters (ours were a 512-token input sequence, 128-token output sequence, and single concurrent request).

Here’s an overview of our findings:

- Thanks to Mixtral’s mixture of experts architecture, the model uses only 12.9B parameters during inference, though all 46.7B parameters are stored in memory.
- Mixtral’s performance doesn’t scale as well for batched inference as more parameters are used.
- Using a TensorRT-LLM model server instead of the default vLLM implementation results in 2-3x improvement in tokens per second and 30% improvement in time to first token.
- Quantizing Mixtral 8x7B to - `int8`cuts inference cost in half (as only one A100 is needed) while preserving quality with only a 0.08% increase in model perplexity — using the quantized model is a no-brainer in most cases.

[Mixtral 8x7B on TRT-LLM is available now](https://www.baseten.co/library/mixtral-8x7b-instruct/) for deployment on Baseten. Just [let us know that you’re interested in the model](mailto:support@baseten.co) and we’ll get you the A100s you need to get up and running.

## Mixtral inference overview

Mixtral 8x7B is a powerful, midsize LLM. With 46.7B parameters, it matches up well against Llama 2 70B and GPT-3.5 on [common benchmarks for output quality](https://mistral.ai/news/mixtral-of-experts/).

It’s a bit surprising that Mixtral has only 46.7B parameters, not 56B. After all, 8x7B is right there in the name, and eight times seven is fifty-six. But the eight “experts” in the model share attention layers, saving some parameter count. This extra space gives more spare memory for batching, KV caches, and other inference overhead.

### Structural advantage of mixture of experts architecture

When Mixtral receives a request, the model’s router component picks two of the model’s eight experts to handle the request. While all 46.7B parameters are loaded into memory, only 12.9B are used during inference (again, not 14B as attention layers are shared).

![Each layer of inference only uses two of eight experts](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1703287796-frame-2014b.png%3Fauto%3Dformat%26w%3D1200&w=3840&q=75)

When handling a single request at a time, Mixtral’s performance is far better than larger models like Llama 2 70B because the request touches fewer weights. This improves both time to first token and tokens per second.

### Issues with batching for Mixtral inference

While the mixture of experts architecture does incredibly well for individual requests, the architecture is less advantageous for batched inference. Mixtral still performs reasonably well for batched inference, but the advantage from only loading two experts is gone.

As we outlined above, each request is handled by two experts, which requires loading 12.9B parameters. However, in a batch, there are multiple requests and it’s unlikely that the requests will each require the same experts. Instead, more of the model will be used — quite likely the full 46.7B parameters for larger batches.

With more of the model’s parameters used during batched inference, the model’s time to first token and the tokens per second of each request decrease. The overall tokens per second throughput does increase with batching, just at a worse-than-linear rate. This remains true regardless of model server engine

## Higher TPS and lower TTFT with TensorRT-LLM

Mixtral was first released using the [vLLM](https://github.com/vllm-project/vllm) inference engine. While vLLM has a number of great properties for running LLMs, we wanted to see if we could get faster performance using [TensorRT-LLM](https://github.com/NVIDIA/TensorRT-LLM), an inference engine developed by NVIDIA.

**A caveat on these numbers**:  we are not saying that TensorRT-LLM is universally better than vLLM. This section is comparing [our TensorRT-LLM implementation](https://github.com/basetenlabs/truss-examples/tree/main/mistral/mixtral-8x7b-instruct-trt-llm-weights-only-quant) to [our vLLM implementation](https://github.com/basetenlabs/truss-examples/tree/main/mistral/mixtral-8x7b-instruct-vllm), which is likely not the most optimal implementation. It's just the baseline we started with. We chose TensorRT-LLM for this project, but we use vLLM heavily and will keep an eye on all model serving engines moving forward as more optimizations are released.

For single requests, using TensorRT-LLM unlocked:

- A 2-3x increase in tokens per second
- A 30% decrease in time to first token

In our testing, we used an input sequence of 512 tokens and an output sequence of 128 tokens and only sent one request at a time (no batching). We saw, for float16 inference on two A100 GPUs:

- 341 total tokens per second with 68 output tokens per second, for a perceived tokens per second of 75 (vs 23 for default vLLM implementation).
- A 169 millisecond time to first token (vs 239 for default vLLM implementation).
- Total end-to-end latency on real prod infra of 1.869 seconds for the request (vs 5.795 for default vLLM implementation).

Of course, these numbers can vary significantly based on the testing parameters such as sequence length.

### Batch inference performance

While batched Mixtral inference can’t take full advantage of the inference speed boost from the mixture of experts architecture, it’s still a great way to improve overall throughput when latency is not as essential.

TensorRT-LLM improves batched inference performance. This benchmark was run with the same input sequence length (512 tokens) and output sequence length (128 tokens) as previous benchmarks.

Batching impacts both latency and throughput — but TensorRT gives massive performance gains on both measurements for batched inference.

![Time to first token across different batch sizes (lower is better)](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1709311928-twitter-post-18.png%3Fauto%3Dformat%26w%3D1200&w=3840&q=75) Time to first token across different batch sizes (lower is better)

Time to first token across different batch sizes (lower is better)While larger batch sizes slightly increase time to first token, they're more than worth it for the increase in total throughput.

![Total tokens per second generated by Mixtral (higher is better)](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1709311970-twitter-post-17.png%3Fauto%3Dformat%26w%3D1200&w=3840&q=75) Total tokens per second generated by Mixtral (higher is better)

Total tokens per second generated by Mixtral (higher is better)## Lower inference costs from quantizing model weights

Mixtral’s VRAM requirements in `float16` mean that inference needs two 80-gig A100 or H100 GPUs. Even though inference only runs through about 12.9 billion parameters at a time, all 46.7 billion need to be loaded into memory, requiring about 94 GB of VRAM at FP16, plus inference overhead.

However, by quantizing the model down to `int8`, we can get equal or better latency and throughput from a single A100, cutting inference cost in half.

Specifically, we’re using weights-only quantization. Model weights generally have a lower dynamic range versus other components like KV cache, meaning that quantizing them shouldn’t reduce model quality in a noticeable way. However, we want to double-check that the quantized model still works well.

### Perplexity: a check on model quality

Perplexity is a broad-strokes measurement of an LLM’s reasoning ability. There are various methods for calculating perplexity, but comparing the perplexity of two models using the same technique for each is a useful measurement of relative model quality.

![Mixtral only gains 0.08% in perplexity when quantized to int8](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1703267236-frame-2015.png%3Fauto%3Dformat%26w%3D1200&w=3840&q=75)

Unlike benchmarks focused on model output for a given input, perplexity works somewhat in reverse. Perplexity is measured by giving a model some real sentences and calculating the probability of the model producing that sentence. If the model is surprised by real sentences — as in it’s unlikely that the model would generate them — then that’s a sign that there’s something wrong with the model.

Perplexity is a useful metric for evaluating quantized models. You’re looking for the smallest possible increase in perplexity from the `float16` version to the `int8` or `int4` version to indicate successful quantizing.

Given the following perplexity scores (smaller is better):

- Mistral 7B in - `float16`: 2.0667777061462402
- Mistral 8x7B in - `float16`: 1.9466325044631958
- Mistral 8x7B in - `int8`(weights only): 1.9481830596923828

In our testing, we see that weights-only quantization to `int8` results in only an 0.08% increase in perplexity. This should have almost no impact on the real world quality of the model results and is more than worthwhile for the major decrease in model cost from running on a single A100.

## Get started with Mixtral inference

Mixtral is a powerful, fast LLM with a permissive Apache 2.0 license and a massive 32K-token context window. But using it in production requires efficient-cost effective inference. Using TensorRT-LLM and int8 quantization allows better performance on less hardware, making Mixtral suitable for a wide range of use cases. If you want to go deeper into optimizing LLM inference and batching, checkout our [guide to transformers inference](https://www.baseten.co/blog/llm-transformer-inference-guide/).

To [deploy Mixtral 8x7B on Baseten](https://www.baseten.co/library/mixtral-8x7b-instruct/), just [let us know that you’re interested in the model](mailto:support@baseten.co) and we’ll get you set up with A100s for inference. We’ve [open-sourced our optimized model server](https://github.com/basetenlabs/truss-examples/tree/main/mistral/mixtral-8x7b-instruct-trt-llm-weights-only-quant), and if you’re looking for specific performance from the model — optimizing for latency, throughput, cost, or a combination of the above — let us know your targets and we’ll help you hit them.
