---
title: How Portola empowers subject matter experts to improve AI quality
topic: product-engineering
subtopic: case-studies
secondary_topics:
- evals-observability/evaluation
summary: Case study of Portola using subject-matter experts to improve AI quality
  through review workflows, datasets, and eval-driven iteration.
source: braintrust
url: https://www.braintrust.dev/blog/portola
author: null
published: '2026-01-01'
fetched: '2026-07-11T04:33:21Z'
classifier: codex
taxonomy_rev: 1
words: 1325
content_sha256: 0723b9318ee6b067d8bbd439d2727d1425ce8087db233f406e82153d9b78e44c
---

# How Portola empowers subject matter experts to improve AI quality

With [Quinten Farmer](https://www.linkedin.com/in/quintendf/), Founder & CEO and [Lily Doyle](https://www.linkedin.com/in/liliandoyle/), Research & Product

4x

Faster prompt iteration

0

Engineering handoffs

Portola builds [Tolan](https://www.tolans.com/), an AI companion app that serves as an alien best friend for users seeking authentic, non-romantic AI relationships. Unlike typical chatbots or productivity assistants, Tolan focuses on creating genuine emotional connections through natural voice conversations and complex memory systems. As Portola's team built an AI that users could truly trust, they realized that the nuances of conversation quality, emotional intelligence, and authentic behavior couldn't be captured by automated evals alone.

![Tolan characters](https://www.braintrust.dev/customers/stories/portola/tolan.jpg)


In this case study, we'll explore how Portola structured their workflow to empower nontechnical subject matter experts, including a behavioral researcher, science fiction writer, and game designer, to spend hours daily reviewing logs, curating datasets, and shipping prompt improvements directly to production without engineering bottlenecks.

"How will humanity build healthy relationships with AI?" asks Quinten Farmer, Portola's CEO. "That's the question Tolan explores."

Creating an AI companion that feels authentically human demands deep domain expertise in psychology, storytelling, and conversation design. The team identified three critical factors for building user trust in their AI companion:

The memory system needs to work in a way that feels authentic to how a friend would remember things. Perfect recall matters less than the subtle nuance of what gets remembered, when it surfaces naturally, and how it integrates into conversations. "When you're chatting with your Tolan and they remember some detail about your life and bring it into the conversation, it feels really special," Quinten explains.

How Tolan reflects and responds to user emotions and communication styles must feel natural, not algorithmic. This involves vocabulary choices, conversation pacing, and emotional resonance that can't be reduced to simple metrics.

Certain question patterns and engagement behaviors immediately signal "this is AI" to users, breaking the illusion of authentic connection. Patterns like asking too many "or questions" ("Would you rather have waffles or pancakes?") or using excessive Gen Z slang need constant monitoring and adjustment.

The technical complexity of Portola's system compounds these challenges. Their prompting pipeline integrates memory retrieval, dynamically generated user context, real-time voice processing, and content that users share (like photos) into a cohesive conversation flow. There's a subjective, contextual quality that makes conversations feel authentic.

Portola built a workflow that enables subject matter experts to identify issues, curate datasets, test solutions, and deploy changes-- all without engineering handoffs. Here's how it works:

4x faster iteration

Pattern identification

Dataset curation

Playground iteration

Direct deployment

Lily Doyle, their behavioral researcher, spends about an hour each day reading through chat logs in Braintrust, looking for patterns in conversation quality. "I look for recurring patterns in form and function. That means both how the messages are sent and what the Tolan is actually saying. I also watch for any signs of user frustration," Lily explains.

When Lily identifies a recurring problem through log reviews, user feedback, or focus group sessions, she creates a dataset in Braintrust tagged with the specific issue. Each dataset becomes a collection of real conversation examples that demonstrate a particular problem.

Recent examples of issues she's tracked in Braintrust include:

- `somatic-therapy`
- `or-questions`
- `gen-z-lingo`

Rather than maintaining a single "golden dataset," Portola creates problem-specific datasets in Braintrust ranging from 10 to 200 examples. "It feels useless to come up with a golden dataset," Lily explains. "We're on a different model, we've changed the prompt eight times. Things change so fast."

Braintrust's dataset management enables several technical advantages for Portola:

- **Focused iteration**: Each dataset targets a specific behavioral pattern, making it easier to measure improvements
- **Fresh data**: Datasets reflect current product state rather than becoming stale snapshots
- **Rapid response**: New issues can be addressed immediately without updating comprehensive test suites
- **Context preservation**: Each dataset maintains the full conversation context through Braintrust's trace storage

Once a dataset is curated, Lily moves to playgrounds for side-by-side prompt comparison. She manually reviews outputs from the current prompt versus iterations, assessing conversation quality through her domain expertise.

"A lot of what we're working on is really squishy stuff," Lily explains. "Things like asking the best question to the user for the context they gave you—that's not super eval-able. For things that tend to be squishier, I prefer to do it manually and use my own judgment."

This manual evaluation approach stands in contrast to typical ML workflows, but it's intentional. For Portola, conversation quality is fundamentally subjective and context-dependent. An automated scorer might flag a response as too long, but miss that the length created emotional resonance in that specific context.

Playgrounds serve as Lily's primary workspace, where she:

- Loads datasets directly from curated logs
- Runs comparison tests between prompt versions
- Reviews outputs holistically, considering tone, appropriateness, and emotional intelligence
- Takes notes on specific failures or edge cases
- Iterates with AI to refine prompts

The final piece of Portola's workflow is their prompts-as-code infrastructure, which enables subject matter experts to deploy changes directly to production once they're satisfied with playground results.

Our science fiction writer can sit down, see something he doesn't like, test against it very quickly, and deploy his change to production. That's pretty remarkable.


This end-to-end autonomy transformed Portola's iteration velocity. Nontechnical subject matter experts own the full cycle from problem identification to production deployment.

SME identifies issue

Write ticket for eng

Wait for eng review

Eng implements change

SME reviews again

Deploy to production

Week-long cycle

Before implementing this workflow, prompt changes required coordination between subject matter experts and engineers. Now, domain experts identify issues, create datasets, test solutions, and ship changes, resulting in **4x the number of weekly prompt iterations**.

The team has systematically addressed edge cases in:

- Memory system behavior and authentic recall patterns
- Natural conversation flow and question patterns
- Brand voice consistency across different contexts
- Appropriate handling of sensitive topics like mental health

The workflow also enabled Portola to quickly handle model transitions, rapidly identifying and fixing regressions when switching to new models.

Portola's approach demonstrates that building trustworthy AI systems for subjective, emotionally-complex domains requires empowering nontechnical domain experts to drive quality improvements. Their workflow offers several lessons:

"Scores are useful, but a lot of what we're working on is really squishy stuff," Lily notes. For conversation quality, emotional intelligence, and brand voice, human judgment from domain experts is just as important as automated metrics.

Instead of maintaining comprehensive test suites that grow stale, create focused datasets for specific issues as they arise. This maintains agility while building institutional knowledge about edge cases and failure modes.

When building AI for emotionally complex domains like companion relationships, mental health support, or therapeutic contexts, manual review from domain experts is essential. The nuances that make these interactions work can't be captured by metrics alone.

Budget time for subject matter experts to spend hours reviewing real usage, and use tools like human review in Braintrust to make that time productive.

Portola's workflow demonstrates that the teams best positioned to improve AI quality might be the nontechnical domain experts who understand the nuances of the user experience you're trying to create. By building infrastructure that empowers a behavioral researcher, science fiction writer, and game designer to identify issues, curate datasets, iterate on prompts, and deploy changes directly to production, Portola achieved a 4x improvement in iteration velocity while systematically improving conversation quality.

If you're building AI for subjective, emotionally complex domains where automated evals can't capture what makes interactions truly work, take a page from Portola's playbook. Invest in observability, build problem-specific datasets, and empower your domain experts to own the quality improvement cycle end-to-end.

Learn how Braintrust can support manual review workflows alongside traditional evals.

“Loop was our way of getting data or synthesizing log data more efficiently at an aggregate level. We use it to find common error patterns every single week.”

Allen Kleiner, AI Engineering Lead

5%

Reduction in negative rules

45x

More feedback with AI grading
