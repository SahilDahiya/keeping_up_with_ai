---
title: 'Arize Skills: Coding Agent Workflows for Traces, Evals, and Instrumentation'
topic: agents
subtopic: tool-use
secondary_topics:
- evals-observability/tracing
summary: Introduces Arize Skills for coding agents, enabling workflows around trace
  extraction, evals, and instrumentation from agentic development environments.
source: arize
url: https://arize.com/blog/arize-skills-coding-agent-workflows-for-traces-evals-and-instrumentation/
author: Aparna Dhinakaran; Chris Cooning
published: '2026-03-10'
fetched: '2026-07-11T04:55:09Z'
classifier: codex
taxonomy_rev: 1
words: 535
content_sha256: e34dd1d2c020e6b2869798da99198159f501032c9abc3441fd13d0341c3d3d08
---

# Arize Skills: Coding Agent Workflows for Traces, Evals, and Instrumentation

*Co-Authored by Aparna Dhinakaran, Co-founder & Chief Product Officer & Chris Cooning, Head of Product Marketing.*

Two weeks ago we launched [Alyx 2.0](https://arize.com/blog/alyx-2-0-the-ai-agent-that-actually-plans/), the AI engineering agent inside Arize AX. Last week we launched the [AX CLI](https://arize.com/blog/ax-cli-dev-preview), which made your trace data headless and agent-readable.

Today we’re shipping the next piece: **Arize Skills**.

## The days of writing syntax are over

We’re firmly in the agent era. You tell software what you want it to do, and it does it. You shouldn’t have to explain your observability platform to your coding agent every time you open a new session.

“Here’s how Arize works. Here’s what a trace is. Here’s how to instrument this app.”

Same wall of context, every time.

Your agent should already know.

## What Arize Skills are

Skills are pre-built instruction sets that give your coding agent native knowledge of Arize workflows. Install them once and your agent already knows how to export traces, add instrumentation, manage datasets, run experiments, and optimize prompts, without you explaining any of it first.

They work with Cursor, Claude Code, Codex, Windsurf, and 40+ other agents.

**One command to install everything:**

`npx skills add Arize-ai/arize-skills --skill '*' --yes`## What’s available now

| Skill | What it does |
|---|---|
| arize-trace | Export traces and spans by trace ID, span ID, or session ID for debugging |
| arize-instrumentation | Analyze your codebase, then implement tracing — two-phase, agent-assisted |
| arize-dataset | Create, manage, and download datasets and examples |
| arize-experiment | Run and analyze experiments against datasets |
| arize-prompt-optimization | Optimize prompts using trace data and meta-prompting |
| arize-link | Generate deep links to traces, spans, and sessions in the Arize UI |

## What this looks like in practice

We asked Claude Code to build a financial agent using Anthropic, with tools for financial advice, payments, loan calculations, and fraud detection. It built a working agent while we walked through the skills.

Next: “set up tracing to Arize, project FinBot.” The **arize-instrumentation** skill loaded automatically and ran its two-phase flow.

**Phase 1** analyzed the codebase: detected the language, the model provider, the framework. It proposed a plan before touching anything.

We approved it, and **Phase 2** implemented instrumentation across LLM calls, tool calls, and chain spans. FinBot appeared in Arize with live spans.

Then we had Claude generate 10 complex queries against the agent covering loans, fraud detection, and account info. While those ran, we used the **arize-trace** skill to start pulling spans back into the editor.

We asked it to find recent financial advice questions FinBot had answered, surface what it was doing well, and flag gaps.

From there: create more advice-focused queries, build a dataset from those traces, and use it to start evaluating how well FinBot actually handles financial advice.

## The bigger picture

Alyx brought natural language to your observability data in the browser. The AX CLI made that data headless, pulling it into any agent or automation. Skills encode the workflows so your agent can act on it without hand-holding.

An agentic workflow embeds Arize directly into your engineering loop, autonomously improving your AI software.

## Get started

`npx skills add Arize-ai/arize-skills --skill '*' --yes`
