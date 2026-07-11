---
title: ⚡️Multi-Turn RL for Multi-Hour Agents — with Will Brown, Prime Intellect
topic: models
subtopic: fine-tuning
secondary_topics:
- agents/planning
summary: Prime Intellect interview on multi-turn RL for multi-hour agents and training
  long-horizon agent behavior.
source: latent-space
url: https://www.latent.space/p/willccbb
author: Latent Space
published: '2025-05-23'
fetched: '2026-07-11T05:17:51Z'
classifier: codex
taxonomy_rev: 1
words: 8575
content_sha256: 1285041a77a77fbcc457c4fdb4b74814ccb76057f72c9e53d199058d96dbb685
---

# ⚡️Multi-Turn RL for Multi-Hour Agents — with Will Brown, Prime Intellect

# ⚡️Multi-Turn RL for Multi-Hour Agents — with Will Brown, Prime Intellect

[The World’s Fair](https://ai.engineer/) is now TEN days away! Today’s guest Will was [one of the most popular speakers](https://www.youtube.com/watch?v=JIsgyk0Paic&t=54s&pp=ygUSd2lsbCBicm93biB5b3V0dWJl) of AIE NYC, and is coming back for the new RL+Reasoning track with [Misha Laskin](https://www.youtube.com/watch?v=DIu7xA898go&t=2s), [Nathan Lambert](https://www.youtube.com/watch?v=skT89EvIjrc&t=16s), [Christian Szegedy](https://www.latent.space/p/iclr-2024-recap), [Greg Kamradt](https://www.youtube.com/watch?v=SKBG1sqdyIU), [Kyle Corbitt](https://www.youtube.com/watch?v=zM9RYqCcioM) and more. [Join the top AI Engineer gathering of the year](https://ti.to/software-3/ai-engineer-worlds-fair-2025/discount/LS30)! If you want JUST the hallway track, Expo tickets are now on sale - with [~30 of the Explorer discounts left](https://ti.to/software-3/ai-engineer-worlds-fair-2025/discount/HNEXPO).

In an otherwise heavy week packed with [Microsoft Build](https://news.smol.ai/issues/25-05-19-not-much), [Google I/O](https://news.smol.ai/issues/25-05-20-google-io), and [OpenAI io](https://news.smol.ai/issues/25-05-21-openai-io), the worst kept secret in biglab land was the launch of Claude 4, particularly the triumphant return of Opus, which many had been clamoring for. We will leave the specific Claude 4 recap to [AINews](https://news.smol.ai/), however we think that both Gemini’s progress on [Deep Think](https://x.com/GoogleDeepMind/status/1924881598102839373) this week and Claude 4 represent the next frontier of progress on inference time compute/reasoning (at last until GPT5 ships this summer).

Will Brown’s [talk at AIE NYC](https://www.youtube.com/watch?v=JIsgyk0Paic&t=54s&pp=ygUSd2lsbCBicm93biB5b3V0dWJl) and open source work on [verifiers](https://github.com/willccbb/verifiers) have made him one of the most prominent voices able to publicly discuss (aka without the vaguepoasting LoRA they put on you when you join a biglab) the current state of the art in reasoning models and where current SOTA research directions lead. We discussed his latest paper on [Reinforcing Multi-Turn Reasoning in LLM Agents via Turn-Level Credit Assignment](https://x.com/willccbb/status/1925389814926647334?s=46) and he has previewed his AIEWF talk on [Agentic RL](https://www.youtube.com/watch?v=Xkwok_XXQgw&t=2s) for those with the temerity to power thru bad meetup audio.

## Full Episode

is on [YouTube](https://youtu.be/furFAnmbam0)!

## Timestamps

- 00:00 Introduction to the Podcast and Guests
- 01:00 Discussion on Claude 4 and AI Models
- 03:07 Extended Thinking and Tool Use in AI
- 06:47 Technical Highlights and Model Trustworthiness
- 10:31 Thinking Budgets and Their Implications
- 13:38 Controversy Surrounding Opus and AI Ethics
- 18:49 Reflections on AI Tools and Their Limitations
- 21:58 The Chaos of Predictive Systems
- 22:56 Marketing and Safety in AI Models
- 24:30 Evaluating AI Companies and Their Strategies
- 25:53 The Role of Academia in AI Evaluations
- 27:43 Teaching Taste in Research
- 28:41 Making Educated Bets in AI Research
- 30:12 Recent Developments in Multi-Turn Tool Use
- 32:50 Incentivizing Tool Use in AI Models
- 34:45 The Future of Reward Models in AI
- 39:10 Exploring Flexible Reward Systems

## Transcript

Alessio (00:01.136)

Hey everyone, welcome to a Lightning plus Emergency News, Late in Space podcast episode. I'm Alessio, partner and CTO at Decibel and joined by my co-host Wix, founder of Small AI.

Swyx (00:05.95)

Ha ha.

Swyx (00:12.776)

Hey, hey. And yeah, honestly, we knew that Cloud 4 was coming. And we just didn't. We're just too busy to have a dedicated episode. So this is our makeup dedicated episode with a special guest, Brown from now I can say it, Prime Intellect.

Will Brown (00:29.518)

Hey, how's it going? Great to be on and Circus and I have known each other for a little bit and this is my first time on the podcast, I believe. Great to chat with you guys. Big news day, I guess. So lots of stuff out in the world. There's always a news day.

Swyx (00:47.988)

I think this week is particularly heavy for some weird reason. Like, Monday was Microsoft Build, Tuesday, Wednesday, Google, and today is Claude. I wonder what tomorrow will bring.

Will Brown (00:56.322)

Yeah, we had IO and then had IO and then the two.

Swyx (01:00.16)

Yeah, different IOs, exactly. Yeah, so we actually were supposed to record this morning, and we all wanted to watch the Cloud Keynote, so we went and watched the Cloud Keynote. Obviously, a good model, big model. They're really emphasizing coding. They didn't really talk much about reasoning, to be super honest. They were just like, it runs for longer now. What are you guys' takes?

Will Brown (01:29.326)

Yeah, so mean, like one thing I've kind of been seeing coming for a little bit that I think people are kind of also all aware of now is that like, the thing that's going to make the next wave of stuff be powerful is just like everyone wants better agents. Everyone wants models that can like go off and do stuff. And like reasoning was kind of like a precursor to that a little bit. Like, I mean, I always think of like open eyes, like five levels framework, where like chat bots was like the RLHF era.

And then Reasoners was like the O1 and R1. But like really what people were thinking of was Reasoners are a step on the path towards agents. And so I can kind of see why Cloud, why Anthopiq is not like, we have the best Reasoner. They're really like showing off their suite agent and like tool use and like function calling benchmarks, multi-turn stuff. Because I think that's really like what people care about more for actual applications as opposed to like...

did really good on this math competition. Like the math competition was like, that stuff was all like a signal that was supposed to think we were getting somewhere. But the thing we were getting towards for a lot of people at least is practical agents.

Swyx (02:40.871)

Alas you

Alessio (02:41.178)

Yeah, I think the extended thinking mode, I think they removed the uppercase. I think in the Cloud 3 release, was like extended thinking, kind of like capitalize and not just like extended thinking with tool use. So I think they're also, yeah, downplaying whether or not it's reasoning or not. I think they're trying to merge everything together. And it's not, I mean, I didn't realize that, but extended thinking could not.

used tools before, the way they worded it, and now they can in Oppos 4, so that's great. But yeah, they haven't put it as far center as last time.

Swyx (03:18.483)

Do we have any, this is already veering off from Claude directly into speculation, but do we have any idea if there are any material differences between how Claude extended thinking works versus the old series models? Do we know?

Will Brown (03:35.758)

The biggest difference seems to be, and this is kind of a thing that's been, I mean, this is all speculation, of course, but from the start, Anthrop had always kind of had this little thinking thing where you could, sometimes even like Cloud 3.5 would do like a tiny bit of thinking. And it was really just like deciding which tool to use for the most part. Like if it was doing an artifact in the Cloud UI, it would have this little thing.

where it would think for like two sentences about which tool to use. And it seemed like Anthropix kind of attitude has been that extended thinking is an instance of tool use. And that it's the kind of thing you want to equip the model with the ability to do, but it's not like, it's a thinking model. It's just a sink for the model to like brain vomit because that brain vomiting will help it like find a nice thing to do next.

In the same way that doing search or doing code execution are like ways to kind of get more information on the path towards like finishing a problem.

Swyx (04:42.929)

Yeah, inference time compute, as they say. I did meet somebody who claimed to have coined to define the scratch pad paper. And this was obviously before the Jason Wei chain of thought paper. But it's all the same sort of method, general family of techniques.

Will Brown (04:51.105)

No.

Swyx (04:56.979)

I think the question for me is also like, is there some model routing going on? Like are they different models, the thinking, non-thinking? Or are they the same models with like, just like you turn off the end of turn token generation. that's it.

Will Brown (05:13.165)

I think these models should be the same model and AnthropicNet is what they're doing well. Like it's not that hard to like, Quinn did it in a very kind of like simple way and they kind of talked about how they did it a little bit. But it's not like too difficult to like have whether or not a model thinks like be the sort of thing. I mean, like obviously all of this stuff is like hard at like serious scale, but like conceptually at least it's not like a big

problem to solve about how would you ever do it. It's like, no, we have reinforcement learning, can kind of like, or we just SFT on like different things, can kind of teach models skills like that pretty directly.

Swyx (05:54.674)

Yeah. You have some work that you've published recently on GRPO and relationship for doing a lot of work on multi-turn RL. I think I wanted to just kind of round out any other Claude highlights that you guys saw. There is controversy that I'm leaving towards the end. But any other technical highlights that you guys want to focus on?

Will Brown (06:09.975)

Sure, sure, yeah.

Will Brown (06:14.219)

Right, right. Okay, yeah.

I mean, I think it seems like a really cool model. But I think like a Calamity's like tweeted this earlier today. It seems like it's linear progress, which is like great. But it doesn't feel like there's not anything that I've seen from it. That feels like a paradigm shift in terms of like, the sorts of stuff Daria talks about, which like I think maybe we're still on the path to get there. And it feels like this is just like, keep going up.

in terms of complexity of agents. think the one thing that to me was really nice to see, I haven't like done too much testing myself yet. But in their reported benchmarks, the reward hacking issues to like, sonnet three seven loves to like do stuff that to me feels reward hacky in the sense of like, it'll try to, you ask it a coding question, and it would like, do your question, and then seven other things also. Presumably because

there was some RL environment where there wasn't really a penalty for doing that or there was an enough penalty and covering its bases like was more likely to pass test cases on some coding thing. Like you could imagine like a sweet bench kind of thing where there's a minimal diff that is really what you want, but there's like you could do a ton of other stuff and put all these other things in place that as long as you don't, as long as it's not enough that you trip over your feet, it's just like extra stuff that's there if it helps pass the test cases.

And what I really think you want to do with these models is like kind of min-max. Like you want the models to like do the thing and no more. And they had some internal benchmark for this that went from like 45 % down to 15 % for both for Sonnet and for Opus as opposed to 3.7. And so I'm hopeful that these models are much more like friendly to code with and maybe more like trustworthy. Like that's the thing that I kind of...

Will Brown (08:14.007)

have buckets for models of like how much can I trust them in a code base? Especially something beyond like a single file like old Gemini to me was very trustworthy. GPT 4.1 is very trustworthy. New Gemini is not, 3-Sonic is not, 03 is not. I haven't decided which bucket new, new sign-up, new outputs are gonna fall into.

Swyx (08:35.453)

trustworthy in terms of reward hacking.

Will Brown (08:38.381)

Just like not gonna make them like the they're gonna do the right thing in the code base and like worst case they'll do it like dumb but they're not gonna like go break a bunch of stuff. They're not gonna leave a bunch of like extraneous comments and helper functions all over the place that aren't really needed or like make seven new files just to have them there. Like this is the sort of thing that 3.7 does a lot. Yeah.

Swyx (09:00.401)

Yeah, way too eager. Yeah, it was like I already have the function of my code base. I would just make a new one just because it felt like it. Yeah, one thing I often wonder about those things is like, just for RL environments in general, why is a token cost more of a thing in the penalties? That's the one rule above all.

Like you can actually skip a lot of reward hacking by just, hey, the more tokens you use, the worse it is.

Will Brown (09:31.502)

I mean, that's not what the model, they're selling you tokens. They want you to use more tokens. But like, so like there's that element of it. But I think also it's that there was this initial kind of reaction of everybody of like, more tokens is better. If you look at the line, it goes up as you spend more tokens, your accuracy goes up. And so I think the pressure to like really tamp down on token usage was not that serious for a lot of people, especially because the companies are like,

Swyx (09:34.139)

This okay.

Will Brown (10:01.617)

to sell you more tokens. it is the sort of thing that you can have some more controls over. like, when did this in kind of like a very kind of abrupt way, where they can like you can in the UI, can like set a token budget and just like truncates the thought. it seems like artificially truncating the thought is actually like fine. Like the model can even if like it got cut off mid sentence with an injected like think token.

these are smart enough models that they can kind of finish with the best that they got from that point. And so that's like one way to do it. The other and like that's becoming a kind of standard API feature now is like your think budget. Claude has that. Yeah, we did a little bit of experimentation with that in our last Interlock2 run at Prime Intellect, which it was before I joined. But thinking budgets are the kinds of things that you can insert into a reinforcement learning objective. And

Swyx (10:34.449)

Compensate, yep.

Will Brown (11:00.575)

You can see the model get better at targeting the right amount of thinking based on, let's say something goes in your system prompt. You can have the prompt just say, use X amount of tokens. doesn't need to be like, but if you've trained the model to respect this, would hope that if you execute this correctly, the model learns to roughly think the right amount.

Swyx (11:24.325)

Okay, this actually changed my opinion of thinking budgets because previously I was thinking that reasoning effort was better than thinking budgets. Thinking budgets is of like a max cutoff. It's a target, right? It's not, it's not a, like it's a, right, right, right. Yeah, because I actually want to set effort. I don't super care about cutoff apart from the cost and like giving me, you know, 64 bits of cutoff or whatever doesn't matter.

Will Brown (11:34.037)

the same thing. think. Right. So the effort is a target probably. Yeah.

Will Brown (11:53.708)

I'm not sure that they're like that different. think like we don't know how they do it under the hood. But my guess is that the whole reasoning effort thing is essentially a token budget that the model has been like RL to like, you would hope that you get different behavior. So the model when it's told it has a short thinking budget, you would hope that uses slightly different strategies that are better versus it has a high budget. It's more willing to like do lots of math calculations, for example. But I think conceptually,

It's really just about the model has some amount of room that can think for in tokens and it's trying to do that well, hopefully.

Swyx (12:29.479)

Yeah.

Alessio (12:30.224)

Do you think we're gonna have these as hyperparameters for like much longer or do you think this is kind of like, know, as we're early in this like recently models, more of the stuff is exposed and then it gets moved away from the user?

Will Brown (12:44.705)

I think in chat interfaces, it probably won't stick around. Like I don't think we're always going to have the drop down of like oath for many and for many high that feels silly. I do think it's a thing that developers want, especially because once you've kind of built around a certain model, like a lot of these writers are hoping you stick with the one model and are not switching all the time. You do need a knob to control costs and also latency. And so that is one kind of useful knob to expose developers.

for controlling this quality versus cost and latency.

Swyx (13:24.443)

Awesome. Cool on all of that. I think the elephant in the room, let's talk about it, is this controversy around opus or opus, right? Snitching on you.

Will Brown (13:38.303)

Mm-hmm. Yeah, I mean, so I have lot of opinions, but I think...

Swyx (13:42.961)

So for those out of the loop, let's recap because I feel like you're closer to this than I am. Like I learned about it from you.

Will Brown (13:49.102)

Sure, sure, yeah. this was someone from Anthropoc, I'm not gonna name him, because I know he doesn't wanna have all this attention on him, he deleted the tweet. But it was essentially like going through different things that people found during safety stress testing of Clod. And so this is not like, what's Clod gonna do for you? I think people took this out of context pretty badly. And so there's a fair point there that it's like, people are really reading into the one sentence much more than they should.

Swyx (13:57.522)

Of course you did.

Will Brown (14:19.201)

But this is thing Anthropic does a lot is they really stress test their models. They try to put their models in situations where they can really see like what could an adversary get them all to do or what does the model do if it's in a situation where there's no right answer. like, I think a lot of the kind of headline Anthropic like safety results, especially related to reward hacking and kind of deviation and alignment faking are all things to me that seem like a rock and a hard place situation where

the model has two objectives it's given that are conflicting with each other and it has to pick one. And no matter which one it picks, it's going to sound terrible. Like it's either following the user's instructions or it's following like common norms. And once you kind of accept either of those, it's going to do the thing that is aligned with that set of like guidelines. So in the case of like, if your model's goal is to be like maxing helpful to the user,

then it would help a user like build a bomb. If a model's goal is to be maximally helpful to society and a user's asking you to build a bomb, it's gonna be like, no, that's bad. I have to do something to stop this. Like you kind of have to pick a goal. And like maybe the right answer is the model just differs and it's like, no, I'm gonna stop talking. But people also get mad when you tell them like that the model will stop talking to you or like refuse to do anything. Like there's just no, it's, there's no, it's.

no way to kind of win and make everybody happy. But I do think like, like they report this because they think it's important to have people understand the safety implications of these models and to understand like, okay, how bad would it be if someone was trying to use this? Could this like meaningfully help someone commit crime or violence or whatever? And so like that's what they have like their state safety framework for. And the things that happen in these like,

blog posts and threads and papers about like the model trying these things, they're kind of putting these models in a scenario that elicits these things. Like it's the sort of thing that you would imagine a very smart human might also do in those situations. Like let's say you are told like accomplish some vague under specified goal at any cost. And you really like want to solve that goal. Think like game shows like survivor, I think is a good example of like

Will Brown (16:43.029)

or Lord of the Flies, any of these kind of canonical situations of people who are put in a weird spot and have to go do stuff and figure it out how to do it. They're kind of crafting these environments for the models and just looking at it and seeing what happens. And so I think it is a little silly to overanalyze behaviors in either direction of like, the model is reporting you to the police or the model is going to go help you find uranium on the dark web. Well, these models can kind of do, there's no, like they're

The base model in general of LLM is not artificially constrained in any way. Like with the right prompt it will do whatever up to its intelligence limit. And so like the question is just how do you constrain the space from all possibilities down to like a more reasonable set and like that's hard. So.

Swyx (17:32.347)

Okay, you actually gave a serious answer, which I totally respect. I was more looking for shitposts. you're treating this as though, like, yep, this is what the problem actually is, which is totally fine. And yeah, I mean, that's what you are as a researcher, right?

Will Brown (17:35.693)

I mean...

Will Brown (17:50.86)

Yeah, I mean, I think tweeting is fun. Like it's it's cathartic to like just kind of like get a post out. So like, when I saw the one about the uranium thing, I was like, let me tweet it. So the tweet was like, we found that quad can go search the dark web to look for like uranium. And I was like, here are the top 10 things that builders are using in their agentic rag applications with the new groundbreaking quad for

And it was just like, silly, both making fun of like, LinkedIn, like, thread posters as well as just like the funniness of the scenario that they were talking about.

Swyx (18:24.721)

Hehehehe

Swyx (18:29.587)

Yeah, this is it.

Alessio (18:30.128)

Does any of this make you think differently about what tools to give an LLM? I know they deleted the tweet, but it's basically like, before if you're putting all these MCPs, like, yeah, you have email access and all of this. now it's like, well, maybe I don't want to give email access all the time if you're going to snitch on me with the email access.

Will Brown (18:31.932)

Hahaha

Will Brown (18:37.761)

Hmm.

Will Brown (18:49.353)

Yeah, I mean, I think coding with these models, especially like quad, I did a fair amount, like for a few weeks, I was doing a lot of quad code with three seven, mostly for kind of random side projects. I never really got to the point where I found it was helpful for a thing that was like a large existing code base. but if it's like, Hey, I want to like cook something up in a few hours for fun. Pretty good at that. But these become messy and they become hard to maintain. And you get to a point where it's like,

nothing is working, I just gotta like dig in and fix it all myself. And so I think part of that is that the models have access to like a terminal and you can do a lot of stuff in a terminal. MCP is kind of a way of constraining the action space. like in like canonical RL, people talk about like states, actions rewards, policies as like the things that are like the moving parts. And

models generally are trained in like old school rl but like a very fixed action space of like what are the keys on the video game i can hit but with that alone it's like text text is like kind of unbounded and what you can do with it in a terminal there's not much you can't do in a terminal and so if you're training models i got a lot of flack for this one people were it was both people who were like

Swyx (20:09.191)

I'm just showing this. Wait, Flack? Why?

Will Brown (20:14.795)

the notation is stupid and bad, but RL is really simple or like RL is like complicated and it's like everyone has a different opinion on what RL means. And I was trying to just like, be like, hey, it's actually kind of complicated. And I wasn't picking this up like, the definition of the NMDP is complicated. I was like, no, there's just like a lot of moving parts. And to think about it, to like do anything, especially if you to change any like part of the system, like here's a question, hypothetical, like

What happens if you have two LLMs learning together? How do you reason about that? How do you like think about that? Is this going to be a stable system or not stable system? What if they're like kind of cooperative, but kind of not cooperative? And then they're training to work together, but also want to backstab each other. Like this is kind of the environment people are finding themselves all in all the time out in the real world. But if you want to make AI's do this, have to like translate this into code and math. And the more complex your

goals are with this thing, the more complex the math gets. like, RL is like one math language that kind of exposes these primitives. But like, I think a lot of people are like, oh, I can follow the equations. That means I understand it. And it's like, well, sure. But like, also, there's, it's like this, I don't know, end body problem thing, where you can freeze it and look at it. It's like, oh, how does one thing moving affect everything else? And what are the cascading ripple effects? And like,

Swyx (21:41.415)

Wow, you just brought three body problem into this. Amazing.

Will Brown (21:45.421)

Like, in like the physics version, not the show. Yeah, yeah, yeah.

Swyx (21:48.786)

Yeah, yeah, No, no, mean, yeah, that actually, actually very impossible to model. Like, I guess you can like simulate it, but like even then, yeah.

Will Brown (21:54.378)

Mm-hmm.

Will Brown (21:58.85)

But it's chaotic. It's like it's sensitive to initial conditions. So like you can't really say like this is one of those things that like like why does no one predict the weather a year out? There's no I don't think anyone has anything that's like good at long term weather forecasting. I'm beyond like I don't know climate trends, but no one can predict whether it's going to rain in Seattle on a given day in a year. Even if you think like like the system's predetermined, like we did. It's all clouds bumping off each other and whatnot. Mountain ranges. We kind of know how these things work.

Swyx (22:09.095)

Mm-hmm.

Swyx (22:14.195)

climate.

Swyx (22:25.363)

So the butterflies are flapping their wings. mean, you got to let it play out. If we had no butterflies, we could predict it. Interesting. OK, so I guess we can sort of round it out, unless there's any more of the controversy. I think there is. I think that the system card is actually very good. They probably went too hard on it.

Will Brown (22:29.431)

But exactly, yeah.

And so, RL is very sensitive to butterflies.

Swyx (22:54.451)

compared to like normal system cards. And it's a little bit confusing whether this is marketing or are they just like, no, we really super care about safety. And part of this is like Apollo just being Apollo, pushing the frontier of red teaming, right? So they're going to report the things because it's extremely good at Apollo marketing. Yeah.

Will Brown (23:13.005)

Right. Yeah.

I think they're really there seem to still be like trying to be creative with their kind of consumer marketing. Like it feels like people in the world like love quad or have ground type of quad, but still had a phase where they were using it a ton. But it hasn't really broken out to general people in the way. And it feels like a lot of their marketing that I've seen is like a little confusing. Like it feels like they've done a really good job at crafting a brand image that appeals to a segment of the population.

who has certain considerations that they really like that a model has a deep personality or whatever. The sorts of people who I think also really like GBT 4.5, many of them really loved Claude III Opus, the big model smell. But a lot of people just don't care. And I think Anthropec is trying to figure out how to...

Swyx (24:12.763)

Yeah, just wanted to use it as a tool.

Will Brown (24:18.177)

like appeal to that audience. The LMSys, Sycophanty, Roporo, the people who love those models, different crowd. And it's a larger crowd. And that's a tough problem to solve as a company.

Swyx (24:30.171)

It is. What's your quick take on Ella Marina getting $100 million?

Will Brown (24:37.313)

We'll see. Like I imagine that they partner with company labs in different capacities to.

Swyx (24:45.405)

Probably making a lot of money, yeah.

Will Brown (24:47.725)

Like I'm not, I'm not in the business of trying to point the finger at like saying they definitely did this, but if I was a company that was able to raise it, that kind of valuation, and I had just had a long public partnership with Metta or eventually public partnership for a thing, which we've kind of seen was Metta had the ability to do a lot more back and forth than a lot of other labs did. I would imagine that there's some compensation going on there or access to data. And so like,

I think being an eval company puts you in a really hard spot. Some people are talking about this on Twitter, like just that to be an eval company, you kind of have to sell to the labs, but selling to the labs doesn't really like kind of wrecks to reviles. And so it's like this dog chasing its tail.

Swyx (25:26.973)

Mm-hmm.

Swyx (25:32.529)

Because your incentives are like your customer. Yeah, yeah, So in finance, would, mean, you you are from Moenstany. So this is the credit rating agencies. Like literally your customer is the one that you're supposed to govern, but they're also your customers. So then you have to be like nice to them or they'll just go to the next one.

Will Brown (25:39.469)

Yeah. Yeah. Exactly. Yeah.

Will Brown (25:53.26)

Yeah, I mean, I do think that like the best source of evals going forward is probably going to be academia. And so this is the thing that I tell people who are like starting a PhD, which is like find things that are like cheap to work on as a PhD student. Because you cannot go pre train a foundation model really on your own, but you can build a really good, really clever eval. And like we're

churning through evals at the time, we saturate them, we always need more. It's not the kind of thing that is ever going to end. And so that's the task of translating vibes of what is good or bad about a model into very precise scientific questions, I think is an important problem. It's a problem that you can get by a lot more with brain power rather than dumping capital into it.

You need to like pay for the API costs, like that is generally the kind of thing that either you can get covered within academic grants or like industry sponsors or the kind of thing that just like there's versions of these things that are like small sample size that get you on get on the radar or you kind of pick and choose which models you can afford to email. But it's like an accessible field of research. And it's one that like the incentives of academia I think are quite good for, which is like write a splashy paper.

that says something interesting about the broader field rather than, we want to make this one look like the winner.

Swyx (27:25.179)

Yeah, I think a lot of grad students still don't have taste. I don't know how better to put it. just, you go to enough academic conferences and I'm like, why did you work on this, man? Like, you're so smart. You're capable of better. So how do you teach taste?

Will Brown (27:31.735)

That's fair, yeah.

Yeah.

Yeah.

I think, I mean, I can tell how I did it originally, which is like, I think you always want to be thinking pretty far ahead and you want to be like making kind of educated bets about what the world looks like in the state in the few years. like, you have to say like, what are the questions that no one's even talking about? And this is like not an easy thing to do. You have to like really convince yourself that you're kind of right about the way things at least might go.

Like when I was like in, I finished up undergrad, late, like they finished in 2019 then went right into grad school. Um, but like towards the end of the 2010s, like we had like, I'll go to deep mind, uh, doing all this multi-agent RL stuff that was like really cool. Um, then it was like, okay, this stuff kind of works like AI is like going somewhere. Multi-agent systems are kind of going somewhere still very early stages, but what's going to happen once this gets there.

Will Brown (28:41.533)

And it seemed like, okay, these things are all going to be like continually learning in parallel as this big multiplayer game, basically. And if you look at the math, the math was kind of like undercooked and there's like some really hard open questions that are still open questions in multi-agent learning theory. And so like that was my focus. was, which was like, how do I like learn about this? How do I learn to think about this stuff better? And at some point I kind of got tired of proving theorems and was like, okay, let's just go build the thing. But I think like,

You want to think about like, whether you're doing theory or experiments, like you have to lay out a few different conditional statements to get to the point where you really doing interesting research that's beyond like, just loathing through that people are like, obviously going to be working on in parallel. You want to be jumping ahead of the curve a little bit. Um, I think my last, I don't know, this isn't like, I wasn't the first person to do this, but like, it was pretty clear to me.

like after O1 and before R1 that like RL was going to work and that that was going to intersect with agents where the solution was going to be like RL Batilius. That seemed like the direction things were going to go. And so that was like, I don't think that was a very risky research bet, but it was like a research bet that seemed to work out.

Swyx (30:12.071)

Yeah, speaking of which, you just published the paper. Now I have the full context as you were an advisor on this, and one of your grad students was doing the work, something like that.

Will Brown (30:15.169)

Yes.

Will Brown (30:22.495)

Yeah, so was me with Sillyong was my intern. This was kind of the last major thing I was working on at Morgan Stanley. And this kind of was in parallel with the verifiers as the repo that I've been building out major updates that coming very soon, by the way, I'm very excited about some stuff. But it kind of was something I really started in earnest, like January, kind of in the follow up to I'd had the GRPO demo thing go viral.

And was like, wait, there's something to this format reward thing. like, this is like a proper repo. the other one. Yeah, yeah, the other one was like just a gist. This one is like a repo for like multi-turn tool use. RL, with GRPO. And so like, in some ways the paper is like, it's the first paper that's really like, actually there's been a couple of papers that people have used the repo for.

Swyx (30:54.675)

It was literally like a GitHub gist, right? Or something.

No, no, the GRPO. Yeah.

Will Brown (31:21.559)

but it's one where a lot of the stuff from the original GRP demo gist gets kind of extended to the multi-turn RL tool use setting. And so there's a lot of experiments here about like, okay, how do you actually get models to use tools? How do you incentivize tool use? Because something we'd see is that if you set these models up to use tools, they just won't. Like if you say, hey, here's a question, you have access to these tools, do as many rounds of tool calling as you want, and then submit your answer, they'll just submit their answer.

because they like are, especially for like small models, like they aren't already trained to use tools. They don't really want to because they don't necessarily have that instinct and they're pretty bad at like function calling and format instruction following. And so what you would see is like when they use a tool, they would like mess up the JSON and then they'd be like, that didn't work. And it threw me, it got me out of focus and it would be more likely following that that the model would just like go off the rails.

because they would get like an error message from the parser. And so the safe option for the models is just to like stay in this basin of like, just do think then respond. Same with like normal formatting awards too. Like if you want models to use thinking tokens, you kind of have to like incentivize that. You have to either do a little bit of like SFT warmup or you have to like reward them for doing it. Otherwise they will not follow it 100 % of the time on format alone versus like

a model like R1, like 100 % of the time, it is going to use its think tokens. You are not going to ever see R1 just like talk normally without the thinking section. And so like, you kind of do have to decide what you want the model to do. Like, this is a little bit like a user facing question of like, what, what behavior of the model should the default be? And if you have, if you want it to do a certain thing, if you want it to be a tool use agent model,

Like it does help considerably to like actually have this incorporated into the reward. The kind of key trick in the paper to get around this problem. So, okay, one kind of reward hack these models would do is like, they would do like a dummy tool call where they would like learn to ask this, use the same Google search every time and ignore it. like the, questions would be like, okay, here's some like MMLU style question, go figure out the answer.

Will Brown (33:47.734)

use web search and if you start rewarding them for like tool use, they will use the tool, but they don't really want to like have to, they want to like be very safe with it. And all of these questions, like they do kind of know a lot of the answers already. And I think calibrating the right difficulty of your questions for RL is like an important problem that we're still kind of figuring out. but they would like do silly versions of tool use where they aren't actually using the tool to assist in their reasoning.

they're using it to get the reward. And so we kind of have to do a credit assignment thing of like, okay, did the tool result in information? And so for these experiments we were doing, the trick was like, okay, does the like some string matching thing involving the ground truth answer and the return search results from Wikipedia. So did the model actually start to thing that retrieved useful information for the question? And so this is like, but the framework is more general than just that it's that

I'm once you have a new a way to do intermediate evaluation if you can evaluate like the quality of an inter-other mid-year estate now you can kind of rewrite the g r p o advantage calculation to take this into account. Because I think this is less a problem like ppo if you know ppo is like the old school rl and it also is what people use for our lhf. But in the context of g r p o g r p o is like great for.

like leaning heavy on highly parallel inference compute, it's more memory efficient for the actual training process. It's much easier to do in a distributed fashion because you have less gradient syncing and less model weight copies. It's kind of like DPO on steroids, I think is one way to think about it, but it's also gets around a lot of the pitfalls of DPO both in that it's like online by default, as well as that you have this large set rather than just a pair of completions. So you do get like some intermediate credit assignment a little bit.

via this group comparison. But for tool use, seems to be far enough out of distribution of small models, doing, incorporating this turn level. So the way that I've been thinking about it is like, in like canonical RL, the state action are like things that you do many rounds of like, take an action, go to a new state, take an action, go to a new state. And for a while people thought about LLM RL as like, each token's action and the new sequence is a new state. And you can kind of do that.

Will Brown (36:10.733)

But you can also think of each turn as an action where, yeah, where the state is the response you get back from the tool call. And now you like have a different way of designing your algorithms to take into account credit assignment, which is that like, and it also is like a little more flexible from a reward perspective. it like feels like people are moving in the direction of model based rewards where you either LLM is a judge where

Swyx (36:14.053)

Yeah, that's more likely.

Will Brown (36:39.681)

the judge sees the correct answer or it has questions it's supposed to verify as properties of the response. Just because that's much more flexible than like trying to write these little parsers, like writing a math parser to check if a math question is right is like not that easy actually because there's so many edge cases and you want to handle like latex support and markdown and like equivalent fractions. And it's like, just like let a model do that. Don't don't have a 2000 line Python script that does that.

Swyx (36:45.341)

Mm-hmm.

Will Brown (37:09.599)

And so...

Swyx (37:09.629)

Sorry, let me clarify. Math parser to verify that the math is right. And you have a latex parser inside it.

Will Brown (37:17.193)

sorry, yeah, so like a lot of models naturally will like think in latex because they've been trained on lot of archive like tech. And so if you're doing like an R1 and people are like, math is easy to verify, the easy to verify still is usually like this very long piece of code that has to handle lots of annoying edge cases. And even then it's like 98%.

Swyx (37:22.695)

I didn't know that. yeah, that makes sense. I I guess.

Swyx (37:38.799)

Yeah. Hmm. Hmm. Okay. Interesting.

Will Brown (37:42.882)

Because like, it's a freeform response that is like, there's not only one way to write an equation. Like if you have two valid mathematical expressions that are equivalent, but they're also like symbolic. Like you need to verify that two symbolic expressions are correct. One of which might be written as code. One of which might be written as latech. One of which might be like written as word. Like you can't do it if it's words with these like literal parsers, but they try to cover a lot of these cases. That's also why you'd see models put boxed around their final answer a lot.

Swyx (38:04.787)

There's pseudocode out there, yeah.

Will Brown (38:12.767)

is that it's one hack is that it's much easier to kind of verify the right piece of the information if you know exactly where it's going to live rather than like the model saying, the answer to the question is four. Then you have to like parse away the answer to the question is, just throw that out. so it's like deterministic rewards are like nice if you can get them to work, but they're also really painful. And they're pretty hard to generalize across domains. Like for math, the easiest is when the final answer is an integer.

and lives in the same spot. Like there's a box that's going to be an integer. And so this is one of the reasons like everyone used GSMAK for so long is because it's like mostly integers. think it, A E is all integers. It's super easy to verify these things and to parse them. But as you go to, and multiple choice too, multiple choice is super easy to verify. But anything that's a little bit more flexible, deterministic, like rule-based rewards start to break down.

Swyx (38:44.645)

you

Swyx (39:08.754)

Alright.

Will Brown (39:10.197)

And, the model based direction seems to be pretty promising. And I think underexplored for like, what if you use LM as a judge in your RL loop? think kind of going back to like, Anthropics has been talking about this for a long time via constitutional AI. In that case, it was less about the LM judging and giving a direct reward to the model and more about training a reward model that was doing like token level advantage estimates. the P which is the PPO way of doing it.

But it seems like you can kind of do that for GRPO2 and other flavors of RL where you can incorporate like, you know, the reward model can basically be an LLM where like it's fine tuned to like be more calibrated maybe and to have the right kind of range of responses. But you could also have it be a reasoner. You could have it be something that is able to do tool calling. There's no reason why the full power of LLMs

Swyx (39:46.684)

A full reward model.

Swyx (39:51.794)

Yeah.

Swyx (39:58.418)

Yeah.

Will Brown (40:09.517)

can't be offloaded or can't be also given to the process of evaluating whether or not an answer is correct or satisfies a certain set of criteria. And so I think like, that's the direction I'm most excited about is like really pushing on kind of beyond deterministic rule-based rewards into like these more flexible things. And I think you want to do this both at like a, so okay, that paradigm is not going to work super well with

uh... turn a lot of token level rewards but i think it does work with turn level rewards like can the alum verify like whether a certain search query was useful? Sure. Um, like there's a lot of these questions that are pretty granular that alums can like basically nail all the time if it's a good enough alum and you can incorporate that into RL with that sort of approach.

Swyx (40:53.745)

Yeah, you decompose it.

Swyx (40:59.795)

Awesome. I think that was all the topics that we had prepped. Alessio, I think you're also pretty good on that. Obviously, it will take some time to figure out Cloud 4. Anything you want to plug? We already talked about your talk, I guess, coming up.

Will Brown (41:16.557)

Sure, yeah. I'll be at A.Engineer in a weeks, yeah, coming up. I'm also doing a course thing. Yeah, mine's gonna be, that's gonna be a lot of fun. I'm also collaborating with Kyle Corbett from OpenPype to do a course, which is both of us have our open source projects that we like, are agentic RL focused and kind of we've been friends for a while and are trying to do something that's a little more...

Swyx (41:20.947)

Two and fourth. Yeah. Your track is particularly hype.

Will Brown (41:44.777)

structured as like a way of kind of getting information out into the world for people who I think we're especially thinking about like kind of practical use cases for agents and helping people giving people a kind of outlet to learn more about like how the stuff works and yeah more coming soon about that.

Swyx (42:04.06)

Awesome. Well, I think that's it. Yeah, thanks for coming on at very short notice. I'm glad we can make this happen. We'll do part two with Callow and do full prime intellect thing whenever you guys are ready. Awesome.

Alessio (42:05.4)

Awesome. Thanks for coming on, Will.

Will Brown (42:14.286)

Sweet. Awesome. That'll be fun. Great.

The grad students not having taste is an advisor problem ;). They don’t make space to push students to improve at it. Many advisors just tell the students what to do actually.
