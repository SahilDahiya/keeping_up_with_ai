---
title: AI that knows your data
topic: agents
subtopic: tool-use
secondary_topics:
- rag-retrieval/search
summary: Discusses MCP-style access to data and tools so AI systems can retrieve context
  and act against application-specific resources.
source: braintrust
url: https://www.braintrust.dev/blog/mcp
author: Braintrust Team
published: '2025-09-09'
fetched: '2026-07-11T04:32:57Z'
classifier: codex
taxonomy_rev: 1
words: 444
content_sha256: 15fcfa7599ec290172ee9b29b926ada28c10fa9c49c2bdd1eeeabf415ff2b056
---

# AI that knows your data

13 September 2025Ornella Altunyan3 min

Your AI tools should know about your Braintrust experiments. They should understand your log schemas, help debug failed evaluations, and answer questions about your model performance.

Today, we're introducing Braintrust's [Model Context Protocol (MCP)](https://modelcontextprotocol.io/) server. MCP is Anthropic's open standard that lets AI tools securely access external data sources. We've built an MCP server that exposes your Braintrust data and works seamlessly with popular AI coding tools to provide better access and help you discover insights about your app's structure and performance.

Building and evaluating AI applications means constantly jumping between tools like your code editor, the Braintrust UI, various documentation, and more.

Without proper tooling, each context switch breaks your flow. The tools that should be helping you debug and improve your product might have no idea what experiments you're running in Braintrust or how they're performing. This means building custom evaluation infrastructure from scratch.

With our MCP integration, your AI tools of choice become aware of your Braintrust projects, experiments, and data. You can now:

**Query experiments naturally**: "What were the accuracy scores for my recent sentiment analysis experiments?" Get instant answers from your data.

**Debug failures in context**: "Show me examples where my model failed on edge cases." See specific data points and understand what went wrong.

**Get contextual documentation**: "How do I create a custom scorer?" Find relevant examples based on your current project.

**Compare model performance**: "Compare GPT-5 vs Claude 4 Sonnet performance on my customer support dataset." Run analysis and get explanations automatically.

We support the most popular AI coding tools:

- **Cursor**: One-click setup via our- [documentation](https://www.braintrust.dev/docs/reference/mcp)
- **Claude Code**:- `claude mcp add --transport http braintrust https://api.braintrust.dev/mcp`
- **VS Code**: Works with GitHub Copilot
- **Windsurf**: Simple JSON configuration

Authentication is handled via OAuth 2.0 with your existing Braintrust account. If you're using SSO, it works with that too. For self-hosted instances, the MCP server runs within your environment, so your data never leaves your infrastructure.

Once connected, your AI assistant gains access to the following tools:

- **Documentation search**: Semantic search across all Braintrust docs
- **Object resolution**: Convert between names and IDs for experiments, datasets, and projects
- **Recent objects**: Browse your latest experiments and datasets
- **Schema analysis**: Understand your data structure with- `infer_schema`
- **BTQL queries**: Execute complex analyses using Braintrust query language
- **Experiment summaries**: Get high-level performance overviews
- **Permalink generation**: Create shareable links to results

With Braintrust's MCP, your AI assistant finally understands your context. It knows your projects and data without explanations, accesses experiment results directly, and runs performance comparisons automatically.

[Get started with MCP](https://www.braintrust.dev/docs/reference/mcp) and let your AI assistant join your evaluation workflow.
