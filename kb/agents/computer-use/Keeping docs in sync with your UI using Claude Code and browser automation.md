---
title: Keeping docs in sync with your UI using Claude Code and browser automation
kind: blog
topic: agents
subtopic: computer-use
secondary_topics: []
summary: Workflow where Claude Code drives Vercel's agent-browser (headless Chromium)
  as a skill to navigate the Logfire UI, capture step-by-step screenshots, and rewrite
  Markdown docs to match the current UI, keeping how-to guides from drifting after
  UI refactors.
triage: null
skip_reason: null
source: pydantic
url: https://pydantic.dev/articles/automating-logfire-docs
author: Daniel Cruz
published: '2026-02-20'
fetched: '2026-07-16T22:04:19Z'
classifier: claude
taxonomy_rev: 2
words: 619
content_sha256: 7e29bf236ab08346aa86fe92d971a6a3ee3e59d4ba25132c4796f8aa5b15cd70
---

# Keeping docs in sync with your UI using Claude Code and browser automation

Teams using LLMs to write code are shipping faster than ever. A side effect: documentation falls behind. When your UI changes frequently, entire workflows can shift. Buttons get renamed, steps get reordered, new fields appear, and users end up following guides that no longer match what they see.

We have some significant UI refactors coming to [Logfire](https://pydantic.dev/logfire). To avoid our docs falling behind, we built a workflow where Claude Code drives a headless browser to navigate the UI, capture screenshots, and update the documentation, all in one terminal session.

![Logfire old UI vs new UI](https://pydantic.dev/assets/blog/docs-screenshots-agent-browser/you-but-stronger-meme.jpg)



Logfire's documentation lives in [a public GitHub repo](https://github.com/pydantic/logfire) as Markdown files built with MkDocs. Many of our how-to guides describe UI workflows: "click Settings, then Write Tokens, then New write token." These guides are accurate when they're written. They start drifting as soon as the next UI change lands.


We use Vercel's [ agent-browser](https://agent-browser.dev/), a headless Chromium browser designed for AI agents. We installed it and 

[set it up as a Claude Code skill](https://agent-browser.dev/installation), which lets Claude drive the browser from the same terminal session where it edits files.

We tested it on our [Write Tokens guide](https://github.com/pydantic/logfire/pull/1722). We asked Claude to add screenshots to the page, and it handled the rest:

- Opened our local Logfire instance in the headless browser
- Navigated to Settings, clicked through to Write Tokens, and created a token
- Captured a screenshot at each step
- Read the existing Markdown and inserted the images at the right places
- Updated the step descriptions to match the current UI

All of this happened in one session. Claude could see both the live UI and the docs source, so it knew where to put things and how to name them. Because it's multimodal, it could also read the screenshots it captured and verify they looked correct before adding them to the page.

What surprised us is how natural the interaction felt. We didn't script a sequence of browser commands. We said "add screenshots to this docs page" and Claude figured out the navigation, decided which steps needed a screenshot, and matched the image conventions already used in the repo.


After doing this once, we used the [skill-creator](https://github.com/anthropics/skills/blob/main/skills/skill-creator/SKILL.md) to turn the workflow into a reusable [skill](https://docs.anthropic.com/en/docs/claude-code/skills) called `docs-updater`. The skill captures the conventions specific to our docs repo so Claude doesn't have to rediscover them each time.

Our docs repo is separate from our platform monorepo. With the skill in place, someone building a feature in the platform repo can update the docs in the same session without switching projects or remembering the docs repo conventions.

You can do the same thing for your own setup. The skill-creator walks you through capturing a workflow and turning it into a skill tailored to your repo structure, image conventions, and deployment setup.

![Wait, it's all skills? Always has been](https://pydantic.dev/assets/blog/docs-screenshots-agent-browser/always-has-been-meme.jpg)


We plan to use this as our UI refactors roll out, updating the docs alongside the code changes rather than after the fact.


- Install `agent-browser`[set it up as a skill](https://agent-browser.dev/installation)for your AI coding assistant
- Point it at your app and ask it to capture screenshots for a docs page
- Review the generated Markdown and images, then commit

Check out the [agent-browser docs](https://agent-browser.dev/) for the full list of commands and options.

One thing to be careful about: if you're automating screenshots, make sure your environment doesn't contain personally identifiable information. We use a local dev instance with synthetic data for this reason. If you're capturing from staging or any environment with real user data, have a plan for redacting PII before those screenshots end up in your docs repo.

**Want full trace visibility into your AI automations?** [Get started with Pydantic Logfire](https://pydantic.dev/logfire).
