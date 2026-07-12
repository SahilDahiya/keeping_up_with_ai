---
title: 'Arize AI + MongoDB: Leveraging Agent Evaluation and Memory to Build Robust
  Agentic Systems'
topic: agents
subtopic: memory-context
secondary_topics:
- evals-observability/evaluation
summary: Explains how Arize and MongoDB combine agent evaluation and memory patterns
  for more robust agentic systems.
source: arize
url: https://arize.com/blog/arize-ai-mongodb-agentic-systems/
author: Amit Goren
published: '2024-09-30'
fetched: '2026-07-11T04:50:04Z'
classifier: codex
taxonomy_rev: 1
words: 1412
content_sha256: c33e858de081145e4cd66c6813d53d0db270440d17f76fa39bbb4a4c7493d058
---

# Arize AI + MongoDB: Leveraging Agent Evaluation and Memory to Build Robust Agentic Systems

In the evolving landscape of artificial intelligence, agentic systems—autonomous agents capable of making decisions and learning from feedback loops in their environment—are becoming increasingly sophisticated.

At the same time, as retrieval augmented generation (RAG) applications become more complex, a critical component of these systems is memory. AI agents depend on memory to perform effectively, adapt to new situations, and make informed decisions. However, a single request to these systems can generate hundreds of calls under the hood, making debugging issues and understanding how they come to their outputs challenging for the AI engineering teams building and maintaining applications.

As more businesses begin adopting and integrating LLM applications with robust agentic systems, it is imperative that teams are able to evaluate, troubleshoot, and improve the performance of their applications.

Arize AI and MongoDB have come together to help AI engineers develop and deploy their LLM applications with confidence.

As large language models (LLMs) continue to advance, efficient and scalable memory systems are essential. Vector databases are critical in this context, particularly for managing the memory of AI agents. MongoDB provides a full document data store and a robust query api that supports integrated full text search and vector search capabilities which lays a powerful foundation for implementing these systems, and when combined with Arize AI’s advanced evaluation and observability capabilities, it becomes possible to build, troubleshoot, and optimize robust agentic systems.

**Fast and Scalable Retrieval**

For AI engineers working with RAG-based systems, the combination of MongoDB and Arize AI offers a powerful toolkit for building and maintaining generative-powered systems. MongoDB’s vector search capabilities ensure rapid, scalable retrieval of relevant vectors that RAG applications rely on. This capability is essential for real-time memory recall, enabling agents to perform effectively even as data volumes grow.

Arize AI’s platform offers comprehensive observability tools that allow engineers to trace the flow of data through the AI system, from input to final output. This tracing capability is especially valuable in complex, multi-layered architectures like RAG, where understanding the impact of each component on the final result is critical for effective debugging and optimization.

**Contextual Memory Management and Interactive RAG Strategy**

By leveraging its document-based architecture and vector search capabilities, MongoDB’s flexible schema allows agents to manage contextual memory effectively. By storing complex documents that include vectors and related context, MongoDB helps agents maintain a nuanced understanding of interactions, ensuring coherence and context-awareness. MongoDB’s schema flexibility also supports the differentiation between short-term and long-term memory, enabling agents to manage their memory resources efficiently.

Arize offers a library of LLM evaluations that are pre-tested on tasks such as code generation, Q&A accuracy, embedding cluster summarization, and more. Leveraging the LLM as a judge approach, an evaluator LLM scores application output based on relevance, toxicity, etc. LLM-generated explanations detail why the output was scored a certain way, providing a scaled mechanism to understand how the LLM application came to its output and potential ways to improve performance of these complex systems.

![Eval chart](https://arize.com/wp-content/uploads/2024/09/image2-1024x489.png)

Employing an interactive RAG approach, allows the knowledge base to access and process real-time information from external sources such as online databases and APIs. This enables it to provide up-to-date and relevant responses, making it suitable for applications requiring access to constantly changing data. Powered by MongoDB Atlas, interactive RAG enables teams to dynamically adjust their RAG strategy in real-time, using the function calling API of large language models—optimizing for a truly interactive and personalized experience.

![Traces screenshot](https://arize.com/wp-content/uploads/2024/09/image4-1024x254.png)

Leveraging Arize’s retrieval evaluation with explanations, developers can quickly see that the LLM hallucinated, see the exact chunk of the retrieval used in the call, and receive an explanation of why the LLM was incorrect:

![Explanation of why the LLM was incorrect](https://arize.com/wp-content/uploads/2024/09/image1-1024x348.png)

**Visibility into the System with Tracing**

Arize’s LLM tracing capabilities provide visibility into each call in an LLM-powered system to facilitate application development and troubleshooting. This is especially critical for systems that implement an orchestration or agentic framework, as those abstractions can mask an immense number of distributed system calls that are nearly impossible to debug without programmatic tracing.

![Visibility into the system with tracing](https://arize.com/wp-content/uploads/2024/09/image3-1024x841.png)

**Evaluate Agent and Retriever Performance**

Evaluations help teams understand their LLM application’s performance. Evals can be used to measure an application across several dimensions such as correctness, hallucination, relevance, latency, tool calling and more. This enables teams to evaluate their application’s performance at every step.

Arize has built an evaluation framework with:

- **Pre-tested Evaluators Backed by Research:**Arize evaluators are thoroughly tested against the latest capabilities from LLM providers, such as needle in a haystack tests.
- **Multi-level Custom Evaluation:**Arize provides several types of evaluations complete with explanations out of the box, enabling users to customize their evaluation using their own criteria and prompt templates.
- **Designed for Speed:**Arize evals are designed to handle large volumes of data, with parallel calls, batch processing, and rate limiting.
- **Ease of Onboarding:**Arize’s framework integrates seamlessly with popular LLM frameworks like LangChain and LlamaIndex, providing straightforward setup and execution.
- **Extensive Compatibility:**Arize’s library is compatible with all common LLMs and offers unparalleled RAG debugging and troubleshooting.

Arize also offers teams the option to create and run automated actions on your LLM spans as their application scales—known as Tasks. During development, engineers can automatically run an evaluation on every trace that doesn’t have an evaluation yet. In production, they can sample a set of your traffic to run evaluations for monitoring that run every few minutes.

![llm evals screenshot](https://arize.com/wp-content/uploads/2024/09/image5-1-934x1024.png)

**Curated Datasets for Experimentation**

In AI development, it’s hard to understand how a change will affect performance. This breaks the dev flow, making iteration more guesswork than engineering. In Arize, datasets and experiments help solve this.

Developers can select examples of interest in Arize—such as cases where an agent failed to perform—to then run experiments and optimize for performance. Teams can track improvements to their prompts, LLM, or other parts of their application across experiments in order to continuously iterate on and improve their application. This systematic experimentation is vital for identifying the optimal configuration to balance agent performance and efficiency.

Developers can leverage Arize’s prompt + data playground to replay problems within their application, test different prompts across their data, as an effective way to improve the outputs of their applications. The interactive environment provides developers real-time feedback into the results, providing valuable insight during experimentation.

![prompt playground screenshot](https://arize.com/wp-content/uploads/2024/09/image6-1-1024x527.png)

**Develop and Deploy Robust Agentic Systems with Confidence**

Vector databases are essential for managing memory in LLM-based agentic systems, and MongoDB offers a robust solution for storing, retrieving, and managing this data. When combined with Arize AI’s advanced features like Tracing, Datasets, Experiments, and LLM Evaluations, developers have a comprehensive toolkit for building, evaluating, and optimizing their AI agents:

- **Data Ingestion and Storage:**MongoDB has a flexible schema allowing it to ingest and store diverse datasets, including structured data, time series dataset, graph dataset, vector embeddings, and unstructured text. This data forms the knowledge base from which the AI agent draws context and information.
- **Unified Query API:**MongoDB is a document data store with full fledged query api to query data with multiple patterns such as vector search, vector search with pre-filtering, vector search with post-filter, full text search, hybrid search. The post-filtering step in the query pipeline also allows the user to couple graph traversal of data along with vector search. When the AI agent receives a query or task, it first retrieves relevant information from MongoDB using one or more techniques mentioned above. The retrieved information is then passed to the LLM for further processing.
- **LLM Processing and Generation:**The LLM, powered by models like OpenAI’s latest embeddings, processes the retrieved data to generate a response or decision. This process is iterative, with the agent potentially making several retrievals and adjustments before finalizing its output.
- **Agent Evaluation and Fine-Tuning:**As the AI agent completes its task, Arize AI’s evaluation tools kick in, scoring the quality of the output and identifying any areas for improvement. This feedback loop is crucial for refining the agent’s behavior over time, ensuring that it remains effective and reliable as new data and scenarios are encountered.

By leveraging MongoDB’s scalability and Arize AI’s powerful evaluation and troubleshooting capabilities, developers can ensure that their agentic systems not only perform well in the short term but also adapt and improve over time. This combination of technologies ensures that AI agents are equipped to handle complex, real-world scenarios with reliability, safety, and efficiency.

See how MongoDB and Arize work together [in this Colab tutorial. ](https://colab.research.google.com/github/Arize-ai/phoenix/blob/main/tutorials/integrations/tracing_and_evals_with_mongodb_and_llama_index.ipynb)
