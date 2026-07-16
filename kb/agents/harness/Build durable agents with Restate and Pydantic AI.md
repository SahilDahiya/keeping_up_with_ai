---
title: Build durable agents with Restate and Pydantic AI
kind: blog
topic: agents
subtopic: harness
secondary_topics:
- product-engineering/architecture
summary: Integrates Restate to give Pydantic AI agents durable execution (journaled
  steps with retry/recovery), durable sessions keyed by user/conversation, human-in-the-loop
  pauses that survive crashes for minutes to months, and durable multi-agent orchestration
  (RPC, fan-out, timeouts).
triage: null
skip_reason: null
source: pydantic
url: https://pydantic.dev/articles/restate-durable-execution-pydanticai
author: Giselle van Dongen
published: '2026-05-12'
fetched: '2026-07-16T22:03:40Z'
classifier: claude
taxonomy_rev: 2
words: 836
content_sha256: a8522bde92ec7d2ede39e50915412c50dd509e10c28073db299bc48c5478aa5e
---

# Build durable agents with Restate and Pydantic AI

*This is a guest post by  Giselle van Dongen.*

We're excited to announce that [Restate](https://restate.dev/) is now integrating with [Pydantic AI](https://pydantic.dev/pydantic-ai). Restate gives agents lightweight, flexible durable execution to make them resilient to failures, persist state across executions, and pause/resume when needed. This integration lets you add that to your Pydantic AI agents with just a few lines of code.


Pydantic AI gives you a type-safe, Pythonic way to define agents with structured outputs, tools, and a unified model provider interface. Restate adds the ingredients they need to work well in production:

- **Durable execution**: retries and recovery, with every step journaled so progress isn't lost or duplicated
- **Durable sessions**: stateful entities keyed by user or conversation, with built-in state and concurrency control
- **Human-in-the-loop**: pause for approvals that take minutes or months, surviving crashes in between
- **Multi-agent orchestration**: durable RPC, fan-out, and timeouts across agents, tools, and services
- **Task control**: cancel, kill, roll back, or restart executions. One at a time or in bulk, via UI or API

Restate is open source and is easy to self-host (single binary, no extra databases, no separate worker processes).


Install the SDK alongside Pydantic AI:

```
uv init .
uv add restate_sdk pydantic-ai
```
Run a Restate server:

```
docker run -p 8080:8080 -p 9070:9070 docker.restate.dev/restatedev/restate:latest
```
Now create your first durable agent:

```
import restate
from pydantic_ai import Agent, RunContext
from restate.ext.pydantic import RestateAgent, restate_context
weather_agent = Agent(
    "openai:gpt-5.2",
    system_prompt="You are a helpful agent that provides weather updates.",
)
@weather_agent.tool()
async def get_weather(_run_ctx: RunContext[None], city: str) -> dict:
    """Get the current weather for a given city."""
    return await restate_context().run_typed("fetch weather", fetch_weather_api, city=city)
restate_agent = RestateAgent(weather_agent)
agent_service = restate.Service("WeatherAgent")
@agent_service.handler()
async def run(_ctx: restate.Context, message: str) -> str:
    result = await restate_agent.run(message)
    return result.output
app = restate.app([agent_service])
```
Your agent is now resilient to failures, with every step logged and recoverable:

- Failed LLM calls will be retried.
- Failed calls to the weather API will be retried.
- If the service crashes, Restate remembers all the steps it did in a journal, and will resume the execution on another process by replaying the journal.

But this is just the start.



Implement stateful agents keyed by user or session ID, with Restate Virtual Objects. Message history is persisted in Restate's durable K/V store and automatically restored on each request:

```
assistant = Agent(
    "openai:gpt-5.2",
    system_prompt="You are a helpful assistant.",
)
restate_assistant = RestateAgent(assistant)
chat = VirtualObject("Chat")
@chat.handler()
async def message(ctx: ObjectContext, req: ChatMessage) -> str:
    # Load message history from Restate's durable key-value store
    history = await ctx.get("messages", serde=MessageSerde())
    result = await restate_assistant.run(req.message, message_history=history)
    # Store updated history back in Restate state
    ctx.set("messages", result.all_messages(), serde=MessageSerde())
    return result.output
```
The conversation state lives in Restate, queryable through the UI, with automatic concurrency control to prevent race conditions when users send multiple messages.


Real-world agents need human oversight. Durable promises make this easy: your agent pauses execution, waits for human input, and resumes automatically, even if the service crashes while waiting:

```
@agent.tool
async def human_approval(_run_ctx: RunContext[None], claim: InsuranceClaim) -> str:
    """Ask for human approval for high-value claims."""
    # Create a durable promise
    approval_id, approval_promise = restate_context().awakeable(type_hint=str)
    # Notify the moderator (persisted)
    await restate_context().run_typed(
        "Request review", request_human_review, claim=claim, awakeable_id=approval_id
    )
    # Wait for review (survives crashes)
    return await approval_promise
```
Add timeouts to prevent workflows from waiting indefinitely. Restate persists both the timeout and the approval promise, maintaining the correct remaining time through restarts:

```
# Wait for human approval for at most 3 hours to reach our SLA
match await restate.select(
    approval=approval_promise,
    timeout=restate_context().sleep(timedelta(hours=3)),
):
    case ["approval", approved]:
        return "Approved" if approved else "Rejected"
    case _:
        return "Approval timed out, evaluate with AI"
```

Pydantic AI lets you define specialized agents and route between them. With Restate, all routing decisions are durable: if any agent in the chain fails, the entire workflow is recovered from Restate's journal:

```
intake_agent = Agent(
    "openai:gpt-5.2",
    system_prompt="Route insurance claims to the appropriate specialist.",
)
medical_agent = Agent(
    "openai:gpt-5.2",
    system_prompt="Review medical claims for coverage and necessity.",
)
restate_medical_agent = RestateAgent(medical_agent)
@intake_agent.tool
async def consult_medical_specialist(_run_ctx: RunContext[None], claim: InsuranceClaim) -> str:
    """Route to the medical specialist for medical insurance claims."""
    result = await restate_medical_agent.run(claim.model_dump_json())
    return result.output
# Add other agents here
```
You can also call agents deployed as separate services using durable RPC, or fan out to multiple agents in parallel using `restate.gather()`:

```
@agent.tool
async def check_fraud(_run_ctx: RunContext[None], claim: InsuranceClaim) -> str:
    """Analyze the probability of fraud."""
    # Durable service call to a remote agent; persisted and retried by Restate
    return await restate_context().service_call(run_fraud_agent, claim)
```

Pydantic AI gives you a type-safe, Pythonic way to define agents, tools, and structured outputs. Restate handles what they need to run in production: durable execution, sessions, human approvals, and orchestration, all from a single binary, no extra database or worker queue.

Try it out now:

- Pydantic AI durable execution [docs](https://pydantic.dev/docs/ai/integrations/durable_execution/restate/).
- Follow the [Restate + Pydantic AI quickstart](https://docs.restate.dev/ai-quickstart).
- Read the [getting started guides](https://docs.restate.dev/ai/patterns/durable-agents)on sessions, human-in-the-loop, and multi-agent patterns.
- Browse the [code examples](https://github.com/restatedev/ai-examples/tree/main/pydantic-ai)on GitHub.
