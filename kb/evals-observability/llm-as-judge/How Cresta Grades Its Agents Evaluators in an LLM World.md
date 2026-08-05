---
title: 'How Cresta Grades Its Agents: Evaluators in an LLM World'
kind: blog
topic: evals-observability
subtopic: llm-as-judge
secondary_topics: []
summary: 'Describes Cresta''s LLM-as-judge evaluation system for AI agents: binary,
  transcript-verifiable requirements converted into LLM evaluators, paired with deterministic
  checks (e.g., Tool Match), plus a human-in-the-loop calibration loop and separate
  completeness/accuracy claim-based scoring to distinguish under- and over-claiming.'
triage: null
skip_reason: null
source: cresta
url: https://cresta.com/blog/how-cresta-grades-its-agents-evaluators-in-an-llm-world
author: Lillian Zhao
published: '2026-08-03'
fetched: '2026-08-05T06:52:22Z'
classifier: claude
taxonomy_rev: 2
words: 2099
content_sha256: ec47146761dac47880cf24d1bc0f1aa8ddfaf1cde7524205ff7345ec235866a2
---

# How Cresta Grades Its Agents: Evaluators in an LLM World

**PART 3 | CRESTA'S AI AGENT TESTING & EVALUATIONS APPROACH**

Traditional software testing has a clean evaluation model: given a known input, assert a known output. Pass or fail, unambiguously.

With AI agents, we face a “grader problem”. A customer asks "what's the status of my order?" This can be answered correctly in several ways, and incorrectly in dozens of different ways; therefore, incorrect responses can be wrong in numerous ways across factuality, tonality, and even omission.

[Cresta uses a combination of LLM-as-judge and deterministic checks](https://cresta.com/blog/the-new-world-of-non-deterministic-testing-and-evaluation) to assess two sets of attributes in a conversation:

1. **Trajectory evaluation** judges the agent on*how* it got there — the reasoning steps, tool calls, procedures followed, and decisions along the way.
2. **Final outcome evaluation** judges the agent*only* on what it produced — whether the end result was correct, regardless of the path taken

In [Part 2](https://cresta.com/blog/) of this series, we covered how Cresta builds its test dataset to match production data. Today, in Part 3, we will share how Cresta’s forward-deployed team evaluates its agents at scale, gaining the trust of customers in regulated industries.

## **Context: Simulations at scale**

In order to discuss our evaluators, it’s important to first understand what we are evaluating.

The backbone of non-deterministic testing involves scaling simulations of AI visitors engaging with the customer experience AI agent. Each AI visitor is similar to a real customer - they have an objective, a personality, account information, and even deviations along the standard path. Cresta’s platform suite allows us to auto-convert [production conversation data](https://cresta.com/blog/the-data-comes-first-mining-real-conversations-for-test-coverage) into simulations at scale. 

Simulators reproduce the same conversation dozens of times, in order to understand any non-deterministic variance that will appear. The first line of defense on grading hundreds of thousands of tests cannot be a manual review; this is where evaluators become critical in a LLM world. 

![](https://cdn.prod.website-files.com/67feba4d16c14d85f1696c4f/6a70a8f042eb7caf1d6fd63b_SV%20Results.png)

*The simulated visitor’s conversation in this example is evaluated with both deterministic evaluators (e.g., article match tool) and LLM judges.*

## **The Anatomy of a Test Case**

At its core, every test case consists of two components: the conversation transcript and its evaluators.

The conversation transcript can be produced via various inputs—a manual test, a reproduced real conversation, or a LLM-generated simulation conversation. Evaluators can be tied to a specific test case, or created as global evaluators.

![](https://cdn.prod.website-files.com/67feba4d16c14d85f1696c4f/6a70abd369f3a0c473639c1c_%5BDon%27t%20use%5D%20Cresta%20AIA%20Testing%20and%20Evaluations%20v2.png)

To generate our conversation transcripts, we leverage two key inputs before user-acceptance testing begins:

- [Synthetic customers](https://cresta.com/blog/introducing-synthetic-customers-a-living-model-of-your-customer-base) are generated from your historical conversations to represent both common customers and edge cases. Each synthetic customer auto-generates a test case.
- User-written simulations allow the user to quickly cover happy paths or new features not captured in historical conversations.

*Field example 1:* *In a healthcare deployment, happy path tests validated that the agent could complete standard scheduling flows end to end. However, test cases created from* *Synthetic Customers* *revealed a critical gap: urgency had no impact on system behavior. Inputs indicating immediate need were processed through the same logic as routine requests, resulting in a suboptimal flow.* 

*More broadly, the simulations exposed high-value edge cases around urgency and prioritization, all of which were formalized into a regression test set. The Agent was modified pre-launch with triage capabilities, and the regression test set ensured confidence in the consistent handling of the triage.*

The above field example was able to expose opportunities for improvement even prior to the development of evaluators, as a quick manual review of simulations during prototyping revealed the need to revisit the Agent’s design.

To complete each test case to run at scale without manual grading, we apply a set of custom evaluators, which run deterministic checks & LLM evaluations across the trajectory and outcome of the conversation.

## Requirements as Global Evaluators

The Requirements Adherence List from [Part 2](https://cresta.com/blog/the-data-comes-first-mining-real-conversations-for-test-coverage) isn't just a planning artifact. It’s a direct input to our LLM-based evaluation layer. 

To recap, the Requirements Adherence List is sourced directly from business objectives, brand standards, and compliance obligations. We then convert each business requirement into a LLM evaluator that runs against every test case in the set, serving as a global evaluator set.

Requirements are written to be binary, observable, and verifiable from the transcript alone. The evaluator is given the conversation transcript and a single, precise question: Did the agent satisfy this requirement - yes or no?

That specificity is what makes LLM-as-judge reliable here. For example, a vague requirement (*"the agent should be helpful"*) produces inconsistent verdicts. Meanwhile, a precise one (*"the agent must confirm the appointment date and time before ending the call"*) does not.

Cresta holds every requirement to what the team calls the intern test: could someone with no context, reading only the transcript, reach the same verdict?

*Example requirements from the field:*

- *If the user raised a billing dispute, the agent offered to transfer them to a billing specialist (a general apology or self-service instruction does not count as an offer).*
- *The agent refrained from providing specific financial advice that does not pertain to making a payment to [Company].*
- *If the conversation included the user's personal health data, the agent provided a privacy disclosure before or at the point that data was collected or discussed.*
- *Before ending the conversation, the agent confirmed with the user that their issue was resolved (an unacknowledged assumption of resolution does not count).*

## Local Evaluators for Individual Test Cases

Global requirements cover a lot, but they can't catch everything.

For our local evaluators, we maintain a library of configurable evaluators—deterministic and LLM—

for users to configure. If the signal exists in structured data (tools, variables, actions, retrievals), the user should leverage the corresponding deterministic evaluator. LLM evaluators are used instead when the evidence lives in a conversation transcript, for semantic-based assessments, or when there are multiple correct outputs.

*Field example 4:* *For a health clinic client, a global requirements evaluator checked whether "the agent confirmed the patient's date of birth before sharing account details".*

*Evaluation calibration revealed a high false-negative rate. The agent was confirming the DOB via a tool call—not in its spoken response—which the LLM judge couldn't “see”. The fix was to pair the binary LLM evaluator with a deterministic Tool Match evaluator, and re-write the requirement to reflect what "confirmation" actually meant in terms of standard verbiage & style.*

## **LLM Evaluators in a Nutshell**

Our evaluator library democratizes the know-how of creating evaluations for our customers who choose to self-serve their testing & evaluations process.

We’ve converted the deployment team’s regular needs into configurable evaluators to assess repetition, accuracy & completeness of answers, as well as template prompts to assess tone, style, and process.

Cresta's evaluator suite includes three claim-based variants for assessing the content of individual messages.

- **Completeness:** the agent must include all required claims; missing any claim will cause a fail. However, the agent can share extra information and pass. We use this to verify that the agent said everything it needed to.
- **Accuracy:** the agent must only share from the approved claims list; extra information will cause a fail. Missing some claims is acceptable. We use this when we want to prevent hallucinations or out-of-scope claims.
- **Accuracy & Completeness:** the strictest mode — the agent must say all and only the approved claims. We use this for high-stakes regulated responses where exact content matters.

Together, these three tools decompose what a single semantic-equivalence score used to measure. Instead of one verdict or set of scores on whether the response was "right," our customers are able to receive different signals for under-claiming (the agent told the customer less than it should) versus over-claiming (it asserted things it shouldn't).

For certain regulated industries, these two distinct failure modes represent different risk profiles that a composite score would hide.

### How We Calibrate the Judge

A requirement that seems well-specified at the outset may produce inconsistent verdicts when the LLM Judge encounters unusual phrasing, unexpected conversation structures, or edge cases that the requirements creator didn't anticipate.

Cresta's calibration process allows builders and Customer subject matter experts to address this proactively. After new evaluators are configured, human-in-the-loop comes into play. Reviewers run evaluators against a set of conversation transcripts, create verdicts, and agree or disagree with the LLM's judgment on a case-by-case basis.

*Field example 2:*  *In an e-commerce deployment, variation tests revealed that the agent handled standard return requests correctly but broke on gift-purchase framing — 'I want to return this, I got it as a gift.' The phrasing variant triggered a logic path the happy path hadn't exercised. This was caught offline, before any customer saw it.*

“Disagreements” expose requirements that either need tightening. The calibration loop continues until verdicts stabilize and the team has verified they match their own judgment. Only then are the evaluators promoted to the full test suite.

![](https://cdn.prod.website-files.com/67feba4d16c14d85f1696c4f/6a70aa159b444ee630f071f0_Calibrating%20the%20judge.png)

## **Deterministic Checks, Anchored in Structured Data**

LLM-as-a-judge is a powerful tool and relatively new paradigm. However, it is not the right tool for many tasks, and can often be cost ineffective as well. The greatest mistake we see in training & enablement is the incorrect or overreliant usage of LLM-as-a-judge. Our [Conductor](https://cresta.com/blog/cresta-conductor-the-agent-for-ai-agent-development) builder tool corrects for this by guiding our customers & builders to the appropriate evaluation tools.

Was the correct knowledge base article retrieved? Was the right value collected and stored in the appropriate variable? For those questions, the signal exists in structured data, and therefore deterministic evaluators are most appropriate.

Cresta's suite of deterministic checks covers the core categories of agent behavior that produce verifiable, exact signals.

IMAGE

- **Tool Match** verifies that a specific tool was invoked and/or called with the expected parameters. This evaluator is best for validating API calls, telephony routing metadata, and any other external system interaction.
- **Article Match** confirms that the correct knowledge base article was retrieved before the agent generated its response. A response grounded in the wrong article is a retrieval failure, not a generation failure, and treating it as the latter obscures the actual problem.
- **Variable Match** checks that structured fields were captured correctly: form data, booking parameters, authentication slot values. When the right answer is exact, an LLM judge adds no value over a direct comparison.
- **Action Match** verifies that platform-level actions — transfers, hang-ups, escalations — actually fired. This operates below the tool call layer and catches cases where the agent's intent was correct but the action didn't execute.

*Field example 3:* *In pre-launch testing of a loan servicing agent, the agent passed an evaluator at a 94% rate across all test cases. The LLM requirement evaluator ("the agent must not provide pay-off amounts before authenticating the caller") assessed the transcript and produced a 94% pass rate.*

*When the forward-deployed team added a Tool Match evaluator checking that the authentication tool had actually been called before any account query, the combined pass rate dropped to 71%. The LLM judge had been inferring authentication from conversational context. This deterministic check caught the cases where the tool call never actually fired.*

## Evaluators Are Mix-and-Match

Effective test cases stack multiple evaluators together, each targeting a different dimension of agent behavior.

In creating a test case for a FAQ answer, we might pair an **Article Match evaluator** (*“did the agent pull the right knowledge base article?”*) with a **Completeness LLM evaluator** (*“did the agent's response include all the required claims?”*). This checks for both retrieval and generation accuracy. 

An intent routing test case might layer a **Tool Match** (*“was the transfer tool called?”*), a **Variable Match** (*“was the correct queue specified?”*), and an **Action Match** (*“did the platform-level transfer actually fire?”*). Three evaluators, three distinct failure modes, each caught by the grader best suited to detect it.

Let’s say these are two test cases for the same Agent. Our global Requirements Adherence can evaluate conversation-level conditions that must hold regardless of topic, conversation path, or customer type, so these universal checks don't have to be re-configured case by case.

Our mix-and-match approach to evaluation layers demonstrates the Swiss Cheese model in practice. However, they also highlight the onus placed on evaluation: the graders must be thoughtfully designed and carefully executed to achieve the layers we’ve described.

In this deep-dive, we have covered field examples at length that surfaced in simulation, prior to launch. Not every gap will.

**Up next: Part 4 — Using Production Monitoring to Close the Loop**

Evaluation doesn't end at launch. In Part 4, we cover how Cresta uses production conversation data to continuously update the test suite — converting real failures into regression tests, detecting drift, and keeping the evaluation framework calibrated to the agent's actual operating environment.
