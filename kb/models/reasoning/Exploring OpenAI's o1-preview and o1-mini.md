---
title: Exploring OpenAI's o1-preview and o1-mini
topic: models
subtopic: reasoning
secondary_topics: []
summary: Analyzes OpenAI o1-preview and o1-mini from a reasoning-model perspective,
  including expected strengths, limits, and evaluation implications for production
  teams.
source: arize
url: https://arize.com/blog/exploring-openai-o1-preview-and-o1-mini/
author: Sarah Welsh
published: '2024-09-27'
fetched: '2026-07-11T04:50:06Z'
classifier: codex
taxonomy_rev: 1
words: 8914
content_sha256: e5475a6b2c1dde20d185e7d269ea8ec5170a5c1c0318f32e685c3b71d7681b50
---

# Exploring OpenAI's o1-preview and o1-mini

OpenAI recently released its o1-preview, which they claim outperforms GPT-4o on a number of benchmarks. These models are designed to think more before answering and handle complex tasks better than their other models, especially science and math questions. We take a closer look at their latest crop of o1 models (including o1-mini), and we also highlight some research our team did to see how they stack up against Claude Sonnet 3.5–using a real world use case.

### Watch

## Listen

## Dive in

## Analysis

### Introduction: o1-preview and o1-mini

**John Gilhuly:** Hello, everybody joining in here. How’s it going? We’ll give it a couple of minutes as people filter their way in, but I get started a minute or two.

**Aman Khan:** Yeah, this should be an interesting one. I feel like I’m like, I definitely think more, more folks joining us on the interesting as well as we go through.

**John Gilhuly: **Yeah, definitely.

Can also give a little bit of quick intros, as folks are sort of making their way. And it’s always a good way to spend the first minute or two.

I’ll go first, because I think mine’s less interesting than yours. So I am, John. I’m a Developer Advocate here at Arize. I do a lot of our events, a lot of tutorials that we’re putting out a lot of the content kind of try to make sure to stay on top of all the new releases and try them out. See how they work with a lot of our different features for Phoenix and for Arize. So you guys have probably seen me on a couple of the materials that we’ve been putting out recently. And yeah excited to talk through some of the o1 stuff. Aman, I’ll let you introduce yourself as well.

**Aman Khan: **John, you’re being way too humble, man. John, for folks that are listening in like John is absolutely crushing it across our entire community surface area right now. So yeah, major kudos to him on covering a ton, including helping out with a lot of the research that you’ll see that we’re going to cover later. 

But for my introduction, my name is Aman. I’m a Product Manager here at Arize. So leading up our LLM tracing product line. So if you’re working on LLM applications, you know, feel free to reach out, happy to try to help in any way that we can. As well, yeah, pretty excited to jump into.

**Aman Khan: Y**ou know, a little bit around what we’re seeing around o1, and where the space is headed. And yeah, this should definitely be an interesting one. It’s been quite a week for models.

**John Gilhuly: **Alright, I think we could probably get started with probably just more people joining as we keep going through here.

Yeah. So today, as you see, we’re gonna go through some of the o1 material and release material that’s come out from open air over the past week or so. We’re gonna talk through kind of talk through o1 what’s been released. There’s not a ton of architecture things in there. So we’re going to sort of glean as much as we can out of some of the information released. We’ll show some of that stuff as well to talk through kind of the chain of thought side of things.

So the decisions made there and then we’ve also done our own benchmarking and research testing out o1. So we’ll kind of compare results that we got against some of the results that that open air released as part of their release materials.

And then talk a little bit more about some of the industry effects that we foresee with this. This is sort of a new kind of model in a way that’s been released, or at least positioned as a new kind of model. So we think there’ll be some kind of fun topics to debate at the end there as we go.

As always, with these kind of things, feel free to drop questions in the chat as we go. We’ll try to answer those as we’re going through just because it’s always more fun when these are more of a dialogue. Especially because this is also new. It’s kind of fun to have everybody jump in, so feel free to drop questions as we go, and we’ll tackle them as we jump through.

Alright. So for anybody who missed it. Back on the 12th we had a release from OpenAi with this preview of their new o1 series of models. They’ve reset the numbering back to one, as they said, because this is such a big leap forward and performance in some areas. So, they’re marking this as kind of a marquee release–o1 preview.

And then a mini version of that same model have been released since the 12th and the positioning of this is, the models are really supposed to be very good at reasoning through complex tasks, solving kind of harder logical problems, math problems, coding, kind of these, more problem solving approaches, as opposed to just sort of text generation and things like that.

So they’re specifically focused towards that particular area and how they’re positioning the models.

**Aman Khan: **Yeah, I’ll add as well like it, you know, there’s a lot of speculation. They call it like a preview. They released mini. As far as I know, we’re still waiting on like the full release which definitely should be pretty interesting as well to see if the capabilities improve even further with with the full release. But yeah, it almost feels like a functional proof of concept of this approach that they’re putting out there and showing that this new kind of model architecture that, you know, basically has those improvements that you might expect to see on tasks that have like multi-step planning and reasoning. So yeah, interesting kind of call out there that it’s like, not the full model yet. Just a preview.

**John Gilhuly:** Yeah, yeah, I think we definitely talk more as we go too. I feel like, part of it is they want to see if people are going to use it for those sorts of use cases. And there’s like enough of a split there because they’re kind of dividing use cases that this is really good for explicitly, as opposed to saying like, it’s a sort of general smile that can do a lot of different things, and it might be better in this area, or very explicit like this is good for this sort of problem solving approach.

So yeah, I mentioned things that they positioned. It’s very good at in some of the release materials is reasoning and logic kind of science, coding math types of problems, especially like more difficult problems that, as Aman said, requires some sort of planning forward. So being able to go through and plan out, okay, some examples they give are like creating a game like creating the code for like a basic kind of game, and it actually will go out and plan what it’s going to do, then execute on the steps, and then we’ll do some kind of sort of working back through errors that it might have made.

And it’s using a chain of thought approach to do a lot of this which we’ll talk about as we keep going, too.

The other thing that it’s that it’s sort of touted as being very good at as a result of this is protecting against jailbreaks or other kinds of attacks against it. So it’s being sort of positioned as a very safe model as well.

So talk a little bit more about that, too. But that’s kind of what’s being put forward is the strengths of the model.

And then it does have some areas where they say it’s actually not the preferred model. Which again, we’ll talk about too, some text generation kind of things, some tasks there.

It actually is less preferred than a GPT-4o. And then also because it’s a preview, right now, it’s not supporting web browsing like automatic web browsing and uploading file and images and things like that we actually don’t know if that’s because it’s a preview, or if that’s just a sort of function of the model that might actually continue to be the case, but I would imagine they’ll probably add those capabilities into it a little later on.

But yeah, so you can see this excerpt from the announcement that they released, that it’s missing some of these features. But they will probably add some of the web browsing and file kind of interaction in the future here, too.

And then I want to show the kind of part of the quick example video that they have here, because it’s sort of fun, I’m sure a lot of folks have seen this, and I’ll probably go sound off for this, so that I don’t blow out anybody’s speakers, but you can see that the model itself is very good at kind of setting up some of the longer term coding tasks, so you can see in the example they have somebody putting in instructions here go through and generate a game in this case. That’s like a sort of just a quick little flash game. But you can see it’s giving some detailed instructions here, saying what some of the images are and some things like that. But then the biggest thing with this model is that it basically like when you put in some sort of request, it sits and thinks for a while and kind of craft through the solution, and it can take kind of a long time to go through and create whatever that solution is gonna look like.

And then, once it has thought, it will go through and kind of execute from there with the generation. So you can see in this case. We thought for 21 seconds, and we’ll talk more about this, too, but you can kind of see it as this log of like: Here’s what I thought through, here’s what I went through. Showing some of those pieces there. Which is sort of the chain of thought, but it’s not exactly it. So we’ll talk about that a little as we go too.

**Aman Khan:** I think there’s a very like subtle hint as well in the the text file as well like the prompt that they show which is the better description you get, the better output you’re going to get, at the end of the day. So with this, with this type of prompt as well. 

I think that’s definitely kind of comes back to how you prompt it. The level of detail you give, you know, the better result you’ll get from the context going into the reasoning. So I thought that was an interesting maybe a subtle nod here to prompting still being really important in this model.

**John Gilhuly:** Definitely and also, the longer time it takes to generate responses to me makes it seem like something where you should spend a little bit more time like constructing, crafting the prompt include a bunch of info there, and almost like ask it to do more in one iteration as opposed to…a lot of times I use that like existing models to do more like, okay, try this. Okay, now tweak it to be like this, not tweak it to be like this.

**Aman Khan:** The quick iteration. Yeah, it’s kind of like, how people get used to like how they’ve how Google queries or Bing queries sort of start to resemble a certain pattern, and people stopped asking questions, they just type in the words and like, get the top query results like it almost feels like prompting with the faster model starts to degrade to something like that.

And now, this is kind of showing that that’s probably not the approach you want to take here. More likely you want to take a more detailed prompt, and spend time on the prompt because it takes longer for an inference.

**John Gilhuly:** You can check out this example as well, too. But it’s cool. The code that they generate actually works out of the box and generates a little game for them, which is pretty cool.

And then I see the question in the chat around: How is it when you go to debug the code? These models get pretty messy.

I guess there’s maybe two versions of that question. It’s like: does the code it generate work pretty well, or is it like having to debug it from there?

I think, anecdotally, I’ve seen it work pretty well for specific setups.

But then, if you’re if the question is more like, how is it at debugging code that you’ve put in to it to actually go and debug?

I think I’ve tested a little bit with that, and it’s been generally pretty good. It is slow, so like I don’t use it in the same way as I use, like a cursor combined with like plot or something along those lines, because it is so slow. In that case I really haven’t used it to like. Do a lot of live ticky tacky in line debugging. I don’t know if you’ve experimented with that?

**Aman Khan: **Same here, I have yet to really fully integrate it in my flow as well. I still find that I get pretty good results for my flow with the faster model, faster inference. But maybe this is more helpful from an architectural standpoint. It kind of feels closer to the replet agent chain of thought approach than you know where you want to maybe scaffold or start a task from scratch as opposed to maybe picking up something existing so.

I think we’ll talk a little bit and give some examples of that later as well. But yeah, anecdotally. I think it’s definitely gearing towards that cold start problem.

**John Gilhuly:** It’s a good question.

And so I want to talk a little bit again, because they haven’t released a lot of the architectural side of things. But they did release some info around the chain of thought reasoning approach and some things there. Basically just say they use a large scale reinforcement learning algorithm to reward the model for using chain of thought reasoning, and kind of to get it, to use that by default.

They mentioned a couple of things that are interesting here, which is that basically, you get better model performance by adding the ability to increase the training time with this reinforcement learning algorithm. So the longer they train it with that the better the model perform.

But then also, the longer they give it, they give the model to think on each sort of query, the better it performs as well, too, which is interesting. So basically, if you up the time that it takes for the model to respond to you after you’ve query, it’s gonna perform better.

Which is interesting to me that this doesn’t tail off at some point, because to me, I feel like, if you really like, explode out the chain of thought and let it go as far as he wants to, I’ve seen cases where previous models, will kind of confuse themselves in a way, andloop back on things, or like like second guess, and then go the wrong direction. And so it’s almost like you had a window of how long you wanted it to go in that chain of thought.

Whereas this is sort of suggesting that they can just blow it out as far as they want to, and it’s increasing the performance of model beyond that which I thought was interesting.

**Aman Khan:** Yeah. I wonder what’s truly going on underneath the hood for that, too. Like, what sort of you know? What that planning step or chain of thought. Looks like if it’s the chain of thought we know from the paper or or some other approach that they’ve taken. 

**John Gilhuly:** I wish we had more info.

**Aman Khan:** Yeah exactly. I don’t know if it’s unclear to me. If it’s exactly that algorithm or something else.

**John Gilhuly:** But yeah, for anyone who’s not familiar. I think most folks on the call are generally probably familiar with chain of thought, but the idea here is that you allow the model to think more step by step, through things, and kind of instructed and and and position it towards

planning out. It’s the steps it’s gonna take. And continuing down that process and then reflecting back on previous steps, examining the completion of each one to see if it’s made some sort of mistake.

And some sort of mistake along the way. So the idea is, it can kind of correct itself. Think more, step by step, as opposed to trying to jump to the answer.

It’s been a popular technique for just generally improving model performance. Over the past couple of years, I would say and so it’s always been a technique that some folks have used. You have things like the replit agent that have used it to more intensity as well.

There’s a bunch of examples within the release, too, that OpenAI put out so you can see what some of this looks like. So like the coding one, for example, you can say: Okay, over here on the OpenAI preview I’ve got, create a script. And then you can say: Okay, show the chain of thought that the model went through. One that I actually really like is this first one, they have the cipher one where they’re saying, here’s this sort of text, and this translates to think step by step and then use that to decode this.

And you can see if you there’s a lot of info here, and it’s kind of a fun one to like read through in detail. But you can see this is sort of what the model is thinking as it goes through. This is the chain of thought that it follows, and so you’ll see it will start to go through.

Okay, let me count the letters and see if there’s anything there, let me break them down, and then it starts to realize that that doesn’t work in certain cases. So it’ll go down these paths, find a blocker, and then return back up to an earlier part in the thought process. Which is kind of cool.

**Aman Khan:** Even drops like: idea! This is an interesting one. Like, yeah, it is sort of interesting. There, you kind of see, maybe again, like early sparks of something there in terms of reasoning.

**John Gilhuly:** I love the “hmm.” It’s like, “Hmm, that didn’t work right?” 

But yeah, one thing that I thought was interesting with this, too, is like, it sort of positions it and makes it seem like it’s thinking like a human would think through a problem.

But if you actually like, read through this full example, you’re going to get to a point in it where, like, it becomes really obvious to you how the cipher works, because you can recognize. I forget where it is. There’s like a moment where it realizes that it thinks you think of the letters and pairs, and then it doesn’t realize that. Or I think it’s like, maybe it doesn’t realize it should think of them in pairs, and it just doesn’t compare the things in the right way.

Anyway, I wish I had a better description of that.

But there’s basically a moment where you’ll read through this and you’re like: Oh, it’s really obvious what the cipher is, and then it still goes down another bunch of different paths to figure out what it is.

So it is sort of still, like linearly problem solving. Oh, it’s right here, actually.

It’s summing the letters like the pairs of letters and saying: Okay, if I send the letters, let’s take the average of that. And once it and that will give them the letter that they need. But they basically realize, okay, so we’ve got to get to T from O and Y. O is 15, y is 25, so the sum is 40 T is 20, and so it’s like, Oh, let me try subtracting these things, and let me keep going from there and test. And it tests out a bunch of different alternatives, you see like 4 or 5 alternatives there.

When, if you’re a human reading through this, you pretty clearly immediately go. Okay, 20 is half of 40. That’s probably the average there, and you can kind of go from there. So I don’t know. That was an interesting one to me. It’s like you. It’s thinking very linearly, but at the same time it sort of it’s almost positioned to think like it seemed like it’s thinking like a human would. But at the same time. It still doesn’t quite match in the ways that a lot of people’s brains would work. At least how I think of it.

**Aman Khan: **Yeah. And who knows what’s going into their chain of thought, if there’s a Max token that they’re trying to hit, or something, you know, depending on how much time, if it’s just producing more and more chain of thought there, to fill time. Also could be something there who knows?

But definitely, very interesting to get a peek inside the ways that the model is thinking.

**John Gilhuly: **Definitely. I mean on that note, though. One thing that’s kind of important to call out is that what we’re seeing for the chain of thought is also not the exact chain of thought that it goes through. So there’s a very interesting part of the release where they talk about the fact that basically there’s a quote from the release. But they say that they want to have the model freely express its thoughts and unaltered form.

Partly because they want to be able to examine that for and actually have a quote here. They want to be able to monitor the chain of thought for signs of manipulating the user is a quote from there, which I thought was interesting.

But they basically we don’t want to modify how it does change of thought. We wanted to do that sort of unaltered, so that we can examine that and learn from that.

Because of that we can’t train any sort of, and we can’t train that chain of thought generation process. And so there might be things in the actual chain of thought that we don’t want to show to users. So they show a chain of thought, but it’s not exactly what’s from the model, and it’s a little unclear right now, whether they’re using a separate model to actually modify the chain of thought output and then make that available for users.

Or if they’re using another version of the same model. Or there’s something happening here where the actual chain of thought is translated into something that’s useful for users, and is a little bit more like sanitized, so that’s something that’s worth knowing. Is that what you see when you use the model for chain of thought isn’t actually the unaltered chain of thought. It’s just a sanitized version of it.

**Aman Khan: **Plus like I mean, even, you know, even just to speculate. No, no way that this is like backed up by anything. But you know, one speculation could be that could be valuable training data as well, right? like how to solve a problem and what their secret sauce is there could be could be valuable IP to own. So sanitizing it could make sense for a few reasons.

**John Gilhuly: **And to their credit they do cite competitive advantage, as one of the reasons they don’t share it. 

**Aman Khan:** And there’s a good question in the chat, which is: How does the model generate chain of thought? Is there another model that creates this chain of thought? How the user prompts and feeds it back to the main model, or what’s happening under the hood? 

Great question, Eduardo.

The short answer is, we don’t really know.

Not to speak for John on this one, but like you know, the truth is that we’re basically consuming a finished product that we aren’t able to go in and like, tear down and look at how it works underneath. We’re basically just: we just have the results, and our own anecdotal evidence of using it. You know, OpenAI hasn’t shared much around the architecture of the model so far.

So yeah, we have the same question on our end.

**John Gilhuly: Yeah. **And I don’t know, this feels funny to me, this last sentence is manipulating the user. I wonder if that’ll be something that we see.

**Aman Khan:** Yeah that’s a big one in the mechanistic interpretability space. And eventually as these models get more and more capable. What their interaction with humans starts to look like is something that I think a lot of researchers are starting to monitor and keep an eye on

So this is cited as a safety concern, I think, to have a sort of being able to inspect if there are any signs that the models might be generating some sort of emergent properties that might be interesting. So.

**John Gilhuly:** Alright. So then, we have some evaluation data opening eyes put out. We have some of this, and we have some of our own as well, too. So we’ll go through both those together and give you guys a picture.

One of the themes here is that for very hard problem areas, o1 is a much better performer than Gpt-4o. Or previous models were like, if you look at the math competition, the aime, or some of the code force competition stuff. You see, Gpt-4o, basically couldn’t solve a lot of these problems and would rank very low.

And then o1 is now given this big boost. And again we’ll remind you that we don’t have access to o1, as of yet. We have access to the preview of o1, which is the yellow that you see here. So apparently, o1 is going to be even more powerful on some of these setups.

And the fun thing is, it starts to kind of outpace some experts, some human experts. So the AIME they talk about is a sort of math competition problem set and basically, o1 out of the box performs at a 74%, or really 83 is probably the true alignment to, or the true result that it would get, because in this test you get 60 submissions per problem. I think it is, or 50% submissions per problem.

So this 83 is probably closer to what it would actually get.

But then, if they remove that restriction of how many submissions you get per problem. That’s part of this competition. Then they can take it all the way up to this 93 which is among the top 500 students nationally so, this model is technically, if you remove that limit of submissions, the US Olympiad, which is kind of fun. So it’s a very high scoring in that particular kind of problem area.

And then also, like you can see in the last last sheet here as well, too, that surpassed human experts on this GPQA diamond problem set, which is kind of a PhD graduate level problem set that it goes through. They’re very quick to say that it doesn’t mean it’s better than a PhD at all things, or even these problems. It’s just like in this specific example. It outpaced human experts.

I guess, Aman, I’m curious for your thoughts on if this a moment of: hey, now we have models that are surpassing human experts in certain areas. Or does this just feel like we’re picking individual things where it’s better than human experts. For, like very specific kinds of tasks or tests.

Yeah, I mean, I think if you look at some of the discourse online and like even their positioning of like, you know, compared to PhD-level students like we’ve gone from in the last two years like high school to college to, you know, experts in a field like lawyers to now, Phds, which is like truly people who have spent–at least from a benchmarking perspective–a lot of time on a particular subject.

So I do think that the increase in the benchmark is interesting to see that the language around the model is starting to be more important positioned as you could have a Phd level scientist to help you with, you know very specific like, imagine a fine tuned version of o1 on like biochemistry or organic chemistry, you could have a Phd, you know, next to you helping you solve the task. I think that’s what the product positioning of o1 is meant to be here.

So yeah, I think, like the scaling up of the benchmark is indicative of their where they’re thinking the use case would be

**John Gilhuly: **Nice. Yeah, yeah. And there’s actually, I think there’s a part in there, too, where they talk about how a bunch of benchmarks we used to are no longer really valid, because we all the models we’re comparing against have already outstripped these. So we’re kind of churning through different benchmarks that they use for as we have each new model release.

### Human Preference Comparison to GPT-4o

**Aman Khan: **Yeah, I’m excited to get to the human expert comparison, or sorry, to the human preference comparison, because I think that’s the moment where I was like well, what is going on here? So, yeah.

![Human preference comparison to GPT-4o](https://arize.com/wp-content/uploads/2024/09/SLIDE-1-1-1024x571.png)


**John Gilhuly:** Yeah, totally. So one more thing we’ll show first, and then we’ll get there is that some of the other kind of improvement. We see over some of these other benchmarks like MMLU, and things like that that we used previously. Oh, one is kind of improving across the board. When you look at these types of things. 

Again, these are very specific towards problem solving in a lot of cases. And you can see things like the AP English lang, for example, it’s equivalent to the Gpt-4o performance. So there are some areas where the increase from the model is actually much smaller, but then you have more logical problem solving, like the LSAT or Physics, or something like that, we see there’s a much bigger increase.

So kind of going towards some of the human preference stuff which maybe I’ll just actually skip to here–it is interesting, because there’s certain areas where, o1 is actually not preferred compared to 4o. So what we’re looking at here in this chart is kind of comparing the outputs of 4o and the outputs of o1 for each of those two basically. Do humans prefer one or the other on different kinds of tasks.

And so you can see that 4o is actually preferred here by a small margin for personal writing. So for text generation or personal writing, humans are choosing the response, borrow more than they’re choosing the o1 response, at least for this test they did.

But then, as you get to more quantitative and sort of logical problem solving kind of areas, then you’re getting more preference towards o1. So it is interesting. It’s like this is not just like, Hey, this is a new model, and it’s better across the board. It is very much better at specific areas.

And then there’s still a slight edge for 4o in some areas like a lot of it seems to be around like text generation and qualitative kind of sides in that regard. So it’s an interesting result as well.

**Aman Khan: **Yeah, I think this for me was interesting because, I think it actually shows that I guess you could view this as, yeah. It’s like, almost like a regression in certain tasks, like, editing text looks like it’s about the same personal writing is a little bit lower, which again could be dependent on the task definition.

But what is interesting to me is that the mapping of the other tasks like mathematical calculation or programming–I think we should also hop to the to the coding one after after this one, but the the model can get can be better at coding, can be better at reasoning, but it almost seems like, for, like writing tasks or creative tasks there’s a slight regression here which is interesting, that that OpenAI themselves is calling this out on this particular kind of subtask. So I think it’ll be interesting to see as people use this more. You know, it doesn’t even make sense to use it for things like creative writing or writing in general, as much as coding or or reasoning.

And I wonder why that is. Like why it’s only better at tasks that seem to be more logical versus reasoning through something more creative as well.

**John Gilhuly: **Yeah, one thing that comes to mind, too, is that you’ve got the error bars here as well and like, there’s a world where the personal writing is actually 50-50, you know, it’s like within that error range. And so I do wonder is it that the models improved generally, and then it’s also very good at this sort of logical side, and so that, like general improvement, pulls it up more, and if you just use the same like, say, they had used the chain of thought kind of reinforcement learning technique back when 4o was released, would we have seen like much worse writing then? 

So I’m curious how much of this gap is if this is like a bigger gap that’s being closed by just an improvement in training techniques and say, the next iteration of 4o is going to blow this out of the water from a writing perspective, you know.

**Aman Khan: **Totally, yeah. That’s a great point, it is within the error bars, so for all we know this is a little bit of their data being represented here versus like in, you know, actuality.

But I just thought it was interesting to see such a huge jump in some of some other areas, and not a massive leap forward in others. So yeah it’s like, what would a human prefer, I guess, in terms of writing? It’s very subjective, you know. People’s styles are different, maybe that could contribute to this as well.

**John Gilhuly:** Yeah and I guess I’ll show the coding eval here.

### Code Generation Performance Comparison

![](https://arize.com/wp-content/uploads/2024/09/SLIDE-2-1024x572.png)



**Aman Khan: **Yeah, this is interesting because of the ioi as well. That particular benchmark as well.

**John Gilhuly:** And if I remember right, I can check the thing. But the ioi is the fine-tuned version of o1 right, if I remember right?

**Aman Khan: **That’s what I’m reading. I’m trying to find the exact reference on if it’s a fine tune, or what sort of training was done there.

**John Gilhuly: **I should have included that in here. But I’m 90% sure. It’s like if I pull up the thing here. There’s a further fine tuning competitions improve.

**Aman Khan:** On that data set?

**John Gilhuly:** Yeah.I believe that’s what we’re looking at here. But it’s not 100% clear on what they show. But I think this is sort of implying that they’ve fine tuned for the like, at least programming competition problems. Maybe they haven’t used specifically the code forces one. 

**Aman Khan:** Yeah, just a quick Google, they do drop like codeforces has made their like submissions public. So you could go look at those as well if you want. If you’re this which is cool to see since it’s like, kind of crowdsourced.

**John Gilhuly:** But yeah, I mean, I think one thing that’s worth mentioning is that like, if you look at code forces, they’re hard coding problems. It’s not like auto complete your line, you know. So this is another area where it’s like, yes, the models are very good for those. 

But going back to an earlier question like, you probably aren’t gonna use this to do auto completing your code. It just takes so long to do or like to do minor edits to code. It’s more like, start from zero. And like, I have to solve a hard problem, let’s have a model try to figure out a path to doing that.

**Aman Khan: **Okay. So I did find the reference in the paper. It says they “initialize from o1 and trained to further improve programming skills.” 

So that’s why I was like, I’m not sure if it’s a fine tune, or if it’s actually like something else going on here might be something else going on here as well. So yeah.

**Aman Khan: **Based on that, it seems a little bit more like there could be something else going on? 

**John Gilhuly:** Do you envision that they’re gonna allow fine tuning for o1 anytime soon?

**Aman Khan: **Yeah, well, I don’t know. I mean, I’m not sure about timing, but I would imagine that this again, kind of indicates that okay, training the model in some way, you know, adjusting the weights for a task like does improve performance. That’s kind of a good selling point to take on some more workload from a compute perspective based on proprietary data. 

So, if your business had its own tasks where you wanted a human level sort of performance like I can imagine you would probably want a trained model to help with that.

So yeah, I I don’t know. And and again, no idea what the complexity setup looks like feels like they’re probably going to go tackle cost and latency next or they can go do training optimization. But yeah, that’s since that those two seem to be the biggest hurdles to usage at the moment.

**John Gilhuly:** Before we jump into those, because we’re gonna touch on latency in a bit. In a second, there’s a couple of questions I wanna make sure we cover. 

One is around circle of temperature and the reasoning process: Are you able to kind of set a temperature parameter to free up the creativity of the problem solving?

I don’t believe that there is an ability to set temperature. Actually, I see Matthew jumping in as well about mentioning the same. I don’t think that you have any sort of temperature parameter that you can set for o1 which is new for this model. You’ve been able to set that for 4o and on previous models. So they’re limiting that in some way, at least, for now.

**Aman Khan: **Basically, I mean, even if you go look at it, there’s like a little bit of helper text in the playground from OpenAI. It says, system instructions and model configuration are not available yet. So they haven’t even allowed you to like set system system prompts or there’s really nothing that you can do there, as Matthew says, like, you know, basically, it’s just the message in the model.

**John Gilhuly: **Which I mean, it could be the way that they’re positioning that though it could be that it’s a more fact function of being a preview versus being like a capability that won’t exist in the full release, too, though.

**Aman Khan:** Totally. I have a feeling this was sort of like a little like we can get into it. But in a bit of like once we get into like public perception. But I do have a feeling. This was like a bit of a you know, equivalent to like chat GPT sort of test to see what people would use it for, how people would use it so that they can determine. You know their own investment here as well.

So yeah, it feels like it feels like a beta to me.

**John Gilhuly: **Another question we had, too. What is your measure on the level of breakthrough here? Is this considerably more groundbreaking than taking your favorite LLM, creating an agent that’s told to take a deep breath, break down the steps, and then executing and analyzing the steps of each sub task?

I’ll share my take, because we’ve actually done a bunch of agent building over the past few weeks.

I think if we had built an agent that was specifically gonna do like, let’s say, the code force problems. And we set it up to do that. We could have set up something that was gonna have that level of reflection and like chain of thought, and added those pieces in. To me the biggest thing is that now I’ve got a model that will do all of that out of the box. And maybe this is jumping ahead to some of the industry effects. But to me it’s like, okay now, I could just use o1 to do that as opposed to spending a few hours trying to code and pull together an agent that has all those extra pieces to it.

So, my perspective on the breakthrough here is that it’s gonna make it easier to use models out of the box for more complicated tasks and not have to cover that ground with extra tooling that you have to set up yourself, but I guess yeah, to me it’s not like we’ve now blown the lid off of AGI, It’s just like we’ve removed a lot of the extra stuff that you have to do and bake that into the the model itself.

**Aman Khan: **Yeah, I mean, I think it’s like the argument is that okay, you have, like a really good like LLM substrate layer. This is sort of like, you know, maybe getting closer to like an application layer above that which is, reasoning closer to your LLM API, or to your model level layer, as opposed to having to go and tweak the system prompts, or agent prompts to do as you’re saying. Here, like, take a breath. Or okay, maybe it’s not take a breath, like what the impact of those like random tokens are on the overall performance? 

I feel like it’s the goal, the argument to be made in favor of o1 is to move that reasoning a little bit closer to the model there and just have that optimization happen underneath the hood.

But yeah, that’s just a speculation.

### GPT-4o and o1-preview Safety

![](https://arize.com/wp-content/uploads/2024/09/SLIDE-3-1024x564.png)



**John Gilhuly: **Alright. I’ll keep this going because we only have a few minutes left actually, but yeah, one other area is the safety side of things.

So with this they also tap that the models much better at detecting harmful prompts and preventing jailbreaks, which I think is also an interesting area.

This is sort of the same theme of, like the models doing things that you previously had to build extra tooling to do yourself. So if you’re detecting jailbreaks, maybe this is an indication that the model can do some of that for you instead. And so you could kind of…maybe guardrails, or something that you can do in slightly less of a degree because o1 is pulling that kind of thing in.

But it makes sense that the kind of reflection and the fact that it goes through each step multiple times gets better at detecting things and try to sort of sneak through it in some way.

I also have to imagine, though, that there’s some element of like existing jailbreak prompts are partly tuned to certain models, and so give it a few weeks, and we’ll have some people who will have created more o1 specific jailbreaks and this number might actually go down.

**Aman Khan: **Yeah. Good point. Who knows what a jailbreak for this type of model looks like? Could be very different.

### Arize Benchmarking of o1-preview

![](https://arize.com/wp-content/uploads/2024/09/SLIDE-4-1024x570.png)



**John Gilhuly: **Cool, and then I want to share some of the benchmarking we did as well, too. Just because this is all we saw that OpenAI is like, announced kind of thing.

We basically did a whole research thread that we’ll we’ll link as well that I’ll kind of summarize as we go through here, where the hardest eval that we do typically is this timeseries data set evaluation, where basically, we have a hundred different time series data sets–a few more than that, actually.

And then each one of those has some metric graphed over time for a world city so, imagine like temperature in a city is one metric, and we have that over time. And so you have a big Json object of all of these different metrics.

And then we have an LLM go through and try to detect anomalies within that, and it has to split that down to like specific metrics, it has to split it down to specific cities that those metrics are relevant to.

And it also has to do that all across these different instances essentially so, it’s a very difficult task for most models to do.

We also did some varying of context length which we’ll show too and then we actually made this even harder by making all of the data points fractional. So they’re all zero to one, and we just brought them all into that range, as opposed to having broader numbers. So this kind of time series analysis is something that we actually do in real world use cases in our Copilot agent that’s built into the Arize platform. So this was a real world thing we were kind of testing: can we use this o1 to improve the performance on that type of eval?

And if you guys scan the QR code there’s we have some of the traces, so you can go actually see the traces of each of these evals run, which is kind of fun. So you thought those links on the bottom will take you towards that. If you want to check out what that looks like.

Here are some of the results that we saw:

![](https://arize.com/wp-content/uploads/2024/09/SLIDE-5-1024x573.png)


So like previously the best one we had, 3.5 Sonnet. Basically each of the red boxes here is a missed anomaly, the green is a detected anomaly, the sort of neutral is neutral, and then there are some false positives in there as well, too.

So Claude Sonnet was the best one we had tested earlier this year, it found 60% of the anomalies.

o1-preview found a hundred percent of them, with one false positive as well. So it actually did a lot better across all the tests that we ran. o1-mini doesn’t do as well, so that’s interesting note as well, too. But we did see a huge performance boost here from o1 preview, which is pretty cool, it actually like was able to kind of go through and create that performance boost

There’s more detailed results that we have, as well, too, of going through different context lengths and things like that. But you can even see on the longer context length, one at the top here, o1 preview still finds almost all of the anomalies and misses free in this case. So even at the higher context windows, it also still performs very well.

o1-mini did not perform, which is interesting, but really it was not up to the same level of performance.

**Aman Khan:** Yeah, who knows whether it’s dropped out with Mini. But this was a really interesting result. It kinda can persuade us that like, okay, maybe maybe Mini is definitely not as capable as a preview of some of these tasks. 

### Takeaways: o1-preview and o1-mini

**John Gilhuly: **And so I mentioned like, this is a real world use case.

The other thing to note here, though, is that each of those run throughs took like 2 to 3 minutes. So the latency is like a real concern here, not concerned. I’m just sure those improve the latency over time, but it does mean that, like for our case, it’s a Copilot agent in our dashboard. We can’t really sit there for 2 min or 3 min and just have it spinning, thinking, and so there is some element of latency where, like this is kind of geared towards these more almost offline tasks where it’s doing reasoning. And you’re not like getting a user experience on it. So we’re not pulling into one. As far as I know, we’re not pulling o1 into copilot as a result of this, but we’re definitely gonna keep paying attention to it as they try to improve some of the latency over time here.

So yeah, I guess we have a couple of minutes left. I kind of jotted down some of my own takeaways. There’s discussion areas to think about. But I wanted to kind of summarize my own takeaways from this. And then we talked about some of the questions. But one of the big things is that to me, now, we have a kind of new state of the art model for these logical offline instruction tasks. So if I have a very hard task, I need to do with that. Oh, one is going to be the one that I go to all of the Evals that we’ve seen other folks running to kind of back up with the performances there, even though the latency is not there.

And then you might have o1 and o1 Mini becoming models for code copilots over time. But again, that latency becomes a big issue that you have there. So you need to have latency kind of come down on this before it’s used in any kind of user facing products as well.

But yeah, Aman, are there any other takeaways in your mind of like top line you’re coming out of this with?

**Aman Khan:** Yeah, I tend to look at how people use the model like what the reception is both our own testing and then our own anecdotal uses. So for me, in those  three areas like it, the reception does generally seem to be that this model is better at, you know, tasks that require planning tasks which this actually comes back to the very first one of the first slides, which is like, the more context you give the model the better it’ll be at planning. And so it’s actually a little bit, you know there’s an optimization there of like the time you spend on the prompt to get a better result.

And then I haven’t yet swapped it out myself for coding and like cursor. But I’d probably try that and see. But anecdotally, I think some folks are saying like it’s better than 3.5 Sonnet. But some people say Sonnet is amazing. So like, you know, so yeah, a little bit unclear there just yet.

I definitely think this is a hint in the direction that you know, this next series of models is gonna go, which is more capabilities, maybe more training abilities as well on specific data. So you have, like a PhD sitting next to you, or something like that. But yeah, the latency is brutal right now, for any sort of usage, so I don’t know. There was a benchmark that we’ll throw up in the links as well. This is like an anecdotal result of like, you know the latest Gemini model that just launched.

So I think maybe we even have to start rethinking some of the benchmarks here like, maybe it doesn’t make sense to use some of these models for solving, you know, basic problems and actually just reserve them for more complex ones.

**John Gilhuly:** Yeah, the takes of the model routing companies will be interesting. I want to see if there’s some element of these models being baked into model routing like martian or something like that. And then, yeah, I definitely want to get cursor to use this as my composer model. So I’m excited for that to come through.

**Aman Khan:** Totally. Yeah.

**John Gilhuly: **Unfortunately we are at time here, so I’ll wrap it up there. 

Lots of exciting stuff is coming there to see. I’m excited to see the full release of o1 coming through. And yeah, those should be good over time.

As always, you guys haven’t tried out Arize or Phoenix, check them out. Phoenix is our open source tool. [Give us a star](https://github.com/Arize-ai/phoenix) if you’re feeling magnanimous today. And then you can always sign up for a free account on Arize to test this out as well, too, and test out some of that Copilot that we showed, which is fine.

**Aman Khan:** And I’ll plug that if there’s any papers you would want us to cover as well, feel free to drop them in our slack community. You know something you would like to see covered. I’m happy to do that. We can even bring in paper authors. Would love to cover what the community wants to see next.
