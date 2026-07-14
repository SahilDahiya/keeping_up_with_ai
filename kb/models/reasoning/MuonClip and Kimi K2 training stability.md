---
title: MuonClip and Kimi K2 training stability
topic: models
subtopic: reasoning
secondary_topics: []
summary: Explains MuonClip as a stability technique for large-scale Kimi-style model
  training.
source: fireworks
url: https://fireworks.ai/blog/muonclip
author: null
published: '2025-07-15'
fetched: '2026-07-11T04:16:53Z'
classifier: codex
taxonomy_rev: 1
words: 890
content_sha256: 1865eef535091b462138e4e6a8a6e72b8bb63fe97b25b951f57379830d805554
triage: keep
skip_reason: null
---

# MuonClip and Kimi K2 training stability

Interactive visualization for MuonClip, brought to you from [Fireworks.ai](https://fireworks.ai/)

With the release of [Kimi-K2](https://fireworks.ai/models/fireworks/kimi-k2-instruct), a state of the art tool calling and instruction following model, Kimi team also talked about how they scaled up their pre-training, with a new optimizer, MuonClip. Honestly we don’t see new optimizers that often, so let’s dive into this a little more to understand how this helped the Kimi team scale their training. Specifically, this was the part of the blog [https://moonshotai.github.io/Kimi-K2/](https://moonshotai.github.io/Kimi-K2/) related to MuonClip.

So for people who are bad at math like me, what are they talking and how exactly does it solves their scaling problem.

Before we hit the problem, let's recall how attention works in transformers (the backbone of most LLMs like GPT or Llama). Attention lets the model "focus" on relevant parts of the input sequence. It does this by computing **query (Q)**, **key (K)**, and **value (V)** projections from the input embeddings.

The magic happens in the attention scores (often called "logits" in this context, but we'll call them "QK scores" to avoid confusion with output probabilities). These are dot products between queries and keys, scaled by the square root of the dimension for stability:

High scores mean the model pays more attention to that key when aggregating values. But if these scores blow up to extreme values during training, things go haywire—leading to NaNs, gradients vanishing or exploding, and your entire run crashing.

As you scale LLMs to billions of parameters and trillions of tokens (like Kimi K2's 15.5T-token pretraining), instabilities creep in. Moonshot AI noticed this especially when using the **Muon optimizer**—a high-efficiency alternative to the trusty AdamW that's great for speeding up training but a bit more aggressive.

If you are interested in learning more about Muon, you can read more about it [Kimi's paper around Muon](https://arxiv.org/pdf/2502.16982), and this blog [from Keller Jordan](https://kellerjordan.github.io/posts/muon/) around this topic.

Existing fixes for the QK score explosion problem? Things like **logit soft-capping** (clamping scores to a max value) or **query-key normalization** (normalizing Q and K vectors) sound promising, but Moonshot found them lacking. Soft-capping can distort the attention distribution unnaturally, while normalization might not address the root cause in the weights themselves.

Enter **MuonClip**, Moonshot's upgrade to Muon that tackles this head-on with a technique called **qk-clip**.

MuonClip keeps Muon's speed advantages but adds a post-update safety net. After each Muon step (which orthogonalizes updates for balance—more on that in a sec), qk-clip checks the potential QK scores. If the max score exceeds a threshold t (say, 1.0 in our demo), it rescales W_q and W_k directly:

- •Compute η = t / max_score (so η < 1 if clipping).
- •Scale W_q by η^α and W_k by η^(1-α), where α (around 0.5) balances the adjustment between query and key.

This bounds scores at t without messing with the update direction—it's like gently shrinking the weights to prevent overflow, right at the source. No distortion in the attention probs, just controlled scales.

Why does this work better? My guess is that it preserves Muon's efficient, balanced updates while ensuring stability for massive datasets. In Kimi K2's case, it enabled smooth training without the crashes that plagued plain Muon. Jianlin’s blog [https://kexue.fm/archives/11126](https://kexue.fm/archives/11126) has way more details here that would go into

To make this tangible, let's look at a simplified visualization. Imagine W_q and W_k as small matrices (e.g., 4x4, simulating a tiny attention head). We apply a Muon-like update (orthogonalizing for balance), then optionally clip.

Here's what happens simulating the “explosion” setup early on in training:

- •**Pre-Clip (Top Row)**: After the update, W_q might have large values, leading to spiky QK scores (dot products). The heatmap shows scores potentially exceeding t, risking explosion.
- •**Post-Clip (Bottom Row)**: qk-clip scales the matrices, capping the max score at t. Notice how the heatmaps use the same color scale—post-clip values are muted (closer to zero), but the relative patterns stay intact. Row norms (bar plots) shrink minimally, balanced by α.

Here is a visualization to help you understand the effect of clipping on the QK score after W_q (again, avoid the word logit so not to be confused with the final logit of the LLM output)

You can try out the interactive example here: [ https://muon-clip-app-644257448872.us-central1.run.app](https://muon-clip-app-644257448872.us-central1.run.app). This toy setup mimics real LLM behavior: Aggressive updates (high scale) cause "explosions," but clip reins them in. The value 100 here and 70k steps is not an accident, it is the setup that Jianlin shared about Kimi K2 training

We also simulate the max QK score later on during training at around 30 ish, where clipping is not active anymore, and you can see the weights are not changed.

Training instability isn't just an academic headache—it's lost GPU hours and delayed launches. Tools like MuonClip democratize big-model training, letting startups like Kimi punch above their weight. The full detail for the QK Clip is actually way more complicated than what I had here, and please check out this blog [https://kexue.fm/archives/11126](https://kexue.fm/archives/11126) if you want to dig into this rabbit hole, especially the comment section has a bunch of back and forth with Jianlin and other researchers; or checkout Jianlin Su’s Tweet here [https://x.com/Jianlin_S/status/1943920839487107372?t=1hmbwDoWTACe8AUY1ZSWWA&s=09](https://x.com/Jianlin_S/status/1943920839487107372?t=1hmbwDoWTACe8AUY1ZSWWA&s=09)

Here is the code for the visualization in case you are interested.

123456789101112131415161718192021222324252627282930313233343536373839404142434445464748495051525354555657585960616263646566676869707172737475767778798081828384858687888990919293949596979899100101102103104105106107108109110111112113114115116117118119120121122123124125126127128129130131132133134135136137138139140141142143144145146147

What do you think? Drop a comment on X/Twitter. If this sparked ideas, stay tuned for more content like this.
