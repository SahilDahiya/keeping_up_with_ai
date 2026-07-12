---
title: Linearizing LLMs with LoLCATs
topic: models
subtopic: reasoning
secondary_topics:
- inference/optimization
summary: Explains LoLCATs for linearizing LLM attention while preserving useful behavior.
source: together
url: https://www.together.ai/blog/linearizing-llms-with-lolcats
author: Michael Zhang; Simran Arora; Rahul Chalamala; Alan Wu; Benjamin Spector; Aaryan
  Singhal; Krithik Ramesh; Christopher Ré
published: '2024-10-14'
fetched: '2026-07-11T04:24:02Z'
classifier: codex
taxonomy_rev: 1
words: 2395
content_sha256: d0d19082c6370767235cd48e00cfffe74899c19d34fe640e7a7fbe1e3634039a
triage: keep
skip_reason: null
---

# Linearizing LLMs with LoLCATs

We're excited to introduce** LoLCATs **(**Lo**w-rank** L**inear **C**onversion via **A**ttention **T**ran**s**fer), a new approach for quickly creating subquadratic LLMs from existing Transformers. Beyond simply accelerating models, our focus is on creating fast models more efficiently, pushing the boundaries of AI development.

Rather than invent and pretrain new architectures from scratch, LoLCATs builds on a recent playbook [[1](https://arxiv.org/abs/2402.04347), [2](https://arxiv.org/abs/2405.06640), [3](https://arxiv.org/abs/2408.10189), [4](https://arxiv.org/abs/2408.15237)] that simply (1) *swaps out* softmax attentions for efficient alternatives (e.g., linear attentions), before (2) further training the model to recover from this layer swapping. This “’linearizing” lets us bring the joys of *linear-time* and *constant-memory* generation to powerful and popular open-source LLMs (cheaper test-time compute, more reasoning for all!). 

However, we developed LoLCATs to make linearizing even more painless and quality-preserving. As our own test, LoLCATs lets us create linear versions of the **complete Llama 3.1 family** (8B, 70B, and 405B) for the first time, doing so no less on the *same budget of a parameter-efficient finetune*. To do so, we found that we could do two simple things:

- **Make swapping more seamless**: replacing softmax attentions with linear attentions- *trained*to approximate their softmax counterparts (“attention transfer”).
- **Make recovery cheaper**: avoiding full model training after swapping, and recovering quality by only adjusting with parameter-efficient finetuning (e.g., low-rank adaptation).

![](https://cdn.prod.website-files.com/69654e88dce9154b5f12070c/699e09931542d62acea6717e_670d6250fc14a207c7bee35a_670d6122a237e6aebf4e400b_image4.png)

In this post, we’ll go over some highlights of the method and results of LoLCATs. We’re also sharing our paper, code, and reference checkpoints, so you can linearize your own LLMs too!

But as quick takeaways:

- **Achieve state-of-the-art linearized quality:**Improving the zero-shot accuracy of popular linearized 7B and 8B LLMs (Mistral 7B, Llama 3 8B) by 6.7 to 8.8 points on average over standard LM Eval zero-shot tasks and 20+ points on 5-shot MMLU. Excitingly, we also outperform strong subquadratic models pretrained from scratch (Mamba 7B, RWKV-6 World, TransNormer 7B, Hawk 7B, Griffin 7B, StripedHyena-7B) on popular zero-shot LM Eval tasks and 5-shot MMLU. Finally, we match the original Transformer-based LLMs on zero-shot tasks for the first time.

- **Drastically reduce linearizing costs:**Getting this quality by training only <0.2% of the parameters needed in prior linearizing methods, while using only 40 million training tokens (a 2,500x improvement in tokens-to-model efficiency versus linearizing methods; and a 35,000x improvement versus pre-training strong 7B subquadratic models like- [RWKV-v6](https://huggingface.co/BlinkDL/rwkv-6-world)and- [Mamba](https://huggingface.co/TRI-ML/mamba-7b-rw))

- **Scale up linearizing to 70B and 405B LLMs**: Using these advances to linearize the complete Llama 3.1 family (8B, 70B, and 405B) and create the first linearized 70B and 405B LLMs all on “academic compute” (linearizing Llama 3.1 405B with less GPU hours than concurrent methods used for 50x smaller 8B LLMs).

{{custom-cta-1}}

## What’s linearizing? And is linearizing all we need?

When we started working on LoLCATs, we really just wanted 7B+ LLMs with three things: competitive quality, subquadratic efficiency, and the ability for us to actually create them.

There’s been a ton of exciting recent work on high-quality and highly-efficient architectures, but we still don’t have ways to easily scale these up, especially to modern LLM regimes. Doing things the typical way—i.e., training new architectures from scratch—would mean training 7B+ parameters on trillions of tokens (so far, 1–15 trillion!). We didn’t have this compute budget lying around (remember, we’re fighting for one of [64 A100s](https://x.com/tsarnick/status/1789052769032138786)).

Alternatively, we could “linearize” (a.k.a., “linear conversion”) or [“continued pretraining”](https://arxiv.org/abs/2004.05150)). We’d start with existing pretrained Transformers, replace their self-attentions with efficient analogs (such as linear attentions), and continue training to adjust to the transplanted layers. In our own work, we started exploring linearizing LLMs in [Hedgehog](https://arxiv.org/abs/2402.04347), linearizing Llama 2 7B for a summarization task. Excitingly, folks at TRI later showed how to linearize Llama 2 7B and Mistral 7B to recover [zero-shot LM capabilities](https://arxiv.org/abs/2405.06640)! And our lab alums more recently shared similar work [[1](https://arxiv.org/abs/2408.10189), [2](https://arxiv.org/abs/2408.15237)] distilling 1.3B and 8B Transformer LLMs into their favorite Mamba architectures.

![](https://cdn.prod.website-files.com/69654e88dce9154b5f12070c/699e0b0d8c2458ebe0840595_670d624ffc14a207c7bee335_670d6050f4598a06e98d1fae_image3.png)

Unfortunately, linearizing was not all we needed just yet. The proposed ways to linearize LLMs were still too expensive and left quality on the table. All prior methods involved fully training 7B parameter LLMs on billions of tokens after swapping attentions. Their linearized models also underperformed the original Transformers by 1.7 to 8.0 points on popular LM Eval tasks (up to 28.2 points on MMLU!). Could we close this gap?

## LoLCATs: adding more L’s to get more W’s

Our main idea was to add three simple concepts to linearizing Transformers:

- Learnable (Linear) Attentions
- Low-rank Adaptation
- Layer-wise Optimization

**1. Learning (Linear) Attentions**. We first train sub-quadratic attentions to mimic and replace softmax attention. This “attention transfer” was inspired by our earlier [Hedgehog](https://arxiv.org/abs/2402.04347) work. There, instead of manually designing linear attention feature maps to be good softmax approximators, we just set them as learnable layers. Surprisingly(?), we found we could explicitly train these layers to learn whatever functions were important to produce good softmax attention approximations.

For LoLCATs, we made two simple improvements to linearize LLMs:

- While in Hedgehog we only used learnable linear attentions, with LoLCATs we generalized to learnable linear-attention-and-sliding-window hybrids. This was inspired by our earlier [Based](https://arxiv.org/abs/2402.18668)work, where some local softmax attention helped improve quality. But now we unify the linear and softmax attentions in a single fully subquadratic layer—and train these layers to approximate softmax attention as a whole. For an N-token sequence, the first W tokens get softmax attention, the remaining N-W get linear attention, and the values get combined as a learned weighted sum.

![](https://cdn.prod.website-files.com/69654e88dce9154b5f12070c/699e0b0d8c2458ebe084059f_670d6250fc14a207c7bee355_670d60c2ed58e830275e36d8_image7.png)

![](https://cdn.prod.website-files.com/69654e88dce9154b5f12070c/699e0b0c8c2458ebe084058e_670d6250fc14a207c7bee344_670d60d133912ee14df08c09_image10.png)

- While in Hedgehog we trained the feature maps to match on attention weights (via a KL divergence), we found we could also use an MSE loss on the outputs of attention layers. This gets around a limitation of Hedgehog where we needed to instantiate all N^2 attention weights as “targets” to supervise. Instead, we can now use [FlashAttention](https://github.com/Dao-AILab/flash-attention)to compute softmax attention outputs, and keep attention transfer in O(N) memory land.

![](https://cdn.prod.website-files.com/69654e88dce9154b5f12070c/699e0b0d8c2458ebe084059c_670d624ffc14a207c7bee338_670d60feed58e830275e66c7_image6.png)

*learn*how to approximate softmax with trainable linear attentions.

In all of the above, we create the linearized LLMs by simply inserting these feature maps into each existing attention. We *only* train these feature maps while freezing all other weights, amounting to training just 0.2% of a 7B LLM’s parameter counts.

![](https://cdn.prod.website-files.com/69654e88dce9154b5f12070c/699e09931542d62acea6717e_670d6250fc14a207c7bee35a_670d6122a237e6aebf4e400b_image4.png)

**2. Low-rank Adaptation. **With attention transfer, we could train linear attentions to approximate softmax attentions. However, we still needed to do a bit more finetuning to “reconnect the wires” and get a coherent model. Fortunately, with LoLCATs we could do so by simply applying low-rank adaptation (LoRA) to attention QKVO weights. Keeping all else frozen, we train LoRA weights so the LLM outputs minimize a next-token prediction loss over some natural language data. Then we’re done!

![](https://cdn.prod.website-files.com/69654e88dce9154b5f12070c/699e0b0d8c2458ebe08405a2_670d6250fc14a207c7bee347_670d6133080b23e26c23ffc6_image5.png)

While LoRA lets us linearize with much less memory (training ~0.1% of the parameters used in prior linearization methods), we also found attention transfer + LoRA let us linearize with many fewer tokens. Despite training on a small post-training dataset (50K Alpaca samples), the LoLCATs LLMs recovered 98+% of general pretrained performance on unrelated LM Eval tasks. This even outperforms prior methods that use 2500x the tokens from more “typical” pretraining datasets (e.g., [RefinedWeb](https://arxiv.org/abs/2306.01116)).

As to why this is possible, it’s still early days in our understanding. One hypothesis is that LoLCATs both preserves the “pretrained knowledge” of LLMs by keeping most of the weights frozen, and reduces the linearizing problem to a simpler task. Via attention transfer, we focus on recovering the “sequence-mixing” patterns in the original attentions, which might make parameter-efficient training on fewer tokens sufficient. Then via low-rank updates, we also guard against any deleterious updates to these pretrained weights, reducing the risk of losing LLM generalization by overfitting to the linearizing data itself.

**3. Layer-wise optimization.** Finally, to help scale up LoLCATs to 405B LLMs, we had to add a third “L”. While we could successfully linearize 7B+ and 70B LLMs by simply optimizing all layers jointly during attention transfer, this led to later layers having much higher attention MSEs than earlier ones. The larger MSEs escalated into a real problem for Llama 3.1 405B. 

![](https://cdn.prod.website-files.com/69654e88dce9154b5f12070c/699e0b0e8c2458ebe08405b9_670d6250fc14a207c7bee35d_670d616bb38fa21ebda53b48_image9.png)

To resolve this and improve layer-wise attention transfer, we used a finer-grained “block-by-block” (or cria-by-cria[ 1](https://www.merriam-webster.com/dictionary/cria)) training setup. We split Llama 405B into blocks of k layers and jointly trained the attentions only within each block. To train all blocks in parallel, with our linearizing data we simply precomputed LLM hidden states every k layers, giving us the inputs for each block.

We pick k to balance the speed of parallel training with the memory of precomputing and saving hidden states to disk. No fancy cost models here, but if we wanted to linearize with 50M tokens:

- At k = 1, we’d need 2 bytes x 126 layers x 50M tokens x 16384 hidden size = 200TB of disk space to store the hidden states!
- At k = 9, we cut this disk space down to just 22 TB, while still being able to train each 9-layer block on its own single GPU in parallel.

The latter sounded better to us. By splitting the 126 layers of Llama 3.1 405B into 14 9-layer blocks, we could parallelize attention transfer on 14 different GPUs. This took just 5 hours. Then we stitched them all together with LoRA to get the final model.

## Results

Armed with high-quality LLMs, high-efficiency subquadratic layers, and a highly efficient method to create subquadratic LLMs from these high-quality LLMs, we now see if LoLCATs can actually make high-quality subquadratic LLMs.

### Closing the linearizing quality gap

As a first test, we evaluated how LoLCATs compared to other linearizing methods at the popular 7B+ LLM scale. Across Mistral 7B v0.1 and Llama 3 8B LLMs, despite only training 0.2% of the model parameters on 40M tokens, LoLCATs closes >80% of the linearizing quality gap averaged across popular LM Evaluation Harness tasks. This outperforms concurrent methods needing 500 - 2500x the tokens. For the first time, LoLCATs further outperforms linearized hybrids with 50% of their layers being full softmax attention, while also closing the gap with the original 100% softmax attention Transformers on non-MMLU tasks.

**Pushing linearized LLMs into state-of-the-art territory**

Along the way, we also found that LoLCATs could create state-of-the-art subquadratic LLMs in general. By converting readily available Transformers like Llama 3 8B or Mistral 7B, we created subquadratic LLMs that outperformed strong pretrained 7B Transformer alternatives by 1.2 to 9.9 higher LM Eval points (averaged over tasks). Rather than pretrain on trillions of tokens, with LoLCATs we could create subquadratic LLMs with the same budget as a parameter-efficient finetune, on 40M tokens no less (a 7,500 to 35,500x boost in “tokens-to-model” efficiency).

### Drastically reducing linearizing costs

![](https://cdn.prod.website-files.com/69654e88dce9154b5f12070c/699e0b0e8c2458ebe08405b1_670d69e6904497ec5976cc38_670d68765717c9b1e2b875a2_image7.png)

As alluded to above, with LoLCATs we could create state-of-the-art subquadratic LLMs with a fraction of prior training costs. Linearizing 7B and 8B LLMs required training just 0.2% of their model parameter counts on 40M tokens, doable in ~5 hours on a single 40GB A100. In our paper, we found that finding close softmax attention approximators was crucial to this efficiency boost. Across various prior linear attentions, by first training to approximate softmax attentions via attention transfer, we could rapidly speed up recovering linearized language modeling quality. We also couldn’t just do attention transfer with our linear attentions. But fortunately only a few LoRA updates were all we needed to get the models talking!

![](https://cdn.prod.website-files.com/69654e88dce9154b5f12070c/699e0b0d8c2458ebe08405ab_670d69e6904497ec5976cc3b_670d688e89430a2396da3c0c_image12.png)

### Scaling up linearizing to 70B and 405B LLMs

![](https://cdn.prod.website-files.com/69654e88dce9154b5f12070c/699e0b0e8c2458ebe08405b6_670d69e6904497ec5976cc67_670d68a2df2f58af6fb77e2d_image15.png)

Finally, to really just see what these quality and training efficiency gains could do, we used LoLCATs to linearize the complete Llama 3.1 8B family. In the process, we created the first linearized 70B and 405B LLMs. Notably, linearizing Llama 3.1 70B took only 18 hours on a single 8x80GB H100. Linearizing Llama 3.1 405B still took fewer GPU hours than what [prior methods used](https://github.com/jxiw/MambaInLlama/blob/main/mamba_zephyr/README.md) for 8B LLMs. LoLCATs also offers significant progress in quality, to tackle these big LLMs with reasonable compute. Compared with following the prior approach of just swapping attentions before training, we were able to close >75% of the performance gap to original Transformers on tasks like 5-shot MMLU.


## What’s next?

In summary, we made LoLCATs, a new method for linearizing LLMs with state-of-the-art quality and orders of magnitude less compute. While we’re excited to share our progress so far, we’re also jazzed about the potential opportunities linearizing unlocks. Two such directions below.

### Unlocking new capabilities with cheaper test-time compute

![](https://cdn.prod.website-files.com/69654e88dce9154b5f12070c/699e0b0d8c2458ebe08405a8_670d69e6904497ec5976cc6a_670d69061c4eeb2ec6db88cb_image1.png)

We’re particularly excited about how linearizing LLMs lets us bring complexity-level improvements in efficiency—like *linear-time* and *constant-memory* generation—to readily-available and state-of-the-art LLMs. Our paper discusses this more, but by replacing each attention layer with a linear or recurrent alternative, we no longer need to deal with growing KV caches and their associated memory pains. Instead, we can dedicate that memory to more fun use cases, such as achieving higher throughput with larger batch sizes. Especially with recent attention on inference scaling laws—and improving answer quality by generating many responses in parallel [cite Monkeys]—we’re excited to further enable these ideas e.g., by now generating 2048 parallel responses at the prior cost of 32. By significantly bringing down the costs of test-time compute, could linearizing unlock further reasoning demonstrations and improve open-source model quality?

### Democratizing Subquadratic LLM Development

We’re also excited about how low-rank linearizing can scale up efficient architecture research. While we stuck to simple linear attentions with LoLCATs, a big motivator was the ability to allow anyone to scale up a subquadratic candidate into competitive 7B+ LLMs that are all the rage these days. We’ve been fortunate that our RWKV, Gated Linear Attention, and Mamba friends (among others!) continue to cook up many exciting architectural developments—often on academic compute no less! And so we’re excited to see how techniques like linearizing can help take their ideas to bigger and badder models. While the effects might not be the same as pretraining from scratch, it seems like a great opportunity to use the open-weight ecosystem available today as a research testbed. Can we open up new avenues of efficient architecture development?


For even more details, please check out our [paper](https://github.com/HazyResearch/lolcats/blob/main/lolcats_preprint_v0.pdf), along with the full [LoLCATs method repo](https://github.com/HazyResearch/lolcats) and some [sample checkpoints](https://huggingface.co/collections/hazyresearch/lolcats-670ca4341699355b61238c37). While we started with simple linear attentions, we hope that our findings + code can help you linearize your Llamas, Mistrals, Gemmas or whatevers into the architectures of your hearts’ desires. Linearized Llamas for all!

Our experts can work with you to linearize and deploy your models leveraging LoLCATs.
