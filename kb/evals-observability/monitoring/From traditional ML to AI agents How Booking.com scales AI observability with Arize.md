---
title: 'From traditional ML to AI agents: How Booking.com scales AI observability
  with Arize'
kind: blog
topic: evals-observability
subtopic: monitoring
secondary_topics:
- product-engineering/case-studies
summary: Case study on how Booking.com built a unified observability architecture
  on Arize, routing OpenTelemetry/OpenInference traces for GenAI agents and tabular
  prediction logs for traditional ML into one platform; details a latency-regression
  investigation traced to a missing model service tier, and using eval scores plus
  P90 token counts to catch context bloat from long attraction URLs accumulating in
  conversation history.
triage: null
skip_reason: null
source: arize
url: https://arize.com/blog/booking-com-ai-observability/
author: Press
published: '2026-07-27'
fetched: '2026-07-28T06:51:49Z'
classifier: claude
taxonomy_rev: 2
words: 2008
content_sha256: ea826fac9ebd5af9f0128082c9838d223f3fe330d81e6e92b151bbd80fddc5b3
---

# From traditional ML to AI agents: How Booking.com scales AI observability with Arize

**Why Booking.com needs AI observability at scale**

At Booking.com, AI helps travellers in every step of their journey, from how people discover destinations to the way we support them while they’re on the road. Rather than a single flagship model, we rely on a large and growing collection of systems that each solve a specific problem at scale.

To make this concrete, consider a few examples:

- **Trip planning assistants**that help travelers turn vague ideas (“somewhere warm in April with good hiking”) into concrete, bookable itineraries.
- **On‑site helpers**that turn property details, amenities, reviews, and options into plain-language guidance, so people can choose the right stay with confidence.
- **Partner copilots**that help accommodation partners and other suppliers respond to guest messages faster and more consistently, while still staying in control of the final reply.
- **Ranking systems**that decide which options to show first in search and recommendation to surfaces, balancing user relevance with experimentation needs.
- **Fraud detection models**that quietly protect customers and partners in the background by flagging suspicious activity before it turns into real harm.

Each of these systems is built and iterated on by different teams, uses different data, and runs under different constraints such as real‑time vs batch, strict latency budgets vs more relaxed ones, fully automated vs human‑in‑the‑loop.

As we scale this ecosystem, **observability becomes a first‑class requirement**, not a nice‑to‑have as we need to:

- Know when something changes in the real world, a new travel pattern, a data quality issue, a misconfiguration and how that affects model behaviour and user experience.
- Detect regressions early: slower responses, more confusing answers, drops in relevance or conversion, or subtle shifts that only show up for specific geographies, devices, or user segments.
- Demonstrate responsible behaviour: protecting personal data, avoiding harmful or biased outputs, and understanding why a model or agent acted the way it did in a particular case.

Observability matters for every ML system, from traditional models that rank results or flag fraud to agentic GenAI workflows that plan, retrieve information, call tools, and sometimes involve human review. What changes with agentic systems is not the importance of observability, but the complexity of what we need to observe: a single user interaction can become a chain of prompts, model calls, retrieval steps, tool invocations, policy checks, and fallback decisions. Aggregate model metrics and service dashboards may still show that something is slow, costly, or failing, but they often cannot explain how the system reached a particular response. For these workflows, we need end-to-end observability that [traces](https://arize.com/glossary/trace/) the full path from user request to final outcome.

When we talk about **AI observability** in this article, we mean the ability to:

- Reconstruct what an AI system did for a given request, end‑to‑end.
- Measure quality, performance, and reliability over time and across cohorts.
- Quickly go from “something looks off” to a concrete, data‑backed explanation and a targeted fix.

To make that possible across both Traditional ML and GenAI, we rely on a dedicated observability platform that can ingest our signals, surface the right views for practitioners, and help teams debug and improve their systems. In the next section, we’ll introduce that platform Arize and explain the role it plays in our AI ecosystem. And, later we’ll dive into how we generate and route the underlying telemetry. Finally, we’ll review some case studies of how we’re using the platform.

**How Booking.com uses Arize for ML and AI observability**

Building on this landscape, the next challenge is supporting these diverse AI use cases within a single, cohesive platform. This means accommodating both traditional machine learning workflows and newer generative AI applications without fragmenting tooling or processes. Arize provides an AI engineering platform that connects development and production environments, enabling our teams to build, evaluate, and improve AI applications at scale.

Built on the [OpenTelemetry](https://arize.com/docs/ax/concepts/otel-openinference/overview) Protocol, Arize captures traces from both production and development environments, providing visibility into [LLM workflows](https://arize.com/docs/ax/observe/tracing-concepts/what-are-traces) and [agent interactions](https://arize.com/ai-agents/). [OpenInference](https://arize-ai.github.io/openinference/), created and maintained by the Arize team, extends OpenTelemetry with AI-specific conventions for tracing LLM calls, retrieval operations, agent actions, and tool usage, ensuring that traces capture the context needed to understand complex AI applications. [Traces](https://arize.com/glossary/trace/) allow the team to dive deep into specific components of a workflow or application and identify targeted areas for improvement.

![](https://arize.com/wp-content/uploads/2026/07/booking-image-02.png)

Beyond basic tracing, Arize enables us to set up alerts and dashboards not just on trace/span attributes, but on [evaluations](https://arize.com/glossary/evaluations/) and custom metrics created within the platform. This means we can monitor application quality metrics – like user frustration rates – alongside traditional operational metrics, giving us a comprehensive view of system health. We can also create datasets for experimentation directly from [production data](https://arize.com/blog/from-production-traces-to-better-ai-agents-automating-the-llmops-feedback-loop/), ensuring we have real-world examples to iterate on.

For traditional ML workloads, Arize provides [drift detection](https://arize.com/docs/ax/observe/monitors/performance-and-drift-monitors) across features and model predictions, helping our teams catch data distribution shifts that could impact model performance. The platform provides tools to analyze model performance through [cohort analysis](https://arize.com/docs/ax/observe/dashboards), making it easier to identify underperforming segments and understand model behavior across different populations.

![Arize performance and cohort analysis for traditional ML models](https://arize.com/wp-content/uploads/2026/07/booking-image-03.png)

Additionally, Arize provides visibility into [feature importance](https://arize.com/docs/ax/observe/explainability) values, allowing teams to understand which features contribute most to given predictions. This explainability helps with debugging model decisions and building trust with stakeholders who need to understand how models arrive at their outputs.

**How Booking.com collects telemetry for AI observability**

To make observability work across different AI systems, we turn their runtime behaviour into telemetry. For GenAI and agentic workflows, this usually means traces that show the steps behind a user interaction. For traditional ML models, it usually means structured prediction logs with features, outputs, labels, and model metadata. Both paths ultimately feed into Arize, but they are collected and prepared differently.

**GenAI traces for agents: AI telemetry collector**

GenAI and agentic applications are instrumented using OpenTelemetry and AI-specific tracing conventions such as [OpenInference](https://arize-ai.github.io/openinference/). This gives teams a consistent way to represent the main parts of an AI workflow: model calls, retrieval steps, tool usage, guardrails, fallback decisions, latency, token usage, and other metadata needed for debugging.

These traces are sent to a dedicated AI telemetry collector before they are used for observability. At a high level, the collector receives traces from applications, samples them to manage volume, applies centralized PII-aware redaction according to internal data-security standards and applicable privacy requirements, and then routes the redacted traces to downstream systems such as Arize and internal analytics environments.

This design gives teams near-real-time visibility into agent behaviour without every application team needing to build its own custom logging pipeline. It also makes the telemetry path more resilient: short-term spikes or downstream delays can be absorbed by the pipeline, while redaction and routing remain centralized and consistent.

![Booking.com GenAI AI telemetry collector architecture with PII redaction and Arize export](https://arize.com/wp-content/uploads/2026/07/booking-image-04.png)

**Logs for traditional ML: from a data warehouse to Arize**

For traditional ML models, such as ranking or fraud detection, observability is usually based on tabular prediction logs rather than traces. These logs capture the information needed to understand model behaviour over time: selected input features, predictions, labels when they become available, timestamps, model metadata, and explainability signals where applicable.

This path is intentionally different from raw production logging. The tabular logs prepared for observability do not contain sensitive data. Sensitive attributes and personal data are excluded before records are made available for analysis, and models with stricter requirements may log only approved fields, sampled records, or aggregated signals rather than every prediction. This keeps the observability dataset useful for debugging while staying aligned with internal data-security and privacy expectations.

Most of this data is prepared from our data warehouse before being ingested into Arize. The pipeline samples and enriches prediction records, reshapes them into model-specific datasets, and connects them to the right teams, use cases, and model metadata. Once ingested, teams can use Arize to monitor distributions, detect drift, analyze performance across cohorts, and investigate individual model behaviour when needed.

![Booking.com traditional ML prediction-log pipeline from warehouse to Arize](https://arize.com/wp-content/uploads/2026/07/booking-image-05.png)

**A unified observability architecture for AI agents and traditional ML**

From a practitioner’s point of view, GenAI and traditional ML systems show up differently. Agentic applications are usually debugged through traces, where teams inspect the sequence of prompts, model calls, tools, retrieval steps, and evaluations. Traditional ML models are usually debugged through production datasets, where teams inspect features, predictions, labels, drift, cohorts, and explainability signals.

Behind the scenes, both paths follow the same principles: standardized telemetry, centralized governance, privacy-aware handling of data, and a shared observability platform that helps teams understand what their AI systems are doing in production.

**AI observability use cases at Booking.com**

**Detecting AI agent latency regressions in production**

As part of our partnership with Arize, Booking.com monitors model and agent performance in production with fine-grained views, including latency drifts by **agent type**.

In one case, an Arize monitor fired when latency for a specific agent suddenly spiked several standard deviations above its baseline. Using Arize, our team quickly pulled concrete examples of slow calls to the alerting agent and confirmed that a new configuration was deployed as an experiment using a different model than before.

Arize helped us identify that the higher latency wasn’t random. It stemmed from the fact that this model was running without a service tier enabled. With this insight, our team could take a straightforward operational action: coordinate with the provider to enable the appropriate service tier and restore expected latency.

Here Arize gave Booking.com the observability and granularity needed to detect performance regressions early, pinpoint their causes, and translate monitoring signals into targeted fixes rather than guesswork.

**Using AI evaluations to detect context bloat in a chatbot agent**

Arize is not only monitoring production but is also connected to our developer environment. During internal prototyping of one of our itinerary-planning chatbot agents, we noticed that messages **after** the initial itinerary response were consistently receiving lower evaluation scores.

While the first reply from the agent looked strong, the quality and reliability of subsequent turns in the conversation degraded in a way that suggested something was off in the underlying setup rather than the model itself.

Using Arize to compare conversations from the new itinerary agent against those from the existing agent, we saw a clear pattern in the dashboards: the token count for the new agent was significantly higher, with **P90 token counts** spiking relative to the existing configuration.

Digging deeper, we connected this to a key change in the new agent: it started returning links to attractions, and those Booking.com attraction URLs are quite long. We were also feeding those long links back into the model as part of the conversation history for subsequent turns. As a result, the context ballooned over time, and this context bloat correlated with the drop in evaluation scores across multi-turn conversations.

Thanks to that visibility in Arize during prototyping, we were able to intervene before this configuration reached production.

**Scaling AI observability across Booking.com**

As AI systems evolve from standalone models to complex, multi-step agents, observability needs to evolve with them. At Booking.com, this means moving beyond isolated metrics and building a unified view that captures what our systems actually do in production, across both GenAI workflows and traditional ML models.

By standardizing telemetry, using traces for agents and logs for Traditional ML, and routing both into a single platform, we give teams a consistent way to understand, debug, and improve their systems. Whether it is investigating a latency spike, diagnosing a subtle regression, or explaining a model’s decision, the goal is always the same: reduce time from signal to insight to action.

Arize plays a central role in this approach, connecting development and production, and providing the tools to analyze AI behavior at the right level of abstraction. Combined with our internal pipelines for telemetry collection, redaction, and enrichment, it enables observability that scales with both system complexity and organizational needs.

At Booking.com, making AI observable is part of making AI trustworthy, and making it trustworthy is part of our broader mission: **to make it easier for everyone to experience the world**.
