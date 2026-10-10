---
title: 'Project Beacon: Bringing safety signals to open models at scale'
kind: blog
topic: product-engineering
subtopic: security
secondary_topics:
- evals-observability/monitoring
summary: Baseten and Goodfire's Project Beacon reads model activations during generation
  to detect prompt injection, policy violations, and data exposure in real time; a
  monitor cascade runs activation and text checks in parallel with generation and
  escalates to a frontier model only when the two disagree, applying per-customer
  policies to approve, refuse, fall back, or log.
triage: null
skip_reason: null
source: baseten
url: https://www.baseten.co/blog/safe-open-models-baseten-goodfire/
author: Sai Maddali
published: '2026-10-09'
fetched: '2026-10-10T06:09:54Z'
classifier: claude
taxonomy_rev: 2
words: 845
content_sha256: 16003e71965ef7372a72c7f4254d0265bb4c9c4e815b8c8b7219c5d5a61792f4
---

# Project Beacon: Bringing safety signals to open models at scale

### Published

![Baseten and Goodfire AI partner to bring safety controls to open models.](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1790958131-partner-background-no-logos.png%3Fauto%3Dformat%26fit%3Dcrop%26h%3D630%26w%3D1200&w=3840&q=100)

The breadth and depth of what AI touches across an organization is growing. Models and agents read internal documents, call tools, push to production systems, and run multi-step workflows autonomously. At the same time, new frontier models are released weekly (sometimes daily), with most teams regularly swapping the old for the new and running different constellations of models side-by-side.

Meanwhile, reports of models taking unexpected or harmful actions have become a regular feature of the news cycle. For enterprises, that risk has become one of the main blockers to AI adoption. Teams need to know when their workflows enter risky territory and have a way to act in response.

We’ve already taken steps to build safety into the Baseten Platform, including [launching Base Labs](https://x.com/baselabs/status/2095561531400540623) to conduct open safety research, partnering with Hugging Face and Goodfire AI to [launch our safety infrastructure](https://x.com/baselabs/status/2100286099121705396), and [partnering with NVIDIA](https://www.baseten.co/blog/announcing-carbon/) on the Open Agent Safety Platform. Today, we’re announcing Project Beacon in partnership with Goodfire AI to bring proactive, inline safety controls to model inference.

## **The risks we’re building for**

Project Beacon will enable us to build toward a world where safety isn't a static feature, or something that happens post hoc. By reading a model's internal activations during generation, you can define proactive policies that detect an unsafe event as it's happening and act on it before the output reaches a user or a tool.

Safety risks at the inference layer take different forms:

- **Prompt injection:** instructions in a document or tool result try to redirect an agent.
- **Actions outside policy:** an agent proposes a change its user or organization did not authorize.
- **Sensitive data exposure:** customer or company information appears where it should not.
- **Cyber misuse:** a model’s behavior raises concerns in a security-sensitive workflow.

Each calls for a mixture of monitoring, text checks, tool controls, and review. While Goodfire develops monitors for specific behaviors on supported models, Baseten connects their signals to the systems that decide how an application responds. By bringing [activation-based probes](https://www.goodfire.com/blog/probe-monitors-101) into Baseten’s inference path, we can open up product experiences that aren't possible otherwise.

![Architecture diagram: activation and text monitors classify each request, and a frontier model weighs in only when the two disagree. Per-customer policies are applied to decide whether to request approval, refuse, fall back, or log the event for admins. Monitoring runs in parallel with generation and does not block response generation.](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1790958306-goodfire-monitor-cascade-baseten-brand-2.png%3Fauto%3Dformat%26w%3D1200&w=3840&q=75) Architecture diagram: activation and text monitors classify each request, and a frontier model weighs in only when the two disagree. Per-customer policies are applied to decide whether to request approval, refuse, fall back, or log the event for admins. Monitoring runs in parallel with generation and does not block response generation.

## **What this means for Baseten customers**

We’re building toward an out-of-the-box safety experience: a baseline of supported monitors and checks, policies for different workloads, alerts, and a record of what was flagged and how it was handled. Teams will be able to apply their own standards per model with a safety stack that’s built in.

### **For enterprises**

Security and AI platform teams see open frontier models they want to deploy, but need guardrails around prompt injection, behavior outside company policy, sensitive data exposure, and unusual usage. As inference spend grows across teams, separate filters and review processes for every application become hard to govern.

We'll provide a safety baseline that can be applied centrally, adjustable policies by workload, and a clear record of what was flagged and how it was handled.

### **For developers**

We’re working toward safety events and controls delivered through the same APIs and developer tools used for inference on Baseten, so builders can easily act on those signals and create safer AI experiences.

Consider a payment-dispute agent that reads merchant messages and account records before proposing a refund. Untrusted content might redirect it; a wrong action could expose data or move money. At scale, reviewing every step with another large model adds cost and latency.

Developers need timely signals they can use to choose the right response—continue, investigate, request approval, or fall back—without giving up control of their users’ experience. Safety becomes part of the product experience as agents run longer and take more actions.

## **What comes next**

Over the next several months, we plan to release safety capabilities tightly integrated with Baseten inference, starting with selected models and monitored behaviors and expanding into enterprise controls and developer-facing experiences.

We’re committed to advancing the state of the art in safety as the ecosystem's needs grow. This includes inference, training, and sandboxes—and whatever comes next. Securing AI gets harder as you scale; each new model brings its own risks, and agents broaden the surface for failure. Project Beacon exists to enforce consistent safety controls across any model, workload, and level of access you run.

We’ll bring the capabilities produced by Project Beacon to market with a small number of early partners. If you're interested, [reach out](https://www.baseten.co/talk-to-us/) to discuss early access and partnership.
