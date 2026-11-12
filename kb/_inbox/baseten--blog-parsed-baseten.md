---
title: 'Parsed + Baseten: Building Models That Touch Grass'
kind: blog
topic: null
subtopic: null
secondary_topics: []
summary: null
triage: null
skip_reason: null
source: baseten
url: https://www.baseten.co/blog/parsed-baseten
author: Mudith Jayasekara
published: '2025-12-10'
fetched: '2026-11-12T06:14:18Z'
classifier: null
taxonomy_rev: 2
words: 1436
content_sha256: 050de9c7582829568b6347a6d6ce4494486b697f74b6ace5e3de377960a7107c
---

# Parsed + Baseten: Building Models That Touch Grass

News
# Parsed + Baseten: Building Models That Touch Grass

Today we are excited to share that Parsed is joining Baseten.


- Authors
- Date
- December 10, 2025

TLDR

By combining Parsed’s training systems with Baseten’s inference and current training stack, we are building a unified platform for the next era of AI development: continuous improvement from real production data; faster iteration cycles; more control for engineering teams; and a clearer path to owning specialized, high-performance models.

From the beginning, we started Parsed with a simple belief: AI wasn’t doing nearly enough real work. Models were powerful, but they weren’t specialized, aligned, or connected to the real systems where they could create value. The world didn’t need ever-bigger models; it needed models that understand context deeply, perform reliably, and can be trusted with actual responsibility.

At Parsed, we believe doing things well requires specialization. The big-model worldview quietly assumes you should rent a multitrillion parameter demigod to perform clerical labour, and pay premium rates for the privilege; specialization is simply the moment you realize you don’t need to subsidize their business model to get real work done. The rest of the world figured this out a long time ago, but language models mostly bet on the opposite: generalization wins, consolidation wins. As the frontier curves began to flatten and each new model release felt less like a phase change and more like a modest bump, the next step seemed obvious. Companies would want models that are really good at the one thing they need them to do.

The truth is, no matter how good your underlying model is or how clever your prompting gets, a specialized model will win on an important, well-defined task. For chatbots and everyday use, the go-to *should be* the general-purpose giants. But for deep work in specific domains with repeatable instructions, lots of implicit context, and clear feedback signals, (medical scribing, insurance policy recommendation, front-end design, finance-flavoured RAG spreadsheet builders, legal review agents, and so on) your best bet is a specialized, post-trained, compounding LLM whose weights and training data are yours. The demand for real intelligence turns out to be fundamentally inelastic, because there is an extraordinary amount of useful work still waiting to be automated.

The big labs do not really want this to be the narrative. Company leaders have called the open versus closed debate a red herring and argued that only base model performance truly matters. Big Token’s preferred cosmology is a monoculture, one model to rule everything and one bill to pay forever. Just trust that next month’s update will finally solve hallucinations, and that the trickle-down effects of new model releases will eventually, fuzzily, vaguely improve what you specifically are trying to do. It is a very convenient story for Big Token, and it misses where durable value is going to be created. If sheer mass were destiny, a Chinese e-commerce company wouldn't be landing clean shots on the crowned giants of San Francisco.

We took the other side of that bet. Parsed has been about building systems that can take an open model and, through careful evaluation, feedback design, and post-training, make it exceptional at one job and better over time – with the model and its training data living on your side of the table, not locked behind someone else’s API. You don’t have to watch helplessly as Anthropic’s quantization lobotomizes your model, without any visibility; you don’t have to tune your prompts to the different personalities of model families. We wanted teams to be able to shape their own intelligence layer without having to build a research lab.

That brings us to Baseten.

Building specialized models is only half the problem. Deploying them fast, reliably, and at scale is the other half. We tried everything: hyperscalers, neoclouds, and just about every inference platform we could find. Most could not support the performance envelope or developer experience required for our real production workloads.

Baseten could. Very quickly it became clear they were meaningfully ahead — better reliability, better performance, better tooling, and a team obsessed with craft. Over the past few months, everything we built ran on Baseten. The partnership made us dramatically better.

There are also a lot of GPUs in the world that are not controlled by the Big Labs. We think the team with the best shot at running the world’s inference on those GPUs is Baseten.

We are beyond excited to join Baseten to help move the world off a single-provider default and onto a more democratic path for intelligence. Together, we are solving for both sides of the equation. Parsed will focus on taking open-source models and making them outperform closed-source models for customers who need it. Baseten will make those models run faster and more reliably than anywhere else in the world. Training and inference will feed into each other in a tight loop: models that learn from real workloads, then serve those workloads even better, then learn again.

We have already been using Baseten as our inference partner for quite some time. Customers trust them to get their models running better than anyone else, even at scales that almost no one outside the Big Labs has tried. All they need is someone who can help a model learn and keep learning on a specific task. That is what we do.

You can’t just spin up a static fine-tuning API and call it a day. The most important thing is not what algorithm you use to execute a gradient update, but what learning signal is used to derive that gradient in the first place. We care about the abstraction that sits upstream of training: deriving the right signal from real-world production data to update on. What is being rewarded, what is being penalized, and how that shapes the gradients that actually move the weights. Your model has to, as we say, keep touching grass!

In Baseten, we have a partner that makes that loop natural. Inference that lives as close as possible to production, and training that is continually fed by it.

If you are already working with Parsed, the short version is: things will keep working, and they will only get better.

Over the coming months, you can expect:

- Continued support for existing deployments, with careful migration onto Baseten’s infrastructure where it makes sense.
- More performance for less money: your specialized models running on Baseten’s inference stack, which means faster, more reliable inference at larger scale and, over time, lower prices.
- Real ownership of your models: continued access to your model weights, training data, and evaluations, so you are not dependent on a black-box API that forgets everything at the end of a context window.
- The same interfaces you use today, now backed by Baseten: ongoing access to the Parsed platform and APIs, with new capabilities coming as we integrate more deeply.
- A clearer path to compounding improvement: tighter loops from real production data to learning signals to gradient updates, so your models get better the more you use them.

We will reach out directly to every customer to talk through specifics, timelines, and opportunities to deepen what we have already built together. If there is a particular deployment or idea you want to push further now that we have more compute and a bigger team behind us, we would love to hear about it.

Baseten believes in the same world that we do. Tuhin, Phil, Amir, Pankaj, and the entire Baseten team have built something exceptional. They have quietly become one of the fastest-growing startups in AI, and have earned a reputation as the most trusted and performant place to run inference. We are looking forward to helping customers figure out what “good” actually looks like for their tasks so that they can teach a model that, and keep teaching it, without having that knowledge vanish at the end of a context window. We are looking forward to productizing our research on how to train these systems, and to continuing to push on the frontier of post-training.

Most of all, we are looking forward to working with some of the most talented, thoughtful and, dare we say it, fun people we have met on this journey.

Parsed will no longer stand on its own, but the future it set out to build is a step closer today. To everyone who trusted us early, shipped with us, or argued with us at unreasonable hours about loss functions and evals, thank you. If you're interested in chatting more about how we can help you, please [reach out](https://www.baseten.co/talk-to-us/train-your-model/).

We’re just getting started.
