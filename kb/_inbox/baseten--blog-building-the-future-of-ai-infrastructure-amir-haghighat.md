---
title: 'Building the future of AI infrastructure: Q&A with Baseten Co-founder Amir
  Haghighat'
kind: blog
topic: null
subtopic: null
secondary_topics: []
summary: null
triage: null
skip_reason: null
source: baseten
url: https://www.baseten.co/blog/building-the-future-of-ai-infrastructure-amir-haghighat
author: Madison Kanna
published: '2025-09-15'
fetched: '2026-11-12T06:10:28Z'
classifier: null
taxonomy_rev: 2
words: 1245
content_sha256: a0198faaaaccde76f2f7d015ff4c3b5eab7aab833cb084eecbe611789efa23f3
---

# Building the future of AI infrastructure: Q&A with Baseten Co-founder Amir Haghighat

Community
# Building the future of AI infrastructure: Q&A with Baseten Co-founder Amir Haghighat

A Q&A with Amir Haghighat about the company's founding journey, our series D and our pivot from traditional ML to generative AI.


- Authors
- Date
- September 15, 2025

At our [Series D celebration](https://x.com/Madisonkanna/status/1964025930474803370), [Philip](https://x.com/philip_kiely) and I sat down with [Amir](https://x.com/amiruci), co-founder and CTO of Baseten, for a Q&A about the company's founding journey, our pivot from traditional ML to generative AI, and the unique challenges of scaling a team amid the breakneck pace of AI infrastructure innovation. We're sharing the highlights here.

**Amir:** I met my co-founders about 14 years ago when we were all working at the same startup together. We went different paths afterward, but always stayed friends, and we got back together to start Baseten for two main reasons.

First, we liked working with each other and had stayed friends all those years. We basically thought, "Let's hang out and figure out something to work on together." Second, we had similar interests in the ML space and similar realizations from our past work about the tooling we wished existed that would have helped us. We wanted to build the tooling that would have helped us. We got funded by Greylock and started building exactly six years ago.

The product was always focused on ML infrastructure and within that it was always focused on inference. We stayed agnostic of training models and cared more about what comes next—the serving of models, the infrastructure for that serving, monitoring, scalability, and things like that.

What changed over time were the types of models that customers were deploying and the use cases. In the early days, five or six years ago, we were dealing with classic machine learning models such as regressors and classifiers.

The reason why engineers were deploying these models to Baseten is because they were doing mostly internal back-office stuff inside of their own companies: trust and safety, content moderation, fraud operations. But that started changing about three and a half years ago.

We began seeing customers deploy deep learning models, BERT-based models, transformers, and later diffusion models. Two things were notably different:

1. These models weren't being used for internal back-office use cases anymore. They were in the path of the end user, which meant our customers suddenly cared about things we were building—low latency, high throughput, four-nines availability.
2. These new architectures solved problems you didn't think were possible before. With a random forest, you know exactly what it can and cannot do. But with transformers, you're constantly surprised—"wait, you can do that?" Same with diffusion models making music.

We realized there was a future here, and we decided to build towards that future.

Building towards this future meant building a lot more depth of product on two main pillars:

1. Optimizations at the model level and the runtime level to get the most out of the GPU.
2. Horizontal scale infrastructure and going across regions, and across clouds. Also, wrapping around these two pillars is the right data to expose the power and control and visibility to the end user.

We did this three and half years ago and this was good timing because two years ago a lot of companies were using these generative models and we already had a good product for them. The first three years, the company wasn’t working. But all along, we were having a good time and we liked working with each other.

**Amir:** We ended up being right but I don’t know if the reason was right. When we first started, people told us this was stupid. They'd say, "Why are you focusing on serving models? You have to first train the model in order to serve it."

The reason we wanted to focus on inference was this. We had worked together at Gumroad, where we had a credit card fraud problem. A classic use case for machine learning is detecting this fraud. My co-founders Tuhin and Phil trained a classifier for fraud detection. The training part was easy—they just trained it on their laptop CPU with structured data. Out came a model that was objectively performing well.

But then came the hard part: operationalizing it. Making sure it runs in production, runs really fast, handles high scale. That's where we wished better tooling existed. So when we got together to start Baseten and we reflected back on what tooling we wished existed, we thought about serving the models and realized tooling would’ve helped us.

Interestingly, we ended up being right later on in a way that we didn’t expect. Later on when open source pre-trained models came out, many people were actually starting from inference first, then maybe doing some fine-tuning later. We had the right thesis. I don’t know if the original reason was correct but it became correct over time.

**Amir:** Every few months there's this sort of hecticness or pain threshold that I hit, and I think, "Let's see if we can go above that." My pain tolerance has just gone up slowly over time.

Growth does mask a lot of problems, so we have that going for us. But it's still hard, especially in our space where product-market fit is fleeting. You can have it today and not have it in nine months.

The key challenge is: do you just put more fuel on the fire since you found the right thing, or do you keep some of that exploratory nature that got you here? We've killed products over time.

The key is having good intuition, being willing to go out on a limb, building fast, learning fast, and killing things when you need to kill them.

**Amir:** There's something very palpable in the market right now. More and more normal engineers—not ML specialists—are being exposed to inference problems and AI generally. It's unreasonable to expect every engineer to be well-read on speculative decoding, attention optimizations, KV cache techniques, or multi-cloud inference strategies.

I want Baseten to be where these AI efforts happen in different companies. From "Hey, I just heard about a new open source model" to having it available immediately - to running benchmarks, fine-tuning, optimizing for latency or throughput. Baseten will tell you the tools you have in your toolbox and when to use which. Not only this but you can apply these tools and see their impact on the model.

We have a lot of the building blocks in this story, but we don't have all of them, and they're not completely tied together in the right developer experience yet. That's what I'm excited about—filling in the holes and having a very cohesive end-to-end story.

**Amir:** I don't have universal advice because it's so situation-specific, but I can tell you how we approached it: we optimized not for valuation or even the pedigree of the firm, but for the person.

A friend told me this analogy I really liked—if you're going to get surgery, you don't care whether it's at UCSF, Stanford, or Kaiser. You care who the surgeon is.

That person you choose is going to be partnered with you for a very long time, for the rest of the life of the company. It's okay if the firm doesn't have the highest pedigree or if the valuation is 10% lower. These outcomes are generally binary—either it works out or it doesn't. You're not going to look back and think, "I should have saved 10% over there."
