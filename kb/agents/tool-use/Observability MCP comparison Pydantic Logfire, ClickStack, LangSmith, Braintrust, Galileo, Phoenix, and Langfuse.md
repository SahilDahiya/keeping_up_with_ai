---
title: 'Observability MCP comparison: Pydantic Logfire, ClickStack, LangSmith, Braintrust,
  Galileo, Phoenix, and Langfuse'
kind: blog
topic: agents
subtopic: tool-use
secondary_topics:
- evals-observability/monitoring
summary: Compares the MCP servers of seven observability platforms (Logfire, ClickStack,
  LangSmith, Braintrust, Galileo, Phoenix, Langfuse) on whether an agent can ask a
  debugging question directly and get bounded, verifiable evidence, arguing MCP tool
  design should return compact aggregates rather than pages of raw trace objects that
  burn the context window.
triage: null
skip_reason: null
source: pydantic
url: https://pydantic.dev/articles/observability-tools-agents-want
author: Anthony Abercrombie
published: '2026-07-02'
fetched: '2026-07-16T22:02:51Z'
classifier: claude
taxonomy_rev: 2
words: 3040
content_sha256: ddd5abfed1af15a7ed366d2a23c2fc3128ee6fd34152b5a3b16714514a015904
---

# Observability MCP comparison: Pydantic Logfire, ClickStack, LangSmith, Braintrust, Galileo, Phoenix, and Langfuse

[YC's Lightcone Podcast](https://www.ycombinator.com/library/NK-the-ai-agent-economy-is-here) put the agent economy shift this way: "the question is no longer just whether you're making something people want. It's whether you're making something agents want."

Observability is no exception. In the last year [Pydantic Logfire](https://pydantic.dev/logfire) and other observability platforms have shipped MCP servers, CLIs, and SDKs so agents can inspect traces, logs, prompts, evals, and dashboards directly.

MCP standardizes how agents talk to systems. It does not standardize what an agent can ask, what data model sits behind the tools, or how much object reconstruction the agent has to do after each tool call. That matters because context windows are finite, and [LLM performance can degrade as the context fills](https://arxiv.org/abs/2601.15300). In observability, the difference between a compact aggregate query and pages of raw trace objects is not cosmetic. It is the difference between an agent spending its budget on reasoning and spending it on rebuilding the table it needed in the first place.

So the useful question isn't whether a platform ships an MCP. Nearly all of them do now. The better question:

Can an agent ask the debugging question directly, and return bounded evidence a human can verify?



Our recent post, [The best AI observability platform in 2026](https://pydantic.dev/articles/best-ai-observability-platform), covers the fundamentals of a great platform: AI-native tracing, integrated evals, full-stack depth, OpenTelemetry portability, queryable data, predictable pricing, and production scale. This post drills into one narrower criterion: whether those capabilities become an investigation surface for agents, not just another UI. For observability, that usually means three things:

- The agent can see the full production context, not just LLM and tool calls.
- The agent can ask new aggregate and correlation questions.
- The agent can return a reproducible artifact: a query, a trace link, a bounded result set.

The right MCP for eval management may be the wrong one for production incident debugging. A raw-analytics MCP may not fit observability unless its telemetry model is clear. A trace-inspection MCP may still leave the agent rebuilding aggregates client-side. And more tools does not mean more utility. We will return to these criteria as a concrete checklist after the results.



Some MCPs expose SQL or another query layer over the underlying data. That lets the agent ask new aggregate questions instead of being limited to prebuilt workflows. Our related post, [SELECT * FROM clickbait()](https://pydantic.dev/articles/select-star-from-clickbait), makes the builder-side case for SQL as a compact agent interface: one familiar, declarative tool can sit on top of application-specific views and functions. The benchmark result below shows the operational version of the same point: when an observability question can be answered as a query, the response can be a few rows instead of pages of objects.

Logfire applies that pattern to observability data. Its MCP exposes SQL over telemetry records, with DataFusion behind Logfire's SQL. ClickStack and Braintrust also expose query-backed surfaces. ClickStack's [Open House observability post](https://clickhouse.com/blog/observability-mcp-server-ai-notebooks) argues for observability-specific MCP tools over raw SQL alone, while keeping SQL as the escape hatch. Braintrust's [MCP docs](https://www.braintrust.dev/docs/integrations/developer-tools/mcp) describe object resolution, schema inference, and SQL over experiments, datasets, and project logs; its [CLI and MCP launch post](https://www.braintrust.dev/blog/cli-and-mcp) frames that surface for developer workflows.


Most other observability MCPs expose product objects directly. LangSmith's [MCP server](https://docs.langchain.com/langsmith/langsmith-mcp-server) exposes runs, traces, threads, datasets, and experiments, with SDK helpers for [trace export](https://docs.langchain.com/langsmith/export-traces) and [thread queries](https://docs.langchain.com/langsmith/query-threads). Langfuse's [MCP reference](https://mcp.reference.langfuse.com/) covers observations, metrics, prompts, scores, datasets, and the rest of the product surface, and its [MCP implementation post](https://langfuse.com/blog/2025-12-09-building-langfuse-mcp-server) explains the product-workflow emphasis. Arize Phoenix splits agent access across CLI, MCP, and skills for traces, evals, datasets, and prompts in its [coding-agent docs](https://arize.com/docs/phoenix/integrations/developer-tools/coding-agents). Galileo's [MCP docs](https://docs.galileo.ai/getting-started/mcp/setup-galileo-mcp) and [Agent Evals MCP launch post](https://galileo.ai/blog/bringing-agent-evals-into-your-ide-introducing-galileo-s-agent-evals-mcp) focus on datasets, experiments, prompt templates, log-stream signals, and integration guidance.

Those object surfaces can answer real debugging questions. The tradeoff is that the agent often has to paginate, fetch the right objects, filter client-side, and stitch aggregates together before it can answer the question.


To compare the shape of these MCPs, we built a synthetic support-bot benchmark with a Pydantic AI application. The application emits standard OpenTelemetry spans, so the data each platform ingested was ordinary OTel telemetry, not a Pydantic-specific format.

The benchmark generated 100 support requests: 20 cases in each of five scenarios, each case producing one root request span and three child spans (policy search, order lookup, generation), for 400 support-bot spans total. Each scenario plants a different root cause, with the evidence recorded as span attributes:

- `normal`: the baseline. The bot retrieves current policy, finds the order, and answers with healthy latency.
- `stale-policy`: the policy-search step retrieves an outdated policy document, flagged as- `stale_policy=true`on the span, and the bot answers from stale context.
- `tool-catalog-miss`: the order lookup succeeds, but a missing catalog alias breaks the compatibility check, recorded as a- `tool_warning`on the lookup span.
- `backend-latency`: the intentionally slow one. The backend order lookup carries a planted- `3200ms`latency signal, dragging the root request to- `3270ms`versus- `120ms`in the other scenarios.
- `model-overconfidence`: retrieval, tools, and backend are all healthy; the failure originates in model behavior, visible in the generation span's- `confidence`and- `resolution`attributes.

That gave the agent a compact but realistic investigation:

- Count requests by scenario.
- Identify the slowest scenario.
- Reconstruct the trace shape.
- Find the child operation responsible for the latency.
- Return evidence a human can verify.

We submitted the same benchmark shape to Logfire, ClickStack, LangSmith, Braintrust, Galileo, Arize Phoenix, and Langfuse, then tested the strongest available programmatic surface for each provider. Where possible, we used the MCP or CLI directly. Where an SDK or API was the reliable way to verify submitted data, we kept that evidence separate from the direct MCP result.

The benchmark does not measure production reliability, ingestion cost, alerting, UI quality, retention, or enterprise readiness. It measures one narrow thing: how much work the agent-facing surface required to answer the same debugging question.

**Method notes**

This was an illustrative single-run benchmark (`n=1` per tested path), not a statistically averaged product benchmark. Each provider got the same 100-case / 400-span support-bot shape, but the tested paths differed because the platforms expose different MCP, CLI, SDK, and API surfaces. No single autonomous model drove every path; most checks were run through deterministic scripts, MCP clients, SDK calls, direct API calls, or Codex-assisted MCP sessions. Treat the call counts as the investigation steps used to reach the reported result in this case study, not averaged traces from a single autonomous agent run.

Calls/pages count investigation work only. Auth, setup, docs lookup, and tool-listing are excluded. Pagination pages count because each page is another response the agent has to inspect.

The proxy numbers are not model billing tokens. We did not capture comparable prompt/completion token usage for an investigating agent across providers. Instead, we use a reconstruction-cost proxy: compact JSON character count divided by four. The **Result payload consumed** column reports that proxy for the payload each tested path actually used, marked `measured` when the value came from recorded tool output and `modeled` when it came from normalized benchmark objects.

The result should be read as a controlled case study of tool shape, not a model-independent leaderboard.


| Platform | Tested path | Debugging status | Calls/pages | Result payload consumed | What this showed | 
|---|---|---|---|---|---|
| Logfire | Hosted MCP `query_run`over telemetry records | Complete | 2 MCP calls | measured ~100 proxy tokens | SQL returned the root latency aggregate and the child-span latency proof. | 
| ClickStack MCP | ClickStack MCP: SQL, search, trace waterfall | Complete | 3 SQL calls; 5 with search/waterfall checks | measured ~200 SQL proxy tokens; ~3k with optional checks | Same benchmark answer, plus trace-waterfall verification, with slightly more tool choreography. | 
| Braintrust | MCP object resolution, schema inference, and SQL over experiments/project logs | Root/eval/log complete; trace depth partial | 3-5 MCP calls | measured ~85 result proxy tokens; schema text excluded | SQL compactly answered root scenario latency and project-log counts; full application trace depth was weaker in the tested path. | 
| LangSmith | Local MCP `fetch_runs` | Complete in principle; reconstruction-heavy | 9 root pages; ~109 calls estimated for all trace trees | modeled root-only proxy ~6k | Recovered all roots and sampled child run trees; full MCP-only analysis requires per-trace reconstruction. | 
| Langfuse | Project MCP metrics and observation listing | Complete; reconstructed | 3 MCP calls | measured ~150 summary proxy tokens; modeled lookup-observation proxy ~6k | Metrics helped, but scenario-level debugging required observation listing and client-side grouping. | 
| Arize Phoenix | MCP `get-spans` | Complete raw span access | 1-2 MCP calls | modeled full span-set proxy ~97k | Direct span access worked; the agent still had to aggregate raw spans client-side. | 
| Galileo | MCP Signals/Insights plus SDK readback | Not comparably scored | 2 MCP signal calls; SDK readback for raw traces | measured small empty signal response | Signal tools were callable, but no non-empty signal was available in this account; raw verification used SDK reconstruction. | 

The tool-count result is straightforward: usefulness did not track the number of exposed tools. Logfire exposed 20 tools, ClickStack exposed 19 observability-oriented tools, Langfuse exposed 52, and Galileo exposed 9. Logfire's advantage in this benchmark was not the largest inventory. It was that two query calls returned the exact aggregate and child-span evidence needed for the debugging task.

The two Logfire queries are short enough to show. First, identify the slow scenario:

```
SELECT
  attributes->>'scenario' AS scenario,
  COUNT(*) AS root_spans,
  AVG((attributes->>'support.latency_ms')::FLOAT) AS avg_latency_ms
FROM records
WHERE kind = 'span'
  AND service_name = 'mcp-comparison-support-bot'
  AND span_name = 'support-bot.request'
  AND attributes->>'benchmark_run_id' = 'mcp-comparison-run-003'
GROUP BY attributes->>'scenario'
ORDER BY avg_latency_ms DESC
LIMIT 10
```
Then, use the same trace model to find the child operation responsible:

```
WITH roots AS (
  SELECT
    trace_id,
    span_id,
    attributes->>'scenario' AS scenario
  FROM records
  WHERE kind = 'span'
    AND service_name = 'mcp-comparison-support-bot'
    AND span_name = 'support-bot.request'
    AND attributes->>'benchmark_run_id' = 'mcp-comparison-run-003'
)
SELECT
  roots.scenario,
  child.span_name,
  COUNT(*) AS spans,
  MAX((child.attributes->>'support.duration_ms')::FLOAT) AS max_duration_ms
FROM roots
JOIN records AS child
  ON child.trace_id = roots.trace_id
 AND child.parent_span_id = roots.span_id
WHERE child.kind = 'span'
  AND child.service_name = 'mcp-comparison-support-bot'
GROUP BY roots.scenario, child.span_name
ORDER BY max_duration_ms DESC
LIMIT 20
```
ClickStack reached the same answer in 3 SQL calls, or 5 calls when including search and trace-waterfall verification. That result reinforces the main pattern: query-backed observability MCPs gave the agent the shortest path to the answer. Braintrust's SQL path was also compact, but required object resolution and schema inference first. LangSmith, Langfuse, Phoenix, and Galileo exposed useful data, but the tested paths moved more work into pagination, SDK/API readback, local grouping, or raw-object reconstruction.

The next table is a modeled reconstruction-cost table, not another provider ranking. It explains why the first table matters. The benchmark had five scenarios, 20 cases per scenario, and four spans per case; the full normalized set is 387,800 characters, or about 96,950 proxy tokens (the same compact-JSON chars/4 proxy used above). A query-backed path can usually collapse a scenario into a few rows. An object path may need roots, the relevant child span type, or the full trace tree before it can prove the same thing.

| Scenario | Debugging question | Query path can return | Modeled object fetch minimum | Modeled tool-response burden | 
|---|---|---|---|---|
| `normal` | Is this the baseline with no hidden warning? | Aggregate roots, then optional absence checks over child spans | 20 roots; up to 80 spans to prove absence | ~4.9k root-only; ~18.0k full scenario | 
| `stale-policy` | Did stale policy context explain the issue? | Roots plus `support-bot.policy-search`rows where`stale_policy=true` | 20 roots + 20 policy-search spans | ~9.1k targeted; ~18.2k full scenario | 
| `tool-catalog-miss` | Did tool/catalog coverage fail? | Roots plus `support-bot.lookup-order`warning attributes | 20 roots + 20 lookup-order spans | ~9.3k targeted; ~18.6k full scenario | 
| `backend-latency` | Which child span explains the slow request? | Root latency aggregate plus child-span latency grouped by scenario | 20 roots + 20 lookup-order spans | ~9.2k targeted; ~18.4k full scenario | 
| `model-overconfidence` | Was the issue model behavior rather than policy, tool, or backend latency? | Roots plus generation/resolution evidence | 20 roots + 20 generation spans | ~10.0k targeted; ~18.4k full scenario | 

These estimates are not exact LLM spend. They show the reconstruction cost the agent can incur when the MCP returns objects and expects the client to build the aggregate locally. Against that full-object cost of about `97k` proxy tokens, the Logfire SQL result payloads were about `100` measured proxy tokens, and did not require reconstruction for this question.

That is the strongest Logfire argument this benchmark supports: SQL over telemetry records let the agent answer the slow-scenario question as two bounded queries instead of a client-side reconstruction job.

Nothing in those queries is Python-specific. They select over the OpenTelemetry span model — `service_name`, `span_name`, `trace_id`, `parent_span_id`, and span attributes. Because Logfire is OpenTelemetry-native, the same spans could come from a TypeScript agent, a Go service, or any other OTel source, and the MCP investigation would be identical.


ClickStack was closest to Logfire on this benchmark: 3 SQL calls for the core answer versus Logfire's 2, or 5 calls when including search and trace-waterfall verification. ClickHouse's [Open House observability post](https://clickhouse.com/blog/observability-mcp-server-ai-notebooks) says raw SQL remains valuable, but observability agents benefit from higher-level investigative tools when the workflow becomes multi-step. Our local ClickStack run confirmed that shape: after OTLP ingestion, ClickStack MCP recovered the full 100-trace / 400-span benchmark, returned the same scenario latency distribution, identified `support-bot.lookup-order` at `3200ms` in backend-latency, and exercised both `hyperdx_search` and `hyperdx_trace_waterfall`.

Braintrust's MCP is broader than a simple eval-only read. Its [MCP docs](https://www.braintrust.dev/docs/integrations/developer-tools/mcp) describe SQL querying over experiments, datasets, and logs, and our recheck confirmed the MCP exposes `sql_query` for `experiment`, `dataset`, and `project_logs` objects. In the benchmark, Braintrust SQL returned the root scenario latency distribution from the experiment object, and SQL over project logs returned 20 rows for each scenario.

LangSmith's [MCP server](https://docs.langchain.com/langsmith/langsmith-mcp-server) exposes `fetch_runs`, thread history, prompts, datasets, experiments, and billing; `fetch_runs` supports filters, FQL, `trace_filter`, `trace_id`, and `tree_filter`. Its SDK docs show how to [export traces](https://docs.langchain.com/langsmith/export-traces), query root and child runs, and [inspect threads](https://docs.langchain.com/langsmith/query-threads). In the benchmark, the local MCP recovered all 100 benchmark root runs with `fetch_runs` plus FQL metadata filtering. A follow-up MCP-only retest found that `fetch_runs` by `trace_id` can recover root and child run trees and reproduce the `support-bot.lookup-order` latency signal. The limitation was the call pattern: bulk filters returned 25 traces / 100 runs in this account, and a full 100-trace reconstruction was estimated at 109 `fetch_runs` calls.

Langfuse exposed a broad project-scoped MCP surface. Its metrics and observation tools recovered benchmark observations, and its [MCP reference](https://mcp.reference.langfuse.com/) includes prompts, observations, datasets, scores, comments, models, media, and more. Langfuse's own post on [building its MCP server](https://langfuse.com/blog/2025-12-09-building-langfuse-mcp-server) emphasizes product-workflow coverage and reuse of existing API logic. In the tested path, scenario-level grouping required listing observations and grouping metadata client-side.

Phoenix exposed a broad span/object MCP and recovered the full 100-root / 400-span benchmark shape through `get-spans`. Its [coding-agent docs](https://arize.com/docs/phoenix/integrations/developer-tools/coding-agents) recommend using CLI, MCP, and skills together: CLI for traces, experiments, datasets, and prompts; MCP for documentation lookup and direct Phoenix instance operations. The tested MCP path was not arbitrary SQL, so deeper aggregations relied on object retrieval and client-side analysis.

Galileo's MCP is best described as eval and signal-oriented, and its [MCP docs](https://docs.galileo.ai/getting-started/mcp/setup-galileo-mcp) and [Agent Evals MCP launch post](https://galileo.ai/blog/bringing-agent-evals-into-your-ide-introducing-galileo-s-agent-evals-mcp) frame it around bringing eval-powered insights into the IDE. We tested `get_logstream_signals` and `get_logstream_insights` against the benchmark log stream and several available sample streams. The tools were callable, but no non-empty generated signal was available in this account. That means Galileo should be marked as not comparably scored for signal quality in this benchmark. Separately, the SDK search path recovered the submitted trace and span data.


**Ask what the agent can see:**

- Does it have access to full application traces, or only LLM and tool calls?
- Are all attributes and metadata of interest queryable?
- Can it traverse from a root request to child operations and back?

**Ask what the agent can ask:**

- Can it run ad-hoc aggregate queries?
- Can it filter and group by attributes no prebuilt tool anticipated?
- Can it correlate model behavior with application performance metrics and data?
- Can common operations be reused and exposed as queryable views and functions?

**Ask what the agent can return:**

- Can it cite the queries it ran in its analysis?
- Can it return bounded results instead of dumping pages of JSON?
- Can it link a human back to the evidence, such as a full trace in a UI?


This investigation evaluated how much debugging work an agent-facing surface could do before forcing the agent into reconstruction. On that narrow test, the lowest-friction paths combined a clear telemetry model with a query layer the agent could use directly. Logfire answered the slow-scenario question in 2 MCP calls. ClickStack answered it in 3 SQL calls, or 5 calls with search and waterfall verification. Several other paths worked, but required pagination, object discovery, per-trace reconstruction, SDK/API readback, or client-side grouping before the agent could state the same conclusion.

That split is the practical lesson. MCP is a wire format. It does not guarantee investigative power, and neither does tool count. What matters is whether the agent can see enough production context, ask aggregate and correlation questions the tool designer did not anticipate, and return evidence a human can verify: a query, a bounded result set, a trace link.

If you are choosing or building agent-facing observability tooling, start with the checklist above: what can the agent see, what can it ask, what can it return. Eval workflows, prompt management, signal generation, and raw trace inspection are all legitimate centers of gravity. Production incident debugging is a different job, and it rewards platforms that expose observability data in a form agents can query rather than reconstruct.

The benchmark does not prove SQL always wins. A careless agent can still write a bad query or fetch too much data. It does show why SQL over telemetry records is such a strong MCP shape for observability: it lets the agent turn an operational question into a bounded, reproducible query before the context window fills with objects.
