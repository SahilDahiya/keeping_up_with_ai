---
title: Explaining Grokking Through Circuit Efficiency
topic: models
subtopic: reasoning
secondary_topics: []
summary: Paper-reading deep dive on grokking and circuit efficiency as a way to understand
  model generalization.
source: arize
url: https://arize.com/blog/explaining-grokking-through-circuit-efficiency-paper-reading/
author: Sarah Welsh
published: '2023-10-06'
fetched: '2026-07-11T04:47:47Z'
classifier: codex
taxonomy_rev: 1
words: 5239
content_sha256: 3b3d44dd8034c67e1563ef0ba3841dddada2d61acfec0fff1b4395c6ef493edd
---

# Explaining Grokking Through Circuit Efficiency

![Community Paper Reading - SallyAnn and Jason blog SallyAnn and Jason Community Paper Blog cover image](https://arize.com/wp-content/uploads/2023/10/Community-Paper-Reading-SallyAnn-and-Jason-blog-1021x560.jpg)

              # Explaining Grokking Through Circuit Efficiency

## Introduction

Join Arize Co-Founder & CEO Jason Lopatecki, and ML Solutions Engineer, Sally-Ann DeLucia, as they discuss “Explaining Grokking Through Circuit Efficiency.” This paper explores novel predictions about grokking, providing significant evidence in favor of its explanation. Most strikingly, the research conducted in this paper demonstrates two novel and surprising behaviors: ungrokking, in which a network regresses from perfect to low test accuracy, and semi-grokking, in which a network shows delayed generalization to partial rather than perfect test accuracy.

## Questions for the Researchers

We had the opportunity to ask one of the paper authors–Rohin Shah–some questions that lingered after the paper reading. You can find the answers below, and our discussion follows after that.

**Sally-Ann DeLucia, ML Solutions Engineer, Arize AI:** Could you elaborate on the concept of “circuit” within the context of neural networks? How does this notion help in understanding or analyzing the network’s behavior during the training process?

**Rohin Shah, Research Scientist, DeepMind:** A core assumption in our work is that a single neural network can learn multiple different “ways” of achieving low loss in parallel. The word “circuit” is mostly meant to point out that we’re making this assumption — it’s our word to denote each of the “ways” that the neural network can achieve more loss. We use the word “circuit” to mimic the terminology from the interpretability literature (see e.g. [Circuits thread](https://distill.pub/2020/circuits/)), which I think provides the best intuition for what could count as a “way” to achieve low loss.

**Sally-Ann DeLucia: **The paper utilizes softmax cross-entropy loss. Were there other loss functions considered, and if so, how did they compare in preliminary testing? Would the findings significantly change with a different loss function?

**Rohin Shah: **I think most if not all of our experiments were done with the softmax cross-entropy loss, but I expect that the results would be similar for other reasonable loss functions like mean squared error, since all of our theory is fairly agnostic to the type of loss function. For example, in Appendix D we theoretically analyze the example from Section 3, and our analysis (primarily Theorem D.4) applies to a broad class of loss functions that includes mean squared error.

**Sally-Ann DeLucia: **The dataset sizes were specified to be slightly above the estimated Dcrit. How was Dcrit estimated initially, and how might different dataset sizes or types of data affect the observed phenomena of semi-grokking and full grokking?

**Rohin Shah: **We estimated D_crit from Figure 3a and 3c — you can see that C_gen usually has parameter norms in the 27-33 range, and C_mem gets that parameter norm at dataset sizes of 500-1,000, suggesting that D_crit is approximately in that range.

**Sally-Ann DeLucia: **The paper leaves the investigation of certain phenomena observed during semi-grokking to future work. Could you share any insights or hypotheses you might have regarding these phenomena, and what steps do you plan to take next to further explore these observations?

**Rohin Shah: **The first thing we mentioned was test accuracy spikes during training before full convergence — I think this was likely a bug we recently found in our code for producing graphs, and isn’t a real phenomenon. The second thing was training loss fluctuation — here I don’t have any specific hypotheses. That being said, it will probably be related to the fact that C_gen and C_mem have similar efficiencies — you could imagine that, combined with noise in the training process, this leads gradient descent to switch between the two. We’re not planning to work on this any more, but I’d love to read any work that other people do to understand what’s going on here!

## Watch

Dive in:

## Transcript

**Jason Lopatecki, CEO, Arize AI:** We’ll give it a couple of minutes for people to come in, and we’re talking about grokking. Do you know where the term grokk comes from?

**SallyAnn DeLucia, ML Solutions Engineer, Arize AI: **I actually don’t, do you?

**Jason Lopatecki:** I do. It’s a science fiction novel called* Stranger in a Strange Land*. I think it was like an alien term from the book where he’s trying to understand the world. So that’s a random fact. As a kid I read a lot of science fiction. So it generally means trying to understand something. Had you read any other papers on grokking prior? Or was this kind of the first?

**SallyAnn DeLucia: **This was my first, and I’m kind of glad it was my first, because I think it really breaks down the whole process of how you know grokking comes to be and especially in this context for neural nets. But yeah, this was my first real paper on it.

**Jason Lopatecki: **Cool, awesome. We’ll give it another minute here for people coming in. I think this whole concept of generalization, which is understanding how to do something when you haven’t seen examples. You see it all over right now, and and and trying to understand how networks or LLMs or neural networks generalize. I think it’s a fascinating topic.

How would you describe generalization yourself?

**SallyAnn DeLucia:** Whenever I think of generalization, I basically think of it as like the model’s ability to properly predict something new. Something like you said that hasn’t been seen. So creating patterns from all the information that it has seen, and then applying that new data point comes in.

**Jason Lopatecki:** Yeah, I agree. And I think it gets more complex like I found there’s so many ways in which GPT-4 fails in some generalization. In some very unique ways. So I think they kind of take a very simple approach, looking at modular addition here. But I think it’s kind of important for a broader set of use cases.

Let’s hop in. So, explaining grokking. In the beginning here they simplify it down to memorization or generalization. So you can use parameters for memorization, or parameters for actually learning the skill, I guess. And in terms of the big picture, I would say, there’s an argument made for why grokking occurs: so how does a network generalize to solve a problem, how does it move from memorization and generalization, and how does that tie to a concept of efficiency and training that trades off essentially parameters used, and where does it come through and what are the loss functions and equations? And what can you use to predict that?

And the core question I think, is why does a network improve dramatically upon continued training already having achieved good performance? So you achieve good performance in your training set, poor performance and training set poor performance in your test set, and at some point there’s a breakthrough where your test set improves drastically. At some point you’ve learned the skill you learn, the generalization that goes beyond your training set for this.

They talk about circuits here. Do you want to describe how you see a circuit and what’s your view of this concept of a circuit?

**SallyAnn DeLucia: **Yeah, I view them as like these modules that we can use for testing these hypotheses. I think, like you can get into a lot of detail there, and they can mean a lot of different things in different contexts. But at a high level that’s what your circuits are going to be. It’s going to be for us to actually test out these theories and the various algorithms.

**Jason Lopatecki: **Yeah, if you’re doing module addition–there’s one way of doing module addition, and there’s another way of doing module addition, and there’s another way to do module addition. They’re all circuits and ways that the network could learn to do it. And they can all be happening in parallel with edging each other out. But it’s just this idea that there’s a lot of ways of accomplishing the task that might be being learned at the same time.

And I guess the point here is kind of one which generalizes well. There’s an idea of a circuit that maybe learned how to do addition, like we learned in school. And maybe there’s one that’s just rote memorizing data. And obviously, that’s going to be the one that struggles on the test set. So when they’re multiple versus when there are multiple circuits achieving strong performance, you know. Weight to K prefers circuits with high efficiency. To be honest I think this is the core point of the whole paper that they’re trying to make which we’ll dive into deeper. And *C*gen, by C it’s the circuit that generalizes. So this is the module addition we learn, or this is addition that we might learn in school versus ??? copying a table or something, and just memorizing the points in the table.

I think the point here is that there are three key properties, which is the circuit that generalizes while cm does not. So that’s kind of one property that they’re demonstrating here. Another one is that the circuit generalizes is more efficient. And do you understand what they mean by efficiency? We’ll dive in later, but I think the point here is like, what’s the mechanism by which gradient descent chooses one versus other? And the last one is just I guess the other key property is just the circuit for generalization kind of kicks in later and then, since *C*gen generalizes well works for new data points. Do you want to describe this? I mean, this is like, the whole idea of generalization.

**SallyAnn DeLucia:** Yeah. So I think with regards to that, the generalization and it performing better on the new data points. I think the real thing is that both of these circuits can offer good training, but only that generalization one is going to be the one that performs well on the unseen data. And it’s going to kind of achieve that through some level of the cross entropy loss on the training with those fewer parameters. I think those are the two key things that I think of in this.

Anything else that you think of?

**Jason Lopatecki: **No, I think I think that’s exactly it. It’s like this whole concept that they came up with with efficiency, which they define later on here. But the idea is efficiency should be independent of the training size, like of the data set that should be independent of the size. That if you generalize addition, you can do addition with like 10 numbers or 50 numbers. And you can get a bunch of examples that you’ve never seen and you should be just as efficient at calculating those, meaning you don’t need to add more parameters to understand how to do that type of addition.

**SallyAnn DeLucia: **Yeah, I think even on that is like they noted that like, if the customer can’t generalize well like, it will remain consistent at any point. Even when those new points and if it can’t generalize, then there’s really no hope for that.

**Jason Lopatecki: **Yeah. And then I think these graphs were interesting. This one kind of tells you the first view of grokking. Do you want to describe what the red line is, what the orange line is and what’s going on here?

**SallyAnn DeLucia:** So what we’re looking at is the grokking phenomenon that we’re talking about here in case we didn’t explicitly say, I just think this is important. So this is just that phenomenon where the neural network is going to memorize its training data. But it’s going to perform poorly on new, unseen data, and until it eventually learns to generalize well, and then that’s like, well past your additional training.

So when the grokking is kind of occurring, we’re seeing the test accuracy that’s going to be that green dotted line. And you can see that it’s kind of moving really low in the beginning, where our training loss is low and our test loss is high there, and you can see as we approach, and we start reducing our training loss and our test loss. You can see at that kind of point then, our test accuracy increases. So it’s kind of that trade off.

So in the beginning portion there, we’re kind of in that memorization phase. We’re doing really well on our train data, but we’re not doing well on our test data. And as we continue to train, if you follow that kind of red line well past maybe that point of where we think that we’re doing well on our training set, then it’s going to kick up. And then we’re gonna see that improved test accuracy which is where that grokking is actually happening. So that point where you see the loss kind of decrease and the test accuracy increase, that’s kind of where we’re seeing that grokking happening.

And we’ll get a little bit more later on to have the data set and all the other parameters play into that.

**Jason Lopatecki: ** I feel like the ungrokking was one of the more interesting things in the paper, too, which is a little bit different, I guess, than sometimes you hear another industry term: catastrophically forgetting. In this case, though, they train on a smaller set and show that you can actually go back to where you were in terms of your test loss so I think this is interesting–I don’t think I’ve seen this anywhere else yet. But, I thought this was interesting where they dive into this. I feel like what was pretty useful about the paper is they like actually predicted this, and it did what it did by their theory. And I think this is you know, efficiencies should decrease as training size increases. We talked about that. There’s a crossover point, so you kind of see it up here–they talk about your critical data size. I think that was another interesting thing from this paper, like the whole idea that with enough data, you can generalize. I mean, that’s another kind of subtle point like, throw enough data at it, and you can generalize which seems to imply that more data is better. But I thought that was kind of an interesting thing that came from this theory. I guess we kind of know that, but it comes from the paper here.

**SallyAnn DeLucia: **Yeah, I like the evidence of it all really is kind of like you said. We kind of know that in theory. But here it’s really showing you what that point is, and where that trade off between memorization and generalization is in relation to that data size.

**Jason Lopatecki:** Yep. And so in un-grokking, we talked about this. They first get it to grok, and then they go and train some more on a smaller data set and get it to ungock. So I think it’s a really good case for their theory, at least on the small example they have actually being cracked.

And then the semi grokking. It’s an interesting phenomenon. They describe it. It seems that it’s kind of like when you’re on the borderline of the critical data set, what happens. We’ll dive in deeper, but it definitely seemed like un-grokking was easier to figure out what that critical data set size was, where semi grokking was a bit harder.

And it’s kind of the contributions they make here to really demonstrate the ideas behind this. They go through the basics: classifier here, the core idea is that there’s a probability here, and that probabilities the logit size, and there’s some relation to the number of parameters needed for that same probability. So that’s one of the big ideas, in this. You know anything else you’d add to that?

**SallyAnn Delucia:** Not really in this section, I think, as we scroll down and we take a look at that loss there is just kind of really highlights the balance. I think that for me the other stuff is more straightforward, but I think this is super important here. Right? So we have the cross entropy loss that drives the class far loss to increase in size, and then the weight decay works to reduce the model’s parameters. So we really need to balance those two things because they’re kind of opposing forces. So I think that was the main things from this notation that I was like, okay, we have to remember that as we move on.

**Jason Lopatecki:** Yeah, exactly. And I think the subtle point in this is that there’s one side here that probably is favoring. *C*mem. which is like, let’s just increase parameters and increase logics. And there’s another side. That’s favoring the *C*gen, which is the which is the wait decay side of this and and the wait decay is just trying to, you know, smallest parameters as possible. So there’s this, this balance and trade off between the two and and there’s an argument that you know. The argument they make, I think pretty solidly, is the way decay is actually what’s responsible for the generalization. Also there’s kind of trade offs between cross entropy and weight decay


The defined circuits which we talked already about. Yeah, the different ways you can get at your task. And then the other thing we talked about is given multiple algorithms, you know, given an algorithm, there’s actually multiple circuits that there’s many, many ways in which you can actually solve, including memorization. And this kind of hits that first point which is like the you know the first term is kind of driven by gradient descent and scaling up the classifiers. Logics. To make it more confident, so it’s like that first term’s kind of incentivizing more parameters. Where the weight decay is kind of pushing you the other direction. So decreasing the parameters. And then you can think of parameters as memorization like you’re going to need more parameters to memorize. So this push to do it with less parameters means that you can’t memorize as much.

So it’s kind of like those two opposing forces that they’re arguing here.


And then, any thoughts from this one? When we have multiple circuits achieving strong accuracy. Constraints apply to each individually. I mean, maybe it’s kind of hinting at semi grokking, what happens in that phenomenon where you have lots of stuff going on and things opposing each other, balanced by each other at about the same rate.


**SallyAnn DeLucia:** Yeah, I just thought, this is kind of interesting, too, how they talk through intuition. They’re saying Okay, intuitively, the answer depends on efficiency of each circuit. That is the extent to which each circuit can convert relatively small perimeters into relatively large logic. So I think that that’s kind of it ties back to that push and pull again. But I really appreciated the way that they broke this section down for me, like when you’re reading any of these papers that are kind of heavy on logic. I felt like, okay, I’m following them at this point, that does make sense.


**Jason Lopatecki: **And I highlight this one even deeper, because I think it’s like the core of the idea. There’s this idea of efficiency and efficiency is less parameters for the same logit or probability and, like the more efficient circuit kind of wins and end. That’s kind of what their their point is.


I guess one question. I don’t know if I thought this was answered, I mean, do you think there’s really a reallocation or does just one term beat it, or because there’s a parameter norm term. You’re going to be shrinking the *C*mem parameters at the same time increasing the circuits that have the generalization ability.

**SallyAnn DeLucia: **Yeah, I had the same kind of pause there, I’m like, what are we actually like reallocating? And I think it’s just kind of that trade off that they’re talking about here is like, it’s just kind of what’s naturally occurring like as we like, approach like. So the see, *C*mem, is gonna happen a lot quicker. And like, as we approach that point, it’s kind of gonna switch over then to where the *C*gen becomes more efficient there. So I didn’t really see there’s like a literal reallocation. But that was my interpretation as well.

**Jason Lopatecki: ** And it says the overall explanation relies on three ingredients. I think we’ve talked about generalization a lot. We’ve talked about efficiency as well. The slow versus fast learning, I guess the point there is there’s some transition point where this kind of moves from one to the other.

And then what they do is construct a really simple example. But it’s actually a module addition example, that both is set up with a training set that pushes memorization. There’s one that helps also test the generalization. So it’s like a really simple hand crafted single algorithm experiment which the other question is whether that’s going to generalize (no pun intended) to other types of circuits.

**SallyAnn DeLucia:** I thought it was interesting, too, that they made all these assumptions in the design choices were really designed to be simple, analytical and traceable rather than reflecting, like real life examples of this in practice which I thought was interesting because, for me if they jumped right into like grokking in practice I probably would’ve been lost. But since they did this approach, I thought it was easy to “grock” what they were saying.

**Jason Lopatecki: **They talk about a classifier here on the memorization and the test set. My takeaway here was they’re trying to model the learning. I didn’t read the paper behind this where they split these out. But they’re trying to model the learning process on the data sets. And there’s some challenges to being able to do that. So it looks like you need to split out into sub-weights.

There’s a question of how to model the parameter norm when weights are not all one so they kind of intuitively increase weights corresponds to increasing parameters. Internal networks of scale up resulting outputs. So that they have come up some other way here that they represent like how to look at efficiency and how to model the parameter norm for this case. Any other additions for these sections here?

**SallyAnn DeLucia: **Yeah, for these sections here for me, it really just was like laying the groundwork of what assumptions were made, what was the setup process they used, so that you have that clear understanding when we get into the next section. What are the phases that need to take place for grokking to come up. And you know what assumptions they made to contribute to that, was really my take away from that section.

**Jason Lopatecki: **In this section here, why generalized circles are more efficient. So this kind of talks about why *C*gen is more efficient and its relationship with data set size, I think this is probably I don’t know one of the more interesting findings. I mean the fact that they did find relationships between data sets. You know, the relationship between data set size and the grokking in this was actually some of the more interesting findings in addition to like the ungrokking.

**SallyAnn DeLucia:** It’s kind of interesting too, because it kind of seems like the perspective here when we get to the section is it’s kind of focusing on the generalization aspects, like, kind of making the assertion of okay, the classifier can generalize well. Then it will remain that its efficiency will remain constant. But if it fails to generalize, which kind of made me feel like, okay. So now we’re talking about the memorization piece then it will just struggle. But it’s kind of interesting that they focus more on the generalization lens in this section.

The note I wrote was that the generation circuit is able to maintain efficiency because it doesn’t need to significantly change those parameters to adapt. Whereas the circuit for memorization has to adjust those parameters for each new data point. And that’s where it’s really losing that efficiency and that for me, like really kind of drove that point home for me.

**Jason Lopatecki: **And then this is probably the most important thing that, you know. I think it’s the biggest challenge out there, like, how much data do you need and like? And obviously there’s going to be many circuits for, for, say, a GPT-4 right? Like, there’s so many things it’s learning. But what’s the right data size, and what’s the critical data sizes that you need to actually generalize. It’s an interesting point too here, where it’s kind of like more data, not more training. I think that’s a very subtle point that what’s needed in this case is more data to generalize. Not necessarily more training. So, maybe there’s some big idea out there in the LLM space on this. So the data critical point at which you know the point is like, it’s kind of whether they’re equally efficient from a certain perspective. So I think that’s kind of the the core idea is that the transition points where those lost functions, those 2 parameters and lost functions are training off against each other

And then there’s the effective weight decay. I thought this was kind of like their other big point that it’s based upon data size, not a function of weight decay itself, that the weight decay maybe determines where in training, it happens, but not necessarily, if it happens or the strength of it.

Yeah, so that’s the point, like, it *may* affect that like when it happens, not IF. Ungrokking might be something that people end up using. I think this is a fascinating idea, unlearning skills might help you tell what’s your critical data set size. I thought that was another fascinating thing here. Maybe there’s some use for that.

**SallyAnn DeLucia: **Yeah, I thought that, and also something to be cautious about, too, as well. If you have your models grokking, and then you try to do some additional training with the smaller set, beware of this phenomena that might occur. You’ll see that performance go down as a result.

**Jason Lopatecki:** Yeah, it’s kinda like, be wary of too much fine tuning, I guess. Can you break skills by fine tuning and on some weird, smaller data set? I think you see a lot into the LLM stuff where people mix in the training set with the fine-tuning set, so like they might randomly mix it, you know, for large fine tunes.

**SallyAnn DeLucia: **That’s kind of exactly what I was thinking. When I read this I was like, I wonder how this relates to the fine-tuning in LLMs? Because you have this extremely large data set that we’re doing our pre-training with fine tune on too small, is that why we don’t see the performance improvement that we would think with fine tuning for LLMs? Because for a while it was like: Oh, you only need 100 data points to fine tune, right? Maybe that’s just way too small. So that definitely got me thinking, when I read this part.

**Jason Lopatecki:** Yeah, I think the good news is normally, you know, the fine tune approach is you’re freezing an Lm, you’re typically freezing the weights, maybe doing LoRA, or something like that. So you’re probably not causing this problem. So it’s worth noting, but I’m not quite sure that breakage is going to totally occur in those situations.

“Ungrokking can be seen as a special case of catastrophic forgetting.”

What do you think catastrophic forgetting is, or what’s that to you, SallyAnn?

**SallyAnn DeLucia:** I honestly haven’t read the paper there that it’s mentioning, but just like kind of looking at it where the model starts forgetting, like some of the information that it’s been trained on things that it’s referenced before. And it just causes this total degrading of performance. That’s kind of what I think of it as.

**Jason Lopatecki: **Yeah. If he and and those of you who’ve been out there, there’s a recent paper on reversal symmetry, A versus B, and it’s kind of taking a bunch of examples where someone’s the parent or son of someone, and sees if it knows the other relationship. And they gave some examples of fine tuning where it knew something, or it knew that relationship. And then you train on some data like breaks, breaks the thing it knows. So that’s kinda the way I see it is that you know something, and then you’re breaking what you know by some fine tuning exercise.

I thought this was kind of like the core core view. So you have your logits, colors by data set size, and a very clear pattern of parameter norm, increasing by data set size for a fixed legit. And then down here it’s all mixed in, you can do larger data, get the same logic or probability of output, but with a smaller set of parameters.

This was an interesting one. With the ungrokking at different data set sizes. So this is you know, as you run with smaller data sets here. you can get poor test accuracy versus versus, you know, the larger I mean, it just shows we’re very clearly. And then I think their point was like with different weight decays. They all collapse on top of each other here.

If you really want to know your critical data set size, that ungrokking might be the better thing to use. It’s much more clear from a transition period. And they talk about related work. I think their point is like there are some examples of grrokking occurring in places where there isn’t weight decay.

So I think this is kind of you know the final thing which is like the different open questions they have within grokking here. And if people have any questions for the authors, or want to leave them, the authors actually offered to answer any questions. So if you all have questions that you want to put to the authors, or talk to the authors about and I think one of the biggest ones is like it’s still open to me is generalization is so important, you know. Get these skills that come out. And all of a sudden you get them and predicting generalization, understanding, generalization like how to like, you know this is a very simple example of modular addition, like what can you say about like data set size versus generalization versus fine, like, I feel like there’s a bunch of open questions in addition to that, the one we brought up on fine tuning.

**SallyAnn DeLucia: **Yeah, I definitely agree with that data set size. I was just even curious about, you know, like the estimation of that, that critical data size, and how it was initially estimated. And I was also curious about the loss function that they chose to go with, and if they considered any other. So I’m looking forward to getting some answers on that.

**Jason Lopatecki:** Thank you everyone for joining us on grokking, and we’ll see you next time.
