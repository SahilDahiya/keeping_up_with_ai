---
title: Time awareness and async input for personal agents | OpenAI Developers
kind: blog
topic: null
subtopic: null
secondary_topics: []
summary: null
triage: null
skip_reason: null
source: openai-devs
url: https://developers.openai.com/blog/time-awareness-and-async-input-for-personal-agents/
author: null
published: '2026-11-20'
fetched: '2026-11-21T06:06:16Z'
classifier: null
taxonomy_rev: 2
words: 3486
content_sha256: dad4f5115422866ec28993fbf25c7b4cbd46714bb8fb9e9fc2aa696db2a8310c
---

# Time awareness and async input for personal agents | OpenAI Developers

If you’re building a personal agent [similar to a dot](https://learn.chatgpt.com/docs/dots), you’ll often want to deliver results to the user on a deadline.

Let’s say I have a meeting with a prospective customer in 15 minutes. I ask my agent to research the company and prepare a briefing, leaving me three minutes to read it before the meeting. That’s a pretty typical timeline for my meeting prep during the workday 😬.

The agent notices that I haven’t said whether the meeting is a technical evaluation or a discussion about pricing. That distinction would change which details to investigate and what content to include in the briefing.

The agent decides to ask about the meeting’s focus. While waiting for my reply, how should the agent use the remaining time, incorporate a reply if one arrives, and deliver a useful briefing even if I never answer?

## Time awareness and async input

**Time awareness**, a recent addition to the [Agents API](https://developers.openai.com/api/docs/guides/agents-api/overview), gives the model periodic reminders of the current time so it can adjust its work to the deadline. **[Async function tools](https://developers.openai.com/api/docs/guides/async-tool-calling#how-async-tools-work)** let the agent continue working while the application waits for an answer from the end user.

With 15 minutes until the meeting, the agent has 12 minutes to prepare my briefing. As that deadline approaches, the agent can prioritize checking its strongest findings and writing the briefing over opening another line of research. Alternatively, providing longer timelines lets the model know it can afford to go deeper and perform more research.

A request like “I have a meeting in 15 minutes. Give me a briefing with three minutes left to review it” sets the deadline. Time awareness keeps the model informed as searches and user input are pending.

To show how this works, we’ll set up an agent to help users prepare for meetings. In the illustration, I ask at 4 p.m. UTC for a briefing by 4:12 p.m., ahead of a 4:15 p.m. meeting. We’ll see how to configure the agent, provide timing updates, react to its tool calls, and handle its final result.

You can [skip right to the full example code for your preferred programming language](https://developers.openai.com#complete-example-code).

## Create the agent

To help the user prep for a meeting, our agent needs to research the company, ask for missing meeting context, and track the time left to prepare a briefing. To perform those tasks, the agent will need web search, an asynchronous tool to ask for user input, and time awareness.

We create an agent [with this configuration](https://developers.openai.com/api/docs/guides/agents-api/configuration) using the SDK’s [agent creation method](https://developers.openai.com/api/reference/resources/beta/subresources/agents/methods/create):

- Set `experimental.time_awareness` to `true` to give the model periodic reminders of the current time.
- Enable the built-in [`web_search` tool](https://developers.openai.com/api/docs/guides/agents-api/tools/web-search) in `live` mode so the agent can search the web for current information.
- Define a [function tool](https://developers.openai.com/api/docs/guides/agents-api/tools/functions) named `request_user_input_async`. Set `async` to `true` so the agent can continue working while your application collects the reply.

Set `OPENAI_API_KEY` to a key from a project with Agents API access. Follow the [SDK libraries guide](https://developers.openai.com/api/docs/libraries) to install an official SDK and create the `client` used below. See the [Agents API quickstart prerequisites](https://developers.openai.com/api/docs/guides/agents-api/quickstart#prerequisites) for required permissions.

```
async def create_agent(client: AsyncOpenAI):
    return await client.beta.agents.create(
        name="Personal assistant",
        model="gpt-6.2-astra",
        experimental={"time_awareness": True},
        instructions=(
            "You are a personal assistant. Deliver useful, well-sourced answers "
            "within the user's time constraints. Ask for clarification when it "
            "would materially improve the result, and keep making progress while "
            "a reply is pending. State important uncertainties."
        ),
        tools=[
            {"type": "web_search", "mode": "live"},
            {
                "type": "function",
                "name": "request_user_input_async",
                "description": "Ask for missing context while continuing independent work.",
                "async": True,
                "parameters": {
                    "type": "object",
                    "properties": {
                        "question": {"type": "string"},
                        "choices": {"type": "array", "items": {"type": "string"}},
                    },
                    "required": ["question"],
                    "additionalProperties": False,
                },
            },
        ],
    )
```
## Start a task with a deadline

Now we can ask the agent to prepare for a meeting with a customer. The request gives the agent the company, the meeting time, and the briefing deadline, leaving it to decide what to research and whether to ask for clarification.

Start a [session](https://developers.openai.com/api/docs/guides/agents-api/sessions) with the SDK’s [session creation method](https://developers.openai.com/api/reference/resources/beta/subresources/agents/subresources/sessions/methods/create) and stream updates as the agent works.

Your application will need to convert time-based language like “in 15 minutes” and “three minutes left to review” into absolute timestamps so the model and application share the same time data. This code tells the agent the meeting is 15 minutes from now and asks for delivery 12 minutes from now.

```
now = datetime.now(UTC)
meeting = (now + timedelta(minutes=15)).isoformat(timespec="seconds")
delivery = (now + timedelta(minutes=12)).isoformat(timespec="seconds")
stream = await client.beta.agents.sessions.create(
    agent_id=agent.id,
    environment={"type": "none"},
    input=(
        f"I am meeting with Pied Piper (example.com) about our customer-support software at "
        f"{meeting}. Get me up to speed on their business, recent product "
        f"announcements, and questions I should ask. Send me a concise briefing by "
        f"{delivery} so I have time to read it before the meeting."
    ),
    stream=True,
    timeout=12 * 60,
)
```
## Display a pending question

When the agent asks about the meeting’s focus, the application needs to show the question while company research continues. Collecting a reply in a separate task lets the application keep receiving the agent’s updates.

It’s up to your application code to collect user input for clarification when the model asks for it via a tool call.

Watch the [session event stream](https://developers.openai.com/api/docs/guides/agents-api/sessions/events) for [`agent.session.turn.item.done`](https://developers.openai.com/api/reference/resources/beta/subresources/agents/streaming-events) events containing a `request_user_input_async` function call. Read the question and any suggested choices from `item.arguments`. The session’s `required_actions` list describes blocking actions, so waiting for an entry there can miss an asynchronous question.

Save the session ID and the call’s `turn_id` and `call_id` to associate the reply with the question. Track pending questions so each is displayed and handled once, and cancel their input handlers when the agent’s run ends:

```
item = event.item
if (
    isinstance(item, AgentFunctionCallItem)
    and item.name == "request_user_input_async"
    and item.call_id not in questions
):
    questions[item.call_id] = asyncio.create_task(
        respond(
            client,
            event.session_id,
            item,
            replies,
            prompt_lock,
            reply_cutoff,
        )
    )
```
The question arrives as a function-call event:

```
{
  "type": "agent.session.turn.item.done",
  "item": {
    "type": "function_call",
    "name": "request_user_input_async",
    "arguments": {
      "question": "Is this meeting mainly a technical evaluation or a commercial discussion?",
      "choices": ["Technical evaluation", "Commercial discussion"]
    },
    "turn_id": "turn_789abcd",
    "call_id": "call_012ef34"
  }
}
```
## Return the tool result

The user’s answer to the agent’s question helps the agent focus the briefing on the right meeting goal. If the user never answers, the agent still needs time to finish writing, so the application closes unanswered questions at 4:10 p.m., two minutes before delivery.

Return one [tool result](https://developers.openai.com/api/docs/guides/agents-api/tools/functions#return-the-result) per pending call while the agent’s run is active:

- **On reply**, set `status` to `answered` and put the typed text or selected choice in `answer`.
- **At the cutoff**, if the same `call_id` is still pending and the user has not replied, return `{"status":"no_answer"}`.

Send the result through the SDK’s [session events method](https://developers.openai.com/api/reference/resources/beta/subresources/agents/subresources/sessions/subresources/events/methods/create), using the saved identifiers to match it to the question. Keep consuming the stream while submitting the result. If the agent finishes early, close the pending question in the interface.

```
result = (
    {"status": "answered", "answer": answer} if answer else {"status": "no_answer"}
)
await client.beta.agents.sessions.events.create(
    session_id,
    events=[
        {
            "type": "agent.session.input.tool_result",
            "turn_id": call.turn_id,
            "call_id": call.call_id,
            "success": True,
            "output": json.dumps(result),
        }
    ],
)
```
## Retrieve and deliver the answer

Deliver a concise briefing as soon as it is ready, leaving the user at least three minutes to read it before the meeting. If the deadline arrives first, return the latest completed briefing or report that no verified findings are ready.

When `agent.session.turn.completed` arrives, retrieve the saved [items](https://developers.openai.com/api/docs/guides/agents-api/sessions/events#fetch-items-and-turns) with the SDK’s [turn items method](https://developers.openai.com/api/reference/resources/beta/subresources/agents/subresources/sessions/subresources/turns/subresources/items/methods/list). Find the completed agent message whose `phase` is `final_answer`.

If the stream closes early, [list the session’s turns](https://developers.openai.com/api/reference/resources/beta/subresources/agents/subresources/sessions/subresources/turns/methods/list) to check the saved status. See [stream recovery](https://developers.openai.com/api/docs/guides/agents-api/sessions/events#how-to-recover-a-disconnected-stream) for reconnecting and retrieving saved work.

```
def final_text(item: AgentSessionItem | AgentOutputItem) -> str:
    if (
        item.type == "message"
        and item.role == "assistant"
        and item.status == "completed"
        and item.phase == "final_answer"
    ):
        return "\n".join(
            part.text for part in item.content if part.type == "output_text"
        )
    return ""
async def retrieve_answer(client: AsyncOpenAI, session_id: str, turn_id: str) -> str:
    async for item in client.beta.agents.sessions.turns.items.list(
        turn_id, session_id=session_id, order="desc"
    ):
        if text := final_text(item):
            return text
    return ""
```
## Complete example code

Each language example below contains the full meeting-preparation workflow in one file, including client setup, asynchronous replies, the delivery timer, and cleanup. Each script reads `OPENAI_API_KEY` from the environment and accepts replies in the terminal.

```
import asyncio
import json
import os
import sys
from contextlib import AsyncExitStack, suppress
from datetime import UTC, datetime, timedelta
from threading import Thread
from openai import AsyncOpenAI, ConflictError
from openai.types.beta import AgentFunctionCallItem, AgentOutputItem, AgentSessionItem
client = AsyncOpenAI(max_retries=0)
async def create_agent(client: AsyncOpenAI):
    return await client.beta.agents.create(
        name="Personal assistant",
        model="gpt-6.2-astra",
        experimental={"time_awareness": True},
        instructions=(
            "You are a personal assistant. Deliver useful, well-sourced answers "
            "within the user's time constraints. Ask for clarification when it "
            "would materially improve the result, and keep making progress while "
            "a reply is pending. State important uncertainties."
        ),
        tools=[
            {"type": "web_search", "mode": "live"},
            {
                "type": "function",
                "name": "request_user_input_async",
                "description": "Ask for missing context while continuing independent work.",
                "async": True,
                "parameters": {
                    "type": "object",
                    "properties": {
                        "question": {"type": "string"},
                        "choices": {"type": "array", "items": {"type": "string"}},
                    },
                    "required": ["question"],
                    "additionalProperties": False,
                },
            },
        ],
    )
def console_replies() -> asyncio.Queue[str]:
    loop = asyncio.get_running_loop()
    replies: asyncio.Queue[str] = asyncio.Queue()
    def read_lines():
        with os.fdopen(
            os.dup(sys.stdin.fileno()), encoding=sys.stdin.encoding
        ) as terminal:
            for line in terminal:
                try:
                    loop.call_soon_threadsafe(replies.put_nowait, line.strip())
                except RuntimeError:
                    return  # The session and its event loop have closed.
    # A pending terminal read must not keep the program open after delivery.
    Thread(target=read_lines, daemon=True).start()
    return replies
async def respond(client, session_id, call, replies, prompt_lock, cutoff):
    loop = asyncio.get_running_loop()
    try:
        async with asyncio.timeout_at(cutoff), prompt_lock:
            if loop.time() >= cutoff:
                raise TimeoutError
            print(call.arguments["question"], file=sys.stderr, flush=True)
            for choice in call.arguments.get("choices", []):
                print(f"  {choice}", file=sys.stderr, flush=True)
            reply = await replies.get()
            answer = reply if loop.time() < cutoff else ""
    except TimeoutError:
        answer = ""
    result = (
        {"status": "answered", "answer": answer} if answer else {"status": "no_answer"}
    )
    await client.beta.agents.sessions.events.create(
        session_id,
        events=[
            {
                "type": "agent.session.input.tool_result",
                "turn_id": call.turn_id,
                "call_id": call.call_id,
                "success": True,
                "output": json.dumps(result),
            }
        ],
    )
def final_text(item: AgentSessionItem | AgentOutputItem) -> str:
    if (
        item.type == "message"
        and item.role == "assistant"
        and item.status == "completed"
        and item.phase == "final_answer"
    ):
        return "\n".join(
            part.text for part in item.content if part.type == "output_text"
        )
    return ""
async def retrieve_answer(client: AsyncOpenAI, session_id: str, turn_id: str) -> str:
    async for item in client.beta.agents.sessions.turns.items.list(
        turn_id, session_id=session_id, order="desc"
    ):
        if text := final_text(item):
            return text
    return ""
async def main():
    async with client, AsyncExitStack() as cleanup:
        agent = await create_agent(client)
        cleanup.push_async_callback(client.beta.agents.delete, agent.id)
        sessions = client.beta.agents.sessions
        session_id = None
        active = False
        saved_answer = ""
        questions = {}
        prompt_lock = asyncio.Lock()
        replies = console_replies()
        loop = asyncio.get_running_loop()
        started = loop.time()
        reply_cutoff = started + 10 * 60
        try:
            async with asyncio.timeout_at(started + 12 * 60):
                now = datetime.now(UTC)
                meeting = (now + timedelta(minutes=15)).isoformat(timespec="seconds")
                delivery = (now + timedelta(minutes=12)).isoformat(timespec="seconds")
                stream = await client.beta.agents.sessions.create(
                    agent_id=agent.id,
                    environment={"type": "none"},
                    input=(
                        f"I am meeting with Pied Piper (example.com) about our customer-support software at "
                        f"{meeting}. Get me up to speed on their business, recent product "
                        f"announcements, and questions I should ask. Send me a concise briefing by "
                        f"{delivery} so I have time to read it before the meeting."
                    ),
                    stream=True,
                    timeout=12 * 60,
                )
                async with stream:
                    async for event in stream:
                        if event.type == "agent.session.created":
                            session_id = event.session.id
                            # A cancelled turn can take a moment to release its session.
                            cleanup_sessions = client.with_options(
                                max_retries=4, timeout=10
                            ).beta.agents.sessions
                            cleanup.push_async_callback(
                                cleanup_sessions.delete, session_id
                            )
                            active = True
                        elif event.type == "agent.session.turn.item.done":
                            item = event.item
                            if (
                                isinstance(item, AgentFunctionCallItem)
                                and item.name == "request_user_input_async"
                                and item.call_id not in questions
                            ):
                                questions[item.call_id] = asyncio.create_task(
                                    respond(
                                        client,
                                        event.session_id,
                                        item,
                                        replies,
                                        prompt_lock,
                                        reply_cutoff,
                                    )
                                )
                            saved_answer = final_text(item) or saved_answer
                        elif event.type == "agent.session.turn.completed":
                            active = False
                            for question in questions.values():
                                question.cancel()
                            # Allow the creation stream to finish releasing its connection.
                            with suppress(TimeoutError):
                                async with asyncio.timeout(1):
                                    async for _ in stream:
                                        continue
                            answer = await retrieve_answer(
                                client, event.session_id, event.turn.id
                            )
                            print(
                                answer
                                or saved_answer
                                or "No verified findings were available.",
                                flush=True,
                            )
                            return
                        elif event.type in (
                            "agent.session.failed",
                            "agent.session.environment.failed",
                            "agent.session.turn.failed",
                            "agent.session.turn.cancelled",
                            "error",
                        ):
                            active = False
                            raise RuntimeError(
                                f"Meeting briefing stopped: {event.type}"
                            )
                        for question in questions.values():
                            if question.done():
                                error = question.exception()
                                # A finished turn can reject a reply still in flight.
                                if error is not None and not isinstance(
                                    error, ConflictError
                                ):
                                    raise error
                raise RuntimeError("The event stream closed before the turn completed.")
        except TimeoutError:
            print(
                saved_answer or "No verified findings were available by the deadline.",
                flush=True,
            )
        finally:
            for question in questions.values():
                question.cancel()
            await asyncio.gather(*questions.values(), return_exceptions=True)
            if active and session_id:
                await sessions.events.create(
                    session_id, events=[{"type": "agent.session.input.cancel"}]
                )
if __name__ == "__main__":
    asyncio.run(main())
```
## Time awareness in a Responses API loop

If your personal agent uses a hand-coded [Responses API loop](https://developers.openai.com/api/docs/guides/function-calling), the application needs to keep the model informed of the time left to prepare the briefing. Calculate the deadline once, then append a fresh time reminder before every model request, including requests that submit tool results.

The steps below implement the same meeting-preparation task. Each Responses request includes an updated time reminder for the model. An application timer runs throughout the loop so delivery still happens if a request or tool takes too long.

## 1. Set the meeting and briefing deadlines

Give the agent the company to research and the time the briefing is due. Keep the same general instructions and [async question tool](https://developers.openai.com/api/docs/guides/async-tool-calling#add-a-tool-to-ask-the-user-for-input), so the model decides whether it needs clarification.

The meeting starts in 15 minutes, the briefing is due in 12, and the application closes unanswered questions 10 minutes after the task starts. Keep those deadlines fixed throughout the task.

```
import asyncio
import json
import os
import sys
from contextlib import suppress
from dataclasses import dataclass, field
from datetime import UTC, datetime, timedelta
from threading import Thread
from openai import APITimeoutError, AsyncOpenAI, OpenAIError
from openai.types.responses import (
    Response,
    ResponseFunctionToolCall,
    ResponseInputItemParam,
    ToolParam,
)
instructions = (
    "You are a personal assistant. Deliver useful, well-sourced answers "
    "within the user's time constraints. Ask for clarification when it "
    "would materially improve the result, and keep making progress while "
    "a reply is pending. State important uncertainties."
)
tools: list[ToolParam] = [
    {"type": "web_search"},
    {
        "type": "function",
        "name": "request_user_input_async",
        "description": "Ask for missing context while continuing independent work.",
        "async": True,
        "strict": False,
        "parameters": {
            "type": "object",
            "properties": {
                "question": {"type": "string"},
                "choices": {"type": "array", "items": {"type": "string"}},
            },
            "required": ["question"],
            "additionalProperties": False,
        },
    },
]
@dataclass
class State:
    response_ids: list[str] = field(default_factory=list)
    questions: dict[str, asyncio.Task[ResponseInputItemParam]] = field(
        default_factory=dict
    )
    seen_calls: set[str] = field(default_factory=set)
    latest_response_id: str | None = None
    saved_answer: str = ""
def configure_task():
    now = datetime.now(UTC)
    started = asyncio.get_running_loop().time()
    meeting = (now + timedelta(minutes=15)).isoformat(timespec="seconds")
    delivery = (now + timedelta(minutes=12)).isoformat(timespec="seconds")
    reply_cutoff = started + 10 * 60
    delivery_cutoff = started + 12 * 60
    input_items = [
        {
            "role": "user",
            "content": (
                f"I am meeting with Pied Piper (example.com) about our customer-support software at "
                f"{meeting}. Get me up to speed on their business, recent product "
                f"announcements, and questions I should ask. Send me a concise briefing by "
                f"{delivery} so I have time to read it before the meeting."
            ),
        }
    ]
    return input_items, reply_cutoff, delivery_cutoff
```
## 2. Add the current time before every model request

The model needs a fresh reading of the clock when it decides what to do next. Use one request helper for both the initial request and every continuation, so the clock update happens in one place.

Immediately before calling the [Responses API](https://developers.openai.com/api/reference/resources/responses/methods/create), append the current UTC time as a [developer message](https://developers.openai.com/api/docs/guides/text#message-roles-and-instruction-following), after the user input or tool results. Send the instructions and tools on every request. The original deadline remains in the conversation history.

```
async def start_response(input_items, previous_response_id, delivery_cutoff):
    remaining = delivery_cutoff - asyncio.get_running_loop().time()
    if remaining <= 0:
        raise TimeoutError
    current_time = datetime.now(UTC).isoformat(timespec="seconds")
    return await client.responses.create(
        model="gpt-6.2-astra",
        instructions=instructions,
        tools=tools,
        previous_response_id=previous_response_id,
        input=[
            *input_items,
            {"role": "developer", "content": f"Current time: {current_time}."},
        ],
        store=True,
        stream=True,
        timeout=remaining,
    )
```
## 3. Collect a reply while research continues

When the agent asks about the meeting’s focus, display the question and collect the reply independently of response generation. The collector returns the answer when it arrives or `no_answer` at the cutoff, using the original `call_id` to keep the result attached to the right question.

```
def console_replies() -> asyncio.Queue[str]:
    loop = asyncio.get_running_loop()
    replies: asyncio.Queue[str] = asyncio.Queue()
    def read_lines():
        with os.fdopen(
            os.dup(sys.stdin.fileno()), encoding=sys.stdin.encoding
        ) as terminal:
            for line in terminal:
                try:
                    loop.call_soon_threadsafe(replies.put_nowait, line.strip())
                except RuntimeError:
                    return
    Thread(target=read_lines, daemon=True).start()
    return replies
async def collect_reply(call, replies, prompt_lock, reply_cutoff):
    arguments = json.loads(call.arguments)
    answer = ""
    # An expired question keeps the empty answer and returns no_answer.
    with suppress(TimeoutError):
        async with asyncio.timeout_at(reply_cutoff), prompt_lock:
            if asyncio.get_running_loop().time() >= reply_cutoff:
                raise TimeoutError
            print(arguments["question"], file=sys.stderr, flush=True)
            for choice in arguments.get("choices", []):
                print(f"  {choice}", file=sys.stderr, flush=True)
            reply = await replies.get()
            if asyncio.get_running_loop().time() < reply_cutoff:
                answer = reply
    result = (
        {"status": "answered", "answer": answer} if answer else {"status": "no_answer"}
    )
    return {
        "type": "function_call_output",
        "call_id": call.call_id,
        "output": json.dumps(result),
    }
```
## 4. Handle questions and completed responses

Start the input collector as soon as the complete question arrives in the [response stream](https://developers.openai.com/api/docs/guides/streaming-responses). Keep reading events while the user considers it, so the model can continue its web research.

When a response completes, save its ID for the next request and retain any completed briefing for delivery. The event handler also records response IDs for cleanup.

```
def final_text(response: Response) -> str:
    return "\n".join(
        part.text
        for item in response.output
        if item.type == "message"
        and item.status == "completed"
        and item.phase in (None, "final_answer")
        for part in item.content
        if part.type == "output_text"
    )
async def read_response(stream, state, replies, prompt_lock, reply_cutoff):
    async with stream:
        async for event in stream:
            if event.type == "response.created":
                state.response_ids.append(event.response.id)
            elif event.type == "response.output_item.done":
                call = event.item
                if (
                    isinstance(call, ResponseFunctionToolCall)
                    and call.name == "request_user_input_async"
                    and call.call_id not in state.seen_calls
                ):
                    state.seen_calls.add(call.call_id)
                    state.questions[call.call_id] = asyncio.create_task(
                        collect_reply(call, replies, prompt_lock, reply_cutoff)
                    )
            elif event.type == "response.completed":
                state.latest_response_id = event.response.id
                answer = final_text(event.response)
                state.saved_answer = answer or state.saved_answer
                # Give the transport a moment to finish after the terminal event.
                with suppress(TimeoutError):
                    async with asyncio.timeout(1):
                        async for _ in stream:
                            continue
                return answer
            elif event.type in ("response.failed", "response.incomplete", "error"):
                raise RuntimeError(f"Meeting briefing stopped: {event.type}")
    raise RuntimeError("The response stream closed before completion.")
```
## 5. Continue the loop with ready results

A reply that arrives during research should inform the next version of the briefing. After each response finishes, collect any ready tool results and send them through the request helper, which adds a new time reminder. Use the latest completed response ID as [`previous_response_id`](https://developers.openai.com/api/docs/guides/conversation-state#passing-context-from-the-previous-response), even when a result belongs to a question from an earlier response.

Keep requests sequential so each builds on the latest conversation state. If the briefing is complete and no result is ready, deliver it and close pending questions. Otherwise, continue working with the updated time, without waiting for an answer.

```
async def run_loop(input_items, state, replies, reply_cutoff, delivery_cutoff):
    prompt_lock = asyncio.Lock()
    while True:
        stream = await start_response(
            input_items, state.latest_response_id, delivery_cutoff
        )
        answer = await read_response(stream, state, replies, prompt_lock, reply_cutoff)
        await asyncio.sleep(0)  # Let ready input handlers finish.
        input_items = []
        for call_id, task in list(state.questions.items()):
            if task.done():
                input_items.append(task.result())
                del state.questions[call_id]
        if input_items:
            continue  # Incorporate replies that arrived during generation.
        if answer:
            return answer
        input_items = [
            {
                "role": "developer",
                "content": "Continue working on the briefing while replies are pending.",
            }
        ]
```
## 6. Enforce delivery while a request is in flight

An application timer enforces the briefing deadline, preserving the user’s review time. Apply the timer to the whole loop, including API requests and stream consumption.

At the deadline, stop the active request and deliver the saved briefing, or report that no verified findings are ready. Close pending input handlers and [delete the stored responses](https://developers.openai.com/api/reference/resources/responses/methods/delete) after delivery.

```
async def main():
    state = State()
    replies = console_replies()
    input_items, reply_cutoff, delivery_cutoff = configure_task()
    async with client:
        try:
            async with asyncio.timeout_at(delivery_cutoff):
                answer = await run_loop(
                    input_items, state, replies, reply_cutoff, delivery_cutoff
                )
            print(answer, flush=True)
        except (TimeoutError, APITimeoutError):
            print(
                state.saved_answer
                or "No verified findings were available by the deadline.",
                flush=True,
            )
        finally:
            for task in state.questions.values():
                task.cancel()
            await asyncio.gather(*state.questions.values(), return_exceptions=True)
            for response_id in reversed(state.response_ids):
                try:
                    await client.responses.delete(response_id, timeout=10)
                except OpenAIError as error:
                    print(f"Could not delete {response_id}: {error}", file=sys.stderr)
if __name__ == "__main__":
    asyncio.run(main())
```
## Conclusion

Personal agents sometimes need to complete work by a deadline. Ideally they ask for clarification to improve the result, but even without that clarification, they still need to perform useful work.

We gave the agent a deadline and enabled time awareness to help it decide whether to investigate further, verify a finding, or finish writing. Async function tools let it keep researching while the user considered its question. The agent still has enough context to write a useful meeting briefing if the question goes unanswered.

ChatGPT and other agent harnesses use this pattern to keep working while asking the user for clarification. We hope that including time awareness in the Agents API helps you build this pattern yourself. [Let us know what you build](https://x.com/OpenAIDevs)!
