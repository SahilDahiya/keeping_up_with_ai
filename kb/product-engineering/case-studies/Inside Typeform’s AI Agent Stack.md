---
title: Inside Typeform’s AI Agent Stack
topic: product-engineering
subtopic: case-studies
secondary_topics:
- agents/planning
summary: Case study of Typeform’s AI agent stack, useful for understanding production
  architecture choices in agent applications.
source: arize
url: https://arize.com/blog/inside-typeforms-ai-agent-stack/
author: David Burch
published: '2026-02-17'
fetched: '2026-07-11T04:54:47Z'
classifier: codex
taxonomy_rev: 1
words: 1021
content_sha256: fcfc9289113693c37d0582db365dbee5fd5f6bf18643f3bbe3b01a1073ad1b9a
---

# Inside Typeform’s AI Agent Stack

Typeform is building generative AI experiences to help customers create better forms faster and to make collecting insights feel more natural and useful end-to-end. In this Q&A, **Marta Lorens, Senior Data Scientist at Typeform**, shares how Typeform thinks about agentic and gen-AI use cases, why evaluation is a core part of the product experience, and what they’ve had to build to make AI reliable in production.

## What are your agent and gen-AI use cases?

**Marta Lorens:** At Typeform, we have plenty of generative AI use cases, and they span across three pillars. We have **Creator AI**, which helps users create their forms and flows.

We have **Interaction AI**, which improves the respondent experience with more natural interactions. And we have **Insight AI**, which helps users get insights from responses and extract patterns.

I mostly focus on Typeform AI for creators—where we let users describe their goal in natural language, and we generate a structured form in seconds for them, with the best question types, the copy, and the logic across different question flows.

The goal is that we create high-performing forms in minutes for our users. They don’t have to struggle with that, and they can spend time focusing on the insights and decisions that truly matter to them.

## Who is your primary cloud provider and how do they fit into your AI strategy?

**Marta Lorens:** Our primary cloud provider is [AWS](https://arize.com/partners/aws/), and they play an important role in our strategy because they provide scalable infrastructure, managed services, and reliability for running our models. Their platform allows us to focus on building the AI experiences and orchestration layers—we don’t have to manage infrastructure.

## What’s the most non-obvious lesson you’ve learned since launch?

**Marta Lorens:** One of the lessons since launching Typeform AI is that **evaluation is an ongoing task**—it’s not a one-off.

We learned that evaluation can quickly become obsolete in fast-evolving applications. Our takeaway is that evaluation is part of the product experience, so you have to revisit it continuously as your feature evolves.

Otherwise, you end up with metrics that look good on paper but quickly stop reflecting real value in production.

## Which capabilities did you have to build or harden yourselves?

**Marta Lorens:** There were several capabilities we had to build ourselves to make AI genuinely useful.

First, turning a user request into a structured form requires its own AI system, integrated with our internal services.

We also built **layers of safeguards**, so customers can use AI confidently and we respect privacy and compliance.

Of course, we built **evaluation pipelines**, because we want to continuously improve behavior.

And traditional product analytics is not enough for AI applications—so we needed to track detailed traces of AI calls: generations, latency, failures, and whether AI actually helped users complete their tasks. These are capabilities where **Arize** was definitely very useful.

## Why are evals so important and what is your approach?

**Marta Lorens:** Evaluation is critical because without it, decisions are driven by intuition rather than evidence.

We don’t want subjective impressions, because they can’t really tell you if your feature is working. Without evaluation, you risk hallucinations, irrelevant outputs, mismatches, and negative impact on user trust.

Our approach is about measuring behavior across many cases and **turning subjective feedback into objective signals**. We track outputs, user interactions, and outcomes to verify AI-generated forms meet our expectations.

Good evaluation impacts everyone: customers get higher quality results and more relevant AI responses; teams building AI gain visibility into quality and reliability; and Typeform benefits from stronger user trust, engagement, and scalable, responsible AI features.

## One trend we see is non-engineer subject-matter experts getting more involved in evals and prompt optimization – are you seeing that, and how do you manage it?

**Marta Lorens:** Yes, we are definitely seeing that trend.

At Typeform, we treat evaluations as part of the product itself—not just a back-end task. PMs, engineers, designers—everyone collaborates on what “good” looks like.

Everyone contributes examples and helps shape test sets. This collaboration improves evaluation a lot because it brings diverse perspectives, helps uncover blind spots, and ensures outputs align with user needs, product goals, and brand standards—while keeping the process measurable.

## What does the “agent engineer” role look like there — skills, interfaces owned, and decision rights?

**Marta Lorens:** An agent engineer is involved end-to-end in AI feature development—from ideation to execution.

They collaborate closely with PMs, designers, and engineers to make sure the AI-driven product is technically feasible and delivers a great UX.

They build and orchestrate the AI logic, define interfaces, guardrails, and integrations, and have decision rights around technical trade-offs—system behavior and evaluation—so the feature is reliable and aligns with the product vision.

## If starting from scratch today, what would you build first—and what would you avoid—to reach production faster?

**Marta Lorens:** One of my favorite AI practitioners points out that the fastest teams are those that maintain a disciplined approach to evaluation and error analysis—and I’ve found that to be true.

If I were starting from scratch today, I would focus on **small, targeted evaluation first** in any application. With just a few test cases, you can see patterns, uncover key issues, and iterate quickly.

At the same time, I would avoid overbuilding and trying to handle every edge case at the beginning—that adds complexity and delays learning before you actually know what creates value.

## How do you work with Arize AX / why did you select Arize AX? Any early findings/successes?

**Marta Lorens:** At Typeform, we ran extensive research and a proof-of-concept phase where we evaluated multiple LLM evaluation and observability frameworks, and we collectively decided that **Arize** was the best fit for our needs.

One key reason was that it was very easy to set up and customize, which was crucial for us because we have specific evaluation requirements.

It also meets our enterprise needs—security, compliance, and ongoing support.

On top of that, the Arize team supporting our onboarding was fantastic. They helped us set everything up quickly, guided us on best practices, were always eager to answer our questions, and the collaboration was a pleasure.
