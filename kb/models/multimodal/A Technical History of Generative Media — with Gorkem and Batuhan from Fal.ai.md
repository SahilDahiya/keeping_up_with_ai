---
title: A Technical History of Generative Media — with Gorkem and Batuhan from Fal.ai
topic: models
subtopic: multimodal
secondary_topics:
- inference/serving
summary: Technical history of generative media with Fal.ai, covering model serving
  and media-generation infrastructure.
source: latent-space
url: https://www.latent.space/p/fal
author: Latent Space
published: '2025-09-05'
fetched: '2026-07-11T05:16:44Z'
classifier: codex
taxonomy_rev: 1
words: 13700
content_sha256: 29000f3cdeca9793422e661fcd2b874fdba55c710bd4e06a1f6383d81df76ecf
---

# A Technical History of Generative Media — with Gorkem and Batuhan from Fal.ai

# A Technical History of Generative Media — with Gorkem and Batuhan from Fal.ai

### From Stable Diffusion to Veo3, why generative media is completely different than LLM inference, and how to scale to $100M ARR while writing custom kernels

[Applications for AI Engineer ](https://apply.ai.engineer/)[Code](https://apply.ai.engineer/)[ Summit](https://apply.ai.engineer/) (**Nov 20-22 in NYC**) are [now open](https://x.com/swyx/status/1964021608198324587).

**Generative Video** has been one of the big trends of 2025. The space has completely exploded and we are even seeing it in mainstream media, like the [Kalshi ad](https://x.com/PJaccetturo/status/1932893260399456513) during the NBA Finals. We made a whole episode on that with the [Moore twins](https://www.latent.space/p/hyperstitions-of-moloch)!

Today, we are covering the unsung heroes that power inference for many of these models: ** Fal.ai **(including some well known closed source image and video diffusion models). They are on track to add

**~$100M of new revenue this year alone**, with video becoming an increasingly high percentage of it. But only 2 years ago they were instead building a tool for

[dbt](https://www.getdbt.com/)data pipelines!

Fal now hosts >600 models on their platform, powered by >100 custom CUDA kernels to improve performance. We tried to use this podcast as a way to recap the history of generative models, and what was a big inflection point in their history. Enjoy!

## Fal’s Model History

*See all links below in the show notes.*

**Stable Diffusion 1.5**

- The first major hit for Fal when they pivoted to hosting optimized inference
- Became very popular with extensive fine-tuning ecosystem
- Still used today with LoRAs due to being fast, cheap, and reliable

**Stable Diffusion 2.1**

- Described as "a bit of a flop" that didn't get much attention

**Stable Diffusion XL (SDXL)**

- First major model to bring FAL their first million in revenue
- Exploded the fine-tuning ecosystem (LoRAs)
- SDXL Lightning: A distilled version by ByteDance for faster generation

**Stable Diffusion 3 (SD3)**

- Had "some drama around it"
- The team left Stability to form Black Forest Labs

**Flux Models (Black Forest Labs)**

- First to breach the barrier of "commercially usable, enterprise-ready" models
- Drove FAL from $2M to $10M revenue in first month, then to $20M
- Three versions: - **Schnell**: Apache 2 licensed, extremely distilled, 4-step generations for lower quality
- **Dev**: Non-commercial license with revenue sharing
- **Pro**: Requires collaboration for hosting


**Gemini Image Models**

- Google's autoregressive image models, considered underrated

## Image Editing Models

**Flux Context (Dev)**

- Released late May
- Popular editing model

**Qwen Image/Qwen Imager**

- Released two weeks before the podcast
- Now topping Flux Context Dev
- Very good text-to-image when using single frame from video model

**Stepfun's Hydream**

- Image editing model from smaller Chinese lab

**VivaGo**

- Another editing model from Chinese labs

## Video Models

**Sora**

- OpenAI's model that showed what was possible
- Motivated researchers but was surpassed within months

**Veo3 (Google DeepMind)**

- Created "usable text-to-video component" with sound
- Very expensive to run
- Excellent at conversation, timing, lip-sync
- Also functions as one of the best text-to-speech models

**Hun Yuan Video**

- Chinese model, considered "pretty good"

**Mochi (Genmo)**

- Quality wasn't quite there initially

**One (Alibaba)**

- "Insanely good model"
- Newer version released recently
- Can run 480p draft mode in under 5 seconds
- 720p full resolution in 20 seconds (aiming for 10)

**Minimax**

- Chinese video model partner

**Kling (Kuaishou)**

- Chinese video model partner

**Movie Jam**

- Research paper arguing MMDiT architecture is unnecessary

**Multitalk**

- Post-trained version of One
- Good for conversation but lost generalization ability
- Only does talking faces

## Audio/Music Models

**PlayHD/PlayAI**

- FAL helps optimize their inference
- Some use autoregressive models
- Some use diffusion-based approaches

**Notorious**

- Known for diffusion-based audio generation

### Show Notes

### Timestamps

- [00:00:00] Introductions
- [00:04:29] History of Major AI Models and Their Impact on Fal.ai

- [00:07:06] Pivoting to Specializing in Diffusion

- [00:10:46] Writing CUDA Kernels

- [00:15:50] Latency importance and A/B testing results with customers

- [00:17:56] Influence of open model availability on Fal's growth

- [00:19:00] Working with closed source model providers

- [00:21:19] Inference optimization for audio and music workloads

- [00:29:10] Performance improvements for video generation

- [00:29:47] OpenAI and Gemini's autoregressive image generation

- [00:34:45] World models for controllable video generation

- [00:36:26] Rise of Chinese open-source video models

- [00:39:30] Monetization strategies & revenue sharing

- [00:42:48] NSFW content moderation and enterprise content safety

- [00:45:10] Trends in startup launch videos and generative video adoption

- [00:46:59] LoRA-based customizations

- [00:47:11] ComfyUI, chaining models, and enterprise workflows

- [00:51:58] Applications of Generative Media

- [00:54:15] Requests for Startups and Future Opportunities

- [00:56:34] Ideas for building startups on top of Fal

- [01:00:29] Hiring and Team Building at Fal.ai

- [01:03:27] What makes a cracked engineer

## Transcript

**Alessio** [00:00:03]: Hey everyone, welcome to the Latent Space podcast. This is Alessio, founder of Kernel Labs, and I'm joined by Swyx, founder of SmolAI.

**Swyx** [00:00:09]: Hello, hello. Today we're so excited to be in the studio with Gorkham and Batuhan of FAL. Welcome. Yeah, thanks for having us. Long time listener, first time caller.

**Swyx** [00:00:21]: Gorkham, you and I actually go back a long way to when it was still features and labels, and you were just coming out of Amazon. I don't even remember the pitch. I honestly should look at my own notes, but you were optimizing runtimes.

**Gorkem** [00:00:33]: Yeah, it was first like we were building a future store, and then we took a step back, and then we decided to build a Python runtime in the cloud. And that evolved into an inference system that evolved into what FAL is today, which is a generative media platform. So we optimize inference for image and video models and audio models, but we do a lot more. We try to own this whole generative media space for developers, basically.

**Swyx** [00:01:01]: Yeah, amazing. And we can talk about. That journey. I wanted to also introduce Batuhan. We're newer to each other, but you've come to some of my meetups before. You're head of engineering.

**Batuhan** [00:01:09]: Yeah, I lead engineering here at FAL. You know, I'm glad to be here.

**Swyx** [00:01:14]: And what's your journey?

**Batuhan** [00:01:16]: I met Burkay in 2021 when they were just starting the company. And like just before the seed round, you know, Burkay and Gorkham, we met online. We're both Turkish. So I think that was a connection. We just met and then they said, oh, why don't you join us? And like, I was one of the core developers of Python language. So I had like really, you know. Really good experience with developer tools around the Python language. So I started coming here to build the Python cloud, which evolved into this like inference engine and the generative media cloud that we're building today.

**Swyx** [00:01:43]: And now you spend time, less time with Python and more time with, I don't know, CUDA, custom kernels.

**Alessio** [00:01:50]: And yeah, yeah, yeah. Yeah. Remember the DBT FAL when the modern data stack was out. Can you guys maybe just give a quick sense of the scale of FAL? So you just raised a hundred twenty five million dollars. Seriously. That's correct. We're going to talk about. Yes. That's how I passed on one of your early rounds. We can go through through that. How many of the developers, how many models do you serve and maybe any other cool numbers?

**Gorkem** [00:02:11]: Yeah, we have around two million developers on the platform and like for the longest time we required GitHub login. It recently changed. But so I'm assuming everyone who has a GitHub account as a developer and we have around three hundred fifty models in the platform. These are mostly image, video and audio models. It used to be only image and then we added audio and the space evolved into video as well. And yeah, that's that's pretty much the scale. We just closed, announced our series C round and we've been growing a lot in the past year and it's still continuous. Yeah.

**Alessio** [00:02:50]: You had a very nice series C party and you guys are over a hundred million in revenue, right? Just this is not, you know, just developers kind of kicking the tires. That's correct. Yeah, that's great. When you say three hundred fifty. Models, I think what percentage of all the models that you could serve is that because, you know, especially in any.

**Batuhan** [00:03:08]: Infinite amount of iTunes post-trained versions of these models, we are trying to serve the models that fix a gap, you know, that fill a gap in the stack. So we don't add a model that's like significantly worse in any aspect compared to other models that we have. We are trying to bring unique models that solve a customer's needs. So that's like these are three hundred fifty models. You know, there's like twenty, thirty text image models, but like one of them excels in logo generation. Another one. Excels in human face generation. So like every model has a unique personality. But if a model is like significantly worse in all aspects, we don't add that to the platform. So there's like infinite amount of models that we can add. And do you rely on your own evals or just like what the community tells you? We mainly rely on our own evals as well as, you know, like we are in the community. So we also like follow the community very well to see like what what is going to be the thing that's going to be in the next generation of apps. So if you think something like we have a good intuition, if you think something is going to pop up, we just add it. Yeah.

**Swyx** [00:03:59]: To my knowledge, you haven't published your own evals, right? No. No, we don't. It's internal. And then the community is Reddit, Twitter?

**Batuhan** [00:04:05]: Twitter, Reddit, you know, Hugging Face, seeing how popular the models are in Hugging Face and other demos. Okay.

**Gorkem** [00:04:12]: I just want to give people a sense of where to get this info. The best part of the job is the day of a model release, the adrenaline rush that comes with it, the whole team trying to scramble something together and release it. And it happens every week. Right. Every week is exciting.

**Alessio** [00:04:27]: Can we do maybe a brief history of like the models that were like the biggest spikes? Maybe usage, you know, you kind of, I think everybody knows stable diffusion, you know, and then you have maybe like the Flux models and then you have Black Forest Labs. You have like all these different milestones.

**Batuhan** [00:04:40]: History-wise, I think the biggest, like the initial hit was stable diffusion 1.5, which is when we actually pivoted into this new paradigm of fall. Generative media cloud. We started hosting it. We noticed like we had the serverless runtime and everyone was running the stable division 1.5 by themselves. And we noticed it's terrible for utilization and they are not optimizing it. So let's just offer an optimized version of this that's ready for API 2.0. It has to be scaled and doesn't require people to deploy Python code because we want product engineers to start using it. We want mobile engineers to start using it. So we started offering stable division 1.5. It was very popular. The fine tunes around it was very popular. Stable division 2.1 came. It was a bit of a flop, so it didn't like, you know, got that much attention. And then STXL came, which was like the first major model that brought like our first million in revenue, if you consider that. And with STXL, obviously like the small fine tuning ecosystem also like tried to explode. People started fine tuning their faces, their objects, whatever, and generations with this, like LORAS started to become very popular. And then after stable division XL, there was like a bit of a quietness around it. You know, ST3, there was like some drama around it and the team at Stability left to start Black Forest Labs, which released Flux models. And that was the first model to reach the barrier of commercially usable, you know, enterprise-ready great models, where in the first month of Flux models, we reached from like 2 million to 10 million in revenue. It was like a big jump. Next month, we were at 2.8 million. Like it just started going from there. And then video models started, came around, you know, we partnered with Luma Labs, we partnered with other video model companies in China. We partnered with Kling, Kuaishou, Minimax, and with these models, like, you know, it created another market segment that was a big jump. And this, the final biggest thing was VO3, where it actually created this like usable text-to-video component, where before text-to-video was like a very boring, soundless video that you would like, you would not get enjoyment out. Whereas now it's like a, such a great experience. You can create all these like memes that you're seeing online, all these ads. So that was like another big jump for us, like partnering with Google, DeepMind, for VO3.

**Swyx** [00:06:41]: Yeah, actually that's a really good history of generative media, that soundbite. So I wanted to double-click on that because obviously we can, we can dive, I think everyone's interested in video, but there's a whole history of the image side that I wanted to cover first. Just definitely wanted to start with was just the decision to pivot. I think I just want to double-click on that, you know, it's not a trivial decision, but obviously the right one. At the time, I would say like a lot of people were hosting stable diffusion, right? So it wasn't obvious that you can just build an entire company around effectively just specializing in diffusion and inference. What gave you the confidence? What were the debates back and forth?

**Gorkem** [00:07:16]: Yeah, a couple of decisions we had to make there. We could have evolved the company into more towards GPU orchestration. And like, essentially we had this Python runtime, we were running it on top of GPUs, like that could have been the company. But we saw everything. Every single person, every single company who are using what we had, like a little SDK to, to run Python code on GPUs, they were doing the same thing. They were deploying a stable diffusion application, maybe using some LORAs on top of it, different versions of it, in-painting, out-painting, things like that. I mean, it was very wasteful. We decided, okay, this needs to be an API where we actually optimize the inference process and everyone benefit from it. And like, you can run it multi-tenant, you know, DTools.io. And like, you can run it multi-tenant, you know, DTools.io. And like, you can run it multi-tenant, you know, DTools.io. So that was the decision number one. And then obviously after stable diffusion, I think like four or five months later, Lama 2 came out and there was a decision point again. You could do language models. Exactly. And a lot of the inference providers at the time, there were maybe a couple of them, and they all went all in on language models. And we decided language models, hosting language models is not a good business. At the time we thought, okay, we are going to be competing again. We are going to be competing against OpenAI and Anthropic and all these labs. Turned out that it was even worse because the killer application of language models is search and you are competing against Google at the end. And Google can basically give this for free if they can, because it's so important for them and, you know, it threatens their business right away. And with image and video models, it was a net new market. We weren't going against any incumbent. We weren't like trying to get market share. We were trying to get market share from someone much bigger than us. And we liked that aspect of it. We thought we could be a leader here. It was a niche market, but it was very fast growing. So we chose to be a leader or play to be a leader in this fast growing niche market rather than trying to go against Google or OpenAI or Anthropic. So that was the decision we made. And turns out it's a good one because we are able to define the market we are in and educate the people and grow with it. And so far it's been growing fast enough that we were able to build a whole company around it.

**Swyx** [00:09:37]: Yeah, and I think you noted at AIE that, you know, now there's a generative media track, generative media specialist investors. Thank you for calling it generative media, by the way. Yeah, I mean, obviously it's a thing and people care about it. And I do think it's going to change the economy. And as a creative person, I think I also wonder what's going to do for us. Just so I want to keep it technical and keep thinking about the pivot, because I think it's still like one of the most interesting pivots I've seen. And in the AI era, you were not CUDA kernel specialists at the time, right?

**Batuhan** [00:10:05]: I come from a compiler's background. So my my job was optimizing, you know, like Python bytecode interpreter to make stuff faster, which is performance engineering. And like, yes, like I don't think at the time there was that many CUDA kernel specialists either. So it's like we were at like the right time. You know, it was like, actually, like the space was actually so, so much worse than what we have today, where like the running basic stable division 1.5 was like a unit with convolutions and the convolution performance on AI was like you're getting like 30% of the GPU power if you just use rough touch because no one cared about it. So there was like so many low hanging fruits that we started to pick up and started optimizing and it kind of evolved, evolved, evolved. Right now, it's like much more competitive space with like NVIDIA is like a 50% 100% kernel team that's writing kernels. You're competing against that at the time. No one cares. No one really cared about it. So it was like a good new field for us to go thrive. And there's no community effort like a VLM.

**Gorkem** [00:10:57]: Not exactly. When these models were first released, like no one in the world has ran them in production. Like it just didn't exist. It's like a research output. Exactly. Yeah, it was stability. Yeah. You had your maybe local GPU. Maybe you had like a single GPU that you rented from the cloud. And basically this was a research interest rather than a product interest. And no one at Meta. Meta. No one at Google had run this in production. So we also thought this is a good, good time to start that company around this and actually spend time optimizing it as much as we can, because if we can get millions of people to use this, there's a lot of economical value to be created there.

**Alessio** [00:11:36]: Can you talk a bit about how much of a performance boost you got? Because I know when I met you guys, you were about a million in revenue. You were like, well, we're writing all these custom kernels and maybe part of it is like, okay, how many kernels can you actually write? Sure. You know, as you as you support. For all these different models, like what's kind of like the breadth of them? Like, are you writing kernels that you can reuse across models? Like how much work do you have to do on a per model basis?

**Batuhan** [00:11:59]: It really evolved in the past three years. You know, when we first started, there was a single model, stable diffusion 1.5. So every all of our kernel efforts were how do we make stable diffusion 1.5 as fast as possible? You know, you go from like 10 seconds with PyTorch at the time, there was no, not even like a torch compiled torch inductor or whatever. So you were going from 10 seconds to maybe like two seconds on the same GPU. Uh. And. And like, we, we started with that, the next thing, like, you know, the, like with, with adding more models, you know, like stable diffusion, Excel was a different architecture. PicsArt was a different architecture. All these like different architectures started coming around. We said, let's build an inference engine, which is what we call a collection of kernels, parallelization utilities, diffusion caching methods, quantization, all that stuff combined into one package. And so we built this inference engine, uh, the same time PyTorch 2.0 was released with Torch inductor and Torch Dynamo to do like Torch compiled, which is like essentially a way to trace the execution of, of your neural net and generate Triton kernels that are fused, like that are more efficient. And I'm a big sucker for just-in-time compilers. I used to work at PyPi, uh, like a just-in-time compiler for Python. And we said, this is a great idea. Let's apply this, but a more specialized, more vertical way for diffusion models. At the time it was Unets. Now it's diffusion transformers. Which are significantly different than your auto-regressive transformers in terms of like the profiles of like how compute bound it is, what sort of the kernels are taking the majority of the time, you know, if you're doing bidirectional attention or causal attention. So we started doing that. And now it's like, what we have today is a inference engine that's like applicable, that gets you like 70, 80% of majority of the models on diffusion transformers. And we still have like a lot of custom kernels for a lot of models to squeeze out, like, because they're still, still small. Every model wants to make an architectural difference. You guys see this on like, you know, even for stuff. Like, you know, Kven, DeepSeq, whatever people want, like, even if we know an architecture is the best, they want to tweak it a little bit just to make sure, oh, we are releasing something cool. So we, we saw this. And then like, for that, we have to write like custom kernels for custom RMS norms that people are doing or whatever, like stuff like that. So we, we have, we have a decent amount of kernels, like over a hundred of custom kernels. This doesn't include the auto-generated ones. You know, we have templates of kernels that generates like, you know, for thousands of different shapes, problems, spaces, whatever. But like, if you consider those, you know, like we have tens of thousands of kernels, obviously. At runtime that we are running and dispatching, but that's pretty much like the depth and breadth of it.

**Alessio** [00:14:13]: And on average, a model on file runs 10X faster than I would self-host it. Like if I just take stable diffusion, right. And I put it.

**Batuhan** [00:14:20]: I know this might be a bigger discussion point. Do we consider speed as a mod? This, this comes to that. It's like the existing open source industry goes so fast where, you know, like if you go to like, this might have been true three years ago. Now, PyTorch is like already like very, very good for H1N1s, right? What about P200s? When you use PyTorch with P200s, Blackwell chips, you're not getting the best performance. So our main objective and our main goal is for whatever GPU type you're using, these diffusion models, we're going to extract the best performance. At any point in time, it could be 1.5X, it could be 3X, it could be 5X. For certain models, it could be 10X. It would be a bit of an unfair thing to say, oh, we're going to make everything magically 10X faster. No one in the world can do that.

**Gorkem** [00:14:57]: We are lucky that this is a moving target and open source community, everyone catches up. But at the same time, new chips come out, new architectures are released. So we are always ahead of like what's possible, but then they catch up, but we have to stay ahead of it. And that's how we can create differentiation because it's a moving target, because there's so much going on. We are, whenever something new comes up, we are the first one to optimize it, first one to adapt our inference engine to it. So at that time, the fastest place to run it, that helps with margins, things like that. But eventually people do catch up. I think it's very hard to create this differentiation over launch. So it's like, oh, we're going to do this long term if there is no new architectures, if there's no new chips. But luckily there is all the time. Yeah.

**Alessio** [00:15:43]: Yeah. And I think with image specifically, you cannot stream a response, so to speak. So when you have a language model, it's like, you're kind of bound by like how quickly you can read. So even with like rock, it's like, it's impressive to show a thousand token a second, but it's like, I'm not reading that fast. Right. So it can go slower versus what images it's like, you just need to see it. That's why mid journey now has like the draft mode. For example, it just gives you this. It's like very low quality resolution. Yeah. But at least you can see whether or not it's going in the right direction. How much of that is actually true for like your customers? What do they care about the most? Like it's latency that important. Like what's the range of latency that matters? Yeah.

**Gorkem** [00:16:20]: Latency is really important. One of our customers actually did a very extensive AB test of like they on purposely slow down latency on file to see how it impacts their metrics. And it had a huge part in it. And it's, it's almost like page load time when the page load slower, you know, you make less money. I think Amazon famously did a, did a, a very big AB test on this. It's, it's very similar. Like when you, when the user asks for an image and, you know, iterating on it, if it's slower to create, they're less engaged, they create fewer number of images and, and things like that. Yeah.

**Swyx** [00:16:56]: It's the same learning that Amazon has like every, you know, 10% improvement in speed. Yeah, exactly. It's the, the elasticity is high. The other thing I wanted to also dive into, you know, like I putting my, a little bit of the investor hat on one of the reasons for file success is kind of with not within your control, which is how, when, and how people reduce release open models for defer diffusion, which like at the time it was just stability and like, there wasn't, there was no Chinese, you know, I'll put, I mean, what we, we did have other image models, but they were not great. Yeah. And like, and so, so you, you made a bet on when it was just like, wasn't super obvious, but then the other thing is, which is what you're touching on. The diffusion workload is very different from the language workload and the language workload is being super optimized, whereas diffusion is not. So you, you just like had kind of no competition for a while, which is fantastic for you.

**Gorkem** [00:17:44]: A hundred percent. And like the open source, we benefit a lot from it, obviously, but like in the, in the past six months, a year, we started working with some of the closed source model developers as well, like behind the scenes, helping them. But they're not sending you their weights.

**Swyx** [00:17:58]: They do. They are. They are. Wow. Yeah. What do you have to give security?

**Batuhan** [00:18:02]: Like guarantee them? I mean, we are any cloud provider, like what, what, what, what do they think in like AWS or Google cloud or these new classes? There's like 50 new class, right? Like we, we are not that different from any other cloud provider. And this is why we package the inference engine in a way that, you know, they can self-service and get 80%, 90% of the performance. So they don't even have to show us like their code. They deploy to our, we have our own cloud platform where our inference engine is available only in that platform. So they can tap into that when they deploy their code and their model weights to us. And we don't really have to look at it. If they want to collaborate with us, which some companies did in the past where we would just essentially, we have performance engineers acting as forward deployed engineers on their behalf and writing custom kernels for them. Okay.

**Swyx** [00:18:43]: Have you disclosed who you're doing this for?

**Batuhan** [00:18:45]: We disclosed PlayHD, PlayAI. That was one of those. We have like four different companies, four major video companies that we are doing this with and one image company that I don't think we disclosed. Yeah.

**Gorkem** [00:18:56]: As you can imagine, it's a little sensitive for them. So yeah. Yeah.

**Swyx** [00:19:00]: I would say like, so like. Yeah. So like a couple of years ago, when sorgenoplicate started serving V03 models and we were like, okay, are you just wrapping their APIs or something? And I think so. It's not obvious like how much integration there is going on and how much this on your infra or like your tech.

**Gorkem** [00:19:13]: Just to be honest, like some of that is happening too. Yeah. V03 like, I think everyone is. It's just API wrapper. Yeah.

**Batuhan** [00:19:19]: It is. Yeah. You have a dedicated pool that you can serve to your customers with like different speed SLA guarantees, whatever. Okay. It's like how it would work for something like V03.

**Swyx** [00:19:27]: But your objective is to be one-stop shop.

**Batuhan** [00:19:32]: Thank you so much for having me.

**Swyx** [00:20:02]: Thank you so much for having me.

**Swyx** [00:20:50]: Thank you so much for having me. Thank you so much for having me.

**Batuhan** [00:21:30]: Thank you so much for having me.

**Batuhan** [00:22:00]: Thank you so much for having me.

**Batuhan** [00:22:30]: Thank you so much for having me. I see, I see. It's a separate product. Yes.

**Alessio** [00:22:32]: From a GPU perspective, do you always need to be on the latest? You keep mentioning H100s.

**Batuhan** [00:22:37]: Majority of our workloads are in H100s because price-per-files, it makes sense. But BlackVal is obviously, we have five people dedicated to writing BlackVal kernels right now to make sure we can, because theoretically it looks good, right? Like flops dollar-wise, it makes sense. But can you reach that actual flops? No. So we have a dedicated team that's working with NVIDIA directly to write custom kernels for BlackVal for diffusion transformers. To get to the, to get to the point where it makes perf dollar make sense. And then, then we would start with our own workloads as well as some of our foundation model companies. We would ask them, oh, if you want to migrate to BlackVal, here's an inference stack that already works.

**Gorkem** [00:23:11]: We are at that point where we should be the ones pushing the boundaries on BlackVal because no one else is doing this work. And maybe it doesn't make sense economically right now, price perf-wise, but we know it can. So we are like working towards maybe like a couple of months away from that point. And then whenever it does, we'll probably, you know, we'll be able to do it. We'll probably switch as many workloads to BlackVal as, as possible.

**Swyx** [00:23:33]: Just to be super crazy. When does it make sense to just work on an ASIC?

**Batuhan** [00:23:38]: I don't think it does. That's like honest opinion. You know, like the people, this is like one of the most controversial topics, right? Like is, is, is all these like ASICs a great idea? If you're like S-RAM, if you're memory bandwidth bound and like you can put all of S-RAM, is it like even economically viable at that point? I don't know. But like the summits are around like this, this chip design. So you see like, okay, what is the overhead of an NVIDIA GAM instruction? Right. It's like 16%. So like you're essentially buying a metrics and multiplication machine. So at like, it doesn't really make sense to specialize it that much. And like some of the, like, like B300s are going to have like a better softmax instruction that gets like 1.5x, whatever. And like, that might be one way where NVIDIA gets like, you know, better performance out of the majority of like, for the majority of workloads, which is like attention heavy stuff. I think it might make sense for like NVIDIA to like add more specialized stuff, but like for us, I don't think it will ever make sense to.

**Swyx** [00:24:30]: Build I6. Just thinking about from first principles that the diffusion workload is very different, but also obviously there's still a lot of changes in the architecture that you need to just general purpose.

**Gorkem** [00:24:40]: We don't have a single model where we are trying to optimize. We are trying to do it for the newest, the best, like always. The flexibility is therefore really important.

**Swyx** [00:24:48]: I was going to show, I'm going to pull up the Quen MMDIT, where there's like this dual streaming thing, which I last, I think SD3 had it. Yes, SD3 Flux. Yeah. Is that the standard, standard model now? MMDIT.

**Batuhan** [00:24:59]: So it's also a controversial topic, you know, scaling rectified flow of transformers paper, the SD3 paper came up with this architecture. And then one of our research team actually, like Simo Raya, he's like our head of research, he found out that like just using MMDITs are inefficient. You need to mix them. And now there's like controversial opinions, you know, like movie jam paper were saying, oh, MMDIT is completely unnecessary. You can just use a single stream DIT, whatever. So like there is like controversial opinions happening in terms of architecture changes, which I understand because everyone wants to do a different architecture. No one wants to use the same architecture because it's lame. Yeah. Yeah. Otherwise, like it's just a matter of compute and data and these researchers don't feel proud that their model is an output of data and compute. They want to make a novel research change. So I think the architectures is going to keep changing until this like paradigm of like, you know, researchers changing stuff for the sake of changing, you know, features.

**Swyx** [00:25:47]: I'll talk about a couple other architectural things just to keep it bounded within this topic. The distillation was a thing for a while. SDXL Lightning, you guys did fantastic demos of Tail Draw, which we've also had it on podcasts. Fantastic episode. What happened to those things? How come they're not popular anymore?

**Gorkem** [00:26:03]: I think it makes for a good demo. You know, you could build real time applications, you could build these drawing applications, things like that. But I don't think people could build applications that like have user retention long term. Like people couldn't really build useful things with it.

**Swyx** [00:26:19]: Let me play out what I thought was going to happen. And then you tell me why it didn't happen. Sure. Which is consistency models for drafting. It's like you use your pen to draw. You draw things and it creates the draft. Then you upscale, right, with a real model. But like, that's it. Like, why can't it be a two stage process instead of one stage? Yeah.

**Gorkem** [00:26:39]: And I think one thing that happened is Flux, like that generation of models were not good at image to image when it first came out. So like you need a good image to image model to be able to draw. Maybe it needs to be revisited around this time with some of the editing models, maybe. Like image to image and control. That's Flux.

**Batuhan** [00:26:58]: Like Excel or Controllers were very popular, where like people were used to do this stuff, like sketch to image, whatever. And like with Flux, I think people cared less about it. One thing that I keep thinking about this is like, is this true for LLMs too? You know, like I always default to cloud 4.1 Opus, right? Even if it's slower than Sonnet, it's just like, I know I'm going to get the best quality. Exactly. That's what's happening here. Yeah. That is, it seems like what's happening here as well.

**Swyx** [00:27:22]: As a, okay, anyway, as a creator, I want fast, quick drafts and then, and then I can refine, right? Like, so. I don't know. I don't know why it didn't happen.

**Gorkem** [00:27:29]: More true for video models, right? It used to be like five minutes, four minutes for a single five second generation. Now it's mostly under a minute, but you want 10 second, five second generation. And then because the workflows of like creatives, when they're working with it, they generate a ton of videos and then like pick one and then create a story around it. So then when you watch these people actually generate videos, they generate like hundreds at a time and they have to like, kind of sit around it. And then wait, and then like iterate on it. Like the faster speeds mean a lot for creators.

**Swyx** [00:28:05]: Yeah, it does. The other thing I wanted to also briefly touch on before we go back to the main topics is the autoregressive models, which you mentioned, right? Like, obviously, I honestly, I still think Gemini is underrated because they were first. And then, but then obviously, openly, I did the 4.0 image gen and that was a huge thing. I actually even wonder if there was a panic for you guys, because obviously it's like, this is Soda image gen and like no one else has it. It's not, it's not open source.

**Batuhan** [00:28:30]: Have you passed through those eras so many times?

**Gorkem** [00:28:34]: Stopped worrying about it.

**Batuhan** [00:28:35]: Your camera's like good stories around Dolly.

**Gorkem** [00:28:38]: Yeah, I mean, I talk about this how like when Dolly 2 first came out, I was like, okay, open AI is so far ahead of anyone else. Like it's impossible for mid-journey and then people caught up within months and then stable diffusion was even maybe better. Or just as good as Dolly, like a couple of months later and it was open source. So like a year later, same thing happened with Sora. Like they, they put out those videos and that time around, like, I think we were excited because now that people see that it's possible, like this is like actually doable. Researchers get motivated and they see the hype. They see that this is possible. So they work on it. And within a couple of months, we had maybe not Sora level, but much better video models. Now we have video. We have video models that are much better than Sora. So whenever we see someone actually pushing the frontier, it's a reason for excitement because now that's possible. Other people are just going to do it within a couple of months. So you don't panic anymore.

**Alessio** [00:29:38]: Is the fact that Anthropic doesn't have an image generation model tell you anything about what the larger labs care about?

**Batuhan** [00:29:44]: It tells more about Anthropic's own like priorities than like the in general, like what the other labs, because if you look at XAI, if you look at Meta, if you look at open AI, it's like, if you look at Google, they all have really good image models. Yeah.

**Gorkem** [00:29:58]: Google in their last announcement, they use the word generative media, by the way, which was a proud moment for us. It's a win. And a lot, and you know, they focused on generative media as much as their new LLM models. So some labs definitely care about it and some labs, it's not a priority for them. Look at XAI. They keep pushing like image language. AI slob. Yeah, I know.

**Alessio** [00:30:19]: I know it's crazy. And waifus. And levels of interactivity. You have images, you have video. Now you have Genie, this kind of like more a world model, you have kind of like gaming applications of that. How far are we from like file getting a lot of traffic on, on those models? Like, is it mostly experimental today in open source? Obviously Genie is impressive, but like it's a Google model, you know?

**Gorkem** [00:30:39]: I have a very optimistic take on this and that may be like a normal outcome. I think at worst, we are going to have very capable video models that come out of world models, right? It's going to be a very controllable video model and the use cases will be. Similar to what video models are. You're going to create content, but you're able to control the camera angles. You're able to control the video model a lot better than what you can do today. At worst, we are going to get that from world world models. And at best, I think it's very hard for anyone to predict what's going to happen. Yeah. Movies and games. Like it's going to be something in the middle where you can be, be part of a whole movie universe that's going to be playable. So it's boundless possibilities. What's, what's going to happen at best and how affordable is it going to be? Like, is this ever going to reach, uh, you know, mainstream adoption? We'll see all that, but it's definitely technically incredibly exciting and impressive. What's, what's coming out of these labs. Yeah.

**Alessio** [00:31:42]: I need to find the paper again, but, uh, there was this study on like, um, video models and like image generation, understanding physics. Yeah. And like, it could like predict the orbit of a planet, but then when it actually had it draw out the gravitational. Yeah. forces, it was like completely wrong. Yeah. You know? And so I, I think like, that's my thing with world model is like, I understand the creator application, which is how you can create consistent world. But I don't know if like the other side of people that are like, Hey, these are like the best way to like simulate the world and like get intelligence and things like that. I don't know that.

**Gorkem** [00:32:10]: Optimism around the two, because whenever you talk to someone who's working on robotics, they're bottlenecked by the amount of data they have. And from all these, you know, past three years of AI innovation, we've seen that. Right. But whenever there's an abundance of data, that type of models actually like improve a lot and you see, so like robotics, we expect something similar whenever they figure out this data problem, those models are gonna get better as well. So that's why people are so optimistic. Okay. Maybe this solves the robotics data problem and it's yeah. Bondless opportunities there.

**Batuhan** [00:32:46]: And regarding like the, the, the example you mentioned about gravitational forces is like, I think this is still the same problem as, oh, LMS can't do 9.5. 9.9 plus like nine, nine point. Yes, it can. It's like, you just need to train it with more data. You need to have a better tokenizer. It is the reason, whatever. It's just a matter of like data scale and like the underlying fundamental architectures. But like, I don't think it's going to change that much. We just like, we're going to put thousand X more data, thousand X more compute, and we'll get like the best physics simulators. And I think this just should be possible with the existing signals coming from the data.

**Swyx** [00:33:18]: Just to double click on video stuff as well. Yeah. Uh, you had a great slide in AI. At AI where you're like currently 18% of files revenue comes from video models and it might be a, that was February.

**Gorkem** [00:33:29]: So now, now it's probably over 80, 50, 50. Yeah. Okay. It's like over 50. Yeah. Yeah. A hundred percent. Wow. Okay. I guess editing models brought some life into the image as well. So like both of them grew, uh, but yeah, video grew faster.

**Batuhan** [00:33:46]: Video is like pretty, pretty significant. And the, the, one of the main drivers is open source models where, you know, in February. There was who knew on video, I think that was like pretty good. There was Mochi from Genmo, uh, but like the quality still wasn't there. And one from Alibaba was like insanely good model. And they released a newer version of this in like a month ago, I think, or like a couple of weeks ago. And now it's getting so, so popular. And like, we can run this, I'm all like for like four ADP, like the draft mode version, we can run it like five seconds under five seconds. So people can have like instant feedback loop. And then when they want to go to seven 20 P like full resolution is just like 20 seconds. I mean, we were planning to bring. It down to 10 seconds. Yeah.

**Swyx** [00:34:25]: That's amazing. Uh, and I want to double click on that for a while. I was kind of bearish on Alibaba because they kept releasing papers with very cherry picked and like, it was like a, it was like, okay, we're on GitHub. And then you go to GitHub. It's a read me.

**Gorkem** [00:34:37]: Like, I mean, you, you can't see something really changed. They've been, what happened to them?

**Batuhan** [00:34:45]: No, no, we haven't talked to them, but like, it seems like, and now there's like competing teams inside Alibaba, you know, one is a really good image model, but they released. As a, as a competing image model. Like, you know, we think like once image model is actually very, very good. If you'll do one with single frame, instead of like 81 frames or whatever, you get a really good text image model out of it. And this is just because of the pure amount of data that you put from the videos. So now there's like, you know, Alibaba has like two, two of the really good models, like from their lab. And then there's like smaller labs in China that like, you might not hear about, but like step fun, they, they released like an image editing model. Hi dream. We want to go like that. Like, there's like all these like small labs. They're releasing because I don't think training these image or editing models are that expensive. And video models might be like slightly more expensive. My guess is like training these costs like a couple million dollars, which is not that much, especially, you know, like, you know, they're probably backed by some sort of entity, you know, like other than Alibaba, you know, like there's, there's like Stefan, whatever they probably raise a really good amount of money. So training these models will bring you a lot of attention and it's more attention that you would get releasing a subpar LLM because like LLM space has so much more competition. So just training this for like a million dollars, a video model, and then releasing it, I think that brings you a lot of attention.

**Gorkem** [00:35:57]: It is a hack. When you look at Hugging Face, let's look right now. I'm sure the top models are image models. Like it's quite an image editing probably is, is probably up there. Yeah. Probably up there.

**Alessio** [00:36:08]: Number one, number one. Yeah.

**Batuhan** [00:36:11]: Hunan Gamecraft is number three, number four, number four, Gemma, 270 million, some image stuff. ByteDance has an open source, but they have a really good team seed. That's their new lab there. They're working on seed. Seedream, Seedance, OmniHuman, like stuff like that. We have a good, good, good partnership going with them to hopefully, you know, have their models hosted in the US as well. Yeah. And the idea is, you know, like, I think that the team that they, they were able to assemble is very good and it's coming from, you know, their previous researches, whatever. Like ByteDance was doing a really good open source stuff on like SDXL Lightning. They, they released like SDXL Lightning paper, Animative Lightning. So I'm, I'm pretty, pretty hopeful about them. Yeah.

**Swyx** [00:36:47]: First of all, you know, hopefully they, they don't reach out to you when they, when they launch, they just drop it and then you have to rush. Okay.

**Batuhan** [00:36:53]: So at this point, like people reach out to us because like we, we, we, we, we are the market leader.

**Swyx** [00:36:56]: So like they, they just like reach out to us for like the getting distribution. Yeah. There's a Chinese platform that they always launch on first, which I forget the name of it, but like you have to. We, we, we all also get like day zero launch with the majority of these models. But like, so, so basically I think the question is always like, you know, you are the ones making money. Stability did not make money from stable diffusion.

**Batuhan** [00:37:17]: I think the thing that Black Forest Labs did was very, very interesting in this aspect. They released three different models. Yeah. Apache two licensed, extremely distilled model, which is good for dev, uh, Chanel. This is the Chanel version. This is like the four, four step generations for like lower quality stuff. They released a dev model with a non-commercial license where their inference partners are, you know, like you're paying a revenue share with like, and this is like very good way. And then there is a pro version where you can like collaborate for hosting it. And I like the, the revenue share is obviously different for that as well. This is, I think a very smart choice for labs whose whole premise is releasing models. But if you're a company. That is doing a product in the side, you don't necessarily need to make money from the open source models, you're doing it for getting researchers get, you know, hiring people, getting distribution, whatever. So it's really depends on like the company's goals, like for, for Alibaba scale, like they don't care if one model is like hosted in their API, right? Like Alibaba makes a, it doesn't touch the Alibaba top line revenue, whatever one makes. So it's like for them, it's like, it's a no brainer to release it and get attention and maybe like get some leads. So they're Alibaba cloud offerings, but like in general for Black Forest Labs or companies like that, I think it's like a. A smart move to release like a distilled version as like fully open source and then like less distilled or like the actual model as non-commercial and then partner with inference companies and stuff like that.

**Alessio** [00:38:32]: What's the distribution of usage. So like it's 80% of your revenue, like five models, like, or are people really using like the, the long tail of all these open models outside of like the initial launch?

**Gorkem** [00:38:42]: I think like there is some power law, but not as much as you would think. And it keeps changing. That's the other part. Like, it's not like only a single model that's being used. A lot like month to month, it changes a lot. This summer has been crazy. They've been like, like just countless amount of new video models, new image editing models, like the leader kept changing week over week even. But if you like take a step back and look which models are being used, people want to use either the best, most expensive video model, or they want to use like a cost efficient, like good, but cheap enough video model. So those two models are. Usually like used a lot and whatever those models are, it changes week over week. And yeah.

**Batuhan** [00:39:29]: The one good example is like Fox context was released, you know, like on late May and co-edit was released like two weeks ago. And now it's like topping out a context that, you know, it's, it's insane how quickly these stuff transition just because it's, there's a better quality model and that's the value prop. Like you don't have to set up the infrastructure to manage flux context dev as soon as like co-edit is available. You can just switch to that with fall.

**Alessio** [00:39:51]: I mean, it seems to me. That if some models are open and some models you have to pay a revenue share, you ideally want to move the people off the revenue share models into the open models, right? Like what, what's that dynamic? It's all price step.

**Gorkem** [00:40:03]: I'm, I'm also thinking like, okay, we'll do whatever our customers are going to be successful with. We are still like early enough that these small calculations, I don't think it matters. I rather people actually go to production and build products with it and be successful rather than like, okay, 20% here, 10% there. I mean.

**Alessio** [00:40:22]: You're doing a hundred million in revenue.

**Swyx** [00:40:26]: Cool. I'll just ask a few more questions we had around just like the, how people really use this. Okay. I'll ask the super obvious question. Yeah. How much is not safe for work? Almost negligible. Yeah. You don't moderate everything in moderation is optional, right?

**Batuhan** [00:40:40]: Moderation is optional to a level where like illegal content is moderated. And we also track the non-illegal content, NSFW moderation. And like, we haven't seen more than 1%.

**Gorkem** [00:40:51]: Like the models themselves. They're actually not generating that type of content.

**Batuhan** [00:40:54]: So this is like some model providers, especially like, you know, if you look at Black Forest Labs models, the models are not for, it's incapable of generating because it, or like it's annealed in a way that is prevented. So, and like majority of our customer base, like if you look at revenue wise, it's like enterprises are like more on like the higher level of stuff where some of them might be like user space, mobile applications, but you know, like for the last six months, nine months, we've been transitioning more and more to enterprise where it's like less of a need for them.

**Swyx** [00:41:19]: Like less of a option. So what are those enterprises doing? You know, apart from like building a general purpose chatbot that can generate images, maybe Canva, you know, would be like a good use case. But my imagination is a bit limited beyond that.

**Gorkem** [00:41:32]: Advertising seems to be absolutely like growing. And if you think about it, it fits very well. And let's talk about video advertising. So like, I keep repeating this, but some companies talk about, oh, we are going to change Hollywood. Filmmaking is going to be revolutionized. Like, I don't think it's that interesting. Like. How many movies do you watch a year? Like maybe 20, 25 movies. How many movies in the theater you watch? Three, four at most. So if, if there are like thousands of movies that a year, like people won't be able to watch all of these movies. Like there's just not enough time. It's a max quality game. Exactly. Exactly. And with advertising, it's the exact opposite. More content there is the different, like, you know, ways you can create ads, there's always economical value attached to it. So. So you can create unlimited number of ads, unlimited different versions of it, and more personalized it is more, you know, economical value there is behind it. So it adds, it fits really well to this type of technology because there's no limit what you can create.

**Swyx** [00:42:35]: I'll tell you a side comment about a Silicon Valley trend I'm seeing, which I cannot explain, which is that all these YC startups and all these, they're spending between $10,000 to $70,000 per launch video. Yeah. In the age of generative video. Like. They're hiring, you know, actual creative directors, hiring a studio, hiring actors, uh, I was in one of them and like, do you need all that when you have generative video? Like, I think clearly Roy started talking about generative video as well. I don't know if you guys know PJ Ace.

**Batuhan** [00:43:05]: I think he's like the absolute killer for this stuff.

**Swyx** [00:43:08]: He, uh, launched like a, is it a Superbowl ad or something? He did like a basketball playoff, NBA finals, right?

**Batuhan** [00:43:15]: He also did our like series B announcement video, like we're like pretty close with him. And like. It's insane that like what he's able to come up with and how viral it goes, or like, you know, these videos where you spend like hundreds of thousands of dollars, right? You know, like, it's just like, you just need to create viral content and these generative media models are the best way to do it. And we are still at the infancy of this, right? Like, obviously it might not be professional quality. I'd still think like, you know, human in the loop, like mixed, like, you know, content is the way for today, but in six months, who would know like 12 months, I think like 80% of it's going to be generated. Like we were like, we were watching Superbowl and we were like saying, oh, how much of it is going to be generated? And now this video is like AI-generated, it looks like AI-generated, like it could be, right? Like you can't tell.

**Swyx** [00:43:54]: So like, I think at some point, you know, we're going to have like 80, 90% AI-generated, all that. It reminds me of, I think, who's, who's that guy, Fofur from Replicate, obviously he is the best inspiration for all these workflows. He like overlaid some kind of NBA realistic sort of lore on top of game footage. So you could play like NBA 2K, but it looks like a real video. I saw that, yeah. I was like, what

**Swyx** [00:44:21]: It's pretty cool. And so maybe, and that's the other part of my question, and I wanted to get into ComfyUI, which is how much lore serving is going on, right? How much custom? A lot. A lot. You know? Okay. Is it like a majority? That's one of the reasons. Not majority, but like, like if it's like 30%, is it like the majority? And everyone trains their own lores, or you pick it off of like a lore marketplace?

**Gorkem** [00:44:42]: That's why open source works very well with image and video models, because you tap into this big lore ecosystem, everyone. Like. It only, like, I've never seen a closed source model that can create a good lore ecosystem. It just basically doesn't exist. Like maybe there is mid-journey SREFs, but I don't know if you can consider them lores. SREFs are just seeds, right? Conditioning.

**Batuhan** [00:45:06]: Let's call it like another condition, like a prompt. Yeah.

**Gorkem** [00:45:08]: Yeah. And then like only the open source models have these rich lore ecosystems and it's extremely, extremely popular.

**Batuhan** [00:45:15]: But even for like the oldest models, it brings a new life, you know? Like when you see these cool lores. Like you, like there's, we have like still a lot of people using STXL with their own lores because they're happy with the quality. It's fast enough, it's cheap enough. You know, like it's amazing. These models are not single shuttable, like the language models. You can't like, even the editing models, you know, GPT image one or like flux context, whatever, coin image. If you put your face or like, if you put like multiple people, whatever, you can't get the quality. Like it's going to be like 90% there. But if you train for like 1000 steps with like six to 20 images, you're getting like 99% accuracy with like, like the, like we, we worked a lot on like fine tuning the right hyper parameters, like writing like distributed trainers, distributed optimizer stuff. And with those, like people who can train like their lores under 30 seconds now on the platform, run an inference with them in the same job and get like 99% accuracy for the same face character, which is one of the biggest challenges that may be like more on the enterprise side they're facing and less on the consumer side. You know, if you're creating assets. You don't really care who it looks like, but if you, if you are actually like doing a product ad, you want it to like exactly look like the product, every single pixel on the products, you know, banner, whatever you want it to look like that. So you train like a LaCroix Lora with like 20 images. And then like, you know, after that, you're, you're, you have almost a perfect pixel, perfect model.

**Alessio** [00:46:29]: All right. We had to train a Lora for every guest, then we can make thumbnails with the guest doing.

**Swyx** [00:46:35]: Yeah. I actually think that's a very good application because it's a nice way to inject brand, but not in a strict style. And.

**Gorkem** [00:46:42]: We are just entering like post-training on video models and what's that that's going to mean, because we didn't have a good base video model that it made sense. But now we have like companies really investing into like post-training on one, 2.2 or who neon and like creating lip sync models on top of it, creating like different video effects, camera angles. Seems like there's a lot of possibilities with, with like creative data sets that people can do, I think in the next six months to a year, we are going to have. We are going to have a lot of like companies that are just built on post-training of, of open source video models. Wow.

**Alessio** [00:47:18]: Let's talk about pipelines. So we are Comfy Anonymous on the podcast. Comfy UI is kind of like this community that like, if you're into it, you love it. If you don't know about it, you kind of underestimate in a way, but people create all kind of crazy workflows. One, have you thought about doing pipelines? Obviously you host all the models. There's kind of this question.

**Batuhan** [00:47:36]: We do have a pipeline product called File Workflows and you can chain models together, but it's obviously less flexible than Comfy where like the, the, you can only. Change like chain different models outputs and not the intermediary stuff in Comfy UI. You can like use like access the latents from like one model and then pass it to like a latent upscale or whatever. In our case, it's like more limited, but we have a workforce product and we have a serverless Comfy product where people can bring their own Comfy UI workflow and run it as an API with just like posting the workflow and inputs. And have the models be served by you. Yes. So is, is that a bullish thing? Is that going to be commoditized by big models? The thing that we saw is as the models get better, like Comfy UI was a. My. Much bigger thing or like, you know, relatively much bigger thing in two years ago, like a year ago when the models were like, you know, one of the biggest Comfy UI use case was you were like generating an ST 1.5 or STXL image and you were fixing six finger situation, you know, like you were fixing like the resolution, you were whatever upscaling. Now that the models are actually so good, the Comfy UI workflows are actually getting simpler for image side for video. It's still very crazy. Like if you look at some video workflows, it's like, there's like 50 nodes, whatever that you're, you're processing. So I think this is still a matter of like how good the models are and how much. Extra stuff you need to do around it for majority of use cases for artistic use cases, you still are doing like all those stuff and that's like something we want to support, but like that, we don't see that happening at super scale, you know, like super scale, there's not companies that are spending like $10 million plus on running this as an API. So that doesn't seem to be happening yet just because it's like a bit inefficient and the more existing, like it's more reliable to use an existing model than patching together 50 different things because you don't know when it's going to not work. Yeah.

**Alessio** [00:49:07]: But it feels like for things like ads you want to do, you know, once. You're like, you know, like if I'm going to do a new step, which is like maybe generate the backdrop, one step is like adding copy. Are you saying that basically the models are so good.

**Gorkem** [00:49:17]: Chaining of models happening for sure. But I think ConfUI did very well is you can also play with the pieces of the model. Yeah, you're basically saying that's all. Yeah. So like chaining of the models, like that's what the File Workflow product does. It's basically calls many different APIs back to back or in parallel, and then creates a result at the end, I think. And it is very popular.

**Swyx** [00:49:37]: We have like enterprise adoption from it, like from very big names. Yeah. Amazing. I was just going to go into sort of broader topics. The first thing that comes to mind was requests for startups. If you're not working on file, but you see a lot of things in the ecosystem. Right. What's the most obvious thing that people should be working on?

**Batuhan** [00:49:53]: More model companies. Go raise more money and train models. That's obviously good for file. And host them on file. If you're not interested in training models, but like if other people are trained, that's amazing. Go raise more money. There's so much money.

**Gorkem** [00:50:05]: Or like scale AI for image and video models, like data, data collection. Like more and more prepared data sets for video models, like effects, different camera angles. Everyone seems to be reinventing the wheel when it comes to collecting that data. I think it's a great opportunity for someone to come in and do this at scale.

**Swyx** [00:50:27]: So it's really interesting because I think this is what Together AI did with Red Pajama is they actually built a data set for language models to help people create more open language models that they can serve. So at some point, like actually it might make sense for you guys to do that. Yeah.

**Batuhan** [00:50:40]: The image data is a bit more finicky situation, like in terms of like copyright stuff, whatever, but it's an interesting area. Do it in Japan.

**Gorkem** [00:50:49]: I think it requires focus. It requires, like this needs to be.

**Batuhan** [00:50:54]: Like one connected thing to what Görkem said is image slash video RL. That's an unknown unknown for us. Say more. I can't. It's like, what does it look like? Can you RL a video model to be a world model? You can, right? Like if you can. Like, it's essentially the verb models aren't RL'd video models where you condition it for like, you know, moving around. So what are the use cases for RL'ing image and video models? I don't know, but that's like if I wasn't working at all, that would be something that like that might be fun to explore. Yeah.

**Swyx** [00:51:24]: And is this is specifically for editing because the RL is for the reward is the edit or?

**Batuhan** [00:51:29]: That's the thing. That's, that's what you should look for, right? Like what, what is the reward function, like what is the interesting reward functions that you can apply on top of these base models?

**Swyx** [00:51:37]: I see. Interesting. Okay. Got it. Actually, I was really asking. But like, if I were to build a file wrapper startup, like on top of that, because you guys are very low level, which is fantastic, you know, but I also want to give our listeners some ideas, you know, if they're not going to work at that level.

**Gorkem** [00:51:51]: I think I'm going to say it again, advertising advertising, there's so much opportunity there and everyone's like still trying to create these horizontal applications where like any creative can come in and do something, but like a lot more targeted to specific industries, a lot more targeted to like different kinds of products. Kind of like ad networks. There's a lot of potential there. Click.

**Swyx** [00:52:13]: And then requests for models, obviously you want more open models. That's good for you. But like any like specialization in the models. Like I think image, image editing was a huge unlock, which I didn't foresee until this year.

**Batuhan** [00:52:26]: Where we're like, oh, obviously we're going to, even OpenAI didn't like guess it was going to go this big. This is like, it's insane. Like how popular it became. And then like everyone started like catching up.

**Swyx** [00:52:35]: I was part of a group in Europe that we meet in Europe every year and like they were talking about this.

**Batuhan** [00:53:02]: Swyx and Alessio image models are really, really, really affected by the data set that you use.

**Gorkem** [00:53:13]: Yeah, I think one obvious thing that there's a gap in the market is like VO3 is very expensive. And the way, the reason why people like it is conversation, right? If you can create maybe a smaller, cheaper video model that is less capable, but can do conversation and sound very well, I think there is definitely...

**Batuhan** [00:53:31]: One open source one that we saw was Multitalk. It was a post-trained version of one, and it's like really, really good for conversations, but it lost the ability to generalize. You know, it's only like talking faces at some point versus like VO3, it could generalize and it could do scenes and whatever. So I think that there needs to be like some middle ground between these two, between talking faces and like, you know, extremely generalized video models where it's like much cheaper to run. But at the same time, you know, you get like this conversation because it's very memetic. You know, people, there's infinite amount of memes that you can post with this, infinite amount of ads that you can do with this.

**Alessio** [00:54:05]: But you don't see a world in which you have a video model and then you have a separate, maybe audio-only model that can generate the audio for that video.

**Swyx** [00:54:11]: This is the word for this question, right?

**Gorkem** [00:54:13]: Yeah. Do you stitch together a whole bunch of things or do you better less? People did that before VO3, but what VO3 gets very well is like the timing. Almost like you ask for a joke and, you know, the delivery and the timing and the laugh and like, you know, waiting right before like the joke drops, like all of that is so perfectly timed. I don't think when you do it separately, you get it. It's all the same.

**Batuhan** [00:54:37]: It also matches the human accent sound to the face that is talking, right? It's like, it's an unknown challenge for like other text-to-speech models. Like, it feels very natural. Is VO3 the best text-to-speech model? It is also one of the best text-to-speech models. It is so good. Like, I don't think any model can do what it is.

**Alessio** [00:54:53]: But I would say the counter argument is that we dub movies. So there's already, you know, obviously you can.

**Batuhan** [00:55:00]: It is also the best lip-sync model. Like VO3 has the best, most accurate lip-sync because it's generating very natively. There's really good lip-sync models. I think they're like 95% there, but VO3 is like a hundred percent there, like 99%.

**Swyx** [00:55:11]: To me, this is like the single most bearish thing about workflows, right? And Comfy UI and all this stuff, like, because just wait for a bigger model. Like it's just pure bitter lesson. Like, yeah, we love Comfy UI.

**Swyx** [00:55:23]: But I mean, obviously like when the technology doesn't exist yet, you have to stitch together things. Yeah. So a request for engineers? Yeah.

**Alessio** [00:55:30]: I mean, what I'm sure you're hiring, right? You're just raised $125 million. We have a very selective way of hiring.

**Batuhan** [00:55:36]: Like we just recently. We've been hiring like 100, cross 40 people, but like for like the. Wow. For like three months ago, we were like 20. So like for the last three months we have been actually accelerating, you know, best kernel engineers, best infrastructure engineers, best product engineers, best ML engineers. If you're the best at what you do, just come join us. I think it doesn't really matter what you do. Just like we're just hiring the best talent right now.

**Gorkem** [00:55:56]: Even on the go-to-market side, we are hiring account executives, customer success managers, because we work with very large enterprises. We got to grow that side of the company as well. Yeah.

**Alessio** [00:56:07]: On the engineering side specifically, how do you think about how many people you need? There's like this whole question of like lean AI, it's like, you know, coding agent.

**Batuhan** [00:56:14]: Our performance team is like seven people. I think seven people like focusing on performance always like some of there's some overlap with our applied ML team, which is taking these models, productionizing them, exposing new capabilities, building fine tuners. So it's like a, and then helping customers adapt these models. So that team, I think we can scale to like double, triple the amount because like there's infinite amount of models and like, you know, it's better because like we're going to have more customers with more proprietary models. Yeah. So just like helping them optimize it. It's just like a really good function that we have.

**Gorkem** [00:56:40]: That team scales very well because there's always like independent work that can be done. Oh, okay. So these three people are working on this new model, trying to optimize that. And it's completely independent from trying to optimize this, this other model. So we've been hiring a lot for, for that applied ML team.

**Batuhan** [00:56:56]: Our aim for a team, you know, we were probably going to keep it lean in contrast to the applied ML team and the product team, maybe like we want to build more higher level components where people can directly integrate to their applications. Because like, that's even like now there's just like SDK or SDKs, but think about with component, like imagine you're an e-commerce website designer and you're not really like the best like component designer. So here's a virtual try on component that you can put to your app, stuff like that, more higher level components. And this is like also coming from the fact that, you know, wipe coding has been very, very insane. We all, we, we see like significant, like revenue wise, it's like very small, but like we see a significant amount of user adoption just coming from people who are like, like just from looking at our support tickets. Maybe they're like more, they need more support, but like, there's like a lot of people who are like coding these applications without like that much expertise in the product building.

**Swyx** [00:57:43]: So we want to provide you, provide them more guardrail experiences where they can integrate much easier without like messing with like all the other like lower level components. That's really nice care of developer experience. So crack low level engineers.

**Alessio** [00:57:57]: And crack high level. Well, yeah, high level engineers, crack engineer, crack go to market people, crack whatever, just your thought.

**Swyx** [00:58:04]: You know, I'm, I'm always trying to refine the definition. You know, crack, you know, like both of you, like you, you leave the technical side of fail. Like what's a really hard technical problem that if someone has the solution, they should talk to you immediately. Maybe that's the way to frame it.

**Batuhan** [00:58:16]: Write a sparse attention kernel with FBA on Blackwell and tell, you know, like if you can't do that, come join us. We already have like a good base. Hired on the spot. Hired on the spot, you know, like stuff like that. I really like picking like all these, like some of these applied ML people, like we just picked them from discords who are working on these sort of terms and media who are like already interested. We really have a high culture bar too. Where everyone in the team lost generation media. Like they're obsessed with it. They would have done this if this wasn't their job. We have this great composition. We're always, it's not like a prerequisite, but it's just naturally happened where we hired these people from like discourse, Twitter's hugging face. Like one of our applied ML engineers is like had the number one top hugging face space with like, you know, creative workflows, whatever. So we hired the person who was training Doris on fall, like just because they were training and posting cool Laura's, you know, like just do cool stuff and we'll find you or like you can.

**Swyx** [00:59:06]: Yeah, that's the master builder is what I've been calling this, this person.

**Alessio** [00:59:10]: Why not make it more explicit? So if I go on your careers website, right. It's like apply to ML engineer. It just kind of looks like any job description. I feel like there's like this question of like, that's why we have to do a podcast, but I think it's not, it's not just about foul.

**Batuhan** [00:59:25]: I think in general, more like, if you know, you know, which I know is not the best way, you know, people know about fall already. So it's like, we haven't really cared that much, but you're absolutely right.

**Alessio** [00:59:35]: Like we should make it more. But if I look at like George hots, like on tiny grad, you have this balance. It's like, Hey, we'll just, if you can solve this, you should probably work here. Like, do you see, I'm adding the bounty, right? It's like, this seems like, Hey, look, if you can write this kernel, it's like, yeah, you'll just get hired.

**Batuhan** [00:59:51]: It is also about like one thing that we saw, even with like, there's a lot of people who are just like wipe coding stuff and reviewing those. You're like, there's a limited amount of people who can really do those. Right.

**Alessio** [01:00:00]: Like, so like, like, how can you tell it's like not a shitty kernel or it's like a good call, but then you're spending the time interviewing. Yeah.

**Batuhan** [01:00:06]: So like, we, we have like first line of defense with our recruiters, whatever. So you only get like, like, so there's like trade-offs, but I, I absolutely agree. Like maybe we should have like a kernel bench version that you can upload your kernels, automatically evaluate the stability, performance, whatever. And then if you do, you get our email unlocked, whatever, especially email for your, for you, but yeah, great ideas. Come join us.

**Alessio** [01:00:31]: Awesome guys. Anything else? Parting thoughts. Yeah. I love your rant. So this was great. Yeah.

**Gorkem** [01:00:37]: I'm happy to rant. But this is a podcast style. Yeah.

**Swyx** [01:00:40]: No, the congrats on all your success. Um, I should also say it's fun to do karaoke with you guys. Yes. Let's do it again. Both extremely technical, but also like a fun crew that like, and I think it's pretty hard to, and rare to, to see. So thank you to see the good guys win.

**Alessio** [01:00:56]: Awesome guys. Awesome.
