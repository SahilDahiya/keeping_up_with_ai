---
title: Serving four million Riffusion requests in two days
kind: blog
topic: infra-platform
subtopic: deployment
secondary_topics:
- product-engineering/case-studies
summary: After Riffusion (a fine-tuned Stable Diffusion music model) got scooped onto
  Hacker News early, Baseten handled 4 million requests peaking at 34 req/s on A10G
  replicas by scaling to 50 replicas and caching common query responses in Postgres
  to cut redundant model invocations.
triage: null
skip_reason: null
source: baseten
url: https://www.baseten.co/blog/serving-four-million-riffusion-requests-in-two-days
author: Phil Howes
published: '2022-12-21'
fetched: '2026-11-12T06:13:06Z'
classifier: claude
taxonomy_rev: 2
words: 775
content_sha256: df40d556f884271b60c75e44dc4228c83148501e702d388726722f79b23e8182
---

# Serving four million Riffusion requests in two days

AI engineering
# Serving four million Riffusion requests in two days

Riffusion is a fine-tuned version of Stable Diffusion. Baseten served Riffusion over four million times in a couple of days, serving top-of-hacker-news traffic.


- Authors
- Date
- December 21, 2022

Recent advances in generative AI have delivered foundational models across a spectrum of tasks: GPT for text generation, Whisper for transcription, Stable Diffusion for image creation. So far, we don’t have a foundational model for generating music. But [Seth Forsgren](https://sethforsgren.com/) and [Hayk Martiros](https://haykmartiros.com/) had an idea: maybe we don’t need a foundational model for music just to write a short song. Instead, they created [Riffusion](https://www.riffusion.com/), which uses a tuned version of Stable Diffusion to generate audio spectrograms and interpret those images as music. Seth and Hayk partnered with us at Baseten to host and serve the project’s [underlying model](https://www.riffusion.com/about).

The reception proved even more enthusiastic than anticipated: Riffusion climbed to the top of Hacker News and circumnavigated Twitter. This intense interest led to lots of traffic. Riffusion handled over four million song requests in a couple of days. Serving generative models at this kind of scale presented immediate and unique challenges. Here’s how we solved them.

While we weren’t expecting this kind of popularity, we anticipated that Riffusion could receive some material traffic, and performed a load test on the system before launch. In the test, we sent the Riffusion backend enough traffic for it to scale up to the default scaling limits and ensured that there were no errors or unusual behavior. With everything working smoothly, the launch timeline was set.

Plot twist! Riffusion got scooped: it was posted to Hacker News several hours before its creators intended to post it themselves and thus several hours before our engineers were planning to scale up resources. Fortunately, the backend was configured with high default scaling parameters, which handled some of the first wave of traffic, but as users poured in, Riffusion hit the limits of normal usage, so latency and error rates reared their ugly heads.

Autoscaling infrastructure has its limits, and for good reason. It’s expensive to provision a ton of compute resources, and at a certain point adding more servers causes as many problems as it fixes. So our infrastructure was ready to scale to a certain level, which handled the start of the unexpected torrent of traffic, but we quickly reached the point where unique solutions were needed.

What kind of traffic does the [twelfth-most-upvoted post](https://hn.algolia.com/?dateRange=pastYear&page=0&prefix=false&query=&sort=byPopularity&type=story) of the year on Hacker News generate? Over the course of a couple of days, Riffusion’s backend processed a little over 4 million song requests, peaking around 34 requests per second.

With a model that runs on an Nvidia A10G receiving that much traffic, we needed to reinforce our ordinary autoscaling capabilities with flexible solutions for our infrastructure to rise to this unique challenge.

Our main constraint: the model required a GPU fast enough to run it in under five seconds (including all the typical HTTP overhead: client-server latency, database calls, etc). The instances we were using were more than capable of running the model, but you can only scale to so many replicas before managing replicas becomes its own problem. At peak we had 50 replicas, each with an Nvidia A10G, churning out songs. Replicas and load balancing are essential tools, but smart scaling is about more than just throwing extra compute at the problem.

The biggest win came from caching model responses. It turns out, some queries are pretty common, like “rock and roll electric guitar solo.” To reduce the number of model invocations needed, we stored the response to queries in a Postgres table and checked requests against that table, returning the stored response if it was a request we had seen before.

In all, serving Riffusion through its high-traffic days cost about a thousand dollars per day. That’s a lot of cash for a hobby project, but it’s not all that outrageous for a GPU-intensive model receiving that many invocations.

Much of the savings came from using a mixture of spot and on-demand instances to scale up and down with traffic. A naive solution would be less flexible and more expensive–this is where it pays to offload your MLOps so you can focus on model development.

The other two biggest factors in cost savings were caching requests to avoid unnecessary invocations and accepting somewhat higher latency and error rates than business-critical processes would allow as an intentional trade-off to keep spend reasonable on a demo.

If you’re working on an ML-powered app like Riffusion and need to serve your models at scale, [sign up for Baseten](https://baseten.co/?utm_source=riffusion_blog) and deploy your model!
