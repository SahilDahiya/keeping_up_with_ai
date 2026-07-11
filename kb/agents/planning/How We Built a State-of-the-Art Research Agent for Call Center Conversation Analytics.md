---
title: How We Built a State-of-the-Art Research Agent for Call Center Conversation
  Analytics
topic: agents
subtopic: planning
secondary_topics:
- product-engineering/architecture
summary: Detailed build story for a research agent over conversation analytics, covering
  agent design and domain-specific workflow constraints.
source: cresta
url: https://cresta.com/blog/how-we-built-a-state-of-the-art-research-agent-for-call-center-conversation-analytics
author: Iwona Bialynicka-Birula
published: '2025-12-04'
fetched: '2026-07-11T03:59:45Z'
classifier: codex
taxonomy_rev: 1
words: 2814
content_sha256: 69d86f654898972d83a5873b859c6cdd2ffae102ff86a6a09c3b812f9d2f425c
---

# How We Built a State-of-the-Art Research Agent for Call Center Conversation Analytics

Conversation transcripts, generated as part of contact center operations, are a goldmine of information for any enterprise.

Why? They answer fundamental questions that uncover valuable business insights, such as:

”Why are customers churning?”

”Why are they choosing competitors’ products over ours?”

”Which sales strategies are the most effective?

**Before the rise of Large Language Models (LLMs), extracting these insights took significant time and money. **

200+ hours and several months of manual effort per analysis to read through hundreds of transcripts to answer a single question. Then, produce a detailed report that included valid sample sizes.

Leaders often had follow-up questions about the analysis result, which landed back in the months-long queue. More often than not, leaders didn’t want to wait so long, so they just gave up on finding out the answer.

**In the best case, businesses could afford to answer only a handful of these questions each year and had no way to quickly adapt to rapidly changing trends.**

LLMs revolutionized this entire process: Now there was a fast, significantly less expensive means to analyze a large volume of conversations to answer a question posed in natural language.

*Cresta AI Analyst** — a deep research conversational agent for analyzing contact center conversations — was among the first products of this revolution.*

This article will detail the technical details behind how AI Analyst works, the journey to build it, and the lessons learned along the way. Let’s start with some of the technical stuff.

### The AI Analyst Architecture Overview

AI Analyst is a conversational research agent for contact-center conversation analytics, which combines LLM reasoning, retrieval grounding, and deterministic analytics.

![__wf_reserved_inherit](https://cdn.prod.website-files.com/67feba4d16c14d85f1696c4f/69f99e5a81e238c395577d9e_6930c249af90b967117f3391_blog-how-we-built-research-agent-inline-1.png)

Instead of dumping transcripts into a single prompt, the system mirrors an expert analyst’s workflow:

- Analyzes each conversation individually
- Composes those per-conversation analyses into taxonomies
- Assigns conversations to categories
- Computes deterministic aggregations and reports, with conversation and message level citations, ensuring results are auditable and verifiable.

![__wf_reserved_inherit](https://cdn.prod.website-files.com/67feba4d16c14d85f1696c4f/69f99e5a81e238c395577d97_69408bd94d351037a1f1607a_blog-how-we-built-a-state-of-the-art-research-agent--in-line-graph-2.png)

Getting a *touch* more technical, the agentic workflow includes the following steps:

A: The user posts a research question or answers/confirms the AI Analyst's previous question as part of a free-flowing conversation.

The request is forwarded to the** Main Agent**, which drives the analysis.

B: The **Main Agent** operates in a controlled, internal *tool-call loop*, intentionally cycling between reasoning and action. Each turn, it either responds in text or calls analysis tools, using their output to decide what to do next. 

C: For analysis tool calls (small or full analysis), the **Main Agent** dispatches per-conversation analyses in parallel to the: 

D: **Conversation Agent** where each conversation is rephrased into a single-conversation question, analyzed, checked for accuracy using proprietary heuristics and embedding similarity, and returned with claims, supporting evidence, and a relevancy flag.

E: The* ***Main Agent** then invokes the **Categorization Agent** to aggregate condensed conversation-level outputs, produce a taxonomy (categories), and assign conversations to categories in batches. The categorizer excludes irrelevant or non-factual answers before aggregation.

F: The AI Analyst report is produced. The **Main Agent** may continue the iterative *tool-call loop* (run further analysis or refinements) as needed. Alternatively, if the **Main Agent **chooses a pure text turn, it returns an assistant message (i.e. *“Report is ready!”*) or a follow-up question, and exits the *tool-call loop*.

G: Finally, the **System** returns the report and/or assistant reply to the user, and waits for the next action from the user (Back to A).

The workflow has the following key properties:

- Multi-agent separation of concerns (orchestration, per-conversation analysis, categorization)
- Explicit evidence grounding and factuality verification
- Parallel per-conversation execution for scale
- An iterative agentic loop

These properties didn't emerge by accident. They're the result of an intentional design process shaped by direct collaboration with the people who use our product every day.

### How we got here

In the AI-powered era, rapid feedback and user iteration loops are essential. Cresta engages our expert user base — our design and strategic thought partners — in our development process from start to finish.

The traditional approach—product managers writing requirements, design and engineering creating specs, and engineering implementing the solution—doesn’t work for ML-powered products. These products require all teams to iterate tightly together, and while this can feel chaotic, having the right experts in the room often produces remarkable clarity and elegance.

We will never know our customers’ businesses and most pressing questions as well as they do. This is why we engage them from the start —onsite, face-to-face meetings, watching and learning how their expert analysts solve problems. From there, we rapidly prototype our system with the customer their, every step of the way across product, ML, and design.

During these iterations, we often make suboptimal decisions and fail...even with our most strategic customers. Yet, instead of failing in an opaque development silo, our “fail publicly” mindset allows us to minimize cycle times from days/weeks to mere hours.

#### Our naive approach, exposed.

When we first embarked on the journey of building AI Analyst, we started with the classic “rookie move” approach: We sampled some conversation transcripts and dumped them along with the user’s question into an LLM’s context, asking it to generate a report in response to the question.

However, reports generated using this approach generally do not hold up to any kind of scrutiny.

Why? A few reasons:

- LLM task quality degrades rapidly as the size of the context increases.
- LLMs are not great at counting, especially when asked to analyze conversations, categorize the outputs, and compute aggregate statistics...all in one go.
- LLMs get easily confused when faced with a variety of different inputs. In this case, many different conversations talking about many different things.

Here is how we solved for this.

#### An LLM workflow to reflect the human expert workflow

We added in the human element.

We replicated the process human data scientists follow when performing similar analysis, breaking it into distinct tasks:

- Analyzed a single conversation to answer the given question.
- Extracted high-level themes (categories) from the analysis results.
- Assigned a batch of analysis results to the identified categories.

Next, we combined these three tasks into a deterministic LLM workflow that also computed statistics and tied each LLM-extracted claim to its corresponding citation in the conversation transcript. This ensured the results were accurate and easy to verify manually.

#### Teaching the LLM when to say "I don't know"

Adding the human element greatly improved the quality of the output, but we were still seeing hallucinated outputs. Upon further investigation, it turned out that the main driver of hallucinations was conversations that did not contain the answer to the question the user was asking.

For example, a user may be asking, “Why are customers cancelling their subscriptions?”, but not all of the conversations in the analyzed samples involved canceling subscriptions. These “irrelevant conversations” led to the hallucinations — after all, most LLMs aim to please. So the AI would tend to make something up (i.e., “The customer canceled their subscription because it was too expensive.”) just to provide an answer to the question.

To address this issue, we added a way for the LLM to “abstain” by marking a conversation as “irrelevant to the question”, instead of providing a made up answer.

#### One agent to rule them all

We found this approach drastically reduced hallucinations; however, this introduced a new problem: users began reporting that for a lot of their queries they were getting back “irrelevant to the question” responses — in some cases, even 100% of the conversations were marked irrelevant.

There were a number of reasons for this overcorrection:

- **Missing translation step:**Since conversations were analyzed one by one, the overall research objective (“What are the top reasons customers are cancelling their subscriptions?”) had to be translated into a question- *about the conversation*(“Why did the customer cancel their subscription in this conversation?”). Without this translation step, the LLM would deem every conversation irrelevant, because a single conversation can not answer a question about something like “top reasons.”
- **Lack of user guidance**: Many users needed help selecting the most representative conversation sample to analyze. For example, they would ask “What are the top reasons customers are cancelling their subscriptions?”, but would forget to select the subset of conversations that contained cancellations.
- **Too many assumptions**: Users would assume a business context that the LLM didn’t have access to, including internal company acronyms or jargon that the LLM had a difficult time interpreting.

To add complexity to our diagnosis and remedy, LLM workflows were quickly giving way to Multi-Agent Systems (MAS) — multiple autonomous agents that interact (either cooperating, competing, or coordinating) — to achieve tasks were becoming more the norm. It quickly became clear we needed a main agent to facilitate the whole analysis. The report-generating LLM workflow was still a great tool (it became a literal tool that the main agent had access to), but we needed an AI agent to do more. Specifically:

- Converse with the user to understand their research objective and ask any clarifying questions, as needed.
- Formulate the question to analyze each individual conversation.
- Collaborate with the user to ensure that the right conversation sample was selected for analysis.

The net result: a framework that is very easy to extend and build upon. Today, AI Analyst has access to a handful of tools to analyze a conversation, generate a report, or drill down into a category of results. But as LLMs become increasingly capable of tool use and as we are building out increasingly deeper integrations with Cresta’s unified platform, we are constantly extending it with additional capabilities.

### Evaluation and prompt-tuning

Prompt engineering and evaluation were key components in the development of AI Analyst.

We broke the work into a few phases: **Phase #1: Coaching**During this phase, we focused on “coaching” AI Analyst to follow the steps that human analysts typically take to complete an analysis task. 

A human expert data scientist reviewed AI Analyst’s behavior and identified opportunities to course-correct, analogous to training a human apprentice to become an expert analyst.

For example, the expert noticed that AI Analyst didn’t clarify acronyms and jargon to better understand the user’s resource objective, as human analysts did. These observations turned into annotations about what the LLM could have done better in a given turn of the conversation, which then could easily be turned into general guidelines for AI Analyst to follow, evaluations to validate that the agent was indeed following these guidelines, and semi-automated prompt tuning iterations.

**Phase #2: Evaluate report quality. **

This stage required a more rigorous review as our customers used these reports to make critical business decisions. Since there’s a host of possible metrics one could use to evaluate AI Analyst reports (i.e., “Did the agent formulate the right research objective?” or “Did the categories strike the right balance between specificity and generality?”), it was crucial to define the key ones to focus on.

Human experts scrutinized a wide range of AI Analyst reports and identified two key metrics that were key drivers of report quality: **relevance** **classification accuracy** and the **factuality of** **claims** about the conversations the agent was having.

Let’s dig into each one.

#### Relevance classification accuracy

Relevance — the process of determining whether an AI model’s response (or a piece of text) is on-topic and useful for a given question or goal — is inherently subjective. For the AI Analyst, relevance evaluation was guided by the concept of *information gain*: a “relevant” conversation being one that contributes insightful information to the overall analysis. 

We chose to cast a wider net rather than filter too narrowly, since the ultimate analysis should deliver a comprehensive answer to the user’s question. Once we established this evaluation metric, we optimized the LLM prompts to accurately reflect the decision boundary between “relevant” and “irrelevant” conversations, as perceived by human experts.

Relevance was only half the equation.

#### Factuality of claims

In evaluating single-conversation analyses, it was crucial to ensure that each conversation was analyzed without fabrication or leaps in reasoning.

This involved assessing whether the LLM introduced hallucinations, something relatively easy to detect when AI-generated claims are about “hard facts” such as, “What year was Barack Obama born?”. But this is not the typical question being asked of AI Analyst. More common were questions like “Why are customers satisfied?”, which required determining whether a specific customer is satisfied in a given conversation *and* conducting a root-cause analysis of why. 

Validating the factuality of the resulting answers was much more involved than checking simple fact-seeking questions. It was for this reason — as well as the [general shortcoming of out-of-the-box evaluators](https://cresta.com/blog/why-you-cant-trust-out-of-the-box-evaluators) — that we took the extra time and effort.

When expert human analysts evaluate each other’s work, much of the factuality assessment relies on their domain-specific knowledge. For example, in the case of “satisfaction,” Cresta has its own [proprietary framework](https://cresta.com/blog/the-csat-mirage-you-might-have-a-survey-problem) for evaluating customer satisfaction in conversations. 

This meant it was essential to align the criteria with Cresta’s expert standards, which led us to an [expert-annotated benchmark dataset](https://github.com/cresta/fect) that reflects our internal expertise in conversation analysis. We use this dataset to continuously monitor AI Analyst performance with respect to the factuality metric to ensure that it continues to meet the high quality standards our customers have come to expect.

With all of the above, we learned a few lessons along the way.

### 5 lessons learned from building AI Analyst

Here are five lessons we learned while developing AI Analyst:

**1. Simplify the problem for the LLM. **Dumping a large number of conversation transcripts into the LLM context yielded poor results. [Hallucinations](https://cresta.com/blog/grounding-reality---how-cresta-tackles-llm-hallucinations-in-enterprise-ai) abounded, counts were off, and the produced reports looked good only on the surface, but did not stand up to any kind of scrutiny. 

To remedy this, we created tasks an LLM could reliably do: analyzing a single conversation, proposing a taxonomy of categories, or assigning a batch of items to these categories. We then tied these basic building blocks together with deterministic code to create an LLM workflow, composed of hundreds of LLM calls, that consistently produced reliable results.

**2. No user inputs should go into an LLM prompt as is. **In the first iteration of AI Agent, we let users pose questions that would get input verbatim into the LLM conversation analysis prompt. 

Testing with internal users produced several reports of unsatisfactory results, due to the fact that the users didn’t know how the system worked under the hood and — importantly — they are not prompt engineering experts. They asked questions that did not work well with the LLM workflow.

In response, we built an AI conversational agent that converses with the user to identify the user’s research goal and formulates the question in a way that is compatible with the LLM workflow.

**3. Mitigate hallucinations by allowing the LLM to “abstain.” **Providing the LLM with a question and a conversation and then asking it to answer the question based on the conversation did not go as anticipated. Remember: most LLMs aim to please. So whenever the conversation did *not* contain the information needed to answer the question (often the case), it would make something up.

As a result, we gave the LLM the option to determine that the conversation doesn’t contain relevant information instead of answering the question, which [greatly reduced hallucination rates](https://cresta.com/blog/grounding-reality---how-cresta-tackles-llm-hallucinations-in-enterprise-ai). 

**4. Require the LLM to cite  and verify evidence. **In addition to answering the question, we also ask the LLM to cite evidence supporting the answer and then use a combination of deterministic lexical and semantic string matching to find that evidence in the conversation. This not only allows us to automatically discard any hallucinated answers, but gives users a way to quickly verify the results, instilling confidence in their accuracy.

**5. Don’t ask LLMs to do what a simple program can do instead.** Don’t overthink. While LLMs are amazing, they are not always the answer, especially when you consider costs. Simple programs can often do tasks for less money, with better results.

Example: In order to produce a report, AI Analyst computes the statistics of how many conversations fall into which category. Naive implementations of similar-looking products dump all of the conversations into a single context window and ask the LLM to perform all the tasks involved in generating a report, including counting and computing statistics. LLMs often make mistakes while performing this type of task, and, unfortunately, the output cannot be easily verified

Lesson learned: We now break the task down into multiple LLM calls. This means the LLM can implement the computations as part of the deterministic code that orchestrates them, so that the statistics in the resulting report are guaranteed to be 100% correct and can be easily verified.

None of this would have been possible without our customers in the room. **That’s the real lesson: Build  with your customers and users, not just for them.**
