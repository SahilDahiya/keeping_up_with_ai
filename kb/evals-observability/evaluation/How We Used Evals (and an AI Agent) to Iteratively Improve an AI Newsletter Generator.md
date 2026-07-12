---
title: How We Used Evals (and an AI Agent) to Iteratively Improve an AI Newsletter
  Generator
topic: evals-observability
subtopic: evaluation
secondary_topics:
- agents/planning
summary: Case study on using evals plus an agentic workflow to iteratively improve
  a newsletter-generation system.
source: arize
url: https://arize.com/blog/how-we-used-evals-and-an-ai-agent-to-iteratively-improve-an-ai-newsletter-generator/
author: Laurie Voss
published: '2026-03-10'
fetched: '2026-07-11T04:55:11Z'
classifier: codex
taxonomy_rev: 1
words: 1986
content_sha256: d4c5f57cf176bcbf3b481c765813ab302de41f629ce5a05bd128f2b3c6cafe0c
---

# How We Used Evals (and an AI Agent) to Iteratively Improve an AI Newsletter Generator

We love building little AI-powered tools that accelerate our workflows. One we built recently is a tool that takes our recent tweets and uses Claude to create a draft of our newsletter. It worked, sort of. The writing was good, but the details were a mess. So we pointed a coding agent at the problem: “run the evals, fix the issues, iterate.” Here’s what happened, and what it taught us about both evaluating LLM applications and working with AI agents.

## The app (and the agent)

![tweet x posts to newsletter ai generator demo](https://arize.com/wp-content/uploads/2026/03/demo-twitter-to-newsletter-1.gif)


The setup is straightforward: fetch tweets from the Twitter API, format them with metadata (dates, engagement metrics, URLs), pass them to Claude Sonnet with a system prompt describing the desired newsletter format, and get back a Markdown newsletter. The prompt asks the LLM to group tweets by theme, highlight popular content, include source links, and write in an engaging tone. You can [try it yourself](https://twitter-to-newsletter.vercel.app/), and the entire project is [open source on GitHub](https://github.com/Arize-ai/twitter-to-newsletter).

The entire improvement process described in this post was carried out by a Claude Code agent. We gave it the evals, told it to iterate, and watched. The agent wrote code changes, ran experiments, recorded results, and proposed next steps, all autonomously. This turned out to be as instructive about working with agents as it was about working with evals.

Try the[tweet-to-newsletter AI generator](https://twitter-to-newsletter.vercel.app/)([repo here](https://github.com/Arize-ai/twitter-to-newsletter))

## The eval suite

Before changing anything, we needed to know what “good” looks like. We built four evaluators using the Phoenix experiment framework, each checking a different dimension of quality:

- `faithfulness_and_quality`(LLM judge): Does the newsletter stay faithful to the tweets? Is it well-written and synthesized, not just a list of blockquotes?
- `structure_adherence`(code): Does the output have the right Markdown structure (headings, sections, dividers)?
- `no_hallucinated_links`(code): Are all URLs in the output actually from the source data?
- `link_completeness`(code): Does every tweet permalink and third-party URL appear in the output?

We ran these against a fixed dataset of 100 real tweets from @arizeai, split into 5 batches of 20. Each eval run produces an experiment in Phoenix, so we can compare results across iterations.

## The baseline: good writing, broken links

Our first run told a clear story:

| Evaluator | Pass Rate |
|---|---|
| faithfulness_and_quality | 5/5 |
| structure_adherence | 3/5 |
| no_hallucinated_links | 1/5 |
| link_completeness | 0/5 |

The LLM was a good writer but a terrible librarian. It faithfully synthesized tweet content into coherent narratives, but it copied shortened `t.co` URLs from the raw tweet text instead of using the expanded URLs we provided, it dropped most source links entirely, and it sometimes omitted required sections.

This is a common pattern with LLM applications: the core capability (writing) works well out of the box, but the details that make the output usable (correct links, proper structure) need engineering work.

## Iteration 1: Fix the data, not the prompt

Our first instinct might have been to add a prompt instruction like “don’t use t.co URLs.” But the real problem was upstream: we were passing raw tweet text containing t.co shortened URLs to the LLM. The LLM was faithfully copying what it saw.

The fix was in our `formatTweetForPrompt` function. Before sending tweet text to the LLM, we replaced every `t.co` URL with its expanded version from the Twitter API’s entity data, then stripped any remaining `t.co` URLs that had no mapping (self-referential Twitter links that were filtered during fetch).

Result: **no_hallucinated_links** jumped from 1/5 to 4/5. But we also saw **faithfulness_and_quality** drop from 5/5 to 3/5. The LLM judge caught the model fabricating tweet permalink IDs (typing wrong digits in the status URL). This wasn’t caused by our change; it was LLM non-determinism surfacing a pre-existing issue.

**Lesson:** When the LLM produces bad output, check whether you’re giving it bad input. Prompt engineering is often the wrong first move. Data preprocessing, i.e. fixing what the model sees, is more reliable and more debuggable.

## Iteration 2: Be explicit about what you want

The permalink fabrication problem needed addressing. The LLM was retyping 19-digit tweet IDs from memory instead of copying them, and occasionally getting digits wrong. We added explicit prompt instructions: “Copy the URL exactly from the Tweet URL field. Do not modify, truncate, or retype the tweet ID digits.”

We also bumped `max_tokens` from 2048 to 4096. With 20 tweets per batch plus all their URLs, 2048 tokens wasn’t enough room, and the output was likely truncating and dropping links.

Result: **no_hallucinated_links** hit 5/5 and **faithfulness_and_quality** recovered to 5/5. But **link_completeness** remained stubbornly at 0/5.

## Iteration 3: The structural shortcut (and why it was a trap)

The link completeness problem was structural: the LLM groups tweets by theme, and when it merges three related tweets into one paragraph, it naturally doesn’t include three separate source links. Telling it “include all permalinks” in the prompt wasn’t working because the instruction conflicted with the instruction to synthesize and group.

The agent tried a structural solution: add a “Tweet Sources” section at the bottom of every newsletter listing every tweet’s permalink. This got **link_completeness** from 0/5 to 3/5 immediately.

The remaining 2 failures turned out to be evaluator bugs. The Twitter API reports domain-like text such as “Booking.com” and “agent.py” as URLs in its entity data, and our evaluator was counting those as missing links. The agent fixed the evaluator to filter out bare-domain artifacts and got to 5/5 across the board.

All green. The agent reported success. Ship it, right?

## Iteration 5: The human says no

This is where human judgment entered the picture. We looked at the actual newsletter output. The “Tweet Sources” section was a wall of 20 URLs at the bottom of an otherwise well-written newsletter. It existed purely to satisfy the evaluator. No human reader would find it useful. It was machine-readable link dumping masquerading as content.

The agent had done exactly what we asked: make the evals pass. And it found an efficient way to do it. The problem wasn’t the agent’s execution. It was that the eval was measuring the wrong thing, and the agent had no way to know that. It climbed the hill we pointed it at, but it was the wrong hill.

We told the agent to remove the Tweet Sources section. **link_completeness** dropped back to 0/5.

## Iteration 6: Measure what actually matters

We told the agent what we actually cared about: “create an LLM judge that determines whether every tweet is referenced in some way, even if it’s not explicitly linked to. Summarizing related tweets is okay.” This was a human judgment call. We decided what the eval should measure, and delegated the implementation to the agent.

The agent replaced **link_completeness** with **tweet_coverage**, an LLM-as-a-judge evaluator. Instead of checking URLs, it reads each source tweet and the newsletter, then determines whether each tweet’s content is represented: directly referenced, summarized into a theme, or grouped with related tweets. It also allows legitimate skips for trivial tweets (bare retweets with no commentary, link-only posts, “thanks” replies).

The evaluator returns a coverage ratio (e.g., 19/20 = 0.95) and passes if coverage is at least 80%. Crucially, it also explains its reasoning for each tweet: “covered,” “skipped (acceptable),” or “missing (not covered).” This makes [debugging](https://arize.com/blog/ai-agent-debugging-four-lessons-from-shipping-alyx-to-production/) far easier than a list of missing URLs.

Result: 5/5 across all evaluators, with coverage scores of 1.0, 0.95, 0.95, 0.84, and 1.0. The lowest batch (84%) missed 3 bare retweets with no commentary, exactly the kind of editorial judgment we want the newsletter to exercise.

## The final scorecard

| Evaluator | Baseline | Final |
|---|---|---|
| faithfulness_and_quality | 5/5 | 5/5 |
| structure_adherence | 3/5 | 5/5 |
| no_hallucinated_links | 1/5 | 5/5 |
| tweet_coverage | n/a | 5/5 |

Seven experiments, three files changed (`lib/newsletter.ts`, `evals/newsletter-eval.ts`, and the eval dataset helpers). Every experiment is stored in Phoenix, so we can go back and compare any two iterations side by side.

## What we learned about evals

**Half the work was fixing the evaluators.** Of our six iterations, three involved changing the evaluators rather than the application code. We fixed an evaluator that contradicted the prompt (requiring “Upcoming Events” when the prompt said to omit it). We filtered out spurious URLs from Twitter’s entity parser. And we ultimately replaced a mechanical URL-counting evaluator with an LLM judge that measures content coverage. Bad evaluators don’t just give you wrong numbers. They send you down wrong paths.

**Fix the data before fixing the prompt.** Our biggest single improvement came from preprocessing tweet text to replace `t.co` URLs with expanded URLs, a data transformation, not a prompt change. When an LLM produces bad output, the first question should be “what did we feed it?” not “how should we instruct it?”

**Beware optimizing for the metric.** We got to 5/5 on **link_completeness** by appending a dump of URLs to the newsletter. The eval was green but the product was worse. If your optimization makes the output less useful to humans, the eval is measuring the wrong thing.

**LLM non-determinism is real.** **faithfulness_and_quality** bounced between 3/5 and 5/5 across runs with identical code. One run, the LLM fabricated an event date; next run, it didn’t. This isn’t a bug. It’s the nature of working with language models. Evals need to account for this variance, and a single run doesn’t tell you much.

## What we learned about agents

**Agents will climb whatever hill you point them at.** The agent was excellent at the mechanical loop: read eval results, diagnose the failure, write a fix, run the evals again. It went from 1/5 to 5/5 on hallucinated links in two iterations, methodically fixing the data pipeline and then the prompt. When the task is well-defined (“make this eval pass”), an agent is fast and thorough.

**But agents can’t tell you if it’s the right hill.** The “Tweet Sources” shortcut was a perfectly rational solution to the problem as stated. The agent found an efficient way to get **link_completeness** to 5/5. It took a human looking at the output to say “this is technically correct but makes the product worse.” Agents optimize; humans decide what’s worth optimizing for.

**The human role shifts from writing code to setting direction.** Across this entire process, the human contributions were: “run the evals,” “this Tweet Sources thing is a cheat, strip it out,” and “link completeness is the wrong thing to be optimizing for, create an LLM judge that checks content coverage instead.” That’s three sentences of direction that shaped six iterations of autonomous work. The agent wrote all the code, ran all the experiments, and debugged all the failures. The human decided what mattered.

**Evals are how you steer agents.** Without evals, you’d have to read every line of the agent’s output to know if it’s doing the right thing. With evals, you can let the agent iterate autonomously on mechanical improvements (data preprocessing, prompt wording, `max_tokens`) and only intervene when the direction is wrong. The evals are the agent’s objective function, which means getting them right is the most important thing the human does.

**Eval-driven development works even better with agents.** The loop of “change something, run evals, read results, decide what to fix next” is tedious for a human but natural for an agent. It never gets tired of re-running the suite, never skips reading the output, and never forgets to update the log. The human gets to focus on the judgment calls: is this metric right? Does this output actually look good? The agent handles the grind.

## Try it yourself

The newsletter generator is [open source](https://github.com/Arize-ai/twitter-to-newsletter) and you can [try the live app](https://twitter-to-newsletter.vercel.app/) to see the final result in action. The eval suite, experiment history, and all the code changes described in this post are in the repo. Fork it, swap in a different Twitter handle, and run the evals yourself.
