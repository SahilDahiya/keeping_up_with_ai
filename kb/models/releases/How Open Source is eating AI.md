---
title: How Open Source is eating AI
topic: models
subtopic: releases
secondary_topics:
- industry/trends
summary: Essay on how open source is eating AI and why open model ecosystems matter
  for product builders.
source: latent-space
url: https://www.latent.space/p/open-source-ai
author: Latent Space
published: '2022-10-09'
fetched: '2026-07-11T05:24:10Z'
classifier: codex
taxonomy_rev: 1
words: 2669
content_sha256: 9c2fda1f88ddbc81a1f679f6336118b6cd8efa60d0639ed7dee68100675c6c40
---

# How Open Source is eating AI

# How Open Source is eating AI

### Why the best delivery mechanism for AI is not APIs

*Translations:  Chinese*

**The GPT-2 cycle took 6 months:**

- In Feb 2019, OpenAI - [announced GPT-2](https://openai.com/blog/better-language-models/), but also said it was- [too dangerous to release](https://techcrunch.com/2019/02/17/openai-text-generator-dangerous/)in full, and restructured from- [nonprofit to capped-profit](https://openai.com/blog/openai-lp/)
- By August, it had been cloned in the - **open**by- [two master’s students](https://www.wired.com/story/dangerous-ai-open-source/)as- [OpenGPT-2](https://medium.com/@vanya_cohen/opengpt-2-we-replicated-gpt-2-because-you-can-too-45e34e6d36dc)
- By November, OpenAI - [released their 1.5B parameter model](https://news.ycombinator.com/item?id=21454273), after a cautious- [staged release process](https://openai.com/blog/gpt-2-6-month-follow-up/)

**The GPT-3 cycle took 10 months:**

- May 2020: OpenAI released GPT-3 as a - [paper](https://news.ycombinator.com/item?id=23345379)and- [a closed beta API in June 2020](https://openai.com/blog/openai-api/).
- Jul 2020: - [EleutherAI forms](https://docs.google.com/document/d/1wfCZBd18DMNt6YcC6boPNMd9qzzH3zpHHfKj4dezk0g/edit#heading=h.cdkflzswstii)as the truly open alternative to OpenAI
- Sep 2020: Grants Microsoft “ - [exclusive license for GPT-3](https://news.ycombinator.com/item?id=24558329)”
- Jan 2021: EleutherAI released - [The Pile](https://blog.eleuther.ai/year-one/#the-pile), their 800GB dataset
- Mar 2021: EleutherAI released their - **open**- [GPT-Neo 1.3B](https://huggingface.co/EleutherAI/gpt-neo-1.3B)and- [2.7B](https://huggingface.co/EleutherAI/gpt-neo-2.7B)models
- Nov 2021: OpenAI takes the - [waitlist off their API](https://openai.com/blog/api-no-waitlist/)
- May 2022: Meta released - [OPT-175B for researchers](https://ai.facebook.com/blog/democratizing-access-to-large-scale-language-models-with-opt-175b/)(- [with logbook](https://github.com/facebookresearch/metaseq/blob/main/projects/OPT/chronicles/OPT175B_Logbook.pdf)! and- [an open license](https://github.com/facebookresearch/metaseq/blob/main/projects/OPT/MODEL_LICENSE.md?fbclid=IwAR3Voi_-OZG-KXVgYuD_QVub72VlbY68YFLKnLJXTxPnHlSBunz7CcPiXBA))
- Jun 2022: Yandex - [releases YaLM-100B](https://news.ycombinator.com/item?id=31846593)under an Apache-2 license
- Jul 2022: HuggingFace - [releases BLOOM-176B](https://news.ycombinator.com/item?id=32067705)under a RAIL license

**The Text-to-Image cycle took 2? years **(Nov 2022 edit: [a fuller 10 year history including GANs is here](https://zentralwerkstatt.org/blog/ten-years-of-image-synthesis))**:**

- Jun 2020: OpenAI blogs about - [Image GPT](https://openai.com/blog/image-gpt/)
- Dec 2020: Patrick Esser et al publish - [Taming Transformers for High-Resolution Image Synthesis](https://twitter.com/sedielem/status/1339929984836788228)(aka VQGAN, a sharp improvement on 2019’s- [VQVAE](https://twitter.com/_akhaliq/status/1135721918689107968)s)
- Jan 2021: OpenAI announces results from the - [first DALL-E](https://openai.com/blog/dall-e/)and open sources- [CLIP](https://openai.com/blog/clip/)
- May 2021: OpenAI releases finding that - [Diffusion Models beat GANs on Image Synthesis](https://twitter.com/arankomatsuzaki/status/1392280377784369152)
- Dec 2021: the CompVis group publish - [High-Resolution Image Synthesis with Latent Diffusion Models](https://research.runwayml.com/publications/high-resolution-image-synthesis-with-latent-diffusion-models)together with the original- [CompVis/latent-diffusion](https://github.com/CompVis/latent-diffusion)repo
- Dec 2021: OpenAI publishes - [GLIDE: Towards Photorealistic Image Generation and Editing with Text-Guided Diffusion Models](https://twitter.com/_akhaliq/status/1473110361167511553)
- Mar 2022: Midjourney launches its - [closed beta](https://boingboing.net/2022/03/24/midjourney-sharpens-style-of-ai-art.html)
- Apr 2022: OpenAI announces - [DALL-E 2](https://openai.com/dall-e-2/)with a limited “- [research preview](https://openai.com/blog/dall-e-2-update/)”
- May 2022: Google releases their - [Imagen](https://imagen.research.google/)paper (implemented in PyTorch- [in 3 days](https://news.ycombinator.com/item?id=31513919))
- Jul 2022: DALL-E 2 available as an - [open beta (with waitlist)](https://openai.com/blog/dall-e-now-available-in-beta/)via OpenAI’s UI/API
- Jul 2022: Midjourney also announces a - [fully-open beta](https://www.vice.com/en/article/wxn5wn/inside-midjourney-the-generative-art-ai-that-rivals-dall-e)via their Discord
- Aug 2022: - **Stable Diffusion**1.4 publicly released,- [under OpenRAIL-M license](https://stability.ai/blog/stable-diffusion-public-release). Models & Code from CompVis + Runway, Funding from Stability AI to scale up compute
- Sep 2022: OpenAI takes the - [waitlist off](https://openai.com/blog/dall-e-now-available-without-waitlist/)DALL-E 2
- **UPDATE**Oct 2022 : Stable Diffusion 1.5- [released by Runway, with some controversy](https://news.ycombinator.com/item?id=33279290)
- **UPDATE**Nov 2022:- [Stable Diffusion 2.0](https://stability.ai/blog/stable-diffusion-v2-release)released by Stability

The timelines above are highly cherrypicked of course; the story is much longer if you take into account the longer development history starting from the academic papers for [diffusion](https://arxiv.org/pdf/1503.03585.pdf) (2015) and [transformer models](https://arxiv.org/abs/1706.03762) (2017) and older work on GANs. See also [the research origins of Stable Diffusion](https://research.runwayml.com/the-research-origins-of-stable-difussion) from RunwayML and Emad’s description of the CC12M breakthroughs in Dec 2021 in [his chat with Elad Gil](https://www.youtube.com/watch?v=ESDeUi8Yl-8&t=1s).

But what is more interesting is what has happened since: OpenAI’s audio-to-text model, Whisper, was [released under MIT license](https://news.ycombinator.com/item?id=32927360) in September with no API paywall. Of course, there is less scope for abuse in the audio-to-text domain, but more than a few people have speculated that the reception to Stable Diffusion’s release influenced the open sourcing decision.

## Dreambooth: Community Take The Wheel

**Sufficiently advanced community is indistinguishable from magic**. Researchers and well funded teams have been very good at producing new **foundational models** (FM), but it is the open source community that have been very good at coming up with productized use cases and optimizing the last mile of the models.

The most quantifiable example of this happened with the **recent  Dreambooth cycle **(finetuned text to image with few shot learning of a subject to insert in a scene).

![](https://substackcdn.com/image/fetch/$s_!OHdM!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Fb191b063-91ad-42c5-97eb-6b392d194057_1678x954.png)

**Dreambooth** is an attractive target for optimization because it doesn’t just involve downloading a model and running it, it also requires you to run finetuning training on your sample images, but the original port required so much memory that it was infeasible for most people to run in on their machines.

Well, that, and also the Corridor Digital guys made it go viral on YouTube:

Timeline in tweet form:

![X avatar for @swyx](https://substackcdn.com/image/fetch/$s_!TnFC!,w_40,h_40,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack.com%2Fimg%2Favatars%2Fdefault-light.png)

*For those counting along at home, that’s  an open source port in 12 days and then a 79% reduction in system requirements in the subsequent 25.*

Edit from the future: on Oct 8 this

[dropped again to 8GB](https://twitter.com/psuraj28/status/1579557129052381185).

Most of this optimization happened [on GitHub](https://github.com/XavierXiao/Dreambooth-Stable-Diffusion/issues/35#issue-1386850702) between [Xavier Xiao](https://xavierxiao.github.io/) (a generative models and optimization PhD from Singapore working at AWS AI), and [Shivam Shrirao](https://www.linkedin.com/in/shivamshrirao) (a Senior Computer Vision Engineer based in India), [with help from Matteo Serva from Italy](https://www.reddit.com/r/StableDiffusion/comments/xsrafl/comment/iqnkk04/?context=3). Both were unaffiliated to the original Dreambooth team.

The low hanging fruit is gone, causing some to [worry about diminishing returns](https://www.reddit.com/r/StableDiffusion/comments/xsrafl/comment/iqnkk04/?utm_source=reddit&utm_medium=web2x&context=3), but some proofs of concept exist for getting Stable Diffusion itself down small enough to run on a phone ([down from 10GB and 5GB before](https://twitter.com/EMostaque/status/1557862289394515973) - consumer cards have [6-12GB](https://www.howtogeek.com/794750/does-gpu-memory-matter-how-much-vram-do-you-need/) and iDevices have unified memory).

![X avatar for @wattmaller1](https://substackcdn.com/image/fetch/$s_!TnFC!,w_40,h_40,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack.com%2Fimg%2Favatars%2Fdefault-light.png)

This would probably be the holy grail of Open Source AI model optimization, because then image generation is effectively unconstrained by cloud economics and the profit motive.

Oct 2022 update: an open source impl is here:

[https://github.com/madebyollin/maple-diffusion](https://github.com/madebyollin/maple-diffusion)

## What Open Source Does that Researchers Don’t

While Stable Diffusion arrived the latest out of the 3 new text-to-image models, there were lots of community advances that have helped Stable Diffusion leap far ahead of the competing image-to-text models Midjourney and DALL-E in terms of mindshare and applications.

This serves as a useful generalizable roadmap for how open sourcing other forms of AI ([music, biology, language models](https://twitter.com/EMostaque/status/1577754082831392774?s=20&t=vvW9q8zp6M_ZhlURFGq7IQ)) might create new opportunities.

![](https://substackcdn.com/image/fetch/$s_!G70w!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Fb32810ef-2e8d-4078-94cf-1ddd957130af_1394x990.png)

In rough order of *increasing* technical skill required:

- **Improving documentation**- The original - [CompVis README](https://github.com/CompVis/stable-diffusion)wasn’t very beginner friendly
- The community came together to create: - [R*tard guides](https://rentry.org/GUItard)(4chan lingo, don’t ask) and- [regular guides](https://keras.io/guides/keras_cv/generate_images_with_stable_diffusion/#wait-how-does-this-even-work)


- **Sharing prompts**- Prompt engineering is an - [acquired skill](https://twitter.com/ESYudkowsky/status/1575345276298018816?s=20&t=Y-07UlB4wvYTNfVNUpoWLA)that is still turning up surprising results like- [this](https://twitter.com/arankomatsuzaki/status/1529278580189908993)and- [this](https://twitter.com/shaneguML/status/1577504502235639808)in GPT3 land 3 years after release; it means LLMs have a large latent space of- *abilities*(not just results), that we are still only beginning to explore.
- Every community now has ingrained ways of - [sharing prompts](https://www.reddit.com/r/StableDiffusion/comments/xqv5tf/people_who_share_their_prompts_are_awesome/), and from then we can build up- [prompt galleries](https://github.com/sw-yx/prompt-eng#communities)that significantly reduce the latency of promptfinding (from >30s to <300ms, 2 orders of magnitude!) and therefore learning curve of prompt engineering.
- In this way the community is also figuring out known hard problems like - [how to generate realistic hands](https://www.reddit.com/r/StableDiffusion/comments/xt9ou9/i_solved_hands_for_now/)and- [the importance of negative prompting](https://www.reddit.com/r/StableDiffusion/search/?q=negative%20prompting&restrict_sr=1&sr_nsfw=&include_over_18=1).

- **Creating new UIs and improving accessibility**- Since Stable Diffusion is “just” a python script, people can build their own UIs to suit their own purposes, without being shackled to Stability AI’s own Dreambooth.
- [AUTOMATIC1111](https://github.com/AUTOMATIC1111/stable-diffusion-webui)has emerged as the leading community web UI, with a- [large range of features](https://github.com/AUTOMATIC1111/stable-diffusion-webui-feature-showcase)encoding the community discovered wisdom on SD usage
- Since the ML community has a Windows bias, the open source community has implemented a ton of tricks to - [make it run on M1 Macs](https://github.com/invoke-ai/InvokeAI)and maybe iPhones (as shown above).
- SD UIs are usually standalone apps, but new delivery modes unlock more casual usage as part of existing workflows, inside - [Photoshop](https://www.getalpaca.io/),- [Figma](https://twitter.com/RemitNotPaucity/status/1562319004563173376?s=20&t=fPSI5JhLzkuZLFB7fntzoA),- [GIMP](https://80.lv/articles/a-new-stable-diffusion-plug-in-for-gimp-krita/), and even- [VR](https://twitter.com/ScottieFoxTTV/status/1578387866572525570).

- **Creating new usecases**by extending existing features in creative ways- I am unclear on who invented Inpainting and Outpainting techniques first (it was first hinted at in the DALL-E announcement, but really became widespread once open source UIs - [like this](https://www.reddit.com/r/StableDiffusion/comments/xogg2u/progress_on_getimgai_outpainting_prototype_and/)were created for it)
- **Remixing with other tooling/techniques**is another source of ripe innovation- “Reverse prompt engineering” aka using image to prompt (with - [CLIP Interrogator](https://twitter.com/pharmapsychotic/status/1557023866404458498))
- Using - [txt2mask](https://github.com/ThereforeGames/txt2mask)to augment inpainting
- Multiple postprocessing steps including using Real-ESRGAN, TECOGAN, GFPGAN, VQGAN, and more (e.g. “ - [hires fix](https://www.reddit.com/r/StableDiffusion/comments/xq8cjp/comment/iq80s34/?utm_source=reddit&utm_medium=web2x&context=3)” in automatic1111)
- Creating a GRPC server (for communicating with - [Stability AI](https://github.com/hafriedlander/stable-diffusion-grpcserver))
- [Preparing for new modalities](https://github.com/parlance-zz/g-diffuser-bot)like txt2music, music2img


- **Optimizing the core**- (as discussed above) minimizing memory for - [Stable Diffusion](https://news.ycombinator.com/item?id=32709201)and- [Dreambooth](https://twitter.com/simonw/status/1574845672087375873?s=20&t=_hag3iW9zglwiK883R-A5A)
- Improving speed on - [Stable Diffusion by 50%](https://twitter.com/labmlai/status/1573634095732490240)


A fun but important tangent - most of this AI/ML stuff is written in Python, which is [comically insecure](https://www.youtube.com/watch?v=2ethDz9KnLk) as a distribution mechanism. This means the rise of “Open Source AI” will also come with increasing need for “**Open Source AI Security**”.

## The Future of Open Source AI

This whole journey is reminiscent of how open source ate Software 1.0:

- Version Control: From Bitkeeper to Git
- Languages: From Java toolchain to Python, JavaScript, and Rust
- IDEs: From [many decent IDEs] to VS Code taking >60% market share
- Databases: From Oracle/IBM to Postgres/MySQL

Anders Hejlsberg, father of 5 languages from Turbo Pascal to TypeScript, famously [said that](https://www.youtube.com/watch?v=jmPZztKIFf4) no programming language will be successful in future without being open source. You can probably say the same for increasingly [more of your stack](https://dx.tips/platform-kinds).

It is tempting to conclude that the same sequence will happen in Software 2.0/3.0, but a few issues remain.

## Issue 1: Economic Incentives

To the economics minded, the desire to release [foundation models](https://en.wikipedia.org/wiki/Foundation_models) as open source is counterintuitive. Estimates for the cost of training GPT-3 run between [$4.6](https://lambdalabs.com/blog/demystifying-gpt-3/) to [$12](https://towardsdatascience.com/the-future-of-ai-is-decentralized-848d4931a29a) million, excluding staff costs and failed attempts (some startups now claim to [get it down to 450k](https://www.mosaicml.com/blog/gpt-3-quality-for-500k)). Even Stable Diffusion’s impressive [$600k cost](https://the-decoder.com/training-cost-for-stable-diffusion-was-just-600000-and-that-is-a-good-sign-for-ai-progress/) (Emad has hinted the real number is [much lower](https://twitter.com/EMostaque/status/1563870674111832066), but also said they spent 13x that ([2m a100 hours](https://youtu.be/ESDeUi8Yl-8?t=574)) for experimentation) isn’t something to sneeze at or give away without a plan for making back the investment.

Taking OpenAI’s trajectory of monetizing through APIs, everyone understood what the AI Economy was shaping up to look like:

![](https://substackcdn.com/image/fetch/$s_!7Y0-!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F5f8aeec6-3938-4770-9893-779e99db597f_2364x1532.png)

*(arguable if Research > Infra, I made them about parity with each other, but just humor me here)*

But Stability AI’s stated goals as a non-economic actor is both pressuring down the economic value of owning proprietary Foundational Model research, and expanding the total TAM of AI overall:

![](https://substackcdn.com/image/fetch/$s_!8R8x!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Fd618786f-53b2-476c-9024-98223653d4b0_1210x872.png)

This is known as Stan Shih’s [Smiling Curve model](https://en.wikipedia.org/wiki/Smiling_curve) of industry value distribution, also [discussed widely by Ben Thompson](https://stratechery.com/outline/smiling-curve/).

The big shoe to drop is how exactly Stability intends to finance itself - [the $100m Series A](https://twitter.com/aarongdillon/status/1571187877081407492?s=46&t=ZWB5uMpCxz-kjKVrauW7-w) bought some time, but the ecosystem won’t really stabilize until we really know how Stability intends to make money.


[Response from Emad](https://twitter.com/EMostaque/status/1579189433982935041?s=20&t=d2x-JV8GQBRh_C-WrhHRZQ): “Business model is simple, scale and service like normal COSS but with some value add twists.”

## Issue 2: Licensing

According to the most committed open source advocates, we’ve been using the word wrong in this entire essay. Strictly speaking, a project is only open source if it has one of the [few dozen OSI approved licenses](https://opensource.org/licenses). Meanwhile, virtually none of the “open source AI” models or derivatives here have even bothered with a license, with sincere questions completely ignored:

- [https://github.com/AUTOMATIC1111/stable-diffusion-webui/issues/24](https://github.com/AUTOMATIC1111/stable-diffusion-webui/issues/24)
- [https://github.com/divamgupta/diffusionbee-stable-diffusion-ui/issues/5](https://github.com/divamgupta/diffusionbee-stable-diffusion-ui/issues/5)

Oct 2022 edit:

[InvokeAI](https://github.com/invoke-ai/InvokeAI)is a[notable exception](https://news.ycombinator.com/item?id=33395972), MIT licensed

Stable Diffusion itself was released with a new [CreativeML Open RAIL-M](https://github.com/CompVis/stable-diffusion/blob/main/LICENSE) license (RAIL stands for [Responsible AI](https://www.licenses.ai/), created by an [independent team](https://www.licenses.ai/team)), which governs the model weights (the thing you spend $600k to obtain) with [certain sections](https://github.com/divamgupta/diffusionbee-stable-diffusion-ui/issues/56#issuecomment-1257190039) compatible with OSI-approved licenses, but also with use case restrictions that are not. If you have ever dealt with legal departments and OSI people, you know that won’t fly and the opinions [are](https://hn.algolia.com/?dateRange=all&page=0&prefix=true&query=%22open%20rail-m%22&sort=byPopularity&type=comment) [mixed](https://hn.algolia.com/?dateRange=all&page=0&prefix=true&query=%22openrail%22&sort=byPopularity&type=comment) with no legal precedents to rely on.

StabilityAI has demonstrated seriousness that you are clear to use its products for commercial purposes, even [publicly supporting](https://twitter.com/EMostaque/status/1561917541743841280?s=20&t=k-xgo6e7HMMeDLrSKCwlVQ) Midjourney in using Stable Diffusion, but when the stakes are someday 1000x higher than this, the legal details start to matter.

Note from

[Carlos Muñoz Ferrandis](https://twitter.com/Carlos_MFerr),[AI Counsel at HuggingFace](https://twitter.com/Carlos_MFerr): “Meta released[OPT175](https://ai.facebook.com/blog/democratizing-access-to-large-scale-language-models-with-opt-175b/)(LLM),[BB3](https://github.com/facebookresearch/ParlAI/blob/main/parlai/zoo/bb3/model_card.md)(chatbot) and[SEER](https://ai.facebook.com/blog/seer-10b-better-fairer-computer-vision-through-self-supervised-learning-training-on-diverse-datasets/)(computer vision) with a license similar to a RAIL (including use-case restrictions) and for research purposes only (2 variants of the license depending on the model).”

OpenAI Whisper is the first instance I am aware of where model, weights, and code have all been released under a straightforward, “honest-to-god open source”, MIT license.


[Correction from Emad](https://twitter.com/EMostaque/status/1579189433982935041): “All of the models we have backed except stable diffusion have been MIT released, eg OpenCLIP that took 1.2 million A100 hours.”


Time sensitive Note: if you’re serious about licenses, GitHub and the Open Source Institute are organizing[discussions](https://blog.opensource.org/osi-leading-an-essential-discussion-on-the-future-of-ai-and-open-source/)and a[panel on Oct 18](https://deepdive.opensource.org/). You can also contact[Luis Villa](https://twitter.com/luis_in_brief/status/1579557030784040960), general counsel of Tidelift.

## Issue 3: What gets “Open Sourced”?

OSI approval aside, another wrinkle we have intentionally ignored until the very end of this essay is the actual nature of what “open sourcing” even means.

In a typical Software 1.0 context, “open source” would mean that the codebase is open source, but not necessarily details around the infrastructure setup nor the data accumulated/operated on by the code. In other words, **open code** does not mean **open infra** nor **open data** (though in practice at least some rudimentary guide on how to self-host is expected though not required).

With [Software 2.0](https://karpathy.medium.com/software-2-0-a64152b37c35), the data collection becomes really important and starts to dominate the code (which is reduced to model architecture). [Open datasets](https://github.com/sw-yx/spark-joy/blob/master/README.md#useful-big-datasets) like [ImageNet](https://www.image-net.org/) helped to train an entire generation of ML engineers, most notably powering [Kaggle competitions](https://www.kaggle.com/competitions) and of course [the ImageNet challenge itself](https://en.wikipedia.org/wiki/ImageNet#ImageNet_Challenge) (where AlexNet and CNNs pushed the entire field to [converge to deep learning](https://twitter.com/karpathy/status/1468370605229547522)). With semi-homomorphic encryption, you could even occlude the data to create systems like [Numerai](https://numer.ai/) - not strictly open, but open enough that a bored data scientist might [play with the fake numbers](https://www.youtube.com/watch?v=wbfu39l0kxg) and make some side cash. Still, the norm was very much not to offer **open weights**, as that is the most expensive thing to train.

With [Software 3.0](https://towardsdatascience.com/software-3-0-how-prompting-will-change-the-rules-of-the-game-a982fbfe1e0) and [known scaling curves due to Chinchilla](https://www.lesswrong.com/posts/6Fpvch8RR29qLEWNH/chinchilla-s-wild-implicationsa), LLMs and FMs become onetime, large investments undertaken on a single large corpus behalf of humanity.

The “Open Source AI” movement is tackling it a few different ways:

- **Open Datasets**: For example,- [LAION-5B](https://laion.ai/laion-5b-a-new-era-of-open-large-scale-multi-modal-datasets/), and- [The Pile](https://blog.eleuther.ai/year-one/#the-pile). These datasets have been modified for- [Waifus](https://github.com/harubaru/waifu-diffusion)(sigh… dont ask),- [Japanese](https://huggingface.co/blog/japanese-stable-diffusion),- [Chinese](https://huggingface.co/spaces/PaddlePaddle/chinese-stable-diffusion), and- [Russian](https://github.com/yandex/YaLM-100B).
- **Open Models:**Usually released by research papers - if enough detail is given, people can reimplement them in the wild as happened with GPT3 and Dreambooth
- **Open Weights**: This is the new movement begun- [first](https://twitter.com/Carlos_MFerr/status/1579563828320567297?s=20&t=jir8GmaEfF3gC3nI74bEsA)by EleutherAI’s GPT-Neo and GPT-J (- [thanks Stella Biderman](https://lspace.swyx.io/p/open-source-ai/comment/11510868)), then HuggingFace’s- [BigScience](https://bigscience.huggingface.co/)(that released BLOOM), then applied to text-to-image by Stability AI, and continued with OpenAI Whisper (- *the economics of which are discussed in Issue 1)*
- **Open Interface**: aka not just provided an API to call, as OpenAI had been doing with GPT3, but actually- **giving direct access to code**so that users can modify and write their own CLIs, UIs and whatever else they wish.
- **Open Prompts:**users (like- [Riley Goodside](https://twitter.com/goodside/status/1568448128495534081)) and researchers (like- [Aran Komatsuzaki](https://twitter.com/arankomatsuzaki/status/1529278580189908993)) sharing prompt technique breakthroughs that unlock latent abilities in the FM.

![](https://substackcdn.com/image/fetch/$s_!AT9g!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F41e745f8-ff15-4c7d-87e7-907fe74fa0a2_1354x1006.png)

The exact order of these will vary based on substance of the advancement and contextual variation, but this *feels* right?

## An Open Source AI Institute?

It is probably true that the Open Source Initiative is not set up to consider all these dimensions in “open source” AI, and the one of the most foundational initiatives for an open source AI culture is to create a credible standard with expectations, norms, and legal precedent. This is [Hugging Face](https://research.contrary.com/company/hugging-face) and Stability AI’s opportunity, but perhaps there have already been other initiatives doing so that I just havent come across yet.

## Related Reads

- Most of my notes are taken in public; - [watch this repo](https://github.com/sw-yx/prompt-eng/)for live updates to my thinking

This was a very helpful overview, thank you. 100%, with open source, the doors get blown "open" in these early waves of experiments, widening the range of uses, but also bottlenecks to widen (UX, upskilling) and gaps (e.g. security) to seal, across all the worldbuilding unfolding among a growing legion of "no names".

EleutherAI's GPT-Neo and GPT-J models, code, and weights was released under an MIT license and GPT-NeoX-20B was released under an Apache 2.0 license. These are open source licenses and substantially predate Whisper and BLOOM, which you credit as being the first.
