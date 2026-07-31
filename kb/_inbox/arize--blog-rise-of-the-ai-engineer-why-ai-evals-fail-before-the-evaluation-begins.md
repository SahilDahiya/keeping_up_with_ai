---
title: Hamel Husain explains why AI evals fail before the evaluation begins
kind: blog
topic: null
subtopic: null
secondary_topics: []
summary: null
triage: null
skip_reason: null
source: arize
url: https://arize.com/blog/rise-of-the-ai-engineer-why-ai-evals-fail-before-the-evaluation-begins/
author: Sara Verdi
published: '2026-07-30'
fetched: '2026-07-31T06:58:20Z'
classifier: null
taxonomy_rev: 2
words: 1377
content_sha256: 4d7a7b7b2e7126dfad1e61c4a41f87800e108791175e09408eb1521765efa542
---

# Hamel Husain explains why AI evals fail before the evaluation begins

Most [AI evaluations](https://arize.com/glossary/ai-evaluation/) are answering the wrong question before they begin.

Hamel Husain sees this enough: a team arrives at an eval review with a dataset, a set of metrics, and a dashboard ready for inspection. He looks at the product and stops them.

“I get into eval reviews all the time where it’s really obvious that the product is not built correctly,” he says. “Stop. This is a product issue.”

That interruption exposes a common mistake in AI development. Teams treat every weak output as a model failure, even when the product never collected the context the model needed, or the [evaluation criteria](https://arize.com/blog/ai-agent-evaluation-how-to-build-evals-you-can-trust/) were never clearly defined. A score can measure the final response while hiding the system decision that produced it.

In the second installment of ** Rise of the Agent Engineer**, Arize’s series on the builders turning agents from demos into production systems, Husain explains why 

[useful evals](https://arize.com/resources/why-do-you-need-evals-for-ai-agents/)begin with product design, close inspection of

[real traces](https://arize.com/glossary/llm-tracing/), and direct participation from

[domain experts](https://arize.com/blog/ai-evals-are-a-data-science-problem-what-most-teams-get-wrong/).

**Ambiguous user queries can create misleading eval results**

One of the most common failures Husain encounters is query disambiguation. A user makes a request that could be interpreted several ways, and the application passes it directly to the model without collecting enough information to resolve the ambiguity.

“A really common way that the model is not the problem is query disambiguation,” Husain says. “The LLM doesn’t have a chance because the user is asking a very ambiguous question and isn’t providing enough context.”

Consider a coding agent asked to “clean up the authentication service.” Before making a safe change, the agent may need to know whether it can alter the public API, introduce a dependency, modify the database schema, or change existing error behavior.

When the application fails to collect those constraints, the model has to guess. An evaluator may later penalize the patch, although the original failure occurred in the product interface.

[Agent engineers](https://arize.com/resources/what-is-ai-engineering/) should treat ambiguity handling as part of the system design. Depending on the application, that may involve:

- Asking a targeted follow-up question.
- Requiring structured fields before execution.
- Retrieving relevant permissions or account context.
- Confirming the intended action before a consequential tool call.

The trace should preserve both the original request and the clarified intent. That gives evaluators enough context to determine whether the agent behaved reasonably given the information it received.

**AI evaluation criteria change as teams see the product in action**

Even when an agent receives adequate context, the team may still be discovering what success means.

Husain calls this ** criteria drift**. “You don’t really know what you want until you see it in action,” he says. “You can only specify a certain amount up front. You have to react to what is happening.”

Generative products expose requirements that may never appear in an initial specification. A support agent can provide an accurate answer while making a promise the company cannot keep. A research agent can cite its claims while presenting evidence in a way that reviewers cannot audit. A coding agent can complete the requested task while producing a patch that maintainers would reject.

Those outputs teach the team something new about quality. Evaluation criteria should evolve as that understanding becomes sharper.

Developers can make those changes easier to interpret by treating eval criteria as versioned product artifacts. Each criterion should have a narrow definition, examples of acceptable and unacceptable behavior, an owner, and a record of why it changed.

Without that lineage, a score may move because the model improved, the application changed, traffic shifted, or reviewers began applying a different standard. Versioned criteria help teams distinguish among those causes.

**Generic AI eval metrics rarely capture the failures that matter most**

Many teams begin with [broad metrics](https://arize.com/resources/agent-evaluation-metrics/) such as correctness, relevance, groundedness, coherence, or helpfulness. These measures can provide a coarse signal, but their generality limits their diagnostic value. For example, a scheduling agent can produce a relevant response while selecting the wrong timezone. A coding agent can generate a correct patch while modifying files outside its authorized scope. A support agent can answer the customer’s question while omitting a required disclosure.

General metrics may miss each of these failures because the behavior that matters depends on the product. The most useful criteria usually emerge from [error analysis](https://arize.com/glossary/error-analysis/), where teams inspect real examples and identify recurring patterns.

“The magic to find what’s most important and really do anything with evals is to look at the data,” Husain says.

That inspection should include more than the final answer. Reviewers may need to see the original request, clarification turns, retrieved context, tool calls, intermediate decisions, final action, and relevant product or model versions.

During the first pass, teams should describe failures in concrete language. A label such as “bad response” gives developers little direction. A label that reads, “called the write tool before receiving approval.” points toward a specific product or engineering change.

Once a pattern appears repeatedly, the team can turn it into a scoped [evaluation criterion](https://arize.com/resources/llm-evaluation/) and measure how often it occurs. A practical loop looks like this:

- Sample representative [production traces](https://arize.com/blog/how-to-evaluate-and-optimize-agent-skills-with-tracing-and-evals/).
- Review them with developers and domain experts.
- Name recurring failure patterns.
- Determine which system layer caused each failure.
- Convert the most consequential patterns into eval cases.
- Make a targeted change and inspect the resulting traces again.

First, qualitative review provides the vocabulary. Then quantitative evaluation shows how common each failure is and whether an intervention reduced it.

**Domain experts need a better interface for reviewing agent traces**

Developers are essential to error analysis because they can identify broken tool calls, missing context, retrieval problems, and infrastructure failures. Plus, product-specific mistakes often require deeper subject-matter knowledge, e.g., a security engineer may notice that an apparently successful action violated policy, a support leader may recognize language that creates an expectation the company cannot meet, and a financial analyst may spot a calculation that uses valid numbers but applies the wrong accounting logic.

“It’s okay to have developers in the loop,” Husain says. “What you want to do is try to get the domain expert as fast as possible to be doing the error analysis.”

That becomes difficult when reviewers receive raw trace data or a spreadsheet containing disconnected inputs and outputs, though. The time required to reconstruct each run slows the process and reduces the number of examples a domain expert can inspect.

A useful [review interface](https://arize.com/resources/ai-agent-tracing-evaluation/) should place the relevant context in one view:

- The user’s request and clarified intent
- Retrieved evidence and application state
- Tool calls, responses, and errors
- The final answer or action
- The criterion being evaluated
- A simple way to record a label and rationale

The goal is to make qualified judgment fast enough that domain expertise can shape the eval system continuously.

“The most important part that people should learn is how to look at data,” Husain says. “It tends to be the one place where 95% of problems are found and resolved and clarity is brought to the eval process.”

That skill takes practice because useful error analysis involves more than finding bad outputs. Reviewers have to connect each failure to the product decision, missing context, tool behavior, or evaluation assumption that created it.

**Better AI evals begin with better diagnosis**

Agent engineers work across product design, context assembly, tools, permissions, models, and [evaluation systems](https://arize.com/resources/ai-agent-evaluation/). A weak result can originate in any of those layers.

Before adding another metric, teams should ask a more basic set of questions:

- Did the product collect enough information?
- Did the agent receive the right context and tools?
- Can reviewers see what happened across the [full trajectory](https://arize.com/resources/agent-harness-evaluation-tracing/)?
- Does the criterion reflect a failure that matters to the product?

Sometimes the right response to a disappointing eval is a prompt change or model experiment. In other cases, the product needs a clarification step, the tool contract needs revision, or the team needs to define success more precisely.

Husain’s advice gives developers a practical place to begin: open the [traces](https://arize.com/glossary/llm-tracing/), bring in the domain expert, and study the failures closely enough to understand which part of the system deserves to change.

A dashboard can show that the agent missed, but error analysis reveals why.
