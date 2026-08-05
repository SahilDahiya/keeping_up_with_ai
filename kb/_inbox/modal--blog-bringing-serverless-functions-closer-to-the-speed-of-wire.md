---
title: Bringing serverless functions closer to the speed of wire | Modal Blog
kind: blog
topic: null
subtopic: null
secondary_topics: []
summary: null
triage: null
skip_reason: null
source: modal
url: https://modal.com/blog/bringing-serverless-functions-closer-to-the-speed-of-wire
author: null
published: '2026-08-04'
fetched: '2026-08-05T06:52:34Z'
classifier: null
taxonomy_rev: 2
words: 1190
content_sha256: ce8669d118cab837c60cc480b487d46d2235afcd8bcfec1bf5b0dd5c94adf163
---

# Bringing serverless functions closer to the speed of wire | Modal Blog

[Back](https://modal.com/blog)

# Bringing serverless functions closer to the speed of wire

![Function Call network hops through our legacy us-east I/O servers (left) vs. our new regional I/O servers (right).](https://modal-cdn.com/cdnbot/daniel_blog_1uoj0r_5x_c8a9a56d.webp) 

On Modal, you’ve always had control over [which region](https://modal.com/docs/guide/region-selection#specifying-a-container-region) your containers run in. However, every [Function](https://modal.com/docs/sdk/py/latest/modal.Function)’s inputs and outputs would always get routed through our servers (a.k.a. the I/O plane) in us-east—potentially adding up to a few 100ms of [network latency](https://www.cloudping.co/) to each [Function Call](https://modal.com/docs/sdk/py/latest/modal.FunctionCall) depending on the caller and container regions.

Say you’re running a tiny embedding model for your [RAG app](https://modal.com/docs/examples/potus_speech_qanda#retrieval-augmented-generation-rag-for-question-answering-with-langchain) that has <50ms of inference time because it’s in the hot path of page loads. For your users in Europe—assuming the processing is done on containers in the EU for data residency reasons—the ~200ms spent on the network roundtrips to us-east would dominate the cost of running the embedding model. This is far from ideal (foreshadowing…).

Over the past few months, we’ve developed a faster and geographically distributed I/O plane. As with our [Modal Servers](https://modal.com/blog/serverless-servers), the new I/O plane is available in ≥4 regions—the [`routing_region` Function flag](https://modal.com/docs/guide/region-selection#regional-routing) lets you specify which one to route your Function’s inputs and outputs through.

```
@app.function(
    region="eu",  # Containers will run here.
    routing_region="eu-west",  # Requests will route through here.
)
def hello_faster_world(name: str) -> str:
    return f"Hello, {name}"
```
This week, we’ve completed the migration of all Functions running on Modal to use the new I/O plane in us-east. End-to-end Function Call latencies have dropped by roughly 80ms at p50. Enjoy the speed up!

# Life of a Function Call

When you call `.remote()` on a Modal Function, your client serializes the input payload and sends it to our I/O plane. The client then immediately polls the I/O plane, waiting some amount of time each poll for the serialized output to become available. Once fetched, the client deserializes the output payload.

Meanwhile, the I/O plane stores and queues the input in a pending state in [Redis](https://redis.io/). Containers with available capacity (as defined by their [input concurrency](https://modal.com/docs/guide/concurrent-inputs#input-concurrency)) constantly fetch inputs for processing from the queue, marking them as running. Once on the container, the input is deserialized and processed by the Function code. When the processing is done, the output is serialized and written to Redis, and the input is removed from the queue.

![](https://modal-cdn.com/cdnbot/daniel_blog_2wrccevp4_84c58b2b.webp) 

Since the client is constantly communicating with the I/O plane by polling for the output, if [something goes wrong](https://modal.com/docs/guide/retries#failures-and-retries) with processing (i.e. server failure, container failure, or retriable user code failure), the client will find out quickly and automatically retry the input.

Off the hot path of input processing:

- The I/O plane sends autoscaling information (e.g. running inputs, input backlog size, average execution time, etc.) about each Function to Modal’s control plane. This feeds into our scheduler, which uses the data to determine how many containers should be brought up or spun down.
- The I/O plane reports input processing events to power the dashboard and [o11y pipelines](https://modal.com/docs/guide/otel-integration#metrics) . These events include when an input was received by the I/O plane, assigned to a container, began executing, etc.
- Containers [heartbeat](https://modal.com/docs/guide/troubleshooting#heartbeat-timeout) against the control plane to ensure healthy operation and against the I/O plane to keep track of inputs.

# Optimizing Function performance

The I/O system has undergone a complete redesign informed by our experience operating Modal Functions at significant scale—each Function can support thousands of containers processing hundreds of inputs every second.

## Small wins add up

From a systems design perspective, there were two major shifts in our code:

- All non-critical work (updating autoscaling stats, publishing input events to power the dashboard, etc.) now happens asynchronously in the background.
- Interactions with shared storage on the hot path of a Function Call are minimized (as our CEO Erik always says - Every Millisecond Counts). While this sounds simple in theory, doing this requires everything from [client-side metadata caching](https://redis.io/docs/latest/develop/clients/client-side-caching/) to a complete redesign of our auth model—the client now receives and refreshes[JWTs](https://datatracker.ietf.org/doc/html/rfc7519) for faster auth.

### E2E request latency within us-east

On the technology side, the most impactful change we made to our server layer was rewriting it fully in [Go](https://go.dev/). When it comes to building highly concurrent [gRPC](https://grpc.io/) servers, Go’s lightweight concurrency model makes it a natural choice over Python. Async Python is cooperatively single-threaded, which makes performance susceptible to [event loop](https://docs.python.org/3/library/asyncio-eventloop.html) lag—a common pain point when handling CPU-intensive operations (e.g. writing large payloads over network).

Another technology choice we revisited was the engine backing our Elasticache deployments—namely [Redis OSS vs. Valkey](https://aws.amazon.com/elasticache/redis/). Valkey is forked off of Redis 7.2 and uses [I/O multithreading](https://valkey.io/blog/unlock-one-million-rps/) to get more utilization out of the single execution thread by moving the I/O work to separate threads.

![Engine CPU usage for a representative intensive workload.](https://modal-cdn.com/cdnbot/ddredisdg7fhid0_2dc846de.webp) 

Our input queues are built on top of [Redis streams](https://redis.io/docs/latest/develop/data-types/streams/). During our input queue load testing, we observed that engine CPU spikes aggressively on Redis 7.2 onwards. As a result, we’ve stuck with Redis 7.1—for the curious, here’s the culprit [change](https://github.com/redis/redis/pull/11012).

## Best user practices

Now that we’ve talked a bit about how we’ve gotten the most for Modal, here’s how you can get the most out of Modal.

Once you’ve made your execution times faster, the next place to look is network overhead. If your clients are located in a particular region, select the `routing_region` closest to them. You can optionally restrict your container region to be near the `routing_region` as well; however, there is a tradeoff between geographic restriction and available capacity to be mindful of (as well as [cost](https://modal.com/docs/guide/region-selection#pricing) implications).

For inputs [larger than 2MiB](https://modal.com/docs/guide/local-data#passing-function-arguments), the client will first upload the payload to our blob storage. Then, the client will send over the blob ID instead of the payload. Performance sensitive workloads should aim to keep the input and output payload sizes under 2MiB to avoid these extra network trips.

One final trick to consider is whether inputs can be batched together in the client. If you have many small and fast inputs, you can reduce the number of network hops needed for them to land on a container by batching them into one larger input:

```
@app.function()
@modal.concurrent(max_inputs=100)
def square(x: int) -> int:
    return x ** 2
@app.function()
def batched_square(xs: list[int]) -> list[int]:
    return [x ** 2 for x in xs]
@app.local_entrypoint()
async def main():
    slow_squares = await asyncio.gather(
        *[square.remote.aio(i) for i in range(100)]
    )
    fast_squares = await batched_square.remote.aio(list(range(100)))
```
# Fin

Modal Functions are the foundational building blocks for autoscaling serverless compute. With our new I/O plane, we’ve questioned every aspect of their internal operation to achieve significant reliability and performance wins.

It took a huge effort from our Core Services I/O team to build a migration that could seamlessly migrate our users to the new system. We set out to deliver a big win without causing user toil, and we had to bridge many incompatibilities between the two architectures to do so. Special shout out to Egor Gagushin, Sam Ross, Parthiv Apsani, and Deven Navani for the marathon grind.

![Parthiv (left) and Egor (right) holding up our team motto the day we completed the migration.](https://modal-cdn.com/cdnbot/daniel_blog_3u9lvht5a_1331147a.webp) 

If you’re interested in building SoTA infra and making it super performant, [we’re hiring](https://modal.com/company#careers)!
