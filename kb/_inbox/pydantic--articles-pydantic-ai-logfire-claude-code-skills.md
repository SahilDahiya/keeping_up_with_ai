---
title: Official Pydantic skills for coding agents
kind: blog
topic: null
subtopic: null
secondary_topics: []
summary: null
triage: null
skip_reason: null
source: pydantic
url: https://pydantic.dev/articles/pydantic-ai-logfire-claude-code-skills
author: Aditya Vardhan
published: '2026-07-29'
fetched: '2026-07-30T06:57:56Z'
classifier: null
taxonomy_rev: 2
words: 396
content_sha256: 4e71088c7dfecb8520c6e42fed51013de065afce335e6b0f57132f427640f585
---

# Official Pydantic skills for coding agents

Pydantic Validation, Pydantic AI, and [Logfire](https://pydantic.dev/logfire) now have official skills, built and maintained by the Pydantic team. Pydantic AI and Logfire are live on Claude's plugin marketplace ([Pydantic AI](https://claude.com/plugins/pydantic-ai), [Logfire](https://claude.com/plugins/logfire)), and all three work across every coding agent that follows the [agentskills.io](https://agentskills.io) spec through the [pydantic/skills](https://github.com/pydantic/skills) repository. In Python projects, the Pydantic AI and Logfire skills also ship with the packages themselves and can be installed via [library-skills.io](https://library-skills.io).


Skills for Pydantic Validation, Pydantic AI, and Logfire already exist, thanks to the OSS community, and we're glad they do. The catch is that all three libraries move fast, and skills maintained outside the repo tend to fall behind. A stale skill is worse than no skill: the agent confidently calls APIs that don't exist anymore.


The Pydantic Validation skill covers data modeling with Pydantic: constraints and field metadata, validators, type coercion, unions, forward annotations, and model hierarchies.

The Pydantic AI skill covers the basics of building an agent: dependencies and output types, tools and run context, structured output, streaming, and stepping through the agent graph.

The Logfire skill covers instrumentation across Python, JavaScript/TypeScript, and Rust: spans and structured logging, framework and library integrations, metrics, and querying telemetry.


In Claude Code, install from the official marketplace: [Pydantic AI](https://claude.com/plugins/pydantic-ai) and [Logfire](https://claude.com/plugins/logfire).

For Pydantic Validation, add the Pydantic marketplace and install the plugin:

```
claude plugin marketplace add pydantic/skills
claude plugin install pydantic@pydantic-skills
```
In Cursor, Codex, Gemini CLI, or any other agent, install the specific skill you need from the `pydantic/skills` repository:

```
npx skills add pydantic/skills --skill pydantic
npx skills add pydantic/skills --skill building-pydantic-ai-agents
npx skills add pydantic/skills --skill logfire-instrumentation
```
The `logfire-instrumentation` skill supports Python, JavaScript/TypeScript, and Rust. It tells the agent to inspect `pyproject.toml` or `requirements.txt`, `package.json`, or `Cargo.toml`, then follow the matching SDK guidance.


For Python projects, you can instead pull the skills straight from your installed dependencies via [library-skills.io](https://library-skills.io):

```
uvx library-skills --all
```
The `--all` flag scans transitive dependencies, which Pydantic AI needs because the skill ships in `pydantic-ai-slim`. For Logfire alone you can drop it (`uvx library-skills`).

The `library-skills` route here is specific to the Python packages.


For Logfire, use the `logfire-instrumentation` `skills` CLI command above.


For Logfire, use the same `logfire-instrumentation` command. The skill includes Rust-specific guidance for `Cargo.toml` projects.

If something's wrong or missing, open an issue on [pydantic](https://github.com/pydantic/pydantic), [pydantic-ai](https://github.com/pydantic/pydantic-ai), or [logfire](https://github.com/pydantic/logfire). We'd rather hear it from you than guess.
