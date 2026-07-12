---
title: 'Mistral AI (Mixtral-8x7B): Performance, Benchmarks'
topic: models
subtopic: releases
secondary_topics:
- models/benchmarks
summary: Technical overview of Mistral and Mixtral model behavior, performance, and
  benchmark positioning.
source: arize
url: https://arize.com/blog/mistral-ai
author: Sarah Welsh
published: '2023-12-27'
fetched: '2026-07-11T04:48:11Z'
classifier: codex
taxonomy_rev: 1
words: 6973
content_sha256: 6fe2622666bc7ca1fee9459d5b0f9febf9b07295b7e08a9c355ac45a7672e4eb
---

# Mistral AI (Mixtral-8x7B): Performance, Benchmarks

![Community Paper Reading - Aparna, Aman, Dat - blog Aparna, Dat, and Aman headshots](https://arize.com/wp-content/uploads/2023/12/Community-Paper-Reading-Aparna-Aman-Dat-blog-1021x560.jpg)

              # Mistral AI (Mixtral-8x7B): Performance, Benchmarks

## Introduction

For the last paper read of the year, Arize CPO & Co-Founder, Aparna Dhinakaran, is joined by a Dat Ngo (ML Solutions Architect) and Aman Khan (Group Product Manager) for an exploration of the new kids on the block: Gemini and Mixtral-8x7B.

There’s a lot to cover, so this week’s paper read is Part I in a series about Mixtral. In Part I, we provide some background and context for Mixtral 8x7B from Mistral AI, a high-quality sparse mixture of experts model (SMoE) that outperforms Llama 2 70B on most benchmarks with 6x faster inference Mixtral also matches or outperforms GPT 3.5 on most benchmarks. According to Mistral AI, this open-source model was optimized through supervised fine-tuning and direct preference optimization. Stay tuned for Part II in January, where we’ll build on this conversation in and discuss Gemini-developed by teams at DeepMind and Google Research.

## Watch

Dive in:

## Listen


🎧 **SUBSCRIBE** [Spotify](https://open.spotify.com/show/4sykmDkrUklwyjOCB8FdLQ) | [Apple Podcasts](https://podcasts.apple.com/us/podcast/toolformer-training-llms-to-use-tools/id1666375694?i=1000605075518) | [YouTube](https://www.youtube.com/watch?v=pSKHDduKt_g)

## Transcript

### Overview and Background: Mixtral 8x-7B

**Dat Ngo:** Awesome. We got the crew here. Welcome, everybody. I think we’ll wait a couple minutes as folks come through into the lobby, but really excited to talk to you all today.

We’re going to start with some quick introductions. My name is Dat, I am a solutions architect here at Arize. I build with a lot of our customers kind of at the ground level in the LLM space. So, really excited to show you kind of what we have today.

I’ll go ahead and let our other presenters introduce themselves.

**Aman Khan: **Hey everyone my name’s Aman. I’m a group product manager at Arize. I’ve been at the company for a couple of years. These days I’m mostly focused on our LLM product line and helping kind of understand what data scientists and LLM application builders are doing in the space and sort of translating that back into our product roadmap. Working very closely with Aparna here.

**Aparna Dhinakaran: **Hey everyone, thanks so much for joining. I think today is going to be a really fun discussion. 

Actually, we started off thinking that we’re going to do both Mixtral and Gemini. But as we were putting together the material, we realized we might only have time to get through Mixtral today. So we’ll focus on Mixtral, and maybe for the next one we’ll do Gemini.

My name’s Aparna and I run product here and work with a lot of people who are actually putting this stuff out into the real world so there are a lot of good nuggets I think we’re going to learn from this, and hopefully we’ll see more Mixtral role users out there in the next couple of months.

I guess, given how much we have to cover, we’ll just jump in.

**Dat Ngo:** Yeah, really excited. So for today’s presentation, I’m going to go through a little bit of the agenda.

There’s a lot of context knowledge that we want to give you all to really understand how we got here. How did we get to such a great open source model with Mistral and Mixtrel? We’ll definitely cover some concepts like power laws in large language models, how researchers and people who train large language models are thinking in the space. And we’ll definitely go through a journey of what was built before Mistral and Mixstrel and how LLMs got better. And then after that, we’ll definitely talk about the recent improvements in these kind of architectures, in these OSS models and how they’re getting better specifically in Mistral and Mixtral, and we’ll also go pretty deeply into the mechanics of not only dense model architectures, but mixture of experts architectures.

So that’s today’s agenda. Let’s get started.

The first thing to understand is that there’s a relationship between three things when you’re training or prepping LLMs for real world applications and performance.

The first one we’re heavily gated on is compute available. So you can think we don’t have unlimited amounts of compute. And so that’s generally the thing that gates us and based off that we can really kind of affect or change the next two items. So I’m sure we’re all familiar with model size. A lot of how this is determined is parameter size. If you hear words like Llama-70-B the 70 B is the model size, or 70 billion parameters essentially is how we measure the changing switches inside of a specific model.

So I think most people are familiar with that.

And the last important thing, too, is training data. When we’re training LLMs, the relationship between maybe model size and training data is something really important to understand.

So let’s travel back in time a little bit. You know we can think of the good old days in 2020 when OpenAI released this paper, scaling laws for neural language models. The Tldr on this paper right here is that OpenAI essentially wanted to answer a question, and the question was, really, you know, given a certain quantity of compute, how large of a model should I train in order to get the best performance possible? And what should the data associated with that look like? So essentially, how do I create the most performant model based off of a specific compute constraint?

We can look at basically this kind of one image, essentially, kind of summarizes their findings. So model size kind of grows and data size kind of grows. The relationship they tended to understand was that model size almost has the most kind of effect on performance. And so we can. We can run through some napkin math, but for this figure here, what essentially they found was to optimize compute efficiency when training, they said most of the increases should go towards increasing the model size–aka, the parameters–a relatively small size, and in the increase of data is needed to avoid reuse of set data. So they’re basically saying, Hey, it’s more important to have bigger models and less data.

![The birth of Mistral AI](https://arize.com/wp-content/uploads/2023/12/Screenshot-2024-04-09-at-10.24.21 AM-1024x574.png)

**Aman Khan:** Dat, we had a question from someone in the community asking: Is model size, a function of just N parameters as well as number of layers. Or how do you define it here, as you’re talking about this? 

**Dat Ngo: **Yeah, that’s a great question. In dense models, we tend to think of model size as what are the number of neurons or how many parameters are being fired at inference time. And so the answer to that question is, yeah, in dense models, we can think of that as parameter size, because all neurons are being used. We’ll talk a little bit later about what that looks like. What is sparseness, things like that. But for the most part in this case, in the early days it was definitely model size.

And so great question. TLDR if I give you 10x more compute, according to this paper, you should increase your model size by about 5. And your data size about 2x. If I give you another 10 after that, the model size increases by 25, and the data only 4. So you can start to see this kind of power law kind of form. And so the result of this paper in early 2020 was that researchers really took this to heart, and everybody was like, oh, OpenAI is doing really well–they really focused on creating larger models. And that’s why, in the early days you can see these parameters getting much higher.

So that was the result of the 2020 paper.

In 2022, a few researchers from DeepMind– specifically, let’s mention Arthur Mensch–they had a new finding they wanted to kind of challenge this kind of thinking. So two years later they released this paper called Training Compute-Optimal Large Language Models, essentially trying to challenge this idea. And their central thesis was, model size and number of training tokens should actually be kind of on parity.

![Screenshot from Dat's presentation of new scaling laws from DeepMind](https://arize.com/wp-content/uploads/2023/12/Screenshot-2023-12-22-at-4.35.48-PM-1024x575.png)

And so what are we looking at here, in this graph here [above], we tried to compute the scaling law here. So we actually use 9 different quantities of compute.

You can think of this as these individual colored lines. And we also chose different sized models which you can think of as the X-axis, and then training losses–optimal training. And so essentially, what they found out was, and you can see, kind of the best place is the minimum for each one of these. That’s where you want to be.

And so, as we move towards smaller model sizes, look at the training loss, the TLDR is that you can draw this power law and the power law essentially states that– data and model size should grow at the same rate given the constraint on compute. So if I get a 10x increase in compute, my model parameters actually get 3 times bigger. And the same should be true for my data.

If I do that again, if I do 10 times 10, essentially, your model gets 10 times bigger and your data gets 10 times bigger.

So, pretty interesting challenge to these findings in 2022. And the really cool part is, this test was actually done with the really small kind of models, because this would be really expensive if you ran this on very large models.

So they actually tested it in the same paper, using two different types of large models. They used chinchilla versus gopher and the TLDR; here is chinchilla was used using the power laws. You can think that DeepMind kind of found out. So the new power laws and Gopher was kind of the older way of thinking. So chinchilla was 70 billion, and Gopher was 280 and so the result was they expected Chinchilla to outperform Gopher. And the really cool thing is, it did.

The training set that they used for Chinchilla was 1.4 trillion tokens versus Gopher was 300 billion, so larger versus smaller. And the result was that Chinchilla, outperformed Gopher on 51 out of the 57 individual tasks, about 8% on average. So the really cool part is that they proved that. So we get these new power laws, great. What does any of this have to do with Mistral and Mixtrel?

If you guys remember correctly, I think for a long time. Llama 2 was kind of like your go to open source model, so this was the birth of Llama 2. but for the Llama 2 researchers, they actually took it a little bit further beyond the chinchilla scaling laws. They actually overtrained on more tokens. And so when you think about overtraining on more tokens, you can compress the model more essentially, you’re trying to stuff and compress as much training data inside of a model, and so that means it can get smaller. And when it gets smaller, that means when you run inferences, they go faster, and they’re essentially cheaper.

And so this is why we saw the birth of Llama 2. It was kind of everywhere. You had Llama 70B. Llama 13B, so the main thesis here is by spending more time in training, you spend less time during inference. So that compression is super key. And this concept comes important later, when we talk about Mistral and Mixtral.

Okay. So why did we talk about any of this?

Well, turns out there are two researchers from Llama 2, and one researcher from Chinchilla. So those two papers we talked about, they actually came together to form a new company called Mistral AI. And that’s really what we’re going to get into today is what were the things that they not only built off in these two papers? But what did they build and Mistral? And how is, you know, Mistral, so performant given it’s relatively small size?

I’m gonna pause here really quickly. Aparna, Aman, anything to add before we move on?

In the Mistral paper–[linked here, if you haven’t read it yet](https://arxiv.org/abs/2310.06825)– one really cool thing about Mistral is you can actually go and grab this model on Hugging Face, the weights are publicly available. There are three concepts I want to go into depth on the improvements made on Mistral…

**Aparna Dhinakaran: **That was great, the walkthrough, but what would you say about this back and forth, you’re kind of explaining here of models versus compete, you know, basically the ratio of models to computes to data. And what’s the big takeaway maybe?

**Dat Ngo:** Yeah. So we’re constrained on compute, generally. We can control model size and training data. And the smarter we train our models during the training stage for these base models, the more performant we’ll get. And so the things that we actually are optimizing for in production is like inference time. So a lot of times when you’re building an LLM application, you don’t want to take forever to generate your tokens. If you’ve used GPT-4, the non pairboard version versus 3.5 turbo. You’ll just notice a significant difference when you get your first token and the subsequent production of the rest of the tokens. 

So when you’re building LLM applications super important.

The other thing is cost. Generally running more parameters. So a larger model size takes more compute to run at inference. And there’s two costs you’re optimizing. For if you’re an LLM like researcher building models. Obviously, you want to reduce training costs, but if you’re a user of one of these LLM models, what you wanna do is reduce inference costs. So at inference time. So generally with more parameters, you have to run more computations.

And so whether you’re thinking from: Hey I’m a researcher, I’m building brand new architectures. You’re really optimizing on all three. But if you’re a user, what you’re really optimizing for is speed of inference, and then cost of inference. If you’re essentially hosting your own model.

Hope that makes sense.

**Aparna Dhinakaran: **That was great. Yeah. 

**Dat Ngo:** I think we’re always learning new things. There hasn’t been a ton of exploration relative to where we are. I think five years from now we’ll just be like, Oh my God, I don’t know why we did the things that we did. And, do I think we’re at an optimal place today? Probably not. We can just see that in two years we’ve increased so much. What we thought was once true is no longer true. And then we’ve actually gone past the Chinchilla scaling laws. 

And so, I really do think there’s a couple of places we can optimize on. And it’s not only like the laws or ratios between model size and training size, and we’ll cover it in the Mistral paper. I think these models are getting smarter, and the architectures are getting more complex, which ends up producing, I think one day we’ll have very, very low latency models performing at a GPT-7, one day. Very much sure about that and the investment into the research space. But I do think we’re not optimized.

It’s not only just the size of data, I think there’s another component here which is the quality of data–completely different. So, a lot of parameters here, and I don’t know the answer completely.

**Aman Khan:** So scaling laws aren’t everything. There’s a ton of other things to go and optimize on, which was kind of against, you know, sort of conventional wisdom, maybe for a little while.

### Overview of the Research: Mixtral 8x-7B

**Dat Ngo:** I view scaling laws as like the lowest hanging fruit. Kind of like a big jump, small change. Kind of dumb, small change, but helped us make leaps. And so, great question.

So let’s get into the Mistral paper. I think that’s kind of what we’re all here for. And there’s three things I really want to highlight here.

The first thing which is grouped query attention. Which we’ll go into depth. But essentially, this helps us create faster inferences at inference time.

The second one is the sliding window attention. It helps us not only reduce cost–well, I think that’s the main thing. It helps us reduce cost and not maybe have so many computations when we’re dealing with extremely long sequences.

The last one which is BPE or byte fallback tokenizer. It’s really how to deal with things like OOV– or out of vocab words–or things in different languages, and how to deal with that that generally has been, has given kind of large language models, kind of issues in the past.

And so let’s go through some conceptual foundations of this. I’m gonna go through the paper real quick. And then we can talk about some of the ideas.

So grouped attention, group query attention. If you are familiar with, like, how regular attention works the way. Okay, the purpose of this kind of mechanic is to reduce computational intensity. And so traditional transformer models utilize attention mechanisms to determine different parts of, like the input data or sentence. Right? These mechanisms are pretty crucial, for, like a model’s ability to understand, you can generate language. But they’re known for, like high computational demand–the model trying to understand, how does this one word relate to every other single word? When these are dealt with in long sequences, compute can be kind of an issue.

And so with group query, attention. It standardizes the standard approach by grouping multiple queries together. So instead of calculating the attention for each individual token you can make GQA computes the attention, for a group of queries simultaneously, so you can kind of think of it as more parallelization.

And what this gives us is like computational efficiency, right? While preserving accuracy. So it’s one of these little cool improvements that we made that help us produce faster, better inferences, but at the same time maintain performance, which is everything we’re after.

So that’s the first mechanic I want to talk about.

And so the second one, which is sliding window attention when you think about addressing really kind of long sequence challenges. The way the sliding window works is…so traditional attention mechanisms have, like a quadratic kind of computational complexity. So with respect to sequence, length, right? So this means as the sequence gets longer, the computational resources required increase exponentially.

So what does sliding window attention fix?

So this introduces a window of a fixed size, and that moves or kind of slides across, like the entire sequence. So for each token in the sequence, the model only computes attention for the tokens within that window. And this actually gives it linear complexity rather than quadratic. So if you’re familiar with big O notation, instead of like big O n-squared is just big O n.

And so why is this important? Well, obviously, it allows us to reduce complexity in terms of computation. So we go from quadratic to linear. And so something as simple as that. Again, we’re able to handle larger sequences more efficiently. Basically, tougher problems are easier to solve. And the last thing which is VPE or byte fallback.

It’s kind of the way we do it with tokenization. So with traditional tokenizer limitations. It’s like whether the word is like whether it’s word-based or character-based–they have limitations. So word based tokenizers struggle with OOV, or people like to call it out of vocabulary words. And then we have character based tokenizers which can lead to really long token sequences. And so the pros here–and I don’t know the mechanics fully–but you have more coverage, comprehensive coverage. It’s like, basically, you have a better dictionary in your LLM. It allows you to adapt kind of to different, even languages, or maybe domain specific items. So there’s jargon there that you wouldn’t normally use. If you ever learned a new language you’re like, oh, I can speak fluently when I’m ordering food, but maybe in a business setting I have no idea what people are saying. So it kind of helps the large language model deal with that. It’s really an optimization between finding the middle ground between word level and character level. So basically dealing with hard words, that’s the best way I can describe it. I don’t really know much about it. But if I had to describe it, it basically helps performance in terms of weird vocabulary.

I’m just explaining it like a layman. But if you want to go into depth, obviously the Mistral paper has a lot of this. And they talk about things like GQA, SWA, and then also the BPE. But one thing, yeah. If we want to cover one of the items here. I think it’s the sliding window attention.

And so just wanted to go here that the normal kind of way of doing this is vanilla attention which it does state right here is quadratic in sequence length and memory increases linearly. Whereas when we do a sliding window, it’s that the computation scales up in terms of just linearly instead of kind of looking at everything.

I’m going to pause, that was a lot.

**Aparna Dhinakaran: **They don’t actually talk about GQA much in the Mistral paper, but there’s another paper that talks about it. And there’s a really good image that actually explains it. That was super helpful for me in the reading of it. 

![Group query method overview](https://arize.com/wp-content/uploads/2023/12/Screenshot-2023-12-26-at-1.17.02-PM-1024x435.png)

Okay, so this is grouped so like that was saying, there’s kind of three major components that I think the Mistral paper we’re going to go through. And there’s also the gaining network. And then the expert tokens that that kind of make up the mistral paper. So the first big one was kind of this grouped query attention, and there’s a couple of different approaches to this, you know. Essentially, you could do multi head attention, you do group query attention. And there’s multi query attention. And so these visuals were actually super helpful in helping me understand this. So the queries here. These are all the blue ones over here, and essentially in a multi head. Each query over here has its own keys, which essentially has its own values in a group query, this is what Dat was explaining, where you have multiple queries that are grouped together to similar keys. And then these are actually routed to the values. Multi query, Obviously, this is kind of nuanced here. Which isn’t totally clear to me in this paper, as well as like, you know, is grouped only limited at two. Can it be multiple versus in a multi query is there kind of spanning across kind of more than a handful or a couple that all group together into one kind of key?

But this visual is really helpful, because essentially, this actually helps with the speed of this, because you’re not going from query to query, you’re actually going from grouping a set of queries associating with the key, and then a value.

Any other thoughts here?

**Aman Khan:** I don’t really have any thoughts, because I’m not comparing. I haven’t. You know I haven’t just just sort of like comparing different attention. I guess my question is like, is this a breakthrough? Is this like a known method? You know what’s unique about this group query, method? That was my question. Probably like further reading, would be like, is  this novel, or is this something that more models should be doing?

**Aparna Dhinakaran:** Yeah, it’s a good question.

So this has actually been around this is this is actually been around like these type of different attention methods. This paper was actually released prior. It sounds like this is kind of a model architecture.

**Aman Khan**: Back to Dat’s point earlier, like, it’s not just all scaling laws like, there’s a lot of optimizations you can do in various parts of your transform architecture to try to try almost like, get around. You know the sort of constraints of the scaling laws and get improvements in your bandwidth.

**Aparna Dhinakaran:**  Yeah, I’m not sure if because of this, there’s cause they’re also doing the sliding window, they’re also doing GQA, so there’s like some sort of, you know, limitation on memory. These models might have compared to maybe more denser, larger models. And so I feel like there’s some trade-off here just looking at the amount of data that’s actually available for these.

**Dat Ngo:** Yup, I think you nailed it. I think Rochon had a question which kinda is a perfect transition. I agree with both of you. I think in the beginning we had. I think we brute force a lot of this like in the beginning, we brute force a lot of like the innovations that we saw. And we’re like, okay, if we maximize the brute force. Great. There’s a lot of diminishing returns everywhere. And I think here we’re just getting smarter in the small mechanics. Not only architecture, mechanics, which is a good segue. 

So Rochon asked: what was the breakthrough of ChatGPT? Was it simply just scaling? And the funny thing is, Rochon, I think we’ll cover it here. I think open source is slightly behind these proprietary models, and we’re starting to see we get to look into the past. I think when GPT-4 released, there was some hints of–is this a bunch of Gpt-3 models running behind there?

And so I’m gonna share my next screen. And we talk about architectural changes. I think, SWE, GQA. And maybe BPE, or like small decisions that you can make smaller decisions that you can make in terms of LLM architecture.

But let’s go through a big one.

And this is dense versus mixture of experts. So what’s the difference between dense and mixture of experts? Well, for the first thing is like, when you think about dense. When you run Mistral 7B or a Llama 70B, All neurons participate in processing each piece of information. And so that’s a pretty key importance. This is what I mean by like everything kind of works, and we kind of, I wanna say brute force. Dense models are generally simpler, even though they don’t seem super simple relative to other things, but they are simpler when compared to a mixture of experts.

But you know there’s some cons here, they’re intensive in terms of like size. So some of the challenges here can be slow at inference time just due to sheer size, they’re expensive to run at inference time, and of course, to train, if you’re training something with almost 300 billion parameters, and it might be harder to scale. When we say scale, it might be obviously training, but obviously with inference time as well. So just just note that what we’re optimizing here for when we’re building applications is inference, speed, and cost.

**Aman Khan:** What is an expert network here? Yeah, that  seems kind of interesting as well, to define that.

**Dat Ngo:** That’s a good question. I think Aparna can also talk about this one. There’s a paper I think she mentioned in like, was it 1997? Something like that? AI’s been around forever.

**Aparna Dhinakaran: **Mixture of experts has been around since 1997. There’s some paper trying to cover on this the adaptive something of mixture experts. So it’s been around. It’s not like mixture of experts was discovered with the Mistral paper. In fact, even the GPT-4 architecture has some mixture of experts in it. And the big one here, I mean. So with the mixture of experts that’s helpful to say, is there? So essentially, what happens is like there’s two components here. There’s a gating network. And then there’s experts. So the experts are basically you know. You think about it like they’re really good at certain concepts. That’s maybe the best way to describe it.

And there’s another paper, the STMO paper that talks about what these experts are good at. There’s a lot of research still going on there like the STMO paper where they observed that experts end up specializing in a group of tokens or some sort of concepts.

They thought actually, the experts would be different languages like maybe one expert might be English, and one expert might be, you know, French, or Roman languages, but what they actually realize in theirs. And they actually, if you want, there’s a really good image I could pull up–But for me, the big thing that I was trying to figure out was like what the heck is an expert like, how is an expert decided? And this is actually an image from the STMoE paper.

And in this one, they were showing that there’s actually experts on things like punctuation and experts on like verbs, one on like proper names. And so, I would love to know in the Mixtral paper, are they on specific groups of tokens, like what are the groups of tokens on? But for me, this was a little counterintuitive that it actually broke up language into these certain things. And there are some experts that were like good at certain components. And so essentially, what happens is that data, if you go back to your image, given any specific token coming from the inputs right, there’s basically a gating network. And the gating network decides essentially which experts to route it to.

![Mixture of experts diagram overview](https://arize.com/wp-content/uploads/2023/12/Screenshot-2023-12-27-at-2.02.44-PM-1024x499.png)

Ok. This is a really good image [above]. So this is not from the Mixtral paper. This is just background material on what an MoE layer looks like. But essentially, there’s kind of like this thing about like a gating network. The gating network essentially tells you which experts to route the tokens to and like we were saying before, there’s some experts that are good at certain types of concepts or certain types of questions. And so it routes it to certain experts.

The key takeaway, that’s important on this is you don’t want it all to go to one expert, like you don’t want it to be highly specialized. One expert every single time. It’s just going to the same expert you. There’s actually a you know, as part of the training of the Mixtral paper. When things they talk about is like there’s some kind of loss where they essentially are are optimizing over so that you have the spread of tokens, and it goes out to as many of the experts as it possibly can. So some kind of like even load distribution across the experts.

Part of this is also for each token, how many experts can you call on? And then the OpenAI GPT-4 paper they both had two experts that are called on.

And so there’s some minimum where it doesn’t just go to one. But it actually goes to multiple experts per token. But this is actually, I mean, this is just outside of even the mixture of paper. This is probably some of the key takeaways on, just like how to mixture of experts even work. There’s typically a gating, it passes into the experts, you want to optimize so that there’s low distribution on your experts. And then you also want to optimize so that you have multiple experts being able to be called on for each token

And maybe we’ll get into this as we go into, like the fine-tuning components. But this is also why one of the reasons why it’s really hard to fine tune mixture of experts types of models.

**Aman Khan: ** And there was a note there on mixture of experts kind of optimization– There’s a ton of optimization. There’s like switch routing that they mentioned, so that that whole layer sounds like, you know, there’s there’s a it’s almost like you are literally fine tuning that layer to perform, you know, an even better sort of, you know, task at switching between experts. So that was pretty interesting as well. It’s like a model within a model.

**Aparna Dhinakaran:** And there’s some point where past this, it’s like how many experts do you want? Do you? Do you get to a point where the number of you know, I think they actually did some analysis of like. do add more experts. And you do see kind of like improved performance, you see efficacy, and like which experts to call on. But there’s some point where there’s just diminishing gains of this. And so I think this is also an area of where does the dimension gains happen, and how many is really enough. And is this an area where in the future of MoE, we’re gonna see more and more optimizing the number of experts.

**Dat Ngo: **Yep, makes total sense. I think there’s a lot we’re still learning, too.  We’ll definitely go over switch transformers and what they optimize for there. But for those folks  who see MoE, yeah, it consists of. So the difference between that and a dense network is like, not all neurons fire. And we’ll definitely get in the math of like, how these things fire off. And what are the gains we get from MoE. Specialized workers that don’t always fire, which is great is you could think of this like–hey, I have a specialized team. And it in just one heads up. Each token has its own path and experts. So this is not like, Hey, I’m seeing in a paragraph, and this paragraph just sends in like to these two experts. It’s each token gets its own. So it starts to make a lot of sense when Aparna showed kind of this is at the language level and at the token level, so super important to denote that.

But the MoE architecture allows, for like an overall, increased number of parameters. When you think of if I add up all the experts and the non feed forward neurons, you have more parameters. So basically more capability. But since you’re not running it through everything, you reduce things like inference time, you reduce things like cost for the same or better performance, which is kind of everything we’re looking for. And so major architectural difference change. And so, knowing this, maybe e like in the past, when we saw GPT-4, that wouldn’t, that might have been OpenAI’s transition over into MoE.

And like Aparna said, there are challenges here knowing how to train MoE architectures is actually more tricky. There’s actually a lot more math involved, as you can imagine, because of more complex architecture. But there’s also proficiency, proficiency, knowledge you need in optimizing hardware use and just overall more rigor. There’s also constraints around managing tokens and routing so it comes with its own kind of set of challenges.

And so, each token has its own path instead of experts, and, like Aparna said, I won’t cover this in depth, but a gating network or router kind of determines which tokens are sent to what expert. We can kind of look at here that like when we look at the token more versus the token parameters. They can kind of get sent into different routes so hence the router, and so that your question should be like, Okay, how has the token know which expert to go into? So what are the things that affect that?

**Aparna Dhinakaran:** I could share a little math if it’s helpful just to think about this one. I think the math always always helps me understand this on share real fast, that on this one.

Okay, let me get back to this. By the way, yeah, I think Sarah linked it and on linked it. But this blog post was actually awesome, it just explains kind of a lot of what we’re covering today. This is essentially what we’re saying here, which is like, Okay, how do you know what tokens end up at what expert? And there’s a lot of things to caveat here, because if you have uneven distribution or some experts don’t get utilized, that’s kind of what you don’t want. And so, if we just think about it in a really simple format, this was great to help me understand this. So there’s a gating network. And then there’s a number of experts.

In the beginning, if I just thought about it as like, you know, what I want is at the end of this is to know which experts should the tokens go to. And you could think about the gating function like, if the gating function is 0, which will be for many of these many of the experts, then it won’t need to go through the compute for all of those respective expert operations, and hence we save the compute.

And so in this example here, they just did something like you know, I think, just explain it like a simple soft math. But post this. So this is kinda the gating function, the experts itself. So this is actually where they’re doing the top K, and the top K is because we don’t want it to be just a single, you know, just a single one here. They want it to actually be more than one expert. So the gate learns how to route to different experts. So at least two experts had to be picked.

I think the switch transformer paper kind of like said revisits this. But if you think about it, essentially, this getting that work function is like weighted multiplication, it’s helping you figure out at the end of the day which expert to pass it through. Most of them will be 0, which means it only has to go through compute for a specific set of those experts.

Hopefully, that was helpful.

**Dat Ngo: **Yup, sure was. Okay, I think we’re kind of coming up on time. So definitely, want to just cover Mixtral 8X7B. 

I actually find the name a bit misleading. When you actually do the math on this. So just as a heads up, not all 7 billion parameters are being 8X’d. So 7 times 8 would be, you know, 56 billion. But when you look at the total number of parameters in the MoE, it’s actually 46.7. And then your question is okay. Why? Like I said, not everything is duplicated 8 times. Actually, there’s a certain set of non feedforward neurons that just just fire every single time. And so if we use a system of equations. And we think, you know, hey, you know, in the total model, we have 46.7 billion parameters. And there’s 8 experts. If we just fire one token right? And we see how many parameters are fired. It’s 12.9. And so using a system of equations, we can actually just understand that the number of parameters per expert is around 5.6. The non feed forward blocks are about 1.6, and then, if you add that together, that equals about 7.26. And so just interestingly enough, only 2 out of the 8 experts are ever executed for a token and so when we think about MoE and why is it helpful? And what happens here. I’m running significantly less number of parameters, but have significantly more access to more parameters. If that makes sense. So each individual token essentially gets the parameters or experts that it needs to to make better generations.

And so that router mechanism which Aparna covered in depth–super important. All the papers are linked, but just wanted to quickly show kind of the model architecture here. And really, how did this thing perform?

And so the Mistral paper, they tested this against Llama 7, 13 and 70. We can actually see the results. And so -lu is a massive multi-task. Let me double check that. Yeah, MMLU stands for massive multitask language understanding. And so this is kind of the main metric used, and we’ll go over it later. But we can also see some interesting things, too, in other places. Knowledge, reasoning, comprehension, math, and code. If you notice the one area that Mistral and Mistral or specifically Mistral doesn’t perform super well, it’s knowledge. And then it starts to make a lot of sense. Because when you think about it–knowledge or like what’s what knowledge is contained inside of an LLM is generally constrained by parameters right? Even though we’re compressing better, we have significantly less parameters to store or compress that knowledge in. So the really cool thing is this makes a lot of sense because When you think about knowledge and compressing the model, Mistral 7B tends to outperform Llama 13. In almost all cases, except for knowledge and the constraint here is the parameters, because you can only compress so much, right?

So really interesting thing here. One interesting thing to highlight is Mixtral, the MoE model is about 6 times faster than you know. Llama 2 70 B, and then performance. You can just see it just out performs everything here.

**Aparna Dhinakaran:** There’s a lot I feel like we still haven’t even gotten through on this, which is like the evaluation results, limitations of these models on things like fine-tuning, etc. Feel like it’s just a whole deep dive. We could still even do the architecture of it. So why don’t we do this? The next community paper reading will just keep deep diving in on Mistral and Mixtral. And let’s follow up on this. There’s just so much we have to cover.
