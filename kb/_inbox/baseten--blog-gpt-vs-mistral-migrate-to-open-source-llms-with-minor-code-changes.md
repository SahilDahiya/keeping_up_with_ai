---
title: 'GPT vs Llama: Migrate to open source LLMs seamlessly'
kind: blog
topic: null
subtopic: null
secondary_topics: []
summary: null
triage: null
skip_reason: null
source: baseten
url: https://www.baseten.co/blog/gpt-vs-mistral-migrate-to-open-source-llms-with-minor-code-changes
author: Sid Shanker
published: '2023-11-21'
fetched: '2026-11-12T06:11:36Z'
classifier: null
taxonomy_rev: 2
words: 863
content_sha256: d4853fcc964f7d08f10a5c53149a0b3e77c4e9cde632461e281dab9844d54745
---

# GPT vs Llama: Migrate to open source LLMs seamlessly

AI engineering
# GPT vs Llama: Migrate to open source LLMs seamlessly

Use ChatCompletions API to test open-source LLMs like Llama in your AI app with just three minor code modifications.


- Authors
- Date
- November 21, 2023

TLDR

If you’re using the ChatCompletions API and want to experiment with open source LLMs for your generative AI application, we’ve built a bridge that lets you try out models like Llama with just three tiny code changes.

In the past few months, researchers have released powerful open source large language models like Llama and Qwen. [Open source LLMs](https://www.baseten.co/blog/the-best-open-source-large-language-model/) demonstrate strong capabilities on tasks from chat completion to code generation, and [many can be run on cost-effective hardware](https://www.baseten.co/blog/using-fractional-h100-gpus-for-efficient-model-serving/).

One barrier to adopting open source ML models is the time it takes to re-integrate the new model into your application. Models have different input and output formats, support different parameters, and require different prompting strategies.

To make it easier to experiment with open source models, we’ve created a new endpoint for LLMs hosted on Baseten that’s compatible with OpenAI’s ChatCompletions API. With this endpoint and a supported model, you can go from GPT-3.5 to open source LLMs like Llama 3.1 with:

- One-click model deployment.
- Zero `pip install` commands.
- Three tiny code changes.

Follow along with the video above or the tutorial below and you’ll be working with open source LLMs in no time!

Any LLM can be implemented with an OpenAI-compatible model server. In particular, vLLM servers are OpenAI compatible out of the box, and TensorRT-LLM Engine Builder servers can be made compatible by adding metadata to the `config.yaml`.

Let’s deploy Llama 3.2 11B for this tutorial:

1. Select [Llama 3.2 11B](https://www.baseten.co/library/llama-3-2-11b-vision-instruct/) from the model library.
2. Click “Deploy on Baseten”
3. Get your model ID by opening the “Call model” modal and copying it from the model endpoint.
4. [Create an API key](https://app.baseten.co/settings/api_keys) for your Baseten workspace with the “Generate API key” button.

You’ll need the API key and model ID to call the model endpoint in the next step.

Note that with open source models deployed on Baseten, you’re [charged per minute of GPU usage](https://baseten.co/pricing) rather than per token. Your Baseten account comes with free credits to fund experimentation, and all models deployed from the model library automatically take advantage of scale to zero with fast cold starts to save you money while the model is not in use.

Here’s the fun part of the project: you can drop this model into existing code that uses the ChatCompletions API with only minor changes.

In fact, the code will still use the OpenAI Python client, so you don’t need to install any new libraries. Let’s take a look at some code, we’ll cover the differences below.

Here’s a code sample for using OpenAI’s ChatCompletions API with GPT-3.5:

python

```
from openai import OpenAI
import os
client = OpenAI(
    api_key=os.environ["OPENAI_API_KEY"]
)
response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": "Who won the world series in 2020?"},
        {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
        {"role": "user", "content": "Where was it played?"}
    ]
)
print(response.choices[0].message.content)
```
And here’s the same code sample for Mistral on Baseten:

```
from openai import OpenAI
import os
client = OpenAI(
    # api_key=os.environ["OPENAI_API_KEY"],
    api_key=os.environ["BASETEN_API_KEY"],
    # Add base_url
    base_url="https://bridge.baseten.co/{model_id}/v1"
)
response = client.chat.completions.create(
    # model="gpt-3.5-turbo",
    model="llama-3-2-11b",
    messages=[
        {"role": "user", "content": "Who won the world series in 2020?"},
        {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
        {"role": "user", "content": "Where was it played?"}
    ]
)
print(response.choices[0].message.content)
```
Rather than making you play spot-the-difference, we’ll highlight the three small code changes that make this work:

1. Replace the `OPENAI_API_KEY` with your `BASETEN_API_KEY` in the `client` object.
2. Set the `base_url` in the `client` object to `https://bridge.baseten.co/{model_id}/v1` where `{model_id}` is the ID of your deployed model.
3. In the `client.chat.completions.create()` call, set `model` to `llama-3-2-11b` instead of `gpt-3.5-turbo`.

The response format will be exactly the same, though token usage values will not be calculated. The endpoint reference docs have complete information on supported inputs and outputs.

LLMs on Baseten can also support streaming. To stream Llama responses, pass `stream=True` in the ChatCompletion API call, and parse the streaming response as needed:

```
from openai import OpenAI
import os
client = OpenAI(
    # api_key=os.environ["OPENAI_API_KEY"],
    api_key=os.environ["BASETEN_API_KEY"],
    # Add base_url
    base_url="https://bridge.baseten.co/{model_id}/v1"
)
response = client.chat.completions.create(
    # model="gpt-3.5-turbo",
    model="llama-3-2-11b",
    messages=[
        {"role": "user", "content": "Who won the world series in 2020?"},
        {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
        {"role": "user", "content": "Where was it played?"}
    ],
    stream=True
)
for chunk in response:
    print(chunk.choices[0].delta)
```
Any LLM can be served with an OpenAI-compatible ChatCompletions model server. Get started by adapting an example, like [this implementation of Ultravox](https://github.com/basetenlabs/truss-examples/tree/main/custom-server/ultravox-0.4), or let us know what you need at [support@baseten.co](mailto:support@baseten.co).

And while this bridge makes it easier to get started with LLMs like Mistral, there’s a wide world of open source models to explore. Our [model library](https://www.baseten.co/library) hosts dozens of curated open source models ranging from LLMs to models like [FLUX](https://www.baseten.co/library/flux-schnell/) and Whisper. Get started with our [checklist for switching to open source](https://www.baseten.co/blog/a-checklist-for-switching-to-open-source-ml-models/) or dive deeper with our [guide to open source alternatives for ML models](https://www.baseten.co/blog/open-source-alternatives-for-machine-learning-models/).
