---
title: '100 AI Agents Per Employee: The Enterprise Governance Gap'
topic: product-engineering
subtopic: security
secondary_topics:
- agents/planning
summary: Argues that enterprises adopting large populations of AI agents need governance
  for permissions, ownership, auditability, and lifecycle management before agent
  scale outpaces human oversight.
source: arize
url: https://arize.com/blog/100-ai-agents-per-employee-governance-gap
author: Chris Cooning
published: '2026-03-22'
fetched: '2026-07-11T04:55:19Z'
classifier: codex
taxonomy_rev: 1
words: 1141
content_sha256: 182bf7364c611bbcb0f031279bfa22febb68441237373f99b533ac36ff2bcc39
---

# 100 AI Agents Per Employee: The Enterprise Governance Gap

# 100 AI agents per employee: The enterprise governance gap

NVIDIA CEO Jensen Huang recently described a future where companies operate with roughly 100 AI agents per employee. That future is already starting to take shape. McKinsey reports 25,000 of its “employees” are agents, working alongside 60,000 humans.

Then NVIDIA GTC happened. The company expanded its [Agent Toolkit](https://developer.nvidia.com/nemo-agent-toolkit): OpenShell as an open-source secure runtime, [NemoClaw](https://www.nvidia.com/en-us/ai/nemoclaw/) for sandboxing OpenClaw with policy-enforced network and filesystem controls, and the AI-Q research agent blueprint, all backed by Nemotron open models. Adobe, Salesforce, SAP, and more than a dozen other enterprise platforms signed on. The message wasn’t subtle: AI agents aren’t a proof-of-concept anymore. They’re operational infrastructure, and the enterprise software industry is building for them accordingly.

So the conversation has to change. The question isn’t whether to deploy agents like OpenClaw (that decision has already largely been made). The question is: six months from now, will your organization be able to account for what those agents did, step by step?

## The gap between policy and runtime

Most enterprises deploying agents today have some version of a governance policy. Access controls, defined scopes, an AI acceptable use framework: the bones of governance are there. The problem is that policies describe what agents are supposed to do. They say nothing about what agents are actually doing real-time in production.

Agents fail differently from traditional software. A broken API call throws an exception. An agent reasoning failure produces confident, plausible output that’s completely wrong. There is no error, no alert, no log entry flagging that anything went sideways. When you’re running one or two agents across your organization, a human is likely to notice. At fifty agents per employee, that’s not a reasonable assumption at all.

[A field analysis of production agent failures](https://arize.com/blog/common-ai-agent-failures/) found that the most expensive failures aren’t crashes or hallucinations caught at the surface. They’re silent errors that get picked up by the next turn or agent in the pipeline and amplified before anyone realizes something went wrong. In a multi-agent workflow, bad output doesn’t stop it becomes the next agent’s input (garbage in, garbage out). By the time the problem surfaces, you’re already downstream.

That’s the governance gap: the distance between what your policy says and what’s actually happening at runtime. A lot of organizations have little to no visibility into that distance. Traditional APM tools lag and lack the depth to trace agents turn-by-turn. And they only discover the gap after the fact — once the damage is already done.

## The real risk isn’t the incident. It’s what comes after.

The operational exposure is obvious. An agent with access to customer data, financial systems, or external communications can cause real harm without ever triggering a security alert. Misconfigured scope, misunderstood context, behavioral drift over time: none of these require malicious intent to produce bad outcomes at scale.

But the harder risk to quantify is trust, and it’s probably the one that should worry executives more. Enterprise AI adoption is still early enough that it’s fragile. One high-visibility failure (an agent that sent something it shouldn’t have, disclosed information it had no business sharing, or made a decision that ended up in front of a customer or a regulator) doesn’t just cost you the incident. It costs you the six months of internal momentum you spent building. It creates the kind of organizational resistance that’s very difficult to reverse once it takes hold, because now everyone who had doubts has an example.

The companies that get through the next few years without that kind of setback will be the ones that treated observability and [evaluation](https://arize.com/llm-evaluation/) as infrastructure rather than a diagnostic they’d pull out after something broke.

## What closes the governance gap

Identity and access controls are table stakes at this point, and most mature deployments have them. Every agent gets an identity, permissions are scoped explicitly, agents can’t inherit privileges from the humans or orchestrators above them. That part of the problem is largely solved.

What’s missing is runtime visibility and enforcement.

Runtime visibility means a complete record of what agents actually do: what decisions they made, what data they touched, what tools they called, what they produced, and in what sequence. Not just “the agent ran and returned a result,” but the full chain of action, traceable after the fact. This is the audit trail your compliance and legal teams will inevitiably ask for, and it’s the signal that lets operations teams catch behavioral drift before it becomes a liability. [How agents manage memory across sessions](https://arize.com/blog/how-to-manage-llm-context-windows-for-ai-agents/) is part of this too. Agents with persistent memory accumulate context over time, and that accumulation needs to be traceable, not a black box you can’t inspect.

Enforcement means acting on that visibility before problems compound. Not every agent action carries the same risk: an agent summarizing a document is not the same as one initiating a financial transaction or sending an external communication. [Observability-driven sandboxing](https://arize.com/blog/how-observability-driven-sandboxing-secures-ai-agents/) is the technical layer that makes enforcement real, intercepting agent actions at runtime, evaluating them against policy, and making a call before they execute rather than reviewing the damage afterward.

The organizations running this well have connected the two: they’re not just observing, they’re [closing the loop between telemetry and behavior change](https://arize.com/blog/closing-the-loop-coding-agents-telemetry-and-the-path-to-self-improving-software/), so the governance layer learns alongside the agents it’s governing.

## The case against waiting

The usual argument for deferring governance investment is speed: get agents deployed, then clean up the compliance side once you know what you’re dealing with. It’s a reasonable-sounding argument that tends to break down the moment something goes wrong.

Retrofitting observability and evaluation gates into a production agent deployment is genuinely hard. The audit trail you didn’t collect doesn’t exist. The behavioral drift you didn’t catch is already baked in. And the regulatory environment isn’t standing still. With frameworks like the [EU AI Act](https://arize.com/blog/quick-guide-to-the-eu-ai-act-for-ai-teams/), governance and auditability requirements are becoming explicit. AI governance requirements are now moving through the compliance stack in financial services, healthcare, and any organization subject to data regulation. The question of which agent accessed which data, when, and what it produced will not remain optional for long.

GTC 2026 drew a line. The enterprise infrastructure for AI agents is built, funded, and shipping. Phoenix is already embedded in that stack: NVIDIA’s own [DeepLearning.ai course on the NeMo Agent Toolkit](https://www.deeplearning.ai/short-courses/nvidia-nat-making-agents-reliable/) uses Phoenix tracing as the observability layer, and the toolkit ships with a native Phoenix exporter alongside support for any OpenTelemetry-compatible backend. What most organizations haven’t caught up on is the governance layer underneath it, and that gap is exactly where the risk lives right now.

Arize provides the observability and evaluation platform that AI platform teams use to trace, evaluate, and govern AI agents in production, from runtime sandboxing to[automated evaluation at scale](https://arize.com/blog/best-ai-observability-tools-for-autonomous-agents-in-2026/). If you’re working through what governance infrastructure looks like for your deployment,[start here](https://arize.com/request-a-demo/).
