---
title: Announcing Embeddings and Reranking On Fireworks
kind: blog
topic: null
subtopic: null
secondary_topics: []
summary: null
triage: null
skip_reason: null
source: fireworks
url: https://fireworks.ai/blog/embeddings-and-reranking-announcement
author: null
published: '2025-10-09'
fetched: '2026-08-12T06:28:55Z'
classifier: null
taxonomy_rev: 2
words: 574
content_sha256: 3f20a154c4b05a67bb2df8fba3de6bec6aeee4d2a63cf4b921b1bb56cbaca7eb
---

# Announcing Embeddings and Reranking On Fireworks

Today, we're announcing a major upgrade to Fireworks for RAG workloads – we’re bringing the state-of-the-art **Qwen3 8B Embeddings** and **Reranking** models to serverless, and are introducing **two new API endpoints** to make it all easily accessible.

Now, whether you're building semantic search, recommendation systems, or agents powered by enterprise data, Fireworks makes it easier than ever to build scalable RAG applications with open models.

At a glance, a RAG pipeline consists of five core stages:

- •**Embed:** Split documents into chunks and turn each chunk into a high‑dimensional vector with an embedding model.
- •**Index:** Persist those vectors in a vector store (MongoDB, Chroma, pgvector, etc.).
- •**Retrieve:** Convert the user query into a vector, run an Approximate‑Nearest‑Neighbor (ANN) search, and pull the most relevant chunks.
- •**Rerank:** Apply a dedicated reranker model to the retrieved set, scoring each query‑chunk pair more precisely and selecting the top candidates.
- •**Synthesize:** Feed the final context to an LLM, which generates the answer.

**The problem:** Until now, teams have had to cobble together different providers for embeddings, reranking, and generation. The result is a pipeline that is complex, inconsistent, and hard to scale. Even though open models are [crushing the leaderboards](https://huggingface.co/spaces/mteb/leaderboard) on embeddings and reranking tasks, AI teams are forced to choose between the operational pain of self‑hosting these models and the cost of closed‑source model APIs.

Now, with native support for embeddings and reranking, Fireworks lets you run every step of the RAG workflow on open models–efficiently, at scale, and on the same virtual cloud that powers mission‑critical workloads for customers like Cursor, Notion, and Cresta.

In particular, RAG workloads on Fireworks benefit from

- •Top-tier performance, from the moment a document is embedded to the final answer you generate
- •Frictionless scalability with global availability through our distributed infrastructure across 8 CSPs
- •Consistent developer experience across embedding, reranking, and generation tasks
- •Unified, pay‑as‑you‑go billing across all model workloads

We are excited to launch serverless support for the state-of-the-art Qwen3 Embeddings 8B and Qwen3 Reranker 8B models, with their 4B and 0.6B variants available via on-demand deployments.

We also support the following BERT-based embeddings models on serverless

- •`nomic-ai/nomic-embed-text-v1.5` and `nomic-ai/nomic-embed-text-v1`
- •`WhereIsAI/UAE-Large-V1`
- •`thenlper/gte-large` and `thenlper/gte-base`
- •`BAAI/bge-base-en-v1.5 and BAAI/bge-small-en-v1.5`
- •`mixedbread-ai/mxbai-embed-large-v1`
- •`sentence-transformers/all-MiniLM-L6-v2`
- •`sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2`

In addition, any LLM on Fireworks can be queried for embeddings, including models you bring yourself through custom model upload (as long as the architecture is [supported by Fireworks](https://docs.fireworks.ai/models/uploading-custom-models)).

We’re excited to be unveiling two new endpoints for interacting with embeddings and reranking models **/v1/embeddings** and **/v1/rerank.** 

(Note: Qwen3 Reranker only)

Here’s an example of querying an embedding model. Simply pass the text you want to embed as an input and the resulting vector can be passed to a downstream storage solution like a vector database.

123456789101112131415161718

And here is an example of querying the Qwen3 Reranker model

1234567891011121314151617181920212223242526

To get started with embeddings and reranking on Fireworks, check out our [docs](https://docs.fireworks.ai/guides/querying-embeddings-models)! For a deeper dive into scaling embeddings and reranking, check out our For a deeper dive into scaling embeddings and reranking, check out our [previous blog post](https://fireworks.ai/blog/Understanding-Embeddings-and-Reranking-at-Scale).

We’re excited to continue building out more features for embeddings and reranking on Fireworks over the coming months. If you have a model you’d love to see enabled or a feature that would supercharge your RAG agent, we want to hear from you -- reach out via [inquires@fireworks.ai](mailto:inquires@fireworks.ai). Your feedback directly helps us shape the roadmap.
