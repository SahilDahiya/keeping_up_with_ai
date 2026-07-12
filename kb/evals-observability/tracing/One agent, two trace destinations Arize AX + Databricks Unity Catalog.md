---
title: 'One agent, two trace destinations: Arize AX + Databricks Unity Catalog'
topic: evals-observability
subtopic: tracing
secondary_topics:
- infra-platform/deployment
summary: Shows how a single agent can emit traces to multiple destinations, highlighting
  interoperability concerns for observability stacks.
source: arize
url: https://arize.com/blog/one-agent-two-trace-destinations-arize-ax-and-databricks-unity-catalog/
author: Richard Young
published: '2026-06-15'
fetched: '2026-07-11T04:56:40Z'
classifier: codex
taxonomy_rev: 1
words: 1126
content_sha256: 2ff84ad26b76b5be4070475a9eeb76a6a9a6d55de3ac2e00eeea8e233cd29eef
---

# One agent, two trace destinations: Arize AX + Databricks Unity Catalog

[Production traces](https://arize.com/docs/ax/observe/tracing-concepts/what-are-traces) serve more than one purpose.

Engineers use them to debug agent behavior, investigate failures, [run evaluations](https://arize.com/docs/ax/get-started/get-started-evaluations), and understand how systems behave in production. Platform and data teams use the same traces to analyze trends, join telemetry with business data, satisfy governance requirements, and build downstream workflows.

Those needs often lead to separate systems. Observability platforms optimize for interactive debugging. Lakehouses optimize for governance, analytics, and long-term storage.

[OpenTelemetry](https://arize.com/docs/ax/concepts/otel-openinference/overview) does not require teams to choose between them.

A single OpenTelemetry pipeline can export the same spans to multiple destinations at the same time. That means the traces used to debug a production incident can also land in governed storage, where they can be queried with SQL, joined with enterprise data, and reused across the rest of the data platform.

This walkthrough shows how to send one stream of OpenTelemetry traces to both [Arize AX](https://arize.com/docs/ax/get-started/get-started-tracing) and [Databricks Unity Catalog](https://arize.com/blog/harnessing-databricks-mosaic-ai-agent-framework-and-arize-for-next-level-genai-applications/), giving engineering teams an operational view of agent behavior and data teams a governed analytical copy of the same telemetry.

**What each destination is optimized for**

The same trace can support very different workflows.

In Arize AX, traces are optimized for investigation. Engineers can inspect prompts, model responses, tool calls, token usage, latency, and evaluation results in a purpose-built trace explorer. The same traces can be used to run evaluations, investigate regressions, create datasets, and understand how an agent behaved in production.

That workflow is useful when the question is operational:

- Why did this response fail?
- Which tool call introduced the error?
- Which retrieval step returned the wrong context?
- Which prompt version produced this output?
- When did this regression start?

Databricks serves a different purpose.

When traces land in Unity Catalog, they become part of the broader data platform. Teams can query them with [Databricks SQL](https://arize.com/blog/harnessing-databricks-mosaic-ai-agent-framework-and-arize-for-next-level-genai-applications/), join them with business and application data, and govern them with the same controls already applied to the rest of the lakehouse.

That workflow is useful when the question is analytical:

- Which customer segments experience the most failures?
- How does agent latency affect conversion or retention?
- Which prompts generate the highest support volume?
- How do evaluation results change across model versions?
- Which production traces should become training or evaluation data?

The value of dual export is that both workflows operate on the same telemetry. Engineers can investigate production behavior in Arize AX while platform and data teams analyze the same traces in Unity Catalog.

**Why split traces at the source**

A natural question is why send traces to two destinations instead of exporting to one system and copying the data later.

OpenTelemetry already provides a simpler option.

A single trace can be exported to multiple destinations at the point where it is created. That means teams do not need a separate replication pipeline, scheduled export job, or custom ETL process to move telemetry between systems.

Each destination receives the same spans directly from the source.

That approach has two advantages.

First, it preserves the workflow each destination was designed for. Engineers can investigate traces in Arize AX while the same telemetry is available in Unity Catalog for analytics, governance, and downstream data workflows. Neither system depends on a secondary copy process before data becomes available.

Second, it keeps trace data under the same governance model as the rest of the lakehouse. Teams that need auditability, data residency controls, or access management can work from governed Unity Catalog tables without giving up the observability workflows they use for debugging and evaluation.

The result is a single instrumentation layer, a single stream of telemetry, and two destinations that serve different parts of the production workflow.

**What this enables**

Production traces become more valuable when they can be reused across multiple workflows.

A failed trace can start as a debugging artifact in Arize AX. The same trace can later become an evaluation example, a regression test case, a human review task, or part of a training dataset. Because the telemetry also lands in Unity Catalog, teams can analyze those traces alongside customer, product, and operational data without moving them into a separate system.

That creates a shared foundation for engineering, ML, and data teams.

Engineers can investigate failures in Arize AX. ML teams can use production examples to evaluate new prompts, models, and agent configurations. Data teams can query the same traces with Databricks SQL and connect agent behavior to business outcomes.

For teams that already use OpenTelemetry, this pattern does not require additional instrumentation. The application emits a single stream of telemetry. OpenTelemetry handles the fan-out, and each destination receives the same spans directly from the source.

The result is one instrumentation layer, one stream of trace data, and multiple ways to use it.

**The setup**

Full code and example can be found in this [ notebook](https://github.com/Arize-ai/tutorials/blob/main/python/cookbooks/databricks/databricks_dual_ingest_otel.ipynb). (

*This notebook will only run in a Databricks workspace environment.)*

The agent can be written in any framework against any model provider, instrumented with [OpenInference](https://arize.com/docs/ax/concepts/otel-openinference/semantic-conventions) for vendor-agnostic, portable tracing. Nothing about the agent code is special. The interesting part is what happens to the spans after they’re emitted.

We register one `TracerProvider` and attach two span processors to it:

One processor exports to Arize AX for sub-second ingest.

A second processor exports to Databricks, which lands spans in Delta tables under Unity Catalog.

Both processors see the same spans. The OpenTelemetry SDK was designed for this. We’re just using it the way it was built to be used.

```
```
```
from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.exporter.otlp.proto.http.trace_exporter import OTLPSpanExporter
from arize.otel import BatchSpanProcessor as ArizeBatchSpanProcessor
from arize.otel import GRPCSpanExporter as ArizeGRPCSpanExporter, Endpoint
provider = TracerProvider(resource=resource)
# Stream 1: Arize AX for real-time observability
provider.add_span_processor(
    ArizeBatchSpanProcessor(
        span_exporter=ArizeGRPCSpanExporter(
            space_id=space_id, api_key=api_key, endpoint=Endpoint.ARIZE,
        )
    )
)
# Stream 2: Databricks Unity Catalog for governed storage
provider.add_span_processor(
    BatchSpanProcessor(
        OTLPSpanExporter(
            endpoint=f"{host}/api/2.0/otel/v1/traces",
            headers={
                "content-type": "application/x-protobuf",
                "X-Databricks-UC-Table-Name": uc_spans_table,
                "Authorization": f"Bearer {token}",
            },
        )
    )
)
trace.set_tracer_provider(provider)
```
			That’s the entire integration. Once the provider is set, every instrumented call to the LLM, every tool invocation, every chain step produces a span that goes to both destinations.

The full working example, including dependencies, secrets handling, and verification queries, lives in [this Databricks notebook](https://github.com/Arize-ai/tutorials/blob/main/python/cookbooks/databricks/databricks_dual_ingest_otel.ipynb).

**Getting started**

You need three things to try this:

- A Unity Catalog workspace with the OpenTelemetry preview enabled, and a SQL warehouse you can use.
- An Arize space ID and API key.
- An agent already instrumented with OpenInference.

From there, the dual-export wiring is the snippet above. A self-contained Databricks notebook with the full demo, including the LangChain agent and the verification queries, is linked below. If you don’t have an Arize account yet, [sign up for a free Arize AX account](https://arize.com/join) to get a space ID and API key.
