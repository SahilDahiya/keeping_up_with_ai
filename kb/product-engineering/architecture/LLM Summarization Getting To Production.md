---
title: 'LLM Summarization: Getting To Production'
topic: product-engineering
subtopic: architecture
secondary_topics:
- evals-observability/evaluation
summary: Covers production considerations for LLM summarization systems, including
  quality controls and deployment pitfalls.
source: arize
url: https://arize.com/blog/llm-summarization-getting-to-production/
author: Shittu Olumide
published: '2024-05-30'
fetched: '2026-07-11T04:48:55Z'
classifier: codex
taxonomy_rev: 1
words: 3236
content_sha256: a5a017c003eaacc8d3f80314fd5b59b023ea5acacdc03b2efcbf1b7ce4b5a102
---

# LLM Summarization: Getting To Production

Recently, I attended a workshop hosted by Arize AI’s Jason Lapatecki and Dat Ngo on large language model summarization covering common challenges with the use case and how to evaluate generated summaries. Drawing from this session and additional research, this article dives into the concept of LLM summarization – why it is important, primary summarization approaches and challenges, and a code-along example of LLM summarization evaluation using [Arize Phoenix](https://phoenix.arize.com/).

## What is LLM Summarization?

LLM summarization is the use of LLMs to generate concise and informative summaries of longer texts. These models leverage advanced natural language processing techniques to comprehend the content of the source document and produce abridged versions that capture the key points and main ideas for an LLM system.

![large language model summarization what it is](https://arize.com/wp-content/uploads/2024/05/llm-summarization-what-is.png)

*This image shows how LLM summarization works – document input comes from different data sources and passes through the LLM, which generates a summary*

The rate at which information grows in this age and time of big data is massive. The emergence of powerful language models also intensifies the volume of data produced. In this era when information inundates various platforms, summarization serves as a strategic filter, swiftly extracting key points from the vast sea of information for use in applied LLM systems.

### Benefits of Summarization

Benefits of summarization range from streamlining the processing of extensive information, thereby saving considerable time for individuals, to enhancing the efficiency of information retrieval, facilitating quicker access to relevant content, and promoting better retention and understanding of materials, leading to improved learning outcomes.

## LLM Summarization Use Cases

There are numerous examples of summarization use cases for LLM systems, each demonstrating the versatility of this technology, such as news aggregation, email summarization, document summarization, meeting summarization, product reviews, and more.

In this section, we will look at three of these use cases using the illustration below.

![](https://arize.com/wp-content/uploads/2024/05/llm-summarization-industry-applications.png)

*LLM summarization: example use cases*

The first application shows how a lot of information across many documents is needed to grab core concepts or relevant information across the vast information available. This is usually the case when you are trying to summarize multiple papers or articles, or are trying to get key facts from case law or multiple regulatory filings.

The second example shows a meeting summarization, by using the [Gong call spotlight](https://www.gong.io/product/call-spotlight/) to automatically give you critical insights from your conversations, like outcomes, deliverables, and next steps. Zoom AI Companion is another version of this concept.

The third use case is an AI-generated review summary by Amazon. Amazon unveiled [its newest enhancement](https://www.aboutamazon.com/news/amazon-ai/amazon-improves-customer-reviews-with-generative-ai) to customer reviews through generative AI last year. This feature condenses sentiments expressed across thousands of verified customer reviews into a concise paragraph.

## LLM Summarization Approaches

A widely-cited research paper — “[An Empirical Survey on Long Document Summarization: Datasets, Models, and Metrics](https://arxiv.org/pdf/2207.00939)” — classifies summarization approaches as either extractive or abstractive or both (hybrid).

![](https://arize.com/wp-content/uploads/2024/05/best-summarization-approaches-long-documents.png)

### Extractive Approach

This approach involves directly selecting and assembling specific sentences or passages from the source document to create a summary. Rather than generating new content, this method relies on identifying the most relevant and informative segments of the original text and presenting them in a condensed form.

#### Pros of using the extractive approach

The pros of using the extractive approach include factual accuracy, transparency, context preservation, reduction in risk bias, and simple implementation. Here are more details on each of these:

| Benefit | Rationale |
| Factual Accuracy | The extractive approach retains the original wording and context of the source document, ensuring a high degree of factual accuracy in the summary. |
| Transparency | Since the summary is composed of verbatim sentences extracted from the source document, the process of summarization is transparent and easy to understand. |
| Preserves Context | By directly selecting sentences from the source text, extractive summarization preserves the context and coherence of the original content, maintaining the logical flow of ideas. |
| Reduces Risk of Bias | Since the summary is based on objective criteria for selecting sentences, such as relevance, there is a reduced risk of introducing bias into the summary. |
| Simple Implementation | Extractive summarization techniques are relatively straightforward to implement, making them accessible and practical for various applications. |

#### Cons of using the extractive approach

There are several drawbacks of using the extractive approach, including lack of creativity, redundancy, and inability to fill gaps. Since extractive summarization does not involve generating new content or rephrasing information, summaries may lack creativity or originality or contain redundant or repetitive information as sentences are selected independently of each other without considering their mutual relevance. Also, the fact that extractive summarization only includes sentences directly extracted from the source document may fail to address gaps in information or provide additional context that is not explicitly stated in the original text.

### Abstractive approach

The abstractive approach to summarization involves a deeper level of comprehension and interpretation compared to the extractive method. Rather than simply selecting and stitching together existing sentences from the source document, abstractive summarization aims to understand the underlying meaning and concepts expressed in the text.

At the core of abstractive summarization is the emulation of human comprehension. Rather than being bound by the exact wording of the source material, abstractive systems aim to grasp the essence of the content, identifying key ideas, relationships, and themes. This understanding allows the system to generate summaries that may not exist verbatim in the original document but effectively capture its core message.

#### Pros of using the abstractive approach

The pros of using the abstractive approach include producing human-like summaries, retaining semantic meaning, and handling complex texts. Here are more details on each of these:

| Benefit | Rationale |
| Retains Semantic Meaning | Unlike extractive summarization, which may result in disjointed or fragmented summaries, abstractive summarization preserves the semantic meaning of the original text by paraphrasing and rephrasing content in a coherent manner. |
| Produces Human-Like Summaries | Abstractive summarization models can generate summaries that closely resemble human-written text in terms of style, tone, and readability, enhancing the user experience and making the summaries more engaging and relatable. |
| Handles Complex Texts | This is particularly effective for handling complex texts that contain nuanced arguments, technical jargon, or domain-specific terminology, as it can extract and distill the key concepts and ideas from such content. |

#### Cons of using the abstractive approach

The cons of using the abstractive approach include difficulty in ensuring accuracy, challenges in content preservation, and dependency on training data. Here are more details on each of these:

| Drawback | Rationale |
| Difficulty In Ensuring Accuracy | Since abstractive summarization involves paraphrasing and rephrasing the original text, there is a risk of introducing errors or inaccuracies into the summary, especially when dealing with complex or ambiguous content. |
| Challenges In Content Preservation | Abstractive summarization may struggle to preserve all the important details and nuances present in the original text, leading to potential loss of information or misrepresentation of key points in the summary. |
| Dependency On Training Data | Abstractive summarization models rely heavily on large datasets for training, which may limit their effectiveness in summarizing texts from domains or languages with limited available data. |

### Hybrid Approach

The hybrid approach in summarization represents a strategic synthesis of both extractive and abstractive techniques. It aims to leverage the advantages of each method while mitigating their respective limitations, ultimately producing summaries that are both informative and coherent.

The hybrid approach begins with an extractive phase, where the system identifies and selects crucial content from the source document. This initial extraction phase serves as a foundation, ensuring that the summary captures the most salient information accurately. Then, the hybrid approach transitions into an abstractive phase. Here, the system employs more sophisticated language processing techniques, such as LLM, to refine and enhance the extracted content.

#### Pros of using the hybrid approach

Potential gains from using the hybrid approach include enhanced accuracy, improved coherence, and comprehensive coverage. Here are more details on each of these.

| Benefit | Rationale |
| Enhanced Accuracy | By starting with an extractive phase, the Hybrid approach ensures that the summary includes crucial information directly sourced from the original document. This initial extraction phase helps maintain the factual accuracy of the summary. |
| Improved Coherence | Through the abstractive phase, the Hybrid approach refines the extracted content, rephrasing it in a more coherent and readable manner. This helps create summaries that flow smoothly and maintain logical coherence, improving comprehension for readers. |
| Comprehensive Coverage | By combining elements of both extractive and abstractive techniques, the Hybrid approach can capture a broader range of information from the source document. This allows for more comprehensive summaries that encapsulate key concepts and details. |

#### Cons of using the hybrid approach

The cons of using the hybrid approach include complexity, difficulty in optimization, and performance trade-offs.

| Drawback | Rationale |
| Complexity | Implementing the hybrid approach requires sophisticated algorithms and language processing techniques to seamlessly integrate extractive and abstractive methods. This complexity can increase the computational resources and development time needed for building summarization systems. |
| Difficulty in Optimization | Balancing the extractive and abstractive components of the Hybrid approach can be challenging, as optimizing one aspect may come at the expense of the other. Achieving the right balance between accuracy and readability requires careful tuning and experimentation. |
| Performance Trade-Offs | Depending on the specific task or domain, the hybrid approach may not always outperform purely extractive or abstractive methods. The performance of the Hybrid approach can vary based on factors such as the complexity of the source document and the quality of the summarization algorithms employed. |

## LLM Summarization Challenges

Summarization tasks vary depending on the specific content being summarized and the objectives at hand. The nature of the data being processed dictates the approach one should take when tackling the task.

There are two types of documents: long documents (research papers, long meeting transcripts, and thousands of reviews) and short documents (news articles, single pages or excerpts, and product reviews).

As data expands, capturing its essence becomes increasingly challenging. Ensuring that a summary effectively encapsulates the larger text presents a significant hurdle. Consequently, the question arises: **does this token in my possession have a good representation of the summary of the large text?**

Some issues with long documents are explored below.

### Recursion Issues – Map Reduce

Dividing texts into chunks without considering their logical and structural flow can pose problems for summarization. We can condense chunk one and chunk two into shorter summaries. Then, we can recursively summarize until we achieve a coherent result.

Let’s say you have a document and you split it into two chunks with a chunk size of 200, with an overlap between the chunks so that there is coherency so you don’t lose data between them. Combining the summary of chunk one and chunk two will give us the final summary.

![](https://arize.com/wp-content/uploads/2024/05/map-reduce.png)

### Refine Issues

Sequentially going through the document, let’s say for the first chunk you summarize it and then you combine the summary with the next chunk, then you also summarize that too.

However, this sequential refinement process cannot be parallelized, meaning it progresses linearly — ultimately taking more time compared to a recursive method. Additionally, the order in which topics appear in the document can influence the summarization outcome.

![](https://arize.com/wp-content/uploads/2024/05/llm-summarization-refine-issues.png)

## Better Chunking For Summarization

Combining summarization with topic modeling can yield excellent results. To enhance summarization quality, avoid arbitrary segmentation based solely on length. The significance of a text snippet within a specific topic should not be solely dictated by its length. You have to utilize case-specific approaches and also understand that lengthy documents with interconnected concepts may require a different summarization strategy compared to product review summaries, for example.

The image below illustrates the chunking of a State of the Union speech which has 10 nicely continuous clusters.

![](https://arize.com/wp-content/uploads/2024/05/chunking-strat-sotu.png)

*How to perform better chunking for long document summarization and its benefits (*

[source](https://towardsdatascience.com/summarize-podcast-transcripts-and-long-texts-better-with-nlp-and-ai-e04c89d3b2cb))## Evaluation

Evaluation generally consists of an evaluation of LLM outputs by using a separate evaluation LLM. This process typically entails using one LLM as a benchmark or reference model to evaluate the outputs generated by the other LLM. Evals is a library that allows teams to generate evals for either chains or individual spans.

![](https://arize.com/wp-content/uploads/2024/05/how-llm-evaluation-works.png)

*How LLM evaluation works;*


[see here](https://arize.com/blog-course/llm-evaluation-the-definitive-guide/)for a comprehensive guide to large language model evaluation### Fundamentals of LLM Production Evals

The fundamentals of LLM evaluation for production include benchmarking with a golden dataset, leveraging task-based evals, and running across environments.

- **Benchmark with the golden dataset**: Utilize metrics such as- **Precision**,- **Recall**- **F1 score**- **golden**” dataset, which serves as a reference for correctness.
- **Tasked-based evals**: LLM evals should be task-oriented, meaning they should consider specific templates and dataset combinations to define performance. Different tasks may require different evaluation criteria based on the intended use case and the nature of the content being summarized.
- **Evals need to run across environments**(Python, Notebooks, and LangChain/LlamaIndex) and need to be as fast as possible.

### LLM Summarization Evaluation

By injecting the Eval template into the prompt/data, you can calculate metrics — like precision, recall, F1 — because we are using another LLM to grade that specific response or summary. You can use the Phoenix library for Evals, it is an open-source observability library designed for experimentation, evaluation, and troubleshooting.

Key details:

- [Summarization Eval](https://docs.arize.com/phoenix/evaluation/how-to-evals/running-pre-tested-evals/summarization-eval)
- [Summarization performance](https://docs.arize.com/phoenix/evaluation/how-to-evals/running-pre-tested-evals/summarization-eval)
- *Tested on:*- [GigaWord](https://www.tensorflow.org/datasets/catalog/gigaword),- [CNNDM](https://paperswithcode.com/dataset/cnn-daily-mail-1),- [Xsum](https://paperswithcode.com/dataset/xsum)

### Code Walkthrough of LLM Summarization Evaluation

In this section, we will perform a summarization classification task. The goal is to evaluate the performance of an LLM-assisted approach to evaluating summarization quality. Similarly, this walkthrough will serve as an experimental framework for us to iterate and improve on the default classification template.

*Note: We will make use of a benchmark dataset and  OpenAI’s API (this is because we want to compare summarization using GPT-4, GPT-3.5 and GPT-4 Turbo).*

#### Install required libraries

`pip install -qq "arize-phoenix-evals>=0.0.5" "openai>=1"`Proceed to import the libraries in your notebook or any development environment of your choice.

```
import os
from getpass import getpass
import matplotlib.pyplot as plt
import openai
import pandas as pd
import phoenix.evals.templates.default_templates as templates
from phoenix.evals import (
   OpenAIModel,
   download_benchmark_dataset,
   llm_classify,
)
from pycm import ConfusionMatrix
from sklearn.metrics import classification_report
pd.set_option("display.max_colwidth", None)
```
#### Download the benchmark dataset

We will assess the performance of the evaluation system, comprising an LLM model, various settings, and an evaluation prompt template, against benchmark datasets containing queries and retrieved documents annotated with ground-truth relevance labels. Our evaluation will utilize the [CNN Daily News Mail dataset](https://paperswithcode.com/dataset/cnn-daily-mail-1), widely recognized as a standard benchmark for text summarization models.

```
df = download_benchmark_dataset(
   task="summarization-classification", dataset_name="summarization-test"
)
df.head()
```
#### Display binary summarization classification template

You can view the default template used to classify summarization and you can tweak this template to evaluate its performance relative to the default.

print(templates.SUMMARIZATION_PROMPT_TEMPLATE)

![](https://arize.com/wp-content/uploads/2024/05/example-summarization-prompt-template.png)

*Example LLM summarization prompt evaluation template*

From the example summarization prompt eval template above, you will notice two variables **input** and **output**. The input variable is the document text to summarize while the output variable is the summary of the document.

You can make this template custom which means that you can choose to rate it good, bad, or neutral and this can be changed on the fly, you can edit and change it to a specific use case.

#### Configure the LLM

As earlier stated, we will make use of OpenAI, so let’s configure the OpenAI API key.

```
if not (openai_api_key := os.getenv("OPENAI_API_KEY")):
   openai_api_key = getpass("🔑 Enter your OpenAI API key: ")
openai.api_key = openai_api_key
os.environ["OPENAI_API_KEY"] = openai_api_key
```
#### Benchmark dataset sample

The sample size determines run-time, it is recommended to iterate small samples, for example, 100 samples then increase to a large test set.

```
N_EVAL_SAMPLE_SIZE = 100
df_sample = (
   df.sample(n=N_EVAL_SAMPLE_SIZE)
   .reset_index(drop=True)
   .rename(columns={"document": "input", "summary": "output"})
)
```
#### LLM Evals: Summarization Evals Classifications GPT-3.5

Let’s evaluate by classifying the quality of the summarization generated by an LLM (GPT-3.5), this process typically entails running summarization classification against a subset of data, often referred to as a benchmark dataset.

`model = OpenAIModel(model_name="gpt-3.5-turbo", temperature=0.0, request_timeout=20)`Using the OpenAIModel, we set the model name and other parameters such as temperature and request timeout.

```
rails = list(templates.SUMMARIZATION_PROMPT_RAILS_MAP.values())
summarization_classifications = llm_classify(
   dataframe=df_sample,
   template=templates.SUMMARIZATION_PROMPT_TEMPLATE,
   model=model,
   rails=rails,
   provide_explanation=True #optional to generate explanations for the value produced by the eval LLM
)["label"].tolist()
```
Rails is used to hold the output to specific values based on the template, it will remove text such as “,,,” or “…”. It also ensures that the binary value expected from the template is returned.

```
true_labels = df_sample["user_feedback"].map(templates.SUMMARIZATION_PROMPT_RAILS_MAP).tolist()
print(classification_report(true_labels, summarization_classifications, labels=rails))
confusion_matrix = ConfusionMatrix(
   actual_vector=true_labels,
   predict_vector=summarization_classifications,
   classes=rails,
)
confusion_matrix.plot(
   cmap=plt.colormaps["Blues"],
   number_label=True,
   normalized=True,
)
```
This block of code is performing the evaluation and visualization task related to the classification of summarization quality based on user feedback.

![](https://arize.com/wp-content/uploads/2024/05/confusion-matrix-gpt3.png)

*This is the output of the classification report. It compares the true labels (obtained from user feedback) against the predicted classifications.*

![](https://arize.com/wp-content/uploads/2024/05/confusion-matrix-first.png)

*the confusion matrix of the true labels and predicted classifications using GPT-3.5*

#### LLM evals: summarization evals classifications GPT-4

We can also run summarization classifications against a subset of the data using GPT-4 so that we can compare the performance of these LLMs.

Instantiate the LLM and set parameters.

```
model = OpenAIModel(
   model_name="gpt-4",
   temperature=0.0,
)
```
Rails removes text such as “,,,” or “…”, and ensure that the binary value expected from the template is returned.

```
rails = list(templates.SUMMARIZATION_PROMPT_RAILS_MAP.values())
summarization_classifications = llm_classify(
   dataframe=df_sample,
   template=templates.SUMMARIZATION_PROMPT_TEMPLATE,
   model=model,
   rails=rails,
   provide_explanation=True # optional to generate explanations for the value produced by the eval LLM
)["label"].tolist()
```
Evaluate the predictions against human-labeled ground-truth summarization labels.

```
true_labels = df_sample["user_feedback"].map(templates.SUMMARIZATION_PROMPT_RAILS_MAP).tolist()
print(classification_report(true_labels, summarization_classifications, labels=rails))
confusion_matrix = ConfusionMatrix(
   actual_vector=true_labels,
   predict_vector=summarization_classifications,
   classes=rails,
)
confusion_matrix.plot(
   cmap=plt.colormaps["Blues"],
   number_label=True,
   normalized=True,
)
```
![](https://arize.com/wp-content/uploads/2024/05/metrics-llm-summarization-evaluation-pre-tested-library.png)

*This is the output of the classification report. Comparing the true labels against the predicted classifications*

![](https://arize.com/wp-content/uploads/2024/05/confusion-matrix-gpt-4-llm-sum.png)

*The confusion matrix of the actual classes and predicted classifications using GPT-4*

#### LLM Evals: Summarization Evals Classifications GPT-4 Turbo

Since we have performed summarization Eval classification on GPT-3.5 and GPT-4, you will notice that there is a significant increase in the quality of predictions. Let’s now try to use GPT-4 Turbo and see if we can get a better result.

`model = OpenAIModel(model_name="gpt-4-turbo-preview", temperature=0.0)`The rails are used to hold the output to specific values based on the template.

```
rails = list(templates.SUMMARIZATION_PROMPT_RAILS_MAP.values())
summarization_classifications = llm_classify(
   dataframe=df_sample,
   template=templates.SUMMARIZATION_PROMPT_TEMPLATE,
   model=model,
   rails=rails,
   provide_explanation=True #optional to generate explanations for the value produced by the eval LLM
)["label"].tolist()
```
Finally, evaluate the predictions against human-labeled ground-truth summarization labels.

```
true_labels = df_sample["user_feedback"].map(templates.SUMMARIZATION_PROMPT_RAILS_MAP).tolist()
print(classification_report(true_labels, summarization_classifications, labels=rails))
confusion_matrix = ConfusionMatrix(
   actual_vector=true_labels,
   predict_vector=summarization_classifications,
   classes=rails,
)
confusion_matrix.plot(
   cmap=plt.colormaps["Blues"],
   number_label=True,
   normalized=True,
)
```
![](https://arize.com/wp-content/uploads/2024/05/results-metrics-precision-f1-gpt-4-turbo-llm-sum-perf.png)

*Output of the classification report. Comparing the true labels against the predicted classifications*

![](https://arize.com/wp-content/uploads/2024/05/confusion-matrix-gpt-turbo-llm-summarization-task.png)

*The confusion matrix of the actual classes and predicted classifications using GPT-4 Turbo*

## Conclusion

To recap, this article covers how to perform LLM summarization, the wide range of important factors around LLM summarization – like better ways to chunk data for summarization – and how to perform summarization evals classification with LLM evals using three OpenAI models.  For more details, see the LLM Evals [documentation](https://docs.arize.com/phoenix/evaluation/llm-evals). Comments or questions? Feel free to reach out in the [Arize Community](https://arize.com/community/).
