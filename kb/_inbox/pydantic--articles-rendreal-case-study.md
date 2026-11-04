---
title: 'Rendreal: conversational print ordering on Pydantic AI and MCP'
kind: blog
topic: null
subtopic: null
secondary_topics: []
summary: null
triage: null
skip_reason: null
source: pydantic
url: https://pydantic.dev/articles/rendreal-case-study
author: Laís Carvalho
published: '2026-10-30'
fetched: '2026-11-04T06:22:21Z'
classifier: null
taxonomy_rev: 2
words: 607
content_sha256: 26478acefe89d6e776ef4dcdcfb646bc2fc6e9c9a86de6080288a397773e385a
---

# Rendreal: conversational print ordering on Pydantic AI and MCP

Ask a general-purpose assistant for a leaflet and you get something that looks good on screen. It is not a print file, it has no price, and there is nowhere to send it. [Rendreal](https://pydantic.dev/case-studies/rendreal) closes that gap: the customer describes what they need, gets print-ready artwork and a quote, and finishes with a checkout link, without leaving the conversation.

"I can imagine the future of services without websites," says Ram Zetuny, Founder and CEO of Rendreal. "But to make it happen for printed materials, agents need Rendreal to ensure print-ready design and fulfillment."

## 

The old route runs through a printer's website. A customer works through a product configurator, then designs artwork in a browser tool, pays a designer, or uploads a file made somewhere else. Someone checks that file against the product: bleed, resolution, whether the text fits the space. When the file fails, the order waits.

Rendreal builds on experience from [Mixam](https://pydantic.dev/case-studies/mixam)'s web-to-print business, where an agent on the printer's own site already guides customers through complex specifications. Rendreal asks the next question. What if the customer never visits the printer's website at all?

## 

Vstorm, an official Pydantic implementation partner, built the system. Customers reach it through web chat, through a WhatsApp bot, or through any external assistant that connects to Rendreal's MCP server and calls its tools directly. Each channel handles its own conversation. All three share the same business services for products, designs, and orders, so a configuration means the same thing wherever the customer starts.

Behind the MCP tools sit specialist agents, one for product configuration and one for design. Vstorm orchestrated the main agent and every specialist with [Pydantic AI](https://ai.pydantic.dev/), so the whole system shares one set of typed tool definitions. The payoff lands at the last step. A print specification that reaches Rendreal's order validation is already well-formed, because Pydantic AI validated the tool arguments and structured outputs on the way through and sent malformed responses back to the model for another attempt.

The design service does the other hard part. A customer drops in assets, describes the goal, and gets a printable file for flyers, posters, business cards, postcards, or bookmarks. It can generate from a prompt, take reference material as direction, edit the current design, switch visual styles, and snapshot versions along the way.

## 

Rendreal now offers a working path from a sentence to a paid print order across three channels and five product types, with every configuration checked against the catalog before a quote is issued. Because Pydantic AI is model-agnostic, moving to a newer model does not mean rewriting the agent logic, and the evaluation set stays with the system so the same tests run again when new models ship.

Rendreal is careful about what it claims. Assistants get tool access to Rendreal's own integrated services. It is not an open network of independent supplier agents that find each other and negotiate orders. That is where the company is heading, not what it says it has today.

## 

Most products that want to be reachable from an assistant face the same shape of problem: the assistant can talk, but the business has rules the conversation cannot be allowed to break. Rendreal's answer is to expose the business as tools, keep one validated service layer behind every channel, and let typed schemas reject bad output inside the agent loop before it reaches the order system. That pattern transfers to anything with a catalog, a quote, and a checkout.

Read the [Rendreal case study](https://pydantic.dev/case-studies/rendreal), or the [full write-up on vstorm.co](https://vstorm.co/case-study/rendreal-agent-to-agent-print-ordering/?utm_source=pydantic&utm_medium=partnership&utm_campaign=rendreal). If you are building agents that other assistants can call, start with [Pydantic AI's MCP support](https://ai.pydantic.dev/mcp/client).
