---
title: Improving voice performance with post-training
topic: models
subtopic: fine-tuning
secondary_topics: []
summary: Describes post-training techniques for improving voice model performance
  and agent interaction quality.
source: sierra
url: https://sierra.ai/blog/voice-post-training
author: Ben Shi; Keshav Dhandhania; Dongxu Zhou
published: '2026-05-12'
fetched: '2026-07-11T03:51:56Z'
classifier: codex
taxonomy_rev: 1
words: 534
content_sha256: dd7843a0ca02b395da30737df012ba30db270bda2e4e0208763b58204f363771
---

# Improving voice performance with post-training

# Improving voice performance with post-training

At Sierra, we’re big believers in using AI to improve AI — constantly teaching our agents to communicate more clearly, more concisely, and more effectively. And one of the tools we use to make this happen is post-training.

## Why post-training?

When people think about improving AI agents, they often think of *prompting: *writing clever instructions to guide the agent’s behavior. Prompting is fast and flexible, but it has limits.

With post-training, we can go a step further. Instead of just asking the agent to behave a certain way, we actually teach it new patterns. Post-training allows us to instill qualities that prompts alone can’t reliably enforce: things like conversational flow, tone, or voice clarity. In other words: prompting sets the rules, but post-training builds the instincts.

## Improving voice quality with post-training

Recently, we focused on improving voice script quality that powers real-time interactions. We trained a custom model to generate user-facing responses, with four key goals in mind:

- **Non-repetitiveness:**Avoiding loops or echoes in phrasing.
- **Conciseness:**Saying what’s needed, no more.
- **Clarity:**Keeping responses easy to follow.
- **Humanness:**Sounding natural, not robotic.

## Internal evaluations

Improving an agent’s voice isn’t just subjective — we wanted measurable proof. To validate the quality gains, we used a two-step evaluation process:

### Automated evaluation

First, we built a model-based judge to compare the fine-tuned system against the base model. The fine-tuned version came out ahead in the majority of comparisons, showing clear improvements in conversational quality.

### Human review

We then had human evaluators independently review the same outputs. Their judgments strongly agreed with the automated results, confirming that the improvements were both real and meaningful.

## What we found

When we tested the fine-tuned voice model with real customers, we saw encouraging signs that the improvements were paying off. A few highlights:

- **Clearer conversations**: Customers asked the agent to repeat itself- *significantly less often*. Shorter, more focused responses were easier to understand during calls, which reduced friction.
- **More natural flow**: Conversations tended to have slightly more back-and-forth exchanges, since the agent delivered information in digestible steps instead of long, packed responses. This felt much closer to how people naturally talk on a phone call.
- **Shorter calls, same outcomes**: Even with more turns, overall call durations were modestly shorter. By cutting down on redundancy, the agent kept conversations efficient while still resolving customers’ issues.
- **Consistent quality**: Across offline and live evaluations, the fine-tuned model produced responses that were judged more concise, clear, and human-like compared to the baseline.

Taken together, these results suggest that post-training helped our agent become easier to follow, more conversational, and more efficient — qualities that matter a lot in a voice setting, where every extra second counts.

## What's next

Voice is just one part of the Sierra experience, but it’s a critical one. By investing in post-training, we’re making sure our agents not only understand *what* to say but also *how* to say it. This project is an early example of how post-training can unlock higher-quality, more human-like conversations.

As we continue to refine these techniques, every Sierra conversation will get just a little smoother, clearer, and more natural.
