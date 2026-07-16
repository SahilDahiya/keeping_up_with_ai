---
title: Full-Stack Agent Observability with AgentSH + Pydantic Logfire | Pydantic
kind: blog
topic: product-engineering
subtopic: security
secondary_topics:
- evals-observability/tracing
summary: Pairs LLM-level tracing (model calls, tool invocations) with AgentSH's OS-boundary
  auditing of what an agent actually did on the machine (file access, network connections,
  process execution) plus policy enforcement, both emitted as OpenTelemetry into one
  timeline to catch failures in the 'seams'.
triage: null
skip_reason: null
source: pydantic
url: https://pydantic.dev/articles/logfire-and-agentsh
author: Eran Sandler
published: '2026-03-25'
fetched: '2026-07-16T22:04:06Z'
classifier: claude
taxonomy_rev: 2
words: 1188
content_sha256: 5986418f146b7474881daf998d80894e6bc9ae609bf16a76b5861b44dcceeef2
---

# Full-Stack Agent Observability with AgentSH + Pydantic Logfire | Pydantic

*This is a guest post by  Canyon Road (AgentSH).*

**TL;DR:**

- Pydantic Logfire traces what your agent thought (model calls, tool invocations, latency).
- AgentSH audits what it actually did on the machine (file access, network connections, process execution).
- Both speak OpenTelemetry, so they land in one timeline. You get end-to-end visibility from prompt to process, with policy enforcement at the OS boundary.

The hardest agent failures are not in the LLM call. They are in the seams. The subprocess that ran `uv add`. The script that touched a credential file. The unexpected outbound connection hiding inside a dependency. The cleanup step that became `rm` on the wrong directory.

[Pydantic Logfire](https://pydantic.dev/logfire) exists for exactly this reality: unified observability across AI and the rest of your application stack, built on OpenTelemetry, so you can see a single timeline instead of jumping between tools.

But there is one blind spot almost every team hits with agents. You can trace what the agent thought and which tools it called, but you still cannot reliably answer: what did it actually do on the machine?

That is what [AgentSH](https://www.agentsh.org/docs) is for.

AgentSH sits under the agent at the execution boundary. It records file, network, and process activity, applies policy decisions, and exports those audit events as OpenTelemetry `LogRecord`s via OTLP.

Put them together and you get something rare in agentic systems: one end-to-end story, from prompt to process.


Let's talk about the mode everyone uses and nobody wants to admit they use.

Claude Code has a bypass mode that skips permission checks. The [docs are blunt](https://code.claude.com/docs/en/permissions): it disables permission checks and should only be used in isolated environments like containers or VMs.

That warning is correct. YOLO mode is never safe.

But teams still turn it on for a reason: prompt-by-prompt supervision does not scale when agents iterate at machine speed. So the real question is not whether anyone should ever use it. It is this: if you need that velocity, can you make the trade survivable?

This is where AgentSH + Logfire is a useful combination.

Logfire gives you the story of the session: traces, model calls, tool calls. AgentSH gives you the runtime truth: what happened at the OS boundary, what was blocked, what was allowed, and what it tried to do anyway.

You keep the speed. You stop flying blind.


Think of it as two streams that land in one place.

**Stream 1: what the agent did in the harness.** Pydantic maintains a [Logfire plugin for Claude Code](https://github.com/pydantic/claude-code-logfire-plugin) that turns each session into a trace with child spans per LLM API call, including token usage, cost tracking, and conversation history.

**Stream 2: what the agent did on the machine.** AgentSH records execution events (files, network, process operations) and exports them as OpenTelemetry `LogRecord`s via OTLP, asynchronously and without blocking if export fails.

Both streams can land in Logfire because Logfire supports standard OTLP ingest over HTTP, configured via `OTEL_EXPORTER_OTLP_ENDPOINT` and `OTEL_EXPORTER_OTLP_HEADERS`. See the [Logfire OTLP ingest guide](https://pydantic.dev/docs/logfire/guides/alternative-clients/).

At that point, Logfire becomes the place you answer questions like:

- Why did this agent run so long?
- What changed in the workspace?
- What did it try to execute?
- Did it attempt outbound network?
- Which policies denied it, and how often?
- Which sessions are doing risky things?


When people say "end-to-end visibility," they often mean "two dashboards." The goal here is tighter: one investigation thread.

AgentSH supports [trace correlation](https://www.agentsh.org/docs/#otel-export). If an event carries `trace_id` and `span_id`, those IDs attach to the exported log record so it lines up with distributed traces. You can align the runtime audit trail with the same trace as your agent session. If you have ever tried to debug an agent incident from partial logs and terminal output, you know how significant that is.


Most teams do not want every tool pushing directly to every backend. They want one place to add environment metadata, filter or scrub sensitive attributes, route to multiple destinations, and standardise authentication.

That is exactly what the [OpenTelemetry Collector](https://pydantic.dev/docs/logfire/instrument/opentelemetry-collector/otel-collector-overview/) is for. Logfire documents using it for data transformation, enrichment, and collecting existing system logs. AgentSH is designed for the same reality: export audit events via OTLP to any OTel-compatible collector.

The clean architecture is:

```
AgentSH → OpenTelemetry Collector → Logfire
```
And optionally, other sinks too.


**Denied becomes a real signal, not a vibe.** AgentSH maps policy decisions to severity. So you can alert on spikes in denied outbound connections, attempts to read disallowed paths, and risky command patterns appearing in nested scripts.

**You can finally answer: what did it do?** With AgentSH events in Logfire, the same place you inspect tool calls is the place you inspect file reads and writes, exec activity and subprocess behaviour, and network attempts, whether allowed or blocked.

**YOLO becomes less dangerous, not safe.** Claude Code's guidance is to only use bypass mode in isolated environments. AgentSH does not erase that warning. It makes it practical to follow it: run in a contained environment, enforce runtime policy at the boundary, ship the full audit stream to Logfire for visibility and incident response. That combination is the difference between "we hope nothing bad happens" and "we can prove what happened."


The best way to understand the correlation is to see it. We built a [working demo](https://github.com/canyonroad/pydantic-demo) that puts all of this together in a single container.

A Pydantic AI agent is given two tools, `list_files` and `cat_file`, and asked to read every file in its working directory. One of those files is `.env`. AgentSH blocks the read at the FUSE filesystem level before the data ever reaches the agent. The agent gets `EACCES`, moves on, and the whole thing shows up in Logfire as a single correlated trace:

```
agent-run
  agent run
    chat claude-sonnet-4-6
    running tool: list_files
      list_files .
        dir_list: /workspace [allow]          ← agentsh FUSE event
    chat claude-sonnet-4-6
    running tool: cat_file
      cat_file .env
        file_open: /workspace/.env [deny]     ← blocked, level=ERROR
    chat claude-sonnet-4-6
    running tool: cat_file
      cat_file sample.txt
        file_open: /workspace/sample.txt [allow]
        file_read: /workspace/sample.txt [allow]
```
The blocked `.env` access appears as `ERROR` under the exact `cat_file` span that triggered it. Not in a separate dashboard. Not in a separate log stream. Right there in the trace.

Trace correlation works like this: the Python agent creates a Logfire span for each tool call, pushes the current `trace_id` and `span_id` to the AgentSH session before executing the tool, and AgentSH attaches that context to every FUSE event it emits. Both streams arrive in Logfire under the same trace.

To run it yourself you need Docker with FUSE support, an Anthropic API key, and optionally a Logfire token (without one, traces print to console):

```
docker build -t pydantic-demo .
docker run --rm \
  --cap-add SYS_ADMIN \
  --device /dev/fuse \
  --security-opt apparmor=unconfined \
  --env-file .env \
  pydantic-demo
```
The `--cap-add SYS_ADMIN` and `--device /dev/fuse` flags are required for AgentSH's FUSE interception to work inside the container.


Logfire gives you the trace of your AI system. AgentSH gives you the audit trail. OpenTelemetry makes it one story.

If you are going to run agents at speed, you owe yourself runtime truth. Visibility that is queryable, alertable, and explainable.
