---
title: 'LangChain Playground: Test Fireworks Open-Source Models | Fireworks'
kind: blog
topic: null
subtopic: null
secondary_topics: []
summary: null
triage: null
skip_reason: null
source: fireworks
url: https://fireworks.ai/blog/langchain-playground-fireworks-models
author: null
published: '2023-10-02'
fetched: '2026-10-23T06:11:34Z'
classifier: null
taxonomy_rev: 2
words: 777
content_sha256: d487cfd0b4bbe6e8b3fba85d30d79902d1842288f58da234c4170216ea6954f0
---

# LangChain Playground: Test Fireworks Open-Source Models | Fireworks

With the popularity of large language models (LLMs) such as ChatGPT and Llama 2, there are now a multitude of models to choose from — including a wide variety of open-source models.

Open-source LLMs have seen large performance gains over the past six months in particular. As these models get better, we’ve seen more and more people wanting to try them out. We are excited to team up with [LangChain](https://www.langchain.com/) to bring Fireworks.ai open-source models to the [LangSmith Playground](https://smith.langchain.com/hub) — completely free of cost.

### Fireworks.ai Inference Platform

Fireworks.ai provides a platform to enable developers to run, fine-tune, and share large language models (LLMs) to best solve product problems.

The Fireworks Generative AI platform provides developers access to lightning-fast OSS models, LLM inference, and state-of-the-art foundation models for fine-tuning. The platform provides state-of-the-art machine performance for latency-optimized and throughput-optimized settings and cost reduction (up to 20–120x lower) for affordable serving.

### Fireworks.ai 🤝 LangChain

Integrating Fireworks.ai models in the [LangSmith Playground](https://smith.langchain.com/hub) means giving the developer community easy access to the best high-performing open-source and fine-tuned models.

The LangChain Prompt Hub already makes it simple to try different prompts, models, and parameters without any coding. The availability of faster inference or faster LLMs helps to further boost productivity in building LLM workflows.

A big part of the LLM workflow requires testing and optimizing prompts which is a highly iterative and time-consuming process. This integration makes it possible for LangChain Prompt Hub users to more efficiently test and optimize prompts for state-of-the-art open-source and fine-tuned LLMs like Mistral 7B Instruct and Llama 2 13B.

While other model providers in the playground require an API key to use, we’ve teamed up with LangChain to enable anyone to use this integration regardless of whether they have a Fireworks API key or not (note: you need to be signed into the LangSmith platform in order for this to work).

### Using OSS Models in LangChain Hub

Before trying out the Fireworks open-source models in the LangSmith Playground, you will need to be signed into the LangChain Hub. Logged-in users can try Fireworks models in the playground without an API key, for free!

If you’re not logged in but want to try Fireworks models in the playground, you can set up an account from Fireworks.ai and get an API key. Here are the steps:

- Step 1: Visit [fireworks.ai](https://fireworks.ai/).
- Step 2: Click the “Sign In” button in the top navigation bar.
- Step 3: Click “Continue with Google” and authenticate with your Google account. A new Fireworks developer account will be provisioned for you the first time you sign in.
- Step 4: Next, we’ll provision a new API key. Click on “API Keys” in the left navigation bar then Click on “New API Key” and give your new API key a name.
- Step 5: Now open-source models like Mistral 7B Instruct and Llama 2 13B Chat are ready to be used in the LangChain Playground. Copy your API Key and enter it in the `Secrets & API Keys` section of the playground.

Here is a full step-by-step example:

First, let’s go the [LangSmith Hub](https://smith.langchain.com/hub?ref=fireworks.ai). We can filter existing prompts in the hub to ones that are meant for Llama 2.

Let’s choose the `[hwchase17/llama-rag](https://smith.langchain.com/hub/hwchase17/llama-rag?ref=blog.langchain.dev)` [prompt](https://smith.langchain.com/hub/hwchase17/llama-rag?ref=blog.langchain.dev). Once on this page, we can click on “Try it” to open it in the playground.

The playground defaults to OpenAI, but we can click on the model provider to change it up.

From here, we can select the **Fireworks** option:

We can now select the model we want to use, and then plug in some inputs and hit run!

We have selected the Mistral 7B instruct 4K model powered by the Fireworks.ai inference platform:

If you are not logged in to the Hub but have a Fireworks.ai API key, you can add your key as shown below:

Here are more examples to try out:

#### Code Infilling

Code infilling is the task of predicting missing code that is consistent with the preceding and subsequent code blocks. The following prompt uses Code Llama 13B to perform infilling. It requires a prefix code section and a suffix code section, then the model will generate the missing code.

Try it on the playground: [https://smith.langchain.com/hub/omarsar/infilling-code-llama/playground](https://smith.langchain.com/hub/omarsar/infilling-code-llama/playground)

Remember to set the Provider to `ChatFireworks` and model to `llama-v2-13b-code`

#### Llama 70B Chat

The following example uses one of the most capable open-source chat models, Llama 2 Chat 70B, to output ten jokes.

Try it on the playground: [https://smith.langchain.com/hub/langchain-ai/fireworks-llama-10-jokes/playground](https://smith.langchain.com/hub/langchain-ai/fireworks-llama-10-jokes/playground)

Remember to set the Provider to `ChatFireworks` and model to `llama-v2-70b-chat`

Feel free to experiment with other open-source models.

Check out all the open-source models available in the Fireworks platform here: **Models**
