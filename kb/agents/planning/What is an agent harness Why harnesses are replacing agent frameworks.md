---
title: What is an agent harness? Why harnesses are replacing agent frameworks
topic: agents
subtopic: planning
secondary_topics:
- product-engineering/architecture
summary: Explains why agent harnesses are replacing simple framework use as the unit
  of production agent engineering.
source: arize
url: https://arize.com/blog/what-is-an-agent-harness-why-harnesses-are-replacing-agent-frameworks/
author: Laurie Voss
published: '2026-06-18'
fetched: '2026-07-11T04:56:47Z'
classifier: codex
taxonomy_rev: 1
words: 1462
content_sha256: 5032002dfe753e2fce6750396856c4ad3bd0bb9129d36af8e3756d975f35a677
---

# What is an agent harness? Why harnesses are replacing agent frameworks

The key work in [agent systems](https://arize.com/blog/llm-observability-for-ai-agents-and-applications/) has moved up the stack. For the last two years the focus was on how you phrased a model call and which Python wrapper you chained it through. It is now in the layer above that, the harness: the control loop that wraps the model and decides how it decomposes a task, retries, isolates execution, manages its own context, and reports what it did. The abstraction worth owning has climbed from the prompt to the harness, and that shift has been everywhere in the last few weeks: from LlamaIndex, LangChain, Anthropic, Arena, Cognition and others. These are not folks who usually agree on things!

Harnesses as the real product surface changes where reliability gets won. The harness is also where things break, which makes [harness behavior](https://arize.com/blog/improve-ai-agents-traces-evals-harness/) an [observability and evaluation](https://arize.com/docs/ax/core-workflows) problem rather than a prompt-tuning one. What does that mean for you?

**Everyone arrived at the same place**

First, the people who just said it outright.

Jerry Liu, co-founder of LlamaIndex (and my former boss), has openly pivoted away from the thing that made the company famous. He now argues that the scaffolding era is collapsing and context quality is the new moat, because models reason over messy data well enough that [there is less need for frameworks to compose deterministic workflows](https://venturebeat.com/infrastructure/the-ai-scaffolding-layer-is-collapsing-llamaindexs-ceo-explains-what-survives). Watching the framework’s own founder call time on heavyweight frameworks is not a small thing.

Harrison Chase and the LangChain team landed on the same noun from the other direction, with the line “if you’re not the model, you’re the harness.” Mitchell Hashimoto gave the practice its name earlier this year when he wrote about “harness engineering,” the idea that when an agent fails you change its environment so the failure cannot recur.

The practitioner version showed up as a widely shared clip from Boris Cherny: “I don’t prompt Claude anymore. I have loops running that prompt Claude and figuring out what to do. My job is to write loops. And this is transition we’re going to see for the rest of the year.”

Elvis Saravia, co-founder of DAIR.AI, put it concretely after Claude Code shipped dynamic workflows: [“The idea of generating harnesses on the fly is so compelling that I reverse-engineered it for my agent orchestrator.”](https://x.com/omarsar0/status/2062553527730540611) Then he built a dashboard to track the resulting tasks and metrics.

Everybody is using the same language to describe the same trend.

**What a harness actually is**

In [What is an agent harness](https://arize.com/blog/what-is-an-agent-harness/), Aparna Dhinakaran draws the line cleanly: frameworks like LangChain and LangGraph “are frameworks designed for humans to build agents. They give you abstractions, configuration options, and a lot of rope.” A harness starts from the opposite end. It “was born bottom-up out of coding agents, solving real-world problems with working agents,” and Cursor, Claude Code, Windsurf, and Codex all converged on the same shape: “A while loop that calls tools. A context manager that compresses history. A permission layer that keeps things safe.”

The distinction that matters for this argument is that a harness works out of the box and a framework does not. You assemble a framework; a harness ships as a running agent and the human provides only the goal. That is exactly why the leverage moved up: the interesting engineering is no longer in wiring the components, it is in the loop that the vendor already wired.

There was progress this week on several important parts of the [harness architecture](https://arize.com/blog/closing-the-loop-coding-agents-telemetry-and-the-path-to-self-improving-software/):

**Better task decomposition.** Work out of CMU on multi-agent computer use argued that computer-use agents should be built with a manager that decomposes the task and dispatches parallel subagents rather than running one monolithic loop. Russ Salakhutdinov’s summary reports the framework [lifts success rates by 3.4 to 25.5% and runs up to 1.5x faster on long-horizon tasks](https://x.com/rsalakhu/status/2062194674794668066). Same models, better-structured loop.

**Execution sandboxes.** The runtime where agent code executes is now a product in its own right. LangChain shipped [LangSmith Sandboxes to general availability](https://www.langchain.com/blog/langsmith-sandboxes-generally-available). Google opened up [Managed Agents in the Gemini API](https://blog.google/innovation-and-ai/technology/developers-tools/managed-agents-gemini-api/), where a single call spins up an agent that reasons, runs code, and manages files in an ephemeral Linux sandbox. Tellingly, Google ships it “powered by the Antigravity harness,” using the word as a product noun.

**Bash composability as a core primitive.** Hugging Face benchmarked the `hf` CLI against an agent hand-rolling `curl` or the Python SDK, they found that on complex multi-step tasks [the no-CLI baseline burned up to six times as many tokens](https://huggingface.co/blog/hf-cli-for-agents). A good CLI composes a chain of REST calls into a few high-level commands, so the agent expresses intent instead of re-deriving the call sequence every run.

**Traces as artifacts.** The execution record is becoming a first-class object. Julien Chaumond released [SynthTraces](https://x.com/julien_c/status/2062524414034423969), which he describes as “a tiny harness where two models talk to each other,” an open model playing the coding agent and a local model playing the user, producing more than 2,000 published session traces. Once traces are artifacts you keep, publish, and grade rather than logs you tail, you are most of the way to treating the harness as something you evaluate.

**The proof is in the failures**

The strongest evidence that the harness now determines product quality is what happens when harness behavior goes wrong with the model held constant.

On June 1, Anthropic [reset the 5-hour and weekly rate limits for all Pro and Max users after fixing a bug that caused some Claude Code sessions to spawn excessive parallel subagents](https://pasqualepillitteri.it/en/news/3995/claude-code-resets-usage-limits-opus-4-8-not-dynamic-workflows), burning through usage faster than expected. The detail that makes this a harness story rather than a model story: the bug hit sessions that were not using the opt-in dynamic-workflows feature at all, so the cause was orchestration behavior in how Opus 4.8 sessions handled parallel calls, not the model’s reasoning and not a feature anyone deliberately turned on. The difference between a productive session and one that incinerated a weekend’s quota lived entirely in the loop **around** the model. It shows harness quality matters in production, at scale.

**Measurement is the unlock**

If the harness is the product, the harness is what you instrument, and the metrics that matter are operational rather than benchmark accuracy on a fixed test set: success rate, retries, tool efficiency, recovery from errors, tool hallucination, and cost per successful trajectory.

The most rigorous example is Arena’s new [Agent Arena leaderboard](https://arena.ai/blog/agent-arena-methodology/), which ranks agents from real Agent Mode sessions rather than pairwise votes. Its five launch signals read almost like a definition of what [harness observability](https://arize.com/docs/ax/observe/tracing) should track:

- **Confirmed success**: the user marks the task done or not.
- **Praise vs. complaint**: explicit positive feedback outweighing negative.
- **Steerability**: whether the agent executes on a mid-task correction.
- **Bash recovery**: how many turns it takes to recover from a self-inflicted shell error.
- **Tool hallucination**: calling a tool that does not exist.

The same instinct is showing up commercially. Weights & Biases [rebuilt Weave from the ground up as agent-first observability](https://wandb.ai/wandb_fc/product-announcements-fc/reports/New-in-W-B-Weave-Observability-and-continuous-improvement-for-production-agents--VmlldzoxNzAzMTcxNg) with out-of-the-box signals that surface failure modes across common harnesses. And Cognition put money behind harness-level value measurement: an [AI Productivity Guarantee that funds a customer’s Devin usage up to $10M if it delivers less engineering value than they paid for](https://cognition.ai/blog/ai-guarantee), with value scored by an agent that estimates each session in hours of productive output. That estimator was [validated against time estimates from 126 users across eight enterprise deployments and deliberately calibrated to underestimate](https://cognition.ai/blog/ai-productivity), the conservative direction for a number you are underwriting. You do not put a financial guarantee behind a metric you cannot measure.

This reframes what an [evaluation product](https://arize.com/blog/what-is-an-evaluation-harness/) is for. The interesting question is no longer only whether the final answer matched the gold label. It is what the trajectory did along the way: where retries clustered, which tool calls were wasted, where the agent recovered and where it gave up. That is the same argument for instrumenting the loop with [spans and traces](https://arize.com/docs/ax/observe/tracing) that platforms like [Arize AX](https://arize.com/docs/ax) are built around, and the case [I made earlier](https://www.linkedin.com/feed/update/urn:li:activity:7467381033206812672/) that outcome-only scoring leaves most of the diagnosis on the table. When the harness is the product, the trace is the primary evidence.

**What this means for you**

Stop tuning prompts in isolation. The labor in agent engineering has moved up the stack into the loop, and the loop is where your reliability now lives. Pick the [operational metrics](https://arize.com/docs/ax) that describe how your agent behaves, not just whether it eventually answered: success rate, retries, tool efficiency, recovery, tool hallucination, and cost per successful trajectory. Instrument those, watch the trajectories rather than the outcomes, and treat every repeated failure as a harness change rather than a prompt to retry. The framework era taught us to compose calls. The harness era is about measuring what happens when they run, and that is the work worth investing in now.
