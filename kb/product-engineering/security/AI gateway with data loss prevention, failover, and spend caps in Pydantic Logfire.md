---
title: AI gateway with data loss prevention, failover, and spend caps in Pydantic
  Logfire
kind: blog
topic: product-engineering
subtopic: security
secondary_topics:
- infra-platform/cost
summary: 'Makes the case for an LLM gateway as the single choke point for governance:
  one key across OpenAI/Anthropic/Google/Bedrock/etc., data-loss-prevention scanning
  of prompts and completions for secrets/PII (observe, flag, redact, or block), priority
  and weighted routing for failover/load-balancing, and hard per-key spend caps that
  block the request rather than alert after the budget is gone.'
triage: null
skip_reason: null
source: pydantic
url: https://pydantic.dev/articles/logfire-ai-gateway
author: Bill Easton
published: '2026-07-15'
fetched: '2026-07-16T22:02:41Z'
classifier: claude
taxonomy_rev: 2
words: 1024
content_sha256: 5f8c618fa568e8792dede3e68dce03de224c2fac49e6959512baccf28b73fcde
---

# AI gateway with data loss prevention, failover, and spend caps in Pydantic Logfire

A customer pastes an AWS key into your support chat. The agent does what agents do: bundles the conversation into a prompt and ships it to your model provider, key and all. Nothing errors. The answer is helpful. And the secret now sits in a third party's request logs, unrotated and unnoticed.

The flagship of this series made the point that an agent's data plane is a compliance plane. A service sees structured payloads you designed years ago; an agent sees whatever the user typed, whatever the tool returned, whatever retrieval dragged in. Some of it is PII. Some of it is somebody else's PII. And every prompt is an outbound transfer to a third party.

You don't fix that at the edges, service by service, one regex at a time. You fix it at the one place every prompt and completion already passes through: the gateway.


Point your app at one endpoint with one `pylf_` key, and route every provider through it. In [Pydantic AI](https://pydantic.dev/docs/ai/?utm_source=pydantic.dev&utm_medium=internal&utm_campaign=logfire-ai-gateway) it's a model string: `Agent('gateway/openai:gpt-5')`, `gateway/anthropic:...`, `gateway/google:...`. Under that one key you get:

- **One key for every provider.**OpenAI, Anthropic, Google, AWS Bedrock, Groq, Mistral, Azure, and more, either Pydantic-managed and prepaid, or bring-your-own-key so your existing provider contracts and rates carry over. The provider credentials live in the gateway and never leave it, so they're not scattered across your services' env vars, and rotating one is one update, not a deploy train.
- **Guardrails and data loss prevention.**Scan prompts and completions for secrets, PII, and policy violations, with prebuilt detectors, custom regex, or an external engine, and choose whether to observe, flag, redact, or block.
- **Routing groups.**Order providers by priority for failover, split traffic across them by weight for load balancing, and toggle any of them off, without touching your code.
- **Hard spending caps.**Per-key limits by day, week, month, or total, that- *block*the request when the budget is spent, not alert you after it's gone. Set per-member limits, a balance, and auto-recharge if you want the tap left on.


Data loss prevention only works at a choke point, and the gateway is the one you already have. Every prompt and completion passes through it, so the scanning happens once, at the boundary, for every agent behind the key, not once per app in code you hope stays deployed. And a redaction here is not a silent filter. The decision lands on the trace next to the call it protected, which is the shape an auditor actually asks for.

The pasted key is the friendly version. The helpful version is a coding agent so diligent it reads your `.env` file and ships the contents to the provider in a prompt, no attacker required. And the hostile version is an agent that reads a webpage, a support ticket, an email, and gets prompt-injected into exfiltrating what it knows: [the lethal trifecta](https://simonwillison.net/2025/Jun/16/the-lethal-trifecta/) of private data, untrusted content, and a channel out. Nobody has a reliable fix for the injection itself. But whatever an injected agent tries to send out has to be emitted by the model first, and everything the model emits comes back through the gateway as a completion. Scanning that direction too is how you cut the one leg you control.

The same boundary is where you manage the dependency that moves under you. A service depends on a database, and the database stays the database. An agent depends on a model that can be deprecated, throttled, or quietly repointed by a provider running to their own roadmap. Your p99 can double overnight with no change on your side. You cannot stop that from happening. You can decide in advance what happens when it does: failover so one provider's outage isn't yours, load balancing so a rate limit on one account isn't a wall, and a hard ceiling on spend so a retry storm or a prompt-injection loop can't turn into a five-figure invoice. A cap that blocks is the only kind that protects you.

Routing groups also work in the other direction: not just surviving a bad provider, but choosing a better one. Split traffic by weight, watch per-provider latency and cost in [the LLMs view](https://pydantic.dev/articles/logfire-agents-llms-view), and move the weight to the winner. Cost optimization becomes a routing decision you make on evidence, not a migration you schedule.

What makes ours different is that it isn't a separate box. Most gateways route and stop there; you bolt an observability vendor on beside them and reconcile two views of the same call. Here the gateway and the observability are the same product, on the same trace. The routing decision, the provider it landed on, the tokens it cost, the redaction that fired, and the failover that saved it are spans in the run you were already watching. And it's one control point for every agent you run: set a routing group, a cap, or a guardrail once and it governs the whole fleet, instead of per-app config you copy into a hundred services and update in none of them.

Because it inherits the rest of Logfire, the enterprise controls come with it: SSO, roles, and audit are the same ones you already set up, not a second access model to maintain.


If your app can set a base URL and an API key, you can be on the gateway in one line, and pointing [Pydantic AI](https://pydantic.dev/docs/ai?utm_source=pydantic.dev&utm_medium=internal&utm_campaign=logfire-ai-gateway) at it is a model-string change. Turn on the secrets and PII detectors and you have data loss prevention; add a second provider to a routing group and you have failover; set a monthly cap and you have a ceiling.

Back to the pasted key. With the secrets detector set to redact, the prompt goes through scrubbed: the customer still gets their answer, and the credential never leaves your boundary. The redaction is on the trace, ready for the audit. And the morning your provider has a bad one, the routing group fails over while you sleep. You read about both after coffee instead of during an incident.

Not using Logfire yet? [Get started](https://pydantic.dev/logfire?utm_source=pydantic.dev&utm_medium=internal&utm_campaign=logfire-ai-gateway). The free tier includes 10 million spans a month, the AI gateway, and so much more.
