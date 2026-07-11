---
title: 'Breaking Down EvalGen: Who Validates the Validators?'
topic: evals-observability
subtopic: evaluation
secondary_topics: []
summary: Deep dive on EvalGen and the problem of validating LLM-generated evaluators,
  including human review limitations and evaluator reliability.
source: arize
url: https://arize.com/blog/breaking-down-evalgen-who-validates-the-validators/
author: Sarah Welsh
published: '2024-05-13'
fetched: '2026-07-11T04:48:44Z'
classifier: codex
taxonomy_rev: 1
words: 7548
content_sha256: 3647787e3bd2187755c156e597c576ffccc8a8f0c0833ff54868c8249521a3d8
---

# Breaking Down EvalGen: Who Validates the Validators?

## Introduction

Due to the cumbersome nature of human evaluation and limitations of code-based evaluation, Large Language Models (LLMs) are increasingly being used to assist humans in evaluating LLM outputs. Yet LLM-generated evaluators often inherit the problems of the LLMs they evaluate, requiring further human validation.

This week’s paper explores EvalGen, a mixed-initative approach to aligning LLM-generated evaluation functions with human preferences. EvalGen assists users in developing both criteria acceptable LLM outputs and developing functions to check these standards, ensuring evaluations reflect the users’ own grading standards.

## Watch

## Dive in

## Listen

## Analysis

### Introducing Who Validates the Validators: EvalGen Challenges and Goals


**Aparna Dhinakaran: **We’ll give people a couple of minutes to join, but I feel like we have a really good paper today.

**SallyAnn DeLucia: **Yeah, that’s something that I think is super relevant to us, something that we think about a lot so it’s cool to see what this group has put forward, and I’m excited to talk about it.

**Aparna Dhinakaran: ** Yeah, I feel like this is one of those papers where you get like all of the research side and the evaluation side. And it’s gonna be a really good discussion.

**SallyAnn DeLucia: **Yeah, I guess we could get started and give introductions.

Thanks for joining. I’m SallyAnn and I work on the product team alongside Aparna. You wanna give a little intro?

**Aparna Dhinakaran:** My name is Aparna. One of the founders here at Arize and I work on the product side as well. So this is a timely topic, because me and SallyAnn think about evaluations all the time. So let’s jump in.

**SallyAnn DeLucia:** Let’s do it. Yeah. So for these paper, we’re reading a paper called Who Validates the Validators. It’s basically a paper that puts forth a framework to align evaluate like LLM-assisted eval with user criteria. So let’s get into it a little bit.

Oh, before we do something very important. We are hosting an event [July 11th in person, in San Francisco](https://arize.com/observe-2024/). It’s going to be a really awesome event. We have some really great speakers–more information will be coming. But definitely grab tickets.

**Aparna Dhinakaran: **It’s going to be awesome.

We have an amazing lineup of speakers joining us. Folks from Mistral, we have researchers, developers, open source community, so check it out.

**SallyAnn DeLucia: **So, in this paper the team puts forward this open source tool called EvalGen, and they do this with a few different motivations. So, thinking about current Eval frameworks, we know that LLM-assisted evals are kind of required.

These automated patterns are required to actually get performance on your LLM application.

Just because of the sheer volume of queries that exist, the time it takes to kind of read through all of them, and manually just takes a lot of time. So it really requires that we use these LLM judges.

But something that this team calls out is that there can be a lack of transparency or assistance and actually aligning your goals with these evals. So that’s really the main piece that they aim to fix with their eval framework.


![Goals of EvalGen overview](https://arize.com/wp-content/uploads/2024/05/Image-1-1024x571.png)


So on the right here we have the actual framework of what usually exists when you’re talking out on assisted evals. So we have our inputs. It’s going to an LLM with some kind of prompt.

So something like, I want you to do XYZ, we get our outputs, and then we’re gonna go to our evaluator. So this is where we have some kind of prompt like. I want you to evaluate my responses for correctness, or I want you to evaluate them for being verbose–whatever it is– and you could also have, like coded evals, which I think is important.

And then you get the test result.

So this is what the current framework is, or the typical framework and we’ll get into a little bit more about the Evals.

But the goals here are to develop an evaluator for greeting LLM outputs but validate the quality of these evaluators through alignment of user preferences. So that second one’s the real key point there.

Anything you want to add?

**Aparna Dhinakaran: **Yeah. So first up, actually, I realize we didn’t mention the paper authors. So this is an awesome paper coming out of UC Berkeley. Shreya Shankar–she actually tweets a lot of really good content about the space. Go Bears.

I guess maybe just a quick zoom out of the paper and why it matters.

So people are building LLM applications. We work with a ton of folks who are doing this. I think, where what people are trying to do is, how do I actually evaluate the outputs of these? So in the image that you see there, there’s all the inputs which could be the contacts to retrieve documents, whatever it is, they have the prompt, and then they have the LLM output itself.

There’s kind of been a path, and this is really more common. You see it on the ML side, where there’s these common coded metrics. So think about the AUCs PRACs, like typically common standardized metrics, people will code them. It’s deterministic.

And that’s one category of metrics.

And I think in the beginning people were trying to use them for things like summarization tasks. Can I use the blue score? Can I use rouge score? And so those are standardized type of metrics.

But what we see across all the folks we’re working with is another paradigm which is called LLM-as-a-Judge that is becoming really popular. It is probably the most popular technique we’re seeing out in the ecosystem, and the reason for it is well, first off, if you have evaluation tasks that if you, if you’re doing anything other than honestly, even summarization.

And you don’t have a ground truth. You’re not going to be able to use those coded metrics and those metrics do depend on having some type of ground truth versus with the other approach, which is kind of the path. Let me see if I can annotate the screen here.

Okay, I can’t. But it’s just the metric prompt and the evaluator prompt over here. Yeah, thanks. Sally, basically what it is. It’s a little meta–it’s using AI to evaluate AI–but you’re basically passing the output over to another LLM call. And you’re giving it an eval template. What they’re calling the metric prompt. And you’re asking an LLM to evaluate: how good was the response? Did it meet XYZ criterias? Which we’ll get into…

And yes, it’s using an LLM, so some people are skeptical, but to be honest, the reason it’s getting so popular is because you don’t need a human. You don’t need ground truth. It’s way faster. It’s way cheaper. And so if you can find some way to test and validate on some data set that it works 80 or 90% effectively, you just have this much cheaper, much faster approach to getting back evaluations for your model. So it is becoming a very, very common practice to do it this way, but as Sally’s mentioning, it’s pretty hard, because people don’t know how good these metric prompts are, how good the eval prompts are.

And this goes back to the title– Who validates the validators– how do you know if it could be better? How do you know if it could be improved? And so that’s kind of what this paper is starting to break down is, let’s evaluate our evaluators.

**SallyAnn DeLucia: **Yeah, it’s really like taking it to the next step. We’ve kind of proven out that the LLM-as-a-Judge is the best way to kind of evaluate. But I think there are some gaps especially depending on which tooling you’re using. And so this just builds on that, and you can kind of go talk about that a little bit more.


### EvalGen Workflow


![EvalGen Workflow](https://arize.com/wp-content/uploads/2024/05/Image-2-1024x570.png)


So this is their their workflow here this is, if you were to use their tool kind of the flow that you would go to and so the first thing you do is it’s it’s part of chain, for do, you would access this multi eval node and then through the interface, there’s a few different options for setting your criteria. And I think this is something that’s super interesting about what they’re proposing here. And so it’s three options that you can do. You can start by inferring, so this is where they’re actually using LLM and AI. However, you want to think about it to generate the criteria.

So it’s kind of looking at the data looking at the responses, the inputs and deciding what would make sense to use as criteria.

The second one’s probably what a lot of people are more familiar with. And that’s when the user themselves are manually selecting the criteria. So it’s like, I want to: look at the format. I want to look at the verboseness of the response. The correctness…Things like that.

And then there’s a third option, which is grading. And you could think of this as user feedback of like, good or bad. So kind of a simple label that you can start there to evaluate the responses.

Aparna, anything to add on those?

**Aparna Dhinakaran:** Yeah. So this is actually the three big, I guess, adds here. It’s like, Okay, either the tool itself can come up with this criteria, which is amazing, right? Because then you don’t have to think about. Okay. So I have this type of summarization task. Here’s maybe common criteria concise.

We see that a lot of people are asking that if you’re generating some type of response? Is the tone what you’d expect it to be is a tone consistent across the responses? So I think the inferring criteria, I think, makes a ton of sense based off of like super valuable cause you’re suggesting what they should care about. But of course, then there’s this, you know, for my specific application, a generic criteria might not just cut it, and so on.

This iterative workflow of which I think we were talking about, we really liked–how do I as a user, if I specifically, I don’t mind if it’s verbose I actually don’t care about it being verbose, I actually more care about it being accurate.

So how do I go in and like, specify that criteria myself, manually?

And then some people will prefer the other, which is maybe they start with the other approaches. Let me start building a golden data set, and I don’t know what my criteria is. I don’t know if the response is good or bad, until I go through the exercise of actually grading them myself.

And so you kind of see the like Section D in this flow, someone’s actually doing the thumbs up doing the thumbs down. And that’s their way of figuring out: Okay, well, how did I figure out if that was good or that was bad. And so they’re figuring out that criteria in this process of doing the grading.

**SallyAnn DeLucia:** We’ll get more into this. It’s definitely like a cyclic flow. But I think you explained it really well. It’s kind of like the first and last options here are kind of like un-opinionated flows. Maybe you don’t know what to do. Or you need to build that golden set. And then this middle one is more. When a user has, like, an opinion of like: Okay, I actually only care about it being correct, that’s all I care about and so they can go in and do that.

So these are the three options. You get the criteria, this is where you can kind of adjust. Then you would view the actual prompt, the results from the criteria, and then you can do a good and bad thumbs up, thumbs down, and that actually gets used, and we’ll talk about that in a little bit more detail.

But at a high level, this is the EvalGen workflow here.

**Aparna Dhinakaran:** And I think you can straight from the beginning of that workflow they’re starting with like this is not a one and done type of thing. And I think we feel this, too, SallyAnn, as we’re building out for different customer use cases or our own use cases don’t just ever come up with one template, and then you feel like it’s done. You go back to that golden data set. So I think this was really nice, just to see that there’s different flows.

**SallyAnn DeLucia: **Yeah, totally. I agree. It’s all iterative, like every part of these element pipelines is just a very iterative process here.

So I guess we could talk about the pipeline here.

So on the first slide we showed you what the pipeline is for kind of current evaluators. This is the Evalgen evaluation pipeline. And so something I thought was really interesting about this paper was the fact that they break down the evaluations into this concept of criteria in assertion.

So I really love this idea. And so what a criteria is, is like that first layer of what you’re looking to evaluate the LLM response on. So in this example here, we want it to understand if the responses are polite or not and then they add the second piece, like the criteria, is very like what’s in the traditional flows. But this assertion is what’s kind of new, are the actual guidelines to assess the criteria, which I really like.

So you can see here that they’re calling out specifically, words like, “Please,” “thank you,” and “sorry” indicate politeness. So that’s something new, and you can kind of see it in this flow here’s the same as the flow we showed you before. But this green box is going to be the EvalGen.

And you can see here that you know they get the candidate criteria. But then, you know, with an LLM, they actually get these assertions as well.

So it’s really cool to see that I like that idea of love giving it a little bit more guidelines. Something about alums that we know is they’re non deterministic. So when you give it a little bit of extra guidance, it kind of increases the chances of you getting a reliable result. So I like that a lot.

So the LLM here, I think they use GPT-4 exclusively in this paper, but you could substitute this for any LLM, theoretically.

It’s going to suggest that criteria, it generates multiple candidate assertions for each criterion which I think is really cool. So we’re doing the multiple iterations. It’s not just one criteria or one assertion it’s, you know, multiple.

And then they actually rank the assertions by comparing them to the human grade sample. So this is where we start seeing this kind of flow like, if you look at this. Here. We’re getting the criteria. We’re getting the assertions. But there’s this iterative flow here where the users are coming in. It’s grading. We’re changing the criteria. And it’s just kind of going through that cycle until we feel confident about the test results here.

**Aparna Dhinakaran:** So you see, there’s kind of like the human in the loop, which is in the pop up there where they’re saying the things like we were saying. Oh, is it concise? Is it polite?

Want it to be? But then, if you had to get down to an actual assertion on it.

So if you’re going to something like this, the polite has to say, “Please,” “thank you,” or “sorry,” it could still, be polite without saying those things. And so I think there’s like this balance of like, what are the assertions? How specific do you need to be? And sometimes, when you’re using these LLM evaluators and you’re not building those assertions itself under the hood, you know, there’s these implicit assertions that are being made.

And so you might think of something if you were going to go back and do the human grading. And you might think of something still plight, even though, if it doesn’t include these words, all of these come back to how do you actually get really concrete about this concept of assertions?

It’s really hard. You don’t want to be too prescriptive, but this is the most concrete way to tell another system, to replicate what a human would do.

So I think that like as we were discussing this earlier, we were talking about–maybe we get to this in. Oh, it’s actually the next slide we could get. It like, is there a benefit of like, how good is the LLM itself in the beginning, coming up with its own as it’s inferring the criteria?

How good is that coming up with those assertions? Is there certain types of tasks generally better on? Is there certain types of task that it’s it’s not that great on. And how do you get that view into those assertions so that you can then know what to go fix or improve? I think that’s a hard challenge.

**SallyAnn DeLucia:** It’s almost like we’re applying, you know, some level of evaluation to our evaluator. Right? Like, that’s what this is really doing is we’re taking the human. We’re adding it to the loop and we can just have a better grasp. And we can iterate.

And I think that’s important, because that’s what you’re really calling out is like, how do we know if this is like the right set? Or if I’ve done too much? And this review process really helps us to do that.

One last thing I’ll call out on the side before we go to the next is another piece that I really liked is that the new assertions are checked immediately. Once we go through this kind of loop, and they remove any of those poorly performing one so kind of make sure that we have super high quality, super reliable results. And so that constant iteration and improvement is something that I really like about this, this pipeline that they put forward.

**Aparna Dhinakaran: **Do you remember how they check that immediately? Is that just based off of that human grading?

**SallyAnn DeLucia:** Yes, it’s actually, we’re gonna touch it. I think on the next side, we can go there. So we can see it’s using these metrics. So they basically use the they rank essentially using coverage and the false failure rate. They use that combined to then rank items, and then, like the top ranked ones are considered, I I think, wanna say 10. We can go check the paper, but there’s a certain ranking that they use, and that becomes kind of like their gold standard, and then, you know, poor performing ones are the ones that they would remove.

**Aparna Dhinakaran:** Got it, got it, got it.

And let me just tackle Raymond’s question in the chat here. So Raymond asks how this would handle sarcasm?

In the previous one of okay, maybe they weren’t polite, but they just threw in the word, please. I don’t know, specifically about how this data set, their eval did on sarcasm. But it’s a really good question. I think it just underscores the point of two specific assertions might not actually hit your criteria because one is politeness you want to be able to catch. If someone’s not, you know it’s being sarcastic, but just because they throw in the words, please and thank you, doesn’t always mean it is.


### Is More Assertions in Evaluations Always a Good Thing?


![Comparison on EvalGen and SPADE across pipelines](https://arize.com/wp-content/uploads/2024/05/Image-3-1024x574.png)

So leads us to really this question, which is, is more assertions always a good thing?

And so there’s kind of a paper that they were comparing against their EvalGen framework as opposed to the SPADE framework, which is a prior work in this area.

And I think the key numbers here is actually so obviously they tested on the same data set size. They had the same number of bad outputs. The important thing here, though, is that you’ll see in the EvalGen paper, there was slightly less, I think they said. In most cases it was like almost half the number of assertions.

So this is like how specific they were in their criteria, but it still did better in terms of coverage, especially on the product pipeline workflow. So this was a specific data set in a specific workflow that they were testing. And so in that one, it did basically almost almost 2X better? Maybe.

Compared to the previous paper, without being as specific in the number of assertions. And so I think that’s kind of like the key thing here. And then alignment to it did better and SallyAnn, do you want to go over the coverage?

**SallyAnn DeLucia:** Yes, we have the definitions up here. These are the metrics that they define. If in the definition, so probably be more similar to some other metrics as we have coverage, and that’s like how well an assertion finds good responses, false failure rate. This is avoiding falsely marked good responses as bad.

And then we have alignment.

So the alignment is the harmonic mean between those two metrics. So you could think of that as like balancing the accuracy and consistency there. So these are the three metrics that they’re using to evaluate and compare these two methods down there.

**Aparna Dhinakaran: **I mean the thing you want. And I think this is like the hard thing we struggle with as humans, too, is like, I just want to say what I want. And I want the LLM to understand specifically, and figure it all out. And then when you start getting into all these nuances of the assertions. And you’re like, Oh, you’re defining all this at that point.

You’re getting to a spot where you’re doing a lot of work to refine it. And so I think I mean the goal–my take away from the goal of the EvalGen workflow, was like, how do we make it easy and simple enough so that people have something to get started with?

But then you just leave them with that, and they aren’t happy. And so you need like iteration. And you know, reinterpretation. And I think we do this a lot when we’re building 1,000 things for customers. We see that like, okay, maybe we were too strong and specific about one thing. And because of that, there’s a lot of things that could have been marked yes, or good enough that we said were hallucinations or etc.

I think that that was a really good concept, or a place to start–can I do as much of the work and lift that off of the user?

**SallyAnn DeLucia:** Totally. It’s a good jumping off point. And when we get to the user feedback, you can kind of see what ends up happening when you actually go through this flow, I think you’re describing it because it’s what we go through with customers all of the time, this iteration. It is really interesting to see that no more searches is not always a good thing. It’s, I think, always a fine line with LLM prompting of too much too specific and not specific enough. So it’s interesting that the same problem applies here.


### EvalGen User Study Takeaways


![User Study Takeaways](https://arize.com/wp-content/uploads/2024/05/Image-4-1024x569.png)


And so they did a user study, that was a big part of this paper. I believe they had nine participants take part and actually use this framework that they put forth. And it was interesting.

Six started with auto generated criteria. That makes sense to me.

I mean something we talk about with customers all the time. They want the out of the box kind of solution. And so that makes a lot of sense that the majority of the folks want to start there. One participant did write their own criteria, and then two actually started with just the manual, like labeling process, too. So we had a variety of different users under entry points of how they started interacting with them.

And these were some of our key takeaways. So I think the first one is really important and something we’ll kind of spend a little bit more time on is this idea of participants continually refining and reinterpreting criteria based on their observation.

So, what this really means here is, you know, starting at the beginning of the flow. If, say, we had a user who did auto generated–once they’re going through the review process of that, they start to identify gaps, maybe in their criteria. Or maybe we’re being too specific.

So they realize that they have to kind of continually adjust the grading approach that they’re using. And so it’s just like this cyclic flow of like you adjust the criteria, then you kind of observe how it’s doing. And then, as you’re going through and you’re manually updating, you find something else that either you’re being too specific about or you forgot about and so participants all like across the board realize this kind of need to to iterate on it, which is really interesting.

And it makes sense to right like, the more time you spend with it. You just kind of just naturally recognize more and more things you want to to touch on. And this is kind of what you were describing what we do with customers right? First off say, like, oh, we need to check hallucination, and maybe we do something that’s too strict. And then we’re like, Oh, maybe that’s not really a hallucination.

And so this happens naturally, this framework just gives you a good way to go about like just being structured about it.

**Aparna Dhinakaran:**  I think the other question we have is like, how much, though, like grading of output?

So people ask us a lot of like, how big does the grading approach affect building that golden data set? So how big does that golden data set need to be? If you only have a couple of examples of something that is maybe being too strict. And then you’re optimizing your eval prompt, based on that, you’re over indexing on something. And they mentioned that in the paper, too.

And so I think that the question I would have is like: How many grading approaches did they feel like they got to a spot where that alignment metric that they cared about the coverage metric they cared about got really really good.

But we actually probably start, I’d say, with a lot of the folks we work with, we definitely ask for this concept of a golden data set, because there’s nothing like a human having thought through the criteria themselves. Especially for folks who are building these LLM applications, like going through and thinking about that criteria yourself, instead of just like first pass relying on an LLM. I think, is super helpful to know where your criteria actually is.

**SallyAnn DeLucia: **That makes a lot of sense.

So some of these other takeaways here. And we can kind of get into a lot of stuff you just touched on our next slide. Just some other things to call here is participants did find that being able to customize like the metrics, and just using those to align the evaluations with the expectations, was super helpful, particularly for any of like the subjective or like complex criteria.

There was often some misalignment between interpretations of criteria, or maybe inconsistencies to like converting natural language versus code based assertions so that can kind of be expected whenever you’re doing any kind of conversion there. Or the subjectiveness right? Like, if you have one AI engineer who set the criteria, and one that’s actually doing a reviewing, they might have different interpretations of what that criteria means. So there is some misalignment that happens?

And something that is interesting that they definitely called out even the participants who took part in this study. They did have some significant skepticism around LLM judges eEssentially especially in production environments. There’s still some skepticism of if this is the right reliable way to assess LLMs and production. So those are the key takeaways.

**Aparna Dhinakaran:** We have a question from Ryan– is there any open source data set for evaluating LLM responses with respect to different criteria or metrics, hallucinations, relevancy, toxicity, etc.?

There is.

We actually have an [open source evaluation library, Phoenix](https://github.com/Arize-ai/phoenix), where you know a lot of these criterias or metrics you’re talking about, we have actually built out and tested on open source data sets. And there’s a lot of different ones out there, the Wiki QA one–let me just pull up a couple just to drop it in the chat for y’all to look at.

I think, the nuance that we see is that even if you’re using these open source data sets, like we mentioned, they’re great for helping you build out that initial. What is the, you know, the eval template.

But the issue is does it have all of the criteria, or all of the assertions that’s necessary for your application. And so if in some of these data sets their focus is not on, let’s say, a specific–I don’t know. They’re not asking questions to say, consumers. They’re asking more about general knowledge type of information.

Just the response, so things like, what does conciseness mean about general knowledge types of questions versus consumer, product, type of questions? What information would you like, for example, with some folks who are building chatbots for recommendation engines they want to include things like cost of the actual product or price of the thing that they’re selling and location of it, and what other reviewers have said. And so all of that might seem a lot, for I don’t know if that qualifies as concise. And some of the data sets that you’ll see that are public out there. But it’s totally okay, and that’s actually what they want when you’re giving these products in more of that like recommendation chatbots.

Yes, to answer your question, and let me just drop the link of where you can see some of these evils and the data sets they’re tested on. Yes, there are out there, I think they’re a great first place to start.

What do you do afterward to incorporate those metrics back into your own application? Used cases where that golden data set in your own world is super helpful.

**SallyAnn DeLucia: **Totally. And it’s like it’s just that flow we’ve been talking about, right? Like you’re talking about starting with the pretested kind of evals. And then you do some kind of maybe grading. Looking at your own data set to try to make this connection. And then you’re implementing. You know the custom kind of eval. So it’s exactly the flow we’re pretty much talking about.

We just have another good one. What, exactly, is ”golden” about the data set?

So with that, Aparna might need to help me up with this answer, too. It’s just basically you can think of it as a good or bad example of a set of examples. Really. So it’s kind of aligning that criteria with where you could actually test against like these are all really toxic responses, or these are all really good responses. Anything like that. You can kind of set the criteria, and then you just gather your examples.

**Aparna Dhinakaran: **It’s a data set with labels essentially, and you’re using it. And those labels can come from humans. And it’s golden because you’re using it as kind of the benchmark to then evaluate how good was your eval template?

You’re using it to basically evaluate how good was my LLM evaluator when I asked it to evaluate these. How good was it relevant to my golden data set labels.

Okay, this one’s actually really interesting one that really only became evident as we were going through the paper. I was like evaluation criteria can change. I don’t know why this is a little bit of a you know, being.

You’ll start out, and someone’s like, I want to be super strict on something like certain criteria they want to be super strict on. So is this age appropriate as one that people are really strict on, as opposed to some of the other ones like, is it concise enough? Etc. But what we noticed is that some of these users might start off either super loose or super strict. And then, as they’re actually grading the examples, there’s a lot of nuance. And what actually matters. And that requirement actually shifts.

And so whether that’s actually in and the paper lays it out, there’s a lot of different reasons. It could happen because of requirements. You want to get tighter on controlling. You want the data itself. This is kind of more of a data drift type of thing, but data of the outside world’s changing. You have different people who are evaluating. It’s not always the same person.

And so that criteria and what those assertions are could slowly drift over time, and what that means is what your LLM evaluations were at one point might not be what might not be matching the bar that you’re looking for at another interval of time.


### Criteria Drift in LLM Evaluations


![Criteria Drift](https://arize.com/wp-content/uploads/2024/05/Image-5-1024x576.png)


**SallyAnn DeLucia: **And so like that just kind of that caused us, like the inaccuracies, in your your eval and the misalignment. So I think the solutions here are really important, and this again, it’s what EvalGen is doing what they’re proposing here with this framework, which is that regularly update criteria to stay relevant. It seems like that is really required.

It doesn’t seem like maybe I mean, as things advance with this kind of inferring criteria, you could maybe skip this step, but for for right now it seems like that kind of looping through and and and having these cycles on your criteria is really gonna be important to make sure that you’re always having these accurate and reliable evals in your production system.

And I think collecting input, when you have these human evaluators that are maybe creating the golden data sets or judging the evals getting their thoughts and collecting that so that you can kind of put it back into your criteria. Those are all things that are going to be helpful in this process.

But yeah, this is I agree Aparna, when I read this, I was like, oh, yeah, that makes sense. there’s drift criteria, things change. But I really never thought of it that way prior to reading this.

**Aparna Dhinakaran: **It’s just interesting. Because I feel like in the typical ML metrics type world where you’re actually using code generate.

It’s like auc or whatever it’s not like the definition is changing the metrics have a drift. The metric might your standards for what’s good, and maybe that’s the way to think about it is that your bar for what is a good auc, and what is a bad auc might change here, because we’re actually using the LLM to do that evaluation and define that criteria. The definition itself could change. And I think that’s the definition could change, because it’s coming out with the outputs, and then the bar for those outputs can also change. So I think that is like a slight little shift, something the ML folks might not be used to.

**SallyAnn DeLucia: **Totally. It’s like, kind of a new nuance of these systems here.

We do have two questions, if you want to answer those before we do that last slide there, I know we’re having a fun time.

So, the first one is: How are folks dealing with large variation of templates? Tools, template designs, etc. Especially now that we’re feeding LLM outputs into other LLMs.

That’s a really good question.

**Aparna Dhinakaran:** I think. So yeah, it’s a really great question. I mean, I think prompt management is just important. So we see a lot of people doing this in a couple of different ways.

A lot of this is code based. So I think people are thinking about prompts as code, especially when you have things like prompt templates where every you have variables that go into the prompts, and so you are essentially building out a template for what the actual prompt will look like, you’re not constructing it every time it’s likely more on the application side. But you’re also. You are doing this in eval templates, of course, as well. And so we’re seeing a lot of people actually use tools like get backed type of version and control systems to handle prompt management.

It’s great if it’s close to code, because then you don’t have something in some UI thing that you have to pull the latest version. And so it’s nice when it’s kind of using similar best practices that we do to code of having it versioned and close to some kind of code versioning tool.

So that’s probably the most common thing we’re seeing.

I think you need some place of maybe groupings of app templates, eval templates. tools. And then, even within an app. I think we have the one of the next eval sessions workshops is on like router based architectures. So we’re seeing a lot of people break it down. So it’s not just like the system’s not just like one prompt one output. A lot of this is like multiple components. And you have a router that’s actually doing the routing to different components in the system, and so defining what those templates are that go to different components is also part of the templates you need to manage.

The questions have been great. Here’s another:

What are your thoughts using LLM to validate LLM response, including selecting first criteria and then testing response on that criteria minimum 2 plus extra LLM calls to validate the response. What will be the cost of such solution? And is it scalable and usable in the industry?

Okay, so let me try to first understand this question. So sounds like the ask, here is first, basically using an LLM to validate the response. Just based off a criteria. And then you’re basically validating those criterias as well.

I don’t know. Is there a good example that we could maybe come up with to help and help grock that? So I get your point of like. You’re breaking down basically the eval into like these multiple criterias. And then you’re evaluating how it’s doing on maybe the each of the criterias itself. So you have like an Eval, and then you have, like a validation layer of each of the criterias.

If I’m totally honest with you, I don’t see this approach right now being used that much. And I can give you my take on just like why, I think first people are themselves trying to struggle and grock the idea of like moving an LLM to do the evaluation call, and the thing that they’re struggling with is like, do I need to do it on all of my data?

To which we actually say samplings pretty often, you’re trying to get a gauge of how good your application is doing. And so I think there’s already this, like, okay, if I’m spending. Let’s say you have. I don’t know an X number of budget, and you’re spending 90% of it on the application LLM, calls itself. I think there’s always debate of like, do you spend 10 or whatever like it depends on how much you sample, because it might be too expensive. So like, how much are you actually gonna sample to generate this evaluation? And now adding additional two extra calls to validate, I think, can be tough.

But the other thing we recommend that it’s kind of getting to your point. But it’s different. We actually recommend explanations on the emails. That actually less of like valid yes or no, or binary on the eval. But more of can you explain why you came up with this response?

And sometimes you can do it. You know, in our library you can actually, there’s ways to do it in a single call. There’s ways to do it in two calls. But you’re basically, that explanation just gives you slightly more reasoning.

Let’s say it, said hallucinated. Maybe it hallucinated because it didn’t use the information within the reference text. So that explanation is super helpful.

And you know you could call that maybe an another way of validating the response, the Eval response.

**SallyAnn DeLucia: **Yeah, I think it is helpful with that criteria, right? Cause a lot of times when it’s generally in the explanation, i’s using the criteria that was set for us. You can kind of see, maybe, where you need to loosen that, maybe add something. Maybe it’s not catching what you want it to? So I think that is a way that you can streamline the process and still get after what you’re asking there.

**Aparna Dhinakaran:** I’m just gonna drop evals with explanations doc here for you. It kind of explains kind of where, when it can be useful.

**SallyAnn DeLucia: **Yeah, I guess there’s what was one comment about the additional latency in the application a lot of times. It’s a slight increase. But a lot of times you can do it like, you know post-hoc so you can kind of remove the latency from that. And in the app, like, when you’re having a user interact with it and kind of do it post-hoc so that you can get the explanations in the emails still. So that would be one hint that I would share but they are generally pretty fast, and so latency is pretty minimal.

It does depend on a few different factors. But that’s one thing I call out in regards to latency.

**Aparna Dhinakaran:** Yeah, I think doing it, decoupling it. So you’re not doing at the same time, as the application is what we commonly see. A lot of people.


### Takeaways for LLM App Builders


![Takeaways for LLM App Builders](https://arize.com/wp-content/uploads/2024/05/Screenshot-2024-05-10-at-9.28.30 AM-1024x574.png)

**SallyAnn DeLucia:** Absolutely awesome. We got just two min. So you can just do these last takeaways for all you LLM app builders.

So even though there is some skepticism around LLM-as-a-Judge, we do believe it’s the strongest path for evaluation. We’re seeing a lot of folks get a ton of value from using LLM-as-a-Judge to evaluate their LLM systems. We talked about this a few times in this, this talk here. But figure out what that criteria is, tends to be the hardest part. We have to kind of really define what the best insights going be on where to improve.

So it just takes some time to kind of develop those insights and and understanding of what you mean. So that’s definitely the trickiest part. It’s an iterative process building that criteria. So we talked a lot about that during this fee reading of needing to set up the initial criteria, have the LLM judge your responses and then go ahead and actually grade those yourself and build up your golden data set. So this combination of tools, the inferring, the adjusting, the grading. All of that is really what’s gonna help you build the strongest evals.

Some questions Aparna and I still have maybe for our own research or for the paper researchers. Is there a world where just inferring criteria is possible? We’d love to understand better what the gaps in the user study were like, what we talked about like, how many rounds did they need to actually get to a good spot? Were they happy with the inferred criteria? Did they find themselves adjusting it?

We have some kind of open questions around that.

And then one thing that the paper said that we are also firm believers in is just having that control and transparency around the eval criteria is really gonna be crucial for yielding reliable and valuable results.

So as Aparna mentioned with like the pre-built evals. It’s a really good starting place. But when you start having control, and you can kind of really dictate what that criteria is, gonna be the eval. That’s where you’re really gonna get your good results and be able to take actionable improvements.

Anything to add Aparna?

**Aparna Dhinakaran:** I think, if you got anything from this paper talk it’s iterative. I think that’d it basically. And I think we’re gonna see a lot more workflows like this on how to validate and do it. So thank you everyone, so much for joining. And yeah, hopefully. Hopefully, you had a good time going through this paper with us.

**SallyAnn DeLucia: **Thanks. Everyone.
