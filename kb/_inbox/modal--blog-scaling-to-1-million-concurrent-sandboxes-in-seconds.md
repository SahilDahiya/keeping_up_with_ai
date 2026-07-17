---
title: Scaling to 1 million concurrent sandboxes in seconds | Modal Blog
kind: blog
topic: null
subtopic: null
secondary_topics: []
summary: null
triage: null
skip_reason: null
source: modal
url: https://modal.com/blog/scaling-to-1-million-concurrent-sandboxes-in-seconds
author: null
published: '2026-07-15'
fetched: '2026-07-17T06:46:43Z'
classifier: null
taxonomy_rev: 2
words: 1964
content_sha256: 0acdc2c6396e93d0d28df5bdb80b036200e0ed9b6e90f6e6a1ec4fc06718387a
---

# Scaling to 1 million concurrent sandboxes in seconds | Modal Blog

[Back](https://modal.com/blog)

# Scaling to 1 million concurrent sandboxes in seconds

At Modal, we build sandboxes, among other things. Agents run in sandboxes, and agents are eating software. Today, Modal runs millions of sandboxes per day, supports up to fifty thousand concurrent sandboxes per customer, and supports a variety of use cases at scale, from [reinforcement learning](https://modal.com/blog/applied-compute-reinforcement-learning) to [background agents](https://modal.com/blog/how-ramp-built-a-full-context-background-coding-agent-on-modal).

Increasingly, our users require more and more sandboxes, created at higher and higher rates. Reinforcement learning can require running millions of sandboxes concurrently, and creating bursts of hundreds of thousands of sandboxes at the beginning of rollouts. Similarly, agents increasingly require massive scale and high concurrent creation rates to deal with traffic bursts.

Our existing sandbox platform is really good, but it wasn’t designed for these scales; nor is any other existing solution. We’re obsessed with scale and performance, and we want our infrastructure to accelerate the growth of agents, not add friction. So we went back to the drawing board.

Over the last few months, we’ve rebuilt our core sandbox platform from the ground up for both scale and reliability. On our new system, users can run millions of sandboxes concurrently and create tens of thousands of sandboxes per second. We’ve removed all central bottlenecks from our control plane so there are no practical scaling limits, and we’ve optimized every part of container scheduling and startup, simplifying the scheduling path to a layer of load balancers which create containers directly on our worker fleet.

As a demonstration of what our platform is capable of, we’ve run a million sandboxes concurrently, creating all 1 million in under a minute.

![Evidence that we can run a lot of sandboxes.](https://modal-cdn.com/blog/images/1Msandboxes.webp) 

 ## Why most solutions don’t scale

Running 1 million sandboxes pushes the limits of any container platform, both because of the sheer number of containers, but also because running this many sandboxes requires many tens of thousands of compute nodes. There will be many operations which are either O(containers), O(nodes), or both, which will cause traditional container platforms to hit scaling limits.

For Kubernetes, as an example:

- The scheduling algorithm is `O(n x p)`for`n`nodes and`p`pods in the worst case, and scheduling is serialized by default.
- Each pod causes multiple writes to etcd (the central Kubernetes durable store) over its lifetime, which can create serious issues under high pod creation rates or high pod churn, and etcd is not natively shardable within a keyspace
- Each node must write to etcd at least once per heartbeat interval to signal liveness, so baseline etcd write load is O(nodes) completely independent of pod creation

![Approximation of Kubernetes scheduling flow. New pods are written to etcd (a strongly consistent durable store) by the API server. The Kubernetes scheduler watches for new unassigned pods, and assigns them to nodes via a call to the API server, which again writes to etcd; after this write goes through, then a node can start the pod.](https://modal-cdn.com/blog/images/kubernetes-architecture.webp) 

 Kubernetes can be scaled, but it requires serious work. To run large numbers of nodes, etcd generally must be [rewritten](https://aws.amazon.com/blogs/containers/under-the-hood-amazon-eks-ultra-scale-clusters/) or [replaced](https://cloud.google.com/blog/products/containers-kubernetes/gke-65k-nodes-and-counting). Supporting high scheduling throughput requires building a [complex scatter-gather system](https://bchess.github.io/k8s-1m/#_scheduler) to parallelize the scheduling algorithm while still maintaining a single source of truth for pod state. Sharding and parallelization is not easy by default, because Kubernetes relies on strong consistency as a backbone of its design.

Modal’s original sandbox architecture has similar issues. Like Kubernetes, we rely on strong consistency throughout our backend, so creating and scheduling sandboxes requires global coordination, and O(sandboxes) writes to Postgres, which we cannot trivially shard.

![Modal’s original sandbox control plane architecture. When sandboxes are created, they are placed on a queue and written to Postgres. Scheduling is optimistic and run in parallel, with central coordination required to avoid conflicts. Assigning a sandbox to a worker (compute node) requires an additional write to Postgres.](https://modal-cdn.com/blog/images/sandbox-scheduling-flow.webp) 

 Because we don’t build on Kubernetes, we’ve been able to scale out many parts of this system. For example, scheduling is parallelized by default, which allows us to achieve very high burst sandbox creation rates. But as we scaled to larger and larger numbers of nodes and sandboxes, we continually encountered new bottlenecks arising from operations which were either O(sandboxes) or O(nodes) but were not easy to scale out.

For example, we run a durable workflow for each sandbox that finishes, so high sandbox churn rates would create massive event backlogs. We’d repeatedly run into RPCs called at a rate of O(sandboxes) which caused unexpected load issues throughout our system. And the sheer number of nodes required to run large numbers of sandboxes caused multiple downstream problems in node management and autoscaling. Lastly, even though we could work around it, leaving an unsharded Postgres instance in the critical path of all sandbox creation and scheduling had proven to be a bad idea.

## Unlocking infinite scale

We quickly realized that achieving the scale we wanted required rethinking our architecture from the ground up. We want to run millions of sandboxes and create tens of thousands of sandboxes per second, which requires much better scaling properties than anything existing. Rather than trying to evolve what we had, we believed that the fastest and cleanest path was to start fresh.

To optimize for scale, we decided that everything taking O(sandboxes) or O(nodes) load must be horizontally scalable by default, the sandbox creation path should be as simple as possible, and everything else should be secondary. The solution we came to is notably different than existing systems. We completely dispensed with any sort of central coordination, and traded global consistency for scalability and performance everywhere on the critical path for running and creating sandboxes. Here’s how it works:

- Rather than a single, serialized scheduler, we run a fleet of scheduling servers which handle sandbox creation requests concurrently. To handle a creation request, a scheduling server runs a fast scheduling algorithm against in-memory cached data. The result is that scheduling scales horizontally, and looks more like load balancing than traditional container scheduling.
- Rather than a central, durable datastore acting as the source of truth for sandbox and worker state, which is how most container platforms work, every worker in our new system is its own source of truth. Workers publish their state periodically into a Redis stream. The scheduling servers consume this state asynchronously and use it to make scheduling decisions. Once a scheduling server decides which worker to create a sandbox on, it contacts the worker directly via RPC to request that a sandbox is created. Workers accept the scheduling request if they have free resources, or otherwise reject it.
- We have no data stores in the critical path of sandbox creation at all, which improves scalability and reliability. While we do need to write sandbox metadata and results to durable storage, we do so largely asynchronously.
- Other than sandbox creations, we have no RPCs which are O(sandboxes). Workers batch control messages for multiple sandboxes together in single RPCs, in the spirit of ideas from [data-oriented design](https://en.wikipedia.org/wiki/AoS_and_SoA).

![Our eventual design, the first time we whiteboarded it.](https://modal-cdn.com/cdnbot/whiteboard6_57d5zl_2ac154c2.webp) 

 ![Sandbox creation path in Modal’s v2 sandbox architecture. Sandbox create requests are handled by horizontally scaled scheduling servers, which then select a worker with a fast in-memory load-balancing algorithm, and contact the worker (compute node) directly to create a sandbox. Sandbox objects are stored in Redis, but not in the critical path.](https://modal-cdn.com/blog/images/sandbox-scheduling-flow-2.webp) 

 The result is that the sandbox creation path requires only two network hops and one cheap CPU operation. There are no central bottlenecks or coordination costs, no single points of failure, and consequently no practical ceiling to aggregate sandbox scale or sandbox creation throughput. We can add more schedulers or workers as needed. The most imminent bottleneck is that all workers publish state to a single Redis stream, but load testing has suggested that this remains viable until well over 100,000 workers; and we don’t depend on ordering on the stream anyway, so it would be easy to just add more streams. By design, we avoid the issues which prevent existing solutions from scaling.

Building this solution was not easy! The entire development process has taken months of work, spanning most major systems in our backend. We spent hours on whiteboards. Four of us decamped to a rental house in Miami Beach to build a prototype of the new system we wanted, without distractions. We spent eight days writing code until we physically could not, playing speed chess to recuperate, jumping in the ocean, and then going right back to the code, fighting to get our new system clean and functional.

![Our best engineer relaxing in Miami Beach.](https://modal-cdn.com/cdnbot/catoz4fhq7d_f8ec8cb7.webp) 

 Once we got the core pieces working (and came back to New York), we also needed to reimplement every single Sandbox feature and all Sandbox observability on top of our new system. This project also necessitated changes to our core worker management stack, as well as our container runtime. For example, one interesting issue we encountered is that our new sandbox schedulers could push containers to workers *so quickly* that many containers starting at once would contend for the `rtnl` lock in the Linux kernel when setting up container networking rules and take tens of seconds to start up, so we had to change our container networking setup for sandboxes just so our workers wouldn’t blow up when flooded with sandbox creations.

## How our performance stacks up

We benchmarked our system by spinning up 1 million sandboxes as fast as we could. At a high level, we can create one million sandboxes in under a minute, where the primary bottleneck is the benchmark itself. Individual sandbox time-to-interactivity remains consistently low, and we see no real degradations with scale.

![Distribution and eCDF of sandbox creation requests. A sandbox creation request returns when our scheduling servers have successfully assigned a sandbox to a worker, and it has begun to start.](https://modal-cdn.com/cdnbot/sandbox-inf-ecdf4p4lrl2v_7cee00a8.webp) 

 We believe this is expected, given our design. There is no coordination in the scheduling path, so scheduling should remain very fast independent of concurrency and scale. As far as we’re concerned, we have no serious limits to concurrent sandbox scheduling or scale outside of available capacity, and managing capacity is [already something we do well](https://modal.com/blog/resource-solver).

![Scatterplot of 10k sandbox start times from our 1M sandbox test, randomly selected from the 1M sandboxes.](https://modal-cdn.com/cdnbot/scatterboxqde_ns39_ac61ab91.webp) 

 Sandbox start times on our new system (the latency from when the client first tries to create a sandbox, to when the sandbox can run user code) are less than half a second at the median, and remain solid at scale. They are also [substantially faster than our old system](https://www.computesdk.com/benchmarks/sandboxes/modal/), largely because scheduling is so much faster — it only takes tens of milliseconds now. The long tail of latency is somewhat longer than we’d like. We attribute much of this tail to kernel and network contention (including the `rtnl` lock contention mentioned previously) when many sandboxes start simultaneously on the same worker, and we’re working to reduce it. Also, the [tail at scale](https://research.google/pubs/the-tail-at-scale/) is real. We expect this to improve as we optimize the container startup path.

Overall, we are very happy with these performance numbers. As agents take over the world, clearly we can scale with them.

## See for yourself

Soon this new system will back all sandbox scheduling at Modal, but it’s already available in Beta. You want to opt in with [one simple change to your code](https://modal.com/docs/guide/sandbox-v2). If you need to run a lot of sandboxes, try it out, and talk to us!

## Acknowledgements

A lot of people contributed blood, sweat, and tears to this project. Our Miami POC was built by [Colin Weld (me](https://www.linkedin.com/in/colin-weld/)), Daniel Shaar, Walter Tang, and Gleb Posobin, and then brought to production by Walter, Colin, Connor Adams, Akshay Balwally, Tom Wildenhain, Scott Hao, and Taylor Baldwin.
