---
title: 'How to run Kimi K3 in any harness: routing with Baseten Switch'
kind: blog
topic: null
subtopic: null
secondary_topics: []
summary: null
triage: null
skip_reason: null
source: baseten
url: https://www.baseten.co/blog/how-to-run-kimi-k3-in-any-harness-routing-with-baseten-switch
author: Zak Keener
published: '2026-07-30'
fetched: '2026-11-12T06:15:10Z'
classifier: null
taxonomy_rev: 2
words: 840
content_sha256: 2ca66b198115dfd0e3b33ca6ad73c222f9eed231bb66845a67aae5e960e6c1b0
---

# How to run Kimi K3 in any harness: routing with Baseten Switch

AI engineering
# How to run Kimi K3 in any harness: routing with Baseten Switch

The easiest way to run a mix of open and closed models in your harness.


- Authors
- Date
- July 30, 2026

TLDR

The easiest way to run a mix of open and closed models in your harness. Baseten Switch is a local mac app written in Go that forwards requests from Codex/Claude Code to models like Kimi K3/GLM 5.2 with a toggle. Track cost, perf, and usage per model in a comprehensive dashboard.

What would yesterday's coding session have cost on Kimi K3 instead of Fable? Every week there's a new open model that's allegedly better at your workload. The only way to know is to try inside your actual harness, on your actual tasks, against what you use today.

Often this looks like one frontier orchestration model for planning and review, and multiple subagents for task execution. Kimi K3 is one model that is a leading candidate for orchestration, which could be paired with GLM-5.2 Fast subagents.

[Baseten Switch](https://github.com/basetenlabs/baseten-switch) is a local Mac app, written in Go, that sits between your harness and your models. It routes traffic between open models on Baseten and the native closed models that come with the popular harnesses, independently at the orchestrator and subagent levels. For example, you can route all your Fable traffic to Kimi K3, all your Opus subagent traffic to GLM-5.2 Fast, then flip back with a menubar toggle and compare the metrics side by side.

The best agent combinations are increasingly mixed. Optimizing your agents now looks more like managing a team with many talents and specialties. An enterprise might weigh cost and security; an individual might value maximizing reasoning on the orchestrator and raw speed underneath. But testing meant reconfiguring endpoints using path variables, restarting sessions, and losing your original settings. Switch makes swapping between models smooth, reversible, and measurable, so you can find your best mix of reliability, performance, and cost instead of guessing.

**Here's exactly how to use Kimi-K3 inside 3 of the most popular harnesses today in \<5min, which can be generalized to any other:**

To get started running open models in Claude Code, first install and launch Baseten Switch.shell

shell

```
brew trust basetenlabs/baseten
brew install basetenlabs/baseten/baseten-switch
baseten-switch setup
baseten-switch up --install
# Enable the Switch for the harness(es) your use:
# for Claude Code
baseten-switch claude on
# for Codex
baseten-switch codex on
baseten-switch doctor --probe
# Start coding!
claude # or codex --profile baseten
```
**Recommended patterns:**We recommend pointing orchestration agents, such as Fable 5 or GPT 5.6 Sol (frontier, reasoning model), to an open model like Kimi-K3. For subagents that execute and implement the individual components of the plan, we recommend substituting Opus or equivalent with GLM-5.2 Fast.From here, you’ll want to start a new session to connect to the local router that Switch has set up.

**Features:**

- You can switch between Native (Anthropic/OpenAI) and Open (Baseten) models live, without having to reconfigure your settings and restart sessions
- Try out any of the Model API models directly from your Claude Code or Codex - no changes to skills, subagents, MCPs or any other of your configured settings

Capture performance and cost metrics from Baseten and Anthropic usage. You can see how much you’re saving by using OSS models and measuring how much the same tokens would have cost if you ran harness default closed-source models. Compare different to each other in charts so you analyze your spend patterns for both open and closed models. Other performance metrics surface tokens per second (TPS), time to first token (TTFT), and total tokens generated from each model.

Baseten Switch appears as a menubar icon for easy access. Toggle the Switch on or off with ease. When toggled on, your Switch model preferences are applied, routing your requests to open models on Baseten; if off, all traffic goes to the native harness endpoints.

Configure where requests from your harness are sent. For example, your usual requests to Fable can be replaced by Kimi K3, Opus and Sonnet be replaced by GLM 5.2, and Haiku by Inkling. All at a fraction of the cost.

1\. Run:

bash

`curl -LsSf https://langch.in/dcode`
2\. Launch with \`dcode\` and inside it:

- /install baseten → add Baseten integration
- /auth → add your Baseten API key
- /model → switch to Kimi-K3

1. **Where do my prompts go?** Switch runs a local router; requests to open models go to Baseten's inference endpoints. Your code and prompts leave your machine the same way they do with Anthropic today—just to a different provider. We have a ZDR policy and Baseten never sees your prompts.
2. **Does Baseten see my usage metrics?** All usage metrics are computed locally on your machine.
3. **Am I double-paying? If I'm on a Claude Max subscription and route to Baseten, am I paying for both?** No. Routing happens based on your preferences. If you map models to be routed to Baseten, then you'll pay for what you use.
