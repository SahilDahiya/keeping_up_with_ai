---
title: Agents are the new services in Pydantic Logfire
kind: blog
topic: evals-observability
subtopic: monitoring
secondary_topics:
- agents/harness
summary: 'Argues agents need service-style observability reinvented for their shape:
  non-deterministic execution paths, per-request token cost, models silently swapped
  or throttled under you, and a data plane that is now a compliance plane (user-typed
  PII in prompts). Contrasts AI-observability vendors (LangSmith, Langfuse, Arize)
  with infra vendors (Datadog, Grafana) and pitches a unified RED-metrics/topology/SLO
  view over a single trace ID.'
triage: null
skip_reason: null
source: pydantic
url: https://pydantic.dev/articles/agents-are-the-new-services
author: Bill Easton
published: '2026-06-15'
fetched: '2026-07-16T22:03:14Z'
classifier: claude
taxonomy_rev: 2
words: 879
content_sha256: 03be2eff9e39171a6b963b7f7d87d76250ed525aa3dc77175918ffe835f76e9c
---

# Agents are the new services in Pydantic Logfire

Your refund agent calls Stripe, retrieves from a vector store, and asks a model whether the customer qualifies. One run in twenty it returns the wrong answer - not an error, an answer, confidently wrong. The model call was fast. The retrieval hit. Nothing logged a stack trace because nothing crashed. The bug is in the seam between three tools, and the three tools live in three different observability products.


It sounds glib. It isn't.

What woke you up is not a service in the sense you have spent the last decade observing. It calls services. It runs on services. It fails in a different shape. The observability you built for services does not catch that shape. It receives a request, it does some work, it returns a response. The work happens to include some LLM calls and some tools. So what?

Four things, mostly.

**Execution paths are non-deterministic.** A service handles a request the same way every time until you get to a distributed system, then things get complicated. An agent has all the unfortunate characteristics of a distributed system right out of the gate. Given the same request, may fire two tools or fifteen, take three turns or twelve. The shape of a run is a runtime property, not a build-time one. A p99 over 100 runs hides what the p99 over 1,000 will tell you.

**Cost is variable per request.** A service costs CPU seconds. An agent costs tokens, and tokens are a thousand to a million times more expensive than CPU seconds, with prices that change every week. Every request has a per-request bill attached measured in dollars not fractions of a penny.

**The dependency moves under you.** A service depends on a database. The database stays the database, you patch it, you upgrade it once a year. An agent depends on a model, and the model is deprecated, throttled, rate-limited, or quietly swapped under you by a provider with their own roadmap. Your latency p99 can double overnight without your code changing.

**Data flows through it and needs governance.** A service sees structured payloads. An agent sees prompts, completions, tool arguments, retrieved chunks. Some of it is PII. Some of it is somebody else's PII. The data plane is now a compliance plane. Users didn't type their credit card numbers into your ecommerce store's search box but when an agent is involved, all bets are off.


Everything we built for services over the last decade (the inventory, the topology graph, RED metrics, deployment markers, SLOs, alerts) needs an agent-shaped reinvention. Agents call services, run on pods, hit the same databases. Both kinds of workload need both kinds of view.

The market has split on which half to build. AI-observability vendors (LangSmith, Langfuse, Helicone, Arize Phoenix, W&B Weave) understand the LLM call beautifully and stop at the SDK boundary. Infra-observability vendors (Datadog, Grafana, New Relic, Dynatrace) are bolting on the OpenTelemetry `gen_ai.*` conventions but do not have the agent-runtime view or the framework integration. Nobody has all of it in one product.

Except Logfire. In one product, with one trace ID propagating through all of it:

- **The gateway.**- [One key for every model provider](https://pydantic.dev/ai-gateway), with budget controls, audit and SSO. The routing layer for the same agents the rest of the product observes.
- **Optimization.**Managed prompt variables with a continuous optimizer that proposes, evaluates and ships better variants from production traffic.
- **Evals.**- [Pydantic Evals](https://ai.pydantic.dev/evals/)for the systematic testing every team eventually needs.
- **Guardrails and Data Loss Prevention.**Prompt and completion scanning for PII, secrets, and policy violations.
- **The agent and LLM views.**A model inventory, per-run distributions, the Tools tab on every agent run.
- **The infra views.**Services, hosts, Kubernetes, metrics. Because the agent still runs on a pod and still calls Redis.


If you build with Pydantic AI, the instrumentation is wired up. If you build with LangChain, LangGraph, the OpenAI SDK, the Anthropic SDK, the Vercel AI SDK, Mastra, CrewAI, AutoGen or anything else that speaks OpenTelemetry, the views in this series light up the same way.

This is the point of building on OpenTelemetry. It is the lingua franca. We are not asking you to instrument again.


Four new views, one per day, each the agent-era equivalent of an observability surface you already know. Every one of them ends in the live view you already use, on the trace that explains the failure.

- **Tuesday.**- [Services and topology](https://pydantic.dev/articles/logfire-services-view). RED per service. A topology graph that draws itself from your traces, edges colored by error rate. The view that tells you whether the slow thing is Redis, Postgres, or the vector DB you tried last quarter.
- **Wednesday.**- [Kubernetes](https://pydantic.dev/articles/logfire-kubernetes-view). Cluster, namespace, workload, pod, node, image. The view that tells you which pod restarted, which deploy broke it, and which workload is hot.
- **Thursday.**- [Hosts](https://pydantic.dev/articles/logfire-hosts-view). CPU, memory, load, disk, network per host. The view that catches the OOM before the trace does.
- **Friday.**- [Metrics explorer](https://pydantic.dev/articles/logfire-metrics-explorer). Three steps from "what am I even shipping?" to a chart. No SQL required, and the SQL is on every card when you need it.

Read along, or [open Logfire](https://pydantic.dev/logfire) and start watching the views populate against your own data. The free tier includes 10 million spans per month, our AI Gateway, and so much more.
