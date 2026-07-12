---
title: Sharing LangSmith Benchmarks
topic: models
subtopic: benchmarks
secondary_topics:
- evals-observability/evaluation
summary: Shares LangSmith benchmarks for evaluating models and chains, including methodology
  and public comparison workflows.
source: langchain
url: https://www.langchain.com/blog/public-langsmith-benchmarks
author: The LangChain Team
published: '2023-11-22'
fetched: '2026-07-11T04:38:52Z'
classifier: codex
taxonomy_rev: 1
words: 1942
content_sha256: e235d2bb681897b6a97efc72a095c6873bec5f7d57c5005044217cda75da52d7
---

# Sharing LangSmith Benchmarks

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb0bae51c6ccf7873ca48_Dribbble-shot---1--1-.png)

The single biggest pain point we hear from developers taking their apps into production is around testing and evaluation. This difficulty is felt more acutely due to the constant onslaught of new models, new retrieval techniques, new agent types, and new cognitive architectures.

Over the past months, we've made LangSmith the best place to go for LLM architecture evaluation ([test comparison view](https://blog.langchain.com/test-run-comparisons/), [dataset curation](https://blog.langchain.com/announcing-data-annotation-queue/)). Today we're making it possible to share evaluation datasets and results, to more easily enable community-driven evaluation and benchmarks. We're also excited to share the new [ langchain-benchmarks](https://langchain-ai.github.io/langchain-benchmarks/index.html?ref=blog.langchain.com)  package so you can reproduce these results and easily experiment with your architecture.

Test sharing makes it easy for anyone on LangSmith to publish all the data and metrics on how different architectures perform on the same set of tasks. As an added benefit, we're not just logging the end results - each evaluation result includes the full accompanying traces for the tested chains. This means you can go beyond aggregate statistics and system-level outputs and see the step-by-step execution of different systems on the same data point.

🦜

The first benchmark we are releasing is a [Q&A dataset](https://smith.langchain.com/public/452ccafc-18e1-4314-885b-edd735f17b9d/d?ref=blog.langchain.com) over the LangChain python docs. Answering these questions requires the system to synthesize answers from different documents in a logical way. You can review the [performance](https://smith.langchain.com/public/452ccafc-18e1-4314-885b-edd735f17b9d/d/compare?selectedSessions=5beb3728-2fb4-4091-b72e-277597284339%2C10e6ece8-a65b-45a4-ac38-9554a16daca4%2C7f0a7983-a6dc-49a1-892d-5b0fdc264bb4%2C10cda074-76f8-4e87-8c21-b6499cb6d83d%2Cb4908c09-f670-4737-bc59-abbd4245c9f6%2Cab3f6db1-3b73-49a1-8538-c4a9dff1b78c%2Ccebda59c-eda5-46dd-bd2b-9d1435bae132%2C1fd06cde-3cc2-4234-9a2a-cf1bdb3ee0ed%2C3490783c-06e2-4b3f-aeaf-da1bed128047%2C4bfcbd94-aefe-4e22-8567-a17788cd0c73&ref=blog.langchain.com) of common approaches in the linked page and try out the performance of your own application using the [langchain-benchmarks ](https://langchain-ai.github.io/langchain-benchmarks/notebooks/retrieval/langchain_docs_qa.html?ref=blog.langchain.com)package.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb0bbe51c6ccf7873ca71_image-13.png)

## Background

Over the past year, the tooling and model quality for building with LLMs has continued to improve with breakneck speed. Each week, dozens of new prompting and compositional techniques are proposed by developers and researchers, all claiming superior performance characteristics. The LangChain community has [implemented](https://github.com/kyrolabs/awesome-langchain?ref=blog.langchain.com) many of these, from simple prompting techniques like [chain of density](https://smith.langchain.com/hub/langchain-ai/chain-of-densit?ref=blog.langchain.com) and [step-back prompting](https://smith.langchain.com/hub/langchain-ai/stepback-answer?ref=blog.langchain.com), to [advanced RAG techniques](https://github.com/langchain-ai/langchain/tree/master/templates/neo4j-advanced-rag?ref=blog.langchain.com) all the way to [RL chains](https://github.com/langchain-ai/langchain/blob/master/cookbook/learned_prompt_optimization.ipynb?ref=blog.langchain.com), [generative agents](https://github.com/langchain-ai/langchain/blob/master/cookbook/generative_agents_interactive_simulacra_of_human_behavior.ipynb?ref=blog.langchain.com), and autonomous agents like [BabyAGI](https://github.com/langchain-ai/langchain/blob/master/cookbook/baby_agi.ipynb?ref=blog.langchain.com). For structured generation alone, we have (thankfully) evolved from [emotion prompting](https://arxiv.org/abs/2307.11760?ref=blog.langchain.com) techniques to fine-tuned APIs like [function calling](https://python.langchain.com/docs/modules/chains/how_to/openai_functions?ref=blog.langchain.com) and [grammar-based sampling](https://python.langchain.com/docs/integrations/llms/llamacpp?ref=blog.langchain.com#grammars).

With the launch of [Hub](https://smith.langchain.com/hub?ref=blog.langchain.com) and [LangChain Templates](https://blog.langchain.com/langserve-hub/), the release rate of new architectures continues to accelerate. But which of these approaches will translate to performance gains in YOUR application? What tradeoffs are assumed by each technique?

It can be hard to separate the signal from the noise, and the abundance of options makes reliable and relevant benchmarks that much more important. When it comes to grading language models on general tasks, public benchmarks like [HELM](https://crfm.stanford.edu/helm/latest/?ref=blog.langchain.com) or [EleutherAI’s Test Harness](https://www.eleuther.ai/projects/large-language-model-evaluation?ref=blog.langchain.com) are great options. For measuring LLM inference speed and throughput, AnyScale’s [LLMPerf benchmarks](https://www.anyscale.com/blog/reproducible-performance-metrics-for-llm-inference?ref=blog.langchain.com) can be a guiding light. These tools are excellent for comparing the underlying capability of language models, but they don't necessarily reflect their real-world behavior within your application.

LangChain’s mission is to make it as easy as possible to build with LLMs, and that means helping you stay up to date on the **relevant** advancements in the field. LangSmith’s evaluation and tracing experience helps you easily compare approaches in aggregate and on a sample level, and it makes it easy to drill down into each step to identify the root cause for changes in behavior.

With public datasets and [evals](https://www.langchain.com/resources/llm-evals), you can see the performance characteristics of any reference architecture on a relevant dataset so you can easily separate the signal from the noise.

## 📑 LangChain Docs Q&A Dataset

The first benchmark task we are including is a [Q&A dataset over LangChain's documentation](https://smith.langchain.com/public/452ccafc-18e1-4314-885b-edd735f17b9d/d?ref=blog.langchain.com). This is a set of hand-crafted question-answer pairs we wrote over [LangChain’s python docs](https://python.langchain.com/?ref=blog.langchain.com). The questions are written to test RAG systems' ability to answer correctly, even if an answer requires information from multiple documents or when the question conflicts with the document's knowledge.

As a part of the initial release, we have evaluated various implementations that differ across a few dimensions:

- The language model used (OpenAI, Anthropic, OSS models)
- The "cognitive architecture" used (conversational retrieval chain, agents)

You can check out the [link](https://smith.langchain.com/public/452ccafc-18e1-4314-885b-edd735f17b9d/d?ref=blog.langchain.com) above to review the results or continue with the information below!

## 🦜💪 LangChain Benchmarks

To help you experiment with your own architectures on the Q&A dataset, we are publishing a new [langchain-benchmarks](https://pypi.org/project/langchain-benchmarks/?ref=blog.langchain.com) package ([docs](https://langchain-ai.github.io/langchain-benchmarks/index.html?ref=blog.langchain.com) link). This package facilitates experimentation and benchmarking for key functionality when building with LLMs. In addition to the are publishing benchmarks [extraction](https://langchain-ai.github.io/langchain-benchmarks/notebooks/extraction/intro.html?ref=blog.langchain.com), [agent tool use,](https://langchain-ai.github.io/langchain-benchmarks/notebooks/tool_usage/intro.html?ref=blog.langchain.com) and [retrieval-based question answering.](https://langchain-ai.github.io/langchain-benchmarks/notebooks/retrieval/intro.html?ref=blog.langchain.com)

For each dataset, we provide functionality to easily test different LLMs, prompts, indexing techniques, and other tooling so you can quickly weigh the tradeoffs in different design decisions and pick the best solution for your application.

💡

Try it yourself using the [links](https://langchain-ai.github.io/langchain-benchmarks/index.html?ref=blog.langchain.com) above or open a feature request in the [LangChain Benchmarks](https://github.com/langchain-ai/langchain-benchmarks?ref=blog.langchain.com) repository to request new tasks.

In this post, we'll review some results from one of the question-answering tasks to show how it works!

### Comparing Simple RAG Approaches

In our initial benchmarks, we evaluated LLM architectures based on the following templates:

Cognitive ArchitectureTestScore ⬆️Cosine Dist ⬇️🔗Conversational Retrieval Chainzephyr-7b-beta a2f30.310.18[link](https://smith.langchain.com/public/452ccafc-18e1-4314-885b-edd735f17b9d/d/compare?selectedSessions=20f78340-a5a8-4193-92ba-eb6c0849ab3b&ref=blog.langchain.com)mistral-7b-instruct-4k 08260.460.13[link](https://smith.langchain.com/public/452ccafc-18e1-4314-885b-edd735f17b9d/d/compare?selectedSessions=80501c49-6845-4a1e-980d-8e36dddba230&ref=blog.langchain.com)gpt-4-chat f4cd0.500.15[link](https://smith.langchain.com/public/452ccafc-18e1-4314-885b-edd735f17b9d/d/compare?selectedSessions=cced8db6-5a08-4076-84b6-67282d718441&ref=blog.langchain.com)chat-gpt-3.5 10980.560.12[link](https://smith.langchain.com/public/452ccafc-18e1-4314-885b-edd735f17b9d/d/compare?selectedSessions=653f5f0c-b250-41bd-b235-ad7e460ef9ba&ref=blog.langchain.com)anthropic-chat f2900.560.13[link](https://smith.langchain.com/public/452ccafc-18e1-4314-885b-edd735f17b9d/d/compare?selectedSessions=d21fe3ec-719c-44bf-a6dd-c0f6bc414e9c&ref=blog.langchain.com)Agentopenai-functions-agent dc910.470.13[link](https://smith.langchain.com/public/452ccafc-18e1-4314-885b-edd735f17b9d/d/compare?selectedSessions=20b3ae59-9eee-43f0-9776-1c1f41b15aa2&ref=blog.langchain.com)gpt-4-preview-openai-functions-agent 58320.580.142[link](https://smith.langchain.com/public/452ccafc-18e1-4314-885b-edd735f17b9d/d/compare?selectedSessions=544a8e44-49fc-4fcb-a976-713ec0d2e9b2&ref=blog.langchain.com)anthropic-iterative-search 1fdf0.500.14[link](https://smith.langchain.com/public/452ccafc-18e1-4314-885b-edd735f17b9d/d/compare?selectedSessions=b01cedc1-e2e4-456c-a442-bd1b27cc4788&ref=blog.langchain.com)Assistantopenai-assistant af8e0.620.13[link](https://smith.langchain.com/public/452ccafc-18e1-4314-885b-edd735f17b9d/d/compare?selectedSessions=9ea0c6d3-31dd-4943-a96d-0d9ee320daae&ref=blog.langchain.com)

The links above let you view the results for each configuration and compare each using the automatic metrics. For these tests, we measure the [cosine distance](https://python.langchain.com/docs/guides/evaluation/string/embedding_distance?ref=blog.langchain.com) between the predicted and reference responses as well as an accuracy "score" using LangChain’s LLM-based [scoring evaluator](https://python.langchain.com/docs/guides/evaluation/string/scoring_eval_chain?ref=blog.langchain.com). For the accuracy score, a larger number is better (⬆️) and for the cosine distance, a *lower* number is better (⬇️). Below, we describe the tests in more detail. See the prompt used for the evaluator [here](https://github.com/langchain-ai/langchain-benchmarks/blob/5f2ce54b4025006d12755e1cc112627ae539e81f/langchain-docs-benchmarking/run_evals.py?ref=blog.langchain.com#L58).

**Conversational retrieval chains**

The following experiments use different models within a simple retrieval chain implementation. The input query is directly embedded using OpenAI's `text-embedding-ada-002`, and the four most relevant docs are retrieved from a ChromaDB vectorstore based on semantic similarity. We compare the following LLMs below:

- `mistral-7b-instruct-4k 0826`: applies open-source- [Mistral 7B model](https://app.fireworks.ai/models/fireworks/mistral-7b-instruct-4k?ref=blog.langchain.com)(with a 4k context-window) to respond using retrieved docs. This model was adapted using instruction tuning.
- `zephyr-7b-beta a2f3`: applies the open-source- [Zephyr 7B Beta](https://huggingface.co/HuggingFaceH4/zephyr-7b-beta?ref=blog.langchain.com)model, which is instruction-tuned version of Mistral 7B, to respond using retrieved docs.
- `chat-3.5-3.5 1098`: uses- `gpt-3.5-turbo-16k`from OpenAI to respond using retrieved docs.
- `gpt-4-chat f4cd`: uses- `gpt-4`by OpenAI to respond based on retrieved docs.
- `anthropic-chat f290`: uses- `claude-2`by Anthropic to respond based on retrieved docs.

💡

All of the above runs use the same retriever, meaning that any differences in results are due to the LLM's ability to reason over the retrieved data

**Agents**

The following tests apply `agent` architectures to answer the questions. The agents are given a single retriever tool, which wraps the same vector store retriever described above. Agents are able to respond directly or call the retriever any number of times with their own queries to answer a question. In practice, we find that the agents typically call the tool once and then respond.

- `openai-functions-agent dc91`: uses the- [function calling API](https://python.langchain.com/docs/modules/agents/agent_types/openai_functions_agent?ref=blog.langchain.com)from OpenAI (now called the 'tool calling' API) to interact with the documentation retriever. In this case, the agent is driven by the- `gpt-3.5-turbo-16k`model.
- `gpt-4-preview-openai-functions-agent 5832`: same as above but uses the new- `gpt-4-1106-preview`model, which is a larger, more capable model than gpt-3.5.
- `anthropic-iterative-searche 1fdf`: applies the- [iterative search](https://python.langchain.com/docs/templates/anthropic-iterative-search?ref=blog.langchain.com)agent, which prompts Anthropic's- `claude-2`model to call the retrieval tool and uses XML formatting to improve reliability of the structured text generation.

💡

Compared to the **conversational retrieval chain**, the above results vary in their **retrieval** methods. Namely, they use the LLM to generate relevant search queries.

**Assistant API**

Finally, we tested OpenAI's new assistants API in `openai-assistant af83`. This still uses our same retrieval tool, but it uses OpenAI's execution logic to decide the query and final response. This agent ended up earning the highest performance of all our tests.

## Reviewing the Results

The comparison views also make it easy to manually review the outputs to get a better sense for how the models behave, so you can make adjustments to your cognitive architecture and update the evaluation techniques to address any failure modes you identify.

To illustrate, let's compare the conversational retrieval chain powered by Mistral-7b RAG application to similarly architected application powered by GPT-3.5: ([comparison link)](https://smith.langchain.com/public/452ccafc-18e1-4314-885b-edd735f17b9d/d/compare?selectedSessions=80501c49-6845-4a1e-980d-8e36dddba230%2C653f5f0c-b250-41bd-b235-ad7e460ef9ba&ref=blog.langchain.com).  Using the tested prompts, GPT-3.5's performance handily outperforms the Mistral 7B model in terms of the aggregate metrics generated for this example (0.01 difference in average cosine difference but lags the average "accuracy" score by 0.1).

*Note: None of the open-source models tested in these experiments matched the aggregate performance of the proprietary APIs off-the-shelf, though additional prompt engineering may close the gap.*

This is interesting, but in order to decide how to improve, you'll need to look at the data. LangSmith makes this easy. Take the following challenging example:

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb0bbe51c6ccf7873ca6e_image-16.png)

For this data point, neither model was able to answer correctly; the question itself requires knowledge of absence, which is a challenging task for RAG applications that often leads to hallucinations.

When inspecting this by eye, the `gpt-3.5-turbo` model clearly hallucinates, even providing a nice made-up link ([https://docs.langchain.com/java-sdk](https://reference.langchain.com/java)). The  `mistral` models' response is preferable, since it doesn't generate inaccuracies (no official LangChain java SDK exists).

To diagnose why the models responded the way they did, you can click through to view the full trace of that architecture.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb0bce51c6ccf7873ca84_image-17.png)

It's clear from the trace ([link](https://smith.langchain.com/public/452ccafc-18e1-4314-885b-edd735f17b9d/d/80501c49-6845-4a1e-980d-8e36dddba230/p/r/1abd725d-d2ce-45b7-9476-54e46e08da31?ref=blog.langchain.com)) that the retrieved documents are all quite irrelevant to the original query.  If you are using a model like `gpt-3.5` and getting hallucinations like this, you can try adding an additional system prompt reminding the model to only respond based on the retrieved content, and you can work to improve the retriever to filter out irrelevant documents.

Let's review another data point, this one where `gpt-3.5` responded correctly but `mistral` did not. If you [compare the outputs](https://smith.langchain.com/public/452ccafc-18e1-4314-885b-edd735f17b9d/d/compare?selectedSessions=80501c49-6845-4a1e-980d-8e36dddba230%2C653f5f0c-b250-41bd-b235-ad7e460ef9ba&peek=fa9f8beb-0cb3-4d67-8ed7-cab5dae0d615&ref=blog.langchain.com), you can see that `mistral` was influenced too much by the document content and mentioned the class from the docs rather than the direct answer.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb0bce51c6ccf7873ca81_image-18.png)

If you look at the [trace](https://smith.langchain.com/public/452ccafc-18e1-4314-885b-edd735f17b9d/d/80501c49-6845-4a1e-980d-8e36dddba230/p/r/965f74aa-6c87-490c-98aa-158db8358fe9?ref=blog.langchain.com), you can see that "SelfQueryRetriever" is only mentioned in Document 5 of the retrieved docs, meaning it's the least relevant document. That the LLM hinges its response based on this document signals that perhaps we could improve its performance by re-ordering the input.

To check this hypothesis, you can [open the LLM run in the playground](https://smith.langchain.com/public/452ccafc-18e1-4314-885b-edd735f17b9d/d/80501c49-6845-4a1e-980d-8e36dddba230/p/r/965f74aa-6c87-490c-98aa-158db8358fe9/playground?ref=blog.langchain.com). By swapping documents 1 and 5, we can see that the LLM responds with the correct answer. Based on this check, we could update the order we present the documents and re-run evaluation!

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb0bbe51c6ccf7873ca7b_image-19.png)

Apart from response accuracy, latency is another important metric when building an LLM application. In our case, `mistral-7b`'s median response time was 18 seconds, 11 seconds faster than `gpt-3.5`'s.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb0bbe51c6ccf7873ca74_image-20.png)

Measuring quality metrics alongside "system metrics" can help you pick the "right-sized" model and architecture for the job.

Finally, let's compare the `openai-assistant af83` with the similar `gpt-4-preview-openai-functions-agent 5832` test. They use the same underlying model and retriever tool and work as an agent, but the former test uses OpenAI's assistant API. You can view the comparison here: [link](https://smith.langchain.com/public/452ccafc-18e1-4314-885b-edd735f17b9d/d/compare?selectedSessions=544a8e44-49fc-4fcb-a976-713ec0d2e9b2%2C9ea0c6d3-31dd-4943-a96d-0d9ee320daae&ref=blog.langchain.com).  

An example data point where the assistant out-performs the agent is this ([example](https://smith.langchain.com/public/452ccafc-18e1-4314-885b-edd735f17b9d/d/compare?selectedSessions=544a8e44-49fc-4fcb-a976-713ec0d2e9b2%2C9ea0c6d3-31dd-4943-a96d-0d9ee320daae&peek=429e58f2-6e9d-4aa6-a8b1-b67b7531bea5&ref=blog.langchain.com)). Both say that they cannot see an explicit answer to the question (since the retriever is the same), but the assistant is willing to provide context on how `strict` is used in other contexts as a pointer for the user.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb0bbe51c6ccf7873ca7e_image-21.png)

## More to come

Over the coming weeks, we plan to add benchmarks for each of LangChain’s most popular [use cases](https://python.langchain.com/docs/use_cases?ref=blog.langchain.com) to make it easier. Check in on the [LangChain](https://github.com/langchain-ai/langchain-benchmarks?ref=blog.langchain.com) benchmarks repository for updates and open a feature request to ensure that your use cases are covered.

You can also download the [langchain-benchmarks package](https://langchain-ai.github.io/langchain-benchmarks/index.html?ref=blog.langchain.com) to try out **your** RAG application on this and other tasks.
