---
title: 'New in Fleet: Deploy AI agents to Slack in one click'
kind: blog
topic: null
subtopic: null
secondary_topics: []
summary: null
triage: null
skip_reason: null
source: langchain
url: https://www.langchain.com/blog/new-in-langsmith-fleet-bring-agents-into-slack-in-one-click
author: Caspar Broekhuizen
published: '2026-07-15'
fetched: '2026-07-17T06:47:01Z'
classifier: null
taxonomy_rev: 2
words: 735
content_sha256: f2bed531fab99aa90bd1b845fe9a82832f7f78b4bf8aa64064870387bf70c9f1
---

# New in Fleet: Deploy AI agents to Slack in one click

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/6a56f34bf9c3e0c7ffe7ad5c_fleet-new-slack.png)

Today, we're making it simple to equip your team with custom agents in Slack, without writing code.

For many teams (including ours at LangChain), Slack is where a lot of work gets done. Projects get kicked off with a question from a teammate, a shared file, or a conversation thread. Much of the project context is there in Slack right alongside the collaborators.

Now Fleet agents can join that work. One person builds an agent, then the whole team can use it in Slack—right in the flow of work.

See how 11x built a Slack-native bug triage agent with Fleet:

## Build an agent around your company’s work

Agents are great at handling repetitive work, and they work best when they understand how your business operates. That’s why Fleet allows you to build specialized agents that follow your company’s best practices. When someone builds an agent, they can give that agent the skills, context, and systems required to do the job right.

It’s a different approach to generalized chat, like ChatGPT or Claude. Generalized agents are great for ad hoc tasks, but when you want a job done consistently, stringing together multiple prompts can get tedious. Specialized agents allow you to codify an approach and enable all of your teammates to use it. You can also tie all the relevant permissions to each agent (more on that in a minute).

Getting started is simple because you build Fleet agents with natural language. That means anyone — from engineers to ops to subject matter experts — can contribute.

Just describe your goal using chat or use one of the prebuilt agent templates. Templates are based on agents we use every day at LangChain, like the Executive Assistant and Software Engineer. Every template includes a short onboarding flow to tailor the agent for your use case, including the app connections and knowledge it needs.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/6a56f4c883e38919255d8f91_Templates.png)

## Give every agent a place in Slack

After creating an agent, you can make it available in Slack with one click. Every Fleet agent has its own Slack identity, with a name, description, and icon, so teammates recognize its role and know when to tag it.

That identity becomes especially useful as agents spread across teams. At 11x, Jeson Patel, CTO, first deployed a bug triage agent to help teams resolve issues faster. The team quickly expanded to additional use cases, including on-call alerts and a product Q&A agent for GTM.

Everyone at the company knows the identity of the agent and it’s all inthe main channels, so they just tag it… We even have salespeople that will pull it up on sales calls when they have a question about the product.

An agent’s role is clear because it isn’t hidden behind a generic bot. It has a recognizable identity and can return work to the same thread where the request started, including attached files when the task requires them.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/6a56f4afa5d669f3e1f6abf3_Slackpreview%20(1).png)

## Keep the work, and the judgment calls, in one thread

Work doesn’t always run in a straight line. If you hand off a customer research request for some outbound prospecting, your agent may need additional context or reach a step that should require approval, like sending an email.

In Slack, Fleet agents can ask follow-up questions and request approval before taking actions right there in the same thread. You can approve, redirect, or ask for a change, then let the agent continue.

This approach keeps the request, the surrounding conversation, and the result together. It also keeps teammates involved where their judgment matters.

## Control permissions, access, and spend

Fleet gives admins oversight across every agent. You can control access to connections, configure which credentials an agent uses, set spend limits, and decide who can view, run, and edit each agent.

With Fleet, you define the scope of each agent’s job, as broad or narrow as needed. Agents have durable instructions and only the tools, credentials, and permissions required for that role, so builders can give agents what they need without giving them access to everything in your company workspace.

## What’s next

Agents should be easy to build, easy to share, and easy to use where work is already happening. Fleet already made building simple, and today’s release makes Fleet agents much easier to bring into Slack, with one-click sharing.

Fleet is where you create, configure, and manage agents. Slack is where your team works with them.
