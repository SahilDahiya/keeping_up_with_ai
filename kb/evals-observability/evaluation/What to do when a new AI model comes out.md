---
title: What to do when a new AI model comes out
topic: evals-observability
subtopic: evaluation
secondary_topics:
- models/benchmarks
summary: 'Playbook for responding when a new AI model ships: run targeted evals, compare
  cost and quality, inspect regressions, and decide rollout strategy.'
source: braintrust
url: https://www.braintrust.dev/blog/new-model
author: Braintrust Team
published: '2024-12-04'
fetched: '2026-07-11T04:33:12Z'
classifier: codex
taxonomy_rev: 1
words: 432
content_sha256: e65f0be31f43d2017c2f27c426774241ac586c7cf97db80f626ef4896941046c
---

# What to do when a new AI model comes out

4 December 2024Ornella Altunyan3 min

Every week, it seems like another AI provider releases a state-of-the-art model. These announcements come with impressive benchmarks, but those benchmarks rarely reflect real-world use cases. So, how do you know if the new model is worth deploying in your app?

To gauge if a particular model will improve your application, it’s first worth understanding how well your app is currently performing. In AI applications, performance is measured using evaluations that consider the accuracy or quality of the LLM outputs. Setting up a baseline is simple— the easiest way is to run an eval with a set of data, the AI function you want to test, and a scoring function.

After you [run your first evaluation](https://www.braintrust.dev/docs/start/eval-sdk), you can adapt it to run against more models.

The best way to evaluate a new AI model is by testing it against the actual data your app handles in production. Generic benchmarks might give a sense of performance, but only your data can reveal how well a model works in your product. To do this in Braintrust, start by pulling [real logs from your app](https://www.braintrust.dev/docs/instrument) and organizing them into a dataset. Consider choosing a set of logs that are underperforming to see if the new model makes an impact on the scores.

Then, use the dataset to run an evaluation using the new model and directly compare the performance (and other factors like cost, tokens, and more) against the one you’re already using.

![Comparing evals](https://www.braintrust.dev/blog/img/eval-comparison.png)


Importantly, you should also closely monitor your overall scores to ensure you are not regressing in any areas. To do so, you can use the **Group by** menu in the **Experiments** pane to see the results of your evals sorted by model.

![Group by model](https://www.braintrust.dev/blog/img/group-by-model.png)


You can also run further evaluations on a more extensive set of logs and check out the eval summaries.

If the results show that the new model outperforms your current one, update it in production. If you make your LLM calls in production using the [AI proxy](https://www.braintrust.dev/docs/deploy/ai-proxy), you can do this with just a one-line code change.

After shipping the new model in production, you can keep tabs on its performance on the **Monitor** page. To focus on your model change, select **Group by model** and tighten the timeline to when you made the changes.

![Monitor page](https://www.braintrust.dev/blog/img/monitor.png)


When the next AI model comes out, you won’t need to guess if it’s better for your app. By testing it with your actual data and swapping models quickly, you’ll know for sure, and be able to make a confident decision every time.
