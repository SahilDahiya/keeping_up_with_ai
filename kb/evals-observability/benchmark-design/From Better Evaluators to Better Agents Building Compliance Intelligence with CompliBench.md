---
title: 'From Better Evaluators to Better Agents: Building Compliance Intelligence
  with CompliBench'
kind: blog
topic: evals-observability
subtopic: benchmark-design
secondary_topics:
- agents/multi-agent
summary: Introduces CompliBench, a synthetic-data pipeline that uses controllable
  compliance-violation injection and three specialized agents (customer, workflow
  tracker, assistant) to generate 318 labeled multi-turn enterprise conversations
  across airline, healthcare, and insurance domains; finds GPT-5 stays below 50% and
  Gemini reaches only the mid-50% range on conversation-level compliance accuracy
  despite strong per-turn guideline identification.
triage: null
skip_reason: null
source: cresta
url: https://cresta.com/blog/from-better-evaluators-to-better-agents-building-compliance-intelligence-with-complibench
author: Duo Ding
published: '2026-09-16'
fetched: '2026-09-17T06:10:19Z'
classifier: claude
taxonomy_rev: 2
words: 2091
content_sha256: 6197325787624e900f25c6594b213c60934c3e5e7e6784fd0fa830d08e751d33
---

# From Better Evaluators to Better Agents: Building Compliance Intelligence with CompliBench

*How CompliBench can help build the evaluation and training infrastructure for trustworthy enterprise AI agents*

Enterprise AI agents are rapidly moving beyond answering questions. They are beginning to execute complete customer workflows, retrieve enterprise data, call tools, update systems, and make decisions that directly affect customers.

This shift raises a harder question than whether an agent can generate a fluent response:

Can the agent reliably follow the business policies, operating procedures, and compliance requirements that govern every step of the interaction?

Consider an airline customer reporting a damaged wheelchair. A general-purpose model may respond empathetically and explain the claims process. An enterprise agent, however, may be required to transfer the customer immediately to a specialized team. In another workflow, the agent may need to verify identity before discussing an account, provide a required disclosure before taking an action, or escalate the conversation when the customer asks for a human.

In these settings, a plausible final answer is not enough; the agent must follow the correct process.

## Better Agents Need Better Feedback

The long-term goal is to build enterprise agents that can complete complex workflows while consistently following business rules, but reaching that goal requires more than a capable foundation model. It also requires a reliable source of feedback.

A conversation-level success signal is often too coarse. An agent may eventually resolve the customer's request while still skipping an authentication step, collecting the wrong information, or performing actions in the wrong order. A single pass-or-fail label cannot explain critical details, like where the failure happened or which guideline was violated.

What enterprise AI needs is a process-level compliance evaluator. Given a conversation and the relevant business guidelines, this evaluator should be able to determine:

- Which guideline applies at each assistant turn.
- Whether the agent followed that guideline.
- Where a violation occurred when the guideline was not followed.

This evaluator can be viewed as a fine-grained LLM judge, but its role can extend beyond offline benchmarking. It could also serve as a structured reward model for improving the agent itself.

During training, turn-level feedback could provide more precise credit assignment: instead of assigning one reward to an entire conversation, developers could identify the exact point where the agent departed from policy. This supervision could support fine-tuning, preference optimization, reinforcement learning, or other methods for improving business compliance.

During evaluation and auditing, the evaluator could provide more useful information than a single score. It could identify the violated guideline, locate the problematic turn, and distinguish between different types of workflow failure, making the result more actionable for AI engineers, quality teams, and compliance reviewers.

During continuous improvement, newly discovered failures could become regression tests, training examples, or scenarios for evaluating the next version of the agent. Over time, the evaluator could help convert production failures into structured signals for agent improvement.

The challenge is that building such an evaluator requires a large amount of high-quality, process-level compliance data.

## Why Compliance Data Is Difficult to Obtain

Enterprises often have large volumes of real customer conversations. At first glance, these conversations may appear to be an ideal training set, but in practice, using them is difficult for several reasons.

First, real conversations may contain personal information, account details, health information, payment data, and other sensitive content. Internal business guidelines may also contain proprietary operating procedures. Privacy, security, and regulatory requirements can make it difficult to use this data directly for model training, external research, or public benchmarking.

Second, the required annotations are expensive. A useful compliance label is not simply a thumbs-up or thumbs-down judgment. Annotators must understand the relevant business procedures, read the full conversation history, decide which guideline applies at each turn, and identify the exact point where a violation occurs.

Third, compliance failures are often subtle and relatively rare. Obvious mistakes are easy to detect, but the most valuable training examples may involve a delayed escalation, a missing disclosure, a slightly incorrect information request, or a workflow step completed in the wrong order. Collecting enough diverse examples of these edge cases from real traffic is difficult.

These constraints create a fundamental data bottleneck. We need detailed supervision to train a strong compliance evaluator, but producing that supervision manually is costly and difficult to scale.

## CompliBench: A Data Pipeline and a Benchmark

CompliBench was developed to address this bottleneck.

At its core, CompliBench is more than a static benchmark. It introduces a scalable pipeline for generating synthetic enterprise conversations with precise, automatically constructed compliance labels. The resulting data can be used both to evaluate existing LLM judges and to train specialized compliance evaluators.

The benchmark tells us whether current models can reliably audit multi-turn enterprise conversations. The data pipeline provides a path toward building better evaluators when general-purpose models are not reliable enough.

## How the CompliBench Pipeline Works

The pipeline starts from real-world enterprise guidelines in customer service domains such as airlines, healthcare, and insurance. It then generates realistic conversations through three main stages.

### 1. Expanding enterprise guidelines

Enterprise policies include several types of rules, some of which apply universally, such as requirements to protect sensitive information. Others describe workflow-specific procedures, such as the steps required to process a claim. A third category contains conditional rules that become relevant only when a particular event occurs.

CompliBench expands seed guidelines into a broader pool of realistic variations. Iterative filtering removes conflicting or overly similar guidelines. This creates diverse workflows without requiring a separate manually annotated dataset for every organization or use case.

### 2. Injecting controllable compliance violations

The central technical idea is controllable flaw injection.

Instead of asking a model to make random mistakes, the pipeline intentionally modifies selected workflow rules. It may delay a required transfer, skip identity verification, request incorrect customer information, change the order of required steps, or introduce another subtle policy deviation.

The modified guideline is designed to remain plausible. An adversarial refinement process searches for violations that produce a genuine behavioral difference while remaining difficult for an LLM judge to detect.

Because the pipeline controls the modification, it knows exactly which business rule has changed.

### 3. Simulating Complete Multi-Turn Conversations

Multiple specialized agents then generate a complete customer interaction.

One agent simulates the customer, while another tracks the workflow and determines which guideline applies at each point. A third generates the assistant's responses while following either the original guideline or the intentionally modified version.

This design produces precise ground truth automatically. For each assistant turn, the pipeline knows which guideline applies, whether the turn is compliant, and where an injected violation appears.

The result is structured supervision that would otherwise require expensive turn-by-turn annotation by domain experts.

## Evaluating the Evaluator

CompliBench uses the generated conversations to test whether an LLM judge can audit an enterprise agent at the level required for real workflows.

For each assistant turn, the judge must reason over the conversation history, identify the relevant guideline, and determine whether the response follows it. The benchmark measures three complementary capabilities:

- **Strict Guideline Accuracy** measures whether the judge correctly identifies the applicable guideline and the compliance status of a turn.
- **Violation Detection Accuracy** measures whether the judge correctly detects turns that contain violations.
- **Conversation-Level Accuracy** measures whether every turn in the complete conversation is judged correctly.

Conversation-level accuracy is especially demanding; a model may be highly accurate on individual turns but still make at least one mistake during a long interaction. For an enterprise workflow, that single missed violation may be the one that matters most.

## What the Results Tell Us

The CompliBench benchmark contains 318 multi-turn conversations across airline, healthcare, and insurance customer service. The conversations average 16.6 turns and contain approximately 3.7 policy violations each.

The results show that enterprise compliance auditing remains difficult even for strong frontier models.

Models such as GPT-5 and Gemini perform well at identifying relevant guidelines on individual turns. However, their conversation-level accuracy is much lower. GPT-5 remains below 50 percent conversation-level accuracy across the evaluated domains, while Gemini reaches only the mid-50 percent range at its best.

This gap reveals an important limitation: strong general reasoning does not automatically translate into reliable process-level auditing across a complete enterprise workflow.

The specialization result is even more informative. A Qwen3-8B model trained with synthetic supervision from the CompliBench pipeline outperforms much larger general-purpose models on key violation detection and conversation-level metrics. This suggests that task-specific data can matter more than model scale for fine-grained compliance evaluation.

The experiment does not yet demonstrate that this evaluator directly improves the compliance behavior of an agent model. It does, however, establish a critical intermediate result: the data pipeline can produce useful supervision for training a stronger specialized evaluator.

## From Better Evaluators to Better Agents

Once a reliable process-level evaluator is available, it could support several stages of enterprise agent development.

- **Fine-grained agent training.** The evaluator could provide turn-level rewards that identify exactly where the agent violated a guideline. This creates better credit assignment than a single reward at the end of a long conversation.
- **Model and workflow evaluation.** Teams could compare prompts, models, retrieval systems, and orchestration strategies based on whether they follow business policies throughout the full interaction.
- **Automated regression testing.** Every workflow update could be tested against realistic compliance scenarios before deployment. Previously discovered failures could remain in the evaluation suite to ensure that they do not reappear.
- **Post-deployment auditing.** The evaluator could help analyze production conversations, identify the affected policy and turn, and prioritize cases for human review.
- **Continuous agent evolution.** Failures discovered during testing or deployment could become new synthetic scenarios, training examples, and evaluator improvements. This creates a feedback loop in which the evaluation system evolves alongside the agent.

## A Natural Fit for Cresta's Development Lifecycle

For Cresta, this direction aligns with the broader engineering challenge of building AI agents that enterprises can trust with real customer interactions.

Cresta AI Agent is designed to combine conversational reasoning with enterprise knowledge, business workflows, tool use, integrations, and human handoffs. Opera supports the design, testing, benchmarking, and deployment of AI workflows. Conversation Intelligence analyzes customer interactions to identify behaviors, quality signals, and compliance events.

A process-level compliance evaluator could connect these stages more tightly.

Before deployment, it could help test whether a new workflow still satisfies every operating requirement. After deployment, it could help identify where a conversation departed from policy. The resulting failure cases could then inform new tests, training data, and workflow improvements.

CompliBench is not presented as a production integration in these systems today. Rather, it provides the research foundation and data-generation methodology for building this kind of evaluator in the future.

## Closing the Feedback Loop

The broader opportunity is to make compliance evaluation part of the development process rather than exclusively a final audit.

Traditional software engineering relies on unit tests, integration tests, and regression tests after every meaningful change. Enterprise AI needs a similar discipline, but its tests must account for natural language, long conversation histories, conditional policies, and non-deterministic behavior.

A scalable compliance data pipeline can make this possible.

As new workflows are introduced, corresponding synthetic conversations can be generated. As operating procedures change, new compliance scenarios can be added. As edge cases appear in production, they can become permanent regression tests.

The development cycle becomes:

**Deploy → Observe → Evaluate → Improve → Validate → Redeploy**

In this cycle, every detected violation can contribute to a better evaluator and, eventually, a better agent.

## Building Enterprise AI That Can Be Trusted

The next generation of enterprise AI will not be defined only by model size or conversational fluency, but by whether agents can reliably execute the workflows and policies that businesses depend on.

Building those agents requires strong models, but it also requires strong evaluators. Without process-level feedback, developers cannot reliably identify where an agent failed, assign credit during training, or determine whether a new system is safer than the one it replaces.

CompliBench addresses this foundational problem by combining a benchmark with a scalable synthetic data pipeline. The benchmark measures how well current LLM judges detect compliance violations. The pipeline generates the structured supervision needed to train more capable specialized evaluators.

The immediate contribution is better compliance evaluation. The longer-term opportunity is larger: using reliable evaluators as reward models, auditing systems, and continuous feedback mechanisms for building enterprise agents that can be trusted throughout an entire customer journey.

If you want to solve hard problems and turn ambitious ideas into measurable customer impact, [come build the future of human-centric AI with us](https://cresta.com/careers).
