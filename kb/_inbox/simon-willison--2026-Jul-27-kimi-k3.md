---
title: moonshotai/Kimi-K3
kind: blog
topic: null
subtopic: null
secondary_topics: []
summary: null
triage: null
skip_reason: null
source: simon-willison
url: https://simonwillison.net/2026/Jul/27/kimi-k3/
author: Simon Willison
published: '2026-07-27'
fetched: '2026-07-28T06:57:22Z'
classifier: null
taxonomy_rev: 2
words: 321
content_sha256: 80dbe27b71b76235974a20059e6084bf7decc423948cfee2522a7a5baf9dbf65
---

# moonshotai/Kimi-K3

27th July 2026 - Link Blog

** moonshotai/Kimi-K3**. As promised 

[earlier this month](https://simonwillison.net/2026/Jul/16/kimi-k3/), Moonshot have released the weights for their excellent 2.8 trillion parameter Kimi K3. They're a hefty 1.56TB on Hugging Face.

Kimi introduced their own janky [modified version of the MIT license](https://huggingface.co/moonshotai/Kimi-K2-Instruct/blob/main/LICENSE) with K2 back in July 2025. That license just added this paragraph requiring attribution beyond a certain size of commercial entity:

Our only modification part is that, if the Software (or any derivative works thereof) is used for any of your commercial products or services that have more than 100 million monthly active users, or more than 20 million US dollars (or equivalent in other currencies) in monthly revenue, you shall prominently display "Kimi K2" on the user interface of such product or service.


The [K3 license](https://huggingface.co/moonshotai/Kimi-K3/blob/main/LICENSE) no longer calls itself "modified MIT" and goes further, requiring a separate agreement with Moonshot for large "Model as a Service" businesses:

If the Licensee or any of its affiliates operates a Model as a Service business, and the aggregate revenue of the Licensee and its affiliates exceeds 20 million US dollars (or the equivalent in other currencies) in total over any consecutive 12 months, the Licensee must enter into a separate agreement with Moonshot AI before using the Software or its derivative works for any commercial purpose.


To Kimi's credit, they make no attempt to describe this as an "open source" license in their own materials, consistently using the term "open weight" in its place.

OpenRouter is already offering K3 [from 7 providers](https://openrouter.ai/moonshotai/kimi-k3), most of which are at the same $3/million input and $15/million output as Moonshot AI themselves.

## Recent articles

- [OpenAI’s accidental cyberattack against Hugging Face is science fiction that happened](https://simonwillison.net/2026/Jul/22/openai-cyberattack/)- 22nd July 2026
- [A Fireside Chat with Cat and Thariq from the Claude Code team](https://simonwillison.net/2026/Jul/21/cat-and-thariq/)- 21st July 2026
- [Kimi K3, and what we can still learn from the pelican benchmark](https://simonwillison.net/2026/Jul/16/kimi-k3/)- 16th July 2026
