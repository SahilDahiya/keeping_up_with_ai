---
title: Rolling deployments for zero-downtime model updates
topic: infra-platform
subtopic: deployment
secondary_topics:
- inference/serving
summary: Explains rolling deployments for zero-downtime model updates in production
  serving systems.
source: baseten
url: https://www.baseten.co/blog/rolling-deployments-zero-downtime-model-updates/
author: Archit Mishra; Jonathan Rochette; Sid Shanker
published: '2026-06-12'
fetched: '2026-07-11T04:05:07Z'
classifier: codex
taxonomy_rev: 1
words: 1091
content_sha256: 55492577f1bd4d48c27b830f5e62bed4d6c4b41da640b2287a52b7f22ab8cd0f
triage: keep
skip_reason: null
---

# Rolling deployments for zero-downtime model updates

![Rolling deployments for zero-downtime model updates](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1781083187-baseten-blog-2026-thumbnails-10.png%3Fauto%3Dformat%26fit%3Dcrop%26h%3D630%26w%3D1200&w=3840&q=100)

We built rolling deployments so you can ship new model versions incrementally, without doubling your GPU footprint or risking downtime. Rolling deployments are unique in the inference landscape; they replace replicas one at a time, shifting traffic incrementally until the new version is fully serving.

We heard from customers coming from other inference platforms that while updating their models, they were stuck choosing between blue-green deployments and hard cutovers.

Blue-green deployments require a full parallel fleet alongside the existing one, effectively doubling compute spend for the duration of the rollout (and challenging to do during a capacity crunch). Hard cutovers are cheaper but all-or-nothing: if you run into issues, there's no pausing mid-rollout.

To mitigate risk, some teams schedule deploys during off-peak hours to limit blast radius and manually watch dashboards for hours. The operational overhead in both cases pushes teams toward batching updates, but this means production models can run weeks behind the latest version.

We built rolling deployments to solve these issues. We see teams ship model updates 50-60% more frequently as a result, without the off-hours scheduling and manual babysitting.

## How rolling deployments work

A rolling deployment replaces replicas one step at a time. New replicas scale up, receive a proportional slice of traffic, and old replicas scale down. That cycle repeats until the new deployment is fully serving.

![Rolling deployments: Traffic shifts from the current deployment to the candidate one step at a time. At each step, a new candidate replica (or portion of replicas) spins up and passes health checks before the current group is removed.](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1781092679-image1.png%3Fauto%3Dformat%26w%3D1200&w=3840&q=75) Rolling deployments: Traffic shifts from the current deployment to the candidate one step at a time. At each step, a new candidate replica (or portion of replicas) spins up and passes health checks before the current group is removed.

Rolling deployments: Traffic shifts from the current deployment to the candidate one step at a time. At each step, a new candidate replica (or portion of replicas) spins up and passes health checks before the current group is removed.Traffic only shifts once new replicas are healthy, avoiding schedule-based issues where traffic shifts while a replica is still loading a multi-gigabyte model into memory.

At any point during the rollout, you can:

- **Pause**to inspect metrics or logs before proceeding
- **Resume**from exactly where you left off
- **Cancel**gracefully, ramping traffic back to the previous deployment
- **Force cancel**for an immediate rollback
- **Force roll forward**to complete the deployment if everything looks healthy

## Under the hood: orchestration, traffic shifting, and autoscaling

### Managing latency and cost sensitivity

Two provisioning modes cover different constraints:

- `max_surge`scales up candidate replicas before scaling down previous ones. Both versions run simultaneously during the transition, so total capacity temporarily exceeds steady-state.
- `max_unavailable`scales down previous replicas first, then scales up the candidate into the freed capacity. Total replica count may dip below steady-state during each step, but you never exceed your original resource footprint.

We built `max_surge` to handle latency-sensitive use cases where, briefly, slight over-provisioning is acceptable.  `max_unavailable` is designed for when compute utilization is the binding constraint.

Both modes take a percentage (0–50%) that controls how many replicas change per step. A lower percentage means more steps and a slower rollout; higher means fewer steps and a faster one.

![During a rolling deployment, Max Surge temporarily runs an extra replica, keeping full capacity online while the new version comes up. Max Unavailable takes the opposite approach: it removes a replica first and replaces it within the existing footprint, accepting a brief capacity dip. Use Max Surge when latency is the priority; use Max Unavailable when you're optimizing for compute cost.](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1781092714-image2.png%3Fauto%3Dformat%26w%3D1200&w=3840&q=75) During a rolling deployment, Max Surge temporarily runs an extra replica, keeping full capacity online while the new version comes up. Max Unavailable takes the opposite approach: it removes a replica first and replaces it within the existing footprint, accepting a brief capacity dip. Use Max Surge when latency is the priority; use Max Unavailable when you're optimizing for compute cost.

During a rolling deployment, Max Surge temporarily runs an extra replica, keeping full capacity online while the new version comes up. Max Unavailable takes the opposite approach: it removes a replica first and replaces it within the existing footprint, accepting a brief capacity dip. Use Max Surge when latency is the priority; use Max Unavailable when you're optimizing for compute cost.### Durable workflow orchestration

Because replicas scale up, health checks run, and traffic shifts, a rolling deployment can take tens of minutes to complete (especially at high scale). To make sure the transition is smooth and robust to failures, you have to ensure the system is stateful.

To ensure statefulness, rolling deployments run on a durable workflow engine. Each step is a discrete operation with well-defined inputs and outputs. Automatic retries, pause/resume semantics, and full visibility into deploy state are baked in. The entire history of the deployment (every step, state transition, and control action) is recorded and queryable.

These precautions prevent the system from failing silently and sitting in an ambiguous state.

### What happens if load spikes mid-deploy?

Autoscaling reacts to load. Rolling deploys move load. If they run independently, they can fight: the autoscaler may scale up replicas when the rollout is about to scale down, or the rollout may remove capacity that the autoscaler just asked for.

Rolling deploys coordinate both versions as one pool, only shifting traffic after replica health and scale readiness are confirmed. They then wait through the configured stabilization window before the next step.

If desired scale jumps mid-rollout, we preserve the current traffic split and resize both versions to match.

A configurable stabilization period (0–3600 seconds) gives operators time to check metrics and confirm the new version is behaving as expected before the next increment.

## Customers deploy 50-60% more often

When deploy risk drops, teams ship more often. Since coming onto the Baseten platform, some customers report deploying 50–60% more frequently with rolling deployments.

Mid-deploy controls are actively used in practice: we see that customers pause to inspect metrics mid-rollout, cancel on early signs of regression, and force roll forward on rollouts that look healthy. Deployments that previously required manual babysitting during off-peak windows now run unattended.

### Credits

Rolling deployments were built by the Dedicated Inference team. Special thanks to the customers (like [Speechify](https://www.baseten.co/resources/customers/speechify-real-time-text-to-speech/#solution)) who provided feedback throughout the design and rollout process!

If deployment logistics are eating into your engineering time, [get started with rolling deployments](https://docs.baseten.co/deployment/rolling-deployments) or[ reach out](https://www.baseten.co/talk-to-us/) to talk to our engineers.
