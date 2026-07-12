---
title: Grounding Reality – How Cresta Tackles LLM Hallucinations in Enterprise AI
topic: rag-retrieval
subtopic: pipelines
secondary_topics:
- evals-observability/evaluation
summary: Explains grounding strategies for reducing hallucinations in enterprise AI
  systems, with emphasis on knowledge and evaluation loops.
source: cresta
url: https://cresta.com/blog/grounding-reality---how-cresta-tackles-llm-hallucinations-in-enterprise-ai
author: Navjot Matharu
published: '2025-08-06'
fetched: '2026-07-11T03:58:35Z'
classifier: codex
taxonomy_rev: 1
words: 1271
content_sha256: 751b0df5e211bac12e296421d56a6dadb19405051f57190c38b02cd436d0cd9e
---

# Grounding Reality – How Cresta Tackles LLM Hallucinations in Enterprise AI

**Introduction**

Large Language Models (LLMs) are known to hallucinate, generating plausible yet inaccurate outputs that are not grounded in the input, reference materials, or real-world knowledge. In enterprise applications where AI supports critical business decisions, LLMs’ hallucinations can be particularly detrimental.

Although hallucination mitigation is recognized as essential, not all AI products in the market *deliberately incorporate hallucination mitigation as part of the solution*. 

In this article, **we introduce the six pillars that form the foundation of Cresta's approach to “hallucination mitigation by design”**, and illustrate their practical application through detailed examples from Cresta [AI Analyst](https://cresta.com/cresta-ai-analyst).

![](https://cdn.prod.website-files.com/67feba4d16c14d85f1696c4f/68929222197cc4423c5b0684_blog-ground-reality-illus-1-1.avif)

## Cresta’s approach to mitigating hallucinations

#### 1. Automated hallucination detection & model building process

When developing an LLM-driven AI feature, we begin by clearly defining critical performance metrics, placing primary emphasis on hallucination rates. To accurately measure these metrics, we create automated verifiers (aligned LLM judges) through an iterative refinement process to ensure they precisely reflect our metric definitions. These automated verifiers are aligned: i.e., tailored to the unique needs and requirements of contact center conversations. To mitigate the risk of hallucinations, we then utilize these automated verifiers to guide machine learning strategies, including:

- Prompt tuning and context engineering (e.g., in-context learning, chain-of-thought and self-critique)
- Response constraints (e.g., template-responses and fallback-refusal-clauses)
- Model selection & hyperparameter optimizations

#### 2. Proprietary LLM-finetuned RAG models

Our proprietary retrieval-augmented generation (RAG) models specialize in grounding answers to factual information present in customer’s knowledge bases and other reference materials, preventing hallucinations which GenAI models are known to exhibit. We achieve this via a proprietary finetuning dataset collection method, which ensures that the model generates grounded responses based on customer-specific knowledge and context, dramatically reducing hallucinations and enhancing response accuracy.

#### 3. Teaching LLMs to abstain

Hallucinations often occur when LLMs are forced to generate responses without access to relevant information, knowledge, or context. To mitigate this, we explicitly tune our LLMs to acknowledge when they cannot find a reliable or relevant answer. Rather than defaulting to confident-sounding but incorrect responses, our models can abstain when they lack sufficient grounding to provide a truthful answer, significantly reducing the risk of hallucinations. This refusal mechanism is embedded in the models through the above proprietary LLM-finetuning pipeline, prompt engineering, output constraints, and fallback logic.

#### 4. Attribution mechanism

We combine evidence citation with a proprietary attribution mechanism to ensure that cited evidence is grounded in reference materials. Most attribution solutions ask the LLM to also generate evidence alongside a generated response – but how does one know that the generated evidence is also not hallucinated? We have a proprietary technique where we can make sure the evidence generation is reliable. This not only helps avoid hallucinations, but also enables traceability of the response output, guiding us to understand where a response comes from and how we can improve our models in the future.

#### 5. Human-in-the-loop design

Our products are carefully designed to leverage human inputs when needed. Before, during, and after development, domain experts are involved in identifying hallucinations within product-specific contexts. In real-time applications, our generative AI systems involve humans when their input is needed. For example, [Cresta AI Analyst](https://cresta.com/cresta-ai-analyst) will ask the user clarifying questions if their request is underspecified and [Cresta AI Agent](https://cresta.com/ai-agent) will transfer the call to a human agent when it detects that it is not equipped to resolve the customer’s issue.

#### 6. Robust guardrails and real-time moderation

We employ AI guardrails and real-time moderation tools that proactively identify and mitigate undesired outputs, including hallucinations. These guardrails operate continuously, leveraging sophisticated language understanding and contextual analysis to ensure strict adherence to the required content guidelines for each customer, significantly reducing the risk of inappropriate, misleading, or off-topic responses.

## Deep Dive with Cresta AI Analyst

Cresta [AI Analyst](https://cresta.com/cresta-ai-analyst) is an agentic system that unlocks the wealth of information locked in contact center conversations. It answers natural language questions about the content of the conversations and provides deep insights structured as easy-to-understand reports.

Customers use these insights (answers to questions such as “Why are customers choosing product X over product Y?”) to make critical business decisions, so it is especially important to ensure that AI Analyst’s insights are grounded in the actual contact center conversations and not hallucinated responses.

At the same time, if implemented naively, products like AI Analyst are especially prone to hallucinations. To illustrate this, here is an extreme example. The following is a report, which could have come from an AI Analyst-like product, summarizing the top reasons why customers of Luxe Emporium are choosing to buy Veloria brand products rather than Cortellini, along with the percentage of conversations they occur in:

Looks great, right? Even the percentages add up to 100%. The only problem? It is completely hallucinated. Luxe Emporium, Veloria and Cortellini don’t exist, and the report was produced by ChatGPT in response to the isolated prompt:

Naive implementations of AI Analyst-like products similarly pose questions like this to an LLM, while attaching a sample of contact center conversations. **But including conversations in the input alongside the question is no guarantee that the output will be fully grounded in these conversations.** In fact, it will most likely be an inextricable mix of correct information and hallucinations, which can be especially misleading.

#### Why does this happen?

A primary source of hallucinations when analyzing contact center conversations are conversations that don’t provide an answer to the question that the user is posing. Let’s say that one of the conversations sampled for analysis was the following one:

Given a conversation like this and the question:

… an LLM instructed to provide a succinct answer to the question will usually answer something like:

… which is a complete fabrication. The topic of the conversation was promotion eligibility, but the customer already bought both Veloria and Cortellini products and didn’t express any preferences regarding them. But LLMs are trained to try very hard to answer the question they are given, so they latch on to the topic of promotion eligibility in this case and falsely output it as the requested reason.

#### So how did we address this?

First of all, we used our [automated hallucination detection system](https://cresta.com#one) to detect hallucinations in the product both online and during offline evaluations. The hallucination detector is one instance of Cresta’s *aligned LLM judges*, i.e. LLM judges that have been systematically aligned to ensure that they accurately reflect human preferences and definitions (in this case, what exactly constitutes a hallucination in the domain of conversation analysis).

It quickly became apparent that conversations not containing the information to answer the user’s question were a dominant source of hallucinations. To address this, we [taught AI Analyst to refuse. ](https://cresta.com#three)Specifically, we taught it to recognize which conversations contained relevant information and only used these conversations in the analysis. We additionally developed another aligned LLM judge to determine whether the AI Analyst correctly identified a conversation as being relevant or not.

Finally, we didn’t just take the LLM’s word for it. We made it provide evidence for the claims it made and then used our [proprietary attribution mechanism](https://cresta.com#four) to match this evidence to specific points in the conversation, discarding any outputs that could not be matched. This not only reduced the hallucinations by discarding the most likely instances, but also gave the user a way to easily verify that the claims were factual.

## Learn more…

Learn more about our journey aligning LLM judges for hallucination detection in contact center conversation analysis, in our paper [FECT: Factuality Evaluation of Interpretive AI-Generated Claims in Contact Center Conversation Transcripts](http://arxiv.org/abs/2508.00889) accepted at [KDD 2025](https://kdd2025.kdd.org/), and the associated [benchmark dataset](https://github.com/cresta/fect/) we open-sourced.
