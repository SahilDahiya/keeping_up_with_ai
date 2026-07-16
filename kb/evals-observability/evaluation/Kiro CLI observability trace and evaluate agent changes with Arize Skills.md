---
title: 'Kiro CLI observability: trace and evaluate agent changes with Arize Skills'
kind: blog
topic: evals-observability
subtopic: evaluation
secondary_topics:
- agents/tool-use
summary: 'Walks through pairing Amazon''s Kiro CLI coding agent with Arize Skills
  to build a validation loop: instrument an app, export traces, build a regression
  dataset from production failures, and run an experiment comparing the current implementation
  against an agent-proposed revision before merging.'
triage: null
skip_reason: null
source: arize
url: https://arize.com/blog/kiro-cli-observability-arize-skills/
author: Richard Young
published: '2026-07-15'
fetched: '2026-07-16T06:48:54Z'
classifier: claude
taxonomy_rev: 2
words: 1984
content_sha256: 7802b946c7c5be1089df625325dc3d3adb747f05f6e6ee1325179a6edbc1e3ac
---

# Kiro CLI observability: trace and evaluate agent changes with Arize Skills

*Co-authored by Rich Young, Director of Partner Solutions Architecture, and Nolan Chen, AWS Partner Solutions Architect*

Coding agents can now inspect a codebase, plan work, edit files, run commands, and ship complex changes in a single session. But faster code generation creates a new problem: teams still need to prove that an agent-generated change improved quality, reliability, latency, or cost before it ships. The bottleneck has moved from writing code to verifying that the agent’s changes are actually better than what came before.

That is the gap Arize Skills and Kiro CLI close together. Kiro CLI is Amazon’s terminal-based coding agent for turning natural-language instructions into codebase changes. Arize Skills give that same agent a packaged way to instrument code, export traces, build datasets, run experiments, and optimize prompts, all through natural language. Together, they create a validation loop for coding-agent work: make the change, trace the behavior, test it against real failures, and decide whether it should merge.

### What you’ll do in this guide

By the end, you will have:

- Kiro CLI running in a local project.
- Arize Skills installed for your coding agent.
- Arize tracing added to an app or notebook.
- A dataset built from representative production failures.
- An experiment comparing the current implementation against a proposed revision.
- Optional tracing for Kiro CLI itself, including tool calls, turn duration, context usage, model name, and credit cost.

## Why coding agents need evaluation, not just faster code generation

The first wave of coding agents was about output volume. The next step is evaluation. When an agent edits a prompt, a tool wrapper, retrieval logic, and three files of application code in the same run, the old “skim the diff, run a few local tests, and hope nothing regressed” loop falls apart.

What teams need is a way to express intent once, let the agent execute against it with guardrails, and measure the result on a representative dataset before it ships. Kiro covers the first two. Arize Skills cover the third without making the developer hand-roll a separate eval pipeline. The result is a workflow where agent-generated changes can be evaluated against traces, datasets, and experiments before they land in production.

## What is Kiro CLI? What are Arize Skills?

[Kiro CLI](https://kiro.dev/cli/) is a terminal-based coding agent. You launch a chat session and Kiro reads your project, runs commands, edits files, and drives multi-step work from natural-language prompts. It handles the gap between intent and implementation across a real codebase.

[Arize Skills](https://arize.com/docs/ax/set-up-with-ai-assistants#arize-skills-and-mcp) are packaged Arize workflows that any coding agent can invoke. They encode the recipes Arize built running its own observability and evaluation platform: how to instrument an app, export traces, create evaluators, build a regression dataset from failures, run an experiment, and optimize a prompt from eval feedback. The agent calls the skill in plain language. The skill handles the `ax` CLI flags, the data shape quirks, and the multi-step orchestration underneath. Arize ships them on GitHub and updates them as the platform evolves. Arize Skills are provider-agnostic. They work with any model, any framework, and any orchestrator your Kiro-driven workflow happens to touch.

In practice, that means a developer can ask Kiro CLI to make a change, then ask the same agent to use Arize Skills to prove whether the change improved.

### What you can do with Arize Skills

| Developer job | Arize Skill | Example prompt | 
|---|---|---|
| Add tracing to an app | arize-instrumentation | “Instrument app.py with Arize tracing and show me the diff before applying it.” | 
| Inspect production failures | arize-trace | “Export the last 100 failed traces and group them by root cause.” | 
| Build a regression dataset | arize-dataset | “Create a dataset from traces where groundedness failed.” | 
| Compare two versions | arize-experiment | “Run the current prompt and answer_prompt_v2.md against this dataset.” | 
| Add evaluators | arize-evaluator | “Create groundedness and answer-correctness evaluators for this experiment.” | 
| Improve prompts | arize-prompt-optimization | “Suggest a revised prompt based on failed examples and rerun the experiment.” | 
| Trace Kiro CLI itself | Coding Harness Tracing | “Install Kiro CLI tracing so I can inspect tool calls, cost, and context usage.” | 

## How Arize Skills evaluate Kiro CLI changes

Kiro CLI and Arize Skills work well together because they split the coding-agent workflow into two clear phases. Kiro moves the team from intent to implementation. Arize Skills move the same agent from implementation to evidence. The Kiro coding agent that updated the prompt is the same agent that ran the experiment and read the regression report.

Here is how that looks in practice.

### 1. Install Kiro CLI, the Arize AX CLI, and Arize Skills

One-time setup on the machine where you build agents. Run this once in the environment where Kiro CLI will edit and evaluate your project.

```
# Install Kiro-CLI, then authenticate with your Builder ID
kiro-cli –version
kiro-cli login –use-device-flow
# Install uv and the Arize ax CLI, then create a profile for auth
curl -LsSf https://astral.sh/uv/install.sh | sh
uv tool install arize-ax-cli
ax profiles create
# Install Node (for npx) and add the Arize Skills plugin
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.1/install.sh | bash
source ~/.bashrc && nvm install –lts && nvm use –lts
npx skills add Arize-ai/arize-skills
```
<
[Install instructions for Kiro CLI](https://builder.aws.com/content/39YT1HHBp9sbuT1dZK9ZMaMcJDb/how-to-install-amazon-q-cli-kiro-cli-on-a-linux-machine-local-laptop-and-ec2-instance) are on the AWS Builder Center. After this runs once, every Arize skill is available to the Kiro agent by name.

### 2. Add Arize tracing from Kiro CLI

Launch Kiro and ask it to run the instrumentation skill against the file you want to trace. For example, start with the app entry point, notebook, or agent file where model calls are made.

```
kiro-cli
```
```
> Instrument “app.py” with Arize tracing. Detect the framework and model provider, add the right OpenInference instrumentation, and show me the diff before applying it.
```
The Kiro agent invokes the arize-instrumentation skill, detects the model provider and framework, adds the `register()` function plus the right OpenInference instrumentor, and prepares the code change for review. You review the change before it lands.

![Kiro CLI terminal running the Arize instrumentation skill: reading notebook files, fetching Arize docs, and planning the tracing setup cells to add.](https://arize.com/wp-content/uploads/2026/07/kiro-cli-arize-instrumentation-skill.png)

### 3. Turn production traces into debugging evidence

Once traces are flowing, point Kiro at the trace data. The goal is to move from “something regressed” to a concrete set of failure categories you can test against.

```
> Export the last 200 traces from my production RAG agent where groundedness failed or the trace ended in an error. Group the failures by root cause and include example trace links for each category.
```
The skill runs `ax traces export` under the hood, pulls the spans, and Kiro reads the output and reports patterns. Instead of manually searching through traces, the agent can turn failures into a short debugging brief: what broke, how often it happened, and which examples should become regression tests.

### 4. Build a dataset and run an experiment

Once failures are grouped, turn them into a regression dataset and compare the current implementation against the proposed change.

```
> create a dataset from the category [category]
> create an experiment to run the current prompt and a proposed revision
  against that dataset. create a groundedness evaluator and evaluate experiments
```
## Trace Kiro CLI itself with Arize for transparency and cost visibility

Everything above measures the agents you build with Kiro CLI. Arize also traces Kiro CLI itself, so you can see what the coding agent is doing on your behalf, how long each turn takes, and what it costs. This is useful when a coding-agent session becomes slow, expensive, or hard to audit.

The Arize Coding Harness Tracing project installs hooks on a Kiro agent and exports OpenInference spans to Arize AX. Install it with one command:

```
curl -sSL https://raw.githubusercontent.com/Arize-ai/coding-harness-tracing/main/install.sh | bash -s — kiro
```
The installer prompts for your Space ID, API key, and an agent name (default `arize-traced`), then wires the hooks. Set the traced agent as the default and Kiro CLI runs it automatically:

`kiro-cli chat`In Arize, inspect:

- **Turn traces.**Each user prompt to Kiro CLI response is a parent LLM span. Tool calls hang off it as child spans, matched from- `preToolUse`and- `postToolUse`hooks.
- **Session grouping.**Every turn in the same session shares a- `session.id`, so a long working session shows up as one trace tree.
- **Credit cost.**Kiro CLI meters in credits rather than tokens. The harness captures cost per turn as- `kiro.cost.credits`plus the full metering payload, so you can roll up by session, user, or day.
- **Model and duration.**- `llm.model_name`,- `kiro.turn_duration_ms`, and- `kiro.context_usage_percentage`show which model handled the turn, how long it took, and how much of the context window is in play.

That gives you the same observability surface you would want for any production agent applied to the coding agent harness itself. You can debug a slow turn, attribute spend by team, and watch context usage climb before a long session hits its ceiling. [Redaction flags](https://arize.com/docs/ax/integrations/platforms/kiro/kiro-tracing#redaction-controls) (`ARIZE_LOG_PROMPTS`, `ARIZE_LOG_TOOL_DETAILS`, `ARIZE_LOG_TOOL_CONTENT`) keep sensitive prompt or tool output out of the trace when you need them off.

## What Kiro CLI observability changes for developers and engineering teams

For developers, verification stops being a separate job. The agent you already use for code edits also pulls traces, builds datasets, and runs experiments. The workflow stays inside the coding session, but the decision is grounded in production evidence.

For engineering leaders, agent-driven changes become measurable when teams make experiments part of the merge path. Every experiment ships with an ID and a regression report. Decisions about which workflows to hand to agents move from intuition to numbers.

For the broader system, the cycle time between idea, implementation, and validation gets short enough to be useful. The agent does more autonomous work. The team does more high-value engineering. The more important shift is that the team can measure whether agent-written code improved the system.

## Getting started

Three things to set up before the loop pays off:

- Install Kiro CLI, the Arize AX CLI, and Arize Skills. Authenticate with `kiro-cli login`and`ax profiles create`.
- From Kiro CLI, instrument one target notebook, app file, or agent entry point with arize-instrumentation.
- Use arize-trace to export 20 to 50 representative failures from production traces.
- Create a regression dataset with arize-dataset.
- Run arize-experiment to compare the current implementation against the proposed change.
- Use the experiment report to decide whether the agent-generated change should merge.

After that, every meaningful agent-generated change can end with an experiment in Arize and a list of failures the next iteration can fix.

## Resources

- [Kiro CLI install guide on AWS Builder Center](https://builder.aws.com/content/39YT1HHBp9sbuT1dZK9ZMaMcJDb/how-to-install-amazon-q-cli-kiro-cli-on-a-linux-machine-local-laptop-and-ec2-instance)
- [Arize Skills and MCP setup for coding agents](https://arize.com/docs/ax/set-up-with-ai-assistants)
- [Arize Coding Harness Tracing for Kiro CLI](https://arize.com/docs/ax/integrations/platforms/kiro/kiro-tracing)
- [Guide to tracing coding agents](https://arize.com/docs/ax/cookbooks/instrument/tracing-coding-agents)
- [GitHub: Arize Skills](https://github.com/Arize-ai/arize-skills)
- [GitHub: Coding Harness Tracing](https://github.com/Arize-ai/coding-harness-tracing)
- [Redaction flags for Harness Tracing](https://arize.com/docs/ax/integrations/platforms/kiro/kiro-tracing#redaction-controls)

## FAQ

### What is Kiro CLI observability?

Kiro CLI observability means tracing coding-agent sessions so developers can inspect prompts, tool calls, model responses, latency, context usage, and cost. With Arize Coding Harness Tracing, Kiro CLI sessions can be exported as OpenInference spans to Arize AX.

### How do Arize Skills help Kiro CLI users?

Arize Skills give Kiro CLI reusable workflows for adding tracing, exporting traces, creating datasets, running experiments, creating evaluators, and optimizing prompts through natural-language instructions.

### How do you evaluate a Kiro CLI code change before shipping?

Use Kiro CLI to make the code or prompt change, then use Arize Skills to build a regression dataset from real traces and run an experiment comparing the current version against the proposed version.

### Can Arize Skills work outside Kiro CLI?

Yes. Arize Skills are designed for coding-agent workflows and can be used with other AI coding agents that support Skills-style workflows.
