---
title: 'Breaking Down Reflection Tuning: Enhancing LLM Performance with Self-Learning'
topic: models
subtopic: fine-tuning
secondary_topics: []
summary: Explains reflection tuning as a self-learning approach for improving LLM
  performance through critique and iterative refinement.
source: arize
url: https://arize.com/blog/breaking-down-reflection-tuning-enhancing-llm-performance-with-self-learning/
author: Sarah Welsh
published: '2024-09-19'
fetched: '2026-07-11T04:50:00Z'
classifier: codex
taxonomy_rev: 1
words: 4847
content_sha256: 8447ca921659bdc906681c00cb40061217ac24be8985c786532f8c7273e1b5bf
---

# Breaking Down Reflection Tuning: Enhancing LLM Performance with Self-Learning

![CPR Reflection-Tuning - blog Rohan Pandey and Dat Ngo headshots](https://arize.com/wp-content/uploads/2024/09/CPR-Reflection-Tuning-blog-1021x560.jpg)

              # Breaking Down Reflection Tuning: Enhancing LLM Performance with Self-Learning

A recent announcement on X boasted a tuned model with pretty outstanding performance, and claimed these results were achieved through reflection tuning. However, people were unable to reproduce the results. We dive into some recent drama in the AI community as a jumping off point for a discussion about Reflection 70B.

In 2023, there was a paper written about reflection tuning that new model Reflection 70B draws concepts from. Reflection tuning is an optimization technique where models learn to improve their decision-making processes by “reflecting” on past actions or predictions. This method enables models to iteratively refine their performance by analyzing mistakes and successes, thus improving both accuracy and adaptability over time. By incorporating a feedback loop, reflection tuning can address model weaknesses more dynamically, helping AI systems become more robust in real-world applications where uncertainty or changing environments are prevalent.

Dat Ngo (AI Solutions Architect at Arize), talks to Rohan Pandey (Founding Engineer at Reworkd) about Reflection 70B, reflection tuning, the recent drama, and the importance of double checking your research.

## Watch


## Listen

## Dive in

- [Read Reflection Tuning: Data Recycling Improves LLM Instruction Tuning](https://arxiv.org/abs/2310.11716)
- [Read Rohan Pandey’s Paper: gzip Predicts Data-dependent Scaling Laws](https://arxiv.org/abs/2405.16684)
- [See more paper readings](https://arize.com/ai-research-papers/)

## Analysis

### Introduction: Reflection 70B Drama Overview


**Dat Ngo:** Awesome welcome folks to this week’s paper reading. Let me share my screen real quick.

So yeah, this week’s paper reading is gonna be a fun one, maybe a little less traditional than how we normally do. Normally, they’re pretty technical. And we go kind of in depth into the paper and why it’s important, which we will do in this week’s paper.

But before that we’ll maybe go over a little bit of the kind of drama that happened last week, and it’s kind of still ongoing. But this week’s paper reading is about reflection tuning.

Basically, you know, the title is data recycling improves LLM instruction tuning. But we’ll actually go over what that means.

But today with me I have a pretty awesome guest, friend, and researcher. If you haven’t seen his work you should definitely check it out. He’s also an archive author, but I’ll let Rohan introduce himself.

**Rohan Pandey:** Hey, guys I’m Rohan. Founding Research Engineer at Reworkd, we focus on web data extraction.

So some of our customers actually use us for creating fine-tuning data sets and rack data sets for their use cases as well. But yeah, I’ve worked on language models, most recently put out a paper called Gzip that predicts data dependent scaling laws, showing that scaling laws for language models are sensitive to the complexity of the training data that they’re trained on. And generally, I’m super interested in these data centric approaches.

So, when Dat suggested that we could hop on and talk about this data recycling approach from last year, it sounded interesting.

I’m looking forward to diving into this paper with you guys.

**Dat Ngo:** Awesome thanks for the introduction. My name is Dat most of you all know me. I’m a Solutions Architect here at Arize. So a lot of building love these research papers. Love being in the space and Rohan is a very big part of the AI community here in SF, so I just wanted to add a new face to the mix. But let’s go ahead and get started.

So, you know, while people are coming in. I just wanted to quickly plug Arize Phoenix. I think most of y’all on the call should know what Arize Phoenix is. But if you don’t, and you’re building LLM applications, and you want a great open source tool to understand, you know: hey, what’s happening? Can I get some sort of observability? You can add like a few lines of code, and then you can get things like traces and and really get a good sense of what’s happening in your application.

But let’s go ahead and move on to the agenda.

So like I said, this one’s going to be a little different than normally. Normally, we just dive straight into the paper.

We’re gonna do a little storytelling here of why I wanted to do this paper reading. I think there was a bit of drama on X or Twitter, whatever you call it, last week. The entire AI community was kind of watching, there was stuff that kind of made the news.

And so you know, there was something called Reflection 70 B that came out, which we’ll cover in a second, and it really just sparked my interest, and I realized that I didn’t know what reflection was.

So the first half will cover for those folks who don’t know what happened last week–it’s still kind of ongoing–and what the result was, and then we’ll actually review the paper in which you know, kind of sparked my interest, and like oh, I missed the paper last year, and I wanted to reread it so that’ll be for the agenda today.

So let’s hop into the first part.


![September 5th overview including screenshot of tweet about Reflection 70B](https://arize.com/wp-content/uploads/2024/09/Slide-1-1024x571.png)



Today is September 11th, so about 10 days ago there was an announcement kind of like a tuned Llama 70 B with some pretty outstanding performance. This was a pretty important breakthrough, because–I think it was a mid size model that on par-ed, or equalled some of the best models in the world.

And I think what a lot of people thought this was a major breakthrough for a stepwise function for LLMs. So I got word of this on Twitter, but Rohan, not sure how you kind of heard of it.

So the next day news gets out that there’s this mid size technique called Reflection Tuning that basically made a mid size model perform super super well, and that there was an expectation that they were going to run this technique on you know Llama 3.1 405 B.

And who knows? That might have gotten us like an amazing kind of model out of this that maybe outperformed.

And the coolest thing is like it’s open source, right? So that was my take, Rohan. I don’t know what yours was, but when I was like, what is this? And I realized I had no idea what reflection even meant. And then hence this paper. But what’s your take, Rohan?

**Rohan Pandey:** Yeah, when I first saw it I was pretty skeptical.

The general consensus right now, in the research community is that a lot of these evals have become sort of like good hearted which refers to good hearts law, where once you define a metric of success, that metric ceases to be a metric and becomes something that people try to solve in and of itself right.

So when MMLU was first proposed, it was a pretty good metric for measuring whether a model had all this kind of knowledge and reasoning ability.

But as more and more people started using MMLU to focus and improve on their model performance. In some sense we over fit to MMLU. No one’s training on MMLU. That’s not what I’m saying, but people themselves by trying to push performance on MMLU, that reduces the usability of MMLU for measuring overall kind of model intelligence. And like that, I think that people have started realizing this over the last several months.

And this was sort of like the nail in the coffin for me. Like, if these results were true, then there are trivial ways to fine tune and enrich data in some way that scores amazingly on a lot of these metrics in ways that intuitively shouldn’t be possible. But at the same time there are really respectable people in the community who believed it upon first glance.

So like some Open AI people thought that it was pretty legit, and that makes you think, like the kind of synthetic stuff–the synthetic data stuff they might be working on at frontier labs are probably directions that are along the same lines.

### The Saga Continues: Reflection 70B Results Can’t Be Reproduced

**Dat Ngo:** I was a little…the GSM8K at 99.2% I don’t know about that, man. But anyways, it was just a big announcement, and it got like everyone kind of heard it. And of course, it did make the news right, people wanted to interview these people. There’s this thing on YouTube.

Let’s bring us back to September 7th, two days later. So this was released on Hugging Face. And then people tried to recreate the results right? Like with any good research, you know, should be vetted by your peers. And the long story short, is actually: people couldn’t recreate the results.

Some people thought the performance results kind of equally matched Llama 3. It just didn’t perform like the announcement kind of said.

And then this is where things kind of kind of took a turn. If you don’t follow Shin you can follow Shin Boson, he has a really good write up of where this kind of came from. But there, there’s a series of events, and you know, we won’t go into depth. We don’t know what’s right or what’s wrong, and there’s a lot of kind of hoopla.

But I think the AI community has just been sitting back while eating their popcorn and just kind of watching this unfold.

![Reflection 70B results can't be reproduced from the model released on Hugging Face](https://arize.com/wp-content/uploads/2024/09/Screenshot-2024-09-19-at-3.50.51 PM-1024x575.png)


So it was very hard to recreate the results. The team that originally put out the weights said: Hey, we put out the wrong weights for whatever reason, and they tried to host an API. And then there were like: We weren’t sure what was behind the API and anyways, long story short, you can Google it yourself and find the Twitter feed. But I think my, take away from the mess that kind of happened after that can help transition us into this week’s paper is that the AI community investigated this, but ultimately couldn’t be verified. But I think the moral of the story is like, if you’re a researcher. Always double check your results.

You never know when you have a data leakage. Or maybe you’ve overtuned. MMLU is not very useful anymore. Because, like Rohan, said you’re just like missing the point right? It’s just a metric for me. It’s a means to an end. But it’s not the end right?

And the other thing is. There could be data leakage. Our models are just getting better and better. And I really like private tests like private data set tests that people have curated.

And then the other thing for the community: It’s important to verify other people’s work.

And so that’s what I would say, the moral of the story is–but Rohan, would love your take on the messier events afterwards.

**Rohan Pandey:** Yeah, no, I totally agree with you there in terms of methodology. Yeah, research. Like, the traditional kind of advice in academia is, there’s like a saying I don’t remember who it’s attributed to, and I forget the exact wording. But basically, if you perform really well on a benchmark, it doesn’t mean that your method worked, it means that you have a bug in your code.

So usually, that is what is happening. And the most interesting, the most compelling and generous hypothesis for what might have happened here. I don’t recall who posted or where the Twitter thread is. Maybe I can find a link to it in a bit. But, like the theory is that Matt is actually not all that technical he had some like somewhere in his LLM pipeline. He had like some call to like Helicone, we sort of use this at ReWork like Helicone. There’s an open pipe there, there’s some of these tools that sort of do this caching for you? I’m sure. Yeah, I’m not sure if you guys have like a prompt caching type of offering as well.

But the theory is that maybe he had something like this in his pipeline, and when he tried running the reflection weights that were given to him by the I think he was working with Sahil. Something failed in the pipeline, and instead of going to reflection it instead, went to like the Claude API, or something like this.

Then he benchmarked it, and he was like, Wow, like this is crazy. The performance is so good, entirely forgetting that he had this like caching layer or routing layer in the middle.

So that’s like, yeah, the most generous theory. And like then after that, he deployed it, showing the privately hosted endpoint was like on his own machine. It had the same kind of routing thing. So then, when everyone else came and tried to test it, they were getting Claude responses. And it wasn’t him like trying to actively redirect them to Claude. But just that’s the way his like proxying service was set up. And once he realized that that was in the middle of then he sort of went silent for two or three days. And that’s like the most generous theory painting. Matt is like not a malicious person. But who knows?

### Overview of Reflection Tuning

**Dat Ngo:** Yeah. So I’m not gonna speculate on intention. But just maybe we focus on the facts. But I totally like it’s definitely possible, and I just think it’s very important to always double check your work. But I love that take, Rohan.

And so that brings us into this week’s paper, which is not actually a very long one.

So actually, the paper is very short, actually, but novel, interesting technique. But I had just never heard of reflection tuning.

And so I was like, oh, this would be great, because, with all you can think that the latest drama and that so some folks haven’t heard of reflection tuning, myself being one of them. It was a paper that came out in 2023, so something I’d missed. But definitely so this won’t be a super long paper. Actually, the idea behind it is actually pretty straightforward. And so we’re going to cover here.

And so, yeah, reflection tuning. If you haven’t read the paper again, it’s a really short read. This is kind of the point of the paper reading, so we’ll kind of distill it down.

I think the premise of this paper is like, here’s some of our axioms.

So we know that LLMs are token classifiers right? The reason why they feel helpful is because we also give them instructions. So it’s like: Hey, you’re gonna help the user with XY, you’re a helpful assistant doing XY, and Z, I’m sure you all seen that.

But basically LLMs are given instructions or instructions to control the input, and output. And then so they’re fine tuned on instruction data to help make them, you know better at producing the output that we want so instruction tuning is really just like the LLMs ability to follow instructions. Generally, there’s like an instruction tuning data set. And the better this data set is, the better the model will kind of perform the instructions that are kind of set for you.

But the thing with Instruction tuning is that it’s really affected by the quality of that dataset, and vice versa.

So if you have very good instruction tuning data sets. They’re obviously gonna perform really well. And obviously, the opposite, is the opposite of that. I think in terms of the method. And then Rohan, anything else you want to add to that?

**Rohan Pandey:** Yeah, I think the biggest thing is that improving training data quality is obviously… my view right now is that LLMs are essentially data wrappers.

Like, you can obviously push a lot of performance by like, you can push some performance by doing architectural level tweaks and systems-level like optimizations and whatnot.

But a lot of the time it really just comes down to what’s in your training data. So I think the paper is looking in the right direction of like, let’s improve instruction data. And I think there’s a lot of work focused on synthetic data approaches. There was definitely a whole like synthetic data hype cycle. Late last year, early this year. For enriching and improving current data sets.

The reflection that they do is different from the reflection that Matt does in the sense that, like Matt’s reflection, is a subset of their type of reflection. So their reflection is like some, yeah, I mean, I’m sure you’ll jump into it. But the reflection in the Matt sense is a very specific type of reflection, and I think it induces like a second order reflection that the approach that they talk about at least–they don’t have very illustrative examples, but the approach that they talk about doesn’t seem to be as powerful necessarily as what Matt had suggested.

But yeah, I mean, yeah, sure we can dive into the paper next if you want.

### Reflection Tuning vs. Reflection 70B

**Dat Ngo: **I think, is what you’re saying. Maybe I missed it, Rohan is like, you’re saying that the Reflection 70B is not the same as this paper?

Oh, yeah, 100%, it’s not the same as this paper. But, even the data enrichment method that Matt used is not precisely what they propose in this paper.

So like the data enrichment method that Matt proposes with these reflection tags that go after…you chain of thought before then you generate the response. Then afterwards you do this reflection.

That is an instruction tuning enrichment approach, and it does require an Oracle LLM to rewrite instruction data, exactly as this reflection tuning paper does. But it’s a very specific instantiation of this idea of reflection tuning, whereas in this reflection tuning paper, you don’t actually need to have chain of thought tags before and reflection tags after often, in some cases the reflection data enrichment step actually reduces the token count of the instructions.

So it is definitely a different method, but same direction of like instruction instruction data set enrichment via synthetic data generation.

**Dat Ngo:** Gotcha that makes sense. I didn’t even realize that, to be honest with you, Rohan. So I’ll maybe cover this paper, and then maybe you go into depth of like the major differences, because the reduction of tokens is interesting, and then you have tags, as in like metadata tags.

**Rohan Pandey:** Yeah.

**Dat Ngo: **Interesting! And then those tags are being produced by an Oracle model.

**Rohan Pandey:** Exactly in Matt’s approach, but in this one, as far as for my reading there, there’s no mention of tags.

**Dat Ngo: **Right? No, there isn’t. Okay. So let’s maybe cover this paper and we’ll go over the differences. I’m learning on this one, too.

I think the reflection tuning method. So for those who don’t know what an Oracle model is, that’s a new word for me, too. Oracle model is just like I don’t know in this paper. It’s like a bet like your best model, right? It’s the thing that is going to be doing the chain of thought or tree of thought, whatever it is. To improve this particular data set or set of tokens if you will and so. I think the novel approach in this paper was about improving both instruction and response pairs together. And so that’s an important detail.

That you would improve one and then improve the other. And this ultimately increases those pairs on the pair data using the Oracle model. So you imagine you use a good model to basically chain of thought or tree of thought on maybe the original data that you had, the instruction and response pairs. And then this produces essentially like a better quality data set

And so let me pull this up real quick. So the core of that method is to do that. You know. So like, why does this set this apart from maybe other methods.

I think previous methods to this paper only focused on improving either the instructions or the responses. But in this paper it’s really just focusing on both. So it’s not just like improving the questions in a textbook, but also like the answer key, if that makes sense.

And so I think in terms of the process for how they did this. So the reflection tuning process occurs in two phases. The instruction reflection phase evaluates and refines instructions based on factors. So they have, like their measures. So it’s like complexity, require detail, level of reasoning, etc.

And then the response reflection phase then optimizes the corresponding responses.

But considering aspects like, I think it was relevance, relevance, relevancy, accuracy and depth of information. And so this kind of phased approach ensures that, like both of the components of this like instruction response pairs are optimized.

And then, you know, potentially leading to more effective instruction tuning. And so they are, you know. So how do you figure out if this works or doesn’t work? So you can have a hypothesis. So to validate this method the researchers in this paper applied reflection, tuning to to at the time prominent data sets–I think Alpaca and Wizard LM. And so they conducted these series of evals on the models trained with these enhanced data sets. And then the evaluation methods included. Like pairwise, comparisons performance between on the like Alpaca eval, leaderboard and tests on like hugging face open. Lm leaderboard. Essentially these techniques provided an assessment of like, how good we’re, how good did it perform? Basically, with these different sets makes sense right?

And so I guess what the results were there were kind of promising models that were trained on reflection tuned data were much more consistently outperforming their kind of counterpart trained on like the original data set.

I think more noticeably they showed significant improvements on ARC. I think Hella Swag, there’s a couple of other things…but anyways they performed better, more consistently.

And so this suggested that it’s not the quality of the training data can sometimes be more impactful than model size. Again, I think it’s like this equation. And, you know some parts are responsible for some sort of effect.

But anything you would add to this Rohan, making sense?

**Rohan Pandey:** Yeah, your last comment on model size versus data quality. This is basically exactly what my Gzip scaling laws work a few months ago investigated where basically, the assumption early on with the scaling laws literature was that your scalable offer performance is agnostic to the type of data you’re trained on, bit what was found anecdotally in the literature in the few years following that in 2022, 2023, was that there was simply a deep seek paper where they found that as your gets cleaner and cleaner, you pass it through these processing steps,  the scaling law that emerges requires less data to reach higher levels of performance.

So yeah, my Gzip scaling law paper investigated that in like a more rigorous kind of controlled setting, showing that you can actually measure the cleanliness or complexity of your data using Gzip compressibility.

So it’s a similar idea to what we see here where? Yeah, focusing on data quality can often be a much more powerful lever then yeah, just pushing model size or even like a ton of data.

So yeah, I think definitely, there’s been a lot of focus as a result of those realizations on getting high quality data, focusing on data filtering and so on. The other famous paper in this space is like, Textbooks Are All You Need.

So yeah, no, I think it’s an important direction.

**Dat Ngo: **Yeah, I did link the paper. If you hadn’t read Rohan’s paper you should definitely check it out. I found it super super interesting, especially the novel method of using Gzip instead of like some sort of form of like, I don’t know entropy, if you will. That was pretty cool.

Okay, let’s maybe go over to the analysis like some takeaways, I think that’s always good. But the one really cool thing. You know, obviously, we went over like the methods for how they improved both the reflection and the response.

I think the interesting finding was how were those pairs changed?

And the finding was that like that adaptive nature from like chain of thought or tree of thought, in this paper it tended to elongate like simpler instructions, and tended to simplify more complex ones. So maybe making things more homogeneous. In terms of like token, token, link, like variability, which is super interesting.

And so it’s just very interesting that it can, that that was like the approach, and that maybe that it demonstrates versatility across maybe different types of instruction tuned data sets so like, how do you deal with more heterogeneity in those?

Every data set might be different and looks different. This might be important, because that adaptability might be crucial for just being applicable in more different use cases, right?

Different use cases require different variability. And so when I think about the conclusion of this paper. It’s like, really at the time it was a promising method for enhancing the quality of instruction to data sets. I think it’s just if I had to put it very simply, you’re just increasing the quality, not using a human. You’re basically recreating like instead of having to pay people to review the data and make them better or worse. You’re just having kind of an element do it via chain of thought and then you’re measuring it.

But yeah, Rohan, I’m just curious, what’s your take? I’m curious to understand, because I didn’t realize that this method was completely…not different, but a different take.

So if you want to walk us through that I think that’d be great.

**Rohan Pandey:** Yeah, I don’t recall the super specifics. And I didn’t read too deep into it. And it turned out that it didn’t work or like, it is possible that it didn’t work. It seems like they might have never trained like a model or some like, I don’t think anyone’s actually gotten access to the weights of the model that was supposedly trying to be a reflection tuning yet. So, the general idea here seems to be that chain of thought allows you to… before you make a decision before your model says anything, it allows the model to take some time to spend some tokens thinking about what it wants to say.

And the idea with reflection tuning is like max reflection tuning is sort of another side to it. That after your model makes it just like says something and makes a decision, it can reflect back on what it planned to say. And then change its thinking. There, blah blah…before actually finally saying it out loud.

So yeah, you do this chain of thought thing between the tags and then you reflect upon it. Something like this.

The general idea, though, is that like, rather than just doing it via prompting, Matt claimed that if you just insert this via system prompt and whatnot the models aren’t that good at it? But if you improve the instruction to if you improve the instruction data set and retrain your model on that, then you get improved like reflection types of performance.

So that’s what his hope was, to direct this method. But it’s unclear that it worked.

**Dat Ngo:** Yeah, I don’t know if we’ll see a white paper. That’s probably why I didn’t see it. But thanks for clearing that up. I had no idea, Rohan, that the caching layer stuff, too. So see you and I learned stuff on this. So I’m sure your audience does, too. But if there’s any other questions or hot takes in the chat. We’d love to hear them.

I didn’t see anything in the mid chat, but thanks, for you know joining us on this week’s paper, reading and big shout out to Rohan for, you know, giving his take. I think there’s certain things that I’m not very good at that I think Rohan is very good at. And one of those is research and deeply understanding that space so big shout out to him.

**Rohan Pandey: **Yeah, thank you so much. Yeah, that was super super fun hopping on to chat about this.

**Dat Ngo:** Yeah, and definitely check out his paper on. I thought the Gzip paper was pretty awesome. We might even cover it here in the future. But thank you so much, Rohan. Thank you so much, everyone else, for joining us.

**Rohan Pandey:** Cool. Thank you so much guys.
