---
title: Real-time video generation inference on Baseten
kind: blog
topic: inference
subtopic: optimization
secondary_topics:
- models/multimodal
summary: Details Baseten's real-time video inference runtime for Wan 2.2, combining
  four-step timestep distillation (~20x), custom kernel fusion (~1.5x), and NVFP4
  quantization (~1.5x) for a combined 53.6x speedup, cutting per-clip generation from
  over two minutes to 2.75 seconds and cost from 5 cents to under a sixth of a cent.
triage: null
skip_reason: null
source: baseten
url: https://www.baseten.co/blog/real-time-video-generation-inference-on-baseten/
author: Ali Taha; Brendan Duke; Yikai Zhu; Faraz Shahsavan; Pankaj Gupta; Philip Kiely
published: '2026-07-16'
fetched: '2026-07-17T06:46:29Z'
classifier: claude
taxonomy_rev: 2
words: 1313
content_sha256: b6672b76eea0a41b70a1144d568e0e691abdc6792101ee344ac0bb2728c1ad72
---

# Real-time video generation inference on Baseten

![Real-time video generation inference](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1784232341-real-time-video.png%3Fauto%3Dformat%26fit%3Dcrop%26h%3D630%26w%3D1200&w=3840&q=100)

We run Wan 2.2 video generation in 2.75 seconds per clip, a 53.6x improvement over the baseline implementation. Our runtime optimizations across custom kernels, NVFP4 quantization, and timestep distillation deliver these performance gains. This video generation runtime is available as a limited-time demo through July 31 behind our custom-built content guardrails.

Baseten’s model performance team has built a new video inference runtime that delivers SOTA performance on Wan 2.2, the leading open-source model for text-to-video generation.

![Real-time video generation inference demo on Baseten](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fimage.mux.com%2Fd9G6JfoFKQkaHZ00JL8cVtdxvOSQOELiI%2Fthumbnail.jpg&w=3840&q=75)

This performance came from multiple model-level and runtime-level optimizations:

- Timestep distillation to four-step video generation (~20x faster than baseline) 
- Custom kernel optimization and fusion (~1.5x faster than original kernels) 
- Linear quantization in NVFP4 (~1.5x faster than original weights) 

These improvements are multiplicative and together result in a 53.6x speedup in video generation speed, going from more than two minutes to less than three seconds. This also brings the cost per video generated down materially, from five cents to less than one-sixth of a cent per video (a 31x reduction in cost).

This blog provides a high-level overview of the runtime performance work we completed, the infrastructure required to deliver that work at scale, and the guardrails we built to safely open the work to public usage.

You can test the fast video inference for yourself at our [public demo platform](https://www.baseten.co/video/) through July 31, 2026.

## Fast video inference runtime

Unlike LLM inference, video generation is not autoregressive. Instead, diffusion works by iterating over the entire latent space of the final video with bi-directional attention for consistency across the entire sequence. The techniques and tooling for video generation are accordingly quite different than for LLM inference, and the overall stack is less mature. This leaves room for substantial performance improvement via both post-training and inference optimization.

### Timestep distillation

The biggest performance lever was model-level optimization via timestep distillation. By default, Wan 2.2 uses 40 to 80 steps to complete the diffusion process from noise to video. By post-training the model with timestep distillation, we can reduce that to four steps.

Timestep distillation is a lossy optimization. With four steps, the model is more likely to produce visual artifacts and less likely to properly handle consistency and physics in active scenes, like a video of a player dunking a basketball over an opponent. However, reaching real-time video generation currently requires this sacrifice. Timestep distillation brings video generation from >120 seconds to ~6 seconds, bringing it in range of the other optimization methods to get below the five-second real-time mark.

For video models, we apply Distribution Matching Distillation (DMD2) as our core training algorithm. Rather than matching individual denoising steps, DMD2 trains a student model to match the distribution of outputs from a teacher model. Training involves three components updated in alternation: the student generator, a fake score model that prevents mode collapse, and a GAN discriminator that sharpens fine-grained details.

To keep attention over the full temporal-spatial context tractable, we use sequence parallelism, distributing the long context across multiple devices during training.

### Custom kernel engineering

Unlike LLMs, we don’t use a pre-built inference engine to run video generation models. While there are now excellent open-source options like SGLang video, frontier performance still comes from building from scratch in PyTorch.

Wan 2.2 inference is bottlenecked on Self-Attention. Using Video Sparse Attention (VSA) would allow the model to only attend to pieces of the sequence, saving substantial time. However, the default VSA Triton kernel did not offer sufficient performance. After 10 iterations, we created a custom kernel with 1.58x better performance. We also optimized an additional nine kernels that contributed less to the end-to-end time.

Fast individual kernels are not enough. The bottleneck shifts from executing kernels to launching them. However, via kernel fusion, we were able to fuse Adaptive LayerNorm modulation, RMS Norm, and Gated Residual Add together into a single triton kernel, saving hundreds of launches across inference.

For a deep dive on the kernel work, read the [dev notes by Ali Taha](https://x.com/waterloo_intern/status/2070643039668974060) on building frontier kernels.

### NVFP4 quantization

Going from 16 to 4 bits is the last big jump in performance. On an NVIDIA B200 GPU, 4-bit inference accesses roughly 4x higher tensor core throughput than BF16. After applying our attention optimizations, the diffusion transformer becomes dominated by operations on the linear layers, so moving the GEMM operations to NVFP4 alleviates the bottleneck.

![Output quality with BF16 vs NVFP4 GEMM kernels](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fimage.mux.com%2Fq00GgXssTrtryfHBQcKglGigaavK61GSx%2Fthumbnail.jpg&w=3840&q=75)

After quantization to NVFP4, output quality remains visually comparable to BF16. For more on quantization, see our [writeup on quantizing FLUX.2 [dev]](https://www.baseten.co/blog/four-bits/). 

## Scalable inference infrastructure

No matter how fast an individual instance serving the model is, it will be overwhelmed with enough traffic. Video generation infrastructure is just as important as runtime optimizations for building a stable, scalable system.

This is an especially important problem for video as video generation runs with a batch size of one. Even with faster than real time inference, horizontal scale is essential for running production services.

Of course, one essential mechanism is autoscaling. As traffic to the system increases, extra GPU capacity should be spun up to support the increased traffic. This requires a cold start.

For a video generation model, the cold start has four parts:

- Provisioning and scheduling the compute 
- Pulling the inference container image onto the compute 
- Downloading the model weights into the container 
- Starting up the model inference server 

Given the size of the images and weights involved, the second and third steps often take the longest. We built the [Baseten Delivery Network](https://www.baseten.co/blog/baseten-delivery-network-fast-cold-starts-big-models/) to optimize this process for large models, including Wan 2.2.

Regardless of how fast cold starts are, requests still need to be stored if a slot is unavailable. That’s where queuing comes into play. There are actually a number of subtly tricky problems in queuing. While a standard queue is a first-in, first-out system for excess requests, you can do a more complex implementation like a priority queue to, for example, give paid users priority over free users. You also need to ensure that as new replicas come online, the queue sees them and enqueued requests don’t continue waiting for the existing replicas.

In our [inference demo](https://www.baseten.co/video/), we separate queue time from generation time to show both pieces of the system in action.

## Ironclad content guardrails

Video generation models have the potential for misuse across multiple vectors. A big piece of the inference problem is figuring out how to serve video generation models responsibly. On top of standard guardrails like rate limiting to protect against abuse, video models require separate classifiers to ensure only desirable outputs are generated.

![Guardrails reject prompts for unsuitable outputs](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1784233913-baseten-git-alit-video-demo-live-blueprintbyb10-vercel-app_video.png%3Fauto%3Dformat%26w%3D1200&w=3840&q=75) Guardrails reject prompts for unsuitable outputs

Guardrails reject prompts for unsuitable outputsFor our Wan 2.2 demo endpoint, we trained a custom classifier with a specific focus on preventing NSFW outputs and other unsuitable uses of the model. This classifier runs in front of every request and determines within a handful of milliseconds whether or not to allow the prompt.

For the demo, we accept a somewhat higher false positive rate than a standard classifier. For deployment in a specific application, we’d recommend training a classifier on common prompts from within the application’s domain to achieve better specificity while retaining high sensitivity.

## Run video inference in production

Through July 31, 2026, you can try our fast video inference for yourself for free at [baseten.co/video](https://www.baseten.co/video/).

We built this demo to showcase the combined capabilities of our runtime, infrastructure, and guardrails on the leading open-source video generation model. Whether you’re building an application on top of open-source or fine-tuned models, or you’re a lab training the next generation of video, we [want to work with you](https://www.baseten.co/talk-to-us/).

For more technical information on our image and video inference runtime, read our work on [video kernel engineering](https://x.com/waterloo_intern/status/2070643039668974060), [four-bit quantization](https://x.com/waterloo_intern/status/2024493443905683859), and [distillation training](https://x.com/waterloo_intern/status/2030074784894308770).
