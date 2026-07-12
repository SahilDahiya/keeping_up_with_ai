---
title: How we built production-ready speculative decoding with TensorRT-LLM
topic: inference
subtopic: optimization
secondary_topics:
- inference/serving
summary: Deep dive into production-ready speculative decoding with TensorRT-LLM.
source: baseten
url: https://www.baseten.co/blog/how-we-built-production-ready-speculative-decoding-with-tensorrt-llm/
author: Pankaj Gupta; Justin Yi; Philip Kiely
published: '2024-12-19'
fetched: '2026-07-11T04:08:38Z'
classifier: codex
taxonomy_rev: 1
words: 2835
content_sha256: 5660d14b321b1da36def5aa480199d0e61b823021bdf59431b33d3bf282096b1
triage: keep
skip_reason: null
---

# How we built production-ready speculative decoding with TensorRT-LLM

![Speculative Decoding with TensorRT-LLM](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1747434660-spec-dec.png%3Fauto%3Dformat%26fit%3Dcrop%26h%3D630%26w%3D1200&w=3840&q=100)

Speculative decoding is an LLM inference optimization technique that can cut latency in half – in theory. In practice, applying speculative decoding to production model inference tasks requires careful implementation to deliver reliable speed improvements. This post details our efforts in productionizing speculative decoding with a focus on reducing latency for code generation tasks.

Speculative decoding is an inference optimization technique designed to improve the latency of LLM inference by coordinating two models on a single model server: a larger target model (e.g. Llama 70B) and a smaller draft model (e.g. Llama 8B). In theory, speculative decoding lets us combine the larger model’s quality with the smaller model’s speed, though only at limited batch sizes.

Running a single optimized LLM on a model server is already a challenge. Running two models in a coordinated fashion multiplies this challenge. To [support speculative decoding in our TensorRT-LLM Engine Builder](https://www.baseten.co/blog/speculative-decoding-engine-builder-integration/), we had to tackle a host of issues preventing speculative decoding from working seamlessly in production:

- **Inefficient batching**: requests were either failing to batch or performance was dropping massively at batch sizes higher than 1.
- **High TTFT**: architectural issues meant it took a long time to generate the first token of LLM output.
- **Crashes and unreliability**: without clean orchestration, the model server was prone to crashing.

We also realized that our customers required support for a set of advanced features like streaming, structured output, and request cancellation, all delivered in an OpenAI-compatible output specification. We’ll describe how we overcame all of these issues in this post.

We focused on code generation as our first production-ready use case. Code generation has a few things that make it a particularly good candidate for speculative decoding:

- **Code generation is latency-sensitive**: for code completion, users want results fast. And code is generally more token-dense than writing, so the inter-token latency speedups are more impactful.
- **There are great models available**: families like Qwen 2.5 Coder come in many sizes, offering us great choices for both draft and target models.
- **Code is predictable**: code is a relatively constrained output space with syntactical patterns that are easy for small models to handle, increasing the likelihood of draft token acceptance.

If you’re not familiar with the mechanics of speculative decoding, check out our [introduction to speculative decoding](https://www.baseten.co/blog/a-quick-introduction-to-speculative-decoding/) for a full explanation of how the process works. In this blog, we’ll thoroughly discuss the performance advantages and limitations of speculative decoding, the steps we took to implement reliable speculative decoding support into TensorRT-LLM, and benchmark results we observed for code generation use cases. If you’re interested in optimizing inference for your LLMs with speculative decoding, [check out our launch blog](https://www.baseten.co/blog/speculative-decoding-engine-builder-integration/) or [talk to a Baseten engineer](https://www.baseten.co/talk-to-us/?model=LLMs%20optimized%20with%20speculative%20decoding) to see how we can boost your model performance in production.

## Speculative decoding in TensorRT-LLM

TensorRT-LLM is a highly performant model inference optimization framework. We use TensorRT-LLM heavily, most notably in our [TensorRT-LLM Engine Builder](https://www.baseten.co/blog/automatic-llm-optimization-with-tensorrt-llm-engine-builder/), to optimize model inference.

While TensorRT-LLM supports speculative decoding, we found it still takes a fair bit of work to get things production-ready.

Considering the core loop in speculative decoding:

- Call the draft model with existing tokens to generate N tokens.
- Call the target model with existing tokens + N draft tokens. Target model accepts a subset of the draft tokens and generates an additional token.
- Call the draft model with these new tokens to generate N more tokens.

![In the speculative decoding core loop, draft tokens are generated, a prefix is accepted, and the target model generates an additional token](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1734626136-specdec.png%3Fauto%3Dformat%26w%3D1200&w=3840&q=75) In the speculative decoding core loop, draft tokens are generated, a prefix is accepted, and the target model generates an additional token

In the speculative decoding core loop, draft tokens are generated, a prefix is accepted, and the target model generates an additional tokenIt is critical that these repeated calls to the draft and target model only do incremental work, not start from scratch. Therefore, TensorRT-LLM’s speculative decoding implementation relies heavily on KV cache re-use. Its highly efficient implementation keeps the overhead of each new request low. Without efficient KV cache re-use, speculative decoding would not be feasible in TensorRT-LLM.

However, the existing implementation has some shortcomings that need to be addressed before going into production.

## Problems with speculative decoding

In the introduction to this piece, we laid out three issues that needed to be addressed before speculative decoding was production-ready:

- Non-existent or inefficient batching
- Slow time to first token
- Model server crashes

Two key improvements solved these problems: better draft-target model coordination and careful batch support.

### Draft-target model coordination

Out of the box, the draft and target models had a tendency to fight for resources when run on the same GPU, leading to degraded performance – the model would run at half speed when they were in contention.

One seemingly easy way to solve this problem would be to run the draft and target models on different GPUs. However, this is not an ideal solution because of GPU utilization. Draft models need a very small amount of compute compared to target models, making efficient packing very challenging:

- Giving the draft and target model 1 GPU each is wasteful as the draft model barely uses its GPU.
- Using an 8-GPU machine and giving 1 GPU to the draft model and the other 7 to the target model is still likely wasteful and limits hardware flexibility.
- Any fixed combination of GPUs restricts your hardware choice significantly and makes it hard to pack multiple replicas efficiently onto nodes.

Instead, we synchronize the execution of the draft and target model, so only one can run on the GPU at a time.

This requires a simple async loop where the draft and target workers run in sequence, each reading from its own dedicated queue. This setup is similar in spirit to the in-flight batching loop found in inference frameworks like TensorRT-LLM.

Synchronized model execution addresses our three main issues by:

- Unlocking batching with scheduled and queued worker execution.
- Improving TTFT by letting us schedule target model inference ahead of draft model inference for the first token.
- Avoiding certain server crashes caused by model contention for resources.

However, it does not solve our problems entirely, especially around batching.

### Efficient batch inference

In our first attempt at running a model server with speculative decoding, we set up a naive implementation where we simply fed each input request to the TensorRT-LLM runtime sequentially in a quick loop. While we didn’t wait for requests to finish before sending the next one, TensorRT-LLM was batching draft model requests poorly and wasn’t batching target model requests at all.

In retrospect, the issue is clear: the target model only executes one inference step. It runs as soon as it receives the first request, so the second request runs on the next step.

We resolved this by implementing a mechanism in the custom C++-based GRPC server that we use in the place of Triton when running TensorRT-LLM. We indicate that the request is part of a batch, so the server waits until all requests in the batch arrive before feeding them into TensorRT-LLM.

While this made the model server start batching, we observed another issue: the batch sizes were much smaller than expected. For a load where we might expect a batch size of 10, we were only seeing 2 or 3 requests processed at once.

This issue was more nuanced. We found that it was related to an interaction between three components of TensorRT-LLM: the request scheduling mechanism, KV cache re-use, and chunked prefill. Specifically, TensorRT-LLM wasn’t accounting for KV cache re-use when doing requests scheduling with respect to chunked prefill.

#### An aside on chunked prefill in TensorRT-LLM

Prefill is the part of an LLM request where the input is processed before token generation. This step is compute-bound, while the actual token generation is usually bound by memory bandwidth. However, processing all of the prefill tokens together can require a large amount of memory. For large models and long input sequences, this can take tens or hundreds of gigabytes of GPU VRAM.

Chunked prefill is the idea of doing this step in pieces, where each chunk is large enough to remain compute-bound but small enough that it doesn’t take a huge portion of the GPU memory. This value is generally between 1024 and 4096 tokens and is specified with the max_num_tokens setting.

In speculative decoding, the draft and target model are called repeatedly. After the first call, all of this prefill work is done and stored in the KV cache. However, the TensorRT-LLM request scheduler doesn’t account for the fact that we’re reusing the KV cache, thinking instead that the whole request needs to be prefilled. As such, it tries to fit the request in around the max_num_tokens setting. As a result, it often thinks there is only room for one or two requests to get scheduled to run together.

We fixed this issue inside of the TensorRT-LLM runtime, correcting it to account for the KV cache re-use in the request scheduling, and provided this patch to the TensorRT-LLM team for merging.

We also found and provided a patch for a bug in the TensorRT-LLM decoding while working with draft tokens.

With this debugging work, we were able to make further improvements to our key batching and stability issues:

- Improving batch performance and GPU utilization through bug fixes.
- Reducing GPU memory usage by enabling chunked prefill alongside batch inference.
- Avoiding server crashes from these bugs and providing patches to the maintainers.

However, we still observe steep performance drops when under high load. Based on TensorRT-LLM’s heavy reliance on KV cache re-use, if you fully utilize the KV cache’s memory allocation, this leads to repeated prefill computations, significantly degrading performance. It is essential to ensure that requests are scheduled with an upper limit on combined tokens for all requests in progress to avoid running out of KV cache.

Newer hardware offers other options, like an offloaded KV cache stored on CPU RAM. For hardware like the H100, H200 and GH200 with high GPU-GPU memory bandwidth, a CPU-based KV cache could serve as a viable option for higher batch sizes.

## Building production-ready speculative decoding

With these essential problems addressed, there was still more to do to make speculative decoding ready to use in production. We still needed to support several important features that AI engineers need from LLMs.

### Streaming support

Many LLM use cases require streaming output token-by-token as it is generated, so streaming support with speculative decoding was absolutely essential. In our custom C++ version of the Triton inference server, we implemented support for streaming output.

### Structured output support

Recently, we launched structured output support for the TensorRT-LLM Engine Builder, enabling LLMs to output structured text like JSON as well as support function calling with structured parameters. This feature works using the outlines library, which generates logit masks based on a provided schema and applies them during inference using a state machine.

We updated the CUDA kernel that we use for logit mask implementation to be compatible with speculative decoding, so you can use speculative decoding to speed up the generation of structured output.

### Request termination support

LLMs can stop generating output for multiple reasons: generating an end of sequence token, generating stop words, and reaching a maximum token count specified in the request, in the model server configuration, or by the model’s own context window.

Our speculative decoding implementation stops when required by any of these request termination methods.

### OpenAI spec support

Sometimes, AI engineers like to ensure that model servers closely adheres to the OpenAI input and output spec for ease of development. This is supported by our TensorRT-LLM Engine Builder and by extension our speculative decoding implementation.

While speculative decoding performance degrades when the model is given more creative freedom (e.g. high temperature, high top_k, high top_p) as the token distribution gets less predictable, our speculative decoding implementation does honor all sampling settings.

Every aspect of the OpenAI model spec was carefully implemented into our runtime code.

## Benchmark results: up to 90% faster in production

There is no one single definitive benchmark that represents speculative decoding performance. Speculative decoding benchmarks are especially sensitive to prompt contents, as a draft model may perform much better for one prompt than another.

Before using speculative decoding in production, it’s essential to benchmark your model server using data that closely matches production inputs and outputs, not generic benchmarks. However, we’ll use popular code generation benchmarks below for illustrative purposes.

Benchmark performance also depends on model server configuration, so we’ve included complete configurations ahead of each benchmark result.

### Qwen 2.5 Coder 14B Instruct

For our first test, we used Qwen 2.5 Coder 14B Instruct as the target model, with the half-billion parameter model from the same family (Qwen 2.5 Coder 0.5B Instruct) as the draft model.

The draft and target models share a single GPU, and for each pass through the draft model, we ask for 4 draft tokens. Here is the complete server configuration:

```
1model_metadata:
2  tags:
3  - openai-compatible
4model_name: Qwen2.5-Coder-14B-Instruct (SpecDec)
5python_version: py310
6resources:
7  accelerator: H100
8  cpu: '1'
9  memory: 24Gi
10  use_gpu: true
11trt_llm:
12  build:
13    base_model: qwen
14    checkpoint_repository:
15      repo: Qwen/Qwen2.5-Coder-14B-Instruct
16      source: HF
17    max_seq_len: 10000
18    plugin_configuration:
19      paged_kv_cache: true
20      use_paged_context_fmha: true
21    speculator:
22      speculative_decoding_mode: DRAFT_TOKENS_EXTERNAL
23      checkpoint_repository:
24          repo: Qwen/Qwen2.5-Coder-0.5B-Instruct
25          source: HF
26      num_draft_tokens: 4
27  runtime:
28    enable_chunked_context: true
29    kv_cache_free_gpu_mem_fraction: 0.62
30    request_default_max_tokens: 1000
31    total_token_limit: 500000
```
#### P50 total request time

We see the impact of speculative decoding on latency: p50 latency is reduced substantially after speculative decoding is introduced.

![Qwen 2.5 14B Spec Dec Performance](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1734627269-output-7.png%3Fauto%3Dformat%26w%3D1200&w=3840&q=75)

#### Time to first token and time per output token

Total request time has two parts: the time it takes to generate the first token, and the time it takes to generate all subsequent tokens. While speculative decoding makes the overall response generation faster, it still does make the time to first token slightly worse despite our optimization efforts.

This table shows a breakdown of the latencies for the json-mode-eval benchmark:

### Llama 3.1 70B Instruct

We also tested Llama 3.1 70B Instruct as the target model, with the 8B version as the draft model.

The draft and target models share a 4xH100 GPU server (we quantize the 70B target model to FP8 to ensure enough headroom for KV cache), and for each pass through the draft model, we ask for 4 draft tokens. Here is the complete server configuration:

```
1model_metadata:
2  tags:
3  - openai-compatible
4model_name: llama-spec-dec-no-evict
5python_version: py310
6resources:
7  accelerator: H100:4
8  cpu: '1'
9  memory: 24Gi
10  use_gpu: true
11secrets:
12  hf_access_token: None
13trt_llm:
14    build:
15      base_model: llama
16      checkpoint_repository:
17        repo: meta-llama/Llama-3.1-70B-Instruct
18        source: HF
19      max_batch_size: 256
20      max_num_tokens: 8192
21      max_seq_len: 10000
22      plugin_configuration:
23        paged_kv_cache: true
24        use_fp8_context_fmha: true
25        use_paged_context_fmha: true
26      quantization_type: fp8_kv
27      speculator:
28        checkpoint_repository:
29          repo: meta-llama/Llama-3.1-8B-Instruct
30          source: HF
31        speculative_decoding_mode: DRAFT_TOKENS_EXTERNAL
32        num_draft_tokens: 4
33      tensor_parallel_count: 4
34    runtime:
35      batch_scheduler_policy: guaranteed_no_evict
36      enable_chunked_context: true
37      kv_cache_free_gpu_mem_fraction: 0.65
38      request_default_max_tokens: 1000
39      total_token_limit: 500000
```
#### P50 total request time

While two benchmarks follow the expected pattern, speculative decoding actually resulted in higher p50 latencies for one test. This is a risk when using speculative decoding. To debug, we’d examine the draft tokens and target model output to figure out why the draft model wasn’t making acceptable tokens.

![Llama 3 70B Spec Dec Performance](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1734627299-output-8.png%3Fauto%3Dformat%26w%3D1200&w=3840&q=75)

#### Time to first token and time per output token

Again, we see a similar breakdown in latencies, this time with an equivalent TTFT but a faster overall speed for spec dec in the json-mode-eval benchmark:

## Deploy production services with speculative decoding

Production-ready speculative decoding is an ongoing part of our model performance efforts. We’re constantly experimenting with different models, different methods (including Medusa), and different model server and inference engine settings to improve the latency and stability of speculative decoding.

Present considerations for improving our speculative decoding setup include:

- Limiting the context window of the target model to - [reduce the cost of speculation for long-context use cases](https://arxiv.org/abs/2408.11049).
- Automatically adjusting the number of draft tokens generated per pass based on factors including batch size and observed acceptance rate to - [ensure that speculative decoding always has a net positive impact on performance](https://arxiv.org/abs/2406.14066).
- Using prompt lookahead decoding for use cases like code completion where provided text can be used to generate draft tokens without even running the draft model.

Additionally, we plan to continue our investments in the performance and stability of speculative decoding on TensorRT-LLM while contributing any bugfixes back to the maintainers.

If you’re running any open-source, fine-tuned, or custom LLM and need better latency without sacrificing output quality, especially for code generation tasks, [reach out to us](https://www.baseten.co/talk-to-us/?model=LLMs%20optimized%20with%20speculative%20decoding) to see how we can help you cut latency in production.
