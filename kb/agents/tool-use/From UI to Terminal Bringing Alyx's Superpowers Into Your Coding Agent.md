---
title: 'From UI to Terminal: Bringing Alyx''s Superpowers Into Your Coding Agent'
topic: agents
subtopic: tool-use
secondary_topics:
- evals-observability/tracing
summary: Introduces an AX CLI preview that brings Alyx-style trace and eval workflows
  into terminal-based coding-agent loops.
source: arize
url: https://arize.com/blog/ax-cli-dev-preview
author: Aparna Dhinakaran; Chris Cooning
published: '2026-03-04'
fetched: '2026-07-11T04:55:05Z'
classifier: codex
taxonomy_rev: 1
words: 339
content_sha256: d1f72a63bd01f76f8c7dbfc88d7d7b4fe9a83d3b20f8d8718d22cce2e53fb9a5
---

# From UI to Terminal: Bringing Alyx's Superpowers Into Your Coding Agent

*Co-Authored by Aparna Dhinakaran, Co-founder & Chief Product Officer & Chris Cooning, Head of Product Marketing.*

Last week we launched[ Alyx 2.0](https://arize.com/blog/alyx-2-0-the-ai-agent-that-actually-plans/), the in-app AI engineering agent for Arize AX.

Alyx replaced clicking through the UI with natural language intent. The [AX CLI](https://github.com/Arize-ai/arize-ax-cli) takes it a step further: making that same data machine readable so your coding agent can work with it directly.

Here’s a quick demo of what that looks like in practice.

In the Arize UI, Alyx can surface things like “what are the most common questions users are asking?” or “which tool calls are failing?” It’s powerful, but you have to be in the browser to use it.

We dogfood everything. Alyx is traced to Arize. I used the CLI to pull recent spans into a local file:

“Hey Claude, can you use the ax cli to figure out what are the most common questions asked in the project [id]?”

Then I dropped that file into Cursor and asked: *“Look at spans.csv and surface what the most common questions users are asking.”*

Same analysis Alyx does in the UI, but now it’s running inside my editor against a local file using whatever coding agent I want: Cursor, Claude Code, Codex, whatever.

This is the idea behind the AX CLI. The data in Arize is valuable. The CLI makes it programmable. Your coding agent does the rest.

## What’s available

```
```
pip install arize-ax-cli
ax config init

			The developer preview ships with **spans, experiments, datasets, and projects**. Every command supports structured output (JSON, CSV, Parquet) ready for agents and automation, because it’s time that humans stop writing syntax by hand.

## What’s next

We’re building toward full headless debugging: traces, experiments, prompts, and higher-level skills that bundle common workflows like “instrument my app,” “debug my traces,” “help me build an eval.” Think of today as the wiring. The workflows come next.

Try it. Pull spans for your own project. Run an analysis in your editor. Tell us what workflows you’d want as built-in skills.

**Get started**
