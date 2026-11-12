---
title: Run Qwen3 Embedding on NVIDIA Blackwell GPUs
kind: blog
topic: null
subtopic: null
secondary_topics: []
summary: null
triage: null
skip_reason: null
source: baseten
url: https://www.baseten.co/blog/run-qwen3-embedding-on-nvidia-blackwell-gpus
author: Michael Feil
published: '2025-07-29'
fetched: '2026-11-12T06:13:56Z'
classifier: null
taxonomy_rev: 2
words: 378
content_sha256: 45f1714ca0a4874019ce58f795b1d4e740697f059370c97063d065c1a1c408fe
---

# Run Qwen3 Embedding on NVIDIA Blackwell GPUs

Model performance
# Run Qwen3 Embedding on NVIDIA Blackwell GPUs

Baseten Embeddings Inference on Blackwell GPUs (B200s) delivers over 3x higher throughput compared to TEI and vLLM for production embedding models at scale.


- Authors
- Date
- July 29, 2025

We’re excited to announce Baseten Embeddings Inference (BEI) for Blackwell GPUs. This means you can take advantage of the latest open-source embeddings models, such as Qwen3 Embedding, and the latest NVIDIA GPUs, while using the most performant embeddings inference engine: [BEI](https://www.baseten.co/blog/introducing-baseten-embeddings-inference-bei/).

To illustrate the unlocked potential, we’ve run benchmarks using the Qwen3 Embedding 8B model. This is the largest of the Qwen3 Embedding series, which has the multilingual capabilities, long-text understanding, and reasoning skills of its foundation model counterpart.

As of this writing, Qwen3 Embedding 8B is #1 on the [Massive Text Embedding Leaderboard](https://huggingface.co/spaces/mteb/leaderboard), with a mean task score of 70.58%.

In terms of throughput on a high query-throughput test (500 tokens/request), running Qwen 3 8B Embedding with BEI on B200s can process 1.5x more tokens per second compared to BEI running on an H100 (the next best solution), 3.3x more than vLLM, and 3.6x more than TEI on H100.

On a low query-throughput test (5 tokens per request), BEI on B200s has 8.4x higher throughput than vLLM and 1.6x higher than TEI.

You can see the full benchmark results in the table below.

| Inference framework | Precision | GPU | Tokens/second (high throughput, 500 tokens/request) | Requests/second (low throughput, 5 tokens/request) | 
|---|---|---|---|---|
| TEI | BF16 | H100 | 34055 | 824.25 | 
| vLLM | BF16 | H100 | 36625 | 155.23 | 
| BEI | BF16 | H100 | 47549 | 761.44 | 
| BEI | FP8 | H100 | 77107 | 855.96 | 
| BEI | FP8 | B200 | 121443 | 1310.52 | 

To get started with Qwen3 Embedding 8B, you can deploy it [via our Model Library.](https://www.baseten.co/library/qwen3-8b-embedding/) *(Note: this link deploys on H100 MIG by default, but you can change the instance type to B200.)*

If you’re running embedding models or compound AI systems at scale, [reach out](https://www.baseten.co/talk-to-us/) to learn how we can optimize your workloads. In the meantime, you can also check out our [technical deep dive](https://www.baseten.co/blog/how-we-built-high-throughput-embedding-inference-with-tensorrt-llm/) on how we optimized BEI, or our [docs](https://docs.baseten.co/examples/bei) for more information!
