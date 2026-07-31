---
title: Advancing the price-performance frontier with GPT‑5.6
kind: blog
topic: null
subtopic: null
secondary_topics: []
summary: null
triage: null
skip_reason: null
source: simon-willison
url: https://simonwillison.net/2026/Jul/30/luna-price-drop/
author: Simon Willison
published: '2026-07-30'
fetched: '2026-07-31T07:03:55Z'
classifier: null
taxonomy_rev: 2
words: 308
content_sha256: 099c627e8dddb1c41a15ca060f1cc91cf80f25d324533df79500899c29fb642f
---

# Advancing the price-performance frontier with GPT‑5.6

30th July 2026 - Link Blog

** Advancing the price-performance frontier with GPT‑5.6** (

[via](https://news.ycombinator.com/item?id=49112867)) Huge price drop from OpenAI today: GPT-5.6 Terra got a 20% reduction, and GPT-5.6 Luna got a massive 80% drop.

OpenAI credit 5.6 Sol with enabling this: in [How GPT‑5.6 fuses frontier intelligence with frontier efficiency](https://openai.com/index/gpt-5-6-frontier-intelligence-efficiency/) they describe using 5.6 Sol to optimize load balancing, and more impressively to optimize inference itself:

We also used GPT‑5.6 Sol to optimize the model’s forward pass: the computation that transforms inputs into next-token predictions. Even when individual operations are fast, excess memory movement, synchronization, and inefficient data layouts can leave GPUs idle. To avoid this, GPT‑5.6 Sol found work that could be precomputed, avoided, or parallelized. With Codex, GPT‑5.6 Sol autonomously rewrote and optimized our production kernels, the core code that executes the mathematical operations that make up the model. This worked in part because we’ve trained GPT‑5.6 to be effective at writing and improving kernels in

[Triton](https://triton-lang.org/main/index.html)and[Gluon](https://triton-lang.org/main/gluon/index.html), two open-source GPU programming languages maintained by OpenAI. These efforts, combined with broader kernel advancements from GPT‑5.6 Sol, reduced end-to-end serving costs by 20%.

That Luna price drop completely changes the landscape with respect to lower priced models. At $0.20/million tokens for input and $1.20/million for output Luna is now cheaper than Google's Gemini 3.1 Flash-Lite ($.025/$1.50).

Anthropic's cheapest current model is Claude Haiku 4.5, and that's $1/$5 - Luna is now 1/5th of that for input, previously it cost the same.

My [agent.datasette.io](https://agent.datasette.io/) demo site was running on Gemini 3.1 Flash-Lite. I've switched it over to Luna.

## Recent articles

- [OpenAI’s accidental cyberattack against Hugging Face is science fiction that happened](https://simonwillison.net/2026/Jul/22/openai-cyberattack/)- 22nd July 2026
- [A Fireside Chat with Cat and Thariq from the Claude Code team](https://simonwillison.net/2026/Jul/21/cat-and-thariq/)- 21st July 2026
- [Kimi K3, and what we can still learn from the pelican benchmark](https://simonwillison.net/2026/Jul/16/kimi-k3/)- 16th July 2026
