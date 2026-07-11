---
title: Boost your throughput with dynamic batching
topic: inference
subtopic: optimization
secondary_topics:
- models/multimodal
summary: Explains dynamic batching for Whisper transcription workloads and how batching
  improves throughput without changing model behavior.
source: modal
url: https://modal.com/blog/batching-whisper
author: null
published: '2024-09-16'
fetched: '2026-07-11T04:29:55Z'
classifier: codex
taxonomy_rev: 1
words: 873
content_sha256: cc4662851415df3dd0c917438a36f6c4ef12db819fb135db4188d55c457222d4
triage: keep
skip_reason: null
---

# Boost your throughput with dynamic batching

[Back](https://modal.com/blog)

# Boost your throughput with dynamic batching

[Cathy Zhou](https://twitter.com/cathyzbn)

[Charles Frye](https://twitter.com/charles_irl)

Dynamic batching is a powerful technique that can significantly improve the efficiency of workloads from machine learning model inference to database queries. By grouping requests and processing them together, dynamic batching increases throughput, reduces duplication of work, and leads to lower costs.

We added [native dynamic batching support](https://modal.com/docs/guide/dynamic-batching) to Modal to make it easier for our users to get these benefits.

In this post, we’ll show you how we added dynamic batching to a Whisper transcription example and achieved a 2.8x increase in throughput — with just a single line of code.

You can find our code [here](https://github.com/modal-labs/modal-examples/blob/main/06_gpu_and_ml/openai_whisper/batched_whisper.py).

## Why batching?

Batching is a fundamental technique in computer systems,
appearing everywhere from [write coalescing in SSDs](https://www.enterprisestorageforum.com/hardware/fixing-ssd-performance-degradation-part-1/) to [Nagle’s algorithm for TCP](https://brooker.co.za/blog/2024/05/09/nagle.html).

The core idea is simple: handling one request often requires more than half the resources for handling two requests together, so we can make more effective use of our resources by grouping requests.

Batching can be particularly effective in the context of data-intensive Python applications. For example, machine learning models often run on GPUs, which are optimized for parallel processing. Handling even a single request on a GPU requires loading the entire model weights into the GPU’s compute units (in the equivalent of CPUs’ caches and registers) so they can be combined with the request’s inputs to produce model outputs.

For OpenAI’s audio transcription model [Whisper large v3](https://huggingface.co/openai/whisper-large-v3),
that means over six gigabytes of data must be loaded from the GPU’s memory into the compute units for each request,
even if there’s only a few KB of audio in and a few bytes of text out.

Combining multiple requests together before passing them through the model means we only have to move the model weights once, leading to significant improvements in throughput. This frequently doesn’t even increase the latency for individual requests, since GPU inference is typically bottlenecked on memory bandwidth rather than compute, and CUDA programs overlap computation with data movement.

If you’re interested in a deeper dive on this subject, check out [Horace He’s blog post](https://horace.io/brrr_intro.html).

## Why dynamic batching?

Traditional batching schemes wait for a fixed number of requests to arrive and “fill the batch” before any are processed. This isn’t such a big deal during jobs with controlled request rates, like training a model on a fixed dataset. But it can incur unbounded delays when requests arrive sporadically, as is typical in web services.

Dynamic batching avoids this unbounded delay by processing batches of requests either when the batch is full or after a fixed time limit, whichever comes first. The size and time limit can be configured to balance throughput and latency for your specific workload.

Some specialized inference frameworks, like [vLLM](https://blog.vllm.ai/2023/06/20/vllm.html) for language models,
offer implementations of dynamic batching and even [continuous batching](https://www.anyscale.com/blog/continuous-batching-llm-inference),
where responses are returned as soon as they finish, without waiting for other members of the batch.
But these frameworks are tied to specific models and use cases.

Modal’s [dynamic batching feature](https://modal.com/docs/guide/dynamic-batching), on the other hand,
is simpler but more general-purpose. It can be combined with any workload that returns single responses to single requests.

## Tripling throughput and cutting costs by two thirds with one line of code

We tested inference with dynamic batching on OpenAI’s [Whisper large v3 model](https://huggingface.co/openai/whisper-large-v3) on an A10G with increasing batch sizes (until the instance ran out of memory).
Here’s a graph of the throughput compared to the batch size:

![Graph of Whisper inference throughput for the A10G GPU versus batch size](https://modal-cdn.com/cdnbot/batching-whisper-batched-throughput-graph.png)



You can enable dynamic batching for your model with one simple change in your inference function.

Here’s how we enabled dynamic batching for Whisper:

- **Add**The decorator takes in- `@modal.batched()`with batch configuration parameters.- `max_batch_size`, which limits the number of inputs combined into a single batch, and- `wait_ms`, which limits the amount of time the function waits for more inputs after the first input is received. In this example, we selected- `max_batch_size`to be the largest power of 2 that doesn’t cause the A10G to run out of memory. See the- [guide](https://modal.com/docs/guide/dynamic-batching)for more tips on optimizing configuration parameters for dynamic batching.
- **Change the inference function to take in a list of samples and return a list of results.**In this example,- `audio_samples`and- `transcriptions`are lists with equal lengths. Modal will automatically assemble the batched input list and distribute the output list for you. Most Hugging Face pipelines already handle lists of inputs, so we didn’t need to change anything here.

And your inference batching is now ready to go!

```
@app.cls(gpu="a10g")  # in Modal, we decorate classes/functions with resource requirements
class Model:
    @modal.enter()  # load the model once when we start up, before processing any batches
    def load_model(self):
        # set up model
        self.pipeline = ...
    @modal.batched(max_batch_size=64, wait_ms=1000)  # add this decorator
    def transcribe(self, audio_samples: list) -> list:  # take in and return lists
        return self.pipeline(audio_samples, batch_size=len(audio_samples))
```
By selecting a `max_batch_size` of 64, dynamic batching boosted our inference throughput by almost 3x
— from ~1.2 to ~3.3 requests per second per container.
This resulted in 65% savings on the cost to run inference on Modal!

Ready to try out dynamic batching for your application?
Explore the [full code example here](https://github.com/modal-labs/modal-examples/blob/main/06_gpu_and_ml/openai_whisper/batched_whisper.py) and start optimizing your inference process!
