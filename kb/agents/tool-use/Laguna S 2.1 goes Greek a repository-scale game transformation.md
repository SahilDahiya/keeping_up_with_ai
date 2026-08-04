---
title: 'Laguna S 2.1 goes Greek: a repository-scale game transformation'
kind: blog
topic: agents
subtopic: tool-use
secondary_topics:
- product-engineering/case-studies
summary: 'Baseten case study: Poolside''s Laguna S 2.1 (118B MoE, 8B active params,
  1M context), running on Baseten Dedicated Inference, autonomously re-themed the
  715-file Hypersomnia C++ codebase from cyberpunk to Ancient Greek in under 99 minutes,
  orchestrating Step 3.7 Flash, Krea 2 Turbo, and NVIDIA Cosmos 3 Nano as sub-models
  (modifying 954 sprites and 64 code/config files) while deliberately declining to
  use the video model when it added no value.'
triage: null
skip_reason: null
source: baseten
url: https://www.baseten.co/blog/laguna-s-21-goes-greek/
author: Albert Lee
published: '2026-08-03'
fetched: '2026-08-04T06:50:57Z'
classifier: claude
taxonomy_rev: 2
words: 1353
content_sha256: 49c228262c4de2433ad782a788c603e6ecc44a4155aa82df50c47e8da768032e
---

# Laguna S 2.1 goes Greek: a repository-scale game transformation

![Poolside Laguna S 2.1](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1785447310-laguna-s-2-1-hi-res-4x.png%3Fauto%3Dformat%26fit%3Dcrop%26h%3D630%26w%3D1200&w=3840&q=100)

We tested a repository-scale transformation to see whether an agent could understand an unfamiliar codebase, coordinate changes across files and tools, and continuously verify its work. Poolside [Laguna S 2.1](https://www.baseten.co/library/laguna-s-21/), now available on Baseten Dedicated Inference, took on the challenge with a mythological twist.

We gave Poolside Laguna S 2.1 a simple task: transform [Hypersomnia](https://hypersomnia.io/), a free and open-source multiplayer top-down shooter game, from neon cyberpunk style into an Ancient Greek odyssey. To do this, Laguna had to understand a complex codebase, coordinate work across multiple AI models, and continuously verify its changes to ensure the gameplay was intact.

This post follows Laguna from its first pass through the repository to the final playable build. Along the way, we examine how it orchestrated specialized models, scaled generated assets across hundreds of sprites, preserved the game’s technical constraints, and decided when *not* to use an available tool.

## Meet Laguna S 2.1

[Laguna S 2.1](https://www.baseten.co/library/laguna-s-21/) is Poolside’s latest model for agentic coding and long-horizon work:

- 118B-parameter Mixture-of-Experts architecture, with 8B parameters activated per token
- Up to a 1 million token context window
- Thinking and no-thinking modes

In Poolside’s [published evaluations](https://poolside.ai/blog/introducing-laguna-s-2-1), Laguna S 2.1 performed competitively with substantially larger models on agentic coding benchmarks.

## Putting benchmarks to the test: transforming an entire repository

Benchmarks can measure coding and tool use, but they cannot fully show whether a model can navigate an unfamiliar codebase, make creative decisions, and recover when an approach fails. This repository-scale transformation put those capabilities to a more practical test.

Before making any changes, Laguna had to understand the codebase’s architecture, dependencies, asset pipeline, and undocumented assumptions. It then had to:

- Coordinate changes across interdependent files.
- Call the right tools and external models at the right time.
- Build and test continuously, diagnosing failures rather than merely detecting them.
- Revise the plan without drifting from the original task.

The [Hypersomnia codebase](https://github.com/TeamHypersomnia/Hypersomnia) is built from scratch in modern C++ without a commercial engine; the open-source game spans 715 compiled source files that power everything from gameplay and networking to physics, visual assets, and an in-game map editor.

That scale turned a playful, creative brief into a tightly constrained engineering task. Laguna had to transform the game’s neon cyberpunk identity into an Ancient Greek odyssey by modifying code, in-game text, configuration, and hundreds of visual assets. And it managed to do it without changing its simulation, geometry, networking, or core gameplay.

Unlike a bounded bug fix, this task combined creative ambiguity with technical interdependence across an entire repository.

### Testing Laguna as a model orchestrator

To make the test even more compelling, we added another wrinkle. Rather than ask Laguna to do everything itself, we deployed three supporting models on [Baseten Dedicated Inference](https://www.baseten.co/products/dedicated-inference/):

- [Step 3.7 Flash](https://www.baseten.co/library/step-37-flash/) , a fast vision-language model built for high-volume agentic work
- [Krea 2 Turbo](https://www.baseten.co/library/krea-2-turbo/) , a text-to-image model built for fast, high-quality image generation
- [NVIDIA Cosmos 3 Nano](https://www.baseten.co/library/cosmos3-nano/) , an 8B world foundation model built for text-to-video and image-to-video generation

Running them on dedicated deployments meant Laguna could call them as often as the task required without budget constraints, but Laguna also had to choose the right model for each job, turn its output into something the repository could use, and keep every contribution from breaking the game.

![Laguna acts as a model orchestrator](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1785442798-laguna-s.png%3Fauto%3Dformat%26w%3D1200&w=3840&q=75) Laguna acts as a model orchestrator

### The results

After 98 minutes and 58 seconds of autonomous work in [pool](https://github.com/poolsideai/pool), Poolside’s coding agent, Laguna S 2.1 produced “Hyperion,” an Ancient Greek-themed proof of concept that successfully launched Hypersomnia’s single-player tutorial.

![Hypersomnia became Hyperion: Laguna replaced the game’s cyberpunk aesthetic with an Ancient Greek visual identity while preserving the gameplay underneath.](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1784904954-screenshot-2026-07-24-at-7-55-24-am.png%3Fauto%3Dformat%26w%3D1200&w=3840&q=75) Hypersomnia became Hyperion: Laguna replaced the game’s cyberpunk aesthetic with an Ancient Greek visual identity while preserving the gameplay underneath.

The run at a glance:

- Laguna token usage: 76.33M input tokens and 449.5K output tokens
- Context used: 590.5K of 1.05M tokens (56%)
- Supporting model usage: 15 vision-language model calls (Step 3.7 Flash) and 100 image-generation requests (Krea 2 Turbo), with 53 successful image generations
- Assets modified: 954 PNG sprites, composited from 53 generated images
- Code and config files modified: 34 .cpp, 15 .h, 7 .hpp, and 8 JSON files

The result was playable, but not production-ready. Hyperion could not connect to existing Hypersomnia multiplayer servers. It did launch the single-player tutorial successfully, confirming that the new assets worked with the core gameplay.

![Laguna S 2.1 produced a playable Greek-themed single-player tutorial.](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1784905042-gameplay_clip-2.gif%3Fauto%3Dformat%26w%3D1200&w=3840&q=75) Laguna S 2.1 produced a playable Greek-themed single-player tutorial.

## Laguna’s creative judgment in practice

The playable tutorial was the final frame of a more layered story where delegation, revision, and a careful balance between creative ambition and technical restraint helped shape the path to get there. That judgment surfaced in three ways: Laguna directed Step’s language work, scaled Krea’s visual outputs, and recognized that Cosmos had no role in the game itself.

### Step 3.7 Flash: mythic language, familiar meaning

Laguna tasked Step 3.7 Flash with adapting the game’s language to the Ancient Greek theme. It specifically prompted Step to “produce a Greek-themed replacement with playful absurdity, NO profanity, kept SHORT and understandable.”

Rather than applying Greek names at random, Step translated each term according to its role in the game. Factions kept their power relationships, character classes remained recognizable, and objectives and game modes preserved their original meaning even as the language became more mythic.

Laguna remained the final editor. When Step returned Greek-language copy that would be inaccessible to most players, Laguna rewrote it in clear English while preserving the mythic tone. Its role went beyond delegation, and it judged whether each output served the larger goal.

### Krea 2 Turbo: scaling a visual language

Krea 2 Turbo served as the artist, while Laguna acted as visual director. For each asset Krea generated, Laguna defined the color palette, style, and key details in a tailored prompt:

![Game assets produced by Krea 2 Turbo](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1784909511-screenshot-2026-07-24-at-9-11-33-am.png%3Fauto%3Dformat%26w%3D1200&w=3840&q=75)

Laguna then applied this visual language across hundreds of assets without breaking the game. Instead of asking Krea to generate every sprite, Laguna built a reusable library of Greek materials from a smaller set of outputs. It composited that library across roughly 945 sprites with faction-specific colors, reducing model calls while keeping the visual language consistent. Each composite preserved the original sprite’s exact dimensions and transparency mask, keeping the asset pipeline, pivots, and collision geometry intact so the game could still compile and run.

For high-visibility assets such as the Hyperion logo, Laguna also commissioned Krea for bespoke “hero” generations. However, for the final build, it chose the validated composites over the more experimental, fully regenerated images. This was a deliberate tradeoff in favor of a stable, playable build.

### Cosmos 3 Nano: restraint is part of orchestration

Laguna’s judgment also showed in the model it chose not to use. Although Cosmos 3 Nano was available for video generation, Laguna found no natural role for video in the game. Adding a cutscene simply to use the model would have expanded the scope without improving the re-theme, so Laguna left Cosmos out. Laguna prioritized matching efficiency rather than maximizing the number of calls.

Later, we found a clear use case outside the game: a playful intro cutscene for this blog. Laguna used Cosmos to produce the GIF below:

![Cosmos 3 Nano produced this gif](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1784909789-intro_cutscene.gif%3Fauto%3Dformat%26w%3D1200&w=3840&q=75)

## The build survived Olympus

Ancient Greece is no joke. But after 98 minutes and 58 seconds, we are proud to report that the marble was intact, the spells still cast, and we were able to launch *Hyperion* into a playable tutorial.

The result showed that Laguna could carry a creative brief across a complex repository, orchestrate specialized models, and make the tradeoffs needed to keep the project running (like not calling models it didn’t need).

[Laguna S 2.1](https://www.baseten.co/library/laguna-s-21/) is now available on Baseten Dedicated Inference. Have a framework migration stuck in your backlog? Give it the repository, define what cannot break, and let it plan, implement, and validate the change. Tell us how it goes!
