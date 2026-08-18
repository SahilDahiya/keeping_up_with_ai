---
title: Baseten delivers open-source inference for You.com
kind: blog
topic: null
subtopic: null
secondary_topics: []
summary: null
triage: null
skip_reason: null
source: baseten
url: https://www.baseten.co/blog/baseten-delivers-open-source-inference-for-youcom/
author: Marylise Tauzia
published: '2026-08-13'
fetched: '2026-08-18T06:07:56Z'
classifier: null
taxonomy_rev: 2
words: 699
content_sha256: 16a7772ce02de765b04c4d6bb6fc42d07843787a06d0dd300fbed9a673310099
---

# Baseten delivers open-source inference for You.com

![Baseten and You.com partnership](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1786555223-baseten-ydc-blog.png%3Fauto%3Dformat%26fit%3Dcrop%26h%3D630%26w%3D1200&w=3840&q=100)

You.com built the Answer API to complete its Web Search API portfolio. It delivers a synthesized, fact-checked answer with verified citations from a single query. It can hit 93.48% accuracy on Simple QA at a 2.67-second p50 latency and $5 per 1,000 calls. Baseten is proud to power the inference behind You.com's search and answer stack and give its customers access to frontier-level answer quality without having to route every query to a frontier model, which significantly improves cost and latency.

[You.com](http://you.com/) built its business on the premise that LLMs are only as good as the information they can access, and most of them can't reliably access the live web. Their goal since day 1 has been to close that gap and give agents and chatbots real-time, cited, hallucination-resistant answers rather than information returned from stale training data.

You.com, which operates at an impressive scale and processes double-digit millions of queries a day, started to run into an inference problem. As every query touches a chain of models before an answer ever reaches the user, each of them adds its own latency budget, creating a serious challenge to hold this chain together at enterprise scale. So their infrastructure team started to look into solutions that could help them pair open-weight inference with their web search stack and see if it could become a viable substitute for routing everything to closed frontier APIs and ideally, at a fraction of the cost. It is what led them to look into the Baseten Inference Platform and work with our team on building a solution.

"We think open-weight inference plus web search is a powerful alternative to routing everything through frontier model providers at a fraction of the price for our developers." - Saahil Jain, CTO, You.com

## Baseten’s solution

Baseten powers the inference layer behind several stages of You.com's search and answer pipeline by running open-source and fine-tuned models across dedicated, multi-region deployments.

On the retrieval and understanding side, You.com runs named entity recognition, embeddings, query annotation, query expansion, and intent prediction models on Baseten. These are deployed across multiple regions so requests can be served close to where they originate.

On the generation side, You.com uses Baseten to serve a variety of open-source LLMs, including the newest ones like GLM-5.2 and Kimi K3, at a Pareto-efficient frontier across accuracy and cost. These models are served through Baseten's inference platform and do the synthesis work behind the new Answers API, turning retrieved passages into a cited, verified answer instead of just a list of links.

Baseten’s key platform capabilities that You.com relies on include:

- Dedicated, multi-region deployments
- Baseten Embedding Inference (BEI) for high-throughput embedding and reranking workloads
- Truss for packaging and deploying fine-tuned and custom models
- Zero Data Retention (ZDR) for enterprise compliance requirements
- Baseten Inference for frontier-grade open source LLMs like GLM-5.2 and Kimi K3

## The results

The You.com Answer API is now running in production using the Baseten infrastructure. They achieved ~60% latency improvement and a 50% cost reduction compared to the prior configuration, with an accuracy rate in line with that of proprietary models.

On the reranking side, moving to Baseten cut response times on long web pages from 3-4 seconds with the previous solution to well under a second, which directly affects how quickly an Answer API response can come back to the caller.

The throughline across both workloads is that not every step in an AI pipeline needs a frontier model attached to it. Entity recognition, reranking, and query understanding all need to be fast and cost-effective. And the synthesis step needs to be accurate and well-cited. Open-source models built on production-ready infrastructure can hit both bars, which is what lets You.com offer frontier-level answer quality for a fraction of what it costs to run the same volume of queries through a closed frontier model.

## Get started

[You.com's Answer API](https://you.com/docs/guides/answer?utm_source=partner-baseten&utm_medium=content-syndication&utm_campaign=2026-08-docs) is live today. If you're building an agent, chatbot, or research tool that needs answers from the live web, it's worth a look. And if you're evaluating open-source models for your own inference stack, [talk to us](https://www.baseten.co/talk-to-us/) about what Baseten can do for your production workloads.
