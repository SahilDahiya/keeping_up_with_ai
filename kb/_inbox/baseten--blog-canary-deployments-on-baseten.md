---
title: Introducing canary deployments on Baseten
kind: blog
topic: null
subtopic: null
secondary_topics: []
summary: null
triage: null
skip_reason: null
source: baseten
url: https://www.baseten.co/blog/canary-deployments-on-baseten
author: Sid Shanker
published: '2024-10-31'
fetched: '2026-11-12T06:09:20Z'
classifier: null
taxonomy_rev: 2
words: 949
content_sha256: 2583d64cf994e2bb76982c6cd802d297b5141883c3dbd89fe73f03642d8b391d
---

# Introducing canary deployments on Baseten

News
# Introducing canary deployments on Baseten

Our canary deployments feature lets you roll out new model deployments with minimal risk to your end-user experience.


- Authors
- Date
- October 31, 2024

TLDR

Canary deployments on Baseten let you gradually shift traffic to a new deployment over a customizable time window, with seamless rollback if any issues surface. From exporting metrics to modularized compound AI systems or our TensorRT-LLM Engine Builder, canary deployments are the latest in a suite of features designed to help engineers move swiftly from testing to deployment, with more stability and a delightful developer experience.

We’re excited to launch canary deployments, enabling you to gradually shift traffic to new model deployments over custom time windows!

Rolling out new deployments is a fraught process, especially when it comes to complex generative AI models. From the model quality to performing at scale and interacting with other moving parts in your pipeline, there’s always a non-negligible risk that something can break.

Despite the risk of error, you never want the transition from an old deployment to a new one to surface bugs for your users, let alone risk downtime. Complexities get exacerbated at high traffic levels, and if you immediately switch over all your incoming requests, you’ll have added latency as your deployment scales to meet demand.

That’s why canary deployments are considered a best practice for DevOps, MLOps, and software engineering workflows. They enable smoother rollouts by:

- Initially exposing only a small subset of users to your new deployment, which gradually increases over time.
- Allowing seamless one-click fallback to your previous deployment.
- Ensuring that even at peak traffic, your new model deployments scale appropriately.

The result:

- Lower latencies.
- More reliable deployments.
- A smoother developer experience.
- Less risk for your end-users.

Inspired by the proverbial “canary in a coal mine,” canary deployments let you detect potential issues with a new deployment early on, helping constrain any impact on your users.

In practice, canary deployments work like this:

- Your new (“canary”) deployment is built and ready to handle incoming requests.
- A small percentage of your incoming traffic is directed to your canary deployment.
- You monitor its performance; if issues arise, you can cancel it, and incoming traffic will revert to your old one.
- If no issues arise, traffic gradually increases until your new deployment gets 100% of incoming requests.

This setup minimizes risk to your end-user experience by letting you catch bugs early on, and address any issues before shifting all your traffic over.

Rime’s state-of-the-art p99 latency and 100% uptime is driven by our shared laser focus on fundamentals, and we’re excited to push the frontier even further with Baseten.


Building a delightful developer experience is one of our core values. [We know how critical it is that production systems are low-latency with high uptime](https://www.baseten.co/customers/rime/), and work with our customers running hundreds of model replicas serving millions of requests per day to ensure reliability and performance for their users. From [exporting metrics](https://www.baseten.co/blog/export-model-inference-metrics-to-observability-tools/) to [modularized compound AI systems](https://www.baseten.co/blog/introducing-baseten-chains/) or our [TensorRT-LLM Engine Builder](https://www.baseten.co/blog/automatic-llm-optimization-with-tensorrt-llm-engine-builder/), canary deployments are the latest in a suite of features designed to help engineers move swiftly from testing to deployment.

With other inference providers, you’re stuck with a manual workaround to mitigate the risk of bugs and downtime from your rollouts. On your new deployment, you could set your minimum number of replicas (`min_replica`) to the actual number you’ll need running to meet incoming traffic before switching it over. Once traffic is (hopefully) running smoothly on your new deployment, you could then manually revert your `min_replica` setting to your actual target value.

This technique has a few obvious problems:

- It’s manual.
- It’s a poor developer experience.
- It’s expensive.

Now you'd be footing the bill for two full-fledged deployments, and any issues would still pose more risk to your end users since your traffic switch is all-or-none.

Instead of manually spinning up a parallel instance with a variable number of replicas, canary deployments on Baseten work by gradually shifting traffic to your new deployment over a customizable window. We ramp up traffic in 10 equal steps over the timeframe you specify, giving your new deployment plenty of leeway to scale up accordingly.

You can enable and configure this feature (including the time window) in the UI under "Configure promotion," or via the [REST API](https://docs.baseten.co/api-reference/updates-an-environment-by-name). If bugs surface, just hit “cancel” and traffic will return to your existing deployment.

Rolling out new deployments this way has several benefits:

1. Decreased latency, since replicas can spin up gradually (vs. throwing all your traffic at a deployment starting with one replica).
2. Easier development loops, since you can catch bugs early and avoid downtime by falling back to your previous deployment.
3. A better (and less expensive) developer experience, since you don’t need to manually increase your `min_replica` count to anticipate incoming traffic (or revert it after).
4. A better end-user experience, since users are less likely to encounter issues or downtime when their requests are transferred to your new deployment.

We’ve never had an outage with Baseten. The platform has been rock solid, giving us the confidence to scale quickly without worrying about downtime.


While our teams of forward deployed and model performance engineers are always here to support our users, we believe that engineers should have the autonomy to use powerful ML infra tools as an integral part of their production workflows. Baseten is built with software engineering workflows in mind, and we're dedicated to expanding our tooling, integrations, and partnerships to advance this goal.

[Check out our docs](https://docs.baseten.co/deploy/lifecycle) to learn more, and come [chat with us at KubeCon](https://www.baseten.co/resources/event/baseten-kubecon24/) about what we're cooking!
