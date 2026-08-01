---
title: Executable Code Actions Elicit Better LLM Agents
kind: paper
topic: agents
subtopic: tool-use
secondary_topics: []
summary: Argues LLM agents should act by generating executable Python code rather
  than JSON tool calls or free text. Consolidating actions into code gives one unified
  action space where the model composes tools, uses control flow, and revises on execution
  feedback; across 17 LLMs CodeAct achieves up to ~20% higher success with fewer actions
  than JSON/text baselines. Releases the CodeActInstruct dataset and the open CodeActAgent
  — the canonical statement of the code-as-action paradigm.
triage: null
skip_reason: null
source: arxiv
url: https://arxiv.org/abs/2402.01030
author: Xingyao Wang, Yangyi Chen, Lifan Yuan, Yizhe Zhang, Yunzhu Li, Hao Peng, Heng
  Ji
published: '2024-02-01'
fetched: '2026-08-01T19:06:43Z'
classifier: claude
taxonomy_rev: 2
words: 10105
content_sha256: 1b56e8d40bc471bd51891dc32f26412fc3a799b7ad8763d5f27c0b5caa54a2f0
arxiv_id: '2402.01030'
categories:
- cs.CL
- cs.AI
fulltext: html
updated: '2024-06-07'
---

# Executable Code Actions Elicit Better LLM Agents

**Authors:** Xingyao Wang, Yangyi Chen, Lifan Yuan, Yizhe Zhang, Yunzhu Li, Hao Peng, Heng Ji
**arXiv:** [2402.01030](https://arxiv.org/abs/2402.01030) · cs.CL, cs.AI
**Comment:** Accepted by ICML 2024; Code, data, model, and demo are available at https://github.com/xingyaoww/code-act

## Abstract

Large Language Model (LLM) agents, capable of performing a broad range of actions, such as invoking tools and controlling robots, show great potential in tackling real-world challenges. LLM agents are typically prompted to produce actions by generating JSON or text in a pre-defined format, which is usually limited by constrained action space (e.g., the scope of pre-defined tools) and restricted flexibility (e.g., inability to compose multiple tools). This work proposes to use executable Python code to consolidate LLM agents' actions into a unified action space (CodeAct). Integrated with a Python interpreter, CodeAct can execute code actions and dynamically revise prior actions or emit new actions upon new observations through multi-turn interactions. Our extensive analysis of 17 LLMs on API-Bank and a newly curated benchmark shows that CodeAct outperforms widely used alternatives (up to 20% higher success rate). The encouraging performance of CodeAct motivates us to build an open-source LLM agent that interacts with environments by executing interpretable code and collaborates with users using natural language. To this end, we collect an instruction-tuning dataset CodeActInstruct that consists of 7k multi-turn interactions using CodeAct. We show that it can be used with existing data to improve models in agent-oriented tasks without compromising their general capability. CodeActAgent, finetuned from Llama2 and Mistral, is integrated with Python interpreter and uniquely tailored to perform sophisticated tasks (e.g., model training) using existing libraries and autonomously self-debug.

---

# Executable Code Actions Elicit Better LLM Agents

###### Abstract

Large Language Model (LLM) agents, capable of performing a broad range of actions, such as invoking tools and controlling robots, show great potential in tackling real-world challenges.
LLM agents are typically prompted to produce actions by generating JSON or text in a pre-defined format, which is usually limited by constrained action space (e.g., the scope of pre-defined tools) and restricted flexibility (e.g., inability to compose multiple tools).
This work proposes to use executable Python code to consolidate LLM agents’ actions into a unified action space (CodeAct).
Integrated with a Python interpreter, CodeAct can execute code actions and dynamically revise prior actions or emit new actions upon new observations through multi-turn interactions.
Our extensive analysis of 17 LLMs on API-Bank and a newly curated benchmark shows that CodeAct outperforms widely used alternatives (up to 20% higher success rate).
The encouraging performance of CodeAct motivates us to build an open-source LLM agent that interacts with environments by executing interpretable code and collaborates with users using natural language.
To this end, we collect an instruction-tuning dataset CodeActInstruct that consists of 7k multi-turn interactions using CodeAct.
We show that it can be used with existing data to improve models in agent-oriented tasks without compromising their general capability.
CodeActAgent, finetuned from Llama2 and Mistral, is integrated with Python interpreter and uniquely tailored to perform sophisticated tasks (e.g., model training) using existing libraries and autonomously self-debug111The code, data, model, and demo are available at [https://github.com/xingyaoww/code-act](https://github.com/xingyaoww/code-act)..

## 1 Introduction

Large Language Models (LLMs) have emerged as a pivotal breakthrough in natural language processing (NLP).
When augmented with action modules that allow access to APIs, their action space expands beyond conventional text processing, allowing LLMs to acquire capabilities such as tool invocation and memory management (Mialon et al., [2023](https://arxiv.org/html/2402.01030v4#bib.bib33); Schick et al., [2023](https://arxiv.org/html/2402.01030v4#bib.bib44)) and venture into real-world tasks such as controlling robots (Ahn et al., [2022](https://arxiv.org/html/2402.01030v4#bib.bib1); Huang et al., [2023](https://arxiv.org/html/2402.01030v4#bib.bib22); Ma et al., [2023](https://arxiv.org/html/2402.01030v4#bib.bib32)) and performing scientific experiments (Bran et al., [2023](https://arxiv.org/html/2402.01030v4#bib.bib4)).

We inquire: how to effectively expand LLM agents’ action space for solving complex real-world problems?
Much existing research has examined using text (Yao et al., [2022b](https://arxiv.org/html/2402.01030v4#bib.bib67); Park et al., [2023](https://arxiv.org/html/2402.01030v4#bib.bib37), inter alia) or JSON (Qin et al., [2023b](https://arxiv.org/html/2402.01030v4#bib.bib43); Chase, [2022](https://arxiv.org/html/2402.01030v4#bib.bib6), inter alia) to produce actions (e.g., tool uses in Fig. [1](https://arxiv.org/html/2402.01030v4#S1.F1) top left).
However, both methods typically suffer from constrained scope of action spaces (actions are usually tailored for specific tasks) and restricted flexibility (e.g., inability to compose multiple tools in a single action).
As an alternative approach, several work (Liang et al., [2022](https://arxiv.org/html/2402.01030v4#bib.bib29); Singh et al., [2023](https://arxiv.org/html/2402.01030v4#bib.bib47); Wang et al., [2023a](https://arxiv.org/html/2402.01030v4#bib.bib52)) demonstrate the potential of using LLMs to generate code to control robots or game characters.
However, they typically rely on pre-specified control primitives and hand-engineered prompts and, more importantly, struggle to dynamically adjust or emit actions based on new environmental observation and feedback.

This work proposes CodeAct, a general-purpose framework that allows LLMs to generate executable Python code as actions (Fig. [1](https://arxiv.org/html/2402.01030v4#S1.F1) top right).
CodeAct is designed to handle a variety of applications and comes with unique advantages:

- 
(1) 
Integrated with a Python interpreter, CodeAct can execute code actions and dynamically adjust prior actions or emit new action based on observations (e.g., code execution results) it receives through multiple turns of interactions. 
- 
(2)
Code actions allow LLM to leverage existing software packages. CodeAct can use readily available Python packages for an expanded action space instead of hand-crafted task-specific tools (Yuan et al., [2023](https://arxiv.org/html/2402.01030v4#bib.bib70); Shen et al.,[2023](https://arxiv.org/html/2402.01030v4#bib.bib45)). It also allows LLM to use automated feedback (e.g., error messages) implemented in most software to improve task-solving by self-debugging its generated code (Chen et al.,[2023b](https://arxiv.org/html/2402.01030v4#bib.bib9); Wang et al.,[2023d](https://arxiv.org/html/2402.01030v4#bib.bib57)).
- 
(3)
Code data is widely used in pre-training today’s LLMs (Yang et al., [2024b](https://arxiv.org/html/2402.01030v4#bib.bib63)). These models are already familiar with structured programming languages, allowing cost-effective adoption of CodeAct.
- 
(4)
Compared to JSON and text with a pre-defined format, code inherently supports control and data flow, allowing for the storage of intermediate results as variables for reuse and the composition of multiple tools to perform complex logical operations (e.g., if-statements, for-loops) with one piece of code, thereby unlocking LLMs’ potential to tackle complex tasks by leveraging its pre-trained knowledge of programming. In Fig. [1](https://arxiv.org/html/2402.01030v4#S1.F1), an LLM using with CodeAct (top right) can apply the same sequence of tools (e.g., passing one tool’s output as input to another tool using the data flow feature) to all inputs through for-loops (i.e., control flow feature) with one action; while text or JSON have to take action for every input (top left).

Our extensive experiments with 17 LLMs (including both open-source and proprietary ones) confirm the above benefits (3
& 4) of CodeAct.
To demonstrate benefit (3), our first experiment (§[2.2](https://arxiv.org/html/2402.01030v4#S2.SS2)) compares CodeAct to baselines on basic tasks involving atomic tool use (i.e., only one tool is used per action), ablating the control and data flow advantage offered by CodeAct.
The results show that, for most LLMs, CodeAct achieves comparable or better performance than the baselines.
CodeAct’s performance gains are more prominent on complex tasks, as demonstrated in our second experiment (benefit 4).
We curate a new benchmark consisting of 82 human-curated tasks that typically require multiple calls to multiple tools in multi-turn interactions (M3ToolEval; §[2.3](https://arxiv.org/html/2402.01030v4#S2.SS3)).
Problems in this benchmark often require intricate coordination and composition of multiple tools.
With its strengths in control and data flow, CodeAct achieves up to a 20% absolute improvement over baselines on the success rate of solving the problems while requiring up to 30% fewer actions.
These performance gains widen as the capabilities of the LLMs increase (Fig. [1](https://arxiv.org/html/2402.01030v4#S1.F1) bottom).

The promising performance of CodeAct motivates an open-source LLM agent that can effectively act through CodeAct, and collaborate with humans through natural language.
To this end, we collect an instruction-tuning dataset CodeActInstruct consisting of 7k high-quality multi-turn interaction trajectories with CodeAct (§[3.1](https://arxiv.org/html/2402.01030v4#S3.SS1)).
CodeActInstruct is motivated by a general agent framework consisting of agent, user, and environments (Fig. [2](https://arxiv.org/html/2402.01030v4#S2.F2)) and focuses on agent-environment interactions with the computer (information seeking, software package use, external memory) and the physical world (robot planning).
On CodeActInstruct, we perform careful data selection to promote the capability of improving from multi-turn interaction (e.g., self-debug).
We show that CodeActInstruct can be used with commonly used instruction tuning data to improve the models’ performance in agent tasks without compromising their general capabilities (e.g., knowledge-based QA, coding, instruction following, §[3.2](https://arxiv.org/html/2402.01030v4#S3.SS2)).
Our model, dubbed CodeActAgent, is finetuned from LLaMA-2 (Touvron et al., [2023](https://arxiv.org/html/2402.01030v4#bib.bib51)) and Mistral-7B (Jiang et al., [2023](https://arxiv.org/html/2402.01030v4#bib.bib23)) and improves on out-of-domain agent tasks with not only CodeAct, but also text action in a pre-defined format (§[3.2](https://arxiv.org/html/2402.01030v4#S3.SS2)).

CodeAct can further benefit from multi-turn interactions and existing software (benefit 1 & 2, §[2.4](https://arxiv.org/html/2402.01030v4#S2.SS4)).
As shown in Fig. [3](https://arxiv.org/html/2402.01030v4#S2.F3), CodeActAgent, designed for seamless integration with Python, can carry out sophisticated tasks (e.g., model training, data visualization) using existing Python packages. Error messages from the environment further enable it to rectify errors autonomously through self-debugging in multi-turn interaction.
Thanks to LLM’s extensive programming knowledge acquired during pre-training, these are achieved without needing in-context demonstrations, reducing the human efforts for adapting CodeActAgent to different tasks.

| CodeAct for LLM action | JSON or Text for LLM action | |
|---|---|---|
| Availability of Data | ✔Large quantity of code available 1for pre-training | ✗Data curation required for particular format | 
| Complex Operation (e.g., looping, composition of multiple tools) | ✔Natively supported via control and data flow | ✗Requires careful engineering if feasible (e.g., define new tools to mimic if-statement) | 
| Availability of Tools | ✔Can directly use existing software packages 2 | ✗Requires human effort to curate tools from scratch or existing software | 
| Automated Feedback | ✔Feedback mechanism 3(e.g., traceback) is already implemented as an infrastructure for most programming languages | ✗Requires human effort to provide feedback or re-route feedback from the underlying programming language used to implement the tools | 

- 
1
Including code demonstrating useful behaviors for LLM agents (e.g., task decomposition, coordination of multiple function calls to different tools). 
- 
2
Human-written Python packages covering a wide range of applications are available on [https://pypi.org/](https://pypi.org/).
- 
3
For example, in Python, errors and exceptions ( [https://docs.python.org/3/tutorial/errors.html](https://docs.python.org/3/tutorial/errors.html)) are available. Most software provides error messages in natural language to help human programmers debug their code. CodeAct enables LLM to use them directly.

## 2 CodeAct Makes LLMs Better Agents

In this section, we first describe CodeAct framework (§[2.1](https://arxiv.org/html/2402.01030v4#S2.SS1)) and provide empirical evidence that supports the choice of CodeAct.
We focus on Python as the programming language for CodeAct due to its popularity (ranked top-1 at (TIOBE Index, [2024](https://arxiv.org/html/2402.01030v4#bib.bib50))) and numerous open-source packages.
We aim to answer several research questions (RQs) using 17 off-the-shelf LLMs. In §[2.2](https://arxiv.org/html/2402.01030v4#S2.SS2), we examine RQ1: Does LLMs’ familiarity with code due to a large amount of code pre-training data bring CodeAct advantages over text and JSON?
We discuss RQ2 in §[2.3](https://arxiv.org/html/2402.01030v4#S2.SS3): Does CodeAct benefit from Python’s innate control and data flow feature in complex problems?
Finally, as an additional benefit, we discuss how using CodeAct further enhances LLM agents by enabling multi-turn interactions and allowing them to access existing software in §[2.4](https://arxiv.org/html/2402.01030v4#S2.SS4) and Fig. [3](https://arxiv.org/html/2402.01030v4#S2.F3).

### 2.1 What is CodeAct?

In Fig. [2](https://arxiv.org/html/2402.01030v4#S2.F2), we first introduce a general multi-turn interaction framework for LLM agents’ real-world usage that considers three roles (Yang et al., [2024c](https://arxiv.org/html/2402.01030v4#bib.bib65)): agent, user, and environment.
We define interaction as the information exchange between the agent and an external entity (user or environment).
For each turn of interaction, the agent receives an observation (input) either from the user (e.g., natural language instruction) or the environment (e.g., code execution result), optionally planning for its action through chain-of-thought (Wei et al., [2022](https://arxiv.org/html/2402.01030v4#bib.bib60)), and emits an action (output) to either user in natural language or the environment.
CodeAct employs Python code to consolidate all actions for agent-environment interaction. In CodeAct, each emitted action to the environment is a piece of Python code, and the agent will receive outputs of code execution (e.g., results, errors) as observation.
We include an example prompt of CodeAct in §[E](https://arxiv.org/html/2402.01030v4#A5).

### 2.2 CodeAct Shows the Promise as a Strong Tool Use Framework

In this section, we perform a controlled experiment to understand which format (text, JSON, CodeAct) is more likely to lead an LLM to generate correct atomic tool calls. The performance in this experiment reflects LLM’s familiarity with the corresponding format. We hypothesize that using CodeAct to call tools is a more natural way to use tools for the models, which typically have extensive exposure to code data during their training.

Setup.
We re-purpose API-Bank (Li et al., [2023](https://arxiv.org/html/2402.01030v4#bib.bib27)) and test LLMs’ API-calling performance, comparing CodeAct, JSON, and text actions.
For each evaluation instance, we instruct LLM to generate one atomic tool call in the format of a Python function call, JSON object, or text expression in a pre-defined format. A concrete example is shown in Tab. [A.6](https://arxiv.org/html/2402.01030v4#A0.T6).
We use API-Bank’s level-1 instructions and the provided toolset. To evaluate API-calling, we follow their correctness metric, matching the ground-truth API outputs with the actual model-generated API’s execution outputs.

Results.
We present results in Tab. [3](https://arxiv.org/html/2402.01030v4#S2.T3).
For most LLMs, CodeAct achieves comparable or better performance even in atomic actions (the simplistic tool use scenario) where its control and data flow strengths are ablated.
Compared to closed-source LLMs, CodeAct’s improvements are more prominent in open-source models. Furthermore, code data is usually more accessible for fine-tuning open-source LLMs than the specialized JSON or text tool-calling format.
Although JSON is consistently weaker than other approaches for open-source models, it achieves decent performance with closed-source LLMs, indicating that these closed-source models may have gone through targeted fine-tuning toward their JSON capabilities.
These results suggest optimizing for CodeAct is a better route for open-source LLMs than alternatives to improve their tool-use capabilities, as they already show good initial CodeAct capability due to extensive exposure to code data during pre-training.

### 2.3 CodeAct Gets More Done with Fewer Interactions

In this section, we investigate whether LLM agents can benefit from the control and data flow of code on problems that require complex patterns of tool use.

M3ToolEval.
As shown in Tab. [A.7](https://arxiv.org/html/2402.01030v4#A0.T7), to the best of our knowledge, no existing tool-use benchmarks contain complex tasks requiring the composition of multiple tools while supporting evaluating different action formats. Hence, we curate a benchmark M3ToolEval to fill this gap, which evaluates LLMs’ capabilities in solving complex tasks that typically require multiple calls to multiple tools in multi-turn interactions.
It contains 82 human-curated instances, spanning tasks including web browsing, finance, travel itinerary planning, science, and information processing.
Each domain is accompanied by a unique set of manually crafted tools.
We intentionally keep the prompt simple (examples in §[F](https://arxiv.org/html/2402.01030v4#A6)) and avoid providing any demonstration to test the LLM’s zero-shot ability to use tools, similar to how a novice user without knowledge of few-shot prompting would use the model.

Setup.
We allow the model to generate fully functional Python code that enables control and data flow (e.g., if-statement, for-loop). We follow the action format for JSON and text described in Tab. [A.6](https://arxiv.org/html/2402.01030v4#A0.T6).
Within each turn, the model can either emit an action or propose an answer to be verified by an exact match with the ground-truth solution.
The interaction will terminate when a maximum of 10 interaction turns are reached or a correct solution has been submitted, similar to (Wang et al., [2023e](https://arxiv.org/html/2402.01030v4#bib.bib58)).

Metric. We measure the success rate by calculating the percentage of the model proposed answers that match the ground-truth solutions. We also include the avg. turns metric: the average number of turns on all evaluated instances.

Quantitative Results on M3ToolEval.
We include full results in Tab. [3](https://arxiv.org/html/2402.01030v4#S2.T3) and a subset of results for visualization in Fig. [1](https://arxiv.org/html/2402.01030v4#S1.F1).
CodeAct generally has a higher task success rate (12 out of 17 evaluated LLMs), similar to the trend in §[2.2](https://arxiv.org/html/2402.01030v4#S2.SS2). Moreover, using CodeAct requires a lower average number of turns (12 out of 17 evaluated LLMs).
For example, the best model gpt-4-1106-preview achieves a % absolute improvement compared to the next best action format (text) while requiring  fewer interaction turns on average.
However, there is still a significant gap in terms of absolute CodeAct performance between open- and closed-source LLMs as the best open-source model achieving 13.4% while the best closed-source model gpt-4-1106-preview 74.4%. This is potentially due to open-source models’ weak task-solving capability and inability to follow complex instructions without demonstration, suggesting an urgent need to improve open-source LLMs for practical, real-world tasks under the zero-shot setting.

### 2.4 CodeAct Benefits from Multi-turn Interactions and Existing Software Packages

In Fig. [3](https://arxiv.org/html/2402.01030v4#S2.F3), we show how an LLM agent can integrate with Python (i.e., CodeActAgent we trained in §[3.2](https://arxiv.org/html/2402.01030v4#S3.SS2)) and use existing software to perform complex tasks in multi-turn interactions.
Thanks to its extensive knowledge of Python learned during pre-training, the LLM agent can automatically import the correct Python libraries to solve tasks without requiring user-provided tools or demonstrations.
As illustrated in Fig. [3](https://arxiv.org/html/2402.01030v4#S2.F3), CodeActAgent can use Pandas to download and process tabular data, use Scikit-Learn for machine learning train-test data split and regression model training, and use Matplotlib for data visualization.
Furthermore, using the interactive Python interpreter for code execution allows automated error messages that help the LLM agent ‘self-debug’ their actions in a multi-turn interaction and eventually complete the human user’s request correctly.

## 3 Empowering Open-source LLM Agent to be Better at CodeAct

The promising results achieved by CodeAct motivate us to build an open-source LLM agent that can both interact with environments through CodeAct and communicate with humans using language.
To improve open-source LLMs’ CodeAct capability, in §[3.1](https://arxiv.org/html/2402.01030v4#S3.SS1), we introduce CodeActInstruct, an instruction finetuning dataset that contains agent-environment interaction trajectories.
We discuss data selection procedures in §[3.1](https://arxiv.org/html/2402.01030v4#S3.SS1) to promote improvement from interaction behavior.
Additionally, we show that CodeAct can be used together with existing agent-user conversation data (§[4](https://arxiv.org/html/2402.01030v4#S3.T4)) to balance the dialog capability of the resulting LLM.
Our model CodeActAgent, finetuned from LLaMA-2 (Touvron et al., [2023](https://arxiv.org/html/2402.01030v4#bib.bib51)) and Mistral-7B (Jiang et al., [2023](https://arxiv.org/html/2402.01030v4#bib.bib23)) on a mixture of CodeActInstruct and general conversations, improves CodeAct performances without hurting LLM’s general performance on a diverse suite of tasks (§[3.2](https://arxiv.org/html/2402.01030v4#S3.SS2)).

### 3.1 CodeActInstruct: Agent-Environment Interactions

We consider four main use cases in agent-environment interaction and repurpose five existing datasets across different domains to generate trajectories:

- 
•
Information Seeking: We use a training subset of HotpotQA (Yang et al., [2018](https://arxiv.org/html/2402.01030v4#bib.bib64)) to generate information-seeking trajectories, where LLMs use the wikipedia_search API (provided as a Python function) to search for information to answer questions.
- 
•
Software Package (Tool) Usage: We use the training set of code generation problems in APPS (Hendrycks et al., [2021a](https://arxiv.org/html/2402.01030v4#bib.bib18)) and math problems in MATH (Hendrycks et al.,[2021b](https://arxiv.org/html/2402.01030v4#bib.bib19)). The code generation tasks already involve importing packages and/or creating new tools by defining a new Python function. For MATH, we provide an in-context demonstration of importing Python packages (e.g., sympy for symbolic math) for problem-solving.
- 
•
External Memory: We repurpose the training subset of WikiTableQuestion (Pasupat & Liang, [2015](https://arxiv.org/html/2402.01030v4#bib.bib38)) and tweak it into two variants of tabular reasoning tasks that require accessing external memory: (1) SQL-based, requiring the LLM to interact with an SQL database through sqlite3 package to answer the question via SQL execution; (2) Pandas-based, requiring the model to interact with pandas tables to perform data operations (e.g., select, filter). Examples of instructions can be found in §[G.3.1](https://arxiv.org/html/2402.01030v4#A7.SS3.SSS1).
- 
•
Robot Planning: We use ALFWorld (Shridhar et al., [2020](https://arxiv.org/html/2402.01030v4#bib.bib46)), a text-only embodied environment simulator, to generate trajectories that use robot-control APIs (repurposed as Python function) to complete household tasks. Following MINT (Wang et al.,[2023e](https://arxiv.org/html/2402.01030v4#bib.bib58)), we provide an in-context demonstration to encourage the use of for-loop and if-statement code blocks to automate repetitive operations (e.g., searching for items by visiting different locations).

Data Down-sampling.
We down-sample each dataset by keeping only the most challenging instances, aiming to make trajectory generation more efficient and cost-effective. Furthermore, it also helps remove simple instances that existing LLMs can already solve.
The statistics of the filtered dataset can be found in Tab. [A.9](https://arxiv.org/html/2402.01030v4#A7.T9). Please refer to §[G.1](https://arxiv.org/html/2402.01030v4#A7.SS1) for details about the down-sample process.

Repurpose Data for Multi-turn Interaction.
Some datasets (APPS, MATH, WikiTableQuestions) are initially single-turn problems that expect one solution per instruction, whereas, in a realistic agent use case, we often require multi-turn interaction to complete each task (Fig. [1](https://arxiv.org/html/2402.01030v4#S1.F1) top).
Following MINT (Wang et al., [2023e](https://arxiv.org/html/2402.01030v4#bib.bib58)), we repurpose single-turn problems into multi-turn ones by allowing LLM to interact with the environment for multiple turns before it decides to submit one solution for evaluation.
Specifically for code generation problems, we provide an in-context example to guide LLMs to test their solution on provided test cases before they submit the solution.
Metrics from the original data will evaluate the submitted solution to determine its correctness. We include examples in §[G.3](https://arxiv.org/html/2402.01030v4#A7.SS3).

Trajectory Generation.
We use MINT’s evaluation framework (Wang et al., [2023e](https://arxiv.org/html/2402.01030v4#bib.bib58)) to generate interaction trajectories for the aforementioned datasets and determine the correctness of each trajectory.
We run gpt-3.5-turbo-0613 from OpenAI, claude-1-instant and claude-2 from Anthropic on down-sampled data, except code generation, which we use a longer-context version of GPT-3.5 (gpt-3.5-turbo-0613-16k) due to the long-context requirement of the self-debugging process.
On a subset of problems that none of these models can solve, we use gpt-4-0613 to generate trajectories.

Enhancing Agent’s Capabilities of Improving from Interaction.
We select a high-quality subset of all the generated trajectories from CodeActInstruct to promote the agent’s ability to improve the next action based on prior observations (e.g., self-debugging from code execution error message, a planning capability in Fig. [2](https://arxiv.org/html/2402.01030v4#S2.F2)).
To achieve this, we selectively preserve those trajectories wherein the model initially encounters errors but rectifies these inaccuracies in later interactions.
For these instances, the LLM typically engages in self-reflection following the initial error, thereby proactively enhancing its future actions.
Other filtering details are discussed in §[G.2](https://arxiv.org/html/2402.01030v4#A7.SS2).
On all trajectories generated, we keep 411 trajectories from gpt-4-0613 and 6728 trajectories from gpt-3.5 and claude.
The statistics of the resulting dataset CodeActInstruct are shown in Tab. [4](https://arxiv.org/html/2402.01030v4#S3.T4).

[3.1](https://arxiv.org/html/2402.01030v4#S3.SS1)for details about CodeActInstruct and general conversation data. Token statistics are computed using Llama-2 tokenizer.

| Data Mixture | Data Type | Data Name | # of Data Instances | # of Total Tokens | Avg. Tokens Per Instance | 
| Prior Work | - | FireAct (Chen et al., [2023a](https://arxiv.org/html/2402.01030v4#bib.bib7)) | |||
| - | AgentInstruct (Zeng et al., [2023](https://arxiv.org/html/2402.01030v4#bib.bib71)) | ||||
| CodeActInstruct (Ours) | Information Seeking | HotpotQA (Yang et al., [2018](https://arxiv.org/html/2402.01030v4#bib.bib64)) | |||
| Software Packages (Tool) | MATH (Math, (Hendrycks et al., [2021b](https://arxiv.org/html/2402.01030v4#bib.bib19))) | ||||
| Software Packages (Tool) | APPS (Code, (Hendrycks et al., [2021a](https://arxiv.org/html/2402.01030v4#bib.bib18))) | ||||
| External Memory | WikiTableQuestion (Pasupat & Liang, [2015](https://arxiv.org/html/2402.01030v4#bib.bib38)) | ||||
| Robot Planning | ALFWorld (Shridhar et al., [2020](https://arxiv.org/html/2402.01030v4#bib.bib46)) | ||||
| Total | |||||
| General Conversation | Single-Turn Reasoning | OpenOrca (Sub-sampled, (Lian et al., [2023](https://arxiv.org/html/2402.01030v4#bib.bib28))) | |||
| Multi-Turn Conversations | ShareGPT (Sub-sampled, (Anonymous, [2023](https://arxiv.org/html/2402.01030v4#bib.bib2))) | ||||
| Multi-Turn Conversations | ShareGPT (GPT-4, (OpenChat, [2023](https://arxiv.org/html/2402.01030v4#bib.bib35))) | ||||
| Multi-turn Reasoning | CapyBara (LDJnr, [2023](https://arxiv.org/html/2402.01030v4#bib.bib25)) | ||||
| Total | |||||

Comparing CodeActInstruct with Prior Work.
Compared with prior work AgentInstruct (Zeng et al., [2023](https://arxiv.org/html/2402.01030v4#bib.bib71)) and FireAct (Chen et al., [2023a](https://arxiv.org/html/2402.01030v4#bib.bib7)) that mainly focus using text as action, CodeActInstruct results in models that are more practical in real-world implementation, as such models using CodeAct can directly interact with Python interpreters and open-source toolkits (Fig. [3](https://arxiv.org/html/2402.01030v4#S2.F3)), reducing the development effort for action parsing and tool creations.
CodeActInstruct is systematically constructed following the general agent framework (Fig. [2](https://arxiv.org/html/2402.01030v4#S2.F2)).
It covers diverse domains (e.g., compared to FireAct that only considers QA-task and search API), contains quality data (e.g., promotes agent’s capability of self-debug) and of larger size (3.8x / 3.5x more data trajectories and 5x / 19x more tokens compared to AgentInstruct / FireAct respectively in Tab. [4](https://arxiv.org/html/2402.01030v4#S3.T4)).
As we empirically show in Tab. [5](https://arxiv.org/html/2402.01030v4#S3.T5), the resulting model (same backbone) of CodeActInstruct achieves 24% and 119% relative improvement compared to AgentInstruct and FireAct.

CodeActInstruct Can Be Used With Existing Agent-User Conversation Data.
We use a sub-sampled set of OpenOrca (Lian et al., [2023](https://arxiv.org/html/2402.01030v4#bib.bib28)) that focuses on single-turn chain-of-thought (CoT) reasoning, ShareGPT (Anonymous, [2023](https://arxiv.org/html/2402.01030v4#bib.bib2); OpenChat, [2023](https://arxiv.org/html/2402.01030v4#bib.bib35)) from two sources that contain multi-turn conversations between human and LLM, and CapyBara (LDJnr, [2023](https://arxiv.org/html/2402.01030v4#bib.bib25)) that focuses on reasoning in multi-turn conversations.
Statistics and down-sampling details can be found in Tab. [4](https://arxiv.org/html/2402.01030v4#S3.T4) and §[C](https://arxiv.org/html/2402.01030v4#A3).

### 3.2 CodeActAgent

We fine-tune Llama-2 7B (Touvron et al., [2023](https://arxiv.org/html/2402.01030v4#bib.bib51)) and Mistral 7B (Jiang et al., [2023](https://arxiv.org/html/2402.01030v4#bib.bib23)) on a mixture of CodeActInstruct and general conversations (Tab. [4](https://arxiv.org/html/2402.01030v4#S3.T4)) to obtain CodeActAgent.

Training Setup. We perform full-parameter supervised fine-tuning with a sequence length of 4,096 tokens for Llama-2 and 16,384 for Mistral. Please refer to §[D](https://arxiv.org/html/2402.01030v4#A4) for more details.

Evaluation Setup.
We use MINT (Wang et al., [2023e](https://arxiv.org/html/2402.01030v4#bib.bib58)) to evaluate LLMs with CodeAct on a diverse range of agent tasks.
CodeActAgent has some training domains overlapping with MINT’s evaluation (i.e., MINT includes ALFWorld and MATH), hence we report separate numbers for MINT’s in- and out-of-domain performance.
Unless otherwise specified, we measure MINT tasks’ success rates with interaction turn .
We also evaluate out-of-domain agent tasks using text actions from MiniWob++ (computer tasks, (Kim et al., [2023](https://arxiv.org/html/2402.01030v4#bib.bib24))) and ScienceWorld (text-based simulator for elementary science curriculum, (Wang et al., [2022a](https://arxiv.org/html/2402.01030v4#bib.bib54))) to test whether CodeActAgent can generalize to different action formats.
Finally, we include a suite of general LLM evaluation tasks to assess general capability: MMLU (Hendrycks et al., [2020](https://arxiv.org/html/2402.01030v4#bib.bib17)) for knowledge-based QA, HumanEval (Chen et al., [2021](https://arxiv.org/html/2402.01030v4#bib.bib8)) for single-turn code-generation, GSM8K (Cobbe et al., [2021](https://arxiv.org/html/2402.01030v4#bib.bib13)) for single-turn tool-free math reasoning, and MTBench (Zheng et al., [2023](https://arxiv.org/html/2402.01030v4#bib.bib73)) for instruction-following.

CodeActAgent Excels in CodeAct Task.
As shown in Tab. [5](https://arxiv.org/html/2402.01030v4#S3.T5), CodeActAgent (both variants) perform better than all evaluated open-source LLMs on both the in- and out-of-domain subsets of MINT.
On M3ToolEval, we find CodeActAgent (Mistral) outperforms open-source LLMs of similar size (7B and 13B) and even reaches similar performance to those 70B models (Tab. [3](https://arxiv.org/html/2402.01030v4#S2.T3)).
Surprisingly, no improvement is observed for the Llama-2 variant. We discuss potential reasons in §[H](https://arxiv.org/html/2402.01030v4#A8).

CodeActAgent Generalizes to Text Action.
When evaluated on out-of-domain text actions, CodeActAgent (LLaMA2, 7B), which has never been optimized for text action, achieves comparable performance to AgentLM-7B (Zeng et al., [2023](https://arxiv.org/html/2402.01030v4#bib.bib71)) which has explicit tuning for text actions.

CodeActAgent Maintains or Improves the Performance on General LLM Tasks.
In Tab. [5](https://arxiv.org/html/2402.01030v4#S3.T5), we find that CodeActAgent (both variants) performs better on generic LLM tasks we tested, except for a slight degradation on MMLU for CodeActAgent (Mistral, 7B).

Ablation Study.
Tab. [A.8](https://arxiv.org/html/2402.01030v4#A0.T8) presents ablation experiments to determine the importance of CodeActInstruct and general conversations.
Both CodeActInstruct and general conversations contribute to agent tasks, while general conversations are essential to maintain performance on general tasks.

## 4 Related Work

### 4.1 Action Module in LLM Agents

As detailed in (Wang et al., [2023b](https://arxiv.org/html/2402.01030v4#bib.bib53)), LLM-based autonomous agents are typically structured around four components: customized profiles (Park et al., [2023](https://arxiv.org/html/2402.01030v4#bib.bib37); Qian et al., [2023](https://arxiv.org/html/2402.01030v4#bib.bib40)), long-term memory capabilities (Zhu et al., [2023](https://arxiv.org/html/2402.01030v4#bib.bib75); Fischer, [2023](https://arxiv.org/html/2402.01030v4#bib.bib15)), reasoning and planning algorithms (Wei et al., [2022](https://arxiv.org/html/2402.01030v4#bib.bib60); Chen et al., [2023d](https://arxiv.org/html/2402.01030v4#bib.bib11)), and, most crucially, action modules.
The action modules are key to facilitating LLM agents to effectively interact with external entities, including humans (Lee et al., [2022](https://arxiv.org/html/2402.01030v4#bib.bib26)) and tools (Qin et al., [2023a](https://arxiv.org/html/2402.01030v4#bib.bib42)) in the environment (Wang et al., [2023e](https://arxiv.org/html/2402.01030v4#bib.bib58); Yang et al., [2024a](https://arxiv.org/html/2402.01030v4#bib.bib62)).
In this study, we address the critical problem of standardizing the action space for LLM agents.
We further discuss the difference between CodeAct and the line of work that uses code generation for problem-solving in §[A](https://arxiv.org/html/2402.01030v4#A1).
We notice a concurrent study TaskWeaver (Qiao et al., [2023](https://arxiv.org/html/2402.01030v4#bib.bib41)) similarly endorses the use of code. We discuss the principal distinctions in §[B](https://arxiv.org/html/2402.01030v4#A2).

### 4.2 Improving LLM Agents

Two primary methods for enhancing LLM agents are prompt engineering and instruction tuning, as surveyed by (Wang et al., [2023b](https://arxiv.org/html/2402.01030v4#bib.bib53)).
For prompt engineering (Liu et al., [2023a](https://arxiv.org/html/2402.01030v4#bib.bib30)), numerous strategies have been introduced to improve the chain-of-thought reasoning (Wei et al., [2022](https://arxiv.org/html/2402.01030v4#bib.bib60)), including self-consistency-based reasoning (Wang et al., [2022b](https://arxiv.org/html/2402.01030v4#bib.bib55); Chen et al., [2023d](https://arxiv.org/html/2402.01030v4#bib.bib11)) and tree-based approaches (Yao et al., [2023a](https://arxiv.org/html/2402.01030v4#bib.bib68)).
Moreover, LLMs can be strategically prompted to reflect on previous plans (Yao et al., [2023b](https://arxiv.org/html/2402.01030v4#bib.bib69); Wang et al., [2023f](https://arxiv.org/html/2402.01030v4#bib.bib59); Zhang et al., [2023](https://arxiv.org/html/2402.01030v4#bib.bib72)), enabling them to refine initial actions through trial and error.
Contrast to prompt engineering, instruction tuning intrinsically enhances LLMs (Chung et al., [2022](https://arxiv.org/html/2402.01030v4#bib.bib12)), particularly in their agent capabilities (Zeng et al., [2023](https://arxiv.org/html/2402.01030v4#bib.bib71); Chen et al., [2023a](https://arxiv.org/html/2402.01030v4#bib.bib7)).
For effective training, human annotators can curate expert demonstrations for specific agent tasks, such as web browsing (Yao et al., [2022a](https://arxiv.org/html/2402.01030v4#bib.bib66); Nakano et al., [2021](https://arxiv.org/html/2402.01030v4#bib.bib34)).
To minimize human annotation efforts, prior work creates synthetic datasets using stronger LLMs to distill agent capabilities into local models, focusing on tool usage (Qin et al., [2023b](https://arxiv.org/html/2402.01030v4#bib.bib43)), interaction (Chen et al., [2023c](https://arxiv.org/html/2402.01030v4#bib.bib10)), and social skills (Liu et al., [2023b](https://arxiv.org/html/2402.01030v4#bib.bib31)).
CodeActInstruct aligns with the latter approach and creates datasets using stronger LLMs.

## 5 Conclusions

This work introduces CodeAct that employs executable Python code for the LLM agent’s action, which is advantageous over using text or JSON action, especially in complex scenarios. We collect CodeAct-focused multi-turn interaction trajectories CodeActInstruct for instruction tuning, and train CodeActAgent that is specially designed for seamless integration with Python and can execute sophisticated tasks (e.g., model training) leveraging existing Python packages and autonomously rectifying errors through self-debugging.

## Acknowledgement

We thank the anonymous reviewers for their suggestions and comments.
This research is based upon work supported by U.S. DARPA ECOLE Program No. HR00112390060 and U.S. DARPA ITM Program No. FA8650-23-C-7316 and KAIROS Program No. FA8750-19-2-1004. The views and conclusions contained herein are those of the authors and should not be interpreted as necessarily representing the official policies, either expressed or implied, of DARPA, or the U.S. Government. The U.S. Government is authorized to reproduce and distribute reprints for governmental purposes notwithstanding any copyright annotation therein.
This work used the Delta system at the National Center for Supercomputing Applications through allocation CIS230256 from the Advanced Cyberinfrastructure Coordination Ecosystem: Services & Support (ACCESS, Boerner et al. [2023](https://arxiv.org/html/2402.01030v4#bib.bib3)) program, which is supported by National Science Foundation grants #2138259, #2138286, #2138307, #2137603, and #2138296.

## Impact Statement

This paper presents work whose goal is to advance LLM-based autonomous agents that can communicate with humans through natural language and assist human users by performing tasks in environments on behalf of humans. In this section, we discuss potential societal consequences, limitations, and future work related to our work and its goal.

CodeActAgent is an initial prototype of an autonomous agent and still has several practical limitations. For example, it may suffer from hallucination commonly seen in LLMs (e.g., imagine the content of a variable without actually printing it out), suggesting the need for subsequent alignment (Ouyang et al., [2022](https://arxiv.org/html/2402.01030v4#bib.bib36)) for further improvements.

Despite being a prototype, CodeActAgent has already demonstrated limited self-improving capability (e.g., self-debug error messages to improve its action) and the ability to interact with environments.
Future work may build upon CodeActAgent to develop better agents by having them perform extensive interactions within a given environment and iteratively bootstrap their self-improving capability to learn to improve from past mistakes.
More powerful agents, as results of such algorithms, are potentially beneficial for solving a wide range of real-world problems (e.g., theorem proving, drug discovery).
As extensively discussed in (Eloundou et al., [2023](https://arxiv.org/html/2402.01030v4#bib.bib14)), a fully autonomous agent may transform the current landscape of the labor market and impact the jobs of existing workers.

Furthermore, since CodeAct directly grants access for the agent to freely execute code in a sandbox environment, in the worst scenario (e.g., in Sci-Fi movies), such an agent may potentially break free of the sandbox restriction and cause harm to the world through cyber-attack, highlighting the need for future work to design better safety mechanism to safeguard autonomous agents (Tang et al., [2024](https://arxiv.org/html/2402.01030v4#bib.bib49)).

## References

- 
Ahn et al. (2022)
Ahn, M., Brohan, A., Brown, N., Chebotar, Y., Cortes, O., David, B., Finn, C., Fu, C., Gopalakrishnan, K., Hausman, K., Herzog, A., Ho, D., Hsu, J., Ibarz, J., Ichter, B., Irpan, A., Jang, E., Ruano, R. J., Jeffrey, K., Jesmonth, S., Joshi, N., Julian, R., Kalashnikov, D., Kuang, Y., Lee, K.-H., Levine, S., Lu, Y., Luu, L., Parada, C., Pastor, P., Quiambao, J., Rao, K., Rettinghouse, J., Reyes, D., Sermanet, P., Sievers, N., Tan, C., Toshev, A., Vanhoucke, V., Xia, F., Xiao, T., Xu, P., Xu, S., Yan, M., and Zeng, A.
Do as i can and not as i say: Grounding language in robotic affordances.
In *arXiv preprint arXiv:2204.01691*, 2022.
- 
Anonymous (2023)
Anonymous.
Sharegpt dataset.
[https://hf.co/datasets/anon8231489123/ShareGPT_Vicuna_unfiltered/blob/main/ShareGPT_V3_unfiltered_cleaned_split_no_imsorry.json](https://hf.co/datasets/anon8231489123/ShareGPT_Vicuna_unfiltered/blob/main/ShareGPT_V3_unfiltered_cleaned_split_no_imsorry.json), 2023. A dataset containing multi-turn conversations between human and LLM assistant.
- 
Boerner et al. (2023)
Boerner, T. J., Deems, S., Furlani, T. R., Knuth, S. L., and Towns, J.
Access: Advancing innovation: Nsf’s advanced cyberinfrastructure coordination ecosystem: Services & support.
In *Practice and Experience in Advanced Research Computing*, pp. 173–176. 2023.
- 
Bran et al. (2023)
Bran, A. M., Cox, S., White, A. D., and Schwaller, P.
Chemcrow: Augmenting large-language models with chemistry tools.
*arXiv preprint arXiv:2304.05376*, 2023.
- 
Cano et al. (2023)
Cano, A. H., Pagliardini, M., Köpf, A., Matoba, K., Mohtashami, A., Wang, X., Fan, O. S., Marmet, A., Bayazit, D., Krawczuk, I., Chen, Z., Salvi, F., Bosselut, A., and Jaggi, M.
epfllm megatron-llm, 2023.
URL [https://github.com/epfLLM/Megatron-LLM](https://github.com/epfLLM/Megatron-LLM).
- 
Chase (2022)
Chase, H.
LangChain, October 2022.
URL [https://github.com/langchain-ai/langchain](https://github.com/langchain-ai/langchain).
- 
Chen et al. (2023a)
Chen, B., Shu, C., Shareghi, E., Collier, N., Narasimhan, K., and Yao, S.
Fireact: Toward language agent fine-tuning.
*arXiv preprint arXiv:2310.05915*, 2023a.
- 
Chen et al. (2021)
Chen, M., Tworek, J., Jun, H., Yuan, Q., Pinto, H. P. d. O., Kaplan, J., Edwards, H., Burda, Y., Joseph, N., Brockman, G., et al.
Evaluating large language models trained on code.
*arXiv preprint arXiv:2107.03374*, 2021.
- 
Chen et al. (2023b)
Chen, X., Lin, M., Schärli, N., and Zhou, D.
Teaching large language models to self-debug.
*arXiv preprint arXiv:2304.05128*, 2023b.
- 
Chen et al. (2023c)
Chen, Y., Sikka, K., Cogswell, M., Ji, H., and Divakaran, A.
Dress: Instructing large vision-language models to align and interact with humans via natural language feedback.
*arXiv preprint arXiv:2311.10081*, 2023c.
- 
Chen et al. (2023d)
Chen, Y., Sikka, K., Cogswell, M., Ji, H., and Divakaran, A.
Measuring and improving chain-of-thought reasoning in vision-language models.
*arXiv preprint arXiv:2309.04461*, 2023d.
- 
Chung et al. (2022)
Chung, H. W., Hou, L., Longpre, S., Zoph, B., Tay, Y., Fedus, W., Li, Y., Wang, X., Dehghani, M., Brahma, S., et al.
Scaling instruction-finetuned language models.
*arXiv preprint arXiv:2210.11416*, 2022.
- 
Cobbe et al. (2021)
Cobbe, K., Kosaraju, V., Bavarian, M., Chen, M., Jun, H., Kaiser, L., Plappert, M., Tworek, J., Hilton, J., Nakano, R., et al.
Training verifiers to solve math word problems.
*arXiv preprint arXiv:2110.14168*, 2021.
- 
Eloundou et al. (2023)
Eloundou, T., Manning, S., Mishkin, P., and Rock, D.
Gpts are gpts: An early look at the labor market impact potential of large language models.
*arXiv preprint arXiv:2303.10130*, 2023.
- 
Fischer (2023)
Fischer, K. A.
Reflective linguistic programming (rlp): A stepping stone in socially-aware agi (socialagi).
*arXiv preprint arXiv:2305.12647*, 2023.
- 
Gao et al. (2023)
Gao, L., Madaan, A., Zhou, S., Alon, U., Liu, P., Yang, Y., Callan, J., and Neubig, G.
Pal: Program-aided language models.
In *International Conference on Machine Learning*, pp. 10764–10799. PMLR, 2023.
- 
Hendrycks et al. (2020)
Hendrycks, D., Burns, C., Basart, S., Zou, A., Mazeika, M., Song, D., and Steinhardt, J.
Measuring massive multitask language understanding.
In *International Conference on Learning Representations*, 2020.
- 
Hendrycks et al. (2021a)
Hendrycks, D., Basart, S., Kadavath, S., Mazeika, M., Arora, A., Guo, E., Burns, C., Puranik, S., He, H., Song, D., et al.
Measuring coding challenge competence with apps.
In *Thirty-fifth Conference on Neural Information Processing Systems Datasets and Benchmarks Track (Round 2)*, 2021a.
- 
Hendrycks et al. (2021b)
Hendrycks, D., Burns, C., Kadavath, S., Arora, A., Basart, S., Tang, E., Song, D., and Steinhardt, J.
Measuring mathematical problem solving with the math dataset.
In *Thirty-fifth Conference on Neural Information Processing Systems Datasets and Benchmarks Track (Round 2)*, 2021b.
- 
Hong et al. (2023)
Hong, S., Zheng, X., Chen, J., Cheng, Y., Wang, J., Zhang, C., Wang, Z., Yau, S. K. S., Lin, Z., Zhou, L., et al.
Metagpt: Meta programming for multi-agent collaborative framework.
*arXiv preprint arXiv:2308.00352*, 2023.
- Hong et al. (2024) Hong, S., Lin, Y., Liu, B., Liu, B., Wu, B., Li, D., Chen, J., Zhang, J., Wang, J., Zhang, L., Zhang, L., Yang, M., Zhuge, M., Guo, T., Zhou, T., Tao, W., Wang, W., Tang, X., Lu, X., Zheng, X., Liang, X., Fei, Y., Cheng, Y., Xu, Z., and Wu, C. Data interpreter: An llm agent for data science, 2024.
- 
Huang et al. (2023)
Huang, W., Wang, C., Zhang, R., Li, Y., Wu, J., and Fei-Fei, L.
Voxposer: Composable 3d value maps for robotic manipulation with language models.
*arXiv preprint arXiv:2307.05973*, 2023.
- 
Jiang et al. (2023)
Jiang, A. Q., Sablayrolles, A., Mensch, A., Bamford, C., Chaplot, D. S., Casas, D. d. l., Bressand, F., Lengyel, G., Lample, G., Saulnier, L., et al.
Mistral 7b.
*arXiv preprint arXiv:2310.06825*, 2023.
- 
Kim et al. (2023)
Kim, G., Baldi, P., and McAleer, S.
Language models can solve computer tasks.
*arXiv preprint arXiv:2303.17491*, 2023.
- 
LDJnr (2023)
LDJnr.
Capybara dataset.
[https://hf.co/datasets/LDJnr/Verified-Camel](https://hf.co/datasets/LDJnr/Verified-Camel),[https://hf.co/datasets/LDJnr/Pure-Dove](https://hf.co/datasets/LDJnr/Pure-Dove),[https://hf.co/datasets/LDJnr/LessWrong-Amplify-Instruct](https://hf.co/datasets/LDJnr/LessWrong-Amplify-Instruct), 2023. A dataset focusing on reasoning in multi-turn conversations.
- 
Lee et al. (2022)
Lee, M., Liang, P., and Yang, Q.
Coauthor: Designing a human-ai collaborative writing dataset for exploring language model capabilities.
In *Proceedings of the 2022 CHI conference on human factors in computing systems*, pp. 1–19, 2022.
- Li et al. (2023) Li, M., Song, F., Yu, B., Yu, H., Li, Z., Huang, F., and Li, Y. Api-bank: A benchmark for tool-augmented llms, 2023.
- 
Lian et al. (2023)
Lian, W., Goodson, B., Pentland, E., Cook, A., Vong, C., and ”Teknium”.
Openorca: An open dataset of gpt augmented flan reasoning traces.
[https://https://huggingface.co/Open-Orca/OpenOrca](https://https://huggingface.co/Open-Orca/OpenOrca), 2023.
- 
Liang et al. (2022)
Liang, J., Huang, W., Xia, F., Xu, P., Hausman, K., Ichter, B., Florence, P., and Zeng, A.
Code as policies: Language model programs for embodied control.
In *arXiv preprint arXiv:2209.07753*, 2022.
- 
Liu et al. (2023a)
Liu, P., Yuan, W., Fu, J., Jiang, Z., Hayashi, H., and Neubig, G.
Pre-train, prompt, and predict: A systematic survey of prompting methods in natural language processing.
*ACM Computing Surveys*, 55(9):1–35, 2023a.
- 
Liu et al. (2023b)
Liu, R., Yang, R., Jia, C., Zhang, G., Zhou, D., Dai, A. M., Yang, D., and Vosoughi, S.
Training socially aligned language models in simulated human society.
*arXiv preprint arXiv:2305.16960*, 2023b.
- 
Ma et al. (2023)
Ma, Y. J., Liang, W., Wang, G., Huang, D.-A., Bastani, O., Jayaraman, D., Zhu, Y., Fan, L., and Anandkumar, A.
Eureka: Human-level reward design via coding large language models.
*arXiv preprint arXiv:2310.12931*, 2023.
- 
Mialon et al. (2023)
Mialon, G., Dessì, R., Lomeli, M., Nalmpantis, C., Pasunuru, R., Raileanu, R., Rozière, B., Schick, T., Dwivedi-Yu, J., Celikyilmaz, A., et al.
Augmented language models: a survey.
*arXiv preprint arXiv:2302.07842*, 2023.
- 
Nakano et al. (2021)
Nakano, R., Hilton, J., Balaji, S., Wu, J., Ouyang, L., Kim, C., Hesse, C., Jain, S., Kosaraju, V., Saunders, W., et al.
Webgpt: Browser-assisted question-answering with human feedback.
*arXiv preprint arXiv:2112.09332*, 2021.
- 
OpenChat (2023)
OpenChat.
Sharegpt dataset.
[https://hf.co/datasets/openchat/openchat_sharegpt_v3/blob/main/sharegpt_gpt4.json](https://hf.co/datasets/openchat/openchat_sharegpt_v3/blob/main/sharegpt_gpt4.json), 2023. A dataset containing multi-turn conversations between human and LLM assistants. It is filtered to contain data only from GPT-4.
- 
Ouyang et al. (2022)
Ouyang, L., Wu, J., Jiang, X., Almeida, D., Wainwright, C., Mishkin, P., Zhang, C., Agarwal, S., Slama, K., Ray, A., et al.
Training language models to follow instructions with human feedback.
*Advances in Neural Information Processing Systems*, 35:27730–27744, 2022.
- 
Park et al. (2023)
Park, J. S., O’Brien, J., Cai, C. J., Morris, M. R., Liang, P., and Bernstein, M. S.
Generative agents: Interactive simulacra of human behavior.
In *Proceedings of the 36th Annual ACM Symposium on User Interface Software and Technology*, pp. 1–22, 2023.
- 
Pasupat & Liang (2015)
Pasupat, P. and Liang, P.
Compositional semantic parsing on semi-structured tables.
In *Proceedings of the 53rd Annual Meeting of the Association for Computational Linguistics and the 7th International Joint Conference on Natural Language Processing (Volume 1: Long Papers)*, pp. 1470–1480, 2015.
- 
Patil et al. (2023)
Patil, S. G., Zhang, T., Wang, X., and Gonzalez, J. E.
Gorilla: Large language model connected with massive apis.
*ArXiv*, abs/2305.15334, 2023. URL[https://api.semanticscholar.org/CorpusID:258865184](https://api.semanticscholar.org/CorpusID:258865184).
- 
Qian et al. (2023)
Qian, C., Cong, X., Yang, C., Chen, W., Su, Y., Xu, J., Liu, Z., and Sun, M.
Communicative agents for software development.
*arXiv preprint arXiv:2307.07924*, 2023.
- 
Qiao et al. (2023)
Qiao, B., Li, L., Zhang, X., He, S., Kang, Y., Zhang, C., Yang, F., Dong, H., Zhang, J., Wang, L., et al.
Taskweaver: A code-first agent framework.
*arXiv preprint arXiv:2311.17541*, 2023.
- 
Qin et al. (2023a)
Qin, Y., Hu, S., Lin, Y., Chen, W., Ding, N., Cui, G., Zeng, Z., Huang, Y., Xiao, C., Han, C., et al.
Tool learning with foundation models.
*arXiv preprint arXiv:2304.08354*, 2023a.
- 
Qin et al. (2023b)
Qin, Y., Liang, S., Ye, Y., Zhu, K., Yan, L., Lu, Y.-T., Lin, Y., Cong, X., Tang, X., Qian, B., Zhao, S., Tian, R., Xie, R., Zhou, J., Gerstein, M. H., Li, D., Liu, Z., and Sun, M.
Toolllm: Facilitating large language models to master 16000+ real-world apis.
*ArXiv*, abs/2307.16789, 2023b. URL[https://api.semanticscholar.org/CorpusID:260334759](https://api.semanticscholar.org/CorpusID:260334759).
- 
Schick et al. (2023)
Schick, T., Dwivedi-Yu, J., Dessì, R., Raileanu, R., Lomeli, M., Zettlemoyer, L., Cancedda, N., and Scialom, T.
Toolformer: Language models can teach themselves to use tools.
*arXiv preprint arXiv:2302.04761*, 2023.
- 
Shen et al. (2023)
Shen, Y., Song, K., Tan, X., Li, D., Lu, W., and Zhuang, Y.
Hugginggpt: Solving ai tasks with chatgpt and its friends in huggingface.
*arXiv preprint arXiv:2303.17580*, 2023.
- 
Shridhar et al. (2020)
Shridhar, M., Yuan, X., Cote, M.-A., Bisk, Y., Trischler, A., and Hausknecht, M.
Alfworld: Aligning text and embodied environments for interactive learning.
In *International Conference on Learning Representations*, 2020.
- 
Singh et al. (2023)
Singh, I., Blukis, V., Mousavian, A., Goyal, A., Xu, D., Tremblay, J., Fox, D., Thomason, J., and Garg, A.
Progprompt: Generating situated robot task plans using large language models.
In *2023 IEEE International Conference on Robotics and Automation (ICRA)*, pp. 11523–11530, 2023. doi: 10.1109/ICRA48891.2023.10161317.
- 
Surís et al. (2023)
Surís, D., Menon, S., and Vondrick, C.
Vipergpt: Visual inference via python execution for reasoning.
*Proceedings of IEEE International Conference on Computer Vision (ICCV)*, 2023.
- 
Tang et al. (2024)
Tang, X., Jin, Q., Zhu, K., Yuan, T., Zhang, Y., Zhou, W., Qu, M., Zhao, Y., Tang, J., Zhang, Z., et al.
Prioritizing safeguarding over autonomy: Risks of llm agents for science.
*arXiv preprint arXiv:2402.04247*, 2024.
- 
TIOBE Index (2024)
TIOBE Index.
Tiobe index.
[https://www.tiobe.com/tiobe-index/](https://www.tiobe.com/tiobe-index/), Accessed at Jan 23rd, 2024, 2024. The TIOBE Programming Community index is an indicator of the popularity of programming languages. The index is updated once a month. The ratings are based on the number of skilled engineers world-wide, courses and third party vendors.
- 
Touvron et al. (2023)
Touvron, H., Martin, L., Stone, K., Albert, P., Almahairi, A., Babaei, Y., Bashlykov, N., Batra, S., Bhargava, P., Bhosale, S., et al.
Llama 2: Open foundation and fine-tuned chat models.
*arXiv preprint arXiv:2307.09288*, 2023.
- 
Wang et al. (2023a)
Wang, G., Xie, Y., Jiang, Y., Mandlekar, A., Xiao, C., Zhu, Y., Fan, L., and Anandkumar, A.
Voyager: An open-ended embodied agent with large language models.
*arXiv preprint arXiv:2305.16291*, 2023a.
- 
Wang et al. (2023b)
Wang, L., Ma, C., Feng, X., Zhang, Z., Yang, H., Zhang, J., Chen, Z., Tang, J., Chen, X., Lin, Y., et al.
A survey on large language model based autonomous agents.
*arXiv preprint arXiv:2308.11432*, 2023b.
- 
Wang et al. (2022a)
Wang, R., Jansen, P. A., Côté, M.-A., and Ammanabrolu, P.
Scienceworld: Is your agent smarter than a 5th grader?
In *Conference on Empirical Methods in Natural Language Processing*, 2022a. URL[https://api.semanticscholar.org/CorpusID:247451124](https://api.semanticscholar.org/CorpusID:247451124).
- 
Wang et al. (2022b)
Wang, X., Wei, J., Schuurmans, D., Le, Q., Chi, E., Narang, S., Chowdhery, A., and Zhou, D.
Self-consistency improves chain of thought reasoning in language models.
*arXiv preprint arXiv:2203.11171*, 2022b.
- 
Wang et al. (2023c)
Wang, X., Li, S., and Ji, H.
Code4Struct: Code generation for few-shot event structure prediction.
In Rogers, A., Boyd-Graber, J., and Okazaki, N. (eds.), *Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)*, pp. 3640–3663, Toronto, Canada, July 2023c. Association for Computational Linguistics. doi: 10.18653/v1/2023.acl-long.202. URL[https://aclanthology.org/2023.acl-long.202](https://aclanthology.org/2023.acl-long.202).
- 
Wang et al. (2023d)
Wang, X., Peng, H., Jabbarvand, R., and Ji, H.
Leti: Learning to generate from textual interactions.
*ArXiv*, abs/2305.10314, 2023d.
- 
Wang et al. (2023e)
Wang, X., Wang, Z., Liu, J., Chen, Y., Yuan, L., Peng, H., and Ji, H.
Mint: Evaluating llms in multi-turn interaction with tools and language feedback.
*arXiv preprint arXiv:2309.10691*, 2023e.
- 
Wang et al. (2023f)
Wang, Z., Cai, S., Liu, A., Ma, X., and Liang, Y.
Describe, explain, plan and select: Interactive planning with large language models enables open-world multi-task agents.
*arXiv preprint arXiv:2302.01560*, 2023f.
- 
Wei et al. (2022)
Wei, J., Wang, X., Schuurmans, D., Bosma, M., Xia, F., Chi, E., Le, Q. V., Zhou, D., et al.
Chain-of-thought prompting elicits reasoning in large language models.
*Advances in Neural Information Processing Systems*, 35:24824–24837, 2022.
- Xu et al. (2023) Xu, Q., Hong, F., Li, B., Hu, C., Chen, Z., and Zhang, J. On the tool manipulation capability of open-source large language models, 2023.
- 
Yang et al. (2024a)
Yang, J., Prabhakar, A., Narasimhan, K., and Yao, S.
Intercode: Standardizing and benchmarking interactive coding with execution feedback.
*Advances in Neural Information Processing Systems*, 36, 2024a.
- Yang et al. (2024b) Yang, K., Liu, J., Wu, J., Yang, C., Fung, Y. R., Li, S., Huang, Z., Cao, X., Wang, X., Wang, Y., Ji, H., and Zhai, C. If llm is the wizard, then code is the wand: A survey on how code empowers large language models to serve as intelligent agents, 2024b.
- 
Yang et al. (2018)
Yang, Z., Qi, P., Zhang, S., Bengio, Y., Cohen, W., Salakhutdinov, R., and Manning, C. D.
Hotpotqa: A dataset for diverse, explainable multi-hop question answering.
In *Proceedings of the 2018 Conference on Empirical Methods in Natural Language Processing*, pp. 2369–2380, 2018.
- Yang et al. (2024c) Yang, Z., Liu, A., Liu, Z., Liu, K., Xiong, F., Wang, Y., Yang, Z., Hu, Q., Chen, X., Zhang, Z., Luo, F., Guo, Z., Li, P., and Liu, Y. Towards unified alignment between agents, humans, and environment, 2024c.
- 
Yao et al. (2022a)
Yao, S., Chen, H., Yang, J., and Narasimhan, K.
Webshop: Towards scalable real-world web interaction with grounded language agents.
*Advances in Neural Information Processing Systems*, 35:20744–20757, 2022a.
- 
Yao et al. (2022b)
Yao, S., Zhao, J., Yu, D., Du, N., Shafran, I., Narasimhan, K. R., and Cao, Y.
React: Synergizing reasoning and acting in language models.
In *The Eleventh International Conference on Learning Representations*, 2022b.
- 
Yao et al. (2023a)
Yao, S., Yu, D., Zhao, J., Shafran, I., Griffiths, T. L., Cao, Y., and Narasimhan, K.
Tree of thoughts: Deliberate problem solving with large language models.
*arXiv preprint arXiv:2305.10601*, 2023a.
- 
Yao et al. (2023b)
Yao, W., Heinecke, S., Niebles, J. C., Liu, Z., Feng, Y., Xue, L., Murthy, R., Chen, Z., Zhang, J., Arpit, D., et al.
Retroformer: Retrospective large language agents with policy gradient optimization.
*arXiv preprint arXiv:2308.02151*, 2023b.
- 
Yuan et al. (2023)
Yuan, L., Chen, Y., Wang, X., Fung, Y. R., Peng, H., and Ji, H.
Craft: Customizing llms by creating and retrieving from specialized toolsets.
*ArXiv*, abs/2309.17428, 2023. URL[https://api.semanticscholar.org/CorpusID:263310662](https://api.semanticscholar.org/CorpusID:263310662).
- Zeng et al. (2023) Zeng, A., Liu, M., Lu, R., Wang, B., Liu, X., Dong, Y., and Tang, J. Agenttuning: Enabling generalized agent abilities for llms, 2023.
- 
Zhang et al. (2023)
Zhang, C., Liu, L., Wang, J., Wang, C., Sun, X., Wang, H., and Cai, M.
Prefer: Prompt ensemble learning via feedback-reflect-refine.
*arXiv preprint arXiv:2308.12033*, 2023.
- 
Zheng et al. (2023)
Zheng, L., Chiang, W.-L., Sheng, Y., Zhuang, S., Wu, Z., Zhuang, Y., Lin, Z., Li, Z., Li, D., Xing, E., et al.
Judging llm-as-a-judge with mt-bench and chatbot arena.
*arXiv preprint arXiv:2306.05685*, 2023.
- 
Zheng et al. (2024)
Zheng, T., Zhang, G., Shen, T., Liu, X., Lin, B. Y., Fu, J., Chen, W., and Yue, X.
Opencodeinterpreter: Integrating code generation with execution and refinement.
*https://arxiv.org/abs/2402.14658*, 2024.
- 
Zhu et al. (2023)
Zhu, X., Chen, Y., Tian, H., Tao, C., Su, W., Yang, C., Huang, G., Li, B., Lu, L., Wang, X., et al.
Ghost in the minecraft: Generally capable agents for open-world enviroments via large language models with text-based knowledge and memory.
*arXiv preprint arXiv:2305.17144*, 2023.

[2023](https://arxiv.org/html/2402.01030v4#bib.bib27)) and M

3ToolEval.

| Format | Action | 
|---|---|
| CodeAct | AddAgenda(content="Meeting with John", time="2023-10-26 09:00:00") | 
| JSON | {"action": "AddAgenda", "content": "Meeting with John", "time": "2023-10-26 09:00:00"} | 
| Text | Action: AddAgenda, content: Meeting with John, time: 2023-10-26 09:00:00 | 

3ToolEval and existing tool-use evaluation benchmark.

| Benchmark | M 3ToolEval | ToolBench | APIBench | API-Bank | ToolBench | 
|---|---|---|---|---|---|
| (This work) | (Qin et al., [2023b](https://arxiv.org/html/2402.01030v4#bib.bib43)) | (Patil et al., [2023](https://arxiv.org/html/2402.01030v4#bib.bib39)) | (Li et al., [2023](https://arxiv.org/html/2402.01030v4#bib.bib27)) | (Xu et al., [2023](https://arxiv.org/html/2402.01030v4#bib.bib61)) | |
| Requiring multi-turn interaction | ✔ | ✔ | ✗ | ✗ | ✗ | 
| Multiple tools | ✔ | ✔ | ✔ | ✔ | ✔ | 
| Evaluation | Answer Match | LLM Evaluator | AST Tree Match | API-Call Match | Test Case | 
| No dependency on external API ∗ | ✔ | ✗ | ✗ | ✔ | ✗ | 
| Supported API Action Format | CodeAct & JSON & Text | JSON | CodeAct | JSON | CodeAct | 

- 
*
Whether to rely on external API (e.g., RapidAPI, Google Sheet) hosted by a third party. The availability of such third-party APIs can greatly impact evaluation results (e.g., low API-calling performance not because the model is bad but rather because the API required is not accessible). 

## Appendix A Comparison with Work that Uses Code Generation for Problem-solving

In this section, we discuss the fundamental differences between CodeAct and prior work that prompt LLM to generate code for problem-solving.
Existing work have explored using code generation for task-solving in different domains, for example, Code4Struct (Wang et al., [2023c](https://arxiv.org/html/2402.01030v4#bib.bib56)) for structured prediction, PaL (Gao et al., [2023](https://arxiv.org/html/2402.01030v4#bib.bib16)) for math reasoning, Meta-GPT (Hong et al., [2023](https://arxiv.org/html/2402.01030v4#bib.bib20)) for multi-agent collaboration, code-as-policy (Liang et al., [2022](https://arxiv.org/html/2402.01030v4#bib.bib29)) for robot control, ViperGPT (Surís et al., [2023](https://arxiv.org/html/2402.01030v4#bib.bib48)) for visual question answering, Voyager (Wang et al., [2023a](https://arxiv.org/html/2402.01030v4#bib.bib52)) for playing games, Data Interpreter (Hong et al., [2024](https://arxiv.org/html/2402.01030v4#bib.bib21)) for data science tasks, etc.

Most prior work generates code (i.e., a static sequence of actions) in a single-turn setting and cannot dynamically readjust action on new observation: It is considered a failure when the model-generated code fails to solve a task on the first attempt.
This setting overlooks the potential of environmental observation (e.g., code execution results) that might benefit future action and overall decision (e.g., dynamically adjusting subsequent code after observing intermediate code execution results, fixing erroneous code after seeing an error message).
That is, the generated code is a static sequence of actions that cannot be dynamically re-adjusted on the fly by incorporating new observations.
Such a single-turn setting makes it challenging to scale to more challenging problems since even expert human programmers usually cannot write functionally correct code in the first pass.
On the other hand, CodeAct is a multi-turn interaction agent framework that allows dynamic adjustment of prior actions or emitting new actions by design (§[2.1](https://arxiv.org/html/2402.01030v4#S2.SS1), Fig. [2](https://arxiv.org/html/2402.01030v4#S2.F2)) and is compatible with any form of textual observation (e.g., tool execution output, automated feedback) from the environment.
Beyond being compatible with environmental observation, our instruction tuning dataset CodeActInstruct specifically collects data for multi-turn self-improving, offering a practical solution to enhance LLM’s multi-turn self-improving process.

In addition, previous approaches require heavy prompt engineering and crafting of few-shot demonstrations to tailor LLMs to a particular domain or task (e.g., robot control (Liang et al., [2022](https://arxiv.org/html/2402.01030v4#bib.bib29))) since the backbone LLMs are not specially optimized for dynamic planning and decision making.
In contrast, in this work, we propose the CodeAct framework that uses executable Python code to consolidate LLM agents’ actions into unified action space and collect CodeActInstruct on a diverse array of tasks (e.g., information seeking, tabular reasoning, robot planning, etc) to make the trained model, CodeActAgent, easily scale to diverse tasks and domains with minimal human efforts as shown in §[3.2](https://arxiv.org/html/2402.01030v4#S3.SS2).

One notable exception among prior work is Voyager (Wang et al., [2023a](https://arxiv.org/html/2402.01030v4#bib.bib52)), which performs iterative prompting in a constrained action space of function definitions to fix code errors.
Different from CodeAct, such setting disallows dynamic re-adjustment of atomic actions on the fly: In CodeAct, for a particular task (e.g., craft stone sword in Minecraft), the agent can first execute one line of code (any atomic action or composed functions, e.g., move forward, locate stone), and dynamically produce different actions based on the observation of the first action.
This is challenging for Voyager to achieve: Similar to code-as-policy (Liang et al., [2022](https://arxiv.org/html/2402.01030v4#bib.bib29)), they generate action (a skill, e.g., craft stone sword) as a Python function definition that outlines the entire plan for a task (e.g., multi-step code outlining how you should craft a stone sword and handles for different potential cases, which requires strong domain knowledge).
This imposes significant constraints on the agent’s action space and disallows dynamic re-adjustment of atomic actions on the fly: That is, the agent can only generate one complete function first (e.g., by imaging all possible cases that might happen when you try to locate stones), execute the entire function, observe the feedback, and update the entire function as action in the subsequent move.
Besides the constrained ability to re-adjust action from environmental observation, they also rely on heavy prompting engineering (a typical drawback discussed above) to provide relevant information (e.g., current state, additional self-critics via prompting) to generate revised code, whereas CodeAct is situated in a setting that requires no prompt engineering efforts: the context window of LLM only contains its past actions and observations and does not require human efforts to filter for relevant information.

Similar to CodeAct, concurrent work OpenCodeInterpreter (Zheng et al., [2024](https://arxiv.org/html/2402.01030v4#bib.bib74)), with a specific focus on competitive code generation questions, collects code-debugging trajectories to improve an LLM’s iterative code debugging performance. However, its applicability to general LLM agent tasks remains unknown.

## Appendix B Comparison with TaskWeaver

In the landscape of unifying the action space of LLM agents, our work represents a leap over the previous initiative, TaskWeaver (Qiao et al., [2023](https://arxiv.org/html/2402.01030v4#bib.bib41)).
While TaskWeaver deserves acknowledgment for initially integrating code into the action space of LLM agents, its exploration remains limited.
This work, primarily characterized by its reliance on a limited set of qualitative examples with close-sourced models as the backbones, fails to harness the full potential of this integration, remaining merely conceptual demonstrations.
Our work transcends mere conceptualization by conducting an extensive and rigorous analysis, clearly quantifying the benefits of code action within LLM agents.
Beyond this, we introduce a unique instruction-tuning dataset CodeActInstruct specifically designed to amplify the agent’s capabilities in executing code-based actions and an open-source LLM agent CodeActAgent.
These contributions not only extend the work of TaskWeaver but also pave the way for future explorations, offering valuable resources to the open-source community and redefining the potential of LLM agents in practical applications.

## Appendix C General Data Down-sample

- 
•
ShareGPT (Anonymous, [2023](https://arxiv.org/html/2402.01030v4#bib.bib2)): We remove all single-turn conversations, then perform random sub-sample to a desired final number.
- 
•
ShareGPT (GPT-4) (OpenChat, [2023](https://arxiv.org/html/2402.01030v4#bib.bib35)): We do not perform sub-sampling on this dataset.
- 
•
OpenOrca (Lian et al., [2023](https://arxiv.org/html/2402.01030v4#bib.bib28)): We select the CoT subset of OpenOrca, then perform a random sub-sample to a desired final number.
- 
•
CapyBara (LDJnr, [2023](https://arxiv.org/html/2402.01030v4#bib.bib25)): We do not perform sub-sampling on this dataset.

## Appendix D CodeActAgent Training Details

All SFT experiments are performed on one 4xA100 40GB SXM node using a fork of Megatron-LLM (Cano et al., [2023](https://arxiv.org/html/2402.01030v4#bib.bib5)) with a training throughput of around 9k tokens per second. We use chatML format222[https://github.com/openai/openai-python/blob/release-v0.28.0/chatml.md](https://github.com/openai/openai-python/blob/release-v0.28.0/chatml.md) for all multi-turn data, and we only calculate and optimize for loss on the assistant response. We pack short instances into longer ones and apply flash attention for training efficiency.

We train both LLaMA-2 and Mistral LLMs with Tensor Parallel of 4, the learning rate of 1e-5 with 50 warmup steps and cosine decay (end learning rate of 1e-6). We train for five epochs with a batch size of 32. We use the 3rd epoch checkpoint for all our experiments.

## Appendix E Example Prompt for CodeAct

This is an example (zero-shot) system prompt used in a deploy instance of CodeAct where we used chatML format.

The users may optionally include tools descriptions similar to §[F](https://arxiv.org/html/2402.01030v4#A6) or including extra in-context examples similar to §[G.3](https://arxiv.org/html/2402.01030v4#A7.SS3).

## 
Appendix F M3ToolEval Prompt

Each {{...}} component above will be substituted with corresponding information.

### F.1 Example of {{Tool Definition}}

The following is an example tool definition for web-browsing.

### F.2 Example of {{Formatting Instruction}}

Different action format has different formatting instructions.

### F.3 Formatting Instruction for Code as Action

### F.4 Formatting Instruction for Json as Action

### F.5 Formatting Instruction for Text as Action

## Appendix G CodeAct Interaction Data

### G.1 Dataset Downsample

| Domain | Capability | Dataset | # of Instances | 
|---|---|---|---|
| Web Search | Information seeking through search API | HotpotQA (Yang et al., [2018](https://arxiv.org/html/2402.01030v4#bib.bib64)) | 3,000 | 
| Math Reasoning | Math problem-solving using math Libraries in Python (e.g., sympy) | MATH (Hendrycks et al., [2021a](https://arxiv.org/html/2402.01030v4#bib.bib18)) | 5,586 | 
| Code Generation | Self-debug from Python error messages and traceback | APPS (Hendrycks et al., [2021b](https://arxiv.org/html/2402.01030v4#bib.bib19)) | 4,439 | 
| Tabular Reasoning | Tabular Reasoning using pandas and sqlite3 (for SQL) library | WikiTableQuestion (Pasupat & Liang, [2015](https://arxiv.org/html/2402.01030v4#bib.bib38)) | 3,000 | 
| Embodied Planning | Interact with embodied environments through APIs | ALFWorld (Shridhar et al., [2020](https://arxiv.org/html/2402.01030v4#bib.bib46)) | 3,553 | 

- 
•
Code generation tasks in APPS (Hendrycks et al., [2021a](https://arxiv.org/html/2402.01030v4#bib.bib18)): We remove instances without any test case available.
- 
•
Tabular reasoning tasks in WikiTableQuestion (Pasupat & Liang, [2015](https://arxiv.org/html/2402.01030v4#bib.bib38)): We select a subset of 3000 instances with the largest table size (i.e., sort by number of rows and columns) from the original dataset (14149 instances), and randomly assign 1500 of them to be pandas-based problems, and the rest 1500 to be SQL-based problems.
- 
•
Web search tasks in HotpotQA (Yang et al., [2018](https://arxiv.org/html/2402.01030v4#bib.bib64)): We select the 15661 problems labeled as “hard” in the original dataset (with 90447 instances), then randomly down-sample them to 3000 problems.
- •
- 
•
Embodied Planning in ALFWorld (Shridhar et al., [2020](https://arxiv.org/html/2402.01030v4#bib.bib46)): We did not perform down-sampling for AlfWorld.

### G.2 Data Selection Heuristic

Given successful task-solving trajectories that have more than 2 turns, we apply the following heuristic to select instances that can promote the code-as-actions, self-improvement, and instruction-following capabilities of LLM agents:

- 
•
Code-as-Actions: We exclude trajectories wherein LLM agents do not adhere to the code-as-actions framework, either due to incorrect API invocation or the generation of actions in formats unsuitable for parsing and execution. 
- 
•
Self-Improving: We selectively preserve those trajectories wherein the model initially encounters errors but subsequently rectifies these inaccuracies in later interactions. In addition, we eliminate successful trajectories that exclusively yield errors in all code executions. These are deemed ineffective demonstrations, as our objective is to prevent the model from learning to consistently execute erroneous code while still managing to provide correct answers. 
- 
•
Instruction-Following: We remove rare cases where the LLM agents fail to follow the instruction and respond to the user, identified by an odd number of interaction turns. 

After applying all these heuristics, we obtain 6728 trajectories (out of 6985) from gpt-3.5 and claude, and 411 trajectories (out of 413) from gpt-4-0613.

### G.3 Example of Trajectory Generation Prompt

The format of the data generation prompt closely follow MINT (Wang et al., [2023e](https://arxiv.org/html/2402.01030v4#bib.bib58)).

#### G.3.1 Tabular Reasoning (WikiTableQuestion)

We only provide one-shot example for SQL-based tabular reasoning. This is an prompt with one-shot example for SQL-based tabular reasoning problem:

This is an example instruction for Pandas-package-based333[https://pandas.pydata.org/](https://pandas.pydata.org/) tabular reasoning problem:

#### G.3.2 Code Generation (APPS)

Here is an example of the prompt with one in-context example for code generation on the APPS dataset (Hendrycks et al., [2021a](https://arxiv.org/html/2402.01030v4#bib.bib18)) that encourages the LLM to self-debug its solution:

## 
Appendix H CodeActAgent Anomaly on M3ToolEval

In §[3.2](https://arxiv.org/html/2402.01030v4#S3.SS2), we find that despite being fine-tuned with the same mixture of CodeActInstruct and general conversations, CodeActAgent with LLaMA-2 backbone failed to improve performance while Mistral can obtain more than 10% absolute improvement.
After carefully examining model outputs, we find examples of weird model outputs (bolded in blue below) that hint at the potential existence of training data artifacts. We double-checked our training mixture for CodeActAgent and found no match for the generated artifacts, suggesting that these artifacts might have been introduced in the pre-training corpus (Touvron et al., [2023](https://arxiv.org/html/2402.01030v4#bib.bib51)), which we don’t have access to.
Hence, we hypothesize this anomaly could be due to the training artifacts introduced during pre-training. Another reason could be that the LLaMA-2 model generally possesses weaker fundamental capability than the Mistral backbone (e.g., lack of essential knowledge for task completion).
