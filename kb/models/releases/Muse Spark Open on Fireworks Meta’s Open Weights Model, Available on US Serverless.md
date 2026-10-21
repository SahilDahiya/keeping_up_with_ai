---
title: 'Muse Spark Open on Fireworks: Meta’s Open Weights Model, Available on US Serverless'
kind: blog
topic: models
subtopic: releases
secondary_topics:
- product-engineering/case-studies
summary: Announces Meta's Muse Spark Open (816B-param MoE, 42B active params, 1M-token
  context) on Fireworks serverless, reporting it ranks first on Harvey's Legal Agent
  Benchmark and beats Claude Opus 5.5 on Rogo's Big Finance Bench, with 33% hallucination
  rate on AA-Omniscience versus 59% for Opus 5.5.
triage: null
skip_reason: null
source: fireworks
url: https://fireworks.ai/blog/meta-muse-spark-open
author: null
published: '2026-10-20'
fetched: '2026-10-21T06:10:17Z'
classifier: claude
taxonomy_rev: 2
words: 793
content_sha256: 3d6ad052f5f07b7390ef8926dde9f4977c18dab332ced1f1705997584df9c038
---

# Muse Spark Open on Fireworks: Meta’s Open Weights Model, Available on US Serverless

[Muse Spark Open](https://fireworks.ai/models/fireworks/muse-spark-open), an open weights model from Meta, is available Day-0 on Fireworks. It's an 816B-parameter mixture-of-experts model with 42B parameters active per token and a 1M-token context window, built for long-horizon coding and agent work that has to stay coherent across very long sessions.

It’s one of the most capable US open weights model to date, and the strongest open weights model we’ve seen for regulated professional work. It ranks first on Vals AI’s leaderboard for Harvey’s Legal Agent Benchmark, with nearly 4x the pass rate of Claude Opus 5. On Rogo’s Big Finance Bench, it beat Claude Opus 5.5 at every difficulty level and edged out GPT-6 Astra on the hardest tasks.

Muse Spark Open was trained and developed in the US, and Fireworks runs it with Zero Data Retention by default. [Try it today on serverless](https://app.fireworks.ai/models/fireworks/muse-spark-open), running on US-only capacity with no US premium. Then move to reserved throughput for production and fine-tune it with serverless LoRA training.

Muse Spark Open shows strong agentic engineering capability: it can navigate repositories, implement nontrivial changes, and validate complex coding work - Zimu, Member of Technical Staff at Factory

Muse Spark Open does its best work where accuracy is paramount, such as legal, finance, and clinical tasks. These results come from independent evaluators and our Specialized Intelligence Index, where every model runs on the same harness:

- •**#1 on Harvey’s egal Agent Benchmark:** On [Vals AI’s leaderboard](https://www.vals.ai/benchmarks/hlab) for completing legal work with files and tools, Muse Spark Open ranks first of 75 models at 25.4%, nearly 4x Claude Opus 5 (6.7%).
- •**Ahead of Claude Opus 5.5 on Rogo’s Big Finance Bench:** In Fireworks’ [Specialized Intelligence Index](https://fireworks.ai/specialized-intelligence-index/benchmarks/finance/big-finance-benchmark) runs, Muse Spark Open beat Claude Opus 5.5 at every difficulty level. On the hardest tasks, it edged out GPT-6 Astra (17.3% vs. 16.5%) and scored more than 2.5x Opus 5.5 (6.6%) (Figure 1).
- •**Top three on Finance Agent:** On [Vals AI’s Finance Agent v2](https://www.vals.ai/benchmarks/fabv2), it scored 60.6%, within a point of Gemini 3.8 Flash at about 60% lower cost per test.
- •**Clinical documentation:** It scored 90.1% on [Vals MedScribe](https://www.vals.ai/benchmarks/medscribe), within a point of Claude Opus 5 (91.0%), at 75-83% lower token prices.

Third-party results from Vals AI and Artificial Analysis in this post were measured on Meta’s API release of this model.

At Rogo we run every new model through Big Finance Bench, our set of 928 real financial workflow questions. Muse Spark Open scored 53.3%, the top open weights model on our board and ahead of even frontier Claude Opus 5 at 49.2%. The emergence of high-performing American open weights models is particularly exciting. They provide a foundation for continued experimentation and the ability to tailor intelligence to the specific demands of financial work. We are excited by the potential to push the frontier of model performance while unlocking new levels of value and efficiency for our customers. - Alex Wang, Member of Technical Staff at Rogo

Muse Spark Open holds its own on standard public benchmarks:

- •Fewer hallucinations: On [Artificial Analysis’ AA-Omniscience](https://artificialanalysis.ai/models/muse-spark-1-2?omniscience=omniscience-hallucination-rate), it has a 33% hallucination rate, lower than Claude Opus 5.5 (59%) and GPT-6 Astra (51%), because it declines to answer when unsure instead of guessing.
- •Agentic coding: In Meta's evaluations, it scores 82.9% on Terminal-Bench 2.1, ahead of GPT-5.6 Terra and Grok 4.5 (Figure 2).

Muse Spark Open represents a step change for Western open-source models, with particularly strong instruction following in our early evaluations. We're excited to build on that foundation through post-training for the complex workflows we power at Decagon - Decagon Labs

Before opening the endpoint, we ran the final open weights through our launch validation suite on our production serving stack. Muse Spark Open scored 91.1% on AIME26, 89.7% on GPQA Diamond, and 84.3% on SWE-bench Verified, and stayed above 80% on image understanding with OCRBench and MMMU Pro (Figure 3). As a check, we also ran the same weights on SGLang, a widely used open-source inference engine, and the scores matched. The model you call on Fireworks performs the way Meta built it.

Filevine was founded in the American West. And we believe the frontier should be open. Working with Fireworks and Meta means that Filevine can open new horizons of possibility for the law, without sacrificing quality for cost. - Ryan Anderson, Cofounder and CEO at Filevine

Muse Spark Open is available on our serverless API today on US-only capacity, with no US premium. See the [Muse Spark Open model page](https://fireworks.ai/models/fireworks/muse-spark-open) for current pricing.

1. Serverless: [Get started](https://app.fireworks.ai/models/fireworks/muse-spark-open) with Muse Spark Open directly on Fireworks serverless or move to reserved throughput for production workloads.
2. Want to tailor Muse Spark Open to your use case? Try our Serverless Training API or [get in touch with Fireworks Lab](https://fireworks.ai/contact-training) to help.
