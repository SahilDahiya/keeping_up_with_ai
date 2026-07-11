---
title: The Baseten Inference Stack at NVIDIA Dynamo Day
topic: inference
subtopic: serving
secondary_topics:
- inference/optimization
summary: Describes Baseten inference-stack ideas presented around NVIDIA Dynamo and
  production serving.
source: baseten
url: https://www.baseten.co/blog/nvidia-dynamo-day-baseten-inference-stack/
author: Rachel Rapp
published: '2026-02-03'
fetched: '2026-07-11T04:06:25Z'
classifier: codex
taxonomy_rev: 1
words: 1236
content_sha256: 5930481632d7c6e084afc9347a930c569f6e5172466ad8817184adde932d17ca
triage: keep
skip_reason: null
---

# The Baseten Inference Stack at NVIDIA Dynamo Day

![NVIDIA Dynamo Day and The Baseten Inference Stack](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1770036136-announcement-important-text-template-8-1.png%3Fauto%3Dformat%26fit%3Dcrop%26h%3D630%26w%3D1200&w=3840&q=100)

**Update: NVIDIA announced ****Dynamo 1.0**** at GTC!**

[The Baseten Inference Stack](https://www.baseten.co/resources/guide/the-baseten-inference-stack/) powers our Dedicated Inference and Model APIs, delivering the lowest latency, highest throughput, and highest uptime for generative AI workloads. We achieve this by combining open-source and in-house tools—runtime engines, scheduling layers, and model-specific optimizations—and using each as best suited to a particular model and use case.

One of those tools is [NVIDIA Dynamo](https://developer.nvidia.com/blog/nvidia-dynamo-1-production-ready/?ncid=partn-888910). We like Dynamo because it’s framework-agnostic, so it doesn’t stop us from choosing the best inference engine (TensorRT-LLM/SGLang/vLLM) for a specific model and use case. We also love that it’s open-source, with biweekly releases and ~90 commits per week (our engineers are frequent contributors to the Dynamo and TensorRT-LLM ecosystems, shipping [fixes](https://github.com/ai-dynamo/dynamo/pull/5497), [new features](https://github.com/ai-dynamo/dynamo/pull/3748), and [performance improvements](https://github.com/ai-dynamo/dynamo/pull/3370)—we also just open-sourced our Suffix Automaton MTP Accelerator from the Baseten Speculation Engine [here](https://www.baseten.co/blog/boosting-mtp-acceptance-rates-in-baseten-speculation-engine/)).

We were excited to present our work using NVIDIA Dynamo at massive scale at [Dynamo Day](https://nvevents.nvidia.com/dynamoday?ncid=so-link-211895&linkId=100000401834089) for thousands of attendees. Here are some of the highlights of the event and features we’re looking forward to working more closely with.

![Screenshot from Baseten’s Lead DevRel, Philip Kiely’s talk at Dynamo Day on how we use NVIDIA Dynamo as part of the Baseten Inference Stack (along with different inference engines including TensorRT-LLM, SGLang, and vLLM).](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1770039917-image2.png%3Fauto%3Dformat%26w%3D1200&w=3840&q=75) Screenshot from Baseten’s Lead DevRel, Philip Kiely’s talk at Dynamo Day on how we use NVIDIA Dynamo as part of the Baseten Inference Stack (along with different inference engines including TensorRT-LLM, SGLang, and vLLM).

Screenshot from Baseten’s Lead DevRel, Philip Kiely’s talk at Dynamo Day on how we use NVIDIA Dynamo as part of the Baseten Inference Stack (along with different inference engines including TensorRT-LLM, SGLang, and vLLM).## NVIDIA Dynamo Day: The highlights

For those needing a primer (or a refresher), [NVIDIA Dynamo](https://developer.nvidia.com/dynamo) is an inference framework built for serving and scaling generative AI workloads in distributed environments. We use Dynamo daily for our customers in production, and our engineers take those learnings to improve Dynamo itself and contribute back to the project (some examples [here](https://github.com/ai-dynamo/dynamo/pulls?q=is%3Apr+is%3Aclosed+author%3Amichaelfeil) and [here](https://github.com/ai-dynamo/dynamo/pulls?q=is%3Apr+author%3Ablarson-b10+is%3Aclosed)). As a result, we achieve metrics like a 50% reduction in time to first token (TTFT), 34% reduction in time per output token (TPOT), and 61% higher throughput on workloads with long inputs and outputs (check out the benchmarks [in our blog here](https://www.baseten.co/blog/how-baseten-achieved-2x-faster-inference-with-nvidia-dynamo/#qwen3-coder-benchmarks-with-kv-routing)).  

Dynamo is all about improving system-level inference performance via three main optimizations:

- Disaggregated serving
- KV cache-aware routing
- KV cache offloading

The whole is greater than the sum of its parts (pardon the cliché)—each optimization compounds the performance gains of the others when used together.

At Dynamo Day, technical leads, engineers, and product managers covered topics including:

- The challenges of serving Mixture of Expert-architecture models at scale
- How Dynamo works under the hood + key features and community growth
- The OSS inference ecosystem featuring vLLM, SGLang, llm-d, and TensorRT-LLM
- Learnings from Dynamo users (featuring our Lead DevRel, - [Philip Kiely](https://x.com/philipkiely), alongside technical team members from Pinterest and Prime Intellect)
- The state of inference today and upcoming trends

NVIDIA’s team touched on several features we’re excited about—more on those below.

## Dynamo in The Baseten Inference Stack

Features of Dynamo that we actively use (or are keen to use more heavily) include Dynamo’s native support for disaggregated prefill and decode, broader support for multimodal model serving (including recently added support for vLLM), and KV cache offloading.

We’re also heavy users of Dynamo’s KV cache-aware routing—[check out our blog](https://www.baseten.co/blog/how-baseten-achieved-2x-faster-inference-with-nvidia-dynamo/) to learn more about the 34%-62% performance gains we see while using it in production.

### Disaggregated serving (prefill / decode)

LLM inference has two phases: prefill and decode. During the prefill phase, context is loaded and a Key-Value (KV) cache is built; during decode, a response is generated token by token.

Prefill is compute-bound, and affects time to first token (TTFT)—you can think of it as the LLM “thinking” before it “speaks.” Decode is memory-bound and measured by inter-token latency (ITL) or time per output token (TPOT)—this is the LLM’s generation speed. When prefill and decode are done together on a single GPU, long, compute-heavy prefill work can block latency-sensitive token decoding and lead to poor GPU utilization under load.

Disaggregating prefill and decode phases (i.e., assigning them to different GPUs) means you can optimize for both TTFT and TPOT by scaling and optimizing for each phase separately, like applying tensor parallelism for prefill and expert parallelism for decoding. By removing the bottleneck, disaggregated serving can also massively increase throughput (tokens per second, TPS)—up to 6x higher TPS per GPU is realistic.

![Screenshot from Harry Kim’s talk “State of NVIDIA Dynamo” explaining disaggregated serving.](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1770039957-image1.png%3Fauto%3Dformat%26w%3D1200&w=3840&q=75) Screenshot from Harry Kim’s talk “State of NVIDIA Dynamo” explaining disaggregated serving.

Screenshot from Harry Kim’s talk “State of NVIDIA Dynamo” explaining disaggregated serving. Dynamo includes an AIConfigurator that suggests good configurations for disaggregated serving with SGLang, TRT-LLM, and vLLM, given a target model, hardware, input and output lengths, and your TTFT and ITL/TPOT SLAs.

Similar to our [KV cache-aware routing post](https://www.baseten.co/blog/how-baseten-achieved-2x-faster-inference-with-nvidia-dynamo/), we have new benchmarks coming out in the next few weeks on the throughput gains we see using disaggregated serving for high-traffic workloads—stay tuned!

### Multimodal model serving 

Building on disaggregated serving and text-based KV cache reuse, Dynamo provides native support for an Encode → Prefill → Decode (EPD) pattern that can encode images as well as text for multimodal models. Support for an embedding cache is also expected in the coming months, which will further reduce latency (TTFT) by skipping encoding repeated inputs (such as images/videos).

As we scale up our multimodal features, we’re excited to use these in our Dedicated Inference and Model APIs.

![A screenshot of the multimodal serving workflow from Kyle Kranen’s talk at Dynamo Day, “Under the Hood: Dynamo Inference for Multimodal AI Workloads.”](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1770039907-image3.png%3Fauto%3Dformat%26w%3D1200&w=3840&q=75) A screenshot of the multimodal serving workflow from Kyle Kranen’s talk at Dynamo Day, “Under the Hood: Dynamo Inference for Multimodal AI Workloads.”

A screenshot of the multimodal serving workflow from Kyle Kranen’s talk at Dynamo Day, “Under the Hood: Dynamo Inference for Multimodal AI Workloads.”### KV cache offloading

KV cache offloading uses the full memory hierarchy to store KV cache (like CPU, local SSD, or network/remote storage) and bring it back as needed, allowing higher concurrency and context lengths without GPU memory becoming the bottleneck.

In Dynamo, KV blocks are managed by the KV Block Manager, and data moves across tiers via NIXL (NVIDIA Inference eXchange Layer), a low-level library used by Dynamo to efficiently move inference state between GPUs, CPUs, and nodes.

With disaggregated serving, KV offloading reduces TTFT enough that you can run fewer prefill workers, freeing up GPU capacity. With KV-aware routing, more storage tiers can also improve the KV hit rate, further reducing TTFT. We currently use KV cache offloading via TensorRT-LLM, with support for Dynamo as needed.

## Final thoughts

We use open-source tools like NVIDIA Dynamo, as well as OSS frameworks like TensorRT-LLM, SGLang, and vLLM, to best serve each individual workload with the Baseten Inference Stack. Our engineers harden these tools for production and iterate on them to push the limits of model performance, frequently shipping these improvements back to the OSS community.

If you want to learn more about the different tools and techniques we use to achieve 99.99% reliability along with the highest throughput and lowest latency on the market, check our guide on [The Baseten Inference Stack](https://www.baseten.co/resources/guide/the-baseten-inference-stack/).
