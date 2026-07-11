---
title: 'From observability to context: What’s next for Arize Phoenix'
topic: evals-observability
subtopic: tracing
secondary_topics:
- agents/memory-context
summary: Connects LLM observability with context management, showing how traces and
  application state can become reusable context for better agents.
source: arize
url: https://arize.com/blog/from-observability-to-context-whats-next-for-arize-phoenix/
author: Mikyo King; Elizabeth Hutton
published: '2026-05-11'
fetched: '2026-07-11T04:55:56Z'
classifier: codex
taxonomy_rev: 1
words: 2937
content_sha256: 99ba97c11b10527ddfe06e80020af54d649b417f5549f87c86eb3c18e6e64a61
---

# From observability to context: What’s next for Arize Phoenix

*Co-Authored by Mikyo King, Head of Open Source & Elizabeth Hutton, Senior AI Engineer.*

*As agents start changing software, they need a way to verify their work that includes traces, evals, feedback, and APIs. This is where Phoenix goes next — not the next release, but what this product becomes.*

Observability was built for a world where humans did the reasoning. A human deployed code, reviewed traces, triaged alerts, and diagnosed failures. The tooling reflected that workflow: dashboards, filters, alerts, and evaluation pipelines. All of it assumed a human in the loop.

That assumption is rapidly breaking. Agents are becoming operators, too. They write code, change prompts, call tools, and modify systems. But they cannot work from tools designed only for human inspection. They need usable context: traces, evals, feedback, experiments, and annotations they can query, interpret, and act on.

That is what we are building with [Phoenix](https://phoenix.arize.com/): not just observability for humans, but a context platform for humans and agents to build great AI-native software together.

**TL;DR**

- Coding agents need feedback loops to verify whether their changes actually improved system behavior.
- Traces, evals, experiments, and feedback are becoming the verification layer for agentic systems.
- Context cannot live only in dashboards; it needs to be accessible through APIs, CLIs, and agent-facing interfaces.
- The goal is to close the loop so agents can self improve: trace, eval, diagnose, fix, and rerun
- We believe AI observability is evolving into a context platform where humans and agents will debug and improve systems together.

**The evolution of software engineering**

![Diagram titled “Who consumes telemetry data?” showing three side-by-side phases of software evolution and how telemetry flows through observability systems. Phase 1: Software 1.0 Flow: Application → Observability Platform → Human Dev → IDE. The application sends telemetry to the observability platform, which is read by a human developer who writes code in an IDE and deploys updates back to the application. Caption: “Human is the sole consumer of telemetry.” Phase 2: Software 2.0 Flow: Application → Observability Platform → Human Dev → Agentic IDE containing a Coding Agent (Claude Code / Cursor). The human developer prompts the coding agent inside the IDE to write code, then deploys updates back to the application. Caption: “Human prompts, agent writes code inside IDE.” Phase 3: Autonomous Flow: Application → Observability Platform → Coding Agent (Claude Code / Cursor) → Human. The coding agent directly reads telemetry from the observability platform, iterates autonomously, and only notifies the human, who “monitors only.” Caption: “Agent autonomously consumes telemetry.” Bottom callout text: “Observability platforms must evolve from human dashboards to programmatic interfaces that agents can consume.”](https://arize.com/wp-content/uploads/2026/05/phoenix-blog-image-2-dad053d76c9a.png)

Two things changed at once.

First, agents started writing and modifying a lot of code. Six months ago, most of us coded by hand with occasional AI assist. Now, many of us are running multiple agents in parallel, and stepping in only when careful scrutiny is needed. But the infrastructure around these workflows hasn’t fully caught up. A coding agent can generate changes, but it often has no effective way to determine whether those changes actually improved the AI system’s behavior.

At the same time, AI-native software is increasingly becoming the norm. Today’s software involves more than just code. You have code, prompts, and model weights. In these systems, you can’t review behavior before it runs. You can only observe it after.

For agents to close the loop, they need verification. For humans to trust agent-generated changes, those agents need to produce evidence and share context: traces, eval results, experiment comparisons, and failure examples. That evidence can’t just live in dashboards. It needs to be available through programmatic interfaces like APIs, CLIs, and other agent-accessible endpoints so agents can inspect what happened, reason over failures, and prove whether their changes worked.

**Why traces matter more when behavior is non deterministic**

![Comparison diagram contrasting “Traditional Software” with “AI Agent” workflows. On the left, a panel titled “Traditional Software” with subtitle “You can read the logic.” A flowchart shows a deterministic code path: handleSubmit() leads to a decision diamond labeled “valid?” If “no,” flow goes to an “Error” box. If “yes,” flow goes to callAPI() Another decision diamond labeled “status?” branches: “500” leads to retry() “200” leads to save(), then Done Caption at bottom: “Every path is visible. Deterministic. You see it all before it runs.” In the center is “vs.” On the right, a panel titled “AI Agent” with subtitle “You can’t read the logic.” A diagram shows: agent.run(query) feeding into a central “LLM” node with the text “What should I do?” The LLM may choose actions like search(), write(), or analyze(), each labeled “maybe?” Additional loops connect to smaller LLMs and “Sub-Agent 1” and “Sub-Agent 2,” with annotations like “loop back” and “more loops.” All paths eventually lead to an “Output” box labeled “different every time.” Caption at bottom: “You can’t see any of this in the code. You only see it after, in the traces.” At the bottom of the overall graphic, an arrow labeled “source of truth shifts” points from a blue “Code” box to a green “Traces” box.](https://arize.com/wp-content/uploads/2026/05/phoenix-blog-image-3-a995bf66a223.png)

In traditional software, you can read the code. Every path a program might take is visible and deterministic; you see it all before it runs. In an agent, you can’t. Decisions happen inside the model at runtime and are different every time even when the context and prompts are exactly the same. You only see the outcome after it’s already been decided within the traces.

That means the source of truth has shifted from code to traces. Traces offer a record of each LLM call, tool invocation, routing decision, retrieved document, latency spike, and failure. They’ve become the substrate for evals, experiments, debugging, and regression analysis..

Without programmatic access to traces, an agent can change an agentic application but cannot reliably inspect whether the application behaved better after the change..

This is not abstract. When a coding agent produces a change to an agentic application, the only record of what that application *did* — its decisions, its tool calls, its outputs — lives in the traces. Source code tells you what *could* happen. Traces tell you what *did*. In a non-deterministic system, the latter matters more.

Phoenix is already vendor-agnostic with OpenTelemetry-based conventions that work across every major framework and provider. The traces are there. The question is what we do with them next.

**From observability platform to a context platform**

Every previous platform category was defined by what it observed: ML metrics, LLM inputs and outputs, agent trajectories, and so on.

The next useful layer is defined by what it enables with shared context humans and agents can both query and act on. It should hold the context including traces, evals, annotations, feedback, experiments, and expose it to both humans and agents so they can act on it.

Not an ML platform, LLM platform, or an agent platform. A context platform.

The distinction matters because it changes what we build. An observability platform optimizes for human consumption with dashboards, visualizations, and alerting rules. A context platform optimizes for *both* human and programmatic consumption. It should expose GraphQL APIs, CLI interfaces, MCP endpoints, and other surfaces where agents can query traces, correlate failures, and reason over eval results without a human intermediary.

We started building toward this with the Phoenix CLI earlier this year. That’s because AI coding assistants operate through the terminal and the filesystem. A browser-based UI is useful for humans, but inaccessible to an agent working in your IDE. Programmatic interfaces need to meet agents where they already are.

**Context should lead to action**

But a context platform that only serves dashboards is still waiting for a human to act. The next step is transforming context into action. We need to turn observability into something that doesn’t just describe what happened, but participates in fixing it.

This is the product thesis that drives everything that follows.

**Agent evals**

If traces are the source of truth and the platform’s job is to turn context into action, evaluation is where it starts.

**The evaluation surface area is expanding**

![Framework diagram showing increasing complexity of AI evaluation systems across two axes. The vertical axis on the left is labeled “eval inputs” with an upward arrow. Input types increase from bottom to top: input / output reference full trajectory sandboxes repetitions ops metrics change history The horizontal axis along the bottom is labeled “what’s under test” with a rightward arrow. Categories increase from left to right: prompt tools security orchestration context mgmt environment infra self-reflection Four overlapping dashed rectangles represent progressively larger evaluation scopes: LLM (small purple box in lower-left) Covers mostly prompt and tools. Caption: “Is the output correct?” Agent (larger blue box surrounding LLM) Expands into orchestration and context management. Caption: “Did it make the right decisions?” Harness (larger teal box surrounding Agent) Extends into environment and infrastructure testing. Caption: “Does the system work reliably?” Fully Autonomous Agents (largest green box surrounding all others) Extends furthest across infrastructure and self-reflection, and highest on the eval-input scale. Caption: “Does it get better over time?” The overall graphic illustrates how evaluating AI systems evolves from simple LLM output checking to broader system-level and autonomous-agent evaluation requiring richer inputs and wider operational coverage.](https://arize.com/wp-content/uploads/2026/05/phoenix-blog-image-4-34d7264efaa8.png)

The evaluation problem is expanding along two dimensions simultaneously. On one axis, what’s being evaluated is growing from prompts and model outputs into tools, security, orchestration, context management, environment interaction, infrastructure, and self reflection. On the other axis, the eval inputs themselves are growing richer and evolving from simple input/output pairs to full trajectories, sandboxed execution, repetition analysis, ops metrics, and change history.

At the LLM level, the question is straightforward: *is the output correct?* But at the agent level, it’s more nuanced: *did it make the right decisions?* At the harness level, the question is more operational: *does the system work reliably?* And for fully autonomous agents, the question we’re ultimately building toward is self-improvement: *does it get better over time?*

The surface area of what needs evaluation is outpacing what a single LLM call can assess.

**Moving from LLM-as-a-Judge to Agent-as-a-Judge**

![Comparison diagram contrasting “LLM as a Judge” with “Agent as a Judge.” On the left, under the heading “LLM as a Judge” with subtitle “Single pass”: Three input boxes labeled “Input,” “Output,” and “Criteria” point into a central purple circle labeled “LLM.” The LLM produces a final box labeled “Label, score, explanation.” The flow represents a one-step evaluation process where a model directly grades an output based on provided criteria. On the right, under the heading “Agent as a Judge” with subtitle “Iterative evaluation”: A central purple circle labeled “Agent” is connected to multiple surrounding components: “Traces” “Sandbox” “Subagents” “Feedback” “Multi-criteria evals” “Tools” “Context” Arrows show the agent interacting iteratively with these systems and evaluation inputs. The layout emphasizes a more dynamic, multi-step evaluation process involving tools, environments, feedback loops, and multiple evaluation dimensions. A dotted vertical line separates the two approaches, highlighting the shift from simple single-pass LLM judging to more complex agentic evaluation systems.](https://arize.com/wp-content/uploads/2026/05/phoenix-blog-image-5-c80046f6d7fd.png)

Evaluation strategies naturally evolve to match the complexity of what they measure. [LLM-as-a-Judge](https://arize.com/llm-as-a-judge/) emerged when generative outputs broke the assumption of a single right answer. That’s because LLM’s are flexible enough to capture subjectivity and customizable along the axes of quality teams actually care about.

But this approach is shaped for outputs LLMs produce in isolation: input/output pairs that fit cleanly into a prompt. A single pass with input, output, criteria in; and label, score, explanation out.

Agentic systems are the next step. Agents don’t produce outputs in isolation; they interact with tools, environments and humans, operating in a long-running loop. Evaluation agents fit this shape because they share it: iterative reasoning, tool use, context management, sub-agents, the ability to run code and verify outputs. The same capabilities that make agents useful in production make them well-suited to evaluating other agents.

This is where Phoenix’s role as a context platform becomes concrete. The evaluator agent consumes the same traces, experiment data, annotations, and feedback the rest of the system produces. In that way, evaluation becomes a consumer of the platform’s context like everything else instead of a separate workflow.

**Closing the loop: trace, eval, fix, rerun**

Everything we’ve discussed from traces as source of truth to the context platform, agent evals, and sandboxes converges on a single architectural goal: pulling verification into the agent loop itself.

**Building verification into an agent loop**

![Workflow diagram showing how an agentic application integrates with Arize Phoenix and a coding agent to create an automated feedback loop for debugging and improvement. On the left: A box labeled “Agentic App” sends data into an “Arize Phoenix” section. The Phoenix section contains three stacked components: “Traces” “Evaluation” “Feedback” Text beside the arrows reads: “Traces, Evaluation, Feedback.” In the center: Outputs from Arize Phoenix flow into a box labeled “Phoenix CLI.” On the right: The Phoenix CLI connects to a green box labeled “Coding Agent.” Text above the connection reads: “Query, Correlate, Reason.” The Coding Agent connects downward to a box labeled “CODEBASE.” Text on that connection reads: “Implement change (PR) + Restart App.” A circular feedback loop appears on the far right: The CODEBASE re-runs the workload. A “test” step feeds back into the “user journey.” The user journey returns to the Coding Agent. Green text beside the loop reads: “Feedback Loop.” The overall diagram illustrates an automated development cycle where telemetry, evaluations, and feedback from Phoenix help a coding agent reason about issues, modify the codebase, rerun workloads, and iteratively improve the application.](https://arize.com/wp-content/uploads/2026/05/phoenix-blog-image-6-6e5655365ed6.png)

Here’s how it works concretely:

- An agentic application emits traces, evaluation results, and feedback into Phoenix.
- A coding agent like Claude Code, or Cursor queries Phoenix through the CLI or API to understand what went wrong.
- The coding agent correlates traces with eval failures, reasons over the context, implements a change, commits it, and re-runs the workload.
- The new traces flow back into Phoenix and the loop starts again.

The early pieces of this workflow already exist. The Phoenix CLI already supports `px traces` for fetching trace data, `px api graphql` for arbitrary queries against the Phoenix backend, and agent skills that teach coding agents how to interpret trace data and diagnose failures. The next step is connecting these pieces into a continuous loop.

**Moving towards self-improving agents and self-improving systems**

Agents are rapidly gaining the ability to evolve themselves. The next step is self-improving agents and self-improving systems. To get there, we need tools, guardrails, and triggers that initiate improvement cycles, context to reason over, and CI gates that enforce quality before changes ship.

The core principle: **make coding agents prove their work.** Don’t trust that an agent’s change is correct. Instead, we need to require that agents demonstrate correctness through traces, evals, and experiments. Phoenix becomes the verification layer in this loop, or the infrastructure through which agents produce evidence and humans audit it.

**Agents debugging agents**

This brings us to the deeper implication. If agents can query traces, run evals, and reason over feedback, then agents can debug other agents. The human doesn’t disappear. They supervise. But the diagnostic work shifts.

**Active and passive modes**

Phoenix sits at the center of two interaction patterns:

- In the *active*mode, a human directs an agent through Phoenix by querying traces, running evals, iterating on changes with the agent as a collaborator.
- In the *passive*mode, an autonomous agent or assistant works proactively to surface issues and propose changes while the human reviews.

Both modes require the same infrastructure: shared context, programmatic access, and mechanisms for agents to present evidence of their reasoning. The difference is who initiates and iterates.

Over time, more workflows may shift toward the passive model. But the platform needs to support both modes because trust is contextual: teams will delegate more when failure modes are well understood, and retain tighter control when the stakes are high.

**Phoenix Intelligence**

This is where the product work converges: Phoenix Intelligence, an agent layer built directly into the platform.

We envision two tiers:

- **An assistant helps you along your AI engineering journey.**This includes human-in-the-loop collaboration for debugging, dataset generation, eval design, and experiment setup. It meets you where you are, whether you’re a PM exploring production data or an ML engineer optimizing retrieval.
- **The**They research your use case, alert you about regressions, run evaluations, and surface insights continuously inside your observability platform.- *experts*autonomously work as specialized agents from our observability context.

Agents building agents, improving agents, observed by agents. The platform that holds the context *is* the platform that acts on it. That’s the thesis, and what we’re building.

**Final thought: the dial of delegation**

None of this means engineering is dead. In fact, it’s quite the opposite. As agents take on more of the verification work, what they can’t take on becomes more valuable: the judgment about when to trust them, what to delegate, and what to keep close.

The dial of delegation is a human decision. The teams that learn to turn it carefully by pulling back when the stakes are high and lean in when the patterns are well understood are the ones that will move fastest. Trust isn’t given to agents; it’s earned. The engineers who calibrate it well will define what their organizations can do.

** Phoenix is an open source platform for agent development and evaluation.** The CLI, tracing infrastructure, eval framework, and OpenInference conventions all ship in the open. What comes next builds on that foundation. If you’re thinking about these problems, we’d love to hear from you.

*– The Arize Open Source Team*
