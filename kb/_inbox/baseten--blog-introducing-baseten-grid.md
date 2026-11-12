---
title: Introducing Baseten Grid
kind: blog
topic: null
subtopic: null
secondary_topics: []
summary: null
triage: null
skip_reason: null
source: baseten
url: https://www.baseten.co/blog/introducing-baseten-grid
author: Sai Maddali
published: '2026-11-04'
fetched: '2026-11-12T06:07:10Z'
classifier: null
taxonomy_rev: 2
words: 1187
content_sha256: 7a5f93829c52d79e96d25ded022d68512e1223d8194337873bf7797b07f65f1b
---

# Introducing Baseten Grid

Product
# Introducing Baseten Grid

Put the right model to work on every task and cut AI coding spend, with intelligent routing, unified access, and enterprise control.


- Authors
- Date
- November 4, 2026

TLDR

Baseten Grid helps enterprises accomplish more with their AI spend. Grid is a single layer to route requests, monitor usage, and govern access. In early benchmarks, Grid cut cost per coding task by up to 70% with minimal quality loss. Grid is in public preview starting today.

AI coding spend has become one of the fastest-growing line items for enterprises. [Over 90% of developers now use AI tools weekly](https://blog.jetbrains.com/research/2026/08/ai-coding-agent-adoption-2026/), and as adoption has exploded, so have costs. Everyone wants AI to take on more demanding work, but that requires matching each task to the right level of intelligence. Thankfully, there are more options than ever: open models now match frontier-class performance on many tasks at up to [3x lower cost,](https://www.baseten.co/resources/customers/how-parallel-web-systems-pioneers-programmatic-web-with-high-throughput-agentic-i) sparing frontier models for the tasks that truly need them. The challenge is knowing which tasks need Astra vs. which are better for DeepSeek Flash.

Today, developers are left to make these decisions on their own, while platform teams juggle the models, harnesses, budgets, and policies that come with using many different providers and tools. Baseten Grid brings this into a single place: access open and closed models through one gateway, route requests based on your quality and performance requirements, and apply controls across your organization.

Baseten Grid helps enterprises get more useful work from their AI spend by bringing together three capabilities:

- **Intelligent Routing:** selects the best-fit model for each request from your list of approved models. Our custom router, Baseten Router, considers expected task performance and cost, including retries, failed tool calls, and incomplete answers. In our benchmarks, Baseten Router has reduced cost per task by up to 70% with minimal quality loss.
- <u>**Gateway:**</u> governs model access across closed- and open-source model providers, including OpenAI, Anthropic, Gemini Enterprise Agent Platform, Amazon Bedrock, and Baseten. View all your AI usage in one place, with team-level model access, budgets, and company-managed credentials.
- <u>**Guardrails:**</u> brings configurable safety policies, and visibility into risks, centrally at the gateway layer so every request and response undergoes safety compliance in a single place.

As AI adoption has surged, developers have carried the burden of matching models to tasks themselves. But the right answer changes constantly, which is why picking models can't be a manual chore. With the right intelligence, that decision can be made automatically and efficiently for developers, every time. Grid solves this with built-in intelligent routing via Baseten Router.

Baseten Router chooses between your approved open- and closed-source models based on expected performance and cost for each task. Intelligent routing goes beyond routing based on token price; it also accounts for the cost of retries and failed tool use. The goal is to reduce the cost of a complete task while meeting your team's quality and performance requirements.

In initial benchmarks, Baseten Router can achieve nearly 70% cost savings with only a 0.9- percentage-point quality tradeoff versus Opus 5.5 (exact cost savings will vary based on your team's workload shape and desired cost and quality tradeoffs). Teams can also opt in to sharing traces, which can be used to train custom routers for Pareto efficiency for your specific workload.

"*Almost everyone at Opendoor uses AI, and most people don’t want to have to form an opinion on which model to pick. Grid has enabled us to get visibility into all our internal AI spend in a single place, and intelligent routing helps us cut spend automatically with minimal quality loss.*"


Grid’s Gateway gives organizations one place to approve models, manage access, set budgets, and understand usage across every team, application, and agent. Today, Grid supports models from OpenAI, Anthropic, Gemini Enterprise Agent Platform, Amazon Bedrock, and Baseten. Every request passes through a single gateway, built on our production infrastructure with the security and compliance you know from Baseten.

Developers connect the harnesses they already use - Claude Code, Codex, OpenCode, and Pi in a single command. Admins can also automate this configuration through an MDM. The same endpoint governs your in-house applications and agents: if it calls the Anthropic or OpenAI API, it can connect with a base URL and a model ID. You get the control and visibility of a centralized system without changing how your team works.

As AI adoption grows across models, agents, and harnesses, so does the attack surface for organizations. Every day, agents can read internal documents, call tools, and act on production systems, opening the door to new risks at the inference layer: instructions hidden in a document that redirect an agent, actions no one authorized, and customer data appearing where it shouldn’t. Most teams handle this with separate filters and review processes for each application, which becomes hard to govern at scale.

Grid’s guardrails give security and AI platform teams a safety baseline they can apply centrally. Policies can be adjusted by workload with clear records of what was flagged and how it was handled.

Guardrails are one layer of protection, not the whole stack: safety checks catch a risky request or response, while execution controls decide what an agent can access and do. Enterprises need both. We’re also working with Goodfire on [Project Beacon](https://www.baseten.co/blog/safe-open-models-baseten-goodfire/) to go further, using signals from inside the model to catch unsafe behavior as it happens, before the output reaches a user or a tool.

We think gateways and routers are the first layer to unlock durable returns on intelligence. More work happens underneath the gateway layer: routing, translating model/harness protocols, caching, scaling, and optimizing so each request reaches the right model, on the right deployment, and is processed inside the GPU kernel as efficiently as possible.

We obsess over those details and build them into our platform so your experience feels effortless. Our model performance research, post-training, and infrastructure teams work together, from custom kernels and speculative decoding to the evals every model must pass before it ships. All of this work is how Grid unlocks lower cost per task: requests land on the right model with the right cost/intelligence tradeoff via Baseten Router, and for models served by Baseten, long multi-turn agentic sessions are routed to warm KV cache so you pay less for the same intelligence.

Soon, Grid will let you delegate longer-running work to cloud-hosted agents and coordinate multiple agents on complex tasks. Routing tuned to your data and use cases will help you meet quality requirements more efficiently, while richer safety signals and support for your own guardrails will help you catch risky behavior and apply your policies.

As you put more AI to work, Grid will give you one place to manage it across your company. Grid connects what agents accomplish with what they cost so you can get more from your AI spend while preserving a great experience for your users.

Grid is now in public preview. [Join the waitlist](https://www.baseten.co/talk-to-us/request-access-grid) for early access and work directly with our team to set up model access, budgets, intelligent routing, and guardrails for your organization.
