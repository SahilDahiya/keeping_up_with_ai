---
title: 'RadixMLP: Intra-batch deduplication for causal transformers'
kind: blog
topic: null
subtopic: null
secondary_topics: []
summary: null
triage: null
skip_reason: null
source: baseten
url: https://www.baseten.co/blog/radixmlp
author: Michael Feil
published: '2026-01-21'
fetched: '2026-11-12T06:16:26Z'
classifier: null
taxonomy_rev: 2
words: 1657
content_sha256: e6d6f4fa88fc39ad0493e49610be2344edf4bb15ed68630a8e83cd59270953a8
---

# RadixMLP: Intra-batch deduplication for causal transformers

Research
# RadixMLP: Intra-batch deduplication for causal transformers

RadixMLP eliminates redundant shared-prefix computations, resulting in 1.4–1.6x speedups in realistic reranking workloads, and up to 5x on synthetic benchmarks.


- Authors
- Date
- January 21, 2026

Batch inference workloads for causal transformer models frequently process sequences that share common prefixes, like system prompts, few-shot examples, or shared queries in reranking tasks. Standard inference engines treat each sequence independently, redundantly recomputing identical MLP activations for every copy of the shared prefix.

To eliminate this redundancy, we developed **RadixMLP**, a technique that exploits the position-wise nature of MLPs, LayerNorms, linear projections, and embeddings. RadixMLP dynamically maps batches to a prefix trie, gathering shared segments into a compressed representation for position-wise computation and scattering results back only at attention boundaries.

In end-to-end serving benchmarks on [MS MARCO v1.1](https://huggingface.co/datasets/microsoft/ms_marco/tree/main) with Qwen3 models (0.6B to 8B parameters), RadixMLP achieves **1.44–1.59x speedups** in realistic reranking workloads, with up to **5x speedups** on synthetic benchmarks with longer shared prefixes.

[RadixMLP is open-source](https://github.com/michaelfeil/radix-mlp) and production-ready: you can use it today on Baseten as part of Baseten Embeddings Inference ([BEI](https://www.baseten.co/blog/introducing-baseten-embeddings-inference-bei/)—sample config [below](https://www.baseten.co/blog/introducing-radixmlp-intra-batch-deduplication-for-causal-transformers/#implementation-deploying-radixmlp-with-truss)) as well as TEI. [Reach out](https://www.baseten.co/talk-to-us/) if you have any questions.

Consider a typical batch inference workload:

- **Embedding models** prepend the same global context to every document.
- **Cross-encoder rerankers** pair each candidate passage with the same query.
- **Classification systems** reuse the same few-shot examples across inputs.

Even with ragged layouts that eliminate padding, duplicate prefix tokens are still materialized as distinct rows in GPU memory. The model therefore recomputes identical activations for each copy. This inefficiency is especially pronounced during prefill, where position-wise components (MLPs, LayerNorms, and linear projections) account for a large fraction of total FLOPs.

This observation motivates **RadixMLP**, a technique designed to eliminate redundant prefix computation by exploiting the position-wise structure of transformer layers.

While causal self-attention is a sequence-mixing operation, the MLP, LayerNorm, linear projections (Q, K, V, O), and embeddings are position-wise. For tokens with identical causal history (i.e., the same prefix path), these per-token computations are identical and can be reused.

This invariance persists across layers: if tokens share a prefix, their position-wise outputs remain the same at each layer. Since attention for prefix tokens depends only on earlier tokens within that same prefix, its outputs are likewise identical. As a result, the shared representation can be preserved layer by layer.

RadixMLP constructs a prefix trie over the batch. Each trie node is identified by its parent and the next `(token_id, position_id)` pair, so nodes are path-specific. No GPU-resident tree structure is required; in practice, we only materialize the resulting index maps (`I_gather`, `I_scatter`) for GPU execution.

For a batch of `B` sequences with shared prefix length `P` and per-sequence suffix length `S`, the compression ratio is:

$r = \frac{N}{N'} = \frac{B(P+S)}{P+BS}$

Where $N$ is the total number of tokens and $N'$ is the number of compacted tokens. In batch workloads with shared prefixes, typically $N' \ll N$.

We define two index mapping tensors:

1. **Gather indices** (`I_gather` $\in \mathbb{N}^{N'}$): For each position in the compact buffer, this specifies which position in the original input to read and selects a representative occurrence for that compact token.
2. **Scatter indices** (`I_scatter` $\in \mathbb{N}^{N}$): For each position in the original layout, this specifies which position in the compact result buffer to read and broadcasts computed results back to all duplicate positions.

The forward pass for the MLP block is modified as follows:

```
X_unique = X[I_gather]
Y_unique = MLP(X_unique)
Y_restored = Y_unique[I_scatter]
```
Since the MLP has complexity $O(N d^2)$, the cost is reduced to $O(N' d^2)$. As the gather/scatter operations are memory-bound $O(N)$ copies, the net speedup approaches the compression ratio $r = N/N'$ as the hidden dimension $d$ grows.

A critical requirement is **causal consistency**. While position-wise layers are independent per token, the attention mechanism requires the full context window.

We place **scatter** and **gather** operations at the boundary between position-wise and sequence-mixing computations:

1. Compute all position-wise operations in compact space: pre-attention LayerNorm, RoPE, Embedding Layer, Q/K norms, and the Q, K, V projections on $N'$ tokens
2. Scatter the resulting Q/K/V tensors back to the full $N$-token ragged layout
3. Run the attention operation (FlashAttention) in full space
4. Gather the attention output back to a compact space for the O projection, post-attention LayerNorm, MLP, and residual additions

Position indices are preserved alongside compact tokens: we gather the position ID tensor using `I_gather`, so each compact token retains its original sequence position for RoPE computation.

Unlike PagedAttention or RadixAttention, which require persistent KV caches with block tables, eviction policies, and distributed coordination, **RadixMLP operates entirely within a single forward pass**.

Beyond that, it's the first cache-like operator for training and deduplicating tokens based on common prefixes. This makes it valuable for batch inference, where maintaining caches for millions of heterogeneous documents is impractical. It enables libraries like [Baseten Embeddings Inference (BEI)](https://docs.baseten.co/examples/bei#embeddings-with-bei) to achieve cache-like speedups, even when inference times are in the 5-millisecond range.

Constructing the trie and generating index maps on GPUs would introduce synchronization overheads. Instead, we utilize a **pipelined scheduler**:

- While the GPU executes batch `t`, the CPU scheduler analyzes the request queue for batch `t+1`
- The scheduler constructs the prefix trie and pre-calculates `I_gather` and `I_scatter`

With an efficient Rust implementation, computing approximately 16,384 tokens takes between 129μs and 750μs on a single-thread Intel Xeon CPU (depending on the prefix ratio). This is around **3 orders of magnitude below the corresponding GPU inference time**, making even synchronous usage feasible.

We evaluated a real serving pipeline by benchmarking TEI on MS MARCO v1.1 validation query–passage pairs. Each request embeds multiple query–document pairs formatted with a reranker-style Qwen3 chat template.

| Model | Base 50 (s) | Radix P50 (s) | Speedup | 
|---|---|---|---|
| Qwen3-0.6B | 0.78 | 0.54 | 1.44x | 
| Qwen3-4B | 3.76 | 2.42 | 1.56x | 
| Qwen3-8B | 5.96 | 3.74 | 1.59x | 

These gains are smaller than synthetic forward-pass speedups because prefix sharing is less extreme in this workload and because end-to-end latency includes non-model overheads. Still, the improvement remains substantial in a practical serving setting.

For controlled evaluation, we used a synthetic fixed batch size of `B=32` sequences, varying the prefix length (shared across all sequences) and suffix length (unique per sequence).

| Configuration | Model | Speedup | 
|---|---|---|
| 2048/256 | Qwen3-0.6B | 2.74x | 
| 2048/256 | Qwen3-4B | 4.14x | 
| 2048/256 | Qwen3-8B | 4.98x | 

We define the compact-token ratio $\gamma = \frac{N'}{N} \in (0, 1]$ and the corresponding compression ratio $r = \frac{N}{N'} = \frac{1}{\gamma}$. The results demonstrate three key trends:

- **Prefix length**: Longer shared prefixes yield lower $\gamma$ (higher $r$) and greater speedups
- **Model size:** Larger models benefit more from RadixMLP, as MLP compute dominates over gather/scatter overhead
- **Suffix ratio:** Shorter suffixes (higher prefix:suffix ratio) maximize compression benefits

We compared TEI with and without RadixMLP against vLLM v0.13.0 on two MS MARCO configurations:

| Model | γ | TEI | TEI RadixMLP | vLLM | 
|---|---|---|---|---|
| Qwen3-0.6B | 0.61 | 0.78 | 0.55 | 0.71 | 

TEI without RadixMLP is the worst-performing inference system. With RadixMLP enabled, TEI outperforms vLLM for the Qwen3-0.6B model. For larger models, vLLM outperforms TEI by a 3-7% margin.

A key difference is memory usage: TEI uses \~17GB vs \~79GB for vLLM with Qwen3-8B, as no additional memory is allocated for a paged KV cache.

Here's how to deploy a Qwen3 model with RadixMLP using Truss:

yaml

```
# Qwen3 with RadixMLP
model_name: BEI-qwen3-radixmlp
python_version: py39
model_metadata:
  example_model_input:
    encoding_format: float
    input:
      type: string
    model: model
resources:
  accelerator: H100
  cpu: 1
  memory: 10Gi
  use_gpu: true
trt_llm:
  build:
    base_model: encoder_bert
    checkpoint_repository:
      repo: michaelfeil/Qwen3-Embedding-0.6B-auto
      revision: main
      source: HF
    max_num_tokens: 32768
  runtime:
    webserver_default_route: /v1/embeddings
```
Deploy with:

bash

`truss push --publish`
RadixMLP excels in scenarios with high prefix redundancy in prefill-heavy workloads. Some such workloads are often:

- **Reranking**: Query-passage pairs with shared system prompts
- **Embeddings**: Global context prepended to every document
- **Post-Training**: Shared system templates in RLHF
- **Classification**: Few-shot examples reused across inputs
- **Instruction following**: Shared instruction templates

RadixMLP operates orthogonally to several existing optimization techniques that are utilized by Baseten today:

- **PagedAttention**: Introduces paged, block-based KV management with block-level sharing. These stateful approaches require complex scheduling and are limited by block granularity, whereas RadixMLP offers block-free, stateless reuse within individual batches.
- **RadixAttention**: Organizes prefixes in a radix tree for cross-request KV reuse. Requires persistent state management, while RadixMLP operates within a single forward pass.
- **FlashInfer Cascade Inference**: Computes attention over shared prefix segments once, then merges partial attention states with per-request suffix attention. RadixMLP complements this by optimizing position-wise components. This is similar to \`HydraGen\` kernels.

These approaches are fully complementary—RadixMLP can stack with KV cache, attention optimizations, or batching/scheduling optimizations.

While the focus of this work is inference, RadixMLP is compatible with training because the compaction operators are differentiable. The compacting gather is an `index_select`, and its backward pass is a scatter-add into the original layout (`index_add`), accumulating gradients when multiple original tokens map to the same compact representative.

We validated both forward and backward correctness on a 2-layer Qwen3-style model across synthetic prefix-sharing patterns. With PyTorch SDPA attention as the reference implementation, enabling RadixMLP produces numerically identical logits up to the specified tolerances (`rtol=1e-4`, `atol=1e-4`) and gradient differences on the order of $10^-5$ or lower.

RadixMLP and Index-Select Kernels, as well as the experimental results, are open-source under the MIT License. You can find the GitHub repository [here](https://github.com/michaelfeil/radix-mlp).

You can read the full paper on arXiv [here](https://arxiv.org/abs/2601.15013).

**For attribution in academic contexts, please cite this work as:**

*Feil, Michael. "Introducing RadixMLP: Intra-Batch Deduplication for Causal Transformers." arXiv, January 21, 2026. https://arxiv.org/abs/2601.15013*

**BibTeX citation**

```
@misc{feil2026radixmlp,
  author       = {Feil, Michael},
  title        = {Introducing {RadixMLP}: Intra-Batch Deduplication for Causal Transformers},
  year         = {2026},
  month        = jan,
  day          = {21},
  howpublished = {arXiv},
  url          = {https://arxiv.org/abs/2601.15013},
}
```
