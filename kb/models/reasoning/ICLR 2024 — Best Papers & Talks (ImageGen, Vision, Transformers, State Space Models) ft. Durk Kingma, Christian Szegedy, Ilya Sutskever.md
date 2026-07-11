---
title: ICLR 2024 — Best Papers & Talks (ImageGen, Vision, Transformers, State Space
  Models) ft. Durk Kingma, Christian Szegedy, Ilya Sutskever
topic: models
subtopic: reasoning
secondary_topics:
- models/multimodal
summary: ICLR 2024 recap covering image generation, vision, Transformers, and state-space
  model research.
source: latent-space
url: https://www.latent.space/p/iclr-2024-recap
author: Latent Space
published: '2024-05-27'
fetched: '2026-07-11T05:20:48Z'
classifier: codex
taxonomy_rev: 1
words: 2355
content_sha256: 209f5f4c450ee16e3fef072173c17e1b020f5aa2649e492aaf8f611f6b668392
---

# ICLR 2024 — Best Papers & Talks (ImageGen, Vision, Transformers, State Space Models) ft. Durk Kingma, Christian Szegedy, Ilya Sutskever

*Speakers for *[AI Engineer World’s Fair](https://www.ai.engineer/worldsfair)* have been *[announced](https://x.com/swyx/status/1791578883625791785)*! See our *[Microsoft episode](https://www.latent.space/p/worlds-fair-2024#%C2%A7show-notes)* for more info and *[buy now](https://ti.to/software-3/ai-engineer-worlds-fair)* with code *`LATENTSPACE`[1](https://www.latent.space#footnote-1)* — we’ve been studying the best ML research conferences so we can make the best AI industry conf! *

![](https://substackcdn.com/image/fetch/$s_!-pYL!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F88b164f2-83eb-464d-8062-655926c5fd06_2700x1504.png)

*Note that this year there are 4 main tracks per day and dozens of workshops/expo sessions; the free livestream will air much less than half of the content this time.*

*Apply for free/discounted  Diversity Program and Scholarship tickets here. We hope to make this the definitive technical conference for ALL AI engineers.*

*UPDATE: This is a 2 part episode - see  Part 2 here.*

[ICLR 2024](https://iclr.cc/) took place from May 6-11 in Vienna, Austria.

Just like we did for our extremely popular [NeurIPS 2023](https://www.latent.space/p/neurips-2023-papers) coverage, we decided to pay the $900 ticket (thanks to all of you paying supporters!) and brave the 18 hour flight and 5 day grind to go on behalf of all of you. We now present the results of that work!

![](https://substackcdn.com/image/fetch/$s_!oPN-!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fce0edfca-005c-4c2a-bb61-be54bb25be40_2568x1364.png)

This ICLR was the biggest one by far, with a marked change in the excitement trajectory for the conference:

![](https://substackcdn.com/image/fetch/$s_!r9Xf!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa63c8a75-683b-42b6-b288-a628d64e5c76_1102x704.png)

Of the 2260 accepted papers (31% acceptance rate), of the subset of those relevant to our [shortlist of AI Engineering Topics](https://www.latent.space/about), we found many, many LLM reasoning and agent related papers, which we will cover in the next episode. We will spend this episode with 14 papers covering other relevant ICLR topics, as below.

As we did last year, we’ll start with the [Best Paper Awards](https://blog.iclr.cc/2024/05/06/iclr-2024-outstanding-paper-awards/). Unlike last year, we now group our paper selections by subjective topic area, and mix in both Outstanding Paper talks as well as editorially selected poster sessions. Where we were able to do a poster session interview, please scroll to the relevant show notes for images of their poster for discussion. To cap things off, Chris Ré’s spot from last year now goes to Sasha Rush for the obligatory last word on the development and applications of State Space Models.

We had a blast at ICLR 2024 and you can bet that we’ll be back in 2025 🇸🇬.

## Timestamps and Overview of Papers

**[00:02:49] Section A: ImageGen, Compression, Adversarial Attacks**

- [00:02:49] VAEs
- [00:32:36] Würstchen: An Efficient Architecture for Large-Scale Text-to-Image Diffusion Models
- [00:37:25] The Hidden Language Of Diffusion Models
- [00:48:40] Ilya on Compression
- [01:01:45] Christian Szegedy on Compression
- [01:07:34] Intriguing properties of neural networks

**[01:26:07] Section B: Vision Learning and Weak Supervision**

- [01:26:45] Vision Transformers Need Registers
- [01:38:27] Think before you speak: Training Language Models With Pause Tokens
- [01:47:06] Towards a statistical theory of data selection under weak supervision
- [02:00:32] Is ImageNet worth 1 video?

**[02:06:32] Section C: Extending Transformers and Attention**

- [02:06:49] LongLoRA: Efficient Fine-tuning of Long-Context Large Language Models
- [02:15:12] YaRN: Efficient Context Window Extension of Large Language Models
- [02:32:02] Model Tells You What to Discard: Adaptive KV Cache Compression for LLMs
- [02:44:57] ZeRO++: Extremely Efficient Collective Communication for Giant Model Training

**[02:54:26] Section D: State Space Models vs Transformers**

- [03:31:15] Never Train from Scratch: Fair Comparison of Long-Sequence Models Requires Data-Driven Priors
- [03:37:08] End of Part 1

## A: ImageGen, Compression, Adversarial Attacks

- [Durk Kingma](https://x.com/dpkingma?lang=en)(OpenAI/Google DeepMind) & Max Welling- [Auto-Encoding Variational Bayes](https://arxiv.org/abs/1312.6114)(- [Full ICLR talk](https://iclr.cc/virtual/2024/test-of-time/21444))- Preliminary resources: - [Understanding VAEs](https://www.youtube.com/watch?v=HBYQvKlaE0A),- [CodeEmporium](https://www.youtube.com/watch?v=fcvYpzHmhvA),- [Arxiv Insights](https://www.youtube.com/watch?v=9zKuYvjFFS8)
- [Inaugural ICLR Test of Time Award](https://blog.iclr.cc/2024/05/07/iclr-2024-test-of-time-award/)!- **the integration of deep learning with scalable probabilistic inference**(amortized mean-field variational inference via a so-called- **reparameterization trick**), giving rise to the- **Variational Autoencoder (VAE)**.”

- [Pablo Pernías](https://x.com/pabloppp?lang=en)(Stability) et al- [Würstchen](https://arxiv.org/abs/2306.00637)- [: An Efficient Architecture for Large-Scale Text-to-Image Diffusion Models](https://arxiv.org/abs/2306.00637)(- [ICLR oral](https://iclr.cc/virtual/2024/oral/19738),- [poster](https://iclr.cc/media/PosterPDFs/ICLR%202024/18142.png?t=1715084847.6410706))![](https://substackcdn.com/image/fetch/$s_!tx9t!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F48cd3b10-4a3f-48dd-9808-6d51c9f4a3ca_2348x1666.png)
- [Hila Chefer](https://twitter.com/hila_chefer)et al (Google Research):- [Hidden Language Of Diffusion Models](https://arxiv.org/abs/2306.00966)(- [poster](https://iclr.cc/media/PosterPDFs/ICLR%202024/18349.png?t=1714768829.9829562))

![](https://substackcdn.com/image/fetch/$s_!OY6K!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F80ef97f0-6c17-4555-a1bb-9d0facdbf4fc_2900x1608.png)

- See also: - [Google Lumiere](https://arxiv.org/abs/2401.12945),- [Attend and Excite](https://arxiv.org/abs/2301.13826)![](https://substackcdn.com/image/fetch/$s_!NFw3!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F22a3d4c5-0a8a-4d94-b981-c9a83b6d83ab_2214x1510.png)
- [Christian Szegedy](https://x.com/ChrSzegedy)(X.ai):- [Intriguing properties of neural networks](https://arxiv.org/abs/1312.6199)(- [Full ICLR talk](https://iclr.cc/virtual/2024/test-of-time/23478))- [Inaugural Test of Time Award runner up](https://blog.iclr.cc/2024/05/07/iclr-2024-test-of-time-award/):- **neural networks can be vulnerable to small almost imperceptible variations to the input**. This idea helped spawn the area of adversarial attacks (trying to fool a neural network) as well as adversarial defense (training a neural network to not be fooled). “
- with - **Wojciech Zaremba, Ilya Sutskever, Joan Bruna, Dumitru Erhan, Ian Goodfellow, Rob Fergus**


## B: Vision Learning and Weak Supervision

- [Timothée Darcet](https://x.com/timdarcet)(Meta)- [Vision Transformers Need Registers](https://arxiv.org/abs/2309.16588)- [ICLR oral](https://iclr.cc/virtual/2024/session/15077),- [Paper](https://arxiv.org/abs/2309.16588))- [ICLR Outstanding Paper Award](https://blog.iclr.cc/2024/05/06/iclr-2024-outstanding-paper-awards/): “This paper identifies- **artifacts in feature maps of vision transformer networks, characterized by high-norm tokens in low-informative background areas**. The authors provide key hypotheses for why this is happening and provide a simple yet elegant solution to address these artifacts using- **additional register tokens, enhancing model performance on various tasks**. The insights gained from this work can also impact other application areas. The paper is very well-written and provides a great example of conducting research – identifying an issue, understanding why it is happening, and then providing a solution.“![](https://substackcdn.com/image/fetch/$s_!0IG4!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F3ec95ee9-4a70-4e1f-b1de-30852fac9870_2598x1426.png)
- [HN discussion](https://news.ycombinator.com/item?id=40329675): “According to the paper, the "registers" are- **additional learnable tokens**that are appended to the input sequence of a Vision Transformer model during training. They are added after the patch embedding layer, with a learnable value, similar to the [CLS] token and then at the end of the Vision Transformer, the register tokens are discarded, and only the [CLS] token and patch tokens are used as image representations.- **The register tokens provide a place for the model to store, process and retrieve global information during the forward pass, without repurposing patch tokens for this role.**- Adding register tokens removes the artifacts and high-norm "outlier" tokens that otherwise appear in the feature maps of trained Vision Transformer models. Using register tokens leads to smoother feature maps, improved performance on dense prediction tasks, and enables better unsupervised object discovery compared to the same models trained without the additional register tokens. This is a neat result. - **For just a 2% increase in inference cost, you can significantly improve ViT model performance**. Close to a free lunch.”

- [Sachin Goyal](https://x.com/goyalsachin007/status/1788307730962190676)(Google) et al:- [Think before you speak: Training Language Models With Pause Tokens](https://arxiv.org/abs/2310.02226)(- [OpenReview](https://openreview.net/forum?id=ph04CRkPdC))- We operationalize this idea by performing training and inference on language models with - **a (learnable) pause token,**a sequence of which is appended to the input prefix. We then delay extracting the model's outputs until the last pause token is seen, thereby allowing the model to process extra computation before committing to an answer. We empirically evaluate pause-training on decoder-only models of 1B and 130M parameters with causal pretraining on C4, and on downstream tasks covering reasoning, question-answering, general understanding and fact recall.
- Our main finding is that inference-time delays show gains when the model is both pre-trained and finetuned with delays. - **For the 1B model, we witness gains on 8 of 9 tasks, most prominently, a gain of 18% EM score on the QA task of SQuAD, 8% on CommonSenseQA and 1% accuracy on the reasoning task of GSM8k**. Our work raises a range of conceptual and practical future research questions on making delayed next-token prediction a widely applicable new paradigm.![](https://substackcdn.com/image/fetch/$s_!TqxG!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd5745004-297d-4d43-836d-29b5b239d0c8_1190x834.png) ![](https://substackcdn.com/image/fetch/$s_!usuB!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F8fc57327-c047-4e8e-8403-3a16377d8b9e_1132x726.png) ![](https://substackcdn.com/image/fetch/$s_!bK1O!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F11ff997a-283b-4ef4-9c2d-45bee9764b2c_1126x628.png)

- [Pulkit Tandon](http://x.com/tandon_pulkit)(Granica) et al- [ICLR Oral](https://iclr.cc/virtual/2024/session/15094),- [Poster](https://iclr.cc/media/PosterPDFs/ICLR%202024/18980.png?t=1714635656.0921783),- [Paper](https://arxiv.org/abs/2309.14563))- **Honorable Mention:**“The paper establishes- **statistical foundations for data subset selection**and identifies the shortcomings of popular data selection methods.”![](https://substackcdn.com/image/fetch/$s_!NpT7!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F1ac0f4b2-8eb0-46ac-ba82-cef849b105ec_2784x1668.png)

- [Shashank Venkataramanan](https://twitter.com/shawshank_v/status/1731296704941457636)(Inria) et al- [ICLR Oral](https://iclr.cc/virtual/2024/oral/19752),- [paper](https://shashankvkt.github.io/dora))![](https://substackcdn.com/image/fetch/$s_!n-zB!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff0763a36-808a-4d1f-a14e-5c4cd6ba26a4_2930x1466.png) - *First, we investigate first-person videos and*- **introduce a "Walking Tours" dataset**. These videos are high-resolution, hours-long, captured in a single uninterrupted take, depicting a large number of objects and actions with natural scene transitions. They are unlabeled and uncurated, thus realistic for self-supervision and comparable with human learning.
- *Second, we introduce a novel self-supervised image pretraining method tailored for learning from continuous videos. Existing methods typically adapt image-based pretraining approaches to incorporate more frames. Instead, we advocate a "tracking to learn to recognize" approach. Our method called*- **DoRA leads to attention maps that DiscOver and tRAck objects over time in an end-to-end manner, using transformer cross-attention**. We derive multiple views from the tracks and use them in a classical self-supervised distillation loss. Using our novel approach,- **a single Walking Tours video remarkably becomes a strong competitor to ImageNet for several image and video downstream tasks.**
- [Honorable Mention](https://blog.iclr.cc/2024/05/06/iclr-2024-outstanding-paper-awards/): “The paper proposes a novel path to- **self-supervised image pre-training, by learning from continuous videos**. The paper contributes both new types of data and a method to learn from novel data.“


## C: Extending Transformers and Attention

- [Yukang Chen](https://x.com/zhijianliu_/status/1705230996155580474)(CUHK)- [ICLR Oral](https://iclr.cc/virtual/2024/session/15074),- [Poster](https://iclr.cc/media/PosterPDFs/ICLR%202024/19390.png?t=1714595034.9664378))- We present - **LongLoRA**, an efficient fine-tuning approach that extends the context sizes of pre-trained large language models (LLMs), with limited computation cost. LongLoRA extends- **Llama2 7B from 4k context to 100k**, or- **Llama2 70B to 32k on a single 8x A100 machine**. LongLoRA extends models' context while retaining their original architectures, and is compatible with most existing techniques, like Flash-Attention2.
 ![](https://substackcdn.com/image/fetch/$s_!RZh-!,w_2400,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4a523b6e-f290-4273-8fd5-1ba74709e56e_2910x1442.png)
- [Bowen Peng](https://x.com/theemozilla/status/1748049343360155811)(Nous Research) et al- [Poster](https://iclr.cc/media/iclr-2024/Slides/17499.pdf),- [Paper](https://arxiv.org/abs/2309.00071))![](https://substackcdn.com/image/fetch/$s_!DW6u!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F164fee80-9e1f-4651-96fb-5dc01dc3bf07_2234x1546.png) - Rotary Position Embeddings (RoPE) have been shown to effectively encode positional information in transformer-based language models. However, these models fail to generalize past the sequence length they were trained on. We present - **YaRN (Yet another RoPE extensioN method)**, a compute-efficient method to extend the context window of such models,- **requiring 10x less tokens and 2.5x less training steps**than previous methods. Using YaRN, we show that LLaMA models can effectively- **utilize and extrapolate to context lengths much longer than their original pre-training would allow**, while also surpassing previous the state-of-the-art at context window extension. In addition, we demonstrate that YaRN exhibits the capability to extrapolate beyond the limited context of a fine-tuning dataset. The models fine-tuned using YaRN has been made available and reproduced online- **up to 128k context length.**
- Mentioned papers: - [Kaikoendev on TILs While Training SuperHOT](https://kaiokendev.github.io/til),- [LongRoPE](https://arxiv.org/abs/2402.13753),- [Ring Attention](https://arxiv.org/abs/2310.01889),- [InfiniAttention](https://arxiv.org/abs/2404.07143),- [Textbooks are all you need](https://arxiv.org/abs/2306.11644)and the Synthetic Data problem![](https://substackcdn.com/image/fetch/$s_!MR9T!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F40376806-c9a4-4c8b-86d1-334790f1a2aa_1850x1464.png)

- [Suyu Ge](https://x.com/ge_suyu)et al- [ICLR Oral](https://iclr.cc/virtual/2024/oral/19790),- [Poster](https://iclr.cc/media/PosterPDFs/ICLR%202024/19390.png?t=1714595034.9664378), Paper)- “We introduce - **adaptive KV cache compression**, a plug-and-play method that reduces the memory footprint of generative inference for Large Language Models (LLMs). Different from the conventional KV cache that retains key and value vectors for all context tokens, we conduct- **targeted profiling to discern the intrinsic structure of attention modules**. Based on the recognized structure, we then construct the KV cache in an adaptive manner:- **evicting long-range contexts**on attention heads emphasizing local contexts,- **discarding non-special tokens**on attention heads centered on special tokens, and only employing the standard KV cache for attention heads that broadly attend to all tokens. In our experiments across various asks,- **FastGen demonstrates substantial reduction on GPU memory consumption with negligible generation quality loss**. ”
- 40% memory reduction for Llama 67b
- [Honorable Mention](https://blog.iclr.cc/2024/05/06/iclr-2024-outstanding-paper-awards/)- **critical KV cache compression problem**with great impact on transformer based LLMs,- **reducing the memory with a simple idea that can be deployed without resource intensive fine-tuning or re-training**. The approach is quite simple and yet is shown to be quite effective.”
 ![](https://substackcdn.com/image/fetch/$s_!GIvQ!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F2e9e0e82-88d9-4a7e-90a6-1f19caf5de55_1174x1664.png)
- [Guanhua Wang](https://x.com/Guanhua_Wang_/status/1671953889485283329)(DeepSpeed) et al- [paper](https://arxiv.org/abs/2306.10209),- [poster](https://iclr.cc/media/PosterPDFs/ICLR%202024/18124.png?t=1712955550.117912),- [blogpost](https://www.microsoft.com/en-us/research/blog/deepspeed-zero-a-leap-in-speed-for-llm-and-chat-model-training-with-4x-less-communication/))- [Zero Redundancy Optimizer (ZeRO)](https://arxiv.org/abs/1910.02054)has been used to train a wide range of large language models on massive GPUs clusters due to its ease of use, efficiency, and good scalability. However, when training on low-bandwidth clusters, or at scale which forces batch size per GPU to be small, ZeRO's effective throughput is limited because of high communication volume from gathering weights in forward pass, backward pass, and averaging gradients. This paper introduces- **three communication volume reduction techniques**, which we collectively refer to as ZeRO++, targeting each of the communication collectives in ZeRO.
- Collectively, ZeRO++ reduces communication volume of ZeRO by 4x, enabling up to 2.16x better throughput at 384 GPU scale. ![](https://substackcdn.com/image/fetch/$s_!5MEa!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa07acb59-f970-4da3-8ced-8572bb111b7f_2478x1656.png)

- Mentioned: - [FSDP + QLoRA](https://github.com/AnswerDotAI/fsdp_qlora)

## Poster Session Picks


We ran out of airtime to include these in the podcast, but we recorded interviews with some of these authors and could share audio on request.

- Summarization
- Uncertainty - [Can LLMs Express Their Uncertainty? An Empirical Evaluation of Confidence Elicitation in LLMs](https://arxiv.org/abs/2306.13063)![](https://substackcdn.com/image/fetch/$s_!3mn0!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4f7a3c00-faa4-4bd6-906e-731744dedc22_1056x754.png)
- [MARS: Meaning-Aware Response Scoring for Uncertainty Estimation in Generative LLMs](https://iclr.cc/virtual/2024/workshop/20577)

- Tabular Data - [CABINET: Content Relevance-based Noise Reduction for Table Question Answering](https://arxiv.org/abs/2402.01155)![](https://substackcdn.com/image/fetch/$s_!_I3x!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F25b8c4d1-75b9-4bca-a50f-264128322186_1040x599.png)
- [Mixed-Type Tabular Data Synthesis with Score-based Diffusion in Latent Space](https://iclr.cc/virtual/2024/oral/19792)
- [Making Pre-trained Language Models Great on Tabular Prediction](https://iclr.cc/virtual/2024/poster/18356)
- [How Realistic Is Your Synthetic Data? Constraining Deep Generative Models for Tabular Data](https://iclr.cc/virtual/2024/poster/17622)

- Watermarking (there were >24 papers on watermarking, both for and against!!)
- Misc - [Massively Scalable Inverse Reinforcement Learning in Google Maps](https://iclr.cc/virtual/2024/poster/17395)
- [Zipformer: A faster and better encoder for automatic speech recognition](https://iclr.cc/virtual/2024/oral/19784)
![](https://substackcdn.com/image/fetch/$s_!0ZGD!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F225fa610-6bfb-45eb-8f97-1c2bcc74cc9c_1102x739.png)


## D: State Space Models vs Transformers

- [Sasha Rush’s](https://twitter.com/srush_nlp)- [ICLR invited talk](https://iclr.cc/virtual/2024/workshop/20589)on workshop day![](https://substackcdn.com/image/fetch/$s_!ELwW!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F66a56faf-c648-4cda-8788-42367f94378a_1928x1110.png)
- [Ido Amos](https://x.com/AmosaurusRex/status/1732010400340758708)(IBM) et al- [ICLR Oral](https://iclr.cc/virtual/2024/oral/19761))- Modeling long-range dependencies across sequences is a longstanding goal in machine learning and has led to architectures, such as state space models, that dramatically outperform Transformers on long sequences.
- However, these impressive empirical gains have been by and large demonstrated on benchmarks (e.g. Long Range Arena), where models are randomly initialized and trained to predict a target label from an input sequence. In this work, we show that - **random initialization leads to gross overestimation of the differences between architectures**.
- In stark contrast to prior works, we find - **vanilla Transformers to match the performance of S4 on Long Range Arena when properly pretrained**, and we improve the best reported results of SSMs on the PathX-256 task by 20 absolute points.
- Subsequently, we analyze the utility of previously-proposed structured parameterizations for SSMs and show they become mostly redundant in the presence of data-driven initialization obtained through pretraining. Our work shows that, when evaluating different architectures on supervised tasks, incorporation of data-driven priors via pretraining is essential for reliable performance estimation, and can be done efficiently.
- [Outstanding Paper Award](https://blog.iclr.cc/2024/05/06/iclr-2024-outstanding-paper-awards/): “This paper dives deep into understanding the ability of recently proposed state-space models and transformer architectures to model long-term sequential dependencies. Surprisingly, the authors find that- **training transformer models from scratch leads to an under-estimation of their performance**and demonstrates dramatic gains can be achieved with a pre-training and fine-tuning setup. The paper is exceptionally well executed and exemplary in its focus on simplicity and systematic insights.”


[1](https://www.latent.space#footnote-anchor-1)

If you need a bigger discount to make it work - use coupon `AINEWS.`
