---
title: Why your traces and evals belong in the same place
topic: evals-observability
subtopic: tracing
secondary_topics:
- evals-observability/evaluation
summary: Argues that traces and evals should live together so teams can connect production
  behavior, offline experiments, and failure analysis.
source: braintrust
url: https://www.braintrust.dev/blog/traces-and-evals-same-place
author: Braintrust Team
published: '2026-05-11'
fetched: '2026-07-11T04:34:10Z'
classifier: codex
taxonomy_rev: 1
words: 628
content_sha256: 7c2e73e28ce77586273c42e276eb2130072c5902e62014df6d1b82edeaa30a3c
---

# Why your traces and evals belong in the same place

11 May 2026Ornella Altunyan4 min

Most AI regressions don't show up on dashboards. It's more common that the request returns valid output, latency is fine, error rates don't change, and the response your agent gave just happens to be wrong. The first sign something is off usually comes from outside the engineering stack, in a support queue or an escalation thread.

The teams who can catch these regressions fast are the ones running their evals in the same place they are logging their traces. When the two are in different tools, every regression has to make it through a long, manual journey before anything gets fixed. Each handoff in the process is a place where the work can stall.

When traces and evals are in the same place, that whole sequence collapses into a problem you can solve quickly. And with automation, it can turn into a problem you don't have to solve at all.

Finding AI failures is hard because you need complex metrics that regular observability doesn't capture, like whether the agent picked the right tool, gave a coherent answer, or hit the right tone for the conversation. Most of these types of regressions are found by someone scrolling through logs who notices a weird trace. From there, getting to a shipped fix is what takes up most of the team's time.

You find the trace in your trace viewer, export it, then move over to your eval tool to build a dataset around it, write a scoring function, run the eval, decide whether the regression is real, write a fix, re-run the eval, and deploy. Every step requires a different mental model, so there's a lot of context switching.

When everything's in one place, you can skip most of that overhead. The suspicious trace you're looking at can become a dataset entry with one click. The scorer you wrote to catch the regression is the same scorer that watches your fix in production after you ship, so you can make sure the regression doesn't come back. This type of debugging can be finished end to end in an afternoon.

Find trace in viewer

Export it

Build dataset in eval tool

Write scoring function

Run eval, confirm regression

Write fix, re-run eval

Deploy

If you're waiting for someone on your team to notice the support queue getting heavy, you're getting the slowest possible quality signal of a regression. To be alerted at the moment it happens, you can run online evals against production traffic. A continuously running scorer can route anomalies to alerts, dashboards, or tickets, depending on how your team prefers to be paged. The system doing the "noticing" is the first step to the system taking action on a fix itself.

Once the traces and the evals are in the same place, automation is the next layer. The signals are already there, since the system knows when a score dropped, which traces drove the drop, and what the dataset for that failure mode looks like.

From there, automation can take a regression and run the workflow itself. Braintrust will propose a prompt change, run the eval, and surface the result for you to review. The same setup can spot a recurring failure pattern that nobody has written a scorer for yet, and suggest one. When a score drops right after a deploy, the system can connect those two events and flag the change that broke things.

None of this works when traces and evals live in separate tools, because no single tool has the full picture. Putting them in the same place is the prerequisite for everything else. You get a faster workflow on day one, and as you start layering automation on top, more and more of that workflow can happen without you.
