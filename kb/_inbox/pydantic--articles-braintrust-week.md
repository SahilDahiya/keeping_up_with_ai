---
title: 'Score freely: Logfire vs Braintrust evaluation pricing'
kind: blog
topic: null
subtopic: null
secondary_topics: []
summary: null
triage: null
skip_reason: null
source: pydantic
url: https://pydantic.dev/articles/braintrust-week
author: Bill Easton
published: '2026-08-03'
fetched: '2026-08-04T06:56:37Z'
classifier: null
taxonomy_rev: 2
words: 575
content_sha256: f55cc6f7ab81e7cf2a82d0022a9c6bc015b13f44d978bc3b2a60965ac2e48ab0
---

# Score freely: Logfire vs Braintrust evaluation pricing

You turned production scoring down to ten percent. Not because ten percent was enough, but because scoring every run added another platform charge and someone had to sign the invoice. So you picked a number that felt responsible, wired your evaluators to one run in ten, and shipped. The failure your users hit the next week was in the other nine.

That is the cost of a meter on scoring: you stop measuring what you built the eval to catch.

## 

Observe, evaluate, improve. That loop is the whole pitch of AI observability. Braintrust can turn production failures into datasets and scorers, but its Pro plan charges $1.50 per thousand scores after the first fifty thousand. The Starter overage is $2.50 per thousand. Those rates look small until coverage is real, and then they teach you to score the traffic you can afford instead of the traffic that matters.

An LLM judge still consumes model tokens wherever it runs. That cost is unavoidable. Cheap code-based checks and heuristics do not have that model bill, though, and neither kind of evaluator needs a second platform fee for recording its result.

## 

[Logfire](https://pydantic.dev/logfire) charges $0 per thousand scores. Each `gen_ai.evaluation.result` is an OpenTelemetry event attached to its originating trace, and telemetry is billed with the same observation rate as everything else: $2 per million after the first ten million observations each month.

At fifty million scores, Braintrust Pro's platform and score charges are $75,174. Exact price parity with the $100 full-rate telemetry cost of fifty million Logfire observations is impossible because Braintrust Pro's $249 platform fee is already higher. Waive that platform fee and allow another $100 for score overages anyway. That budget buys 66,667 overage scores, plus the 50,000 included. Out of fifty million runs, you could score 116,667 and would have to skip **99.77%**.

That comparison is deliberately conservative for Logfire. It treats every score event as a full-rate observation, ignores Logfire's ten-million-observation free allowance, and still leaves Logfire without a separate score charge. Provider and model costs for LLM judges are excluded on both sides.

Coverage can go back to being a quality decision. Cheap heuristics can fire on every run. LLM judges can sample the traffic that earns their model cost. The observability platform does not add another reason to look away.

## 

The score is only half of it. Braintrust can ingest application spans over OpenTelemetry, but its product is centered on AI tracing and evaluation. Logfire is a full observability suite: browser, service, database, model, tool, logs, metrics, and infrastructure, with evaluation results attached to the same trace.

When a score drops, the cause may be a stale retrieval result, a rate-limited upstream, or a slow database call. The whole system is already there to query. That is not a pricing difference. It is an architectural one.

## 

- **Tuesday: Switch the pipe.** Redirect the Braintrust SDK to Logfire without rewriting your instrumentation.
- **Wednesday: Economies of score.** See what three separate Braintrust meters do at production scale.
- **Thursday: Close the whole loop.** Move from a trace-backed failure to a reviewed change and controlled rollout.
- **Friday: SQL over the whole trace.** Use PostgreSQL-compatible SQL and MCP across all your telemetry.

## 

Braintrust is an evaluation platform with a per-score price. Logfire keeps evaluation inside the full production trace and charges no separate score fee.

[Open Logfire](https://logfire.pydantic.dev/), point it at your agents, and stop rationing what you measure.

Score freely.
