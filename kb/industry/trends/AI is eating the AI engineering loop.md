---
title: AI is eating the AI engineering loop
topic: industry
subtopic: trends
secondary_topics:
- agents/tool-use
- evals-observability/evaluation
summary: Argues that AI is reshaping the AI engineering loop itself, with agents increasingly
  participating in prompt, eval, observability, and product iteration workflows.
source: langfuse
url: https://langfuse.com/blog/2026-06-09-ai-is-eating-ai-engineering
author: Swyx · Follow
published: '2026-06-09'
fetched: '2026-07-11T04:36:38Z'
classifier: codex
taxonomy_rev: 1
words: 1262
content_sha256: 523cbc79be945b08833e056000028902b268e4a3438f8b4a289298aec75bb4ee
---

# AI is eating the AI engineering loop

![swyx](https://pbs.twimg.com/profile_images/2073162797354217472/hNny55eF_normal.jpg)

every evals/analytics startup is going through a onetime generational upgrade into a continual learning platform in 2026 many will fail but as always the tasteful ones win

June 9, 2026# AI is eating the AI engineering loop

![Picture Lotte Verheyden](/_next/image?url=%2Fimages%2Fpeople%2Flotteverheyden.jpg&w=96&q=75) Lotte Verheyden

Lotte Verheyden

The full AI engineering loop can technically be automated now. But that doesn't mean it should. Here is what we think you should hand to agents, and what you should keep doing yourself.

AI agents can run almost every step of the [AI engineering loop](https://langfuse.com#ai-engineering-loop) on their own. The tools are in place, the context is available, and the loop can close without a human touching it.

That is also where the industry is heading, often referred to as "continual learning":

every evals/analytics startup is going through a onetime generational upgrade into a continual learning platform in 2026 many will fail but as always the tasteful ones win

We think this is directionally right. We also think handing over the whole loop is a mistake. Automate past the point where you can still vouch for the output, and you'll find yourself shipping *agent slop*.

The AI engineering loop is how we describe the process of continuously improving AI agents, based on what we have seen across the industry and across our user base. We wrote about it extensively in our [academy](https://langfuse.com/academy/ai-engineering-loop).

Part of the loop runs on live activity. Traces flow in from production, and monitoring surfaces anything worth a closer look. Part of monitoring is reading traces yourself. This gives you direct insight into how the system behaves and is one of the more valuable steps in the whole process.

The rest happens in development, before shipping a change. You build a dataset that approximates real production usage, so you can test changes systematically and hill-climb on quality. If a change performs better, you deploy it to production. **This is a continuous process**.

Walk through the steps and none of them technically need a human. Instrumenting an app is something agents do fully autonomously now. For every other step, platforms usually have an [API](https://langfuse.com/docs/api-and-data-platform/features/public-api) or a [CLI](https://langfuse.com/docs/api-and-data-platform/features/cli) an agent can call to do the work.

| Job | Tools exist to automate |
|---|---|
| Read traces, surface all anomalies, and label them | ✅ |
| Build datasets from production errors and synthetic cases | ✅ |
| Run experiments and derive new ideas to hill-climb against evals | ✅ |
| Test a newly released model and open a PR with the adapted agent | ✅ |
| ... | ... |

So if every step can be automated, the loop can close on its own. But while we can technically automate the entire process, that does not mean we should. Removing yourself from the loop comes at a cost, and that cost has a name: **agent slop**.


Agent slop: low-quality AI agents, mass produced by other AI agents. Often the result of agents optimizing against imperfect evals and datasets.

You want your agent to behave the way you decided is right, with the nuance you care about. That nuance lives in your head and is based on your continuously evolving opinion. Automate the entire loop and the agent optimizes toward a target that is not complete, and becomes stale over time.

![Without course correction along the way, the loop drifts off the path and never reaches the optimal destination](https://langfuse.com/_next/image?url=%2Fimages%2Fblog%2F2026-06-09-ai-is-eating-ai-engineering%2Fagent-slop.png&w=3840&q=75)


This produces agents that behave sort of how you want, but people can feel the quality bar is lacking. Your users deserve better than that, and it's your responsibility to hold the bar high.

A practical example of an incomplete target function is when we ran [autoresearch on the Langfuse skill](https://langfuse.com/blog/2026-03-24-optimizing-ai-skill-with-autoresearch). An agent optimizes against the evaluator's gradient, so misspecify the target and it will move in the wrong direction very quickly.

We do see a future where most of this loop runs on its own. But you need to make **deliberate choices on what an agent can own, and keep yourself involved where your judgment is the product**.

![Manual work is high effort, automating everything sacrifices quality; the ideal balance shifts your effort toward judgment for higher-leverage, higher-quality work](https://langfuse.com/_next/image?url=%2Fimages%2Fblog%2F2026-06-09-ai-is-eating-ai-engineering%2Fautomate-manual-quadrant-v2.png&w=3840&q=75)


If you do this well, your quality should improve, because you can focus on the high-leverage work you would otherwise not have time for. But if you overdo it, you risk producing *agent slop*.

AI applications produce behavior you cannot predict in advance. If you only read the traces an agent or previously set up evaluators flagged for you, you only ever see the slice it was already told to look at. To catch what would otherwise slip through, sample your traces regularly and read them yourself. **This is also where your opinion gets formed**.

While forming your opinion, you'll leave feedback on these traces that the agent can then pick up. These corrections steer the agent back towards what you consider good.

![The AI engineering loop annotated with the steps where you should keep looking at traces manually](https://langfuse.com/_next/image?url=%2Fimages%2Fblog%2F2026-06-09-ai-is-eating-ai-engineering%2Fmanual-steps-loop-v2.png&w=3840&q=75)


One thing worth mentioning is the value of **implicit user signals**. It's technically automated, but the input stays human. It's a great way to surface traces worth a closer look, that you didn't tell the system to look at.

Everything else can be handed to an agent, **as long as it has the context to do it well**.

What your app should do, what counts as a good answer, which behaviors are unacceptable: only you can teach the agent that. You give that context in concrete forms: the feedback you leave on traces as you monitor, and the direction you set for what to evaluate. From there, you can build the datasets and evaluators together with the agent.

| Step | Manual | Automated | Ideal balance |
|---|---|---|---|
| Trace | - | One-time setup; traces flow in automatically. | Automated. |
| Monitor | You read every trace by hand. Insightful but unsustainable. | Agent flags known rules and obvious mistakes; quality plateaus early. | Automate it, but keep sampling traces to catch unanticipated behavior. |
| Build datasets | You hand-pick every example. Representative but slow to maintain. | Agent builds datasets from its own labels; they plateau with your monitoring. | Your monitoring feedback keeps the dataset diverse and representative. |
| Experiment | You test variants by hand. Thorough but limited in reach. | Agent generates and runs variants to push the metrics. | Automate by default; step in ad-hoc. |
| Evaluate | You grade runs and build evaluators by hand. Accurate but tedious. | Evaluators self-update; quality plateaus once the obvious is fixed. | Review a sample and let the agent calibrate from your feedback. |

As your application matures, this context becomes more and more about opinionated nuances that only you can capture. **All of this comes from you looking at your traces**, and the sharper the context, the more of the loop you can safely hand off.

Automation only pays off once you have a good enough understanding of what to evaluate continuously, and what representative datasets and metrics look like for that. [Error analysis](https://langfuse.com/academy/monitoring/error-analysis) is a good way to build that understanding before you hand off.

The mechanical work of the loop is going to agents, and that is good news: it frees you for the part that makes your agent yours. With the labor becoming the same for everyone, what sets your agent apart is your sense of what good looks like, and the care you put into teaching it.

Was this page helpful?
