---
title: Prompt optimization and managed prompts in Pydantic Logfire
kind: blog
topic: null
subtopic: null
secondary_topics: []
summary: null
triage: null
skip_reason: null
source: pydantic
url: https://pydantic.dev/articles/logfire-prompt-optimization
author: Bill Easton
published: '2026-07-17'
fetched: '2026-07-18T06:44:04Z'
classifier: null
taxonomy_rev: 2
words: 1552
content_sha256: b216677920d6f890fb9df944f4889d313112301033f61916f39a0ba0976037e0
---

# Prompt optimization and managed prompts in Pydantic Logfire

Nobody has touched the summarizer prompt in three months. It works. It also returns a subtly wrong summary on about one legal document in twenty, and no one has connected those two facts, because the failures are scattered across forty thousand runs and not one of them threw. There is no stack trace for "confidently wrong."

This is the last day of the week, and the payoff. The views found the failing runs. A human might have annotated a few. Now you finish it: find the fix, and ship it, without opening your editor.


Open the Optimize tab on the agent. The optimizer reads its recent production traces, up to a hundred conversations over the last five days, with the failures weighted highest, finds the pattern, and proposes a single edit to the prompt. Then it does the thing most "AI that improves your AI" refuses to do. It shows its work: seven traces, quoted, next to the diff.

![An agent card in the Agents view, an SRE agent with 1.5K runs and its cost, average time, and usage, and the Optimize button ready to click](https://pydantic.dev/assets/blog/agents-week/sre-optimize.png)


- **Evidence, not vibes.**Every claim in a proposal has to cite specific traces. If the model can't ground a change in a run you can open, a validator rejects it and makes it try again. You get a side-by-side diff and a "Why this proposal?" panel that deep-links into the exact runs behind it.
- **One edit, not a rewrite.**At most one error-reduction change and one quality change per run. And a confidence ladder: it only climbs from "prefer" to "always" and "never" when the evidence is both frequent and high confidence. It writes "should" when the data says should.
- **It knows what isn't a prompt problem.**When the real cause is a flaky provider, a broken tool, a quota, or the model itself, it does not cram that into the prompt. It surfaces separate "fix this elsewhere" cards, each pointing at the trace that proves it.
- **Human-gated.**Nothing changes until you accept the diff, and- **Refine proposal**lets you push back in plain English and re-run.

The reason to trust it is that it can't hide. Most prompt auto-tuners give you an opaque score and a black-box rewrite, and ask you to believe both. This one grounds every claim in a trace you can open, makes one change you can read in ten seconds, and refuses to escalate the language past what the data supports. That restraint is the feature. An optimizer that rewrites your whole system prompt on thin evidence is just a faster way to ship a regression. And the training set is your production traffic itself: the inputs your users actually sent yesterday, not a benchmark you curated once and never updated.

There is one risk every prompt edit carries: a change that fixes the failing inputs can quietly regress the ones that were already fine. That is exactly why it makes one small, evidence-cited change instead of a rewrite, and why you canary it before it reaches everyone. A single held-out score can hide that trade-off; a label move you watch on the live agent view can't.

And the output is the most portable artifact in software: a prompt. Accept the diff and put it wherever your prompt actually lives, a Python string, a YAML file, a `CLAUDE.md`, another vendor's console. The optimizer reads the `gen_ai.*` spans any OpenTelemetry framework emits, and the fix it hands back works anywhere you can paste text. Whatever you build with, the loop is: send traces, read the evidence, copy the better prompt.


Copy-paste is the whole loop, and you can stop there. But a one-sentence prompt change traveling the same path as a schema migration, waiting behind your slowest test and a full deploy, is the absurd part of the old workflow. That's what **managed prompts** remove: your prompt becomes config you control from outside the deploy, and accepting a proposal writes the new version for you.

In a [Pydantic AI](https://ai.pydantic.dev) agent it's one capability, no variable plumbing:

```
from pydantic_ai import Agent
from pydantic_ai_harness.logfire import ManagedPrompt
agent = Agent(
    'anthropic:claude-opus-4-7',
    capabilities=[
        ManagedPrompt('summarizer', default=SUMMARIZER_PROMPT, label='production'),
    ],
)
```
The agent's instructions now resolve from the managed prompt, and the `default` ships in your binary, so if [Pydantic Logfire](https://pydantic.dev/logfire) is ever unreachable the agent keeps running on it. This is not a hard dependency on the request path. Everything else is controlled from the UI, API, or MCP:

- **Versions**are immutable, numbered snapshots. Every change is a new version you can diff and roll back to, nothing is edited in place.
- **Labels**are movable pointers,- `production`,- `canary`,- `staging`. Your app resolves the label, so moving- `production`from version 7 to 8 changes what's served instantly, and rolling back is moving it to 7 again.
- **Weighted rollout**splits a label across versions,- `canary`at ten percent and- `production`at the rest, so a change earns its way to everyone.
- **Targeting**applies ordered, first-match-wins rules, so a version can go to one customer, region, or cohort first.

Every resolution records *why* it resolved the way it did as OpenTelemetry baggage on the trace, so analyzing an A/B split is SQL over your telemetry, not a second analytics product.

A managed prompt freezes the template text as an immutable version and carries its model, settings, and tool definitions alongside, so promoting a version ships the whole configuration together, not a prompt that's out of step with the tools it assumes. Test a version in the playground, with those tools, before you move a label toward it.


This is where the week stops observing and starts changing things. Every team eventually builds a worse version of the optimizer by hand, someone exports a few hundred traces, reads until a pattern emerges, edits the prompt, and ships on faith. The reading is the expensive part, and the part you skip when you're busy. A one-in-twenty failure does not reveal itself in the ten runs you have time to skim. The optimizer does that reading at the scale where the pattern lives, and hands you the edit and the evidence. Judgment stays where it belongs: with you, approving the change.

And managed prompts make the shipping match the change. Prompts and model settings are the highest-churn, highest-risk part of an agent, and teams route around the deploy pipeline the wrong way, editing prompts in the database or keeping a Google Doc of "current" ones, so the thing most likely to change has the least version control. Managed prompts make a prompt what it is: configuration. Versioned so you can see what changed, labeled so shipping and rolling back are one gesture, rolled out by weight, targeted to a cohort, and observable, because the version that served each run is on the run's trace next to its cost and outcome. Feature flags for the part of an agent that isn't code, borrowing the two ideas that already work for software: immutable versions, like a Docker tag, and movable labels, like a git branch.

Point the optimizer at an agent that uses a managed prompt and improving and shipping become one motion. Propose, review, accept, canary, move a label. That's the loop the whole week has been building toward, closed in one screen. And it's the same motion on every agent you run, which is the only way this works at scale: you don't hand-tune a thousand pets, you point the optimizer at the one that's drifting, read the evidence, and move a label. The herd stays legible, and every improvement is still yours to approve, one trace-backed edit at a time.

One more thing is visible from here. A prompt is one key of an agent's configuration; the model, the settings, and the tool definitions are the others, and they want the same treatment. That's where this goes, and soon: **the whole agent's configuration, managed the way the prompt is**, instructions, model, settings, and tools behind one managed value, with the same versions and labels, and any key you don't manage falling back to what's in your code, so the code-defined agent stays the always-safe fallback. Your code still runs the agent; Logfire manages what it runs with. It even starts from the traces: Logfire has watched enough of your agent's runs to draft its config as the first version. The deploy becomes the safety net instead of the bottleneck, and the optimizer gets a bigger canvas: the whole agent, prompt and all.


Open an agent in Logfire and click **Optimize**. That's the setup. It reads the traces you already send, whatever framework produced them.

Back to the summarizer. The proposal was one clause: on contracts, cite the clause number for every claim, justified by seven runs where the model asserted a term the contract didn't contain, each a click away. Accept the diff and paste the clause into your prompt, or, since this one is a managed prompt, let it become version 8: move `canary` to it, watch the agent view for five minutes, see the error rate hold, and move `production`. The change that used to cost forty minutes and a rollback plan cost one label move, and undoing it is one more.

Not using Logfire yet? [Get started](https://pydantic.dev/logfire). The free tier includes 10 million spans a month, our Pydantic AI gateway, and more.
