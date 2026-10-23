---
title: SDXL and SSD-1B Image-to-Image and ControlNet API | Fireworks
kind: blog
topic: null
subtopic: null
secondary_topics: []
summary: null
triage: null
skip_reason: null
source: fireworks
url: https://fireworks.ai/blog/sdxl-ssd-1b-image-to-image-controlnet
author: null
published: '2023-11-02'
fetched: '2026-10-23T06:12:06Z'
classifier: null
taxonomy_rev: 2
words: 646
content_sha256: d5b398bd378af70ec7356ec2eca77105e479d8417ef4fb9e2916ddfe1674d563
---

# SDXL and SSD-1B Image-to-Image and ControlNet API | Fireworks

![](https://fireworks.ai/_next/image?url=https%3A%2F%2Fcdn.sanity.io%2Fimages%2Fpv37i0yn%2Fhorizon%2F4d5a265fb9eebfe8792c59ae5d285f50fc7ffef1-1024x549.png%3Fauto%3Dformat&w=3840&q=75)

The Fireworks.ai blazing-fast inference platform enables developers to build with generative AI to accelerate product innovation.

We are thrilled to announce a set of comprehensive features available through our image generation APIs. These new features will empower generative AI developers to take their image-generation apps to the next level:

- Blazing-Fast Image Generation
- Image-to-Image Generation
- ControlNet Support
- Native Resolutions
- Safety Checker
- Cost-Effective Pricing

**Try out the new features in the** [Fireworks console](https://fireworks.ai/models/fireworks/stable-diffusion-xl-1024-v1-0)!

**Try our** [API](https://docs.fireworks.ai/getting-started/quickstart)!

### Blazing-Fast Image Generation

We are excited to introduce Segmind Stable Diffusion 1B (SSD-1B) to the Fireworks.ai inference platform. SSD-1B, released by Segmind, is one of the fastest diffusion-based text-to-image models available today. We are making it accessible to all our users via our fast inference platform with unprecedented image generation performance. **It’s now possible to generate 1024x1024 images in 30 steps in just 1 second!**

Try out the SSD-1B model in the [**Fireworks console**](https://fireworks.ai/models/fireworks/SSD-1B)!

### Image-to-Image

The Image-to-Image functionality can be used to transform photos with text prompts. To use it, provide an image description, a negative prompt (optional), and an initial image.

Here is a step-by-step example of how to use [**SDXL on the console**](https://fireworks.ai/models/fireworks/stable-diffusion-xl-1024-v1-0):

**Step 1:** Use the following text prompt: “*Fennec Fox Van Gogh, cartoon, purple, vibrant painting, fantasy concept*”.

**Step 2:** Leave “Negative Prompt” empty for now and don’t set any LoRA Adapter.

**Step 3:** Click on the image-to-image option under “Additional Conditioning” and upload the following image:

![](https://fireworks.ai/_next/image?url=https%3A%2F%2Fcdn.sanity.io%2Fimages%2Fpv37i0yn%2Fhorizon%2F510c97fdf8933043b7fdd1e1e91adf14fbcea940-480x640.webp%3Fauto%3Dformat&w=3840&q=75)

**Step 4:** Click on the “Generate Image” option. Here are a few generations obtained using the default parameters.

![](https://fireworks.ai/_next/image?url=https%3A%2F%2Fcdn.sanity.io%2Fimages%2Fpv37i0yn%2Fhorizon%2F48d9cb17fbbe07e4fdcb5e84ae8420478462377f-480x640.webp%3Fauto%3Dformat&w=3840&q=75)

![](https://fireworks.ai/_next/image?url=https%3A%2F%2Fcdn.sanity.io%2Fimages%2Fpv37i0yn%2Fhorizon%2F7f58b8bf0bd5a7d38c84f9ed475d6005c0d7ed5f-480x640.webp%3Fauto%3Dformat&w=3840&q=75)

![](https://fireworks.ai/_next/image?url=https%3A%2F%2Fcdn.sanity.io%2Fimages%2Fpv37i0yn%2Fhorizon%2Fbac4509f224314c89f9e1b417684e39fd3e1335c-480x640.webp%3Fauto%3Dformat&w=3840&q=75)

This is a lot of fun! Feel free to play with the console by creating an account, and learn more about image-to-image generation from our [**API reference**](https://docs.fireworks.ai/api-reference/generate-a-new-image-from-an-image).

### ControlNet

The SSD-1B and SDXL models also now support using ControlNet to generate images using a provided image as guidance.

Let’s use the same original image above to guide the generation of the SDXL example above. You can follow the same steps as before but now you set “Additional Conditioning” as “ControlNet” and upload the image. Here are a few of our own generations:

![](https://fireworks.ai/_next/image?url=https%3A%2F%2Fcdn.sanity.io%2Fimages%2Fpv37i0yn%2Fhorizon%2Fc481f460faeddcc509ba59049b7b488ff89a0590-480x640.webp%3Fauto%3Dformat&w=3840&q=75)

![](https://fireworks.ai/_next/image?url=https%3A%2F%2Fcdn.sanity.io%2Fimages%2Fpv37i0yn%2Fhorizon%2Fd2dd5e57763aa1be8efd8eda8bc7b0bee54c970d-480x640.webp%3Fauto%3Dformat&w=3840&q=75)

![](https://fireworks.ai/_next/image?url=https%3A%2F%2Fcdn.sanity.io%2Fimages%2Fpv37i0yn%2Fhorizon%2F1bb2fe59bd042dc33359843e3c53b381f6f7ea37-480x640.webp%3Fauto%3Dformat&w=3840&q=75)

There is still more room for experimenting but you can see that the generated image is now much closer to the original image, all possible with the ControlNet support.

Learn more about ControlNet support for SDXL via our [**API reference**](https://docs.fireworks.ai/api-reference/generate-a-new-image-using-controlnet-with-provided-image-as-a-guidance).

### Native Resolutions

The text-to-image feature now supports nine different resolutions of various aspect ratios: (1024, 1024), (1152, 896), (896, 1152), (1216, 832), (832, 1216), (1344, 768), (768, 1344), (1536, 640), and (640, 1536). In addition, you can also specify the return type to be either `PNG` or `JPEG`.

### Safety Checker

It’s fun to develop with these image generation models but it’s important to also think about safety when developing with generative AI. To address this, we also now support enabling a safety check in the API for content filtering.

Enable *safety\_check: true* in the API to run an unsafe content detection network on generated images. Unsafe images are blacked out and a CONTENT\_FILTERED finish reason is returned.

To demonstrate how the safety check works, below is a sample code snippet that demonstrates how to use the [**Fireworks.ai Python client**](https://docs.fireworks.ai/getting-started/quickstart) to generate images with the safety check enabled. Make sure to include your own `FIREWORKS_API_KEY` and set `safety_check=True`.

`pythonCopy`
12345678910111213141516171819202122232425262728

**Try out the features in the** [Fireworks console](https://fireworks.ai/models/fireworks/stable-diffusion-xl-1024-v1-0)!

**Try our** [API](https://docs.fireworks.ai/getting-started/quickstart)!

### Billing

We’ve also introduced our [**competitive cost-effective pricing**](https://fireworks.ai/pricing) for using the image-generation models. Check it out and hit us up with any questions.

### Closing Words

We’re amped to see how developers use these new features to accelerate product innovation and creative applications with the advanced image-generation capabilities of SSD-1B and SDXL on the Fireworks inference platform.

🗣 Join our community on [**Discord**](https://discord.gg/gJ3B6UVrjA).

🎆 Learn more about the [**Fireworks Generative AI platform**](https://fireworks.ai/blog/fireworks-ai-fast-affordable-customizable-gen-ai-platform-7205c4559fe8).
