---
title: 'When the Call Runs Too Long: Modeling Outcomes for Long Conversations'
topic: models
subtopic: reasoning
secondary_topics:
- evals-observability/evaluation
summary: Discusses modeling outcomes for long conversations, including challenges
  around sequence length and delayed success signals.
source: cresta
url: https://cresta.com/blog/when-the-call-runs-too-long-modeling-outcomes-for-long-conversations
author: Parkavi Prabaharan
published: '2026-03-05'
fetched: '2026-07-11T04:03:49Z'
classifier: codex
taxonomy_rev: 1
words: 1218
content_sha256: 7f5a35a22aff600ec789ba8f06d71f1da0970c02634d07e4fd79408a4cee540f
---

# When the Call Runs Too Long: Modeling Outcomes for Long Conversations

Contact center conversations are often long, messy, and outcome-driven. A single call can span from tens of minutes to even an hour or longer with multiple topics and shifting intents - from discovery to troubleshooting to sale.

Yet many of the most valuable modeling tasks in this domain are defined not at the turn level - where predictions are made per utterance - but at the conversation level: Was the sale closed? Was the issue resolved? Did the customer leave satisfied? Was a potential churn retained?

In practice, the signal for these outcomes is often sparse and unevenly distributed. Looking for a single message or a brief moment that determines the outcome can feel like searching for a needle in a haystack. Context windows are finite, and even when a full conversation technically fits, naively feeding the entire transcript into a model often leads to death by context: irrelevant details dilute signal, critical moments get buried, and performance degrades rather than improves.

In real-world systems, there is no one-size-fits-all solution. Different outcome types exhibit different structural properties, and effective modeling strategies depend on where the signal appears, how much context is required, and how precise the outcome needs to be.

In this post, we discuss four practical approaches for modeling outcomes on long conversations, each suited to different use cases and constraints.

We organize the approaches roughly from simplest to most complex:

- **Simple Truncation**
- **Chunking**- Simple Chunking
- Running Summaries

- **Drivers + Truncation**
- **Dynamic Retrieval**

**Simple Truncation**

Simple truncation is the most straightforward approach—and in some cases, surprisingly effective.

If the outcome of interest typically occurs in a predictable part of the conversation, we can often get away with truncating the transcript to the top or bottom x turns (or characters). For example, modeling call reasons or caller profiles often relies heavily on the opening of the conversation, while sales outcomes are frequently indicated near the end.

However, truncation assumes structural regularity, and real conversations are rarely perfectly structured. Connectivity issues might consume the opening minutes of a call, causing the call reason to appear later than expected. Post-sale support requests may follow a completed purchase, pushing the sale signal earlier than the truncation window. These edge cases can lead to systematic misses, especially as conversations grow longer and more variable. Sales outcome models utilizing truncation, currently deployed to several customers, consistently achieve strong performance, with an average F1 score of approximately 0.88 and 92% accuracy.

![](https://cdn.prod.website-files.com/67feba4d16c14d85f1696c4f/69a8aac36516e7a4e1712b64_blog-call-runs-long-figure-1-1.png)

**Chunking**

When conversations are too long on average and the position of the relevant signal is unclear—but full conversational context is not strictly required—chunking becomes a natural next step.

**Simple Chunking**

In simple chunking, the conversation is split into overlapping chunks, each processed independently, and the results are aggregated across chunks. This approach works well for tasks like entity extraction or detecting compliance statements, where the outcome can occur anywhere in the conversation and is not strongly dependent on prior context.

However, if multiple candidate entities appear across chunks, the model lacks the context needed to decide which one is correct. For example, a customer may cancel one booking and create a new one in the same call. Without broader conversational context, it becomes difficult to determine which booking ID should be surfaced as the final outcome.

![](https://cdn.prod.website-files.com/67feba4d16c14d85f1696c4f/69a8ce62728b4518c546f5ba_blog-call-runs-long-figure-2-1.png)

**Running Summaries**

To address the lack of context, chunking can be augmented with a running summary. In this setup, a small portion of the model’s context window is reserved for a rolling summary that is passed forward across chunks. This allows the model to maintain state across the conversation while still operating within fixed context limits.

Running summaries work reasonably well for entity extraction tasks that require limited contextual grounding - such as distinguishing whether a booking ID corresponds to a cancellation, upgrade, or new purchase. However, they struggle with more nuanced outcomes. Summary length constraints often force the model to discard early but critical context.

For instance, a “booking made” outcome may rely on understanding what the customer intended to purchase early in the call. Later signals like payments or add-ons (e.g., drink packages or upgrades) can generate false positives if the original intent has been lost through repeated summary roll-ups. In such cases, performance can degrade - sometimes even below that of simple truncation. We have been able to achieve 95%+ accuracy on certain sales outcome models using the chunking approaches with knowledge distillation.

![](https://cdn.prod.website-files.com/67feba4d16c14d85f1696c4f/69a8d1edad152e58350b7363_blog-call-runs-long-figure-3-1.png)

**Drivers + Truncation**

Many conversation-level outcomes are fundamentally comparative: what the customer wanted versus what actually happened by the end of the call.

Customer support resolution is a good example. A customer may call about one primary issue, discuss several secondary topics, and end the call with partial or full resolution. Simply truncating the end of the conversation loses the initial intent, while truncating the beginning misses the resolution.

A common and effective pattern is to extract drivers—such as call reason or customer intent—from the beginning of the conversation, and concatenate them with a truncated tail of the conversation. This allows the model to explicitly reason about whether the original issue was addressed, without needing the full transcript.

This approach is particularly effective for outcome modeling tasks that depend on aligning intent with resolution, and often outperforms both naive truncation and summary-based approaches. On a recent customer QA on our resolution model utilizing this approach, the model scored a 95% accuracy and surfaced insights about their call center performance they were previously unaware of.

Resolution models combined with topics can help companies learn about the areas of assistance the agents currently struggle with and can generate actionable insights to leadership on what needs to change to improve customer experience and First Call Resolution (FCR).

![](https://cdn.prod.website-files.com/67feba4d16c14d85f1696c4f/69a8d23b92ed49a669471a81_blog-call-runs-long-figure-4-1.png)

**Dynamic Retrieval**

Some outcomes require precise extraction rather than classification: the number of additional phone lines added, prescriptions filled, or the amount paid for a purchase. In these cases, the value of interest may not even exist in the transcript—or may appear only in specific topical segments.

Dynamic retrieval approaches address this by selectively identifying the most relevant parts of the conversation before modeling the outcome. The conversation is first split into chunks or turns and embedded. Given a query (e.g., “additional lines added” or “total amount paid”), similarity search is used to identify the most relevant segments. The outcome is then extracted from these segments using truncation or chunk-level modeling. Retrieval-based methods are especially useful when the outcome is neither binary nor general-purpose, and when processing the entire conversation would be both inefficient and noisy.

![](https://cdn.prod.website-files.com/67feba4d16c14d85f1696c4f/69a8d2983ac58ccf00bb8bab_blog-call-runs-long-figure-5-1.png)

**Model Performance**

Recently deployed models show that live performance evaluated by customer QA teams is in line with or surpasses Cresta's rigorous offline evaluation, which upsamples edge cases for testing. Our Out-of-Box (OOB) models are highly effective, typically covering 80-90% of use cases. The remaining cases are addressed by refining hyperparameters or prompts, all while preserving the core conversation strategy.

![](https://cdn.prod.website-files.com/67feba4d16c14d85f1696c4f/69a8d2ba96bfa72f01d47498_blog-call-runs-long-figure-6-1.png)

Long conversations force us to confront a key reality: accuracy does not come from seeing everything, but from modeling what matters. The most effective outcome models are those that respect conversational structure, selectively preserve context, and align modeling strategy with the nature of the outcome itself - and when the approach aligns with the requirements of the use case.

To see Cresta in action, [request your personalized demo today](https://cresta.com/request-a-demo).
