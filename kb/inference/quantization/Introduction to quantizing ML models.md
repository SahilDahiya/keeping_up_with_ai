---
title: Introduction to quantizing ML models
topic: inference
subtopic: quantization
secondary_topics:
- models/fine-tuning
summary: Introduces model quantization concepts and how they affect inference efficiency
  and model quality.
source: baseten
url: https://www.baseten.co/blog/introduction-to-quantizing-ml-models/
author: Abu Qader; Philip Kiely
published: '2024-01-31'
fetched: '2026-07-11T04:10:13Z'
classifier: codex
taxonomy_rev: 1
words: 1695
content_sha256: 22835ca69f04df252ee8d5bec233e91ccd56798e7bb67cef9fae6209fc073497
triage: keep
skip_reason: null
---

# Introduction to quantizing ML models

![Quantization](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1747529505-intro-quant.png%3Fauto%3Dformat%26fit%3Dcrop%26h%3D630%26w%3D1200&w=3840&q=100)

Quantization is the process of taking an ML model’s weights and mapping them to a different number format that uses fewer bytes per parameter. This makes model inference substantially faster by making memory access more efficient and unlocking greater Tensor Core compute. However, quantization can meaningfully reduce model output quality for LLMs unless done carefully to preserve the model’s perplexity.

ML models — from the simplest classification model to the most advanced LLM — are made up of parameters: numerical values assigned during training that determine how a model operates. Models can have billions of parameters; the “70B” in “Llama 2 70B” reveals that the model is made up of seventy billion parameters. These parameters are stored along with other configuration information in a file, called the model weights file, and are loaded onto a GPU to run inference.

At a super basic level, model weights are big matrices of numbers. These numbers all have a certain format, called a “precision.” ML model weights generally use one of the following four precisions:

- FP32: a 32-bit floating point number called “full precision”
- FP16: a 16-bit floating point number called “half precision.”
- FP8: an 8-bit floating point number supported on L4 and H100 GPUs.
- INT8: an 8-bit integer format.
- INT4: a 4-bit integer format.

Quantizing is lowering the precision of your model weights by one or more steps along this chain, such as going from FP16 to INT8. This in turn reduces the demand that running the model places on GPU compute and memory, improving inference performance.

## Why float16 is the default precision for LLM inference

Using a given precision for ML inference is a tradeoff between speed and accuracy. Using a higher precision means more accurate calculations, which manifests in higher output quality. But those more precise number formats are larger, which slows down inference considerably.

For inference on most LLMs and many other ML models, FP16 is the go-to precision because it presents the right tradeoff between expressiveness and speed:

- FP16 is a sufficiently expressive format for most model weights but a substantial savings versus FP32.
- FP16 computation is well-supported on GPU Tensor Cores across many generations and architectures.
- FP16 is a good starting point and best practice, but other precisions have a lot to offer as well.

Quantizing a model is a kind of compression, just like creating a JPEG image. When working with images, you need to find a balance between image size and quality. FP16 is like a high-quality JPEG: a larger but reasonable size with almost no loss from compression.

FP16 is a well-supported format on GPU Tensor Cores, offering strong compute performance. When looking at a GPU’s FP16 capabilities, don’t be distracted by a format called BFLOAT16, as that’s meant for model training, not inference. For inference, a GPU’s TFLOPS on FP16 Tensor Cores is your metric. While most LLM inference is memory-bound, it doesn’t hurt that FP16 works well for compute, too.

That said, FP8, INT8, and INT4 are all very capable formats that, when used carefully, can create the same or nearly the same output quality during inference while saving substantially on memory bandwidth and increasing available compute resources. That’s where quantization comes in to take advantage of these small-footprint number formats.

## How to quantize an ML model

Quantization is not a uniform process. There are different algorithms, approaches, and implementations across various libraries and frameworks. We heavily use TensorRT-LLM, a model serving framework by NVIDIA, which also has built-in quantization algorithms.

- A quantization algorithm finds a scaling factor to apply to model weights.
- One simple quantization algorithm is weights-only quantization, which we’ve had success with.
- Quantization requires similar GPU resources to inference; nothing close to what’s required for training or fine tuning.

Quantization algorithms come in different forms, but they generally work by finding a scaling factor and using it to map a range of one type of values (say 16-bit floating point numbers) to a range of another type of values (say 8-bit integers). This scaling factor needs to consistently map these values without distortion to be effective.

One quantization algorithm that we’ve had success using is weights-only quantization. This algorithm only quantizes the model weights, leaving activation functions alone. This preserves some precision in key areas while quantizing most values. Weights-only quantization is implemented in TensorRT-LLM as well as many other frameworks and can be a great first approach when working with a new model.

Like with training or fine tuning a model, quantizing a model is a one-time process. Once you create quantized model weights, you can use them over and over again for inference. Fortunately, compared to training or fine tuning, quantizing only requires minimal GPU resources, similar to inference. When we [quantized Mixtral 8x7B with TensorRT-LLM](https://www.baseten.co/blog/faster-mixtral-inference-with-tensorrt-llm-and-quantization/), running the weights-only algorithm only took a few minutes on an A100.

## How quantization improves inference performance

Quantizing a model makes running inference faster and cheaper in three ways:

- Reducing the file size of model weights files so you can use fewer or smaller GPUs
- Reducing the amount of memory access required by up to 4x per level of precision
- Increasing the amount of compute available by up to 2x per level of precision

In FP16, every billion parameters of an LLM results in about two gigabytes of model weights. So the weights files for, say, Mistral 7B are about 14 gigabytes, while Mixtral 8x7B’s 46.7 billion parameters come in at just under 94 gigabytes.

Quantizing reduces these file sizes linearly. Going from FP16 to INT8 for Mixtral weights cuts the file size to about 47 gigabytes, which fits on a single 80-gig A100 with plenty of headroom for inference. This means you can run the same model with half the hardware.

But quantizing offers more than just smaller file sizes. [Most inference for LLMs is memory-bound](https://www.baseten.co/blog/llm-transformer-inference-guide/), meaning that the GPU memory’s bandwidth is just as important as its size. As quantized models use fewer bits per parameter, reads from memory are faster, speeding up inference. And it doesn’t just double — because model weights are stored in matrices, there is four times less memory access required when working with INT8 vs FP16, and another 4x for going down to INT4.

Where inference is instead compute-bound, such as the prefill phase for language models, quantization is still helpful on most GPUs. GPUs have cores dedicated to computations at different precisions. For example, the A100 is capable of 312 TFLOPS of compute at FP16, but it doubles to 624 trillion operations at `int8`. While there’s always some overhead, quantization offers nearly linear speedups for compute-bound operations.

Even though memory access is up to four times faster and compute only gets up to twice as fast, most LLM inference is still going to be memory bound after quantizing, even down to INT4.

## Why quantization can make model output worse

There is a catch to all of these performance gains. Quantizing can sometimes make model output substantially worse. This depends on three factors:

- The model’s perplexity, a score used to approximate a model’s output quality.
- The size of the model, as models with more parameters generally quantize better.
- The dynamic range and distribution of model weights in key sections of the model.

Perplexity measures model output quality by giving it a fixed set of inputs and outputs and calculating how “surprised” the model is by the output given the input — in other words, the model’s likelihood of generating a known good output in a fixed situation. For perplexity, lower scores are better.

When you quantize a model, one thing to look at is the model’s perplexity before and after quantizing. If there’s a noticeable increase in perplexity, that can signal that the quantization process degraded the model’s reasoning ability.

This is more likely to happen to smaller models than larger ones. Intuitively, as smaller models have fewer parameters, each parameter is more important. There’s less room for error. Fortunately, quantization is generally most useful on larger models with many billions of parameters, as smaller 7B models already fit on less expensive GPUs.

However, more than model size, the dynamic range of model weights within a given area of the model is the clearest indicator of how successful quantizing will be. Remember, quantizing a model is effectively mapping a set of larger, more expressive numbers to a set of smaller, less expressive ones. A large range and uniform distribution within model weights means that the mapping will be clear. As with quantizing in general, there are a range of algorithms and techniques to calculate this, but the distribution of model weights is a good predictor of how well it will survive quantization.

## When to quantize models for production inference

Quantizing models can be a great way to save money on inference by using fewer, smaller, less expensive GPUs to run the same model. If you can preserve an LLM’s perplexity during the quantization process from FP16 to INT8 or even INT4, you can get up to four times better memory usage and two times better compute performance without drastically affecting the model outputs.

Just as there exists a wider variety of quantization algorithms and frameworks than we covered here, so too exist other number formats. Recent GPUs like the L4 and H100 support FP8 as an alternative to INT8. Depending on the algorithm used, [quantizing to FP8 can be an improvement upon using INT8](https://www.baseten.co/blog/fp8-efficient-model-inference-with-8-bit-floating-point-numbers/). Many cards also support FP64, known as “double precision,” but it’s almost never relevant for model inference. By default, most LLM inference is done in FP16, with quantization taking inference to one of the lower precisions.

Quantization is a complex balance to get right — you want to target uniform values within the model weights without affecting the activation functions, KV caches, and other essential values for inference. And models like [Mixtral 8x7B, with its mixture of experts architecture](https://www.baseten.co/blog/faster-mixtral-inference-with-tensorrt-llm-and-quantization/), introduce new complications like routers. But the payoff is that a successful quantization only takes similar GPU resources to a few minutes of inference then permanently reduces the cost to operate your model.
