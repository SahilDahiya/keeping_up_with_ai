---
title: Proxying inference requests in 6ms with Pingora, Envoy, and Spanner
topic: inference
subtopic: serving
secondary_topics:
- infra-platform/deployment
summary: Explains low-latency inference proxying with Pingora, Envoy, and Spanner,
  including request-routing architecture.
source: modal
url: https://modal.com/blog/serverless-servers
author: null
published: '2026-06-25'
fetched: '2026-07-11T04:26:47Z'
classifier: codex
taxonomy_rev: 1
words: 2359
content_sha256: e61b089a6702ebd7fbd14fa36546d0deae95e55b301ae7b2417d990435952ad6
triage: keep
skip_reason: null
---

# Proxying inference requests in 6ms with Pingora, Envoy, and Spanner

[Back](https://modal.com/blog)

# Proxying inference requests in 6ms with Pingora, Envoy, and Spanner

[Charles Frye](https://twitter.com/charles_irl)

[Richard Gong](https://twitter.com/_gongy)

Modal makes it easy to run high-performance code in the cloud: Python functions, agent runtimes, notebooks, batch jobs, and more. Now, you can also run ultra-low-latency Servers on Modal for HTTP, WebSocket, and gRPC traffic.

```
@app.server(
    compute_region="us",
    routing_region="us-west",
)
class FileServer:
    @modal.enter()
    def start(self):
        import subprocess

        subprocess.Popen(["python", "-m", "http.server", "8000"])
```
Servers are designed for applications where every millisecond counts, like [LLM inference](https://modal.com/blog/introducing-auto-endpoints) for interactive agents. Servers give you a regionalized, autoscaling pool of HTTP server replicas behind Modal’s routing layer, with the deployment ergonomics, fast feedback loops, and autoscaling we consider table stakes ([for humans and for agents](https://modal.com/blog/agents-devex)).

This might sound familiar: with [Modal Web Functions](https://modal.com/docs/guide/webhooks), you could already expose HTTP endpoints on Modal. But Web Functions were [architected](https://modal.com/blog/serverless-http) for batteries-included robustness — queueing, retries, and a platform-managed request lifecycle — rather than bleeding-edge latency. As inference latencies have plummeted, it has become increasingly critical to remove latency in the happy path and push everything else to the application layer. Those few dozen milliseconds are [the difference between winning and losing](https://modal.com/blog/achieve-sota-specdec).

So we built an HTTP serving solution on Modal with minimum overhead without sacrificing core features. We reduced p50 latency from 39ms to 6ms:

### Request Latency

In this blog, we’ll explain how. The hard part was not accepting and routing HTTP traffic; Envoy can do that. The hard part was preserving Modal’s semantics — auth, dynamic replica placement, regional routing, autoscaling, inference features, and tenant isolation — without putting a control-plane lookup or queue in the hot path.

# What are Modal Servers for?

Modal Servers enable communication between your clients and a regionalized, autoscaling pool of HTTP server replicas on Modal via a [reverse proxy](https://www.cloudflare.com/learning/cdn/glossary/reverse-proxy/) routing system.

![](https://modal-cdn.com/blog/images/serverless-servers-regionalized-routing.webp)

Contrast that lightweight system (right below) with Modal Web Functions, which include an input plane that affords queueing and retries (left below).

![](https://modal-cdn.com/blog/images/serverless-servers-planes-input-vs-routing.webp)

To understand these architectures and their choices better, consider the differences between the [Transmission Control Protocol](https://datatracker.ietf.org/doc/html/rfc9293) (TCP) and the [User Datagram Protocol (UDP)](https://datatracker.ietf.org/doc/html/rfc9868). TCP provides Internet applications with a reliable, ordered byte stream. UDP provides a lower-latency primitive that requires applications to handle out of order/dropped datagrams. Neither is “better” in the abstract. They optimize for different things.

Some applications (e.g., GPU-to-GPU comms, video calling) build on UDP — [via RDMA over converged Ethernet (RoCE) v2](https://developer.nvidia.com/blog/oci-accelerates-hpc-ai-and-database-using-roce-and-nvidia-connectx/) or [via Web Real-Time Communication (WebRTC)](https://datatracker.ietf.org/doc/html/rfc8835). They achieve lower jitter/latency than TCP (cf the limited uptake of [iWARP](https://en.wikipedia.org/wiki/IWARP) RDMA-over-TCP). The tradeoff is reimplementing higher-layer reliability/ordering in an application-specific way (cf [“the end-to-end argument”](https://web.mit.edu/saltzer/www/publications/endtoend/endtoend.pdf)).

[Modal Web Functions](https://modal.com/blog/serverless-http) are closer to TCP: retries and queueing are built in, so clients don’t need to worry about them. Modal Servers are closer to UDP: requests take a lighter, lower-latency path, but applications must handle the rough edges. If no replica is available, clients get a [503 Service Unavailable](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Status/503)—the same response as if the service didn’t exist. Queueing and load-shedding (via 503s) are likewise pushed to the container application (for now!).

But in certain applications like low-latency LLM inference, it makes sense to make this trade.

*Aside: This difference isn’t literal, btw — you can serve UDP applications on Modal containers using either stack with UDP hole-punching, e.g. to *[drive a robot](https://modal.com/blog/physical-intelligence-runs-real-time-remote-inference-for-robotic-control-on-modal)* or *[detect objects in a webcam feed](https://modal.com/docs/examples/webrtc_yolo)*. But the engineering constraints, our choices, and your options are analogous.*

# Designing Modal Servers

At a high level, the routing layer for Modal Servers comprises a streaming edge proxy for I/O, an intelligent stateless proxy, and a compute load balancer. The stateless proxy is configured by a shared global state and the compute load balancer communicates with user containers and with the Autoscaler that creates and destroys them.

That looks something like this:

![](https://modal-cdn.com/blog/images/serverless-servers-arch-overview.webp)

Two principles governed every choice we made for and within this architecture:

- **Maximize resource sharing while minimizing interference**. We need to pool resources across tenants and requests (work-stealing, connection pooling, stream multiplexing) for aggregate performance, but we also need to provide the illusion of dedicated resources for correctness and per-tenant/per-request performance.
- **No network calls on the request path.**No metadata fetches, no KV store, no fallback to blob storage. That prevents us from handling queueing and retries at this layer (though we can layer it back on as an opt-in later). It requires us to materialize minimal state inside the routing layer while maintaining consistency.

The first principle is the most important and deserves some comment. A high-performance proxy naturally [organizes work around the resources it manages](https://dropbox.tech/infrastructure/how-we-migrated-dropbox-from-nginx-to-envoy): workers, connections, streams, buffers, and flow-control windows. But Modal’s serving path has a different set of boundaries that matter more to users and therefore to us: customer traffic to their HTTP Server replicas. Those are the boundaries where users define correctness and experience latencies.

When these two views do not line up, shared proxy resources can become shared fate. A connection pool is added as an optimization, but becomes the determinant of which requests interfere under load. A queue is added to buffer but becomes an implicit scheduler. A flow-control window starts as a transport detail but at scale defines how backpressure composes across streams. So there wasn’t really “one weird trick to make your latency go down”. Instead, it was a series of microscopic adjustments to align resource use with our macroscopic goals.

# How do Modal Servers work?

The resulting implementation looks like this:

![](https://modal-cdn.com/blog/images/serverless-servers-arch-diagram-detail.webp)

The core of the routing system runs in our [AWS Elastic Kubernetes Service](https://aws.amazon.com/eks/). As we’re fond of saying, Kubernetes wasn’t built for inference — but it *was* built for scaling high-availability distributed proxies. In contrast, the user containers and the [custom container runtime supporting them](https://modal.com/blog/truly-serverless-gpus) are managed by our scheduling system, not Kubernetes, and they run on dozens of clouds [all around the world](https://modal.com/docs/guide/region-selection).

In the following, we walk through the life of a request in this system.

## Clients request a resource backed by Modal Servers

The resource is identified by a URL like `https://[domain].[routing_region].modal.direct/[path]`.

- The `[domain]`component identifies a specific Modal Server (aka autoscaling pool of containers)
- The `[routing_region]`picks out a regionalized deployment of the proxy system (together, the deployments form our Routing Plane)
- `modal.direct`
- The `[path]`component identifies the resource on the server — along with bodies and query parameters, that’s how users interact with your business logic

We connect to clients via an [AWS NLB](https://aws.amazon.com/elasticloadbalancing/network-load-balancer/), an L4 proxy. Because it operates at L4 (here, TCP) instead of L7 (HTTP), it can’t implement features at L7, so it’s kept as a simple load balancer.

## Envoy convert requests to h2 streams

The first L7 features are implemented by the streaming edge proxy, for which we use [Envoy](https://www.envoyproxy.io/). This component terminates TLS, so that we can communicate without it inside of our VPC and so that we can manipulate headers. It also normalizes all HTTP traffic to HTTP/2.

With HTTP/2, we can multiplex client streams onto a single TCP connection, drawn from a pool. Pooling here reduces latency and multiplexing controls the total resource demand — scaling with total load, rather than directly with client cardinality. But the contention introduced between different clients on the same connection required deep scrutiny.

## fprs, our in-house proxy, maps client streams onto Server replicas

At an architectural level, the next goal is to map the `domain` in the URL to a particular user-deployed Modal Server application (”domain association”) and to load balance across that application’s replicas in Modal’s Compute Plane. The majority of non-routing features are implemented at this layer.

Envoy is engineered for excellent performance, but it did not allow us to implement these features. Because we could not deliver a product without them, we kept Envoy at the edge and chose to build our own system for domain association and load-balancing into which we could inject core features.

We love [going deep and building things in-house](https://modal.com/blog/truly-serverless-gpus), but we didn’t make this decision lightly. We were focused on supporting LLM inference, but not to the exclusion of other workloads, so we couldn’t use a system like [NVIDIA Dynamo](https://github.com/ai-dynamo/dynamo) or [llm-d](https://llm-d.ai/docs/getting-started). We have lots of production experience operating [AWS NLB](https://aws.amazon.com/elasticloadbalancing/network-load-balancer/) and [nginx](https://nginx.org/), but we needed a distinct feature set — for instance, handling rapid churn in upstreams as users create & destroy services (and services create & destroy replicas).

### fprs makes it easy for us to ship what we need

We built `fprs` using the excellent [pingora](https://github.com/cloudflare/pingora) library from CloudFlare. We are fairly seasoned Rustaceans, so we felt comfortable bringing this into our stack and operating it at scale. As the creators note in [their blog](https://blog.cloudflare.com/pingora-open-source/), the underlying Tokio runtime is a great fit for a streaming, multiplexed HTTP proxy. Work-stealing inside Rust’s lightweight, in-thread coroutine concurrency model elegantly separates shared resources from shared fates.

That said, we had some work to do to achieve pingora’s tight tail latencies in our unique use case. For instance, we turn over domains far faster than is typical. When we investigated some occasional stalls, we determined that there was a hidden DNS resolution path triggered by this turnover and which we needed to carefully cache.

We designed this proxy to be stateless so that it would be easy to scale up and down. But configuration is state. And included in that configuration here are `url: host` mappings, which change rapidly. Misconfiguration is [an easy way to take down a proxy service](https://blog.cloudflare.com/5-december-2025-outage/), so we wanted to make sure we got this right. We read configuration state from [Spanner](https://static.googleusercontent.com/media/research.google.com/en//archive/spanner-osdi2012.pdf), a globally replicated database.

We don’t read from Spanner on every request of course. Sticking with our design principle of avoiding network calls on the hot path, we maintain an in-memory cache of domain associations. That cache is concurrently reconciled with the global state via a [change stream](https://docs.cloud.google.com/spanner/docs/change-streams) (Spanner’s external consistency guarantees came in handy here).

With performance and routing handled, we could add our key features.

#### Autoscaling metrics

This layer also emits metrics to the Modal Autoscaler, which decides whether to create new containers to handle increased load (or to spin them down when no longer needed).

Autoscalers need a signal and an algorithm. The signal emitted by the routing layer is the per-container in-flight request count, based on (logical) connection counting. The algorithm is to increase/decrease the container count when the average count of connections exceeds/falls below the user-specified `target_concurrency`, subject to a `scaleup_`/`scaledown_window`.

#### Proxy auth

We also need routing layer auth. User services can implement auth themselves, but that only takes affect after at least one replica starts and can process requests. If you need to spin up eight B200s drawing a kilowatt of power each just to reply [ 401 Unauthorized](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Status/401) in response to a few bytes of HTTP traffic, you are handing leverage to a denial-of-service attacker.

So we implement [proxy auth](https://modal.com/docs/guide/webhook-proxy-auth) to block these requests at the routing layer, before they reach user containers.

#### Mirroring

Inference systems are the end products of machine learning systems. Machine learning systems have some unique needs from other systems. Most notably, they care deeply about the semantics of the data they are run on and their behavior in production is hard to predict. For this reason, understanding user data in production is critical, and so we support mirroring as a first-class feature.

A simple case is A/B testing. As with UI changes, sometimes the only thing to be done to assess a change in an ML system is to test in production, ideally with a randomized controlled trial, aka an A/B test. With inference systems, it is often sufficient for this traffic to shadow production, via a mirror.

Another mirroring use case we are excited about is continual learning. ML systems get better with more data. We’ve directly seen this for inference system performance via [our training of custom speculator models for inference acceleration](https://modal.com/blog/achieve-sota-specdec). It’s also a critical part of the loop for continual improvement of model quality — a fact we expect more of the industry to become aware of as they move towards open-weights inference in light of recent drama in the world of proprietary model services.

## Workers in the compute plane relay HTTP requests to container

Requests forwarded by `fprs` reach container runtime workers in Modal’s Compute Plane. This container runtime wraps user containers and provides their runtime semantics. The Compute Plane comprises everything from common-and-garden CPU servers to refrigerator-sized NVLink racks operated by everyone from hyperscalers who invented cloud computing to neoclouds who pivoted from crypto and only just got good enough to pass [our quality evaluations](https://modal.com/blog/gpu-health).

These workers speak HTTP/2 to `fprs`. They speak HTTP/2 to user servers that support it, but can switch to HTTP/1 if needed — without impacting the HTTP/2 streams in the rest of our system. The worker also handles graceful draining for containers by tracking request completion.

## The path runs in reverse to return responses to client.

Each component of the system (after the AWS NLB) is an HTTP server, and so they must return a response to their client, in reverse order, until we reach the original client. The whole process completes in 5-7ms. This feels like a good moment to admire the power of computing and networking. All of the work described above can be done faster than [a neural impulse can travel down your leg](https://en.wikipedia.org/wiki/Nerve_conduction_velocity).

# Why build this?

In an era of vibe-coding and ephemeral software, Modal still believes in the power of fundamental building blocks. These high quality, reusable, composable components can be used to build new services and unlock new workloads for us and our users. If anything, the strength and efficiency of core infrastructure becomes more important as machines allow us to create more software, more cheaply, to better serve the needs of end users.

Servers are a new addition to Modal’s primitives. They are available to users [directly via our SDK](https://modal.com/docs/guide/servers). We expect a certain class of users to take that and run with it — as [some already have](https://modal.com/blog/achieve-sota-specdec)!

But they are also consumed as a component by our [new Endpoints product](https://modal.com/docs/guide/endpoints), which [makes serving LLM inference at state-of-the-art performance effortless](https://modal.com/blog/introducing-auto-endpoints).

If you’re interested in tackling tough infrastructure problems and building strong bones, [we’re hiring](https://modal.jobs).
