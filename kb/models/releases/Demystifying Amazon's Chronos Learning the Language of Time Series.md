---
title: 'Demystifying Amazon''s Chronos: Learning the Language of Time Series'
topic: models
subtopic: releases
secondary_topics:
- models/benchmarks
summary: Deep dive into Amazon Chronos for time-series modeling, including model behavior
  and evaluation context.
source: arize
url: https://arize.com/blog/demystifying-chronos-learning-the-language-of-time-series/
author: Sarah Welsh
published: '2024-04-04'
fetched: '2026-07-11T04:48:38Z'
classifier: codex
taxonomy_rev: 1
words: 7065
content_sha256: 6aacdf7c2e6f24aeb8e501c977b396771343935daf67cb4941e3fb6d41c14445
---

# Demystifying Amazon's Chronos: Learning the Language of Time Series

![Chronos - blog SallyAnn and Amber headshots](https://arize.com/wp-content/uploads/2024/04/Chronos-blog-1021x560.jpg)

              # Demystifying Amazon’s Chronos: Learning the Language of Time Series

## Introduction

This week, we’ve covering Amazon’s time series model: Chronos. Developing accurate machine-learning-based forecasting models has traditionally required substantial dataset-specific tuning and model customization. Chronos however, is built on a language model architecture and trained with billions of tokenized time series observations, enabling it to provide accurate zero-shot forecasts matching or exceeding purpose-built models.

We dive into time series forecasting 101, some recent research our team has done, and take a community pulse on what people think of Chronos.

## Watch

## Dive in

## Listen

## Analysis

### Introducing Chronos

**Amber Roberts:** I just posted on Linkedin, too, because I think before we did the last paper reading. We had the Deep Learning talk we did. So hopefully, people are kind of coming in now to see. So obviously, we don’t have time for a full walkthrough but hopefully, people are joining to kind of see how that’s done. I recognize some names actually, that

**SallyAnn DeLucia: **Yeah, that was such a great reading. And yeah, you’ll kind of get to see it in action. Today, we have a really interesting paper. Something that I’ve just been kind of keeping tabs on since LLMs came on the scene is, how does this work for Time Series. I’ve been kind of thinking through every use case. And one of the used cases that just hasn’t really clicked for me as Time Series. So I’m really excited to be reading this paper with you.

**Amber Roberts: **Same people joining might have noticed, like Sally Ann and I do a lot of these together. So put your questions. And if you have questions Sally Ann also works a lot with customers and their Time Series use cases. So if you have similar Time Series used cases. And you’re wondering how deep learning models or LLMs could fit into that, just let us know in the chat.

**SallyAnn DeLucia: **Absolutely I think we’ll get started. So welcome, everybody. Today we’ll be reading Amazon’s Chronos paper that they published about a month ago. Now. I’m SallyAnn,  I work on the product team here at Arize, and Amber–do you want to do a quick, quick intro.

**Amber Roberts: **Yeah. Hi, everyone. My name’s Amber. I’m an ML Growth lead here at Arize. You probably see me a lot on the community side. I do a lot of conferences, events and workshops. Also create a lot of content. So if there’s any content that you want to see in the generative AI space. You could just message me directly in our Arize community Slack. I’m always looking for new ideas or what people are interested in content-wise.


### Time Series 101

**SallyAnn DeLucia:** Amazing. Yeah, as Amber mentioned before, if you have any questions as we’re going along, feel free to drop in the chat or the Q&A we’ll we’ll be peeking at them as we go, and we’ll definitely try to reserve some time at the end for us to go through them. Before we get into our paper today, I did wanna do a little announcement about our in person conference. Observe, it’s happening July eleventh this year we’re going to be in San Francisco at Shack 15. Really super cool venue. We’re excited for that.

We do have a special promo for all the joining today. So you can use promo code Chronos to get 50% off the standard ticket. Sarah’s going to drop the link in the chat for you all to register. So come join us. It’s gonna be an awesome event.

![Time Series 101 overview slide](https://arize.com/wp-content/uploads/2024/04/Screenshot-2024-04-04-at-11.14.36 AM.png)


**SallyAnn DeLucia:** Cool. So for today’s agenda we’re gonna do a little Time Series 101 just really quick refresh of like what the current landscape of Time Series is. Then we’re gonna go through the Chronos framework. Amber’s done a really awesome test on Chronos. They share stats in the paper, but it’s always fun to kind of try it out for yourself. She also has a lot of different anecdotal research that she’s done to see what people are saying about it. So we’ll get into that, and then we’ll have an overview of our founder’s research–Aparna has done a lot of research on if LLMs can do Time Series. So we’ll walk through that at the end.

But at a high level. What we’re trying to do today is understand: does Chronos, or do LLMs have the capacity to be the gold star for Time Series models? Or will these traditional models continue?

So if anybody’s familiar with Greek mythology, this is what this is taking inspiration from that. So we’re excited to kind of walk through it today and see what we find now.

So Time Series 101. I thought it was important. Maybe people haven’t touched Time Series since school, or maybe they have been sticking with the same model for a long time. So I just wanted to kind of call out some of our classical models, deep learning models.

So for our classical models, these are usually called local models, since they independently fit. You know that unique model for every Time Series. We have ETS, ARIMA, Theta. These are kind of commonly used for testing techniques.

I’d say, ARIMA is probably the most popular. It’s a really reliable model that folks seem to love to use and as I note there are really effective for those series with clear trends and seasonality, which is going to be important when you’re dealing with this kind of wild Time Series data.

There are deep learning models that exist that are used. These are more like global models. Because they’re going to like, look at the multiple Time Series in the data set.

They’re going to capture those complex patterns and relationships. And they’re really powerful in those environments with really large data sets. So classical models analyze each Time Series independently, while deep learning is going to look at the whole data set. The output is very similar for both. So classical models will usually focus on predicting the precise value while deep learning is gonna provide that like density function of feature values.

So, just kind of a tldr; on Time Series, I think it sets the scene well, of what the benchmark is that we’re comparing against and with that let’s get into the Chronos.

Oh sorry forgot about this–LLM-based forecaster. So something that’s interesting is, I feel like this paper is getting a lot of attention, I’ve been seeing it a lot more than some of the other papers that come before it. So, in case you’re not aware–LLM-based forecasters is something that’s a really hot research topic right now.

There’s a lot of people in the Time Series community who have been kind of using the same model we’ve been using a remote for years. It’s reliable.

And as soon as LLMs came on the scene they’re like, what does this mean for Time Series? So some of the approaches we’ve seen before are pre-trained LLMs to forecast through prompting. So if you’ve ever heard of promptcast, it’s a way to prompt a pre-trained LLM to look at Time Series. We’re making the numerical data strictly textual, and passing it through the prompt.

But then there’s other series of research that focus on adapting LLMs to Time Series via fine tuning. So this is LLMTime, Time-LLM, Gpt-4 ts, and so these are basically the two main approaches we’ve seen so far.

The challenges with this is, it requires a lot of prompt engineering specifically for that first approach. You gotta get your prompt, really well positioned to be able to actually get accurate results here.

If you’re doing the second approach it’s gonna take a lot of fine tuning like each new forecasting task requires you to fine-tune the model. And that’s just kind of really expensive in a lot of different ways.

And then they’re resource intense. So they depend on large models which are gonna increase computational demands. And then it could have prolonged inference time. So these are kind of the growing interests, approaches, challenges.

And then I think the key thing to call out here is where Chronos is a little bit different than this is the fact that the Amazon Research group had the realization that LLMs and Time Series forecasting kind of share the similar goal, and it’s to decode sequential data patterns to forecast future events. So that is kind of the cornerstone of all of this research. And what inspired them. To kind of go and create this Chronos framework. Amber before we move on to the framework, anything you want to add?

**Amber Roberts: **Yeah, definitely, and I think with what a lot of people say in the Time Series community a lot of statisticians like you know, this tabular use case is kind of like the last frontier for deep learning and kind of the differences between looking at a purely statistical method, and like Time Series forecasting versus something that has content understanding to it.

So I think with what we’re seeing with large language models and especially like RAG use cases, is this ability to add context and then, you know, you’re making things like content specific. It’s like, okay, the LLMs actually understanding what you’re trying to get from it. It can provide explanations on it.

And so I think a big thing with Time Series–and SallyAnn and I will get more into this. But SallyAnn, from your perspective, the format versus content debate–where do you see LLM forecasters fitting into that?

**SallyAnn DeLucia: **Yeah, it’s tough. Because, like with normal Time Series models that, like the idea of adding context, be able to add that additional context. Maybe knowledge that you know about the data is not something you can do with ARIMA, right? So it could potentially be a really really powerful thing to have the edge over those traditional use cases.

That’s just not something that will ever work for that. So I think context could potentially be the real secret to all this, the secret sauce, if you will. I see a lot of potential with that, and I think that’s common. With a lot of LLM use cases–that ability to really frame the data in a way that gives the LLM more context is just really powerful.

Curious what you think, though.

**Amber Roberts: **Yeah, no, definitely. And I think maybe that could be on the horizon. It’d be amazing to have a Time Series model like, explain. Oh, we’re predicting a drop here. Because I don’t know. Maybe like weather patterns. That reoccur like every few years. I remember  Walmart labs coming in and  talking about how they sell out of strawberry pop tarts every time there’s a major storm in certain areas, and so that they need to kind of stock up on those.

And they wouldn’t even have realized like that was part of their model until someone very specifically looked at it. But if you ask an to explain like, you know, give me 5, you know, kind of interesting facts of things we have to stock up on that we don’t normally stock up on. I think that’d be really interesting.

We’ll get more to the result, SallyAnn cause I think right now, we’re not obviously there yet. We’re still trying to build forecasters to compete with things like Arima. But yeah, let’s show them how it works.

![Chronos framework: Time series tokenization, training, and inference chart](https://arize.com/wp-content/uploads/2024/04/Screenshot-2024-04-04-at-11.14.56 AM.png)

**SallyAnn DeLucia:** Alright. Let’s get into the framework a little bit. So this is a visual that’s right from the paper here. It gives a really high level overview of how all of this works.

So I think the idea that you know Time Series predicts sequential patterns. When I read that in the paper I was kind of like I had a Duh moment because I had been kind of playing around with this, you know, we’ve had some colleagues who have tested it, we tested it– the idea of like prompting an LLM for Time Series, and it just feels so weird to like, try to take Time Series data and like format text and send it to an L, and it just felt wrong, and I wasn’t ever surprised when it performed badly.

But when I saw Amazon’s approach I was like, Oh, that actually makes so much sense to take this approach. So what they do is essentially, we have our Time Series data. We’re gonna do mean scaling. Then they’re gonna quantize it and don’t worry. We’re gonna get into that in a little bit more detail. And so from this quantization, they can then get our context tokens.

So this is gonna be the actual tokens that will then pass for training so for training, they use Google’s T5, and then that’s going to get, you know, these predicted probabilities, and you know that next token ID, which is essentially that forecasted value. At inference, something very similar happens. We take that context token, except we’re gonna get, you know, the sample tokens.

And what’s interesting is you have to then de-quantize and unscale to get back to our forecasted value, because you remember in the beginning, that’s how we’re training. So you kinda have to reverse that to get back to your ultimate prediction.

So this is a high level. We’ll kind of break down these steps in the next few slides, but a really interesting approach, and we’ll kind of make it more.

The first thing you mentioned was scaling, different scaling approaches you can take. They use mean scaling here. So the data scaling really helps keep its shape, but it restricts it to a smaller set. If you think of LLMs that’s going to be important, less kind of range for the LLM. Have to kind of attend to so this is a really important step in it. So this is kind of a visual comparison. You can see this is just kind of some generated data. I did use GPT-4 to help me generate some data here to plot this out. A secret weapon. But yeah, you can see the number of purchases just as an example. Here, plot over time. Pretty high range–30 to 70. And now we’re kind of through these discrete values there.

![](https://arize.com/wp-content/uploads/2024/04/Screenshot-2024-04-04-at-11.15.13 AM.png)



From the scale Time Series data, so just that range is gonna decrease from like, you know 0 to 1.4 instead of like 30 to 70. So super important. Then the next step is we’re gonna take that skill data and we’re gonna quantize it. So there are, again, different kind of approaches you can take here. But what Chronos says is take the scale Time Series data–So that’s kind of what we’re visualizing up here–And then we’re gonna create a Time Series of fixed tokens. So they’re using percentile binning. So the tokens can really only go from 1 to 100.

And the really key point of both of these tasks is, it makes it easier to represent the values as a fixed set to the LLM, if we skipped all that, it would just be a lot less performant. So these are really important steps, and, as I mentioned before, they’ll kind of come back in the end to reverse this process that they did.

**Amber Roberts: **We have a brief question. I know you’re kind of in the middle of it. But so someone asked, like they understand tokenization of words for vocab can you elaborate a bit on the tokenization of Time Series? Maybe just a little example of–I don’t know if you’re given prices like how that just gets tokenized like through these steps.

**SallyAnn DeLucia: **You go to the paper. Maybe I think there’s a good example of it in here. Let me see if I can find it.

**Amber Roberts: **Yeah, no problem. While Sally Ann looks for that. Yeah, it’s, I feel like, you know, like the tokenization of words has become so logical to us. And the sequence is already understood. Because it’s whatever context that sequence is put in And yeah, looking at it. And this is also why LLMs traditionally aren’t very good for regression tasks because of how difficult it is to create like context or meaning behind just numeric values.

**SallyAnn DeLucia: **100%, I think what we’ll do is, I know there’s a visual on that paper somewhere that I’d love to show when you’re showing your research, I’m gonna find it. And then we’ll circle back to this question at the end.

Alright. So just kind of breaking down everything we did a little bit more.

So it enhances the traditional language model frameworks by kind of exploiting that sequential similarities between the language and Time Series models.

So these are the core components. We just talked about the scaling and quantization. But one thing that I thought was really interesting in this was the fact that Chronos doesn’t take any of the temporal data into consideration. I feel like that’s something that you know traditionally is super important for Time Series, but for Chronos, it ignores all those indicators. Amber. I’d love to kinda hear your thoughts on that, because I know you spent some time playing around with this.

Any ideas on the differences that that could cause between Chronos and your traditional Time Series models?

**Amber Roberts: **So I think this kind of goes to use case as well. Where I do think Chronos did a better job than some previous deep learning Time Series models where they’re only really benchmarking against other deep learning Time Series models. But if you have a use case where it’s like, I only care about a forecast that’s going to have like an hourly component or a daily component like, take Chick-Fil-A, for example, like they’re closed on Sundays, and so they don’t really need something that’s going to include Sundays in their prediction, because they’re not gonna have data for it.

Chronos is really good at predicting month over month like sales that could be good. But if I’m a machine learning engineer, and I don’t care about month to month like I need it on a much more granular scale, then I’m not going to use it. So, or if I care about seasonality, or if I don’t have trends like very use case specific here. And so it, you know, we might get what we might get like LLM leaderboards for Time Series LLM models.


### Training Chronos

**SallyAnn DeLucia:** Yeah, it’s a really interesting approach. I think they’ll get into that a little bit more later on, about what use cases and what the unknowns are for this model.

Okay, for training. I think I already mentioned this. They use Google T5, they do employ cross categorical. I’m sorry. Categorical cross entropy loss. So we’re really viewing forecasting as a classification problem to learn these distributions, which is again a very very interesting approach here. Kind of turns like everything.

If back in like undergrad and grad school, when we learned about Time Series, if we were told that it was going to be turned into a classification problem, my brain might have exploded.

So the world we live in now with these large language models, another really important call out for the training is that they actually enhance train diversity using TSMix and KernelSynth.

I think this is a really really important thing to call out, because we see in some of the research that you know our founders have done, and that other people have done of like, how important it is to kind of have diverse training sets and try your best to make sure that the training data sets are not the same as the benchmarking marking data sets, so that when you know they have those zero-shot forecasting for that new unknown data it can actually perform.

So it’s great to see, these techniques are really interesting. I definitely encourage you to maybe check out the paper and see exactly how they do that. TSM, explain scaled sequences from existing series. And then KernelSynth create synthetic series from Gaussian processes. So it’s really interesting to see how they employed those. And that’s how they got their training data set.

For the forecasting approach, the model sped sampled context tokens to generate a sequence of future tokens. That was that last image here. In that visual. We looked at before. And then these are de-quantized and unscaled to get the final prediction.

So they do all the scaling to kind of get the tokens into these like finite values. And then we kind of have to reverse that so that we can get back to the original data set that we’re looking at. So, really interesting approach there.

So that’s kind of the Chronos framework at a high level. I’ll pass it to you, Amber, and we can get into the research that you’ve done to get into understanding how it performs.

**Amber Roberts: **Yeah, we also have, like a few questions, so let’s maybe like, have a bit of a discussion here. And then SallyAnn, I’ll also have the paper up. So if you find that example we can show that example that someone asked about.

Someone also asked is Chronos good for intermediate Time Series?

Some of these questions, I’ll show how to play around with it.

I bet if you ask the Chronos team versus someone that like does intermediate Time Series, the answer may vary, I’m sure you could get it to work for it. I’m showing two different examples for just the granularity of the time that’s being looked on? Jazz asked: Would it work if you have missing slash nulls in the data sequence.

SallyAnn, did that come up at all for you, I know missing data and all like there are ways to get around it. Obviously, with traditional techniques and kind of smoothing or different like, Eda approaches but not sure if you if you came into contact with like nulls in the data sequence?

**SallyAnn DeLucia: **Yes, they did. They essentially had this like pad time, series of different lengths to kind of replace any missing values. And they also end of sequence tokens take, denote that end of the sequence. So I think those two techniques. That they mentioned the paper probably how they overcome nulls in the data there.

**Amber Roberts: **Awesome and then Farid pretty much asks something that we’re gonna talk about more. But this is absolutely correct. You know. So the training data is quantized, been forecast to become a classification which Sally Ann, like you mentioned that’s not definitely how we were taught serious analysis. But that can mean that you’re not gonna forecast novel values. And that’s very true. And it almost goes a little bit with ponds.

Another question–is it valid for multivariate Time Series, which you know it’s interesting because I think like what some discussions are saying is like, if you apply deep learning and apply this like LLM layer, it could be good for multimodal. So it’s going to be less good for traditional things like things that you really like doing with traditional statistical Time Series forecasting like, I don’t think these techniques should try to beat Time Series at its own game.

But in terms of research and in terms of just expanding capabilities–that’s really, that’s really what it’s about. So there are some big claims for these LLM Time Series methods.

But most of the time the claims fall short of traditional methods. But–and this is what we were discussing, SallyAnn, like there could be additional methods, and different things that you could get from using something like this versus traditional. It’s not gonna be less money, we can say, to use these methods.

**SallyAnn DeLucia:** It’s really interesting, I guess, just to kind of just clarify that last question we got of like, how does it become a classification problem. So you talk a bit about their objective function there. And how it really works is they’re essentially trying to minimize the cross entropy between those different distributions of the quantized ground truth in a sense. So it’s like performing regression like via classification, not like just a full classification problem. So I would say that that’s essentially what it is.

So they’re explicitly trying to recognize the cross entry between them. It’s not trying to see like this bin is closer to this bin. It’s just trying to kind of understand that distribution there. So hopefully that adds in a little bit more clarity to how it’s doing it by classification.

**Amber Roberts: **Yes, awesome. Yeah. I realize that was a question and not a comment, after you said that Sally Ann.

**Amber Roberts: **Awesome. So SallyAnn and just went through kind of the the tokenization the training a bit on like the inference, like the processes there, for how they’re tackling it. Again. This is kind of the next steps for these, like the language of Time Series, if you will.

And so what I did, and anyone could go to the Chronos forecasting GitHub. And the first thing I wanna do, which we talked about this and how to read AI research papers effectively, once you understand the paper, once you can compare the techniques, the audience is already asking really great relevant questions like for their own use cases and traditional use cases that they’ve seen.

The next step is to just start testing those, and if they don’t provide the ability to recreate their own experiments, I just don’t believe anything really that goes on in the paper. The paper put out by the team. The Amazon team did put out the model so you can run your own benchmarks. But anytime someone’s talking like up their own results, either reproduce them or wait and see if someone else in the field is going to produce them for you.

I am running, GPUs. I did try it on CPU it worked, and the first time, and then I ran out of space. So if you want to run this, I would recommend using a GPU for it. You don’t need the GPU for the ARIMA versions of this experiment. For Chronos they have these different models. Obviously they talk about the tiny one, which is 8 million parameters, and the large, which is 700 million parameters. It is pretty amazing that we do have models this large for Time Series, like 5 or 6 years ago, like I would not expect models this size for a Time Series. And it’s still being more and more effective, so it is really cool to see this research being done.

I used the small here–so 46 million parameters. And the example they had was how many passengers on the plane like over time. But this is just the example data set they created. And so this is passengers over a trend period. And you see, obviously a trend. You see the seasonality, you see, like an increase. And it’s saying, like, can Chronos, the small model, predict this next peak for it.

And so it does do a good job. Now, again. This is the example that Amazon put in the Github notebook. So first step is being able to recreate what Amazon showed. And so, okay, I could recreate that with what they’re showing, the next step is comparing it to a different data set.

A popular forecasting open source data set is the Walmart sales forecasting data set. There’s a lot of really good work done on this on Kaggle. I believe it was a Kaggle competition. I got this data from [this github notebook](https://github.com/liamarguedas/walmart-sales-forecast). This person really dives into it. This notebook is huge with workflows, machine learning workflows and kind of traditional data cleaning and Time Series techniques. So if you want to run that, you can. I just kind of ran the results for it.

But it’s not computationally dense like, you can run this notebook yourself.

So, looking at the Walmart data, essentially, we just care about the weekly sales forecast over time, which looks like this. So you do have some periods of negative sales not many. Walmart is making a lot of money. And this is like, I think, 2012 data.So like upwards here, for just the idea of the range. So let’s predict, you know the next. I think I have it as the prediction link of just 25.

If you want to expand it further than a prediction length of like 60 points, it’s going to break. So just note that so maybe predicting the next 25, 50 like that’s fine. And a good number of samples is like 10 to 30 samples here.

So I ran the forecast, and just to get an understanding of how much data compared to what’s being forecast. This is the forecast amount I’m going to zoom in. But just so you understand how much compute is going into predicting the next like 25 points here. It’s a lot of compute to get at this prediction. Now, this is over a long, a long period of time. This is each week over, I think a few years for the data here.

And so when we run Chronos like from like, this is the very end of our data. When we run, the Chronos predict, it actually looks pretty good. So when just looking at it anecdotally, it’s like, okay, so it actually does a decent prediction. Yeah, the prediction interval might be a little high. If this is, you know, essentially this is the money, the value for sales. So you know it’s definitely within those bounds. But it looks pretty good. But then we have to actually compare it to reality.

And so when we overlap the actual data, the difference here is like half the sales that were made in this time. So for the compute, for the process, it’s fine, but when we run the ARIMA notebook just to see how close this is. These are much higher numbers with, I mean, the actual versus ARIMA is pretty crazy. And if I smoothed this out to be kind of like the actual residuals it would be very, very close. So this is just kind of a little example, little toy example of, you know, just some real world data. And overall. Cronos would not win the Kaggle competition.

But the main thing to say, and yeah, like, SallyAnn if there’s anything we want to get into here, otherwise we could either go back to the paper or talk about some even talking about some of the discussions around Chronos. So there was another Github repo, which I did have time to run through. But I saw it posted. I believe this is Nixtla, is the company, and pretty much they found that, you know, Chronos is like 10% less accurate and 500 slower than training classical statistical models.

You could run these experiments yourself, they did provide the notebook–I haven’t been able to go through this, but a lot of people agree that it’s going to be a lot slower. Mostly, these models are about fast imprints. And then, the accuracy we kind of just saw like, yeah, that’s probably at least 10% less accurate.

### Community Pulse: Chronos

**SallyAnn DeLucia:** Actually, this reminds me, I have a slide of kind of community questions.  This is my new favorite segment.

If you were here for the [Claude 3 paper](https://arize.com/blog/anthropic-claude-3/), Aman and I started kind of pulling things from the community. And I’m really excited to have these, because I think it just gets a really good pulse.

So one thing I think this is kind of showing in the sentiments from the questions we’ve got here.

![Selection of community comments on chronos](https://arize.com/wp-content/uploads/2024/04/Screenshot-2024-04-04-at-11.27.46 AM.png)



This person says: am I missing something? We tokenize text because it isn’t numbers. Now we’re tokenizing numbers into less precise numbers, like what is going on with this? I thought that was a great call out, because at first it seems kind of counterintuitive to do this. So kind of countering my initial remark was, this makes perfect sense. So I thought that was interesting.

Oh, this one was really classic, I think. It said, because they thought that what they really should have said in this paper was, we used all of the techniques to see if Time Series forecasting was better so far, not really.

Yeah, this is the real one. I was looking for, so this person calls out the fact that, like you get comparable results. But like the resources that you have to use, trading in like the CPU based approach. For you know, Gpus and these massive models from a cost perspective just doesn’t seem realistic. And I think that’s kind of a point you were just getting at.

They’re just so large, and it takes so much. And it’s gonna have latency, and all this. So it doesn’t really feel like we’re quite there yet.

Something that I also thought was interesting was somebody called out the lack of interpretability. That’s something that always sticks with me, because right now we don’t have true explainability for these large language models. We really don’t know exactly how they’re coming to their conclusion. So when you have a lot of money on the line like you typically do with a forecasting use case, using a model that you can’t really interpret is something to me that definitely stands out.

This is also an interesting call out where I think it counters everything that you and I have been saying, which is for some people, though if you can pay a price to get better results, they’ll do it. So just just really interesting mixed results from the community. But I just wanted to call out that whole, the GPU comment. Since that was kind of your note, Amber.

**Amber Roberts: **Yeah, no, that’s exactly the four takeaways that I had written down. From people that’s, you know, less accurate, slower, less interpretable and more money like the interpretability is really a key area, because with stats, you know, you can essentially derive what? What’s going on from, what you’re seeing, and know how each thing is predicted and why it’s predicting that.

And I think you know, that’s where research could get really cool around language models, because, like the same way that you could ask a data scientist to say, what’s happening here, and they have to figure it out.

And it could do that when provided the data. So it’s not going to be interpretable from a statistics, perspective like, not from a derivation perspective. Where you can go in and figure out why this is happening, it is going to. It can be interpretable from an observability perspective, like where you can ask the model why it’s, you know, predicting an increase or why it’s not increasing or decreasing at all, because maybe it’s like, well, you know, if we just stay here, it’s a safe bet–and understand like, why, it’s actually making those predictions.

### Q&A: Chronos and Time Series Forecasting

**SallyAnn DeLucia: **Yeah, that’s a good call. I know we only have a few minutes left. We do have a few more questions. For the question about how we do time service tokenization, I couldn’t find the visual that I thought existed in the paper, I thought there was one but the scaling and the quantization that I was discussing in the beginning. That’s the Tldr; on how it’s done. So we’re taking those infinite values in through the scaling. And more importantly, through the quantization, that’s how we’re getting those fixed values of tokens.

So I typed that out there. But hopefully, that clears things up.

Let’s see, we have some in the Q&A.

How does Chronos compare with Google’s times FM?

That one I didn’t come across in my investigations. And while reading the paper, Amber did you happen to come across Google’s time?

**Amber Roberts:** I was looking at that one. I didn’t see any specific mention on that. We pretty much saw that Lag Llama was very poor performing, and GPT-4 TS performed pretty well.

This is coming out now like kind of these benchmarks against each other. And again use case specific. Someone asked about, is there a way to put in features to improve the Chronos prediction?

SallyAnn, you looked excited.

**SallyAnn DeLucia: **Well, I think that’s kind of the question that you and I were chatting in the beginning of, like the whole idea of adding context. And so I think they didn’t really explicitly say that there’s a way to add in features. But when I hear that I kind of think of adding more context to the prompt. So in theory, I think it’s totally doable. But love to kind of hear what your take on it is.

**Amber Roberts: **Yeah, yeah, it’s interesting, because the example they showed was just like a prediction of a number of passengers over time, which was a perfect Time Series sequence. And you know, it had pretty perfect components.

I couldn’t find where that came from. I don’t know if it was just generated, but that’s essentially an example, and it only had you know the one features.

So, would more features help? My guess would be yes, like. There’s so many Time Series examples of leveraging features, especially features that have that seasonality component which help with your predictions.

But yeah, like, I mean, this one was a zero-shot. That was kind of the whole point. It was zero-shot, so I would guess any additional thought methods would help, and any additional features or content would help with the prediction.

**SallyAnn DeLucia: **Yeah, it would be interesting with some of those prompt casts like, kind of comparing that and playing around with the prompt that’s used there and comparing it. I wonder if that could be a good test for us to see if that theory does edge out without using it.

I think the last question in the Q&A, at least, is what exactly gets assigned a token is it 1 point or a sequence of data points?

I think you’re referring to kind of like the initial context, token that gets passed on to the model. And that is going to be the whole sequence of data points. You can kind of think of it as when you know you’re proctoring chatGPT, tell me something, and then it’s going to kind of predict the next token based off of your initial question there.

We’re doing the same thing, except we’re taking Time Series as our prompt in a way, or our initial input. And then we’re predicting the next token, which is a data point from there. So that’s kind of how it works.

So we do the scaling to get our token, and then we’re predicting the next token that is then de quantized and unscaled to get that final value. So that’s a little bit more on that process.

**Amber Roberts: **And if you play around with the model yourself, you can select that prediction length like how long, essentially of a sequence you want predicted from your examples, and you could probably change that window size.

You could put in the number of examples. And you could put in the prediction length. And so you could chunk, essentially that data. I haven’t played around with that. But yeah, it would be interesting to see because it correctly predicted, like the next sequence, for the example they had with those passengers, like the number of passengers. But if it was only given half a sequence, or sorry half a period, would it be able to do that like if you stopped at the last amplitude, would it be able to do a full prediction which I really don’t know.

But that’s an interesting question, and that’s why I think there’s so much research around it as well overall.

SallyAnn, what are your takeaway thoughts from Chronos?

**SallyAnn DeLucia: **My final takeaway is really the fact that no, I don’t think Chronos is going to reign supreme right now, I think there’s a lot of work that needs to be done in this field to understand how we can more efficiently, really leverage LLMs. I think they’re just way too costly. The performance isn’t edging out something that’s kind of simple and straightforward that everybody’s been using for a really long time. So it’s exciting. It’s fun to see these new models and new applications come out. But it’s definitely not there yet, in my opinion.

**Amber Roberts: **Yeah, I agree. I’m glad we read the paper, I’m glad we experimented with it, I think it’s really cool seeing all this research being done by teams that can afford all the computation costs, and they’re putting out research on it.

So it’s really neat to see the claim of not sacrificing accuracy. I don’t believe that accuracy is sacrifice compared to traditional methods, and it really all depends, when you see these papers coming out, look at the benchmarks being used. Cause right now, it’s really cool research. I love seeing it. Do I recommend people change out their forecasting models with something like this? No. But if you have the compute you could play around and see.

**SallyAnn DeLucia: **Absolutely.  And I’m gonna post one more thread. Aparna, our founder, did more research on LLMs. And I think she has a Tldr there, that was like: don’t trust your stock prices with LLMs, so read that out if you want more context. But yeah, Amber, I think you summarized it perfectly.

**Amber Roberts:** Awesome. Thanks, SallyAnn, thanks everyone for joining. If you have additional questions you can ask them in the Arize community Slack.

**SallyAnn DeLucia: **Absolutely. Thanks everyone.
