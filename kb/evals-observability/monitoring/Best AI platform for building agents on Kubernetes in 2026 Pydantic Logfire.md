---
title: Best AI platform for building agents on Kubernetes in 2026 | Pydantic Logfire
kind: blog
topic: evals-observability
subtopic: monitoring
secondary_topics:
- infra-platform/deployment
summary: Surveys the observability landscape for AI agents running on Kubernetes,
  contrasting AI-native eval tools (Langfuse, LangSmith, Arize, Braintrust) that are
  blind to pod/node health with infra incumbents (Datadog, Grafana, New Relic, Elastic)
  whose LLM tracing is a bolted-on, separately-priced product; details Groundcover's
  eBPF zero-instrumentation approach versus Pydantic Logfire's OpenTelemetry Collector
  + k8sattributes processor for correlating OOMKills and CPU throttling with agent
  traces in one view.
triage: null
skip_reason: null
source: pydantic
url: https://pydantic.dev/articles/best-ai-platform-agents-kubernetes
author: Bill Easton
published: '2026-07-30'
fetched: '2026-08-07T06:29:24Z'
classifier: claude
taxonomy_rev: 2
words: 3088
content_sha256: 55e8fdbd850382bdb0d71119b69e5be4b2d46708ff92cb7d0bfbfae5f02680ad
---

# Best AI platform for building agents on Kubernetes in 2026 | Pydantic Logfire

Your agent starts returning truncated answers at 2am. Was the prompt wrong, did the model quietly degrade, or did the pod hit its memory limit and get OOMKilled mid-generation? On most stacks you cannot answer that from one screen, because the agent's trace lives in one tool and the cluster's health lives in another.

That gap is what this post is about. Not how to deploy agents on Kubernetes, and not the AIOps tools that use AI to watch your cluster. This is about the platform you reach for to observe and improve the agents you already run on a cluster: the one that has to see both the reasoning and the pod.

## 

An agent on Kubernetes fails in one of two directions, and most tools can only see one of them.

- **Blind to the cluster.** The AI-native eval and observability tools (Langfuse, LangSmith, Arize, Braintrust) trace the agent beautifully and run real evals, but the trace stops at the LLM boundary. A slow or failed run cannot tell you a pod was OOMKilled or a node was under memory pressure. These tools expect you to run a separate infrastructure tool beside them. Braintrust says so in its own documentation: use Datadog for infrastructure monitoring while Braintrust manages evaluation.
- **Sees the pod, thin on the agent.** The APM and infrastructure incumbents (Datadog, Grafana, New Relic, SigNoz, Elastic) know Kubernetes cold, and they have all bolted on LLM or agent observability. The catch is the seam: for most of them the AI layer is a separately priced product or a separately instrumented path, correlated next to the infrastructure rather than unified in one view. And the loop stops at observe-and-maybe-evaluate. None of them proposes a fix and ships it.

A couple of newer platforms escape the split: Groundcover, on eBPF, and SigNoz, on OpenTelemetry, do get the pod and the agent into one view. There the missing piece is not visibility but the engineering loop, the ability to turn what you see into a shipped fix.

The platform you want closes both gaps: one view from the agent's reasoning down to the pod that killed it, and an engineering loop that turns what you learn into a shipped change.

## 

- **One view, agent to pod.** When a run misbehaves you should see the model call, the tool call, the database query, and the container's memory and CPU on the same timeline, linked by the same Kubernetes attributes. Correlating two products by timestamp is not the same thing.
- **Real Kubernetes monitoring, not just LLM spans.** Pods, nodes, resource limits, container restarts, OOMKills, CPU throttling, and node pressure, captured natively, not left to a second vendor.
- **The AI-engineering loop.** Evaluation you do not ration, a trace-backed optimizer that proposes a change, and managed configuration that ships it without a redeploy. Observability tells you what broke; this is what fixes it.
- **Open standards.** OpenTelemetry-native by default, so agent and infrastructure telemetry share one format and your instrumentation is portable off the cluster and off the vendor.
- **Pricing that survives the cardinality.** Kubernetes telemetry is high-volume and LLM spans are large. The bill should be predictable, not a stack of per-host and per-span meters.

## 

### 

[Pydantic Logfire](https://pydantic.dev/logfire), from the team behind Pydantic and Pydantic AI, is the one platform that keeps the agent and the cluster in one OpenTelemetry-native view: the agent's trace and the cluster's metrics, correlated by shared Kubernetes attributes. A single OpenTelemetry Collector, deployed as a DaemonSet, scrapes kube-state-metrics and kubelet cAdvisor and enriches everything with the `k8sattributes` processor, so pod restarts, resource limits, OOMKills, CPU throttling, and node pressure line up alongside your application traces. The result is the thing every other tool asks you to assemble: [a single place where you see a pod's memory climbing, the OOM kill, and the exact request trace that triggered it](https://pydantic.dev/articles/kubernetes-cluster-observability-logfire).

On top of that trace sits the AI-engineering loop the incumbents do not have. Evaluation runs on the same traces you already emit, online and offline, with no separate per-score meter. The optimizer reads the runs that scored badly, finds the pattern, and proposes one evidence-cited change. Managed variables ship that change, an agent's instructions, model, and settings as versioned config, with targeting and rollback and no redeploy. Because it is all OpenTelemetry, any framework that speaks OTel lights up the same surfaces, and Pydantic AI, the type-safe agent framework, is wired in out of the box. Your coding agent can query the whole thing, agent spans and pod metrics together, in PostgreSQL-compatible SQL over the MCP server.

Pricing is flat and capped: 10 million records included, then $2 per million, with a hard spend ceiling, which matters when a cluster's worth of high-cardinality metrics meets large LLM spans. And when you need to keep everything in your own environment, [Logfire](https://pydantic.dev/logfire) self-hosts on your Kubernetes cluster via the official Helm chart, with your own PostgreSQL and object storage.

**Honest limitation:** the Kubernetes metrics path is a Collector you configure, not a one-click cluster integration, and Logfire's own marketing leads with AI observability rather than infrastructure, so the full-stack K8s story is one you have to go find. If your only need is cluster monitoring with no agents in sight, a pure infrastructure tool will feel more turnkey.

**Best for:** teams running real agents on Kubernetes who want the reasoning and the pod in one view, and a way to ship the fix. **Pricing:** free tier (10M records); Team $49/month; Growth $249/month; Enterprise custom.

### 

Groundcover is the strongest pure-play in this category after Logfire, and the most direct answer to Datadog's cost. It uses eBPF to capture the whole cluster with zero instrumentation, one Helm chart and no code changes, and as of April 2026 that capture extends to agents: full execution traces with every model call and tool invocation, token counts, and cost, emitted as OpenTelemetry gen_ai spans. So unlike the AI-only tools it sees the pod and the agent in one view, and unlike Datadog it is flat node-based pricing (roughly $30 to $50 per host, not a stack of per-product meters), with the data plane running in your own cloud so telemetry never leaves your VPC.

The gaps are the other half of the loop, and the limits of eBPF itself. Groundcover observes agents in production but has no evals, no prompt optimizer, and no managed configuration, so improving the agent happens somewhere else. And eBPF buys its zero instrumentation at a real cost. It runs only on schedulable Linux nodes, so Fargate and other serverless are out and Windows is unsupported; it wants a recent kernel; encrypted TLS and Java stacks need extra uprobes or an agent; custom binary protocols may not be parsed; and smart sampling with payload truncation means not every request is kept. The deepest limit is structural: eBPF watches syscalls and packets, not your code, so it cannot tell which business function, workflow, or tenant a request belongs to without exactly the application instrumentation it was supposed to spare you. The sensor is proprietary too, though several components (Caretta, Murre, the CLI) are Apache-2.0.

**Best for:** teams running agents on Kubernetes who want zero-instrumentation eBPF coverage, predictable node-based cost, and their data kept in their own cloud, and who run the eval loop elsewhere. **Pricing:** free tier; Pro $30/host/month; Enterprise $35/host/month; on-prem $50/host/month.

### 

Datadog knows Kubernetes as well as anyone: the Orchestrator Explorer maps pods, nodes, and deployments, and there is a dedicated OOM-kill integration and first-class CPU-throttling and resource views. Its Agent Observability product traces LLM and agent workflows with cost and token usage and an execution-flow view of an agent's decisions, and it has managed evaluations and experiments.

Two seams keep it out of the top spot. Its collection is proprietary-first: the Datadog Agent and dd-trace libraries are the native rails, and OpenTelemetry is a secondary ingest path that needs specific semconv versions and an opt-in. So "agent and cluster in one view" means instrumenting on Datadog's own agents, paying for two products, and correlating them on-platform, not one OTel-native view. And the loop stops at evaluate; there is no trace-backed optimizer or managed agent config. The other cost is literal: infrastructure, APM, and Agent Observability are separate meters (roughly $15 per infra host, $31 per APM host, plus per-span LLM billing), and Datadog's bill-shock reputation is well earned. One customer's [surprise $65M bill](https://blog.pragmaticengineer.com/datadog-65m-year-customer-mystery/) became a genre of its own, with users noting "almost no way to put controls in place to prevent overspend."

**Best for:** organizations already standardized on Datadog that want AI tracing without adding a vendor. **Pricing:** multi-SKU, per host and per LLM span; Enterprise custom.

### 

Kubernetes monitoring is Grafana's home turf: the Kubernetes Monitoring app drills cluster to node to pod with dedicated CPU-throttling and OOMKilled triage. And as of GrafanaCON in April 2026, Grafana Cloud has native AI observability in public preview, with agent conversations, tool calls, tokens, cost, and live evals, instrumented OTel-natively via its SDK or a zero-code operator on the cluster. The AGPL core keeps it open.

The seam is honesty from Grafana itself: its own zero-code writeup describes correlating the AI and infrastructure layers "through a common platform... rather than unified traces." And the stack's center of gravity is still Prometheus: metrics in PromQL, logs in LogQL, traces in TraceQL, three query languages across the LGTM stack where an OpenTelemetry-native platform gives you one model and one SQL surface. The AI product is new and preview-stage, it stops at observe-and-evaluate with no optimizer or managed config, and getting to one story across agent and cluster still means standing up the instrumentation yourself. Cloud billing is by active series and ingested gigabytes, which is the cardinality trap teams [get burned by at scale](https://news.ycombinator.com/item?id=31387327).

**Best for:** teams already running the Grafana/Prometheus stack for Kubernetes who want to add AI observability without leaving it. **Pricing:** free tier; Pro from $19/month plus usage; Advanced/Enterprise custom.

### 

New Relic has deep Kubernetes monitoring, including the cluster explorer and eBPF via Pixie, and its AI Monitoring product traces LLM calls with token and cost data, extended in late 2025 with agentic monitoring and an AI MCP server. It is a genuine full-stack incumbent.

But the AI half is the shallowest of the incumbents on the engineering loop: it surfaces responses, user feedback, and bias or hallucination signals, with no eval framework, no LLM-as-judge scoring, no optimizer, and no managed config. AI and Kubernetes live on separate product surfaces rather than one OTel-native view, instrumented through New Relic's own agents. And its per-user pricing is a recurring gripe, with the full-platform seat at $349 per user per year on top of data ingest, prompting complaints like ["our bill went up 20x for no additional value"](https://news.ycombinator.com/item?id=31197789) when the model shifted to per-user.

**Best for:** teams standardized on New Relic APM that want LLM traces in the same account. **Pricing:** per-user (Pro $349/user/year) plus data ingest ($0.40/GB).

### 

SigNoz is the closest to Logfire architecturally: OpenTelemetry-native, ClickHouse-backed, no proprietary agents, with APM, logs, metrics, and Kubernetes infrastructure in one place. It ingests `gen_ai` spans from LangChain, CrewAI, Pydantic AI, and others and renders agent workflows in the same UI as your pods, which means it really does put agent and infrastructure in one OTel-native view. The core is MIT-licensed.

Where it stops is the AI-engineering loop: evaluation and prompt management exist only "via integrations," with no native LLM-as-judge, no optimizer, and no managed config. It observes the agent and the cluster together but does not help you improve either. And self-hosting at scale is a heavy ClickHouse and ZooKeeper cluster; teams report it is [resource-hungry and operationally involved](https://news.ycombinator.com/item?id=45294767).

**Best for:** open-source teams that want one OTel-native view across agents and Kubernetes and will handle the eval loop themselves. **Pricing:** free self-host (MIT); cloud from $49/month, usage-based.

### 

Elastic monitors Kubernetes well (clusters, nodes, pods, DaemonSets via Elastic Agent, Beats, or OTel) and, since August 2024, Elasticsearch is AGPLv3 and OSI-approved open source again. Its LLM observability, though, is an explicit tech preview delivered through EDOT, and its Agent Builder is a separate preview for building retrieval agents over Elasticsearch data, not for optimizing the agents you run. There is no eval or optimization loop tied to the observability.

The other cost is operational. Elastic's reputation for taking a PhD in Elastic to run well, between the query DSL, index lifecycle management, and cluster tuning, is real enough that Elastic shipped AutoOps to catch the misconfigurations. It is a capable cluster monitor with an immature AI bolt-on.

**Best for:** teams already deep in the Elastic Stack for logs and Kubernetes who can treat AI observability as early-stage. **Pricing:** resource and usage-based on Elastic Cloud.

### 

Langfuse, LangSmith, Arize, and Braintrust are strong at the agent: tracing, evals, datasets, prompt management. On Kubernetes they share one hard limit, they do not monitor infrastructure at all. There are no pod, node, or host metrics, no OOMKill or throttling signals; Kubernetes appears in their docs only as a place to deploy them, never as something they watch. When the 2am truncation is a memory limit rather than a prompt, the trace goes quiet exactly where you need it, and you are back in a second tool. Braintrust is refreshingly direct about it, telling you to pair it with Datadog for the infrastructure half. Use these to evaluate the agent; do not expect them to see the cluster it runs on.

**Best for:** the eval and prompt-engineering layer, beside a separate infrastructure tool.

### 

Tools like kagent, KubeAI, Ray, and Argo Workflows are how you *run* agents on a cluster: operators, model servers, and orchestration. They are not observability or AI-engineering platforms, and none correlates an agent's reasoning with cluster health. They sit upstream of everything in this list; you still need one of the platforms above to see and improve what they run.

## 

| Platform | Agent + cluster in one OTel view? | K8s monitoring | AI-engineering loop | Open standards | Best for | 
|---|---|---|---|---|---|
| **Pydantic Logfire** | Yes, by default | Pods, nodes, OOMKills, throttling (Collector) | Evals + optimizer + managed config | OTel-native, MIT SDK | Agents on K8s, full stack | 
| **Groundcover** | Yes, via eBPF (infra + agent) | eBPF, zero-instrumentation | None (observe only) | eBPF-first; OTel ingest, sensor proprietary | Own-your-data eBPF on K8s | 
| **Datadog** | Correlated, SDK-first, separate SKU | Deep (Orchestrator Explorer, OOM integ) | Evals + experiments; no optimizer/config | SDK-first; OTel secondary | Existing Datadog shops | 
| **Grafana** | Correlated layers, "not unified traces" | K8s-native home turf | Evals (preview); no optimizer/config | OTel-native; AGPL core | Grafana/Prometheus teams | 
| **New Relic** | Separate product surfaces | Mature + Pixie eBPF | AI monitoring; no eval loop | SDK-first; OTel ingest | New Relic APM shops | 
| **SigNoz** | Yes, OTel-native | Yes, OTel-native | None native (integrations only) | OTel-native, MIT | OSS OTel-native teams | 
| **Elastic** | Bolt-on (tech preview) | Mature | None | OTel; AGPL core | Existing Elastic estates | 
| **AI-native tools** | No infrastructure at all | None (blind to the cluster) | Evals; optimizer varies | Mixed | Agent evals beside a separate tool | 

## 

Start with the failure you cannot currently debug. If your agent breaks and you cannot tell whether it was the model or the pod, you need agent and cluster in one view, and that rules out the AI-native tools on their own. If you already run Datadog, Grafana, New Relic, or Elastic for the cluster, you can bolt their LLM product onto it, as long as you accept a second SKU or a correlated-not-unified view and no optimize-and-ship loop. If you want zero-instrumentation eBPF coverage and your data kept in your own cloud, Groundcover is the strongest alternative, as long as you run the eval loop elsewhere. If you want one OpenTelemetry-native view across both and you are happy to build the eval loop yourself, SigNoz is the open-source answer. If you want that one view and the AI-engineering loop and flat pricing, that is the gap Logfire fills.

For most teams building real agents on Kubernetes, Pydantic Logfire is the strongest starting point: one OpenTelemetry-native view from the agent's reasoning to the pod that killed it, an evaluation and optimization loop that ships the fix, flat and capped pricing, and the option to run the whole thing on your own cluster.

## 

**What does "observing agents on Kubernetes" actually require?**

Two things most tools split apart: the agent's trace (model calls, tool calls, tokens, eval scores) and the cluster's health (pod restarts, memory limits, OOMKills, CPU throttling, node pressure), on one timeline linked by shared Kubernetes attributes. Without both, a failing run cannot tell you whether the cause was the prompt or a pod that ran out of memory.

**Can Datadog or Grafana show the agent and the cluster in one view?**

Partly. Both monitor Kubernetes deeply and both now have AI or LLM observability, but the AI layer is a separately priced or separately instrumented product correlated next to the infrastructure. Grafana describes this in its own words as correlating "through a common platform... rather than unified traces." Neither adds a trace-backed optimizer or managed agent configuration.

**Are the AI eval tools (Langfuse, LangSmith, Arize, Braintrust) enough on Kubernetes?**

For evaluating the agent, yes. For running it on a cluster, no: none of them monitors infrastructure, so they cannot see a pod OOMKill or node pressure. Braintrust's own documentation recommends pairing it with an infrastructure tool like Datadog. You would run two products and correlate by hand.

**What about kagent, KubeAI, or Ray?**

Those run agents on Kubernetes: operators, model serving, orchestration. They are not observability or AI-engineering platforms and do not correlate agent behavior with cluster health, so you still need one of the platforms above to see and improve what they run.

**Which options are open source?**

SigNoz (MIT) and Grafana (AGPL core) are open-core and OpenTelemetry-friendly; Elasticsearch is AGPLv3 again as of 2024. Pydantic Logfire's SDK is MIT and OpenTelemetry-native, and the full platform self-hosts on your own Kubernetes cluster via the official Helm chart.

## 

You can have agent traces and Kubernetes metrics in one place in a few minutes: point the OpenTelemetry Collector at your cluster and your agents at Logfire. The free tier includes ten million records a month.

[Start free with Pydantic Logfire](https://logfire.pydantic.dev/)

AI is still just engineering.
