---
title: 'Fireworks f1: Compound AI Model for Complex Reasoning | Fireworks'
kind: blog
topic: null
subtopic: null
secondary_topics: []
summary: null
triage: null
skip_reason: null
source: fireworks
url: https://fireworks.ai/blog/f1-compound-ai-reasoning-model
author: null
published: '2024-11-15'
fetched: '2026-10-23T06:13:48Z'
classifier: null
taxonomy_rev: 2
words: 539
content_sha256: c74a822659ed058d27f756efac6e5773e9972c968f7d41c017a26e9817519f22
---

# Fireworks f1: Compound AI Model for Complex Reasoning | Fireworks

At Fireworks, we believe the future of AI is shifting to [compound AI systems](https://fireworks.ai/blog/fireworks-ai-series-b-compound-ai) that combine specialized models and tools to achieve better performance, reliability and control, compared to a single model.

However building compound AI systems is difficult and time-consuming, right from selecting and tuning different components to orchestrating how they work together. So earlier this year, we set out to simplify the process of building compound AI, with the goal of making compound AI as easy to use as prompting a model.

**Today, we’re releasing a first step in that direction. f1 is a compound AI model specialized in complex reasoning, that interweaves multiple open models at the inference layer.** Early testing has shown reasoning capabilities that match or exceed many closed frontier models as well as the best open models.

**f1 enables developers to access the power of compound AI with the simplicity of prompting.** f1 is designed with the idea of [declarative programming](https://en.wikipedia.org/wiki/Declarative_programming). Using prompt as the universal declarative programming language for Gen AI application building, developers can describe *what* they want to achieve via prompting, without needing to specify exactly *how* to accomplish it. We’ve shared some examples of using f1 through prompting later in this blog.

[\*\*f1](https://fireworks.ai/models/fireworks/f1-preview/playground) and [f1-mini](https://fireworks.ai/models/fireworks/f1-mini-preview/playground) (a smaller, faster variant) are now available in preview with free access on Fireworks Playground.\*\* **We’re also [inviting applications](https://forms.gle/UZYbnhAioT7fSeFf7) for early access to the f1 API and design partnerships for use cases that require complex reasoning.**

We invite you to help us improve these models and shape the future of compound AI.

## f1 sets a new state of the art for complex reasoning with open models

f1 demonstrates strong capabilities across benchmarks focused on complex reasoning. On coding, chat, math and reasoning use cases, it surpasses the best open models and most closed frontier models. We will share more comprehensive benchmark results soon.

## Examples of f1’s capabilities

f1’s use of interleaved generation from multiple open models allows it to reason through a variety of complex reasoning tasks. Here are some examples:

### Math (AIME 2024 problem):

Every morning Aya goes for a $9$-kilometer-long walk and stops at a coffee shop afterwards. When she walks at a constant speed of $s$ kilometers per hour, the walk takes her 4 hours, including $t$ minutes spent in the coffee shop. When she walks $s+2$ kilometers per hour, the walk takes her 2 hours and 24 minutes, including $t$ minutes spent in the coffee shop. Suppose Aya walks at $s+\frac{1}{2}$ kilometers per hour. Find the number of minutes the walk takes her, including the $t$ minutes spent in the coffee shop.

### Math proof:

Is this statement correct - given any five points on the surface of a sphere, there is some closed hemisphere (i.e., including the boundary) that contains at least four of them.

### Coding:

Prompt:

Output:

### Logic puzzle:

Find, with proof, the maximum number of knights one can place on a chessboard such that no two of them attack each other.

Do the same for bishops

## Get started with f1

Access [f1](https://fireworks.ai/models/fireworks/f1-preview/playground) and [f1-mini](https://fireworks.ai/models/fireworks/f1-mini-preview/playground) in preview with free access now on Fireworks Playground. [Apply](https://forms.gle/UZYbnhAioT7fSeFf7) for early access to the f1 API and design partnerships for use cases that require complex reasoning.
