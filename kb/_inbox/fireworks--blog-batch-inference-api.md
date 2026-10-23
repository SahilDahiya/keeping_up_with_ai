---
title: 'Batch API: Run Async Batch Inference at 50% Lower Cost | Fireworks'
kind: blog
topic: null
subtopic: null
secondary_topics: []
summary: null
triage: null
skip_reason: null
source: fireworks
url: https://fireworks.ai/blog/batch-inference-api
author: null
published: '2025-07-31'
fetched: '2026-10-23T06:11:24Z'
classifier: null
taxonomy_rev: 2
words: 285
content_sha256: b76c32dd9f414edf002b786ba36016dc8506f44be8e8f1ebdbeebd2d0ea37004
---

# Batch API: Run Async Batch Inference at 50% Lower Cost | Fireworks

With Fireworks’ Batch API, you can asynchronously run large volumes of requests on 1000+ open or finetuned models with no rate limits, 50% lower cost, and a 24-hour turnaround time.

This is helpful for use cases like:

- **Evaluations:** Benchmark across models to identify the best model for your use case
- **Data generation:** Generate bulk outputs using large models to fine-tune smaller models
- **Data augmentation:** Create paraphrases, sentiment labels, or question-answer pairs at scale
- **ETL Pipelines and Daily bulk processing:** Process large numbers of documents daily without worrying about rate limits

To use the Batch API, you simply upload your dataset in JSONL batch format and kick off a Batch API job. You can then check in on the status of your request, and retrieve the results once they are ready.

The Batch API has the following benefits:

- **High rate limits:** There is no upper limit on the number of requests in a batch job. The dataset must be \<500 MB in size.
- **Lower cost:** 50% lower cost compared to typical Serverless (synchronous) API pricing
- **Fast processing:** Results can be retrieved in a few hours, with a max turnaround time of 24 hours
- **Access 1000+ models**: Run batch jobs on all major open models supported by Fireworks or your own fine-tuned models

### Getting Started in 3 Steps

**Prepare Your Dataset**

Create a JSONL Batch format dataset, for example:

`pythonCopy`
12

`pythonCopy`
1

**Launch a Batch Job**

Choose from **1,000+ models**—including base models in our Model Library \[link\], public community models, and your own fine-tuned variants.

`pythonCopy`
1234

**Download Results**

Once the job completes, fetch your outputs in one command:

`pythonCopy`
12

Ready to unlock true AI scale?
