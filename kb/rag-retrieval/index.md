# rag-retrieval

45 articles.

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
- **2026-04-04** — [How Arize Skills Improved RAG Recall from 39% to 75% in 8 Hours](<pipelines/How Arize Skills Improved RAG Recall from 39% to 75% in 8 Hours.md>) · `pipelines` · arize
  Uses an eval-guided RAG improvement loop to show how retrieval recall can be diagnosed and improved quickly.
- **2026-02-23** — [Mastering Production RAG with Google ADK and Arize AX for Enterprise Knowledge Systems](<pipelines/Mastering Production RAG with Google ADK and Arize AX for Enterprise Knowledge Systems.md>) · `pipelines` · arize
  Explains production RAG architecture with Google ADK and Arize AX, including agentic retrieval and evaluation concerns.
- **2026-01-01** — [How Dropbox built an evaluation pipeline for AI search](<search/How Dropbox built an evaluation pipeline for AI search.md>) · `search` · braintrust
  Case study of Dropbox's evaluation pipeline for AI search, focused on measuring retrieval and answer quality for production search experiences.
- **2025-10-28** — [RAG Observability and Evals](<pipelines/RAG Observability and Evals.md>) · `pipelines` · langfuse
  Explains observability and evaluation for RAG systems, including tracing retrieval/generation steps and measuring answer and context quality.
- **2025-10-07** — [AI-Ready Knowledge for Contact Centers: Closing the Gap Between the Knowledge Base and AI](<pipelines/AI-Ready Knowledge for Contact Centers Closing the Gap Between the Knowledge Base and AI.md>) · `pipelines` · cresta
  Explains how operational knowledge bases need to be structured for AI agents, with emphasis on grounding and retrieval readiness.
- **2025-09-12** — [Understanding embeddings and reranking at scale](<search/Understanding embeddings and reranking at scale.md>) · `search` · fireworks
  Explains embeddings, reranking, and retrieval architecture patterns for production RAG systems.
- **2025-08-19** — ["RAG is Dead, Context Engineering is King" — with Jeff Huber of Chroma](<pipelines/RAG is Dead, Context Engineering is King — with Jeff Huber of Chroma.md>) · `pipelines` · latent-space
  Chroma interview arguing that context engineering changes how teams should think about RAG and retrieval systems.
- **2025-08-06** — [Grounding Reality – How Cresta Tackles LLM Hallucinations in Enterprise AI](<pipelines/Grounding Reality – How Cresta Tackles LLM Hallucinations in Enterprise AI.md>) · `pipelines` · cresta
  Explains grounding strategies for reducing hallucinations in enterprise AI systems, with emphasis on knowledge and evaluation loops.
- **2025-06-12** — [Your client code matters: 12x higher embedding throughput with Python and Rust](<embeddings/Your client code matters 12x higher embedding throughput with Python and Rust.md>) · `embeddings` · baseten
  Shows how client implementation choices in Python and Rust affect embedding throughput.
- **2025-04-09** — [Building Enterprise-Scale RAG Systems with Fireworks AI and MongoDB Atlas](<pipelines/Building Enterprise-Scale RAG Systems with Fireworks AI and MongoDB Atlas.md>) · `pipelines` · fireworks
  Builds an enterprise-scale RAG system with MongoDB Atlas and Fireworks, covering retrieval and serving pieces.
- **2025-03-27** — [How we built BEI: high-throughput embedding, reranker, and classifier inference](<embeddings/How we built BEI high-throughput embedding, reranker, and classifier inference.md>) · `embeddings` · baseten
  Deep dive into BEI, a high-throughput embedding, reranker, and classifier inference system.
- **2025-02-05** — [Understanding Agentic RAG](<pipelines/Understanding Agentic RAG.md>) · `pipelines` · arize
  Explains agentic RAG and how agents change retrieval planning, tool use, and synthesis workflows.
- **2024-11-18** — [Building a RAG app with MongoDB Atlas](<pipelines/Building a RAG app with MongoDB Atlas.md>) · `pipelines` · braintrust
  Walkthrough of building a RAG app with MongoDB Atlas, covering retrieval setup, model calls, and evaluation of the generated answers.
- **2024-10-08** — [Multimodal Document RAG with Llama 3.2 Vision and ColQwen2](<pipelines/Multimodal Document RAG with Llama 3.2 Vision and ColQwen2.md>) · `pipelines` · together
  Builds a multimodal document RAG pipeline with Llama 3.2 Vision and ColQwen2.
- **2024-10-03** — [Building AI Assistants with Vectara-agentic and Arize](<pipelines/Building AI Assistants with Vectara-agentic and Arize.md>) · `pipelines` · arize
  Shows how to build AI assistants with Vectara-agentic and Arize, tying retrieval, agent tools, and observability together.
- **2024-09-24** — [Hybrid search over California embeddings with Modal, MongoDB, and Clay](<search/Hybrid search over California embeddings with Modal, MongoDB, and Clay.md>) · `search` · modal
  Example of hybrid search over embeddings, combining vector retrieval with MongoDB and a geospatial dataset.
- **2024-09-19** — [Contextual Retrieval in AI Systems](<pipelines/Contextual Retrieval in AI Systems.md>) · `pipelines` · anthropic-engineering
  Introduces contextual retrieval: prepending chunk-situating context before embedding and BM25 indexing, cutting retrieval failure rates by 49% (67% with reranking).
- **2024-09-17** — [Building high-performance compound AI applications with MongoDB Atlas and Baseten](<pipelines/Building high-performance compound AI applications with MongoDB Atlas and Baseten.md>) · `pipelines` · baseten
  Shows how to build high-performance compound AI applications with retrieval, orchestration, and model serving.
- **2024-08-14** — [Building a RAG with Astro, FastAPI, SurrealDB and Llama 3.1](<pipelines/Building a RAG with Astro, FastAPI, SurrealDB and Llama 3.1.md>) · `pipelines` · fireworks
  End-to-end RAG application example using Astro, FastAPI, SurrealDB, and Llama 3.1.
- **2024-07-02** — [Improving Memory Retrieval: How New Computer achieved 50% higher recall with LangSmith](<search/Improving Memory Retrieval How New Computer achieved 50% higher recall with LangSmith.md>) · `search` · langchain
  New Computer case study on improving memory retrieval recall with LangSmith-backed evaluation and debugging.
- **2024-06-28** — [RAFT: Adapting Language Model to Domain Specific RAG](<pipelines/RAFT Adapting Language Model to Domain Specific RAG.md>) · `pipelines` · arize
  Summarizes RAFT as a method for adapting language models to domain-specific RAG workflows.
- **2024-06-24** — [Building a personalized code assistant with open-source LLMs using RAG Fine-tuning](<pipelines/Building a personalized code assistant with open-source LLMs using RAG Fine-tuning.md>) · `pipelines` · together
  Builds a personalized code assistant using RAG fine-tuning with open-source LLMs.
- **2024-03-21** — [Optimizing Retrieval Augmented Generation (RAG) with MongoDB Atlas and Fireworks AI](<pipelines/Optimizing Retrieval Augmented Generation (RAG) with MongoDB Atlas and Fireworks AI.md>) · `pipelines` · fireworks
  Shows how to optimize a RAG pipeline with MongoDB Atlas and Fireworks models.
- **2024-03-15** — [Benchmarking Query Analysis in High Cardinality Situations](<search/Benchmarking Query Analysis in High Cardinality Situations.md>) · `search` · langchain
  Benchmarks query analysis in high-cardinality situations, relevant to retrieval, search, and observability filtering workloads.
- **2024-03-06** — [Evaluate RAG with LLM Evals and Benchmarks](<pipelines/Evaluate RAG with LLM Evals and Benchmarks.md>) · `pipelines` · arize
  Workshop recap on evaluating RAG systems with LLM evals and benchmarks.
- **2024-02-16** — [Evaluating the Generation Stage in RAG](<pipelines/Evaluating the Generation Stage in RAG.md>) · `pipelines` · arize
  Focuses on evaluating the generation stage in RAG pipelines, complementing retrieval-focused evaluation.
- **2024-02-08** — [RAG vs Fine-Tuning](<pipelines/RAG vs Fine-Tuning.md>) · `pipelines` · arize
  Compares RAG and fine-tuning as adaptation strategies, including when retrieval is preferable to model updates.
- **2024-01-23** — [Embedding English Wikipedia in under 15 minutes](<embeddings/Embedding English Wikipedia in under 15 minutes.md>) · `embeddings` · modal
  Walkthrough of embedding English Wikipedia quickly, covering large-scale embedding jobs, batching, and storage workflow.
- **2024-01-16** — [Build and deploy a RAG app with Pinecone Serverless](<pipelines/Build and deploy a RAG app with Pinecone Serverless.md>) · `pipelines` · langchain
  Walkthrough for building and deploying a RAG application with Pinecone Serverless and LangChain components.
- **2024-01-11** — [Long context retrieval models with Monarch Mixer](<search/Long context retrieval models with Monarch Mixer.md>) · `search` · together
  Explains long-context retrieval models using Monarch Mixer.
- **2024-01-01** — [Evaluate RAG with LLM Evals and Benchmarking](<pipelines/Evaluate RAG with LLM Evals and Benchmarking.md>) · `pipelines` · arize
  Workshop recap on evaluating RAG systems with LLM evals and benchmarking.
- **2023-11-29** — [Notebooks = Chat++ and RAG = RecSys! — with Bryan Bischof of Hex Magic](<pipelines/Notebooks = Chat++ and RAG = RecSys! — with Bryan Bischof of Hex Magic.md>) · `pipelines` · latent-space
  Connects notebooks, chat interfaces, RAG, and recommender-system thinking for data-oriented AI products.
- **2023-11-08** — [Ingesting Data for Semantic Searches in a Production-Ready Way](<pipelines/Ingesting Data for Semantic Searches in a Production-Ready Way.md>) · `pipelines` · arize
  Explains production ingestion concerns for semantic search, including data preparation and retrieval pipeline reliability.
- **2023-11-02** — [Deployment and inference for open source text embedding models](<embeddings/Deployment and inference for open source text embedding models.md>) · `embeddings` · baseten
  Covers deployment and inference patterns for open-source text embedding models.
- **2023-10-17** — [RankVicuna: Zero-Shot Listwise Document Reranking with Open-Source Large Language Models](<search/RankVicuna Zero-Shot Listwise Document Reranking with Open-Source Large Language Models.md>) · `search` · arize
  Summarizes RankVicuna for zero-shot listwise reranking and its implications for LLM-powered search.
- **2023-06-27** — [HyDE: Precise Zero-Shot Dense Retrieval without Relevance Labels](<search/HyDE Precise Zero-Shot Dense Retrieval without Relevance Labels.md>) · `search` · arize
  Summarizes HyDE for zero-shot dense retrieval and how hypothetical document generation can improve semantic search.
- **2023-06-09** — [Retrieval-Augmented Generation - Paper Reading and Discussion](<pipelines/Retrieval-Augmented Generation - Paper Reading and Discussion.md>) · `pipelines` · arize
  Paper-reading summary of retrieval-augmented generation and the architecture behind combining retrieval with generation.
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
- **2026-04-29** — [Using context graphs: build a data moat like Google's using your enterprise data](<../agents/memory-context/Using context graphs build a data moat like Google's using your enterprise data.md>) · `memory-context` · arize
  Explains context graphs as an enterprise memory layer for agents and retrieval-heavy AI systems.
- **2025-09-12** — [Understanding embeddings and reranking at scale](<search/Understanding embeddings and reranking at scale.md>) · `search` · fireworks
  Explains embeddings, reranking, and retrieval architecture patterns for production RAG systems.
- **2025-09-09** — [AI that knows your data](<../agents/tool-use/AI that knows your data.md>) · `tool-use` · braintrust
  Discusses MCP-style access to data and tools so AI systems can retrieve context and act against application-specific resources.
- **2025-04-16** — [Open Deep Research](<../agents/tool-use/Open Deep Research.md>) · `tool-use` · together
  Describes an open deep research system combining retrieval, planning, and tool use.
- **2025-04-09** — [Building Enterprise-Scale RAG Systems with Fireworks AI and MongoDB Atlas](<pipelines/Building Enterprise-Scale RAG Systems with Fireworks AI and MongoDB Atlas.md>) · `pipelines` · fireworks
  Builds an enterprise-scale RAG system with MongoDB Atlas and Fireworks, covering retrieval and serving pieces.
- **2024-11-18** — [Building a RAG app with MongoDB Atlas](<pipelines/Building a RAG app with MongoDB Atlas.md>) · `pipelines` · braintrust
  Walkthrough of building a RAG app with MongoDB Atlas, covering retrieval setup, model calls, and evaluation of the generated answers.
- **2024-09-24** — [Hybrid search over California embeddings with Modal, MongoDB, and Clay](<search/Hybrid search over California embeddings with Modal, MongoDB, and Clay.md>) · `search` · modal
  Example of hybrid search over embeddings, combining vector retrieval with MongoDB and a geospatial dataset.
- **2024-07-25** — [Building A Generative AI Platform](<../product-engineering/architecture/Building A Generative AI Platform.md>) · `architecture` · chip-huyen
  Reference architecture for generative AI platforms covering context construction and RAG, guardrails, gateways and routers, caching, observability, orchestration, and tool/action layers.
- **2024-06-11** — [How AI is eating Finance — with Mike Conover of Brightwave](<../product-engineering/case-studies/How AI is eating Finance — with Mike Conover of Brightwave.md>) · `case-studies` · latent-space
  Interview on AI-native finance workflows, including retrieval, analysis, and product design for financial knowledge work.
- **2024-04-29** — [How fine tuned LLMs power knowledge assist, summarization, and chat suggestions](<../models/fine-tuning/How fine tuned LLMs power knowledge assist, summarization, and chat suggestions.md>) · `fine-tuning` · cresta
  Explains how fine-tuned LLMs support knowledge assist, summarization, and chat suggestions in production workflows.
- **2024-04-26** — [Beating proprietary models with a quick fine-tune](<../models/fine-tuning/Beating proprietary models with a quick fine-tune.md>) · `fine-tuning` · modal
  Explains fine-tuning embedding models to beat proprietary baselines for a retrieval task with a compact training loop.
- **2024-03-21** — [Optimizing Retrieval Augmented Generation (RAG) with MongoDB Atlas and Fireworks AI](<pipelines/Optimizing Retrieval Augmented Generation (RAG) with MongoDB Atlas and Fireworks AI.md>) · `pipelines` · fireworks
  Shows how to optimize a RAG pipeline with MongoDB Atlas and Fireworks models.
- **2024-02-20** — [Evaluating and Analyzing Your RAG Pipeline with Ragas](<../evals-observability/evaluation/Evaluating and Analyzing Your RAG Pipeline with Ragas.md>) · `evaluation` · arize
  Explains how to evaluate RAG pipelines with Ragas and Phoenix, including retrieval and generation quality dimensions.
- **2024-01-16** — [Build and deploy a RAG app with Pinecone Serverless](<pipelines/Build and deploy a RAG app with Pinecone Serverless.md>) · `pipelines` · langchain
  Walkthrough for building and deploying a RAG application with Pinecone Serverless and LangChain components.
- **2023-11-08** — [Ingesting Data for Semantic Searches in a Production-Ready Way](<pipelines/Ingesting Data for Semantic Searches in a Production-Ready Way.md>) · `pipelines` · arize
  Explains production ingestion concerns for semantic search, including data preparation and retrieval pipeline reliability.
- **2023-10-26** — [Powering your Copilot for Data – with Artem Keydunov of Cube.dev](<../product-engineering/architecture/Powering your Copilot for Data – with Artem Keydunov of Cube.dev.md>) · `architecture` · latent-space
  Covers building a copilot for data with Cube.dev, including semantic layers and analytics-oriented AI architecture.
- **2023-06-27** — [HyDE: Precise Zero-Shot Dense Retrieval without Relevance Labels](<search/HyDE Precise Zero-Shot Dense Retrieval without Relevance Labels.md>) · `search` · arize
  Summarizes HyDE for zero-shot dense retrieval and how hypothetical document generation can improve semantic search.
- **2023-04-11** — [Building LLM applications for production](<../product-engineering/architecture/Building LLM applications for production.md>) · `architecture` · chip-huyen
  Practical guide to production LLM applications covering task decomposition, retrieval, prompt construction, evaluation, monitoring, and latency/cost tradeoffs.
- **2022-12-01** — [Why You Need To Monitor Recommender Systems](<../evals-observability/monitoring/Why You Need To Monitor Recommender Systems.md>) · `monitoring` · arize
  Explains why recommender systems need monitoring and what signals matter for production ranking quality.
- **2022-11-09** — [How to Monitor Ranking Models](<../evals-observability/monitoring/How to Monitor Ranking Models.md>) · `monitoring` · arize
  Explains monitoring patterns for ranking models, including drift and performance signals relevant to search and recommendations.
- **2022-06-08** — [Monitor Unstructured Data with Arize](<../evals-observability/monitoring/Monitor Unstructured Data with Arize.md>) · `monitoring` · arize
  Covers monitoring techniques for unstructured data and embeddings in production AI systems.
