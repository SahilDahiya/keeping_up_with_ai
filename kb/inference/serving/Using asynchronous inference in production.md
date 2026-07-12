---
title: Using asynchronous inference in production
topic: inference
subtopic: serving
secondary_topics:
- infra-platform/deployment
summary: Explains asynchronous inference patterns for production model-serving workloads.
source: baseten
url: https://www.baseten.co/blog/using-asynchronous-inference-in-production/
author: Samiksha Pal; Helen Yang; Rachel Rapp
published: '2024-07-11'
fetched: '2026-07-11T04:09:27Z'
classifier: codex
taxonomy_rev: 1
words: 1154
content_sha256: 3a30956af60f2bf7df80c0811c06c1f08df75e1edf0749f6fe020e4fdda3198e
triage: keep
skip_reason: null
---

# Using asynchronous inference in production

![Asynchronous inference](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1747439254-async.png%3Fauto%3Dformat%26fit%3Dcrop%26h%3D630%26w%3D1200&w=3840&q=100)

Real-time inference can fail for long-running requests, spikes in traffic, and request prioritization. In contrast, async inference queues your requests for processing and executes them based on your model’s capacity and each request’s priority. This smooths out spikes in traffic, reduces timeouts, and improves GPU utilization. Join [our live webinar](https://www.baseten.co/resources/webinar/asynchronous-inference-on-baseten/) to learn more!

After witnessing numerous customers encounter the limitations of real-time inference, we set out to build [asynchronous inference](https://docs.baseten.co/invoke/async) on Baseten. Now, anyone can run async inference on any model—whether trained in-house, fine-tuned, or open-source—without making any changes to their code!

The async workflow looks like this:

- You send an async request to your model for inference, optionally specifying its priority.
- The request is added to a queue.
- You receive your request’s ID to track its status.
- As soon as your model has capacity, it processes your request based on its place in the queue.
- The inference output is sent to your webhook, written to a file on cloud storage, or both.

![A diagram showing the five steps of the async inference workflow.](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1720692430-fig1.png%3Fauto%3Dformat%26w%3D1200&w=3840&q=75) The async inference request workflow lets you queue, prioritize, and track inference requests before receiving model outputs via a webhook or cloud storage.

The async inference request workflow lets you queue, prioritize, and track inference requests before receiving model outputs via a webhook or cloud storage.Async inference on Baseten protects against different types of inference failures, like overloaded models and timeouts. You can reliably schedule thousands of inference requests without worrying about the complexity of queueing, model capacity, or scaling GPUs at inconvenient times.

## What is async inference?

Most model inference is real-time: you send data to your model, it gets processed, and you receive the output immediately afterward (think ChatGPT). Each inference request has equal priority.

Real-time inference is convenient but can fail with long-running tasks and spikes in traffic. Requests start queuing up at your model once it reaches capacity (i.e., it can’t process any more requests); if too many requests are queued, you can run into timeouts. You could try increasing the number of instances you use, but this would be more expensive, require more developer attention, and waste resources if the number of requests decreases.

On the other hand, async inference does not immediately send your requests for processing. Instead, your requests are added to a queue; they get processed by your model based on its capacity and the requests’ priority.

![A diagram highlighting the request queue as part of the async inference service.](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1720692442-fig2.png%3Fauto%3Dformat%26w%3D1200&w=3840&q=75) Async inference requests are added to a request queue before being sent to your model for processing.

Async inference requests are added to a request queue before being sent to your model for processing.Any task that doesn’t need real-time inference outputs can benefit from async inference. Baseten's async inference system is mindful of how many requests your model can handle at once and only sends requests when your model has the capacity for them.

## When to use async inference instead of real-time

Imagine you’re running 5 model replicas, each configured to handle 20 concurrent requests. That’s 100 requests that can be processed concurrently, but what happens if you get an unexpected spike of 200? Or 1000?

Real-time inference breaks down when models are at capacity (e.g., due to spikes in traffic) or requests hit timeouts (e.g., they run too long or get starved by active requests). Whether you’re generating embeddings over thousands of documents or running transcription batches for a long audio clip, jobs that create thousands of requests can overwhelm your model. Real-time inference failures like these can create a poor user experience and a stressful developer experience.

Async inference addresses these issues while being more cost-efficient: instead of adding more instances, you leverage your idle capacity by sending queued requests during off-peak times. For jobs that don’t need to happen immediately (like backfills), running these requests at a lower priority also allows live requests to be served first.

Async inference should be used when you want to:

- Execute workloads in order of assigned priority.
- Handle long-running tasks with increased robustness against timeouts.
- Schedule tens of thousands of inference requests without worrying about model capacity.

## Building a seamless async inference solution

Building an async inference mechanism might seem straightforward, but creating a robust solution requires gathering insights from diverse customer use cases.

Real-time inference can fail for many reasons, and a robust async inference system should give developers visibility and control over their requests. With this in mind, we built a [user-configurable retry schema](https://docs.baseten.co/api-reference/production-async-predict), detailed model logs, [metrics](https://docs.baseten.co/invoke/async#observability) to understand the time spent in-queue, and the ability to [cancel requests](https://docs.baseten.co/api-reference/cancel-async-request) as needed. If you’re curious about what’s happening with your (tens of) thousands of async requests, you can ask the async service [for its status](https://docs.baseten.co/api-reference/get-async-request-status). 

We also implemented backpressure to ensure that requests only get processed when the model has capacity, and a heartbeat mechanism to save stuck requests—two features that keep things running smoothly behind the scenes.

![A messy diagram highlighting the many different points of failure async inference has to account for.](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1720692452-fig3.png%3Fauto%3Dformat%26w%3D1200&w=3840&q=75) A robust async inference solution provides visibility while accounting for different points of failure, like stuck requests and overwhelmed models.

A robust async inference solution provides visibility while accounting for different points of failure, like stuck requests and overwhelmed models.To access your async inference results, you can use a webhook to receive model outputs or send them directly to [cloud storage](https://docs.baseten.co/invoke/async). Using a webhook also lets you get notified instantly when your requests are finished, and [results can be secured](https://docs.baseten.co/invoke/async-secure) by creating a webhook secret and validating the signature sent.

Working directly with different customers on their problems helped us turn the flowchart above into a simple developer experience like this:

![A clean and simple async inference workflow of sending a request and receiving outputs to cloud storage.](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1720692464-fig4.png%3Fauto%3Dformat%26w%3D1200&w=3840&q=75) Baseten’s async inference solution abstracts complexity for a simple developer experience.

Baseten’s async inference solution abstracts complexity for a simple developer experience. ## Production-ready async inference on Baseten

Asynchronous inference on Baseten is flexible: you can combine async requests with real-time ones while making your inference pipeline more robust, and leverage async in multi-component inference pipelines like [Chains](https://docs.baseten.co/chains/overview). 

Async inference on Baseten enables you to fully utilize compute that would otherwise be idle, gives you increased visibility and control over your pipelines, and makes you robust to different types of inference failures. You can be greedy with your pipelines and do pre-processing on the fly, since you can handle those longer-running jobs. And you definitely won’t have to get up in the middle of the night to scale up your GPUs.

You can leverage async inference for any model running on Baseten without making any changes to your model code. Check out our [guide to using async inference](https://docs.baseten.co/invoke/async) and try it out with your models, and don’t miss [our webinar on August 15th](https://www.baseten.co/resources/webinar/asynchronous-inference-on-baseten/) to learn more!
