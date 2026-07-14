---
title: How we made the fastest GPT-OSS on NVIDIA GPUs 60% faster
topic: inference
subtopic: optimization
secondary_topics: []
summary: Explains optimization work that made GPT-OSS inference faster on NVIDIA GPUs.
source: baseten
url: https://www.baseten.co/blog/how-we-made-the-fastest-gpt-oss-on-nvidia-gpus-60-percent-faster/
author: Tri Dao; Abu Qader; Philip Kiely
published: '2025-10-24'
fetched: '2026-07-11T04:07:00Z'
classifier: codex
taxonomy_rev: 1
words: 1244
content_sha256: 482b762fe0a216a9af8f3d9dee0812bdbfe676d5369f720304910ac5ef33f350
triage: keep
skip_reason: null
---

# How we made the fastest GPT-OSS on NVIDIA GPUs 60% faster

![650+ TPS on GPT OSS 120B](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1761317999-gpt-oss2.png%3Fauto%3Dformat%26fit%3Dcrop%26h%3D630%26w%3D1200&w=3840&q=100)

Using EAGLE 3 speculative decoding, we were able to achieve an uplift from ~400 to ~650 tokens per second on GPT-OSS 120B as verified by Artificial Analysis. On top of our existing work with TensorRT-LLM and NVIDIA Dynamo, reinforces Baseten’s lead as the fastest NVIDIA-based provider of GPT-OSS 120B, now rivaling custom hardware providers on speed.

As a [launch partner](https://openai.com/index/introducing-gpt-oss/) on the GPT-OSS release, we created the world’s fastest inference API for OpenAI’s 120B flagship open-source model on day zero.

In the 10 weeks since that launch, we’ve improved our performance by at least 60% and had our API [independently benchmarked by Artificial Analysis](https://artificialanalysis.ai/models/gpt-oss-120b/providers), which ranks us as the fastest NVIDIA-based API on the market.

![Artificial Analysis ranks Baseten as the fastest NVIDIA-based provider at 650+ TPS](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1761322126-image-10-24-25-at-9-05-am.jpeg%3Fauto%3Dformat%26w%3D1200&w=3840&q=75) Artificial Analysis ranks Baseten as the fastest NVIDIA-based provider at 650+ TPS

Artificial Analysis ranks Baseten as the fastest NVIDIA-based provider at 650+ TPSThis update on our model performance work on GPT-OSS 120B covers:

- The performance improvements we’ve been able to achieve and the work that we have left to do.
- Why you should be skeptical about benchmarks and how to validate them.
- The performance at scale of NVIDIA GPUs versus the straight-line speed of custom hardware providers.

[Try our GPT-OSS 120B API for yourself](https://www.baseten.co/library/gpt-oss-120b/) and let us know what you think of the performance.

### Baseline performance engineering

On launch day, we leveraged the [Baseten Inference Stack](https://www.baseten.co/resources/guide/the-baseten-inference-stack/) to build a [day zero leading API](https://www.baseten.co/blog/sota-performance-for-gpt-oss-120b-on-nvidia-gpus/) for GPT-OSS.

Our main tools and optimizations were:

- **Blackwell GPUs:**We run GPT-OSS 120B on the most powerful NVIDIA hardware generally available on the market today: B200 GPUs
- **TensorRT-LLM:**Our inference engine of choice for many workloads is TensorRT-LLM, which provides everything from optimized kernels to in-flight batching.
- **NVIDIA Dynamo:**Baseten is- [an early adopter of NVIDIA Dynamo](https://www.baseten.co/blog/how-baseten-achieved-2x-faster-inference-with-nvidia-dynamo/)for our Model APIs, including GPT-OSS 120B.
- **Tensor Parallelism:**While GPT-OSS is a Mixture of Experts model, we run with TP8 EP1 across 8 B200 GPUs as this configuration yields the lowest latency.
- **KV-aware routing:**Using NVIDIA Dynamo, we route incoming requests to instances where the KV cache has a prefix match that can be re-used to shorten TTFT.

While 400-500 tokens per second was leading performance at launch, today it would be middle of the pack. With over a dozen inference providers competing for the best GPT-OSS 120B inference, we needed to continuously improve our implementation to stay ahead.

### 60% higher tokens per second with EAGLE-3

We experimented with several techniques for speculative decoding on GPT-OSS 120B, and ultimately found [EAGLE-3](https://arxiv.org/abs/2503.01840) to be the most performant for general-purpose use.

[Speculative decoding](https://www.baseten.co/blog/a-quick-introduction-to-speculative-decoding/) is the practice of generating draft tokens to accelerate LLM decode. Each pass through the target model to generate a token is slow and memory-bound, so if we can use spare compute to run a draft model and generate potential tokens, it makes inference faster.

![Speculative decoding accelerates inference by generating multiple tokens per forward pass](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1754532511-specdecnew.png%3Fauto%3Dformat%26w%3D1200&w=3840&q=75) Speculative decoding accelerates inference by generating multiple tokens per forward pass

Speculative decoding accelerates inference by generating multiple tokens per forward passWhile traditional speculative decoding uses a smaller model from the target model’s family as a draft model, EAGLE-3 works by training a draft model specifically for speculative decoding.

EAGLE-3 is faster than an ordinary draft model thanks to its:

- **Size:**EAGLE models are ~1B parameters.
- **Accuracy:**EAGLE models are trained to use the hidden states of the target model as input, massively increasing draft token acceptance rate.

Running the 120B GPT-OSS model on 8xB200 GPUs, there is tons of headroom for techniques like speculative decoding, even at the reasonably large batch sizes needed for cost-effective high-throughput inference. However, orchestrating the EAGLE draft model and the main target model is complex, requiring updates to the TensorRT-LLM engine configuration to ensure seamless co-existence.

### What we’re not doing (yet)

There are some model performance techniques we are not (yet) using for GPT-OSS:

- **Quantization:**GPT-OSS 120B was released in a MXFP4 data format, meaning that additional post-training quantization is not a relevant optimization.
- **PD disaggregation:**NVIDIA Dynamo supports disaggregating prefill and decode onto separate worker nodes, which we are actively investigating.
- **Advanced speculation:**Beyond EAGLE, there are additional speculation techniques that we’re testing for even more performance gains.

We expect to continue to run GPT-OSS in its native quantization, but will be working on even further speed improvements with PD disaggregation and advanced speculation. Every new technique has a multiplicative effect, extending our leading performance.

### NVIDIA GPUs vs custom hardware

One common question when looking at performance benchmarks is how NVIDIA-based inference providers like Baseten compare to custom hardware companies that create their own GPU alternatives.

NVIDIA GPUs are high-performance accelerators manufactured by the millions and [available on hyperscalers and NCPs worldwide](https://www.baseten.co/blog/how-we-built-multi-cloud-capacity-management/). They combine scale and flexibility with speed and efficiency as the clear market leader in inference hardware.

However, many alternatives provide truly incredible benchmark performance. By leveraging unique architectures, custom hardware inference providers can achieve fantastic TPS numbers. But engineering is about making tradeoffs, and this performance comes with limitations like capacity constraints and limited input/output sequence lengths.

Today’s GPT-OSS benchmark shows Baseten matching or exceeding several custom hardware inference providers while serving models on generally available NVIDIA GPUs with full context window. Whether you’re serving high-volume traffic or custom models like [fine-tuned GPT-OSS 120B](https://www.baseten.co/blog/how-to-fine-tune-gpt-oss-120b-with-baseten-and-axolotl/), Baseten provides the performance, flexibility, and scale you need in production.

### Performance in production on OpenRouter

Benchmarking latency and throughput for LLM inference is an intricate exercise. Everything from input and output sequence length to inference server load to the exact contents of a request affect its real-world performance.

The two independent benchmarks we have for GPT-OSS 120B performance are:

- **Artificial Analysis:**an independent performance benchmark designed to measure realistic performance for model APIs. Artificial analysis sends consistent requests to each benchmarked API and reports the results.
- **OpenRouter:**a third-party router for inference providers that reports observed performance from real time real-world traffic for their user base.

For the top providers of GPT-OSS, OpenRouter shows varied results versus Artificial Analysis. Depending on the exact nature of the traffic that a given provider is getting at a given time, speeds can be better or worse than Artificial Analysis’ benchmark.

At the time of writing, Baseten’s GPT-OSS API was the [highest-performing option on OpenRouter](https://openrouter.ai/openai/gpt-oss-120b) on both TTFT and TPS, even beating custom hardware providers on real production workloads.

![OpenRouter performance for top providers of GPT-OSS 120B, 7:30 PT 10/24.](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1761322157-image1.png%3Fauto%3Dformat%26w%3D1200&w=3840&q=75) OpenRouter performance for top providers of GPT-OSS 120B, 7:30 PT 10/24.

OpenRouter performance for top providers of GPT-OSS 120B, 7:30 PT 10/24.Both Artificial Analysis and OpenRouter provide useful and accurate benchmark data, just with different inputs and conditions. Ultimately, the best performance benchmark for any model is testing it against your real-world use case, ideally by shadowing production traffic.

### GPT-OSS 120B in production

At Baseten, we specialize in taking cutting-edge research techniques and applying them in production. We’ll continue to push the envelope on performance for open-source models on our model APIs as well as our customers’ fine-tuned and custom foundation models. If this kind of performance engineering work is exciting to you, we are [hiring for our model performance team](https://www.baseten.co/resources/careers/).

You can try our [GPT OSS 120B model API](https://www.baseten.co/library/gpt-oss-120b/) to experience 600+ tokens per second with ultra-low TTFT for yourself, or [get in touch with us](https://www.baseten.co/talk-to-us/) if there’s another model that you want to run at state-of-the-art speed on NVIDIA GPUs.
