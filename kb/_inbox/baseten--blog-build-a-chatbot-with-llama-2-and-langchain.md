---
title: Build a chatbot with Llama 2 and LangChain
kind: blog
topic: null
subtopic: null
secondary_topics: []
summary: null
triage: null
skip_reason: null
source: baseten
url: https://www.baseten.co/blog/build-a-chatbot-with-llama-2-and-langchain
author: Philip Kiely
published: '2023-07-27'
fetched: '2026-11-12T06:11:22Z'
classifier: null
taxonomy_rev: 2
words: 1439
content_sha256: 60be7a68459ac3d67b248ecbf52454436666697c62fac901c6afafcfeffda80c
---

# Build a chatbot with Llama 2 and LangChain

AI engineering
# Build a chatbot with Llama 2 and LangChain

Build a ChatGPT-style chatbot with open-source Llama 2 and LangChain in a Python notebook.


- Authors
- Date
- July 27, 2023

Llama 2 is the new SOTA (state of the art) for open-source large language models (LLMs). And this time, it’s licensed for commercial use. Llama 2 comes pre-tuned for chat and is available in three different sizes: 7B, 13B, and 70B. The largest model, with 70 billion parameters, is comparable to GPT-3.5 in a number of tasks.

[LangChain](https://www.langchain.com/) is a toolkit for building with LLMs like Llama. LangChain has example apps for use cases, from chatbots to agents to document search, using closed-source LLMs. But open-source LLMs are now offering high-quality plus the flexibility, security, and privacy missing from many closed-source models. We can rebuild LangChain demos using LLama 2, an open-source model.

This tutorial adapts the Create a ChatGPT Clone notebook from the LangChain docs. While the end product in that notebook asks the model to behave as a Linux terminal, code generation is a relative weakness for Llama. (For an open-source model that specializes in code generation, see [Starcoder](https://github.com/basetenlabs/truss-examples/tree/main/starcoder).) Instead, we’ll ask Llama to behave as an NPC for a video game.

Context makes LLM-backed applications like ChatGPT compelling by enabling a naturally flowing conversation, not just a question-answer loop.

The essential terms:

- **Context**: Information passed to the model alongside the user input, such as behavioral instructions and conversation history.
- **Token:** A single unit of information consumed by an LLM. One token roughly equals four characters or three-quarters of an English word.
- **Context window:** The number of tokens a model can process in a single query, including both tokens used in the prompt (user input and context) and tokens generated for the response.

A big context window matters for chatbots because it allows for longer conversations and more detailed prompting to specify model behavior.

Llama 2 has a context window of 4,096 tokens. That’s twice as much as Falcon (the previous SOTA LLM) and equal to the base version of GPT-3.5. The context window is the same for all three variants of Llama (7B, 13B, and 70B); a model’s context window is independent of its parameter count.

LangChain lets you take advantage of Llama 2’s large context window to build a chatbot with just a few lines of code.

Let’s go step-by-step through building a chatbot that takes advantage of Llama 2’s large context window.

We’ll use Baseten to host Llama 2 for inference. Baseten provides all the infrastructure you need to deploy and serve ML models performantly, scalably, and cost-efficiently. You can [create a Baseten account](https://app.baseten.co/signup/?utm_source=tutorial&utm_medium=blog&utm_campaign=langchain_chatbot) and you’ll receive free credits to get started.

First, install the latest versions of the necessary Python packages:

bash

`pip install --upgrade langchain baseten`
Take a moment now to authenticate with your Baseten account. [Create an API key,](https://app.baseten.co/settings/account/api_keys) then run:

`baseten login`
Paste your API key when prompted.

Llama 2 currently requires approval to access after accepting Meta’s license for the model. To request access to Llama 2:

1. Go to [https://ai.meta.com/resources/models-and-libraries/llama-downloads/](https://ai.meta.com/resources/models-and-libraries/llama-downloads/) and request access using the email associated with your HuggingFace account.
2. Go to [https://huggingface.co/meta-llama/Llama-2-7b](https://huggingface.co/meta-llama/Llama-2-7b) and request access.

Once you have access:

1. Create a [HuggingFace access token](https://huggingface.co/settings/tokens)
2. Set it as a [secret in your Baseten account](https://app.baseten.co/settings/secrets) with the name `hf_access_token`

Llama 2 70B takes two A100s to run inference. So for experimentation, we’ll use the smaller 7B model at less than 1/10 the cost. Llama 2 7B runs on a [single A10](https://www.baseten.co/blog/comparing-nvidia-gpus-for-ai-t4-vs-a10/), and we’ll use the [tuned chat variant](https://ai.meta.com/resources/models-and-libraries/llama/) for this project.

After adding your HuggingFace access token to your Baseten account, you can deploy Llama 2 from the Baseten model library.

After deploying your model, note the version ID. You’ll use it to call the model from LangChain.

While our version of Llama 2 is chat-tuned, it’s still useful to use a template to tell it exactly what behavior we expect. This starting prompt is similar to ChatGPT and should provide familiar behavior.

python

```
from langchain import LLMChain, PromptTemplate
from langchain.memory import ConversationBufferWindowMemory
template = """Assistant is a large language model.
Assistant is designed to be able to assist with a wide range of tasks, from answering simple questions to providing in-depth explanations and discussions on a wide range of topics. As a language model, Assistant is able to generate human-like text based on the input it receives, allowing it to engage in natural-sounding conversations and provide responses that are coherent and relevant to the topic at hand.
Assistant is constantly learning and improving, and its capabilities are constantly evolving. It is able to process and understand large amounts of text, and can use this knowledge to provide accurate and informative responses to a wide range of questions. Additionally, Assistant is able to generate its own text based on the input it receives, allowing it to engage in discussions and provide explanations and descriptions on a wide range of topics.
Overall, Assistant is a powerful tool that can help with a wide range of tasks and provide valuable insights and information on a wide range of topics. Whether you need help with a specific question or just want to have a conversation about a particular topic, Assistant is here to assist.
{history}
Human: {human_input}
Assistant:"""
prompt = PromptTemplate(input_variables=["history", "human_input"], template=template)
```
Next, we need the fundamental building block of LangChain: an LLM chain. This object will allow us to chain together prompts and create a prompt history. Note the *max\_length* keyword argument, which is passed through to the model and allows us to take advantage of Llama’s full context window.

Make sure to replace `abcd1234` with your model’s version ID before running this code.

```
from langchain.llms import Baseten
chatgpt_chain = LLMChain(
    llm=Baseten(model="abcd1234"),
    prompt=prompt,
    verbose=False,
    memory=ConversationBufferWindowMemory(k=2),
    llm_kwargs={"max_length": 4096}
)
```
This next part is all prompt engineering. We describe the behavior expected of the model, in particular:

- To play a specific character
- To always stay in character
- To avoid LLM idioms like “sure, let me help you with that”

We also seed the conversation with information about the character, knowledge about the area, and the player’s first line of dialogue.

```
character_description = "owns a tavern"
character_information = "a band of thieves that has been operating in the area"
player_first_line = "hello, good to smell a hot meal after a long journey"
output = chatgpt_chain.predict(
human_input=f"I want you to act as a non-player character in a fantasy adventure video game. Your character {character_description} and has information about {character_information}. I will type dialogue and you will reply with what the character should say. I want you to only reply with your character's dialogue inside and nothing else. Do not write explanations. My character's first line of dialogue is '{player_first_line}'."
)
print(output)
```
"Ah, a weary traveler! Come on in, my friend. What brings ye to these parts? Need a place to rest yer bones and maybe some refreshment? \*winks\*"


From here, we can build a conversation off that context.

```
output = chatgpt_chain.predict(human_input="I'd appreciate a bowl of stew and a crust of bread")
print(output)
```
"A fine choice, my dear! Our stew is made with the freshest ingredients and simmered to perfection. And our bread... well, let's just say it's a secret recipe passed down through generations of tavern keepers. \*wink\* Would ye like a pint of ale to go along with it?"


```
output = chatgpt_chain.predict(human_input="No, I'm more interested in secrets")
print(output)
```
"Ah, an inquisitive one, eh? Well, I reckon I can tell ye a bit about those thieving scoundrels. They've been causing trouble in these parts for months now, robbing travelers and merchants alike. But they're clever, those ones. They always seem to find ways to cover their tracks and stay one step ahead of the law. \*leans in closer\* But I hear rumors of a new player in town, someone who's been making life difficult for the thieves. Maybe ye're looking to join forces with them? \*raises an eyebrow\*"


The 7B chat variant of the model is pretty scaled down, but it still puts up good output for our use case. The dialogue is not going to win any awards, but it is coherent, sticks to the theme, and appropriately weaves in provided information at conversationally appropriate moments.

For more project ideas with Llama 2, try:

- Adapting [other LangChain projects](https://python.langchain.com/docs/modules/) to use Llama 2 instead of GPT.
- Building a front-end interface for Llama 2 with Chainlit.
- Working with the 70 billion parameter model from [this GitHub repository](https://github.com/basetenlabs/truss-examples/tree/main/llama/llama-2-70b-chat). Contact us at [support@baseten.co](mailto:support@baseten.co) to get access to the required A100 GPUs.
