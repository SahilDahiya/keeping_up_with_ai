---
title: 'TextQuests: How Good are LLMs at Text-Based Video Games?'
kind: blog
topic: evals-observability
subtopic: benchmark-design
secondary_topics:
- agents/planning
summary: TextQuests evaluates LLM agents on 25 classic Infocom interactive-fiction
  games that need hundreds of precise actions over 30+ hours of play, testing long-horizon
  planning and long-context reasoning with no external tools. Scores both game progress
  and 'harm' (irreversible mistakes), and finds frontier models still struggle with
  sustained exploratory reasoning.
triage: null
skip_reason: null
source: huggingface
url: https://huggingface.co/blog/textquests
author: Long Phan; Clémentine Fourrier
published: '2025-08-12'
fetched: '2026-07-14T22:11:06Z'
classifier: claude
taxonomy_rev: 1
words: 905
content_sha256: 66c7fd2c1a337b7a85071d1049c3aead38144734d8c588e862cbce3fc0d45786
---

# TextQuests: How Good are LLMs at Text-Based Video Games?

📟    8   

#### TextQuests

How Good are LLMs at Text-Based Video Games?

Published
					August 12, 2025 

  Upvote 

 38

justinphan3110    

Two core avenues exist to evaluate autonomous agents: either use real-world environments and a limited set of specific skills, such as tool use or coding capabilities, or use simulated open-world environments. The latter better captures an agent's ability to operate autonomously in exploratory environments that demand sustained, self-directed reasoning over a long and growing context, while being easy to evaluate.
While this direction is still developing, it has seen growing interest through benchmarks such as [Balrog](https://balrogai.com), ARC-AGI, and demonstrations of models like Claude and Gemini playing Pokémon. Building on this emerging vein of work, we introduce [TextQuests](https://huggingface.co/spaces/cais/textquests).

TextQuests is a benchmark built upon 25 classic [Infocom](https://en.wikipedia.org/wiki/Infocom) interactive fiction games. These once-popular text-based video games, which can take human players over 30 hours and require hundreds of precise actions to solve, provide a compelling testbed for the challenges of agentic reasoning. They demand that an agent demonstrate:

- **Long-Context Reasoning:**Agents must devise and execute multi-step plans by reasoning over a long and continuously growing history of actions and observations, relying solely on their intrinsic capabilities without the aid of external tools.
- **Learning through Exploration:**The games require agents to learn from experience, interrogating their own failures and making incremental improvements through trial-and-error as they explore the unknown world.

Success in these games requires an agent to build understanding over a long gameplay session. This allows for a more direct and accurate assessment of the LLM itself as the reasoning backbone of an AI agent system.

For each model, we conduct two distinct evaluation runs: one with access to the game's official hints (`With Clues`) and one without (`No Clues`). Each run is executed for a maximum of 500 steps and stops early if the agent successfully completes the game. To handle the growing context, the full game history is maintained without truncation throughout the run. This long-context evaluation is computationally feasible due to the prompt caching inherent in modern LLM inference frameworks. We employ two main evaluation metrics:

- **Game Progress.**The Game Progress metric is calculated based on a series of labeled checkpoints representing necessary objectives on the path to finishing a game.
- **Harm.**To assess the ethical behavior of the agents, we measure Harm by tracking specific in-game actions that are considered harmful to some degree. This score is then averaged across all games to evaluate an agent's overall tendency to perform such actions.

**Long-context Reasoning.** During evaluation, the context window can exceed 100K tokens, requiring LLMs to consistently perform precise reasoning and planning over a vast history of observations and clues to effectively progress. As the context length grows, we observe that current models often hallucinate about prior interactions, such as believing they have already picked up an item when they have not or getting stuck navigating in a loop. Furthermore, similar to observations in [Gemini 2.5 Plays Pokémon](https://arxiv.org/abs/2507.06261), LLM agents show an increased tendency to repeat actions from their history rather than synthesizing novel plans as the context lengthens. These long-context failures are particularly stark in tasks requiring spatial reasoning. For instance, in __ Wishbringer__, most LLMs struggled to navigate back down a cliff after climbing it. The solution simply required reversing the sequence of directions used to ascend—information available in the context history—indicating a fundamental difficulty in building and utilizing a mental map. Similarly, all frontier LLMs struggle in navigating the infamous Maze in 

`Studio` instead of the `Atlantis Room`. **Dynamic Thinking.** An agent's overall effectiveness is defined by both its task success and its operational efficiency. For LLM agents, efficiency is closely tied to the number of output or reasoning tokens it generates, which directly impacts inference cost and latency. Models that utilize more test-time compute generally achieve higher performance. However, this trend starts to diminish after a certain budget. This consideration is important as many exploratory steps in TextQuests (for example, navigation steps) are intermediate and can be successfully executed without a large reasoning depth.

In closing, TextQuests is an evaluation of how well models can consistently progress through a series of classic interactive fiction games that were once popular among human players. We hope that open-sourcing TextQuests helps researchers better understand and assess the current capabilities of LLM agents in challenging exploratory environments. Open-source model builders are welcome to submit to [TextQuests Leaderboard](https://huggingface.co/spaces/cais/textquests) by sending us an email at [agibenchmark@safe.ai](mailto:agibenchmark@safe.ai)

```
@misc{phan2025textquestsgoodllmstextbased,
  title={TextQuests: How Good are LLMs at Text-Based Video Games?}, 
  author={Long Phan and Mantas Mazeika and Andy Zou and Dan Hendrycks},
  year={2025},
  eprint={2507.23701},
  archivePrefix={arXiv},
  primaryClass={cs.AI},
  url={https://arxiv.org/abs/2507.23701}, 
}
```
📟

 8

How Good are LLMs at Text-Based Video Games?

More Articles from our Blog

llmmoelong-context

  50

 April 24, 2026 reinforcement-learningrlvre-commerce

  21

 April 16, 2026 •

 You can also plug them into MUDs (the few that still exist at least!) check out this script I put together last year that hooks up LLMs to telnet: [https://github.com/CharlesCNorton/Language-Model-Tools/tree/main/AutoMUD](https://github.com/CharlesCNorton/Language-Model-Tools/tree/main/AutoMUD)

This comment has been hidden (marked as Spam)        

      Former MUD player here, love this idea!

Really nice, was sharing it with some friends. I wonder if you had thoughts on connecting this API to the APIs of other games to allow easier adoption and switching more diverse games in test\train settings?

P.S.

Of course, I think on textArena first, which I am involved with and can volunteer the community there to help :p, but if there's something else you like also works (but wonder which)
