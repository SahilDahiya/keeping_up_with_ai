---
title: How Cresta Built a World-Class Forward Deployed Engineering Team in a Year
kind: blog
topic: null
subtopic: null
secondary_topics: []
summary: null
triage: null
skip_reason: null
source: cresta
url: https://cresta.com/blog/building-a-world-class-fde-team
author: Jove Zhong
published: '2026-10-06'
fetched: '2026-10-08T06:10:53Z'
classifier: null
taxonomy_rev: 2
words: 1156
content_sha256: 8deb8155ebf203b97297c7945f6a48ef9acac2dd16dd0f785ea994e1af672d19
---

# How Cresta Built a World-Class Forward Deployed Engineering Team in a Year

In just twelve months, our Forward Deployed Engineering (FDE) team grew from 1 to 50+ members across the world. And we're still growing.

![Map of where the FDE team members are located](https://cdn.prod.website-files.com/67feba4d16c14d85f1696c4f/6ac50a6470f4582927508fee_17d1c262.png)

Our rapid expansion, along with [winning the FDE team of the year at Propel 26](https://www.linkedin.com/posts/jovezhong_fde-ugcPost-7462376724698206209-8h2E/) and getting invited to join the [Insight Partners FDE Council](https://www.prnewswire.com/news-releases/insight-partners-launches-forward-deployed-practice-anchored-by-the-industrys-first-fde-advisory-council-302898352.html), signals that we've developed a model for helping enterprise customers turn [Cresta AI Agent](https://cresta.com/ai-agent) from a promising demo into a scalable production system that delivers measurable value.

Here's what we've learned over a year of building a Forward Deployed Engineering team that enables industry-leading brands—like [Brinks](https://cresta.com/customers/brinks-home), [Snap Finance](https://cresta.com/customers/snap-finance), and [Alaska Airlines](https://cresta.com/customers/alaska-airlines)— to deliver a world-class customer experience.

## **We put FDE in engineering to optimize for customer value**

AI projects rarely fail because someone can't build a prototype. They fail in the distance between prototype and production.

A prototype can reach 80% of production readiness quickly. The remaining distance requires domain language, edge cases, labeled data, real test sets, permissions, compliance, integrations, and a process for handling failure. That's where most projects slow down or stop.

![Where AI projects typically stall](https://cdn.prod.website-files.com/67feba4d16c14d85f1696c4f/6ac50a6470f4582927508ff1_b0fe7531.png)

We created the Forward Deployed Engineering team to not only own that distance but also adapt the product when it isn't enough to close the gap.

Our core idea is simple: customers don't pay for a demo. They pay for the distance between the demo and production.

Closing that distance takes two kinds of judgment, and we ask every FDE to carry both:

- **Business judgment:** a deep understanding of the customer's business and their end customers, so we can spot where the process gets stuck and what needs to get solved first. When a customer makes a request, an FDE can build and present a “menu” of options
- **Technical judgment:** how to integrate systems, tune models, build evaluations, and make the solution reliable enough to run in production, handling real conversations and real money

Building the “menu” means laying out real options with levels of effort and payoff.

Option A can be the full fix done properly in two weeks; option B can be a minor change that gets 80% of the benefit for a fraction of the effort; and option C can be doing nothing, because what's already shipped is good enough.

Most customers choose Option B. But that only works if the person presenting the menu is also capable of building Option A.

The reason all of this works is structural: our FDEs sit in the Product Engineering org and report up through engineering, not GTM, customer success, or professional services.

With FDEs sitting in engineering, they can open pull requests against the product directly. That's what makes the value compound: what one FDE learns on a project becomes a permanent part of the platform, so the next customer starts from a stronger baseline.

Some of our FDEs have even gone on to design and build entirely new products, like [Cresta Conductor](https://cresta.com/blog/cresta-conductor-the-agent-for-ai-agent-development) and the [Cresta CLI](https://cresta.com/blog/introducing-the-cresta-cli-a-developer-surface-for-an-agent-operable-platform).

## **We move fast between kickoff and production, but never skip evals**

Most of our agent deployments move from kickoff to production in one to three months. The work typically looks like this:

![The FDE team's phases of work](https://cdn.prod.website-files.com/67feba4d16c14d85f1696c4f/6ac50a6470f4582927508ff4_8eeee88f.png)

You'll notice FDEs aren't spending all of their time with customers. No single customer trip runs longer than about five days, and most are two to three.

Trips are timed around discovery and around launch, since that's when the most valuable learning happens. FDEs meet the operators who do the work, watch the workflow in context, and resolve the decisions that determine whether the system can launch.

The rest of the work happens remotely, where the team can build, evaluate, and partner with the core product team.

At any given time, an FDE is usually running two to four projects in parallel. Each project is staffed with two to three FDEs: one member owns the technical design and key implementation, another provides peer review and picks up adjacent use cases, and sometimes a 3rd member acts as an advisor.

It’s also worth noting that we’ll never ship without evals. We always validate that a given model, prompt, and toolset is actually right for the vertical.

A prompt that performs well in one vertical can fail completely in another. Always showing empathy might be the right call in healthcare, for example. But in fintech, when someone owes $4,000 and the agent is being overly empathetic about it, customers have mixed feelings.

## **Our impact on Cresta and customers compounds over time**

Moving a promising AI Agent into one customers can trust, use, and measure is obviously invaluable, but our impact doesn't stop there.

When we see the same task pattern across multiple customers, we turn it into a reusable skill. When a connector is missing, we build it. When a product workflow creates friction, we improve it. And when a model's quality is hard to judge, we create an evaluation set grounded in real conversations.

We don't bill hours and walk away with a forked codebase. Our agents run on a shared platform, so when an FDE improves how we handle guardrails for one airline, that improvement is already there for the next airline.

If one FDE's early deployment takes twelve weeks to get a solution onto the platform, the next can take eight, and the third can take six.

Put simply: every deployment should start much further ahead of the previous one.

This only works because our customer relationships operate like a high-trust omakase restaurant, not an à la carte menu. Our customers don't just ask for what we've already shipped. When we tell them "we have something new, no one's adopted it yet, want to be first?", they say yes.

That's not naivety on their part. It's trust earned over time by consistently showing up with things that actually work.

## **We interview FDEs for judgment, not coding proficiency**

We decided early on to hire FDEs with experience. And our bar isn't "can you code." Almost anyone can spend a weekend with Claude Code and build a chatbot that demos well.

In interviews, we ask about real production scenarios instead, like: “What happened when your agent made a mistake in front of a customer?” And “How did you handle a feature request you knew was wrong?”

These questions expose two things that separate a good FDE from someone who can just code, and neither shows up in a typical interview.

The first is vertical knowledge: what airlines actually care about, what fintech compliance really means, etc. The second is customer-facing maturity: knowing how to say no without losing the relationship, and delivering bad news before the bad news delivers itself.

If this approach resonates with you, we’d love to chat. We're hiring FDEs globally who’ll make decisions that compound across the biggest and most innovative companies in the world.

You can see our open roles and apply [here](http://cresta.com/careers).
