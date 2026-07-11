---
title: 'Towards Monosemanticity: Decomposing Language Models With Dictionary Learning'
topic: models
subtopic: reasoning
secondary_topics: []
summary: Summarizes monosemanticity and dictionary learning work for decomposing language
  model internals.
source: arize
url: https://arize.com/blog/towards-monosemanticity/
author: Sarah Welsh
published: '2023-11-02'
fetched: '2026-07-11T04:47:57Z'
classifier: codex
taxonomy_rev: 1
words: 5040
content_sha256: f35ece7e805c956e13e8bda22056d1b8e533a08d6a31ad3435790a4a79795ec0
---

# Towards Monosemanticity: Decomposing Language Models With Dictionary Learning

![Community Paper Reading - Jason and Harrison blog (1) Jason Lopatecki and Harrison Chu headshots](https://arize.com/wp-content/uploads/2023/11/Community-Paper-Reading-Jason-and-Harrison-blog-1-1021x560.jpg)

              # Towards Monosemanticity: Decomposing Language Models With Dictionary Learning

## Introduction

## Watch

Dive in:

Listen:

## Transcript

### Overview of the Research

**Jason Lopatecki, CEO, Arize AI: **This is a really good one. I actually think the work done in this paper is pretty amazing. You know, the thought in the write up around it is probably some of the better visuals, some of the best put together kind of insights. I thought it was really well done.

**Harrison Chu, Director of Engineering, Arize AI: **Yeah it’s pretty rare that you get to paper this length and wish there was more. I mean there was just an intense, amazing amount of stuff that’s pretty applicable. Pretty mind blowing, so I’m excited to go through it.

**Jason Lopatecki: **Why don’t we kick it off? Harrison put together just an overview, a couple of slides with quick takeaways of the paper, and then we’ll probably go through that first, which gives an overview of the ideas and material behind it, and then we’ll hop into different sections and different visuals within it. So for all of you don’t know what this paper is, Anthropic put out a paper around understanding, it’s kind of an interpretability paper, and I guess the background is, there’s been a lot of approaches which I completely think are the wrong direction, and I think they made a really good case here. So this is one of the best approaches I’ve seen for understanding interpretability inside these large language models.

Harrison will start with the material here, and then we’ll hop directly into the paper.

**Harrison Chu: **Cool.Thanks for coming everybody. What I was thinking I would do with these first few slides is to just break it down a little bit. So we’re all on the same page. As to the bigger the bigger ideas of the paper before we dive in. So I think Jason set it up quite well already. The problem is, you have these really large neural networks and we don’t know exactly what’s happening there. And why do we care? Well, if we have a mechanistic way of interpreting these models, we have a better way of steering them, controlling them with safety, alignment. 

Usually the analogy I give is, if you’re a mechanic, you should know something about how cars work–you don’t just want to know if you press the gas pedal the car goes. You need to have some understanding of the reasons as to why the car goes when you press the gas pedal, so you can fix the car when it brakes, or even make improvements to it. So that’s the general motivation behind why we want to do this.

What does the paper mean by monosemanticity? I think the easiest way to think about it is just, you look at this meme that’s about existential risk neurons. It says: Just turn it off and you’re safe from us.

![existential risk neuron meme](https://arize.com/wp-content/uploads/2023/11/Screenshot-2023-10-31-at-2.05.59-PM-300x290.png)


Why is it funny? Well, I think it’s funny, because we all intuitively probably get that a single neuron doesn’t encode these human-level meaningful features. And in the first part of the paper, they say that the most natural unit is the neuron, but it’s probably not the unit we want to be looking at for human understanding. But because we’re humans, we do want some unit that represents a monosemantic, like a singular aspect of reality. Maybe it’s, you know, the likelihood that a text is Arabic or something, that is model semantic. That’s what the paper sets out to try and find, that is being said, we’re gonna take just a small detour to dive into what they mean by dictionary learning and the specific technique of dictionary learning they use.

**Jason Lopatecki:** So one thing I would note on the single neuron stuff…OpenAI put it out a paper–I think we did a paper reading on it–which was trying to use an LLM to understand the individual neurons within an LLM, and I think that the direction they’re going here, which is understanding the way in which things learn, it’s makes a really good case that individual neurons are not going to map to a single idea. As easy as it sounds like for us, if that was the case, it would be great. It’d be easy. But it’s just not how these models are trained or learn. The multiple neurons work together to create a vector and embedding and those represent those look to represent things that can be mapped to things that we we might interpret as a human, which is what the paper does.

**Harrison Chu:** Totally. And Jason, I think you had a great point before about how it’s a very human thing to want a single neuron to mean something, because it’s something we can mechanically see, and it’s something we can understand easily. But that’s totally not the case. The authors here make the case that many neurons are polysemantic, and all that means is you can show it a token that’s Arabic, and another token that’s numbers or English. And the same neuron will fire and might fire intensely. 

But we still need some unit to understand these features to be in, to reason about it. And so, going back to the brief detour here, you know, towards monosemanticity, using dictionary learning, the specific technique they will be using is something called an auto encoder. And what you have here is just a super basic example of what an autoencoder neural network will look like. Typically in these cases, the input layer the loss function is so that you’re training the identity function. So the input and output is the same.

The trick is in the hidden layer. You typically have a small amount of neurons. And what you’re doing is you’re training the network to find a compressed encoding of what’s going on in the input.

Anything you want to add here, Jason?

**Jason Lopatecki: **No, I mean, I’m gonna hit on some ideas later on autoencoder stuff. But that’s exactly it. It’s trying to discover features that represent whatever you’re looking at internally.

### Problem Set Up

**Harrison Chu:** And so the problem set of the paper is the authors take a simple transform with a single layer NLP multilayer perceptron, and train an autoencoder on the activations of the neurons of that feed forward network. And so the meat and potatoes of the paper just goes on in the boxes that that are orange, that you see and in the paper it says, well, the autoencoder is sparse and over complete. That’s actually two very important details. If we Zoom in we can show exactly what they mean.

**Jason Lopatecki:** Yeah, the word features on the right can be kind of confusing because features are used so often in the network. So on the left, what you have are the neuron activations on the left, and almost you have on the right are kind of like what we’re going to find is human discernible features or dictionary basis features that describe human-like things. So we’re mapping from a vector and embedding within the transformer layer to a set of human discernible dictionary features.

**Harrison Chu: **Exactly, and I think it is confusing, because it’s a bit circular. And the authors put it in quotes here, right–the features here are what the authors hope to recover as these like monosemantic, interpretable units. You’re exactly right. And if you zoom a little more you can just imagine that their attaching weights from these neurons to the hidden layer of that auto encoder. And now the very, the novel thing between what the authors are doing here versus the auto encoder here is that bottleneck is over complete.

What that means is, instead of trying to compress information, they’re actually trying to way out, and increase the dimensionality of it. So you can see in this example here, you know. Just suppose that there’s a toy feed 4 network here with 2 neurons. They’re going to expand it to 5, something greater. And in reality it’s 512 to, you know 131,000. You can see it in the graph on left. So it’s over complete in that sense. And it’s sparse. So during training, what they force the network to do is almost at these features are one-hop encoded, since back to that monosemanticity thing is what they hope is something like. Whenever these are activated, you only get feature one that’s activated from neuron one and two, or feature 3, 4, 5, or so on. And so that’s how they coerce this again. The authors have features in quotes, because they don’t know if they’re gonna recover features from it. But that was one way of getting at it.

**Jason Lopatecki:** Yeah, I think it’s a good point now. It’s not exactly 100 and coded. They’re just trying to find a sparse mapping, so a handful or small number of these features can work together. But exactly that. It’s a, you know a handful of the features actually describe the set of activations.

**Harrison Chu:** okay. So then, this is the really interesting part of the paper. Again, we’ll go into the details after. But so in this sort of setup, assuming that we recover from these sparse features in the auto encoder, will semantically map to something. Well, what is a feature like if you really ask rigorously, mathematically, what is a feature? And I’m going to try and explain this with a picture behind some of the technical jargon. Here, you know, empirical event evidence suggesting that neural networks have interpol linear directions and activation space.

So going back to the example here, if you have these neurons that are firing based on some tokens and say you are dealing with a network with three neurons, and if you plot each of these points in space–it’s 3D space–and now just imagine a case where what you’re plotting turns out to be a box or something like that. Imagine you have a three neuron MLP for a cat picture like classifier. And so these points are being plotted on the square.

What the authors are saying is that what is actually a feature is the basis vectors that span this vector space. And so you can reframe your question as: well, every feature is a basis vector and so maybe cat image 33 that is somewhere on that box is cuteness plus fluffy plus whiskers. And, moreover, you can combine these basis vectors to create more complex features. And I think that’s a very interesting and insightful reframing of what a feature is. It’s not a singular neuron. It’s a direction of points of activation space. And it’s just a fascinating sort of geometric way to look at what’s happening and these neural networks.

I have one more down to earth example, but Jason is there anything you wanted to add to that?

**Jason Lopatecki:** No, I mean, as you know, some of us have been applying UMAP to transformer embeddings for quite a while from, say, Llama models. And I think it’s clear that there’s some topology, transformers are learning ideas, and those ideas are represented by topologies that are learned in that space. And that’s kind of what you’re essentially doing here, except you’re mapping it to a set of dictionaries, and the dictionaries are these basis factors. And so, I think that fast forward a couple of years here, I think there’s a massive amount of interesting work to be done on how topologies mapped out by embeddings or the vectors within transformers, map to concepts or ideas. 

And then there’s the big thing they hinted in there, and we’ll talk a little bit about it, which is: are these topologies that are learned, model-specific or if you compare multiple models trained on different data, would they learn the same topologies? And can you start to find similar ones as you look at lots of different models. So the big idea, is information represented by topological structure? And is it common across different time, you know, totally different training runs for models, and they kind of hit at that in the paper.

**Harrison Chu: **One last example. If basis vector or subspaces is not part of your common data vocabulary, this is just an even more simple example of what we’re trying to illustrate. In the scatter plot, if Y-axis is the activation of neuron one, and if X-axis is the activation neuron two. And each point is an example that you feed into the network that you get these activation intensities from. What the feature is, is a vector in some direction of that scatterplot. That’s it. It’s not. It’s not neuron one. It’s not neuron two. It is the direction of some subset of these plots of data, and there can be infinitely many of them. There can be five of them. There can be 10 of them, and what you get back is just how much you skilled the auto encoder in the hidden layer. So, just a fascinating way to look at it. 

And I will hand it over to Jason for the rest of the paper.

**Jason Lopatecki:** So we’ll hop in to kind of go through some of these some of the sections here, and feel free to, you know, throw out questions or ideas, or thoughts. 

So, the beginning kind of gives the background, which I think is, you know, the problem set up and what they’re gonna do, what they’re going to go through. If you haven’t seen it’s a really well done piece of research that includes things like interactive analysis and in the beginning they kind of do the summaries results. We kind of talked about which is I mean, it’s clear you can use a sparse encoder to extract the features that represent human level ideas–you know Arabic or the base 64 encoding, or cat cuteness–and I think it’s clear they did a really good job of actually showing that these can be extracted.

There are some really interesting ideas about how the features work together, that they can actually explode the feature space into larger sizes that you could tune the auto code, or you can choose a smaller encoder, get less features, or you can get more visibility by actually increasing the size and having things more subtly represent different feature sets. I think we talked about this a lot, so I’m not going to go through too much. One note is they did choose a very small transformer here. So it’s one layer like this is done on a very simple setup.

We talked a bit about the feature decomposition. So this is kind of what they highlighted previously, what you said about dictionary learning, which is mapping a set of data and activations to a set of dictionary basis functions that might be over complete within the space. As you’re thinking about this, the dictionary kind of basis functions represent those human readable, and understandable things that make up your data.

They kind of give the example of the problem, which is, if you imagine in this blown out space where maybe things aren’t superimposed, and they’re kind of putting this hypothetical disentangled model, which also kind of represents the dictionary learning problem, too, that you’re trying to learn this like very large sparse matrix that represents your data in an expanded form, and disentangles what is your low dimensional projection.

There are a couple of questions here. 


**Question from the audience: **Thinking of vector space terms, can this process be thought of as principal component analysis or singular value decomposition, perhaps. Not exactly, but it’s a useful analogy. 

**Jason Lopatecki: **Yeah, if you look at what dictionary learning is, it’s very related to SVD. SVD is more a general thing, where the other constraint I think on dictionary learning is the activation is supposed to be sparse across the dictionary terms. So, maybe it’s a special form of some of this. 

**Harrison Chu: ** I think there’s an even more intuitive point here, sparsity is definitely a thing, but in SVD you’re typically going from many dimensions in trying to extract out the smaller amount of like lesser dimensions. And you know the interesting things from this paper came from when they took the inputs–which is 512 dimensions–to a higher dimension, and it maintains sparsity. And you won’t be able to get that with SVD, but you could with this autoencoder approach.

**Jason Lopatecki:** Yeah, but definitely related in terms of its matrix factorization, and trying to get a set of matrices that represent the original one. So I would say, related in that sense. 

**Question from the audience: **How do you assign meaning to the basis vectors of your new expanded feature space? It’s a similar problem to general embeddings, at least in scaling down with UMAP, you might be able to visualize it and guess it?

**Jason Lopatecki:** So this is a good question actually. I think I want to go through the paper– It’s a similar problem that we have in UMAP or any of these things where you end up with a feature, maybe a dictionary feature. But then this feature activates, so in this case, this dictionary value, this dictionary, which is a basis vector activates for some set of your data, maybe it’s an Arabic text, and you have the same problem in UMAP where you’re kind of looking at this cluster of data and say: Okay, well, what does it represent? Well, I have to look through all the samples. And by the way, let go look at what it you know. Come up with something we’ve done in our what we do with our software quite quite a bit is actually used GPT-4 to summarize cluster data. So I think I think it’s a similar problem, which is you’re kind of like looking at what is common across these and trying to come up with a summary of it. But yeah, it’s a great question. It’s like a summarization problem. In UMAP it’s a cluster, in this case, it’s a dictionary activation on a set of examples.

### On Architectural Approaches

**Question from the audience: **So why not use architectural approaches?

**Jason Lopatecki:** So this was a question in the original paper, which is–and I don’t love this myself–but why not force an architectural approach to a model that makes it understandable instead of trying to understand what we built in terms of large language models and transformers. I think they came to the pretty clear conclusion at the end of this, that it’s just not going to work. You lose a lot by forcing a neuron to mean something. And I think they found that like that it kills a lot on performance. And I think you’re giving up an incredible amount of how these models learn if you try to force it in this direction. So that was my take on my my intuition going in, and probably why they came the conclusion they came to at the end of this.

So then they came to kind of using sparse auto encoders to find good decompositions. And this definitely works. It looks like it works great. To those of you who are researchers–UMAP itself does mapping, and we use it all the time, and one of the questions I have when looking at this is like, why not use a sparse auto encoder to UMAP directly? And one is the you know. I do think there’s some good scaling properties that maybe the auto encoder might have, but I think it’s research that I’m interested in someone doing or seeing, I’m sure there’ll be a paper and we’ll cover it. But they kind of tackle similar issues, which is finding structure and surfaces and mapping those into distinct groups of things. In one case, you get this clear dictionary activation. And in UMAP you get 2D and 3D kind of space where you still have to cluster.

There’s also versions where you can take this feature and look at like a piece of text and kind of look at like different components to the text. And what top features activate for certain words within these. So like computer here, you see the top activation in this case is the auto interpreter. One name is like the neuron fires and proper nouns for technology and mobile apps. So there’s a couple of different ways of looking at these that they’ve put visualizations on, which are pretty awesome. You know, abilities to look at like the piece of text in which features are firing, where and ordering of those.

Only other thing I look at is, if you look at the activations, it’s pretty clear if they know the dictionaries here are decently sparse at the top here. You know that there’s a couple features that are active and in the sets for each one of these. So awesome work in, in kind of looking and interpreting what these dictionary features mean and visualizing them. There’s a set of investigations they do into like these, these activations, and like what these features are and like, and then really ensuring that they probabilistically mean the thing that they’re kind of indicating they do mean.

One thing I thought was interesting too is this section where you have this poly semanticity, where, if it was truly polysemantic. And you had lots of things overlapping and meaning different things–it’s kind of hard to interpret, but there are meaningful ways in which you can look at these activations as a whole.

And then I thought, yeah, this section was pretty good, just kind of proving out like does this feature really mean Arabic’s script feature? I think they came up with a way of detecting Arabic script through a text based approach, and then compared it to the probability of it really being Arabic script versus this feature actually detecting it as Arabic script. Just to go prove that it’s actually detecting the thing you think it is.

These aren’t perfect encoders of the ideas which we all think we have in our heads, but they’re good, you know. Their goods overlaps with them, and you know they might be slightly different than the ones. There are some points in this section around like, is it really learning something, the data, or is it actually using these features to do the prediction which was the transform was trained for so is it causal, or is it causing something downstream to actually happen?

**Harrison Chu:**  Wait, Jason, do you want to linger on the one just above that? I think that’s the most powerful one right before that. Yeah, they took the neuron that fires on the highest correlation with that Arabic feature. And you see like it’s dominantly blue, which shows the neuron typically fires with even more intensity, with magnitudes of more frequency, on things that are not Arabic than the things that are Arabic. You might not even see it on the screen, that tiny red section. And so again, you take it, you’re all that fires with highest correlation with the feature, and you show that it actually just fires more intensely for everyone else. Just a great, great demonstration about the poly semanticity of neurons.

**Jason Lopatecki:** I think this is one of the more interesting questions.  From what I’ve what I’ve read and seen so far, and kind of what I’ve kind of experienced in in kind of looking at a lot UMAPs of transformer outputs, of transformer internals–I think there’s something to be said for this, like, I think there’s a whole field around this. And it’s a really interesting question, does the relationship between objects and ideas form similar topological structures in totally differently trained models, is there something naturally inherent in a model or an idea that represents structure. And that same structure is learned and can be pulled out. You know different transformers or LLMs trained on maybe even different data sets would learn the same ideas of the same– call it basis functions and topological structures. So expect a lot of research in this area. 

### Questions and Areas for Further Research

**Harrison Chu:** Jason, question for you, when I first saw this paper, I think one of the main authors tweeted it out, and the claim was well, now, the mechanistic interpretability of these models in general is now like a computation problem: now we just have to figure out how to train these sparse autoencoders to the actual size of these transforms that we’re using today. 

To what extent do you think that’s a true statement, or or do you think they’re overplaying their hand a little bit? And on this paper, I’m just wondering if you have any rough thoughts on that?

**Jason Lopatecki: **This is a well done, well researched paper, and it still fills early in the interpretability space. You know, again, like, I do think the ideas of okay, this is Arabic, and this is not Arabic, you know, like those types of dimensions are fascinating, but think of like code generation for an LLM, and it messes up something. What you’d like to get to is something from an interpretability perspective that would help you understand? Like, what should I do? Where’s it breaking down? And so you might be able to detect an activation. But how does that represent like a missed bracket, or like something on that like, how do the different generations of an LLM connect to each other. In trying to understand the many levels here to understand this well enough to go, make a fix, or change, or or do something where we still feel kind of far from that.

**Question from the audience:** How many vectors are required to either capture all of human knowledge, or at least the domain that is of interest to your problem?

**Harrison Chu:** Beautiful question. 

**Jason Lopatecki: **Yeah, that’s a big one. I don’t know if I can take a stab at that. 

**Harrison Chu: **I forgot who I was joking with. But it was like, Okay, maybe they tried the auto encoder at two, the only thing you get is like good and evil, or something from this thing. But my intuition is not much, actually. Because if you think about 512, I think maybe humans overestimate how rich our language and our lives are. But within these 512 features they found features that detect, like the numerical digits in basic encoding like. Surely that’s not out of the sum total of things that are important to humans like that doesn’t seem like that important to be there. So my sense is it’s not much. 

**Question from the audience: **What do we think the next area of research or areas that I like to see? 

**Jason Loptecki: **There’s a common thing I’ve been seeing. And across there’s a set of papers that I think would be fascinating is like the idea we were talking about earlier, which is: is there universality to the topological structures that these models learn? And this would be for like ideas around negative subjects, or harmful subjects, or toxicity, or whatever– Basically, these dictionaries are pulling out these subjects but it could just also be structural stuff. 

So I think the universality one is a really interesting one. And can you just look at the topologies that come out based upon. You know the data you put in and understand exactly what this object is. Oh, this is a car based upon the structures. Or this is a wheel, because it’s related to a car. It’s related to black. So I think there’s a whole thing around universality that I think, is a fascinating area of like, you know, do models learn the same structures totally independent on different data? So that’s kind of one area that’s fascinating. And then what does that mean? Well, I think it comes down to like if you want to control outputs or or control things in different ways, you can easily, you know, be easy to do. I think there’s a wealth of like, how do you use this to go fix or improve stuff. I think that’s still like a massively open question, like when you know, there’s just so many simple mistakes that LLMs make, you know. Is there any way of using these fields to improve or fix or understand those problems better? So those are at two directions i’d like to see.

**Harrison Chu:** And if there’s anything I know about engineers, I feel like the more plausible way is they’ll find that: Oh, if you stimulate this particular feature, you can coerce the text to be Arabic or HTML, so like the code doesn’t come out right, you’ll just increase the value of that feature activation. It’d be more likely HTML, that’s the next best thing you got.

**Jason Lopatecki: **Yeah, I mean, I think there’s been work on steering vectors that has come out in different areas. So I think there’s ways in which you can use these activations to steer models, maybe do it in a way that doesn’t fill up the context window or something. But there’s probably a lot of ways to leverage this that’s gonna be very interesting in the future.

So an audience member said that there’s a whole area of research is going on around proving unsafe generations and stuff also, it’s in the training, fine tuning aspect too.

Awesome work by this group here. Someone on Twitter recreated this on Llama recently. If someone has that drop it in the chat or share it around. It was pretty awesome work to recreate this work on some open models.

Well, thank you everyone for joining, we appreciate your time.

**Harrison Chu:** Bye!
