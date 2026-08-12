---
title: How Gumloop Scaled Open-Weight Model Usage 7x in 3 Weeks with Fireworks
kind: blog
topic: null
subtopic: null
secondary_topics: []
summary: null
triage: null
skip_reason: null
source: fireworks
url: https://fireworks.ai/blog/gumloop
author: null
published: '2026-07-09'
fetched: '2026-08-12T06:29:23Z'
classifier: null
taxonomy_rev: 2
words: 749
content_sha256: 695bcdab6be39dd4de0b932ff3ddd386dd15ececf2a22aab2332dc2cc30569f2
---

# How Gumloop Scaled Open-Weight Model Usage 7x in 3 Weeks with Fireworks

AI teams are reaching a turning point. Open-weight models are becoming capable enough to power real production workloads, giving teams more flexibility over how they build and scale AI applications.

For [Gumloop](https://www.gumloop.com/), that shift created an opportunity to rethink how AI agents are powered.

As usage grew, inference costs increased for both Gumloop and its customers. The team saw that many agent workloads could be handled by open-weight models, but only if those models delivered the reliability and quality required for production.

After optimizing its agent harness for open-weight models and partnering with [Fireworks](https://fireworks.ai/) for inference, Gumloop made open-weight models a first-class option in its platform. Within three weeks, the number of agent chats running on open-weight models grew **7x**.

Gumloop helps teams build AI-powered workflows and agents that automate complex tasks across their organizations. These agents perform a wide range of tasks, including information extraction, classification, routing, summarization, and other workflow steps.

As adoption increased, Gumloop saw the economics of AI becoming a growing consideration. Every additional workflow could introduce more model calls and higher inference costs.

At the same time, newer open-weight models such as GLM-5.2 and DeepSeek V4 Pro reached a level of capability that made them viable candidates for production agent workloads.

The remaining question was whether they could deliver the experience users expected.

Gumloop tested that question internally with one of its most important agents: a company-wide assistant that employees use to access company data and answer questions.

Previous attempts to move this agent from frontier models to open-weight alternatives had failed. Employees noticed the difference immediately, and the team would move the agent back to Opus.

That changed when Gumloop moved the agent from Opus 4.8 to GLM-5.2 running on Fireworks.

Nobody noticed.

The outputs remained consistent with Opus, giving Gumloop confidence that open-weight models were ready to become a recommended production option.

"The aha moment was when we were deciding whether to roll out GLM-5.2 as one of our recommended model options. We felt Fireworks gave us the confidence to do this without reliability concerns. We have a main agent that has access to all of our data that everyone across the company interacts with and asks questions. When we moved this agent from Opus 4.8 to GLM-5.2, nobody noticed a difference in the experience. The outputs were consistent with what we expected, which gave us the confidence to make GLM-5.2 a recommended model option."

**Gonzalo Soto Mallqui, Chief Product Officer, Gumloop**

For Gumloop, adopting open-weight models required optimizing the entire agent experience around them.

The team optimized its agent harness for open-weight models and validated models internally before making them available to customers. Open-weight models now power Gumloop agent workflows as well as supporting operations such as classification, tagging, and evaluation.

After moving its internal agent from Opus 4.8 to GLM-5.2, Gumloop saw up to **72% cost savings** while maintaining the same user experience.

Production AI workloads require infrastructure that can deliver consistent performance and reliability at scale.

Gumloop evaluated multiple inference providers before selecting Fireworks as its default inference provider for open-weight models.

Reliability was the deciding factor.

"The biggest benefit has been reliability. We tried other providers, but we've seen Fireworks lead in this sense, as well as respond to our requests and queries very fast."

With Fireworks, Gumloop gained the confidence to make open-weight models a recommended option for production agent workloads.

By combining its optimized agent harness with Fireworks' inference platform, Gumloop achieved:

- •**7x growth** in agent chats running on open-weight models in three weeks
- •**Up to 72% cost savings** after moving an internal production agent from Opus 4.8 to GLM-5.2
- •Confidence to recommend open-weight models for production agent workloads
- •Reliable infrastructure for scaling open-weight model adoption

"Gumloop is a fascinating example of how every company will build AI agents tailored to its own workflows and data. The future of AI belongs to specialized intelligence built on open models, and we're proud that Fireworks provides the infrastructure that lets those agents run with the speed, reliability, and efficiency required for production."

**Lin Qiao, CEO, Fireworks**

Gumloop's experience reflects a broader shift in AI development. As open-weight models improve, teams have more flexibility to choose the right model for each workload based on capability, cost, and control.

For Gumloop, the breakthrough was reaching the point where open models could deliver the quality users expected while improving the economics of running AI agents.

With Fireworks powering inference, Gumloop is bringing that approach to production scale.
