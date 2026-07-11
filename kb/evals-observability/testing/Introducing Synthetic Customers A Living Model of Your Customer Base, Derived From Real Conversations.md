---
title: 'Introducing Synthetic Customers: A Living Model of Your Customer Base, Derived
  From Real Conversations'
topic: evals-observability
subtopic: testing
secondary_topics:
- agents/planning
summary: Introduces synthetic customers as test fixtures for agent behavior, useful
  for scenario coverage and launch readiness.
source: cresta
url: https://cresta.com/blog/introducing-synthetic-customers-a-living-model-of-your-customer-base
author: Ping Wu
published: '2026-05-28'
fetched: '2026-07-11T04:00:23Z'
classifier: codex
taxonomy_rev: 1
words: 1990
content_sha256: 63ed9e1e3edb20460e6749b2a9f9d88381a5661cbe6c42f49e33daa6a83ca0c9
---

# Introducing Synthetic Customers: A Living Model of Your Customer Base, Derived From Real Conversations

A frustrated customer calls to dispute a charge on his statement. He’s impatient and combative, interrupting the agent before she can finish a question, and threatening to cancel before she’s had a chance to respond. Minutes later, another customer calls because she wants to verify recent activity on her account. She’s calm, methodical, and asks the agent to walk her through the statement line by line.

Two customers, two different conversations, and two completely different outcomes for the business depending on how the agent, AI or human, handles each one.

This dynamic is just a microcosm of the behavior patterns happening every day across every channel, queue, and customer segment your business serves. And most companies are working from an understanding of customers that, in reality, bears only passing resemblance to how customers actually behave.

The reason is structural. Traditionally, enterprises have built customer personas from surveys, CRM records, support tickets, and periodic research. Each of those sources holds value for the business, but still only captures a sliver of information: what customers bought, what went wrong, what they said they wanted on a survey conducted six months ago. None of these measures can capture the full complexity of a customer interaction: the hesitation before asking about cancelling, the specific phrase that triggers an escalation, the emotional state they’ve brought to the call before the agent has even spoken.

These moments live in conversations; every single one is a direct, real-time signal of how customers think, what they need, how they behave under pressure, and what drives them to escalate, abandon, or stay. It’s the only data source that is fully unfiltered. Most enterprises are sitting on a gold mine of this data, but until now, haven’t had a practical and efficient way to turn that data into a living, usable representation of their customer base.

## Introducing Synthetic Customers

Today, we’re launching **Synthetic Customers**, a new capability in the Cresta platform that creates realistic, representative, and evolving customer personas directly from an enterprise’s own conversation data. Synthetic Customers analyze your business’ customer conversations, extract the behavioral patterns inside them, and produce a population of personas that reflect how your customers actually communicate, think, and feel. 


Each persona is a detailed behavioral portrait: the personality and mindset a customer brings to an interaction, the language they use, the emotions they carry, why they reach out, and how they're likely to behave when things don't go as expected. The rich data enterprises need to understand their customers on a deeper level already exists; Synthetic Customers pull it out and put it to work.

Imagine that a financial services team runs Synthetic Customers on 90 days of closed conversations in their account support queue. The system surfaces a population of personas, each one a specific behavioral profile drawn from real interactions:

![](https://cdn.prod.website-files.com/67feba4d16c14d85f1696c4f/6a17c98f8eac902ef96ff08e_blog-synthetic-custoemrs--illus-1-2.png)

These four personas represent 100% of the company’s real account support volume, and each one links back to the actual source conversations it was derived from. And critically, each persona behaves differently in a conversation: the ‘Persistent Challenger’ may interrupt, escalate, and push back; the ‘Cautious Verifier’ slows the interaction down, double-checks every detail, and won’t move forward until they feel completely secure; the ‘Efficient Transactor’ gets straight to the point; and the ‘Anxious First-Timer’ may ask the same question multiple times. These behaviors can’t be surfaced from a survey, but are present in every one of your customer conversations.

Synthetic Customers are built around three key properties.

## What Makes Synthetic Customers Different

### Realistic by design

Synthetic Customers start from your historical data; personas are grounded in real conversations, capturing the language, behaviors, emotions, and patterns that show up in actual interactions. This includes the frustration, impatience, topic-shifting, and unpredictability that are hard to model manually. A purpose-built response model then reproduces those dynamics in simulation. Cresta validates simulation realism using a blind evaluation methodology, testing whether humans and AI can distinguish synthetic conversations from real ones.

### Representative and defensible coverage

Synthetic Customers are organized into a population ranked by real traffic volume, so you can see exactly which behaviors matter most and what share of your actual customer base each persona represents.

Coverage is measurable, replacing assumptions with data-backed evidence. Each persona links back to the source conversations it was built from, so teams can inspect and validate what’s behind each profile. ‘These 12 personas represent ~82% of conversation volume’ is defensible and actionable in a way that ‘We think we’ve covered the main use cases’ simply is not.

### Evolves as your business does

Customer behavior isn’t static. New products launch, policies change, new segments emerge, and the conversations happening today look different from the ones that happened six months ago. [70% of executives](https://www.pwc.com/us/en/services/consulting/commercial-excellence/library/2025-customer-experience-survey.html) acknowledge the issues posed by this dynamic, reporting that customer expectations are evolving faster than their company can adapt. 

Synthetic Customers refresh to incorporate your most recent conversation data, so your personas reflect current behavior rather than a snapshot that’s already aging. As customer behavior shifts with the market and your business evolves, so does your understanding of the customers it serves.

## New Applications Across the Enterprise

### AI agent simulated testing

How can you know you’re testing your AI agent against the customers that it will actually encounter in production?

It’s a question more AIM teams are being forced to answer; 32% of organizations cite quality as the single largest blocker to getting AI agents into production, according to [LangChain’s 2026 State of Agent Engineering report](https://www.langchain.com/state-of-agent-engineering). Pre-launch testing built on assumptions is part of why this is such a persistent obstacle. An agent can pass every test in its suite…and still fail in production if the tests were written against a partial representation of the customer base. 

Generic LLM simulations compound the problem. A [recent arXiv preprint](https://arxiv.org/html/2604.08362v1) on LLM-based human behavior simulation found that most converge toward an overly cooperative, generic user that flattens individual differences and misses the long-tail behaviors that actually break agents in production.

Synthetic Customers solve this by grounding simulation in the behaviors your customers have actually exhibited, using a purpose-built response model that reproduces the dynamics that generic LLMs cannot. These personas integrate directly into [Cresta's AI Agent automated testing suite](https://cresta.com/blog/cresta-launches-automated-ai-agent-testing-confidence-in-every-conversation), each becoming a prompt in a Simulated Visitor test, with reusable evaluators that attach to each test case for consistent quality management across every run. Coverage estimates make it possible to answer ‘are we ready to launch?’ with a number, not intuition. As the agent evolves, the same Synthetic Customers used at initial launch become the baseline for every subsequent update, supporting continuous and cumulative regression testing as the agent updates.

The shift this represents for AI teams is significant: the time between identifying a failure and validating a fix collapses, and creates a reusable testing foundation that grows stronger with every release.

### Human agent training

The same Synthetic Customers that validate an AI agent can train a human agent. Agents can practice conversations with Synthetic Customers modeled on real customer behavior, including the frustration, impatience, and complexity that scripts and supervised role-plays rarely capture.

This changes the shape of agent training. A newer agent can spend more time practicing with the ‘Persistent Challenger’ to build the de-escalation muscle they’ll need on day one, while a more experienced agent can train specifically on the ‘Cautious Verifier’ to answer nuanced questions and ensure every detail is clear and understood without losing the customer. A team rolling out a new policy can train against personas most likely to have an issue with it, before the policy even goes live to real customers.

Because the same personas power both AI agent testing and human agent training, teams can enforce consistency between how their AI and human agents handle the same situations. The standards your AI agent is being held to in pre-launch validation are the same standards your human agents are being trained against.

### Voice of Customer (VoC) simulation

Most consequential business decisions, whether a pricing change, a new policy, or a messaging shift, get made without a reliable way of anticipating how customers will actually react. Teams ship the change, watch what happens, and adjust after the fact.

Simulated Customers change the order of operations; before a decision is finalized, teams can interact directly with specific customer segments, asking questions and pressure-testing assumptions against personas grounded in real behavior. A policy team can probe how the 'Anxious First-Timer' responds to a new claims process, catching confusion or hesitation before it shows up in production. A communications team can preview a planned outage notification with the 'Efficient Transactor,' learning whether the message lands the way it's intended or whether it's likely to trigger the exact follow-up calls it was meant to prevent. This allows teams across the organization to pressure test that a change meant to reduce friction doesn't create it for the customers least likely to tolerate it.

The result is a faster, less resource-intensive feedback loop that doesn’t require waiting for production to tell you what your customers think.

### Deeper customer analysis

Synthetic Customers also surface what's happening inside the customer base over time. Teams can see how different personas and segments behave across the customer journey: where they typically struggle, where they disengage, and how their needs shift from the moment they reach out to the moment the conversation closes, without waiting for a quarterly research cycle or a survey to come back.

Those patterns also have predictive value, and they’re drawn from a fundamentally more complete picture of the customer base than traditional research can produce. A typical customer survey reaches 3-5% of customers, and focus groups reach somehow even fewer. Synthetic Customers are derived from 100% of the conversations your business has captured. That shift — from inferring patterns from a small, self-selected sample to surfacing them from the full population — is what makes the predictive layer credible. Persona becomes an additional dimension that teams can layer onto behavioral cohort analysis: customers who had a given type of experience and belong to a specific persona behave differently from customers who had the same experience but a different behavioral profile. That makes it possible to anticipate what individual customers are likely to need next, where friction is likely to emerge, and which customers are at risk, well before the signal shows up in a survey result or a churn report.

And because these insights are tied to specific, traceable personas rather than aggregate trends, teams can act on them with precision. With visibility into 100% of conversation volume, Cresta surfaces what to prioritize next based on what’s happening across the full customer base, not just what shows up in the small slice that complains, churns, or responds to a survey. That includes getting ahead of churn before it's too late, identifying the underlying problems that drive repeat issues (a self-service flow that's quietly broken, an agent guidance gap that keeps producing escalations, a policy that's friction-inducing for one segment but not another), and routing the right fix to the right team — agent guidance, workflows, AI agent behavior, or the product itself.

## A New Foundation for Customer Understanding

Synthetic customers are poised to completely change the way that enterprises understand and test against customer behavior in 2026. Companies that accept and lean into this will make faster, more confident decisions with less real-world risk.

They’ll have the first look at what becomes possible when an enterprise has a continuously updated, behaviorally accurate model of its own customer base.

Synthetic Customers is the first capability in a broader layer of customer intelligence coming to the Cresta platform, one that turns the conversations you already have into an accurate, living model of the customers you actually serve.

Everything you need to truly know your customers is already in your conversations. Synthetic Customers help you unlock it.

[See Synthetic Customers in action - sign up for our demo webinar today!](https://na2.hubs.ly/H05MYr70)
