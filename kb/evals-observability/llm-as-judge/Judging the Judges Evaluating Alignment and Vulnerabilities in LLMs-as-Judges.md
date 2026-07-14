---
title: 'Judging the Judges: Evaluating Alignment and Vulnerabilities in LLMs-as-Judges'
topic: evals-observability
subtopic: llm-as-judge
secondary_topics:
- product-engineering/security
summary: Analyzes vulnerabilities and alignment issues in LLM-as-judge systems, with
  implications for production evaluator design.
source: arize
url: https://arize.com/blog/judging-the-judges-llm-as-a-judge/
author: Sarah Welsh
published: '2024-08-16'
fetched: '2026-07-11T04:49:36Z'
classifier: codex
taxonomy_rev: 1
words: 7887
content_sha256: 3cfa721ac9a7f094e7a793e62d4cc9d719654e80d971361dd66051f6cf1844da
---

# Judging the Judges: Evaluating Alignment and Vulnerabilities in LLMs-as-Judges

## Introduction

This week’s paper presents a comprehensive study of the performance of various LLMs acting as judges. The researchers leverage TriviaQA as a benchmark for assessing objective knowledge reasoning of LLMs and evaluate them alongside human annotations which they find to have a high inter-annotator agreement. The study includes nine judge models and nine exam-taker models – both base and instruction-tuned. They assess the judge models’ alignment across different model sizes, families, and judge prompts to answer questions about the strengths and weaknesses of this paradigm, and what potential biases it may hold.

## Watch

## Listen

## Dive in

## Analysis

** Introduction: LLM-as-a-Judge**

**SallyAnn DeLucia: **Hi everyone I’m SallyAnn, I’m a Senior Product Manager here at Arize. Today we’ll be doing a paper reading for Judging the Judges. So evaluating the alignment and vulnerabilities with LLMs as the judges.

With me today I have Julia.

**Julia Gomes: **I’m Julia. I’m also a Product Manager at Arize focusing on the LLM observability component. And I’ve been here for a few months. This is my first paper reading, so I’m really excited to dive in.

**SallyAnn DeLucia:** Yeah, I think this is a really great one and paper, actually, I think you found and you surfaced to the group so I think it’s really great. So with that, we’ll jump into it. As we go through the paper. We love these to be interactive, so feel free to drop us messages or questions in the chat or the Q&A. We’ll be monitoring it and answering questions as we go, and we’ll try to save some time at the end to answer questions as well.

Alright. So for today’s agenda, we’re going to start off by just giving a little bit of an introduction to LLM as a judge, just in case anybody’s not familiar with it, and then we’ll go through the experimental setup of this paper, and then we’ll finish off with an analysis, the results and just the practical takeaways

So I feel like LLM as a judge is definitely a popular topic today in the generative AI space. In case anybody here is not familiar with it, LLM as a judge is a way to kind of evaluate your LLM responses using another LLM.

So the real problem with evaluating an LLM Is that trying to do human evaluation is expensive, it’s time consuming. And it’s just all around impractical. You can imagine, you have a system running and trying to get a human evaluator to kind of sit there, read through all the text–because you know a lot of times these are generating lots of text–read through it and decide whether or not it’s correct. It’s just going to be very time consuming.

So the idea is to have the second LLM, oftentimes the same LLM, or maybe a different one smaller version, perhaps evaluate the responses. And this will often be through binary labels.

That’s a practice that we at Arize believe in is using these binary labels, like good or bad, or incorrect, correct to evaluate whether or not. So oftentimes there’s a prompt like we have here as an example of one where we’re maybe giving it the text. And then we’re determining whether or not it’s toxic.

So this is actually a toxic eval that we’re doing here. We do have a ton of examples in Arize. If you’re curious, we have a whole evaluation package through Phoenix. And so you can take a look there, and look at some examples that we have built, but of course you can always do like a custom judge, too.

Julia, anything you want to add here. Anything that I might have missed?

**Julia Gomes: **Yeah, I think that covers it really well. And I was just gonna add that we do have all these examples over [here in this library](https://docs.arize.com/arize/large-language-models/catching-hallucinations/arize-evaluators-llm-as-a-judge). And it’s very versatile. You can do hallucinations, summarization, toxicity evals. And there’s even SQL generation eval, so it’s just a very versatile method that we use a lot at Arize.

**SallyAnn DeLucia:** Totally. And you know, if you’re curious, like what those packages, it’s really the prompt that changes there. And you’re just gonna pass that to whatever LLM, you want to use. But those are some really great examples if you’re wanting to get started. 

Alright cool. So now we understand what LLM as a judge is. Again, the whole premise of this paper, you can see here. The goal is to evaluate the strengths and weaknesses of LLM as a judge. So there’s a lot of talk on the effectiveness of this or exploring different methods of doing this. This paper really wants to understand, what are the strengths? What are the weaknesses of using this approach?

And so what they use as their data set to do this is the Trivia QA benchmark. So it’s about 400 examples of 95,000 QA pairs, or from, you know, 14 trivia and quiz leak websites. So on the side here we have an example where you can see you have a question and answer, and there’s also an excerpt that’s kind of like reference tense text. You can think of it that way. That contains information on how to answer.

So they actually chose the cleaning samples where the inter human agreement is high. So that 96% range, and so they’re going to use this as the basis and we’re going to talk a little bit more about the different types of models they use and how they set up the experiment. But kind of the cornerstone, if you will, of this experiment is this Trivia QA Benchmark. This is what we’re going to have our task me on, and what we’ll have ultimately that one judge on.

Julia, I have a question for you. Something that I thought was curious is their choice to only use this Trivia QA benchmark. I see the pros to this, because it’s like just a classic question answering dataset. It’s kind of got a nice variety to it. It also has these excerpts in it. But I’m curious what your thoughts are on this choice of data set are?

**Julia Gomes:** Yeah, I thought it was interesting. I mean, first of all, they chose a much older data set. This is from 2017 back when you know, LLMs weren’t as powerful as we have today. So it’s a much simpler problem. And the focus there, I think originally, when they made this data set, was just being able to extract the right information from the excerpt.

So they include this excerpt when using these Exam Taker models, and see if they can extract like for this first example is the relevant part of this excerpt to answer the question. But then for this, they’re actually kind of like changing the task of it and focusing just on open, ended questions and answers for these judge LLMs without the it’s like extracting that information from the excerpt which is interesting.

**SallyAnn DeLucia:** Yeah, I agree. It’s an interesting setup here. Interesting data set. I totally agree. That was my first kind of thought when I started looking into this. I was like, this is kind of old.

**SallyAnn DeLucia: **So also that kind of conversation we have of, like the bias towards what the model’s been kind of trained on. I wonder how that impacted this experiment to choosing a data set that is so old. But just a little anecdote there.

So this is a template, we’re gonna get into it in a slide or two. But basically there are exam taker models. These are the models that they’re actually gonna have. Execute this task of answering these QA questions. So this is a template we’re kind of translating that example we saw on the last slide to this template here. And so you can see it’s giving questions and answers that the LLM is to choose from essentially.

It’s a little bit more on the setup. So again, as I just mentioned, we have exam behavior models that are going to generate answers to the trivia questions. We have the LLM judge models that will label those question answer pairs as correct or incorrect.

And then something they did is they have this idea of a baseline, and there are a few different ways that they establish this baseline.

So there’s exact match. So you can think of this as like, was the two answers, this or an exact match across them. There’s contains, and you can kind of think of that as like an overlap type of metric of like is there, you know, similar words that are contained in the answer. And then, of course, the gold standard: human labels of correct or incorrect. So that’s how they’re gonna establish their baseline.

And then for measuring alignment between judge models and humans, there’s a few different metrics they use. I think the two main ones, and they do kind of like a delta between them is percent alignment. And the Cohen’s Kappa so we’ll go into a little bit more detail of what those are I don’t know. I had never really had that much experience with Cohen’s Kappa, for example, before reading this paper. So we do a little bit of an introduction so you all will have some context on that.

And then here’s the template for, Judge. You can kind of see that this is pretty similar. I think Julie and I have some notes on how we think this prompt could be optimized. But you can see this is pretty similar to that one that we showed you on the first slide, that example from Arize where we’re saying, Okay, your task is to look at the question, and then based on the reference for having to determine if it’s correct or incorrect. So this is just sort of like labeling judge model here.

Julia, any comments on, you know the approach, or anything I might have missed for the alignment metrics?

**Julia Gomes:** Yeah, no, I think that was great. And I just want to comment. If you look at this prompt template for judge models, you can see how simple the task is– it really is a much more simple task than most tests we see for LLMs today. Where you know this reference that the LLM judge is looking at, it basically exactly matches the model response, just, you know, in capital letters, instead of various casing.

**SallyAnn DeLucia:** Yea, and it’s interesting it’s in there twice, too. So I think that’s really problematic. We want us just like its ability to discern there. But yeah, that’s a good call out

We just got a question from somebody else. They asked why, it’s in there twice. I don’t actually recall. If the paper mentioned why, they include the reference twice, or if that’s just like an artifact from the data set. Julia, do you remember reading anything about that?

**Julia Gomes: **Yeah, I think there were. There’s usually multiple references from different annotators. So I think every question will probably have multiple references.

**SallyAnn DeLucia: **That makes sense. Yeah. So it’s just in there because, you know, multiple references. And it doesn’t sound like they’re filtering out any repetitive information. They’re just kind of propagating it through. That makes sense, didn’t catch that detail. 

And then the last part of the setup is, of course, understanding. What are our Exam taker and models? What are our judge models? So exam takers? They actually have kind of two versions of models that they often use. So we have the pre-trained base model as well as instruction to chat model. So you’ll see them call it base or chat throughout the paper and so that’s what it’s referring to, either the the pre trained version or the instruction-tuned version they did try to use a wide range of model sizes, which I think is really important, and it comes up and some of their takeaways. How this impacted things and then the prompts for the Exam Taker models contained five few shot examples. So they are using few shot here for the exam takers.

For the judges they actually stuck to exclusively the instruction tuned versions. And there’s also a wide range of model sizes. So again, I think that’s important that they included that on both sides of things and then, of course, they were instructed to respond only with the correct or incorrect. A very common best practice when using LLM as a judge. And if you’re curious down there, that’s like just the full list of models they used again. They have the exam taker and the judge.

And there’s a nice range there between different types, models, different model providers. I personally feel like there’s a few that I would like to see. Added to this list, I know we just had the release of 4o, which was definitely after this paper was completed. And I also think some of the Claude models would be cool to see in here, too. So that would just be one note I had but overall, I think this is a pretty comprehensive list of models here.

**Julia Gomes: **I also thought it was interesting that they’re using a lot of the same models for the Exam Taker models and the judge models. Because I do know that there’s other papers that talk a little bit about self-biasing models so like a GPT judge model might prefer outputs from Gpt models. But I guess in this case, where it’s such a simple task of just responding with a single answer often, just like one or two words. I think in this case that probably isn’t an issue.

### Overview of Alignment Metrics

**SallyAnn DeLucia:** Totally. And that’s kind of the impression I got is they really made a call out to it, even in the paper. It’s like they tried to create this controlled environment. But I think in doing so, they kind of oversaw some of those nuance like what you’re talking about with like that bias and so I totally agree, like I would love to see some more, and when we get into the results you all will see they do some kind of overlap, but they don’t specifically, really call out, Okay, like, let’s do Llama 2 specifically with, you know, Gemma or Mistral, or or GPT-4. If there is that that overlap, that’s a really great call out Julia.

So, as promised. Here’s a little bit more in depth information on the alignment metrics. So first off we have the Delta scores. This is the difference between the score assigned by the LLM and the human judgment. So you can imagine a positive delta score means there’s the LLM scored higher than the human judgment. And then the negative delta squared indicates a lower score by the LLM, so this is kind of a comparison.

I think this is one of the easiest to grock in terms of like alignment. When they talk about alignment, I think this is another important point–alignment for them is really between the LLM as a judge and the human evaluator. If you’ve read some other papers that can mean a little bit of different things. So just as we talk about alignment, that is specifically what this paper is talking about.

Then you have percent agreement. And this is the percentage of instances where the LLM judgment agreed with the human judgment. And then, Cohen’s Kappa is a statistical measure. That accounts for the agreement occurring by chance. So we have these visuals over here.

Actually, Julia, I feel like you did a lot more research on this here, do you want to explain these visuals to folks just so they can understand what that Kappa means?

**Julia Gomes:** Yeah, so the idea here is that you have two different readers, rater one and raider 2. And let’s say, the smiley face is correct and the frowny faces they label it incorrect. So you can see the percentage of times on the right in this equation where they’re just basically both labeling it the same way due to chance. And that’s what gets you PE. So here it’s like, for rater 1–25 out of the 50 ratings they just based, like statistically half of those ratings are going to be the correct score, and then half are going to be incorrect. And then it’s slightly different for rater or two. There you have 23 out of the 50 ratings are correct. 27 out of 50 are incorrect. So just like using those numbers, you can calculate the probability that those two raters agree just due to random chance. And then you use that as PE over here on the bottom equation, and then PO is just the observed agreement.

So that would be the 17 and the 19. Those values where they’re actually just agreeing because they chose the same answers.

![Alignment metrics and kappa score overview](https://arize.com/wp-content/uploads/2024/08/Alignment-Metrics-Slide-1024x576.png)

**SallyAnn DeLucia:** That makes a lot of sense there. So yeah,  that bottom is the full calculation for Kappa. So whenever we reference that in the following slides. And that’s what we’re talking about. And then they did call out that, you know, Kappa score is more reliable than the simple percent agreement, especially when dealing with categorical data that makes a lot of sense to me.

I think anytime you try to kind of abstract too much away from an assessment. I kind of lose again that nuance. So I think that it makes complete sense to me, and I think we touched on this a little bit more on exactly kind of breaking down why the Kappa score is more reliable.

**Base Models Outperform Chat Models**

![Base models outperform chat models](https://arize.com/wp-content/uploads/2024/08/Base-models-slide-1024x571.png)

So we’ll start talking through some results. This first one here is actually specific to the exam takers. So just a call out on that. The base models outperform chat models. I think this is an important, just for you know anybody here who’s kind of setting up some tasks here that you know, using the base models might actually be the better choice.

So it seems that their explanations were that the chat models have a worse understanding of the particular prompt format which is tuned more to fit. You know the base models? And that the chat models have, you know, unlearned some of their alignment or some knowledge during their alignment training. So we have some graphs here, you kind of see, I won’t spend too much time, because I think that the real point of this page where it is talking about judge models.

But you know, we felt like it was important to call this out so you can see just looking at that first one–this is just Llama 2, and you can see the difference between you know the base and the chat, and it’s kind of tricky. The Y axis here is the number of incorrect answers. So it looks. Maybe sneaky. That’s a higher number of incorrect and that’s for incorrect entity under specified to the main entity. So it’s doing it across a few different axes here.

**Julia Gomes: **One interesting thing. It’s just interesting to think about when it’s more appropriate to use base models versus chat models. To kind of keep in mind that a lot of chat models are designed to be better at either doing specific tasks or having a more conversational style. I think in this case, since the task is just answering a question with a few words, and not in a conversational style. Ideally, I think that’s also why the chat models tend to be performing worse in this task.

**Only the Best LLM Models are also Good Judges**

**SallyAnn DeLucia: **That makes a lot of sense, really great call out there.

So I think personally, this is one of my key takeaways from the paper I could give, or take all the other information there. But this is I think, one of the key things, which is that only the best models are good judges.

So of the nine LLM judges only GPT-4, Turbo and Llama 3 70 B showed very high alignment with humans. So again, alignment is that concept of how much overlap there is with the human judgment. And you can see kind of on that visual there that honestly GPT-4 is not too far behind human. We call it here that it’s 12 points behind.

And I think, Julia, we were chatting about this earlier that you can see that that percent agreement is kind of really close. So it is way more aligned than maybe one might think. And you can kind of see, you know, Gemma, smaller models here, not performing as well. Mistral is kind of in the middle there and then, you know, we have our Llama model shortly after GPT-4. So what we would commonly think of as our best models, are ones that they feel are best fit to be judges.

![Best models from the paper chart](https://arize.com/wp-content/uploads/2024/08/Best-Models-Slide-1024x570.png)

**Julia Gomes:** Yeah i’m looking at Figure 1 (a). You can definitely see that, like  the red dots of GPT-4, they’re pretty much perfectly matching up with the human scores that are in black. For across all the different Exam taker models, which is really interesting, rest like, if you look at like Gemma. 2 B, like the scores are just all over the place, like they don’t correlate with the human very well at all.

**Kappa Score is Better than Percent Alignment**

**SallyAnn DeLucia:** Yeah, totally. 

So this is kind of what we were talking about earlier. Kappa score is better than percent alignment. So in this visual here, you can see we have percent agreement. And then we have the Cohen’s Kappa.

![Kappa score](https://arize.com/wp-content/uploads/2024/08/Kappa-Score-1024x580.png)

You can see there’s kind of these vertical colorizations as well as coloring of the points. I’m calling this out only because it took us a little while to understand exactly what they were trying to tell us with this chart. So each of those points are colored by the judges. And then each point represents one of the exam taker models.

So the Cohen’s Kappa distinguishes judges better than percent alignment. So again, it just has that better ability to distinguish.

For percent agreement there are deviations up to 20 points in evaluation, scores for similar capital alignment. And the scores aligned, or even the best judges. Models can differ up to 10 points with human assessments or human assigned scores.

So, I think the tldr; here is like, if you’re going to perform any kind of assessment on your LLM judge, you’re probably going to want to use the Kappa score. It just gives you a little bit better understanding of exactly how well your judge is doing compared to your human evaluator. I think that’s the main point I take away.

But, Julia, any other thoughts you want to add here?

**Julia Gomes:** Yeah, totally agree there. And they even kind of give this threshold that they recommend where it’s like a Kappa above 10.8 shows that it’s very well correlated and aligned with humans. And they do these little vertical slices. So this vertical slice, where they have that near perfect alignment in blue. You can see a lot of the GPT-4 judges are falling in that category. That delta score is in a fairly narrow range around zero, which kind of shows the alignment, and you get a much wider vertical range. If you look at the percentage agreement chart on figure 1A on the left.

**SallyAnn DeLucia: **Yeah, I think it’s way easier to discern on the Cohen’s agreement, like, really, the differences between models, as you’re saying, like, it’s all kind of smushed together. It might almost appear that like, Oh any of these models does fairly well with that agreement. But when you really break it down, using Cohen’s Kappa. You called out that in your perfect agreement slice, and then you have kind of all of these slices. It just is a much, I think, better way to to understand their performance, for sure.

![human rankings graph from paper](https://arize.com/wp-content/uploads/2024/08/HUman-rankings-slid-1024x569.png)

Alright, so for this visual here, I think another one of their key takeaways is that LLM judges align well with human rankings.

So the judge models may not assign identical scores as the humans, but they are lined in ranking the exam model takers. So this is where they’re ranking again, you know, which of those models is better.

And so the judge model struggled to distinguish between poor performing exam taker models. I thought that was kind of interesting. That was like it was hard, and maybe could get the best ones, but then, when it got to kind of those worst ones, it struggled a little bit to be like exactly which one was truly the worst. And you can kind of see that, I think, with like the zigzag of those that bottom set.

And then contains demonstrates the highest alignment with the human ranking. So swapping them ranks of only two of the nine models there so again contains is just kind of that. It’s not a strict exact match, but it’s more of like that overlap of like. Is there some overlap between the responses there.

**Julia Gomes:** So this also demonstrates again, just like, how much of a toy problem this is.  Because, like in the real world, if you’re using judge LLMs like contains is not going to perform better than any of the judge LLMs. For, like a task like, you know, evaluating toxicity right? It just isn’t capable of doing that. So I think, yeah, the fact that contains is doing so well on this means that we really are in a toy setting.

**SallyAnn DeLucia: **Totally. When I first read that they were doing like exact matching contains. I just was like, exactly what you’re saying is like you wouldn’t use that in most settings unless it was some kind of generative task where you were trying to compare like a gold standard answer. So I definitely agree, that is definitely evidence of a toy environment here.

**Position Bias**

**Julia Gomes: **I’m just gonna walk through a few more of these. 

One common problem that they were seeing that I think has come up in other papers as well is position bias.

![Position bias overview](https://arize.com/wp-content/uploads/2024/08/Position-Bias-Slid-1024x568.png)

This actually goes back to the references that were mentioned earlier. So here we’re looking at an example of what the prompt was that was fed into the judge LLM. And we can see in these two different cases the references which are the annotated human answers are in two different orders and the model response is Granite City.

In one case, Granite City is at the bottom, and it says, the Granite City at the top. And then the judge says that this is incorrect, because the reference order is in such a way that the granite city is at the bottom. Whereas in the other case the matching answer, Granite City is at the top, and then the judge output is correct.

So just changing the position of the references when feeding this to the judge LLM actually changes the judge’s output. And an interesting take away here is this tends to happen more if the judge is more likely to to identify the correct answer if the reference is at the top of the list than at the bottom, and this is also only an issue with the smaller models. So, larger models don’t get confused by this like GPT-4 doesn’t usually get confused by this, but for the small models in this case, Llama 2 7 B. It is getting confused by these cases.

Anything to add SallyAnn?

**SallyAnn DeLucia: **No, I think I think this was interesting. I think you hit on the most important part here is just the large versus small. I think that was something that was really interesting, and perhaps something to kind of keep in mind, as we think about the smaller models for evaluation tasks. Specifically, I guess, how we structure their prompts.

**Julia Gomes: **Yeah, this is sort of adding on to it. It’s kind of like explaining why we’re observing this in small models, and I think the authors of the paper kind of hypothesize that small models just ignore the reference. And they’ll often just kind of use internal knowledge. So here’s an example where the question is:  The oldest known American cocktail, what whiskey forms the base of the cocktail known as Sazerac?

And then there’s a bunch of references that mention rye. But then for this smaller model, it thinks that the correct answer is Bourbon whiskey, because it’s just using its own internalized knowledge rather than looking at the references. So it just kind of fails to capture all the information in the prompt.

Another interesting thing, and I think this has come up in other papers as well, is that LLM judges have a leniency bias.

![Leniency Bias](https://arize.com/wp-content/uploads/2024/08/Screenshot-2024-08-16-at-12.54.55 PM-1024x572.png)

So there’s a few definitions on the left. So there’s this value PC. Which is that the judge assigns the correct judgment with the probability of PC. And then there’s this other value of P Positive, which is the judge assigns the rest of the samples to be correct. With just this probability, P Positive. And in the appendix they’re able to actually do these calculations. It’s quite long.

So I’m not going to go into how they’re deriving those numbers. But as you can see here, for P Positive, we would expect that just to be 0.5, we wouldn’t expect any bias, basically. So it should assign randomly whether or not the samples are correct versus incorrect. But here we’re actually seeing that it tends to be above 0.5. So for, like, especially for the small models for Gemma to be. We have a value of 0.8. For GPT-4 turbo it’s not as extreme. It goes down to 0.6.

But in general, the judge models just tend to be lenient and tend to agree with the Exam taker output

Anything to add SallyAnn?

**SallyAnn DeLucia:** Yeah, I think this is one of the interesting points I, personally would be curious like we. We looked at that prompt at the very beginning. It’s a very basic prompt. I wonder if there’s some things we can do like just with prompting of like prompting it like, if you’re unsure like, you know, responding later, and that might not also be good. But I definitely think there’s some implications of this especially if you’re using this, you know, to evaluate your LLMs. So I think this is something definitely to consider.

But I would be curious to kind of even see some future research on what may be the best way is to overcome this, and how different approaches help.

**Julia Gomes:** Yeah, I remember also, like, when I was going through the appendix, like they have the prompt that they give to the humans. And I did notice that it’s much more detailed than the prompt that they give to the judge models. And they’re kind of telling the humans how to handle cases where it’s like partially correct or other sorts of issues, whereas, like they don’t give that information to the judge. So I definitely agree with you that that could kind of account for some of the leniency bias.

**SallyAnn DeLucia: **Hopefully. And I think that’s something you and I talked about a lot is just like some of the prompting. I think they gave the LLM very little, and I always say with a prompt like, if you, if you can’t expect a human to understand what you wanted to do with your prompt. The LLM. Is totally not going to get it. So that’s a really excellent call out that like, okay, they’re giving so much information, such a detailed instruction to humans. But they just choose not to do that for the LLM judges. So yeah, good call out.

**Julia Gomes:** They also did some analysis on the types of errors that the LLM. Judges were making, and it seemed that LLM judges are better at error, recall than precision. And also depends on the size of the model. So here, on the top right, we can see how the performance in terms of like capital alignment in black. How it just kind of linear, linearly improving as we increase the model size from like Llama 2 B over to the best performing model. GPT-4.

For recall the line in blue is also following a similar trend, whereas we increase the model size. We also are getting that better performance and alignment with respect to humans. But then for precision, it’s just kind of this flat line and kind of random. So that doesn’t seem to be improving. And we can see that the correlation coefficient over here is like .003. Precision is just not well correlated with human alignment.

And a lot of this is related to false positives, where we falsely label the correct examples as incorrect, and that just seems to be happening across the board, whereas false negatives, where we falsely label incorrect examples as correct. That seems to be like we’re able to drive that down by improving the model and moving towards a larger, better model like GPT-4.

**SallyAnn DeLucia:** Yeah, I think this is another one of those areas where I’d love to see some research on, like, maybe how we can improve this to better handle these situations.

**Julia Gomes: **Yeah, totally agree. 

We also noticed that that judges failed to recall under specified air types specifically, so here they actually asked the humans to annotate the types of error codes so in this example, there’s a question that is: Excluding Lady Jane Gray, who were the five monarchs at the house of Tudor? And then there’s supposed to be this list of five answers, Henry, Henry, Edward, Mary, and Elizabeth.

There’s different types of ways that the models can get this wrong. So it could be that there’s an incorrect entity. So the response refers to a wrong entity. That’s like the 1st example on the top. And we’re seeing that, judge models like GPT-4 are really good at recalling this.

But then, when it comes to things like under specified answers. So here they’re listing Edward, but they’re failing to say it’s like Edward the 4th. When they have these under specified answers, that’s when the models tend to be more lenient and even though they should be saying that this is incorrect, they tend to label it as correct.

And it is a really tricky case, right? Again the humans are prompted to actually be able to label this as an incorrect answer, if it’s under specified with some examples, whereas the judges didn’t receive that information in most cases.

But it’s these underspecified answers, particularly that we see that the judge LLMs are struggling with the most. Anything to add SallyAnn?

**SallyAnn DeLucia:** No, I think you covered everything there.

**Julia Gomes:** And then the last thing we want to discuss is the sensitivity to prompt guidelines. And so that’s something we brought up a few times, and in one experiment they actually did experiment with feeding in different guidelines to the judge LLMs. 

So we have these guidelines over here which is, without guidelines. I mean, it’s all without guidelines, which is just much simpler, and you can see the prompt right here. This is the prompt we’re looking at before, which is kind of like two sentences explaining what the task is, and then the question, the references, and the model response.

And then they also do have an example of detailed guidelines that they gave the LLM, so here they’re actually explaining in four steps what to do in different types of edge cases. For example, given the model response, only consider the parts of the response answering the question and ignore any extra text.

And then, in this last prompt it’s guidelines with examples. So here they actually explicitly mention under specified answers. So, the example here is December versus December 20. If the model only says December instead of December 20, which is correct, then it should be marked as incorrect, so they do experiment with different types of prompts in this last experiment.

And yet the results are interesting, because it seems like the bigger models like GPT-4. They are benefiting from those extra guidelines and the extra detail. Whereas the smaller models, they actually get confused by the additional detail in those prompts. So that’s just an interesting takeaway that it really depends like the prompting style really depends on the model that you’re working with.

**SallyAnn DeLucia:** Totally. I think that’s something that, like I would have loved to see them again, maybe expand on even how they did this, how they determine what guidelines they use to even establish their prompts. Because something like that we know, that’s talked about a lot. Is that like, yeah, different models respond differently to different sets of instructions, different prompting techniques.

If anybody here is building an application, if you switch your model out, most of your prompts are going to end up breaking so it would be interesting to you to to kind of see that kind of indexed on, I guess, a little bit more, and maybe giving a little bit more specialized instruction based off of the model type. Because that’s just a nuance of how these models work–the same prompt just doesn’t work for the same or for different models across the board.

**Takeaways: Judging the Judges**

My takeaway still, after reading this, and reading other papers, and even just seeing it in practice. I still feel like LLM as a judge is the best way to evaluate your model, even if there are small discrepancies in alignment.

It’s going to have a high success rate. You know, we saw it was like 84% versus 94%, or like 97%. And that’s still pretty high, and it’s gonna save a ton of time and money. I’m still not gonna want to have to read through all of my LLM responses and try to judge them by eye, or just by reading through them. So, I think that LLM as a judge is still the best way to go.

I did think that again, one of the key takeaways from this paper is that using best in class models is going to be your best bet for using an LLM as a judge.

And then I wanted to make a call out that, you know there are a lot of research papers out there that you can actually improve alignment by doing things like using assertions or criteria and some of the things that, like Julia and I talked about today. So I do think that it’s worth calling out that while they took a very I guess they tried to be very clear with their experiment set up and try to make sure that you know, they have a good controlled environment. I think there’s some things that you can do just in a more practical sense that will improve that alignment.

And then just some follow ups that I’d like to see like we now have 4o, we have 4o mini like, how does that do here? I think we personally have seen a lot of great success with 4o mini like it’s been doing really awesome with evals. So I would love to see some testing there. I’d love to see different testing for prompts for different models again.

I’ve experienced this. You know, we just recently released copilot, our AI assistant. And you know, I ran into the issue of like. We swapped out 4 for 4o, and it broke everything, and that’s in the same kind of model family like I as you work with different models, and something I’m actually trying to solve for right now is just like when you have these variety of models from different providers like the prompts need to be different. And so I’d love to see more testing around that.

And I’d like to just see more prompt optimization. I think there’s some stuff they could do there to kind of improve the performance of those judges. But yeah, Julia I want to see what yours are.

**Julia Gomes: **Yeah, my takeaways are honestly quite similar. I mean, the 1st one is prefer large models. Judges. So they were looking at GPT-4 Turbo and Llama 3 7 B specifically and showing that those have really good alignment. But yeah, maybe we shouldn’t be saying large models just, but just the top performing models. Since 4o Mini, like you’re saying is also really good, and it’s a smaller model that might actually perform just as well if we were to test it.

And then, yeah, if you’re using a smaller model, I thought, it’s interesting that in that case you might want to prefer shorter prompts, whereas for larger models, having the more detailed instructions, will always help.

And then the other thing about evaluating LLM judges, I did think it was interesting to start looking at Kappa score instead of percent alignment, which is what I think most people would do by default. So it would be interesting to start using that metric some more.

And then also, in terms of prompt optimization. I definitely think you know, the first thing that LLM judges do have this issue around under specified answers, then I think it’s probably helpful to specifically in the prompt explain how to handle those types of edge cases to kind of avoid that failure mode. I’m not sure if it would totally resolve it. But you know it might be that if you just give the alum judge those specific instructions to mark under specified answers as incorrect, then that wouldn’t be a problem.

And then, yeah, the last thing I just want to note is that this is definitely a toy setting, in practice we wouldn’t be using LLMs a judge for this type of use case, we’d probably use it more for something like toxicity, eval or hallucinations. So because of that, we don’t know if these takeaways from this paper necessarily will scale to those other use cases that we see in practice. So, it’s kind of important to try this again on your own data, and you know, take the takeaways with a grain of salt.

### More About Cohen’s Kappa

**SallyAnn DeLucia:** I think that’s another thing I forgot to add, there is like I definitely like to see more ambiguous and open end tasks be tested here. Cause you’re absolutely right like this. This toy setting. It’s hard for us to kind of take this and translate it to what we’re doing in the real world or in production settings. So I totally agree, I’d love to see that.

Yeah, cool. Well, that’s the end of the reading. I think we can do a call for questions again, either in the chat or the Q&A. We’re happy to spend some time answering them. We’ll give folks a few minutes to submit any questions.

Yes, we can share some more information on the Kappa score. Julia, you want to pull back up that slide? We can just go over that.

So I think it’s really just a statistical measure that accounts for the agreement occurring by chance, so I think that’s one of the main takeaways there, so again, we have this kind of visual here. And so we have, you know, two graders, if you will. And they have the smiley face, sad faces, as Julia explained. It’s like basically correct or incorrect.

And so what they’re doing is first taking just that probability by chance. And so that’s what that PE is going to be.

So they’re looking at like where their agreement was, and just doing this kind of statistical measure there. And so the top is kind of illustrating where that PE comes from, and then the Kappa calculation is below there.

So we’re taking the observed agreement or subtracting that expected agreement by chance, and then just doing that statistical calculation. But, Julia, you explained it better the first time.

**Julia Gomes:** Yeah, I think that explained it really clearly. And I guess one idea that I’m kind of seeing in this is that each reader may kind of have their own bias. So this rater labels it as correct 25 out of 50 times, whereas the other rater labels it correct at 23 out of 50 times, and we just kind of assume like this is just the natural inclination of these raters, and then by chance the probability that they both label as correct is just 25 out of 50 times 23 out of 50, and that’s you know you do it for both correct and incorrect. And then you get that just probability that they agree in general.

**SallyAnn DeLucia:** Yeah you got it right there. So it’s a comparison to random grading. It’s and to answer the other question we have there is like, do other evaluation metrics take into that agreement by chance? Not really. You can see like percent agreement, as Julia mentioned, is probably the most common way to kind of assess human versus judge. And that’s just simply looking at like how much overlap there is. 

How many times did the LLM agree with what the human said, and I think we see that a lot when we’re reading and and seeing, you know content being put out about, you know, like LLM as a judge versus human evaluators.

And so I think that the Cohen’s Kappa that’s why it’s so promising. That’s why this paper really asserts that that’s the way to go. Because there is this assessment of random grading that is important if you’re really going to objectively assess the performance here.

**Julia Gomes:** I would add that it didn’t make too much of a difference. So it’s going back to like–even though it’s a key point of the paper–if you look here like the percentage agreement other than these first examples, Gemma 2B versus exact match. The trends are the same between percentage agreement and Kappa scores like humans have the highest agreement and also the highest Kappa scores. And then you know as you go down to GPT-4 and worse models you just see those same trends between the two.

**SallyAnn DeLucia: **Yeah, that’s a really great call out, so I guess we can kind of take away that chance, the random grading chance, might not have as big of an impact there as you might think. 

Well, thanks, everybody for joining and we’ll see you next time.
