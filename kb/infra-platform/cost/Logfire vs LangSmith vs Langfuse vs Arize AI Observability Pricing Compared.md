---
title: 'Logfire vs LangSmith vs Langfuse vs Arize: AI Observability Pricing Compared'
kind: blog
topic: infra-platform
subtopic: cost
secondary_topics:
- evals-observability/monitoring
summary: Breaks down how AI-observability billing units (spans, traces, GB ingested,
  Langfuse-style billable units) interact with agentic/RAG workloads, noting LLM spans
  carry tens of KB payloads (system prompts, retrieved chunks, completions) versus
  sub-KB REST spans. Compares Logfire, LangSmith, Langfuse, and Arize pricing to show
  the billing unit, not the headline fee, drives real cost.
triage: null
skip_reason: null
source: pydantic
url: https://pydantic.dev/articles/ai-observability-pricing-comparison
author: Chris Samiullah
published: '2026-03-31'
fetched: '2026-07-16T22:04:02Z'
classifier: claude
taxonomy_rev: 2
words: 1454
content_sha256: 4302c2980623be292ddfc0fe33686af3d045a22b83eb3fbbcce0346dbf6a8f41
---

# Logfire vs LangSmith vs Langfuse vs Arize: AI Observability Pricing Compared

The observability market is currently split in two. On one side: general-purpose platforms like Datadog, Grafana, and Honeycomb, built for traditional infrastructure and application monitoring. On the other: a new crop of "AI observability" tools - LangSmith, Langfuse, Arize - purpose-built for LLM workflows.

We think this bifurcation is temporary.

Just as we no longer talk about "cloud observability" as a separate category (it's just observability), LLM support will eventually be table stakes. Teams will want one place for everything - their APIs, their databases, their agents, their evals - rather than context-switching between a general-purpose platform and a specialist AI tool. The vendors who win that future will be the ones engineers trusted first on their AI workflows.

That's the bet behind [Logfire](https://pydantic.dev/logfire)'s pricing. We're not optimizing to extract maximum revenue from AI observability in 2026. We're pricing to become the platform teams reach for across their entire stack - which means making it genuinely affordable to instrument everything, now, so that trust compounds over time.

Monitoring AI applications is nothing like monitoring a traditional web service - but not in the way you might expect. AI-only observability tools are scoped to trace LLM-specific operations: the model call, the retrieval steps, the eval scores. Everything else in your application - the HTTP layer, database queries, background workers - goes uninstrumented. That narrow scope is a structural constraint: these platforms ingest only a fraction of the telemetry a general-purpose platform would collect from the same application.

What makes that fraction expensive is payload size. Each span in an LLM trace carries outsized data: system prompts, retrieved document chunks, full model completions - often tens of kilobytes per span versus the sub-kilobyte payloads typical of REST API calls. AI observability vendors face a structural challenge: low ingestion volumes mean they need to charge more per span to sustain their businesses, and several add a separate data-volume charge on top to recover storage costs.

This creates a surprisingly high-stakes procurement decision. The billing unit your vendor chooses - spans, traces, gigabytes, or some proprietary blend - interacts with your workload in ways the headline monthly fee completely obscures. We ran the numbers.


Before comparing prices, you need to understand what each vendor is actually charging for.

**Spans** are the atomic unit of OpenTelemetry: a single timed operation. A single user request in an agentic or RAG application might generate a handful of spans or hundreds, depending on complexity - but each carries much larger payloads than you'd see in a conventional web service trace. We use 25 spans per trace as a modelling assumption throughout this comparison.

**Traces** group all the spans for a single request into one logical container. Billing by trace penalizes complexity - a 50-step autonomous agent costs the same as a single LLM call if you're billed per span, but 50× more if you're billed per trace.

**Langfuse Billable Units** are an aggregate of traces + spans + evaluation scores. A 10-span trace with one automated eval score costs 12 billable units.

**Arize adds a second axis**: both span count *and* raw data volume in GB. RAG applications that log large context windows get hit twice.


To make this concrete, we modeled three realistic scenarios using consistent assumptions: 25 spans per trace, 5 KB per span average payload, and 1 eval score per trace for Langfuse unit calculations.

You can explore the full numbers in [this Google Sheet](https://docs.google.com/spreadsheets/d/1NXyjGTSDNMhh_4sDPxQuaqBPho84euVJnhTscVo_tZ4/edit?gid=1687382227#gid=1687382227).

| Logfire | Arize AX Pro | Langfuse | LangSmith | |
|---|---|---|---|---|
| Billing model | Spans ($2/1M) | Spans + GB ($10/1M + $3 per GB) | Proprietary units (graduated) | Seats + Traces ($39/seat + $2.50/1K traces) | 
| 1 user, 5M spans/mo | $0 | $99 | $451 | $514 | 
| 5 users, 50M spans/mo | $129 | $999 | $3,451 | $5,170 | 
| 20 users, 500M spans/mo | $1,229 | $12,249 | $36,801 | $50,755 | 

The gap is not marginal. At moderate production scale (5 users, 50M spans), Logfire is **8× less expensive than Arize**, **27× less expensive than Langfuse**, and **40× less expensive than LangSmith**.



LangSmith's free Developer tier locks you to one user and 5,000 traces per month. The moment you add a second engineer, you're on the Plus plan at $39 per seat per month. Five engineers costs $195 before you've ingested a single trace.

The trace-based overage pricing compounds the damage. At 50M spans (2M traces at 25 spans per trace), the overage alone exceeds $4,900. Data retention defaults to just 14 days; extending to 400 days doubles your per-trace cost.

The practical consequence: LangSmith customers routinely sample down to 0.1% of their actual traffic to keep costs manageable. For AI applications, where failures are probabilistic and context-dependent edge cases, sampling away 99.9% of your telemetry defeats the entire purpose of having observability.

See our full [Logfire vs LangSmith comparison](https://pydantic.dev/logfire/vs-langsmith).


Langfuse's Core plan ($29/mo) looks reasonable until you factor in how quickly the included 100,000 billable units are consumed. Because every trace, span, and evaluation score is counted separately, a 10-span trace with one eval score costs 12 units. A 5M span workload requires roughly 6M units - consuming the included allowance in under a day of moderate traffic.

Overage pricing is graduated ($8.00 → $6.00 per 100K units), but the absolute numbers climb steeply. At 50M spans across a 5-person team, the monthly bill reaches $3,451.

Self-hosting avoids the per-unit cost but introduces serious infrastructure overhead. Real-world deployments have required 500+ vCPUs to handle moderate ingestion volumes, turning the "free" option into a five-figure AWS bill plus dedicated DevOps time.

See our full [Logfire vs Langfuse comparison](https://pydantic.dev/logfire/vs-langfuse).


Arize's dual-axis model charges $10 per million spans over the limit *and* $3 per GB of payload. For simple applications this is manageable. For any application logging prompts and completions in full, it's punishing.

A 50M span workload generates roughly 250 GB of telemetry at 5 KB per span. The Pro plan includes 100 GB; the remaining 150 GB costs $450 in data overages on top of the span overages. Data retention is capped at 15 days on the Pro tier.

More insidiously, this model creates a perverse incentive: developers start truncating prompt and completion logging to avoid gigabyte charges. When the model hallucinates in production, the trace that might have explained why has been deliberately stripped of the context that caused the problem.

See our full [Logfire vs Arize AX Pro comparison](https://pydantic.dev/logfire/vs-arize).


Logfire charges $2.00 per million spans, flat. No per-trace multiplier. No gigabyte surcharge. Seat limits vary by plan tier, but overage costs are driven purely by span volume - not by headcount.

The free Personal plan covers 10M spans per month for a solo developer with a hard cap to prevent bill shock. The Team plan ($49/mo) adds overage billing at the same flat rate. The Growth plan ($249/mo) removes seat limits entirely, making it practical to give engineers, product managers, and data scientists access without triggering a procurement review each time.

Because the marginal cost of a span is $0.000002, organizations can afford full 100% ingestion. No sampling. No truncation. When something breaks, the trace is complete.

This pricing is also a direct consequence of how Logfire is built. The platform is built on Apache DataFusion, giving us a high-performance query engine without the operational overhead of running a large external database cluster. The infrastructure cost of processing a span is genuinely low, which is why we can charge genuinely low prices and still build a sustainable business.

The longer-term vision matters here too. As AI functionality becomes table stakes in every application, teams will consolidate their observability tooling. The platform that earns trust on AI workflows today - by being affordable enough to instrument everything, and reliable enough to trust at scale - is the one that earns the right to monitor the rest of the stack tomorrow. That's why we price the way we do.


The headline monthly fee of an observability platform is almost irrelevant. What matters is the billing primitive and how it interacts with your actual workload.

- Trace-based billing (LangSmith) collapses under agentic workloads where one user action generates dozens of spans.
- Proprietary unit blending (Langfuse) hides a multiplier effect that accelerates spend faster than the raw numbers suggest.
- Dual-axis volume pricing (Arize) actively punishes RAG architectures and incentivizes the kind of telemetry truncation that makes debugging impossible.
- Flat span pricing (Logfire) aligns cost directly with application load, stays predictable at every scale, and never creates incentives to discard the data you actually need.

If you're building production AI applications and paying more than $2 per million spans for observability, it's worth running the numbers for your own workload.
[Start here](https://pydantic.dev/pricing).
