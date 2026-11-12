---
title: Export your model inference metrics to your favorite observability tool
kind: blog
topic: null
subtopic: null
secondary_topics: []
summary: null
triage: null
skip_reason: null
source: baseten
url: https://www.baseten.co/blog/export-model-inference-metrics-to-observability-tools
author: Helen Yang
published: '2024-10-02'
fetched: '2026-11-12T06:09:16Z'
classifier: null
taxonomy_rev: 2
words: 509
content_sha256: 47cd3d8e31077f3b6346d112a7e05b5f340adb02e8263f20ee27fedd51b8c323
---

# Export your model inference metrics to your favorite observability tool

News
# Export your model inference metrics to your favorite observability tool

Export model inference metrics like response time and hardware utilization to observability platforms like Grafana, New Relic, Datadog, and Prometheus.


- Authors
- Date
- October 2, 2024

Today, we’re excited to announce our new export metrics integration, which lets you export model inference metrics like response time, replica count, and hardware utilization to a long list of observability platforms including Grafana, New Relic, Datadog, and Prometheus.

Exporting metrics unlocks key improvements to production model management workflows:

- **Single source of truth**: unify data within your observability stack and build dashboards that integrate every component of your AI-powered applications.
- **Fine-grained metrics and control**: dive deeper into your metrics with the power of dedicated tooling.
- **Custom alerts**: wire in your inference metrics to get alerts for unexpected traffic, latency, or status codes.

Integrating metrics from model inference into your broader observability stack is essential for operating AI-powered applications in production.

Rime’s model serving infrastructure is mission-critical – our stellar uptime relies on Baseten’s stellar uptime. We have complex deployments combining multiple models with key infrastructure components, all of which needs to be monitored. Adding our Baseten metrics to our Grafana dashboards lets us apply the same DevOps best practices to our AI models that we do to our other critical components.


To start integrating your inference metrics with your existing observability tools, [check out the documentation](https://docs.baseten.co/observability/export-metrics/overview) or read on for answers to common questions.

Almost everything that you see in the “Metrics” tab for a model in your Baseten workspace can be exported via this integration.

Available metrics include:

- **Inference request count**, with status, environment (i.e. production vs development), and more.
- **End-to-end response time**, including the status and environment.
- **Replica count**, both active and starting up.
- **Hardware usage**, both compute and memory, for CPU and GPU resources.

For a full reference, see the [metrics support matrix](https://docs.baseten.co/observability/export-metrics/supported-metrics) in the documentation.

Our metrics export is based on the vendor-neutral [OpenTelemetry](https://opentelemetry.io/) standard to maximize compatibility across platforms. Metrics are integrated by configuring a Prometheus receiver for an OpenTelemetry Collector.

Metrics are available via a `/metrics` endpoint, which observability tools can scrape at a set interval (we generally recommend every 60 seconds). Collecting metrics requires configuring a receiver, such as this example for Prometheus:

```
global:
  scrape_interval: 60s
scrape_configs:
  - job_name: 'baseten'
    metrics_path: '/metrics'
    authorization:
      type: "Api-Key"
      credentials: "{BASETEN_API_KEY}"
    static_configs:
      - targets: ['app.baseten.co']
    scheme: https
```
See the [export metrics documentation](https://docs.baseten.co/observability/export-metrics/overview) for details on receiver configuration.

We chose to implement our exporting feature with OpenTelemetry in mind for the broad compatibility it gives across a wide range of tools. You can scrape Baseten inference metrics from any [exporter in the OpenTelemetry registry](https://opentelemetry.io/ecosystem/registry/?component=exporter) – over 800 tools at the time of writing.

In addition to this broad support, we’ve ensured compatibility with and written specific documentation for a set of popular platforms:

To confirm support or add documentation for your favorite observability platform, [get in touch](mailto:support@baseten.co) and we’ll work with you to build and test the integration!
