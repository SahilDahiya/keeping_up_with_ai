---
title: Comparing few-step image generation models
topic: models
subtopic: benchmarks
secondary_topics:
- models/multimodal
summary: Compares few-step image generation models and the tradeoffs between speed
  and output quality.
source: baseten
url: https://www.baseten.co/blog/comparing-few-step-image-generation-models/
author: Rachel Rapp
published: '2024-06-14'
fetched: '2026-07-11T04:09:33Z'
classifier: codex
taxonomy_rev: 1
words: 1152
content_sha256: d16a11341504f750cd10036ca6d4ca30ba1c702801bc88ebc39b7c9862bbf8b5
triage: keep
skip_reason: null
---

# Comparing few-step image generation models

![Comparing few-step image generation models](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1747441175-comparing-few-step.png%3Fauto%3Dformat%26fit%3Dcrop%26h%3D630%26w%3D1200&w=3840&q=100)

Few-step image generation models like LCMs, SDXL Turbo, and SDXL Lightning are state-of-the-art for producing high-quality images in less than a few seconds. While LCMs can generate images in under a second, they may not provide the same level of quality as SDXL Turbo and Lightning. SDXL Turbo is optimized to balance speed and detail, whereas SDXL Lightning is optimized for speed without compromising image quality.

Few-step image generation models take only 1-8 iterations to generate an image (versus ~50 for standard models), making them faster and more computationally efficient than their predecessors. These model optimization techniques have three goals:

- To be fast (real-time or near-real-time).
- To increase throughput (images per second) on compute resources.
- To maintain (or increase) image detail and resolution.

In this guide, we identify the bottleneck in diffusion-based image generation, compare state-of-the-art few-step image generation models, discuss their limitations, and explain how to choose the right one for your use case.

## The history of image generation models

Image generation hasn't always relied on deep learning methods, but modern AI-generated images are the result of integrating deep learning into the field. In particular, the publication of [Generative Adversarial Networks](https://arxiv.org/abs/1406.2661) (GANs) in 2014 marked a turning point, becoming one of the first models to produce realistic images. In 2015, [alignDRAW](https://ar5iv.labs.arxiv.org/html/1511.02793) leveraged an iterative generation process, becoming the first text-to-image model.

Diffusion-based methods have recently dominated the space. Models like [Stable Diffusion](https://www.baseten.co/library/stable-diffusion/), DALL-E 3, and Imagen have greatly improved image quality (detail, realism, variety) and resolution (up to 1024x1024 pixels). While inference speed has also improved, it remains one of the significant open issues today: how to increase speed without sacrificing quality. 

Diffusion models create images by beginning with random noise and [gradually transforming it through iterative steps](https://www.baseten.co/blog/how-latent-consistency-models-work/). Due to their iterative image generation, models leveraging diffusion have struggled to reach real-time production speeds. A pre-trained Stable Diffusion model takes up to 50 steps to develop a detailed image at inference. For SDXL, [an optimized implementation takes over 3 seconds on an A100](https://www.baseten.co/blog/40-faster-stable-diffusion-xl-inference-with-nvidia-tensorrt/). 

Three state-of-the-art methods have since been developed to accelerate image generation by reducing iterations to just 1-8 steps:

- Latent Consistency Models (LCMs).
- Stable Diffusion XL Turbo (SDXL Turbo).
- Stable Diffusion XL Lightning (SDXL Lightning).

## Latent Consistency Models (LCMs)

[Latent consistency models](https://www.baseten.co/blog/how-latent-consistency-models-work/) (LCMs) are trained to predict a target latent image vector directly, skipping the many iterations of the diffusion process. In theory, this means LCMs can predict an image in just one step; in practice, the process is repeated 2-4 times to improve image quality. 

To train an LCM, you:

- Sample two latent image vectors from a noising sequence (two vectors with different amounts of noise).
- Predict the target image vector for both samples.
- Optimize such that the difference between the two predictions is minimized.

![A diagram showing a series of penguin pictures with different amounts of noise; two of these images have corresponding noise-free predictions](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1717402255-untitled-presentation-1.jpg%3Fauto%3Dformat%26w%3D1200&w=3840&q=75)

LCMs offer a powerful combination of quality and efficiency for high-resolution image generation. They can be fine-tuned on custom datasets and generate diverse, detailed 1024x1024 pixel images. LCM-LoRA also introduced low-rank adaption training to learn LCM modules efficiently.

LCMs are a good option for real-time image generation: [PixArt-𝝳](https://arxiv.org/pdf/2401.05252) can generate 1024x1024 pixel images from text prompts in half a second. However, these images may be less detailed than those generated by SDXL Turbo and Lightning. If you use too few iterations (typically fewer than four), the images can also become blurry or exhibit noticeable artifacts.

## Stable Diffusion XL Turbo (SDXL Turbo)

Both [SDXL Turbo](https://www.baseten.co/library/sdxl-turbo/) and [SDXL Lightning](https://www.baseten.co/library/sdxl-lightning/) leverage distillation to capture the effectiveness of traditional [SDXL](https://www.baseten.co/library/stable-diffusion-xl/), but in fewer steps. SDXL Turbo leverages [adversarial diffusion distillation](https://static1.squarespace.com/static/6213c340453c3f502425776e/t/65663480a92fba51d0e1023f/1701197769659/adversarial_diffusion_distillation.pdf) (ADD) in particular, which involves three models:

- A relatively simple “student network” initialized with pre-trained weights.
- A more complicated pre-trained “teacher network” (a diffusion model, such as SDXL).
- A discriminator model.

The student model has two objectives:

- To match the target predictions of its teacher (SDXL).
- To fool the discriminator model, which is trained to distinguish the generated samples from real images.

The method is “adversarial” due to the inclusion of the discriminator model, whereas “distillation” refers to the technique of training simpler models to imitate more complicated ones. The adversarial objective encourages image quality, while distillation allows the results to be achieved in so few iterations.

SDXL Turbo is optimized to balance speed and quality, generating images in only 1-4 steps. Compared to LCMs, SDXL Turbo is designed to produce higher quality results in detail and fidelity, given a similar generation time (less than 1 second on an A100 or H100). A disadvantage of Turbo compared to both SDXL Lightning and LCMs is that it’s only designed to generate images of 512x512 pixels.

## Stable Diffusion XL Lightning (SDXL Lightning)

[SDXL Lightning](https://www.baseten.co/library/sdxl-lightning/) is optimized for high inference speed and low response latency. It builds on SDXL Turbo to go as low as one step for text-to-image generation (although in practice, more are needed to ensure image quality — typically 2-8).

Similar to SDXL Turbo, SDXL Lightning uses adversarial distillation to preserve image quality. However, SDXL Lightning also leverages progressive distillation, which involves training a sequence of increasingly smaller models, each learning from the distilled knowledge of the previous, larger model. Progressive distillation is the key to improving speed and resource efficiency in SDXL Lightning.

In practice, users often find images produced by SDXL Lightning to be much higher quality than SDXL Turbo. SDXL Lightning can also generate images of size 1024x1024 pixels, different aspect ratios, and offers LoRA models that produce high-quality outputs.

![Two example image outputs from SDXL Lightning and SDXL Turbo given the prompt "a rhino wearing a suit." SDXL Lightning produces a much more detailed image.](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1718296065-sdxl_lightning_vs_turbo.avif%3Fauto%3Dformat%26w%3D1200&w=3840&q=75)

## How to choose between LCMs, SDXL Turbo, and SXL Lightning

All three model optimization techniques share a common goal: to circumvent traditional diffusion models’ slow UNet denoising steps.

If you’re focused on speed, LCMs like PixArt-𝝳 provide real-time image generation and can be adapted into various models and tasks. However, their image quality might not reach the level of SDXL Turbo or Lightning. SDXL Lightning has a comparable inference speed to PixArt-𝝳 while offering more robust image quality.

If image quality is your primary concern, 512x512 pixels is a sufficiently high resolution, and you’re willing to wait a second or two at inference, then SDXL Turbo is a fair choice. It offers a balance between speed and fidelity, performing inference in under a few seconds.

That said, many users find the quality of images generated by SDXL Lightning much better than Turbo. Given that Lightning can generate high-quality 1024x1024 images, different aspect ratios, has a LoRA offering, and is optimized for speed and efficiency, it’s a solid choice for most use cases. Deploy SDXL Lightning today [in one click from our model library](https://www.baseten.co/library/sdxl-lightning/).
