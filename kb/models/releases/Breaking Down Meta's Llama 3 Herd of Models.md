---
title: Breaking Down Meta's Llama 3 Herd of Models
topic: models
subtopic: releases
secondary_topics: []
summary: Technical overview of Meta's Llama 3 model family, including architecture,
  capabilities, and benchmark interpretation.
source: arize
url: https://arize.com/blog/breaking-down-meta-llama-3/
author: Sarah Welsh
published: '2024-08-06'
fetched: '2026-07-11T04:49:22Z'
classifier: codex
taxonomy_rev: 1
words: 7680
content_sha256: 268f7088d7c101eec995a431f38fca83eb5cafbd2b41852fe330bb82c0332cf6
---

# Breaking Down Meta's Llama 3 Herd of Models

![Chris Park and Aman Khan Chris Park and Aman Khan](https://arize.com/wp-content/uploads/2024/08/CPR-The-Llama-blog-1-1021x560.jpg)

              # Breaking Down Meta’s Llama 3 Herd of Models

## Introduction

Meta just released Llama 3.1 405B–and according to them, it’s “the first openly available model that rivals the top AI models when it comes to state-of-the-art capabilities in general knowledge, steerability, math, tool use, and multilingual translation.” Will the latest Llama herd ignite new applications and modeling paradigms like synthetic data generation? Will it enable the improvement and training of smaller models, as well as model distillation? Meta thinks so. We take a look at what they did here, talk about open source, and decide if we want to believe the hype.

## Watch

## Listen

## Dive in

## Analysis

### Llama 3 Overview

**Aman Khan:** My name’s Aman, I’m on the product team at Arize. I’m joined by Chris. Chris, you want to do a quick intro of yourself as well, maybe a bit of background. So, since you actually have the ML researcher background–it’s going to be relevant to the paper read.

**Chris Park: **Sounds good. I’m currently a software engineer here at Arize, mainly working on instrumentation and like the open source platform, we have: Phoenix. And I’m currently doing a masters in CS and AI at UCLA. So yeah, for the summer, working at Arize and having a great time.

**Aman Khan:** I think this paper read is a pretty interesting one, and as we jump in it’ll be pretty deep into model training and data prep. So, welcome everyone. How we typically like to do this is, we’re going to kind of give a bit of an overview. This is an interesting one, because it is a model paper read. Sometimes we do architecture, or sometimes we do, you know, other interesting papers we find, but this one is kind of coming on the heels of a pretty big drop last week for the open source AI community.

So what we’ll do here is sort of go through the parts of the paper that we found interesting. Feel free to pepper us with questions in the chat–we’re keeping an eye on the chat as well, and we’ll pick up the questions that seem relevant to the sections that we’re on. If we don’t get to your question, we might get to it later in the paper.

Or you know, just feel free to ask us, and we can try and work them into the discussion. Don’t hesitate to drop anything you find interesting. With that, I’ll kind of hand it back to Chris to introduce the paper for us.

**Chris Park: **Yeah. So let me share the deck real quick.

![Llama Models timeline covering Llama in 2023 to Llama 3 in 2024](https://arize.com/wp-content/uploads/2024/08/Slide-1-Llama-TImeline-1024x578.png)

So today, we’re going to be talking about the Llama 3.1 paper that Meta just dropped, which kind of improves the Llama 3 herd of models. And this paper is super long–it’s like 92 pages–so like Aman said, we’ll be going over the key points and things that we found interesting. And they’ll definitely like things that we will be missing. But I encourage everyone to kind of just look at the paper and read the sections they’re interested in.

So as an overview. We’re kind of just gonna go over what’s new, how they developed the model like pre training post training. And then these 3 key levers that they mentioned, as well as kind of the results, capabilities, and some of the discussions around this new paper.

And I think it’s kind of useful to talk about the timeline of like Llama development, and look at when it first came out versus what it is now.


So in 2023, when Llama first came out. It was a big deal, because it was like an open source foundation model, right, from a big company. And it had around, like from 7 billion to 65 billion parameter model sizes and a context window 2,048. And just the training data, 1.4 trillion tokens or one trillion tokens depending on the model size.

And then they released Llama 2, which kind of doubles the context window and then increase the token size. And for the training data, with a similar model, parameter size. And with Llama 3, what’s interesting is that they double the context window. But the pre training on that was 15 trillion token, so huge right? And that was just in April–that was a couple of months ago, I believe.

And then they came out with Llama 3.1, which is a really big deal because of this huge model with 405 billion parameters and 128,000 context window size with 15 trillion multilingual tokens.

So I mean the difference between a few months ago and now in terms of parameter sizes and context windows is kind of insane. And just looking at that timeline. Yeah, it’s they usually just double context window. But I guess in this case, in a couple of months, it’s just crazy.

**Aman Khan:** With basically keeping the number of tokens, you know, fairly constant there. And yeah, and scaling up the number of parameters as well. So a lot of really interesting stuff on the training side.

### What’s New with Llama 3?

**Chris Park: **Yeah, exactly. And what’s new about this is that they update the previous foundation models that they released for Llama 3, a couple of months ago. And like, we talked about the 400 to 5 billion parameter model size. So, and these foundation models, what’s big is that they also natively support multilingual capabilities, coding, reasoning, tool usage… which they didn’t really have before. And this kind of new flagship model they have, the 405 billion parameter model, is on par with a lot of the leading close source language models like GPT-4 and for an open source foundation model. That’s kind of huge.

And we talked about 128 K tokens context window. Big jump from just Llama 3, which was 8,000. And a lot of the data that they use was multilingual. So they have multilingual support, I think, around 8 languages.

![Text overview of what's new for Llama 3 including multilingual support, llama guard, and multimodal integration](https://arize.com/wp-content/uploads/2024/08/Slide-2-whats-new-1024x569.png)


And we’ll look at some of that later as well as some initial experiments on multimodal integration. So image, video, speech. But this is not released yet.

But I believe they’re going to incorporate this stuff onto basically all Meta platforms. And use these features, which I think will be interesting. And then Llama 3 they introduced for content safety filtering stuff like that. So a lot of big stuff. I think the key stuff is obviously just the huge flagship model, the context window and just the capabilities with multilingual coding and stuff like that.

And if you look at the table, they have the instruct fine tune models as well, which has a lot more capabilities.

So I think, in the paper they describe these 3 levers of development or high quality foundation model development [ Includes data, scale, and managing complexity].

And what was surprising to me is that they don’t really incorporate that many recent architectural or methodological innovations into this. Instead, they focus on just data scale and managing to improve the performance of this model and the flagship model, which I think is interesting.

And looking into one of these key levers in terms of data…this is really important for Llama 3.1, because a lot of the increased performance. And just the quality of these models is based on the data quality and how much time and effort they spend on the data.

So they pre train it on, I think, around 15.6 trillion multilingual tokens and spent a lot of effort on pre-processing, curation, quality assurance, filtering approaches for the pre-training and post training data.

And the source for this data became a lot more diverse, and it starts to include web data, code, repos, multilingual text, like we talked about and they put a heavy emphasis on just high quality tokens. And we’ll look over that in a bit as well. So essentially just the quantity, quality, diversity of this training data as well as the scale.

**Aman Khan: **Yeah. And they kind of list a couple of strategies they have there for how they gauge the quality of the token, which I found pretty interesting–the data printing techniques. So, you know how they classify. We’ll get into data prep, but the topics that they want to pick tokens from how they score tokens. I think here it’s like a lot of emphasis, a lot of effort on how do you pick high quality tokens to train on versus just scraping the internet training on everything.

### Scaling Laws in Llama 3 Paper

**Chris Park:** Yeah, exactly.

So, then, obviously, the second key lever they mentioned is scale, and they obviously have it with the model size with the 405 billion parameters–one of the largest AI models right now. And they utilize in terms of computational power 3.8 times the power 25, like flops, which is 50 times more than Llama 2, and that’s kind of insane because they said that they use 16,000 Nvidia 100 GPUs. And this is something I read in an article. Based on the cost of these chips. It means they spent northwards of 640 million dollars to train the new model. And I’ve seen higher estimates. And just in terms of training scale. They have 15.6 trillion tokens.

And this huge, like computational resources and model size. And they kind of just go into this and why they chose this kind of parameter size and and in terms of the pre training data or the training data this flagship model is approximately compute optimal. So that’s kind of just balance in terms of the size of the model and the computational expense to kind of offer good performance.

So just as a small aside, we can go into the scaling laws that they mentioned. So they have a bunch of these evaluations based on, you know, identify compute optimal models. And they see that as the more compute is used, performance of the model doesn’t really change with small adjustments in either model size or training tokens. And we see that looking at the compute power, the minimum kind of just like slopes out right? It kind of just flies a little bit. And according to this these evaluations. They chose the flagship model with 405 billion parameters, because it provides a good balance within their compute budget.

![Scaling Laws charts from the paper](https://arize.com/wp-content/uploads/2024/08/Slide-4-Scaling-Laws-1024x571.png)


And then extrapolating from this, with the computational power they had, they found that training a 402 billion parameter model would be, you know, optimal with 16.5 trillion tokens, which is kind of similar to what they have or close to what they have. So it’s approximately compute, optimal and they kind of emphasize the scaling laws a little bit in the paper, which I think is interesting, provides a good background into the choices that they made.

**Aman Khan:** Yeah, it’s kind of insane. I mean, when we were reading this like Chris and I were talking about it yesterday, I think that the key takeaway on this slide–well there’s kind of two. One is that it’s insanely predictable right now, that if you have, you know on one axis, your number of tokens, your training tokens and the other axis is the amount of compute in the form of FLOPs you want to throw at this model architecture, you will get a predictable loss. So you’ll actually get a predictable performance on the other end of it, which is kind of crazy because it’s actually a linear relationship still.

So that’s actually the second point, which is that we haven’t reached an inflection point or bend in that curve like scaling laws are still holding up. There’s a big question of like, how long can we keep throwing tokens and compute at models to have predictably better performance. I’m not sure about the specifics of some of the other close source models. I know we’ve read Anthropic. And then, you know, some of the other ones that have come out recently. But it’s really interesting to see that an open source model is kind of exposing: Here’s the number of tokens, here’s the number of FLOPs, here’s the scaling laws still holding up.

Especially since you’re getting comparable performance to a lot of the closed source players which we’ll talk about–so I found that to be really interesting, just how predictable this is from a compute standpoint.

**Chris Park: **Yeah. And I also like the like, you said, how transparent they’re being. And also like I like the fact that models are model development nowadays focus a lot on scaling laws instead of just throwing like parameters in there, right? Like, maybe with GPT-2 and GPT-3. So I think, yeah, this is pretty interesting.

**Aman Khan: **Yeah, if you wanna hit the next slide, we have a question from Harrison Chu, which is: does the paper talk about whether they will, they think, will be nearing a bottleneck in terms of compute or FLOPs, or available high quality tokens in the world to train on? So there’s actually two parts to that question. One is was there anything in the paper so far alluding to like where this will stop? What’s interesting is I linked this tweet here from Karpathy, who actually also has the same observation. In fact, if you scroll, if you, if you kind of read through this tweet.

The interesting line here is the model doesn’t seem to be converging in a standard sense. In other words, the LLMs we work with all the time are significantly under trained by a factor of maybe 100 or 1,000 x or more. Nowhere near the point of convergence. So what’s interesting is, as far as we know, there’s no allusion to this in the paper, and the speculation is that this will continue to keep scaling. Now the second part of that question was like, are we reaching a limit or nearing a limit of high quality tokens?

The researchers do talk about the quality of the tokens and the kind of approach to training, which we’ll get into. But the answer is there’s synthetic data generation and sort of like bottlenecks around really, high quality tokens and certain specific fields that you know, for general knowledge that you might want to train a model on. So that does come up a little bit of sparsity of data.

**Chris Park:** And on that same point I think there were some sensational headlines a couple of months ago about how AI model training. We’re running out of data to train models. I don’t know if you saw that, but I thought that was just an interesting viewpoint in terms of–are we really running out of data to train these models? I think this paper also utilizes a lot of synthetic data, which is also relatively new from what I understand.

**Aman Khan:** So, yeah, I think the last few major foundation models also allude to it. But like, even like 5 to some of the smaller models are like, we’ll just start using GPT models to create synthetic data. But yeah, it is a pretty new technique overall.

**Chris Park:** So then, yeah, I guess in terms of the third key lever, they also talk about managing complexity, and they very consciously opted for design choices to maximize the ability to scale the model right? So in terms of the architecture, like I said before, it was surprising that they didn’t really change up the architecture. From Llama or Llama 2 or enhance in a lot of different ways. So they just use a standard dense transform model architecture like decoder base, with just minor adaptations and instead of just also a mixture of experts model, which I think, has been a trend lately.

So, they just do this for better scalability and training efficiency, and then use a bunch of post training procedures as well that can be scaled without increasing too much complexity. So, like direct preference optimization and stuff like that.

And then we’ll go over the architecture like we talked about, standard dense transform architecture. But they do make some key enhancements like grouped query attention.

Just a little background– in a traditional attention mechanism, each token looks at every other token, but in terms of group credit, which is kind of an interpolation between multi-head and multiquery, they just group a bunch of queries together, pairing it with different, just a single like key value pairs. And that kind of increases the efficiency and decreases the memory requirements for right?

So they do that. They do attention masking, which just prevents self attention between different documents with the same sequence. So it kind of, you know, stabilizes or upholds the context of these different documents, and I think that makes it perform better in long context scenarios which you know you might need in the context window that they had for this right.

In terms of the token vocabulary, they also combine 100K tokens from the tokenizer with 28K additional token vocabulary from non-English, so, multilingual. So that’s pretty important for multilingual capabilities.

And then, in terms of positional embeddings. They use rotary positional embeddings. So in a standard positional embedding, you’re adding positional info into the model, which is important, because sequence or the position of words, and how they relate to that to each other provides really important information. But as you kind of scale up this in the standard positional embedding is usually linear, which might not work with the model that we have now, so they use rotary positional, which is like using rotational matrices and kind of just kind of try to go across that issue.

**Aman Khan: **So some serious optimizations here to take advantage of to really make the long context window usable. Like, you know, more efficient, and more usable.

**Chris Park:** So I thought that was pretty interesting. And then, yeah, like, going into pre training a lot of data collection. So they data source up until the end of 2023. Rigorous deduplication filtering to remove PII and low quality content. And then they also unlike previous Llama models, hey have a pretty good diversity of different data. So they have the general knowledge, but as well as kind of the math and reasoning code and multilingual. So that’s pretty important. That kind of enforces the capabilities of Llama 3.1.

And we’ll actually go into some of the techniques that they used or some of the interesting techniques they use for the pre-training. So they actually made their own custom parser, and tested that to improve HTML parsing for web data and preserve, like math, content and co-structures heuristic filtering and quality filtering. And the quality of filtering they used model based filtering actually using Llama 2 to select high quality tokens and then annealing, which is just the gradual reduction of the learning rate during the final stages and focusing on small amounts of high quality code. Near the end of the training process.

So very interesting stuff.

Personally, what I found interesting was that in heuristic filtering what they did was one of the steps they use is KL divergence to filter out documents containing tokens that you don’t usually see. I think that is interesting because I don’t know how that applies to data that’s highly technical or niche that might provide very high quality tokens. And whether or not. You’re filtering out that kind of data. Right? So that’s a question that I kind of want to explore a little bit more and see if there’s interest in that.

**Aman Khan: **The interesting takeaway here to somebody is if you connect it back to the results like it’s pretty clear that they’re optimizing for general knowledge as well. So they really want this thing to be a good general purpose. Model and you see that in the results of the model’s capabilities. So it kind of makes sense for them to want to do that. But yeah, interesting to see how that pans out for certain specific fields that may be having fewer tokens in. So the data balance has a huge impact on the performance.

**Chris Park: **Yeah, exactly. And although this, this, you know, these models are open source, they don’t actually release the training data that they used, which is unfortunate. So we don’t get a peek inside.

And then, in terms of the quality filtering I think they actually use FastText or RoBERTa. They kind of experiment with this stuff, and they enhance it, using Llama 2. So they use the previous version of this model to evaluate document quality, which I thought was pretty interesting.

### Llama 3 Pre-Training Benchmarks

**Aman Khan:** What’s being enhanced by Llama 2 in this part, I guess, like what does that mean?

**Chris Park:** Yea so FastText or I think RoBERTa, they just kind of enhance it with Llama 2. And classify which documents are quality and and they have, like a certain set of quality standards and see if it meets those standards.

**Aman Khan: **Gotcha, is it like another pass? Or it’s something like that where it’s like one or two. Yeah, okay, cool.

**Chris Park: **Yeah. And then we’ll just like shortly go into post training. They just do supervised fine tuning with human annotating synthetic data. Direct preference optimization, just to align it with human feedback and regularize it, and optimize outputs. And then I think, from my understanding, what’s unique about Llama is that they do a lot of post training. Don’t quote me on that. But I think that’s what Llama does a lot, and that’s how they kind of increase the quality of their models.

So that’s post training.

And then I guess we can kind of go into the results and some of the benchmarks they had. So these charts are some of the pre-training benchmarks.

![Pre-training benchmarks from the paper](https://arize.com/wp-content/uploads/2024/08/Slide-8-Pre-Training-Benchmarks-1024x572.png)


And I think what’s of note here is that we can compare Llama 2 and Llama 3 in the 8 billion, 70 billion token models. And we see just just in the general, like knowledge, sense like Llama 3 just completely outperforms Llama 2 in both categories, right? In math and reasoning there’s just a huge difference.

it’s kind of just huge, how different it is, right, how enhanced it is.

**Aman Khan:** And they reference Llama 3.1 as Llama 3 in the papers. So it’s like the family of models, I think they call it, so that’s something to keep in mind here. This is really this benchmark kind of shows compared to other smaller models. This is just the architecture that they’ve picked. Seems to work really well relative to some of the other ones. So this is kind of more of a comment on you know, general knowledge and certain tasks that they’ve optimized their model. For with the training data and compute that, combined with the architecture, comp you know, compared to like, mixture of experts. That’s kind of one of the takeaways here.

**Chris Park: **Yeah, pretty interesting stuff. I think a lot of the benchmarks that they use or the results that came out of this are pretty interesting.

Just looking at kind of the fine tune benchmarks, comparing a lot of our current 3.1 models to the leading models right now.

I think what’s of note here, and what they mentioned specifically in the paper is that in terms of the 8 billion, 70 billion categories, the smaller model categories. They are just completely outperformed and superior to all the models in that category. So we can see that, you know, in general code math, reasoning just outperforms a lot of these smaller models. Which makes sense based on how they train these right? And then, in comparing it to the leading close source models like GPT-4 or Claude 3.5 Sonnet, it’s pretty comparable, right? There’s high performance and multilingual and cogeneration, maybe reasoning, long context, handling.

So yeah, it’s an open source model, that’s you know, on par with these leading state of the art models.

**Aman Khan: **Yeah, it’s like some of the takeaways on this one for me was Llama 370 B–you’re getting some great bang for your buck there, relative to the other models out there like you’re just getting a better model across the board.

Llama 3 405 is comparable to the close source model. So you’re getting a really high performance model. Relative to a 3.5 Sonnet or 4.0, which is kind of nuts that you can just take the model, post it. And you’re getting basically something very close to what you would get from a close source model across these benchmarks, at least.

**Chris Park:** Exactly yeah. And for, like you know, individual developers, maybe like the 405 billion parameter models is not feasible. Maybe if it’s hosted somewhere else. But like, obviously, the 70 billion like that might be so useful for just research and continued development of AI, which I think you know is so interesting, and so, you know, helpful.

**Aman Khan:** Or token generation, right? I mean, you can imagine that more, you know, for future models, you know, have this open source model to be more token generation. You know imagine a Llama 4 trained on Llama 3 tokens. You’ll just get higher, even higher body output there.

**Chris Park: **Exactly. Yeah. So you know. Opportunities are endless with these fine tune models.

**Aman Khan: **Yeah. So I thought this one was interesting. I’ve started to see this come up a bit more in papers. There’s a good amount of optimization that you know the the foundation model providers are starting to and like, you know, really fun, your labs are starting to to kind of do around tool use or function calling really specifically. This part in the paper was actually around multi-step function calling. So that’s given a task the model needs to combine functions and perform a certain order of operations of those functions to solve a problem.

And I think what’s interesting here is that this has made its way into the paper, they’re starting to do some optimizations around this. There is a whole section on function calling and tool usage in the Llama paper as well. Just so is that that’s where you know that’s sort of generally where the space is headed. If you hit the next slide, actually.

So in terms of tool performance. There’s a certain series of benchmark data sets here. One of them is called Nexus it looks like. And you know, Nexus API Bank, a couple of these others where you have to combine. Okay, here’s an API that’s being exposed, how do I use that to answer a question?

The takeaway on this one is that Llama 3 8B and 70B perform other models in their category. So that’s 3 turbo and some of the other smaller models like Mistral. It does say the 4 8, 405 B model is behind Claude 3.5 Sonnet by only 0.6% which means that this is a really performer model for tool calling. This is really important for agent type use cases, if you wanted to interact with APIs and the multi-turn sort of tool calling is interesting, I think you know, probably a stat that if you’re building an agent you might want to keep a track on you know which models are sort of edging out over there.

**Chris Park: **Excited to see what people you know utilize or use. With this capability.

**Aman Khan:** Okay? And then when it comes to human evals. So this is an interesting one. So this is really a sort of almost a preference test of like, you know, which output does. You know, which output is scoring better or worse relative to so they compared it to GPT-4

So this is not so much a benchmark as much as it is like you know, based on some 1,000 number of rows. You know. How does Llama 3.1 compared to like a 400 for some almost like subjective quality of tasks a little bit here. So yeah this is, this is kind of interesting. In that, you know, generally this kind of just goes back to the point of this model is pretty comparable to like a 4.0 based on human evals.

So this is a pairwise evaluation based on human annotators picking one model’s response.

So it’s interesting. I think you’re gonna start seeing more of this type of eval is my takeaway on this slide. The reason for that is because there’s already stuff out there like discussion out there of like back to like the token token generation. Do we have enough tokens, benchmarks making their way into the training set. This is a way for you to make sure that when you’re you know your holdout on your Eval isn’t tainted by potentially the model just responding from memory, so it’s actually just a qualitative measure of performance.

So I thought this was interesting. I know that we might get into a little bit later on, like discussion in the space. But what do people see qualitatively in terms of this model? Do people prefer it versus others? At least, according to Meta’s benchmarking here, it seems to be, you know, pretty comparable to for up so. But yeah, very subjective measure. I think we’ll see more like this as well.

**Chris Park: **Yeah. And I think it’s kind of important to include these kind of measures, although they might not be as objective as quantitative because sometimes quantitative benchmarks don’t completely reflect how people use these models and their opinions on it. Right? On how well informed. So I think it’s just interesting how, in terms of code execution plus generation, it just really outperforms 4o, and a bit, but file upload just completely underperforms.

**Aman Khan: **Yeah, actually, the next slide kind of covers this as well. So this is actually a snippet from the paper, which basically should have underlined it on this. But if you just read a couple of sentences and you’ll see that they basically compare so that the previous plot was to 4o, but they do also talk about some qualitative measures around. I don’t think that I don’t remember if they posted the results of this, this part of the papers? I don’t think there was like a chart for it, but they do just kind of qualitatively measure like they actually don’t, as far as I know, link a figure for this. So take it with a grain of salt…but they do say that Llama 3 405B outperforms GPT-4 on multi term reasoning and coding tasks, but underperforms GPT-4 on multilingual prompts.

Llama 3, performs on par with GPT-4o on English prompts on par with click Claude 3.5 on multilingual and outperforms on single and multi-turn English, but trails in capabilities such as coding and reasoning. So I think it’s kind of interesting because you’re basically getting trade offs for each of them. But it’s very cool that they’re comparing to these larger models. I wish we had more data around this. It’s a you’re kind of just taking a qualitative like, oh, we’re very close but they didn’t post the results on that.

So yeah. This one stood out to me. It would be great to see more data around this. I wonder why they didn’t?

**Chris Park:** Yeah, I think that that is definitely interesting. And I guess the multilingual performance of Llama 3 is also interesting, and how it underperforms in certain aspects.

And I guess that might be because although there was kind of emphasis on multilingual token data, I’m guessing the data isn’t as diverse in terms of languages. It’s interesting how they only supported eight languages and how that choice came to be, compared to models like T5 or MT 5, even, the multilingual version and how huge the wide range of languages it supports and the multilingual data it’s supported. I’m curious what kind of data they used.

**Aman Khan: **The chart they actually used is not in the slide deck, but if you’re reading along in the paper on page 41, they do post the bar charts on each of those qualitative measures.

And they have sort of the error bounds. And they’re indicating that the model’s performances within error bounds, for most cases most tasks against the function model. But in some cases it’s clearly underperforming as well. And they don’t really tell you what the data set is. So you’re kind of taking their word on that one. But it’s interesting, at least like how close it is in terms of performance.

![Proficiency Exam Evaluations from Llama Paper](https://arize.com/wp-content/uploads/2024/08/Screenshot-2024-08-06-at-1.48.18 PM-1024x570.png)

**Chris Park: **Interesting stuff.

So I thought this was an interesting evaluation that they included. They do human-based proficiency exams and how well models do on them.

I thought something to point out was Llama 3. The flagship model, I think, does well, on tests that you wouldn’t think are standard for a large language model. So things like art history or environmental science or macroeconomics, psychology. But what we discussed yesterday Aman was that if you look at GRE physics and AP Physics and how different these models perform. We don’t know how that maybe puts into question the objectivity of this kind of evaluation, right?

**Aman Khan: **A little bit of a takeaway here is like, it does really seem like the data…. I mean, if you extrapolate out again, we’re not looking at the data. But if you were to maybe infer from here the mix of the data that you’re using to train the model does have a huge impact on specific tasks.

So it’s like, you know, you can be really good at AP Physics, but you didn’t train enough on GRE Physics, or you know. So if you’re using that as a benchmark, it’s just going to fall away. And it does make you wonder how linked some of these fields might be in terms of like semantic understanding. You know a lot of this might come down to knowledge, representation, and and like topic modeling. So it is interesting that like, if you’re just using out of the box exams, the results might be a little bit surprising.

**Chris Park:** Yeah, so I thought, that was an interesting evaluation they included.

And then, in terms of cogeneration, like, we talked about the smaller models kind of perform very well compared to their class.

But then, in terms of the flagship, the largest models, we see that Claude 3.5 and 4 0 kind of just outperform the 4 405 billion flagship model. But it doesn’t look too like too big of a difference. I think it’s pretty on par. But we know that Claude 3.5 Sonnet is pretty good at code generation.

So that was an interesting thing to see.

In terms of the benchmarks, it’s mainly Python, and then they included a bunch of other common, then programming languages.

**Aman Khan:** The takeaways from the Evals and Benchmarks section I think really, for us, was like, okay, they’re proving that this model is on par in many dimensions, with the larger models, and you’re and you’re getting an open source one. It’s like proving that point.

**Chris Park: **Exactly.

**Aman Khan: **Cool. So this is one that’s been getting pretty interesting. So you know again, I’d love to have seen more data around this, but there are more benchmarks emerging. They’re all really new benchmarks, if you look at when they’re referenced, we’ve done a bunch of studies against Kamradt’s new approach, and a few others there as well. The interesting note here on long context, this is like needle in a haystack for folks that might have seen some of our Twitter posts on that.

There’s sort of a need for this space to have better evals as well. Like you know, they claim that they’ve successfully retrieved 100 of needles at all document depths and context lengths. But what those needles are, what data those needles are. How out of place they seem, or how easy are they to pick up is an interesting note to just sort of keep in mind like it does feel like the space doesn’t have a ton of great benchmarks around it.

But it’s interesting, it’s another section than you know the model trainers can stick you know. Hey we do really good context retrieval based on the benchmarks out there. It’s just that, you know, as far as to be honest, I think a lot of those benchmarks are still pretty early.

And probably a space of further development for any retrieval tasks, your mileage may vary depending on what the task is.

**Chris Park: **Yeah. And I believe some of the current other closed source flagship models also in terms of needle in a haystack test, they also achieve 100%. I’m not completely sure about that.

**Aman Khan: **Might just indicate we need a better test, is kind of the takeaway on that to some degree.

**Chris Park: **Yeah, so with the long context window with them. I think that gives us at least some information on how effective the context retrieval is.

**Aman Khan: **It’s at least on par with the others in terms of the benchmark. But yeah, as you know, if you look into that. It’s like, are you combining a number? How out of places that needle it’s like, does it stand out in the context? Which is why it’s easy to pick up so there’s a lot of optimization we could do on that as well to make it more realistic in the real world.

**Chris Park:** Yeah. Still developing fields.

**Aman Khan:** 2023. It’s already feeling like old news now, sometimes.

**Chris Park: **Yeah, if you think about it really hasn’t been that long since the explosion of all these different models and AI.

**Aman Khan: **Yeah. I can drop a note on this one. So this one’s pretty interesting. This is a prompt injection test. So they set this under the safety section. I haven’t seen this in too many papers but I hope to see it more.

They do talk about safety a fair amount, and I think it’ll be in a future slide as well, but basically, the paper authors are kind of indicating well Llama 3 is on average, more susceptible to prompt injection than GPT-4 Turbo or Gemini pro.

So the prompt injection test here on the X axis is the category. The type of prompt injection test. And then on the Y is the model’s performance on it overall. Pretty good safety scores, I would say. But you know, you do still see GPT-4 and Gemini pro less susceptible to prompt injection relative to Llama 3 70 B. And 405 B. So I hope to see more tests like this as well. But again, it’s a pretty early area of like, how do you try to jailbreak each of these models?

So something to keep in mind, it’s great that they’re posting the results.

This doesn’t make them look amazing, quite frankly, relative to the other models. This is an area where it looks like they are lagging compared to the larger model providers. So if you’re deploying something into production, there’s something there’s something you might care about. So it’s great to see them releasing this data at least.

**Chris Park:** Yeah. And I think this has always been the case, for the Llama series of models is that they always lag behind in terms of safety and even just social biases compared to the leading models, and I think that because it’s an open source model, that’s just kind of the nature of what happens.

**Aman Khan: **I would hypothesize that if you have like a 4o, and if you’re Open AI, you’re getting feedback, you’re collecting feedback that you can fine tune the model on further and further as we get into. Actually, if you wanna hop to the next slide– multilingual. The interesting part of multilingual, and some of what their models capabilities are is they want to put this model in Whatsapp and other surface areas of Meta broadly. And so I think the goal there is really to start getting feedback and start getting the model more integrated into the app to really learn: Okay, you know, how do we fine tune for things like prompt injection? So that’s my hypothesis on that one at least.

**Chris Park: **Yeah, I wanna see how they improve with that for sure. And then I guess, in terms of multilingual languages, like we said, 8 languages, English, German, French, Italian, Portuguese, Hindi, Spanish, and Thai. So I guess all very high resource languages which makes sense.

And then evaluation wise they use the multilingual grade school math and the 0 scrolls benchmarks. So those assessing model ability to solve out problems in multiple languages or tasks and different long multilingual documents and generation related to that performance. Wise. It demonstrates competitive performance with the models like GPT-4 and can handle, you know, generating text and diverse languages with high accuracy. So we see again smaller models performing pretty well on par in terms of the large model.

I’m very glad that they included multilingual capabilities. I think that’s really important for AI. And then, you know, democratizing AI access, and this is actually something that I focus a little bit in in my studies and some of my research projects so it’s cool to see this happening.

**Aman Khan:** I’m sure you’ll pick it up when you get back to doing that. And you know, in your research as well.

**Chris Park: **Yeah. And then, just in terms of comparison, in the model arena. We see that Llama, the flagship model, is, you know, very high up there. So it’s tied with Gemini Advanced. And just a bit below just the leading flagship models right there. So that’s really cool for an open source model.

### Key Takeaways for Llama 3

![Text list of key takeaways for Llama 3](https://arize.com/wp-content/uploads/2024/08/Slide-11-Key-Takeaways-1024x573.png)


**Aman Khan:** Cool. So a little bit of like fine tune capabilities. We’ll drop a link on this, too, in the blog post, but [they actually trained a guardrail model as well](https://llama.meta.com/trust-and-safety/). So this is a small model you can use based on Llama 3 that you can use for guarding so for things like prompt injection, essentially classifying tasks for what might be potentially trying to generate tokens that you don’t want your model to create. So this will sit sort of in the request path and sort of you know, guard against that token generation or the inputs that might cause that token generation.

What’s cool about this is, it’s a fine tune model. We actually have our own you know, as part of this we’re doing. We’re releasing a lot of research coming out very soon in our Arize research teams, including a webinar later this month with the guardrails AI team where, you know, we’re fine-tuning models. And, you know, sharing some results around models for guardrails as well. So really cool to see Meta sort of starting to invest in this area as well.

We [have a webinar later this month](https://arize.com/resource/ai-with-assurance) where you can learn more about what we’re doing in the guardrails area as well.

**Chris Park: **So I guess in terms of open source the models are available under community license. But there, I think there is a limit in terms of the money that if you, if you’re trying to profit from these models, there’s a limit in terms of how you can use it. The weights are available online. I think the largest weight file is huge. I think from what I read, maybe like 100 gigs or more. But like we said, the training data is not being released right now.

**Aman Khan: **So you can’t go use the training set. I know we’re wrapping up on time. I feel like you know. Just we have one more takeaway. On a previous note, Zuck, you know that kind of put out there: Open source is the path forward, I think we can expect Llama models to continue to be open source as long as it makes sense to Meta as a strategy. But it is really cool to see that coming from a large, you know, they spent so much money training this model prepping data for it and releasing the weights and making the license open source. Pretty interesting.

I know we’re at time and we didn’t get to some sections like multimodal you know, or some of the impact and community. But I think. Takeaways here, Chris, do you wanna run out with any takeaways on this one.

**Chris Park: **Yeah. So I guess just very quickly. The takeaways, the big flagship model parameter size context window and the enhanced training data and scale. That was that kind of led to this flagship model as well as some of the multimodal capabilities that they’re planning on releasing. And the fact that this, you know, is all open source.

**Aman Khan:** Pretty amazing release for the team. Awesome. Well, appreciate you all joining. Feel free to keep dropping questions in our community. We’re happy to take more questions there. But yeah, thank you all for joining and looking forward to seeing you all at the next one.

**Chris Park: **Thank you, everyone!
