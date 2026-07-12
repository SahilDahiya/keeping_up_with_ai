---
title: 'EU AI Act Compliance: What AI Engineering Teams Should Monitor'
topic: product-engineering
subtopic: security
secondary_topics:
- evals-observability/monitoring
summary: Explains what AI engineering teams should monitor for EU AI Act compliance,
  connecting regulation to observability and operational controls.
source: arize
url: https://arize.com/blog/eu-ai-act-compliance-what-ai-engineering-teams-should-monitor/
author: Hakan Tekgul
published: '2025-12-22'
fetched: '2026-07-11T04:54:18Z'
classifier: codex
taxonomy_rev: 1
words: 1291
content_sha256: 8557ce82b917961df389691083cb6b0bdf355e5dd8a776b8acdf4730e2cbd931
---

# EU AI Act Compliance: What AI Engineering Teams Should Monitor

The EU AI Act is no longer a distant regulatory concept; it is in force and enterprises are road testing their real-world implementation. The core law is Regulation (EU) 2024/1689, and the full legal text is available on [EUR-Lex](https://eur-lex.europa.eu/eli/reg/2024/1689/oj).

The Act went into effect in August 2024, with different obligations phasing in over the next few years like bans on “unacceptable risk” systems, transparency duties for general-purpose AI, and stringent requirements for high-risk AI, including risk management, data governance, and post-market monitoring.

## Why EU AI Act Compliance Rests on AI Engineering and Product Teams

This is not just a legal or policy problem. Compliance depends heavily on what AI engineers, data scientists, and product teams actually build: how systems are architected, how they are evaluated and tested, which safeguards and guardrails are in place, what data is logged, and how issues are monitored and remediated over time. Legal teams can define what needs to be true; engineering and product teams make it true in code, pipelines, and dashboards.

### Key EU AI Act Dates Teams Should Have on Their Radar

The European Parliament’s briefing on the AI Act timeline is a helpful reference for how enforcement ramps up. At a high level, teams building AI agents and related systems should keep three anchor dates in mind (and verify against the latest EU guidance and implementing acts):

- **1 August 2024**: Act in force: The EU AI Act formally entered into force, starting the phased transition toward full application.
- **2 August 2025**: Key governance and transparency obligations begin for providers of general-purpose AI (GPAI) models, alongside supporting enforcement infrastructure and guidance on prohibited AI and core definitions.
- **2 August 2026**: General date of application: Most of the AI Act, including most obligations for high-risk AI systems, becomes applicable, with some legacy deadlines extending into 2027.

## What To Monitor for EU Act Compliance

What follows is a concrete walkthrough of how you can use AI-driven evaluations and observability to monitor EU AI Act compliance across your GenAI and AI agent applications.

## How To Build an EU AI Act Compliance Dashboard

To operationalize EU AI Act compliance, you need to translate regulatory obligations into measurable metrics and dashboards that track compliance posture across your AI use cases.

When you look at the definition of EU AI Act compliance, there are specific metrics you need to focus on in order to have one compliance score overall across all your AI use cases. Some of these key dimensions include transparency and user disclosure, safety and safeguards, data governance, factuality, bias and fairness, and change management.

In a system like Arize AX, you can create different EU AI Act compliance dashboards in order to have a compliance score for each use case in your organization. For example, you might have a compliance score that is an aggregated metric of all your different evaluations in a particular agentic application. On top of that, you can monitor concrete indicators such as the total number of non-compliant users in a given week.

The first view gives you the ability to see your current compliance posture over time. From there, you can dig deeper into specific compliance metrics as needed.

### Mapping EU AI Act Chapters to Concrete Metrics

A crucial step is mapping the different chapters and requirements of the EU AI Act into specific metrics that you can compute and monitor.

For example, for transparency obligations and general-purpose AI models with specific human oversight, you can define and monitor metrics such as blocked malicious attempts, unique user count over time, the number of compliance incidents, and the top questions being asked to the agent. This mapping lets you connect high-level policy language directly to observable, quantitative signals in your system.

![example of an ai engineer european union ai act dashboard for compliance](https://arize.com/wp-content/uploads/2025/12/eu-ai-act-compliance-dashboard-example.png)

### Transparency, User Disclosure, and Human Oversight

One part of the dashboard focuses on transparency and user disclosure.

Here, you track how users interact with the agent and how well the system honors transparency and oversight requirements. You can monitor blocked malicious attempts and unique user count over time. You can also keep an eye on compliance incidents and the top questions to the agent.

This gives you a clear picture of where transparency obligations intersect with real user behavior, and how patterns in user questions or malicious attempts relate to overall compliance posture.

![](https://arize.com/wp-content/uploads/2025/12/unique-users-transparency-disclosure-metrics-eu-ai-act.png)

### Safety and Safeguards for Higher-Risk AI Systems

![](https://arize.com/wp-content/uploads/2025/12/jailbreak-attempts-harmful-output-over-time-eu-ai-act-chapter-three-requirement-examples.png)

When it comes to higher-risk AI systems, safety and safeguards are central concerns.

In the safety and safeguards section of the dashboard, you can monitor jailbreak attempts, harmful output rate over time, and any toxic content produced by your models. These metrics are tracked over time, and you can set up alerts if something goes wrong as part of the safety and safeguards monitor.

If you see a spike in jailbreak attempts or harmful outputs, you immediately have a signal that something has changed: either in user behavior or in the system itself—and you can investigate before it turns into a broader incident or a regulatory issue.

### Bias, Fairness, and Equality

![](https://arize.com/wp-content/uploads/2025/12/eu-ai-act-bias-fairness-gender-bias-pii-leakage.png)

Another critical dimension is bias, fairness, and equality.

In some use cases, particular forms of bias (i.e. gender bias) are especially important to monitor. Using AI-based evaluations and automated evaluation features, you can check for gender bias and track it over time. This helps you see whether certain groups are receiving systematically different responses or outcomes, and whether your mitigation strategies are working.

By treating bias and fairness as ongoing metrics rather than one-time checks, you can build an auditable history of how your systems behave and improve.

### Data Governance and Privacy

Data governance and privacy are also fundamental pillars of EU AI Act compliance.

Within the data governance and privacy section of the dashboard, you can monitor for any leaks of personally identifiable information (PII) or protected health information (PHI), as well as PII leakage over time. When evaluations detect that the model output contains sensitive information, those events are tracked as part of your compliance monitoring.

This allows you to demonstrate that you are actively tracking data leakage risk across your GenAI and agentic applications and that you have the ability to detect and respond to issues when they appear.

### Factuality and Groundedness

![](https://arize.com/wp-content/uploads/2025/12/eu-ai-act-chapter-ix-factuality-examples-dashboard.png)

For applications that use context from a wide range of sources—such as retrieval-augmented generation or complex agentic workflows—factuality and groundedness are key.

In this part of the dashboard, you can [check for hallucination](https://arize.com/llm-hallucination-examples/) and correctness across your applications. Evaluations assess whether responses are grounded in the retrieved context or knowledge base and whether they are factually correct.

By monitoring hallucination and correctness as first-class metrics, you align EU AI Act expectations around accuracy and reliability with concrete, trackable signals in your observability stack.

### Rolling Everything Up into a Single Compliance Score

All of these metrics – transparency and user disclosure, safety and safeguards, data governance, factuality, bias and fairness, and change management – can be collected into a single, high-level compliance score.

The dashboard aggregates these evaluations to create a compliance score at the top for each GenAI or agentic use case. You can see how that score evolves over time, drill into the underlying metrics that drive changes, and correlate shifts with specific model updates, prompt changes, retrieval updates, or workflow modifications.

In the end, this approach gives you the ability to monitor any metrics you care about from a compliance perspective. Specifically for the EU AI Act, it provides a way to map the different chapters of the Act into concrete metrics that you can use to evaluate all your GenAI and agentic use cases and measure how your compliance posture changes over time.
