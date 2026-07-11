---
title: 'RWKV: Reinventing RNNs for the Transformer Era — with Eugene Cheah of UIlicious'
topic: models
subtopic: reasoning
secondary_topics:
- inference/optimization
summary: RWKV interview on reinventing RNNs for the Transformer era and efficient
  sequence modeling.
source: latent-space
url: https://www.latent.space/p/rwkv
author: Eugene Cheah
published: '2023-08-30'
fetched: '2026-07-11T05:22:29Z'
classifier: codex
taxonomy_rev: 1
words: 977
content_sha256: 0b0e093503e6d42b218ca6eb1088202b236a184eb5de7cd6df2c13b41d84842c
---

# RWKV: Reinventing RNNs for the Transformer Era — with Eugene Cheah of UIlicious

*The AI Engineer Summit Expo has been  announced, presented by AutoGPT (and future guest Toran Bruce-Richards!) Stay tuned for more updates on the Summit livestream and Latent Space University.*

*This post was on  HN for 10 hours.*

**What comes after the Transformer?** This is one of the [Top 10 Open Challenges in LLM Research](https://huyenchip.com/2023/08/16/llm-research-open-challenges.html) that has been the talk of the AI community this month. Jon Frankle ([friend of the show](https://www.latent.space/p/mosaic-mpt-7b)!) has an ongoing [bet](https://www.isattentionallyouneed.com/) with Sasha Rush on whether **Attention is All You Need**, and the most significant challenger to emerge this year has been [RWKV - Receptance Weighted Key Value models](https://huggingface.co/blog/rwkv), which revive the RNN[1](https://www.latent.space#footnote-1) for GPT-class LLMs, inspired by a 2021 paper on [Attention Free Transformers](https://arxiv.org/abs/2105.14103) from Apple (surprise!).

![](https://substackcdn.com/image/fetch/$s_!75qK!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F42c58619-46a2-4402-b5bb-258fd8458d14_667x742.png)

[from the RWKV docs](https://wiki.rwkv.com/)

What this means practically is that RWKV models tend to scale in all directions (both in training and inference) much better than Transformers-based open source models:

![](https://substackcdn.com/image/fetch/$s_!BJzC!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Febadfb46-25fb-4732-b04d-882e1ee82483_683x582.png)

[RWKV paper](https://arxiv.org/pdf/2305.13048.pdf)

While remaining competitive on standard reasoning benchmarks:

![](https://substackcdn.com/image/fetch/$s_!aPCt!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F665f5880-65b1-46a6-b38e-4550e8a47cec_1366x779.png)

swyx was recently in Singapore for meetings with [AI government and industry folks](https://aisingapore.org/)[2](https://www.latent.space#footnote-2), and grabbed 2 hours with RWKV committee member Eugene Cheah for a deep dive, the full recording of which is now up on [Latent Space TV](https://youtu.be/dvk6X5zeIfY):

Today we release both the 2hr video and an edited 1hr audio version, to cater to the different audiences and provide “ablation opportunities” on RWKV interest level.

## The Eleuther Mafia?

The RWKV project is notable not merely because of the credible challenge to the Transformers dominance. It is also a distributed, international, mostly uncredentialed community reminiscent of early 2020s Eleuther AI:

- Primarily Discord, pseudonymous, - [GPU-poor](https://www.semianalysis.com/p/google-gemini-eats-the-world-gemini)volunteer community somehow coordinating enough to train >10B, OPT/BLOOM-competitive models
- Being driven by the needs of its community, it is extremely polyglot (e.g. English, Chinese, Japanese, Arabic) not because it needs to beat some benchmarks, but because its users want it to be for their own needs.
- “Open Source” in both the good and the bad way - properly Apache 2.0 licensed ( - [not “open but restricted](https://www.alessiofanelli.com/blog/llama2-isnt-open-source)”), yet trained on data taken from commercially compromised sources like the Pile (where- [Shawn Presser’s Books3 dataset has been recently taken down](https://www.theatlantic.com/technology/archive/2023/08/books3-ai-meta-llama-pirated-books/675063/)) and Alpaca (taking from- [Steven Tey’s ShareGPT](https://lmsys.org/blog/2023-03-30-vicuna/)which is technically against OpenAI TOS)

The threadboi class has loved tracking the diffusion of Transformers paper authors out into the industry:

![Jeremy Howard on X: "Ouch. Google failed to keep a single one of the authors  of the Transformers paper." / X Jeremy Howard on X: "Ouch. Google failed to keep a single one of the authors  of the Transformers paper." / X](https://substackcdn.com/image/fetch/$s_!n4jV!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Faa66e2d1-328e-4013-8fc6-a43dd65d9cec_1364x856.jpeg)

[left Adept](https://www.theinformation.com/briefings/two-co-founders-of-adept-an-openai-rival-suddenly-left-to-start-another-company), and Jones

[finally left Google to join David Ha](https://twitter.com/YesThisIsLion/status/1692172541039939958)to work on “nature-inspired intelligence”

But perhaps the underdog version of this is tracking the emerging Eleuther AI mafia:

![](https://substackcdn.com/image/fetch/$s_!XESR!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F387d54b3-2b2d-4b57-8c06-87de8b9da89f_826x591.png)

[just to clarify - LAION isn't the creation of Emad Mostaque or Stability AI. Emad is/was a funder who showed up well after its inception… LAION was also partially born from _frustrations with_ Eleuther's TPU culture and inability to ship](https://news.ycombinator.com/item?id=37370188)”. Further corrections on

[the HN discussion](https://news.ycombinator.com/item?id=37381809)

It will be fascinating to see how both Eleuther and Eleuther alums fare as they build out the future of both LLMs and open source AI.

## Audio Version Timestamps

*assisted by  smol-podcaster. Different timestamps vs the 2hr YouTube*

- [00:05:35] Eugene's path into AI at UIlicious
- [00:07:33] Tokenizer penalty and data efficiency of Transformers
- [00:08:02] Using Salesforce CodeGen
- [00:10:17] The limitations of Transformers for handling large context sizes
- [00:13:17] RWKV compute costs compared to Transformers
- [00:16:06] How Eugene found RWKV early
- [00:18:52] RWKV's focus on supporting many languages, not just English
- [00:21:24] Using the RWKV model for fine-tuning for specific languages
- [00:24:45] What is RWKV?
- [00:33:46] Overview of the different RWKV models like World, Raven, Novel
- [00:41:34] Background of Blink, the creator of RWKV
- [00:49:55] The linear vs quadratic scaling of RWKV vs Transformers
- [00:53:29] RWKV matching Transformer performance on reasoning tasks
- [00:54:31] The community's lack of marketing for RWKV
- [00:57:00] The English-language bias in AI models
- [01:00:33] Plans to improve RWKV's memory and context handling
- [01:03:10] Advice for AI engineers wanting to get more technical knowledge

## Show Notes

Companies/Organizations:

- RWKV - - [HF blog](https://huggingface.co/blog/rwkv),- [paper](https://arxiv.org/abs/2305.13048),- [docs](https://wiki.rwkv.com/),- [GitHub](https://github.com/BlinkDL/RWKV-LM),- [Huggingface](https://huggingface.co/docs/transformers/model_doc/rwkv)
- [EleutherAI](https://www.eleuther.ai/)- Decentralized open source AI research group
- [Stability AI](https://stability.ai/)- Creators of Stable Diffusion
- [Conjecture](https://www.conjecture.dev/)- Spun off from EleutherAI

People:

- Eugene Chia - CTO of - [UIlicious](https://uilicious.com/), member of RWKV committee (- [GitHub](https://github.com/PicoCreator),- [Twitter](https://twitter.com/picocreator))
- [Blink/Bo Peng](https://github.com/BlinkDL)- Creator of RWKV architecture
- [Quentin Anthony](https://www.latent.space/p/transformers-math#details)- our Latent Space pod on Eleuther, coauthor on RWKV
- [Sharif Shameem](https://www.latent.space/p/sharif-shameem#details)- our Latent Space pod on being early to Stable Diffusion
- [Tri Dao](https://www.latent.space/p/flashattention#details)- our Latent Space pod on FlashAttention making Attention subquadratic
- [Linus Lee](https://www.latent.space/p/ai-interfaces-and-notion)- our Latent Space pod in NYC
- [Jonathan Frankle](https://www.latent.space/p/mosaic-mpt-7b)- our Latent Space pod about Transformers longevity
- [Chris Re](https://cs.stanford.edu/~chrismre/)- Genius at Stanford working on state-space models
- Andrej Karpathy - - [Zero to Hero](https://karpathy.ai/zero-to-hero.html)series
- Justine Tunney (" - [Justine.lol](https://justine.lol/)") -- [mmap trick](https://justine.lol/mmap/)

Models/Papers:

- [Retentive Network: A Successor to Transformer for Large Language Models](https://arxiv.org/pdf/2307.08621.pdf)
- [GPT-NeoX](https://github.com/EleutherAI/gpt-neox)- Open source replica of GPT-3 by EleutherAI
- [Monarch Mixer -](https://hazyresearch.stanford.edu/blog/2023-07-25-m2-bert)Revisiting BERT, Without Attention or MLPs

## Misc Notes

RWKV is not without known weaknesses - Transformers do well in reasoning because they are [expressive in the forward pass](https://twitter.com/karpathy/status/1593417989830848512?s=20), yet the RWKV docs already note that it is [sensitive to prompt formatting and poor at lookback tasks](https://wiki.rwkv.com/#tldr-vs-existing-transformer-models). We also asked pointed questions about RWKV’s challenges in the full podcast.

[1](https://www.latent.space#footnote-anchor-1)

The [Unreasonably Effective](https://karpathy.github.io/2015/05/21/rnn-effectiveness/) architecture strikes back!

[2](https://www.latent.space#footnote-anchor-2)

Let us know if a dedicated essay/podcast on AI industrial policy would be ideal, and who you’d like to hear on the topic. We don’t have policy experience, but as citizens of smaller countries we do care about offering any help we can.
