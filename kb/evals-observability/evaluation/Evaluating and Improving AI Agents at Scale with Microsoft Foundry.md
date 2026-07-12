---
title: Evaluating and Improving AI Agents at Scale with Microsoft Foundry
topic: evals-observability
subtopic: evaluation
secondary_topics:
- agents/planning
summary: Guide to evaluating and improving production AI agents at scale with Microsoft
  Foundry and Arize workflows.
source: arize
url: https://arize.com/blog/evaluating-and-improving-ai-agents-at-scale-with-microsoft-foundry/
author: Richard Young
published: '2025-11-18'
fetched: '2026-07-11T04:54:04Z'
classifier: codex
taxonomy_rev: 1
words: 2099
content_sha256: 18115e6c875d7a64bce5a9fff15874e75d787aea32d64b0b8639b65b3c3e2954
---

# Evaluating and Improving AI Agents at Scale with Microsoft Foundry

## The Case for Continuous AI Quality

As generative and agentic systems mature, the question for enterprises is no longer simply “can we build it?” It is “can we trust it?”. Production-ready AI must not only perform, but also behave responsibly. When large-language models generate content, reason across multiple steps, or act through tools, organizations need continuous visibility into what these systems produce, how they respond to edge cases, and whether they remain safe, fair, and compliant.

Historically, evaluation and monitoring were treated as separate phases: data scientists tested models offline, and engineers observed them after deployment. In the new world with LLM’s and non-determinism, this divide no longer works. Today’s AI applications require a new integrated lifecycle that unites observability, evaluation, and experimentation.

Arize AI and Microsoft together provide exactly that. [Microsoft Foundry](https://azure.microsoft.com/en-us/products/ai-foundry) offers a rich library of enterprise-grade evaluation capabilities such as Risk and Safety, while [Arize AX](https://arize.com/generative-ai/) delivers observability, evaluation and experimentation workflows for continuous improvement. Combined, they let organizations close the loop between insight and action, transforming Responsible AI from policy into practice. The result is a continuous feedback system where the same evaluators that power offline testing also monitor live production traffic. Data moves seamlessly from trace logs to evaluation results to experiment dashboards.

## Enterprise Integration Framework

This joint workflow demonstrates the flexibility of open evaluation and observability architectures. Microsoft Foundry brings flexible build and deploy agent capabilities and evaluators, built for enterprise security and compliance; Arize AX’s platform is built for extensibility and improvement workflows. Together, they create an observability and evaluation ecosystem that enables:

- Flexibility to leverage Arize or 3rd party evaluators
- Online evaluations running continuously on production data
- Dataset curation from evaluation labels
- Evaluation driven improvement/experimentation
- Visualization, comparison, and governance reporting
- Near real-time production monitoring/alerting on evaluation and trace metrics

This best-of-breed approach avoids lock-in. Enterprises can adopt new evaluators, models, orchestration frameworks and technical stacks as the landscape evolves, while maintaining a consistent observability foundation. Whether the evaluator, models or agent code come from Microsoft, an open-source model, or an in-house tool, the results flow through the same pipeline and visualization layer.

## Better Together

### About Microsoft Foundry

Microsoft Foundry already offers the widest selection of models of any cloud. It unifies:

- Agent development: Accelerate agent development using popular orchestration frameworks, custom code or Foundry SDK.
- Evaluation: Pre-built evaluators covering three multiple categories: general purpose, textual similarity, RAG quality, safety and security, and agent quality.
- Model catalog: Direct access to foundation models from OpenAI, Meta, Mistral, and other model providers,with consistent APIs.
- Azure Monitor integration: Native cloud monitoring infrastructure that captures OTEL based tracing and GenAI semantic conventions—message roles, token counts, model parameters.
- Content Safety APIs: Enterprise-grade harm detection trained on Microsoft’s scale of data, with severity scoring from 0-7 and detailed reasoning for each flag.
- Deployment: Deploy models and agents on highly performance, scalable and reliable infrastructure for immediate access.

### Arize AX

Arize AX is complementary, offering:

- Universal observability: OpenTelemetry-based trace capture that works with any framework, language and technology stack. Microsoft Foundry, LangChain, LlamaIndex, custom implementations.
- Experimentation: Run systematic A/B tests on datasets before production deployment. Experiment with different prompt versions, model configurations, or evaluation strategies side-by-side.
- Flexible evaluation framework: Plug in any evaluator – Arize’s pre-built ones, Azure’s evaluation libraries, open source tools, or custom domain logic. Arize’s flexible evaluation framework does not limit you.
- Production analytics: Track model quality trends across millions of interactions. Identify degradation patterns before users complain.
- Human feedback loops: Labeling queue and annotation tools to create golden datasets from production data. Capture edge cases, label failures, build regression tests.
- AI assistant (Alyx): Leverage AI on top of trace and evaluation data to conduct analysis, derive insights, debug traces, provide recommendations, optimize prompts and improvement cycles.

## Code and Example Walkthrough: Content Safety Evaluation

In the section below, we’ll demonstrate integration patterns using Azure’s content safety evaluations with sample code from notebook examples. The same architecture applies to any evaluation need: quality, accuracy, compliance, or custom domain metrics.

There are two complementary evaluation paths. The first is dataset-driven, focusing on curated test sets before deployment. The second is trace-driven, analyzing real model responses as they occur in production. Both feed into Arize AX, creating a single pane of glass for AI quality metrics.

*Full code and links to notebooks provided below:*

- Notebook 1: [Trace and evaluate an Microsoft Foundry agen](https://github.com/Arize-ai/tutorials/blob/main/python/llm/agents/Azure%2BArize_observability_evaluations.ipynb)t
- Notebook 2: [Arize AX datasets and experiments workflows](https://github.com/Arize-ai/tutorials/blob/main/python/llm/agents/Azure%2BArize_evaluators-datasets.ipynb)

### Observability — Capturing Model Behavior Through Traces

The journey begins with [observability](https://arize.com/blog/llm-observability-for-ai-agents-and-applications/). Arize AX captures every interaction a model or agent produces prompt, context, response, and tool calls through OpenTelemetry-compatible tracing. For enterprise teams, this trace data forms the foundation of Responsible AI monitoring. Traces and spans are captured through a process called instrumentation.

Code example below shows setting up Arize AX tracing on our sample Langchain agent with just a few lines of code:

```
```
from arize.otel import register
from openinference.instrumentation.langchain import LangChainInstrumentor
# Setup OTel via Arize convenience function
tracer_provider = register(
   space_id=os.environ["ARIZE_SPACE_ID"],
   api_key=os.environ["ARIZE_API_KEY"],
   project_name=os.environ["ARIZE_PROJECT_NAME"],
)
# Instrumentation code
LangChainInstrumentor().instrument(tracer_provider=tracer_provider)

			Next, we create our Microsoft Foundry agent.

The abbreviated code example below shows creating the agent in Microsoft Foundry, invoking the agent. OTEL spans will be generated and sent to Arize AX.

```
```
```
# Initialize Azure AI Foundry Models
from langchain_azure_ai.chat_models import AzureAIChatCompletionsModel
........
# Producer model: Mistral-Large for content generation
producer = AzureAIChatCompletionsModel(
   endpoint=os.environ["AZURE_INFERENCE_ENDPOINT"],
   credential=os.environ["AZURE_INFERENCE_CREDENTIAL"],
   model="Mistral-Large-2411",
)
.........
# Create sub-chains
generate_poem = producer_template | producer | parser
verify_poem = verifier_template | verifier | parser
.........
# Combine into a parallel chain that returns both poem and verification
chain = generate_poem | RunnableParallel(poem=RunnablePassthrough(),
   verification=RunnablePassthrough() | verify_poem
)
.........
# Invoke the chain
response = chain.invoke({"topic": "living in a foreign country"})
```
			Once spans are collected in Arize AX, out of the box observability features such as graph, sankey and trace views provide aggregate and granular level views. All views are fully interactive to promote key visualizations, insights, smart filtering, AI assist to debug and improve your agent.

![](https://arize.com/wp-content/uploads/2025/11/microsoft-foundry-agent-observability-agent-graph.png)

![](https://arize.com/wp-content/uploads/2025/11/arize-ax-alyx-assistant-microsoft-foundry.png)

### Evaluation — Measuring Content Safety with Evaluators in Microsoft Foundry

Evaluation transforms observability into actionable insight. In this example, Microsoft Foundry’s Hate and Unfairness Evaluator analyzes text for both overtly hateful content and subtler forms of bias. It returns a structured result with numerical severity, qualitative labels, and human-readable explanations. Arize AX’s flexible evaluation framework can invoke Azure’s evaluators and receive structured output, attaching them to spans and incorporating them back into the Arize platform. In the Arize AX platform, evals drive the creation of curated datasets and initiate improvement workflows (fine-tuning or prompt optimization).

“Modern AI systems demand integrated visibility across development and production,” says Sebastian Kohlmeier, Principal PM Manager for Foundry Observability at Microsoft. “It’s great to see Arize enabling seamless interoperability with Microsoft Foundry evals to power quality and safety evaluations.”

The abbreviated code example below illustrates how enterprises can integrate this evaluator into trace data (see notebook for full code):

```
```
#Extract spans from Arize
export_client = ArizeExportClient(api_key=os.environ["ARIZE_API_KEY"])
primary_df = export_client.export_model_to_df(
   space_id=os.environ["ARIZE_SPACE_ID"],
   model_id=os.environ["ARIZE_PROJECT_NAME"],
........
#Initialize Azure HateUnfairnessEvaluator
hate_unfairness_eval = HateUnfairnessEvaluator(
   azure_ai_project=os.environ["AZURE_AI_PROJECT"],
   credential=credential,
   threshold=3
)
........
# Run Azure evaluation
   azure_result = hate_unfairness_eval(
   query=input_text[:2000],
   response=output_text[:2000]
)
........
# log_evaluations to Arize
response = arize_client.log_evaluations(
   dataframe=arize_eval_df,
   model_id=os.environ["ARIZE_PROJECT_NAME"]
)

			Each row now carries quantitative safety metrics tied to a specific trace.

Scores above a defined threshold (for example, ≥ 4) trigger a flagged status, allowing immediate filtering to datasets, deriving custom metrics and alerting. After scoring, teams log the combined trace + evaluation dataset back to Arize for visualization and long-term analysis. Within Arize AX, evaluators appear alongside other metrics such as latency, cost, or accuracy.Dashboards display hate/unfairness distributions over time, highlight top offending prompts, and allow trace-level drill-downs. Custom metrics can be derived from evaluations to create executive summary dashboards and proactive monitoring to alert stakeholders when important KPIs start to degrade.

![](https://arize.com/wp-content/uploads/2025/11/arize-ax-microsoft-foundry-trace-unfairness.png)

![](https://arize.com/wp-content/uploads/2025/11/arize-ax-dash.png)

### Experimentation — Iterating and improving with Arize AX Experiments

While trace evaluation provides visibility into production defects, experimentation enables controlled benchmarking of improvement iterations. Arize AX Datasets and Experiments offer a structured way to measure how different models or prompt versions perform on curated regression and golden datasets.

The latest integration lets teams define Azure evaluators as native Arize Evaluator classes, aligning both frameworks under a shared interface. This makes it easy to plug Azure’s safety scoring into repeatable experiments.

The abbreviated code example below illustrates how to setup datasets, tasks, evaluators and experiments in Arize AX to validate improvement runs (see notebook for full code):

```
```
```
# Create a new dataset in Arize -> Regressions from production
dataset_id = arize_client.create_dataset(
   space_id=os.environ["ARIZE_SPACE_ID"],
   dataset_name=DATASET_NAME,
   data=hate_unfairness_dataset
)
# Create agent -> Azure AI Foudry agent
agent = project.agents.create_agent(
   model="o4-mini",
   name="poem-creator-agent",
   instructions="You are an urban poet....."
)
# Define experiment task (prompt,model improvements -> A/B tests)
def task(dataset_row) -> str:
   topic = dataset_row["topic"]
   thread = project.agents.threads.create()
   message = project.agents.messages.create(
.....
   run = project.agents.runs.create_and_process(
       thread_id=thread.id,
       agent_id=agent.id
   )
#Define Evaluator -> Azure Hate and unfairness evaluator
class AzureHateUnfairnessEval(Evaluator):
   def evaluate(
       self, *, output: str, dataset_row: Dict[str, Any], **_:
   ) -> EvaluationResult:
       topic = dataset_row["topic"]
       conversation = {
           "messages": [
               {"role": "user", "content": f"You are an urban poet, your job is to come up with verses based on a given topic. Here is the topic you have been asked to generate a verse on:{topic}"},
               {"role": "assistant", "content": output}
           ]
       }
       azure_result = hate_unfairness_eval(conversation=conversation)
       # Map Azure fields to Arize EvaluationResult format
       return EvaluationResult(
           explanation=azure_result.get("hate_unfairness_reason", ""),
           score=azure_result.get("hate_unfairness_score", 0),
           label=azure_result.get("hate_unfairness", "")
       )
## Run Experiment -> Post results to Arize
arize_client.run_experiment(
  space_id=os.environ["ARIZE_SPACE_ID"],
  dataset_id=dataset_id,
  task=task,
  evaluators=[AzureHateUnfairnessEval()],
  experiment_name="Azure Hate Unfairness Evaluation-3",
)
```
			Once the dataset, task and evaluators are defined, Arize AX Experiments automatically run agent calls against every row in our dataset, capturing and evaluating agent outputs, and aggregating performance statistics. These results are posted back to Arize for visibility, analysis, auditability and reporting. Inside Arize AX UI, teams can compare experiments side by side, perform diff functions, view metrics impacts and drill down into detailed views of experiments.

![](https://arize.com/wp-content/uploads/2025/11/arize-ax-experiment-runs.png)

![](https://arize.com/wp-content/uploads/2025/11/arize-ax-prompts.png)

## Putting It All Together: A Unified Lifecycle

The true power of Microsoft Foundry and Arize emerges when organizations connect features of these two products into a single best of breed solution. In practice, the same evaluator definition can operate across both live and offline contexts. A model might first undergo dataset evaluation during development, then continue being monitored through trace evaluation once deployed. Because both outputs follow the same schema, the metrics align perfectly in Arize dashboards.

This closed loop enables continuous Responsible AI: every model response, experiment result, or safety alert becomes data for the next iteration.

Enterprise teams adopting this pattern typically follow several best practices:

- Use consistent evaluation standards across environments – Define clear cutoffs for what constitutes “flagged” regressions so that testing and monitoring align.
- Leverage domain experts and AI PMs into your workflows – Domain experts and AI PMs should participate in the evaluation development and experimentation cycles.
- Automate evaluations and dataset creation – Automate evaluation processes by configuring Arize evaluators to run on spans continuously. Auto-route route production regressions into curated datasets.
- Combine evaluators for holistic coverage – Risk and safety may be only one dimension, combine it with other evaluators for a broader view of agent quality
- Data-driven improvement – Derive and report evaluation and KPI metrics into visualizations and audit reporting to bridge cross-functional stakeholders – technical, governance and executive teams. Create processes based on data-driven improvement.
 Following these principles turns evaluation into an operational discipline rather than a one-time test.

## Conclusion

Building Responsible AI is a journey that requires more than good intentions, it demands a scalable framework. Observability, evaluation, and experimentation are the three pillars of that framework, ensuring that every model decision is visible, measurable, and improvable.

Microsoft Foundry and Arize AX embody this lifecycle. Observability captures the data; evaluation interprets it through trusted metrics; experimentation turns insights into progress. Using Azure’s content safety evaluators as an example, teams can see how the entire feedback loop functions, from trace export to dataset benchmarking to dashboard insight.

For enterprises, this approach means Responsible AI at scale: automated monitoring, transparent governance, and a culture of continuous learning.

In short, observability tells you what your AI is doing, evaluation tells you how well it aligns with your values, and experimentation justifies how to make it better. Azure and Arize make that cycle seamless, empowering organizations to build AI systems that are not only powerful but principled.

**Resources:**
