---
title: 'Code is free, technical debt isn’t: Notes from AI Engineer Europe'
topic: industry
subtopic: trends
secondary_topics:
- evals-observability/testing
summary: AI Engineer Europe notes arguing that faster code generation increases the
  need for verification, standards, and technical-debt management.
source: arize
url: https://arize.com/blog/code-is-free-technical-debt-isnt-notes-from-ai-engineer-europe/
author: RL Nabors
published: '2026-04-20'
fetched: '2026-07-11T04:55:29Z'
classifier: codex
taxonomy_rev: 1
words: 968
content_sha256: 3d5cf25db2494a733afb6b578d5d2193da922a5668295a42330e3968cbef3e6d
---

# Code is free, technical debt isn’t: Notes from AI Engineer Europe

Keynotes at [Europe’s first flagship AI Engineer Conference](https://www.ai.engineer/europe) shared one theme: **code generation has accelerated past our ability to verify it, and the industry is quietly reorganizing around that fact.** The smartest practitioners on stage and YC’s president are converging on the same answer.

This post is a field report from three days in London and an argument about why quality is the work now. If you need recordings, we have them! (Check out [Day 1](https://www.youtube.com/watch?v=O_IMsEg91g8) and [Day 2](https://www.youtube.com/watch?v=_zdroS0Hc74).)

## Code is free…

“Code is free. And it is not a thing to get hung up on anymore.”—[, OpenAI](https://www.linkedin.com/in/ryanlopopolo/)Ryan Lopopolo

[ Sarah Chieng](https://www.linkedin.com/in/milksandmatcha/) (Cerebras) shared that Codex Spark generates code at

**1,200 tokens per second**, roughly 20× the typical Sonnet-family rate. At that speed, you can’t watch 10 agents at once, and you don’t need to.

“We are in the fuck around and find out phase of coding agents.”—[, former game developer and creator of](https://mariozechner.at/)Mario Zechner[Pi](https://github.com/badlogic/pi), the minimal harness powering[OpenClaw](https://openclaw.dev/)

Every engineer now has access to anywhere between 50 and 5,000 engineers’ worth of implementation capacity. PRs are stacking up. Code is stacking up. **The scarce resource is no longer producing code but the capacity to review it** and maintain the quality of a codebase.

## …but unreviewed code is expensive

“Slow the fuck down. Everything’s broken.”—Mario Zechner

“Bad code is the most expensive it’s ever been.”—[, educator and founder of](https://x.com/mattpocockuk)Matt Pocock[AI Hero](https://www.aihero.dev/)

“The friction is your judgment.”—[&](https://ronacher.eu/)Armin Ronacher[,](https://www.cristinaponcela.com/)Cristina Poncela Cubeiro[Arendil](https://www.arendil.ai/)

There are four “smells” coming from orgs adopting agentic coding at scale and open source projects inundated with generated PRs:

**1. Review can’t keep up with generation.** Producer-to-reviewer ratios are broken. Engineers can ship 5,000-line PRs that no one can meaningfully audit. Rubber stamping becomes the norm, and bugs and security issues ship regularly with teams in “hopes and prayers” mode.

**2. Agents don’t feel pain.** Humans write defensive code because shipping a bug hurts. Agents are rewarded for making code *run* and pay none of tomorrow’s cost for today’s shortcuts. Zechner’s examples: agents cheerfully add backwards-compatibility scaffolding nobody asked for and silent fallbacks to default configs that corrupt production data two hours later.

**3. Codebases become illegible.** Arendil made the argument that your codebase *is* infrastructure. If the code isn’t legible to your agents, they’ll corrupt it globally with locally reasonable changes. Reviewing the code more intensely is less effective than designing code as a surface agents can navigate without hallucinating.

**4. Removing friction removes HITL (human in the loop).** This was the drumbeat under every other talk. Tan-style thin harnesses, Pi-style skinny agents, skills instead of MCP tool sprawl. Friction keeps getting engineered out of the loop in places where friction *was* the loop.

The underrated skill of 2026, according to multiple speakers: **learning to say no.**

“Fewer features but the ones that matter.”—Mario Zechner

It’s like we’ve all been given credit cards, so we’ve been making all the feature purchases we couldn’t afford to make in years past. But technical debt accrues interest.

## Paying down technical debt at the speed of inference

Beyond developing taste, saying no to more, and keeping humans in the loop, we can use AI and testing to pay down technical debt at the same speed as we are generating.

“If a task is solvable and it’s easy to verify, then it’s going to get solved by AI.”—Jacob Lauritzen,[Legora](https://legora.com/), paraphrasing verifier’s law

Lauritzen’s point: the work that gets delegated to agents is whatever we can make cheaply verifiable. Everything else stays on humans. Which makes the boundary between “ships itself” and “needs human judgment” an engineering choice about how you scaffold verification, not a fixed property of the task.

**Lawrence Jones** at [incident.io](https://incident.io/) went further: use AI to understand the AI. Dump traces to a filesystem. Point a coding agent at it with a runbook. Have it cluster failures, identify which prompt in a 50-agent hierarchy actually broke, and propose a fix against the eval suite. Red-green TDD (test-driven development), but for probabilistic systems.

“Evals are AI unit tests.”—Lawrence Jones,[incident.io](http://incident.io)

**Sarah Chieng** made the companion point from the speed side. If “code is free,” verification has to become free, too:

“At 1,200 tokens per second, validation is basically free. There is no excuse to not be doing test suites, linting, pre-commit hooks, diff reviews, browser-based QA automations.”—Sarah Chieng, Cerebras

Without evals, the rest of the 2026 agent stack (thin harnesses, fat skills, MCP, on-device SLMs, long-running missions) is a faster way to ship worse software. **With evals, it’s an architecture where models improve, codebases stay legible, and production stays honest:**

- **Capability evals:**The hill your agent is climbing. How you build something new and measure whether it’s actually getting better, not just different.
- **Regression evals:**The floor it can’t fall below. How you protect what already works while everything else changes around it.
- **Trace-level observability:**How you actually- *see*which prompt, in which sub-agent, at which step, shipped the bug. Without this, the fastest feedback loop in the world is pointed at the wrong target.

![](https://arize.com/wp-content/uploads/2026/04/PXL_20260408_143038316-scaled.jpg)

## Notes from Expo Hall

Back at the Arize booth at QEII Centre, the conversation wasn’t theoretical.

Practitioner after practitioner came up with the same concerns: *“We don’t test. Where should we start?”*

Agents in production. Vibes as the verification strategy. A nervous, knowing laugh from the whole room during my own talk when I asked, *“Have you ever shipped something that broke your company’s agentic flows?”*

The answer? Yes, we have. All of us.

We can start to pay down our technical debt with traces, then evals, then a tight feedback loop between them.

**Quality is new bottleneck.** The speed is already here. The code is already free. The only question left is whether you know what your agents are actually shipping. And that’s the loop [Phoenix](https://phoenix.arize.com/) and [Arize AX](https://arize.com/ax) were built for.
