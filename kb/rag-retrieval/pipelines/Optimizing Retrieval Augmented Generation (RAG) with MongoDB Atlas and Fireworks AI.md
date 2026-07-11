---
title: Optimizing Retrieval Augmented Generation (RAG) with MongoDB Atlas and Fireworks
  AI
topic: rag-retrieval
subtopic: pipelines
secondary_topics:
- rag-retrieval/search
summary: Shows how to optimize a RAG pipeline with MongoDB Atlas and Fireworks models.
source: fireworks
url: https://fireworks.ai/blog/optimize-rag-with-mongodb-atlas-and-fireworks
author: null
published: '2024-03-21'
fetched: '2026-07-11T04:14:58Z'
classifier: codex
taxonomy_rev: 1
words: 1334
content_sha256: a95ac15ad232f807ef3222a597d4efeb11f7ce21569f0f441a4b0e14bf98e1cd
triage: keep
skip_reason: null
---

# Optimizing Retrieval Augmented Generation (RAG) with MongoDB Atlas and Fireworks AI

- What is RAG?
- Why RAG?
- RAG Architecture
- Optimizing RAG architecture
- Prerequisites
- Configuring your environment
- Gathering Credentials
- MongoDB Atlas
- Fireworks
- Initializing Fireworks and MongoDB Clients
- Using Fireworks with OSS Embedding Models
- Generating embeddings
- Creating a Index on MongoDB Collection
- Generating personalized recommendations with Fireworks
- Querying the Recommender System
- Generating Recommendations
- What’s next?

RAG is all the rage now! Haven’t heard about it? In this blog, we precisely help you kickstart your Generative AI Application development Journey and how to build a Retrieval Augmented Generation (RAG) App using [MongoDB Atlas](https://www.mongodb.com/atlas/database) and Fireworks AI. Further we’ll discuss how to optimize the architecture to achieve better cost and performance.

In a post-ChatGPT world, hearing about a new AI advancement or a Large Language Model (LLM) as a developer is as common as a new Javascript framework. Playing around with LLMs is fun, but creating AI-enabled experiences is the real deal in skill building for any developer.

Building apps or experiences on pre-trained LLMs has limitations. GPT, Claude, Llama and Mixtral have their knowledge/learning cutoff at a specific date. Methods to add custom knowledge, like fine-tuning, also have restrictions, like cost and knowledge limits that are restricted to training data.

MongoDB and Fireworks have partnered together to help enterprises build the next generation of scalable, secure cost-effective RAG applications grounded in their operational data.

Retrieval Augmented Generation (RAG) combines best of both worlds by leveraging a retrieval component to fetch relevant information from a database (or a vector store) and a generative component (LLM) to synthesize and generate a coherent response to the user query.

Through a RAG Architecture, LLMs get a second brain and the ability to fetch relevant and up-to-date info and turn the LLM into a real-time response generation engine that is grounded in your own data.

Some more reasons that make a RAG App special are:

**Data Efficiency: **RAG is data-efficient because it dynamically pulls in relevant data or information that may not have been seen during training. This saves time, effort and money compared to more data-hungry solutions like fine-tuning, which also often demand specialist, hard to find skills.

**Flexibility: **RAG enables dynamic updating of underlying knowledge bases or documents, making it easier to maintain the model without regular retraining. It is beneficial when the domain information is changing frequently, like with stock prices, weather etc.

A RAG Architecture consists of a Large Language Model to synthesize and submit the query to a data store (also can be called a vector store). The vector store then returns the relevant vector chunks as response to the LLM’s initial request. The LLM absorbs the response into its context and generates a response relevant to the user’s query.

As mentioned in the beginning of the blog, we’ll create a RAG-based app which recommends movies based on the user’s query. We are going to build a model to index and retrieve movie recommendations. The example will be built on top of MongoDB and Fireworks AI and involves:

- •[MongoDB Atlas Database](https://www.mongodb.com/atlas)that indexes movies using embeddings. (*Vector Store*)
- •A system for document embedding generation. We'll use the Fireworks embedding API to create embeddings from text data. (*Vectorisation*)
- •[MongoDB Atlas Vector Search](https://www.mongodb.com/products/platform/atlas-vector-search)that responds to user queries by converting the query to an embedding, fetching the corresponding movies. (*Retrieval Engine*)
- •The Mixtral model using the [Fireworks](https://fireworks.ai/login)inference API to generate the recommendations. You can also use Llama, Gemma, and other great OSS models if you like. (*LLM)*
- •Loading [MongoDB Atlas Sample Mflix Dataset](https://www.mongodb.com/docs/atlas/sample-data/sample-mflix/)to generate embeddings (*Dataset*)

💡Note: You can further[learn more](https://fireworks.ai#heading=h.x21yudnzpz0i)about optimizing RAG architecture. We have some helpful tips to reduce costs, improve throughput, add batching, and introduce function calling. These options help customize and scale your RAG architecture to suit your specific needs.

While this tutorial focuses on building a basic RAG Pipeline, we have guides to build optimized RAG architectures that can be further customized and scaled to suit various needs. For example:

- •Reduce the cost: Fireworks provides a range of embedding models with advanced capabilities. You can reduce the size of the embeddings, without a significant drop in retrieval performance, leading to reduced downstream costs associated with storing and retrieving embeddings. Improve the throughput: We are only documenting 400 movies in this example, which is not a lot. This is because we wanted to keep this tutorial simple and not batching the embedding lookups, and just have a for loop that goes through all the documents and embed them manually. This method does not scale. First, we will cover basic batching in the [following guide](https://github.com/fw-ai/cookbook/blob/main/examples/rag/mongo_resize_embeddings.ipynb).
- •Tap into the rich AI ecosystem: MongoDB and Fireworks work great with the various tools and frameworks you may be already using. Food for thought! There are a lot of great frameworks that offer batching out of the box, and please check out our guides here for [LlamaIndex](https://github.com/run-llama/llama_index/blob/cf0da01e0cc756383e07eb499cb9825cfa17984d/docs/examples/vector_stores/MongoDBAtlasVectorSearchRAGFireworks.ipynb)and[LangChain](https://python.langchain.com/docs/templates/rag-codellama-fireworks).

- •MongoDB Atlas Account
- •Fireworks AI Account

Note: You can follow the tutorial using the[Notebook](https://github.com/fw-ai/cookbook/blob/main/examples/rag/mongo_basic.ipynb)

Before we dive into the code, make sure to set up your environment. This involves installing necessary packages like `pymongo`, `fireworks-ai` and `openai`.

12

Note: We use the OpenAI Python SDK because it’s compatible with the Fireworks SDK

To interact with Fireworks AI and MongoDB Atlas Cluster, we need to initialize their respective clients. Replace "FIREWORKS_API_KEY" and "MONGODB_URI" with your actual credentials.

You can create and pick up the MongoDB URI from the MongoDB Atlas Cluster following the steps below.


After creating your account at Fireworks.ai, you can find the Fireworks API_Key under `Account Settings` -> `API Keys`

12345678910111213

Fireworks serves many state-of-the-art embedding models. Here are the full list of models Fireworks support.

- •mixedbread-ai/mxbai-embed-large-v1 (current leader for OSS model on [MTEB leaderboard](http://mteb/leaderboard), from Mixbread.ai)
- •BAAI/bge-base-en-v1.5 (great embedding model from BAAI)
- •nomic-ai/nomic-embed-text-v1.5 (great for Matryosha variable embedding dimension support)
- •WhereIsAI/UAE-Large-V1
- •thenlper/gte-large
- •thenlper/gte-base

In this blog, we are using the Nomic AI Model as one example to generate embeddings from the document corpus, specifically the `[nomic-ai/nomic-embed-text-v1.5](https://huggingface.co/nomic-ai/nomic-embed-text-v1.5)` variant. The function `generate_embeddings` below takes a list of texts and returns embeddings.

1234567891011121314151617

We will be adding more OSS embedding models as the space evolves, please check the fireworks.ai website for the most up to date list of embedding models.

Now, let's process our movie data through the `generate_embeddings` function created above.

We'll extract key information from our MongoDB collection and generate embeddings for each movie. Ensure NUM_DOC_LIMIT here is set to limit the number of documents processed.

12345678910111213141516171819202122232425

For our system to efficiently search through movie embeddings, we need to set up a search index in MongoDB. Define the index structure as shown:

1234567891011121314

Let's test our recommender system. We create a query for superhero movies and exclude Spider-Man movies, as per user preference.

123456789101112131415161718192021

Finally, we use Fireworks' chat API to generate a personalized movie recommendation based on the user's query and preferences.

123456789101112131415161718192021222324252627

We successfully built a movie recommendation system RAG using Fireworks, MongoDB, and the nomic-ai embedding model.

While this tutorial focuses on building a basic RAG Pipeline, we have guides to build optimized RAG architectures that can be further customized and scaled to suit various needs. For example:

- •Tunable cost for storage: We used the default 768 embedding dimension in the example. There are cases where the cost for storing the embedding is high, and you might want to reduce that, and we will walk you through another example with MongoDB + leveraging [Matryoshka embedding](https://arxiv.org/abs/2402.14776)to reduce embedding size in[this guide](http://examples/rag/mongo_reduced_embeddings.ipynb).
- •Improve the functionality with [Function calling](https://docs.llamaindex.ai/en/stable/examples/llm/fireworks_cookbook.html): You may want to dynamically decide to do RAG depending on the user query, and construct different filters that would fulfill the user query on the fly. In that case, Fireworks offers one of the[fastest function calling models](https://fireworks.ai/blog/firefunction-v1-gpt-4-level-function-calling)for you to orchestrate your application logic on top of your RAG architecture. You can check out how to combine RAG with function calling[in this guide](https://github.com/fw-ai/cookbook/blob/main/examples/rag/mongodb_agent.ipynb), or from the MongoDB interactive RAG example[in this blog](https://www.mongodb.com/developer/products/atlas/interactive-rag-mongodb-atlas-function-calling-api/).
