---
title: Composable Interventions for Language Models
topic: models
subtopic: reasoning
secondary_topics:
- prompt-engineering/techniques
summary: Deep dive on composable interventions for language models, covering techniques
  for steering or modifying model behavior.
source: arize
url: https://arize.com/blog/composable-interventions-for-language-models/
author: Sarah Welsh
published: '2024-09-11'
fetched: '2026-07-11T04:49:52Z'
classifier: codex
taxonomy_rev: 1
words: 6832
content_sha256: a3e830de2123340eb8cbe52d4d120c1f7e4abfc8e18771fffc0e66eb3cedc092
---

# Composable Interventions for Language Models

![Composable Interventions Blog image Sally-Ann Delucia and Kyle O'Brien](https://arize.com/wp-content/uploads/2024/09/CPR-RAFT-blog-1021x560.jpg)

              # Composable Interventions for Language Models

## Introduction

We’re excited to be joined by Kyle O’Brien, Applied Scientist at Microsoft, to discuss his most recent paper, Composable Interventions for Language Models. Kyle and his team present a new framework, composable interventions, that allows for the study of multiple interventions applied sequentially to the same language model. The discussion will cover their key findings from extensive experiments, revealing how different interventions—such as knowledge editing, model compression, and machine unlearning—interact with each other.

## Watch

## Listen

## Dive in

- [Read Composable Interventions for Language Models](https://arxiv.org/pdf/2407.06483)
- [Read Kyle’s Twitter Thread](https://x.com/KyleDevinOBrien/status/1810867690237743489)
- [See more paper readings](https://arize.com/ai-research-papers/)

## Analysis

**SallyAnn DeLucia:** Welcome, everybody. Thanks for joining us. We’re gonna get started in just a second. Here we have a really great presentation, and we have an author with us today, a contributor which I’m always super excited to have–Kyle. We’ll do some intros in just a second.

While people are joining us. I do want to give just a little shout out to an agent session that we’re doing a workshop, really. It starts on September 10th, and it’s a 6-session event, it’s gonna be running weekly.

We’re going to have some really awesome guests joining us like we’ll have Jerry from LlamaIndex joining. We’ll have a slide when we start presenting for y’all to get information. And we’re dropping [the link here](https://arize.com/resource/ai-agents-mastery). But yeah, if you’re interested in learning more about agents you wanna learn how to, you know, build with these agentic workflows. You want to learn how to evaluate them.

It’s going to be a really great session for you.Definitely invite you all to register and save your spot to join us. But with that Kyle, we can jump into it.

**Kyle O’Brien:** I’ll go ahead and present my screen. Can you all see my slides?

**SallyAnn DeLucia:** Yeah, looks great.

**Kyle O’Brien: **Fantastic.

Hey, folks! My name is Kyle, and I’m really excited to be speaking with you all today. Thanks SallyAnne and Sara for the invites.

I’m an Applied Scientist at Microsoft and a community researcher at Eleuther AI. I’m going to be talking about this research direction that some collaborators and I recently proposed and wrote a paper on discussing this problem, setting up composable interventions for language models.

We’re going to be talking through some of the high and the high level insights from our paper, trying to have as few tables in the slides as possible. But we’re only really going to be scratching the surface.

I recommend that if folks want a good primer on this work, to check out [the Twitter thread that I wrote](https://x.com/KyleDevinOBrien/status/1810867690237743489), and then, if that piques your interest, jump into the paper itself.

**SallyAnn DeLucia:** Awesome. And for anybody joining late, I’m SallyAnn. I’ll be joining Kyle here. I’m a product manager here at Arize. Really excited. I think this research paper is really awesome. I always love a paper that is something that’s actually actionable, something that can help. You know, all the community members and people who are in industry here. So I’m really excited to drop in. We love these to be interactive as well.

So if you have questions for Kyle, or you want us to elaborate on anything, feel free to drop questions either in the chat or the QAI know I certainly have some Kyle. So with that I’ll leave it to you to get us started.

**Kyle O’Brien:** Certainly I don’t know if I’ll be able to keep an eye on the chat. But SallyAnn and Sara, if one of you could interrupt me. If any interesting questions come up.

**SallyAnn DeLucia:** Totally, I’ll keep eyes open for you, and I’ll let you know if we have something to discuss.


**Introduction to Problem Statement: Composable Interventions**


**Kyle O’Brien:** Fabulous. So language models are really fantastic. I know that’s not quite what the title of my slide says, but I think, just to give credit where it’s due. The capabilities we’ve seen are really in the advancement of capabilities. Velocity is really remarkable. I had a professor only a few years ago telling me: Oh, with deep learning, maybe you can get strong capabilities in one domain. But you can’t have a model that’s good at multiple tasks.

However, that turns out not to be the case. If you can just scale and get really good at predicting the next token, you learn all these other capabilities that are instrumentally valuable, like translation, summarization, arithmetic, poetry, and so on.

But even though we’ve seen these rapid advances, there’s still some foundational problems which I don’t think obviously seem like they’re being improved with scale. In some cases they actually become worse with scale.

And while there’s still many limitations with language models that researchers and practitioners are working hard to solve, this is how I kind of think about them is they broadly fall into these three categories. Although, there are some others that don’t fit quite as nicely either, that are beyond the scope of our work.

But first off, and perhaps the most top of mind for people is language models are expensive both to train–that’s well understood, even for a relatively small model that maybe is only a few billion parameters, which maybe a year or a couple of years ago would be considered a very large model as well. But even if you had your 3 or 8 million parameter model that can still require significant amounts of money in the form of compute to train, and even to run inference as well, especially in a high throughput setting, where you maybe need to have multiple instances of your mobile, hosted and have high uptime, etc.

So models are expensive in terms of their resources generally, regardless of how you’re using them.

Additionally, at least the kind of parametric knowledge that models have, what they learn from training about the world.

This can be incorrect or outdated, especially if we’re hosting our model in production in a setting where the world’s changing, and it needs to be able to provide updated information.

Especially in democracies for example, the leaders of countries change fairly frequently. If you ask who’s the leader of so and so country, it might give an outdated answer. We have these knowledge cut off dates with many of the most capable models.

Or what the model has learned is perhaps information that is incorrect even at the time of training. So models factual knowledge can be incorrect, outdated, and this can be a con for deploying models or present a challenge for practitioners that want to provide a strong and safe user experience.

Additionally, and perhaps more speculatively, this is getting increasing interest in research lately is that models, perhaps can be unsafe.

This can take many forms, both in terms of more well understood harms more related to say, responsible AI, many of these are well understood. This is bias propagating existing harms that are perhaps learned from training data sets, and can lead to again subpar and unsafe user experiences.

Models can also learn dangerous capabilities or dual use knowledge such as if you train a model on the internet, you may learn some useful information around how maybe offensive cyber security or other perhaps dangerous capabilities.

Or even more prosaic settings. Your model may be trained on copyright information that the legal provenance has changed since training such that you want the model to forget this training data, or it’s trained on individual user information that you may want the model to forget.

While this takes the form of many harms, this can maybe broadly be thought of as the model is unsafe or unaligned with the operator’s values.

It’s unclear if scaling is going to solve all of these problems. Even in some cases, especially with maybe the expensive part, that’s only going to be getting more expensive.

**Post-Training Interventions: Model Editing, Unlearning & Compression**

This kind of leads to mitigations that have been studied and are beginning to be deployed in industry that I broadly refer to as “post training interventions” or interventions.

![List of Post-Training Interventions](https://arize.com/wp-content/uploads/2024/09/Screenshot-2024-09-11-at-5.48.42 PM-1024x576.png)


For the previous concerns, you could perhaps retrain your model from scratch. In the expensive case you could perhaps distill your model into a smaller version, using like a student teacher type of setup for outdated factual knowledge and for safety, perhaps you can identify the parts of your training data set that is leading to this undesirable behavior and modify your data set such that you retrain the model, and the model now has, say the updated factual information, or is no longer exhibiting the unwanted or unsafe behavior.

But A.) Identifying what’s wrong with training data sets can be challenging. But, more importantly, this is an expensive time consuming process that is beyond the reach of many practitioners. Especially if you’re leveraging a pre-trained model produced by another organization or produced by others and adapting it to your domain, chances are you can’t retrain one yourself, for example, even if you have the training data sets available.

With this kind of universal problem, these kinds of post training interventions are looking to solve them by making comparatively lightweight modifications to your model to address these different concerns.

Some common techniques across the three different categories of interventions that we studied in this work is model editing.

If you maybe heard of the “Eiffel Towers in Rome” kinds of papers and things like that, these are Updating the models factual knowledge by making relatively surgical modifications to the model, perhaps by doing some very lightweight fine-tuning or modifying the models in a more interpretability-inspired approach. So model editing is maybe largely focusing on useful literature and on updating actual knowledge.

Then there is unlearning which kind of alluded to many of the challenges here in discussing safety earlier. Perhaps you want the model to forget something for one reason or another. Unlearning techniques were originally motivated by a lot of privacy concerns such as Right to be Forgotten laws, but these are getting increasing interest as well.

Since language models are really good at learning stuff, but sometimes they’re learning things that you don’t necessarily want them to have learned.

And then, lastly, and this is the most widely applied set of interventions in industry today is compression. These are perhaps the most valuable testing with quantization being the most common one.

These take your model and modify them to be more resource efficient. They require less DRAM, and during inference, and there’s even been some efforts to be able to train your fine tune models reliably while also being compressed.

The trick here is that you reduce compute requirements while preserving overall performance.

So these are all interventions that have been studied commonly in the literature, and are beginning to slowly but surely get more deployed in practice.

**More on Practical Interventions **

However, a limitation in how interventions are studied today is they’re largely studied in isolation. If you have a paper or a blog post often talking about some new model editing or quantization technique, the convention is to only apply that intervention to your model and no other interventions. This makes sense from a scientific standpoint in that you really want to isolate the causal effect that applying your intervention has on model performance.

![Practical interventions should be order invariant and not regress overall perf](https://arize.com/wp-content/uploads/2024/09/Screenshot-2024-09-11-at-5.50.19 PM-1024x575.png)


If you’re working on a new quantization technique, you might want to say: Oh, I can lower the bits to this level and might still preserve overall performance more than baseline techniques. But a practical dimension that is neglected in the current literature is this need for interventions to be composable. If you think of these 3 axes of maybe concerns one might have when deploying their model, you would want your model to be resource-efficient, or perhaps you also wanted to be able to update your model’s factual knowledge and forget other knowledge without retraining from scratch.

So you might want to be applying more than one intervention to your model. You might be applying to multiple. And the interactions between interventions is understudied.

You would want your interventions to be order invariant, in that it doesn’t quite matter the order and of the interventions which you do apply. It shouldn’t matter that much for an intervention to be maximally composable and practical, whether you edit first and then compress or compress, and then do unlearning after, this can be useful if you perhaps don’t know ahead of time, which interventions you’re going to apply.

And we don’t want to compress applying interventions sequentially to regress overall performance or the performance of these interventions on their particular metrics. Such as if we–besides measuring overall performance– if we apply some edits to the model, we don’t want to, then have a subsequent intervention, undo or corrupt those edits.

This is the problem that we study in our work, is for these popular interventions, study in the literature across model editing unlearning and compression, how composable are popular interventions? And that this is an important requirement for them to be kind, especially for editing and learning, move beyond an academic interest and be actually techniques that practitioners can apply.

**Are Popular Interventions Composable?**

![Are popular interventions composable?](https://arize.com/wp-content/uploads/2024/09/Screenshot-2024-09-11-at-5.52.26 PM-1024x575.png)


So I guess I began to touch on this in my previous slide, but this is the research question that we broadly study with our work for the techniques that we study for editing. We study the popular MEMIT model editing technique, along with some fine-tuning based approaches, a full parameter, fine-tuning in LoRA for data sets.

We use some popular question answering or question answer dataset in the model editing literature, and we use various editing metrics. We study two types of compression: weight pruning where you learn how to make your model more sparse, but have a larger number of its weights set to zero while still maintaining overall performance. And quantization where we reduce the precision of our models weights which takes up less compute. And it’s perhaps one of the most popular compression techniques.

And then for home learning, we study two popular unlearning techniques, gradient ascent, where we essentially flip the loss function and try to make the model minimize the likelihood of the correct token on a different or on some unlearning distribution.

And then we study a technique that I’m a big fan of–representation misdirection for unlearning or RMVL. And this is a recently introduced unlearning technique that intervenes on the model’s activation inside a given layer which I’ll discuss a little bit more in subsequent slides.

But to measure overall performance despite as well as these intervention specific metrics, we largely use MMLU. There’s many different ways to measure overall model performance, that’s one of actually the big open questions in negative modeling is, what does it mean for a model to be capable?

But in our case, we largely focus on MMLU and all of our interventions are applied to Llama 3, 8 billion. a

**SallyAnn DeLucia:** I’d love to hear a little bit more just on those metrics there. Just curious, and you might be getting to this later. But is there a way we could think about this, of how these composability metrics align with any of our real world performance requirements? Can you elaborate on that a little bit?

**Kyle O’Brien:** Certainly. When thinking about composability, order invariance can be thought of as kind of like reducing headaches for practitioners, it’s easier to use interventions if they don’t need to be applied in a particular order.

Say, maybe you don’t know ahead of time all the interventions you want to apply to your model. Perhaps you deploy your model and then three months later, some new requirement comes up where you need to update its factual knowledge. Maybe you don’t know ahead of time that that’s gonna happen.

So you want to choose a compression. But you’re gonna compress your model right out of the gate, right when you deploy it. Perhaps you want to choose a model that, or you should choose a compression technique that’s been shown to be more order invariant with other interventions, but keep your options open so you don’t need to maybe retrain your model or do all of your compression again from scratch.

I don’t go into the equations that much in this presentation, but for folks who are interested. I recommend diving into the paper and the Twitter thread. But this is largely focusing on just what’s the maximum performance that you can get when you pair two interventions? And then you can compare that against performance if you didn’t apply any interventions, or you apply only one.

Because let’s say you have your original model, you apply some editing, but then you apply quantization, and that reduces overall performance. Or maybe your top level performance measured by MMLU remains the same, but your editing performance goes down.

That order free error will track that drop in your editing profile. So they’re some fairly simple formulas. They’re a useful way to think about how performance along different axes changes when you begin composing multiple interventions together, and that can help you choose, maybe, which order of interventions to apply, or which specific interventions maybe you shouldn’t apply.

**SallyAnn DeLucia: **Makes a lot of sense, thanks.

**Editing and Compression**

**Kyle O’Brien:** Certainly. Now I’m cycling to maybe seven of the main points or findings that my collaborators and I–our takeaways from conducting this work. There’s a lot of graphs and line charts and I won’t analyze them all individually. I recommend folks going to the Twitter thread or the paper. We want to look at a lot of performance of these individual interventions.

![Editing and compression](https://arize.com/wp-content/uploads/2024/09/Screenshot-2024-09-11-at-5.55.02 PM-1024x577.png)


But while there’s some variance across the specific interventions we study. And that’s one of the findings that we found interesting, I’m going to largely use this presentation to talk about our kind of meta themes or heuristic that we found.

So we start with pairing, editing, and compression, and for our experience we generally do these comparing two different classes of interventions together. When we’re looking at editing and compression, what we generally found was that compression can degrade model editing performance, especially at more aggressive levels of compression. Points one and two are pretty similar. But for weight pruning, what we found was that it’s generally better to apply your edited edits after you prune your model. And to a similar extent, but less so with quantization, what we find is that if you edit first and then compress afterwards, these compression algorithms tend to undo or corrupt the previously successful edits.

For folks who are very interested in the model editing part of this, this is interesting because this perhaps shows that edits aren’t in some sense robustly or deeply modifying the model. So that if you modify your model just a little bit with compression that can begin to undo your edits. This shows that with the model editing literature that may show very strong editing performance, if you only apply their editor, if you then further modify your model, then those edits are, you get become undone.

With editing and compression, if you’re doing aggressive levels of compression, such as if you’re maybe pruning more than a quarter of your model, or compressing below 8 bits, or quantizing below 8 bits, then, if you are going to be editing as well, you should be editing after you do your compression.

And composability can vary by method and have some variance, by the particular techniques within your class of interventions. So what we find is that quantization is a bit more composable than weight pruning.

And between GPTQ and AWQ– the two types of quantization techniques that we study, there can be some variance across which, yeah, performs better more extreme levels of compression in terms of top level performance, but also their composability.

And that, MLU or overall model performance, doesn’t seem to really track these challenges of composability. Performance will remain fairly steady, even if we see cases where compressing or editing first and then compressing might be undoing edit. And when there is imperfect composability, this lends more credence to the idea that it’s useful to have composability driven metrics.

We next study unlearning and compression, where we find a similar effect, that compression and unlearning can have challenges composing well together, but we find the ordering to be opposite. Interestingly, what we find here is that in contrast to editing. It’s better to apply unlearning, before you do decompression. There’s something about these unlearning algorithms that we study that are some of the most popular in the literature, that it’s more difficult to modify the knowledge of an already compressed model.

And while this hasn’t been proven in the literature, or studied rigorously, it does not seem particularly surprising that maybe if you compress a model, its knowledge is maybe some in some sense more compressed in a way that makes it harder to modify with these post training techniques.

That’s something to keep in mind when applying compression is, if you compress your model modifying it afterwards, it might be more brittle in some sense, even if it’s overall performance metrics without any modifications remain strong.

And that in our learning we found to be one of the clear cases of order, sensitivity, or order, invariance being important. So two of the three unlearning techniques were formed quite well. Gradient difference in RMU, gradient difference in that work. It extends gradient descent where you’re trying to minimize the likelihood of the correct token on some online distribution.

This is like the opposite of our original loss function, but with gradient difference, we have an additional regularization term. We’re also trying to maximize the correct token on some unrelated distribution. What we generally find is for unlearning, the RMU and gradient difference have similar unlearning success. But gradient difference is far more sensitive to ordering than RMU.


![Weight pruning](https://arize.com/wp-content/uploads/2024/09/Weight-pruning-graph.png)



This suggests that in this case [ above ] while they both are equally good unlearners. Largely RMU modifies the model in a way such that its unlearning is more robust to additional interventions being applied.

**Editing and Unlearning Results**

And then our last main set of results is with editing and unlearning. And this one, we’re pairing the editors like fine tuning, LoRA and Nemet, with our learning techniques, gradient descent gradient difference, and RMU. A result that I was especially interested in which hasn’t been cited yet is can you modify a model’s knowledge with different techniques or from different directions. I suppose these editing techniques are modifying a model’s and all like factual knowledge by making very targeted fine tunes generally.

![Editing and unlearning](https://arize.com/wp-content/uploads/2024/09/Screenshot-2024-09-11-at-5.58.14 PM-1024x575.png)


This is where updating, like the answers to specific questions. Whereas with the unlearned techniques we studied, we’re trying to forget a broad distribution of knowledge.

In our case we were evaluating our learning on the weapons of mass destruction proxy data set where it’s focusing on making the model forget a broad set of knowledge that can be potentially dangerous, or a proxy for dangerous knowledge, such as information about epidemics, or how to do hacking.

In this one, we’re not trying to forget, maybe specific facts necessarily, but rather broad distribution of knowledge. And we find that editing and unlearning can be quite composable, but it depends on the technique.

With RMU it’s quite composable. With the order invariance being unimportant for gradient difference and gradient descent. We find that similar to before you can achieve a strong unlearning performance, but the order sensitivity is much more important, or it’s more sensitive to ordering, which makes me excited about some of these representation engineering type techniques, which RMU is an early example of, where we’re modifying the instead of fine tuning a model. In the end, we’re choosing a specific layer in trying to steer its representations or activations in some way or change to kind of steer model behavior.

It’s an interesting technique that I recommend folks check out RMDL.

I think for the broad takeaways, we’re only scratching the surface on this direction. And one of the main points we’re interested in is galvanizing interest in studying composability when we’re introducing new interventions in the literature, because this is an important requirement for making interventions practical to use in production, which is ultimately what we want them to be. If we’re going to realize the positive impact. I’ll talk more about my manifesto on this. And this is one slide. But for our empirical results, what we broadly find is that compression, this most popular class of interventions, aggressive compression, which more and more there’s more and more interest in, is more struggles to compose well with other interventions.

While the field is beginning to look at more aggressive forms of compression, like 4 bit quantization, higher degrees of sparsity, it’s important to understand that while yes, you may, this may reduce your maybe GPU footprint.

It also may tie your hands more in terms of what other modifications you can make to your model editing and unlearning generally compose. Well, we can modify a model’s kind of knowledge base in some sense, using different techniques.But the specific techniques, and but in terms of order, sensitivity, specific techniques, matter and while this is like a useful, useful kind of same recheck overall performance. Doesn’t really capture things like maximum composed error for our intervention, specific metrics for order, sensitivity.

So while you still want to whenever you’re making a new intervention, or any sort of modifications to your model have really robust overall performance evals. Metrics like your edit success or unlearning success–These intervention-specific metrics, you’ll need to measure those as well along with your overall model capabilities.

**Future Work on Interventions**

This is kind of the first of what we think can be a quite fruitful direction for practitioners and researchers to look into for making interventions more practical. Some specific directions that my collaborators and I are thinking about, but also I’ll be excited for other folks to look into is expanding our scope of interventions. There’s many proposed in the literature, and more things like every week or so I see some new interesting paper come out. So, expanding out the set of interventions that we do study.

![List of plans for future work including studying more interventions, studying across LM families, composability scaling laws, and complicated compositions.](https://arize.com/wp-content/uploads/2024/09/Screenshot-2024-09-11-at-5.59.28 PM-1024x576.png)


A limitation of our work is that we only focused on one with 3 8 billion. And while this is I’d argue a fairly representative model because, since it’s amongst the most capable at its parameter count, there could be some factor where our results may not generalize across model families.

We have run some initial experiments as a part of our NeurIps reviews where we have a studied mistral, 7 billion. So quite a similar model and find that our results seem to generalize.But more work is needed along this direction. What I’m especially interested in is maybe scaling laws for composability.

As models become larger, how do these factors change? Maybe it could be that if you have a really capable hundred billion parameter model, that even when you do aggressively compress it, maybe it’s large enough such that, modifying its compressed knowledge is easier in a way that bringing a billion model in might be. This is largely an empirical question that currently remains unstudied.

And then, lastly, we’ve always studied pairs of two interventions in this work, largely through the practical reason, I think the combinatorial explosion of, we have a dozen or so interventions. You’d make all the pairings together, each one typically requires, like an hour on an a 100 it’s challenging to do a wide set of experiments with increasing the cardinality of your maybe set up interventions. You’re trying to see if you’re maybe applying 3 or 4 or 5 different classes of interventions. How does that affect performance?

And all this together can be broadly kind of characterized, and maybe my motivation for this work, if I had to sum it up, would be these interventions are very exciting way to make models better in a way that doesn’t require retraining. None of us want to retrain models. Even the folks who know how to do it don’t want to. But much more work is needed to make them practical.

We have seen success with compression and interventions being widely used. I think it’s possible for other interventions, such as editing and unlearning to be just as practical. It’d be really great if we could just super easily modify our models, knowledge, or its answers to questions without having to do complicated fine-tuning, but much more work is needed, and it would be really awesome if we could get this to work. I think it would go a long way towards making models more aligned with their operators, and easier to control and adopt for a greater variety of use cases.

This work was a fantastic collaboration. There were a lot of folks in this team, but the principal folks, were Arinbjorn, Tianjin were my fellow lead authors.

And then Tom Hartvigsen, at the University of Virginia was the main PI on this work. But we were part of a broader team, including the folks from Harvard, Oxford, and University of North Carolina.

I recommend checking out their work, they’re all really talented researchers. If you’re really interested in editing like model editing, I recommend checking out Tom Hartvigsen’s work. If you’re interested in compression, especially pruning, Tianjin’s work is really good. These are folks to definitely keep on your radar.

I’m happy to kind of open up the floor and answer any more questions. If folks are interested in chatting about any of this work or other things, or find some of this direction interesting. Hit me up on Twitter or check out my website, or I’m on LinkedIn.

Tanks for the invite. And I’m curious to hear what folks think.

**Q+A with the Author: Composable Interventions**


**SallyAnn DeLucia:** Yeah, I mean, I think this is an awesome paper. I really like that slide where you have kind of the 3 bullet points on like, what’s next. That was actually gonna be one of my questions. But you got ahead of me of what’s next, what’s the future of this work here?

We do have a few questions in the channel that I want I want to get to. But I think one thing that I think we should wrap up with is like, do you have any advice for practitioners looking to kind of implement any of these findings in their own deployments?

**Kyle O’Brien:** Certainly. Hmm. Let’s see, I think maybe to narrow the question a little bit. It would be, while our work does provide some heuristics, in general, if you’re going to use edit, if you’re going to be compressing your model, but you think you want to also do editing, it’s better to compress first, and then edit and things like that.

Really, these are kind of recommendations based off of the model that we studied, and the interventions, as with so many things in kind of machine learning or language modeling research, it might vary across scale and across small training regimes.

When in doubt just have really good evals. This is like a broad machine learning heuristic especially with my like more applied work that I do at Microsoft, just make sure you have really good evals for whatever you’re interested in, because there’s very little in the way of theory and heuristics. You can rely upon when working language models.

If you’re interested in applying a set of interventions, our work can provide some tips. But I would still recommend, have really good evals and just experiment with different combinations yourself.

**SallyAnn DeLucia: **Really great answer. Cool, alright. Some of  the questions in the chat. We have one from Matt asking if we could dive in or, I guess, drive home the interpretation of the surprising effect that, you know, editing after pruning hurts the performance while I’m learning a pruned model also hurts performance. Any thoughts on that?

**Kyle O’Brien: **Certainly, a limitation of our work is that we’re largely, to maybe use a 5-dollar word, phenomenological, in that, we look at how appliance interventions affects these top level metrics, but we don’t dive deeply into looking exactly what that properties of the different interventions are causing specific behavior.

That’s something I’m really interested in personally, but it was just beyond the scope of this work.

But if I had a conjecture, I don’t know. This is like, definitely, mostly just like half baked thoughts that, like collaborators and I have, but it might be that this is very half baked, but it could be that the way that other research has found in model editing, that the edits made to models seem to be fragile in some sense. Like, if a popular editing technique that really galvanized a lot of interest among editing was the roam technique. This is a great paper by David Bau’s lab. He’s a fantastic interpretability researcher, and also has a lot of great podcasts–recommend checking out their lab. But they were looking at things like: Can you change the Eiffel model? To think that the Eiffel Tower is not in Paris, but rather in Rome, and you can do that. They’re doing some very targeted fine tunes to them, internal to the model, but that if you rephrase the question sufficiently, or you ask some like logical follow up questions, then the edits kind of break, or they don’t seem to really deeply modify the models knowledge in some vague sense.

It could be the case that if you make these not really deep in some sense modifications to the model, and then you do something like pruning where? You’re setting all the weights to 0. And this, maybe, could be considered a fairly drastic modification of the models internals, even if the top line performance is maintained, maybe that shuffles the models knowledge in a way that undoes these lightweight edits.

As for why unlearning is robust to this, by contrast, I don’t see right now. Yeah, I think, it just goes to show this is very much like on the frontier. But that’s a great question, Matt.

**SallyAnn DeLucia: **Alright awesome. Yeah, they appreciate the answer. They think it’s a good showcasing of their thought process. Here we have another one coming in. It looks like it says:

In July a paper was published in *Nature* about how models collapse when trained on recursively generated data. So models could be trained on data generated artificially unknown to the developers, and that has not factually correct or updated data. They gradually degrade in quality before collapsing. And start to, you know, generate nonsense. Could these intervention interventions help combat these kinds of itch issues? Which ones that you mentioned, do you think would be suitable to kind of tackle this issue.

**Kyle O’Brien:** Now, that’s interesting. If I understood the question correctly, it’s this idea that as more and more the Internet becomes AI generated, which is a weird world to live in.

**SallyAnn DeLucia:** Super meta.

**Kyle O’Brien:** Future models are going to be trained on more and more AI generated data.

And there’s been some research that suggests that if you train models on AI generated data that you get some sort of collapse where models begin to get worse. It could be the case that maybe if you have some sort of model editing work where you want to preserve the model’s ability to answer these factual questions, that you could apply editing after you’ve done your training on additional AI generated data, and that causes the models actual knowledge to update and be aligned with what you want to say.

Notwithstanding the point I alluded to in the previous answer, where model editing seems in its current form to have limitations, that could be one way. On that note about the recursive training and collapse without being expert in it, my sense is that it’s still an open question, since you might be training on a mixture of AI generated and human text.

And, funnily enough, a big research direction in the leading labs right now is, how can we create synthetic data like we’re running out of data on the internet, how can we create new data using an AI to train another AI on that.

Funnily enough, being able to train future generations of model to maybe train GPT-5 on GPT 4’’s data, for example, something like that, is something that’s a big, open question right now. But a lot of people are trying to get it to work right. So that’s another cool research direction is synthetic data, and how training on that affects the robustness of your models.

**SallyAnn DeLucia: **Yeah, I think synthetic data is a really hot research topic. I think as this problem they’re describing becomes more and more prevalent. It’s needed that we have some kind of a way to combat that, so I’ll definitely be watching.

I guess we have two minutes. I’ll squeak in one last question here. Obviously, this industry and everything is evolving so fast. How do you feel like we can ensure that these interventions remain relevant and effective? Do you think we just have to kind of stay on top of what’s latest, continue to push research forward? Or do you think there’s some methods that will kind of withstand this rapid evolution?

**Kyle O’Brien:** I guess maybe the rational or mature answer would be, nobody knows.My hot take is anyone who really tries to make confident predictions about the future is a selling moonshine, and reminds me of my professors who are so confident that deep learning would never give you general capabilities.

But maybe in terms of practices that stand the test of time is, I mentioned it before–have really good evals. If you’re trying to measure your performance on some task, make sure you have a really good measurement regime in place.

And also understand that, maybe if you have some model that’s deployed in production that takes in new data over time. Understand that your distributions might shift.

I was previously doing in my work at Microsoft, a lot of ML for hate speech detection in the news domain. And in the news domain of all things is especially extreme, since you have Black Swan events and the news is constantly changing, this was kind of like the distribution shifts on steroids in some sense.

And what was really helpful for us is to just have really good measurement, because the nature of your distribution is changing. You can’t guarantee that your model will generalize to that new distribution, so try to measure that ahead of time.

That’s kind of maybe where my intuitions are today on that question, at least, how I think about the future.

**SallyAnn DeLucia: **Yeah, I think it’s a great answer. Things are moving so fast, so I guess we’ll see but, Kyle, thank you so much for joining us. This is a super interesting paper, like, Kyle said. Feel free to take out. Take a look at his twitter, thread, dive into the paper. I think there’s a lot of really helpful stuff here. And just thank you again, Kyle, for joining us. It’s been a lot of fun.

**Kyle O’Brien:** Yeah, it’s been really fantastic chatting with everyone. Yeah, again, hit me up. Feel free to hit me up online. If you’re interested in any of these directions, or some of the other words I’m looking into.

I forgot to do it at the top, but also big shout out to Eleuther AI as an open source research community. They’re how I got into research. And I’m involved with some of their projects. So if you’re interested. I mean, it’s just a very fun discord of people who are really on the cutting edge of our research and sharing papers and talking about stuff.

I recommend checking out or getting involved in open source research. I recommend reaching out or taking a look at the Eleuther AI Discord.

**SallyAnn DeLucia: **Awesome stuff. I know I’ll definitely be taking a look. Well, that’s it. Everyone for today. Thanks so much for joining us, and we’ll see you on the next one.

**Kyle O’Brien: **Fantastic thanks y’all.
