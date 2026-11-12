---
title: High performance ML inference with NVIDIA TensorRT
kind: blog
topic: inference
subtopic: optimization
secondary_topics: []
summary: Overview of using NVIDIA TensorRT and TensorRT-LLM to compile models into
  optimized serving engines, citing 40% lower SDXL latency and sub-200ms TTFT on Mixtral
  8x7B.
triage: null
skip_reason: null
source: baseten
url: https://www.baseten.co/blog/high-performance-ml-inference-with-nvidia-tensorrt
author: Justin Yi
published: '2024-03-11'
fetched: '2026-11-12T06:12:04Z'
classifier: claude
taxonomy_rev: 2
words: 1084
content_sha256: 7193dda53410ebec842bb2b2ae15c150f20558a0e3a7142793cfe7690784da02
---

# High performance ML inference with NVIDIA TensorRT

Model performance
# High performance ML inference with NVIDIA TensorRT

Use TensorRT to achieve 40% lower latency for SDXL and sub-200ms time to first token for Mixtral 8x7B on A100 and H100 GPUs.


- Authors
- Date
- March 11, 2024

At Baseten, we’ve used NVIDIA TensorRT and TensorRT-LLM to achieve exceptional performance on ML model inference. We’ve seen [40% lower latency on SDXL](https://www.baseten.co/blog/40-faster-stable-diffusion-xl-inference-with-nvidia-tensorrt/), [sub-200 ms time to first token on Mixtral 8x7B](https://www.baseten.co/blog/faster-mixtral-inference-with-tensorrt-llm-and-quantization/), and [3x higher 7B LLM throughput on H100 GPUs](https://www.baseten.co/blog/unlocking-the-full-power-of-nvidia-h100-gpus-for-ml-inference-with-tensorrt/). These early results show the power of TensorRT, but also raise questions — what is TensorRT, what performance benefits can it offer, and how can you leverage it to serve your own models?

“TensorRT-LLM was a breakthrough for Bland. Working with Baseten to optimize all of our GPU processes, **we were able to hit our incredibly ambitious latency target for time to first token** along with much higher throughput. Our users care deeply about speed, and we’re able to meet their needs because of NVIDIA and Baseten.” — Isaiah Granet, CEO, Bland AI

In this guide, we’ll provide a detailed overview of TensorRT, covering:

- The role TensorRT and TensorRT-LLM play in the ML model [inference stack](https://www.baseten.co/resources/guide/the-baseten-inference-stack/).
- Using TensorRT to serve models in production.
- Performance benchmarks for popular open source models optimized with TensorRT.

We’re excited to share the best practices for model optimization that we’ve learned from working closely with NVIDIA engineers from the TensorRT team.

NVIDIA TensorRT is a software development kit for high-performance deep learning inference. Alongside TensorRT, NVIDIA TensorRT-LLM is a Python API for using TensorRT to serve large language models. At Baseten, we use both TensorRT and TensorRT-LLM in production to optimize model performance.

TensorRT takes model weights as input and returns a servable model engine as output. The TensorRT optimization process is run after training and fine-tuning but before inference.

TensorRT works by taking a model description, such as an ONNX file, and compiling the model to run more efficiently on a given GPU. This optimized model can then be served with lower latency and higher throughput using built engines with C++ and Python runtimes. TensorRT achieves best-in-class performance gains by making optimizations at the CUDA level on compiled models rather than serving raw weights directly.

Optimization requires specialization: modifying something with strong general performance to perform even better at a specific task. Optimizing a model for production with TensorRT requires up-front knowledge about your compute needs and traffic patterns. You need to know what you’re optimizing for across:

- **GPU**: TensorRT compiles models to take advantage of specific hardware and architectural features of a given GPU.
- **Batch size**: Batching increases throughput and GPU utilization, giving you more inference for your money, but must be balanced with latency requirements.
- **Precision**: TensorRT comes with various quantization algorithms out of the box, [which can enable faster, less expensive model serving](https://www.baseten.co/blog/introduction-to-quantizing-ml-models/).
- **Input and output shapes**: Approximate input and output shapes (e.g. sequence lengths for LLMs) mimic actual usage, enabling further optimization.

TensorRT compiles your model based on the information you provide for these four factors. The compiled model is not portable — if any one of these factors change, you’ll need to compile a new optimized model.

Using TensorRT and TensorRT-LLM in production requires a supported model and a supported GPU.

TensorRT-LLM supports a [wide range of large language model families](https://github.com/NVIDIA/TensorRT-LLM/?tab=readme-ov-file#models) including Mistral, Llama, Qwen, and many others, plus models in other modalities like Whisper and LLaVA. TensorRT itself supports even more models, including Stable Diffusion XL and models with similar architectures.

TensorRT and TensorRT-LLM [support NVIDIA’s more recent GPU architectures](https://github.com/NVIDIA/TensorRT-LLM/?tab=readme-ov-file#support-matrix), including Volta, Turing, Ampere, Ada Lovelace, and Hopper architectures. We’ve found that TensorRT optimizations provide more performance gains on larger, more recent GPUs, such as the A100 and H100 GPUs.

What level of performance gains do TensorRT and TensorRT-LLM offer? It depends on the model, use case, and GPU. In general, more powerful GPUs, higher traffic, and larger sequence lengths lead to higher performance gains as the more load is on the system, the more there is for TensorRT to optimize.

Below, we’ll share benchmarks for one language model (Mixtral 8x7B) and one image model (SDXL) as examples of the performance gains that are possible with TensorRT.

We [benchmarked Mistral 8x7B with TensorRT-LLM](https://www.baseten.co/blog/faster-mixtral-inference-with-tensorrt-llm-and-quantization/) versus a baseline implementation on A100 GPUs. With larger batches, TensorRT offers even greater performance gains, making it useful for cost efficiency while adhering to strict latency requirements — improving overall throughput while keeping excellent time to first token and perceived tokens per second.

Running in float16 with 512 tokens of input and 128 tokens of output, Mistral 8x7B saw 40% lower latency (time to first token) and 60% higher throughput (total tokens per second) on more realistic higher-concurrency workloads.

We [benchmarked SDXL with TensorRT](https://www.baseten.co/blog/40-faster-stable-diffusion-xl-inference-with-nvidia-tensorrt/) versus a base implementation on A10G, A100, and H100 GPUs. On larger, more powerful GPUs, TensorRT offers even higher performance gains as it’s able to take full advantage of the GPU’s hardware and features. On an H100 GPU, serving SDXL with TensorRT improves latency by 40% and throughput by 70%.

TensorRT and TensorRT-LLM are powerful tools for accelerating model inference, but require specialized technical expertise and a clear understanding of your compute needs and traffic patterns to operate in production.

We’ve worked closely with NVIDIA’s technical specialists to understand and productionalize best practices around using TensorRT to serve ML models in production. We’ve written in depth about our process and results using TensorRT to optimize inference for [Mistral 7B](https://www.baseten.co/blog/benchmarking-fast-mistral-7b-inference/), [Mixtral 8x7B](https://www.baseten.co/blog/faster-mixtral-inference-with-tensorrt-llm-and-quantization/), and [SDXL](https://www.baseten.co/blog/40-faster-stable-diffusion-xl-inference-with-nvidia-tensorrt/) — showcasing how TensorRT on top-of-the-line GPUs leads to world-class performance on latency and throughput sensitive tasks.

Additionally, we’ve productized our model serving work by supporting TensorRT and TensorRT-LLM in [Truss](https://truss.baseten.co), our open source model packaging framework. Out of the box, you get access to all of TensorRT’s model serving features, such as in-flight batching (also known as continuous batching). Get started with production-ready open source implementations of popular models with TensorRT and Truss, including [Mistral](https://github.com/basetenlabs/truss-examples/tree/main/mistral/mistral-7b-instruct-chat-trt-llm-h100), [Llama](https://github.com/basetenlabs/truss-examples/tree/main/llama/llama-2-7b-trt-llm), [Gemma](https://github.com/basetenlabs/truss-examples/tree/main/gemma/gemma-7b-instruct-trtllm), and [many more examples](https://github.com/basetenlabs/truss-examples).

Leverage TensorRT to optimize model performance in production, reducing latency and increasing throughput on high-traffic workloads by deploying them on Baseten. Your models will run securely on our autoscaling infrastructure with scale to zero and fast cold starts. To use TensorRT in production:

1. Choose a TensorRT-optimized model like Mixtral 8x7B from our model library.
2. Deploy the model on an autoscaling instance with a powerful GPU in just one click.
3. [Call your new model endpoint](https://docs.baseten.co/invoke/quickstart) for high-performance inference.
