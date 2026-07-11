---
title: Kimi QK-Clip and multi-head latent attention
topic: models
subtopic: reasoning
secondary_topics:
- inference/optimization
summary: Explains Kimi QK-Clip, multi-head latent attention, and why training-inference
  key construction affects stability.
source: fireworks
url: https://fireworks.ai/blog/kimi-qkclip
author: null
published: '2025-07-22'
fetched: '2026-07-11T04:17:08Z'
classifier: codex
taxonomy_rev: 1
words: 2199
content_sha256: 4fe2bb578d3ba606103b9b192daa1541f91ab6e9e6214bae85194572e1255cbe
triage: keep
skip_reason: null
---

# Kimi QK-Clip and multi-head latent attention

- A Comment Exchange on the Kimi Blog
- 2. Background: LLMs, Attention, and Why Efficiency Matters
- 3. The Problem and Math Deep Dive: Training vs. Inference in Multi-Head Latent Attention (MLA)
- First, Recap the Big Idea in Simple Terms
- Step 1: Understanding the Input and Basic Setup
- Step 2: Building the Key in Training (Full Version)
- Step 3: Building the Key in Inference (Simplified Version) – And Why We Skip the Projection
- Step 4: Why This Breaks Normalization (Like RMSNorm) – And Where Else Norms Can (or Can't) Help
- 4. Visualizing It All: Step-by-Step Through the Graph
- The Genius of QK-Clip: Kimi's Smart Solution, and Why This Matters

Today, we're unpacking a clever insight from the researchers behind Kimi K2, a powerful LLM from Moonshot AI. This all started from a fascinating exchange in the comment section of a [technical blog post](https://kexue.fm/archives/11126).

We'll break it down step by step, with real math to appreciate the elegance, but I'll explain it like we're chatting over coffee. By the end, you'll see why this "[QK-Clip" trick](https://moonshotai.github.io/Kimi-K2/) is so smart and how it makes models like Kimi more reliable for your apps.

Anecdotally, I have heard whispers on the street that there are quality trade-offs with using MLA, and this may be the secret ingredients that some of the top labs have been missing, paving the future for inference to be more efficient across the board.

Our story begins on the comment section of a blog post by Su Jianlin (苏剑林) on [https://kexue.fm/archives/11126](https://kexue.fm/archives/11126).

- •Someone asked, why “during decoding, you cannot fully materialize the k you get during training”
- •Jianlin structural difference in how Keys are computed in Multi-Head Latent Attention (MLA), a memory-efficient variant used in models like Kimi K2 (inspired by DeepSeek-V2). In training, Keys are fully "materialized" (computed and structured in a way that allows normalization), but in decoding (inference), a key component is missing, breaking techniques like RMSNorm.

This exchange fascinated me because it highlights a real-world engineering challenge in scaling LLMs. As app devs, we often treat models as black boxes, but peeking inside reveals why innovations like QK-Clip are crucial for stable performance. Inspired by this, I created an animated visualization to make the concept accessible.

But let me explain, in case you don’t know the details about MLA.

If you're building GenAI apps- say, a chatbot or text generator, you're likely using LLMs like GPT models or Kimi models via APIs. At their core, LLMs are giant neural networks that predict the next token (word or subword) in a sequence. They do this by processing inputs through layers of "attention" mechanisms.

Attention is the secret sauce: It lets the model weigh the importance of different parts of the input. In standard Multi-Head Attention (MHA), for each position in the sequence, we compute:

- •**Queries (Q)**: What the current token is "asking" about.
- •**Keys (K)**: Representations of past tokens to match against Q.
- •**Values (V)**: The actual info to retrieve based on Q-K matches.

The attention score is basically , where is the dimension, and this gets multiplied by V.

But here's the catch for large models: During inference (decoding), especially for long conversations, storing all K and V (the "KV cache") eats up memory. Models like Kimi K2 use Multi-Head Latent Attention (MLA) to compress this.

In MLA, Keys and Values are projected into a lower-dimensional "latent" space (e.g., from 5120 dims to 512), saving memory without losing much power. This is genius for apps handling long contexts, like summarizing documents or maintaining chat history.

However, as the comment revealed, MLA introduces a subtle difference between training (where we process the whole sequence at once) and inference (where we generate one token at a time). This can cause instability, like exploding values in attention scores.

If you're an app developer who's used LLMs but never really dug into how they compute attention under the hood, this section is for you. We'll merge the problem explanation with a detailed math breakdown, stepping through everything one piece at a time. Imagine we're walking through a recipe: I'll define each ingredient (variable), show how they're mixed (the formulas), and explain what goes wrong if you skip a step.

Along the way, I'll address two common follow-up questions proactively:

(1) Why not just compute the missing projection in inference, isn't skipping it an inconsistency?

(2) Does this breakage only affect norms in one spot, or can you norm elsewhere to fix explosions?

By the end, you'll see exactly why training and inference differ in MLA, why that breaks normalization tricks like RMSNorm, and how it sets up Kimi's clever fix.

In attention mechanisms (the part of LLMs that decides what to "pay attention to" in a sentence), we need to create **Keys** (K) for each token. These Keys are like searchable tags that help the model match the current query to past context.

In **Multi-Head Latent Attention (MLA)-** used in efficient models like Kimi K2 to save memory. Keys are built in a compressed way. During **training** (when the model learns from data, processing entire sequences at once), Keys are fully built with all parts.

But during **inference** (or "decoding," when your app generates text one token at a time), we simplify the process to be faster and use less memory. This simplification skips a key step, which is fine for basic computation but breaks add-on techniques like normalization (which keeps values from exploding).

The result? Without careful handling, attention scores can go haywire in inference, leading to weird outputs or crashes in your app. Now, let's unpack the math to see why.

Every token in your  input (like a word in a prompt) starts as a high-dimensional vector called the **embedding**, denoted . Here:

- •i is the position of the token in the sequence.
- •To make attention efficient, MLA first compresses part of this into a "latent" space- a smaller vector to save memory.
- •We multiply by a weight matrix $$, where is much smaller than (e.g., ).
- •Result: $$.

This is the compressed "latent" version of the token. It's like summarizing a long article into key points- efficient for storage in the KV cache during long chats.

In training, we build the Key () for each attention head(s) (models have multiple "heads" to focus on different aspects). The Key is concatenated from two parts:

- •**Part 1: The Projected Latent (Head-Specific)**- •Take the latent .
- •Multiply it by a head-specific weight matrix , where is the per-head key dimension (e.g., 128).
- •Result: .

- •**Part 2: The Rotary Path (Position-Aware)**- •Take the original
- •Multiply by another weight matrix , where is small (e.g., 64).
- •Then apply Rotary Position Embedding (RoPE), , which rotates the vector based on position i to help the model understand order.
- •Result: .

- •**Concatenate Them**: Stack these two vectors vertically:



(E.g., 128 + 64 = 192 dimensions.)

This full Key is "materialized"- fully computed and structured, ready for anything, like applying norms. Here is the MLA construction in the original DeepSeek paper. I circled the concat in orange.

In inference, we optimize for speed: We cache the latent once and reuse it across heads, avoiding recomputing heavy projections. So, the Key (now shared, not per-head) becomes:

- •**Part 1: Direct Latent (No Projection)**- •Just use  directly—no multiplication by ! This saves compute and memory, as  is "absorbed" into other parts of the model (like the query or output weights). - •Specifically, the benefit from MLA is so that we can precompute components during training. If we write out the formula
- •
- •Here can be precomputed for inference, so simply “disappears” in inference


- •Just use  directly—no multiplication by ! This saves compute and memory, as  is "absorbed" into other parts of the model (like the query or output weights).
- •**Part 2: The Rotary Path**- •Same as training: .

- •**Concatenate Them**:

(E.g., 512 + 64 = 576 dimensions—notice it's larger and structurally different because .)

Key difference: No in Part 1! This is efficient but means the Key isn't "fully materialized" like in training.

Now, addressing a natural follow-up: Why not just compute in inference anyway? Isn't skipping it an inconsistency between training and inference?

It could be computed, but that would defeat MLA's main goal: massive efficiency in memory and speed.

Instead, the projection is "absorbed" or fused mathematically into other weights (e.g., query and output keeping outputs identical without explicit computation. For example, the effect of is pre-multiplied into queries: , so you query the latent directly. This isn't an inconsistency in the core math (attention outputs match), but it does alter the internal structure—making the Key non-materializable for add-ons like norms.

Normalization techniques, such as RMSNorm, are used to stabilize attention by scaling vectors to prevent huge values (explosions). RMSNorm for a vector is:

(where is element-wise division, and is a tiny number to avoid division by zero).

Here, RMSNorm is often part of "QK-Norm": Normalizing Queries and Keys before their dot product $Q K^T$ to tame explosions from unchecked weight growth.

- •**In Training**: We can apply RMSNorm to the full Key . The norm is computed over both parts, including the projected latent . Everything is there, so it works: The model learns stable weights.
- •**In Inference**: We try to apply RMSNorm to , but... the structure is different! The first part is raw (512 dims, different scale/distribution) vs. projected (128 dims). Worse, since the projection is fused elsewhere, norming the raw latent would mess up the fused math, leading to wrong outputs. The blog comment nails it: You can't compute the norm of the absent .

This leads to another follow-up: Does this just break RMSNorm on that specific part (the Keys in attention)? Can you apply norms elsewhere to fix QK explosions?

Yes, it specifically breaks QK-Norm (RMSNorm on Keys/Queries in attention), as you can't norm the missing projected part. You can (and do) apply norms elsewhere—like LayerNorm after attention or FFN layers, which stabilizes the overall hidden state without MLA issues. But these don't target QK explosions directly: If blows up (e.g., max values in thousands), Softmax overflows, causing repetitive or garbage output. Norms elsewhere help the model overall but can't prevent that local issue in attention—the hotspot for explosions from weights like and .

To make this tangible, I built an animated flowchart using NetworkX and Matplotlib (code shared in the query). It’s a side-by-side views of Training (left) and Decoding (right), with nodes as variables/operations, edges as computations, and colors indicating success (light green) or failure (salmon red). The animation highlights paths orange step-by-step, unfolding the process.

Here's a walkthrough:

- •**Overall Layout**: At the top is the input token embedding (e.g., = 5120). It branches left (latent compression) and right (rotary path). They merge into the Key , then to RMSNorm and Output.
- •**Step 1: Input Splitting**- •Both sides start with .
- •Left: Multiplies by to get compressed latent (e.g., = 512).

- •**Step 2: Left Branch (Latent Projection)**- •Training: *multiplies by head-specific * (green node) to get (e.g.,).
- •Decoding: This projection is missing (red node labeled "Missing Projection")! Instead, it uses direct (no multiplication).

- •**Step 3: Right Branch (Rotary Embedding)**- •Both: multiplies by (e.g., ), then applies RoPE () via a curved self-loop (for position encoding).
- •Result: .

- •**Step 4: Concatenation to Key**- •Merge the branches: Training gets full Key ; Decoding gets incomplete \boldsymbol{k}_i \in \mathbb{R}^{d_c + d_r}$ (note $d_c > d_k, so dimensions mismatch slightly in structure).

- •**Step 5: Applying RMSNorm**- •Training: Norm works on the full vector (green).
- •Decoding: Norm fails due to missing component (red)—can't compute the norm of the absent projection!

- •**Step 6: Output to Attention**- •Training: Stable output.
- •Decoding: Potential instability.


The animation reveals this flow sequentially, ending with a note on dimensions and QK-Clip's fix. Colors make the "missing piece" pop—training flows smoothly in green, decoding stalls in red.

Kimi researchers spotted that Muon (an optimizer without weight decay) causes "MaxLogit explosions" (huge pre-Softmax values). Instead of runtime norms (which break in MLA decoding), QK-Clip clips the weights and during training when MaxLogit exceeds a threshold :

Final version:

If :

For column-wise weights like :

For row-wise like : .

This "absorbs" the fix into the weights permanently, so inference stays stable without structural changes. It's smart because it's per-head, avoids over-clipping, and works with MLA's latent tricks—enabling Kimi K2 to scale to billions of parameters. For you as a dev, this means more reliable APIs: Fewer crashes in long sessions, better outputs without custom hacks.

We started with a curious comment on a Kimi blog and ended with a visualization demystifying MLA's training-inference gap. This isn't just academic—understanding these internals helps you choose models wisely (e.g., Kimi for memory-efficient chats), and appreciate the engineering smarts behind them. Kimi's QK-Clip shows how targeted fixes can push LLMs further, making your GenAI apps more robust.

I have attached the code for the animation at the end. Watch the video—it's enlightening! Questions? Drop a comment. Happy building! 🚀

123456789101112131415161718192021222324252627282930313233343536373839404142434445464748495051525354555657585960616263646566676869707172737475767778798081828384858687888990919293949596979899100101102103104105106107108109110111112113114115116117118119120121122123124125126127128129130131132133134135136137138139140141142143144145146147148149150151152153154155156157158159160161162163164165166167168169170171172173174175176177178179180181182183184185186187188189190191192
