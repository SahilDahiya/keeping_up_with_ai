---
title: Turn production data into better AI with Loop
topic: evals-observability
subtopic: monitoring
secondary_topics:
- product-engineering/architecture
summary: Explains Loop as a way to turn production data into AI improvements through
  review, labeling, datasets, and feedback-driven iteration.
source: braintrust
url: https://www.braintrust.dev/blog/loop
author: Braintrust Team
published: '2025-11-24'
fetched: '2026-07-11T04:32:55Z'
classifier: codex
taxonomy_rev: 1
words: 753
content_sha256: 586e89bf094c0d246341d0f6b2836cb84293d99570955105a6215e93bd0448cc
---

# Turn production data into better AI with Loop

24 November 2025Ornella Altunyan5 min

Understanding what's happening in production and deciding what to fix next remains one of the hardest parts of AI development. You have dashboards showing error rates and latency. But when something breaks or quality drops, you have to dig through logs, write complex queries, and manually hunt for patterns.

Loop is an AI assistant built into Braintrust that helps you go from "something's wrong" to "here's what to fix."

Ask Loop questions in plain English and get actionable answers:

"What are the common failure modes of my agent?" → Loop surfaces patterns and recommendations instantly.

"Generate 5 more dataset rows" → Loop creates realistic test cases based on your production data.

"Prepare a report for stakeholders on product usage and satisfaction" → Loop analyzes trends and generates custom charts.

**Describe your query** and Loop will semantically search for the right traces to surface, even when you're not sure exactly how to filter for them.

**Generate BTQL** when you need precise filters. Describe what you want to see and Loop writes the query without needing to remember field names or syntax.

**Bootstrap scorers** directly from production traces. Found a failure pattern? Loop generates a scorer to catch similar issues in evals.

**Generate datasets** from production logs. Select problematic traces and Loop creates a focused dataset for regression testing.

**Analyze experiments** to understand what improved and why. Loop summarizes metrics, drills into specific eval rows, and surfaces insights across runs.

**Optimize prompts** with Loop's guidance on the Prompt detail page. Get suggestions for examples, run evals, and iterate faster.

**Generate custom charts** to visualize patterns in your data. On the Monitor page, ask Loop to create a chart, then share it with your team and stakeholders.

Loop is available wherever you work in Braintrust, including on Logs, Datasets, Experiments, Scorers, Prompt, Monitor, and Playground pages, via the Command Bar, and in the BTQL sandbox. You can edit and re-run messages, queue follow-ups, and use keyboard shortcuts.

Loop makes production data accessible to everyone on your AI team.

**For product managers**: Analyze production behavior without writing code. Ask Loop to surface patterns, identify high-impact issues, and generate insights and charts you can share directly with stakeholders. Turn qualitative feedback into measurable data and make informed roadmap decisions.

**For engineers**: Debug production issues in seconds instead of hours. Loop helps you query logs semantically, generate test cases from failures, and build scorers that catch issues before they reach production.

Teams use Loop to collaborate on the same production data. PMs identify issues worth prioritizing, engineers investigate root causes, and everyone shares a single source of truth.

Loop is our way of getting data or synthesizing log data more efficiently at an aggregate level. We use it to find common error patterns every single week.


Retool uses Loop every week to identify issues by impact, not just frequency, and make data-driven roadmap decisions. Loop helped them discover that multi-page support was their #1 user request and quickly prioritize fixes for context window overflow. [Read the story →](https://www.braintrust.dev/blog/retool)

We asked Loop to analyze itself (!) and collect interesting statistics about its performance and what teams are using it for. Here's what we found:

Loop has a **99.97% success rate** across all model calls. In the rare cases when tool calls fail, Loop's error handling and retry logic make sure conversations successfully complete.

Additionally, Loop works with several AI models that you can choose from depending on what you have added to your AI providers list in your organization. We found that the most commonly used model, comprising **42%** of Loop conversations, is `gpt-5-nano`.

Among all Loop usage, we found that **most teams use it in playgrounds**, with **30%** of conversations originating in that UI. Logs come in at a close second, with 26%.

Interestingly, the top 3 tools (`get_results`, `btql_query`, `edit_task`) account for 49% of all tool usage. Loop is best at querying, analyzing, and taking action on production data.

Loop is available for all Braintrust users. Here's how to get started:

- **Open any Logs page**and click the Loop icon to start querying your production data
- **Try searching**to find traces semantically without writing filters
- **Ask Loop to generate a dataset**that matches a specific use case, or to add edge cases
- **Use the Command Bar**(Cmd/Ctrl + K) to access Loop from anywhere

Loop works with all your existing Braintrust data. No setup required.

**Ready to turn your production data into better AI?** [Start using Loop →](https://www.braintrust.dev/app) or [book a demo →](https://www.braintrust.dev/contact)
