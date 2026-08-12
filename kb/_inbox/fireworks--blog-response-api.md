---
title: 'Unlock Your Tools: Fireworks Adds OpenAI-Response API with MCP Support (Beta)'
kind: blog
topic: null
subtopic: null
secondary_topics: []
summary: null
triage: null
skip_reason: null
source: fireworks
url: https://fireworks.ai/blog/response-api
author: null
published: '2025-06-22'
fetched: '2026-08-12T06:28:53Z'
classifier: null
taxonomy_rev: 2
words: 777
content_sha256: 086336dfe9bc37672aa33a04ed1121e625518cd1db1ca3b0480bd4eaf1d450b2
---

# Unlock Your Tools: Fireworks Adds OpenAI-Response API with MCP Support (Beta)

**TL;DR:** Fireworks now supports an OpenAI-response API endpoint that allows you to connect our library of leading open models to your own tools and data using the open **Model Context Protocol (MCP)**.

Large Language Models are incredibly powerful, but out of the box, they exist in a vacuum. They can't check your inventory, update a customer's order, or query your internal database. To make them truly useful for your business, they need to securely interact with your proprietary APIs, tools, and data sources.

Historically, this required developers to build complex, brittle "glue code." You'd have to orchestrate a multi-step dance: prompt the model, parse its output to see if it wants to use a tool, make the API call yourself, and then feed the result back to the model. This process is slow, error-prone, and a significant engineering bottleneck that stifles rapid product development.

We're thrilled to announce a powerful new capability to solve this challenge: **Fireworks now supports an OpenAI-compatible Responses API, with first-class support for the Model Context Protocol (MCP).**

MCP is an open protocol that standardizes how applications provide context and expose tools to LLMs. Think of it as a universal adapter, creating a seamless and secure bridge between a language model and any external system. Instead of being locked into a proprietary set of tools, you can now connect any model on Fireworks to any tool you build, as long as it speaks MCP.

This new endpoint handles the entire agentic loop—reasoning, tool selection, and execution—server-side, allowing you to build sophisticated applications with a single, elegant API call.

Bringing an open protocol like MCP to our platform helps developers on Fireworks to:

- •**Connect Any Open Model to Your Tools:** Take state-of-the-art open models like**Qwen 3, DeepSeek or Llama 4** and connect them directly to your business logic. Empower a Llama model to interact with your Shopify store, or have Qwen query your internal Jira instance. State will also be managed on the Fireworks server side, so you don’t have to worry about managing a long conversation with LLMs with chat completion API anymore.
- •**Break Free from Vendor Lock-in:** MCP is an open standard. The MCP server you build for your tools is portable. You’re not tied to a single model provider’s ecosystem. This gives you the freedom to choose the best model for the job, today and tomorrow, without rebuilding your tool integrations.
- •**Supercharge Your Custom Models:** The possibilities are explosive when you combine this with custom models. Use our [Supervised Fine-Tuning V2](https://fireworks.ai/blog/supervised-finetuning-v2) and[Reinforcement Fine-Tuning](https://fireworks.ai/blog/reinforcement-fine-tuning) to train a model that understands your company’s unique terminology, and then give it access to your internal tools via MCP. This creates a hyper-specialized and immensely capable agent.

Integrating your tools is now stunningly simple. You just need to tell the model the location of your MCP server. The model will then be able to discover and call the tools it provides.

Here’s a quick example of how you can get **qwen3-235b-a22b** to answer up-to-date questions about our latest open source project **reward-kit** that was released only last week and hence is not in the model’s training data. All you need is to add the **gitmcp** server in the request:

12345678910111213141516171819202122

1234567891011121314

Behind the scenes, the model identified the user's intent, discovered the tool for fetching GitHub repo documentation via an MCP server, called it with the correct parameters, and used the result to formulate its final response...all in one API call!

This unlocks a new class of applications built on open models:

- •**E-commerce Automation:** Build agents that check inventory, process returns, or apply discount codes by connecting directly to your Stripe, Shopify, or custom e-commerce backend.
- •**Internal Operations Bots:** Create a Slack bot that can file bug reports in Jira, create pages in Confluence, or query your internal HR systems, all through a secure, company-specific MCP server.
- •**Data-Driven Assistants:** Connect a model to your company's databases and data warehouses via an MCP interface. Allow your business teams to ask natural language questions like, "What were our top 10 selling products in Europe last quarter?"

The future of AI is not just about better models; it's about better-connected models. By embracing open standards like MCP, we're giving you the power to integrate the best open-source AI deeply into your own products and workflows.

- •[Dive into our API documentation to learn more.](https://docs.fireworks.ai/api-reference/post-responses)
- •[Learn how to build your own MCP server with this guide from Cloudflare.](https://developers.cloudflare.com/agents/guides/remote-mcp-server/)
- •[Explore compatible models in our Model Library.](https://app.fireworks.ai/models)

We can't wait to see what you build. Note that this is a preview feature from Fireworks, we would love to hear your feedback.

**Start building today!**
