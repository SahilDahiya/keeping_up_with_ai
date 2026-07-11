---
title: 'Alyx 2.0: The AI Agent That Actually Plans'
topic: agents
subtopic: planning
secondary_topics:
- product-engineering/case-studies
summary: Introduces Alyx 2.0 as an agent that plans over observability workflows,
  covering product design lessons from building a more capable AI analyst.
source: arize
url: https://arize.com/blog/alyx-2-0-the-ai-agent-that-actually-plans/
author: Sally-Ann DeLucia; Jack Zhou; Chris Cooning; Aman Khan
published: '2026-02-24'
fetched: '2026-07-11T04:54:41Z'
classifier: codex
taxonomy_rev: 1
words: 1078
content_sha256: 187b8d1fed6e031cda39c34e37f81917e69c78ef423e7e89456e348d4649f552
---

# Alyx 2.0: The AI Agent That Actually Plans

*Co-Authored by Sally-Ann DeLucia, Director, Product & Jack Zhou, Staff Software Engineer & Chris Cooning, Head of Product Marketing & Aman Khan, Group Product Manager.*

Two years ago, we started building Alyx with GPT-3.5, a vision, and honestly, no clear path forward. Agents were a buzzword. The models were rough. Tool calling was just emerging. But we had a hypothesis: **the future wouldn’t be clicking through UIs or even just chatting with an assistant**. You’d say what you want, and an agent just does it.

Then we watched Cursor and Claude Code show us what it feels like when a real agent actually works for you. That changed everything.

Today, we’re releasing Alyx 2.0. A true planning agent for AI engineering that can reason across your entire AI lifecycle in Arize AX, break down complex tasks, and execute autonomously across the platform.

To try Alyx,[check out our docs](https://arize.com/docs/ax/alyx/arize-copilot)or[book a meeting](https://arize.com/request-a-demo)for a custom demo

## Planning Changes Everything

The biggest unlock here isn’t better models or more tool calls. It’s planning.

Most “AI assistants” in observability and development tools are either glorified chatbots or rigid, pre-defined workflows. They follow one decision tree from the top. They can’t adapt. They can’t compose complex actions. They definitely can’t surprise you.

Alyx 2.0 is different. It’s built on a true orchestrator that can reason about multi-step tasks, maintain context across actions, interact with the UI when needed, and ask for approval at critical decision points.

## What Alyx Can Actually Do

### Error analysis without the grind

Most error analysis workflows are manual by design. You sift through traces, annotate issues, collapse them into labels, guess what matters, then wire up evaluations after the fact. It’s slow, subjective, and brittle.

Alyx collapses that entire workflow into a single question. If you already have traces flowing into Arize AX, you can ask:

*“Review my reasoning annotations, identify the most critical issue and turn it into an eval.”*

Alyx does the rest. It synthesizes annotations into discrete labels, determines what’s actually critical (not just most frequent), generates evaluation templates, and spins up a live evaluation task automatically.

No manual review. No label taxonomy debates. No wiring things together by hand. Just answers and the evals to back them up.

### Prompt engineering, without staring at a blank page

[Prompt experimentation](https://arize.com/docs/ax/develop/datasets-and-experiments) usually starts in the worst possible state: a blank playground, no dataset, no baseline, and no idea where to begin. With Alyx, you can delegate.

Ask Alyx to generate a dataset for your use case. It creates it, populates it with realistic examples, and loads it directly into the playground. You’re ready to iterate immediately.

But Alyx doesn’t stop at setup. Ask for something more complex:

*“Create two prompt variants, attach an evaluation, and run an experiment.”*

Alyx plans the work, interacts with the UI, requests approval when needed, runs the experiment end-to-end, analyzes the results, and recommends concrete improvements.

You’re not clicking through interfaces or manually running experiments anymore; you’re directing outcomes and Alyx handles execution.

### Trace debugging that actually debugs

Most “debugging tools” just show you more data. Alyx explains why things broke.

We use Alyx to build Alyx. When we noticed spans returning evaluation templates without any reasoning (a bad UX that felt incomplete), we asked:

*“Find spans where we returned a final eval template without reasoning.”*

Alyx identified the spans instantly. From there, we clicked into a trace and asked:

*“Why didn’t this return reasoning?”*

Alyx traced the failure to a specific guideline, pointed to the exact decision path, and surfaced the root cause. No guesswork. No spelunking. We knew exactly what to fix.

## Why This Matters

If you’re an AI PM or AI engineer, the hardest part of your job isn’t writing prompts, it’s everything around them.

Managing context across long-running sessions. Turning vague failures into reproducible test cases. Figuring out why an agent broke after a seemingly harmless prompt change. Manually setting up experiments just to compare two prompt variants. Stitching together traces, annotations, evals, and metrics across half a dozen tools.

These workflows are fragmented, manual, and slow and they don’t scale as systems become more agentic.

Alyx changes the unit of work.

Instead of operating at the level of prompts, traces, or individual evaluations, Alyx operates across the entire AI engineering lifecycle. It can synthesize datasets from real failures, derive evaluations from failure patterns, optimize prompts against annotations, run and analyze experiments, annotate traces, compute metrics, and surface what actually matters – all in one continuous loop.

You’re no longer orchestrating tools. You’re delegating intent.

That’s what makes Alyx different. It’s not a loop, a chat interface, or a smarter playground. It’s an agent grounded in your Arize data that can plan and carry out multi-step AI engineering workflows, from diagnosis to execution, without you stitching everything together by hand.

The response from our customers has been explosive. And honestly, building Alyx has surprised us too. There have been multiple moments where it accomplished things we didn’t explicitly design for. That’s the fun – and the challenge – of building true agents.

## The Hard Parts No One Talks About

Building something this good is genuinely difficult. Some lessons learned:

**Context management is brutal**. Message buses, UI state, context window bloat. Keeping everything coherent without losing critical information is an ongoing challenge.

**Testing an agent to prevent regressions is unsolved**. How do you make sure prompt or architecture changes don’t break previous workflows when the system is adaptive by design? We’ve had to build custom evaluation frameworks just for Alyx itself.

**UI integration is harder than you think**. Programmatic actions versus sub-agents, splitting tools smartly so they’re small and reusable. Every decision compounds.

Alyx isn’t perfect. But it delivers real value. And we’re learning constantly.

## What’s Next

This is just the beginning. We’re doubling down on capability and on making Alyx fit naturally into how you already work, including using Alyx directly inside tools like Claude Code and Cursor. Not forcing you into a new workflow.

Longer term, our vision is for Alyx to become a true partner for AI PMs and engineers. One that can reason, plan, and act across your entire AI lifecycle in Arize AX. Cursor for AI engineering.

We’ve been using Arize AX and Alyx to build Alyx. Those lessons are shaping where this goes next.

Watch the intro video to see Alyx 2.0 in action, and stay tuned for deep dives on specific workflows over the coming weeks.
