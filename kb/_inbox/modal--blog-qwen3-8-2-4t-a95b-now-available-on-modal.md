---
title: Qwen3.8-2.4T-A95B now available on Modal | Modal Blog
kind: blog
topic: null
subtopic: null
secondary_topics: []
summary: null
triage: null
skip_reason: null
source: modal
url: https://modal.com/blog/qwen3-8-2-4t-a95b-now-available-on-modal
author: null
published: '2026-08-12'
fetched: '2026-08-13T06:30:00Z'
classifier: null
taxonomy_rev: 2
words: 196
content_sha256: ea46efb27e9b95c118f92e8e1470400553d00f872def8ede0e0ce8906da7e3d3
---

# Qwen3.8-2.4T-A95B now available on Modal | Modal Blog

[Back](https://modal.com/blog)

# Qwen3.8-2.4T-A95B now available on Modal

[Qwen3.8-2.4T-A95B](https://modal.com/library/qwen/qwen3-8-max) just launched as an open weights model, and it’s now available on Modal. 

Over Qwen 3.7, the latest model sees substantial improvement across coding, work, research, and long-horizon tasks.

We worked with Qwen ahead of the drop to bring day zero support to Modal Auto Endpoints, backed by SGLang and a custom [DFlash](https://z-lab.ai/projects/dflash/) speculator tuned to Qwen3.8’s shape.

[Try it out now](https://modal.com/endpoints?model=Qwen%2FQwen3.8-2.4T-A95B&type=shared) as a Shared Endpoint.

![](https://modal-cdn.com/cdnbot/qwen38benchmarksybym6za3_1c337e41.webp) 

## Speeding up inference with custom DFlash speculation

Just getting the model running is one thing, making it fast is another. For this, we once again turn to a DFlash speculator model because—say it with us now—[Speculation is all you need](https://modal.com/blog/spec-is-all-u-need).

A speculator only earns its keep when the target accepts the tokens it drafts, and acceptance comes down to whether the drafter has seen sequences like the ones it's predicting. Because of Max’s improvements in coding, research, and work (things that tend to use more tool calls) we leaned into that in our training data to increase accepts.

### Try it now

Qwen3.8-2.4T-A95B (text only) is available for the next month as an OpenAI compatible Shared Endpoint with token-based pricing.
