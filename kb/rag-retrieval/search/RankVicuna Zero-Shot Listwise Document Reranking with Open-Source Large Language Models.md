---
title: 'RankVicuna: Zero-Shot Listwise Document Reranking with Open-Source Large Language
  Models'
topic: rag-retrieval
subtopic: search
secondary_topics:
- models/reasoning
summary: Summarizes RankVicuna for zero-shot listwise reranking and its implications
  for LLM-powered search.
source: arize
url: https://arize.com/blog/rank-vicuna
author: Sarah Welsh
published: '2023-10-17'
fetched: '2026-07-11T04:47:51Z'
classifier: codex
taxonomy_rev: 1
words: 6277
content_sha256: b459d8a375b34f2a32a126cb3e5ce1060df1f8a978a3045e477e9a034e4a7c54
---

# RankVicuna: Zero-Shot Listwise Document Reranking with Open-Source Large Language Models

![Community Paper Reading - resource image - Amber and Claire Amber Roberts and Claire Longo Profile Pictures](https://arize.com/wp-content/uploads/2023/10/Community-Paper-Reading-resource-image-Amber-and-Claire-1021x560.jpg)

              # RankVicuna: Zero-Shot Listwise Document Reranking with Open-Source Large Language Models

## Introduction

In this paper reading, we’ll be discussing RankVicuna, the first fully open-source LLM capable of performing high-quality listwise reranking in a zero-shot setting. While researchers have successfully applied LLMs such as ChatGPT to reranking in an information retrieval context, such work has mostly been built on proprietary models hidden behind opaque API endpoints. This approach yields experimental results that are not reproducible and non-deterministic, threatening the veracity of outcomes that build on such shaky foundations. RankVicuna provides access to a fully open-source LLM and associated code infrastructure capable of performing high-quality reranking.

## Watch

Dive in:

Listen:

## Transcript

**Amber Roberts, ML Growth Lead, Arize AI:** Alright cool, Claire, want to kick us off? 

**Claire Longo, Head of MLOps Solutions Engineering, Arize AI:** Yeah, hey, everyone. Thank you so much for joining, my name is Claire Longo. I lead customer success here at Arize, and I’m also tinkering with LLMs in my free time, as I’m sure a lot of y’all are. We’ve got a great paper that we’re going to talk through today, and it covers some really cool topics around ranking. But it does not at any point describe what those actually are. So I’m going to give a quick overview of ranking models and reranking, and what that really is before we dive in here.

The first thing I want to cover here is: What is ranking in the first place?

So I think of ranking models as really like two core kinds. Here, there’s recommender systems and document ranking. And specifically, we’re gonna be thinking about document ranking right now. But the bones of how these model work models work are very similar.

Essentially, what you have here is input data that gets turned into features. So, in document ranking, you’re looking at a query and documents. So you have embeddings that are representing those. And you have some kind of ranking model. Now, the architecture of this can definitely vary. You could have some kind of simple cosine similarity system here. You could have a deep learning network–that’s like a hybrid recommender system. But the output is always going to be a ranked list. And so that’s what makes these kind of learning to rank models special. They’re different from classification, different from regression, and different from NLP in the sense that they are predicting not a single value or item, but they’re predicting what the rank is of a list of items.

So in a situation like this, the output would be a list of ranked documents. You want your best documents at the top, your worst documents at the bottom, and we’re ranking based on a score, and the score is usually some kind of like engagement metric like it can be like probability of a click, probability of a purchase probability of reading a document end to end whatever kind of signal you can get here, but the model will be trained to optimize and predict that score. And that’s what’s used to do the ranking.

So that’s what the predictions look like. But then you get into: what do your actuals look like? What’s your feedback loop? And in a lot of these situations, you will get a label as the actual. So you’ll get something coming back saying, giving you some kind of signal like, was your ranking right, did people actually click on that document? Giving you that indication of whether your rank list was good. Did you have your best items at the top?

So that’s document ranking. Now, let’s jump into the cooler stuff, which is LLMs.

So RAG is a really common pattern in LLM architecture today, its retrieval augmented generation. Essentially, what these systems look like is, you have a user query coming into the system, and you’re using that query to get some kind of response out of your LLM. So you’ll have essentially the system that is orchestrating the query with the context data that that kind of corpus of documents as well as making calls to your LLMs, formatting response and maybe collecting any user feedback if you have it.

The really interesting thing about this is reranking and how that might fit into a system here.

So this system doesn’t show reranking. It’s essentially just doing the query step. You have the user query, you reach into your vector store where you’ve embedded and shoved all your documents and chunked them up. And then you are retrieving, let’s say, top K relevant documents.

So it’s not necessarily optimized for ranking that list. It is optimized for retrieving you the most relevant content. So the retrieval is trying to get relevant stuff. It’s kind of a ranking to do that. It’s usually like a cosign similarity kind of operation there. But what you’re really trying to get out of this step is like, give me the most relevant content to augment into this prompt and then pass into the LLM.

The reranking step here is adding another LLM here in the system before you put it into your kind of foundational LLM that’s doing the generation of response. Essentially, what you’re doing is… let’s say you retrieved 100 documents from your vector store or 100 chunks. And you want to make sure that those really are ranked in a meaningful way, with the best at the top and the worst at the bottom. So then you apply this reranking model system that I talked about earlier where you’re essentially reranking and maybe choosing like a smaller K, so let’s say, K equals 5 here. So you’re taking, like your top, most relevant five, and then only using that going forward. So it kind of further narrows this system here.

**Amber Roberts:** Awesome. Thanks, Claire. 

And if people have questions, there’s a Q&A. And there’s also a chat where you can get your questions answered.

Alright, let’s dive into the paper here.

And then, of course, like the other thing, this paper doesn’t really get into are how metrics for ranking and re-ranking are calculated. At Arize, we have a full unit on [rank aware evaluation metrics](https://arize.com/blog-course/model-evaluation-metrics/) as one of our free units in our evaluation and metrics courses. So Arize University, we have an entire unit that goes in depth on the NDCG or normalized, discounted communicative gain, and the steps of that. If you have questions on these metrics, we can answer those, but these are the three main metrics that you see in ranking systems, and the two main ones discussed in this paper are NDCG and mean average precision. 

NDCG is very sensitive to rank order and MAP is a little more digestible, but tends to be for binary cases where the examples we’ll see through the paper are looking at a binary relevance. Mean reciprocal rank (MRR) isn’t really used in this, but it’s another one you might see in ranking. So if you’re interested in these metrics, recommend checking out more in Arize University.

Alright. So we’re talking about RankVicuna. I think that’s how you say it. Which is a zero shot list wise document, reranking with open source large language models.

So there’s a lot in that one sentence, and that’s why Claire and I are kind of breaking it up. You know, now that we’ve talked about document reranking, this is an open source model available for the public. It’s a large language model. We’ll get into the zero-shot component. But Claire, do you want to talk about listwise versus pairwise? I also put some information just at the top of the page, because it wasn’t something I even think about often. When thinking about ranking systems.

**Claire Longo: **Yeah, so this is really cool. So there are some models that are specifically made to rank a list and their output as a ranked list. There are also classification models that produce a score that could be also used to rank a list. And that’s kind of where we get into these nuances.

So, a ranking model, let’s think of maybe like a hybrid, deep learning recommender system– is going to take a list of items or documents, and it’s going to produce that ranked list as the output. Another way to get a ranked list would be to feed a document into a classification model one at a time, get a score, and that score is again going to be like probability of a click–it’s just going to be that score that we use to rank. And so you could pass those same documents through more of a classification model, and then use that score to rank, and that is the difference between a listwise and the pointwise. List wise is like you are returning that list right away and breaking those documents together through like one call to the model, whereas pairwise is like having these right? Yeah. So pairwise is when you’re predicting that score and then using that to rank the documents individually.

I think there are trade offs here because when you’re doing listwise, you’re considering the other documents almost as like additional information or context to help bring that list, whereas when you’re doing more of the pointwise approach, you’re not necessarily looking at the other documents to determine what the score of the one document that you’re interested in should be. And so it’s a little bit blind when it comes to what else is in the list. And that’s kind of an interesting thing to think about when you choose which approach.

So here we’re talking about listwise document reranking.

**Amber Roberts:** Awesome. Thanks for that. So, looking at just a few things about the abstract before we get into the depth of the paper.

Essentially their claims are that RankVicuna is the first of its kind that’s open source.

Has this LLM capability performs reranking in a zero-shot setting. So it’s not given a bunch of examples. It’s just essentially asked the question like, when you use chatGPT, and you’re asking a question gives that response back. You’re not giving it a bunch of examples, you’re not doing few shot, you’re not doing chain of thought learning. If you’re interested in learning more about zero-shot versus other prompting techniques. I recommend checking out the prompt engineering guide that goes into depth on the different types, but basically zero-shot is just a single action. And it’s the most straightforward and most commonly used. It’s definitely the benchmark. If you’re testing out against different prompt engineering methods. So that’s when you see, like the zero-shot setting, that’s what we’re seeing here.

But it’s saying that it is just as effective as some of these other zero-shot reranking with GPT4, but it’s a much smaller model. So this is a 7 billion parameter model and their effectiveness is essentially on par. But you have a much smaller model that you’re using for this re-ranking step and going back to what Claire mentioned, that re-ranking step is after you select all the documents. So okay, I have all the documents I need, now, I’m going to go back through and we rank. Essentially, if you have an assistant, and you say, get me all the files on this case, and that assistant goes and gathers all the files you might want to go through the files to organize them for a certain type of priority.

The other thing this paper gets into is the open source versus these proprietary models, and you know the fact that we don’t have access to them. And right now the proprietary models, like all the GPT models are performing so well, but open source is improving at a constant rate, so they’re still not as good. But this paper is pointing out the advancements that are being made especially for individualized cases and special use cases for these open source models and how the effectiveness is steadily improving over time.

So it’s just interesting to see when GPT-5 comes out. How much better is it than these other models, and how much better is it than other open source models?

It also gets into rank being deterministic. We’ll get into that a little bit later, because that definitely was non-trivial for us when we were going through the paper.

Claire, anything you want to talk about in background or related work?

**Claire Longo:** When I was reading this paper I was looking for two things. What is the value prop of what they’re doing here? What value could it bring to my workflow today, or could I use it as a jumping off point for additional research? 

And then also, just how are they measuring “good”? They mentioned in the first few pages of the paper here that you know it performs as well as a larger model. But what does that mean? What does “performs well” mean? And so that is something that we’ll get into and how they’re actually measuring the value of the reranking here, because reranking is becoming a very popular part of an LLM system. And that’s something that I was thinking through a lot–why are we even doing this, what’s the value of it?

**Amber Roberts: ** Yeah, it makes sense when you’re going from traditional recommendation systems where that rank that you’re given is already based on some of your specifications. For you’re using collaborative filtering. And what you want to do there versus using an LLM which you know can hallucinate like, you know. You don’t know exactly what’s going on under the hood, but re-ranking, you have a bit more control over there, and especially if you want to get into personalization. And that reranking step I do feel is necessary, but I wasn’t really thinking about it too much before reading this paper, and just starting to have those thoughts of like, oh, like, why is this necessary? What is the value? Prop? Why are people doing this? And I think you’re exactly right. 

**Claire Longo: **And another thing that I was thinking about was kind of letting different LLMs and and prompt pairs, like a little bit of like a components of your LLM system, separating it out and letting different components be good at different things, like I have a retriever system, and it’s really really good at retrieving. But I’m not necessarily optimizing that system to rank. But now I’ve also got a re ranking system that’s really, really good at ranking. Just let those two systems be separate and be good at what they’re good at.

**Amber Roberts: **Yeah, that’s a great point. The other thing I just wanted to highlight was the mention of HyDE. [We do have a full paper discussion on the HyDE paper](https://arize.com/blog/hyde-paper-reading-and-discussion/). One of these community paper discussions on our Youtube channel, so if you’re interested, the HyDE approach–what’s special about it is like when we put in a query that we’re then collecting documents for, the normal processes we put in the query and then that’s connected to our vector database, and all of our relevant documents are selected, based on that query, but HyDE generates the response and then the relevant documents are based on this kind of created answer. So, instead of it being all the relevant documents based on the question, they’re actually being based on this created answer that’s generated from another LLM, which is really interesting when you think about it because that’s HyDE trying to show these relevant documents might be the closest to this created answer than they are to the actual question. Especially in that vector space.

**Claire Longo: **Yeah, that’s fascinating.

**Amber Roberts:** But yeah, another reason why Claire and I picked this paper. We love ranking. We love recommendations. Anything ranking and recommendations, especially with all that we’re seeing in industry use cases–every team, regardless of industries, has some kind of ranking, some kind of recommendation, even if it’s internal versus external, and everyone’s trying to see how they can leverage LLMs for this use case.

Let’s see, I think here I just kind of highlighted that again, they’re talking about prompting methods. They’re talking about evaluation metrics such as NDCG, which we talked about a little earlier. And then this is the prompt.

Claire, anything you want to say on this prompt?

**Claire Longo:** Okay, this was fascinating to me because I come from a background of like boring old tabular traditional recommender systems. And in this new age, with new technology, ranking becomes just like a very different kind of system under the hood. So, the way that they’re ranking is actually through a prompt. They have constructed–through some very good prompt engineering here–they’ve constructed a prompt where the output is going to be that ranked list. So it’s not necessarily that the model is trained and we’re leveraging that. But we’re really just leveraging the power of a language model with a very good prompt that inputs a chunk of documents just like a model here would and outputs a ranked list. So really kind of cool to see that this is really a strong, prompt engineering problem.

**Amber Roberts: **Yeah. And I think we’ve shown a few times the differences between fine-tuning versus prompt engineering, and when you might want to use one over the other. And I think just being able to even specify and change out this prompt you can have slightly different ranking systems that are maybe specialized to your own company. And things and trends you might have seen. It’s definitely easier to do this over fine tuning, but that’s a different conversation. 

**Claire Longo:** Yeah you always want to start there. 

**Amber Roberts:** Agreed. And then they also talk a bit about the training process, and then we get into the experimental setup. So they’re not using just GPT-4 for re-ranking. They’re using these rank GPT models that they’re referring to as rank GPT-3.5 and rank GPT-4. And so these are re-ranked systems from research that are using these other models. And that’s what’s being used there. And again, the model that we’re looking at the RankVicuna is 7 billion parameters. And they do include a few other open source options as well when doing the comparison. They’re using MS Marco passages for their data set, so you’re going to see DL-19 and DL-20 referred to throughout this paper. These are the data sets that they’re using for ranking, re-ranking.

They go a little bit into the context size, which is very small compared to GPT-3.5

If you’re interested in the sliding window training times they get into that into the paper. But we’re going to get a bit more into the results here.

**Claire Longo: **Before we get to the results there was something that stood out to me on the training part. First of all, they never use the word fine-tuning, which is interesting, but they are training these models.

The thing that stood out to me is that the way they generated some of the data here for training, or maybe all of it is they generated query and ranked documents as a response. They generated that data, that training data from another larger model. And I thought that was really creative and cool. Because isn’t that like a great way to get your smaller, cheaper model to learn some of the patterns that this larger model might have already encoded by just training your smaller model, on data generated from that larger model.

**Amber Roberts: **Yeah, it’s interesting that we keep hearing this is a smaller model, but it’s almost like, if you think of hyper-parameter tuning on that and you know you’re like collapsing layers, and you’re just making it smaller–that’s what it is– and it’s a clever way of doing it. With the model a lot smaller. But you also can’t have this model without those larger ones. So you can have the large ones without the small ones. But you can’t create those small ones without these larger models.

And the rank GPT-3.5, these are like 175 billion parameters. So from what we’re seeing highlighted here, rank GPT-3.5 rank GPT-4. This is, you know, different sources here I haven’t heard of, but it’s some kind of ensemble method. And they claim it’s a state of the art neural first stage parse retrieval method so like for different stages of that reranking. So it’s like an added step, so you would expect performance to be better with this added step and performance your NDCG at 10. Now this at 10 is just the at K value. So within the 10 documents. And then this mean average precision at the first 100 documents in that rerank list. And the performance does improve with this this added step.

But the overall findings from this first piece of information is that this 7 billion parameter model achieves comparable performance to these proprietary models of GPT-3.5, GPT-4 that are about 20 to 30 times its size.

Now, Claire, does it talk about how fast it is at all like throughout this paper? Maybe we’re jumping the gun a little, but there is a big emphasis on the size of this model compared to the size of these large language models for a step of reranking. So any thoughts there?

**Claire Longo: **Yeah, it’s really interesting. So the metrics here are great. These are traditional ranking metrics. You got your NDCG, your map at K-100 but we’re so that’s great for measuring the quality of the ranked items, like, how good is the system at actually ranking a list? 

We’re also looking at the smaller table there, some consistency in the output, which we’ll talk about a little bit more. But what I did not see anywhere here was like, how fast is it, and how does it compare to others? But, that being said, this is definitely like a really cool open source model that you have full control of to look under the hood and use, and it’s something it could be built on. So I think it lays some good foundations, even if it’s not fast enough for production yet. It’s definitely worth looking into.

**Amber Roberts: **Yeah. And so this, the second table that Claire is talking about is the number of malformed responses for each re ranking method. So the total is the same for each–the total responses. And then we get missing repetition, wrong formats. And okay, if it’s what is expected the wrong format here includes responses that do not have a given requested format which GPT-4 reranking isn’t doing too well on. For example, it’s saying, rank GPT-4 refuses to generate a sorted list. So that falls into this category. Repetition here includes responses that contain repeated document IDs. So it’s not so, because they’re trying to do one to one mapping like making sure it’s correct. So if they’re repeating documents, then that’s not correct. If they’re getting a format wrong, that’s not correct. And then missing includes responses missing document IDs, so like a mismatched part for the document IDs, which seems to be GPT’s lowest part. So getting the wrong format is happening more for GPT-4. 

Hardly any repetition, but there are a few with missing document IDs, and RankVicuna scored, you know–no wrong format, no repetition, no missing, and Claire and I were talking, we think like this is where they say it is deterministic, and it’s not stochastic. So with LLMs, we assume all of them are non-deterministic, because every time you run them you get a different response. But the reranking that RankVicuna does, they’re saying like, you’re expected to get the same thing every time. And so it’s a deterministic model in that respect.

**Claire Longo:** Yeah, this threw me for a loop. Amber and I were on a call just deep diving into it, trying to figure it out because there was one trigger word that Amber noticed. And I didn’t notice it. But the earlier in the paper actually, if you scroll up to where we first highlighted it, they use the word deterministic, and that was so strange to see in the context of a large language model system, because large language models like this, the way they work is output is probabilistic in the sense that the language model is predicting the next token in the sequence, and there’s a probability of the right token. And so when you rerun this model with the same query, you have a little bit of a confidence bound around what that token could be, and you could actually see, like a different token for a different run. So you’re not going to see the exact same output with the exact same input with these models. 

And so that was very strange. But then, when I think about the task of re-ranking, you do want consistency in the format of the output, in the sense that you want a ranked list, and you have specific things about that rank list–you need the document ID, you don’t want documents to repeat things like that.And so you do need, in a sense, a deterministic system here that’s going to be consistent and give you a ranked list. And I think that’s what they’re trying to highlight here with the smaller table and what Amber is talking through. It’s really interesting stuff.


**Amber Roberts: **And then they say since RankVicuna is deterministic, they’re just going to report the results of a single run. Because it’s the same for every run. It doesn’t get the wrong format. It doesn’t get repetition, doesn’t go missing. And like the three ways you can think of just any model and machine learning like, is this probabilistic? Is this stochastic? Or is this deterministic? Is this going to make decisions based on a probability? Is this going to give you the same results every single time? Is it like shaking in magic 8 ball? And you’re gonna get different results every time. Because that’s the stochastic nature and stochastic gradient descent comes from that comment.

**Claire Longo:** Talking about the speed and how that would depend on the hardware, the deployment system, and Amber, I know, like you were looking at this at the end, too, and we can circle back on that one.

**Amber Roberts: **Yeah, I think the only other thing I had highlighted here is the mention of prompt cost. That it is cheaper to use RankVicuna for prompt cost in comparison. But again, we’re not getting the information on speed for how fast it is, which tends to be the most important for users. For instance, if I’m loading my Spotify like search results and getting my ranked list for recommendations, if the recommendation I want is second and or third versus if it takes, you know, if it’s like instant versus it takes a few seconds, I’d rather it be extremely fast, and my results be there so decent ranking, but very fast output, very low latency than me having to wait for those results.

And then I think this is pretty much just more information on malformed responses results. Here we’re seeing the same thing that everything is comparable to. We’re RankVicuna is comparable to all these large language model reranking systems.

I’m trying to think if there’s anything we wanted to go into, much more because we’re seeing like these first stage candidate generations with repeated experiments. They’re using a bag of words models so just essentially doing word counts as their baseline when they’re doing comparables for these different first stage candidate generations. And then the other thing we’re seeing is data augmentation aspects where the training process for RankVicuna. They highlight the use of data augmentation as a crucial step in their training pipeline. I’ll note these aren’t very large data sets. And that’s one reason why there is going to be a lot of performance when you do see this data augmentation step.

Claire, do you want to talk about the augmentation at all?

**Claire Longo:** Yeah, I think they were doing some interesting stuff on the augmentation, but actually didn’t go deep here. What jumped out to you? 

**Amber Roberts:** I think you’ve mentioned this before that, like teacher-student relationship, that’s for that augmentation step. So they’re saying this data augmentation step involves, like the shuffling of the input order of the documents. And so it’s not like how I’d normally think of data like augmentation. It’s more shuffling is what it seems like here. And then using that to provide a teacher model. 

**Claire Longo:** So essentially, what they’re doing is they’re generating training data examples from that larger model. And then they’re augmenting those samples by shuffling things around really just trying to like, give more examples to the model to learn from here. 

**Amber Roberts:** Yeah. And I think this is necessary because this is not a very large training data. But this is a great example technique that you can use if you don’t have a lot of data. You know, the way we create synthetic data to help train the models for use cases. This can be a really good thing to use if you just don’t have that much data, and you want to be able to use ranking and re-ranking systems. 

So that was just one thing there essentially being that you get better performance if you do this augmented step in that process before you do the re-ranking.

I think I’m just getting into conclusions here.

So what we’re seeing with the conclusions, or what we’ve been talking about throughout this paper, we’re going to highlight, the kind of the main things that this paper shed light on, what we’ve been using it for, what we might use it for in the future. And then, Claire, we could talk about things we’d like to see in the future. And what we might need as someone who understands working in production like what we would need in order to find RankVicuna as a viable approach to use in production.

So let’s start with our takeaways.

A big takeaway being that this model is 20 to 30 times smaller than the re-ranking models that leverage GPT and GPT-4. So that is great. This is incredibly stable. There’s a deterministic approach where you’re getting the exact same results. A bunch of documents are missing IDs. You’re not getting documents that aren’t following the ranking structure that you provide in the prompt.

(Yes, bring Zena in the frame, everyone see? I’m always excited to see dogs. My dogs are too big for me to lift into the camera. Next time. I got distracted, always distracted by dogs.)

But basically showing that they are on par with these larger models the RankVicuna variations. They are open source. So that’s another big area that these models being open source, we are seeing more and more open source models improving on performance, I’d say, being comparable to GPT-3 from the papers I’ve read I still see GPT-4 coming out on top for the majority of use cases. But being able to get semi-close to that point and not having a proprietary LLM is kind of a make or break for a lot of teams. So, noting that this is improving performance around open source large language models.

It also shows the importance for data augmentation and the role it plays in ensuring stability. How stable your document reordering can be, and like the variations, the additional steps you can take in the re-ranking order. Not only is there re-ranking, there’s like a single stage, there’s these additional methods that we’ve seen introduced which can really help in that kind of first stage for that reranking.

I think those are the main things that I’m thinking about and the main things that they bring up in the conclusion of their paper.

For me, the big takeaway is showing the capabilities of open source large language models that essentially condensed versions of larger models, like just how good they can be while also being able to change out prompt engineering. I would have liked to see more variations on the prompt but just the power of prompt engineering is that prompt is really what’s getting it to be so stable in those outputs, and getting these results here, which I thought–I mean, you don’t even think this should be possible. But it is very stable. And this is what’s happening now: very large data sets, I don’t know but these results are pretty impressive, especially when you do have GPT 3.5 and GPT-4 kind of hitting the mark for wrong format and for missing document IDs.

**Claire Longo:** Yeah, I’m thinking the same things like the stability here is really cool and highlights maybe some potential of having a system that’s just really good at one thing. This system is just really good at ranking, whereas ChatGPT, as we all know, is really good at a lot of things. But maybe in some situations, you want this kind of consistency of getting a ranked result.

The other thing that’s super cool is like their prompts look excellent. I really like how it’s constructed, how it’s taking the documents in and forcing a rank out of it as the response. And I would love to see how they kind of iterated and came up with a prompt like that, so that’s something we could dive into.

In terms of next steps, like exactly what this comment is saying here, like, I’m curious to see how it deploys, how it scales, how much it costs, so I probably want to tinker with it in that way. And then also, there’s discussion around vector databases. And how that would fit with something like this, like, if you have a vector database that is very good at efficient re-ranking before. It’s like returning that retrieved list of documents. Do you need a system like this? I think that’s kind of an open question still.

**Amber Roberts:** Yeah, thank you for that response. Yeah, it would be very interesting to see that. Also, that kind of LLM framework that Claire showed earlier. We actually found an interesting conversation, and we have a few minutes left. So there’s no questions, I’m just going to pull it up real quick. Kind of diving into this topic a bit more.

And Pascal Biese is great, I find a lot of interesting papers to read from his post, from his newsletter. But this is where obviously, Nils is going to be supporting coherence, the Director of Machine Learning at Cohere. But he raises interesting points of how long it can take for this step to be added into that process that some of the comments we were getting are showing and being able to use the document embeddings at query time being able to connect them with vector databases, using reranking. And so Cohere–an LLM company-it’s interesting because they’re thinking about this as well. And they’re thinking about the speed and I don’t think it’s Cisco here. I think other LLMs, other vector, database companies are leveraging this area. And trying to think how to get ranking down pat and how to get re-ranking down.

And these use cases are incredibly important for folks who want to leverage large language models in production, but they want to minimize hallucinations.

The paper also did mention that all this was done with a temperature of 0 so trying to get as little hallucinations as possible, so those are the exact kind of questions to think about, and you know how it fits in. But what I’ve learned from this paper is reranking is a necessary step. If you’re leveraging large language models like pool all your documents, and you’re leveraging them to create a response. And you’re leveraging them to decide in which order to select these documents? There’s a lot of questions around that. But it might be almost like another layer, another like a human in the loop. Essentially to do a very stable process of reranking.

Claire, anything to add in this last minute?

**Claire Longo: **I think that covers all that. The only thing I wanna point out is Amber is amazing at reading papers. She’s been doing it for a while, and I learned something from her here. She went to Linkedin. It was like following this conversation and the thread around the paper where someone had posted about it, and I thought that was just like a really cool way to just be part of the community discussion around a paper and hear what other people are saying and kind of validate, like our gut reaction to things, too. So definitely, something that I recommend and like we’ll do going forward is just finding a community to talk to about these papers as we read through them. Don’t read an echo chamber!

**Amber Roberts: ** Exactly. Well, thanks everyone for joining, and you know we’re a community as well and feel free to talk to us. We have a great community on our Arize community Slack, and if you have any questions about this paper or other papers, please let us know. Alright, have a great Wednesday. Thanks everyone.
