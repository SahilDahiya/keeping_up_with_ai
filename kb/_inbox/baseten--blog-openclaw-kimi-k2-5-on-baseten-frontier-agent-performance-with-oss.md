---
title: OpenClaw + Kimi K2.5 on Baseten = frontier agent performance with OSS
kind: blog
topic: null
subtopic: null
secondary_topics: []
summary: null
triage: null
skip_reason: null
source: baseten
url: https://www.baseten.co/blog/openclaw-kimi-k2-5-on-baseten-frontier-agent-performance-with-oss
author: Alex Ker
published: '2026-02-04'
fetched: '2026-11-12T06:14:28Z'
classifier: null
taxonomy_rev: 2
words: 471
content_sha256: e55887a47ee22ac059ef281679f5ca201f61bad4af716a7bac9734d080774853
---

# OpenClaw + Kimi K2.5 on Baseten = frontier agent performance with OSS

AI engineering
# OpenClaw + Kimi K2.5 on Baseten = frontier agent performance with OSS

OpenClaw + Kimi K2.5 on Baseten: frontier agent performance with open-source models. Outperforms Opus 4.5 and 8x cheaper. Install in 2min.


- Authors
- Date
- February 4, 2026

OpenClaw, previously ClawdBot and MoltBot, has taken over the internet as the first Jarvis-like agent that can actually get things done. If you’re not familiar with OpenClaw, think of it as your personal assistant or teammate. OpenClaw runs on your local machine (or the cloud), and executes sub-agents with the ability to maintain memory and use tools. That means OpenClaw can do just about everything: write, execute scripts, browse online and use apps. You can even monitor its behavior from any chat of your choice, such as Telegram and Whatsapp.

OpenClaw is an incredible everyday agent when paired with OSS inference, *especially* Kimi K2.5 on Baseten Model APIs. By pairing OpenClaw and Baseten’s Kimi K2.5 you get quality on par with closed source models and better performance all at a fraction of the cost. On agentic benchmarks, [Kimi K2.5 outperforms Opus 4.5](https://www.kimi.com/blog/kimi-k2-5.html). Kimi K2.5 costs $3/1M output tokens vs. Claude's $25/1M, that's 8x the savings. That can add up extremely fast for token-hungry applications like OpenClaw.

If you’re interested in utilizing Baseten’s Kimi K2.5 Model API in OpenClaw, we’ve added a step by step guide below. All you need is a Baseten API key to get started ([here](https://app.baseten.co/settings/api_keys)). Add this to your environment or save it in a secure location before you dive in!

Enter the following into your terminal:

bash

```
git clone https://github.com/basetenlabs/openclaw-baseten.git
cd openclaw-baseten
pnpm install
pnpm ui:build  # auto-installs UI deps on first run
pnpm build
pnpm openclaw onboard --install-daemon
```
You should see this as the initial screen:

Select QuickStart as onboarding mode

Select Baseten from Model/auth provider and paste your Baseten API key generated before.

After entering your API key details, you should keep the current model (as we recommend Kimi-K2.5). Alternatively, GLM-4.7 is a powerful agentic model.

Continue through the rest of the steps, optionally setting up links to apps or skills. If you have a gateway previously running, it may interfere with this instance, so please select restart.


Hatch the bot in TUI

You now should automatically be redirected to a webpage where you start interacting with OpenClaw. If you prefer the CLI, you can also chat with OpenClaw in the terminal. If you have set up Telegram or Whatsapp, you can control your agent through those apps!

You no longer need to choose between performance, quality and cost. You can get access to higher throughput, lower latency, all while enjoying the smartest OSS agent in your pocket. You can power OpenClaw with any frontier open-source models like Kimi-K2.5, GLM-4.7, and GPT-OSS 120B on Baseten with this [repo](https://github.com/basetenlabs/openclaw-baseten) today.
