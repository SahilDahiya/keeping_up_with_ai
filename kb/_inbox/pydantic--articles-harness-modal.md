---
title: Running Pydantic AI Harness agents on Modal sandboxes
kind: blog
topic: null
subtopic: null
secondary_topics: []
summary: null
triage: null
skip_reason: null
source: pydantic
url: https://pydantic.dev/articles/harness-modal
author: Bill Easton
published: '2026-07-23'
fetched: '2026-07-24T06:55:41Z'
classifier: null
taxonomy_rev: 2
words: 1163
content_sha256: d94866c45d2d98ec678975b3ca8fbc0d7f983da34ddd73d9f1402a4e4ff99c80
---

# Running Pydantic AI Harness agents on Modal sandboxes

The agent's run on your laptop all week, and for demos and one-off tickets that was fine. Then you hand it a real one: bump a dependency with a CVE across every service that pins it, run each service's test suite, open the PRs. The agent does exactly what you built it to do. It plans the work, spawns a sub-agent per service, and forty test suites hit one Docker daemon on eight cores. The fans come on. The laptop is the bottleneck, and the agent is idling on your hardware.

The mistake was thinking the agent needs a computer. It needs computers, for about six minutes, and then it needs them to not exist.


Give the agent a shell allowlist and an `output_type`, and it can already do the small version of this ticket — one service, on your laptop, no vendor:

```
import logfire
from pydantic import BaseModel
from pydantic_ai import Agent
from pydantic_ai_harness import Shell
logfire.configure()
logfire.instrument_pydantic_ai()
class ServiceResult(BaseModel):
    service: str
    passed: bool
    failing_tests: list[str]
agent = Agent(
    'anthropic:claude-opus-4-7',
    output_type=ServiceResult,
    capabilities=[
        Shell(
            allowed_commands=['git', 'uv', 'pytest'],
            denied_commands=[],
        )
    ],
    instructions=(
        'Clone the service, bump httpx past the CVE, run the suite, and return '
        'the failing tests as data. Do not push.'
    ),
)
agent.run_sync('Ship the httpx CVE bump for acme/billing.')
```
That's a working CVE-bump agent — the shell allowlist keeps it to `git`, `uv`, and `pytest`, the `output_type` forces the report to be data. Run it and it clones, bumps, tests, reports. It's honest about its ceiling, though. Every command runs on your laptop, every test suite fights the same cores and Docker daemon, and *forty* of them at once turns your machine into a very expensive job runner. Isolation is whatever your OS decides, and a runaway install script from a compromised transitive dep is running as you. Which is where the fastest path lives.


[Modal](https://modal.com) is where the workload half goes when you want that same loop shipping across forty services instead of one. Its [sandboxes](https://modal.com/docs/guide/sandboxes) are gVisor-isolated containers you create programmatically, with sub-second scheduling, and their own pitch is specific: scale to "the parallelism that production agent systems and RL training actually demand." It behaves that way in practice — if the plan fans out into five hundred jobs, five hundred sandboxes spawn in parallel. Nobody provisions anything. When the suite finishes, the container is gone.

The harness wires it in as [ ModalSandbox](https://github.com/pydantic/pydantic-ai-harness/tree/main/pydantic_ai_harness/modal_sandbox): the agent gets command and file tools that execute inside a fresh sandbox instead of on your machine. Same three imports as the basic version, one line different:

```
import logfire
from pydantic_ai import Agent
from pydantic_ai_harness import CodeMode
from pydantic_ai_harness.modal_sandbox import ModalSandbox
logfire.configure()
logfire.instrument_pydantic_ai()
agent = Agent(
    'anthropic:claude-opus-4-7',
    capabilities=[
        CodeMode(),
        ModalSandbox(
            image='python:3.12-slim',
            sandbox_timeout=900,
            default_command_timeout=600,
        ),
    ],
)
result = agent.run_sync(
    'Run apt-get update && apt-get install -y git, then install uv with pip. '
    'Clone acme/billing, bump httpx past the CVE, run the full test suite, '
    'and report every break with a suggested fix.'
)
print(result.output)
```
Same agent, same work, and none of it happened on your laptop: every command ran in a container created for this run and torn down when it ended. `CodeMode` keeps the model's *reasoning* code in-process ([Monty](https://github.com/pydantic/monty)-sandboxed, milliseconds), and `ModalSandbox` sends the *workloads* — clone, install, test — to a real container with real cores. Two sandboxes, each shaped for what it holds.

And because the whole run is instrumented, every sandbox's work lands in the [Logfire](https://pydantic.dev/logfire) trace as spans under the sub-agent that did it, so "which of the forty suites failed" is a click, not an archaeology dig through container logs.


The fan-out is where Modal stops being a convenience and becomes the point. Put `ModalSandbox` on a sub-agent, and the plan that spawns forty of them has just provisioned forty isolated containers, without a line of infrastructure code. The orchestration stays ordinary Python — fan the candidates out, take the first to finish green, cancel the losers — and Modal supplies the bodies:

```
import asyncio
import logfire
from pydantic import BaseModel
from pydantic_ai import Agent
from pydantic_ai_harness.modal_sandbox import ModalSandbox
logfire.configure()
logfire.instrument_pydantic_ai()
class Attempt(BaseModel):
    passed: bool
    summary: str
def runner() -> Agent:
    # each runner run gets its own fresh, gVisor-isolated Modal sandbox
    return Agent(
        'anthropic:claude-sonnet-5',
        output_type=Attempt,
        instructions=(
            'Work inside the sandbox. Run apt-get update && apt-get install -y git, '
            'install uv with pip, clone the repo, apply the proposed fix, run the full '
            'test suite, and report whether it passed.'
        ),
        capabilities=[
            ModalSandbox(image='python:3.12-slim', sandbox_timeout=900, default_command_timeout=600),
        ],
    )
async def race(repo: str, fixes: list[str]) -> str | None:
    # fan the candidates out, take the FIRST to finish green, cancel the losers
    tasks = [
        asyncio.create_task(runner().run(f'Repo: {repo}. Apply this candidate fix and run the suite:\n{fix}'))
        for fix in fixes
    ]
    try:
        for finished in asyncio.as_completed(tasks):
            result = await finished
            if result.output.passed:
                return result.output.summary
        return None
    finally:
        for task in tasks:
            task.cancel()
```
Three candidate fixes, three isolated sandboxes, spun up the instant the code asks for them and gone when the suites finish. This is Modal's own pitch, not ours: *"From interactive coding agents to long-running RL rollouts, Modal Sandboxes are the execution layer AI systems need — isolated, flexible, and built to scale."* RL rollouts and agent fan-outs are the same shape: isolated containers executing AI-generated code at whatever parallelism the system demands, autoscaling from zero to a thousand and back. And when one branch needs real hardware — an embedding sweep, a fine-tune — point it at a GPU-backed Modal function: the lineup runs from T4s to B200s, used for six minutes and given back. Your code picks the structure. Modal makes it real.


Agents Week made the argument that at scale you treat agents like cattle. The same argument lands one level down: **an agent's compute should be cattle too.** A container that gets created for one task, does the task, and is destroyed is a container nobody hand-tunes, nobody patches on a weekend, and nobody mourns.

There's a security argument stacked on the economics. Agent-dispatched workloads are untrusted by definition — the agent decided what to run, and the whole point is that you didn't review it first. gVisor isolation per task means the blast radius of a bad decision is one disposable container, not your machine and not your cluster.


The laptop version costs nothing more than the model you're already paying — `pydantic_ai_harness.Shell` with an `allowed_commands` list runs on your laptop today. Install the dependencies used by all three examples with `uv add "pydantic-ai-slim[anthropic,logfire]" "pydantic-ai-harness[modal,code-mode]"`. Modal credentials in the environment (`MODAL_TOKEN_ID` / `MODAL_TOKEN_SECRET`) connect the production loop. The Modal free tier is enough to run this post's examples.

Back to the CVE ticket. The agent planned, fanned out, and the forty suites ran in the time one of them used to take locally, on containers that no longer exist. The laptop's job was to hold the conversation.

The agent didn't need a bigger computer. It needed the computer to stop being a place.
