---
title: 'Laguna S 2.1 goes Greek: a repository-scale game transformation'
kind: blog
topic: product-engineering
subtopic: case-studies
secondary_topics:
- agents/multi-agent
summary: Case study testing Poolside's Laguna S 2.1 (118B MoE, 8B active, 1M context)
  on a repository-scale restyling of the open-source game Hypersomnia, examining how
  it orchestrated multiple specialized models and verified its own changes.
triage: null
skip_reason: null
source: baseten
url: https://www.baseten.co/blog/laguna-s-21-goes-greek
author: Albert Lee
published: '2026-08-03'
fetched: '2026-11-12T06:08:20Z'
classifier: claude
taxonomy_rev: 2
words: 1600
content_sha256: 7fad5a3d184294375e4fbbc6a19a40bffe1c841a4200ab6bd1312e8c8aceeccb
---

# Laguna S 2.1 goes Greek: a repository-scale game transformation

AI models
# Laguna S 2.1 goes Greek: a repository-scale game transformation

We put Poolside’s new Laguna S 2.1 model to the test, tasking it with a repository-scale transformation of the open-source game Hypersomnia.


- Authors
- Date
- August 3, 2026

TLDR

We tested a repository-scale transformation to see whether an agent could understand an unfamiliar codebase, coordinate changes across files and tools, and continuously verify its work. Poolside Laguna S 2.1, now available on Baseten Dedicated Inference, took on the challenge with a mythological twist.

We gave Poolside Laguna S 2.1 a simple task: transform [Hypersomnia](https://hypersomnia.io/), a free and open-source multiplayer top-down shooter game, from neon cyberpunk style into an Ancient Greek odyssey. To do this, Laguna had to understand a complex codebase, coordinate work across multiple AI models, and continuously verify its changes to ensure the gameplay was intact.

This post follows Laguna from its first pass through the repository to the final playable build. Along the way, we examine how it orchestrated specialized models, scaled generated assets across hundreds of sprites, preserved the game’s technical constraints, and decided when *not* to use an available tool.

[Laguna S 2.1](https://www.baseten.co/library/laguna-s-21/) is Poolside’s latest model for agentic coding and long-horizon work:

- 118B-parameter Mixture-of-Experts architecture, with 8B parameters activated per token
- Up to a 1 million token context window
- Thinking and no-thinking modes

In Poolside’s [published evaluations](https://poolside.ai/blog/introducing-laguna-s-2-1), Laguna S 2.1 performed competitively with substantially larger models on agentic coding benchmarks.

| Benchmark | What it measures | Poolside Laguna S 2.1 (Thinking) | DeepSeek-V4-Pro Max | Thinking Machines Inkling | 
|---|---|---|---|---|
| Size | Model scale based on total and active parameters | 118B-A8B | 1.6T-A49B | 975B-A41B | 
| Terminal-Bench 2.1 | Execution of practical, multi-step terminal tasks | 70.2% | 61.8% | 63.8% | 
| SWE-Bench Pro (Public Dataset) | Resolution of bug reports and feature requests in large, existing codebases | 59.4% | 52.6% | 54.3% | 

Benchmarks can measure coding and tool use, but they cannot fully show whether a model can navigate an unfamiliar codebase, make creative decisions, and recover when an approach fails. This repository-scale transformation put those capabilities to a more practical test.

Before making any changes, Laguna had to understand the codebase’s architecture, dependencies, asset pipeline, and undocumented assumptions. It then had to:

- Coordinate changes across interdependent files.
- Call the right tools and external models at the right time.
- Build and test continuously, diagnosing failures rather than merely detecting them.
- Revise the plan without drifting from the original task.

The [Hypersomnia codebase](https://github.com/TeamHypersomnia/Hypersomnia) is built from scratch in modern C++ without a commercial engine; the open-source game spans 715 compiled source files that power everything from gameplay and networking to physics, visual assets, and an in-game map editor.

That scale turned a playful, creative brief into a tightly constrained engineering task. Laguna had to transform the game’s neon cyberpunk identity into an Ancient Greek odyssey by modifying code, in-game text, configuration, and hundreds of visual assets. And it managed to do it without changing its simulation, geometry, networking, or core gameplay.

Unlike a bounded bug fix, this task combined creative ambiguity with technical interdependence across an entire repository.

To make the test even more compelling, we added another wrinkle. Rather than ask Laguna to do everything itself, we deployed three supporting models on [Baseten Dedicated Inference](https://www.baseten.co/products/dedicated-inference/):

- [Step 3.7 Flash](https://www.baseten.co/library/step-37-flash/), a fast vision-language model built for high-volume agentic work
- [Krea 2 Turbo](https://www.baseten.co/library/krea-2-turbo/), a text-to-image model built for fast, high-quality image generation
- [NVIDIA Cosmos 3 Nano](https://www.baseten.co/library/cosmos3-nano/), an 8B world foundation model built for text-to-video and image-to-video generation

Running them on dedicated deployments meant Laguna could call them as often as the task required without budget constraints, but Laguna also had to choose the right model for each job, turn its output into something the repository could use, and keep every contribution from breaking the game.

After 98 minutes and 58 seconds of autonomous work in [pool](https://github.com/poolsideai/pool), Poolside’s coding agent, Laguna S 2.1 produced “Hyperion,” an Ancient Greek-themed proof of concept that successfully launched Hypersomnia’s single-player tutorial.

The run at a glance:

- Laguna token usage: 76.33M input tokens and 449.5K output tokens
- Context used: 590.5K of 1.05M tokens (56%)
- Supporting model usage: 15 vision-language model calls (Step 3.7 Flash) and 100 image-generation requests (Krea 2 Turbo), with 53 successful image generations
- Assets modified: 954 PNG sprites, composited from 53 generated images
- Code and config files modified: 34 .cpp, 15 .h, 7 .hpp, and 8 JSON files

The result was playable, but not production-ready. Hyperion could not connect to existing Hypersomnia multiplayer servers. It did launch the single-player tutorial successfully, confirming that the new assets worked with the core gameplay.

The playable tutorial was the final frame of a more layered story where delegation, revision, and a careful balance between creative ambition and technical restraint helped shape the path to get there. That judgment surfaced in three ways: Laguna directed Step’s language work, scaled Krea’s visual outputs, and recognized that Cosmos had no role in the game itself.

Laguna tasked Step 3.7 Flash with adapting the game’s language to the Ancient Greek theme. It specifically prompted Step to “produce a Greek-themed replacement with playful absurdity, NO profanity, kept SHORT and understandable.”

Rather than applying Greek names at random, Step translated each term according to its role in the game. Factions kept their power relationships, character classes remained recognizable, and objectives and game modes preserved their original meaning even as the language became more mythic.

| Original: Hypersomnia | New: Hyperion | Re-theming rationale | 
|---|---|---|
| Metropolis | Athens | Metropolis is the established center of power. Athens preserves that role as Ancient Greece’s most recognizable political and cultural capital. | 
| Atlantis | Sparta | Atlantis is Metropolis’s formidable rival. Sparta conveys the same sense of disciplined military strength and creates a natural counterweight to Athens. | 
| Resistance | Thebes | The Resistance is the underdog willing to challenge larger powers. Thebes fits that role as a smaller polis that rose to defy the dominant forces around it. | 
| Commando | Hoplite | A commando is an elite frontline soldier. Hoplite gives players an equally recognizable Greek warrior archetype without changing the role’s function. | 
| Bomb | Sacred Flame | The bomb is the dangerous object at the center of the match. Sacred Flame preserves that sense of urgency while recasting the objective as a volatile ritual element. | 
| Gun Game | Gauntlet of Arms | Gun Game challenges players to advance through a sequence of weapons. Gauntlet of Arms reframes the same progression as a mythic trial while keeping the focus on weapon mastery. | 

Laguna remained the final editor. When Step returned Greek-language copy that would be inaccessible to most players, Laguna rewrote it in clear English while preserving the mythic tone. Its role went beyond delegation, and it judged whether each output served the larger goal.

Krea 2 Turbo served as the artist, while Laguna acted as visual director. For each asset Krea generated, Laguna defined the color palette, style, and key details in a tailored prompt:

| Prompt prefix | 
|---|
| “ancient Greek themed game asset, flat vector heraldic illustration, bold clean lines, 2D sprite style, white background or transparent,” | 

| olive\_branch | bronzeMetal | coin\_obol | 
|---|---|---|
| "single olive branch with leaves and tiny olives, flat vector, green & gold, transparent background” | "aged bronze metal texture, warm brown with teal patina highlights, seamless tileable” | "Greek obol silver coin with-face groove edge, flat vector, silver, transparent bg, top-down” | 

Laguna then applied this visual language across hundreds of assets without breaking the game. Instead of asking Krea to generate every sprite, Laguna built a reusable library of Greek materials from a smaller set of outputs. It composited that library across roughly 945 sprites with faction-specific colors, reducing model calls while keeping the visual language consistent. Each composite preserved the original sprite’s exact dimensions and transparency mask, keeping the asset pipeline, pivots, and collision geometry intact so the game could still compile and run.

For high-visibility assets such as the Hyperion logo, Laguna also commissioned Krea for bespoke “hero” generations. However, for the final build, it chose the validated composites over the more experimental, fully regenerated images. This was a deliberate tradeoff in favor of a stable, playable build.

Laguna’s judgment also showed in the model it chose not to use. Although Cosmos 3 Nano was available for video generation, Laguna found no natural role for video in the game. Adding a cutscene simply to use the model would have expanded the scope without improving the re-theme, so Laguna left Cosmos out. Laguna prioritized matching efficiency rather than maximizing the number of calls.

Later, we found a clear use case outside the game: a playful intro cutscene for this blog. Laguna used Cosmos to produce the GIF below:

Ancient Greece is no joke. But after 98 minutes and 58 seconds, we are proud to report that the marble was intact, the spells still cast, and we were able to launch *Hyperion* into a playable tutorial.

The result showed that Laguna could carry a creative brief across a complex repository, orchestrate specialized models, and make the tradeoffs needed to keep the project running (like not calling models it didn’t need).

[Laguna S 2.1](https://www.baseten.co/library/laguna-s-21/) is now available on Baseten Dedicated Inference. Have a framework migration stuck in your backlog? Give it the repository, define what cannot break, and let it plan, implement, and validate the change. Tell us how it goes!
