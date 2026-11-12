---
title: 'How to choose an AI model: lessons from Notion and Gamma'
kind: blog
topic: null
subtopic: null
secondary_topics: []
summary: null
triage: null
skip_reason: null
source: baseten
url: https://www.baseten.co/blog/how-to-choose-a-model-lessons-from-notion-and-gamma
author: Chloe Florit
published: '2026-07-22'
fetched: '2026-11-12T06:08:06Z'
classifier: null
taxonomy_rev: 2
words: 1099
content_sha256: 78bf398202fa2ececbed96c1c45dc7b2c2c7cf954f291cfd09bcec5f07fc233c
---

# How to choose an AI model: lessons from Notion and Gamma

Community
# How to choose an AI model: lessons from Notion and Gamma

Takeaways from Notion and Gamma on picking AI models: swap for cost and reliability, match model to task, and lean into open-weight models.


- Authors
- Date
- July 22, 2026

Two years ago, choosing a model was simple: call the best API and build around it. Today, every model behaves differently, the same task can cost 10x more on one model than another, and open-weight models are nearly as good as closed ones. The labs supplying intelligence are also shipping products that compete with the companies buying it.

We hosted a panel on how to navigate this with Sarah Sachs, Head of AI at [Notion](https://www.notion.com/), and Jon Noronha, co-founder of [Gamma](https://www.baseten.co/resources/customers/how-gamma-makes-building-presentations-criminally-fun/), moderated by Baseten's [Charles O'Neill](https://x.com/oneill_c).

Here are the main takeaways from the talk.

A [harness](https://www.baseten.co/blog/harnesses-are-everything-heres-how-to-optimize-yours/) is everything built around an LLM to connect it to the outside world: it handles parsing outputs, calling tools on the LLM's behalf, feeding results back to the model, managing context, and handling errors and retries. You can modify an existing harness to add new tools and tighten guardrails for a specific use case.

At the harness level, "model agnostic" means one harness with swappable models underneath. But each model expects a harness structured like the one it was trained on. A shared harness fails because prompts written to steer one model away from its failure modes degrade the models that never had those failure modes.

Similarly, a model-agnostic harness would affect context management: if you rebuild compaction\* yourself instead of using a model's native compaction, you're overriding how it was trained to decide what to keep and what to drop, which leaves you with worse context handling.

You should take each model's native harness and modify it for your use case.

*\*Compaction in LLMs is the technique of summarizing or compressing a conversation's accumulated context as it nears the model's context window limit.* 

Per-model investment is expensive, but it’s cheaper than committing to a single model for three reasons:

1. Reliability. When a provider degrades, you have the flexibility to move.
2. Cost. When a cheaper model clears the quality bar, you can substitute it.
3. Speed of adoption. When a new model ships, you can test it in days instead of re-engineering for weeks.

But to swap models, you need to know how to correctly compare them. Some outputs are easy to score with evals like whether the code compiled or the answer was factually correct. Other outputs are subjective: how can an automated script score whether a presentation is well-designed?

So instead of pure evals, companies use A/B testing: they show real users different versions (made by different models) and see which performs better in practice. Gamma tests GPT vs. Gemini vs. Claude against each other, at different price tiers, because a budget user and a premium user have different tolerances for cost vs. quality. They combine this human A/B testing with whatever can be automatically scored (like "does the text fit on the slide without overflowing?").

Models behave differently on the same request. GPT models are literal: they do exactly what you ask. Claude models are better at inferring intent.

For example, Gamma users might dump a long, wordy document and say: make this a presentation, preserve every word. GPT preserves every word and produces a wall of text on every slide. Claude keeps the gist and makes a presentation you'd actually present.

Notion sees the same thing from a different perspective. Some tasks don’t need a more advanced model: editing a page, deciding which team a ticket should be triaged to, or summarizing a meeting note. Notion's evals show no measurable quality difference from a smarter model on those jobs. The extra intelligence is a "capability overhang."

To determine the right model for a task, companies should measure cost per capability per second, per user flow: what capability does this task require, and what's the cheapest, fastest way to deliver it? Defaulting to the most powerful model is not the solution: users will wait longer and pay more for intelligence the task never needed.

On many production workloads, [open-weight models](https://www.baseten.co/library/?utm_term=baseten&utm_campaign=Core+Brand&utm_source=adwords&utm_medium=ppc&hsa_acc=9990356727&hsa_cam=21493664768&hsa_grp=163775031783&hsa_ad=706521141070&hsa_src=g&hsa_tgt=kwd-384324573564&hsa_kw=baseten&hsa_mt=p&hsa_net=adwords&hsa_ver=3&gad_source=1&gad_campaignid=21493664768&gbraid=0AAAAAqCKh1uB-kAv5pIYKn1eqQmNPkwpR&gclid=CjwKCAjwx7LSBhB3EiwAjcodxCkGSzih1_mrjvBVQRWxwieIPltQQ1Sf7iwTo1zouHxN1VWViQFXzBoCemYQAvD_BwE) now match frontier closed models, with far more knobs to turn on serving speed and fine-tuning.

That unlocks markets that closed models can't serve. More than three-quarters of Gamma's revenue comes from outside the US, much of it from countries like Brazil and India, where willingness to pay is lower but model costs are fixed. Cheaper open-weight models make a good product viable at those price points.

With open-weight models, the inference provider becomes part of the quality equation. The same weights served by different platforms, with different optimizations, produce different quality at scale. Evaluate the provider, not just the model.

Open-weight models help keep the market from narrowing down to just one or two dominant players. Supporting them is how companies at the application layer keep control over their own pricing.

The obvious case for fine-tuning an open-weight model is margin: swap an expensive closed API for a cheaper fine-tuned model, keep prices the same, and pocket the difference on every request.

But fine-tuning offers more than margin: cheaper intelligence at fair value per task lowers the barrier to AI-enabled work, and the market grows from there. It makes features like meeting summaries effectively free. Businesses are offered something they couldn't otherwise afford, and the market expands.

[Reinforcement learning](https://www.baseten.co/resources/guide/why-reinforcement-learning-matters/#why-should-you-care-about-rl) (RL) takes this further by training a model on your own task, rewarding outputs that succeed and penalizing ones that fail. RL can push a model past the best closed models at your specific job. But RL is only as good as your data, and data is exactly what product-market fit produces. RL learns from signal, and improves only when it has enough real examples labeled clearly as success or failure.

Notion notes that RL is an investment: they had to be able to spin up duplicate copies of a workspace and train against them hundreds of thousands of times, without taking down the production search index. The returns of RL are worth it, but it's an investment.

The old rule was no GPUs before product-market fit. The new rule: no post-training before explosive product-market fit.

It’s time to choose your model differently. That means comparing models with the right tests, switching for reliability and cost, and picking the right model for your task instead of defaulting to the most powerful one. Open-weight models are now strong enough for most production workloads, and the right provider can help you serve them with high-quality outputs.
