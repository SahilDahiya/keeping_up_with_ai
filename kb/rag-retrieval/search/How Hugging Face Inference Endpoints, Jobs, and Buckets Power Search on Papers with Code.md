---
title: How Hugging Face Inference Endpoints, Jobs, and Buckets Power Search on Papers
  with Code
kind: blog
topic: rag-retrieval
subtopic: search
secondary_topics:
- inference/serving
summary: 'Details the hybrid search architecture behind Papers with Code: an offline
  Jobs pipeline embeds papers with Qwen3-Embedding into a versioned pgvector contract
  (HNSW, 0.9955 Recall@20 at 256 dims), while online queries fuse lexical and semantic
  branches via weighted RRF and fall back to full-text search if the Inference Endpoint
  is cold or unhealthy.'
triage: null
skip_reason: null
source: huggingface
url: https://huggingface.co/blog/pwc-search
author: Niels Rogge
published: '2026-08-21'
fetched: '2026-08-26T06:15:19Z'
classifier: claude
taxonomy_rev: 2
words: 1816
content_sha256: 2edeac0618c62d230780b11601b21084b3395902a8ac4203d9b8af10635ba487
---

# How Hugging Face Inference Endpoints, Jobs, and Buckets Power Search on Papers with Code

[Feature Extraction •  0.6B • Updated   •  7.04M  •  1.17k](https://huggingface.co/Qwen/Qwen3-Embedding-0.6B)  

#### Qwen/Qwen3-Embedding-0.6B

![](https://cdn-avatars.huggingface.co/v1/production/uploads/6215ca5692c0ecfba9186921/hrRM50-6XcdWgg2AKpENG.jpeg) 

Published
					August 21, 2026 

  Upvote 

 9

3 months ago, we started a [revival](https://www.reddit.com/r/MachineLearning/comments/1tgmwqr/reviving_paperswithcode_by_hugging_face_p/) of [Papers with Code](https://paperswithcode.co) (see also the [announcement tweet](https://x.com/NielsRogge/status/2056366395605078252)). Its goal is to make open AI research accessible and digestible, so that people can easily find the artifacts related to a paper, find state-of-the-art (SOTA) across the various domains of AI, share interesting research and build on top of each other's work. In other words, its goal is to power the wave of research that leads to the next [Transformer](https://paperswithcode.co/paper/1706.03762).
It's important to note that searching for research is not quite the same as searching for regular text. A useful paper search engine should find an exact title or arXiv identifier, but it should also understand a query such as “small language models for code generation” even when those words do not appear together in a paper. It needs to recognize that “the original BERT paper” is a navigational request, tolerate an incomplete title or typos, and still respond quickly when a model service is cold or temporarily unavailable.

  ![Papers with Code search results for the query 'DINO'](https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/blog/pwc-search/search-results.png) 

Search results on Papers with Code for the query DINO. 
 
  ![Chart showing hybrid retrieval outperforming vector-only and keyword search](https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/blog/pwc-search/hybrid-search.png) 

Hybrid retrieval outperforms keyword- and vector-only search. Figure from Microsoft, [Azure AI Search: Outperforming vector search with hybrid retrieval and reranking](https://techcommunity.microsoft.com/blog/azure-ai-foundry-blog/azure-ai-search-outperforming-vector-search-with-hybrid-retrieval-and-reranking/3929167) (2023). 
 
## 
	
		
	
	
		TL;DR
	

We deliberately split search into an offline corpus build and an online search service:

  ![Architecture diagram of the offline corpus build and online hybrid search pipeline](https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/blog/pwc-search/architecture.png) 

Architecture of the offline corpus build and online hybrid search pipeline. 
 
The expensive, throughput-oriented work runs as Jobs. Durable artifacts live in a Bucket. Only the small query-embedding step sits on the request path, behind a protected Inference Endpoint, to power the online search. If that endpoint is cold, busy, or unhealthy, search immediately falls back to full-text retrieval. This separation makes the system both powerful and fast.

## 
	
		
	
	
		Start with a strict embedding contract
	

Embedding pipelines often fail in subtle ways: a model revision changes, query and document prompts are mixed up, vectors are truncated differently, or an updated abstract no longer matches its stored vector.

We avoid this by treating the embedding format as a versioned API. Every paper is encoded as:

This contract follows an embedding from export, through GPU inference, into PostgreSQL, and finally into online retrieval.

## 
	
		
	
	
		Jobs turn a database snapshot into a vector corpus
	

Our corpus build starts by exporting the latest version of every paper from a repeatable-read PostgreSQL snapshot. The exporter streams rows rather than loading the catalog into memory, writes bounded JSONL shards, and creates a manifest containing row counts and SHA-256 checksums.

Each completed shard has its own marker, so a restarted Job can skip verified work. This is useful for a large corpus: retrying should just resume work rather than overwriting existing embeddings.

In our 5,000-paper pilot, the Qwen Job encoded about 75 papers per second at 1024 dimensions on an L4 GPU. The same pass could be deterministically materialized at 512 and 256 dimensions, so we could compare the storage and retrieval trade-offs without paying for more inference.

## 
	
		
	
	
		Buckets are the connective tissue
	

For us, the Bucket is more than a place to put vectors. It is the boundary between three systems with different lifecycles:

We organize artifacts under immutable run prefixes:

Buckets themselves are intentionally mutable, so immutability is an application-level rule: a run ID is never overwritten, and every artifact is covered by a manifest and checksum.

## 
	
		
	
	
		Inference Endpoints put semantic search on the request path
	

Batch embeddings solve the document side of retrieval. A user query still needs to be embedded at request time using the same model contract.

  ![Hugging Face Inference Endpoint overview for the Papers with Code query embedding model](https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/blog/pwc-search/inference-endpoint.png) 

Hugging Face Inference Endpoint for the Papers with Code query embedding model. 
 
The API then performs a cosine-distance search over the active pgvector generation:

The HNSW index keeps this lookup fast. On our 5,000-paper pilot, the 256-dimensional Qwen index achieved 0.9955 Recall@20 against exact search, with 1.31 ms p50 and 2.21 ms p95 HNSW lookup latency. Its table and index used about 27% of the storage of the 1024-dimensional version while retaining essentially the same ANN recall in that test.

Our query client therefore has deliberately strict behavior:

If the endpoint is scaling up, times out, returns a malformed vector, or has no concurrency available, we skip the semantic branch immediately. Users still receive lexical results instead of waiting for an unreliable dependency.

Inference Endpoints works really reliably, and includes a nice dashboard so you can quickly see key analytics.

  ![Hugging Face Inference Endpoint analytics dashboard showing request volume, errors, latency, and replica state](https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/blog/pwc-search/endpoint-analytics.png) 

Inference Endpoint analytics showing request volume, errors, latency, and replica state. 
 
## 
	
		
	
	
		Hybrid retrieval is stronger than either branch alone
	

For every query, the lexical branch retrieves up to 50 candidates using weighted PostgreSQL full-text search. The semantic branch retrieves up to 50 candidates from pgvector.

We combine their ranks using weighted reciprocal rank fusion (RRF):

RRF is simple and robust, because it combines ranks rather than scores from two systems with different scales. Basically, if a paper is ranked high both by the lexical branch and the semantic branch, it has a higher chance of being ranked high by the hybrid search. We currently use equal branch weights and (k=60) (k is the "rank constant", a hyperparameter of the RRF algorithm).

Dense retrieval improves recall for conceptual queries. Full-text retrieval remains excellent for exact terminology, identifiers, and rare names. We also preserve deterministic identity behavior on top of the fused ranking:

## 
	
		
	
	
		One Endpoint, two update paths
	

The large initial corpus is embedded with Jobs, but Papers with Code changes continuously. New papers arrive, abstracts are corrected, and new arXiv versions become current.

Each run processes at most 500 papers in batches of 16. Before an embedding is written, the source row is locked and its content hash is checked again. If a paper changed during inference, that vector is discarded and picked up by the next run.

The hourly path keeps the active index close to the live catalog without turning an online endpoint into an unbounded batch processor.

## 
	
		
	
	
		Related papers become almost free online
	

The same document embeddings also power related-paper recommendations on each paper page.

  ![Related papers feature](https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/blog/pwc-search/related_papers.png) 

Related papers for [SenseNova-U1](https://paperswithcode.co/paper/2605.12500). 
 
## 
	
		
	
	
		What we learned
	

### 
	
		
	
	
		1. Separate throughput work from latency-sensitive work
	

Corpus embedding and query embedding use the same model, but they are different infrastructure problems. Jobs optimize for throughput and bounded cost; Inference Endpoints optimize for availability and request latency.

### 
	
		
	
	
		2. Make storage the explicit contract between compute and production
	

Buckets provide an explicit handoff between compute and production. Checksummed artifacts create a reviewable boundary before data enters the production index.

### 
	
		
	
	
		3. Pin more than the model name
	

The revision, dimension, prompt, normalization, and input formatter all affect retrieval. Store them together and validate them everywhere.

### 
	
		
	
	
		4. Design for cold starts
	

Scale-to-zero is valuable when traffic is intermittent, but only if the product has a fast fallback. Hybrid search gave us that fallback naturally: lexical search is always useful on its own.

### 
	
		
	
	
		5. Smaller vectors can be a systems feature
	

Matryoshka embeddings let us evaluate quality, memory, index size, and latency as one trade-off. In our pilot, 256 dimensions preserved ANN recall while materially shrinking storage compared with 1024 dimensions.

### 
	
		
	
	
		6. Activation should be boring
	

New generations are imported beside the current one, indexed independently, checked for complete and current coverage, and then activated atomically. Rollback is a configuration change, not an emergency recomputation.


- [Hugging Face Jobs](https://huggingface.co/docs/hub/jobs) gives us burstable GPU compute for embedding the paper corpus.
- [Hugging Face Storage Buckets](https://huggingface.co/docs/hub/storage-buckets) provides the durable handoff between our database, experiments, and Jobs.
- [Hugging Face Inference Endpoints](https://huggingface.co/docs/inference-endpoints/index) serves low-latency embeddings for live queries and incremental updates.

```
normalized title + "\n\n" + normalized abstract
```
For each vector generation, we record:

- the model repository and exact revision;
- the output dimension;
- the input-format version;
- whether the input is a query or a document;
- the normalization method;
- a content hash for the source title and abstract.

- one can specify a **dynamic embedding size** , which allows to trade-off quality with speed/storage costs. Qwen models call this "MRL" which is short for[Matryoshka Representation Learning](https://paperswithcode.co/paper/2205.13147) . You can learn all about it[here](https://huggingface.co/blog/matryoshka) . We chose an embedding size of 256 to make the search fast.
- one can provide an **instruction prompt** . Qwen embedding models support a`document` prompt (which we use to embed the papers) and live searches use their`query` prompt (to embed the user query).

The worker:

1. verifies the input manifest and every shard checksum;
2. loads the pinned model revision;
3. sorts texts by length to reduce padding;
4. calls `encode_document` in batches (as noted in the[model card](https://huggingface.co/Qwen/Qwen3-Embedding-0.6B) );
5. reduces the batch size automatically if the GPU runs out of memory;
6. truncates the [Matryoshka representation](https://huggingface.co/blog/matryoshka) to 256 dimensions and normalizes it;
7. writes float16 Parquet shards atomically; and
8. records throughput, package versions, hardware, peak VRAM, row counts, and output checksums.

- the production database exports source records;
- ephemeral Jobs consume those records and produce vectors;
- the importer validates the results before touching the search index.

This gives us several useful properties:

- **Reproducibility:** we can trace a database generation back to an exact corpus snapshot, model revision, and set of artifacts.
- **Safe retries:** Jobs can resume from completed shards in the same run prefix.
- **Cheap experiments:** several models or dimensions can reuse one verified input snapshot.
- **Controlled rollout:** importing a generation does not activate it. We first validate coverage and build its index.
- **Simple rollback:** the previous generation and its artifacts remain available until the new one is proven stable.

- a one-second production timeout;
- a non-blocking concurrency limit;
- response dimension, finiteness, and norm validation;
- a short cache keyed by the query and embedding generation;
- a circuit breaker after repeated failures; and
- no raw query text in logs, only a normalized fingerprint.


- exact titles and arXiv IDs stay at the top;
- the [method taxonomy](https://paperswithcode.co/methods) recognizes navigational searches such as “the original BERT paper”;
- incomplete titles and bounded spelling mistakes use conservative trigram candidates; and
- ambiguous fuzzy matches abstain rather than forcing a bad result.

This gives us a useful division of labor:

- **Jobs** handle full rebuilds, new model generations, and large backfills.
- **Inference Endpoints** handle interactive query embeddings and small incremental document updates.
- **Buckets** preserve the large-build artifacts and make those builds resumable and auditable.

📊

 7.63k

Embedding Leaderboard

More Articles from our Blog

guidevllminference

  12

 June 26, 2026 audiospeechbenchmark

 
- +3

 53

 August 21, 2026
