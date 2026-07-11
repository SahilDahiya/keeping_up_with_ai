---
title: '[State of Post-Training] From GPT-4.1 to 5.1: RLVR, Agent & Token Efficiency
  — Josh McGrath, OpenAI'
topic: models
subtopic: fine-tuning
secondary_topics:
- models/reasoning
summary: State-of-post-training recap covering RLVR, agent training, token efficiency,
  and GPT-4.1 to GPT-5.1 shifts.
source: latent-space
url: https://www.latent.space/p/state-of-post-training-from-gpt-41
author: Latent Space
published: '2025-12-31'
fetched: '2026-07-11T05:15:42Z'
classifier: codex
taxonomy_rev: 1
words: 660
content_sha256: 9cf68218262f62177fad7aa3db6ab9479559f59fb96edaf434c8e98ccfafc0cc
---

# [State of Post-Training] From GPT-4.1 to 5.1: RLVR, Agent & Token Efficiency — Josh McGrath, OpenAI

From pre-training data curation to shipping **GPT-4o**, **o1**, **o3**, and now **GPT-5 thinking** and the **shopping model**, **Josh McGrath** has lived through the full arc of OpenAI’s post-training evolution—from the PPO vs DPO debates of 2023 to today’s RLVR era, where the real innovation isn’t optimization methods but **data quality, signal trust, and token efficiency**. We sat down with Josh at **NeurIPS 2025** to dig into the state of post-training heading into 2026: why RLHF and RLVR are both just policy gradient methods (the difference is the input data, not the math), how **GRPO** from DeepSeek Math was underappreciated as a shift toward more trustworthy reward signals (math answers you can verify vs. human preference you can’t), why **token efficiency** matters more than wall-clock time (GPT-5 to 5.1 bumped evals *and* slashed tokens), how **Codex** has changed his workflow so much he feels “trapped” by 40-minute design sessions followed by 15-minute agent sprints, the infrastructure chaos of scaling RL (”way more moving parts than pre-training”), why **long context** will keep climbing but agents + graph walks might matter more than 10M-token windows, the **shopping model** as a test bed for interruptability and chain-of-thought transparency, why **personality toggles** (Anton vs Clippy) are a real differentiator users care about, and his thesis that the education system isn’t producing enough people who can do **both distributed systems and ML research**—the exact skill set required to push the frontier when the bottleneck moves every few weeks.

We discuss:

- Josh’s path: - **pre-training data curation → post-training researcher at OpenAI**, shipping GPT-4o, o1, o3, GPT-5 thinking, and the shopping model
- Why he switched from pre-training to post-training: “Do I want to make 3% compute efficiency wins, or change behavior by 40%?”
- The - **RL infrastructure challenge**: way more moving parts than pre-training (tasks, grading setups, external partners), and why babysitting runs at 12:30am means jumping into unfamiliar code constantly
- How - **Codex**has changed his workflow: 40-minute design sessions compressed into 15-minute agent sprints, and the strange “trapped” feeling of waiting for the agent to finish
- The - **RLHF vs RLVR debate**: both are policy gradient methods, the real difference is- **data quality and signal trust**(human preference vs. verifiable correctness)
- Why - **GRPO**(from DeepSeek Math) was underappreciated: not just an optimization trick, but a shift toward reward signals you can actually trust (math answers over human vibes)
- The - **token efficiency revolution**: GPT-5 to 5.1 bumped evals- *and*slashed tokens, and why thinking in tokens (not wall-clock time) unlocks better tool-calling and agent workflows
- **Personality toggles**: Anton (tool, no warmth) vs Clippy (friendly, helpful), and why Josh uses custom instructions to make his model “just a tool”
- The - **router problem**: having a router at the top (GPT-5 thinking vs non-thinking)- *and*an implicit router (thinking effort slider) creates weird bumps, and why the abstractions will eventually merge
- **Long context**: climbing Graph Blocks evals, the dream of 10M+ token windows, and why agents + graph walks might matter more than raw context length
- Why the education system isn’t producing enough people who can do - **both distributed systems and ML research**, and why that’s the bottleneck for frontier labs
- The 2026 vision: - **neither pre-training nor post-training is dead**, we’re in the fog of war, and the bottleneck will keep moving (so emotional stability helps)

—

Josh McGrath

- OpenAI: https://openai.com

## Full Video Episode

## Timestamps

[00:00:00](https://www.youtube.com/watch?v=botHQ7u6-Jk) Introduction: Josh McGrath on Post-Training at OpenAI[00:04:37](https://www.youtube.com/watch?v=botHQ7u6-Jk&t=277s) The Shopping Model: Black Friday Launch and Interruptability[00:07:11](https://www.youtube.com/watch?v=botHQ7u6-Jk&t=431s) Model Personality and the Anton vs Clippy Divide[00:08:26](https://www.youtube.com/watch?v=botHQ7u6-Jk&t=506s) Beyond PPO vs DPO: The Data Quality Spectrum in RL[00:01:40](https://www.youtube.com/watch?v=botHQ7u6-Jk&t=100s) Infrastructure Challenges: Why Post-Training RL is Harder Than Pre-Training[00:13:12](https://www.youtube.com/watch?v=botHQ7u6-Jk&t=792s) Token Efficiency: The 2D Plot That Matters Most[00:03:45](https://www.youtube.com/watch?v=botHQ7u6-Jk&t=225s) Codex Max and the Flow Problem: 40 Minutes of Planning, 15 Minutes of Waiting[00:17:29](https://www.youtube.com/watch?v=botHQ7u6-Jk&t=1049s) Long Context and Graph Blocks: Climbing Toward Perfect Context[00:21:23](https://www.youtube.com/watch?v=botHQ7u6-Jk&t=1283s) The ML-Systems Hybrid: What's Hard to Hire For[00:24:50](https://www.youtube.com/watch?v=botHQ7u6-Jk&t=1490s) Pre-Training Isn't Dead: Living Through Technological Revolution
