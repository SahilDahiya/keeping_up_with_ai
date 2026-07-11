---
title: Arize AI Brings LLM Evaluation, Observability To Microsoft Azure AI Model Catalog
topic: infra-platform
subtopic: deployment
secondary_topics:
- evals-observability/evaluation
summary: Describes Arize integration with Microsoft Azure AI Model Catalog for LLM
  evaluation and observability in Azure-hosted development workflows.
source: arize
url: https://arize.com/blog/arize-ai-brings-llm-evaluation-observability-to-microsoft-azure-ai-studio/
author: Jason Lopatecki
published: '2024-05-21'
fetched: '2026-07-11T04:48:46Z'
classifier: codex
taxonomy_rev: 1
words: 1592
content_sha256: afa2d23eb91614cd79d14c6f243f352bd648d58e4ea2a3db144c6abe6fc8edbc
---

# Arize AI Brings LLM Evaluation, Observability To Microsoft Azure AI Model Catalog

Generative AI is reshaping the modern enterprise. According to a recent survey, over half (61%) of developers say they plan to deploy LLM applications into production in the next 12 months or “as soon as possible.”

However, challenges remain in getting a generative application from toy to production – and staying there. This week at Microsoft Build, Arize AI is rolling out a deepened partnership and integration with Microsoft Azure to help AI engineers speed the reliable deployment of LLM applications.

## Microsoft Azure Model-as-a-Service

Many Fortune 500 airlines, financial services firms, retailers, technology companies, and others rely on Azure along with Arize for robust ML and LLM observability.

For these users, Azure AI model catalog provides a great starting point. Featuring popular open source models curated by Azure AI – including from Azure Open AI Service, Meta, Mistral, Cohere, and others – the catalog leverages a partnership with Hugging Face to offer thousands of OSS models for inference.

Critically, Azure AI model catalog offers several pay-as-you-go inference APIs through Models- as-a-Service (MaaS). With Azure managing the infrastructure and GPU and users accessing a curated set of models – including Llama 3, Mistral Large, Cohere Command R/R+ and Embed models – via a pay-as-you-go API with billing based on tokens for LLMs, users can do hosted fine-tuning without provisioning GPUs and integrate seamlessly with LLMOps tools like prompt flow, LlamaIndex, and Arize – ultimately getting to production sooner.

With MaaS available on these GenAI development platforms, now developers can continue using their preferred tools to build GenAI apps while leveraging enterprise grade pay-as-you-go APIs. These APIs are subject to [Azure’s data, privacy, and security commitments](https://learn.microsoft.com/en-us/azure/ai-studio/how-to/concept-data-privacy), ensuring Microsoft does not share your data with third parties without your permission. Your data, including the data generated through your organization’s use of Models as a Service on Azure – such as prompts and responses – are kept private and are not disclosed to third parties.

## Azure Model As a Service Integration with Arize

Arize has integrated the Azure AI Model as a Service into the Arize LLM evaluation and observability platform. By offering access to a curated set of easy-to-use hosted models like Llama 3 and Mistral Large as a service, Azure is making it faster to build generative AI applications than ever. Through a seamless integration with Arize AI — which offers a leading platform for LLM evaluation, tracing, and observability — AI engineers and developers using [Azure AI Studio](https://ai.azure.com/) can ensure enterprise grade deployments of sophisticated LLM systems.

![azure model as a service in arize observability platform](https://arize.com/wp-content/uploads/2024/05/azure-model-as-a-service-in-arize.png)


## The Need for Better LLM Evaluation and Observability

Given the wealth of models available and variation in performance, the need for objective [evaluation for specialized tasks](https://arize.com/blog-course/llm-evaluation-the-definitive-guide/) and use cases as well as observability to detect and troubleshoot issues once an LLM app is in production becomes paramount. This is often easier said than done given how complex it is to select the right model and get applications working with use cases like retrieval augmented generation (RAG), co-pilots, or agents.

![llm app development flow](https://arize.com/wp-content/uploads/2024/05/large-language-model-application-pain-points.png)

RAG deployments include a complex set of technology that is required to work together in order to connect private customer data to LLM generative models. The problems that occur as this technology is deployed into the real world can be hard for teams to troubleshoot. These include Incorrect retrieval, hallucinations on private data, incomplete context chunks causing incomplete answers, and questions with no context data to answer.

Complex AI systems like these require world-class technology solutions for observability and analysis. Paired with the high visibility of these initiatives in executive suites, there is little room for error or mistakes that snowball into PR issues. In short, the need for LLM observability is an imperative to any team deploying LLMs in their applications or services.

![llm tracing in arize ai](https://arize.com/wp-content/uploads/2024/05/arize-ai-llm-tracing-observability.png)

## Arize AI Provides LLM Evaluation and Observability Across the Emerging Stack

Arize AI is deepening its collaboration with Azure AI Studio to help teams objectively evaluate LLM apps, working backwards from the output to pinpoint where exactly an issue is stemming from across an LLM stack.

![phoenix arize lifecycle](https://arize.com/wp-content/uploads/2024/05/phoenix-arize-lifecycle.png)

For LLM evaluation, Phoenix – [an open source library from Arize](https://docs.arize.com/phoenix) – offers simple, fast, and accurate LLM-based evaluations for a variety of tasks including code generation, context relevance, hallucination, Q&A correctness, summarization, and toxicity. All evaluation templates are tested against golden datasets that are available as part of the LLM eval library’s benchmarked datasets and target precision at 70-90% and F1 at 70-85%.

![](https://arize.com/wp-content/uploads/2024/05/arize-observability.png)

Arize’s platform also offers tools for collecting evaluation data, troubleshooting search and retrieval, and tracing to see where an LLM app chain fails.

## Arize AI: LLM Observability for Azure

Arize AI’s observability platform features native support for Azure customers leveraging Azure AI Studio, offering complete visibility into every layer of an LLM-based software system: the application, the prompt, and the response. Through the lightweight integration, teams can easily enable AI observability for any LLM or ML-powered application built on top of Azure’s stack.

Arize AI’s joint offering with Azure covers the [five pillars of LLM observability](https://arize.com/blog-course/large-language-model-monitoring-observability/#five-pillars):

- **LLM Evaluation**: the Phoenix open source framework allows robust, fast LLM-as-a-judge evaluations underpinning the AI technology of Azure.
- **Retrieval Augmented Generation (RAG)**: Arize’s troubleshooting solutions combined with Azure AI Studio create a powerhouse for using private data to create more robust LLM applications powered by your own data.
- **LLM Traces and Spans**: with agent tracing and spans, teams can understand what calls failed, or where in the span issues occurred.
- **Prompt Engineering**: Azure AI model catalog is easily integrated with Arize’s Prompt Playground, enabling teams to improve prompt templates and iterate in real-time, verifying results.

**Fine-Tuning**: curate golden datasets using Arize tools, with integrations back to Azure AI Studio for fine tuning.

![](https://arize.com/wp-content/uploads/2024/05/pillars-llm-observability.png)

## LLM Traces and Spans

In a deployed chatbot application, every conversation thread creates a large set of traces and spans that include calls to LLMs and vector retrieval systems. These are critical to debugging any LLM application. The simplified example below shows calls to retrievers, embeddings, tools, chains, and more. Each span does a specific job, and troubleshooting each span type requires specific types of evaluations.

![](https://arize.com/wp-content/uploads/2024/05/traces-viz.png)

The traces are first collected using instrumentation. The instrumentation options include auto-instrumentation for frameworks like LlamaIndex,and DSPy. In the case of manual instrumentation, OTEL instrumentation is supported using standard interfaces along with PythonSDK dataframe based instrumentation.

![](https://arize.com/wp-content/uploads/2024/05/ways-send-data-arize.png)

Each span powering a chatbot interaction can be visualized and analyzed with Phoenix OSS and persisted to Azure when you are in the development phase. As the application approaches production, you can seamlessly graduate to Arize’s SaaS platform (or deploy on VPC) for always-on monitoring and troubleshooting to automatically monitor for problematic spans.

![](https://arize.com/wp-content/uploads/2024/05/poor-retrieval-troubleshooting.png)

## Evaluations: LLM As a Judge

The foremost way in which teams evaluate LLMs at scale is by using an approach called LLM as a judge. The Phoenix open-source evaluation library developed by the Arize team is designed to run LLM as a judge at scale, in parallel, across lots of data – providing high quality, pre-tested templates for analysis. Azure customers can set any model from Azure AI model catalog as the evaluation LLM.

![](https://arize.com/wp-content/uploads/2024/05/llm-as-judge-visual-azure.png)

The eval library comes enabled with pre-set eval templates for specific tasks such as RAG relevance, Q&A, and hallucination detection:

![](https://arize.com/wp-content/uploads/2024/05/pre-tested-evals.png)

The Arize LLM library is designed to be fast, using parallel calls with evals run over large datasets utilizing models from Azure AI model catalog or Azure OpenAI Service. The library supports explanations and uses async calls with concurrency. The following features are supported across Azure AI Studio:

- Fast, customizable parallelization of LLM calls
- Explanations for all eval results
- Bring your own eval with custom eval support
- Pre-tested evals for toxicity, human vs AI, relevance, Q&A, citation link checks, and retrieval relevance
- Context window overflow

## RAG: Retrieval Troubleshooting

RAG is the key component in connecting companies’ private data to LLMs to create AI applications. Making RAG work consistently and at scale is critical to building LLM-powered applications that are differentiated for your products and services.

Arize helps you identify several critical issues can emerge during the retrieval process, namely:

- Lack of content similar to the query in question
- Lack of relevant content in your vector database
- LLM hallucinates in the response

![](https://arize.com/wp-content/uploads/2024/05/search-retrieval-problems.png)

The Arize platform helps detect clusters of problems, determine why those clusters have retrieval problems, and sort those clusters based on evaluation metrics.

![](https://arize.com/wp-content/uploads/2024/05/retrieval-troubleshooting-workflow-umap.png)

Arize has RAG troubleshooting flows that allow teams to visualize both the embeddings of chunks and the embeddings of queries to your application. These workflows enable teams powerful debugging capabilities to pinpoint problematic groups of queries in RAG systems. The RAG troubleshooting workflows include:

- Prompt and chunk embedding analysis
- Clusters of query performance sorted by evals
- Relevance evals, Q&A evals, citation link correctness evals, and AI vs human evals
- Eval monitoring and generation
- Explanation on retrieval evals

The Azure AI Studio and Arize suite of tools allow teams to go from benchmarking to production deployment analysis of retrieval results, narrowing down retrieval problems in minutes.

## Navigating a New Era of Generative AI with Azure and Arize AI

In addition to the push-button data integration, the Arize platform has multiple integration points with Azure.

The combination of foundation models offered as Model as a Service via Azure AI model catalog and LLM troubleshooting with Arize provides customers a powerful suite for evaluating models and debugging production deployments.
