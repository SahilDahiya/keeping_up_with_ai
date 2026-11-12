---
title: Introducing our Speculative Decoding Engine Builder integration for ultra-low-latency
  LLM inference
kind: blog
topic: inference
subtopic: speculative-decoding
secondary_topics: []
summary: Baseten's TensorRT-LLM Engine Builder gained a speculative-decoding integration
  with pre-optimized draft/target model configs, reportedly halving latency for production
  LLM workloads with no output-quality impact.
triage: null
skip_reason: null
source: baseten
url: https://www.baseten.co/blog/speculative-decoding-engine-builder-integration
author: Justin Yi
published: '2024-12-19'
fetched: '2026-11-12T06:09:28Z'
classifier: claude
taxonomy_rev: 2
words: 915
content_sha256: dbe306c7c7aa35f6214e0748ae02a743a99e62ca28b28f609c56e2829a521771
---

# Introducing our Speculative Decoding Engine Builder integration for ultra-low-latency LLM inference

News
# Introducing our Speculative Decoding Engine Builder integration for ultra-low-latency LLM inference

Our new Speculative Decoding integration can cut latency in half for production LLM workloads.


- Authors
- Date
- December 19, 2024

TLDR

With our new integration, you can add speculative decoding to your production LLM deployments as part of our streamlined TensorRT-LLM Engine Builder flow. Hit the ground running with pre-optimized config files or further tune settings according to your needs. If you're thinking about adding speculative decoding to your latency-sensitive LLM applications, talk to our engineers to see if it's the right fit!

From [live translation](https://www.baseten.co/customers/toby/) to chatbots and coding assistants, when it comes to latency-sensitive LLM applications, best-in-class performance is a requirement for successful products. Our customers uphold aggressive SLAs for their LLM services, targeting ultra-low time to first token (TTFT) and total response times—without compromising output quality for their users.

As our latest effort in making industry-leading model performance tools easily accessible to elite AI builders, we’re excited to introduce our **Speculative Decoding Integration** for our [TensorRT-LLM Engine Builder](https://www.baseten.co/blog/automatic-llm-optimization-with-tensorrt-llm-engine-builder/)!

Using our new integration, we’ve seen **latencies halved** with no effect on output quality. Use a pre-optimized configuration from Baseten engineers while retaining full control to tune settings further. This makes it easier than ever to leverage state-of-the-art model performance optimizations for your mission-critical production AI workloads.

Check out the demo by [Justin Yi](https://www.linkedin.com/in/justin-yi-6aa5a0173/), one of the lead engineers behind our new integration!

Our integration is useful for any low-batch, latency-sensitive application, but we’ll focus on a code generation use case here to make things concrete. For more technical details on how our engineers implemented the integration, check out the [technical deep dive](https://www.baseten.co/blog/how-we-built-production-ready-speculative-decoding-with-tensorrt-llm).

Instead of doing inference with one large LLM, speculative decoding (SpecDec) combines a larger (“target”) LLM with a smaller “draft” (or “speculator”) model. This way, instead of doing a full forward pass through the large model to generate each token, the smaller model can be used to predict easier tokens (like syntactical tokens based on grammar, or straightforward recall from earlier in the sequence).

Speculative decoding is an important tool for decreasing LLM latency, but it can be a mess to configure. With SpecDec, you’re handling two models instead of one, and you need to:

1. Select a good draft model.
2. Handle the interactions between your draft and target models.
3. In certain cases, further tune the draft model as a last resort.

These complexities are why other products on the market treat speculative decoding as a black box: you input your model and data, and your settings get automatically configured with minimal transparency. While this certainly makes SpecDec easier to use, it fails to provide developers with the visibility or control needed for production AI.

We want our customers to leverage powerful model performance techniques with the least amount of complexity. Nonetheless, we believe that power users should be able to use tools to their full extent. That’s why we took a two-tiered approach for our speculative decoding integration to provide ease of use without sacrificing control:

1. Our Engine Builder does the heavy lifting by handling the orchestration between draft and target models for minimal overhead.
2. Users can lift the hood to further tune parameters for their specific application.

As always, **our integration is production-ready** for mission-critical AI workloads. However, speculative decoding with draft models (e.g., using `DRAFT_TOKENS_EXTERNAL`) is an advanced feature that requires careful GPU memory allocation to accommodate both models simultaneously. If you plan to use this technique, consider consulting [the Baseten support team](https://baseten.co/talk-to-us) for guidance on optimal configuration.

Using SpecDec is as easy as using our existing Engine Builder flow: with a single config file, you can specify a build as minimal or complex as you want. Use a pre-optimized config built by Baseten engineers, or further tune parameters as you see fit. For instance, the sample config below works out of the box for latency-sensitive code generation applications, using Qwen 2.5 Coder 14B as the target model and 0.5B as the speculator (or draft) model.

yaml

```
model_metadata:
  tags:
  - openai-compatible
model_name: Qwen2.5-Coder-14B-Instruct (SpecDec)
resources:
  accelerator: H100
  cpu: '1'
  memory: 24Gi
  use_gpu: true
trt_llm:
  build:
    base_model: qwen 
    checkpoint_repository:
      repo: Qwen/Qwen2.5-Coder-14B-Instruct
      source: HF
    max_seq_len: 10000
    plugin_configuration:
      paged_kv_cache: true
      use_paged_context_fmha: true
    speculator:
      speculative_decoding_mode: DRAFT_TOKENS_EXTERNAL
      checkpoint_repository:
          repo: Qwen/Qwen2.5-Coder-0.5B-Instruct
          source: HF
      num_draft_tokens: 4
  runtime:
    enable_chunked_context: true
    kv_cache_free_gpu_mem_fraction: 0.62
    request_default_max_tokens: 1000
    total_token_limit: 500000
```
That said, there are scenarios where you might not want to use speculative decoding. For instance, under high load (when GPU usage is at or near 100%), running the draft model in addition to the larger one can cause performance bottlenecks. And if you’re already using relatively lightweight LLMs, the overhead of running two models could outweigh any performance gains.

Ideal use cases for our new integration are applications using large models in production (like Llama 3.1 70B or 405B), where those models’ smaller counterparts (like Llama 3.1 8B) are nearly as capable and can thus generate useful draft tokens.

Baseten exists to provide organizations with the best performance, reliability, and scalability for their mission-critical AI workloads in production. Since speculative decoding does not affect output quality, our new Engine Builder integration can be instrumental in improving LLM performance for many latency-sensitive use cases.

Check out our [technical deep dive](https://www.baseten.co/blog/how-we-built-production-ready-speculative-decoding-with-tensorrt-llm) to learn more about how our engineers built production-ready speculative decoding as part of our Engine Builder, [get started with our docs](https://docs.baseten.co/performance/engine-builder-config#speculator), or [talk to a Baseten engineer](https://www.baseten.co/talk-to-us/?model=LLMs%20optimized%20with%20speculative%20decoding) to see how we can boost your model performance in production!
