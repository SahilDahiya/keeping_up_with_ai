---
title: 'Measuring what matters: An intro to AI evals'
topic: evals-observability
subtopic: evaluation
secondary_topics:
- evals-observability/testing
summary: Intro to AI evals focused on choosing metrics that reflect product quality,
  building datasets, and measuring what matters for users.
source: braintrust
url: https://www.braintrust.dev/blog/measuring-what-matters
author: Braintrust Team
published: '2025-10-10'
fetched: '2026-07-11T04:33:01Z'
classifier: codex
taxonomy_rev: 1
words: 1685
content_sha256: 8e5887966f5267c0c07fd2a2681cbe29edf7f7975bcc3913f37b2c28ec4c3bd5
---

# Measuring what matters: An intro to AI evals

10 October 2025Carlos Esteban9 min

*This post is based on an online event on October 7, 2025. You can watch the full replay on  YouTube.*

AI systems are non-deterministic. Give an LLM the same question twice, and you'll get different answers. This randomness creates a fundamental problem: how do you know your changes improved quality instead of just shifting failure modes around?

Without a systematic evaluation process, teams build on vibes. You ship blind, fix one issue only to break another, and wonder which model performs best. You capture user feedback but can't integrate it into development. The questions pile up: Which LLM should I use? How do I catch hallucinations? When something breaks, where do I look?

Evals answer these questions. They give you statistical confidence that your changes work, catch regressions before users do, and create a process for continuous improvement. Here's how to build them.

Every eval in Braintrust follows this structure:

python

```
from autoevals import Levenshtein
from braintrust import Eval
Eval(
    "My Project",
    data=lambda: [
        {"input": "Hello", "expected": "Hi"},
        {"input": "Goodbye", "expected": "Bye"},
    ],
    task=lambda input: call_my_llm(input),
    scores=[Levenshtein],
)
```
Let's break down each component:

The task is your subject of evaluation -- the thing you're testing and iterating on. Start simple with a system prompt, but scale to whatever complexity you need: a chain of prompts, a full agent, or a multi-step workflow. The only requirement is that your task takes an input and produces an output.

For example, you might start with a basic prompt like "You are a helpful customer support agent" and test how it handles common questions. As you identify issues, you'll iterate: add retrieval for knowledge base articles, adjust the tone to be more empathetic, or incorporate tools for order lookups. The eval process shows you how each change affects your scores downstream.

Your dataset contains examples of how end users actually interact with your AI application. This isn't hypothetical -- it's real questions, real edge cases, real failure modes you didn't anticipate when you started.

Start small. Five to ten examples representing your main persona is enough to get started. The goal is reaching the eval phase fast, because evals expose weaknesses and drive actions that improve performance. As you gather production feedback and identify issues, feed those examples back into your dataset. Over time, this scales to hundreds of cases covering the full range of user interactions.

This becomes your golden dataset -- the comprehensive test suite you run before any production deployment. It catches regressions across all the ways users interact with your product.

Scores define what you care about and what you want to measure. Unlike unit tests with strict pass/fail criteria, eval scores return values between 0 and 1 -- a percentage that gives you flexibility in analysis and insight gathering.

Start with **code scores**. These are deterministic, cheap, and familiar to engineering teams. They're perfect for quantitative checks:

python

```
def conciseness_scorer(output: str, **kwargs) -> int:
    # Penalize responses over 200 tokens
    return 1 if len(output.split()) <= 200 else 0
def has_quotes_scorer(output: str, **kwargs) -> int:
    # Check for quotation marks (not apostrophes)
    import re
    return 1 if re.search(r'[""]', output) else 0
```
But code scores can't capture everything. For subjective qualities like tone, helpfulness, or factual accuracy, you need **LLM judges**:

python

```
project.scorers.create(
    name="Tone scorer",
    messages=[
        {
            "role": "user",
            "content": """Does the response maintain a professional yet empathetic tone?
Response: {{output}}
Choose:
A) Professional and empathetic
B) Professional but cold
C) Unprofessional""",
        }
    ],
    model="gpt-4o",
    choice_scores={"A": 1, "B": 0.5, "C": 0},
)
```
The key is aligning your LLM judge to human judgment through careful prompt design and validation.

Think of scores as the backbone of your eval. Each score should measure one dimension on a 0-1 scale, giving you clear signal on specific aspects of your AI's performance.

The biggest mistake teams make is kicking off an MVP without articulating requirements. This leads to going back to the whiteboard and restarting the process. Instead, define what success looks like upfront. Be specific about your success metrics and what you want to achieve.

This clarity creates an improvement target. When you know what you want, the path to get there becomes obvious. It also bridges the product-engineering gap. Product teams excel at defining success criteria (it's essentially a PRD) -- for example, "responses must include relevant citations," "tone should be empathetic but not apologetic," or "answers must address all parts of multi-part questions." Engineers then implement the evaluation infrastructure and ensure production data flows into the eval loop.

Begin with end-to-end evals where your agent or workflow runs completely, and you evaluate the final output. Ask: Did the agent accomplish its goal? This broad evaluation solves many problems without complexity.

As your system grows more complex with intermediate steps, you'll need single-turn or step-by-step evals. Was this the right tool call? Were the arguments correct? By evaluating each step along the way, you pinpoint what caused errors and fix the root cause instead of guessing.

For example, in a RAG use case, evaluate the retrieval step separately. Did it fetch the right documents? Were they relevant? This granular approach reveals exactly where your pipeline breaks down.

Follow these guidelines for scoring functions that actually work:

-
**One dimension per score**: Don't try to measure factuality, conciseness, and tone in a single score. It confuses the LLM and makes human review harder. If you're checking five criteria, create five separate scores.
-
**Start binary**: Use 0 or 1 initially. Does the response meet the threshold? Yes (1) or no (0). This makes review straightforward and alignment clear.
-
**Set harsh thresholds**: If you're passing 100% of your evals, you're not setting the bar high enough. Low scores are okay -- they're a sign you're measuring what actually matters. Make your evals fail initially, then improve your way to higher scores.
-
**Use production feedback**: When you spot patterns in your logs -- repeated failures, edge cases, user complaints -- create dedicated scores for them. Each production issue should become its own dimension to measure and prevent.

For example, say your application struggles to use a calculator tool when it should. You might have only one test case requiring calculator use, but production shows it's a common failure. Add 5-10 targeted examples that specifically require calculator use, then create a scorer to test tool usage. Similarly, if users report your chatbot keeps apologizing unnecessarily, create a scorer that penalizes responses containing "I'm sorry" or similar phrases.

A support chatbot might ultimately have separate scores for factuality (does it answer correctly?), tone (is it helpful and friendly?), conciseness (under X tokens?), and format compliance (follows the template?). Each dimension gets its own score.

The most powerful eval strategy connects production data back to your development process. Here's how it works:

- **Production**: Your AI app runs with automatic logging
- **Capture failures**: Users report issues or you spot patterns in monitoring
- **One-click test cases**: Convert production traces to dataset rows instantly
- **Rapid iteration**: Test fixes in the playground, compare side-by-side
- **Quality gates**: Run evals in CI/CD to verify fixes don't break other cases
- **Deploy with confidence**: See quality scores on every commit
- **Continuous monitoring**: Production traces feed back into your eval suite automatically

This creates two feedback loops: a fast inner loop (evals → iterate → evals) where you rapidly test prompt changes, and a larger outer loop (production → datasets → evals → production) that ensures real-world usage continuously improves your product.

Teams with this process in place adopt new models within 24 hours of release. When a user complains, that interaction becomes a test case immediately. Feature ideas get validated with evals before shipping to users.

Here's what successful teams do:

**Start simple, but start now**. One score with 5-10 test cases is enough. You can expand from there. The friction is starting, so lower the barrier as much as possible.

**Make evals part of your workflow**. When a user complains in any channel, add it to a dataset. When a new model drops, run your evals immediately. When you think of a new feature, validate it with evals first. Invest in the process so these actions become automatic.

**Integrate CI/CD**. Automate your evals so every pull request shows quality scores before merge. Set up quality gates that block degraded prompts from reaching production:

bash

```
# Run evals on every commit
npx braintrust eval my-evals/
# Or use the GitHub action
- name: Run Evals
  uses: braintrustdata/eval-action@v1
  with:
    api_key: ${{ secrets.BRAINTRUST_API_KEY }}
    runtime: node
```
Make the eval loop as frictionless as possible.

**Optimize the whole system**. Don't just tweak prompts. Evaluate intermediate steps, tool outputs, retrieval quality, context formatting. Everything that influences the final response deserves measurement and optimization. For instance, in a RAG system, switching a tool's output format from JSON to YAML might double its success rate because YAML is shorter, easier for the model to parse, and uses fewer tokens. These context optimizations often move the needle more than prompt tweaks alone.

**Embrace imperfection**. Evals are hard. Your scores will be approximations, and that's fine. The goal isn't perfect measurement -- it's systematic improvement as you iterate. Data can be noisy, scores can fluctuate, and you'll still ship better products than teams building on vibes.

With evals in place, you'll shift from hoping your changes work to knowing they work. You'll catch hallucinations systematically instead of discovering them in user complaints. You'll compare models based on real performance data instead of marketing claims. You'll turn every production failure into a test case that prevents future regressions.

The complete development loop -- from production traces to evals and back -- is how leading AI teams ship verified quality improvements instead of building on vibes. It's how Notion increased from fixing 3 issues per day to 30. It's how Zapier improved AI products from sub-50% accuracy to 90%+ within 2-3 months.

Start simple. Build the process. Measure as you iterate. That's how you ship AI products with confidence.

To learn more about Braintrust, [sign up](https://www.braintrust.dev/signup) or [book a demo](https://www.braintrust.dev/contact).
