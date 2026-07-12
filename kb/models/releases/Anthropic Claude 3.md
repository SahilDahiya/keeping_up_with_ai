---
title: Anthropic Claude 3
topic: models
subtopic: releases
secondary_topics:
- models/benchmarks
summary: Overview of Anthropic Claude 3 model releases and capabilities, including
  model comparisons and implications for LLM application builders.
source: arize
url: https://arize.com/blog/anthropic-claude-3/
author: Sarah Welsh
published: '2024-03-26'
fetched: '2026-07-11T04:48:36Z'
classifier: codex
taxonomy_rev: 1
words: 7518
content_sha256: 4eaa20371d30fc43137fa294639202453b2b0e7999bb29edce34c8222b610ae1
---

# Anthropic Claude 3

![Claude 3 Blog feature image SallyAnne Delucia and Aman Khan headshots](https://arize.com/wp-content/uploads/2024/03/Claude-3-blog-1021x560.jpg)

              # Anthropic Claude 3

## Introduction

In this week’s Arize Community Paper Reading we dive into the latest buzz in the AI world—the arrival of Claude 3. Claude 3 is the newest family of models in the LLM space, where Opus Claude 3—Anthropic’s “most intelligent” Claude model—challenges the likes of GPT-4.

According to Anthropic, the Claude 3 family of models “sets new industry benchmarks,” and includes “three state-of-the-art models in ascending order of capability: Claude 3 Haiku, Claude 3 Sonnet, and Claude 3 Opus.” Each of these models “allows users to select the optimal balance of intelligence, speed, and cost.” We explore Anthropic’s [recent paper](https://www-cdn.anthropic.com/de8ba9b01c9ab7cbabf5c33b80b7bbc618857627/Model_Card_Claude_3.pdf), and walk through Arize’s [latest research](https://twitter.com/aparnadhinak/status/1766161976529711298) comparing Claude 3 to GPT-4. This discussion is relevant to researchers, practitioners, or anyone who’s curious about the future of AI.

## Watch

## Dive in

## Listen

## Analysis

### Introducing Claude 3

**SallyAnn DeLucia: **Excited for this one. It’s always fun when we have a new model to talk about.

**Aman Khan:** I know it’s like another challenger has entered the arena, and you just have to figure out: what does this challenger look like? What does it actually do? I’m sure that’s probably what a lot of people are wondering as well.

**SallyAnn DeLucia:** I think so. For a while there right after the initial release of chatGPT there were new models coming out all the time, and it got really exhausting. And now we’re at a point where models are still coming out all the time, but only a few kind of make their way to the main stage.

**Aman Khan:** Well, this one should be interesting. This is definitely a main stage sort of boxing night.

Well, maybe while folks are just coming in we can just sort of tee up a little bit of you know what we’ll be covering today. So I’ll just introduce myself for folks in the room. My name is Aman. I’m one of the product managers here at Arize, working on our LLM product line. Joined by SallyAnn–if you want to give a quick intro as well.

**SallyAnn DeLucia: **Yeah, sure, I’m SallyAnn. I’m also on the product team here at Arize. I work more on our core product team. But yeah, my background is in data science and engineering. And I am super stoked to be talking about Claude 3 today.

**Aman Khan: **Yeah so I feel like you’re on so many of the paper reads, I’m sure that if you have a repeat audience here. There’s gonna be a lot of folks that recognize you there. But yeah, very, very excited to jump in. And for anyone who’s new you know. Feel free to drop any questions in the chat and the Q&A section.

We’ll be taking questions live if they’re kind of relevant to what we’ll be covering. I can’t promise that we’re gonna have a lot of very pointed answers, because a lot of the tech that we’re covering is pretty new, but we can definitely try to hypothesize and share our anecdotes.

So I do want to caveat that the space is moving so fast. We have not tried these models out for everything that they’re good for. But we can definitely share what we’ve learned so far.

Awesome. Cool with that, maybe I’ll hop in and just share my screen. And we can start covering what we’re what we’re planning to to kind of dive deeper, dive deeper on today. So today is a long-awaited Claude 3. So this is the latest challenger from Anthropic, so we’re gonna be covering what was in the press release, and the model card that was also in conjunction, released with the latest Claude models.

In the papers there’s a number of comparisons to Claude 2 so like, what are the performance improvements from? Just honestly, just even just a year ago from release from Anthropic. But then also looking to compare to competitors out there and then what we’ve seen so far in the last week. Since the release around capabilities, what’s new? What do these models seem to be good at? Anything more to add there, SallyAnn?

**SallyAnn DeLucia:** No, I think this covers it. We’ll do our best like you said it’s really hasn’t been around for too long. So we’re taking a lot from that model card paper. And what we’re seeing online being talked about and what we’re experimenting with and just sharing our hypotheses here.

**Aman Khan:** Awesome. Cool. So with that, I think we wanted to jump into what’s new.

So there’s three new models that we’re going to be taking a look at. They’re kind of cleverly named: Haiku, Sonnet, Opus.

And kind of similar to the recent Google release as well from Gemini, but kind of three models for three different use cases. So you have Haiku, which is efficient, smaller model meant for quicker inference, cheaper inference Sonnet, you can kind of compare it to like a GPT-4 turbo or like a 3.5 turbo just sort of like all round, but better performance than that now.

And then Opus, which is like your GPT-4 highest performance. You know, models that they’re offering come with longer context windows multimodal support, which is a new capability as well. in terms of, you know, in terms of the level of performance that you’re gonna get from multimodal and then improved multilingual capabilities, and then a ton more in terms of the latest evals that were dropped in terms of different tasks that these models are good at. So we’ll definitely be diving deeper into that.

With that I think maybe we can jump into just the press release super quick, and maybe cover that at a high level.

So kind of typical to you know. I guess what’s happening these days with these more close source model providers. We didn’t get a paper. So unfortunately, this paper read is doesn’t have a technical architecture we can cover. However, what we will be able to share is going to be more of like hands-on sort of practical what we’re seeing these models being used for, and how people are assessing them. But unfortunately, no architecture. We’re not gonna be able to break that down much more in terms of number of parameters, training data. You know the specifics there that we like to typically try and tear apart.

Kind of one takeaway is, at least for me. I don’t know, SallyAnn, and feel free to you know, kind of kind of jump in with any of and then any thoughts here. But I did want to tee up the benchmarks that are being used, we’re starting to see consolidate around a pretty common set.

I still have my questions around like how much these benchmarks are being used in the training data and what the crossover is. You know now that these are becoming pretty well known. Benchmarks that models are, you know, being released to kind of compare to. I don’t know if any thoughts on that like it’s starting to feel more and more like, who knows how much leakage there is in the training data these days, right?

![Claude models comparison chart](https://arize.com/wp-content/uploads/2024/03/Screenshot-2024-03-22-at-4.06.21 PM-1024x575.png)

**SallyAnn DeLucia:** Yeah, it is super tough to say. And like you mentioned, we didn’t really get an extensive paper. We got this. They called it a paper, but it was like this extensive model card, and they focused a little bit on the training part, and all they really said was, they deduped some information from the Internet. And they were kind of secret about what close source third party data they use. So I would totally like to see a little bit more transparency, especially from a company like Anthropic, where that’s kind of their thing to understand a little bit more what the overlap is. Because you’re right, it’s a little bit hard to trust that face value without knowing for sure whether it was included in that training set.

**Aman Khan: **Yeah we’ll dive into the model card, too, and just sort of break down what they have been able to share there. It seems like one of the things that’s kind of called out in the comparisons to cloud to, but also in general is performance improvements around latency. So you know, sonnet being too x faster than Claude to being near instantaneous in terms of input tokens being processed, you know, archive, etc.

You know, basically, the used cases that they’re trying to tee up this. This. These models are going to be super helpful, for you know, being able to actually, you know, be able to take a large amount of info tokens, process them and generate results, and quote unquote near real time.

They do also call out vision capabilities. So that’s a new bar as well, I like the comparisons to you know those same tasks compared to like your other sort of large multimodal models out there.

Interestingly, they do call out that Gemini Ultra is actually still the leader in many of these tasks.

I thought, that’s interesting. On the same benchmarks. they’re not gonna claim that they necessarily win on things like, you know, document, visual, Q&A. So it seems to be like Gemini 1.0 Ultra you know, that’s performing. Gemini model is definitely in the lead there. So that was pretty interesting as well.

And then I thought this was also an interesting sort of, you know, heading to put in the press release, which is fewer refusals. SallyAnn, do you wanna do you want maybe, to take this one on. I know we’ll cover it a little bit more in depth, in a little bit more depth in the model card.

**SallyAnn DeLucia: **Yeah. So here, what they’re specifically talking about is like when you ask Claude 3 a question, any of the versions of it. It’s less likely to refuse a prompt that’s kind of on the system guard rails. Or if it’s lacking context.

Something about Anthropic is that their mission is just to really bring a lot of transparency and guardrails and safety to the models that they build. So they take a lot of effort in implementing these guardrails, but with Claude 2, it was just refusing way too many things that it shouldn’t have things that weren’t within those kind of red zones if you will. So they made a really good attempt at fixing that. And the results definitely prove that they’ve improved it drastically.

I think you can see there that it’s like it went from refusing 25% of harmless prompts down to around 10 based on the model, the Haiku looks to be maybe it’s at 6% so it’s definitely interesting. It’s one of those problems where you don’t want over-correct. Right?

You want to make sure that these systems are built safely, that they’re not going to be targets of malicious intent. But you also wanna make sure users or whoever who’s using these models are not getting frustrated by the model, not answering. So it’s kind of this fine line, especially for them who? Really put it at the center of their mission here. So it’s quite interesting.

**Aman Khan:** I think we’ll get into an example, too. But it’s I like that. I think the note is like the nuance to the response as well, which is like being able to detect. Oh, is this actually it’s almost like a classification. Is this actually this question, this prompt, actually gonna violate my policies. It’s sort of like being asked a really hard question as a human being right like, oh, do, I would do. I want to comment on this touchy subject or topic? Or is the person actually, you know, asking for something? I can still give an answer, even if it’s not, you know exactly what the person is looking for. So it’s less refusal, it’s more giving an answer. But I  thought, that’s interesting, you know.

**SallyAnn DeLucia:** LLMs are now trying to grasp AI ethics, something that we’re all trying to do. It’s really interesting.

**Aman Khan:** We have a couple of questions already, so maybe we can tackle a couple of those before jumping into the model cards and the slides.

Someone asked: Another point of contention is whether they’re using the same prompt for each of these evaluations. Each model works best on a different kind of prompt.

Great comment actually, we’re actually going to be covering a little bit more about how Claude is a little bit different from a prompting standpoint. But Yup! Each model has completely different prompts teeing up how they respond, not just in the evals, but in some of the benchmarks that you’ll see as well.

Another question: And then they have hidden data sets for each test. Right? So it’s not self proclaimed benchmarks.

Yeah, I think that there, I mean, I think that the comment is just more on whether the data set is hidden is one aspect of it, but also just how much, how much of the data, you know from these data sets is now public domain that could be considered part of the training set. I think that’s more generally how we’re, you know, looking to sort of understand better ourselves. It’d be great if, like these data sets were, you know, a little bit more widely shared, or you know that explicitly pruned in some way. But there’s just no information around that.

**SallyAnn DeLucia: **Yeah, I think that’s a complaint, if you will. That we get a lot is like, how do we reproduce these benchmarks that are always being put forth in these papers. And I think that’s something that’s really tricky. And I think the community as a whole would love to see a little bit more transparency on.

**Aman Khan:** SallyAnn, where would you like to hop into our model card here.

**SallyAnn DeLucia: **Let’s take a look, maybe at some of more in more detail, those refusals, maybe because we were just chatting. Kind of about that. I think that’s an interesting topic. There’s some examples of the performance. We have these kind of standardized charts. You can see there. Something that I thought was really interesting about this model card is a lot of it is dedicated to what guardrails they’ve put up, what tests they’ve done for their red zoning, or something like that. So it’s very entropic in that way. Because they’re really those champions of of transparency.

Or we could do the vision. Maybe the vision would be good. Since that’s new for Claude too. Let’s take a look.

**Aman Khan:** Yeah, so they do image and video frame inputs. So kind of implying that like, you can, you know, send in multiple frames of a video and also get you know, certain certain outputs there.

**SallyAnn DeLucia: **Yeah, I think it’s interesting. There, I again  find it interesting, that gem and I still the leader there. I like that. They did indeed call it out. Sometimes I find that they like just to leave out those models that perform better. But it’s cool to see it kind of called out, and I think it gives them a benchmark to kind of work towards the next iterations.

**Aman Khan: **Kind of coming back to the prompting note the symbol indicates chain of thought prompting as well. So you can see that a number of the benchmarks here. That Claude is generating results for actually use chain of thought prompting as well, which is interesting because we we actually know that that cloud tends to perform better when you repeat information actually, that sent tends to be actually something that a number of these LLMs are, you know, call out as being a you know, whether it’s a bug or feature. The more you repeat the information, the stronger it seems to enforce that concept or idea in the context.

So chain of thought is like one mechanism to reiterate a point, and so interestingly that has made its way into the prompting technique for these benchmarks, too.

**SallyAnn DeLucia: **And I think that’s part of what they’re trying to hear. Cause they make a call out that they’ve made, like, you know significant progress in the vision and language understanding. So not only being able to actually just read the text from an image, like doing that kind of classic OCR type extraction, but actually understanding and having those like that complex visual reasoning, I think that chain of thought probably played a decent role on that.

**Aman Khan:** Yep. You know, an example would be being able to interpret this image data like a chart, and being able to extract the information from the chart, but then also be able to do math on top of it as an example.

**SallyAnn DeLucia:** For sure. It’s pretty interesting stuff.

**Aman Khan: **Okay, we’re at refusals. Do you wanna kind of cover this one? I know that this was something that yeah, you spent some good time digging in on.

### Guardrails, Evals, and Competitors

**SallyAnn DeLucia:** Yeah, I think it’s interesting. They even call it out in that first sentence of this is like that trade off between helpfulness and harmlessness. And so what they really do is just take a look at the I think they use the wild chat data set and they just are looking at these kind of user chat enter actions. I think there’s if you scroll down, not the next page, but this page after you can kind of see the comparison between what’s considered a benign response. And I think that kind of illustrates the point quite well, so you can see there. This is like, Help me draft an island for a science fiction novel explains a little bit of what it wants. It’s talk about social media as a surveillance system.

So, Claude 1 is saying like, Hey, I can’t really answer that, this is illegal, this is unethical surveillance activities, kind of missing the point that the user is not asking about it. In a realistic sense, it’s asking it so it can write a science fiction novel. So it’s kind of identifying that prompt incorrectly. And then you can see now with Claude Opus, it realizes this is kind of harmless. Yes, it mentions social media surveillance, maybe something in the real world context we wouldn’t want to speak on. But in this sense it’s harmless.

So I think it’s cool. I think that is definitely an important thing. I’m a big believer that we should have some decent guardrails to make sure that you know these models are not being abused as much as possible, spreading this information, things like that.

So I’m happy to see that they’ve released them a little bit, those refusals and making it more accurate, but also there’s still a lot of thought that’s being done on making sure that they’re still safe. So they’re really doing a great job of balancing it. Well, and it’s cool to see that now. Not only are they balancing it, but it’s got some really good performance to go along with it.

**Aman Khan: **Yeah, exactly. It’s like the new. The detection and nuance has definitely gone up as an example in the paper they cover incorrect refusals versus correct refusals. And so, Claude 3 performs better across the board on incorrect refusals. Interestingly, you know, Claude 2 seems to also be refusing to do you know, a relatively like it. It hardly really refuses Claude 2 that seems to be refusing more. So that’s an interesting benchmark to comparison.

But then, when you look at correct refusals, which are, you know, toxic requests in some way. And this data set that we, you know, wouldn’t be able to show examples up here. That is actually, you know where Claude 3 still holds the bar quite well. So yeah, exactly as you just noted, it didn’t regress on, you know, producing toxic results. It’s just that it’s more nuanced and the types of refusals it gives.

And then I think that there’s another you know, and they know that you know the way that they measure. This is employing another model to grade responses. So they’re actually using Eval here LLM Evals, you know, aLLM, as a grader. Did the model refuse correctly or not, basically as another way to look at it.

And then, you know, and then using string matching to identify. If this was actually, you know, should have been a refusal or not. So yeah, interesting to see. You know the role of human creators, is there? But more and more we’re seeing LLMs performing the job of what would maybe be a human greater before. You know, even just a year ago.

So I thought that was one major point. Do you have higher levels of quote, unquote intelligence for the vast majority of workloads.

This was an interesting slide. Do you want to take this one on one SallyAnn and then we’ll kind of tee it up with the pricing slide?


![Pricing chart for Claude 3 and competitors](https://arize.com/wp-content/uploads/2024/03/Screenshot-2024-03-22-at-4.11.27 PM-1024x574.png)

**SallyAnn DeLucia: **Whenever we do these kind of, you know, paper readings. When a new model comes out, I always kinda think you all are probably wondering: why should I care?

This is actually a chart from anthropic’s docs. And I thought it just did a really good job of understanding why 3 is important. Why you should care about it compared to Claude 2?

So the top is just kind of the descriptions that we’ve already given you. Well rounded, fastest, cheapest kind of highest performing the different strengths there.

But I think, the lower half is actually what’s really interesting.

So I think first off the multilingual Claude 2.1 and 2 had this capability. But you can see in the model card that performance is much better in Claude to 3. Vision is obviously new, we didn’t have that in Claude 2. So that’s gonna be a new capability. And as you mentioned in that previous portion, the capabilities are better. It’s not only just reading text off of an image, it’s really having that critical thinking around the image.

API formats are a little bit different. There’s some better latency, as Aman pointed out. Context window here from Claude 2 it’s bigger, but it’s just the same as 2.1 here. Same with kind of max output. They’re the same there. Cost, I’m sure, is something that’s important to anybody who’s going to use it here? So this just outlines the cost compared to the Claude models. As well as the training cut off.

And if you want to go to the next slide, which I think is also probably very important to people, is, where does Claude hold up against its competitors? So it’s a little expensive, it maybe is not that much different than say, like a GPT 4. But like looking at, maybe like Gemini or a Mixtral, it’s definitely a little bit more pricey.

These are the input or output prices per 1 million token Gemini’s pricing, I will know, is a little bit different than the rest of the providers on how they price. So you might see some kind of different pricing depending on what you’re looking to do with Gemini. And another interesting thing, I think, is the context window. So Claude 3 has a lot higher of a context window. I have my thoughts on really long context windows. I’m not super convinced that this is the solution. I’d love to kind of hear your thoughts on that.

But it’s interesting to see that we have like we hear that Gemini, you know, to or whatever it is. 1.2 is gonna have like a million token context window. So you definitely see that there’s these model providers that are pushing this larger context window to try to get more information in maybe rags dead like here all this stuff. But I’m interested to see if that’s actually the future because we’ve seen some, you know, conflicting research on that, whether they can really attend to all that context.

**Aman Khan:**  I think the cost note. So well, actually, the cost note is an interesting one. I think in doing this research we were kind of surprised, like Mixtral is super low cost as well. Gemini, you know, Gemini pro etc. There’s definitely a lot of optimization to do I think, on the cost side to make these models more affordable for a variety of tasks, but still, for a million tokens. It’s actually, I mean, that’s a lot of tokens, and I think that 200K context window, 200K token context window.

I think that there is a yeah. So this is the recall accuracy over context length.

We’ll dive a little bit more into some eval’s around context limits and context windows. But the tldr is that you know, context windows increasing means that the models can, you know,you can basically you can stuff more data into the context, which means that your retrieval of data from a vector, database starts to become… It’s still important to evaluate what exactly you’re retrieving, how it’s being stuffed into the context. But it’s a lot more forgiving. Now, if your context window is larger.

The thing is, though, the way that, like context, windows are being assessed, and these kind of like needle in a haystack types of tests which are, you know, stuff some data, some part into the context and retrieve that data. So you know, it might be like a key value pair or some other type of data. It. It’s, I think a big question is like, how representative are those tests on large context windows, in the first place, and should you actually be trying to evaluate the model’s reasoning capability instead of it’s just like pure retrieving a key value from, you know. And just like returning that value from a context window.

So I think it’s a pretty hotly debated area of. Okay. Even if the context window is increasing, are we evaluating those larger context windows the right way compared to just a better retrieval system in the first place, so that’s definitely an area that is open in terms of, you know, research and as you could see, it’s making its way into like the mainstream in terms of the model card, and Claude, and and even Gemini, 1.5 Pro–the 1.5 million token contacts window model from Google–you know Jeff Dean retweeting that information. I mean, I think that really goes to show that those investments and context lengths, they’re really starting to break into the mainstream.

**SallyAnn DeLucia:** For sure. It’s an interesting call out about the eval side of it.

**Needle in a Haystack Test**

**Aman Khan:** Yeah, especially on the  recall is interesting. But how much is you know, how much are we actually pushing  the capabilities of those context limits. In terms of you know what we’re actually evaluating them with, that might be a good transition over into you know, into how we’re evaluating you know, evaluating retrieval in the first place.

So this is actually some research that we’ve shared out on from the Arize AI research team here.

We actually did a similar test to what you’re seeing in the needle in a haystack. But we made it a little bit harder.

So this is what we’re calling retrieval with generation. It’s not a normal haystack retrieval test. And, by the way, you can always follow our research on Twitter, using Aparna’s twitter handle here.

This is an aggressive variation of haystack that is retrieving two random numbers rounding those numbers. So it’s doing a little bit of, you know, a little bit of intelligence, a little bit of math there, what number should I round to? Formatting it and then calculating a percentage growth. So it’s actually a practical task on top of retrieval. It’s not just, you know. Oh, let’s look at the recall. Or let’s look at how well the model is retrieving data from its context window. It’s how well is it actually using the data from its context window.

For what it’s worth Opus Claude 3 actually performs really quite well at that task. Even compared to Claude 2, which was, when we, you know, kind of put out a result initially with the needle in a haystack with Claude 2.1 that you know kind of showed that you have to prompt it differently and all these other things. Now you’re actually seeing that, you know, with the right prompt. That it’s actually, you know, performing at GPT-4 levels of performance there.

And we basically scored that up against, other types of eval tasks as well. So I think this one, the one that’s kind of called out here, date mapping in addition. That’s another type of like, do more, you know, do perform a task. In this case, it’s retrieving data and doing more sort of, you know. Calculations on top of that in the context window. GPT-4. Still, you know, wins at that task. But I mean honestly the result, looking at Claude 3. It’s night and day compared to cloud, 2 by one. So clearly there’s been a ton of investment in making the longer context windows more useful.

But what’s interesting is one, I mean, you know. And these tests are always. They’re always so interesting because they depend on things like how we prompt or the, you know, like the apples to apples comparison can be tough in some cases as well, but a normal haystack retrieval test.

It does look like Claude 3, didn’t you know, didn’t necessarily perform better than GPT-4 on that so for what it’s worth, It is interesting to see that there’s still variance in those tasks depending on you know, what the task is. If it’s just vanilla kind of retrieve information, or if it’s performing you know calculations on top of it.

Coming back to the importance of Evals, I think, in general. So whether or not you’re using a haystack test to determine. Okay, is this model going to be good at just stuffing the whole, you know an sec filing in and performing a calculation. You probably still want an Eval on top of that to make sure that whatever is being generated, you’re checking it by another model.

We did also see massive improvements in Claude 3 as a judge. There was a question on which model is being used to judge the toxicity of the results of the correct refusals. And I mean, it’s very. It’s very possible that that ends up being Claude 3. Claude 3 does quite well at that.

So maybe a real challenger there, in terms of LLM Evals and a new judge, that we might be leveraging more.

**SallyAnn DeLucia: **Yeah, it’s interesting. I feel like it’s been so long since we’ve really seen anybody be able to kind of hold up against GPT-4. So it’s an exciting time. And I think you know the last part of this thread here. Where they talk about the prompting…there’s a lot of research as a pronoun points out here on like the prompting approaches. You mentioned it like the optimization around that. I think it’s gonna be really key and I’m interested to see, like as we, we focus on that a little bit more. And we maybe, just take time to work with call 3 like it’s new. We’ve been. Everyone’s been experimenting with GPT-4 quite some time, and I’ll be interested to see as we do the same with Claude 3 what results we get from that.

**Aman Khan: **Yeah, I mean just to kind of reiterate as well. Reiteration sort of seems to be the trick here a little bit even more than perhaps chain of thought. That we’re finding that just repeating the instruction in the prompt. This is actually a good note. Maybe we should put some of those prompts up just to see, just to show how we’re, you know, repeating the prompt here. But you know, literally repeating the instruction generates much stronger results.

**SallyAnn DeLucia: **I was just gonna ask you,  I don’t know of an exhaustive list. I kind of know there’s blogs and twitter threads and and reddit threads on like general guidelines. But I don’t know if you might know better.

**Aman Khan: **Yeah, no, I mean for different models, I think. Like I mean, I saw a bunch coming out this week. We’ll cover a couple in the last sort of slides here of prompting techniques for Claude 3. I can’t say I’ve seen a conclusive database of different types of prompting techniques per model, per task. But that seems like an area that probably someone should go and tackle you know, being able to to capture all of that.

**SallyAnn DeLucia: **Sure.

### Claude 3 Hot Takes and Q&A

**Aman Khan: **So there’s another question: I’d be curious to see what really long prompts or contexts whether Claude 3 can outperform GPT-4, not forgetting as much of the prompt.

Yeah, I mean, that’s kind of a little bit of what we’re testing here. It’s a little adjacent, but where we’re where we often have to reiterate the prompt to get, you know, strong responses. But it’s hard to say how often you have to reiterate the prompt for GPT 4 versus Claude 3.

And in general it sort of comes back to like the prompting technique. How much of your contact center do you want to give up to the same prompt of it to the same instruction. To get a reliable result. So it turns out, just repeating the instructions does a really good job of giving you better results. And so maybe that’s just one of the features of these LLMs.

But great question there, and something I’m curious to see, too. That’s probably a great eval as well, just to see how much do you need to reiterate results?

**SallyAnn DeLucia: **Maybe that’s our next research topic.

**Aman Khan:** Yeah, might be, that’s a good point.

Awesome. Yeah. So alright. So let’s get into, I think, like, maybe the last 10 min here. I think it’ll be fun. This one’s gonna be fun. So, we talked a little bit about theory, a little bit about Eval, the training data, the benchmarks.

Let’s get into some hot takes. So SallyAnn do you want to kind of take this one?

I remember when we were prepping for this, I sent a Hacker News thread. I’m like, well, Claude seems to be doing really well. You sent over this Reddit thread. That is sort of like I guess, actually let me let me tee up the Hacker News one, and then we can jump over.

So Hacker News. There was a post that went out two days ago. If you use GPT-4 Turbo and Claude, which one do you prefer?

A lot of people were saying Claude, for you know the writing style. It’s almost like a breath of fresh air in terms of it doesn’t seem AI generated. Maybe because people are getting used to GPT’s writing style, or the style of its writing generation, Claude, for coding people moving over to Claude, like, you know, finding it to me much better.

And then you kind of shot over this Reddit thread that you found you wanna take on this one.

**SallyAnn DeLucia: **Yeah, it was just really interesting. I think it’s just the Anthropic message board or the LLM dev message or one of the two and I saw this, thread on Claude 2, and of course, as we’re prepping, I’m like, let me take a look at this, and one of the top threads over the last 2 days. Like, how do I get back to Claude? Claude 3 is horrible. It sounds like chatGPT, I used to like Claude 2 because it didn’t and I think one of the actually the first. I don’t have it here, but I think one of the first responses is like, Oh, that’s weird, like, there’s a lot of people saying other things. But then there’s a massive list of people saying it used to be one request or two to get it to where I wanted it to be, with a meaningful reply. And now I’m running out of messages that I can send with my free account to get Claude 3 to respond.

So it’s just really interesting to see kind of this polarizing view in the community. Some people are all for Claude 3. They think it’s much better than GPT-4. But then we’ve got some other folks that are just saying they hate it, essentially. They want Claude 2 back. So it’s interesting to see. I think this is maybe a symptom of it being so new. People are still getting used to it, you know. I think we’ll see this kind of back and forth. I think we see it almost with every new model that we get. There’s a lot of hype around it. And then maybe people play around with it, and they’re like, maybe it’s not as great, and vice versa.

**Aman Khan: **Yeah, there’s two kind of meta ideas that kind of come to mind here when I see this type of debate. One is that it feels a lot like when a new piece of tech like you just called out SallyAnn, and a new piece of tech is released.

For instance, when Facebook–I’m dating myself here–but when Facebook would like redesign their news feed. And they took away the wall. And people freaked out about that. They’re like, Oh, my God! I’m never gonna use this product again, or like apple takes away like touch ID, it’s like people get used to something, and they’re kind of used to the writing style of these models in some way, and when it’s new or when it’s different it can kind of freak people out, because it’s it’s less consistent. I think that there’s a certain degree of you get used to something, and then this is different. So I wonder how much of that is just human behavior being reflected here.

And then the other part is, you know, even if the model is better. Are we prompting it the right way right? And like getting results the way that we would expect. So it is really interesting to see such a polarizing response to this tech.

But I wonder if it’s actually the humans that are, you know, looking at the data and we’re scratching our head and wondering: is it better or worse? Versus like, are we even utilizing this newer tech the right way?

So yeah, I thought that was kind of interesting when I saw the debates here.

Yeah, so maybe the jury is still out, you know, it’s contentious. The Internet hasn’t really voted you know. But at the same time like it does look that anecdotally for writing or for coding tasks. People are a little bit split.

I did want to also call out a couple of interesting notes here on how would I use it. Anecdotally I can say I’m starting to try to use it more for coding tasks. If you look at the loss for Haiku on code. It looks like Anthropic is really investing more and leaning into code and that they call this out. This is also in the press release and and you know, in terms of like you know, what I think is that a press release of the model card? But coding is like a core capability here and and there’s some pretty interesting Twitter threads that we saw around this. So one is by person, Alex Burt. They actually call out that you can prompt Claude to essentially create its own sub agents to build apps, which is kind of interesting. I think a lot of people saw the Devin example from earlier in the week.

But this is one where Claude actually creates a set of instructions that gets sent to Haiku, shards them out as sub agents to actually you know, those tasks are then used as prompts for a sub call for a Haiku, which is a cheaper model. So you actually end up getting back a large amount of code that sort of works together to solve a task. I thought that was really interesting. It’s almost orchestrating agents within the LLM call itself. I hadn’t seen that before, and that this was a pretty interesting new kind of technique. So using Claude to actually create sub agents to perform things like coding tasks, was kind of interesting as well.

I’ll let this demo sort of round. It’s round its way out here.

You can kind of see the amount of text that’s generated really leveraging that longer context window.

Pretty interesting to see it kind of work here in the end. At the same time, like, you know, I think it’s all I I have seen some examples of these coding blocks that are generated, that you do still have to tweak aspects of it to get it to work. So here’s another one, which is again, a lot of the code. Examples seem to be like end or visualization, javascript code. This one is another one. I asked Pop 3 to generate an animation from our Rahul for the Pov of a neuron in a large neural net. It gave me this.

So it actually seems to be a pretty cool javascript animation, that, you know. Kind of looks really interesting. It looks really cool like it’s I remember using, like GPT for animations. And this this just seems to be way more visual, very interesting. It’s almost like taking liberty, artistic liberty there. But tagline is the code. Just need a couple of minor tweaks. So you do still need a human in a loop there to modify the code a little bit. Didn’t seem to work out of the box.

But you know it is interesting that it’s like, you know, the way that it’s showing how it works seems to take a lot more almost artistic liberty in the types of visualizations which is pretty cool to see.

**SallyAnn DeLucia:** For sure it is really interesting. I totally agree with that. That artistic liberty was not there. So it’s cool to see it with Claude 3 improving. And there are some really cool visuals I’ve seen come out of it.

**Aman Khan: **You know, one note is, you know, feel free to share your own thoughts as well on this. I think we’re always looking for folks to share ideas around, maybe different types of prompting techniques. In general, we’ll be trying it out more as well for coding tasks.

But we’d love to see we’d love to get input from folks who are trying it out for evals, prompting it for different tasks, maybe coding as well, or writing and just dropping their thoughts as well in our community can take the discussion from there. But yeah, I appreciate everyone for asking sort of questions and engaging in this. And yeah, thanks for thanks for dropping in. Feel free to keep the conversation going in Slack. And yeah, I would love to kind of, you know. Kind of kind of keep sharing ideas there as well as we get a little bit deeper on evaluating Claude for ourselves.

**SallyAnn DeLucia:** For sure I did see one question that we might have missed while we were answering. It was about niche kind of languages and making sure that they’re accurate and culturally sensitive for communication.

That’s something that they do call out that, you know, for they call them like low-resource languages. So I think anything that is really nuanced with language is something that’s going to be really difficult for these large language models you can have, you know, Italian, Spanish, many languages that have a lot of dialects going on. So mastering that nuance, I think, is going to be a challenge. And I think that’s just another place where you kind of need that human in the loop to make sure that you’re kind of respecting and being accurate for all those so sorry for missing that one earlier.

**Aman Khan: **Yeah, thank you for. Thank you for calling that out. And exactly, you need more data. You need more humans to kind of generate that data for these models to perform well on it.

Cool, awesome. Thank you everyone.
