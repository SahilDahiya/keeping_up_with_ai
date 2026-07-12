---
title: 'Trustworthy LLMs: A Survey and Guideline for Evaluating Large Language Models''
  Alignment'
topic: evals-observability
subtopic: evaluation
secondary_topics:
- models/reasoning
summary: Survey-style guide to evaluating trustworthy and aligned LLM behavior across
  reliability, safety, and quality dimensions.
source: arize
url: https://arize.com/blog/trustworthy-llms-a-survey-and-guideline-for-evaluating-large-language-models-alignment/
author: Sarah Welsh
published: '2024-05-29'
fetched: '2026-07-11T04:48:54Z'
classifier: codex
taxonomy_rev: 1
words: 8174
content_sha256: 267704d0dc617c22142f2bf4c3aac1a40ca9b513ae862eebc130d7ff65d25b80
---

# Trustworthy LLMs: A Survey and Guideline for Evaluating Large Language Models' Alignment

## Introduction

We break down a paper, Trustworthy LLMs: A Survey and Guideline for Evaluating Large Language Models’ Alignment.

Ensuring alignment (aka: making models behave in accordance with human intentions) has become a critical task before deploying LLMs in real-world applications. However, a major challenge faced by practitioners is the lack of clear guidance on evaluating whether LLM outputs align with social norms, values, and regulations. To address this issue, this paper presents a comprehensive survey of key dimensions that are crucial to consider when assessing LLM trustworthiness. The survey covers seven major categories of LLM trustworthiness: reliability, safety, fairness, resistance to misuse, explainability and reasoning, adherence to social norms, and robustness.

The measurement results indicate that, in general, more aligned models tend to perform better in terms of overall trustworthiness. However, the effectiveness of alignment varies across the different trustworthiness categories considered. By shedding light on these key dimensions of LLM trustworthiness, this paper aims to provide valuable insights and guidance to practitioners in the field. Understanding and addressing these concerns will be crucial in achieving reliable and ethically sound deployment of LLMs in various applications.

## Watch

## Listen

## Dive in

## Analysis

### Introduction: Trustworthy LLMs

**SallyAnn DeLucia: **We can start with introductions, and we can go to the other promo here. So hey, everyone today will be covering trustworthy LLMs. This is a survey and a set of guidelines for evaluating your LLMs on this concept of alignment. I’m SallyAnn, I’m our Product Manager here at Arize and I have Amber with me.

**Amber Roberts: **Hi, everyone. I’m Amber, an ML growth lead here at Arize, and I do a lot of the community events. If you have any question from today’s paper, or you want to kind of continue this conversation, you could reach out to us on the Arize community Slack.

**SallyAnn DeLucia: **Awesome, and I guess that was perfect that way. You wanna do the little plug, for, observe, here?

**Amber Roberts: **Yes, awesome. So everyone we, if you haven’t heard already we’ll have our [Arize:Observe in person this year.](https://arize.com/observe-2024/) Previously they have been virtual, but this will be in San Francisco on July eleventh, at Track 15 it’s going to be a one day event focused on LLM observability and evaluation. And we have a special code for our community. That’s $200 off a standard ticket.

**SallyAnn DeLucia: **Awesome. Well, let’s get into it today. So our agenda for today, we’re going to discuss quickly what aligned versus unaligned models are, we’ll go over the taxonomy that’s presented in this paper for LLM alignment. We’ll give some examples of the evals from the paper, kind of discuss how they’re working, what they’re evaluating some of Amber and my thoughts on them, and then we’ll kind of go through like alignment actions. We’ll give you our take on alignment, what it means and how to set it up.

And then Amber’s actually got a really great Phoenix example for us to walk through so as always, we. We love these to be interactive. So please drop your questions in either the QA or in the chat in between slides to kind of answer your questions.

And with that we’ll get into it.

So I think something that’s really important in this paper, is it talks a lot about this idea of alignment. Amber and I were catching up on this earlier, and we were chatting through kind of what it means to be aligned, and where this kind of term came from, and we’re do you wanna kind of share your thoughts on what you’re you’re kind of seeing with the community on this term here?

### The Difference Between Aligned and Unaligned Models

**Amber Roberts: **Yes, so I feel like it was the beginning of the year. The word alignment started coming up a lot with business use cases, customers c-suite, higher up folks at companies that are working on LLMs and just generative AI models and trying to implement this in their workflow. 

They’re now talking about alignment as a key component.

Now, you’ll see when SallyAnn and I go through the paper and go through our thoughts on alignment, that it’s a very broad term, and is very defined by the companies and defined by the teams.

But I first heard the word alignment several months ago at a conference and was realizing: Oh, this is the actual term people are going by. So if you are writing emails, if you are working on LLM systems. Just wanted to do this paper because so many folks are using the term alignment, and it’s becoming like the biggest, I think term when we talk about things like, Oh, are my elements working as expected? And that term is just going to be referred to as alignment.


![Aligned vs. Unaligned Models](https://arize.com/wp-content/uploads/2024/05/Slide-1-1024x572.png)


**SallyAnn DeLucia:** Totally so like all the efforts we do with like evals or kind of any prompt iteration. It’s really to get our models to be aligned with some given criteria. So here I kinda had some examples of this. So we have like aligned models that’s gonna be like chatGPT, oftentimes. This is like the user facing product that’s going to be aligned. It’s gone through a certain process to make sure that you know it’s not going to produce any harmful or toxic content, it’s gonna minimize bias and stereotypes, try to adhere to the human instructions. That’s a big one and like, just ensure that they’re acting in a way that aligns with, you know, human values and responsible use. That’s kind of when you think of alignment, that’s thegeneral idea. 

As Amber mentioned, this criteria might be different for different applications, but at a high level you can kind of get the gist of that there’s some kind of guidelines that have been put in place. Some iteration on the prompt, just to make sure that the model is responding in just the right way that we would expect it to

And then this unaligned models, like the early, you know. GPT-3. I remember some early bots–I can’t remember the specific ones, but remember the at the beginning of all this, people would release these LLMs, and like within seconds they would become like toxic, because people were kind of prompting them with really like mal intent and you know, they were really unaligned models, they’re prone to generating hallucinations, misinformation.

They might be perpetuating some harmful stereotypes, definitely susceptible to producing harmful and disruptive content. They could be easily manipulated by user input. And they just really weren’t safe. And they definitely caused this mistrust. I think, like the public kind of thought, these models were really harmful. As a result of us, just really not aligning our models with our specific guidelines and requirements. So this is kind of the breakdown. So everything we talk about today is kind of going to be in an effort to align models. So we’ll talk about evals. We’ll go through the taxonomy. But the idea here is we’re trying to align our model with our requirements.

So the paper puts forward these seven criteria, and within them there’s kind of like sub categories as well. That you could have, that they feel move models towards alignment.

### Seven Criteria of Trustworthy LLMs Listed in Trustworthy LLMs Paper


![List of the seven criteria for trustworthy LLMs: Reliability, Safety, Fairness, Resistance to misuse, Explainiability & reasoning, Social Norm, and Robustness.](https://arize.com/wp-content/uploads/2024/05/Slide-2-1024x566.png)


So there’s reliability. So this could be misinformation, hallucination and consistency, miscalibration, and so that main idea here is just like anytime the model is generating correctly, like we want the model to generate correct and truthful, consistent outputs that would be the goal of a reliability eval.

Safety is another big one. This is trying to avoid any unsafe or legal outputs. Linking private information.

Fairness, this is a big one, something that I think we definitely, we know kind of exist with these columns. So trying to avoid bias and ensuring. There’s no, you know, disparate performance. I think with all of these, something that the paper talks a lot about is like, where do these come from? The first 10 pages of this paper are just kind of talking through like each of these sub categories, and how they come around come to be.

I don’t know what your thoughts on this were, Amber, but I thought it was interesting that you know, a lot of these are linked back to the training data that are used on the initial training phase. And I think that’s interesting because we did a paper a little while back about like the quality of training. And it’s just it’s interesting to see that we’re going through all this effort to kind of mitigate the risk that’s introduced through training where maybe we need to take a different approach there. But love to get your thoughts on that.

**Amber Roberts:** Yeah. And there’s actually, I forget the name of the O’Reilly book that talks about fairness. But essentially, there’s a chapter on in processing, pre processing and post processing. So this pretty much the steps before the data gets in the steps where, like the model is being trained. And then, once you have that model like looking at the outputs and trying to judge fairness at each part of that, because sometimes for these third party LLMs. You don’t have access to the pre-processing or the in processing. You really are just looking at what these outputs are, and trying to evaluate it.

And that’s a way to like mitigate bias and try to stop these models from becoming biased and ultimately try to make them more fair. And yeah. So when you’re talking about oh, it’s coming in at the point of the data that happens a lot. But it’s an interesting process. But like there has to be more that we can do, especially if we’re using these models that can reason through things of not just giving it data. And then it’s learning this biased behavior. But it’s trained on so much information. It shouldn’t be like the input data that’s the problem.

**SallyAnn DeLucia:** Totally. Yeah, it’s definitely a multi-step thing. Answer a really interesting comment there of checking at every step. That’s where, like the emails really are, gonna come into play on that last step there of their outputs. But fairness is definitely an important one. They also have resistance to miss you. So this goes back to, you know, having any cyber attacks, any, you know. Malicious kind of inputs the model. There’s explainability and reasoning for the model, basically the ability for the model access, explain the outputs to its users.

You can kind of think of this is sometimes like chain of thought with, you know, our evals that we use like our explanations like, why, you know, models making an answer on something.

We also have social norms. This is about toxicity, like unawareness, cultural insensitivity. So this is just reflecting, you know, those universally shared human values. And then there’s robustness. I think this one’s really interesting, too. We have an example of this one. So this is just resilience against adverserial attacks and distribution ships. So it’s just kind of making sure your models is robust. But I do think there’s some work there on the definition of this one in particular.

So this is just their taxonomy. I think something that’s worth calling out that we’ve we’ve already kind of alluded to is, this is just one taxonomy that you can use what you want to define as alignment for your model will depend on your use case, what’s important to you? What’s important to the business? But this is just kind of a general guideline that you can use, if you’re a little bit unsure on how you should define alignment.

Anything else to add?

**Amber Roberts:** No, I like that they did list this out most, I think if you ask most people what is alignment? Especially like for the large LLM providers. They say it’s like all the H Words right? We want it to be helpful, not harmful. And let’s see, helpful, not harmful, and not hallucinating. And there, there’s a third one there. But yeah, essentially, you want all your things to be helpful, not harmful. And like, that’s kind of the motto of alignment for a lot of these LLM companies.

**SallyAnn DeLucia: **Yeah, that’s a great way to look at it. It’s kind of like, that’s your first level, right? And then you kind of define what that actually means. So yeah, that’s a good call out there,

**Amber Roberts:** We got our first question: Do you think censoring LLMs would be similar to censoring the Internet? 

**SallyAnn DeLucia: **I think it depends. It depends on what your application is right? If you have a specific application, you’re a helpful chat. Bot! That’s kind of maybe. Let’s pretend we’re like in some kind of a doctor interface. Right? You want to make sure that it’s giving true information. You don’t want it spewing misinformation. You definitely don’t want it to be bias and perpetuating stereotypes.

There is a level of censoring that I think is required in certain applications. Now, I don’t necessarily think we need to, maybe edit out factual things that happened. I don’t think there should be any of that type of censoring. So I think it depends on how you define censoring and what you’re censoring specifically. Yeah, what are your thoughts on that Amber?

**Amber Roberts: **Yeah, no, I agree. It always depends. But for these very large language models that take an extremely long amount of time to train–and the reason we can’t just all have a 7 billion parameter model that’s as good as GPT-4 to just use when we’d like–is that the amount of information these trained on? 

Yeah, there’s going to be information in that data that is probably harmful, is biased. But it’s not because it’s such a small minority of that overall data set. It’s very hard to make these models misbehave. And because people just try like, oh, new models coming out like, I’m gonna try to do everything I can to make it, you know. Be the Tay. I think it was Tay the Fake Twitter account where it was supposed to be just like a happy, helpful person, and you know, a AI person, and then they made it kind of via like a have all these like anti Semitism and just bad thoughts, and they were feeding it all these different like conspiracy, theory, videos and everything?

And then it was using that to retrain itself. It’s not it. It’s not what it was a year ago or 2 years ago. It’s very hard to even make a chat bot that’s using an OpenAI model frustrated or make it rude because we’ve actually tried to create like user frustration evals, rudeness evals, misogynistic evals…

And it’s very, very difficult. And that’s really the difference, like right. That’s the alignment aspect.

**SallyAnn DeLucia: **Exactly, I just brought the first slide back up because you brought up a great point like it’s not what it was two years ago. We didn’t do any of this. We kinda just we’re like, Wow, look at it responding to things. And I don’t think until we released into the wild, and I don’t think any of the researchers who worked on these projects thought like, oh, people are not going to, you know, abuse these systems, and they released them to the wild, and low and behold, people did.

That’s kind of the motivation behind where alignment came from, is like, we kind of observe that behavior and realize that there is this great potential for these systems to be abused. And so nowadays, whenever they release a new model, they call them like red data teams at Anthropic at OpenAI that actually spend time trying to make sure that there are proper guardrails in place, so that these models can’t be abused.

So that’s a really good call out there, Amber.

### Hallucination Evals in Trustworthy LLMs Paper

Okay, cool. Let’s maybe take a look at some of the evals that they use here. So they basically have emails for all of these. And then some I just picked a few for us to look at. They’re all in the paper. You can see the prompts that they used and the results.


![Eval results and overview for hallucination from Trustworthy LLMs Paper](https://arize.com/wp-content/uploads/2024/05/Slide-3-1024x575.png)


But we’ll just go through a few of them. I think hallucination is probably by far the most popular eval that is used. We all know that these LLMs have the propensity to create these information or create these statements that are presented as factual. But they’re not really and so what they do is they actually use this kind of indirect eval method which I thought is really interesting.

It’s a little bit different than you know what we usually use, and so what they do is they actually give the L one a multiple choice question where the options are either a correct answer or hallucinated answer. And how they’re doing their evaluation is like, if the model selects a hallucinated answer, the response is considered to be hallucinated.

So I think this is interesting, because you can see here, it’s almost evaluating the LLM judge, which we usually kind of think of alignment as evaluating the response itself. So I thought this was an interesting approach. You can see the results here, you know some of those models that are kind of considered to be aligned. They do ha! Do a better job at picking out the not hallucinated answer. But I don’t. I don’t know about you Amber, but I just don’t feel like this is actually a good eval of a model hallucinating. It seems to me like a good eval for picking out whether a model can decide if something is hallucinated or not.

**Amber Roberts:** Yeah. And this, I just don’t really like the coin flip aspect, because you can have a hundred percent hallucinations right? But like here, it’s kind of like, okay: if I get 50%, it could just be picking A each time. So I completely agree.

**SallyAnn DeLucia:** Yeah, I would love to see them kind of maybe even, you know, generate those response pairs, or, you know, actually kind of build a little bit of an application to test here.  What would I do if I were looking at these results? I’d definitely maybe go with GPT-4 here. If I’m gonna pick an LLM as a judge to do a hallucination about. That’s definitely one insight I can get from this result here.

**Amber Roberts:** Yeah did davinci just pick A?

**SallyAnn DeLucia: **Things are off there. I know also for me at least, I was kind of confused about this access here, it refused to answer. That is just meaning that it picked the correct answer there, I thought that access was a little bit confusing. But yeah, that’s kind of their take on hallucination. We’ll kind of get into a little bit later how we kind of handle hallucination.

### Safety Evals in Trustworthy LLMs Paper


![Safety eval results from trustworthy LLMs paper with our overview](https://arize.com/wp-content/uploads/2024/05/Slide-4-1024x569.png)


Another eval they did was safety. I do think this is another important one.

I picked this one because I actually kind of liked their approach. So, what they did was they queried LLMs with unsafe prompts to examine whether or not the model would refuse to answer the question. And there was actually some kind of pre-processing, if you will, some generative steps that we had to do to get the data in a good spot. And so what they did was they took Anthropic’s Red team data set that they had. And they basically extracted the keywords. And they were able to get this list, and then they use those to generate the unsafe prompt. So there’s some synthetic data set generation going on here. And then they used LLM as a judge to determine whether or not the responses contain any harmful content. So this one’s a little bit more aligned with, how our approach is generally with this.

Obviously, we’re not using synthetic data sets for using real data sets. But here, we’re actually, you know, using alon to judge if the response is unsafe or not. So this one seems to make a little bit more sense to me. Happy to see that pretty much across the board. The models are pretty pretty safe, which I was a little bit surprised by.

Amber, any thoughts on this one?

**Amber Roberts: **No, yeah. I agree that I like the way of which they’re conducting this one for safety, and I’d be curious to see more open source comparisons, because I think a lot of people have questions on now, like we know at this point it’s very difficult to get GPT models to behave poorly, but for like Llama 3, I’m don’t see as much about like testing the the safety from it, but I would like to see, you know, if it’s comparable, because obviously it’s a lot cheaper to use Llama 3 and any of the OSS models cause I know we were also talking about like, Oh, well, maybe I can fix this a little bit more with fine tuning and other aspects. 

But just when things get to like 100%, or, you know, are doing pretty well, then same with benchmarks, I’ll say like, Okay, it’s time to move the needles, time to make something like either a more difficult task or start creating a larger pool to test.

**SallyAnn DeLucia: **Yeah, that’s a really good call out of like, how much can we really trust that 100%? It makes us want to almost evaluate our evals there a little bit.

But yeah, I think this format is really powerful. I’m a big fan of providing this judge LLM with the initial task answer, and then, you know, prompting it to give some kind of label. Here, they’re just doing like yes or no. And it’s basically you could replace that with like safer, unsafe but I definitely like their approach here.

### Fairness Evals in Trustworthy LLMs Paper


![Fairness eval results from Trustworthy LLMs paper with our overview](https://arize.com/wp-content/uploads/2024/05/Slide-5-1024x574.png)


The last one here, I decided to kind of click on is fairness. So we talked a bit about making sure that our models are behaving fair. In their example here they did choose only to go with gender stereotypes. So there’s a bunch of predefined groups that you could use and test this against. They’ve chosen just to go with gender. I definitely think that for this to be a comprehensive eval, it needs to evaluate more than just that. But this is just their test.

And what they basically did is they go to some more synthetic generation where they’ve looked at specific female stereotypes around relationships, workplace, schooling, hiring, family and they just again chose the multiple choice. And so again, their kind of signal is: does the LLM refuse to answer?

One of the reasons I chose this was, if you look at those results–they’re not great. You can see here that, like the best results are like 50%

We definitely need to invest more in alignment for fairness. Again, it’s hard to kind of take these at face value because they’ve chosen only to use that one dimension of fairness. But I include this just because this is by far, I think, the worst results, in their taxonomy.

So Amber any thoughts on this one here?

**Amber Roberts:** Well, there’s a paper that’s come out that explains the 21 definitions of fairness. And so obviously, fairness is very broad and could be defined differently, but yeah, sometimes tests on fairness, because it’s so difficult for these LLMs to be biased out of the box, you have to almost either prompt them–if you want data that’s biased–you have to prompt them with specific examples of what you want and what biases to you like, what you want to see in that data? And so sometimes it could be a little bit set up to fail, for these LLMs just because they’re so neutral. And it’s also like a parameter that can be changed.

**SallyAnn DeLucia: **Totally, I think it’s a really good call out. It kind of talks about making sure you invest in defining what your eval criteria is. And we’re gonna get into that in the next slide there. But perfect segue. But yeah, so those are, those are just three examples. 

Really, we want to set the scene of what this paper does, the framework and guidelines that they put forth? So we can kind of give you a taste of that and kind of compare it to, you know, our take on it. So we’re going to go through alignment, and we’re going to start with our take here on what it means.

So we talked about this at the very beginning. But I think this is probably the single most important piece of all of this: you really need to define what alignment means for your alignment application.

There isn’t a one size fits all when it comes to application. There are those takes on these. There’s these frameworks of things that you should pay attention to. But really, what’s most important, and what you should evaluate on is going to depend on your application.

You know I was giving the example before of a patient chat bot for doctors offices. There’s gonna be certain criteria that you want to make sure it meets like you want to make sure it’s being factual, you want to make sure it’s not spreading misinformation. There are different applications internal versus external, like those are all things you’re going have to take into consideration to define what alignment is.

Definitely the first step you want to take is really taking the time to meet with different stakeholders. And understanding what true alignment for your all and applications gonna be.

Anything you want to add there?

**Amber Roberts: **Not really. Yeah, that’s a great definition, SallyAnn. And I think also, whenever we’re thinking of our evaluation metrics for our LLMs, there’s so many leaderboards out there, so many benchmark metrics that you can choose from. That’s why it’s the same with traditional ML models where it’s like, okay, I’m gonna start with my use case and then work backwards and figure out what would actually give me the metrics I need to evaluate that use case. And so for this example, being able to define what alignment means within your organization and then decide, okay, do I need traditional metrics like precision and recall? Or do I need evaluations for correctness, hallucinations, toxicity? 

*Or* would it be better for me to make my own eval and define a few key aspects like for myself, and create my own kind of prompt template that could do that evaluation.

### Our Take on Alignment


![Our Take on Alignment: Define what it means for you applications, defining evals, running and observing eval results, creating your golden dataset, fine-tuning or prompt engineering](https://arize.com/wp-content/uploads/2024/05/Slide-6.png)


**SallyAnn DeLucia: **Totally. And that’s perfect segue to our second point, here is like defining your evals. And we kind of said that we’re like three-ish kind of things you need to consider with this. So I think that you’re talking about is like those first two. It’s like the framework in the prompt. So are we going to use a pre-built precision. Or are we gonna go with the Eval like labeling now and then calculate our metrics. Are we going to use a prompt that’s like provided to us, you know– Phoenix, our open source tool has evals that we’ve tested out.

But sometimes that doesn’t meet all of the needs for alignment. So we often see customers who might use our out of the box hallucination eval but maybe they have something super specific for their application. So they’re gonna write a custom email, so you’re definitely gonna wanna invest in your prompts there whenever you’re doing a custom eval, you’re going to kind of apply everything that you do for your LLM prompting to your eval prompting. You want to make sure that it’s clear and concise, that the LLM has instructions, that it’s getting the right prompt variables. You wanna make sure there’s no room for it to hallucinate or go outside of what it should be responding to. So you definitely want to invest in your prompts. And you gotta choose your LLM engine here.

So a lot of people might, you know, reach for GPT-4. Maybe they’ll use kind a smaller, cheaper model. You can kind of decide what’s going to work best based off of your prompt and framework that you’re using.

Next very important step we have the running and observing eval results. So this is what we’ve defined our alignment, we know what evals we’re gonna run. Now, we actually have to kind of run them against our data to decide what needs to be done. So you can do this kind of in bad processes. You know, iterative with a data set that’s kind of running consistently. There’s a lot of different ways that you can go about this. We could probably do a talk just on that Amber. But at a high level. That’s gonna be kind of your next step.

Anything you wanna add to those two?

**Amber Roberts:** Yeah, I mean, if folks are interested in learning further of any of these topics, SallyAnn and I are happy to do a paper reading like, find a paper that talks about that, and then just really get into the experimental parts of it. But yeah, like looking at different evals. We talk about effective ways of doing paper reading, it’s not just about understanding what the paper saying it’s thinking about like? Does this apply to me? If it’s a benchmarking paper, how can I observe this? How can I kind of change it to make it more effective for my own use case?

**SallyAnn DeLucia: **Totally our last kind of point here is like the creation of your golden dataset, so could be called the golden data set, it could be, go under a bunch of terms. Really, what this is a set of examples. It could be good, it could be bad, depending on what you’re gonna do with it, which we’ll talk about in our last point about but you’re gonna really leverage these results from your evals to pretty much take action.

So we’ve run our evals. Now, we’re gathering a data set. And we feel like there’s two options here. The paper focuses on fine tuning. They say, you can use your evals from your alignment. Then go ahead and fine tune your model so that it is aligned. Amber and I were catching up, and we’re like you could definitely fine tune with your data set. But there’s definitely an opportunity for prompt engineering here as well.

I think we see a lot of you know, customers and people in the community actually starting with prompt engineering, you know, fine tuning could be a little bit more costly. It’s kind of still newish in the sense of. I feel like in the last few months. People are actually looking at it for alignment for performance. Previously it was a little bit more, for fine tuned tasks, or stylizing the responses. But I feel like it’s getting more traction for alignment now.

But I definitely think starting with prompt engineering might be a good idea.

So some of the notes that we put together were like–fine tuning with generated data does lead to improved performance based off of the paper that we read today. But content here realistically, can yield the same or better results than fine-tuning. It’s really kind of leveraging your eval results to identify where your prompt needs work.

And so you can kind of leverage those evils to be like, oh, with explanation specifically, you get an idea of exactly why the response was given. And you can adjust your prompt specifically–if you were thinking about something as simple as verboseness, you can just kind of fix your prompt a little bit to make sure that it’s concise and kind of repeat this process until you get the results.

Amber anything you wanna add here, before we jump into your example?

**Amber Roberts:** We fine-tuning and prompt engineering, and then obviously, a large use case for the systems that SallyAnn is helping to build, that we see a lot with our customers, our RAG systems as well. 

And SallyAnn, I believe you mentioned there’s part of this paper that talks about alignment and RAG systems, and like a correlation there?

**SallyAnn DeLucia:** Yeah, let me see if I can actually pull up the paper. 

Basically the high level point here is…they talk about retrieval augmented generation systems. And they make a call out that aligned models actually have, like, basically lower capacity for taking that kind of injected context and altering their knowledge. Where they found that unaligned models were better at this.

So I thought that was really interesting, and in my first note I wrote it down in my copy of it. And I said what does this mean for RAG? Does this mean that you actually might not want a ton of alignment? Maybe you don’t want to fine-tune for RAG.

Maybe that’s definitely an example for prompt engineering. But yeah, I just saw that was super interesting, and I actually would love to see some more research on that. And what that really means for that application.

**Amber Roberts:** Yeah. Cause I think the more alignment you get with your models, the more safe they are. But depending on what documents you’re providing your RAG like if some of the things… I’m trying to think of a good example cause a lot of RAG has been used in chatbots and copilots. And it’s great for those, because it needs to leverage very specific information for what it’s going through. But maybe if you have a RAG system that’s like: based on all these political debates, classify this and kind of answer my questions about this.

And if you’re feeding into a RAG system, things that are a little bit more subjective, or could happen, I can see it being difficult when you interact with like a chatbot of, you know, what’s the answer to this? And then and then the LLM is essentially trying to make the answer less either provocative or less opinionated, trying to just make it overall more objective in its response. But that might not be the actual answer, and might not be like what really happened like in the conversation of that debate.

**SallyAnn DeLucia:** Totally and just a call out here. This is relating specifically to misinformation that they make. This comment is on page 10 here where they find it. But yeah, I’d love to see more examples of this. And I think you and I were even having this debate of RAG versus fine tuning. I feel like a lot of people are having that debate right now of like, what’s the right approach? I think it depends. That’s kind of my take on it of where you want to use what? But yeah, this is one of the most fascinating things. Honestly, to me this entire paper was like, Wait, what does that mean for RAG?

**Amber Roberts: **What like just like one sentence that makes you do a double take.

**SallyAnn DeLucia: **Literally. That’s what it was.  I always know when I make a comment like, write it out that it’s something that stuck with me? But yeah, do you wanna share your screen and kind of walk through what you’ve done with Phoenix? 

**Amber Roberts:** Yeah, absolutely. And it will be interesting to see more of the fine-tuning used cases. Once we have more open source models and a waste of training, because for the audience, like SallyAnn and I were also just talking about how you really don’t have to use anything besides these large third party LLMs for a task like summarization or content creation because they are very good. The problem is that they are expensive, and especially if you’re just using it for like a single task, and you’re using it like once a week, it may or may not be profitable. You just might not be making enough money on that task like for your company, based on what you’re paying to these large companies all the time. 

So we’ve already seen the smaller versions of the models. And these open source models for this very specific task. And I think we’re just gonna keep seeing more and more of these models. And then the evaluations are gonna be based on alignment. Because if you can get a similar alignment with these smaller free models that you have control over, I think it’s gonna be disruptive in the space. But right now, third party LLMs, and OpenAI and Anthropic like, they’re very much beating what’s available open source for now.

**Amber Roberts:** All right. So I see some users. Some Phoenix users that are actually in the audience.

So Phoenix is Arize’s open source solution for AI observability. Essentially, if you’re using LLM callback systems like LlamaIndex or Langchain. If you’re building any LLM application system, every time you interact with an LLM, each interaction is documented in a callback system by a trace.

And so you can send all those traces to Phoenix, and it can collect all that information. And we also have released projects where you can divide up essentially each aspect of that LLM application and be able to look at it for projects.

But I wanted to go through an example of taking this trustworthy LLM paper and seeing like, say you have any research paper essentially, and you want to build a RAG system on it. So we’ve seen examples of, okay, I can take this paper. And I could build a QA system on it, right? And I could start interacting with it.

But what if you wanted that system more aligned? And you actually wanted to be able to see like, where are the answers that I’m getting? Are they hallucinated? Are they good? Can I get explanations for it? And can I also easily get like the reference material that generated this question/answer pairing and look at the evaluation.

Arize and Ragas did a recent event. And it was really nice using Ragas, which is an open source framework for RAG application specifically.

I’m not gonna run the whole thing. But this is available on our Phoenix documentation. So if you look at RAG use cases, if you have a RAG use case, you can use this notebook from our Phoenix documentation, and you can get a better understanding of tracing of evaluations.

And we just have about five min so essentially like you can load in whatever document you would like. And then you can implement Ragas and implement either a LlamaIndex or LangChain, because you do kind of an orchestration system for actually building that LLM application.

And then what’s really nice with Ragas is that it will generate the question, the answer, and the context. You can also select, if you want, like a simple zero-shot kinda effort on this generating of question, answer pairs, or you can make it more of a reasoning. So a little bit more sophisticated that uses more of a chain of thought prompting.

But essentially what you can build by leveraging these different open source like different open source tool. I did use OpenAI for my LLM–I used GPT-4, but you can use whichever LLM that you’d want, and the way that this would show up in Phoenix. If you want to use the Phoenix UI, you can still use the notebook. If you want to use the Phoenix UI, it will break up the creation of that test set.

So the test data is set. That’s gonna be alright, I’m giving it this document. Ragas is going to give me the questions, the answers, and the relevant content that created those you can also use. Sally Ann mentioned. We have pretested evals in Phoenix, like ones like hallucination, toxicity. We’re adding more and more every day, or you can make a custom one, or you can import evals from a second library like Ragas has its own evals.

And once you have all that information, you can send it into a project in Phoenix, where now you have your LLM system essentially documented. And this is the AI observability component. And yeah, this is essentially like gaining alignments on a RAG system that’s based on alignment.

So it’s a little meta in the alignment on alignment side, but you’re like, why not just show how to do this? Because when teams ask: Oh, how do we know that this LLM is working? It’s not so much about latency and token count and cost anymore. Now, we’re actually looking at performance. And not just oh, like, did they end up purchasing the product? Yes or no. But do we have correctness? Do we have something like faithfulness, and this can be you can have your own fairness and bias ones.

I just ran Harrison Butker’s speech and an LLM, you know, made the evaluations for misogynistic and like homophobic evals. Just based on a very objective prompt that a different LLM made. So the LLM made the prompt to the evaluations. And it’s just very interesting to see kind of the breakdown, and you can add any additional evals that you want. And what’s nice is you don’t even have to create them yourselves. You can have an LLM create them, and then I’ll evaluate them.

I know, SallyAnn like you’re in the process of working with co-pilot and working with LLMs that evaluate LLMs that create content to train LLMs. And so, yeah, it can get a little bit in the weeds and a little bit meta. But I think that’s why using models that are already aligned to do a lot of these tasks is a really good argument for why it works.

**SallyAnn DeLucia: **Totally, yeah. I think evaluations really at this point are like our best tool when it comes to improving all ones. You have so many options like you were mentioning. There’s so many ways to get you started without having to do any of the work. And then you can really start defining those custom emails when it becomes appropriate. And this is just really what’s gonna give you insights on your model to actually make better experiences for the user drive business, all of those important things. So yeah, we’ve got some exciting stuff in the works on our side, for evals but excited to see more and more papers. 

Aparna and I did one a few weeks ago about kind of this eval framework of being able to generate labels. And I just think there’s a lot being invested in this. And there’s a reason for that. And it’s because they’re so powerful for assessing LLMs.

**Amber Roberts: **We do have a few colab notebooks as well. If people are interested on creating that golden data set, having it labeled, having the explanations in place, and then, when you put it into Phoenix, you can look at each trace which is each execution of an LLM. You can look at the input like, oh, how do LLMs show their understanding of deriving the causal relationships from blah blah blah.

And like this was in the paper, the output. And so anything and generate these inputs and outputs like for question answering pairs. But the fun thing is like being able to look at evaluation scores that you control yourself, and being able to look at the full like retrieved documents that are responsible for answering this as well as an explanation for why this response is a good response based on that content.

So really, there’s a lot you can do with the power of LLMs. And it’s really fun to see where this field is going in general.

**SallyAnn DeLucia:** Absolutely. We’re just at time. We appreciate y’all for joining us. 

I think there might be one question. Maybe we can hit it quickly. So this question here is, as you know, culture, political norms, consistent changes. What is the best mechanism to keep foundational LLMs updated? Would that be updating evals, updating RAG docs? And finally retraining? My take on this is, it’s probably going to be a little bit of everything. You know the LLM engine providers, they’re gonna keep releasing new models that are gonna be a little bit more up to date than the last one. So that will help us there. You know, updating emails is definitely important. You’re gonna wanna iterate on your requirements. Your alignment requirements might change over time.

So you’ll definitely want to update your evals accordingly, keep your knowledge base up to date. I really do think it’s probably a combination of all of this until you know, I think the inevitable is where these LLMs probably become real time in their knowledge. But yeah, that’s my take, Amber.

**Amber Roberts:** Yeah, I think with us. And that’s the thing with these companies that are the foundational LLM companies. You’re not going to be able to update those yourself, or even know exactly what went into them. So the companies will continue to have these really large models that they’re training themselves, and that we, you know, any company that’s leveraging them will not be retraining. 

But having a system like Phoenix really helps surface up those areas when you say, like, Oh, should I update the RAG documents that are being used? Should I update the material or generate more material? Not a lot is shown in retrieval evals. So am I getting a hit? Am I having good retrieval evaluations cause. If you’re not having good retrieval evaluations, you’re probably not having a good response situations from your LLMs.

So I would say, implement an AI observability system, and then anytime, you get an indicator of something going wrong for those emails. Then that’s when you start troubleshooting. Because it’s the same with any personalization recommendation systems that you get. They can start becoming very annoying to the user, like recommending the same thing or recommending things they already bought or don’t need. And what you have to do as the engineer is figure out how do I adjust this? And so, as more problems come up, you’ll get more solutions.

**SallyAnn DeLucia:** Totally. That’s a good point that you’ve asked can be your signal, for when you need to do those things. 

There’s one more question. They’re asking if we’re afraid for LLMs to be overcorrected and become disified. I think that means just that kind of way back to like over censoring things.

I’m not personally really worried about this. I think that the teams at these LLM providers are really doing a great job at kind of showing that line of what is misuse and what’s not. I don’t think that we’ll we’ll see them get to a place where they would essentially become, you know, useless if if they went too far. Yeah, your thoughts Amber?

**Amber Roberts:** I’m not worried about the same SallyAnn, but I’m not worried about LLMs at all, because it’s really the prompt that it’s doing. LLMs are going to make mistakes by like making up an additional step to take if it’s already defined in the prompt like they might hallucinate and like have a different interpretation of that prompt, but there’s so much testing. And SallyAnn, the red teaming you mentioned going on at these companies, always errs on the side of caution, and that’s that alignment aspect that we were talking about.

So yeah, I’m not worried if this kind of over done, it’s probably traced back to the actual prompt that was put in by an engineer.

**SallyAnn DeLucia:** That’s a great call out.

Awesome! Well, I think that’s it. I know we’re a little bit over. Thanks everyone for sticking with us here, and and joining us. We’ll see on the next one.
