---
title: 'From Signal to PR: What if your agents got better every time they failed?'
kind: blog
topic: null
subtopic: null
secondary_topics: []
summary: null
triage: null
skip_reason: null
source: arize
url: https://arize.com/blog/from-signal-to-pr/
author: Chris Cooning; Sally-Ann DeLucia; Jason Lopatecki; Aparna Dhinakaran
published: '2026-07-29'
fetched: '2026-07-30T06:52:22Z'
classifier: null
taxonomy_rev: 2
words: 1004
content_sha256: 9d00a67397c24e7d527e13911e582d00b69817f1effb976ff9eef750c143b176
---

# From Signal to PR: What if your agents got better every time they failed?

*Co-Authored by Chris Cooning, Head of Product Marketing & Sally-Ann DeLucia, Director, Product & Jason Lopatecki, Co-founder and CEO & Aparna Dhinakaran, Co-founder & Chief Product Officer.*

### What if your agents got better every time they failed?

It’s 2 AM, and the pager goes off. User frustration rates are climbing, so someone opens a laptop, and the clock that matters (time to fix) has barely started.

The eventual patch may be two lines, but the expensive part comes first: finding the right traces, reconstructing the failure, forming a theory, and locating the responsible code.

We’re launching [ Signal](https://arize.com/docs/ax/observe/signal?utm_source=blog&utm_medium=web&utm_campaign=signal&utm_content=signal-docs), a managed agent built into 

[Arize AX](https://app.arize.com/auth/join)that takes on that investigative work continuously.

![Signal running on production traces: issues found, each with evidence and a proposed fix](https://arize.com/wp-content/uploads/2026/07/signal-image-01.png)

Signal reviews production traces, identifies recurring failure patterns, and groups them into ranked issues. Each issue includes supporting evidence, a root-cause analysis, and a proposed fix.

Signal doesn’t stop at surfacing issues. With a repository connected, a managed agent can carry the investigation into the codebase, propose a fix, and open a pull request, turning production telemetry into a reviewable change.

This launch points toward a more ambitious future. We believe agents will not only run in production, but also help improve the systems they run in. In fact, Signal is part of the agent improvement loop in Arize AX where production behavior becomes evidence, evidence becomes an investigation, and the investigation becomes a reviewable change.

The engineer still makes the call; they just begin with a diagnosis instead of a blank query box.

**TL;DR**

- **Signal finds the issue.**It continuously reviews production traces, groups related failures, and surfaces the evidence, likely cause, and proposed fix.
- **Managed Agents help close the loop.**With repository access, they can inspect the relevant code, propose a patch, and open a pull request.
- **Agent Studio makes the loop configurable.**Teams can run guided or custom investigations once, on a schedule, or in response to an operational trigger.
- **Humans remain in control.**The agent investigates and proposes; the engineer reviews and ships.

Signal ships on **Arize AX** **Free and Pro** today. Full managed agents, including Agent Studio, presets, and repository access, are available to **Enterprise** customers in beta.

**Observability has a new reader**

![Observability telemetry consumed by an agent, not only a human engineer](https://arize.com/wp-content/uploads/2026/07/signal-image-02.png)

For decades, production telemetry had one real consumer: a human. Applications emitted logs, metrics, and traces, and dashboards organized them. Alerts woke someone up, and an engineer then translated that telemetry into an explanation.

Coding agents accelerated the final step. Once a developer understood the problem, an agent could write the patch for them. But the human still had to consume the telemetry, isolate the failure, and turn the investigation into a prompt.

Signal moves the agent upstream. This is the next step toward [self-improving software](https://arize.com/blog/closing-the-loop-coding-agents-telemetry-and-the-path-to-self-improving-software/?utm_source=blog&utm_medium=web&utm_campaign=signal&utm_content=closing-the-loop-blog): the telemetry you capture stops being something only a human reads and becomes an input an agent can immediately act on.

**From traces to action**

An [agent improvement loop](https://arize.com/glossary/ai-improvement-loop/?utm_source=blog&utm_medium=web&utm_campaign=signal&utm_content=ai-improvement-loop-glossary) needs three things:

- **Evidence**comes from traces and evaluations. Traces capture what the agent did: model calls, retrievals, tool executions, inputs, outputs, timing, and errors. Evals help distinguish a technically successful run from a good result.
- **Context**connects runtime behavior to its cause. That can include logs, application spans, metadata, and, when connected, the repository where the change needs to land.
- **A trigger**determines when the investigation runs. Signal continuously sweeps new production traces, while broader managed-agent workflows can run on a schedule or in response to an operational event.

![Agent improvement loop: investigate, propose, review, ship, observe again](https://arize.com/wp-content/uploads/2026/07/signal-image-03.png)

Together, those pieces create an improvement loop:

- Investigate
- Propose
- Review
- Ship
- Observe again

This makes observability, especially tracing, more important. Traces serve as the source of truth and the backbone of the feedback loop. The higher the quality of the traces, the better the agent can investigate failures and identify the right code to change. Paired with strong evaluations that distinguish error modes from silent quality issues, they help the agent turn “this behavior is broken” into “this is the code that should change.”

**Start with Signal, extend with Managed Agents**

Signal comes preconfigured for continuous production reliability. Turn it on for a tracing project, and it begins reviewing new runs, tracking issues it has already seen, and surfacing emerging failure patterns.

For teams that want to go beyond that workflow, [Managed Agents](https://arize.com/docs/ax/agents/how-agents-work?utm_source=blog&utm_medium=web&utm_campaign=signal&utm_content=how-agents-work-docs) and [Agent Studio](https://arize.com/docs/ax/agents/agent-studio?utm_source=blog&utm_medium=web&utm_campaign=signal&utm_content=agent-studio-docs) in Arize AX include templates for investigating failing traces, triaging monitor alerts, analyzing costs, running recurring health checks, inspecting repositories, and proposing pull requests. Teams can also start with a blank agent and build around virtually any engineering workflow they need.

![Managed Agents in Arize AX investigating failing traces and proposing pull requests](https://arize.com/wp-content/uploads/2026/07/signal-image-04.png)

![Agent Studio: describe the task, inherit a preset, and run it once or as an automation](https://arize.com/wp-content/uploads/2026/07/signal-image-05.png)

Signal is not the endpoint, though. It is an early piece of a broader shift toward self-improving agent systems: software that can observe its own behavior, identify where it is failing, and propose the next improvement for a human to approve.

The future is not an agent rewriting itself in production. It is a controlled loop in which every trace can become evidence, every failure can become an investigation, and every investigation can become a reviewable change.

**Signal is available in Arize AX today. Turn it on against the traces and evaluations you already capture.**

**See the agent improvement loop run live**

On July 30, *From Signal to PR*, we run it live, end to end, against a production agent.

- Signal reviewing production traces and grouping failures into issues
- Agent-as-a-Judge building evals from plain-language criteria — no column mapping, no brittle rubrics
- Full-agent experiments that confirm a change moved tool use, latency, and trajectory, not just the one response you looked at
- Managed agents that investigate with repo access and open the PR

**July 30 at 11 AM PT. 30 minutes live, followed by 15 minutes of Q&A**

[Save your seat](https://luma.com/arizeai?e=evt-gUXOBwWtmjDMmK8)
