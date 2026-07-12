---
title: Machine Learning Tools Landscape v2 (+84 new tools)
topic: industry
subtopic: trends
secondary_topics:
- infra-platform/deployment
summary: Updates the MLOps tooling landscape to 284 tools and identifies deployment,
  monitoring, serving hardware, and regional infrastructure divergence as major production-ML
  trends.
source: chip-huyen
url: https://huyenchip.com/2020/12/30/mlops-v2.html
author: Chip Huyen
published: '2020-12-30'
fetched: '2026-07-11T05:08:25Z'
classifier: codex
taxonomy_rev: 1
words: 950
content_sha256: 38447b261b34cba3f1a43ce59789ad1305f60aae44eb79c0854f2f22af61b81e
---

# Machine Learning Tools Landscape v2 (+84 new tools)

# Machine Learning Tools Landscape v2 (+84 new tools)

Last June, I published the post [What I learned from looking at 200 machine learning tools](https://huyenchip.com/2020/06/22/mlops.html). The post got some attention and I got a lot of messages from people telling me about new tools. I updated the old list to now include 284 tools. I’ll keep on updating the list as I find out about new tools. Any lead would be much appreciated!

While looking for these MLOps tools, I discovered some interesting points about the MLOps landscape:

- Increasing focus on deployment
- The Bay Area is still the epicenter of machine learning, but not the only hub
- MLOps infrastructures in the US and China are diverging
- More interests in machine learning production from academia

Click here to see [the list in Google Sheets](https://docs.google.com/spreadsheets/d/1i8BzE4puGQ3dmQueu4LQCcwaqrulgK1Vb-xeFwhy6gY/edit?usp=sharing). To see a fancy interactive chart, scroll to the end of this blog post.

## 1. Increasing focus on deployment

In the list of 284 MLOps tools, there are 180 startups. Out of these 180 startups, 65 raised money in 2020. Most startups that raised money in 2020 are in still in the Data pipeline category, with an increasing number of in all-in-one (end-to-end platforms), hardware, and serving.

Here are further breakdowns on the most popular categories:

- Accelerators (building chips optimized for machine learning algorithms, often with a focus on data centers)
- AI Apps platform (end-to-end platforms for developing & deploying AI applications)
- Data management
- Monitoring
- Edge devices (building chips optimized for inference on consumer devices with low power)

![MLOps startups that raised money in 2020](https://huyenchip.com/assets/pics/mlops_v2/1_mlops_cat.png)

![MLOps startups that raised money in 2020](https://huyenchip.com/assets/pics/mlops_v2/2_mlops_focus.png)

## 2. The Bay Area is still the epicenter of machine learning, but not the only hub

Among 65 MLOps startups that raised money in 2020, more than half of them are outside the Bay Area, with growing hubs in Boston, New York City, Israel.

10 notable MLOps startups outside the Bay Area that raised money in 2020:

- [DataRobot](https://www.datarobot.com/)- Boston - $320M: enterprise AI apps platform
- [Graphcore](https://www.graphcore.ai/)- UK - $250M: chips for machine learning
- [Dataiku](https://www.dataiku.com/)- NYC - $100M: enterprise AI apps platform
- [Hailo](https://hailo.ai/)- Israel - $60M: chips for machine learning
- [DefinedCrowd](https://www.definedcrowd.com/)- Seattle - $50.5M: training data generation
- [Zilliz](https://zilliz.com/)- China - $43M: open-source software for processing unstructured data
- [Starburst Data](https://www.starburstdata.com/)- Boston- $42M: distributed SQL query engine
- [Anodot](https://www.anodot.com/)- Israel - $35M: enterprise data monitoring
- [Materialize](https://materialize.com/)- Boston - $32M: stream processing
- [Rasa](https://rasa.com/)- Germany - $26M: API for conversational AI

This is an encouraging signals for people who want to build tools for machine learning production but don’t want to: succumb to the Bay Area monoculture and astronomical cost of living deal with American fickle immgration policies.

It’s cheaper to find good engineers outside the Bay, and it might also be easier since you don’t have to compete with hundreds of tech giants and other startups for top engineers.

![MLOps startups that raised money in 2020](https://huyenchip.com/assets/pics/mlops_v2/3_mlops_location.png)

## 3. MLOps infrastructures in the US and China are diverging

One term I saw while reading China-focused AI newsletters is “localization” (国产化替代) – replace foreign technologies with Chinese alternatives. Chinese companies use tools similar to what American companies use, but not quite the same.

In the US, companies rely on Google Cloud, Amazon AWS for hosting services. In China, companies rely on [Tencent Cloud, Alibaba Cloud](https://www.sans.org/blog/doing-cloud-in-china/). In the West, the Cloud Native Computing Foundation (CNCF) acts as the caretaker for container technologies including Kubernetes. In China, they have TARS Foundation for open-source microservices projects.

One reason for a separate foundation is language barriers. Chinese engineers might fork a popular repo, modify it for their use, then either can’t merge back because they don’t know how to communicate with the maintainers in English, or don’t want to merge back because it’d take a lot of time.

The list includes a few Chinese tooling startups, but it missed out so many because Chinese startups don’t get enough attention from the Western media. Many of them have their websites and documents only in Mandarin, which makes it hard to find information about them.

## 4. More interests in machine learning production from academia

The AI research scene seemed to have calmed down in 2020 – Google freezed hiring for AI researchers, [Uber laid off their entire AI research team](https://analyticsindiamag.com/uber-ai-labs-layoffs/), [Element AI was sold for cheap](https://twitter.com/chipro/status/1341075433173860352).

However, the ML production scene is still growing with more and more tools on the market. There’s also a growing interest in ML production even from academia. Here are some of the venues for those who want to learn about ML production in academia:
**Challenges in Deploying and Monitoring Machine Learning Systems** workshop at ICML[MLSys Seminars at Stanford](https://mlsys.stanford.edu/)
[Conference on Machine Learning and Systems](https://mlsys.org/)

The seemingly less steep curve from 2019 to 2020 is because a lot of companies that started this year are still in stealth.

![MLOps startups that raised money in 2020](https://huyenchip.com/assets/pics/mlops_v2/4_mlops_total.png)

Click on a category to see the tools in that category. Click on the white space in the center to go up a level.

**Acknowledgment**: Thanks [Luke Metz](https://twitter.com/Luke_Metz) for being a faithful first reader.

I want to devote a lot of my time to learning. I’m hoping to find a group of people with similar interests and learn together. Here are some of the topics that I want to learn:

- How to bring machine learning to browsers
- Online predictions and online learning for machine learning
- MLOps in general

If you want to learn any of the above topics, join our [Discord chat](https://discord.gg/Mw77HPrgjF). We’ll be sharing learning resources and strategies. We might even host learning sessions and discussions if there’s interest. Serious learners only!
