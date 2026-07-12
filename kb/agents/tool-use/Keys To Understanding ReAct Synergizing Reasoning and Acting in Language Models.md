---
title: 'Keys To Understanding ReAct: Synergizing Reasoning and Acting in Language
  Models'
topic: agents
subtopic: tool-use
secondary_topics:
- models/reasoning
summary: Explains ReAct as a reasoning-plus-acting pattern for agents and how it structures
  tool use.
source: arize
url: https://arize.com/blog/keys-to-understanding-react/
author: Sarah Welsh
published: '2024-04-26'
fetched: '2026-07-11T04:48:43Z'
classifier: codex
taxonomy_rev: 1
words: 7677
content_sha256: 58f1dd8d4ec0499da234e2b3a98318375c01d2a18b87663ca9bfad12e26fcff4
---

# Keys To Understanding ReAct: Synergizing Reasoning and Acting in Language Models

![ReAct - blog SallyAnn and Aman](https://arize.com/wp-content/uploads/2024/04/ReAct-blog-1021x560.jpg)

              # Keys To Understanding ReAct: Synergizing Reasoning and Acting in Language Models

## Introduction

This week we explore ReAct, an approach that enhances the reasoning and decision-making capabilities of LLMs by combining step-by-step reasoning with the ability to take actions and gather information from external sources in a unified framework. There is also a ReAct demo with a colab, and a deep dive into reflexion.

## Watch

## Dive in

## Listen

## Demo: ReAct Prompting Framework

## Analysis

### Introducing ReAct


**SallyAnn DeLucia:** Awesome. Well, thanks everyone from joining. I’m SallyAnn. I work on the product team here to rise. And I have Aman with me. Do you want do a quick intro?

**Aman Khan:** Yeah, hey folks, my name’s Aman. I’m also on the product team, working very closely with Sally Ann. These days a lot on the Al and generative side of the world.

**SallyAnn DeLucia: **We have a really good paper today. ReAct. It’s a prompting technique, and we’ll also cover some other prompting techniques. So just to give you an idea of what our agenda looks like. We’re gonna read through. Read using lately, we’re gonna show you some of the best parts of the paper. We also have a coding sample with ReAct super simple implementation, using OpenAI’s API. So, looking forward to that, and then we might go into some other prompting techniques like chain of thought, I think we’re actually gonna focus a lot on reflexion.

So yeah, with that, we can kind of get to it.

So what is ReAct? The title comes from the idea that the researchers were really trying to mimic the way that human intelligence works. So if you think about anytime a human’s given a problem, or they’re trying to learn something. They kind of reason through something. And then they take an action.

So this is something that they were trying to bring to LLMs, and so ReAct comes from having a re-reason component of the prompt. And then an action component of the prompt. So the whole concept is, it integrates reasoning with these actionable outputs. And so it allows language models to interact with external environments to retrieve information. So that’s gonna be the action part of that. So you can think of that as calling a tool or a function, to get some kind of information to them.

You know, it’s kind of the cyclic loop of reasoning, taking action until eventually the other one comes to an answer.

So I kinda hinted at this. The main goal of all this research was to enhance those task solving abilities by mimicking human intelligence. Something I always find interesting–I’d love to get your take Aman– human intelligence is always our gold standard, like with every paper that we read. There’s some kind of human intelligence, human reasoning that we’re really trying to emulate. And I just find that so interesting. I feel like it’s always been the backbone a little bit to machine learning is that neural networks are mimicked off the brain.

So I just love seeing this. And it just makes so much sense to me when researchers come up with these new principles just to, you know, do what humans do.

**Aman Khan: **Yeah and what’s funny is I’ve been spending more and more time. Maybe folks on the call can relate to this–with all of the latest, in the last week of LLM news. It’s been obviously an interesting one with Llama 3, you know, a lot of really interesting information from the researchers and from Mark Zuckerberg on, like what the team did to train that model, and then you had like Phi-3, which we might have to come back and revisit. We just applied to it felt like a little while ago.

But another small model. It does feel like, you know, what’s interesting is, you actually have the research side which is building and training these foundational models. And they’re trying to do kind of the same thing right? They’re trying to build models that have some level of what we kind of understand to be like human intelligence, although, yeah, you’re suffering large amounts of data, and you’re suffering in trillions of tokens. But the goal is really to have general, you know, General Hu levels of human intelligence. And so they’re doing their job of like modeling. How the brain works and trying to like, you know, model these like action neurons. And you know, different types of neurons with the neural nets.

And then on the prompting side, once you take the output you’re like, Oh, actually, the model out of the box is fine. But it’s not good at Xyz thing. So we’re going to try and optimize it for that. So it’s in a way you could kind of think of it as like fine tuning for almost an application, it’s not actually fine tuning.

But in a similar way it’s changing the parameters, the output, you know, the input parameters that you’re providing to this LLM to actually get some action or output. So yeah, I think that’s really, it’s really interesting. I think that’s a lot of what we’ll cover is how these different prompting techniques, kind of optimize kind of in small ways in their own ways for certain tasks.

### Hotspot QA, AlfWorld & ReAct

**SallyAnn DeLucia: **Totally yeah. It’s super interesting. And I love your note, too, like the coming at it from 2 different ways, like, there’s the modeling aspect of like, let’s get the models to actually mimic the way the brain works. And there’s this prompting side of it like how can we just take the models because they do pretty well and do it? So we’ll definitely dive into that a little bit.

So yeah, this is making it more practical. For real world applications, and I think some of the key features of using ReActor, it’s suitable for various applications across different domains. It’s really just this prompting technique. It quickly adapts to new tasks with minimal data because of the way that the model is being prompted. It really does demonstrate efficient learning capabilities, and I think it just enhances the interpreter like we’ll see what the coding example you can kind of exactly track how the LLM is coming to its answer, which is something that I think is a little bit difficult with a lot of these LLMs.

We don’t have traditional explainability and not yet not something that’s super flushed out. For these elements. So like kind of relying on your prompt and getting the response. That kind of shows you the journey that the LLM took to come to its answer, I think, is something that’s pretty cool and powerful.

**Aman Khan: **There’s a thread of like, even when we get to like interpretability for LLMs, it might actually do one of these things which is like, reflect or ReAct and or reason, and then act, and kind of drop all of the steps that you did in between, and then use those intermediate steps up, you know, as a form of like interpretability to and and then we know that out of the entire context window, depending on how much of that you know, it ends up being like self reinforcement for the LLM to perform a task, which I’m sure we’ll go into.

It’s really interesting to see how much of the next action that the LLM takes is actually dependent on how you frame the input prompt in the first place.

**SallyAnn DeLucia:** Totally. Yeah. I think we’ll get into that a little bit later in more detail. But first like, let’s take a look at some of these different methods. So what the paper really needs to do is they put forward this ReAct prompting where they have the thought and action and observation.

And it goes in this kind of cyclic manner until it comes to like finish where it actually gives an answer. And they test it up against a few other types of prompting. So there’s the standard prompt where you can think of it as just like, there’s nothing special done. It’s kind of like that 0 shot type prompting where it’s just like, here’s do this with no extra information.

And then we have the chain of thought which you can think of as reason only. So this is like, only give the reasoning behind each step in the prompt and then they have the opposite side of that which is just action only. So this is just like kind of where the element is just choosing a tool or choosing some function to call to get some information. It doesn’t include the reasoning side of it. So you know, standard and the two components.

And then we have ReAct. So you can see the examples here:


![Hotspot QA](https://arize.com/wp-content/uploads/2024/04/Screenshot-2024-04-26-at-10.46.33 AM-1024x848.png)



This first one is from HotspotQA, so this is going to be like a question answering kind of benchmarking. I think it’s all based off Wikipedia questions and answers. There are a variety of different features to this data set. And so this is the one benchmark that they use. And so you can see on the right here, this is like the ReAct prompt. So you can really see this structure that they’re putting forward where we have this thought that’s like this is the initial reasoning that I need to go figure this out, then there’s the action, now I’m taking that reason and actually applying it, I’m going to call this function.

And then there’s this idea of an observation. So they kind of observe the results of the action which then kind of will kick off the next cycle of doing all of this. So it goes again. So you can see here first is like I need to search for the apple remote and find where it was originally designed to interact with. It does a search just like a Wikipedia API. And then it comes back, observes that. And then it does another round because it realizes there’s this front row. Software that needs to get more information. So it does it again and eventually gets to the bottom. And it’s able to actually answer that front row is a software that is controlled by that port. So you get that whole list.

**Aman Khan:** And there’s one kind of distinct property of this dataset that I think is really interesting is…So HotspotQA is based on this question answering dataset, but what’s distinct about it is, it’s actually multi hop questions. It’s almost like a trivia type of question. But it’s not meant to be direct, it’s meant to have, like some signal in the question itself about what to do next. So that’s one interesting call out is, that’s a really interesting property of this data set. And what makes it so, you know, so sort of interesting to use for agent types of assessment.

### ReAct Reasoning Tasks Results

**SallyAnn DeLucia: **Totally, because it really requires, you know, the all them to fetch multiple pieces of like Wikipedia Docs, or whatever it is. So that’s a really good call out. And it’s good for this type of application that ReAct is really being researched on. 

The other example below is for the decision making part of the research. So the first tasks are kind of like QA, there’s some fact checking apps using like fever, and then there’s this app world in this. I think it’s webshop is the name of the second part of it. And so this is where it’s needing to make a decision. And like, kind of take an action. So again, there’s here. We’re not introducing the reasoning, only prompting. We’re just comparing the act only to ReAct. So we’ll get into the details of this a little bit more, but just kind of wanted to show everyone the comparison of the different prompts and answers from them all.

Cool, so the reasoning tasks here:

![Results - Reasoning Tasks](https://arize.com/wp-content/uploads/2024/04/Screenshot-2024-04-26-at-12.21.30 PM-1024x576.png)


You can see that ReAct performs better than action alone on both tasks. But it does lag behind chain of thought for the HotspotQA. So it beats it in Fever. So that fact that’s kind of a known thing with chain of thought. It does suffer with hallucination a little bit. And so that’s probably the reason yeah, comes on top is because of that. Those action steps allow it to get that external information.

It’s kind of adding more context to the prompt and reducing those hallucinations. But it’s again. The ReAct is still struggling. What I thought was really interesting is they take the combination of ReAct and a chain of thought. And that’s actually what yields the best results. And you can kind of see that in this bottom portion here.

And I think that’s because ReAct relies on the info that’s retrieved. And so the chain of thought, I think, helps it when maybe the search wasn’t informative, because we see that it struggles when that happens, and it doesn’t know how to get back on track. And I think the chain of thought helps it kind of more easily recover and formulate its thoughts a little bit. But I’d love your take on that.

**Aman Khan:** Yeah, I think as we’ll kind of get further and and like you, you kind of realize like we were just catching up right before this and that you had an interesting point, which is like, so just to be clear, it’s just, it’s reasoning in action. And like the action is something that you know, basically the prompting kind of almost forces the LLM. To like, take some sort of action.

And that’s really true right? The interesting thing about these papers and the academic work is, you’re often trying to like, invent a new form of doing something, accomplishing some task. But the simpler you can make it, the more you can make it fundamental and separate from other prompting techniques. Other things like the more kind of you know, the more it might stand out in research as well.

So it is interesting to see like ReAct plus chain of thought is actually, you know, potentially even more powerful than just the straight up ReAct. And that kind of makes sense because you want to combine these techniques to get the best output depending on the task you’re trying to do. In this case, more complex, multi-hop question answering.

**SallyAnn DeLucia: **Yeah, I feel like we see it a lot with the prompt engineering techniques like a lot of the times. One alone is not the solution. It’s a combination depending on what you’re trying to do, what problems you’re having. So it’s interesting to see that kind of pattern emerge here as well.

So yeah, this is reasoning. So it’s much better than just standard prompting. But for the question, answering, Chain of thought has a little bit better performance there. So that’s the results for reasoning. Then we have the decision making so ReAct from way better than you know action alone. I think that’s something that’s a little bit expected. Because if you think about it with the action alone. Like all their all the element is getting is that response from whatever action they take, they don’t have any of that kind of additional context, and like the chain of thought, part of it or the reasoning, it’s lacking that completely.

So it makes sense in a decision making exercise where you know it has to go through multiple steps to ultimately make the decision that action alone would be worse performing. But what I think is something worth calling out is the fact that we’re still not close to what the human experts do on this task. So that tells me that we’re making progress. But we’re probably not actually ending up where we would want in a task like this, like the whole goal is to mimic human intelligence right? And this shows us that ReAct, unfortunately, is just not able to do that. And it’s kind of not even, you know, close either, which is definitely an interesting point.

**Aman Khan: **What is the IL+RL part there?

### ReAct Decision Making Results

**SallyAnn DeLucia: **Yes, so it’s imitation learning. And then it’s imitation learning plus reinforcement learning and then BUTLER is also at the top. There’s another imitation learning and the IM is actually an inner monologue where you can basically think about the whole environment versus just the one piece of it. Yeah. It’s pretty interesting that they can add that as an additional kind of variable into all of this. It looks like it helps somewhat, but not always. You can see in the different tasks that it doesn’t always help out, but it does for this one here.


![Results - Decision Making](https://arize.com/wp-content/uploads/2024/04/Screenshot-2024-04-26-at-10.58.43 AM-1024x573.png)



**Aman Khan:** Yeah, that’s interesting. right? Like, they call out specifically I thought what was kind of interesting in the paper is ReAct versus chain of thought for the benchmarks. Then they have a you know, a section a little bit more below ReAct plus chain of thought performs best for prompting out a lens, and then they then they decide to, you know, use imitation learning and

IN+IL and and then at the same time, you know they kind of introduce this, and I guess the result that they’re showing here is the base ReAct performs better than those techniques.

But you’re comparing, ReAct with inner monologue, it looks like it performs at all. It improves performance a little bit. But you don’t see IL. And maybe this is just like a fundamental like, you know how imitation learning is. But I don’t see a you know, ReAct plus imitation learning benchmark there. So I thought that was kind of interesting as well.

**SallyAnn DeLucia: **Yeah, I did, too. It didn’t seem like they really elaborated on that, either. So I’m not sure if that was just like a choice they made, or maybe it’s not compatible. So that’s an interesting thing to call out.

**Aman Khan: **Yeah, totally. I was a little confused. I guess I’m additionally. And being like  the training you know, find fine fine tuning or training technique there. But like, why not just apply ReAct to that? 

**SallyAnn DeLucia:** We’ll get to that in the next slide. But they do some fine-tuning exercises there. So it just adds a little bit more confusion. Too bad we didn’t get the authors to come join us then we could have asked them about that decision.

So, what we covered so far, it is great. For those reasons, decision making, it does better than actual loan, but still not where our human experts are.

And so let’s talk about briefly fine-tuning. I thought this was pretty interesting.

So ReAct performs the least effectively among these four different methods. We have standard again, that’s just no real prompting technique. We have chain of thought, action only, and then ReAct. And so when we’re looking just like a base model. And this is all variations of the palm model.

It really does not perform well.

And I think that they call out that it’s due to the complexity of learning for both reasoning and actions. But I think the real interesting part is just with a little bit of fine-tuning, like 3,000 examples, not a lot of examples–it switches and it outperforms all of the other methods.

So we know some of these things like the standard, and chain of thought they tend to work on like memorizing facts. And it does tend to lead to that like fact, hallucination. So it’s probably a big part of it again with ReAct. It does seem to minimize those hallucinations a little bit. There’s no world which I at least think of right now, where hallucinations go away. But we can minimize them.

And so it just suggests that with further fine tuning, with even higher quality data, like, maybe they could do some work on more examples, and maybe it goes back to the quality of his examples used. It just seems to amplify the effects of ReAct, which I think is really interesting, and I actually love to see a lot more research on this here.

**Aman Khan:** Yeah, I just to double down on that, hearing more and more about how the foundational, like, the foundation models, are using synthetic data generation, for the base model training, I’m excited to see more of that synthetic data generation going towards fine tuning and then coming back to see how these prompting techniques actually improve. Because you’re right–that’s just that’s only 2,000 examples–if you turn on Gpt. 3.5, and which, by the way, like Phi-2, was like most of the data, I think it was trained on like the textbook data. And GPT- 3.5 like it wasn’t even like, like the most capable. 

Anyone who’s really interested in this topic could probably go and, you know, generate 10,000, 20,000 examples. Go back, run the same benchmark and see. Oh, across these different model sizes as ReAct actually performs, you could run it on llama and you know, really interesting opportunity to go back and revisit. It’s funny you mentioned right before, SallyAnn–this paper is old! why are we revisiting ReAct? It’s from 2022. And I’m like, oh my gosh it is. But you’re like, absolutely right, like 2022 feels like ages ago.

**Aman Khan: **So the data at this point is pretty out of date. So, it would be interesting to come back and revisit that.

### ReAct Prompting Framework Demonstration

**SallyAnn DeLucia: **Totally, and I think it also highlights the fact that there isn’t this silver bullet when it comes to making these models perform well. And I think this kind of highlights it, too, like we were talking about before. It’s a combination of prompt engineering techniques. It’s fine-tuning, it’s the models, it’s all of it together, and I think that’s an important thing to note.

Let’s look at a coding example. So we want to really show you all how easy it is to really implement this example. So we’ll drop the notebook so everyone here can try it out. But this is just an example, there is this learning log here that we used as inspiration for this but showing you how easy it is to get started with this type of application. So kind of traditional standard installation of just getting your OpenAI, getting some packages. And then you define just a basic chat box class. So this is just gonna manage our conversation flow.

You can see I’m really just setting up that chat client with OpenAI. I’m using 3.5 turbo right now. You can even add in some kind of logging to see how many tokens you’re using.

And then we set up a very basic prompt. So, reading through this, we’re setting the scene that you’re the Lm is to go through this loop of thought, action, pause, and observation. So, the pause is when it’s actually calling that function or taking that action there and then the observation is that the output of the action, and observing whether or not it needs to kind of loop again.

And so at the end of the loop, it’s saying, give us the answer, and it actually outlines the action. So this is a very simple example, again, we grabbed this from that great log at the top.

So it’s calculate–this is like some kind of mathematic operation. There’s a Wikipedia call, so I can access the Wikipedia API to do a search. There’s a blog search that can be done.

And then it gives it some guidelines so like, always look through things on Wikipedia, if you, if you have the opportunity to and it actually gives an example session for all of them to fall. So you can see it’s not a lot properly. Again, this is a very simple example. But like, that’s pretty straightforward. And you can see there’s not much more to it from here.

**Aman Khan: **To pause on that for a sec like like, I do think it’s interesting like it often comes up like–should I be providing examples in the prompt?Yes, you know,  single shot, multi shot like provide examples you’ll see, like, you know, without the examples that it’d be pretty tough to, I think, for the LLM to infer what you mean by taking action. So you do definitely need examples in the prompt. Some shots.

**SallyAnn DeLucia: **That’s a really great call out there. I definitely think it would be confused. That would be an interesting experiment to see if we check that out and put it back in. 

We just have this kind of simple query function that actually, you know, starts the query process when a user wants to ask a question, and then we have our actual action handlers. These are the actual functions that the alum will use. As well as the known functions here. So that’s kind of all the setup of it. You can see that it was like 4 blocks of code with a few functions, one class. Not a lot to get this up and running

And it’s really simple. So I’m gonna run this new one again: what state does Ohio border? And you can see here it’s really cool, like it’s gonna go ahead and not…

**Aman Khan: **So this is something that can happen, which makes sense right, using GPT-3. And we actually observed this before, which is like the first component actually finished, it actually did figure out, oh, I should calculate states that share borders with Ohio, and take an action. But before I take an action, I should pause, and the LLM seems to have taken that very literally, and actually pause without taking a further action. 

So, sometimes we’ve noticed, the pause statement can actually pause the call to the streaming call to stop. So it’s kind of interesting.

**SallyAnn DeLucia: **It gets confused. So let’s run it there again here.

It’s still not liking this. Let’s try one of the other ones.

Let’s calculate the square root of 256.

There we go. It’s working.

Something about that Ohio one. It was getting confused. But you can see here that that same kind of process that we showed from the paper here. The LLM is little bit cocky there, it says, I can easily calculate the square root of 256.

And then it goes ahead and then runs the action. You can see here, it’s the observation here. So it’s observing the output of that action and then goes ahead and gives us the answer. So that’s the gist of it. It’s really straightforward.

You can imagine this being used for a variety of different applications here, but I think the point that Aman and I really wanted to show here was that it can be done with a few lines of code from scratch like you don’t really need anything fancy to do it. You just need that check completion from OpenAI, and you’re off and running.

**Aman Khan:** Yup, we totally. And you’ve got an interesting question here, actually, which is: what happens if you skip the pause?

**SallyAnn DeLucia:** That’s a really good question. I did not test that.  I would have guessed that the LLM might try to respond before it should. But I’m down to do a little live experimenting. Let’s see what happens.

**Aman Khan:** Did you run that code block when you reboot the pause?

**SallyAnn DeLucia: **Yep, I thought I did. Okay, let’s do it again, just to be sure. Run the same one. Here, let’s see what happens.

**Aman Khan:** Still has a pause. Hmm! You might have to rerun cause that’s just a prompt definition. You might need to rerun where that’s being called right?

**SallyAnn DeLucia:** And I actually think the first time I didn’t remove it from the initial guidelines. And I think that could have also contributed to our problem. So it could also be the functions that take a long time, too. So something like just doing this kind of simple calculation. It’s a really fast operation. Doing some kind of retrieval might maybe even take longer. So I could see that also causing different results.

**Aman Khan:** Yeah, totally. I mean, when this paper came out, the latency of the models was also a lot slower. I do think that, the takeaway here is the technique is very valuable to like, you know, decompose the thought, observation, and action, and how you do that, how you construct it together probably requires some prompt engineering as well.

**SallyAnn DeLucia:** Totally. 

But really good example. [We have the notebook. It was shared in the chat](https://colab.research.google.com/drive/1CC4qvYuLYKkIUcbG1pn_bR47kYaukG-3?usp=sharing). Definitely try it out.

But with that we can go into some prompting techniques. Aman, did you want to share or do you want me to continue to share?

**Aman Khan: **Yeah, I can go ahead and share. So we were going to go a little bit further into another. It was kind of interesting. So I think you know the main takeaway from the notebook. It’s just. It’s so simple to stand up your own sort of agent if you’re trying to do anything that requires multi hop. We wanted to just do a little bit of a deeper dive into a couple of more interesting, prompted tech techniques. 

And actually, before diving in, we’d love people’s feedback. You know, during or after this paper if you want us to do a deeper dive, you want to see more content like this when it comes to, you know, practical examples of other prompting techniques that could be really amazing to know from folks as well.

So we’re gonna dive a little bit deeper into reflexion.

This could easily be its own topic as well. It’s another great paper on prompting.

So the interesting thing about reflexion. This is again a paper that came out some time back you know, in 2023 and it sort of builds off of ReAct and a few of the other sort of like well known papers in the space that try to get agents to use tools. They have also called a number of components. Here you have the actor evaluator, but the main one that. They wanna that they’re kind of calling out is self reflexion, and then memory, which you can kind of think of that state.

And so, and and you know we’ll kind of go into an example of how that works as well. So I have some example logs from the reflexion run. So you folks can kind of see, you know how that works practically. But the idea here is that sort of it’s kind of similar to ReAct, and that, you know, don’t just take an action right away, think about, you know, basically generate some sort of thought of like, What do I want to go do next? And then self reflexion says, Hey, what do I know already about the context that I’ve been provided to try to go figure out what to do next.

And the main and and yeah, I think, like some of the pros here, it really does feel a lot more human like, especially because of the data set that we’re gonna go through.

It’s less I think, less interesting on like multi-hop question answering more interesting on problem solving. So so this is more kind of like chaining problems together to accomplish the task. And then, yeah, continuously improving itself by, you know, basically, this, this sort of self, reinforcing cycle, of creating an action, and then and then going back and reflexing on it. Anything else to add here, SallyAnn on reflexion.

### What is Reflexion?

**SallyAnn DeLucia:** No, I would really just tie back to what we send in the beginning about like the mimicking of human intelligence. And I think the key thing here is like, you know, humans make mistakes right? And what do we do when we don’t get something right? We kind of reflect on it. And then we take a new approach. And that’s what it’s doing is, you know, it’s taking an initial go at the problem. If it’s not quite right, it’s looking at that and kind of recalibrating and taking another go at it. So I think it’s kind of expanding on that concept a lot which I think is why it’s so powerful.


![Reflexion](https://arize.com/wp-content/uploads/2024/04/Screenshot-2024-04-26-at-12.05.31 PM-1024x578.png)



**Aman Khan:** Totally, and then and then great points on like evaluation. Evaluation is a core component here. So once the action is taken, go back and assess if they make the right action. Something we think about a lot of humans as well like, did I do the right thing? What can I learn from this, right? Sometimes it keeps us up at night: oh what about that thing I did?

**SallyAnn DeLucia: **Relatable

**Aman Khan:** Yeah, exactly. Yeah.

LLMs have feelings, too. If you program them to, but so complex evaluation I think. So this actually adds a fair amount of open-ended complexity to the LLM call that you’re making. And by that I mean you know, it’s actually pretty tough to evaluate an action. The LLM is basically performing that same action again, of like, did I do the right thing? It’s going to go back and reflect on that. And I think, what’s kind of interesting.

And I’d like to go a little bit further into reflexion to prove this, but it does seem like like that can sometimes cause the prompt to like break, or that the LLM, the response that break at times, because you know, it ends up almost looking like recursive logic. It sort of gets stuck into like, you know, self reflection, evaluation. And then, you’re trying to get it to take an action message, maybe, but it kind of gets into like decision paralysis at times, which is kind of interesting to think about.

So, let’s make it a little bit more tangible. The paper and Github repo is open source.

[There is a great blog post ](https://nanothoughts.substack.com/p/reflecting-on-reflexion)that the author on the paper put out that makes it super readable. 

And again, you can kind of see, hey? This is how reflexion performs on Hotspot QA. And then also Alf World. And so we’ll actually talk a little bit about Alf World, and I’ll drop this paper as well.

Okay. Awesome. It’s already there.

So Alf World is this interesting data set which it’s kinda it’s kind of just easier to read about. I think I’ve got it up here.

So it’s this interesting data set, which contains an interactive text world environment, which means it’s kind of like an escape room. Is how I would think about it. And if you go through we can read a little bit of it. It’s not gonna be super readable. I apologize, but I’ll try and read out some of this. But it’s like you’re in the middle of a room. Looking around, you see these things, a cabinet, a cabinet counter top. So it’s kind of describing an environment.

And it says, Okay, now, you know, figure out, you know these are these are the things around you. I need you to perform some action. I need you to clean this with that. And so it’s kind of like this, like a narrative script of you pre, you know, make some observations and perform an action. And you’re trying to basically get the LLM to, you know, kind of like old style Rpg games. Respond with text of what to do next.

You kind of wanted to make it work its way out of this world, and not actually. But more, you know, take some action in the environment that it’s allowed to take, and if it does that it gets a reward, and it gets kind of the next kind of piece of the puzzle here to go and solve. So that’s how the main dataset calls out, they have the hop off QA runs. I just think the outfold ones are kind of interesting, and where self reflection really shines.

So any questions, or I guess any thoughts on that one SallyAnn?

**SallyAnn DeLucia: **No, I think the only thing we call it is this one is one of the decision making data sets that they also use and ReAct. So it’s kind of cool to kind of see it being used here. It’s a little bit of that, like one to one kind of comparison.

**Aman Khan:** Totally. Yeah. And it’s interesting. Because, like again, HotpotQA, multi hop questions go figure out an answer, use a tool or the equivalent of like a tool. Go figure it out. You know what you need to to actually perform an action. OutWorld has a little bit of that. But out world is primarily in this data set, mostly focuses on, you know, making observations about an environment to kind of almost like narratively. Try and solve its way through so you know, for the agent to solve its way through it. 

So really, really interesting. I think. You know, main takeaways. Here is what reflexion does seem to perform quite well on OutWorld.

And then they actually also call out ReAct plus reflexion. Significantly, outperforms ReAct by completing 130 out of the 134 tasks. So what’s interesting is the success rate on OutWorld goes up significantly when using self reflexion. So I thought that was kind of interesting, like, you know, ReAct is great at that. What should I do next? And take action.

Alf World is given the context I have. What’s the right next action to take? So it’s sort of like these prompting techniques kind of play off of each other as well.

**SallyAnn DeLucia:** Yeah. And I think it is just a call just to kind of put it in. You said it was something that they got.

**Aman Khan:** 134, I mean, pretty high number of yeah tasks. I think it performed correctly 130 out of 134.

**SallyAnn DeLucia:** Yeah, it was in like the fifties range for ReAct alone. So just kind of giving that kind of comparison of it definitely improves it, but not by a small amount. Like we’re talking a large large amount.

**Aman Khan: **Yeah. One note is that the technique does involve what’s called  trial numbers. Which you do. It does allow, like this data set kind of allows the LLM to kind of go back into a loop as well. So it kind of gets to see and learn from the environment itself as well. So those are what the trials look like. So you can. So that’s how this data set is sort of like, based on the number of trials. So it kind of learns about the world through each trial. So you can see the success of the number of trials going up. They score it up to 10 in the logs. Over here, so you can actually see this is what the code looks like when the output log looks like, which is.

I’ll try and zoom in here to make it a little bit more readable. But it’s basically looking at, based on the first scene, the first environment. Did it succeed? Yes, or not?

And then you’ll see the memory about the environment, too.

“In this environment. My plan was to find the plate, then clean it with the sync basin that put it on the countertop, however, I forgot to put the plate in or on the countertop after cleaning it. I should have gone to this. So it’s sort of similar. It’s like this inner monologue in there. You know. Narration of like: Well, I should have done this better.

And then, as you go further, you know, you actually have the run logs here.

It does get to run through that environment multiple times, which is what gets it to successively improve. So it kind of gets to learn from itself over time. It’s like I’ve seen this scenario before. So you’re kind of answering from like your parametric, it’s the non parametric. But like context memory as opposed to you know, having to solve it from like a zero-shot from the get go.

**SallyAnn DeLucia: **Super cool. I really love when they include the repo, like they did with this paper here. So we could actually dig into those logs.

**Aman Khan: **Yeah, totally. I unfortunately couldn’t get a nice notebook up and running right before this. If someone else manages to do that, please do feel free to share it in community would love to take a look. I have it running kind of locally. But again, pretty straightforward code examples. Here, you’re basically just defining. I think this is okay, yeah. So this is sort of a another, a few shot example of what the output looks like. 

So it’s you know, you’re in the middle of room. These are what you see, and it says: okay. To solve this task, I need to find and take a mug, then put it on the coffee machine. Okay. Then it looks around. Then it says, Okay, here’s the next part of the environment. Okay. And so it kind of just keeps working through. And that way, but yeah, pretty straightforward you know, in terms of implementation.

I didn’t see an example of the available agents. Types include ReAct and reflexion strategies. So you can kind of combine the two in the code example as well. So you kinda get you kind of get an agent that works out of the box with ReAct and reflexion.

Awesome.

We do have a couple more, but I just wanted to kind of you know, I feel like these were kind of the two main main datasets. And then do we want to kind of briefly touch on chain of thought, and then we can come back in a future paper read?

**SallyAnn DeLucia: **Totally. Yeah, like, let us know folks. If you want to see more on reflexion, we can even have that coding example. Let us know we can follow up. 

But yeah, the other one I just want to call out was chain of thought because it is used in the paper and just to make sure that everyone understands how that works. And so basically, it prompts the elements to verbalize it’s intermediate intermediate reasoning. If you remember from that first example from the beginning, when we had all of them up, you could see that the thought process was there.

So it definitely helps with the model handling like any multi step reasoning but it then also makes it more transparent, similar to ReAct just so that we can kind of see that log. But again, we do have that fact hallucination problem, because, still relying only on the models. Internal knowledge which can lead to, you know, hallucination. So that’s kind of where the ReAct has that step above because of the actions we’re bringing in that external info. So calling that out there, ReAct doesn’t interact with external. But one thing that’s important is, it actually uses a slight variation of chain of thought in the papers.

I’m blanking on the word but basically the idea here is, it has those multiple reasoning paths, and then it uses this kind of like consensus, like approach to determine the most likely correct answer. So it is slightly different. It has a slight edge above the traditional chain of thought. But that is the actual method that is used to compare in the ReAct paper itself.

**Aman Khan:** I think that’s interesting. Right? That’s like a variation on a fundamental sort of prompting technique. 

**SallyAnn DeLucia: **Totally yeah. And it seems to be pretty powerful based off of some of the results. That I suspect. But yeah, that’s the chain of thought. I think it’s just worthwhile noting how that works.

### Conclusion

**Aman Khan: **Awesome. Well, I hope that this was at least helpful for folks who are maybe just getting started with agents and experimenting with them hopefully, makes them more tractable, easier to understand. And as you can see, the code examples are not super complicated. 

They’re actually pretty easy to pick up once you take a look at the Github repo you don’t need to use, you know, too many like complex abstractions, and you’ll be able to like. Understand the code more deeply if you’re seeing it yourself. And a lot of it just comes down to stringing these prompting techniques together. And of course tweaking the prompts for your use case. That’s sort of that’s my takeaway, at least for this, I guess. Anything more to add, there, SallyAnn?

**SallyAnn DeLucia:** No, I think you hit on everything and my main ones, too, was like it’s a combination of efforts to get that on really what you want, which is, I’m sure you’ve experienced. I’ve experienced that definitely to be the case. Yeah, thanks. Everyone.

**Aman Khan:** Yeah. And we I, this one was really fun. So if folks want to see more of this type of paper read please do let us know. Would love to kind of come back, and maybe cover reflexion or chain of thoughts, consistency, more depth as well, or some of the other more emerging prompting techniques.

**SallyAnn DeLucia:** Totally. It feels like new ones every day.

**Aman Khan:** Cool thanks everyone. 

**SallyAnn DeLucia:** Bye.
