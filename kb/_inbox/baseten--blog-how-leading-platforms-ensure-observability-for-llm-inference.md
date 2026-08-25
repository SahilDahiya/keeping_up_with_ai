---
title: How leading platforms ensure observability for LLM inference
kind: blog
topic: null
subtopic: null
secondary_topics: []
summary: null
triage: null
skip_reason: null
source: baseten
url: https://www.baseten.co/blog/how-leading-platforms-ensure-observability-for-llm-inference/
author: Chloe Florit
published: '2026-08-24'
fetched: '2026-08-25T06:08:39Z'
classifier: null
taxonomy_rev: 2
words: 1934
content_sha256: a0315507d4eaa3910cdde7430685c79c1f5e1de763cbd2ceb4eb1ef5f3139b98
---

# How leading platforms ensure observability for LLM inference

![LLM inference observability](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1787173173-baseten-blog-2026-thumbnails-8.png%3Fauto%3Dformat%26fit%3Dcrop%26h%3D630%26w%3D1200&w=3840&q=100)

*LLM inference observability means tracking metrics, logs, and traces to catch problems before users do. This post covers the key metrics (TTFT, TPOT, throughput, latency, KV cache hit rate), the three types of logs that cover build, deploy, and serve stages, and how traces help determine exactly where a request slowed down or failed.* 

When inference slows down, everything downstream is affected: agents stall mid-task, AI chat responses lag, and requests start timing out. Observability lets you catch these problems before your users do and gives you visibility into how your model is running in production.

When your model is live, you can use metrics, logs, and traces to detect when something goes wrong, fix it, determine what happened, and figure out how to prevent it from happening again. In this post, we'll cover each of these tools and how they fit together to catch and debug issues like slow responses, errors, and failed builds or deployments.

## **Key metrics: TTFT, TPOT, TPS, latency, and cache hit rate**

Tracking metrics helps you know when something is wrong before a user tells you. Here are the key metrics for LLM inference observability:

- **TTFT (Time to First Token):** measures how quickly users see something after sending a request. Low TTFT means users see a response quickly; high TTFT makes an app feel frozen or unresponsive.
- **TPOT (Time per Output Token):** measures the average time it takes to generate each subsequent token. High TPOT means text trickles out in stutters instead of flowing.
- **TPS (Tokens per Second, or tokens/sec; throughput):** measures the number of tokens the system generates per second across all requests. It's a measure of system-level capacity, not individual response speed. Low throughput means the system can't scale well to serve more users.
- **End-to-end latency:** how long it takes to get a complete response for a single request. This is the top-line SLA metric: does your app meet its speed requirements?
- **KV cache hit rate:** the fraction of input tokens that already had a KV pair stored in the cache. This happens when a new request begins with the same text (prefix) as a request the model recently processed. Because the model already computed and stored the KV pairs for those tokens, it can retrieve them from the cache instead of recomputing them. A higher hit rate means faster responses at lower cost because less computation is redone. Lower hit rate is slower and more expensive, because most tokens need fresh computation.

**What's a KV (Key-Value) cache?** "Keys" help the model figure out which words to pay attention to, and "values" determine what information gets added to a word's meaning based on the context. Together, they're cached as the "KV cache."

**KV cache management** improves TTFT. It automatically routes requests to replicas that have the necessary context cached, which eliminates redundant prefill compute. This is especially useful for shared prompts, like system messages or few-shot examples.

## **Logs**

Once metrics flag a problem, logs can show you what's causing it. There are three kinds of logs, and each one covers a different stage of a model's lifecycle: building the container, deploying the model, and serving requests.

![The model lifecycle: build, deploy, serve.](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1787172214-inference-observability-1.png%3Fauto%3Dformat%26w%3D1200&w=3840&q=75) The model lifecycle: build, deploy, serve.

### **Build logs**

The build logs track the process of assembling the container image, which holds everything your model needs to run: the model weights, the dependencies (libraries your code needs), and your code (which processes a request and runs it through the model). The container needs to be correctly assembled before it can be deployed to receive requests, so build logs are useful for catching problems before deployment.

The most common failures that build logs catch include:

- **Missing packages:** the code references a library that wasn’t added to the container.
- **Incompatible system requirements:** the container image is built on top of a base image, which usually comes with a CUDA version already installed. If the packages you add during the build expect a different CUDA version than what's in that base image, there's a mismatch and the build fails.
- **Network errors:** if the connection drops, a package or the model weights might fail to download during the build.

![Container image build logs show how Baseten prepares and verifies a model container before deployment.](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1787584392-chatgpt-image-aug-24-2026-05_13_01-pm.png%3Fauto%3Dformat%26w%3D1200&w=3840&q=75) Container image build logs show how Baseten prepares and verifies a model container before deployment.

### **Deploy / promotion logs**

Deployment logs track every key change in the deployment's lifecycle, like replicas coming online, scaling up or down.

Some of those changes are promotions, which occur when a model version moves from one environment to the next: development to staging to production. Development is where you build and test work-in-progress code. Staging is a near-exact copy of production, used to test changes before users see them. Production is the live version of the deployment customers use.

If errors spike, you can check whether that spike happened right after a promotion or scaling event. Comparing deploy/promotion logs with serving logs helps you tell whether a problem was caused by a deployment change or something else.

### **Serving logs**

Serving logs keep track of everything your model prints out while running in production. That includes automatic system messages, such as errors and warnings, as well as anything you’ve told your code to log. These logs can also show some steps during inference (e.g., when a request is received, when generation starts, and whether any errors or retries occur) so you can confirm that requests are coming through and understand what’s happening while the model runs.

Most common failures serving logs catch include:

- **Model-loading errors:** the model fails to load properly at startup (e.g., incompatible dependencies, missing files, memory limits).
- **Runtime exceptions:** a request comes in, but something breaks partway through processing it (e.g., the input data is in the wrong format).
- **GPU/hardware errors:** issues like running out of GPU memory (OOM) or a hardware-level crash.

Every log carries a `request_id`, so you can filter any log down to a single request. For example, if a specific inference request fails, you can use its `request_id` to isolate every log event associated with that request and reconstruct what happened. That's how Baseten does request-level log investigation.

## **Traces**

Serving logs are a running feed of every event and error across all requests, over time. A trace is different: it’s a timed, step-by-step story of *one individual* request. Where was time spent, and at which step did it break?

Traces show what happens before your request ever reaches the model:

- **API Gateway:** checks that the API caller is authenticated and authorized to call the model, before letting the request into the serving path ([Istio](https://istio.io/) → Activator → Queue → Server). It also decides which cluster should handle it. This lets Baseten shard a model across clusters where capacity is available.
- **Service Mesh:** routes the request within the selected cluster to a ready model replica. If no replicas exist, it routes to the Activator.
- **Activator:** when there are zero replicas running, the Activator holds the request, starts a replica, and forwards the request once it's ready.
- **Queue:** if replicas exist but are all busy, the queue holds the request until one frees up.
- **Server:** runs the request through the model and produces a response.

![The request path before it reaches the model.](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1787172562-api_gateway_service_mesh_diagram.png%3Fauto%3Dformat%26w%3D1200&w=3840&q=75) The request path before it reaches the model.

A trace tells you when a request started, when it ended, and whether it completed successfully or errored out.

Most production slowdowns happen in these before-the-model steps, and traces help you pinpoint which one caused it. Here are a few common failures traces can detect:

- **Cold-start latency** ***(Activator)*****:** delay caused by waiting for a replica to boot up from zero.
- **Queue backups** ***(Queue)*****:** replicas are all busy, so requests pile up waiting their turn.
- **Routing failures** ***(Istio)*****:** requests dropped or misrouted before they ever reach the model.

Here's what that looks like as a waterfall, for a single request that took 240 milliseconds end-to-end:

![Waterfall diagram of request latency broken down by component, showing how long each stage takes in the request path.](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1787172812-inference-observability-3-2.png%3Fauto%3Dformat%26w%3D1200&w=3840&q=75) Waterfall diagram of request latency broken down by component, showing how long each stage takes in the request path.

In this example, most of the time is in the Server step, which is expected: that's the actual model computation. But if the API Gateway, Service Mesh, or Queue start eating up a larger share, that's a sign that there's a problem upstream of the model. Depending on where the request spends the most time, the fix will vary. For example, long Queue time might require raising min replicas or concurrency tuning, while long Server time may call for different hardware, model/runtime optimizations, or batching changes.

## **What LLM inference observability tools should you use?** 

Build logs, deploy/promotion logs, serving logs, and traces each tell a different story of your model in production. Metrics tell you if and when something is wrong. Logs tell you what went wrong, and at which stage: building, deploying, or serving. Traces tell you where in the request path there was a delay. When you run into a deployment issue, check the right tool for the job, and make sure you understand what the data is actually telling you.

Baseten includes built-in observability in the product dashboard for monitoring [deployment health](https://docs.baseten.co/observability/health), [request volume, latency, errors, and model performance](https://docs.baseten.co/observability/metrics). You can also [export metrics](https://docs.baseten.co/observability/export-metrics/overview) to your own stack via a Prometheus-compatible endpoint, or [stream logs over OTLP](https://docs.baseten.co/observability/logs#export-logs-to-an-otlp-endpoint) to Honeycomb, Datadog, Grafana Cloud, Sentry, or any OTLP/HTTP receiver. For metrics, there are guides for [Prometheus](https://docs.baseten.co/observability/export-metrics/prometheus), [Datadog](https://docs.baseten.co/observability/export-metrics/datadog), [Grafana Cloud](https://docs.baseten.co/observability/export-metrics/grafana), and [New Relic](https://docs.baseten.co/observability/export-metrics/new-relic), plus a [metrics support matrix](https://docs.baseten.co/observability/export-metrics/supported-metrics).

Most teams don't run inference in isolation: it's one service inside a larger application. Inference is mission-critical when your product stops working correctly if the model stops responding. When that's the case, the model metrics belong in the same place as the rest of your application metrics. Otherwise, every time something slows down, you would need to check your inference platform in one tab and your own monitoring in another to figure out where the problem comes from.

## **FAQ**

**What is observability for LLM inference?**

Observability is how you monitor a model in production: metrics tell you how well it's performing, logs tell you what happened and why, and traces tell you where time went on a single request.

**What's the difference between logs and traces?**

Logs are a running feed of every event across all requests over time. A trace is the step-by-step story of one specific request, showing when it started, when it ended, and which step it failed or slowed down at.

**What causes high time to first token (TTFT)?**

High TTFT usually comes from cold starts, queue backups, or low KV cache hit rates. A cache miss means the model has to recompute the prefix instead of reusing what's already stored, which adds time before the first token appears.

**What is KV cache hit rate, and why does it matter?**

KV cache hit rate is the fraction of tokens that reuse a cached key-value pair instead of being recomputed from scratch. A higher hit rate means faster responses at lower cost, because less computation gets redone.

**What causes cold-start latency in LLM inference?**

Cold-start latency happens when zero replicas are running, and a new one has to boot up before it can serve a request. This step is handled by the Activator, which holds the request until the replica is ready.
