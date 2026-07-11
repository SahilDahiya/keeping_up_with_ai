---
title: 'Building the AI factory for self-improving agents: What’s new in Arize AX'
topic: evals-observability
subtopic: monitoring
secondary_topics:
- agents/planning
summary: Introduces Arize AX updates aimed at building an AI factory for self-improving
  agents through traces, evals, and feedback loops.
source: arize
url: https://arize.com/blog/building-ai-factory-self-improving-agents-arize-ax/
author: Jason Lopatecki; Aparna Dhinakaran
published: '2026-06-04'
fetched: '2026-07-11T04:56:32Z'
classifier: codex
taxonomy_rev: 1
words: 1419
content_sha256: c3761466054f39c0e817083054a23daafa0593dd24304033deedaf00b9543c5d
---

# Building the AI factory for self-improving agents: What’s new in Arize AX

*Co-Authored by Jason Lopatecki, Co-founder and CEO & Aparna Dhinakaran, Co-founder & Chief Product Officer.*

Production agents often fail in two ways: obvious failures you can alert on (timeouts, tool errors, 5xxs) and nuanced agent failures that aren’t deterministic and require intelligent examination of the agent trajectory (wrong retrieval, bad tool args, skipped steps, plausible answers built on bad reasoning).

Once a failure is identified, teams still need to investigate traces, understand what changed, identify the root cause, decide on a fix, and verify the outcome. Today, most of that work remains manual.

At our annual conference, Observe 2026, we’re launching new Arize AX capabilities that make the agent improvement loop more automated and repeatable. Our vision is one where observability plays the foundational role in the AI factory for self-improving agents.

As agents increasingly help build and automate workflows and augment knowledge work, teams need a way to improve those systems at the same pace they’re being developed.

**TL;DR: What’s new in Arize AX**

At Arize: [Observe 2026](https://arize.com/observe/), we’re launching new capabilities designed to help teams close the agent feedback loop in production: detect failures, investigate root causes, test fixes, and automatically improve behavior over time.

- **Signal**
- **Managed agents**- **:**Run fleets of repo-aware agents that can investigate failures, use skills, propose fixes, create evals, catch security issues, and custom workflows.
- **Swarm observability**
- **Agent experiments**- **:**Compare complete agent system behavior across runs, including tool use, retrieval quality, latency, trajectories, and eval results. This moves experimentation beyond prompt testing into full-harness testing.
- **Agent-as-a-Judge**- **:**Generate adaptive eval signals directly from production behavior. Instead of relying only on predefined rubrics, teams can let agentic judges inspect traces, identify emerging failure modes, and create reusable labels for monitoring and evaluation.
- **Voice agents**- **:**Observe, search, replay, and evaluate voice conversations with support for audio sessions, transcripts, and multimodal traces.

**Why agent improvement needs a feedback loop **

Shipping the first version of an agent is faster than ever. The challenge is turning agent improvement into a repeatable engineering process for AI systems at production scale.

Production traffic exposes edge cases that pre-release tests miss. Some failures are obvious: timeouts, tool errors, broken JSON, or 5xxs. Others are harder to catch: the agent retrieves the wrong context, skips a required step, passes the wrong arguments to a tool, or returns a plausible answer built on bad reasoning.

Fixing those issues requires more than a trace. Teams need to connect the full path from production behavior to an engineering change: the trajectory, eval result, dataset row, prompt or code diff, retrieved context, tool response, and deployment history.

When that context lives across different tools, improvement becomes a manual research project. Engineers search traces, rebuild datasets, rewrite evals, inspect logs, check repo history, and run experiments by hand.

Arize AX is designed to make those steps part of one engineering workflow for continual improvement:

- The trace shows what happened
- Evals and judges turn behavior into signal
- And managed agents help move from signal to investigation and proposed fix.
- Experiments test whether the change helped

![](https://arize.com/wp-content/uploads/2026/06/signal-arize-managed-agents.png)

Today, we’re releasing several new capabilities. Let’s jump in.

**Signal: continuous investigation for production agents**

As agent traffic scales, human review does not. A team can spot a problem in one trace, but finding recurring patterns across thousands or millions of traces quickly becomes impossible.

[ Signal](https://arize.com/docs/ax/agents/get-started-with-signal) is an always on AI worker that continuously reviews new production traces, remembers previously identified issues, and surfaces new failure patterns as they emerge. It groups related traces into investigation reports with a summary, root-cause analysis, impact, and suggested next steps.

The goal is to move teams from reactive debugging to continuous investigation. Instead of waiting for a monitor to fire, teams can wake up to a prioritized list of issues, evidence, and recommended actions.

![Arize AI Signal agent](https://arize.com/wp-content/uploads/2026/06/signal-scaled.png)

Signal is also the easiest way to start using managed agents in Arize AX. Teams can enable it with minimal setup, then extend the workflow with repo access, custom skills, automations, and agent-driven fixes over time.

**Managed agents**

Long-running agents are emerging as a new operational layer for AI factories. Instead of answering a single prompt, they investigate issues over time, gather context across tools and codebases, and return with recommendations or proposed fixes.

With Arize AX, teams can [orchestrate repo-aware managed agents](https://arize.com/docs/ax/agents/agent-studio) that inspect traces, access external systems, analyze code, create investigation artifacts, and propose changes as pull requests for human review. These agents can be customized to engineering workflows such as regression triage, debugging production behavior, dataset curation, eval generation, security reviews, and code remediation.

Teams can start with prebuilt workflows or create their own using configurable harnesses, sandboxes, repositories, skills, and automations. The result is a flexible system for delegating repetitive investigation and analysis work while keeping engineers in control.

These workers are not autonomous production agents making changes on their own. They investigate, gather evidence, and propose actions that engineers can review, approve, modify, or reject.

**Swarm observability**

As teams deploy more AI workers, they need visibility into what those agents are doing, how they’re performing, and what resources they’re consuming. [Swarm observability](https://arize.com/docs/ax/agents/manage-agents) provides a centralized view of managed agents across the organization, including status, activity, trajectories, token usage, and cost. Teams can track long-running investigations, understand agent behavior over time, and manage their growing fleet of AI workers from a single pane of glass.

**Agent experimentation: test the full agent harness**

Prompt testing is useful, but production agents are not just prompts.

They are systems made of tools, retrieval, routing, memory, models, fallbacks, application code, and business logic. A small change in any layer can improve one behavior while breaking another.

[ Agent experimentation](https://arize.com/docs/ax/improve/agent-experiments-overview) in Arize AX is the verification step in the loop. Teams can run curated datasets through the full agent system, then compare outputs, traces, and evals across runs to understand whether a change improved behavior or introduced a new regression.

This matters because the meaningful diff for an agent is behavioral. Did tool use improve? Did latency change? Did retrieval quality hold? Did the model upgrade improve final-answer quality while making tool calls less reliable? Did the fix solve the target failure without breaking another task class?

You answer those questions by running the system, capturing the trajectory, scoring the behavior, and comparing runs.

**Agent as a judge**

Traditional LLM judges work best when teams already know what they’re looking for. Agent failures are rarely that predictable. New failure modes emerge as agents interact with tools, users, and changing environments in production.

[Agent-as-a-Judge](https://arize.com/docs/ax/evaluate/harness-as-a-judge) helps the agent improvement loop adapt when production reveals failure modes the team did not predefine. Teams can describe good behavior, let an agentic judge inspect traces, identify relevant spans, classify issues, and create labels for future monitoring, evaluation, and experimentation. The goal is eval signal that keeps up with what is actually breaking.

**Voice agent support**

[Voice agents](https://arize.com/docs/ax/cookbooks/evaluation/tracing-and-evaluating-audio) introduce a new layer of complexity beyond text: audio streams, interruptions, speech latency, transcription quality, and multimodal interactions all become part of the agent experience.

Arize AX now provides native support for observing, searching, replaying, and evaluating voice conversations. Teams can inspect audio sessions alongside transcripts and traces, analyze interruptions and time-to-first-audio, replay conversations end-to-end, and run evaluations directly against audio interactions.

[Arize AX audio support for agents](https://arize.com/wp-content/uploads/2026/06/audio-support.mov)

By bringing voice conversations into the same observability and evaluation workflow as text agents, teams can debug, monitor, and improve conversational AI systems with the same rigor they apply to the rest of their agent stack.

**What this changes for AI engineering teams**

As agents become more capable, the bottleneck shifts from building them to improving them. The challenge is creating a reliable system for finding issues, understanding failures, validating fixes, and continuously improving behavior.

**Signal** helps teams discover emerging issues in production.

**Managed agents** enables teams to run long-running, repo-aware AI workers across engineering workflows.

**Agent-as-a-Judge** creates new evaluation signal as failure modes evolve.

**Agent experiments** helps teams validate changes against complete agent system behavior before deployment.

**Swarm observability** provides visibility into the AI workers operating across that process.

**Voice agent **support extends the agent improvement loop to voice, bringing observability, replay, and evaluation to conversational AI systems in production.

Engineers still review and approve the work. The difference is that they no longer start every incident from a blank trace, a Slack thread, and a scavenger hunt across logs, datasets, evals, and repository history.

**Arize AX helps teams build the AI factory for self-improving agents.**
