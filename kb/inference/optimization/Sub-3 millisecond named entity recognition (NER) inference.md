---
title: Sub-3 millisecond named entity recognition (NER) inference
topic: inference
subtopic: optimization
secondary_topics:
- models/benchmarks
summary: Shows how to achieve sub-3-millisecond NER inference with optimized serving.
source: baseten
url: https://www.baseten.co/blog/sub-3-millisecond-named-entity-recognition-ner-inference/
author: Michael Feil; David Oy
published: '2026-04-06'
fetched: '2026-07-11T04:05:45Z'
classifier: codex
taxonomy_rev: 1
words: 1491
content_sha256: eaeb8a49754af9c092024924dbfce6c0983ec1b412362ab3990240ebbe992d82
triage: keep
skip_reason: null
---

# Sub-3 millisecond named entity recognition (NER) inference

![Sub-3 millisecond named entity recognition (NER) inference](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1774873256-baseten-blog-2026-thumbnails-1.png%3Fauto%3Dformat%26fit%3Dcrop%26h%3D630%26w%3D1200&w=3840&q=100)

[Baseten Embeddings Inference (BEI)](https://www.baseten.co/blog/introducing-baseten-embeddings-inference-bei/) started with a simple goal: to make encoder inference so fast that it vanishes into the background of your application.

In service of this goal, we have expanded BEI beyond embeddings to include named entity recognition (NER): a token-classification workload that shows up everywhere in production, from document ingestion and support analytics to compliance pipelines, routing, and retrieval augmentation.

With BEI’s serving path and runtime optimizations, we can run common BERT-class NER models with sub-3 millisecond client-side inference and 1 millisecond server-side inference under realistic production conditions.

![Sub-3 millisecond named entity recognition inference with Baseten](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1775492112-linkedin-1.png%3Fauto%3Dformat%26w%3D1200&w=3840&q=75) Using BEI, named entity recognition (NER) inference runs at 1 ms P50 and 3 ms P99 latency on the server side, and 3 ms P50 and 4 ms P99 latency end-to-end (including network latency, which can be variable). In comparison, an optimized PyTorch model implementation (transformers + the open-source Baseten Performance Client, which improves throughput up to 12x) achieves 16 ms P50 and 23 ms P99 latency (without the Performance Client we see up to 50 ms P99 latency, but use the more conservative estimate here). The BEI implementation is ~7.7x faster.

Using BEI, named entity recognition (NER) inference runs at 1 ms P50 and 3 ms P99 latency on the server side, and 3 ms P50 and 4 ms P99 latency end-to-end (including network latency, which can be variable). In comparison, an optimized PyTorch model implementation (transformers + the open-source Baseten Performance Client, which improves throughput up to 12x) achieves 16 ms P50 and 23 ms P99 latency (without the Performance Client we see up to 50 ms P99 latency, but use the more conservative estimate here). The BEI implementation is ~7.7x faster.This post covers:

- What NER models do (and why NER inference has different requirements than embeddings)
- What we changed in BEI to make NER inference so fast
- How to deploy an NER model with BEI
- How to inspect token-level predictions

## Optimizing NER inference: NER vs. embeddings

Named entity recognition (NER) models turn free-form text into structured data by identifying character spans that represent entities such as people, organizations, locations, and dates.

Most modern NER models are implemented as token classification:

- Tokenize the input text into word pieces (e.g., WordPiece/BPE).
- Run an encoder model (often from the BERT family).
- Produce a label distribution for every token (e.g., B-PER, I-ORG, O, etc.).
- Optionally post-process token labels into entity spans aligned with the original string.

Unlike embedding models (which output one vector per input text), NER returns a prediction per token. That makes the inference compute relatively small compared to the overhead around inference (tokenization, HTTP parsing, JSON serialization, connection behavior, proxying, and framework overhead).

Once the model is fast enough, the real work becomes removing everything else from the hot path.

## How we get sub-3 millisecond NER inference

To achieve sub-3 ms NER inference, we focused on removing latency at every layer of the serving stack: the web framework and tokenizer, the proxy, connection handling, and the deployment topology.

### Low-overhead serving with Rust

BEI uses a Rust-based web server and tokenizer stack designed for high-throughput encoder workloads. NER benefits even more than embeddings here, because token classification requests can be small enough that a Python web framework’s overhead dominates the end-to-end latency.

By keeping tokenization and request handling in Rust, we minimize per-request overhead and keep CPU utilization predictable under concurrency.

### Nginx is configured to stay out of the way

At sub-millisecond inference, “just the proxy” can become the bottleneck. We configure Nginx to reduce overhead on the serving path, minimizing unnecessary buffering and avoiding disk-backed behavior that can introduce latency variance.

The goal is simple: keep the request path memory-backed and lightweight, so the model runtime is what you’re measuring — not incidental IO.

### HTTP/2 connection pooling in the Baseten Performance Client

If you benchmark without connection reuse, you’re mostly measuring TLS handshakes, socket setup, and request lifecycle overhead. That’s not what production looks like, and it’s especially misleading when the model itself is extremely fast.

Our [Performance Client](https://www.baseten.co/blog/your-client-code-matters-10x-higher-embedding-throughput-with-python-and-rust/) uses HTTP/2 connection pooling, so repeated requests reuse connections, and your latency reflects inference + minimal request handling rather than repeated setup costs.

### Geographical co-location

If you’re calling your NER pipeline as part of a larger processing pipeline, e.g., for anonymization or query understanding, running it in the same physical datacenter can help reduce latency.

Baseten has products like [Chains](https://docs.baseten.co/development/chain/overview) that allow co-location of Baseten deployments.

### Calling `/predict_tokens` vs `/hello_world` in FastAPI

A helpful mental model:

- A minimal FastAPI route like - `/hello_world`is effectively a benchmark of framework overhead.
- A Python-served NER endpoint often adds tokenization, model runtime, and serialization on top of that.
- BEI’s - `/predict_tokens`is designed to keep overhead low enough that token classification can run at the speed the hardware allows.

When you’re chasing sub-millisecond inference, these differences matter: at that point, even “small” overhead (routing layers, connection setup, JSON parsing/encoding) can dominate end-to-end latency.

## How to deploy an NER model with BEI

Below is an example configuration for deploying a BERT-family NER model checkpoint via BEI on an L4 GPU. It sets BEI’s default route to `/predict_tokens`, which returns token-level predictions.

```
1model_metadata:
2  example_model_input:
3    inputs:
4      - - Apple is looking at buying U.K. startup for $1 billion
5      - - John works at Google in Mountain View, California
6    raw_scores: true
7    truncate: true
8    truncation_direction: Right
9model_name: BEI-Bert-ner-bert-base-ner-uncased-truss-example
10python_version: py39
11resources:
12  accelerator: L4
13  cpu: "1"
14  memory: 10Gi
15  use_gpu: true
16trt_llm:
17  build:
18    base_model: encoder_bert
19    checkpoint_repository:
20      repo: baseten-admin/bert-base-ner-uncased
21      revision: main
22      source: HF
23    max_num_tokens: 16384
24  runtime:
25    webserver_default_route: /predict_tokens
```
A few notes:

- `base_model: encoder_bert`selects the encoder runtime path suitable for token classification.
- `webserver_default_route: /predict_tokens`makes the model behave like a dedicated token prediction endpoint.
- `raw_scores: true`returns per-label probabilities per token (useful if you want to apply confidence thresholds or custom decoding).

## Getting NER predictions from BEI

BEI returns token-level predictions from `/predict_tokens`. The response includes one entry per token and (when enabled) a per-label probability distribution.

Here’s a minimal BEI-only script that:

- Sends a list of texts
- Prints the top 1 label + score per token
- Optionally prints the top scores per token when - `raw_scores = true`

```
1"""
2BEI-only NER predictions
3- Calls /predict_tokens with a list of texts
4- Prints per-token top-1 label + score
5"""
6
7import json
8from baseten_performance_client import PerformanceClient
9
10client = PerformanceClient(
11    base_url="https://model-<model-id>.api.baseten.co/environments/production/sync"
12)
13
14def bei_predict(texts: list[str], raw_scores: bool):
15    resp = client.batch_post(
16        "/predict_tokens",
17        payloads=[{"inputs": [[text] for text in texts], "raw_scores": raw_scores}],
18        aggregation_strategy="max"
19    )
20    return resp.data[0], resp.total_time
21
22
23def print_predictions(bei_data, raw_scores: bool):
24    if not (isinstance(bei_data, list) and len(bei_data) > 0):
25        raise ValueError(f"Unexpected BEI response format: {type(bei_data)}: {bei_data}")
26
27    per_text = bei_data[0]
28    if not isinstance(per_text, list):
29        raise ValueError(f"Unexpected per_text type: {type(per_text)}: {per_text}")
30
31    for text_idx, token_preds in enumerate(per_text, start=1):
32        print(f"\n{'=' * 80}")
33        print(f"Input {text_idx}")
34        print(f"{'=' * 80}")
35
36        if not isinstance(token_preds, list):
37            raise ValueError(f"Unexpected token_preds type: {type(token_preds)}: {token_preds}")
38
39        print(f"\n{'Token':<20} {'Label':<20} {'Score':<10}")
40        print("-" * 55)
41
42        for token_pred in token_preds:
43            tok = token_pred.get("token")
44
45            if "results" in token_pred and isinstance(token_pred["results"], dict):
46                best_label, best_score = max(
47                    token_pred["results"].items(),
48                    key=lambda x: x[1]
49                )
50                print(f"{tok:<20} {best_label:<20} {float(best_score):<10.4f}")
51
52                if raw_scores:
53                    topk = sorted(
54                        token_pred["results"].items(),
55                        key=lambda x: x[1],
56                        reverse=True
57                    )[:5]
58                    topk_str = ", ".join(
59                        [f"{lbl}:{float(scr):.4f}" for lbl, scr in topk]
60                    )
61                    print(f"{'':<20} {'top5':<20} {topk_str}")
62
63            elif "label" in token_pred and "score" in token_pred:
64                print(
65                    f"{tok:<20} "
66                    f"{str(token_pred['label']):<20} "
67                    f"{float(token_pred['score']):<10.4f}"
68                )
69
70            else:
71                raise ValueError(
72                    f"Unexpected token prediction format:\n"
73                    f"{json.dumps(token_pred, indent=2)}"
74                )
75
76
77if __name__ == "__main__":
78    test_texts = [
79        "Apple is looking at buying U.K. startup for $1 billion",
80        "John works at Google in Mountain View, California",
81        "The Eiffel Tower is in Paris, France",
82    ]
83
84    bei_data, _ = bei_predict(test_texts, raw_scores=False)
85    print_predictions(bei_data, raw_scores=False)
```
## Drop BEI into your existing NER pipeline

If you’re already using NER in production, switching the inference layer is often the easiest way to make the pipeline faster (and cheaper) without changing your models or your application logic. BEI NER is designed for exactly that: a low-overhead serving path for encoder workloads where “everything else” can dominate latency.

If you want to deploy a specific NER checkpoint (or a token classifier for PII detection, moderation, or routing), you can use the same BEI workflow — point BEI at your checkpoint, expose `/predict_tokens`, and scale it like any other Baseten deployment.  If you have any questions, [reach out](https://www.baseten.co/talk-to-us/) or check out [our docs](https://docs.baseten.co/engines/bei/bei-bert#named-entity-recognition-ner-models); we’re happy to help!
