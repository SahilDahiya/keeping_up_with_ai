---
title: Fable's judgement
topic: agents
subtopic: multi-agent
secondary_topics:
- infra-platform/cost
summary: Practical coding-agent pattern for delegating implementation work to cheaper
  subagents while reserving the main model for judgment, review, synthesis, and model-selection
  decisions.
source: simon-willison
url: https://simonwillison.net/2026/Jul/3/judgement/
author: Simon Willison
published: '2026-07-03'
fetched: '2026-07-11T05:25:04Z'
classifier: codex
taxonomy_rev: 1
words: 368
content_sha256: 47160975e6431a690448541fa91b253ebc359907156be7ebf0771aa4634e71b1
---

# Fable's judgement

3rd July 2026

One of the most interesting tips I got from [the Fireside Chat](https://www.ai.engineer/worldsfair/schedule?session=asn_slot_2026_06_30_main_stage_1230_2026_06_08t09_35_43_039z) I hosted with Cat Wu and Thariq Shihipar from the Claude Code team at AIE on Wednesday was to let Fable (and to a certain extent Opus) use their own judgement rather than dictating how they should work.

The example they gave was testing. You can tell Fable "only use automated testing for larger features, don't update and run tests for small copy or design changes" - but it's better to just tell Fable to use its own judgement when deciding to write tests instead.

Jesse Vincent just gave me a related tip to help avoid burning too many of those valuable Fable tokens in the few days we have left before the prices go up. Tell Fable to use other models for smaller tasks, applying its own judgement about which model to use.

I prompted Claude Code just now with:


`For all coding tasks use your judgement to decide an appropriate lower power model and run that in a subagent`

Claude saved this memory file in `~/.claude/projects/name-of-project/memory/delegate-coding-to-subagents.md`:

`--- name: delegate-coding-to-subagents description: Simon wants coding tasks delegated to subagents running an appropriately lower-power model metadata: node_type: memory type: feedback originSessionId: 30068d78-43a9-4fb1-bb29-9799e18c526a ---`Stated by Simon on 2026-07-03: "For all coding tasks use your judgement to decide an appropriate lower power model and run that in a subagent."


Why:cost/efficiency — implementation work rarely needs the top-tier model; judgment, review, and synthesis stay with the main loop.

How to apply:when a task in this project is primarily writing/editing code, spawn an Agent with a model override (sonnet for substantive implementation, haiku for trivial/mechanical edits) and a self-contained prompt; review the result in the main loop before committing. Design, auditing, data synthesis, and anything judgment-heavy stays in the main model. See also [[project-goals]].

So far it seems to be working well. I'm getting a *ton* of work done and my Fable allowance is shrinking less quickly than before.

## Recent articles

- [The new GPT-5.6 family: Luna, Terra, Sol](https://simonwillison.net/2026/Jul/9/gpt-5-6/)- 9th July 2026
- [sqlite-utils 4.0, now with database schema migrations](https://simonwillison.net/2026/Jul/7/sqlite-utils-4/)- 7th July 2026
- [sqlite-utils 4.0rc2, mostly written by Claude Fable (for about $149.25)](https://simonwillison.net/2026/Jul/5/sqlite-utils-fable/)- 5th July 2026
