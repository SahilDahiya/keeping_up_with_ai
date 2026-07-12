---
title: The Agent Development Life Cycle
topic: agents
subtopic: planning
secondary_topics:
- evals-observability/evaluation
summary: Defines an agent development lifecycle from design and simulation through
  evaluation, deployment, monitoring, and continuous improvement.
source: sierra
url: https://sierra.ai/blog/agent-development-life-cycle
author: Clay Bavor; Bret Taylor
published: '2026-05-12'
fetched: '2026-07-11T03:53:55Z'
classifier: codex
taxonomy_rev: 1
words: 1672
content_sha256: 4fed47f91f0937002631da53b3e41a794b08c64b615996e25f89a30066414048
---

# The Agent Development Life Cycle

# The Agent Development Life Cycle

Over the past few decades, [software has eaten the world](https://a16z.com/why-software-is-eating-the-world/) as the world’s economy has digitized. As the world has come to run on software, engineers have developed a shared methodology to make software more robust called the [software development lifecycle (SDLC)](https://aws.amazon.com/what-is/sdlc/). The standard SDLC represents all the hard-won best practices we’ve collectively developed to ensure the software we use is reliable, functional, and trustworthy.

[AI agents](https://sierra.ai/blog/ai-agents-guide) break all the rules we’ve come to expect from software – and they’ve broken the typical software development life cycle in the process.

Traditional software is written in a programming language that is rule-based and deterministic, so the same input reliably produces the same output. Agents, in contrast, often include [Large Language Model (LLM) prompts written in English](https://en.wikipedia.org/wiki/Prompt_engineering), and are goal-based and non-deterministic, producing dramatically different results with even modest changes to input.

Traditional software collects user input in a structured manner through forms, fields, touchscreens and keyboards. Agents typically communicate through natural language – both text and voice – producing a nearly infinite number of possible interactions that need to be accounted for by agent developers.

Traditional software is extremely fast and inexpensive thanks to the past few decades of [Moore’s law](https://en.wikipedia.org/wiki/Moore%27s_law). You can deliver over 10 million page views from your website on [Amazon Web Services](https://aws.amazon.com/cloudfront/pricing/) for free, served to users around the world within milliseconds. Agents, on the other hand, depend on LLMs that are often slow and orders of magnitude more expensive than traditional software due to model inference costs. If each of those 10 million page views invoked GPT-4, your OpenAI bill could easily exceed hundreds of thousands of dollars – and each page view would take multiple seconds to render.

When your traditional software vendor releases an upgrade, you can reasonably expect that your software will continue to work with few if any changes. In contrast, when an upgrade is available to one of the LLMs on which you’ve built your AI agent, all bets are off. Prompts designed for one model rarely produce the same results on a more powerful model, and if you’ve fine-tuned the model with your own proprietary data, you’ll need to start the training and evaluation process over from scratch.

We’ve moved from a world of rule-based, deterministic, fast, cheap, and rigid software with well-understood dependencies and upgrade processes to a world of goal-based, non-deterministic, slow, expensive, and flexible software with absolutely no change management process for upgrades. How in the world do we make our AI agents reliable? And how can we make agents future-proof so they can benefit from the billions of dollars in investment from foundation model providers like OpenAI, Microsoft, and Google?

A new kind of software demands a new approach to development. At Sierra, we’ve built industrial grade AI agents for consumer brands like Sonos, WeightWatchers, and SiriusXM, serving millions of consumers every month. With [Agent OS](https://sierra.ai/product/agent-sdk), we’ve developed a unique agent development lifecycle to enable Sierra agents to be reliable, testable, and incredibly capable.

This post captures the lessons we’ve learned along the way. It’s designed for a technical audience, for those engineers who are building AI agents at their own companies, either [on the Sierra platform](https://sierra.ai/) or elsewhere. We hope you find these lessons as useful as we have.

**Development: Declarative goals and guardrails**

Computers have traditionally enabled automation by rapidly and reliably executing the rules defined by software developers. With the reasoning capabilities of large language models, software can solve problems in creative ways that are not predefined by the developer.

To take advantage of these reasoning capabilities, developers can train custom models, [fine-tune](https://en.wikipedia.org/wiki/Fine-tuning_(deep_learning)) an open source model, or [prompt engineer](https://en.wikipedia.org/wiki/Prompt_engineering) one of widely available foundation models. Properly constructed, a specialized model with a well-constructed prompt enables sophisticated reasoning: What caused the spike in sales last quarter? Of the three products available, which would best satisfy the user’s needs?

The problem with many LLM-based applications is their non-determinism. 90% of the time, they’re magical. 10% of the time, they [hallucinate](https://en.wikipedia.org/wiki/Hallucination_(artificial_intelligence)) and go haywire – [making up airfares](https://www.bbc.com/travel/article/20240222-air-canada-chatbot-misinformation-what-travellers-should-know) or even [making up case law](https://www.nytimes.com/2023/05/27/nyregion/avianca-airline-lawsuit-chatgpt.html).

How can we get the power and flexibility of agents without the (sometimes catastrophic) downsides? Our solution is the Sierra Agent SDK.

The Sierra Agent SDK enables developers to use a declarative programming language to build powerful, flexible agents using composable skills to express procedural knowledge – the way things should be done.

This declarative model enables developers to not only express the goals they want their agent to achieve (e.g., *help the customer return an order*), but also deterministic guardrails that the agent cannot cross (e.g., *orders can only be returned within 30 days of purchase*). Agents built on Sierra are creative, but in the moments that matter, like processing an order or upgrading a plan, deterministic safeguards ensure that your business logic is strictly and deterministically enforced.

The Sierra Agent SDK enables developers to declare the behaviors they want to see from the agent in a way that is abstracted from the underlying LLMs. This enables Sierra customers to build incredibly complex agents that are both maintainable and composable – avoiding the inscrutable, almost impossibly complex workflows of agents built on prompt engineering. And when new models become available, like [GPT-4o](https://openai.com/index/hello-gpt-4o/), agents can benefit from these upgrades without code changes.

**Release: Immutable agent snapshots**

Modern software teams define their [infrastructure as code](https://en.wikipedia.org/wiki/Infrastructure_as_code), storing their software and hardware provisioning in source control, so that an entire application – from the servers to the database to the business logic itself – is defined atomically. This approach enables modern software teams to easily expand capacity with demand, and perhaps most importantly, is one of the key mechanisms that makes it possible to roll back software systems when something goes wrong.

AI agent behavior is defined by a number of new types of dependencies in addition to traditional source code, including foundation models versions, knowledge bases to power [retrieval-augmented generation](https://en.wikipedia.org/wiki/Prompt_engineering#Retrieval-augmented_generation), and prompts.

Sierra’s Agent OS enables developers to package agent releases to include all these dependencies atomically. Like software built with infrastructure as code, each agent release is a snapshot that includes not only the underlying source code and prompts, but model version dependencies and an immutable snapshot of all of the knowledge available to the agent.

Immutable agent releases enable Sierra customers to roll back agent behavior instantly if necessary. Agent releases also enable powerful new forms of experimentation, including A/B testing multiple releases to measure new agent behaviors against business goals.

**Quality assurance: Continuous, structured human feedback**

Live conversational AI agents can conduct thousands or even millions of conversations every week. To continuously improve these agents, we need to continuously evaluate their performance and directly incorporate that feedback into agent behavior.

Evaluating a conversation is rarely a technical task. Knowing whether an AI agent behaved correctly requires a subject matter expert that knows the rules of the road of your business, like a customer experience or sales manager.

To facilitate continuous quality assurance, the Sierra platform includes the Experience Manager, a sophisticated platform for auditing conversations that is accessible to technical and non-technical users alike. Using the Experience Manager, customer experience teams formally evaluate samples of conversations every single day, annotating the conversations with feedback. Did the AI agent make the correct decision? Did the AI agent use the correct language and tone? Was the agent missing the knowledge it needed to answer a question? If a decision was incorrect, what should the agent have done?

These annotated conversations form the basis for agent improvement. Because the agent is built with the Agent SDK, we know the trace of reasoning behind every agent decision, enabling the platform to precisely identify why an agent may have misbehaved. Because every issue annotates a conversation, developers can quickly and easily simulate the conversations that have produced issues, enabling a broad spectrum of developer tools to rapidly deploy agent improvements.

More importantly, these annotated conversations become the basis for the agent’s regression tests – ensuring that your AI agent never makes the same mistake twice.

**Testing: Regression tests for conversations**

[Integration testing](https://en.wikipedia.org/wiki/Integration_testing) is a notoriously hard problem for complex software systems, but it is even harder with conversational AI because of the non-deterministic nature of underlying language models. Making subtle changes to models or prompts that fix one problem can easily break previous solutions, leading to a game of prompt engineering whack-a-mole and very frustrated customers.

Agent OS provides agent testing natively with conversation simulation.

Every annotated conversation in the Experience Manager can become a conversation test – a snapshot of the conversation that is simulated against mock APIs to reliably reproduce the problem. As customer experience teams annotate thousands of conversations, developers are provided with thousands of conversation tests that can be run in parallel during development and prior to every agent release, creating a virtuous cycle of agent quality.

These tests enable [test-driven-development](https://en.wikipedia.org/wiki/Test-driven_development) for agent developers creating an agent, and the entire test suite becomes a robust regression test suite to validate agent releases.

When Sierra upgrades the underlying Agent OS platform, we not only run internal evaluations to judge quality, but also run the regression test suite for every one of our live customers to ensure our platform upgrades do not regress behaviors in our customers’ agents.

**The future of agent development**

If it feels like we’re in the very early days of AI agent development, it’s because we are. We’re in uncharted territory. Sophisticated LLM-based agents simply weren’t available much more than a year ago, and neither were the methods and tools for developing and testing them. It’s a bit like it’s 1996, the Internet exists, and people are building web sites and early web applications, but there’s no [LAMP stack](https://en.wikipedia.org/wiki/LAMP_(software_bundle)). At Sierra, we're not only building industrial-grade agents for our customers, but also inventing new tools and processes to build agents that are more reliable, scalable and maintainable.

If you’re interested in building an agent for your company with Sierra, we’d love to [work with you](https://sierra.ai/learn-more).
