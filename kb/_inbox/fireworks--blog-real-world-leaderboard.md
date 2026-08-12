---
title: Fireworks AI
kind: blog
topic: null
subtopic: null
secondary_topics: []
summary: null
triage: null
skip_reason: null
source: fireworks
url: https://fireworks.ai/blog/real-world-leaderboard
author: null
published: '2025-07-30'
fetched: '2026-08-12T06:30:50Z'
classifier: null
taxonomy_rev: 2
words: 694
content_sha256: cd17e9717f826c4f15bacef970aaa12b11b82daaf5ca69d86eaa1f6f9ef4a580
---

# Fireworks AI

The open-source model landscape is exploding, making it hard to choose the right model. To help you cut through the noise, Fireworks is sharing **real-world benchmarks** on recent model releases based on tasks we've seen in production. Our initial findings show **Qwen Instruct** excels at knowledge-heavy tasks, **Qwen3 Coder** is a strong contender for simple tool-use, and **Claude Sonnet 4** remains the leader for complex, multi-step agentic workflows.

Dozens of new open-source models have been released in the past few weeks alone. While this rapid innovation is exciting, it creates a significant challenge for developers and businesses: which model is actually the best for your specific use case?

All models claim to top the latest benchmarks but how do the models actually perform on real-world tasks, like classifying customer support tickets, powering an e-commerce search, or running a complex agent? At Fireworks, our goal is to help customers deploy the best possible model for their job, without the guesswork.

To provide clarity, we’re starting to build a  **Fireworks Real-World Leaderboard**.

Instead of focusing on broad academic benchmarks, our leaderboard evaluates models on targeted, vertical-specific tasks that mirror the real use cases we've seen customers ask most frequently about. This helps you see how models perform on tasks you actually care about.

While we'd love for you to use open models for all your tasks, we recognize that the best model is specific to your preferences and task. Sometimes, the best model might be closed source and sometimes it may be open-source. Regardless of your task, we want you to be able to confidently and easily choose the best model.

Here’s our initial take on where open-source models shine and where there's still room to grow.

For tasks that are heavy on world knowledge, classification, or ranking, we see the new **Qwen Instruct** model outperforming even proprietary models like GPT-4.1 and O4 mini. Its strong performance is directly correlated with its high score on SimpleQA, a benchmark that measures a model's ability to answer fact-based questions.

**Recommendation:** If your application relies on factual accuracy and knowledge retrieval, **Qwen Instruct** is an exceptional choice.

| Model | Score | 
|---|---|
| qwen3_235b_a22b_instruct | 0.7576530612 | 
| qwen3_coder_480b_a35b_instruct | 0.7474489796 | 
| qwen3_235b_a22b_thinking_2507 | 0.7389455782 | 
| o4_mini | 0.7261904762 | 
| gpt_4_1 | 0.6794217687 | 
| kimi_k2_instruct | 0.6760204082 | 

In simple tool-calling scenarios, such as those found in e-commerce applications (e.g., "find black shoes in size 10"), **Qwen3 Coder** is neck-and-neck with GPT-4.1. It provides a powerful and cost-effective alternative right out of the box, demonstrating that OSS models are highly competitive for structured, single-turn tasks.

**Recommendation:** For straightforward tool-use and function-calling, **Qwen3 Coder** is a top-tier open-source alternative.

| Model | Score | 
|---|---|
| gpt_4_1 | 0.91 | 
| qwen3_coder_480b_a35b_instruct | 0.862 | 
| qwen3_235b_a22b_instruct | 0.836 | 
| qwen3_235b_a22b_thinking_2507 | 0.8176666667 | 
| kimi_k2_instruct | 0.654 | 

Open models don't always win in our benchmarks. When it comes to complex instruction following and multi-tool use—where world knowledge, reasoning, and tool calling are all required simultaneously—we still see **Claude Sonnet 4** as the hands-down leader. These sophisticated, agentic workflows require a level of nuanced understanding that proprietary models currently handle best.

**Recommendation:** For complex agents that require multi-step reasoning and tool orchestration, **Claude Sonnet 4** remains the leading choice. Amongst the OSS models

- •If you are ok with the latency of a reasoning model, Qwen 235B thinking is the top choice and very close to Sonnet 4.0
- •If you want an instruct model, Kimi K2 is the best choice for following complex instructions

| Model | Elo Rating | 
|---|---|
| claude_sonnet_4_20250514 | 1000 | 
| qwen3_235b_a22b_thinking_2507 | 941 | 
| gpt-4.1-2025-04-14 | 917 | 
| kimi_k2_instruct | 825 | 
| qwen3-coder-480b-a35b-instruct | 790 | 
| qwen3_235b_a22b_instruct_2507 | 739 | 

We find OpenHands 100 turn SWE-bench to be a great representative benchmark for production coding, and Qwen3 Coder comes closest to Sonnet

These insights are just the beginning. Let us know where more data or benchmarking would be helpful for you. The open-source community is moving faster than ever, and we'll be continuously building out benchmarks with new models and tasks.
