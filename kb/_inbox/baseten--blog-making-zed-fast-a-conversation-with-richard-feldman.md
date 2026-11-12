---
title: 'Making Zed fast: A conversation with Richard Feldman'
kind: blog
topic: null
subtopic: null
secondary_topics: []
summary: null
triage: null
skip_reason: null
source: baseten
url: https://www.baseten.co/blog/making-zed-fast-a-conversation-with-richard-feldman
author: Madison Kanna
published: '2025-09-23'
fetched: '2026-11-12T06:10:30Z'
classifier: null
taxonomy_rev: 2
words: 1143
content_sha256: 020e6cb9cd8607c6360839eecf9af671b06e613c2787c45b6d995f3165274154
---

# Making Zed fast: A conversation with Richard Feldman

Community
# Making Zed fast: A conversation with Richard Feldman

How Zed achieves blazing-fast performance through custom graphics rendering, their vision for real-time code collaboration, and thoughtful AI integration.


- Authors
- Date
- September 23, 2025

TLDR

In this interview, Richard Feldman, Software Engineer at Zed Industries, and I discuss what makes Zed so remarkably fast. We dive into the technical decisions behind building a code editor, explore the Zed team’s broader vision for text editors, their approach to AI integrations, Baseten’s partnership for edit predictions, and how real-time collaborative editing works in practice.

**Richard:** Fundamentally, Zed is fast because it was built from the ground up with "let's be as fast as possible" as the primary goal. Everything was created from scratch with that objective in mind.

This wasn't the case with [Atom](https://atom-editor.cc/), which spun off Electron that VS Code is built on. Atom's original design goals were to be really hackable and built on web technologies. Zed takes a different approach—it's not built on web technologies at all.

The three co-founders (who previously worked on Atom at GitHub) sat down and asked: "How do we make this thing go as fast as possible?" Step one was going straight to the graphics card, which is where GPUI came from—the custom framework they developed.

They literally wrote hand-coded shaders for different platforms (Mac, Linux, Windows). These are what the graphics card speaks directly—different for each operating system. This is actually why we don't have stable Windows support yet; achieving that level of performance takes time when you're building everything from scratch.

**Richard:** If you look at the Zed codebase, there's a ton of handwritten custom code—shaders written in languages like Metal (Apple's shader language) for different targets. They wrote everything from scratch rather than building on top of existing frameworks.

The approach was definitely not quick and easy, but the goal was quality, not speed of development. It's all about rendering straight to the GPU and doing everything possible to maximize performance at every layer.

**Richard:** The big picture goes beyond just being a fast editor. There's a [blog post](http://zed.dev/blog/sequoia-backs-zed#introducing-deltadb-operation-level-version-control) we released about Delta DB, which outlines our long-term vision for collaboration and version control.

For decades, Git has been the standard for version control, based around snapshots—you make commits representing the code at a particular point in time. But that's a really coarse-grained way to look at code. We have much more useful information: How did the code get there? What were the conversations around it? Where are the code reviews and discussions?

We're often doing code archaeology, staring at snapshots wondering how and why code evolved to its current state. Delta DB aims to build an open system that captures the entire real-time collaboration process—all that high-fidelity data of humans collaborating with each other and with AI agents.

The vision is to be like Git and GitHub—Git is free, GitHub is the business built around it. We want to create the next evolution after Git, with seamless Google Docs-style real-time collaboration on code as a central feature.

**Richard:** We have several AI features, but it's important to understand our philosophy. A common misconception is that we ship AI features to make money—that's not our business model. We charge for some AI features because they cost us money to provide, but we'd give them away for free if we could. We don't make money off integrations like Claude Code.

Two of our AI features:

1. **Edit predictions** (tab autocomplete) - We're currently working on V2 of this system
2. **Agentic AI** - Conversational AI that can read and modify your codebase with different permission levels

What makes our AI integration unique is customization. You can choose any model you want, or even bring your own agent. You can use Claude Code right in Zed with a proper GUI instead of terminal interface.

**Richard:** The thing that was really awesome about working with Baseten on this was just that we care a lot about latency. We're writing graphics shaders from scratch, and we really don't want to do all that work just to have really slow edit predictions.

The challenge with edit predictions is that if you want really fast predictions using a model that's useful enough to make reasonable predictions, that just really can't be running on my laptop. It needs to be running on really high-powered GPUs. Since I don't have really high-powered GPUs on my laptop, that means it needs to be in somebody else's data center.

That's exactly what we use Baseten for—they have a bunch of really high-powered GPUs. They also worked with us to get the latency on this as low as possible, counting the entire network round trip and the fact that different users are geographically distributed. There are a lot of factors that go into how many milliseconds pass before we get some prediction back that I can use in my editor.

Baseten's been an awesome partner for getting that number as low as possible so the edit predictions can be really fast. Since that's not the business we're in, we really appreciate working with the Baseten folks.

*Note: To see our case study with Zed, check out this post.*

**Richard:** I think of large language models as "rough draft generators." They give me a boost by saving time on the initial draft, but I usually end up rewriting most or all of the code for anything non-trivial.

This is especially true for the lower-level, high-performance work I do on Zed. AI models often get subtle things wrong, so I need to review and iterate. But they're excellent for getting unstuck—if I have an intuition that something should be possible in a language, I can ask an AI to generate valid syntax and then study that code.

The key is maintaining control. I don't feel like I'm delegating to AI and letting it take the wheel. It's another tool in my toolkit, and I remain in control of the final output.

**Richard:** We use Zed for everything at the company—meetings, issue triage, pair programming. When we have meetings, we're all co-editing markdown documents in real-time, just like Google Docs but for code.

The pair programming experience is seamless. You can follow someone's cursor, see their edits in real-time, and jump in to make changes yourself without any coordination overhead. No "wait, what line are you on?" or keyboard sharing needed.

We regularly have 30+ people editing the same document simultaneously, and it feels responsive and fast. The performance allows this kind of large-scale real-time collaboration that just works.

*Want to try Zed? Visit zed.dev.*

*Richard Feldman can be found as @rtfeldman on social platforms. He also hosts the Software Unscripted podcast and Zed's Agentic Engineering, as well as teaches several courses for Frontend Masters, including Introduction to Elm, Advanced Elm and introduction to Rust.*
