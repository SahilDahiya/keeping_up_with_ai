---
title: 'Agents Week: ship real agents and fix them from production traces | Pydantic
  Logfire'
kind: blog
topic: evals-observability
subtopic: monitoring
secondary_topics:
- agents/harness
summary: Argues that agent quality is learned from production traces rather than pre-ship
  eval suites ('evals are a steering wheel, not a destination; it's a trace, not a
  test'), and that at scale you observe a 'herd' of agents over OpenTelemetry rather
  than hand-tuning each one.
triage: null
skip_reason: null
source: pydantic
url: https://pydantic.dev/articles/agents-week
author: Bill Easton
published: '2026-07-13'
fetched: '2026-07-16T22:02:49Z'
classifier: claude
taxonomy_rev: 2
words: 968
content_sha256: 53870a251c3e4a7c43dbdcd56787e56c0e4c200b0fd482d44fc56603d3fd6012
---

# Agents Week: ship real agents and fix them from production traces | Pydantic Logfire

Ninety-five percent of enterprise AI pilots fail. The few that reach production split in two, and it's the second group nobody warns you about: they shipped, and they shipped the wrong agent.

The ones who never shipped and the ones who shipped wrong made the same bet: that they could perfect the agent before they'd earned the right to know what it was for. Weeks on the eval suite, the dataset, the tool descriptions, the model, the sampling settings. Tuning a thing they had never once watched meet a real user. Evals are a steering wheel. A steering wheel decides how you drive, not where. You can steer flawlessly to the wrong address.


This is not an argument against evals. Evals are how you find out whether the agent does the thing. The mistake is believing you can finish that work before you ship, because the harder question, whether it's the thing anyone needed, was never in your eval set. It's in production. It's a trace, not a test.

So you ship earlier than is comfortable, on purpose, and you read what comes back. The requirement you got wrong shows up in the runs, not the rubric: the tool the model reaches for that you never anticipated, the question your users actually ask, the fluent and confidently wrong answer that no assertion caught. You learn which agent to build by running the one you have.


Last month we argued that [agents are the new services](https://pydantic.dev/articles/agents-are-the-new-services), and shipped the operational half you already recognize: Services, Kubernetes, Hosts, Metrics. Here's the corollary nobody says out loud. You don't hand-raise a service. You run a herd of them.

Today you might have a handful of agents. You can name each one, tune it by hand, and mourn it when it breaks. Gartner thinks the average large enterprise will be running over a hundred thousand within three years, up from about fifteen. At that number an agent is not a pet. It's one animal in a herd, and the only thing that has ever made a herd manageable is being able to see every animal in it. The enterprise vendors will sell you a control tower that watches the agents they sold you. Your herd is spread across every model and framework you use, and all of it speaks OpenTelemetry. You need to see the whole thing, not one vendor's paddock.

That's the week. Ship the rough agent, read what production tells you, change it without ceremony, and do it across the herd instead of one prize animal at a time. **Ship it. Optimize it. Move on.** You make the calls. Logfire runs the herd.


- 
**Tuesday. See the herd.**[The agent and LLM views](https://pydantic.dev/articles/logfire-agents-llms-view). An inventory of every model you run, with latency, throughput, and cost, priced from Pydantic's open-source[genai-prices](https://github.com/pydantic/genai-prices)dataset so you can check the math. Per-agent run distributions that surface the runaway: the one run in ten thousand that fired forty tools where the median fired three. And a Tools tab that reconstructs exactly what the agent was allowed to do on the run that went wrong.
- 
**Wednesday. Control the dependency.**The[AI gateway](https://pydantic.dev/articles/logfire-ai-gateway). One key for every provider, with failover, load balancing, per-key spending caps that block the request before it bankrupts you, and guardrails that scan every prompt and completion for PII and secrets on the way through. A model gets deprecated, throttled, or quietly repointed on someone else's schedule; this is how you route around it without a deploy and without a second billing relationship.
- 
**Thursday. Catch the wrong agent.**Annotations. An automated judge can tell you the answer was fast and polite. It cannot always tell you it was wrong for your business. A human can, in three keystrokes, and that verdict becomes durable, structured data your evals learn from, kept long after the trace itself has aged out.
- 
**Friday. Change it, and ship it.**The optimizer reads your production traces, finds the pattern in the failures, and proposes one evidence-cited edit to your prompt. Accept it and managed variables take it live with a label move: no deploy, no rollback plan, and rollback is moving the label back. Feature flags for the part of an agent that isn't code.


These surfaces are not a grab bag. The views find the failing run. A human annotates the one the eval blessed and the customer didn't. The optimizer reads that annotated trace and the thousands around it and proposes a fix grounded in what actually happened. Managed prompts ship it without a deploy. The gateway keeps the provider honest while you do. Every step is the same distributed trace, in the same product, on the same free tier, queryable in SQL and readable by your coding agent through our [MCP server](https://pydantic.dev/docs/logfire/guides/mcp-server/). The loop that used to span four vendors and a deploy is now one product.

Every one of those surfaces runs on the traces you already emit. Your production traffic is the substrate: the thing the views read, the annotator grades, and the optimizer learns from. There's no eval corpus to curate and nothing new to instrument. And none of it asks which framework you used. Pydantic AI is wired up out of the box; LangGraph, the OpenAI SDK, the Vercel AI SDK, CrewAI, or anything else that speaks OpenTelemetry lights up the same surfaces on the same `gen_ai.*` spans. We built on OpenTelemetry so the herd is legible by construction.

Ship the rough one. Read what comes back. Change it without a deploy, and do it at the scale a herd demands. A perfect agent you never shipped is just an expensive opinion.

Read along this week, or [open Logfire](https://pydantic.dev/logfire) and point it at your own agents. The free tier includes 10 million spans a month, the AI Gateway, and everything you need to stop tuning pets.
