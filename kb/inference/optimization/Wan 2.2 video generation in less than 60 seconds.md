---
title: Wan 2.2 video generation in less than 60 seconds
kind: blog
topic: inference
subtopic: optimization
secondary_topics:
- models/multimodal
summary: Built a Wan 2.2 video-generation runtime delivering 3x faster inference on
  NVIDIA Blackwell and 2.5x on Hopper versus the default runtime, cutting cost 67%
  for high-volume dedicated deployments at batch size one.
triage: null
skip_reason: null
source: baseten
url: https://www.baseten.co/blog/wan-2-2-video-generation-in-less-than-60-seconds
author: Faraz Shahsavan
published: '2026-01-21'
fetched: '2026-11-12T06:14:26Z'
classifier: claude
taxonomy_rev: 2
words: 1245
content_sha256: 4c6cae544f3ce01483268b6a9a82ae7cf889454776f430e45bb6e9844fc75c04
---

# Wan 2.2 video generation in less than 60 seconds

Model performance
# Wan 2.2 video generation in less than 60 seconds

Baseten delivers three times faster Wan 2.2 inference on NVIDIA Blackwell GPUs than the default runtime


- Authors
- Date
- January 21, 2026

TLDR

We developed a Wan 2.2 runtime that delivers three times faster Wan 2.2 inference on NVIDIA Blackwell GPUs than the default runtime, while also providing 2.5 faster inference on NVIDIA Hopper GPUs.

[Wan 2.2](https://github.com/Wan-Video/Wan2.2) is an open video generation model by [Wan AI](https://wan.video/), a research lab affiliated with Alibaba. At Baseten, we developed a Wan 2.2 runtime that delivers three times faster Wan 2.2 inference on NVIDIA Blackwell GPUs than the default runtime, while also providing 2.5 times faster inference on NVIDIA Hopper GPUs.

Video generation is the most demanding modality for inference. Architecturally, video generation extends image generation: it uses the same iterative denoising process in latent space (around 50 steps) but operates on far more data per step. As with images, video generation is compute-bound, but each iteration processes an entire video rather than a single frame.

Due to this compute intensity, batching video generation requests provides little benefit. Video model inference typically runs with a batch size of one, even on a full node of eight GPUs, with every GPU working together to produce a single video.

Because inference generally runs at a batch size of one, improving latency also improves throughput and thus cost. Our Blackwell-based Wan 2.2 runtime delivers a 67% cost reduction for high-volume dedicated deployments.


This blog post details the model performance techniques and runtime optimizations we used within the [Baseten Inference Stack](https://www.baseten.co/resources/guide/the-baseten-inference-stack/) to optimize inference for Wan 2.2.

To compare our implementation with Wan-video, we ensured identical environments, prompts, and parameters.

Our benchmarking setup for both implementations ran with:

- 40 sampling steps
- A 1280x720 resolution
- 81 frames per video

Prompt sequence lengths ranged from 32 to 512 characters. Prompt sequence length did not affect performance.

Each benchmark was run multiple times to prevent outliers, with the median scores reported. Overall, Wan 2.2 video generation runs 2.6x faster on H100 and 3.2x faster on B200 when run with the Baseten inference stack.

Video generation is still an emerging modality, and tooling for inference is less robust than the ecosystem around LLMs. Specifically, we found that video generation inference still has a lot of low-hanging fruit at the CUDA kernel level.

Within our PyTorch-based inference service, we optimized a number of kernels that collectively represent a good chunk of the wall clock time for Wan 2.2 inference.

The most essential CUDA kernel optimization was around the `multiply_add` kernel (GEMM) for larger operands. PyTorch implementations of this kernel are optimized for small inputs, with libraries like cuBLAS working around this with built-in lookup tables tailored to specific applications like popular model architectures (e.g., Llama). Outside of these well-supported applications, it is difficult to pick the best possible configuration for matmul. We created our own optimized kernel based on the specific input shapes of Wan 2.2 video generation.

We also improved upon the following CUDA kernels with Wan-specific optimizations:

- **RoPE attention:** Implements rotary positional embeddings by applying a position-dependent rotation to the query and key vectors. Concretely, this kernel multiplies the inputs by sinusoidal frequency terms and applies a rotation relative to a baseline position before the attention matmul, encoding temporal and spatial order directly into attention.
- **LayerNorm:** A normalization kernel that standardizes activations by subtracting the mean and dividing by the variance across the feature dimension, followed by learned scale and bias parameters. LayerNorm helps stabilize both training and inference by ensuring consistent activation distributions across layers.
- **RMSNorm:** A simplified normalization layer that scales activations based on their root mean square, without subtracting the mean. RMSNorm is commonly used in transformer models to keep activation magnitudes stable while reducing computation and memory overhead compared to full LayerNorm.

In addition to this kernel-level work, we optimized multiple features of the inference engine itself.

Video generation models use sequence parallelism to split across multiple GPUs. Specifically, Wan 2.2 uses [Ulysses Sequence Parallelism (USP)](https://arxiv.org/pdf/2309.14509) to shard on the latent sequence dimension and share latent space.

USP requires all-to-all communication among GPUs. In a naive implementation, that communication is serial. Our implementation bypasses this with NCCL and uses the Blackwell architecture’s asynchronous programming paradigm to enable async copying for USP.

To further take advantage of the multi-GPU inference hardware, we set the `offload_model` parameter to false for Wan 2.2 inference. When this parameter is true, it preserves VRAM by pushing large modules to the CPU when idle, which introduces overhead from PCIe transfers. By defaulting to false, we keep everything on the GPU to maximize throughput.

For these inference optimizations to be usable in production, they need to work across a range of video generation requests. Wan 2.2 supports a number of inference parameters:

- `prompt`: A text prompt processed by the text encoder describing the desired video in natural language. There is no special schema or structure to this prompt.
- `size`: A selection from possible resolutions (720\*1280, 1280\*720, 480\*832, 832\*480, 704\*1280, 1280\*704, 1024\*704, and 704\*1024).
- `frame_num`: The number of frames, which determines the length of the video. Must equal 4n+1 for some integer value of N (e.g. 49, 81, 125) to align the temporal transformer.
- `shift`: Adjust the diffusion noise to make the timing of the video slower (higher value) or faster (lower value).
- `sampling_steps`: Like in image generation models, the number of steps to iterate over the latent space, trading off quality for inference speed (default of 50).
- `guide_scale`: Like in image generation models, a higher guidance offers greater prompt adherence while a lower guidance gives the model more creative freedom.
- `seed`: A number used to condition randomness, making noise reproducible.

Throughout the benchmarking process, we tested various combinations of parameters to ensure robust, production-ready support in all scenarios.

All optimizations described in this post have been fully lossless, they have not affected output quality at all.

Compared to, say, an LLM, it’s hard to measure the output quality of a video generation model. The best metrics are head-to-head Elo-based rankings. This makes it even more challenging to find the right tradeoff between speed and quality for lossy speed improvements.

We are experimenting with a few promising areas of research that, in limited testing, allow trading off some quality for more speed. Using an attention cache drops observed quality slightly but results in up to another 50% latency improvement, while FP4 quantization reduces output quality further for even more speed. We plan to publish more on lossy quality optimizations as we find success in production.

Ultimately, lossless inference optimization allows all users to confidently deploy optimized models and guarantee that they are receiving the best possible performance with the highest quality output.

Wan 2.2 in production

Ultimately, these inference optimizations are only valuable when used to actually make video generation faster for high-volume production use cases.

Baseten runs large-scale video generation for top AI-native companies. Delivering this demanding modality at scale requires more than just a fast inference engine. Our entire inference stack, including multi-cloud capacity management, ensures reliable performance through traffic spikes from moments like launches and viral marketing campaigns.

If you want to serve Wan 2.2, or your own custom-built video generation model, with best-in-class latency and throughput, our model performance engineering team is ready to deliver the same kinds of optimizations described in this article to your model and workload.
