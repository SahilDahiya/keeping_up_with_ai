---
title: 'Functions: flexible AI engineering primitives'
topic: agents
subtopic: tool-use
secondary_topics:
- prompt-engineering/structured-output
summary: Introduces functions as flexible AI engineering primitives for tool calling,
  structured behavior, and reusable evaluation or workflow components.
source: braintrust
url: https://www.braintrust.dev/blog/functions
author: Braintrust Team
published: '2024-10-08'
fetched: '2026-07-11T04:32:21Z'
classifier: codex
taxonomy_rev: 1
words: 924
content_sha256: 7249471aa86fa28863286c5d8e689ed218652165c12b9702fbc974c1c1aa427d
---

# Functions: flexible AI engineering primitives

8 October 2024Ornella Altunyan6 min

Over the past year, the field of software engineering has been inundated with AI. There are tons of tools for improving developer productivity with the help of large language models (LLMs), but very few make it straightforward to build and scale AI-powered products. That's because introducing AI models fundamentally changes the software development lifecycle. Instead of measuring performance and reliability, developers need to assess accuracy and quality, which are much harder to pin down. Work happens in two distinct environments when iterating and making improvements to a product that uses an LLM: interactive playgrounds designed for testing prompts and data, and code editors, where we integrate those prompts with programming logic, evaluations, and deployments. Neither environment feels purpose-built for developing AI-powered software.

We believe this development experience—where you can fluidly compose, edit, and run prompts, data, and business logic—represents the future of
software engineering with LLMs. Today, we're excited to unveil the first major step towards this vision: **functions**.

Functions allow you to define atomic, reusable building blocks for executing AI-related logic. There are currently three types of functions in Braintrust:

-  [Prompts](https://www.braintrust.dev/docs/evaluate/write-prompts), templated messages to send to an LLM
-  [Tools](https://www.braintrust.dev/docs/evaluate/write-prompts#add-tools), general purpose code that can be invoked by LLMs
-  [Custom scorers](https://www.braintrust.dev/docs/evaluate/write-scorers), functions for scoring the quality of LLM outputs

You can create functions in your codebase or in the UI. You can *push* them from your codebase to the UI, and *pull* them back into your codebase as you edit them. You can also link them together;
for example, a prompt can call a tool, and Braintrust will automatically feed its results back to the prompt and continue execution. Functions can also be invoked through the [API](https://www.braintrust.dev/docs/reference/api/Functions),
with built-in support for [streaming](https://www.braintrust.dev/docs/reference/streaming) and structured outputs.

This means you can:

- Create a custom tool that browses the internet and invoke it through a prompt in the UI
- Run custom TypeScript and Python scorers in the playground
- Run scoring functions on a sample of your logs

Functions are the fastest way to prototype and deploy agentic applications. Braintrust takes care of the heavy lifting of securely and scalably executing, versioning, and logging each function independently, enabling you to iterate on your prompts and code much faster.

Last, but not least, functions are open and embrace standards — this is **not** a framework. For example, prompts work with any OpenAI-compatible model (our [proxy](https://www.braintrust.dev/docs/deploy/ai-proxy) extends
this to non-OpenAI models as well including Gemini, Anthropic, LLaMa, and others). Tools are TypeScript or Python functions with a well-defined input type, invoked through the standard
tool calling protocol. And scorers fit the popular, open-source [autoevals](https://github.com/braintrustdata/autoevals) framework.

The simplest type of function is a prompt. Any prompts you've created in Braintrust's prompt editor and playgrounds are already accessible as functions.

For example, a prompt like:

```
Reword the following question as a simple math formula using addition:
{{question}}
```
can now be invoked as a function that takes an argument called `question`:

typescript

```
await invoke({
  slug: "math-parser-41ae",
  input: {
    question: "How many days are there in June and July combined?",
  },
});
// Should return something like "30+31"
```
When you invoke prompts as functions, it unlocks even more capabilities. To stream results in an easy-to-parse format, set `stream: true`. Behind the scenes, Braintrust automatically caches and optimizes the prompt through our proxy and logs it to your project so you can debug completions later. This allows you to quickly change the model in the Braintrust UI and automatically deploy it to any environment that invokes it.

You can now create both prompt and code-based scorers from the Braintrust UI or your codebase, and seamlessly sync them between the UI and your app logic using the API. Once you create a custom function, you can use it in the playground and your code, and run it automatically on a sample of logs. For more information on scoring functions, check out the [full blog post](https://www.braintrust.dev/blog/custom-scorers).

Functions can also be composed using tool calls to produce sophisticated applications that would otherwise require lots of brittle orchestration logic. Any function can be used as a tool, which can be called, and its output added to the chat history. For example, a RAG agent can be defined as just two components:

- A system prompt containing instructions for how to retrieve content and synthesize answers
- A vector search tool, implemented in TypeScript or Python, which embeds a query, searches for relevant documents, and returns them

typescript

```
export const menuSearch = project.prompts.create({
  name: "Menu search",
  slug: "menu-search",
  description:
    "Help the user find the food they are looking for in San Francisco",
  model: "Claude-3.5-Sonnet",
  messages: [
    {
      content:
        "The user will ask some questions about food. Search through the menus in San Francisco to answer their question.",
      role: "system",
    },
  ],
  tools: ["menu-search"],
});
```
To learn more about building a RAG agent with functions, check out this [cookbook](https://www.braintrust.dev/docs/cookbook/recipes/ToolRAG).

Functions are not only the future of AI engineering, but they also have deep roots in the history of AI. At its core, a machine learning model itself is a black-box function, optimized through a loss function to minimize error and improve predictions. This concept has always been at the heart of AI — using functions to transform data into meaningful insights.

In Braintrust, we’ve taken this foundational idea and expanded it, bringing together evals, logging, datasets, prompts, and the playground  into one powerful workflow that redefines the software engineering lifecycle. [Try building with functions](https://www.braintrust.dev/docs/cookbook/recipes/ToolRAG) for free today, and [let us know what you think](https://www.braintrust.dev/contact).
