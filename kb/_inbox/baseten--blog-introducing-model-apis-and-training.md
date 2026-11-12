---
title: Introducing Model APIs and Training
kind: blog
topic: null
subtopic: null
secondary_topics: []
summary: null
triage: null
skip_reason: null
source: baseten
url: https://www.baseten.co/blog/introducing-model-apis-and-training
author: Tuhin Srivastava
published: '2025-05-21'
fetched: '2026-11-12T06:10:02Z'
classifier: null
taxonomy_rev: 2
words: 532
content_sha256: 6b69147206bdfc8b0763cec7c71cd2fe3d515596d8ef56272dd516044b2ada65
---

# Introducing Model APIs and Training

News
# Introducing Model APIs and Training

Today we're launching two new products to serve the inference lifecycle: production-ready Model APIs and Training infrastructure.


- Authors
- Date
- May 21, 2025

Over the last few years, we’ve been steadfast in supporting dedicated infrastructure for our customers. Customers have come to us when they have trained their own models or wanted to use open-source models at sufficient scale, and care deeply about consistent, fast performance, reliable uptime, and best-in-class developer experience to manage models in production.

But there’s been a significant shift — open-source models are better than ever, and out-of-the-box are rivaling SOTA in most benchmarks. Today, we're excited to introduce two new products that help take those models into production: Model APIs and Training.

We were excited to be the first provider that gave access to DeepSeek V3 and R1, and the ecosystem continues to get richer with recent drops of Llama 4 and Qwen 3. However, APIs for accessing these models have lagged; performance is variable, reliability is nonexistent, and the developer experiences have left a lot to be desired. For developers getting started using open-source models, you are forced to deal with non-production grade products with subpar experiences.

We think we can do better, and today we’re releasing [Baseten Model APIs](https://www.baseten.co/products/model-apis/). Our goal with Model APIs is to provide an easy path to integrate open-source models into production. We’ve built it with developers in mind, and we aim to provide state-of-the-art performance, production-grade reliability and an easy path from getting started to using Model APIs to using Dedicated Infrastructure on Baseten. We’re launching with four great models today, and we’ll add new models across modalities as the landscape evolves going forward. Get started [here](https://app.baseten.co/signup/?_gl=1*ftuskc*_gcl_aw*R0NMLjE3NDQ4Mjg3MzYuQ2owS0NRandxdjJfQmhDMEFSSXNBRmI1QWNfQWNnOHBQaVVZU3RmTEFmZWV5Ny1KNEhVUGY0Y0tyUDRHWDJDUzFObjZQTnJaOHVwaWRuWWFBaG5qRUFMd193Y0I.*_gcl_au*MjAxNzQxNjE2OC4xNzQ3ODQwMjc1LjEzNDI5MDg2Ny4xNzQ3ODQwMzAzLjE3NDc4NDI1NzI.) today. Thank you to our great partners [Retool](https://retool.com/), [OpenRouter](https://openrouter.ai/models?fmt=cards&providers=BaseTen), and [Poe](https://poe.com/baseten) for helping us get Model APIs launch ready.

At the same time, we’ve seen a natural evolution of customers going from closed-source models, to open-source models, to wanting to train and fine-tune their own models. Like the vast majority of AI infrastructure problems, software for running training and fine-tuning jobs is either non-existent (acquire compute, SSH into boxes, pray), or too black-boxey in nature (i.e. give us data, we’ll give you an underwhelming model). On a weekly basis, for the last year, we’ve heard from customers that they’d love to see the “Baseten developer experience” applied to training.

Today, we’re really excited to announce [Baseten Training](https://www.baseten.co/talk-to-us/request-access/). We’re solving the infrastructure problems that come with training — this includes acquiring capacity, scheduling jobs, accommodating multi-node workflows, and attempting to help customers incorporate new techniques (such as SFT and GRPO) without the infrastructure problems that come with them. If you have your own data, and training scripts, you can get started right away. If you need some help along the way, our Forward Deployed Engineering team is here to help. As always, we’re trying to keep the easy things easy, while making the hard things remain possible.

As part of our launch, we’re excited to announce that we’re working with companies [MixedBread](https://www.mixedbread.com/), [Oxen.ai](https://www.oxen.ai/entry/fine-tuning-a-with-oxen-ai) and [Canopy](https://canopylabs.ai/) that are training at the frontier. You can read more about it [here](https://www.baseten.co/products/training/), and get in touch for [early access](https://www.baseten.co/talk-to-us/request-access/).
