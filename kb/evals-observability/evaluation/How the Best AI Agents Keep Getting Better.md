---
title: How the Best AI Agents Keep Getting Better
kind: blog
topic: evals-observability
subtopic: evaluation
secondary_topics: []
summary: Argues AI agent experimentation needs metrics that reward outcomes plus guardrails
  that protect against gaming (e.g. containment rising because customers gave up,
  not because they were helped), given agents are probabilistic, conversational, and
  evaluated by inferred/judged outcomes.
triage: null
skip_reason: null
source: cresta
url: https://cresta.com/blog/how-the-best-ai-agents-keep-getting-better
author: Krystal Truong
published: '2026-08-07'
fetched: '2026-08-12T06:27:56Z'
classifier: claude
taxonomy_rev: 2
words: 1634
content_sha256: 61695e45e096dab27ff64283de23904e60f07b92230f37429dfec97c61ee732d
---

# How the Best AI Agents Keep Getting Better

A team ships a change to their AI agent's opening greeting. It sounds warmer, it tested well with everyone who hears it, and containment climbs the following week. Success, on paper.

Then someone reads the transcripts and finds that a group of customers now spend two extra turns being redirected before they give up on reaching a human. Containment went up because more people wore out, not because more people actually got helped. The team improved a number and worsened the experience…and they almost shipped it everywhere.

This is the real work of improving AI agents in production. Splitting traffic and comparing a number is the easy part. The hard part is everything around the number: picking a metric that reflects a genuinely better experience, protecting the outcomes that metric ignores, gathering enough data to trust the result, and understanding what caused it inside a conversation with many moving parts.

Teams that treat agent experimentation as split-and-compare learn the wrong lessons fast and the right ones slowly. A set of habits separates the teams who get this right from the teams who don't; we’ll discuss them here.

## Three Things Make an AI Agent Hard to Test

An AI agent is a living system whose behavior shifts with every customer and every turn. Three properties set it apart from anything you have tested before, and each one shapes how experimentation has to work.

1. **It is probabilistic.** The same variant can respond differently to two customers who open with the same sentence, because the model samples and the context differs. You are measuring a distribution of behaviors, so a single strong or weak conversation tells you very little on its own.

1. **It is conversational.** An outcome is the product of a whole sequence of turns, not a single choice. Change the greeting and you change what the customer says next, which changes what the agent does after that, so effects ripple through the rest of the conversation.

1. **Its outcomes are inferred.** Whether an issue was resolved is a judgment, often made by a model reading the transcript, and whether the customer was satisfied is a prediction. When the success metric is itself an estimate, the experiment inherits that uncertainty, and reading a result well means accounting for it.

These three properties raise the bar for experimentation. They are also why a handful of habits separate deliberate optimization from expensive guesswork.

## Pick a Metric That Rewards the Outcome, and a Guardrail That Protects It

Ask most teams what a better AI agent looks like and containment, the share of conversations handled without a human, comes up first. It is easy to measure and it maps to cost, so it becomes the default target, making it risky to use alone.

A variant can raise containment by helping more customers, or by wearing them down until they stop asking for a human. If containment is all you track, both look identical. Make escalation harder to reach, add another clarifying loop, keep the customer engaged a little longer, and the number improves while the experience gets worse. You win the metric and lose the customer.

The habit that prevents this is pairing a primary metric with a guardrail metric. You optimize for one outcome while holding a line on another. Optimize containment, but set CSAT as a guardrail, so a variant that lifts containment by frustrating people gets flagged instead of promoted. The guardrail is the mechanism that keeps optimization honest, and it is the difference between a *real* improvement and a masked regression.

The primary metric also has to match the goal of the specific change, which is not always containment. For example:

A regulated health payer testing whether simpler benefit explanations reduce confusion might set containment as the primary metric, with conversation sentiment and requests for a human as supporting signals, because the real question is whether people understood the explanation.

A travel brand testing a more consultative cancellation flow might set resolution as the primary metric, with containment and predicted CSAT alongside, because the goal is solving the underlying need rather than simply avoiding a transfer. 

The metric you choose defines what you mean by better, so choose it *before* you choose the variant.

![](https://cdn.prod.website-files.com/67feba4d16c14d85f1696c4f/6a7a6948086d380c68eec735_A_B%20Test%20Setup.png)

## Validate First, Then Let Real Traffic Pick the Winner

Experimentation belongs downstream of validation. Before a variant reaches live traffic, it should clear the same bar as any change: simulation against realistic customer behavior and a suite of test cases confirming it still does what it must.

That way, A/B testing answers a sharper question than whether the agent works, which you have already settled. It answers which working version performs best against the outcome you care about. Controlled, percentage-based exposure then keeps any single variant from carrying more traffic than you intend while you find out.

![](https://cdn.prod.website-files.com/67feba4d16c14d85f1696c4f/6a7a76575c04530d769c0653_blog-ai-agents-better-illus-1-1.png)

## Match the Experiment to Your Conversation Volume

One constraint decides whether A/B testing is even viable: statistical power. To trust that a gap between variants is real rather than noise, you need enough conversations.

How many depends on four factors that interact:

1. Your baseline rate
2. The size of the effect you want to detect
3. The confidence level you require, and
4. How many of your conversations are relevant to the change at all.

Three experiment designs from real Cresta customers show how differently this can play out. Each one carries a hypothesis, a methodology, and a bar for evaluating the result, the groundwork that has to exist before a number is worth trusting.

1. A consumer fintech lender running about 4,400 conversations a week wanted to test whether prompting customers to try the AI agent once before offering a human transfer would raise containment from a 50 percent baseline. Only about 8 percent of conversations were relevant to that change, so reaching the 190 relevant conversations needed for 95 percent confidence meant collecting roughly 2,375 conversations overall. At 4,400 conversations a week, that took under a week.

2. A home security provider on voice, at about 1,800 calls a week, tested whether a warmer, more empathetic voice improves containment. The change touched every call, so the full volume counted, and the test needed about 5,500 conversations, reaching confidence in about three weeks.

3. A lower-volume brand at about 180 conversations a week tested bullet points against prose for issue resolution. Half of those conversations were relevant to the change, and, even sized for a modest 5 percent target lift, it needed about 2,200 conversations overall, which meant roughly twelve weeks to a conclusion.

That third case is the one to plan around. Twelve weeks is long enough that the agent, the customers, and the business question may all move before the test finishes. A/B testing rewards high volume and frustrates low volume, so knowing which situation you are in belongs at the start of the design, not the end. When volume is thin, transcript review and pre-production simulation often teach you more than a test that will not conclude in time to matter.

![](https://cdn.prod.website-files.com/67feba4d16c14d85f1696c4f/6a7a69ef02e882fdbced5f7c_Examples%20Plot%20Graph.png)

## Test the System, Not Just the Prompt

Modern AI agents are rarely a single prompt. They are built from sub-agents that hand off to one another, and the behavior of one shapes the context the next one inherits. That structure makes attribution harder. If you change the triage sub-agent and resolution improves, the cause could be the change itself, or the way it altered what reached the sub-agents downstream.

Serious agent experimentation accounts for these interaction effects instead of treating each change as isolated. Sometimes that means running variants across more than one part of the agent at once and analyzing how the combinations perform together, rather than reading each change on its own. It is more involved than testing one variable in isolation, and skipping that step is how teams draw clean conclusions from messy data.

![](https://cdn.prod.website-files.com/67feba4d16c14d85f1696c4f/6a7a6a0b098d4d93be560459_agents%20hierarchy.png)

## What Disciplined Optimization Looks Like

A few principles fall out of all this:

- Define what better means before you test, and express it as a primary metric plus a guardrail that protects the experience
- Validate variants in simulation and test cases before they reach a customer, so experiments compare working versions rather than debug in production
- Confirm you have the volume to reach significance in a useful timeframe, and be willing to decide a test is not worth running
- Read results in the context of the whole agent, so you credit the right change in a multi-part system
- Treat a win as the start of the next question, since customer needs and agent behavior keep moving

## The Teams Whose Agents Keep Improving

The gap here is between running experiments and running them well. Run them casually and A/B testing hands you confident, wrong answers. Run them with discipline and it turns an AI agent from something you launch and hope holds up into something that improves against the outcomes you actually care about, conversation after conversation, without trading one away for another.

![](https://cdn.prod.website-files.com/67feba4d16c14d85f1696c4f/6a7a6a23c79d79e9c403dbc2_A_B%20Test%20Analysis.png)

This is the discipline we've built into A/B testing at Cresta. Variants clear simulation and test cases before they ever reach a live customer. Every experiment pairs a primary metric with a guardrail, so a win on one is never a hidden loss on the other. Results are measured on the same outcome models that already score your production traffic, not a separate scoring system. And because agents are systems, experiments can run across sub-agents, not just a single prompt.

The through line is simple: the teams whose agents keep getting better are not the ones who test the most, but the ones who test the right thing, and hold the line on everything else while they do it. To learn more and see these updates in action, [request a demo](https://cresta.com/request-a-demo).
