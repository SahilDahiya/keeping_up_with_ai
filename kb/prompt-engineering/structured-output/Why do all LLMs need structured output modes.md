---
title: Why do all LLMs need structured output modes?
topic: prompt-engineering
subtopic: structured-output
secondary_topics:
- agents/tool-use
summary: Explains why structured-output modes matter for reliable LLM applications
  and tool-calling systems.
source: fireworks
url: https://fireworks.ai/blog/why-do-all-LLMs-need-structured-output-modes
author: null
published: '2024-02-20'
fetched: '2026-07-11T04:18:20Z'
classifier: codex
taxonomy_rev: 1
words: 1446
content_sha256: 027848014740a35dd5740cf8a86423e36ac0e8d8939fc309ad8fd08d32f6169f
triage: keep
skip_reason: null
---

# Why do all LLMs need structured output modes?

**Tl;dr:** All Fireworks language models can now be invoked with either a (a) JSON schema (b) context-free grammar (similar to Llama.cpp’s feature) to guarantee that LLM output strictly follows your desired format without hallucinations.

**Intro**

Since [ReAct](https://arxiv.org/abs/2210.03629) and [Gorilla](https://arxiv.org/abs/2305.15334), there have been tentative explorations into tool use for both chatbots and agents. However they were not reliable or scalable and mostly constrained to research, until OpenAI launched ChatGPT plugins last March and then innovated the function calling API in June, becoming the most widely adopted way for LLMs to generate JSON, initially only for function calling, but formalized as an official “JSON Mode” API in November. However, this is only available in OpenAI’s closed platform.

Simultaneously, explorations in constraining LLM output proceeded both in academia ([ReLLM](https://arxiv.org/abs/2211.15458), [GCD](https://arxiv.org/abs/2305.13971)) and industry ([guidance](https://github.com/guidance-ai/guidance), [guardrails](https://github.com/guardrails-ai/guardrails), [outlines](https://github.com/outlines-dev/outlines)), The most flexible and widely used version of LLM constraints eventually came out of Llama.cpp’s [grammar-based-sampling](https://github.com/ggerganov/llama.cpp/pull/1773) feature. However, this was only available locally on certain supported llama.cpp models.

**We believe that structured output modes for LLMs have gone from research prototypes in 2023 to table-stakes in 2024**. Ensuring that LLMs respond with predictable, parsable output is critical to many use cases. For example, if you’re using an LLM to generate arguments for an API call, you always want the model to respond with a specific API schema. If you’re using an LLM to tag text, you might always want to use the same labels. Developers can spend hours perfecting a system prompt to “only respond in valid JSON'' or “respond in less than 500 words” and still get unintended output. With function calling, you can build even more complex AI engineering abstractions, resulting in leading developers concluding that [Pydantic is all you need](https://www.youtube.com/watch?v=yj-wSRJwrrc) and [Structured Data is the best way to do Chain of Thought](https://minimaxir.com/2023/12/chatgpt-structured-data/).

**What we’re doing about it**

Today, we’re launching of two features on all Fireworks language models:

- **JSON mode**
- **Structured grammar mode**- ***- Always generate valid output according to**.** As we understand, we’re the **only** hosted model API provider supporting this feature!- **arbitrary context-free grammar**for maximum flexibility. We take inspiration from- [the popular grammar feature](https://github.com/ggerganov/llama.cpp/blob/master/grammars/README.md)in Llama.cpp

Use both features on the Fireworks generative AI platform to get blazing fast inference and battle-tested reliability!

**JSON mode**

JSON mode enables users to define a [JSON output schema](https://json-schema.org/) for the model to follow. In Python, you can get the schema from [any Pydantic structure](https://docs.pydantic.dev/latest/why/#json-schema). Similarly, it can be generated from [a TypeScript structure](https://github.com/YousefED/typescript-json-schema).

JSON mode allows you to better use any of our models for function calling or other structured output. For example, if you were using the Fireworks Mixtral model to tag characteristics from an email, you would first define the schema you’d want to output. In this example, that might be: '''json class Tag(BaseModel): language: str sentiment: str topic: str ''' We would then specify this output schema when we call the model by specifying it as the response. Note that we also still describe the output format in the prompt.

123456789101112131415

The model would then respond according to the specified JSON schema. In this example, we get the output:

12

Voila! Every time you call the model, you can rest assured that the output will fit your JSON schema.How does it work? What’s happening behind the scenes is that we’re taking the scheme you provide and forcing the model to decode according to its structure. For each step of the autoregressive decoding, we only allow new tokens to be generated that would be considered valid in the provided schema. See our [documentation](https://docs.fireworks.ai/structured-responses/structured-response-formatting) for more information on how JSON mode works and how to use it!

**Important**: when using JSON or Grammar mode, it's crucial also to instruct the model to produce the desired schema via a system or user message. The description in the prompt may be the same formal schema or it can be in natural language.

**Grammar mode**

Outputting JSON is great but not all rules/structure can fit neatly in JSON. Grammar mode lets you describe the desired [context-free grammar](https://en.wikipedia.org/wiki/Formal_grammar#Context-free_grammars) in an [extended BNF form](https://docs.fireworks.ai/structured-responses/structured-output-grammar-based). The possibilities are endless! Anything from output styles to entire programming languages can be represented as grammars. Let’s take a few examples.

**Use case #1**

Let’s say you want to make use of a mistral model to make an initial medical diagnosis. (NOTE: Fireworks does not intend to give medical advice). In this example, you’d want to limit the medical diagnosis to just the name of 1 of 5 conditions. Here is what the grammar would look like:

1234

The `root` rule is what the entire output has to match. We define the `root` rule to be just the `diagnosis` rule. And for diagnosis, we defined it to be one of the five different classes, each separated with a `|` to signify that it can be any of these words.

123456789101112131415161718192021222324252627282930313233

Note, that we also described the output format in the prompt in free form. Alternatively, could have used a fine-tuned model for the medical domain.

You can see the response was “arthritis” - the model responded with only the name of the medical condition, exactly as we had specified.

12

What happens if we use the prompt without the grammar? Output is often chattier, like in this real example: “The possible diagnosis for these symptoms could be arthritis.”

**Use case #2**

The fact that LLMs can generate output in multiple languages but what if we only want responses in one language? For example, let’s say we’re building a Japanese-speaking tour guide and only want Japanese output. This can also be represented in a grammar.

12345678910111213141516171819202122232425262728293031323334353637383940414243444546474849

Here the grammar is a little more sophisticated. We are saying there are multiple parts to the Japanese language, there is hiragana, katakana, punctuations and all the other possible CJK (Chinese, Japanese and Korean) characters. And then we go on to specify all the different character ranges for these concepts. Note that not all CJK is actually not valid Japanese. But with the help of grammar, the output is entirely Japanese text, adhering to the specified grammar.

12

And since the grammar is actually more lenient than Japanese and covers Chinese as well, we can also just prompt the model to be a fluent Chinese speaker.

12

And you can see here that we are trying something a little difficult, asking a Japanese tour guide to speak Chinese. But with the help from the grammar, the model replied in Chinese, with the same grammar specified

12

Without the help from the grammar, here is the model reply in a mix of Chinese and English

12

So we see this as a powerful tool for programmers to have more constrained and stronger system prompts for the model to follow.

**Use case #3 - programming language:**

GBNF grammar can be more complicated. **This is a llama.cpp example, the grammar describes what words/symbols are allowed, in this case, it's all valid C.**

123456789101112131415161718192021222324252627282930313233343536373839404142434445464748495051525354555657585960616263646566676869707172737475767778798081828384858687888990919293949596

And then you can see our little mistral model came up with an ugly but correct C program

123

**Enabling Product Innovation on Fireworks**

JSON and grammar mode represent an important improvement in LLM usability by enabling controllable output with guaranteed accuracy. Spend less time fiddling with your system prompt wordings or few-shot examples! JSON mode and grammar mode make it easier than ever to build complex systems where LLMs programmatically call functions or pipe output to other systems.

Fireworks is committed to providing the best platform for Generative AI product innovation and the best experience for structured output. Compared to other providers, we’re excited to offer JSON mode with blazing fast speed for low-latency cases. In our benchmarks, our JSON mode provided 120 tokens/sec while the average “JSON mode” from competing platforms generated 30 tokens/sec.

Beyond JSON mode, we’re the only inference platform that we’re aware of with grammar mode. We’ve also just released our own “FireFunction” function calling models (see [docs](https://docs.fireworks.ai/guides/function-calling)) for more complex use cases that require intent detection in addition to structured output. The model excels at tasks like making decisions between multiple structured schemas or deciding how to fill more complex schemas.

Get started today with our docs on [JSON mode](https://docs.fireworks.ai/structured-responses/structured-response-formatting) and [grammar mode](https://docs.fireworks.ai/structured-responses/structured-output-grammar-based) to get 100% syntactically correct output and dramatically improved end-to-end accuracy for your application! Visit the Fireworks [models](https://fireworks.ai/models) page to get started with any of our Fireworks-hosted models - served at blazing fast speeds and an OpenAI-compatible API. Use JSON mode and grammar mode with any of these models to bring unparalleled responsiveness and quality to your users.


We’d love to hear what you think! Please join the function calling channel on our [Discord](https://discord.gg/mMqQxvFD9A) community to discuss our structured output offerings with the team. Happy building!
