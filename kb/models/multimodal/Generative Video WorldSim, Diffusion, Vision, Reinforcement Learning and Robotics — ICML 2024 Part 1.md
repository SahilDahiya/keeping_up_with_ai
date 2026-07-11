---
title: Generative Video WorldSim, Diffusion, Vision, Reinforcement Learning and Robotics
  — ICML 2024 Part 1
topic: models
subtopic: multimodal
secondary_topics:
- models/reasoning
summary: ICML recap on generative video world simulation, diffusion, vision, RL, and
  robotics.
source: latent-space
url: https://www.latent.space/p/icml-2024-video-robots
author: Latent Space
published: '2024-12-10'
fetched: '2026-07-11T05:19:28Z'
classifier: codex
taxonomy_rev: 1
words: 889
content_sha256: 1b3b30807c741a1a6b9efcaff8d45d17b4ccc567536a51915012c9b7faef8614
---

# Generative Video WorldSim, Diffusion, Vision, Reinforcement Learning and Robotics — ICML 2024 Part 1

*Regular tickets are now sold out for  Latent Space LIVE! at NeurIPS! We have just announced our last speaker and newest track, friend of the pod Nathan Lambert* who

*will be recapping 2024 in Reasoning Models like o1*!

*We opened up a handful of late bird tickets for those who are deciding now — use code DISCORDGANG if you need it. See you in Vancouver!*

We’ve been sitting on our ICML recordings for a while (from today’s first-ever SOLO guest cohost, [Brittany Walker](https://x.com/brittwalker_?ref_src=twsrc%5Egoogle%7Ctwcamp%5Eserp%7Ctwgr%5Eauthor)), and in light of [Sora Turbo’s launch](https://www.youtube.com/live/2jKVx2vyZOY) ([blogpost](https://openai.com/index/sora-is-here/), [tutorials](https://www.youtube.com/watch?v=360ZqfabuPQ&list=PLOXw6I10VTv8q5PPOsuECYDFqohnJqbYB&index=1)) today, we figured it would be a good time to drop part one which had been gearing up to be a deep dive into the state of **generative video worldsim**, with a seamless transition to **vision** (the opposite modality), and finally **robots** (their ultimate application).

## Sora, Genie, and the field of Generative Video World Simulators

Bill Peebles, author of Diffusion Transformers, gave his most recent Sora talk at ICML, which begins our episode:

Something that is often asked about Sora is how much inductive biases were introduced to achieve these results. Bill references the[ same principles brought by Hyung Won Chung from the o1 team ](https://www.youtube.com/watch?v=kYWUEV_e2ss)- “sooner or later those biases come back to bite you”.

![](https://substackcdn.com/image/fetch/$s_!AqI9!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F444f933d-a022-43bc-bcac-088c54c9c7ae_1342x930.png)

We also recommend these reads from throughout 2024 on Sora.

- Lilian Weng’s - [literature review of Video Diffusion Models](https://lilianweng.github.io/posts/2024-04-12-diffusion-video/)
- Estimates of - [100k-700k H100s](https://www.factorialfunds.com/blog/under-the-hood-how-openai-s-sora-model-works)needed to serve Sora (not Turbo)
- [Artist guides on using Sora](https://www.fxguide.com/fxfeatured/actually-using-sora/)for professional storytelling

**Google DeepMind** had a remarkably strong presence at ICML on Video Generation Models, winning TWO Best Paper awards for:

- [Genie: Generative Interactive Environments](https://icml.cc/virtual/2024/oral/35508)(covered in- [oral](https://icml.cc/virtual/2024/oral/35508),- [poster](https://icml.cc/virtual/2024/39080), and- [workshop](https://icml.cc/virtual/2024/workshop/29960#collapse-sl-39299))

We end this part by taking in [Tali Dekel’s talk on The Future of Video Generation: Beyond Data and Scale](https://icml.cc/virtual/2024/39508).

![](https://substackcdn.com/image/fetch/$s_!YGK3!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F344bdc2d-00fe-4e34-bd37-80b69fecfeca_924x297.png)

## Part 2: Generative Modeling and Diffusion

Since 2023, **Sander Dieleman**’s perspectives ([blogpost](https://sander.ai/2024/09/02/spectral-autoregression.html), [tweet](https://x.com/sedielem/status/1820233922287919263)) on diffusion as “spectral autoregression in the frequency domain” while working on Imagen and Veo have caught the public imagination, so we highlight his talk:

![](https://substackcdn.com/image/fetch/$s_!lv-8!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7b162348-bdb2-4502-b450-efc2cbce1f26_1539x576.png)

Then we go to [Ben Poole](https://icml.cc/virtual/2024/37921) for his talk on **Inferring 3D Structure with 2D Priors, **including his work on NeRFs and DreamFusion:

Then we investigate two flow matching papers - one from the Flow Matching co-authors - [Ricky T. Q. Chen (FAIR, Meta)](https://icml.cc/virtual/2024/37945)

And how it is implemented in Stable Diffusion 3 with [Scaling Rectified Flow Transformers for High-Resolution Image Synthesis](https://icml.cc/virtual/2024/oral/35548)

Our last hit on Diffusion is a couple of oral presentations on speech, which we leave you to explore via our audio podcast

- [NaturalSpeech 3: Zero-Shot Speech Synthesis with Factorized Codec and Diffusion Models](https://icml.cc/virtual/2024/oral/35499)
- [Speech Self-Supervised Learning Using Diffusion Model Synthetic Data](https://icml.cc/virtual/2024/oral/35493)

## Part 3: Vision

The [ICML Test of Time winner was DeCAF](https://joltml.com/icml-2024/test-of-time-decaf/), which Trevor Darrell notably called “the OG vision foundation model”.

![](https://substackcdn.com/image/fetch/$s_!RhSI!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa39775dd-1190-449f-b949-18de4dae2caf_1298x407.png)

[Lucas Beyer’s talk on “Vision in the age of LLMs — a data-centric perspective”](https://slideslive.com/39022228/vision-in-the-age-of-llms-a-datacentric-perspective?ref=search-presentations) was also well received online, and he talked about his journey from Vision Transformers to PaliGemma.

![](https://substackcdn.com/image/fetch/$s_!eZTt!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe9198fac-d709-431f-85ef-1f593ecd8dff_1069x409.png)

We give special honorable mention to [MLLM-as-a-Judge: Assessing Multimodal LLM-as-a-Judge with Vision-Language Benchmark](https://icml.cc/virtual/2024/oral/35497).

## Part 4: Reinforcement Learning and Robotics

We segue vision into robotics with the help of Ashley Edwards, whose work on both the Gato and the Genie teams at Deepmind is summarized in [Learning actions, policies, rewards, and environments from videos alone.](http://Ashley Edwards, whose work on both the Gato and the Genie teams at Deepmind is summarized in Learning actions, policies, rewards, and environments from videos alone)

Brittany highlighted two poster session papers:

- [Behavior Generation with Latent Actions](https://icml.cc/virtual/2024/poster/33379)- We also recommend Lerrel Pinto’s - [On Building General-Purpose Robots](https://icml.cc/virtual/2024/39069)

- [PIVOT: Iterative Visual Prompting Elicits Actionable Knowledge for VLMs](https://icml.cc/virtual/2024/poster/35217)

However we must give the lion’s share of space to ** Chelsea Finn**, now founder of Physical Intelligence, who gave FOUR talks on

- special mention to PI colleague - **Sergey Levine**on- [Robotic Foundation Models](https://icml.cc/virtual/2024/39068)

We end the podcast with a position paper that links generative environments and RL/robotics: [ Automatic Environment Shaping is the Next Frontier in RL](https://icml.cc/virtual/2024/oral/35495).

![](https://substackcdn.com/image/fetch/$s_!A9C6!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F8599deef-879b-447a-bbf6-ee26de27c9c3_1079x442.png)

## Timestamps

- [00:00:00] Intros
- [00:02:43] Sora - Bill Peebles
- [00:44:52] Genie: Generative Interactive Environments
- [01:00:17] Genie interview
- [01:12:33] VideoPoet: A Large Language Model for Zero-Shot Video Generation
- [01:30:51] VideoPoet interview - Dan Kondratyuk
- [01:42:00] Tali Dekel - - [The Future of Video Generation: Beyond Data and Scale](https://icml.cc/virtual/2024/39508).
- [02:27:07] Sander Dieleman - - [Wading through the noise: an intuitive look at diffusion models](https://icml.cc/virtual/2024/workshop/29968#collapse-sl-39511)
- [03:06:20] Ben Poole - Inferring 3D Structure with 2D Priors
- [03:30:30] Ricky Chen - Flow Matching
- [04:00:03] Patrick Esser - Stable Diffusion 3
- [04:14:30] - [NaturalSpeech 3: Zero-Shot Speech Synthesis with Factorized Codec and Diffusion Models](https://icml.cc/virtual/2024/oral/35499)
- [04:27:00] - [Speech Self-Supervised Learning Using Diffusion Model Synthetic Data](https://icml.cc/virtual/2024/oral/35493)
- [04:39:00] - [ICML Test of Time winner: DeCAF](https://joltml.com/icml-2024/test-of-time-decaf/)
- [05:03:40] - [Lucas Beyer: “Vision in the age of LLMs — a data-centric perspective”](https://slideslive.com/39022228/vision-in-the-age-of-llms-a-datacentric-perspective?ref=search-presentations)
- [05:42:00] Ashley Edwards: - [Learning actions, policies, rewards, and environments from videos alone.](http://Ashley Edwards, whose work on both the Gato and the Genie teams at Deepmind is summarized in Learning actions, policies, rewards, and environments from videos alone)
- [06:03:30] - [Behavior Generation with Latent Actions](https://icml.cc/virtual/2024/poster/33379)
- [06:09:52] Chelsea Finn: - ["What robots have taught me about machine learning"](https://icml.cc/virtual/2024/invited-talk/35253)
- [06:56:00] Position: - [Automatic Environment Shaping is the Next Frontier in RL](https://icml.cc/virtual/2024/oral/35495)
