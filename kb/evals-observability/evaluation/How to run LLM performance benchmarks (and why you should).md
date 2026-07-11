---
title: How to run LLM performance benchmarks (and why you should)
topic: evals-observability
subtopic: evaluation
secondary_topics:
- inference/serving
summary: Explains how to run LLM performance benchmarks and which serving metrics
  matter.
source: baseten
url: https://www.baseten.co/blog/how-to-run-llm-performance-benchmarks-and-why-you-should/
author: Alex Ker; Bryce Dubayah
published: '2026-02-05'
fetched: '2026-07-11T04:06:21Z'
classifier: codex
taxonomy_rev: 1
words: 1485
content_sha256: 397950585507b99c2cc92e2e0b4bdb2d9cf05d376698f4b5b32e9431d84f423f
triage: keep
skip_reason: null
---

# How to run LLM performance benchmarks (and why you should)

![LLM performance metrics](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1773096546-llm-performance-metrics_blog.png%3Fauto%3Dformat%26fit%3Dcrop%26h%3D630%26w%3D1200&w=3840&q=100)

LLMs are simulacrums of human behavior, or as Andrej Karpathy described them, stochastic "people spirits." This emergent quality makes them notoriously hard to evaluate in terms of speed and quality: performance depends on the model, the hardware, the workload, the batch size, and a dozen other factors that interact in non-obvious ways.

Industry-standard LLM performance benchmarking is helpful but difficult to do well. One group that's done it right is SemiAnalysis with [InferenceMAX](https://inferencemax.semianalysis.com), a comprehensive benchmark that tests popular models across common hardware configurations, with results focused particularly on inference speed rather than output quality, giving the community solid reference points for throughput and latency.

But there’s one caveat: these LLM performance benchmarks measure how off-the-shelf models perform on generic workloads. You probably care about how *your* model performs on *your* data. The only way to know is to run benchmarks yourself.

In this series, we'll show you how. In this post, we’ll walk through replicating InferenceMAX on Baseten by running off-the-shelf TensorRT-LLM, which should be extensible to other similar performance benchmarks. In part two, we'll show how the [Baseten Inference Stack](https://www.baseten.co/resources/guide/the-baseten-inference-stack/) (BIS) with speculative decoding techniques like a well-selected [EAGLE](https://github.com/SafeAILab/EAGLE) or [Suffix Automaton MTP Accelerator](https://www.baseten.co/blog/boosting-mtp-acceptance-rates-in-baseten-speculation-engine/) can push LLM performance further for use cases like code generation. You’ll learn to identify the best providers from the worst, as well as understand if a model is sufficient vs. truly good for your task. Along the way, you'll pick up some patterns to make you more effective at model evaluations.

We chose to reproduce InferenceMAX’s “Token Throughput per GPU vs. End-to-End Latency” numbers for B200s on TRT-LLM with the TP4EP1 configuration, specifically the lower concurrency settings, more on that later. Quick primer: Tensor Parallelism (TP=4) slices the model's weight tensors across four GPUs, while Expert Parallelism (EP=1) controls how mixture-of-experts layers are distributed (in this case, there's no expert parallelism).

For long-context workloads like coding or document processing, visualizing the trade-off between throughput and end-to-end latency is particularly useful. In code generation, for example, a lower concurrency setting is recommended to improve latency and maximize developer experience, while accepting the hit in throughput and cost. This is a core tradeoff surfaced by well-designed LLM performance benchmarks.

## How to reproduce InferenceMAX

### Provisioning and config

We provisioned 4xB200s on a dedicated Baseten deployment.

- We set up the config.yaml, (the way to configure dependencies, resources, and other settings for your model on Baseten) to match the exact TensorRT-LLM image that InferenceMAX used, we pulled the exact image from their GitHub action, https://github.com/InferenceMAX/InferenceMAX/actions/runs/18978812542, nvcr.io/nvidia/tensorrt-llm/release:1.2.0rc2.
- We mirrored the setup taken from the /benchmarks and /runners folder to create our own benchmark scripts: - `run_baseten_comparsion.sh`as the runner scripts that calls- `gptoss_baseten.sh`at various concurrency settings. A critical note is that we had to use the /completions endpoint rather than the /chat-completions endpoint and the- `ignore_EOS`flag for benchmarking OSS to reach the desired number of tokens.
- We then trussed up the deployment with - `truss push --publish`and collected results from the three runs and averaged them to produce the throughput/gpu vs. end-to-end latency graph.

### Cold starts / model cache

A common issue in model serving is being responsive to traffic during cold starts, or handling incoming requests in a reasonable time when there are zero replicas. To improve cold-starts and avoid redownloading weights whilst iterating on the deployment, we used model_cache for GPT-OSS-120B. For docker servers, we included `truss-transfer-cli` in start_commands, to force populate of the `/app/model_cache `location, which is used to store the model weights we will reference later. For any Hugging Face model, below is how you would use Baseten's distributed model cache:

```
model_cache:
- repo_id: openai/gpt-oss-120b  
  revision: main  
  use_volume: true  
  volume_folder: gpt_oss_120b
```
Read more about model cache here: [https://docs.baseten.co/development/model/model-cache](https://docs.baseten.co/development/model/model-cache)

## LLM Benchmarking methodology

### Client-side vs. server-side

To avoid network latency and mirror the InferenceMAX setup, we adapted the benchmark to run server-side on Baseten. Because the benchmark script lived on the same machine as the model server, it hit the local endpoint (`http://localhost:8000/v1)` rather than making requests over the public internet. This isolates the model's inference performance from network variability—you're measuring pure GPU throughput and latency without the noise of round-trip times, TLS handshakes, or regional routing. We created a script called startup_and_benchmark.sh to first start the TRT-LLM server in the background, then run the benchmarks against this local server.

For any serious LLM inference benchmark, isolating network variables is critical to understanding true hardware-level LLM performance.

However, for testing inference performance in your applications, it will be best to benchmark from client side because that is more closely aligned with the UX in the wild. But since InferenceMAX benchmarks and compares hardware performance, server-side was the right approach here. A good rule of thumb: server-side benchmarks tell you what the hardware can do, while client-side benchmarks tell you what your users actually experience. Both perspectives matter when designing comprehensive LLM performance benchmarks.

![trtllm-serve run averages on Baseten closely mirrors and aligns with the InferenceMAX baseline for the TP4EP1 GPT-OSS-120B 1k tokens input/1k tokens output.](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1770236411-image1.png%3Fauto%3Dformat%26w%3D1200&w=3840&q=75) trtllm-serve run averages on Baseten closely mirrors and aligns with the InferenceMAX baseline for the TP4EP1 GPT-OSS-120B 1k tokens input/1k tokens output.

trtllm-serve run averages on Baseten closely mirrors and aligns with the InferenceMAX baseline for the TP4EP1 GPT-OSS-120B 1k tokens input/1k tokens output.## Three benchmarking nuggets

**1. Use DevEx constructs to shorten your development flow. **

Benchmarking is iterative. You will tweak configs, adjust concurrency settings, and rerun tests dozens of times before landing on the right setup that gives you something informative about your workload. Anything that slows down this cycle compounds quickly. We've highlighted a few infrastructure features that kept our iteration tight: caching to avoid redownloading weights for billion parameter models, server-side benchmarking against localhost to eliminate network variability, and scripting patterns like startup_and_benchmark.sh to automate the start-measure-analyze cycle. Shortening the feedback loop between changing config to getting results will invariably help you increase the quality of your benchmarks, and downstream models, more efficiently.

**2. Dataset selection is the foundation.**

For this specific replication, we used the random dataset, which is a sample of random tokens from the vocab. At Baseten, we take a three-prong approach from the forward deployed engineering team when working with other ML teams:

- **Use production data as gold standard.**If you have existing data from your customers or application that the model will consume in production, take a subset and gather relevant performance metrics: tokens-per-second, time-per-output-token (inter-token latency), time-to-first-token, and end-to-end latency. Understanding how these metrics shift as your workload scales is extremely useful.
- **Use public datasets as proxies.**If no production data exists, there are many datasets on Hugging Face—WizardLM (user + assistant conversations) or code_edits_sample (code edits)—that can mimic your usage patterns and plug nicely into benchmarks like InferenceMAX. We'll show this in part 2.
- **Use synthetic data for quick vibe-checks.**Frontier models like Claude work well as synthetic benchmark data generators. For ruling out models or providers that clearly don't perform, a synthetic dataset can be enough to get directional numbers.

**3. Benchmarking will be frustrating to set up, but it's worth your time.**

Establishing robust performance evaluations is essential as you scale as this is intimately tied to downstream user experience. Set this up as early as possible; it will become a critical data point for deciding which model, configuration, and provider supports you best. Without LLM performance benchmarks, you're flying blind, and that can lead to user churn as you scale. Think of benchmarks as an early-alerting system for your team. You can create a fork based on popular and well-maintained open source benchmarks, such as [https://github.com/sgl-project/genai-bench](https://github.com/sgl-project/genai-bench) that we have forked at Baseten, as a great starting point.

## Conclusion and what’s next

For this experiment, we used InferenceMAX's random dataset—a sample of random tokens from the vocabulary. This works for measuring baseline inference performance benchmarks, but it's a poor fit for benchmarking speculative decoding techniques like EAGLE. EAGLE uses a lightweight draft model to predict upcoming tokens. Because the draft model was trained on real language patterns, it can't predict effectively when given random noise as context; that’s why speculation fails and there's no speedup.

The broader point: improving [inference ](https://www.baseten.co/blog/ai-inference-explained/)performance is the central piece of the puzzle to get the maximum return on investment for your models, and benchmarking is the only way to know if your optimizations are actually working. If you're benchmarking incorrectly, the result is a poorly optimized model in production without you even realizing it. The right benchmark setup depends on your workload, and there are many techniques that can improve performance once you know where to look.

So in part two, we'll dive into a realistic dataset and show how BIS (Baseten's optimized inference stack) with EAGLE pushes performance for GPT-OSS-120B. We'll cover latency-sensitive use cases like code generation and general conversational workloads, showing how these techniques affect per-user experience and scale across concurrencies.
