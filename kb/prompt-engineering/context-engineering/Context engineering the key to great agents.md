---
title: 'Context engineering: the key to great agents'
topic: prompt-engineering
subtopic: context-engineering
secondary_topics:
- agents/memory-context
summary: Explains context engineering for agents, including how the right knowledge,
  state, and instructions shape agent quality.
source: sierra
url: https://sierra.ai/blog/context-engineering-the-key-to-great-agents
author: Neil Rahilly
published: '2026-05-12'
fetched: '2026-07-11T03:50:53Z'
classifier: codex
taxonomy_rev: 1
words: 1144
content_sha256: 53987de46a988f062b51ec44d4aa921bb9d94c0c53f30e23fe4f0c534bea6393
---

# Context engineering: the key to great agents

# Context engineering: the key to great agents

In media, it’s often said that content is king. For agents, it's context.

The large language models (LLMs) powering today’s agents are remarkably capable — not just at answering questions, but doing things. They can handle everything from returning an order to originating a mortgage or preventing subscriber churn.

But like people, they can’t act on information they don't have. And when overloaded, they lose sight of what’s important. Getting these models the right context, at the right time, is the central challenge in building sophisticated, real-world agents.

The solution: context engineering — deciding what information an agent has access to at each moment, and when it should be used.

## Three eras of customer interaction

To understand why, it helps to look at how customer interactions have evolved.

**Era 1: Interactive voice response (IVR)**. IVRs cannot think or reason. There’s only the menu. Press 1 for billing. Press 2 for returns. Press 0 to talk to a person. And if a customer’s issue doesn’t match precisely, they’re stuck.

**Era 2: Flow**. Many AI agents today still follow a predefined path — a flowchart, decision tree, or digitized standard operating procedures (SOPs). Customers can speak naturally, but the system still operates on “if this, then that.” When a problem falls outside the flow, it gets escalated. And as more SOPs are added, the system becomes harder to manage, increasing the risk of errors.

**Era 3: Context engineering**. The most sophisticated agents today are not driven by these more rigid flows. They’re guided by goals and constrained by guardrails. The models on which they are built drive the conversation, and the agent’s behavior adapts in the moment based on what it learns. Sierra’s role is to deliver the right context, at the right time — so they reason effectively and act correctly.

## Progressive disclosure

As the number of tokens (pieces of text) in a model's context window grows, its ability to recall and act on that information accurately declines. Every irrelevant token competes for the model's attention with the tokens that actually matter.

Context engineering solves this problem through progressive disclosure: providing only the minimum, most relevant information at each moment in the conversation.

For example, if a customer calls about an international shipment to Europe, the agent doesn't need custom rules for every country upfront. That information becomes relevant only after it learns the destination. If the shipment is going to Germany, the agent needs Germany-specific guidance. Until then, that information is noise.

## Conditions: the connective tissue

Conditions are what make progressive disclosure work. They answer the question: under what circumstances does this piece of information become relevant?

Conditions can be based on state (a tool returns specific data, the customer is authenticated, a subscription is loaded) or on observation (the customer mentioned a topic, expressed a desire to cancel, asked about a specific product). Once a condition is met, the information is given to the agent.

This layering ensures the conversation starts minimal — basic tools, general policies, brand voice — but can still handle long, complex customer interactions. As the conversation progresses and the agent learns more, additional information is provided. Once the customer is authenticated, account-specific tools and policies become available. Questions about a charge reveal the dispute workflow, policies, and tools needed to investigate the transaction. Each step unlocks exactly what's needed for the next.

## Types of context

Sierra’s platform structures context into manageable components. These include:

| Block | Purpose |
|---|---|
| Journey | A goal the agent knows how to pursue: dispute a charge, file a claim, book a flight. Each journey has a trigger and an outcome. |
| Tool | A way for the agent to interact with external systems: pull an itinerary, check coverage, process a refund. |
| Rule / Policy | Guardrails and business logic expressed in natural language (e.g., “Premium cardholders waive foreign transaction fees.”). |
| Workflow | Step-by-step guidance for situations that require a specific sequence, like regulated intake or multi-step verification. |
| Knowledge | Help center articles, product docs, FAQs, and internal policies the agent can access on demand. |
| Memory | The customer’s history: past conversations, preferences, and prior issues. |
| Glossary | The terminology your business uses: product names, plan tiers, and internal jargon. |
| Response phrasing | Brand voice and tone. |

A note on workflows: while we just discussed why rigid flows are limiting, some situations (like a highly regulated intake process) genuinely require them. The difference is that a workflow becomes just another piece of context made available when conditions are met, rather than the organizing paradigm for the entire system.

## Sierra handles the context engineering for you

The question, then, is how you actually build a system like this. Sierra represents an agent as a set of composable context blocks, each with an associated condition. We built an integrated stack to make this architecture usable — without sacrificing control:

- **Ghostwriter**: An agent that does the context engineering for you. You can give it natural language instructions or have it ingest your existing SOPs, call transcripts and documentation to produce context blocks and conditions automatically.
- **Journeys**: Our no-code editor lets you inspect and refine what Ghostwriter produced, or build directly in the UI.
- **Agent SDK**: Offers full programmatic control for teams that want to manage agents as code. Developers can define custom blocks or write arbitrary code.

No matter how you build it, it works the same way under the hood.

## Why this matters

With one task and a couple of tools, any modern agent will perform naturally and reliably. But at production scale — with dozens of supported use cases, multiple systems, and segment-specific policies — the realities of performance and complexity set in.

An agent that handles five journeys can get by with loose context management. One that handles fifty needs every piece of context to arrive at exactly the right moment. Without that discipline, the model gets overwhelmed, and the experience degrades.

Context engineering solves this at an architectural level. By sending fewer highly relevant tokens to the model, you reduce hallucination, improve naturalness, and increase performance. And you aren’t paying to process a thousand tokens of baggage policy during a simple flight rebooking.

More importantly, it future-proofs the agent. When you hardcode logic, you constrain the model — it can only be as capable as the paths you've predefined. With context engineering, the agent can reason more freely. As new, more capable models are released, your agent inherits that improvement.

A smarter model doesn't replace the need for context engineering. Even the smartest people can't know what they don't know. But it does amplify the payoff for doing it right.

Context engineering is the work of building great agents.
