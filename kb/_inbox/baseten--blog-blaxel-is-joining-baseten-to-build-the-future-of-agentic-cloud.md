---
title: Blaxel is joining Baseten to build the future of agentic infrastructure
kind: blog
topic: null
subtopic: null
secondary_topics: []
summary: null
triage: null
skip_reason: null
source: baseten
url: https://www.baseten.co/blog/blaxel-is-joining-baseten-to-build-the-future-of-agentic-cloud/
author: Amir Haghighat; Tuhin Srivastava; Paul Sinai
published: '2026-09-10'
fetched: '2026-09-11T06:11:24Z'
classifier: null
taxonomy_rev: 2
words: 985
content_sha256: f49af1da411157cc55e1e735ddf80a8cb1b93ec6fd59c918376788106539cff3
---

# Blaxel is joining Baseten to build the future of agentic infrastructure

![Blaxel and Baseten](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1789055607-image-21.png%3Fauto%3Dformat%26fit%3Dcrop%26h%3D630%26w%3D1200&w=3840&q=100)

Today, Blaxel is joining Baseten. By joining forces, we aim to build the cloud for the next trillion agents.

Baseten has built the infrastructure that teams use to train and serve models with industry-leading performance, reliability, and efficiency. Blaxel has built the stateful execution layer agents need to act: fast, isolated sandboxes, persistent storage, and production-grade connectivity. Together, we are expanding Baseten into the infrastructure foundation where teams can serve and train models and can now build long-running agents, all in one integrated platform.

Both companies were founded with the conviction that AI would become ubiquitous and require a new generation of infrastructure. Baseten was started with the belief that delivering fast, reliable inference at scale would become a defining bottleneck to AI adoption. Blaxel was founded on the belief that existing clouds weren't designed for how AI agents run and couldn't support them at scale.

For more than 18 months, we at Blaxel have been building this new cloud, one primitive at a time.

Sandboxes came first because nothing else works without them. Agents write and run code, call tools, and carry state across long tasks, and you can't do that safely in a shared process. Every agent gets its own microVM. We made them extremely fast: suspend and resume in 25 milliseconds, up to 5x faster than other sandbox products. A sandbox can sit idle for months at close to zero cost and come back before the model finishes its next sentence, so state persists without paying for compute you aren't using.

Sapiom runs hundreds of millions of agent loops on Blaxel. As David Zhang, founding engineer there, put it: "Blaxel handled that kind of growth in a way I'd normally expect to take a year or more to reach."

Agents also need to persist and share many artifacts: files, code, and working context. That has to outlive a single run and be accessible to the next sandbox or agent. Agent Drive is our distributed filesystem for that. Mount it into any sandbox and whatever an agent writes is durable, versioned, and there when something else needs it.

And agents have to talk to things. Tools, MCP servers, APIs, other agents. We rebuilt a networking layer that connects all of these pieces with the isolation and access controls a production team will actually sign off on.

The primitive we didn't own was inference. We've seen open-weight & custom models become core to how autonomous agents get deployed in production. Inference is no longer a service you call from another data center. It has to sit next to compute, storage, and network; or latency compounds on every loop.

That brings us to Baseten – joining forces is how we colocate all four, bringing the brain next to the muscles. Baseten's inference stack is the best on the market, running at scale across dozens of regions, with more than $2B raised to build it.

Our shared vision is a future where many agents use many models at massive scale across every part of our daily lives. Together, we’ll build the infrastructure layer that lets millions of autonomous agents run safely with the best performance, reliability, and economics possible.

## Why Blaxel and Baseten

When our teams first met, we each believed running agents at scale meant more than a great sandbox solution or a great inference solution. As conversations progressed and we continued to share learnings, however, it became clear that the best solution was to operate as closely together as possible.

The decision worked because we made the same architectural bets based on the same shared beliefs about the market. We had just done it from different parts of the stack.

Both companies built from the ground up for what it would take to truly scale the workload to our customers’ requirements, rather than taking the fastest path to market. We had both decided that performance, reliability, scalability, security, flexibility, and cost-efficiency needed to be first-class considerations. And we each believed customers need maximum visibility, control, and ownership.

And customers confirm this. As Utkarsh Sengar, CTO of Webflow, put it: "You guys helped us bring a lot of reliability in our system.”

For us, the most important point is that this massively accelerates our vision. We are bringing together two highly complementary companies at exactly the right moment as the market takes shape.

Together we're building a platform where agent execution, inference, and training run on one system. Agents act next to the models they're calling, not across a network boundary. Persistent environments that carry state across turns and sessions. Post-training runs that write to the same storage layer the sandbox reads from, so improving a model on what its agents actually did is part of the same system.

We give them the cloud infrastructure they need, highly configurable and delivered at the velocity they require, in milliseconds. 

Today, this means building around what customers care about most: speed, uptime, and economics. The teams that win will not be the ones running the most agents; they’ll be the ones whose agents are most efficient and improve fastest.

## What this means for our customers

Blaxel is continuing. The team you've been reaching out to for support will continue to assist you just the same as always. The product doesn't change, and features will keep shipping.

Over time, Baseten will add new products based on Blaxel's primitives, starting with Sandboxes. Together with inference and training, these new primitives will be the foundation for the agentic infrastructure we're building.

Charles, Mathis, Chris, Nico, and the rest of the team you talk to daily remain the same people, doing the same work, with more behind them.

Most importantly, we’re grateful for the trust you've placed in us. You made a bet on our infrastructure early and have shaped the product with your feedback. We don't take that lightly, and we thank you for it!
