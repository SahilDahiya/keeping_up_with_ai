---
title: How to build a better agent harness with traces and evals
topic: agents
subtopic: planning
secondary_topics:
- evals-observability/tracing
summary: Shows how traces and evals combine inside an agent harness to make agent
  behavior easier to test and improve.
source: arize
url: https://arize.com/blog/improve-ai-agents-traces-evals-harness/
author: Aaron Winston
published: '2026-05-29'
fetched: '2026-07-11T04:56:16Z'
classifier: codex
taxonomy_rev: 1
words: 2495
content_sha256: d78a7df2a3c876b6279b81358130b9a9e6d4ef64c5feb56328e1a2e0f20772b4
---

# How to build a better agent harness with traces and evals

AI agents are easy to prototype and hard to improve. A better prompt may help, but most durable improvement comes from the harness around the model: the tools it can call, the context it receives, the traces it emits, the evals it runs, and the review gates that decide what changes safely ship.

An agent improvement loop makes that harness better over time. Trace each run, evaluate specific spans, inspect failures, decide whether the agent or evaluator is wrong, update the prompt, rubric, tool, context, or eval, and run the loop again.

In a live demo with Aakash Gupta, Arize AI cofounder and CPO Aparna Dhinakaran showed this workflow using a PM agent for [Arize Phoenix](https://arize.com/phoenix/). The agent pulled GitHub issues, discussions, and releases, scored product feedback, generated a report, and then used traces and evals to understand where the system failed.

The first run was useful, but it didn’t answer the more important question: why did the agent make those decisions?

When the report is wrong, you need to know where the failure happened. Did the agent fetch the wrong data? Miss important context? [Pick the wrong tool](https://arize.com/blog/how-to-evaluate-tool-calling-agents/)? Stop too early? Apply the wrong scoring rubric? Or did the eval judge the output incorrectly?

Most agent projects stall here. Teams can inspect the final answer, but they can’t reliably replay the agent’s trajectory, evaluate the right behavior, and turn failures into a concrete change.

A better pattern is to treat agent improvement as an engineering loop: [trace the run](https://arize.com/blog/llm-tracing-and-observability-with-arize-phoenix/), evaluate behavior from those traces, inspect failed spans, decide whether the agent or the eval is wrong, [improve the harness](https://arize.com/blog/what-is-an-evaluation-harness/), and run it again.

**TL;DR: Better agents come from better harnesses **

Agents are easy to prototype and hard to improve. The fix is not a better prompt by default. Trace the run, use those traces to [create one targeted eval](https://arize.com/docs/phoenix/evaluation/tutorials/run-evals-with-built-in-evals), inspect failed spans, decide whether the agent or eval is wrong, then improve the prompt, tools, context, rubric, or evaluator. [Better agents come from a repeatable loop](https://arize.com/blog/from-production-traces-to-better-ai-agents-automating-the-llmops-feedback-loop/): trace, evaluate, debug, refine, and run again.

**Start with an agent that does real work**

Start with a task you can inspect.

In the demo, the task was a PM agent for Phoenix. It read product feedback, scored what mattered, and turned that into a priority report. The first version didn’t need every possible source of context. GitHub issues, GitHub discussions, and recent releases were more than enough.

The important thing is your workflow has clear units of behavior:

- Fetch recent issues, discussions, and releases
- Score each issue or discussion by priority
- Write a short rationale for each score
- Generate a markdown report with top pain points, feature requests, recurring themes, shipped items, and recommended P0 to P3 priorities

That gives you something concrete to debug. If the report is wrong, you can inspect whether the agent fetched the right issues, missed an important discussion, overweighted reactions, underweighted customer impact, or introduced a recommendation that was not supported by the source data.

A useful starter prompt might look like this:

```
```
Build a PM agent for this product.
Use recent GitHub issues, GitHub discussions, and releases as input.
For each issue or discussion, score its priority based on:
- whether it is a bug or feature request
- number of comments and reactions
- recency
- customer impact
- relationship to recent releases
Generate a markdown report with:
- top pain points
- top feature requests
- recurring themes
- recommended priorities from P0 to P3

			This works because the agent isn’t being abstractly asked to “understand users.” Instead, it’s being asked to collect feedback, score each item, explain the score, and synthesize the results. Each step can be traced and evaluated.

Over time, you can expand the context to Slack, Discord, Gong transcripts, product analytics, support tickets, user interviews, and social feedback. But start narrow. Get one workflow running, trace it, evaluate it, and add more context once you understand where the agent fails.

**Trace every step before you write serious evals**

Don’t start designing eval from a blank page. You should always start from traces.

For agents, the final answer is not enough. You need the path the agent took to produce it: data fetched, tool calls made, LLM calls made, intermediate outputs created, and how each step led to the final report.

In the demo, the agent pulled 40 discussions, 60 issues, and 8 releases before scoring each item and generating the report. A simplified trace might look like this:

```
```
Trace: generate_pm_report
Span: fetch_github_discussions → 40 discussions
Span: fetch_github_issues → 60 issues
Span: fetch_recent_releases → 8 releases
Span: score_issue_priority → priority score + rationale for each item
Span: synthesize_report → markdown PM report

			Each step is a span, and the full run is the trace.

If a privacy issue is ranked P3, you can inspect the relevant spans. Maybe the agent never fetched the right comments. Maybe it fetched the issue but scored it incorrectly. Or maybe it scored the issue correctly but dropped it during synthesis. Without traces, you don’t know the answer and you’ll end up rewriting prompts blindly.

**Use traces to pick one eval, then criticize it**

Once traces are flowing, ask a more specific question: what behavior should this agent be evaluated on first?

In Aparna’s demo, Claude initially suggested report-level evals: groundedness, priority alignment, and actionability. Those are useful, but they’re coarse. Aparna pushed the eval down to the issue level: for each issue the agent scored, did it assign a reasonable priority?

That eval maps directly to the behavior that drives the report. If the agent misscores individual issues, the final report will be wrong even if it’s well written.

A priority-accuracy evaluator might inspect:

- the issue or discussion
- metadata like comments, reactions, recency, and labels
- the agent’s assigned priority
- the agent’s rationale
- the team’s prioritization rubric

Then it returns a judgment: accurate or inaccurate, with a reason.

Here’s an example: if a bug affects active users and has multiple confirmations, your rubric may say it should never be P3. If the agent repeatedly gives those bugs low scores, the eval should catch the pattern.

That’s the key shift: evals should emerge from traces, not abstract guesses about what might go wrong.

The first eval is a draft. It gets you into the loop, but still needs human criticism.

A generated eval may flag useful failures. It may also misjudge behavior. Your job is to review a small set of passed and failed spans and ask: was the agent wrong, or was the eval wrong?

This matters because “priority accuracy” is product judgment. One team may prioritize enterprise customer bugs above everything else. Another may prioritize open-source adoption blockers. Another may care most about roadmap-aligned feature requests. The eval needs that judgment encoded clearly.

**A good review loop should be simple: run the eval, filter for failures, inspect the relevant spans, then ask:**

- Did the agent misunderstand the issue?
- Did the agent miss important context?
- Did the evaluator apply the wrong rubric?
- Did the evaluator overreact to a weak signal?
- Did the evaluator fail to account for product strategy?

From there, revise the eval, revise the agent, or both.

**Failures are useful when they create a path to improvement.** If every output passes, your eval may be too weak. If every output fails, your eval may be misaligned. The useful middle is a healthy mix of passes and failures that you can inspect, categorize, and act on.

In the PM-agent example, failed evals might show that the agent consistently under-ranks bugs. That gives you a concrete fix: update the scoring rubric, add examples of historically escalated bugs, or add product analytics and support data so the agent has more context about impact.

The loop becomes:

```
```
Run the agent.
Trace the run.
Evaluate the spans.
Inspect failed evaluations.
Identify the failure pattern.
Update the eval, the prompt, the tools, or the context.
Run the agent again.

			That is the practical version of self-improvement. The agent doesn’t magically get better. The system gets better because traces expose behavior, evals turn behavior into measurable signals, and humans refine the policy behind the loop.

**Run two loops: the agent loop and the improvement loop**

In the live session, Aparna showed two key loops:

- The agent loop runs on a schedule: fetch new feedback, score issues, and generate the report.
- The improvement loop reads failed evals, opens the relevant traces, groups failures, and proposes the smallest safe change to the agent, evaluator, data sources, or tools.

For the PM agent, you could ask:

```
```
Find all spans where the priority accuracy eval failed.
Group the failures by root cause.
For each group, recommend whether we should improve:
- the agent prompt
- the scoring rubric
- the evaluator
- the data sources
- the tool implementation
- the tool sequence or stopping criteria
Draft the smallest safe change that would improve the next run.

			This is where the workflow stops looking like a dashboard and starts looking like an engineering loop. The agent can consume traces, read eval results, cluster failures, and suggest changes.

The improvement agent isn’t just reading final outputs. Instead, it’s reading the trace: which tools were called, what each tool returned, which LLM calls happened, which spans failed, and how those steps led to the final output. That trajectory is typically where the real bug lives.

The human still decides what ships. For an internal PM agent, the loop can move quickly. For a production agent, proposed changes should go through review, especially changes to prompts, tools, routing policy, and evals. Eval changes deserve extra scrutiny because they redefine what “good” means.

That is the governance layer: automate analysis and recommendations, but keep humans responsible for policy, review, and deployment.

**Make observability part of the harness**

Observability is usually framed as a debugging tool for humans. For agents, it also becomes input data for the improvement loop. Traces become evidence, evals become checks, and failure clusters become improvement tasks.

That’s why the architecture matters. If trace data is trapped in a dashboard, the loop stays manual. If traces and eval results are available through APIs, CLIs, and [standard formats](https://arize.com/blog/the-role-of-opentelemetry-in-llm-observability/), agents can consume them directly.

That’s what happened in the demo: Aparna’s [Claude Code skills could call APIs](https://arize.com/blog/arize-skills-coding-agent-workflows-for-traces-evals-and-instrumentation/), fetch traces, inspect spans, and use that data to suggest evals and improvements.

This doesn’t remove humans from the loop. But it does change where humans add leverage: defining rubrics, reviewing changes, inspecting ambiguous failures, and deciding what level of autonomy is safe.

Prompts matter, but the harness is where most agent improvement happens. The harness controls context, tools, state, retries, routing, memory, evals, and review gates. If an agent underperforms, the fix might be a prompt change, but it might also be a better tool, a new retrieval step, a stricter policy, a different scoring function, or an improved eval.

**In other words, self-improvement is really harness improvement.**

In the PM-agent example, GitHub data is enough to prototype the workflow but will eventually hit limits. Customer calls, support tickets, sales notes, product analytics, and community discussions may all change how an issue should be prioritized.

The same pattern applies to support agents, coding agents, research agents, and in-product assistants. The model is one part of the system. The harness determines whether the model has the right context, whether behavior is observable, whether outputs are evaluated, and whether the system can improve safely.

**A practical starter workflow**

Start with the two-hour version and pick a repetitive internal workflow where the cost of failure is low and the learning value is high.

Pick something that already takes a few hours each week: triaging GitHub issues, summarizing release feedback, drafting support insights, reviewing sales call themes, or generating a weekly product report.

From there, you can:

- Build the simplest agent that can perform the task
- Give it one or two data sources
- Trace tool calls, LLM calls, intermediate decisions, and final outputs
- Pick one eval tied to one behavior
- Run the eval on real traces
- Inspect failed spans
- Make one improvement
- [Run the loop again](https://arize.com/docs/phoenix/cookbook/ai-engineering-workflows/iterative-evaluation-and-experimentation-workflow-python)

Here’s a basic rubric (pun intended) to consider depending on what you’re building:

- **Triage agent:**priority accuracy
- **Support agent:**answer groundedness
- **Research agent:**citation correctness
- **Coding agent:**requirement satisfaction

That single cycle teaches more than a generic eval framework because it is grounded in your agent’s actual behavior.

**What changes when this moves into production**

Production agents use the same loop with stricter review boundaries.

The agent should still be instrumented, evals should still run on real traces, and failures should still feed improvement workflows. The difference is production systems need a clear separation between analysis and action.

A safe production loop can automatically detect failed interactions, retrieve the relevant trace, run evals, cluster root causes, and draft a proposed fix. Shipping that fix should depend on the risk of the change.

For example, [a thumbs-down on an in-product agent response](https://arize.com/blog/how-to-use-annotations-to-collect-human-feedback-on-your-llm-application/) could trigger a debug workflow that retrieves the trace, checks whether the eval or agent was wrong, and proposes a fix. That proposal should still go through review before it changes production behavior.

Low-risk changes might update documentation, add examples to an eval dataset, or create a ticket. Higher-risk changes should require review before modifying a prompt, tool policy, routing rule, or production agent behavior. Eval changes deserve special care because they alter the definition of quality.

The goal is shortening the distance between production failure and safe improvement.

**Make agent improvement a repeatable system**

The best teams are [moving from one-off debugging to repeatable improvement workflows](https://arize.com/blog/ai-agent-debugging-four-lessons-from-shipping-alyx-to-production/). Every run should produce evidence you can use: traces that show what happened, evals that identify where behavior broke down, and failed spans that point to the next change.

That’s the role of the harness. It gives the agent the right context, records the path it took, runs checks against the behavior you care about, and creates a safe place to propose changes before they reach production.

This is how agent systems become more reliable over time: not through a single better prompt, but through a workflow that makes failures visible, reviewable, and actionable.

**For developers and AI engineers, here’s a practical takeaway: don’t wait until your agent is “finished” to add observability and evals.** The first useful version of an agent is exactly when you should start collecting traces. Those traces will show you what to evaluate. The evals will show you what failed. The failures will tell you what to improve.

Build the agent, trace the run, create one eval from real behavior, [criticize the eval](https://arize.com/blog/how-to-build-llm-as-a-judge-evaluators-that-hold-up-in-production/), inspect failed spans, improve either the agent or the evaluator, and run the loop again.

That’s how you move from a prototype that works once to an agent system you can keep improving.
