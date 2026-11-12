---
title: New MCP and skill for coding agents to use Baseten
kind: blog
topic: agents
subtopic: tool-use
secondary_topics:
- evals-observability/evaluation
summary: Describes Baseten's MCP server and coding-agent skill for operating its platform,
  benchmarked across 320 runs/16 tasks to show a 7.5% average cost/time reduction
  (up to 57% on operation-heavy tasks) and acceptance rate rising from 89% to 97%.
triage: null
skip_reason: null
source: baseten
url: https://www.baseten.co/blog/new-mcp-and-skill-for-coding-agents-to-use-baseten
author: Marius Killinger
published: '2026-11-01'
fetched: '2026-11-12T06:06:44Z'
classifier: claude
taxonomy_rev: 2
words: 968
content_sha256: 0b30d87f417480ef038ac3329474d628ca0cf205e825bb0bcf505c68ace294a6
---

# New MCP and skill for coding agents to use Baseten

AI engineering
# New MCP and skill for coding agents to use Baseten

The Baseten MCP server and skill cut agent task time and cost by 7.5% on average, and by roughly 50% for backend-heavy tasks.


- Authors
- Date
- November 1, 2026

TLDR

We launched a remote MCP server and skill so coding agents like Claude Code, Cursor, VS Code, Codex, Gemini CLI, and Windsurf can operate Baseten faster and more efficiently.

Most Baseten users already write their code with agents. Now, those agents have more tools to operate the Baseten platform: a backend MCP server, a docs MCP server, and a skill to more easily complete tasks like deploying models, checking a deployment's health, and debugging from the logs with greater safeguards and efficiency.

According to our benchmarks (fully documented [here](https://github.com/basetenlabs/baseten-skills/tree/main/evals/baseten)), with MCP, the token usage, cost, and time to complete a task are reduced by 7.5% on average. The reduction goes up to 57% for operation-heavy tasks.

*Wall time and cost (top) as well as pass rate (bottom) across five eval configurations from the baseten-skills benchmark (320 runs across 16 tasks). The two configurations that include the backend MCP (green) both land around 99 seconds and $0.55, while the three without it (gray) range from 107–136 seconds and $0.56–$0.73. The full kit shows a 7.5% improvement over baseline performance and cost on average, while bringing the acceptance rate up from 89% to 97% (an 8% increase).*

*On backend-heavy tasks, adding the MCP to a skill-loaded agent cuts both wall time and dollar cost roughly in half on operate, overview, debug, and tune categories.* 

**The bundle: MCP for the Baseten platform, documentation, and skill**

We’re introducing three separate assets:

- **A backend MCP server at api.baseten.co/mcp.** This wraps the full Baseten REST API: deployments, autoscaling, logs, secrets, training jobs, and more. Point any MCP-compatible agent at it, and the agent gets those tools immediately.
- **A docs MCP server at docs.baseten.co/mcp.** Unauthenticated search over our docs and blog content, so an agent can look something up without you opening a browser tab. *(This existed previously, but now it ships alongside the backend MCP and skill as part of the same one-command setup.)*
- **Skill: basetenlabs/baseten-skills.** A baseten skill that “routes” the agent to the correct resource(s) to use given a situation, like picking an authoring surface ([Truss](https://docs.baseten.co/development/model/overview), [custom Docker server](https://docs.baseten.co/development/model/custom-server), [engine config](https://docs.baseten.co/examples/overview#engines), [Chains](https://docs.baseten.co/development/chain/overview)), debugging a stuck deployment, tuning autoscaling, and promoting between environments.

An agent with the MCP server and Baseten skill can:

- **Deploy a model from scratch.** The agent creates the deployment, watches the logs, catches errors as they come up, and iterates autonomously.
- **Debug a stuck or crashing deployment.** Point the agent at the deployment, and it pulls logs and deployment state to figure out what's wrong.
- **Tune autoscaling for a traffic spike.** The agent adjusts replica counts and scaling policy based on current load.
- **Manage day-to-day ops.** Answer questions like "Which model is costing me the most?", "How many replicas do I have live right now?", or directly execute commands like "Clean up my broken deployments."

*A simple use case for the Baseten skill and MCP server bundle: debugging a slow deployment.*

Every tool is annotated as read-only or mutating, so your harness can gate the ones that change your account.

To install the backend MCP, docs MCP, and skill, run these commands in your terminal:

bash

```
export BASETEN_MCP_KEY=<your-api-key> 
npx skills add basetenlabs/baseten-skills -g -y 
npx add-mcp https://api.baseten.co/mcp -g -y --header "Authorization: Bearer ${BASETEN_MCP_KEY}" 
npx add-mcp https://docs.baseten.co/mcp -n "baseten_docs" -g -y
```
`Baseten_MCP_KEY` key can be any personal Baseten API key; there’s no specific “MCP” key, but we do encourage the creation of separate keys for security reasons.

Technically, all of this was possible before; an agent could already call the Baseten REST API directly, or write its own scripts to automate a workflow, and plenty of people do exactly that. What the MCP server and skill change is:

- **Discoverability.** The agent gets a self-described set of tools and agent-specific usage instructions, instead of having to read REST API docs cold.
- **Safeguards on write and destructive operations.** Tools are explicitly annotated as read-only or mutating, and your agent harness can enforce policy on top of that annotation, like requiring approval before a scale-down or delete.
- **Lower cost and time to solve the same task**. Our eval benchmarks (fully documented [here](https://github.com/basetenlabs/baseten-skills/tree/main/evals/baseten), and plotted at the top of this blog) show reductions in token usage and wall time, especially for iteration-heavy tasks.

| Configuration | Pass rate | Wall time (sec) | Cost ($) | 
|---|---|---|---|
| Model (no skill, MCP, or docs) | 0.89 | 107 | 0.56 | 
| + docs MCP | 0.85 | 110 | 0.66 | 
| + docs MCP + skill | 0.87 | 136 | 0.73 | 
| + docs MCP + Baseten MCP | 0.91 | 99 | 0.54 | 
| + docs MCP + Baseten MCP + skill (full kit) | 0.97 | 99 | 0.55 | 

That said, if a workflow is a long, fixed sequence of steps, a single custom script that bundles the equivalent of several MCP calls can still be faster and cheaper than an agent working through them one tool call at a time. Our MCP and skill are built more for the exploratory, iterative work most people use an agent for, like debugging or tuning.

Agents already account for a large share of how developers write and ship code day to day, and we’re dedicated to building the tools to support them in using the fastest, most reliable inference and training.

baseten-skills is open source at [basetenlabs/baseten-skills](https://github.com/basetenlabs/baseten-skills); contributions and issues are welcome. Full setup instructions, including per-agent configs, live at [docs.baseten.co/ai-tools](http://docs.baseten.co/ai-tools.Try). Try it out, and let us know what you think!
