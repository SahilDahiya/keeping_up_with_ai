---
title: deepseek-ai/DeepSeek-V4-Flash-0731
kind: blog
topic: null
subtopic: null
secondary_topics: []
summary: null
triage: null
skip_reason: null
source: simon-willison
url: https://simonwillison.net/2026/Jul/31/deepseek-v4-flash-0731/
author: Simon Willison
published: '2026-07-31'
fetched: '2026-08-01T06:55:16Z'
classifier: null
taxonomy_rev: 2
words: 414
content_sha256: 72d5047aba3ed86ab4fcbd18b7ffe0442fca51ab5b9e27dc33d32534724f093f
---

# deepseek-ai/DeepSeek-V4-Flash-0731

31st July 2026 - Link Blog

**[deepseek-ai/DeepSeek-V4-Flash-0731](https://huggingface.co/deepseek-ai/DeepSeek-V4-Flash-0731)** ([via](https://news.ycombinator.com/item?id=49120299)) The latest release in DeepSeek's V4 family, "with substantially enhanced agentic capabilities". It's 304 billion parameters - 167GB on Hugging Face - but it appears to punch *well* above its weight.

Artificial Analysis [rank it](https://artificialanalysis.ai/models/deepseek-v4-flash) ahead of MiniMax M3 - a 428B model. It's $0.14/million input and $0.27/million output pricing means this may currently be the best value-per-intelligence model out there. It's looking very good on the [Intelligence Index vs. Cost per Intelligence Index Task](https://artificialanalysis.ai/models/deepseek-v4-flash#intelligence-comparison-tabs) chart:

![Scatter plot from Artificial Analysis titled with axes "Artificial Analysis Intelligence Index" (20 to 65) and "Cost per Task (USD, Log Scale)" ($0.02 to $3), with a green "Most attractive quadrant" box in the upper left and a dotted "Pareto line". DeepSeek V4 Flash 0731 (max) is highlighted in dark blue at roughly $0.028 and an intelligence score of 50, sitting alone at the far left edge of the green quadrant where the Pareto line jumps sharply upward. Models of similar or lower intelligence like MiniMax-M3, Kimi K3 (low), GLM-5.1 and Kimi K2.6 cost ten times more, and the models that beat it (Grok 4.5, Gemini 3.6 Flash, GLM-5.2, Kimi K3, Claude Opus 5, Claude Fable 5, GPT-5.6 Sol) all sit far to the right at $0.4 to $3 per task.](https://static.simonwillison.net/static/2026/deepseek-flash-chart.webp)


I got [a disappointing pelican](https://gist.github.com/simonw/83bfb1171792f1e7a4d8935b5e82317e#prompt) from it using the default reasoning level via OpenRouter:

![Flat vector illustration of a white pelican with a long neck and large orange beak pouch, hovering above a mangled blue and orange bicycle on a dark grey road with white dashed lane markings. The bike is drawn incorrectly: the wheels are just orange arcs with no rims or spokes, the frame tubes float apart and the handlebars connect to nothing. The background is pale blue with a yellow sun in the upper left, white clouds, and grey speed lines on the left suggesting motion.](https://static.simonwillison.net/static/2026/deepseek-flash-v4-default.png)


But when I bumped reasoning level up to high I got [something much better](https://gist.github.com/simonw/83bfb1171792f1e7a4d8935b5e82317e#options):

`llm -m openrouter/deepseek/deepseek-v4-flash-0731 -t pelican -o reasoning_effort high`

![Flat vector illustration of a white pelican riding a bicycle to the right against a pink background with a lighter pink circle behind it. The pelican grips the handlebars with its wings and one orange foot rests on the pedal, and a small blue fish is visible tucked in the corner of its large orange beak pouch. The bike has a red, blue and orange frame with dark tires, and grey speed lines trail behind to suggest motion.](https://static.simonwillison.net/static/2026/deepseek-flash-v4-high.png)
