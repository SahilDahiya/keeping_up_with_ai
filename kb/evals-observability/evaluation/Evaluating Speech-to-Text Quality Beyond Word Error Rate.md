---
title: 'Evaluating Speech-to-Text Quality: Beyond Word Error Rate'
topic: evals-observability
subtopic: evaluation
secondary_topics:
- models/multimodal
summary: Explains why word error rate is insufficient for speech-to-text evaluation
  and what production teams should measure instead.
source: cresta
url: https://cresta.com/blog/evaluating-speech-to-text-quality-beyond-word-error-rate
author: Binoy Robin Dalal
published: '2026-05-29'
fetched: '2026-07-11T03:58:04Z'
classifier: codex
taxonomy_rev: 1
words: 1722
content_sha256: 5b049e335ff7e35bbdedcc9b16b26135ad9c1b42c03a459bb6eb3700b21a42a2
---

# Evaluating Speech-to-Text Quality: Beyond Word Error Rate

**LLMs do not fail gracefully on Speech-to-Text (STT) errors. They fail confidently.** A single digit swap triggers the wrong tool call. A missed "not" flips intent from refusal to agreement. A botched turn boundary causes an agent to interrupt mid-sentence. These are not edge cases. They are the dominant failure modes in production voice systems, and the reason **Word Error Rate (WER)** **alone no longer tells us whether an STT system is shippable**.

At Cresta, STT sits at the foundation of every voice product we ship: real-time coaching, post-call analytics, voice agents, translation. When STT quality degrades, the symptom is rarely "WER moved from 9 percent to 10 percent". It is a voice agent aborting a flow because it misheard a confirmation code. A supervisor flagging transcripts that hallucinate profanity. A multilingual deployment where Chinese calls are unusable while German calls are fine. This post explains how we evaluate STT in a way that catches those problems *before* they ship.

## Why WER Is Not Enough

**Word Error Rate** counts substitutions, insertions, and deletions against a human reference. It became the default metric because it is simple, model-agnostic, and correlates reasonably with how accurate a transcript looks to a human reader. That last assumption is the problem: WER assumes transcripts are read by people. In modern voice stacks, transcripts are read by LLMs that branch on entities, intents, and timing. **All errors are not equal.** Missing "the" costs nothing. Missing "not" inverts the call. 

WER weights every token the same. The downstream system does not. A single function word can flip "I do not want to upgrade" into "I do want to upgrade," and the agent confidently routes a customer into a sales flow they explicitly refused. The transcript is **99 percent accurate**. The interaction is **100 percent broken**.

This asymmetry is why we stopped trusting aggregate accuracy as a release gate. The errors that matter are not the frequent ones; they are the consequential ones, and **WER is structurally blind to the difference**.

## A Layered Evaluation Framework

We evaluate STT in four layers. Each measures something different, and each is critical.

### Layer 1: Lexical

We still compute the classics on every release.

- **WER**is our baseline accuracy gauge.
- **CER**is what we use for- **CJK languages**where word boundaries are ambiguous, and for any utterance where character-level precision matters (emails, IDs, confirmation codes).
- **SER**is what we use when any error breaks the task.

Their limitation is the same: all errors weighted equally, semantic correctness ignored, pathologies averaged away.

### Layer 2: Entity and Keyword Metrics

In voice workflows, **entities drive business logic**. A wrong account number breaks the call even at 3 percent WER. We track three metrics here:

- **Keyword Recall Rate (KRR):**how often domain-specific terms are correctly recognized.
- **Entity Accuracy Rate (EAR):**per entity type (phone number, email, amount, date), what percentage are correct end to end.
- **Entity-Weighted WER:**standard WER, but errors on entity tokens are multiplied. We typically use 3x to 5x, but- **the right multiplier is application-dependent**. Set it based on how much downstream damage an entity error causes in your workflow.

In head-to-head vendor evaluations with near-identical WER, entity metrics have been the deciding factor for us more often than not.


### Layer 3: Semantic Evaluation

When dense ground truth is not available, or when we care more about meaning than exact words, we use LLMs as evaluators. Three patterns work:

- **LLM as judge.**Given reference and hypothesis, ask: does the hypothesis preserve meaning? Rate one to five with a rubric. Blind the model to which transcript is which.
- **LLM as extractor.**Extract structured facts (amount, date, intent) from both transcripts independently. Compare the extractions.
- **LLM as consistency checker.**For a single transcript, are there contradictions or nonsensical outputs?

We treat LLM scores as a **signal**, not ground truth. They tell us where to look, not what to ship. We calibrate against human ratings on a sample of every evaluation. The temptation with **LLM-as-judge** is to fully automate the quality loop and stop sampling. We do not. LLM judges have their own failure modes: **prompt sensitivity**, **position bias** when comparing two transcripts side by side, and a tendency to confidently agree with whichever hypothesis sounds more fluent even when it is factually wrong. Treating a 4.7 average from a judge model as proof of shippability is how regressions slip through.

Our rule is simple. Every evaluation includes a **human-rated sample** large enough to catch judge drift. When the judge and the humans disagree, the **humans win and the judge gets re-tuned**. The LLM accelerates triage, but does not replace the release decision.

### Layer 4: End-to-End Task Metrics

This is where we stop asking "how good is STT in isolation?" and ask "what happens to the product?"

For voice agents, three metrics matter most:

- **Latency distribution (p50, p95):**time from the user's last word to the agent's first response. The 50th and 95th percentile latencies tell us whether the system is fast enough on a good day and on a bad day. In- [Engineering for Real-Time Voice Agent Latency](https://cresta.com/blog/engineering-for-real-time-voice-agent-latency), Cresta CTO Daniel Hoske discussed how conversational flow degrades sharply above 800ms end-to-end. A transcript that arrives 400ms late is worse than one that arrives 150ms late with marginally higher WER.
- **Interruption rate:**how often the agent talks over the user, measured from STT timestamps and- **VAD**(voice activity detection) boundaries.
- **Failure patterns:**short utterances never recognized, long silences without finalization, misaligned endpointing causing mid-sentence replies.

For translation, we layer STT metrics per language on top of translation metrics like **COMET** and **chrF** (standard MT quality scores), then check end-to-end entity fidelity. For **analytics**, we compare LLM answers on STT transcripts against the same LLM's answers on human transcripts. The divergence rate is itself a task-level quality signal.

## Two Failure Modes That Shaped Our Approach

The framework above came out of real production incidents, two of which illustrate why WER alone is not enough.

### Hallucinated Profanity

**What happened:** An STT model update started inserting profanity into transcripts where none was spoken. Supervisors flagged it within hours. Overall WER had barely moved because the hallucinations were rare in aggregate.

**Why WER missed it:** A hallucinated word is just a substitution error. Spread across millions of tokens, the impact on aggregate WER may be invisible; the reputational impact on a single flagged call is not.

**What we added:** Now, we construct review sets of every segment containing sensitive terms, then human-classify whether the term is present in the audio or hallucinated. We track **hallucinated profanity rate** as a separate metric with a hard floor: zero. No model ships if it fails this check, regardless of how well it performs on WER.

### Multilingual Cliffs

**What happened:** In a multilingual deployment, German calls performed within target while Chinese calls were close to unusable. The vendor's reported cross-language WER looked acceptable because it averaged everything together.

**Why WER missed it:** Aggregate cross-language WER averages away per-language disasters. A 15 percent average can hide one language at 8 percent and another at 40 percent.

**What we added:** We evaluate per language with dedicated test sets per slice. We measure language detection accuracy independently, and for code-switching calls, we measure switch latency. We do not ship a new language until it clears per-language thresholds on WER, entity accuracy, and human usability ratings. **No exceptions.**

Two other failure modes shaped the framework as well: digit and character confusions (O vs 0, "fifty" vs "fifteen") and short-utterance recognition under noise. We address both with **Entity Accuracy Rate** and **short-utterance recognition rate** respectively. A future post will go deeper on those.

## What the Output Looks Like

Below is a representative slice report from one of our evaluation runs.

The pattern this slice report surfaces in seconds: Chinese needs work before shipping, and noisy customer audio degrades **entity accuracy** more than raw WER suggests. WER alone would have told us "Chinese is worse." The slice view tells us **which workflows we can ship and which we cannot**.

## The Pipeline We Run

Five steps, repeated on every model release and every vendor evaluation.

- **Define slices and metrics.**Languages times speaker roles times noise conditions times scenarios (authentication, booking, complaints). For each slice: lexical, entity, and semantic metrics on samples.
- **Prepare the dataset.**Representative audio per slice. Human-annotated transcripts following a consistent normalization convention. Entity spans labeled. Both raw and normalized scores reported.
- **Run evaluation.**Every STT system or config through the same pipeline. Compute all four layers.
- **Interpret by layer.**Filter on hard constraints first (zero hallucinated profanity, per-language thresholds). Compare on WER. Break ties on entity metrics, worst-slice behavior, and downstream task metrics.
- **Monitor continuously.**Sample production calls. LLM-based quality estimation at scale. Spot audits on flagged slices. Every real-world failure feeds back into the eval dataset.

## What This Means for Voice AI in 2026

The voice AI conversation in 2026 has moved on from "is the transcript accurate?" Voice-to-voice models like Realtime 2 are reframing what "STT" even means, and the cascaded pipeline is no longer the only architecture on the table. But the **evaluation philosophy holds**: task fidelity matters more than transcript fidelity, hard constraints matter more than averages, and slice-level visibility matters more than headline metrics.

For teams still running cascaded pipelines (which is most of the enterprise contact center stack today), this framework is what separates a system that demos well from one that survives production. For teams moving to voice-to-voice, the same layers apply. We will share results from our voice-to-voice eval harness in a follow-up post.

### Annotation and Normalization Conventions

For teams setting up their own eval pipeline, two ground rules matter more than any specific tool choice.

**Evaluate what was said, not what you wish had been written.** Spoken numbers, dates, and amounts go into ground truth in their spoken form, not their canonical form.

**Report both raw and normalized scores.** Normalized scores (lowercase, no punctuation, numbers spelled out, fillers stripped) give fair vendor comparisons. Raw scores show what downstream systems actually see. We have had cases where normalized WER looked fine but raw formatting issues were breaking entity extraction. Both numbers tell different stories. Both belong in the report.

To see how Cresta's voice platform applies this evaluation philosophy end to end across STT, agents, and analytics, [request a personalized demo](https://cresta.com/request-a-demo).
