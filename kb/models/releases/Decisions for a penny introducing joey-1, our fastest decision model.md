---
title: 'Decisions for a penny: introducing joey-1, our fastest decision model'
kind: blog
topic: models
subtopic: releases
secondary_topics:
- inference/optimization
summary: Baseten introduces joey-1, a 2B-parameter decision model post-trained from
  Qwen3.5-2B that returns a label and calibrated probability in a single token instead
  of generating text, hitting 20ms P50 latency and $0.01/M tokens, 5x faster than
  its 9B sibling elephant-1 and a tenth the cost of the 27B mammoth-1.
triage: null
skip_reason: null
source: baseten
url: https://www.baseten.co/blog/decisions-for-a-penny-introducing-joey-1/
author: Max Kirkby; Charles O'Neill
published: '2026-10-29'
fetched: '2026-10-30T06:07:38Z'
classifier: claude
taxonomy_rev: 2
words: 685
content_sha256: ee9d9c15b0e2e5bf9a09d8d28bc8e9430ab51553d1ac7776ff44c9a48db73d9d
---

# Decisions for a penny: introducing joey-1, our fastest decision model

### Published

![joey-1](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1793290906-li-image_joey-1-1.png%3Fauto%3Dformat%26fit%3Dcrop%26h%3D630%26w%3D1200&w=3840&q=100)

Eight days ago we released mammoth-1 (27B) and elephant-1 (9B), the #1-ranked decision models. Today we’re adding joey-1 (2B), our fastest and most affordable decision model, with a P50 latency of 20 ms, 5x faster than comparable decision model models.

Many LLM use cases don’t need generated text; they need decisions:

- Where should this ticket go?
- Should this message be flagged?
- Should this request be approved?

LLMs have historically answered these by generating text, which adds cost and latency to every call, and that overhead compounds with each decision in a chain. Decision models return the answer directly as a single token and a calibrated probability score, drastically reducing cost and latency.

LLMs now come in many shapes and sizes, from full-scale models to flash and fast variants, because every workload weighs intelligence, speed, and cost differently. Decision models should too. With joey-1, the Base Labs decision model family now spans three sizes. At release, each is among the most capable models in its weight class, accepts text and images, and is built to be cost-efficient and low-latency.

In our internal testing (details coming soon), joey-1 is the strongest decision model with 3B or fewer parameters. At production scale, joey-1 serves the average 2,000-token request at a P50 end-to-end latency of 20 ms, about 2.5x faster than elephant-1 (49 ms). At $0.01 per million tokens, it also costs a tenth of mammoth-1.

Our research and post-training teams will keep improving these models and expanding the family, so you’ll have the right model for every decision you need to make. joey-1 is available now on Baseten Model APIs, with open weights on [Hugging Face](https://huggingface.co/baselabs/joey-1).

## **Should this LLM workload be a decision model?** 

A decision model returns a label (a decision) and a confidence score for that label in one forward pass. For joey-1 specifically, it’s worth moving an LLM workload when:

- **Decision volume is high**, so cost per call decides whether the project is economic.
- **The decision you need to make is a requisite for something else**, meaning its latency is added to every response.

For context, classifying 10 million support tickets a month at \~500 tokens each is 5 billion tokens, which is about $50 a month on joey-1 versus $500 on mammoth-1. joey-1 is a solid first-line model to keep workloads fast and cost-efficient, while you can still use heavier models like elephant-1 or mammoth-1 as an escalation path when joey-1 is uncertain.

## **The Base Labs decision model family**

All three models are trained by Base Labs on the same data mixture and share the same API, so moving between them is a one-line change. That makes the family a single toolkit rather than three separate choices: mammoth-1 for the decisions where accuracy matters most, elephant-1 as the balanced default, and joey-1 for high-volume, latency-sensitive calls where speed and cost come first.

These models are built to improve over time. Base Labs, our in-house research lab, continuously releases refreshed weights and new capabilities under the same API. Each release launches on Baseten Model APIs, optimized by our model performance team for high throughput and cost-efficient inference, so your workloads benefit from every improvement with no integration changes required.

![Artificial Analysis (Internal Replica)](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1793293253-artificial-analysis-internal-replica.png%3Fauto%3Dformat%26w%3D1200&w=3840&q=75) Artificial Analysis (Internal Replica)

## **From Model APIs to your own weights** 

joey-1 is post-trained from Qwen3.5-2B by [Base Labs](https://labs.baseten.co/), our research lab, using the same data and recipe as elephant-1 and mammoth-1 with Baseten Training Jobs.

All three models are available on Model APIs and as dedicated deployments. On Model APIs, the models support a 16k context window and are optimized for low-latency workloads.

Dedicated deployments unlock the full 262k context window, support fine-tuned weights, and can deliver even faster TTFT and TPS through workload-specific optimizations and co-location with your LLM workloads.

To create your own fine-tuned weights, elephant-1 and joey-1 are available for post-training on Training Jobs. Get started with our [fine-tuning cookbook](https://github.com/basetenlabs/ml-cookbook/tree/main/training-jobs/examples/joey-1-sft/training).

## **Try joey-1**

joey-1 is live on Baseten Model APIs with zero data retention by default, and the weights are open on [Hugging Face](https://huggingface.co/baselabs/joey-1). Jump on it.
