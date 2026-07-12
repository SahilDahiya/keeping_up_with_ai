---
title: 'AI Agent Debugging: Four Lessons from Shipping Alyx to Production'
topic: evals-observability
subtopic: tracing
secondary_topics:
- product-engineering/case-studies
summary: Case study from shipping Arize Alyx that distills debugging lessons around
  traces, failure analysis, context inspection, and production agent iteration.
source: arize
url: https://arize.com/blog/ai-agent-debugging-four-lessons-from-shipping-alyx-to-production/
author: Laurie Voss
published: '2026-02-25'
fetched: '2026-07-11T04:54:57Z'
classifier: codex
taxonomy_rev: 1
words: 3971
content_sha256: 0b867b78be91c44559d807e54a15dd0cc2e3096425f76e0f81398fb00dc1d8df
---

# AI Agent Debugging: Four Lessons from Shipping Alyx to Production

Building AI systems that actually work in production is harder than it sounds. Not demo-ware, not “it worked once in a notebook.” Real systems that keep working after week two.

We built [Alyx, Arize’s agent for AX](https://arize.com/blog/alyx-2-0-the-ai-agent-that-actually-plans/), and it broke in ways we didn’t expect. This post is about what broke, what surprised us, and the patterns that actually worked — with enough implementation detail that you can reuse them.

Alyx is an AI assistant that helps people use Arize AX, a platform for observing and evaluating AI systems. Users ask questions in natural language:

- *“What’s the bottleneck in this trace?”*
- *“Which experiment had better accuracy?”*
- *“Why did this eval score drop?”*

Alyx is an LLM-powered agent with tools that map to product features — trace analysis, experiment comparison, dataset operations, eval scoring. Under the hood, it’s an orchestrator loop: the LLM receives a user question, decides which tools to call, processes the results, and either calls more tools or responds.

To try Alyx,[check out our docs](https://arize.com/docs/ax/alyx/arize-copilot)or[book a meeting](https://arize.com/request-a-demo)for a custom demo

Here are four lessons we learned, mostly the hard way.

## Lesson 1: If you want agents to follow rules, put the rules in code

Early on, Alyx had a wandering mind. You’d ask it to do three things. It would do the first one, then spiral deep into that task and forget the other two.

We have a `finish` tool it is supposed to call when done. It called it early, constantly. In one memorable session, we asked it to summarize multiple traces. It made 27 LLM calls — almost all of them reorganizing its own to-do list, going in circles, never actually getting anywhere.

This wasn’t a hallucination problem. It was an **attention problem**. Tool outputs, JSON blobs, and intermediate results flood the context window. The original user request gets buried. By the time the agent decides what to do next, it has forgotten what “next” was.

### The fix: make planning a first-class tool

The fix wasn’t a “think step by step” instruction in the prompt — it was a structured tool the system can inspect and enforce. Before Alyx touches any data, it writes a plan using three tools:

| Tool | Purpose |
|---|---|
| `todo_write` | Create a new plan or restore a previous one |
| `todo_update` | Change a task’s status |
| `todo_read` | Fetch the current plan state |

Each task is a simple structure:

```
```
```
class Todo(BaseModel):
    id: int
    description: str
    status: Literal["pending", "in_progress", "completed", "blocked"]
```
			The four statuses matter more than you’d expect. Our first version only had `pending` and `completed`, and it didn’t work well — the agent had no “working pointer” — it knew what it hadn’t started and what it had finished, but not what it was currently doing. Adding `in_progress` gave it a concrete anchor: “this is my current task, everything else can wait.” Task completion rates improved immediately.

The `blocked` status handles human-in-the-loop scenarios. Sometimes the agent genuinely can’t proceed without user input — “I found three possible bottlenecks, which one should I focus on?” When a task is marked `blocked`, the agent is allowed to finish, because the ball is in the human’s court.

### The plan lives outside conversation history

This was our critical architectural decision: the plan is not stored in the conversation history where it can be buried or truncated. It’s stored on disk, and on every single LLM call we dynamically regenerate a `PlanMessage` from the current state and inject it right after the system prompt, before the noisy tool call history.

Here’s what the agent actually sees:

```
```
# Current Plan
0. [x] Review the trace data and sort LLM spans by latency
1. [~] Identify bottlenecks and suggest changes  ← CURRENT
2. [ ] Generate a summary report for the user
---
## Plan Management Instructions
**Current focus:** Identify bottlenecks and suggest changes
**REMINDER:** Task 1 is marked `in_progress`. When you finish it,
call `todo_update(id=1, status="completed")`. Then mark task 2
as `in_progress` when you start it.

			The plan isn’t just displayed — it coaches the agent through execution. It tells the agent exactly which API call to make when it finishes the current task. Visual status markers ([x], [~], [ ], [!]) give it an instant read on progress. The `← CURRENT` marker draws attention to the active task. No matter how deep the agent gets into tool calls, the plan is always visible, always current.

### The finish gate

If the agent tries to call `finish` with incomplete tasks, it gets an error:

```
```
```
def finish(llm_args, todos, messages):
    incomplete_todos = [
        todo for todo in todos.todo_list
        if todo.status not in {"completed", "blocked"}
    ]
    if incomplete_todos:
        raise RecoverableException(
            message_to_llm=f"You must complete or mark as blocked all todos "
                           f"before finishing. Incomplete: {incomplete_todos}"
        )
```
			Not a suggestion, not a reminder: a `RecoverableException` — a structured error that lists which tasks are unfinished and bounces the agent back into the work loop. The agent can try to finish early. The system won’t let it.

This is the big pattern from lesson one: **prompts are suggestions; code is constraints**. If you want the agent to follow a rule, build the rule into your tools. Tool validation is your friend.

### What we learned getting here

This planning system went through four iterations before it worked well. A few specific things we learned:

- **Few-shot examples beat abstract instructions**. “Always use todo_write to plan your tasks” was in the prompt for a while and basically nothing changed. What worked was showing the agent a concrete example: here’s a real user request, here’s how to decompose it into todos, here’s what to do when each one is done. Show, don’t tell.
- **Status granularity matters more than you’d think**. Going from 2 statuses to 4 had an outsized impact.- `in_progress`prevents the agent from getting distracted mid-task.- `blocked`gives it an escape hatch when it genuinely needs human input.
- **Return the full plan on every mutation**. Both- `todo_write`and- `todo_update`return the complete TodoList, not just the modified item. This ensures the model always sees the full state after any change.

## Lesson 2: Context engineering is the real work

AX experiments can be enormous: hundreds of rows, each with LLM outputs, eval scores, latencies, and metadata. A single experiment can easily hit 100,000 tokens. Two experiments could overflow the context window entirely.

Our first “solution” was a line in the system prompt: “*DO NOT TRY TO COMPARE MORE THAN 2 EXPERIMENTS AT A TIME*.” That’s not engineering. That’s giving up.

### The file system insight

Think about how Cursor or Claude Code navigates a large codebase. They don’t dump entire files into context — they read a preview, use grep to find what they need, and read specific line ranges. The file lives on disk; the agent holds a reference to it and queries incrementally.

We needed the same pattern for structured data.

### LargeJson: store data out-of-band, give the agent a handle

When a tool returns a huge dataset, Alyx doesn’t put it all in context. It stores the full data in server-side memory and gives the LLM a preview plus a stable handle:

```
```
```
LargeJson
├── json_id: "experiment_a1b2c3d4"    ← handle for the agent to reference
├── json_data: { ... full data ... }   ← stored in server memory, never sent to LLM
├── partial_data: { ... preview ... }  ← structure-preserving preview shown to LLM
├── is_truncated: true
├── total_tokens: 85000
├── partial_tokens: 980
└── note_to_llm: "Use jq() tool to query this data."
```
			The agent can reference that handle for the entire session, making targeted queries as it needs specific slices.

### Compress values, not structure

This was our key insight about previews. The obvious approach is to take the first N tokens of the JSON and cut off. But that shows the agent a few complete rows with no idea what the rest looks like.

What we do instead is **compress the values inside the JSON**, not the structure. We recursively walk the JSON tree and truncate every string value to 100 characters, but preserve all keys, all nesting, all array lengths. The agent sees the full shape of the data — every field name, every level of nesting, every array size — with shortened values. That’s exactly what it needs to write a useful query.

If the structure-preserving compression is still over budget, we fall back to brute-force character slicing. But phase one almost always gets it small enough.

Here’s what it looks like in practice:

```
```
```
async def get_experiments(llm_args, large_response_memory) -> LargeJson:
    exp_data = await get_experiments_data(experiment_ids=llm_args.experiment_ids)
    experiments_data = {
        "experiment_ids": experiment_ids,
        "experiment_names": experiment_names,
        "rows": rows,
    }
    return LargeJson.from_json_data(
        data=experiments_data,
        memory=large_response_memory,
        partial_data_token_limit=20000,
        prefix="experiment",
    )
```
			### Query tools: jq and grep_json

Now the agent has two ways to drill into the data:

`jq` — the same jq you’d use at the command line. The agent writes jq expressions to slice, filter, aggregate, and transform:

```
```
.experiments[0].rows[:5]                          # first 5 rows
[.rows[] | select(.eval_score < 0.5)]             # all failing rows
[.rows[].latency_ms] | add / length               # average latency
.rows[] | select(.example_run_id == "abc123")      # find a specific row

			`grep_json` — regex search across the serialized data, like grep -B2 -A2 but over JSON. Useful for exploratory analysis when you don’t know the structure yet.

Both tools have a **hard output limit of 10,000 characters per call**, enforced in code with no exceptions. If a query returns too much, the tool throws a `RecoverableException` suggesting a more specific query. This creates a feedback loop: the agent tries, the tool guides, the agent refines.

### The result

Before LargeJson and jq, comparing experiments meant context overflow. After the change, the agent fetches a preview, identifies which rows need closer inspection, runs targeted jq queries, calculates statistics, and answers the question. Ten targeted tool calls instead of one context-exploding dump. The two-experiment cap was removed entirely. Users can now compare ten experiments at once.

### Design your tools like Unix commands

A theme you’ll see across all of these lessons: **small, composable tools**. jq is an old idea. grep is even older. These tools do one thing well, they accept input and produce output, and the output of one can feed the input of another. That’s exactly right for agents. When you design tools for an LLM agent, think like a Unix programmer. The agent is the shell script; your tools are the commands.

### What we learned about context management

- **Hard token budgets on every tool output**. Every call should have a maximum, enforced in code rather than guidelines.
- **Don’t paper over problems with artificial limits**. The old “max 2 experiments” rule was a workaround, not a solution. The right fix is a better data access pattern.
- **RecoverableExceptions create guided exploration**. The agent tries a query, gets an error with suggestions, and refines. This is the same feedback loop that makes IDE agents effective at code navigation.
- **Tool responses may contain customer data**. Our initial LargeJson implementation logged the full JSON to application logs — hundreds of rows of experiment data, visible to anyone with log access. Caught in code review before it shipped. Be careful about what gets logged.

## Lesson 3: You can’t vibe-check a production agent

Traditional software tests assert deterministic outputs: given input X, expect output Y. Agents break this completely — the same prompt produces different responses every run, multiple responses might be correct, and you can’t assert exact text matches or even the same sequence of tool calls.

Most teams end up doing vibe checks: watch the agent run, eyeball the output, decide it looks roughly right. We did too, and it doesn’t scale, doesn’t catch regressions, and doesn’t run in CI.

### Golden sessions: let production define “good”

Our key insight was to stop writing expected outputs by hand and let production tell us what good looks like.

When Alyx has a great session — when it does exactly the right thing — we capture that session as a golden trace. Arize traces give us everything: what the LLM saw, what it produced, which tools it called and in what order. That becomes ground truth, verified by a real user rather than invented by an engineer.

We test against this golden dataset in two ways.

### Level 1: decision-point tests

These are pytest-based tests that validate specific agent decisions. The pattern: build message history up to a decision point, run the actual orchestrator, assert the output is correct.

The assertion framework handles the reality that LLM output varies in format:

```
```
```
class OutputAssertion(BaseModel):
    contains_any: list[str] | list[list[str]] | None  # OR / AND-of-ORs
    contains_all: list[str] | None                     # AND
    not_contains: list[str] | None                     # NOT
```
			The powerful pattern is** AND-of-ORs** — assert that the output mentions certain facts, each of which could appear in multiple formats:

```
```
```
OutputAssertion(
    contains_any=[
        ["2000 ms", "2000ms", "2.0 seconds", "two seconds"],  # latency
        ["OpenAIChat.invoke", "LLM Span", "LLM span"],         # span reference
    ],
)
```
			This asserts: the output mentions the latency (in any format) AND mentions the span (by any identifier). Deterministic, but flexibly so. You’re matching facts, not phrasing.

For testing conversation memory, you provide prior message history — including tool call signatures, assistant responses, even TodoList state — and then test what the agent does at that specific decision point:

```
```
```
message_history = [
    UserChatMessage(input=UserInput(question="What is the bottleneck of this trace?")),
    AssistantChatMessage(content=[
        ToolCallSignature(name="get_trace_preview", ...),
        TextMessage(content="The bottleneck is OpenAIChat.invoke at 2.00 seconds..."),
        TodoList(todo_list=[Todo(id=0, description="...", status="completed")]),
    ]),
]
# Now test: given this history, what does the agent do next?
user_input = UserInput(question="Can you list all the questions I asked?")
expected = OutputAssertion(
    contains_all=["bottleneck", "most tokens"],
)
```
			Tests run against the real orchestrator with real API clients — not mocks. This catches integration bugs that unit tests miss. The tradeoff is speed, so tests are gated behind a `--evals` flag.

### Level 2: trajectory tests

While decision-point tests validate individual choices, trajectory tests validate entire sessions end-to-end.

The pipeline has three steps:

- Extract production traces into a dataset. A CLI tool pulls a successful session from Arize and converts it to a CSV where each row is one orchestrator turn — the user’s input, the expected text output, expected UX events, trace IDs, and session context.
- Replay through the real orchestrator. Each row is fed through the actual agent. The test runner maintains session memory across rows, so multi-turn conversations replay accurately. If the agent triggers an experiment, the framework actually runs it via the Arize API. IDs get remapped between environments so the same test can run in dev or prod.
- Score with [LLM-as-a-judge](https://arize.com/llm-as-a-judge/). A GPT-4o evaluator compares expected vs. actual output and classifies each turn as CORRECT or INCORRECT.

The evaluation prompt matters a lot. We tuned it extensively with domain-specific rules:

- **Numeric tolerance**: “2000ms” and “two seconds” are both correct. If the test was captured in prod but replayed in dev, different data means different counts — check the logic, not the absolute values.
- **Ordering tolerance**: A and B doesn’t have to mean A before B.
- **Tool-only completion**s: Sometimes the agent completes via tool call and says nothing at all. That can be correct.
- **Multi-instance tasks**: Ignore assignment ordering (A/B/C) unless the user specified it.

An LLM is the only thing capable of semantic evaluation when outputs can vary this much.

### Prompt-tool drift: a subtle CI problem

Here’s one we didn’t anticipate: Alyx’s prompts reference tools by name. “Call `get_trace_preview` to examine the trace.” What happens when a tool gets renamed? The agent tries to call a function that doesn’t exist. Runtime failure, completely invisible in unit tests.

We now run structured validation that cross-references tool names in prompts against actual `@llm_tool` decorators in the code:

```
```
# Extract tool references from prompts
grep -r "call \`" alyx/prompts/
# Cross-reference against actual tool definitions
grep -r "@llm_tool" alyx/tools/*.py | grep "tool_name"

			Claude Code Review runs on every PR with validation rules in [CLAUDE.md](https://arize.com/blog/claude-md-best-practices-learned-from-optimizing-claude-code-with-prompt-learning/), catching prompt-tool mismatches before they ship. Natural language bugs caught by natural language review.

### The dog-food loop

And yes, we dog-food everything. Our tests run inside Arize, test results are logged as Arize experiments, and every trace is debuggable in the same UI our customers use. If Alyx’s own evals can live in Arize, that’s a pretty good validation that our product is doing its job.

### What we learned about testing agents

- **Capture good sessions; don’t invent expected outputs**. Build the infrastructure to capture golden sessions early. Don’t wait until you need tests to figure out how to write them.
- **Match facts, not phrasing**. The AND-of-ORs pattern in OutputAssertion lets you assert semantic correctness without brittleness.
- **LLM-as-judge is necessary for trajectory evaluation**. When the agent can take different (but valid) paths to the same goal, only a semantic evaluator can judge correctness.
- **Real APIs, not mocks**. Mocks are fast but they miss the class of bugs that only show up when real systems talk to each other.

## Lesson 4: Debugging an agent is an agent-shaped problem

You deploy, and something breaks — of course it does. When Alyx misbehaves — calls the wrong tool, [hallucinates data](https://arize.com/llm-hallucination-examples/), gets stuck in a loop — the bug isn’t in a stack trace. It’s distributed across three systems:

- Arize AX shows the agent’s perspective: what the LLM saw each turn, what tools it called, what it produced.
- Datadog APM shows the server’s perspective: latencies, errors, HTTP status codes for each tool call’s backend processing.
- GCP Cloud Logging shows the infrastructure perspective: OOMKills, container restarts, gRPC deadline errors that never made it into a span.

Debugging requires all three. A human doing this manually opens Arize, finds the trace, copies a span ID, switches to Datadog, writes a query in different syntax, notes a timestamp, switches to GCP, writes yet another query syntax, and correlates the results. It’s brutal — and it’s also exactly the kind of tedious, cross-system, structured work that LLMs happen to be very good at.

### Skills: markdown runbooks for coding agents

So we built debugging skills. A skill is a markdown file that teaches a coding agent how to perform a specific task — structured instructions the LLM reads and follows, the same way an engineer reads a runbook:

```
```
.agents/skills/
├── alyx-traces/        # Export and query Arize trace data
│   ├── SKILL.md
│   └── scripts/arize_cli.py
├── datadog-debug/      # Search Datadog spans, fetch traces
│   ├── SKILL.md
│   ├── references/REFERENCE.md
│   └── scripts/dd-search-spans.sh
├── gcloud-logs/        # Query GCP Cloud Logging
│   ├── SKILL.md
│   └── scripts/safe-gcloud-logs.sh
└── env-context/        # Resolve environment aliases

			Skills are discovered automatically by Cursor, Claude Code, and Codex via symlinks from a single canonical directory. Write once, debug everywhere.

### The three-pronged debugging loop

The three skills chain together naturally:

**1. **`alyx-traces`: Start here. Pull the production session from Arize. The skill wraps a Python CLI that exports the complete trace as structured JSON — every span, every tool call, every LLM input/output. It can also open a specific span in the Arize Playground so you can replay the exact moment the agent went wrong.

**2. **`datadog-debug`: Search backend spans for the time window. The skill includes jq recipes for reconstructing call trees, extracting errors, and identifying bottlenecks:

```
```
```
# Timeline reconstruction from Datadog spans
jq '[.[] | {
  start: .attributes.start_timestamp,
  duration_ms: ((.attributes.custom.duration // 0) / 1000000 | round),
  service: .attributes.service,
  name: .attributes.resource_name,
  status: .attributes.status
}] | sort_by(.start)' .agents/tmp/*-dd-trace-*.json
```
			**3. **`gcloud-logs`: Correlate with Kubernetes pod logs at the same timestamp. Some bugs — OOMKills, container restarts, gRPC deadline exceeded — don’t show up in spans at all. They only appear in infrastructure logs.

Each skill’s output feeds the next. Here’s a real example:


“Alyx gave the wrong answer in session XYZ.”

The coding agent reads the `alyx-traces` skill, pulls the full session trace, and identifies the failing tool call. It notes the trace ID. Then it reads `datadog-debug` and searches backend spans — finds a 500 error on a GraphQL resolver. Then it reads `gcloud-logs` and finds an OOMKill two minutes before the 500. Root cause in minutes, not half an hour.

### Safety lives in the wrappers

Every skill uses wrapper scripts that enforce read-only access. `safe-kubectl.sh` rejects all mutating verbs (`apply`, `delete`, `edit`, `patch`, `scale`, `exec`, `rollout restart`), and `safe-gcloud-logs.sh` only allows `gcloud logging read`. In production environments, the skill generates the command and tells the engineer to review it before running.

All bash scripts source a shared library (common.sh) that handles environment resolution, credential management, and safety enforcement. There’s a single source of truth for mapping environment aliases (like “prod”) to GCP project IDs and Kubernetes contexts. Individual scripts never hardcode environment details.

LLMs will follow whatever instructions you give them, so the wrapper is where you put the guardrails — not the prompt, the code. Same lesson as lesson one.

### What we learned about debugging agents

- **Skills are just markdown — low cost, high value**. Writing a markdown file is not traditional engineering work, but it dramatically expands what your coding agent can do. We have 13 in our repo.
- **Composability through shared conventions**. Skills reference each other by name and assume shared conventions — output to- `.agents/tmp/`, use jq for analysis, resolve environments through- `env-context`— so the LLM chains them naturally without orchestration code.
- **Build observability before you need it**. When things go wrong at 2am, you want the debugging tools already in place.
- **Agent debugging is itself an agent-shaped problem**. Sifting through traces, spans, and logs, correlating IDs and timestamps, following a procedure to narrow down a root cause — that’s exactly what agents are built for. Use the thing you built to fix the thing you built.

## The patterns that actually matter

If we boil this down to two themes, they are:

**Context engineering** is the work of deciding what the agent knows, when it knows it, how much of it fits, and what happens when it doesn’t. The todo plan injected on every call, the LargeJson handle with structure-preserving previews, the 10,000-character hard budgets on tool output, the RecoverableExceptions that guide the agent toward better queries — all of it is context engineering, and it is most of the work.

**Testing nondeterministic systems** is the work of defining what “correct” looks like when you can’t assert exact outputs: golden sessions captured from production, OutputAssertions that match facts rather than phrasing, LLM-as-a-judge for semantic evaluation, and CI pipelines that catch prompt-tool drift. Get this right and you’ve got a system you can actually iterate on with confidence.

## Final takeaways

Four big lessons:

- **Enforce behavior in code, not prompts**. Prompts are suggestions. Tool validation is constraints. The finish gate works because finishing throws an error when tasks are incomplete.
- **Provide just enough context**. The right preview, the right handle, the right query tools. Not so much that attention degrades. Not so little that the agent has to guess.
- **Crystallize good behavior into tests**. When something works, capture it, formalize it, test it. Good behavior should be permanent, not lucky.
- **Build your debugging loop before you need it**. Skills, observability, the three-pronged debugging chain — none of it is hard to build. But you want it in place before you’re staring at a broken agent in production.

And the meta-lesson: the way you debug an agent is with an agent. Use the thing you built to fix the thing you built.

Some of this is specific to Alyx, but most of it applies to any production agent. If you’re building one, we hope this saves you at least one 2am debugging session.
