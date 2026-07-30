---
title: How to improve agent skills with tracing and evals
kind: blog
topic: null
subtopic: null
secondary_topics: []
summary: null
triage: null
skip_reason: null
source: arize
url: https://arize.com/blog/how-to-evaluate-and-optimize-agent-skills-with-tracing-and-evals/
author: Yusuf Cattaneo
published: '2026-07-28'
fetched: '2026-07-30T06:52:24Z'
classifier: null
taxonomy_rev: 2
words: 1496
content_sha256: f8f1398d451ed28eb8d8c5a6fbe6bb604192305f1f19cd347a00f665ec78e92a
---

# How to improve agent skills with tracing and evals

An agent skill cut average latency by 56%, token usage by 27%, and estimated cost by 44%. It also made the agent’s answers worse.

The regression was nearly invisible in the transcripts. It only surfaced after I tagged the traces, ran both versions against a fixed dataset, and scored those outputs against a completeness evaluator. From there, I gave a long-running agent access to the experiment results and the skill file. After several iterations it produced a version that kept most of the efficiency gains while pushing completeness above the original baseline.

Here’s how I got there. When LLM chatbots first showed up, I didn’t mind the verbosity. I was just glad to get real answers. That tolerance eventually wore off. Now the filler costs me real tokens and real time spent skimming for the actual answer. So when I stumbled on the[ i-have-adhd](https://github.com/ayghri/i-have-adhd) repo on X (promising to skip the preamble and get straight to what the agent actually means), it sounded too good to be true. Naturally, I had to try it.

This post walks through the instrumentation, evaluation setup, and multi-pass optimization loop I used to recover quality without giving back the efficiency gains.

**Key findings: trust in agent skills is earned in evals not vibes**

- Built a test agent with a flag that enabled or disabled the skill while keeping the model, prompt scaffolding, and task constant.
- Traced both paths in Arize AX and tagged every span with an OpenInference-style attribute marking whether the skill was active.
- Enabling the skill reduced token usage by 27%, latency by 56%, and estimated cost by 44%, but also reduced answer completeness.
- Used a long-running agent to revise the skill against a fixed evaluation dataset until completeness exceeded the baseline while preserving most of the latency and cost improvements.
- **The pattern**: instrument before you tune, and don’t trust a skill until an eval says it’s ready, not a vibe.

**Why agent skills need quality evals**

Skills are easy to write—and [writing effective AI agent skills](https://arize.com/blog/how-to-write-effective-ai-agent-skills/) is its own craft. The [i-have-adhd](https://github.com/ayghri/i-have-adhd) repository, for example, contains a single SKILL.md with ten rules that instruct an agent to lead with the action, number its steps, and remove preambles such as “Great question!” The intended outcome is straightforward: shorter responses that are easier to scan.

![Example SKILL.md rules from the i-have-adhd agent skill repository](https://arize.com/wp-content/uploads/2026/07/img_01-1.png)

What’s not obvious is what gets lost when a response becomes shorter. A rule set built for a coding assistant (“cap lists at five,” “suppress tangents,” “no preamble”) makes different tradeoffs depending on what the agent is actually used for. I wanted to find out what those tradeoffs looked like on a task where cutting content is a real risk, not just a style preference.

**Why manual transcript reviews missed the regression**

My first instinct was to just read skill-on and skill-off transcripts side by side. That fell apart fast. The skill-on responses *looked* better. They were shorter, more structured, and easier to skim. The stuff that was missing wasn’t obvious unless you already knew what the response was supposed to cover. By the third comparison, I was pattern-matching to “looks cleaner” instead of checking whether the response contained the required information.

![Side-by-side skill-on versus skill-off transcript comparison that looks cleaner but hides missing content](https://arize.com/wp-content/uploads/2026/07/img_02-1.png)

So I built a controlled experiment where I could measure real data. Which manifested itself as a small ADHD self-screener agent behind a single flag using the same model, the same prompt scaffolding, and the same task with the only difference being the skill.

I then traced both paths in Arize AX and tagged every span with an attribute (skill.enabled: true/false) following [OpenInference semantic conventions](https://arize.com/blog/project-rosetta-stone-instrumenting-agents-any-framework/). This made the skill-on and skill-off runs directly comparable within the same dataset instead of two piles of transcripts I was eyeballing.

![Arize AX tracing page showing the skill.enabled OpenInference-style attribute on spans](https://arize.com/wp-content/uploads/2026/07/img_03-1.png)

**Initial results: lower costs, latency, and token usage**

The first experiment produced substantial efficiency gains:

| Metric | Skill Off | Skill On | Change | 
|---|---|---|---|
| Average latency | 9,194ms | 4,081ms | -56% | 
| Total token usage | 105,994 | 76,881 | -27% | 
| Average estimated cost per run | $0.559 | $0.312 | -44% | 

The efficiency metrics around cost and latency suggested a clear improvement, which almost led me to believe that my work here was done. However, something that was gnawing at me was the thought that maybe for whatever reason those shorter/faster/cheaper responses were missing critical information. So to definitively be sure that the skill was a win all around, I decided to build an experiment that would look to put that concern to rest.

**How a completeness evaluator caught the regression**

Building on how teams [approach agent evals](https://arize.com/blog/how-to-evaluate-ai-agents-and-build-better-specs/), I curated a fixed dataset of screener conversations made up of the kind of back-and-forth you’d actually see from someone working through an ADHD self-screening chat (open-ended descriptions of symptoms, follow-up clarifying questions, incomplete answers a user circles back to) and added a completeness evaluator alongside the cost and latency metrics.

The evaluator measured whether each response covered the information required by diagnostic criteria. This was a custom evaluator for this experiment, not a clinically validated assessment or industry benchmark.

Right away, I found out my hunch was right: skill-on responses were covering fewer of the required criteria. The same rules that removed a coding assistant’s preamble were also removing required information. If I had evaluated only cost and latency, I would have shipped a faster, cheaper, and worse agent without realizing it.

**How a long-running agent optimized the skill**

Because the experiment ran against a fixed dataset, I used a long-running agent in Arize AX (Agent Swarms) to revise the skill while tracking completeness, latency, and cost — the same [systematic agent improvement](https://arize.com/blog/from-human-operated-agent-development-to-systematic-agent-improvement/) pattern of iterating against eval scores rather than vibes.

The agent repeated the following loop:

![Long-running agent optimization loop: run experiment, check scores, decide, and revise the skill](https://arize.com/wp-content/uploads/2026/07/img_05.png)

It took a few passes. The first rewrite of the completeness-related rules overcorrected and gave back most of the latency gain. The second held the line better but still lagged the skill-off baseline on one criterion. It then took a number of additional iterations to achieve the desired outcome with passes three through seven chipping away at the remaining gap.

This wasn’t a one-shot fix, and I want to be upfront about that. The evaluation scores determined whether another revision was necessary instead of a subjective review of the transcripts.

**Final results: higher completeness without losing efficiency gains**

The final skill preserved most of the cost and latency improvements while pushing completeness above the skill-off baseline. That meant it was faster, cheaper, and more complete than where I started, but only because the eval caught the regression in the middle instead of us finding out after it shipped.

**A practical workflow for evaluating agent skills**

- Tag every trace with what changed (skill on/off, prompt version, whatever the variable is), so comparisons are queries, not guesswork.
- Pick an evaluator for the quality dimension most at risk. Cost and latency can improve even when the agent becomes less useful — [token costs alone don’t tell you if your AI is working](https://arize.com/blog/why-ai-token-costs-dont-tell-you-if-your-ai-is-working/). And know what your evaluator actually measures and where it’s limited. The evaluator in this experiment was purpose-built instead of a general benchmark.
- Build your evaluation dataset from interactions you’d actually see in production instead of synthetic edge cases. Ours was made of realistic ADHD-screener conversations, not generic prompts.
- Treat the first version of a skill as a hypothesis and test it against a fixed dataset before it touches real traffic.
- Let a long-running optimization agent iterate against the eval score, not your read of a handful of transcripts — similar to how we’ve [used evals and an AI agent to iteratively improve](https://arize.com/blog/how-we-used-evals-and-an-ai-agent-to-iteratively-improve-an-ai-newsletter-generator/)other workflows. Ours took ~8 passes before completeness exceeded the baseline.
- Decide the bar before you optimize, then ship only when the skill clears it without giving back the cost and latency gains.

Agents don’t work without evals. Agent skills can change agent behavior in ways that seem good, but can still be measurably worse. Tracing makes those changes comparable, and evals show whether the new behavior is actually better. Instrument the variable, test it against a fixed dataset, and define the quality threshold before you optimize.

**Run the agent skill evaluation itself**

For anyone who might be interested, the accompanying [repository](https://github.com/Yusful33/adhd-screener-skill-demo.git) has the test application I referenced along with the two different versions of the skill (the optimized and original one). You can use it to reproduce the comparison or adapt the workflow to evaluate a skill against your own dataset and quality criteria. For a complementary look at tracing and evaluating agent changes with Arize Skills, see [Kiro CLI observability with Arize Skills](https://arize.com/blog/kiro-cli-observability-arize-skills/), and for evaluating agents more broadly, [how to evaluate AI agents and build better specs](https://arize.com/blog/how-to-evaluate-ai-agents-and-build-better-specs).
