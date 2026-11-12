---
title: 'From prompt to production: Baseten inference in your IDE with Cline'
kind: blog
topic: null
subtopic: null
secondary_topics: []
summary: null
triage: null
skip_reason: null
source: baseten
url: https://www.baseten.co/blog/from-prompt-to-production-baseten-inference-in-your-ide-with-cline
author: Alex Ker
published: '2025-08-13'
fetched: '2026-11-12T06:13:58Z'
classifier: null
taxonomy_rev: 2
words: 517
content_sha256: d59cca8981cb350358de33c0b3d75cfbd38d82d45ae03ef552b53a82a9fb099b
---

# From prompt to production: Baseten inference in your IDE with Cline

AI engineering
# From prompt to production: Baseten inference in your IDE with Cline

Get started with Kimi K3, Qwen3 Coder, and DeepSeek R1 via Baseten with Cline


- Authors
- Date
- August 13, 2025

Cline is an open-source AI coding assistant that transforms your development workflow by bringing powerful language models directly into your favorite IDE. With our new Cline integration, you can now leverage cutting-edge models like DeepSeek R1, Kimi K3, and Qwen3 Coder to accelerate your coding projects with enterprise-grade performance and reliability.

This integration brings together Cline's intuitive coding interface with Baseten's robust model serving infrastructure, giving you access to state-of-the-art open-source models optimized for different coding workflows.

Before starting, you'll need:

1. **Cline installed** in your IDE. Add Cline to your development environment by visiting [cline.bot](https://cline.bot) and following the installation instructions for your preferred IDE.
2. **A Baseten account** for Model APIs access. Sign up at [baseten.co](https://baseten.co) to get started.

Step 1: Open your IDE and activate the primary sidebar (you can use the Command+B shortcut on macOS).

Step 2: Click the up arrow to expand the sidebar options and select the Cline icon to open the assistant interface.

You should see a window like this open.


Step 3. Click the gear icon in the Cline interface to access configuration options. From the API Provider dropdown, select "Baseten" as your model provider. Navigate to [app.baseten.co/settings/api\_keys](https://app.baseten.co/settings/api_keys) to generate your API key and copy it into the Baseten API Key field. You can select from the model dropdown your preferred model to code with. We recommend Qwen3 Coder for this tutorial. Then click “Done” to save the settings.

You can now start prompting the AI in either Plan or Act mode. For example, we can use the prompt “generate flappy bird in one file and launch the game!” to one-shot a version of Flappy Bird you can play in your browser.

In the Cline interface, you can choose between "Plan" and "Act" modes:

- **Plan mode** will gather information to architect a plan
- **Act mode** immediately begins implementation based on your prompt

For our Flappy Bird example, try this prompt under act mode.

\`Generate flappy bird in one file and launch the game!\`

Watch as the AI assistant:

1. Analyzes the requirements for a Flappy Bird implementation
2. Generates complete HTML, CSS, and JavaScript code
3. Creates game mechanics including physics, collision detection, and scoring
4. Produces a fully playable browser-based game

Different coding scenarios benefit from different models. For rapid prototyping and quick implementations, Qwen3 Coder's speed delivers fast iterations and immediate feedback. For complex system integrations, Kimi K3's function calling excels with APIs, webhooks, and multi-service architectures across long, multi-step agentic workflows. For comprehensive analysis and reasoning-heavy tasks, DeepSeek R1 provides thoughtful code reviews, architectural suggestions, and detailed problem-solving across multiple programming languages.

Feel free to experiment with our full list of supported models—all accessible with a single Baseten API key.

Whether you're building a weekend prototype or enterprise software, Baseten's robust, lightning-fast inference infrastructure can power your development workflow through Cline. We can't wait to see what you create.
