---
title: 'FLUX.1 on Fireworks: Fast, frugal, and flexible'
kind: blog
topic: null
subtopic: null
secondary_topics: []
summary: null
triage: null
skip_reason: null
source: fireworks
url: https://fireworks.ai/blog/flux-launch
author: null
published: '2024-10-22'
fetched: '2026-09-22T06:12:18Z'
classifier: null
taxonomy_rev: 2
words: 1107
content_sha256: 40151de11792af309c63be170dad4ba71d03ef56f7e7aff859b487ab03e97de7
---

# FLUX.1 on Fireworks: Fast, frugal, and flexible

In partnership with [Black Forest Labs](https://blackforestlabs.ai/), Fireworks is excited to announce commercially-usable **FLUX.1 [dev] and FLUX.1 [schnell]** models on Fireworks:

- •**Leading speeds at half the cost** : The efficiency of Fireworks’ Distributed Inference Engine provides both Flux models at up to 2x speeds and half the cost of other platforms ($0.0014 for FLUX.1 [schnell] and $0.014 for FLUX.1 [dev] for default images)
- •**Customize FLUX for your compound AI system:** Use FLUX as part of your products and for specialized applications by using FLUX on-demand with custom**ControlNet architectures** and custom**LoRA adapter** support.
- •**Privately deploy FLUX with on-demand deployments:** FLUX is our first image generation model supported via on-demand deployments. On-demand deployments provide private GPUs to guarantee reliability and consistent speed.

Fireworks has been committed to fast, production-ready image generation - through milestones like an [exclusive launch](https://fireworks.ai/blog/sd3-api-powered-by-fireworks) of Stable Diffusion 3 and serving SDXL and Playground v2.5 with < 1 second generation times. Today, Fireworks is partnering with Black Forest Labs, the original creators of the Stable Diffusion image generation models, to offer FLUX.1 [dev] and FLUX.1 [schnell]. Fireworks’ platform is designed to bring AI applications from prototype to production usage. By default, FLUX.1 models used outside of Fireworks have restrictions on commercial usage, but Fireworks and Black Forest Labs’ partnership enables commercial usage of both models on the Fireworks platform. Fireworks offers:

- •[**FLUX.1 \[dev\]](https://huggingface.co/fireworks-ai/FLUX.1-dev-fp8-flumina) :** A distilled version of Black Forest Labs’ highest quality pro model, striking a balance between quality and speed.
- •[**FLUX.1 \[schnell\]](https://huggingface.co/fireworks-ai/FLUX.1-schnell-fp8-flumina) :** Black Forest Labs’ fastest model. FLUX.1 [schnell] is trained to quickly generate images with significantly fewer steps (default step size of 4).

The FLUX models are two of the highest-quality image models available and Fireworks offer the most customizable, fastest, and scalable services for running these models. The FLUX models are available both on Fireworks serverless, where you pay per image (per diffusion step) and do not need to configure GPUs.

Flux on Fireworks is served with industry-leading speeds and prices. FLUX.1 [dev] and FLUX.1 [schnell] cost $0.0005 and $0.00035, respectively, per diffusion step. This equates to a price of $0.014 and $0.0014 per image, respectively (with default settings), less than half the cost of other providers of FLUX which typically serve at $0.03 and $0.003 per image.

|  | Serverless price per step | Serverless price per image (default steps) | Images per $1 | Serverless Deployment | 
|---|---|---|---|---|
| FLUX.1 [dev] FP8 | $0.0005 | $0.014 (28-step) | 71 | https://fireworks.ai/models/fireworks/flux-1-dev-fp8 | 
| FLUX.1 [schnell] FP8 | $0.00035 | $0.0014 (4 step) | 714 | https://fireworks.ai/models/fireworks/flux-1-schnell-fp8 | 

*Example images generated with FLUX.1 [dev] text-to-image and ControlNet on Fireworks (see example [code](https://huggingface.co/fireworks-ai/FLUX.1-dev-ControlNet-Union-Pro-flumina))*

While the FLUX models are powerful on their own, they can be even more useful as part of a broader compound AI system. Production usage of AI frequently requires the use of multiple components, API calls, and models. That’s why Fireworks is excited to offer the most customizable implementation of FLUX.

Fireworks supports:

1. **LoRA serving -** Serve FLUX with LoRAs to get perfect images for your use case.[Low-Rank Adaptation](https://arxiv.org/abs/2106.09685) (LoRA) is a fine-tuning technique to customize model quality. For example, you can use LoRAs to produce FLUX images with[logo design](https://huggingface.co/Shakker-Labs/FLUX.1-dev-LoRA-Logo-Design) or[film portrait](https://huggingface.co/Shakker-Labs/FilmPortrait) styles. Check out the[FLUX.1-dev-flumina](https://huggingface.co/fireworks-ai/FLUX.1-dev-flumina) README to get started with LoRAs on FLUX.
2. **ControlNet -** Serve FLUX with ControlNet to get fine-grained control over shapes, depth and other styling. ControlNet enables developers to pass along a conditioning image to guide image generation along properties like edges, depth, pose, and more (see[details](https://huggingface.co/Shakker-Labs/FLUX.1-dev-ControlNet-Union-Pro) ).
3. **Custom server apps** - Directly compose custom server-side code with FLUX to run AI apps easily and with low latency. Arbitrary custom server apps and code are runnable alongside FLUX as part of server-side inference. This enables blazing-fast inference for common image generation use cases, like using FLUX alongside safety models, upscalers or prompt enhancement models.

These customizations are available for FLUX models served on our on-demand deployments, where you ****[deploy private, auto-scaling GPU(s)](https://fireworks.ai/blog/why-gpus-on-demand). Beyond offering additional support for customizations, the private GPUs that back on-demand deployments are perfect for production traffic and demand spikes. On-demand are billed by GPU-second and users pay nothing when GPUs aren’t in use. Both FLUX.1 [schnell] and [dev] fit on a single A100 or H100.

|  | Price per GPU-hour (on-demand) | 
|---|---|
| A100 | $2.90 | 
| H100 | $5.80 | 

Please note that these customizations are currently only available with BF16-precision versions of FLUX. Fireworks on-demand deployments support users’ choice of BF16 and FP8-quantization for either Flux model. Fireworks’ serverless implementation of FLUX models is FP8-quantized, where we’ve observed substantial speed improvements with negligible quality impact.

- •As always, check out our pricing page for the most up-to-date on-demand prices: [Fireworks Pricing](https://fireworks.ai/pricing#ondemand)

Fireworks’ FLUX.1 support has been built on an alpha version of Fireworks’ **Flumina Server Apps** framework. Multimedia models are frequently used alongside other models or code. For example, image generation models are often used with LoRAs or upscaling models. However, these multimedia apps can be hard to deploy and slow.

Flumina is a framework that solves this problem by enabling custom multimedia models and workloads to run on Fireworks infrastructure. Flumina unlocks:

- •(1) Easy deployment of flexible, scalable workloads composing model inference and other business logic
- •(2) Higher efficiency through Fireworks’ expertise in runtime and deep learning optimization.

Developers package together models, pre/postprocessing logic, and business logic into an app and Fireworks provides an API to optimized, scalable infrastructure. Get started today with Flux customizations on Flumina. See the implementations of FLUX and the ControlNet-Union adapter for examples. Stay tuned for the full Flumina announcement! Fill out this [form](https://forms.gle/1vu3fifDwTEDF95n6) if you have a specific multimedia (audio, video, image, etc) app that you’d want to deploy quickly and easily through guided, alpha usage of Flumina.

Deploy Flux FP8 models on-demand

- •[https://huggingface.co/fireworks-ai/FLUX.1-dev-fp8-flumina](https://huggingface.co/fireworks-ai/FLUX.1-dev-fp8-flumina)
- •[https://huggingface.co/fireworks-ai/FLUX.1-schnell-fp8-flumina](https://huggingface.co/fireworks-ai/FLUX.1-schnell-fp8-flumina)

Deploy Flux FP16 models on-demand

- •[https://huggingface.co/fireworks-ai/FLUX.1-dev-flumina](https://huggingface.co/fireworks-ai/FLUX.1-dev-flumina)
- •[https://huggingface.co/fireworks-ai/FLUX.1-schnell-flumina](https://huggingface.co/fireworks-ai/FLUX.1-schnell-flumina)

Use ControlNet with FP16 Flux models on-demand

With speed, cost-efficiency, and customizability, FLUX on Fireworks provides everything developers need to bring AI to production. The Fireworks platform provides the best building blocks for compound AI applications by providing a variety of customizable models and components, on top of Fireworks’ blazing-fast inference engine.

Ready to start building with FLUX?

- •**Use FLUX serverless:** Visit our UI playground to try[Flux.1\[dev\]](https://fireworks.ai/models/fireworks/flux-1-dev-fp8) and[\[schnell\]](https://fireworks.ai/models/fireworks/flux-1-schnell-fp8) instantly with a text prompt.
- •**Deploy and customizing Flux on-demand** - Check out[examples](https://huggingface.co/fireworks-ai/FLUX.1-dev-ControlNet-Union-Pro-flumina) of customizing with Flumina
- •**Join Our Community** : Join our[**Discord channel**](https://discord.gg/fireworks-ai) to connect with other developers and the Fireworks team
- •**Contact us** :[**Reach out**](https://fireworks.ai/company/contact-us) to discuss how we can help you leverage FLUX for your specific use cases.
