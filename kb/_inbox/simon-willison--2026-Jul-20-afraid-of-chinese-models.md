---
title: Who’s Afraid of Chinese Models?
kind: blog
topic: null
subtopic: null
secondary_topics: []
summary: null
triage: null
skip_reason: null
source: simon-willison
url: https://simonwillison.net/2026/Jul/20/afraid-of-chinese-models/
author: Simon Willison
published: '2026-07-20'
fetched: '2026-07-21T06:56:25Z'
classifier: null
taxonomy_rev: 2
words: 349
content_sha256: 25db02428bedcb9a8cf6fdde534c2f49c7270d9ceee65b2c57981dd7938ca062
---

# Who’s Afraid of Chinese Models?

20th July 2026 - Link Blog

** Who’s Afraid of Chinese Models?** (

[via](https://daringfireball.net/linked/2026/07/20/thompson-chinese-models-distillation)) Interesting proposal from Ben Thompson that both addresses the hypocrisy of labs outlawing distillation against their models despite training on unlicensed data, and could help US open models compete more effectively with their Chinese counterparts:

The U.S. should pass a law that (1) makes explicit that collecting data for training models is fair use, and (2) bars terms of service that forbid distillation, for U.S. companies at a minimum. Stopping distillation — which is literally just querying the API — is nearly impossible; the U.S. should go the other way and lean into a new copyright policy that both indemnifies the labs and also guarantees that what they learned fuels further innovation for everyone else.


Ben also theorizes that Alibaba's decision to release Qwen 3.8 Max as open weights - a reversal from their decision [not to release Qwen 3.7 Max](https://qwen.ai/blog?id=qwen3.7) in May - may have been influenced by a [recent speech](http://english.scio.gov.cn/topnews/2026-07/18/content_118605932.html) by Xi Jinping, who said:

We should seize this rare, historic opportunity to encourage open source, openness, collaboration and sharing.


And on the subject of [Qwen 3.8 Max](https://twitter.com/Alibaba_Qwen/status/2078759124914098291) - a new 2.4T parameter model (nearly as large as the 2.8T Kimi K3) - here's [a pelican it drew](https://tools.simonwillison.net/markdown-svg-renderer#url=https%3A%2F%2Fgist.github.com%2Fsimonw%2F735f2cf19b795517cb2ff6cae1c71c64):

![Described by Qwen 3.8 Max: Flat vector cartoon illustration of a white pelican with a large orange beak and pouch riding a red bicycle, its orange legs on the pedals, against a light blue sky with a yellow sun top right and a white cloud top left, with horizontal motion lines behind the bike and a pale green ground strip at the bottom.](https://static.simonwillison.net/static/2026/qwen-3.8-max-pelican.png)


I particularly enjoyed seeing these notes in the (extensive) reasoning trace: "Could add helmet? No." and "Maybe add small bell? no." and "Need maybe add small fish in basket? Not necessary."

## Recent articles

- [Kimi K3, and what we can still learn from the pelican benchmark](https://simonwillison.net/2026/Jul/16/kimi-k3/)- 16th July 2026
- [The new GPT-5.6 family: Luna, Terra, Sol](https://simonwillison.net/2026/Jul/9/gpt-5-6/)- 9th July 2026
- [sqlite-utils 4.0, now with database schema migrations](https://simonwillison.net/2026/Jul/7/sqlite-utils-4/)- 7th July 2026
