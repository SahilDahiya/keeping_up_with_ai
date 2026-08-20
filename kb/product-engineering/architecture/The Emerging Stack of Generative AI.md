---
title: The Emerging Stack of Generative AI
kind: blog
topic: product-engineering
subtopic: architecture
secondary_topics:
- prompt-engineering/techniques
- agents/tool-use
summary: Lays out the LLM != AI System != AI Product distinction with a worked example
  chaining several GPT-4 calls (name extraction, scoring, recommendation) against
  a Salesforce CRM lookup and purchase history as real-time context. Argues for vertically
  integrated stacks where UI feedback propagates backwards into knowledge, system,
  and eventually RLHF on the model itself.
triage: null
skip_reason: null
source: cresta
url: https://cresta.com/blog/the-emerging-stack-of-generative-ai
author: Tim Shi
published: '2023-05-04'
fetched: '2026-08-20T06:15:05Z'
classifier: claude
taxonomy_rev: 2
words: 1195
content_sha256: b3a06c74bf011895841b5786846af894f487b5d8e3adaa47a13502fb3190a806
---

# The Emerging Stack of Generative AI

Remember "Intel Inside"? At the heart of modern-day computing lies the microprocessor, a fact that Intel astutely capitalized on with its memorable catchphrase. In a similar vein, large language models (LLM) serve not only as the figurative "microprocessor" for AI-centric enterprise applications, but also as the catalyst for the buzz surrounding the GPT phenomenon.

![Intel Inside](https://cdn.prod.website-files.com/67feba4d16c14d85f1696c4f/68138f51878c77f17d08f6bf_68135f3d2769050dc2267948_blog-intel-inside.avif)

SupportGPT, MedicalGPT, ThreatGPT… "thin-wrapper" apps are being built upon ChatGPT and introduced to the world every single day. These solutions offer a thin layer of software tailored to specific tasks while leveraging the generic language model. Is this going to be the new paradigm of computing? Or is this merely an economical means of demo and hype?In this article, we aim to shed light on the recent advancements in generative AI and provide a view of how the future AI technology stack will unfold. We think:

- **“A PC is more than its microprocessor”** . Comprehensive and intricate AI systems will build on top of multiple LLM in conjunction with private data connectors, API integrations, end user workflows, etc.
- **“An Apple is better than a PC”** . A vertically integrated product stack is more advantageous for the development of high-value enterprise applications.

### LLM ≠ AI System ≠ AI Product

First we’ll dive into our thoughts around the emerging technology stack of LLM. Let’s start with the difference between LLMs, AI System and AI Products.Large language models have defined a new paradigm of computing. A set of new capabilities began to emerge as people started training larger and more powerful language models. One such capability is tuning the model to follow instructions.

In this example, LLM will follow the instruction and classify the message as “Yes, name is John”. In other words, we could build a name extractor by feeding the prompt with different message inputs. Starting from here, we could even come up with instructions for different natural language tasks, such as intent detection, PII redaction, summarization, etc. These all become components of an AI system, while we are leveraging the same underlying LLM as the “core microprocessor” to follow different “instructions” to perform tasks. This is the paradigm of “prompt engineering”.

### From LLM to AI Systems

Now with prompt engineering, we see that LLM can perform specialized tasks through following instructions. To build a powerful AI system, however, multiple LLM are often chained together along with specialized AI components to deliver the most value.Let’s go back to the name extraction example. Suppose we want to build an AI system to determine if the customer qualifies for Halloween promotions and make recommendations based on his preferences.

1. Extract customer’s name using the LLM and the instruction shown above.
2. Using the name to do a CRM lookup, such as Salesforce.
3. Pull customer’s purchase history as realtime context.
4. Use specialized AI system for scoring and qualifying the customer for promotions.
5. If customer qualifies, combine customer profile and promotion information into another LLM for final recommendation.

In this example, we can make a few observations. First, the LLM (“the microprocessor”) is called multiple times with different instructions. Each instruction led to a specialized AI component: one for name extraction and one for final recommendation.Second, a specialized AI system might still be used in addition to the LLM to combine multiple information features about the customer to determine the best promotion.And most importantly, connecting to private data and/or integrating with APIs brings true power for enterprise applications. Most LLM are trained on primarily public data, it has no knowledge or expertise about your company. For example, it won't know your latest competitive positioning or have access to the competitive battle card your salespeople rely on to differentiate their offering with customers. Here, we rely on CRM to pull the latest customer information and use it in real time for the final recommendation. We hooked up our “microprocessor” with an “external memory”.

### From AI Systems to AI Products

As we see, an AI system becomes truly powerful when it knows about your company and can further optimize its components. One might wonder where the wealth of knowledge and proficiency stems from. At [Cresta](https://cresta.com/), we believe that AI systems will learn from human experts in your domain.By adding the human element, AI systems evolve into AI products. Enterprise leaders will re-design workflows around generative AI. Just like you equip your best sales agents with competitive battle cards, there will be a set of steps to edit and improve the AI system deployed for the contact center.For example, our [insights product](https://cresta.com/product/insights/), which also leverages LLM, helps you discover such expertise. We can not only detect which customer messages are having objections, but also visualize objections happening across millions of conversations. Managers are able to look at each type of objection, and, in one step further, understand what top agents are doing differently to overcome objections and achieve better outcomes. They can make those insights actionable through real-time agent coaching or automated [virtual agents](https://cresta.com/product/virtual-agent/).As we can see, a new tech stack for AI-first products is emerging around LLM. LLM like GPT-4 are the core of the stack and AI systems can be built to leverage multiple AI components to drive value. Ultimately, workflows are built around these systems to help consolidate expertise and improve the system.

### Vertically Integrated Stack

Prompt engineering might be a quick way to build demos. But there are limitations such as accuracy for complex tasks, latency for real-time applications, and cost for running at scale. In particular, once an AI system rolls out to production, what if a name extraction is missed for PII redaction, or an important type of objection is left undiscovered? Enterprise AI systems need to learn from user feedback.To create a feedback loop to improve the system, we would start with the end user workflow. For example, building feedback mechanisms into the user interface and collecting feedback data.Next, we can take the feedback and improve the underlying knowledge and expertise leveraged by LLM. For example, using LLM to discover potential new types of objections and write battle cards for your sales team.Finally, we can even improve the underlying LLM model through human feedback. Just like how Reinforcement Learning from Human Feedback (RLHF) made ChatGPT really good at consumer conversations, we think RLHF on enterprise data would unlock LLMs’ true potential.By creating a vertically integrated stack, we can effectively propagate feedback data backwards and continuously improve the LLM, AI System, and finally the AI product. The more your product is used the better and faster it gets, becoming a true expert AGI for your domain.

### Conclusion

We envision a future where the AI realm ushers in numerous AI “super apps”. Rather than being superficial containers for large language models (LLM), these advanced AI systems will boast domain-specific expertise and seamless integration with customer systems. Such applications will likely be vertically integrated, utilizing user feedback data to perpetually enhance their knowledge, proficiency, and the LLM at their core. While "GPT-inside" may still come to mind occasionally, much like how we reminisce about “Intel-inside” CPUs, the true delight for its users will stem from an exquisitely crafted and robustly engineered "Personal Computer."
