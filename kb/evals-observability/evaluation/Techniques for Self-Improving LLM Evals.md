---
title: Techniques for Self-Improving LLM Evals
topic: evals-observability
subtopic: evaluation
secondary_topics: []
summary: Covers techniques for making LLM evals self-improving through feedback, iteration,
  and evaluator refinement.
source: arize
url: https://arize.com/blog/techniques-for-self-improving-llm-evals/
author: Eric Xiao
published: '2024-10-23'
fetched: '2026-07-11T04:50:20Z'
classifier: codex
taxonomy_rev: 1
words: 1664
content_sha256: 729ce53928700da2aaa66db29aee713617c663773c8ab2cf2235e63204a9e95f
---

# Techniques for Self-Improving LLM Evals

![Technique for self-improving evals - blog Techniques for self-improving llm evals graphic](https://arize.com/wp-content/uploads/2024/10/Technique-for-self-improving-evals-blog-1021x560.jpg)

              # Techniques for Self-Improving LLM Evals

LLM evaluations have become a great tool for benchmarking performance - and they’re particularly useful for times where measuring the quality of the output is complicated, like in summarization or classification, for instance.

Teams sometimes use LLM-assisted evals to help with things like ranking or suggesting improvements for the evaluation process. LLM-as-a-judge is a popular way AI practitioners can benchmark and evaluate performance for their applications. These are usually evals built specifically for judging task outputs where it is difficult to ascertain quality. An example might be using an LLM to assist in reviewing consistency of translations across multiple languages, or in validating responses for a chatbot.

If you’ve implemented a series of LLM-based evaluations or unit tests but aren’t sure if your methods are robust, this guide is for you. In this article, we’ll explore how to create self-improving [LLM evals](https://arize.com/llm-evaluation/) by following a systematic approach:

- Curating a dataset of examples
- Determining evaluation criteria using LLMs
- Updating prompts using human annotations
- Fine-tuning your evaluation model

![Examples, Criteria, Annotations, Prompt Tuning](https://arize.com/wp-content/uploads/2024/10/image1-1024x594.png)


## Step 1. Curating Your Dataset of Examples for Effective LLM Evals

Curating your dataset of examples is the first step if you want to create self-improving evals, but it consists of two separate parts: manual creation or selection, automated generation. We’ll review both below.

### Manual Creation or Selection

In every part of the self-improving process, you need data to tell your AI application how to improve. You can curate this manually to start by selecting examples from your traces, or by hand-writing them yourself.

![](https://arize.com/wp-content/uploads/2024/10/Dataset-Gif.gif)


You can find problematic traces using your observability application and filter for problematic outputs, such as bad requests, timeout errors, long latency, blank prompt variables, and low scoring evaluations. You can also use our embeddings UMAP view to identify clusters of data to find trends.


![Embeddings Gif](https://arize.com/wp-content/uploads/2024/10/clusters.gif)

### Streamline LLM Evals with AI-Generated Test Cases

When you are in the development phase, often you don’t have any data, so you need to manually create test cases in excel. You can use LLMs to generate unit tests and code-based assertions for your application.

You can also use LLMs to synthetically generate example LLM as a judge test cases based on your prompts. Here’s an example, where we can use ChatGPT or your LLM of choice to create a set of examples.

```
You are a data analyst. You are using LLMs to summarize a document. Create a CSV of 20 test cases with the following columns:
1. Input: The full document text, usually five paragraphs of articles about beauty products.
2. Prompt Variables: A JSON string of metadata attached to the article, such as the article title, date, and website URL
3. Output: The one line summary
```

This will generate a CSV file for you that you can use as your first dataset of assertions:


| Input | Prompt Variables | Output |
|---|---|---|
| With the rise of beauty trends and innovations, many new skincare products have emerged in the market. This article reviews the latest in anti-aging serums, focusing on their ingredients and effectiveness. Experts weigh in on the benefits of Vitamin C and hyaluronic acid, two popular components in modern skincare. The review highlights both high-end and budget-friendly options, providing a comprehensive guide for consumers. The rise in popularity of natural and organic products is also discussed. | {“title”:”Top Anti-Aging Serums Reviewed”,”date”:”2024-08-25″,”url”:”https://beautywebsite.com/top-serums”} | The article reviews the latest anti-aging serums, comparing ingredients, effectiveness, and price points will highlighting the shift toward natural products. |
| Explore the world of luxury beauty products with this detailed guide. This piece delves into the benefits of premium skincare items, including serums and moisturizers. It covers the history of luxury beauty brands and their evolution over time. The guide includes expert opinions on which products offer the best results and why they are worth the investment. Special focus is given to emerging trends in the luxury beauty market and consumer attitudes towards high-end products. | {“title”:”The Allure of Luxury Beauty Products”,”date”:”2024-08-26″,”url”:”https://beautywebsite.com/allure”} | This guide examined luxury beauty products, their benefits, brand histories, expert opinions, and emerging market trends. |

## Step 2. Determine Your Evaluation Criteria Using LLMs

Typically when creating an LLM evaluator, you can use pre-tested evaluation templates along with prompt engineering to get a fairly effective evaluation prompt template. But to get to the next level of reliability, you need to be able to evaluate your evaluator. In [this paper on EvalGen](https://arize.com/blog/breaking-down-evalgen-who-validates-the-validators/), we discuss validating the validators by aligning them with human preferences.

A typical evaluation pipeline looks like the following:

![Typical evaluation pipeline](https://arize.com/wp-content/uploads/2024/10/image3-1024x309.png)


In this graphic you can see that there is a prompt under test with a set of inputs and outputs, and an evaluator LLM which judges the output based on your specified criteria.

But how do you decide what is a good criteria? Specific criteria will be more precise but less robust. An example of an abstract criteria is to judge whether the response is “polite.” A more concrete assertion specifies whether the response “contains words like please, thank you, or sorry.”

We can try to toe the line between abstract criteria and concrete assertions by using LLMs to create assertions. Then human annotators grade the responses, and the evaluator can determine which assertions align best with the human scoring.


![EvalGen evaluation pipeline](https://arize.com/wp-content/uploads/2024/10/image4-1024x523.png)


Let’s say you had a message thread with a travel agent chatbot you are trying to evaluate. An example of an abstract criteria is to judge whether the response is “polite.” A more concrete assertion specifies whether the response “contains words like please, thank you, or sorry.” Sometimes they match! But sometimes they are too specific.

Based on this lack of alignment, you can use LLMs to regenerate assertions based on the new sample of data to retry, and remove poorly performing assertions:


```
user
Can you give me a quick travel itinerary for a day in San Francisco?
Assistant
Certainly, here’s a quick travel itinerary for San Francisco. You can visit these three destinations: (1) Golden Gate Bridge (2) The Marina (3) Fisherman’s Wharf.
```

| Evaluator | Grade | |
|---|---|---|
| Criteria | Is the response polite? | Yes |
| Assertion(generated by LLM) | Does the response contain words like please, thank you, or sorry? | Negative |

## Step 3. Refine Your Prompts Using Human Annotations to Improve LLM Evals

Now that you have your golden dataset of corrections, you need to choose which ones to provide within the prompt that best demonstrate what you’re looking for.

You can start with a set of standard few-shot examples, but likely you will want to use examples that are more relevant to the input, documents, and output.

![](https://arize.com/wp-content/uploads/2024/10/Annotations-Gif.gif)


You can select data points based on semantic distance between your input and human annotated data.

Let’s use the following evaluation prompt to check for hallucination. Notice we have an additional section to add few-shot examples using the {examples} prompt variable.


```
In this task, you will be presented with a query, a reference text and an answer. The answer is generated to the question based on the reference text. The answer may contain false information. You must use the reference text to determine if the answer to the question contains false information, if the answer is a hallucination of facts. A 'hallucination' refers to
an answer that is not based on the reference text or assumes information that is not available in
the reference text. Your response should be a single word: either "factual" or "hallucinated", and
it should not include any other text or characters. "hallucinated" indicates that the answer
provides factually inaccurate information to the query based on the reference text. "factual"
indicates that the answer to the question is correct relative to the reference text, and does not contain made up information.
Use the examples below for reference:
{examples}
Here is the query, reference, and answer.
   # Query: {query}
   # Reference text: {reference}
   # Answer: {response}
Is the answer above factual or hallucinated based on the query and reference text?
```

How do you determine which examples to add to your prompt? You can select your examples based on the cosine similarity between each of the given prompt variables. You can add examples of queries that are very similar to the user query to increase your precision.

You can also use an LLM to summarize the examples and insert them as additional instructions. As you add additional examples, you can start catching more and more edge cases, add them to your prompt, and re-test them against your golden dataset to ensure reliability.


![](https://arize.com/wp-content/uploads/2024/10/image2-1024x665.png)


You can track the effectiveness of this approach using Arize experiments. Each time you run your new prompt with selected examples across your data, you can get performance and evaluation metrics against your test dataset to see whether this approach is improving your alignment with human annotations of your evals.

## Step 4. Fine-Tune Your Model for Self-Improving LLM Evals

Once you’ve built a robust dataset and chosen your examples, the last step is fine-tuning your evaluator. You can fine-tune your evaluator just like you can fine tune the LLM used for your application by uploading the data points you collected earlier.

This also allows you to use smaller language models, which reduces latency and cost while maintaining similar levels of performance. As your dataset of corrections increase, you can connect your evaluator to your CI/CD pipeline and continuously run fine tuning jobs to increase the precision of your evaluator.

We have an upcoming piece that dives into fine-tuning in more detail!

## Conclusion: LLM Evals are an Iterative Process

We hope you enjoyed this guide to self-improving LLM evaluations. Building LLM evals is an iterative process, and with the right techniques and tools, you can improve your evaluation pipeline in tandem with your LLM application performance.
