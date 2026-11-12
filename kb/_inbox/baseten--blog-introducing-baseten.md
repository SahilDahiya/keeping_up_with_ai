---
title: Introducing Baseten
kind: blog
topic: null
subtopic: null
secondary_topics: []
summary: null
triage: null
skip_reason: null
source: baseten
url: https://www.baseten.co/blog/introducing-baseten
author: Tuhin Srivastava
published: '2021-05-20'
fetched: '2026-11-12T06:12:52Z'
classifier: null
taxonomy_rev: 2
words: 1110
content_sha256: 45a795ec1fc1bcb6d86ea8bdb2027de513f59ad22ece5f444737c99fb8c54223
---

# Introducing Baseten

News
# Introducing Baseten

Introducing the fastest way to build applications powered by machine learning


- Authors
- Date
- May 20, 2021

*Author's note: We have made exciting progress in the years since posting this introduction, you'll find more up-to-date information in our Series C announcement.*

Over the last decade, our team has used machine learning to solve problems across organizations big and small, all the way from framing problems and ideating to putting the power of models directly in the hands of users. We’ve seen amazing ML-driven outcomes in healthcare, the creator economy, and business operations, and become convinced that machine learning is poised to have a profound impact on the way we live and work.

We have also learned that it is still far too difficult to build end-to-end product solutions that use machine learning for impact. Despite the cost of training having rapidly decreased and the increased prevalence of effective pre-trained models, the vast majority of gains are yet to be realized. There are many things that are obviously difficult about doing machine learning today — gathering the right data, labeling data, training and optimizing models, and of course, deploying and serving models. And a whole new set of impressive tools has emerged to tackle these problems.

However, in our experience, the stickiest part of modern ML work is shipping — and this crucial step is where most teams get stuck. It’s taking the model out of the notebook and embedding it in an internal or external-facing application such that real users can interact with it, give feedback, and ultimately make decisions. Shipping an ML product to end users isn't the last step in a linear pipeline. It's a crucial part of an iterative loop -- only then can you establish the virtuous cycle you need to improve the performance of the model in the real world.

Achieving this requires an immense amount of high-coordination engineering work — grappling with web frameworks to serve the model, building the complex infrastructure to scale properly, and finally a completely separate stream of product-engineering work to either integrate into existing systems or build new user interfaces. All in all, it is still prohibitively expensive to go zero-to-one on solving real problems with machine learning and many talented teams are stuck in the “analytics” and “experimentation” phase of ML; there is data and models, but few can point to outcomes such as better user experiences, more revenue or lesser costs.

Baseten is the fastest way to build applications powered by machine learning. Our mission is to increase the value delivered with machine learning by lowering the barrier to usable, productized ML.

Today, with Baseten, data scientists can deploy machine learning models with a couple of lines of code and serve fast, scalable APIs without the infrastructure, framework, and deployment nightmares. And you don’t have to be an ML practitioner to find BaseTen useful — engineers can choose from a library of state-of-the-art pre-trained models to bootstrap their machine learning efforts. It doesn’t stop there — if and when you need a user interface for your users, our drag-and-drop builder lets you build stateful and interactive interfaces; no front-end experience required.

Building a horizontal product with such a wide surface area has been challenging and fun. A few guiding ideas that have helped pave the way for us are:

- **Principle of least astonishment**. Baseten is a new way to build ML-powered applications, but it should not seem foreign. Data scientists and engineers will notice concepts that match ones they’re already familiar with.
- **Easy things are easy; hard things are possible**. Most use cases are dead simple, fast and scalable using Baseten. That doesn’t come at the cost of control and visibility — Baseten is architected modularly and is built using standard technologies (e.g. Docker, Knative, Postgres, etc), so more advanced users can have access to the underlying technologies when need be.
- **Scale gracefully from toy apps to complex, mission-critical full-stack applications**. We expect that our users will build fun toy apps with Baseten. However our sights are on supporting the development and operationalization of large-scale, mission-critical applications with many creators and operators. This goal enforces additional requirements on the product, including building statefulness as a first-class concept. This sets BaseTen apart from the notebook-based app frameworks.

And we have seen promising signs from our alpha users: from a small data science team at a fintech company operationalizing a customer-scoring ML model without needing engineering resources, to a digital therapeutics startup with no ML practitioners creating a workflow application for their clinical operations team powered by a state-of-the-art pre-trained model from Baseten’s model zoo. What excites us the most is the diversity of the use cases we’re seeing with our alpha users. We’re truly in the early innings of machine learning adoption and we’d love for you to be a part of it as well.

Today, we’re excited to announce our **Closed Beta** — we’re opening up free access for early users to kick the tires and help shape our product roadmap. All we'd like from you is your feedback. If you'd be interested in working with us during this period, please fill out this [**short form**](https://form.typeform.com/to/dXDdS72b?typeform-medium=embed-snippet) and tell us a little more about your use case. We're really excited about the coming weeks and months that we will get to work with you all.

We're also shipping fast — some core areas we're focused in the short term:

- Expanded model zoo — over the past months we’ve added the most in-demand state-of-the-art models (including HuggingFace and GPT-3) to our library of pre-trained models that users can import into their applications. We’re continuing to add models to this library with every release — if there are any models that you’d like to see in the Baseten model zoo, please reach out.
- A rich library of front-end components — today we support over a dozen native Baseten components for our users; we are working on adding more components including media inputs, richer data visualization options, and better queueing/inbox components.
- More integrations — Salesforce, Zendesk, and HubSpot are all on our roadmap. Let us know what else you’d like to see.
- Source control and application versioning.
- Perfecting the ideal development environment.

We’re a small group of engineers and designers figuring out how to make our dent with thoughtfully designed software. We’re an internationally and intellectually diverse group of passionate builders, and try not to take ourselves too seriously. We're backed by top-tier investors and prominent angels and are looking to grow our team. If this sounds interesting to you, please drop us a line at [hi@baseten.co](mailto:hi@baseten.co).
