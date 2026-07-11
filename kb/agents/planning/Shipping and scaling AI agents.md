---
title: Shipping and scaling AI agents
topic: agents
subtopic: planning
secondary_topics:
- infra-platform/deployment
summary: Practical guide to shipping and scaling AI agents, including lifecycle, reliability,
  deployment, and continuous improvement concerns.
source: sierra
url: https://sierra.ai/blog/shipping-and-scaling-ai-agents
author: Zack Reneau-Wedeen
published: '2026-05-12'
fetched: '2026-07-11T03:53:47Z'
classifier: codex
taxonomy_rev: 1
words: 1534
content_sha256: f490cdc1d46293f633852778097128646c08698fc6f3b4fe715eb35c22fa3c56
---

# Shipping and scaling AI agents

# Shipping and scaling AI agents

![Sierra's agent development process](https://sierra.ai/-/cdn/image?src=https%3A%2F%2Fcdn.sanity.io%2Fimages%2Fca4jck6w%2Fproduction%2F570dafee81e7db1b21f8718f85ed3c2350eee372-2475x1393.png&width=3840&quality=75)

Sierra AI agents are transforming customer experiences in the real world. They are helping customers set up Sonos speakers, refresh SiriusXM radios, and process OluKai shoe returns and exchanges. As we’ve scaled with our early customers, we’ve incorporated dozens of refinements and product insights into the [Agent Development Life Cycle](https://sierra.ai/blog/agent-development-life-cycle), our methodology for building, testing, and optimizing AI agents.

For anyone wondering what it looks like in practice to ship and scale AI agents, this post delves into key lessons we’ve learned during each stage of agent development. At the outset of a partnership, we’ve found success running toward complexity and targeting previously unsolvable challenges. While building and testing with our customers, we’ve learned how to equip each AI agent with the instruction manual it needs to be successful and avoid failure. And when an agent is ready for launch, we’ve discovered how to accelerate learning exponentially in production. Finally and most importantly, we’ve found that every agent must be crafted as a full-fledged product, tailored seamlessly to the unique requirements of your company.

**The hardest problems tend to be most valuable**

Companies often approach us with a variety of scenarios they hope an AI agent will be able to handle. Some are simple, like providing answers to customer questions (“what is your return policy?”), while others are more complex and may require customer-specific information, multi-step reasoning, and taking action (“can you help me return my shoes that don’t fit?”).

AI agents are a completely new domain, so it can be tempting to start simple. But we’ve learned that straightforward problems like Q&A typically represent only a small portion (and the least valuable portion) of conversations that businesses are having with their customers. The magic of AI agents—from both the technological and business perspectives—comes through when they demonstrate deeper integrations and “agentic” reasoning, allowing them to fully resolve complex customer issues.

At Sierra, we design and build AI agents directly with our customers. This collaboration starts with a 90-minute design workshop focused on the different “journeys” the agent must be able to traverse. A journey corresponds to a goal that an end user might have in mind, such as returning a package or debugging a technical issue. This session helps teams from CX to IT align on the most important jobs to be done.

We search for problems that, were they easy, would already be solved. For example, troubleshooting your Sonos system or refreshing your SiriusXM radio can be a many-step process depending on a half-dozen different systems integrations. Using Agent OS, our underlying platform for AI agent development, we are able to compose agents with the skills they need to execute complex processes, and we can ensure they have access to the tools and systems they need to do the work (i.e. actually sending a refresh signal from a satellite to your car).

**AI agents need manuals, just like the rest of us**

Balancing creativity and predictability is one of the fundamental challenges of AI engineering. As detailed in the [Agent Development Life Cycle](https://sierra.ai/blog/agent-development-life-cycle) post, agents should be “creative, but in the moments that matter, like processing an order or upgrading a plan, deterministic safeguards [must] ensure that your business logic is strictly and deterministically enforced.” Put more simply, in the same way you would give your employees a handbook, you need to give your AI agent a manual.

Once we have worked with our customers to define an initial set of journeys to focus on, we build out detailed specifications. Journey specs serve as the initial instruction manual for an AI agent. For example, a spec for returns and exchanges might detail how to communicate return policies to different groups of customers (e.g. premium subscribers), as well as the APIs needed to process a return.

Sierra agents are able to model not only the policy itself, but also the policy behind the policy. In the case of one of our retail customers, their Sierra agent is able to explain to shoppers that the company offers a 30-day return window. Simultaneously, the agent is also modeled to make exceptions in certain cases, like accepting returns from loyal customers for up to 45 days.

During development, customers perform quality assurance using Sierra’s Experience Manager, which is Sierra's app for observability, evaluation, reporting, and optimization. In essence, the Experience Manager is how customers can track agent performance, manage the agent to ensure it is following its instruction manual, and continuously improve the manual and agent over time. (And once the agent is live, Customer Experience teams often learn about product issues—such as app crashes, customer frustrations, and quality control lapses—before any other part of the business.)

Our customers also get a major assist from AI. Not only are they able to review conversations manually, but each conversation is additionally reviewed by AI models for quality and to tune review processes before production launch. Any time an agent makes a mistake, customers can pinpoint where and why, ground the agent in the correct processes and information, and generate tests to make sure they never make the same mistake twice. Large Language Models (LLMs) may be “black boxes,” but Sierra agents are highly observable.

![Sierra Experience Manager](https://sierra.ai/-/cdn/image?src=https%3A%2F%2Fcdn.sanity.io%2Fimages%2Fca4jck6w%2Fproduction%2F5cc2dd2b190eb06531bce4e831c86f6e4750cb7d-1758x1759.png&width=3840&quality=75)

**Learning accelerates after launch**

The agent “launch”—when your AI agent begins having live conversations with your customers—is one of the most important parts of agent development. No matter how sophisticated the agent orchestration or quality assurance, customers inevitably make unpredictable requests. For example, “My dog chewed up my shoes. Can I get a new pair?” It’s unlikely that an AI agent was initially designed to manage dog-specific product exchanges.

These interactions are where the real learning begins. Over time, the process of iteratively observing and tuning an AI agent generates a continuous feedback loop, and agents improve exponentially as they handle more interactions and gather more data and insights.

The most agile companies have fully-aligned customer experience and technology teams who are working closely to monitor those insights on a daily basis. Tight-knit collaboration creates an environment designed for continuous improvement and speed. For example, CX teams will review conversations for quality assurance while technical teams debug integrations and provision APIs. Then, everyone works together to connect the dots. Aligned teams are better able to see the big picture and think holistically about opportunities and challenges before and after the launch.

The Experience Manager becomes even more powerful once an agent is live. Conversations are automatically annotated with tags and AI-based supervision, which are used to generate reports, track key performance indicators, and route key insights back to customer experience and product teams.

Post-launch, the Experience Manager continues to be the hub for conversation review, issue management, and interaction testing. As the agent scales, we can sample conversations based on tags to ensure representative and efficient review. We continue to meet weekly with customer stakeholders to review performance, ship updates, and prioritize new journeys. As you might suspect, manual review is still just as important as AI-based tooling.

Within a few weeks of accelerated iteration and improvement, Sierra agents are often able to fully resolve most incoming inquiries without ever needing to transfer the customer to a representative. In some customer journeys, even very complex ones, Sierra agents are able to fully resolve more than 90% of customer inquiries.

**Every agent is a product**

Sierra sees a number of universal requirements across AI agents. Abstractly, they all need to be trustworthy and imbued with sophisticated process knowledge and information. They need to have the capability to work with internal systems, and they need to perform with high accuracy and empathy.

At the same time, each agent also must be tailored seamlessly to the unique requirements of your company, representing your brand to the highest standards, internalizing your processes, knowledge bases, business goals, and risk controls to the same degree as your best representatives.

We’ve learned to treat each agent as a full-fledged product in and of itself, instead of trying to overly apply abstractions to the platform layer underneath. This means our customers can create AI agents with near limitless customization, while also benefiting from ongoing innovation at the platform level. When the stakes are representing your business to your customers, there is no one-size-fits-all approach.

In order to pull it off, we staff a dedicated agent engineer and product manager on each of our deployments. They are responsible for translating the journey design into agent code, integrating with customer systems, and partnering closely with operations teams to review conversations and continuously iterate.

At each stage of scaling—from 100 conversations per week to 1,000 to 10,000 to 100,000 and beyond—the agent improves to reach a point where new issues slow to a trickle and greater scale is needed to uncover new ones. This is working as intended and lasts all the way until the agent is at full scale with minimal issues.

Scale, however, does not mean steady state. Just as [fifteen percent of all Google searches have never been searched before](https://x.com/Google/status/1493681643290300425), Sierra agents are constantly fielding new and more complex requests, and businesses are constantly evolving and changing.

Every agent is a product, and great products are never done.
