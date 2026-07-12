---
title: Bringing more agent harnesses and frameworks to Cloudflare, starting with Flue
topic: infra-platform
subtopic: deployment
secondary_topics:
- agents/tool-use
summary: Describes a three-layer production agent stack — framework (Flue, from the
  Astro team, built on the Pi harness), harness (Project Think, Pi), and runtime (Cloudflare
  Agents SDK) — with durable execution, dynamic code execution, and a durable filesystem
  exposed to any harness.
source: cloudflare-ai
url: https://blog.cloudflare.com/agents-platform-flue-sdk/
author: Thomas Gauvin
published: '2026-06-17'
fetched: '2026-07-11T04:12:54Z'
classifier: claude
taxonomy_rev: 1
words: 2024
content_sha256: ab97416cc0afc6d4f7cbe286144bff6787163e80cc950fa1b0ec5971bb5673d9
---

# Bringing more agent harnesses and frameworks to Cloudflare, starting with Flue

2026 is the year agent harnesses go to production. The software that controls the model’s access to the outside world — harnesses like Codex, Claude Code, OpenCode, Pi, and Project Think — has matured to the point where teams are deploying agents as real, load-bearing infrastructure, not just prototypes.

But building agents that survive production is hard.

We learned this firsthand building [ Project Think](https://blog.cloudflare.com/project-think/) as our first-party agent harness. In working with our customers to run agents in production, we found a common set of distributed systems problems that every agent faces when running in the cloud. When an agent is interrupted, how can it automatically and gracefully resume from where it left off, without losing context or wasting tokens? How can agents run untrusted code securely? How can agents use the tools they were trained for?

A harness can’t solve these problems on its own. They’re tied to state, storage and compute — which means they’re dependent on the platform the agent runs on. That’s why we’re taking our learnings from hardening [ Project Think](https://blog.cloudflare.com/project-think/) for production and bringing them to the

[as a base layer. Durable execution, dynamic code execution, a durable filesystem and dynamic workflows, now available to any harness building on Agents SDK.](https://developers.cloudflare.com/agents/)

__Cloudflare Agents SDK__At the same time, a new layer has emerged above the harness. Frameworks like [Flue](https://flueframework.com/) wrap a harness with the project structures, conventions, integrations and developer experience that make agents productive to build.

To solve these scaling challenges, there’s a new, three-layer stack that is emerging for building production-grade AI. Here is how the pieces fit together, moving from the user-facing developer experience down to the underlying platform primitives:

- **The framework (Flue)**— the project structure, the conventions, the integrations, the CLI and the developer experience for building agents.
- **The harness**- **(Pi, Project Think)**— the agentic loop that calls tools, reads results, manages context and keeps going until the task is done.
- **The runtime/platform**- **(the Cloudflare Agents SDK)**— the compute, state, and storage primitives everything above depends on

The Agents SDK is that bottom layer: it makes primitives like durable execution available to any harness and any framework. Flue, our new open-source framework from the team behind [ Astro](https://astro.build/), is the first to build on it. Here’s how.

[ Flue](https://flueframework.com/) shipped 1.0 Beta this week, built on the

[harness, the same harness that](https://pi.dev/)

__Pi__[is built on. What makes it different as an agent framework is the approach: you don’t script what your agent does, you describe what it knows. Define the context an agent needs — its model, skills, sandbox, and instructions — and it solves whatever task you give it, autonomously. There’s no orchestration loop to write.](https://openclaw.ai/)

__OpenClaw__This declarative model is what makes writing agents easy: here’s a triage agent that intercepts a bug report, reproduces it in a sandbox, and diagnoses the issue in under 25 lines.

Flue’s power comes from the fact that agents don’t live in isolation. They are built to exist where your users already work, and integrate with your preferred tooling:

- **Anywhere agents**: Drop your agents into Slack, GitHub, Linear, or Discord with pre-configured Channels that handle event verification and dispatch boilerplate automatically.
- **Headless, but UI-ready**: Agents shouldn’t live in a black box. Flue agents can run completely headlessly for background tasks, but- __@flue/react__
- **Ecosystem-ready**: Flue makes it easy to add and upgrade integrations with commands like- `flue add channel slack`, generating a Markdown blueprint that your own coding agent can read, modify, and cleanly integrate straight into your codebase.

Moving an agent out of a local terminal and into a production ecosystem introduces traditional distributed systems failures. Host crashes, API timeouts from LLM providers, and unexpected restarts threaten to erase the short-term memory of a running agent turn.

Flue solves this via Durable Streams. Each event in the execution history is added to an append-only log. By processing every prompt, tool response and model choice as an unchangeable ledger, an agent’s state is never volatile. If a process dies, another simply picks up the log and continues from the exact step it left off.

Flue is a multi-cloud framework. On [ Node.js](http://node.js), each agent runs as a long-lived process. You can deploy it to any VM or container, run it in GitHub Actions, or embed it on an existing server. But when you target Cloudflare, each agent becomes a Durable Object.

By running each Flue agent inside its own Durable Object, Cloudflare can automatically scale to as many agents as you need, each with their own isolated storage and compute. You don’t have to provision servers, manage sticky sessions, or worry about noisy neighbors. And when Flue agents are deployed to Cloudflare, they get durable execution using Agents SDK’s `runFiber()`, `stash()`, and `onFiberRecovered()` methods. Flue also uses `@cloudflare/codemode` and `@cloudflare/shell` for sandboxed code execution against a durable workspace.

Flue’s Cloudflare target works so effectively because it maps cleanly to the core primitives we built into the Agents SDK. You can even [ dig into the Flue source code](https://github.com/withastro/flue/blob/0fd59475d303d8e8d5bc184a9d3fc4ed58c0de93/packages/runtime/src/session.ts#L13) to understand how Pi, the underlying harness, is adapted to work on Cloudflare Agents SDK.

Here’s how Flue leverages the Agents SDK under the hood, and what it takes to run any modern agent harness reliably at scale.

An agent turn is not a single request. The model streams tokens, calls tools, waits for results, maybe asks a human for approval, or delegates work to a subagent. That sequence can take seconds or minutes, and at any point the process can be interrupted or crash. When that happens, all of the agent state that was in memory is gone: the streaming connection, the pending tool calls, where the agent was in its turn. Sure, the conversation history is persisted on disk, but the user sees a spinner that never resolves. That’s a broken user experience.

[ Fibers](https://developers.cloudflare.com/agents/runtime/execution/durable-execution/) solve this problem by providing a native checkpointing mechanism directly inside the Agent’s underlying

[.](https://developers.cloudflare.com/durable-objects/)

__Durable Object__`runFiber()` records the progress to the Durable Object’s SQLite storage before the work in the Agent turn starts and checkpoints with `stash()` as the turn advances. When a fresh agent instance boots after an interruption, `onFiberRecovered()` delivers the last checkpoint, so your agent knows a turn was interrupted, where it got to, and can decide how to continue. ```
import { Agent } from "agents";
import type { FiberRecoveryContext } from "agents";
class MyAgent extends Agent {
  async doWork() {
    await this.runFiber("my-task", async (ctx) => {
      const step1 = await expensiveOperation();
      ctx.stash({ step1 });
      const step2 = await anotherExpensiveOperation(step1);
      this.setState({ ...this.state, result: step2 });
    });
  }
  async onFiberRecovered(ctx: FiberRecoveryContext) {
    if (ctx.name !== "my-task") return;
    const { step1 } = (ctx.snapshot ?? {}) as { step1?: unknown };
    if (step1) {
      const step2 = await anotherExpensiveOperation(step1);
      this.setState({ ...this.state, result: step2 });
    }
  }
}
```
Flue uses `runFiber()` [ on its Cloudflare target](https://github.com/withastro/flue/blob/cf775a84e7cf1d7037a464b947d8b2f7e9efcfd1/packages/runtime/src/cloudflare/agent-coordinator.ts#L475) for exactly this. With the

`onFiberRecovered()` hook, your harness can decide how to resume the execution of the turn, whether it attempts a full reconstruction model like Project Think that repairs turn state or whether it replays certain parts of the turn. Agent harnesses give models access to the outside world through tools. But tool surfaces grow fast, and models get worse at selecting the right tool as the list gets longer and the context window fills up with tool definitions. A better pattern: give the model one tool that executes code. The model writes a TypeScript function that calls the APIs it needs, and the harness runs it. We wrote about this when we introduced [ Code Mode](https://blog.cloudflare.com/code-mode).

The question is where that code runs. To run LLM-generated code securely, you need a sandbox. But typical sandboxes would be slow, cost-prohibitive and inefficient to run each tool call. That’s why the Agents SDK provides

__@cloudflare/codemode__

[, to execute LLM-generated code in its own Worker isolate with only the bindings you provide.](https://developers.cloudflare.com/dynamic-workers/)

__Dynamic Workers__Code Mode creates a fresh Dynamic Worker for each snippet, runs it, and discards it. Isolates start in under 10ms and $0.002 per load, resulting in drastically faster and cheaper cost of execution than booting a container every time your agent needs to execute a short piece of code. Flue uses

__@cloudflare/codemode__

Agent harnesses often need a filesystem, whether it’s to read files, write outputs, search through code and understand diffs. Coding agents in particular live in the filesystem. But if the harness is running in a serverless environment, how can it get a durable filesystem that persists across executions?

The usual answer is a container. That works, but it’s expensive for what agents mostly do. The majority of filesystem operations in an agent turn are text. Consider a review agent that reads files, greps through source code, or perhaps writes a patch. You don’t need a full Linux boot for that.


__@cloudflare/shell__

Instead of calling individual tools, a Flue agent running on the Cloudflare target writes JavaScript against the workspace virtual file state API. By running more operations within the Durable Object, the agent benefits from the isolate model’s more efficient execution process, entirely avoiding container overhead:

```
async () => {
  const files = await state.glob("src/**/*.ts");
  const results = [];
  for (const file of files) {
    const content = await state.readFile(file);
    const todos = content.match(/\/\/ TODO:.*/g);
    if (todos) results.push({ file, todos });
  }
  return results;
}
```
This translates into a faster and more cost-efficient sandbox environment for agents that need to run shell and filesystem operations to get their work done. And for agents that need a full OS, to run npm install, git, or compilers, Cloudflare Containers provides that. We’re also building

__@cloudflare/workspace__

But what happens when an agent needs to do more than read files or execute single code snippets? What happens when it needs to orchestrate a massive, multi-step pipeline that must repeat consistently over time, like a code review that successfully resolves bugs or a research workflow that produces good results? A harness can’t provide durable multi-step execution on its own. It needs the platform to persist each step, retry failures, and resume after interruptions.

This pattern is gaining traction. Claude Code recently shipped [ dynamic workflows](https://code.claude.com/docs/en/workflows), where Claude writes a JavaScript script at runtime to hand off work to dozens of subagents, and the runtime executes it durably.

[provides this for any harness running on the Agents SDK. Your agent generates a workflow at runtime, and the Workflows engine persists each step, retries failures, and can sleep for hours or wait for external events like human approval.](https://developers.cloudflare.com/dynamic-workers/usage/dynamic-workflows/)

__@cloudflare/dynamic-workflows__From the Agent class, `runWorkflow()` connects your agent to the [ Workflows](https://developers.cloudflare.com/workflows/) engine. The agent kicks off the workflow and can go to sleep. The workflow calls back into the agent via RPC to report progress, update state, or request approval. When the workflow finishes, the agent wakes up with the result.

Beyond compute and storage, agent harnesses need access to external capabilities: web browsing, email, memory, search, inference. A harness shouldn't have to integrate each of these separately, manage API keys for each, or worry about credentials leaking through agent-generated code.

The Agent class gives your harness access to the rest of Cloudflare through [ bindings](https://developers.cloudflare.com/workers/runtime-apis/bindings/):

[for per-agent spend tracking and limits,](https://developers.cloudflare.com/ai-gateway/)

__AI Gateway__[for web automation,](https://developers.cloudflare.com/browser-rendering/)

__Browser Run__[for inbox workflows,](https://developers.cloudflare.com/email-service/)

__Email Service__[for persistent recall,](https://developers.cloudflare.com/agents/api-reference/agent-memory/)

__Agent Memory__[for retrieval,](https://developers.cloudflare.com/ai-search/)

__AI Search__[for workloads that need a full OS, and inference across](https://developers.cloudflare.com/containers/)

__Containers__[. Bindings grant capabilities without exposing credentials: your agent uses them, but the keys never enter agent-generated code.](https://blog.cloudflare.com/ai-platform/)

__14+ model providers__We know this approach works because it is the exact architectural foundation we used to build [ Project Think](https://blog.cloudflare.com/project-think/), our first-party agent harness. While Project Think remains our highly optimized, out-of-the-box solution for native Cloudflare agent experiences, the Agents SDK ensures that the broader open-source ecosystem can leverage those exact same battle-tested primitives, including Flue.

If you're building agents today with Flue, you can deploy in just a few clicks to Cloudflare. And if you're building your own agent harness or you’re building an agent framework, target the Agents SDK and get the platform integration for free.

- Agents SDK: - __developers.cloudflare.com/agents__
- Think: - __docs__
- Cloudflare Community: - __community.cloudflare.com__
