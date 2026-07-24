---
title: 'Cresta’s Compass AI: Improving Discoverability in Enterprise Applications'
kind: blog
topic: null
subtopic: null
secondary_topics: []
summary: null
triage: null
skip_reason: null
source: cresta
url: https://cresta.com/blog/crestas-compass-ai-improving-discoverability-in-enterprise-applications
author: Zewen Liang
published: '2026-07-23'
fetched: '2026-07-24T06:49:41Z'
classifier: null
taxonomy_rev: 2
words: 1272
content_sha256: edce7eb4b6366e966ad667df59258adc6e0af8079d82649815d51adb808751fa
---

# Cresta’s Compass AI: Improving Discoverability in Enterprise Applications

**Introduction**

Cresta’s Director platform is where our customers manage every aspect of their customer experience (CX) AI: configuring AI agents, reviewing performance insights, managing quality, building coaching programs, and tuning conversation rules.

Like most enterprise products, Director is organized around distinct capabilities: Agents, Insights, Coaching, and Quality Management (QM). Each section maps to specific workflows, personas, and jobs to be done. That structure is valuable, and customers depend on it.

But as enterprise products become more agentic, the way users navigate them has to evolve. Rather than belonging to a single product area, AI can act as a collaborator that can assist users anywhere in the experience when given the right context.

This shift also changes what navigation is meant to accomplish. Traditional enterprise navigation answers the question, *“Where is this feature?”* But users aren’t trying to find features - they’re trying to achieve outcomes. An AI-first navigation experience instead helps answer a different question: *“What’s the next step toward my goal?”*

These ideas led us to rethink how users discover information and move through Director. The result is Compass, a new navigation experience centered around the Compass Support Agent - an AI collaborator our users chat with - and also helps users move seamlessly across workflows instead of product boundaries.

Traditionally, users had difficulty navigating between product areas. Compass agentically bridges that gap.

**What makes the Compass Support Agent different**

Building Compass Support Agent was different from building the AI agents we deploy for customers. While the same development process – defining requirements, testing through evals, and iterating with users – still applied, there was a unique opportunity to explore how we would embed it within our own product’s infrastructure.

**1. AI agent-first hierarchy**

Enterprise software is organized around products and capabilities because there’s an established mental model of where that should be found – much like you wouldn’t look for Coca-Cola in the produce section. But users don’t come to enterprise software to visit products; they come to accomplish goals. Users in Cresta need to venture between several different areas to accomplish their goals. For example, customers looking to improve care conversation outcomes will start with insights to discover trends, move to Opera where they build automations, and then configure monitoring through scorecards and quality management. Users can get lost moving between these steps of a workflow, and that’s where we’ve brought in Compass to bridge the gap.

Compass follows that workflow, helping users move across products with the right context instead of requiring them to navigate each destination on their own.

Cresta’s Compass Support Agent helps users find the next step in their workflow.

**2. Compass understands context**

Compass Support Agent understands far more than a user’s prompt. Because it lives inside Director, it can reason over the user’s role, current workflow, navigation history, and their current screen to deliver timely, relevant recommendations. Its greatest strength is leveraging the rich context already available throughout the platform.

In some cases, Compass Support Agent has enough context to automate entire workflows for our users. The traditional process of creating a support ticket is time-consuming and unnecessarily structured, requiring users to leave their workflow, manually gather context, and navigate rigid ticketing systems.

Compass takes a different approach. By integrating directly with our support systems and knowledge sources, it uses the context from a user’s conversation, browsing history, and current workflow to answer questions, surface relevant documentation, or generate a support ticket with the information our support team needs, without forcing users to start from scratch.

After chatting with the Compass Support Agent about an issue, the user decides to file a support ticket, and Compass automatically pre-fills the form with their conversation and relevant context.

"Compass is also the first Cresta AI Agent to support more complex customer support workflows, such as filing support tickets with attachments directly from the conversation, with seamless integration into external ticketing systems."– Di Lu, Forward Deployed Engineer

**Rethinking the navigation**

Experienced users navigate product silos with ease. New users, however, have to learn both what each product does and how workflows connect across them. For example, how does a user learn how to translate a discovery from Insights into a QM behavior, or an improvement to their AI agent?

**1. Global and local navigation**

To make those connections easier to understand, the product design team moved from a flat page structure to a system of “levels” by clarifying the spatial hierarchy: a persistent global layer for navigating the product, and a local layer for complementing focused tasks.

The previous UI limited interaction to one area at a time, while the updated UI introduces a layered navigation model with clearer visual hierarchy.

- **Global layer**: acts as the user’s map of Director. It combines existing and new navigation elements like breadcrumbs that ground users to where they are in the product, and Compass Search which is an omnipresent entry point to powerful AI features like workflow recommendations and support.
- **Local layer:**a focused workspace where users complete tasks with page-specific AI agents, such as- [AI Analyst](https://cresta.com/cresta-ai-analyst)and- [Prompt Optimizer](https://cresta.com/ai-agent-build). Here, users complete the tasks needed for workflows that solve their goals.

**2. User’s explicit and implicit needs**

Users approach AI with different levels of intent. Sometimes they know what they want - updating a scorecard for quality management, or refining a guardrail on an AI agent. Other times, they know they have a goal in mind but don’t know where to start or what they should ask to get started.

Compass is designed to support both: Compass Search helps users discover the right starting point, while Compass Support Agent provides a direct way to ask questions and complete tasks.

Compass Search (left) implicitly understands what the user wants through context and recommendations, while Compass Support Agent (right) uses the same knowledge, but handles requests explicitly stated by the user. 

- **Discovery phase:**Users don’t always know where to begin. Compass Search speeds up the discovery process by understanding our users and recommending to them the best way to achieve a goal, or surfacing options in the product they may not have heard of yet.
- **Action phase:**Once users have a plan, the Compass Support Agent acts as a companion that can guide the user through workflows, ensuring strong outcomes. Users can ask questions or receive recommendations as they progress.
- **Monitoring phase:**As users measure the impact of what they’ve built, both search and chat entry points to the Compass Support Agent work alongside each other to guide them to the right monitoring experiences, no matter if it’s surfacing relevant Insights dashboards or helping create custom monitoring solutions

**Looking ahead**

One of the most rewarding parts of this project was building Compass Support Agent with the same AI agent platform we deliver to our customers and incorporating a new set of best practices for our navigation UI. Dogfooding our own technology gave us firsthand insight into designing, evaluating, and refining AI agents for complex enterprise workflows. Every challenge we encountered became an opportunity to improve both Compass and the platform that powers it.

Building Compass reinforced our belief that AI shouldn’t be another feature bolted onto enterprise software. It should be woven into the product’s architecture and navigation. We believe this is where enterprise UX is headed. The best products won’t simply organize information - they’ll understand user intent, carry context across workflows, and help users achieve their goals frictionlessly.

P.S. A special thank you to Andrei Khlivniuk, Lavinia Petrache, Di Lu, Henry Zhang, Alex Xu, Yiming Lyu, Tanya Batsenko, Joshua Levin, Phoebe Wang, Samarth Singhal, and many others whose efforts and early explorations helped bring this project to life.
