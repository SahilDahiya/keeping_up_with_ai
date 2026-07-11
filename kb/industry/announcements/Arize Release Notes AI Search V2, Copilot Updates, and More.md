---
title: 'Arize Release Notes: AI Search V2, Copilot Updates, and More'
topic: industry
subtopic: announcements
secondary_topics:
- evals-observability/monitoring
summary: Arize release notes covering AI Search V2, Copilot updates, and related product
  improvements for observability workflows.
source: arize
url: https://arize.com/blog/arize-release-notes-ai-search-v2-copilot-updates-and-more/
author: Sarah Welsh
published: '2024-09-19'
fetched: '2026-07-11T04:50:02Z'
classifier: codex
taxonomy_rev: 1
words: 387
content_sha256: 38e3c043e3d90cb76a66308cd8626c89bbb88f1f11cc735598ae219550eedac2
---

# Arize Release Notes: AI Search V2, Copilot Updates, and More

![Release notes 9-19 Release Notes Title and Arize Logo](https://arize.com/wp-content/uploads/2024/09/Release-notes-9-19-1021x560.jpg)

              # Arize Release Notes: AI Search V2, Copilot Updates, and More

Welcome to our regular update on new releases, enhancements, and changes.

## What’s New

### AI Search V2

We’re excited to announce the release of AI Search V2, packed with new features and improvements designed to enhance the user experience.

Here’s what’s new:

- **Column Search**(Improved) The original AI search skill now offers refined semantic search capabilities within a single column based on user criteria. Try it out:- *“Find me confused inputs”*
- **Table Search**(New) Our newest skill allows users to search across multiple or all columns within a table, making it easier to catch patterns and outliers. Try it out:- *“Find inputs that reference pricing that are hallucinated”*
- **Text to Filter**(New) This skill generates precise query filters based on natural language commands. Simply use “filter by” to trigger it and narrow down data based on your needs. Try it out:- *“Filter by input contains SDK”*
- **LLM Analysis Lite**(New) This lightweight analysis skill helps users find patterns in their data and provides filter suggestions to improve their search results. Try it out:- *“What are the top 5 types of questions asked?”*

![Ai Search V2 screenshot](https://arize.com/wp-content/uploads/2024/09/Ai-Search-1024x657.png)


### Documentation Questions in Copilot

Copilot can now answer questions about the Arize product!

Try it out: *“How do I send in traces?”*

*Note: Arize has partnered with **Run LLM** to provide support via Copilot. Users must first authorize the use of Run LLM. Only the user’s question is sent to Run LLM, no other data will be included.*

[Learn more about annotations here.](https://docs.arize.com/arize/llm-evaluation-and-annotations/annotations)

## Enhancements

### Experiments Overview Visualization

There’s a new way to visualize experiment results on the Experiments Overview page. Users can now see up to the 10 most recent experiments and select which evaluations they’d like to visualize.

This is just the beginning of our investment in visualization tools, so stay tuned for more exciting updates!

![Experiments overview](https://arize.com/wp-content/uploads/2024/09/Experiments-overview.avif)


### Data API

Users can now query for drift over time using GraphQL.

### Admin API

Users can now query for organization users, update space membership or delete a user from a space.

## New Content

✏️ [Tracing a Groq Application](https://arize.com/blog/tracing-groq/)

🤖 [Composable Interventions for Language Models](https://arize.com/blog/composable-interventions-for-language-models/)

🧠 [Creating and Validating Synthetic Datasets for LLM Evaluation & Experimentation](https://arize.com/blog/creating-and-validating-synthetic-datasets-for-llm-evaluation-experimentation/)
