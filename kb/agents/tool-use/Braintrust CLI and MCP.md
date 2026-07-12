---
title: Braintrust CLI and MCP
topic: agents
subtopic: tool-use
secondary_topics:
- evals-observability/tracing
summary: Covers Braintrust CLI and MCP support for connecting agent tools, local workflows,
  and observability/eval data into AI development loops.
source: braintrust
url: https://www.braintrust.dev/blog/cli-and-mcp
author: Braintrust Team
published: '2026-04-03'
fetched: '2026-07-11T04:31:53Z'
classifier: codex
taxonomy_rev: 1
words: 716
content_sha256: 08d2a219e0c32911255b6e1d739e2fc1e11d723c35eee0e3a5c8f2a62ab33eaa
---

# Braintrust CLI and MCP

3 April 2026Ornella Altunyan4 min

The classic advice for developer tools has always been to "go where the developers are." The step function with AI coding agents is that they can call and access tools on your behalf, which changes what "going where the developers are" actually means.

CLI and MCP come up a lot in this conversation. A CLI (command line interface) gives you discrete commands to run in a terminal or script. An [MCP](https://modelcontextprotocol.io/) (Model Context Protocol) server lets AI coding agents read, search, and act on a platform's data as part of a conversation.

In practice, the CLI is the stronger foundation. It is reliable, scriptable, and works the same way every time. MCP is useful in narrower contexts, mostly when you want an agent to reason over your data as part of a conversation. Many developers use both as part of their workflow, depending on the moment, and Braintrust supports both.

The [Braintrust CLI ( bt)](https://www.braintrust.dev/docs/reference/cli) is built for terminal-native, scriptable workflows. You can use it to run evals, integrate into CI, query logs with SQL, and manage configuration as code. Coding agents like Claude Code can call

`bt` commands directly, which means you get the same reliability whether you or your agent is driving.- Run evals automatically on every PR or merge with `bt eval`
- Query logs and traces with SQL directly from the terminal
- Compose shell scripts with JSON output and standard piping
- Set up your entire agent workflow, including MCP configuration, with `bt setup`

The CLI is the surface you can trust for repeatable operations. It works the same locally, in CI, and in scripts. Auth is straightforward and you always know exactly what ran.

The [Braintrust MCP](https://www.braintrust.dev/docs/integrations/developer-tools/mcp) connects AI coding tools like Claude Code, Cursor, and VS Code directly to your Braintrust data and docs.

- Ask it to pull the trace from a failing eval row and summarize what went wrong
- Look things up in natural language, like "How do I create a custom scorer?"
- Resolve names, URLs, and IDs to the exact Braintrust object you need

The Braintrust MCP is currently read-only, so it is best for querying and exploring your data from within your editor. It is also a good fit for non-technical users on platforms that support MCP natively, like Claude Cowork or Notion AI.

That said, MCP has real friction today. Re-authentication can be annoying, configuration differs across IDEs, and small breakages are hard to debug. It works best as a complement to the CLI, not a replacement for it.

The CLI is the core of the loop here. Run evals repeatedly as you tweak scorers and prompts locally. Query logs and traces from the terminal, including SQL queries against your data. The tight edit-eval-compare cycle is where most debugging actually happens.

MCP can help with the diagnosis step if you are already in an editor. Ask it to find the worst-performing examples from the last run, pull a trace, or summarize failure modes. But the iteration itself runs through the CLI.

Add [ bt eval](https://www.braintrust.dev/docs/reference/cli) to CI so every PR gets scored before merge. This is squarely CLI territory. It is deterministic, scriptable, and fits naturally into any pipeline.

MCP can help you figure out what to measure and which datasets and scorers to use, but the actual enforcement belongs in CI.

The CLI is often the fastest way to get started, for both humans and agents. Install once, then set up agent workflows (including MCP configuration) with `bt setup`.

From there, most teams keep the CLI as the primary interface and add MCP in their editor for occasional lookups.

**Reach for the  CLI** for most things. Running evals, automating in CI, querying logs, scripting workflows, onboarding. Coding agents can call

`bt` commands directly from your editor too. If you want something repeatable and reliable, this is it.**Reach for  MCP** when you want an agent to reason over your Braintrust data as part of a conversation. It is also worth considering for non-technical users on platforms with native MCP support.

- Install the [CLI](https://www.braintrust.dev/docs/reference/cli)and make`bt eval`part of how you ship.
- Optionally, connect [MCP](https://www.braintrust.dev/docs/integrations/developer-tools/mcp)in your editor for in-context lookups.

With this combination, Braintrust goes from a web app you visit to an engineering system you build with.
