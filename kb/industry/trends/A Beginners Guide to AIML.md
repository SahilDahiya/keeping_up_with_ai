---
title: A Beginners Guide to AI/ML
topic: industry
subtopic: trends
secondary_topics: []
summary: Introductory overview of AI and machine learning concepts for non-specialists,
  covering the basic vocabulary and why ML systems need operational support.
source: arize
url: https://arize.com/blog/a-beginners-guide-to-ml/
author: Krystal Kirkland
published: '2021-07-23'
fetched: '2026-07-11T04:43:13Z'
classifier: codex
taxonomy_rev: 1
words: 968
content_sha256: 21d7d2de6fd89ccd981980c89fabca183449b500887b979cb873aad253072ec9
---

# A Beginners Guide to AI/ML

![Server room, datacenter and cloud storage concept. Modern isometric illustration.](https://arize.com/wp-content/uploads/2021/07/AdobeStock_330677832-1021x560.jpeg)

              # A Beginners Guide to AI/ML

As I near my one-year mark in the artificial intelligence and machine learning industry, the once daunting and complex space has indeed remained as such – just with a little more clarity amongst the complexity. AI isn’t a straightforward field to enter, and given its newness, it generally lacks an incredible amount of documentation and tried-and-true best practices. Luckily, there’s an endless wealth of knowledge to gain in this space.

Here’s a quick glimpse as told from the perspective of a non-technical person living in a very technical world:

**1. AI Is Not ML **

Artificial intelligence, as told by Alex Garland’s *Ex Machina* or Spike Jonze’s *Her*, while entertaining, is not the reality of the situation – *at all*. AI simply refers to the concept of, well, artificial intelligence, where machines (i.e., computers) can carry out tasks that generally require some level of human intelligence. Meanwhile, machine learning is an application of AI, where machines learn from data that is then transformed into action, like deciphering your loan worthiness based on your previous spending history.

Generally speaking, it’s reasonable to think that as the more data is gathered, the more models are reinforced, and the more likely AI becomes sentient. But that is simply not the case. In fact, machine learning models are extremely fragile in the real world. Anomalous data (for example, all of 2020) can break models quicker than you can go out to buy toilet paper in 2021.

The machine learning infrastructure space is exceptionally vast, seemingly endless, and very convoluted. Each step in the machine learning lifecycle outlined [here ](https://arize.com/what-is-ml-observability/)requires a different set of tools to ensure success. While you could dive deep and evaluate all the options, as diagramed [in this series](https://arize.com/ml-infrastructure-tools-for-data-preparation/), simply put, there are only [3 ML Tools You Need](https://arize.com/the-only-3-ml-tools-you-need/) to cover your bases.

**2. ML Engineers Are Not Data Scientists**

As the AI/ML space booms, different roles and how they interact become incredibly ambiguous. Buzzwords such as machine learning, artificial intelligence, and data science lose a sense of meaning as organizations stammer to revive technical relevancy in a digital-first era. As a result, there is typically a lot of confusion about delineating roles within organizations and amongst different companies.

Overall, Data Scientists are in charge of overseeing offline research environments, preparing training sets, and focusing on defining the algorithm (the math and logic required to complete a task) itself. Meanwhile, ML Engineers focus on programming models to get them from research to production (aka the “real” world). Once a model is in production, ML Engineers are tasked with monitoring how models interact with real-world data.

Notably, the ML Engineer is faced with the challenges of post-production model performance issues, where there is very little telemetry regarding model performance, drift, data quality, and explainability. While the ML Engineer is expected to put models into production for a multitude of goals, there is currently limited to no understanding of how these models interact with the real world until it’s too late.

Learn more about [The Rise of the ML Engineer ](https://arize.com/the-rise-of-the-ml-engineer/)to better understand the ins and outs of  ML Engineering. In addition, the [Arize AI ML Observability Un/Summit](https://arize.com/resource/un-summit-2020-a-tech-showdown-ml-engineering-v-data-science/) dives deeper into the Data Scientist v. ML Engineer battle for clarity.

**3. Monitoring Is Not Observability **

While ML Engineers can deploy some checks to understand their models better, surfacing issues is [not all there is to it](https://arize.com/beyond-monitoring-the-rise-of-observability/). Monitoring, the act of detecting a problem at hand, is the first step to improving model performance in the long run. But it’s only the tip of the iceberg.

Don’t get me wrong, [monitoring your models in production ](https://arize.com/the-playbook-to-monitor-your-models-performance-in-production/)is extremely important, but it’s not enough to simply know what’s wrong. ML Observability digs deeper to not just surface issues but helps you uncover and understand *why* the issue emerged in the first place.  It enables introspection into your ML system to continuously improve your models once they are in production. [ML Observability](https://arize.com/what-is-ml-observability/) can create a feedback loop between data scientists and the research environment and ML Engineers and production environments.

Through introspection into your models’ performance over time, ML observability can help your teams identify gaps in training data, surface slices of examples where your model is underperforming, compare model performances side by side, validate models, and identify issues in production.

**4. Responsible AI Is Not A One-And-Done Project**

There is a multitude of examples that represent bias in ML models, from racial bias in facial recognition software to gender bias in recruiting tooling. Having biased models comes with the territory of using data produced by the real world.

While many companies and organizations want to deploy initiatives to tackle these problems, responsible AI, fairness, and bias mitigation don’t have a neatly packaged solution. It is an ever-evolving [practice](https://arize.com/the-chronicles-of-ai-ethics-the-man-the-machine-and-the-black-box/) that should be front of mind whenever data is gathered, a new training set comes out, a new model is deployed, or a new team [member is hired](https://arize.com/unleashing-the-power-of-a-diverse-team-to-build-more-ethical-ai-technologies/). The definition of ‘ethical’ and ‘fair’  changes depending on the organization you’re in, the product you’re building, who you work with, [what information you work with](https://arize.com/if-data-is-the-new-oil-whats-happening-to-its-precious-new-source/), and much more. Responsible AI is not a stagnant goal but an ever-morphing mindset that necessitates intentional action, foresight, and patience.

It’s been a challenging but rewarding year for me as I dip my feet in the AI/ML industry. While research environments in the field are thoroughly studied, most ML infrastructure is still new to everyone. There is endless opportunity to learn and grow within the space and a lot of responsibility to do it right.

P.S. If you’re interested in joining an all-star team in machine learning or learning more about ML monitoring and observability, check out our open positions [here](https://arize.com/careers/) and resources [here](https://arize.com/blog/)!
