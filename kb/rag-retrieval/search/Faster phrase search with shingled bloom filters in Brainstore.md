---
title: Faster phrase search with shingled bloom filters in Brainstore
topic: rag-retrieval
subtopic: search
secondary_topics:
- evals-observability/tracing
summary: Explains faster phrase search over Brainstore data using shingled bloom filters,
  aimed at efficient trace and log search for AI observability.
source: braintrust
url: https://www.braintrust.dev/blog/brainstore-phrase-search
author: Braintrust Team
published: '2026-07-07'
fetched: '2026-07-11T04:31:40Z'
classifier: codex
taxonomy_rev: 1
words: 1254
content_sha256: 6532f55ee174b29224643ba09a60ab7a04771ebdd8be38407dc75a019359df70
---

# Faster phrase search with shingled bloom filters in Brainstore

7 July 2026Ankur Goyal7 min

When you debug an agent, you often start from a bit of text you saw somewhere, maybe a line in a Slack screenshot, a snippet from an X post, or an output you want to trace back through your logs. Say you search for "They also touched on AI provider modifications." Every word in it shows up in almost every trace, but the exact wording, in that order, is rare. Common terms with a rare intersection is the worst case for a traditional search system, and at agent scale, where a dataset can balloon past 100TB of text, it is the difference between an instant answer and a query that never returns. Search stays fast when at least one term is rare or the intersection is common, but when the terms are common and the intersection is rare, performance falls apart.

[Brainstore](https://www.braintrust.dev/blog/brainstore), our database built specifically for agent traces, ran into this wall. Searches like that one would time out after several minutes while scanning more than 100 GB. We solved it with shingled bloom filters, which enabled better segment elimination and let Brainstore scan under 4 GB and successfully return the correct text, a more than 25x increase in efficiency. Here is how.

[Brainstore's search stack](https://www.braintrust.dev/blog/brainstore-architecture) runs over large, semi-structured logs. It uses an inverted index plus columnar structures via Tantivy, stores data in object storage, and keeps a write-ahead log for real-time visibility.

In that layout, query time is determined by how many segments you touch, and queries run fast when you can confidently eliminate almost every segment before doing any heavy work. Classic inverted-index retrieval leans on at least one rare term to do that. When a term is rare, its postings list is short, that short list is the candidate set, and most segments fall away.

Phrase search has no rare term, only rare orderings of multiple terms. Every token fans out to a huge postings list, and most segments plausibly contain every word, which necessitates a lot of work before eliminating anything. Initially we tried to solve this problem with bloom filters, but the standard approach of using unigram bloom filters wasn't helpful.

Bloom filters have a reputation for being a leaky abstraction, but this is based on using bloom filters in the wrong context. A bloom filter is a pruning tool, and pruning only pays off when the answer is usually "no." Point it at a selective predicate and it's one of the best tools available. Point it at the kind of query common in agent debugging workflows and it costs you a probe.

Brainstore keeps a per-segment bloom filter to answer "does this segment contain token X?" without reading the segment. Equality filters on high-cardinality fields like request ids, session ids, and conversation ids feel instant, even on cold object storage. This is what bloom filters are good at, and they work well in these contexts.

Phrase search complicates this approach. Probe the filter for the term "also" and it doesn't return a helpful answer, because "also" is in nearly every segment. The same holds for every other word in what you're searching for. When using bloom filters this way, you keep almost all segments and pay the cost because the bloom filter can't prune properly. Finding the individual terms is easy; the hard part is finding multiple terms in a specific order.

The solution was to use shingled bloom filters based on trigrams, not unigrams. Take the query from the opening, "They also touched on AI provider modifications." It produces the following trigrams:

- they also touched
- also touched on
- touched on ai
- on ai provider
- ai provider modifications

The individual words in isolation are common, the three-word combinations are rare, and the intersection of several shingles from the whole sentence is rarer still. So instead of probing for a single word, we decided to probe for a shingle.

To make this work in Brainstore, we built indexing that emits trigrams. For each tokenized text field we search, we tokenize as usual, then at each position emit a shingle of three consecutive tokens, and add those shingles to the same per-segment structure we already probe for unigrams. This reuses Brainstore's existing segment-elimination machinery, with only the indexed unit changed.

Three tokens is selective enough to break the "everything matches" problem in traditional approaches to phrase search. It stays robust to minor variation, since a sentence produces multiple overlapping shingles and you don't need all of them to match. It's also cheap to compute at index time and cheap to probe at query time.

Before, unigram signals were too common, almost nothing got pruned, and phrase search fanned out across segments. After, the shingles are selective, pruning is aggressive, and phrase search behaves like an equality filter.

When developing this approach, we tested it on a representative slice of real customer usage, not a synthetic benchmark. The dataset contained 6.4 million spans, each averaging 45 KB, for a total size of around 290 GB.

The test case was finding a single trace that contained text from a support screenshot. Only one document contained the search term, but traditional single-term bloom filters only eliminated 5% of the dataset. With shingle search enabled, we eliminated 98.5% of the dataset. This let us find the desired trace while scanning less than 4 GB of data. Without shingle search, the query would time out after scanning more than 100 GB.

That 290 GB is a slice, but the advantage is a property of the data, not its size. A shingle prunes because the ordered terms are rare, and they stay rare as the corpus grows. At the [100TB+ scale](https://www.braintrust.dev/blog/brainstore-benchmarks) where traditional phrase search degrades the most, there are far more segments to eliminate, so the win only gets larger.

In concrete numbers, moving from a unigram bloom filter to increasingly finely-tuned trigram bloom filters allowed for a search that eliminates 63 of 64 segments rather than 3 of 64 segments.

Shingle search is part of a workflow that makes segment elimination more effective in Brainstore across varying kinds of searches.

Bloom filters handle high-cardinality equality, and are used to search for things like request ids, session ids, and developer-provided identifiers, where a single token is already selective.

Shingle indexing handles phrase searches that commonly arise for agent debugging, where each token is common but the ordered terms are unique.

Phrase search is becoming more common as agents become more popular and debugging them becomes harder. Brainstore is able to handle these searches faster and cheaper than traditional databases that weren't built for agents. Since our customers build agents that handle real customer problems at meaningful scale, performance improvements like this can have a significant impact on their business.

We're constantly working on making Brainstore better, and are focusing on a few areas for improvement.

One focus is making aggregations over large ranges of data faster by building materialized views over common aggregations and optimizing our columnar storage format and columnar execution engine.

We're also continuing to improve the work described above, so our full-text search and filtering performance gets even better by optimizing the way we use the inverted index, especially around how it interacts with cold reads from object store.

All of it points at the same outcome. As agent data grows larger and colder, the searches teams rely on to debug stay fast, and for customers running agents against real problems at scale, staying fast is what keeps them moving.
