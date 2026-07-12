---
title: Brainstore makes AI observability at scale possible
topic: evals-observability
subtopic: monitoring
secondary_topics:
- infra-platform/deployment
summary: Benchmark-oriented note on Brainstore performance and why purpose-built storage
  is needed for high-volume AI observability workloads.
source: braintrust
url: https://www.braintrust.dev/blog/brainstore-benchmarks
author: Braintrust Team
published: '2025-12-18'
fetched: '2026-07-11T04:31:35Z'
classifier: codex
taxonomy_rev: 1
words: 482
content_sha256: fba9709a3154c509483a54bf180424755303c6eeaec4077b60037037b9936a2f
---

# Brainstore makes AI observability at scale possible

18 December 2025Ornella Altunyan3 min

AI systems generate massive amounts of data. A single trace can contain thousands of spans, each with gigabytes of prompt and response data. Traditional observability databases weren't built for this scale, which means teams either wait minutes for queries to complete or can't query their production data at all.

Brainstore is a purpose-built database for AI observability. It handles the volume and complexity of modern AI systems while delivering query times under one second, even across terabytes of data.

The numbers speak for themselves. Testing against a leading competitor on identical production workloads with 3.9 million traces shows Brainstore is significantly faster across every operation:

23.9x

Faster full text searchCompetition

9,587 ms

Brainstore

401 ms

2.55x

Faster write latencyCompetition

17,775 ms

Brainstore

6,984 ms

3.73x

Faster span load timeCompetition

1,290 ms

Brainstore

346 ms

Full text search is where the difference is most dramatic. Searching for a specific error message or prompt phrase completes in under half a second with Brainstore, compared to nearly 10 seconds with the competitor. That's the difference between interactive debugging and waiting around for results.

AI teams need to move fast. When a production issue hits, engineers need to search logs, identify the problem, and test a fix. If each query takes 10 seconds instead of half a second, debugging sessions stretch from minutes to hours.

Brainstore makes it possible to work with AI observability data at production scale. Teams can search through millions of traces in real time, filter by complex conditions, and get results instantly. The full workflow from finding an issue to deploying a fix happens without waiting for slow queries.

Unlike traditional databases that rely on persistent disks, Brainstore stores all data on S3 or similar object storage. This makes it infinitely scalable, resilient, and far simpler to operate. Popular commercial solutions partially use object storage but still rely on persistent disks for metadata and consensus, making them complex to self-host.

Data warehouses typically store everyone's data in one massive table, which slows down queries as the table grows. Brainstore partitions each organization's data separately, keeping queries fast regardless of total database size.

AI logs contain deeply nested JSON with varying schemas. Brainstore uses [Tantivy](https://github.com/quickwit-oss/tantivy), an open-source library with a built-in inverted index and columnstore designed for this exact use case. Traditional data warehouses try to "shred" JSON into columns, which breaks down as schemas evolve.

Brainstore also implements a custom write-ahead log (WAL) for real-time writes. As soon as a WAL entry is written to object storage, it's immediately available for reads alongside the indexed data, making Brainstore strongly consistent. The WAL is compacted into optimized Tantivy indices in the background.

For a deeper dive into Brainstore's architecture, see the [technical blog post](https://www.braintrust.dev/brainstore).

Brainstore is on by default for all SaaS and self-hosted customers. Want to see how it handles your production workload? [Book a demo →](https://www.braintrust.dev/contact)
