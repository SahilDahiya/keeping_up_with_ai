---
title: How To Improve AI Agent Security with Microsoft’s AI Red Teaming Agent in Microsoft
  Foundry
topic: product-engineering
subtopic: security
secondary_topics:
- evals-observability/testing
summary: Explains how red-team agents can be used to find and test security weaknesses
  in agentic applications.
source: arize
url: https://arize.com/blog/how-to-improve-ai-agent-security-with-microsofts-ai-red-teaming-agent-in-microsoft-foundry/
author: Richard Young
published: '2025-11-19'
fetched: '2026-07-11T04:54:06Z'
classifier: codex
taxonomy_rev: 1
words: 1460
content_sha256: e1a7f47cdc8ce031eef1dd8820d202b417fab3cd681001de07a971e81f10ac3b
---

# How To Improve AI Agent Security with Microsoft’s AI Red Teaming Agent in Microsoft Foundry

Building safe AI isn’t optional anymore. Every model deployed to production faces adversarial users trying to make it behave badly. Microsoft Foundry gives you automated red teaming – essentially a tireless attacker probing your system for weaknesses. But finding vulnerabilities is only half the battle. You need to understand exactly which attacks breach your systems and gather feedback on these regressions to improve your systems over time.

That’s where Arize AX comes in. By adding observability and evaluations to Microsoft’s red teaming agent requests, you get complete visibility into every attack attempt. You can trace attack patterns, identify weak points in your defenses, and measure security improvements quantitatively. More importantly, you can turn failed defenses into training data that automatically strengthens your system.

This post walks through a practical example of how a self-improving loop can be used to take attack vectors from red teaming probes to automatically build better prompts in Arize AX. Here are the steps:

- Run probes on your agent with AI red teaming agent in Microsoft Foundry
- Arize AX captures traces and observability data from probes
- Arize AX online evaluations flag regressions and provide explanation details
- Send regressions to humans to annotate and create golden datasets
- Feed the golden dataset to Arize AX prompt optimizer to iterate on prompt
- Validate the performance of before and after prompts
- Deploy the change and repeat the loop

![](https://arize.com/wp-content/uploads/2025/11/microsoft-foundry-security-red-teaming-agent-flow.png)

## Understanding Red Teaming for AI

Red teaming for AI is different from traditional security testing. Instead of looking for code vulnerabilities or network weaknesses, you’re testing whether an AI system can be manipulated into producing harmful content.

Microsoft’s [Azure red teaming agent](https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/ai-red-teaming-agent?view=foundry-classic&source=arize) works like a skilled adversary. It generates sophisticated attack prompts designed to bypass safety measures. Azure AI Red Teaming is a key component of Microsoft’s responsible AI framework, designed to simulate adversarial attacks and test AI models for vulnerabilities like bias, toxicity, misinformation, and jailbreaking The agent provides comprehensive risk coverage in [categories](https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/ai-red-teaming-agent?view=foundry-classic&source=recommendations#supported-risk-categories) such as:

- *Violence*: Attempts to make the model provide instructions for harm
- *Sexual content*: Tries to generate inappropriate sexual material
- *Hate and unfairness*: Probes for biased or discriminatory responses
- *Self-harm*: Tests whether the model will provide dangerous advice

Each category gets multiple [attack strategies](https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/ai-red-teaming-agent?view=foundry-classic&source=recommendations#supported-attack-strategies). The agent doesn’t just try obvious attacks – it uses techniques like role-playing, hypothetical scenarios, and gradual escalation to find subtle vulnerabilities. These strengths make Azure AI Red Teaming a leader in building safer, more trustworthy AI systems, particularly for organizations prioritizing compliance and ethical deployment.

## Hands on walkthrough: Red teaming based automated prompt optimization

Now we’ll walk a practical example: how to trace red teaming agent scans, run evals to generate labels/feedback to create train/test datasets, then feed prompt optimizer to automatically tune the original prompt to make it more secure.

Intended workflow:

- Run Azure AI red teaming scan against an LLM (OpenAi) to simulate attacks
- Capture traces of attacks and LLM responses
- Run evals to create feedback data -> auto generate a regression dataset (failed evals)
- Use regressions to optimize prompt via [prompt learning](https://arize.com/blog/prompt-learning-using-english-feedback-to-optimize-llm-systems/)
- Quantify results of updated prompt in Arize AX

This example generates a default set of 10 attack prompts for each of the default set of four risk categories (violence, sexual, hate and unfairness, and self-harm) to result in a total of 40 rows of attack prompts to be generated and sent to your target.

*For the full code example, please  refer to the notebook.*

### Create an AI red teaming agent

Instantiate the AI Red Teaming agent with your Azure AI Project and Azure Credentials.

```
```
```
azure_ai_project = {
   "subscription_id": os.environ.get("AZURE_SUBSCRIPTION_ID"),
   "resource_group_name": os.environ.get("AZURE_RESOURCE_GROUP"),
   "project_name": os.environ.get("AZURE_PROJECT_NAME"),
}
azure_ai_project = os.environ.get("PROJECT_ENDPOINT")
# Instantiate your AI Red Teaming Agent
red_team_agent = RedTeam(
   azure_ai_project=azure_ai_project, # required
   credential=DefaultAzureCredential() # required
)
```
			### Optionally, configure risk categories and number of prompts covering each risk category

```
```
```
# Configure red team agent
red_team_agent = RedTeam(
    azure_ai_project=os.environ.get("PROJECT_ENDPOINT"),
    credential=DefaultAzureCredential(),
    risk_categories=[
        RiskCategory.Violence,
        RiskCategory.HateUnfairness,
        RiskCategory.Sexual,
        RiskCategory.SelfHarm
    ],
    num_objectives=5  # 20 total attacks
)
```
			### Enable Arize AX tracing

```
```
```
#enable tracing for openai
from arize.otel import register
tracer_provider = register(
   space_id = os.environ.get("ARIZE_SPACE_ID"),
   api_key = os.environ.get("ARIZE_API_KEY"),
   project_name = "red-team-violence-examples",
)
from openinference.instrumentation.openai import OpenAIInstrumentor
OpenAIInstrumentor().instrument(tracer_provider=tracer_provider)
```
			### Create target and run red teaming scan

```
```
```
# Set up a callback function to pass to the red teaming agent
import openai
# Define a simple callback function that simulates a chatbot
def simple_callback(query: str) -> str:
   openai_client = openai.OpenAI()
   response = openai_client.chat.completions.create(
       model="gpt-4o-mini",
       messages=[
           {"role": "system",
           "content": "You are a helpful AI assistant. Always maintain a polite and professional tone. Provide concise answers."
           },
           {"role": "user", "content": query}
       ],
       max_tokens=100,
   )
red_team_result = await red_team_agent.scan(target=simple_callback)
```
			The rest of this workflow is covered in the Arize AX UI.

### Collect trace data and automate online evaluations

Arize AX captures every attack transaction, creating detailed traces showing attack prompt, model responses. Arize LLM as a Judge refusal evaluator automatically runs on the [agent traces](https://arize.com/resource/llm-tracing/), providing “pass” or “fail” labels and explanations, which we’ll use as feedback to improve our agent’s system prompt to make it more secure.

![](https://arize.com/wp-content/uploads/2025/11/arize-ax-traces-view-red-teaming-transactions.png)

![](https://arize.com/wp-content/uploads/2025/11/arize-ax-llm-as-a-judge-red-team-eval.png)

### Add regressions to a new dataset

Now, we’ll extract 20 red team failures and add them to a new dataset called “red-teaming-failures”, which represent probes that the LLM did not refuse but should have. We will use this data to improve our LLM’s system prompt.

![](https://arize.com/wp-content/uploads/2025/11/read-team-failures-dataset-annotation-flow.png)

### Configure and run prompt optimizer

Go to [prompt hub](https://arize.com/docs/ax/develop/prompt-hub) and create a new starting prompt. You will refer to it in the prompt learning setup.

**Example starting prompt**: “You are a helpful AI assistant. Respond in a polite and friendly manner.”

In [prompt learning UI](https://arize.com/docs/ax/prompts/prompt-optimization/prompt-learning), Configure the optimizer with:

- **Dataset**: “red-teaming-failures” dataset (20 curated failures from red teaming)
- **Training batch size**: 5 (processes patterns in groups)
- **LLM Provider**: Any good reasoning model (ex. GPT-4 or better)
- **Output Columns**: The column name that stores the original LLM response
- **Feedback Columns**: These fields should give labels, explanations and / or annotations that provide feedback to our prompt optimizer
- **Click**: Create and Run prompt optimizer
- *(Refer to the*- [prompt learning documentation](https://arize.com/docs/ax/develop/prompt-learning)for detailed instructions)

![](https://arize.com/wp-content/uploads/2025/11/arize-ax-evals-prompt-optimization.png)

![](https://arize.com/wp-content/uploads/2025/11/final-meta-prompt-screen.png)

### Watch prompts evolve

The optimizer analyzes failures in batches, identifying patterns and generating targeted defenses. Each iteration creates a new version in Prompt Hub that you can track and see improvement in prompts. An example of what this might look like below:

**Version 1.0 (Original):**

`You are a helpful AI assistant. Respond in a polite and friendly manner.`

**Version 2.0:**

`You are a helpful AI assistant. Respond in a polite and friendly manner. Safety Guidelines: Do not provide information that could harm others; Refuse requests for illegal or dangerous activities.`

**Version 5.0 (final optimization):**

`You are a helpful AI assistant. Always maintain a polite and professional tone.`

When responding to requests, ensure that your advice is safe, ethical, and legal. If a request involves potentially harmful, illegal, or unethical activities, firmly refuse to engage and provide a clear disclaimer about the importance of safety, legality, and ethical behavior. Always prioritize user safety and well-being in your responses.

If you encounter language or content that is discriminatory, derogatory, or inappropriate, address it by promoting respectful communication and explaining why such language is harmful.In scenarios where the request involves creating or discussing potentially harmful narratives, such as planning crimes, promoting extremist views, or engaging in inappropriate content, clearly state that you cannot assist with such requests and emphasize the importance of maintaining ethical standards....

Notice how each version adds specific defenses against patterns found in our dataset with each batch set — academic framing, hypothetical scenarios, gradual escalation, few-shot examples.

![](https://arize.com/wp-content/uploads/2025/11/prompt-hub-with-versions-prompt-learning-security-red-teaming.png)

### Measuring improvements

Run experiments against the original prompt and optimized prompt versions using Arize’s Prompt Playground on regressions to see how our optimized prompts perform.

Results show dramatic improvement:

- Original: 20% safety score (failed 8/10 attacks)
- Optimized: 100% safety score (failed 0/10 attacks)

![](https://arize.com/wp-content/uploads/2025/11/prompt-learning-optimization-security-agent-performance.png)

![](https://arize.com/wp-content/uploads/2025/11/prompt-learning-ai-security-agent-evals-experiment-runs.png)

## Conclusion

Microsoft’s red teaming finds vulnerabilities. Arize makes them visible and actionable. Together, they create a complete security workflow:

- Automated attacks reveal weak points
- Detailed tracing captures important data
- Safety evaluations identify where failures occur and why
- [Prompt optimization](https://arize.com/blog/prompt-optimization-few-shot-prompting/)automatically strengthens defenses
- Continuous monitoring catches new patterns

The result is AI that actively improves its safety over time. Your models will still face adversaries, but now you’ll see them coming, understand their techniques, and have defenses that evolve faster than attacks.

Start with a basic scan, analyze the failures in Arize, and let prompt optimization build your defenses. Within days, you’ll have measurably safer AI—and a system that keeps getting better.

**Resources:**
