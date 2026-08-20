---
title: 'Software That Learns: How Cresta Captures Expertise'
kind: blog
topic: null
subtopic: null
secondary_topics: []
summary: null
triage: null
skip_reason: null
source: cresta
url: https://cresta.com/blog/software-that-learns
author: Tim Shi
published: '2020-05-03'
fetched: '2026-08-20T06:14:39Z'
classifier: null
taxonomy_rev: 2
words: 883
content_sha256: 7fa6a670bba47786c93383fa0f646c3d2612aafb18d512d19eaf452cc25db105
---

# Software That Learns: How Cresta Captures Expertise

Think about the last time you taught someone something difficult. Did you just tell them what to do, or did you show them how it’s done?

Showing how something is done conveys a wealth of unspoken information. By observing a skill in practice, we can see which actions and behaviors to emulate, and which to avoid. Observation also lets us identify situational nuances that we can’t define, or wouldn’t otherwise be aware of. These concepts are at the core of experiential education and hands-on learning philosophies.

These same concepts apply to programming intelligent software, and are the foundation of Cresta’s expertise management technology.

**Software 2.0: Software that learns by example**

Traditional software engineering focuses on telling a program *what* it should do, e.g. encoding rules and functional parameters to determine output. But as we use programs to address higher-order more complex real-world problems, traditional approaches to software engineering start to reach their limitations.

The key limitation lies in the distinction between knowledge and expertise.

Expertise is situational. It is the sophisticated understanding of how to best approach a given scenario. It takes years for a person to accumulate expertise, which often remains locked inside a person’s brain. Expertise is hard to explain, and much harder to code.

*“Stochastic Gradient Descent can write better code than you.” – Andrej Karpathy.*

So how do you teach a program expertise? By example. Rather than programming with step-by-step instructions, machine learning allows us to program by example. By training machine learning programs with examples of successful outcomes, we unlock the full potential of human knowledge, allowing neural networks to give value to data points we may have not considered previously. Andrej Karpathy describes this as [Software 2.0](https://medium.com/@karpathy/software-2-0-a64152b37c35). As Andrej [put it](https://twitter.com/karpathy/status/893576281375219712?lang=en), “Stochastic Gradient Descent can write better code than you.”

**An example of Software 2.0 in action**

To better understand how learning by example can empower teams, let’s take a look at another practical implementation: AlphaGo.

![](https://cdn.prod.website-files.com/67feba4d16c14d85f1696c4f/68137001530fe88afd05a467_20_10_karo_11_oktjabr_otkrytie_festivalja_360_jpg_1507968337-1024x576.avif)

A workflow is like a game; your next move could take you anywhere, leading to many different potential outcomes. (Image courtesy of AlphaGo)

[AlphaGo](https://deepmind.com/research/case-studies/alphago-the-story-so-far) was first program to defeat a world Go champion. For humans, the game of Go requires years of experience to master. But AlphaGo was able to beat world-class players within months of its inception.

There are two key architectural components that help the program make its decisions.

- **Policy** : given the situation, what move can I make*next* ?
- **Reward** : given these options, what*value,* or*reward,* is associated with each of them?

To know what move to make next, a Go player needs to stay calibrated within the changing contexts of the game. In each configuration of the board, each potential move has its own unique reward. Just like a board game, an individual’s workflow can vary. Experts learn how to optimize their workflows for the reward of a given task. This was the focus of our PhDs.

At Stanford, we worked on reinforcement learning to “clone” workflows from demonstration. We built [World of Bits](http://proceedings.mlr.press/v70/shi17a.html), a platform in which crowd-workers perform simple tasks defined by NLP questions. Leveraging human data, we trained a neural network policy to optimize for the reward of a given task.

![](https://cdn.prod.website-files.com/67feba4d16c14d85f1696c4f/68138f3420794c334135e0b8_681370b836a44d39df2bcdd7_wob-new.gif)


**Cresta: A System of Record for Expertise**

At Cresta, we apply these principles to help make contact center agents [Experts on Day One®](https://cresta.com/blog/experts-on-day-one). Consider the workflow of a contact center agent communicating with a customer. A conversation can have many different endings. The agent must rely on her expertise to optimize the outcome. She continuously evaluates the possible behaviors, expressions, questions, or offerings that would help close a deal. Naturally, experts produce better outcomes than average performers.

Cresta captures the expertise of your best agents and distributes it across your entire team. [Cresta’s AI](https://cresta.com/about/) observes expert agent behavior, identifies high-leverage actions, and weighs the rewards of each action based on prior outcomes. Actions with the highest values are converted into suggestions and shared with the rest of the team at the right moment. It’s as if every agent is your best agent.

By helping agents expertly navigate customer interactions, Cresta has been able to close the 3x performance gap between the lowest and highest performing agents.

For the enterprise, Cresta’s impact is immediate. Large enterprise sales teams with hundreds of agents currently use Cresta to capture expert behavior and dramatically increase revenue, improve conversion, and accelerate agent on-boarding. By helping agents expertly navigate customer interactions, Cresta has been able to close the 3x performance gap between the lowest and highest performing agents.

This is the foundation of our work at Cresta — and sales is just the beginning. Across every company, there exists expertise locked away in many different domains. We are moving towards a world where observation trumps codification. With enough examples of how experts have accomplished desired outcomes, we leave it to our neural network to decide the best way of achieving them. This is what makes Cresta unique as we work to deliver partially automated, highly intelligent work experiences in any domain.

We are absolutely excited about the road ahead! If you are interested in building systems that learn by example, please consider applying for [a role](https://cresta.com/careers/) on our team!

*Thanks to Andrej Karpathy, Alex Roe, Navjot Matharu, Sophia Arakelyan, and Osman Javed for their reviews.*
