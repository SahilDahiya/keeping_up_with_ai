---
title: Fast, accurate retrieval with NVIDIA Nemotron 3 Embed
kind: blog
topic: rag-retrieval
subtopic: embeddings
secondary_topics:
- inference/quantization
summary: 'Compares NVIDIA''s Nemotron 3 Embed 8B and 1B embedding models available
  on Baseten: the 1B model uses pruning, distillation, and NVFP4 quantization to retain
  95% of the 8B''s retrieval accuracy (99% in NVFP4 on Blackwell, 2x throughput) while
  cutting indexing latency and serving cost; also covers a fine-tuning recipe yielding
  ~10% accuracy gains in 5 hours.'
triage: null
skip_reason: null
source: baseten
url: https://www.baseten.co/blog/ai-retrieval-nvidia-nemotron-3-embed/
author: Albert Lee
published: '2026-07-16'
fetched: '2026-07-17T06:46:31Z'
classifier: claude
taxonomy_rev: 2
words: 1052
content_sha256: 8b55e61cf69791ea26fa274ace04c14ae03c984eb7c83509bb94fc6bb0ea3400
---

# Fast, accurate retrieval with NVIDIA Nemotron 3 Embed

![NVIDIA Nemotron 3 Embed models are now available in Baseten.](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1784067225-model-releases-4.png%3Fauto%3Dformat%26fit%3Dcrop%26h%3D630%26w%3D1200&w=3840&q=100)

[NVIDIA Nemotron 3 Embed](http://huggingface.co/blog/nvidia/nemotron-3-embed-wins-rteb) helps AI systems find relevant information in large collections of text and code. The larger 8B model delivers leading retrieval accuracy, while the smaller, faster 1B model retains 95% of that accuracy. Both are now available on Baseten for AI agents, enterprise search, and code retrieval.

Starting today, NVIDIA Nemotron 3 Embed 8B and NVIDIA Nemotron 3 Embed 1B are available on Baseten, giving developers two complementary options for balancing retrieval accuracy with indexing speed.

## Embeddings are the memory layer for retrieval

Retrieval starts by giving information an address.

An embedding model converts data, like text, into a list of numbers called an **embedding**. In this mathematical space, passages with similar meanings sit close together, even when they use different words. A **vector index** stores these embeddings and makes them fast to search.

When an agent or coding assistant needs more information, it can search the index to find the most relevant context for its task.

![Nemotron 3 Embed converts knowledge sources into embeddings stored in a vector index. It then embeds user queries to retrieve the most relevant context.](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1784066790-nemottron-3-diagram-01_ld.png%3Fauto%3Dformat%26w%3D1200&w=3840&q=75) Nemotron 3 Embed converts knowledge sources into embeddings stored in a vector index. It then embeds user queries to retrieve the most relevant context.

Nemotron 3 Embed converts knowledge sources into embeddings stored in a vector index. It then embeds user queries to retrieve the most relevant context.Two common use cases show how this works in practice:

**Agentic retrieval:** An AI agent can find relevant information across enterprise knowledge bases, documentation, and internal systems, helping it answer questions and complete tasks. Better retrieval leads to better context, and ultimately better answers.

**Code retrieval:** A coding assistant can surface relevant files, functions, and dependencies across a large codebase, especially when the full repository can’t fit in the model’s context window. Better retrieval helps developers receive more accurate implementation guidance.

## Retrieval quality comes with a cost

Larger embedding models can produce higher-quality semantic representations, helping retrieval systems find more relevant information. However, they also require more processing time and hardware to generate embeddings. As documentation is revised, runbooks change, and pull requests land, slower indexing can leave a system searching an outdated version of its knowledge.

![Updates accumulate in an embedding queue. When the embedding model can’t process changes quickly enough, the vector index becomes stale and the retrieval system may return outdated context.](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1784066897-nemottron-3-diagram-02_ld.png%3Fauto%3Dformat%26w%3D1200&w=3840&q=75) Updates accumulate in an embedding queue. When the embedding model can’t process changes quickly enough, the vector index becomes stale and the retrieval system may return outdated context.

Updates accumulate in an embedding queue. When the embedding model can’t process changes quickly enough, the vector index becomes stale and the retrieval system may return outdated context.Agentic and code retrieval both face this tradeoff. Agents need to reason across sprawling enterprise knowledge, while coding assistants need to keep up with codebases that may change hundreds of times a day. Larger models can improve relevance, while smaller models can refresh the index faster as the underlying information changes.

The best embedding model isn’t simply the most accurate one. It’s the one that balances retrieval quality with indexing speed for the workload.

## Two models for different priorities

NVIDIA designed [Nemotron 3 Embed](http://huggingface.co/blog/nvidia/nemotron-3-embed-wins-rteb) to combine high retrieval quality with the speed and efficiency needed for production workloads. Rather than forcing every use case into the same compromise, Nemotron 3 Embed offers two model sizes.

**Nemotron 3 Embed 8B** delivers leading retrieval quality across major benchmarks - topping the RTEB leaderboard across both open and closed models. Choose it whenever retrieval quality is the highest priority.

**Nemotron 3 Embed 1B** combines pruning — which removes less important parts of a model — and distillation — which trains a smaller model to reproduce the behavior of a larger one — to retain 95% of the 8B model’s retrieval accuracy while substantially reducing serving cost and indexing latency. For NVIDIA Blackwell GPUs, the NVFP4 version delivers up to 2x higher throughput while retaining 99% of BF16 accuracy.

Together, the two models let teams optimize for either maximum retrieval quality or production-scale efficiency.

## Choose based on what matters most

Choose **Nemotron 3 Embed 8B** when a missed or irrelevant result is mission critical. It’s the better fit for complex enterprise collections of information and accuracy-critical workloads where maximizing retrieval quality matters more than how quickly the index can be updated.

Choose **Nemotron 3 Embed 1B** when you need to index large amounts of content or refresh the index frequently. It generates embeddings faster and more efficiently while retaining 95% of the 8B model’s retrieval accuracy.

## Bringing Nemotron 3 Embed to turbopuffer

Choosing an embedding model is easier when teams can test it within their existing retrieval stack. That’s why we’re partnering with [turbopuffer](https://turbopuffer.com/) to make Nemotron 3 Embed available through its [native embeddings](https://turbopuffer.com/docs/embedding).

turbopuffer is a vector and full-text search engine built for AI applications. Its native embeddings reduce the engineering work required to deliver relevant semantic search results.

That matters because getting search relevance right is hard. Teams need to compare models, tune their retrieval systems, and potentially re-embed documents as better options become available. By supporting existing and new, state-of-the-art embedding models, turbopuffer helps customers choose the right balance of retrieval quality, speed, and cost for their use case.

As part of our partnership, we gave turbopuffer early access to Nemotron 3 Embed so the team could test the model and make it available through turbopuffer’s native embeddings. We’re excited to keep working together to help teams bring high-quality retrieval to production.

## Put Nemotron 3 Embed into production

Both Nemotron 3 Embed models are available in the Baseten Model Library for [Dedicated Inference](https://www.baseten.co/products/dedicated-inference/), giving teams a ready-to-deploy path to production without managing the underlying infrastructure.

For workloads with specialized terminology, data, or relevance requirements, NVIDIA’s [Nemotron Embed fine-tuning recipe](https://github.com/NVIDIA-NeMo/Nemotron/tree/main/docs/nemotron/embed) provides a path for adapting the models to a specific domain and can easily be run on Baseten Training. In-domain fine-tuning delivers ~10% accuracy improvement within just 5 hours. Fine-tuned models can then be [packaged with Truss](https://docs.baseten.co/development/model/overview) and deployed on Baseten.

Whether you use a Model Library deployment or a fine-tuned model, once it’s deployed, [generate an API key](https://docs.baseten.co/organization/api-keys) and start creating embeddings for your knowledge sources.
