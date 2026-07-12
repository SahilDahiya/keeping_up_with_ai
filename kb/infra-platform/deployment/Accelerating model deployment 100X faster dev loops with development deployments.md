---
title: 'Accelerating model deployment: 100X faster dev loops with development deployments'
topic: infra-platform
subtopic: deployment
secondary_topics:
- models/fine-tuning
summary: Explains development deployments and draft models as a way to shorten model
  deployment iteration loops.
source: baseten
url: https://www.baseten.co/blog/100x-faster-dev-loops-with-draft-models/
author: Philip Kiely
published: '2022-12-08'
fetched: '2026-07-11T04:11:20Z'
classifier: codex
taxonomy_rev: 1
words: 810
content_sha256: 46f6eaa726a36aa4800821fe64c01324848e79218e32ab6cdcf645a1fae9f5b7
triage: keep
skip_reason: null
---

# Accelerating model deployment: 100X faster dev loops with development deployments

![100x faster dev loop](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1747614462-dev-loop.png%3Fauto%3Dformat%26fit%3Dcrop%26h%3D630%26w%3D1200&w=3840&q=100)

When working with ML models, slow dev loops make all but the most essential deployment workflows too expensive and time consuming to even consider. To fix this, Baseten introduced development deployments, which unlock a live reload dev loop that makes testing your updates take seconds not minutes.

## Slow dev loops break flow state and make for a frustrating experience

When a web developer using any modern framework is coding locally, they don’t have to wait for a server to restart, container to rebuild, or dependency chain to resolve before seeing the result of their change. Instead, the update is nearly instant. Web developers have come to expect this live reload experience from their toolchains, and it is time that data scientists and ML engineers expect the same.

But when working with ML models, slow dev loops make all but the most essential deployment workflows too expensive and time consuming to even consider. To fix this, Baseten introduced development deployments.

When you make a code change to a development deployment, the model server checks if it can hot-swap the new code in place of the code that is currently running. For example, if you update your pre-processing function to parse input differently, that new function can be swapped in and run immediately, without shutting down and rebuilding your model serving environment.

This live reload workflow — redeploying and testing code in real time — is exactly the same superpower that web developers have enjoyed for decades. Live reload makes common deployment tasks 100X faster: from waiting five minutes or more for your container to rebuild to just about three seconds for everything to be updated. Live reload means you can test your model in the context of your entire application and rapidly iterate until you’re happy with the system end-to-end.

## One hundred times faster

Spinning up a model server from nothing takes time. First, resources must be allocated to a server. Then a Docker image is built and a proper Python environment is installed. Once everything is ready, the model is loaded onto the server, and the server is configured to accept requests.

This whole process varies in duration based on the complexity of the environment and the size of the model, but it takes a few minutes. Let’s say five. Deploying a model in five minutes as a last step in a workflow is not that bad; the problem is that this five-minute deployment happens over and over again during common dev loops.

Baseten has solved this choke point for common model deployment tasks by enabling live reload on development deployments. With these specialized deployments, the dev loop for testing an update to your model code gets 100X faster — from about five minutes to about three seconds.

### Slow dev loops break flow state

I’ll admit it … every once in a while a [few minutes of compile time is nice](https://xkcd.com/303/). Waiting for my code to build, I can stretch, grab a snack, or respond to a Slack message. But when I’m trying to iterate rapidly during development, waiting minutes for each change is just brutal. And in the course of ordinary dev work, these gaps impede finding and staying in a flow state.

With this pain in mind, we set out to radically shorten the dev loop for writing model serving code. We decided that data scientists and ML engineers need live reload for better workflows. Let’s take a look at where and how this affects the model creation process.

## How it works

### Creating a development deployment

The `truss push` command deploys your model as a development deployment by default. Here’s a simple example for deploying [Stable Diffusion XL](https://www.baseten.co/library/stable-diffusion-xl/):

```
pip install --upgrade truss
git clone https://github.com/basetenlabs/truss-examples
cd stable-diffusion/stable-diffusion-xl-1.0
truss push
```
Your model will be deployed as a development deployment with a live reload server to patch changes that you make locally.

To have your development deployment watch your local environment for changes, run:

`truss watch`### Testing in a production-like environment

Creating a development deployment doesn’t interfere with existing deployments. When you're satisfied with your model, you can promote the deployment to production.

Development deployments operate much like published deployments. They have their own [API endpoint](https://docs.baseten.co/api-reference/development-predict) and [special autoscaling settings](https://docs.baseten.co/deploy/lifecycle) designed to save you money while experimenting, but otherwise behave exactly like a production deployment.

Once you've tested your model, you can promote it to production from the model dashboard or run the `truss push` command again with the `trusted` flag:

`truss push --trusted`## Accelerate your dev loop

Development deployments are available today for Baseten users. Just upgrade to the latest version of [Truss](https://pypi.org/project/truss) and [check the docs for more complete examples](https://truss.baseten.co/usage).

And if you’re not yet using Baseten to deploy your models, sign up today to accelerate your dev loop with development deployments and the entire Baseten platform.
