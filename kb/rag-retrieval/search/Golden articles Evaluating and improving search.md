---
title: 'Golden articles: Evaluating and improving search'
topic: rag-retrieval
subtopic: search
secondary_topics:
- evals-observability/evaluation
summary: Covers golden-article evaluation for search quality and how retrieval systems
  can be measured and improved for support agents.
source: sierra
url: https://sierra.ai/blog/evaluating-and-improving-search
author: Ola Zytek; Pedram Razavi; Alex Avery; Ben Dong; Colin VanLang
published: '2026-05-12'
fetched: '2026-07-11T03:51:05Z'
classifier: codex
taxonomy_rev: 1
words: 664
content_sha256: ee268e319907218c1320e62f709a0de9faf48cc6b2794c52eddd2d1cb0a53478
---

# Golden articles: Evaluating and improving search

# Golden articles: Evaluating and improving search

Last week, we [explained](https://sierra.ai/blog/meet-linnaeus-and-darwin-the-sierra-search-team) how Linnaeus and Darwin — Sierra’s retrieval and reranking models — equip agents to solve problems versus just answer questions. But building a strong model is only half the challenge. You need to know they’re effective in practice. So we’ve developed an evaluation system that measures search quality against real conversations on a daily basis, and uses those signals to ensure it gets better over time.

## Real-time, grounded, golden datasets

You can’t measure search quality against static test data because knowledge bases change, new policies get introduced, and customer issues evolve. So for every organization we work with, we sample thousands of anonymized examples from the previous day’s conversations — the points where an agent searched its knowledge base.

For every search call, an automated pipeline determines which articles would have best resolved the customer’s issue at that point in the conversation. We then use a multi-stage pipeline of frontier LLMs to filter and rank those articles for that conversation, identifying the ideal set. The set includes both articles that directly answer the customer’s question and others that provide essential background or supporting information. This produces a high-quality “golden dataset” for each organization — a clear benchmark for what good search results should look like.

We then compare these “golden” articles to what the agent actually retrieved during the conversation, creating daily retrieval metrics for each customer. We use industry-standard retrieval metrics, such as recall (did we find everything needed?), precision (did we avoid cluttering the agent with noise?), and nDCG (which stands for normalized discounted cumulative gain, or did we correctly order articles by importance?) — to identify exactly where search works well and where it falls short.

## From measurement to improvement

Measurement is a means to an end — Sierra’s evaluation signals feed a continuous improvement loop.

For each customer, we look at specific conversations where the system failed to find the right articles. These examples help us spot patterns — like a recently reorganized knowledge base or gaps in coverage for certain types of issues. From there, it’s clear what needs to change, whether that’s improving the model, adjusting the search settings, or reorganizing the knowledge base.

In one case, we identified a company whose system was worse than others at finding the right articles. The issue turned out to be the way their knowledge base was organized — content from different brands wasn’t clearly separated, so the system was pulling in irrelevant articles. After reorganizing the content to better separate those brands, search accuracy improved immediately.

This evaluation system also lets us track the impact of platform changes in near real time. After we released our retrieval and reranking models, recall improved day by day across customers. Recall measures how much relevant information the system retrieves. Those gains also correlated with resolution-rate improvements of up to 16 percentage points.

## We're just getting started

Better retrieval doesn't just return better articles — it determines whether a conversation is successfully resolved. When a customer asks where to pick up their prescription, retrieving only the pickup locations answers the question but doesn't solve the problem. Retrieving pickup locations alongside opening hours and other potentially important considerations from context (for example, can someone pick up the prescription on my behalf) gives the agent everything it needs to resolve the issue in a single conversation.

We track this as resolution rate: the percentage of conversations fully handled by the agent without the need to hand over to a customer support associate. For high-volume agents, even modest retrieval gains translate to thousands of additional resolved conversations a year, and in several cases, measurable improvements in customer sentiment.

Search for an AI agent isn’t something you build once. By defining “good search” in terms of resolution, generating rigorous evaluation data from real conversations every day, and feeding those signals back into the system, we’ve built a system that reliably gets better over time.
