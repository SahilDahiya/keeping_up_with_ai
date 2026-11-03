---
title: Redesigning Agent Studio around Ghostwriter
kind: blog
topic: null
subtopic: null
secondary_topics: []
summary: null
triage: null
skip_reason: null
source: sierra
url: https://sierra.ai/blog/redesigning-agent-studio-around-ghostwriter
author: Sachi Shah
published: '2026-11-02'
fetched: '2026-11-03T06:06:31Z'
classifier: null
taxonomy_rev: 2
words: 556
content_sha256: 452a7ebbb15a9dd1623289fe39ba3ad7e2f5b0ec72f3b70ce90b853e38cba5fb
---

# Redesigning Agent Studio around Ghostwriter

# Redesigning Agent Studio around Ghostwriter

A year ago, almost every piece of code was written by engineers. Today, you’d be hard pressed to find a tech company that writes over five percent of its code by hand. Agent building is following the same path, from code to clicks to prompts.

[Ghostwriter](https://sierra.ai/blog/agents-as-a-service) is our agent for building agents — an [always-on teammate](https://sierra.ai/blog/ghostwriter-ai-tool-to-teammate) that not only helps you build but also understands how agents are performing, suggests improvements in Slack and Teams, and pushes whatever you approve live.

But even the best teammates need a shared place to work — and that’s Agent Studio, where you can investigate problems, work on improvements, test changes, and decide what ships. Until today, that involved navigating between the different parts of Agent Studio needed to edit journeys, run simulations, and review performance.

We’ve now redesigned Agent Studio around Ghostwriter, so you can go from asking why resolution rates dropped to examining the conversations, updating a journey, and testing the fix — all in one conversation. The evidence, changes, and test results stay together for your team to review before anything goes live.

![Ghostwriter](https://sierra.ai/-/cdn/image?src=https%3A%2F%2Fcdn.sanity.io%2Fimages%2Fca4jck6w%2Fproduction%2F1d8527179c0c73a9ea614922a76e49e6facd1d26-3200x1800.png&width=3840&quality=75)

## **Ghostwriter, wherever you are in Agent Studio**

Ghostwriter now stays with you as you move through Agent Studio, and it sees what you’re looking at — whether that’s a journey, a simulation, or a dashboard. When something looks off, you can ask about it or have Ghostwriter fix it on the spot, without stopping to explain the context. It combines what used to be spread across Explorer, Sierra Assistant, and other specialized agents, so you no longer need to know which tool does what.

## **A session for each piece of work**

Similar to ChatGPT or Claude, each session works like a chat thread. It keeps your conversation with Ghostwriter together with the changes it makes. Changes stay in the session until someone reviews and merges them. That means you can investigate why more customers are asking to speak with a support associate in one session, and build a new journey in another, without the two interfering with each other.

Sessions also make teamwork easier. You can share a session to work through a problem together, or fork one to pick up where a colleague left off. Before anything merges, you can ask Ghostwriter to review a teammate’s changes.

## **Build across multiple agents**

Most customer journeys involve more than one agent. Agent Studio now brings related agents into a single project, along with the data and channels they share, so your team can test and release them together.

Take a lender. One agent collects documents from applicants, while another manages the application and follows up until the loan closes. When the lender adds a new document requirement, Ghostwriter updates what the first agent asks for and how the second one follows up, all in one session.

## **Make every change easy to review**

As Ghostwriter does more of the editing, reviewing its work becomes more important. Line-by-line comparisons show exactly what changed. Preview Chat and Simulations let you test behavior before you merge. [Release governance](https://sierra.ai/blog/release-governance-guardrails-for-agents-at-scale) adds required approvals and controlled rollouts, so nothing reaches customers until your team says so.

The best agents are never finished. Ghostwriter keeps finding ways to make yours better, and Agent Studio keeps your team in control of every change.
