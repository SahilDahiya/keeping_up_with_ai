---
title: 'Gisting: Compressing LLM Agent context to ↑ throughput and ↓ cost (2026)'
kind: blog
topic: inference
subtopic: optimization
secondary_topics:
- prompt-engineering/context-engineering
- models/fine-tuning
summary: Shopify's Sidekick GraphQL agent uses gisting -- training special 'gist'
  token embeddings via knowledge distillation -- to compress its ~6,000-token system
  prompt to ~1,500 gist tokens (4:1), cutting median TTFT from 438ms to 354ms and
  end-to-end latency from 6.8s to 4.2s while raising throughput from 20.2 to 23.4
  QPS at 350 RPM, reducing the GPUs needed to serve the agent.
triage: null
skip_reason: null
source: shopify
url: https://shopify.engineering/gisting
author: Cody Mazza-Anthony
published: '2026-08-19'
fetched: '2026-08-21T06:14:40Z'
classifier: claude
taxonomy_rev: 2
words: 1110
content_sha256: aa92f1854afc9b511c0ef412ed5e22a2bfec163c45c479613df79bd1a3a73a7b
---

# Gisting: Compressing LLM Agent context to ↑ throughput and ↓ cost (2026)

System prompts can account for thousands of tokens per request. A longer prompt means slower, more expensive inference. This results in more GPUs required to accommodate the same traffic when serving a model on dedicated hardware.

Our implementation of gisting, as first proposed in *Prompt Compression and Contrastive Conditioning for Controllability and Toxicity Reduction in Language Models**,¹* allows us to reap the behavioral advantages of a long prompt at the cost of a short one.

Through gisting, we cut down the Sidekick GraphQL agent’s system prompt from ~6,000 tokens to ~1,500 gist tokens (a 4:1 reduction) without losing prediction quality. We achieve this by learning the embeddings for a set of special tokens via knowledge distillation and swapping them with the system prompt at inference time.

The serving gains from a 4:1 compression of the system prompt into gist tokens are significant. At 350 requests per minute (RPM), the median time to first token (TTFT) dropped from 438ms to 354ms, the median end-to-end request latency dropped from 6.8s to 4.2s, and throughput rose from 20.2 to 23.4 queries per second (QPS). These gains allowed us to reduce the number of GPUs allocated for the GraphQL agent’s traffic.

## How gisting works

A *gist toke**n* is a special token that we add to the model's vocabulary. We train the sequence of embeddings so that their substitution into the context induces the model to behave as though it’s seen the full prompt. At 4:1 compression, we add one gist token for every four prompt tokens. We freeze the weights of the model and only train the gist embeddings.

![How gisting works](https://cdn.shopify.com/s/files/1/0779/4361/files/System_prompt.png?v=1787078946)

We learn the gist embeddings via knowledge distillation. We run the forward pass twice on each trajectory. During the teacher pass, the model sees the full natural-language prompt to derive the teacher logits for each position in the model’s response. For the student pass, we swap the full prompt for the gist tokens and run the same model again to derive the student logits corresponding to each teacher response position. We train the gist embeddings using the KL divergence between the teacher logits and the student logits, until the student's predictions closely match the teacher's.

![Teacher vs student predictions](https://cdn.shopify.com/s/files/1/0779/4361/files/Teacher_student.png?v=1787078978)

Deploying a gisted model is simple. When training finishes, we write the gist embeddings straight into the model's embedding matrix, and register the new gist tokens as special tokens in the model’s tokenizer. The model loads and runs like any other at inference time: no custom attention mask, extra encoder, or special serving path. The only inference-time change is on the request-side: replacing the prompt with the string of gist tokens. The entire cost of compression is paid once, at training time.

## Why prefix caching isn't enough

The advantages of gisting and prefix caching are not mutually exclusive. All modern serving engines maintain a KV cache that stores the keys and values for previously-seen sequences. When new requests include a sequence that exists in the cache (including the system prompt, usually), the KV tensors for that sequence are fetched instead of being recomputed.

Though prefix caching is powerful, it doesn't eliminate the decode cost. Every time the model generates a token, that token attends over every key in the sequence, cached or not. Because decode is memory-bandwidth-bound, every generated token must stream the entire KV cache from high bandwidth memory, and that read grows linearly with the cached sequence length. Gisting reduces the cost of attention computations and KV cache reads, the latter of which is especially impactful on throughput when batch sizes grow large.

The optimizations of gisting and prefix caching compound, and we use both in our experiments and production serving stacks.

## Autoresearch found the recipe

To tune our hyperparameters, we pointed an [autoresearch loop](https://shopify.engineering/autoresearch) at the trainer. It proposes a recipe, trains gist embeddings, evaluates the resulting model, and repeats.

![Autoresearch progress](https://cdn.shopify.com/s/files/1/0779/4361/files/Autoresearch_progress.png?v=1787079011)

During the autoresearch loop, three optimizations in particular had high impact:

- 
**Initialization** : Instead of initializing the embeddings with random noise, we split the system prompt into sequences of length*k* (where*k* is derived from the*k* :1 compression ratio) and initialized the*n* th gist embedding with the mean of the*n* th system prompt chunk. This optimization reduced our initial loss by a factor of 7.
- 
**Compression** : After experimenting with a range of compression ratios, we found the ratio beyond which prediction quality began to degrade (4:1 was the optimal ratio for the complexity of our domain; other domains vary).
- 
**Data quantity and diversity** : Curating a large and diverse dataset closed the remaining gap.

In addition to streamlining hyperparameter tuning, autoresearch also helped us implement several key optimizations in our training infrastructure. The first was how we normalized the loss: averaging per response token made the model hallucinate, while averaging over the batch preserved more signal from long responses and produced stable embeddings. The second was speed: precomputing the teacher logits and pre-tokenizing the data cut a full run from thirty hours to six.

## The payoff: latency and throughput

We ran load tests comparing the same model with the compressed prompt against the full-prompt.

Gisting results in significant latency gains over the full prompt, and the gap becomes even more pronounced as request concurrency rises and batches get larger. At 350 RPM, TTFT dropped 19%, E2E latency dropped about 38%, and throughput increased by 16%.

In practice, that 16% gain in throughput translated directly into GPU savings on our production workload. With the hardware configuration serving our GraphQL traffic, we were able to use 14% fewer GPUs with gisting.

![The results](https://cdn.shopify.com/s/files/1/0779/4361/files/TTFT_E2E.png?v=1787079042)

## Gisting and continual learning

Gisting also feeds nicely into [Shopify’s continual learning loop](https://shopify.engineering/sidekicks-continual-learning-loop). Once we have the distilled gist embeddings for a model, we can treat that model as a new starting point for continual learning. We can post-train using the gist embeddings as the prefix and apply the gradient updates to both the model weights and the gist embeddings. By optimizing both the weights and gist embeddings on the incremental data, we can continuously calibrate and improve the model without the computational load of distilling the gist embeddings from scratch each time. 

## The takeaway

Long system prompts are useful but expensive. Gisting allows agents to leverage all the advantages of extensive instructions with a fraction of the tokens, reducing their latency and GPU spend. In the recent era of GPU demand outpacing supply, every inference optimization matters, but we also refuse to compromise on quality. Gisting gives us both, and at Shopify, it is the new standard.

**References**

1. Wingate, Shoeybi, and Sorensen. Prompt Compression and Contrastive Conditioning for Controllability and Toxicity Reduction in Language Models. [2022](https://arxiv.org/abs/2210.03162).
