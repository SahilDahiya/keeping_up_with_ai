---
title: Reinforcement Learning in the Era of LLMs
topic: models
subtopic: fine-tuning
secondary_topics:
- models/reasoning
summary: Explains reinforcement learning concepts in the LLM era and how RL fits into
  model improvement workflows.
source: arize
url: https://arize.com/blog/reinforcement-learning-in-the-era-of-llms/
author: Sarah Welsh
published: '2024-03-15'
fetched: '2026-07-11T04:48:32Z'
classifier: codex
taxonomy_rev: 1
words: 7427
content_sha256: c6022baeafcd3b35d58dbb5161d38ae06971d05520ac3490e092b2f6737185f3
---

# Reinforcement Learning in the Era of LLMs

![Reinforcement Learning in the Era of LLMs - blog Claire Longo and Duncan McKinnon headshots](https://arize.com/wp-content/uploads/2024/03/Reinforcement-Learning-in-the-Era-of-LLMs-blog-1021x560.jpg)

              # Reinforcement Learning in the Era of LLMs

## Introduction

This week, we explore *Reinforcement Learning in the Era of LLMs: What is Essential? What is needed? An RL Perspective on RLHF, Prompting, and Beyond, *with Claire Longo, Arize’s Head of Customer Success and Duncan McKinnon, ML Solutions Engineer at Arize.

Recent advancements in Large Language Models (LLMs) have garnered wide attention and led to successful products such as ChatGPT and GPT-4. Their proficiency in adhering to instructions and delivering harmless, helpful, and honest (3H) responses can largely be attributed to the technique of Reinforcement Learning from Human Feedback (RLHF). This week’s paper aims to link the research in conventional RL to RL techniques used in LLM research and demystify this technique by discussing why, when, and how RL excels.

## Watch

## Dive in

- [Read Reinforcement Learning in the Era of LLMs: What is Essential? What is needed? An RL Perspective on RLHF, Prompting, and Beyond](https://arxiv.org/abs/2310.06147)
- [See more paper readings](https://arize.com/ai-research-papers/)

## Listen

## Transcript

**Introduction**

**Claire Longo:** Hey, everyone welcome. Thank you for joining us for this paper reading. We’ve got myself and Duncan here. We’re going to go through some really exciting math around reinforcement learning applied to LLMs. We’ve got a great paper here that covers that as we talk through this, please drop questions in the chat. We’ll be monitoring that if I can find it in my tabs here. Yep, great. Yeah. So definitely drop questions in the chat and interact with us as we go through this. We love to make this a conversation and interactive. Let’s start with some introductions. 

Hi, I’m Claire Longo, I have a math background. But now I’m working in customer success here at Arize working directly with our customers, which is really fantastic to see what they are all building, and we also have Duncan joining us. Duncan, do you want to give a quick intro?

**Duncan McKinnon: **Yeah, Hi, I’m Duncan. I also work on Claire’s team with the customers here at Arize. I’ve been a software engineer but I started out and then worked in data science for a few years, and ML engineering. So I’ve kind of gone through several different roles, but I’m excited to be here to talk about reinforcement learning with everyone. 

**Claire Longo:** Awesome, really excited to have you here on this call, Duncan because reinforcement learning is something that we’ve talked about a lot internally, it’s personally one of my favorite mathematical models. I’m not sure why, I think it’s just so fascinating the mathematics behind it. I’m going to go ahead and share my screen, and we’ll show the paper that we’re going through. Just kind of set the stage here.

So the way I like to read papers is I’ll go through and mark it up. Some key points really stand out to me. And then Duncan has really pulled out some really important stuff. That we’re gonna talk through with some slides because it’s pretty in depth. Awesome technical details.

But what we’re talking through here is Reinforcement Learning in the Era of LLMs, like I said, reinforcement learning is one of my favorite kind of algorithms here. It’s been around for a long time. I remember learning about it quite a few years ago in school. But now, in this era of LLMs. It’s becoming more important because it’s being applied to LLMs in a way that can really help us apply LLMs to very specific use cases and kinda keep them on the rails.

So what this paper does and the reason we chose it, is it really gives a little bit of an overview of reinforcement learning in the first place, and then it delves into how to apply it to LLMs in the context of RLHF–which is reinforcement learning with human feedback–prompting, and a little bit more so. There were some really cool learnings takeaways that we got from reading this thinking about how to apply reinforcement learning to LLMs.

And I’m just excited to see reinforcement learning really starting to catch on in this context. So before we jump over to the slides that go through this main section. I’ll just kind of scroll through this and show you what this contains.

The first section is kind of reinforcement learning 101. You’ve got some beautiful diagrams that describe it. We’re gonna talk about online and offline RL, so we actually have some slides to break down these more complex concepts. And then, once that’s queued up, then we’re talking about how to actually apply this in the context of reinforcement learning human feedback with LLMs, so the thing that really stood out to me here is LLMs, we know they’re fantastic. They’re large language models. The reinforcement learning helps these large language models adhere to instructions–Duncan, you and I were talking about this–hallucination. Maybe you want to talk us through a little bit about how that hallucination happens, and how we could use something like this to kind of keep that model on the rails and prevent that?

**Duncan McKinnon: **Yeah. So the way that the large language models are trained is more predictive. So they’re trying to predict the next token on an individual basis in the sequence. 

And their feedback mechanism is more based on what you want to hear–they’re trying to give you something that you want to hear. So if you ask it a question, it wants to give you an answer, because that’s going to be preferable to saying that it doesn’t understand, or it doesn’t know something. So it may try and pull together some information to give you a response, because that’s going to give it better feedback from the person who’s judging it.

And what we can use reinforcement learning to do is focus the objective of the language model to be more based on providing truthful answers or penalizing answers that aren’t, that don’t have context or aren’t based on any background.

**Claire Longo: **Yeah, yeah, I love that. I think there’s something here they mentioned a few times like the LLM alignment problem, and that really, really resonated with me because the LLM is a language model. And like you’re saying, it’s kind of optimized to produce sensible and coherent responses, but not always accurate ones. But then, when you can layer some kind of objective function around that, and that’s a super mathie term, but like some kind of mathematically explicit metric that you can optimize for, then you can start to kind of steer these things to do what you actually want beyond just producing helpful language output.

Really cool. Well, Duncan, I’m going to pass it over to you if you want to talk us through the slides, but really go through this first section here. Really kind of reinforcement learning 101, the terminology here, and then how we’re applying it to the LLMs.

**Reinforcement Learning 101**

**Duncan McKinnon: **Yeah, let’s jump into that. 

So we’re going to go all the way back to the basics of what reinforcement learning is doing. And you can formalize it with this Markov decision process.

And the idea here is that the agent in reinforcement learning would be looking at these systems like this, where you have different states that you can be in, you’ll start out with an initial state that could be in chess that could be the starting board of the chessboard where all the pieces are lined up–and then the agent can move from one state to another by choosing action.

So–and this was actually generated by ChatGPT–I was trying to avoid pulling anything off the internet. But it did a really good job. This is what a Markov decision process looks like. It has these 10 states, and it has 5 actions available. There are transitions between these States, and then in between, you see these, the numbers are the reward function or the reward you get for that transition.

So in chess, we could formalize this, as like the starting state is the initial board, and then each action is moving a piece, and the reward function in chess, you want the objective to be to reach checkmate. So to motivate that you could say that, like you get a large reward for entering a State that results in checkmate.

And then this is like the environment in a Markov decision process is the state and reward, and the decisions are the actions and the transitions between states on each step. An important part of reinforcement learning is that it is discrete steps. So you’re going from a state, you’re picking an action, and you’re moving to the next state in discrete steps.

And then the objective in these processes is actually not to get the maximum reward for each step, but to get the maximum cumulative reward, so that nuance kind of requires some exploration of the space to figure out if choosing a different action will lead to a better reward in the long run, rather than picking the action at each step that will lead to the largest reward for that step.

![Markov Decision Process chart](https://arize.com/wp-content/uploads/2024/03/Screenshot-2024-03-15-at-12.27.01 PM-e1710523744522-1024x571.png)

**Claire Longo: **That’s a really good point there that I want to circle back on. The thing that stands out to me with this when you talk me through it is you kind of have, like a little bit of a different mathematical description than you would for machine learning. In machine learning, which we’re all pretty familiar there, you have features, and you have some kind of response that you’re trying to predict. But here the definition is quite different. Where you really have states, actions, and the agent is taking steps to do things you’re trying to maximize that reward. What I really love here is you have that very clear, like reward function that you’re trying to maximize mostly how that kind of pulls into LLMs. 

The thing you mentioned here that was really interesting is, you’ve got your short term reward and your long term reward. So like, there’s actually some cool parallels, I think, in poker, of course, but if you’re playing a lot of poker hands you can think about taking action to maximize a short term reward, like, I just want to win this one hand, or you could step back and look at your long term kind of expected value of playing a ton of hands. And you wanna actually maximize your long term reward there. So, having this kind of mathematical framework can really kind of apply to those gamified situations there.

**Duncan McKinnon:** Yeah. And it’s interesting too, that beyond games this framework can be made to work for a lot of situations, and we’ll go back at the end and show how this actually can be used with an LLM in training to improve the actions that it’s taking. So it’s very generalizable to a lot of different processes, which is really cool.

Going beyond taking that and taking it to the next step of the actual training of the agent.

The agent in reinforcement learning is learning a policy, and that policy is how it approaches decisions in that Markov environment. So like how it goes from one state to what decision it makes to go to the next–that’s called the policy. And it has, like a set of actions at each state that it can choose from, and it can move through the environment in that way.

So, to train a reinforcement learning agent, you go through many different cycles of trials, where it can go through the whole process like for poker, it could play like many different hands, or many different hands until you reach a terminal state. And it’ll go through that many times, and it’ll learn what actions lead to better outcomes and kind of balance that explore, exploit that we talked about earlier.

So like in a lot of situations, once it’s found a good path, for, like the first couple of steps. It will want to keep that path because it leads to better outcomes in the long run.

But every now and then you still wanted to like, deviate from that, to see if there was a better path in those first couple of steps that will lead to longer term rewards. So there’s a lot of balancing and reinforcement learning when you’re training a model between that consistency. And the first like 10 steps versus deviating and seeing if you find something better. And then, after many trials, the agent learns a policy that can generalize to any state, and then you kind of can let it go off into the wild and interact with the environment.

So this is why we have these two different paradigms for online and offline reinforcement learning.

**Claire Longo: **Yeah, I love this. You mentioned something interesting on the explore, exploit. The explore exploit trade off here is really why reinforcement learning is one of my favorite algorithms. What this does is it allows the algorithm to constantly try new things and learn from what it’s doing. So it’s kinda like how we learn as people like–I’m gonna try something. If it didn’t work I might not do that again. If it did work I might repeat the behavior. So it is like the way neural nets kinda model the brain. This kind of algorithm is kind of modeling how humans learn. The thing that makes this so powerful is like when the model is learning, you’re optimizing the kind of optimal, happy path that you’ve learned like, what’s maximizing reward you’re gonna start to like, do that behavior a lot. But then, on the side, you’re also gonna continue to explore. So you don’t just converge to that one kind of happy path that you found, because maybe the environment’s changing and you need to update your happy path. Or maybe that happy path is kind of a local minima, and you’re kind of stuck somewhere that’s like good, but not the best. 

And so by being able to like randomly explore a little bit of percentage of that actions that you’re taking, maybe random or following some kind of like different policy other than the optimal one that helps us like, get new data and adapt to what we’re seeing, which is really what I think makes these things so powerful.

**Duncan McKinnon: **Yeah, I think that’s a really good point about the local minima. That it’s very robust to those types of things like it can get out of a local minima pretty better than a lot of like gradient descent type algorithms. 

**Claire Longo:** I love that often I feel like I as–a human–I’m stuck in a local minima. It’s a great parallel.

**Duncan McKinnon:** Yes. So, the difference between these two online and offline paradigms? It’s kind of subtle so like with the online reinforcement learning, we’re saying that the agent can interact directly with the environment.

And this is something usually seen in situations where it’s like a video game. You know, you can release the agent into the video game. Let it, you know, run the controls based off of the screen. And you’re not too worried that it’s going to run into issues doing that because the environment is kind of isolated.

And then offline reinforcement. Learning is more common in the industry because you’re not allowed to interact with the environment. So like, if you’re training a self-driving car, you’re not gonna put an agent behind the wheel of a car and just like, tell it to learn how to drive, so you have to develop like an offline decision data set to teach the agent how to interact with the environment through a simulation without ever interacting the environment. And once it’s trained, you can use that behavior policy to make decisions in the real environment.

The next thing that the paper goes through is some of the actual paradigms of reinforcement learning to kind of drive towards reinforcement learning from human feedback.

And to get there we have to talk about things like imitation learning. And this is a different approach to reinforcement learning like the offline reinforcement learning problem, where the agent can’t interact with the environment. So we need to have some kind of way of teaching it. What to do when it’s in the real environment without exposing it to that environment.

The other piece of it is that like when you’re teaching an agent to drive, it’s not very clear what the rewards are, or what the reward mechanism should be for driving.

So it’s hard to come up with a reward function to teach the agent which actions to choose when it gets information from the state. It’s not necessarily clear. Or if you’re training an agent to pick something up like you can give it a reward when it picks it up. But how do you get it there? It’s hard to tune a reward function. So, in imitation learning, instead of doing that, you have a human driving. And you use that data set to teach the agent what expert decisions are being taken.

So in this example, the human driver, like an expert, goes through the same course that the agent is exposed to and makes decisions, and then the agent has access to those decisions and uses those to to build its own policy. So it sees what a human is doing. And then it says, oh, I should build a policy that’s similar to that.

And that’s the imitation aspect.

**Claire Longo:** So in this case, it’s kind of learning from example.

**Duncan McKinnon: **Yeah, exactly. 

**Reinforcement Learning vs Machine Learning**

**Claire Longo: **When you think one thing that kind of tripped me up here was like, how is this different from machine learning where we train offline with an example data set. What are your thoughts on that?

**Duncan McKinnon: **Yeah, that’s a good question. I think that like with this mechanism, the agent still has a little bit of leeway to explore. So we can try other actions and see how that cause it’s still passing that action to the environment. It doesn’t need to go off of and totally imitate everything. So there’s still some aspect of that explore, exploit. But for the most part it’s like most of its information is still coming from the driver, so it wants to stay close to that.

So it gives it kind of a head start is the way that I think the paper describes it. You’re giving it a head start so that it has something to go off of, and then it can build its policy through more exploration once it has the basics.

![](https://arize.com/wp-content/uploads/2024/03/Screenshot-2024-03-15-at-12.30.23 PM-1024x578.png)


**Claire Longo:** Oh, that makes so much sense, because it’s still defined as a reinforcement learning problem. So you still have that explore, exploit mathematically. There, that makes a lot of sense. And then there’s something in the paper here about when it’s difficult to define the policy or the reward function. This can allow it to kind of learn that, am I thinking about that right? 

**Duncan McKinnon:** Yeah. So I heard an example about this from a book called *The Alignment Problem*, that was talking about alignment and reinforcement, where you’re trying to align the way that the rewards are designed with the actual behavior that you want to see. Which is actually a pretty hard problem. There’s a lot of ways that you can create a reward function that lead to outcomes that you wouldn’t want–you could train a model that you get a reward interest every time you take a piece based off of the value of that piece, but that doesn’t necessarily lead to checkmate. You could still lose the game pretty easily if you just are basing your reward off of capturing pieces. 

So the problem in the book was learning to fly a model plane and do loops and different aerial maneuvers. And it’s really hard to even get an agent to learn how to take off a plane.

So, going off of that problem, they tried to build reward functions for it and couldn’t do it. And eventually they came to the conclusion that if the only way to get the agent to the level that they needed to get it to was to show it sensor data from a human flying that plane and show it what they wanted it to do up to that point. And then eventually, the agent learned to like, execute these maneuvers far better than the human could.

**Claire Longo:** Yeah, super powerful framework there, because you’re leveraging both learning from example as well as optimizing that reward function with explore, exploit. Alignment Problem–what a great title for a book. Because that’s kind of like the issue with LLMs today is like that alignment problem. 

**Duncan McKinnon: **Yeah, it was before LLMs, but it’s definitely ahead of like, kind of ahead of its time.

So the next logical step from imitation learning is this idea of inverse reinforcement learning. But isn’t that? The author talks about it as a type of imitation learning, but it works in two steps where, instead of basing all of the agent’s decisions–training it off of a decision data set from an expert. You’re training the reward model as like a standard machine learning problem to give rewards based out of the decision data set. So you’re trying to figure out what rewards would have incentive like you could think of it as what rewards would have incentivized that human to execute those behaviors? And how do you capture that in a reward model?

So as somebody’s driving, you know they take a left turn to get to the street that they want to and stay within the lines. The reward function is looking at what incentives were driving the human to make that decision, and try and capture that like if they were trying to stay in the lines. They were trying to go to this street to stay on their path, those types of things. So it’s training the reward model. And then using that reward model to train the agent directly.

**Claire Longo:** Interesting, whereas the more traditional RL model is actually optimizing directly the actions to drive the reward? 

**Duncan McKinnon:** Yeah, it’s so in the imitation learning, it’s basing all of the actions off of the human behavior. And then the agent is kind of just learning a policy that continues with those actions. So this is done in two steps where you have to first build that reward model. So you take the decisions. Take the same data set that you were training the model on with imitation learning, and you use that to train the reward model instead.

And then in the second step, you can use that reward model to train the agent.

**Claire Longo: **That’s pretty cool.

**Duncan McKinnon: **And this is kind of more like the paradigm that’s used in reinforcement learning from human feedback. That we’ll talk about a little bit later, which is why we had to go through all these steps to get here, too.

And this is the way that it’s formalized in the paper. is that the human demonstrator takes these prompts that people are putting into the that would be putting into a large language model and demonstrates the app of behavior. So that’s the decision data set where you know, a human driver would be driving to show the model what to do.

And this is used to do fine tuning. We hear about it a lot, but it’s kind of hard to see how it fits into the overall process.

So in the second step. It’s collecting data, so more prompts, like a large set of prompts to sample from. And using those to have to label a rank the best to the worst prompts, and this gives the agents and feedback to go off of. and that’s used to train the actual reward model.

So the agent is learning what the human thinks is better or worse in terms of its outputs, so that it can. So that that’s actually just the reward model. So it uses that to decide the overall reinforcement learning problem. And then it optimizes a policy to output data that gets the highest report.

**Claire Longo:** Yeah. So that’s where you’re mathematically defining what you want this LLM to do. So if you don’t want it to hallucinate with this reward model and the policy that you’re optimizing towards you’ve defined it mathematically. And you’re kind of like forcing the system onto those rails mathematically. And it’s gonna converge to the right place over time. So if your models are doing something, you don’t want it to hallucinate, you’re kinda protecting it against doing that and teaching it not to do that, I think, is the right way to do that, right way to say it. 

But you’ve got this mathematical way of doing it. So instead of just like saying it, a prompt which I see a lot of people doing today. And I think it can be quite effective like you can give like very explicit instructions and a prompt but sometimes, it’s still gonna generate, maybe something that’s wrong. And this is gonna kind of like, pull it back to keep it on the rails for what he wanted to do.

**Duncan McKinnon:** Yeah it’s interesting that you talk about the prompts because, like you’re going off of this data set where it’s sampling a lot of prompts and somebody gets the control over what the ranking is for those outputs that the model is producing. So like your control mechanism goes from having to write some kind of reward function, or having to write some kind of prompt and hoping that that does the job to like. So it’s a different framing of that alignment problem that you’re talking about. 

You’re trying to align the model with a prompt change or like to to adjust what you’re telling them to do. You could also adjust it by writing a reward function for this directly, and saying explicitly: This is how I want the model to behave. But that’s a much harder problem to generalize across every prompt that it could get. So instead, you’re controlling your feedback on the prompts and saying like this is a good prompt, this is a bad, prompt, and then just trusting that a reward model will capture that and use that to tell the agent what to do.

**Claire Longo: **Yeah, that makes sense. What if, like some examples, I was trying to think through some examples here of like what is an example of the reward and a policy for like a real life application, like, I think sometimes about generating marketing content. And I want to optimize some kind of true metric there, like, I want people to click on the email I send, or I want people to purchase the item. So you have a metric there? Does that feed into like the reward model here?

**Duncan McKinnon: **Yeah. So in that situation, like, if you’re sending out emails, and you’re looking at the response rate has, like the feedback you could use the you could train a model on the email and the response rate and use that as the reward model to kind of direct the behavior to produce more emails that look like the input. 

And then, like, so like that reward model would take in the output of the model and then give it a report score based off of the expected clicks.

**Claire Longo: **I love being able to tie it directly to a business metric.

**Duncan McKinnon:  **Yeah, it’s interesting, I hadn’t thought about actually formalizing it in that way that you have kind of helps make it click a little bit.

**Claire Longo: **Yeah. Honestly showing earlier is where it kind of clicked for me, cause I’ve always thought about reinforcement, learning human feedback, but never seen like a diagram of what that workflow actually looked like. And it was kind of a Aha! moment to see like those steps that you just laid out.

**Duncan McKinnon: **Yeah, I agree like this. This slide was really, this part of the paper was so powerful to me that I just pulled it out into the slide because I thought it was really interesting. It helped me understand how this is applied to actual language models.

So basically, what it’s saying here is that going all the way back to the first slide to the markup decision process means formalizing how this works.

So the initial state pulled from, you know, all possible states is the prompt to the model. So that means that the States for this are just concatenations of strings, like concatenations of tokens. That’s your state.

So when you’re in a state, when you’re training this reinforcement learning premium feedback. That’s the text, either the response or the prompt and so the action based off of that initial state of that prompt is to pick a new token.

And that’s the first token of your response. And then you concatenate that to get the next date and the transition, and then you get some kind of reward for that based off of the reward model that you’ve trained.

And then you keep going. So it’s like each state is just the prompt and the next token and the action that you’ve chosen, which is the token also. Pure action is to pick the next token. So you’re just picking one token after another, which is actually how our loans work.

So it’s really I thought it was a good way to formalize it, and this goes through what that means in terms of the MDP. These are their parts of the MDP. That we have and then the last thing that I want to bring up is that you know we talked about in the last slide. How the model learns from human scoring.

But it seems like you could also do the same thing with an Eval like another model that’s judging the responses. So you could write an Eval to say, like, you know, I want a response that looks like this and use that to develop a reward model instead.

**Claire Longo:** Oh, that’s powerful. That’s one of the common ways that people will actually measure the performance of an LLM in production is the LLM Eval. It’s essentially functioning as LLM as a judge. So you have one LLM model evaluating the output of another one. And it’s a great way to just generate a metric that you can actually track to see like, hey, is my system going off the rails here? Is it hallucinating? And yeah, so you actually have, like a prompt in the loop there, that is doing the evaluation.

**Duncan McKinnon: **Yeah. So that kind of makes it a closed system where you don’t actually need the human, because you can have the LLM evaluate as a separate prompt, evaluate the response at each step.

**Claire Longo: **Yeah. When you and I read this, we both kinda had the same takeaway. I think we are both surprised that it is at the token level. So like the action is the next token. That’s the next word to be generated in the output, and the state is like concatenation of all the tokens. That’s so interesting. Because that means we’re after actually optimizing this at the token level and my assumption before I read the paper–It’s a good thing I read it–it was my assumption that this was maybe optimizing things at a level where it’s maybe like this prompts versus that prompt where those would be the action. 

So it’s kind of an interesting takeaway here.

**Duncan McKinnon: **Yeah, thank you. So that’s the last slide. I think it’s good to jump over the paper and talk about that a little bit more cause I think it goes through some of that.

**Q + A: Reinforcement Learning in the Era of LLMs**

**Claire Longo:** Yeah, let me share the paper here

**Duncan McKinnon: **Because what you were talking about with the output in this formalization, is a token. And that’s the next section in the paper, I think, is that he talks about how we actually don’t have access to the tokens.

So in an ideal world, we would be judging, each token would get its own reward, and that would give the agent more information to go off of it as it’s developing the full response.

**Claire Longo:** What do we have access to there? Like, what is the optimization done on? Where are we looking? Is it credit assignment credit assignment. So here they’re talking about the credit assignment.

The learn reward model can only compare responses on an entire level. So they’re concatenating everything up. So they’re actually. is it where it’s assigned credit to different tokens or part of tokens. Yeah, okay, that’s interesting.

**Duncan McKinnon: **Yeah. So he talks about how dense reward problems are easier to learn. 

So like you want to be giving feedback at every step that the agent takes, and in this case the agent is choosing each of those tokens sequentially.

And it would be able to learn faster if it had like, if it could tell if it could explore within that space of choosing tokens which ones are going to get a better reward overall. But instead, we get the full response, and have to just give it a single reward at the end.

**Claire Longo: **So the reward is actually not assigned at the token level. It’s actually like you’re you’re creating the state and the action by concatenating tokens up until a certain point. But then the credit assignment that, like reward optimization is still happening, based on the action level, which is like a concatenation of all your tokens up into that date.

**Duncan McKinnon: **Yeah. So maybe OpenAI could do that with access to the underlying model. Yeah, okay, so you need access to the underlying model to really optimize this at the token level.

**Claire Longo:** That’s really interesting. The other thing that stood out to me actually was prompting. So the actions that are taken to improve the system is fine tuning. So there’s kind of that loop up in this really cool diagram here where you’re using this data to fine tune with ChatGPT, it would be interesting, I think, to think about how to optimize the prompting strategy under this. Because kind of under this framework, because I’ve worked a lot with LLMs. I’ve prompted them quite a few times, and I’m really starting to notice that the way I prompt really matters just like the articulation use of language because it is a language model matters. How you’re really instructing the system.

So when I’m iterating and building an LLM system, I am iterating on my prompting strategy quite a bit. And that would be something very interesting to kind of mimic here.

We have a question here:

“I wonder if there is a response to it? I wonder if there is a method to deconstruct the response and measure Delta between request, prompt and response at the token level.”

**Duncan McKinnon: **Yeah, I think that’s a good idea. So you’re saying like. pulling apart the tokens that are in the response, and looking at that separately, individually. I think that’s an interesting idea. If you could feed that back into the model somehow.

**Claire Longo:** Yeah. It could be mathematically measurable maybe with cosine similarly but with Euclidian distance you could get that representation of the distance. Good question.

**Duncan McKinnon: **And then also like adjusting the prompt, too, like at the same time, if there was a mechanism to improve that.

**Claire Longo:** Yeah, I think they have a cool example here, actually, of the prompts, and what optimization there could look like. So you kind of have like user input staffing a math question. TBD, if I think that’s the right thing to do with an LLM but I always like testing their limits here. So we’re out asking, what’s raised to the power of four equals one. It gives a correct answer, that’s great.

And then this prompt. Here we’re saying, the prompt is a little bit different, a raised to the power. four equals one. Two experts are debating on the answer, and that is often a good way to prompt engineer to like, get these systems to reason and then give you the right output, but in this case it gives a wrong answer. So this is such a great example, like comparing two prompts and you could start to converge on which one is giving you correct answers.

**Duncan McKinnon: ** Yeah, it’s a hard problem, yeah, it goes through I think those next couple of sections. I didn’t go as deep into these, but it seems like it goes through that prompt optimization. And if you could use, prompt offline reinforcement learning to optimize. 

**Claire Longo: **Yeah, it looks like they’re talking about it, right here. You definitely use an offline data set here. I know, we’re running close to time here. But overall my take away on this paper was like, I loved it, the math was really fun to read through here. I really liked it. It gave me like the overview of reinforcement learning before it helped us think through how the reinforcement learning is actually applied in the context of an LLM, so it really helps me kind of map. What I know about reinforcement learning to that context of the LLM. And for me like that really was the Aha! Moment when I think through kind of this workflow here, and seeing how that flows, and then when they break it down with these diagrams, you can just kind of see, well, I know what a state is, an action, an environment. How does that actually map to the LLM world stuff. But yeah, how does the RL map to the LLM world, and they really made that mapping really explicit here, and also laid out some great next steps here with the credit assignment and prompting as well.

Duncan, what’s your kind of high level takeaway here?

**Duncan McKinnon:** Yeah, I think that I was really excited about this. The last thing that we specifically talked about the credit assignment, because it seems like that is a better  first, with their formalization of picking the next token as the action. And then getting feedback at that level.

Then the agent has a lot of different paths to take, even just responding to a single prompt you know, so like you would be, you could train on the same prompt. So in their formalization, you’re sampling. You’re picking a prompt from a set of prompts.

And running the model on it and getting rewarded off of different responses. But you could take the same prompt and keep doing it over and over again, and adjusting the path that you take through, selecting from all the tokens, because all of those tokens are the actions that you have access to.

So yeah, it just gets a little bit deeper into the weeds.

**Claire Longo: **We have one question from the chat here. Well,  Eric recommends that we look up Dspy for prompt optimization. So I’m definitely gonna check that out. It’s a cool problem to solve.

Matt asks a great question here. So assuming I’m a model–if I force a user to provide feedback before giving them a new answer, I can continuously learn from users and adjust my weights, add parameters. Would this be a good example of RL in practice?

I think somewhat. But I think you would actually want to…. Let’s see. So you force the user to provide feedback. So you got that user feedback right? And then you’re giving that the right answer. So you’ve got the user feedback and the answer there, and you can continuously adjust. I think kind of the reinforcement learning, like a good example of that in practice, would be like a model is getting human feedback, like feedback from the user.

And then, based on that feedback, you are adjusting those weights, parameters, that kind of thing in your mathematical definition of like policy and reward. So you don’t really have to like not give them the answer. You’re just like you are getting that answer through the feedback loop, and then, like adjusting from that, I think, is kind of how I think about it. But, Duncan, how does that really resonate with your understanding as well?

**Duncan McKinnon:** For example, like we see everyday like with ChatGPT, it has like a response like, Is this a good response? Is this a bad response, or even just like with text feedback. They can collect that information and use that to train a reward model.

**Claire Longo: **Yeah, exactly. That’s kind of the signal you want to grab.

**Duncan McKinnon: **Yeah.

**Claire Longo:** Johnny Lin makes a great point here: Wouldn’t it forget things if they concatenate and truncate words at the token level? It would seem to be limited by the token limits?

Yeah, right? Because, isn’t it kind of similar? Just having like a super super long, prompt, or like a really really long like, if you’re in that search and retrieval, and you retrieve like a ton of documents, sometimes too much information into this thing and oh, how to pinpoint the right information. So if you have a very long document in any of those contexts, I think you do have that challenge.

**Duncan McKinnon: **Yeah. It’s like, probably even more of a challenge than with the training. The language model, because your context includes the prompt at every step. So that is probably a problem.

**Claire Longo: **Yeah, I think that’s a good problem to kinda solve there.

Raymond says, “latency, though.”

Yeah, I mean, isn’t that kind of the known thing with reinforcement learning is latency challenges?

I do like offline learning and kind of like learning from example before the thing goes live. I think that probably helps jump start it, but that is a challenge that I’ve heard before with reinforcement learning. And when you have the human in the loop, like you’ve got to wait for the actual real human to come up with the feedback and get back to you. So that kind of adds to it.

One thing that actually stood out to me is the human in the loop here, because one assumption I had before I read the paper. Where’s our lovely diagram?

![Diagram from p.6 (via Ouyang et al.) There are 3 steps to align LLMs to human preference.](https://arize.com/wp-content/uploads/2024/03/Screenshot-2024-03-15-at-12.01.59 PM-1024x697.png)

Before I read the paper, I thought you could maybe put an automated feedback loop here, like signal that’s generated automatically. I guess a human has to generate it. But like a purchase or a click. Those kinds of signals are usually generated automatically through your software where this thing is getting deployed. And so you might not need, like an actual human labeler that has the job of like, actually reviewing things. It might be a little bit more automatic here.

**Duncan McKinnon:** Yeah. I think. Yeah, we talked about the Evals, too, like we could use an Eval to judge the responses based on some criteria that you put it also kind of like. I feel like every time you throw something into a limit as ambiguity in terms of what it’s doing. And if it’s picking up the right signals. But kind of the same problem with the human labeler.

**Claire Longo: **Yeah, that’s a good point. 

I think we’re right at time. Big thank you to the community for the questions, I love making this a conversation. Thanks for joining us today, guys.

**Duncan McKinnon:** Yeah, thanks, everyone, good questions. 

**Claire Longo:** Bye.
