---
title: What is AI observability?
topic: evals-observability
subtopic: monitoring
secondary_topics: []
summary: Explains AI observability concepts for production systems, including traces,
  evals, logs, monitoring, and feedback loops.
source: braintrust
url: https://www.braintrust.dev/blog/what-is-ai-observability
author: Braintrust Team
published: '2026-03-19'
fetched: '2026-07-11T04:34:20Z'
classifier: codex
taxonomy_rev: 1
words: 1486
content_sha256: 814408648d5932909eae6b88938ed24e029ddf3cf48227d2df9b517202ac7551
---

# What is AI observability?

19 March 2026Ornella Altunyan8 min

Traditional observability tells you whether your software is up and how fast it responds. Logs, metrics, and traces capture operational state, and alerting fires when known thresholds are breached. The model works because traditional software is deterministic, meaning the same input produces the same output through the same code path.

AI breaks every one of those assumptions. A language model can return a 200 status code, respond in under 100ms, and still produce an answer that is factually wrong, off-brand, or harmful. Your infrastructure metrics won't catch it and your dashboards won't flag it, because the system looks perfectly healthy while the product degrades.

AI observability exists because AI products fail differently than traditional software, and improving them requires a fundamentally different set of tools.

AI observability is the infrastructure that lets you see what your AI system did, measure whether it was good, and systematically improve it. It connects three workflows that have historically lived in separate tools: tracing production behavior, evaluating output quality, and iterating on system configuration.

The reason these workflows need to be connected is that AI improvement is a closed loop. You observe production traces, identify quality issues, build evaluation datasets from real interactions, run experiments to test changes, and deploy improvements that you then observe again. Break the loop at any point -- whether by using separate tools for tracing and evaluation or by manually moving data between systems -- and iteration slows down.

Monitoring answers "is the system operational?" AI observability answers "is the system producing good outputs, and how do we make them better?"

Two things changed in 2025 that made AI observability an infrastructure requirement rather than a nice-to-have.

The first is that agents went into production. A year ago, most AI products were single-turn, where a user sends a prompt and a model responds. Observability for that was manageable. Now, production AI systems involve multi-step agents with tool calls, retrieval steps, branching logic, and parallel execution. A single user interaction can generate dozens of spans across multiple model invocations. [Research from IBM](https://arxiv.org/abs/2503.06745) measured a mean coefficient of variation of 63% in execution paths for identical inputs to agentic systems. The same agent, given the same task, takes materially different paths each time. Dashboards can't capture that kind of variance, which is why you need structured traces and systematic evaluation.

Today, our agents are doing a lot more path finding. They're finding different feedback from their own results and adjusting what they do, and that's kind of a combinatorial explosion in evaluation.


*— Sarah Sachs, AI Lead at  Notion*

The second is that evaluation became a production concern. Early AI products could get away with vibes-based testing, where you try a few prompts, eyeball the results, and ship. That stopped working once AI features reached millions of people and errors started showing up as customer complaints rather than test failures. A [survey on LLM agent evaluation](https://arxiv.org/abs/2507.21504) found that current approaches are "fragmented," with no systematic frameworks for real-world assessment. Enterprise-specific requirements like role-based access control (RBAC), reliability guarantees, long-horizon interactions, and compliance are largely absent from existing benchmarks. The gap between how AI systems are evaluated in research and how they need to be evaluated in production is enormous, and closing it requires purpose-built infrastructure.

I'm actually amazed at how many teams still think about continuing to build AI by just refining prompts all the time and still waiting for customers to call in saying, hey, this is how I felt about using your product, rather than actually institutionalizing the process of evals.


*— Sarav Bhatia, Senior Director of Engineering at  Navan*

Building AI observability infrastructure is a systems problem as much as an AI problem. There are four technical challenges that make it fundamentally different from traditional observability, and understanding them matters if you're considering whether to build or buy this part of your stack.

An AI trace contains structured metadata, unstructured text spanning thousands of tokens, tool call schemas, retrieved documents, numeric scores, and sometimes binary attachments. It's heterogeneous, nested, and large in a way that log data simply isn't.

The [OpenTelemetry GenAI semantic conventions](https://github.com/open-telemetry/semantic-conventions-genai/blob/main/docs/gen-ai/README.md) formalize this structure with standard attributes for model calls, token usage, tool invocations, and provider metadata across vendors. A [separate proposal](https://github.com/open-telemetry/semantic-conventions/issues/2664) extends these conventions to agentic systems, introducing attributes for tasks, actions, agents, teams, artifacts, and memory. The fact that the industry's standard telemetry project needed entirely new semantic conventions for AI says a lot about how different the data model is from anything that came before.

Traditional observability data is append-only, where you write a log line or metric and it never changes. AI observability data needs to be annotated, re-scored, and linked to evaluation datasets after the fact. A trace written during a production interaction might be scored by an automated judge an hour later, annotated by a domain expert the next day, and added to an evaluation dataset the following week. Append-only databases, the default for most observability platforms, can't support this workflow without expensive workarounds.

When debugging a traditional system, you generally know what to look for, whether that's p99 latency, error rates by endpoint, or the trace for a specific request ID. AI debugging is different because the questions are open-ended. You're asking things like "find traces where the model ignored the system prompt" or "compare score distributions between this week's prompt and last week's." Answering these requires full-text search, vector similarity, and SQL analytics operating over the same dataset simultaneously, and while most databases handle one of those well, almost none can do all three with interactive latency.

Sometimes just knowing what to search for was the complicated part.


*— Luis Héctor Chávez, CTO of  Replit*

A single agent interaction can generate megabytes of trace data, and at production volumes you're writing and querying terabytes of heterogeneous, mutable data with interactive latency requirements. General-purpose databases weren't designed for this combination of constraints, and teams that start with general-purpose columnar stores or relational databases will hit scaling walls within months.

At Braintrust, we built [Brainstore](https://www.braintrust.dev/blog/brainstore), a custom-designed database engine that combines object storage, columnar analytics, full-text search, vector indexing, and mutable row semantics in a single system. We did it specifically because no existing database could handle AI observability workloads at the scale our customers operate.

AI observability, implemented correctly, is a tightly integrated platform covering six capabilities.

- Tracing production behavior across model calls, tool invocations, retrieval steps, and multi-step agent execution
- Running structured evaluations against datasets with configurable scorers and comparing results across experiments
- Managing and versioning datasets derived from production traces, with annotation workflows for domain experts
- SQL-level analytics over trace data including full-text search and statistical analysis
- Iteration tooling for prompt engineering, model comparison, and configuration management that works for both engineers and product managers
- Automation for pattern detection, scheduled evaluations, regression alerts, and quality drift monitoring

These capabilities are coupled because the data flows between them continuously. Tracing feeds evaluation, evaluation drives iteration, and iteration produces changes observed through tracing. Separate tools for each step mean separate data stores, manual exports, and broken feedback loops, and the teams iterating fastest on AI quality are the ones running this entire loop in a single platform.

If you're building AI products and don't yet have AI observability infrastructure, here's a practical way to approach it.

- **Start with traces**by instrumenting your AI system to capture structured data for every interaction. This is the foundation everything else builds on, because without traces you have no visibility into why your system produced a given output and no raw material for evaluation.
- **Define your quality criteria early**, even before you have a full evaluation pipeline. Decide what "good" means for your AI feature and break it into specific, measurable dimensions like accuracy, relevance, tone, or compliance. These criteria become your scorers.
- **Build datasets from production**rather than synthetic examples, because the best evaluation data comes from real interactions. Once you're tracing production traffic, curate small, targeted datasets around specific failure modes and quality dimensions. Ten to two hundred examples is enough to start catching regressions.
- **Close the loop**by connecting your traces to your evaluations to your iteration workflow. The value of AI observability compounds when you can go from "I see a problem in production" to "I've tested a fix against real data" in minutes instead of days.

Evals have become the new PRD. You need to really recognize what success looks like, what good looks like, how you want to apply your own judgment and think about taste.


*— Josh Clemm, VP of Engineering at  Dropbox*

AI observability is the infrastructure that makes AI products measurable and improvable. It sits between your application and your models, where traces, evaluations, and iteration come together so you can ship with confidence. At Braintrust, this is the problem we built the entire platform to solve.
