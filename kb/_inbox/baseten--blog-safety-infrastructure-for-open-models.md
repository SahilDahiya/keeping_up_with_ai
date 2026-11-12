---
title: Safety Infrastructure for Open Models
kind: blog
topic: null
subtopic: null
secondary_topics: []
summary: null
triage: null
skip_reason: null
source: baseten
url: https://www.baseten.co/blog/safety-infrastructure-for-open-models
author: null
published: '2026-01-01'
fetched: '2026-11-12T06:15:32Z'
classifier: null
taxonomy_rev: 2
words: 512
content_sha256: 80ec32d00f2742259cdbcf4f4281cba40a5c3fd5d2de3f2071de4062509ffa93
---

# Safety Infrastructure for Open Models

While safety research has been prominent in the AI field for some time, it has become a forefront topic in mainstream discussion this past week. We're hearing much more about these concerns from our friends and families outside the field, largely due to a very public Anthropic safety researcher exit, raising eyes on Anthropic's security report, the OpenAI/Hugging Face security incident, and various other security and safety concerns. We take these safety issues very seriously, and we are glad to see that safety has gone broadly and globally mainstream.

Open-source models occupy a lot of this safety discussion, where a lot of past discussion unfortunately confuses “open” with “unmonitored”. On the contrary, an open model provides much more tooling and visibility for safety research from a broader audience, which has led to many of the safety and security techniques we use today. Linux is a great example of this: open-source and secure deployment are not only compatible but heavily intertwined, as a properly secure system needs an extensive feedback loop of finding and fixing vulnerabilities. As open-source models catch up in performance to frontier models, providers like ourselves and the community at large have a great opportunity to establish a common practice for effective safety and security research.

We are at a crucial point for the open-source model ecosystem: Safety must be built into the model itself and provided by those who serve it. If we can properly set the safety and security standard and techniques for all future open-source model deployments, we can help make the future of AI one that everyone can benefit from, without fear of misuse or security vulnerabilities.

To this end, we are excited to announce our effort at Baseten and Base Labs to build safety evaluation and monitoring infrastructure for the open models that we serve. We plan to connect safety research directly to our systems that train and serve models. This lets us test how changes to training affect behavior, whether monitors detect failures, and whether deployment controls catch and contain failures.

- Training: teach models to follow explicit policies, recognize their limits and ask for help when a task cannot be completed legitimately.
- Monitoring and intervention: study inputs, outputs, tool use and internal model states, then connect useful signals to permissions, isolation and checks before execution.
- Learning from failures: investigate what went wrong, improve the training or controls, and test whether the change works without obstructing legitimate tasks.

Base Labs will develop and publish methods for training and monitoring these models. Baseten will integrate that work into its deployment infrastructure, live at runtime, and offer this work as a managed service, with published methods and evidence that customers and outside evaluators can test for themselves.

We hope this will set a standard for all open-source providers to raise the bar for the safety and security of deployed models, and invite everyone in the open-source model community to contribute to such safety evaluation protocols. We hope that, together, we can build an ecosystem of open models that are safe and accessible to all.
