---
title: The platform for inference, training, and execution | Baseten
kind: blog
topic: agents
subtopic: memory-context
secondary_topics:
- inference/optimization
summary: Proposes a forward-pass-speed intermediate working-memory layer between the
  lossless KV cache and lossy long-term weights, building on Attention Matching and
  Cartridges cache-compaction research, compressing KV cache 8x while retaining 85%+
  factual accuracy.
triage: null
skip_reason: null
source: baseten
url: https://www.baseten.co/blog/towards-infinite-context-windows-neural-kv-cache-compaction
author: Charles O'Neill
published: '2026-04-01'
fetched: '2026-11-12T06:16:14Z'
classifier: claude
taxonomy_rev: 2
words: 4154
content_sha256: 2f0e2e04f879e4870809739054502b2ea0f5900f83f6d31490198e490b1ed325
---

# The platform for inference, training, and execution | Baseten

Research
# Towards infinite context windows: neural KV cache compaction

Building an intermediate memory layer is a prerequisite for continual learning in LLMs.


- Authors
- Date
- April 1, 2026

TLDR

We compress an LLM's KV cache 8x in milliseconds, retaining 85%+ of factual accuracy across domains. Here's how.

Current LLMs have a memory problem. Not the kind solved by longer context windows, but the kind where an agent forgets everything at the end of a conversation. Today's approaches to persistent memory are crude. They are either lossless but expensive (the full KV cache, scaling linearly with context), or highly compressed and lossy (fine-tuning, markdown-style memory files, RAG). There is no middle ground.

Humans don't work this way. We maintain roughly seven items in lossless working memory (Miller's magic number) which is far less than an LLM's context window. But, we have a large, structured short-term memory that is neither verbatim nor fully compressed into long-term knowledge. This intermediate layer, a lossy but high-fidelity working memory, is what lets us hold a meeting, read a document, or carry a multi-day project without either forgetting everything or memorizing every word.

We believe building this intermediate memory layer is a prerequisite for continual learning in LLMs, that is, the kind that goes beyond cron-job online LoRA updates as production data comes in. Getting to an intern-style LLM that accumulates knowledge across conversations requires three capabilities:

(1) a compressed working memory that sits between the lossless KV cache and the lossy long-term memory stored in weights

(2) a way for models to be able to operate well with this memory in the loop, and possibly even learn to manage this memory themselves (deciding when to compress, what to keep, what to discard)

(3) a mechanism to project what's been learned in compressed memory back into the weights, turning experience into durable knowledge (like humans do during sleep)

This article describes our progress on the first capability. The lossless extreme of LLM memory (the KV cache) stores every token verbatim, but a 128k-token context in some open-source models costs hundreds of gigabytes of state, and every decoding step attends over all of it. Recent compaction methods have shown that this cache can be replaced with a much shorter one that preserves the model's behavior. [Attention Matching](https://arxiv.org/abs/2602.16284) (Zweiger et al., 2026) decomposes the problem per KV-head, selecting compact keys and solving for biases and values analytically to produce a compact cache, with the analytical solution depending on the context. [Cartridges](https://arxiv.org/abs/2506.06266) (Eyuboglu et al., 2025) optimizes compact caches end-to-end via gradient descent. Both achieve strong quality at high compression ratios, but both run per-context optimization at inference time, spending seconds to minutes to hours compressing each new context. For a working memory layer, we need something that runs at forward-pass speed.

The connection to sparse autoencoders (SAEs) is what originally motivated this work. In classical sparse coding, you run an iteration optimization per input to find a sparse representation over a fixed dictionary. SAEs amortize this: they learn a single encoder that produces sparse codes in one forward pass, trading marginal per-input quality for orders-of-magnitude speed gains. Attention Matching and Cartridges are doing the sparse coding equivalent in running a bespoke optimization for every new context.

The question that launched this project was whether we can do what SAEs did for dictionary learning, but for KV cache compaction? Learn a fixed encoder that maps any full cache to a compact one in a single forward pass, generalizing across contexts the way an SAE generalizes across inputs?

**STILL is a perceiver bottleneck that does exactly this.** A fixed set of learned query vectors cross-attend into the full KV cache, producing compact keys and values in a single forward pass; a fast, differentiable compressed memory that the LLM can attend to as if it were real context. Applied iteratively in compressing one chunk, prepending it to the next, compressing again, etc, it can in principle process documents of arbitrary length while maintaining a fixed-size memory. The perceiver is trained via KL distillation: the student (LLM + compact cache) must match the teacher (LLM + full cache) on answer token distributions. The entire LLM is frozen; only the perceiver parameters (\~7M per layer) receive gradients.

The idea is clean, but making it work required solving several non-obvious problems. This article describes the architecture, the fixes that made training converge, and initial results that demonstrate the approach across compression ratios, domains, and model scales.

Two recent methods have demonstrated that KV caches can be compressed with surprisingly little quality loss. Attention Matching (Zweiger et al., 2026) works analytically: for each KV head, it selects or constructs compact keys, solves for attention biases via NNLS, and fits compact values via least squares. The quality is strong, but the method requires reference queries -- and the queries that work well come from a "self-study" phase where the model generates continuations of its own context, adding minutes of per-context compute. Cartridges (Eyuboglu et al., 2025) takes an end-to-end approach: it gradient-optimizes a compact cache directly against downstream loss by backpropagating through the frozen LLM, essentially doing at inference time, for every new context, what we do once at training time. This produces excellent compact caches, but at a cost of minutes to hours per context.

Both methods deliver quality that validates the premise: the information in a KV cache can be preserved at high compression ratios. But both are too slow for a working memory layer. STILL compresses an 8K context in milliseconds; a single forward pass through a small perceiver, with no query generation, no self-study, and no per-context optimization. We also anticipate that as we move from MCQ-based training to training on repeated cache / model continuations (which we’ve already started on; see below), we will remove the remaining self-study requirement from the training pipeline as well, making the entire system self-supervised. Direct quality comparisons to both methods are in progress and will follow.

STILL operates independently at each layer of the frozen LLM. At layer $l$, the compactor takes the full KV cache $(K_l, V_l)$ and produces a compact cache $(C_k, C_v, \beta)$, where $T$ is the original sequence length, $t << T$ is the number of latents, $H$ is the number of KV heads, and $d$ is the head dimension.

The architecture is a standard perceiver:

1. *Latent queries*. A learnable parameter $Z$ provides $t$ query vectors per KV head group. These are the "questions" the perceiver learns to ask of any input cache.
2. *Cross-attention*. Latent queries attend into the concatenated key-value input $[K; V]$. This maps $(T, 2d)$ to $(t, d_lat)$ in $O(T * t * d)$ time, linear in context length.
3. *Self-attention*. Latents attend to each other, enabling coordination, e.g., “I captured the medication dosage, you captured the patient name, we don't need to duplicate.”
4. *Output heads*. Separate linear projections produce compact keys $C_k$, compact values $C_v$, and scalar biases beta from the refined latent representations.

The bias term beta corrects for attention mass lost during compression. In our earlier architecture (random init, 128 latents), we used a mass-matched beta offset of `log(T/t)` to force the LLM to attend to the compact cache; without it, the perceiver learned to produce caches the LLM simply ignored, achieving high utilization scores while fabricating content. With identity initialization, mass-matched beta is no longer needed: the compact cache starts as a near-copy of the input KVs, so the LLM attends to it from the first training step. Beta is instead learned end-to-end via a linear projection, zero-initialized.

Each training step:

1. Prefill (no grad): Forward document tokens through the frozen LLM to obtain the full KV cache at all layers.
2. Teacher logits (no grad): Forward answer tokens with the full cache to obtain target distributions.
3. Compact (with grad): Run STILL at each layer to compress the full cache to t positions.
4. Student logits (with grad): Forward the same answer tokens with the compact cache.
5. Loss: KL(P\_teacher || Q\_student) on answer tokens only.

Training data consists of extractive multiple-choice questions (MCQs) generated from long documents. Each MCQ tests whether a specific fact from the document is preserved in the compact cache. We use a two-stage generation pipeline: Claude Sonnet 4.6 generates questions, then generates distractors separately without seeing the source text (producing harder wrong answers).

We found on-policy data to be important. That is, answer text must be generated by the same model being compacted. Cross-model answers (e.g., Claude-generated answers for a Qwen compactor) sometimes produce catastrophic failure, i.e., the perceiver learns to shift the LLM's distribution toward the other model's patterns rather than preserving information.

The perceiver architecture is simple, but three non-obvious problems initially prevented training from working at scale.

Rotary position embeddings (RoPE) are applied to keys before they enter the KV cache. When the perceiver synthesizes compact keys as weighted combinations of original keys, it blends vectors that carry different positional encodings. A blend of RoPE-rotated keys from positions 5, 42, and 300 is not a valid RoPE-rotated key at any position; the result is a scrambled vector with no coherent positional meaning.

We solve this with a three-step pipeline:

1. *Un-rotate.* Before the perceiver, we apply inverse RoPE to strip positional encoding from the cached keys, recovering position-free representations.
2. *Compress with position-aware cross-attention.* The perceiver has its own internal RoPE on its cross-attention. Key positions match the original token positions $\[0, T)$. Latent query positions are spread evenly across the same range via `linspace(0, T-1, num_latents)`, i.e., the positions scale by $T/t$, so each latent “covers” a proportional span of the original context. This gives the perceiver position awareness without entangling it with the LLM's RoPE encoding.
3. *Re-rotate.* After compaction, we apply forward RoPE to the compact keys at their evenly-spaced positions. Each compact key now carries a clean, well-defined positional encoding that the LLM's attention mechanism can interpret correctly.

Without this pipeline, the perceiver either operates on scrambled positional encodings (producing compact keys that confuse the LLM's attention) or treats all input positions as interchangeable (losing sequential structure). An early MoE training run spent 235 steps with completely broken positional encoding before the bug was identified (util = -1.83, indicating the compact cache was actively worse than no context).

Standard perceiver architectures apply a final RMSNorm to the latent representations before the output heads. In our setting, this normalization constrains the compact key and value vectors to lie on a hypersphere of fixed radius in the latent space, regardless of the content. Real KV cache entries from the LLM have varying norms that carry information – layer norm in the transformer produces outputs whose norms reflect the magnitude of the residual stream updates. By forcing all latent vectors to have unit RMS before projection, the final norm discards this signal and forces the output heads to compensate.

Removing the final norm allows the perceiver to produce compact keys and values with the natural norm variation that the LLM's attention mechanism expects, improving convergence and final quality.

The original perceiver was limited to \~128 latents regardless of context length. At 256 latents, training matched but never exceeded 128-latent performance; at 512+, training diverged entirely. We attributed this to the LLM's attention capacity for synthetic positions.

The breakthrough came from initializing the entire perceiver pipeline as a near-identity function; at init, each latent should simply copy the input KV entry at its corresponding position. This requires coordinated initialization across the full pipeline:

- *Value pathway (identity chain).* `v_proj` and `out_proj` are set to identity matrices, and the output heads `W_key/W_value` are set to identity patterns that extract the key and value halves of the latent representation, respectively. At init, the value pathway is a straight pass-through: whatever the cross-attention selects flows unchanged to the output KVs. At 1:1 compression this is an exact copy; at higher ratios, each latent produces a weighted average of its \~T/t nearest positions.
- *Q/K pathway (biased projections).* With the value pathway as identity, the remaining question is which input positions each latent attends to. We add bias terms to `q_proj` and `k_proj` in the cross-attention. The `k_proj` bias is set to a large constant vector (`q_hat * 10`), making all projected keys content-independent at init – they all point in the same direction regardless of input content. The `q_proj` bias provides a matching query direction. With content stripped from the Q/K pathway, the only remaining signal that differentiates attention across positions is RoPE → the perceiver's internal positional encoding becomes the dominant factor in attention routing.
- *Zero-init residuals.* Self-attention output projections and later blocks' cross-attention output projections are zeroed, so only the first block's identity pathway is active at init.

The effect is that at initialization, latent i attends most strongly to the input positions closest to its RoPE position (position `i * T/t`), and copies those positions' keys and values through the identity value pathway. Training then refines this from a position-copying baseline toward content-aware compression. The identity init gives every latent a meaningful starting point and prevents the collapse where hundreds of latents converge to similar representations under a weak gradient signal. It should be noted that in this setup, $d_{lat}=2d$

With this initialization, STILL scales monotonically from 128 to 8192 latents, with MCQ accuracy increasing from \~60% to \~95% as compression ratio decreases (Figure 1). The previous 128-latent ceiling was not a fundamental limit of LLM attention over synthetic positions – it was an optimization failure (although the architecture did need to change as well; see below).

All experiments use Qwen3-4B with 8192-token contexts unless otherwise noted. Training runs on 8x H200 GPUs with DDP. The perceiver has 2 blocks, 1 cross-attention head, 1 self-attention head, and latent dimension 256. Total trainable parameters: \~7.1M (0.18% of the base model). We evaluate on held-out extractive MCQs and continuation cross-entropy.

We report two main evaluation metrics. MCQ accuracy measures factual retention: can the model answer extractive multiple-choice questions about the document using only the compact cache? This is deliberately adversarial because each question targets a specific fact (a medication dosage, a date, a variable name) that the compactor must have preserved among thousands of tokens. It tests pointwise retrieval, the hardest task for lossy compression.

Utilization measures how much of the gap between no-context and full-context performance the compact cache closes, defined as: `utilization = (no_context_metric − compact_metric) / (no_context_metric − full_cache_metric)`.

A utilization of 1.0 means lossless compression (compact matches full cache). A utilization of 0.0 means the compact cache is no better than having no context at all. We compute utilization over cross-entropy (CE) and MCQ accuracy.

**Latent sweep with block-diagonal initialization.** All metrics improve monotonically as the number of latents increases from 128 (64x compression) to 8192 (1:1, no compression). At 1024 latents (8x compression): MCQ accuracy \~85%, KL \~0.15, CE utilization \~0.93. The KL and CE are computed over the full context LLM’s reasoning trace tokens in response to the MCQ prompt. Continuation here refers to the task of completing the next 128 tokens in the compacted passage when prompted with 64 cue tokens.

With identity initialization, STILL scales monotonically across the full range of latent counts. At 1024 latents (8x compression of an 8192-token context), MCQ accuracy reaches \~85% with utilization above 0.90. Even at 128 latents (64x compression), the perceiver preserves enough information for \~60% MCQ accuracy, which is well above the 20-22% no-context baseline.

The smooth scaling curve has a practical implication in that the compression ratio is a continuous knob, not a binary works/doesn't-work decision. Deployments can choose their operating point on the accuracy-memory tradeoff based on their latency and memory budget.

**Domain-specific training at 1024 latents (8x compression).** We trained separate STILL instances on four domains (financial filings, legal documents, source code, and Project Gutenberg literature) each with domain-specific MCQ datasets. The perceiver achieves strong compaction across all domains at 8x compression (1024 latents / 8192 context). The final MCQ accuracy is as follows:

Financial and code documents compress most effectively (86-90% MCQ accuracy), likely because they contain structured, locally-concentrated information that maps well to individual latents. Legal and Gutenberg text are harder; they have more distributed, context-dependent information that is inherently harder to compress into discrete positions.

**Constant 8x compression with varying context length.** Holding compression ratio fixed at 8x, we vary context length (and correspondingly the latent count). MCQ accuracy is stable at 85-92% across configurations, confirming that the perceiver learns compression as a ratio-dependent operation, not a latent-count-dependent one.

An important control experiment was holding the compression ratio fixed at 8x while varying the absolute context length and latent count. MCQ accuracy remains stable at 85-92% across all configurations (128 latents for 1k context through 1024 latents for 8k context), confirming that STILL learns compression as a function of the ratio, not the absolute number of positions (although there is a slight drop-off). This is a prerequisite for the variable-length generalization we discuss below.

**Cross-domain transfer.** Each cell shows performance when a perceiver trained on one domain (column) is evaluated on another (row). Diagonal entries (in-domain) are strongest, but off-diagonal transfer is surprisingly robust: 70-86% MCQ accuracy across all train/eval pairs. A perceiver trained on financial documents achieves 87% MCQ accuracy on financial eval, but also 74% on legal, 70% on Gutenberg, and 72% on code. The Code-trained checkpoint shows the broadest transfer, reaching 78-89% across all eval domains. The Financial checkpoint transfers worst, but no cross-domain pair drops below 70% MCQ accuracy.

CE utilization is similar. The diagonal entries (in-domain) range from 68-77%. Off-diagonal CE utilization is lower (53-79%), with the largest drops when evaluating financial checkpoints on Gutenberg data; evaluating Gutenberg checkpoint on financial data actually yields an improvement. The continuation metric is more sensitive to domain shift than MCQ accuracy, likely because it evaluates the full token distribution rather than just whether specific facts are preserved.

A single STILL pass compresses a fixed-length context (e.g., 8K tokens → 1024 latents). But the compactor can be applied iteratively: process the first chunk of a document, compact it, prepend the compact cache to the next chunk, compact the combined cache, and repeat. After N passes, the final compact cache represents the entire document in a fixed number of latent positions, regardless of how long the original was.

The key question is whether the perceiver can handle its own output as input. That is, compact KV entries from a previous pass occupy a different region of representation space than real KV entries from the LLM. The natural training strategy is to randomize the number of passes per training step (sampling from e.g. `{1, 2, 4, 8}`), so the perceiver sees both fresh and previously-compacted input during training.

We are currently evaluating iterative compaction with the identity-init architecture, both with the current setup and training explicitly for re-compaction. Results will follow.

The central bet of this work was that KV cache compaction is regular enough across contexts to be amortized into a learned forward pass. The results confirm this: a 7.1M-parameter perceiver, trained on a few thousand documents from a single domain, generalizes to held-out documents from both the same and different domains with minimal quality loss. The learned compression function captures something about the structure of attention in Qwen3-4B that is not context-specific. We are now in the process of scaling this up to massive compression (256x) and iterative compaction.

STILL is a first step on what we see as a longer road to continual learning in LLMs. The current landscape of "model memory" has two extremes and nothing in between:

- **Lossless but expensive.** The KV cache stores every token verbatim. Perfect fidelity, but memory and compute scale linearly with context length. When the window fills up, everything is lost.
- **Compressed but lossy.** Fine-tuning bakes experience into weights, but it's slow, coarse-grained, and prone to catastrophic forgetting. RAG and markdown-style memory files are brittle workarounds that store facts outside the model's native representations.

What's missing is the middle layer, i.e., a compressed working memory that preserves the structure and fidelity of the KV cache at a fraction of the cost. This is what STILL provides: a differentiable, learned compression of the model's own internal representations, stored in a format the model can natively attend to.

But compressed memory alone is only the first of three capabilities we think are needed:

1. *Compressed working memory (this work).* A learned compactor that produces compact KV caches the LLM can attend to as if they were real context. STILL demonstrates this is feasible: 8x compression with 90%+ factual retention, generalizing across domains, with a forward-pass cost. Applied iteratively, it should extend to unbounded context lengths with fixed memory.
2. *Learned context management.* The model should learn to manage its own memory in deciding when to compress, what compression ratio to use, and what information to prioritize. This means integrating STILL into the model's action space and training with RL so the model can learn context management policies from reward signals. Rather than compaction being a fixed post-processing step, the model would invoke it as a tool: "My context is getting long, compress the older conversation but keep the recent code changes at full fidelity." The perceiver's differentiability makes it compatible with policy gradient methods, and its fixed computational cost makes it practical to invoke repeatedly during generation.
3. *Memory consolidation into weights.* The most speculative piece: can we project what's been learned in compressed KV caches back into the model's weights? One path is a hypernetwork that takes a compressed KV cache, representing a body of experience, and outputs a LoRA adapter for the model. This would be the mechanism for turning short-term compressed memory into durable long-term knowledge, closing the loop between in-context learning and weight updates. If the compactor learns to produce structured, information-dense representations (which the cross-domain transfer results suggest it does), these representations might be a better substrate for weight projection than raw text or token-level gradients.

Together, these three capabilities would produce an LLM that accumulates knowledge across conversations: compressing recent context into working memory, managing that memory actively, and periodically consolidating important patterns into its weights. Not a chatbot that forgets everything at the end of a session, but an agent that gets better at its job over time.

We're early on this road. STILL demonstrates that the first capability (compressed working memory) is achievable with current methods. The next steps are extending to iterative compaction for unbounded contexts, training a universal compactor that works across domains, and beginning the integration with RL for learned context management.

**KV cache compaction.** [Attention Matching](https://arxiv.org/abs/2602.16284) (Zweiger et al., 2026) provides per-head analytical compaction via key selection, NNLS beta fitting, and least-squares value reconstruction. [Cartridges](https://arxiv.org/abs/2506.06266) (Eyuboglu et al., 2025) optimizes compact caches end-to-end via gradient descent. Both operate per-context at inference time. Token eviction methods (H2O, ScissorHands, StreamingLLM) drop tokens based on attention scores but cannot synthesize new representations.

**Perceiver architectures.** The [Perceiver](https://arxiv.org/abs/2103.03206) (Jaegle et al., 2021) introduced learned latent queries for handling long inputs via cross-attention bottlenecks. [Perceiver IO](https://arxiv.org/abs/2107.14795) (Jaegle et al., 2022) extended this to structured outputs. [Perceiver Resampler](https://arxiv.org/abs/2204.14198) in Flamingo (Alayrac et al., 2022) applied the same idea to vision-language models. STILL applies the perceiver bottleneck to KV cache compression, a setting where the input (KV cache entries) is highly structured and the output must be compatible with a frozen LLM's attention mechanism.

**Knowledge distillation.** Our KL distillation objective follows standard practice ([Hinton et al., 2015](https://arxiv.org/abs/1503.02531)), with the frozen full-cache model as the teacher and the compact-cache model as the student. The key difference from model distillation is that we distill the cache, not the model.

STILL demonstrates that KV cache compaction can be amortized into a learned forward pass. A small perceiver, trained via KL distillation on a frozen LLM, achieves up to 92% extractive accuracy at 8x compression, generalizes across domains, and scales monotonically to 8192 latents. Three architectural fixes (un-rotate/re-rotate RoPE with perceiver-internal positional encoding, removing the final norm, and identity initialization with biased attention projections) were all necessary to unlock this scaling behavior.

But the goal is not only efficient inference. Compressed KV caches are a new kind of model memory: denser than raw context, richer than weight updates, and natively compatible with the model's attention mechanism. We see this as the foundation for continual learning: models that compress experience into working memory, learn to manage that memory actively, and eventually consolidate knowledge into their weights. STILL is the first step, and iterative compaction should extend it beyond any fixed context window.

**For attribution in academic contexts, please cite this work as:**

*O'Neill, Charles. "Towards infinite context windows: neural KV cache compaction." Baseten Research, April 1, 2026.* [https://www.baseten.co/research/towards-infinite-context-windows-neural-kv-cache-compaction](https://www.baseten.co/research/towards-infinite-context-windows-neural-kv-cache-compaction)

**BibTeX citation**

```
@misc{o'neill2026still,
  author       = {O'Neill, Charles},
  title        = {Towards Infinite Context Windows: Neural {KV} Cache Compaction},
  year         = {2026},
  month        = April,
  day          = {1},
  howpublished = {Baseten Research},
  url          = {https://www.baseten.co/research/towards-infinite-context-windows-neural-kv-cache-compaction/},
}
```
