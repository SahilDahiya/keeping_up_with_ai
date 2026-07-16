---
title: Human annotations for agent runs in Pydantic Logfire
kind: blog
topic: evals-observability
subtopic: evaluation
secondary_topics:
- agents/planning
summary: Human-in-the-loop annotation of agent runs in Logfire to catch cases automated
  LLM judges miss—an agent that is fluent, polite, and wrong—by letting domain experts
  label traces the judge scored as good.
triage: null
skip_reason: null
source: pydantic
url: https://pydantic.dev/articles/logfire-annotations
author: Bill Easton
published: '2026-07-16'
fetched: '2026-07-16T23:01:17Z'
classifier: claude
taxonomy_rev: 2
words: 657
content_sha256: fbc38a4de4dd75ad3baf8c78d29ee759678d25aeacd58530076c59a17dff97d7
---

# Human annotations for agent runs in Pydantic Logfire

The refund agent said yes. The customer didn't qualify. Nothing errored, and your automated judge scored the run "helpful and polite," because it was, fluent and courteous and wrong. The only person who can tell you it was wrong is the support lead who knows the policy. Until now, the way she told you was a Slack message that scrolled away by lunch.

Annotations let her tell the system instead, on the run, in three keystrokes. We don't believe you should have to pay for rigor in your Agent development process and so we have priced annotations at $0.00/1000 scores.

![Annotate panel on an agent run with verdict, comment, and tags](https://pydantic.dev/assets/blog/agents-week/annotate-panel.png)



On any agent run, a reviewer can record a structured verdict:

- **A three-tier verdict:**pass, neutral, or fail. Three tiers calibrate more consistently across reviewers than a binary thumb, where one person's "fine" is another's "no."
- **A category:**the failure mode, hallucination, wrong tool, refused, off-topic, format error, too slow, so failures group instead of scattering.
- **An expected output:**the corrected answer, what the agent should have said. This is the field that turns a bad run into a training example.
- **A comment and tags**, for the context a category can't hold.

The review surface is built for volume, not for one-offs. A keyboard-driven panel sits next to the run: `1`, `2`, `3` to set the verdict, `⌘↵` to save and jump to the next run. You can grade fifty runs in the time a review meeting takes to schedule. Multiple reviewers can annotate the same run, so you can see where humans disagree, and the whole project's annotations live on their own page with a running "42 of 200 annotated" count.

Two things make this more than a comment box. Annotations are not stored as trace attributes, so they **outlive the trace**: when the run itself ages out of retention, the judgment about it doesn't. And you can **export** them to JSONL or CSV, and feed them straight back into your evals.


We shipped [online evals](https://pydantic.dev/articles/online-evals-pydantic-logfire) so an automated judge could score every production run. Automated judges scale, and they miss things, precisely the things that matter most: the answer that is confidently, specifically, domain-wrong in a way only someone who knows your business can see. Annotations are the other half of that pair. Evals give you coverage; annotations give you ground truth.

This is the difference the whole week turns on. An eval tells you the agent did what you specified. A human is the first to tell you when what you specified was wrong: when the refund was processed flawlessly and should never have been approved at all. Correct and wrong are not the same axis, and only someone who knows the business can pull them apart. An annotation is your earliest read on whether the working agent you built is the right one.

And they give it to you in a shape you can use twice. Every fail with an expected output is a case for your offline eval set: here is an input, here is what the agent should have said. Every time a human disagrees with the automated judge, you've found a bug in the judge, not the agent, and that improves your evals. Point your reviewers at production for an afternoon and you leave with a dataset built from real failures on real inputs, not the synthetic cases you'd have guessed at instead.

That is the pattern under the whole week: observe the run, let a human judge it, turn the judgment into data, measure the next version against it. The verdicts anchor to the trace that produced them, so a fail is one click from the prompt, the tools, and the response, and because they persist past retention, your library of hard cases only grows.

Not using Logfire yet? [Get started](https://pydantic.dev/logfire). The free tier includes 10 million spans a month, our AI gateway, and so much more.
