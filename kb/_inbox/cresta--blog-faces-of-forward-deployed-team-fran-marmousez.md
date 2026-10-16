---
title: 'The Faces of the Forward Deployed Team: Fran Marmousez'
kind: blog
topic: null
subtopic: null
secondary_topics: []
summary: null
triage: null
skip_reason: null
source: cresta
url: https://cresta.com/blog/faces-of-forward-deployed-team-fran-marmousez
author: Jove Zhong
published: '2026-10-15'
fetched: '2026-10-16T06:10:03Z'
classifier: null
taxonomy_rev: 2
words: 1442
content_sha256: 3c72d6c48d1932ae7c3c89b26feca58d216f2d3080cad0b937211ec4b36a6a6d
---

# The Faces of the Forward Deployed Team: Fran Marmousez

Welcome to our first edition of The Faces of the Forward Deployed Team, our spotlight on team members who take AI agents from a promising idea to a production reality for customers.

In this edition, we're putting the spotlight on Fran Marmousez, a Forward Deployed Engineer (FDE) who works out of Cresta’s Australia office.

Before joining Cresta, Fran spent over five years at Google Cloud, most recently as the AI Agents Lead for Japan and Asia-Pacific.

Along the way, she led technical delivery on generative and conversational AI projects for major customers. That included a multi-year implementation for a telecommunications company’s contact center, which employs thousands of agents and serves millions of customers.

We talked about how conversational AI has changed since she entered the field in 2020, the traps hiding in AI quality evaluation, and what customers often get wrong about deploying agents. We also covered why she made the jump from Google to Cresta.

Read on to see what she shared.

### **You've worked in conversational and GenAI since 2020, which gives you a unique perspective on the space. What have been the biggest changes over the years?**

Building a basic chatbot just a few years ago used to be a lot of work.

You had to define what we call intents, which is every possible action a user could ask about. Then for each intent, you had to find as many ways as you could think of to say the same thing and then train classification models on all the variations.

Now an LLM takes over that work. You tell the LLM what a user can do, like make a payment, and the LLM understands the many ways a customer might ask for that action, with no intent lists or training variations needed.

Agentic AI also gives us far more flexibility.

We used to build rigid flows: once a customer said a certain thing, they entered a flow that asked questions in a fixed order, expecting a yes, a no, or another very specific answer. Every path had to be mapped out ahead of time.

Now we give the agent instructions about what to accomplish, and the agent decides how to get there.

If a step isn't needed, for example because the customer already provided the information, the agent moves on instead of asking again. This approach gives the customer a better experience and is much easier for us to plan than mapping every possible combination of flows.

The way we build agents has changed too. At Cresta, for example, we have [Conductor](https://cresta.com/blog/cresta-conductor-the-agent-for-ai-agent-development), where you provide your requirements and what you want the agent to do, and the AI helps developers build the agent and iterates alongside them.

### **You spent a couple of years measuring and improving AI quality at a telco's global contact center. What did that teach you about evaluating AI quality?**

Building an agent is so easy today that the real question is whether it’s good enough for production. The only way to answer that is through evaluation.

At the telco, I learned there are a lot of ways to evaluate an agent, and a lot of traps. For example, in customer service we have plenty of metrics we want to improve, like customer satisfaction.

You'd hope that when CSAT goes down, something is wrong with the agent, but a drop in CSAT doesn't always mean the agent is at fault. Some use cases will always have a low CSAT.

If your internet is down and the agent does everything right and tells you service will be back tomorrow, you're still not going to say you're happy on the survey.

Sometimes the situation is even more extreme, like a thunderstorm that knocks out everyone's internet at once. In those moments the agent is most useful, because so many people are contacting you at the same time that your contact center couldn't have handled the volume, even if the metrics look bad.

All of that to say, the right metric depends on the context.

These days we can use an LLM as a judge to go through transcripts and understand what went on. We [use this approach for Cresta AI Agent](https://cresta.com/blog/how-cresta-grades-its-agents-evaluators-in-an-llm-world) and it’s made evaluations a lot easier than it used to be.

### **What's the most common gap you see between what companies expect an AI agent to do and what it can actually do?**

Some companies think that because an AI agent runs on an LLM, and an LLM is smart, they don't need to give detailed requirements anymore.

That assumption isn't really true. You still need to understand how your company works, what your tone of voice is, and how you want to answer customers in specific situations.

Requirements also aren't the whole picture. We sometimes skip the step of analyzing the conversations that already exist. There are probably human agent conversations about the same topic already, and those conversations matter for two reasons.

First, they show what customers actually ask.

You can build for the happy path, but the interesting part is all the side questions and other problems customers mention along the way. An agent built only from requirements will miss them.

Second, they show why customers escalate to a human today. If we don't solve for those escalation reasons, our new agent won't be any more helpful than the one already in production.

At Cresta we have [Insights](https://cresta.com/cresta-insights) to run this analysis, and Insights surfaces the most commonly-asked questions and reasons users escalate.

### **What drew you to transition from Google to Cresta?**

At Google I saw product gaps and bugs, but I could only raise a feature request or a bug report. A different team handled the request, and I had no control over what happened next.

At Cresta, the Forward Deployed team is encouraged to fix what it finds.

When we spot a gap or a bug while working with a customer, we look at whether we can add the fix to the product ourselves, and the team actively pushes us to try.

This lets us improve the product quickly across our user base.

We can make the change, put it in front of the customer, and keep refining it as we learn, instead of waiting on another team's schedule. Every other customer ends up benefiting from the change as well.

### **Is there a project at Cresta you're especially proud of?**

My first project focused on improving [Compass](https://cresta.com/blog/crestas-compass-ai-improving-discoverability-in-enterprise-applications), an AI assistant built into Cresta’s UX.

It helps customers get answers, find relevant documentation, and move between steps in a workflow without having to navigate the product on their own.


Compass uses context to answer questions accurately and without having users repeat themselves. For example, we’ll look at which page the user is on in the platform. And if Compass can't give a good answer, it offers to raise a support ticket.

My work on Compass included taking what we learn from real customer conversations and using it to sharpen how the assistant responds, as well as reviewing how Compass handled real customer conversations and fixing the cases where it gave a bad or incomplete answer.

These optimizations have helped more customers get accurate answers quickly, and they’ve lightened the ticket load for our support team, giving them the time to resolve each remaining issue thoughtfully instead of rushing through a queue.

All in all, Compass was the perfect project to start with. Our customers ask all kinds of questions about our products, so I learned a lot about Cresta quickly.

### **What advice would you give to someone considering joining the Forward Deployed team at Cresta?**

There’s no shortage of open jobs at AI companies right now, but that doesn’t automatically make the roles rewarding or impactful. Many actually involve shallow work, like wiring up someone else’s model or tweaking prompts, and there’s little real ownership.

Cresta’s FDE role stands out by offering a mix of product engineering and customer-facing work. This means you’re close enough to customers to spot what’s actually broken, and you have the ability to go build the fix, ship it, and see how it lands.

Over time, our hands-on work with customers is what earns their trust in the product. That’s been super satisfying.

The last thing I’d say is that our team is growing super quickly. This means you’re joining at a point where you’ll actually help shape our standards, tools, technical direction, and approach to customer partnership, rather than just inheriting a process someone else already built.

*Our Forward Deployed team is hiring, and we'd love to meet you. Check out our open roles and see if there's a fit.*
