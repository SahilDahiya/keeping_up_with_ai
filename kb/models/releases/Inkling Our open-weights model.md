---
title: 'Inkling: Our open-weights model'
kind: blog
topic: models
subtopic: releases
secondary_topics:
- industry/announcements
summary: 'Simon Willison covers Thinking Machines Lab''s first open-weights release,
  Inkling: a 975B-parameter (41B active) Apache-2.0 MoE transformer trained on 45T
  multimodal tokens, positioned as a fine-tuning base for their Tinker platform rather
  than a frontier model, plus a promised smaller Inkling-Small variant.'
triage: null
skip_reason: null
source: simon-willison
url: https://simonwillison.net/2026/Jul/16/inkling/
author: Simon Willison
published: '2026-07-16'
fetched: '2026-07-17T06:52:40Z'
classifier: claude
taxonomy_rev: 2
words: 668
content_sha256: faa8ee2ffa455d822f5eee91e6dba0bf56ebe496da625089343f7d5a47692665
---

# Inkling: Our open-weights model

16th July 2026 - Link Blog

** Inkling: Our open-weights model** (

[via](https://news.ycombinator.com/item?id=48924912)) Mira Murati's Thinking Machines Lab just released their first open-weights model. Inkling is "a Mixture-of-Experts transformer with 975B total parameters, 41B active" - an Apache-2.0 licensed multimodal model trained on 45 trillion tokens of text, images, audio and video.

They're also promising Inkling-Small, a 276B (12B active) model, but that's still being tested and the weights will be released "once that work is complete".

The [model card](https://thinkingmachines.ai/model-card/inkling/) is much shorter than I've come to expect from US AI labs. It links to even shorter [Training Data Documentation](https://thinkingmachines.ai/training-data-documentation/) with almost nothing of interest in it - it's best summarized by these two paragraphs:

The datasets Thinking Machines Lab uses to develop its AI services includes content that is in the public domain as well as content that may be subject to intellectual property protection.

Thinking Machines Lab’s services were developed using publicly available content obtained from the open internet and publicly accessible data repositories. Certain datasets were also obtained from third parties.


By Thinking Machines' own admission, this is not a frontier model. It's instead intended as a strong base model for fine-tuning using their own [Tinker training platform](https://thinkingmachines.ai/tinker/):

Inkling is not the strongest overall model available today, open or closed. Instead, a combination of qualities makes it a good open-weights base for customization: multimodal capabilities, efficient thinking, and availability on Tinker for fine-tuning.


There's a lot to like about this release. It's Apache-2.0 licensed, and looks competitive with the open weight models coming out of China - it's good to see the US open weights ecosystem gain a new viable contender to join NVIDIA Nemotron and Gemma 4.

Here's its attempt at an SVG pelican riding a bicycle, which I generated using this `curl` command against the Thinking Machines API:

```
curl "https://tinker.thinkingmachines.dev/services/tinker-prod/oai/api/v1/chat/completions" \
  -H "Authorization: Bearer $TINKER_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "thinkingmachines/Inkling",
    "messages": [
      {"role": "user", "content": "Generate an SVG of a pelican riding a bicycle"}
    ],
    "stream": false
  }'
```
Full [response here](https://gist.github.com/simonw/8117ac4376371dd3fc2b5dbce27e0855).

![See image description below](https://static.simonwillison.net/static/2026/inkling-pelican.jpg)


Since it's a multi-modal model I had it describe its own image (after I rendered it to a JPEG) by sending this JSON:

```
{
  "model": "thinkingmachines/Inkling",
  "messages": [{
    "role": "user",
    "content": [
      {"type": "image_url", "image_url": {"url": "data:image/jpeg;base64,$BASE_64_JPEG"}},
      {"type": "text", "text": "Describe this image in detail"},
    ],
  }],
  "stream": false
}
```
Here's [the full response](https://gist.github.com/simonw/dccebd0581f5c4056c5b0ca5bdc38cd9#reasoning_content). It thought it had drawn a "stork or seagull":

This is a cheerful, flat-vector cartoon illustration featuring a white bird riding a bicycle across a green landscape.


The Bird:The central figure is a stylized white bird—resembling a stork or seagull—with a plump, rounded body. It has a long, prominent orange beak that is slightly open, revealing a black line for the mouth. Its eye is small and black with a tiny white highlight. The bird has black wing and tail feathers with white edges, and thin orange legs ending in black feet that rest on the bicycle's orange pedals.

The Bicycle:The bike has a simple black frame with two large wheels featuring black tires, gray inner rims, and black spokes arranged in a cross pattern. The handlebars are black, and there are bright orange pedals attached to a black crank. A white seat is visible behind the bird's body.

The Setting:The scene is set against a clear, light blue sky. There are two fluffy white clouds—one on the left side and a smaller one near the bird's head on the right. A bright, solid yellow sun shines in the upper right corner. At the bottom, there are rolling green hills with a smooth, curved top edge where the bicycle rests.The overall style is playful, simple, and colorful, with clean lines and a bright, sunny atmosphere.


## Recent articles

- [Kimi K3, and what we can still learn from the pelican benchmark](https://simonwillison.net/2026/Jul/16/kimi-k3/)- 16th July 2026
- [The new GPT-5.6 family: Luna, Terra, Sol](https://simonwillison.net/2026/Jul/9/gpt-5-6/)- 9th July 2026
- [sqlite-utils 4.0, now with database schema migrations](https://simonwillison.net/2026/Jul/7/sqlite-utils-4/)- 7th July 2026
