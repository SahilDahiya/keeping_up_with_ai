---
title: 'Code Llama Infilling: Generate Missing Code via API | Fireworks'
kind: blog
topic: null
subtopic: null
secondary_topics: []
summary: null
triage: null
skip_reason: null
source: fireworks
url: https://fireworks.ai/blog/code-llama-infilling-api
author: null
published: '2023-09-12'
fetched: '2026-10-23T06:13:56Z'
classifier: null
taxonomy_rev: 2
words: 402
content_sha256: cc7bfdfb55ccf830e7deda7f30bfe7685b6b5c97c4db25664424485b49708f53
---

# Code Llama Infilling: Generate Missing Code via API | Fireworks

**Llama 2 and Code Llama**

[Llama 2](https://ai.meta.com/llama/) is one of the latest open-source foundation large language models (LLMs) from Meta AI. [Code Llama](https://ai.meta.com/blog/code-llama-large-language-model-coding/) is a new family of code LLMs based on Llama 2 and specifically trained for code generation tasks. Code Llama achieves state-of-the-art performance on several code benchmarks when compared to other open models.

These code models support large input context, infilling capabilities, and instruction following for several programming tasks.

**Code Llama Infilling**

Code infilling is the task of predicting missing code that is consistent with the preceding and subsequent code blocks.

The 7B and 13B variants of Code Llama and Code Llama Instruction support infilling, which is important for practitioners as it enables the use of LLMs for features such as type inferencing or docstring generation.

But Code Llama infilling is tricky to use out of the box.

First, you must format your prompt properly and use proper whitespacing, especially for whitespace-meaningful languages such as Python. For instance, the model expects this format: `<PRE> {pre} <SUF>{suf} <MID>`. But you won’t get infilling if the last space isn’t added such as in `<PRE> {pre} <SUF>{suf}<MID>`. This user experience can be improved by having a standard interface that prevents these issues.

Second, we’ve noticed Code Llama base models are better than instruction models for the infilling task. Although instruction models are capable of infilling, it’s hard to have precise control over it.

**Infilling with the Fireworks API**

To improve the experience and make it easier to use code infilling, we now support Code Llama infilling with the [Fireworks API](https://fireworks.ai/)!

For Code LLama base models (currently `llama-v2-7b-code` and `llama-v2-13b-code` on Fireworks Platform), we’ve set up a default chat completion template capable of infilling.

We have simplified how to easily use Code Llama infilling with a convenient and familiar API. You simply pass a prefix and suffix, which represents the surrounding context, and ask the API to return the missing parts. It’s that simple!

In the example below we are prompting the model to generate the remaining code between the given comment (prefix) and the returned value (suffix):

![](https://fireworks.ai/_next/image?url=https%3A%2F%2Fcdn.sanity.io%2Fimages%2Fpv37i0yn%2Fhorizon%2F9be361c0092bf53364f1397799d630e90bb634c2-785x529.png%3Fauto%3Dformat&w=3840&q=75)

The code returned by the model properly completes the function to add two numbers:

![](https://fireworks.ai/_next/image?url=https%3A%2F%2Fcdn.sanity.io%2Fimages%2Fpv37i0yn%2Fhorizon%2F175046ccccf3f377ec9f4c59d9264d4c867cc85e-386x140.webp%3Fauto%3Dformat&w=3840&q=75)

Here is another more advanced example:

![](https://fireworks.ai/_next/image?url=https%3A%2F%2Fcdn.sanity.io%2Fimages%2Fpv37i0yn%2Fhorizon%2Fc5b1b4e326f9ab053e4eafdd08054ae315ea0e6c-720x501.webp%3Fauto%3Dformat&w=3840&q=75)

The actual code returned by the model is as follows:

![](https://fireworks.ai/_next/image?url=https%3A%2F%2Fcdn.sanity.io%2Fimages%2Fpv37i0yn%2Fhorizon%2F6e6775b47d3ab5d3b680c420f34cc0f6d6894215-650x243.webp%3Fauto%3Dformat&w=3840&q=75)

Check out our API to start using Code Llama infilling and other models like Llama 2 to build your products: [http://fireworks.ai/api](https://t.co/VUo8COTUih)
