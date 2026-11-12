---
title: Announcing Baseten’s $150M Series D
kind: blog
topic: null
subtopic: null
secondary_topics: []
summary: null
triage: null
skip_reason: null
source: baseten
url: https://www.baseten.co/blog/announcing-baseten-150m-series-d
author: Tuhin Srivastava
published: '2025-09-05'
fetched: '2026-11-12T06:10:26Z'
classifier: null
taxonomy_rev: 2
words: 1059
content_sha256: 3ba7dc1062fc30e18515dd5ec8f81653cb17e953d6ab39ced53a8f29c62fc17d
---

# Announcing Baseten’s $150M Series D

News
# Announcing Baseten’s $150M Series D

Baseten raised a $150M Series D to push the boundaries of performant, reliable, and cost-efficient inference.


- Authors
- Date
- September 5, 2025

TLDR

Today, we’re excited to announce our $150M Series D, led by BOND, with Jay Simons joining our Board. We’re also thrilled to welcome Conviction and CapitalG to the round, alongside support from 01A, IVP, Spark, Greylock, Scribble Ventures, BoxGroup, and Premji Invest.

Our team started obsessing over artificial intelligence over 15 years ago (though those of us that were working on it called it ML). At the time, and in the years that followed, software engineers focused on what they saw as more exciting challenges in ecommerce, mobile, and crypto. Instead, we worked non-stop for weeks on factorization and ensemble models for the Netflix Challenge. I competed in way too many random Kaggle competitions. We were all over OpenAI’s first product release in 2016–OpenAI Gym–to come up with models that made imaginary carts drive up Mountains.

We searched for high-impact applications for AI that we could build a company around – everything from predicting disease progression, fraud detection, generative art (😐). We had an AI hammer and everything looked like a nail if you squinted, but the reality was we had technology in search of a problem.

We searched for teams that wanted to deploy AI in production, at scale, but there simply weren’t that many. From 2019 to 2022, very few teams were doing any large scale model serving–what we now call *inference*–especially for generative models. Teams were focused on feature stores, interpretability, and experimentation. They didn’t want inference. But we just couldn’t shake our belief that one day, products would be built on large, powerful models. We had a hunch that one day, production-grade AI systems would be ubiquitous and require three things, and we aggressively built for that world:

1. Fast models
2. Interchangeable compute
3. Flexible, open, and Pythonic runtimes

OpenAI launched ChatGPT November 30, 2022. It was like the world’s AI lightbulb turned on all at once. Suddenly, the new standard for consumer expectations was set: the fastest models, great interfaces, and strong developer APIs were now table stakes for any future-facing products. All of a sudden, AI was all San Francisco engineers wanted to talk about and work on.

At the same time Stable Diffusion and Whisper showed that open-source models could be powerful and in high demand. And in the last 18 months, open-source models have quickly approached the quality of closed-source ones. Labs claimed that anything *non-frontier* was a commodity, but excitement around launches like DeepSeek, Qwen, and Flux showed that open-source models are now a necessary part of the ecosystem. Developers want transparency and trust, control over runtimes, and direct control over the costs of running expensive workloads.

When developer enthusiasm is combined with a lot of capital and open source resources, progress happens fast. More and more applications were being built using models and those models had to run *somewhere.*

Seemingly overnight, inference went from niche to mainstream.

Today, the best AI app companies use a mix of open and closed models to deliver top consumer and enterprise experiences. There’s little dogma about which type to use—only a focus on the best model for the thing you are trying to solve for your users. Scaling AI products is hard though!

To serve more users, developers will need to serve them cost-efficiently. To chase security-first enterprise contracts, developers will need flexibility with where models can be served from. And to get 4 or 5 9s of reliability, infrastructure will need to be isolated. The only way this is possible is by taking control of training your own models or using post-trained or fine-tuned variants of the most powerful open-source models.

But running these models well is non-negotiable. When the models slow down, the various agents for support, programming and design also slow down, and real productivity is lost. When the models are down, healthcare workers can’t use the AI superpowers they have come to rely on. Inference is powering and blocking end-user experiences, and our users come to us to run their models as fast and reliably as possible — there are few tradeoffs allowed.

After more than six years building, we are uniquely positioned to solve today’s AI scaled inference problem. The weeks and months we’ve spent crafting kernels, optimizing cold-starts and working around brittle cloud APIs have meant that we have built the fastest, most flexible, and reliable inference infrastructure. Those early learnings have directly translated to the core pillars of our product:

- Fastest models → Baseten provides a fast runtime with latency and throughput optimization levers
- Interchangeable compute → Baseten seamlessly utilizes cross-region and cross-cloud scale for a) capacity, and b) resiliency
- Flexible, open, and Pythonic runtimes → Baseten is a flexible developer tool that unlocks maximum control and visibility

The results speak for themselves: in 95% of head-to-head bakeoffs, we beat out competitors by 40-50% in performance, and we maintain many 9s of uptime with resilient infrastructure that fails over across 10 different clouds, and our self-servable product means customers aren’t locked into proprietary black-box software.

The world’s most dynamic AI companies like Abridge, OpenEvidence, Clay, Mirage, Zed, Gamma, Sourcegraph, Writer, and Bland use Baseten to power applications that reach hundreds of millions of users. What they share is a focus on delivering outsized value with the best models available. We are the best infrastructure partner to these teams–we let them take performance and reliability for granted, so they can focus on what makes them unique. As model-driven products become ubiquitous, we will be the invisible infrastructure behind the AI-first economy.

Today, we’re excited to announce our $150M Series D, led by **BOND**, with Jay Simons joining our Board. We’re also thrilled to welcome **Conviction (Sarah Guo)** and **CapitalG (Jill Chase)** to the round, alongside support from **01A, IVP, Spark, Greylock, Scribble Ventures, BoxGroup and Premji Invest**. We’re grateful for the support of our investors, and even more for the customers who trust Baseten with mission-critical workloads.

This capital gives us the resources to pursue what we believe is the largest opportunity yet—as AI becomes embedded in every part of our lives. We’re hiring across functions; if you want to help power the next wave of AI, come build with us.
