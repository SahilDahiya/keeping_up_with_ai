---
title: 'God is hungry for Context: First thoughts on o3 pro'
topic: prompt-engineering
subtopic: context-engineering
secondary_topics:
- models/reasoning
summary: First thoughts on o3 pro framed around context hunger and reasoning-model
  workflows.
source: latent-space
url: https://www.latent.space/p/o3-pro
author: Ben Hylak; Alexis
published: '2025-06-10'
fetched: '2026-07-11T05:17:27Z'
classifier: codex
taxonomy_rev: 1
words: 1128
content_sha256: 517b890de25994de3ed73582a8584131d12a5da6eb664ade408bd57ad9fa4d31
---

# God is hungry for Context: First thoughts on o3 pro

# God is hungry for Context: First thoughts on o3 pro

### OpenAI dropped o3 pricing 80% today and launched o3-pro. Ben Hylak of Raindrop.ai returns with Alexis Gauba for the world's first early review.

*As “ leaked”, OpenAI cut o3 pricing by 80% today (from $10/$40 per mtok to $2/$8 - matching GPT 4.1 pricing!!) to set the stage of the launch of o3-pro ($20/$80, supporting an unverified community theory that the -pro variants are 10x base model calls with majority voting as referenced in their papers and in our Chai episode). o3-pro reports a 64% win rate vs o3 on human testers and does marginally better on 4/4 reliability benchmarks, but as sama noticed, the actual experience expands when you test it DIFFERENTLY…*

*Thanks to  Hacker News and theo for covering us.*

**I’ve had early access to o3 pro for the past week. below are my (early) thoughts:**

![](https://substackcdn.com/image/fetch/$s_!jlPu!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa958ca07-2119-4dd1-a0c0-617528fd5d49_1042x896.png)

## God is hungry for context.

We’re in the era of task-specific models. On one hand, we have “normal” models like 3.5 Sonnet and 4o—the ones we talk to like friends, who help us with our writing, and answer our day-to-day queries. On the other, we have gigantic, slow, expensive, IQ-maxxing reasoning models that we go to for deep analysis (they’re great at criticism), one-shotting complex problems, and pushing the edge of pure intelligence.

If you follow me on [Twitter](https://x.com/benhylak/status/1878237490194366744), you know I've had a journey with the o-reasoning models. My first impression of o1/o1-pro was quite negative. But as I gritted my teeth through the first weeks, propelled by other people's raving reviews, I realized that I was, in fact, using it wrong. I wrote up all my thoughts, got ratio’ed by @sama, and quote-tweeted by @[gdb](https://x.com/gdb/status/1878489681702310392).


![o1 isn’t a chat model (and that’s the point)](https://substackcdn.com/image/fetch/$s_!PUC3!,w_140,h_140,c_fill,f_auto,q_auto:good,fl_progressive:steep,g_auto/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F3e97fcc3-a572-4a87-b2c2-6fc016edd5dd_1276x598.png)

The key, I discovered, was to *not* chat with it. Instead, **treat it like a *** report generator* Give it context, give it a goal, and let it rip. And that's exactly how I use o3 today.

[1](https://www.latent.space#footnote-1).

But therein lines the problem with evaluating o3 pro.

It’s smarter. *much smarter.*

**But in order to see that, you need to give it ****a lot**** more context. and I’m running out of context.**

There was no simple test or question i could ask it that blew me away.

But then I took a different approach. My co-founder Alexis and I took the the time to assemble a history of all of our past planning meetings at ** Raindrop**, all of our goals, even record voice memos: and then asked o3-pro to come up with a plan.

We were blown away; it spit out the exact kind of concrete plan and analysis I’ve always wanted an LLM to create — complete with target metrics, timelines, what to prioritize, and strict instructions on what to absolutely cut.

The plan o3 gave us was plausible, reasonable; but the plan o3 Pro gave us was specific and rooted enough that **it actually changed how we are thinking about our future.**

This is hard to capture in an eval.

# Integrating with the Real World

Trying out o3 Pro made me realize that models today are so *good* in isolation, we’re running out of simple tests. The real challenge is integrating them into society. It's almost like a really high IQ 12-year-old going to college. **They might be smart, but they’re not a useful employee if they can’t integrate.**

Today, this integration primarily comes down to tool calls: how well the model collaborates with humans, external data, and other AIs. It’s a great thinker, but it’s gotta grow into being a great do-er. o3 Pro makes real jumps here. It’s noticeably better at discerning what it’s **environment** is; accurately **communicating what tools it has access to**, when to **ask questions about the outside world** (rather than pretending it has the information/access), and **choosing the right tool** for the job.

**o3 pro (left) vs o3 (right):**

![](https://substackcdn.com/image/fetch/$s_!GX6V!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F70e6cdb1-9691-4f10-b495-d4479c207bf7_2684x1582.png)

![](https://substackcdn.com/image/fetch/$s_!a4ia!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F31b789a0-a417-4b2b-9984-624a1d03c772_1942x1580.png)

o3 pro (left) clearly understanding the confines of it’s environment way better.

# Shortcomings

One thing I noticed from early access: if you don’t give it enough context, it does tend to overthink. It’s insanely good at analyzing, amazing at using tools to do things, not so good at doing things directly itself. I think it would be a fantastic orchestrator. But, for example, there were some ClickHouse SQL questions that o3 did better with. YMMV!

To illustrate:

![](https://substackcdn.com/image/fetch/$s_!v0yS!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F6e7c5aa6-5ffd-40cb-941b-f25631d8fa5a_6863x3935.jpeg)

## Compared to other models

o3 Pro feels very, very different from Opus and Gemini 2.5 Pro. Where Claude Opus *feels* big but never truly showed me a clear sign of its “bigness,” o3 Pro’s takes are just... better. It feels like a completely different playing field.

OpenAI’s really driving down this vertical RL path (Deep Research, Codex)—not just teaching models how to use tools, but how to reason about when to use them.

# Closing Thoughts

The best ways to prompt reasoning models haven’t changed. [My guide on how to prompt o1 still stands](https://www.latent.space/p/o1-skill-issue). Context is everything, its like feeding cookies to the cookie monster. It’s a way of bootstrapping LLM memory but actually targeted so it works well. And the system prompt really matters. Models have actually become really malleable so LLM “harnesses” that teach a model about it’s environment and its goals have outsize impact. It’s this “harness” - a combination of model, tools, memory, and other methods - that makes AI products actually good (what makes things like Cursor just work most of the time).

Other assorted tasks:

- The system prompt wildly shaped model behavior (in a good way!) It felt way more pronounced than even o3.
- Leaps and bounds different than anthropic and gemini. Where Claude Opus - *feels*big (but has really never shown me a true sign of its “bigness”), these takes are just.. better. Feels like a completely different playing field.
- OAI’s really driving down this vertical RL path (Deep Research, Codex). E.g. teaching models not just how to use tools, but to reason about when to use them.

[1](https://www.latent.space#footnote-anchor-1)

Many are [saying this](https://x.com/jxnlco/status/1931411011447226804) - “report generation” is basically what we do at [AINews](https://news.smol.ai/) and also with [Deep Research](https://www.latent.space/p/gdr) and [Brightwave](https://www.youtube.com/watch?v=MWTJIAwAAnk&t=490s).

LLMs need to ask more questions. There is too much focus on taking up a task and making autonomous decisions when there are gaps. Instead the priority should be to help the user to refine the task first.

I’ve seen more questions with recent models but it’s still scratching the surface.

Considering how different models require different type of prompting and context, task usage, etc to make it function optimally, is there a tool that can help select the appropriate model, tune the prompt and then run it? Like a meta reasoning model sitting atop a library of models.
