---
title: Deployment and inference for open source text embedding models
kind: blog
topic: rag-retrieval
subtopic: embeddings
secondary_topics: []
summary: Overview of deploying open-source text embedding models for search, RAG context
  retrieval, recommendations, and classification, stressing that the same embedding
  model must be used consistently for both corpus indexing and query time.
triage: null
skip_reason: null
source: baseten
url: https://www.baseten.co/blog/deployment-and-inference-for-open-source-text-embedding-models
author: Philip Kiely
published: '2023-11-02'
fetched: '2026-11-12T06:13:42Z'
classifier: claude
taxonomy_rev: 2
words: 1335
content_sha256: 7fbab5eacc4eabed38d677f6322134bb61182940402d460391d2b11dde8fae7b
---

# Deployment and inference for open source text embedding models

AI engineering
# Deployment and inference for open source text embedding models

Text embedding models convert text into semantic vectors. Numerous open source models cater to search, recommendation, classification & LLM-augmented retrieval.


- Authors
- Date
- November 2, 2023

TLDR

A text embedding model transforms text into a vector of numbers that represents the text’s semantic meaning. There are a number of high-quality open source text embedding models for different use cases across search, recommendation, classification, and retrieval-augmented generation with LLMs.

Text embedding models aren’t flashy like large language models, but they’re a foundational piece of the natural language processing field and a key component for building production-ready applications on LLMs.

At face value, turning nice human-readable text into a long list of numbers might seem pointless. One text embedding can’t be used for much. But creating embeddings from a corpus of text—say every post on your blog or every paragraph in your documentation—enables use cases like:

- **Search**: given a query, create an embedding of that query and compare its similarity with embeddings from the data set, and return the most relevant content.
- **Retrieval-augmented generation (RAG)**: use embedding search to grab chunks of content to use as context for text generation with LLMs.
- **Recommendations**: surface related content like similar blog posts or podcast episodes.
- **Classification and clustering**: categorize text by similarity.

As each of these use cases relies on creating a set of embeddings, it’s important to use the same embeddings model for both the initial dataset and any subsequent embeddings (such as search queries).

A text embedding encodes a chunk of text as a vector (a list of floating-point numbers). This vector represents the text’s meaning in an n-dimensional space.

This is difficult to visualize at the scale of real text embedding models, which have hundreds of dimensions, but here’s a simple example in two dimensions:

Here, we have a simplified two-dimensional vector space for sentences. The sentences are clustered by similarity, with the same change in a sentence (e.g. yellow -> red) resulting in the same direction and magnitude of shift in sentence location.

Of course, what’s happening in the model is far more complex than this example, but the basic intuition remains the same. Text embedding models encode the meaning of chunks of text into vectors, which can then be compared and grouped.

Along with this general intuition, it’s worth understanding three key aspects of text embedding models: their tokenizer, context window, dimensionality, and similarity function.

Like large language models, text embedding models use a tokenizer to split up the input text into chunks called “tokens” to be encoded. This happens behind the scenes in the encoding function.

Every [embedding model](https://www.baseten.co/resources/guide/high-performance-embedding-model-inference/) we’ll talk about uses “subword tokenization,” which is also standard for LLMs. This form of tokenization strikes a balance between limiting the number of possible tokens and making each token meaningful.

Subword tokenization gives short, common words their own token, while splitting up larger and more complex words by their roots, prefixes, suffixes, and other components.

Like LLMs, text embedding models have a context window: the number of tokens of input they can process at once. If you give a text embedding model a string that’s too long, it will only encode the meaning of the first N tokens of the string, where N is the number of tokens in its context window.

A larger context window allows for embedding more substantial pieces of text, which expands the use cases for the text embedding model. A context window of 256 tokens (\~200 words) lets you create embeddings of a book a page at a time, while a 8,192-token (\~6,000-word) context window will let you process whole chapters at a time.

One trick to using text embedding effectively is finding the right chunk size when embedding a corpus of text. For your use case, do you get the most value from retrieving sentences, paragraphs, or pages? If you need to embed longer chunks of text for the project to work, you’ll be limited to picking text embedding models with larger context windows.

One cool property of text embedding models is that no matter how short or long the input string is, the output will be exactly the same length.

That’s because a text embedding model has a fixed dimensionality, or length of output sequence. Remember, the output of a text embedding model is a vector, or list of floating-point numbers. Having every output the same length is essential for using embeddings later on.

| Pros of high-dimensionality models | Cons of high-dimensionality models | 
|---|---|
| They can provide more accurate results. | They require a larger dataset to make the most of extra dimensions. | 
| They can encode more semantic meaning, especially from longer chunks of text. | They make search and indexing much more costly. | 
| They are likely to encode the meaning of rare words, which can be essential to the text. | Their longer outputs mean an increased cost of storage. | 

Every use case for text embedding models involves comparing vectors. Every vector produced by the model will be the same length, and linear algebra gives us three popular comparison methods:

- **Euclidean distance**, which measures the linear distance between the endpoints of two vectors.
- **Cosine similarity**, which measures the angle between two vectors. This is the only similarity function that does not consider magnitude.
- **Dot product similarity**, which is calculated based on each component of two vectors.

While [each method has its advantages and disadvantages](https://www.pinecone.io/learn/vector-similarity/), what’s most important when building with text embedding models is always using the same similarity function to create consistency between comparisons.

New and updated open source text embedding models are released every week. You’ll find [thousands on Hugging Face](https://huggingface.co/models?pipeline_tag=sentence-similarity&sort=trending). Which model to pick depends on your use case and compute resources.

When building with text embedding models, it’s essential to pick a model that meets all of your needs. If you decide to switch models, you’ll need to regenerate embeddings for your entire database with the new model; you can’t meaningfully compare embeddings generated with different models.

Check out our [guide to open-source embedding models](https://www.baseten.co/blog/the-best-open-source-embedding-models/) for recommendations!

Many modern text embedding models are now LLM-based. This means LLM-oriented performance optimizations like TensorRT-LLM can accelerate embedding model inference.

We built [BEI, the fastest runtime for embedding models](https://www.baseten.co/blog/introducing-baseten-embeddings-inference-bei/) in the industry. With BEI, you get lower latency, higher request volume, and up to 2x the token throughput of previous solutions.

Here’s a demonstration of using BEI for inference on [Mixedbread Embed Large V1](https://www.baseten.co/library/mixedbread-embed-large-v1/), a high-quality embedding model that runs fast on L4 GPUs.

We start by installing the truss package from PyPI and initialing an empty Truss:

bash

```
pip install --upgrade truss
truss init embedding-model
```
Enter a model name like `Mixedbread Large V1` when prompted.

In the Truss’ `config.yaml` file, we can configure the runtime.

yaml

```
model_metadata:
  example_model_input:
    encoding_format: float
    input: text string
    model: model
model_name: BEI-mixedbread-ai-mxbai-embed-large-v1-embedding-truss-example
python_version: py39
resources:
  accelerator: L4
  cpu: '1'
  memory: 10Gi
  use_gpu: true
trt_llm:
  build:
    base_model: encoder
    checkpoint_repository:
      repo: mixedbread-ai/mxbai-embed-large-v1
      revision: main
      source: HF
    max_num_tokens: 16384
  runtime:
    webserver_default_route: /v1/embeddings
```
With the model packaged as a Truss, we can deploy it to Baseten. In your terminal, run:

`truss push`
Enter your [Baseten API key](https://docs.baseten.co/observability/api-keys) if prompted, and the model will be deployed to your account.

Once the model is deployed, we can run inference. Text embedding models served with BEI are compatible with the OpenAI SDK:

python

```
from openai import OpenAI
import os
client = OpenAI(
    api_key=os.environ['BASETEN_API_KEY'],
    base_url="https://model-xxxxxx.api.baseten.co/environments/production/sync/v1"
)
embedding = client.embeddings.create(
    input="Baseten Embeddings are fast",
    model="model"
)
```
If this primer got you excited about text embedding models, there are a ton of resources to explore:

- Our writeup on [BEI for embedding inference](https://www.baseten.co/blog/how-we-built-bei-high-throughput-embedding-inference/).
- Resources from vector store provider Pinecone like intros to [embeddings](https://www.pinecone.io/learn/vector-embeddings/) and [vector similarity](https://www.pinecone.io/learn/vector-similarity/).

For inspiration on projects, check out [embeds.ai](https://www.embeds.ai/), a text embedding battleground where you can compare the performance of popular open and closed source text embedding models.
