---
title: How to build function calling and JSON mode for open-source and fine-tuned
  LLMs
kind: blog
topic: prompt-engineering
subtopic: structured-output
secondary_topics:
- inference/optimization
summary: 'Explains the implementation behind guaranteed-schema structured output and
  function calling in a customized NVIDIA Triton server: building a state machine
  over a JSON schema and using pre-computed logit-bias token masks with no TPS penalty.'
triage: null
skip_reason: null
source: baseten
url: https://www.baseten.co/blog/how-to-build-function-calling-and-json-mode-for-open-source-and-fine-tuned-llms
author: Bryce Dubayah
published: '2024-09-12'
fetched: '2026-11-12T06:09:08Z'
classifier: claude
taxonomy_rev: 2
words: 1377
content_sha256: 498faf0197a1ff8055ebf83f6bdc35c7e4208c291d3873075b8cde826e6ac173
---

# How to build function calling and JSON mode for open-source and fine-tuned LLMs

Model performance
# How to build function calling and JSON mode for open-source and fine-tuned LLMs

Use a state machine to generate token masks for logit biasing to enable function calling and structured output at the model server level.


- Authors
- Date
- September 12, 2024

Today, we [announced support for function calling and structured output](https://www.baseten.co/blog/function-calling-and-structured-output-for-llms/) for LLMs deployed with our [TensorRT-LLM Engine Builder](https://www.baseten.co/blog/automatic-llm-optimization-with-tensorrt-llm-engine-builder/). This adds support at the model server level for two key features:

1. **Function calling**: also known as “tool use,” this feature lets you pass a set of defined tools to a LLM as part of the request body. Based on the prompt, the model selects and returns the most appropriate function/tool from the provided options.
2. **Structured output**: an evolution of “JSON mode,” this feature enforces an output schema defined as part of the LLM input. The LLM output is guaranteed to adhere to the provided schema, with full Pydantic support.

To introduce these features, we build new capabilities into our customized version of NVIDIA’s Triton inference server. This engineering deep dive explains how the implementation works under the hood: defining schemas and tools, building a state machine, and using logit biasing to force valid output.

And the best part? Thanks to pre-computed token masks, there’s minimal latency impact from using either feature after the first call with a given schema is completed. You can expect the same tokens per second when generating JSON as when generating ordinary text.

If you’re looking to get started quickly with these new features, check out our [launch announcement](https://www.baseten.co/blog/function-calling-and-structured-output-for-llms/) and docs for function calling and structured output. For implementation details, keep reading!

To understand how it’s possible to guarantee structured output, we need to dive into the details of how a token is generated during LLM inference. If you’re familiar with LLM inference, you’ll know that a new token is generated on each forward pass through the model. During that forward pass:

1. A vector of logits is outputted from the final layer of the LLM’s neural network.
2. A normalization function like softmax is applied to turn the logits into probabilities.
3. Using these probabilities, a token is selected. Depending on settings like `top_p`, `top_k`, `beam_width`, and `temperature`, this may not always be the highest-probability token.

Structured output uses logit biasing in the first step to guarantee valid tokens are generated.

The length of the logit vector outputted in the first step is equal to the number of tokens in the model’s vocabulary. For example, Llama 3 LLMs have a vocabulary of \~128,000 tokens. Thus, the logit vector will have about 128K values. Each logit in the vector is a score representing how much the LLM thinks that the given token from the vocabulary could be the next token in the output sequence.

For structured output, we only want to generate valid tokens. For example, an array in JSON must have both an opening and closing bracket: `[1, 2, 3]`. If we already have generated `[1, 2, 3` then the valid options are:

1. A comma, space, and another value such as four: , `4` .
2. A closing bracket to end the array: `]`.

From the model’s vocabulary, most of the possible tokens will not be valid at certain points when generating structured output. Logit biasing guarantees valid output structure by identifying every invalid token and setting its score to negative infinity, ensuring that the invalid tokens cannot be generated.

This discussion of logit biasing raises a natural question: how do we know where we are in the output schema and which tokens are valid?

The model server running beneath the inference process is responsible for tracking output format using a state machine. This model server is a modified version of NVIDIA Triton with extra capabilities that we call “Briton” (Baseten + Triton = Briton).

Using an industry standard library [Outlines](https://github.com/outlines-dev/outlines), which also powers VLLM, the Briton model server takes the schema passed as model output, transforms it into a regular expression, then generates a state machine from that regex. We chose Outlines for its robust feature set and reliability.

However, Outlines is written in Python, while TensorRT-LLM and Triton run in C++ for speed and efficiency. To handle this, we first generate the state machine in Python, then serialize it to [Protocol Buffers](https://protobuf.dev/) and load it into the model server.

Once loaded into the model server, the state machine makes the logit biasing process incredibly efficient. The state machine is cached in memory, and an appropriate token mask – a list of 1s and 0s corresponding to valid and invalid tokens – is created for each node of the state machine for logit biasing. This means that these calculations aren’t made during inference time, rather, existing masks are applied based on which state is active.

With no token mask calculations happening during token generation, this approach to logit biasing has a negligible effect on model performance, so you’ll get the same high tokens per second that you’re used to from TensorRT-LLM while also ensuring that every token is valid for the provided output schema.

Function calling works by providing LLMs with a structured description of a set of tools. Based on the prompt, the model selects the most appropriate tool or tools for the task described. Functions can be anything: API calls, ORM access, SQL queries, or just a script.

It’s essential to understand that function calling does not give the LLM the capability to execute code. Instead, the function calling asks the LLM to choose the most appropriate function from the list of available tools. The actual function execution needs to happen in the same environment that made the LLM call.

Our function calling implementation follows the OpenAI API spec for compatibility, but applies to any model served with TensorRT-LLM via the Engine Builder that has built-in function calling capabilities (e.g. Llama 3.1 Instruct, but not Llama 3). Using the same logit biasing process that creates structured output, Briton (the modified Triton inference server) guarantees schematically correct tool responses.

Function calling is critical for building agentic workflows and other [advanced Compound AI systems](https://www.baseten.co/blog/compound-ai-systems-explained/). To use function calling for yourself, check out our function calling example in the documentation.

The more general structured output feature forces LLMs to return output that adheres to a Pydantic schema. Structured output is valid JSON, but goes beyond JSON mode with support for required and optional fields, multiple data types, and additional validations like maximum length.

To start, define your output schema as a Pydantic model.

Then, when you add the schema to the LLM call, the model server will build the schema into a state machine and use it for token masking as described above. The LLM inference arguments match the OpenAI API spec for structured output to ensure maximum compatibility.

Structured output is useful for a wide range of [Compound AI applications](https://www.baseten.co/blog/compound-ai-systems-explained/) as the guaranteed schema adherence means you can integrate LLMs into larger systems without worrying about type errors. To try structured output for your application, start with our structured output example in the documentation.

While the implementation behind these new features is interesting, what’s even more exciting is the use cases they enable.

Function calling unlocks a wide range of agentic use cases for open source LLMs. With function calling, you can give agents access to a set of tools to accomplish tasks. As we saw above, the LLM is only able to select the best tool, not actually execute the API call or run the function, so that’s where multi-step AI systems are needed.

These multi-step, often multi-model systems are commonly known as [Compound AI](https://www.baseten.co/blog/compound-ai-systems-explained/). When building multi-stage Compound AI systems, structured output is critical. With structured output, each component of the system can communicate in valid JSON, preventing errors and avoiding parsing overhead.

As you build with function calling and structured output, remember that the model server changes don’t enhance quality, they only enforce format. Clear prompting and techniques like few-shot prompting still have their place for getting quality output within the enforced structure.

Get started building:

- First, deploy Llama 3.1 8B with the TensorRT-LLM Engine Builder
- Then try function calling with an accurate LLM math demo
- And get JSON-mode output with in a document parsing demo
