---
title: 'Monarch Mixer: A new model architecture for increased efficiency'
topic: models
subtopic: reasoning
secondary_topics:
- inference/optimization
summary: Introduces Monarch Mixer as an efficient model architecture.
source: together
url: https://www.together.ai/blog/monarch-mixer
author: Dan Fu; Simran Arora; Chris Ré
published: '2023-07-25'
fetched: '2026-07-11T04:24:34Z'
classifier: codex
taxonomy_rev: 1
words: 1885
content_sha256: ed2c8897a66d85d9d1e794e2cc8a58895a41e444433978fc565eb3b1c2e333bd
triage: keep
skip_reason: null
---

# Monarch Mixer: A new model architecture for increased efficiency

![](https://cdn.prod.website-files.com/69654e88dce9154b5f12070c/699e0b11c5092d2627752e70_6547315a591eec2876101f73_653ba10aaa9d826f030b509d_653001bf820081815063941c_monarch-visual-final-share.png)

Transformers are the workhorse architecture behind modern foundation models. Our team at Together AI has released optimizations like [FlashAttention-2](https://together.ai/blog/tri-dao-flash-attention) to help further scale their capabilities. However, the computational requirements for Transformers increase quadratically with sequence length, which limits the extent of knowledge these models can capture from available datasets. We are interested in new, sub-quadratic approaches to increase scale and eventually produce models that learn from data more comprehensively.

**Today, in partnership with Hazy Research, we’re releasing a first look at Monarch Mixer—an exploration into an alternative, more efficient model architecture.**

Monarch Mixer (M2) is sub-quadratic in both sequence length and model dimension, enabling it to scale more efficiently while still matching quality. Our first target for M2 is BERT, the most popular model in use today for language tasks. M2-BERT is 25% more parameter-efficient than BERT and trains up to 3x faster.

This is just the beginning of research into Monarch Mixer models, and we are excited to share the results. You can access the first set of checkpoints at a standard sequence length today, and expect long-sequence BERT models to be coming soon!

Access M2-BERT [code on Github](https://github.com/HazyResearch/m2) and [80M](https://huggingface.co/danfu09/m2-bert-80M) and [110M](https://huggingface.co/danfu09/m2-bert-110M) checkpoints on Hugging Face.

Read more details in the full blog post on [Hazy Research](https://hazyresearch.stanford.edu/blog/2023-07-25-m2-bert) and below.

**Monarch Mixer: Revisiting BERT, Without Attention or MLPs**

Written by Dan Fu*, Simran Arora*, Chris Ré

Over the past six years, we’ve seen Transformers take the world by storm. Transformers have been the workhorse architecture behind modern foundation models and have seen impressive empirical success across diverse applications – from pretrained language models like [BERT](https://arxiv.org/abs/1810.04805), [ChatGPT](https://chat.openai.com/), and [Flan-T5](https://arxiv.org/abs/2210.11416), to image models like [SAM](https://arxiv.org/abs/2304.02643) and [stable diffusion](https://arxiv.org/abs/2112.10752). We think Transformers are great (and have had lots of fun [optimizing](https://arxiv.org/abs/2205.14135) [them](https://crfm.stanford.edu/2023/07/17/flash2.html)), but we’ve also been thinking about a deeper [question](https://hazyresearch.stanford.edu/blog/2023-03-23-ai-everywhere):

*Are Transformers the only way to get this amazing performance?*

Now, the first reason we’ve been poking around at this is because it’s really interesting! Diving into the inner workings of the architectures could help us understand what makes our current generation of models really tick and learn how to train or use them better. And we’ve been really excited by a lot of the work looking into new architectures, from [S4](https://arxiv.org/abs/2111.00396) to [BiGS](https://arxiv.org/abs/2212.10544), [Mega](https://arxiv.org/abs/2209.10655), [Liquid](https://arxiv.org/abs/2209.12951), and more. It’s great to live in a world where there are so many great ideas!

But we’re also interested in this question for some core efficiency reasons. Ideally, an alternative to Transformers would scale more efficiently while still matching in quality. One strong motivation for us has been scaling in sequence length – hence the line of work in our lab looking into replacing attention with a sub-quadratic operator (S4, [H3](https://arxiv.org/abs/2212.14052), [Hyena](https://arxiv.org/abs/2302.10866), [HyenaDNA](https://arxiv.org/abs/2306.15794)). And we’re encouraged by the groundswell of work into new architectures for long sequences, from [RetNet](https://arxiv.org/abs/2307.08621) to [RWKV](https://arxiv.org/abs/2305.13048), and [positional interpolation](https://arxiv.org/abs/2306.15595) – just to name a few!

MLPs – the other core building block of Transformers – also introduce an efficiency bottleneck, which becomes more acute as we continue to optimize attention. MLPs are quadratic in the model width, which means they grow more expensive as you make models wider. This is why models like GPT-3 are so expensive, and why GPT-4 has allegedly started using techniques like mixtures of experts.

*What if there were a model that were sub-quadratic along both sequence length and model dimension, and could match Transformers in quality?*


Today we’re excited to present a little teaser of some work in this direction – Monarch Mixer BERT (M2-BERT). M2-BERT is sub-quadratic in sequence length and model dimension, has 25% fewer parameters/FLOPs than BERT, and matches in quality (potentially exceeding a little bit when parameter-matched). We’re still very early days, so come talk to us if you find these questions exciting! And if you’re reading this the week of release, we’ll be at ICML – come find us in Hawaii, we’ll be putting up a poster at the [ES-FoMo](https://es-fomo.com/) workshop!

#### Monarch Mixer

Our basic idea is to replace the major elements of a Transformer with Monarch matrices — which are a class of structured matrices that generalize the FFT and are sub-quadratic, hardware-efficient, and expressive. A key property of Monarch matrices is that they can be computed using a series of block-diagonal matrices, interleaved with permutations:

![](https://cdn.prod.website-files.com/69654e88dce9154b5f12070c/699e0b11c5092d2627752e78_653001e3f71788cd9b9d99d1_M2%252B1.png)

In Monarch Mixer (M2), we use layers built up from Monarch matrices to do both mixing across the sequence (what attention does in Transformers) and mixing across the model dimension (what the MLP does in Transformers). This is similar in spirit to great work like [MLP Mixer](https://arxiv.org/abs/2105.01601) and [ConvMixer](https://arxiv.org/abs/2201.09792), which similarly replaced everything with a single primitive for vision tasks (but went for quadratic primitives).

Why go for a fully sub-quadratic architecture now? We’re continuing off a recent line of work in our lab ([and](https://arxiv.org/abs/2212.10544) [elsewhere](https://arxiv.org/abs/2206.13947)) that replaces attention with long convolutions – which is implemented efficiently with the FFT. Critically, Monarch matrices can implement the FFT – which gives us hope that a fully Monarch-based architecture can get there.

#### Revisiting BERT with Monarch Mixer

As a first proof-of-concept of our ideas, we’re going to roll the clock back to 2018, and look at one of the first big applications of pretrained Transformers – language modeling with BERT! Despite its (relative) age, BERT is still a workhorse model for applications such as text classification, retrieval, search, and more (see [this](https://sayanchak.medium.com/practical-uses-of-bert-c384ae3a5c2a) great summary – and this great [tweet](https://twitter.com/marktenenholtz/status/1682436003158433816) on why we love BERT).

For our model, we’ll replace the attention block with a layer inspired by previous work in attention-free models ([H3](https://arxiv.org/abs/2212.14052) & [Hyena](https://arxiv.org/abs/2302.10866)), and replace the fully-connected layers in the MLP with some simple block-diagonal matrices. All of these operations can be implemented with Monarchs, and the rest is standard stuff like element-wise multiplication, and simple pointwise operators.

Our sequence mixer block builds off H3 and Hyena. Our [previous](https://hazyresearch.stanford.edu/blog/2023-01-20-h3) [blogs](https://hazyresearch.stanford.edu/blog/2023-03-07-hyena) give some intuition about what the architecture is doing – in brief, the short convolutions allow the model to do a quick lookup of nearby tokens, while the long convolutions allow global information to pass over the sequence.

![Diagram of Sequence Mixer with convolutions and Dimension Mixer with GelU and GLU activations.](https://cdn.prod.website-files.com/69654e88dce9154b5f12070c/699e0b11c5092d2627752e6d_653001e3ee995a284fad3a3f_M2%252B2.png)

The deltas between our sequence mixer the original H3/Hyena layer are a bit interesting, so we’ll go over them briefly:

- **FFT -> Monarch:**in H3 and Hyena, the long convs are computed using the FFT, e.g. `iFFT(FFT(x) * FFT(k))`. In M2-BERT, we compute these FFTs with Monarchs!
- **Causal vs. bidirectional:**in H3 and Hyena, the long convs are causal (for the autoregressive language modeling loss). This is done by padding the inputs of the FFTs with zeros, since the FFT implements a- [circular](https://en.wikipedia.org/wiki/Convolution_theorem)convolution. In M2-BERT, we make the convolutions non-causal by making the convolution kernel twice the length of the input, which makes the weights wrap around.
- **Convolution kernel:**For the actual kernels k, we use a- [CKConv](https://arxiv.org/abs/2102.02611)parameterization with an exponential, similar to Hyena! In our bidirectional setup, this makes the convolution kernels focus on nearby tokens in the input.
- **Extra convolution connection:**for BERT, we found that adding an extra convolution (a “residual” so to speak) improved performance on synthetic tasks and pretraining loss.
- **Average pooling in fine-tuning:**BERT models are traditionally fine-tuned using the embedding of the CLS token. We find that taking the average pool of the embeddings in the input can work a bit better for M2-BERT on downstream tasks that require comparing information spread across multiple sentences such as GLUE NLI tasks (one intuition is that the convolutions spread the information across more tokens).

Lastly, the dimension mixer looks a lot like a normal MLP, but replaces the fully-connected layers with block-diagonal layers – which drastically reduces the parameters and makes the model more efficient!

So then the natural questions are – given the drastic parameter reduction, how does quality compare to a standard BERT model, and how much faster is it?

#### Quality on GLUE

So our first evaluation was pretraining some M2-BERT models and comparing their downstream GLUE scores after fine-tuning.

When we take our M2-BERT models with the same model width and depth as a standard BERT model, we get some pretty decent parameter savings – M2-BERT-base with 12 layers and model with 768 has 80M parameters, compared to a standard BERT-base of 110M parameters. We pretrained M2-BERT-base (80M) on 36.5B tokens of C4, at sequence length 128, as well as an M2-BERT parameter-matched to BERT-base.

Surprisingly, we can get pretty decent results, even with fewer parameters – M2-BERT-base (80M) matching the original BERT-base scores from Devlin 2018 BERT, and the parameter-matched M2-BERT-base sees further lift (see the end of the blog post for full numbers):

There’s still a lot we don’t know about these models, so quality could get even better. We mostly took standard Transformer BERT-base hyperparameters, besides some basic hyperparameter sweeps on fine-tuning. The Transformer hyperparameters have been optimized by the community in tons of ways over the past five years, so there’s a lot still to learn about what the best hyperparameters and training formulae are for M2 (e.g., we observed up to half-point swings in average GLUE score during our sweeps). And there’s been great work in the community about exactly how much gating you need for different tasks (e.g., [BiGS, section 7.2](https://arxiv.org/abs/2212.10544), so lots more to explore here).

#### Long sequence preview

So what does this new architecture buy us? One possibility is speed, and scaling to longer sequences. Since M2 is sub-quadratic in model dimension, we see a FLOP reduction (which is reflected in the lower parameter count). But the sequence mixer is also sub-quadratic in sequence length, which means the potential to scale to longer sequences.

We’ll be exploring long-sequence M2-BERT models more in-depth in the coming weeks, but for now here’s a simple preview of throughput at different sequence lengths, compared to the HuggingFace BERT-base and a more optimized FlashAttention BERT-base, for various sequence lengths. Here, we’re looking at throughput in terms of tokens/ms, on a single A100.

Today we’re releasing two initial M2-BERT checkpoints pretrained on short sequences, but M2-BERT has the potential to scale to much longer sequences. We’ve started using these scaling properties to experiment with data recipes for long-sequence M2-BERT’s – stay tuned!

#### What’s next

- We are releasing code for BERT and checkpoints for 80M and 110M models today, pretrained using a standard recipe at sequence length 128 – stay tuned for longer sequences! Check out our [code](https://github.com/HazyResearch/m2)and checkpoints ([80M](https://huggingface.co/danfu09/m2-bert-80M),[110M](https://huggingface.co/danfu09/m2-bert-110M)).
- In the coming weeks, watch out for further releases, as we train up long-sequence BERT’s and start tracing the history of Transformers forward – on ImageNet, causal language modeling, T5-style models, as well as explorations of the long sequence capabilities
- As part of this release, you’ll find some optimized CUDA code for the forward pass of the M2 layer (which we used for the benchmarks) – we’ll continue to optimize and release updates over the coming weeks. Expect another series of blogs and materials on these soon as we explore the computational tradeoff space!
- And of course, full arXiv coming soon!

#### Full GLUE numbers

#### Acknowledgements

This work would not have been possible without the full Monarch Mixer team!

Full author list: Daniel Y. Fu, Simran Arora*, Sabri Eyuboglu*, Jessica Grogan*, Isys Johnson*, Armin W. Thomas*, Benjamin Spector, Michael Poli, Atri Rudra, Christopher Ré
