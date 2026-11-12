---
title: Sub-second image generation with Flux.2 and Qwen-Image
kind: blog
topic: null
subtopic: null
secondary_topics: []
summary: null
triage: null
skip_reason: null
source: baseten
url: https://www.baseten.co/blog/sub-second-image-generation-flux2-and-qwen-image
author: Faraz Shahsavan
published: '2026-05-18'
fetched: '2026-11-12T06:07:34Z'
classifier: null
taxonomy_rev: 2
words: 705
content_sha256: 5cf8c5adf5e30800007b7dcc4f4481aedddeaa61a730b781a161509180241d4e
---

# Sub-second image generation with Flux.2 and Qwen-Image

Model performance
# Sub-second image generation with Flux.2 and Qwen-Image

2.3x faster Flux.2 \[dev\] and 1.6x faster Qwen-Image on NVIDIA Blackwell GPUs using quantization, optimized attention kernels, and runtime improvements.


- Authors
- Date
- May 18, 2026

TLDR

We optimized image generation serving for Flux.2 \[dev\] and Qwen-Image, delivering 2.3x and 1.6x speedups over SGLang on NVIDIA Blackwell GPUs, and 1.9x and 1.1x speedups on NVIDIA Hopper GPUs.

Image generation has become a core inference workload for creative tools, design workflows, marketing applications, and various AI-native products. Like [video generation](https://www.baseten.co/blog/wan-2-2-video-generation-in-less-than-60-seconds/), it relies on an iterative denoising process in latent space, repeatedly refining an image over multiple sampling steps. These workloads are highly latency-sensitive and usually run at very small batch sizes, so improving single-request latency directly improves user experience, throughput, and cost efficiency.

In this post, we show how the [Baseten Inference Stack](https://www.baseten.co/resources/guide/the-baseten-inference-stack/) accelerates image generation for Flux.2 \[dev\] and Qwen-Image on NVIDIA B200 and H100 GPUs through a set of runtime and serving optimizations. [Flux.2 \[dev\]](https://github.com/black-forest-labs/flux2) is an open-weight model from [Black Forest Labs](https://bfl.ai/) for high-quality text-to-image generation and image editing, designed for strong prompt-following and production deployments. [Qwen-Image](https://huggingface.co/Qwen/Qwen-Image-2512) is a foundation image generation model developed by [Qwen](https://qwen.ai/), known for complex text rendering, precise image editing, and multilingual text generation.

To compare default and optimized image generation serving, we benchmarked each model under consistent single-request settings.

Our benchmarking setup used:

- Single-request latency
- Single-GPU inference
- B200 and H100 GPUs
- 1024x1024 image generation
- `n = 1` images generated
- `num_inference_steps = 8`
- Fixed seed for reproducibility

The prompt sequence lengths ranged from 32 to 4096 tokens. Prompt length did not meaningfully affect latency, so we report a single representative latency value per configuration.

Overall, optimized image generation runs up to 2.3x faster for Flux.2 \[dev\] and up to 1.6x faster for Qwen-Image on B200 GPUs.

Image generation is latency-sensitive. Most production image generation workloads run at low batch sizes because users expect interactive responses. As a result, reducing single-request latency improves both user experience and cost efficiency.

Within the Baseten Inference Stack, we optimized image generation serving with:

- Hardware-aware quantization FP4 on B200
FP8 on H100
- Memory optimizations
- Optimized attention kernels
- Specialized element-wise kernels
- Runtime-level serving improvements

For Flux.2 \[dev\], FP4 on B200 provides the strongest result, bringing latency below one second. On H100, FP8 and memory optimizations eliminate the need for CPU offload and nearly halve latency.

For Qwen-Image, FP8 provides significant gains on both B200 and H100, while FP4 provides the strongest B200 result with a 1.57x speedup over baseline.

For these optimizations to be useful in production, they need to work across real image generation requests. The optimized serving stack supports common image generation parameters, including:

- `prompt:` Text prompt describing the image
- `n:` Number of images to generate
- `size:` Output image dimensions, such as 1024x1024
- `response_format:` Response format, such as b64\_json
- `num_inference_steps:` Number of diffusion steps
- `seed:` Random seed for reproducibility
- `guidance_scale:` Prompt adherence strength
- `negative_prompt:` Text describing what to avoid
- `output_format:` Output format, such as png, webp, jpeg, or jpg
- `background:` Background handling, such as transparent, opaque, or auto

The benchmarks in this post used:

```
{
  "n": 1,
  "size": "1024x1024",
  "num_inference_steps": 8,
  "seed": 42
}
```
The results in this post focus on Flux.2 \[dev\] and Qwen-Image, but the same serving approach can support additional image generation workloads.

Baseten can currently support workloads for other models, such as:

- Qwen-Image-Layered
- Flux.2 \[klein\]
- Other Flux and Qwen-Image variants

Future optimization work includes additional workload- and use-case-specific runtime tuning, and further improvements to image generation latency on Blackwell and Hopper GPUs.

Fast image generation only matters if it works reliably in production.

The Baseten Inference Stack is built for production workloads that need low latency, high reliability, and efficient GPU utilization. These optimizations make it easier to serve image generation models across both Hopper and Blackwell GPUs while reducing cost per request.

For teams building with Flux.2 \[dev\], Qwen-Image, Qwen-Image-Layered, Flux.2 \[klein\], or custom image generation models, Baseten’s model performance engineering team can deliver the same kinds of workload-specific optimizations in production. [Reach out](https://www.baseten.co/talk-to-us/) to talk to our engineers!
