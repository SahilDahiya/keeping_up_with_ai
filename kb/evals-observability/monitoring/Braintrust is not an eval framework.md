---
title: Braintrust is not an eval framework
topic: evals-observability
subtopic: monitoring
secondary_topics:
- evals-observability/evaluation
summary: Argues that production AI quality needs a full observability and iteration
  system around evals, not only an isolated evaluation framework.
source: braintrust
url: https://www.braintrust.dev/blog/braintrust-not-eval-framework
author: Braintrust Team
published: '2025-07-14'
fetched: '2026-07-11T04:31:46Z'
classifier: codex
taxonomy_rev: 1
words: 1160
content_sha256: 6a52c624473a27272b7725dcb87b997d40e2fbe9d248260850b6fb774cfb9b1c
---

# Braintrust is not an eval framework

14 July 2025Ankur Goyal7 min

There's a recurring theme in conversations about AI development tools lately: "You don't need an eval framework." Sometimes Braintrust gets lumped into this category, but Braintrust is not an eval framework.

**Braintrust is infrastructure for building, scaling, and optimizing AI evaluations.** And while you might not need an eval framework, you absolutely need eval infrastructure.

Eval infrastructure is the set of systems that make it possible to run, visualize, and learn from evaluations at scale. It's what transforms evaluations from academic exercises into practical tools that actually improve your AI products.

**Instrumentation.** It's really useful to see detailed traces for each test case in an eval. If you're building an agent, seeing each individual LLM call and tool call, for example, is invaluable. If you're working on RAG, it's very helpful to see the retrieved documents. It's also useful to automatically capture metrics like token counts, cost, latency, and error rates.

**Production data integration.** The best evals use real production data. You need systems to capture traces from your application, extract relevant examples, and manage (versioned) datasets. This problem gets really hard at scale. We put a lot of love into the workflow of finding useful traces and saving them to datasets to power your evals. To make this work at scale, we even had to build our own database called [Brainstore](https://www.braintrust.dev/blog/brainstore), which is specifically optimized for handling AI-shaped data.

**Reproducibility and versioning.** Every eval run needs to be reproducible. This means capturing the state of the world at the time of the eval, including the model(s), dataset, and code. It also means making it straightforward to play with this state. For example, you can open LLM calls, tweak parameters, and re-run them.

**Real-time visualization and exploration.** A spreadsheet works great for 100 rows. But modern evals run on thousands or even millions of test cases, and it's non-trivial to visualize that much data, quickly, while still drilling down all the way to individual LLM calls. We work very hard on designing the eval UI to make this intuitive. For example, you can slice and dice by different attributes,
quickly see aggregated scores for each group, and even look at diffs per group across experiments.

**Scoring infrastructure.** Modern scoring functions aren't just simple metrics: they might call LLMs, run code execution, or implement complex domain-specific logic. Running these at scale, handling failures gracefully, and iterating quickly requires specific infrastructure. We run each scoring function in its own sandbox, and deal with creating/running these securely for you.

**AI optimization deeply integrated with your evals.** Braintrust exposes all of its core functionality as tools that our agent, [Loop](https://www.braintrust.dev/docs/observe/loop), can use to automate the manual gruntwork of evaluations for you. One of my favorite use cases is adding new data to a dataset while taking into account current eval performance.

Here's a fun fact: most of our users don't write eval code anymore. They create playgrounds to define and run evaluations interactively. This shift happened once we added enough infrastructure that you didn't *have* to write code anymore. Once you don't have to, the experience of testing and evaluating becomes much more accessible and efficient for everyone on the team.

In a playground, you can tweak a scoring function and immediately see results across your entire dataset. You can test prompts on thousands of datapoints without writing a line of code. The infrastructure handles all the complexity, like parallelization, caching, and error handling, so you can focus on improving your AI.

This is the real test of good infrastructure: it becomes invisible. You stop thinking about how to run evals and start thinking about what to evaluate.

There are compelling reasons to start with solid eval infrastructure rather than logging traces to `JSONL` files or querying them with `pandas`:

-
Infrastructure engages users across the technical spectrum. Through tools like playgrounds and human annotation, we provide a way for subject matter experts and domain leads (people who might be intimidated by JSON, spreadsheets, or code) to participate. Everyone knows that failing to involve subject matter experts is the surest way to fail at building evals.
-
Infrastructure provides battle-tested conventions. We use simple conventions like inputs, outputs, expected, and metadata to log traces. These conventions are shared across your team, queryable, and handle everything from small traces to large agentic interactions with tool calling and multimodal content.
-
Infrastructure scales from tens to millions of traces. This is why we built Brainstore. You can send as much data as you want and query everything fast using BTQL (Braintrust Query Language). With multi-turn conversations and agentic systems, traces are getting bigger all the time. Good infrastructure doesn't care about trace size or volume.

The beauty of infrastructure is that it works with any framework, or no framework at all. Dozens of eval frameworks integrate with Braintrust because they recognize the same thing we do: frameworks handle the "what" of evaluation, but infrastructure handles the "how."

But Braintrust does come with its own framework that's quite powerful without being constraining. Our primary innovation was turning the otherwise imperative code structure of an eval into a simple declarative API:

typescript

```
Eval("My feature", {
    data: [...],
    task: () => { ... },
    scores: [...]
})
```
This forces you to think about the three fundamental challenges of constructing a good eval: data, task, and scores. It handles parallelization and rate limits automatically. And the `Eval` object itself can be used in more clever ways than just running it. For example, Braintrust has a feature called [Remote evals](https://www.braintrust.dev/docs/evaluate/remote-evals), that allows you to interactively run any `Eval` in our UI.

But here's the key: frameworks are optional patterns for organizing your eval code. Infrastructure is the foundation that makes evals actually useful.

I spend a lot of time working on our product, and it turns out that very little of that time is spent on the framework itself. If you look at the git history for [framework.ts](https://github.com/braintrustdata/braintrust-sdk/blob/2a256e4dec0180e6e27cd8bda8b4ef1bc3b1bdd9/js/src/framework.ts#L4) and [framework.py](https://github.com/braintrustdata/braintrust-sdk/blob/2a256e4dec0180e6e27cd8bda8b4ef1bc3b1bdd9/py/src/braintrust/framework.py#L4), you'll see they haven't changed much recently.

Instead, I focus most of my energy on the problems that impact our customers the most: improving our UI and solving for scale. We recently reworked [how experiment data is loaded in the UI](https://www.braintrust.dev/blog/faster-experiments) to make loading them 10x faster. We're currently reworking the UI for defining scoring functions, so it's easier to test and iterate on them without running a full eval.

This is what infrastructure work looks like: solving the hard problems that make evaluations actually useful in practice.

The next time someone tells you "you don't need an eval framework," they're probably right. But you absolutely need eval infrastructure. At Braintrust, we're laser-focused on building that infrastructure. Whether you use our framework, bring your own, or write raw Python loops, we make sure your evals actually help you ship better AI. [Give Braintrust a try](https://www.braintrust.dev/signup), and you'll see why the best AI teams don't talk about their eval framework—they talk about their eval results.
