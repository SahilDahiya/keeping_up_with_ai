---
title: 40% faster Stable Diffusion XL inference with NVIDIA TensorRT
topic: inference
subtopic: optimization
secondary_topics:
- models/multimodal
summary: Explains TensorRT optimization for Stable Diffusion XL inference, including
  latency and throughput gains.
source: baseten
url: https://www.baseten.co/blog/40-faster-stable-diffusion-xl-inference-with-nvidia-tensorrt/
author: Pankaj Gupta; Justin Yi; Philip Kiely
published: '2024-02-22'
fetched: '2026-07-11T04:10:05Z'
classifier: codex
taxonomy_rev: 1
words: 2583
content_sha256: 280482a59d5bc4c46c2e4e8e24334d4867e1b5783496c010932f3d110212a083
triage: keep
skip_reason: null
---

# 40% faster Stable Diffusion XL inference with NVIDIA TensorRT

![40% faster SDXL](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1747527735-faster-sdxl.png%3Fauto%3Dformat%26fit%3Dcrop%26h%3D630%26w%3D1200&w=3840&q=100)

Using NVIDIA TensorRT, we were able to improve SDXL inference latency by 40% and throughput by 70% on NVIDIA H100 Tensor Core GPUs. We achieved these performance gains by individually optimizing each component in the SDXL image generation pipeline. Performance gains are greater for higher step counts and more powerful GPUs, and the techniques used can be applied to similar image generation pipelines, including SDXL Turbo.

[Stable Diffusion XL (SDXL)](https://www.baseten.co/library/stable-diffusion-xl/) is a text-to-image model that can generate anything from line art to photorealistic images from simple text prompts. SDXL powers all kinds of AI-based image applications, but to create a great user experience, images need to be created quickly. By optimizing model inference, we can create images with SDXL more quickly and efficiently, delivering a better user experience while saving money on model hosting.

Using [NVIDIA TensorRT](https://developer.nvidia.com/tensorrt), a software development kit for high-performance deep learning inference, we were able to improve SDXL inference times by up to 30% on NVIDIA A100 Tensor GPUs and 40% on H100 Tensor Core GPUs. This guide to our optimization process introduces:

- The essential components of SDXL’s modular architecture and how they work together to form an image generation pipeline.
- The process of using TensorRT to - [optimize ML models for inference](https://www.baseten.co/blog/unlocking-the-full-power-of-nvidia-h100-gpus-for-ml-inference-with-tensorrt/).
- Performance benchmarks for SDXL with TensorRT on A10G and A100 and H100 Tensor Core GPUs.
- Considerations for using TensorRT in production.
- Options for deploying an optimized implementation of SDXL as an API endpoint.

In this guide, we’ll focus on optimizing the performance of the base SDXL model. There are other approaches to image generation with SDXL that provide substantial increases in speed, such as Latent Consistency Models (LCMs) and SDXL Turbo. However, the image quality from these approaches is not high enough for every use case. The techniques described in this guide can also speed up LCMs and SDXL Turbo, but we’ll stick to the traditional SDXL model here.

SDXL is an incredible foundation model not only because of its strong image generation capabilities but also its modular architecture. Understanding the individual components of the model is key to creating an optimized implementation without reducing image quality.

## The essentials of SDXL architecture

SDXL is not just one model. It’s a modular collection of smaller models working together as an image generation pipeline. This modular architecture makes SDXL flexible and powerful, but it also makes optimization more complicated as each component must be optimized individually.

The SDXL pipeline has four major components:

- **CLIP**: Two different models create an embedding from the prompt.
- **UNet**: The base model in the sequence, this denoiser applies the embedded prompt to noise in latent space for a series of steps.
- **Refiner**: This optional model is really a pipeline-within-a-pipeline with its own embeddings and UNet.
- **VAE**: This model maps UNet/Refiner output from latent space to pixel space.

These individual models work together to create images in latent space. From [the SDXL paper](https://arxiv.org/pdf/2307.01952.pdf), we can visualize how the entire pipeline operates:

![Figure 1 right from SDXL: Improving Latent Diffusion Models for High-Resolution Image Synthesis](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1708466541-screenshot-2024-02-07-at-3-46-10-pm.png%3Fauto%3Dformat%26w%3D1200&w=3840&q=75)

### How does SDXL understand prompts?

SDXL takes a text prompt of up to 75 tokens (about 300 characters). It uses CLIP ViT-L and OpenCLIP ViT-bigG as embedding models to encode text as vectors that are passed to the UNet and Refiner models.

### What is latent space?

SDXL inference happens in something called “latent space.” Images, as you see them on your screen, are made up of pixels, or a matrix of values for concepts like red, green, blue, and opacity. This is called “pixel space.” Latent space offers a different mechanism for representing image data.

Images represented in latent space use substantially less memory, which makes inference much faster. For SDXL, the latent space representation of an image is a 128x128 matrix, while the pixel space is a 1024x1024 matrix.

Latent space, more generally, refers to any representation of data where the values map back to concrete meaning, even if the map isn’t clear. For SDXL images, individual values in latent space don’t have the same precise meaning as, say, “red,” but the values are legible to the UNet model and are massively more efficient to use than pixel values.

### How does a UNet work?

UNet is the denoising component of the pipeline and operates in latent space. It iteratively removes noise according to the prompt to generate an image.

UNet is the main phase of SDXL inference and is memory-bound, meaning that a GPU’s VRAM bandwidth will be the bottleneck in image generation speed. UNet works in inference steps, with each step creating a clearer and clearer image. The more inference steps are needed, the longer it will take to create an image. Depending on the model, prompt, and use case, anywhere from twenty to fifty steps are needed to create an acceptable image.

![SDXL image quality at different inference step counts](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1705955599-sdxl-5.png%3Fauto%3Dformat%26w%3D1200&w=3840&q=75)

### What is a Refiner model?

There are certain things like facial features and hands that Stable Diffusion models tend to have trouble generating accurately. To address this, SDXL introduces an optional Refiner model. This model targets those specific weaknesses of the main model and corrects issues in latent space.

The Refiner model is its own pipeline within the SDXL pipeline with its own UNet. It’s also memory-bound and runs inference in steps. Using the Refiner model can add to inference time, but is often worth it for the increased realism in the output. In previous experimentation, we’ve found that you can [reduce the number of steps of the base UNet when using the Refiner](https://www.baseten.co/blog/sdxl-inference-in-under-2-seconds-the-ultimate-guide-to-stable-diffusion-optimiza/) with minimal impact on output quality to offset this increased generation time.

### What does a VAE do?

A Variational AutoEncoder, or VAE, is a model that translates from latent space to pixel space. In other words, it takes the output of the UNet/Refiner model and converts it into an actual image. There are several VAEs available for SDXL with relative strengths and weaknesses. We use the standard VAE included in SDXL, but with a [community-generated fp16 quantization](https://huggingface.co/madebyollin/sdxl-vae-fp16-fix) that takes less processing power.

## How we optimized SDXL with TensorRT

[TensorRT](https://github.com/NVIDIA/TensorRT) is NVIDIA’s library for highly performant ML model inference. TensorRT has a number of plugins, such as TensorRT-LLM, which we used for [optimizing models like Mixtral 8x7B](https://www.baseten.co/blog/faster-mixtral-inference-with-tensorrt-llm-and-quantization/). TensorRT-LLM is a library for optimizing all the popular LLMs. But for SDXL, the core TensorRT framework had what we needed.

TensorRT’s [documentation](https://docs.nvidia.com/deeplearning/tensorrt/developer-guide/index.html) has a great [getting-started guide](https://docs.nvidia.com/deeplearning/tensorrt/quick-start-guide/index.html) that walks you step by step from installation through optimizing your first model. TensorRT has a large surface area, with support for multiple input formats, output options, and intermediate steps like [quantization](https://www.baseten.co/blog/introduction-to-quantizing-ml-models/). Here’s what we did for SDXL:

- We exported the model pipeline to - [ONNX](https://pypi.org/project/onnx/), an open model description format. ONNX is an encoding protocol for the entire SDXL pipeline, including architecture, config, and weights.
- We passed the ONNX files to TensorRT, which made an optimized engine for serving each sub-model within SDXL.
- We exported and saved the optimized models as .plan files.
- We used - [Truss](https://truss.baseten.co), our open-source model packaging framework, to get the optimized model ready to serve.

We based this process on an [implementation of SDXL using TensorRT](https://huggingface.co/stabilityai/stable-diffusion-xl-1.0-tensorrt) created by Stability AI in collaboration with NVIDIA. While we took a great deal of inspiration from this example, we re-built the model engines end to end to fully understand the process, and as a result, we now know how to optimize each component individually without compromising image quality — essential for optimizing SDXL variants to achieve similar results.

### Optimization details for SDXL

Throughout this guide, we’ve been calling SDXL a pipeline. This is how the transformers library exposes the model — you only deal with the input text and output image. SDXL acts as a pipeline, but only because each model within it is an interoperable component.

During optimization, it’s our responsibility to maintain this seamless interface between each component. This requires careful checks like:

- Accurately representing model components during ONNX export.
- Mapping the input/output memory allocation space to ensure it is aligned.
- Synchronizing CUDA streams to make sure that each inference step in the UNet actually receives the result of the previous step.
- Testing optimized components individually and in sequence to ensure no SDXL internals are broken.

We completed this optimization process — converting diffusers model code to ONNX, generating optimized versions of each model, and integrating the new components back into the SDXL pipeline — for the CLIP, UNet, and Refiner portions of SDXL.

### Remaining optimization work

While we’ve achieved substantial performance improvements already with TensorRT, there are more avenues for us to explore to unlock even more increases in speed:

- We’re not yet using an optimized implementation of Attention. TensorRT-LLM, a module of TensorRT designed for LLMs, has an optimized implementation for attention layers that could be interesting to apply to SDXL.
- We’re not yet using an optimized implementation of the VAE. The VAE is a relatively small portion of the overall inference time, but an optimized version could shave off as much as another 100 milliseconds.
- We’re using a cutting-edge release of TensorRT, but it’s a rapidly evolving library. As new features are added, we’ll be able to improve inference speed and efficiency even further.

New hardware and updates to TensorRT can help offer even more performance gains. Engines for TensorRT need to be built individually for each type of GPU you want to run the model on to take advantage of that GPU’s specific architectural features. We originally built TensorRT engines for SDXL on the A100 GPU but repeated the work to create matching implementations for the A10G and H100 GPUs.

We were able to test [SDXL on H100 GPUs with TensorRT](https://www.baseten.co/blog/unlocking-the-full-power-of-nvidia-h100-gpus-for-ml-inference-with-tensorrt/), in addition to A100 GPUs. H100 GPUs receive even more benefits from TensorRT than A100 GPUs, including 40% lower latency vs a standard implementation (A100 GPUs see a 26% improvement). Below, we’ll discuss hardware-specific benchmarks in detail.

## Benchmarks for SDXL inference

It would be great if there was just one number that fully summarized SDXL performance. Instead, [understanding SDXL benchmarks](https://www.baseten.co/blog/how-to-benchmark-image-generation-models-like-stable-diffusion-xl/) requires looking at several figures together in context. SDXL inference depends on:

- The number of inference steps. We measured a range of inference steps.
- The hardware selected. We ran benchmarks on A10G, A100, and H100 GPUs.
- The inference configuration. We kept all factors like batch size, image resolution, and prompt constant across benchmarks to ensure consistency.

Here is a summary of our benchmark results, which closely aligns with the [metrics published by Stability AI](https://huggingface.co/stabilityai/stable-diffusion-xl-1.0-tensorrt#performance-comparison).

### SDXL performance with TensorRT across inference step counts

In the SDXL architecture breakdown, we discussed the UNet model — the main motor of SDXL that acts as a denoiser to turn random values into an image representation in latent space. The UNet model runs iteratively, in inference steps.

The UNet model takes by far the longest of any model in the SDXL image generation pipeline, so the step count is the biggest factor in image generation time. We found that as inference step count increases, TensorRT performance gains slightly increase, as optimization to the UNet causes a greater and greater effect on total generation time.

For 1024x1024 pixel images on an A100 GPU, we observed the following improvements in latency when using TensorRT:

Visualized, the speedup improves slightly in percentage terms but substantially in absolute terms as step counts increase:

![Inference time at different step counts for SDXL on an A100 GPU (lower is better).](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1708467354-twitter-post-13.png%3Fauto%3Dformat%26w%3D1200&w=3840&q=75) Inference time at different step counts for SDXL on an A100 GPU (lower is better).

Inference time at different step counts for SDXL on an A100 GPU (lower is better).For 1024x1024 pixel images on an A100 GPU, we observed the following improvements in throughput when using TensorRT:

![Throughput at different step counts for SDXL on an A100 GPU (higher is better).](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1708467236-twitter-post-14.png%3Fauto%3Dformat%26w%3D1200&w=3840&q=75) Throughput at different step counts for SDXL on an A100 GPU (higher is better).

Throughput at different step counts for SDXL on an A100 GPU (higher is better).### SDXL performance with TensorRT across GPUs

TensorRT helps produce consistently higher performance gains on larger, newer GPUs such as the H100 GPU. At 30 inference steps, our benchmarks and [number reported by Stability AI](https://huggingface.co/stabilityai/stable-diffusion-xl-1.0-tensorrt#performance-comparison) confirm that TensorRT improves SDXL performance by:

![Percentage improvement in latency and throughput from using TensorRT (higher is better).](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1709237035-twitter-post-19.png%3Fauto%3Dformat%26w%3D1200&w=3840&q=75) Percentage improvement in latency and throughput from using TensorRT (higher is better).

Percentage improvement in latency and throughput from using TensorRT (higher is better).The A100 and H100 GPUs see larger performance gains than the A10G GPU due to their architectural features, which are utilized by TensorRT. The additional performance gains for the H100 GPU are thanks to optimizations provided by its [NVIDIA Hopper architecture](https://www.nvidia.com/en-us/data-center/technologies/hopper-architecture/).

## SDXL with TensorRT in production

Running benchmarks on a warm node is great, but operating an optimized image-serving pipeline in production is another hurdle.

In the past, we achieved [20 steps of SDXL inference in as little as 2 seconds](https://www.baseten.co/blog/sdxl-inference-in-under-2-seconds-the-ultimate-guide-to-stable-diffusion-optimiza/) on an A100 GPU with torch.compile, but that approach has two downsides versus TensorRT for production use:

- While the optimizations we made were carefully designed, they could reduce model output quality. TensorRT runs the model as is with zero impact on quality.
- More importantly, torch.compile with max autotune is a just-in-time process that adds as much as 40 minutes to model server start-up time, so it isn’t feasible with any kind of autoscaling infrastructure.

Using TensorRT, we bundle the engine and weights and use them when scaling up model servers. TensorRT does have a material disadvantage versus a baseline model server for cold starts. While the baseline server offers cold starts of about 10 seconds, spinning up with TensorRT can take a full minute. We’re actively working to reduce that time, but it still allows for meaningful autoscaling capabilities.

Additionally, TensorRT scales extremely well to H100 GPUs, as we saw in the performance benchmarks. In less than 2 seconds, you can run 30 steps of inference, creating higher-quality images with a much greater throughput of 0.68 images per second.

## Deploy SDXL with TensorRT as an API endpoint

SDXL, an image generation pipeline, is a powerful and modular foundation model that can be adapted to a huge variety of use cases. But many use cases are latency-sensitive, and almost all are cost-sensitive. Decreasing latency and increasing throughput makes SDXL viable for even more uses. With TensorRT, you can get optimized SDXL inference that delivers up to 40% lower latency and 70% higher throughput than the unoptimized model on the same hardware.

Thanks to SDXL’s modular architecture, you can introduce additional capabilities like ControlNet, new models like Playground V2 Aesthetic, and radically increased generation speeds with LCMs and SDXL Turbo. TensorRT can be used to optimize any of these additional components and is especially useful for SDXL Turbo on the H100 GPU, [generating a 512x512 pixel image in 83.2 milliseconds](https://huggingface.co/stabilityai/sdxl-turbo-tensorrt) (though with lower image quality). 

You can run our optimized SDXL build with TensorRT behind a production-ready API endpoint with zero config on Baseten. Regardless of which GPU you use to serve SDXL, you’ll get the benefits of our [autoscaling infrastructure](https://docs.baseten.co/performance/autoscaling), [security and compliance](https://docs.baseten.co/observability/security), and [model management features](https://docs.baseten.co/deploy/lifecycle). Get started:

- To run the model on an A100 GPU, - [deploy SDXL in one click from the model library](https://www.baseten.co/library/stable-diffusion-xl/).
- To maximize performance on an H100 GPU, - [let us know about your use case](https://share.hsforms.com/110ZOAIthRo6IgZXjfPE6tQd5zj5).
