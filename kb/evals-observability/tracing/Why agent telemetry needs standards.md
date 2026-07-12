---
title: Why agent telemetry needs standards
topic: evals-observability
subtopic: tracing
secondary_topics:
- agents/tool-use
summary: Argues for standard agent telemetry schemas so teams can reconstruct tool
  calls, model hops, context use, and handoffs across production agent systems.
source: arize
url: https://arize.com/blog/agent-telemetry-standards/
author: Richard Young
published: '2026-05-01'
fetched: '2026-07-11T04:55:44Z'
classifier: codex
taxonomy_rev: 1
words: 1039
content_sha256: bf3fd9c1d995e979c1a7b7da6bf4733a36ec04a555faf3693fce6d2dd07dce95
---

# Why agent telemetry needs standards

Enterprise agents are moving from demos into production workflows, which creates a basic problem: teams need to understand what those agents actually did.

A production agent may rewrite a user request, call multiple tools, retrieve context, invoke several models, hand work to another agent, and return an answer that looks simple on the surface. Without a shared way to capture that behavior, every platform becomes its own black box.

That’s why the Google Cloud and Arize AI collaboration matters. This isn’t just about sending traces from [Gemini Enterprise Agent Platform](https://cloud.google.com/blog/products/ai-machine-learning/introducing-gemini-enterprise-agent-platform) into Arize AX, but aligning agent telemetry around OpenTelemetry and OpenInference so teams can instrument agents once, analyze behavior consistently, and avoid locking critical observability data inside a single platform.

In [a Google Cloud NEXT breakout session](https://www.youtube.com/watch?v=nLH0IqHLxaA), Arize AI founder and CEO Jason Lopatecki and Google Cloud product leader Rami Shalom discussed the foundation for how enterprise AI agents will be monitored and improved today and in the future.

Here’s what you need to know.

**The important part is portability, not the integration**

The real story isn’t a point-to-point integration, but the push toward a shared telemetry model for agents.

Observability has already gone through this transition once. Before OpenTelemetry, teams dealt with competing tracing standards, vendor-specific SDKs, and fragmented instrumentation. [OpenTelemetry](https://opensource.googleblog.com/2019/05/opentelemetry-merger-of-opencensus-and.html) gave developers a common way to generate and export telemetry across languages, services, and backends.

Agent systems need the same thing. Today, frameworks and platforms often describe prompts, tool calls, retrieval steps, and handoffs differently. That makes traces harder to compare, route, evaluate, or migrate. A shared standard changes the operating model: instrument once, route anywhere.

**Why it matters to you:**

When you use standards like OpenTelemetry and OpenInference, you keep optionality without losing visibility. Standardized agent telemetry lets you change frameworks, models, tools, or observability backends without rebuilding your instrumentation every time. The trace format stays consistent even as the stack changes.

In practice, that means faster experiments, cleaner migrations, and less time spent maintaining one-off telemetry adapters.

**2. Traces are the “system of record” for agent behavior**

For traditional applications, traces usually explain why a request was slow or why a service failed. For agents, traces do something more important: they capture the decision path.

A single agent run can include request rewriting, planning, retrieval, tool calls, model calls, retries, handoffs, and final response generation. The final answer is only the output; the trace shows the process that produced it. And that process is what teams need to debug, evaluate, and improve.

A useful agent trace should answer:

- What did the user ask, and how was that request transformed?
- Which models, tools, prompts, and data sources were used?
- Where did latency, hallucination, policy failure, or bad retrieval enter the trajectory?
- Which step should be evaluated or improved?

Semantic conventions are what make agent traces usable instead of merely visible. OpenTelemetry already gives teams a shared vocabulary for infrastructure telemetry: HTTP requests, database calls, queues, and other service-level events. [OpenInference](https://github.com/Arize-ai/openinference) extends that model to AI systems with spans and attributes for model calls, prompts, retrieval, tool use, evaluations, and multi-agent workflows. That turns an agent run from an opaque transcript into a typed, queryable timeline you can filter, compare, evaluate, and debug step by step.

**What to consider:**

If you own reliability, risk, or product quality, “the agent worked in the demo” isn’t enough. Standardized traces create the feedback loop production teams need:

- Compliance teams get an audit trail for agent decisions.
- Safety teams can search for recurring failure patterns instead of investigating one incident at a time.
- Product and engineering teams can turn real trajectories into eval datasets, prompt changes, retrieval improvements, and fine-tuning examples.

Without that feedback loop, teams are shipping behavior they cannot reliably inspect.

**3. Standardization only matters if you can act on it**

Agreeing on a standard is only useful if it changes how teams work day to day.

Google’s role here is making agent telemetry portable. Instead of instrumenting each framework or tool separately, teams can emit OpenTelemetry-compatible traces once and route them wherever they need.

In practice, that means standardized agent traces flowing out of Gemini Enterprise Agent Platform into downstream systems like Arize AX without custom adapters or re-instrumentation.

But portability only matters if you can do something with the data once it arrives.

Because Arize already understands OpenInference and OpenTelemetry semantics, it can work directly on these traces without translation. That enables a few concrete workflows:

- Tracing failures back to specific steps in an agent trajectory (retrieval, tool call, model response)
- Running continuous evaluations on production traces instead of static test sets
- Identifying recurring failure patterns across agents, not just single incidents
- Feeding real trajectories into prompt iteration, retrieval tuning, or fine-tuning pipelines

Because OpenInference defines the structure of those traces, the data is rich enough to support that level of analysis instead of being an unstructured log stream.

**Why it matters to you:**

If you are building or operating agents, this changes how you manage them in production:

- You can swap tools (or add new ones) without re-instrumenting your system
- You can run evaluations and debugging workflows on the same trace data
- You avoid rebuilding telemetry pipelines every time your stack changes
- You have a consistent way to audit agent behavior across teams and systems
- You can standardize how reliability and safety are measured
- You are not dependent on a single vendor’s console to understand system behavior

**The theme tying it all together**

The next durable layer in the agent stack may not be another model or framework. It may be the telemetry standard that determines how agent behavior is captured, evaluated, and improved.

OpenTelemetry and OpenInference give teams a path toward portable, structured agent telemetry: traces that can move across platforms, retain enough semantic detail to support evaluation, and become useful beyond debugging.

That is the practical importance of the Google Cloud and Arize collaboration. If agent telemetry becomes standardized, teams get more than better observability. They get a shared foundation for debugging, auditing, comparing, and improving agents in production.

*Learn more about  our enterprise agent development platform Arize AX, and open source observability platform Arize Phoenix. *
