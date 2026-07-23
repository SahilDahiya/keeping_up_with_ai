---
title: Are AI labs pelicanmaxxing?
kind: blog
topic: null
subtopic: null
secondary_topics: []
summary: null
triage: null
skip_reason: null
source: simon-willison
url: https://simonwillison.net/2026/Jul/22/are-ai-labs-pelicanmaxxing/
author: Simon Willison
published: '2026-07-22'
fetched: '2026-07-23T06:55:52Z'
classifier: null
taxonomy_rev: 2
words: 336
content_sha256: 27fd8e52c4afd1557987b43992eee81c3f064de7ac39bf6bfc2d77f283ef7c9d
---

# Are AI labs pelicanmaxxing?

22nd July 2026 - Link Blog

** Are AI labs pelicanmaxxing?** (

[via](https://news.ycombinator.com/item?id=49010129)) Excellent piece of work by Dylan Castillo, who took a deep-dive into the frequently pondered question of whether the AI labs have been deliberately training models to draw pelicans riding bicycles in response to my

[deeply unscientific benchmark](https://simonwillison.net/tags/pelican-riding-a-bicycle/).

I've been randomly spot-checking this in the past by testing models against other animals riding other types of vehicle, but never with anything close to the diligence of Dylan's methodology here.

Dylan took 8 animals × 6 vehicles = 48 prompts and ran them three times each through 7 different models ( GPT-5.6 Terra, Claude Sonnet 5, Gemini 3.5 Flash, Grok 4.5, Qwen3.7-Max, GLM-5.2, and DeepSeek V4 Pro). He then used GPT-5.6 Luna and Gemini 3.1 Flash-Lite to help evaluate the results.

There's a neat filter view for exploring the results:

![Screenshot of a grid for sample 1/3 of GLM-5.2, with pelicn and flamingo and heron riding bicycle, unicycle, skateboard, scooter, plane and boat](https://static.simonwillison.net/static/2026/pelican-grid.webp)


For the models he tested he could find no evidence of pelimaxxing:


[The pelicans on bicycles don’t look any better](https://dylancastillo.co/posts/pelicanmaxxing.html#evidence-1-the-pelicans-on-bicycles-dont-look-any-better)
[Labs are not better at drawing pelicans](https://dylancastillo.co/posts/pelicanmaxxing.html#evidence-2-labs-are-not-better-at-drawing-pelicans)
[Labs are not better at drawing bicycles](https://dylancastillo.co/posts/pelicanmaxxing.html#evidence-3-labs-are-not-better-at-drawing-bicycles)
[Labs are not better at drawing pelicans on bicycles, even adjusting for difficulty](https://dylancastillo.co/posts/pelicanmaxxing.html#evidence-4-labs-are-not-better-at-drawing-pelicans-on-bicycles-even-adjusting-for-difficulty)
[The pelican-bicycle scenes don’t look memorized](https://dylancastillo.co/posts/pelicanmaxxing.html#evidence-5-the-pelican-bicycle-scenes-dont-look-memorized)[...]Pelicans aren’t drawn any better than other animals. Bicycles aren’t drawn any better than other vehicles. And no lab draws the combination better than its pelicans and bicycles already predict. GLM-5.2 comes closest: it has the largest boost on the exact pelican-bicycle cell, and and its first pelican-on-bicycle sample caught my eye. But the effect is small and not significant, so I wouldn’t put too much weight on it.


## Recent articles

- [OpenAI’s accidental cyberattack against Hugging Face is science fiction that happened](https://simonwillison.net/2026/Jul/22/openai-cyberattack/)- 22nd July 2026
- [A Fireside Chat with Cat and Thariq from the Claude Code team](https://simonwillison.net/2026/Jul/21/cat-and-thariq/)- 21st July 2026
- [Kimi K3, and what we can still learn from the pelican benchmark](https://simonwillison.net/2026/Jul/16/kimi-k3/)- 16th July 2026
