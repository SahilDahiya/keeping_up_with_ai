---
title: Introducing Baseten Hosted Tools
kind: blog
topic: agents
subtopic: harness
secondary_topics:
- inference/serving
summary: Baseten's new Hosted Tools run the agentic tool-use loop server-side, co-located
  with model inference, instead of round-tripping through the client; the company
  reports a 15% end-to-end latency reduction versus client-side tool loops and launches
  web search with Exa, Keenable, Parallel, and You.com as the first hosted tool.
triage: null
skip_reason: null
source: baseten
url: https://www.baseten.co/blog/introducing-baseten-hosted-tools/
author: Sai Maddali; Marius Killinger; Marylise Tauzia
published: '2026-09-16'
fetched: '2026-09-17T06:10:21Z'
classifier: claude
taxonomy_rev: 2
words: 1441
content_sha256: b91c5390c2779945e8137415b2b84cfe8319e5e6689f4457bf319cff0b701827
---

# Introducing Baseten Hosted Tools

![Baseten hosted tools](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1789514403-baseten-hosted-tools_blog.png%3Fauto%3Dformat%26fit%3Dcrop%26h%3D630%26w%3D1200&w=3840&q=100)

Today we’re introducing Baseten Hosted Tools, a new ecosystem for capabilities like web search, code execution in sandboxes, browser use and automation, and more to enhance models and agents running on Baseten. The first category of tools we are introducing is Web Search, and we are excited to launch it today with Exa, Keenable, Parallel, and You.com, bringing their search technologies into the Baseten platform with a consistent developer experience.

Until now, developers building apps and agents with open-source models had to assemble one tool at a time. While MCP provides unification to some degree, developers still need to handle the ReAct loop, task coordination, model steering, and eager or concurrent dispatch - all adding implementation complexity. As an application gains more capabilities, this integration work quickly becomes part of the product’s critical path.

Baseten Hosted Tools makes that layer a simple config change, robust and low latency.

## **Baseten Grounded Inference**

Our first Baseten Hosted Tool is web search: *Baseten Grounded Inference*.

Baseten Grounded Inference gives models hosted on Baseten access to information that is as recent as the current day, specific, and absent from their training data. It unlocks product experiences that are difficult to build with a model alone: researching a company before a sales call, comparing current products and prices, investigating a developing event, finding recent technical documentation - generally grounding an answer in the entire knowledge base of the web.

Web search runs inside the [Baseten Inference Stack](https://www.baseten.co/resources/guide/the-baseten-inference-stack/) and can be enabled by adding the name of our hosted search tools as config to a standard Messages, Chat Completions, or Responses request.

![Web search experience with open souce models on Baseten](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fimage.mux.com%2FzVRCDWliEPH33kE005vdaRkq7OriFlexX%2Fthumbnail.jpg&w=3840&q=75)

The model decides whether a prompt needs web search based on its native tool use capability and may execute multiple iterations until it is confident. Via the system prompt and a configurable budget for iterations the behavior can be customized to the desired set point: ranging from one-shot to deep research agent.

Baseten interleaves model inference and search requests in server-side a loop, while streaming tool-use and tool-result blocks as live progress to your client which you can use for progress display. Eventually the model produces a grounded response.

A simple example of a grounded inference request looks like this:

```
1curl https://inference.baseten.co/v1/messages \
2  -H "Authorization: Bearer $BASETEN_API_KEY" \
3  -H "Content-Type: application/json" \
4  -H "x-baseten-server-tools: true" \
5  -d '{
6    "model": "zai-org/GLM-5.3-Fast",
7    "max_tokens": 1200,
8    "messages": [{"role": "user", "content": "What are latest news about Baseten?"}],
9    "tools": [{"type": "baseten__<INSERT_PROVIDER>__web_search"}],
10    "baseten": {"tool_settings": {"max_react_iterations": 5}}
11  }'
```
- Tool selection and header are required.
- ` `` baseten.tool_settings` `` is optional.
- Works for `` `ChatCompletions` `` ,`` `Messages` `` and`` `Responses` `` in streaming and buffered mode.
- `<INSERT_PROVIDER>` must be replaced before the script can be run.

## **Launching with Exa, Keenable, Parallel and You.com**

Great tools require deep specialization. That’s why we’re building Baseten Hosted Tools as an ecosystem, starting with partners who have invested deeply in making the web useful to AI applications.

At launch we offer access to 4 leading web search providers, listed below in alphabetical order in their own words:

[**Exa**](https://exa.ai/) gives your AI agent access to 100B+ websites, docs, papers, people, companies, news, and much more. From there, your agent can search the web in real time, read relevant pages, and answer with up-to-date sources. It's a token efficient way to search the web. Loved by 500k+ developers and companies. Exa powers search for Cursor, Vercel, Lovable, HubSpot, Clay, CodeRabbit, and more.

[**Keenable**](https://keenable.ai/?utm_source=google&utm_medium=cpc&utm_campaign=Search_US_eng_ALL_Brand_ImpShare_fww&gad_source=1&gad_campaignid=24026138874&gbraid=0AAAABEAf7ubY-CznO0drb-WIeFDx4v7W0&gclid=CjwKCAjwtp7VBhBjEiwAJfpV-3FbxYdd4gWmHA6tANXhWDxzbkPubKo3b7FXpmKGn5xhDunZGBmGPxoCuHUQAvD_BwE) provides independent web search infrastructure for AI labs and agents, powered by its own index of 100B+ web documents updated in real time to surface the latest content. It delivers state-of-the-art quality on agentic benchmarks. Latency is sub-250 ms p95 in US East, at $4 per 1,000 requests. Designed for high-volume low-latency inference, agentic workloads or reinforcement learning and data generation at scale.

[**Parallel Web Systems**](https://parallel.ai/) provides web infrastructure for AI agents, powering agentic web research at companies like Notion, Harvey, Granola, Hex, and Dropbox. Its Search and Extract APIs are designed to match the intelligence and cost of open-source models, retrieving relevant web information and delivering it in a format models can use directly, so agents spend fewer tokens discovering, scraping, and processing pages.

[**You.com**](http://you.com/) delivers enterprise-grade web search APIs built for AI agents. Running on an independently crawled index, they serve 1B+ queries per month for global enterprises, frontier labs, and AI-native companies broadly. Their search APIs are built for both accuracy and speed. Highlights, their extraction mode, delivers citable, token-efficient context to downstream LLMs, keeping costs per task low, especially when paired with Baseten open-weight models. The same API scales from prototype to ZDR-compliant, high-QPS production without re-architecting your stack.

Each partner brings a different approach, and making them available through Baseten lets developers choose the search experience that best fits their application without rebuilding the surrounding integration.

## Baseten Hosted Tools

Baseten Hosted Tools gives developers access to production-ready capabilities from Baseten and our partner ecosystem. The benefits are:

- Keep agents fast: With *Baseten Hosted Tools* , tool calls sit directly in the agent loop. It is built for low latency, runs eagerly and concurrently, and delivers production-scale throughput.
- Ship faster: Add capabilities without integrating and orchestrating every service independently.
- Choose the best tool for the job: Access specialized providers through a consistent developer experience.
- Operate everything together: Run models and the tools they call on the same production platform.
- Integrated billing and usage reporting: like model API token usage, tool calls are differentiated line items, broken down by model, provider and tool type.

This means teams can spend more time improving what their apps do and less time maintaining the plumbing behind it.

### **Server-side tool execution = fewer round trips and faster agents**

In our benchmarks, agents running with our Hosted Tools saw a 15% decrease in end-to-end latency compared to client side tools.

A client-side search loop pays a transit tax on every iteration. Your app calls the model, the model asks for a search, the response travels back to your app, your app calls the search vendor in whatever region they run, and the result travels back. And you re-send the entire growing context to the model. This adds many network hops and requires re-parsing each request.

![When you run the tool in your client, each pass is a fresh request that carries the whole conversation. When you run the tool in the serving path, your client only sees one request.](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1789514247-hosted-tools_diagram-1_updated.png%3Fauto%3Dformat%26w%3D1200&w=3840&q=75) When you run the tool in your client, each pass is a fresh request that carries the whole conversation. When you run the tool in the serving path, your client only sees one request.

Baseten Hosted Tools eliminate the redundant work:

- The runtime is co-located execution
- Context stays server-side, reducing parsing round trips
- Eager and concurrent tool execution while model streams
- Graceful failures
- Live SSEs of every granular step and additional metadata for observability.
- Mixed tool support (client and hosted tools)

![When a co-located loop dispatched each search as it appears in the token stream, a client must wait for the whole turn to arrive.](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1789514345-hosted-tools_diagram-2.png%3Fauto%3Dformat%26w%3D1200&w=3840&q=75) When a co-located loop dispatched each search as it appears in the token stream, a client must wait for the whole turn to arrive.

## **One platform for models and agents**

Baseten has focused on making models fast, reliable, and easy to operate in production. *Baseten Hosted Tools* expands that foundation to the capabilities models use at inference time.

Baseten Grounded Inference is the first step. Over time, we’ll add more tools from Baseten and our partners, giving developers a growing set of building blocks for agents and AI-native applications.

We want to give agents and developers the best primitives to build great experiences. That means expanding Hosted Tools with capabilities like code execution and browser use, with Baseten managing execution and orchestration. Our [acquisition of Blaxel](https://www.baseten.co/blog/blaxel-is-joining-baseten-to-build-the-future-of-agentic-cloud/) accelerates the complementary foundation: fast, isolated, persistent sandboxes and storage where developers can run their own agentic workflows and tool execution..

Our goal is to bring together the models and tools developers need to build high performance AI products and make the entire system production-ready.

Baseten Grounded Inference is available in playground [preview](https://app.baseten.co/model-apis/zai-org/GLM-5.3-Flash/playground) with lowered rate limits (25 RPM) and $2 of free credits to test. If you want to perform scaled evaluations or integrate higher volume production workloads, please [reach out](https://www.baseten.co/talk-to-us/?product=web-search) and our team will be in touch soon.

Explore Baseten Hosted Tools in our [technical documentation](https://docs.baseten.co/inference/model-apis/web-search) or experience it in our [playground](https://app.baseten.co/model-apis/zai-org/GLM-5.3-Flash/playground).
