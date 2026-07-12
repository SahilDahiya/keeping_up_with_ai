---
title: Open Deep Research
topic: agents
subtopic: tool-use
secondary_topics:
- rag-retrieval/search
summary: Describes an open deep research system combining retrieval, planning, and
  tool use.
source: together
url: https://www.together.ai/blog/open-deep-research
author: Together AI
published: '2025-04-16'
fetched: '2026-07-11T04:24:58Z'
classifier: codex
taxonomy_rev: 1
words: 3026
content_sha256: 7183c2f8970ba6d014e8d7e1a9a08e08df50bf54833738d3f404d4b822998227
triage: keep
skip_reason: null
---

# Open Deep Research

**TL;DR**: Deep Research is an emerging AI workflow that enhances web search by producing comprehensive, well-cited content on complex topics. We present Together AI’s Open Deep Research, an LLM workflow that can answer complex questions that require multi-hop reasoning and generate research reports. It features a flexible architecture designed to educate developers and be extended by the community, focusing specifically on providing an in-depth understanding of specific topics rather than just short answers to complex questions. We release our [dataset](https://huggingface.co/datasets/togethercomputer/together-search-bench), [code](https://github.com/togethercomputer/open_deep_research) and share learnings here.

## Introduction

Finding, organizing, and presenting salient information is critical in our daily lives. This is why much of AI developments focus on search. Recently, OpenAI has released their Deep Research (OpenAI, 2025), a powerful workflow that goes beyond simple search: the goal is to produce long-form content that provides in-depth explanations about a topic or a user question. Deep Research navigates the web in depth and uses reasoning to ensure it gathers the right information to answer users’ questions effectively.

Why is this important now? The emergence of Deep Research like applications represent a fundamental shift in how we interact with information. Traditional search has long been limited to a query-to-documents model, where users input keywords and receive a list of potentially relevant sources that they must read, synthesize, and extract insights from manually. Deep Research transforms this model by enabling users to pose complex, multi-faceted questions and receive comprehensive, synthesized reports in return. This agentic approach—where the system autonomously conducts multiple searches, evaluates information quality, identifies knowledge gaps, and synthesizes findings into coherent reports—pushes the frontier of what's possible in information retrieval and analysis. It enables intellectual work higher up the reasoning stack that was previously only possible for human researchers and analysts.

Since OpenAI’s release, there have been remarkable efforts from the open-source community to develop Deep Research alternatives (LangChain-AI, 2025; Huggingface, 2025). While several implementations already exist, we believe there's significant value in providing an accessible [open-source Deep Research toolkit](https://github.com/togethercomputer/open_deep_research) the community can build on. Our implementation aims to improve upon current approaches and, crucially, to share practical insights into what works and what doesn't when building such complex AI workflows from scratch.

Our workflow tries to mimic what humans do when they need to go through a research process. Think about your experience when addressing complex questions or comparing options—such as evaluating investment opportunities or staying informed about recent research. These tasks typically require dozens of hours of dedicated research work. A simple online web search will not give you all the necessary information. Deep Research is designed to help you make smarter decisions by presenting more comprehensive information and always citing its sources. Similar to what an analyst would do, Deep Research starts with a plan, searches for information, evaluates the information it has found, and iterates until convergence.

Together AI’s Open Deep Research is an LLM agent workflow that can answer complex multi-hop questions and simultaneously write long-form research reports to provide value to users. Our workflow integrates models from the TogetherAI cloud platform, with each component—text, image, and audio generation—powered by the most suitable model available through TogetherAI's cloud infrastructure.

Our focus in this blog post is to cover the general architecture and methodology. We first explain the design principles of our Deep Research, we then introduce our technical stack, and finally, we go into our evaluations.

Regarding evaluations, benchmarks are often difficult to interpret, and identifying baselines is even more challenging. There are also challenges concerning training costs, error propagation and hallucinations, and bias and fairness.  Our goal is to design a Deep Research by offering a flexible architecture that can be easily extended, and we believe this workflow can serve as a foundation for the community to expand and experiment with. This effort extends [our recent cookbook release](https://github.com/togethercomputer/together-cookbook/blob/main/Agents/Together_Open_Deep_Research_CookBook.ipynb), detailing the additional efforts we invested and the broader challenges we encountered along the way. 

## Building a Deep Research Workflow

![](https://cdn.prod.website-files.com/69654e88dce9154b5f12070c/699e0b169c48c6bbda61e006_67ffdfdcc14446d60a2a9d0e_AD_4nXedElgrxG9r72Qx0ASenFOwpU2sg7AqWXy_tReaAVpxwBM_NtjasugR0jQEkACRBulSdUztfUVACbGsEsQkyh9ESADAsPdu1QQzfRQEDyMK3ph9WUorZNwYLfFMFWS7CYIfVOlg.png)

There are a few different dimensions to building good and useful search workflows:

- Information collection: how to thoroughly research a topic and find the answer a user is looking for.

- Communication: while being comprehensive is valuable, we need to present it in a way that users can easily understand and utilize.

- Inference and costs: we use [Together APIs](https://docs.together.ai/docs/quickstart)for highly efficient LLM inference and caching mechanisms to save costs for repetitive search queries.

### Plan, Search, Self-Reflect, and Write

Gathering the *right* information is a multi-step process. For example, answering "What are the five largest companies in the green/renewable energy sector by market capitalization, and what are their current stock prices?" requires a two-step process:

- first, identifying the five largest companies in the sector,
- and second, retrieving the current stock price for each company.

We structure our Deep Research following a similar methodology. The initial planning component focuses on generating an initial plan: a set of important search queries. After collecting results from these queries through a search engine, we ask an LLM to evaluate whether any knowledge gaps remain unfilled by the current sources. This approach draws inspiration from Self-Reflection techniques that have contributed to the success of many AI Agents (Shinn et al., 2023).

An additional struggle we had to overcome was dealing with long content: assume we retrieve 10 sources and send them all to the final writing step of the pipeline. If the raw content of these sources is too long, it will occupy the entire context window, preventing us from generating an answer. We approach this problem in two ways:

- We use an LLM to summarize the raw content of the sources to keep only important information. This summarization comes with several limitations (e.g., the summarizer might extract a citation that has to be interpreted in context), but it has been useful to condense the long source content in our pipeline.
- Before writing the research report, we use a language model to rank all sources according to their relevance and cite the high-quality information sources; this is similar to a classical language model/classifier used as re-ranker, with the difference and possible limitations that come from the fact that it produces the rank in a single step.

### Communication

The design of the final report is also important to effectively convey information and our findings. We enhance our Deep Research outputs using several visualizations and formatting techniques. We provide multi-modal capabilities through [Mermaid](https://github.com/mermaid-js/mermaid) JS charts that display relationships and flows visually. We also generate custom cover images using [Black Forest Labs](https://blackforestlabs.ai/)’s FLUX models, available on Together’s AI platform. Additionally, we also generate a podcast that explains the content of the report in an engaging manner.

Combining HTML rendering with Mermaid JS charts has proven to be a successful strategy. Even though language models cannot provide structured image outputs directly, it becomes straightforward to ask LLMs to generate content in JavaScript that can then be rendered and manipulated with external libraries. The high quality of the JS charts that LLMs can generate is surprising, as shown in Figure 2.

![](https://cdn.prod.website-files.com/69654e88dce9154b5f12070c/699e0b169c48c6bbda61e00f_67ffc25035bd3d5ea88c9b0b_image%2520(6).png)

**(Disclaimer: This visualization is for demonstration purposes ONLY. We strongly encourage users to refer to the source citations and perform rigorous fact-checking before using them.)**

The podcast is created after Deep Research has prepared the research report. We use the answer to generate an audio podcast that analyzes and explains the topic researched in a few minutes. To generate the podcast, we use the [Cartesia](https://cartesia.ai/) AI Sonic models hosted by [Together AI](https://www.together.ai/models/cartesia-sonic).

### Inference and Search Costs

When selecting LLM models for the workflow, quality, latency, and cost are the three main elements taken into consideration: while DeepSeek-R1 is one of the best models out there, its responses are lengthy, more expensive, and time-consuming.

In our workflow we extend our Together AI’s mixture-of-agents (MoA) approach (Wang et al., 2025) focusing on assigning different LLMs to four different roles:

- A planner: a model with strong planning and reasoning capabilities (we use Qwen/Qwen2.5-72B-Instruct-Turbo).
- A summarizer is a long-context and efficient model that summarizes long content from web pages (we use meta-llama/Llama-3.3-70B-Instruct-Turbo).
- A JSON extractor: a model tasked with extracting information from a previous model’s response and returning JSON, to improve the workflow robustness (we use meta-llama/Meta-Llama-3.1-70B-Instruct-Turbo)
- A report writer: a strong model that can aggregate information from sources and write a high-quality research report (we use together_ai/deepseek-ai/DeepSeek-V3).

The large availability of models in TogetherAI's cloud—spanning text, image, and audio generation—allows us to select the most suitable model for each task, balancing quality with cost-efficiency while allowing us to provide optimized configurations available in our open-source codebase.

Caching is another important component in our design. During our experiments, we realized that running web search can be very expensive when using a multi-step process and more than a few hundred test questions. We implemented a caching mechanism that allows us to temporarily store retrieved sources so that we can re-run experiments with different configurations without having to re-run every query. Note that caching is a double-edged sword; caching without time to live (TTL) support prevents us from getting new and fresh information when needed. While this is fine for evaluation or benchmark purposes, it might be worth adopting enterprise-level solutions in a production environment.

## Technical Stack

As previously mentioned, for our implementation, we use models available on the Together AI platform for highly efficient and cost-effective LLM inference as well as AI-powered image and audio generation. We settled on [Tavily](https://tavily.com/) to retrieve relevant information from the web. A nice feature in Tavily is that it allows us to get the raw content of the web page with one single call, without having to search and then scrape a website in two separate steps, allowing us to provide a more scalable experience.

Getting a reply from our Deep Research usually takes 2 to 5 minutes (without the podcast generation), depending on the number of evaluation/reflection loops the model can do. Moreover, as mentioned above, the models we use in the pipeline play a big role in this: using DeepSeek-V3 as a writer can significantly increase the response time and cost, but it also increases the quality of the output.

## Open Deep Research Evaluation

#### Quantitative Benchmarks

Evaluating long-form context is still a challenging task, we focus on popular benchmarks to understand the capabilities of our Deep Research. There are three main dimensions that we are interested in considering when evaluating a Deep Research tool.

- Factuality: We want to be sure that the content generated is factual. This task becomes more complex as the output from the model gets longer.
- Search Capabilities: DeepResearch should be able to do multi-hop search and aggregate information over different steps.
- Output quality: It is important to understand the overall quality of the output and the clarity of the document. We will show some qualitative examples of outputs.

We perform different rounds of evaluation to ensure that the answers we provide are factual. We use a sample of three quantitative benchmarks: FRAMES (Krishna et al., 2024), SimpleQA (Wei et al., 2024), and HotPotQA (Yang et al., 2018).

FRAMES is a multi-hop benchmark designed to test complex reasoning requiring integrating information across multiple passages (e.g., “If my future wife has the same first name as the 15th first lady of the United States' mother and her surname is the same as the second assassinated president's mother's maiden name, what is my future wife's name?”)

SimpleQA provides specific questions to assess factuality ("When did X happen?"), instead HotPotQA is another benchmark for multi-hop reasoning (e.g., "The painter who depicted the Arnolfini Portrait was born in which modern-day country?"). The latter is thus useful for evaluating systems that can perform multiple searches to answer a question. We build a dataset by sampling 50 examples from each of the three (150 in total). When prompting the models, we add a suffix asking for a short reply since these benchmarks usually focus on short replies.

We compared our Deep Research against several baselines. First, we evaluate against base models without search tools to establish a performance floor.  Second, we conduct a comparison with [SmolAgents](https://github.com/huggingface/smolagents) (SearchCodeAgent), an intuitive and flexible agent framework from HuggingFace, as well as the well-crafted LangChain implementation [open_deep_research](https://github.com/langchain-ai/open_deep_research) (LDR). We acknowledge the imperfect nature of this comparison, but we still believe it provides valuable performance insights; we are not sharing this comparison to demonstrate that our tool is the best, but to give a sense of the general level of performance of this kind of approach. Further optimizations could be used to improve any baseline.

To evaluate, we use an LLM-as-a-judge strategy. The reason behind this choice is due to the lengthy outputs generated by Deep Research, which makes them hard to evaluate.

According to the results in Figure 3, our Deep Research consistently improves the answer quality over the base models by a significant margin, which holds across Llama, DeepSeek, and Qwen flagship models, demonstrating the quality of our workflow.

![](https://cdn.prod.website-files.com/69654e88dce9154b5f12070c/699e0b169c48c6bbda61e012_67ffc34372429b3972c1bb56_AD_4nXcpI6CjkUHb8ucNHnD_Aoarg4UJCXJef_ExDqLeDAT4OOp1Zze8AVpqvHbCS0lNiGTd8jACnYBvXjdu83SWiGnavhN3lQjA9od47PRU5_Zmq5jHFX9SGDb55vsxtx8y9ABi3hiw.png)

#### The Importance of Multi-Step Search

We evaluate the usefulness of multi-step search by constraining our Deep Research to only one step (essentially turning it into a simple one-time retrieval augmented generation - RAG). According to Figure 4, the multi-step search improves the benchmark accuracy across the model classes, indicating the necessity for multi-step web-search and result refinement for this benchmark. This result was expected since some of the questions in the benchmark require multi-hop exploration.

![](https://cdn.prod.website-files.com/69654e88dce9154b5f12070c/699e0b169c48c6bbda61e015_67ffc36e78ad6a7ea9bd182e_AD_4nXcr_kBfgNZmiXusO-MG_xRni7ClFo0Yqi0oFPvw0ERgRWHw1z6joztABWCwDXVJOAAwRVIfcvOqloflrj0XEVe-ZGEkYmxCoIw9CHIRzHso7Fbj_3ABFeCz1PBDYD2bDZq1HCLx4w.png)

#### Together Deep Research Reports

Below, we present several example reports generated by our Deep Research Tool, which shows the promises of complex knowledge mining and synthesis.

![Manufacturing facility with robotic arms and workers amid sparks, illustrating AI impact in industry.](https://cdn.prod.website-files.com/69654e88dce9154b5f12070c/699e0b169c48c6bbda61e018_67ffdef64e467e0f96eb429f_Screenshot%25202025-04-16%2520at%25208.31.13%25E2%2580%25AFAM.png)

## Limitations

Any new technology comes with its challenges and limitations, and its impact can manifest throughout society. Developers need to think deeply about the expected impact of these types of limitations in their pipeline, even more so when the expected accuracy from this kind of product is very high. We describe some of the possible issues that we have encountered and identified:

#### Error Propagation and Hallucinations

Our multi-step research process is vulnerable to error propagation. Initial misinterpretations can cascade through subsequent search iterations, amplifying inaccuracies. Language models may also generate plausible but incorrect information, especially with source data from conflicting sources. These issues are inherent challenges in complex AI research systems that combine multiple inference steps.

### Representation Bias

Foundation models (LLMs and text-to-image models), like many AI systems, may inherit biases present in the training data and search indices it utilizes. These biases can manifest in various ways, including underrepresentation of minority perspectives, amplification of stereotypes, and uneven quality of results across different demographic groups. There is always the need for a better understanding of how these technologies can impact the field.

### Search Bias and Freshness

The quality and diversity of search results depend heavily on the underlying search indices and ranking algorithms. Certain topics require more comprehensive and up-to-date coverage than others, which can lead to information gaps and potential reinforcement of existing knowledge inequalities. For example, asking for information about a live event will give correct results only if pages are scraped in real time and not indexed every few hours. Additionally, recency bias can occur where newer content is prioritized over potentially more accurate or comprehensive older resources.

—

We hope our open-source release can help the community better understand Deep Research systems and contribute to community efforts to improve the tooling and mitigate the aforementioned limitations.

### Acknowledgements

We thank [Tavily AI](https://tavily.com/) for enabling scalable web search and retrieval, [Cartesia](https://cartesia.ai/) for their high-quality Sonic voice models used in podcast generation, and [Black Forest Labs](https://blackforestlabs.ai/) for their Flux model, which powers our image-generation capabilities. Their tools were instrumental in building Together Open Deep Research’s multi-modal outputs. We also extend gratitude to the open-source community and model providers whose work underpins this project, including Meta Llama Team, DeepSeek Team, and Alibaba Qwen Team—their models form the core of our workflow.

**Research Leads**: Federico Bianchi, Zhichao Li, Shang Zhu

**Core Contributors**: Roy Yuan, Zain Hasan, Hassan El Mghari

**Leadership**: James Zou, Albert Meixner, Ben Athiwaratkun

### More Details on Evaluations

SmolAgent’s (Search)CodeAgent is an agent that generates code actions, so it is, in general, more flexible. However, since we are giving it access to a portion of the web page and we do not allow it to use a Browser Tool, it might struggle reading long content. We give this agent access to a Tavily search tool. In this sense, this agent we use is similar to the one described in the original HF [blog post](https://huggingface.co/blog/smolagents). We expect CodeAgent to have higher performances when using a Browser Tool.

LangChain’s open_deep_research is based on LangGraph for workflow orchestration: a planner that constructs a section-by-section research plan, and each section is created by searching and writing in parallel. Note that in our evaluation, we realized that the research planner needs a more specific prompt, so we slightly modified the instructions of the input prompt. More details on the entire evaluation can be found in our [codebase](https://github.com/togethercomputer/open_deep_research).

### References

OpenAI (2025). Introducing deep research. [https://openai.com/index/introducing-deep-research/](https://openai.com/index/introducing-deep-research/)

LangChain-AI (2025). [https://github.com/huggingface/smolagents/tree/main/examples/open_deep_research](https://github.com/huggingface/smolagents/tree/main/examples/open_deep_research)

Huggingface (2025). Open-source DeepResearch – Freeing our search agents. Blog Post. [https://huggingface.co/blog/open-deep-research](https://huggingface.co/blog/open-deep-research)

Wang, J., Jue, Wang, Athiwaratkun, B., Zhang, C., & Zou, J. (2025). Mixture-of-agents enhances large language model capabilities. In *The Thirteenth International Conference on Learning Representations*.

Shinn, N., Cassano, F., Gopinath, A., Narasimhan, K., & Yao, S. (2023). Reflexion: Language agents with verbal reinforcement learning. *Advances in Neural Information Processing Systems*, *36*, 8634-8652.

Krishna, S., Krishna, K., Mohananey, A., Schwarcz, S., Stambler, A., Upadhyay, S., & Faruqui, M. (2024). *Fact, Fetch, and Reason: A Unified Evaluation of Retrieval‑Augmented Generation*. arXiv preprint arXiv:2409.12941.

 Wei, J., Karina, N., Chung, H. W., Jiao, Y. J., Papay, S., Glaese, A., Schulman, J., & Fedus, W. (2024). *Measuring short‑form factuality in large language models*. arXiv preprint arXiv:2411.04368.

Yang, Z., Qi, P., Zhang, S., Bengio, Y., Cohen, W. W., Salakhutdinov, R., & Manning, C. D. (2018). *HotpotQA: A Dataset for Diverse, Explainable Multi‑hop Question Answering*. In *Proceedings of the 2018 Conference on Empirical Methods in Natural Language Processing* (pp. 2369–2380).
