---
title: How we use agents to review production infrastructure
topic: product-engineering
subtopic: case-studies
secondary_topics:
- agents/tool-use
- infra-platform/deployment
summary: Case study of using agents to review production infrastructure, including
  operational workflows, review boundaries, and human oversight.
source: langfuse
url: https://langfuse.com/blog/2026-06-05-agentic-setup-for-operational-work
author: null
published: '2026-06-05'
fetched: '2026-07-11T04:36:36Z'
classifier: codex
taxonomy_rev: 1
words: 805
content_sha256: 7b71851dbbbb0e7372495835872753ce21eed77332b0bf3e2f2af1a9f7825f13
---

# How we use agents to review production infrastructure

# How we use agents to review production infrastructure

How repo-owned agent workflows help us review incidents, infra cost, security findings, and bugs in production.

![Picture Max Deichmann](https://langfuse.com/_next/image?url=%2Fimages%2Fpeople%2Fmaxdeichmann.jpg&w=96&q=75) Max Deichmann

Max DeichmannWe use agents to turn production data into recurring artifacts for engineering review:

- A weekly production review surfaces important production signals to act on.
- Cloud cost analysis explains the main infrastructure spend drivers.
- Daily repository scans turn security findings into engineering priorities.

The impact is concrete: every week we now find regressions or new error cases that an engineer looks into, instead of letting them slip by unnoticed across our tools and production environments.

With AI, we can generate these reviews without adding bureaucracy for the engineering team. Engineers stay focused on systems judgment instead of weekly evidence collection. They decide whether a cost driver is acceptable, whether a page was customer-impacting, whether a bug needs an owner, whether a monitor is noisy, and whether a DeepSec finding needs an owner.

The data already lived across our tools, like Datadog, Linear, incident.io, and Metabase, spread across four production environments. Nothing pulled the systems together, so reviewing it every week would mean going through each tool and environment by hand.

This post walks through our current setup and how we got there.

[The system combines queryable data, MCP, and repo-owned skills](https://langfuse.com#the-system-combines-queryable-data-mcp-and-repo-owned-skills)

We set up a system with three layers. First, we made the relevant data queryable. Second, we exposed these sources to the agent harness through MCP. Third, we developed and iterated on repo-owned skills, each of which defines a fixed output table for review.

The workflow lives in [ langfuse/langfuse](https://github.com/langfuse/langfuse/tree/main/.agents), not in one engineer's local prompt history.

Linear is the deduplication layer across workflows. Before the agent reports an item as new, it searches existing Linear issues and comments. This keeps recurring items from showing up as fresh work every week.

[How each workflow works](https://langfuse.com#how-each-workflow-works)

[Weekly production review](https://langfuse.com#weekly-production-review)

The [ weekly-production-review](https://github.com/langfuse/langfuse/tree/main/.agents/skills/weekly-production-review) skill produces a report from Linear bug tickets, Datadog error signals, and public status-page incidents.

The agent returns signals it finds in our production environments. This gives us one weekly pass over the signals that may need action: bugs to prioritize, incidents to discuss, and Datadog errors that should become follow-up issues.

We iterated heavily on this skill. The agent needs to query each source with the right filters, deduplicate issues across tools, keep regions distinct, and preserve links already attached to Linear tickets.

[Cloud cost analysis depends on warehouse data](https://langfuse.com#cloud-cost-analysis-depends-on-warehouse-data)

Agents need data access before they need better prompts. For cost analysis, we export AWS Cost and Usage Reports into BigQuery, enrich them with business data using dbt, expose the resulting marts through Metabase, and make the relevant tables accessible through MCP.

The [ analyze-cloud-costs](https://github.com/langfuse/langfuse/tree/main/.agents/skills/analyze-cloud-costs) skill does not ask the model to "think about spend." It points the agent at cost marts and asks for the same grain every time: recent complete days versus a baseline, provider/service breakdowns, and cost per 100k ingested billable events.

The agent runs the broad pass: it queries source tables, identifies drivers, preserves caveats such as incomplete current-day rows in the AWS Cost and Usage Reports, and returns the same breakdown every time.

[Security skill turns daily scans into a triage table](https://langfuse.com#security-skill-turns-daily-scans-into-a-triage-table)

The `security-review` skill runs DeepSec daily on selected repositories. It scans the repositories and exports a compact findings table for review.

Before assigning work, the agent checks Linear for existing issues so the same vulnerability does not get reported every day. After reviewing the table, we ask the agent to create Linear tickets for the relevant findings. Linear Intelligence assigns those tickets to the right engineer.

[Skills need review and iteration](https://langfuse.com#skills-need-review-and-iteration)

Skills are not done when the first version works. They need review and iteration until engineers can trust them in a recurring workflow.

We review skill output like product behavior: whether the agent found enough evidence, kept formatting stable, and stopped at the right point. Each miss becomes a skill change.

*For example, we initially missed many error cases when searching Datadog for issues. We then updated the skill with the same instructions we would give a coworker: which data to query, how to filter it, and how to link the results. This improved output quality over time.*

[Next: ClickHouse query-log analysis by feature area](https://langfuse.com#next-clickhouse-query-log-analysis-by-feature-area)

The next step is to connect agents directly to ClickHouse query-log data through MCP. We already tag ClickHouse queries with dimensions such as project, API route, feature area, query name, and accessed tables. Today, dashboards use these tags to show live resource consumption for each ClickHouse cluster.

After that, we want agents to use the ClickHouse data to enrich the production review and cost reports. This should let us allocate ClickHouse cost to specific features or projects and find access patterns that caused API performance issues.
