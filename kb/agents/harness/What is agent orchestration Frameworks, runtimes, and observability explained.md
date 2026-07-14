---
title: What is agent orchestration? Frameworks, runtimes, and observability explained
topic: agents
subtopic: harness
secondary_topics:
- evals-observability/tracing
summary: Explains agent orchestration across frameworks, runtimes, and observability
  concerns.
source: arize
url: https://arize.com/blog/what-is-agent-orchestration-frameworks-runtimes-and-observability-explained/
author: Laurie Voss
published: '2026-06-16'
fetched: '2026-07-11T04:56:44Z'
classifier: codex
taxonomy_rev: 1
words: 2440
content_sha256: 9930e0c973e8e323da5e23c9d8144bcbed921fb43ee09d3a239438835d87bbd3
---

# What is agent orchestration? Frameworks, runtimes, and observability explained

If you’ve been on AI Twitter at any point in the last year you have watched the same argument play out about a hundred times. Someone says you should build multi-agent systems. Someone else says you definitely shouldn’t. A third person says it depends. Everyone moves on, nothing is resolved, and the argument restarts a week later under a slightly different topic.

The cleanest version of this happened in June 2025. Within about 48 hours of each other, Walden Yan at Cognition published an essay called [“Don’t Build Multi-Agents”](https://cognition.ai/blog/dont-build-multi-agents) and Anthropic published [“How we built our multi-agent research system”](https://www.anthropic.com/engineering/multi-agent-research-system). Yan argued that multi-agent architectures produce fragile systems because of poor context sharing and conflicting decisions between agents. Anthropic argued that their multi-agent Research feature outperformed a single-agent baseline by more than 90% on certain tasks. Same week. Opposite conclusions. Both from people who obviously know what they’re talking about.

The discourse around this has been less illuminating than you’d hope. Half the takes are “well it depends on your use case” which is true but unhelpful. The other half are partisans for one camp or the other. Almost nobody points out that Cognition and Anthropic are not actually disagreeing about the same thing.

The reason this argument never goes anywhere is that the word “orchestration” is doing too much work. When two people argue about agent orchestration, they are often arguing about three completely different layers of the stack without realizing it. Once you separate them, the entire discourse gets clearer, the Cognition versus Anthropic standoff stops looking like a contradiction, and a recent release from Google ([yes, also confusingly called AX](https://github.com/google/ax); no relation to ours) suddenly makes a lot of sense.

**But first: what is agent orchestration?**

Agent orchestration is the coordination of [AI agent behavior](https://arize.com/blog/llm-observability-for-ai-agents-and-applications/) across three layers:

- Expression (frameworks and control flow)
- Runtime (execution, recovery, durability)
- Observability (tracing, evaluation, debugging)

Most debates about agent orchestration focus on only one of these layers.

**Three layers, not one debate**

When people say “agent orchestration” they could mean any of three different layers, and these layers have very different problems, very different vendors, and very different right answers.

**Layer one is expression.** This is how you write down what your agent does. [LangGraph](https://www.langchain.com/langgraph), [CrewAI](https://crewai.com/), [AutoGen](https://github.com/microsoft/autogen), [Google’s ADK](https://google.github.io/adk-docs/), [Mastra](https://mastra.ai/), [OpenAI’s Agents SDK](https://openai.github.io/openai-agents-python/), the new wave of “deep agents” frameworks. The question this layer answers is: what does my agent’s control flow look like in code? Is it a graph? A state machine? A loop with tools? Hierarchical handoffs? This is where most of the framework discourse lives.

**Layer two is runtime.** This is how your agent actually runs, recovers from failures, resumes after crashes, and persists state across long-running executions. [Temporal](https://temporal.io/). [Restate](https://www.restate.dev/). [Cloudflare Workflows](https://developers.cloudflare.com/workflows/). Microsoft’s [Durable Task](https://learn.microsoft.com/en-us/azure/durable-task/common/what-is-durable-task). [LangSmith Deployment](https://www.langchain.com/langsmith/deployment) (formerly LangGraph Platform). And now [google/ax](https://github.com/google/ax), which is explicit about being a runtime and not a framework — its README literally says it is “agnostic of the framework used to build agents.” The question this layer answers is: when my agent runs for three hours and a worker dies in minute 47, what happens?

**Layer three is observability.** This is how you see what your agents actually did, evaluate whether they did it well, and debug when they didn’t. [Traces, evals, judges, replays](https://arize.com/docs/ax/core-workflows). The question this layer answers is: when the demo works but production doesn’t, how do you find out why?

The Cognition versus Anthropic argument is entirely a layer-one argument. It’s about how to express your agent. Single thread or many threads? Centralized context or distributed? It is interesting and it matters, but it is one debate, in one layer, and the partisans of each side mostly agree about layers two and three. Both Cognition and Anthropic care a lot about context management, both invest heavily in observability, and both assume a robust runtime underneath.

Once you separate the layers, the perpetual orchestration debate becomes much less confusing. You can have opinions about each one independently. The “right” answer at layer one depends entirely on the shape of your task. Layer two is increasingly a solved problem with off-the-shelf options. Layer three is where most teams are still flying blind, and where the research suggests the actual returns are.

**Layer one: the expression debate**

The thing that finally made the Cognition versus Anthropic standoff make sense to me was noticing that they’re optimizing for different task topologies.

Anthropic’s Research agent is broad and parallel. It needs to comb through hundreds of websites quickly. Each subagent can work in isolation on its own slice of the search space, then the supervisor synthesizes. This is embarrassingly parallel work, and a multi-agent fan-out structure makes obvious sense. As Anthropic noted, the tradeoff is that they [burn roughly 15 times the tokens of a normal chat](https://www.anthropic.com/engineering/multi-agent-research-system) — but for research, that’s worth it.

Cognition’s [Devin](https://devin.ai/) is deep and sequential. Writing code requires every step to be informed by every previous step. If you fan out parallel coding agents, they’ll make conflicting decisions about variable names, architectural patterns, and which library to use, and you’ll spend more effort reconciling them than you saved by parallelizing. So Devin keeps a single thread of reasoning with a continuous context.

[Yan’s two principles](https://cognition.ai/blog/dont-build-multi-agents) from the Cognition post are worth quoting because they generalize beyond coding:

- Agents must share full context, including complete agent traces, not just isolated messages.
- Every action carries implicit decisions that can conflict if not properly aligned.

The first principle says: if you’re going to have multiple agents, don’t let them communicate by passing terse messages. They need to see each other’s full reasoning, or they’ll diverge. The second says: agents make a lot of micro-decisions implicitly during execution, and parallel agents will make incompatible micro-decisions you didn’t anticipate.

Notice that neither of these is an argument against multi-agent systems per se. They’re arguments for a particular kind of multi-agent system: one with rich context sharing and aligned decision-making. Anthropic agrees with both principles; they just argue you can satisfy them with careful design. [Harrison Chase made roughly this point](https://www.langchain.com/blog/how-and-when-to-build-multi-agent-systems) about a week after both posts: “despite their opposing titles, I would argue they actually have a lot in common.”

This is why Andrej Karpathy’s framing of context engineering as [“the delicate art and science of filling the context window with just the right information for the next step”](https://x.com/karpathy/status/1937902205765607626) has eaten the field. Cognition’s post argues that context engineering is [“effectively the #1 job of engineers building AI agents”](https://cognition.ai/blog/dont-build-multi-agents) — a phrase Harrison Chase has [adopted and amplified](https://www.linkedin.com/posts/harrison-chase-961287118_the-rise-of-context-engineering-context-activity-7342960325635297281-b3Pg) ever since. Whether you’re team single-agent or team multi-agent, you’re really arguing about how to do context engineering at scale.

The [MAST paper](https://arxiv.org/abs/2503.13657) from UC Berkeley (Cemri et al, NeurIPS 2025) backs this up empirically. The authors analyzed 1,642 execution traces from seven popular multi-agent frameworks — [ChatDev](https://github.com/OpenBMB/ChatDev), [MetaGPT](https://github.com/FoundationAgents/MetaGPT), [HyperAgent](https://arxiv.org/abs/2409.16299), [AppWorld](https://appworld.dev/), [AG2](https://github.com/ag2ai/ag2), [Magentic-One](https://www.microsoft.com/en-us/research/articles/magentic-one-a-generalist-multi-agent-system-for-solving-complex-tasks/), [OpenManus](https://github.com/FoundationAgents/OpenManus) — and found failure rates between 41% and 86.7%. They built a taxonomy of 14 failure modes in three categories: system design issues (41.8%), inter-agent misalignment (36.9%), and task verification (21.3%). Their key finding, which I’ll quote because it’s good: “Successful systems all work alike; each failing system has its own problems.” Most failures are not model limitations. They are organizational design failures. The paper invokes Charles Perrow’s [ Normal Accidents](https://press.princeton.edu/books/paperback/9780691004129/normal-accidents) — failures emerge from how the system is structured, not from the capability of any individual component.

In other words, layer one matters a lot, and you can get it badly wrong. But it’s also not where you’ll find the easy wins anymore. The frameworks have converged on a similar set of primitives (loops, tools, handoffs, supervisors) and the remaining differences are mostly ergonomic.

**Layer two: agents are getting their Kubernetes moment**

Layer two is the most interesting layer to watch right now, and it’s the one that google/ax brings into sharp relief.

For years, “running an agent” meant calling an LLM in a while loop in a Python process. If the process died, the agent died. If the user disconnected, the agent died. If the LLM API hiccuped halfway through a 30-step research task, you either swallowed the error and corrupted state or threw away 29 steps of work. This was tolerable when agents were toys. It is not tolerable when [OpenAI’s Codex is processing millions of coding tasks](https://temporal.io/blog/improving-java-sdk-codex-openai) a day for paying customers.

The runtime layer is what makes long-running, durable, recoverable agents possible. The pattern is borrowed almost wholesale from durable execution systems like [Temporal](https://temporal.io/), which have been doing this for distributed business workflows for years: an event log, deterministic replay, automatic retries, checkpointing, and resumption. The agent’s progress is journaled to durable storage. If the worker dies, another worker picks up exactly where the dead one left off, replaying the event log to reconstruct state.

This is no longer theoretical. [OpenAI Codex runs on Temporal](https://temporal.io/blog/improving-java-sdk-codex-openai) in production. [Replit migrated its agent to Temporal](https://temporal.io/resources/case-studies/replit-uses-temporal-to-power-replit-agent-reliably-at-scale) for reliability. Microsoft’s [durable task extension for the Microsoft Agent Framework](https://techcommunity.microsoft.com/blog/appsonazureblog/bulletproof-agents-with-the-durable-task-extension-for-microsoft-agent-framework/4467122) shipped in late 2025 with explicit support for multi-day human-in-the-loop agent pauses. [Cloudflare Workflows](https://blog.cloudflare.com/workflows-ga-production-ready/) hit GA in 2025 with Python support and step-based durable execution that can run for weeks. LangChain has rebuilt its deployment platform (formerly LangGraph Platform, now [LangSmith Deployment](https://www.langchain.com/langsmith/deployment)) around the same primitives and now [markets it as letting you treat agents like real distributed systems](https://blog.langchain.com/why-langgraph-platform/).

And then [google/ax](https://github.com/google/ax) shipped, and Google’s framing is the cleanest articulation of what’s happening. From the README: “as agents evolve from simple assistants to autonomous long running workers, developers need a robust runtime to manage state, ensure reliability, and audit execution.” They explicitly call out single-writer architecture, event logs with automatic recovery, and resumable bidirectional streams. They explicitly disclaim being a framework or a managed service.

This is the part I find genuinely exciting, because it follows a pattern we’ve seen before in software. Web development went through this in the 2010s: first came the application frameworks (Rails, Django, Express), and once those stabilized people started realizing that the harder problem was the runtime underneath. That’s how we got Kubernetes. Agents are now at the equivalent moment. The frameworks have stabilized enough that the bottleneck has moved to the layer below.

If you’re building an agent that needs to run for more than a few minutes, survive a deploy, or recover from a worker crash, you do not want to be writing your own retry logic and checkpointing. You want a runtime that handles it for you. This is increasingly available off the shelf.

**Layer three: where the actual reliability problem lives**

The thing nobody wants to hear is that none of this matters if you can’t see what your agents are doing.

[Hamel Husain](https://hamel.dev/), who has consulted with 30+ AI teams, opens [his “Field Guide to Rapidly Improving AI Products”](https://hamel.dev/blog/posts/field-guide/) with a scene that has played out for him repeatedly:

AI TEAM: Here’s our agent architecture — we’ve got RAG here, a router there, and we’re using this new framework for…

ME: Can you show me how you’re measuring if any of this actually works? Room goes quiet.

This is the part that ties everything together. Cognition and Anthropic both invest enormous engineering effort in observability because they have to. When your agent fails 50% of the time and the failure modes are subtle — step repetition, role disobedience, reasoning-action mismatch, premature termination — you cannot debug them from the outside. You cannot vibe-check your way to reliability when [the MAST researchers](https://arxiv.org/abs/2503.13657) needed 1,642 annotated traces and grounded theory analysis to figure out what was even going wrong.

The MAST paper is, structurally, a giant argument for [trace-level observability](https://arize.com/docs/ax/observe/tracing). The whole reason the authors could identify those 14 failure modes is that they had complete execution traces. The whole reason their [MAST-Data dataset](https://huggingface.co/datasets/mcemri/MAST-Data) is useful is that other teams can now diagnose their own failure mode distributions and target interventions. A ChatDev agent terminating early gets fixed by giving the CEO agent final say — a 9.4% improvement. Adding a high-level verification step to ChatDev gets 15.6%. Those numbers are only available because someone is looking at the traces.

This is what [AX](https://arize.com/generative-ai/) is for. The argument we’d make is not that you need yet another framework, or that you need to rip out your runtime and start over. It’s that the entire field has now formally documented that [production agents](https://arize.com/blog/building-ai-factory-self-improving-agents-arize-ax/) fail in ways that are invisible from outside, and that the teams winning at this are the ones who built the visibility first. AX is what visibility looks like when it’s built specifically for agents — traces, [evals](https://arize.com/docs/ax/evaluate/create-evaluators), [judges](https://arize.com/docs/ax/evaluate/evaluators/llm-as-a-judge), replay, all designed around how agentic systems actually fail. Not because observability is the most important layer (it isn’t, all three matter) but because it’s the one where the gap between what most teams have and what the leaders have is largest.

**The synthesis**

So when somebody asks you “what do you think about agent orchestration?”, the honest answer is “which part?”

Layer one is the layer where most arguments happen, and most of those arguments are religious wars between people with different task topologies. The Cognition versus Anthropic debate is not actually a debate; it’s two correct answers to two different problems. Pick the structure that fits the shape of your task, do excellent context engineering regardless, and don’t be too precious about which framework you’re using to express it.

Layer two is the layer where the field is maturing fastest. The runtime question — how does your agent survive contact with reality — is being answered by an emerging consensus around durable execution primitives. Whether you’re on Temporal, Restate, LangSmith Deployment, Microsoft’s Durable Task, or eventually google/ax, the shape of the answer is becoming clear. You should probably not be building this from scratch.

Layer three is the layer where the reliability dragons actually live. The research is unambiguous about this: production agents fail at rates between 41% and 86.7%, the failures are organizational rather than model-level, and you cannot fix what you cannot see. This is where the next year of agent engineering progress is going to come from.

And the underlying frame that ties it all together is still [Karpathy’s](https://x.com/karpathy/status/1937902205765607626): the context window is RAM. Everything you’re building — frameworks, runtimes, observability — is operating system plumbing around that single resource. The question is not which framework is the “real” orchestrator. The question is whether you’ve thought clearly about all three layers, or whether you’re picking a fight on one layer because you haven’t yet noticed the other two.

We’re past the moment of arguing about whether to build multi-agent systems. We’re into the moment of running them in production, and finding out what breaks.
