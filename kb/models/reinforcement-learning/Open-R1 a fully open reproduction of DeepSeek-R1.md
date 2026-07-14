---
title: 'Open-R1: a fully open reproduction of DeepSeek-R1'
kind: blog
topic: models
subtopic: reinforcement-learning
secondary_topics: []
summary: 'Lays out the Open-R1 plan to fully reproduce DeepSeek-R1: distill reasoning
  traces from R1 to build an open SFT dataset, reimplement the pure-RL (GRPO) pipeline
  that produced R1-Zero without human supervision, and run the multi-stage RL+SFT
  recipe — naming the unknowns DeepSeek left out (data curation, hyperparameters,
  scaling trade-offs).'
triage: null
skip_reason: null
source: huggingface
url: https://huggingface.co/blog/open-r1
author: Elie Bakouch; Leandro von Werra; Lewis Tunstall
published: '2025-01-28'
fetched: '2026-07-14T22:11:26Z'
classifier: claude
taxonomy_rev: 1
words: 1727
content_sha256: f493912b0c50bc8b3e637c152325c89abaa14cfb87b461a16079e0e0374f83fc
---

# Open-R1: a fully open reproduction of DeepSeek-R1

Text Generation •  685B • Updated   •  8.89M  •  13.5k  

#### deepseek-ai/DeepSeek-R1

![](https://cdn-avatars.huggingface.co/v1/production/uploads/6538815d1bdb3c40db94fbfa/xMBly9PUMphrFVMxLX4kq.png) 

 Published
					January 28, 2025 

  Upvote 

 890

If you’ve ever struggled with a tough math problem, you know how useful it is to think a little longer and work through it carefully. [OpenAI’s o1 model](https://x.com/polynoamial/status/1834280155730043108) showed that when LLMs are trained to do the same—by using more compute during inference—they get significantly better at solving reasoning tasks like mathematics, coding, and logic.

However, the recipe behind OpenAI’s reasoning models has been a well kept secret. That is, until last week, when DeepSeek released their [DeepSeek-R1](https://huggingface.co/deepseek-ai/DeepSeek-R1) model and promptly broke the internet (and the [stock market!](https://x.com/KobeissiLetter/status/1883831022149927352)).

Besides performing as well or better than o1, the [DeepSeek-R1](https://huggingface.co/deepseek-ai/DeepSeek-R1) release was accompanied by a detailed [tech report](https://github.com/deepseek-ai/DeepSeek-R1/tree/main) that outlined the key steps of their training recipe. This recipe involved several innovations, most notably the application of pure reinforcement learning to teach a base language model how to reason without * any* human supervision. As shown in the figure below, making a powerful reasoning model is now very simple if you have access to a capable base model and a high-quality data mixture:

However, the DeepSeek-R1 release leaves open several questions about:

- **Data collection:**How were the reasoning-specific datasets curated?
- **Model training:**No training code was released by DeepSeek, so it is unknown which hyperparameters work best and how they differ across different model families and scales.
- **Scaling laws:**What are the compute and data trade-offs in training reasoning models?

These questions prompted us to launch the [Open-R1 project](https://github.com/huggingface/open-r1), an initiative to systematically reconstruct DeepSeek-R1’s data and training pipeline, validate its claims, and push the boundaries of open reasoning models. By building Open-R1, we aim to provide transparency on how reinforcement learning can enhance reasoning, share reproducible insights with the open-source community, and create a foundation for future models to leverage these techniques.

In this blog post we take a look at key ingredients behind DeepSeek-R1, which parts we plan to replicate, and how to contribute to the Open-R1 project.

Let’s dive in 🚀!

DeepSeek-R1 is a reasoning model built on the foundation of [DeepSeek-V3](https://huggingface.co/deepseek-ai/DeepSeek-V3-Base). Like any good reasoning model, it starts with a strong base model, and DeepSeek-V3 is exactly that. This 671B Mixture of Experts (MoE) model performs on par with heavyweights like Sonnet 3.5 and GPT-4o. What’s especially impressive is how cost-efficient it was to train—just $5.5M—thanks to architectural changes like Multi Token Prediction (MTP), Multi-Head Latent Attention (MLA) and a LOT (seriously, a lot) of hardware optimization.

DeepSeek also introduced two models: DeepSeek-R1-Zero and DeepSeek-R1, each with a distinct training approach. DeepSeek-R1-Zero skipped supervised fine-tuning altogether and relied entirely on reinforcement learning (RL), using Group Relative Policy Optimization (GRPO) to make the process more efficient. A simple reward system was used to guide the model, providing feedback based on the accuracy and structure of its answers. This approach helped the model develop useful reasoning skills, such as breaking problems into steps and verifying its own outputs. However, its responses often lacked clarity and were difficult to read.

That’s where DeepSeek-R1 comes in. It started with a "cold start" phase, fine-tuning on a small set of carefully crafted examples to improve clarity and readability. From there, it went through more RL and refinement steps, including rejecting low-quality outputs with both human preference based and verifiable reward, to create a model that not only reasons well but also produces polished and consistent answers.

This all sounds great, but what's actually missing? Let's have a look at the missing pieces of the puzzle.

The release of DeepSeek-R1 is an amazing boon for the community, but they didn’t release *everything—*although the model weights are open, the datasets and code used to train the model are not 😢.

The goal of *Open-R1* is to build these last missing pieces so that the whole research and industry community can build similar or better models using these recipes and datasets. And by doing this in the open, everybody in the community can contribute!

As shown in the figure below, here’s our plan of attack:

- **Step 1:**Replicate the R1-Distill models by distilling a high-quality reasoning dataset from DeepSeek-R1.
- **Step 2:**Replicate the pure RL pipeline that DeepSeek used to create R1-Zero. This will involve curating new, large-scale datasets for math, reasoning, and code.
- **Step 3:**Show we can go from base model → SFT → RL via multi-stage training.

Note that we don’t want to stop at math datasets. There’s a lot of potential in exploring other areas, obvious one like code but also scientific fields such as medicine, where reasoning models could have significant impact.

This initiative isn’t just about replicating results—it’s about sharing insights with the community. By documenting what works, what doesn’t, and why, we hope to save others from wasting time and compute on unproductive paths.

If this sounds interesting, we’d love your help! Whether it’s contributing [code](https://github.com/huggingface/open-r1/issues/23), joining discussions on [Hugging Face](https://huggingface.co/open-r1), there are plenty of ways to get involved. Let’s build this together! 🚀

 Text Generation •  685B • Updated   •  8.89M  •  13.5k 

  685B • Updated   •  22.8k  •  1.7k 

More Articles from our Blog

llmsreasoningresearch

 
- +3

 130

 February 4, 2025 llmnlpreasoning

  Hot
- +19

 782

 July 8, 2025 Where is the evaluation numbers? without it you can’t call it reproduction.

True, but it seems like there’s nothing to be evaluated as of right now. I assume the ultimate goal is to train a new reasoning model and then use the same evaluation metrics as o1 and the DeepSeek-R1.

•

 That's quite interesting,I was asking myself why the questions the author exposed here are not being asked by others ? I believe the work they have done is memorable but at the same time I wonder why they wouldn't put these missing  pieces on if they are supposed to be fully open.

Why even without reproduction and comprehension of the innovation they could affect so much the market in this way ?

Hi! This blog post is an introduction to the project, not a claim that we’ve reproduced R1 yet. We will totally share the missing piece when we have them, you can expect the models and datasets to be upload in this [Hugging Face org](https://huggingface.co/open-r1) and the code to be in this [GitHub repo](https://huggingface.co/(https:/github.com/huggingface/open-r1)

Interesting read, and it is good that we see more effort into this direction: more optimization and less brute force.

Also wonder what tool did the author use for creating step diagram.

Excalidraw 👀

I'm so glad that initiative like this already exist, I'm gonna try to contribute :)

looking forward to it! 🚀

So racist articel

WTF are your talking about?

•

 Awesome to have this open reproduction started!

For Step #1 check out [https://github.com/open-thoughts/open-thoughts](https://github.com/open-thoughts/open-thoughts)!

[https://x.com/ryanmart3n/status/1884284101265612856](https://x.com/ryanmart3n/status/1884284101265612856)

Let's do this thing!

It's really cool to see how the whole open source community comes together!

Does anyone know the actual training cost of r1? I can't find it in the paper or the announcement post. Is the 6M cost reported by media just the number taken from v3's training cost?

Ops...

Has anyone asked the DeepSeek team to publish their training data and code, or at least share them privately with an independent replication project like this? Have they rejected such a request?

A faithful replication depends on using the same dataset and hyperparameters. Otherwise, any major discrepancies with the published benchmarks would be hard to pin down—whether due to training data differences or the replication method itself.

Historically, they have never released code or datasets of their LLM training, so I wouldn't expect this time to be different. If they would release it that would be amazing of course!

In the meantime we have to make best guess estimates and see if we can get there ourselves.

You provide good replication process of Deepseek reasoning training. I will try something similar to it.

This is really good information, can we fine tune with specific use case when code is released ?

Yes of course!

Please consider removing biased, tainted or unaligned training data and make an effort to remove copyrighted works from the crawl from intake.  This will make the model more usable.  If you reused anthropic curation checks,  this might also help, remove obviouslybiased data will likely add a lot of value.  We don't want another tainted, unaligned open source model, right?  And no corporate would ever use deepseek or a model that reuses it, right?

We appreciate your work for the benefit of humanity,  we hope.

Miike C from NJ

So basically you're asking to replace existing censorship with another flavour of censorship?

Can't wait! Hopefully the model will be uncensored but whatever you can do is alright! Love seeing open source building itself up. I'm not smart enough to actually help but I can contribute moral support lol

Hello guys, I am even just trying to find code for DeepSeek-V2, in order to fully understand multi-head latent attention. You do not seem to have code in Hugging Face even for that. Or am I missing something? Don't see anything in src/transformers/models. MLA is not properly described in their paper, so it would be important to have code for this.

The code for the models are inside the model repositories, e.g. for V3: [https://huggingface.co/deepseek-ai/DeepSeek-V3/blob/main/modeling_deepseek.py](https://huggingface.co/deepseek-ai/DeepSeek-V3/blob/main/modeling_deepseek.py)

Is it possible to contribute to this project?

Yes, you can look at [https://huggingface.co/open-r1](https://huggingface.co/open-r1) and [https://github.com/huggingface/open-r1/discussions](https://github.com/huggingface/open-r1/discussions) :)

I wonder what data was used for the training of R1 and R1-zero. Is there any news on the possibly tos -breaking openAI API calls that were made this past autumn?

Let's build this together

This project inspires me. At the moment, I developed an enhanced transformer. The goal is to figure out an equivalent SFT component in deepseek. The theoretical part and numeric examples worked out fine. I am now implementing it in a small scale LLM. Hopefully we can see the benchmark results in a few weeks. Thanks for the inspiration.

Charles

releasing weights means open-binary ie freeware (as opposed to SAAS). but the actual blueprint/design of the network, defined in a HL language, is not provided, so it isn't even partially open (SOURCE).

Amazing work!

PS: Why don't OpenAI change its name since it guide AI industry into another directions?

If you need any help with Open-R1? Please let me know.

How's it going? I don't see more comment or updates here since Feb
