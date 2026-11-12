---
title: 'Fine-tuning models, AI and Hollywood: A conversation with Oxen’s founder Greg'
kind: blog
topic: null
subtopic: null
secondary_topics: []
summary: null
triage: null
skip_reason: null
source: baseten
url: https://www.baseten.co/blog/fine-tuning-models-ai-and-hollywood-a-conversation-with-oxen-s-founder-greg
author: Madison Kanna
published: '2026-02-05'
fetched: '2026-11-12T06:10:58Z'
classifier: null
taxonomy_rev: 2
words: 3158
content_sha256: dc6f9d42f3bce5126dcd5850d48acfed445c7de52e79f436d811db72fa1eb78e
---

# Fine-tuning models, AI and Hollywood: A conversation with Oxen’s founder Greg

Community
# Fine-tuning models, AI and Hollywood: A conversation with Oxen’s founder Greg

In this interview with Greg, founder of Oxen AI, we discuss his journey from IBM Watson to building fine-tuning infrastructure.


- Authors
- Date
- February 5, 2026

TLDR

In this interview with Greg Schoeninger, founder of Oxen AI, we discuss his journey from IBM Watson to building fine-tuning infrastructure, how Hollywood studios are using AI for pixel-perfect VFX work, the furniture industry's surprising use case that saved $40K per project, and why pairing version control with compute infrastructure is transforming how companies deploy custom models.

Yeah. So I've been working in AI since 2012, the very early days of deep learning. Right out of school, I joined a startup that was doing deep learning before any of the TensorFlows or PyTorches of the world. So we were writing our own neural net libraries from scratch in C++ training ConvNets. And then there was the AlexNet moment that really blew our minds, when this convolutional neural network beat all of the handcrafted features on ImageNet. So we just went all in on deep neural networks.

That was called Alchemy API, and that company eventually got acquired into IBM, into the Watson Group. Our job was going into IBM Watson that won Jeopardy back in the day and replacing all of the models that were logistic regression models or maximum entropy models with deep neural nets that could do the same but generalize better to the data.

IBM would go sell a big contract to be able to do some natural language processing task, and then they'd bring the requirements back to the engineering team. We were part of a fast domain adaptation team that would have to get our models to work in Korean on a financial dataset. We don't even speak Korean, but as long as we get the data, we're able to customize the model and then hit whatever accuracy the customer asked for.

So that was in the early days of my career and I did a bunch of reps of just going from a research idea to a production deployment. And almost every single time it just came back to what data we were feeding into the model. That kind of sparked the idea of Oxen. We actually started as a data management layer, version control layer for machine learning datasets. Because it's really just garbage in, garbage out or good data in, good data out. We started to see some traction there, but what's really been picking up is fine tuning some of these foundational models or open source models on the datasets. So pairing the data with the compute and infrastructure and letting a company own their own model end to end is really where we're seeing traction now.

Yeah, so we started a version control tool to replace Git. We actually rewrote the internals of Git to be able to scale to terabyte-size datasets. This was in the pre-ChatGPT era where these pre-trained models would take a ton of data and we were just saving them in S3 buckets with no sense of version control, no sense of what data trained what model. So that's where we started. Could we build a distributed version control that actually works? If you've ever hit the limits on GitHub, it's like two gigabytes of data that you can put in there. Ours scales to—I think our biggest deployment has 20 terabytes of data in it, and thousands of engineers collaborating on the same repository.

It turned out that a lot of people were using the version control tool to fine tune their own models as a natural use case for it. Because you have to pair what dataset went with what model, and you might have a bunch of models deployed out in the edge or models deployed in your own infrastructure. And being able to tie that specific version of the dataset to the model weights – both the dataset and the model weights can get pretty hefty. The DeepSeek models are 600 gigabytes alone, the model weights. So how do you store and manage the connections between those?

Yeah. And they were having to home roll a lot of their infrastructure to build on top of our version control stack. So they would take it, wire it up to their compute infrastructure, and have their own training loops. The time to value for some of those customers was the time that it took their engineering team to integrate the version control tool with their training infrastructure. So we were like, what if we just paired it with a training infrastructure that kind of came out of the box? One click, go from your dataset to a fine-tuned model and then eventually deploy it into your production setting.

Yeah, so we work across a couple of different modalities. There's the classic LLM use cases for text in, text out, classification, agents making tool calls or name your LLM use case. What we're seeing is a lot of people who would build the MVP of their application on OpenAI or Anthropic just to see if this is possible. And then they start to run into either accuracy because it's out of distribution, or speed or latency requirements that they need, or even just privacy. I just don't want this data leaving my infrastructure and going to some other cloud. So they either take the data that they've collected in production or do some hand labeling, fine tune their own models and now they have full control over the experience from a latency, cost, or accuracy perspective. So that's on the LLM side.

And then on the diffusion model or image generation, video generation side, we're seeing a lot of people who care a lot about the quality of the output. There's the meme of AI slop going around with Sora and all of these image gen models. We're based in LA so we have some clients that are Hollywood grade. They need it pixel perfect on every single frame and they're gonna have their VFX coordinator looking at it and marking it as an AI shot. But it has to look as if it's not. In that case, quality matters a lot and fine tuning can take you from an 8 out of 10 to a 10 out of 10 in quality.

Yeah, yeah. And you know, these video gen models are getting pretty good. You see the Google models or Sora—those are more the consumer grade ones that people are playing with. But then there's the open model ecosystem. Ones coming out of Alibaba called Wuan, and some of the Chinese labs are actually leading a lot in the open ecosystem.

I had a demo last night at AI Tinkerers trying to describe how well these models are working. The real Hollywood use case is they messed up one of the shots and they accidentally had the actor wearing a white blazer in the scene when it should have been his red one. Everything else about the scene was amazing, but can we just swap him into the right outfit for this ten second clip? It has to be pixel perfect or they would have to call everybody back in, do the reshoot again. If we can do this with AI, we'd rather do this with AI.

So just as a quick demo last night, I took that—obviously I couldn't use the real data—but I took Pulp Fiction and that famous scene where Samuel L. Jackson and John Travolta raise their guns slowly. I was like, can we swap the jacket that Samuel L. Jackson is wearing into a cool red leather jacket instead of his suit? And how quickly you can do that and how high quality you can get these models is just blowing my mind every day.

I think it's interesting to see the shift in Hollywood. I'd say two years ago you saw the actors strike and you saw a lot of people in Hollywood being against using AI. And more recently I go to these ComfyUI meetups. It's kind of this node-based editor where each one of the nodes can be a diffusion model or some sort of AI process, and they'll be chaining together AI tools. So it'll be video in, and then the first module extracts masks. So the mask might be the jacket itself. So in each frame it's got a segmented out jacket, and then you're passing each one of those frames into another model that's filling in the jacket with the real thing, but you're not touching any of the other pixels in the frame. It's just filling in where that mask is. With that level of control plus a little fine tuning, you can get these things to be pixel perfect. I wouldn't even be able to tell that AI was involved.

Yeah, it'll be interesting. You know, these things do really well for five second clips right now. So for these bugs or just shots that they need a swap, I feel like it's really good for that now. But for longer form film or movie, they're having a hard time with character consistency or scene consistency between those five second clips being chained together in a fully automated AI way. So I feel like we're still a ways out from that.

And I still think people are gonna connect with the humans in the movie. You're gonna go see the Nicole Kidman movie because you really like Nicole Kidman, not your favorite AI bot actress. So I think there'll still be humans in the loop, but I think I frame it as a VFX problem more than an AI problem. You're just speeding up your VFX team who might be adding the cool CG that might take them a couple weeks to work on before, but now they can do in a day or two.

Yeah, actually the advertising and branding. You can think of Super Bowl commercials or even music videos. We're seeing traction in these. These brands have big budgets. Name your favorite soft drink and they have to make a 30-second Super Bowl ad. They will be fine tuning actually on their previous catalog of things that they've Photoshopped in the past or things that their VFX artists have done in After Effects. So they have this big catalog of things that they've created before, and that's a great dataset to fine tune a model on. But now it frees up their artists to get creative with the scenes and try something that might take a month to do in post, but they can just prompt their way into a really cool animation or something like that.

So we've seen traction with the agencies who are then going and pitching out to multiple brands. And this agency has the problem of. I fine tuned a model for Brand X and a model for Brand Y and a model for Brand Z—and being able to have all of those datasets sectioned off from each other and you know exactly what version of the dataset trained what model. That's one thing that they're loving the Oxen platform for, because the version control plus the data storage plus the fine tuning is the perfect storm for them to scale up their operations.

Yeah. So originally met you guys, I think I was presenting at one of our Friday events we do with the community and we were talking about training small models. Ebola was actually in the audience and he came up to me after and he was like, you guys working with a lot of customers with small models? And then he was like, are you doing any fine tuning? And I was like, our customers are, but we haven't quite integrated that into our product yet, but we're thinking about it. And he was like, well, let me let you in on a little secret. We're launching some training infrastructure, maybe we can partner on seeing what it would look like to bring the datasets and the compute together and see if we can have an all-in-one solution for the customers to go straight from dataset to model weights to deploy.

So it was like a month or two of us talking about it and then we decided to tackle it and within, I think it was like a month and a half, we had the end-to-end prototype and we started to have customers kick it around. And the reaction was, oh my God, I used to have to spin up all of these RunPod instances myself or manage my Lambda Labs or Vast AI cluster. And I'd kick off a training job and know that if I didn't wake up at 4 AM to kill it, I'd just be spending extra cash on this GPU without it spinning down.

And once we integrated the end to end datasets plus fine tuning infrastructure from Base 10, it's literally one click to kick off an experiment and we see customers kicking off 10 experiments at once. They're training on a bunch of different GPU clusters and then they all wind down and save the model weights back at the end. So it's given our users superpowers of being able to explore the hyperparameter space and then look at all the outputs of all the different models and be like, ooh, okay, learning rate of 0.3 works well and batch size 4 and time step type sigmoid. Try all of these combinations in parallel without having to have a PhD in machine learning or worry about out of memory because they didn't pick the right GPU or any of that.

So it's really been a magical experience for the customers. And it's been fun to see how quickly they can go from I have an idea, I wonder if this would work, to oh my God, it works. And we just get these messages from our users on Discord like, I can't believe that worked the first time we tried it. Because normally a machine learning engineer would spend a week or two just fiddling with things.

Yeah. So we use you guys behind the scenes under the hood. And so we've set up for each one of these open source models—they have different GPU requirements. So you know, if you're gonna fine tune GPT-J or something, you might need a cluster of 4x H100. An H100 has 80 gigabytes of VRAM, and to do a full fine tune on that, you need 240 gigabytes.

So we've done the mapping between what model are you training, how big of a dataset do you have, how big is your batch size, how big is your sequence length, so that when you kick it off, you can have the confidence that I'm not gonna spend a lot of money on just an out of memory error. So we've done that math and then it's been great partnering with Base 10 because we don't have to worry about where do we get those GPUs. Is AWS out of capacity, do we get them from GCP, do we roll our own on Lambda Labs? It's just like we can focus on the software and you guys can focus on getting us the GPUs we need. So having that be API driven has been a really nice experience for us.

We use Baseten for that right now, and there's kind of two use cases that our customers come with us for. Either they want access to the raw model weights and they just want to download it into their own infrastructure or even onto their laptop and run it locally at this point, because some of the models can run locally pretty quickly. Or they want to deploy it to a managed service.

So we do the same kind of thing that we do on the fine tuning side of, okay, I know it took 4x H100 to fine tune this model, but it only takes one H100 to run it in production. And so we set up all the Docker images, set up all the dependencies, and let you just one button deploy that goes to a cluster of GPUs on Base 10 and then they can just hit it with either our API key or eventually we want them to be able to bring their own.

It can be a bit overwhelming. I feel like every week there's a new launch of a new model that claims that they're better at X, Y, Z. So the first thing I always tell customers is make sure that you understand your requirements first and foremost and what problems you're running into in production before you just go and hot swap a model. Because who knows, just because ChatGPT got better at coding doesn't mean it's gonna be better at your document processing use case. So that's the first thing that I say—make sure you have some sort of baseline or benchmark that you have in place so that you can confidently switch between models.

But on a more practical side of things, or just more opinionated, I do think the Qwen series of models have been really impressive and that lab has just been shipping like crazy. So there's something that they've done in the Qwen language models that make them pick up information super quickly, and we've seen the 8 billion and 4 billion parameter models there be really good if you have a very well defined—if you don't need it to also generate poetry because you have more of a business use case, those models can pick up that task really quickly and you can deploy it at scale, and even some coding use cases. You can picture like a Cursor tab—I'm not saying they use Qwen in the background, but I would guess they use Qwen in the background for that.

And then from a video generation side, I think the Wuan series of models are really cool from an open source perspective. I'd say they can get you even higher quality than a Sora generation if you're willing to give the compute to it. And that's also from Alibaba. So I'd say Alibaba's kind of crushing the open source game and I'd hope to see—I'm excited to see what Meta will do next with their series of models. I feel like the Llama models were very strong when they came out, and I have a sense that they're gonna drop something soon with their new super intelligence team that's gonna be the American version of that. A good new model. So excited for that too.

Try out [<u>Oxen.AI</u>](http://oxen.ai) or read more on Baseten’s [<u>work with Oxen.</u>](https://www.baseten.co/resources/customers/from-datasets-to-deployed-models-how-oxen-ai-builds-on-baseten/) You can also watch the full recording of this interview on <u>Youtube.</u>
