---
title: OpenTelemetry (OTel) for LLM Observability
topic: evals-observability
subtopic: tracing
secondary_topics:
- infra-platform/deployment
summary: Introduces OpenTelemetry for LLM observability and how OTel-style traces
  can standardize spans, metadata, and interoperability across AI systems.
source: langfuse
url: https://langfuse.com/blog/2024-10-opentelemetry-for-llm-observability
author: null
published: '2024-10-14'
fetched: '2026-07-11T04:34:51Z'
classifier: codex
taxonomy_rev: 1
words: 1133
content_sha256: 181cc184b15736181c8977bbd1e5193fddeefc2db9f488f5a81ae1fa30b02c79
---

# OpenTelemetry (OTel) for LLM Observability

# OpenTelemetry (OTel) for LLM Observability

Explore the challenges of LLM observability and the current state of using OpenTelemetry (OTel) for standardized instrumentation.

![Picture Marc Klingen](https://langfuse.com/_next/image?url=%2Fimages%2Fpeople%2Fmarcklingen.jpg&w=96&q=75) Marc Klingen

Marc Klingen**Update**: We have released the [Langfuse OTel Endpoint](https://langfuse.com/docs/opentelemetry/get-started) to increase compatibility with emerging OTel-based instrumentation libraries.

[Introduction to ](https://langfuse.com#introduction-to-)![OpenTelemetry Logo](/images/blog/2024-10-opentelemetry-for-llms/opentelemetry-logo.svg)


[OpenTelemetry](https://opentelemetry.io/) is an open-source observability framework designed to handle the instrumentation of applications for collecting traces, metrics, and logs. It helps developers monitor and troubleshoot complex systems by providing standardized tools and practices for data collection and analysis.

OpenTelemetry supports various exporters and backends, making it flexible and adaptable to different environments. By using OpenTelemetry, applications can achieve better visibility into their operations, aiding in root cause analysis and performance optimization.

[Goal of this post](https://langfuse.com#goal-of-this-post)

This post is a high-level overview of the challenges of LLM observability and the current state of using OpenTelemetry (OTel) for LLMOps.

OTel is geared towards general observability, and **traces are a great standardized way to capture LLM application data** – we have recorded a [webinar](https://langfuse.com/guides/videos/webinar-observability-llm-systems) on this. While we are excited about OTel and the roadmap towards it across LLMOps tools, non-OTel LLMOps tools are preferred by many teams. This post explores why this is the case and how OTel can address these challenges in the future.

*Example trace of our  public demo*

[Outline](https://langfuse.com#outline)

- Overview of LLM Application Observability
- Unique Challenges
- Comparison with Traditional Observability
- Experimentation vs. Production Monitoring

- OpenTelemetry (OTel) for LLM Observability
- Current State
- My Personal View


[1. Overview of LLM Application Observability](https://langfuse.com#1-overview-of-llm-application-observability)

[LLM Application Observability](https://langfuse.com/faq/all/llm-observability) refers to the ability to monitor and understand how Large Language Model applications function, especially focusing on aspects like performance, reliability, and user interactions. This involves collecting and analyzing data such as traces, metrics, and logs to troubleshoot issues and [optimize the application](https://langfuse.com/faq/all/llm-analytics-101).

[Unique Challenges](https://langfuse.com#unique-challenges)

LLM applications present distinct challenges compared to traditional software systems. Evaluating the quality of LLM outputs is inherently complex due to their non-deterministic nature. Metrics like [cost](https://langfuse.com/docs/model-usage-and-cost), [latency](https://langfuse.com/docs/analytics/overview), and [quality](https://langfuse.com/docs/scores/overview) must be balanced and cannot be purely derived from traces as they are in traditional applications.

Additionally, the interactive and context-sensitive nature of LLM tasks often requires real-time monitoring and rapid adaptation. Addressing these challenges demands robust tools and frameworks that can handle the dynamic and evolving nature of LLM applications.

[Comparison with Traditional Observability](https://langfuse.com#comparison-with-traditional-observability)

Traditional observability focuses on identifying exceptions and compliance with expected behaviors. LLM observability, however, requires monitoring dynamic and stochastic outputs, making it harder to standardize and interpret.

| Observability | LLM Observability | |
|---|---|---|
| Async instrumentation(not in critical path) | ✅ | ✅ |
| Spans / traces(as core abstractions) | ✅ | ✅ |
| Metrics | ✅ | ✅ |
| Exceptions | At runtime | Ex-post (evaluations, annotations, user feedback, …) |
| Main use cases | Alerts, metrics, aggregated performance breakdowns | Debug single traces, build datasets for application benchmarking/testing, monitor hallucinations/evals |
| Users | Ops | MLE, SWE, data scientists, non-technical |
| Focus | Holistic system | Focus on what's critical for LLM application |

[Experimentation vs. Production Monitoring](https://langfuse.com#experimentation-vs-production-monitoring)

In development, experimentation with various models and configurations is crucial. Developers iterate on different approaches to fine-tune model behavior, optimize performance metrics, and explore new functionalities.

Production monitoring, however, shifts the focus to real-time performance tracking. It involves constant vigilance to ensure the application runs smoothly, identifying any latency issues, [tracking costs](https://langfuse.com/docs/model-usage-and-cost), and integrating [user interactions and feedback](https://langfuse.com/docs/scores/user-feedback) to continuously improve the application. Both phases are essential, but they have distinct objectives and methodologies geared towards pushing the boundaries of what the LLM can achieve and ensuring it operates reliably in real-world scenarios.

| Development | Production |
|---|---|
| Debug step-by-step, especially when using frameworks | Monitor: cost / latency / quality |
| Run experiments on datasets and evaluations | Debug issues identified in prod based on user feedback, evaluations, and human annotations |
| Document and share experiments | Cluster user intents |

[2. OpenTelemetry (OTel) for LLM Observability](https://langfuse.com#2-opentelemetry-otel-for-llm-observability)

[Current State](https://langfuse.com#current-state)

The OpenTelemetry Special Interest Group (SIG) focused on "Generative AI Observability" pushes for standardized semantic conventions for LLM/GenAI Applications and instrumentation libraries for the most popular model vendors and frameworks. Learn more about the SIG in its [project doc](https://github.com/open-telemetry/community/blob/main/projects/gen-ai.md) and [meeting notes](https://docs.google.com/document/d/1EKIeDgBGXQPGehUigIRLwAUpRGa7-1kXB736EaYuJ2M/edit?tab=t.0#heading=h.ylazl6464n0c).

Deliverables of the working group (as of Oct 14, 2024) include:

Immediate term:


- Ship OTel instrumentation libraries for OpenAI (or any other GenAI client) in Python and JS following existing conventions
Middle term:


- Ship OpenTelemetry (or native) instrumentations for popular GenAI client libraries in Python and JS covering chat calls
- Evolve GenAI semantic conventions to cover other popular GenAI operations such as embeddings, image or audio generation
As a result, we should have feature parity with the instrumentations of existing GenAI Observability vendors for a set of client instrumentation libraries that all vendors can depend upon.

Long term:


- Implement instrumentations for GenAI orchestrators and GenAI frameworks for popular libraries in different languages
- Evolve GenAI and other relevant conventions (DB) to cover complex multi-step scenarios such as RAG
- Propose mature instrumentations to upstream libraries/frameworks

Currently, there's a mix of progress and ongoing challenges. Significant issues include dealing with large traces, diverse LLM schema implementations (often biased towards OpenAI), and capturing evaluations and annotations. Many OTel-based LLM instrumentation libraries don't strictly adhere to evolving conventions, resulting in vendor-specific solutions.

[My Personal View](https://langfuse.com#my-personal-view)

Despite the challenges, I'm excited about OTel instrumentation in the mid-term. The real value lies in its standardized data model, enabling seamless workflow integration across various frameworks and platforms. This standardization leads to increased interoperability across vendors, which is the main reason why OTel is interesting. Currently, we maintain [countless integrations](https://langfuse.com/integrations) with popular models/frameworks/languages but can't support the long tail due to capacity constraints. Standardizing on OTel will allow the ecosystem to crowdsource instrumentation efforts, benefiting everyone and enabling LLMOps vendors to focus more on core features rather than maintaining numerous integrations. These developments are essential for achieving consistent and reliable observability across diverse LLM frameworks and platforms.

We are committed to OTel and are happy to contribute to the SIG. We will continue to maintain our integrations and SDKs and are currently exploring adding an OTel collector to allow for integrations with OTel-based instrumentation libraries.

If you are interested in contributing to our OTel efforts, join the [GitHub
Discussion thread](https://github.com/orgs/langfuse/discussions/2509).

**Update**: We have released a [Langfuse OTel Collector](https://langfuse.com/docs/opentelemetry/get-started) to increase compatibility with emerging OTel-based instrumentation libraries.

[Get Started](https://langfuse.com#get-started)

If you want to get started with tracing your AI applications with Langfuse today, check out our [quickstart guide](https://langfuse.com/docs/get-started) on how to use Langfuse with multiple LLM building frameworks like [Langchain](https://langfuse.com/integrations/frameworks/langchain) or [LlamaIndex](https://langfuse.com/integrations/frameworks/llamaindex).

If you are curious about why Traces are a good fit for LLM observability, check out our [webinar](https://langfuse.com/guides/videos/webinar-observability-llm-systems) on the topic.
