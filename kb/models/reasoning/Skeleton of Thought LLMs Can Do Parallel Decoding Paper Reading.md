---
title: 'Skeleton of Thought: LLMs Can Do Parallel Decoding Paper Reading'
topic: models
subtopic: reasoning
secondary_topics:
- inference/optimization
summary: Summarizes Skeleton of Thought and how parallel decoding can speed structured
  reasoning.
source: arize
url: https://arize.com/blog/skeleton-of-thought-llms-can-do-parallel-decoding-paper-reading/
author: Sarah Welsh
published: '2023-08-24'
fetched: '2026-07-11T04:47:37Z'
classifier: codex
taxonomy_rev: 1
words: 5542
content_sha256: c49cec6d6346b49b63b6f9c101ceacda9162b0ebe466063415a7b4a43a6c890a
---

# Skeleton of Thought: LLMs Can Do Parallel Decoding Paper Reading

![Community Paper Reading - Xuefei Ning & Zinan Lin blog (2) Xuefei Ning and Zinan Lin, Skeleton of Thought authors](https://arize.com/wp-content/uploads/2023/08/Community-Paper-Reading-Xuefei-Ning-Zinan-Lin-blog-2-1021x560.jpg)

              # Skeleton of Thought: LLMs Can Do Parallel Decoding Paper Reading

## Introduction

Join us for an exploration of the ‘Skeleton-of-Thought’ (SoT) approach, aimed at reducing large language model latency while enhancing answer quality, with the presence of two authors, Xuefei Ning and Zinan Lin. SoT’s innovative methodology guides LLMs to construct answer skeletons before parallel content elaboration, achieving impressive speed-ups of up to 2.39x across 11 models. Don’t miss the opportunity to delve into this human-inspired optimization strategy and its profound implications for efficient and high-quality language generation.

Join us every Wednesday as we discuss the latest technical papers, covering a range of topics including large language models (LLM), generative models, ChatGPT, and more. This recurring event offers an opportunity to collectively analyze and exchange insights on cutting-edge research in these areas and their broader implications.

## Watch

Dive in:

## Main Takeaways

- Skeleton-of-Thought (SoT) builds on the chain-of-thought approach that aims to encourage generative AI to showcase its presumed logic when answering a question or solving a problem.
- This method is similar to writing an outline on a given topic. The “skeleton” is another way of referring to an outline.
- SoT guides the LLM to derive a skeleton first by itself. Based on the skeleton, the LLMs can complete each point in parallel so that we get a speed up. SoT can be used to “accelerate both open-source models with batched decoding and closed-source models with parallel API calls.”

## Transcript

**Aparna Dhinakaran, Co-Founder and Chief Product Officer, Arize AI:** Awesome. We’ll give a couple of minutes to let everyone hop into the Zoom here. Okay. Looks like we have folks joining in, so maybe we can get started. So today we have a really cool version of the community paper reading, because we actually have the paper authors joining us. So we’ll actually get to ask all the questions that we have at the end of the paper to the authors directly.


So really excited to welcome both Xuefei and Zinan who are the authors of the Skeleton of Thought: Large Language Models Can Do Parallel Decoding paper. The link to the paper is linked in the webinar, so you can go ahead and take a look at it.

But welcome. Thank you so much for joining us Xuefei, do you want to maybe kick us off with an introduction?

**Xuefei Ning, Postdoctoral Researcher at Tsinghua University: **Okay, nice to meet you. I’m Xuefei from Tsinghua University. I’m now a postdoctoral researcher. And Zinan is a friend of mine during my undergraduate time. So we usually talk about doing research together. And by chance, we’re together doing this work. 

**Aparna:** Zinan, do you mind introducing yourself?

**Zinan Lin, Senior Researcher, Microsoft Research: **Thanks very much for inviting us, we’re very excited to be here. My name is Zinan. I recently graduated from Carnegie Mellon University. And I’m now a senior researcher at Microsoft Research based in Redmond, Washington.

And as Xuefei said, we have been friends for a long time and we’re very excited to be here, to share this work.

**Aparna Dhinakaran: **Awesome. Well, I gotta ask, how did you guys come up with the– first of all really cool title–But how do you guys come up with the idea of the paper? How did that start?

**Xuefei Ning:** Actually, the idea originates from our user experience of chatGPT. Usually, I want to find some key points and expand on those key points when I’m using chatGPT. And if I don’t see the key point I want, I actually want to rephrase my question. But I have to wait for chatGPT to output each word one by one. And for many questions I ask, for example, I’m looking for some knowledge and some inspiration. It often gives me many points, and usually there isn’t a close relationship between these points. So I wondered–why can’t chatGPT give these points out for me in parallel, and it would be much faster.


Actually, my research field is on efficiency. And I think this is like a new perspective on improving efficiency. So I discussed this with Zinan, and Zinan had some really good ideas on how to make this work using Promptly. So we started on this work after this discussion. 

**Aparna Dhinakaran:** That’s really interesting, So from your own usage of chatGPT is kind of what inspired this.

Also, I want to also introduce Sally-Ann on the call. Sally-Ann will also be here doing the paper, reading and asking our guests today a bunch of questions. Yes, Sally-Ann, go ahead. You have anything you want to jump in with.

**Sally-Ann DeLucia, ML Solutions Engineer, Arize AI**: Yeah, really, where I want to start is kind of just diving in. And I’d love for you to give an overview of the paper so we can really understand what the key pieces are here and what your findings are.  So I would say just go ahead and take it away. 

Xuefei Ning: Okay, so I’ll show my screen. Okay, I think I will use [this website ](https://sites.google.com/view/sot-llm)while I go through the key ideas. So our work actually aims at decreasing end to end generation latency. So while the major course of the high generation latency, the sequential decoding approach–Actually, this aspect is not tackled that much in the efficiency literature–we propose “Skeleton-of-Thought” (SoT), which guides LLMs to first generate the skeleton of the answer, and then conducts parallel API calls or batched decoding to complete the contents of each skeleton point in parallel. Not only does SoT provide considerable speed up (up to 2.39× across 11 different LLMs)–as we expected–but it can also potentially improve the answer quality on several question categories in several aspects, especially in terms of diversity and relevance. And we regard SoT as an initial attempt at data-centric optimization for efficiency–we haven’t seen many efforts in this direction, and reveal the potential pushing LLMs to think more like a human in a more strategic and organized way for answer quality. 

There are some background numbers that reveal how the LLM generation process is slow. For example, for API-based models it takes 22 seconds for Claude (accessed through Slack, middle July, 2023) and 43 seconds for Vicuna-33B V1.3 (a 33B LLaMA-based model, running locally on one NVIDIA A100 GPU).

We actually analyzed three major causes of an LLM’s slow inference. So the first one is caused by the model size. The model size leads to large memory consumption, large memory access and large computation workloads. And this all induced non latency throughput.

And the second one can be the same as brought by the special attention operator in the transform architecture. And many people are talking about this problem. Because this attention operation has a quadratic memory and a computation complexity. And this is especially important in training or generation of known sequence.

And the third reason is that currently almost all the LLMs decode words one by one or generate tokens, one by one. There are some people talking about this problem, but talking about it a different way. But, generally speaking, most of the literature has been addressing the first access by compressing and red designing the model, or is designing the serving system hardware.

So we asked a question, which is: can we accelerate off the shelf LLMs no matter if it is running locally or if it is an API-based model without any changes to their model to the system or hardware? So in this way, we rely on a data centric method to prompt the LLM to be faster.

Actually, our method is very straightforward. We have two stages. The first stage is a skeleton stage in which we query the LLM to first list out a skeleton, and in each skeleton point you only have three to five words. And after you list out the skeleton in this, in this second stage that we call the point expanding stage. We led the LLM to parallelly decode the content for each point of the skeleton. And for local models we just batch the decoding together, and this will accelerate the decoding. And for API-based models we issue parallel API calls.

**Sally-Ann DeLucia:** Hey quick question I’d love to stop you on this diagram, I think it’s super helpful for understanding the method here. And you touched on this a little bit. But can you explain to us all where the kind of inspiration was to come up with this method of sending in the prompts this way?

**Xuefei Ning:** Actually, the inspiration comes from how we humans think about this problem. When we encounter a question, no matter if this is a single question or complex task, we usually first establish a skeleton over how we can answer this question. Let’s just think about when we are taking a test. Taking a test we know there is a well-established protocol of how we can reply to this question to get a high score. So, we just write down the protocol, and then we search in our mind for what’s the knowledge to add to each point of the skeleton? So based on this point we just designed to first prompt in the LLM to make itself behave like an organizer. It should organize the answer to the question, and then in the next stage each LLM is only responsible for adding the content and details of one point. Actually, this is very straightforward. And we just like, think about how we humans do this work: we just ask ourselves, and then we find the knowledge needed to add to each point.  

**SallyAnn DeLucia: **Yeah, that’s awesome. I think that it helps add that context because it makes so much sense like when I read that when I was doing the paper, the first thing I wrote down was like super cool. And then the second that was like it just makes sense to think about it in this way, like that is what we’re doing. We’re breaking it down. And we should try to mimic it. I think that’s a secret there. So awesome thanks for explaining that.

**Xuefei Ning:** Thank you for the question. Now, my English is not so good. So I think this already helps me to expand on the details.  I think, actually on our website, we did not write the prompt template, but the prompt templates given in our paper. Actually I’ve finished going through our methods and the end section is the results section. We tested models and open source models that we run locally on our 3090 GPU and our A100 GPU and two API-based models.

This is the summary of our results, and the X axis to the speed up. And y-axis shows the net wing rates. with respect to the sequential decoding approach. We can see that almost all models can achieve a speed up with SoT. But many models can achieve a higher relevance and diversity of further answer quality than this equation decoding baseline. This is a very brief overview of our results. And this (at the bottom of the page) is a demonstration which echoes the very first motivation of our study. After SoT is used, we can see the points are decoding in parallel. At first we can see what the point is it gives us, and if I cannot find the key point I’m interested in, I will just stop the generation to rephrase my question. Or I will just stop the generation and say, Okay, I don’t care about the other points, I just want to know time management techniques, please give me more information. So yeah, I think this is a simple demonstration that shows the very first motivation.

Finally, we discussed the limitations. We regard SoT as very conceptually reasonable and maybe useful. But this kind of solution is not very general for different question types especially. It cannot answer math or code questions. This makes sense because before we started to implement SoT, we anticipated that it would not be very good at math or coding problems, because it’s somehow contradictory. Because SoT actually relies on the expanded details of each step to give a better reasoning, better results. SoT hopes to strategically list out of skeleton in advance before all the details come out, so this is somehow contradictory and more broadly SoT is suitable for the questions with a clear answer structure that can be planned in advance. For example, when you take a test, or when you give some knowledge or ideas. So in order to use SoT for general questions, all the types of questions, what we are thinking is that we can design a pipeline to only trigger the SoT mode for question types and descriptions that are suitable for SoT.

For example, an active case will be that when the user require a very short answer or by formulating a multi choice question, or by explicitly saying: please give me an answer in two words, should not trigger SoT and also mass and coding problems should not trigger SoT.

**Aparna Dhinakaran:** Quick question before we go into the quality of the answers. I think we had one question. I think Zinan may have already answered it, but could we jump back to just how you guys are defining this? What models did you see the biggest speed up and what types of questions do you see the biggest speed up in?

**Xuefei Ning:** Oh, okay. This detailed answer is actually in our paper. For bigger models, we can get a larger speed up, for example, in Vicuna this is not like a universal conclusion because many aspects will influence the speed up. For example, how long is the sequence it will generate in the sequential mode, or in SoT mode. But if we only sync from the hardware aspect, like a larger model maybe can benefit more from this SoT process. And why is that? Because a larger model is usually more bottlenecked by the way it is loading in the decoding process. So because it had more ways, and the decoding is like totally bounded by the way to loading from the GPU onto the GPU chip, and so like popular work, such as flash attention cannot have much, because it cannot help with the way to loading, but our sot work it batches the decoding of the points, and for especially for large models it has considerable speed up.

I think maybe looking at the model that provides the least speed up will be somehow more clear to explain how in which cases our method can speed up the generation. We cannot speed up StableVicuna because StableVicuna cannot follow our point expanding prompts. And we say that in which you just expand on this point very shortly. Do not expand on other points. But we find that StableVicuna cannot always follow this instruction. So for each point it will output a very long sequence. And this sequence names will match the overall sequential decoding, and so it cannot get a speed up.

So as long as our model can follow the instruction well, and is bounded by the way, to loading in the decoding stage, it should get a good speed.

Also, if we analyze which types of questions we can get a better speed up. And the green one marks the question types that SoT can get a good answer quality on, while the red one is the question types that my SoT, the current SoT solution cannot get a good answer quality. (See Figure 5). We can see that on the common sense knowledge generate, which we intuitively think SoT is suitable for, it can indeed get a very good average on all the models. Between all these concrete questions. So at least, I think Sot is very useful with these types of questions. If we can trigger at the correct time.

**Aparna Dhinakaran:** Got it. And actually, I think someone in the chat had a question on that: In the case where you can parallelize, how do you at the end combine all the responses? Are you guys using any chains or agentic approaches? How are you doing that? 

**Xuefei Ning: **This is a very good question because, actually, we only concat them together. It’s a very simple method, which by the way, we have discussed this many times. 

So because, intuitively for some question types, this concatenation is not that suitable, especially for the coherence of the answer. But as SoT’s main aim is at decreasing the latency, if we use another model to combine all this content, and then we decode one by one, it cannot get a good speed up. But we can use a smaller model to do the combination. Maybe the expert has already written all the content and you just need to aggregate all this information. And then maybe the output process or the aggregation process can be parallelized by a token. It can like, put all the tokens together and output some tokens together. Maybe that’s possible, but we actually haven’t tried it ourselves. That’s our prospect of how it can be done for improving the coherence.

**Zinan Lin: **The other approach we were thinking about is that instead of having another step at the end for concatenating all the answers–like using another model in other ways–the other way is like during the outline skeleton stage, like when the model outputs the skeleton. They could not not only output the skeleton, but also output, like how we should concatenate the answers in the end. So if you look at the paper we show some reasons. So currently, what we’re doing is that for each point we first put a skeleton point and then the expanded answer, and then the second skeleton point in the expanded answer, and we’ll see that it doesn’t work that well for some types of questions like emails. So for emails, people usually just start to write the content and we don’t have like 1, 2, 3, 4, 5, right? So this is something we were thinking that during the skeleton stage, the model has the information like how we should concatenate the answer in the end. Like should we put a skeleton point as a part of the answer, or should we remove them?

So the other thing we were thinking about is in the skeleton stage, we not only prompt the model to opt for the skeleton, but also indicate to us how we should concatenate the answer in the end, or how we post-process it. And then in the end, we just directly do whatever the language model suggests us to do, so that we don’t don’t need to have another processing at the end which will increase the latency.

And also it’s more natural to think about how humans think like we when people ask us to write the email, we directly know that we don’t need to pull like 1, 2, 3, 4, 5, in the answer. We know what the answer is. So it’s closer to how humans think.

**Xuefei Ning: **Actually, we have tried estimation, and it works well for the API based commercial models and works, not that good for the open source models. So we just do not include this trial in our paper. 

**Zinan Lin: **So because the prompt will be more complicated and for powerful models, especially those closed source models are able to understand it and then give very good results. But for open source it’s currently challenging to make them understand those kinds of requests.

**Aparna Dhinakaran:** Could you maybe walk us through…The first pass, reading the paper the examples like you said common general knowledge made sense. But I kept wondering, how does it work for math? Right for sequential? Could you walk through where it goes wrong? Is it in the concatenation step?  The parallelization step?  What have you noticed in the common pitfalls for math types of questions or coding?

**Xuefei Ning:** Yeah, so SoT cannot answer math questions well. It’s because of what you just said, it does not have the context. Maybe Zinan can add more information on the concrete reasons for the math question.

**Zinan Lin:** Yeah, sure. So, basically, I can mention on a high level why math is kind of challenging for SoT, and then maybe we can look into those examples to understand. Basically for math as many other papers previously point out, in order to understand correctly, it’s very important to ask the language model to think step by step. It’s also how humans think about math questions: we think step-by-step.


But in Skeleton of Thought we basically request that  the language models first come up with the outline, which is kind of like skipping the computation details and directly jumping to the conclusion–the answer should contain several steps. And then we fill in the details without referring to the previous results, which is very hard to make the answers correct and also counterintuitive about how humans think about math questions. And if we go into the technical details, the  key challenges of applying Skeleton of Thought to math questions is that first, we need to come up with the skeleton, and secondly, we need to fill in the detailed computation step for each skeleton point without referring to the previous result. 

And what we see in this experiment is that models like chatGPT are able to come up with a reasonable skeleton. So for example, we can look at the examples in the paper.

Here the question is: “Solve for x in the equation 3x + 10 = 5 (x – 2).” So this Skeleton of Thought answer in the upper block, the orange part is the skeleton, and if we really look at the skeleton like you mentioned which steps we need to do. Those steps are actually correct. So it’s able to understand what steps we need to take. They will look at the details so that I could expand the answer for each skeleton point (which is in black), we see that it starts making mistakes at the second step. It’s very reasonable, because when we expand the point, we’re expanding the detail from point one and point two independently. So basically, when the model tried to fill in the details for the second point, it doesn’t know the result from the first point. But in math, we need to know the previous result in order to deduce the second one. So that’s why it makes mistakes.

And this is for strong models. But if we look at a weak model ( like those skeletons in orange), it’s even harder for them to make this correct. So, for example, if we look at the same problem but if we use the Vicuna-13B V1.3 model, the third step says apply FOIL, which is incorrect–we don’t need to do it for this step. So the skeleton point is incorrect, and it’s even harder to get a complete answer correct.

So this is why SoT is not suitable for math questions, and even more general like any questions that require step-by-step reasoning.

**Sally-Ann DeLucia:** Awesome, thanks for walking us through that. I guess it makes sense like you said that it struggles with creating the actual details because it’s lacking the context from point one, and it can’t multiply what it doesn’t know to multiply–things like that. So that makes a lot of sense. 

But it also got me thinking: do you see a future where we have a specialized Skeleton of Thought for these types of questions? And what might that even look like?

**Xuefei Ning: **Yeah, actually, we have some solutions in the near future, and some solutions in the remote future. In the near future, we think we can trigger SoT only for the questions it is suitable for. And how can we trigger it? We can use like another small model to do this work for us, or we can tune to fine-tune the LLM to output a special token to indicate whether it should trigger this second stage, because there is a very interesting phenomenon in our work which is that in some cases, some strong models can only output the skeleton stage when it encounters the math question, and it will output nothing in the point expanding stage, and it will get math questions well. This is a very real case if the model is not tuned.

But after some fine-tuning, models should be able to understand if it should put answers out in sequential order and just skip the point expanding stage. And also in the long term, we think maybe Skeleton of Thought should generalize all these things into a graph, because humans actually do not think all in parallel or sequentially– it’s actually more complex. And it should also be dynamic because we cannot plan all these important points in advance, but after some details are out we come up with another idea, find a new connection, and within we add another point that we will expand later. So this Graph-of-Thought is a very long-term plan, and some discussion is still needed.

**SallyAnn DeLucia:** That sounds amazing, I’ll look forward to that future work, it makes sense too, especially the Graph-of-Thought mimicking what our brains do, because it’s a little less orderly, and needs to be a little bit more dynamic. So that will be really interesting to see the results of that.


But you did mention something else that got me thinking, when you were answering that– you were saying that maybe we could fine-tune these elements to choose specific or when to use Skeleton of Thought or when to not use it, but then you also talked about using this without optimizations. But I was curious what your thoughts are on combining Skeleton of Thought with other optimization techniques. We’ve talked about LoRA here before, so what are your thoughts on that?

**Xuefei Ning:** Oh, yeah actually, LoRA helps in many ways with the training stage. So if we want to tune the models to be more SoT capable, we can use the LoRA organization to fine-tune our model faster. We actually do not think more on how to combine your training time optimization like LoRA and optimization like SoT further. But some people have mentioned to me that they  want to adapt it as an idea in the training stage. But actually, I do not know how that can be done, so it’ll be interesting to think about. 

**SallyAnn DeLucia: **Yeah, absolutely, it’s definitely interesting, because we’re seeing what I’m experiencing. At least there’s a lot of optimization. But there are definitely people working on different pieces of the puzzle. And I think something that’s really exciting is we’ll get to see how these pieces can work together and what results those bring. So, I think it’s really exciting to see. 

I have just a few more questions for you, if you don’t mind here.

Another thing that we touched on or we didn’t maybe touch on too much, was the fact that there seems to be weaker models in this and stronger models, and there were two models that you mentioned as weaker in this context, and that was OpenChat-13B and Vicuna 70. Any ideas why they’re weaker in this context? Is it something to do with their architecture? Or what do you think makes them different?

**Zinan Lin: **So those models are all based on LLama models so their architecture is the same. But the difference is that when they do the instruction fine tuning, they’re using different ways.

And why they perform not that well, like with SoT is because, like their ability to understand the SotT instructions is kind of weak.

The model needs to have some basic instruction understanding capabilities to understand what we’re asking for. If it doesn’t understand those kinds of things well, then, the SoT answer will be a mess. So what we see is that for those models is their capability of instruction, understanding might not be that good enough to use with SoT.

**Sally-Ann DeLucia: **That makes a lot of sense. I had a hunch that there was something that those models did a little bit differently. Because it makes sense right? How could they have such poor performance compared to some of the other ones? 

I have one more question for you all before I let Aparna get in with some of her questions.

This is one that’s been on my mind a lot, as I read all these different papers. There seems to be kind of one thing that keeps being brought up. And so you mentioned being this data centric era of machine learning. But it seems like in all these papers, there’s more and more evidence that the transformer architecture, and more specifically, the attention mechanism is not that helpful. It actually is hindering us in a lot of ways. So do you see a shift back into this kind of more model centric paradigm where we’re looking to replace that attention mechanism. Do you see that in the future?

**Xuefei Ning:** Actually, Zinan and I have discussed this kind of thing a lot–what is the next architecture towards AGI. And we haven’t started our investigation into this yet, but our very personal opinion is that the counter architecture is not an automatic solution. We might need other architectural components at least to go a step further. For example, we’re very curious whether we need some ew neural memory mechanism with an access interface and updated strategy, and so on. But this is a very personal opinion without any experiments, and it needs more design in order to go further. 

**Zinan Lin:** Both Xuefei and I definitely believe in the future that this transformer architecture is is definitely not the end–we need something new. But that’s relatively far into the future. But what we currently see at the current stage is that this transformer architecture still has a lot of potential that we haven’t fully explored yet.

And that’s why, there are a lot of papers coming out saying: we just used transformer architecture, and just by doing a little bit more data engineering we are able to get much better performance. If we look back in the history of machine learning, it’s always like alternating between data centric and model centric and data centric. So every time a new model comes out there like and there, there are a lot of potential things we can do like people do a lot of like data engineering to further boost the performance. If we look at the longer horizon, then there would definitely be a new model architecture that came out to dramatically improve all the previous resources. And then people started thinking back about how to design better models.

So I think, if we go back to this question in the short term, there’s definitely a lot more people can explore, based on transformer architecture. And our work is kind of like the first trial in this direction for efficiency, so there’s relatively little previous work on that.

But if you look further into the future, then yeah I agree, we need better architectures, and some people are already exploring that.

**Aparna Dhinakaran:** I’m noticing that you have about a couple of more minutes before we have to wrap up, so maybe I’ll just ask one last question, and then thank you guys for joining us.

I think we’re seeing a lot of folks actually trying to use LLMs or generative architecture in production. Any application that you guys are maybe more in the real world side, you guys think this could have big potential for any real world application you’re motivated by?

**Xuefei Ning: **So the very first motivation comes from the general chatbot application, I think SoT actually has the potential to be using a general chatbot to improve the user experience and also lower down the system cost, because SoT actually introduces a new parallelizing label–it can parallelize between segments of content. And this actually gives some space for the system optimization for some serving framework it can choose to like more intelligently paralyzed between the segments of one question or even multiple questions, multiple uses, and it will help lower the assistant calls to improve your experience. So I think this general teleport system is an application that I care about the original motivation.   

**Aparna Dhinakaran: **Got it. Cool. Well, I think we’re at time, so just want to say a big thank you for joining us today and going over this.  This is a really outstanding paper and wishing you both the best of luck on future work, and we’ll be following along. 

**Xuefei Ning:** Thank you very much for inviting us.

**Zinan Lin:** Thank you.

**Aparna Dhinakaran: **Thank you so much.

**SallyAnn DeLucia: **Thanks everyone.
