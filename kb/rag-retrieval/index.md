# rag-retrieval

20 articles.

- **2026-07-07** — [Faster phrase search with shingled bloom filters in Brainstore](<search/Faster phrase search with shingled bloom filters in Brainstore.md>) · `search` · braintrust
  Explains faster phrase search over Brainstore data using shingled bloom filters, aimed at efficient trace and log search for AI observability.
- **2026-06-30** — [Benchmarking GLM-5.2 vs Opus 4.8 for real-world long-context retrieval](<search/Benchmarking GLM-5.2 vs Opus 4.8 for real-world long-context retrieval.md>) · `search` · braintrust
  Benchmarks GLM-5.2 against Opus 4.8 on real-world long-context retrieval, focusing on retrieval quality under large-context conditions.
- **2026-06-25** — [How we built SmithDB’s inverted index for full-text search](<search/How we built SmithDB’s inverted index for full-text search.md>) · `search` · langchain
  Deep dive on constructing and querying SmithDB's inverted index for full-text search over observability data.
- **2026-06-10** — [Full Text Search in SmithDB: Designing an Inverted Index for Object Storage](<search/Full Text Search in SmithDB Designing an Inverted Index for Object Storage.md>) · `search` · langchain
  Architecture writeup on designing an inverted index for object storage in SmithDB, motivated by full-text search over agent traces.
- **2026-05-12** — [Expert Answers: Turn everyday support conversations into compounding knowledge](<pipelines/Expert Answers Turn everyday support conversations into compounding knowledge.md>) · `pipelines` · sierra
  Describes turning everyday support conversations into compounding knowledge, using agent interactions to improve knowledge bases and answers.
- **2026-05-12** — [Golden articles: Evaluating and improving search](<search/Golden articles Evaluating and improving search.md>) · `search` · sierra
  Covers golden-article evaluation for search quality and how retrieval systems can be measured and improved for support agents.
- **2026-05-12** — [Meet Linnaeus and Darwin: Search models that drive higher resolution rates](<search/Meet Linnaeus and Darwin Search models that drive higher resolution rates.md>) · `search` · sierra
  Introduces Sierra search models for improving support-agent resolution rates through better knowledge retrieval and answer grounding.
- **2026-01-01** — [How Dropbox built an evaluation pipeline for AI search](<search/How Dropbox built an evaluation pipeline for AI search.md>) · `search` · braintrust
  Case study of Dropbox's evaluation pipeline for AI search, focused on measuring retrieval and answer quality for production search experiences.
- **2025-10-28** — [RAG Observability and Evals](<pipelines/RAG Observability and Evals.md>) · `pipelines` · langfuse
  Explains observability and evaluation for RAG systems, including tracing retrieval/generation steps and measuring answer and context quality.
- **2024-11-18** — [Building a RAG app with MongoDB Atlas](<pipelines/Building a RAG app with MongoDB Atlas.md>) · `pipelines` · braintrust
  Walkthrough of building a RAG app with MongoDB Atlas, covering retrieval setup, model calls, and evaluation of the generated answers.
- **2024-09-24** — [Hybrid search over California embeddings with Modal, MongoDB, and Clay](<search/Hybrid search over California embeddings with Modal, MongoDB, and Clay.md>) · `search` · modal
  Example of hybrid search over embeddings, combining vector retrieval with MongoDB and a geospatial dataset.
- **2024-09-19** — [Contextual Retrieval in AI Systems](<pipelines/Contextual Retrieval in AI Systems.md>) · `pipelines` · anthropic-engineering
  Introduces contextual retrieval: prepending chunk-situating context before embedding and BM25 indexing, cutting retrieval failure rates by 49% (67% with reranking).
- **2024-07-02** — [Improving Memory Retrieval: How New Computer achieved 50% higher recall with LangSmith](<search/Improving Memory Retrieval How New Computer achieved 50% higher recall with LangSmith.md>) · `search` · langchain
  New Computer case study on improving memory retrieval recall with LangSmith-backed evaluation and debugging.
- **2024-03-15** — [Benchmarking Query Analysis in High Cardinality Situations](<search/Benchmarking Query Analysis in High Cardinality Situations.md>) · `search` · langchain
  Benchmarks query analysis in high-cardinality situations, relevant to retrieval, search, and observability filtering workloads.
- **2024-03-06** — [Evaluate RAG with LLM Evals and Benchmarks](<pipelines/Evaluate RAG with LLM Evals and Benchmarks.md>) · `pipelines` · arize
  Workshop recap on evaluating RAG systems with LLM evals and benchmarks.
- **2024-02-16** — [Evaluating the Generation Stage in RAG](<pipelines/Evaluating the Generation Stage in RAG.md>) · `pipelines` · arize
  Focuses on evaluating the generation stage in RAG pipelines, complementing retrieval-focused evaluation.
- **2024-01-23** — [Embedding English Wikipedia in under 15 minutes](<embeddings/Embedding English Wikipedia in under 15 minutes.md>) · `embeddings` · modal
  Walkthrough of embedding English Wikipedia quickly, covering large-scale embedding jobs, batching, and storage workflow.
- **2024-01-16** — [Build and deploy a RAG app with Pinecone Serverless](<pipelines/Build and deploy a RAG app with Pinecone Serverless.md>) · `pipelines` · langchain
  Walkthrough for building and deploying a RAG application with Pinecone Serverless and LangChain components.
- **2024-01-01** — [Evaluate RAG with LLM Evals and Benchmarking](<pipelines/Evaluate RAG with LLM Evals and Benchmarking.md>) · `pipelines` · arize
  Workshop recap on evaluating RAG systems with LLM evals and benchmarking.
- **2022-12-31** — [Measuring Embedding Drift](<embeddings/Measuring Embedding Drift.md>) · `embeddings` · arize
  Explains embedding drift and how teams can measure changes in embedding distributions over time.

## Also relevant (filed elsewhere)

- **2026-07-10** — [OpenWiki Brains: Proactive Memory for AI Agents](<../agents/memory-context/OpenWiki Brains Proactive Memory for AI Agents.md>) · `memory-context` · langchain
  Introduces OpenWiki Brains as proactive wiki memory for agents, focused on persistent context and retrieval over project knowledge.
- **2026-07-02** — [From World Cup matchups to research maps: evaluating Parallel's web research agents](<../agents/tool-use/From World Cup matchups to research maps evaluating Parallel's web research agents.md>) · `tool-use` · braintrust
  Evaluates Parallel web research agents using World Cup matchups and research-map tasks, connecting tool use, knowledge graphs, and answer quality.
- **2026-07-01** — [How to Use RLMs in Deep Agents](<../agents/memory-context/How to Use RLMs in Deep Agents.md>) · `memory-context` · langchain
  Explains how to use retrieval language models in Deep Agents to improve context selection and long-running agent performance.
- **2026-07-01** — [OpenWiki: Open Source Repo Documentation for Coding Agents](<../agents/tool-use/OpenWiki Open Source Repo Documentation for Coding Agents.md>) · `tool-use` · langchain
  Introduces OpenWiki as an agent for repository documentation, combining code understanding, retrieval, and generated docs.
- **2026-07-01** — [Making AI search smarter](<../industry/business/Making AI search smarter.md>) · `business` · cloudflare-ai
  Two initiatives to rebuild search economics: a research program sharing content-freshness signals with answer engines (over 50% of good-bot crawl traffic re-fetches unchanged pages) and evolving Pay Per Crawl into Pay Per Use, piloting pay-per-query compensation with Ceramic.ai and You.com.
- **2026-06-30** — [Wiki Memory](<../agents/memory-context/Wiki Memory.md>) · `memory-context` · langchain
  Explains wiki memory as a persistent knowledge layer for agents, supporting retrieval, documentation, and long-term project context.
- **2026-06-30** — [GLM-5.2 vs. Opus 4.8 technical report](<../models/benchmarks/GLM-5.2 vs. Opus 4.8 technical report.md>) · `benchmarks` · braintrust
  Technical report comparing GLM-5.2 and Opus 4.8, including benchmark methodology, long-context retrieval behavior, and model-performance tradeoffs.
- **2026-06-24** — [How to Build Memory into AI Agents](<../agents/memory-context/How to Build Memory into AI Agents.md>) · `memory-context` · langchain
  Explains how to build memory into AI agents through state, retrieval, persistence, and context injection patterns.
- **2026-05-13** — [Tau-Knowledge: benchmarking agents on realistic knowledge](<../evals-observability/evaluation/Tau-Knowledge benchmarking agents on realistic knowledge.md>) · `evaluation` · sierra
  Introduces tau-knowledge for benchmarking agents on realistic knowledge tasks that require grounded retrieval and use of external information.
- **2025-09-09** — [AI that knows your data](<../agents/tool-use/AI that knows your data.md>) · `tool-use` · braintrust
  Discusses MCP-style access to data and tools so AI systems can retrieve context and act against application-specific resources.
- **2024-11-18** — [Building a RAG app with MongoDB Atlas](<pipelines/Building a RAG app with MongoDB Atlas.md>) · `pipelines` · braintrust
  Walkthrough of building a RAG app with MongoDB Atlas, covering retrieval setup, model calls, and evaluation of the generated answers.
- **2024-09-24** — [Hybrid search over California embeddings with Modal, MongoDB, and Clay](<search/Hybrid search over California embeddings with Modal, MongoDB, and Clay.md>) · `search` · modal
  Example of hybrid search over embeddings, combining vector retrieval with MongoDB and a geospatial dataset.
- **2024-07-25** — [Building A Generative AI Platform](<../product-engineering/architecture/Building A Generative AI Platform.md>) · `architecture` · chip-huyen
  Reference architecture for generative AI platforms covering context construction and RAG, guardrails, gateways and routers, caching, observability, orchestration, and tool/action layers.
- **2024-04-26** — [Beating proprietary models with a quick fine-tune](<../models/fine-tuning/Beating proprietary models with a quick fine-tune.md>) · `fine-tuning` · modal
  Explains fine-tuning embedding models to beat proprietary baselines for a retrieval task with a compact training loop.
- **2024-01-16** — [Build and deploy a RAG app with Pinecone Serverless](<pipelines/Build and deploy a RAG app with Pinecone Serverless.md>) · `pipelines` · langchain
  Walkthrough for building and deploying a RAG application with Pinecone Serverless and LangChain components.
- **2023-04-11** — [Building LLM applications for production](<../product-engineering/architecture/Building LLM applications for production.md>) · `architecture` · chip-huyen
  Practical guide to production LLM applications covering task decomposition, retrieval, prompt construction, evaluation, monitoring, and latency/cost tradeoffs.
