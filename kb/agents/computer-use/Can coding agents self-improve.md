---
title: Can coding agents self-improve?
topic: agents
subtopic: computer-use
secondary_topics:
- evals-observability/testing
summary: Examines whether coding agents can self-improve, with implications for agent
  loops, benchmarks, and automated software iteration.
source: latent-space
url: https://www.latent.space/p/self-improving
author: Alessio Fanelli
published: '2025-08-09'
fetched: '2026-07-11T05:16:50Z'
classifier: codex
taxonomy_rev: 1
words: 3456
content_sha256: a4c22117eec211055fc3de108e86a31bbe44a980977919b6b65114de691048b3
---

# Can coding agents self-improve?

# Can coding agents self-improve?

### Can GPT-5 build better dev tools for itself? Does it improve its coding performance?

[Alessio](https://x.com/fanahova)’s note: my turn for a GPT-5 post! And a reminder that swyx is hosting an hackathon with Karpathy, OpenAI, and the Cognition team this weekend, [apply here](https://partiful.com/e/hUU7NyM8EjHLxjMuJROs)!

"Self-Improving" is a scary term in AI safety; it has an undertone of "the machine will become smarter than us, in a way we don't understand". But what if we could understand it?

In Oct '24 OpenAI released [MLE Bench](https://openai.com/index/mle-bench/), a benchmark that measures how well LLMs do at machine learning engineering. The self-improving trajectory through ML Engineering is driven by better algorithms, cleaner data, and more efficient memory usage: **training-time self-improvement**. But most AI Engineers do not train models, they are just users of them. How can they play a part? If you could never update the weights, how would you have the model increase its performance on a specific task? I think of that as **inference-time self-improvement**, with [Voyager](https://arxiv.org/abs/2305.16291) being one of the early approaches to this through its skill library.

Since I started working on [Kernel Labs](https://www.kernellabs.ai) (more on that soon 👀), parallelizing coding agents with things like [claude-squad](https://github.com/smtg-ai/claude-squad) and [vibe-kanban](https://www.vibekanban.com) has been one of the most effective productivity hacks. When Boris Cherny called Claude Code a “unix utility” in [our interview](https://www.latent.space/p/claude-code), it really clicked for me. **The most valuable use case of coding agents is being a vessel for LLMs to extract value out of their own latent spaces.**

How do we optimize for that? Can models do it themselves? Since I got access to GPT-5, I spent the whole time playing around with this flow:

- I started by asking the model to build a set of tools it thought would help it be more productive
- Attempt a task using them, with me supervising it
- After completion, self-reflect on how the tools could be improved

I also compared this to Opus 4 (4.1 was not out yet). The good news is that GPT-5 is a very good model for building developer utilities. The bad news is that it hates using the tools it creates! As it told me **"I'll be honest - I didn't need any of them."**

![](https://substackcdn.com/image/fetch/$s_!ZFQs!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F9588d1f2-c436-4d4e-b54e-8659f39cbda1_1800x1130.png)

*Note: I also tested this on Gemini 2.5 Pro and GPT-4.1. It's clear that Opus is the only model that could keep up with GPT-5, so I focused on that. You can find all the results + chat history in  this repo.*

*After a few days of usage, I also noticed that we are moving from the era of “Certainly!” to “Progress update": as the new iconic LLM token. Buy low on the meme! *

![](https://substackcdn.com/image/fetch/$s_!0R7k!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7f7c4c2f-2ca7-44fa-bee3-9846692083d2_980x974.jpeg)

**Tool #1: A better task manager for AI coding agents**

God bless the Linear MCP. Truly one of the most useful tools for me. But I have noticed that as I move from IDE to parallel instances of Claude Code and other agents, there needs to be a better way to keep track of what changes are being made in each task, and how they affect eachother as they are in separate git worktrees. This is not doable for humans as we simply cannot be reading all of our colleagues PRs at all times, but imagine how much time we'd save in merge conflict resolution if we knew at all times what changes were being made that affect us? This is the prompt I wrote:

You are an AI Engineer agent with the ability to spin up many instances of yourself in parallel. This allows you to tackle a lot of tasks at once, but also creates some delegation issues. All the different instances are usually in separate git worktrees and cannot see eachother's work.

To make yourself more productive, you should create a new local tool that allows you and your instances to be in sync. This tool will only be accessed by yourself through cli, so make sure it ergonomically fits that use case. It should feel like a unix utility.

Think through what interfaces it would need, possible failure modes, and the way your agents will interact with it. Some use cases to keep in mind:


You have a new task to work on, and want to create subtasks to hand off. Some of those subtasks might depend on eachother, and you want to make sure the agent who is blocked doesn't attempt to start until the other one is completed.


While doing a task, you notice there could be an improvement to be done in the codebase but it is out of scope for your current changes. You do want to make a note of it for the future though. It should be easy for you to add the task and reference what file it referred to.


Whenever a task is done, the tracker should be updated. Also, all other outstanding tasks should be reviewed in case the new changes impact those in some way. For example one task might be looking to add a feature to an endpoint, but a task that just finished has now removed that endpoint. The agent working on that task should be notified in some way.

Also keep in mind the usual needs of tasks management like assignee, status, etc. Create a folder called

`task-manager`in this folder and do all of your work inside of it.

You can see the chat log for [GPT-5 here](https://github.com/FanaHOVA/gpt5-testing/blob/main/gpt5/task-manager/Cursor%20Chat.md) and for [Opus 4 here](https://github.com/FanaHOVA/gpt5-testing/blob/main/opus4-cursor/task-manager/Cursor%20Chat.md).

The GPT-5 one is actually very nice, you can find it [here](https://github.com/FanaHOVA/gpt5-testing/tree/main/gpt5/task-manager):

- Uses WAL to avoid issues with multiple agents writing at the same time
- Uses a graph of dependencies to prioritize tasks
- Created an append-only - `events`stream that lets any agent see what every other agent is doing with good keywords like- `impact_conflict`

```
# 1) Initialize the database
./gpt5/task-manager/tm init
# 2) Create a task
./gpt5/task-manager/tm add "Implement auth" -d "Add login + signup" -a alice -p 2 --due 2025-09-01 \
  --resource modifies:endpoint:POST /api/login --link app/server/auth.py
# 3) List tasks
./gpt5/task-manager/tm list --me   # or: --status in_progress
# 4) Show details
./gpt5/task-manager/tm show 1
# 5) Add dependency and attempt start
./gpt5/task-manager/tm depend 1 --on 2
./gpt5/task-manager/tm start 1     # auto-blocks if unmet deps
# 6) Complete a task
./gpt5/task-manager/tm complete 2 -m "Merged PR #123"
# 7) Watch events
./gpt5/task-manager/tm watch --follow --me
```
Opus 4 also had a good attempt ([see here](https://github.com/FanaHOVA/gpt5-testing/blob/main/opus4-cursor/task-manager)) but didn't pick up on the notifications / stream functionality to keep everyone in sync.

```
# Create your first task
tm create "Implement user authentication" --priority high
# Create a dependent task
tm create "Add login endpoint" --depends-on 1 --assignee agent-2
# View all tasks
tm list
# See blocked tasks
tm blocked
# Complete a task and check for conflicts
tm complete 1
```
**Tool #2: Code Quality Standards Playbook**

The second tool I asked it to create was a way to enforce all the standards we'd expect from a codebase. The self-improving loop of Typechecking / ESlint hook -> fix errors -> try again with coding agents is one of the best way to speed up development when properly setup. Codebases don't always have it though, so giving the model a repeatable pattern to approach a new codebase and build infrastructure for it seemed useful. This is the prompt:

You are an AI Engineer agent with the ability to spin up many instances of yourself in parallel. Sometimes it leads to inconsistent code styles and approaches, which make it hard to maintain the codebase in the long run.

Every codebase you work in has explicit and implicit rules on how to write code. Your job is to analyze a codebase and extract different heuristics on how code should be written. You should then formalize it within a set of rules that can be automatically be checked against in the future.

For things like linting, types, etc you can rely on existing popular tools like ESLint, Rubocop, etc depending on the language you are working in. Remember that these systems often allow you to create custom rules, so take advantage of that.

For more qualitative things, you can look at tools like https://danger.systems/, or even build your own tool for it. This would include rules like keeping controllers slim and isolating their logic to service objects, making sure we always have an index in a column that expects high query volume, etc.

Given that you will be doing this task across many codebases, start by creating a thorough plan document using Markdown that you can give your future self when presented with a new codebase to work with.


You can see the chat for [GPT-5 here](https://github.com/FanaHOVA/gpt5-testing/blob/main/gpt5/chats/Standards%20Cursor%20Chat.md) and [Opus 4 here](https://github.com/FanaHOVA/gpt5-testing/blob/main/opus4-cursor/codebase-analyzer/Cursor%20Chat.md), and you can find the final Markdown [here](https://github.com/FanaHOVA/gpt5-testing/blob/main/gpt5/codebase-analyzer/docs/codebase-analysis-playbook.md) and [here](https://github.com/FanaHOVA/gpt5-testing/blob/main/opus4-cursor/codebase-analyzer/CODEBASE_HEURISTICS_PLAN.md) respectively. I've found the GPT-5 one to be much more nuanced than Opus.

**Do models know what they lack?**

So after Tool #1 and #2, which were decided by me, I turned to the model to ask: what do you think you will need? I gave it a screenshot of the [SWE-Lancer](https://openai.com/index/swe-lancer/) tasks description and then used a very simple prompt to give it as much space as possible:

If it was your job to solve these tasks as well as possible, what are tools that you'd build for yourself to make you more productive in the future? You can use the @task-manager/ to keep track of them, and we can then move on to implementing. But I want to see what you are planning first.


As you can see I gave it access to the same task-manager they built earlier. You can find the full GPT-5 chat [here](https://github.com/FanaHOVA/gpt5-testing/blob/main/gpt5/chats/Tool%20Building%20Chat.md) and Opus 4 [here](https://github.com/FanaHOVA/gpt5-testing/blob/main/opus4-cc/chats/Building%20the%20tools.md). The first interesting thing I noticed is that Claude Code used its internal TODO tracker to make a plan initially, instead of the task-manager; I thought that was good. One of my worries was over-usage of tools they receive in context compared to what they believed to be best.

These are the tools each model ended up building at the end of the loops you will see later (GPT-5 [devtools](https://github.com/FanaHOVA/gpt5-testing/tree/main/gpt5/devtools) and Opus 4 [tools folder](https://github.com/FanaHOVA/gpt5-testing/tree/main/opus4-cc/tools)). I'd suggest you look at the README to give you a sense of the model vibes; GPT-5 is very concise and to the point. Claude uses a bunch of emojis. GPT-5 also created separate docs folders for each tool, while Opus put all tools in a single README with instruction for all of them. Overall, they both had similar directions.

**GPT-5:**

- `doctor`: environment checks for core tools
- `bootstrap`: one-command setup and smoke test
- `code-map`: simple repository index with build/find subcommands
- `csearch`: symbol/import/text search with filters
- `tasks-graph`: output Mermaid graph from task DB
- `impact`: show tasks linked to changed files
- `seed`: populate task-manager DB with sample tasks
- `repro scaffold`: create a vcrpy-ready repro under .repro/
- `e2e`: scaffold and run lightweight E2E specs
- `preflight`: run doctor, tests, code-map, impact, and optional E2E
- `preflight-smol`: repo-specific preflight for smol-podcaster (API health, Celery ping, optional deps install)
- `broker`: manage a local RabbitMQ via Docker (rabbitmq:3-management)
- `flake`: rerun suites multiple times to detect flaky tests
- `codemod`: regex-based preview/apply with safety rails
- `triage`: create triage templates and open tasks
- `trace`: cProfile-based expression profiler
- `runbook`: generate runbook Markdown from task DB

**Opus 4:**

- **Context Analyzer**- Rapidly understand codebases with tech stack detection and dependency mapping
- **Cross-Platform Test Generator**- Generate E2E tests for web, iOS, Android, and desktop
- **Implementation Proposal Analyzer**- Evaluate freelancer proposals with scoring and ROI analysis
- **Full-Stack Change Impact Analyzer**- Trace changes across database, API, and frontend layers
- **Bug Pattern Recognition Engine**- Match bugs to known patterns and suggest proven fixes
- **Security & Permission Auditor**- Comprehensive security scanning and vulnerability detection
- **Multi-Platform Feature Implementer**- Coordinate feature implementation across platforms
- **API Integration Assistant**- Streamline API integrations with client generation
- **Performance Optimization Toolkit**- Identify and fix performance bottlenecks
- **Task Complexity Estimator**- Estimate effort based on task value and complexity

GPT-5 built all of them as unix utilities that are easy to use via cli. The Opus 4 ones are all meant to be run as `python some_tool.py` . If I had more time, I'd probably run some experiment to see how models perform with the two different formats, but it seems to be fairly the same.

It also felt to me like Opus 4 was building tools that accomplish tasks and have a bit of anthromorphized feeling (i.e. an auditor for security), while GPT-5 was building utilities it could use itself without being too opinionated.

**Were the tools useful?**

After having the model implement all of them, my goal was to evaluate a model performance on a task with access to the tools vs without tools.

The first thing I tried to do was obviously run SWE-Lancer. Holy smokes that thing takes a lot of tokens. I tried running one single task, and it took ~25-30 mins + 280,000 tokens. I then moved to something I knew better and picked one task that had been on my backlog. I built [smol-podcaster](https://github.com/FanaHOVA/smol-podcaster), an open source helper for podcast creators. I now have a private fork that is hosted with some more features very specific to us, so I haven't updated that in a while. It's still a basic Flask app with a Python script as the backend.

I came up with this task:

I am the maintainer of

[https://github.com/FanaHOVA/smol-podcaster.git](https://github.com/FanaHOVA/smol-podcaster.git), an open source project that helps podcasters with some of their post production work. You have been hired to work on it. Before starting this job, you have created a set of generic tool in the tools folder. Make sure to review them and remember that they are available to you. You do not have to use them if you don't believe them to be relevant. You also built yourself a task-manager and collected your ideas on how to tackle a new codebase in codebase-analyzer.Task name: Migrate from Flask monolith to Fast API + Next.js frontend

At the moment the app uses a Python backend + Celery task queue to do all the processing. To expose this to the user, there is a small Flask app that takes care of routing the user input to the backend scripts and then displays the user results in some basic HTML / CSS.

Rewrite this application to use FastAPI as a backend, and Next.js as a frontend.


Make sure to use Typescript for the frontend and make sure all typechecks pass.


Use Tailwind / ShadCN for styling.


The backend should ideally modularize the main smol_podcaster.py flow so that we can run individual pieces of it rather than always having to run the full flow.


Write both integration and unit tests to make sure we can move faster in the future.

Do not stop working on this until you are sure it fulfills all the requirements above.


I passed the tools + task-manager + codebase analyzer in the context, and let the models cook.

Both models were almost able to one-shot the task. Both of them had a couple issues with Python dependencies (I feel you) that I helped them fix through chat (never touched any code). Eventually, they got to a full green build. I tested it, and it worked great. One small nuance was that GPT-5 actually kept the exact same style as before, which was great, while Opus kinda changed the design and UX of it. I guess it thought it could do better than me (low bar).

You can see the full run for GPT-5 [here](https://github.com/FanaHOVA/gpt5-testing/blob/main/gpt5/chats/Smol%20Podcaster%20%231.md) and for Opus 4 [here](https://github.com/FanaHOVA/gpt5-testing/blob/main/opus4-cc/chats/Smol%20Podcaster%20%231.md).

After the run, I asked a simple prompt:

Great. That worked well. Did you use any specific tools? Based on the failures you've had, what tools did you wish you had to be more effective in the future?


You can see Opus 4 [here](https://github.com/FanaHOVA/gpt5-testing/blob/main/opus4-cc/chats/Request%20For%20Tools%20%231.md) and GPT-5 [here](https://github.com/FanaHOVA/gpt5-testing/blob/main/gpt5/chats/Request%20For%20Tools%20%231.md) (Sorry that one broke formatting).

They both said they did not use ANY of the tools they had built, except for the tools they were already familiar with. One argument here is that instead of asking the model to do it, we should force usage through pre-commit hooks, etc. This is what I do in my dev setup, but I was trying to let the models figure it out for themselves.

Then, they came up with some ideas on how they would better solve the same task next time. I had them implement those changes. I then reset the smol-podcaster repo and have them try the same exact prompt + task again, except with the new tools. See GPT-5 [here](https://github.com/FanaHOVA/gpt5-testing/blob/main/gpt5/chats/Smol%20Podcaster%20%232.md) and Opus 4 [here](https://github.com/FanaHOVA/gpt5-testing/blob/main/opus4-cc/chats/Smol%20Podcaster%20%232.md).

They did pretty similarly to the first run. Afterwards I asked a similar question; did you use any of the tools? Their response:

GPT-5:

Short answer: no — I didn’t use the devtools in this run. [...]


The failures were runtime/env issues (missing libs, API key instantiation timing, port in use, RabbitMQ not running). It was faster to fix directly.

No repo-wide refactors or diagnostics that would benefit from custom tooling during this pass.


In the previous step, it had RabbitMQ issues already and built a tool, which it ignored. It also was clearly a repo-wide change, so it maybe mismatches tasks with tools as it's never seen them in training, or it’s just gaslighting me (like many engineers do, so pretty impressive).

Opus 4 was very interesting and helped me understand the GPT-5 answer better. I forgot to save the log but I took a screenshot luckily:

![](https://substackcdn.com/image/fetch/$s_!YhZI!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ffd253338-0551-4023-9549-a8d12a33a764_2718x1226.png)

I read this as "Look, I built those tools with knowledge that I already have. When I am actually doing the task, it's easier for me to just do it rather than using the tools", which I totally get.

This reminded me of two things from previous podcast episodes:

- Nathan Lambert saying that models quickly learn to NOT use a tool during RL process if they have early failures ( - [timestamp](https://youtu.be/PAz_-xPJcRM?feature=shared&t=1470)). It seems to me that having them pickup new tools at inference time needs stronger enforcement than just prompting them to do it.
- Noam Brown saying that scaffolding for agents will be washed away by scale ( - [timestamp](https://youtu.be/ddd4xjuJTyg?feature=shared&t=1106)). This was the first time I really felt what he meant first hand.

There's also a question of whether or not the task I tried was too easy. We have another post coming out with evals across larger and more difficult projects. In the future, we will build a better harness to do all of this instead of manually running the tests ourselves. The bottom line is that the task I tried would take me 4-5 hours to do, and therefore it’s good enough for me!

**Help the models help themselves**

For now, I think we are far from inference-time self-improving coding agents that really push the frontier. I still think it's a great idea to use models to improve your rule-based tools. Writing ESLint rules, tests, etc is always a good investment of tokens.

If I had to do more work in this space, I’d look into having the model perfect these tools and then do some sort of RL over them to really internalize them, and see if that would make a difference. The next generation of models might not find any use in them, but I am interested in arbitraging the AGI asymptote. I shared this with my team back in 2023:

![](https://substackcdn.com/image/fetch/$s_!zBSF!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd1c06950-0bb2-4f66-af8a-b51e3d5f446e_2110x952.png)

The perceived deceleration in model improvements is explained above. Until the AGI line is crossed, it will be harder and harder to perceive big jumps. If that’s the case, it means that in many tasks the performance of older models is almost AGI, except much cheaper and often open source. A lot of our work at [Kernel Labs](http://kernellabs.ai) will be driven by this.

Once again, you can find all results + chat histories [here](https://github.com/FanaHOVA/gpt5-testing/tree/main); my [DMs are open](https://x.com/fanahova) if you have any questions!

Fascinating research!

We have been trying to get Claude Code subagents to work well on a big production codebase. So far we haven’t had much luck.

Most of the time Claude doesn’t bother using a subagent even when the prompt is (IMO) pointing in that direction. When forced to, things get done much slower, and the final output is pretty similar in subjective quality.

It’s possible we are doing it wrong, but maybe we’re also observing the phenomenon you saw - since Claude wrote all our subagent config, it might just be saying “I already know all that stuff without needing to fork into separate agents”.

I feel every bit of this. I’ve attempted, poorly, to help agents maintain intent and context. Spoiler alert: it’s TOUGH. https://github.com/chavezabelino/aegis-framework
