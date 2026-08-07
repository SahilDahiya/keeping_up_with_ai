---
title: 'Designing Partnership: How Conductor Works With You, Not For You'
kind: blog
topic: null
subtopic: null
secondary_topics: []
summary: null
triage: null
skip_reason: null
source: cresta
url: https://cresta.com/blog/designing-partnership-how-conductor-works-with-you-not-for-you
author: Janice Cheuk
published: '2026-08-06'
fetched: '2026-08-07T06:23:35Z'
classifier: null
taxonomy_rev: 2
words: 1424
content_sha256: d71c01358dcd5fb3f5ca92d3a6577364045eabf052d22acdd63d337510bad3f4
---

# Designing Partnership: How Conductor Works With You, Not For You

What separates a tool you operate from a collaborator you work with lies in the design. That principle is at the heart of Cresta Conductor, our developer-first environment for building, testing, and refining AI agents, [which we launched in June](https://cresta.com/blog/cresta-conductor-the-agent-for-ai-agent-development). 

Conductor reads your actual historical conversations and knowledge bases before it proposes a build plan, and narrates its thinking the whole time it builds, so you can weigh in while the work is still in motion, rather than only approving or rejecting it once it's done. 

That's the difference between a partnership and a handoff; a tool waits to be told what to do and hands back a result, with no expectation you'll be part of the process, while a collaborator does the reading first, proposes an approach, and stays in step with you as it goes. 

I designed Conductor to be the latter, because what it's building, an agent that will eventually act on its own with real customers, has to be something shaped by human judgment, not something simply signed off on.

## From Tool to Collaborator: A Different Interaction Model

Before AI agents, software was always deterministic: click a button, and you already know what happens next. That's still true for pieces of what Conductor does, such as a tool call, a lookup, or a pipeline step that will run the same way every time it's invoked. 

What's *not* deterministic is the reasoning Conductor employs to decide which of those steps to take, in what order, and when. Conductor composes that path at runtime based on the request in front of it, rather than following a sequence designed in advance. The real design work was the interaction patterns, the rules that had to hold no matter which path a given request took.

One design pattern runs through everything else. Point at a piece of feedback, a failing test, or a message from a Conversation Lab run, and it becomes a citation in your next message, the same way every time, no matter where it came from. The five things that follow are what that same principle looked like applied to the moments that mattered most.

## A Partner Shows You the Plan Before Building It

Starting from a blank prompt puts all the thinking on the builder before the agent has done any of its own. Conductor starts from a different place. It goes looking through your real historical conversations, knowledge bases, and coverage gaps first, then runs a discovery pass before anything gets built. 

What comes out is a series of questions to further customize your agent. After Conductor proposes a build plan, nothing gets generated until you approve it. 

This approval step keeps you in the role of judge rather than approver, evaluating a design built on evidence you recognize instead of skimming already-generated output for mistakes.

## A Partner Hands You Work You Own

Once the blueprint is approved, Conductor generates the real substance of a production agent: the prompts, configuration, tools, and custom code needed for deterministic actions against your own APIs. That output is real and it's yours, living in your environment and your codebase right alongside the tools your team already uses. 

When an agent's behavior lives in inspectable, developer-owned code rather than only in prompt instructions, you can read it, diff it, test it, and take responsibility for it the way you would any other part of your codebase. I scoped this working closely with the engineers building the runtime underneath it, because a real partnership should leave you with work you can understand, change, and own.

## A Partner Knows When to Decide and When to Ask

At genuine branch points, scope, approach, tradeoffs, and phase handoffs, Conductor presents a structured decision, leading with a recommended option, offering real alternatives, and leaving room for custom input. If the context moves on before you answer, a stale prompt marks itself superseded rather than letting you resolve a decision that no longer maps to reality.

Before it runs a command, Conductor asks in plain language rather than raw permission-rule syntax, so approval is a real decision rather than a reflexive click on jargon you can't parse. Every phase –discover, build, test, optimize – closes on an explicit choice to proceed, iterate, or pause, instead of carrying you through a wizard you can't stop.

## A Partner Shows Its Work

Judgment about when to ask is only half the process. The other half is whether you can actually see and verify what your collaborator has done, and Conductor was designed to always give you that visibility.

You can check its work directly instead of taking its word for it. Conversation Lab lets you drive the agent you're building, running real conversation flows against it, generating simulated conversations to smoke-test its behavior, and dropping straight into debugging when a case fails an evaluation, with the evidence in front of you the whole time. When a specific response is wrong, you don't have to reconstruct the problem from memory afterward. You can click on that exact turn in the transcript, suggesting a fix right there in context.

While it's working, the work stays legible. A live timeline narrates what the agent is doing in plain language, translated out of file paths and command output. The design lives in the blueprint as the single source of truth. The agent's logic renders as a visual map instead of raw config, and for developers who want full fidelity, an advanced view exposes the underlying trace. Progressive disclosure is applied to autonomy, utilizing a calm surface by default, with an in - depth surface only one intentional click away.

## A Partner Stays After the Work Ships

The collaboration doesn't end at launch. When customer feedback comes in, it surfaces in the performance view ranked by priority, not just as a raw list. Selecting an item and asking Conductor to look into it sends the same request every time: identify the root cause, propose a fix, and leave everything alone until I confirm it. It's the same instinct as suggesting a fix on a message in Conversation Lab, just running later, once real customers are the ones surfacing the problems.

## Automate the Necessary, Protect the Judgment

A philosophy emerges from these five decisions. Conductor takes on the mechanical parts of building an agent, the setup, the wiring, the discovery legwork, so the builder's attention stays on the work that actually determines whether the agent can deliver a good customer experience: what it should do and refuse to do, where it needs to be careful, which tradeoff is right for this particular customer.

Those are human decisions, and the best collaborators clear everything around that work instead of taking it off your plate entirely. Building Conductor required making that same trade myself.

## The Same Shift Changed How I Design

My design thinking hasn't changed. I still start from the user, design for trust and clarity, obsess over the details. The toolchain is what's different. Figma is still my scratchpad, but not the whole process anymore, because an agentic product can't be evaluated at static fidelity. A static mock up can’t show you whether the agent asks you at the right moment, or whether the wait in between feels like an intentional part of the process or dead time. 

I finish my designs in the running system, working alongside the engineers building it. I push code both to prototype and to ship it into production, resolving the finer interaction details against real agent behavior, because that's the only context where they're actually true. 

That's the same trade Conductor offers its users, one layer up. Human judgment, direction, and taste don't move. The execution that used to consume time gets automated, so you can invest yourself in the part only a person can do well.

## What Partnership Requires

Agent tools are often measured by how much they can do without you. I think the more interesting question is how well they work with you. 

The ones that hold up as AI agents grow more capable will be the ones that feel like a good collaborator, rooted in your reality, transparent about their work, clear about when to decide and when to ask.

That's what it means to design a partnership rather than a tool. Conductor is aimed to be the collaborator that makes your judgment go further, not the system that takes the work off your hands. And if working on systems like this sounds interesting, **we’re hiring. Come build with us****.**
