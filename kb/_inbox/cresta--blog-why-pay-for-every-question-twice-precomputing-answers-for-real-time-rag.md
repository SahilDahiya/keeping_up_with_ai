---
title: Why Pay for Every Question Twice? Precomputing Answers for Real-Time RAG
kind: blog
topic: null
subtopic: null
secondary_topics: []
summary: null
triage: null
skip_reason: null
source: cresta
url: https://cresta.com/blog/why-pay-for-every-question-twice-precomputing-answers-for-real-time-rag
author: Ethan Jiang
published: '2026-08-26'
fetched: '2026-08-31T06:13:05Z'
classifier: null
taxonomy_rev: 2
words: 1439
content_sha256: b9fb1f146573fd991107899eaf088846205960be054dc5105b96c501744ea9d8
---

# Why Pay for Every Question Twice? Precomputing Answers for Real-Time RAG

In a contact center, every second an agent waits for an AI-generated suggestion is a second the customer is waiting too. That makes latency one of the hardest constraints on any retrieval-augmented generation (RAG) system in production: stretch the pipeline and the agent moves on; cut corners and the answer suffers. For the past year, Cresta’s Knowledge Assist team has been working on a third option: **doing the expensive work ahead of time**.

The result is the **Precomputed Answer Engine (PAE)**, a system that serves precomputed, high-confidence answers for common questions and falls back to the full RAG pipeline when no match is found. In early production evaluations, PAE intercepts **a significant portion of incoming questions in under a second**, and the remaining traffic flows through unchanged.

But the harder problem isn’t just caching answers, it’s knowing *which* answers to cache, and keeping that cache aligned as both customer behavior and knowledge base content shift over time. This post is about how PAE was designed to do both.

## The Bottleneck: Paying for Every Question, Every Time

A standard Knowledge Assist request runs the full retrieve-rank-generate loop: searching an index, re-ranking results, assembling context for a large language model (LLM), generating an answer, and rewriting that answer to fit the live conversation. Each stage is necessary to handle the long tail of questions a contact center receives, but each stage also costs latency and tokens.

Two observations made us want to avoid paying that cost on every request:

1. **Quality is bounded by the latency budget.** Tighter latency forces smaller models and lighter processing. If we could move some of the work offline, we could afford richer pipelines for the answers we precompute, including:
  - Retrieving from a broader set of sources and reranking more candidates to improve both recall and precision
  - Reasoning across multiple documents to find the best consolidated answer
  - Addressing conflicts between sources [multiple-hop reasoning and conflict resolution not yet supported].
3. **A meaningful slice of production traffic is repetitive.** Customers ask  similar questions about cancellations, refunds, policies, and dozens of other recurring topics. Computing those answers from scratch every time is wasted work.

PAE is the system that takes those two observations seriously.

## What PAE Actually Serves

Rather than treating the knowledge base as a flat collection of chunks, PAE builds a curated index of question–answer pairs designed to match how end users actually think and ask questions.

The core challenge is anticipating the questions customers will ask—or are very likely to ask—before they arrive. PAE approaches this by anchoring question generation on multiple complementary angles, each providing a different lens into the same underlying information:

- **Behavioral anchors.** Questions mined from real historical conversations reveal patterns in how customers actually phrase their needs. These are the highest-value entries because they directly reflect production distribution.
- **Content anchors.** Questions and definitions lifted from the knowledge base itself, capturing what the documentation is explicitly designed to address.
- **Predictive anchors.** Questions generated against each piece of content to expand coverage, anticipating what customers might ask about topics the KB already covers but that haven’t appeared frequently in production yet.

Each anchor provides a different angle on the same information. A customer asking about refunds might phrase it as “How do I get my money back?”, “What’s your refund policy?”, or “Can I cancel and get a refund?”—all targeting the same underlying answer but from different entry points. By generating questions from multiple anchors, PAE increases the likelihood that when a real user question arrives, there’s already a precomputed answer waiting that matches their intent.

![](https://cdn.prod.website-files.com/67feba4d16c14d85f1696c4f/6a8f1998f68988e626e5ef4c_PAE_Diagrams_Deck%201.png)

*Figure 1: PAE generates questions from three complementary sources, each providing a different lens into the same information.*

## Smart Matching: Fast, Then Careful

Serving accuracy is where PAE earns its keep. Returning the wrong precomputed answer is worse than falling through to the full pipeline, so question matching combines lexical and semantic approaches in a staged process, each layer more expensive and more selective than the last:

**Lexical match.** If the incoming query matches a stored question verbatim (after normalization), return immediately. Zero overhead, handles canned questions.

**Semantic match.** For queries that don’t match exactly, PAE uses a two-stage filtering process:

1. **Embedding-based candidate retrieval** finds questions with similar meaning, catching paraphrases and minor rewordings.
2. **LLM-based verification** examines each candidate to confirm that the intent, entities, and qualifiers are identical, not just similar. A robust language model picker ensures that “*Is technical support included with the basic plan?* ” and “*Is technical support included with the premium plan?* ” don’t match just because they’re structurally similar; the qualifier difference matters. If no candidate passes this strict check, PAE returns no match and the request falls through to the full pipeline.

![](https://cdn.prod.website-files.com/67feba4d16c14d85f1696c4f/6a8f19b7f68988e626e5ff19_PAE_Diagrams_Deck%202.png)

*Figure 2: The two-stage matching process combines fast lexical lookup with careful semantic verification.*

## Manual Curation Alongside Automation

While PAE automates question generation and answer creation, contact center teams know their customers best. The system supports manual workflows at every stage:

**Manual Q&A creation.** Content admins can create question–answer pairs directly, bypassing automated generation when they know exactly what customers ask and how to answer it.

**Review and refinement.** Auto-generated pairs can be flagged for human review before going live, allowing admins to refine phrasing, adjust answers, or reject entries that don’t meet quality standards.

**Protected edits.** When a content admin improves an answer by hand, that edit is locked by default. Future automated refreshes park new generated candidates for review rather than silently overwriting curated work—the system assumes human judgment should win.

This hybrid approach means PAE scales through automation while preserving the precision and context that only domain experts can provide.

## Adapting to Drift: Usage and Content

Contact centers are not static. Customer behavior shifts — new products launch, policies change, seasonal questions spike. Knowledge base content evolves — articles are added, updated, deprecated. A precomputed index that doesn’t track these changes becomes stale fast.

PAE addresses both kinds of drift through continuous learning:

**Usage drift: learning what customers actually ask.** The system monitors production traffic to identify which questions are common, which are trending, and which have low match rates. High-frequency misses, like questions users ask repeatedly that PAE can’t answer, are flagged for priority inclusion in the next refresh. Over time, the index shifts toward the questions customers care about, not just the questions we predict they’ll ask.

**Content drift: staying aligned with the knowledge base.** When knowledge base articles are updated or new content is published, PAE re-generates affected Q&A pairs and evaluates whether existing answers are still accurate. Manual edits are protected by default; if a content admin has improved an answer by hand, the system parks the new generated candidate for review rather than silently overwriting curated work.

The result is an index that evolves with both sides of the equation: what users need, and what the knowledge base can deliver.

![](https://cdn.prod.website-files.com/67feba4d16c14d85f1696c4f/6a8f1d60ee959b2063dec8d6_PAE_Diagrams_Deck%203.png)

*Figure 3: PAE’s continuous learning loop adapts to both usage drift (customer behavior) and content drift (knowledge base updates).*

## What the Numbers Say

In a recent evaluation against production traffic:

- **Match rate: a substantial fraction of queries(~40%)** answered from cache, with the strongest signal coming from questions grounded in real prior conversations.
- **Average latency: ~0.7 seconds** for cache hits, well under the multi-second cost of the full pipeline.
- **Customer-rated answer quality:** On questions automatically detected from live Enterprise customer conversations, PAE-powered answers achieved**>80% strict pass rates** .

The takeaway: a meaningful share of production questions can be answered from cache, the answers are reliably on-target, and the remaining traffic flows through the existing pipeline with no degradation.

## What’s Next

Two capabilities will close the learning loop:

- **Mining questions and answers directly from production conversations** :  extracting high-quality Q&A pairs from live agent interactions to capture the most current and relevant customer inquiries and validated answers.
- **Surfacing knowledge gaps** : identifying patterns in unmatched queries to flag where the knowledge base needs new content or where existing documentation fails to address customer needs.

PAE started as a wager that most of the value in a knowledge assist system can be precomputed, and that the system can learn which parts to precompute by watching what users actually ask. The early production data says the wager is paying off, and these next steps will make that learning continuous.

Cresta engineers are rethinking production AI, from real-time RAG and intelligent retrieval to continuous learning and subsecond delivery. If you want to solve hard problems and turn ambitious ideas into measurable customer impact, [come build the future of human-centric AI with us](https://cresta.com/careers).
