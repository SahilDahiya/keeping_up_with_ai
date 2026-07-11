---
title: Claude Code meets Braintrust
topic: agents
subtopic: tool-use
secondary_topics:
- evals-observability/tracing
summary: Shows how Claude Code workflows can connect to Braintrust so coding-agent
  traces, experiments, and eval data are captured for review.
source: braintrust
url: https://www.braintrust.dev/blog/claude-code-braintrust-integration
author: Braintrust Team
published: '2025-12-23'
fetched: '2026-07-11T04:31:47Z'
classifier: codex
taxonomy_rev: 1
words: 348
content_sha256: 02040d09cdfbc308e0538bfad637547f26b1e711b530a616d313126df4f0b269
---

# Claude Code meets Braintrust

23 December 2025Morgane Palomares2 min

[Claude Code](https://docs.anthropic.com/en/docs/claude-code/overview) is a fast way to build AI agents. You stay in the terminal, iterate quickly, and work with an AI that understands your codebase. But the moment something breaks, the workflow falls apart: you leave Claude Code, open Braintrust in a browser, search for the right traces, and piece together what happened after the fact. Checking experiment results or logging new data adds more tab switching and more lost context.

That gap between where you build and where you debug slows agent development. We closed that gap by making Claude Code and Braintrust work as a two-way system instead of a one-way export.

There are two plugins. The first, [ trace-claude-code](https://www.braintrust.dev/docs/integrations/sdk-integrations/claude-code#trace-claude-code), automatically captures every Claude Code session as structured, hierarchical traces in Braintrust. Conversations, tool calls, and intermediate steps are logged by default with no extra work.

![Trace Claude Code](https://www.braintrust.dev/blog/img/trace-claude-code.png)


The second plugin, [ braintrust](https://www.braintrust.dev/docs/integrations/sdk-integrations/claude-code#use-braintrust-with-claude-code), brings Braintrust data back into Claude Code so developers can query logs, fetch experiment results, and log new data directly from the terminal using natural language.

![Use Braintrust in Claude Code](https://www.braintrust.dev/blog/img/use-braintrust-in-claude-code.png)


The bidirectional flow is the important part. Most observability integrations only send data out, but agent development requires moving in both directions. You need to see what just happened, pull context from past runs, and compare behavior across experiments while you are still writing code.

In practice, this means you can ask Claude Code to find sessions from last week related to authentication issues, or pull the failing cases from a specific experiment, or log a new example for an eval dataset without leaving your editor. Claude Code queries Braintrust and returns the results inline, keeping the full development context intact. This matters because agents grow more complex and failures become harder to reason about after the fact.

[Once the plugins are installed](https://www.braintrust.dev/docs/integrations/sdk-integrations/claude-code#setup) and an API key is added, trace capture starts automatically. When you need production data or experiment results, Claude Code can fetch them on demand. The same Braintrust infrastructure teams use to run production AI now operates directly inside the development loop.
