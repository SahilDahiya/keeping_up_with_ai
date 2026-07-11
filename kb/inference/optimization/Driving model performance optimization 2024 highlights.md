---
title: 'Driving model performance optimization: 2024 highlights'
topic: inference
subtopic: optimization
secondary_topics:
- inference/serving
summary: Summarizes concrete model-performance optimization work across inference
  serving, batching, and hardware.
source: baseten
url: https://www.baseten.co/blog/driving-model-performance-optimization-2024-highlights/
author: Pankaj Gupta
published: '2025-01-09'
fetched: '2026-07-11T04:08:33Z'
classifier: codex
taxonomy_rev: 1
words: 1486
content_sha256: da248d33a30a5b09cb5fca3745a7383c59909422363c048a115038bdfb4d855d
triage: keep
skip_reason: null
---

# Driving model performance optimization: 2024 highlights

![MP 2024 highlights](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1747428776-model-performance-2024.png%3Fauto%3Dformat%26fit%3Dcrop%26h%3D630%26w%3D1200&w=3840&q=100)

Baseten’s **Model Performance Team** is a group of engineers dedicated to adapting cutting-edge inference optimization research and productionizing it to support high-volume real-world workloads. Our roadmap is customer-driven and focuses on:

- **Latency**: Achieving top-tier TTFT, TPOT, and other key latency metrics.
- **Scalability:**Supporting massive expansions in user volume without compromising latency or quality.
- **Quality**: Retaining or enhancing model output quality throughout the optimization process.
- **Cost**: Delivering robust inference solutions that are affordable at scale.
- **Functionality**: Supporting OpenAI-compliant specs, sampling parameters, function calling, structured output, streaming, asynchronous inference and more.
- **Ease of use**: Packaging these outcomes in developer-friendly tooling.

2024 was a critical year as we expanded the team and achieved significant breakthroughs in each of these areas. In this year in review, we’ll connect the dots on what we shipped last year and preview some things we’re excited about in 2025.

Our work includes both LLMs and models across modalities, from images to ASR to embeddings. We focus on solutions over tools and leverage the best open-source technologies but don’t hesitate to build custom solutions to meet our customers’ needs. If you’re interested in working on productionizing cutting-edge research, [visit our careers page](https://www.baseten.co/careers/) for information on open roles in the model performance team.

## Adopting TensorRT-LLM as our core framework

In 2024, we adopted [TensorRT-LLM](https://www.baseten.co/blog/high-performance-ml-inference-with-nvidia-tensorrt/), a fast inference framework from NVIDIA, as our core framework while still maintaining support for options including vLLM, TGI, and SGLang.

We began the year with experiments like [optimizing Mixtral 8x7B](https://www.baseten.co/blog/faster-mixtral-inference-with-tensorrt-llm-and-quantization/) and achieving [then-leading Mistral 7B performance](https://www.baseten.co/blog/benchmarking-fast-mistral-7b-inference/) using TensorRT-LLM. Based on these promising results, we rigorously benchmarked TensorRT-LLM against popular frameworks like vLLM and TGI.

TensorRT-LLM emerged as the clear leader in performance. It incorporated standard optimizations such as Flash Attention, paged attention, and in-flight batching with SOTA CUDA kernels. We collaborated closely with the TensorRT-LLM team to roll out advanced features like KV cache reuse and chunked prefill, setting the stage for the year ahead.

We use TensorRT-LLM at a deep level, using the C++ executor API directly and providing logits processors where necessary. We build it from source and make changes to this source when needed and contribute patches back. We often dig into TensorRT-LLM source code to figure out how things work internally. We expect to continue to go deeper in this direction. This work has led to recognition including conference talks at the [AI Engineer World’s Fair in 2024](https://www.ai.engineer/worldsfair/2024/schedule/from-model-weights-to-api-endpoint-with-tensorrt-llm) and the upcoming NVIDIA GTC in 2025.

## Leveraging NVIDIA’s Hopper architecture

While TensorRT-LLM is powerful on its own, we found it works best when combined with the Hopper GPU architecture, [most notably the H100 GPU](https://www.baseten.co/blog/unlocking-the-full-power-of-nvidia-h100-gpus-for-ml-inference-with-tensorrt/). After extensive benchmarking, we launched support for H100 GPUs in January, working closely with our infrastructure team to ensure seamless availability for our users.

H100 GPUs offer exceptional performance thanks to large and high-bandwidth onboard memory, strong compute profiles, and excellent architectural features. H100s are excellent not only for LLMs, but for models of all modalities, [including image models](https://www.baseten.co/blog/40-faster-stable-diffusion-xl-inference-with-nvidia-tensorrt/).

One major advantage of H100s is their support for [FP8 precision for post-training quantization](https://www.baseten.co/blog/33-faster-llm-inference-with-fp8-quantization/). Previous methods like SmoothQuant, AWQ, and GPTQ had quality losses that were unacceptable to customers. FP8 offered a breakthrough—delivering up to 40% improvements in TTFT, throughput, and overall performance with negligible quality loss. 

We wanted to bring these capabilities to more workloads in a cost-effective way, so we invested heavily in using H100 GPUs’ [multi-instance GPU (MIG) configurations](https://www.baseten.co/blog/using-fractional-h100-gpus-for-efficient-model-serving/). With MIG, we can split a single H100 into two independent halves, which allows for efficient serving of smaller models.

As part of our commitment to staying ahead, we benchmarked [H200](https://www.baseten.co/blog/evaluating-nvidia-h200-gpus-for-llm-inference/) and GH200 GPUs, analyzing their nuanced performance and cost tradeoffs. These insights help us provide tailored recommendations for diverse use cases.

## Supporting production-ready speculative decoding

Speculative Decoding (SpecDec) gained prominence as an optimization technique in 2024. While SpecDec's benefits are context-dependent, especially with long contexts or small batch sizes, our careful orchestration made it a powerful tool in our arsenal.

We built [support for SpecDec](https://www.baseten.co/blog/how-we-built-production-ready-speculative-decoding-with-tensorrt-llm/) into our performance toolkit, with an emphasis on optimizing code generation use cases.

In addition to ordinary SpecDec, we’ve invested in self-speculative techniques as well. We saw great results in our [Medusa benchmarks](https://www.baseten.co/blog/how-to-double-tokens-per-second-for-llama-3-with-medusa/), and expect even better results from Eagle in the near future. Prompt look-up decoding is another promising technique that we plan to make available out of the box in the near future.

## Implementing featureful inference servers

Serving models with low latency and high throughput isn’t enough. Developers need featureful inference servers that support industry standards and cutting edge features.

We implemented [guaranteed structured output and function calling](https://www.baseten.co/blog/how-to-build-function-calling-and-json-mode-for-open-source-and-fine-tuned-llms/) on top of TensorRT-LLM, using the `Outlines` library and our own CUDA kernels. Soon, we will optimize these further using xGrammar. We also implemented support for full Open AI spec for interacting with TensorRT-LLM based models on our stack. 

We also [introduced LoRA inference support](https://www.baseten.co/blog/how-to-serve-10-000-fine-tuned-llms-from-a-single-gpu/) via TensorRT-LLM, allowing customers to run multiple lightweight fine-tunes on a single model deployment. This drastically reduced the barrier to fine-tuning and unlocked new possibilities for model personalization.

As the demand for long context models (128k tokens or more) grew, we implemented optimizations like chunked prefill and KV cache reuse to manage increased GPU memory pressure and maintain high performance. Additionally, we adopted innovative techniques like Writing in the Margins to improve long-context retrieval accuracy without significant performance overhead.

## Delivering performance optimizations in developer-friendly tooling

This performance and feature set wouldn’t be useful if there wasn’t a consistent and developer-friendly way to use it in production.

Manually building TensorRT-LLM engines was a cumbersome and error-prone process. We addressed this by developing the [Engine Builder](https://www.baseten.co/blog/automatic-llm-optimization-with-tensorrt-llm-engine-builder/), an automated tool that streamlines engine creation and deployment. What once required hours of manual effort now takes mere minutes. Additionally, the Engine Builder supports features like dynamic GPU allocation for FP8 quantization, simplifying complex workflows for our users.

To further enhance deployment efficiency, we replaced Triton Inference Server with a custom C++ server. Building using TensorRT-LLM directly provided us greater control, allowing us to build features such as structured output and fixing bugs and performance issues crucial to performant implementation of Speculative Decoding. Integrating the Rust HF tokenizers library, we significantly improved tokenization and thus inference speed on our stack. We were also able to reduce the docker image size a lot which improves startup time.

## Achieving best in class performance results across modalities

### Optimized inference for custom LLMs

Optimizing the performance of custom LLMs presents a unique challenge. However, our flexible tooling allowed us to achieve excellent results, including [60% better performance for Writer’s custom LLMs](https://www.baseten.co/resources/customers/writer/).

### Real-time AI phone calls

We also developed low-latency multi-model inference for use cases like AI phone calling. With Bland, we optimized end-to-end phone calling to below 400 milliseconds, creating a real-time user experience.

### 1000x real-time factor for Whisper ASR

In Q4, we [launched the world’s fastest, cheapest, most accurate ASR](https://www.baseten.co/blog/the-fastest-most-accurate-and-cost-efficient-whisper-transcription/) (automatic speech recognition) pipeline. This effort combined model performance and infrastructure work and has unlocked new opportunities and use cases for our customers.

### Day-one DeepSeek V3 support with SGLang

In December, DeepSeek V3 was released as the new state-of-the-art open-source LLM rivaling GPT-4o and Sonnet 3.5. We [supported DeepSeek V3 on day one](https://x.com/basetenco/status/1872402216247808056) using SGLang and H200 GPUs.

### Large model cold starts in less than a minute

With autoscaling GPU infrastructure, the time it takes to bring a new deployment of an AI model online is called the “cold start time” and needs to be minimized. A major component of cold start times is downloading large model weights onto the model serving instance.

Depending on external services like Hugging Face for model weights presented challenges, including downtime and performance bottlenecks. To address this, we developed a secure, in-house weight distribution system.

With download speeds now measured in gigabytes per second, we reduced model start times to under a minute for large models and under 10 seconds for smaller ones. Collaboration with NVIDIA is in progress to further enhance TensorRT engine load times by 10–25%.

## What we’re excited about for 2025

2024 was a year of relentless innovation and impactful results. We’re excited to both broaden and deepen our work in 2025 to deliver even more performant models for our customers.

Some areas of research we’re excited about in the coming year include:

- Expanding our work on speculative decoding to include Eagle.
- Optimizing - [embeddings models](https://www.baseten.co/resources/guide/high-performance-embedding-model-inference/)across various architectures.
- Exploring NVIDIA’s new Blackwell GPU architecture while continuing to optimize the use of Hopper GPUs.
- Supporting FP4 quantization and SpinQuant for efficient model inference .
- Adding disaggregated serving for increased performance.

This is only a sample of what we’ll be working on in 2025. We are actively recruiting engineers to join our model performance team. If you’re interested in working on productionizing cutting-edge research, [visit our careers page](https://www.baseten.co/careers/) for information on open roles in the model performance team.
