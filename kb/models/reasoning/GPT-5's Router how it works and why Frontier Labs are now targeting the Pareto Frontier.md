---
title: 'GPT-5''s Router: how it works and why Frontier Labs are now targeting the
  Pareto Frontier'
topic: models
subtopic: reasoning
secondary_topics:
- inference/serving
summary: Explains GPT-5 routing and why frontier labs optimize along a Pareto frontier
  of model capabilities and latency.
source: latent-space
url: https://www.latent.space/p/gpt5-router
author: Latent Space
published: '2025-08-07'
fetched: '2026-07-11T05:16:53Z'
classifier: codex
taxonomy_rev: 1
words: 674
content_sha256: afd1b518acf8409acd5675d8de44ccda005828f2a5bbbf1629c3bbdba14b7ef4
---

# GPT-5's Router: how it works and why Frontier Labs are now targeting the Pareto Frontier

# GPT-5's Router: how it works and why Frontier Labs are now targeting the Pareto Frontier

### The big reveal of GPT-5 was entirely unexpected but is welcome nonetheless - there's a router!

We have been the most vocal [proponents of the intelligence pareto frontier](https://www.latent.space/p/reasoning-price-war?utm_source=publication-search) since the start of the reasoning model era. [Demis took note](https://x.com/demishassabis/status/1908301867672560087) and [GDM went for it](https://x.com/demishassabis/status/1913013113630110093).** But with GPT-5, OpenAI now dominates the intelligence per dollar frontier for the first time.**

![](https://substackcdn.com/image/fetch/$s_!toeh!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe585c017-9a82-4a05-b339-d0e76d507a2b_1672x1236.png)

[lasted all of 3 months](https://news.smol.ai/issues/25-05-20-google-io)at the pareto frontier

When we first tried it out, [those of us in the developer beta](https://x.com/OpenAIDevs/status/1953535155789865423) were initially concerned - “it’s a great coding model… but is that it?” was kind of the unspoken elephant in the room. Sentiment turned more positive over time and the big aha that got me fully hyped was the pricing reveal.

**This is because the $ per intelligence frontier is ultimately a routing problem; **one that has been a developing and increasingly optimized story since the introduction of GPT-4 and o1.

The #1 question that people have about GPT-5 being “unified” is “**is it a router??**”, a question I have asked both [Greg Brockman](https://youtu.be/avWhreBUYF0) and [Noam Brown](https://www.latent.space/p/noam-brown), and after a lot of back and forth on Twitter and inconclusive answers, we now have the answer right there in [the GPT-5 system card](https://openai.com/index/gpt-5-system-card/):

![](https://substackcdn.com/image/fetch/$s_!4g2w!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4238c3fa-4e3f-4823-9b92-d0cc7025b4df_969x807.png)

This is a level of transparency I had been asking for from the team, but was never really optimistic about getting!

**To really drive it home:**

If the big breakthrough from GPT-3 to [GPT-4 was the Mixture of Experts](https://x.com/swyx/status/1671272883379908608), then perhaps **the big breakthrough from GPT-4o/o3 to GPT-5 is the Mixture of Models (aka the “router”).**

![](https://substackcdn.com/image/fetch/$s_!dsKb!,w_2400,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe3c57d4b-ba61-4ad4-bd8a-2b5dfcb54161_2676x1372.png)

## Why does it matter?

To some extent, whether or not GPT5 is a “unified model” or “unified system”, whether or not there’s a component that you call a “router” point blank, doesn’t quite matter. The moment you have reasoning and non reasoning modes, the moment you have different paths for inference for efficiency or specialization (“experts”) or [compute depth](https://arxiv.org/abs/2404.02258)[1](https://www.latent.space#footnote-1), you essentially have a router somewhere in the system, and now it is just a question of semantics and “thickness” of the router layer.

For example you can see the MoE layer in open source models like Qwen 3, where it is clearly routing.

![](https://substackcdn.com/image/fetch/$s_!8spu!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F3dcf98b9-5d19-4531-befe-1cfc8ffffd6e_5906x4341.png)

[@rasbt’s excellent substack](https://substack.com/@rasbt)

So even though there’s DEFINITELY a router, one benefit and reason why people are still extremely curious about it is the ability to lock down parts of the model performance and independently progress them.

So for example, if GPT5 = router + “new 4o” + “new o3”, then (if we had control of the weights) if a bug happened there are only 3 sources of error:

- did it route to the right model?
- if it was a nonreasoner bug, can we fix that?
- if it was a reasoner bug, can we fix that?

And because these are “orthogonal” independently moving pieces, you can expect that improving one while holding the other constant is an intuitive important step to engineering better AI systems.

Perhaps most comforting (or disappointing?) to the rest of us [non-OpenAI-millionaires](https://x.com/deedydas/status/1953318528385167695) is that *that’s how we would do this too*, and there is no big secret that the BigLabs have been hiding that there is a more Bitter Lesson-y way to make hybrid models.

![](https://substackcdn.com/image/fetch/$s_!oIbA!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F1643dfbc-8a6a-4306-bcca-be41448229aa_391x103.png)

## The Great Consolidation

The immediate benefit of the GPT-5 launch is a question of cognitive load - as you can tell [the model picker mess](https://x.com/swyx/status/1922797421484011758) weighs heavily on OpenAI and a unified system starts to fix it (even though for developers, control remains as the “model picker” effectively shifts into [the new reasoning effort, verbosity, function calling params](https://cookbook.openai.com/examples/gpt-5/gpt-5_new_params_and_tools)):

![](https://substackcdn.com/image/fetch/$s_!_HuJ!,w_2400,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F15c76f92-8801-4ae7-b892-be0f0bdf9c04_2604x812.png)

This is backed up by [impending model deprecations](https://help.openai.com/en/articles/6825453-chatgpt-release-notes) confirmed in release notes:

![](https://substackcdn.com/image/fetch/$s_!kpC9!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fdea0adc0-faf8-45ed-96db-8c51545aa11e_1824x1016.png)

Which is a -far- more ambitious deprecation schedule than the Developer facing options, with all their permutations:

## Keep reading with a 7-day free trial

Subscribe to Latent.Space to keep reading this post and get 7 days of free access to the full post archives.
