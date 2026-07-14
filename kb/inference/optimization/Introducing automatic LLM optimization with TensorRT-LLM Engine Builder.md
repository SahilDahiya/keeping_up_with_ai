---
title: Introducing automatic LLM optimization with TensorRT-LLM Engine Builder
topic: inference
subtopic: optimization
secondary_topics: []
summary: Describes automatic LLM optimization with TensorRT-LLM Engine Builder for
  production serving.
source: baseten
url: https://www.baseten.co/blog/automatic-llm-optimization-with-tensorrt-llm-engine-builder/
author: Abu Qader; Philip Kiely
published: '2024-08-01'
fetched: '2026-07-11T04:09:19Z'
classifier: codex
taxonomy_rev: 1
words: 980
content_sha256: 56fe5d75f547d2961ae2fdf5c07a088d6e50d77d75c68f01caeb7ad756419f29
triage: keep
skip_reason: null
---

# Introducing automatic LLM optimization with TensorRT-LLM Engine Builder

![TensorRT-LLM Engine Creation](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1747439101-trt-engine.png%3Fauto%3Dformat%26fit%3Dcrop%26h%3D630%26w%3D1200&w=3840&q=100)

Today, we’re launching the TensorRT-LLM Engine Builder, which empowers every developer to deploy extremely efficient and performant inference servers for open-source and fine-tuned LLMs in minutes. The Engine Builder replaces hours of tedious procurement, installation, and validation via automated deploy-time engine creation.

The TensorRT-LLM Engine Builder anchors a complete pipeline from model weights to low-latency, high-throughput production inference for open-source and fine-tuned models.

In a single command, you can now build and serve a wide range of foundation models like Llama, Mistral, and Whisper, plus fine-tuned variants. The Truss framework gives you full control to customize your model server, while the Baseten platform provides dedicated deployments with automatic traffic-based scaling, logging and metrics for observability, and best-in-class security and compliance.

![Manual compilation vs engine builder: same great performance, 90% less effort](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1722526885-group-14155.png%3Fauto%3Dformat%26w%3D1200&w=3840&q=75) Manual compilation vs engine builder: same great performance, 90% less effort

Manual compilation vs engine builder: same great performance, 90% less effort## Why we made the TensorRT-LLM engine builder

TensorRT-LLM is an open-source performance optimization toolbox created by NVIDIA for optimizing large language model inference. [TensorRT](https://www.baseten.co/blog/high-performance-ml-inference-with-nvidia-tensorrt/) and TensorRT-LLM are extremely performant; we’ve achieved results like [33% faster LLM inference](https://www.baseten.co/blog/33-faster-llm-inference-with-fp8-quantization/), [40% faster SDXL](https://www.baseten.co/blog/40-faster-stable-diffusion-xl-inference-with-nvidia-tensorrt/) inference, and [3x better LLM throughput](https://www.baseten.co/blog/unlocking-the-full-power-of-nvidia-h100-gpus-for-ml-inference-with-tensorrt/).

We often use TensorRT-LLM to support our custom models for teams like [Writer](https://writer.com/). For their latest industry-specific Palmyra LLMs, Palmyra-Med-70B and Palmyra-Fin-70B, [Writer saw 60% higher tokens per second with TensorRT-LLM inference engines](https://www.baseten.co/resources/customers/writer/) deployed on Baseten.

While TensorRT-LLM is incredibly powerful, we found ourselves and our customers repeatedly facing three issues when trying to use it in production:

- It can take the better part of an hour just to spin up a GPU instance and wait for all of the required runtimes and packages to finish installing.
- The GPUs used for engine building must exactly match the production hardware – for Llama 3.1 405B that means you’re tracking down at least 8 extra H100 GPUs.
- Once the TensorRT-LLM engine is built and validated, it needs to be exported, packaged, and deployed manually.

In total, building engines is more often an exercise in patience than engineering—it often takes hours of babysitting the build process to produce a single engine.

To eliminate manual work from the engine building process and bring the power of TensorRT-LLM to more teams, we created the TensorRT-LLM Engine Builder, which automatically builds optimized model serving engines at deploy time from a single configuration file.

TensorRT-LLM works by converting model weights into an inference engine. The TensorRT-LLM engine builder handles this entire process automatically during model deployment. With the engine builder, you no longer need to procure or configure a separate GPU instance for compilation, deal with compatibility issues, or manually export finished engines.

## How TensorRT-LLM makes model inference faster

In computing, optimization comes from specialization. For example, GPUs are better at inference than CPUs because GPUs specialize in matrix multiplication. Building a model serving engine follows the same philosophy. To improve your model’s performance, you need to bake in constraints.

A TensorRT inference engine is built for a specific model, GPU, sequence shape, and batch size. TensorRT-LLM uses this information to compile optimized CUDA instructions to maximize every aspect of the model’s performance and take advantage of every feature of the chosen hardware.

TensorRT-LLM is [compatible with over 50 LLMs](https://nvidia.github.io/TensorRT-LLM/reference/support-matrix.html) along with similarly-architected models like Whisper and certain large vision models. It also supports fine-tuned versions of these foundation models. During the engine building process, TensorRT-LLM can also apply post-training quantization for further speed and efficiency gains. For production serving, TensorRT-LLM supports model serving features like [in-flight batching](https://www.baseten.co/blog/continuous-vs-dynamic-batching-for-ai-inference/) and [LoRA swapping](https://www.baseten.co/blog/how-to-serve-10-000-fine-tuned-llms-from-a-single-gpu/) and advanced optimization techniques like speculative sampling.

Using TensorRT-LLM, you can build inference engines maximized for latency, throughput, cost, or a balance thereof.

## How to use the TensorRT-LLM engine builder on Baseten

![TensorRT-LLM Engine Builder Demo](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fimage.mux.com%2Fz900s1Rp00z8lFuzfadLZX5j5PjO02NN4bD%2Fthumbnail.jpg&w=3840&q=75)

The TensorRT-LLM engine builder is built into [Truss](https://github.com/basetenlabs/truss), our open-source model packaging framework. To use the engine builder, install the latest version of Truss:

`pip install --upgrade truss`One thing that makes TensorRT-LLM so powerful is the wide range of options provided for inference optimization. The engine builder supports [the full set of parameters for TensorRT-LLM](https://docs.baseten.co/performance/engine-builder-config), so you’re not sacrificing control for convenience.

To build an engine for a given LLM on a given GPU, it’s helpful to first think about your goals.

- What kinds of inputs and outputs are you expecting?
- Do you need to support a large number of concurrent requests?
- Do you want the lowest possible latency, regardless of cost?

With your goals set, building an inference engine becomes straightforward. Based on your use case, set values like:

- Sequence shapes: TensorRT-LLM compiles CUDA instructions for specific input and output sequence lengths. Correctly predicting sequence shapes improves performance.
- Batch size: how many requests to process at once. Larger batch sizes mean lower costs but worse latency.
- Quantization: running a model at a lower precision improves performance and cost but may affect output quality and must be carefully validated.

When you deploy the Engine Builder Truss, your TensorRT-LLM engine will be seamlessly built and deployed to the model inference server. You get full control over the model server – you can access the engine object directly in the Truss’ Python interface – plus all of the benefits of deploying a model on Baseten like autoscaling in response to traffic, logging and metrics, and secure and compliant inference.

[Sign up for Baseten today](https://app.baseten.co/signup/?utm_source=Web&utm_medium=Blog&utm_campaign=Engine-Builder-Launch) to [access the Engine Builder](https://docs.baseten.co/performance/engine-builder-overview) – get started with our [end-to-end guide to TensorRT-LLM engine building](https://docs.baseten.co/performance/engine-builder-tutorial) or follow along with our [demo video](https://www.youtube.com/watch?v=h4F6s84vrw4). You can also try example implementations for [Llama](https://docs.baseten.co/performance/examples/llama-trt), [Mistral](https://docs.baseten.co/performance/examples/mistral-trt), and [Whisper](https://docs.baseten.co/performance/examples/whisper-trt) models.

If you have any questions about how to get the best possible performance for LLMs in production, especially for fine-tuned and custom LLMs, [let us know](https://www.baseten.co/talk-to-us/)! We’ll get in touch to discuss your use case and support your team’s experimentation.
