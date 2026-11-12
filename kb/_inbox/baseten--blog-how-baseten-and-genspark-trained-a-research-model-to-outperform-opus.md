---
title: The platform for inference, training, and execution | Baseten
kind: blog
topic: null
subtopic: null
secondary_topics: []
summary: null
triage: null
skip_reason: null
source: baseten
url: https://www.baseten.co/blog/how-baseten-and-genspark-trained-a-research-model-to-outperform-opus
author: Jonathon Liu
published: '2026-11-10'
fetched: '2026-11-12T06:06:42Z'
classifier: null
taxonomy_rev: 2
words: 2656
content_sha256: ba9959f3f54a1fae855b0d37f1344c770f0621d099dc65db15f21723bb67e56d
---

# The platform for inference, training, and execution | Baseten

News
# How Baseten and Genspark trained a deep research model to outperform Opus 5.5

Genspark worked with Baseten Applied Research to post-train Qwen3.5-397B into a specialized deep research model that outperforms the closed frontier.


- Authors
- Date
- November 10, 2026

Genspark worked with Baseten Applied Research to post-train Qwen3.5-397B into a specialized Deep Research model. On Genspark's quality grader, it scores **0.759, up from 0.612** for the base model, scoring above Opus 5.5 (0.738), Sonnet 5.5 (0.742), GPT-5.6 Sol (0.637), as well as Kimi K3 (0.724) and DeepSeek V4 Pro (0.675).

The post-trained model researches more broadly and deeply, crawling **5× more sources** than the base model per user query, and writes longer and better-cited reports. Running with NVFP4 weights on just 2×B200 GPUs per replica, the model now powers Genspark’s Deep Research agent in production.

"Deep Research is one of the most demanding workloads we run: long contexts, dozens of tool calls per question, and users who expect the report to be right. Working with Baseten, we post-trained an open 397B model on our own research tasks and now serve it as the default for Deep Research because it outperforms closed models. We keep the weights, the evaluations and the training code, so the model keeps improving on our terms."


[Genspark](https://www.genspark.ai/) is one of the fastest-growing AI workspaces, and Deep Research is one of its flagship agents. Give it a hard question and it plans a research strategy, runs dozens of searches, reads the pages that matter, and returns a long, cited report in minutes.

Frontier closed-weight models handle Deep Research well, but they are expensive at Genspark's volume, and you can only change the prompt, not the weights. Genspark was ahead of most teams here: when we started working with them, Deep Research already ran on an open model they had fine-tuned. So the question wasn't whether to move off closed models, but how much further post-training could take an open one. They wanted deeper research and stronger reports, trained to their own quality bar, from a model efficient enough to serve at scale.

Good training infrastructure is the foundation for post-training. Baseten provides it through the [Baseten Loops SDK](https://docs.baseten.co/loops/overview), a platform for teams that want to run supervised fine-tuning (SFT) and reinforcement learning (RL) themselves with full visibility and control over the process. For teams that want hands-on support, Baseten also offers Baseten Applied Research, a team that works alongside them to reach their cost and performance goals. Deep Research called for that kind of partnership.

In this engagement, the Baseten Applied Research team worked hands-on alongside Genspark's team. Training ran against Genspark's own agent harness and tools the team had already built, so the model learned in the same environment it would eventually serve in. From there, the work was reading trajectories, running diagnostic experiments, designing rewards, and debugging training runs. We start with high-level research questions like: Which behaviors are holding the model back? Which training method fits each one? Is the reward teaching the model the right things? The rest of this blog dives into what this actually looks like, from the first grader review to production serving.

To establish the training target, we start every applied research engagement with the evaluation. Some customers arrive with a product and an intuitive sense of what "better" means, and we build the evaluation with them from scratch. Others already have evals they trust.

Genspark was in the second group. They had already built out a full evaluation infrastructure, including representative research queries and an LLM grader that was served from their own endpoint and scored reports against their quality bar. Before training against it, we stress-tested the grader for blind spots and reward hacks, and Genspark's engineers tightened it based on what we found. Together we agreed on baselines, a held-out test set, and what a model would need to show before going to production.

The obvious next move would have been to start RL: roll out the agent, grade the report, reinforce what scores well. Instead, we went through the agent's trajectories first. Because training ran in Genspark's own harness, every trajectory showed exactly how their production agent behaves, which made it possible to see where reports were going wrong.

A Deep Research trajectory can be thought of as two phases.

1. In the **research** phase, the agent performs searches, reads pages, and decides when it has seen enough.
2. In **synthesis**, it turns 50K+ tokens of raw evidence into a complete, cited report.

When a report is scored as weak, the score alone does not provide enough insight into which phase was the issue. So we ended up measuring the two phases separately. To isolate synthesis quality, we held the research fixed. For each base-model trajectory, we compared the model’s own report with a report written by a stronger writer model from exactly the same collected evidence. On a small diagnostic panel, the score rose from **0.58 to 0.73**. So, while both research and report-writing stages had room to improve, replacing only the writing recovered most of the gap to the frontier. The base model’s research was a workable starting point; its synthesis was the larger bottleneck to a higher eval score.

**From a training perspective, the Deep Research task is two jobs, not one.** Research and synthesis fail differently and learn from different kinds of signal, so we trained them with different methods.

RL learns from a single reward at the end of a long episode, and here that reward mostly comes from an LLM judge. For the research phase, that signal worked well: whether the agent searched broadly and read the right sources is relatively easy for a judge to assess, and partly countable.

However, good writing is a bit more subtle to judge and grade. Structure, emphasis, and how evidence is weighed and cited are harder to capture in a single score, so RL alone is a slower, noisier way to teach this skill. Instead, strong example reports show the model directly what good writing looks like. Our first attempt to train the writing stage with RL stalled because nearly every report scored about the same, so there was almost no signal to learn from. An SFT warm-up introduced the target writing behaviors of style, conciseness, and structured prose, enabling the model to break through this initial limitation. Subsequent RL smoothed out the effects of SFT, integrating those behaviors with the model’s existing research behavior.

So we split the methods along the same line as the task:

- **Research → reinforcement learning.** The agent explores, and the reward tells it which research strategies lead to better reports.
- **Writing → primarily supervised fine-tuning.** We paired each of the model's own research trajectories with a high-quality report written from exactly that evidence. Every token of the target shows how to use what's in the context, and because the evidence is the model's own, it learns to write from the material it actually gathers.

A grader captures what a team can write down in advance, rarely everything they care about. To find the rest, each round of training ended with Genspark's team reviewing our candidate trained models. They ran side-by-side comparisons against their production agent and a frontier model, and scored reports on coverage, depth, citations, and trustworthiness. They also compared outputs in pairs on real production queries, using the grader rubric to evaluate each report. Genspark manually reviewed a sample of the outputs.

Genspark’s reviews helped us look beyond the grader score and incorporate elements such as citation quality, corroboration across sources, and how well the model followed multipart instructions. Their feedback called for more research and longer, more complete reports. Broader research gives the model more evidence to check claims against and more complete reports give it room to address each part of a question.

To check that these gains held beyond the training signal, Genspark evaluated candidate models using a separate grader and manual spot checks. This helped distinguish actual improvements in report quality versus overfitting to the grader we trained against. The decision to put the model into production was based on Genspark’s own harness grader plus an independent judge model on real production cases.

A good eval is not always a good reward. An eval only has to rank finished answers correctly. A reward has to give a **crisp, directional signal at every stage of training**: it has to tell the model which way is better to guide it from a weaker base model to a stronger, specialized model. Genspark's grader could identify better reports, but it gave the model little direct incentive to research more broadly. Extra searches only improved the score if they led to a better final report. Training against that score alone therefore increased research breadth slowly.

Reward shaping is how we closed that gap. It adds terms that give a direct signal for the behavior you want, sized to what the model can currently do. For research breadth, the hard part was deciding how much research is *enough*. A factual lookup might need two searches, and a market analysis might need thirty searches and a dozen sources. Using the same target for every question would ask too much of easy questions and too little of hard ones.

So we set targets per question, from data. We ran a suite of models on every training question and analyzed the distribution of their research: across roughly a thousand questions, a median of about 17 distinct searches and 5 distinct sites, a long tail past 30 and 10, and about one question in ten where the reference models didn't search at all. Each question's targets ${Q_i}$ and ${D_i}$ are the most distinct queries and sites any reference model used on it. The research score credits the agent's distinct queries $q$ and sites $d$ against those targets, capped once a target is met:

$$
S = w_q \cdot \min\left(\frac{q}{Q_i}, 1\right) + w_d \cdot \min\left(\frac{d}{D_i}, 1\right), \quad w_q = 0.4,\; w_d = 0.6
$$

Sites weigh more because reading sources is what puts evidence into a report, and redundant queries are cheap. If no reference model searched on a question, that component gets full credit, so the agent isn't pushed to search where it isn't warranted. The final reward blends S with the LLM grader's quality score G at 2:1 and stays in \[0, 1\]:

$$
{R = \frac{G + \lambda S}{1 + \lambda}}, \quad{\lambda = 0.5}
$$

Can the model hack this by searching for random, unrelated things? Not very far, because the LLM grader component keeps it in check. The LLM judge reads the full research trace alongside the report and judges whether searches were relevant and sources actually used, so padding a trace lowers G even if it raises S. We monitored for it anyway, and breadth gains came with higher grader scores, not at their expense. In our experiments, **our reward-shaped run at 50 steps outperformed runs without reward shaping at 200 steps.**

This is a **semi-verifiable** reward: an LLM judgment of quality combined with objective, countable signals about behavior. In our experience it often beats a pure LLM-judge reward. The objective terms give a steady, hard-to-fool signal on what can be counted, and the judge captures qualities that cannot be calculated as simple metrics. Purely verifiable rewards aren't an option for most real tasks. There is no unit test for a good research report.

Reward shaping is also not set-and-forget. The right terms and weights depend on how strong the model is, and as training progresses they may need re-tuning. We have done this on other engagements, and it's a normal part of running RL on real tasks.

At its core, the training recipe consists three stages:

1. **Search RL**: targets research breadth and tool use, trained against the shaped reward. The agent's own report is set aside, and a frozen strong writer produces the report from its research, so the reward reflects the quality of the research and not the model's still-weak writing.
2. **Writing SFT**: starting from the search-trained model, dense supervision on synthesis, pairing its own research trajectories with high-quality reports written from exactly that evidence. The research turns stay anchored during this stage, so the model learns to write without forgetting how to search.
3. **End-to-end RL:** the full agent loop, training research and writing together with the same shaped reward, to smooth out the effects of SFT so the two stages work well together.

We've since rerun the recipe from scratch in controlled replication studies, changing one variable at a time, and reproduced the result.

| Variables | Base Qwen3.5-397B | Genspark x Baseten | 
|---|---|---|
| Grader Score | 0.612 | 0.759 | 
| Sites crawled per question | 4.5 | 21.7 | 
| Tool calls per questions | 7.9 | 28.5 | 
| Report length | 12.1K characters | 15.9K characters | 

In Genspark’s review against its previous production model, the new model showed strengths in citation quality, corroboration across sources, and handling complex, multipart instructions. It also crawled 5× more sources per query than the base model.

Cost efficiency was a significant factor in this engagement, so serving was planned from the start. We quantized the expert weights to NVFP4 and kept the fine-tuned attention layers at full precision. On our full eval suite, the NVFP4 model matched full precision within eval noise, while reducing the GPU requirement per replica by half from 4 x B200 to 2 × B200 at FP8. Cache-aware routing keeps each research session on the same replica. Each request decodes at about 160 tokens/s in production, and in load testing a single replica stayed above Genspark's 110 tok/s target with up to 8 concurrent requests.

Genspark validated the quantized model in their own harness against a series of tests, then rolled it out gradually, starting with a small share of production traffic and scaling up until it became the default for Deep Research.

- **Split the task when it has subcomponents.** Research breadth and report synthesis are distinct behaviors with different measures of success. Evaluating them separately revealed where the model was weak and let us target each one independently.
- **Use the right tool for each behavior.** RL works well when a scalar reward can reliably distinguish better from worse and guide incremental improvement. SFT works better when strong examples can demonstrate the desired behavior with dense, token-by-token supervision.
- **Evals need iteration and shaping to become good rewards.** A grader is a starting point: stress-test it with the customer, and revise it as review surfaces new preferences. To train against it, add shaping terms that give a clear signal for the behaviors you want, with the judge positioned to catch the model gaming them.
- **Treat product-owner review as a training signal.** The most important requirements came from Genspark's team generating outputs with our model and reading through them, not from the grader. Each round of their feedback became a new reward term or training target.

Most applied research engagements start in different places, but we often find that real, production workloads are different from what’s studied in academia. Much of the academic RL literature studies fully verifiable domains like math and code. Most customer workloads, such as research, writing, and analysis, are judged rather than checked. **Training for these workloads calls for semi-verifiable rewards that combine LLM judgments with objective metrics, and this is where we specialize.**

Our work encompasses building or hardening the evaluation, diagnosing where the model falls short, choosing and running the right training methods, turning product feedback into training signal, and optimizing serving. It’s been great working with Genspark and since they keep the weights, the evaluations, and the training code, the model will continually improve.

Open-weight models are a strong foundation. Post-training is how they become *your* model, trained on your specific data and improving on your schedule.

Work with Baseten's Applied Research team [here](https://www.baseten.co/talk-to-us/research-support).
