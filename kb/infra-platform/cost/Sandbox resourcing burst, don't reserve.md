---
title: 'Sandbox resourcing: burst, don''t reserve'
kind: blog
topic: infra-platform
subtopic: cost
secondary_topics:
- agents/computer-use
summary: Explains Modal's active-resource (bursting) pricing for Sandboxes used by
  coding agents, RL rollouts, and evals, which spend most of their life under 6% peak
  CPU; shows a billing model and calculator claiming ~58% savings over fixed-size
  reservations, plus limit/eviction tradeoffs and SLOs for OOM rates.
triage: null
skip_reason: null
source: modal
url: https://modal.com/blog/sandbox-bursting
author: Kevin Yang
published: '2026-11-12'
fetched: '2026-11-13T06:06:25Z'
classifier: claude
taxonomy_rev: 2
words: 1219
content_sha256: 3c2065ddd1738133ad7e1f61385f3f13456a0b327416555227b67d4a762fe265
---

# Sandbox resourcing: burst, don't reserve

Across Modal, a typical Sandbox spends more than half its life using less than 6% of its peak CPU. Take a coding agent: the Sandbox sits nearly idle while the model reasons about what to do next, and spikes only when the agent installs dependencies, runs tests, or builds the project. The same pattern shows up in other common Sandbox workloads: RL rollouts, evals, and app builders.

Today, most sandboxes are priced based on a fixed-resource reservation model. Reservations are a poor fit for spiky work, for two reasons:

- **You have to guess your peak.** Agent resource usage varies greatly from task to task, and an undersized Sandbox can crash, so you end up reserving well above your real peak.
- **You pay for the peak all the time.** The Sandbox spends most of its life far below its reservation, but you pay for all of it.

We believe your bill should align with your workload, rising when it’s busy and falling when it’s idle. That’s why our Sandboxes burst: a Sandbox gets the CPU and memory it needs when your work spikes and gives them back when it is done. You pay for what you actually use.

## What it looks like on Modal: active-resource pricing

Every Sandbox bursts by default. Start with the base 0.125 cores and 128 MiB request and let your Sandbox grow as it needs.

With active-resource pricing, you pay each second for what you use, with the small request as a floor. You can request more to guarantee it, but you’ll pay for those resources even when your Sandbox is idle. You can also set a limit to cap how far your Sandbox can burst; think of it as setting the size of the computer the Sandbox lives on. Most workloads don’t need to set a request or limit: use the default and burst from there.

## Estimating Sandbox costs on Modal

Because you pay for what you use, estimate your costs from average usage rather than peak usage:

**CPU cost** ≈ runtime × CPU rate × average cores used

**Memory cost** ≈ runtime × memory rate × average GiB used


This average works for bursting Sandboxes because each second, a Sandbox is billed for the higher of its request and what it actually uses. Since the average sits well below the peak, customers with bursty workloads can end up paying a fraction of their typical reservation bill.

The calculator below can help you estimate how your bill would change.

**14.19¢**/CPU·hr

**2.40¢**/GiB·hr

**Bursting is cheaper**: savings of

**58%**vs a fixed-size reservation.

- Average billed use
- 0.44 CPU · 0.94 GiB
- Peak use
- 6.00 CPU · 2.30 GiB
- Reserved size
- 1.5 CPU · 3 GiB CPU for the busiest minute, memory for the peak
- Modal cost per Sandbox-hour
- 8.4¢ 14.19¢ × 0.44 CPU + 2.40¢ × 0.94 GiB
- Reservation cost per Sandbox-hour
- 20.0¢ 10.08¢ × 1.5 CPU + 1.62¢ × 3 GiB
- Bursting savings
- 58%

**1 CPU ≈ 2 vCPU.**Modal prices CPU by physical core; most sandbox providers price by vCPU. Costs are per Sandbox-hour. The reservation covers the workload's busiest minute of CPU and its peak memory, rounded up to whole vCPU and GiB, at a common fixed-size list price. Illustrative workloads, not production traces.

## Why bursting works

Your Sandbox is guaranteed its request, which is small by default. When it bursts beyond that, it draws from a shared pool of the machine’s idle capacity, which Modal’s scheduler keeps free on every machine.

It works because of the law of averages. Sandboxes sharing a machine mostly run unrelated work for different customers, so they rarely spike at the same moment. If every Sandbox reserved capacity for its peak, the machine would need room for the sum of all the peaks. With bursting, it only needs room for the most they use at the same time. It’s the same reason a power grid can be much smaller than the sum of every household’s peak demand.

## How should I size my Modal Sandboxes?

For most workloads, don’t. Start with the defaults and let your Sandbox burst, paying only for what it uses. By default, CPU can burst up to 16 cores above its request, and memory has no limit.

```
# defaults: request 0.125 cores / 128 MiB; limit 16.125 cores, no memory limit
sb = modal.Sandbox.create(app=app)
```
A limit is optional but can be helpful in the following situations:

1. **You need a consistent environment**: For evals, RL rollouts, and other benchmarks, a limit keeps any run from using significantly more CPU and memory than others. If an environment needs exactly the same resources every time, set the request to be equal to the limit.
2. **You want to cap costs**: A limit bounds how much memory and CPU a Sandbox can get and thus limits the total bill from an uncapped process or runaway agent.

When setting a memory limit, set it above the Sandbox’s real peak. Sandboxes that cross the memory limit are stopped.

```
# default request with bursting and a limit: a hard cap at 4 cores and 2 GiB
sb = modal.Sandbox.create(app=app, cpu=(0.125, 4.0), memory=(128, 2048))
```
The default request means you aren’t paying for idle resources: your Sandbox is billed for the default request when it’s idle and you pay for what you use when it bursts.

### Minimizing the impact of evictions

Spikes rarely line up. However, if they do and a machine runs out of CPU, the bursting Sandboxes slow down until CPU frees up. Every Sandbox is guaranteed at least its requested CPU, but in practice most get more when needed.

Memory has a bigger downside. If a machine runs out of memory, Sandboxes using more than their request at that moment may be evicted with an out-of-memory error, or OOM (a Sandbox within its request is never evicted).

Evictions are rare, and we back that with an SLO: for bursting Sandboxes under 8 GiB, an OOM rate below 0.0001% per minute (about 1 eviction per 694 Sandbox-days). We don’t yet have an SLO for larger Sandboxes, but in practice they also see low eviction rates.

We have also provided tools to help reduce the impact of OOMs. [Exit snapshots](https://modal.com/docs/guide/sandbox-exit-snapshots) save your Sandbox’s files automatically when it stops, and [filesystem snapshots](https://modal.com/docs/guide/sandbox-snapshots) save them whenever you choose. [Volumes](https://modal.com/docs/guide/volumes) keep data outside the Sandbox, and the termination reasons SDK lets you detect an eviction and retry.

If your workload can’t tolerate OOMs at the given rates, set a higher memory request (guaranteed memory). To find the right size, start with the default request, check the [Exit Reasons chart](https://modal.com/docs/guide/sandbox-resources#tuning-your-requests) in your dashboard to see how it goes, and adjust your request if needed.

## Summary

In short, most Sandbox workloads are bursty, so they need a pricing model that matches. With Modal’s active-resource pricing you pay for what you use while giving your Sandbox the resources it needs, so estimate from average usage, not peak. Leave the defaults, and your Sandbox will start small and burst as it needs.

Every Sandbox bursts by default, so you can try it with your next `modal.Sandbox.create()`. If you are still unsure where your use case fits, reach out to your sales rep or contact us at [sales@modal.com](mailto:sales@modal.com).
