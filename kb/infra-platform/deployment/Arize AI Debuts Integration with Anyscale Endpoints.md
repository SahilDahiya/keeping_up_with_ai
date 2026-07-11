---
title: Arize AI Debuts Integration with Anyscale Endpoints
topic: infra-platform
subtopic: deployment
secondary_topics:
- inference/serving
summary: Announcement and integration walkthrough for using Arize with Anyscale Endpoints
  to monitor hosted open-model inference.
source: arize
url: https://arize.com/blog/anyscale-endpoints-code-along/
author: Gabe Barcelos
published: '2023-09-19'
fetched: '2026-07-11T04:47:41Z'
classifier: codex
taxonomy_rev: 1
words: 743
content_sha256: c6bc4462b3dc935e24ee581f0080fc47238112b8ba5f23c8d4fbf39ad277d87e
---

# Arize AI Debuts Integration with Anyscale Endpoints

At Ray Summit 2023, [Anyscale Endpoints](https://app.endpoints.anyscale.com/landing) – a new service enabling developers to integrate fast, cost-efficient, and scalable large language models (LLMs) into their applications using popular LLM APIs – made its grand debut. The service promises to be “the fastest way to fine-tune and deploy powerful open-source LLMs at scale.”

In addition to Hugging Face and Weights & Biases, Arize AI is proud to be a launch partner of Anyscale Endpoints. Through an early integration, Arize and Anyscale Endpoints enable developers to achieve LLM observability across different use cases on any cloud as their AI applications evolve.

This code-along blog and [accompanying Colab](https://colab.research.google.com/gist/PubliusAu/1298e5ddadade67f88081577aa8c2a36/arize_anyscale_endpoints_integration_2023.ipynb) dive into how to get started with Anyscale Endpoints and the integration, including:

- Importing and setting up the Arize client
- Defining a chat model supported by Anyscale Endpoints
- Testing LLM responses and logging into Arize
- Testing LLM chains and agents with Arize integration

## Install Dependencies, Import Libraries, Use GPU 📚

To get started, let’s import LangChain, Arize, and Arize CallBack Handler to set up an integration between the two tools.

*💡**PRO TIP**: Try using a GPU to save time generating embeddings. Click on ‘Runtime’, select ‘Change Runtime Type’ and select ‘GPU’.*

```
!pip install -q arize[AutoEmbeddings]
!pip install -q langchain
!pip install -q openai
```
```
from langchain.callbacks.arize_callback import ArizeCallbackHandler
from langchain.chat_models import ChatAnyscale
from langchain.schema import SystemMessage, HumanMessage
from langchain.callbacks import StdOutCallbackHandler
from langchain.callbacks.manager import CallbackManager
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SimpleSequentialChain
```
If you have not done so yet, [sign up for a free Arize account](https://app.arize.com/auth/join).

## Step One: Import and Set Up Arize Client

The first step is to set up our Arize client. After that. we will log the data from Anyscale LangChain-driven applications into Arize.

Retrieve your Arize API_KEY and SPACE_KEY from Arize’s Space Settings page, and paste them in the set-up section below.

We will also set up some metadata and the ArizeCallBackHandler to use while logging.

![arize copy keys](https://arize.com/wp-content/uploads/2023/09/arize-keys.png)

```
ARIZE_SPACE_KEY =  "YOURSPACEKEY"
ARIZE_API_KEY = "YOURAPIKEY"
if ARIZE_SPACE_KEY == "YOUR_SPACE_KEY" or ARIZE_API_KEY == "YOUR_API_KEY":
   raise ValueError("❌ CHANGE SPACE AND API KEYS")
# Define callback handler for Arize
arize_chat_callback = ArizeCallbackHandler(
   model_id="anyscale-langchain-demo-1",
   model_version="meta-llama/Llama-2-70b-chat-hf",
   SPACE_KEY=ARIZE_SPACE_KEY,
   API_KEY=ARIZE_API_KEY
)
manager = CallbackManager([StdOutCallbackHandler(), arize_chat_callback])
```
## Step Two: Define Chat Model Supported by Anyscale Endpoints

Before getting started, [sign up for Anyscale Endpoints](https://app.endpoints.anyscale.com/landing) to obtain an ANYSCALE_ENDPOINT_TOKEN.

In this example, we’ll use meta-llama/Llama-2-70b-chat-hf

Define the chat model thusly:

```
ANYSCALE_ENDPOINT_TOKEN = "YOURTOKEN"
MODEL = "meta-llama/Llama-2-70b-chat-hf"
chat = ChatAnyscale(anyscale_api_key=ANYSCALE_ENDPOINT_TOKEN,model_name=MODEL, temperature=1.0, callback_manager=manager)
```
## Step Three: Test LLM Responses and Logging Into Arize

Next, let’s use some simple prompts to test if the LLM works properly and each prompt-response pair is logged into Arize with embeddings.

```
messages = [
   SystemMessage(
       content="You are a helpful AI that shares everything you know."
   ),
   HumanMessage(
       content="How to evaluate the value of a NFL team"
   ),
]
chat.apredict_messages(messages, callbacks=[arize_chat_callback])
```
## Step Four: Test LLM Chain and Agents with Arize Integration

Finally, let’s bring everything together and test the LLM chain and agents with the Arize integration.

```
template = """You are a playwrighter. Given the title of play, it is your job to write a synopsis for that title.
Title: {title}
Playwright: This is a synopsis for the above play:"""
prompt_template = PromptTemplate(input_variables=["title"], template=template)
synopsis_chain = LLMChain(llm=chat, prompt=prompt_template, callback_manager=manager)
overall_chain = SimpleSequentialChain(
   chains=[synopsis_chain], callback_manager=manager
)
test_prompts = [
   {
       "input": "documentary about pandas who are about be extinct because of global warming"
   },
   {"input": "once upon a time in hollywood"},
   {"input": "the best model observability tooling"},
   {"input": "childrens play about a frog living in an alpine lake just discovered by humans"},
   {"input": "utopian society being disrupted by new AI"},
]
overall_chain.apply(test_prompts)
```
In the *LLM performance tracing* tab in Arize, you can see that all prompts and responses are recorded and any additional metadata associated with the chain – including things like completion tokens, prompt token, total, and timestamp – are present.

![anyscale endpoints tutorial code along](https://arize.com/wp-content/uploads/2023/09/anyscale_endpoint_integration_demo_tutorial_code.png)

From there, you can dive into the Arize *LLM Dashboard* with standard and custom metrics for any given use case.

![arize llm monitoring dashboard](https://arize.com/wp-content/uploads/2023/09/llm-analytics-dashboard.png)

## Conclusion

As the open source LLM ecosystem expands and enterprises look to build and take more LLM-powered systems into production environments using tools like Anyscale Endpoints, there is a distinct need for better tools for [LLM evaluation](https://arize.com/blog-course/assessing-large-language-models/) and observability. With this integration, teams can ensure they have the tools necessary to achieve that vision and better troubleshoot LLMs in real-world environments.
