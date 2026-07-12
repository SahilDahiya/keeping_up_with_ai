---
title: 'LLM Interpretability and Sparse Autoencoders: Research from OpenAI and Anthropic'
topic: models
subtopic: reasoning
secondary_topics: []
summary: Explains sparse autoencoders and interpretability research from OpenAI and
  Anthropic as tools for understanding model internals.
source: arize
url: https://arize.com/blog/llm-interpretability-and-sparse-autoencoders-openai-anthropic/
author: Sarah Welsh
published: '2024-06-14'
fetched: '2026-07-11T04:48:57Z'
classifier: codex
taxonomy_rev: 1
words: 8612
content_sha256: 19696f20255797763d57d8d99e3c2b51d78353e6573f635b5a827eb026c7b199
---

# LLM Interpretability and Sparse Autoencoders: Research from OpenAI and Anthropic

![Dat Ngo, Vibhu Sapra and Sai Kolsani headshots Dat Ngo, Vibhu Sapra and Sai Kolsani headshots](https://arize.com/wp-content/uploads/2024/06/CPR-First-Glimpses-Blog-1021x560.jpg)

              # LLM Interpretability and Sparse Autoencoders: Research from OpenAI and Anthropic

## Introduction

It’s been an exciting couple weeks for GenAI! Join us as we discuss the latest research from OpenAI and Anthropic. We’re excited to chat about this significant step forward in understanding how LLMs work and the implications it has for deeper understanding of the neural activity of language models. We take a closer look at some recent research from both OpenAI and Anthropic. These two recent papers both focus on the sparse autoencoder–an unsupervised approach for extracting interpretable features from an LLM. In “Extracting Concepts from GPT-4,” OpenAI researchers propose using k-sparse autoencoders to directly control sparsity, simplifying tuning and improving the reconstruction-sparsity frontier. In “Scaling Monosemanticity: Extracting Interpretable Features from Claude 3 Sonnet,” researchers at Anthropic show that scaling laws can be used to guide the training of sparse autoencoders, among other findings.

## Watch

## Listen

## Dive in

- [Read OpenAI’s Paper: Extracting Concepts from GPT-4](https://openai.com/index/extracting-concepts-from-gpt-4/)
- [Read Anthropic’s Paper: Scaling Monosemanticity](https://transformer-circuits.pub/2024/scaling-monosemanticity/)
- [See more paper readings](https://arize.com/ai-research-papers/)

## Analysis

### Introduction to the Research and LLM Interpretability

**Dat Ngo:** Alright. Let me share my screen really quickly.

So welcome everyone to our weekly paper reading this week we’re gonna be talking about really the first glimpses of LLM interpretability. So we might just start some as folks start to come into the room. We’ll do some introductions. So my name is Dat. I’m a Solutions Architect here at Arize. I build very closely with a lot of our customers specifically in the LLM space.

But I brought with me some two very special guests, so I’ll let them introduce themselves. We’ll start off with Vibhu.

**Vibhu Sapra:** Hey, everyone! I’m Vibhu. I’ve been here before. We hopped on a different paper reading. I used to be in AI research, now I do more AI engineering, but been in the field for quite a while, you might have seen me hosting different events, running our own paper club or whatnot, but it’s always fun to hang out and chat with the Arize team.

So different topic, none of us are super specialists and interpretability, but it seemed like a fun paper. Good place to get people interested. So that’s why we’re here.

**Sai Kolasani:** And then, yeah, I guess I’ll go next. Hey, everyone, my name’s Sai. I also work at Arize. I focus more on the backend side of things. I also do research at Berkeley in the Sky Computing Lab. So this is one of my first paper readings per se, so I’m kind of excited to get going.

**Dat Ngo:** Awesome, thank you for those intros. So as you could see, we have old faces and new, and so you know, as folks for hopping in. Maybe we’ll just cover a little bit of the agenda today.

But before we do that, what I wanna do is just plug an event that we’re hosting at the Ferry Building for those of folks in San Francisco. [This is our annual Arize:Observe event.](https://arize.com/observe-2024/) So there’s going to be a lot of amazing guests here from OpenAI, Mistral, Microsoft, and beyond,

But the idea is like we wanted to get practitioners, whether from the research side, whether actual builders or kind of different tracks to come in and really talk about what they’re experiencing in terms of what’s new on the research side? How are things being built on the enterprise side in terms of LLM applications and so forth. So it’ll be on July 11th hosted at Shack 15 in the Ferry Building.

And there’s also a QR code. So if you scan this QR code, you’ll actually get 80% off the standard price ticket. And so the tickets tend to be kind of expensive. So we wanna make sure that everyone gets a chance to kind of attend

Vibhu will also be a speaker here. So if you want to see more of him, kind of talk or yap feel free to attend.

But in terms of the agenda today, we’re really gonna go through it, you know, for those who haven’t read the paper. It’s actually quite the papers the Anthropic and the OpenAI paper. They’re quite long and pretty deep, so we thought as we kind of break it down and give our kind of opinions on it. But we’ll walk through a little bit of the background, and maybe why this particular subject or topic is important.

Then we’ll actually walk through maybe the paper from Anthropic and Open AI and walk through, and then add some closing thoughts. But that should be the agenda for today.

So I think the first topic is, maybe, why is this important? Why is LLM interpreting important? So I’ve got opinions on this. But maybe we ask our guests, you know. I don’t know. Vibhu, Sai, any what’s your take on maybe why is this important? Or maybe why, it’s not important.

What’s your take?

### Why is LLM Interpreting Important?

**Vibhu Sapra:** That’s a good question. Why is it *not* important? I think it’s important. You wanna learn what’s going on in models, I think to start off, we should actually define what mech interpretability is, what they’re doing here, what are they kind of trying to do? So essentially, they’re trying to map features to understand what’s going on in a model. So Anthropic put out a pretty interesting short three minute video of what mechanistic interpretability is. Essentially as researchers, you kind of define what are the layers of the model you have like this scaffolding so like, what are the different hidden dimensions, what’s the layers? Is it a mixture of experts? And then from there you go and you train it on trillions of tokens and the model starts to fill in this knowledge. But we don’t really understand what’s happening on the inside of a network. So you have a good high level overview of like, here’s the architecture, here’s all the dimensions. Here’s how many parameters there are.

But as the model starts to learn, we don’t really understand what’s going on inside the network? So part of it is, why is it important to know that?

I think Anthropic has their take of: you know they’re all safe. AI, so alignment, safety, all this all that. I think there’s also practical examples like there’s the meme aspect. If we’ve seen Golden Gate Claude. Why don’t we have a Golden Gate Llama yet? You know, we gotta build some of those. But outside it is just safety as well. Sometimes it’s like, you know, there’s just

exploration of ideas like, is this an alternative to rag? Is this an alternative to fine tuning? Could you clamp different feature vectors to dear models in different ways. So it’s always just a great idea to understand what’s going on. So we know what we’re doing. Fine. What are your thoughts?

**Sai Kolasani:** Yeah, kind of building off of that, I guess from a research perspective. First thing that came to mind is if we can identify the key features and actually understand what’s going on behind the scenes. Then maybe we don’t have to go down that route of trying to just ingest so many parameters to new LLMs, we can actually focus on just the ones that are important. So this could actually make LLMs more scalable. And even an industry like maybe more companies can actually use them. Now start sort of like, build their own LLMs, so because that’s like one thing I was thinking about. But then another thing is kind of around the whole idea of like AI human alignment. There’s like a lot of research going into, can we get LLMs to kind of have a state of mind?

Can we kind of make them identify the emotion that the user is feeling at the time?

So I feel like, if we can kind of use this sort of interpretability research to identify the features that actually allow the other ones to maybe have these capabilities. It could make a lot of progress there, too.

**Dat Ngo:** Yup totally agree. I think it has applications from AI alignment, safety, fairness, and bias. All that stuff. But I really agree with Vibhu’s take, I don’t think from a pure mechanic standpoint, I think the more we understand, the more we can get better models out of this and really kind of understand, you know, know what we don’t know kind of thing.

I think the first thing maybe we do a little timeline about the papers, and so the link should be shared kind of in chat, but I think it really started off with this paper I don’t know what your take is, but it came out kind of last year in October, but it was really doing this decomposition with sparse autoencoders, but they only did this on small, like low scale models, right? Not very large models, and then it was on only until recently, right like maybe last month in May, where they released one of the papers that we’ll be reviewing, and I think very quickly. This read is super in depth. You can tell. Anthropic put a lot of work in, and then OpenAI quickly followed up with their own version of this, maybe a different flavor, which we’ll go into a second kind of how to recreate the experiment.

So that’s the timeline. I’m kind of what we’re in. So now it’s June 12th or maybe 6 days after this has released. And so maybe one thing I wanted to talk a little bit about. So it’s a very dense read, but I kinda wanna talk a little bit about some just folk apps just for maybe the folks who haven’t read the paper.

But when we talk about things like monos, semantic features, the the reality of what that means is really like, can we have, like a single clear understanding of a particular feature. Right? Does this one thing mean this one concept? It’s really mapping understanding to a human level, whereas things that are maybe poly semantic might have multiple meanings or you could think a second order kind of relationship where it’s much more complex. And so the monosemantic importance here is like, hey, can we map this one concept or thing to one specific set of? And we’ll go into later. How this feature is fired.

**Vibhu Sapra:** Before we go into specifically the vocabs of this, do you wanna just give like a one min high level of what these papers are trying to do. So Mech Interp is trying to understand a model. One approach that Open AI and anthropic have taken is using these sparse autoencoders to map feature vectors towards activations in a network. So I don’t know if you wanna take this or I can just yap on, you know, but I’ll let you. It might be useful to just get a high level of what’s going on.

So essentially, we’re trying to train another network to solve the problem of, do we understand what happens in a neural network so as tokens are being generated, can we understand, are there actual, interpretable meanings in our network towards what makes specific tokens activate?

So the high level before, like going through all this presentation is, yes, we find that we can map specific concepts to different parts of networks. The approach that they take to do this is, they train sparse autoencoders to kind of have these feature vectors, and then these are some of the terms that they use to kind of do this. So sorry to cut you off, but high level they’re training and autoencoder to map features to understanding, and these are the weird terms I use for.

**Dat Ngo:** Totally totally makes sense. I was actually looking for one of the slides. But yeah, Vibhu if you wanna go through or sigh. If you wanna go through, maybe the other two definitions that’ll be great. And then we can kind of move on.

**Sai Kolasani:** Yeah, I mean, I guess next thing we can talk about as far as autoencoders. I feel like that’s where the bulk of the work in both of the papers is essentially, it’s just kind of a way to kind of project features from one input space into a much larger one, creating sparse features. Then essentially, it’s used to train like few features at a time, and it identifies the most important parts like to kind of dumb it down into my basic terms.

And they allow, like the decomposition of the model activations under the hood, in these models, into like specific components which we then would say are interpretable.

**Dat Ngo:** Awesome.

I think I have a slide on the experiment here. Let me actually pull it up. But maybe while we’re talking about yeah, go for it.

**Vibhu Sapra:** I’ll just talk over while you’re going over that. So while you find your slides, some of the you’re free to swap slides, by the way, some of the background of this. So in that first October paper, what Anthropic tried to do is they tried to train a new network from scratch very small model to just go from. Here’s inputs here’s a single layer transformer, here’s the outputs. Can we map this middle layer and try to see what inputs have, what activations, to what outputs.

Now, what they did here at a high level is they tried to poke in and see for an actual production scale bottle. Can we do this with thoughts on it? So a lot of the background questions of, why do we care about mechanistic interpretability? Is we want be able to understand stuff at a big scale, a lot of LLM research. AI research into these models. A lot of the problems is that small scale. Experiments don’t always scale up. So that’s been a kind of common critique of sparse autoencoders, this whole thing. They did it on a very small toy model, little bit of data, nothing that would be used in production.

And what this paper really showed is, hey, this technique that we tried actually scales up significantly. We could do it on a production grade model. OpenAI showed the same. They can poke in a GPT-4. But traditionally at a high level. Some other stuff like solid state models, the whole state space models.

They’re all very small models. We haven’t scaled that up until recently. So that’s a big concern.

A high level reason for why this is important as well is, it’s pretty directly impactful. It gives us a cool problem to work for, it seems useful. And it gets a lot of like young researchers interested into the field of AI research. But what they tried to do here is, yeah. I guess we’ve got the side for their high level experiment. You wanna take it over.

**Dat Ngo:** Yeah, I’ll maybe summarize the experiment here, because the really cool part is not really. It’s what kind of happens after the experiment and what they found out. But yeah, as Vbu said, sparse autoencoders for those who aren’t familiar with just autoencoders in general, they’re generally built up with encoding, the first part, which is an encoding network, and then the second part, which is a decoding network.

What they use the encoding network for is to map to a higher dimensional space. So imagine you take this thing that’s very dense and complex, and you just map it out to a bigger space and the bigger space allows us to really understand, hey, what are the specific features or concepts semantically that we’re kind of looking for. So they used a varied set of sparse autoencoders here of different sizes. So 1, 4, and 34 million.

You have to train these very or sorry. I keep trying to say ves, but sparse autoencoders.

And what you’re really looking for is like you. You train them in a sense that you’re trying to really understand. Like, what’s the best computational resources for them. But the goal is you. You’re kind of playing around with them to see. Hey? What are the best ways that I can find these mono semantic features. So there were some scaling laws they were. They were really trying to understand while training the SAEs.

And then they really focused on the middle layer inside of Claude. And the reason for that was that it just struck a really good balance in terms of semantic…there’s just a lot of complex complexity in terms of semantics. There’s like very low, level things, very high, level things and complex things. And they found, like the middle layer, a good place to start.

Again, I think there’s a lot of research happening here, but anything else that you know you do want to add, in terms of the experiment details, any other interesting things?

**Vibhu Sapra:** Yeah, the few key points is there’s traditional autoencoders where you’ve got an encoder decoder. They’re traditionally used. The previous challenge that makes this work unique is scaling them up is difficult training. An autoencoder is pretty hard making it sparse means to make it so that when you have this middle layer, not all features activate. Only as like the specific features that are representative of input to output activate. So they were able to achieve that, I think, for every token, for any given token, no more than 300 features activate.

So, a lot of the real research here is: 1.) They could scale it up. 2.) They could actually make it sparse. So not a lead lot, a lot of features activate per token 3.) They were able to actually correlate topics to features, and, like that, stayed active across different domains.

The other aspect is yeah where they probed. I think Openai did it towards one of the last layers, but somewhere, like towards the bottom half. So the key part there is just that there’s still a lot of research opportunity, there’s a lot of unanswered questions. There’s a lot to go off on, but that’s the core research that they did. They scaled it, they kept it sparse, it works, they could identify features.

**Dat Ngo:** Yeah, exactly. Anything else Sai on your end?

**Sai Kolasani:** I guess a little bit about like the activation functions themselves that used these papers used a top K sort of function. So they kind of select like the top most interpretive features.

And then that’s kind of what they pass it back into like the decoding network. So it’d be kind of interesting, maybe, in like future directions, if we could figure out some other sorts of like activation functions and see what we could do with that.

### Scaling Laws and Sparse Autoencoders

**Dat Ngo:** Yeah. And then, for, like, maybe the layman on the call, the way I describe it is the reason why they use sparse autoencoders. It’s really trained to use only a few features at a time, right? Really making it focus on really the most important parts. Which makes things like more clear to understand for like human interpretability, when we think about the model sizes that just like was a variance across the experimentation.

And so what do we learn from the scaling laws? So more compute leads to better results. And so you know the best number of features and training steps both increase as you use more compute, which makes sense. And then optimal learning rates actually decrease as compute increases, suggesting that, like more efficient learning with maybe larger budgets.

So just wanted to highlight that for folks on the call. And then maybe we get into the fun section. I just put this gif in here because I think this is OpenAI’s way of like describing to the layman how this works, but I really don’t think this is very representative at all, but it’s just kind of a cool Gif.

But maybe we go into experiment results. And so for folks on the call. You can actually go in and look at the experiments done by Anthropic. So they have this kind of feature browser. Where, if you look for you can think I think they’re calling these kind of paper features.

Where are the activations actively happening in the text? So, for instance, Golden Gate was, you know, one of the things that are featured here. But if you ever want to play around with this it’s linked in the slide deck which we will share out. So if you wanted to see kind of their curated example of activations and “paper features” you can kind of play with that.

And so maybe we go into assessing the other parts of the paper. Again. This paper was extremely dense. If we look at the contents, I think it’s 70 pages long. What we tried to do for this is really just break down the components of this paper into digestible pieces for this particular paper reading.

And so I think the first thing that we want to maybe talk about is assessing feature interpretability like, what does that even mean?

And so maybe we scaled it down to? Maybe these four points we’ve gotta get through the rest. But I think it comes to specificity things like sophisticated features, like, there’s simple versus extremely complex when you think about language.

Assessing the difference between features and neurons and influences on behavior. So we’ll we’ll quickly go into this. But I don’t know, Vibhu, Sai, if you wanted to take one of these, or we’re particularly interested. If not, I can keep going.

### Breaking Down OpenAI’s Paper: Extracting Concepts from GPT-4

**Sai Kolasani**: Alright! I’ll start off here. I guess. One of the things that I found really interesting was the influences on behavior. How they kind of just like decided to kind of set higher values to certain features and like lower ones to others, to kind of see how the model interacts with that. And I think that’s a pretty interesting avenue. Like most recently, like even them, like

trends and stuff like that. I see, like a lot of people trying to kind of figure out like what parts of the model makes it good at like coding, or things like arithmetic. So it’d be kind of cool to like. See if we can get some open source on like that avenue and trying to figure out like which

features, and, like some of these video models, actually correlate to that.

**Vibhu Sapra:** I found that section pretty interesting as well. So some of the stuff that they showed here something that we haven’t gone over on a high level is after you extract these features, they have this topic of feature clamping where they kind of go back in the model activations they really aggressively tune up or tune down this feature. So, some main features that they found, for example, or stuff like, let’s say you take the feature of country or a specific country like Kenya.

Now that feature gets activated, when you talk, not only about the token, but also different, like you know the word country, the word like anything about the place. The feature is represented there. So they showed some safety examples of this, so like with racial terms with some typical terms like the term nurse. The feature for the term nurse also very actively fires up with woman or something. So they show how you can kind of mess with this. And this is like a safety issue right where, if you clamp up the word nurse. You start getting responses that talk about women.

And there’s like fundamental bias in the model.

Same thing goes with racial problems or like. there’s a feature that talks about malicious code. If you clamp this into the model when you’re using sonnet and you increase the feature for, like malicious code. Now, Claude will start actually outputting malicious code. So I think that the influence on behavior is pretty large there,there is a safety aspect to this, too. But it’s also just interesting high level information that we should know, that’s like the second motivation for this work.

Not only can we understand what’s going on in the model. We can also influence the behavior of outputs based on these features, where all the math and implementation aside, which is actually pretty straightforward if you look into it, you can take a feature, and you can scale it up or scale it down.

So that was my favorite section. The majority of this paper is just more and more examples of that. I think Anthropic did a great job with all the visualization showing this, they also showed, if you scale something up or down what that looks like, but Dat I’ll pass it back to you.

**Dat Ngo:** Yeah, this is, that’s a really good points on this, and clamping as well some other points, too. I think. I really like the features versus neurons. It just kinda makes sense. Why, using sparse autoencoder coders was used here. Because I think, when you just look at neurons. It’s very hard to get something human interpretable. I think you need something complex to digest, something complex to give you something simple. And so yeah, when they think about features versus neurons, it made a lot of sense for me. It’s like we can find something much more interpretable, using sparse autoencoders.

And then this sophisticated features. It was really cool to see that you could end up with more features than the number of neurons, total, which would describe like, not only do neurons represent maybe low level concepts, but higher order thinking as well, which makes sense, right? You can combine ideas to get, I don’t want to call it feature engineering, because it’s too close to classic ML, but yeah, you can combine things to make it more complex, like second order, third order, classes of complexity in terms of modeling language.

So I thought that was pretty cool. You know, kind of goes along with how complex this all is, and to be very honest, like the reading was like more of like a discovery of like. Oh, these are the things we tried out and found out. But the reality is, I think there’s so much more to kind of explore here.

And his specificity was really the kind of the paper saying like, hey, here’s there’s also challenges kind of here. And some of the challenges was that, like activation to a specific concept is really tough, especially for maybe very abstract features. So I thought that was pretty interesting. But any other highlights here from our guests before we move on to the next section.

![Experiment details: use of sparse auto encoders](https://arize.com/wp-content/uploads/2024/06/Slide-7--1024x572.png)


**Vibhu Sapra:** Yeah, I think at a high level. So what they did is they trained multiple, sparse autoencoders with different dimensions. Right? Something to note is as they scaled up, there was a pretty drastic drop in feature activation, so like the smallest sparse autoencoder had a million features that can kind of be as like hidden dimension. There’s a million features for that 1, 2% of them just never activated. As they scaled up to the one with 4 million, 35% of them never activate. And then for the biggest 1, 65% of features, just kind of never, never activate. That shows how it’s still hard to train these things.

And you know, the second aspect is as you scale up, and you have more and more features. There’s no great automated way to map these features to real world examples. So a lot of the work they had to do was really, yeah, we did this discovery. We found that we use the bigger Claude Opus model to try to interpret some of this. But they didn’t have a clear cut formula. So there’s still a lot of discovery in these features to be made.

And now that you can also have new features, you can have more features than there are like neurons or parameters. You open up more and more complexities. So all that just kind of shows that this is still pretty early research, and it’s hard to actually map all these features.

**Dat Ngo:** Yeah. And it wasn’t like the study was exhaustive either, like it almost never can be. So it was like, and we’ll go through this in the rest of the paper, but just knowing I think they probably did a lot more work than what they published, to be very honest. I bet there were a bunch of areas where they thought it might be fruitful, but I guarantee you probably wasn’t so again, I think we’re just seeing maybe a little bit of selection of what was chosen for us, but again agree with that wholeheartedly.

**Vibhu Sapra:** To not discredit their study, though they do show these adversarial examples. So for most features, they show how the top activations are what makes sense. For this given feature, it activates where we expect it to. But on the adversarial I think they showed an example of Kobe Bryant, and what you would expect to pop up is like Los Angeles Lakers, basketball, and stuff. However, some of those things that you would expect to be like the most active features actually are like, you know, bottom half of what should activate, they’re not the top 20. So they do explain. And they do bring up these limitations. It’s a really great introduction on what to expect if someone’s an early researcher, what they should think about it brings up so many questions that you should be asking.

And then the OpenAI example of this. The OpenAI paper is a little bit more like, here’s the formulas. Here’s the scaling laws. Here’s what we derive. Anthropic was more…we followed general scaling laws. We see that they hold true. But we do see some stuff like, yeah, sparsity is hard to measure, and we do have some feature drop off. The OpenAI paper was more so. Here’s better formulas to follow. Here’s how we keep it so that all features activate, they have the more so implementation paper in my experience. So for people that are following along, the OpenAI, one is more so. Here’s the steps to redo this. Here’s how you would do it right. Here’s our learnings on that. The Anthropic one is. Here’s all our discovery. Here’s like 50 pages of all this cool stuff.

That’s how I separate them.

### Breaking Down Anthropic’s Paper: Scaling Monosemanticity

**Dat Ngo:** Awesome. I think we’ll go into the second part of the paper. Let me just scroll up here. Table of contents is a really good place to just grock the ideas, if you just read without looking at the table of contents, it’s really hard to keep track of where you are. And so next, maybe we’ll talk about as we just did, assessing feature, interpretability. The feature survey was pretty cool, too.

And so I’m just actually gonna just pull this up into this part.

And so really, this was just like, Hey, they wanted to see what the neighborhood of features kind of looked like. So maybe I’ll go straight to the visuals here. Oh, that did not link me to the right spot.

Let’s go up here. Specificity

Should be down here.

The feature neighborhood stuff was down here.

Feature versus neurons.

Oh, feature study. So yeah, they’re basically saying, Hey, what’s in Sonnet? What are all the features? And maybe how do they relate to each other?

And so I think we can look at some of these. And these are amazing visualizations, too. I think, I’m not sure if these are views of the embedding space as well.

But these are really the nearest neighbors to the Golden Gate Bridge feature, and you can see things like if I’m looking at this particular feature as Vibhu said earlier, what are the things that kind of maybe pop up?

![Nearest neighbors to the Golden Gate bridge feature detail](https://arize.com/wp-content/uploads/2024/06/Slide-8-1024x732.png)

And so here’s the San Francisco region, the earthquake region. And this is a zoom in on, on that particular region.

And then they also find evidence of feature splitting, which is where a feature can be split into multiple, larger features inside the SAE, which are geometrically close and semantically related to the original feature.

**Vibhu Sapra:** Hey, Dat, quick thing! So before we go deep into what these features and feature bubbles are, we’ve got a question about what do they precisely mean by feature? You wanna take that.

**Dat Ngo:** Yeah, that’s a good question. I think in terms of what feature means. In this case I think it’s the Golden Gate bridge feature. So I think we can go back to this definition here of maybe a single concept or subject semantically again, feature is ambiguous here, but if the term is like mono mono semantic features like, what does this idea represent in language? That’s the way I would describe it. But Vibhu, Sai, any other way you describe it?

**Sai Kolasani:** That’s basically how to explain it to. It’s just kind of like a semantic term that you can pull out.

**Dat Ngo:** Again. The thing with this paper is. There’s like no fine line in the sand, right? There’s no official like this is a feature, not a feature, because features can be combined upward to more complex, sophisticated features like we were talking about earlier down to more simple less intricate meanings. But that’s kind of what we mean by feature until.

**Vibhu Sapra:** Yeah, I think the visualizations are pretty strong for features. So like if you go to the paper and you scroll through any of the specific. So you want to scroll up a little bit?

Anywhere where they’ve kind of got the clickable feature. I think it’s like the first 3rd of the paper.

**Dat Ngo:** Golden Gate might make the most sense.

I think in terms of feature, like. So in this case, it’s the feature distributions for Golden Gate Bridge. I think the way you can read these plots is like in the text that you can think we’re analyzing. The highlights are really like for theSAE that was used. What activations do we see in the text?

And more specifically so when we see things like GG bridge, right? It’s always activated with this text. So like Golden Gate Bridge activated the GG Bridge activate Golden Gate Bridge at the..

I think this distribution plot I’m not super familiar with.

**Vibhu Sapra:** I would kind of avoid the distribution plot. It’s not relevant to what it is. But you see at the top how it says feature number. So this is saying, out of the autoencoder that had 34 million parameters, this is that specific feature. So 3, 1, 6, whatever that feature pops off most strongly based on, if you see the bottom. So words like Golden Gate Bridge, Presidio! That’s where that feature is most active. So for every parameter there, like for feature number 4, let’s say, that’s about like basketball, it would be most highly active about basketball, sports, orange ball. So that’s what they mean by feature.

So it’s feature number whatever out of this autoencoder is most strongly activated about whatever tokens. And now going back to where we were in the paper, if you want to scroll back down to the section you were at, they’re grouping down. Sections of different autoencoders have different, like feature mapping bubbles. So the biggest circle here is like their smallest auto encoder. It has a rough idea of San Francisco.

So if we look at the bottom or at the left side of the screen, you see how there’s that San Francisco Bubble, the smallest autoencoder kind of bubbles everything just as just San Francisco features the second one, the 4 million parameter autoencoder. It’s got features about San Francisco and its surrounding areas. The biggest autoencoder has stuff like San Francisco, San Francisco airport, the location airport code, SFO, articles like the SF Gate. So

this visualization is kind of showing the density of features. We can double click into a topic so like the smallest autoencoder has a high level feature around San Francisco. The medium one has, like San Francisco areas around San Francisco. The bigger one can also double click into this, more like SFO, articles around us of stuff like that. But that’s kind of what this was showing.

**Dat Ngo:** Gotcha that just tells you even I read the paper, and I couldn’t believe but that actually makes a lot of sense right? That like a smaller SAE model would have to have larger… the concepts are grouped into larger places because it can’t get as granular if that makes sense.

**Vibhu Sapra:** They’re higher level. And then the bigger autoencoders can break core features down into smaller subsets. So San Francisco, as an example, there’s others here, too. Right? So like you’ve got San Diego, you’ve got Mac OS for all these. If you look into what they are, it’s basically saying that as you get a bigger autoencoder, you can break down features smaller and smaller. And now questions to think about is, what if we scale this up even more? What if we have a bigger one? Can we keep it sparse? Can we train it in such a sense?

What features are we specifically looking for? But this was part of their discovery.

**Dat Ngo:** Yeah, I also think there’s a balance right? Cause I think if you go too big, you start to lose like, if you used an SAE that was like as large as maybe the parameter size of the model. You would just get the model right? So I think there’s like.

**Vibhu Sapra:** Part of that is like, that’s a lot of what in mech interp the end goal is right. You wanna know what every neuron does. So in SAE, the size of the model is basically, can I train a model where I can map every parameter to a specific topic? But you know you scale that back to how much of a model can we understand means what saes are like steps here to probe into it, but specifically there with the size of the model is basically, can we just train the perfect model from A to Z?

**Dat Ngo:** Hmm. Interesting. Interesting. Lot of food for thought in this one. Yeah. It got me thinking that was a good way to explain it Vibhu, I appreciate that

Sai anything on your end before we maybe we’ve got about 10 min left? So I wanna make sure you make it to the rest.

**Sai Kolasani:** I think I think we’re good.

**Dat Ngo:** Cool. There was another section is features as computational intermediates. I think the long story short here is like I think we can go from like, Hey, here’s an input to the output text. But the idea was that understanding the intermediary steps between can really help us understand really how these things work? So I’m sure Vibhu has a take here, so I’ll let him do his take.

**Vibhu Sapra:** I have takes, but I think we should, you know, go through the rest of the paper at a high level, save the last few minutes for which for discussion. So I’m gonna let you go through the slides.

**Dat Ngo:** Perfect. Yeah, I think the tldr is that features help us understand how the models work. Right? We’re kind of seeing it right here. There’s a couple of metric methods for how we do this, and the intermediary is our attribution. So it’s like looking at the effect if we turn things off or on in a specific way. What? What does the output tend to look like?

So it’s a quick way to see which features might be important or not important.

For specific outputs, feature ablations. It’s really turning things off at a specific point to measure the impact of the overall kind of output or the tokens that we get out.

Again super high level. Here, I think the next section was searching for specific features.

Again, the challenge was like, they didn’t do an exhaustive search for all this. It’s almost impossible to do this so really for finding specific features. They use methods like using kind of single prompts to see if, like specific features would activate or not activate, related to specific concepts, prompt combinations, geometric methods, and and attributions. I probably won’t go into super depth here in terms of that. But Sai any take on this?

**Sai Kolasani:** Oh, yeah, I think from like what I got out of it, I think it just calls for like, obviously, I just kinda wanna see like if people can kind of come up with like other types of searching for these features like, obviously, it’s not very exhaustive, but I think there’s definitely like more work to be done here. And it’s just like such a new like kind of scope of investigation.

So I definitely think there could be a lot of improvements made in this aspect.

**Dat Ngo:** Gotcha, yeah,

And so yeah, I think like an example here, for, like prompt combinations, like filtering features, not active on like an image of like Taylor Swift So, for example, helped identify features specific to…So if it’s not active in like, for example, the concept of Taylor Swift. It was used to help identify features specific to Golden Gate Bridge. So it’s like just saying like, Hey, if I turn these off, does it affect some other feature concept things like that.

Geometric methods really like inspecting nearest neighbor features with the math here is like high cosigned similarity to features of like features of interest revealed that you know there was also additional significant features kind of near there. So it’s really like, hey? Are things near each other, do feature sets overlap, or things to that effect.

And then maybe attribution was you know, maybe features were selected, based off of, you know their next estimated effect on model outputs, such as the the logic difference between

possible next token completions.

Again, this was a little dense for me, so I didn’t really quite grok.

I don’t know if you did, either, Vibhu, but it was starting to get really dense, and I was like, well, let me just summarize this and get to it later. But I really didn’t discern too much meaning from this.

**Vibhu Sapra:** So part of this is OpenAI tries to go into a way of like, how do we better search for these features as part of their blog. I think a lot of that’s a little too low level on a high level.

There’s still some topics that we should bring up like in their whole sa like model probing. Something that they did notice with these features was like, they don’t only work across text. These features are also multilingual. They also work multimodal, so they fire up for not only Golden Gate Bridge in English they fire up in multi languages, they fire up for the images the visual domain of the Golden Gate Bridge.

The other aspect of all of this is outside of just how they did their model feature search like there’s finding specific features. They in the paper show a lot of examples of how they ensure a feature is about something right?

Right now it’s pretty high level to just say, like, Hey, we found features that correspond to code errors. But then they go into like, let’s actually double click into this is this feature just over fit on, like the Python programming language? So it says the same feature and see if it activates in a different programming language. Now let’s try it and see if it’s just good at auto correct, let’s try it in like English.

So they go through all these levels of not just finding specific features, but also, how do they test to make sure that these features are actually sparse and specifically represent something. The paper has a lot of great walkthroughs of this, but that was the higher level takeaway around finding features as opposed to what’s the technical way to find them. That’s the bigger takeaway, I would say.

![Safety-Relevant Features](https://arize.com/wp-content/uploads/2024/06/Slide-10-1024x573.png)

**Dat Ngo:** Gotcha just based off time, we’re gonna go through here. I think this one was pretty interesting. One was just safety. I think the Tldr; is like, we wanna make sure these models don’t don’t do any harm.

And like, you know, fairness, bias, etc. I think what they did found was like, just because there were features that were that seemed unsafe didn’t necessarily mean that they would cause issues, for example. A lot of feature study here, too, to see if we can maybe use feature sting to avoid certain subjects, or speak feature outputs as well.

So what are the things that might be dangerous? It might be like unsafe code, bias, sycophancy, deception, etc. And really the conclusion here was that this feature work provides a good foundation for future work in this area like, Hey, can we steer away from certain subjects? And I have a little meme here. What would George Hinton do as the kind of godfather?

Maybe for discussion and related work this was another section in in the very large paper, but they really discussed about things like implications to safety generalization beyond. And then they also mentioned a lot of additional side kind of research work that was happening in these kind of areas. Theory of superposition, dictionary learning, etc., especially in safety as well.

But maybe with the last three min we go to key takeaways. So for me, I kinda had a didn’t have a super prescriptive takeaway other than like this is super cool, very, you know. Really, the 1st steps into understanding. How these things that we use kind of work. And I really think there’s a lot more work that’s gonna come out here. I think, OpenAI quickly followed anthropic. But love to see something from Google.

### Conclusion

**Dat Ngo:** And I know Mr. Vibhu here himself has some takes.

**Vibhu Sapra:** Yeah, but in the two min we’ll keep them non spicy. So basically, just people need to build more versions of this. There’s so many questions unanswered. Where do you probe? In what features do you look for? How do you do more clamping on this?

Can this replace like guardrails, you know, if you plan out a feature that you don’t want talked about, so there’s so much like experiments to run. A lot of this is pretty open source accessible. You’re not training a huge model. You just need activations of whatever model you want. And then you’re training hundreds of millions or like tens of millions of parameters.

Other things, you know. Apply it to other domains. Can we apply this to stable diffusion, find feature activations, clamp them out? So like, let’s say you want the safety aspect of stable diffusion right now.

Right now you have to have, like a content moderation filter to make sure nothing’s NSFW or whatever can we clap that feature down instead? Can we optimize? There’s just so many things you can test for. What about deepfake detection? My thought experiment was like let’s say you wanna find a feature for hallucination and clamp it down to 0. How would that look like? How do we approach this? Can you, let’s say, do a bunch of activations find where models hallucinate? They don’t hallucinate. Now you’ve got some like training data. Can you fine-tune an SAE for this thought experiment I gave more than I was supposed to. I was supposed to pick your 2 brains, but not much time, but something to think about. You know, there’s just a lot of work left to probe around with, Sai off to you.

**Dat Ngo:** Yeah, before we go to Sai, I’m just gonna add one more bullet point. Yeah, I think. I kinda just had this idea off the bat, I’m sure people already doing it, but taking some open source models and running the the OpenAI library on it, just to see what exists in the open models today. So, not having to rely on these papers. That would be my not thought experiment, but just experiment. But go ahead.

**Vibhu Sapra:** Experiment wise essays don’t necessarily transfer over like, I can’t use Anthropic’s on OpenAI. They’re kind of model specific. Not that straightforward but a cool idea.

**Sai Kolasani:** To kind of sum it up in the interest of time. I was also kind of thinking along the same things like it’d be cool to like. See if people can do this for long. See what we find there, just like smaller models in general. But I kinda touch into this a little bit, but I think it’d be cool if we can kind of find a way to just prevent like dead latents. So what I mean by that is just like all the features that we don’t see activate for a specific use case, can we kind of just figure out a way to get rid of them, and then make sure that, like all the features are actively contributing to all of your tasks.

I think this would obviously lead to a more robust and capable model. And you also wouldn’t need, like, as many training parameters. So I think this could actually be like a pretty good idea, for, like a replacement, for, like fine tuning, in some sort of sense, we can kind of get this working.

**Dat Ngo:** Awesome. We’re kind of at time here, but we’ll add the resources and again, if you get a chance. We’ll also plug. Observe, wherever we post this video. But thanks for the time, also special.

**Vibhu Sapra:** Quick, quick question is the Observe ticket really 80% off? That’s huge!

**Dat Ngo:** Yes it is Vibhu.

**Vibhu Sapra:** I definitely recommend checking out this amazing conference.

**Dat Ngo:** Awesome Vibhu. He will be speaking there as well, so if you want to get more of him he’ll be there. But thanks for the time. Really big shout out to our two guests today, Sai, researcher at Berkeley, and then Mr. Vibhu himself. He is the most knowledgeable person I think I know in this space. So thank you so much to you, too.

**Vibhu Sapra:** Thanks for the Arize team for having us on, and thanks for everyone on the back end. Sarah, shout out for logistics.

**Dat Ngo:** Awesome. Thank you very much. Everyone have a good one.

**Vibhu Sapra:** [Check out Observe!](https://arize.com/observe-2024/)
