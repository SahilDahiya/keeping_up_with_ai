---
title: 'Arize, Vertex AI API: Evaluation Workflows to Accelerate Generative App Development
  and AI ROI'
topic: evals-observability
subtopic: evaluation
secondary_topics:
- infra-platform/deployment
summary: Describes Arize and Vertex AI API evaluation workflows for accelerating generative
  application development and measuring AI ROI.
source: arize
url: https://arize.com/blog/arize-vertex-ai-api/
author: Gabe Barcelos
published: '2024-11-01'
fetched: '2026-07-11T04:50:26Z'
classifier: codex
taxonomy_rev: 1
words: 1938
content_sha256: f5aca985c0af1b31cecb47b8a37d34b092d063b266cd67d2535352f301c28f4d
---

# Arize, Vertex AI API: Evaluation Workflows to Accelerate Generative App Development and AI ROI

*Written in collaboration with Christian Williams, Principal Architect AI/ML, Google Cloud. *

In the rapidly evolving landscape of artificial intelligence, enterprise AI engineering teams must constantly seek cutting-edge solutions to drive innovation, enhance productivity, and maintain a competitive edge. In leveraging an AI observability and evaluation platform like Arize AI with the advanced capabilities of Google’s suite of AI tools, enterprises looking to push the boundaries of what’s possible with their AI applications have a robust, compelling option.

As a state-of-the-art large language model (LLM) with multi-modal capabilities, Vertex AI API serving Gemini 1.5 Pro offers enterprise teams a powerful model that can be integrated across a wide range of applications and use cases. From improving customer interactions and automating complex processes to enhancing data analysis and decision-making, the potential to transform business operations is significant.

By adopting Vertex AI API for Gemini, enterprise AI teams can:

- **Accelerate development:**Leverage advanced natural language processing and generation capabilities to streamline code development, debugging, and documentation processes.
- **Enhance customer experiences:**Implement sophisticated chatbots and virtual assistants capable of understanding and responding to customer queries across multiple modalities.
- **Boost data analysis:**Utilize the ability to process and interpret various data types, including text, images, and audio, for more comprehensive and insightful data analysis.
- **Improve decision-making:**Harness advanced reasoning capabilities to provide data-driven insights and recommendations to support strategic decision-making.

Teams using the Vertex AI API further gain from implementing a telemetry system, or AI observability and LLM evaluation, as they’re developing generative applications to validate performance and accelerate the iteration cycle. By adopting Arize AI in tandem with their Google AI tools, AI teams can:

- **Help ensure application reliability:**Continuously validate and monitor generative app performance as input data shifts and new use cases arise, to quickly address issues in development and after deployment.
- **Speed development cycles:**Rapidly iterate using pre-production app evaluations and workflows to test and compare the results of various prompt iterations.
- **Implement guardrails for protection:**Systematically test app responses to a wide range of inputs and edge cases to ensure outputs comply in the boundaries of expectations.
- **Make improvements with dynamic data:**Automatically flag low-performing sessions for review and identify challenging or ambiguous examples for further analysis and fine-tuning.
- **Consistent evaluation from development to deployment:**Use Arize’s open-source evaluation solution during development, alongside an enterprise-ready platform as applications become ready for production.

## Solutions to Common Challenges Afflicting AI Engineering Teams

In working with hundreds of AI engineering teams building and deploying generative-powered applications, a common set of challenges emerged:

- **Small changes can lead to performance regressions**– even minor alterations in prompts or underlying data can result in expected degradations. It’s difficult to anticipate or track down these regressions.
- **Hard to discover data for testing and improvement**– identifying edge cases, underrepresented scenarios or high-impact failure modes requires complex data mining techniques to extract meaningful subsets of data.
- **Bad LLM responses can lead to outsized business impact**– a single factually incorrect or inappropriate response can result in legal issues, loss of trust, or financial liabilities.

Arize’s AI observability and evaluation platform enables engineering teams to tackle these challenges head on, building a foundation during the app development phase to carry through to online production observability. Let’s delve deeper into the specific applications and integration strategies for Arize and Vertex AI, and how an enterprise AI engineering team can build better AI using the two solutions together.

![Pillars of LLM observability](https://arize.com/wp-content/uploads/2024/11/1_Pillars_of_LLM_Observability.max-1000x1000-1.png)

## Gain Visibility with LLM Tracing in Development

Arize’s LLM tracing capabilities provides visibility into each call in an LLM-powered system to facilitate application development and troubleshooting. This is especially critical for systems that implement an orchestration or agentic framework, as those abstractions can mask an immense number of distributed system calls that are nearly impossible to debug without programmatic tracing.

With LLM tracing, teams gain a comprehensive understanding of how the Vertex AI API serving Gemini 1.5 Pro processes input data through each layer of the application: query, retriever, embedding, LLM call, synthesis, etc. Traces are available from the session-level down to specific span — e.g., retrieval of an individual document — which let AI engineers pinpoint the exact source of an issue and how it might propagate through the system’s layers.

![LLM tracing with document retrieval](https://arize.com/wp-content/uploads/2024/11/2_LLM_tracing_with_document_retrieval.max-2000x2000-1-1024x555.png)

LLM tracing also surfaces fundamental telemetry data such as token usage and latency in system steps and Vertex AI API calls. This allows for identification of bottlenecks and inefficiencies for further application performance optimization. Instrumenting Arize tracing on apps takes just a few lines of code — traces are collected automatically from over a dozen frameworks such as OpenAI, DSPy, LlamaIndex, and LangChain, or manually set up using the OpenTelemetry Trace API.

## Replay and Fix Issues with Vertex AI in Prompt + Data Playground

Replaying problems and prompt engineering with your application data is an incredibly effective way to improve the outputs of LLM-powered applications. The prompt + data playground in Arize offers an interactive environment for optimizing prompts used with Vertex AI API for Gemini, providing developers real-time feedback into the results using app development data.

Use it to import trace data and explore the impact of changes to prompt templates, input variables, and model parameters. Workflows in Arize allow developers to take a prompt from an app trace of interest and replay scenarios directly in the platform. This is a convenient method to rapidly iterate and test different prompt configurations as new use cases are being deployed, or encountered by Vertex AI API serving Gemini 1.5 Pro once apps are live.

![Prompt data playground using Vertex AI](https://arize.com/wp-content/uploads/2024/11/3_Prompt__Data_Playground_Using_Vertex_AI_.max-2000x2000-1-1024x553.png)

## Validate Performance with Online LLM Evaluation

Once tracing is implemented, Arize helps developers validate performance with a systematic approach to LLM evaluation. The Arize evaluation library is a set of pre-tested evaluation frameworks to score the quality of LLM outputs on specific tasks such as: hallucination, relevance, Q&A on retrieved data, code generation, user frustration, summarization, among many others.

Google customers can use Vertex AI API serving Gemini models to automate and scale evaluation tasks, in a process called Online LLM as a judge. With Online LLM as a judge, developers define the evaluation criteria in a prompt template in Arize and designate Vertex AI API serving Gemini as the evaluator in the platform. As the LLM app runs, the model scores, or evaluates, the outputs generated by the system based on the criteria defined.

![LLM as a Jodge](https://arize.com/wp-content/uploads/2024/11/4_Online_LLM_Evaluation_Method_Using_Verte.max-2000x2000-1-1024x563.png)

Furthermore, Vertex AI API serving Gemini can be used to explain the evaluations generated. In many cases it can be difficult to understand why an LLM responds in a specific way — explanations expose the rationale and can help further improve the accuracy of evaluations downstream.

![](https://arize.com/wp-content/uploads/2024/11/5_LLM_evaluation_with_explanations_generat.max-2000x2000-1-1024x552.png)

Teams greatly gain from employing evaluations while they are actively developing their AI applications, as this serves as an early benchmark for performance to base subsequent iterations and fine-tuning.

## Curate Dynamic Datasets for Experimentation

The ability to curate dynamic datasets in Arize arms developers with a workflow to capture examples of interest — whether high-quality evaluations or edge cases where the LLM struggles to perform — to run experiments and track improvements to their prompts, LLM, or other parts of their application.

Paired with Vertex AI Vector Search, developers can bring together offline and online data streams in a curation process that leverages AI to find similar data points to the ones of interest, curating the examples into a dataset that continues to evolve as the application runs. Developers can automate online tasks in Arize that identify examples of interest as traces are collected to continuously validate performance. Examples can be further augmented manually or with Vertex AI API for Gemini driven labeling and annotation.

![Screenshot Curate dynamic datasets in Arize for experimentation](https://arize.com/wp-content/uploads/2024/11/6_Curate_dynamic_datasets_in_Arize_for_exp.max-2000x2000-1-1024x553.png)

Once a dataset is created, it can be leveraged for experimentation, offering developers workflows to conduct A/B testing against prompt template changes, prompt variable changes, or even validate newly tuned versions of Vertex AI API serving Gemini against specific use cases. This systematic experimentation is vital for identifying the optimal configuration to balance model performance and efficiency, particularly in production environments where response times are critical.

## Safeguard Your Business with Arize and Vertex AI API Serving Gemini

Together, Arize and Google AI can help safeguard your AI from undesirable outcomes for your customers and business. LLM guardrails are essential for real-time safety against malicious attempts like jailbreaks, context management, compliance, and overall user experience.

Arize guardrails can be configured using custom datasets and a fine-tuned Vertex AI Gemini model for the following detections:

- **Embeddings guards:**Uses your examples of “bad” messages to guard against similar inputs based on analysis of cosine distance between embeddings. The benefit of this approach is the continuous iteration on breaks so the guard gets more advanced over time.
- **Few-shot LLM prompt**: With your few-shot examples, the model classifies the input as “pass” or “fail”. This is especially advantageous when you want to define a completely customized guardrail.
- **LLM evaluations:**Uses Vertex AI API serving Gemini to evaluate for PII data, user frustration, hallucination, etc. as trigger. This approach leverages scaled LLM evaluations as its foundation.

![](https://arize.com/wp-content/uploads/2024/11/7_Arize_Guardrails_Using_Vertex_AI_API_ser.max-1100x1100-1-1024x444.png)

Arize guardrails using Vertex API serving Gemini 1.5 Pro for detection.If these detections are flagged in Arize, an immediate corrective action will kick in to protect your application from outputting an undesired response. Developers can specify the remediation to block, retry, or default an answer such as “I cannot answer your query”.

## Your own Arize AI Copilot Powered by Vertex AI API Serving Gemini 1.5 Pro

To further streamline the AI observability and evaluation process, developers can leverage Arize AI Copilot, powered by Vertex AI API serving Gemini. This in-platform assistant streamlines the workflows for AI teams, automating tasks and analysis to lighten the daily operational effort for team members.

With Arize Copilot, engineers can:

- **Initiate AI Search with Vertex AI API serving Gemini**– find specific examples such as “angry responses” or “frustrated user inquiries” to add to a dataset.
- **Perform quick actions and analysis**– configure monitors for dashboards or ask questions about your models and data.
- **Automate a task**– define and build LLM evaluations.
- **Prompt engineering**– ask Vertex AI API serving Gemini to generate prompt playground iterations for you.

![](https://arize.com/wp-content/uploads/2024/11/8_Arize_Copilot_utilizing_the_Vertex_AI_AP.max-2000x2000-1-1024x610.png)

Arize Copilot utilizing the Vertex AI API serving Gemini 1.5 Pro.

## Accelerating AI Innovation with Arize and Vertex AI

As enterprises push the boundaries of AI, the integration of Arize AI with Vertex AI API serving Gemini offers a compelling solution for optimizing and safeguarding generative applications. By leveraging Arize’s observability and evaluation platform and Google’s advanced LLM capabilities, AI teams can streamline development, enhance application performance, and help ensure reliability from development to deployment.

Whether it’s through dynamic dataset curation, real-time guardrails, or the automated workflows of Arize AI Copilot, these tools work in harmony to accelerate innovation and drive meaningful business outcomes. As you continue to develop and scale AI applications, Arize and Vertex AI API serving Gemini models provide the critical infrastructure to navigate the complexities of modern AI engineering, so your projects remain efficient, resilient, and impactful.

To get started with tracing and evaluation for your Google-powered AI applications, visit [Arize’s product documentation here](https://docs.arize.com/arize/llm-tracing/tracing-integrations-auto/vertex-ai-gemini). Or [try out this Colab](https://colab.research.google.com/github/Arize-ai/phoenix/blob/main/tutorials/tracing/langchain_vertex_ai_tracing_tutorial.ipynb) to visualize how the tools work together to help accelerate your AI development journey.

Want to simplify your AI observability even further? You can find [Arize on Google Cloud Marketplace](https://console.cloud.google.com/marketplace/product/arize/arize-ai?pli=1)! This integration makes it easier than ever to deploy Arize and monitor the performance of your production models. Visit the Arize listing on Google Cloud Marketplace today to learn more and get started.
