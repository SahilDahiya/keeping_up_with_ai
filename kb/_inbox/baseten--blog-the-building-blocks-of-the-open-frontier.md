---
title: The building blocks of the open frontier
kind: blog
topic: null
subtopic: null
secondary_topics: []
summary: null
triage: null
skip_reason: null
source: baseten
url: https://www.baseten.co/blog/the-building-blocks-of-the-open-frontier
author: Amir Haghighat
published: '2026-11-03'
fetched: '2026-11-12T06:07:12Z'
classifier: null
taxonomy_rev: 2
words: 873
content_sha256: 4722145725ec44712fca82826fb8395013814881d57eaa4b9dcbaef7ba1b66b3
---

# The building blocks of the open frontier

News
# The building blocks of the open frontier

This week we’re expanding our inference platform with three launches alongside our fresh new website.


- Authors
- Date
- November 3, 2026

Every AI product runs on a system: models, the infrastructure that serves them, the training that improves them, and the agents that orchestrate them all. Many teams stitch that system together from separate vendors, and we’ve seen the costs firsthand. They lose time connecting the pieces, add latency moving data between them, and face downtime when one piece fails.

We’ve learned a lot from our customers about what it takes to build that system well, and many of them helped shape what we’re launching this week. OpenEvidence trains models that outperform closed models on Baseten Training, then serves them directly via Dedicated Inference. Datadog trains models on Loops, and serves models via Dedicated and Model APIs. Opendoor routes every AI request across the company through Grid (launching tomorrow), sending each one to the right frontier or open model without changing the harnesses their developers already use.

Each of these use cases needs a tight loop between inference, training, and execution. We built Baseten to bring all of those pieces into one unified platform. Every piece shares the same optimized infrastructure and runs on [Multi-cloud Capacity Management](https://www.baseten.co/blog/how-we-built-multi-cloud-capacity-management/) across dozens of clouds, delivering 99.99% uptime while making intelligence many times faster and cheaper to run at scale.

This week, we’re launching three product milestones to extend our inference platform:

1. Grid: our new gateway, router, and guardrail platform
2. Sandboxes: launching Thursday
3. Loops: our serverless training infrastructure, now generally available

You might notice some new visuals on our site as well; they lean more heavily into the base ten building blocks that inspired our name.

We’ve seen an enormous uptick in coding agent usage, and an explosion in spend has followed. Organizational usage is sprawled across models, providers, and harnesses. Developers default to the most intelligent model available, not the one that’s best-suited to a specific task.

At the same time, open-weight models have caught up to frontier performance on coding, while costing much less to run. Companies need a centralized platform to govern model usage and route tasks to the best model for the job, not just in terms of token cost but quality and overall price. That routing also needs to maximize KV cache hit rate, so multi-turn agentic sessions keep landing on a warm cache and cost per task keeps dropping.

Baseten Grid is our single control layer that gives enterprises access, visibility, and control over their coding spend. It has three parts:

1. Gateway: puts every model and dollar of spend in one place
2. Intelligent Router: matches each task to the right model
3. Guardrails: set company-wide policies on who can use what, and what models are allowed to do

Grid is harness- and model-agnostic, compatible with whichever tools your developers already use (including Claude Code, Codex, OpenCode, and Pi). Each task gets matched to the right model, with the performance, reliability, and security you know from Baseten.

Grid launches tomorrow as a public preview, and we’ll release more details then.

Agent performance is a systems problem. Running code in a container isn’t hard; the hard problems are storage (state), networking (millisecond-long cold starts), and security (VMs). That's what Blaxel has built for sandboxes, and why we recently [acquired Blaxel](https://www.baseten.co/blog/blaxel-is-joining-baseten-to-build-the-future-of-agentic-cloud/) to bring sandboxes to Baseten.

Now, we’re bringing together specialized compute, storage, and networking to build the cloud for agents. Sandboxes are one piece in that puzzle. Baseten Sandboxes are stateful, pause/resumable, VM-isolated, and scale to thousands of instances in seconds.

Because Sandboxes will be co-located with inference, you also get better performance, visibility, and reliability across the full loop between inference and execution.

Sandboxes are moving from private to public preview, and Paul, our Head of Agent Infrastructure, will go into more depth later this week.

It’s become clear that companies want to own their intelligence layer. We help teams like Datadog, Harvey, Lovable, and Parallel post-train open models for their specific use cases, continuously improving on their own data to build durable intelligence.

But not everyone wants to deal with the underlying infrastructure. Top researchers working on training should spend their time on their data and reward functions instead. Loops is our answer to that: serverless SFT and RL on frontier open-weight models, so you can focus on shaping the model you need.

The Loops SDK is also Tinker-compatible, and we let customers run on single-tenant capacity. Loops is fully integrated with our Dedicated Inference, so after training on your incoming data, you can serve your model directly as a production inference endpoint. You always retain ownership of your trained weights.

Loops has been available as a public preview for some time. It will be generally available starting Friday.

Inference, training, routing, governance, and sandboxes are the building blocks of every AI product today. When they come together on a unified platform, the whole is greater than the sum of its parts. That’s the future we’re building for.

Stay tuned this week for more technical content coming about each of these products. You can join the waitlist for the products we’re launching this week [here](https://www.baseten.co/talk-to-us/join-the-waitlist-upcoming-product-launches).
