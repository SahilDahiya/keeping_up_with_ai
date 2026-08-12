---
title: Fireworks AI
kind: blog
topic: null
subtopic: null
secondary_topics: []
summary: null
triage: null
skip_reason: null
source: fireworks
url: https://fireworks.ai/blog/deepseek-v3p1
author: null
published: '2025-08-26'
fetched: '2026-08-12T06:28:45Z'
classifier: null
taxonomy_rev: 2
words: 466
content_sha256: 98bb97ca2f7d483ff5a01d19a313b1bea5195391b4e4a047e228b6709bd2ebf1
---

# Fireworks AI

DeepSeek V3.1 is a major leap forward in open‑source LLMs. It introduces hybrid reasoning modes (“thinking” vs. “non‑thinking”), and reduces hallucinations by around **38%** compared to V3.

With enhanced tool integration and expanded multilingual capabilities across 100+ languages, V3.1 is optimized for real‑world, agent‑centric applications.

To truly leverage its power, especially in agentic workflows and long‑document analysis, you’ll benefit from experienced engineers integrating it with APIs, tool chains, and memory systems.

At its core, DeepSeek V3.1 expands on DeepSeek V3’s architecture with several major enhancements:

- •**Hybrid Reasoning Modes** : Toggle between “thinking” (chain‑of‑thought) and “non‑thinking” (rapid reply) using chat templates.
- •**Massive Context Capacity** : Standard 128K‑token windows, trained with 10× more data for 32K context and 3.3× more tokens in the 128K phase than V3.
- •**Lower Hallucination Rates** : About**38% fewer hallucinations** , yielding more factually consistent outputs.
- •**Enhanced Tool & Agent Support** : Sharper API integration, better memory across tool chains, and more reliable function calling.
- •**Expanded Multilingual Support** : Gains across 100+ languages, with standout performance in Asian and low‑resource languages.
- •**Optimized Architecture** : Sparse Mixture‑of‑Experts with ~685B parameters (37B active), using FP8 microscaling for performance gains.

DeepSeek V3.1 ships with flexible usage modes tailored for varied tasks:

- •**Thinking Mode** : Activates chain‑of‑thought reasoning ideal for math, coding, complex multi‑step logic.
- •**Non‑Thinking Mode** : Optimized for low‑latency Q&A, summarization, and task completion.

Switch modes easily by selecting suitable chat templates in API calls or orchestration layers.

Here’s a clean example demonstrating how you'd call DeepSeek V3.1 in “thinking mode” via Fireworks API:

12345678910111213141516171819202122


This makes it straightforward to toggle reasoning behavior per request.

In head‑to‑head benchmarks, DeepSeek V3.1 shows substantial improvement:

- •**+43%** boost in multi‑step reasoning (math, logic, code) over V3
- •Stable coherence across contexts
- •**38% fewer hallucinations** , enabling more reliable enterprise usage
- •Stronger multilingual accuracy, especially in Asian and low‑resource languages

These gains stem from smarter instruction tuning, expanded training corpora, and better context handling across phases.

DeepSeek V3.1 is designed for impactful use cases:

- •**Smart Research Copilots** that analyze entire scientific papers or books in context
- •**Enterprise Agent Workflows** coordinating APIs, memory, and tool chains
- •**Code Companions** capable of multistep logic, cross-file reasoning, and debugging
- •**Global Conversational Assistants** supporting over 100 languages with real accuracy
- •**Knowledge‑Dense Longform Tools** , e.g. summarizing legal, medical, or financial documents end‑to‑end

DeepSeek V3.1 is more than just an update, it’s a redefinition of open‑source LLM capabilities.

It enables:

- •Controlled, hybrid reasoning
- •Native million‑token memory
- •Reliable agentic and tool workflows
- •Reliable, multilingual communication

For teams building real-world, high-complexity AI applications, especially those involving reasoning, long context, or multilingual agents- DeepSeek V3.1 offers both flexibility and power at an open frontier.

Try it now on Fireworks:
