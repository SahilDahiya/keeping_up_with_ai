---
title: 'FP8: Efficient model inference with 8-bit floating point numbers'
topic: inference
subtopic: quantization
secondary_topics: []
summary: Explains FP8 numeric formats and why 8-bit floating point can improve efficient
  model inference.
source: baseten
url: https://www.baseten.co/blog/fp8-efficient-model-inference-with-8-bit-floating-point-numbers/
author: Pankaj Gupta; Philip Kiely
published: '2024-03-07'
fetched: '2026-07-11T04:09:59Z'
classifier: codex
taxonomy_rev: 1
words: 1045
content_sha256: 508d23ba0d250550784f35b8a68838bb6542475ec153b332bac01df2c7ecd6ce
triage: keep
skip_reason: null
---

# FP8: Efficient model inference with 8-bit floating point numbers

![8-bit floating point numbers](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1747527531-fp8-basic.png%3Fauto%3Dformat%26fit%3Dcrop%26h%3D630%26w%3D1200&w=3840&q=100)

FP8 is an 8-bit data format that offers an alternative to INT8 for quantizing LLMs. Thanks to its higher dynamic range, FP8 is suitable for quantizing more of an LLM’s components, most notably its activations, making inference faster and more efficient. FP8 quantization is also safer for smaller models, like 7B parameter LLMs, than INT8 quantization, offering better performance improvements with less degradation of output quality.

Large language models (LLMs) have billions of parameters, each of which is a number that has to be stored, read, and processed in a consistent format while running the model. There are multiple data formats, or precisions, that you can use for model parameters.

By default, most LLM inference uses a data format called FP16, meaning that the model’s components (weights, activations, KV cache) are all expressed as 16-bit floating point numbers. However, it’s increasingly common to [quantize LLMs for production use](https://www.baseten.co/blog/introduction-to-quantizing-ml-models/), meaning the model is served using a lower precision, like an 8-bit integer, for model weights.

Quantizing a model can massively improve inference speed and decrease operational cost, but if not done carefully can degrade model output quality. Thus, quantizing isn’t always a feasible strategy, especially for models with fewer parameters (such as the 7B class of LLMs).

Traditionally, quantization goes from FP16 to INT8 or INT4. However, quantizing to FP8, [a newly supported data format for model inference](https://arxiv.org/pdf/2209.05433.pdf), can offer even more performance benefits without significant quality degradation. FP8, or an 8-bit floating point format, is supported on GPUs with NVIDIA Ada Lovelace and Hopper architectures, including the L4 and H100 GPUs.

In this article, we’ll investigate the FP8 data format to understand how it works and why it can offer better output quality for quantized LLMs, including models with just seven billion parameters.

## An introduction to floating point numbers

Floating point number formats were a revelation in the math that underpins computer science, and their history stretches back over 100 years. Today, floating point number formats are codified in the IEEE 754-2019 spec, which sets international standards for how floating point numbers are expressed.

A floating point number has 3 parts:

- **Sign**: a single bit indicating if the number is positive or negative
- **Range**(or- **Exponent**): the power of the number.
- **Precision**(or- **Mantissa**): the significant digits of the number.

In contrast, an integer representation is mostly significant digits (precision). It may or may not have a sign bit depending on the format, but no exponent.

![Visualizing FP32, FP16, FP8, and INT8 precisions](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1709770809-twitter-post-20.png%3Fauto%3Dformat%26w%3D1200&w=3840&q=75) Visualizing FP32, FP16, FP8, and INT8 precisions

Visualizing FP32, FP16, FP8, and INT8 precisionsWhile FP8 and INT8 are both 8-bit values, the way they use those bits determines their utility as data formats for model inference.

## FP8 vs INT8 data format

Model inference in INT8 uses signed 8-bit integers, which can range in value from -128 to 127. FP8 also has 256 possible values — the fundamental math that 8 bits equals 2^8 distinct numbers doesn’t change — but what changes is the dynamic range that these numbers can express.

There are two FP8 formats supported on the [NVIDIA Hopper architecture](https://developer.nvidia.com/blog/nvidia-hopper-architecture-in-depth/):

- E4M3, which has 4 exponent bits and 3 mantissa (precision) bits.
- E5M2, which instead has 5 exponent bits and 2 mantissa bits.

We use the default E4M3 variant of FP8, which offers a higher precision than E5M2 but with a lower dynamic range. However, the dynamic range of E4M3 FP8 is still substantially higher than INT8. Here’s the dynamic range of each data format:

- INT8 dynamic range: 2^8
- E4M3 FP8 dynamic range: 2^18 (we use this variant)
- E5M2 PF8 dynamic range: 2^32

Again, both INT8 and FP8 only have 256 possible values. But while each number in INT8 is exactly the same distance from its neighbors, FP8 uses exponents to represent much smaller and much larger numbers, but with larger, less uniform gaps between neighboring values within the space.

## The role of dynamic range in quantization

At a high level, quantization is the process of mapping from one value space to another value space. Mapping from one value space to another is a common operation in computing — for example, to convert a full-color photo to black and white you map each pixel from an RGB value to a constrained set of grayscale values.

If you’re converting a color photo that has colors that are close together, they can get muddy in the black and white version. That’s because the dynamic range of grayscale is compressed: the values are grouped close together, so differences that are large in full color can become imperceivable. You can use an algorithm to adjust for this, but what if you could instead just expand the dynamic range of the values space that you’re mapping to?

Quantization is a more robust mapping operation than conversion to grayscale; the goal is to retain as much information from the original data format as possible. That’s why FP8’s higher dynamic range makes it more effective than INT8 for many circumstances. Dynamic range isn’t everything, you also need precision, so the E4M3 variant provides the right balance.

This higher dynamic range means that after FP16 values are mapped to FP8, it’s easier to tell them apart and retain more of the encoded information from the model parameters. This makes FP8 quantization more reliable for smaller models, like 7B LLMs, where the relatively low parameter count necessitates retaining as much information per parameter as possible.

## Applying FP8 in production

In practice, FP8 enables quantizing not just an LLM’s weights (which is possible with [weights-only quantization in INT8](https://www.baseten.co/blog/faster-mixtral-inference-with-tensorrt-llm-and-quantization/)) but also the activations and KV cache. This avoids expensive calculations in FP16 during model inference; these operations are instead done natively in FP8. While there exist quantization schemes for doing activations in INT8 such as SmoothQuant, these methods have a high risk of introducing loss of quality and degrading model output compared to FP8.

FP8 is supported on latest-generation GPUs such as the [NVIDIA H100 GPU](https://www.baseten.co/blog/unlocking-the-full-power-of-nvidia-h100-gpus-for-ml-inference-with-tensorrt/), where alongside other optimizations from TensorRT-LLM it can [deliver remarkable performance](https://www.baseten.co/blog/33-faster-llm-inference-with-fp8-quantization/). There are always [multiple factors to consider when quantizing models](https://www.baseten.co/blog/introduction-to-quantizing-ml-models/), such as checking for any increase in perplexity, but FP8 offers a new path to highly efficient model inference for many LLMs.
