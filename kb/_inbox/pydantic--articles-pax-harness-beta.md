---
title: 'Pax: the Pydantic AI coding agent for your terminal'
kind: blog
topic: null
subtopic: null
secondary_topics: []
summary: null
triage: null
skip_reason: null
source: pydantic
url: https://pydantic.dev/articles/pax-harness-beta
author: Michael Pfaffenberger; Douwe Maan; Aditya Vardhan; David Sanchez
published: '2026-11-25'
fetched: '2026-11-26T06:13:01Z'
classifier: null
taxonomy_rev: 2
words: 1873
content_sha256: b8095271dd00f0eb481017a564ed868d937d08a5be35470ba8c1bd42bba5a49b
---

# Pax: the Pydantic AI coding agent for your terminal

![Pax in a terminal running anthropic:claude-opus-5-5: the PAX banner and pydantic-ai-pax 0.75.0, the prompt Briefly: how is a forecast fetched? Three numbered steps, one line counting the tool calls it made (run\_code, list\_files, read\_file), a three-step answer, and the status bar with the model, its 1m-token context window and the cost.](https://pydantic.dev/assets/blog/pax-harness-beta/pax-hero.png)


[Pydantic AI Harness](https://pydantic.dev/docs/ai/harness/) has come a long way since we [launched it alongside Pydantic AI v2](https://pydantic.dev/articles/pydantic-ai-v2) in June. It's the official capability and harness library for Pydantic AI, with more than 100 [capabilities](https://pydantic.dev/docs/ai/capabilities/overview/) you can add to any agent.

We're getting ready to call it 1.0 in about a month, and start maintaining the same [version policy](https://pydantic.dev/docs/ai/project/version-policy/) as Pydantic AI. That means this is the best time to stress test it and let us know if there's still anything we should change before the public API gets set in stone for a while.

Along with that, we're releasing **[Pax](https://pydantic.dev/docs/ai/pax/)** ([`pydantic-ai-pax`](https://pypi.org/project/pydantic-ai-pax/)), the official [Pydantic AI](https://pydantic.dev/pydantic-ai) coding agent for your terminal, built on the Harness SDK. Just as everything in the Harness is a capability, everything in Pax is a plugin: the coding agent itself, sandboxes, MCP, [Logfire](https://pydantic.dev/logfire) tracing, and your own. And you can bring your own harness: point Pax at any Pydantic AI agent with `--agent`. In single runs of Harness-Bench SWE81, it had the highest average score of the four harnesses that ran all eight models, narrowly. It cost less than half of what Codex did on GPT-6.2 Sol, and about the same as Claude Code on Claude Opus 5.5.

If you try it out, please let us know what you think in [our Slack](https://pydantic.dev/docs/logfire/join-slack/).

## What is what?

**[Pydantic AI](https://pydantic.dev/docs/ai/overview/)** is the agent framework: the loop, models from every major provider, tools, and structured output. For reusable building blocks on top of that core, you pass [Capabilities](https://pydantic.dev/docs/ai/capabilities/overview/): bundles of tools, instructions, and hooks you can add to an agent.

**[Pydantic AI Harness](https://pydantic.dev/docs/ai/harness/)** is a library of production capabilities we've built so you can assemble a harness for your own use case. Built in: [durable execution](https://pydantic.dev/docs/ai/capabilities/durable_execution/overview/) that survives crashes and restarts (for agents built on the SDK; not in Pax yet), one [workspace](https://pydantic.dev/docs/ai/core-concepts/workspace/) API across your machine and a dozen cloud and local sandboxes, [computer use](https://pydantic.dev/docs/ai/harness/computer-use/) on each provider's native tool, [model fallback](https://pydantic.dev/docs/ai/capabilities/model-fallback/) that also catches refusals, and [code mode](https://pydantic.dev/docs/ai/harness/code-mode/). Plus the table stakes: file and shell tools, guardrails, [memory](https://pydantic.dev/docs/ai/harness/memory/), [sub-agents](https://pydantic.dev/docs/ai/harness/subagents/), [context management](https://pydantic.dev/docs/ai/harness/compaction/) and [Agent Skills](https://pydantic.dev/docs/ai/harness/skills/).

One of those capabilities is [`Coder()`](https://pydantic.dev/docs/ai/harness/coder/), our coding harness. What the industry calls a coding harness is, in Pydantic AI, just a capability (technically a bundle of capabilities that turns any agent into a coding agent).

**[Pax](https://pydantic.dev/docs/ai/pax/)** is the terminal UI in front of `Coder()`. Think of it as both a daily-driver coding agent and a showcase of what you can build on the Harness SDK: bring your own agent with `--agent`, swap sandboxes on the fly, and run any model.

## Everything is a plugin

A Pax plugin is just a [capability](https://pydantic.dev/docs/ai/capabilities/overview/) one layer up: tools and hooks for the agent, plus terminal pieces like `/commands`, status-bar items, and logins.

Even the coding agent itself is a plugin. Open `/plugins` to toggle `coder`, `sandbox`, `observability` (Pydantic Logfire tracing), `mcp`, and the rest on or off. Turn `coder` off with `/plugins disable coder` and you have a clean chat client with no file or shell tools. Any Pydantic AI capability works as a plugin by its import path, and Pax can even write new plugins for itself when you ask. See the [Pax plugins docs](https://pydantic.dev/docs/ai/pax/#plugins).

## Bring your own agent with `--agent`

Plugins extend Pax's default agent. `--agent` replaces it with any Pydantic AI `Agent` from your codebase:

```python
# my_agents.py
from pydantic_ai import Agent
from pydantic_ai.capabilities import LocalWorkspace
from pydantic_ai_harness import Coder
reviewer = Agent(
    'openai:gpt-6.1-sol',
    instructions='You review diffs against our internal engineering guidelines.',
    capabilities=[LocalWorkspace('.'), Coder()],
)
@reviewer.tool_plain
def get_guideline(topic: str) -> str:
    """Look up an internal engineering guideline by topic."""
    ...
```
```bash
pax --agent my_agents:reviewer
pax -a my_agents:reviewer -p "Review the diff on this branch against our guidelines"
```
Pax loads no plugins and runs your agent as-is with its own model, tools, and instructions (here `Coder()`'s file and shell tools in the current directory, plus your guideline lookup), while giving you the full terminal (`--resume`, `--worktree`, `-p`, and `-m`). Build an agent in your repo, test it in a real terminal, and ship the exact same `Agent` object in your service. See [Pax in your own code](https://pydantic.dev/docs/ai/pax/#pax-in-your-own-code).

## Sandboxes and workspaces

File system and shell tools talk to a [workspace](https://pydantic.dev/docs/ai/core-concepts/workspace/), so the same agent runs on your machine or in a cloud sandbox without changing any tool code. [Swap `LocalWorkspace('.')` for a sandbox capability](https://pydantic.dev/docs/ai/core-concepts/workspace/#move-it-into-a-sandbox), like [`E2BSandbox`](https://pydantic.dev/docs/ai/harness/e2b-sandbox/), and `Coder()`'s file and shell tools run there instead:

```python
from pydantic_ai import Agent
from pydantic_ai_harness import Coder, E2BSandbox
agent = Agent('anthropic:claude-sonnet-5-5', capabilities=[E2BSandbox(), Coder()])
```
In Pax, you can swap where a session runs **before the first prompt**: `/sandbox e2b` (or [`boxd`](https://pydantic.dev/docs/ai/harness/boxd-sandbox/), [`daytona`](https://pydantic.dev/docs/ai/harness/daytona-sandbox/), [`opensandbox`](https://pydantic.dev/docs/ai/harness/opensandbox-sandbox/), [`modal`](https://pydantic.dev/docs/ai/harness/modal-sandbox/), [`render`](https://pydantic.dev/docs/ai/harness/render-sandbox/), [`sprites`](https://pydantic.dev/docs/ai/harness/sprites-sandbox/), [`kubernetes`](https://pydantic.dev/docs/ai/harness/kubernetes-sandbox/)) for a cloud sandbox, or `/sandbox local smol` / `/sandbox local boxlite` for a local [smol](https://pydantic.dev/docs/ai/harness/smol-sandbox/) or [BoxLite](https://pydantic.dev/docs/ai/harness/boxlite-sandbox/) micro-VM. Pax syncs your branch and uncommitted diff while every edit, build, and `!` command runs inside the sandbox, and [`/resume`](https://pydantic.dev/docs/ai/pax/#pick-up-where-you-left-off-resume) reconnects automatically. On proxy-enabled providers (`e2b`, `boxd`, `daytona`, `opensandbox`), your GitHub token never enters the sandbox; the egress proxy injects it on outbound GitHub requests.

## Computer use

Need more than a shell? Give any agent a full desktop in one line with [`ComputerUse()`](https://pydantic.dev/docs/ai/harness/computer-use/) on [Docker](https://pydantic.dev/docs/ai/harness/docker-container/#give-the-agent-a-desktop) or [any of ten sandboxes](https://pydantic.dev/docs/ai/harness/computer-use/#sandboxes). It uses [OpenAI's](https://pydantic.dev/docs/ai/models/openai/#computer-use), [Anthropic's](https://pydantic.dev/docs/ai/models/anthropic/#computer-use), or [Google's](https://pydantic.dev/docs/ai/models/google/#computer-use) native computer-use tool automatically where supported:

```python
from pydantic_ai import Agent
from pydantic_ai_harness import ComputerUse, DockerContainer
agent = Agent(
    'anthropic:claude-sonnet-5-5',
    capabilities=[DockerContainer(desktop=True), ComputerUse()],
)
result = agent.run_sync('Open Firefox and find the latest Python release on python.org.')
```
The model sees the screen, clicks, types, and gets a screenshot back after each step, all inside the sandbox.

In Pax, computer use is coming in the next release as `/computer-use`: run it in a new conversation before `/sandbox PROVIDER`, and the sandbox starts with a desktop the model can see and control through a `computer` tool. The desktop needs `/permissions full`, and `/computer-use off` takes the tool away again.

## Code mode

Pax turns on [code mode](https://pydantic.dev/docs/ai/harness/code-mode/) by default. Instead of burning turns shuffling results between tools, the model writes a short Python snippet in Monty that searches, reads files, and returns only what matters. Press **Ctrl+X, then Ctrl+S** for [speculative execution](https://pydantic.dev/docs/ai/harness/code-mode/#speculative-execution) so Pax starts safe file reads while the model is still streaming.

![A Pax session after a run\_code call that ran the tests, listed files, read three files, and searched with grep, followed by a three-step explanation of the forecast CLI. The status row reads Speculative Execution, 5 hits, 0 misses, 0 wasted, saved at least 0.2 seconds.](https://pydantic.dev/assets/blog/pax-harness-beta/pax-code-mode.png)


With the `observability` plugin, [Pydantic Logfire](https://pydantic.dev/docs/ai/integrations/logfire/) still traces [every tool call as its own span](https://pydantic.dev/docs/ai/harness/code-mode/#observability).

## Migrating from another coding agent

Already using Claude Code or Codex? `/resume` shows your existing sessions right next to Pax's own, or import one directly with `pax --resume-claude` or `pax --resume-codex` and keep going on any model.

Your repo setup carries over too: `repo_context` reads `AGENTS.md` and `CLAUDE.md`, and the default `coder` plugin loads [Agent Skills](https://pydantic.dev/docs/ai/harness/skills/) from `.agents/skills` and `.claude/skills`. (With standalone `Coder()` in Python, add `Skills()` alongside it if you want skills.)

## How does it compare to other harnesses?

We've been benchmarking Pax against other harnesses on Terminal-Bench and Harness-Bench. Here's one illustrative result: Harness-Bench SWE81 across eight models, holding the model fixed within each comparison (higher score is better; lower cost is better). Pax had the highest average score of the four harnesses that ran every model, narrowly: 58.5, ahead of OpenCode at 58.2, deepagents-code at 57.6, and pi at 57.3. pi was the cheapest, averaging $6.47 a run to Pax's $7.69. Against the native harnesses, Pax cost $9.21 to Codex's $21.05 on GPT-6.2 Sol, and $24.61 to Claude Code's $25.10 on Claude Opus 5.5. Full methodology, more runs and more benchmarks are coming with the 1.0 launch.

*Single runs from November. Sol and Opus use a relaxed rescore applied identically to every harness, and Pax ran Sol with `Coder(autonomy='max')`, the setting for unattended runs that never stop to ask. Full methodology and reruns are coming with 1.0.*

## **Full per-model SWE81 results (8 models, score and cost)**

Score (higher is better):

| Model | Pax | OpenCode | pi | deepagents-code | Codex | Claude Code | 
|---|---|---|---|---|---|---|
| GPT-6 Luna | 55.1 | 57.2 | 53.3 | 55.1 | 56.0 | n/a | 
| GPT-6.1 Terra | 54.1 | 54.7 | 57.2 | 51.4 | 54.2 | n/a | 
| Claude Haiku 5.5 | 56.0 | 55.5 | 52.9 | 59.1 | n/a | 56.5 | 
| Claude Sonnet 5.5 | 58.4 | 60.8 | 57.9 | 57.7 | n/a | 56.9 | 
| MiniMax M3.1 Flash | 54.7 | 50.8 | 52.3 | 50.7 | 54.7 | 38.6 | 
| Kimi K3.1 Pro | 63.7 | 64.3 | 59.1 | 61.5 | 61.8 | 62.9 | 
| GPT-6.2 Sol | 64.7 | 61.0 | 64.8 | 61.7 | 60.1 | n/a | 
| Claude Opus 5.5 | 61.2 | 61.4 | 61.1 | 63.3 | n/a | 60.4 | 

Average cost in USD of one run over all 81 tasks (lower is better):

| Model | Pax | OpenCode | pi | deepagents-code | Codex | Claude Code | 
|---|---|---|---|---|---|---|
| GPT-6 Luna | $0.77 | $0.69 | $0.57 | $1.08 | $1.04 | n/a | 
| GPT-6.1 Terra | $4.97 | $5.41 | $3.97 | $13.79 | $6.36 | n/a | 
| Claude Haiku 5.5 | $1.46 | $1.50 | $1.20 | $1.34 | n/a | $1.37 | 
| Claude Sonnet 5.5 | $7.90 | $7.43 | $6.54 | $7.90 | n/a | $6.86 | 
| MiniMax M3.1 Flash | $1.67 | $2.94 | $1.40 | $2.92 | $1.85 | $2.95 | 
| Kimi K3.1 Pro | $10.92 | $9.81 | $9.44 | $11.88 | $14.42 | $11.40 | 
| GPT-6.2 Sol | $9.21 | $9.17 | $7.69 | $12.98 | $21.05 | n/a | 
| Claude Opus 5.5 | $24.61 | $27.33 | $20.96 | $23.51 | n/a | $25.10 | 

Scores are averaged over graded tasks. Costs use list-price tokens for OpenAI and Anthropic, and OpenRouter billed cost for MiniMax and Kimi. With the stock grader, Pax scored 51.0 on Sol to Codex's 49.8, and 54.9 on Opus to Claude Code's 53.5. In a separate head-to-head on GPT-6.1 Sol, Pax scored 62.4 to Codex's 63.0 for 29% less cost (8.0M vs. 20.8M input tokens per run).

## Try the beta

Run `uvx pydantic-ai-pax` to try Pax without installing it, or `uv tool install pydantic-ai-pax` to keep it. macOS ships with an unrelated `/bin/pax` archiver installed by default, so if `pax` doesn't start Pax right after installing, open a new terminal (or run `rehash` in zsh / `hash -r` in bash) so your shell picks up the new `PATH` entry, or run `pydantic-ai-pax` directly.

Rather build your own harness? Start with the [Harness docs](https://pydantic.dev/docs/ai/harness/).

We're heading toward 1.0 next month, so tell us what breaks and what you want to see in V1: [join our Slack](https://pydantic.dev/docs/logfire/join-slack/) or [file an issue](https://github.com/pydantic/pydantic-ai/issues).
