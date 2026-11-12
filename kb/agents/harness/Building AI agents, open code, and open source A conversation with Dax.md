---
title: 'Building AI agents, open code, and open source: A conversation with Dax'
kind: blog
topic: agents
subtopic: harness
secondary_topics: []
summary: Interview with OpenCode/Zen creator Dax Raad on why terminal-native agent
  harnesses (vs browser-based LLM chat) won engineers over once Claude Code let models
  manipulate the filesystem directly, and why model-agnostic, open-source harness
  design matters as new models ship weekly.
triage: null
skip_reason: null
source: baseten
url: https://www.baseten.co/blog/building-ai-agents-open-code-and-open-source-a-conversation-with-dax
author: Madison Kanna
published: '2025-10-09'
fetched: '2026-11-12T06:10:36Z'
classifier: claude
taxonomy_rev: 2
words: 2760
content_sha256: 585c8031a2ce0e080f6620be6f7d0c05c3a81b552fe482f6f0b67dd5338fc296
---

# Building AI agents, open code, and open source: A conversation with Dax

Community
# Building AI agents, open code, and open source: A conversation with Dax

Dax Raad, creator of OpenCode and Zen, discusses the launch of Zen, the philosophy behind building in open source, and why terminal-based workflows matter.


- Authors
- Date
- October 9, 2025

TLDR

In this interview, Dax Raad, creator of OpenCode and Zen, we discuss why Dax built OpenCode, the launch of Zen, the philosophy behind building in open source and why benchmarks often mislead users about actual product quality.

**Dax:** We all started to use LLMs for our work. And it was always a very clunky experience. It was, I'm in my editor, I'm in the zone, I got all my key bindings. I'm really happy with how it works. I have a question, okay, I need to stop, switch over to my browser, type out my question, paste in some code, potentially submit, wait for the response, have a conversation. Then maybe I get some code that it spits out and I have to copy paste back into my editor. And this just felt really bad. I'm in  this loop that I'm gonna use constantly throughout the day, but it's not the right approach.

And I kept thinking, browsers can technically access your file system. So I was just waiting for one of these LLMs to let you say oh, you can just mount a folder, which is your project, and you can mention files in your project. It can write results back into your files and imagine it's all in the browser. And I just thought, okay, someone's gonna do this one day.

But then Claude Code came out where it ran in your terminal, alongside your editor. You can ask it stuff and it can just manipulate your file system directly. And it elegantly solved the problem I had, which was the LLM can't touch my files. And that was the first AI coding product that really clicked for me. I had the aha moment. And I started to use it. I tried a bunch of AI products in the past year, but that was the first one that stuck.

Then I started to think, there's other models out there that I want to try. Every week there's a new cool model that's claiming X, Y, Z things. Also we have Terminal, our coffee shop. So I had a deep understanding of how much you can do in the terminal. And we had another project that we were working on that also had some really advanced terminal functionality. 'm also a Neovim user, so I kind of understand what the ceiling of what you can do in the terminal is.

The scope that Claude Code defined makes a lot of sense. They're not trying to go crazy with terminal stuff. They just want something that's simple and works everywhere and friendly to the average person, but they're never gonna go and push the limits of what's possible in a terminal. And I felt myself wanting to do that. Claude Code's good, but again, there's certain things that I felt could be done better.

We started exploring this and thought, what if we built an open source version of Claude Code that was heavy on the terminal stuff. And also was really flexible for any model because that's where open source has an advantage.

**Dax:** Just because something's open source doesn't mean it's going to be any better than the closed source equivalent. It only happens when there's a long tail of things to cover. We need to cover all the different models and people playing with all different models. We need help improving how it all works. Then it kind of makes sense to be open source so the community can help with that. And we're obviously very good at bootstrapping the open source community overnight, so it felt like the right problem for us.

Claude Code, for example, is not open source. And I think that makes total sense because there's no problem that Claude Code has that a large open source effort would solve, right? Claude Code, it just works with Anthropic models, it's all tightly integrated. You don't really need help from the community too much. I'm sure they can fix bugs here and there, but the core reason for existing doesn't benefit from the open source stuff.

On our side we need to make sure our stuff works really well across all the models. And new models come out every day. I can't go and use every single model every day. I'm not gonna know the quirks between them. I never use Gemini. This is not something I use. We're never going to deliver a good Gemini experience because we don't use it personally.

But this is where the open source community can help because someone out there uses Gemini every single day and they're oh, Gemini makes these common mistakes when editing tool calls. Here's a fix for that. Or here's a bug with your API. We can fix that. So if you need large manpower for something you're doing, but you can't directly fund that effort, being open source helps quite a bit. And that's our core positioning. We are the open source option in this space.

**Dax:** I made so many jokes about this a while ago where I said, we just added a new word for no reason. But to be fair, I see the reason for the term.

When you're using an LLM and you're just prompting it and getting a response, that's one way of using it. When you're giving it a goal and giving it access to tools and it's just going to keep running until it achieves that goal, that's a kind of different way of using it, and that's what people categorize as an agent.

At the end of the day, it's just an LLM that has access to some tools. I can edit a file or I can read a file, or I can look up something on the internet. And it's going to think about what tool to call. It's gonna call tools, then it's gonna use that result as a new input. It's gonna think again, it's gonna call a tool, the result as a new input. It's gonna keep repeating that until it decides the task is complete. Or it doesn’t know how to solve this. And then you get the response back.

**Dax:** So if you think about how I described OpenCode, it’s very flexible, very configurable. You can use whatever model, you can hack it, you can customize it. There's so many ways to tweak it. When people hear that, they think, oh, they're the advanced user product. This is for people that really want to tinker. They're not the everyday user product. But these things aren't in conflict. We start with the primitives and then we build up to a good default experience.

The downside of being able to use any model is, oh, what model should I use? If you're the average person, you have no idea. You think, I hear this QwQ-32B thing is pretty interesting. Let me go figure out how to plug that in. Maybe you find OpenRouter, sign up for that. It gives you access to a hundred models. Seems useful, but then when you go to use it, the experience is really variable.

We didn't understand this right away because we were kind of particular, we were in the space so we knew where to find hostings for these models. But in our GitHub issues, every single day it would be somebody saying “the LLM is randomly stopping in the middle” or “I'm getting this random HTTP error” and issues like that.

And what we learned is these open source models that are coming out constantly are actually very, very good. But then when you go to use them, depending on the provider, they could be really bad. Especially for coding if you didn't deploy it in a high quality way, especially with all the tool calling stuff. So we just constantly kept seeing people complain, this isn't working, that isn't working. And they blame us because they're like, oh, this is an OpenCode problem. And I get it, it makes sense like you're trying to use this thing, it doesn't work. You go to the people that respond to GitHub issues.

We really liked what OpenRouter did. It's like a single thing. You sign up for a single API key and you get access to a bunch of different models. Whatever is new and cool, they get added there pretty quickly. But their approach was to give you as many providers as possible for any possible use case. We realized we don't need to have 50 providers backing QwQ-32B. We just need to have a few good deployments that we've tested, make sure they work well, that we have SLAs with, that we can talk to the team when something goes wrong, and ensure that we're really high quality deployment for it. And it's also something that we use ourselves, so we know that it's good. It’s good enough for us.

That's what OpenCode Zen is. It gives you access to some of the brand name models like Claude and GPT, but also the latest open source models deployed in the best possible way. And it works with OpenCode, but it works with anything else as well. So you can plug it into other tools too. We don't care if you don't use it with OpenCode.

This isn't a for-profit thing. This is something we try to do at breakeven. So what's nice about this is we can pool resources. Every new person that starts to use Zen, we're pooling all of our volume together and we're going to providers and negotiating discounted rates, given that we have larger volume. And when we do that, the cost savings flow right back down to everyone. If everyone just used this, everyone could just have access to the cheapest possible rates that exist out there right now.

**Dax:** I've always been a big believer in anecdotes over data. So I will personally use these as my daily driver for a day or two and just get a feel for how it feels. I think that's a number one signal. I can pretty much always tell, not with deep granularity, but from a binary sense:is this good or bad? That's what I usually do first.

And then there's this guy on X, [GosuCoder](https://x.com/GosuCoder). He has a set of evals that he runs. They're private, they're not public because he doesn't want people optimizing for them. But he has shared with me his approach, and it's actually the exact same approach that I would take, but he's just done a really fantastic job with it and gone way deeper than I ever would.

We deployed a bunch of stuff ourselves and had him run benchmarks we could see quantitatively here's the ceiling on where it could be. Then we went to providers, Baseten and then some other people to see if they can get close to that. And some of them were able to, and that's what we're using.

**Dax:** if you ever see a company, any AI coding product, if they launch a product or launch a new announcement and they say, hey, we're number one on this benchmark, you know they're bullshit because it's always a benchmark you've never heard of. And they just found the thing that they could be number one on. So anytime you see someone say, hey, we're number one on a benchmark, it should be a red flag.

When you go look into the benchmarks, 90% of them do not look like anything in the real world. A lot of the coding benchmarks are, hey, given this maze, write a program to get yourself outta the maze. That's cool, but none of my work day-to-day involves escaping a maze. It does not look real world stuff.

GosuCoder's benchmarks are more real world code bases, actual feature building in them, stuff that you would really do. And he has a scoring process that sits on top of it. So I don't like most benchmarks 'cause the reality is that they're built by AI researchers and AI researchers don't know what day-to-day work looks like. And they focus on very academic problems like programming puzzles. So most benchmarks are useless.

The other thing is, I think it's also a stupid game to play because if you can only notice your LLM or product is better on a benchmark, that means the end user can't tell. They can't tell when they're using your thing versus the other thing. Because the difference only shows up on the benchmark.

People always ask us to optimize for certain things, but I don't think the user's gonna be able to tell 'cause these things are so non-deterministic. People are using them in all different kinds of code bases, all different kind of environments. People really can't tell whether OpenCode is better than Claude Code or whether Cursor is better than Claude Code or whatever. Every week there's something new. “This is better than that, this is better than the better.” But people really can't tell.

So perhaps you won the benchmark game, but nobody can tell the difference. The things that the end user can notice aren't these crazy advanced AI, like math genius optimizations. It's just really basic stuff. Is it a good product experience? You know, does it feel responsive? If I'm trying to do something, is it easy to do? Those people see that and feel that and they tend to articulate it as, oh, the AI is better, but it's really not. The AI is not better. It's just the experience around it is better. That's what people can notice. They can't really tell that, you know, the incremental. And it's incrementally smarter on this benchmark.

**Dax:** Have you heard of that superstitious pigeon experiment? So there's this psychologist. He had this experiment where he had a bunch of pigeons and on totally random intervals, he would give them food. Right. Completely randomly. The pigeons started developing superstitious behavior because at some point they would notice that, oh, the food came when I walked this way, or when I did this head movement. They developed superstitions, they would start doing a certain thing thinking it was causing the food to show up.

And it's this funny, even a pigeon can develop superstition. I'm seeing this so much with LLMs because LLMs are not like anything else in tech. They behave randomly and it's really hard to predict how they're gonna work. They'll be great one day on a certain task and be horrible the next day. They're effectively random, but people are developing superstitious behavior around this.

And it's funny because I build these things so I know how they work under the hood and I'll see people say stuff that I know is impossible. They'll say, wow, OpenCode is so much better than Claude Code in these situations and it works like this and Claude Code works like that. They're not understanding that under the hood we reverse engineered Claude Code and re-implemented almost the exact same logic. There's some differences. But it's almost the exact same thing, but people are perceiving all these differences and they're getting really intellectual about it–a pigeon is gonna be stupid about superstitions. A human's going to be really smart about their superstitions and believe that, and build it up into this really complex and intellectual thing.

Every week there’s a new trend. For example, “Cursor is so much better than Claude now.” But it’s just based on superstition. The level of superstition that's happening in tech right now is, it's at this crazy level.

I think in tech, almost everything we do has been very deterministic and not random or complex like this. So I think our industry is being exposed to this for the first time. And we all think we're so much better and so much more rational than the rest of the world. And we're not. We're now exposed to this stuff and we are literally operating the same way that people who are into astrology feel. And it's all the same stuff. It's all just human nature. Smart engineers are basically doing astrology when you have opinions on these models or these tools.
