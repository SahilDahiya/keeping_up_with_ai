---
title: Genspark deep research agent with Fireworks RFT
topic: models
subtopic: reinforcement-learning
secondary_topics:
- agents/tool-use
- evals-observability/evaluation
summary: Case study of reinforcement fine-tuning a deep research agent to improve
  quality, tool calls, and cost.
source: fireworks
url: https://fireworks.ai/blog/genspark
author: null
published: '2025-10-31'
fetched: '2026-07-11T04:16:10Z'
classifier: codex
taxonomy_rev: 1
words: 1037
content_sha256: 95b705630776ad532e5067c8e95b00b5ca7425baf501d6ef080e90b8bee1619f
triage: keep
skip_reason: null
---

# Genspark deep research agent with Fireworks RFT

[Genspark](https://www.genspark.ai/), a leading innovator in the AI-powered application workspace, excels at delivering Agentic Full-Stack Web Applications, ranging from advanced Deep Research Search Agents to AI-generated Slides, Documents, and Sheets. By leveraging Fireworks’ Reinforcement Fine Tuning to train large state-of-the-art open models, in one month Genspark achieved 12% better quality and 33% more tool calls than a state of the art (SOTA) closed-source model , leading to a 50% cost reduction and superior answer quality.

*Note: These were measured by Fireworks AI

'Deep Research' AI agents are designed to perform complex, multi-step research tasks autonomously. The [Genspark Deep Research tool](https://www.genspark.ai/agents?type=agentic_deep_research) is an AI-powered agent designed to automate and streamline the process of conducting thorough, multi-source investigations and generating comprehensive, structured reports on a given topic. Genspark’s Deep Research tool puts together a team of the best AI Models to collaborate for you.

An example scenario would be if a user asks a query such as “Explore cutting-edge methods and tools that can be used to optimize inference“, the agent will try to use different tools in a skillful manner to derive a final research report about the query. The agent will repetitively append the tool call result to the messages and ask LLM to generate the next steps. The execution will stop when the agent collects enough information.

**The Challenge: Hitting the quality wall with closed source models**

Genspark's Deep Research application streamlines the process of going from a single query to a well-structured, multi-source report, saving you hours of manual work and allowing you to focus on the insights and analysis that matter most. Genspark’s goal was to drive the best quality, and user experience. They initially started with a SOTA closed source model, but faced challenges when they wanted to scale, and add more customization. Genspark required a Mixture of Agents(MoA) that required multiple tool calls that were very specific to their workload. This was challenging to do with a proprietary model, because the only way to do customization on a proprietary model would be to use prompt engineering . As they would like to provide a more comprehensive research report to their users , they wanted to customize their model by finetuning.

By leveraging Fireworks, Genspark aimed to use reinforcement learning to fine tune capable large open source models to build up a unique state-of-the art Deep Research Agent. Fireworks provided Genspark with three key capabilities to unlock improved quality, more tool calling, and 50% reduced cost.

Genspark’s CTO Kay Zhu said,“We are really excited to see what we were able to achieve partnering with Fireworks. Fireworks enabled us to own our AI journey, and unlock better quality in just four weeks. This resulted in a better user experience for our customers.”

Flame Zhou, Research Engineer at Genspark spoke about the collaboration,“We are excited to be partnering with Fireworks to deploy our Deep Research Agents using Fireworks. Outstanding work! We’ve achieved fantastic results with the post-training on Kimi-K2. We conducted a series of systematic benchmarks for the deep_research task, and the conclusions are really positive. It performed comparably to SOTA closed source models in detailed human evaluations. It uses tools more frequently and skillfully, which we are excited to see.”

**1.Seamless 1-Click transition from training to deployment with best in class performance on OSS models with reinforcement fine tuning. **

In order to fine-tune a large 1 Trillion Parameter Model like Kimi K2, powerful infrastructure combined with cutting edge hardware like NVIDIA H200 and B200 are required. The Genspark team needed a partner to help provide the infrastructure to deploy such a large model.

Fireworks removed the complexities with running fine-tuning on large models by providing a seamless managed service, deploying on new HW, and enabled best-in-class performance with Reinforcement Fine-tuning on NVIDIA’s B200 for Genspark’s open-source model of choice Kimi K2.

**2. Better quality and tool calling than a proprietary model**: allowed the Genspark team to inject more unique ideas directly into the model, and create richer answers.

Genspark's core agent orchestrates exploration and solutions by skillfully utilizing a diverse array of tools, which can include software, sub-agents, or other LLMs. The selection of LLMs is dynamically tailored to suit various use cases. To ensure optimal output for the Research Agent, Genspark used Fireworks’ Reinforcement Fine Tuning with their custom data set to significantly improve the quality compared to a SOTA closed source model.. Additionally, Genspark prioritizes maximizing tool call support, and with the RFT optimizations unlocked a 33% jump in tool calls. A greater number of supported tool calls directly enhances the user experience. The improved quality and higher number of tool calls resulted in a better Quality Answer to Genspark Deep Research Tool.

| Model | Reward Score | Average Number of Tool Calls |
|---|---|---|
| Closed Source Proprietary Model | .76 | 3.74 |
| Deepseek v3.1 | .69 | 2.78 |
| Qwen 235B A22B Instruct 2507 | .35 | 2.83 |
| Kimi-K2 Instruct Base 0905 | .65 | 2.86 |
| Kimi-K2 Fine Tune | .82 | 5 |

Table 1: Reward Quality Rate and Tool Call Count per Model on Fireworks

**3. Dedicated quality support from research engineers: **enabled Genspark** **to Own Their AI Journey

This commitment to providing quick and high-quality answers proved to be a game-changer. Genspark worked directly with one of our expert research engineers to help expedite their development. Whenever a technical question arose or an issue needed troubleshooting, the Genspark team could rely on Fireworks team to provide quick and high quality responses. This seamless support meant that the Genspark Engineers could focus on innovation and development without being slowed down by technical roadblocks. This expert level support enabled Genspark to deploy a complex optimized solution from POC to Production in 4 weeks.

The collaboration between Genspark and Fireworks significantly enhanced the Deep Research Tool's capabilities, delivering several key benefits:

- •**Seamless infrastructure for a 1 trillion parameter open-source model**: Eliminated the challenges of fine tuning and deploying on cutting-edge NVIDIA hardware
- •**Surpassed frontier closed source model in both quality and tool call performance with RFT:**Results in a 50% cost optimized higher quality response
- •**Accelerated time to production with premium support**: Went from POC to Production in 4 weeks
