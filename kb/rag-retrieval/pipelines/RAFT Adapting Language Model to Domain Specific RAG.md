---
title: 'RAFT: Adapting Language Model to Domain Specific RAG'
topic: rag-retrieval
subtopic: pipelines
secondary_topics:
- models/fine-tuning
summary: Summarizes RAFT as a method for adapting language models to domain-specific
  RAG workflows.
source: arize
url: https://arize.com/blog/raft-adapting-language-model-to-domain-specific-rag/
author: Sarah Welsh
published: '2024-06-28'
fetched: '2026-07-11T04:49:02Z'
classifier: codex
taxonomy_rev: 1
words: 7545
content_sha256: ef6248d27789dd81f65fd07b935acf9613c425812cebb2848f88f3dc1ff86889
---

# RAFT: Adapting Language Model to Domain Specific RAG

![CPR-TrustworthyLLMs - blog SallyAnn Delucia and Sai Kolsani headshots](https://arize.com/wp-content/uploads/2024/06/CPR-TrustworthyLLMs-blog-1021x560.jpg)

              # RAFT: Adapting Language Model to Domain Specific RAG

## Introduction

Where adapting LLMs to specialized domains is essential (e.g., recent news, enterprise private documents), we discuss a paper that asks how we adapt pre-trained LLMs for RAG in specialized domains. SallyAnn DeLucia is joined by Sai Kolasani, researcher at UC Berkeley’s RISE Lab (and Arize AI Intern), to talk about his work on *RAFT: Adapting Language Model to Domain Specific RAG. *

RAFT (Retrieval-Augmented FineTuning) is a training recipe that improves an LLM’s ability to answer questions in a “open-book” in-domain settings. Given a question, and a set of retrieved documents, the model is trained to ignore documents that don’t help in answering the question (aka distractor documents). This coupled with RAFT’s chain-of-thought-style response, helps improve the model’s ability to reason. In domain-specific RAG, RAFT consistently improves the model’s performance across PubMed, HotpotQA, and Gorilla datasets, presenting a post-training recipe to improve pre-trained LLMs to in-domain RAG.

## Watch

## Listen

## Dive in

## Analysis

### Introduction to the RAFT Paper


**SallyAnn DeLucia:** Hey everyone. Thanks for joining us today. We got a really exciting paper reading on a technique called RAFT. And what’s really great is, we actually have Sai here with us who participated in the research. So an extra special treat.

Let’s go ahead and get started. We’ll start with the intro, so I’ll start on my side. Hey, everyone! I’m Sally Ann. I’m a product manager here at arise. I help build out the product and as well as help our customers, you know, get the most value and with me today I have Sai.

**Sai Kolasani:** Hi, everyone. My name is Sai. I’m interning on the backend side of Arize. And I also do research at Berkeley. And this is actually one of the papers that my lab produced. So kind of excited to introduce this one.

**SallyAnn DeLucia:** Yeah. Well, I’m super excited to have you here. It’s always more fun when we have somebody here who’s participated in the research or as an author on the paper. So I think you have a really great perspective and we’re excited to go through it.

Before we get to that, I want to give a little shout to our conference that’s happening in just about two weeks here.

[Arize:Observe](https://arize.com/observe-2024/) is happening in person in San Francisco at Shack 15 you can use the promo code “RAFT50” for a $50 ticket. So really great savings, it’s gonna be an awesome event. We have so many great speakers, people from Anthropic, Mistral, Open AI, Microsoft, Meta, Wayfair and many, many more.

It’s definitely gonna be a great time–I’ll be there. So come and say hello!

Alright, so for today’s agenda, we’re gonna do a background and intro to RAG and fine-tuning just to set the scene because it’s really important to understand those. Then we’ll get into RAFT and go through the training test time results. And then Sai and I will give you our closing remarks.

So with that I’ll hand that over to you Sai, go ahead.


### Background for RAFT Paper: RAG and FineTuning


![Diagram depicting the anatomy of RAG](https://arize.com/wp-content/uploads/2024/06/Image-1-RAG-Diagram-1024x570.png)


**Sai Kolasani: **Yeah, of course. So I’m sure most of you already know where RAG is by now, but for those of you that don’t, this is a diagram. Essentially, you have documents that you want to use to help your LLM answer questions.

You can do whatever you want with them, like you can host them in a vector store, or some sort of database. And then when you have a query perform a similarity search between the query and the documents in your document store.

And then use the most similar documents to help your LLM answer the question. I’m sure most of you already know about this, but we just wanted to do a slight overview, just in case.

Totally. We see this framework a lot with our customers so it’s good to just give a layout here.


![FineTuning Overview](https://arize.com/wp-content/uploads/2024/06/Image-2-Fine-tuning-slide-1024x548.png)


And then fine tuning is kind of like the other big thing that we’re gonna be kind of talking about today. So it’s essentially customizing an LLM that’s already pre trained on additional data, or a specific new task just so that it performs better than if you just used it out of the box.

This is important because this actually ends up improving the LLM’s performance for specific tasks greatly compared to other ma other situations like RAG. But the issue is that it tends to be a lot more knowledge intensive. You need to have a lot more behind the scenes knowledge of these models to kind of make this happen. It’s also just a lot more computationally expensive.

**SallyAnn DeLucia: **Totally. I think there’s different use cases to RAG versus fine tuning, I think. RAG can do really well when you have this kind of need, for in context knowledge being passed to the LLM, whereas fine tuning is really, you know, more helpful for those situations where you have a specific task in mind, and you wanted to fine tune an LLM to just provide that single task there.

**Sai Kolasani: **Just a little bit about why, you would actually want to fine tune. Oftentimes you get better performance. So by fine tuning the models, you end up getting better results for specific tasks or specific domains.

And then essentially, fine tuning sometimes can make a really small model even outperform maybe a bigger one for a very specific task. So that could also be a reason why just kind of from a cost perspective, or like us being able to use less resources.

And then the last thing is differentiation. Most people can’t train like a foundation model from scratch like none of us are going to be able to create like ChatGPT from scratch. So fine tuning with our own data sources helps us create a model that’s a little bit more customized to what we want.

### Challenges of FineTuning

**SallyAnn DeLucia:** All right. Do you want to run through the challenges of fine tuning a little bit. So we just kind of just touched on why, you would want to fine tune to get better performance. It could be cheaper and faster definitely. Don’t want to spend all that time, you know, training a foundation model. But what are some of the challenges here?

**Sai Kolasani: **Yeah, of course. So I mean, everything sounds good about fine tuning. But when it actually comes to practically implementing fine tuning, there’s three main challenges.

The first challenge is data. Oftentimes we don’t really have access to a lot of data for finding tuning to be effective. You kind of want to provide the model with as much data as possible. A lot of times. This data can be very expensive to parse or kind of gather. So that’s one of the biggest issues.

Another challenge that I kind of alluded to before was computational horsepower.

It takes a lot of GPUs and a lot of computational power to be able to fine tune a model to a specific use case, and oftentimes in industry, when you’re trying to launch a new product it’s kind of just not feasible.

And then, lastly–we also alluded to this–fine tuning requires a lot more expertise and understanding of, like the behind the scenes of language, models compared to like, maybe like a RAG system, just a lot more easy to understand and implement. So those are like the three big barriers to actually using fine tuning in production, I would say.

**SallyAnn DeLucia:** I think some of these are getting better. I think we’ve seen that some smaller samples of data might be enough to fine tune, and there’s certain things out there. I think you know the computational aspect of it. We haven’t seen too many improvements there. We have seen some fine sheeting methods. That kind of help you constrain your resources there. But yeah, these are definitely challenges that we want to touch on quickly before we dive into RAFT.

**Sai Kolasani: **Yeah. And then, just like a last overview, here’s a diagram to kind of visualize what happens in actual production and industry.

So the first step for anyone trying to improve model performance would be prompt engineering, seeing if maybe wording the question or the query differently could get better performance.

And then, after that, typically is when people move into a RAG-like system, where you bring in other context at test time to help your LLM perform better.

Then, lastly, is fine-tuning. And this diagram just kind of shows that as you kind of go down the technique might be more effective, but also more costly. So it ends up being used less frequently.

![Hierarchy of language model customization](https://arize.com/wp-content/uploads/2024/06/Image-3-Heirarchy-1024x549.png)


**SallyAnn DeLucia: **Totally, I think, something important to call out to here is like a lot of times. What we see it’s a combination of a lot of, or all of these together. There’s some prompt engineering retrieval, and then fine tuning. You don’t have to use these independently of each other. And I think that kind of gets to where your research group is going with this concept of raft. So let’s get into it.

### What is Retrieval Augmented FineTuning (RAFT)?

**Sai Kolasani: **Yeah. So this is a good segue for us to introduce what RAFT is in full terms. It’s retriever aware fine tuning. So as some of you can probably kind of interpret from the name.

Essentially, it’s a way to kind of incorporate fine-tuning, and like a retrieval system to be able to better identify which documents are most helpful for that.

So we’ll kind of start off with kind of like an exam analogy, just so that I can kind of explain it in layman’s terms.

So, traditional fine-tuning. We can kind of relate that to a closed book exam. You learn all of the information beforehand, and you memorize it. And then, when you take the test, you kind of just have to recollect from your memory.

Whereas a RAG system would be an open book assessment. So you have some sort of base knowledge. And then, while you’re taking the exam, you’re allowed to go through your textbook and try to find the answer in there to help, and you answer the question during the test.

But how RAFT is different is during the exam itself, you still have the textbook, but during your memorization and your studying phase, you actually understand how to use the textbook properly. So when you get a question on a test, you’re able to kind of identify which chapter you want to go to, or which section that you want to go to when you focus on that section so that you’re actually able to get the right answer.

So it kind of just teaches you how to use the textbook effectively by incorporating both methodologies.

![Diagram of the open book vs closed book analogy used to explain RAFT](https://arize.com/wp-content/uploads/2024/06/Image-4-Exam-Analogy-1024x577.png)

**SallyAnn DeLucia: **Right and I think that that last part there, teaching uses the context effectively, like we’re gonna get into it. But I think that’s really like the meat of this research here, and one of the most important parts. So we can dive into that a little bit more here.

**Sai Kolasani: **Yeah. So we’ll start off by talking about the training portion of RAFT

The way this works is we use a traditional supervised fine tuning of the model. But what we do is we provided documents that act as distractors. So these documents don’t contain the right answer.

And then we have one golden, one couple of golden set documents which contain the answer that we need. So if we look at the example on this slide. Let’s say our question is: Who invented transformers?

So during this fine tuning stage for the LLM, we’ll give it documents that talk about Adam, GloVe, Resnet, which don’t relate to the invention of transformers.

And then we have one document which is a golden set that has “Attention is All You Need,” and that is the paper that kind of introduces transformers to the world.

So now, during training, we kind of show the LLM. That the right document is attention is all you need. So as the LLM keeps training, it’s able to understand which document is the right one and how to kind of pick that up.

So just like a little bit more of like a detailed overview of the training data set preparation. There are four major components to the data set that you need to train the model using our RAFT pipeline. So first is the prompt or the query that needs to be answered. The second is the golden document, which is a relevant document or a set of relevant documents that contain the information that is actually needed to answer the query at hand.

And then a set of distracted documents. So these are documents, as I mentioned, that do not contain information relevant to the query, but they are included because oftentimes in the real world, even with the RAG systems there’s a high probability that even if you have a high similarity between a document and the query, there’s not actually any valuable information in that document.

So this is kind of trying to simulate that by providing distractor documents, and then we have the correct response, the answer which is formulated in a chain of thought style.

We’ll get more specific into this in the next slides, but essentially, it’s kind of just a paradigm for the LLM to go through the documents, and identify the relevant parts of the documents that it used to get that answer.

So by training the LLM to do this from the start, it’s essentially learning how to go through each of the documents, identify the relevant parts of the documents, and then use that relevant information to answer the question.

And just one more tiny thing to touch on is the data split.

So, essentially, P% of the data contains the question, the golden document, and the distractor documents, and then (1 – P%) of the data contains the question and only distractor documents.

The reason why we do this is we don’t want the LLM to kind of get biased to where it’s always assuming that there’s some sort of golden document. There’s lots of cases in the real world when none of the documents you have in your RAG system are actually useful for the users query.

So to kind of emulate this, we actually have a subset of the data where there’s no golden document at all. So all of the documents are irrelevant and the LLM has to kind of learn to also understand this. This is just kind of to keep it true to itself, and not bias towards one one style of thinking.

![RAFT training dataset preparation](https://arize.com/wp-content/uploads/2024/06/Image-5-Raft-training-1024x574.png)

**SallyAnn DeLucia: **Totally. Yeah. I mean, it is definitely a common issue that we see. Like, you know, the whole conversation of how similar is not always relevant. And that’s a common problem that you have with these RAG systems they’re built on like you touched on that very first slide there on a similarity metric. So we’re looking at these embeddings, and we’re grabbing something that’s similar to the users query. But that doesn’t mean that it has the answer. So this is definitely something that’s required to have a robust RAG system.

I’d be curious, I’m not sure if we were gonna touch on one of the later slides. But in the paper itself, your group talks about wanting a certain percentage of distractor documents to kind of and have this improved robustness for your rag system. Can you talk a little bit, maybe, about how the group determined, like that optimal proportion, how you decided kind of how many use cases in your data set to have. Only you know your distractor documents?

**Sai Kolasani: **Yeah, of course, I think it was just kind of like through a series of iterations. So we kind of just experimented with different percentages. I think we’ll get into this a little bit more later. But it’s just kind of an idea for research purposes. We kind of experimented with different quantities, and then kind of figured out which ones work best for each data set. 

But I think it’s also kind of just one of those parameters that you need to optimize for your specific use case.

Sometimes it might make sense to include a larger set of data with no ground truth versus including a larger set with the ground truth. So it kind of just goes into your specific use case. And it’s I would say it’s something that you should kind of optimize for in a specific use case.

**SallyAnn DeLucia:** Yeah so kind of like a hyper parameter almost. It’s kind of an interesting call. It sounds like we’ll get into more details, so I’ll save some other questions for later. 

But we do have a question from the group here: In RAG, LLMs are good at filtering out completely unrelated context, but they tend to fail when documents are relevant, but not actually quite applicable. How are the distracted documents chosen to fit this criteria? Is this something that the group thought about at all?

**Sai Kolasani: **Yeah, so I think the short answer to that would be, we kind of tried to include some documents that were similar to the ground truth. And then some documents that were completely different, just so that we kind of encompass the whole wide range of possible situations. Because even like, let’s consider a real case scenario. With your RAG system, you could with similarity search some of the documents, could actually be kind of relevant, but not contain the right answer, whereas some are just not relevant at all. 

So we kind of emulated that by using a mixture of documents that were completely irrelevant, and then some that were getting more relevant.


So I guess if you go back to like the slide with the example of the transformers….

So like, if you look at this, Adam and GloVe might not be related at all. But Resnet could actually be maybe a little bit closer to the true answer. So we kind of just try to vary that composition.

And just have a wide range of documents that encompass all the different scenarios.

**SallyAnn DeLucia: **So is there a level of curation that you all did to do your best to kind of emulate what happens in the real world where you can get something that’s related, but doesn’t have the answer, and something that’s completely unrelated altogether.

**Sai Kolasani: **For sure. I think this that’s also an interesting topic to bring up. I think future work that’d be really cool to kind of like explore all these different scenarios, maybe like a scenario where all the documents are completely irrelevant, and then a scenario where all of them are like almost exactly relevant, like, really close to being relevant. So I think that’d be cool if, like, someone could kind of explore that and then see what the results are that way.

**SallyAnn DeLucia: **Totally. Yeah, that would be. It would be interesting to see. Not only how you know it impacts the answer. The following is but just kind of to see how effective this technique is.

There’s another question in the chat, but I think we’ll circle back to it in a second.

Let’s talk about chain-of-thought, I thought that was a super interesting part of the paper.


### RAFT and Chain-of-Thought


**Sai Kolasani:** Yeah, exactly. So RAFT uses the chain-of-thought style for generating answers. This means that the model is trained to kind of provide the reasoning that it need to answer. 

So when we kind of prompt the LLM, we don’t just go, okay, use these documents and then give me the right answer. We kind of tell it: Go through these documents, give me the relevant parts of the documents that you’re using, and then answer the question.

So this structured approach kind of helps a model better navigate through the mixture of relevant and irrelevant information, which then ultimately kind of makes it better at reasoning and extraction. We have an example of this and a couple of slides coming up as well. So we’ll get a little bit more detail about that later.

**SallyAnn DeLucia: **Awesome. Yeah, I think chain-of-thought is is a super powerful technique. Specifically, anytime, you’re doing any type of research. And you’re trying to understand, like, how the LLM is formulating thoughts. But I think it also just helps LLM, perform better when it’s, you know, required to kind of go through and think you can think of just how any human were to reason through something. There’s a chain of thought right that happens to arrive at an answer. 

I think you have some slides coming up that will dive in a little bit deeper on it.

**Sai Kolasani: **And then this is kind of just like an illustration of test time. So now you did the fine tuning part of RAFT, And now we want to be able to use the model, so what happens?

So now again, like the traditional RAG system, now we have our fine tuned LLM. And then we pass in the similar research like whatever type of similarity search you want. You retrieve these documents and then pass that into the LLM with the query.

And now the LLM is able to output the answer, but while it’s generating the answer now, because of the fine tuning, it knows how to eliminate the distractor documents and kind of focus on the document with the ground truth.

So essentially the test time, like inference, part of raft, is kind of emulating like an a regular RAG system, just that the model is now so much more accustomed to getting the relevant part of the information.

**SallyAnn DeLucia:** Totally so at inference, nothing really changes. It’s all about that kind of fine tuning that you’re doing. It’s the the data that you’re providing for fine tuning, the structure of that including those documents, some distractors, some not. And I think the chain of thought was also provided in that the find or the fine chain data set correct?you gave kind of the ideal kind of chain-of-thought there.

**Sai Kolasani: **Exactly. Yeah. The reason why we provide the chain-of-thought reasoning is the answer in our training data set. And the reason we do this is because then, because the LLM is trained to respond that way.

Now, when it kind of produces an answer, it’s inherently using that chain-of-thought, reasoning to generate the answer.

And obviously, I think, as many studies have shown, chain-of-thought has been very effective in improving answer quality.

**SallyAnn DeLucia: **Yeah, I  think that’s really important. I’d be curious to learn a little bit more about your process. There is kind of going back to, I guess one of the other slides of like how you all went about generating those chain-of-thoughts for the training was that something that you leveraged another LLM to do? Was it kind of, you know, manual, where you all in the group kind of provided the correct chain-of-thought. How did you go about doing that?

**Sai Kolasani: **Yeah, so I guess the four main data sets that we used were a medical data set PubMed, HotPot QA, which is kind of just like a general question answering data set, and Hugging Face, which is for coding like APIs. And then we also used an in-house data set called from Gorilla LLM, which is kind of just like a tool calling for APIs.

So a couple of the data sets, they actually had chain-of-thought answers as the traditional answers within the data set. So we didn’t have to perform any modifications to that.

But for the other data sets like HotPot QA and PubMed, we passed in the answers to the oracle LLM, like let’s say like GPT-4. And now I guess you would use like Gpt-4 0. And we kind of had it come up with like chain-of-thought, reasoning that way. And then we curated data sets that way. I mean, I guess it depends on the specific use case. If you have the capabilities to kind of generate chain-of-thought reasonings yourself, or like your team, then you can curate the data set that way.

But it’s just a lot easier to kind of have a really strong LLM do that for you.

**SallyAnn DeLucia: **Totally. I think we see that a lot with these techniques. So this, this synthetic generation, I mean, the models are so good these days that you can rely. I think you know you do want to have some kind of level of human evaluation before you just automatically assume that it’s of high quality. 

I think, in a lot of the research that we’ve gone over, you know, previously we’ve seen that the quality of the data is one of the most important things. There was one point where volume mattered, but now we’re actually seeing that you can get really good results with a smaller data set as long as it’s super high quality.

So it makes sense that you leveraged what you had from those you know, data sets that you’ve chosen and then you leveraged an LLM to do some synthetic data generation.

**Sai Kolasani:** Exactly. Yeah. And then, just like, even for the synthetic data generation, we used our examples. For some of the questions we actually did generate our own chain of thought reasonings, and then pass that into the oracle LLM to kind of use that as the backbone for its chain-of-thought answers. So we kind of got everything in a format that we wanted.

**SallyAnn DeLucia:** At least we had some, you know, few shot prompting there to get that.

**Sai Kolasani: **Exactly. Yeah.

**SallyAnn DeLucia: **Those chain-of-thoughts that you were looking for. That’s awesome. Cool. Well, let’s keep going. I might have some more questions for you. But this is great example.


![RAFT Chain-of-thought demo overview](https://arize.com/wp-content/uploads/2024/06/Image-6-1024x576.png)

**Sai Kolasani: **Yeah. So this is kind of what I was alluding to earlier. So here’s a question for our like RAFT LLM. 

And the next slide would be the context. So this is the context that you would retrieve from your document store. And it just has a bunch of information relating to the query through similarity. Search and then. Now this is our instruction to the language model.

So we say, give them the question, the context and the answer provide a logical reasoning for that answer. And then use the format of reason, and then answer. So that’s kind of where the chain-of-thought reasoning comes in. We tell it to kind of provide its reasoning first and then answer, based on that reasoning.

And yeah, this is kind of the answer that the model produces after. So, as you can see, it has a reason. Shows the document chunks that were the most relevant. And then it kind of provides the answer after.

So this essentially makes the LLM use the document use, like the relevant parts of the documents, to answer the question, as we intended.

**SallyAnn DeLucia:** Totally. It’s almost like you’re making it site its source, right? You can’t just give an answer for no reason. You gotta set your source there. Very cool. 

Let’s talk about the results. I thought these were really interesting.

**Sai Kolasani: **Yeah, for sure. I’ll go through the term DSF, that is just kind of our the fine tuning part of our RAFT pipeline. So the RAFT pipeline without using like the RAG at inference time.

So not RAG, it’s just DSF. And then DSF plus RAG would then kind of go into our RAFT pipeline

So as it can be seen for 4 out of the 5 data sets using our RAFT pipeline actually improve the performance quite a bit compared to other iterations of the models. And it honestly does better than GPT-3.5. But Bard, which is really impressive because we’re using an open source LLaMA model with only 7 billion parameters.

So the model is not necessarily the strongest offering on the market in terms of open source, but it’s able to kind of match the performance of GPT, which is really interesting to see.

**SallyAnn DeLucia: **Yeah, something I really appreciate. No reading through this paper is, you have all these different comparisons, you know. You have just like a base model you have with Rag. But then you also have fine-tuning that fine tune with RAG. You can really just see, like, across all of those different scenarios. You know, RAFT is really outperforming. And I think it makes a lot of sense. If you think about what you all have done with this research. I think it’s a very common problem of getting the LLM to attend to the pieces of context that it should be and actually making use of them, and not, you know, loosening an answer. 

And so the idea of training it on how to use the context, I think, is obviously very powerful, and we see that in the results here. I’m curious if you guys explored the role of kind of prompt engineering as well?

I’m specifically curious if there would be any use cases where maybe, like the prompt engineering would be able to kind of help. You know, the LLMs ability to ignore, you know, a relevant context, or like where you maybe see the gaps in terms of prompt engineering.

**Sai Kolasani:** Yeah, for sure. I think prompt engineering is something that the lab didn’t really focus on. The authors didn’t really focus on in terms of this paper.

So we kind of just stuck with a very simple prompt instruction, but I think that is definitely one avenue for future research, being able to optimize that better would actually, for sure improve performance, by how much we don’t know, but I think it definitely will make some sort of positive impact.

And for accuracy, even a little bit of an increase means a lot for actual use cases. So I do definitely think that kind of experimenting with the prompt engineering will help the LLM produce better answers for sure.

And then I guess another thing that I wanted to point out from these results is as you can see, for PubMed and all of the coding API data sets. Our model did a lot better.

But then, when it was like a general question answer dataset like HotPot. It didn’t quite beat traditional chatGPT and it did even worse than some of the other models.

And this kind of goes to like our understanding, or one of our takeaways is that RAFT makes a lot of sense to use when you have a very specific domain, or like something where you have a use case that’s differentiated from just needing general information.

So in the case of HotPot, it has questions spanning from various different topics. There’s not one general theme in the questions.

So it makes sense that RAFT didn’t really perform better than just using a traditional RAG system, because there’s not really much to fine tune on it, because the questions are so diverse.

### If You’re Doing RAG, You Should be Doing RAFT

**SallyAnn DeLucia:** I think that’s a definitely a really great call out, because I think a lot of people who are listening, their question is, you know, when exactly should I be using RAFT? 

And I think you might read this paper and be like, Oh, anytime I’m doing RAG. I should be using RAFT, and I don’t think I agree with you. It’s not necessarily the case. I think you really have to consider. You know the domain, the task itself. And decide whether or not you know, RAFT is worth the end investment, because, you know, fine tuning these models does require cost, it requires time, resources, all of that. And it just might not be necessary.

So I think maybe doing a little research on your own and testing this out might be a good call there.

We got some questions in the chat. Let’s maybe go through those quickly. So there’s one question here where they are trying to do HR FAQ, probably you know RAG, chatbot just about 200 questions. If they were to want to use RAFT, how many questions would we need to prepare for the training data set?

That’s always a tricky question that everyone wants to know.

**Sai Kolasani:** I think my take on it is, do what makes sense to your specific use case. I think there’s not one general answer about, like the number of questions you just have in your data set right? Like the obviously, the more training data you’re able to provide in the fine tuning stage, the more customized the model is to your specific use case. So kind of just really depends. I think.

As a general use case 200 does seem kind of like on the smaller ends, smaller end for a data set. But it honestly just kind of depends on your use case. And just, I’d say, just kind of experiment with it.

SallyAnn can talk a little bit more in regards to that, in terms of actually using this in industry.

**SallyAnn DeLucia: **I think everybody wants to know what that golden number is. We had that same question, you know, back in the traditional days of how much data do I need? And I I unfortunately just don’t think there’s a good answer. 

I would say that you could maybe get away with 50, you might need all 200. You really won’t know. I think it depends on the quality. And as I mentioned exactly what the task is. Something with like a simple kind of RAG system for just answering kind of HR-Related questions. You might be able to get away with a smaller number of data sets, because it’s just that breadth of knowledge that the means is just not very wide. So I would say, make sure that you create some really high quality examples, and you could always start small and expand. But at 200 you might be able to just kind of use all of those, but just definitely make sure it’s high quality. I think that’s the key to fine tuning here.

We have another question around fine tuning. This specifically, is about how you all took precautions around catastrophic forgetting.

Did you guys account for that? Was that something that wasn’t necessarily top of mind for you all?

**Sai Kolasani: **Yeah, we do have some abolition studies. So if you look in the paper itself, we do have some studies. So we kind of tested RAFT without using chain-of-thought, reasoning. So just using normal question/answer, type of prompts. And then also just some other abolitions as well. So if you kind of read the paper, there’s a little bit more specification on that. But obviously that wasn’t necessarily too much of our focus in this paper. It was more so trying to kind of effectively bridge the gap between just having to use rag or like fine-tuning kind of like being able to use both in a sense. But I would definitely recommend reading the paper. There’s a lot of fabulation studies on there, a lot of information that we provide there that can answer your question better.

SallyAnn DeLucia: Totally. I know we’re running low on time. Here, let’s get through the rest of this. You had a lot of good information here.

**Sai Kolasani: **Yeah, for sure. And then I guess one other kind of thing we looked at in the paper was during test time, like how many documents do we use? So for natural questions, we got the best results when we use like 3 documents as our top K, whereas in HotPot, it was one document, so one document as a distractor, and then like a golden document.

And then, for all natural questions, it is one document, and then three distractors. So I think that also kind of just goes back to what I was talking to a little bit earlier than in HotPot it doesn’t make sense to have, like as many distractors, just because the questions are so general, whereas in natural questions the questions tend to have more of like a specific type of guidelines, specific type of format. And they’re a lot more similar to each other. So it makes sense to include more distractors.

So it really just goes to show that you need to understand your data set really well, to kind of figure out if RAFT makes sense to use, because, in my opinion. Just kind of looking at these graphs in the HotPot QA. I don’t think it makes sense to necessarily even have to use RAFT

resident natural questions. So I think it would be fair to say that you know there is kind of this varying robustness when you introduce different numbers of documents at test time there. So that’s something to kind of keep in mind.

And I think there could be another potential. You know, I think a research avenue around this of like, how can we ensure, you know, consistency performance. Really, when you’re having kind of that bearing at test time.

And yeah just kind of throwing in a little message here from my team: If you’re doing RAG, you should be doing RAFT.

Sometimes.

I think, from an academic perspective, it makes sense to kind of use it all the time. Just make sure, like, you actually understand your use case. And you’re careful about what your data set is actually looking for.

**SallyAnn DeLucia: **Let’s go through our takeaways in the last few minutes here. 


### Main Takeaways for the RAFT Paper


**Sai Kolasani: **Yeah, for sure. I guess I can start this off. Just so those at the top of the slide. But I was kind of talking about this the whole time. 

It’s really useful for settings where the documents might have a unique format, or the topic is very obscure, not necessarily worth the extra work during implementation for traditional document sources.

So what do I mean by this? Let’s say that your RAG system is just kind of retrieving articles from Wikipedia, and that’s kind of your source. I don’t know if it’s necessarily worth it. Worth the extra hassle to use raft, but let’s say, you’re like a medical company, and all of your documents are like diagnoses, or like kind of like chart statements for your clients.

Makes a lot more sense to use RAFT here just because you really need to be able to identify the right customer. Like, if you do like a similarity, search for a customer like some specific ID for equipment.

And you end up getting 10 different documents on that. It’s really important to know which one to use because it could be like life or death in some situation. So that’s kind of what I took away from this.

**SallyAnn DeLucia: **Sure. And then, you know, for my takeaways, I think the key thing I got here is RAFT is different than most fine tuning techniques. In the sense that it’s about getting the LLM to use context effectively rather than just making an LLM respond in a specific manner.  

A lot of times when we’re fine-tuning where we’re fine-tuning so that the LLM can respond according to the task we’re fine tuning for. This is actually training it to use context which I think is really important. And this kind of detailed reasoning that we’re incorporating in the training process that is doing this instruction.

It just really helps the models make the best of the context. And I think if you have a use case where you’re using RAG, and it’s not effectively using a retrieval. You’ve tried to change how you’re doing retrieval. You’ve added more knowledge to your contact space, and you still can’t get it to respond or attend to the right pieces of context. I think this would be a really good option for you.

So, it’s exciting to see. RAG is still very popular. And I think there are often these issues around. It’s not using the retrieval context, right? And I think RAFT is going to really help you do that.

We do have one question in the chat here. I guess we’re on the last 5 min here. If anyone else has any questions, drop them in the chat or the QA. We’re happy to answer them.

Mike asked: How did you pick the distractors for that training process?

**Sai Kolasani: **Yeah. So I guess it really just kind of depends on the data set. So for something like HotPot QA, we kind of filtered through other questions that had a similar topic, and then used context from those questions as distractors, and then chose some random questions, and then use the context for those questions as some of the other distractors.

So it’s kind of just using the documents for different questions that is not like the question at hand for the data set.

But I think that’s also like, yeah, I think generally like, that’s probably the most you can do with a predefined data set like that, just for kind of getting some results.

**SallyAnn DeLucia: **Yeah, it sounds like the curation, the data. There’s just gonna be some manual work involved in that. And I think the distractor specifically, or something that would be difficult to kind of automate that or leverage an LLM. You know, an LLM you could maybe use now, and to maybe generate some synthetic context examples. But if you’re wanting to use examples from perhaps your actual knowledge base, you’re probably just gonna have to comb through that data and find those pieces of context that make the most sense there.

**Sai Kolasani: **Yeah or like some sort of randomization where you choose random queries. And then just provide the context for those in. And I think, yeah, I think that’s probably the best way to go about it. That is something that is pretty intensive to do.

**SallyAnn DeLucia:** Yeah, for sure. That’s a really helpful hint.

Question: Any examples of RAFT in production?

This paper’s pretty new. You all did this two or three months ago?

**Sai Kolasani: **Yeah.

**SallyAnn DeLucia: **So yeah, I don’t know if you know of any. I think there’s a lot of folks who are exploring this right now. Specifically, this talks to an issue that a lot of folks have with their RAG system. So I think it’s gonna gain some traction here, but I’ll let you answer too Sai.

**Sai Kolasani: **Yeah, I mean, I guess, I don’t really like, necessarily our information about like, who’s actually using this in production. But I did hear that there are a couple of medical companies that are trying to kind of incorporate this and they’re in kind of talks with the others of the paper and seeing, if, like, this is something that’s like valuable for them, because their issue traditionally has been that they get a lot of documents. But for them, it’s really important to kind of identify the best document to use because let’s say for kind of like a disease, right like, there’s so much documentation for different symptoms, different treatments. So it really make sense like, they really need to be able to identify the best document to use in this case. So I did hear that there’s some talks about using RAFT. But obviously this is still like a really new paper produced like published like couple of months ago. So nothing that I know of concretely yet.

**SallyAnn DeLucia: **Yeah, just gonna be like going beyond just the medical use case. You can imagine that any type of customer facing system could benefit from this anytime. You’re putting anything in front of a customer and user, it matters what the LLMs outputting as its response. So anytime that that is the case, you’re struggling to do it with just your out of the box model, or you’re just traditional fine tuning. I think Raft could really help there. So I do have some confidence that we’ll start seeing teams implementing this type of fine tuning for sure.

Alright, everyone. Well, thanks, guys so much for walking us through this paper. It’s super interesting. I’m excited to see the future research here. And what teams do with this? Yeah, thanks everybody for joining!
