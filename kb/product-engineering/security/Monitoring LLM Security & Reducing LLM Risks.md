---
title: Monitoring LLM Security & Reducing LLM Risks
topic: product-engineering
subtopic: security
secondary_topics:
- evals-observability/monitoring
summary: Covers monitoring patterns for LLM security risks such as prompt injection,
  data leakage, and unsafe outputs, with observability as part of the mitigation loop.
source: langfuse
url: https://langfuse.com/blog/2024-06-monitoring-llm-security
author: null
published: '2024-05-14'
fetched: '2026-07-11T04:34:37Z'
classifier: codex
taxonomy_rev: 1
words: 1194
content_sha256: 1d9b96e6dc3514bf2773e49d6245bd004373a730ff72a619c23af40e2aa9125a
---

# Monitoring LLM Security & Reducing LLM Risks

# Monitoring LLM Security in Langfuse

How to use Langfuse to trace, prevent, and evaluate security risks common to LLM-based applications.

![Picture Lydia You](https://langfuse.com/_next/image?url=%2Fimages%2Fpeople%2Flydiayou.jpg&w=96&q=75) Lydia

Lydia![Picture Marc Klingen](https://langfuse.com/_next/image?url=%2Fimages%2Fpeople%2Fmarcklingen.jpg&w=96&q=75) Marc

MarcProtecting against security risks and attacks is becoming increasingly important for ensuring LLM apps are production-ready. Not only do LLM applications need to be secure to protect users' private and sensitive information, they also need ensure a level of quality and safety of responses to maintain product standards.

This post offers an overview of how you can use security tools in conjunction with Langfuse to monitor and protect against common security risks. The [OWASP Top 10](https://owasp.org/www-project-top-10-for-large-language-model-applications/) list is a useful resource on the topic. It provides a consensus of the most critical security risks for LLM applications.

[Introduction](https://langfuse.com#introduction)

In the video below, we walk through an example of how to use the open-source security library LLM Guard, and how to integrate Langfuse to monitor and protect against common security risks.

[How to Monitor LLM Security](https://langfuse.com#how-to-monitor-llm-security)

LLM Security can be addressed with a combination of

- LLM Security libraries for run-time security measures
- Langfuse for the ex-post evaluation of the effectiveness of these measures

[1. Run-time security measures with LLM security libraries](https://langfuse.com#1-run-time-security-measures-with-llm-security-libraries)

There are several popular security libraries that can be used to mitigate security risks in LLM-based applications. These include: [LLM Guard](https://llm-guard.com), [Prompt Armor](https://promptarmor.com), [NeMo Guardrails](https://github.com/NVIDIA/NeMo-Guardrails), [Microsoft Azure AI Content Safety](https://azure.microsoft.com/en-us/products/ai-services/ai-content-safety), [Lakera](https://www.lakera.ai). These libraries help with security measures in the following ways:

- Catching and blocking a potentially harmful or inappropriate prompt before sending to the model
- Redacting sensitive PII before being sending into the model and then un-redacting in the response
- Evaluating prompts and completions on toxicity, relevance, or sensitive material at run-time and blocking the response if necessary

[2. Asynchronous monitoring and evaluation of security measures with Langfuse](https://langfuse.com#2-asynchronous-monitoring-and-evaluation-of-security-measures-with-langfuse)

Use Langfuse [tracing](https://langfuse.com/docs/tracing) to gain visibility and confidence in each step of the security mechanism. These are common workflows:

- **Investigate security issues**by manually inspect traces.
- **Monitor security scores over time**in the Langfuse Dashboard.
- **Evaluate effectiveness of security measures**. Integrating Langfuse- [scores](https://langfuse.com/docs/scores)into your team's workflow can help teams identify which security risks are most prevalent and build more robust tools around those specific issues. There are two main workflows to consider:- [Annotations (in UI)](https://langfuse.com/docs/scores/annotation). If you establish a baseline by annotating a share of production traces, you can compare the security scores returned by the security tools with these annotations.
- [Automated evaluations](https://langfuse.com/docs/scores/model-based-evals). Langfuse's model-based evaluations will run asynchronously and can scan traces for things such as toxicity or sensitivity to flag potential risks and identify any gaps in your LLM security setup. Check out the docs to learn more about how to set up these evaluations.

- **Track latency to balance tradeoffs**. Some LLM security checks need to be awaited before the model can be called, others block the response to the user. Thus they quickly are an essential driver of overall latency of an LLM application. Langfuse can help disect the latencies of these checks within a trace to understand whether the checks are worth the wait.

[Example Workflow: Anonymizing Personally Identifiable Information (PII)](https://langfuse.com#example-workflow-anonymizing-personally-identifiable-information-pii)

We redact and un-redact sensitive information using a security library before and after it is fed into the model. We wrap the whole process with the Langfuse [ observe decorator](https://langfuse.com/docs/sdk/python/decorators) to trace and monitor the security process.

*In the following example below we use the open source library*

[LLM Guard](https://llm-guard.com), an open-source security tool. All examples easily translate to other libraries.Exposing Personally Identifiable Information (PII) to models can pose security and privacy risks, such as violating contractual obligations or regulatory compliance requirements, or mitigating the risks of data leakage or a data breach.

The example below shows a simple application that summarizes a given court transcript. For privacy reasons, the application wants to anonymize PII before the information is fed into the model, and then un-redact the response to produce a coherent summary.

This is a Python example. It works similarly in other languages and can be traced via the Langfuse SDKs or API.

[Install packages](https://langfuse.com#install-packages)

`pip install llm-guard langfuse openai`First, import the security packages and Langfuse tools.

```
from llm_guard.input_scanners import Anonymize
from llm_guard.input_scanners.anonymize_helpers import BERT_LARGE_NER_CONF
from langfuse.openai import openai # OpenAI integration
from langfuse import observe, langfuse
from llm_guard.output_scanners import Deanonymize
from llm_guard.vault import Vault
```
[Anonymize and deanonymize PII and trace with Langfuse](https://langfuse.com#anonymize-and-deanonymize-pii-and-trace-with-langfuse)

We break up each step of the process into its own function so we can track each step separately in Langfuse.

By decorating the functions with `@observe()`, we can trace each step of the process and monitor the risk scores returned by the security tools. This allows us to see how well the security tools are working and whether they are catching the PII as expected.

```
vault = Vault()
@observe()
def anonymize(input: str):
  scanner = Anonymize(vault, preamble="Insert before prompt", allowed_names=["John Doe"], hidden_names=["Test LLC"],
                    recognizer_conf=BERT_LARGE_NER_CONF, language="en")
  sanitized_prompt, is_valid, risk_score = scanner.scan(prompt)
  return sanitized_prompt
@observe()
def deanonymize(sanitized_prompt: str, answer: str):
  scanner = Deanonymize(vault)
  sanitized_model_output, is_valid, risk_score = scanner.scan(sanitized_prompt, answer)
  return sanitized_model_output
```
[Instrument LLM call](https://langfuse.com#instrument-llm-call)

In this example, we use the native OpenAI SDK integration, to instrument the LLM call. Thereby, we can automatically collect token counts, model parameters, and the exact prompt that was sent to the model.

Note: Langfuse [natively integrates](https://langfuse.com/integrations) with a number of frameworks (e.g. LlamaIndex, LangChain, Haystack, ...) and you can easily instrument any LLM via the [SDKs](https://langfuse.com/docs/sdk).

```
@observe()
def summarize_transcript(prompt: str):
  sanitized_prompt = anonymize(prompt)
  answer = openai.chat.completions.create(
        model="gpt-4o",
        max_tokens=100,
        messages=[
          {"role": "system", "content": "Summarize the given court transcript."},
          {"role": "user", "content": sanitized_prompt}
        ],
    ).choices[0].message.content
  sanitized_model_output = deanonymize(sanitized_prompt, answer)
  return sanitized_model_output
```
[Execute the application](https://langfuse.com#execute-the-application)

Run the function. In this example, we input a section of a court transcript. Applications that handle sensitive information will often need to use anonymize and deanonymize functionality to comply with data privacy policies such as HIPAA or GDPR.

```
prompt = """
Plaintiff, Jane Doe, by and through her attorneys, files this complaint
against Defendant, Big Corporation, and alleges upon information and belief,
except for those allegations pertaining to personal knowledge, that on or about
July 15, 2023, at the Defendant's manufacturing facility located at 123 Industrial Way, Springfield, Illinois, Defendant negligently failed to maintain safe working conditions,
leading to Plaintiff suffering severe and permanent injuries. As a direct and proximate
result of Defendant's negligence, Plaintiff has endured significant physical pain, emotional distress, and financial hardship due to medical expenses and loss of income. Plaintiff seeks compensatory damages, punitive damages, and any other relief the Court deems just and proper.
"""
summarize_transcript(prompt)
```
[Inspect trace in Langfuse](https://langfuse.com#inspect-trace-in-langfuse)

In this trace ([public link](https://cloud.langfuse.com/project/cloramnkj0002jz088vzn1ja4/traces/43213866-3038-4706-ae3a-d39e9df459a2)), we can see how the name of the plaintiff is anonymized before being sent to the model, and then un-redacted in the response. We can now evaluate run evaluations in Langfuse to control for the effectiveness of these measures.

[Get Started](https://langfuse.com#get-started)

Run the end-to-end cookbook or check out our documentation.

[About Langfuse](https://langfuse.com#about-langfuse)

[Langfuse](https://langfuse.com/docs) is the open source AI engineering platform. It is used by teams to track and analyze their LLM app in production with regards to quality, cost, and latency across product releases and use cases.

[Feedback / Questions?](https://langfuse.com#feedback--questions)

Join us on [GitHub Discussions](https://langfuse.com/gh-discussions)!
