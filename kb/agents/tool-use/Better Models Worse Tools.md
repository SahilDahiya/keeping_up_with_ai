---
title: 'Better Models: Worse Tools'
topic: agents
subtopic: tool-use
secondary_topics:
- evals-observability/evaluation
summary: Short analysis of newer coding models producing malformed arguments for third-party
  edit tools, raising the issue that tool schemas and edit mechanisms may need model-specific
  evaluation and adaptation.
source: simon-willison
url: https://simonwillison.net/2026/Jul/4/better-models-worse-tools/
author: Simon Willison
published: '2026-07-04'
fetched: '2026-07-11T05:24:57Z'
classifier: codex
taxonomy_rev: 1
words: 309
content_sha256: 0dd7f6baa1f6ac2d96bc8c3a1e3a5ca42f856fd0cb75a872d19702c39405e935
---

# Better Models: Worse Tools

4th July 2026 - Link Blog

** Better Models: Worse Tools**. Armin reports on a weird problem he ran into while hacking on Pi:

The short version is that newer Claude models sometimes call Pi’s edit tool with extra, invented fields in the nested

`edits[]`array. And not Haiku or some small model: Opus 4.8. The edit itself is usually correct but the arguments do not match the schema as the model invents made-up keys and Pi thus rejects the tool call and asks to try again.That alone is not too surprising as models emit malformed tool calls sometimes. Particularly small ones. What surprised me is that this is getting worse with newer Anthropic models as both Opus 4.8 and Sonnet 5 show it but none of the older models. In other words, the SOTA models of the family are worse at this specific tool schema than their older siblings.


Armin theorizes that this is because more recent Anthropic models have been specifically trained (presumably via Reinforcement Learning) to better use the edit tools that are baked into Claude Code. This has the unfortunate effect that other coding harnesses, such as Pi, may find that their own custom edit tools are more likely to be used incorrectly.

Claude's edit tool [uses search and replace](https://platform.claude.com/docs/en/agents-and-tools/tool-use/text-editor-tool#str-replace). OpenAI's Codex [uses an apply_patch mechanism instead](https://developers.openai.com/api/docs/guides/tools-apply-patch), and OpenAI have talked in the past about how their models are trained to use that tool effectively.

Does this mean third-party coding harnesses like Pi should implement multiple edit tools just so they can use the one with the best performance for the underlying model the user has selected?

## Recent articles

- [The new GPT-5.6 family: Luna, Terra, Sol](https://simonwillison.net/2026/Jul/9/gpt-5-6/)- 9th July 2026
- [sqlite-utils 4.0, now with database schema migrations](https://simonwillison.net/2026/Jul/7/sqlite-utils-4/)- 7th July 2026
- [sqlite-utils 4.0rc2, mostly written by Claude Fable (for about $149.25)](https://simonwillison.net/2026/Jul/5/sqlite-utils-fable/)- 5th July 2026
