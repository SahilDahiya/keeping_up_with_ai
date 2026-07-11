---
title: 'Your client code matters: 12x higher embedding throughput with Python and
  Rust'
topic: rag-retrieval
subtopic: embeddings
secondary_topics:
- inference/optimization
summary: Shows how client implementation choices in Python and Rust affect embedding
  throughput.
source: baseten
url: https://www.baseten.co/blog/your-client-code-matters-10x-higher-embedding-throughput-with-python-and-rust/
author: Michael Feil
published: '2025-06-12'
fetched: '2026-07-11T04:07:56Z'
classifier: codex
taxonomy_rev: 1
words: 1353
content_sha256: 80d40280e7c362ab2f4d7d13c01d212c847218a9ab2762916e5e45ee1b524f47
triage: keep
skip_reason: null
---

# Your client code matters: 12x higher embedding throughput with Python and Rust

![The Baseten Performance Client](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1749761203-text-template-3.png%3Fauto%3Dformat%26fit%3Dcrop%26h%3D630%26w%3D1200&w=3840&q=100)

The Baseten Performance Client is a new [open-source Python library](https://github.com/basetenlabs/truss/tree/main/baseten-performance-client) (built with Rust) that massively improves throughput for high-volume embedding tasks, like standing up a new vector database or pre-processing text samples for model training. The client is OpenAI-compatible, so whether you are running models on Baseten (I hope you are) or using another inference provider, our Performance Client can improve embedding throughput by up to 12x.

We achieve this boost by freeing Python’s Global Interpreter Lock (GIL) during network-bound tasks – allowing true parallel request execution. The result is dramatically lower latencies under heavy loads; for example, in our benchmarks with large batches of embeddings, `PerformanceClient` delivered results in **1 minute and 11 seconds vs. more than 15 minutes** for a standard `AsyncOpenAI` client at extreme scale (2,097,152 parallel inputs). It also fully utilizes multi-core CPUs to maximize throughput.

![The Baseten Performance Client achieves 12x faster corpus backfill in an extremely high-volume test](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1749832130-diagram-9.png%3Fauto%3Dformat%26w%3D1200&w=3840&q=75) The Baseten Performance Client achieves 12x faster corpus backfill in an extremely high-volume test.

The Baseten Performance Client achieves 12x faster corpus backfill in an extremely high-volume test.Using the client is as simple as pointing it to your embedding model’s endpoint (whether you’re running on Baseten, OpenAI, or any OpenAI-compatible service) and swapping in our client class. You’ll immediately benefit from higher throughput and lower latencies for tasks like semantic search (embeddings), retrieval-augmented generation (where you might embed and then rerank documents), or real-time classification of content.

In this post, we’ll explain how `PerformanceClient` works under the hood, compare it to a typical Python client, and show why it has such a high impact on high-volume embedding, reranking, classification, and custom batched workloads.

## How the Baseten Performance Client removes inference performance bottlenecks

Python’s infamous Global Interpreter Lock (GIL) prevents multiple threads from executing Python code at the same time. This means that even if you spawn many threads to send embedding requests, the GIL often serializes their execution, becoming a bottleneck.

In I/O-heavy workflows, like embedding large document corpora or handling thousands of simultaneous user queries, pure-Python clients can struggle – the GIL causes contention and idle CPU cores. While Python’s `asyncio` can interleave I/O tasks in a single thread, it still can’t harness multiple CPU cores effectively, and overhead grows with huge numbers of coroutines.

At Baseten, we see developers sending traffic to hundreds of GPU replicas simultaneously. The OpenAI client only allows 2,048 batched items per request, and Python multi-core processing does not allow for sharing objects like an HTTP request pool. This adds high latency overhead to workloads.

`PerformanceClient` sidesteps this limitation by leveraging Rust and [PyO3](https://pyo3.rs/v0.25.0/) to release the GIL during network calls. Under the hood, PerformanceClient uses PyO3’s `Python::allow_threads` to temporarily drop the GIL while Rust code runs. The embedding requests are executed on a global [Tokio](https://tokio.rs/) runtime (a high-performance async executor in Rust) that can spawn many tasks across OS threads.

Because the GIL is not held when these requests are in flight, multiple HTTP requests for embeddings can proceed in parallel. Other Python threads can run, and all CPU cores can be kept busy with networking and JSON processing. Once the Rust side has the responses ready, it reacquires the GIL only to assemble results for Python, minimizing GIL-held time. This architecture allows dozens or even hundreds of embedding requests to be handled concurrently, without Python becoming the bottleneck.

**Getting started with the Baseten Performance Client**

You can install [PerformanceClient](https://pypi.org/project/baseten-performance-client/) from PyPi.

`pip install baseten_performance_client`The function signature for PerformanceClient is similar to the OpenAI client.

```
1from baseten_performance_client import PerformanceClient
2import os
3
4client = PerformanceClient(
5     api_base="<https://model-xxxxxx.api.baseten.co/environments/production/sync>",
6     api_key=os.environ["BASETEN_API_KEY"]
7  )
8
9texts = ["Hello world", "Embed this text.", "Third sample."]
10response = client.embed(
11    input=texts,
12    model="my_model",
13    batch_size=4,
14    max_concurrent_requests=32,
15    timeout_s=3600,
16)
17print(response.data[0].embedding)
18# Async
19# response = await client.aembed(
20#    ...
21# )
```
Whether you’re using OpenAI, Baseten, or another OpenAI-compatible embedding inference provider, you can swap out your client in seconds and see up to 12x higher throughput for extremely large workloads.

**Benchmarking Baseten’s Performance Client vs. AsyncOpenAI**

To quantify the benefits, we benchmarked our Performance Client against a standard asynchronous OpenAI API client across increasing numbers of simultaneous embedding requests (each with 128 embeddings, so ranging from 128 up to 2,097,152 embeddings total). The workload simulates a high-concurrency scenario: many small texts being embedded at once.

![The Baseten Performance Client’s relative performance improves with workload scale](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1749831884-diagram-10-2.png%3Fauto%3Dformat%26w%3D1200&w=3840&q=75) The Baseten Performance Client’s relative performance improves with workload scale. A full breakdown of the results can be found in the table below.

The Baseten Performance Client’s relative performance improves with workload scale. A full breakdown of the results can be found in the table below.As concurrency increases, the differences in latency and resource usage become stark:

- **Fast at extreme scale:**At the highest load (2,097,152 parallel inputs), the Baseten Performance Client returned all embeddings in- **1 minute and 11 seconds**, whereas the typical AsyncOpenAI-based client took- **more than 15 minutes**to complete the same work. This 12x speedup showcases how removing the GIL bottleneck lets requests flow through as quickly as the network and CPUs allow.
- **Efficient multi-core utilization:**- `PerformanceClient`drove average CPU utilization to- **≈280%**(on a 16-core machine), effectively utilizing multiple cores for parsing JSON, handling sockets, and other tasks. The Python- `AsyncOpenAI`client, by contrast, was largely bound by the GIL to a single core (peaking around 100% CPU on one core), leaving most of the machine’s potential untapped.
- **Scaling with input size:**Even at more moderate batch sizes (e.g., 1k or 10k concurrent requests), our Performance Client consistently achieved lower latency per batch and higher throughput than the pure-Python client. The gap widens as you scale up the workload – a testament to the overhead of Python’s context-switching and- `asyncio`event loop vs. Rust’s optimized asynchronous execution.

These results make it clear that when you need to embed massive datasets or serve thousands of embedding queries in parallel, the Baseten Performance Client can dramatically cut down latency and throughput bottlenecks. By letting Rust handle the heavy lifting, it avoids the Python overhead that grows with each extra thread or coroutine. We are also releasing the benchmarking code [here](https://github.com/basetenlabs/truss/blob/26a7de3ff1e4341c074b0c1d0ef62899bb4ea7b6/baseten-performance-client/scripts/compare_latency_openai.py).

**Extensible synchronous and asynchronous APIs**

One of the standout features of Baseten’s `PerformanceClient` is that it supports both synchronous and asynchronous usage.

If you prefer simple sync code, you can call the embedding methods in a blocking fashion:

`embeddings = client.embed(list_of_texts))`Internally, it will still run the requests concurrently on Rust threads, not blocking other Python operations. Thanks to the GIL release, even the “blocking” calls won’t freeze your Python program. Other threads can do work while embeddings are fetching.

Conversely, if you’re writing an async application (for example, an async web server handling user queries), `PerformanceClient` provides async methods that integrate with `asyncio` seamlessly:

`await client.async_embed(texts))`This flexibility means you can drop PerformanceClient into existing codebases – synchronous scripts or async frameworks – and get a safe, significant speed boost with minimal changes.

## Support for general batch requests

The `PerformanceClient` extends performant inference beyond the boundaries of the OpenAI client to support modalities like classification and reranking. With support for user-side batching (sending multiple payloads to the same URL via `batch_post`), `PerformanceClient` is a great choice for synthetic data generation or batch processing.

```
1client = PerformanceClient(
2     api_base="<https://model-xxxxxx.api.baseten.co/environments/production/sync>",
3     api_key=os.environ["BASETEN_API_KEY"]
4
5custom_request1 = {"model": "my_model", "input": ["Hello world 1"]}
6custom_request2 = {"model": "my_model", "input": ["Hello world 2"]}
7
8response = client.batch_post(
9    url_path="/v1/embeddings", # sent to api_base/v1/embeddings
10    payloads=[custom_request1, custom_request2],
11    max_concurrent_requests=192,
12)
```
You can use the Baseten Performance Client with leading open-source models like [BGE Reranker M3](https://www.baseten.co/library/bge-reranker-m3/) and [Tulu 8B Reward](https://www.baseten.co/library/tulu-3-8b-reward/).

**Open-source and ready for production**

We built the Baseten Performance Client to empower developers running large-scale embedding, reranking, and classification workloads to get production-level performance right from their Python code. It’s available as an open-source package, and we welcome you to check out the code, contribute, or file issues on [our GitHub](https://github.com/basetenlabs/truss/tree/main/baseten-performance-client).

For an embedding service that can keep up with this level of throughput at extremely low latencies, try [embedding models deployed on Baseten](https://www.baseten.co/library/tag/embedding/) optimized with [Baseten Embedding Inference](https://www.baseten.co/blog/how-we-built-high-throughput-embedding-inference-with-tensorrt-llm/).
