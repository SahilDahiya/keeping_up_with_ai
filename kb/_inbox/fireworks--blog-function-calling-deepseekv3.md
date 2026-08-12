---
title: 'Enabling Function Calling in DeepSeek v3: Bridging the Gap Between Text and
  Action'
kind: blog
topic: null
subtopic: null
secondary_topics: []
summary: null
triage: null
skip_reason: null
source: fireworks
url: https://fireworks.ai/blog/function-calling-deepseekv3
author: null
published: '2025-02-14'
fetched: '2026-08-12T06:30:11Z'
classifier: null
taxonomy_rev: 2
words: 719
content_sha256: 30347b05f2d28ba42a3e328124807ac6b40b9de444b032fdb8570b98b13faa70
---

# Enabling Function Calling in DeepSeek v3: Bridging the Gap Between Text and Action

Large language models (LLMs) have revolutionized natural language processing by generating impressive text based on massive pretraining and strategic alignment with user preferences during post training. However, their inherent limitation is that—while they excel at generating human-like language—they lack the ability to access or update real-world information on demand. This is where **function (or tool) calling** comes into play. By enabling LLMs to invoke external functions or APIs, we can dynamically extend their capabilities, making them not only great conversationalists but also powerful, interactive agents.

We are thrilled to announce that Fireworks API now supports function calling on top of the latest generation DeepSeek V3 model.

Function calling refers to the process by which an LLM detects that a user request requires external data or action and then produces a structured output (typically in JSON) that specifies which function to call along with the necessary arguments. For example, instead of simply generating text to answer “What is the weather in London?” an LLM equipped with function calling can output a JSON object that triggers a weather API call. Once the external tool returns the relevant data, the LLM integrates this information into its final response.

This paradigm is sometimes also called **tool calling**, and it fundamentally transforms LLMs from static knowledge generators into dynamic, interactive agents capable of real‐world tasks.

At its core, function calling involves the following key steps:

1. **Tool Specification and Prompting:** Developers define a set of external functions—each with a name, description, and a JSON schema for its parameters. For example, a weather retrieval function might be specified with parameters such as location and temperature unit. The LLM is then prompted with both the user query and the tool definitions. By passing in the tool definitions as part of the prompt context, the model learns to generate structured calls when it identifies that a user query requires external data.
2. **Detecting and Generating Function Calls:** When the LLM processes a user query, it decides whether to answer directly or issue a function call. If the latter is chosen, the model outputs a JSON string with the name of the function and the relevant arguments. This output does not execute the function—it merely indicates what external call should be made. The ability to output a function call in a structured format is critical; it lets developers safely and reliably integrate external APIs into the LLM’s workflow.
3. **Function Execution and Feedback Loop:** An external system or middleware detects the structured function call, executes the specified function (e.g., calls a weather API), and retrieves the result. This result is then fed back into the conversation context for the LLM to generate a comprehensive answer. In many implementations, a second round of prompting uses both the original query and the function’s output to produce the final response. This two-step process—first generating the function call, then using the result to refine the final output—forms the backbone of interactive LLM systems.

The ability to call functions extends LLMs’ applicability into numerous domains:

- •**Real-Time Data Retrieval:** LLMs can fetch up-to-date information such as weather forecasts, stock prices, or news updates, overcoming the limitations of static pretraining data.
- •**Task Automation and Workflow Integration:** By invoking functions, LLMs can perform tasks like scheduling meetings, managing databases, or even controlling IoT devices, effectively operating as autonomous agents.

We are excited to announce that the Fireworks API now offers function calling capabilities integrated with the latest DeepSeek v3 model. This enhancement enables developers to create applications where the model can interact with external functions or APIs, thereby extending its capabilities beyond static responses.

123456789101112131415161718192021222324252627282930313233343536373839404142434445464748495051525354555657585960616263646566676869707172

123456789101112131415161718192021222324252627282930313233343536373839404142434445464748495051525354555657585960616263646566676869707172737475767778798081828384858687888990919293949596979899100101102103104105106107108109110111112113114115116117118119120

DeepSeek has never released a complete official template for tool formatting in the DeepSeek v3 model. We did our best to deduce it from info available in the community. We will keep updating the template as new information appears.

One issue we discovered during testing is that the model is not great at multi-turn function calling. It performs best in scenarios where a single user message triggers (potentially multiple) function call(s).

The function calling feature is currently enabled on the Serverless offering only for now. If you want it activated for your On Demand or Reserved instances, please reach out to us.

Find the detailed documentation for function calling [here](https://docs.fireworks.ai/guides/function-calling).

Try out DeepSeek models on [Fireworks Model Library](https://fireworks.ai/models)
