---
title: 'Meet Linnaeus and Darwin: Search models that drive higher resolution rates'
topic: rag-retrieval
subtopic: search
secondary_topics:
- models/reasoning
summary: Introduces Sierra search models for improving support-agent resolution rates
  through better knowledge retrieval and answer grounding.
source: sierra
url: https://sierra.ai/blog/meet-linnaeus-and-darwin-the-sierra-search-team
author: Ola Zytek; Pedram Razavi; Alex Avery; Colin VanLang; Ben Dong
published: '2026-05-12'
fetched: '2026-07-11T03:51:09Z'
classifier: codex
taxonomy_rev: 1
words: 838
content_sha256: 9ef7a681024c7edc356777f0bd384559a54a16250788cb217e851917e826af84
---

# Meet Linnaeus and Darwin: Search models that drive higher resolution rates

# Meet Linnaeus and Darwin: Search models that drive higher resolution rates

For most customer queries, there’s a goal behind the question. When someone asks, “Can I cancel my order?”, what they really want to know is: will I get a refund, how much will it be, and what do I need to do next? Most knowledge base search is built to answer the immediate question. But great customer experiences address the goal behind it.

Search systems are often optimized for accuracy and relevance at the level of a single response. The result is answers that are correct, but don’t necessarily help resolve the issue. At Sierra, we’ve rebuilt search so agents have everything they need to fully solve the problem. Our purpose-built retrieval and reranking models outperform off-the-shelf ones, driving up to 16 percentage point improvements in resolution rates.

**Hundreds of millions of searches a year**

Agents built on Sierra perform over two million searches a day across knowledge bases. Each search is about more than finding a single right answer. It’s about retrieving the information needed to move from conversation to resolution: policies, edge cases, and next steps.

Consider the following conversation:

Customer:Hey, I want to check on my contact lenses. My name is Maya Chen.

Agent:I'm sorry, I'm not finding that name in our system.

Customer:Oh I got married and changed my name recently, it's probably under Maya Anderson.

Agent:OK I’ve found it…

Customer:Ok great, so where can I pick it up?

A traditional search system might return articles for prescription pickup locations. But Maya also needs to know opening hours and how name mismatches are handled at pickup. Sierra’s search is designed around understanding the broader problem — not just answering the immediate question — so agents have the context they need to resolve the issue.

**Measuring what matters**

We evaluate search across four dimensions — speed, cost, quality, and outcomes. Each is tied to how well the agent can drive to an outcome:

- **Speed**— how quickly can we retrieve useful context and keep conversations flowing? We’ve reduced P90 latency by more than 75%.
- **Cost**— can we do this efficiently at scale? Search costs are down more than 75%.
- **Quality**— are we retrieving the right set of documents to enable resolution? We’ve brought recall@30 averages up to around 95%.
- **Outcomes**— do improvements in retrieval actually lead to better customer experiences? We’ve driven gains of up to 16 percentage points in resolution rates.

The result is fast, accurate, and outcome-driven customer interactions.

**Customer experience specific search**

This requires a different definition of relevance — one grounded in resolution.

Back to the “Can I cancel my order?” example. A general-purpose search system might return the cancellation policy. But resolving the issue requires more: refund timelines, restocking rules, and exceptions for loyalty members.

In customer service, success looks like:

- Returning information that enables policy-compliant decisions
- Anticipating downstream steps
- Avoiding common resolution dead-ends
- Providing the right context for escalation

By redefining retrieval in this way, informed by real conversations, we can systematically improve outcomes.

**The models powering Sierra’s search**

Our system is built on two custom models: Linnaeus for retrieval, and Darwin for reranking. Together, they are designed not just to find relevant information, but to assemble what’s needed to solve the problem.

**Linnaeus: Transcript-Aware Retrieval for Customer Service**

Traditional search pipelines generate a query, embed it, and retrieve similar documents. This adds latency and often compresses the conversation in ways that miss the end goal behind the question.

Linnaeus operates directly on full conversations when appropriate. This preserves nuance — like distinguishing between contact lenses and other prescriptions — and removes the need for a separate query generation step. Off-the-shelf embedding models aren't designed for this. They're typically optimized for short queries, not multi-turn conversations. Sierra’s is purpose-built for conversational transcripts and evaluated against tens of thousands of real-world conversations.

More importantly, it retrieves not just the most relevant document, but the set of information needed to move the conversation forward: policies, edge cases, and next steps.

This shift improves recall (recall@5 up 20%, recall@30 at ~95%) while reducing latency by up to ~800ms per search.

**Darwin: Customer-Experience Aware Reranking**

Retrieval casts a wide net. Darwin selects what will actually help resolve the issue.

Frontier LLMs can do this well, but are too slow and expensive at scale. Smaller models are faster, but often miss context that requires reasoning.

Darwin is purpose-built for customer experiences, identifying both directly and indirectly relevant information — like surfacing profile settings when a customer asks about changing their name. This delivers precision and efficiency, reducing cost and latency while improving outcomes.

**From Retrieval to Resolution**

Together, Linnaeus and Darwin form a system designed not just to answer questions, but to solve the goal behind them.

Across thousands of real-world conversations, this approach leads to faster responses, better answers, and higher resolution rates. Because the goal customers have isn’t to get an answer to their question — but to resolve the issue behind it.
