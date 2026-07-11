---
title: The three pillars of AI observability
topic: evals-observability
subtopic: monitoring
secondary_topics:
- evals-observability/tracing
summary: Defines three pillars of AI observability and how traces, evals, and production
  feedback combine to improve AI systems.
source: braintrust
url: https://www.braintrust.dev/blog/three-pillars-ai-observability
author: Braintrust Team
published: '2025-11-18'
fetched: '2026-07-11T04:33:58Z'
classifier: codex
taxonomy_rev: 1
words: 1346
content_sha256: 0c0efdf8c968b4b8587ed6a4d91dd77c77162028675885f9c25d8ab5567004d8
---

# The three pillars of AI observability

18 November 2025Ankur Goyal8 min

In traditional observability, we often refer to the three pillars of metrics, logs, and traces. In AI, this has shifted toward a new set of challenges: traces, evals, and annotation.

Classical app stacks are deterministic. You instrument code paths, emit metrics, capture logs, and (if needed) follow a trace to a root cause. AI systems are probabilistic and data‑coupled. The same input can produce different outputs. Quality depends on prompts, models, retrieval, tools, context length, and training data. Observability must therefore explain behavior and tie it to measurable outcomes, not just runtime health.

At Braintrust, we see three pillars that matter in practice:

- **Traces**: Reconstruct the full decision path for a request, across model calls, tools, retrieval, and control‑flow.
- **Evals**: Quantify performance, both in production (online) and in dev and CI (offline), to understand how well your application works and systematically improve it.
- **Annotation**: Create corrective signals for both your application and evaluators, to inject taste and ground results in user expectations.

Traditionally, tracing helps you to understand performance bottlenecks: what functions or APIs are called, how long do they take, and how do they interleave. While this remains relevant in AI, the primary use case for tracing in AI is understanding what happened in the first place. Which tools were called, and why? What context did the LLM have while generating a strange output?

Doing so requires tracing raw inputs/outputs, which are both very large (the average span in our world is 50kb compared to 900 bytes in traditional o11y) and full of PII. The leading traditional observability platforms fall apart with traces larger than 100mb. In AI, however, it's common to have 10GB+ traces. The accumulation of these challenges requires a shift in data architecture. At Braintrust, this led to developing [Brainstore](https://www.braintrust.dev/blog/brainstore), which is both designed for scale and ease of self-hosting.

Beyond the data and scale challenges, non-technical users can use AI traces to understand user behavior and product interactions, which presents a whole new set of user experience challenges. Simply viewing JSON for debugging purposes is not enough. Traces have to be simple to consume and proactive in offering insight. Users also don't want to jump between three disjointed experiences (metrics, logs, and traces) to create a full picture of user behavior, so in AI, these have collapsed into one thing: tracing.

You can't stare at a prompt and know what's going to happen. AI systems are inherently non-deterministic, and therefore you must measure their behavior to know how they perform. This process is called "evaluation", and you can do it both in production ("online") and in dev and CI ("offline"). Evaluation is best thought of as a new component of the overall observability lifecycle. You can use evals to quantify real-world performance, discover examples that need to be improved, test and improve them in dev and CI, ship, rinse and repeat.

The core primitive of evaluation is scoring. Scoring allows you to look at an entire agent interaction (trace) or turn (span) and quantify it. Usually, this means producing a number (for example, how factually grounded is the answer?), but it can also be categorical (for example, what type of error is this?). The best teams use online evals to help them discover what to test in dev and CI.

For example, if you discover that your agent is highly repetitive, you can write an evaluator to detect that case, and then capture a handful of real-world examples that you can test on your laptop. While testing, you should use *exactly the same* tracing that you run in production, and assess how the changes you make affect both the repetition score and other performance indicators that you track. Once you feel confident, you can ship a new iteration, and see how it affects production eval scores.

In traditional observability, when you notice something is wrong, the next action to take is almost always to update code and try again. However, in AI, incorrect behavior often requires input from an expert (product manager, subject-matter expert, or even a user) who can clarify the behavior. The best workflows for annotation involve curating interesting examples that would benefit from annotation, flagging them for review, and then utilizing the annotated data in evals to improve performance.

Once again, this breaks core assumptions in traditional observability. First, traces must be mutable, so that you can save annotations and query them alongside other metadata. Supporting updates on traces at "agent-scale" makes the agent-tracing database problem even more challenging. Second, the users who annotate are rarely developers, and so they benefit from UIs that simplify the data they must annotate into its simplest components.

Once you capture annotations, you should save them into datasets which are the basis for offline evaluation. Each time you want to make a change to your application, you should evaluate it against the datasets you've accumulated to approximate its impact. Although people often use the term "golden dataset", we have seen a shift away from this concept in favor of a more fluid approach called "dataset reconciliation", where the goal shifts to incrementally and frequently updating datasets to represent real-world behaviors, rather than commissioning one up front.

We built Braintrust to support these three pillars. Here's what that looks like in practice:

**Tracing that scales**

Most traditional observability tools break down when you feed them AI-shaped data. We built [Brainstore](https://www.braintrust.dev/blog/brainstore), a purpose-built database that is 80x faster than traditional data warehouses on real-world benchmarks, with median query times under one second. You get full-text search across massive datasets, immediate visibility of new data, and the ability to self-host everything in your own infrastructure. No matter what framework you use (Google ADK, OpenAI Agents SDK, LlamaIndex, and so on), Braintrust can capture your traces.

**Evaluation across every phase**

You need to evaluate at every stage: prototyping on a handful of examples, developing against larger test sets, and monitoring production at scale. Our eval system supports everything from simple assertions to LLM-as-judge scorers, and you can write custom scorers in a few lines of code. You can use the exact same evaluation code from prototype to production, which means you can confidently predict how changes will affect real users. We also built features like [Loop](https://www.braintrust.dev/docs/observe/loop) to help you systematically improve evals and discover what's not working.

**Annotation workflows for cross-functional teams**

We've built annotation tools directly into the trace viewer so product managers, domain experts, and other stakeholders can review traces, flag issues, correct outputs, and build datasets without getting lost in JSON or touching code. These annotations flow directly into your evaluation datasets, creating a continuous improvement loop that leverages expertise across your entire team.

**Deployment options**

We know some data can't leave your infrastructure. Braintrust supports hybrid deployment, where the control plane lives in our cloud but all your sensitive data stays in your VPC. You can also self-host the entire stack, including Brainstore. We designed it to be easy to run: it's a single Rust binary that uses your existing Postgres and Redis, plus object storage like S3.

AI observability requires a fundamental shift in how we think about quality, from "is it up?" to "is it good?". This requires collaboration between engineers who build the systems, product managers who define what "good" means, and subject matter experts who can correct the model's mistakes.

If you're building AI that real customers rely on, you need to:

- **Trace everything**. You can't improve what you can't measure, and you can't measure what you can't see.
- **Run evals constantly**. Both online (to catch regressions) and offline (to test improvements).
- **Build annotation into your workflow**. The best AI systems improve over time by learning from expert feedback.

This is what we've built Braintrust to do. We've worked with hundreds of teams shipping production AI, from startups to enterprises, and these three pillars are what separate successful AI products from science projects.

If you're interested in trying Braintrust, [sign up for free](https://www.braintrust.dev/signup) or [book a demo](https://www.braintrust.dev/contact) to see how we can help you ship better AI.
