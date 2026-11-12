---
title: The best open-source embedding models
kind: blog
topic: rag-retrieval
subtopic: embeddings
secondary_topics: []
summary: Curated comparison of open-source embedding models for RAG/search, recommending
  Qwen3 8B Embedding in FP8 on B200 for top quality and EmbeddingGemma (Matryoshka
  Representation Learning, <500M params, best-in-class MTEB for its size) for lower-cost
  deployments.
triage: null
skip_reason: null
source: baseten
url: https://www.baseten.co/blog/the-best-open-source-embedding-models
author: Philip Kiely
published: '2025-04-04'
fetched: '2026-11-12T06:13:50Z'
classifier: claude
taxonomy_rev: 2
words: 1073
content_sha256: aa5638f04c45c1359b22d577e023ce72537c61725bc23b54f01756916be7c141
---

# The best open-source embedding models

AI engineering
# The best open-source embedding models

Discover the best open-source embedding models for search, RAG, and recommendations—curated picks for performance, speed, and cost-efficiency.


- Authors
- Date
- April 4, 2025

Embedding models are the foundation of AI-powered search, retrieval, and recommendation systems. But with over 100,000 embedding models available on Hugging Face, selecting the ideal one often involves complex trade-offs among accuracy, embedding speed, and cost—particularly when models excel at different applications.

Taking what we’ve learned from technical benchmarks, customer feedback, and our internal testing, we've curated this list of embedding models to help you confidently select the right one for building everything from agents to RAG pipelines to recommendation engines.

Developed by the Qwen lab at Alibaba, [Qwen3 8B Embedding](https://www.baseten.co/library/qwen3-8b-embedding/) excels in generating high-quality English text embeddings for a wide range of topics and use cases. We used this model for [benchmarking our Baseten Embedding Inference (BEI) runtime on NVIDIA B200 GPUs](https://www.baseten.co/blog/run-qwen3-embedding-on-nvidia-blackwell-gpus/) due to its versatility and architectural similarity to a large number of high-quality embedding models.

We recommend running Qwen3 8B Embedding in FP8 on an NVIDIA B200 GPU for best performance.

- **Size:** 8B parameters
- **Base model:** Qwen3
- **License:** Apache 2.0

You can deploy [Qwen3 8B Embedding](https://www.baseten.co/library/qwen3-8b-embedding/) from our model library.

If you want a still-excellent but lower-cost embedding model, consider [EmbeddingGemma](https://www.baseten.co/library/embeddinggemma/). The model uses Matryoshka Representation Learning and supports over 100 languages, while scoring an industry-best for models under 500 million parameters on the [MTEB benchmarks](https://github.com/embeddings-benchmark/mteb).

For efficient, cost-effective inference, try this model on H100 MIG GPUs.

- **Size:** 300M parameters
- **Base model:** Gemma3
- **License:** Apache 2.0

Deploy [EmbeddingGemma](https://www.baseten.co/library/embeddinggemma/) from our model library.

Like LLMs, embedding models can be optimized for performance in specific domains. Nomic’s [code embedding model](https://huggingface.co/nomic-ai/nomic-embed-code) delivers outstanding performance on code embedding and retrieval tasks, rivaling the best closed-source models (and outperforming general embedding models). We recommend running Nomic Embed Code on an H100 GPU or H100 MIG, depending on the required throughput, with FP8 for optimal performance.

- **Size:** 7B parameters
- **Base model:** Qwen2Model
- **License:** Apache 2.0

[Try Nomic Embed Code](https://www.baseten.co/library/nomic-embed-code/) from our model library.

Developed by the Beijing Academy of Artificial Intelligence (BAAI), [bge-reranker-v2-m3](https://huggingface.co/BAAI/bge-reranker-v2-m3) is a performant and efficient reranking model. These models are often used in RAG systems, where a first pass of vector retrieval might surface dozens or snippets of data as context, to reorganize the context based on relevance. For high-throughput or latency-sensitive use cases, we recommend an H100 MIG GPU for this model despite its smaller size.

- **Size:** 279M parameters
- **Base model:** XLMRobertaForSequenceClassification
- **License:** Apache 2.0

Get started with bge-reranker-v2-m3 from our model library.

Reward models are essential in reinforcement learning as they provide immediate feedback to an agent, indicating the success or failure of its actions, which is crucial for adjusting policies and improving performance over time. AllenAI’s [Tulu model](https://huggingface.co/allenai/Llama-3.1-Tulu-3-8B-RM) is particularly effective due to its advanced instruction-following capabilities for a wide range of tasks. As the model is based on Llama 3.1 8B, it’s slightly larger than the others listed in this article and benefits from a full H100 GPU for efficient inference.

- **Size:** 8B parameters
- **Base model:** LlamaForSequenceClassification
- **License:** Llama 3.1

You can test Tulu 3 8B Reward from our model library.

Embedding models quietly power a wide range of AI applications, including:

- **AI Agents**: Providing agentic systems with access to essential information to make decisions.
- **RAG Pipelines**: Adding relevant context to LLM inference.
- **Semantic Search:** Enhancing search engines to retrieve results based on meaning rather than keyword matching.
- **Text Classification:** Categorizing documents, emails, or customer feedback into predefined labels.
- **Recommendation Systems:** Providing personalized content suggestions by understanding user preferences.

Additionally, reward models are increasingly useful for training and fine-tuning projects, especially with RL-based reasoning models.

When choosing an embedding model, it’s natural to look at benchmarks and leaderboards to figure out what the best model to use is. But can you trust these numbers?

In general, yes. Resources like the [MTEB leaderboard](https://huggingface.co/spaces/mteb/leaderboard) are trustworthy sources of benchmark data that are useful for apples-to-apples comparisons between models. However, benchmarks don’t tell the whole story. Just because a model is better on a given benchmark does not mean it will be better for your data. New models are coming out all the time with new benchmarks and taking top position on leaderboards, but you should only switch if you see a meaningful difference in your own real-world product metrics.

Open source embedding models like the ones recommended here routinely match or exceed the quality of closed-source options on both benchmark leaderboards and real-world testing. New embedding models, both open and closed, are constantly released, and embedding models can be fine-tuned on your data for even greater accuracy.

Besides output quality, there are a number of reasons to choose open-source models. Sticking with open source gives you control over your AI systems. You can run your model anywhere without worrying about service interruptions or deprecations, which is important because switching embedding models requires re-processing your entire corpus. Additionally, with open-source models, you can optimize your own systems for latency and throughput to get better performance and save on cost.

Optimizing embedding model performance is a two-part challenge. First, you need a high-throughput inference engine to process your initial corpus of texts. Then, you need a low-latency model server that can handle many simultaneous user requests.

We built [Baseten Embedding Inference (BEI)](https://www.baseten.co/blog/introducing-baseten-embeddings-inference-bei/) to address both of these challenges. BEI is the highest-performance embedding model inference engine in the world, with best-in-class throughput and latency for every model listed in this article.

Even more than embedding, reranking, and reward scoring, classification models are incredibly task-specific, making it difficult to recommend a single model. It’s often easiest to use an LLM with careful prompting and [structured output](https://www.baseten.co/blog/how-to-build-function-calling-and-json-mode-for-open-source-and-fine-tuned-llms/) for classification tasks.

The best open-source embedding model is the one that performs the best for your use case. Balancing capabilities, dimensionality, and hardware requirements, the right embedding model makes agents, RAG pipelines, search, and recommendations faster and more accurate. Finding the right model might take some experimentation, but will power new capabilities in your AI application.

Deploy the best embedding models from the Baseten model library:

- Best overall embedding model: [Qwen3 8B Embedding](https://www.baseten.co/library/qwen3-8b-embedding/)
- Best model under one billion parameters: [EmbeddingGemma](https://www.baseten.co/library/embeddinggemma/)
- Best code embedding model: [Nomic Embed Code](https://www.baseten.co/library/nomic-embed-code/)
- Best reranking model: BAAI bge-reranker-v2-m3
- Best reward model: Tulu 3 8B Reward
