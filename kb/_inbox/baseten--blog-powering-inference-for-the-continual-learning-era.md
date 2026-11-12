---
title: Powering Inference for the Continual Learning Era
kind: blog
topic: null
subtopic: null
secondary_topics: []
summary: null
triage: null
skip_reason: null
source: baseten
url: https://www.baseten.co/blog/powering-inference-for-the-continual-learning-era
author: Bola Malek
published: '2026-05-27'
fetched: '2026-11-12T06:14:50Z'
classifier: null
taxonomy_rev: 2
words: 1402
content_sha256: a7701dafe14421c5e1e163c644ac7b41973187f5db1c56997e9505efd045df30
---

# Powering Inference for the Continual Learning Era

Community
# Powering Inference for the Continual Learning Era

How Trajectory went from research to production at scale with Baseten.


- Authors
- Date
- May 27, 2026

Models are more powerful than ever. But the way we use them is static. You use a product, and the model behind it stays the same until the next quarterly release. Every time you run into an issue and find a workaround, you have to wait weeks or months for the model itself to hopefully get better. Benchmarks go up. Products don't.

A new paradigm is on the horizon: continual learning. Models that get better the longer you use them. A legal product sharpens on legal work the longer lawyers use it. A support agent internalizes the shape of the tickets it actually sees. A coding product learns the codebase it lives inside. The model and the product stop being separate things.

Getting there means solving many problems at once. At the research layer, how do you learn from production traces in a way that turns every interaction into a training signal? At the product layer, how do you let builders shape their model and the harness around it as a single object, so the way the product behaves and the way the model learns evolve together. At the infrastructure layer, how do you serve a model that is no longer a fixed artifact but a moving target?

Trajectory is the team pioneering this paradigm. They take production traces, identify failure modes, and continuously retrain models to fix them. Over the last five months, we have been working with them on the infrastructure question, because the inference stack is what determines whether the loop can close fast enough to matter. The rest of this post is about what we have built together, and the road ahead.

Inference is built around a model that holds still. Quantization, speculative decoding, KV cache reuse, prefix caching, every meaningful optimization in modern serving assumes that the weights are stable. The model is the constant; the request is the variable.

Continual learning relaxes that assumption in two directions at once.

The deploy cadence compresses drastically. Checkpoints arrive from training runs hourly. The pipeline from a freshly-trained model to a live endpoint has to be measured in minutes; anything longer breaks the feedback loop that the training side depends on.

The number of distinct models multiplies. A single product can run a different model per customer, per environment, per experiment. The serving fleet routes thousands of subtly different variants rather than a handful of base models, and each variant needs the same first-class treatment: auth, routing, observability, versioning.

Continual learning compresses every step between training and serving. A new adapter coming off a training run has minutes, not hours, before the signal that prompted the retrain goes stale. The pipeline we built with Trajectory takes a LoRA adapter from a finished training run and puts it behind a live OpenAI-compatible endpoint at `model-{id}.api.trajectory.ai`. Each stage looks superficially like normal model deployment, and each one is different under the hood because the assumptions have changed.

- **Checkpoint arrives.** A training run finishes and writes a LoRA adapter to training storage. This is the moment the clock starts.
- **Merge.** The adapter is pulled and merged into the base model. A LoRA merge looks like a single matrix multiplication on paper. In modern model families it isn't always. There can be fused projections (where Q, K, V projections share one underlying matrix), MXFP4 quantization (where the merge has to respect block-wise scaling factors), and expert broadcasting in MoE models (where each expert's adapter has to be merged independently) where each imposes different correctness constraints that a naive merge does not respect. In a static deployment, you do this once and ship. Under continual learning, you do it every hour, on every customer's adapter, against a moving target of base model versions. We run architecture-aware correctness checks on every merged checkpoint, because shipping a silently broken model into a training loop poisons the next round of training too.
- **Packaging.** The merged model is packaged with Truss, Baseten's framework for turning a model into a deployable artifact. Truss handles dependencies, runtime spec, and serving configuration. Without it, every new checkpoint would require hand-assembling the same boilerplate; with it, the merged model is one command from being deployable.
- **Validation against the serving runtime.** Baseten's custom serving runtime applies the optimizations that make inference fast in production: quantization narrowed to the layers that survive it, RoPE scaling for extended context, speculative decoding with a matched draft. Each has correctness constraints that not every checkpoint satisfies. Under continual learning, a checkpoint that fails one of these is not a once-a-quarter release blocker; it is an hourly occurrence that has to be caught automatically before deployment, not after a user hits it.
- **Deployment and A/B test routing.** The validated artifact is deployed onto Baseten's distributed network and routed at `model-{id}.api.trajectory.ai`. Routing is where one of the deeper inversions of continual learning shows up: every new checkpoint is treated as an experimental variant, not a promotion. In static-model serving, a new version replaces the old one. Under continual learning, the new version is a hypothesis, and the old version is its control. Our routing layer splits traffic between the two, partitions telemetry so the training pipeline can compare them on live production load, and only promotes when the data says to. The same routing layer also handles multi-tenancy: every model, route, and API key is scoped to a customer, with isolation inherited from the data model rather than bolted onto the serving layer.
- **Live with provenance.** Once the endpoint is live, every request it serves is logged with full provenance: which model version answered it, deployed when, from which training run. This is the part of the pipeline that closes the loop. Inference is not the end state of a continually-trained model; it is the source of the next training run.

The whole pipeline runs in roughly an hour, end to end. That is short enough to keep the training side useful, and longer than we want it to be.

We have an inference stack that ships continually-trained models into production. But there is still a long road ahead to the true continual learning dream, where models improve within hours, and a single product serves hundreds of distinct models across its users.

Two of the open challenges on that road:

- **Multi-LoRA serving.** Today, we merge each adapter at deploy time for architectural correctness. The next step is a base-resident architecture that selects an adapter per request, collapsing the cost curve for serving a long tail of customer-specific intelligences.
- **Continually-trained draft models.** Offline-trained draft models lose acceptance quickly as the main model shifts underneath them, a failure mode that gets worse as the refresh rate climbs. To preserve speculative decoding under continual learning, every shipped checkpoint needs a matched draft model trained alongside it.

Continual learning is a shift from models as artifacts to models as processes. The research question of how to learn from production traces, the product question of how builders compose a model and its harness as one object, and the infrastructure question of how to serve a moving target are all open. The era is just starting.

Trajectory is taking the platform approach to this paradigm. Rather than building a single vertical product on top of continual learning, they are building the substrate that lets any product company adopt it, and they are building it for scale from day one. But that is no easy feat. What we have built together is the first version of the inference layer for that platform: a pipeline that takes a freshly trained LoRA adapter and puts it behind a live, A/B routed, fully provenanced endpoint in roughly an hour. That is enough to run continual learning in production today, and it is the foundation we will keep pushing on as the loop tightens to minutes and a single product begins serving hundreds of distinct intelligences across its users.

We are entering a multi-model future. We are excited to be building the inference stack for it alongside Trajectory. If you want to learn more about the Baseten Inference Platform, reach out to talk to our engineers [here](https://www.baseten.co/talk-to-us/). And if you would like to learn more about Trajectory’s continual learning solution, visit their website [here](http://trajectory.ai/).
