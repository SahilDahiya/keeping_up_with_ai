---
title: Rolling deployments for zero-downtime model updates
kind: blog
topic: null
subtopic: null
secondary_topics: []
summary: null
triage: null
skip_reason: null
source: baseten
url: https://www.baseten.co/blog/rolling-deployments-zero-downtime-model-updates
author: Archit Mishra
published: '2026-06-12'
fetched: '2026-11-12T06:07:38Z'
classifier: null
taxonomy_rev: 2
words: 794
content_sha256: 489debd286f819f9fa3d829e377ae8d8611fa0b3c6f1fcadc853eb03ff252ff2
---

# Rolling deployments for zero-downtime model updates

AI engineering
# Rolling deployments for zero-downtime model updates

Update models incrementally without downtime or doubling GPU spend. Teams ship 50–60% more often, with pause, resume, and rollback controls mid-rollout.


- Authors
- Date
- June 12, 2026

TLDR

We built rolling deployments so you can ship new model versions incrementally, without doubling your GPU footprint or risking downtime. Rolling deployments are unique in the inference landscape; they replace replicas one at a time, shifting traffic incrementally until the new version is fully serving.

We heard from customers coming from other inference platforms that while updating their models, they were stuck choosing between blue-green deployments and hard cutovers.

Blue-green deployments require a full parallel fleet alongside the existing one, effectively doubling compute spend for the duration of the rollout (and challenging to do during a capacity crunch). Hard cutovers are cheaper but all-or-nothing: if you run into issues, there's no pausing mid-rollout.

To mitigate risk, some teams schedule deploys during off-peak hours to limit blast radius and manually watch dashboards for hours. The operational overhead in both cases pushes teams toward batching updates, but this means production models can run weeks behind the latest version.

We built rolling deployments to solve these issues. We see teams ship model updates 50-60% more frequently as a result, without the off-hours scheduling and manual babysitting.

A rolling deployment replaces replicas one step at a time. New replicas scale up, receive a proportional slice of traffic, and old replicas scale down. That cycle repeats until the new deployment is fully serving.

Traffic only shifts once new replicas are healthy, avoiding schedule-based issues where traffic shifts while a replica is still loading a multi-gigabyte model into memory.

At any point during the rollout, you can:

- **Pause** to inspect metrics or logs before proceeding
- **Resume** from exactly where you left off
- **Cancel** gracefully, ramping traffic back to the previous deployment
- **Force cancel** for an immediate rollback
- **Force roll forward** to complete the deployment if everything looks healthy

Two provisioning modes cover different constraints:

1. `max_surge` scales up candidate replicas before scaling down previous ones. Both versions run simultaneously during the transition, so total capacity temporarily exceeds steady-state.
2. `max_unavailable` scales down previous replicas first, then scales up the candidate into the freed capacity. Total replica count may dip below steady-state during each step, but you never exceed your original resource footprint.

We built `max_surge` to handle latency-sensitive use cases where, briefly, slight over-provisioning is acceptable.  `max_unavailable` is designed for when compute utilization is the binding constraint.

Both modes take a percentage (0–50%) that controls how many replicas change per step. A lower percentage means more steps and a slower rollout; higher means fewer steps and a faster one.

Because replicas scale up, health checks run, and traffic shifts, a rolling deployment can take tens of minutes to complete (especially at high scale). To make sure the transition is smooth and robust to failures, you have to ensure the system is stateful.

To ensure statefulness, rolling deployments run on a durable workflow engine. Each step is a discrete operation with well-defined inputs and outputs. Automatic retries, pause/resume semantics, and full visibility into deploy state are baked in. The entire history of the deployment (every step, state transition, and control action) is recorded and queryable.

These precautions prevent the system from failing silently and sitting in an ambiguous state.

Autoscaling reacts to load. Rolling deploys move load. If they run independently, they can fight: the autoscaler may scale up replicas when the rollout is about to scale down, or the rollout may remove capacity that the autoscaler just asked for.

Rolling deploys coordinate both versions as one pool, only shifting traffic after replica health and scale readiness are confirmed. They then wait through the configured stabilization window before the next step.

If desired scale jumps mid-rollout, we preserve the current traffic split and resize both versions to match.

A configurable stabilization period (0–3600 seconds) gives operators time to check metrics and confirm the new version is behaving as expected before the next increment.

When deploy risk drops, teams ship more often. Since coming onto the Baseten platform, some customers report deploying 50–60% more frequently with rolling deployments.

Mid-deploy controls are actively used in practice: we see that customers pause to inspect metrics mid-rollout, cancel on early signs of regression, and force roll forward on rollouts that look healthy. Deployments that previously required manual babysitting during off-peak windows now run unattended.

Rolling deployments were built by the Dedicated Inference team. Special thanks to the customers (like [Speechify](https://www.baseten.co/resources/customers/speechify-real-time-text-to-speech/#solution)) who provided feedback throughout the design and rollout process!

If deployment logistics are eating into your engineering time, [get started with rolling deployments](https://docs.baseten.co/deployment/rolling-deployments) or [reach out](https://www.baseten.co/talk-to-us/) to talk to our engineers.
