---
title: Designing the AI Agent Supervision Experience
topic: product-engineering
subtopic: ux-patterns
secondary_topics:
- agents/planning
summary: Discusses UX and workflow design for supervising AI agents, including human
  oversight and intervention surfaces.
source: cresta
url: https://cresta.com/blog/designing-the-ai-agent-supervision-experience
author: Zewen Liang
published: '2026-05-01'
fetched: '2026-07-11T03:57:48Z'
classifier: codex
taxonomy_rev: 1
words: 1260
content_sha256: ff59f46972e80b5aa77675581acd8d190f41cfe6fd1838b098a4c7b7c2ff4e7a
---

# Designing the AI Agent Supervision Experience

Agentic AI workers powered by tools like OpenClaw or Claude Cowork have gained attention recently, and the promise is compelling: digital workers equipped with specialized skills that can proactively handle tasks – even when you’re not present.

But what happens when the plan doesn’t work out? As these agents gain more autonomy, the stakes of failure also rise. [Recent reports](https://techcrunch.com/2026/02/23/a-meta-ai-security-researcher-said-an-openclaw-agent-ran-amok-on-her-inbox/), such as a security researcher’s AI agent accidentally wiping an entire email inbox, highlight a critical reality: autonomy without oversight is a liability. For designers, the challenge has evolved; it is no longer just about *“designing an AI that works end-to-end”*; it’s about designing the systems of supervision and trust required for when that AI inevitably stumbles or deviates.

Cresta offers several layers of solutions to ensure reliable, enterprise-grade AI agents that deliver high-quality customer experiences:

- **Before**AI Agent deployment: robust testing, evaluation, and safety harnesses.
- **During**AI Agent operation: real-time guidance and instant intervention
- **Post**AI Agent conversations: quality assurance and continuous optimization loop

![](https://cdn.prod.website-files.com/67feba4d16c14d85f1696c4f/69f388da5e8b158432ebc58a_1st%20inline%20image.png)

[Last November](https://cresta.com/blog/beyond-automation-how-crestas-new-innovations-give-businesses-control-and-confidence), we launched the Agent Operations Center at Cresta to address the “Live Operations” layer of this framework. The Agent Operations Center provides supervisors with a “mission control” to oversee AI agents in real time. This enables a collaboration loop where AI agents proactively request human assistance when they encounter uncertainty or risk, and humans can guide, correct, or take over when needed.

From the start, the Cresta Product Design team has had a front-row seat in shaping this initiative. The evolution of Agent Operations Center was driven by a set of five non-negotiable UX imperatives.


Supervising live AI agents is inherently chaotic. Dozens, sometimes hundreds, of conversations unfold simultaneously, each with its own context, urgency, and emotional tone. It’s not just visual overload – there are voices, intents, and edge cases competing for attention. It’s like standing in front of a wall of live TVs, all playing different channels at once. In a sea of 100 live chats, how can a supervisor know where to look, what matters, and when to act?

The product design team has explored multiple approaches, not to eliminate complexity, but to make complexity navigable – through the deliberate use of visual hierarchy, motion, and color. For example, this is the “grid view” at the top of the page, which, at a glance, compresses a high-volume system into a legible pattern: from lower-priority conversations, to those that need some attention, to those that demand immediate intervention. From this bird’s-eye view, supervisors can quickly decide whether to drill into a specific conversation or intervene in real time.

Grid view cuts through noise to surface signals across 100 live AI agent conversations.


When an AI deviates, every second of inaction is a risk to providing a great customer experience. Speed to intervene means supervisors can move from seeing a problem to intervening instantaneously. Our design centers on a high-clarity “action hub,” where all critical controls are consolidated into one surface, including context – a quick summary of what’s happening in the conversation and what’s needed.

Here are the different kinds of actions and modalities in the “action hub”: providing guidance to unblock or steer the AI agent, sending direct messages to customers, temporarily pausing and unpausing AI agents, transferring the conversation to a human agent, switching between concurrent AI agent requests within a conversation, watching live-stream screen recordings, spectating an interaction, and more. All of these controls are intentionally placed to optimize for speed and efficiency to intervene.

The "action hub" enables fast action across multiple modalities


"Steering an AI agent should feel like tapping a teammate on the shoulder. Internally, we deliberately use human-centered vocabulary. An AI agent 'raises a hand' when it needs guidance, and a supervisor can 'whisper' to steer the AI agent in real time."– Zewen Liang, VP of Product Design, Cresta

This isn’t just stylistic. It’s a deliberate design choice. While AI agents are increasingly human-like (in both realistic voice and capable reasoning), more importantly, this approach simplifies the mental model for customer experience. Supervisors already know how to manage people: assign tasks, check in, give feedback, coach behaviors, and escalate when needed. The same managerial skills should apply to managing AI agents.

By blurring the two experiences, we reduce the overhead of retraining supervisors or redefining new roles, because supervisors who are effective with human agents should be equally effective with AI agents.

In fact, Cresta has always taken this approach of building a unified platform for both human and AI agents - the same system, the same capabilities, and the same experience. Here are examples of how the hybrid workforce (human and AI agents) can be supervised from a single place.

AI handraises should feel the same as human ones, on a unified AI + human agent platform


We should also acknowledge that AI agents, while powerful, will inevitably encounter intricate, high-stakes situations where the cost of a wrong answer is too high. The system should instill user trust so supervisors can intervene with confidence.

Confidence comes from control. To eliminate panic and enable decisive action, we designed the multi-turn guidance feature. It allows the supervisor to immediately halt the AI’s autonomous flow and take command of the conversation. The supervisor can engage directly with the customer for multiple turns, until the situation is stabilized or they feel sufficiently assured, before handing it back to the AI agent.

Multi-turn guidance: pause the AI agent, take control, and hand back with confidence.


The contact center has always been a team sport, where success depends on seamless collaboration across many players: specialists with different skills across departments, supervisors, AI agents, and customers. Designing a new tool in this space is not just about interfaces; it’s about designing the playbook. It means shaping the workflows that govern how work flows between these players.

And that playbook is far from simple. How do you distribute AI agent requests across available supervisors? What happens when a supervisor is already at capacity but new requests keep coming in? What if a “resolved” request resurfaces? What if a supervisor accepts an assignment but doesn’t respond in time? What if no supervisors are online and the issue needs to be escalated to a CCaaS queue?

In many ways, designing this operational pipeline is similar to building a ride-hailing platform that constantly balances demand (ride requests) and supply (drivers). The same rigor applies here. Working closely with our customers, we’ve thought deeply about these dynamics and translated them into a robust, end-to-end orchestration pipeline. The result is a system that doesn’t just handle complexity - it coordinates it.

Diagram of the orchestration system balancing demand (AI agent requests) and supply (supervisor skills and availability) before routing.


The industry often frames progress in AI as a march toward full autonomy. We see it differently. The future isn’t AI systems that operate without humans. It’s humans *and* AI operating in lockstep. At Cresta, this belief shapes how our Product Design team approaches AI: not as a feature, but as an integrated experience. The Agent Operations Center is the result of designing for **signals over noise**, **speed to intervene**, **human-centered interaction**, **trust through control**, and **orchestration at scale**. This is the kind of problem space we care about and continue to invest in.

If this resonates with you, we’re always looking for talented product designers to join us. Check out our [careers page](https://cresta.com/careers), and reach out at **zewen@cresta.ai**.

P.S. Thanks to Max Rico de Castro and Phoebe Wang, who interned with us last summer and helped explore the early ideas of the [Agent Operations Center.](https://cresta.com/agent-operations-center)
