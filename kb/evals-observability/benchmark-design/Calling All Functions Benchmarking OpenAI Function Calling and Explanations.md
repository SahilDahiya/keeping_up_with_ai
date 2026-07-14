---
title: 'Calling All Functions: Benchmarking OpenAI Function Calling and Explanations'
topic: evals-observability
subtopic: benchmark-design
secondary_topics:
- agents/tool-use
summary: Benchmarks OpenAI function calling and explanation quality, using evaluations
  to understand third-party LLM tool behavior.
source: arize
url: https://arize.com/blog/calling-all-functions-benchmarking-openai-function-calling-and-explanations/
author: Amber Roberts
published: '2023-12-07'
fetched: '2026-07-11T04:48:04Z'
classifier: codex
taxonomy_rev: 1
words: 2131
content_sha256: dba5cd957cec67d7a2deed406b96e65bff3242c3ef12a7218917345ac7aa8b3c
---

# Calling All Functions: Benchmarking OpenAI Function Calling and Explanations

*This piece is co-authored by  Roger Yang, Software Engineer at Arize AI*

Observability in third-party large language models (LLMs) is largely approached with benchmarking and evaluations since models like Anthropic’s Claude, OpenAI’s GPT models, and Google’s PaLM 2 are proprietary. In this blog post, we benchmark OpenAI’s GPT models with function calling and explanations against various performance metrics. We are specifically interested in how the GPT models and OpenAI features perform on correctly classifying hallucinated and relevant responses. The results below show the trade-offs between speed and performance for different LLM application systems, as well as a discussion on how these results with explanations can be used for data labeling, LLM assisted evaluation, and quality checks. The experimental framework we used is provided below so that practitioners can iterate and improve on the default classification template.

## OpenAI Function Calling and Explanations

With OpenAI function calling you are able to describe functions to various GPT models, which can then be used to output a JSON object containing arguments to call those functions. Function calling is essentially acting as a tool or agent for recording a response in a given format in order to reliably connect OpenAI GPT model capabilities with external tools and APIs. In regards to explanations, since it can be hard to understand in many cases why an LLM responds in a specific way, these are designed to prompt the LLM to justify whether or not an output is correct. The explanation feature of Arize [Phoenix](https://github.com/Arize-ai/phoenix) allows you to get an output label (‘relevant’ or ‘irrelevant’) and an explanation from the LLM at the same time. This, along with Phoenix’s ability to trace the documents retrieved for generating the output response, are both incredibly useful tools for debugging LLM responses. Below is an example of a ‘relevant’ evaluation with an explanation.

![eval with explanation example](https://arize.com/wp-content/uploads/2023/12/eval-with-explanation.png)


In the *Results and Tradeoffs* section below, comparison tables are provided for two use cases: predicting relevance and predicting hallucinations (these are Table 1 and Table 2, respectively). Each table compares the performance of GPT-4-turbo, GPT-4, GPT-3.5 and GPT-3.5-turbo across a variety of classification metrics (accuracy, precision, recall and F1 score) under specific prompt instructions and LLM attributes.

The four foundational models tested are evaluated with those metrics (in addition to median processing time) in the cases:

- Without_function_calling & without_explanations
- With_function_calling & without_explanations
- With_function_calling & with_explanations
- Without_function_calling & with_explanations

The prompt template in the LLMs is therefore unchanged (i.e the ordinary prompt completion) for examples **without_function_calling & without_explanations**. Samples **with_function_calling  & without_explanations** ask the LLM to put its answer in a JSON object that only accepts enum as input and samples **with_function_calling  & with_explanations** ask the LLM to provide explanation alongside its answer in the same JSON object (see [Google colab notebook](https://colab.research.google.com/github/Arize-ai/phoenix/blob/benchmarking-function-calling-and-explanations/tutorials/internal/benchmarking_function_calling_and_explanations.ipynb)).

## Benchmarked Dataset and Evaluation Metrics

Correctly identifying hallucinations and relevant responses in LLM outputs are two of the largest pain points for our customers who are currently implementing LLM applications. Optimizing LLM evaluation systems for hallucinations means correctly identifying all hallucinated responses, while keeping track of factual outputs. For use cases that leverage search and recommendation as part of their user experience, the most important factors related to user satisfaction are speed and relevance of results. In order to evaluate the performance of a LLM system for relevant and irrelevant outputs you should be aware of key metrics:

- [Precision and recall](https://arize.com/blog-course/precision-vs-recall/): How relevant is the information retrieved?
- Accuracy: How contextually accurate are the responses?
- Latency: How long does the system take to provide the response?
- User Feedback: How have the relevance and response time for the result impacted the user’s experience?

While we won’t go over using search and retrieval techniques like [retrieval augmented generation (RAG)](https://arize.com/blog-course/introduction-to-retrieval-augmented-generation/) and the Phoenix [LLM evals library](https://docs.arize.com/phoenix/llm-evals/running-pre-tested-evals) in this piece, you can check out [Arize AI’s latest blog posts](https://arize.com/blog-course/llm-evaluation-the-definitive-guide/) for optimizing relevance within your LLM system.

To benchmark these LLM systems we used datasets of queries and retrieved documents with ground-truth labels. Currently supported datasets from Arize Phoenix include:

- Binary hallucination classification: “[halueval_qa_data](https://github.com/RUCAIBox/HaluEval)” from the[HaluEval](https://arxiv.org/abs/2305.11747)benchmark
- Binary relevance classification: “wiki_qa-train”
- Additional [benchmarked datasets](https://docs.arize.com/phoenix/llm-evals/running-pre-tested-evals)for additional LLM use cases

## Results and Trade-Offs

![Table 1: Benchmarking LLM systems for Irrelevant and Relevant Predictions](https://arize.com/wp-content/uploads/2023/12/irrelevant-relevant-openai-function-calling-leaderboard.png)

*Table 1: Benchmarking LLM systems for Irrelevant and Relevant Predictions*

![Table 2: Benchmarking LLM systems for Hallucination and Factual Predictions](https://arize.com/wp-content/uploads/2023/12/benchmarking-openai-llms-gpt-4-hallucinations-large.png)

*Table 2: Benchmarking LLM systems for Hallucination and Factual Predictions*

Before going into the analysis of the results, you are able to reproduce these results for yourself in this [Google colab notebook](https://colab.research.google.com/github/Arize-ai/phoenix/blob/benchmarking-function-calling-and-explanations/tutorials/internal/benchmarking_function_calling_and_explanations.ipynb). Note that ordinarily you wouldn’t be able to recreate the numbers in these tables exactly, because of the non-deterministic nature of LLMs, but for this notebook we have added a seed to the sampling so it’ll be the same every time. Also, stratified sampling has been added so the binary categories are exactly 50/50. **Be aware that there is a computational cost associated with running this notebook with your OpenAI API keys. **The default number of samples has been set to 2, but you can change the number to 100 if you wish to replicate the results from this blog post.

### Processing Time

For clarity, these comparisons (using 100 samples) were run on Google Colab with a standard OpenAI API account and key. So while the latency values are unlikely to be exact when run on a different setup, the slowest and fastest models will be reproduced.

Additionally, using explanations in your evaluations is likely to take anywhere from 3 – 20x longer to compile (this is independent of function calling).

For model predictive ability on relevance overall:

- latency: GPT-3.5-instruct > GPT-3.5-turbo > GPT-4-turbo > GPT-4

For model predictive ability on hallucinations:

- latency: GPT-3.5-instruct > GPT-3.5-turbo ~ GPT-4-turbo > GPT-4

GPT models with function calling tend to have a slightly higher latency than LLMs without function calling, but take this with a grain of salt because there are a few caveats:

- The latency is extracted from HTTP headers returned to us by OpenAI, so depending on your account and your method of making these requests, the latency values can shift since they were calculated by OpenAI internally.
- Function calling trade-offs depend on your use case. For example, without function calling you would need to specify exactly how you would need your output structured by providing examples and a detailed description. However, if your use case is [structured data extraction](https://arize.com/blog-course/structured-data-extraction-openai-function-calling/?utm_campaign=Q323%20Content&utm_source=Content)then it is simplest to work directly with the OpenAI function calling API.

Overall, LLMs with function calling perform on par with LLMs that do not leverage function calling and instead use the ordinary prompt completion. Whether you decide to use the OpenAI function calling API over prompt engineering should depend on your use case and complexity of your outputs.

### OpenAI GPT Model Performance Comparisons

For model predictive ability on relevance overall:

- performance : GPT-4 ~ GPT-4-turbo ~ GPT-3.5-turbo >>> GPT-3.5-instruct

For model predictive ability on hallucinations:

- performance : GPT-4 ~ GPT-4-turbo > GPT-3.5-turbo > GPT-3.5-instruct

Interestingly, in both use cases, using explanations does not always improve performance. More on this below.

### Evaluation Metrics

If you are deciding which LLM to predict relevance, you want to use either GPT-4, GPT-4-turbo or GPT-3.5-turbo.

GPT-4-turbo is precisely identifying when an output is relevant, but is sacrificing on recalling all 50 examples, in fact recall is no better than a coin flip even when using explanations.

GPT-3.5-turbo suffers from the same trade-off, while having lower latency and lower accuracy. From these results GPT-4 has the highest F1 scores (harmonic mean of precision and recall) and overall best performance, while running comparable times to GPT4-turbo.

GPT-3.5-instruct and predicts everything to be relevant and therefore is not a viable LLM for predicting relevance. Interestingly, when using explanations the predictive performance improves drastically, although it still underperforms the other LLMs. Also GPT-3.5-instruct cannot use the OpenAI function calling API and is likely [to be deprecated in early 2024](https://platform.openai.com/docs/deprecations).

If you are deciding which LLM to predict hallucinations, you want to use either GPT-4, GPT-4-turbo or GPT-3.5-turbo.

The results show GPT-4 correctly identifying hallucinated and factual outputs more often (~3% of the time more) across precision, accuracy, recall and F1 than GPT-4-turbo.

While both GPT-4 and GPT-4-turbo perform slightly higher than GPT-3.5-turbo (*note a higher number of samples should be used before concluding that the small margin isn’t noise*), it might be worth working with GPT-3.5-turbo if you are planning to use explanations.

Explanations for predicting hallucinated and factual returned at a rate greater than three times faster for GPT-3.5-turbo than they did for both GPT-4 and GPT-4-turbo, however the recall did suffer for both GPT-3.5 models when compared to the recall of the GPT-4 models when predicting hallucinations correctly.

## Discussion

When deciding on which LLM to use for your application, there is a series of experiments and iterations required to make that decision. Similarly, benchmarking and experimentation is also required when deciding on whether or not a LLM should be used as an evaluator. Essentially these are the two main methods of benchmarking LLMs: LLM model evaluation (evaluating foundation models) and LLM system evaluation through [observability](https://arize.com/blog-course/large-language-model-monitoring-observability/).

![Evaluating two different prompt templates on a single foundational model. We are testing the same dataset across the two templates and seeing how their metrics like precision and recall stack up.](https://arize.com/wp-content/uploads/2023/12/llm-system-evals-benchmarking-gpt-models-leaderboard.jpg)

*Evaluating two different prompt templates on a single foundational model. We are testing the same dataset across the two templates and seeing how their metrics like precision and recall stack up.*

Ultimately, when deciding if an LLM will make a good performance evaluator for your use case, you need to consider the latency of your system in addition to the performance of relevant prediction metrics. Throughout this post we summarize how these models perform out of the box– without the addition of techniques to increase speed and performance. Recall that out-of-the-box all of these LLMs use zero-shot templates, so no examples were added to the LLM prompt template to improve the model outputs. Since these numbers act as a baseline, teams are able to improve the LLM system performance with prompt engineering, prompt templates (and stored libraries), agents, fine-tuning, as well as with search and retrieval applications like RAG and [HyDE](https://arize.com/blog/hyde-paper-reading-and-discussion/).

## Future Work: Explanations for Data Labeling

Through this benchmarking, we found some interesting examples where providing an explanation changes the predicted label. The example below predicts “relevant” when not using an explanation and even has a “relevant” label for the ground truth. Since even “golden datasets” can have mislabeling (especially for more subjective tasks), a well justified explanation from a LLM could be enough to edit the ground truth label. This can be thought of as a LLM assisted evaluation or quality check.

Below is one example from the wiki dataset for relevance, note column ‘D’ is the ground truth label provided by the dataset, column ‘E’ is the predicted label without function calling and without explanation, while column ‘F’ is the predicted label created (without function calling) with the explanation in column ‘G.’ Therefore column ‘E’ and columns ‘F’ & ‘G’ are responses from two separate LLM calls. F&G were generated together from the same call as seen from the figure below.

![](https://arize.com/wp-content/uploads/2023/12/script-example.png)

*Figure 1. Screenshot of script (code provided in colab). Here the label and explanation are returned together but we call for the explanation to be provided first (see prompt).*

In Table 3, we show an example when we have a ground truth label = ‘relevant’ , a LLM predicted label without function calling = ‘relevant’ , but then we have the label change to ‘irrelevant’ when the LLM is asked to provide an explanation first. Like several similar examples we encountered, the LLM makes a valid argument for labeling the retrieved answer to the user’s question as ‘irrelevant.’ While many of us think about the Roman Empire often, we can agree that the multi-paragraph response to “how long did the roman empire last?” is not a concise nor relevant enough response to elicit positive feedback from the end user. There are many possibilities for LLM assisted evaluations, including cost and time savings to companies that need data labeled. This as well as the visibility that explanations provide, along with LLMs returning their references (documents used in the prediction), are major advancements for the LLM observability space.

![Table 3. Relevance Example](https://arize.com/wp-content/uploads/2023/12/relevance-example-data.png)

## Conclusion

Hopefully this piece provides a good start for teams looking to better understand how GPT models and OpenAI features perform on correctly classifying hallucinated and relevant responses and the trade-offs between speed and performance for different LLM application systems. As always, the generative AI and LLMOps space are evolving rapidly so it will be interesting to watch how these findings and the space change over time.
