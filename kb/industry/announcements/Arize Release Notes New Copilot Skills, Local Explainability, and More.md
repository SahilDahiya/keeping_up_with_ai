---
title: 'Arize Release Notes: New Copilot Skills, Local Explainability, and More.'
topic: industry
subtopic: announcements
secondary_topics:
- evals-observability/monitoring
summary: Arize release notes covering new Copilot skills, local explainability, and
  other model observability improvements.
source: arize
url: https://arize.com/blog/arize-release-notes-new-copilot-skills-local-explainability-and-more/
author: Sarah Welsh
published: '2024-11-07'
fetched: '2026-07-11T04:50:28Z'
classifier: codex
taxonomy_rev: 1
words: 388
content_sha256: f7ad97c9e870a12b16304fd6f8d0b48ce83776651b356fd91c2c87914f8b916e
---

# Arize Release Notes: New Copilot Skills, Local Explainability, and More.

![Release notes 11-7 Arize logo with text and reads: Release notes, November 7, 2024](https://arize.com/wp-content/uploads/2024/11/Release-notes-11-7-1021x560.jpg)

              # Arize Release Notes: New Copilot Skills, Local Explainability, and More.

Welcome to our regular update on new releases, enhancements, and changes.

## What’s New

### New Copilot Skills

**Custom Metric Skill**: Copilot now writes custom metrics! Users can generate their desired metric by having copilot translate natural language descriptions or existing code (e.g., SQL, Python) into AQL. [Learn more](https://docs.arize.com/arize/llm-monitoring-and-guardrails/custom-metrics-api/arizeql-generator)

![Custom metrics](https://arize.com/wp-content/uploads/2024/11/custom_metrics.gif)


**Embedding Summarization Skill**: Copilot now works for embeddings! Users can select embedding data point and Copilot will analyze for patterns and insights. [Learn more](https://docs.arize.com/arize/computer-vision-cv/how-to-cv/embedding-summarization)

![cluster summarization](https://arize.com/wp-content/uploads/2024/11/cluster_summarization.gif)


## Enhancements

### Local Explainability Report

Local Explainability is now live, providing both a table view and waterfall style plot for detailed, per-feature SHAP values on individual predictions. [Learn more](https://docs.arize.com/arize/machine-learning/how-to-ml/explainability/interpreting-and-analyzing-feature-importance-values#local-feature-importance)

![](https://arize.com/wp-content/uploads/2024/11/local_explainability.gif)


### Experiment Over Time Widget

This widget allows users to integrate experiment data directly into their dashboards for ongoing visibility and analysis. Users can now:

- Select dataset of interest
- Choose specific evaluations they want to visualize over time
- Complete with direct connectivity to experiment details, making it easy to access the individual experiment results

![](https://arize.com/wp-content/uploads/2024/11/experiment_widget.gif)


### Full Function Calling Replay in Prompt Playground

Now users can follow the full [function calling tutorial](https://platform.openai.com/docs/guides/function-calling) from OpenAI and iterate on different functions in different messages from within the Prompt Playground.

![full function calling replay](https://arize.com/wp-content/uploads/2024/11/full-function-calling-replay.avif)


### Instrumentation Enhancements

- **Context Attribute Propagation**: Arize now has a set of utilities (eg: using_session) that allow users to set properties on context. All of these properties will be picked up by all of our auto instrumentations and added to spans.- [Learn more](https://docs.arize.com/arize/llm-tracing/how-to-tracing-manual/hybrid-instrumentation#add-attributes-to-multiple-spans-at-once)
- **Typescript Trace Configuration**: Typescript auto instrumentations now accept a trace configuration which allows for data masking and configuration of attribute values on spans.- [Learn more](https://docs.arize.com/arize/llm-tracing/how-to-tracing-manual/masking-span-attributes)
- **Vercel AI SDK**: Users can now ingest traces created by the Vercel AI SDK into Arize.- [Learn more](https://docs.arize.com/arize/llm-tracing/tracing-integrations-auto/vercel-ai-sdk)
- **LangChain Auto Instrumentation**: Arize’s LangChain auto instrumentation now supports langchain.js version 0.3 and is backwards compatible with all previous versions.- [Learn more](https://docs.arize.com/arize/llm-tracing/tracing-integrations-auto/langchain)

## 📚 New Content

The latest video tutorials, paper readings, ebooks, self-guided learning modules, and technical posts:

🧑🏫 [Prompt Optimization Course](https://arize.com/course/prompt-optimization/)

📊 [Evaluation Workflows to Accelerate Generative App Development and AI ROI](https://arize.com/blog/arize-vertex-ai-api/)

🐝 [Swarm: OpenAI’s Experimental Approach to Multi-Agent Systems](https://arize.com/blog/swarm-openai-experimental-approach-to-multi-agent-systems/)

✏️ [LLM Evaluation Course](https://arize.com/llm-evaluation/)

🤖[Techniques for Self-Improving LLM Evals](https://arize.com/blog/techniques-for-self-improving-llm-evals/)
