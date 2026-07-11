---
title: 'DSPy Assertions: Computational Constraints for Self-Refining Language Model
  Pipelines'
topic: prompt-engineering
subtopic: techniques
secondary_topics:
- evals-observability/evaluation
summary: Explains DSPy assertions as computational constraints for self-refining language-model
  pipelines.
source: arize
url: https://arize.com/blog/dspy-assertions-computational-constraints/
author: Sarah Welsh
published: '2024-07-24'
fetched: '2026-07-11T04:49:10Z'
classifier: codex
taxonomy_rev: 1
words: 5896
content_sha256: bc056f234e5b7004b3f0fb6b2335e0df3e932f40af3ca614fc260f9df9d96673
---

# DSPy Assertions: Computational Constraints for Self-Refining Language Model Pipelines

![CPR DSPY Assertions Blog Dat Ngo, Cyrus Nouroozi, and SallyAnn Delucia headshots.](https://arize.com/wp-content/uploads/2024/07/CPR-DSPY-Assertions-Blog-1021x560.jpg)

              # DSPy Assertions: Computational Constraints for Self-Refining Language Model Pipelines

## Introduction

Chaining language model (LM) calls as composable modules is fueling a new way of programming, but ensuring LMs adhere to important constraints requires heuristic “prompt engineering.” The paper this week introduces LM Assertions, a programming construct for expressing computational constraints that LMs should satisfy. The researchers integrated their constructs into the recent DSPy programming model for LMs and present new strategies that allow DSPy to compile programs with LM Assertions into more reliable and accurate systems. They also propose strategies to use assertions at inference time for automatic self-refinement with LMs. They reported on four diverse case studies for text generation and found that LM Assertions improve not only compliance with imposed rules but also downstream task performance, passing constraints up to 164% more often and generating up to 37% more higher-quality responses.

This week we have Cyrus Nouroozi–a DSPy key contributor–with us to answer questions and break down LM assertions.

## Watch

## Listen

## Dive in

## Analysis

### DSPy in a Nutshell


**Dat Ngo: **Welcome to this week’s paper reading here at Arize.

While folks come into the room, we might start with some introductions. So my name is Dat. I’m a solutions architect here at Arize. I build a lot with our customers. I brought some very special guests with us here today, SallyAnn, if you want to introduce yourself.

**SallyAnn DeLucia: **Yeah, hey, everyone. I’m SallyAnn. I’m a product manager here at Arize. I work on a lot of our products. But most recently I worked on our Copilot feature. If you haven’t checked it out definitely, go do that and then we also have Cyrus with us.

**Cyrus Nouroozi:** Hey, everybody! I’m Cyrus. I am a core contributor at DSPyy. And with another one of the core contributors who’s a good friend of mine. We started a startup called ZenBase to commercialize its technology.

![DSPy in a nutshell](https://arize.com/wp-content/uploads/2024/07/DSPy-in-a-Nutshell-1024x571.png)

**Dat Ngo:** Awesome thanks. And so, yeah, the reason I brought SallyAnn and Cyrus is because I don’t really know much about DSPy, so I thought I’d bring them on here to to educate our audience and our users on DSPy, and why it’s so amazing

I did get a chance to listen to Omar Khattab’s talk recently here in San Francisco. Amazing talk. So you know, thought it’d be great to bring one of the heavy hitters.

So to get us started, I think for the agenda today, we’re really just gonna do an intro into DSPy. I think, for a lot of folks like myself and others who’ve never really heard of it or used it. You kind of really want to understand why do people like it? Why is it, you know? How is it so different from maybe some of the other frameworks?

We’ll go into things like assertions inside of DSPy, so some of the moving parts really kind of what makes DSPy unique is, maybe it’s optimizers which Cyrus and SallyAnn will go into in depth. And then we actually have a coded up example.

At the end that we’ll walk through just to give people really a feel and the intuition for the framework and really to get us off to get us started.

Maybe I just wanna talk a little bit about my journey, kind of trying to understand the framework. And if I had to really describe DSPy in a nutshell, and I and I could be completely wrong here. So Cyrus and SallyAnn correct me.

The way I described is you’re really telling DSPy not how to do something, but like what you want.

And it’s very different than how we do prompt engineering today. So, SallyAnn will go into the motivation, but if I had to break it down…

Step One: You really define what you want it to do. So in DSPy I think they’re called signatures. This is like the shorthand for signatures. It’s like you basically describe three things. What’s the input of this task or thing you want it to do? What’s the output look like? And then maybe a small description. So it’s basically, hey, what’s the task you needed to do?

And then maybe Step 2 is like, you collect a very small amount of examples of what that looks like. What are good versions of, you know. Input output and kind of examples from your real world of the task that maybe you want it to look like.

Step 3. And then you construct. And this is the part I don’t know super well, but you construct your pipeline using modules or DSPy Layers. And it’s really kind of like building a pipeline to get the thing that you want. I think we’ll go into depth on that later.

Step 4, DSPy optimizes your prompt and generates your final text from all the examples. And your pipeline.

For me, I guess. Starting, I think, running the minimal viable example in colab was really a great place to start. So we’ll post the GitHub link in kind of the chat here, and then, you know, to be very honest while we’re looking at the paper.

It was a little dense for me really to get a feel for what’s happening. I kind of have to do something to understand it. I really thought the docs were really great to kind of get started. So that minimal kind of working example was here in the quick start.

So just as a heads up for me. That was a really great way to kind to get started here. And so next we’ll go on kind of the motivation, but just wanted to give a quick DSPy in a nutshell.

**Cyrus Nouroozi: **Can I jump in on the nutshell part? If you are coming from an ML background, and you’re used to something like Pytorch or TensorFlow where you create modules, you say how you’re gonna do the math. But when you initialize it, it’s got all these random weights. And DSPy is kind of like that.

You create these modules. You create your transformations. Initially, there’s these basic prompts. And just like you would in Pytorch with an optimizer like Atom or Sgdr, DSPy has its own optimizers that will go through and optimize the prompts to minimize your loss, or rather DSPy calls it maximize your metric in your training set so point number 2, you can think of as your training set. There’s a testing set, too. And like Dat said, the whole goal here is to be more explicit about what you want and not have to worry about how it’s exactly done, and let the computer optimize that for you.

**Dat Ngo:** Awesome.

Yeah, I think going into the motivation, and maybe why you should learn DSPy, SallyAnn?


**Motivation for DSPy Assertions**


![DSPy Motivation](https://arize.com/wp-content/uploads/2024/07/DSPy-Motivation-1024x569.png)


**SallyAnn DeLucia: **Yeah. So DSPy was a great framework. It kind of had all those modules that Dat was just describing, and Cyrus just describing. But there, there was kind of this need to control and refine the LLM output. So they created this way so that you didn’t need to do all this prompt engineering. You could just use these composable modules and automatic optimizers, that was great. But there was no way to actually control the outputs.

So that was kind of the main motivation. There were no tools that you could set the specific rules for the LLM behavior could kinda just set your intention, or what you wanted the LLM output to be and they also felt that there was a need for help in debugging and improving the responses. So taking the example of the multi hop question answering data set. If you’re not familiar with what that is, essentially, it’s a data set where it requires the LMor the task to gather information from multiple sources and do this multistep reasoning.

And so even looking at that task there. The task is to do these complex question answering. But there’s long and imprecise queries. There was redundant information, retrieval, and so these were kind of some of the challenges that the team wanted to use assertions for to kind of overcome.

So that’s kind of the high level motivation. I don’t know Cyrus, any anything else you would add there for that?

**Cyrus Nouroozi: **Yeah, I would add that like, when you have a pipeline of language model calls there are checks and balances you wanna have at different stages.

Before this paper, you would have to run through the whole pipeline and then get to the final result at the end. And you couldn’t really implement those checks and balances in between, let alone have those checks and balances optimize the prompt, and loop back into what prompt is used to maximize the metric in the pipeline.

So you know, asserts and suggestions let us give hard and soft constraints of sorts to the language model, and this way we can sort of nudge it along in the individual steps of the pipeline.

**Dat Ngo:** Yeah. And then one thing I’d like to add to is like for folks who maybe like used to

If folks on the call have ever done like prompt engineering. Right? What you’re kind of doing is like, you’re manually crafting your like saying, kind of like, this is what I want you to do and how to do it. It’s probably the most common approach when you think about other frameworks. Right? You’re just like saying, Hey, here’s the prompt. Go do this. You might chain together some modules.

I think maybe the take is, if you’ve done a lot of this, you kind of notice. Maybe if you change a model, or you mess something up, or you have conflicting kind of sentences in your prompts engineering, or maybe sets of prompts. It doesn’t feel as robust. It kind of feels like it would break, and it’s very fragile. And I really think this paradigm shift of like–what if we made this more robust rather than like, you know, more like less brittle? How do we make this less brittle and more scalable to changes? I think, is a really good motivation, too, for folks who feel like there needs to be a little bit more engineering rigor around LLMs.

**Cyrus Nouroozi: **That’s very true. And another analogy I can draw that might help people out is, if you think of prompts as assembly and language models as CPUs, then you know that, like every type of CPU or different architectures, instruction sets have different assemblies that have you have to use to get the maximum performance out of it.

Similarly, like one prompt that might work really well for GPT-4 may not work that good for Sonnet 3.5. And so what did we do in programming? There are still people that write assembly, but we now have higher level languages that we code in. And then we have the computer figure out how to execute that on the CPU.

DSPy is offering a similar level of abstraction.

Instead of focusing on the prompts themselves, and how do you craft the precise best prompt for the specific model that you’re running it on. You let the DSPy optimizers handle that for you. And you just focus on the High Level program logic.

**Dat Ngo: **Yup, exactly.

**SallyAnn DeLucia:** We actually have a good question, I think, in the QA. To kind of clarify how DSPy works. So the question here is asking if this is like some kind of supervised learning where we’re taking the input and output. Do you wanna add some more color to like what’s actually happening in DSPy when we’re defining the what and not the how.

**Cyrus Nouroozi: **Sure. So this is Vignesh’s question in the QA. And DSPy does support supervised learning. If you have the inputs and outputs for the entire pipeline that works great. But you can also use DSPy without the outputs. So long as the final output passes, your metric function passes a certain threshold in the metric function. Then DSPy will consider that as a successful case, a path, you know a pass, so you could use DSPy in both a supervised and an unsupervised sort of way.

**Dat Ngo: **Awesome. I’m gonna hand over the sharing over to Cyrus so he can walk us through. We have the expert here. So folks in the audience. Please ask all your questions while you can.

**How to use DSPy Assertions**

**Cyrus Nouroozi:** Sweet. So here is a DSPy book on how to use assertions with Tweet generation. I’m using this example because you know, a lot of people have seen tweets. It’s pretty straightforward, and after doing all the setup here, you know all the imports, you import the right things from you. Set up the right things in DSPy, and you set up your data, set your train set and your dev set.

So let’s look at what it’s like to create a basic pipeline and DSPy. So here we have a tweet generator. So we’ve got our first signature that says, Okay, look, if you have a context and a question, we want to generate a query. This is an output field. So you have the input fields, and then you have the output field.

You also have a generate tweet that says, Okay, I’ve got a question, and I’ve got the contacts that may have relevant facts. And now I want you to generate the Tweet. So there you go.

And then we create a little module that has this generate tweet attribute. And in the forward method it’s kind of similar to how you might. In PyTorch we have some logic.

And in this logic it’s going to go ahead and generate some search queries over here, then retrieve relevant passages. So this is kind of like a RAG setup.

And then it’s going to duplicate things over here.

Then it’s going to go ahead and generate a tweet based on the context that it looked up as well as the original question that came in.

Now, how would you go ahead and evaluate something like this. Well, you might want to make sure that it has no hashtags. It’s within the length limit.

If there’s this assessment like LLM as judge over here. You wanna make sure it says yes, and whether the correct answer is also been mentioned. Some other metrics here. So metrics are numbers, and DSPy is trying to maximize the metrics. So here sometimes we’re gonna go ahead and convert booleans to integers, just to make our life easier. So some more metrics here within the length.

There you go.

There’s this overall metric so DSPy optimizes one overall metric for the whole pipeline and the way you can handle compound metrics. In this case we have a bunch of things we wanted to check is you can turn them into integers and sum them, and then maybe divide by 5, because there’s 5 of them. So you can do something like that this way, if it is correct and engaging and faithful, and there are no hashtags, and it’s within the length limit. Then this is going to be 5 5, divided by 5 is one. Perfect score.

If any of these is false, then the score is going to be lower than one.

So let’s take a look at what it’s like to have an example and generate a Tweet, and it does that over there. What happens with assertions of the paper that we’re looking at today is DSPy. With assertions. Some of those metrics that we were checking at the very end of the pipeline and move them into the logic, so that as it is generating the as the intermediate steps are running, then we can offer soft and hard nudges or hard constraints, and also soft nudges to the system.

So, for example, here we have DSPY dot suggest, which suggests that it should not have hashtags. And you tell the prompt optimizer: hey, please revise the tweet to remove hashtags.

Here’s another suggestion within the length limit. Suggestion having the correct answer.

And suggestions are these soft nudges. They won’t fail the entire run. They won’t fail the entire pipeline. But they just suggest to the prompt optimizer that this is how you ought to adjust your prompt so that you can come out with the right output.

Then you can compile it with assertions. So this is actually, this is a great place to explain. What what does compilation mean in the context of DSPy? Coming from an Ml background, a teleprompter or an optimizer. Here is your analog to Sgdr or atom and Bootstrap fusion with random search is our optimizer here you can pass it. The metric that you’re trying to optimize. You have some hyper params that you can pass through, and then you can compile a student module on the train set and the validation set.

So how does something like Bootstrap with few shot with random search work?

The first thing you need to understand is that language models are in context learners, so the more examples you give the better. It’s gonna perform at the task that you wanted to. And so the few shot family of optimizers are trying to figure out what are the best few shot examples to include in the prompt.

**Dat Ngo: **Real, real quick, Cyrus. We had a question in the chat.

Raymond asked: Is there a reason you aren’t asserting the length limit versus suggesting? Which is a good question.

**Cyrus Nouroozi: **That’s a good point. Honestly, I think this cookbook should be updated to use assert on the length limit.

Nice catch.

**Dat Ngo:** Then my question on top of Raymond’s is how do you know when you should do an assertion versus a suggestion? And what’s your thinking around that?

**Cyrus Nouroozi**: Hmm, okay.

There was another example here in the there’s another example in the DSPy repo, where they have both assertions and suggestions. And the example was like RAG with citations.

And so there was a suggestion that every one to two sentences ought to have a citation. That shouldn’t be a hard requirement. That’s a soft, soft requirement.

There should be some citation there. Whereas an assertion, you know, in this Tweet example is, it can’t be longer than 280 characters. It’s a very hard constraint. Suggestions are nudges. Assertions are hard constraints that’ll fail everything.

So, depending on the problem you’re dealing with. Like, for example, an assertion could be: Do not use profanity with the user or something like that.

**Dat Ngo: **Gotcha.

**Cyrus Nouroozi: **And then…back to few shot with random search. So let’s look at Bootstrap few shot with random search. We learned what Few shot meant here, which is like, how do we find the best examples?

And then random search says, Okay, we’re going to be randomly sampling from the examples that are there, and then putting them into the prompt to see which ones make sense. And then the Bootstrap side, the what the what Bootstrap means here is it means that maybe you don’t initially have the output label. So somebody asked about supervised versus unsupervised learning. Maybe you don’t have the initial output labels, and you probably don’t have the input and output values of the intermediate steps in your pipeline.

And so what bootstrap few Bootstrap will do is it will run your pipeline end to end, and when there is a successful record, a successful run based on your metric. It’ll go and save the intermediate input and output values for each of the steps and use those and add those to the set of valid few shot examples for those intermediate steps.

And so this Bootstrap few shot does a bunch of things. Really, it’s trying to at the high level, figure out the best few shot examples to include at every step of the pipeline.

And Raymond, you’re asking if there’s a way to give a starting prompt to the bootstrap.

There is not. All of DSPy is like: you don’t have to worry about it. But if you wanted to include something like that and nudge the L. You know. Nudge the Llm. In the right direction. Then you can in your signatures over here as the Doc string. You can put a starting prompt of sorts like this. This is where you can put your best knowledge into it so that it’s not starting from scratch.

And that’s it for the example. This was a whirlwind tour of an example. I’m sure there may be questions around this.

But I would encourage anybody to go into the DSPy docs check out some of the examples that are around. And if you’d like to, if you have any questions. You can hit me up on Twitter or Linkedin.


### DSPy Assertions

![Text overview of Assertions](https://arize.com/wp-content/uploads/2024/07/Assertions-Slide-1024x573.png)


**SallyAnn DeLucia:** I think it would be helpful for us to take maybe a step back kind of go over the different types of insertions and optimizers. And then maybe we can answer some of these questions that we have in the chat.

Alright. So so I just walked us through a great example of how to kind of implement with DSPy. Use these assertions in your pipeline, but I think it’s worthwhile for us just to kind of outline what even an assertion is so it is a way for you to do this user. Confine constraints on those outputs. So you gave the example of like length limits. You can say, you know, only implement with this length, or don’t use profanity. Those are all types of assertions. And the goal really here is to enhance the predictability and correctness.

I think those are two things that are a little bit hard to kind of get down when you’re dealing with these LLMs, just because there’s so many variables here that we’re dealing with. So this really helps you know, enhance those two things.

And you talked about this, Cyrus. There are two types of assertions. So you have these kinds of hard assertions. Those are actually the assertions, and these are, gonna be strict, and they halt the pipeline if repeatedly violated. So once you set your assertion like for the response length one, the idea here is that we’re kind of retrying a certain amount of times, and if it continues to violate the assertion, the pipeline fails. It will not move forward to the next step. I think that’s something really important to kind of understand here.

And then there’s the more soft kind of assertions suggestion where it’s like, we’re gonna guide towards a desired output. But we’re not gonna fail the pipeline. If we repeatedly violate this.

So this is just a little excerpt from the paper here. I think the ones that you gave Cyrus were great, but I did just wanna call out that kind of idea of exactly what an assertion is.

And the two types here. Anything that you would add to this, Cyrus?

**Cyrus Nouroozi:** No, I think you did a great job.

![Text overview of Optimizers](https://arize.com/wp-content/uploads/2024/07/OPTIMIZERS-1024x570.png)


**SallyAnn DeLucia:** Alright awesome. And then the other thing you talked about were optimizers, and I think these are really cool, and I think we have some questions about these in the chat, but the paper itself calls out these 3 types. I know there’s a a variety of other kind of optimizers that DSPy. Has, but I I think these are the ones that are relevant to be, you know, assertions.

So the first one is the assertion-driven backtracking.

And so I think the Tldr; here is that it enables retry and self refinement. So here we’re gonna use that certain suggest to retry in this special state. So we’re gonna process the current error state in the message. And we return to this basically new state. And so we’ll kind of continue and retry with these updated prompts, we’re including the past failure outputs and instructions. And then, basically, once that retry limit is met, we’re either going to halt for those asserts, or move to the next module for suggest.

So this is kind of that process we are describing on that last date of you know whether or not we’re going to move forward or not. And we’re just kind of using those kind of states to kind of go between based off the type of assertion being used.

The second one is assertion, driven example, bootstrapping. So this is gonna be optimizing the prompt.

And so what we’re doing here is we have this teacher, student model approach, which I think is really interesting.

And so the teacher model bootstraps examples from the student model. And then we’re using that backtracking to ensure the correct intermediate output. So if I’m understanding this correctly, it kind of goes back to that first type of optimization where we’re doing the backtrack to make sure we’re checking our assertions or suggestion to make sure our outputs are correct.

And then that just makes sure that we’re meeting those kind of enhanced quality constraints.

Last one here the counter example bootstrapping this guides models away from making mistakes.

So it’s gonna collect traces of failed assertions during backtracking, and then use those examples as demonstrations. So you kind of think of this almost as few shot prompting in a way where we’re giving examples of what not to do, actually, rather than examples of what to do.

So yeah, I just wanted to call out these here. I think it’s important to kind of understand the differences here.

And then, yeah, maybe we could take some questions from the audience.


**DSPy Q & A **

**Question: Is there a UI for DSPy? **

**Cyrus Nouroozi:** As far as I know, there isn’t one. But there is somebody named Tom Doer, who is experimenting with one. I’ve been seeing him tweet about it over the last week. So I would reach out to him  on Twitter and go through his tweets for that. But currently No.


**Question: Can DSPy be integrated into agent frameworks like AutoGen? **

**Cyrus Nouroozi: **I’m gonna send the answer here as well. But Tldr is that  DPSy is more around pipelines of LLM function calls and an agentic use case where the agent is deciding the control flow. You could use DSPy for it as well. There’s a react agent in DSPy, for example.

But there’s a lot more work to be done on that front. We’re actually gonna be working with Omar on figuring out how to optimize agents in a more robust way. We’ve got a kick off for that on Saturday.

I would say that agents are definitely supported in some capacity, but not like a not like a 1st class. Robust thing right now, and we are working on that


**Question: Is DSPy Similar to Text Grad? **

**Cyrus Nouroozi: **So for those who may or may not. Have heard of text grad. It is a paper that also came out of Stanford a couple of weeks ago, and what Text Grad does is…it uses an LLM to look at the response and be like, Okay, now that you know, you responded this way and maybe this was the score, or whatever, LLM can you suggest how we might update the original prompt so that it gets better. So you’re using the LLM to generate a textual gradient, they call it.

And this the idea is that like, if you have a metric mountainscape, as I like to call it. Maybe I can share my screen to show this, to show this thing.can everybody see this?

![](https://arize.com/wp-content/uploads/2024/07/Flipped-Version-Loss-Landscape-Screen-Share-1024x611.png)

Okay. Awesome. If you’re coming from an ML background. This is a flipped version of a Loss Landscape. But really, you can imagine there’s a search space over here of possible prompts.

And these hills represent, you know, the metric you have, and there’s a big hill at the top that you’re gonna have the best result on your metric, because you have the best prompt.

And this is like a local maximum over here.

And so from my understanding of Text Grad, you know, it might start the prompt somewhere over like here, and then it’ll do some hill climbing to eventually get you to here. But if Text Grad starts over here, it’s hill climbing will get you over here, and then it won’t get you over there.

DSPy approaches it from a from a different perspective. DSPy is like, I want to be able to provide some guarantees on finding the global maximum. So with the Bootstrap few shot with random search, it’s actually gonna be testing the whole search space, because it’s gonna be testing, you know, which few shot examples can be used and are the best, and in what order

There are more advanced DSPy. Optimizers that will also do instruction tuning. So there’s the instruction you give to the LLM, and then there’s the examples. And then the spies, more advanced optimizers like me pro v. 2. They will also tune the instruction in a way that is trying to find these higher parts, but I think it’s a deeper dive. Check it out if you’re really curious to dive into the deep end. But it’s a bit of a deep rabbit hole for us to get into now.

So, DSPy is similar to Text Grad. Both trying to be like a PyTorch for LLMs, slightly different approaches to it and addressing similar challenges.


**Question: How does DSPy optimize what gets nudged or guided?**

**Cyrus Nouroozi: **It’s not. It’s not doing the individual token probability distribution. Because some LLM providers give us that some don’t. You know, you can’t play too much with OpenAI’s LLM probability distribution. But if I’m correct, I think it’s the assertions. One is about actually modifying the prompt. So it’s going through a discrete search space of prompts with that little example that I was showing earlier. And it’s testing out all those different different candidates on your behalf, and then reporting back to you which one is the best anonymous attendee.


**Question: Is there any code example with agents and to impose the appropriate choice of agents and proper handshaking agents?**

Okay, this is a deep question. Great question, Brenda. You’re also hinting at multi agent systems here and there is an example of DSPy, where you sort of do a mixture of agents like you have some question come in, you have like five agents answer and then you have one step at the end that synthesizes everything. So you can do that, but in that flow the agents are guaranteed to terminate at some point.

They’re not like very open-ended in terms of imposing the appropriate choice, I think you can do that actually, like you could create a DSPy signature that says, Okay, like: which agent do I route this to? And then route to that agent. And then that agent, being like a DSPy react agent, can like handle that task and using DSPy optimizers, it would go and actually optimize the prompt on both of those modules and all the other agents as well, and any other modules you may have in that system. So I think that that is a really interesting question. And I think you should be able to do some of that with DSPy.


**Question: Can DSPy be used with LoRA Fine tuning?**

**Cyrus Nouroozi: **Yes, so DSPy has series of optimizers. One of those optimizers is a fine tuner. I’m I don’t think it’s doing Laura fine tunes at the moment, but there’s really no reason why, there couldn’t be a DSPy LoRA fine tuning optimizer that would go and do fine tuning for you like you noted. And actually, an extension of your question. Brenda is like, you know, there are so many different ways that we can guide LLMs There’s the prompt. There’s fine tuning, there’s also now some interesting work being done on control vectors. And you know the promise of DSPy is that as the developer or as the scientists or as the engineer, you can write your program without defining how it gets optimized, and then later, bring in an optimizer. And we can figure that out for you.

So you could one day have a control vector optimizer. You could have a fine tune optimizer. You have bootstrap few shot. You have all these optimizers they can use for your problem.

**How is DSPy different from LLM compiler?**

Okay, I’m opening up LLM Compiler right now to take a look at it. As it’s loading on my Internet.

I am quite literally just looking at the GitHubRead me. I have come across this paper before.

And I think that…okay, so LLM compiler is a bit more like going literally off of this diagram in the paper. You have a planner. You have a task fetching unit that figures out presumably like dependencies between tasks and what needs to get executed before. Now you have. This executor, which is like executing the current thing to do. And then these function calling units may interact with some tools.

And so I would say that this is sort of like. This is an architecture of a system that uses language models for both this executor piece. Maybe this task fetching you and definitely the LLM Planner, and you could recreate this architecture in DSPy. And then optimize the prompts at the various stages of this.

They’re not the same. Rather this is an architecture of a compound AI system, which is a great thing. If you want to deal with complex tasks, compound AI systems are what to do.

And DSPy can help you create architectures like this or other ones. And then, instead of you focusing on optimizing or or like fiddling and prompt engineering, or I call it prompt fiddling, prompt fiddling the different prompts in the pipeline. You can have DSPy do something like that for you.

### Conclusion

**Dat Ngo:** Awesome. Thank you so much. A big shout out to our friend, Cyrus, for joining us on this paper.

**Cyrus Nouroozi: **Of course.

**Dat Ngo:** He is a great friend and a great person. SallyAnn, thank you so much for joining, too.

On the product side of Arize before we hop. I just wanted to give a quick plug.

We’ve had a lot of releases inside of our open source offering called, Arize Phoenix. If you have some time tomorrow you can see the newest features that have dropped in our open source offering in Arize, Phoenix. ([Catch the recording of our Town Hall where we overview new Phoenix features here](https://www.youtube.com/watch?v=f-a3X0e508I))

So thank you so much everyone big shout out to Cyrus and SallyAnn for joining us this week on the paper reading.

**SallyAnn DeLucia: **Awesome. Thanks.

**Cyrus Nouroozi:** Take care folks.
