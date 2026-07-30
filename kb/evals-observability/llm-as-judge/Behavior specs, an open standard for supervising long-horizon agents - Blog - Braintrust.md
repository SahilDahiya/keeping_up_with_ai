---
title: Behavior specs, an open standard for supervising long-horizon agents - Blog
  - Braintrust
kind: blog
topic: evals-observability
subtopic: llm-as-judge
secondary_topics:
- agents/planning
summary: Braintrust and Basis (an AI tax-return agent builder) introduce behavior
  specs, an open standard (agentbehavior.dev) for judging long-horizon agent trajectories
  on individual expected behaviors (true/false/NA) rather than only outcomes, citing
  OpenAI's 2023 and DeepMind's process-reward-model research as precedent for process
  over outcome supervision.
triage: null
skip_reason: null
source: braintrust
url: https://www.braintrust.dev/blog/behavior-specs
author: Braintrust Team
published: '2026-07-29'
fetched: '2026-07-30T06:52:15Z'
classifier: claude
taxonomy_rev: 2
words: 1617
content_sha256: 076234431c070e0c32f706755e055a8a377b5e74208ec95676a93e13869efa2a
---

# Behavior specs, an open standard for supervising long-horizon agents - Blog - Braintrust

29 July 2026Ankur Goyal, Mitchell Troyanovsky9 min

A modern agent can work for hours. [Basis](https://www.getbasis.ai/) builds AI agents for accountants. One of them completes a full tax return on its own, running research, building workbooks, and deciding when and how to make judgments. Over a single trajectory it makes hundreds of decisions, and you cannot reduce that behavior to one outcome metric. Outcome evals matter, but on long trajectories they are expensive to run, and the outcome is rarely easy to verify.

To build long-horizon agents you can trust, you have to supervise the process, not only the result. Braintrust and Basis are releasing **behavior specs**, an open standard for defining and evaluating how an agent should behave across a trajectory. Everything is open source at [agentbehavior.dev](https://agentbehavior.dev) so you can start writing and judging behavior specs on your own traces with Braintrust today.

Basis started where most teams start, with outcome evals that scored whether the agent produced an accurate return. Those evals are necessary, but in a domain like tax, a correct return does not tell you whether the agent reached it the right way. Consider a Form 1040 that includes a Schedule K-1 with difficult-to-extract footnotes. The agent may need to determine whether the taxpayer materially participated in an activity and whether that activity should be treated as passive or active. Even if an outcome-only eval scores the final return as correct, it cannot reveal whether the agent used the proper OCR method or properly grounded its thinking in primary sources to verify the outcome.

Each score requires the agent to run the full trajectory, making runs expensive and iteration slow, especially when success is difficult to define and verify. Because the eval set reflects only a fraction of the scenarios an agent encounters in production, a high score can reflect overfitting. A pass or fail also does not reveal which of the hundreds of decisions went wrong.

Instead of judging only the final answer, Basis defines the process it expects and evaluates each step across the trajectory. The limits of outcome evals pushed Basis to formalize intended behaviors as specs.

In human organizations, we set process standards because we trust them to produce better outcomes. An accountant is expected to complete a proper month-end close before finalizing the books. An engineer is expected to write a scoping doc before a major refactor.

ML research on process supervision supports the same premise, that improving the process improves the result. [OpenAI showed in 2023](https://arxiv.org/abs/2305.20050) that when training models to solve math problems, process reward models (PRMs) outperformed and generalized better than outcome reward models (ORMs). [Uesato et al.](https://arxiv.org/abs/2211.14275) reached a similar conclusion at DeepMind a year earlier.

Public research on process supervision slowed after that, as reinforcement learning from verifiable rewards (RLVR) scaled up for reasoning tasks. RLVR works best when a task has an objectively verifiable answer, such as a correct answer to a math problem or a passing software test. As agents take on more long-horizon work, process supervision becomes more important for accurate outcomes.

![The unit of process supervision, 2023 to today: a short five-step 2023 math solution with dense human step labels, next to a one-hour agent trajectory of model turns and tool calls, with a selected behavior judged true, false, or NA across the trace](https://www.braintrust.dev/blog/img/behavior-specs/unit-of-process-supervision.png)


A modern trajectory uses four to five orders of magnitude more compute than a 2023 math problem. Even when the raw reasoning trace is hidden, the tool calls and summarized reasoning carry more than enough evidence to judge whether the agent followed the process. For an agent, process is a set of expected behaviors in specific situations. Behavior specs make those expectations explicit. They capture a team's point of view on how the agent should operate. Here's an example:

markdown

```
---
name: validate-rendered-deck
description: Render the current PowerPoint before delivery, inspect it for visual issues, and revalidate after fixes.
---
## Validate the rendered deck before returning it
**Intent:** Ensure the deck the user receives is visually usable, not merely
valid as PowerPoint code.
**Evidence:** Before returning a created or edited PowerPoint, the agent
should use the current saved version of the deck and its rendered slide
images. A render made before the most recent edit is not evidence about the
deck now being returned.
**Decision:** The agent should determine whether the current rendered deck
has formatting, layout, readability, or other visible presentation issues
that make it unsuitable to return.
**Execution:** The agent should render the current deck to images and inspect
those images before returning it to the user.
**Recovery:** If the inspection finds an issue the agent can fix, it should
fix the deck, render the updated version again, and inspect that new render
before returning it. If it cannot render or inspect the deck, it should not
represent the deck as visually validated.
**Failure modes:** Returning an unrendered deck; relying on a render from
before the latest edit; fixing a visual issue without re-rendering; missing a
formatting problem that code-level checks cannot reveal.
```
The spec is written in the second-person imperative so a person or a judge can read a trajectory and tell whether the behavior happened. It is not a prompt and it is never shown to the agent. A behavior spec defines the intended behavior so you can align on it and measure against it. It does not prescribe how training, runtime context, or tools produce the desired behavior.

The labels are an optional structure you can lean on when it helps:

markdown

```
# Behavior name
**Intent:** Why this behavior matters and when it applies.
**Evidence:** What the agent SHOULD inspect, retrieve, preserve, or verify before deciding.
**Decision:** What the agent SHOULD infer, choose, or become confident about.
**Execution:** What the agent SHOULD do after deciding.
**Recovery:** What the agent SHOULD do when the first path fails, evidence is incomplete, or the request is ambiguous.
**Failure modes:** What bad or unintended behavior this spec is meant to prevent.
```
Plain Markdown works too. The only hard requirements are the frontmatter and a clear description of the behavior the agent should exhibit and what it should avoid.

Not everything you want from an agent belongs in a spec. A behavior deserves a spec when it governs a recurring choice, can be evaluated from a trajectory, and matters enough to test continuously.

That continuous testing creates a tighter feedback loop. Teams can identify which behavior failed, update the agent's prompts, tools, or context, and test whether the change improves performance across many trajectories.

You already encode behaviors today, in prompts, skills, and tool descriptions. A single production agent has hundreds of them. Writing them all into one list and keeping it in sync with the runtime context is unmanageable.

The goal is to elevate the few you care about enough to measure. Writing a spec says you want a standing test against this behavior. Everything else stays where it lives today, and the file stays sparse on purpose.

A sparse file is still authoritative. When a spec and the runtime context disagree, the spec takes precedence. The team revises the implementation until the agent follows the intended behavior. The eval catches future drift. That keeps the spec honest instead of becoming another stale doc.

Related specs live together under an `.agents/behaviors/` root next to the rest of the agent's configuration:

text

```
.agents/behaviors/
└── behavior-name/
    ├── BEHAVIOR.md       # Required: metadata and behavior text
    ├── references/       # Optional: rationale, examples, background docs
    └── ...               # Optional additional files
```
A consistent layout lets trajectory judges discover specs automatically. A skill for writing good behavior specs ships alongside the standard at [agentbehavior.dev](https://agentbehavior.dev).

A behavior spec is only useful if you can judge it. Judging runs across production traffic, so the verdict has to be easy to produce and read. Each spec gets one of three grades, true, false, or NA.

| Run | Verdict | 
|---|---|
| The agent answered a question and did not create or edit a deck | NA | 
| The agent rendered the final deck to images, inspected them, and fixed a layout issue before returning it | true | 
| The agent edited the deck and returned it without rendering or inspecting the result | false | 

Each spec in a file is judged on its own. A judge prompt ships alongside the standard that you can use as-is or adapt to your agent.

Judging at that scale is a platform problem. Because you have to judge agent behavior over whole trajectories at production scale, each behavior spec becomes a standing eval. You reproduce what happened in production, evaluate it against the specs, and iterate on the runtime context until the agent behaves the way you intend.

A behavior spec is an opinion, formed from experience, about how the agent should work. Evals check whether the agent followed it, but they cannot tell you whether the opinion was good in the first place. You still decide which behaviors are worth requiring.

As models get better, this pays off in an unusual way. Teams should retire behavior specs once the model reliably exhibits the behavior without extra guidance. The remaining specs should focus less on low-level mechanics and more on the judgment you care about. Expect to remove prescription over time, not accumulate it. The behavior specs that survive become your organization's standards for good agent behavior.

This is how you build trusted long-horizon agents. The spec, the docs, example agents, the authoring skill, and the judge prompt are open at [agentbehavior.dev](https://agentbehavior.dev). [Start judging behaviors](https://www.braintrust.dev/signup) across your own traces and evals, or [book a demo](https://www.braintrust.dev/contact).

Thank you to [Mitchell Troyanovsky](https://x.com/mitch_troy) and the Basis team for the collaboration.
