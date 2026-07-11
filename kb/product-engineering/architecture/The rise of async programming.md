---
title: The rise of async programming
topic: product-engineering
subtopic: architecture
secondary_topics:
- agents/planning
summary: Explains why asynchronous programming patterns matter for long-running AI
  workflows, background jobs, agent tasks, and responsive product experiences.
source: braintrust
url: https://www.braintrust.dev/blog/async-programming
author: Braintrust Team
published: '2025-08-19'
fetched: '2026-07-11T04:31:27Z'
classifier: codex
taxonomy_rev: 1
words: 831
content_sha256: da4c5a682ab5fd58dfce433d55cf55d24b1a45b583119b653f22d82847271e5d
---

# The rise of async programming

19 August 2025Ankur Goyal5 min

I spend a decent amount of time reviewing code I didn't write. An AI agent takes a detailed problem description, writes code (primarily Typescript, Rust, and Python), adds tests, and commits the changes to a branch. I tap back in when everything's ready for review.

This used to feel like a futuristic scenario, but it's how I work now, and it's how many developers are starting to work. The shift is subtle but powerful: instead of writing code line by line, we're learning to describe problems clearly and let tools solve them in the background.

This version of "async programming" is different from the classic definition. It's about how developers approach building software.

The workflow looks like this:

- **Define the problem clearly.**Write a detailed specification of what needs to be built, including edge cases, constraints, and success criteria.
- **Hand it off.**Delegate the implementation to an AI agent, a teammate, or even your future self with comprehensive notes.
- **Return later.**Come back to review results, provide feedback, and decide on next steps.

The key difference from traditional programming is the time separation between problem definition and implementation. Instead of immediate feedback loops, you have background problem solving driven by clear requirements and automated verification.

Async programming is not *vibe coding*. Vibe coding enables you to write code without getting into the nitty gritty details. Async programming is a workflow for developers to solve more complex problems simultaneously, while still understanding the details
of the code being written. You're still architecting solutions, reviewing implementations, and maintaining a codebase. You're just not typing a vast majority of characters yourself.

For async programming to work in practice, you need three things: a clear definition of the problem you're solving, a way to automatically verify your results, and human-driven code review.

The quality of your problem statement determines everything else. Vague requirements produce vague results. Precise specifications produce working code.

Here's the difference:

**Vague:** "Make the search faster"

**Precise:** "My goal is to reduce search latency from about 800ms to around 200ms. I suspect the root cause is the heap allocation I'm doing on each batch of rows. Can you try refactoring the allocation to happen once per search, instead, and measure the impact?"

The precise version includes the current state, target outcome, proposed approach, and acceptance criteria. An AI agent (or human teammate) can work independently because the requirements are unambiguous.

Effective async programming specs read like technical documentation: they include context, constraints, examples, and explicit success criteria. If you can't explain the problem clearly, you probably don't understand it well enough to delegate it.

Async programming only works if you can verify results without manual testing every edge case. You need systems that can check the work automatically.

This might include:

- **Unit and integration tests**that validate core functionality
- **Type checking**that catches interface mismatches
- **Performance benchmarks**that ensure code meets speed requirements
- **Linting and formatting**that enforce style guidelines

The goal is developing a process that agents can use to validate their work independently. This takes time. You'll provide significant guidance initially, then develop patterns that allow agents to work autonomously. Setting this up in CI is challenging but enables background agents to perform work outside your development environment.

Once you're not typing every character yourself, code review becomes absolutely crucial. I regularly find PRs that solve the completely wrong problem, make poor design decisions, or have large amounts of code duplication.

Reviewing AI-generated code is valuable, similar to traditional code review. Expect to spend significantly more time on code review than before.

The code may not be yours line by line, but the system design and technical decisions should still reflect your judgment.

My workflow has changed since adopting async programming. I now work on four or five tasks simultaneously: one complex problem synchronously and three or four in the background. When I context switch, I review in-progress work on each background task, provide guidance, and return to synchronous work or code review.

We've been using async programming to build Braintrust itself, and now we're building tools to translate these ideas to AI engineering.

Traditional prompt engineering is manual. You write a prompt, test it against examples, observe failures, make small adjustments, and repeat. The process requires expertise but involves significant iteration.

Our agent, Loop, lets you describe the evaluation problem you're trying to solve and spends time in the background analyzing experiment results, identifying patterns in failed test cases, and suggesting improvements to prompts, datasets, and scorers.

The implications of working this way are still emerging. This changes what I optimize for as a developer: less time on IDE shortcuts and typing speed, more time explaining problems clearly and reviewing solutions thoroughly.

The implementation work can happen in parallel with other thinking. More developers will likely adopt this approach as tools improve. AI isn't replacing programming, but the most valuable parts of programming are becoming more prominent while routine tasks move to the background.
