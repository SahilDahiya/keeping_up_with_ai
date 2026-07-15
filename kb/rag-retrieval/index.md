# rag-retrieval

56 articles.

- **2026-07-07** — [Faster phrase search with shingled bloom filters in Brainstore](<search/Faster phrase search with shingled bloom filters in Brainstore.md>) · `search` · braintrust
  Explains faster phrase search over Brainstore data using shingled bloom filters, aimed at efficient trace and log search for AI observability.
- **2026-06-30** — [Benchmarking GLM-5.2 vs Opus 4.8 for real-world long-context retrieval](<search/Benchmarking GLM-5.2 vs Opus 4.8 for real-world long-context retrieval.md>) · `search` · braintrust
  Benchmarks GLM-5.2 against Opus 4.8 on real-world long-context retrieval, focusing on retrieval quality under large-context conditions.
- **2026-06-25** — [How we built SmithDB’s inverted index for full-text search](<search/How we built SmithDB’s inverted index for full-text search.md>) · `search` · langchain
  Deep dive on constructing and querying SmithDB's inverted index for full-text search over observability data.
- **2026-06-10** — [Full Text Search in SmithDB: Designing an Inverted Index for Object Storage](<search/Full Text Search in SmithDB Designing an Inverted Index for Object Storage.md>) · `search` · langchain
  Architecture writeup on designing an inverted index for object storage in SmithDB, motivated by full-text search over agent traces.
- **2026-05-19** — [Introducing the Ettin Reranker Family](<search/Introducing the Ettin Reranker Family.md>) · `search` · huggingface
  Releases six CrossEncoder rerankers (17M-1B) built on Ettin ModernBERT encoders with the full training recipe: data selection, loss choice, hard-negative mining, and BEIR/NanoBEIR numbers showing SOTA at each size.
- **2026-05-12** — [Expert Answers: Turn everyday support conversations into compounding knowledge](<pipelines/Expert Answers Turn everyday support conversations into compounding knowledge.md>) · `pipelines` · sierra
  Describes turning everyday support conversations into compounding knowledge, using agent interactions to improve knowledge bases and answers.
- **2026-05-12** — [Golden articles: Evaluating and improving search](<search/Golden articles Evaluating and improving search.md>) · `search` · sierra
  Covers golden-article evaluation for search quality and how retrieval systems can be measured and improved for support agents.
- **2026-05-12** — [Meet Linnaeus and Darwin: Search models that drive higher resolution rates](<search/Meet Linnaeus and Darwin Search models that drive higher resolution rates.md>) · `search` · sierra
  Introduces Sierra search models for improving support-agent resolution rates through better knowledge retrieval and answer grounding.
- **2026-04-16** — [Training and Finetuning Multimodal Embedding & Reranker Models with Sentence Transformers](<embeddings/Training and Finetuning Multimodal Embedding & Reranker Models with Sentence Transformers.md>) · `embeddings` · huggingface
  Walks through finetuning Qwen3-VL-Embedding-2B for Visual Document Retrieval with Sentence Transformers' new multimodal support, showing a specialized 2B model beating much larger general-purpose embedders on NDCG. Covers multimodal dataset format, loss selection (cached MNRL), hard-negative mining and training a reranker on top.
- **2026-04-09** — [Multimodal Embedding & Reranker Models with Sentence Transformers](<embeddings/Multimodal Embedding & Reranker Models with Sentence Transformers.md>) · `embeddings` · huggingface
  Sentence Transformers v5+ adds multimodal embedding and reranker models (shared text/image embedding space, mixed-modality cross-encoder scoring) for visual document retrieval, cross-modal search and multimodal RAG; covers the API and model choices.
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
- **2025-10-01** — [Introducing RTEB: A New Standard for Retrieval Evaluation](<embeddings/Introducing RTEB A New Standard for Retrieval Evaluation.md>) · `embeddings` · huggingface
  RTEB is a retrieval benchmark that mixes open and permanently-private held-out datasets, so a model's gap between public and private scores exposes overfitting to MTEB-style public leaderboards. Covers the dataset selection across domains/languages, the private-eval protocol, and evidence that several leaderboard-topping embedding models generalize worse than their public scores suggest.
- **2025-09-12** — [Understanding embeddings and reranking at scale](<search/Understanding embeddings and reranking at scale.md>) · `search` · fireworks
  Explains embeddings, reranking, and retrieval architecture patterns for production RAG systems.
- **2025-09-04** — [Welcome EmbeddingGemma, Google's new efficient embedding model](<embeddings/Welcome EmbeddingGemma, Google's new efficient embedding model.md>) · `embeddings` · huggingface
  EmbeddingGemma is a 308M-param multilingual embedding model: a Gemma3 backbone converted to bidirectional attention plus mean pooling and two dense layers, trained on ~320B tokens with Matryoshka Representation Learning so its 768-dim output can be truncated to 512/256/128; runs under 200 MB RAM quantized, tops MTEB under 500M, and the post shows a domain fine-tune on MIRIAD that beats models twice its size.
- **2025-08-06** — [Grounding Reality – How Cresta Tackles LLM Hallucinations in Enterprise AI](<pipelines/Grounding Reality – How Cresta Tackles LLM Hallucinations in Enterprise AI.md>) · `pipelines` · cresta
  Explains grounding strategies for reducing hallucinations in enterprise AI systems, with emphasis on knowledge and evaluation loops.
- **2025-07-01** — [Training and Finetuning Sparse Embedding Models with Sentence Transformers](<embeddings/Training and Finetuning Sparse Embedding Models with Sentence Transformers.md>) · `embeddings` · huggingface
  End-to-end guide to training SPLADE-style sparse embedding models with Sentence Transformers: the model/loss/evaluator/trainer components, FLOPS regularization to control sparsity, distillation from a cross-encoder, and NanoBEIR results plus the retrieval-cost tradeoff versus dense vectors.
- **2025-06-12** — [Your client code matters: 12x higher embedding throughput with Python and Rust](<embeddings/Your client code matters 12x higher embedding throughput with Python and Rust.md>) · `embeddings` · baseten
  Shows how client implementation choices in Python and Rust affect embedding throughput.
- **2025-04-09** — [Building Enterprise-Scale RAG Systems with Fireworks AI and MongoDB Atlas](<pipelines/Building Enterprise-Scale RAG Systems with Fireworks AI and MongoDB Atlas.md>) · `pipelines` · fireworks
  Builds an enterprise-scale RAG system with MongoDB Atlas and Fireworks, covering retrieval and serving pieces.
- **2025-03-27** — [How we built BEI: high-throughput embedding, reranker, and classifier inference](<embeddings/How we built BEI high-throughput embedding, reranker, and classifier inference.md>) · `embeddings` · baseten
  Deep dive into BEI, a high-throughput embedding, reranker, and classifier inference system.
- **2025-03-26** — [Training and Finetuning Reranker Models with Sentence Transformers](<search/Training and Finetuning Reranker Models with Sentence Transformers.md>) · `search` · huggingface
  Full guide to training cross-encoder reranker models with Sentence Transformers v4: dataset formats, losses (BinaryCrossEntropy, CachedMultipleNegativesRanking, ListNet), hard-negative mining, and evaluation, with a fine-tune that beats much larger general rerankers on the target domain.
- **2025-02-05** — [Understanding Agentic RAG](<pipelines/Understanding Agentic RAG.md>) · `pipelines` · arize
  Explains agentic RAG and how agents change retrieval planning, tool use, and synthesis workflows.
- **2025-01-15** — [Train 400x faster Static Embedding Models with Sentence Transformers](<embeddings/Train 400x faster Static Embedding Models with Sentence Transformers.md>) · `embeddings` · huggingface
  Trains static (token-embedding-lookup, no transformer forward pass) retrieval and similarity models with Sentence Transformers that run 100x-400x faster on CPU than all-mpnet-base-v2 while keeping ~85% of quality; details the recipe: contrastive MNRL loss with large batch sizes, hard-negative mining, Matryoshka dimensionality reduction, and dataset selection.
- **2025-01-10** — [Visual Document Retrieval Goes Multilingual](<embeddings/Visual Document Retrieval Goes Multilingual.md>) · `embeddings` · huggingface
  vdr-2b-multi-v1 is a ColPali-style visual document retrieval embedding model trained on a new 500k multilingual query/page synthetic dataset across 5 languages, beating the English-only baseline on multilingual and cross-lingual document retrieval benchmarks.
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
- **2024-07-16** — [How we leveraged distilabel to create an Argilla 2.0 Chatbot](<pipelines/How we leveraged distilabel to create an Argilla 2.0 Chatbot.md>) · `pipelines` · huggingface
  End-to-end build of a docs chatbot: distilabel generates synthetic query/answer pairs from Argilla 2.0 documentation, which fine-tunes a bge-base Matryoshka embedding model used in a retrieval + Gradio chat pipeline.
- **2024-07-02** — [Improving Memory Retrieval: How New Computer achieved 50% higher recall with LangSmith](<search/Improving Memory Retrieval How New Computer achieved 50% higher recall with LangSmith.md>) · `search` · langchain
  New Computer case study on improving memory retrieval recall with LangSmith-backed evaluation and debugging.
- **2024-06-28** — [RAFT: Adapting Language Model to Domain Specific RAG](<pipelines/RAFT Adapting Language Model to Domain Specific RAG.md>) · `pipelines` · arize
  Summarizes RAFT as a method for adapting language models to domain-specific RAG workflows.
- **2024-06-24** — [Building a personalized code assistant with open-source LLMs using RAG Fine-tuning](<pipelines/Building a personalized code assistant with open-source LLMs using RAG Fine-tuning.md>) · `pipelines` · together
  Builds a personalized code assistant using RAG fine-tuning with open-source LLMs.
- **2024-05-28** — [Training and Finetuning Embedding Models with Sentence Transformers](<embeddings/Training and Finetuning Embedding Models with Sentence Transformers.md>) · `embeddings` · huggingface
  Complete guide to finetuning embedding models with Sentence Transformers v3: choosing a loss for your dataset shape (MultipleNegativesRankingLoss for (anchor, positive) pairs, CoSENT, etc.), the SentenceTransformerTrainer API, training args (batch size matters a lot for in-batch negatives), and evaluators for measuring retrieval gains.
- **2024-03-22** — [Binary and Scalar Embedding Quantization for Significantly Faster & Cheaper Retrieval](<embeddings/Binary and Scalar Embedding Quantization for Significantly Faster & Cheaper Retrieval.md>) · `embeddings` · huggingface
  Binary (1-bit) and int8 scalar quantization of embeddings cuts retrieval memory/cost ~32x and ~4x while retaining ~92-96% of performance; covers rescoring with float embeddings and combining binary search + int8 rescoring in FAISS/usearch.
- **2024-03-21** — [Optimizing Retrieval Augmented Generation (RAG) with MongoDB Atlas and Fireworks AI](<pipelines/Optimizing Retrieval Augmented Generation (RAG) with MongoDB Atlas and Fireworks AI.md>) · `pipelines` · fireworks
  Shows how to optimize a RAG pipeline with MongoDB Atlas and Fireworks models.
- **2024-03-15** — [CPU Optimized Embeddings with 🤗 Optimum Intel and fastRAG](<embeddings/CPU Optimized Embeddings with 🤗 Optimum Intel and fastRAG.md>) · `embeddings` · huggingface
  Speeds up bge-base embeddings on Xeon CPUs by quantizing to int8 with Optimum Intel / IPEX, reporting latency and MTEB retrieval-quality deltas, then wires the optimized encoder into a fastRAG retrieval pipeline.
- **2024-03-15** — [Benchmarking Query Analysis in High Cardinality Situations](<search/Benchmarking Query Analysis in High Cardinality Situations.md>) · `search` · langchain
  Benchmarks query analysis in high-cardinality situations, relevant to retrieval, search, and observability filtering workloads.
- **2024-03-06** — [Evaluate RAG with LLM Evals and Benchmarks](<pipelines/Evaluate RAG with LLM Evals and Benchmarks.md>) · `pipelines` · arize
  Workshop recap on evaluating RAG systems with LLM evals and benchmarks.
- **2024-02-23** — [🪆 Introduction to Matryoshka Embedding Models](<embeddings/🪆 Introduction to Matryoshka Embedding Models.md>) · `embeddings` · huggingface
  Matryoshka Representation Learning trains embeddings whose leading dimensions are independently useful, so vectors can be truncated (e.g. 768 -> 64) with small quality loss; compares a Matryoshka vs regular model across truncation sizes and shows the Sentence Transformers loss to train one.
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
- **2020-05-22** — **[Paper]** [Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks](<pipelines/[Paper] Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks.md>) · `pipelines` · arxiv
  Introduces Retrieval-Augmented Generation: a seq2seq model coupled to a dense-vector Wikipedia index via DPR, with the retriever and generator fine-tuned end-to-end. Sets SOTA on three open-domain QA tasks and yields more factual, specific generations than a parametric-only BART baseline.

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
- **2026-06-17** — [Clustering billions of products for agentic commerce with Catalog API (2026)](<../product-engineering/case-studies/Clustering billions of products for agentic commerce with Catalog API (2026).md>) · `case-studies` · shopify
  How Shopify clusters billions of product listings across millions of stores into canonical entities via embeddings for its agentic-commerce Catalog API, reconciling inconsistent merchant listing structures.
- **2026-05-13** — [Tau-Knowledge: benchmarking agents on realistic knowledge](<../evals-observability/benchmark-design/Tau-Knowledge benchmarking agents on realistic knowledge.md>) · `benchmark-design` · sierra
  Introduces tau-knowledge for benchmarking agents on realistic knowledge tasks that require grounded retrieval and use of external information.
- **2026-04-29** — [Using context graphs: build a data moat like Google's using your enterprise data](<../agents/memory-context/Using context graphs build a data moat like Google's using your enterprise data.md>) · `memory-context` · arize
  Explains context graphs as an enterprise memory layer for agents and retrieval-heavy AI systems.
- **2026-02-25** — [The generative recommender behind Shopify's commerce engine (2026)](<../models/architectures/The generative recommender behind Shopify's commerce engine (2026).md>) · `architectures` · shopify
  Shopify's generative recommender treats a buyer's cross-storefront event history as a sequence and predicts the next action, a sequence-modeling approach to commerce recommendations over months-long journeys.
- **2025-11-12** — [Building world-class product search at Shopify: Where C++ excellence meets ML innovation (2025)](<../inference/serving/Building world-class product search at Shopify Where C++ excellence meets ML innovation (2025).md>) · `serving` · shopify
  How Shopify runs transformers, neural rankers, and gradient-boosted models (LightGBM, CatBoost) at native C++ speed for product search, meeting millisecond-latency-at-scale while keeping fast ML iteration.
- **2025-09-09** — [mmBERT: ModernBERT goes Multilingual](<../models/training/mmBERT ModernBERT goes Multilingual.md>) · `training` · huggingface
  mmBERT is a ModernBERT-style multilingual encoder trained on 3T+ tokens across 1,800+ languages using a three-phase schedule with an inverse masking-ratio decay and 'annealed language learning' that progressively adds low-resource languages late in training. Beats XLM-R and mGTE on multilingual retrieval and classification while running significantly faster.
- **2025-07-16** — [Ettin Suite: SoTA Paired Encoders and Decoders](<../models/training/Ettin Suite SoTA Paired Encoders and Decoders.md>) · `training` · huggingface
  Ettin is the first suite of paired encoder-only and decoder-only models (17M-1B params) trained on identical data (2T tokens), architecture and recipe, giving a true apples-to-apples MLM vs causal-LM comparison. The open ModernBERT-style recipe beats ModernBERT on encoder tasks and beats Llama 3.2 1B and SmolLM2 on decoder tasks; also tests cross-objective continued training.
- **2025-04-16** — [Open Deep Research](<../agents/tool-use/Open Deep Research.md>) · `tool-use` · together
  Describes an open deep research system combining retrieval, planning, and tool use.
- **2024-12-19** — [Finally, a Replacement for BERT: Introducing ModernBERT](<../models/architectures/Finally, a Replacement for BERT Introducing ModernBERT.md>) · `architectures` · huggingface
  ModernBERT (149M base / 395M large) modernizes the BERT encoder with 8192-token context, rotary embeddings, alternating global/local attention, GeGLU, unpadding and Flash Attention 2, trained on 2T tokens of web+code — a Pareto improvement over BERT/DeBERTa on both speed and accuracy and a slot-in replacement for retrieval and classification encoders.
- **2024-10-28** — [Expert Support case study: Bolstering a RAG app with LLM-as-a-Judge](<../evals-observability/llm-as-judge/Expert Support case study Bolstering a RAG app with LLM-as-a-Judge.md>) · `llm-as-judge` · huggingface
  Digital Green's agricultural advisory RAG chatbot for smallholder farmers adds an LLM-as-a-Judge evaluation loop, with judge prompt/criteria design and human-alignment checks used to iterate on retrieval and answer quality.
- **2024-07-25** — [Building A Generative AI Platform](<../product-engineering/architecture/Building A Generative AI Platform.md>) · `architecture` · chip-huyen
  Reference architecture for generative AI platforms covering context construction and RAG, guardrails, gateways and routers, caching, observability, orchestration, and tool/action layers.
- **2024-07-09** — [Banque des Territoires (CDC Group) x Polyconseil x Hugging Face: Enhancing a Major French Environmental Program with a Sovereign Data Solution](<../product-engineering/case-studies/Banque des Territoires (CDC Group) x Polyconseil x Hugging Face Enhancing a Major French Environmental Program with a Sovereign Data Solution.md>) · `case-studies` · huggingface
  Banque des Territoires (CDC) x Polyconseil build a sovereign, on-prem RAG assistant for the EduRénov program using open models (Mistral-7B-Instruct, Sentence Transformers, TGI): retriever/reader architecture, data-sovereignty constraints, and production lessons.
- **2024-06-25** — [XLSCOUT Unveils ParaEmbed 2.0: a Powerful Embedding Model Tailored for Patents and IP with Expert Support from Hugging Face](<../product-engineering/case-studies/XLSCOUT Unveils ParaEmbed 2.0 a Powerful Embedding Model Tailored for Patents and IP with Expert Support from Hugging Face.md>) · `case-studies` · huggingface
  XLSCOUT fine-tunes BGE-base into ParaEmbed 2.0 on expert-curated patent data, gaining 23% accuracy over its predecessor and beating GPT-4/text-embedding-ada-002 on patent prior-art retrieval — a case for domain-specific open embeddings over closed APIs.
- **2024-04-29** — [How fine tuned LLMs power knowledge assist, summarization, and chat suggestions](<../models/fine-tuning/How fine tuned LLMs power knowledge assist, summarization, and chat suggestions.md>) · `fine-tuning` · cresta
  Explains how fine-tuned LLMs support knowledge assist, summarization, and chat suggestions in production workflows.
- **2024-04-26** — [Beating proprietary models with a quick fine-tune](<../models/fine-tuning/Beating proprietary models with a quick fine-tune.md>) · `fine-tuning` · modal
  Explains fine-tuning embedding models to beat proprietary baselines for a retrieval task with a compact training loop.
- **2024-04-04** — [Text2SQL using Hugging Face Dataset Viewer API and Motherduck DuckDB-NSQL-7B](<../prompt-engineering/structured-output/Text2SQL using Hugging Face Dataset Viewer API and Motherduck DuckDB-NSQL-7B.md>) · `structured-output` · huggingface
  Text-to-SQL walkthrough using MotherDuck's DuckDB-NSQL-7B (Llama-2-7B fine-tuned on DuckDB SQL pairs) with the HF Dataset Viewer parquet API: schema-in-prompt templating, generation, and executing the SQL against DuckDB.
- **2024-02-20** — [Evaluating and Analyzing Your RAG Pipeline with Ragas](<../evals-observability/evaluation/Evaluating and Analyzing Your RAG Pipeline with Ragas.md>) · `evaluation` · arize
  Explains how to evaluate RAG pipelines with Ragas and Phoenix, including retrieval and generation quality dimensions.
- **2023-04-11** — [Building LLM applications for production](<../product-engineering/architecture/Building LLM applications for production.md>) · `architecture` · chip-huyen
  Practical guide to production LLM applications covering task decomposition, retrieval, prompt construction, evaluation, monitoring, and latency/cost tradeoffs.
