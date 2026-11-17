---
title: Durable Pydantic AI agents with Azure Durable Task
kind: blog
topic: null
subtopic: null
secondary_topics: []
summary: null
triage: null
skip_reason: null
source: pydantic
url: https://pydantic.dev/articles/azure-durable-task-pydantic-ai
author: Laís Carvalho
published: '2026-11-16'
fetched: '2026-11-17T06:12:51Z'
classifier: null
taxonomy_rev: 2
words: 2318
content_sha256: 91dd5b177ff48ab1d4b008074c70c28c6faafcd204bcf993fcb8723f02a370db
---

# Durable Pydantic AI agents with Azure Durable Task

![Pydantic logo, a multiplication sign, and the Microsoft logo beside the words Azure Durable Task](https://pydantic.dev/assets/blog/azure-durable-task-pydantic-ai/azure-durable-task-pydantic.png)


A support agent gets a ticket: order A-1001 arrived damaged. It asks the model what to do, looks up the order, asks the model again, and issues a refund. Then the worker running it is killed by a deploy, a scale-in event, or an out-of-memory error, and the process takes everything it knew about the run with it.

Restart the run from the top and you pay for the model requests twice, call the order API twice, and maybe refund the customer twice. Don't restart it and the ticket sits half-handled until someone notices.

[Durable Task](https://github.com/microsoft/durabletask-python) is Microsoft's answer to that problem, and it is the engine behind Azure Durable Functions. You write an orchestrator as ordinary Python code. The work it delegates runs as activities, and [Azure Durable Task Scheduler](https://learn.microsoft.com/en-us/azure/durable-task/scheduler/durable-task-scheduler) records the result of every completed activity. When a worker dies, another worker picks up the orchestration, replays the recorded results, and carries on from the step that was in flight.

[Pydantic AI Harness](https://pydantic.dev/docs/ai/harness/) now ships [`AzureDurableTaskDurability`](https://pydantic.dev/docs/ai/harness/azure-durable-task/), a capability that brings the agent loop into that model. By default, model requests, function tool calls, MCP calls, and durable capability operations each run as a Durable Task activity. Outside an orchestration the agent runs exactly as it did before. The Azure team announced it on their side too, in [Introducing Azure Durable Task for Pydantic AI agents](https://techcommunity.microsoft.com/blog/appsonazureblog/introducing-azure-durable-task-for-pydantic-ai-agents/4571024?utm_source=pydantic&utm_medium=partnership&utm_campaign=azure-durable-task-pydantic-ai).

## 

```
uv add logfire "pydantic-ai-harness[azure-durable-task]" "pydantic-ai-slim[anthropic]"
```
The `azure-durable-task` extra installs the Durable Task Python SDK, the Azure-managed worker and client, and `azure-identity`. The examples use Anthropic, but any provider Pydantic AI supports works. [Pydantic Logfire](https://pydantic.dev/logfire) instruments the agent, so each run shows up as a trace with every model request, tool call, and activity.

Set your model provider key and a [Logfire write token](https://pydantic.dev/docs/logfire/manage/create-write-tokens/) before running the examples:

```
export ANTHROPIC_API_KEY='your-anthropic-api-key'
export LOGFIRE_TOKEN='your-logfire-write-token'
```
For local development, start the [Durable Task Scheduler emulator](https://learn.microsoft.com/en-us/azure/durable-task/sdks/quickstart-portable-durable-task-sdks) in Docker:

```
docker run --rm --name dts-emulator \
  -p 127.0.0.1:8080:8080 -p 127.0.0.1:8082:8082 \
  mcr.microsoft.com/dts/dts-emulator:v0.0.9
```
The emulator serves the SDK on port 8080 with a task hub called `default`, and its dashboard on [http://localhost:8082](http://localhost:8082). No Azure subscription needed yet.

## 

Attach the capability to the agent, give the agent a `name`, and write the orchestrator. The name prefixes every activity the agent registers, so it is recorded in orchestration history. Save this as `support_agent.py`:

```
from collections.abc import Generator
import logfire
from durabletask import task
from pydantic_ai import Agent, RunContext
from pydantic_ai_harness.azure_durable_task import AzureDurableTaskDurability, run_durable
logfire.configure(service_name='support-agent')
logfire.instrument_pydantic_ai()
agent = Agent(
    'anthropic:claude-sonnet-5-5',
    name='support',
    instructions='Look up the order, then refund it if it arrived damaged.',
    capabilities=[AzureDurableTaskDurability()],
)
@agent.tool_plain
def lookup_order(order_id: str) -> dict[str, str]:
    return {'order_id': order_id, 'status': 'delivered', 'note': 'box arrived crushed', 'total': '42.00'}
@agent.tool
def issue_refund(ctx: RunContext[None], order_id: str, amount: str) -> str:
    idempotency_key = f'{ctx.run_id}:{ctx.tool_call_id}'
    logfire.info('refund {order_id} {amount}', order_id=order_id, amount=amount, idempotency_key=idempotency_key)
    # Stub: call your payments API here with idempotency_key, so a repeated call is a no-op.
    return f'Refunded {amount} on {order_id}'
def support(ctx: task.OrchestrationContext, prompt: str) -> Generator[task.Task[object], object, str]:
    result = yield from run_durable(ctx, lambda: agent.run(prompt))
    return result.output
```
The tools are ordinary Pydantic AI tools. `issue_refund` is a stub that logs the refund to [Logfire](https://pydantic.dev/logfire) instead of moving money, so the example runs without a payments account. Nothing about either tool changes to make it durable, apart from the idempotency key, which the section on replay explains.

`run_durable` is the bridge between the Durable Task generator style and an async agent run, and you call it wherever the agent belongs in your workflow. The orchestrator returns JSON-compatible output. If the agent has a Pydantic model as `output_type`, return `result.output.model_dump(mode='json')`.

Finally, start a worker and schedule an orchestration from `main.py`:

```
import logfire
from durabletask.client import TaskHubGrpcClient
from durabletask.worker import TaskHubGrpcWorker
from support_agent import AzureDurableTaskDurability, agent, support
emulator = dict(host_address='localhost:8080', metadata=[('taskhub', 'default')], secure_channel=False)
worker = TaskHubGrpcWorker(**emulator)
worker.add_orchestrator(support)
durability = AzureDurableTaskDurability.from_agent(agent)
assert durability is not None
with durability.register(worker), worker, TaskHubGrpcClient(**emulator) as client:
    worker.start()
    with logfire.span('support ticket A-1001'):
        instance_id = client.schedule_new_orchestration(
            support, input='Order A-1001 arrived damaged. Please sort it out.'
        )
        state = client.wait_for_orchestration_completion(instance_id, timeout=60)
        assert state is not None
        state.raise_if_failed()
        print(state.get_output())
```
`Agent` binds its own copy of each capability, so `from_agent` fetches the bound one. Enter `register(worker)` before the worker starts and leave it after the worker stops. It registers the agent's activities and runs them. Orchestrators and clients are plain Durable Task SDK code, and a client can live in a different process that never imports the agent. The `logfire.span` wraps client code, which never replays, so it appears once per ticket in Logfire.

## 

I ran the agent above against the emulator and killed the worker with `os._exit(1)` inside `issue_refund`, after the refund ran and before its result reached the scheduler. Then I started a second worker. For the test, each tool also appended a line to a file every time its body executed:

```
lookup_order A-1001 pid=10761
issue_refund A-1001 key=d3885ebc...:support:d6b9f9de...:toolu_01M455EcNkh3yCYePF2ieJAt pid=10761
issue_refund A-1001 key=d3885ebc...:support:d6b9f9de...:toolu_01M455EcNkh3yCYePF2ieJAt pid=10821
```
The first worker made two model requests, ran `lookup_order`, and died inside `issue_refund`. The second worker didn't repeat any of the first three activities. It replayed them from history, ran `issue_refund` again because its result was never recorded, made the final model request, and completed the orchestration about a second later:

```
COMPLETED I've refunded order A-1001 in full, $42.00. The order was marked delivered,
and its note said the box arrived crushed, which matches the damage you reported.
```
The refund tool ran twice. That is the honest shape of durable execution, and it brings us to the rules.

## 

Each time an activity completes, the SDK runs your orchestrator again from the start and serves every completed result from history. That is how a replacement worker resumes the orchestration, and it means a few things about how you write the agent:

- **Activities run at least once.** A worker can die after a tool's side effect and before its result is recorded, as it did above. Make tools idempotent. `ctx.run_id` and `ctx.tool_call_id` survive the restart unchanged, which makes them a good idempotency key: the two `issue_refund` lines carry the same one.
- **Orchestrator-side code runs on every replay.** Hooks, instruction functions, output validators, and inline tools must be deterministic and must not do network, file, or thread I/O. Put I/O in a tool or a capability's `@durable_operation` method.
- **Names are persisted.** Activity names come from the agent's `name`, toolset IDs, and tool names. Don't rename any of them while orchestrations that use them are still running.
- **Replay cost grows with run length.** Each replay re-runs the agent up to its latest step, so orchestrator CPU grows with the square of the number of steps. Keep very long conversations in separate orchestrations.
- **Spans repeat.** Pydantic AI spans created in orchestrator code are emitted again on every replay, so one run shows its agent run and model request spans several times in Logfire.
- **Errors change type.** An exception raised in a model request or tool reaches the orchestrator as `durabletask.task.TaskFailedError`. `UserError` keeps its type.

Dependencies follow the same logic. They cross into activities as data, so they must be JSON-serializable (dataclasses, Pydantic models, and JSON values), and activities rebuild them from the agent's `deps_type`. Create database clients and HTTP sessions inside the tool that uses them, not in `deps`.

## 

A refund above a threshold, a production deploy, a payment: some tool calls need a person to say yes. With Durable Task the approval belongs to the orchestrator, and the orchestration waits for an external event. No activity runs while it waits, so a review can take five minutes or three days.

Mark the tool with `requires_approval=True` and add `DeferredToolRequests` to the output type:

```
from collections.abc import Generator
from durabletask.task import OrchestrationContext, Task
from pydantic import TypeAdapter
import logfire
from pydantic_ai import Agent, DeferredToolRequests, DeferredToolResults, UserError
from pydantic_ai_harness.azure_durable_task import AzureDurableTaskDurability, run_durable
logfire.configure(service_name='payment-review')
logfire.instrument_pydantic_ai()
agent = Agent(
    'anthropic:claude-sonnet-5-5',
    name='review',
    output_type=[str, DeferredToolRequests],
    capabilities=[AzureDurableTaskDurability()],
)
@agent.tool_plain(requires_approval=True)
def approve_payment(amount: int) -> str:
    return f'Paid {amount}'
def review(ctx: OrchestrationContext, prompt: str) -> Generator[Task[object], object, str]:
    result = yield from run_durable(ctx, lambda: agent.run(prompt))
    while isinstance(result.output, DeferredToolRequests):
        requests = result.output
        event_name = f'review:{ctx.new_uuid()}'
        ctx.set_custom_status({
            'event': event_name,
            'requests': TypeAdapter(DeferredToolRequests).dump_python(requests, mode='json'),
        })
        payload = yield ctx.wait_for_external_event(event_name)
        approvals = TypeAdapter(dict[str, bool]).validate_python(payload, strict=True)
        if set(approvals) != {call.tool_call_id for call in requests.approvals}:
            raise UserError('Decisions must match the reviewed tool-call IDs exactly.')
        result = yield from run_durable(
            ctx,
            lambda: agent.run(
                message_history=result.all_messages(),
                deferred_tool_results=DeferredToolResults(approvals=dict(approvals)),
                usage=result.usage,
                conversation_id=result.conversation_id,
            ),
        )
    ctx.set_custom_status(None)
    return result.output
```
The orchestrator publishes the pending tool calls and a fresh event name in its custom status. Your review UI reads that status with `client.get_orchestration_state(instance_id)`, shows the requests to a person, and sends their decision back with `client.raise_orchestration_event(instance_id, event_name, data={tool_call_id: True})`. The agent resumes with the full message history and the usage it had already accumulated.

Two details are easy to get wrong. A new event name per pause means a late decision can't answer a later review. And Durable Task matches event names case-insensitively, so tool-call IDs belong in the payload, never in the event name. The [Azure Durable Task docs](https://pydantic.dev/docs/ai/harness/azure-durable-task/#approvals-and-deferred-calls) include a `submit_review` helper that checks the review is still pending before raising the event.

## 

Pass native `RetryPolicy` values to set activity retries separately for model requests and tool calls:

```
from datetime import timedelta
import logfire
from durabletask.task import RetryPolicy
from pydantic_ai_harness.azure_durable_task import AzureDurableTaskDurability
logfire.configure(service_name='support-agent')
logfire.instrument_pydantic_ai()
durability = AzureDurableTaskDurability(
    model_options=RetryPolicy(first_retry_interval=timedelta(seconds=1), max_number_of_attempts=3),
    tool_options=RetryPolicy(first_retry_interval=timedelta(seconds=1), max_number_of_attempts=2),
)
```
`ModelRetry` and deferred calls are agent control flow, not activity failures, so they never consume a retry. `UserError` and serialization failures aren't retried at all. For finer control, `resolve_tool_options` returns a policy per tool, or `False` to run a pure function tool inline in the orchestrator instead of as an activity. Inline tools replay on every step, so they must be deterministic and free of I/O. MCP and dynamic tools always run as activities.

## 

Moving from the emulator to a real scheduler changes the worker and the client. The orchestrator and `register(worker)` stay the same:

```
import logfire
from azure.identity import DefaultAzureCredential
from durabletask.azuremanaged.client import DurableTaskSchedulerClient
from durabletask.azuremanaged.worker import DurableTaskSchedulerWorker
logfire.configure(service_name='support-worker', environment='production')
logfire.instrument_pydantic_ai()
credential = DefaultAzureCredential()
endpoint = '<scheduler>.<region>.durabletask.io'
worker = DurableTaskSchedulerWorker(host_address=endpoint, taskhub='<hub>', token_credential=credential)
client = DurableTaskSchedulerClient(host_address=endpoint, taskhub='<hub>', token_credential=credential)
```
Grant the worker's identity the [Durable Task Data Contributor](https://learn.microsoft.com/en-us/azure/durable-task/scheduler/durable-task-scheduler-dashboard#assign-dashboard-access-roles-azure) role on the scheduler or task hub. Use the same task hub on workers and clients, and a separate hub per environment so staging orchestrations never replay against production workers.

The worker is a long-running Python process. It runs wherever you already run those, such as Azure Container Apps, AKS, or a VM. This capability uses the standalone Durable Task SDK and does not register anything with Azure Functions.

## 

Pydantic AI runs durably on these engines. The [durable execution overview](https://pydantic.dev/docs/ai/capabilities/durable_execution/overview/) has a complete example for the engines listed there, and the [Azure Durable Task docs](https://pydantic.dev/docs/ai/harness/azure-durable-task/) cover this integration:

Temporal and Restate put a server in front of your agent, as the [Restate and Pydantic AI walkthrough](https://pydantic.dev/articles/restate-durable-execution-pydanticai) shows. DBOS runs in-process and checkpoints into a database you already have, which the [DBOS and Pydantic AI post](https://pydantic.dev/articles/pydantic-ai-dbos) covers. [AWS Lambda durability](https://pydantic.dev/articles/harness-aws-lambda) is the choice when the agent already runs as a Lambda function.

Azure Durable Task is the choice when your infrastructure is on Azure. Durable Task Scheduler is a managed service, so there is no orchestration server for you to run, patch, or scale. Identity is the `DefaultAzureCredential` your other Azure services already use. Once your identity has a [dashboard role](https://learn.microsoft.com/en-us/azure/durable-task/scheduler/durable-task-scheduler-dashboard#assign-dashboard-access-roles-azure) on the scheduler, its dashboard shows every orchestration and activity, with no separate tool to deploy.

## 

**Does this need Azure Functions?**

No. The capability uses the standalone Durable Task Python SDK with your own worker process. Azure Durable Functions is built on the same engine, but this integration doesn't register orchestrators or activities with it.

**Can I stream tokens to a user from inside an orchestration?**

Not to the client. Streamed model responses are buffered inside the model request activity, because an activity returns one recorded result. If you need live events, pass an `event_stream_handler` to the capability. It runs as activities, so make it idempotent like any tool.

**Can tools read `ctx.messages` inside an activity?**

No. Inside activities, live run fields such as `ctx.messages` and `ctx.prompt` raise `UserError`, and tools cannot emit run events. An activity only receives what was serialized into it: the tool arguments, the deps, and the run identifiers.

**What happens if I redeploy while orchestrations are running?**

Replay matches activities by the names in history, so renaming the agent, a toolset, or a tool breaks orchestrations that recorded the old name. When a change renames things, let in-flight orchestrations finish on the old workers first, or run the new version against a fresh task hub.

## 

Start the emulator, add `AzureDurableTaskDurability()` to an agent you already have, and wrap the run in an orchestrator. Then kill the worker halfway through, start it again, and watch the dashboard at `localhost:8082` as the run picks up from the step that was interrupted.

When you want more than the first run:

- The [Azure Durable Task docs](https://pydantic.dev/docs/ai/harness/azure-durable-task/) cover dependencies, deferred calls, and every option the capability takes.
- Microsoft's [announcement post](https://techcommunity.microsoft.com/blog/appsonazureblog/introducing-azure-durable-task-for-pydantic-ai-agents/4571024?utm_source=pydantic&utm_medium=partnership&utm_campaign=azure-durable-task-pydantic-ai) walks through the scheduler dashboard and its per-activity timeline.
- In [Logfire](https://pydantic.dev/logfire), search for the `refund` log from `issue_refund` to see whether a tool body ran more than once, and count the repeated orchestrator spans to see how often a run replayed. Retries and token counts sit on the same trace.
- The [Pydantic AI capabilities](https://pydantic.dev/docs/ai/capabilities/overview/) docs explain how capabilities bundle tools, hooks, and settings, and the [Pydantic AI Harness overview](https://pydantic.dev/docs/ai/harness/) lists the rest of the shelf.

Harness is on 0.x releases, so the API can change between minor versions. Changes come with deprecation warnings and migration guidance in the release notes. If something breaks or is missing, the issues on [GitHub](https://github.com/pydantic/pydantic-ai) are open, and you can find us in the [Pydantic Slack](https://pydantic.dev/docs/logfire/join-slack/).
