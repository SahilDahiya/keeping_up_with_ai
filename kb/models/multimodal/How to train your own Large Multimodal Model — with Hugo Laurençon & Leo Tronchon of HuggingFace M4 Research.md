---
title: How to train your own Large Multimodal Model — with Hugo Laurençon & Leo Tronchon
  of HuggingFace M4 Research
topic: models
subtopic: multimodal
secondary_topics:
- models/fine-tuning
summary: Hugging Face M4 interview on training large multimodal models and the IDEFICS
  project.
source: latent-space
url: https://www.latent.space/p/idefics
author: Latent Space
published: '2024-01-19'
fetched: '2026-07-11T05:21:25Z'
classifier: codex
taxonomy_rev: 1
words: 1141
content_sha256: 548845bf4e918b68a429b363d6d120cd703c13a17c433007ceeffc8622ae4f6d
---

# How to train your own Large Multimodal Model — with Hugo Laurençon & Leo Tronchon of HuggingFace M4 Research

*Latent Space is heating up! Our  paper club ran into >99 person Discord limits, oops. *

*We are also introducing 2 new  online meetups:  LLM Paper Club Asia for Asia timezone (led by Ivan), and AI in Action: hands-on application of AI (led by KBall). *

*To be notified of all upcoming Latent Space events, subscribe to *[our new Luma calendar](https://lu.ma/ls) (*sign up for individual events, or* *hit the RSS icon to sync all events to calendar*).

In the halcyon open research days of 2022 BC (*Before-ChatGPT*), DeepMind was the first to create a SOTA multimodal model by taking a pre-existing LLM ([Chinchilla 80B ](https://arxiv.org/abs/2203.15556)- now [dead](https://news.ycombinator.com/item?id=37383413)?) and pre-existing vision encoder ([CLIP](https://arxiv.org/abs/2103.00020)) and training a “glue” adapter layer, inspiring a generation of stunningly cheap and effective multimodal models including [LLaVA](https://x.com/ChunyuanLi/status/1710299381335798202?s=20) (one of the [Best Papers of NeurIPS 2023](https://www.latent.space/p/neurips-2023-papers)), [BakLLaVA](https://github.com/SkunkworksAI/BakLLaVA) and [FireLLaVA](https://twitter.com/lqiao/status/1748243039766925351).

However (for reasons we discuss in today’s conversation), DeepMind’s Flamingo model was never open sourced. Based on [the excellent paper](https://storage.googleapis.com/deepmind-media/DeepMind.com/Blog/tackling-multiple-tasks-with-a-single-visual-language-model/flamingo.pdf), LAION stepped up to create [OpenFlamingo](https://laion.ai/blog/open-flamingo/), but it never scaled beyond 9B. Simultaneously, the M4 (audio + video + image + text multimodality) research team at HuggingFace [announced](https://x.com/SanhEstPasMoi/status/1632775840135016448?s=20) an independent effort to reproduce Flamingo up to the full 80B scale:

![](https://substackcdn.com/image/fetch/$s_!96BZ!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F9f5ddd2b-4efa-43cb-b48c-ca1d995580a4_954x818.png)

[from Victor Sanh](https://twitter.com/SanhEstPasMoi/status/1632775840135016448), coauthor on IDEFICS

The effort started in March, and was released in August 2023.

We happened to visit Paris last year, and visited HuggingFace HQ to learn all about HuggingFace’s research efforts, and cover all the ground knowledge LLM people need to become (what [Chip Huyen has termed](https://huyenchip.com/2023/10/10/multimodal.html#clip)) “LMM” people. In other words:

![](https://substackcdn.com/image/fetch/$s_!A2YA!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fedc61db8-3a51-4b9b-af0b-dc8db360ecb7_1068x1528.png)

## What is IDEFICS?

IDEFICS is an Open Access Visual Language Model, available in [9B](https://huggingface.co/HuggingFaceM4/idefics-9b) and [80B](https://huggingface.co/HuggingFaceM4/idefics-80b) model sizes. As an attempt to re-create an open-access version of [Flamingo](https://arxiv.org/abs/2204.14198), it seems to track very well on a range of multimodal benchmarks (which we discuss in the pod):

![](https://substackcdn.com/image/fetch/$s_!Rtxz!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F885336bf-7450-4679-9124-5abaecf52e76_3432x1444.png)

You can see the reasoning abilities of the models to take a combination of interleaved images + text in a way that allows users to either describe images, ask questions about the images, or extend/combine the images into different artworks (e.g. poetry).

![](https://substackcdn.com/image/fetch/$s_!JtLG!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F2f886b11-e918-4634-b7c1-24b60d48f86a_2994x1608.png)

![](https://substackcdn.com/image/fetch/$s_!gki4!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F5bf75534-b94f-498f-ab18-c58827503ed7_992x1864.png)

📷 From IDEFICS’s

[model card](https://huggingface.co/HuggingFaceM4/idefics-80b-instruct)and[blog post](https://huggingface.co/blog/idefics)

The above demo screenshots are actually fine-tuned instruct versions of IDEFICS — which are again in [9B ](https://huggingface.co/HuggingFaceM4/idefics-9b-instruct)and [80B ](https://huggingface.co/HuggingFaceM4/idefics-80b-instruct)versions.

IDEFICS was built by connecting two unimodal models together to provide the multi-modality you see showcased above.

- [Llama](https://huggingface.co/huggyllama/llama-65b)v1 for language (specifically- [huggyllama/llama-65b](https://huggingface.co/huggyllama/llama-65b)) - the best available open model at the time, to be swapped for Mistral in the next version of IDEFICS
- [A CLIP](https://github.com/mlfoundations/open_clip)model for vision (specifically- [laion/CLIP-ViT-H-14-laion2B-s32B-b79K](https://huggingface.co/laion/CLIP-ViT-H-14-laion2B-s32B-b79K)- after a brief exploration of- [EVA-CLIP](https://huggingface.co/QuanSun/EVA-CLIP), which we discuss on the pod)

## OBELICS: a new type of Multimodal Dataset

IDEFICS’ training data used the usual suspect datasets, but to get to par with Flamingo they needed to create a new data set.

Enter [OBELICS](https://huggingface.co/datasets/HuggingFaceM4/OBELICS): “An Open Web-Scale Filtered Dataset of Interleaved Image-Text Documents”:

- 115B text tokens
- 141M English documents
- 353M images

These bullets are carefully curated and filtered by going through Common Crawl dumps between FEB 2020 - FEB 2023. We discuss the 2 months of mindnumbing, unglamorous work creating this pipeline:

![](https://substackcdn.com/image/fetch/$s_!eJRu!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F0d5c50ec-6789-4a45-bd85-5d0f9e230ad5_1760x1008.png)

There’s a lot of mentions of ‘multi-modal' web documents’ which deserves some explanation. We’ll show you instead of tell you:

![](https://substackcdn.com/image/fetch/$s_!Ze4k!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F2301678f-9f96-4960-b72a-5c0bf16ed2a9_1716x958.png)

You can see from this graph that OBELICS ends up outperforming the other image-text pairs dataset (LAION in this case) when stacked head-to-head.

![](https://substackcdn.com/image/fetch/$s_!wAwe!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb5aad288-7723-4361-8d1e-0d21398be535_1146x296.png)

You can view a subset of OBELICS and perform visualizations on them [here](https://atlas.nomic.ai/map/f2fba2aa-3647-4f49-a0f3-9347daeee499/ee4a84bd-f125-4bcc-a683-1b4e231cb10f):

![](https://substackcdn.com/image/fetch/$s_!xUyQ!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe7907c05-8d2d-4ea6-94af-397b2703b9aa_3016x1716.png)

## 2024 Update: WebSight et al

Most of this interview was recorded on Halloween 2023 at HuggingFace’s headquarters in Paris:

![](https://substackcdn.com/image/fetch/$s_!qVKa!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F1ec0a5cf-7af3-44d6-8fb1-31316f775882_4032x3024.jpeg)

![](https://substackcdn.com/image/fetch/$s_!y-BX!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F2d326eaf-5bc5-4b8e-bc15-95928568e8f6_4032x3024.jpeg)

![](https://substackcdn.com/image/fetch/$s_!ls3R!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F84beec12-30de-44d2-adcf-711e0fe7a58c_4032x3024.jpeg)

[meetup](https://twitter.com/swyx/status/1718924377452884034)!

In anticipation of an IDEFICS v2 release. However, several roadblocks emerged, including a notable scandal around [CSAM in LAION-5B](https://www.theverge.com/2023/12/20/24009418/generative-ai-image-laion-csam-google-stability-stanford), which affected all models using that dataset. The M4 team have adopted a strategy of shipping smaller advancements in 2024, and the first ship of the year is [WebSight](https://huggingface.co/datasets/HuggingFaceM4/WebSight), a dataset of 823,000 HTML/CSS codes representing synthetically generated English websites, each accompanied by a corresponding screenshot (rendered with ** Playwright**). This is intended for tasks like screenshot-to-code workflows like Vercel’s V0 or

[TLDraw](https://www.latent.space/p/tldraw), and will be part of the dataset for IDEFICS-2.

![](https://substackcdn.com/image/fetch/$s_!KJWO!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4412cea9-9cc2-4f90-aa93-4e3cf83214a4_475x448.png)

[thread from Leo](https://x.com/LeoTronchon/status/1746952870824394953?s=20)

![](https://substackcdn.com/image/fetch/$s_!FZDW!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fff218083-f63e-4563-a9fa-91d0fa22797a_473x546.png)

[thread from Hugo](https://twitter.com/HugoLaurencon/status/1746950099089883382)

As noted in [our Best Papers recap](https://www.latent.space/p/neurips-2023-papers), **synthetic data** is emerging as one of the top themes of 2024, and the IDEFICS/OBELICS team have wasted no time enabling themselves with it.

## Timestamps

- [0:00:00] Intro
- [0:00:00] Hugo, Leo’s path into multimodality
- [0:09:16] From CLIP to Flamingo
- [0:12:54] Benchmarks and Evals
- [0:16:54] OBELICS dataset
- [0:34:47] Together Redpajama v2
- [0:37:12] GPT4 Vision
- [0:38:44] IDEFICS model
- [0:40:57] Query-Key Layernorm for training
- [0:46:40] Choosing smaller vision encoders - EVA-CLIP vs SIG-GLIP
- [0:49:02] IDEFICS v2
- [0:52:39] Multimodal Hallucination
- [0:59:12] Why Open Source Multimodality
- [1:05:29] Naming: M4, OBELICS, IDEFICS
- [1:08:56] 2024 Update from Leo

## Show Notes

- [Introducing IDEFICS: An Open Reproduction of State-of-the-Art Visual Language Model](https://huggingface.co/blog/idefics)
- [OBELICS: An Open Web-Scale Filtered Dataset of Interleaved Image-Text Documents](https://huggingface.co/papers/2306.16527)
- Papers cited: - [BLOOM](https://arxiv.org/abs/2211.05100): A 176B-Parameter Open-Access Multilingual Language Model
- [Barlow Twins](https://arxiv.org/abs/2103.03230): Self-Supervised Learning via Redundancy Reduction
- [CLIP paper](https://arxiv.org/abs/2103.00020): Learning Transferable Visual Models From Natural Language Supervision
- [Vision Transformers paper](https://arxiv.org/abs/2010.11929): An Image is Worth 16x16 Words: Transformers for Image Recognition at Scale
- [Flamingo paper](https://arxiv.org/abs/2204.14198): a Visual Language Model for Few-Shot Learning
- [VQAV2 paper](https://paperswithcode.com/paper/making-the-v-in-vqa-matter-elevating-the-role): Making the V in VQA Matter: Elevating the Role of Image Understanding in Visual Question Answering
- [OK-VQA: A Visual Question Answering Benchmark](https://arxiv.org/abs/1906.00067)Requiring External Knowledge- [https://okvqa.allenai.org/](https://okvqa.allenai.org/))
- [Qwen-VL](https://arxiv.org/abs/2308.12966): A Versatile Vision-Language Model for Understanding, Localization, Text Reading, and Beyond
- [Sig-GLIP paper](https://arxiv.org/pdf/2303.15343):- [Sigmoid Loss for Language Image Pre-Training](https://arxiv.org/pdf/2303.15343)
- [Nougat](https://facebookresearch.github.io/nougat/): Neural Optical Understanding for Academic Documents
- [MMC4 (Multimodal C4)](https://arxiv.org/pdf/2304.06939v1.pdf): An Open, Billion-scale Corpus of Images Interleaved With Text
- Dall-E 3 paper: - [Improving Image Generation with Better Captions](https://cdn.openai.com/papers/dall-e-3.pdf)- [GPT-4V(ision) system card](https://openai.com/research/gpt-4v-system-card)from OpenAI

- Query-Key Layernorm trick: - [paper](https://arxiv.org/abs/2302.05442)(Scaling Vision Transformers to 22 Billion Parameters),- [tweet](https://x.com/SanhEstPasMoi/status/1632775853640646657?s=20)
- [EVA-CLIP: Improved Training Techniques for CLIP at Scale](https://arxiv.org/abs/2303.15389)- “We intially explored using a significantly bigger vision encoder (the biggest in open-access at that time) with - [EVA-CLIP](https://huggingface.co/QuanSun/EVA-CLIP). However, we ran into training instabilities very quickly. To lower the risks associated to the change of vision encoder, we decided to continue with- [laion/CLIP-ViT-H-14-laion2B-s32B-b79K](https://huggingface.co/laion/CLIP-ViT-H-14-laion2B-s32B-b79K)which we have been using until that point. We will leave that swap for future iterations and will also consider using higher resolution images.”


- Datasets - [Together’s RedPajama-Data-v2](https://www.together.ai/blog/redpajama-data-v2): An open dataset with 30 trillion tokens for training large language models

- [HuggingFace timm](https://huggingface.co/docs/timm/index): library containing SOTA computer vision models, layers, utilities, optimizers, schedulers, data-loaders, augmentations, and training/evaluation scripts. It comes packaged with >700 pretrained models, and is designed to be flexible and easy to use.
- [Logan Kilpatrick declaring 2024 the year of Multimodal AI](https://www.youtube.com/watch?v=bNZV9s3_u44&t=80s)at AI Engineer Summit
