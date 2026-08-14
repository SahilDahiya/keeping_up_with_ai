---
title: StackOne is now a Pydantic AI capability
kind: blog
topic: agents
subtopic: harness
secondary_topics:
- prompt-engineering/context-engineering
summary: Pydantic AI Harness's new StackOne capability exposes hundreds of SaaS connectors
  (Workday, Salesforce, Zendesk) to an agent via a search-then-execute tool pair that
  queries the action catalog at runtime instead of serializing it into the prompt,
  keeping context flat regardless of catalog size, plus an 'individual' mode for exact
  per-action tool schemas and required approval gating for write actions.
triage: null
skip_reason: null
source: pydantic
url: https://pydantic.dev/articles/stackone-pydantic-ai-harness
author: Laís Carvalho
published: '2026-08-13'
fetched: '2026-08-14T06:33:44Z'
classifier: claude
taxonomy_rev: 2
words: 1418
content_sha256: 1f5c5f51f24e67f843a78af32feb08c077419c79fcd9a3d34105e9af454e4a4d
---

# StackOne is now a Pydantic AI capability

[StackOne](https://www.stackone.com/?utm_source=pydantic&utm_medium=referral&utm_campaign=pydantic-harness-launch&utm_content=pydantic-homepage), the integration gateway for AI agents, is now a capability in [Pydantic AI Harness](https://pydantic.dev/docs/ai/harness/overview/). Add StackOne(account_id=...) to an agent's capabilities list and it can work with the actions on a linked account: Workday, BambooHR, Salesforce, Zendesk, and the rest of the StackOne connector catalog.

This post covers the problem this new capability solves, how it works, and what to configure before an agent starts writing to a system of record.

## 

An agent that answers questions about your company's data needs to reach the systems that hold it. In practice, there are two usual ways to do that, and each has a cost.

The first is to hand-write a tool per endpoint: a `list_employees` wrapper here, a `create_ticket` wrapper there, each with its own auth handling, its own pagination quirks, and its own schema to keep in sync when the vendor changes something. Do that across three or four providers and the integration code outgrows the agent.
The second is the obvious shortcut, and it backfires too: dump every action you might need into the tool list and you spend your context window on schemas the model will never call, while tool selection gets worse as the list grows.

StackOne handles both. It is one gateway in front of hundreds of SaaS systems, with thousands of executable actions behind it, and [Search & Execute](https://docs.stackone.com/optimize/search-and-execute?utm_source=pydantic&utm_medium=referral&utm_campaign=pydantic-harness-launch&utm_content=pydantic-docs-search-execute) running on the gateway so a catalog that size never has to be serialized into a prompt. The capability in Pydantic AI Harness is the front door to it from an agent, and it is one line.

## 

Pydantic AI Harness is the official capability library for Pydantic AI. A capability is a self-contained battery: tools, hooks, instructions, and settings bundled together, added to an agent through the `capabilities=[...]` array, and composable with the other capabilities in the library. `StackOne` is one of those, alongside code execution, memory, planning, and guardrails.

An agent can work across as many accounts as it needs. Each StackOne instance is scoped to a StackOne [linked account](https://docs.stackone.com/gateway/concepts/linked-accounts?utm_source=pydantic&utm_medium=referral&utm_campaign=pydantic-harness-launch&utm_content=pydantic-docs-linked-accounts), meaning one end user's authenticated connection to one underlying system, whether that is their Workday, their Salesforce, or their Zendesk.

## 

Install the harness with the `stackone` extra, plus the model provider you want. The `spec` extra covers the YAML agent example further down and logfire covers the tracing calls in every snippet:

```
uv add "pydantic-ai-harness[stackone]" "pydantic-ai-slim[openai,spec,logfire]"
```
Before the first run you need to configure a connector in StackOne, link an account, copy the linked account ID from the dashboard, and create an API key that can execute actions. For a first test, enable only the read actions you need.

```
export STACKONE_API_KEY='your-stackone-api-key'
export STACKONE_ACCOUNT_ID='your-linked-account-id'
export OPENAI_API_KEY='your-openai-api-key'
```
`StackOne` reads `STACKONE_API_KEY` on its own. The account ID is read explicitly in the example below so it stays out of the source:

```
import os
import logfire
from pydantic_ai import Agent
from pydantic_ai_harness.stackone import StackOne
logfire.configure()
logfire.instrument_pydantic_ai()
agent = Agent(
    'openai:gpt-5',
    capabilities=[
        StackOne(account_id=os.environ['STACKONE_ACCOUNT_ID']),
    ],
)
result = agent.run_sync('List the first 5 employees')
print(result.output)
```
That is the whole setup. The model receives two tools by default: one to search for an action matching the request, one to execute the action it found by ID.

## 

The search-then-execute pair is the interesting design decision, so it is worth understanding both modes before you pick one.

| Mode | What the model receives | Use it when | 
|---|---|---|
| `search_execute` | Two tools: search for an action, then execute it by ID | The account has many enabled actions. This is the default. | 
| `individual` | One tool and schema per enabled action | You need exact action selection or per-tool behavior. | 

`search_execute` keeps the context cost flat no matter how many actions the account has enabled, because the catalog is queried at runtime instead of being serialized into the prompt. Action IDs come back from the search tool and should not be guessed.

`individual` mode sends every selected schema to the model, which is what you want when the set is small and you care about exactly which actions are reachable. Filter it with `actions`, using [`fnmatch`](https://docs.python.org/3/library/fnmatch.html) patterns that ignore case and match the full `{connector}_{action}_{entity}` tool name:

```
from pydantic_ai_harness.stackone import StackOne
StackOne(account_id='your-linked-account-id', actions=['*_list_*'])            # All matching list tools
StackOne(account_id='your-linked-account-id', actions=['workday_get_worker'])  # One exact tool
```
Passing `actions` selects `individual` mode for you. Combining it with an explicit `tool_mode='search_execute'` raises an error, because that mode only ever registers the search and execute tools.

One thing to be clear about: `actions` is a context-management tool, not an access control. StackOne controls which actions are enabled for the linked account, and that configuration is the real boundary. Treat the pattern list as a way to shape what the model sees, and the StackOne dashboard as the place where permissions live.

If you want the tools kept out of context entirely until the agent needs them, defer the load:

```
from pydantic_ai_harness.stackone import StackOne
StackOne(account_id='your-linked-account-id', defer_loading=True)
```
The capability uses `id='stackone'` by default so it can be loaded on demand. Give each instance a distinct `id` when one agent manages more than one linked account.

## 

Two settings matter as soon as the agent does more than read.

Provider actions can return large exports, and a full employee list will happily eat a context window. `ToolOutputLimits` bounds oversized returns agent-wide, and composes with `StackOne` like any other capability:

```
import logfire
from pydantic_ai import Agent
from pydantic_ai_harness.stackone import StackOne
from pydantic_ai_harness.tool_output_limits import ToolOutputLimits
logfire.configure()
logfire.instrument_pydantic_ai()
agent = Agent(
    'openai:gpt-5',
    capabilities=[
        StackOne(account_id='your-linked-account-id'),
        ToolOutputLimits(),
    ],
)
```
Approval is not enabled automatically, and it should be your default for anything that mutates a system of record. Use the public `StackOneToolset` with Pydantic AI's [tool approval](https://pydantic.dev/docs/ai/tools-toolsets/toolsets/#requiring-tool-approval):

```
import os
import logfire
from pydantic_ai import Agent
from pydantic_ai_harness.stackone import StackOneToolset
logfire.configure()
logfire.instrument_pydantic_ai()
stackone_tools = StackOneToolset(
    account_id=os.environ['STACKONE_ACCOUNT_ID'],
    actions=['workday_create_employee'],
).approval_required()
agent = Agent('openai:gpt-5', toolsets=[stackone_tools])
```
That returns deferred approval requests for your application to resolve, so a human sits between the model and the write. `StackOneToolset` is the lower-level entry point in general: reach for it when you need `Agent(toolsets=[...])` or another toolset wrapper rather than the capability's defaults.

## 

The capability works with Pydantic AI's [agent spec](https://pydantic.dev/docs/ai/core-concepts/agent-spec/) format, so the configuration can live outside the code. Keep the key in `STACKONE_API_KEY` rather than in the file:

```
# agent.yaml
model: openai:gpt-5
capabilities:
    - StackOne:
          account_id: 'your-linked-account-id'
          actions: ['*_list_*']
```
```
import logfire
from pydantic_ai import Agent
from pydantic_ai_harness.stackone import StackOne
logfire.configure()
logfire.instrument_pydantic_ai()
agent = Agent.from_file('agent.yaml', custom_capability_types=[StackOne])
```
Pass `custom_capability_types` so the spec loader knows how to instantiate `StackOne`.

## 

Pydantic AI brings the parts that make an agent debuggable: typed tool definitions, validated outputs, and tracing through [Pydantic Logfire](https://pydantic.dev/logfire). StackOne brings the connector surface, so the agent's business logic is not buried in HTTP plumbing per vendor.

The combination matters most in the failure cases. When an agent picks the wrong action, or a provider returns a payload shaped differently than last week, a trace shows you which action ID was searched, what was executed, and what came back.

A few caveats worth reading before you ship:

- Harness uses 0.x versioning, so the API may change between releases. Breaking changes ship with a deprecation warning where that is practical.
- Custom `base_url` and URL-valued`client` values must use HTTPS.
- For URL values, the toolset appends the `tool-mode` query parameter when it is absent for the search_execute path. It raises an error when a URL's`tool-mode` conflicts with the configured mode, because rewriting it would invalidate a signed URL. If you use`search_execute` with a signed URL, include`tool-mode=search_execute` before signing.
- Prebuilt clients are used as-is, so configure their transport, auth, account selection, and tool mode yourself.

## 

Link an account in [StackOne](https://docs.stackone.com/guides/introduction?utm_source=pydantic&utm_medium=referral&utm_campaign=pydantic-harness-launch&utm_content=pydantic-docs-get-started), export the two environment variables, and add `StackOne(account_id=...)` to an agent's capabilities. Then:

- The [StackOne capability docs](https://pydantic.dev/docs/ai/harness/stackone/) carry the full API reference for`StackOne` and`StackOneToolset` .
- The [Harness overview](https://pydantic.dev/docs/ai/harness/overview/) lists the other capabilities you can compose with it, including memory, planning, and guardrails.
- All examples call `logfire.configure()` . That is[Pydantic Logfire](https://pydantic.dev/logfire) , and it turns each run into a trace you can open: tool searches, action calls, retries, and token costs, queryable with SQL. Try[Logfire](https://pydantic.dev/logfire) 's[MCP Server](https://pydantic.dev/docs/logfire/guides/mcp-server/) for debugging.
- The [Pydantic AI integration docs](https://pydantic.dev/docs/logfire/integrations/llms/pydanticai/) cover the setup for other parts of your application.
- [Pydantic Evals](https://pydantic.dev/docs/ai/evals/evals/) is what you want once the agent is choosing between actions on its own, so a prompt change that improves one workflow does not quietly break another.

Together, these are pieces of [the Pydantic Stack](https://pydantic.dev/).
