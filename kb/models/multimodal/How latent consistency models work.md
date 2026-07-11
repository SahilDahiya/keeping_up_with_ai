---
title: How latent consistency models work
topic: models
subtopic: multimodal
secondary_topics:
- inference/optimization
summary: Explains latent consistency models and how they enable faster image generation.
source: baseten
url: https://www.baseten.co/blog/how-latent-consistency-models-work/
author: Rachel Rapp
published: '2024-06-04'
fetched: '2026-07-11T04:09:35Z'
classifier: codex
taxonomy_rev: 1
words: 1197
content_sha256: 13d21d09520fb15c22f7f255999e9b8ce64fccbdd327039ad02b0f00fe579719
triage: keep
skip_reason: null
---

# How latent consistency models work

![How LCMs work](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1747441215-lcms.png%3Fauto%3Dformat%26fit%3Dcrop%26h%3D630%26w%3D1200&w=3840&q=100)

Latent consistency models are designed to speed up image generation by circumventing the iterative generation process of diffusion-based methods. Building on direct consistency models that operate on image pixels, latent consistency models operate in the latent (lower-dimensional) space. This accelerates inference speed for high-resolution image generation in real time.

Diffusion models like [Stable Diffusion XL](https://www.baseten.co/library/stable-diffusion-xl/) generate images from text prompts by starting with random noise and iterating step-by-step toward a final image. This process, called de-noising, is why it takes several seconds to generate a high-fidelity image, even on a powerful GPU.

But what if you need to generate images in less than a second? That’s where latent consistency models (LCMs) are useful. An LCM combines two types of models:

- Latent diffusion models, which de-noise in the lower-dimensional latent space.
- Direct consistency models, which directly predict image pixels from random noise.

Using a traditional diffusion model like Stable Diffusion, you need as many as 50 steps to create a detailed image. But an LCM can create an image that’s nearly as good in just 2-4 steps, yielding massive time savings during inference.

In this guide, we’ll discuss the architecture of LCMs and their component models to learn how they can create images so fast, what their limitations are, and how to use few-step image generation models in production.

## How diffusion models generate images

Diffusion models are the backbone architecture of many text-to-image models, like DALL-E 2, Imagen, and (not surprisingly) Stable Diffusion. Given a training dataset of images, you can train a diffusion model through a two-phase process:

- The “forward diffusion” or “noising” phase, where noise is incrementally added to an image.
- The “reverse diffusion” or “denoising” phase, where noise is incrementally removed from an image.

In the forward diffusion phase, noise is added until the image’s content is completely replaced (imagine an image of static). During reverse diffusion, the network (model) learns to predict and subtract the noise in a given image. After enough denoising steps, the model should reconstruct the original training sample.

![Two rows of image series show forward diffusion, where a clear image gets replaced by noise, and reverse diffusion, where a noisy image becomes clear.](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1717402486-untitled-presentation-edited.png%3Fauto%3Dformat%26w%3D1200&w=3840&q=75)

The motivation behind the (de)noising process is to encourage the network to learn outlines and finer details of the training images. For instance, given a low noise level, the network should learn which details to adjust to recreate the original image. At inference, the trained model can also leverage a text prompt to guide the denoising process.

Realistically, hundreds to thousands of denoising steps can be necessary to produce high-resolution images, creating a bottleneck.

## Direct diffusion vs latent diffusion

Performing the noising and denoising processes directly on the pixels of an image (or directly on any data) is called “direct diffusion.” With each iteration of (de)noising, you manipulate and return a full-resolution image. For a 1024x1024 image, that’s 1,048,576 pixels per iteration.

On the other hand, latent diffusion models operate on a “latent representation” of the data: a compressed version designed to preserve its essential features. Latent diffusion models (LDMs) operate through a three-step process:

- First, a training image is passed through an “encoder” network which compresses it into a lower-dimensional vector.
- Diffusion occurs in this latent (lower-dimensional) space.
- After denoising is complete, the latent representation is passed to a “decoder” network to reconstruct the final image.

Depending on the network architecture, the latent representation of a 1024x1024 image could be a vector of dimensionality 100-1,000, a huge reduction compared to the number of pixels. While LDMs benefit from less computationally expensive iterations as a result, they also typically need far fewer total iterations (by about an order of magnitude) to generate a high-quality image.

That said, the iterative denoising process is still a bottleneck. Generating 1024x1024-pixel images with SDXL can take 2-4 seconds on an H100 GPU. Further speed improvements are needed to ensure robust, real-time production speeds at high resolutions and on less-powerful hardware.

## How consistency models improve on image generation via diffusion 

Consistency models were developed to overcome the iteration bottleneck of diffusion. Like diffusion models, they also learn to remove noise to generate images. However, rather than doing this stepwise, consistency models learn to map any noisy image directly to a clear final image, skipping the individual denoising steps between.

![A diagram showing a series of penguin pictures with different amounts of noise; two of these images have corresponding noise-free predictions](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1717402255-untitled-presentation-1.jpg%3Fauto%3Dformat%26w%3D1200&w=3840&q=75)

Training a consistency model is theoretically simple:

- Sample two images from a noising sequence (two images with different amounts of noise).
- Predict the target image for both samples.

The model is trained to minimize the difference between the two predicted targets, forcing it to give consistent results regardless of how much noise the sample images have. This is where “consistency” in the name comes from.

You can train a consistency model from scratch, but they’re typically derived from pre-trained diffusion models through a process known as “distillation.” This entails training the consistency model to replicate the outputs of a pre-trained diffusion model, achieving comparable visual outputs with reduced complexity and computational demand.

During inference, consistency models can jump directly from pure noise to a clear image. In practice, this process is often repeated (typically 2-4 times) to obtain a high-resolution image — a huge reduction from the number of iterations required by diffusion models.

That said, consistency models were developed to generate relatively low-resolution images (64x64 or 256x256 pixels). And like direct diffusion models, they operate on an image's pixels.

## Latent consistency models explained

[Latent consistency models](https://arxiv.org/pdf/2310.04378) (LCMs) combine the advantages of latent diffusion and direct consistency models to produce high-resolution images in real time. Employing consistency models in the image latent space, they also learn to directly predict a target image, skipping the iterations of the reverse diffusion process. After denoising, a decoder network reconstructs the image pixels. 

Like direct consistency models, LCMs can be distilled from any pre-trained diffusion model. Unlike direct consistency models, they can be fine-tuned on custom datasets and generate higher-resolution 1024x1024 images. LCMs can generate images from text prompts (PIXART-𝝳) and produce high-fidelity video (VideoLCM), but they haven’t yet been adapted for tasks like inpainting or super-resolution.

LCMs offer a powerful combination of quality and efficiency for high-resolution image generation. For instance, while standard SDXL can take 3.8 seconds to generate a 1024x1024 image on an A100, [PIXART-𝝳 takes only half a second](https://arxiv.org/pdf/2401.05252). 

## Using few-step image generation models in production

LCMs combine the advantages of latent diffusion models and direct consistency models to create accurate, reasonably detailed images in as few as two inference steps. They’re one of the newest developments in the field of few-step image generation.

If you’re building an application where speed is more important than image quality – you’re willing to give up a few details to get images generated in under a second – using similar few-step image generation models like [SDXL Lightning](https://www.baseten.co/library/sdxl-lightning/) is a great option. Or, if image quality is essential, you can still get faster inference for full SDXL runs [using an optimized implementation with TensorRT for 40% faster image generation](https://www.baseten.co/blog/40-faster-stable-diffusion-xl-inference-with-nvidia-tensorrt/).
