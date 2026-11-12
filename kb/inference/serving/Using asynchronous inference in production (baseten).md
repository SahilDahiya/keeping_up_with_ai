---
title: Using asynchronous inference in production
kind: blog
topic: inference
subtopic: serving
secondary_topics: []
summary: Describes Baseten's async inference queueing architecture (priority queue,
  webhook/cloud-storage delivery) that protects against timeouts and traffic spikes
  for long-running or non-interactive inference requests.
triage: null
skip_reason: null
source: baseten
url: https://www.baseten.co/blog/using-asynchronous-inference-in-production
author: Samiksha Pal
published: '2024-07-11'
fetched: '2026-11-12T06:12:32Z'
classifier: claude
taxonomy_rev: 2
words: 964
content_sha256: ba8aef55c2eb0d93342f701a104502ad621fda98e4f6c2158f1f1ff5b67750f5
---

# Using asynchronous inference in production

AI engineering
# Using asynchronous inference in production

Learn how async inference works, protects against common inference failures, is applied in common use cases, and more.


- Authors
- Date
- July 11, 2024

TLDR

Real-time inference can fail for long-running requests, spikes in traffic, and request prioritization. In contrast, async inference queues your requests for processing and executes them based on your model’s capacity and each request’s priority. This smooths out spikes in traffic, reduces timeouts, and improves GPU utilization. Join our live webinar to learn more!

After witnessing numerous customers encounter the limitations of real-time inference, we set out to build [asynchronous inference](https://docs.baseten.co/invoke/async) on Baseten. Now, anyone can run async inference on any model—whether trained in-house, fine-tuned, or open-source—without making any changes to their code!

The async workflow looks like this:

1. You send an async request to your model for inference, optionally specifying its priority.
2. The request is added to a queue.
3. You receive your request’s ID to track its status.
4. As soon as your model has capacity, it processes your request based on its place in the queue.
5. The inference output is sent to your webhook, written to a file on cloud storage, or both.

Async inference on Baseten protects against different types of inference failures, like overloaded models and timeouts. You can reliably schedule thousands of inference requests without worrying about the complexity of queueing, model capacity, or scaling GPUs at inconvenient times.

Most model inference is real-time: you send data to your model, it gets processed, and you receive the output immediately afterward (think ChatGPT). Each inference request has equal priority.

Real-time inference is convenient but can fail with long-running tasks and spikes in traffic. Requests start queuing up at your model once it reaches capacity (i.e., it can’t process any more requests); if too many requests are queued, you can run into timeouts. You could try increasing the number of instances you use, but this would be more expensive, require more developer attention, and waste resources if the number of requests decreases.

On the other hand, async inference does not immediately send your requests for processing. Instead, your requests are added to a queue; they get processed by your model based on its capacity and the requests’ priority.

Any task that doesn’t need real-time inference outputs can benefit from async inference. Baseten's async inference system is mindful of how many requests your model can handle at once and only sends requests when your model has the capacity for them.

Imagine you’re running 5 model replicas, each configured to handle 20 concurrent requests. That’s 100 requests that can be processed concurrently, but what happens if you get an unexpected spike of 200? Or 1000?

Real-time inference breaks down when models are at capacity (e.g., due to spikes in traffic) or requests hit timeouts (e.g., they run too long or get starved by active requests). Whether you’re generating embeddings over thousands of documents or running transcription batches for a long audio clip, jobs that create thousands of requests can overwhelm your model. Real-time inference failures like these can create a poor user experience and a stressful developer experience.

Async inference addresses these issues while being more cost-efficient: instead of adding more instances, you leverage your idle capacity by sending queued requests during off-peak times. For jobs that don’t need to happen immediately (like backfills), running these requests at a lower priority also allows live requests to be served first.

Async inference should be used when you want to:

- Execute workloads in order of assigned priority.
- Handle long-running tasks with increased robustness against timeouts.
- Schedule tens of thousands of inference requests without worrying about model capacity.

Building an async inference mechanism might seem straightforward, but creating a robust solution requires gathering insights from diverse customer use cases.

Real-time inference can fail for many reasons, and a robust async inference system should give developers visibility and control over their requests. With this in mind, we built a [user-configurable retry schema](https://docs.baseten.co/api-reference/production-async-predict), detailed model logs, [metrics](https://docs.baseten.co/invoke/async#observability) to understand the time spent in-queue, and the ability to [cancel requests](https://docs.baseten.co/api-reference/cancel-async-request) as needed. If you’re curious about what’s happening with your (tens of) thousands of async requests, you can ask the async service [for its status](https://docs.baseten.co/api-reference/get-async-request-status).

We also implemented backpressure to ensure that requests only get processed when the model has capacity, and a heartbeat mechanism to save stuck requests—two features that keep things running smoothly behind the scenes.

To access your async inference results, you can use a webhook to receive model outputs or send them directly to [cloud storage](https://docs.baseten.co/invoke/async). Using a webhook also lets you get notified instantly when your requests are finished, and [results can be secured](https://docs.baseten.co/invoke/async-secure) by creating a webhook secret and validating the signature sent.

Working directly with different customers on their problems helped us turn the flowchart above into a simple developer experience like this:

Asynchronous inference on Baseten is flexible: you can combine async requests with real-time ones while making your inference pipeline more robust, and leverage async in multi-component inference pipelines like [Chains](https://docs.baseten.co/chains/overview).

Async inference on Baseten enables you to fully utilize compute that would otherwise be idle, gives you increased visibility and control over your pipelines, and makes you robust to different types of inference failures. You can be greedy with your pipelines and do pre-processing on the fly, since you can handle those longer-running jobs. And you definitely won’t have to get up in the middle of the night to scale up your GPUs.

You can leverage async inference for any model running on Baseten without making any changes to your model code. Check out our [guide to using async inference](https://docs.baseten.co/invoke/async) and try it out with your models, and don’t miss [our webinar on August 15th](https://www.baseten.co/resources/webinar/asynchronous-inference-on-baseten/) to learn more!
