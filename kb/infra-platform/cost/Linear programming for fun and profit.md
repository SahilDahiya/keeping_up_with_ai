---
title: Linear programming for fun and profit
topic: infra-platform
subtopic: cost
secondary_topics:
- infra-platform/gpu-clusters
summary: Shows how linear programming can allocate compute resources under constraints,
  useful for GPU scheduling and cost control.
source: modal
url: https://modal.com/blog/resource-solver
author: null
published: '2025-05-07'
fetched: '2026-07-11T04:28:58Z'
classifier: codex
taxonomy_rev: 1
words: 1774
content_sha256: 2ef681e16c392e063659f1b8675485c45f251b1597a4ded216f604ac23991425
triage: keep
skip_reason: null
---

# Linear programming for fun and profit

[Back](https://modal.com/blog)

# Linear programming for fun and profit

![](https://modal-cdn.com/cdnbot/tmp8y8y9umw_673275d4.webp)



If you haven’t noticed, the GPU market is highly volatile. NVIDIA repeatedly spews out new chip architectures, doubling FLOPS every few years. Everyone shifts towards the newest cards, causing temporary supply crunches and high prices. But Modal’s customers don’t want to think about these price fluctuations. They want GPUs of all kinds at predictable and good prices, and the ability to demand thousands of GPUs on a moment’s notice, without having to worry about pricing, capacity planning, or supply.

At Modal, we’ve built a “resource solver” system which is capable of finding and enjoying arbitrages in this cloud storm, satiating our customers’ demand for scalable compute at good prices. Did you know that a few months ago you could get hundreds of superior H200 GPUs for 20% less than the going rate for inferior H100s? The solver did, and it took that deal.

At its core, Modal’s resource solver is a [linear programming](https://en.wikipedia.org/wiki/Linear_programming), or LP, solver — an algorithm which can quickly and reliably maximize an objective given a set of linear constraints. We feed this algorithm information about current demand in our system, plus current prices, availability and performance for a variety of cloud server types. It then spits out a delta — which kinds of instances we should spin up and spin down, and how many we need of each to satisfy demand. The resource solver keeps our serverless system afloat, allowing our customers to gleefully forget about the horrors of cloud instance quotas and reservations. But it also finds temporary discounts and arbitrage opportunities, saving millions of dollars a year.

## Understanding capacity

The problem the solver solves is easy to understand, and it shows up in many domains. Consider the simplest possible version of Modal — let’s call it Modull, because it’s simple. Your customers want to run on NotVidia’s flagship GPU, the A1. As customers call their Modull Functions over the course of a day, you have an ever-changing number of containers (we call them Tasks) which demand variable numbers of A1 GPUs. How do you service all these containers? With only a single type of resource, it’s easy — you add up the total number of A1 GPUs requested. If you’re already running that many GPUs, you’re done. If not, figure out how many more GPUs you need, and then get as many as you can from whatever cloud provider offers them for the best price. If you can’t scale up sufficiently, you try the next best cloud provider, and so forth. You could write a script that does this.

```
# For each per‑cloud instance type, we know the current price and the capacity limit.
cloud_provider_prices_and_limits = {
    "CloudA": {"price": 1, "limit": 5},
    "CloudB": {"price": 2, "limit": 20},
}
def solve_for_demand(
    requested: int,
    providers: dict = cloud_provider_prices_and_limits,
):
    remaining = requested
    allocation = {name: 0 for name in providers}
    # Sort providers by increasing price.
    for name, info in sorted(providers.items(), key=lambda p: p[1]["price"]):
        if remaining == 0:
            break
        # Exhaust cheaper instances before using more expensive ones.
        buy = min(remaining, info["limit"])
        allocation[name] = buy
        remaining -= buy
    return allocation
```
A key problem: users want containers scheduled in seconds, but it takes minutes to acquire and start a new cloud server. So you have to maintain some headroom. To do this relatively cost-efficiently, you can maintain a buffer — some configured number of extra, idle GPUs — that newly scheduled containers can burst into, without having to wait for scale-up. This doesn’t come for free, but it’s an easy way to deliver good performance. Modal does this, more-or-less. When a customer suddenly runs hundreds of containers at once, we maintain a large enough buffer to schedule their containers instantaneously, while scaling up concurrently. You’d need to account for this buffer in the solver.

In the simplest version of this problem, finding an arb(itrage) is easy. It’s barely even an arb — you’re just looking for the cheapest prices to satisfy demand, which is easy to find. But the problem becomes more complicated when you introduce more constraints:

- Modal users don’t just care about GPUs; they also need specific amounts of CPU and RAM, too.
- Tasks that only want CPU can run anywhere, even on GPU machines, but GPU tasks must run on particular machines, but maybe only in a subset of regions.
- Users can choose between 7 kinds of GPUs if they want, [multiple types of GPUs](https://modal.com/docs/examples/gpu_fallbacks)in order of preference, or no GPU at all.
- User demand on our system varies wildly as customers constantly scale up and down by orders of magnitude.
- We run instances on every major cloud, and prices change by the minute.

This problem quickly becomes hairy to solve in the naive way we handled the simple case above. It’s possible we could find an arb; it’s more likely we’d write buggy code that bleeds money and doesn’t even let our users scale.

## Simplex made easy

If we view our capacity challenge through the right mathematical lens, we can see opportunity, rather than risk, in the nonstop volatility of cloud compute supply and demand. Consider the simplest possible example, where we only offer one type of GPU in one region, and instances have 8 GPUs each. We can represent this as a [linear programming](https://en.wikipedia.org/wiki/Linear_programming) problem — a linear expression to minimize, and a set of linear constraints: ![](https://modal-cdn.com/cdnbot/math3d3f4958_51e2bc04.webp)



Modal’s complicated demand story can also be represented this way, more or less!

Fortunately, computer scientists and mathematicians have been producing algorithms to solve these problems for nearly two hundred years. Specifically, we rely on the [simplex algorithm](https://en.wikipedia.org/wiki/Simplex_algorithm), an old tool with an interesting history. In the late 1930s, the American mathematician [George Danzig](https://en.wikipedia.org/wiki/George_Dantzig) was working on his doctorate. Like Matt Damon in Good Will Hunting, he walked into a classroom one day, found statistics problems written on the blackboard with no context, brought them home, and solved them as part of his homework. It turned out the problems were unsolved; Danzig’s solutions became the foundation of the simplex algorithm, which he invented a few years after while analyzing logistics for the US Army during WWII. Now, 80 years later, we use it for optimizing cloud prices, a problem of much less consequence.

The simplex algorithm models our constraints as surfaces in N-dimensional space, which enclose a set of points; every point representing a possible solution to the constraints. It then searches through the boundaries of this space to minimize or maximize an objective function — cost, in our case, in polynomial time in the average case, and exponential time in the worst case.

It’s complicated to run the simplex algorithm in production. If you want to solve linear programming problems as part of a high-availability system, you begin to care about how predictable and reliable your LP solver’s performance is. You don’t want to hand some constraints to your optimizer and have it run through an exponential number of possible solutions without warning you, or spin endlessly trying to solve an unsolvable problem. Like so many systems problems, Google worked on this class of issues with little fanfare years ago — we use their rock-solid [GLOP solver](https://developers.google.com/optimization/lp/lp_advanced), published as part of the OR-Tools library. We have nothing but good things to say about both. They work well enough out of the box, and come with useful knobs appropriate for our continuously running production context (things like bounding the maximum optimization steps, feasibility tolerances, or internal iterations — to keep solve times predictable).

## The solver’s self-actualization

![How GLOP fits into our system. We wrap it in an external service which regularly scrapes information from our backend and all our cloud providers, which then massages the inputs to produce a relatively small set of constraints which GLOP is likely to solve quickly. GLOP emits the solution to an external pool of background tasks, which make the actual instance requests to the cloud providers, and report observed per-instance scaling limits back to the solver service.](https://modal-cdn.com/cdnbot/tmpzi4q990l_40d5f730.webp)



Our users want to scale up fast, and keeping them happy comes before keeping our prices low. Therefore the solver, and the system built around it, end up, like the Fed, with a [dual mandate](https://www.chicagofed.org/research/dual-mandate/dual-mandate) — our scaling decisions must be made quickly and be cost-optimal. Like the Fed, we find that our two mandates are often in conflict.

For instance, we’ve periodically struggled with solves taking far too long, and some solves never finishing at all. To address this, we’ve found that we can run some cheap heuristics on the solver’s inputs before running GLOP to prevent unsolvable problems and reduce solve times to fractions of a second. As an example, exposing our myriad instance types to the solver can result in very long solve times — sometimes several minutes. We can prune many instance types ahead-of-time, to speed up our solver by as much as an order of magnitude, at the cost of a small amount of accuracy. By keeping our solve times reliably short, we ensure that we can scale up fast; currently we’re primarily limited by the speed at which we can acquire and start new instances from cloud providers rather than anything internal in our system.

To complete the rest of the owl: GLOP emits its solution to our database, and a separate pool of background workers requests new instances from the cloud providers as needed. When those requests fail, we know we’ve hit some underlying capacity limit in the cloud provider, and we use the scaling limit we’ve observed as an input to the solver in subsequent runs. This way we ensure that subsequent attempts to scale up are likely to request instance types the cloud provider still has available.

Should you replace your autoscaler with linear programming? Maybe! We’ve found that the presence of the solver allows us to focus on things that our customers see directly, like starting containers quickly and getting deep into network infrastructure. We spend less time worrying about optimality, because we can trust that the linear programming is a tried-and-true method that will deliver optimal solutions as long as we give it the right inputs, which makes it easy to take advantage of GPU pricing chaos to the benefit of our users. This makes sense for Modal — serverless is complicated, and the more we can make the complexities of the cloud disappear behind the curtain, the better.

## Acknowledgements

Thanks to [Jonathon Belotti](https://thundergolfer.com/) for extensive feedback throughout the process of writing this!

If you’re interested in crafting reliable and performant systems at scale for the next generation of cloud infrastructure, Modal is [hiring](https://modal.com/careers).
