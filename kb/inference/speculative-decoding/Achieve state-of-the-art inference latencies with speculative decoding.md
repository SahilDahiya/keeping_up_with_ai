---
title: Achieve state-of-the-art inference latencies with speculative decoding
topic: inference
subtopic: speculative-decoding
secondary_topics:
- models/reasoning
summary: Explains speculative decoding for lower inference latency, including draft-model
  tradeoffs and production serving considerations.
source: modal
url: https://modal.com/blog/achieve-sota-specdec
author: null
published: '2026-06-22'
fetched: '2026-07-11T04:26:49Z'
classifier: codex
taxonomy_rev: 1
words: 2049
content_sha256: 07ba47d95492dd8ec68e41bdd0049fb904e98237053d9ed57a69fdb5ad04c479
triage: keep
skip_reason: null
---

# Achieve state-of-the-art inference latencies with speculative decoding

[Back](https://modal.com/blog)

# Achieve state-of-the-art inference latencies with speculative decoding

[Charles Frye](https://twitter.com/charles_irl)

[Shankha Biswas](https://twitter.com/ShankmanJunior)

This week, we are launching [Modal Auto Endpoints](http://modal.com/blog/introducing-auto-endpoints), which bring the scalability and robustness of Modal infrastructure to state-of-the-art inference performance — with a single click and without losing control of the code.

How do we achieve such high performance? Is it a [goated kernel authoring team](https://modal.com/blog/flash-attention-4-faster)? Is it our [GPU fleet](https://modal.com/blog/resource-solver) and [container runtime](https://modal.com/blog/truly-serverless-gpus)? Do we have some [special sauce in the inference engine](https://modal.com/blog/boosting-multimodal-inference-performance-by-greater-than-10-with-a-single-python-dictionary)? Are we [agent-maxxing](https://modal.com/blog/autoscaling-autoresearch)?

Kernels, compute capacity, inference engines, and software velocity all matter, but when it comes to low latency inference serving, to first approximation, [speculation is all you need](https://modal.com).

In particular, we have found that if you have Blackwell GPUs, a strong open source engine like SGLang and a low-overhead regional deployment system like [Modal Servers](https://modal.com/docs/guide/servers), you can match or beat proprietary inference providers for latency-sensitive use cases just by doing a better job at one key optimization: speculative decoding.

![](https://modal-cdn.com/blog/images/achieve-sota-specdec-latencies.webp)

## The low latency playbook

If you squint, serving transformer inference looks a bit like this:

![](https://modal-cdn.com/blog/images/achieve-sota-specdec-prefill-decode-diagram.webp)

That is, a client sends a request to an inference server, which processes the input tokens in the request (”prefill” step) and then processes the output tokens sequentially (”decode” steps).

This model indicates four sources of latency:

- Client-server communication latency
- Host/comms latency before prefill, between prefill and decode, and between decodes
- Prefill latency
- Decode latency

The decode phase is often the primary source of latency. There are generally several decode steps; each decode step requires a full forward pass, which requires loading model weights [from GPU RAM to SM SRAM](https://modal.com/gpu-glossary/perf/memory-bandwidth). And so optimizations on the decode path have the biggest lift.

For each of these sources of latency, we have a go-to optimization technique:

- Put servers close to clients and [keep routing/services overhead minimal](https://modal.com/docs/guide/servers)
- Use an inference engine with [low host overhead](https://modal.com/blog/host-overhead-inference-efficiency),[remove](https://modal.com/blog/boosting-multimodal-inference-performance-by-greater-than-10-with-a-single-python-dictionary)any overhead you observe
- Use speed-of-light kernels for state-of-the-art GPUs, like [FA4](https://modal.com/blog/reverse-engineer-flash-attention-4)for B200s/B300s
- Apply speculative decoding with high-quality [DFlash draft models](https://www.lmsys.org/blog/2026-06-15-next-generation-speculative-decoding-dflash-v2/)

Because decode generally contributes the most to latency, speculative decoding has the biggest impact on the final end-to-end latency number.

### Why speculation is all you need

By default, decoding is sequential, one iteration per output token. Speculative decoding makes it parallel across several tokens — a chance to avoid Amdahl’s heartbreaking law and map better onto the underlying hardware. [Much like speculative execution in processors](https://charlesfrye.github.io/programming/2023/11/10/llms-systems.html#speculative-execution), you can do more work in parallel without any change to behavior, at the cost of sometimes wasting work.

In speculative decoding, the parallelization comes from running the target model on a number of guessed or “speculated” tokens produced by a separate speculator model:

![](https://modal-cdn.com/blog/images/achieve-sota-specdec-specdec-diagram.webp)

Work is wasted when those guesses are incorrect, as in the final word in the diagram above. But for small batch sizes, transformer decoding without speculation doesn’t use all the [arithmetic bandwidth](https://modal.com/gpu-glossary/perf/arithmetic-bandwidth) of the GPU, and so even when much work is wasted, this needn’t slow down execution.

The resulting speedups from speculative decoding are not small *percentage* improvements, as in [kernel optimization](https://modal.com/blog/flash-attention-4-faster) or [host overhead reduction](https://modal.com/blog/host-overhead-inference-efficiency). They are small *multiplicative* improvements, roughly linear in the average number of accepted tokens (”acceptance length”):

![](https://modal-cdn.com/blog/images/achieve-sota-specdec-speedup-vs-acc-len-dflash.webp)

We present the general argument for the importance of speculative decoding and the key role of acceptance length in greater detail in [this article](https://modal.com/blog/spec-is-all-u-need).

The easiest way to achieve high acceptance lengths is to customize the speculator model to a particular application. We’ll explain that process in the context of a particular application: [Decagon Voice](https://decagon.ai/product/voice).

## Case Study: Decagon Agent Operating Procedures

[Decagon](https://decagon.ai/) is a unified platform to build, optimize, and scale AI agents that deliver concierge-level customer experiences across every channel. Voice is one of the most important of these channels. It’s a natural communication modality for humans, but it poses challenges for support automation:

- Fuzzy sound waves and language model inferences drawn from them need to be turned into crisp actions in the downstream system
- To feel natural and avoid frustrating human users responses need to be fast end-to-end/mouth-to-ear

Solving 1) is the core work of Decagon’s AI team as they build the [Decagon Agent Operating Procedures (AOP)](https://decagon.ai/product/aop) product. With everything from custom models to novel inference techniques, they work to map spoken natural language instructions to system actions with the precision and rigor of code.

We worked with them on 2): running the inference components of this system at the fastest speeds possible. [Every millisecond counts](https://x.com/akshat_b/status/1972000417937818054?s=20) — each one saved adds headroom for increased intelligence, additional features, added robustness, or reduced costs.

Focusing on one inference subsystem in particular, we took a baseline implementation on Modal that ran at ~290ms (p50) and cut off 100ms, beating the best latencies offered by proprietary inference providers for this same workload by over 60ms.

![](https://modal-cdn.com/blog/images/achieve-sota-specdec-latencies.webp)

## How we applied our low latency playbook to win

### Reducing communication latency, host overhead, and prefill latency

To keep communication latency between clients and hosts low, we used [Modal Servers](https://modal.com/docs/guide/servers). Modal’s [dynamic, global compute fleet](https://modal.com/blog/resource-solver) ensures we have GPU capacity [within milliseconds of your clients](https://modal.com/blog/physical-intelligence-runs-real-time-remote-inference-for-robotic-control-on-modal), wherever they are. Modal Servers wrap ultra light-weight regional proxies around auto-scaling pools of replicas running inside this fleet so that deployments don’t have to compromise on robustness and scalability to achieve low latency. More on how they work later this week!

![](https://modal-cdn.com/blog/images/achieve-sota-specdec-regionalized-server.webp)

When the input tokens of a request are being processed by the GPU(s), latency is primarily determined by the speed at which the GPU executes prefill [kernels](https://modal.com/gpu-glossary/device-software/kernel). High-quality kernels for key operations like grouped query attention or mixture-of-experts multi-layer perceptrons are available open source. We used these as a starting point and [contributed back](https://modal.com/blog/flash-attention-4-faster) our improvements.

In between an HTTP request and a kernel launch sits the inference engine. High-performance engines like vLLM and SGLang are available open source. They generally use the same GPU kernels, so the primary opportunity for improvement is in getting the CPU out of the way of the GPU — [avoiding host overhead](https://modal.com/blog/host-overhead-inference-efficiency). Again, we start from these engines and [contribute back](https://www.lmsys.org/blog/2026-06-15-next-generation-speculative-decoding-dflash-v2) our improvements, which we derive by profiling workloads, looking for GPU bubbles, and then removing synchronization or [speeding up host logic](https://modal.com/blog/boosting-multimodal-inference-performance-by-greater-than-10-with-a-single-python-dictionary).

### The big win: Speculative decoding and "mid-training"

These improvements alone were not yet enough to beat proprietary inference providers. The final win came from using a high-performance custom speculator model. As with other ML tasks, we don’t start from scratch these days. We want to start with pre-trained models and then train them further (”mid-training”) to apply them to our specific task.

#### "Pre-training" — Starting from generic draft models

Building off of [the work of the DeepSeek team](https://arxiv.org/html/2412.19437v1), many models are now released with multi-token prediction (MTP) heads that can be used for speculative decoding. These heads improve quality in training and performance in inference, so they’re something of a no-brainer.

But for that same reason, they are first-and-foremost a train-time optimization. Better performance at inference time can be had by training a distinct speculator model. However, MTP speculators have a nice advantage: they re-use the representations of the target model, which of course “knows best” about what it’s going to say next.

Contemporary speculative decoding techniques all take advantage of target model activations. We have found the best performance from [the DFlash technique](https://arxiv.org/abs/2602.06036), invented by Jian Chen and collaborators at [Z Lab](https://z-lab.ai/). This technique uses the KV projections from the target model, which reduces redundant computation by the draft and offers more opportunities for decoupling of host/device and draft/target work.

We had to add a custom op and Triton kernel to keep that projection snappy (e.g. batched across layers). It also generates draft tokens in parallel (a la BERT or a single-step diffusion), which makes it a better fit for modern hardware with high [ridge point arithmetic intensity](https://modal.com/gpu-glossary/perf/roofline-model).

We worked with Z Lab and SGLang to release high performance open source implementation and pre-trained speculator models, including a speculator for Qwen 3.5 397B-A17B that improves on MTP by over 50%.

![](https://modal-cdn.com/blog/images/achieve-sota-specdec-dflash-speedup.webp)

You can read more [here](https://www.lmsys.org/blog/2026-06-15-next-generation-speculative-decoding-dflash-v2/).

#### "Mid-training" — fine-tuning on task-specific synthetic data

Custom speculator models are fine-tuned on the specific task that the target model is being used for. Generally, speculator models need to be faster than the target model, which also makes them less intelligent. So fine-tuning is even more important here than it is in the target model!

We think of this as speculator “mid-training”. Mid-training is a recently-coined term for the training phase that comes after exposure to generic, Internet-scale data (”pre-training”). Mid-training comes before “post-training”, when models are improved through reinforcement learning. We foresee a future where speculators are trained via RL (on the acceptance length or even the speedup), which will neatly mirror this post-training.

Mid-training is a machine learning problem. That’s good, because ML problems generally fall not to algorithmic cleverness, which is hard to scale, but to data and compute, which are [easy to scale](https://modal.com/blog/llama-human-eval).

But that’s also bad, because [ML is hard, and many ML projects fail](https://fullstackdeeplearning.com/course/2022/lecture-8-teams-and-pm/#0-why-is-this-hard).

But mid-training a custom speculator is, in our opinion, “ML on easy mode”. The hardest problem in ML, making sure your data and your objective reflects the real world and your real goals, is essentially solved. Any ML project aims to replicate a data-generating process; here, the data-generating process is already an ML model, the target. Its data generation [can be understood](https://blog.nelhage.com/post/computers-can-be-understood/).

It also doesn’t hurt that the second hardest problem in ML is infrastructure, and [we know infrastructure](https://modal.com/blog/reinforcement-learning-infrastructure-problem).

But data isn’t always fully solved. Production systems often touch sensitive data — consider, say, the customer support line for a hospital. The possibility of side channel attacks on speculative decoding models is remote, but under-explored. And more concretely, access to user data is rightfully restricted, so research teams or external vendors like us often don’t get to see it.

The solution, as in other domains where data is scarce, is synthetic data. Especially in tasks with a strong grammar, like code generation or tool-calling or structured data extraction, synthetic data can capture much of what needs to be taught to the custom speculator.

For instance, an output like

```
{
	"action": <redacted>,
	"policy_id": <redacted>,
	"reasoning": <redacted>,
}
```
is still useful for training a speculator, so long as you fill in something reasonable for `<redacted>`. You can just use any and all public datasets to get vaguely-aligned prompts and pass them through the target to get the structured completions using the same grammar. Hallucination is here a feature, not a bug. This synthetic generated data can then be used to fine-tune the generic draft, without exposing any user data.

A small amount of the hornet’s nest of complexity in ML projects does shine through here. Since you’re no longer training on samples from production, you need to watch out for overfitting. We use additional data to track out-of-distribution performance, watching for major regressions. We find this predicts inability to generalize high acceptance lengths to the production system.

The custom DFlash speculator models we trained were able to cut another 100 ms off of end-to-end latency. That was about 40% of total server-side decode latency, taken off a strong baseline that already included speculative decoding.

With the custom speculator in place, we were a full 60ms faster than the fastest alternative.

![](https://modal-cdn.com/blog/images/achieve-sota-specdec-latencies.webp)

## Outcomes and what’s next

One of the outcomes that our friends at Decagon were [most excited about](https://x.com/cyrusasg/status/2061583081577050486?s=20) was the ability to self-serve their deployments on Modal — increasing developer velocity without needing to sacrifice performance or control.

The extra tens of milliseconds optimized inference bought them are a currency that they can spend elsewhere in their system to improve outcomes. An extra tool call or guardrail, a few dozen more `<thinking>` tokens from an orchestrator or agent to improve quality.

Right now, speculator training is fairly manual. Some of our customers do it themselves, perhaps triggering a training run on Modal whenever acceptance lengths decrease. We work with others to offer our [training and infrastructure expertise](https://modal.com/blog/reinforcement-learning-infrastructure-problem). But we anticipate a very near future where speculator systems continually improve based on accumulated data and agentic inference — `autospec` for Auto Endpoints. More on that soon.

If you want to join teams like Decagon, DoorDash, and Cognition who are deploying highly optimized inference that they control, come build on [Modal Auto Endpoints](https://modal.com/endpoints).
