---
title: How to build a day-0 API for Kimi K3
kind: blog
topic: null
subtopic: null
secondary_topics: []
summary: null
triage: null
skip_reason: null
source: baseten
url: https://www.baseten.co/blog/how-to-build-a-day-zero-api-for-kimi-k3/
author: Model Performance Team
published: '2026-07-27'
fetched: '2026-07-28T06:51:23Z'
classifier: null
taxonomy_rev: 2
words: 2049
content_sha256: 8bed8dba4e0c438931d8f299e43a0b081b0bea56908b70ad23d00150093f4f3c
---

# How to build a day-0 API for Kimi K3

![How to build a day zero API for Kimi K3](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1785098868-kimi-k3-blog-philip.png%3Fauto%3Dformat%26fit%3Dcrop%26h%3D630%26w%3D1200&w=3840&q=100)

Baseten has day-0 support for Kimi K3 on our Model APIs. We want to thank Moonshot AI for sharing the Kimi K3 weights with us for early access, as well as the Inferact and RadixArk teams for their collaboration throughout the development process.

![Kimi K3 is available today on Baseten Model APIs with vision input and full 1M-token context window.](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1785162679-image4.png%3Fauto%3Dformat%26w%3D1200&w=3840&q=75) Kimi K3 is available today on Baseten Model APIs with vision input and full 1M-token context window.

Kimi K3 is available today on Baseten Model APIs with vision input and full 1M-token context window.Kimi K3 is a new open frontier model. At 2.8T parameters, it is much larger than any previous open model, introducing a number of challenges to building a performant inference API. New architectural techniques allow Kimi K3 to scale beyond the trillion-parameter threshold of prior frontier open models:

- Kimi Delta Attention (KDA) and Attention Residuals (AttnRes) as a scalable backbone for the Kimi Architecture. 
- Extremely sparse experts, with just 16 of 896 experts active at a time, organized using Stable LatentMoE. 
- A new vision encoder for processing image inputs and mapping visual information into latent space. 

This article describes the technical work required to run Kimi K3’s novel model architecture and huge weights at scale in time for launch day.

## Milestone 1: Generate a token

After receiving early access to the Kimi K3 weights from the Moonshot AI team, our first priority was to simply get the model up and running.

Generating our first tokens of Kimi K3 required:

- **Provisioning hardware:**Given the size of Kimi K3, we decided to run the model on NVIDIA GB300 NVL72 systems.
- **Loading weights:**In MXFP4, Kimi K3 weights are over 1.4TB of data.
- **Bringing up an inference engine:**We worked with the teams behind vLLM and SGLang to run pre-release builds of the inference engines for Kimi K3.

Often, when building day-0 APIs, an early step is porting the weights to NVFP4 to improve performance and compatibility with NVIDIA Blackwell and our inference stack. However, Kimi K3 uses native MXFP4 weights with MXFP8 activations, and we were able to use these weights directly.

With the weights in hand, we worked closely with Inferact on vLLM and RadixArk on SGLang. Before running Kimi K3 on the Baseten Inference Stack, we needed to establish a baseline in collaboration with the leading open-source inference engines.

Adding support for a model to an inference engine is non-trivial. It requires implementing core modeling code, optimized kernels for new architectures like KDA, and building frontend compatibility for Kimi K3 across everything from tokenization to tool calling.

vLLM’s early access image for NVIDIA Blackwell GPUs helped us establish basic feature completeness, pass initial evals, and set a baseline performance target. This work around accommodating Kimi K3 architectural features like KDA, AttnRes, and Stable LatentMoE formed a solid foundation for us to build on. We also did extensive validation of the vLLM inference engine for Kimi K3, and made contributions back to the open-source engine based on our work.

SGLang’s early access image provided a reference for fast, reliable serving of Kimi K3. SGLang has a history of strong support for vision language models, and Kimi K3 is no exception. With the RadixArk team, we focused on frontend compatibility and kernel optimization, and our engineering team contributed fixes for frontend bugs around tool call handling and structured outputs to support release readiness.

Thank you to the Inferact and RadixArk teams for building side by side with us throughout the preview window. This work provided both an essential foundation for our Kimi K3 API and an opportunity to contribute back to the open-source community.

## Milestone 2: Validate the inference engine

Kimi K3 is the smartest open model ever. It’s essential to actually deliver on that intelligence during inference.

![Kimi K3 benchmarks show strong performance on agentic tasks, which depend on accurate tool calls and high-quality model outputs.](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1785162782-image6.png%3Fauto%3Dformat%26w%3D1200&w=3840&q=75) Kimi K3 benchmarks show strong performance on agentic tasks, which depend on accurate tool calls and high-quality model outputs.

Kimi K3 benchmarks show strong performance on agentic tasks, which depend on accurate tool calls and high-quality model outputs.Quality validation can occur at different levels of rigor. Simple sanity checks, like calling the model with a known prompt or running a light benchmark like gsm8k or BFCL and checking if results are within the margin of error, are useful checkpoints during the development process to make sure that things aren’t going off the rails. But releasing a public API requires more rigorous benchmarking.

The Moonshot AI team operates [Kimi Vendor Verifier](https://github.com/MoonshotAI/Kimi-Vendor-Verifier), which helps inference providers ensure accurate, high-fidelity serving of model weights. Passing Kimi Vendor Verifier was an essential early milestone in our API development, and it was an extremely helpful tool throughout the development process.

There are lots of opportunities to mess up in serving models. While the popular narrative is that quantization is the root of all quality issues, in practice that is not true. Most quality issues, especially with tool calling and other structured model behaviors, come from the inference server frontend.

![The frontend sits in front of the inference engine and processes the inputs and outputs](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1785162967-image5.png%3Fauto%3Dformat%26w%3D1200&w=3840&q=75) The frontend sits in front of the inference engine and processes the inputs and outputs

The frontend sits in front of the inference engine and processes the inputs and outputsThe frontend is deterministic code that runs on the CPU in front of the inference loop. It is responsible for accepting inputs and returning outputs. The frontend must:

- Operate and validate the API 
- Tokenize prompts and detokenize outputs 
- Render the chat template 
- Parse reasoning and tool calls 
- Format the output to ChatCompletions, messages, or another standard 

These tasks are subtly different from model to model, and it is all too common to introduce bugs and performance degradation when building quickly for day-0 support. Robust checks like Kimi Vendor Verifier evaluate performance across common failure modes, like tool calling, to ensure the model is served with a high degree of fidelity across both the inference loop and the API surface.

As we continued to develop the API, we used Kimi Vendor Verifier at subsequent milestones to ensure that performance optimizations had not introduced bugs that would degrade accuracy.

## Milestone 3: Find the right configuration

Inference engines offer a wide range of configuration options to tune performance to different models, hardware, traffic shapes, and latency/throughput tradeoffs. These options, and the interactions between them, are complex.

To discover the right configuration, we do a sweep over various options like Tensor Parallelism (TP) and Expert Parallelism (EP) settings, Attention Data Parallelism (ADP) toggling, batch sizing, speculative decoder draft lengths, linear layer caching intervals, routing parameters, and inference engine settings.

![Tensor Parallelism and Expert Parallelism split large models across multiple GPUs.](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1785162807-image2.png%3Fauto%3Dformat%26w%3D1200&w=3840&q=75) Tensor Parallelism and Expert Parallelism split large models across multiple GPUs.

Tensor Parallelism and Expert Parallelism split large models across multiple GPUs.Running Kimi K3 requires eight NVIDIA GB300 GPUs to fit the enormous model weights into VRAM. However, unlike many other NVIDIA GPUs that come in nodes of eight, GB300s come in nodes of four. While this might initially appear to limit possible parallelism strategies – Tensor Parallelism is traditionally not possible across nodes as slow interconnects make expensive all-reduce operations a bottleneck for inference – the GB300 NVL72 system has a sufficiently fast interconnect between nodes that we can run inference with Tensor Parallelism and Expert Parallelism across nodes.

These configuration decisions are downstream of inference engine choice. Engineers worked in parallel to configure vLLM, SGLang, and our own in-house engine, sharing findings and applying learnings back to our in-house inference engine while also contributing PRs back to the open-source engines.

## Milestone 4: Optimize performance

Once a model is up and running on an optimized configuration, there are a large number of inference engineering techniques that can materially improve latency, throughput, or a combination thereof. For model APIs, we generally look at:

- **Speculation:**Using a small draft model to predict multiple tokens, then validating them as part of the forward pass. This lossless optimization improves per-user TPS on decode.
- **Disaggregation:**Move prefill and decode to separate workers. This prevents competition for resources, allows more targeted configuration, and makes the ratio of prefill to decode compute adjustable to match traffic.
- **Caching:**Allocating memory to save KV cache and KDA states between requests, allowing subsequent requests with shared prefixes in input sequences to skip all or part of prefill. This improves TTFT and overall system throughput.

Having the model up and running from previous milestones is a dependency for this work. For example, training a speculator model using a method like DSpark, [DFlash](https://www.baseten.co/blog/dflash-faster-llm-inference/), or [EAGLE-3](https://www.baseten.co/blog/how-to-train-custom-eagle-3-heads-for-speculative-decoding/#what-is-eagle-3) requires generating hidden states from the target model (Kimi K3) using a set of prompts that resemble expected real-world usage. To do this, you need a reasonably high-throughput instance of the model live and running inference.

One novel performance optimization was in the tokenizer. For years, inference engineers have been able to disregard tokenization time as negligible. For a model like Kimi K3 with long input sequences and high KV cache re-use rates, this actually changes, and tokenization can become material to prefill time, as tokenization must occur whether or not the input sequence is a cache hit.

We built a custom tokenizer that is up to 18x faster than tiktoken for long input sequences and rolled it out alongside our Kimi K3 API.

![Basetenkenizer is up to 18x faster than Tiktoken for long input sequences.](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1785162847-image1.png%3Fauto%3Dformat%26w%3D1200&w=3840&q=75) Basetenkenizer is up to 18x faster than Tiktoken for long input sequences.

Basetenkenizer is up to 18x faster than Tiktoken for long input sequences.There is still more work to be done on performance. With every model we launch, we continue to invest in latency and throughput optimizations in the weeks following release. With the unprecedented size of Kimi K3, there is a huge surface area for further performance improvement across every main inference engineering technique and every layer of the inference stack.

## Milestone 5: Deploy at scale

There is massive industry-wide excitement for Kimi K3. This will be matched by a huge wave of demand for the API at launch. Accordingly, system-wide throughput, not just per-user latency, is a top priority.

On a GB300 NVL72 system, a node is 4 individual GPUs, meaning there are 18 nodes. As an instance, Kimi K3 takes up 2 nodes (8 GPUs); each NVL72 rack can host 9 replicas of the model. Each cluster has multiple GB300 NVL72 racks, and we serve the model across multiple regions and cloud providers to access more capacity.

![Each NVL72 system can run nine replicas of Kimi K3.](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1785162923-image3.png%3Fauto%3Dformat%26w%3D1200&w=3840&q=75) Each NVL72 system can run nine replicas of Kimi K3.

Each NVL72 system can run nine replicas of Kimi K3.The most consequential factor for a given replica’s throughput is prefix cache hit rate. Given the scale of the deployment, this makes KV-aware routing the primary challenge to solve on infrastructure. When a user sends a sequence of input tokens that we’ve seen before, we need to route that request to a replica that can access the saved KV cache to skip prefill.

Our KV-aware routing system, built with the NVIDIA Dynamo toolkit, ensures that we are able to route traffic to replicas with warm caches for repeat queries. As coding and multi-turn agents are common use cases for Kimi K3, this cache-aware routing system is critical for saving users money and maintaining high total system throughput.

## Build with Kimi K3 on Baseten

We’re excited to offer day-0 access via Model APIs, and look forward to continuing to optimize our implementation of this model to achieve the highest standards in performance and reliability.

The Moonshot AI team’s [Kimi K3 announcement](https://www.kimi.com/blog/kimi-k3) includes a number of interesting tests for the model, including coding tasks like kernel optimization and vision-in-the-loop game development, research tasks, and agentic tasks like video editing and knowledge work. On Tuesday, July 28 at 11AM Pacific Time, we are [hosting an executive briefing on Kimi K3](https://www.baseten.co/resources/webinar/executive-briefing-on-kimi-k3/) use cases with [Joey Zwicker](https://www.linkedin.com/in/josephzwicker/), who leads all forward-deployed engineering at Baseten, and [Philip Kiely](https://x.com/philipkiely), author of *Inference Engineering*.

[Kimi K3 is available today on Baseten Model APIs](https://www.baseten.co/library/kimi-k3/). Welcome to the new frontier in open weight intelligence.
