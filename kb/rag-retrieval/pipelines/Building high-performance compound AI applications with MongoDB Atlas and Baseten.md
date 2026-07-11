---
title: Building high-performance compound AI applications with MongoDB Atlas and Baseten
topic: rag-retrieval
subtopic: pipelines
secondary_topics:
- product-engineering/architecture
summary: Shows how to build high-performance compound AI applications with retrieval,
  orchestration, and model serving.
source: baseten
url: https://www.baseten.co/blog/building-high-performance-compound-ai-applications-with-mongodb-atlas-and-baseten/
author: Philip Kiely
published: '2024-09-17'
fetched: '2026-07-11T04:09:01Z'
classifier: codex
taxonomy_rev: 1
words: 1586
content_sha256: 5a00a157fc9698865984edbff8136e8f0598b07f55334a6470130cdd75d2e874
triage: keep
skip_reason: null
---

# Building high-performance compound AI applications with MongoDB Atlas and Baseten

![MongoDB + Baseten](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1747437717-google-cloud-1.png%3Fauto%3Dformat%26fit%3Dcrop%26h%3D630%26w%3D1200&w=3840&q=100)

Compound AI systems combine multiple AI models to power more advanced workflows than can be achieved with individual models. But these multi-step processes can introduce high latency and performance bottlenecks in production applications. Using [MongoDB Atlas](https://www.mongodb.com/atlas) and [Baseten’s Chains framework](https://www.baseten.co/blog/introducing-baseten-chains/) for compound AI, you can build high-performance compound AI systems like RAG that can scale to handle massive production traffic without introducing bottlenecks.

![A diagram comparing single model AI and compound AI with multiple components.](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1722960435-untitled-6.png%3Fauto%3Dformat%26w%3D1200&w=3840&q=75) In contrast to single model AI, compound AI systems combine multiple models and processing steps.

In contrast to single model AI, compound AI systems combine multiple models and processing steps.## What is compound AI?

A [compound AI system](https://www.baseten.co/blog/compound-ai-systems-explained/) integrates multiple AI models and processing steps to form a cohesive, modular workflow capable of handling complex tasks. Unlike traditional monolithic AI systems that rely on a single model tightly coupled with specific hardware, compound AI systems leverage the strengths of various models, processing techniques, and architectures.

Compound AI systems can incorporate diverse components, including:

- Multiple AI/ML models across various modalities.
- Interfaces with databases, vector stores, and API endpoints.
- Processing stages for chunking or formatting input or output data.
- Varying hardware configurations to optimize performance and flexibility.

The modularity of compound AI systems allows for greater adaptability, enabling developers to modify or expand individual components without overhauling the entire system.

### What are some examples of compound AI?

Compound AI systems are useful for anything that you can’t do with an AI model right out of the box. Compound AI powers the most popular AI workflows: agents, phone calling, advanced image processing, intelligent routing, LLM as judge. When working with single models, compound AI can also be useful, for example in orchestrating high-throughput batch processing.

![A diagram comparing monolithic AI with one workflow tightly coupled to its hardware, and compound AI with multiple models and processings steps, each with their own hardware.](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1722960410-untitled-5.png%3Fauto%3Dformat%26w%3D1200&w=3840&q=75) Monolithic AI uses single models tightly coupled with their infrastructure, while compound AI leverages multiple modularized processing components.

Monolithic AI uses single models tightly coupled with their infrastructure, while compound AI leverages multiple modularized processing components.### Is retrieval-augmented generation (RAG) compound AI?

Yes! Looking at the definition of compound AI — multi-step, multi-model workflows that unlock new capabilities that aren’t present in the foundation model. Let’s take a look at those three criteria:

- **Multi-step**: RAG systems have several steps: embedding the initial query, vector search, prompt building, and of course the LLM inference.
- **Multi-model**: RAG requires both embedding and language models.
- **New capabilities**: LLMs don’t have domain-specific or up-to-date knowledge, which is provided by RAG.

RAG is a perfect example of a compound AI workflow. It fits all three parts of the definition and demonstrates the power of compound AI.

## Steps for retrieval-augmented generation

Building a RAG system requires three components: an [information embedding model](https://www.baseten.co/blog/deployment-and-inference-for-open-source-text-embedding-models/), an LLM, and a vector store like MongoDB Atlas. There is initial setup, like selecting the right embedding model, populating the vector database with a corpus of data, and building a prompt framework for the LLM. But these are one-time tasks, while the compound AI system we’ll build will run in production every time a user queries it.

Below, we’ll discuss the bottlenecks that can make these frequently-used RAG workflows slow and expensive. But first, we’ll establish a shared definition of the steps involved in RAG to see where we can eliminate inefficiencies.

For simplicity, we’ll base this example around a popular RAG use case: chat with your docs. The user will send a query about the documentation for a specific platform that is not within the LLM’s knowledge cutoff.

### Embed the initial query

First, we need to embed the initial query to pass it to the database. This requires an embedding model, which usually needs only a small GPU like an NVIDIA L4 for low-latency inference. It’s essential to use the same embedding model for live inference that was used for corpus generation, otherwise the vectors won’t make meaningful comparisons.

### Vector search with MongoDB Atlas

In this step, we accurately retrieve relevant context to pass to the large language model. In this example, we’d be retrieving chunks of documentation from the original corpus that are relevant to the user’s question.

Using MongoDB Atlas Vector Search, we can compare the vector generated by the query across an index of our database. The comparison can use your choice of algorithm, like euclidean distance or cosine similarity. MongoDB Atlas Vector Search gives you full control over the retrieval step while fully managing the underlying infrastructure.

### Build the final prompt

The information retrieved from the database needs to be assembled into a prompt for the LLM. This can look like providing context, building few-shot examples, or other prompt engineering to ensure that the model understands the question and relevant information.

This is generally a string template or concatenation that can execute nearly instantly on a small CPU-only instance.

### Run LLM inference

In the final step, we pass the prompt with context to the large language model, which will use the provided information to answer the user’s question. This generally requires one or more powerful GPUs for low-latency inference.

## Potential bottlenecks in compound AI systems

Each of these steps – query embedding, vector search, prompt building, and LLM inference – need to be optimized individually for a low-latency, high-throughput production system.

There are great tools for optimizing individual steps. High-performance model serving frameworks like [TensorRT-LLM](https://www.baseten.co/blog/high-performance-ml-inference-with-nvidia-tensorrt/) and TEI make inference on the LLM and embedding model fast, and MongoDB Atlas Vector Store provides scalable, reliable vector retrieval out of the box. But the system also needs to be optimized cohesively to make sure that no one step is holding up the others.

![A diagram of a compound AI system with specific resource allocation (GPU vs. CPU) per node.](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1722960266-untitled-7.png%3Fauto%3Dformat%26w%3D1200&w=3840&q=75) A compound AI pipeline with modularized, custom hardware. Only the AI models use GPUs.

A compound AI pipeline with modularized, custom hardware. Only the AI models use GPUs.### Appropriate hardware allocation

Which hardware setup would be the most appropriate for a RAG system: a single-core CPU-only instance, a small L4 GPU, or multiple H100 GPUs?

The answer is all of the above! While any one hardware package would not be appropriate for every step – it’s completely infeasible to run an LLM on a CPU, while the H100 GPUs would be massively cost-inefficient for text embedding – we can assign each step in the compound AI workflow the appropriate hardware resources.

For generating text embeddings, an L4 or similar GPU is the right fit for low-cost, low-latency inference. The middle part of the pipeline, communicating with the vector store and assembling the prompt, is a CPU workload. Finally, the best hardware can be reserved for where it can make the biggest impact: LLM inference.

Not only must the appropriate hardware be allocated, but it also must be scaled individually. Rather than having the same number of replicas for each step, the infrastructure must automatically scale in response to traffic to ensure that no step becomes a bottleneck.

### Minimized network overhead

Introducing multiple compute stages, as well as network calls, can add a lot of latency to a system if not managed carefully. Strategies for addressing this include co-locating inference compute with other services like vector databases, reducing the need for long-distance round trips. Additionally, leveraging in-database search and processing can reduce communication overhead. Finally, building a tightly integrated inference system ensures that even complex workflows remain performant.

### Batching and throughput

As data moves through various stages – such as preprocessing, model inference, and post-processing – the need to batch data effectively becomes critical to maintain high throughput. However, improper batching strategies can lead to increased latency and reduced system efficiency.

## How to eliminate bottlenecks from your compound AI systems

By combining MongoDB Atlas Vector Store for data retrieval and Baseten for model inference, you can build scalable, secure, performant compound AI applications, including RAG systems.

### Use MongoDB Atlas Vector Store for low-latency retrieval

MongoDB Atlas offers a native vector search capability embedded within its operational database, making it an ideal solution for compound AI systems like RAG. By storing, indexing, and querying vector embeddings alongside other data types, developers can enhance the accuracy of LLMs. This integration simplifies the development process, allowing teams to iterate quickly and adapt to changing data requirements with minimal effort.

The flexible document data model in MongoDB Atlas supports a wide variety of multimodal data, including text, images, and sound files, supporting all kinds of compound AI systems. With its robust scalability, security features, and serverless architecture, MongoDB Atlas provides the performance and reliability needed to serve global customers while maintaining low-latency retrieval and high availability. This makes it ideal for integrating into flexible autoscaling compound AI applications.

### Use Baseten Chains for workload orchestration

Baseten’s [open-source Chains framework](https://www.baseten.co/products/chains/) streamlines the process of [building high-performance compound AI systems in production](https://www.baseten.co/blog/baseten-chains-explained/). Chains provides modular workflow composition with independent GPU and CPU resource allocation — this way only the LLM is using the powerful-but-expensive GPU required for inference, while other parts of the system run on more appropriate hardware.

With Chains, you can [build performant, reliable, scalable infrastructure for compound AI](https://www.baseten.co/blog/introducing-baseten-chains/) with a streamlined development process and a comprehensive local testing story. Discover the flexibility and power of loosely coupled but tightly integrated interactions between models, hardware, and services as you build your next compound AI system with Baseten Chains.
