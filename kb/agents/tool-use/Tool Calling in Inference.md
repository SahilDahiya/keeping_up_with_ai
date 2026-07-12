---
title: Tool Calling in Inference
topic: agents
subtopic: tool-use
secondary_topics:
- prompt-engineering/structured-output
summary: Explains tool calling in inference and how model servers support structured
  external actions.
source: baseten
url: https://www.baseten.co/blog/tool-calling-in-inference/
author: Kenzie Amack; Bryce Dubayah
published: '2025-11-05'
fetched: '2026-07-11T04:06:54Z'
classifier: codex
taxonomy_rev: 1
words: 2394
content_sha256: 98ebbf70f6d2f5112be9833b3ac0085a221b2759d453e602e572b6b241b9258d
triage: keep
skip_reason: null
---

# Tool Calling in Inference

![Tool Calling in Inference](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1762301113-text-template-2.png%3Fauto%3Dformat%26fit%3Dcrop%26h%3D630%26w%3D1200&w=3840&q=100)

The rise of AI agents has fueled a surge in open-source models that support tool calling, but developers have quickly realized that the quality of tool calling varies among inference providers. Inference providers play a critical role in ensuring tool calling success from pre-processing to model execution, all the way to post-processing.

This post breaks down the tool calling basics, how to find the best agentic model, and unpacks what inference providers can do at each layer to ensure reliable, high-quality inference for agentic workloads.

Over the past year, the rise of AI agents has fueled an explosion of open-source models that support tool calling. If you’re a consumer of AI trends, you may have also noticed the explosion of something else around that time: tool calling benchmarks.

While benchmarks have always been the darling of the AI world, the consumption of third-party benchmarks related to tool calling seems to take on a whole new fervor. Developers have caught on that there is a significant range in tool calling success between different inference providers, and they’re grasping for answers on who does it best. Historically, inference providers had *relatively *similar model quality (quantization fixed). The tool calls upend this historical trend and introduces a particularly opaque criterion for developers to evaluate. 

As the ecosystem races to benchmark and compare performance, it’s worth looking beyond what’s being touted in the Twitter sphere to make your own informed decision. In this blog, we’ll cover everything you’ll need to make informed decisions when evaluating tool calling success among providers. We’ll unpack what these benchmarks evaluate, how inference providers influence tool calling outcomes, and how Baseten is working to deliver best-in-class tool calling for developers.

## Tool calling demystified

At its simplest, tool calling is how LLMs interact with external applications. Through tool calls, models retrieve, analyze, and generate information. LLMs began using external functions with function calling in 2021 and can now utilize multiple tools and further orchestrate external applications. By offloading certain tasks to tools, models can remain relevant for longer periods without requiring retraining. Tool calling also increases efficiency (less needs to be stored in model weights), ensuring models can be more dynamic to adapt to user requests.

![Agentic workflow overview](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1762322420-image-11-4-25-at-10-00-pm.jpeg%3Fauto%3Dformat%26w%3D1200&w=3840&q=75) Agentic workflow overview

Agentic workflow overviewFor example, ChatGPT can query your contacts within your Google Suite for an email or phone number (contact lookup) or search and analyze documents in Slack (internal knowledge search). Both of these are tool calls that enable models to utilize user context to create personalized product experiences. When coordinating with external applications, models must generate specifically formatted text (a schema) that specifies which tool to “call” and what inputs must be provided. For the contact lookup, ChatGPT may invoke a contact lookup tool that requires { "name": "Jane Doe" } as the input to return the email address for Jane.

Tool calls can be single-turn and multi-turn. In a single-turn tool call, the model requests a single tool (indeed, it’s aptly named) and returns the result. But the real fun starts with multi-turn calls. Developers utilize multi-turn for complicated requests where multiple different applications must be called.

Let’s take an agentic workflow that generates an outbound sales email. One tool generates a prospect that matches the title the user supplied, the next tool generates recent company news to include, and the last tool combines these inputs to create an email template. Each tool is kicked off in a chain-like pattern where the output of one tool becomes the input for the next.

While multi-turn tool calls are powerful, output quality can degrade with each successive “turn”. Each turn requires the model to interpret the received output correctly and translate it into a schema that the next tool will accept. All of this translation creates room for error.

In addition to single-turn and multi-turn tool calls, there are four types of tool choice implementations:

## How to select the right model and provider

### Benchmarking models

2025 is the year of agentic AI for a reason. Since the release of DeepSeek R1 in January 2025, there has been a significant rise in models that can power agentic workflows. Thankfully, you now have more models than ever to choose from, but it’s still important to ensure you’re utilizing the model best fit for your agentic use case.

When testing with your prompt, you’ll want to monitor model outputs across:

- **Tool selection accuracy:**Did the model pick the right tool(s), in the right order?
- **Argument fidelity:**Were inputs (into the tool call) complete and grounded in context?
- **Schema validity:**Did the outputs match the prompted schema and return valid JSON?
- **Turn efficiency:**how many calls and tokens did it take to complete each task?

Thankfully, you don’t have to start from scratch. Libraries like [BFCL](https://gorilla.cs.berkeley.edu/leaderboard.html), [ToolBench](https://github.com/OpenBMB/ToolBench?utm_source=chatgpt.com), and [ShortcutsBench](https://github.com/EachSheep/ShortcutsBench) can serve as a great starting point to show results across the dimensions. While it may be tempting to opt for the highest-rated model and run with it, we suggest testing your workflows against multiple LLMs. Each LLM has a different “personality” and may be uniquely powerful for your workflow (regardless of public benchmarking scores).

### Benchmarking inference providers

Once you’ve selected your model, you’ll want to test the same prompt across multiple inference providers to choose the provider that gives you high tool calling accuracy, reliability, and the right mix of latency and throughput. Buyer beware: it’s tempting to skip this step after all the work of finding the right model. But tool call success is very reliant on having the right inference provider. [Public benchmarks](https://x.com/Kimi_Moonshot/status/1976926483319763130) have shown some of the worst providers give a success rate of only 7% - meaning for every 100 tool call attempts you make, only seven go through. Sometimes, you get what you pay for. 

To avoid a situation like the one above, it’s crucial to benchmark inference providers. There are plenty of [open-source libraries](https://github.com/adamwlarson/LLMToolCallingTester) for you to start with. You’ll want to look for a high percentage of successful tool call completions across various real-world scenarios (50-200). It’s key to investigate the failures: where do models break? How do providers retry? How often does schema validity slip? 

But, just having great quality isn’t enough. Due to the long context typically associated with tool calling, latency (time to first token) and throughput (tokens per second) can fluctuate significantly across inference providers. It’s key to look for a provider that offers the fastest *end-to-end latency*. This ensures users get a prompt and natural response. 

While it would be nice to rely on public static benchmarks, tool calling success isn’t about synthetic scores. It’s about knowing which model and inference provider combination performs best with your workload.

## Inference's influence on tool calling success

Finding the best model that works for your agentic prompt is only the first step. While foundation model labs work to create model weights that are well-trained to utilize tools, inference providers also directly influence tool calling success. The following areas influence tool calling success during inference:

- Pre-processing - *(chat template validation, model prompting)*
- Model execution - *(structured outputs, quantization technique)*
- Post-processing - *(parsing)*

### Pre-processing

Building successful tool calling starts even before an LLM receives a prompt. During pre-processing, inference providers should 1) validate the chat template, and 2) utilize model prompting to ensure successful tool calls.

The respective foundation model provider creates the chat template. The chat template transforms the user-provided request into a specific structure (a single text string) and then feeds it into the LLM. While the foundation model provider creates the chat template, inference providers are responsible for validation and testing to ensure the template passes the right tokens in the right format. This helps ensure consistency across different requests and context lengths.

![Example of the chat template transformation](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1762323479-group-1723497774-4.png%3Fauto%3Dformat%26w%3D1200&w=3840&q=75) Example of the chat template transformation

Example of the chat template transformationInference providers can also utilize model prompting to ensure higher-quality tool calls. There are two reasons inference providers might prompt the model. While each one is technically the same in spirit, they have different purposes. Inference providers might utilize unique prompting to support the model in producing high-quality outputs. To achieve this, they’ll test various prompts to determine which ones support better outputs and reliability, and then insert these along with each user request.

Inference providers can also utilize model prompting when they don’t have structured outputs to obtain higher-quality required or named tool calls. When the specific tool is called, inference providers use logic (essentially an `if` statement) to inject the correct schema into the prompt as part of the chat template transformation. This ensures the model consistently produces the right schema for common tools. This technique isn’t necessary when inference providers have added structured outputs, so it’s worth inquiring with your inference provider on how they are supporting accuracy on required and named tools. 

While these may seem like small implementation details, chat template validation and model prompting can have a significant impact on whether a model can consistently understand when and how to utilize tools.

### Model execution

During model execution, providers can utilize structured outputs and make thoughtful decisions regarding quantization to ensure tool calling success.

#### Structured outputs

One of the most critical levers for tool calling is creating reliable structured outputs. Structured outputs ensure models produce a machine-readable format that can be easily parsed into a function call. Inference providers decide how strongly to enforce structure at the model level versus leaving validation to developers. Inference providers may expose parameters such as `response_format` to encourage the model to return JSON, or opt for a softer approach that uses only prompt-based instructions (typically less reliable).

Even when models can produce structured outputs, good inference providers validate that the schema adheres to the declared schema before returning it to the developer. This ensures inference providers catch incorrect generations.

#### Quantization

Quantization is a common technique to reduce the memory footprint of large LLMs to make them more efficient for inference. Most open-source foundation model providers provide a quantized version of their model at launch. But not all quantization techniques are built the same. Inference providers must be thoughtful about how much quantization they employ (FP8 vs. FP4) and whether to utilize the provided quantized checkpoints or quantize themselves.

When quantizing a model, it’s important to include data within the quantization phase that closely resembles the prompts the model will serve. Quantization is often achieved by retraining a model and truncating floating-point numbers, utilizing public news sources as the training data. Given that this data typically doesn’t include any tool calls, this quantization technique can decrease a model's ability to appropriately call tools post-quantization. To ensure high tool calling completion, inference providers must quantize with tool calling in mind.

### Post-processing

Post-processing is the final workflow for the LLM, in which the implementation of inference providers can significantly impact the success of tool calls. Most LLMs return a single text string that contains the tool call embedded within.

Each model provider uses a slightly different formatting convention for tool calls. Inference providers implement parsers to extract and normalize these outputs, allowing application developers to pass the tool call to the correct API. Because LLMs can produce subtle variations in how they format or label tool calls, inference providers must carefully monitor outputs and design parsers that robustly capture every valid call type.

## How Baseten builds with tools in mind

The Baseten platform is built for production inference. With the rise of agentic models, we’ve heavily invested to ensure tool calling is reliable and performant.

In Moonshot’s most recent [Kimi K2 vendor benchmark](https://x.com/Kimi_Moonshot/status/1976926483319763130) Baseten shows among the highest number of successful tool calls. In addition to high tool calling accuracy, we work on providing the right mix of quality and performance (both latency and throughput) while remaining cost-efficient for intensive workloads. You can view our performance with Kimi K2 [live on OpenRouter](https://openrouter.ai/moonshotai/kimi-k2-0905?sort=latency) to get a sense of our metrics. 

So, how do we get such high tool calling accuracy? We’ve made investments in every category that influences tool calling success. Here’s a quick overview across the three categories introduced a bit earlier:

- Pre-processing - *(chat template validation, model prompting)*
- Model execution - *(structured outputs, quantization technique)*
- Post-processing - *(parsing)*

### Pre-processing

While the model provider creates the chat template, we 1) validate the chat template and resolve bugs, and 2) include model prompting to ensure models correctly respond to user tool calls. We do a significant number of tests to find the sweet spot for each model; each model works best with different prompting techniques. Once we find the right prompting technique, we’ll use this behind the scenes to support high-quality model outputs.

### Model execution

Within the model execution phase, we utilize 1) structured outputs and 2) proprietary quantization to ensure high tool calling quality.

Our structured outputs feature ensures LLMs return outputs that adhere to a Pydantic schema. That means outputs are not only valid JSON but also follow the articulated Pydantic schema, which includes required and optional fields, multiple data types, and validations (such as maximum length). Our structured outputs utilize [logit biasing](https://www.baseten.co/blog/how-to-build-function-calling-and-json-mode-for-open-source-and-fine-tuned-llms/#logit-biasing-ensures-token-validity) that identifies invalid tokens (not the correct data type, etc.) and labels these outputs with a probability of negative infinity, ensuring they will not be generated. 

Baseten thoughtfully utilizes quantization to lower latency while ensuring output quality remains high. In specific cases, we self-quantize the models available in our Model APIs instead of using off-the-shelf quantized checkpoints. We find that by quantizing with the desired use case in mind (agentic), we retain higher model quality while also greatly increasing inference performance. For DeepSeek v3.1, we quantized the model using a dataset closely resembling agentic use cases to improve multi-turn performance and enhance the model's ability to make high-quality tool calls.

### Post-processing

Lastly, we parse the LLM output into an OpenAI-compatible format to ensure outputs are easily accessible when returned to developers (instead of raw model output).

## Conclusion

Successful agentic workloads rely on using high-quality models *as well as *reliable inference providers. While benchmarks can be a great starting point, it’s crucial to understand what your providers do to ensure success and to validate the accuracy and performance of your workload. 

If you’re interested in trying out an agentic model on Baseten, we recommend our [Kimi K2 0905 Model API.](https://www.baseten.co/library/kimi-k2-0905/)
