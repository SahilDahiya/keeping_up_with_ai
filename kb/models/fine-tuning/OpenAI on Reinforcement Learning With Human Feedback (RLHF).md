---
title: OpenAI on Reinforcement Learning With Human Feedback (RLHF)
topic: models
subtopic: fine-tuning
secondary_topics: []
summary: Summarizes RLHF concepts from OpenAI and how human feedback changes model
  behavior during post-training.
source: arize
url: https://arize.com/blog/openai-on-rlhf/
author: David Burch
published: '2023-05-05'
fetched: '2026-07-11T04:46:45Z'
classifier: codex
taxonomy_rev: 1
words: 2755
content_sha256: 993180a50db80b6635c48a2f6a311c690e50875b17e41ffbce407657064dd681
---

# OpenAI on Reinforcement Learning With Human Feedback (RLHF)

![how-does-chatgpt-work new podcast on research behind chatgpt](https://arize.com/wp-content/uploads/2023/01/how-does-chatgpt-work-1021x560.jpg)

              # OpenAI on Reinforcement Learning With Human Feedback (RLHF)

Recently, we interviewed Long Ouyang and Ryan Lowe, research scientists at OpenAI. As the creators of InstructGPT – one of the first major applications of reinforcement learning with human feedback (RLHF) to train large language models – the two played an important role in the evolution of RLHF models and paving the way for GPT-4. Here are some highlights from the conversation. For more, listen to the [original podcast](https://arize.com/blog/podcast-openai-chatgpt/) and read their [paper](https://openai.com/research/instruction-following).

## What’s the motivation behind InstructGPT? And what are the problems with GPT-3 that inspired InstructGPT?

**Long Ouyang: **I think one of the main issues we’re trying to solve is that when GPT-3 came out there was a lot of excitement about using it to do useful cognitive work, for example, summarizing a news article. Out of the box it’s not exactly designed to do that, it’s designed to predict what someone on the internet might say in a given setting. And it turns out that you can kind of trick the model into performing useful work for you by setting up text that when the model auto completes it gives you what you want.

So for a summary, an example would be, maybe a few examples of an article and then a summary of the article, and then finally the article that you want summarized and tldr, and then you ask them to complete it. So the model isn’t designed to actually be an assistant or a useful tool, but you can kind of contort it to do that in some cases. And the overall goal of the paper and the project–which continues to this day–is to just fine tune the model on an objective function which is to be a useful assistant or a useful tool. And this emerged out of some earlier work on what we call aligning language models.

Actually, Ryan, do you want to talk a bit about alignment at OpenAI?

**Ryan Long: **People have different definitions of alignment, but one definition that you could use is how do you get the AI systems that we’re training to optimize the thing that we actually want to optimize?

Historically, it started with a small team and that’s where some of the initial early RLHF work came into play. That evolved, and now we have a short term alignment team, which is how do we have current language models optimize the thing we really want to optimize which is be useful, be helpful and also mitigate harms and be truthful. And there’s also some work on longer term alignment which is trying to think about new alignment problems that might come up. So there’s some work on scalable supervision and a bunch of other things.

## Could you give us a short elevator pitch or summary of the InstructGPT paper?

**Long Ouyang: **This is an automated system, where you provide some text as an input and it provides you some text as an output. These are probability distributions over what we call tokens, so a token is a part of a word, sometimes it’s an entire word, and you get output from this tool by sampling at every stage what the next token might be and then continuing that process until you’re done. So sometimes you get different results because the model is a little bit probabilistic.

Importantly, the input that you give this model is just a natural language command or instruction like “Write a story about frogs in french,” and it’s trained on a wide variety of different tasks so it can generalize two tasks like write a story about frogs in French which I think was not seen during the training.

And just to highlight the difference between the instruct model and earlier vanilla language models, the instruct model “understands” that you’re giving it some explicit cognitive tasks to do and you’re doing that explicitly in language, whereas previous models, the way that you communicated through the model, the task you wanted done was maybe through some examples or is a more implicit fashion.

**Ryan Lowe: **At a high level, how we get there is essentially using human data. Using labelers – we hire a set of contractors to label data for us, and we do an extra fine tuning stage on top of the normal language model pre-training stage.

One of the main kinds of data these labelers produce given some input like “write a story about frogs,” there’s multiple candidate outputs generated by different models and labelers go and they rank from best to work which outputs they prefer according to some set of instructions and their interpretation of their instructions. And then we train the model using reinforcement learning to try to produce outputs that are closer to the outputs that a human would prefer or rank highly.

## Why train a reward model at all? Why do the supervised fine tuning in the first step?

**Long Ouyang: **So maybe we’ll start with the reward model because that’s the really critical piece of our method.

The kind of data that Ryan referred to earlier where data labelers are giving their preferences over say, stories about frogs, we use that data to train one very large neural network that we call a reward model. You can think of the reward model as almost like a score in a video game or a teacher. So what the reward model takes in as input is an instruction and output and it returns a number and the number tells you how good this output was. If the number was good it means the story about frogs was a good story, if the number is low it means the story about frogs was a bad story. We train this reward model on human judgments so this big model is kind of like approximating what people think is a good attempt at writing frog stories or summarizing news articles or what have you. And then we train an entirely different model to actually do a good job according to the reward model.

So the important piece of our method is instead of doing some other approaches, we’re explicitly learning a representation of what people think is good performance on a task. And then separately, we optimize a neural network to do a good job according to that representation. And so that’s the kind of substantive reinforcement learning from human feedback piece of things.

We’re doing reinforcement learning because we have one model trying to do a good job according to a different model. And then the human feedback piece comes from the teacher or score model that’s trained to predict what humans would prefer. And that’s the meat of the method, and then separately, to bootstrap a bunch of things, we do what’s called supervised learning or supervised fine tuning, where instead of having people give their preferences about stories of frogs that were already written, we actually just ask them to directly produce what’s called a demonstration. So, they themselves are asked to write a story about frogs in french and we train the model to mimic the words that they used in those cases. That happens to be useful for bootstrapping data but it’s not necessarily required to do this RLHF method.

## Do you see other major applications just skipping the first step?

**Long Ouyang:** We still do it sometimes, I think one thing is that few shot prompting is getting pretty competitive now. And so you can sometimes just skip collecting demonstrations because the outputs from the model few shot is already acceptable or just good enough to where it doesn’t make sense to do separate supervised fine tuning.

**Ryan Lowe: **One way to think about it is: RLHF helps you get more fine-grained tuning of model behavior whereas supervised fine-tuning and collecting demonstrations can more drastically shift model behavior. For instance, let’s say you have some model and it sucks at generating summaries. Getting a bunch of ranking feedback between different crappy summaries is not the most useful. So instead what you want to do is collect some examples of really good summaries and then have your model try to imitate that for a bit. And really, it’s kind of an empirical question as to when is it the best to switch over from collecting demonstrations to collecting comparisons or ranking data. And we have some results on this in a different paper but it’s still a very open question.

## How did you come up with the idea of InstructGPT? How did this idea emerge, how did the project emerge within OpenAI?

**Long Ouyang:** We’d actually been working on this method for a while with slightly different motivations. The alignment team is generally interested in not necessarily making the models better–although that does happen as a side effect sometimes–but making them more in line with what we want. And so in a couple of previous papers we applied this method in narrower domains to see whether it would work. And immediately on the heels of GPT-3 being deployed to the public through an API, some members of the team had the thought to apply these alignment techniques that we had developed in previous papers on this new model which we’re now serving to the public.

**Ryan Lowe:** The person who wrote the original Google Doc proposing this was Paul Chirstiano who was at the time, the manager of the alignment team.

## There are a lot of murmurs in the air that the next generation of language models are going to be really powerful. Are there interesting challenges that come from that or are there new ways that you’ll have to adapt this method to deal with these even more powerful language models? Where do you want to take this work?

**Ryan Lowe:** We have a content policy that says that we don’t want the models to generate code to hack a bank or something, and we find that actually it is possible to get criminals to write code to hack a bank. Right now we have this tough process to steer things in the direction of not doing that, but there are still gaps in reliability and durability. So we’re just continuing to own our techniques and make them better and make it so that if you identify some misalignment you can fix it quickly.

There are some recent papers by Anthropic around using models to help this process which are super interesting. One of the things I’m particularly interested in is moving beyond the framework of essentially aligning to the average labeler. And there’s going to be some really tricky questions when we start to ask: to whom are you aligning these models? Right now it’s essentially our labelers plus us through a set of instructions that we’re getting them to follow. And OpenAI doesn’t want to be in a position of where we’re the moral dictator of what’s right and what are the correct values. So navigating that is going to be challenging and involves machine learning interventions but also a broader social technical perspective.

## Are there interesting questions that come up or new challenges or new directions for this kind of research as language models become much more powerful?

**Long Ouyang: **One of the issues is that just making these comparison judgments becomes much harder if those models are very powerful. So an example of a task we’d like to give a powerful model is something like: write a code review for this pull request on GitHub. Models can’t do that today but you can imagine more capable models in a year or two might be able to, and that’s definitely the kind of thing we want ML helping out with. The time it’s going to take a data labeling contractor to evaluate whether a model-written code review is good might be very high and they might not be able to do it at all. So in cases where the things people use models for outstrips any individual person’s ability to evaluate the model. One very salient challenge is when the models are very powerful at a large diversity of things then just evaluating whether or not they’re doing a good job is pretty non-trivial. That’s an area where you want to start building ML systems that help people evaluate the behavior of other ML systems.

**Ryan Lowe:** I agree with what Long said, the only thing I’d maybe add is speaking to the longer term alignment research; these systems optimize literally what you program them to optimize. So if they’re optimizing things that humans would rank highly when they’re doing their rankings, what you’re literally optimizing is producing outputs that sound good to humans. It’s possible that as models get more and more powerful it’s possible that as they optimize this they find interesting or tricky or deceptive (maybe that’s arguable) ways to generate outputs at a high score which actually aren’t the kinds of output that we want. I don’t think we’re quite there yet but at least it’s something we want to keep an eye on.

Thinking about ways to mitigate that, there are the kinds of approaches that Long talked about, which is that you have other AI models to help you in evaluating the outputs–that’s the scalable supervision style of research that I talked about. So people are working on more interpretability things like: can we try to understand what’s going on inside of a model? And that’s another vein of alignment research. Who knows when we’ll get there but that’s something to think about.

## You just hinted that there are people looking at stuff going on inside a model. Anything you can point to that’s external that you’ve seen recently that’s interesting in that space?

**Ryan Lowe: **I haven’t gone super deep into this literature, but from what I’ve seen and skimmed is some really interesting research from Anthropic on interpretability. They’re working on smaller scale transformers..trying to understand what’s happening inside them.

**Long Ouyang: **There’s some complimentary work on setting up the work that language models do in a way that’s more observable. Anthropic is interested in this idea, as are we, of supervising the process that language models do rather than the outcome. SO the idea here might be something like breaking down a big task into a bunch of small components, and you maybe have a better handle on some of the components than you do on the overall end to end training process.

## And is that part of the training or the fine tuning at the end?

**Long Ouyang: **I’ve seen this so far in people building programs. There’s a research group called Ought, which also builds what’s called a lit review assistant for academic papers. They’ve used this kind of technique for building their language model assisted lit review tool . So the examples I’ve seen so far are like that, but it’s interesting to think about how you’d decompose training.

## Is there anything you’d recommend checking out to learn further about this paper or your work more broadly?

**Ryan Lowe: **I think people are probably already doing this but if you haven’t already, playing around with these models and getting an intuition for what it can and can’t do. Noticing ways in which you’re trying to get it to do something and it’s not doing that thing. We’re doing alignment work but you can also think of the work that companies do aligning it for a very specific use case.

Maybe also developing a bit of curiosity thinking about what will happen if we have GPT7, and there have been people thinking about these longer term alignment questions. Our colleagues on the longer term alignment side wrote a paper about critiques, and training language models to critique which is kind of a step in the scalable alignment question.

**Long Ouyang:** I’d also recommend giving InstructGPT a try. It’s not that widely known that this is a public model that you can get some free credits to play with at beta.openai.com.

**Ryan Lowe: **Yeah,  it’s funny because the underlying GPT 3.5 has been available since much earlier last year and only once people have used it for free and it’s in the form of an assistant has it really taken off. But try out InstructGPT, in some ways it’s better and in some ways it’s worse than ChatGPT.
