---
title: 'Atropos Health’s Arjun Mukerji, PhD, Explains RWESummary: A Framework and
  Test for Choosing LLMs to Summarize Real-World Evidence (RWE) Studies'
topic: evals-observability
subtopic: evaluation
secondary_topics:
- models/benchmarks
summary: Summarizes RWESummary, a healthcare-focused framework for choosing LLMs to
  summarize real-world evidence studies safely and reliably.
source: arize
url: https://arize.com/blog/atropos-healths-arjun-mukerji-phd-explains-rwesummary-a-framework-and-test-for-choosing-llms-to-summarize-real-world-evidence-rwe-studies/
author: Jason Lopatecki
published: '2025-09-19'
fetched: '2026-07-11T04:53:24Z'
classifier: codex
taxonomy_rev: 1
words: 346
content_sha256: a491086b089e7fbedb30962142f329c943176284d1b4cb7291318bcb574c27ba
---

# Atropos Health’s Arjun Mukerji, PhD, Explains RWESummary: A Framework and Test for Choosing LLMs to Summarize Real-World Evidence (RWE) Studies

Large language models are increasingly used to turn complex study output into plain-English summaries. But how do we know which models are safest and most reliable for healthcare?

In this most recent community AI research paper reading, Arjun Mukerji, PhD – Staff Data Scientist at Atropos Health – walks us through RWESummary, a new benchmark designed to evaluate LLMs on summarizing real-world evidence from structured study output — an important but often under-tested scenario compared to the typical “summarize this PDF” task.

## Watch

## Listen

## Highlights

### Why medicine is a special (and high-stakes) domain

*Mukerji*: “The medical field is one of the highest-stakes applications of AI—especially in real-world evidence. It’s very important to get things right, and approaches that work elsewhere don’t always translate to medicine.”

### The “evidence gap” & the role of RWE

*Mukerji*: “Only a fraction of daily medical decisions are backed by high-quality evidence—the ‘evidence gap.’ RWE complements clinical trials by covering larger, more varied cohorts that trials often exclude.”

### What RWESummary actually tests

*Mukerji*: “Our task isn’t ‘dump a full paper into an LLM.’ We supply structured study inputs—question, PICOT, outcomes, effect sizes—and ask for a plain-English summary. Current benchmarks rarely test this scenario.”

### The three mission-critical evals

*Mukerji*: “We empirically chose three evaluations that matter most in production: getting the **direction of effect** right, reporting **numbers accurately**, and **completeness**. Direction of effect is the single most important.”

### Why direction of effect is weighted so heavily

*Mukerj*i: “If you could fix only one class of errors, fix **direction of effect**. Saying Treatment X is better than Y when it’s actually the reverse is the worst possible mistake.”

### Results, speed, and trade-offs

*Mukerji*: “No model wins across the board. Gemini 2.5 led overall on direction and numbers; Gemini 2.0 Flash was the clear winner on latency. In production, inference time matters.”

### Robust evals essential

*Mukerji*: “Given the stakes, you need robust evals and a human-in-the-loop. AI can make serious mistakes—like reversing an effect—so health workflows must be designed for safety from the ground up.”
