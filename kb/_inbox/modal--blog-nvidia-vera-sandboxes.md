---
title: NVIDIA Vera CPUs double throughput for Modal Sandboxes
kind: blog
topic: null
subtopic: null
secondary_topics: []
summary: null
triage: null
skip_reason: null
source: modal
url: https://modal.com/blog/nvidia-vera-sandboxes
author: Erik Dunteman
published: '2026-10-19'
fetched: '2026-10-20T06:09:40Z'
classifier: null
taxonomy_rev: 2
words: 1267
content_sha256: 0dacdcbc011756372c1d4ecda41d8d3f3d6a7706e832015a6b30065bd6e4a0fe
---

# NVIDIA Vera CPUs double throughput for Modal Sandboxes

Last week, NVIDIA hand-delivered Modal’s first Vera CPU server to our SF office. It’s now purring away in a server rack, and we’re pretty excited about what it could mean for Modal Sandboxes and, consequently, Modal users.

Vera is NVIDIA’s new Arm-compatible CPU, built for the Vera Rubin GPU platform but also available as a standalone CPU server.

Supporting Arm would be a huge change for Modal, coming from a long history exclusively running x86 machines. We’d need to make changes across our infrastructure and image build system to support an entirely different CPU architecture, but the benchmarks are impressive: a 2x increase on throughput. With this, the NVIDIA Vera CPU becomes an incredibly compelling option for powering Modal Sandboxes.

## Why Vera could be a big deal for Modal

**Firstly, multi-tenant clusters are noisy.**

Orchestration for a Sandbox product means running hundreds of concurrent containers and VMs on each cloud host. Unlike normal Kubernetes server deployments colocating pods on the same host, the shape of each sandbox workload is unique, and it leads to some interesting dynamics within a multi-tenant cluster:

- Resource usage can be extremely spiky. A sandbox could spend most of its uptime relatively inactive, waiting on an LLM, with sudden and unpredictable CPU surges 10x above baseline, due to an `npm install` or expensive `grep` command.
- Workload shapes are not statically known. An LLM could throw anything into the sandbox, and the shape of that is only known at runtime. Resource sizing is often just a guess.
- All of these heterogeneous workloads jam together into a single homogeneous pool of compute, which can lead to noisy neighbor issues. One tenant’s performance can be impacted by another’s behavior.

As a result of this, it’s incredibly difficult for users to know how to size their workloads, and for Modal to schedule them without contention.

Unlike other providers that force users to choose fixed reservations for max usage, [Modal Sandboxes support bursting](https://modal.com/docs/guide/sandbox-resources#pay-for-what-you-use), which allows users to reserve guaranteed capacity for their P50 usage, rather than the worst-case P100 `npm install` moment, and trust when the transient spike comes along it’d be absorbed by the padding within the host node.

It’s a great strategy, and we’ve saved users millions of dollars teaching them to trust burstability, but it increases exposure to noisy neighbor issues otherwise avoided by strict limits.

**Secondly, every second of CPU time costs more than just that CPU.**

Sandboxes are usually run to *augment* some external process, and that process bottlenecking on the CPU leads to real dollars spent.

At Modal, we see two prevalent use cases: background agents and reinforcement learning rollouts.

- For background agents, such as Ramp Inspect or those running on Niteshift, faster agents mean faster answers, which means higher revenue and user retention. It also means lower CPU time, driving down COGS.
- For reinforcement learning, there are GPUs sitting idle while sandboxed processes run. Most training setups are still synchronous, and an entire fanout of rollouts must complete before the GPU system can move forward to the next step. Any time saved on CPU is time saved on GPU.

## Benchmarking the Vera CPU

To test Vera, we built a set of representative workloads and benchmarks for agentic Sandboxes.

Creating an “agentic” benchmark is a challenging task, given most of the work done on the servers is not CPU bound, and there’s no specific dimension we’d want to optimize for. Where a DB workload could optimize for disk I/O and an image processing workload could optimize SIMD, for sandboxes we needed to come up with a simulator that is both concurrent and heterogeneous: a big ol’ bag of chaos we could throw at the CPU.

From this we developed [Agentless Agent Bench](https://github.com/modal-projects/agentless-agent-bench), a collection of 50 Terminal-Bench oracle solutions and verifiers, stripped of all network calls and prewarmed in concurrent Docker containers, isolating just the tasks actually performed on the CPU by agents and RL - compilation, file grepping, git operations, device emulation, and more.

Running the benchmark shows us both linear task completion time, and concurrent throughput metrics.

Below are results showing per-task latency for a selection of Terminal-Bench tasks you’d reasonably see an agent running in your sandboxes. This experiment was run on a machine without load, serially, so the results show pure straightline latency.

![Serial task latency in seconds for ten selected workloads on NVIDIA Vera, Intel GNR, AWS Graviton 4, AWS Graviton 5, and AMD Zen 5](https://modal.com/_app/immutable/assets/nvidia-vera-latency.B-WY-X3i.webp)


Seeing these results first, I was admittedly skeptical. Across the 50 tasks we benchmarked, Vera often performed better than the other CPUs, but not always, and not by a particularly large margin.

But straightline latency on a quiet host isn’t what Sandbox users experience. In practice, hundreds of workloads are competing for resources at once. Moving onward to testing under load, we get an entirely different story for Vera.

## The false tradeoff

In most systems, throughput and latency are a tradeoff.

- Latency can be defined as the time that elapses from the start to the end of a task.
- Throughput is the quantity of completed tasks per unit time. This tests the host system’s ability to concurrently interleave processes and make progress on them all simultaneously.

The more densely you pack tasks, the higher the throughput. But once the CPU becomes fully utilized, individual task latency suffers due to contention.

In terms of the Modal scheduler, it’s always tempting for us to run at a higher packing density, to squeeze more juice out of the host machines we have, and to offer a higher absolute scale that users can reach. But just as workloads are spiky within their containers, the absolute scale of the containers in our cluster is also spiky, which leaves us at the risk of overpacking host machines.

Usually, overpacking is felt as increased latency by the user.

But we’ve found this isn’t the case for Vera.

## Vera gets better under heavy load

Agentless Agent Bench has a test for throughput, in which it increases the count of concurrent containers running on the machine, looping as many task completions as possible in a fixed time.

Counterintuitively, Vera gets better under heavy load.

During one of our onsites at NVIDIA HQ, I vividly remember first seeing these results, and being unable to believe how they could be true.

Our early benchmarking runs show up to double the task throughput on Vera compared with an equivalent x86 GNR machine, despite individual task latency measuring equal to, or sometimes even lower than, the x86 machine. This is because Vera does not slow down as jobs accumulate but rips through each one at the original pace.

When asked, the Vera team confirmed that these results are not surprising. It was at this moment I became a Vera believer.

## The killer feature is contention

Vera’s killer feature is the ability to hold up under contention. Its high memory bandwidth allows for significantly more container workloads to pack per core, without CPU throttling - which explains why Vera pulls so far ahead of the alternatives in our benchmarks.

At added CPU counts, the alternatives hit early throughput plateaus, while Vera continues to improve, suggesting we could push it even further than the node we had access to for benchmarking.

For Modal, this unlocks greater packing density and more forgiving burst protection.

For Sandbox users, we can offer higher absolute scale and throughput, without sacrificing latency.

We’re very excited to roll out support for Vera CPUs to power Modal Sandboxes, and work closely with NVIDIA and cloud providers to scale up our fleet.
