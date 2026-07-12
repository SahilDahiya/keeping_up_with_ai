---
title: Agentic eval development with the Braintrust CLI
topic: evals-observability
subtopic: testing
secondary_topics:
- agents/planning
summary: Shows how to use the Braintrust CLI for agentic eval development, turning
  local experiments into repeatable tests for agent behavior.
source: braintrust
url: https://www.braintrust.dev/blog/agentic-eval-development
author: Braintrust Team
published: '2026-04-08'
fetched: '2026-07-11T04:31:12Z'
classifier: codex
taxonomy_rev: 1
words: 940
content_sha256: cf7a6f23dd739eda3c11e975ad11c7394c8c5005098b11d916baf8c6e6d8d3bf
---

# Agentic eval development with the Braintrust CLI

8 April 2026Ornella Altunyan5 min

Running evals is the easy part. The hard part is figuring out what to do when they fail. You stare at a score, dig through traces, form a hypothesis, tweak a prompt or scorer, re-run, and repeat. This loop is where most of the real work happens, and it compounds quickly when you have dozens of failing cases to triage.

Coding agents are good at exactly this kind of work. They can read structured output, form hypotheses, make targeted edits, and verify the results. The [Braintrust CLI ( bt)](https://www.braintrust.dev/docs/reference/cli) gives them a direct interface to your eval data, which means the debugging loop that used to require you to context-switch between terminal, browser, and editor can now run in a single session.

The core workflow has five steps.

- Run evals with `bt eval`
- Inspect results with `bt view logs`or`bt sql`
- Identify failures
- Have the coding agent fix the prompt, scorer, or application code
- Re-run and compare

Each of these steps maps to a CLI command that produces structured output. A coding agent like Claude Code can call `bt` commands directly, read the JSON results, and act on them without any special integration. The agent gets the same data you would see in the Braintrust UI, but in a format it can reason over programmatically.

`bt view logs` gives you interactive trace browsing directly in your terminal. It defaults to the last hour of data, but you can widen the window with `--window` (e.g. `--window 3d`). You can narrow down to specific spans, filter by score thresholds, or search for patterns in inputs and outputs.

The real power for agentic workflows is `bt sql`, which lets you query your logs with full SQL:

bash

```
bt sql "SELECT id, input, output, scores FROM project_logs('<project-id>') WHERE scores.Factuality < 0.5 LIMIT 10"
```
This returns JSON that a coding agent can parse and reason over. You can pipe the output into your agent's context, ask it to identify common failure patterns, and let it propose fixes.

`bt view trace` pulls a single trace by ID, which is useful when you need the agent to do a deep analysis of one specific failure. The agent can see the full span tree, including tool calls, LLM completions, and intermediate reasoning steps.

`bt setup` configures your coding agent with Braintrust context, including MCP configuration so the agent can query your data natively. `bt setup instrument` auto-instruments your repo so traces flow to Braintrust without manual setup.

Once configured, your agent can query eval results, browse traces, and look up documentation as part of its normal workflow. The setup is a one-time step that makes every subsequent debugging session faster.

`bt eval --watch` re-runs your eval every time the underlying code changes. Pair this with a coding agent that is iterating on a prompt or scorer, and you get a tight feedback loop where the agent can see the impact of each change in seconds.

The agent makes an edit, the eval re-runs automatically, and the agent reads the new scores. If scores improved, it moves on. If not, it tries a different approach. This is especially effective for prompt tuning, where small changes can have outsized effects that are hard to predict without running the eval.

Use `bt sql` to surface the lowest-scoring examples from a recent run:

bash

```
bt sql "SELECT id, input, expected, output, scores FROM project_logs('<project-id>') ORDER BY scores.overall ASC LIMIT 5"
```
Hand these to your coding agent and ask it to analyze the traces for common patterns. Maybe the model is hallucinating when the input contains ambiguous references, or maybe a tool call is returning unexpected results. The agent can propose targeted fixes, whether that means updating the prompt, adding input validation, or adjusting a scorer threshold.

Add `bt eval` to your CI pipeline so every PR gets scored before merge. When evals fail, the agent that opened the PR can query the results with `bt sql`, diagnose the regression, and push a fix, all without human intervention.

This turns evals from a reporting mechanism into an active part of your development process. Failing evals become actionable signals, not just red badges.

Say you have a customer support agent that is hallucinating product features on certain inputs. You ask your coding agent to figure out why and fix it.

The coding agent starts by querying for the failing cases:

bash

```
bt sql "SELECT id, input, output, scores FROM project_logs('<project-id>') WHERE scores.Factuality < 0.5 ORDER BY scores.Factuality ASC LIMIT 10"
```
It reads the results and notices that most failures involve questions about pricing tiers. It pulls a trace for one of these cases to look deeper:

bash

```
bt view trace --trace-id <span-id>
```
The trace reveals that the retrieval step is returning documentation about a deprecated pricing page. The coding agent updates the retrieval configuration to exclude deprecated docs, then re-runs the eval to verify:

bash

```
bt eval evals/support-agent.ts
```
Factuality scores jump from 0.3 to 0.9 on the affected cases. The agent runs the full suite to confirm there are no regressions, then commits the fix.

You asked one question. The coding agent ran the SQL query, inspected the trace, made the code change, and verified the result, all in one session without leaving the terminal.

Install the CLI and run `bt setup` to configure your coding agent:

bash

```
npm install -g braintrust
bt login
bt setup
```
From there, start with `bt eval` on an existing eval and let your agent take it from there. The [CLI reference](https://www.braintrust.dev/docs/reference/cli) covers the full set of commands.
