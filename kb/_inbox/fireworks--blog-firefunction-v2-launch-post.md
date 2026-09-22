---
title: 'Firefunction-v2: Function calling capability on par with GPT4o at 2.5x the
  speed and 10% of the cost='
kind: blog
topic: null
subtopic: null
secondary_topics: []
summary: null
triage: null
skip_reason: null
source: fireworks
url: https://fireworks.ai/blog/firefunction-v2-launch-post
author: null
published: '2024-06-17'
fetched: '2026-09-22T06:11:52Z'
classifier: null
taxonomy_rev: 2
words: 1753
content_sha256: e33ee7c3884e9d9588324f696181206fe7cc3598017f2ce6bfa45b0b63058620
---

# Firefunction-v2: Function calling capability on par with GPT4o at 2.5x the speed and 10% of the cost=

- •We are releasing Firefunction-v2 - an open weights function calling model. Quick links: [Docs](https://readme.fireworks.ai/docs/function-calling) ,[model playground](https://fireworks.ai/models/fireworks/firefunction-v2) , demo[UI app](https://functional-chat.fireworks.ai/) and[Hugging Face model page](https://huggingface.co/fireworks-ai/firefunction-v2)
- •Firefunction-v2 is optimized for real world scenarios including multi-turn conversation, instruction following and parallel function calling. It retains Llama 3’s multi-turn instruction capability (0.84 vs 0.89 on MT bench) while consistently outscoring Llama 3 on function calling tasks (0.51 vs 0.30 on Nexus parallel multi function eval)
- •Firefunction v2 is competitive with GPT-4o function calling capabilities, scoring 0.81 on a medley public benchmarks vs 0.80 for GPT-4o. It’s available at a fraction of the cost of GPT-4o ($0.9 per output token vs $15) and with better latency (180 tok/sec vs 69 tok/sec).

Over the last few months, we’ve seen a huge leap in large language model capabilities with model releases like Llama 3. One area where improved model reasoning ability is particularly valuable is function calling.

We’re excited to build upon recent model advances and push the frontier of function calling with the release of our latest function calling model, Firefunction-v2. Firefunction-v2 is designed to have the intelligence and generalizability to handle real-world agentic use cases, like chat assistants, which involve function calling capabilities, alongside general chat and instruction following. Highlights include:

1. **Llama-3-esque chat capabilities:** Preservation of chat and other generalized capabilities from Llama-3 70B (Firefunction-v2’s base model)
2. **Better function calling, especially for multiple functions:** Better ability to handle more complex function calls and follow instructions for function calls
3. **Faster and less expensive than GPT-4o** - Enjoy similar function calling ability to GPT-4o with better UX and lower costs. Reach speeds of 180 token/sec and pricing of $0.9 per 1M tokens, instead of speeds of ~69 tokens/sec and costs of $15 per 1M output tokens

|  | Firefunction-v1 | Firefunction-v2 | GPT-4o | 
|---|---|---|---|
| Single turn function call (routing) | ✅ | ✅ | ✅ | 
| Multi-turn conversations | 😐 (limited) | ✅ | ✅ | 
| Parallel function calling | ❌ | ✅ | ✅ | 
| Instruction following | 😐 | ✅ | ✅ | 
| General conversation (with optional function calling) | 😐 | ✅ | ✅ | 
| Cost per 1M tokens | $0.5 | $0.9 | $5 (input), $15 (output) | 
| Response latency | Up to 200 tokens/sec | ~180 tokens/sec | ~69 tokens/sec | 
| Combined benchmark scores (MT bench, Gorilla, Nexus) | 0.49 | 0.81 | 0.80 | 

**Function calling - 1 year in retrospect**

It’s now been almost exactly 1 year since OpenAI unveiled function calling as a [feature](https://openai.com/index/function-calling-and-other-api-updates/). Function calling is the ability for a model to output structured text to call external APIs. LLMs have immense utility on their own but cannot access real-time or internal data. Function calling bridges that gap by letting LLMs format text to call APIs and optionally incorporate the API response.

In the last year, we’ve seen a proliferation of function calling and agentic usage. Fireworks was one of the first to offer a function calling-focused improvements in our models by launching:

(1) [**Firefunction-v1](https://fireworks.ai/blog/firefunction-v1-gpt-4-level-function-calling) and [Firefunction-v0](https://fireworks.ai/blog/fireworks-raises-the-quality-bar-with-function-calling-model-and-api-release)** - Firefunction-v1 excels at structured output and simple function calling use cases. It powers a variety of routing and decision-making use cases for developers today.

(2) [**Structured output modes**](https://fireworks.ai/blog/why-do-all-LLMs-need-structured-output-modes) - Options to guarantee that any of Fireworks’ LLMs adhere to a desired output format, like JSON

Most major closed-source models, like Google’s Gemini and Anthropic’s Claude, have added function calling capabilities and several open-source function calling-models have been released. While function calling has massive potential, there’s been limited success productionizing the capability. Developers have to choose between different tradeoffs with open-source vs closed-source models.

**Traditional open-source function calling models - overly specialized**

Most open-source models have focused on narrow use cases. They introduce function calling capabilities through an aggressive fine-tuning process that focuses narrowly on function calling and erases the native capabilities of the base model. This creates models that perform well on benchmarks (usually emphasizing single-turn, forced function calling). However these models (1) Don’t generalize outside of benchmarks to real world scenarios and (2) Are poor at general reasoning and chat.

**Closed function calling models - slow and expensive for production usage**

Given the narrow focus of open-source function calling models, closed source function calling models like GPT4 and Claude tend to significantly outperform open-source models in non-function calling tasks, like chat and text generation. However, these models have both high latencies and costs, limiting their production usability. Moreover, generalized models weren’t specifically designed for function calling and have limited ability in structuring responses and determining when to call functions.

One counter-intuitive thing we’ve learned is that real-world function calling models must be great at non-function calling tasks. When Llama 3 and Firefunction-v1 were released, we received a flood of user comments like:

- •“Llama 3 is insanely good. Can you just add better function calling to it?"
- •“Is [your function calling model] useful for chat conversations or only useful for function calling?”
- •“I’m using Llama 3 for function calling in my app right now. It mostly just chats with users but every once in a while, we need it to call an API”

This feedback led us to depart from the aggressive, narrow fine-tuning approach used for other open-source function calling models. Instead of overfitting to function calling scenarios, we augmented the base model with function calling capabilities while preserving its instruction following abilities.

We selected llama3-70b-instruct as the base for Firefunction v2, based on its excellent performance in real world scenarios, like its high scores on [blind crowdsourced evaluations](https://chat.lmsys.org/?leaderboard). We conducted fine-tuning on a highly-curated dataset composed of both function calling and regular conversation data and carefully monitored the training process to prevent the degradation of base model capabilities. We preserved the original context length of llama3-70b-instruct which is 8k.

Our evaluations show that our training process led to a well rounded model that is:

- •More intelligent and thus more adept at complex tasks, like parallel function calling.
- •Adaptable to a wide variety of function calling tasks, instead of only benchmarks
- •Excellent at non-function calling tasks like chat, reasoning and instruction following

We evaluated fire-function on a mix of publicly available datasets. Specifically, we evaluated on the popular Gorilla and Nexus benchmarks for function calling capability evaluation and mtbench for multi-turn instruction following. We compared the model against Firefunction-v1, Llama3-70b-instruct (using the same prompt as Firefunction) and GPT-4o.

The results are shown below, where we see that Firefunction-v2 achieves the highest performance on the medley of benchmarks. Firefunction-v2 consistently outperforms Llama 3 on function calling tasks while performing similarly on multi-turn instruction following.

|  | Firefunction v1 | Firefunction v2 | Llama 3 70b Instruct | GPT-4o | 
|---|---|---|---|---|
| Gorilla simple | 0.91 | 0.94 | 0.925 | 0.88 | 
| Gorilla multiple_function | 0.92 | 0.91 | 0.86 | 0.91 | 
| Gorilla parallel_function | 0 | 0.89 | 0.86 | 0.89 | 
| Gorilla parallel_multiple_function | 0 | 0.79 | 0.62 | 0.72 | 
| Nexus parallel | 0.38 | 0.51 | 0.30 | 0.47 | 
| Mtbench (multi turn instruction following) | 0.73 | 0.84 | 0.89 | 0.93 | 
| Average | 0.49 | 0.81 | 0.74 | 0.80 | 

Gorilla benchmarks are using code in the [official repository](https://github.com/ShishirPatil/gorilla) with the [following change](https://github.com/ShishirPatil/gorilla/pull/470) adding support for Firefunction-v2.

The Nexus parallel data used in the eval is [available](https://huggingface.co/datasets/fireworks-ai/nexus_parallel_messages) on HuggingFace alongside the corresponding [function definitions](https://huggingface.co/datasets/fireworks-ai/nexus_parallel_functions).

Mtbench scores were obtained through [FastChat](https://github.com/lm-sys/FastChat).

To illustrate the model’s capability in realistic settings, we [open sourced](https://github.com/fw-ai/forge/tree/main/apps/functional_chat) a fully-functional chat bot that users can customize with their own functions. You can play with the demo app [here](https://functional-chat.fireworks.ai/). The chat bot demonstrates some of the improved capabilities of Firefunction-v2.

**Parallel function calling**

The demo showcases the model’s adeptness at more complex function calling tasks. Firefunction-v2 handles up to 30 function specs reliably whereas Firefunction-v1 performance degrades when utilizing more than ~5 functions.

Firefunction-v1 also often fails at parallel function calling, where you need the model to execute two calls from one query (see example below). Parallel function calling is important for real world usage because it enables a more intuitive use experience and allows the model to be used with a wider range of APIs.

**Instruction-following**

Generalized models like Llama 3 often do not follow prompt instructions and struggle to make intelligent decisions about when to call functions. For example, we prompted Llama3 to call functions but “only when needed”. We give the model access to a function called calculate_bmi and feed it the following instruction: “Write a short travel post from Hawaii”.

As shown in the response below, llama3-70b-instruct forces an unnecessary function call in its response. In contrast, Firefunction v2 correctly discerns that the instruction is not related to the “calculate_bmi” function and correctly responds like a typical chat model.

Ready to try Firefunction-v2? Get started directly in our [documentation](https://readme.fireworks.ai/docs/function-calling), where we also offer a variety of sample apps and guides. We host FireFunction on Fireworks platform in a speed-optimized setup with OpenAI-compatible API. So you should be able to [easily swap in our model](https://readme.fireworks.ai/docs/openai-compatibility) with a 1-line code change if you were previously using OpenAI. You can also play with the model in our UI playground [here](https://fireworks.ai/models/fireworks/firefunction-v2), where you can add example functions and get code for your experimentations.

With Firefunction-v2, we’re aiming to provide a model that’s optimized for real-world usage in terms of its response quality, speed and cost. We’ve been crafting Firefunction-v2 with the help and feedback of the Fireworks community and have been delighted by the initial reactions to our real-world-focused approach. We’ve received multiple eager inquiries from beta testers about when Firefunction-v2 will be GA’d and production-ready and have received enthusiastic feedback like this:

Color me impressed with [Firefunction-]v2!… Called 3 functions as expected and…Still seems to retain the personality of Llama 3, which is great!

We’ll be continuing to iterate on Firefunction models and would love to hear what you think! Please join our Discord function calling [community](https://discord.gg/fireworks-ai) or directly [schedule](https://calendly.com/raythai) time with our PM if you have feedback.

At Fireworks, we’re committed to helping developers productionize generative AI at scale. We’re offering a platform that’s (1) Fast (2) Cost-efficient (3) Specialized to your use case. We’re excited to provide a model that embodies these traits with the release of Firefunction-v2. Happy building - we can’t wait to see what you build!

Devashish Tyagi had invaluable contributions to the development of Firefunction v2. Ray Thai managed the product side of the project and developer relationships.
