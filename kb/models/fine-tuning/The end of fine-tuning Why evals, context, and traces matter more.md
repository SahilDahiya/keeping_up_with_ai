---
title: 'The end of fine-tuning: Why evals, context, and traces matter more'
topic: models
subtopic: fine-tuning
secondary_topics:
- evals-observability/evaluation
summary: Argues that evals, context, and traces can reduce the need for fine-tuning
  in many production AI workflows.
source: arize
url: https://arize.com/blog/the-end-of-fine-tuning/
author: Laurie Voss
published: '2026-06-02'
fetched: '2026-07-11T04:56:24Z'
classifier: codex
taxonomy_rev: 1
words: 1845
content_sha256: 3574e9c3a9f136a9ca6f3d6cfbd5a8d3480330246673862e0daef953fbecc7c0
---

# The end of fine-tuning: Why evals, context, and traces matter more

Fine-tuning isn’t dead. But the way most teams iterate on AI products has permanently split in two. A tiny fraction of companies, the Cursors and Cognitions of the world, are doing more model training than ever: continuous reinforcement learning against their own production environments, with dedicated ML teams and custom GPU clusters. Everyone else has moved the iteration loop out of the model entirely, into the harness of prompts, tools, evals, and feedback loops that wraps around it. OpenAI [winding down its self-serve fine-tuning platform](https://openai.com/index/gpt-4o-fine-tuning/) in May 2026 didn’t cause this split, but it did make it impossible to ignore.

This post is about why the split happened, who ended up on each side of it, and what the 99% should actually be doing instead.

**TL;DR**

- Fine-tuning is still useful, but it is no longer the first thing most AI teams should try.
- Most teams get better returns from improving prompts, retrieval, context, tools, and evals.
- Fine-tuning requires high-quality data, strong evaluation infrastructure, and ongoing maintenance.
- Production AI systems need feedback loops, traces, and evals before model training.
- Your data is still valuable, but its value often comes from improving the system around the model.

**A quick history of fine-tuning as a product**

Fine-tuning as a concept goes back decades, but the modern lineage runs through [ULMFiT](https://arxiv.org/abs/1801.06146), a 2018 paper by Jeremy Howard and Sebastian Ruder demonstrating that a pre-trained language model could be fine-tuned on a specific task with relatively little data and achieve state-of-the-art results. That three-step structure (pre-train, fine-tune on a domain, fine-tune on a task) became, in Howard’s own words, “what everybody still does today. That’s what ChatGPT is.”

But fine-tuning as a *product*, something a developer with an API key could just do, is newer. OpenAI launched its [fine-tuning beta in mid-2021](https://community.openai.com/t/fine-tuning-beta-release/5778/2) for GPT-3, then shipped the [modern API alongside GPT-3.5 Turbo](https://openai.com/index/gpt-3-5-turbo-fine-tuning-and-api-updates/) in August 2023. The real inflection came in 2024 when they [opened fine-tuning for GPT-4o](https://openai.com/index/gpt-4o-fine-tuning/) and offered free training tokens. For roughly two years it was genuinely mainstream: on the dashboard, in the docs, the subject of every “fine-tune or RAG?” conference talk.

Other labs participated more cautiously, mostly through enterprise channels. Anthropic never offered self-serve fine-tuning. Google’s tuning lives in the corners of Vertex AI. The open-model ecosystem (Llama, Mistral, Qwen) became the place where fine-tuning stayed fully democratized, helped along by LoRA and QLoRA and services like Together AI that charge [well under a dollar per million training tokens](https://pricepertoken.com/fine-tuning). You can still fine-tune open models today. What closed is the frontier-lab on-ramp for new developers.

**Jeremy Howard saw the cracks early**

In October 2023, Howard went on Latent Space for an episode the hosts titled, provocatively given the guest, [“The End of Finetuning.”](https://www.latent.space/p/fastai) He did not say fine-tuning didn’t work. He said something more unsettling: that nobody really understood it.

“I still don’t know how to fine-tune language models properly,” he told the hosts, “and I haven’t found anybody who feels like they do.” He pointed at loss curves that showed models memorizing datasets in a single epoch. He pointed at catastrophic forgetting: Code Llama got better at code and measurably worse at everything else because almost none of its fine-tuning data was non-code. He connected this to the “alignment tax” where more-aligned versions of models were often less capable.

His conclusion was heresy from the inventor of the three-step recipe: “the right way to fine-tune language models is to actually throw away the idea of fine-tuning. There’s no such thing. There’s only continued pre-training.” Howard wasn’t predicting a have/have-not split in the industry. He was a fine-tuning *advocate* arguing for doing it properly. But what he correctly identified was the fragility at the center of the paradigm: fine-tuning done casually is a blunt instrument with side effects nobody had fully mapped. That fragility made it hard to keep offering as a point-and-click feature, and hard for anyone but deeply committed teams to wield safely.

**Why fine-tuning is hard (and “you need tons of data” is the wrong reason)**

The most common explanation for why teams shouldn’t fine-tune is “you need a huge amount of data.” This is not really true. [OpenAI’s own docs](https://developers.openai.com/api/docs/guides/supervised-fine-tuning) say the minimum is 10 examples, with improvements visible at 50 to 100. Researchers have shown that [as few as 60 data points](https://arxiv.org/pdf/2409.15825) can activate pre-trained knowledge for question-answering. Practitioners using LoRA on open models [routinely report good results from a few hundred curated examples](https://particula.tech/blog/how-much-data-fine-tune-llm). Quality beats quantity, consistently.

The real walls are elsewhere. Fine-tuning memorizes and forgets in ways nobody fully controls, exactly as Howard warned. The base model you tuned gets deprecated underneath you (as [OpenAI’s deprecation schedule](https://developers.openai.com/api/docs/deprecations) keeps demonstrating), so your carefully tuned artifact decays toward a shutdown date. Modern base models got good enough that the simplest SFT use cases, output formatting, tone, style, largely evaporated; the models just follow instructions now. And the kind of training that *does* still deliver a durable edge is not supervised fine-tuning on a few hundred examples but continuous reinforcement learning against your own production environment. That requires a fundamentally different company, not just a different dataset.

**The 1%: who’s still training, and how**

In June 2025, swyx posted [an observation](https://x.com/swyx/status/1932125643384455237) that has become a structural frame for thinking about AI products: “the top 1% of ai applications are building completely differently than the bottom 99%. Both are correct and good and usecase appropriate.” The failure mode isn’t picking the wrong approach. It’s pretending the gap doesn’t exist, or assuming you can smoothly graduate from one stack to the other.

**Cursor** published [“Improving Cursor Tab with online RL”](https://cursor.com/blog/tab-rl) in September 2025. Their Tab autocomplete handles over 400 million requests per day, giving them an enormous stream of accept/reject signals. They used policy-gradient RL to reshape the model so it produces fewer bad suggestions in the first place, rolling out new checkpoints to users and pulling data back into training within 1.5 to 2 hours. Result: 21% fewer suggestions, 28% higher accept rate. A month later they shipped [Composer](https://cursor.com/blog/composer), a full MoE coding model trained with RL across diverse environments.

**Cognition** told a parallel story with [SWE-1.5](https://cognition.ai/blog/swe-1-5): start from a strong open-source base, run RL on their own agent harness across tens of thousands of concurrent coding environments. The line that matters most: “Our vision is to co-optimize models and harness: we repeatedly dogfooded the model, noticed issues with the harness, made adjustments to tools and prompts, and then re-trained the model on the updated harness.” Even the teams whose thesis is “we train our own models” describe a *harness loop* at the center of their process.

What these examples share: hundreds of millions of daily interactions, dedicated ML research teams, [five- and six-figure training budgets per run](https://learningdaily.dev/what-is-the-cost-of-fine-tuning-llms-f5801c00b06d), and ownership of model weights they can actually do RL on. Cognition trained SWE-1.5 on “a cluster of thousands of GB200 NVL72 chips.” This is not a tier you reach by clicking a button.

**So what do you do instead?**

If iteration isn’t happening inside the model, it happens in the layer around it. That layer has matured into a real discipline with a documented lineage: prompt engineering (2022–2024), context engineering (mid-2025, crystallized by Andrej Karpathy and Shopify’s Tobi Lütke), and harness engineering (2026, pushed into circulation by Mitchell Hashimoto and [OpenAI’s Codex team](https://openai.com/index/harness-engineering/)).

Martin Fowler’s formulation is “Agent = Model + Harness,” where the harness is everything in the agent except the model: tools, memory, verification gates, retry logic, lifecycle management. As [our breakdown of agent harness architecture](https://arize.com/blog/what-is-an-agent-harness/) puts it, the modern harness “was born bottom-up out of coding agents, solving real-world problems… Cursor, Claude Code, Windsurf, and Codex are all harnesses. The same patterns, discovered separately, over and over again.”

The key insight is that harness engineering *is* a learning loop. It ingests production data (failures, traces, eval results) and turns it into a better system, encoding the learning into tools, prompts, retrieval logic, and guardrails instead of model weights. Compared to fine-tuning it is more accessible (no GPU cluster or ML team needed), lower commitment (a prompt change, not a five-figure training run), faster (minutes, not weeks), robust to model swaps (a good harness survives a deprecation; a fine-tuned artifact doesn’t), and inspectable (a harness change is a diff you can review and explain). And remember Cognition’s sentence: even the 1% describe their core loop as co-optimizing the model *and* the harness. The harness loop is not the consolation prize. It is the loop everyone runs.

**What makes the loop a loop: evals**

None of this works without rigorous evaluation, on both sides of the split. The 1% can’t do RL without it (a reward function is just an eval you’ve decided to optimize against). The 99% can’t do harness engineering without it, because without measurement, “change the harness” is just guessing with extra steps.

The kind of evaluation that matters here is not model benchmarking. As we argued in [“What is an evaluation harness?”](https://arize.com/blog/what-is-an-evaluation-harness/), the thing being evaluated in production is no longer a model; it’s a *system* whose behavior depends on retrieved context, tool calls, memory, and routing. A benchmark runner evaluates a model against standardized datasets. An [evaluation harness](https://arize.com/blog/what-is-an-evaluation-harness/) evaluates a system: it takes inputs at the right granularity (spans, traces, trajectories, sessions), scores them with whatever method fits, and acts on the result by routing failures to annotation queues, firing alerts, gating CI/CD, or feeding [experiment loops](https://arize.com/blog/from-first-eval-to-autonomous-ai-ops-a-maturity-model-for-ai-evaluation/). That third stage, acting on the score, is where most homegrown eval setups break down and where a repeatable harness turns evaluation from a measurement into a loop that moves the product.

When fine-tuning isn’t your lever, your production iteration lives in this cycle: instrument the system, observe how it behaves, evaluate against criteria you trust, change the harness, measure the delta. That cycle needs somewhere to happen. It shouldn’t be a notebook and a Slack thread.

**Your data is still your moat**

Your proprietary data, your production traces, your accept/reject signals, your records of how users succeed and fail, remains your single most defensible asset. The frontier labs didn’t take your moat. What changed is the mechanism by which you convert that data into a better product.

In the fine-tuning era the answer was: pour the data into a training run, adjust the weights, get a slightly different model. For a brief window that was a reasonable default. For a small number of well-resourced teams running continuous RL against their own environments, a more powerful version of it still is. But for the 99%, the leverage is in the harness. You take the same data and use it to evolve the system around the model: sharper prompts, better-scoped tools, smarter retrieval, tighter verification gates, a structural fix for every class of failure your evals surface.

You’re not fine-tuning a model anymore. You’re evolving a harness. The data still flows in. The product still gets better. The loop is faster, cheaper, more inspectable, and more durable than the one it replaced. And it’s the same loop, it turns out, that even the 1% can’t stop running.
