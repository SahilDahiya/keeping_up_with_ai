---
title: Build AI agents in production (without writing code)
kind: blog
topic: null
subtopic: null
secondary_topics: []
summary: null
triage: null
skip_reason: null
source: baseten
url: https://www.baseten.co/blog/production-ai-for-non-technical-knowledge-workers-langchain-agent-builder-with-gl
author: Alex Ker
published: '2026-01-14'
fetched: '2026-11-12T06:14:24Z'
classifier: null
taxonomy_rev: 2
words: 618
content_sha256: ad84c5d7e74aca3a2c348f9a997639ff44e97d0529ff0e7feb1a06bb77fb0af9
---

# Build AI agents in production (without writing code)

Community
# Production AI for non-technical knowledge workers: How to build agents with LangChain Agent Builder + GLM 4.7 on Baseten

Learn how to build AI agents that are fast and performant with natural language


- Authors
- Date
- January 14, 2026

What if you could describe an agent in English and have it running in production two minutes later? That's what LangChain's LangSmith Agent Builder does. It's a practical way to build AI agents without writing code. And with Baseten's GLM 4.7 LLM as the inference backbone, it runs extremely fast.

Now everyone can build, no matter their business function. But there remain a few barriers–picking the right tools to augment the quality and accuracy of output and iterating quickly to refine the agent to fit your workflow perfectly. This guide focuses on removing those barriers so you can build AI agents that work reliably.

Tell Agent Builder what you want, then it will write a detailed system prompt, select the appropriate tools, and can even spin up subagents to delegate portions of complex tasks. Under the hood, it continuously tool calls over long horizons to accomplish tasks.

In this guide, we’ll show how to build agents like a meal planning agent that fits your specific fitness, dietary requirements and other constraints so you can shop smoothly at a grocery store pulling in your favorite recipes from the web. You can similarly build other agents such as a LinkedIn Recruiter, Email Assistant, and many more following prebuilt templates in LangSmith (or create your own from a simple prompt).

Let’s get started.

Watch this video or follow the instructions below!

Before starting, you’ll need:

1. LangSmith account. Visit [https://smith.langchain.com/](https://smith.langchain.com/) to sign up.
2. A Baseten account for Model APIs access. Sign up [here](https://login.baseten.co/sign-up). In this example, we will be using GLM 4.7, the leading open source coding and reasoning model at time of writing.
3. A Tavily account for web search. Visit [https://www.tavily.com/](https://www.tavily.com/) to sign up.

Step 1. Open Agent Builder by clicking on the upper left side bar.

Step 2: Open the model selection dropdown and click add custom model.

Step 3: All Baseten Model API models are OpenAI compatible chat completion format so will select the default OpenAI API Spec.

**IMPORTANT**: Model ID field must match the slug on Baseten listed [here](https://docs.baseten.co/development/model-apis/overview). For GLM 4.7, the slug is `zai-org/GLM-4.7`. Enter any display name (we’ve used the same string as the model ID here for simplicity). Enter [https://inference.baseten.co/v1](https://inference.baseten.co/v1) for the Base URL.

Lastly, navigate to [app.baseten.co/settings/api\_keys](https://app.baseten.co/settings/api_keys) to generate an API key. Go back to Agent Builder, name the key BASETEN\_API\_KEY and paste generated key in. You only need to do this once and the API key will be saved in the Agent Builder environment. Click Save.

Step 4. Describe the agent in a short sentence such as “meal planning assistant”. Press enter and follow the Agent Builder questions that will help you narrow down the desired behavior of the agent. Then generate an agent instantly using Baseten Inference.

Step 5. Many agents, including this one, often use web search tools such as Tavily to improve the quality and accuracy of their answers. In this case you need to provide the API key in settings once the agent is created. Now you can use the agent!

Agent Builder in LangChain allows anyone to build no code AI agents quickly, automatically suggesting the right set of tools to enhance its capabilities and saving you the headache of writing massive system prompts. Agent Builder becomes even more capable when used in conjunction with open source models powered by Baseten Inference, one of the most cost efficient and performant API on the market. Get started with Agent Builder today: [www.langchain.com/langsmith/agent-builder](http://www.langchain.com/langsmith/agent-builder)
