---
title: How to build function calling and JSON mode for open-source and fine-tuned
  LLMs
topic: prompt-engineering
subtopic: structured-output
secondary_topics:
- agents/tool-use
summary: Shows how to build function calling and JSON mode for open-source and fine-tuned
  LLMs.
source: baseten
url: https://www.baseten.co/blog/how-to-build-function-calling-and-json-mode-for-open-source-and-fine-tuned-llms/
author: Bryce Dubayah; Philip Kiely
published: '2024-09-12'
fetched: '2026-07-11T04:09:03Z'
classifier: codex
taxonomy_rev: 1
words: 1484
content_sha256: bee24f951979a6526ad1354e108cf610adb715b2cebd761b838eb65c6b697530
triage: keep
skip_reason: null
---

# How to build function calling and JSON mode for open-source and fine-tuned LLMs

![JSON Mode](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1747437754-json-mode.png%3Fauto%3Dformat%26fit%3Dcrop%26h%3D630%26w%3D1200&w=3840&q=100)

Today, we [announced support for function calling and structured output](https://www.baseten.co/blog/function-calling-and-structured-output-for-llms/) for LLMs deployed with our [TensorRT-LLM Engine Builder](https://www.baseten.co/blog/automatic-llm-optimization-with-tensorrt-llm-engine-builder/). This adds support at the model server level for two key features:

- **Function calling**: also known as “tool use,” this feature lets you pass a set of defined tools to a LLM as part of the request body. Based on the prompt, the model selects and returns the most appropriate function/tool from the provided options.
- **Structured output**: an evolution of “JSON mode,” this feature enforces an output schema defined as part of the LLM input. The LLM output is guaranteed to adhere to the provided schema, with full Pydantic support.

To introduce these features, we build new capabilities into our customized version of NVIDIA’s Triton inference server. This engineering deep dive explains how the implementation works under the hood: defining schemas and tools, building a state machine, and using logit biasing to force valid output.

And the best part? Thanks to pre-computed token masks, there’s minimal latency impact from using either feature after the first call with a given schema is completed. You can expect the same tokens per second when generating JSON as when generating ordinary text.

If you’re looking to get started quickly with these new features, check out our [launch announcement](https://www.baseten.co/blog/function-calling-and-structured-output-for-llms/) and docs for [function calling](https://docs.baseten.co/invoke/function-calling) and [structured output](https://docs.baseten.co/invoke/structured-output). For implementation details, keep reading!

## How structured output is generated

To understand how it’s possible to guarantee structured output, we need to dive into the details of how a token is generated during LLM inference. If you’re familiar with LLM inference, you’ll know that a new token is generated on each forward pass through the model. During that forward pass:

- A vector of logits is outputted from the final layer of the LLM’s neural network.
- A normalization function like softmax is applied to turn the logits into probabilities.
- Using these probabilities, a token is selected. Depending on settings like - `top_p`,- `top_k`,- `beam_width`, and- `temperature`, this may not always be the highest-probability token.

Structured output uses logit biasing in the first step to guarantee valid tokens are generated.

### Logit biasing ensures token validity

The length of the logit vector outputted in the first step is equal to the number of tokens in the model’s vocabulary. For example, Llama 3 LLMs have a vocabulary of ~128,000 tokens. Thus, the logit vector will have about 128K values. Each logit in the vector is a score representing how much the LLM thinks that the given token from the vocabulary could be the next token in the output sequence.

For structured output, we only want to generate valid tokens. For example, an array in JSON must have both an opening and closing bracket: `[1, 2, 3]`. If we already have generated `[1, 2, 3` then the valid options are:

- A comma, space, and another value such as four: , - `4`.
- A closing bracket to end the array: - `]`.

From the model’s vocabulary, most of the possible tokens will not be valid at certain points when generating structured output. Logit biasing guarantees valid output structure by identifying every invalid token and setting its score to negative infinity, ensuring that the invalid tokens cannot be generated.

![Logit biasing visualization](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1726156432-frame-14655.png%3Fauto%3Dformat%26w%3D1200&w=3840&q=75)

This discussion of logit biasing raises a natural question: how do we know where we are in the output schema and which tokens are valid?

### State machine provides token requirements

The model server running beneath the inference process is responsible for tracking output format using a state machine. This model server is a modified version of NVIDIA Triton with extra capabilities that we call “Briton” (Baseten + Triton = Briton).

Using an industry standard library [Outlines](https://github.com/outlines-dev/outlines), which also powers VLLM, the Briton model server takes the schema passed as model output, transforms it into a regular expression, then generates a state machine from that regex. We chose Outlines for its robust feature set and reliability.

However, Outlines is written in Python, while TensorRT-LLM and Triton run in C++ for speed and efficiency. To handle this, we first generate the state machine in Python, then serialize it to [Protocol Buffers](https://protobuf.dev/) and load it into the model server.

Once loaded into the model server, the state machine makes the logit biasing process incredibly efficient. The state machine is cached in memory, and an appropriate token mask – a list of 1s and 0s corresponding to valid and invalid tokens – is created for each node of the state machine for logit biasing. This means that these calculations aren’t made during inference time, rather, existing masks are applied based on which state is active.

With no token mask calculations happening during token generation, this approach to logit biasing has a negligible effect on model performance, so you’ll get the same high tokens per second that you’re used to from TensorRT-LLM while also ensuring that every token is valid for the provided output schema.

## How to use function calling

Function calling works by providing LLMs with a structured description of a set of tools. Based on the prompt, the model selects the most appropriate tool or tools for the task described. Functions can be anything: API calls, ORM access, SQL queries, or just a script.

![A function written to be passed to an LLM — note the descriptive docstring.](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1726153339-carbon-49.png%3Fauto%3Dformat%26w%3D1200&w=3840&q=75) A function written to be passed to an LLM — note the descriptive docstring.

A function written to be passed to an LLM — note the descriptive docstring.It’s essential to understand that function calling does not give the LLM the capability to execute code. Instead, the function calling asks the LLM to choose the most appropriate function from the list of available tools. The actual function execution needs to happen in the same environment that made the LLM call.

Our function calling implementation follows the OpenAI API spec for compatibility, but applies to any model served with TensorRT-LLM via the Engine Builder that has built-in function calling capabilities (e.g. Llama 3.1 Instruct, but not Llama 3). Using the same logit biasing process that creates structured output, Briton (the modified Triton inference server) guarantees schematically correct tool responses.

![Example payload with function calling via the "tools" key](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1726153386-carbon-51.png%3Fauto%3Dformat%26w%3D1200&w=3840&q=75) Example payload with function calling via the "tools" key

Example payload with function calling via the "tools" keyFunction calling is critical for building agentic workflows and other [advanced Compound AI systems](https://www.baseten.co/blog/compound-ai-systems-explained/). To use function calling for yourself, check out our [function calling example](https://docs.baseten.co/invoke/function-calling) in the documentation.

## How to use structured output

The more general structured output feature forces LLMs to return output that adheres to a Pydantic schema. Structured output is valid JSON, but goes beyond JSON mode with support for required and optional fields, multiple data types, and additional validations like maximum length.

To start, define your output schema as a Pydantic model.

![Pydantic model for a "Person" object. The schema can be passed to an LLM to structure output.](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1726153425-carbon-52.png%3Fauto%3Dformat%26w%3D1200&w=3840&q=75) Pydantic model for a "Person" object. The schema can be passed to an LLM to structure output.

Pydantic model for a "Person" object. The schema can be passed to an LLM to structure output.Then, when you add the schema to the LLM call, the model server will build the schema into a state machine and use it for token masking as described above. The LLM inference arguments match the OpenAI API spec for structured output to ensure maximum compatibility.

![Example LLM request payload with a response schema.](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1726153505-carbon-53.png%3Fauto%3Dformat%26w%3D1200&w=3840&q=75) Example LLM request payload with a response schema.

Example LLM request payload with a response schema.Structured output is useful for a wide range of [Compound AI applications](https://www.baseten.co/blog/compound-ai-systems-explained/) as the guaranteed schema adherence means you can integrate LLMs into larger systems without worrying about type errors. To try structured output for your application, start with our [structured output example](https://docs.baseten.co/invoke/structured-output) in the documentation.

## What to build with function calling and structured output

While the implementation behind these new features is interesting, what’s even more exciting is the use cases they enable.

Function calling unlocks a wide range of agentic use cases for open source LLMs. With function calling, you can give agents access to a set of tools to accomplish tasks. As we saw above, the LLM is only able to select the best tool, not actually execute the API call or run the function, so that’s where multi-step AI systems are needed.

These multi-step, often multi-model systems are commonly known as [Compound AI](https://www.baseten.co/blog/compound-ai-systems-explained/). When building multi-stage Compound AI systems, structured output is critical. With structured output, each component of the system can communicate in valid JSON, preventing errors and avoiding parsing overhead.

As you build with function calling and structured output, remember that the model server changes don’t enhance quality, they only enforce format. Clear prompting and techniques like few-shot prompting still have their place for getting quality output within the enforced structure.

Get started building:
