---
title: GLM 5.2 with vision
kind: blog
topic: models
subtopic: multimodal
secondary_topics: []
summary: Post-trains vision onto GLM 5.2 by training only a 50M-parameter two-layer
  MLP projector reusing Kimi K2.6's vision tower, reaching Claude 4.5 Haiku-level
  MMMU-Pro (55%) via SFT then RL to restore reasoning.
triage: null
skip_reason: null
source: baseten
url: https://www.baseten.co/blog/glm-52-with-vision
author: Harry Partridge
published: '2026-07-21'
fetched: '2026-11-12T06:15:06Z'
classifier: claude
taxonomy_rev: 2
words: 731
content_sha256: 9f03bbe784cd7b040415bbd950021c30002591fadb477194e03c7aa5cbeca9b0
---

# GLM 5.2 with vision

AI models
# GLM 5.2 with vision

Is it possible to post-train vision onto GLM 5.2 without having any impact on its raw text-only capabilities?


- Authors
- Date
- July 21, 2026

TLDR

GLM 5.2 is one of the best currently available open source language models. However, unlike other flagship models like Qwen, Kimi and Minimax, GLM 5.2 does not support image inputs. We took this as a challenge: would it be possible to post-train vision onto GLM 5.2 without having any impact on its raw text-only capabilities? It turns out that the answer to this question is yes. Amazingly, by training only a tiny two-layer MLP with just 50M parameters, we are able to give GLM 5.2 vision capabilities equivalent to Claude 4.5 Haiku on MMMU-Pro (55%). Along the way, we witnessed an incredible level of generalization: GLM is even able to identify people who were never mentioned in our dataset!

Open source language models like Qwen, Kimi and Minimax process images using a module called a **vision tower**. The first thing to note about these vision towers is that they are typically very small in comparison to the main language model. For example, the Kimi K2.6's vision tower is only 466M parameters - just 0.04% of the total parameters in Kimi K2.6.

A typical vision tower has three key components: preprocessing, transformer encoder and projector. Preprocessing is typically a convolutional layer that process**es** the raw pixels in patches, producing a string of tokens which are then fed into the transformer encoder. This encoder typically uses full attention (no causal mask). The projector takes the outputs from the encoder, and maps them into the embedding space of the main language model.

Therefore, the aim with this project was to see if we could give GLM vision capabilities by starting with a publicly available vision tower, and training only the vision projector. We decided to start with the vision tower from Kimi K2.6 due to its strong performance on benchmarks and strong support in training and inference frameworks such as Megatron, vLLM, SGLang and TRT-LLM. In fact, Moonshot themselves used a very similar process when they were training Kimi k2.6: they used continual pre-training on SigLIP-SO-400M, which was a vision encoder trained by Google in 2023 ([https://arxiv.org/abs/2303.15343](https://arxiv.org/abs/2303.15343)).

We randomly initialize a projector to map from Kimi's vision encoder to GLM's embedding space. To begin with, we ran two epochs of SFT on 66k publicly available images paired with questions and answers. We used batch size 64 and a learning rate of 5e-4. Around 900 steps into this process (one epoch is 1035 steps), we observed a sharp drop in the loss, indicating that the vision projector had learned to align the vision features with GLM's latent space.

After we observed this grokking, we were interested in the extent to which the model would be able to recognize objects, images and people that did not appear in these 66k images that we used for alignment. Interestingly, we find that this effect is quite strong: the model is even able to name famous people that did not appear in the alignment dataset.

In order to induce grokking in SFT, we found it necessary to ensure that we only used simple question/answer pairs rather than long descriptions. Our hypothesis is that longer descriptions are 'off policy' for the language model and contribute high loss regardless of how well the vision features have been aligned. As such, our SFT dataset did not have any reasoning, so the model produced at the end of that phase is not able to reason with the images in context.

To restore GLM's reasoning capabilities and teach the model to reason about images, it was necessary to use reinforcement learning. Again, we were training **only** the vision projector for this whole process.

To begin with, GLM almost never produces any reasoning at all. Indeed, the first 4 batches of 512 examples contained exactly 0 reasoning. It was only on the 5th batch that the model produced a single reasoning trace. Amazingly, this **single** update was enough to nudge the model towards generating reasoning traces more often, and the reward curve was soon racing upwards towards 0.8.

If you are interested in using GLM 5.2 with vision, fill out the form below or download it for yourself here: [https://huggingface.co/baseten/GLM-5.2-Vision-NVFP4](https://huggingface.co/baseten/GLM-5.2-Vision-NVFP4)! We've open sourced it and hope you find value from it.
