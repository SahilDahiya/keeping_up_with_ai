---
title: How to price serverless GPUs
topic: infra-platform
subtopic: cost
secondary_topics:
- inference/serving
summary: Explains serverless GPU pricing from utilization, scheduling, and workload-shape
  constraints rather than simple hourly rates.
source: modal
url: https://modal.com/blog/how-to-price-serverless
author: null
published: '2026-07-06'
fetched: '2026-07-11T04:26:39Z'
classifier: codex
taxonomy_rev: 1
words: 1699
content_sha256: d7bc92b5dda3e7cc7603bf50b42919eabb1eded72d505ed82898dcc8431bde64
triage: keep
skip_reason: null
---

# How to price serverless GPUs

[Back](https://modal.com/blog)

# How to price serverless GPUs

[Charles Frye](https://twitter.com/charles_irl)

The gap between “paying for peak” and “earning on average” is critical to understand how the economics of large-scale cloud systems differ from traditional single-tenant systems.

— Marc Brooker,

[Surprising Scalability of Multitenancy](https://brooker.co.za/blog/2023/03/23/economics.html)

GPUs are expensive but critical to operations for artificial intelligence. So it is no surprise that as engineering teams have embraced development of AI applications, the cost of GPUs has attracted the attention of finance departments.

This has led to conflicts and misunderstandings between procurement teams, which want to control costs but don’t always have application context, and application teams, which want to build but don’t always have market context.

So we built this interactive tool to help teams estimate costs for serverless and reserved GPUs.

You can select a preset workload based on our experiences with customers
or draw in your own traffic patterns by clicking/touching and dragging on the chart.
The model defaults to current rates for a B200 GPU serverlessly on Modal and via three-year reservation on hyperscalers.
You can find the rest of our rates [here](https://modal.com/pricing).

We hope this helps financial and engineering teams understand one another, have productive discussions, and make informed decisions about when to buy serverless GPUs and when to make reservations.

The critical workload parameter in this model is the *peak-to-average ratio*:
how many GPUs you need to satisfy peak demand versus how may GPUs you need “on average”.
High peak-to-average demand ratios come from rapid growth, from social media buzz, or just from the whims of users.
With reservations, high peak-to-average ratios lead to [low GPU allocation utilization](https://modal.com/blog/gpu-utilization-guide),
SLO violations, or both.

According to this model, **when the peak-to-average ratio is larger than discount rate for the reservation,
the total cost of the application is lower for serverless GPUs.**

In our and our customers’ experience, reflected in the cases available in the widget above,
workloads like inference, training, and agentic development have peak-to-average ratios in excess of 5:1, even 10:1,
making serverless GPUs on Modal far cheaper than reservations, despite a higher base rate.
Our users also find that they [accelerate development](https://modal.com/blog/suno-case-study), leading to superior product outcomes at reduced engineering cost.

# How are serverless GPUs different from reservations?

Modal makes it easy to run code on GPUs in the cloud.

```
@app.function(gpu="B200:8")
def go():
    import subprocess
    subprocess.run("nvidia-smi")
```
```
const modal = new ModalClient();
const app = await modal.apps.fromName("my-app", {
  createIfMissing: true,
});
const image = modal.images.fromRegistry("python:3.13-slim");
const sb = await modal.sandboxes.create(app, image, { gpu: "B200:8" });
const p = await sb.exec(["nvidia-smi"]);
console.log(await p.stdout.readText());
await sb.terminate();
```
```
ctx := context.Background()
mc, _ := modal.NewClient()
app, _ := mc.Apps.FromName(ctx, "my-app", &modal.AppFromNameParams{
  CreateIfMissing: true,
})
image := mc.Images.FromRegistry("python:3.13-slim", nil)
sb, _ := mc.Sandboxes.Create(ctx, app, image, &modal.SandboxCreateParams{Gpu: "B200:8"})
defer sb.Terminate(ctx, nil)
p, _ := sb.Exec(ctx, []string{"nvidia-smi"}, nil)
stdout, _ := io.ReadAll(p.Stdout)
fmt.Println(string(stdout))
```
`uvx modal shell --gpu b200:8`We provide GPU access [ serverlessly](https://modal.com/blog/truly-serverless-gpus):
you only pay for what you use, because you are only allocated what you are using
at any moment, up to some limit (hundreds or thousands of GPUs in Modal’s

[Enterprise Tier](https://modal.com/pricing)). Resource purchase and resource use are tied together.

Modal is able to provide serverless GPUs because we [developed a variety of technologies that enable fast and efficient allocation of resources](https://modal.com/blog/truly-serverless-gpus),
from [cloud instance management with linear programming](https://modal.com/blog/resource-solver) and [health-checking across over a dozen providers](https://modal.com/blog/gpu-health) to [container memory snapshotting](https://modal.com/blog/gpu-mem-snapshots).

The serverless paradigm is quite different from the dominant paradigm for GPU delivery,
which requires *reserved allocations*.
In this paradigm, resource purchase and resource use are separated.
A “block” of GPU “capacity” is “reserved” under a long-term contract (generally, months to years).
That exact quantity of GPUs is available for use — no more, no less.

According to industry surveys, applications [achieve very low utilization](https://modal.com/blog/gpu-utilization-guide) of these reservations (less than 30% in general, often under 10%)
leading to substantial wasted spend — and worsening the compute crunch for everyone.

# How much do serverless GPUs and reserved GPUs cost? How do I know which is better?

Let’s consider a simple model for the total cost of application delivery for both serverless and reserved GPUs. We encourage you to take this model and build off of it!

We start with the application’s demand for GPUs at any given moment, demand(*t*).
That might look something like the following, derived from Modal usage data from a real application:

![Applicaton GPU demand over two months, showing high variability](https://modal-cdn.com/blog/images/how-to-price-serverless-sample-demand.webp)



Let’s assume serverless GPUs are allocated instantly.
Then, the total cost *C s* is just the serverless provider’s rate

*R*times the demand at each point in time.

s![Serverless cost: C_s equals the sum over time of R_s times demand at each instant](https://modal-cdn.com/blog/images/how-to-price-serverless-eq-cs-sum.png)



In the reserved model, demand must instead be predicted. Let’s assume that the demand can be perfectly predicted on the timescale of the reservation — a charitable assumption to match our charitable assumption about serverless GPUs.

To satisfy application demand, we need to allocate for peak demand, throughout the entire reservation. We’ll assume that is the same as the lifetime of the application.

With these assumptions, the total cost *C r* is just the reservation provider’s rate

*R*times the

r`max`imum demand times the length of the reservation *T*.

![Reserved cost: C_r equals R_r times T times the peak demand over time](https://modal-cdn.com/blog/images/how-to-price-serverless-eq-cr-formula.png)



Which strategy costs more depends, then, on just how “peaky” that peak demand is.

We start by taking the ratio of the two costs:

![Cost ratio: C_r over C_s equals R_r times T times max demand divided by the sum of R_s times demand over time](https://modal-cdn.com/blog/images/how-to-price-serverless-eq-cost-ratio.png)



Then, we move the factor of *T* to the bottom.

![Cost ratio with T moved to denominator: C_r over C_s equals R_r times max demand divided by R_s times average demand](https://modal-cdn.com/blog/images/how-to-price-serverless-eq-cost-ratio-t-moved.png)



Now, we have the two rates multiplied by two statistics of the demand: the peak value and the average value.

Let’s get the equations closer to English:

![Full derivation: C_r over C_s simplifies to reservation discount rate times peak-to-average ratio](https://modal-cdn.com/blog/images/how-to-price-serverless-eq-final-derivation.png)



That is: if reserved GPUs are 10 times cheaper than serverless GPUs, but the application has a peak-to-average ratio of 10, the application cost is the same. We generally observe discounts on the order of 2-5x and peak-to-average ratios of 5-10x, which makes serverless an obvious win on cost.

And note that that’s just raw application service cost! The superior engineering velocity afforded by the flexibility of the serverless approach also reduces development and maintenance costs. For instance, Modal’s fast cold starts make it easy to develop against the same infrastructure you deploy to production. That removes one very common source of friction, velocity reduction, and high time-to-repair.

# What is missing from this cost model?

All models are wrong, including this one, but some are useful, including this one.

Let’s examine the key assumptions of the model and what happens when they break.

**We assumed that demand could be perfectly predicted.**

Practically, this assumption is really “demand can be predicted up to the requirements of the service-level objective”. This assumption benefits the reservation model.

When our predictions (or educated guesses) are off low, we end up with an underperforming application, increased faults and/or queues, and angry users. This also leads to repeated rounds of procurement discussions across application builders, internal teams, and external vendors — generally under time/customer pressure due to violation of SLOs.

When our predictions are off high, there is waste, which again triggers additional rounds of financial discussions, now after money is spent and a contract is signed.

**We assumed that allocation and de-allocation is instant**.

Practically, this assumption is really “service-level objectives can be met with autoscaling serverless capacity”. This assumption benefits the serverless model.

At Modal, we [invest heavily to speed up autoscaling](https://modal.com/blog/truly-serverless-gpus) so that even complex applications like a vLLM or SGLang inference server can start in seconds.
When this speed is insufficient, users can over-provision with warm pools and buffers.
This increases cost, but generally, buffers become less expensive to operate with scale.

In any case, adjustments occur within the envelope of application development (from engineering’s perspective) and an aggregate budget (from finance’s perspective), without triggering more rounds of internal and external negotiation due to artificial contract limits, as happens with a reservation.

**We assumed only “all-or-none” strategies: all serverless or all reservation.**

This is not just a helpful assumption to make math easier — it also corresponds to reduced operational cost. One system is cheaper to maintain at a given level of robustness and performance than two, for both financial and engineering teams.

But some organizations pursue a mixed strategy. Most commonly, they aim to use a reservation to cover “baseline” load (minimum demand) and serverless GPUs to cover “burst” or “excess” load (everything else). The same peak-to-average ratio math can be used here, but with the peaks and averages of burst/excess load over the baseline. We observe very large peak-to-average ratios for bursts — 10-100x — which makes serverless deployment particularly compelling.

We’re exploring options for bringing the combined reservation/serverless economic model to Modal,
so that finance teams don’t need to procure two vendors and engineering teams don’t need to integrate two systems.
If you’re interested in reserving and bursting into hundreds or thousands of GPUs, [contact us](mailto:sales@modal.com).

**We assumed that GPU cost was the only factor.**

Cost matters, but costs can only be directly compared for substitutable goods.
But serverless GPUs and reserved GPUs are not identical!
And on Modal in particular, we’ve made substantial investments in [developer (and agent) productivity](https://modal.com/blog/agents-devex).

For instance, the speed of allocation and deallocation of serverless resources on Modal allows for development against the same infrastructure running in production. Reduced dev/prod skew means faster development at a lower defect rate.

# What’s next?

We hope this document is helpful to you in navigating GPU procurement or development, whether you’re thinking about cost control, demand satisfaction, or both. The contents have certainly helped us clarify options and qualify (or disqualify!) customer engagements.

If you’re running an application with high peak-to-average GPU demand ratios, like inference, training, or agentic development,
and you think serverless GPUs are right for you, [try Modal right now](https://modal.com/docs/playground).

If you’re interested in mixed serverless/reserved models for hundreds or thousands of GPUs, [contact us](mailto:sales@modal.com).
