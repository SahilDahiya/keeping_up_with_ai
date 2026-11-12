---
title: Open-sourcing Baseten’s suffix automaton MTP accelerator
kind: blog
topic: null
subtopic: null
secondary_topics: []
summary: null
triage: null
skip_reason: null
source: baseten
url: https://www.baseten.co/blog/boosting-mtp-acceptance-rates-in-baseten-speculation-engine
author: Mahmoud Hassan
published: '2026-01-22'
fetched: '2026-11-12T06:10:52Z'
classifier: null
taxonomy_rev: 2
words: 1058
content_sha256: d14c09c2af55172b7ec2c3e62e6405f273b81e275d423a61e20774909d75bacf
---

# Open-sourcing Baseten’s suffix automaton MTP accelerator

Model performance
# Open-sourcing Baseten’s suffix automaton MTP accelerator

We've open-sourced a library from the Baseten Speculation Engine to boost MTP acceptance rates by up to 40% using Suffix Automaton Decoding.


- Authors
- Date
- January 22, 2026

Link to open-source library [<u>here</u>](https://github.com/basetenlabs/sa_spec/).

Two common approaches are widely adopted for speculative decoding:

- **N-gram speculation**, which predicts the next token based on fixed-length patterns from recent context.
- **Draft model speculation,** like EAGLE or multi-token prediction (MTP), which uses a smaller, faster neural network to predict several tokens ahead.

At Baseten, we developed a hybrid method to effectively batch the token verification phase, significantly reducing latency for individual requests. Our method combines a suffix automaton—an advanced form of n-gram lookup—with an MTP/EAGLE draft model. This approach is particularly impactful for applications like code generation, where long, repetitive patterns are common.

For the open source version, we’ve integrated our technique into NVIDIA TensorRT-LLM so that anyone can use it. We achieved these speedups with zero added overhead, making it suitable for production deployments. On production agentic coding workloads, we see **up to 40% higher throughput** at equal latency and **up to 40% lower latency** at equal throughput, compared to MTP alone.

This approach improves upon n-gram lookup decoding by using a [suffix automaton](https://en.wikipedia.org/wiki/Suffix_automaton) (SA) for prediction lookups.

Unlike the fixed-size pattern matching available in vLLM and TensorRT-LLM’s n-gram speculative decoding, SA decoding identifies arbitrarily long patterns and selects the longest possible match. Additionally, the suffix automaton is updated in real time during generation, resulting in higher acceptance rates on long sequences.

SA Decoding shines at code generation, where the accept length is 10+ with long context, but performs poorly on reasoning and other writing tasks, with accept rates near 0. Meanwhile, MTP produces consistent speed-ups across all domains, though the accept rate is usually only 2-4 tokens per iteration.

Baseten Speculation Engine, which is a core component of the [Baseten Inference Stack](https://www.baseten.co/resources/guide/the-baseten-inference-stack/#why-building-performant-inference-at-scale-is-challenging), combines both approaches: if the SA finds a match longer than a threshold then the SA match is used, otherwise MTP is used.

This achieves a significant speedup on MTP models like [DeepSeek-V3.1-NVFP4](https://huggingface.co/nvidia/DeepSeek-V3.1-NVFP4). The level of speedup depends heavily on the task, with a more pronounced increase on agentic coding and math tasks. We commonly see up to 40% improvements on coding applications for production workloads.

To integrate with the TRT-LLM runtime, requests are processed as follows:

1. The suffix automaton for the initial prompt is constructed on the host, overlapping with the KV-cache prefill on the device.
2. Before the first generation step, the automaton state is transferred to the device.
3. During generation, the suffix automaton is **updated directly on the device**, without introducing additional synchronization points.

The suffix automaton itself is a highly efficient data structure, with an amortized runtime complexity of O(1) per update. As a result, by carefully scheduling its construction and updates to avoid new synchronization points, near-zero overhead is achieved.

To support this design, we built a Python API that exposes three core operations (check out the full API in [the repository here](https://github.com/basetenlabs/sa_spec/blob/dev/src/bind.cc)):

- `add_request(request_id: int, prompt: list[int])`: builds a suffix automaton state on the host.
- `prepare(request_ids: list[int])`: prepares a GPU batch, copying newly created suffix automaton states to the device.
- `extend(draft_tokens_out: tensor, accepted_tokens_in: tensor)`: a CUDA-kernel, CUDA-graph-compatible operation that updates a batch of suffix automaton states on the GPU and returns SA draft tokens and match lengths (i.e., confidence scores). A batch of *N* requests is updated in parallel by launching a grid with one block per batch slot and 1 thread each.

`extend` is called before draft sampling to compute match lengths from the suffix automaton. These **match lengths are compared against a threshold to decide how many draft tokens come from suffix-automaton continuations versus multi-token prediction sampling**.

To achieve high performance while avoiding platform-specific core logic, suffix automaton states are represented as [plain old data](https://en.wikipedia.org/wiki/Passive_data_structure) (POD) structs, and the core algorithm is implemented in a [header-only implementation](https://github.com/basetenlabs/sa_spec/blob/dev/src/sa_spec/suffix_automaton.hpp) that compiles for both C++ and CUDA. This allows the suffix automaton logic to be written once and run on both the CPU and GPU. Additionally, the use of POD structs enables efficient, low-overhead data transfer between host and device.

This implementation demonstrates the high level of interoperability between C++ and CUDA. For example, we implement a POD [graph structure](https://github.com/basetenlabs/sa_spec/blob/dev/src/sa_spec/util/flat_graph.hpp) along with a dynamic hash map for storing suffix automaton states, both of which are fully C++ and CUDA-compatible. By embracing POD structs, all we need for CUDA support is a [C++ smart pointer type](https://github.com/basetenlabs/sa_spec/blob/dev/src/sa_spec/util/memory.hpp) with CUDA specializations for `malloc` and `memcpy`. Finally, we achieve torch stream capture (CUDA graph) compatibility by specializing the smart pointer’s `memcpy` and `extend()` invocations to run on the active torch stream.

As a result, the profile output for the decode phase shows minimal idle GPU time.

The absence of latency overhead was verified by setting the SA threshold to infinity, effectively disabling SA predictions while still executing the computation, and confirming that end-to-end latency matches that of baseline MTP. This demonstrates that this implementation introduces zero overhead.

By augmenting draft model speculation with suffix automaton-based lookups, we achieved up to 40% efficiency gains on existing workloads that use speculative decoding. These improvements are orthogonal to other inference optimizations and, in many cases, provide additional speedups on top of existing MTP/EAGLE deployments without requiring any changes to configuration parameters such as draft length.

Looking ahead, we find several directions for future work particularly promising:

- **Continuous draft model training alongside inference**, enabling the draft models to adapt to evolving workloads and further improve acceptance rates.
- **Dynamic-length speculation**, where the draft length is adjusted based on speculation confidence on a per-request, per-micro-batch basis.

For more information on incorporating our hybrid MTP/SA decoding approach into your workloads, [get in touch with our engineers](https://www.baseten.co/talk-to-us/).

Several related efforts were developed independently and explore overlapping ideas. While the implementations and goals differ, they share core concepts with the approach described here and are therefore worth highlighting:

You can use lookahead decoding with any [LLM supported](https://docs.baseten.co/engines/engine-builder-llm/overview#use-cases) in our Engine Builder. Check out our docs for examples and best practices on deploying models using SA with lookahead decoding.[](https://docs.baseten.co/engines/engine-builder-llm/lookahead-decoding#when-to-use-lookahead-decoding)

A comprehensive academic treatment of suffix automaton-based speculative decoding, providing useful background and formal analysis.

An exploration of suffix-tree-based speculation in vLLM, with a particular focus on repetitive, agent-driven workloads.
