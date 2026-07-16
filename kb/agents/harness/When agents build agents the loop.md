---
title: 'When agents build agents: the loop'
kind: blog
topic: agents
subtopic: harness
secondary_topics: []
summary: 'Second post in the harness series on orchestrating loops of agents: sub-agent
  delegation via a delegate_task tool that gives each child an isolated context and
  its own narrow toolset, with tool_retries/contain_errors to bound and absorb child
  failures, plus ''code mode'' dynamic workflows where the model writes a Python program
  (in sandboxed Pydantic Monty) to gather/vote/retry across specialists.'
triage: null
skip_reason: null
source: pydantic
url: https://pydantic.dev/articles/when-agents-build-agents
author: David Sanchez
published: '2026-07-14'
fetched: '2026-07-16T22:02:45Z'
classifier: claude
taxonomy_rev: 2
words: 1357
content_sha256: 8730c888ca24f52aac19cd9e71fbc05b5783cbd162d89964dcf33ff8d0eca629
---

# When agents build agents: the loop

The [first post of this series](https://pydantic.dev/articles/what-makes-a-good-harness) argued that a good harness is about timing: it discloses the right context before the model acts, and it steers the run once the run starts to drift. A harness arms a single run and makes it reliable. This post is about what you build when one run is not enough.

We already called the agent a loop: a model working tools toward a goal. We'll now use loop to refer to *a loop of agents* (loopception?). A loop of agents does two things a single harnessed run cannot: it chooses its own structure, and it outlives the run.

The pieces below are experimental in the [Pydantic AI Harness](https://pydantic.dev/docs/ai/harness/overview/) today, but already clear enough to build on.


The way you point an agent at hard work today is to settle a plan with it first, then hand that plan to a fresh agent to carry out. You own the plan; the agent runs it, stops to ask when it is stuck, and goes idle at the end.

A loop is handed the goal instead of the plan: the target, the constraints it has to hold to, and enough of a north star to make its own calls. It works out the structure as it goes, what to split off, what to delegate, what to check.

The first move is delegation. [Sub-agents](https://github.com/pydantic/pydantic-ai-harness/tree/main/pydantic_ai_harness/experimental/subagents) hand a parent one tool, `delegate_task`, and a roster of specialists it can call by name. Each call is a fresh, isolated run: the child sees only the task it was handed, not the parent's conversation, and hands back its result. The parent keeps a small context and a roster of narrow experts, each carrying only the tools its job needs, so every agent in the tree sees the little it needs and nothing else.

Isolation also contains failure. A child that crashes or loops forever does not take the parent down with it. The delegate tool bounds how many times a failing sub-agent is retried (`tool_retries`), and can catch a child's crash and hand it back as a correction to work around instead of an error that aborts the run (`contain_errors`). That is part one's steering, moved down a level.

In the second move, the agent choreographs the sub-agents in code. One delegation per turn is a slow way to run ten independent checks, because the parent has to read each result before it asks for the next. So you give it a single `run_workflow` tool and let it write the coordination as a program.

[Dynamic workflows](https://github.com/pydantic/pydantic-ai-harness/tree/main/pydantic_ai_harness/experimental/dynamic_workflow) expose each specialist as an async function, composed in [Pydantic Monty](https://pydantic.dev/articles/pydantic-monty), our sandboxed Python subset. The model fans work out with `gather`, votes across the results, retries the ones that fail, and only the final value returns to its context. It is [code mode](https://pydantic.dev/docs/ai/harness/code-mode/) for agents: the same trick [the first article](https://pydantic.dev/articles/what-makes-a-good-harness#a-good-harness-discloses) used to collapse a wall of tool schemas, now collapsing a wall of delegations.

You compose the roster; the model writes the program that runs it:

```
from pydantic_ai import Agent
from pydantic_ai_harness.experimental.dynamic_workflow import DynamicWorkflow, WorkflowAgent
reviewer = Agent('anthropic:claude-sonnet-4-5', instructions='Review the diff for one class of bug.')
fixer = Agent('anthropic:claude-opus-4-7', instructions='Apply the smallest fix for a finding.')
coordinator = Agent(
    'anthropic:claude-opus-4-7',
    instructions='Find and fix the bugs in this diff, then verify.',
    capabilities=[
        DynamicWorkflow(agents=[
            WorkflowAgent(reviewer, name='reviewer', description='Reviews a diff for one class of bug.'),
            WorkflowAgent(fixer, name='fixer', description='Applies the smallest fix for a finding.'),
        ]),
    ],
)
```
The coordinator never sees `reviewer` and `fixer` as buttons to press one at a time. It sees two functions and writes the program that coordinates them. Who writes that program falls on a spectrum: you can hand it a fixed plan, let an orchestrator agent design the roster, or let the model decompose the task entirely, which is what recursive language models do when they treat their own context as a variable to grep, partition, and recurse over.[1](https://pydantic.dev#user-content-fn-1)


Splitting work is one half of choosing your own structure; the other is extending yourself. If you give an agent a task it has no tool for, the question worth asking is whether it can make one.

[Runtime authoring](https://github.com/pydantic/pydantic-ai-harness/tree/main/pydantic_ai_harness/experimental/authoring) gives an agent a tool that writes a new capability to disk. The agent generates the code; the harness imports it and runs its static checks before it counts as real.

To author against the actual API instead of a guessed one, a companion capability serves the current [Pydantic AI](https://pydantic.dev/docs/ai/) docs on demand, and another walks the repo the agent was pointed at, loading its `CLAUDE.md` and `AGENTS.md` files and cataloging the skills and sub-agents already defined there. The loop discovers the context a team already wrote, then adds to it.

The honest boundary, and it is the load-bearing part, is that none of this happens mid-run. Pydantic AI resolves an agent's full set of [capabilities](https://pydantic.dev/docs/ai/core-concepts/capabilities/) once, at the start of a run, and holds it fixed. A capability the agent authors on turn nine is not live on turn ten, it is live on the next run. The loop does not rewrite itself in flight: it runs, learns something, re-arms, and runs again. The unit that improves is the loop, not the turn.

That constraint buys something. A run whose tools and instructions are fixed at the start presents a stable prefix, and a stable prefix is one the provider can serve from cache. A run that rewrote its own toolset every few turns would invalidate that cache on every edit and pay full price for the whole history each time.

This is why the one in-flight change that does exist, revealing a new sub-agent to a running workflow, appends it at the tail and leaves the tool definitions untouched: new capacity, same cached prefix. Working with the provider's cache instead of against it is most of the difference between a loop that is cheap to run and one that is not.


The second axis is time. A harnessed run lives inside one request: it starts, works, and returns. A loop is decoupled from any single request. It can go idle and wake on an outside event, a closed pull request, a failed CI job, a teammate's reply, and pick up where it left off. It survives a restart, and carries state across a horizon far longer than any one model's context window.

Two mechanisms make that concrete, both forms of step persistence:

- **Checkpoint and continue:**a loop that is interrupted resumes instead of restarting.
- **Fork:**a loop branches at a decision, tries two approaches in parallel, and keeps the one that verifies.

Forking is the one that points forward: a loop that can split itself and keep the winner is the raw material for a loop that gets better at its own job.

Before it can do that, two things are still missing. The loop needs to see every one of its runs on one timeline, and it needs a memory of what its sub-agents did that outlives any single context.

The first exists today: every model call, tool call, delegation, and context compaction lands as a span in [Pydantic Logfire](https://pydantic.dev/logfire), so the whole agent tree reads as one trace. The second is the frontier we are working toward, making each sub-agent's history a substrate the rest of the loop can query on demand, scoped by rank, reachable and known but not loaded into every context by default. No harness ships that yet.


A loop that picks its own structure, writes its own tools, and can see its own runs is one step from a loop that improves them. Sub-agents, dynamic workflows, and runtime authoring are the moving parts; the interesting question is what happens when the loop starts turning that machinery on itself, proposing a better prompt, writing an evaluator for its own output, keeping the change only if it measurably helps.

That is the last part of this series: loops that improve themselves, and where Pydantic Logfire fits when they do.


## Footnotes

- 
Alex Zhang and colleagues (MIT), ["Recursive Language Models"](https://alexzhang13.github.io/blog/2025/rlm/). The model, not a person, decides how to break the context down; the authors are explicit that "RLMs are not agents."[↩](https://pydantic.dev#user-content-fnref-1)
