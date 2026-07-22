---
title: Devin Outposts on Modal | Modal Blog
kind: blog
topic: null
subtopic: null
secondary_topics: []
summary: null
triage: null
skip_reason: null
source: modal
url: https://modal.com/blog/devin-outposts-run-devin-in-modal-sandoxes
author: null
published: '2026-07-21'
fetched: '2026-07-22T06:51:24Z'
classifier: null
taxonomy_rev: 2
words: 587
content_sha256: 93261a20a755483bcbd3ac9a099e706d03c45d698e7a28afc27bfcc5868bca05
---

# Devin Outposts on Modal | Modal Blog

[Back](https://modal.com/blog)

# Devin Outposts on Modal

[Adam Azzam](https://twitter.com/aaazzam)

Devin, built by Cognition, is an AI software engineer: it plans, writes, tests, and ships code semi-autonomously.

*How* an engineer works depends on the job in front of them. A data engineer needs a machine with a private connection to Snowflake, while an ML engineer needs a devbox with a GPU. The machine we reach for is a function of the *job to be done*, and Devin is no different.

Devin's default environment, hosted and managed by Cognition, is what most sessions run in today, and it's built to handle the bulk of software engineering work well. Today, Cognition is extending that with Devin Outposts, which lets Devin's execution move into an environment you control and configure, while Devin's reasoning stays in Cognition's cloud.

We're excited to be a launch partner for Devin Outposts. With `modal-devin`, our open-source integration, Devin Outpost sessions run in a Modal Sandbox. You get Modal's fast cold-starts, [custom images](https://modal.com/docs/guide/images), [various snapshotting techniques](https://modal.com/docs/guide/sandbox-snapshots), [cost-efficient bursting mechanisms](https://modal.com/docs/guide/resources#billing) and [million-sandbox scale](https://modal.com/blog/scaling-to-1-million-concurrent-sandboxes-in-seconds) while keeping the convenience of Cognition's managed Devin Cloud experience. It's live in alpha starting July 21, 2026.

Consider a task like:

Figure out an optimal serving config for Qwen3.6-35B-A3B on this box; we're targeting the lowest time-to-first-token we can get at ~5–8 concurrent users.

On Cognition's default sandbox, this fails immediately: there's no GPU, so the serving engine never starts. On a Modal-backed Outpost, it's one more task Devin can pick up: Modal spins up a GPU-backed Sandbox on demand for the session, then scales back to zero when it's done.

### Environmental Engineering with `modal-devin`

`modal-devin` is Modal's open-source library and CLI for running Devin Outposts.

A queue connects each Devin Cloud session to the machines you operate. Cognition calls that queue an "outpost" (a control plane for you orchestration nerds). `modal-devin` implements the execution side (the data plane) as an ordinary Modal application: an orchestrator function watches your outpost for queued sessions, and starts a worker, an isolated Modal Sandbox, to run each one.

With `modal-devin` ,

**Devin arrives with your actual toolchain already set up.** Build its image the same way you build any Modal image: your repo already cloned, your dependencies already installed, your internal registries already wired up. It ships with the Devin CLI, FFmpeg, and Chromium already installed, so screen recording and Devin's live desktop view work without any extra setup.

**Devin picks up where it left off.** Suspend a session and `modal-devin` snapshots the whole workspace, files, installed tools, everything. Resume it later and there's no re-cloning the repo or reinstalling dependencies.

**One command sets up your outpost.** Standing up secure infrastructure for an agent to run on your own machines usually means real work: a queue watcher, credential handling, sandboxing, lifecycle management. `uvx modal-devin init` does all of it, and generates code you own and can keep customizing: a `scheduler` function (the orchestrator from above) and a `session` function (the worker):

```
@app.function(
    name="session", 
    image=image, 
    secrets=[devin_secret],
    timeout=worker.session_function_timeout_seconds
)
def session(session_id: str) -> None:
    worker.run_session(
        session_id, 
        app=app, 
        image=image, 
        gpu="H100"
    )
@app.function(
    name="scheduler", 
    image=controller_image, 
    secrets=[devin_secret],
      schedule=modal.Period(seconds=worker.settings.scheduler_interval_seconds),
    max_containers=1
)
def scheduler() -> None:
    worker.dispatch_pending_sessions(session.spawn)
```
**Each team gets its own outpost.** Run `uvx modal-devin init` again for each team or environment, say once for frontend and once for backend. Each gets its own deployment and its own credentials, with no visibility into the other's secrets or sessions.

## Get started

`uvx modal-devin init`Requirements: [uv](https://docs.astral.sh/uv/getting-started/installation/), Python 3.11+, a Modal account, a Devin organization with Outposts enabled. Full documentation is at [modal.com/docs/devin](https://modal.com/docs/devin).
