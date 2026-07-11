---
title: 'Toolformer: Training LLMs To Use Tools'
topic: agents
subtopic: tool-use
secondary_topics:
- models/reasoning
summary: Summarizes Toolformer and how language models can learn to use external tools.
source: arize
url: https://arize.com/blog/toolformer-large-language-model-meta-ai/
author: Jason Lopatecki
published: '2023-03-21'
fetched: '2026-07-11T04:46:43Z'
classifier: codex
taxonomy_rev: 1
words: 3430
content_sha256: 6663db18e8f74c946169928a2180d0199269d54e4896fe457f3d393cf585225b
---

# Toolformer: Training LLMs To Use Tools

![Deep_Papers-e1-blog alt Deep Papers Toolformer](https://arize.com/wp-content/uploads/2023/01/Deep_Papers-e1-blog-alt-1021x560.jpg)

              # Toolformer: Training LLMs To Use Tools

## Deep Papers, a Podcast from AI Pub and Arize AI, Presents a Conversation with the Meta AI Research Scientists Behind Toolformer

** Deep Papers** is a podcast series featuring deep dives on today’s seminal AI papers and research. Hosted by

[creator Brian Burns and](https://twitter.com/ai__pub)

**AI Pub****Arize AI**founders Jason Lopatecki and Aparna Dhinakaran, each episode profiles the people and techniques behind cutting-edge breakthroughs in machine learning.

## About This Episode

In this episode, we interview Timo Schick and Thomas Scialom, the Research Scientists at Meta AI behind Toolformer. “Vanilla” language models cannot access information about the external world. But what if we gave language models access to calculators, question-answer search, and other APIs to generate more powerful and accurate output? Further, how do we train such a model? How can we automatically generate a dataset of API-call-annotated text at internet scale, without human labeling?

Timo and Thomas give a step-by-step walkthrough of building and training Toolformer, what motivated them to do it, and what we should expect in the next generation of tool-LLM powered products.

## Listen

🎧 **SUBSCRIBE** [Spotify](https://open.spotify.com/show/4sykmDkrUklwyjOCB8FdLQ) | [Apple Podcasts](https://podcasts.apple.com/us/podcast/toolformer-training-llms-to-use-tools/id1666375694?i=1000605075518) | [YouTube](https://www.youtube.com/watch?v=pSKHDduKt_g)

## Links

- Read Schick and Scialom’s original paper titled [Toolformer: Language Models Can Teach Themselves to Use Tools](https://arxiv.org/abs/2302.04761)
- Sign up for the [Arize AI Slack community](https://arize.com/community/)to ask the authors questions
- Follow Timo Schick on [Twitter](https://twitter.com/timo_schick)and[LinkedIn](https://www.linkedin.com/in/timoschick/)
- Follow Thomas Scialom on [Twitter](https://twitter.com/thomasscialom)and[LinkedIn](https://www.linkedin.com/in/tscialom/)
- Follow AI Pub on [Twitter](https://twitter.com/ai__pub)
- Learn more about [Arize AI](https://arize.com/)and[signup for a free account](https://app.arize.com/auth/join)

## Transcript Highlights

Edited for length/clarity.

**Can you give us the elevator pitch for Toolformer? **

**Timo Schick:** If you play around with one of those recent very large language models, they can do all kinds of amazing things, but there are also some limitations that you can find very clearly when you just play around with them for a few minutes, mostly because they’re not connected to their external world. But there are also some skills that humans find very easy that those models just can’t do, so a very natural way of making them able to connect to the external world, do calculations and all kinds of things, is to just try and equip them with the ability to communicate via APIs, or via external tools. And that is  basically what I would say this project is about.

**Can you go a little deeper on just what these limitations are? We see examples where for instance, chatGPT can’t solve basic math problems, but can you give some examples of what motivated you all? **

**Timo Schick: **I think one of the big motivations is obviously having up-to-date information about events, that is something that people want very often when they chat with models. They want to have comments about things that happen in their daily lives, and this is something that clearly those models can’t do when they’re not connected to the external world–you don’t want to retrain them every day. So i think that’s one of the biggest things

And then there are other things like for example calculations and translation that those models theoretically can do, but it just needs a significant scale and very, very strong models to do that. So, using tools in those cases is a way of getting similar performance but with much smaller models. And then there’s also all different kinds of things like if you want to do some complex tasks you might want to have a model that can execute some kind of code maybe or you want the model to get some context about you personally when you ask questions and I think fundamentally all those issues could be addressed with different kinds of tools.

**What are some of the heavy hitters right now where you see some of the large language models really struggling? **

**Thomas Scialom:** I think Timo mentioned updating information, even more general than that is the sense of the notion of time: what happens when, before, yesterday. I mean obviously the training objectives have been supervised. You extract the paragraph randomly, you shuffle your data, you don’t provide any information about when this paragraph was written, you don’t have any metadata. So, you can’t expect the model to learn that.

**Timo Schick: **Let me also get one more example of one of those abilities that those models don’t have. So we have temporal awareness, updatability, math. Another thing that you won’t find in the toolformer paper but that I would still believe is one of those things that tools could address is the way those models work based on transformers  with their quadratically time complexity self-attention means usually can only look at a limited context window. Usually they can look at 4,000 or maybe 8,000 tokens but  nothing beyond that. And you might think of many cases where that is not enough but you have a long document that you want to ask questions about or that you want to work with.  I think this is also something where you could think of tools that allow you to somehow search in the document that you’re currently operating in or do some other operations to address that limitation.

**Could you run through how a language model actually uses these tools? All these language models do is take the context and then spit out the next token, add in the context, and you spit out the next token, etc. So how does a language model use different APIs just given that all it can do is just spit out the next token? **

**Timo Schick: **In the current version of the Toolformer we have one limitation that we impose upon those APIs and that is they need to be text to text, so the input that you give to those APIs should be representable in some way as text and the same should be true for the output. And basically how those models can then call tools is they would first generate text as long as they want. Then we allow them to generate one special token–one special kind of word–that would signal: now I want to call an API. And after the model has produced this kind of token, we then do some kind of a constraint decoding where the model first needs to specify which tool it wants to call and can then also specify the parameters it wants to call. And then it will finally produce another token which says now I’m done, now I want to get the result. And this is basically where we interrupt the decoding process, we stop it from producing any further tokens, we do that API recall so we call our calculator, or we look something up in our calendar, we do a search, and we get the result from that which is also a piece of text and we then just put that into the string that the model has already produced and after that we let it continue writing text.

**Why start with the set of tools that you started with? What was the reasoning behind that? **

**Timo Schick: ** One of the things we wanted to do is we wanted to work with a publicly available language model. And by today’s standards the language model is relatively small and not as capable as some of the models that people might have experience with. So, what this means is the tools could not be too complicated. For example, writing python code might be something that this model isn’t good enough at that the approach would work, so that was one criteria was trying to find tools that are not too hard and always relatively clear how you could use them.

And the other thing is obviously we wanted to try tools that address some of those fundamental limitations. You can think of a lot of tools that are very specialized and that would be helpful in very specific circumstances. We tried to find tools that are somewhat general, and obviously we also wanted them to be kind of diverse. So you can see we have one tool that is based on a language model, one tool that uses BM25 retrieval, we have a calculator; we wanted to see whether the same approach can work for different kinds of tools that are very diverse.

**Thomas Scialom: **This paper is just the first step in this direction and we wanted to maximize the diversity of the tools. We see there’s a lot of things that could come now and so it’s just a proof of concept that using tools and diverse tools like calendar search,  local search, or global search with information will work. And now that we have proof of this concept there are a lot of things to explore.

**One of the main problems with training these tool transformers is getting the right data. Part of the problem is you can’t because of the scale of these these text data sets is so large, you can’t just pay human labelers to do it so there’s kind of a setup where you have to generate these huge API annotations but you also have to do it in a kind of automated way at scale. How did you guys do that, what are the key ideas? **

**Timo Schick: **I can maybe quickly walk you through the process on a high level. One of the things that was very important to us was that we wanted to avoid having huge costs from humans having to annotate data and also we wanted to find an approach that works with whatever data set you care about.  So if you had a specific data set that you want to train your language model on, we wanted to find some way of using that specific data set and adding two calls to that, regardless of whether it is general language modeling or an instruction tuning data set or some very task-specific data, that was kind of one of the the premises that we worked with.

And then the basic idea is that we proceed in three steps. The first one is we just take this large piece of text that we want to annotate with API calls and we use a language model to sample a massive amount of different API calls.The way we do this is we use the in-context learning abilities of pre-trained language models. What that means is basically if you show a pre-trained language model in its context window three examples of inputs and corresponding outputs it can often do a relatively good job at creating an output for the fourth input that you would show it. So for each API we give the language model this prompt and we say: you have access to a question answering API, you should annotate text with API calls wherever you think those might be helpful, here are some examples. And then we give it three examples of an input and the corresponding output would be the same text with API calls inserted, and then we ask the model to do the same for a fourth text.

**When would the model know when to call a tool? How does a model know that this is an area where I could get it wrong, so I should call a tool?**

**Timo Schick:** I think the key thing is that at this step the language model really doesn’t know. So what we do is just massively over sample API calls. Now if you give a language model those examples of inputs and corresponding API calls, it will start generating API calls for new texts, but they will very often be at the wrong place or they will just ask for information that is completely irrelevant. In general, what we observed is that depending on the tool between 90% and even 99% of all the API calls generated were just completely useless, so this is something that we need to live with at this point. Obviously as you move to better models, and as you move to bigger models that might become a bit better. But with the model that we experimented with, a lot of the API calls really don’t make any sense at all. I think we have a figure or a table in the paper where we show some of the good and some of the bad API calls that will give you an idea of how bad those bad API calls are, and as I’ve said 90 to 99% of them are really bad.

**So, if you don’t want to train your model on lots of bad API calls, what do you do to handle the 90 or 99% of the API annotations that you’ve generated to only include the good ones? **

**Timo Schick: **To me this is the most interesting part of the paper because obviously we want to find some way of distinguishing good from bad API calls. We don’t  want to have humans involved at that point because again that would be super expensive and also which API call is useful really depends on what you already know and who you are.

So for example as a human you might know where Joe Biden was born and you’d say oh well I don’t need to call an API for this, and maybe a gpt3 model also knows that and says I don’t need to call an API. But maybe a much smaller model like GPT-J doesn’t know that and needs to call the API. So what makes a good API call? I don’t think there’s a universal answer. I think it really depends on what you already know and what kind of information you still need.

And with that in mind, we said okay our idea is we’ll just try to measure whether this API call is helpful to the language model itself in doing its actual job which is just continuing the text and producing the next few tokens. So what we do is, given an API call, we look at the next few tokens that come after the API call and then we look at the probability that our language model would assign to those few following tokens if there was no API call, and we compare that to the probability that it would assign to those next tokens that we know to be correct if we do the API call. And only if this probability increases by a certain threshold when we do the API call, that’s when we say okay, apparently this API call is helpful because it makes it easier for the language model to predict the next few tokens. And this is basically what we use as a filter criterion.

**Timo Schick:** I think this is a strong idea here because one of the limitations in my opinion of self supervised learning is you can think about self-supervised learning as a paragraph and we try to predict some tokens based on the context nearby, and like they are kind of like a log of thoughts but only a log, and there’s a lot of hidden context that we don’t provide. If you ask me a very complex question maybe we’ll just ping on my calculator and give you the answer, but if you train the model to predict that directly without the calculator it’s arguably something very hard which actually maybe even amplifies the hallucination problem. Because with the lack of context if you are asking, something like: The King of France was….? And you don’t have any more context except maybe the date, arguably you are emphasizing hallucination. And so maybe adding the tools here help to capture some of the hidden parts of the reasoning for additional context.

**So**** you’ve generated this massive amount of API calls to annotate your data set: they’re not very good, you filter them using this kind of clever mechanism, you cut out 90 or maybe 99% of the bad ones, and now you have a data set that is annotated with these API calls. What do you do? How do you actually use that to get the language model to use the tools? **

**Timo Schick: **So like there are two steps here. One that is very important: all of that filtering we do for each API separately but then obviously before that we use the data set to do anything we merge all those API calls. So that means even though we  generate the API calls independently, in the end we end up with a data set that contains different API

calls four different APIs sometimes in the same example um so we really have this nice mixture of different APIs in one data set.

And then the final step is actually very simple: we just train the language model for a bit longer on this new data set with API calls. And because we selected our data that we annotated the API calls ourselves, we can basically use whatever data we want. In particular we can also use the same data that the model was trained on in the first place. So if you do that additional fine tuning it won’t lose any of its generality, it won’t unlearn things that it learned during pre-training because it’s still the exact same data distribution. The only thing that is new is that now it’s trained on data that contains those API calls and as we discussed earlier of course we have those special API call tokens in there and the token that says now I want to wait for the result and so much is training on that data the model automatically learns to call those apis and because it generated the API calls itself and it’s got them itself it will only do them at exactly those positions where it really thinks that they are necessary and where there’s useful information to be expected.

**What does the future look like? What are the next areas of research that  you’re excited about and where do you see this going?**

**Thomas Scialom: **I think one of the obvious next steps is to have multiple tools and multiple steps of calling the tools, which was one of the main limitations of this first paper.  That skill is the next big thing if you want to add more. There are many more things to do, but the one that seems the most obvious.

**Timo Schick:** I think in general given that all of our API calls are created independently as Thomas said, you won’t find examples where the model first uses one API then uses that information to call another API etc., so that is obviously something that I think would be interesting to study. I’m also personally really interested in the idea of

having maybe the model itself as a tool, so you could just say: okay I need to do a bit of reasoning about something before I get a response so I want to call myself as a tool in a kind of reasoning mode prompted in a particular way. And then use that result. And in particular if the model calls itself then you basically get for free those kinds of hierarchical trains where the model that called itself could again call itself or it could call another tool and so that allows you to have much more complex interactions with those tools which I think would be very interesting to study.

**Hypothetically, in a world where people are using these and calling tools and using  it to take actions, do you think there should be some constraints on what kind of calls can be made? **

**Timo Schick: **Well I think like  for the for the current version of tool former we deliberately lead to chose tools where this is  not really an issue,  I think this is like even more pronounced when you get from this kind of  passive tool use that we have right now, where you just use the tools to get some information.  Or what Thomas described earlier where where you want  the model to act where you have kind of tool use  that actually changes something in the word and I  think at that point it becomes like a a really a  problem that we need to think a lot about and be  very very careful about what kinds of abilities we  give to those models and what we really want them to do.
