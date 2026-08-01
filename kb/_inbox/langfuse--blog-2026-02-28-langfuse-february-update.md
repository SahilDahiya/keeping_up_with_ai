---
title: Langfuse February Update - Langfuse
kind: blog
topic: null
subtopic: null
secondary_topics: []
summary: null
triage: null
skip_reason: null
source: langfuse
url: https://langfuse.com/blog/2026-02-28-langfuse-february-update
author: null
published: '2026-02-28'
fetched: '2026-08-01T06:49:38Z'
classifier: null
taxonomy_rev: 2
words: 355
content_sha256: 198f3825d6f9edea258ca401f59aa0c4c32fd5f5613187fb3f445ff89cc6e6c1
---

# Langfuse February Update - Langfuse

![Langfuse February Update](https://langfuse.com/_next/image?url=%2Fimages%2Fblog%2F2026-02-28-langfuse-february-update%2Fobservation-centric-model.png&w=3840&q=75) February 28, 2026

# Langfuse February Update

Observation-centric data model, faster UI, Observations API v2 and Metrics API v2 out of beta, faster evaluation workflows

![Picture Marc Klingen](https://langfuse.com/_next/image?url=%2Fimages%2Fpeople%2Fmarcklingen.jpg&w=96&q=75) Marc Klingen

We heard your feedback on performance and took it seriously: Langfuse just got a major speed and scalability upgrade — with faster UI, faster API workflows, and faster evaluation workflows.

## [Observation-centric data model](https://langfuse.com#observation-centric-data-model)

After analyzing query patterns across billions of monthly events, we're introducing changes to scale with our customers. Historically, Langfuse was built around traces & observations as two distinct objects.

Going forward the data model is focused on observations as the primary object. We have written extensively about the technical choice made [here](https://langfuse.com/blog/2026-03-10-simplify-langfuse-for-scale).

![Observation-centric data model](https://langfuse.com/_next/image?url=%2Fimages%2Fblog%2F2026-02-28-langfuse-february-update%2Fobservation-centric-model.png&w=3840&q=75)


The rebuild is based on three core principles that ultimately power simpler and faster database queries:

- **Immutable observations:** Observations are written once and never modified, eliminating deduplication operations
- **No joins:** Trace-level attributes propagate to observations in the SDK. Queries run on a single table without joins
- **Observation-centric model:** Observations are the primary data source for APIs and UI

## [Impact](https://langfuse.com#impact)

![Performance impact](https://langfuse.com/_next/image?url=%2Fimages%2Fblog%2F2026-02-28-langfuse-february-update%2Fimpact-metrics.png&w=3840&q=75)


**Faster UI**

Chart loading times are now significantly shorter. You can now confidently load charts over longer time ranges. Browsing traces, users, and sessions is also much faster, and filters respond more quickly in large projects.

**Faster API workflows**

The new [Observations API v2](https://langfuse.com/docs/api-and-data-platform/features/observations-api#v2) and [Metrics API v2](https://langfuse.com/docs/metrics/features/metrics-api#v2) are officially **out of beta** and ready for production use. They are designed for faster querying and aggregations at scale.

**Faster evaluation workflows**

Observation-level evaluations execute in seconds as they no longer require querying ClickHouse for each evaluation.

## [How to unlock new performance](https://langfuse.com#how-to-unlock-new-performance)

Depending on what performance improvements help you most, here are some steps you can take:

**[1] Struggling with long load times in the UI tables and dashboards?** → flip the toggle in the UI

![UI toggle for new data model](https://langfuse.com/_next/image?url=%2Fimages%2Fblog%2F2026-02-28-langfuse-february-update%2Fui-toggle.png&w=3840&q=75)


**[2] Want real-time data on fast UI?** → [Upgrade SDK](https://langfuse.com/faq/all/upgrade-to-langfuse-v4#ingestion)

**[3] Need more performance in LLM-as-a-Judge?** → [Migrate to observation level evaluators](https://langfuse.com/faq/all/llm-as-a-judge-migration)

**[4] Retrieve data quickly and at scale?** → [Adopt new observations and metrics APIs](https://langfuse.com/faq/all/deprecated-api-migration)
