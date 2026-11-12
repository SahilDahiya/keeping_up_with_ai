---
title: 'Introducing NVIDIA Nemotron 3 Ultra: The Nemotron 3.x family is here!'
kind: blog
topic: models
subtopic: architectures
secondary_topics:
- agents/harness
- inference/optimization
summary: NVIDIA Nemotron 3 Ultra is a 550B-parameter MoE (55B active) built mostly
  from Mamba layers instead of quadratic attention so long agent trajectories don't
  slow down over hundreds of steps, giving up to 5x faster inference and 30% lower
  cost; it is post-trained with RL across agentic environments and released fully
  open.
triage: null
skip_reason: null
source: baseten
url: https://www.baseten.co/blog/nvidia-nemotron-3x-model-family
author: Fred Liu
published: '2026-06-04'
fetched: '2026-11-12T06:14:56Z'
classifier: claude
taxonomy_rev: 2
words: 1790
content_sha256: d6815dd3c4400498f0afc237ce58b987fa14970b86468ddc0106b86bb62ebcb4
---

# Introducing NVIDIA Nemotron 3 Ultra: The Nemotron 3.x family is here!

AI models
# Introducing NVIDIA Nemotron 3 Ultra: The Nemotron 3.x family is here!

Are you tired of waiting 17 minutes for a code change?


- Authors
- Date
- June 4, 2026

TLDR

Nemotron 3 Ultra is built for agents that run long. Most models slow to a crawl as an agent's context piles up, because attention cost grows with the square of the context length. Nemotron replaces most of that attention with Mamba layers, whose cost grows in a straight line, so step 300 runs about as fast as step 3. The result is up to 5x faster inference and up to 30% lower cost for long-running agent workflows. The payoff is not a higher score on a single prompt. It is that the agent finishes the job. And it is fully open, so you run it on your own infrastructure.

We have quietly agreed that a spinner running for twenty minutes means the agent is "working hard." It is not working hard. It is rereading its own notes for the four-hundredth time, and each reread is longer than the last.

You give a coding agent a ticket and hit go. The first few steps fly by: it reads a file, makes an edit, runs the tests. Then it reads another file, and another, the plan gets longer, the diff gets longer, and somewhere around step 30 it has slowed to a crawl. Steps that took a second now take twenty. You alt-tab away. You answer some Slack. You get lunch. When you come back, the agent is on step 80, and you have to scroll up to remember what you asked it to do in the first place. Forty minutes, for what was honestly about five minutes of real work.

Here is the part that should bother you. The agent did not slow down because the work got harder. It slowed down because the work got longer. And those are not the same thing.

[Nemotron 3 Ultra](https://blogs.nvidia.com/blog/nvidia-gtc-taipei-computex-2026-news/#nemotron-3-ultra) is a mixture-of-experts (MoE) language model: 550 billion total parameters, with 55 billion active on any given token. Text in, text out. It reasons before it answers, it calls tools, and NVIDIA post-trained it with reinforcement learning (RL) across many agentic environments, so it behaves inside an agent loop and not just a chat box. NVIDIA released it fully open: open weights under the NVIDIA open model license, open training data, and open recipes.

The unusual part is the architecture, and it is the entire reason the agent stays fast. Most frontier models are pure transformers. Nemotron is a hybrid, built mostly from Mamba layers. The outcome is simple: faster task completion for long-running agents. NVIDIA reports up to 5 faster inference and up to 30% lower cost compared with other open frontier models in its class.

It is structural, and it happens to almost every agent running today. An agent works by appending to its own context. Every file it reads, every tool result, every line of its own reasoning gets added to a running transcript, the context only grows. It never shrinks.

For a transformer, that reread gets more expensive the longer the transcript is. Attention is quadratic: twice the context, four times the work per step. So the agent that flew through its first ten steps crawls through its three-hundredth. The longer the task, the worse each step gets.

Read that again, because it is backwards from what you want. The agent slows down most on the big, multi-step jobs, which are exactly the jobs you wanted an agent for in the first place. Hand it something Ulttrivial and it's quick. Hand it something worth doing and it bogs down.

An agent that gets slower the longer it runs punishes you for giving it anything interesting to do.

The slowdown is baked into attention. So the fix is to not use attention for most of the work. That is what Mamba does, and it is the less familiar half of this model, so it is worth slowing down on.

Mamba comes from a family called state-space models (SSMs), and the idea is almost embarrassingly simple. Instead of comparing every token to every other one, imagine one person reading the transcript one entry at a time, keeping running notes on a single index card. Read an entry, update the card: jot down what is new, cross out what no longer matters, move on. The entry itself can be set down, because whatever mattered about it now lives on the card.

Here is what that does to the clock. The index card is a fixed size. Updating it on step 300 costs exactly what it cost on step 3. The work per step never grows, so it stays flat no matter how long the agent runs. A 300-step task is just more entries, at the same steady cost each.

There is an honest tradeoff, and it is the reason the design is cheap. A fixed-size index card cannot hold a word-for-word copy of everything the agent has seen. It is a compression. A well-trained state-space model is very good at choosing what to write down and what to drop, but a running summary is, in the end, a summary.

Side by side, the two patterns look like this. Attention fills an n-by-n grid, one score for every pair of tokens. Mamba threads every token through one fixed-size state.

The triangle is the whole problem. Every filled cell is work the model redoes on every step, and it grows with the square of the context. Mamba replaces the triangle with a single chain, so the work grows in a straight line instead. That is the difference between an agent that crawls by step 300 and one that doesn't.

**Nemotron uses both**

Nemotron 3 Ultra does not pick one. Most of its layers are Mamba, carrying the cheap, tireless index card that keeps every step fast no matter how long the run gets. A smaller number of attention layers stay in the mix, giving the model the power to flip back to the exact token when a step needs precision. The index card for the long haul, the photograph for the moments that need it.

That combination is the whole pitch. The agent keeps the full task in context, takes hundreds of steps, and the three-hundredth step runs about as fast as the third. It does not score higher than a frontier model on a single hard prompt. It finishes the long job while the others are still on step 100.

Each capability earns its place in a long-running agent:

| Capability | What it is | What it does for a long-running agent | 
|---|---|---|
| Hybrid Mamba-Transformer | Mostly SSM layers, some attention | Step time stays roughly flat as the context grows, so the agent finishes long tasks in reasonable wall-clock time. | 
| 1M-token context | Up to a million tokens in one window (NVIDIA's figure) | The whole task fits: every file, the full step history, the plan. Nothing gets truncated and re-fetched. | 
| Reasoning with a token budget | Controllable thinking length | Cap the thinking on routine steps so the agent does not burn minutes over-reasoning a one-line edit. | 
| Tool calling, RL-trained | Post-trained across many agentic environments | Search, edit, run, and retry across hundreds of steps without drifting off the rails. | 
| Latent MoE | NVIDIA: 4 experts for the inference cost of one | More specialized reasoning per token, which NVIDIA reports comes at no added compute. | 
| Multi-token prediction (MTP) | Predicts several future tokens per forward pass | NVIDIA reports faster generation on long sequences, so each step returns sooner. | 

For an agent, wall-clock time is not a vanity metric. It is whether the thing is usable. An agent that finishes a real task in three minutes is a tool you reach for. The same agent at forty minutes is a thing you kick off and forget, and a thing you forget is a thing you stop trusting. Staying fast deep into a long run is what moves an agent from demo to daily driver.

In a one-shot chat, speed is a nicety. In a 300-step agent run, speed is whether it finishes before you give up. That’s why NVIDIA optimized nemotron 3 Ultra around task completion rather than single-turn benchmarks: Faster inference and lower cost compound across hundreds of reasoning steps.


Coding is the easiest slowdown to picture, but every long-running agent hits the same wall, and the same fix applies. A few of the other places teams are pointing it:

- **Deep research**. Search, read, and cross-reference hundreds of sources, then synthesize. The context balloons as sources pile in, which is exactly where a transformer agent grinds to a halt and Nemotron keeps moving.
- **Enterprise workflows.** Persistent, tool-using loops that run all day: triaging thousands of security alerts, ingesting regulatory filings, orchestrating operations. The reasoning steps stay fast even after thousands of tool calls.
- **Chip design**. In electronic design automation (EDA), the agent generates RTL (register-transfer level) descriptions from a spec and verifies a design across thousands of constraints. The state it has to track is enormous, and step time is what decides whether a run finishes overnight or over a week.

Long-running reasoning is only one part of the agentic stack. NVIDIA is also releasing two additional open models that are available on Baseten right away.

**Nemotron 3.5 ASR**

An open streaming speech recognition model for real-time multilingual voice agents covers 40 language-locales with native punctuation and capitalization, runtime-configurable latency modes (80ms–1.12s). Cache-aware architecture means true chunk-by-chunk processing — no recomputation, no buffering lag. Use cases include voice agents, call centers, meeting transcription, in car-assistants and live captions.

**Nemotron 3.5 Content Safety**

An open, efficient multimodal safety model for enterprise AI guard ails across text, images and custom policies. Use cases include prompt and response moderation, content classification, safety pipelines and policy enforcement.

[Nemotron 3 Ultra](https://www.baseten.co/library/nvidia-nemotron-ultra/), [3.5 ASR](https://www.baseten.co/library/nemotron-3-5-asr-streaming-multilingual-0-6b/) and [3.5 Content Safety](https://www.baseten.co/library/nemotron-3-5-content-safety/) are live on Baseten today. At the center of the release is Nemotron 3 Ultra, built for long-running autonomous agents across coding, deep research, and enterprise automation. Point your existing agent harness at it and it behaves like any other chat-completions model, except it does not bog down as the run gets long. Use the token budget to keep routine steps cheap and save the deep reasoning for the steps that earn it.

Smaller siblings. Nemotron 3 also ships in smaller sizes. Its 120B sibling, [Nemotron 3 Super](https://www.baseten.co/library/nvidia-nemotron-super/), is already available on Baseten. For short tasks or latency-bound single calls, start there. Ultra is for the long, many-step runs where staying fast is the whole game.
