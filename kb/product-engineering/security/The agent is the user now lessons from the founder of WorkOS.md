---
title: 'The agent is the user now: lessons from the founder of WorkOS'
topic: product-engineering
subtopic: security
secondary_topics:
- agents/planning
summary: Interview-driven discussion of agents as users, covering identity, permissions,
  memory, evals, and feedback loops as core production-agent infrastructure.
source: arize
url: https://arize.com/blog/ai-engineer-agents-workos-identity-permissions-evals/
author: Aaron Winston
published: '2026-07-08'
fetched: '2026-07-11T04:41:34Z'
classifier: codex
taxonomy_rev: 1
words: 1690
content_sha256: 892a3e66158ce72fdb73e2386a6d53a985bf1f906125b43f6e9af754e9272622
---

# The agent is the user now: lessons from the founder of WorkOS

**WorkOS founder  Michael Grinich says the next era of AI engineering will not be defined by prompts alone. It will be defined by the systems around agents: identity, permissions, evals, memory, and the feedback loops that keep autonomous software from succeeding in all the wrong ways.**

This is the first installment of Rise of the Agent Engineer, a new Arize series on the builders turning agents from demos into production systems.

Michael Grinich gave an AI coding agent a simple instruction: make the tests pass.

“The agent decided to delete all the tests,” Grinich says, “because then none of them would fail.”

The agent didn’t crash, hallucinate a library, or refuse the task. The system asked for green tests, so the agent removed the thing that could turn red.

It’s the kind of story you can’t help but laugh at (and there’s probably a reference to the popular show Silicon Valley in here somewhere). But it exposes a real problem.

“While that’s like technically accurate,” Grinich says, “it wasn’t something I was expecting.”

That’s one of the central problems of AI engineering: agents can fail in ways that superficially look like success.

For Grinich, the founder and CEO of WorkOS, this was more than just a coding-agent anecdote. WorkOS helps companies become enterprise-ready, which means it lives in the layer where software meets company boundaries: authentication, authorization, directories, admin portals, and the infrastructure that determines whether a product can actually be adopted inside an enterprise.

That gives Grinich a practical view of the agent era. Agents are becoming operators inside software systems and are reading docs, calling APIs, changing files, configuring services, running tests, and crossing boundaries that used to only be crossed by humans.

“With agents, it changes the equation completely,” Grinich says. “There’s more of them than people. You can spawn them really fast to do specific tasks and they’re non-deterministic.”

The agent is becoming the user, and the old user model in software is starting to break.

**Agents don’t use software like people do**

Developer tools have always assumed the user is a person.

A developer might read docs and log in to a product. They’d then get a role, copy an environment variable, and interpret an error before deciding what to change and why.

Agents scramble that model because they are useful for exactly the reason they are risky: they can act across systems.

An agent installing a product may need access to code, docs, tickets, CI, identity providers, deployment settings, logs, and billing surfaces in the same run. It may act on behalf of a user, a team, a workflow, or another agent, then disappear.

That creates authorization issues.

Grinich describes one failure mode he’s seen as an agent behaving “like a little minion that was succeeding at the task, but it was actually breaking past a security boundary.”

That’s the new security problem: agents pursue goals, but goals aren’t policies.

“We want to give agents access to tons of systems and go do stuff,” Grinich says. That creates “this kind of tension around the security model.”

In the agent era, permissions need to describe the work, not just the user.

**Developer experience is becoming agent experience**

The first response to agents was to make software easier for models to read.

WorkOS spent a lot of time making its product and documentation “agent ready,” Grinich says. The goal was still collaborative: a developer would ask questions, the agent would read the docs, and they would work together.

But that’s changing quickly.

Earlier this year, for instance, WorkOS built a system that uses AI to handle installation and migration without a human doing the steps manually.

“There’s no human involved,” Grinich says, and the agent is now navigating the product by itself.

“It’s no longer about developer experience or even human-AI experience,” Grinich says. “It’s like a full agent experience end to end.”

That line captures a key shift as the industry moves from thinking purely about developer experience (DX, or DevEx) to the [agent experience](https://arize.com/blog/what-is-an-agent-harness-why-harnesses-are-replacing-agent-frameworks/).

Developer experience was built around clear docs, fast setup, good defaults, helpful errors, predictable APIs, and clean SDKs. But agent experience asks whether autonomous software can use a product correctly, safely, and observably without a person filling in the gaps.

Agents go beyond using an API. If your docs are ambiguous, the agent may guess. If your CLI has unsafe defaults, the agent may find them. And if your [eval](https://arize.com/blog/evals-in-ci-how-to-write-llm-evals-as-tests/) only checks whether the task finished, the agent may learn to finish the task in a way you never intended.

In other words: your product surface is becoming part of the agent runtime.

**The new funnel is an eval**

WorkOS now tests whether an agent can use its product without a person steering the work.

“We actually have evals for how agents can go use our products without humans involved,” Grinich says. “How can agents sign up for it? How can they configure it? Can they test? Can an agent fully go into production without a human involved at all?”

That changes the benchmark for developer tools.

For years, teams measured onboarding by time to integration: how quickly can a developer get from docs to production?

For agents, the better test is whether an agent can complete the integration correctly, stay inside the right boundaries, and leave behind a [trace](https://arize.com/blog/project-rosetta-stone-instrumenting-agents-any-framework/) someone can inspect.

That requires more than a prompt. A product that is agent-ready needs to answer five questions:

- Who is the agent acting as?
- What is it allowed to do for this specific task?
- Can the system tell whether it succeeded without violating an invariant?
- Can a human or another system inspect the path it took?
- What should the agent remember, and what should it forget?

Identity defines the actor, permissions define the boundary, evals define success, observability makes the path inspectable, and memory determines what improves next time.

The deleted-tests anecdote shows why each of these steps matters. “Tests are passing” is a metric, and “the tests still exist” is an invariant. If the system only measures the metric, the agent can satisfy the dashboard while destroying the thing the dashboard was supposed to protect.

The agent’s version of success has to be checked against the system’s definition of acceptable behavior.

**Memory is the next moat**

Many agents today are still task machines. They can inspect a repo, make a change, summarize a thread, call a tool, or generate a plan. But long-running autonomy requires something more durable than context packed into a prompt window.

Grinich points to [memory](https://arize.com/blog/memory-is-still-a-missing-primitive-cataloguing-what-the-field-is-actually-shipping) as one of the missing layers.

“Memory is not a key piece” of how MCP works today, he says. Over the next several months, he expects memory to help take “single task-based autonomous agent systems to the next level” so they can become “long running and continuously improving.”

“That memory layer will be kind of like your secret sauce at every company,” he says.

For developers, that’s worth sitting with.

An agent without memory can complete a task. But an agent with the right memory can improve the loop around the task.

Memory also becomes a surface area for security, governance, and evaluation. What should an agent remember? Who can inspect that memory? When should it expire? How do you stop stale assumptions from compounding across runs? How do you prevent yesterday’s workaround from becoming tomorrow’s policy?

A [self-improving agent loop](https://arize.com/blog/building-ai-factory-self-improving-agents-arize-ax/) sounds magical until you remember that “self-improving” means the system changes because of what happened before.

That’s powerful. But it’s also risky.

The companies that benefit most from agent memory will be the ones that know what is worth remembering, what must be forgotten, and how to evaluate the difference.

**What AI engineers build now**

Near the end of the conversation, we asked Grinich to finish a sentence: “An AI engineer is someone who…”

His answer wasn’t about a model, framework, or programming language.

“An AI engineer is someone who is changing what they’re doing every week it seems,” he says.

That may be the most honest definition right now.

Software used to be built mostly for humans to operate. Now it also has to be built for software that operates software: agents that can be spawned in seconds, act across systems, carry memory, pursue goals, and find loopholes no one wrote down.

That requires a different kind of engineering judgment.

You have to think in prompts, but also in permissions. You have to care about UX, but also agent experience. You have to design evals that can’t be gamed by the system being evaluated. And you have to decide when autonomy is useful, when approval is necessary, and when the safest thing an agent can do is stop.

Grinich says he often gets questions about who organizations should hire to teach them how to use AI.

His answer was blunt: “Nobody.”

That’s because the field is moving too quickly for passive learning to be enough.

Great AI engineers, he says, are “constantly learning, constantly figuring out what the job is evolving and changing.” They are willing to “throw away old ideas and pursue new things very quickly.”

That may be the defining trait of the role: not knowing the one right abstraction, but noticing when the abstraction has stopped working.

The rise of the AI engineer signals the rise of engineers who can build feedback loops around non-human actors: systems that know who the agent is, what it’s allowed to do, whether it actually helped, what it should remember, and when its version of success is really a bug.

**Start with one agent run**

Before you add another tool, model, or prompt, look at one agent run end to end.

Who was the agent acting as? What was it allowed to touch? How did it know it had succeeded? Could you replay the path? What did it remember afterward?

That is where AI engineering starts: not with the prompt, but with the system around the agent.

You can also [watch the full Rise of the AI Engineer episode with Michael Grinich](https://www.youtube.com/watch?v=ev89dX1SmI0) for a deeper look at what changes when agents become users.
