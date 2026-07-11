---
title: Hungry Hungry Hippos (H3) and Language Modeling with State Space Models
topic: models
subtopic: reasoning
secondary_topics:
- inference/optimization
summary: Explains H3/state-space model ideas as alternatives to standard attention
  and why they matter for sequence modeling efficiency.
source: arize
url: https://arize.com/blog/hungry-hungry-hippos-h3-state-space-models/
author: Jason Lopatecki
published: '2023-03-29'
fetched: '2026-07-11T04:46:35Z'
classifier: codex
taxonomy_rev: 1
words: 3508
content_sha256: c32caaba1f31e195421fa580612317fdd39bf986bb3c782a7775a42fb9526f1b
---

# Hungry Hungry Hippos (H3) and Language Modeling with State Space Models

![Deep Papers Cover Image Deep Papers Cover Image](https://arize.com/wp-content/uploads/2023/01/Deep_Papers-e1-blog-alt-1-1021x560.jpg)

              # Hungry Hungry Hippos (H3) and Language Modeling with State Space Models

## Deep Papers, a Podcast from AI Pub and Arize AI

** Deep Papers** is a podcast series featuring deep dives on today’s seminal AI papers and research. Hosted by

[creator Brian Burns and](https://twitter.com/ai__pub)

**AI Pub****Arize AI**founders Jason Lopatecki and Aparna Dhinakaran, each episode profiles the people and techniques behind cutting-edge breakthroughs in machine learning.

## About This Episode

In this episode, we interview Dan Fu and Tri Dao, inventors of “Hungry Hungry Hippos” (aka “H3”). This language modeling architecture performs comparably to transformers, while admitting much longer context length: n log(n) rather than n^2 context scaling, for those technically inclined. Listen to learn about the major ideas and history behind H3, state space models, what makes them special, what products can be built with long-context language models, and hints of Dan and Tri’s future (unpublished) research.

## Listen


🎧 **SUBSCRIBE** [Spotify](https://open.spotify.com/show/4sykmDkrUklwyjOCB8FdLQ) | [Apple Podcasts](https://podcasts.apple.com/us/podcast/hungry-hungry-hippos-h3/id1666375694?i=1000599442353) | [YouTube](https://www.youtube.com/watch?v=x_Z9fzYClB0)

## Links

- Read Fu and Dao’s original paper titled [Hungry Hungry Hippos: Towards Language Modeling with State Space Models](https://arxiv.org/abs/2212.14052)
- Sign up for the [Arize AI Slack community](https://arize.com/community/)to ask the authors questions
- Follow Dan Fu on [Twitter](https://twitter.com/realdanfu)and[his website](https://www.danfu.org/)
- Follow Tri Dao on [Twitter](https://twitter.com/tri_dao)and[his website](https://tridao.me/)
- Follow AI Pub on [Twitter](https://twitter.com/ai__pub)
- Learn more about [Arize AI](https://arize.com/)and[signup for a free account](https://app.arize.com/auth/join)

## Transcript

### What’s your one minute elevator pitch for the paper? What are the major problems that you address, and what are the major contributions or results that you came up with?

**Dan Fu: **If you take a very high level view, there are a couple things we’re interested in.

In H3 we were looking at language modeling, and language models these days have one major bottleneck that we wanted to address, which is, they really struggle to capture long context. That’s due to a very fundamental technical reason in the architectures that people are using these days. They’re all using this thing called attention, which has this property where it scales quadratically in the sequence length. So in H3, we wanted to see if we could replace attention with something else. And [our lab](https://hazyresearch.stanford.edu/) has been working on these primitives called state space models for a couple of years now, so we wanted to see: can we use state space models in language modeling?

There were some more technical challenges which I’m sure we’ll have time to get into, basically having to do with comparing words in a sentence to try to do some semantic reasoning. We found that once you solve that problem, you can use state space models and language modeling, and then you can go to very long sequences without scaling quadratically.

**Tri Dao: **One challenge that we run into is the expressiveness problem, but the other problem is efficiency: how do you actually make these things efficient? Because transformer attention came out five or six years ago, there were tons of engineers and researchers who have been optimizing attention, and we’ve also worked on optimizing attention. So with a new model, we had to put in some work to make sure that it runs at least as fast as attention on modern hardware. So, we tackle both expressiveness and efficiency. In the end, I think it worked out pretty well, and maybe it will be able to scale to longer sequences and hopefully get better models that way.

### Not everyone knows what a state space model is. What is it and how is it different versus what’s been done?

**Tri Dao: **So state space is actually an old concept from control theory back in the 1960s. And if you’re heard of a common filter, that’s state space. But more recently people have been putting these things in deep learning. The way they work is you can view them as a kind of linear RNN, but there’s no nonlinearity. The other way to view them is a really long convolution where you’re convolving with something that’s as long as the sequence length.

And then we have some more recent stuff leveraging this connection. Folks in the lab have been working in this direction and they made really exciting progress in the last couple of years, and things like the S4 model seem to be doing really great at some of these long range benchmark tests. So, we’re excited to take that architecture and put it in things like language modeling, which requires a little bit of a twist. I think the high level take is that the state space model is actually quite old. They look like either linear RNN or long convolution. And now we’re trying to figure out how to put them on par with attention in the realm of language modeling.

### Can you give us a brief introduction to attention?

**Tri Dao: **Sure. Attention was [introduced in 2014](https://arxiv.org/abs/1409.0473), and folks were using it in the context of recurrent neural networks. Back then RNN, RSDM, things like that were all the rage. And then in 2017, a team at Google figured out that you actually don’t need all this recurrent stuff, and if you stack a bunch of attention layers, they actually do really really well, and they parallelize really well on hardware. So you can scale these things up and train really well and that has kind of taken over machine learning. I think all applications like transformers and attention are what’s powering all of these exciting applications like ChatGPT, AlphaFold, and Stable Diffusion. The concept has enabled a bunch of really exciting progress. We’re happy to be in machine learning right now.

### Why are state space models so good at doing long context stuff?

**Dan Fu: **I think there are maybe two two ways to look at it. One just from an efficiency standpoint. Tri mentioned that one way of looking at these state space models is that you can look at them as just a very long convolution over the sequence. There’s this theorem from the signal processing literature called the FFT convolution theorem, and it basically says that you can compute a very long convolution using the FFT, and the FFT is another one of those algorithms that is decades old and people have been thinking about it and working on it for a long time. And they can compute it in almost linear time. So, just from a computational standpoint you can just use a much longer sequence.

From a more theoretical standpoint around the actual architecture of what it’s doing, there’s a lot of interesting, rich theory about how this representation can kind of remember the entire sequence and take information from the whole sequence, depending on what you need. So there’s sort of these fundamental reasons that you have very long memory. There’s also just these efficiency reasons for just being able to process long sequences.

### Can you give me an example of a long range task that an SSM would do much better than a transformer on?

**Dan Fu: **A very simple one that I think a lot of people will understand is audio processing. If you imagine your audio waveform, these things will be sampled at like 64 kHz or something. So that means that in one second of audio, you have 64,000 audio points.

If you try to feed this into a transformer, you need 64,000² (squared) different computations in order to do that. And now you’ve blown out your GPU memory, you can’t load your model, and video SMI is going to say: Oh I can’t do that any more. With an SSM, not only can you process it, but you also have a chance of actually kind of modeling how the audiowave form changes over time, and that’s one example of how SSMs have shown a lot more power than transformers.

### You have some examples in your paper of a very specific long range task like recall–what’s an example of a long range task like recall that you tested against, and maybe also describe some of the data sets out there that people are testing against.

**Dan Fu: **So in H3 we were very interested in language modeling, and there’s a few ways that you can look at it. Let me give you an example sentence. So if you have a sentence, like: President Obama went to the park with his dogs and met Michelle (Blank). And the question is what is the word that is going to come after Michelle? As humans, we know that the answer is going to be Michelle Obama, because at the beginning of the sentence we were talking about President Obama, and so that’s an example of one of the tests that we were looking at. So there’s a token at the beginning of your sentence and near the end of your sentence, can you recall it? Hence the name “recall.” That’s one of the tests that we were looking at.

In our paper we actually found that SSMs could not immediately do that recall. And the reason is a little bit interesting. One way to look at attention is you’re going to be making comparisons across your entire sequence, and that’s why it’s quadratic. So if you get to the end of the sentence and see “Michelle,” you’re gonna be like “Okay, there are a bunch of different words that can come after Michelle, let me go one by one with every single word in my sentence.” President… Michelle President? Maybe not. Obama…Michelle Obama? Sounds right. But then I’m going to keep looking at Michelle park, Michelle dog, Michelle, etc. So attention can do it by brute forcing it and kind of saying Okay, I’m going go look one at a time at each word.

But with a state space model what we’re able to do is encode a little bit and say maybe there’s a concept that you should remember throughout the whole sequence? Maybe this President word or this Obama word? Like, If you think about the sentence, the words that you probably remember, maybe something about a dog, maybe something about a park or something about a walk. So, one intuition is that the state space model allows us to have a model of what to remember from the sentence so that you can recall it at the end.

**Tri Dao: **To add to that, right now there are a bunch of applications that would benefit from this long range interaction. One is obviously ChatGPT. So when ChatGPT came out, one feature OpenAI advertised was that it has great memory. So for attention right now we’re kind of brute forcing it, and we just compare against all the words that came before. Even though these models are really large, the context lane is actually not. Or we’ve talked to folks who are doing things like co-generation: if you’re editing a file, can it suggest things that are from a completely different file in the same directory or from different directories or from the libraries that you’re importing. So somehow it has to remember what’s in the library or in different files. There are a bunch of really new AI applications that could benefit from this long context. And this is why it is an area that we want to make progress on.

### What’s novel about this work? You mention other people have been using state space models to do this kind of stuff, but obviously they haven’t been able to perform as well on various language benchmarks. What are some of the new key ingredients that you found that made this work so well?

**Dan Fu: **Part of this answer will explain why it’s a hungry hungry hippo and just a single hungry hippo.

If we go back to this recall example from before, you get to the end of the sentence and you see Michelle, and now you need to see what things are associated with Michele. At the beginning Sentence we said President Obama, So we’re going to say: Okay, Michelle, President, there’s some sort of relation there.

So we took two SSM layers (and that’s why it’s hungry hungry, because there’s two of them). We gave it a representation that can kind of say: do a little bit of comparison nearby in the sequence, So it just gives you enough ability to compare Michelle to the words nearby or other words in the sequence.

And then the other hippo is doing that memory thing. So the other hippo is remembering words from the entire sequence. So between this first hippo that can do this comparison, and then the second hippo is remembering words through the whole sequence, then you get to Michelle, and then you can say there’s President, that appeared some time ago, So now we can bring out Obama as the next word. For those who are listening who are kind of more technically inclined, the physical mechanism that we use is called a multiplicative gate. All that means is that we take the outputs of these two hippos and we multiply them. That’s kind of how we do the comparison.

**Tri Dao: **Part of it is inspired by attention. Of course, with attention, you have tokens interacting with each other. I think this gating idea actually goes back a long time to even in RNN, things like long and short term memory and LSTM, they were doing this kind of gating. So people working in recurrent neural nets were thinking about these things ten years ago. Folks at Google who were thinking about this kind of multiplicative interaction as well, and there’s [concurrent work](https://rush-nlp.com/). We’ve been chatting with them exchanging notes, because we see that this multiplicative interaction actually makes it work well for causal language modeling. And they were working with mass language modeling and they also found that this multiplicative interaction is quite helpful there as well. So I think some of these old ideas are coming back and becoming useful again. So that’s more on the modeling side.

The other side is this efficiency side. If you want to scale these models up to be large, that’s actually really expensive to do. And if you don’t have the right framework, if you don’t have the right optimization, it’s actually really hard to do. So we’ve been working hard to make these things efficient so that we can scale to relatively large models. And of course we scale larger given the budget. But thinking about taking some of the ideas from existing literature on expressivity and multiplicative interaction combined with improvement in efficiency I think is what enabled us to do some of this work.

### How do you measure the expressivity? What was your way of comparing across these types of data sets, how did you measure that?

**Tri**: You can measure them through performance on the task that you care about. For example, nowadays people do language modeling and they measure either perplexity, which is a metric on the upstream pre-training, or measure the zero shot, or few shot evaluation on down stream. That means how well can you prompt the model with some examples and can it then figure it out. This is called in context learning, which is pretty expensive to evaluate. I think Dan can go into more detail on some of the toy tasks.

**Dan: **Yeah, so as Tri mentioned, one way to test is just train a big model, wait a week, then at the end see if it works. But that’s a very expensive way to do research. Maybe at certain nameless large tech companies that have too many GPUs and other hardware, maybe that’s something you can do, but as a couple of grad students it’s not something that was quite available to us, so we put some effort into developing toy tasks.

So Jason mentioned recall. The toy task here is to come up with a fake little language that has ten words in it, and then you give it a pattern. So one is associative recall, and you just have some words be keys, and then some words to be values. An example is: A, three, B, two, C, four, D, one. And then you say “A” and then you have the model try to predict what comes next.

And so this is kind of a very toy version of that President Obama, Michelle Obama and the park example. And that’s a task that you can run in minutes on your computer. And we were finding that S4 and some other things by themselves before H3 were having a lot of trouble doing that, But then when we designed H3 we saw we saw that it could kind of pick it up immediately, and then that gave us the confidence and then go start the expensive runs and do the big downstream evaluation.

### Could you talk a little bit about the results? The results that you mentioned in the paper are very impressive, both for your pure H3 language models, and then also the blended one where you throw in like two attention layers.

**Tri Dao: **Sure. In some of the large benchmark tests we saw that  H3 does almost as well as a transformer. There’s still a little bit of a gap that we want to  figure out– I think transformer and attention in particular, doing something pretty powerful. We don’t completely understand all of that yet, so we make a step towards understanding what a transformer is doing. Can we achieve the same thing with a different architecture?

And as you mentioned, when we mix it with one or two attention layers, we see really promising results. So, on some of the larger language tasks we saw that this hybrid architecture does this as well, or slightly better than a transformer. That’s really encouraging because the transformer has been an architecture that’s been there for five or six years. We were able to get some models up to about 1.3 billion and 2.7 billion language models that do about as well as existing transformers like GPT Neo. So that’s pretty pretty encouraging and we’re excited to either scale that up or figure out a way to do even more efficient inference. I think inference right now is a big big concern for most folks who want to deploy these things, and we believe that state space methods could be much much more efficient during inference. We haven’t done as much work optimizing the inference, but we already saw some early promising results that show these things can do inference quite a bit faster. So that would be fun to push on and either scale things up or optimize the inference piece.

### A lot of product people and fans of AI right now might be curious: what are some product applications for what you’re building? And how could someone leverage the blended architecture you came up with?

**Dan Fu: **One I think that we’ve mentioned a couple of times is code generation. So you’re writing a code file and you have some import at the top, and it’s very important context for code to work. But you’ve written a very long code file and you’re at the bottom, so your CoPilot (or whatever the next version of copilot could be) would be useful to kind of look at that, and be able to have that context. Or maybe you have a file, and you have some piece of code in another file that’s very relevant. Or maybe there’s some comment somewhere in some other part of your code base, so code generation is very compelling.

Video processing is another one of these. Your average Youtube video these days is at least ten minutes long, sixty frames a second. That’s thousands and thousands of frames–way longer than anything that a transformer can process these days.

People have also talked to us about biological applications, and one of the longest sequences that we deal with on a daily basis is our DNA. There’s a lot to do there with understanding the genetics and genomics. So those are three examples that we’re very excited about but i’m sure there’s many others.

**Tri Dao: **There are these new AI workflows that are much more interactive. So with Chat GPT as I mentioned, you go back and forth with the chat bot: you ask it to do something, and then take some actions and you can either correct or accept these actions. So these multi-turn user interactions are going to be really important.

There are folks building things like automatic slide generation. You ask them to make ten slides on this thing and it would go back and forth and give feedback. These things are going to be everywhere, and they’re going to require interaction between users and the system. Long-range context is going to be more and more important in the future for these workflows.
