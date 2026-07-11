---
title: How to Improve LLM Safety and Reliability
topic: evals-observability
subtopic: testing
secondary_topics:
- product-engineering/security
summary: Covers testing and monitoring practices for improving LLM application safety
  and reliability in production.
source: arize
url: https://arize.com/blog/improving-safety-and-reliability-of-llm-applications/
author: Eric Xiao
published: '2024-11-11'
fetched: '2026-07-11T04:50:30Z'
classifier: codex
taxonomy_rev: 1
words: 1875
content_sha256: 0a0066cde8cb8c8ad660342f0195f52043839ab00ca38e66d5dd6227d9fd41fa
---

# How to Improve LLM Safety and Reliability

As language models (LLMs) become integral to customer-facing applications, safety is a requirement. When AI systems are trusted to provide information, guidance, and customer support, lapses in safety can have serious consequences.

There are many real-world examples where LLMs have ended up in the news, sometimes in unexpected and unsettling ways: AI-powered search engines suggesting unsafe uses for household items, chatbots offering advice that crosses ethical or legal boundaries, and customer service bots making costly errors like offering cars for a dollar. These incidents highlight the critical need for robust safety measures in LLMs, not only to protect users but also to uphold brand trust and prevent damage to reputations.

![Some headlines that show cases where LLMs have been unsafe or cause for concern.](https://arize.com/wp-content/uploads/2024/11/image9-1-1024x422.png)

Safety and reliability is not a singular metric, it is comprehensive across every part of your application–and there are so many ways to measure safety. You can look at what the user input contains, what document chunks you’re retrieving to put into the context window, what the response contains, and what the qualitative outputs of the response are.

Today’s AI engineering loop is very brittle, where small changes can result in big performance drops. Building better AI requires that you address LLM safety and reliability, and in this blog, we’ll show you how. Read on to learn about all the different ways to improve safety and reliability in your LLM applications, including tracing, evaluations, experiments, guardrails, and more.

![Includes a grid of the many different ways to measure safety and reliability based on what the input contains](https://arize.com/wp-content/uploads/2024/11/image10-e1731094997766-1024x438.png)

### Getting Started: Tailoring LLM Evaluation to Your Task

The first thing to note is that evaluation needs to be tailored to your task, not an LLM benchmark. There are many different evaluation benchmarks across various models, such as MMLU or LLM’s SysChatbot Arena, as well as specific datasets tied to bias, harmlessness, and toxicity. But these evaluations only get you so far. They are meant to compare different chat models against each other, and they’re directionally accurate.

The only thing that really matters is how well it performs on your task. How an LLM model eval is generated is based on a set of thousands of different questions where it generates answers, and it’s annotated with a score of whether or not it’s accurate.

A task eval is based on your context, where the user is in the journey of using your application, what prompt template you’re using, where they are within the conversation, whether it’s a background task, whether a human is in the loop, or if it’s an actual chatbot generating responses to customer support agents.

![LLM model evals and llm task evals](https://arize.com/wp-content/uploads/2024/11/image12-e1731094950401-1024x714.png)

### Next Up: Building Task Evaluation with a Golden Dataset

To evaluate your performance, you need data points to prove whether it’s working.

Below is an example of a dataset for a chatbot that helps you book a hotel based on the dates you want to book and the destination you want to go. On the left-hand side is the user input query. The middle shows the context that the retriever returns in response, and the response is the LLM output generated to address the user query. You also have a set of ground truth labels to determine if this query is accurate based on the criteria you want to judge.

![Here’s an example below of a dataset for a chatbot that helps you book a hotel based on the dates you want to book and the destination you want to go. On the left-hand side is the user input query. The middle shows the context that the retriever returns in response, and the response is the LLM output generated to address the user query. You also have a set of ground truth labels to determine if this query is accurate based on the criteria you want to judge.](https://arize.com/wp-content/uploads/2024/11/image8-e1731094905202-1024x532.png)

So, given this dataset or your task, how would you actually benchmark whether your LLM application is working? The way to benchmark it is to base it on what you believe is a good enough user experience.

An example of this is GitHub Copilot, where autocomplete within your code doesn’t always have to be correct because there’s a human in the loop. It’s forgiving—if it recommends the wrong autocomplete, the user can simply continue coding as if the autocomplete did not exist. However, if you have an LLM engineer agent like Devin coding on your behalf and you’re delegating a much more abstract task, the floor for what is considered “good enough” is much higher.

Model benchmarks are directionally correct, but the real benchmark is how it performs against your task. For safety cases, that could mean aiming for 0% of the time or maybe 2% of the time, depending on your application and how bad the offending output is.

## Improving LLM Safety & Reliability in Four Steps

![](https://arize.com/wp-content/uploads/2024/11/image6-1-e1731097114689-1024x303.png)

Today’s AI engineering loop is very brittle. Without evals, AI engineers don’t know if prompt changes will actually improve performance. They create a prompt to help achieve a certain outcome, whether it’s summarization or data extraction or building a chatbot support agent for a specific use case. And the reality is that once you get the demo working, creating iterations and refinements are generally non-deterministic. So you don’t know whether by changing a prompt or a model or a retrieval step, are you going to break a use case or are you going to degrade performance?

When you’re just trying to get something working quickly, you don’t have any visibility into what’s actually breaking and what’s working. You can’t judge what you can’t see. You have your prompt templates, retrieved documents, prompt variables, embeddings, function calls, and outputs. How do you actually make sure that every step is working? You really need every level of visibility into your application, essentially a full stack trace of logs for your LLM app.

![A trace tree for an LLM application in Arize](https://arize.com/wp-content/uploads/2024/11/image13-1-1024x441.png)

Once you have visibility, you can add the following components to your development process to improve reliability:

- Create evaluators to judge performance
- Use experiments to track performance over time
- Set up guardrails to protect performance in production
- Data curation to improve performance in production

Let’s explore each of these in detail.

### 1. Create Evaluators to Judge LLM Performance

Now you have your working demo. You have a set of outputs that you can generate. You need to figure out a way to actually measure performance. You can start by generating scores for relevance, hallucination and latency with manual annotations or with LLM as a judge. But if you only have these metrics for a small set of cases, you don’t have a reliable signal of whether it will work in the wild in production against many different kinds of questions and queries.

The first step is to have a good evaluator. You also need to have an evaluation prompt template, which you can use to run against a variety of different output metrics or a variety of different data points in your data set to generate a label like relevant, not relevant, with a given explanation.

![](https://arize.com/wp-content/uploads/2024/11/image5-1-e1731362814544-1024x546.png)

Below is an example of an evaluation we ran on an Arize Docs chatbot, where we evaluated it for QA correctness and hallucination. The evaluator gives it a label, score, and explanation, which you can aggregate to get an overall performance indicator on your application.

![An example of an evaluation we ran on an Arize Docs chatbot, where we evaluated it for QA correctness and hallucination. The evaluator gives it a label, score, and explanation, which you can aggregate to get an overall performance indicator on your application.](https://arize.com/wp-content/uploads/2024/11/image7-1024x583.png)

### 2. Use Experiments to Track Performance Over Time

Once you have your evaluator, you need a good evaluation process. You also need a set of examples that you’ve curated to test against a variety of use cases, whether it’s toxic responses or hotel bookings in multiple locations. It’s important to be able to track those changes.

You can change your model, change your prompt, change the context. Then run that change against the same data and then get an evaluation score. Then you can start evaluating your application on multiple levels and run these tests on every build in your CI/CD pipeline. So you’re constantly testing your application for reliability on every change.

And you can even create self-improving systems where you have your data set of examples, which can be generated via your LLM. Determine a different set of assertions and evaluation criteria using your LLMs to be more or less specific, to use code-based validators or LM-based qualitative evaluation. And then you can use human annotations to make corrections when it’s gone wrong or awry. When you tune your prompts and you’re retrieving sets of examples, you can add a few-shot examples to make the prompts perform better on the various different use cases that you have.

![](https://arize.com/wp-content/uploads/2024/11/image3-1024x318.png)

In Arize, you can track every experiment run as an audit trail for your AI application, similar to running test cases for typical software. Below is an example where we ran three different experiments using GPT 3.5, GPT-4, and GPT-4 with a new prompt. You can see the green bar for GPT-4 with the new prompt hallucinated less and answered correctly more often.

![](https://arize.com/wp-content/uploads/2024/11/image1-1-1024x511.png)

### 3. Set Up Guardrails to Protect Performance in Production

Once your application is deployed to customers, you can add a guardrail to protect against bad behavior. For example, where there’s PII within the output, there’s a user frustrated query, or there’s a detected hallucination, you can actually use either code-based, embeddings-based or LLM-based validator to protect against responding to users in production. This is a step that you would add to essentially guarantee some level of protection against returning bad outputs to a user. Then if every time you detect one of these bad responses, you can either ask it to retry, you can send a default response, or you can just block it from responding at all.

![](https://arize.com/wp-content/uploads/2024/11/image11-1-1024x427.png)

We partner with guardrails.ai to offer guardrails based on your data loaded in Arize. You can track guardrails in Arize and audit why a particular response was blocked. Below is an example of a guardrail which blocks against AI application jailbreaks.

![](https://arize.com/wp-content/uploads/2024/11/image4-1-1024x377.png)

### 4. Data Curation to Improve LLM Performance

To improve performance in production, you can use the spans from production usage to expand the robustness of your testing datasets. You can use Arize to find examples of frustrated user queries. You can use embeddings to find points similar to a specific kind of query, such as questions about pricing or queries in a different language.

![](https://arize.com/wp-content/uploads/2024/11/ai_search.gif)

## Conclusion

Building better AI happens across the entire development lifecycle, and we are building tools to help you navigate that. Whether or not you’re just getting started with building production grade applications, we offer tracing, evaluation, datasets and experiments, prompt playground, guardrails, and more to help you measure and improve safety and reliability for your applications.

Try out [Phoenix](http://phoenix.arize.com) if you’d like to get started quickly with our open source offering, which is great for developers early in their journey but also anyone else. Happy building!
