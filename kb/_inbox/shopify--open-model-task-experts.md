---
title: How Shopify turns open models into task experts (2026)
kind: blog
topic: null
subtopic: null
secondary_topics: []
summary: null
triage: null
skip_reason: null
source: shopify
url: https://shopify.engineering/open-model-task-experts
author: Andrew McNamara
published: '2026-10-21'
fetched: '2026-10-24T06:16:06Z'
classifier: null
taxonomy_rev: 2
words: 1032
content_sha256: 23858e29424268649421ad95576f437fba5cb5f569eb32959de1646bfbca2eb7
---

# How Shopify turns open models into task experts (2026)

[Sidekick](https://www.shopify.com/ca/sidekick), Shopify’s AI commerce assistant, runs on a frontier model that talks to the merchant, plans the work, and calls tools. For focused jobs, it hands off work to subagents, several of which run open models we’ve post-trained for that one task.

Take the GraphQL subagent. When a merchant asks, “Which products are almost out of stock?”, it reads Shopify’s API schema, searches the docs, writes and runs a query, and returns the results. That work is context-heavy: the subagent reads about 40 tokens for every one it writes, and a frontier model’s API charges for every one of them.

For that subagent, we built a task expert by post-training NVIDIA Nemotron 3.5 Lightning. On this task, it scores slightly higher than the frontier model, responds 7× faster, and costs about 90% less to serve. And because Shopify controls the post-trained weights, we can serve the model on our own GPUs and decide when it changes.

The loop that builds them is [Sidekick’s continual learning loop,](https://shopify.engineering/sidekicks-continual-learning-loop) with a hardware twist.

![](https://cdn.shopify.com/s/files/1/0779/4361/files/Screenshot_2026-10-20_at_4.45.30_PM.png?v=1792540098) The Model Optimization Flywheel. Three setup steps define the target, and the loop then repeats with each new batch of production data. Green tags mark NVIDIA technology.


Every task expert goes through the same steps:

### Define quality

Product experts turn requirements into a scoring rubric. For GraphQL, it covers completeness, execution, and response quality. How closely two experts agree on the same conversations sets the bar, and we tune an LLM judge with the GEPA and ACE optimizers until it agrees with held-out human labels just as well. From then on, the judge scores every agent change, candidate model, and training run.

### Improve the frontier agent

Before an open model enters the picture, we push the frontier-model version of the agent as far as it will go. An [autoresearch](https://shopify.engineering/autoresearch) loop proposes one small change at a time to the prompts, tool descriptions, or control flow, and keeps the change only if the judge’s score improves. The improved agent is the bar the open model has to beat.

### Choose an open model

We don’t pretrain. We test open models like NVIDIA Nemotron inside the real subagent, with the same tools and judge, and weigh starting quality, serving speed, and support in NVIDIA Megatron Bridge, which we train with. For GraphQL, we chose Nemotron 3.5 Lightning, a mixture-of-experts model with three billion of its 30 billion parameters active per token.

### Optimize inference

We measure serving from the start, because a model that’s too slow for production isn’t worth post-training. We benchmark every workload with NVIDIA AIPerf, an open-source  load tester in NVIDIA Dynamo, which replays production traces with synthetic text instead of customer data. Shopify contributed support for [live-response replay](https://ai-dynamo/aiperf#1400), so multi-turn tests hit the server’s prefix cache the way production does.

Those measurements guide our choice of serving stack. For Buyer Profile, a batch job, AIPerf compared vLLM, SGLang, and NVIDIA TensorRT-LLM. TensorRT-LLM did the most work per GPU. In NVIDIA’s measurements, SimGym (our shopping simulator) ran 4.5× faster on Blackwell B200 than on H200, at 1.48× lower cost.

### Turn failures into training data

![](https://cdn.shopify.com/s/files/1/0779/4361/files/Screenshot_2026-10-20_at_4.46.14_PM.png?v=1792540150) Self-healing turns a failed production conversation into a training example. Over 86 nightly runs, it repaired 69% of the failures it tried.


Every night, the judge scores a sample of production GraphQL conversations, and anything short of perfect goes to self-healing. A frontier model acting as critic writes a hint, never the answer, and a simulated merchant reruns the request with it against the same store. If the judge passes the rerun, we remove the hint, anonymize the conversation, and add it to the training set. If not, the critic tries again, up to three times.

Over 86 nightly runs recently, self-healing repaired 59,535 GraphQL conversations—69% of the failures it tried. Human annotators corrected the rest, and their corrections join the ground truth that calibrates the judge.

### Post-train on Blackwell

We post-train with NVIDIA Megatron Bridge, which brings standard Hugging Face checkpoints onto NVIDIA’s Megatron Core training library without rewriting the model, and scales across nodes on Nebius by changing settings, not code. Blackwell makes each loop cheaper: on the same FP8 post-training job for our Analytics model, eight B300 GPUs trained 1.86× faster than eight H200s, using 46% fewer GPU-hours. Then the judge scores the new checkpoint, and the loop starts again.

![](https://cdn.shopify.com/s/files/1/0779/4361/files/Screenshot_2026-10-20_at_4.46.39_PM.png?v=1792540214)

*Hopper versus Blackwell on Shopify workloads. Training: the same FP8 post-training job for our Analytics model on eight GPUs. Serving: SimGym, in NVIDIA’s measurements.*

## Results on GraphQL

![](https://cdn.shopify.com/s/files/1/0779/4361/files/Screenshot_2026-10-20_at_4.46.56_PM.png?v=1792540264)


*GraphQL judge score for Nemotron 3.5 Lightning across six flywheel loops, with the healed examples added in each loop.*

Out of the box, Nemotron 3.5 Lightning scored 37.7 on our GraphQL judge; the frontier model scored 73. The first loop took it to 61.5, and after six loops and 61,000 healed examples, the post-trained model scored 74.5.

![](https://cdn.shopify.com/s/files/1/0779/4361/files/Screenshot_2026-10-20_at_4.47.11_PM.png?v=1792540319)


*GraphQL load test, replaying production traffic with AIPerf: response time per request at the median and for the slowest 1% (p99), and serving cost compared with the frontier model.*

The post-trained model is also much faster. In an AIPerf replay of production GraphQL traffic, post-trained Nemotron returned a full response in 0.87 seconds at the median, against 6.50 seconds for the frontier model’s API, and its slowest 1% of requests finished 8× sooner. It also beat another post-trained open model of comparable size, which was close at the median but more than twice as slow at p99.

Serving cost on that traffic is about 90% lower than the frontier model’s. Across our post-trained models, self-hosting cuts serving cost by 90-98% compared with frontier model pricing.

## Frontier intelligence, specialist efficiency

The frontier model keeps the work it’s best at: talking to the merchant and deciding what to call. The token-heavy specialist work moves to open models we own, and every turn of the flywheel compounds: human corrections sharpen the judge, production traffic grows the training set, and each generation of NVIDIA hardware and software makes the next loop faster and cheaper to run.

*Thanks to NVIDIA's Megatron Bridge, AIPerf, TensorRT-LLM, and Nemotron teams; the CentML team (now part of NVIDIA); and Nebius.  Adapted from our NVIDIA GTC Berlin 2026 talk.*
