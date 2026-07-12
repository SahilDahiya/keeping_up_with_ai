---
title: Using Agent Skills to Automatically Improve your Prompts
topic: prompt-engineering
subtopic: techniques
secondary_topics:
- agents/tool-use
- evals-observability/evaluation
summary: Shows how agent skills can automatically improve prompts, using evaluation
  feedback and reusable agent workflows to iterate on prompt quality.
source: langfuse
url: https://langfuse.com/blog/2026-02-16-prompt-improvement-claude-skills
author: null
published: '2026-02-16'
fetched: '2026-07-11T04:36:08Z'
classifier: codex
taxonomy_rev: 1
words: 1419
content_sha256: a03f8f92c2d41e2a6e56b42fcac287542b2fc2098e64bcc9e1c31129882a3487
---

# Using Agent Skills to Automatically Improve your Prompts

# Using Agent Skills to Automatically Improve your Prompts

Use the Langfuse skill to analyze trace feedback and iteratively improve your prompts.

![Picture Lotte Verheyden](https://langfuse.com/_next/image?url=%2Fimages%2Fpeople%2Flotteverheyden.jpg&w=96&q=75) Lotte

Lotte![Picture Felix Krauth](https://langfuse.com/_next/image?url=%2Fimages%2Fpeople%2Ffelixkrauth.jpg&w=96&q=75) Felix

FelixDid you know you can use an AI agent and the [Langfuse skill](https://github.com/langfuse/skills/tree/main/skills/langfuse) to iteratively improve your prompts? You annotate a handful of traces in Langfuse, then let the agent fetch your feedback, analyze the patterns, and propose prompt changes. It's a fast way to get from a rough first prompt to something more robust. It will get you from 10% to 70% before you invest in more structured evaluation like datasets and automated scoring.

We'll walk through the full loop using an example: a chatbot that searches past GitHub discussions in the Langfuse repository. We'll use Claude with the Langfuse skill as the AI agent.

[Prerequisites](https://langfuse.com#prerequisites)

**An LLM application with Langfuse tracing set up**. If your application is not instrumented yet, you can take a look at the [tracing get started page](https://langfuse.com/docs/observability/get-started) to set it up.

**An AI agent with the Langfuse skill installed**. You can use any AI agent, we'll use Claude with the [Langfuse skill](https://github.com/langfuse/skills/tree/main/skills/langfuse) in this guide (which uses the [Langfuse CLI](https://github.com/langfuse/langfuse-cli) under the hood).

**Your prompt managed in Langfuse Prompt Management (optional)**. This lets the agent fetch and update your prompt directly, and links prompts to traces automatically. See the [Prompt Management setup guide](https://langfuse.com/docs/prompt-management/get-started) and [linking prompts to traces](https://langfuse.com/docs/prompt-management/features/link-to-traces).

[Context on the Workflow](https://langfuse.com#context-on-the-workflow)

Before diving into the walkthrough, here's a quick overview of the workflow and the example application we'll be using.

[The Concept](https://langfuse.com#the-concept)

The workflow is a loop with three steps: you look at traces, annotate the ones that are off, and then hand your annotations to an AI agent that analyzes them and updates the prompt. Then you run the app again and repeat until the obvious issues are gone.

![Workflow diagram: You review traces and annotate failures, the agent fetches scores and analyzes gaps in the prompt, then updates prompts in Langfuse](https://langfuse.com/images/docs/guides/prompt-improvement-workflow-diagram.png)

[The Example Application](https://langfuse.com#the-example-application)

We're using a chatbot that searches GitHub discussions in the [Langfuse repository](https://github.com/langfuse/langfuse/discussions) to help users find whether their bug or feature request has already been in the past.

![Terminal output of the GitHub issue search chatbot](https://langfuse.com/images/docs/guides/prompt-improvement-terminal-example.png)

It fetches its system prompt from Langfuse, searches Github multiple times with different queries, evaluates the results and responds with the issues that are relevant. Every interaction produces a trace in Langfuse. You can find the full example repository [here](https://github.com/langfuse/langfuse-examples/tree/main/applications/github-issue-search).

## Example application code snippet

```
from langfuse import Langfuse, get_client, observe
from langfuse.openai import OpenAI
# using the @observe decorator to trace the function
@observe(name="github-issue-search-bot", capture_input=False)
def handle_turn(client: OpenAI, console: Console, messages: list):
    # Take the user's message as the trace input instead of the function's input parameters
    get_client().update_current_trace(input=messages[-1]["content"])
    while True:
        # This call is automatically traced by the Langfuse OpenAI wrapper
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=messages,
            tools=TOOLS, # tools are defined earlier in the code
        )
        choice = response.choices[0].message
        messages.append(choice)
        if not choice.tool_calls:
            break
        tool_results = handle_tool_calls(console, choice.tool_calls)
        messages.extend(tool_results)
    return choice.content
def main():
    langfuse = Langfuse()
    # Fetch the prompt from Langfuse
    prompt = langfuse.get_prompt("github-issue-search", label="production")
    system_prompt = prompt.compile()
    messages = [{"role": "system", "content": system_prompt}]
    # ... conversation loop
```
[Let's Dive In](https://langfuse.com#lets-dive-in)

Before you start, you need to have some traces to work with. If your application isn't live yet, you can manually enter a few inputs to start with. In my case, I ran the chatbot with about 10 different inputs to cover a range of cases: feature requests, bug reports, off-topic questions, and some that were intentionally vague.

[1. Go Through your Traces and Annotate](https://langfuse.com#1-go-through-your-traces-and-annotate)

Looking at the traces, there are likely a few things you notice right away. Some are clear mistakes, in other cases you only realize you want a different behavior while reading the trace. You'll have many scattered feedback points, which you want to write down somewhere so you have a log of things to tackle.

You can do this in Langfuse with **scores and comments**. I like to create a few [score configs](https://langfuse.com/faq/all/manage-score-configs) for the broad categories of mistakes I see. In my specific case, after looking through about 10 traces, three categories emerged that I created score configs for:

- `response-not-relevant`
- `outside-response-scope`
- `bad-search-results`

You need to create score configs in order to manually annotate your traces with these scores. See

[manual scores via UI](https://langfuse.com/docs/evaluation/evaluation-methods/scores-via-ui)and[how to create and manage score configs](https://langfuse.com/faq/all/manage-score-configs)for details.

![Annotating a trace with a score and comment in Langfuse](https://langfuse.com/images/docs/guides/prompt-improvement-score-annotation.png)

Every time you notice something, annotate the trace with the relevant score and add your specific feedback as a comment. The score gives Claude the category, the comment gives it the reason why, which is what you want Claude to address later on.

You don't need to score every trace. Just the ones where something is clearly off. I scored 8 out of roughly 10.

[2. Analyze with Claude](https://langfuse.com#2-analyze-with-claude)

After some time, you'll have a good collection of feedback to work with. Where in the past you might have manually started working through these points, you can now ask Claude to do a lot of the heavy lifting.

**I asked it to fetch my scores:**

```
Retrieve all scores that were created today. For each score, include the score
name, any comments left on the score, and the full content of the linked trace.
```
Claude pulls in everything via the Langfuse CLI and comes back with a structured summary:

![Claude's summary of all 8 annotation scores grouped by category: response-not-relevant, outside-response-scope, and bad-search-results](https://langfuse.com/images/docs/guides/prompt-improvement-scores-summary.png)

**Now ask Claude to look at the prompt itself:**

```
Fetch the prompt linked to these traces. What gaps in this prompt could be
causing these issues?
```
Because our prompt is linked to the traces, Claude can fetch the correct version and analyze it. In this case it mapped each annotated issue back to six specific gaps. See the three first ones below:

![Claude's analysis of prompt gaps: no scope guardrail, no guidance on tool failure, no instruction to interpret results critically](https://langfuse.com/images/docs/guides/prompt-improvement-gap-analysis.png)

This kind of analysis across multiple traces would take a while to do by hand.

[3. Improve the prompt](https://langfuse.com#3-improve-the-prompt)

You can iterate on the issues Claude identified if you don't completely agree with them. Once you're happy with it, you can go into improving the prompt.

```
Propose updates to this prompt that addresses the issues above. Keep it concise;
group related issues into single instructions where possible.
```
Claude will propose a revised prompt. Once you agree with all changes, you can update the prompt. You can ask Claude to update the prompt in Langfuse for you.

`Update the prompt in Langfuse.`![Claude confirms the updated prompt is live as version 2 of github-issue-search with production and latest labels applied](https://langfuse.com/images/docs/guides/prompt-improvement-claude-response.png)

Here's what the diff looks like in Langfuse:

![Prompt diff in Langfuse showing changes from version 1 to version 2](https://langfuse.com/images/docs/guides/prompt-improvement-prompt-diff.png)

[4. Keep iterating](https://langfuse.com#4-keep-iterating)

You can keep doing iterations of this loop until you don't see any obvious issues. In my case, I did about 3 iterations, after which I was consistently getting good results on my small set of traces.

[Variations](https://langfuse.com#variations)

In this guide we manually annotated traces, but the same approach works with different sources of feedback:

- **User feedback from production**: If your app collects- [user feedback (thumbs up/down, ratings, comments)](https://langfuse.com/docs/observability/features/user-feedback), you can fetch those via the CLI and use them in the same way. Be selective though: not all user feedback is actionable, so you may want to filter for feedback you actually agree with before handing it to the agent.
- **Annotation queues**: If your team reviews traces through- [Langfuse annotation queues](https://langfuse.com/docs/evaluation/evaluation-methods/annotation-queues), you can fetch scores from a specific queue to work with a curated set of annotations.
- **Experiment results**: After running an- [experiment](https://langfuse.com/docs/evaluation/experiments), you can fetch the scores and comments from that run.

[What's next](https://langfuse.com#whats-next)

At some point, it will make sense to do more structured evaluation, to make sure your prompt changes are not causing any regressions on earlier cases.

One natural next step is to [build a dataset](https://langfuse.com/docs/evaluation/experiments/datasets) out of the traces you annotated, so you can rerun your new prompts against this fixed set of cases. You can do this using the AI agent skill too, or you can use the Langfuse UI to create a dataset. Later, you can then:

- **Run experiments**: Use- [Langfuse experiments](https://langfuse.com/docs/evaluation/experiments)to compare prompt versions on your dataset, measuring accuracy, cost, and latency side by side.
- **Automate scoring**: Set up- [LLM-as-judge evaluators](https://langfuse.com/docs/evaluation/evaluation-methods/llm-as-a-judge)for your score categories, so you don't have to review every trace yourself.
