---
title: 'A Q&A From Inference To Training: The Inside Story Of Baseten’s Newest Product'
kind: blog
topic: null
subtopic: null
secondary_topics: []
summary: null
triage: null
skip_reason: null
source: baseten
url: https://www.baseten.co/blog/a-q-a-from-inference-to-training-the-inside-story-of-baseten-s-newest-product
author: Madison Kanna
published: '2026-01-07'
fetched: '2026-11-12T06:10:48Z'
classifier: null
taxonomy_rev: 2
words: 1594
content_sha256: e7cf3da443a98021a73697a1e81842313fcc9dccd7305b854f1aaef9339d8f50
---

# A Q&A From Inference To Training: The Inside Story Of Baseten’s Newest Product

Product
# A Q&A From Inference To Training: The Inside Story Of Baseten’s Newest Product

Baseten launched a new training infrastructure that lets teams bring their existing code and run it on scalable compute with no heavy abstractions.


- Authors
- Date
- January 7, 2026

TLDR

We launched a new training infrastructure that lets teams bring their existing code and run it on scalable compute with no heavy abstractions. It’s built for flexibility, custom models, audio models, multi-node jobs rather than point-and-click constraints. The product ties directly into Baseten’s inference stack, making it easy to go from training to deployment seamlessly. Early customers like OpenEvidence and Oxen have already used it to speed up inference, distill models, and even build full platforms on top of Baseten.

We just launched training at Baseten. I sat down with one of the engineers, Raymond, who built it to learn about the product, early customers, and what makes it different.

I joined in June 2024, so almost a year and a half ago. What really stood out to me was how transparent the founders were about iterating on the product and learning from the market. They talked about how we had "earned the opportunity" to do certain things with our customers. Like how we're an inference company, but we've earned the trust to do training with them. Looking back, it's kind of crazy that a year later I was in the thick of building that training product.

I'd love to start with the customer journey. A handful of our customers kept asking us, "When are you going to build training?" We had done tons of customer interviews and research, and when I joined the project, they handed me these videos and said, "Watch these and figure out what to build."

What we learned was that if you're not an infrastructure company, it's really hard to get the resources to train world-class, open-source models. We heard stories of customers being up at 1 AM clicking the "add machine" button on DWS, waiting and waiting. They just wanted to train on Baseten.

A lot of these customers already had training scripts and pipelines that worked. They had ML engineers and researchers who had worked really hard to get something functional. So we asked ourselves: how can we just help them get to Baseten?

It’s essentially a training infrastructure product. We started with the premise: take all your working code, no frills. Bring whatever image you want, whatever repo you run, and come run it on Baseten. We'll make that really easy.

We provide storage primitives that help you iterate quickly with persistent storage, so you don't have to re-download your model and datasets each time. We give you a pipeline for moving your checkpoints into inference so that deploys and evals end to end can be done seamlessly. The goal is to cut out those little 15-30 minute tasks that slow everything down.

When we started building the product this year, we saw a lot of point-and-click solutions in the market. You'd have a dropdown of model options—train Qwen 3 70B, train Llama 3 70B—and you'd bring your data and use their training loop.

**But if you want to do something experimental, something that gives you a competitive edge because you're not doing what everyone else is doing, you might want to come to Baseten.** We built a platform that's flexible enough that people training audio models—like Orpheus or Whisper—love coming to Baseten, because these point-and-click solutions don't really cater to different mediums beyond text-based LLMs.

Because we built an infrastructure product and we're not constraining which models you can select, we've opened up more options for customers. If you want to go out of your way and do something that's not in a dropdown menu somewhere, we support that.

We also see people who need multi-node training for longer sequence lengths coming to Baseten. In addition, when things go wrong or you want to go deeper, our solution caters to people who are more hands-on. You get into the code, you're able to debug, you can tweak parameters—we're not limiting you to some set of knobs. It's built for developers, essentially.

Say you're training on GCP today and having a tough time with infrastructure setup. You want to use multi-node on H200s, but DWS doesn't support that. You have an existing stack and want to expand somehow.

Bringing that code over, bringing that training pipeline over to Baseten, is really simple. We built this with that person in mind—it's quick to switch over, quick to migrate. We're very unopinionated. You're not going to run into tons of abstractions or SDKs that force you to mold your code to fit our view of the world. You can take the code that works today and bring it to our platform, take advantage of on-demand compute, and use storage primitives that make your iteration loop tighter.

Baseten is incredibly good at inference, and I've never felt like there was more fertile ground to build a new product. Everybody who's on inference at Baseten is looking to train, right? You're going to train that model and where do you want it to go? You want to serve your customers, build a differentiated product.

One way we really stand out is our pipeline from training into Baseten's premier inference product. When we go into a call to talk about training, we actually start by asking: What does your inference look like? What do you need for time to first token? What do you need for throughput? What models are you using today? This helps us understand the use case and constrain the number of viable solutions.

We launched closed beta on May 19th. A big day for Baseten because we also launched Model APIs. Everyone was in SF, we did two product launches. I couldn't believe it—everything worked on the first day.

For training, we were building from the ground up, taking customers in one by one. One of the luxuries of building a new product at Baseten is this FDE-driven development cycle where we deeply integrate with customers to understand their stack. It helped us find rough edges and align what we're building with what we envision taking to market.

My biggest learning was how much marketing could actually help shape the product and technical requirements. It almost feels taboo to say as an engineer. You know the hierarchy: you interact with your product team, your PM, then marketing, then sales. But understanding positioning and what message you want to go to market with can really help you internalize what's worth moving up in the backlog.

Here's a simple example: in beta, we built support for bringing your own image, and we thought, "At some point, we'll build support for private Docker images." The first customer spent an hour trying to recreate an image they already had. We told them to stop and built private registry support the next day. That type of product development works because we had high conviction about our thesis, so when we heard feedback, we knew exactly what to prioritize.

They were a really early adopter of the product. They were able to take a use case where they were using a larger model and distill it into a smaller model for their specific task. This led to a [23x improvement in end-to-end inference speed](https://www.baseten.co/resources/customers/openevidence-delivers-instant-medical-information-with-baseten/).

We're seeing this pattern where customers prove out a use case with general-purpose models, then take smaller models and figure out how to make them as performant so the user experience is just as good, if not better. A lot of people think about training and want to train DeepSeek or Qwen 2.5 72B—incredibly powerful models. But there's utility and pragmatism in asking: what's the minimum viable model we can use that maintains the quality of our product?

For example, Qwen3-8B and [Qwen3-Coder](https://www.baseten.co/library/qwen3-coder-30b/) are incredibly powerful models. So when you take these smaller models and you build a more constrained task for them, they do really well.

[Oxen](https://www.baseten.co/resources/customers/from-datasets-to-deployed-models-how-oxen-ai-builds-on-baseten/) is a platform for fine-tuning and serving models with a user-friendly interface for bringing your data, training a model, tracking changes, and handling data versioning really well. They're built on top of Baseten end-to-end—both training and inference.

This is a different use case from OpenEvidence. With OpenEvidence, you see a team of researchers improving their model stack. With Oxen, you see a platform building on top of our infrastructure so others can do the same.

One awesome thing: the Thinking Machines blog post recently generated hype around training, and Oxen noticed their training usage picking up. As they got more traffic, Baseten scaled seamlessly. We built the product so it's not just something you use via CLI. We provide APIs that do everything the CLI does, so it's a really seamless technical integration if you want to build a platform on top of our training infrastructure.

Check out the [docs](https://docs.baseten.co/training/overview) at Baseten. There's a [Getting Started guide](https://docs.baseten.co/training/getting-started), and even better, we give you a single command at the top that you can run to actually kick off a training job. We know engineers don't always want to read through guides; they want to get their hands dirty and play with code.

Look at our [cookbook recipes](https://github.com/basetenlabs/ml-cookbook/tree/main) to see if there's anything close to what you're working with in production. Whether you want to do GRPO, SFT, run with LoRA, or run full fine-tunes. Find something close to your use case and run a truss train push.

Ready to Train? [Get started with Baseten Training.](https://app.baseten.co/training)
