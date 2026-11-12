---
title: What I learned from my AI startup’s internal hackathon
kind: blog
topic: null
subtopic: null
secondary_topics: []
summary: null
triage: null
skip_reason: null
source: baseten
url: https://www.baseten.co/blog/what-i-learned-from-my-ai-startups-internal-hackathon
author: Julien Reiman
published: '2023-06-12'
fetched: '2026-11-12T06:11:18Z'
classifier: null
taxonomy_rev: 2
words: 676
content_sha256: 5f16e86caf025a2bc53c2d2cce9b6aabb999151325584ac650b8ed32ce66bee4
---

# What I learned from my AI startup’s internal hackathon

Community
# What I learned from my AI startup’s internal hackathon

See hackathon projects from Baseten for ML infrastructure, inference, user experience, and streaming


- Authors
- Date
- June 12, 2023

Every team at every company has a list of dream projects. Close your eyes and think about it: what’s a feature you’ve always wanted to build—or an initiative you wanted to spearhead—but never had the time? At Baseten, our list is miles long.

That’s why we hosted our first-ever internal hackathon. In May, we set aside an entire day for each Baseten employee to make the thing they always wanted to create. The rules were simple: build something related to Baseten in 8 hours or less.

To sweeten the deal, we offered a free trip to the Baseten team member who made the best project, as decided by popular vote. On the day of the hackathon, we all set off in different directions like kids on a scavenger hunt. Some of us posted up in coffee shops, others stayed in their AirBnB hotel rooms. But most of us sat around a table and worked furiously and quietly.

The projects we developed over those eight hours proved how important it is to meet together in-person, and how a month’s worth of work can be squeezed into a single day when everyone is having fun. What we built that day accelerated the work of Baseten, widening our lead as the best-in-class infra provider for ML teams.

Here’s a rundown of what we developed:

- Ujjwal prototyped a byte range downloader to reduce cold start times for model invocation by speeding up model weights downloads. It usually takes at least a week of work to make something like this, but Ujj used his genius infra skills to make it in a day. We implemented his creation this week, so Baseten users will be able to download their model weights with speeds of up to 1GB/sec from services like S3, OpenAI, CloudFront, and HuggingFace.
- Co-founder [Pankaj](https://twitter.com/defpan) made a set of updates that reduced cold start times for LLaMA to below 30 seconds. Over the next few weeks, Pankaj expanded his work across our model library, bringing our cold start times to under 10 seconds.
- Co-founder [Phil](https://twitter.com/saltyph) redesigned our entire infrastructure roadmap to optimize for multi-cluster deployment and data security. He calls the new system “Beefeater” after the elite soldiers who guard the Tower of London. After rigorously testing and strengthening Beefeater, we deployed it last week. Make an account at [app.baseten.co](https://app.baseten.co/signup/) to see it in action.

- Bola and CEO [Tuhin](https://twitter.com/tuhinone) teamed up to demo a fast UI generator for our application builder.
- [Abu](https://twitter.com/aqaderb) and Justin wowed everyone by building a theoretical “Federated Inference Engine,” which hot-swaps GPUs across multiple servers, which allows builders to run massive models across many GPUs, rather than shelling out thousands of dollars for a big one.

- [Philip](https://twitter.com/philip_kiely) made a [Baseten-LangChain integration](https://python.langchain.com/en/latest/modules/models/llms/integrations/baseten.html) allowing developers to craft applications with LangChain’s modules using LLMs deployed on Baseten.
- [Matt](https://twitter.com/MattDotHow) created some fantastic Looker dashboards to give us insight into how devs are deploying and scaling their models.
- I ([Julien](https://twitter.com/JulienTech)) redesigned our documentation. As a novice engineer, my goal was to make our platform accessible to everyone, even beginners. With the help of our wizard technical writer Philip, we edited and recently published the changes. [Check out our new docs today](https://docs.baseten.co/) and give us any feedback!

- When [Samiksha](https://twitter.com/samshineeee) demoed her creation, audible gasps were heard across the room. Samiksha made “I Stream 4 Ice Cream.” It’s a feature incorporated into our model management workstream that allows builders to see all models stream their progress as they run inference. So needed by so many ML engineers—and now Baseten has it.

With the success of the hackathon, we have many more on the way: some internal, some wide open for all engineers to build with Baseten. We’d love to show you what we’re crafting every step of the way, so [follow us on Twitter](https://twitter.com/basetenco) for updates on all our events and advancements.
