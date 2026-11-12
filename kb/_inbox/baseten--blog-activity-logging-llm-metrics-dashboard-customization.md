---
title: 'New observability features: activity logging, LLM metrics, and metrics dashboard
  customization'
kind: blog
topic: null
subtopic: null
secondary_topics: []
summary: null
triage: null
skip_reason: null
source: baseten
url: https://www.baseten.co/blog/activity-logging-llm-metrics-dashboard-customization
author: Suren Atoyan
published: '2024-12-20'
fetched: '2026-11-12T06:09:34Z'
classifier: null
taxonomy_rev: 2
words: 555
content_sha256: eee188231e4086069949a97203d560ef63faa55ea2508a353921a653e035e54f
---

# New observability features: activity logging, LLM metrics, and metrics dashboard customization

News
# New observability features: activity logging, LLM metrics, and metrics dashboard customization

We added three new observability features for improved monitoring and debugging: an activity log, LLM metrics, and customizable metrics dashboards.


- Authors
- Date
- December 20, 2024

TLDR

We added three new observability features to make monitoring, debugging, and optimizing your production AI workloads even easier: activity logging for timestamped changes across your workspace and models, request-level LLM metrics, and customizable metric views.

At Baseten, we’re laser-focused on powering our customers’ mission-critical AI workloads with unmatched performance and reliability. Comprehensive observability is crucial to ensuring our customers maintain the performance they require—and their end users expect.

Clear metrics and logging are critical for:

- Understanding model performance.
- Detecting and addressing issues before they affect end users.
- Identifying bottlenecks and ensuring optimal resource allocation.

To further enhance observability on Baseten, we’re excited to introduce our latest suite of features: the activity log, LLM metrics, and metrics dashboard customization!

The new activity log helps you monitor and audit changes across your workspace, models, and [Chains](https://docs.baseten.co/chains/overview) with timestamped records assigned to individual users. This adds more clarity to what happens in your workspace and with your models, and makes it easier to debug any changes in performance due to altered settings.

Click the Activity tab to view:

- **Model and Chain activity:** including new, activated, and deactivated model deployments, as well as changes to instance type and autoscaling settings.
- **Organization-level changes:** including updates to teammates and secrets.

Working with LLMs often involves working with variable input and output lengths. This can make it difficult to determine whether a spike in inference time is due to a model issue or simply a change in the input/output interaction.

To provide the necessary context, we added three request-level metrics for:

- Request size
- Response size
- Time to first byte

Time to first byte shows whether users are getting quick responses regardless of overall latency, while request and response sizes are useful for narrowing down the causes of any increased latency.

Together, LLM metrics paint a fuller picture of how your LLMs are performing in production while making debugging quicker and easier.

Rapid debugging cycles are essential for fast releases. For simplified monitoring, we redesigned our metrics interface to provide:

- **A unified view:** All metrics are now displayed on a single page—no clicking between tabs.
- **Customizable views:** Drag and reorder graphs, hide irrelevant charts, and organize metrics based on their priority.
- **One-click logs access:** Hover over a graph and click “Logs” on the x-axis to jump to the relevant logs at that point in time.

Quickly identify and debug errors while keeping your most relevant metrics front and center. Plus, with custom views (and all your charts in one place), finding correlations between latency, inference volumes, and request metrics is straightforward.

Custom views persist per user, so everyone in your workspace can make it their own!

From day one, we’ve been committed to pairing industry-leading AI infrastructure with a second-to-none developer experience. Whether you’re leveraging a dedicated deployment on Baseten Cloud, [Self-Hosted](https://www.baseten.co/blog/baseten-self-hosted/), or [Hybrid](https://www.baseten.co/blog/baseten-hybrid-control-and-flexibility-in-your-cloud-and-ours/), we ensure transparency and confidence in how your user-facing applications perform.

Check out our [metrics export tooling](https://www.baseten.co/blog/export-model-inference-metrics-to-observability-tools/) if you’re interested in more observability features, and [reach out](https://www.baseten.co/talk-to-us/) to get industry-leading performance for your models in production!
