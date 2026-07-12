---
title: Building AI Assistants with Vectara-agentic and Arize
topic: rag-retrieval
subtopic: pipelines
secondary_topics:
- agents/tool-use
summary: Shows how to build AI assistants with Vectara-agentic and Arize, tying retrieval,
  agent tools, and observability together.
source: arize
url: https://arize.com/blog/vectara-agentic/
author: Ofer Mendelevitch; John Gilhuly
published: '2024-10-03'
fetched: '2026-07-11T04:50:12Z'
classifier: codex
taxonomy_rev: 1
words: 1078
content_sha256: e6ffde43507ad2728350fc30100baaa2edd6b7d591547c43bba74ad273b189fb
---

# Building AI Assistants with Vectara-agentic and Arize

*Co-Authored by Ofer Mendelevitch, Head of Developer Relations, Vectara & John Gilhuly, Developer Advocate.*

*Thanks to the Vectara team for contributing this post!*

# Introduction

Retrieval-Augmented Generation (RAG) is a framework that enhances the capabilities of large language models (LLMs) by integrating external information retrieval systems to provide more relevant and factual responses.

In a standard RAG setup, the model retrieves documents from a knowledge base, and feeds those documents into a generative model to create informed and contextually relevant outputs. This allows RAG to reduce hallucinations by grounding the model’s responses in real-world data.

However, RAG systems are typically passive; they rely on pre-defined retrieval strategies and lack the ability to dynamically adapt their approach or decision-making based on evolving tasks.

Agentic RAG, on the other hand, introduces an element of autonomy and decision-making to the RAG framework. In this enhanced version, the system can make choices about which tools or retrieval strategies to use depending on the context of the task.

Agentic RAG might decide to invoke different APIs, consult diverse sources, or adjust its retrieval behavior in real-time, making it more flexible and capable of handling complex workflows to answer user queries or perform tasks for the user.

[Vectara-agentic](https://github.com/vectara/py-vectara-agentic) is an Agentic RAG package (in Python) that allows developers to quickly and easily develop AI assistants and agents using Vectara.

Today we are announcing the integration of [Arize Phoenix](https://phoenix.arize.com/), a leading open-source observability tool, into vectara-agentic. In this blog post we will show how to use vectara-agentic to build a simple AI assistant, and how to use Arize Phoenix to gain insight into its operation.

Let’s get started!

# EV Assistant

Let’s explore the “[EV assistant](https://huggingface.co/spaces/vectara/ev-assistant)” application created with vectara-agentic, that helps answer questions about electric vehicles.

We started by ingesting the data into two Vectara corpora. The first corpus focuses on general EV information, including content about electric vehicles from websites like [driveclean](https://driveclean.ca.gov/), [edmunds](https://www.edmunds.com/), [greenlancer](https://greenlancer.com/), [epa.gov](http://epa.gov) and [energy.gov](http://energy.gov). The second corpus focuses on laws and regulations, based on data in *laws_and_incentives.csv* from the [AFDC website](https://afdc.energy.gov/) (data ingested into Vectara using [vectara-ingest](https://github.com/vectara/vectara-ingest) with the CSV crawler).

In addition, we created a sample database with registration information about EVs, taken from [electric-vehicle-title-and-registration-activity](https://catalog.data.gov/dataset/electric-vehicle-title-and-registration-activity), which includes 3 tables, covering the state of Washington: Electric Vehicle Title and Registration Activity, Electric Vehicle Population Data, and Electric Vehicle Population Size History By County.

We then used vectara-agentic to define the following [tools](https://huggingface.co/spaces/vectara/ev-assistant/blob/main/agent.py):

- *ask_vehicles*: a RAG tool to ask general questions from the first corpus about EVs.
- *ask_policies*; a RAG tool to ask questions from the second corpus about law and incentives.
- ToolsFactory.database_tools() which provides a set of tools for querying 3 tables in the database

Then the agent itself is simple to generate:

```
agent = Agent(
        tools=tools
        topic="Electric vehicles in the United States",
        custom_instructions=ev_instructions
    )
```

Where we have provided explicit [instructions](https://huggingface.co/spaces/vectara/ev-assistant/blob/main/agent.py#L92) to our EV assistant. The instructions are important, you have to make sure you don’t overdo them, but provide enough information to the bot to understand the desired behavior.

# Adding Observability

Now that our EV assistant is ready, let’s add some observability using the integration with Arize Phoenix. This will allow us to see what happens during the query and understand how it works.

To do this, we first install Arize Phoenix locally, and run it:

```
pip install arize-phoenix
python -m phoenix.server.main serve
```

Now that the server is running, we set the vectara-agentic environment variable to enable Arize observability:

VECTARA_AGENTIC_OBSERVER_TYPE=”ARIZE_PHOENIX”

This tells vectara-agentic to send instrumentation of all agent activities into your local Phoenix server, and record them. The integration will also ingest Vectara’s Factual Consistency Score (FCS) for RAG calls, and visualize scores in Phoenix.

And that’s it. We are ready to go!

# EV Assistant in Action

Let’s start by asking this question:

agent.chat(“What are the environmental impact of EVs?”)

The response is shown in the screenshot below:

![](https://arize.com/wp-content/uploads/2024/10/Screenshot-2024-10-02-at-12.30.59 PM.png)

*Figure 1: vectara-agentic based application in response to the question “What are the environmental impacts of EVs?”*

Since we enabled Arize Phoenix observability we can go to localhost:6006 to see what happened during the execution of this query:

![](https://arize.com/wp-content/uploads/2024/10/Screenshot-2024-10-02-at-12.32.06 PM.png)

*Figure 2: screenshot of Arize Phoenix UI showing the main traces with vectara-agentic*

If we click on the trace itself, we can see more details about what happened internally:

![](https://arize.com/wp-content/uploads/2024/10/Screenshot-2024-10-02-at-12.32.14 PM.png)

*Figure 3: Trace details showing Agent thought process*

As we can see the agent decided that it needs to call the *ask_vehicles* tool with the question “what types of electric vehicles exist”?

And then the agent proceeds to actually call the tool and get the response back.

If I then ask a different question like:

agent.chat(“How have EV registration numbers in Washington changed over the past few years?”)

We get the following output:

![](https://arize.com/wp-content/uploads/2024/10/Screenshot-2024-10-02-at-12.32.24 PM.png)

*Figure 4: vectara-agentic based application in response to the question “How have EV registration numbers in Washington changed over the past few years?”*


You can follow the traces in this case and see that the agent chose to use the database tools:

- First it runs *ev_list_tables*to learn that it has the following tables available: ‘county_registrations’, ‘ev_population’, ‘ev_registrations’
- Then it calls*ev_load_sample_data*to get a sense of the data in the selected table (ev_registrations), and then*ev_load_data*, with the exact correct SQL query to get the result needed.

This demonstrates one of the best features of Agentic RAG: the agent not only knew to use the right tools (in this case database tools), but was also able to inspect the data in those tables and craft the correct SQL query to use with the tool to match the user query.


# Conclusions

Vectara-agentic provides an easy way to create Agentic RAG applications, and its integration with Arize Phoenix provides a quick and easy to add observability capabilities so that it’s easy to look under the hood of your agent as it operates.

This is especially important in order to ensure that the agent behaves in the way you intended in terms of inputs, outputs, tool choice as well as latency and LLM use.

Check out our open source Agentic RAG demos: [finance-assistant](https://huggingface.co/spaces/vectara/finance-assistant), [legal-assistant](https://huggingface.co/spaces/vectara/legal-assistant), [ev-assistant](https://huggingface.co/spaces/vectara/ev-assistant) and our [hacker news assistant](https://huggingface.co/spaces/vectara/hacker-news-chat), all built with vectara-agentic.

To build your own Agentic RAG application, you can [sign up](https://console.vectara.com/signup?utm_source=vectara&utm_medium=signup&utm_term=DevRel&utm_content=blog&utm_campaign=vectara-signup-DevRel-blog) for a free Vectara account, upload your data, and look at [vectara-agentic docs](https://vectara.github.io/vectara-agentic-docs/) for more details. If you need help you can find us in the Vectara [discussion forum](https://discuss.vectara.com/) or on [Discord](https://discord.gg/GFb8gMz6UH).

And if you haven’t, get started with [Phoenix](https://phoenix.arize.com/) today!
