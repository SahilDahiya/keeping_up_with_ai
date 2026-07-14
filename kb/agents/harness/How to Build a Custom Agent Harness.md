---
title: How to Build a Custom Agent Harness
topic: agents
subtopic: harness
secondary_topics:
- product-engineering/architecture
summary: Guide to building a custom agent harness, covering control loop design, state,
  tools, observability, and evaluation hooks.
source: langchain
url: https://www.langchain.com/blog/how-to-build-a-custom-agent-harness
author: Sydney Runkle
published: '2026-06-03'
fetched: '2026-07-11T04:40:17Z'
classifier: codex
taxonomy_rev: 1
words: 926
content_sha256: e0523f975b7de1e1a42f5bc34f4741314754ea7381af23ac48b4ac3a3da0d78f
---

# How to Build a Custom Agent Harness

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/6a2035adfcf624bfe1b4fd22_94%20(1).png)

## Key Takeaways

- A harness is the scaffolding around the model that connects it to the real world.
- How well a harness fits the task at hand determines how useful an agent is.
- LangChain's `create_agent`is the easiest way to build a custom harness tailored to a given task.


Building useful agents is largely about *customization:* connecting your agent to the right context, data, and environment(s) for the task at hand.

At its core, an agent is a model calling tools in a loop until it completes a task and returns a result:

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/6a2030b364751b0b7b69bd2d_Screenshot%202026-05-26%20at%203.38.24%E2%80%AFPM.png)

You can also define an agent as:

agent = model + harness

The harness is the scaffolding around the model that connects it to the real world.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/6a2030d9edf4c6cf5969df53_Screenshot%202026-06-01%20at%2010.22.02%E2%80%AFAM.png)

The remainder of this post assumes the following:

- An agent is only as good as the context provided to the model
- The job of a harness is to provide context to the model at every step

So, to build a useful agent, you need a harness that’s great at delivering the right context for the given task to the model.

## The base harness

`create_agent` is LangChain's primitive for building a harness. Pass in a model, tools, and a system prompt, and you have a working agent:

```
from langchain.agents import create_agent
agent = create_agent(
    model="anthropic:claude-sonnet-4-6",
    tools=tools,
    system_prompt="you are a helpful assistant..."
)
```
Harnesses like [Deep Agents](https://docs.langchain.com/oss/python/deepagents/overview) and the [Claude Agent SDK](https://code.claude.com/docs/en/agent-sdk/overview) come pre-assembled with an opinionated middleware (explained below) stack: memory, context management, sandboxing, and more. They're designed to get you to a production-ready agent fast, and they work well for most cases. But many agents need finer grained customization than these harnesses support: custom prompting, business logic, guardrails, etc.

`create_agent` takes a different approach: it’s *purposefully minimalistic*. Our philosophy is similar to that of [Pi](https://pi.dev/), a highly configurable coding agent harness. `create_agent` just implements the core agent loop, and it exposes **middleware** as a primitive for customization.

## Middleware: how you customize the harness

Middleware hooks into the agent loop at each step: before and after model calls, before and after tool calls, at agent startup and teardown. Each piece handles one concern and composes freely with any other:

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/6a203176250a89bbc45c8bf0_Screenshot%202026-05-26%20at%208.24.17%E2%80%AFAM.png)

Middleware allows you to add **capabilities** to your agent via a few levers that often work together:

**Deterministic Logic.** Business logic, policy enforcement, dynamic agent control — anything that needs to fire at a specific point in the loop. This includes runtime control over the agent itself: swapping the model based on task complexity, adjusting the prompt, and updating the agent’s message history (during compaction, for example). The right place for anything that can't (or shouldn't) live in a prompt.

**Tools.** Rather than registering tools directly on the agent, middleware can handle the full lifecycle — setup, teardown, registration — and hand the agent a clean set of tools to work with. This matters when tools have dependencies, require initialization, or need to be torn down cleanly at the end of a run. It also keeps tool configuration close to the logic that governs it, rather than scattered across the agent definition.

**Custom state.** If your middleware needs to track state across hooks, middleware can extend the agent’s state with custom properties. This enables middleware to track state throughout execution (maintain counters, flags, or other values that persist throughout agent runs) and share data between hooks.

**Stream handlers.** Middleware can intercept and transform the agent's output stream — filtering events, injecting metadata, routing different event types to different consumers. Useful when different parts of your stack need to react to different things the agent does: a UI consuming token deltas, an audit log capturing tool calls, a monitoring system tracking latency.

The beauty of middleware is that it:

- Enables customization at any point in the agent loop
- Bundles related logic in composable, sharable units of code

LangChain ships [prebuilt middleware](https://docs.langchain.com/oss/python/langchain/middleware/built-in) for the most common patterns. Anything bespoke to your use case is one [custom middleware](https://docs.langchain.com/oss/python/langchain/middleware/custom) away. Because each piece is isolated, the same middleware can be reused across every agent in an organization so that new agents inherit battle-tested behavior without rebuilding it.

## Harness capabilities

The job of a harness is to get the model the right context at the right time for the given task.

The table below maps common capabilities to middleware that support them. Most production agents end up using several together, depending on the agent’s needs (is it long running? how complex are the tasks? how sensitive are the agent’s actions?, etc):

See the full list of prebuilt middleware [here](https://docs.langchain.com/oss/python/langchain/middleware/built-in).

## Task-harness fit

Task-harness fit is how well your harness matches the actual demands of the task: the context it needs, the failures it'll encounter, the policies it must enforce, the environment it operates in. A harness for a customer service agent looks very different from one built for a long-running coding agent.

Every agent we build at LangChain, including our [GTM agent](https://www.langchain.com/blog/how-we-built-langchains-gtm-agent), [asynchronous coding agent](https://github.com/langchain-ai/open-swe), and our [no-code agent builder](https://www.langchain.com/langsmith/fleet), is built on `create_agent` with a middleware stack tailored to that agent’s mission.

The best agents aren't just built with capable models, they're built with harnesses that tightly fit the task. The easiest way to build a custom harness is with `create_agent`.

## References

### Get Started

- [Quickstart: build your first agent with](https://docs.langchain.com/oss/python/langchain/quickstart)- `create_agent`
- `create_agent`guide
- [Middleware reference](https://docs.langchain.com/oss/python/langchain/middleware/built-in)
- [Custom middleware guide](https://docs.langchain.com/oss/python/langchain/middleware/custom)
- [Deep Agents: a production harness built on](https://docs.langchain.com/oss/python/deepagents/overview)- `create_agent`

### Acknowledgements

Thanks to [@hwchase17](https://x.com/@hwchase17), [@huntlovell](https://x.com/@huntlovell), [@masondrxy](https://x.com/@masondrxy), and [@Vtrivedy10](https://x.com/@Vtrivedy10) for their thoughtful review and feedback.
