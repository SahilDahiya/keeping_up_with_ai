---
title: Securing the open frontier with NVIDIA OpenShell and Blaxel sandboxes
kind: blog
topic: null
subtopic: null
secondary_topics: []
summary: null
triage: null
skip_reason: null
source: baseten
url: https://www.baseten.co/blog/announcing-carbon/
author: Nicolas Lecomte
published: '2026-09-28'
fetched: '2026-09-29T06:10:46Z'
classifier: null
taxonomy_rev: 2
words: 584
content_sha256: ed75eda114d352318756d1828ae275693f1f7022b8187b8ee9eda3e43f332ef5
---

# Securing the open frontier with NVIDIA OpenShell and Blaxel sandboxes

![Baseten partners on the NVIDIA Open Agent Safety Platform](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1790618240-nvidia_x.png%3Fauto%3Dformat%26fit%3Dcrop%26h%3D630%26w%3D1200&w=3840&q=100)

Agent safety has become top of mind in recent weeks, specifically focused on where failure modes lie and how to address them. We’re thrilled to support NVIDIA’s Agent Safety Platform, which addresses safety across three critical areas: the application layer, runtime, and infrastructure.

As a launch partner for [NVIDIA OpenShell](https://build.nvidia.com/openshell) and part of the [Open Secure AI Alliance](https://blogs.nvidia.com/blog/open-secure-ai-alliance/), we are working together to further the open, secure frontier, including the stack powering agents in production. 

## Building open safety controls for agentic infrastructure

At Baseten, we believe openness is an advantage for AI safety. We continue to invest in building safety controls for the open frontier across inference, training, and sandboxes.

[Base Labs](https://labs.baseten.co/) develops and publishes methods for training and monitoring open models, and Baseten builds that work into our deployment infrastructure at runtime. We [recently launched our safety infrastructure effort](https://x.com/baselabs/status/2100286099121705396) with Base Labs, Hugging Face, and Goodfire AI in this vein; joining the Open Secure AI Alliance extends that commitment.

Monitoring only helps if its signals connect to permissions, isolation, and checks before an agent executes code. Blaxel's sandboxes and networking layer are where those controls live for agents running on Baseten. Blaxel also supports OpenShell, NVIDIA’s open-source runtime that enforces policy at the kernel level; OpenShell is agnostic to the compute the agent runs on.

## Why Blaxel: secure sandboxes for agents

We [acquired Blaxel](https://www.baseten.co/blog/blaxel-is-joining-baseten-to-build-the-future-of-agentic-cloud/) to build the cloud for the next trillion agents. While Baseten builds the infrastructure to train and serve models, Blaxel is the execution layer agents need to act: microVM sandboxes, persistent storage, and networking with tight access controls.

Today we're introducing a private preview of Carbon, Blaxel's fourth infrastructure generation built to support trillions of agents in production. Coming to Baseten soon, Carbon will provide the backbone for sandboxes and broader execution infrastructure for agentic workflows on the Baseten platform.

## Introducing Carbon: Blaxel’s fourth-generation infrastructure

When Astra-grade agents are writing and running their own code, hardware-level isolation becomes a necessity (we've written before about [why containers break down once agents start generating their own code](https://blaxel.ai/blog/container-escape)). Carbon still runs on microVMs, and every Carbon sandbox gets its own dedicated IPv6 address. Somewhere between billions and trillions of agents will be running in parallel this decade; IPv6 is the only addressing scheme with room to spare.

Carbon is much more flexible and configurable than any previous infrastructure generation we built. Beyond IPv6, the main features shipping with Carbon are kernel capabilities for agents and runtime enforcement, manual snapshotting, forking, and a direct path from snapshot to production within milliseconds.

Because Carbon brings additional kernel capabilities to the sandbox, it can run heavier runtime software directly inside it. That opens the door to a new generation of tooling built specifically for frontier agentic AI, including NVIDIA's newly announced OpenShell. We built a [ready-to-use template](https://github.com/blaxel-ai/openshell-blaxel) so you can boot a Carbon sandbox with OpenShell already installed.

If OpenShell flags an agent mid-task and quarantines it, Carbon's snapshots mean you roll back to the last known-good state instantly instead of losing the run.

## Get early access to Carbon

Carbon is currently in private preview and rolling out progressively by region and workspace. The full snapshot and fork API reference is available in the [Blaxel docs](https://docs.blaxel.ai/Infrastructure/Gens#mark-3-1).

Upcoming posts will go deeper into security inside and outside Carbon sandboxes, [forking and snapshotting](https://docs.blaxel.ai/Sandboxes/Fork) workflows, and the [application model](https://docs.blaxel.ai/Applications/Overview) that Carbon makes possible. If you're already on 3.0 and want access to Carbon, [reach out](https://blaxel.ai/contact)!
