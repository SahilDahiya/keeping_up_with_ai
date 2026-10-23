---
title: 'FLUX.1 Kontext Pro vs Max: Image Editing Models | Fireworks'
kind: blog
topic: null
subtopic: null
secondary_topics: []
summary: null
triage: null
skip_reason: null
source: fireworks
url: https://fireworks.ai/blog/flux-1-kontext-pro-max
author: null
published: '2025-07-09'
fetched: '2026-10-23T06:13:36Z'
classifier: null
taxonomy_rev: 2
words: 376
content_sha256: 1b9cfc74f304001a50fb7748038e4777dcc9275def92cb7923af5841085872f5
---

# FLUX.1 Kontext Pro vs Max: Image Editing Models | Fireworks

We’re excited to bring **FLUX.1 Kontext**, a suite of generative flow matching models that can generate and edit images, to Fireworks. Unlike the text-to-image models, the FLUX.1 Kontext family can perform in-context image generation, allowing you to prompt with both text and images, and seamlessly extract and modify visual concepts to produce new, coherent renderings.

## What is FLUX.1 Kontext?

FLUX.1 Kontext models are developed by [Black Forest Labs](https://bfl.ai/models/flux-kontext) (BFL) and mark a significant expansion of classic text-to-image models by unifying instant text-based image editing and text-to-image generation. As a multimodal flow model, it combines state-of-the-art character consistency, context understanding and local editing capabilities with strong text-to-image synthesis.

As part of the FLUX.1 Kontext suite, we bring two new in-context image models to the Fireworks API:

- [FLUX.1 Kontext Pro](https://app.fireworks.ai/models/fireworks/flux-kontext-pro)
  - Support local editing, generative in-context modifications and classic text-to-image generation.
  - Handle both text and reference images as inputs and enable precise region edits and full-scene transformations.
  - Maintains style, characters, identities across multiple editing turns and distinctive features consistent across different scenes and viewpoints.
- [FLUX.1 Kontext Max](https://app.fireworks.ai/models/fireworks/flux-kontext-max)
  - Kontext Max is the new experimental model from BFL.
  - Greatly improves prompt adherence and typography generation, and high consistency for editing without compromise on speed.

## The Core Capabilities of FLUX.1 Kontext

##### **Character Consistency**

Kontext can preserve unique elements of an image, such as a reference character or object in a picture, across multiple scenes and environments.

##### **Local Editing**

Kontext can also make targeted modifications of specific elements in an image without affecting the rest. For example, you can change the text while preserving the others in the image.

##### **Style References**

Kontext can generate novel scenes while preserving unique styles from a reference image, directed by text prompts.

## Try It on Fireworks

Ready to start building with FLUX.1 Kontext?

- Build with Fireworks API: You can get started right away using our simple and production-ready [API](https://fireworks.ai/docs/api-reference/generate-or-edit-image-using-flux-kontext).
- Use Fireworks Playground: Visit our UI playground to try [FLUX.1 Kontext Pro](https://app.fireworks.ai/playground?model=accounts/fireworks/models/flux-kontext-pro) and [FLUX.1 Kontext Max](https://app.fireworks.ai/playground?model=accounts/fireworks/models/flux-kontext-max) instantly.
- Join Our Community: Join our [Discord channel](https://discord.gg/fireworks-ai) to connect with other developers and the Fireworks team.

Contact us: [Reach out](https://fireworks.ai/company/contact-us) to discuss how we can help you leverage FLUX.1 Kontext for your specific use cases.
