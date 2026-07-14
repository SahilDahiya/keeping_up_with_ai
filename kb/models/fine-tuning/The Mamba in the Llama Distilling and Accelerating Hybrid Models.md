---
title: 'The Mamba in the Llama: Distilling and Accelerating Hybrid Models'
topic: models
subtopic: fine-tuning
secondary_topics: []
summary: Explains distilling and accelerating hybrid Mamba/Transformer models.
source: together
url: https://www.together.ai/blog/the-mamba-in-the-llama-distilling-and-accelerating-hybrid-models
author: Junxiong Wang; Daniele Paliotta; Avner May; Alexander M Rush; Tri Dao
published: '2024-09-09'
fetched: '2026-07-11T04:26:01Z'
classifier: codex
taxonomy_rev: 1
words: 1798
content_sha256: 94b69278b49c8e9c8b6c53251fa11ba42039a04a7b289ee7d8044c4e8d116d16
triage: keep
skip_reason: null
---

# The Mamba in the Llama: Distilling and Accelerating Hybrid Models

## Introduction


The evolution of large language models (LLMs) has been largely driven by the success of Transformer architectures. However, despite their impressive capabilities, Transformers suffer from significant inefficiencies, particularly in scenarios involving long sequences due to their quadratic complexity and heavy memory requirements. These challenges have spurred interest in exploring alternative architectures that can offer similar or even better performance with greater efficiency.

One such promising direction is the use of linear Recurrent Neural Networks (linear RNNs), specifically the Mamba and Mamba2 architecture. Mamba and its variants have demonstrated competitive performance to Transformers while offering significant advantages in inference speed. Mamba enjoys parallel training, as well as constant memory requirements during inference.

But can we bridge the gap between these architectures and harness the strengths of both? The answer lies in distilling large-scale Transformer models into hybrid linear RNNs and accelerating inference, combining the best of both worlds.

## From Transformer to Mamba


The self-attention mechanism is vital to transformers, enabling models to weigh the importance of different tokens in a sequence. However, this comes at the cost of computational and memory inefficiencies, particularly for long sequences. For example, during inference, transformers store the key and value vectors for every token they encounter in the KV-cache. For big models and long sequences, dealing with the KV-cache causes a big memory overhead. It slows inference down, and it occupied a lot of GPU memory.

In contrast, linear RNNs like Mamba enjoy linear-time scaling during training, and constant memory cost during inference as the entire state is summarized in a fixed size tensor. As a consequence, Mamba offers up to 5× higher throughput in inference tasks.

Therefore, it would make sense to take a pretrained transformer and distill its capabilities in a Mamba model, so as to explot the inference capabilities of linear RNNs while preserving the generation quality of transformer LLMs.

Despite their differences, a natural relationship exists between attention mechanisms in Transformers and the operations in linear RNNs. By linearizing the attention mechanism—essentially removing the softmax non-linearity—we can approximate the behavior of attention using linear RNNs. Therefore, we begin our distillation process by initializing the parameters in Mamba so as to mimic a linearized version of the transformer attention.

![](https://cdn.prod.website-files.com/69654e88dce9154b5f12070c/699e0b1ec4b14e2b4cb06c71_66d737d1ec01c690a9a52223_66d73711665af350bf120883_Mamba%252520-_%252520SSm%252520(1).png)

Linear RNNs take the following form

By linearizing transformer attention, we get

Thus the relationship:

We know have a clear relationship between the matrices of a Mamba block and those of a (linear) attention layer! This relationship, and the way we use it for distillation, is shown in Figure 1.

#### Distilling to an Expanded Linear RNN

**Initialization**The initialization procesdure is shown in Figure 2.

![](https://cdn.prod.website-files.com/69654e88dce9154b5f12070c/699e0b1ec4b14e2b4cb06c6b_66d737d0ec01c690a9a52203_66d7371fb4044f56c0477238_mamba%252520(3).png)

**Figure 2: **Transferring Transformer to Mamba. Weights, represented by layers, in the same color are initialized from the transformer (Linear projections for Q, K, and V are initialized using linear projection for C, B, and X respectively). We replace individual attention blocks with Mamba blocks, and then finetune Mamba blocks while freezing the MLP blocks. Shapes are kept mainly the same. New parameters are introduced for the learned A and ∆ parameters.

####

Distillation


The goal of our distillation is not to exactly replicate the performance of the original model but rather to provide a good starting point for the next distillation steps.

Figure 2 shows the resulting architecture. Our version directly replaces Transformer attention heads with fine-tuned linear RNN layers. During this phase, the Mamba layers are trained while the original Transformer's MLP layers are kept frozen to preserve their learned knowledge. This approach also requires processing additional components, such as grouped query attention that shares keys and values across heads. We note that this architecture differs from the architecture used in many Mamba systems, which combines MLP-SSM layers and uses a single head.

This initialization allows us to replace any attention block with a linear RNN block. We experiment with hybrid models where we keep every

𝑛 attention layers. Empirically, we found that replacing layers in a stepwise manner was the most effective strategy; i.e., we first keep every 2 layers, distill, then every 4, and continue distillation.

We use the pseudo-label distillation approach with the following loss functions.

**1. Word-level KL-Divergence:** The student model's probability distribution is trained to match the teacher model's distribution by minimizing KL divergence over all possible next tokens.**2. Sequence-level Knowledge Distillation (SeqKD): **This method involves replacing the ground truth text with the teacher's generated output, known as pseudo-labels.

The overall loss function for SFT combines sequence and word-level loss:

where 𝜃 represents the trainable parameters of the student model, and 𝛼 and 𝛽 control the weights of the sequence and word loss terms, respectively.

**Supervised Fine-Tuning (SFT)**Then, we perform supervised fine-tuning with the distilled hybrid model on datasets generated by GPT-4, such as OpenHermes 2.5, for one epoch.

**Direct Preference Optimization (DPO)**The third stage of instruction-tuning aligns the LLM with user preferences, aiming to maximize a reward model 𝑟 while staying close to a reference model, typically the supervised fine-tuned model. The optimization objective is:

Recent methods, such as Direct Preference Optimization (DPO), have proven effective for this purpose. If preferred (𝑦𝑤) and dispreferred (𝑦𝑙) outputs are available for a given prompt

𝑥, the optimization problem can be reformulated as:

This optimization is performed at the sequence level by scoring the preferred and dispreferred outputs of the model with the teacher and then backpropagating to the student. This work introduces DPO as a novel distillation objective at the sequence level.

## Speculative decoding for Mamba and Hybrid Models

![Flowchart of draft and verifier models with token generation, multistep decode, cache, and acceptance or rejection steps.](https://cdn.prod.website-files.com/69654e88dce9154b5f12070c/699e0b1ec4b14e2b4cb06c68_66d737d1ec01c690a9a52226_66d73796ed6ba1748d7ab55d_specdec%252520(1).png)

**Figure 3**: Multi-Step RNN Speculative Decoding. Left (top): The draft model generates the set of blue draft tokens sequentially. The draft tokens are then verified. Right (top): Verification uses the multistep kernel, without materializing the intermediate states. The last token is rejected and replaced with the true best token. Note, that even though more tokens are generated we cannot advance the hidden state cache. Left (bottom): The draft model can now generate more blue draft tokens from the current tokens, resulting in six total. Right (bottom): When the new draft is verified, the multi-step kernel returns both the hidden state after the yellow token and the final hidden state, since verification will fall between those positions.

One of the most significant challenges in deploying large language models (LLMs) like Transformers is their slow inference speed, particularly when generating long sequences. This limitation arises because these models generate text in an autoregressive manner—each token is generated sequentially, depending on the previous one. This inherently serial process becomes a bottleneck, preventing efficient utilization of computational resources.

To address this,** speculative decoding** has been introduced as a means to accelerate the inference process. Speculative decoding leverages the idea of using a smaller, faster draft model to predict several tokens ahead, which are then validated by a more accurate but slower verifier model.

**The Basics of Speculative Decoding**In speculative decoding, the process begins with a draft model that generates a sequence of candidate tokens (let's say 𝐾 tokens). This draft model is designed to be lightweight and fast, allowing it to produce these tokens quickly. However, because the draft model is not as accurate as the main model, these tokens need to be verified.

The verifier model, which is typically the main model or in our case a hybrid model checks, in parallel, the sequence of tokens generated by the draft model. If the tokens pass the verification check, they are accepted and included in the final output. If a token fails the verification, the process stops at that point, discards the remaining speculative tokens, and the main model takes over to generate the correct token.

This process then repeats, with the draft model generating another sequence of 𝐾 tokens from the new point, followed by verification. The key advantage here is that when speculations are correct, multiple tokens are generated and verified in a single step, significantly reducing the number of sequential operations required.

**Speculative decoding for Mamba and Hybrid Models**

While speculative decoding has been effectively used in Transformer models, applying it to Mamba and hybrid models presents unique challenges.

Attention-based models are particularly amenable to speculation, as they are slow at generation due to their sequential nature, but fast at verification due to their ability to check multiple tokens in parallel. Linear RNN models like Mamba have significantly different performance characteristics that make them less amenable to speculative decoding. Sequential decoding using recurrent-style sampling is already significantly faster than attention. Like attention, there are parallel modes for models like Mamba which are used at training.

These are efficient, but are tuned for extremely long sequences. In addition, they rely on hardware-aware optimizations, such as avoiding materializing intermediate states. These properties make it difficult to use for speculation for relatively short chains when it is unknown when a conflict will occur.

An additional challenge arises from caching states in RNN models. The state of an attention model is represented by the key-value cache, 𝐾1:𝑡, 𝑉1:𝑡; whereas the state of an RNN model is simply ℎ𝑡. To be competitive with attention this single RNN state needs to be very large. During speculation, we need to rewind to a previous state at time step 𝑡′. For attention, this is simply 𝐾1:𝑡′ , 𝑉1:𝑡′ ; however, for RNNs this would require caching all ℎ1:𝑡 which would require a large memory overhead.

We propose a new algorithm for linear RNN speculative decoding using hardware-aware multi-step generation. The core to the approach generation kernel that computes,

Where 𝑖 is the starting hidden state, 𝑖≤𝑗≤𝑘, and 𝑗…𝑘 is the range of y outputs needed. The kernel is hardware-aware because it avoids materializing key terms off of the fast GPU memory. Specifically, it avoids instantiating most h1:𝑛 as well as the discrete-time linear RNN parameters. This kernel is aimed to target the issues presented above.It can save a snapshot of the state h𝑗 before evaluating the draft tokens. This allows recomputing the correct state on the fly after a token is rejected. The assumption is that decoding is bottlenecked by memory and not by compute, as we can compute multiple steps of decoding with very little overhead over single-step decoding.

Figure 3 shows the algorithm. The approach maintains only one RNN hidden state in cache for verification and advances it lazily based on the success of the multi-step kernel. Since the distilled models contain transformer layers, we also extend speculative decoding to Attention/RNN hybrid architectures. In this setting, the RNN layers perform verification according to the aforementioned method, while the transformer layers simply perform parallel verification.

#### Experimental Results

**Distillation Experiments**

- Target Models: We conducted experiments using two LLM chat models: Zephyr-7B and Llama-3 Instruct 8B. Our goal is to distill transformer models into hybrid Ma
