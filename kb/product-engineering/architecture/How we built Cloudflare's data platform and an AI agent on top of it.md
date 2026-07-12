---
title: How we built Cloudflare's data platform and an AI agent on top of it
topic: product-engineering
subtopic: architecture
secondary_topics:
- agents/tool-use
summary: How Cloudflare built Town Lake, a single-SQL-interface data platform on R2/Workers/Workflows
  unifying Postgres, ClickHouse, Kafka, and BigQuery sprawl (1B+ events/sec), and
  Skipper, an AI agent on top that answers plain-English questions with auditable
  queries and PII-aware governance.
source: cloudflare-ai
url: https://blog.cloudflare.com/our-unified-data-platform/
author: Brian Brunner
published: '2026-05-28'
fetched: '2026-07-11T04:13:04Z'
classifier: claude
taxonomy_rev: 1
words: 3206
content_sha256: 81b86b2658e5b5095cfe864904d571f9b8c0cb3d166b9f1dafbd4ddc70a8bace
---

# How we built Cloudflare's data platform and an AI agent on top of it

Cloudflare processes more than a billion events every second. Our network spans 330+ cities in 120+ countries. Behind every HTTP request, every Worker invocation, every R2 read operation, there is data, and a lot of it.

For years, that data was not very easy to access. It lived in dozens of production databases, ClickHouse clusters, Kafka streams, Google Cloud buckets, BigQuery datasets, and a long tail of pipelines. To answer a simple question like "How many domains that signed up today are in the Top 100 by traffic?", an analyst at Cloudflare had to know which system to ask, what credentials to use, what query language to write, and whether the data they were looking at was sampled, fresh, or seven-days stale. As a result, it was difficult to glean informed insights from the data.

To solve this problem, we built two in-house tools: Town Lake, Cloudflare's unified data analytics platform, and Skipper, an AI data agent that runs on top of it. Town Lake is a single SQL interface to everything Cloudflare knows, and Skipper is how anyone at Cloudflare can ask questions in plain English and get correct, auditable answers back in seconds.

This is the story of how we built both.

If you have ever worked at a company that went through a hyper-growth period, you know what data sprawl looks like. Ours had a few specific symptoms:

- **Too many disparate systems.**A product engineer who wanted to investigate a customer issue might need to query Postgres for account metadata, ClickHouse for analytics events, BigQuery for usage rollups, R2 for raw logs, and Kafka topics for real-time signals. Each system had its own credentials, its own language, and its own retention policy.
- **Sampled data.**This is fine for dashboards, but doesn’t work for domains like billing. Our- __analytics pipeline__
- **External dependencies for internal data.**Parts of our previous internal reporting stack were powered by external vendors. Beyond the cost, we had a hard external dependency on another cloud for some of our critical data.
- **No one could find the data.**Even if you had all the right credentials, you needed to know that the right table for "Billable Workers requests by account" lived in a specific ClickHouse cluster, in a specific schema, joined to a specific Postgres dimension table, and that the join required an obscure customer ID translation. There was too much tribal knowledge.

We had a cultural challenge too: data infrastructure had historically been treated as a back-office function that was in service of the business, rather than critical infrastructure in its own right.

We wanted to create one place where anyone at the company with appropriate permissions and a need to know could get answers to questions about Cloudflare: “Show me the top 100 customers by revenue in the last quarter”, “List all Bot Management ML scoring events with score > 0.9 in the last 48 hours coming from a specific ASN”, “Find the Top 100 billing support tickets from customers who have spent >$100”, etc.

We wanted that place to give fresh, accurate, unsampled data for the queries that need it (like billing or security investigations) and fast, downsampled data for the queries that don't (like dashboards or exploration).

We wanted security and governance baked in, with personally identifiable information (PII) detected automatically, and sensitive tables locked down by default. All access should be auditable, and have time-bounded permission grants so that users could only access data when they were actively working on tasks that required it.

We wanted it to be built on Cloudflare’s own platform: [ R2](https://www.cloudflare.com/products/r2/) for storage,

[for compute,](https://www.cloudflare.com/products/workers/)

__Workers__[for authentication,](https://www.cloudflare.com/products/access/)

__Cloudflare Access__[for orchestration. If we were going to make a major investment in our data infrastructure, it was going to be built on the same products we sell to customers.](https://www.cloudflare.com/products/workflows/)

__Workflows__And we wanted, eventually, an interface that did not require knowing any SQL. The goal was to empower anyone at the company with appropriate permissions and a need to know to look at the stream of data flowing through our network, not just analysts.

That last requirement is what became Skipper.

At its core, our data platform’s architecture is a [ data lakehouse](https://en.wikipedia.org/wiki/Data_lakehouse): a query engine that reads from object storage, with a metadata layer that makes the storage behave like a database. We call it Town Lake, after its namesake in Austin, Texas.

Its most important components are:

**Query engine.** We chose Apache Trino for that: a single SQL query can join a Postgres table, a ClickHouse table, and an Iceberg table on R2 without a need to materialize the intermediate results into a different system. A query that asks "what are the top 100 paying customers by Workers requests this week" compiles into a plan that pushes filters into ClickHouse, joins against an account dimension in Postgres, and ranks against billing rollups in R2, all in one go.

**R2 Data Catalog,** our managed Apache Iceberg service, is where the cold and warm data lives. Iceberg gives us schema evolution, time travel, partition evolution, and the ability to compact data as it ages. Per-minute usage from last week becomes hourly, hourly from last quarter becomes daily, etc. The storage cost decreases as recency does, while the data stays queryable. Parquet files in R2 are much cheaper compared to keeping the same data in an OLAP database.

**DataHub** is our metadata catalog. Every table, column, owner, lineage edge, and glossary term lives there. When a user asks "what's in `townlake.dim.accounts`," DataHub provides an answer, including the table description, the column descriptions, the owning team, the upstream tables that feed it, and the downstream tables that consume it.

**Lifeguard** is our access control service: it stores access rules in D1, dynamically pulls user and group membership from our internal access management system, and renders a combined JSON policy that Trino reads over HTTP. Lifeguard also feeds basic access information to Skipper and the Gateway, so users get blocked at the front door rather than at query time.

**Skimmer** is a PII detection scanner. It runs continuously, samples rows from every column in every table, and uses Workers AI to classify whether each column contains PII. It does this in two passes: first, a fast per-column classifier; then, if anything is flagged, an agentic second pass that gets full table context and can query Trino directly to verify. Findings flow into DataHub and into Lifeguard's allowlist to allow human-in-the-loop review.

**Transformer** is our ELT (extract, load, transform) engine built on Workflows. Users define a Directed Acyclic Graph (DAG) of SQL transformations with YAML frontmatter (target table, materialization mode, dependencies, schedule). Transformer compiles the graph and runs it on Trino, with state managed by Durable Objects, definitions stored in R2, and run history in D1.

**Ingestion** is the bridge from operational systems into the lake. An orchestrator runs as a long-lived Kubernetes deployment, reads pipeline configs, and spawns short-lived worker jobs to extract from Postgres or ClickHouse, transform to Parquet, and load into R2 as Iceberg tables. Each pipeline runs as either full-replace or incremental-append.

A real concern when you build a unified data platform is that you have just built a large sensitive-data surface. The traditional answer to this is: open by default, restrict by exception. Allow access to everything, then audit and lock down sensitive tables when someone notices.

Town Lake takes the opposite approach. Tables are inaccessible for querying until they have been reviewed. When a new database is connected to Trino or a new table is created, Skimmer scans it, classifies its columns, and registers it in the central allowlist as pending. Until a reviewer approves the table, and the specific columns within it, users can't query it. This sounds painful, and it would be, except for two things.

First, it's automated. Skimmer's classifier is reasonably good: it catches obvious PII (emails, IPs, names, phone numbers) and the long tail of non-obvious sensitive data (API tokens that match certain prefixes, opaque IDs that can be traced back to users). Reviewers see what was detected and either approve, override, or deny. Most reviews take seconds.

Second, the workflow is self-serve. If you query a table you don't have access to, the error message is not "permission denied." It's "this table needs review, click here to request one." Skipper, the AI agent, will even suggest the right [ RBAC](https://www.cloudflare.com/learning/access-management/role-based-access-control-rbac/) group to request and link you straight to it.

We separate schema discovery from data access. Users can see what tables exist, but unreviewed columns are hidden from `DESCRIBE` and `SHOW COLUMNS` and from `SELECT *`. That subtle distinction matters: it means a new unreviewed column doesn't break existing dashboards built on the rest of an approved table.

PII is opt-in per session. By default, Trino redacts sensitive columns before they ever hit your screen. If you have a legitimate need for raw PII (e.g., fraud investigation), you flip the bit on the session, your permissions are checked, and the redaction is lifted. The flip and every query is logged.

A query engine alone isn’t enough these days. SQL is still a barrier, as is knowing which of tens of thousands of tables to query — you need to know the canonical schema.

Skipper is our take on a conversational AI agent that goes from natural-language question to validated answer, grounded in the company's actual data, code, and institutional knowledge. We built it on top of Town Lake and on top of our developer platform: Workers, Workers AI, Durable Objects, D1, R2, Workflows, KV.

The interface is a chat box. Ask a question:


Show me the top 10 customers by R2 storage cost in the last 30 days, and the change versus the previous 30 days.

Skipper finds the right tables (DataHub search), pulls their schemas and lineage, writes the SQL, submits it to Trino, polls for results, and shows you a table or a chart. Follow up:


Now break it down by region, and ignore internal Cloudflare accounts.

It carries the context, refines the query, and reruns it. If something looks wrong, e.g., a join produced zero rows or a filter excluded what you expected, then Skipper investigates, adjusts, and tries again, in the closed-loop reasoning. The hard part was having the right context.

Skipper can also package charts into dashboards that can be shared internally and embedded into other internal applications. It also has tools for building transformation graphs via Transformer and for checking access and permissions via Lifeguard.

Skipper meets its users wherever they are. All of these tools are available via a Worker backed by a built-in agentic harness powered by Workers AI. On the flip side, many of our internal users work via local agentic flows, and Skipper’s tools are additionally available via an MCP server.

An LLM, given a SQL prompt and a list of table names, can hallucinate joins, misuse columns, and confidently produce a number that is completely wrong. We learned this the hard way during early experiments. The fix is multiple layers of grounded context that the model can pull from at retrieval time.

Layer 1: Schema and usage metadata. DataHub knows every column, every type, every primary key, every foreign key for every table. It also knows which tables are commonly joined together based on historical query patterns. Skipper's `search_datasets` and `get_entity_details` tools surface this directly.

Layer 2: Human annotations. When the team that owns `dim.accounts` writes a description like *"Account-level entity. One row per account_id. Every account belongs to exactly one customer (via customer_id FK),"* that description lives in DataHub and ends up in Skipper's context. Tags like `curated` mark validated tables that Skipper should prefer over scratch space.

Layer 3: Code-derived knowledge. Some of the most valuable context is not in any catalog: it's in the SQL that produces the table. The Transformer pipeline emits per-node `.meta.json` documentation to DataHub on every successful run. So when Skipper looks at `fct.billings_allocated`, it doesn't just see the schema; it sees that this is a pre-joined fact table built from `dim.accounts`, `dim.customers`, and `seed.product_classification`, with its `alloc_amount` column computed as `billed_amount / 12 for annual; billed_amount for monthly`. That's the kind of nuance that separates a correct answer from a confidently wrong one.

Layer 4: Curated data models. We maintain a small set of "data model" pages: short, human-written documents that describe how to think about billing, customers, accounts, and zones. *"Prefer tables tagged 'curated'. Avoid **scratch_r2** and tables tagged 'internal'. Search with data model terms (e.g., 'billing product revenue') not natural language."* These are surfaced as MCP resources that the agent can pull when the question matches.

Layer 5: Runtime introspection. When everything else fails, Skipper can issue live queries to Trino: `DESCRIBE table, SELECT DISTINCT col LIMIT 20, SELECT COUNT(*)`. It uses these sparingly as runtime context is expensive, but it's the safety net that makes the rest of the system robust.

One specific implementation detail is worth pulling out, because it is uniquely a Cloudflare-shaped solution.

When you build an AI agent with tools, the standard pattern is to define the tools in your prompt, let the model call them one at a time, parse the response, execute, and return results. This is fine, but it is chatty: a five-tool workflow is five model round-trips, each of which has to re-establish context.

For our MCP server, we use [ Code Mode](https://blog.cloudflare.com/code-mode/). Instead of defining 30 individual tools, we expose two:

`search` and `execute`. The model writes a JavaScript snippet that calls our entire toolset programmatically:```
const datasets = await skipper.search_datasets({ query: "billing product revenue" })
const queryId = await skipper.start_query({ sql: "SELECT ..." })
const results = await skipper.fetch_results({ queryId, mode: "inject" })
return skipper.create_chart({ chartType: "bar", data: results.rows, ... })
```
That JavaScript runs in a sandboxed Dynamic Worker isolate via [ WorkerLoader](https://developers.cloudflare.com/workers/runtime-apis/bindings/worker-loader/). The model gets to express complex multi-step workflows in a single round-trip, in a language it already knows extremely well. It's faster, it's cheaper, and the workflows it produces are auditable as code.

Everything Skipper does runs as the calling user. If you don't have access to a table, Skipper can't query it for you. If you ask for PII, your permissions are checked. If a query you save is shared with a teammate, their access is checked at view time, not at save time, because group membership changes.

Shared dashboards have their own twist. They can be embedded in any internal Cloudflare tool with a single placeholder div and a script tag:

```
<div data-skipper-dashboard="dash-123"></div>
<script src="https://skipper.cloudflare.com/embed.js" async></script>
```
The iframe auto-resizes to fit content. Content Security Policy (CSP) `frame-ancestors` blocks embedding from anywhere outside the corporate domain. Cloudflare Access still gates the iframe contents, so an unauthenticated viewer hits the Access login page in the iframe rather than seeing the data. Non-owner viewers are checked against the underlying tables: if they don't have access, they get pointed at the right group to request.

**Billing.** This was the original use case. Our Billable Usage Dashboard, the customer-facing dashboard that shows pay-as-you-go users exactly what they owe, is powered by a metering pipeline whose source of truth is a set of Iceberg tables in R2, queried via Trino. The dashboard's API pulls the same compact `(date, account_id, metric_name, usage)` rows that the invoicing system uses, so the number on the dashboard matches the number on the bill.

Billing-related queries account for 53% of all queries Town Lake serves: 91,760 queries from 324 distinct Cloudflare employees in a recent measurement period. The 200–300 line legacy SQL queries that used to compute revenue rollups by customer are now five lines.

**Business intelligence.** The "top 100 customers by revenue" question takes about three seconds in Skipper now. So does "how many domains that signed up today are in the top 100." So do most of the data-related questions we used to file Jira tickets for.

**Security analytics.** Our Bot Management team uses Town Lake to query ML scoring events with score > 0.9 in the last 48 hours filtered by ASN and geography. Threat researchers have built their own query toolkit on top of it. Trust & Safety pulls signals to help police abuse.

**Customer support.** "Find the top 100 billing support tickets from customers who have spent >$100" used to be a multi-day project. Now it's a Skipper query.

A few things have surprised us.

Less prompting is more. Early versions of Skipper had elaborate, prescriptive system prompts: *"First, use search_datasets. Then, use get_entity_details. Then, use list_schema_fields if needed..."* Quality went down. The model is good at reasoning about analytical workflows; it doesn't need to be micromanaged. We replaced the prescriptive prompts with high-level guidance and let the model pick its own path. Results got better.

Tool overlap is poison. We initially exposed every variant of every tool: three different "fetch results" tools, two "search" tools, several "list" tools. The model got confused and called the wrong one. We consolidated. Now `fetch_results` has a `mode` parameter `(inject / display / both)` instead of three separate tools. Every tool has a single reason to exist.

Code, not metadata, captures meaning. The biggest accuracy wins came when we started ingesting the actual SQL that produces a table, not just its schema. A `customer_type` column with values `contract`, `paygo`, `free` looks identical in either context, but the SQL tells you that `customer_type` defaults to `paygo` when Salesforce data is missing. That kind of context never lives in column descriptions.

Memory matters more than we expected. There is a long tail of corrections that look like "you have to filter for X like this" or "ignore tables tagged Y." Without a memory layer, the agent rediscovers and re-learns these every conversation. With one, it gets monotonically better at the recurring questions a team actually asks.

The boring infrastructure is the hard part. Trino + Iceberg is not new technology. The hard work is in the boring stuff: per-row access control, default-closed table allowlisting, query auditing, time-bound credentials, PII detection, idempotent ingestion, schema evolution. Those are the things that make a data platform safe to actually use.

We're expanding the agent surface. Skipper already integrates as an MCP server into any IDE that supports it. The next step is deeper integration with our own internal chat and ticketing systems, so that "ask the data" becomes the natural first move for anyone debugging an incident, scoping a project, or sanity-checking a hypothesis.

We're investing heavily in the Transformer pipeline. The goal is for any team at Cloudflare to be able to build a curated dataset with a few SQL files and a `.meta.json` description, deploy it as a Workflow, get it scheduled and monitored automatically, and have it surface in DataHub and Skipper without any additional work. The idea is self-serve data engineering, with the same shape as self-serve software engineering.

[ R2 SQL](https://developers.cloudflare.com/r2-sql/), Cloudflare's serverless, distributed, analytics query engine, is getting more and more robust by the day. As its feature set expands, we plan to move many parts of Town Lake’s workflow over to it.

The bet we made — that the next breakthrough product comes from someone looking at the data and seeing something nobody else sees — is one we're still betting on. Town Lake is how we make sure they can find it.
