---
title: Making Kimi K3 tokenization 18x faster for million-token agentic workloads
kind: blog
topic: null
subtopic: null
secondary_topics: []
summary: null
triage: null
skip_reason: null
source: baseten
url: https://www.baseten.co/blog/making-kimi-k3-tokenization-18x-faster-for-million-token-agentic-workloads
author: Michael Feil
published: '2026-07-27'
fetched: '2026-11-12T06:08:14Z'
classifier: null
taxonomy_rev: 2
words: 1376
content_sha256: ec931359225d537d2a3415c4af2ffabe063630102d593352f90d900a8df18d26
---

# Making Kimi K3 tokenization 18x faster for million-token agentic workloads

Model performance
# Making Kimi K3 tokenization 18x faster for million-token agentic workloads

We built the Baseten Tokenizer (Basetenkenizer) to optimize tokenization for long input sequences, starting with Kimi K3.


- Authors
- Date
- July 27, 2026

For years, inference engineers have been able to disregard tokenization time as negligible. Short input sequences take a couple of milliseconds to tokenize, a tiny fraction of the time required for prefill and decode.

This has changed. Open frontier models like [Kimi K3](https://www.baseten.co/library/kimi-k3/) support input sequences of up to one million tokens. These long input sequences are increasingly common in agentic workloads, where an agent loop repeatedly appends tool results, observations, retrieved documents, intermediate state, reasoning traces, and updated instructions back into the next request.

We built the Baseten Tokenizer (Basetenkenizer) to optimize tokenization for long input sequences, starting with Kimi K3. Within the Baseten Inference Stack, we migrated from a custom Python tiktoken implementation to the Rust-based Basetenkenizer, for the day zero release. On the long input sequences where tokenization time matters most, the complete serving path is up to 18x faster than tiktoken while preserving exact token IDs.

This post describes the implementation and the benchmarking process for Baseten Tokenizer.

Bastenkenzier relies on work from -- and -- under the hood. We're proud to contribute to the open-source community and thankful for their contributions, which made this work possible.

Building the Baseten tokenzier is fastokens and ...

Most LLMs use a byte-pair encoding (BPE) tokenizer wrapped in a standard chat template. This tokenizer design dates back to the earliest Transformer models like GPT-2 and RoBERTa.

Kimi K3 ships with a `tiktoken.model` BPE vocabulary along with a regex pre-tokenization for structural tokens like `<|open|>`, `<|sep|>`, `<|close|>`, and `<|end_of_msg|>`. A Python chat renderer emits typed encode\_segments, and long-text chunking behavior is inherited from the custom `tiktoken` path.

In structural parts of the rendered prompt, a string like \<|open|> should encode as a control token. In user or tool text, the exact same string must be treated as ordinary text.

For example, if a user writes:

`please explain the literal token <|open|>`
The characters `<|open|>` must not become a structural marker. It has to be encoded as normal user text. Losing this distinction changes the prompt.

The old tokenizer handled this by rendering chat into segments:

python

```
EncodeSegment(text="<|open|>", allow_special=True)
EncodeSegment(text="message role=\"user\"", allow_special=False)
EncodeSegment(text="<|sep|>", allow_special=True)
EncodeSegment(text="literal user text <|open|>", allow_special=False)
```
To maintain exact token IDs, we needed to implement the same behavior in the Baseten Tokenizer. To make it easy to compare token IDs with other libraries, we are also releasing a Kimi K3 `tokenizer.json` on [Hugging Face](https://huggingface.co/baseten/kimi-k3-tokenizer/blob/main/README.md) today.

The old Kimi path looped over those segments in Python. It also reproduced tiktoken's long-input safety rules — splitting text into at most 400k characters, then splitting runs of whitespace or non-whitespace at 25k characters — and finally assembled Python lists of token IDs. Every segment and every chunk paid for a trip across the Python/native boundary.

Baseten Tokenizer accepts the ordered \`(text, allow\_special)\` segments in one native call, returning the tokens in an array interface:

```
encoding = tokenizer.encode_segments(
    [(segment.text, segment.allow_special) for segment in segments],
    add_special_tokens=False,
    tiktoken_safe=True,
)
input_ids = encoding.into_numpy(ids=True)["ids"]
```
The chat renderer stays in Python, outside the measured encode region. Special-token selection, safe chunking, regex pre-tokenization, BPE, ordered assembly, and the NumPy handoff all happen behind one native boundary. Serving code never materializes a million Python integers.

Our implementation combines several optimizations:

- **Specialized pre-tokenization scanners:** Recognizes Kimi's split regex pattern ahead of time and dispatches to a handwritten function instead of a general regex engine. For those not interested in writing this, the Kimi model family's regex can be matched and reformulated for the PCRE2 JIT library.
- **A stack-resident BPE merge tier:** Short pre-tokens of up to 32 bytes run in a stack-allocated linked list with a linear minimum-rank scan and dense first-round byte-pair table, avoiding heap and priority queue overhead.
- **Multi-core semantics:** Identical pre-tokens are routed to the same CPU core on cold, long inputs, ensuring repeated words are merged once and served from cache before output order is restored. `encode_segments` has a limit of 400,000 characters, a legacy limitation of tiktoken. Basetenkenizer uses this as an opportunity to schedule each 400,000-character chunk on a separate core, making long-context ISL faster than Gigatoken.
- **Native typed segments and safe chunking:** Per-span special-token policies and compatibility rules run in Rust, preventing the creation of Python work lists.
- **Zero-copy NumPy ownership transfer:** The token array is handed to Python without intermediate lists of integers, and encodings are only materialized when accessed.
- **Smart-pointer PyO3 bindings:** Uses `abi3-py310` bindings, with strings borrowed as Cow values in Rust to improve efficiency.

These improvements compound on long context and multiple turns.

We evaluated this performance gain against the workload profile it is designed to help the most: a long input sequence with a high prefix cache hit rate.

The primary workload is a rendered Kimi K3 chat prompt containing 54 typed segments. Every measured round uses a new deterministic corpus of the same character length, mixing prose, code, JSON, Unicode scripts, punctuation, numbers, unique request IDs and hashes, and literal K3 control strings inside user text. No measured prompt is encoded twice, so BPE caches start cold and only benefit from naturally recurring vocabulary — as they would in real traffic. Basetenkenizer parallelizes internally across the pinned CPU set — this is a comparison of the fastest complete path each library offers for this workload. Inference Servers typically provide a large amount of available CPU cores.

To separate the serving-path win from raw BPE speed, we also measured plain already-loaded Python strings on the Kimi K2.7 base tokenizer, each library using its fastest applicable API:

| Tokens encode(string) | Basetenkenizer | tiktoken 0.13.0 | PyPI fastokens 0.2.0 | PyPI gigatoken 0.10.0 | 
|---|---|---|---|---|
| 10k | 0.456 ms | 2.102 ms | 1.594 ms | 0.118 ms | 
| 200k | 2.452 ms | 40.355 ms | 16.409 ms | 2.471 ms | 
| 1M | 9.233 ms | 210.293 ms | 82.903 ms | 13.027 ms | 

For a full benchmark, tiktoken, fastokens and gigatoken omit the fact that a chat-template needs to be rendered. This codepath is more String allocation heavy, Basetenkenizer is the first library solving this for Kimi K3 though a fused encode call, as well as all other models like GLM5.2 or Kimi K2.7 that use jinja templates.

| \~200k-token conversation apply\_chat\_template() | Basetenkenizer p50 | Python p50 | P50 approximate tokenization time | 
|---|---|---|---|
| 40 string messages | 1.18 ms | 0.50 ms | 2.42 ms | 
| 400 string messages | 2.12 ms | 3.47 ms | 2.36 ms | 
| 400 content-block messages | 2.85 ms | 3.56 ms | 2.36 ms | 
| 2,000 messages | 6.45 ms | 16.51 ms | 2.32 ms | 

Benchmarking is always a tricky subject. Notes on what we did to make the comparison as fair as possible:

1. Neither published competitor exposes typed segment encoding, so their measurements include the Python orchestration required to preserve K3 semantics; gigatoken returns NumPy natively and the benchmark uses that path. We have included Kimi K2.7 benchmarks that dispatch in a single Python call.
2. Gigatoken is fastest at 10k tokens; the crossover appears before 200k, and at 1M Baseten Tokenizer leads it by 1.41x on this input. And on gigatoken's own target workload — offline corpus files read directly in Rust — gigatoken is in a different throughput class entirely (2.68 GiB/s on a 64 MiB direct-file benchmark, versus 118 MiB/s for our Python-string path). The conclusion is specific: for K3 online serving from typed, already-rendered segments, Baseten Tokenizer is the fastest path we measured; for offline dataset tokenization, use gigatoken's \`encode\_files\`. Baseten specialized the caches for serving efficiency, while gigatokens optimizes global throughput.
3. All times are end-to-end encode medians on 52 pinned vCPUs (Intel Xeon Platinum 8480+), including each library's supported conversion to a NumPy `uint32` token array. tiktoken's public encode call is single-threaded;
4. Fastokens underperforms since it cannot exercise its pcrc2 jit backend for the Kimi regex. Aside from a handrolled scanner, the regex can be rewritten, making it around 1.5x faster than the fallback regex scanner.
