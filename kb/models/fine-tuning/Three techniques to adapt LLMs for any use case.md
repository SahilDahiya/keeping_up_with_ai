---
title: Three techniques to adapt LLMs for any use case
topic: models
subtopic: fine-tuning
secondary_topics:
- prompt-engineering/techniques
summary: Explains prompt engineering, fine-tuning, and related techniques for adapting
  LLMs to use cases.
source: baseten
url: https://www.baseten.co/blog/three-techniques-to-adapt-llms-for-any-use-case/
author: Philip Kiely
published: '2023-06-15'
fetched: '2026-07-11T04:10:56Z'
classifier: codex
taxonomy_rev: 1
words: 1114
content_sha256: 96b7ef6a212b3015d3fbc005d92ae3a0bfe16887d0fde2686496b93cbc9d1225
triage: keep
skip_reason: null
---

# Three techniques to adapt LLMs for any use case

![Three ways to adapt LLMs](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1747610618-llms-adapt.png%3Fauto%3Dformat%26fit%3Dcrop%26h%3D630%26w%3D1200&w=3840&q=100)

Large language models (LLMs) have powerful general capabilities out of the box: they can answer questions, write poems and stories, invent recipes, and write code. But they may not precisely fit your use case. Their answers may be too vague, poorly formatted, or even incorrect.

Fortunately, you can adapt LLMs to meet your needs. There are three levels of LLM customization:

1. Prompt engineering

2. Retrieval-augmented generation

3. Fine-tuning

Each level is an order of magnitude more difficult and expensive than the previous, but offers far more customization.

## Level 1: Prompt engineering

Use cases: data formatting, prompt chaining, copywriting, stylized writing, chat

Adding additional detail and context to prompts in order to improve model results is called “prompt engineering.” There are many different strategies for prompt engineering.

One method is called few-shot prompting. In an ordinary prompt, you ask the model directly for what you want—a poem, an essay, a Python function—without giving it any examples of the thing you want. This is called “zero-shot prompting,” and today’s LLMs are quite good at responding to zero-shot prompts. But giving one or more example inputs and outputs, called “one-shot” or “few-shot prompting” depending on the number of examples given, can give you even better results.

Few-shot prompting is especially useful for data formatting. By giving the model a couple of examples of unformatted and formatted data, you give it a pattern to match for your next input.

In the example below, ChatGPT doesn’t understand what converting an integer to a “float,” or floating-point number, means. But when given examples of similar conversions, it is able to convert the number correctly.

![A few-shot example teaches a chat model how to convert ints to floats](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1692717457-648a3c3e3ba048a17c1e3a63_wvhv1q2e8akqf8a5tkjenrr8f4xfzqmftmf9bfe9f2q6nryyz15dcrgn_f_hylqcpfcy7670b82ma2oghf7bqhzfsql1w1d6elwg0dim7ssnveprghuz4c35xqjeudqk-6mp6zbfzvkkjxvmsxsus3e.png%3Fauto%3Dformat%26w%3D1200&w=3840&q=75) A few-shot example teaches a chat model how to convert ints to floats

A few-shot example teaches a chat model how to convert ints to floatsBut prompt engineering doesn’t have to use few-shot examples. Sometimes, simply providing clearer, more explicit instructions is enough.

For example, let’s say you’re building an application to come up with menus and recipes. The open-source LLM [WizardLM](https://app.baseten.co/explore/wizardlm) provides a detailed response to my original query by default, but if you only need the dish’s name, you can specify that. Here’s the modified prompt:

![The highlighted text shows additional instructions given to the model during the prompt](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1692717480-648a3c3da248706e92c463ab_o4crvfkx7okwr5xwg0s22fj0ilklcmvz_nou-n5us0wk8ld0ecr9qhz2a2yoz_e7_zi4ot9g4qp9jmcjuyr7_cpfw735m9_9f3xd7bm2wn5febquwbrwmdavi6d8xvolqa72sgynou2vsrtv7pie7xu.png%3Fauto%3Dformat%26w%3D1200&w=3840&q=75) The highlighted text shows additional instructions given to the model during the prompt

The highlighted text shows additional instructions given to the model during the prompt### Prompt engineering cost

#### Up-front cost: low, ongoing cost: low.

Prompt engineering can actually make operating an LLM less expensive if your well-crafted prompt yields a useful answer the first time rather than taking multiple tries. Unless your prompt is incredibly long, the larger input will only marginally increase the cost of invoking the model. Overall, prompt engineering is an inexpensive and effective way to get a wide range of behaviors from an off-the-shelf model.

## Level 2: Retrieval-augmented generation

Use cases: document search, help center chatbots, domain-specific writing

Prompt engineering has its limits. If you try to provide a lot of inputs to an LLM—like passing in a textbook and asking the model to use it to answer a question—you’ll overload the model context window (the number of characters it can accept as input).

Adding a vector database like [Pinecone](https://www.trychroma.com/) or [Chroma](https://www.trychroma.com/) lets you embed extra information in every call to your LLM. Rather than passing the entire textbook to answer a question, use a vector database to select relevant context and efficiently provide it to the model. This lets you bring in or emphasize data that may have been missing from the model’s training dataset, such as up-to-date documentation for your product.

The clearest example use case for vector databases is making a chatbot for your help center or documentation—the vector database finds relevant snippets from the documentation based on each user query, then passes the query and those snippets to the chat model. For a concrete instance of this use case, here’s a demo of Stripe’s new LLM-backend docs search.

![Stripe previews their docs search experience](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1692717528-648a53bc99fbee4db795b602_smart_doc_flow_0314.gif%3Fauto%3Dformat%26w%3D1200&w=3840&q=75) Stripe previews their docs search experience

Stripe previews their docs search experience### Retrieval-augmented generation cost

#### Up-front cost: medium, ongoing cost: medium.

While embeddings from a vector database are a more efficient way to pass lots of data to a model, they still use more of a model’s context window, increasing invocation time and cost. Overall, using a vector database represents a moderate increase in engineering effort and maintenance cost but unlocks many use cases that require an LLM to be aware of your data.

## Level 3: Fine-tuning

Use cases: chat-style models, step-by-step reasoning, storytelling models

Vector databases are a great way to provide context to a model. But if you want to provide new corpuses of text on the order of hundreds of millions or billions of words, or modify the base behavior of a model, that’s where fine-tuning comes in.

Fine-tuning modifies the underlying model directly to add information and behavior. It can be used in combination with embeddings and prompt engineering.

One common use case for fine-tuning is taking a base open-source LLM and adapting it to a specific type of output, like chat. For example, Alpaca is a fine-tuned version of Llama that specializes in chat, and the standard for new open-source LLMs is to release both a standard foundation model and a fine-tuned chat or “instruct” variant of the model.

![Alpaca is a version of LLaMA fine-tuned for a chat interface](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1692717583-648a3c3d606e053b19e3e301_q30h_f7f1y7upn_byn9j2pew_k1z21bebegpisfvpz06du43-32q1j-2u2qu3lsjjpmsbf6ms1l3tqirv9zefseupcdoe-io3jekm7g7ema4smktpp0nysdzuqi6duhpi8-gnv4m6ryyuwmvvfpyxnk.png%3Fauto%3Dformat%26w%3D1200&w=3840&q=75) Alpaca is a version of LLaMA fine-tuned for a chat interface

Alpaca is a version of LLaMA fine-tuned for a chat interface### Fine-tuning cost

#### Up-front cost: high, ongoing cost: low.

Fine-tuning re-trains a portion of the LLM on new data. While not as time-consuming or expensive as training a model from scratch, major fine-tuning jobs can run for days on multiple GPUs, giving fine-tuning a higher up-front cost. But once the model is fine-tuned, running it returns the customized results you need for the same price as running the base model.

## Picking a customization option for your use case

Customization takes time and money. Always start with the most basic approach and try to get good results, then reach for more customization if the model’s outputs aren’t meeting your needs. First, try prompt engineering and few-shot prompting to demonstrate your desired results to the LLM. Then, see if a vector database would allow you to embed enough context in your inference to generate good answers. If neither approach seems sufficient, try fine-tuning to further alter the model’s behavior.

And of course, there’s always level 4: training your own LLM from scratch!
