---
title: Switch from Braintrust to Logfire without rewriting
kind: blog
topic: null
subtopic: null
secondary_topics: []
summary: null
triage: null
skip_reason: null
source: pydantic
url: https://pydantic.dev/articles/switching-from-braintrust
author: Bill Easton
published: '2026-08-05'
fetched: '2026-08-06T06:59:00Z'
classifier: null
taxonomy_rev: 2
words: 570
content_sha256: a62c06734dee31004b3094c25d92be12408f14f78e0675e08b147924b8c7c02c
---

# Switch from Braintrust to Logfire without rewriting

Your app is instrumented, your evals run in CI, and your experiments have a year of history. Nobody rewrites all of that because a comparison page told them to.

You do not have to. Fork the loop.

## 

Set the Braintrust app URL to [Logfire](https://pydantic.dev/logfire)'s compatibility endpoint and use your Logfire project write token as the API key:

```
export BRAINTRUST_APP_URL="https://logfire-us.pydantic.dev/v1/braintrust"
export BRAINTRUST_API_KEY="<your-logfire-write-token>"
```
Use `https://logfire-eu.pydantic.dev/v1/braintrust` for an EU project. If you previously set `BRAINTRUST_API_URL` or `BRAINTRUST_PROXY_URL`, unset them. Those overrides take precedence over the endpoint returned during login.

Existing Python and TypeScript `Eval` code that uses local data, tasks, and scorers can stay in place. Logfire accepts the SDK requests, folds the experiment updates, and emits the completed evaluation cases as OpenTelemetry data when the normal SDK summary finishes. Those two SDKs are verified for launch. Other Braintrust SDK languages are in early access while we expand conformance testing.

The change sends future runs to Logfire. It does not duplicate events to both products or import your Braintrust history. Switching back only requires restoring the previous app URL and key.

### 

| Braintrust workflow | Status in Logfire | 
|---|---|
| Python `braintrust` 0.30.1 and TypeScript`braintrust` 3.24.0`Eval` runs | Verified with normal score summarization | 
| Other Braintrust SDK languages | Early access while we expand conformance testing | 
| Inline or callable data, local tasks and scorers, multiple scores, metadata, tags, trials, and child spans within those verified flows | Supported | 
| Braintrust-hosted datasets, prompts, functions, remote parameters, attachments, BTQL, the model proxy, server-side scoring, and public sharing | Not provided by this endpoint | 

The compatibility endpoint is not an LLM proxy. Model-based scorers should use an explicit provider client rather than Braintrust's hosted proxy defaults.

Are you a heavy Braintrust user who depends on hosted datasets, prompts, functions, remote parameters, or another managed workflow? [Contact us](https://pydantic.dev/contact). We are looking for design partners to shape what Logfire supports next.

## 

For compatible eval runs, the events become part of the same telemetry model as the rest of your application:

- Scores sit on the timeline with model calls, retrieval, tools, and the request that started the trace. Logfire charges no separate score fee.
- Every score is queryable with PostgreSQL-compatible SQL and available to your coding agent over MCP.
- The surrounding browser, service, database, logs, metrics, and infrastructure can live in the same observability system.

## 

After the SDK summary completes, its result link opens the experiment in Logfire's Evals workspace. From there:

- **Human review (beta).** Logfire annotation queues capture verdicts, expected outputs, comments, and tags on production runs.
- **Experiment review.** Inspect evaluator results case by case, compare a run with its baseline, and follow the trace behind a result.
- **CI eval gates.** Pydantic Evals uses the same evaluator model online and offline, so production findings can become version-controlled regression cases.

Start with a staging or canary deployment. Compare the traces, queries, and score economics on your own traffic. The decision is reversible, and the instrumentation work is already done.

We are also improving Pydantic Evals, with simpler authoring and tighter Logfire workflows in mind. Whether your suite uses the Braintrust SDK today or Pydantic Evals, you can review its results alongside the telemetry that explains them.

[Start on the free tier](https://logfire.pydantic.dev/), change the destination and key, and watch your next Braintrust eval run land in Logfire.

No rewrite. Two environment variables.
