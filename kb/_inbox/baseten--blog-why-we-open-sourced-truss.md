---
title: Why we built and open-sourced a model serving solution
kind: blog
topic: null
subtopic: null
secondary_topics: []
summary: null
triage: null
skip_reason: null
source: baseten
url: https://www.baseten.co/blog/why-we-open-sourced-truss
author: Phil Howes
published: '2022-08-05'
fetched: '2026-11-12T06:13:04Z'
classifier: null
taxonomy_rev: 2
words: 1047
content_sha256: 8e0073a531f306bdf3d6194afc4f6abcd47dc8a197facfbd2956541c56021540
---

# Why we built and open-sourced a model serving solution

AI engineering
# Why we built and open-sourced a model serving solution

Truss, our open-sourced bridge for model development to deployment, saves time for data scientists and ML engineers on MLOps tasks in model serving.


- Authors
- Date
- August 5, 2022

Model serving, as part of MLOps, is the DevOps challenge of keeping a model functional through repeated train-deploy cycles and production workloads. DevOps is its own specialty for a reason: the endless configuration options and compatibility checks throughout this process can be overwhelming. So data scientists, if they're lucky, are able to turn to infrastructure teams for help. But this is not an ideal solution:

- Data scientists compete for the limited bandwidth of infrastructure teams, leading to long wait times to get models deployed.
- The cost and friction of accessing infrastructure expertise means that only the safest ideas ever see the light of day. A lot of brilliant models may not seem promising at first, and will die in the backlog before reaching their potential.
- The considerations and requirements for serving models with real traffic — reliability, throughput, scalability — differ greatly from running inference in development.
- Debugging is hard when the model serving environment is different from the data scientist's notebook, introducing cumbersome and time-consuming effort to get everything set up right.

And to make things worse, data scientists at small companies and startups might not have access to infrastructure teams at all. And maintaining production models yourself can eat up the majority of a workday. So progress on ML is stifled and business value stays locked up.

To address this problem, we built Truss. Truss bridges the gap between model development and model deployment by making it equally straightforward to serve a model on localhost and in prod, making development and testing loops rapid.

We built and open-sourced Truss with the conviction that eliminating this friction will accelerate machine learning productivity:

- Data scientists can build or deploy Docker images with a single command, reducing the model serving workload.
- Models can be packaged in a standardized format, making it easier to share models within or beyond a team.
- Data scientists can build on each other's work by pulling down popular models without spending hours coaxing them into running in a new environment.

Check out [Truss on GitHub](https://github.com/basetenlabs/truss) — and leave a star to keep an eye on it — to see if it can make your model serving process easier.

Data scientists and machine learning engineers spend a lot of time building models that solve specific problems: sentiment classification, facial recognition, anomaly detection. Generally, this exploratory, experimental work is done using an interactive environment like a Jupyter notebook. To match the wide variety of use cases for ML models, there are a number of popular frameworks to build in, like PyTorch, TensorFlow, and scikit-learn. Each framework specializes in different kinds of models, so a data scientist will pick the framework based on the type of problem they are solving.

As such, the data scientist's development environment needs to be flexible and permissive. Jupyter notebooks are a great tool for training models, but as an impermanent and development-oriented environment they aren't great for model serving. Model serving, or making a model available to other systems, is critical; a model is not very useful unless it can operate in the real world.

We built Truss as a standard for serving models that takes advantage of proven technologies like Docker but abstracts away complexity regardless of model framework. There are other such standards — MLFlow, BentoML, Cog — and next week we’ll do a deep dive into comparisons. But we built Truss for data scientists in startups and scrappy teams, and we wanted a project guided by that vision.

Truss emerged from our internal model serving infrastructure. We decided to maintain it as an open-source package to participate in and give back to the ML community, to give Baseten users more transparency and confidence in their tooling, and to show our work and hold ourselves accountable to high standards for code quality and development practices. Truss as an open-source project that delivers standalone value is an integral part of our roadmap.

Truss turns your ML model into a backend for web, no Django or Flask needed. This "model as a microservice" approach saves time writing and maintaining web server code, and makes the model a single unit within your application.

Every model runs in its own environment. This is a different intuition than most APIs, where endpoints share the same dependencies and resources. But two different machine learning models might depend on different frameworks, packages, and hardware. So Truss keeps everything separate, preventing tangled configurations or repeated model serving work.

And with your model behind an API, you can do end-to-end tests locally with your front-end or other systems. Turning a Python-first object into a web-first object unlocks workflows for all kinds of software developers.

Running a model that someone else has created is non-trivial. Sometimes it even requires re-creating their training environment and training it yourself, but at minimum requires setting up an environment, deserializing the model, and creating a model server.

With Truss, "a model exists" and "I can run the model on any machine" are equivalent statements. Truss reliably packages models to be ready for the web and any other ways people want to interface with it. Package your model as a Truss and share it within your team or with the world, and the "setup" portion of your README will be shorter than ever.

Over time, we aim to add features for iterative development, helping with detecting anomalies, drift, and more. And by composing multiple models, each with their own Truss, you'll be able to build more powerful, capable systems with just a few lines of pre- and post-processing code, conveniently bundled with your model. Truss' use cases are expanding quickly, and you can [review and contribute to the roadmap on GitHub](https://github.com/basetenlabs/truss/blob/main/CONTRIBUTING.md).

To get started with Truss, try following the quickstart guide. If you have ideas for future development or bugs to report, let us know as a [GitHub issue](https://github.com/basetenlabs/truss/issues). And if you want to keep tabs on the development of Truss, [star the repo on GitHub](https://github.com/basetenlabs/truss) and look out for new releases on PyPi!
