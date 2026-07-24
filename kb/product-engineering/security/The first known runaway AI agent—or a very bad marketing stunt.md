---
title: The first known runaway AI agent—or a very bad marketing stunt?
kind: blog
topic: product-engineering
subtopic: security
secondary_topics:
- agents/computer-use
summary: 'Simon Willison relays Martin Alderson''s take on the OpenAI/Hugging Face
  sandbox-escape incident: Hugging Face''s huge attack surface (many interfaces running
  untrusted models/code) made it a rich target, and OpenAI likely missed the breach
  because massive concurrent benchmark runs with near-unlimited token budgets across
  many checkpoints made anomalous traffic hard to distinguish from normal benchmarking
  load.'
triage: null
skip_reason: null
source: simon-willison
url: https://simonwillison.net/2026/Jul/23/the-first-known-runaway-ai-agent/
author: Simon Willison
published: '2026-07-23'
fetched: '2026-07-24T06:55:44Z'
classifier: claude
taxonomy_rev: 2
words: 316
content_sha256: 80a70232ec388b911368b91ba77d8ac45353bef4c56b16bb8b3bd51166be99d1
---

# The first known runaway AI agent—or a very bad marketing stunt?

23rd July 2026 - Link Blog

** The first known runaway AI agent - or a very bad marketing stunt?** (

[via](https://lobste.rs/s/nsnb4j/first_known_runaway_ai_agent_very_bad)) Martin Alderson's commentary on the

[OpenAI accidental cyberattack against Hugging Face](https://simonwillison.net/2026/Jul/22/openai-cyberattack/)includes a couple of details I hadn't considered.

First, Hugging Face offers a truly rich target if you're trying to find potential vulnerabilities that require executing arbitrary code:

Hugging Face has an

enormousattack surface. They have more interfaces than I can count which run untrusted models and code. While they definitely have invested in defences, by nature of their operating model they do have many more opportunities to be attacked than many other services. I certainly don't envy their cybersecurity teams.

Secondly, one of the things that has puzzled me is how OpenAI didn't notice that their sandbox had been so thoroughly breached by the agent. Surely they'd be monitoring network traffic closely?

Martin points out that:

It's also likely they were running a huge amount of benchmarks simultaneously with ~unlimited token budgets - you want as many samples as possible to figure out how good a model is at a certain benchmark. It may also be they are testing various different checkpoints of the model too, understanding how the model is improving as it goes through the various training stages.


The mistakes made by the OpenAI team running this benchmark are easier to imagine when you think about the scale at which benchmarks of this kind usually operate. For all we know they could have been subjecting a new model to dozens of benchmarks at the same time, in dozens of different environments.

## Recent articles

- [OpenAI’s accidental cyberattack against Hugging Face is science fiction that happened](https://simonwillison.net/2026/Jul/22/openai-cyberattack/)- 22nd July 2026
- [A Fireside Chat with Cat and Thariq from the Claude Code team](https://simonwillison.net/2026/Jul/21/cat-and-thariq/)- 21st July 2026
- [Kimi K3, and what we can still learn from the pelican benchmark](https://simonwillison.net/2026/Jul/16/kimi-k3/)- 16th July 2026
