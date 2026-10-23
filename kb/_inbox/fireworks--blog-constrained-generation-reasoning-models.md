---
title: Constrained Generation for Reasoning Models With JSON Mode | Fireworks
kind: blog
topic: null
subtopic: null
secondary_topics: []
summary: null
triage: null
skip_reason: null
source: fireworks
url: https://fireworks.ai/blog/constrained-generation-reasoning-models
author: null
published: '2025-02-01'
fetched: '2026-10-23T06:13:58Z'
classifier: null
taxonomy_rev: 2
words: 1167
content_sha256: 1bee0ee00ef6f32fe003730c27bc6052623590627b41c143bdb90cd3ce9b14ac
---

# Constrained Generation for Reasoning Models With JSON Mode | Fireworks

# What is constrained generation and why is it useful

[Constrained generation](https://docs.fireworks.ai/structured-responses/structured-response-formatting#reasoning-model-json-mode) is a technique in natural language processing (NLP) where language models are guided to produce text that adheres to specific predefined rules or structures. This approach is particularly useful in applications requiring structured outputs, such as generating code, creating formatted documents, or producing data in formats like JSON. By enforcing constraints during the text generation process, models can ensure outputs that are not only coherent but also conform to the desired structure, enhancing both the utility and reliability of the generated content.

## What we’ll cover

- **How constrained generation works**
  - Guiding model token selection
  - Constrained decoding for structured outputs
- **Reasoning models and structured extraction**
  - The role of constrained generation in reasoning models
  - Fireworks’ JSON mode for reasoning models
- **Examples of constrained generation in action**
  - Structured Q&A with reasoning
  - Healthcare records with AI-driven summaries
  - Computer system specifications with structured recommendations
- **Conclusion**
  - Why structured generation improves AI reliability
  - Future applications and best practices

# How does it work

The process of constrained generation involves manipulating a model’s token generation to restrict its next-token predictions to only those that do not violate the required output structure. This can be achieved through various methods, such as constrained decoding, where the model’s output is directed to follow specific patterns or formats. For instance, in structured generation tasks, constrained decoding can simplify the next-token prediction space, accelerating generation by allowing some token generation steps to be skipped. Additionally, by focusing only on generating the necessary parts of the output and bypassing boilerplate sections, the overall efficiency of the generation process is improved.

Implementing constrained generation not only enhances the quality of the output by ensuring adherence to desired formats but may also improve performance. By reducing the complexity of the generation task and narrowing down the prediction space, the model can generate outputs more quickly and with greater accuracy. This efficiency gain is particularly beneficial in applications where rapid and reliable generation of structured text is crucial.

# Constrained generation in reasoning models

In the context of reasoning models, such as the recently released [DeepSeek R1](https://fireworks.ai/models/fireworks/deepseek-r1), constrained generation plays a pivotal role in ensuring that outputs adhere to specific formats and structures. The DeepSeek R1 model exemplifies this by incorporating a unique mechanism: it generates a reasoning process enclosed within `<think>` and `</think>` tokens, followed by a JSON-formatted output. This structured approach allows the model to transparently display its thought process before presenting the final result. Notably, the JSON schema applies exclusively to the JSON section that follows the `<think>` tags, ensuring that the reasoning process and the final output are clearly delineated and properly formatted. The caller can employ simple output parsing to separate the reasoning section from the structured output.

# Example 1: Simple Q&A

In this section, we’ll demonstrate how to utilize the [DeepSeek R1](https://fireworks.ai/blog/deepseek-r1-deepdive) reasoning model in JSON mode [using the Fireworks API](https://docs.fireworks.ai/structured-responses/structured-response-formatting#example-usage-with-pydantic).

`pythonCopy`
1234567891011121314151617181920212223242526272829303132333435363738394041424344454647484950515253545556

## How it works

1. **User Input:** A question is submitted to the model (e.g., “Who wrote Pride and Prejudice?”).
2. **Constrained Generation:** The model first produces its reasoning, enclosed in `<think>...</think>`, ensuring a structured explanation before providing the answer.
3. **Schema Enforcement:** The JSON-formatted response follows a **Pydantic-defined schema**, ensuring structured data.
4. **Parsing and Validation:** The reasoning section and JSON output are extracted separately, maintaining **cleanly structured and machine-readable responses**.

Let’s show another example, this time for a health care use case.

# Example 2: Structured healthcare data generation with reasoning JSON mode

This example showcases how to generate structured healthcare records using Fireworks’ DeepSeek R1 model in Reasoning JSON Mode. By combining structured output with an explanation of the model’s thought process, this approach enhances transparency and reliability in AI-generated medical documentation.

The workflow consists of the following steps:

- **Defining a Pydantic Schema** – Ensures consistency in patient records by specifying required fields.
- **Making an API Request** – Generates structured healthcare data tailored to a given medical scenario.
- **Extracting Model Reasoning** – Captures the model’s thought process within `<think>...</think>` tags to provide insights into diagnoses and treatments.
- **Validating and Parsing JSON Output** – Uses Pydantic to ensure compliance with the predefined schema.

This structured approach enables seamless integration of AI-generated healthcare data into medical systems, making it valuable for clinical documentation, decision support, and automated reporting.

`pythonCopy`
12345678910111213141516171819202122232425262728293031323334353637383940414243444546474849505152535455565758596061626364656667

## Output

When the script is run, the outputs would be similar to the following:

### The response from R1

`pythonCopy`
1234567891011121314151617181920212223242526272829

### The reasoning

`pythonCopy`
123456789101112131415161718192021222324252627

### The parsed JSON data

`pythonCopy`
123456789101112

# Example 3: Generating structured computer system specifications with reasoning JSON mode

In this last example, we show how to generate structured computer system specifications using DeepSeek R1 in Reasoning JSON Mode. By leveraging structured output and model reasoning, this method ensures clear and consistent AI-generated hardware recommendations.

The process involves:

- **Defining a Pydantic Schema** – Enforces structured specifications for computer components.
- **Making an API Request** – Generates PC configurations based on user requirements.
- **Extracting Model Reasoning** – Explains why specific components were selected within `<think>...</think>` tags.
- **Validating and Parsing JSON Output** – Ensures the structured response adheres to expected hardware constraints.

This approach is particularly useful for system builders, procurement tools, and recommendation engines that require AI-driven hardware configurations with explainable decision-making.

`pythonCopy`
123456789101112131415161718192021222324252627282930313233343536373839404142434445464748495051525354555657585960616263646566676869707172737475767778798081

### Output

When the example above is run, you should see output similar to:

### The response from R1

`pythonCopy`
123456789101112131415161718192021222324252627282930313233

### The reasoning

`pythonCopy`
1234567891011121314151617181920212223242526272829303132

### The parsed JSON data

`pythonCopy`
1234567891011121314

## Additional resources

For more details on using constrained reasoning in Fireworks, check out our documentation on [structured response modes](https://docs.fireworks.ai/structured-responses/structured-response-formatting#structured-response-modes), where we hope to publish additional examples soon.

# Conclusion

To conclude, constrained generation in reasoning models like DeepSeek R1 enables AI to produce structured, interpretable, and machine-readable outputs across a wide range of applications. By enforcing predefined formats through JSON mode, grammar-based constraints, and reasoning-enhanced responses, we can ensure reliability, transparency, and consistency in AI-generated content. Whether it’s structured Q&A, healthcare documentation, or computer system recommendations, this approach not only improves the accuracy of outputs but also enhances their usability in real-world systems. As AI continues to evolve, structured generation techniques will play a crucial role in making model outputs more actionable, verifiable, and seamlessly integrable into existing workflows.

# **Why Fireworks**

[**Fireworks**](https://fireworks.ai/signup) is an enterprise scale LLM inference engine. Today, several AI-enabled developer experiences built on the Fireworks Inference platform are serving millions of developers.

Fireworks lightning fast serving stack enables enterprises to build mission critical Generative AI Applications that are super low latency. With methods like prompt caching, speculative API, we guarantee high throughput performance with low total cost of offering (TCO) in addition to bringing best of the open-source LLMs on the same day of the launch.

If you have more questions, [**join our community**](https://discord.gg/J6ayEBXz) and tag a Fireworks team member or [**drop a note**](https://fireworks.ai/company/contact-us) to discuss building with LLMs from prototype to production.
