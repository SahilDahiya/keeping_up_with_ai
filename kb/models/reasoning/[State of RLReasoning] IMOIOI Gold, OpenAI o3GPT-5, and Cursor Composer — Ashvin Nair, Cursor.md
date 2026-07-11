---
title: '[State of RL/Reasoning] IMO/IOI Gold, OpenAI o3/GPT-5, and Cursor Composer
  — Ashvin Nair, Cursor'
topic: models
subtopic: reasoning
secondary_topics:
- evals-observability/evaluation
summary: State-of-RL reasoning recap covering IMO and IOI results, o3, GPT-5, and
  Cursor Composer.
source: latent-space
url: https://www.latent.space/p/state-of-rlreasoning-imoioi-gold
author: Latent Space
published: '2025-12-30'
fetched: '2026-07-11T05:15:44Z'
classifier: codex
taxonomy_rev: 1
words: 660
content_sha256: 973057de2f1e5a5f9d44c9bc9f44e8923a312c596407b00093f34c9271747eec
---

# [State of RL/Reasoning] IMO/IOI Gold, OpenAI o3/GPT-5, and Cursor Composer — Ashvin Nair, Cursor

From Berkeley robotics and OpenAI’s 2017 Dota-era internship to shipping RL breakthroughs on GPT-4o, o1, and o3, and now leading model development at **Cursor**, **Ashvin Nair** has done it all. We caught up with Ashvin at **NeurIPS 2025** to dig into the inside story of OpenAI’s reasoning team (spoiler: it went from a dozen people to 300+), why **IOI Gold felt reachable in 2022 but somehow didn’t change the world** when o1 actually achieved it, how RL doesn’t generalize beyond the training distribution (and why that means you need to bring economically useful tasks *into* distribution by co-designing products and models), the deeper lessons from the RL research era (2017–2022) and why most of it didn’t pan out because the community overfitted to benchmarks, how **Cursor is uniquely positioned to do continual learning at scale** with policy updates every two hours and product-model co-design that keeps engineers in the loop instead of context-switching into ADHD hell, and his bet that the next paradigm shift is **continual learning with infinite memory**—where models experience something once (a bug, a mistake, a user pattern) and never forget it, storing millions of deployment tokens in weights without overloading capacity.

We discuss:

- Ashvin’s path: - **Berkeley robotics PhD → OpenAI 2017 intern (Dota era) → o1/o3 reasoning team → Cursor ML lead**in three months
- Why - **robotics people are the most grounded at NeurIPS**(they work with the real world) and simulation people are the most unhinged (Lex Fridman’s take)
- The - **IOI Gold paradox**: “If you told me we’d achieve IOI Gold in 2022, I’d assume we could all go on vacation—AI solved, no point working anymore. But life is still the same.”
- The - **RL research era (2017–2022) and why most of it didn’t pan out**: overfitting to benchmarks, too many implicit knobs to tune, and the community rewarding complex ideas over simple ones that generalize
- Inside the - **o1 origin story**: a dozen people, conviction from Ilya and Jakob Pachocki that RL would work, small-scale prototypes producing “surprisingly accurate reasoning traces” on math, and first-principles belief that scaled
- The - **reasoning team grew from ~12 to 300+ people**as o1 became a product and safety, tooling, and deployment scaled up
- Why - **Cursor is uniquely positioned for continual learning**: policy updates every two hours (online RL on tab), product and ML sitting next to each other, and the entire software engineering workflow (code, logs, debugging, DataDog) living in the product
- **Composer**as the start of product-model co-design: smart enough to use, fast enough to stay in the loop, and built by a 20–25 person ML team with high-taste co-founders who code daily
- The - **next paradigm shift: continual learning with infinite memory**—models that experience something once (a bug, a user mistake) and store it in weights forever, learning from millions of deployment tokens without overloading capacity (trillions of pretraining tokens = plenty of room)
- Why - **off-policy RL is unstable**(Ashvin’s favorite interview question) and why Cursor does two-day work trials instead of whiteboard interviews
- The vision: automate software engineering as a process (not just answering prompts), co-design products so the entire workflow (write code, check logs, debug, iterate) is in-distribution for RL, and make models that - **never make the same mistake twice**

—

Ashvin Nair

- Cursor: https://cursor.com

## Full Video Episode

## Timestamps

[00:00:00](https://www.youtube.com/watch?v=4JHXU1Cpcsc) Introduction: From Robotics to Cursor via OpenAI[00:01:58](https://www.youtube.com/watch?v=4JHXU1Cpcsc&t=118s) The Robotics to LLM Agent Transition: Why Code Won[00:09:11](https://www.youtube.com/watch?v=4JHXU1Cpcsc&t=551s) RL Research Winter and Academic Overfitting[00:11:45](https://www.youtube.com/watch?v=4JHXU1Cpcsc&t=705s) The Scaling Era and Moving Goalposts: IOI Gold Doesn't Mean AGI[00:21:30](https://www.youtube.com/watch?v=4JHXU1Cpcsc&t=1290s) OpenAI's Reasoning Journey: From Codex to O1[00:20:03](https://www.youtube.com/watch?v=4JHXU1Cpcsc&t=1203s) The Blip: Thanksgiving 2023 and OpenAI Governance[00:22:39](https://www.youtube.com/watch?v=4JHXU1Cpcsc&t=1359s) RL for Reasoning: The O-Series Conviction and Scaling[00:25:47](https://www.youtube.com/watch?v=4JHXU1Cpcsc&t=1547s) O1 to O3: Smooth Internal Progress vs External Hype Cycles[00:33:07](https://www.youtube.com/watch?v=4JHXU1Cpcsc&t=1987s) Why Cursor: Co-Designing Products and Models for Real Work[00:34:14](https://www.youtube.com/watch?v=4JHXU1Cpcsc&t=2054s) Composer and the Future: Online Learning Every Two Hours[00:35:15](https://www.youtube.com/watch?v=4JHXU1Cpcsc&t=2115s) Continual Learning: The Missing Paradigm Shift[00:44:00](https://www.youtube.com/watch?v=4JHXU1Cpcsc&t=2640s) Hiring at Cursor and Why Off-Policy RL is Unstable
