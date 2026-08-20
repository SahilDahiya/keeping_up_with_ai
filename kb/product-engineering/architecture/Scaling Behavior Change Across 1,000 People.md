---
title: Scaling Behavior Change Across 1,000 People
kind: blog
topic: product-engineering
subtopic: architecture
secondary_topics:
- inference/optimization
summary: Cresta's Behavioral Engine runs BERT, GPT-2 and T5 models over 40,000 live
  chats a day to detect decision points (price objections, package questions) and
  fire real-time coaching hints. Reports scaling hint volume 5x while cutting cost
  per hint, over 2 million hints delivered, and per-chat rather than sampled analytics.
triage: null
skip_reason: null
source: cresta
url: https://cresta.com/blog/scaling-behavior-change
author: Lars Mennen
published: '2021-03-16'
fetched: '2026-08-20T06:14:29Z'
classifier: claude
taxonomy_rev: 2
words: 613
content_sha256: f13d48b17c39693675f6c3921d688c16efebe761c0ce337ace6f5064b8a1944c
---

# Scaling Behavior Change Across 1,000 People

*"Run a mile in under 6 minutes.""Meditate once a day.""Eat avocado toast every morning."*These are some of the responses when we asked engineers at Cresta about their goals. However, adopting new habits is challenging, even when we know it's the right thing to do.The same challenge applies to the 3.4 million contact center agents in the United States. Zooming into the floor of a contact center, we meet Bob, an agent helping customers find the right internet service at [Cox](https://cresta.com/customers/cox/). Bob's goals include *"Increase my conversion rate"* and *"Make customers happy."*He takes around 100 chats a day, and sometimes he brings the deal home, but other times the customer leaves the chat — often for reasons he doesn't know. How can we help Bob better guide customers to the right solutions and increase his conversion rate?Enter Cresta's **Behavioral Engine**, a machine learning system that drives behavior change at scale. Combining state-of-the-art machine learning models, cognitive psychology, and human-centered coaching, the Behavioral Engine helps contact center agents grow into experts with every chat they take. The 2-part system, described below, not only helps an agent like Bob achieve his goals, but ultimately drives success for his manager and company.

Today, Cresta powers thousands of agents handling over 40,000 chats every day. To provide custom coaching tailored to every agent, our machine learning models (BERT, GPT-2, and T5) diligently observe each chat in real-time and determine the best thing to do at any given moment.During key moments that shape the trajectory of a conversation — for example, a customer asking about the right package for their needs, or objecting to the price of a service — Cresta's Behavioral Engine steps in and guides agents with best practices to handle these critical moments.**Hints** prompt agents to seize an opportunity and positive feedback reinforces the learning when the behavior is performed. Over time, agents learn to ask the right discovery questions and address objections with empathy and ease.In the past year, by advancing our AI models, we have scaled the volume of hints by a factor of 5, while simultaneously reducing cost per hint. As of today, we have sent over **2 million hints** — providing agents with 2 million custom coaching touchpoints for their personalized growth.Agent Progression: a comprehensive analytics engine that tracks the behaviors performed in every chat. With progression, it's simple to drill into a particular agent or particular behavior and see progress over time. Access to these insights allows agents to understand their personal improvement and prompts growth-oriented conversations with their managers.Our latest edition of Agent Progression is powered by our AI models at every turn. Previously, we provided insights on a sample of chats per agent. Now, insights are available on every chat an agent takes. With our current volume of 40,000 chats per day, this means over 40,000 insights are aggregated into a few key metrics for agents and their managers.Additionally, we introduce an hourly view to complement the standard weekly view. As our AI models generate insights dynamically, managers can see real-time data on the behaviors agents exhibit at any given moment.Measurable ResultsTo date, Cresta's Behavior Engine has driven the adoption of hundreds of expert behaviors across thousands of agents in diverse domains (including telecom, retail, and software), resulting in measurable value for our customers, ranging from 12% revenue growth to 19.1% increase in NPS (for more, see [case studies](https://cresta.com/resources/case-study/cox)).Behavior change is challenging, whether you're an agent trying to adopt an expert behavior or just someone trying to eat avocado toast every morning. With Cresta, it can be visible, measurable, and scalable.*To empower your contact center with Cresta,* *get started today.**If these problems sound interesting to you, we are* *hiring**!*
