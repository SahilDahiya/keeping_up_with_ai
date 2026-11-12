---
title: Repeated KV cache for long-running agents
kind: blog
topic: agents
subtopic: memory-context
secondary_topics:
- inference/optimization
summary: Tests whether Attention Matching's KV-cache compaction (50x compression in
  one shot) can be applied repeatedly as a long-running agent's context grows; using
  Qwen3-4B on the LongHealth clinical-QA benchmark, it evaluates fresh versus incremental
  re-compaction strategies under a fixed memory budget across sequential patient arrivals.
triage: null
skip_reason: null
source: baseten
url: https://www.baseten.co/blog/repeated-kv-cache-for-long-running-agents
author: Charles O'Neill
published: '2026-03-05'
fetched: '2026-11-12T06:16:08Z'
classifier: claude
taxonomy_rev: 2
words: 2073
content_sha256: 7fce431777d80670fca3a1db0bcafe3cc3c1c095b06db27de22567dd8b78a8c0
---

# Repeated KV cache for long-running agents

Research
# Repeated KV cache for long-running agents

Can you compress, add new context, and compress again, maintaining a fixed memory budget as information accumulates indefinitely?


- Authors
- Date
- March 5, 2026

A coding agent accumulates tool outputs for hours; a clinical assistant ingests patient records one at a time. In both cases, context grows without bound while memory stays fixed.

The standard solutions (truncation, summarization, retrieval) each sacrifice something. Truncation bets that old context is dispensable. Summarization is lossy in ways you can't predict: the lab value that seemed unimportant at compression time turns out to answer a later question. Retrieval requires knowing what's relevant before you've seen the query.

Instead of operating on text, Attention Matching ([Zweiger et al., 2026](https://arxiv.org/abs/2602.16284)) compacts the model's key-value cache directly in latent space, replacing $T$ cached key-value pairs with $t \ll T$ fitted replacements that approximate the same attention behavior. Applied once, it achieves 50× compression with minimal quality loss, in seconds.

But single-shot compression isn't enough for a growing context. Can you compress, append new context, and compress again, maintaining a fixed memory budget as information accumulates indefinitely?

When attention operates over two concatenated KV blocks, it decomposes into a mixture of each block's local attention output, weighted by each block's share of the total unnormalized mass. This means compaction reduces to two local objectives that don't depend on future tokens: match the block's attention output, and match its attention mass.

The algorithm solves these sequentially, per layer, per KV head. First, select $t$ keys from the original $T$ by attention score. Second, fit a scalar bias $\beta \in \mathbb{R}^t$ via nonnegative least squares so that the compact keys' reweighted mass matches the original. Without $\beta$, the compacted block would be systematically underweighted in any future concatenation. Third, fit replacement values $C_v \in \mathbb{R}^{t \times d}$ via ordinary least squares so that the compact block's attention output matches the original under the new attention weights.

Two details matter for what follows. The value fitting solves $\min_{C_v} |XC_v - Y|F^2$, where each row of $X$ is the attention weight vector over compact keys for one reference query, and $Y$ contains the corresponding target attention outputs. This is a standard regression, and its quality depends on the conditioning of $X$. And the reference queries $Q_\text{ref}$, the proxy for future queries, come from a forward pass on the context itself, which produces broad, reconstructive attention patterns rather than sharp retrieval patterns.

We used Qwen3-4B on [LongHealth](https://arxiv.org/html/2401.14490v1), a clinical QA benchmark with medical records for 20 fictional patients. Each patient contributes \~12,000 tokens of dense clinical notes and 20 five-option multiple-choice questions testing factual recall: patient names, lab values, medication dosages, and temporal ordering. We simulated an incremental agent session: 5 patients arrive sequentially, and after each arrival, we compress the accumulated context to a fixed memory budget before answering questions about all patients seen so far. Results are averaged across 4 context groups (20 patients, 400 questions per step).

**Fresh compaction:** At each step, re-prefill all accumulated text from scratch, then compress the clean cache in one shot. No approximation feeds into any subsequent approximation. We test this with both chunked compaction (fitting each patient's attention independently, then stitching results together) and monolithic compaction (a single least-squares fit over the entire sequence).

**True re-compaction:** A persistent cache that grows incrementally. Each new patient's tokens are appended to the existing (previously compressed) cache via chunked prefill, then the whole thing is re-compressed to budget. This is what a real agent would do: it never re-reads old text. We test this with monolithic compaction at a 4,096-token budget.

Our first result had nothing to do with re-compaction. At a 12,288-token budget, fresh monolithic compaction (a single least-squares fit over the entire multi-patient sequence) scored 30.8% at step 1 (24k → 12k, just 2× compression). At the same budget, fresh chunked compaction scored 79.3%.

The 49% gap comes from the structure of attention on concatenated independent documents. When the model processes a token inside Patient 1's chemotherapy notes, its attention is overwhelmingly local: it attends to the dosage, the cycle timing, and the protocol name. It has no reason to attend to Patient 2's renal imaging. The result is an approximately block-diagonal attention matrix: dense within each patient, near-zero between patients.

This structure makes global least-squares fitting ill-posed. Each row of the design matrix $X$ is a compact attention weight vector for one reference query. Queries from Patient 1 load on Patient 1's columns; queries from Patient 2 load on Patient 2's columns. The rows cluster into nearly orthogonal subspaces. A single $C_v$ must serve both, but because the subspaces barely overlap, fitting one patient's queries tells you almost nothing about the other's.

We tested the obvious alternative explanation: that the system was underdetermined. A query budget sweep from 20,000 to 60,000 queries per KV head (5× overdetermination relative to the number of compact keys) moved accuracy from 21.7% to 23.8%. More rows in Patient 1's subspace don't help fit Patient 2's subspace. The problem is geometric, not statistical.

Chunked compaction fixes this by splitting at patient boundaries and fitting each chunk independently. Each sub-problem has dense, full-rank $X$ and captures local attention structure faithfully. This is a structural requirement for any heterogeneous multi-document context, not an optimization choice.

With chunked compaction, fresh-from-text compression shows clean, predictable degradation. At a 12,288-token budget with chunked compaction (the configuration we call "Chunked fresh compaction": fresh prefill and compress at each step, using article boundaries for chunk-local fitting):

The marginal cost of each additional increment of compression decreases: 11.4pp for the first 2×, then 5.6, 4.3, 3.8 for each subsequent 1×. Roughly logarithmic, with no phase transition or sudden collapse. At step 0, chunked fresh compaction actually *exceeds* the full-context accuracy (90.7% vs 81.5%), likely because compaction acts as a form of denoising.

At the same 12k budget, text summarization scored 30.4%, barely above the 34.0% no-context baseline. Attention matching (AM) preserves the kind of detail that summarization discards: at 5× compression, the model can still recall specific lab values, medication dosages, and temporal ordering across five patients' records.

Where does the 25% gap between uncompressed and 5× come from? Partly from information genuinely lost at high compression. But likely also from a mismatch between reference query geometry and test-time query geometry. The reference queries come from context-prefill: the model reconstructing what it just read, producing broad, diffuse attention patterns. LongHealth questions demand needle-in-a-haystack retrieval, nearly all attention on a handful of specific tokens. The fitted $C_v$ was optimized for diffuse queries and may be poorly calibrated for sharp ones.

The original paper shows that self-study reference queries, which produce more targeted attention patterns, consistently improve compaction quality; we used only context-prefill.

With local fitting established as a structural requirement and fresh compression characterized, we can isolate the question we started with: what happens when you compress the already-compressed?

We ran all three compaction strategies at a matched 4,096-token budget (aggressive compression, 3–15× across steps), across 4 context groups:

The three lines decompose the total accuracy loss into distinct components. At step 3 (4 patients, \~12× compression), starting from the full-context baseline of 81.3%:

- **Chunked fresh compaction** (chunked, fresh): 52.8%, a 28.5% cost from compression itself.
- **Fresh compaction**: 46.4%, an additional 6.4% from fitting globally instead of locally.
- **True re-compaction**: 30.5%, a further 15.9% from compressing the already-compressed.

The compression cost is the largest component and largely unavoidable at 12× ratios. The local fitting penalty is moderate and fixable by using chunked compaction. The re-compaction penalty is the open problem.

To map these penalties more precisely, we ran all three strategies at seven budgets from 512 to 16,384 tokens, evaluating on two patients (\~24k raw tokens at step 1, a single re-compaction event):

The data reveals two regimes separated by a sharp transition:

- **Below 8k (compression ≥ 3×):** Monolithic fitting works. All three paths produce coherent output. Chunked fresh compaction leads, Fresh Compaction trails by 10–13% (the local fitting penalty), and True Re-compaction trails Fresh Compaction by a further 4–11% (the re-compaction penalty). The re-compaction penalty peaks at 2,048 tokens (\~12× compression), suggesting that moderate compression creates the worst conditioning for the $C_v$ regression.
- **Above 8k (compression ≤ 3×):** Monolithic fitting collapses. Fresh Compaction (fresh compaction with no recursive error) drops to 12–17%, confirming this is a fitting failure, not a re-compaction problem. Chunked fresh compaction, using chunked compaction, holds at 73–80%. The 50–67% gap between Chunked fresh compaction and Fresh Compaction is entirely attributable to chunked vs monolithic fitting.

At budget=8,192, True Re-compaction (56.3%) beats Fresh Compaction (28.2%) by 28%, the opposite of the expected direction. This is because re-compaction inadvertently helps: True Re-compaction's source at step 1 is \~20k tokens (8k compressed Patient 1 + 12k raw Patient 2), shorter than Fresh Compaction's 24k (both patients uncompressed). The monolithic fit operates on a less heterogeneous sequence, accidentally sidestepping the failure. This confirms that absolute source length, not compression ratio, is the critical variable for monolithic fitting.

All outputs remain coherent and parseable throughout. The model doesn't collapse; it just loses accuracy. But the re-compaction penalty is systematic and grows with rounds.

What drives it? The mechanism is intrinsic to recursive least-squares fitting. Each round solves:

$$
C_v^* = (X^\top X)^{-1} X^\top Y
$$

In fresh compaction, $Y$ is always computed from a clean forward pass. The targets are exact. In re-compaction, $Y$ is computed from the *previously compacted* cache. The targets are themselves approximations, and the error propagates through a recurrence:

$$
e_{r+1} \leq ||A_r|| , e_r + \eta_r
$$

where $e_r$ is output approximation error at round $r$, $\eta_r$ is fresh noise from the current round's compression, and $||A_r||$ is the local amplification factor, determined by the condition number of the design matrix $X$ for that round's regression.

When $||A_r|| > 1$ on some heads, error grows geometrically across rounds. This happens when $X$ is poorly conditioned: when the compact attention weights don't span enough of the query space, or when a few keys dominate.

The amplification is not uniform across heads. A handful of poorly-conditioned heads drive worst-case error while most remain stable.

This is the JPEG-of-a-JPEG problem. Each round of lossy compression is individually reasonable, but the errors introduced by one round become the signal for the next. The structure of AM (fitting values by least squares against attention-output targets) means the error amplification is governed by the conditioning of the attention weight matrix, which is a property of the key distribution and query distribution rather than something the algorithm can trivially control.

For practical deployment: if you can afford periodic re-prefill from raw text (say, after every few turns), you get clean compression with no compounding penalty. Chunked fresh compaction with chunked compaction at 2–5× maintains 65–80% accuracy on dense factual QA, well above both the no-context floor and what summarization achieves at matched budget.

If you need true incremental compaction without re-reading old text, the current penalty is 4–16% at the ratios we tested. Whether this is acceptable depends on the task. For conversational agents where approximate recall is fine, it probably is. For clinical factual recall, where every lab value matters, it may not be.

Three things are likely to reduce the re-compaction penalty. Nonuniform head budgets, the original paper's most impactful component (which we didn't use), would allocate more capacity to the sensitive heads that drive worst-case error amplification. Self-study reference queries would better capture the sharp retrieval patterns exhibited by test-time queries. And regularization of the $C_v$ fit could bound the amplification factor $|A_r|$ at the cost of per-round approximation quality.

One-shot compression is a regression problem. Repeated compression is a dynamical system. The tools you need to analyze them are different: for one-shot, it's bias-variance and approximation quality; for repeated, it's stability, amplification, and convergence. Single-round compaction already works well. The open question is how to make the recurrence stable. We’ll explore this more in our future research.

**For attribution in academic contexts, please cite this work as:**

*O'Neill, Charles. "Repeated KV Cache for Long-Running Agents." Baseten Research, March 5, 2026. https://www.baseten.co/research/repeated-kv-cache-for-long-running-agents/*

**BibTeX citation**

```
@misc{oneill2025rgt,
  author       = {O'Neill, Charles and Partridge, Harry and Jayasekara, Mudith},
  title        = {Upweight the Strategy, Not the Tokens: Faster Training with Explicit Reasoning Through {RGT} (Rationale-Guided Training)},
  year         = {2025},
  month        = oct,
  day          = {29},
  howpublished = {Baseten Research},
  url          = {https://www.baseten.co/research/upweight-the-strategy-not-the-tokens-faster-training-with-explicit-reasoning-thro/},
  note         = {Accessed: 2026-03-12}
}
```
