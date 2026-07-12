---
title: LLM Eval Driven Development with Claude Code
topic: evals-observability
subtopic: evaluation
secondary_topics:
- agents/tool-use
summary: Explains eval-driven development with Claude Code, using tests and feedback
  loops to improve coding-agent behavior.
source: fireworks
url: https://fireworks.ai/blog/eval-driven-development-with-claude-code
author: null
published: '2025-08-25'
fetched: '2026-07-11T04:14:47Z'
classifier: codex
taxonomy_rev: 1
words: 1100
content_sha256: ba7ae4f35ca55f34e03f841c7e34a8e223510c502c830b87b8f0d623e55bed4d
triage: keep
skip_reason: null
---

# LLM Eval Driven Development with Claude Code

In [our previous blog](https://fireworks.ai/blog/test-driven-agent-development), we showed how to go from one test to many tests with **Eval Protocol** with Cursor. But what if you're starting from scratch?

Today, with Claude Code supercharged by MCP servers pointing directly to our docs and a deep wiki, we'll show you how to go from 0 to 1. In other words, from a completely blank project to your first fully tested AI agent.

To recap the core idea from the previous blog, we're adapting the classic software engineering practice of **Test-Driven Development (TDD)** to use evals in the era of LLMs. The idea is simple: you write evals that define the desired behavior before writing the actual code, and then build your agent to pass them. This post will demonstrate how applying a TDD workflow ensures that as you add new features or swap out models, you have a safety net to prevent regressions.

To give our AI agent the context it needs about Eval Protocol by Fireworks AI, we're leveraging Model Context Protocol (MCP) servers. These act as secure bridges, allowing the agent to access external data sources.

With Claude Code, you can easily add these servers directly from the command line:

12

The first link is an MCP server that points to our documentation, and the second link is an MCP server that points to our GitHub repository of our open-source implementation of Eval Protocol. These MCP servers give Claude the ability to "read the manual.”

Alternatively, you can use an `mcp.json` file. This is a commonly used format that other MCP clients, like Cursor, can also use, making your configurations portable across different tools.

12345678910

This simple addition is a game-changer, as it grounds the agent in the specific documentation relevant to our task.

With our environment enhanced, the next step is to give Claude Code its mission. We start with a general prompt that defines its role and how to use Eval Protocol. Below that, we append the specific instructions for our project, which are copied over from our [previous blog's prompt](https://fireworks.ai/blog/test-driven-agent-development#setup-in-minutes-vibes-cursor-eval-protocol). This "meta-prompting" is crucial for guiding the agent effectively.

Here is the initial prompt we'll use with Claude Code:

You are an applied AI engineer whose job is to write tests called "evals" in the form of code. An "eval" helps determines whether an AI application is working as expected by programmatically assessing the output of the model. To do this, you will use a library called "eval-protocol" (aka EP) that helps you easily author, run, and review evals. Evals accept whats called an EvaluationRow and outputs an EvaluationRow (or multiple EvaluationRows depending on the mode of the @evaluation_test decorator). In the eval, a score from 0 to 1 is generated based on the output of the model. Use the provided tools to help you understand more about eval-protocol so that you can generate evals for the given task. The tools can help provide examples of evals, guide you with tutorials on how to use eval-protocol, retrieve reference documentation for the eval-protocol API, and ask questions about the source code of eval-protocol.

GitHub source repos:

- for the docs, see eval-protocol/eval-protocol

- for the Python SDK, see eval-protocol/python-sdk

Please follow the below instructions to write our evals:

`project.md` is something I want to work on, I want you to use EP to create the application. We want to use `https://github.com/lerocha/chinook-database` has the database info, please use `https://github.com/gldc/mcp-postgres` for the setup, then let's setup the project with the MCP server, and then use Eval Protocol to test at least 1 simulated user to check if the project is working end to end, thanks!

To be clear, you would add your own instructions as the last paragraph. This prompt does several key things:

- **Assigns a Persona:**It tells Claude to act as an "applied AI engineer."
- **Defines the Core Task:**It explains what an "eval" is and its purpose.
- **Introduces the Tools:**It points to the Eval Protocol library and the MCP servers we configured.
- **Provides Specific Resources:**It gives direct links to the GitHub repositories for context.
- **States the Goal:**It clearly outlines the end-to-end task of setting up the project and creating the first test.

Note:Enabling Web Access: Our prompt asks Claude to reference several GitHub URLs, so it needs web access to succeed. You can configure this in Claude Code's settings (e.g., in`.claude/settings.json`), by adding a rule to permit the`WebFetch`tool.

From there, because we supercharged it with the MCP tools, our AI agent Claude Code was able to navigate and write Eval Protocol tests more accurately. It set up an environment and had our first test running quickly.

12345678910111213141516

For a bit more color, this is what the initial `data/storefront_eval_dataset.jsonl` looked like.

1234

A significant challenge in TDD is creating a comprehensive set of tests. Our project.md outlined several key user stories and security requirements that we needed to validate. This resulted in an initial set of four diverse test cases, covering browsing, authentication, complex search, and security.

While these four tests provided a good baseline, we needed to cover more edge cases. We gave Claude Code a new task: take these four initial test cases and expand each one into eight variations. Claude quickly generated a rich dataset of 32 tests, creating subtle variations in phrasing, combining different filters, and exploring different angles for each core scenario. This AI-assisted test generation saved hours of manual work and resulted in a much more robust evaluation suite.

In our last blog, we detailed why the TDD workflow was so powerful—with it, you can confidently change system prompts, switch models, or add features, knowing you won't cause unexpected regressions.

But now, by grounding the AI agent with specific, relevant context via MCP, we enable it to move beyond directed code generation. It becomes a true partner in the TDD loop, capable of understanding the nuances of a testing framework and creatively expanding a test suite. The developer's role shifts from writing every line of code to defining the high-level goals and then supervising the AI as it handles the detailed implementation and iteration. This creates a powerful feedback loop where you can confidently build, test, and scale your agent's capabilities.

As AI continues to reshape our industry, developers must also evolve. It's time to embrace new superpowers like MCP that allow us to work in closer collaboration with our AI counterparts. This represents a fundamental shift in how we build intelligent systems—moving from manual implementation to AI-driven validation. At Fireworks, we believe this partnership is the future of agent development.

Check out the completed code [from this exercise here](https://github.com/eval-protocol/claudecode_digital_store_app)!
