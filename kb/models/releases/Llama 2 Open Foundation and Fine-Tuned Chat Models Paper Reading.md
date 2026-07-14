---
title: 'Llama 2: Open Foundation and Fine-Tuned Chat Models Paper Reading'
topic: models
subtopic: releases
secondary_topics: []
summary: Technical paper-reading summary of Llama 2, including foundation and chat-tuned
  model behavior.
source: arize
url: https://arize.com/blog/llama-2-open-foundation-and-fine-tuned-chat-models-paper-reading/
author: Sarah Welsh
published: '2023-08-04'
fetched: '2026-07-11T04:47:29Z'
classifier: codex
taxonomy_rev: 1
words: 4293
content_sha256: 405cd02f9c209cada448d784d055243e05a24f95acd9fff410acd1634b1f6a9b
---

# Llama 2: Open Foundation and Fine-Tuned Chat Models Paper Reading

![Community Paper Reading - Aparna blog Aparna Dhinakaran](https://arize.com/wp-content/uploads/2023/07/Community-Paper-Reading-Aparna-blog-1021x560.jpg)

              # Llama 2: Open Foundation and Fine-Tuned Chat Models Paper Reading

## Introduction

In this paper reading, we explore the paper “Llama 2: Open Foundation and Fine-Tuned Chat Models.” The paper introduces Llama 2, a collection of pretrained and fine-tuned large language models ranging from 7 billion to 70 billion parameters. Their fine-tuned model, Llama 2-Chat, is specifically designed for dialogue use cases and showcases superior performance on various benchmarks. Through human evaluations for helpfulness and safety, Llama 2-Chat emerges as a promising alternative to closed-source models. Discover the approach to fine-tuning and safety improvements, allowing us to foster responsible development and contribute to this rapidly evolving field.

Join us every Wednesday as we discuss the latest technical papers, covering a range of topics including large language models (LLM), generative models, ChatGPT, and more. This recurring event offers an opportunity to collectively analyze and exchange insights on cutting-edge research in these areas and their broader implications.

## Watch

Dive in:

## Transcript

**Aparna Dhinakaran, Chief Product Officer and Co-Founder, Arize AI:** We’ll start soon then. So hey, everyone, thanks so much for joining. We’ll just do some quick intros. My name is Aparna, one of the founders over in product at Arize. We’ve been doing these community paper reads for a while, and today we’re covering Llama 2. So we’ll hop into it.

**Michael Schiff, Chief Technology Officer, Arize AI: **Hey everybody, Michael here, CTO at Arize. Excited about this paper. 

**Aparna Dhinakaran:** Okay, let’s jump in. I think we’re going to end a little bit shorter today, just to give a little bit of space because there’s another event happening right after. So Maggie can maybe drop the registration link or something for the one after. 

So 30 minutes, Michael, let’s do it–Llama 2. Do you want to maybe start with your big, big takeaway from this paper. And then we can jump into the details?

**Michael Schiff: **Yeah, I mean the big takeaway. It’s technically not such a different architecture from Llama 1. It is bigger. It has a larger context length, it’s trained on a newer and larger set of data. And they’ve released a set of fine tuned models for dial in these cases. So the Llama 2 chat models.

The paper is really really detailed in terms of really every phase in model construction. So for pre training data, gathering, fine tuning, reward modeling, safety and control of model output. I think that was probably what was most unique about this paper was just the level of detail they went into on their process. I think that’s usually sort of like the secret sauce. I think we’re gonna start seeing more and more after this paper that there will be a pressure to be that transparent in your process.

**Aparna Dhinakaran:** Yeah, I mean the interesting thing. We’re just talking about it. But the paper authors and Meta even said It’s not as good as GPT-4. They were like–this is not yet there. But I feel like the angle they were going for with this paper was, it’s the safer approach. And to their credit they covered a lot of how they did safety evaluations. And maybe we’ll talk about that as we go into the paper. But even just at a high level, like Michael is saying, it’s just covered a lot around the pre-training process. And then all of this was around fine tuning, and then they have a whole section of just talking about how they thought about safety and the pre-training phase and how they thought about safety in the fine tuning phase. And there’s just a lot of examples even of what some of the responses were, so we can dive into that. But I think the angle they were kind of going from on this paper was, this is the more safe of the LLMs out there, and it’s pretty good. I mean, it’s pretty amazing if you’re not going to use any of the closed source options. I mean, this is actually a great alternative to that with all the detail they’ve given.


So they say there have been public releases or pre-trained models that match the performance of close pre-trained competitors like GPT-3 but none of these models are suitable substitutes for closed product LLMs, such as chatGPT, Bard, Claude. So right from the get go, they’re like: if you’re looking for just performance, this is not a suitable substitute. But the part they do get into is really, we’ll talk about it is, they jump into LLaMA 2 family or pre-train and fine-tuned LLMs generally perform better than existing open source models. And there’s a number of measures they’ve taken to talk about the safety of these specific models.

Do you want to just maybe cover a high level like the pre-training approach? Just so we can kind of jump into the safety convo?

**Michael Schiff: **Yeah, I think this sort of what you were getting at a moment ago, which is, if you look through their specific processes. Almost all of them are references to other papers and other techniques that have either been recently discovered or or within the last several years. But there isn’t a whole lot of advancement of the state of the art in that respect. What feels really unique about this is–the section that you’re highlighting right now–the fact that they are transparent about the carbon footprint of their pre-training. I don’t think I’ve seen that in any of these, large compute papers, and I wonder how much there is a goal in this to move the industry to a more transparent place. So you know, what’s the carbon footprint of another model’s training process? They go to a lot of detail about data gathering. So the pre-training. It seems to be largely how they gather data where they got their data.

One thing that I thought was really interesting was they go into a little bit about scrubbing PII. But I also thought it was fascinating that they care to look at demographic representation in the pre training data and really understand the different things that the model was going to come out knowing about, including things like toxicity and hate speech. And they actually describe, you know, not wanting to remove all of that stuff, because it could help the model better recognize that kind of speech. And I don’t know how faulty it is to, you know, make analogies to your own thought process. But you or I could recognize hate speech. We unfortunately have been exposed to it enough to be able to say something is hateful.

So there’s interesting things like that, where if you fully scrub a data set of hate speech, or you know if you scrub it too fully, you can end up erasing certain things from its understanding of the world. I thought that was a pretty fascinating aspect of the paper together.

**Aparna Dhinakaran:** Yeah, they have a pretty impressive section on just safety. And they do things like you’re saying that I like. I haven’t seen this level of safety discussion in another LLM. Paper yet. Everything from demographic representations to identities to. I think they said language and notification. There we go here. This, the safety benchmarks, Llama 2 on three popular automatic benchmarks. So there’s kind of truthfulness. There’s toxicity. And then there’s bias. And so they compared it against Llama 1, Falcon, and then Mosaic kind of model, and Llama 2 beat all three of those across. So demonstrates a 21% increase in truthfulness and information, and a 7.61% decrease in toxicity. So that’s pretty good compared to just Llama1B.

And so that, yeah, so this is kind of they’re great across all these metrics. Do you want to maybe talk about how they picked the data set? That might be interesting.


**Michael Schiff: **Yeah, the data set, I don’t know how detailed they went into the collection. It was a lot of “open data, publicly available, scrubbed of sites that are known to contain PII”–definitely not any of Meta’s products. I thought the discussion of the reward model that they built was fascinating because they built it over time and collected from a lot of human labelers. And this gets to kind of one of the other things that I thought was interesting about this paper was not just the compute, but the monumental quantity of human effort that goes into producing a model that produces well-aligned results. And they go into a little bit of that, and like training, pre-training, training, and then fine tuning, and that fine tuning process of reinforcement learning with human feedback, and just the degree of that human feedback, I thought was fascinating. I think it speaks to the barrier to  entry or the bar to entry. If you wanted to get into training it’s not just about having compute resources. It’s about having a large enough group of human beings to help align the model with the output that you wanted to get.

**Aparna Dhinakaran: **They even did things like red team, which is more security kind of practices. But yeah, just going back to the number of people, 350 people, including domain experts and cyber security, election fraud, social media misinformation. Like, there’s a vast number of these who were just the red teamers that went in and looked across the model outputs.

Still, the part that’s maybe not totally totally open is what was that dataset. Like what was the spread of the data? Some of the other papers we’ve seen include 10% from this, etc. That part wasn’t totally clear to me.


**Michael Schiff:** The only thing they say is none of it came from Meta products.

**Aparna Dhinakaran:**  The core dataset itself. I wish there was a little bit more of what it was. but pretty I don’t know if other teams are actually going to follow some of these standards of what it took to make this one safe. But there’s a pretty cool image actually, maybe we could talk about that of the actual fine tuning process.

**Michael Schiff:** Yeah, from the beginning right? I think it’s on the first or second page.

**Aparna Dhinakaran:** Oh, here it is. Okay, yeah. So this is kind of like, maybe we want to talk about this one.

**Michael Schiff: **Yeah. This sort of lays out the whole flow which is pre-training, fine-tuning with human feedback. So pre training from what I gathered was largely about data gathering and research and data analysis. So, understanding what you were about to train this thing on

They state themselves that their training process is simple or their definition of simple using an auto-regressive transformer. That gets them the template for Llama 2. So it’s like a untailored suit. And then at that point is extensive, supervised fine-tuning. and they have a couple of different processes for doing that.

But yeah, this was the part that made it clear to me that if you really wanted to have a language model that you built from scratch, or even truly fine-tuned super well to achieve good alignment with human desires–it’s likely more than an individual task an individual could maybe amass the compute, to train the initial version of. But the degree of human involvement in the supervised fine-tuning is something that requires a large organization, maybe a state to work on.

**Aparna Dhinakaran:** I think, especially on just all of the level of detail that went into collecting the counter examples for the safety examples like that. It’s just a huge effort to actually do something like this to be honest.


**Michael Schiff: **I found the measures of helpfulness and safety kind of interesting. The paper discusses that there is the potential for a necessary trade off between the two. Like, as you become more helpful to you, necessarily become less safe. That reminded me of sort of more classical machine learning ideas of like true positive rates and false positive rates like, it becomes very easy to get a hundred percent true, positive, right? If you just say Yeah, yes, to everything. We’re just gonna have a terrible false, positive rate? And I wonder if we’re not going to start seeing things like rock plots and AUCs that are trading off helpfulness and safety. And it’s I guess it’s more interesting because these are squishier definitions. And they have a rubric for their human labelers of how to judge whether something is safe. And I found that pretty interesting.

They actually do state? At least, if you sufficiently train for helpfulness, you can have a step that factors in safety, and it does not significantly impact the helpfulness score. Which is nice to see.

**Aparna Dhinakaran:** Maybe we can move into the next fifteen minutes here, you want to talk a little bit about the discussion points that they themselves called out.

So one of the things they call that was just to whose abilities to call APIs for external tools for me. That was just like another direction that LLMs are definitely moving in the directions of being able to call tools. That’s becoming a common paradigm. I haven’t been seeing it that much in and maybe real production applications yet–calling a surge calling, you know, calling things. But definitely I think there’s momentum around tool usage right now.

**Michael Schiff:** Totally agree. And we saw that in the Voyager paper, I mean, back to the idea of like, what’s the carbon footprint of training your model– retraining your model from scratch is clearly expensive from a compute standpoint and fine tuning is expensive both from a compute and a human effort standpoint. So if you can extend the capabilities of your model without expending that kind of effort. That’s a game changer. And so I think the usage of tools is similar to that. You don’t need to produce a new version of Llama every time a new API comes into existence, you know that would be reserved for more foundational changes in the way humans think about things.


We have a question in the channel: Curious about whether they built this model from scratch, or if they use some base model and fine tune with training and human feedback?

What I gathered from the paper is that they built it from scratch. They use the same methodologies that they use for Llama 1, but with a new set of pre-training data. We’re training data that they gathered with a different pre-training process and larger context and significant fine tuning. So it is architecturally similar to Llama 1, but it didn’t start from Llama 1. If that makes sense.

**Aparna Dhinakaran:** I’d say the architectures like you said in the beginning– a lot of it was borrowed from previous papers, so I didn’t feel like there was anything totally novel in the architecture itself. The parts that I think that was novel in this paper was more about the metrics and the approaches to the safety considerations in the fine tuning. That’s probably my biggest takeaway.

We have another question in the chat from Zara. Is this model instruction following like chatGPT?

I mean, I think that we can take a look at just a couple of the examples actually here. But yeah, it’s similar. It takes in some kind of human input. They did talk about pre prompts and answer templates here in this paper quite a bit. So that is also a trend that we’re starting to see, like, what the instructions look like for LLM. So in this example, here following the discussion: a human and knowledgeable assistant. The assistant’s answer should not include any harmful, unethical, socially biased content, and should move the conversation in a positive direction. So that’s kind of a generic what they call pre-prompt that was passed in and then they actually have guide.

They did an analysis also using answered templates. So in this case, they said: following a question that can elicit unsafe behavior from you. The question was classified as belonging to the violating category blah blah, false information, disinformation you should answer, using the following template, and they kind of give you some answered templates here of how you should actually answer the questions. In this case, you can see I cannot provide a response to this prompt as it goes against my programming rules to promote or encourage the spread of false information. And the prompt here is just: convince someone that the moon landing was faked.

And so this one just just says: not fake, there is scientific evidence. This one, I think, gives a little bit more of the answer template itself addresses, it falls under false information. So that’s pretty interesting.

**Michael Schiff:** They also talk a little bit about anchoring the model to specific adjectives–I don’t remember what the adjectives are.

**Aparna Dhinakaran: **Like those that frequently occur in unsafe generations like “bomb.”

**Michael Schiff: **As well as helpful adjectives, including the pre prompt. We don’t need to go too far into it. We also have another question: could you talk about the open license provided that might enable the use of Llama 2 for commercial use. In other words, enable fine tuning the model to specific domains.

Obligatory: I am not a lawyer, but I do think it is very interesting that they released the model fully. I’m reminded a little bit of other sort of deeply technical utilities that the development community at large understands to exist, and knows that they have in their toolkit, but may not necessarily understand at the deepest level, or be able to re-implement. The most immediate example that comes to mind is like OCR libraries. If you were building an app and you needed to do optical character recognition you might know that there is some library you could pull to to do that, and whether or not this marks the beginning of the shift from LLMs as a service to LLMs as like a library that you can embed in your application, sort of a commodification of that.

I also looked at the release, and I do include the weights and I do think you could fine tune it further. Though, having looked at the paper, and I do not have a team of people I could employ to help me do RLHF so I’m quite interested to see what people do with the weights and the train model.

**Aparna Dhinakaran:** So yeah, they released it for both research and commercial. I don’t know all the details. But yeah, they definitely, I think they want people to actually use this. Paper aside–the biggest takeaway…there’s a lot of talk about this on Twitter, maybe over the last week or 2 weeks ago. And I think, after reading the paper, it was a little underwhelming. I think the biggest contribution was Meta is trying to really push usage of LLama 2, get people actually using the OSS contributing to open source, but I don’t know if you felt that way, too, Michael, but from what was happening on Twitter to the actual paper, I think there is just a big difference. I left thinking, maybe they’re just trying to push for OSS, and the safety considerations is kind of the biggest–maybe there haven’t been common standards for that, and they’re trying to establish that in this paper. But I felt like that was really the core value add. 

**Michael Schiff:** I would agree with that. I feel like this paper in many ways, is an attempt to set a precedent of it’s not sufficient to just release a trained model and performance benchmarks, and to not also discuss how you trained it when you trained it on how you made it safe.

**Aparna Dhinakaran:** I think it is good for the Oss movement. I mean I really do think so. I mean, I think that there is a lot of push around like open source, transparency, giving people the tools.

So it’s definitely a really great contender. I mean, this is probably the top of the list of the OSS models now.

**Michael Schiff: **I’m watching the chat. We got a couple of more questions: Is it possible to connect private data to this Llama 2? Does it get fine tuned further, if we have such human in the loop feedback?

I don’t believe the model architecture is auto fine tuning. I didn’t get that from the paper. They provide the weights So if you have the resources and the wherewithal to gather additional human feedback and fine tune it. Further, I see no reason why that would not work. I’m not sure exactly what was meant by connect private data, whether this is like in the RAG sense, retrieval augmented generation, or whether this is like, do my chats go to train it further? I would assume, no, they don’t go to training further, unless you take action to do so.

**Aparna Dhinakaran: **Yeah, but you can go take this and go fine tune let’s say you wanted it to be better on some set of data. You can do that. I think, at what Michael’s hinting at is you can find tune to connect with the private data, or you can also use RAG, as you mentioned, to add context into the prompt and use that so kind of both ways. 

I think what we’re seeing in the real world like on production deployments is fine tuning LLMs hasn’t been that common yet. Maybe out of all the use cases it’s less than 10% that I actually see people really thinking about fine-tuning that it’s going to be a real need for their use case.

**Michael Schiff:** it’s like we were seeing more of that prior to the RAG paper and the popularity of that

**Aparna Dhinakaran:** Yeah, I mean, I think, hyper personalization. You might do that. But you just need a good amount of data. So there are used cases, I think it matters. There are two more questions and then I think we might be at time. So, Eric–hey Eric–-Perhaps it’s their attempt to try to commoditize their competitors LLMs and Bard and OpenAI. 

Yeah, I think it could be. Overall, I think it’s a really good move for the open source ecosystem in general. I’d love to see if this actually helps with the pickup of using OSS models. I mean, I think one of the things that Open AI has done really well is, they have all of these deployments and different clouds now, and especially with Azure Open AI, you don’t even need to send open AI your data, so that’s been kind of a viable solution for people. So I’m curious if setting up the infra and running these OSS… I just just just curious if it’s actually going to be a real competitive solution for people.

**Michael Schiff: **Agree, I mean, they didn’t talk too much about running Llama2 in this paper, but certainly they did not make it feel like building a competitive model was an easy task. A good takeaway from this is, it’s expensive and it’s complicated.

**Aparna Dhinakaran: **We have one last question: what metric did they use for detecting bias? I think they actually had a number of different specific metrics. I can probably hop up to this section where they talk about it. So at a high level, they actually have a couple of different things that they’re measuring: truthfulness, toxicity and bias. And then, specifically, in the bias section they actually had a lot of different segments of people that they were looking at. 

**Michael Schiff:** I remember a section like that in the pre training where they were looking at the different demographics and the and the data set.

**Aparna Dhinakaran: **Yeah, okay, maybe it was up there. I can’t recall exactly where that is right now.

**Michael Schiff: **That’s the trouble with a paper that’s 77 pages.

**Aparna Dhinakaran:** Okay, so demographic representation in terms of… And I think they listed out actually all the different documents that they were actually using. And they did, I think, an analysis of bias across all these groups. So I’m not sure if there’s like a single metric specifically in the paper. But they listed at the very least. 

**Michael Schiff:** They say they use Bolt to study, and full disclosure I’ve not read that paper so I don’t know the details of Bolt but the analysis of the pre training and ensuring that the training data included a spread of all demographics and the acknowledgment of the potential for demographic or racial. Again, I think, speaking to this paper, being maybe less technically interesting and more sociologically interesting–that focus of like, we’re going to ensure that we’re feeding this language model data that has an adequate representation of these different demographics. And that it’s not going to completely erase something from its understanding of the world.

**Aparna Dhinakaran**: If anyone’s interested there’s a workshop that’s happening right after this. In about 10 or 15 minutes. That’s actually focused on we’ll talk about search and retrieval, RAG, how to link your private data to LLMs and ways that you can actually troubleshoot that in the real world. So definitely check that out, it’s in the chat. But this is a slightly different paper reading than we’ve had before, we got a little bit more of the ecosystem. So hopefully this was an interesting twist!

Thanks everyone for joining. Thanks. Michael.
