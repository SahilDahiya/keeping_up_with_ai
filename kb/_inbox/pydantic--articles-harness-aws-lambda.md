---
title: Durable Pydantic AI agents on AWS Lambda
kind: blog
topic: null
subtopic: null
secondary_topics: []
summary: null
triage: null
skip_reason: null
source: pydantic
url: https://pydantic.dev/articles/harness-aws-lambda
author: Laís Carvalho
published: '2026-09-09'
fetched: '2026-09-11T06:17:27Z'
classifier: null
taxonomy_rev: 2
words: 1701
content_sha256: 5ce50c33dd6395ced4a86fd472c1d42dfa5b6275c87e45abc41087d7fd0cfd6b
---

# Durable Pydantic AI agents on AWS Lambda

Picture this: an AI support agent spends fifteen minutes working on a ticket. It reads the order, calls the billing API, asks the model what to do next, calls another tool, and somewhere in the eleventh minute the Lambda invocation times out. Lambda retries it. The handler runs again from the first line, so the same model requests go out, the same tools run, the same tokens land on the same invoice, and the billing API issues a second refund for the ticket it already refunded. You now have spent double as many tokens, and have a duplicated refund.

This might sound like a bug, but it is not. A Lambda handler is stateless, and a retry has nothing to resume from because nothing recorded what the run had already finished.

[AWS Lambda durable functions](https://docs.aws.amazon.com/lambda/latest/dg/durable-functions.html) let you build reliable, long-running workflows on Lambda. A durable function can pause, wait for external events, retry failed operations, and resume where it left off, even if Lambda recycles the execution environment. Under the hood, durable functions are regular Lambda functions that use a checkpoint and replay mechanism to track progress. An execution can span up to a year, and a wait suspends it without compute charges for on-demand functions.

[Pydantic AI Harness](https://pydantic.dev/docs/ai/harness/) now ships [`AWSLambdaDurability`](https://pydantic.dev/docs/ai/harness/aws-lambda/), a capability that makes the run durable: every model request, function tool call, MCP call, and dynamic-toolset resolution is checkpointed as an [AWS Lambda durable functions](https://docs.aws.amazon.com/lambda/latest/dg/durable-functions.html) step. A resumed execution replays the handler from the top and serves completed steps from stored results.

## 

```
uv add logfire "pydantic-ai-harness[aws-lambda]" "pydantic-ai-slim[bedrock]"
```
The AWS Durable Execution SDK needs Python 3.11 or newer. `logfire` carries the instrumentation behind every trace in this post.

## 

Put an agent in a handler and deploy it. This is the honest starting point, and for a lookup that finishes in four seconds it is also the finishing point:

```
from typing import Any
import logfire
from pydantic_ai import Agent
logfire.configure()
logfire.instrument_pydantic_ai()
agent = Agent('bedrock:us.amazon.nova-pro-v1:0')
@agent.tool_plain
def get_weather(city: str) -> str:
    return f'It is sunny in {city}.'
def handler(event: dict[str, Any], context: Any) -> str:
    return agent.run_sync(str(event['prompt'])).output
```
The ceiling is the retry. When the invocation source retries a failed handler, such as an asynchronous or event-source invocation after a timeout, throttling, or a transient network error, the whole run starts again, so you pay for the completed work as well as the failed step.

## 

Attach the capability when you build the agent, then adapt the handler body with `durable_agent_handler`:

```
from typing import Any
import logfire
from aws_durable_execution_sdk_python import DurableContext, durable_execution
from pydantic_ai import Agent
from pydantic_ai_harness.aws_lambda import AWSLambdaDurability, durable_agent_handler
logfire.configure()
logfire.instrument_pydantic_ai()
agent = Agent(
    'bedrock:us.amazon.nova-pro-v1:0',
    name='support',
    capabilities=[AWSLambdaDurability()],
)
@agent.tool_plain
def get_weather(city: str) -> str:
    return f'It is sunny in {city}.'
@durable_execution
@durable_agent_handler
async def handler(event: dict[str, Any], context: DurableContext) -> str:
    result = await agent.run(str(event['prompt']))
    return result.output
```
Two decorators and one capability. `@durable_execution` has to be outermost, because its wrapper is what Lambda invokes, and reversing the order raises a `UserError` when the handler is defined. Underneath, `durable_agent_handler` hosts the async agent on a background event loop and services its steps on the Lambda handler thread, which is how a synchronous durable API and an async agent run end up in one continuous step sequence.

Deploy it with a durable configuration and invoke a published version, since in-flight executions are pinned to the version that started them:

```
aws lambda create-function \
  --function-name support-agent \
  --runtime python3.13 \
  --handler handler.handler \
  --role <ROLE_ARN> \
  --zip-file fileb://support-agent.zip \
  --timeout 300 --memory-size 1024 \
  --durable-config '{"ExecutionTimeout":3600,"RetentionPeriodInDays":7}'
aws lambda publish-version --function-name support-agent
```
The role behind `--role` needs `lambda:CheckpointDurableExecution` and `lambda:GetDurableExecutionState`, which the AWS managed [`AWSLambdaBasicDurableExecutionRolePolicy`](https://docs.aws.amazon.com/lambda/latest/dg/durable-security.html) carries. The console attaches them when it creates a durable function and the CLI does not, so a function deployed like this on an ordinary execution role fails at its first checkpoint.

The agent keeps the API it had before. Same `Agent`, same tools, same `output_type` if it has one, and the run now survives the invocation it started in.

Attaching the capability does not make a run durable by itself. Only a run entered through `durable_agent_handler` or `run_durable` is checkpointed, so `await agent.run(...)` in the handler body is the durable path. Drive the same agent from your own `asyncio.run(...)` somewhere else and you get a fully working, non-durable run with no warning at all. `agent.run_sync(...)` inside the handler body does not even get that far: the body is already on a running event loop, and `run_sync` cannot be called from one.

Step names use the agent's `name`, or `AWSLambdaDurability(name=...)` when the agent is unnamed, together with each toolset's `id`. The weather tool above is checkpointed as `support__function_toolset__<agent>.call_tool:get_weather`, and a model request is `support__model.request`. Those names are what you read when a resumed execution does something surprising.

## 

The two [Logfire](https://pydantic.dev/logfire) lines in the snippet are what make a durable run readable. `logfire.instrument_pydantic_ai()` puts every model request and tool call in the trace, and those are the same operations Lambda checkpoints under the step names above, so a step in the durable log has a span you can open and read the arguments of.

A run that resumes is not one trace, though. Each invocation traces itself, and the invocation that picks the run back up records only the steps that actually executed: the completed ones return their stored results instead of running, so they have nothing to report. Reading a resumed run means reading the invocations in order, and the short second trace is the good outcome. It is the work you did not pay for twice.

## 

Checkpointing is per step, so the configuration is per tool. Metadata under the `aws_lambda` key sets that tool's `retry_strategy`, `step_semantics`, and `serdes`:

```
from aws_durable_execution_sdk_python.config import StepSemantics
from pydantic_ai.toolsets import FunctionToolset
toolset = FunctionToolset(id='billing')
@toolset.tool_plain(metadata={'aws_lambda': {'step_semantics': StepSemantics.AT_MOST_ONCE_PER_RETRY}})
def charge_card(amount: int) -> str:
    return f'charged {amount}'
```
`AWSLambdaDurability(step_config=...)` sets the base for every step, and per-tool metadata overrides it key by key, so a tool that sets only `step_semantics` keeps the base retry strategy. At the other end, `metadata={'aws_lambda': False}` opts a tool out of checkpointing entirely and lets it run inline on every attempt, which is the right call for something cheap and side-effect-free. MCP tools cannot opt out, because they do I/O that must not re-run.

Two constraints:

**Steps are at least once, and retried by default.** A step is checkpointed after it runs, so an interruption between a tool's side effect and its checkpoint re-runs the tool on resume. The SDK's default policy allows six total attempts (the initial attempt plus five retries) with exponential backoff. Keep side effects idempotent. For the tool that genuinely must not repeat, `AT_MOST_ONCE_PER_RETRY` is only half the answer: it prevents re-execution within an attempt, and the retry policy still starts further attempts that do execute the body. Set both, pairing it with `RetryPresets.none()`. While you are there, turn off one of the two retry layers, because Pydantic AI and the provider clients have their own and stacking them multiplies attempts and mishandles `Retry-After`.

**Changing the shape of the run breaks in-flight executions.** Checkpoints are matched by the order operations are reached, so adding a tool, removing an MCP server, flipping an opt-out, adding an `event_stream_handler`, or changing the model all shift the sequence out from under an execution that started on the old code. Publish a new version and let the old one drain. This is the same discipline a schema migration asks for, applied to the shape of an agent.

## 

Pydantic AI officially supports five durable execution solutions. [Temporal](https://pydantic.dev/docs/ai/capabilities/durable_execution/temporal/) and [Restate](https://pydantic.dev/docs/ai/capabilities/durable_execution/restate/) put a server in front of your agent and provide durable orchestration. [DBOS](https://pydantic.dev/docs/ai/capabilities/durable_execution/dbos/) runs in-process as a library and checkpoints into a database you already have, and [Prefect](https://pydantic.dev/docs/ai/capabilities/durable_execution/prefect/) brings the transactional semantics of a workflow framework. Lambda durability is the one that adds no component at all: if the agent is already a function, durability is a capability, two decorators, and a flag on the deploy. The [durable execution docs](https://pydantic.dev/docs/ai/capabilities/durable_execution/overview/) cover all five.

The [AWS Lambda durability docs](https://pydantic.dev/docs/ai/harness/aws-lambda/) document every step name, the per-tool configuration, and the budgets, and the [capability matrix](https://github.com/pydantic/pydantic-ai-harness#capability-matrix) tracks the rest of the shelf.

## 

**Does this work with any model provider, or only Amazon Bedrock?**

Any provider Pydantic AI supports. The capability checkpoints the model request itself, not a particular client, and a model operation that does not use the agent's default model records its model id in the step name so a resumed execution maps each checkpoint back to the model it was recorded for. Bedrock appears in the examples because it is the provider most Lambda deployments reach for first.

**What does checkpointing cost?**

Steps consume a durable execution's operations and storage quotas. A turn consumes one model step plus one step per tool call. Large tool results consume the storage budget, [so store references, not payloads](https://docs.aws.amazon.com/durable-execution/patterns/best-practices/state/#store-references-not-payloads), or use the [FileSystem serdes](https://docs.aws.amazon.com/durable-execution/sdk-reference/state/serialization/#filesystem-serdes) to keep large values on Amazon S3 Files and checkpoint only a file pointer. You benefit because you do not pay for repeated model requests and repeated tool calls on every retry. [Please see durable functions quotas](https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html#durable-functions-quotas).

**Can tools still run in parallel?**

Not inside a durable handler. A step's identity comes from the order steps are reached, so concurrently scheduled tool calls could claim each other's checkpoints on resume. The run is switched to sequential tool execution inside the handler and keeps its configured parallelism everywhere else.

**What happens if I redeploy while executions are running?**

They break, unless you version. A resumed execution matches checkpoints positionally, so any change to the number or order of steps invalidates executions started under the old code, and renaming the agent or a toolset `id` changes the recorded names too. Deploy under a new published version and let in-flight executions finish on the old one.

**Can I stream tokens out of a durable execution?**

Not to a caller. A durable execution returns a single value when it completes, so there is no channel to stream through while it runs. `run_stream` and `iter` still work inside the handler and are checkpointed normally, and an `event_stream_handler` gets you live model events inside the model step, with each agent-level event checkpointed in its own step.
