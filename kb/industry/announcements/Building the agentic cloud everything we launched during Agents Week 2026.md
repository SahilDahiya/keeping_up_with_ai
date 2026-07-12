---
title: 'Building the agentic cloud: everything we launched during Agents Week 2026'
topic: industry
subtopic: announcements
secondary_topics:
- infra-platform/deployment
summary: 'Roundup of every Agents Week 2026 launch for Cloudflare''s ''agentic cloud'':
  Artifacts (Git-compatible versioned storage), Sandboxes with Outbound Workers for
  zero-trust egress, Durable Object Facets, and Workflows rearchitected to 50,000
  concurrency for durable background agents.'
source: cloudflare-ai
url: https://blog.cloudflare.com/agents-week-in-review/
author: Ming Lu
published: '2026-04-20'
fetched: '2026-07-11T04:13:16Z'
classifier: claude
taxonomy_rev: 1
words: 1703
content_sha256: 60a87d8cb8c9ee0485ab66e84dacec746ee8dc54feebb6a33ae6210bfdf97347
---

# Building the agentic cloud: everything we launched during Agents Week 2026

Today marks the end of our first Agents Week, an innovation week dedicated entirely to the age of agents. It couldn’t have been more timely: over the past year, agents have swiftly changed how people work. Coding agents are helping developers ship faster than ever. Support agents resolve tickets end-to-end. Research agents validate hypotheses across hundreds of sources in minutes. And people aren't just running one agent: they're running several in parallel and around the clock.

As Cloudflare's CTO Dane Knecht and VP of Product Rita Kozlov noted in our [ welcome to Agents Week post](https://blog.cloudflare.com/welcome-to-agents-week/), the potential scale of agents is staggering: If even a fraction of the world's knowledge workers each run a few agents in parallel, you need compute capacity for tens of millions of simultaneous sessions. The one-app-serves-many-users model the cloud was built on doesn't work for that. But that's exactly what developers and businesses want to do: build agents, deploy them to users, and run them at scale.

Getting there means solving problems across the entire stack. Agents need **compute** that scales from full operating systems to lightweight isolates. They need **security** and identity built into how they run.  They need an **agent toolbox**: the right models, tools, and context to do real work. All the code that agents generate needs a clear path from afternoon **prototype to production** app. And finally, as agents drive a growing share of Internet traffic, the web itself needs to adapt for the emerging **agentic web**. Turns out, the containerless, serverless compute platform we launched eight years ago with Workers was ready-made for this moment. Since then, we've grown it into a full platform, and this week we shipped the next wave of primitives purpose-built for agents, organized around exactly those problems.

We are here to create Cloud 2.0 — the agentic cloud. Infrastructure designed for a world where agents are a primary workload.

Here's a list of everything we announced this week — we wouldn’t want you to miss a thing.

It starts with compute. Agents need somewhere to run, and somewhere to store and run the code they write. Not all agents need the same thing: some need a full operating system to install packages and run terminal commands, most need something lightweight that starts in milliseconds and scales to millions. This week we shipped the environments to run them, as well as a new Git-compatible workspace for agents:

|
 |
 |
|---|---|
| Give your agents, developers, and automations a home for code and data. We’ve just launched Artifacts: Git-compatible versioned storage built for agents. Create tens of millions of repos, fork from any remote, and hand off a URL to any Git client. | |
| Cloudflare Sandboxes give AI agents a persistent, isolated environment: a real computer with a shell, a filesystem, and background processes that starts on demand and picks up exactly where it left off. | |
|
 | Outbound Workers for Sandboxes provide a programmable, zero-trust egress proxy for AI agents. This allows developers to inject credentials and enforce dynamic security policies without exposing sensitive tokens to untrusted code. |
|
 | Durable Object Facets allows Dynamic Workers to instantiate Durable Objects with their own isolated SQLite databases. This enables developers to build platforms that run persistent, stateful code generated on-the-fly. |
|
 | Cloudflare Workflows, a durable execution engine for multi-step applications, now supports 50,000 concurrency and 300 creation rate limits through a rearchitectured control plane, helping scale to meet the use cases for durable background agents. |

Running agents and their code is only half the challenge. Agents connect to private networks, access internal services, and take autonomous actions on behalf of users. When anyone in an organization can spin up their own agents, security can't be an afterthought. It has to be the default. This week, we launched the tools to make that easy.

|
 |
 |
|---|---|
|
 | Cloudflare Mesh provides secure, private network access for users, nodes, and autonomous AI agents. By integrating with Workers VPC, developers can now grant agents scoped access to private databases and APIs without manual tunnels. |
|
 | Managed OAuth for Cloudflare Access helps AI agents securely navigate internal applications. By adopting RFC 9728, agents can authenticate on behalf of users without using insecure service accounts. |
|
 | Cloudflare is introducing scannable API tokens, enhanced OAuth visibility, and GA for resource-scoped permissions. These tools help developers implement a true least-privilege architecture while protecting against credential leakage. |
|
 | We share Cloudflare's internal strategy for governing MCP using Access, AI Gateway, and MCP server portals. We also launch Code Mode to slash token costs and recommend new rules for detecting Shadow MCP in Cloudflare Gateway. |

A capable agent needs to be able to think and remember, communicate, and see. This means being powered with the right models, with access to the right tools and the right context for their task at hand. This week we shipped the primitives — inference, search, memory, voice, email, and a browser — that turn an agent into something that actually gets work done.

|
 |
 |
|---|---|
|
 | Announcing a preview of the next edition of the Agents SDK — from lightweight primitives to a batteries-included platform for AI agents that think, act, and persist. |
| An experimental voice pipeline for the Agents SDK enables real-time voice interactions over WebSockets. Developers can now build agents with continuous STT and TTS in just ~30 lines of server-side code. | |
|
 | Agents are becoming multi-channel. That means making them available wherever your users already are — including the inbox. Cloudflare Email Service enters public beta with the infrastructure layer to make that easy: send, receive, and process email natively from your agents. |
|
 | We're building Cloudflare into a unified inference layer for agents, letting developers call models from 14+ providers. New features include Workers binding for running third-party models and an expanded catalog with multimodal models. |
|
 | We built a custom technology stack to run fast large language models on Cloudflare’s infrastructure. This post explores the engineering trade-offs and technical optimizations required to make high-performance AI inference accessible. |
|
 | Running large LLMs across Cloudflare’s network requires us to be smarter and more efficient about GPU memory bandwidth. That’s why we developed Unweight, a lossless inference-time compression system that achieves up to a 22% model footprint reduction, so that we can deliver faster and cheaper inference than ever before. |
| Cloudflare Agent Memory is a managed service that gives AI agents persistent memory, allowing them to recall what matters, forget what doesn't, and get smarter over time. | |
| AI Search is the search primitive for your agents. Create instances dynamically, upload files, and search across instances with hybrid retrieval and relevance boosting. Just create a search instance, upload, and search. | |
| Browser Rendering is now Browser Run, with Live View, Human in the Loop, CDP access, session recordings, and 4x higher concurrency limits for AI agents. |

The best infrastructure is also one that’s easy to use. We want to meet developers and their agents where they’re already working: in the terminal, in the editor, in a prompt, and make the full Cloudflare platform accessible without context-switching.

|
 |
 |
|---|---|
| We’re introducing cf, a new unified CLI designed for consistency across the Cloudflare platform, alongside Local Explorer for debugging local data. These tools simplify how developers and AI agents interact with our nearly 3,000 API operations. | |
|
 | Agent Lee is an in-dashboard agent that shifts Cloudflare’s interface from manual tab-switching to a single prompt. Using sandboxed TypeScript, it helps you troubleshoot and manage your stack as a grounded technical collaborator. |
| Introducing Flagship, a native feature flag service built on Cloudflare’s global network to eliminate the latency of third-party providers. By using KV and Durable Objects, Flagship allows for sub-millisecond flag evaluation. | |
|
 | Learn how to deploy PlanetScale Postgres and MySQL databases via Cloudflare and connect Cloudflare Workers. |
|
 | The Cloudflare Registrar API is now in beta. Developers and AI agents can search, check availability, and register domains at cost directly from their editor, their terminal, or their agent — without leaving their workflow. |

As more agents come online, they're still browsing an Internet that was built for people. Existing websites need new tools to control what bots can access their content, package and present it for agents, and measure how ready they are for this shift.

|
 |
 |
|---|---|
|
 | The Agent Readiness score can help site owners understand how well their websites support AI agents. Here we explore new standards, share Radar data, and detail how we made Cloudflare’s docs the most agent-friendly on the web. |
| Soft directives don’t stop crawlers from ingesting deprecated content. Redirects for AI Training allows anybody on Cloudflare to redirect verified crawlers to canonical pages with one toggle and no origin changes. | |
| By migrating our request handling layer to a Rust-based architecture called FL2, Cloudflare has increased its performance lead to 60% of the world’s top networks. We use real-user measurements and TCP connection trimeans to ensure our data reflects the actual experience of people on the Internet | |
|
 | We give you a sneak peek of our support for shared compression dictionaries, show you how it improves page load times, and reveal when you’ll be able to try the beta yourself. |

Agents Week 2026 is ending, but the agentic cloud is just getting started. Everything we shipped this week — from compute and security to the agent toolbox and the agentic web — is the foundation. We're going to keep building on it to give you everything you need to build what's next.

We also have more blog posts coming out today and tomorrow to continue the story, so keep an eye out for the latest [ at our blog](https://blog.cloudflare.com/).

If you're building on any of what we announced this week, we want to hear about it. Come find us on [ X](https://x.com/cloudflaredev) or

[, or head to the](https://discord.com/invite/cloudflaredev)

__Discord__[.](https://developers.cloudflare.com/products/?product-group=Developer+platform)

__developer documentation__
