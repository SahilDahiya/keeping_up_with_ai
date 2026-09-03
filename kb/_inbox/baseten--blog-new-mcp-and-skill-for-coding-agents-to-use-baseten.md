---
title: New MCP and skill for coding agents to use Baseten
kind: blog
topic: null
subtopic: null
secondary_topics: []
summary: null
triage: null
skip_reason: null
source: baseten
url: https://www.baseten.co/blog/new-mcp-and-skill-for-coding-agents-to-use-baseten/
author: Marius Killinger; Rachel Rapp
published: '2026-09-02'
fetched: '2026-09-03T06:10:58Z'
classifier: null
taxonomy_rev: 2
words: 1002
content_sha256: 763d7b2942f16e1383d71c5d98d098f0d3e736a7ca5706c9f38c877d70c957c7
---

# New MCP and skill for coding agents to use Baseten

![New MCP and skill for coding agents to use Baseten](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1788187676-baseten-blog-2026-thumbnails-17.png%3Fauto%3Dformat%26fit%3Dcrop%26h%3D630%26w%3D1200&w=3840&q=100)

We launched a remote MCP server and skill so coding agents like Claude Code, Codex, Cursor, Gemini CLI, VS Code, and Windsurf can operate Baseten faster and more efficiently.

## **Agents as first-class Baseten users**

Most Baseten users already write their code with agents. Now, those agents have more tools to operate the Baseten platform: a backend MCP server, a docs MCP server, and a skill to more easily complete tasks like deploying models, checking a deployment's health, and debugging from the logs with stronger safeguards and greater efficiency.

According to our benchmarks (fully documented [here](https://github.com/basetenlabs/baseten-skills/tree/main/evals/baseten)), with MCP, the token usage, cost, and time to complete a task are reduced by 7.5% on average. The reduction goes up to 57% for operation-heavy tasks.

![Wall time and cost (top) as well as pass rate (bottom) across five eval configurations from the baseten-skills benchmark (320 runs across 16 tasks). The two configurations that include the backend MCP (green) both land around 99 seconds and $0.55, while the three without it (gray) range from 107–136 seconds and $0.56 to $0.73. The full kit shows a 7.5% improvement over baseline performance and cost on average, while bringing the acceptance rate up from 89% to 97% (an 8% increase).](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1788365074-graphs-1_updated-1.png%3Fauto%3Dformat%26w%3D1200&w=3840&q=75) Wall time and cost (top) as well as pass rate (bottom) across five eval configurations from the baseten-skills benchmark (320 runs across 16 tasks). The two configurations that include the backend MCP (green) both land around 99 seconds and $0.55, while the three without it (gray) range from 107–136 seconds and $0.56 to $0.73. The full kit shows a 7.5% improvement over baseline performance and cost on average, while bringing the acceptance rate up from 89% to 97% (an 8% increase).

![On backend-heavy tasks, adding the MCP to a skill-loaded agent cuts both wall time and dollar cost roughly in half on operate, overview, debug, and tune categories.](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1788365146-graphs-2_updated.png%3Fauto%3Dformat%26w%3D1200&w=3840&q=75) On backend-heavy tasks, adding the MCP to a skill-loaded agent cuts both wall time and dollar cost roughly in half on operate, overview, debug, and tune categories.

## **The bundle: MCP for the Baseten platform, documentation, and skill**

We’re introducing three separate assets:

- **A backend MCP server at api.baseten.co/mcp.** This wraps the full Baseten REST API: deployments, autoscaling, logs, secrets, training jobs, and more. Point any MCP-compatible agent at it, and the agent gets those tools immediately.
- **A docs MCP server at docs.baseten.co/mcp.** Unauthenticated search over our docs and blog content, so an agent can look something up without you opening a browser tab.*(This existed previously, but now it ships alongside the backend MCP and skill as part of the same one-command setup.)*
- **Skill:** [**basetenlabs/baseten-skills**](https://github.com/basetenlabs/baseten-skills)**.** A Baseten skill that “routes” the agent to the correct resource(s) to use given a situation, like picking an authoring surface ([Truss](https://docs.baseten.co/development/model/overview) ,[custom Docker server](https://docs.baseten.co/development/model/custom-server) ,[engine config](https://docs.baseten.co/examples/overview#engines) ,[Chains](https://docs.baseten.co/development/chain/overview) ), debugging a stuck deployment, tuning autoscaling, and promoting between environments.

An agent with the MCP server and Baseten skill can:

- **Deploy a model from scratch.** The agent creates the deployment, watches the logs, catches errors as they come up, and iterates autonomously.
- **Debug a stuck or crashing deployment.** Point the agent at the deployment, and it pulls logs and deployment state to figure out what's wrong.
- **Tune autoscaling for a traffic spike.** The agent adjusts replica counts and scaling policy based on current load.
- **Manage day-to-day ops.** Answer questions like "Which model is costing me the most?", "How many replicas do I have live right now?", or directly execute commands like "Clean up my broken deployments."

![A simple use case for the Baseten skill and MCP server bundle: debugging a slow deployment.](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1788365212-diagram-1-10.png%3Fauto%3Dformat%26w%3D1200&w=3840&q=75) A simple use case for the Baseten skill and MCP server bundle: debugging a slow deployment.

Every tool is annotated as read-only or mutating, so your harness can gate the ones that change your account.

## **Quickstart**

To install the backend MCP, docs MCP, and skill, run these commands in your terminal:

```
export BASETEN_MCP_KEY=<your-api-key> 
npx skills add basetenlabs/baseten-skills -g -y 
npx add-mcp https://api.baseten.co/mcp -g -y --header "Authorization: Bearer ${BASETEN_MCP_KEY}" 
npx add-mcp https://docs.baseten.co/mcp -n "baseten_docs" -g -y
```
`Baseten_MCP_KEY` key can be any personal Baseten API key; there’s no specific “MCP” key, but we do encourage the creation of separate keys for security reasons.

## **Benchmark results: half the time, half the cost**

Technically, all of this was possible before; an agent could already call the Baseten REST API directly, or write its own scripts to automate a workflow, and plenty of people do exactly that. What the MCP server and skill change is:

- **Discoverability.** The agent gets a self-described set of tools and agent-specific usage instructions, instead of having to read REST API docs cold.
- **Safeguards on write and destructive operations.** Tools are explicitly annotated as read-only or mutating, and your agent harness can enforce policy on top of that annotation, like requiring approval before a scale-down or delete.
- **Lower cost and time to solve the same task** . Our eval benchmarks (fully documented[here](https://github.com/basetenlabs/baseten-skills/tree/main/evals/baseten) , and plotted at the top of this blog) show reductions in token usage and wall time, especially for iteration-heavy tasks.

That said, if a workflow is a long, fixed sequence of steps, a single custom script that bundles the equivalent of several MCP calls can still be faster and cheaper than an agent working through them one tool call at a time. Our MCP and skill are built more for the exploratory, iterative work most people use an agent for, like debugging or tuning.

## **The future will be agentic**

Agents already account for a large share of how developers write and ship code day to day, and we’re dedicated to building the tools to support them in using the fastest, most reliable inference and training.

Baseten Skills is open source at [basetenlabs/baseten-skills](https://github.com/basetenlabs/baseten-skills); contributions and issues are welcome. Full setup instructions, including per-agent configs, live [in our docs](https://docs.baseten.co/agent-setup). Try it out, and let us know what you think!
