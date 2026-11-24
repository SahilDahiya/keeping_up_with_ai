---
title: 'The Faces of the Forward Deployed Team: Shengyao Qian'
kind: blog
topic: null
subtopic: null
secondary_topics: []
summary: null
triage: null
skip_reason: null
source: cresta
url: https://cresta.com/blog/faces-of-forward-deployed-team-shengyao-qian
author: Jove Zhong
published: '2026-11-18'
fetched: '2026-11-24T06:06:29Z'
classifier: null
taxonomy_rev: 2
words: 1390
content_sha256: e41a63b3197eea4e7d34919d8fa8e498507e462bdde9a2ed00871ccefe4daf69
---

# The Faces of the Forward Deployed Team: Shengyao Qian

Welcome to another edition of the Faces of the Forward Deployed Team, our spotlight on team members who work with customers to build and deploy [Cresta AI Agent](https://cresta.com/ai-agent).

In this edition, we’re putting the spotlight on Shengyao Qian, a Forward Deployed Engineer (FDE) who works out of San Francisco.

Before joining Cresta, Shengyao spent time at Google Cloud building time series infrastructure, at Waymo building fleet operations software, and at a startup she co-founded with her friends.

We talked about her path from Google to Waymo, her journey as a founder, what a day looks like in her FDE shoes, and more.

### **You’ve worked at some really impressive businesses, including Google Cloud and Waymo. What did you do at those organizations?**

When I was on the Google Cloud team I helped build a time series database for cloud logging and monitoring. It was deep backend infrastructure work, so it was highly technical and a great learning opportunity.

Then one day, Waymo threw a party on the top floor of our building, and after having a drink or two with the hiring manager, he asked if I wanted to join.

> Waymo cars were just starting to show up in San Francisco, so the opportunity sounded really interesting. I couldn’t turn it down.

At Waymo, I worked on fleet management software. We had a depot in Phoenix, Arizona with about 100 cars, and our software sent them on different missions. Some cars did training, some did mapping, and some drove trial rounds with real passengers.

### **You’re also a co-founder! Tell me about that experience.**

I co-founded a startup with friends called Joint AI. It used AI agents to automate logistics operations.

My initial co-founder and I both came from technical backgrounds and had zero business sense. Building things was never hard for us, but figuring out how to talk to people and sell something was a real struggle.

We later brought on a sales-focused co-founder who’s also a friend. We were selling to warehouses and freight forwarders, so one day he drove us around a logistics center in Hayward and we just knocked on doors to pitch our platform. We did the same thing in LA, where a lot of logistics companies are concentrated. It was a bit traumatizing but also really exciting.

> The startup ultimately didn’t work out for many reasons, but I came away wanting to be closer to the customer.

### **Why did you want to move into a forward deployed engineering role?**

When you’re doing work for another internal team, it’s hard to verify that a need is real. People can have different opinions, and sometimes the better presenter wins, even when the idea isn’t validated.

For example, at Google, our customers were internal infrastructure teams, so nobody was paying for what we built. That made it hard to tell a real need from one that just sounded convincing.

> But when customers are willing to pay for something, that’s a very real signal. It proves we’re meeting a need in the market.

This led me to search for roles where I could talk to customers directly, get exposure to their business needs, and build for them.

Given my background, nobody was going to hire me as a salesperson, so engineering plus being close to the customer was my ideal combination—and forward deployed engineering met those requirements.

### **Why did you choose Cresta?**

I liked everyone who interviewed me.

My first interviewer gave me an algorithm problem I had never heard of. He explained it so well that I implemented it the first time I heard it, and that told me how well he understood it.

Every interviewer after that explained problems the same way, including concepts that were new to me. Because I could finish each problem, I also felt like I was growing during the interview itself.

I also wanted flexibility in my role. For example, I knew I wanted to be involved in pre-sales and focus less on product development.

> While interviewing, it became clear that leadership was open to me exploring pre-sales and other areas I was interested in, and they still are. I don’t think I could find leaders as open minded about where I could contribute elsewhere.

### **Tell me about a project or two you’ve done at Cresta that you’re most proud of.** 

There are two projects that immediately come to mind:

**1. Helping close Mercury Insurance as our first self-serve customer for AI Agent.**

I led our work with Mercury from the beginning.

I started by educating Mercury’s team on how our AI Agents work. From there, a solutions engineer and I took Mercury’s call flows to uncover the best automation opportunities. We landed on two use cases: claim status checks and discount offers for customers calling to cancel.

Next, I held daily calls with their team over the course of a week to demo each use case. I walked them through how I built them, how to read traces, and the steps for building them on their own. We took their feedback each day and brought back refined versions the next so they always had something new to react to.

I also took their broader platform feedback and translated it into requests for our engineering team. Working together, we ended up improving [Cresta CLI](https://cresta.com/blog/introducing-the-cresta-cli-a-developer-surface-for-an-agent-operable-platform), the command-line tool developers use to build and test AI Agents. We also built environments and deployments, which let teams set up separate testing and production versions of an agent and move changes between them.

It’s safe to say that Mercury’s feedback helped our engineers focus on the improvements that mattered most, ensuring every future self-serve customer starts with a stronger platform.

**2. Building retrieval-augmented generation (RAG) functionality for AI Agent.**

My work focused on how AI Agent can find the right information in a customer’s documents and use it to write answers that are accurate, complete, and personalized for every user.

Our [implementation with Xanterra](https://cresta.com/customers/xanterra), the largest operator of lodges, restaurants and concessions in U.S. national parks, is a great real-world example of AI Agent using RAG.

Their guests ask about everything from lodging to wildlife tours across four contact centers, so AI Agent has to answer a wide range of questions at a really high volume.

With RAG, the AI Agent can pull answers from Xanterra’s own content for each park, giving guests accurate, up-to-date answers across parks consistently.

The results with Xanterra speak for themselves: “Skye”, the AI Agent for Glacier National Park, contains 84% of conversations, while “Faith,” Yellowstone’s AI Agent, contains 76% of conversations.

### **What does a typical day at Cresta look like?**

Most FDEs work on deployments, and I do too.

We design, develop, and deploy Cresta AI Agent for customers. But we aren’t just builders. For example, when a customer wants to add something, we give technical advice and help them weigh the tradeoffs.

In addition, I support Cresta’s partner channel.

We want third-party resellers to feel enabled to sell and implement AI agents, so I work with partner companies on what kind of talent they need to hire. And once those people join, I train them on how AI agents work and how to deploy them on the Cresta platform.

I also work with our core infrastructure team to make the platform easier for our partners’ developers to use, from the interface to the rules for deploying code.

### **What advice would you give someone choosing between FDE roles at different companies?**

Candidates often ask me whether the FDE role is temporary, because AI agent solutions today are highly customized and might eventually be automated. I don’t know if that’s true, and nobody can predict the future.

> What I do know is that whatever the future holds, you want a role that’s flexible and can adapt. That’s true of an FDE role and of any other job.

At Cresta, I have a lot of room to explore and learn. I get to work in sales, partnerships, and with customers on initiatives that extend beyond simply building AI agents, like helping them set revenue goals.

That flexibility means I’m well positioned no matter how the FDE role evolves.

*Our Forward Deployed team is hiring, and we’d love to meet you! Check out our open roles and see if there’s a fit.*
