---
title: SPC hackathon winners build with Llama 3.1 on Baseten
kind: blog
topic: prompt-engineering
subtopic: context-engineering
secondary_topics:
- product-engineering/case-studies
summary: Hackathon-winning tool TestNinja used deterministic Python code to build
  a dependency graph around a PR's modified lines and passed that graph (rather than
  raw diffs or the whole codebase) as context to Llama 3.1 405B for test generation.
triage: null
skip_reason: null
source: baseten
url: https://www.baseten.co/blog/spc-hackathon-winners-build-with-llama-3-1-on-baseten/
author: Philip Kiely
published: '2024-08-16'
fetched: '2026-11-24T06:12:44Z'
classifier: claude
taxonomy_rev: 2
words: 633
content_sha256: 9fb5f2a203e5dfecdbb2ccc3e82b6f65326d949eecd6e7522f4d0a0b8f001d96
---

# SPC hackathon winners build with Llama 3.1 on Baseten

Community
# SPC hackathon winners build with Llama 3.1 on Baseten

SPC hackathon winner TestNinja and finalist VibeCheck used Baseten to power apps for test generation and mood board creation.


- Authors
- Last updated
- Originally published

At [South Park Commons](https://www.southparkcommons.com/)’ recent “Llamathon” — a hackathon focused on the new Llama 3.1 family of LLMs — teams spent the weekend pushing the boundaries of these new open-source models from Meta. As a sponsor, Baseten provided participants with free model hosting on H100 GPUs and technical support.

Two teams — TestNinja and VibeCheck — made the finals using Baseten-powered projects, with TestNinja winning a prize for “Most Interesting Technical Achievement.” We spoke with members of both teams to learn more about their projects.

Stanford students [Ameya Jadhav](https://www.linkedin.com/in/ameyajadhav/), [Nahum Maru](https://www.linkedin.com/in/nahum-maru-062957202/), [Alexander Waitz](https://www.linkedin.com/in/waitz/), and [Niall Kehoe](https://www.linkedin.com/in/niallkehoe/) teamed up to build [TestNinja](https://www.ameyajadhav.xyz/work/testninja), an LLM-powered test generation tool.

TestNinja is a perfect example of the power of combining traditional software engineering with AI engineering. The tool uses a webhook to catch new PRs to GitHub and find modified lines of code. Using pure Python logic, it builds a dependency graph around the modified code and passes that entire graph into the LLM as context for test generation.

The intermediate dependency graph generation is what makes this agent so interesting. In a naive approach, you might pass only the diffs into the LLM, or at the other extreme, you could pass as much of the codebase as the context window can fit. TestNinja uses deterministic Python code, not AI tools, to extract the most relevant context for test generation. That context is passed into Llama 3.1 405B, which writes the tests.

> Baseten streamlined the integration of Llama 3.1 405b into TestNinja, requiring minimal setup and delivering impressively low latency. Our product's success is largely due to the powerful Baseten suite and the unwavering support of their engineering team!

Congratulations to Ameya, Nahum, Alexander, and Niall on their hackathon victory! For more details on their project, see [Ameya’s LinkedIn post](https://www.linkedin.com/posts/ameyajadhav_we-won-most-interesting-technical-achievement-activity-7226294361829847040-0jIU) or the team’s [demo video on YouTube](https://www.youtube.com/watch?v=cH-eiGTKLr4).

[Irfan Manji](https://www.linkedin.com/in/irfanmanji/) and [Paul Crouther](https://www.linkedin.com/in/paul-crouther-47221b52/), Co-Founders of [June AI](https://www.tryjune.ai/), teamed up with [Priya Shah](https://www.linkedin.com/in/priyashah13/) and [Ayush Garg](https://www.linkedin.com/in/lazeash/) to explore Llama’s inherent design intelligence. Together, they built [VibeCheck](https://www.linkedin.com/posts/irfanmanji_we-made-it-to-the-finals-in-an-adrenaline-fueled-activity-7226259416021356545-wPXV), which automates the manual process of generating early-stage design concepts for creative projects.

As co-founders of [June AI](https://www.tryjune.ai/), an AI event planner, Irfan and Paul wanted to see if Llama 3.1 could power their next set of features. The team started the hackathon with a simple question: can Llama 3.1 generate high-quality design assets from a simple user input — in this case, hex code representing a color?

As it turns out, it can! The team used Baseten to deploy Llama 3.1 8B, and expanded the project to an iterative design process for generating mood boards. Design professionals, from UX designers to interior decorators, use mood boards early in the client consultation process to get aligned on high-level vision. However, this process requires manually creating multiple mood boards at each stage, most of which will be thrown away. VibeCheck reduces the amount of time designers spend on temporary mood boards, giving them more time to focus on the rest of the process.

Paul used Baseten to experiment with multiple sizes of Llama 3.1 for the project. As it turned out, they just needed the inexpensive 8B size to get quality results for this use case.

> I was trying to figure out the quickest way to get everything up and running — using Truss on Baseten was the best way to get things running but also to manage the infrastructure of any model from 8 to 405B parameters.

We’re looking forward to seeing what Irfan, Paul, Priya, and Ayush build next! For info on VibeCheck, see [Irfan’s LinkedIn post](https://www.linkedin.com/posts/irfanmanji_we-made-it-to-the-finals-in-an-adrenaline-fueled-activity-7226259416021356545-wPXV) or the [team’s demo Loom](https://www.loom.com/share/a50f67aa0add4260ab6982d0286d8bed?sid=c37b0d28-d3af-411c-9641-10c86114cb30).
