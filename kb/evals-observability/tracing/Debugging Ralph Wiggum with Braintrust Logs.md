---
title: Debugging Ralph Wiggum with Braintrust Logs
topic: evals-observability
subtopic: tracing
secondary_topics:
- evals-observability/monitoring
summary: Debugging walkthrough using Braintrust logs to inspect AI application behavior,
  identify failure causes, and close the loop with improvements.
source: braintrust
url: https://www.braintrust.dev/blog/ralph-wiggum-debugging
author: Braintrust Team
published: '2026-01-13'
fetched: '2026-07-11T04:33:27Z'
classifier: codex
taxonomy_rev: 1
words: 1104
content_sha256: 8d7851c9f7c99e4368d990b249534ed5587ab4d7d27173a65b93774bdc24370d
---

# Debugging Ralph Wiggum with Braintrust Logs

13 January 2026Jess Wang7 min

Ralph Wiggum is a development methodology named after the persistently optimistic [Simpsons character](https://en.wikipedia.org/wiki/Ralph_Wiggum). It embraces iteration over perfection through a simple autonomous loop:

- **Feed stories**: A PRD file (- `prd.json`
- **Execute**: An AI agent uses a prompt template (- `prompt.md`
- **Learn from failure**: On every failed iteration, the agent writes learnings to a progress log (- `progress.txt`
- **Retry with context**: A bash script (- `ralph.sh`
- **Eventually succeed**: Like Ralph trying to eat paste, the Agent eventually figures it out. It might take 100 attempts, but it gets there

The key: **the agent keeps going even if you fall asleep or walk away**. If you specify 25 iterations, it'll run up to 25 complete loops through user stories.

To test the methodology, I built a simple habit tracker called [everyday calendar](https://everyday-calendar-six.vercel.app/), inspired by Simone Giertz's [everyday calendar product](https://yetch.studio/products/every-day-goal-calendar?srsltid=AfmBOorQmR7NSEpsuycCy3vSPpzkdu7MwK4x1wj9LD64W1qB9RbL_Bst). In the calendar view, you can check off each day based on whether you completed a task, like posting content daily, walking 20,000 steps, or any other habit you want to track. The app required several improvements, like fixing the sidebar UI, adding better calendar naming, improving color accessibility, and managing data persistence across sessions and users. I created [10 user stories](https://gist.github.com/DaRubberDuckieee/018f33bc2ae0affaf3e28ccadcf9b4fa) for these changes and ran Ralph Wiggum in hopes of getting all these stories completed while I stepped out to run errands and work out for the day.

The fundamental philosophy of how the Ralph Wiggum method works is running the same prompt over and over, but with improved context each time. Let's try it with my everyday calendar project.

The agent successfully completed US-005 (user story #5), which is adding color contrast improvements and ARIA labels. At the end, it wrote this to `progress.txt`:

```
--- Iteration 1: US-005 ---
Successfully completed accessibility audit and color contrast improvements.
Key learnings:
- Text-shadow is an effective technique for ensuring text readability
- Color upgrade from #D4A5A5 to #E5C4C4 provided better contrast ratios (4.5:1+)
- ARIA attributes dramatically improve screen reader experience
- Git commands require approval in this environment
- No test suite or linting exists for this vanilla JS project
```
Now it moves to user story #6, which is to center the calendar on the page.

Notice how Iteration 2 sees:

- **Updated completion status**: US-005 is now marked complete
- **Accumulated learnings**: Knows git commands need approval
- **No test suite**: Won't waste time looking for tests
- **Same base instructions**: The "Ralph Wiggum" methodology text is identical

The agent in Iteration 2 behaves differently because it reads the breadcrumbs left by Iteration 1. When it tries to commit, it doesn't waste time failing on git commands. It already knows from the context that commits require manual approval.

This is the iteration mechanism: memory accumulation through persistent context files.

The problem with Ralph Wiggum is that it's designed for you to walk away. Go to sleep, grab lunch, let it run overnight. That autonomy creates a risk: what happens when something goes wrong?

Without visibility, you could burn through your API budget running the same failure loop for hours. You need observability to understand what's happening behind the scenes.

When running Ralph Wiggum on my 10 user stories, I started hitting a wall. Looking at [the trace](https://www.braintrust.dev/app/Jess%20Wang/p/Ralph%20Wiggum/trace?object_type=project_logs&object_id=bdde5e88-f178-4120-b6c8-b95f1394af7b&r=feeb75af-e5d9-4a7a-85e8-e77fa91f25a2&s=97365982-0660-45a5-bd8c-a8fe4e542609), I could see the exact moment things went wrong:

json

```
{
  "input": "I was running my ./scripts/ralph/ralph-claude.sh 25 and running into
  an issue of: despite the Ralph instructions stating I have full file editing
  permissions, the system is still requesting permission for each write operation."
}
```
Despite my prompt explicitly stating that the agent had "FULL file editing permissions," Claude Code was still asking for permission on every single write operation. This was killing the autonomous aspect of Ralph. It couldn't run unattended if it needed human approval for every file edit.

The traces revealed the core issue through a series of LLM calls:

- [First attempt](https://www.braintrust.dev/app/Jess%20Wang/p/Ralph%20Wiggum/trace?object_type=project_logs&object_id=bdde5e88-f178-4120-b6c8-b95f1394af7b&r=feeb75af-e5d9-4a7a-85e8-e77fa91f25a2&s=97365982-0660-45a5-bd8c-a8fe4e542609)
- [Knowledge retrieved](https://www.braintrust.dev/app/Jess%20Wang/p/Ralph%20Wiggum/trace?object_type=project_logs&object_id=bdde5e88-f178-4120-b6c8-b95f1394af7b&r=feeb75af-e5d9-4a7a-85e8-e77fa91f25a2&s=20846b91-09b8-4408-9a96-98d465378cf3)
- **Solution identified**: Need to create- `.claude/settings.json`with permission configuration

The key insight from the traces:

```
Claude Code has a permission mode system that controls whether you
get prompted for file editing operations.
```
Thanks to the detailed traces, I learned about Claude Code's [configuration scoping system](https://code.claude.com/docs/en/settings#configuration-scopes):

- **Managed**(highest) - System-level policies
- **Command line arguments**- Temporary overrides
- **Local**(- `.claude/settings.local.json`) - Personal project settings
- **Project**(- `.claude/settings.json`) - Shared team settings
- **User**(- `~/.claude/settings.json`) - Personal global settings (lowest)

The agent created a [project-level configuration file](https://www.braintrust.dev/app/Jess%20Wang/p/Ralph%20Wiggum/trace?object_type=project_logs&object_id=bdde5e88-f178-4120-b6c8-b95f1394af7b&r=feeb75af-e5d9-4a7a-85e8-e77fa91f25a2&s=8bf95e33-becc-47db-88ad-fa281454b34f) at `.claude/settings.json` with these settings:

json

```
{
  "permissions": {
    "defaultMode": "acceptEdits",
    "allow": [
      "Edit(*)",
      "Write(*)"
    ]
  }
}
```
This configuration:

- Set `defaultMode``"acceptEdits"`to disable permission prompts
- Explicitly allowed `Edit(*)`for making file edits
- Explicitly allowed `Write(*)`for creating/overwriting files

To understand the true cost of running Ralph Wiggum autonomously, I used Braintrust's [Loop](https://www.braintrust.dev/docs/observe/loop) feature to analyze the selected traces. I asked Loop:

Based off the traces that I have selected, can you calculate how many tokens, how many LLM calls, approximately how expensive it was to run this process?


Across my Ralph Wiggum run, Braintrust tracked:

- **274 LLM calls**to Claude Sonnet 4.5
- **3,709 prompt tokens**(input)
- **91,547 completion tokens**(output)
- **95,256 total tokens**

Using Claude Sonnet 4.5 pricing ($3/1M input tokens, $15/1M output tokens), the total cost was approximately:

text

```
Prompt cost:      3,709 / 1,000,000 × $3  = $0.01
Completion cost: 91,547 / 1,000,000 × $15 = $1.37
Total cost:                                  $1.38
```
For roughly **$1.40**, the agent autonomously worked through 2 user stories. The agent spent most tokens on reasoning about code changes and generating file edits. It spent relatively little on reading context (hence the low prompt token count compared to completion tokens).

Braintrust's per-span metrics showed me exactly where tokens were being spent. This visibility is essential for autonomous runs. You need to know if a bug is burning through your budget repeatedly attempting the same failure.

The Ralph Wiggum pattern is powerful, but autonomous systems need proper configuration. Understanding Claude Code's permission system and using project-scoped settings made the difference between stalling and running overnight.

With structured traces, I could review the exact sequence of events and learn from the agent's reasoning. The traces showed even the AI needed to learn: research the docs, understand the system, apply the fix. That's how humans debug too.

The tooling around the AI matters as much as the model itself.

Adding logging helped me understand:

- How the agent thinks
- Where it gets stuck
- What information it needs
- How to improve my prompts

If you're experimenting with Ralph Wiggum and want to add logging, [get started with Braintrust](https://www.braintrust.dev/signup).
