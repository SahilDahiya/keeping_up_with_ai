---
title: 40% faster Stable Diffusion XL inference with NVIDIA TensorRT
kind: blog
topic: inference
subtopic: optimization
secondary_topics: []
summary: Using NVIDIA TensorRT to optimize each component of the SDXL image-generation
  pipeline improved inference latency by 40% and throughput by 70% on H100 GPUs versus
  A100.
triage: null
skip_reason: null
source: baseten
url: https://www.baseten.co/blog/40-faster-stable-diffusion-xl-inference-with-nvidia-tensorrt
author: Pankaj Gupta
published: '2024-02-22'
fetched: '2026-11-12T06:11:56Z'
classifier: claude
taxonomy_rev: 2
words: 2567
content_sha256: 50f9aacee4d16f31cf8b8193fb710af13e4b68fe4988bbbaf59a6bed3e0c0900
---

# 40% faster Stable Diffusion XL inference with NVIDIA TensorRT

Model performance
# 40% faster Stable Diffusion XL inference with NVIDIA TensorRT

Using NVIDIA TensorRT to optimize each component of the SDXL pipeline, we improved SDXL inference latency by 40% and throughput by 70% on NVIDIA H100 GPUs.


- Authors
- Date
- February 22, 2024

TLDR

Using NVIDIA TensorRT, we were able to improve SDXL inference latency by 40% and throughput by 70% on NVIDIA H100 Tensor Core GPUs. We achieved these performance gains by individually optimizing each component in the SDXL image generation pipeline. Performance gains are greater for higher step counts and more powerful GPUs, and the techniques used can be applied to similar image generation pipelines, including SDXL Turbo.

Stable Diffusion XL (SDXL) is a text-to-image model that can generate anything from line art to photorealistic images from simple text prompts. SDXL powers all kinds of AI-based image applications, but to create a great user experience, images need to be created quickly. By optimizing model inference, we can create images with SDXL more quickly and efficiently, delivering a better user experience while saving money on model hosting.

Using [NVIDIA TensorRT](https://developer.nvidia.com/tensorrt), a software development kit for high-performance deep learning inference, we were able to improve SDXL inference times by up to 30% on NVIDIA A100 Tensor GPUs and 40% on H100 Tensor Core GPUs. This guide to our optimization process introduces:

- The essential components of SDXL’s modular architecture and how they work together to form an image generation pipeline.
- The process of using TensorRT to [optimize ML models for inference](https://www.baseten.co/blog/unlocking-the-full-power-of-nvidia-h100-gpus-for-ml-inference-with-tensorrt/).
- Performance benchmarks for SDXL with TensorRT on A10G and A100 and H100 Tensor Core GPUs.
- Considerations for using TensorRT in production.
- Options for deploying an optimized implementation of SDXL as an API endpoint.

In this guide, we’ll focus on optimizing the performance of the base SDXL model. There are other approaches to image generation with SDXL that provide substantial increases in speed, such as Latent Consistency Models (LCMs) and SDXL Turbo. However, the image quality from these approaches is not high enough for every use case. The techniques described in this guide can also speed up LCMs and SDXL Turbo, but we’ll stick to the traditional SDXL model here.

SDXL is an incredible foundation model not only because of its strong image generation capabilities but also its modular architecture. Understanding the individual components of the model is key to creating an optimized implementation without reducing image quality.

SDXL is not just one model. It’s a modular collection of smaller models working together as an image generation pipeline. This modular architecture makes SDXL flexible and powerful, but it also makes optimization more complicated as each component must be optimized individually.

The SDXL pipeline has four major components:

- **CLIP**: Two different models create an embedding from the prompt.
- **UNet**: The base model in the sequence, this denoiser applies the embedded prompt to noise in latent space for a series of steps.
- **Refiner**: This optional model is really a pipeline-within-a-pipeline with its own embeddings and UNet.
- **VAE**: This model maps UNet/Refiner output from latent space to pixel space.

These individual models work together to create images in latent space. From [the SDXL paper](https://arxiv.org/pdf/2307.01952.pdf), we can visualize how the entire pipeline operates:

SDXL takes a text prompt of up to 75 tokens (about 300 characters). It uses CLIP ViT-L and OpenCLIP ViT-bigG as embedding models to encode text as vectors that are passed to the UNet and Refiner models.

SDXL inference happens in something called “latent space.” Images, as you see them on your screen, are made up of pixels, or a matrix of values for concepts like red, green, blue, and opacity. This is called “pixel space.” Latent space offers a different mechanism for representing image data.

Images represented in latent space use substantially less memory, which makes inference much faster. For SDXL, the latent space representation of an image is a 128x128 matrix, while the pixel space is a 1024x1024 matrix.

Latent space, more generally, refers to any representation of data where the values map back to concrete meaning, even if the map isn’t clear. For SDXL images, individual values in latent space don’t have the same precise meaning as, say, “red,” but the values are legible to the UNet model and are massively more efficient to use than pixel values.

UNet is the denoising component of the pipeline and operates in latent space. It iteratively removes noise according to the prompt to generate an image.

UNet is the main phase of SDXL inference and is memory-bound, meaning that a GPU’s VRAM bandwidth will be the bottleneck in image generation speed. UNet works in inference steps, with each step creating a clearer and clearer image. The more inference steps are needed, the longer it will take to create an image. Depending on the model, prompt, and use case, anywhere from twenty to fifty steps are needed to create an acceptable image.

There are certain things like facial features and hands that Stable Diffusion models tend to have trouble generating accurately. To address this, SDXL introduces an optional Refiner model. This model targets those specific weaknesses of the main model and corrects issues in latent space.

The Refiner model is its own pipeline within the SDXL pipeline with its own UNet. It’s also memory-bound and runs inference in steps. Using the Refiner model can add to inference time, but is often worth it for the increased realism in the output. In previous experimentation, we’ve found that you can [reduce the number of steps of the base UNet when using the Refiner](https://www.baseten.co/blog/sdxl-inference-in-under-2-seconds-the-ultimate-guide-to-stable-diffusion-optimiza/) with minimal impact on output quality to offset this increased generation time.

A Variational AutoEncoder, or VAE, is a model that translates from latent space to pixel space. In other words, it takes the output of the UNet/Refiner model and converts it into an actual image. There are several VAEs available for SDXL with relative strengths and weaknesses. We use the standard VAE included in SDXL, but with a [community-generated fp16 quantization](https://huggingface.co/madebyollin/sdxl-vae-fp16-fix) that takes less processing power.

[TensorRT](https://github.com/NVIDIA/TensorRT) is NVIDIA’s library for highly performant ML model inference. TensorRT has a number of plugins, such as TensorRT-LLM, which we used for [optimizing models like Mixtral 8x7B](https://www.baseten.co/blog/faster-mixtral-inference-with-tensorrt-llm-and-quantization/). TensorRT-LLM is a library for optimizing all the popular LLMs. But for SDXL, the core TensorRT framework had what we needed.

TensorRT’s [documentation](https://docs.nvidia.com/deeplearning/tensorrt/developer-guide/index.html) has a great [getting-started guide](https://docs.nvidia.com/deeplearning/tensorrt/quick-start-guide/index.html) that walks you step by step from installation through optimizing your first model. TensorRT has a large surface area, with support for multiple input formats, output options, and intermediate steps like [quantization](https://www.baseten.co/blog/introduction-to-quantizing-ml-models/). Here’s what we did for SDXL:

1. We exported the model pipeline to [ONNX](https://pypi.org/project/onnx/), an open model description format. ONNX is an encoding protocol for the entire SDXL pipeline, including architecture, config, and weights.
2. We passed the ONNX files to TensorRT, which made an optimized engine for serving each sub-model within SDXL.
3. We exported and saved the optimized models as .plan files.
4. We used [Truss](https://truss.baseten.co), our open-source model packaging framework, to get the optimized model ready to serve.

We based this process on an [implementation of SDXL using TensorRT](https://huggingface.co/stabilityai/stable-diffusion-xl-1.0-tensorrt) created by Stability AI in collaboration with NVIDIA. While we took a great deal of inspiration from this example, we re-built the model engines end to end to fully understand the process, and as a result, we now know how to optimize each component individually without compromising image quality — essential for optimizing SDXL variants to achieve similar results.

Throughout this guide, we’ve been calling SDXL a pipeline. This is how the transformers library exposes the model — you only deal with the input text and output image. SDXL acts as a pipeline, but only because each model within it is an interoperable component.

During optimization, it’s our responsibility to maintain this seamless interface between each component. This requires careful checks like:

- Accurately representing model components during ONNX export.
- Mapping the input/output memory allocation space to ensure it is aligned.
- Synchronizing CUDA streams to make sure that each inference step in the UNet actually receives the result of the previous step.
- Testing optimized components individually and in sequence to ensure no SDXL internals are broken.

We completed this optimization process — converting diffusers model code to ONNX, generating optimized versions of each model, and integrating the new components back into the SDXL pipeline — for the CLIP, UNet, and Refiner portions of SDXL.

While we’ve achieved substantial performance improvements already with TensorRT, there are more avenues for us to explore to unlock even more increases in speed:

- We’re not yet using an optimized implementation of Attention. TensorRT-LLM, a module of TensorRT designed for LLMs, has an optimized implementation for attention layers that could be interesting to apply to SDXL.
- We’re not yet using an optimized implementation of the VAE. The VAE is a relatively small portion of the overall inference time, but an optimized version could shave off as much as another 100 milliseconds.
- We’re using a cutting-edge release of TensorRT, but it’s a rapidly evolving library. As new features are added, we’ll be able to improve inference speed and efficiency even further.

New hardware and updates to TensorRT can help offer even more performance gains. Engines for TensorRT need to be built individually for each type of GPU you want to run the model on to take advantage of that GPU’s specific architectural features. We originally built TensorRT engines for SDXL on the A100 GPU but repeated the work to create matching implementations for the A10G and H100 GPUs.

We were able to test [SDXL on H100 GPUs with TensorRT](https://www.baseten.co/blog/unlocking-the-full-power-of-nvidia-h100-gpus-for-ml-inference-with-tensorrt/), in addition to A100 GPUs. H100 GPUs receive even more benefits from TensorRT than A100 GPUs, including 40% lower latency vs a standard implementation (A100 GPUs see a 26% improvement). Below, we’ll discuss hardware-specific benchmarks in detail.

It would be great if there was just one number that fully summarized SDXL performance. Instead, [understanding SDXL benchmarks](https://www.baseten.co/blog/how-to-benchmark-image-generation-models-like-stable-diffusion-xl/) requires looking at several figures together in context. SDXL inference depends on:

- The number of inference steps. We measured a range of inference steps.
- The hardware selected. We ran benchmarks on A10G, A100, and H100 GPUs.
- The inference configuration. We kept all factors like batch size, image resolution, and prompt constant across benchmarks to ensure consistency.

Here is a summary of our benchmark results, which closely aligns with the [metrics published by Stability AI](https://huggingface.co/stabilityai/stable-diffusion-xl-1.0-tensorrt#performance-comparison).

In the SDXL architecture breakdown, we discussed the UNet model — the main motor of SDXL that acts as a denoiser to turn random values into an image representation in latent space. The UNet model runs iteratively, in inference steps.

The UNet model takes by far the longest of any model in the SDXL image generation pipeline, so the step count is the biggest factor in image generation time. We found that as inference step count increases, TensorRT performance gains slightly increase, as optimization to the UNet causes a greater and greater effect on total generation time.

For 1024x1024 pixel images on an A100 GPU, we observed the following improvements in latency when using TensorRT:

| Inference steps | Baseline | TensorRT | Improvement | 
|---|---|---|---|
| 10 steps | 2.0498 sec | 1.4985 sec | 26.9% | 
| 15 steps | 2.6786 sec | 1.8542 sec | 27% | 
| 20 steps | 3.3871 sec | 2.4146 sec | 28.7% | 
| 25 steps | 4.0698 sec | 2.8729 sec | 29.4% | 
| 30 steps | 4.7317 sec | 3.3390 sec | 29.4% | 

Visualized, the speedup improves slightly in percentage terms but substantially in absolute terms as step counts increase:

For 1024x1024 pixel images on an A100 GPU, we observed the following improvements in throughput when using TensorRT:

| Inference steps | Baseline | TensorRT | Improvement | 
|---|---|---|---|
| 10 steps | 0.4878 req/sec | 0.6673 req/sec | 36.8% | 
| 15 steps | 0.3733 req/sec | 0.5117 req/sec | 37.1% | 
| 20 steps | 0.2952 req/sec | 0.4142 req/sec | 40.3% | 
| 25 steps | 0.2457 req/sec | 0.3481 req/sec | 41.6% | 
| 30 steps | 0.2113 req/sec | 0.2995 req/sec | 41.7% | 

TensorRT helps produce consistently higher performance gains on larger, newer GPUs such as the H100 GPU. At 30 inference steps, our benchmarks and [number reported by Stability AI](https://huggingface.co/stabilityai/stable-diffusion-xl-1.0-tensorrt#performance-comparison) confirm that TensorRT improves SDXL performance by:

| GPU | Latency decrease | Throughput increase | 
|---|---|---|
| A10G | 13% | 20% | 
| A100 | 29% | 42% | 
| H100 | 41% | 70% | 

The A100 and H100 GPUs see larger performance gains than the A10G GPU due to their architectural features, which are utilized by TensorRT. The additional performance gains for the H100 GPU are thanks to optimizations provided by its [NVIDIA Hopper architecture](https://www.nvidia.com/en-us/data-center/technologies/hopper-architecture/).

Running benchmarks on a warm node is great, but operating an optimized image-serving pipeline in production is another hurdle.

In the past, we achieved [20 steps of SDXL inference in as little as 2 seconds](https://www.baseten.co/blog/sdxl-inference-in-under-2-seconds-the-ultimate-guide-to-stable-diffusion-optimiza/) on an A100 GPU with torch.compile, but that approach has two downsides versus TensorRT for production use:

1. While the optimizations we made were carefully designed, they could reduce model output quality. TensorRT runs the model as is with zero impact on quality.
2. More importantly, torch.compile with max autotune is a just-in-time process that adds as much as 40 minutes to model server start-up time, so it isn’t feasible with any kind of autoscaling infrastructure.

Using TensorRT, we bundle the engine and weights and use them when scaling up model servers. TensorRT does have a material disadvantage versus a baseline model server for cold starts. While the baseline server offers cold starts of about 10 seconds, spinning up with TensorRT can take a full minute. We’re actively working to reduce that time, but it still allows for meaningful autoscaling capabilities.

Additionally, TensorRT scales extremely well to H100 GPUs, as we saw in the performance benchmarks. In less than 2 seconds, you can run 30 steps of inference, creating higher-quality images with a much greater throughput of 0.68 images per second.

SDXL, an image generation pipeline, is a powerful and modular foundation model that can be adapted to a huge variety of use cases. But many use cases are latency-sensitive, and almost all are cost-sensitive. Decreasing latency and increasing throughput makes SDXL viable for even more uses. With TensorRT, you can get optimized SDXL inference that delivers up to 40% lower latency and 70% higher throughput than the unoptimized model on the same hardware.

Thanks to SDXL’s modular architecture, you can introduce additional capabilities like ControlNet, new models like Playground V2 Aesthetic, and radically increased generation speeds with LCMs and SDXL Turbo. TensorRT can be used to optimize any of these additional components and is especially useful for SDXL Turbo on the H100 GPU, [generating a 512x512 pixel image in 83.2 milliseconds](https://huggingface.co/stabilityai/sdxl-turbo-tensorrt) (though with lower image quality).

You can run our optimized SDXL build with TensorRT behind a production-ready API endpoint with zero config on Baseten. Regardless of which GPU you use to serve SDXL, you’ll get the benefits of our autoscaling infrastructure, security and compliance, and model management features. Get started:

- To run the model on an A100 GPU, deploy SDXL in one click from the model library.
- To maximize performance on an H100 GPU, let us know about your use case.
