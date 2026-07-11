---
title: 'Lambda on hard mode: Inside Modal''s web infrastructure'
topic: infra-platform
subtopic: deployment
secondary_topics:
- product-engineering/architecture
summary: Deep dive into Modal web infrastructure, including serverless HTTP routing,
  isolation, and platform architecture.
source: modal
url: https://modal.com/blog/serverless-http
author: null
published: '2024-03-14'
fetched: '2026-07-11T04:30:37Z'
classifier: codex
taxonomy_rev: 1
words: 4003
content_sha256: f3991030ac5dd6cead3f8434886987a40de209d3a1092515a84c751b10b399bc
triage: keep
skip_reason: null
---

# Lambda on hard mode: Inside Modal's web infrastructure

[Back](https://modal.com/blog)

# Lambda on hard mode: Inside Modal's web infrastructure

[Eric Zhang](https://twitter.com/ekzhang1)

At Modal, we built an HTTP and WebSocket stack on our platform. In other words, your serverless functions can take web requests.

This was tricky! HTTP has quite a few edge cases, so we used Rust for its speed
and to help manage the complexity. But even so, it took a while to get right. We
recently wrapped up this feature by introducing [full WebSocket support](https://modal.com/blog/websocket-launch) (real-time bidirectional
messaging).

We call this service `modal-http`, and it sits between the Web and our core
runtime.

![Simple schematic with modal-http at the center](https://modal-cdn.com/cdnbot/modal-http-20.png)



You can deploy a simple [Web Function](https://modal.com/docs/guide/webhooks) to a `*.modal.run` URL by running some Python code:

```
import modal
app = modal.App(name="small-app")
@app.function()
@modal.fastapi_endpoint(method="GET")
def my_handler():
    return {
        "status": "success",
        "data": "Hello, world!",
    }
```
(*This takes  0.747 seconds to deploy today.*)

But you can also run a much larger compute workload. For example, to set up a data-intensive video processing endpoint:

```
import modal
from .my_video_library import Video, do_expensive_processing
app = modal.App(name="big-app")
# 30 minutes, 8 CPUs, 32 GB of memory
@app.function(timeout=1800, cpu=8, memory=32 * 1024)
@modal.fastapi_endpoint(method="POST")
def my_handler(video_data: Video):
    # Process the video
    edited_video = do_expensive_processing(video_data)
    # Return it as a response
    return edited_video
```
This post is about the behind-the-scenes of serving a Web Function on Modal. How does your web request get translated into an autoscaling serverless invocation?

What makes our HTTP/WebSocket implementation particularly interesting is its
lack of limits. Serverless computing is [traditionally understood](https://www2.eecs.berkeley.edu/Pubs/TechRpts/2019/EECS-2019-3.pdf) to prioritize small, lightweight tasks, but Modal can’t compromise on speed or
compute capacity.

When resource limits are removed, handling web requests gets proportionally more difficult. Users may ask to upload a gigabyte of video to their machine learning model or data pipeline, and we want to help them do that! We can’t just say, “sorry, either make your video 200x smaller or split it up yourself.” So we had a bit of a challenge on our hands.

## “Lambda on hard mode”

Serverless function platforms have constraints. A lot of them, too!

- Functions on [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html)are limited to 15-minute runs and 50 MB images. As of 2024, they can only use 3 CPUs (6 threads) and 10 GB of memory. Response bandwidth is 16 Mbps.
- [Google Cloud Run](https://cloud.google.com/run/quotas)is a bit better, with 4 CPUs and 32 GB of memory, plus 75 Mbps bandwidth.
- [Cloudflare Workers](https://developers.cloudflare.com/workers/platform/limits/)are the most restricted. Their images can only be 10 MB in size and have 6 HTTP connections. Execution is limited to 30 seconds of CPU time, 128 MB of memory.

But modern compute workloads can be [much more demanding](https://modal.com/examples): training
neural networks, rendering graphics, simulating physics, running data pipelines,
and so on.

Modal containers can each use up to **64 CPUs**, **336 GB of memory**, and **8
Nvidia H100 GPUs**. And they may need to download up to **hundreds of
gigabytes** of model weights and image data on container startup. As a result,
we care about having them spin up and shut down quickly, since having any idle
time is expensive. We scale to zero and bill [by the second](https://modal.com/pricing).

As a user, this is freeing. I often get questions like, “does Modal have enough
compute to run my [fancy bread-baking simulation](https://modal.com/docs/examples/blender_video)”
— and I tell them, are you kidding? You can spin up dozens of 64-CPU containers
at a snap of your fingers. Simulate your whole bakery!

In summary: Modal containers are potentially long-running and compute-heavy, with big inputs and outputs. This is the opposite of what “serverless” is usually good at. How can we ensure quick and reliable delivery of HTTP requests under these conditions?

### A distributed operating system

Let’s take a step back and review the concept of serverless computing. Run code in containers. Increase the number of containers when there’s work to be done, and then decrease it when there’s less work. You can imagine a factory that makes cars: when there are many orders, the factory operates more machines, and when there are fewer orders, the factory shifts its focus. (Except in computers, everything happens faster than in a car factory, since they’re processing thousands of requests per second.)

This isn’t unique to serverless computing; it’s how most applications scale today. If you deploy a web server, chances are you’d use a PaaS to manage replicas and scaling, or an orchestrator like Kubernetes. Each of these offerings can be conceptualized by a two-part schematic:

- **Autoscaling:**Write code in a stateless way, replicate it, then track how much work needs to be done via latency, CPU, and memory metrics.
- **Load balancing:**Distribute work across many machines and route traffic to them.

Together autoscaling and load balancing constitute a kind of analogue to an *operating system* in the distributed services world: something that manages
compute resources and provides a common execution environment, allowing software
to be run.

Although a unified goal, there are many approaches. (A lot of [ink](https://research.google/pubs/maglev-a-fast-and-reliable-software-network-load-balancer/) [has](https://aosabook.org/en/v2/nginx.html) [been](https://www.eecs.harvard.edu/~michaelm/postscripts/mythesis.pdf) [spilled](https://github.com/tangchq74/papers/blob/fad260ab66567e843e5ad6e238f7051ffe384e8a/XFaaS-SOSP23-Final.pdf) on load balancing in particular.) Here’s a brief summary to illustrate how this
schematic maps onto a few popular deployment systems. We’re in good company!

| System (release date) | Autoscaling | Load balancing |
|---|---|---|
| Heroku (2009) | By p95 latency | HTTP reverse proxy |
| Kubernetes (2014) | Resource metrics (custom) | Custom reverse proxy and/or load balancer |
| AWS Lambda (2014) | Traffic | HTTP reverse proxy |
| Azure Functions (2016) | Traffic | HTTP reverse proxy |
| AWS Fargate (2017) | Resource metrics (custom) | HTTP/TCP/UDP load balancer |
| Render (2019) | CPU/memory target | HTTP reverse proxy |
| Google Cloud Run (2019) | Traffic and CPU target | HTTP reverse proxy |
| Fly.io (2020) | Traffic (custom) | HTTP/TCP/TLS proxy, by distance and load |
| Modal (2023) | Traffic (custom) | Translate HTTP to function calls |

So… I spot a difference there. Hang on a second. I want to talk about Modal’s HTTP ingress.

### Translating HTTP to function calls

You might notice that setting up an HTTP reverse proxy in front of serverless functions is a popular option. This means that you scale up your container, and some service in front handles TLS termination and directly forwards traffic to a backend server. For most of these platforms, HTTP is the main way you can talk to these serverless functions, as a network service.

But for Modal, we’re focused on building a platform based on the idea that
serverless functions are just *ordinary functions* that you can call. If you
want to define a function on Modal, that should be easy! You don’t need to set
up a REST API. Just call it directly with `.remote()`.

```
from modal import App
from PIL import Image
app = App()
@app.function()
def compute_embeddings(image: Image) -> list[int]:
    return my_ml_model.run(image)
@app.function()
def run_batch_job(image_names: list[str]) -> None:
    for name in image_names:
        image = fetch_image(name)
        vec = compute_embeddings.remote(image)  # invoke remote function
        print(vec)
```
Since `run_batch_job()` can be invoked in any region, and `compute_embeddings()` can be called remotely from it, we needed to build generic high-performance
infrastructure for serverless *function calls*. Like, actually “calling a
function.” Not wrapping it in some REST API.

Calling a function is a bit different from handling an HTTP request. There’s a mismatch if you try to conflate them! By supporting both of these workloads, we can:

- Use a faster, optimized path (for calls between functions) that can be location and data cache-aware, rather than relying on the same HTTP protocol.
- Fully support real-time streaming in network requests, rather than limiting it to fit the use case of a typical function call.
- Offer first-class support for complex heterogeneous workloads on CPU and GPU.

Modal’s bread and butter is systems engineering for heavy-duty function calls. We’re already focused on making that fast and reliable. As a result, we decided to handle web requests by translating them into function calls, which gives us a foundation of shared infrastructure to build upon.

## Understanding the HTTP protocol

To understand how HTTP gets turned into a function calls, first we need to
understand HTTP. HTTP follows a request-response model. Here’s what a typical
flow looks like. On the top, you can see a standard `GET` request with no body,
and on the bottom is a `POST` request with body.

**Note:** HTTP GET requests can technically have bodies too, though they should
be ignored. Also, a less-known fact is that request and response bodies can be
interleaved, [sometimes even in HTTP/1.1](https://datatracker.ietf.org/doc/html/rfc6202)!

![Diagram of two requests, HTTP GET on top and HTTP POST on the bottom](https://modal-cdn.com/cdnbot/modal-http-10.png)



The client sends some headers to the server, followed by an optional body. Once the server receives the request, it does some processing, then responds in turn with a set of a headers and its own response body.

Both the client and server directions are sent over a specific wire protocol, which varies between HTTP versions. For example, HTTP/1.0 uses a TCP stream for each request, HTTP/1.1 added keepalive support, HTTP/2 has concurrent stream multiplexing over a single TCP stream, and HTTP/3 uses QUIC (UDP) instead of TCP. They’re all unified by this request-response model.

Here’s what an HTTP/1.1 GET looks like, as displayed by `curl` in verbose mode.
The `>` lines are request headers, the `<` lines are response headers, and the
response body is at the end:

```
$ curl -v http://example.com
*   Trying 93.184.216.34:80...
* TCP_NODELAY set
* Connected to example.com (93.184.216.34) port 80 (#0)
> GET / HTTP/1.1
> Host: example.com
> User-Agent: curl/7.68.0
> Accept: */*
>
* Mark bundle as not supporting multiuse
< HTTP/1.1 200 OK
< Accept-Ranges: bytes
< Age: 521695
< Cache-Control: max-age=604800
< Content-Type: text/html; charset=UTF-8
< Date: Fri, 23 Feb 2024 17:22:54 GMT
< Etag: "3147526947+gzip"
< Expires: Fri, 01 Mar 2024 17:22:54 GMT
< Last-Modified: Thu, 17 Oct 2019 07:18:26 GMT
< Server: ECS (cha/8169)
< Vary: Accept-Encoding
< X-Cache: HIT
< Content-Length: 1256
<
<!doctype html>
<html>
<head>
    <title>Example Domain</title>
    <!-- note: head contents omitted for brevity -->
</head>
<body>
<div>
    <h1>Example Domain</h1>
    <p>This domain is for use in illustrative examples in documents. You may use this
    domain in literature without prior coordination or asking for permission.</p>
    <p><a href="https://www.iana.org/domains/example">More information...</a></p>
</div>
</body>
</html>
* Connection #0 to host example.com left intact
```
To iron out the differences between HTTP protocol versions, we needed a backend
data representation for the request. In a reverse proxy, the backend protocol
would just be HTTP/1.1, but in our case that would add additional complexity for
reliably reconnecting TCP streams and parsing the wire format. We instead
decided to base our protocol on a stream of *events*.

Luckily, there was already a well-specified protocol for representing HTTP as
event data: [ASGI](https://github.com/django/asgiref), typically used as a
standard interface for web frameworks in Python.

**Note:** ASGI was made for a different purpose! Usually the web server and
ASGI application run on the same machine. Here we’re using it as the internal
communication language for a distributed runtime. So we adjusted the protocol to
our use case by serializing events as binary Protocol Buffers.

ASGI doesn’t support every internal detail of HTTP (e.g., gRPC servers need access to HTTP/2 stream IDs), but it’s a common denominator that’s enough for web apps built with all the popular Python web frameworks: Flask, Django, FastAPI, and more. That’s a lot of web applications, and the benefit of this maturity is that it lets us greatly simplify our model of HTTP serving.

Here’s what a POST request looks like in ASGI. The blue arrows represent client events, while the green arrows are events sent from the server.

![Diagram of an HTTP POST request with events marked](https://modal-cdn.com/cdnbot/modal-http-11.png)



- At the start of a request, when headers are received, we begin by parsing the
headers to generate a *function input*via the`http`request scope. This triggers a new function call, which is scheduled on a running task according to availability and locality.
- Then, the request body is streamed in, and we begin reading it in chunks to
produce real-time `http.request`events that are sent to the serverless function call. If the server falls behind, backpressure is propagated to the client via TCP (for HTTP/1.1) or HTTP/2 flow control.
- The function starts executing immediately after getting the request headers, then begins reading the request body. It sends back its own headers and status code, followed by the response body in chunks.
- The request-response cycle finishes, optionally with HTTP trailers.

In this way, we’re able to send an entire HTTP request and response over a generic serverless function call. And it’s efficient too, with proper batching and backpressure. We don’t need to establish a single TCP stream or anything; we can use reliable, low-latency message queues to send the events.

Unlike AWS Lambda’s 6 MB limit for request and response bodies, this architecture lets us support request bodies of up to 4 GiB (682x bigger), and streaming response bodies of unlimited size.

Of course, although conceptually simple, it’s still a pretty tricky thing to
implement correctly since there are a lot of concurrent moving parts. Our
implementation is in Rust, based on the [hyper](https://hyper.rs/) HTTP server
library and [Tokio](https://tokio.rs/) async runtime. Here’s a snippet of the
code that buffers the request body in chunks of up to 1 MiB in size, or waits
for 2 milliseconds of duration.

```
/// Stream an HTTP request body into the `data_in` channel for a web
/// endpoint. This function also sends `http.disconnect` when the request
/// finishes, or the HTTP client disconnects.
async fn stream_http_request_body(
    &self,
    function_call_id: &str,
    mut body: hyper::Body,
    disconnect_rx: oneshot::Receiver<()>,
) -> Result<()> {
    let asgi_body = |body, more_body| Asgi {
        r#type: Some(asgi::Type::HttpRequest(asgi::HttpRequest {
            body,
            more_body,
        })),
    };
    let asgi_disconnect = Asgi {
        r#type: Some(asgi::Type::HttpDisconnect(asgi::HttpDisconnect {})),
    };
    let (tx, mut rx) = mpsc::channel(16); // Send at most 16 chunks at a time.
    tokio::spawn(async move {
        let body_buffer_time = Duration::from_millis(2);
        let body_buffer_size = 1 << 20; // 1 MiB
        let mut last_put = Instant::now();
        let mut current_segments = Vec::new();
        let mut current_size = 0;
        while let Some(result) = body.next().await {
            let Ok(buf) = result else {
                // If the request fails, send a disconnection immediately.
                tx.send(asgi_disconnect).await?;
                return Ok(());
            };
            if buf.is_empty() {
                continue;
            }
            current_size += buf.len();
            current_segments.push(buf);
            if current_size > body_buffer_size || last_put.elapsed() > body_buffer_time {
                let message = asgi_body(Bytes::from(current_segments.concat()), true);
                current_segments.clear();
                current_size = 0;
                tx.send(message).await?;
                last_put = Instant::now();
            }
        }
        // Final message, possibly empty.
        let message = asgi_body(Bytes::from(current_segments.concat()), false);
        tx.send(message).await?;
        // Wait for a client disconnect signal (or for the response to finish sending),
        // then forward that to the data channel.
        match disconnect_rx.await {
            Ok(()) => {}
            _ => tx.send(asgi_disconnect).await?, // => RecvError
        };
        anyhow::Ok(())
    });
    let mut index = 1;
    let mut messages = Vec::new();
    while rx.recv_many(&mut messages, 16).await != 0 {
        self.put_data_in(function_call_id, &mut index, &messages)
            .await?;
        messages.clear();
    }
    anyhow::Ok(())
}
```
You might have noticed the `disconnect_rx` channel used in the snippet above.
This hints at one of the realities of making reliable distributed systems that
we glossed over: needing to thoroughly handle failure cases everywhere, all the
time.

### Edge cases and errors

First, if a client sends an HTTP request but exits in the middle of sending the body, then we propagate that disconnection to the serverless function.

![Diagram of a disconnected HTTP request](https://modal-cdn.com/cdnbot/modal-http-12.png)



We reify this using an ASGI `http.disconnect` event, which allows the user’s
code to stop executing gracefully. Otherwise, we might have a function call
that’s still running even after the user has canceled their request.

Another issue is if the server has a failure. It might throw an exception, crash due to running out of memory, hit a user-defined timeout, be preempted if on a spot instance, and so on. If a malicious user is on the system, they also might send malformed response events, or events in the wrong order!

We keep track of any violations and display an error message to the user. Rust’s pattern matching and ownership help with managing the casework.

### Dealing with HTTP idle timeouts

Okay, so if we had been a standard runtime, we would be done with HTTP now. But we’re still not done! There’s one more thing to consider: long-running requests.

If you make an HTTP request and the server doesn’t respond for 300 seconds, then Chrome cancels the request and gives you an error. This is not configurable. Other browsers and pieces of web infrastructure have varying timeouts. Our users often end up running expensive models that take longer than 5 minutes, so we need a way to support long-running requests.

Luckily, there’s a solution. After 150 seconds (2.5 minutes), we send a temporary “303 See Other” redirect to the browser, pointing them to an alternative URL with an ID for this specific request. The browser or HTTP client will follow this redirect, ending their current stream and starting a new one.

Browsers will follow up to 20 redirects for a link, so this effectively [increases the idle timeout to 50 minutes](https://modal.com/docs/guide/webhook-timeouts).
An example of this in action is shown below, with a single redirect.

![Diagram of a long-running request with one 303 See Other response](https://modal-cdn.com/cdnbot/modal-http-13.png)



Is this behavior a little strange? Yes. But it just works “out-of-the-box” for a lot of people who have Web Functions that might execute for a long time. And if your function finishes processing and begins its response in less than 2.5 minutes, you’ll never notice a difference anyway.

For people who need to have very long-running web requests, Modal *just works*.

### WebSocket connections

That’s it for HTTP. What if a user makes a WebSocket connection? Well, the
WebSocket protocol works by starting an HTTP/1.1 connection, then establishing a *handshake* via HTTP’s connection upgrade mechanism. The [handshake](https://datatracker.ietf.org/doc/html/rfc6455#section-1.2) looks
something like this:

```
> GET /ws HTTP/1.1
> Host: my-endpoint.modal.run
> Upgrade: websocket
> Connection: Upgrade
> Sec-WebSocket-Key: dGhlIHNhbXBsZSBub25jZQ==
> Sec-WebSocket-Version: 13
>
< HTTP/1.1 101 Switching Protocols
< Upgrade: websocket
< Connection: Upgrade
< Sec-WebSocket-Accept: s3pPLMBiTxaQ9kYGzzhZRbK+xOo=
```
**Note:** There is also another version of the WebSocket protocol that
bootstraps from HTTP/2, but it’s not supported by many web servers yet. For now,
you need a dedicated TCP connection.

The `Sec-WebSocket-Key` header is random, while `Sec-WebSocket-Accept` is
derived from an arbitrary hash function on the key. (This is just some protocol
junk that we had to implement, see [RFC 6455](https://datatracker.ietf.org/doc/html/rfc6455).) ASGI has a separate [WebSocket interface](https://asgi.readthedocs.io/en/latest/specs/www.html#websocket) that encodes this handshake into a pair of `websocket.connect` and `websocket.accept` events, so we translated our incoming request into those
events.

After the handshake, all of the infrastructure is already in place, and we
transmit messages between `modal-http` and the serverless function via data
channels in the same way as we did for HTTP.

![Diagram of a WebSocket connection](https://modal-cdn.com/cdnbot/modal-http-14.png)



Our server-side Rust implementation is based on hyper as before, but it upgrades
the connection to an asynchronous [tokio-tungstenite](https://github.com/snapview/tokio-tungstenite) stream once
the handshake is accepted.

## Building on open-source infrastructure

We’ve built a lot of infrastructure to support HTTP and WebSocket connections, but we didn’t start from scratch. The Rust ecosystem was invaluable to making this custom network service, which needed to be high-performance and correct.

But while we’ve talked a lot about the serverless backend and design choices
made to support heavy workloads, we haven’t talked yet about how requests
actually *get* to `modal-http`. For this part, we relied on boring, mature
open-source cloud infrastructure pieces.

Let’s still take a look though. Modal Web Functions run on the wildcard domain `*.modal.run`, as well as on [custom domains](https://modal.com/docs/guide/webhook-urls#custom-domains) as assigned by users
via a CNAME record to `cname.modal.domains`. The most basic way you’d deploy a
Rust service like `modal-http` is by pointing a [DNS record](https://en.wikipedia.org/wiki/Domain_Name_System) at a running
server, which has the compiled binary listen on a port.

![A browser sends a request to modal-http](https://modal-cdn.com/cdnbot/modal-http-0.png)



Rust is pretty fast, so this is a reasonable design for most real-world services. A single node nevertheless doesn’t scale well to the traffic of a cloud platform. We wanted:

- **Multiple replicas.**Replication of the service provides fault tolerance and eases the process of rolling deployments. When we rollout a new version, old replicas need a gradual timeout.
- **Encryption.**Support for TLS is missing here. We- *could*handle it in the server directly, but rather than reinventing the wheel, it’s easier and safer to rely on well-vetted software for TLS termination. (We also need to allocate- [on-demand certificates](https://caddyserver.com/docs/automatic-https#on-demand-tls)for custom domains.)

So, rather than the simplified flow above, our actual ingress architecture to `modal-http` looks like this. We placed a TCP network load balancer in front of
a [Kubernetes](https://kubernetes.io/) cluster, which runs a [Caddy](https://caddyserver.com/docs/) deployment, as well as a separate
deployment for `modal-http` itself.

![Full path of a request through L4 NLB and Caddy](https://modal-cdn.com/cdnbot/modal-http-1.png)



Note that none of our *serverless functions* run in this Kubernetes cluster.
Kubernetes isn’t well-suited for the workloads we described, so we wrote our own
high-performance serverless runtime based on [gVisor](https://gvisor.dev/), our
own file system, and our own job scheduler — which we’ll talk about another
time!

But Kubernetes is still a rock-solid tool for the more traditional parts of our cloud infrastructure, and we’re happy to use it here.

### Caveat: Multi-region request handling

It’s a fact of life that light takes time to travel through fiber-optic cables
and routers. Ideally, `modal-http` should run on the edge in geographically
distributed data center regions, and requests should be routed to the nearest
replica. This is important to minimize baseline latency for web serving.

We’re not there yet though. It’s early days! While our serverless functions are
already running in many different clouds and data centers based on *compute
availability*, since GPUs are scarce, our actual servers only run in Ashburn,
Virginia for now.

This is a bit of a tradeoff for us, but it’s not a fundamental one. It gives us
more flexibility at the moment, although `modal-http` will be deployed to more
regions in the future for latency reasons. Right now heavyweight workloads on
Modal probably aren’t affected, but for very latency-sensitive workloads (under
100 ms), you’ll likely want to specify your container to run in Ashburn.

## Lessons learned

So, there you have it. Serverless functions are traditionally limited to a request-response model, but Modal just released full support for WebSockets, with GPUs and fully managed autoscaling. And we did this by translating web requests into function calls.

Our service, `modal-http`, is written in Rust and based on several components
that let us handle HTTP and WebSocket requests at scale. We’ve placed it behind
infrastructure to handle the ingress of requests, and we’re planning to expand
to more regions in the future.

Some may wonder: If Modal translates HTTP to this message format, wouldn’t that
stop people from being able to use the traditional container model of [ EXPOSE](https://docs.docker.com/reference/dockerfile/#expose)-ing TCP ports?
This is a good question, but it’s not a fundamental limitation. The events can
be losslessly translated back to HTTP on the other end! We
wrote examples of this for systems like ComfyUI, and we’re

[building it into the runtime](https://github.com/modal-labs/modal-client/pull/1513)with just a bit of added code.

We’ve already been running Rust to power our serverless runtime for the past two
years, but `modal-http` gives us more confidence to run standard Rust services
in production. Just for comparison, when we first introduced this system to
replace our previous Python-based ingress, the number of `502 Bad Gateway` errors in production decreased by 99.7%, due to clearer error handling and
tracking of request lifetimes. And it laid the groundwork for WebSocket support
without fundamental changes.

Today, Web Functions and remote function calls on Modal use a common system. Having uniformity allows us to focus on impactful work that makes our cloud runtime faster and lower-priced, while improving security and reliability over time.

## Acknowledgements

Thanks to the Modal team for their feedback on this post. Special thanks to
Jonathon Belotti, Erik Bernhardsson, Akshat Bubna, Richard Gong, and Daniel
Norberg for their work and design discussions related to `modal-http`.

If you’re interested in fast, reliable, and heavy-duty systems for the cloud, [Modal is hiring](https://modal.com/company).
