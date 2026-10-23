---
title: 'Stable Diffusion 3 API: Generate Images With Python | Fireworks'
kind: blog
topic: null
subtopic: null
secondary_topics: []
summary: null
triage: null
skip_reason: null
source: fireworks
url: https://fireworks.ai/blog/stable-diffusion-3-api-python
author: null
published: '2024-04-17'
fetched: '2026-10-23T06:12:18Z'
classifier: null
taxonomy_rev: 2
words: 1033
content_sha256: 1328c442635396ccd8ddf606569757e98290c827a28004c3c9bb368e9a20685b
---

# Stable Diffusion 3 API: Generate Images With Python | Fireworks

We are super excited to partner with [Stability AI](https://stability.ai/) in bringing the state-of-the-art image generation models [Stable Diffusion 3 (SD3) and Stable Diffusion Turbo (SD3-turbo)](https://stability.ai/news/stable-diffusion-3-api) to the market with Fireworks’ enterprise-grade distributed inference service.

Stable Diffusion is a cutting-edge deep-learning model that generates high-quality images from textual descriptions. By leveraging the power of latent diffusion, it enables users to create stunning visual content with unprecedented ease and flexibility.

Stable Diffusion 3 improvements upon the previous version:

- Stable Diffusion 3 outperforms state-of-the-art text-to-image generation systems such as DALL·E 3, Midjourney v6, and Ideogram v1 in typography and prompt adherence, based on human preference evaluations.
- With the new Multimodal Diffusion Transformer (MMDiT) architecture, Stable Diffusion 3 improves upon text understanding and spelling capabilities compared with previous architectures.

We benchmarked Stable Diffusion 3 with our distributed inference stack and achieved an impressive speed of 3.8 seconds per image at a resolution of 1024x1024. Additionally, we can launch an enterprise deployment with speeds optimized up to 1.8 seconds per image.

Meanwhile, SD3-turbo improves efficiency further, processing high-resolution images of the same resolution at a speed of 0.37 seconds per image.

![A whimsical and creative image depicting a hybrid creature that is a mix of a waffle and a hippopotamus. This imaginative creature features the distinctive, bulky body of a hippo, but with a texture and
appearance resembling a golden-brown, crispy waffle. The creature might have elements like waffle squares across its skin and a syrup-like sheen. It’s set in a surreal environment that playfully combines a
natural water habitat of a hippo with elements of a breakfast table setting, possibly including oversized utensils or plates in the background. The image should evoke a sense of playful absurdity and culinary
fantasy A whimsical and creative image depicting a hybrid creature that is a mix of a waffle and a hippopotamus. This imaginative creature features the distinctive, bulky body of a hippo, but with a texture and
appearance resembling a golden-brown, crispy waffle. The creature might have elements like waffle squares across its skin and a syrup-like sheen. It’s set in a surreal environment that playfully combines a
natural water habitat of a hippo with elements of a breakfast table setting, possibly including oversized utensils or plates in the background. The image should evoke a sense of playful absurdity and culinary
fantasy](https://fireworks.ai/_next/image?url=https%3A%2F%2Fcdn.sanity.io%2Fimages%2Fpv37i0yn%2Fhorizon%2Fa051317d5e027946266a6fd1c96e2c4ea856b299-1024x1024.jpg%3Fauto%3Dformat&w=3840&q=75)

*A whimsical and creative image depicting a hybrid creature that is a mix of a waffle and a hippopotamus. This imaginative creature features the distinctive, bulky body of a hippo, but with a texture and appearance resembling a golden-brown, crispy waffle. The creature might have elements like waffle squares across its skin and a syrup-like sheen. It’s set in a surreal environment that playfully combines a natural water habitat of a hippo with elements of a breakfast table setting, possibly including oversized utensils or plates in the background. The image should evoke a sense of playful absurdity and culinary fantasy*

![image1.png image1.png](https://fireworks.ai/_next/image?url=https%3A%2F%2Fcdn.sanity.io%2Fimages%2Fpv37i0yn%2Fhorizon%2F3de7b49d90dce05824a469deab3ca6bdb0a888da-1024x1024.png%3Fauto%3Dformat&w=3840&q=75)

*An entire universe inside a bottle sitting on the shelf at walmart on sale.*

![image4.jpg image4.jpg](https://fireworks.ai/_next/image?url=https%3A%2F%2Fcdn.sanity.io%2Fimages%2Fpv37i0yn%2Fhorizon%2F9f5a0bfee4b25147b3eb5839f09d19d4ad0c1771-1024x1024.jpg%3Fauto%3Dformat&w=3840&q=75)

*human life depicted entirely out of fractals*

*A cheeseburger surfing the vibe wave at night*

![image7.jpg image7.jpg](https://fireworks.ai/_next/image?url=https%3A%2F%2Fcdn.sanity.io%2Fimages%2Fpv37i0yn%2Fhorizon%2Fdc090b7193ce691ab7142bf668cb45c382e63407-1600x1201.jpg%3Fauto%3Dformat&w=3840&q=75)

*A Llama reaching a road sign that says stable diffusion has arrived*

## The Fireworks Promise

At Fireworks, our mission is democratizing AI for developers and businesses, serving the best of language and image models at the fastest speeds and highest reliably.

Today, we provide companies like Quora, Sourcegraph, Upstage, Tome, and Anysphere with industry-leading inference speed and quality for production use cases across image and text generation.

In this blog, we will explain how you can quickly access the Stable Diffusion 3 (SD3) model via the API using Python. By the end of this tutorial, you will be able to understand the new SD3 API and incorporate it into your production workloads.

## Prerequisites:

Before diving into further, make sure you have the following:

- Python 3.7 or higher installed
- [API Key](https://platform.stability.ai/account/keys) from Stability AI
- Basic knowledge of Python and API usage

## Set Up Your Environment

To get started, create a new Python file and import the necessary libraries:

`pythonCopy`
123

## Authenticate with the Stable Diffusion 3 API

To access the Stable Diffusion 3 API, you’ll need to authenticate using your [API key](https://platform.stability.ai/account/keys).

Replace `YOUR_API_KEY` with your actual API key:

`pythonCopy`
12

## Generate an Image

To generate an image using Stable Diffusion 3, you need to provide a text prompt that describes the desired image. Here’s an example of how to make an API request to generate an image:

`pythonCopy`
123456789101112131415161718192021

![image2.jpg image2.jpg](https://fireworks.ai/_next/image?url=https%3A%2F%2Fcdn.sanity.io%2Fimages%2Fpv37i0yn%2Fhorizon%2Fa80d1de0ead4498552ba01f585b56a645817377c-1024x1024.jpg%3Fauto%3Dformat&w=3840&q=75)

*smiling cartoon dog sits at a table, coffee mug on hand, as a room goes up in flames. “This is fine,” the dog assures himself*

In this example, we specify the `prompt` as “‘smiling cartoon dog sits at a table, coffee mug on hand, as a room goes up in flames. “This is fine,” the dog assures himself” to generate an image that is descriptive of a final product with symbolic association with the word fireworks. We also set ‘aspect\_ratio’to “16:9” and `negative_prompt` to avoid blurry or distorted images.

## Explore Additional Parameters

Stable Diffusion 3 offers various parameters to customize the image generation process. Some commonly used parameters include:

- `Accept`: You can include either `image/jpeg` or `image/png` for generating the corresponding image type.
- `aspect_ratio`: The proportion of width to height in the output image. While the default is `1:1`, aspect ratio also supports `16:9`, `21:9` `2:3`, `3:2`, `4:5`, `5:4`, `9:16`, `9:21`.
- `seed`: Random seed for generating consistent results (default: 0). Seed can vary between `0` to `4294967294`. `0` will result in using a randomly selected seed.

Feel free to experiment with these parameters to achieve different styles and variations in your generated images.

## Wrapping up

Stable Diffusion 3 is a powerful tool for generating stunning images from textual prompts. By following the steps outlined in this blog post and leveraging the provided code examples, you can easily integrate Stable Diffusion 3 into your projects and start creating amazing AI-generated art.

If you have more questions or feedback, please reach out via our [Discord](https://discord.gg/mMqQxvFD9A) to chat directly with the team. We’re excited to see what you build!
