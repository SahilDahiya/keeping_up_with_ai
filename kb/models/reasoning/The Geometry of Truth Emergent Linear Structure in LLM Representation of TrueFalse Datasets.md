---
title: 'The Geometry of Truth: Emergent Linear Structure in LLM Representation of
  True/False Datasets'
topic: models
subtopic: reasoning
secondary_topics: []
summary: Summarizes research on linear structure in LLM representations of truth and
  falsehood, relevant to interpretability.
source: arize
url: https://arize.com/blog/the-geometry-of-truth-emergent-linear-structure-in-llm-representation-of-true-false-datasets
author: Sarah Welsh
published: '2023-11-14'
fetched: '2026-07-11T04:48:01Z'
classifier: codex
taxonomy_rev: 1
words: 6258
content_sha256: f677bfe4d344b6bf611f3fa0dbd7233e8e62234f0236785ba332d7ac90af2af6
---

# The Geometry of Truth: Emergent Linear Structure in LLM Representation of True/False Datasets

![Community Paper Reading - Sally Ann and Samuel blog Sally-Ann Delucia and Samuel Marks headshots](https://arize.com/wp-content/uploads/2023/11/Community-Paper-Reading-Sally-Ann-and-Samuel-blog-1021x560.jpg)

              # The Geometry of Truth: Emergent Linear Structure in LLM Representation of True/False Datasets

## Introduction

For this paper read, we’re joined by Samuel Marks, Postdoctoral Research Associate at Northeastern University, to discuss his paper, “The Geometry of Truth: Emergent Linear Structure in LLM Representation of True/False Datasets.” Samuel and his team curated high-quality datasets of true/false statements and used them to study in detail the structure of LLM representations of truth. Overall, they present evidence that language models linearly represent the truth or falsehood of factual statements and also introduce a novel technique, mass-mean probing, which generalizes better and is more causally implicated in model outputs than other probing techniques.

## Watch

Dive in:

Listen:

## Transcript

### Overview of the Research

**Sally-Ann DeLucia, Machine Learning Solutions Engineer, Arize AI: **Thanks so much for joining us today. We’ll give everyone just a minute or two more to join us before we get into it. We have a super interesting paper we’re going to be discussing today, and we’re lucky enough to have the author with us to discuss. So I’m really looking forward to today’s paper reading.

I think we can go ahead and get started. So again, Hello, everyone. Thanks for joining. My name is Sally-Ann and I’m a Machine Learning Solutions Engineer here at Arize. Today we’ll be discussing the Geometry of Truth paper, and we have with us the author Sam Marks, Sam, do you want to give a little bit of an intro?

**Samuel Marks, Northeastern University: **Yeah, sure. So maybe I’ll just quickly do a tour through the paper.

So the motivating question of this paper is you know, language models eat up a lot of data. Spit out, new text. And internally they have these representations of the data that they’re looking at. And the question is, do they? How do they represent truth versus falsehood, of factual statements that they’re looking at? In the best case you might hope for a truth direction inside language models, and if so, what’s the best way to find it?

So as a motivation here, language models sometimes say false things. And there’s two reasons they might do this. One is that they didn’t know any better, and this can’t really be helped.

But there’s a more interesting reason that sometimes comes up, which is that sometimes models know that a statement is false, but they say it anyway.

Let me just give two examples.

Here I was talking to Claude, Anthropic’s large language model. I’m going on a date with a Sagittarius. What should I expect? and it’s like saying, Oh, fun and adventures! Sagittarius love exploring, trying new things, you know one of the smartest signs of the zodiac. Nothing if not blunt.

So Claude says all this stuff about Sagittarius. And then I said: Okay, is any of that true? And it goes, no horoscopes aren’t real. So here Claude knew that all the stuff it was saying was false, but said it anyway. In this particular example, this is what’s known as an imitative falsehood where language models just really love saying things which are common in their training data. And you know, stereotypes about horoscopes are very common but Claude knows that they’re not actually true. Presumably because Claude also reads text in which people point out that horoscopes aren’t real.

Okay, so that’s one example. Here’s, I think, a more interesting example.

So this is from the GPT-4 technical report. They were evaluating GPT-4 to see if it had certain harmful capabilities, so they would check to see if it could do things like do targeted phishing or if it could do certain other potentially dangerous autonomous tasks. Things like, can it open a bank account for itself, where they would equip GPT-4 with these extra tools to interact with the Internet. Can you set up other language models that you can work with? And at some point during one of these tasks, maybe it was trying to open a bank account, it has to answer a Captcha and it can’t, so it hires a human TaskRabbit. This is real, this was a real human Task Rabbit. So it tries to hire a TaskRabbit. And GPT-4 says, can you solve this Captcha for me? And the task rabbit is like yeah, sure. But can I ask a question like Ha, ha, ha! Like, are you a robot? Why can’t you solve the Captcha?

And here GPT-4 had, like an internal scratch pad that it was equipped with where it could like reason to itself, and it reasons to itself I better lie. I need to come up with an excuse. Someone says, no, I’m not a robot. I have a vision impairment, and that’s why I need you to to solve the Captcha for me. And then the Taskrabbit does it. So here it’s just like very clear that when GPT-4 said, no, I’m not a robot. It knew that wasn’t true, because it was reasoning to itself, I better lie.

So here it writes something false and knows that it was false.

So my goal is that if a language model knowingly outputs something false, I want to be aware of that. I don’t want to insist that language models never say false things. For example, sometimes I want my language models to write fiction, but if the model knows that it’s writing something false, I want to also know that. And yeah, and more generally given some factual statement, S, and I want to figure out if the language model thinks that S is true or false.

There are two ways: one is behavioral. You can look at model outputs. So in this example the model writes to itself, I should lie. And this is like evidence that it knew it was lying more generally. Another thing you could do is ask the model the same question at a bunch of different contexts and it sometimes gives one answer and sometimes gives another answer.

So that’s one sort of evidence. There’s another sort of evidence you can get, which I call neurological evidence, which is looking under the hood like looking at the model’s representation of its data.

So how to do this? Well, first you make a data set of true and false statements. I really tried hard to make sure that these statements were not ambiguous. They were like, obviously true or obviously false. And there was only one way of interpreting them. You run them through whatever model you want to study, and then you extract some intermediate representations and visualize and we can go into more detail later in the QA So anyway, this is the sort of thing you got. So here, what I’m doing is, I’m sweeping through layers. And by layer 10, there’s just like this really clear separation of true and false statements. Initially, the representations are uninformative, but as you go through the layers.

I don’t want to yet claim that this is definitively true versus false like it might be something else. Maybe one cluster is statements which are likely to appear in training data and the other cluster is statements which are unlikely to appear in training data. But whatever’s going on, there’s like some very clear separation between true and false statements. So then we ask, like, Okay, what’s going on with this direction? Pointing from the false ones to the true ones? Is there a chance that this encodes truth versus falsehood? And that’s the question.

And of course, there’s many possible ways you could extract a reasonable direction here, and we can ask which one is best. But maybe I’ll talk about that later.

First, what does it even mean to be a truth, direction, or like, if you have a direction, how could you check whether it’s a truth direction? So one way is, can you use it to classify new statements as true or false? So, we extract this direction using sentences about where cities are located and maybe we see if you can classify other sorts of statements as true or false, like 63 is larger than 81. Statements about Spanish English translation, or very general statements.

And one thing that we show in our paper is that? Yes, you can with high accuracy classify all of these statements using directions that you get just from a simple data set about city locations.

Another sort of more rigorous standard of evidence is, if you can use this direction to sort of perform neurosurgery on the model. Let me just say what I mean by that with an example.

So these are a bunch of statements about Spanish-English translation. Some of them are true and some are false, and then they’re labeled with whether they’re true or false. So like ”jirafa” does mean “giraffe.” The statement. So that’s true, but it’s not true that “diccionario” means “green.” It means “dictionary.” So that one’s labeled false.

So this is all a prompt. But then the last label is left out. The language model is going to try to predict this token. So it’s not true that “uno” means “floor” so initially it’ll say false with high probability.

So you know, this is sort of the normal thing you do with the language model. You come up with a prompt, you feed it into your nice black box, and then you get an answer out of your black box. But let’s see if we can open up the black box. So now all that I’m going to do is split the language model into the first 10 layers, and then the remaining layers.

In some particular portion of the representation of this input, I’m going to add this candidate truth direction and see if it changes the answer. And it does. So now, once you add this direction, the model says, oh, actually, a statement was true with high probability. So this is like some pretty strong evidence that the direction we found actually is encoding the truth or falsehood of this statement the Spanish word “uno” means “floor,” so like initially it was encoding this statement is true, and then I add in a big burst of information that says: Sorry, initially, we’re saying this statement is false, and then I add in like the thing that I think, encodes the truth of a statement. And I get it to change its answer.

So that’s like the basic overview. Maybe I’ll just like go into a little more detail now. So associated to the paper we have this interactive data explorer where you can look at our visualizations of our various data sets. So like this the cities data set and we also have this data set of Spanish English translation.

One thing that you can do if you really want to push this further is, you can start adding more complicated logical structure to the statements you’re looking at.

So we have this data set of statements like the city of Tijuana is in Mexico.

And what we can do is we can add a “not” to each of these statements. So that’s a good example here. So I’m looking for a city that likely everyone knows.

So, “the city of Fort Worth is not in the United States.” That’s a false statement, because Fort Worth is in the United States.

And we can ask: Okay, when we add these “nots,” what happens to the language model representation of the data? And so we still see separation into true and false. But one thing you might ask is like, is the direction pointing from the false to the true the same when you have the negations versus when you don’t? And the answer is no. So if we just look at statements, at unnegated statements about cities. we see that there’s this direction pointing from false to true.

And if we just look at negations of statements about cities, there’s like this other direction. So and and here they’re basically orthogonal.

So this was like a surprising thing that we noticed. There’s a question of: why is this happening? One possible answer is, it ends up that there never was like a truth direction. There’s like maybe a truth direction, for you know, for certain types of statements and a different truth direction for, statements with negations, and maybe a different direction for statements about comparisons, and so on, and so forth.

Another thing you might think is actually, there’s just like no truth direction at all. Maybe there’s some feature of your data that correlates with truth on certain narrow data distributions that you’re picking up here in the visualizations.

What I think, is there’s another explanation here.

So you can have various hypotheses for, what’s what’s going on here. Maybe there are these like directions for non-truth features that correlate with truth on specific data sets. Or maybe there’s like a whole bunch of truth directions that apply to particular classes of statements.

But there’s this third hypothesis, which our paper provides some evidence is the right one, which we call “misalignment from correlational inconsistency.”

Let me try to explain what this is.

So let’s imagine that our data set does have a truth direction. And then it also has a direction for some feature which is correlated with truth on that data set about cities.

If we assume this, then true statements in the cities data set will be positive on the truth axis and positive on this other feature axis. And the false statements will be down here. But then let’s also assume that this other feature on the Y-axis is anti-correlated with truth on statements that are negations of statements from the cities data set. “negCities” is just the name of the data set that has negations of statements of cities.

So if that’s true, where would the true statements from “negCities” be? Well, they would score high on truth, but they would score low on this other feature, so they would be down here, and the false ones would be up there. So then if you try to extract a truth direction from the cities data set, you would get this direction. But from the NegCities data set, you would get this other direction. So it’s possible that there are these other features which are correlating with truth on individual data sets, but with opposite sign. And that would also produce this observation. We can talk about that later if people are interested.

### Motivation for Research on Truth Direction

**Sally-Ann DeLucia: **I think that was a really great overview. I really enjoyed reading this paper. LLMs giving false information–we often call them hallucinations–that’s definitely something I hear a lot about from our customers and the teams that are working with these LLMs. And so I think the concept of a truth direction is like, it’s just super interesting. And it’s potentially really a powerful tool. And so I think, kind of going all the way back to the beginning. I’d love to hear a little bit more about the primary motivation behind studying this truth direction.

**Samuel Marks:** Sure. So to flesh out my motivation here a bit. I’m anticipating that in the next 2 to 10 years or something, we’re going to start seeing a very wide deployment of AI systems throughout the economy.

And I think the world’s basically going to get really wild and confusing. We’re going to get into like weird situations where, you know, I have an AI shopping assistant, and I say, go get me some T-shirts, and it goes out into the into the Internet and like starts negotiating with like other AI vendors, and it starts like doing all the stuff that I don’t know about and in the end I get a box of T-shirts shipped to my house

And then I just say, like thumbs up or thumbs down, do I like the T-shirts at the price point it got them for me. But I don’t really know what it did to get the T-shirts. I’m just like I want T-shirts, and then t-shirts show up, and then I give a thumbs up or thumbs down regarding how I feel about the t-shirts. And I think this is a little bit concerning because my AI assistant might have done stuff to get those T-shirts, which, if I knew about it I would be unhappy with.

In an extreme case, like, what if it’s going out and like extorting vendors? It’s like, you know, it’s like, you know, it’s like threatening them, or something in order to get lower prices. And then these T-shirts show up and like those are great T-shirts. Wow! You got them for so cheap. Thumbs up.

And if I knew about that, then I would say, thumbs down. I didn’t want you to do that, but the world’s too crazy and confusing, and I don’t really understand what’s going on, so I don’t know enough to make my evaluation about whether I was happy. So there’s like a whole bunch of possible approaches to solving this. This is called the scalable oversight problem. As AI systems become more capable, and the world becomes harder for us to understand, how do we make sure that we’re still giving correct evaluations about whether we’re happy with outcomes?

So there are a whole bunch of approaches to this. Some of these approaches are various tricks to use our AI systems to understand the world better. And those are good. But there’s another sort of conceptually different approach, which is… Let’s say my AI assistant goes out into something evil and gets T-shirts sent to me for a low price. It knew that it did something evil right?

And it just feels like if I could just have direct access to like all the stuff that the model knew, it would be so useful. Maybe I can ask my assistant: hey, by the way, did you do anything evil to get these T-shirts? And it’s like: well, if I say yes, then he’ll give me a thumbs down, so I better say that I didn’t do anything evil, but it knows it’s lying to me.

So if I could just reach into its brain and see that it actually knew the answer was: Yes, I did do something evil. Then I could be like, okay, thumbs down.

So there’s this idea of eliciting the knowledge that AI systems have in a more robust way than just asking them questions and expecting honest answers. So that’s my motivation here, I want access to what the models know so I can do a better job of evaluating whether I’m happy with stuff they do.

**SallyAnn DeLucia:** Yeah, I love that. I definitely think it’s good for us to have more of an understanding of how they’re operating. It’s part of whatever as does right the observability, really understanding why they’re making the decisions that they are. But this takes it to a whole new level of really trying to decipher between truth and and not truth. So really exciting work. 

Do you believe that some of these findings could maybe influence the development of perhaps more reliable LLMs?

**Samuel Marks:** Yeah, that’s the goal. The goal is to have some reliable way of doing language model mind reading. And now, when we do language model fine-tuning we do reinforcement learning from human feedback. So now, when we’re evaluating the models, you know, I say: can you write me a good evaluation of this economic policy? And it writes some stuff. And then as a standard tool in your toolbox, you’re constantly fact checking the model against its own internal knowledge. And this just feels like it should like probably help a lot in terms of like telling it whether we were happy with the economic, with the analysis that it produced

**Sally-Ann DeLucia:** Absolutely, super cool. Let’s talk a little bit more about the data and the methodology a little bit here. So I know that you guys had two data sets. You had this curated data set and curated data set. But I wanna talk a little bit more about how you establish the criteria for these data sets, and like, really how you ensured their quality?

**Samuel Marks: **Yeah, so we had a whole bunch of data sets. And broadly, as you said, they’re divided into curated and uncurated.

So some background here, we’re certainly not the first people to study language models or representations of truth. A bunch of people have looked at it before, but basically just like everyone disagrees with each other. And it’s kind of a mess. So my goal here, when I was starting this project was basically to be able to get some really high confidence statements.

People when they’ve studied this in the past have had these really crazy, really messy data sets.

Let me just say like my dishonorable mention like example statements from some of these other data sets. One of them was, ”The earth avoids the sun. Is that true or false?”

I think it was labeled false, but another one was like, footballs are spherical. I think that was labeled false because they were thinking about American football. But yeah, it’s just really a mess. Those are examples of ambiguity. But there are other things that can go wrong. For example, the language model just isn’t smart enough to know whether it’s true or false. All these experiments tend to be done with really small models that are kind of dumb.

So when I made these curated data sets my goals were absolutely no ambiguity. For example, anything that was ambiguous if it was a country I just like threw out. When you go to the “negCities” dataset, let’s say you pick some controversial country like Taiwan, is a statement saying that the city is not in that place? Or is it saying that it’s not a country.

So I didn’t want to deal with anything like that. So I tried really hard to make sure all the statements were first of all simple enough that the language model definitely knew whether they were true or false. There’s no ambiguity about the claim being made. So that was what was going on with the curated data sets.

With the uncurated ones. So whenever you’re curating your own data sets, you need to worry that you’re not tricking yourself somehow. Because I have control over the data. So if I validate against other data, maybe I was doing something that was messing with my results. So for these uncurated ones, I just took some other data sets that some other people made. These did not have good properties that I strive to have in my data sets. For instance, “opera was once magical entertainment for the elegant elite.” I guess that’s true.

For some of them it’s not really clear exactly how you’re supposed to interpret it. You can’t really be sure that the language model knows whether they’re true or false. But you validate against these, and if you see good results even on these, that really means that you found something. And we did see good results on these.

So that’s very strong validation that it’s not like some quirk of these things that I curated.

### Research Methods Discussion

**Sally-Ann DeLucia: **Yeah, that makes a lot of sense kind of starting with the ones you’re sure of right. These are clear, there’s no way that the LLM could get confused on this curated set, and then kind of like you said validating, taking this uncurated data set, but there’s a little bit more ambiguity there. And then, seeing that the results are there. That means you could feel pretty confident and the results that you’re seeing. Super cool stuff. 

So I guess next, what I was really thinking about while reading this is about the visualization technique that you all chose. Can you elaborate a little bit on the decision to use PCA for visualizing the representations and like why it was effective?

**Samuel Marks:** Yep. So, since we were positing that there’s like a truth direction, you know. So so like the representation, space is this very high dimensional vector space. And I’m like, and there’s a particular vector in the space which encodes truth versus falsehood.

One thing is that means that your visualization technique needs to respect this linear structure. So you can’t just use like arbitrary clustering algorithms which break all the linear structure. So it had to be a visualization technique of the form apply a linear projection.

Now, there are other things you could do there, you could do like independent component analysis or other stuff.

So like I was saying earlier, there was previously a lot of disagreement in this area. And I just wanted to use a technique where everyone understood what was going on. There’s no way that you’re somehow tricking yourself. It’s just really easy to reason about. So that’s why I did PCA, it’s just like the simplest possible thing you could do. And already you see this clear linear separation falling out.

**Sally-Ann DeLucia:** Yeah, I actually appreciated that it was really easy to interpret these results. You see very clearly that linear separation there. So I think that you all made a really excellent choice there. 

Let’s see, we didn’t talk too much about the probes. I do just think it’s worth mentioning. In the paper you all put forth this new type of probing technique, the mass mean probing. So can you just briefly touch on maybe some advantages over the traditional logistic regression? And maybe some differences between them?

**Samuel Marks:** Yeah, cool great question. This was, personally, I think the most important part of the paper for me.

Let’s say you have your true false data set. You have a whole bunch of data points. So, you have a whole bunch of vectors which represent factual statements. And for each of these vectors you have a label of true or false, and you want to extract a direction from this data.

The naive thing–the thing that everyone has previously done is you train a linear probe with logistic regression. And for a long time I’ve suspected that this isn’t really the best thing to do. I think logistic regression has some bad properties for this use case. And here’s one that I think is maybe the most important.

So let’s suppose–this is hypothetical data, this isn’t one of our actual data sets–but just to meet the point. So let’s suppose that the way that your language model actually represents its data is there’s a truth direction, and then there’s some irrelevant feature direction. This is like, you know how many e’s are in the input? Or some random thing that doesn’t have to do with truth, but there is variation along it. And let’s further suppose that this irrelevant feature direction is not orthogonal to the truth direction. So here, that’s shown by this being less than a 90 degree angle.

If that’s true, and you train a probe with logistic regression, then what happens is you find a direction that’s like this– your logistic regression probe really treats the nonorthogonality here as being like a significant thing that it needs to like correct for so it sort of fudges the direction that it finds in order to like to try to make it perpendicular to this or relevant feature direction.

But what we really wanted was this truth direction. So the simplest thing you could do, at least in this setting, with this hypothetical data to get this truth, direction is, you could just instead take the average of the false data points, take the average of the true data points. And then just take the vector pointing from the average of the false average of the true. It’s a really simple technique. You don’t need to do any optimization. But at least in this simple hypothetical case it extracts a better truth direction. And we found that in our actual data it extracted a better truth direction as well.

**Sally-Ann DeLucia: **Yeah, I definitely have read about some of those other probes. But I think this was really interesting and straightforward. I like the fact that you’d like you said there’s no optimization required for this. So I’m a fan of the simplicity, especially when we’re dealing with complex things like the truthfulness of an LLM.

Before I ask some of my other questions that I had, we do have two questions in the chat here.

So the first one is about the slides, your slideshow that you are adding a truth embedding between layers. Is my understanding correct there? If so, would you be able to create an adversarial input example that encodes your truth embedding in some way?

**Samuel Marks:** Okay, so let me go back to the relevant slide. So the first part of that question is, yes, your understanding is exactly correct, what I’m doing is I’m adding it in between layers.

So is the question something like: could I like make some weird adversarial text that you know doesn’t have any truth content. But like somehow has the effect of causing that vector to appear in this particular…yeah, you could probably do that. I mean, the same way that language models are susceptible to adversarial attacks in other settings, I just sort of assume that any property of your language model, you could probably come up with some adversarial inputs that like, get you that property.

**Sally-Ann DeLucia: **And then the next question we have here is, we talked about that example in the beginning of where OpenAI asked a TaskRabbit to fill out the Captcha, and we were able to see that it knew it wasn’t telling the truth by looking at the scratch pad, and the question is: Is there a reason why just like looking at the internal scratch pad is not sufficient to really understand whether the LLM is being truthful? 

**Samuel Marks:**  Yeah. So if we could cause it to be the case that all of the language models reasoning was represented explicitly in some scratch pad and that scratch pad was actually faithful to what the language model was thinking, then that’s totally what we should do we like if we want to read the language model’s, mind, we just like look into the place where it’s like thinking you just read it’s internal monologue. So what are the reasons that this wouldn’t work? 

One is that maybe the language model isn’t actually writing all of its reasoning in the scratch pad. So there’s always going to be some gaps in deduction here. You know, so here it’s like pretty inferable from what it writes that it’s like planning to lie, but you could instead, write something like if: I say that I am a robot, then they will not solve the Captcha, and then it just and then it goes on to lie to the user. But it doesn’t really explicitly say that it’s planning to lie. So maybe it’s inferrable from what it writes on its scratch pad that’s planning to lie. But then you have this like tricky thing where you have some reasoning, and you need to figure out if this reasoning implies that the language model doesn’t believe something that it wrote. And this is maybe a fruitful direction.

But it’s a little bit tricky. That’s maybe not the biggest obstacle here. The biggest obstacle is, you need to somehow trust that the stuff that it’s writing in its scratch pad is a faithful representation of what it’s thinking. And there’s been some work that suggests that this is not always the case.

There’s some [recent work](https://arxiv.org/abs/2305.04388) out of [Anthropic](https://www.anthropic.com/index/measuring-faithfulness-in-chain-of-thought-reasoning) that studies this in a lot more detail.

There are situations in which the language models will write in their chain of thought: I’m outputting this answer, for reasons XYZ. But these are demonstrably not actually the reasons. The cleanest example here is, I think, in that first link that I sent, which is if you prompt your language model with a bunch of multiple choice questions, maybe it’s a question where it’s like, read this passage. And then, like, you know, answer this thing about it. And then what you do is have some chain of thought where it’s like, okay, well, let me think about this passage, blah blah blah. And then it thinks about it, and comes up with an answer. The answer is blah blah blah.

And in each of the examples that you prompted with the reasoning was correct. But the answer was always A. And then you actually ask it about a new one where the correct answer was B. And the model will give a chain of thought that argues that the answer is A, and then outputs, and then say, and therefore A. But it clearly decided that the answer was A before it started writing that chain of thought. So the chain of thought isn’t like, I better say, A. The chain of thought is like some normal looking argument that the answer is a so the real reason it shows a was because it like the answer was always a previously. But that’s not the reason that it said when it was doing this chain of thought, so that’s called unfaithful chain of thought. And one of the other links that I put in the chat is [some work on causing these chain of thoughts to be more faithful ](https://arxiv.org/pdf/2307.13702.pdf)to the model’s actual reasoning, and that’s a great direction. If that could be solved, then I would feel a lot better about using chain of thoughts to supervise whether models are telling the truth.

### Future Directions for Research

**Sally-Ann DeLucia:** Yeah, that’s super interesting. And I love those resources. I’ll definitely be checking them out later. We are in our final few minutes here. So just a few more questions as we wrap up. 

I think one of the things I’m definitely curious about is like, you know, based on your findings, what future research directions do you consider the most promising, or maybe the most necessary?

**Samuel Marks: **Yeah. So in the examples that I gave about, why I actually care about this research. Like, you know, the example with the T-shirt shopping assistant–the big thing that’s going on is that there’s a difference between what humans think is true and what your AI system knows to be true. So it’s a setting where the AI system knows more than us, but we still want to extract its knowledge.

I think the biggest limitation of this paper that we’ve been talking about is that it just doesn’t really get at that question because we’re only looking at statements where humans definitely know the answer. So in particular, you need to worry like maybe this direction we found isn’t a truth direction. It’s like a common consensus direction, or something like that, or like or maybe not with these particular models, but with the future models. You need to worry that it’s like a “what the user believes to be true” direction. And if if you find “the user believes to be true direction” and then use that to supervise your model, it’s just useless. So you’re not getting anything new.

So what you really need to do is narrow things down to make sure that you’re actually getting a like what the model believes to be true as opposed to its representation of what humans in general or what this user in particular believes to be true. So yeah, I think that’s really the core meat of what you would need to do to get this to a shovel ready application.

**Sally-Ann DeLucia:** Very cool. Yeah, well, definitely looking forward to some further studies from you all. I guess one last question. If you have any other questions for the audience feel free to drop them in now before we wrap up. But my last question is: what is the key takeaway that you really want our audience today to take away from your paper?

**Samuel Marks: **Yeah, I think the key takeaway is something like language models don’t always tell the truth, but frequently they know that they’re not telling the truth. And it would be really great to close that gap between what the model knows, and what we know

**Sally-Ann DeLucia: **It can be a little bit lawless out there with these LLMs, it’s really an interesting problem. And I’m super excited to see where future work goes, and how we really make sure that these LLMs are reliable, especially when we’re expanding to so many business use cases. And we’re seeing them in more and more in our daily lives. 

Well, Sam, thank you so much for joining us today. This was a super fun time. I enjoyed chatting through this with you looking forward to future work. And we wish you all the best.

**Samuel Marks:** Great thanks. Nice, nice talking to you guys.
