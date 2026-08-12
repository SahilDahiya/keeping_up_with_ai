---
title: Getting Started with Stability’s API Powered by Fireworks
kind: blog
topic: null
subtopic: null
secondary_topics: []
summary: null
triage: null
skip_reason: null
source: fireworks
url: https://fireworks.ai/blog/sd3-api-powered-by-fireworks
author: null
published: '2024-04-17'
fetched: '2026-08-12T06:28:47Z'
classifier: null
taxonomy_rev: 2
words: 790
content_sha256: 8fcea2273942b9d856cb0ef6560a0d44c351fbf7b1faa39de3384156e05c2666
---

# Getting Started with Stability’s API Powered by Fireworks

We are super excited to partner with [Stability AI](https://stability.ai/) in bringing the state-of-the-art image generation models [Stable Diffusion 3 (SD3) and Stable Diffusion Turbo (SD3-turbo)](https://stability.ai/news/stable-diffusion-3-api) to the market with Fireworks’ enterprise-grade distributed inference service.

Stable Diffusion is a cutting-edge deep-learning model that generates high-quality images from textual descriptions. By leveraging the power of latent diffusion, it enables users to create stunning visual content with unprecedented ease and flexibility.

Stable Diffusion 3 improvements upon the previous version:

- •Stable Diffusion 3 outperforms state-of-the-art text-to-image generation systems such as DALL·E 3, Midjourney v6, and Ideogram v1 in typography and prompt adherence, based on human preference evaluations.
- •With the new Multimodal Diffusion Transformer (MMDiT) architecture, Stable Diffusion 3 improves upon text understanding and spelling capabilities compared with previous architectures.

We benchmarked Stable Diffusion 3 with our distributed inference stack and achieved an impressive speed of 3.8 seconds per image at a resolution of 1024x1024. Additionally, we can launch an enterprise deployment with speeds optimized up to 1.8 seconds per image.

Meanwhile, SD3-turbo improves efficiency further, processing high-resolution images of the same resolution at a speed of 0.37 seconds per image.

*A whimsical and creative image depicting a hybrid creature that is a mix of a waffle and a hippopotamus. This imaginative creature features the distinctive, bulky body of a hippo, but with a texture and appearance resembling a golden-brown, crispy waffle. The creature might have elements like waffle squares across its skin and a syrup-like sheen. It’s set in a surreal environment that playfully combines a natural water habitat of a hippo with elements of a breakfast table setting, possibly including oversized utensils or plates in the background. The image should evoke a sense of playful absurdity and culinary fantasy*

*An entire universe inside a bottle sitting on the shelf at walmart on sale.*

*human life depicted entirely out of fractals*

*A cheeseburger surfing the vibe wave at night*

*A Llama reaching a road sign that says stable diffusion has arrived*

At Fireworks, our mission is democratizing AI for developers and businesses, serving the best of language and image models at the fastest speeds and highest reliably.

Today, we provide companies like Quora, Sourcegraph, Upstage, Tome, and Anysphere with industry-leading inference speed and quality for production use cases across image and text generation.

In this blog, we will explain how you can quickly access the Stable Diffusion 3 (SD3) model via the API using Python. By the end of this tutorial, you will be able to understand the new SD3 API and incorporate it into your production workloads.

Before diving into further, make sure you have the following:

- •Python 3.7 or higher installed
- •[API Key](https://platform.stability.ai/account/keys) from Stability AI
- •Basic knowledge of Python and API usage

To get started, create a new Python file and import the necessary libraries:

123

To access the Stable Diffusion 3 API, you'll need to authenticate using your [API key](https://platform.stability.ai/account/keys).

Replace `YOUR_API_KEY` with your actual API key:

12

To generate an image using Stable Diffusion 3, you need to provide a text prompt that describes the desired image. Here's an example of how to make an API request to generate an image:

123456789101112131415161718192021

*smiling cartoon dog sits at a table, coffee mug on hand, as a room goes up in flames. “This is fine,” the dog assures himself*

In this example, we specify the `prompt` as "'smiling cartoon dog sits at a table, coffee mug on hand, as a room goes up in flames. “This is fine,” the dog assures himself" to generate an image that is descriptive of a final product with symbolic association with the word fireworks. We also set 'aspect_ratio'to "16:9” and `negative_prompt` to avoid blurry or distorted images.

Stable Diffusion 3 offers various parameters to customize the image generation process. Some commonly used parameters include:

- •`Accept` : You can include either`image/jpeg` or`image/png` for generating the corresponding image type.
- •`aspect_ratio` : The proportion of width to height in the output image. While the default is`1:1` , aspect ratio also supports`16:9` ,`21:9``2:3` ,`3:2` ,`4:5` ,`5:4` ,`9:16` ,`9:21` .
- •`seed` : Random seed for generating consistent results (default: 0). Seed can vary between`0` to`4294967294` .`0` will result in using a randomly selected seed.

Feel free to experiment with these parameters to achieve different styles and variations in your generated images.

Stable Diffusion 3 is a powerful tool for generating stunning images from textual prompts. By following the steps outlined in this blog post and leveraging the provided code examples, you can easily integrate Stable Diffusion 3 into your projects and start creating amazing AI-generated art.

If you have more questions or feedback, please reach out via our [Discord](https://discord.gg/mMqQxvFD9A) to chat directly with the team. We’re excited to see what you build!
