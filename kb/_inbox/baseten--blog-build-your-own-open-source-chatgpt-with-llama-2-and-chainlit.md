---
title: Build your own open-source ChatGPT with Llama 2 and Chainlit
kind: blog
topic: null
subtopic: null
secondary_topics: []
summary: null
triage: null
skip_reason: null
source: baseten
url: https://www.baseten.co/blog/build-your-own-open-source-chatgpt-with-llama-2-and-chainlit
author: Philip Kiely
published: '2023-08-23'
fetched: '2026-11-12T06:11:24Z'
classifier: null
taxonomy_rev: 2
words: 1053
content_sha256: 40d3f618346fd12cba6127afcba150319b19e13f8c4f767f171b05349a773f65
---

# Build your own open-source ChatGPT with Llama 2 and Chainlit

AI engineering
# Build your own open-source ChatGPT with Llama 2 and Chainlit

Llama 2 rivals GPT-3.5 in quality and powers ChatGPT. Chainlit helps build ChatGPT-like interfaces. This guide shows creating such interfaces with Llama 2.


- Authors
- Date
- August 23, 2023

Llama 2 is a recent open-source large language model (LLM) that is [competitive on results quality with GPT-3.5](https://ai.meta.com/research/publications/llama-2-open-foundation-and-fine-tuned-chat-models/), the closed-source LLM that powers ChatGPT. AI-powered products like ChatGPT require high model quality, but model quality alone isn’t enough to make a compelling user experience.

[Chainlit](https://github.com/Chainlit/chainlit) is an open-source tool for creating a ChatGPT-style interface on top of any LLM. We’ll use it to get a chat UI out of the box with support for streaming model output, prompt history, context-aware chat, chat restart, and many other essential features.

This tutorial takes you through the [Baseten + Llama 2 Chainlit cookbook](https://github.com/Chainlit/cookbook/tree/main/baseten-llama-2-chat) to build a ChatGPT-style interface for your favorite open source LLMs like Llama 2.

It took ChatGPT [two months to hit 100 million users](https://www.reuters.com/technology/chatgpt-sets-record-fastest-growing-user-base-analyst-note-2023-02-01/). What makes it such a compelling user experience, and how can we match that with open-source tools?

1. **Quality output:** GPT-3.5 is a very capable model that creates coherent output for a variety of topics. As of Llama 2, we now have an open-source model that performs comparably across most benchmarks.
2. **Conversation in context:** ChatGPT goes beyond a question-answer loop to pass the message history into each model call, making chat feel like a natural conversation. We can do the same thanks to Llama 2’s 4096-token context window (which matches GPT-3.5 base).
3. **Streaming output:** ChatGPT feels fast because you get the first word of the result as soon as it’s generated rather than waiting for the full response. Baseten also [supports streaming model output](https://www.baseten.co/resources/changelog/stream-model-output/).
4. **Prompt history:** The ChatGPT web UI includes a number of quality-of-life features like prompt history, which we’ll get out of the box from Chainlit.

Plus, our open source version adds the security and privacy of running a private instance of the model on [SOC 2 Type II certified](https://www.baseten.co/blog/soc-2-type-2/) and [HIPAA compliant](https://www.baseten.co/blog/baseten-announces-hipaa-compliance/) infrastructure. And you use whatever open-source LLM best matches your specific use case.

With Llama-2 on Baseten as the backend and Chainlit as the front-end, let’s build an open-source ChatGPT.

To follow along, [download the Chainlit cookbook from GitHub](https://github.com/Chainlit/cookbook/tree/main/baseten-llama-2-chat).

Llama 2 currently requires approval to access after accepting Meta’s license for the model. To request access to Llama 2:

1. Go to [https://ai.meta.com/resources/models-and-libraries/llama-downloads/](https://ai.meta.com/resources/models-and-libraries/llama-downloads/) and request access using the email associated with your HuggingFace account.
2. Go to [https://huggingface.co/meta-llama/Llama-2-7b](https://huggingface.co/meta-llama/Llama-2-7b) and request access.

Once you have access:

1. Create a [HuggingFace access token](https://huggingface.co/settings/tokens)
2. Set it as a [secret in your Baseten account](https://app.baseten.co/settings/secrets) with the name `hf_access_token`

After you have the required access and have set the access token secret in your Baseten account, you can deploy Llama-2-chat 7B with just a couple of clicks from the Baseten model library.

You can also deploy the [13B](https://github.com/basetenlabs/truss-examples/tree/main/llama-2-13b-chat) or [70B versions](https://github.com/basetenlabs/truss-examples/tree/main/llama-2-70b-chat) of the model from GitHub. These models run on A100 GPUs, so inference is more expensive than the 7B variant, which runs on an A10.

To follow this step, [download the Chainlit cookbook from GitHub](https://github.com/Chainlit/cookbook/tree/main/baseten-llama-2-chat) and navigate to the `baseten-llama-2-chat` directory in your terminal.

First, install the latest version of Chainlit:

bash

`pip install --upgrade chainlit`
Open the file `.env.example` and do the following:

1. Set `BASETEN_API_KEY` to [an API key for your Baseten account](https://app.baseten.co/settings/account/api_keys)
2. Set `VERSION_ID` to the model version ID listed for Llama 2 on your model dashboard in your Baseten account
3. Rename `.env.example` to `.env`

With that configuration set, you’re ready to run the cookbook:

`chainlit run app.py -w`
This will open the Chainlit UI on localhost and you’ll be able to start chatting with Llama 2.

Rather than go through the whole `app.py` file line-by-line, let’s focus on three key details that make this chatbot work. You can [see the full file on GitHub](https://github.com/Chainlit/cookbook/blob/main/baseten-llama-2-chat/app.py).

Context is essential for the chatbot. Before sending the prompt to the model, prepend the prompt history from the Chainlit user session.

python

```
prompt_history = cl.user_session.get("prompt_history")
prompt = f"{prompt_history}{message}"
```
After the model response is generated and shown to the user, both the message and response are added to the prompt history and saved to the Chainlit user session.

```
prompt_history += message + response
cl.user_session.set("prompt_history", prompt_history)
```
We’re going to send a POST request to the model endpoint with the argument `stream=True` to get streaming output, then iterate over that response later in the code.

Note also the `max_new_tokens` argument which is used to make sure we take advantage of the full context window in Llama 2.

```
s = requests.Session()
with s.post(
    f"https://app.baseten.co/model_versions/{version_id}/predict",
    headers= {
        "Authorization": f"Api-Key {baseten_api_key}"
    },
    data=json.dumps({
        "prompt": prompt, # Prompt includes conversation history
        "stream": True, # Stream results a token at a time
        "max_new_tokens": 4096 # Use full context window
    }),
) as resp:
    # Process response here
```
When Llama 2 generates a response, its first seven characters are *\[/INST\]* which we want to strip from the output. That is a bit tricky with streaming, you can’t just parse the full output before showing it to the user.

Instead, in the response block, fill a buffer to grab those first seven characters, then once the buffer is full, stream the remaining output to the user.

```
buffer = ""
start_response = False
for token in resp.iter_content(1):
    token = token.decode('utf-8')
    buffer += token
    if not start_response:
        if "[/INST]" in buffer:
            start_response = True
    else:
        response += token
        await ui_msg.stream_token(token)
```
Let’s see how our all-open-source chatbot performs. Remember, we’re using the scaled-down 7B version.

Llama 2 is capable of expanding on the details of one option from a list:

Like all LLMs, Llama 2 has issues. Apparently, Neptune and Uranus are not real planets:

On its own, that’s just a series of hallucinations and contradictions. What makes it hilarious is the next chat, where Llama pretends to hallucinate then … changes its mind?

There’s a lot that you can build with Llama 2! If you want to work more with the model’s context window, try [our tutorial for building a chatbot with LangChain](https://www.baseten.co/blog/build-a-chatbot-with-llama-2-and-langchain/). And if you want to evaluate the most powerful version of the model, you can get [a packaged version of Llama 70B on GitHub](https://github.com/basetenlabs/truss-examples/tree/main/llama-2-70b-chat) that’s ready to deploy on Baseten.
