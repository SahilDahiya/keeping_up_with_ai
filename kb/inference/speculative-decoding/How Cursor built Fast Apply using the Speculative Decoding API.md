---
title: How Cursor built Fast Apply using the Speculative Decoding API
topic: inference
subtopic: speculative-decoding
secondary_topics:
- agents/tool-use
summary: Case study of Cursor Fast Apply using speculative decoding to reduce coding-assistant
  latency.
source: fireworks
url: https://fireworks.ai/blog/cursor
author: null
published: '2024-06-23'
fetched: '2026-07-11T04:14:23Z'
classifier: codex
taxonomy_rev: 1
words: 853
content_sha256: 15b76453f7685bd02af6bf47a958c6181327a6b23210f464646e83f2560f308c
triage: keep
skip_reason: null
---

# How Cursor built Fast Apply using the Speculative Decoding API

TL;DR

- •Cursor leveraged Fireworks inference stack to achieve 1000 tok/sec.
- •Announcing new Speculative Decoding API, that enables users to speculate a larger number of tokens in parallel.

Millions of developers write code everyday to improve software systems at large bringing productivity to many business workflows, however, very few tools help them improve their own productivity.

With the advent of Generative AI, we see an emerging category of developer tooling built around Large Language Models (LLMs) especially for [code generation](https://fireworks.ai/blog/coding-copilot). Some popular tools in this regard are Github Copilot, Sourcegraph, Phind, Continue, Blackbox, Codeium, Cognition, Factory, Aider., the list goes on…

Among them is a standout product, [Cursor](http://cursor.com/). Cursor is an AI-native IDE that helps developers write better code faster. Their core features include:

- [Cursor’s Copilot++](https://cursor.com/cpp)is a more powerful AI-assistant which predicts your next edit taking in account of your recent change.
- Cmd/Ctrl-k, an instructed edit model that you can use to make changes to any region of code with natural language
- A chat that sees your whole codebase and can “instantly apply” the changes to your code.

Our mission at Fireworks is to assist developers building innovative and mission critical Generative AI experiences at enterprise scale. In this blog, we will go through how [Fireworks inference stack](https://fireworks.ai/blog/fireattention-v2-long-context-inference) enabled Cursor to achieve 1000 tokens per sec using our Speculative Decoding API with low latency.

There are many feature highlights in Cursor, but here are some that are making developers love them more.

Instantly applying the generated code to a file using a “Play” button.

Rewriting and making minute multi-line syntactic corrections to a snippet of code as developers write code like prose.

Cursor’s Copilot++ predicts your next cursor position so you can seamlessly navigate your code.

- •Fireworks Custom Model deployment for inference with performance optimizations for specific workload.
- •Fireworks Chat Completion and Completion API enabled with Speculative Decoding flag.

Frontier models like GPT-4 and GPT-4o struggle with large code edits, exhibiting issues such as laziness, inaccuracy, and high latency. These weaknesses are particularly evident in coding agents, where accurately editing hundreds of lines of code can require multiple model calls and lead to infinite loops or buggy outputs. The slow performance of existing models on large edits also disrupts programmers' workflow.

To address these challenges, Cursor has trained a specialized model on the "[fast apply](https://cursor.sh/blog/instant-apply)" task, which involves planning and applying code changes. The fast-apply model surpasses the performance of GPT-4 and GPT-4o, achieving speeds of ~1000 tokens/s (approximately 3500 char/s) on a 70b model.

The model is trained on a combination of synthetic data generated from CMD+K prompts and instant apply inputs. Fireworks deployed a custom trained “llama-70b-ft-spec” model on the inference engine using speculative decoding, enabling the model to generate speeds >1000 tokens/s.

In a regular LLM inference, every token depends on the context of the entire corpus of tokens generated previously. It is not possible to generate the n+1 token without the nth token.

Speculative Decoding enables parallelization of the token generation, enables users to speculate a larger number of tokens in parallel and consume them without deviating from the provided context.

Most LLM use cases have a wide variety of possible inputs which makes it hard to produce good speculations. Usually one trains a [separate “draft” model (or adapter) capable](https://sites.google.com/view/eagle-llm) of [guessing a few tokens](https://sites.google.com/view/medusa-llm) at time.

Cursor built a variant of speculative decoding called “[speculative edits](https://cursor.com/blog/instant-apply)”, an algorithm that uses much longer speculations to make code edits substantially faster.

These longer speculations are possible in case of partial text rewriting when the caller has a strong guess of what the generation might look like, especially with Code Generation. This speculative guess is used by Fireworks to speed up the response considerably.

The speculation is always validated using deterministic (greedy) generation. I.e., the server will find the longest prefix of the "speculation" field that matches the model's generation with temperature=0. After that, it will proceed with normal generation respecting request parameters, including the temperature.

Fireworks deployed Cursor’s special fine-tune of Llama-3-70b for the coding task “[Fast Apply](https://www.cursor.com/blog/instant-apply)” using the speculative API flag, enabling them to ~13x speedup over vanilla inference using Llama-3-70b and a ~9x speedup over their previous GPT-4 speculative edits deployment leading them to achieve ~1000 tokens/sec.

Powered by Llama

Using Speculative Decoding as a feature is easy because it is a flag in [Fireworks API](https://docs.fireworks.ai/api-reference/post-completions).

123456789101112131415161718192021222324252627282930

Traditional Large Language Models struggled with providing relevant context and often produced suboptimal results or slow responses.

Using Fireworks AI Inference stack, Cursor achieved a remarkable speed bump compared to vanilla inference and their previous GPT-4 deployment.

At Fireworks, our mission is democratizing AI for developers and businesses, serving the best of [language](https://fireworks.ai/models/fireworks/llama-v3-70b-instruct), audio and [image](https://fireworks.ai/models/stability/sd3) models at the fastest speeds and highest reliability. Today, we work with companies like Quora, Uber, Doordash with industry-leading inference speed and quality for production use cases across image and text generation.

If you are a developer or an enterprise starting on the Generative AI, consider [joining our community](https://discord.gg/fireworks-ai) of practitioners, sign up to [Fireworks AI platform](https://fireworks.ai/login) to freely build Generative AI experiences up to two million tokens.
