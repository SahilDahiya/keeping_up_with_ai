---
title: 'How we built BEI: high-throughput embedding, reranker, and classifier inference'
kind: blog
topic: inference
subtopic: optimization
secondary_topics:
- rag-retrieval/embeddings
summary: Details building Baseten Embedding Inference (BEI) on TensorRT-LLM to double
  throughput for embedding, reranker, and classifier models, addressing the dual demands
  of high-throughput corpus processing and millisecond real-time querying.
triage: null
skip_reason: null
source: baseten
url: https://www.baseten.co/blog/how-we-built-bei-high-throughput-embedding-inference
author: Michael Feil
published: '2025-03-27'
fetched: '2026-11-12T06:09:50Z'
classifier: claude
taxonomy_rev: 2
words: 1960
content_sha256: a6d9d46d5480439b6cf97f662ffeb8fadb423662722fe7e5da63081ebac8e55f
---

# How we built BEI: high-throughput embedding, reranker, and classifier inference

Model performance
# How we built BEI: high-throughput embedding, reranker, and classifier inference

Discover how we optimized embedding, reranker, and classifier inference using TensorRT-LLM, doubling throughput and achieving ultra-low latency at scale.


- Authors
- Date
- March 27, 2025

TLDR

We built Baseten Embedding Inference (BEI), an optimized inference runtime leveraging TensorRT-LLM to significantly boost throughput and minimize latency for embedding, reranker, and classification models. In this piece, we'll show the benchmarking methodology behind our claims of 2x higher throughput and detail the challenges we overcame to create the world's fastest embedding runtime.

Since the release of BERT in 2018, the humble embedding model has grown up in the shadow of LLMs, quietly powering critical AI tasks from search to reranking, classification, and retrieval. In the past year, embeddings models have shifted from BERT-based architectures to building on top of smaller language models from families like [Llama](https://www.baseten.co/library/family/llama/), [Qwen](https://www.baseten.co/library/family/qwen/), [Gemma](https://www.baseten.co/library/family/gemma/), and [Mistral](https://www.baseten.co/library/family/mistral/).

This new class of embeddings models is more accurate, scores better on benchmarks, and can handle more advanced use cases. However, they’re also substantially larger, going from a few hundred million parameters for BERT-based models to several billion for the most powerful LLM-based models.

These larger models require new approaches for inference optimization. Improving the performance of embeddings models is a unique challenge within the model performance space because you have to optimize for two very different workload profiles:

1. **Corpus processing:** An embedding inference runtime must be able to process extremely high-throughput workloads efficiently to handle multi-billion-token document processing tasks, or even multi-trillion-token training data preparation tasks.
2. **Real-time querying:** The runtime must also be able to handle individual requests with millisecond-level latency to support real-time queries against an existing corpus.

We built a new [inference stack](https://www.baseten.co/resources/guide/the-baseten-inference-stack/) for these language-based embeddings models that leverages [TensorRT-LLM](https://www.baseten.co/blog/automatic-llm-optimization-with-tensorrt-llm-engine-builder/) to achieve as much as double the throughput of previous industry standards. We’ve achieved our goal of making this stack a Pareto improvement that offers benefits across the board, including:

- Higher throughput to enable massive ingestion into vector databases
- Massive parallelism to scale workloads efficiently and handle traffic spikes
- Lower latency for one-off queries in real time
- Lower memory buffer consumption for improved hardware utilization

In this piece we will describe our approach to model inference optimization for [embedding models](https://www.baseten.co/resources/guide/high-performance-embedding-model-inference/). For more information on the use cases these faster embedding, reranking, classifier, and retriever models enable and instructions for getting started, check out our [launch blog for our new inference embedding runtime](https://www.baseten.co/blog/introducing-baseten-embeddings-inference-bei/).

Baseten Embedding Inference (BEI) is our new TensorRT-LLM-based runtime for high-performance embedding inference. We benchmarked BEI against the best open-source solutions on the market, including [TEI](https://github.com/huggingface/text-embeddings-inference), [vLLM](https://github.com/vllm-project/vllm), [Infinity](https://github.com/michaelfeil/infinity), and [Ollama](https://github.com/ollama/ollama).

To test system throughput, we created test requests where each request has 256 sentences and each sentence has 512 tokens – that’s 131,072 tokens per request. This is adapted from the [benchmarking scripts](https://michaelfeil.eu/infinity/0.0.51/benchmarking/) used by Infinity, an open-source embedding inference library developed by [Michael Feil](https://github.com/michaelfeil), one of the authors of this post.

We selected [BAAI/bge-icl](https://huggingface.co/BAAI/bge-en-icl), a leading model on the [MTEB leaderboard](https://huggingface.co/spaces/mteb/leaderboard), and ran it on a single H100 GPU (HBM3). This model is based on Mistral 7B, a seven-billion-parameter large language model.

BEI outperforms the competition by a large margin. In bfloat16, it can handle a 1.36x higher global throughput over competitors like vLLM and TEI. After quantizing the model to FP8, BEI offers 2.05x more throughput, while having the lowest memory consumption.

Beyond throughput, we are also interested in the user experience BEI can provide when deploying latency-sensitive tasks, like embedding a user query or reranking a small number of documents during a RAG pipeline. For these cases, we benchmark the single-sentence performance at eight tokens per request. BEI retains both the lowest latency on an idle server and the highest amount of concurrent requests per replica.

A single model server using BEI scales better-than-linearly under high load. In an extreme test, we implemented a C client and directly interacted with the server to minimize connection times. Using this setup, BEI can handle more than 1000 individual clients sending eight tokens per request.

Below, we’ll discuss the challenges we had to overcome to achieve these results and the methods we used to increase performance.

To maximize throughput, we want to run inference with very large batches. Without batching, embeddings inference is constrained by memory bandwidth. Batching allows us to perform more operations per memory read and approach a more desirable compute-bound state.

However, we also want to be able to handle very large token inputs, say up to 32,000 tokens in a single request. If we set our batch size based on the largest requests, we won’t have high throughput, but if we base it on the average request to increase throughput, many large requests at once can easily cause out of memory (OOM) errors.

However, batching with a token-based limit rather than a request-based limit would allow maximum throughput without the risk of OOM errors. Modern mechanisms like [sequence packing](https://huggingface.co/blog/modernbert) enable this, but they need to be supported in our runtime.

Memory buffers are allocated at startup, allowing us to run very large embeddings models like those based on a Llama-70B architecture, to run on a single H100 with 32,768 context using FP8.

When processing a large corpus, we generally need to scale past a single replica. In a traffic-based autoscaling system, we might run in a steady state with a handful of replicas serving production traffic, then get hit with a huge corpus to process.

This is an infrastructure challenge, not a model performance challenge. A production-grade queueing system must appropriately handle backpressure to keep everything running, enqueue additional requests as more replicas spin up (with fast cold starts), and distribute load evenly among the system as more replicas come online. Of course, the replicas will need to be gracefully spun down after the spike in usage.

We also benefit from [asynchronous inference](https://www.baseten.co/blog/using-asynchronous-inference-in-production/) for queue processing. With asynchronous inference, you get a response as soon as the request is enqueued. Once the inference output is ready, it’s returned via webhook. This asynchronous setup is ideal for many high-volume batch processing workloads.

Embedding models are built on a wide variety of architectures, from `BertModel` and `XLMRoberta` to `LlamaModel` and `MistralModel`. Within each architecture, there are innumerable subspecies of models, including models specific for classification and reranking tasks like `QwenForSequenceClassification`.

While plenty of low-latency runtimes are available on the market, it’s difficult to find a single runtime that supports multiple model architectures and modalities robustly and is optimized for extremely low-latency serving.

Like with throughput, latency is not purely a model performance issue. Network latency is always a material factor in production, even outweighing actual inference time in some cases. Infrastructure work around the embedding model server, from efficient routing to [workload colocation](https://www.baseten.co/blog/the-benefits-of-globally-distributed-infrastructure-for-ml-model-serving/) to traffic-based autoscaling, is critical for achieving state-of-the-art latencies in production.

We have built an embedding inference engine that offers double the throughput of previous SOTA for batch inference and improved latency for real-time queries.

Baseten embedding inference (BEI) is our performant runtime for embedding, reranking, reward, and classification models. It provides an OpenAI-compatible interface for text embedding models and a text-embeddings-inference compatible interface for all other models.

The core engine for BEI is TensorRT-LLM, which offers exceptional performance and consistent throughput without the risk of OOM errors. TensorRT-LLM supports many architectures, from BERT-based models to recent models derived from LLMs.

BEI has four main components:

1. The **model server** processes inputs and outputs and handles any errors. BEI uses the Rust-based frontend service from text-embeddings-inference for this task.
2. The **tokenizer** is a multi-core system responsible for turning requests into tokenized sentences.
3. The **batch manager** packs individual tokenized sentences into batches up to a maximum sequence size, using a scheduling policy to maximize GPU utilization, [minimize tail effects](https://hazyresearch.stanford.edu/blog/2025-03-04-thundermla), and preserve request order.
4. The **TensorRT-LLM inference engine** runs inference in C++ using tokenized batches and creates embeddings.

Each request flows through all four components on the way in, but skips the tokenizer on the way out as embedding and classification outputs are numerical.

TensorRT-LLM offers incredible performance for embedding models through optimized inference engines. We see at least a 15% speedup from enabling TensorRT-LLM into the stack, jointly with minimizing latency between the Rust frontend and TensorRT-LLM runtime.

Two highly relevant optimizations are the XQA kernel and layer fusing. TensorRT-LLM uses XQA as a fast variant of Flash Attention 3, which improves latency and throughput. Meanwhile, fusing multiple layers reduces memory access overhead and improves computational efficiency. This fusion technique minimizes the need to store intermediate results in memory, leading to faster execution times and lower latency during inference. This approach significantly outperformed other methods, such as adding [flash-attention-3 to TEI](https://github.com/michaelfeil/candle-flash-attn-v3), which we open-sourced in January.

Most importantly, these optimizations are equally effective in real-time and batch serving, so they help both workload profiles that we’re building for with embedding inference.

While H100 GPUs don’t offer much in terms of performance benefits for smaller BERT-based embedding models, they do provide meaningful improvements when serving larger LLM-based embedding models. In addition to the great performance that TensorRT-LLM achieves with the Hopper architecture, H100 GPUs add one key unlock: [FP8](https://www.baseten.co/blog/33-faster-llm-inference-with-fp8-quantization/).

By quantizing these language-based embedding models to FP8, we gain another 50% or more in throughput while retaining >99% cosine similarity to outputs from non-quantized models. For most workloads, this performance gain is more than worth the small hit to output quality.

Baseten’s implementation of traffic-based autoscaling supports enqueueing millions of requests while additional model serving replicas are brought online automatically with fast cold starts. As replicas come online, traffic is seamlessly routed to the new replicas rather than continuing to pile up behind the original servers. With this setup, you can scale up to process massive corpora of documents.

Additionally, Baseten lets you deploy models into your preferred cloud and region, or even in your own VPC, to minimize network overhead. And when you’re building with multiple models, like a RAG application with an embedding and reranking model alongside an LLM, Baseten’s [Chains framework](https://www.baseten.co/blog/baseten-chains-for-production-compound-ai-systems/) further reduces communication overhead between models.

BEI models can be deployed using our [TensorRT-LLM Engine Builder](https://www.baseten.co/blog/automatic-llm-optimization-with-tensorrt-llm-engine-builder/), making it easy to get started and deploy any open-source or fine-tuned model with a supported architecture.

In the long run, our model performance work aims to make open-source models viable alternatives to closed models (e.g., OpenAI `text-embeddings-3`) by creating low-latency, high-throughput, feature-compatible model servers. Today, open-source models like the `mixedbread reranker-v2` series and `tulu-reward` model outperform closed-source counterparts for reranking and classification. This gives developers flexibility in picking a model or bringing their own, along with the privacy, cost, and reliability benefits of running on dedicated infrastructure.

Embedding models, as well as similar models for retrieval, reranking, reward, and classification are a particularly exciting set of models to work with. Embedding and reranking models have already proven useful in multi-model systems like RAG. Calculating embedding similarity to hydrate context, using reranking to surface the most relevant information, and a reward model to pick the best output to return to the user massively improves RAG quality. If these models can be run quickly enough, the user can’t even perceive the additional latency.

And even more exciting use cases are emerging from frontier research. Embedding models are important for synthetic data usage, as well as pre-processing large batches of synthetic data for training. With the rise of RL-based reasoning models, classification and reward models are increasingly important during training.

Whether you’re using a reward model to score chat history or a classification model for content moderation, a high-volume, low-latency model serving runtime makes your system more user-friendly and cost-effective. You can [learn more about BEI in our launch blog post](https://www.baseten.co/blog/introducing-baseten-embeddings-inference-bei/) and try it for yourself using [this tutorial to get started](https://docs.baseten.co/examples/bei).
