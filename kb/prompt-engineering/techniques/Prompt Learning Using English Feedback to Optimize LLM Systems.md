---
title: 'Prompt Learning: Using English Feedback to Optimize LLM Systems'
topic: prompt-engineering
subtopic: techniques
secondary_topics:
- evals-observability/evaluation
summary: Explains prompt learning driven by natural-language feedback as an optimization
  loop for LLM systems.
source: arize
url: https://arize.com/blog/prompt-learning-using-english-feedback-to-optimize-llm-systems/
author: Jason Lopatecki; Aparna Dhinakaran; Priyan Jindal; Aman Khan
published: '2025-07-18'
fetched: '2026-07-11T04:52:39Z'
classifier: codex
taxonomy_rev: 1
words: 2889
content_sha256: 3cd197d1405b51b129b676055cdd491f1ef7849e18ba88e11860950c6f2af526
---

# Prompt Learning: Using English Feedback to Optimize LLM Systems

*Co-Authored by Jason Lopatecki, Co-founder and CEO & Aparna Dhinakaran, Co-founder & Chief Product Officer & Priyan Jindal, AI Engineer & Aman Khan, Group Product Manager.*

Applications of reinforcement learning (RL) in AI model building has been a growing topic over the past few months. From Deepseek models incorporating RL mechanics into their training processes to other success stories of RL-based improvement, “AI Twitter” has been ablaze.

As more agents get deployed, a question emerges: can reinforcement learning control systems be built only in prompts? After all, reinforcement learning is all about using real-world feedback to optimize toward a goal, traditionally by adjusting model weights. But prompts themselves are the primary interface for guiding large language models.

We’ve been experimenting with a new approach to optimizing LLM prompts that we’re calling “Prompt Learning” (PL). Unlike traditional optimization methods that rely on numerical scores, PL uses natural language feedback to iteratively improve prompts. The roots of this approach are in the [Voyager paper](https://arize.com/blog/voyager-an-open-ended-embodied-agent-with-llms-paper-reading-and-discussion/) by Jim Fan’s team at NVIDIA. It is also alluded to by Andrej Karpathy in several [recent](https://x.com/karpathy/status/1944435412489171119) [tweets](https://x.com/karpathy/status/1921368644069765486), where he argues prompt-centric learning will be a key technique.

Despite these early inklings, to our knowledge no one has yet rigorously researched, characterized, and measured a full implementation of a reinforcement learning based approach to prompt tuning. That’s exactly what we set out to do.

This implementation is inspired by an idea introduced in the original Voyager paper. The iterative prompting mechanism used in the original Voyager paper as the agent acquires and refines forms the basis for our prompt learning approach.

[Here is the repo](https://github.com/arize-ai/prompt-learning) for this research those who want to dive in deeper or run their own experiments!

💡 Learn more about how[Arize AX supports prompt learning](https://arize.com/docs/ax/prompts/prompt-optimization)

## What Is Prompt Learning?

Prompt learning differs from MetaPrompt prompt optimization in a couple major ways.

First and foremost, the error term is in English and is not a score. The English error term allows for English feedback that is used directly to tune instructions. An explanation from an eval tells you exactly why the evaluation failed and prompt learning then adds instructions to help fix the problem to the system prompt. The English error term allows us to solve a set of problems that are unsolvable by current pure prompt optimization techniques.

Secondly, prompt learning is an online approach to manage your system instructions that is designed to be run continually against your prompt – tuning instructions back into the context. LLM-based systems can assist with context engineering your system instructions.

The English instructions in the prompt context allow for management of instructions, such as how to deal with competing instructions or expiring instructions or human review of instructions, all in English. In our prompt learning meta prompt we even allow keywords where it will only make edits to a specific instructions-based area of the prompt. In “weights” and “gradient”-based prompt optimization approaches, this is nearly impossible.

This implementation of prompt learning uses evaluations, explanations, and annotations on runs of an application to automatically improve your prompt.

The results are promising: prompt learning can make significant levels of improvements, with only one-tenth or one-hundredth the number of labeled examples.

Let’s dive into the mechanics of prompt learning and examine exactly why it’s working.

## What’s the Difference Between Reinforcement Learning and Prompt Learning?

Traditional reinforcement learning relies on using scores or errors to generate gradient error terms, which then update your original model. Each gradient error term pushes your model slightly closer to optimal performance.

![reinforcement learning how it works flow](https://arize.com/wp-content/uploads/2025/07/how-traditional-reinforcement-learning-works.avif)


The key here is that you need many, many examples to align your model. Over time, these myriad examples push your model towards outputting the correct values across your possible inputs. It works by accumulating error gradients and nudging your model in a certain direction.

![rl needs many examples to work](https://arize.com/wp-content/uploads/2025/07/rl-needs-many-examples.avif)


Reinforcement learning is a very powerful technique. But what if you don’t have thousands of examples? What if you have a complex set of goals and those goals don’t easily express as a score? Lastly, what if someone, an annotator or human expert, has relayed to you in English what the problem actually is and how to fix it?

Prompt learning allows you to make powerful changes using individual examples. Instead of gradient error terms calculated for each example, you calculate full text explanations of why an example was scored a certain way. These examples are then fed back into the optimization flow and incorporated into the prompt.

The key idea is:

- The “error”, an Eval explanation OR annotation term is in English
- The modification that changes your actions are done in the prompt context, not weights
- The reward function is an evaluation or human annotation
- The instructions are maintained and managed in the prompt context, allowing instruction management

![json generation example](https://arize.com/wp-content/uploads/2025/07/annotation-json-generation-example.avif)

![example of an evaluation and a metaprompt created instruction to fix to showcase prompt learning](https://arize.com/wp-content/uploads/2025/07/evaluation-explanation-example-json-creation-task-for-prompt-learning-approach.avif)

Our research data shows examples where well known optimization libraries fall short today. Namely, where evals with critiques or annotations contain information not available in the training set on how to fix a failure. There is not an easy way to take information-rich feedback in English and easily feed it back into a gradient update. In general you might not want to do gradient updates at all. Having all of your instructions in English allows you to deal with things that are not easy to do in “weight land,” such as what to do with competing instructions, removal of instructions, compaction of instructions and managing when to expire an instruction — essentially what we call **instruction management**.

One other advantage of prompt learning over gradient based updates is instead of using tens of thousands of examples, you can make changes to your system prompt with a single annotation example.

![prompt learning flow shows difference from rl](https://arize.com/wp-content/uploads/2025/07/prompt-learning-meta-mechanics.avif)

## How Is This Different from Prompt Optimization?

There are a lot of techniques out there for [prompt optimization](https://arize.com/blog/prompt-optimization-few-shot-prompting/). Prompt optimization applies more traditional machine learning train and test approaches to optimizing prompts by gathering examples and attempting to find similarities with those examples.

The seed of the failure of all prompt optimization approaches comes from the focus on scores as the means of propagating failure errors. As you think about failures, not every failure expresses itself easily as a numeric number and a numeric value hides the reason for a failure.

Using a score as your main approach for propagating a failure disconnects the optimization fix from the reason it failed.

| Prompt Learning | Reinforcement Learning | Prompt Optimization | |
| Feedback Mechanism | Evaluation-based English explanations and human annotations | Numeric rewards | Numeric scores |
| Optimization | Metaprompt defines optimization approach | Updating model based on gradients | Varied but some support metaprompts |
| Prompt Control | Can optimize only specific section of prompt (instruction section) | N/A | Typically optimizes whole prompt |
| Online Setup | Designed to be used always on, with human control of “prompt change” acceptance or total automation | Designed to be used online | Normally one off |

## How Does the Optimization Loop Work?

In many real world use cases, as we tested with customers on real data, a single optimization run with a single shot output worked great. In cases where you need multiple loops over the optimization to improve performance, the English explanation (or critique) output of an Evaluator can improve performance.

![](https://arize.com/wp-content/uploads/2025/07/prompt-learning-optimization-loop.avif)


The English explanation (Critique) is an important feature of our evaluation library, generating an explanation then allows the results to be used in a feedback loop.

In our testing, as the model was required to add more instructions back into the context window to fix the prompt, the iterative loop became more important. In cases where only 1-10 instructions needed to be added a single meta-prompt improvement loop was sufficient.

## How Did We Test Prompt Learning?

We ran a series of optimization experiments using prompt learning in order to benchmark its efficacy. To date, this has been run across a sizable production set of AI application and agent use cases:

For our demo data application, we chose a JSON generation problem where models had to generate JSON for a webpage based on natural language prompts.

We additionally generated a set of latent rules that the responses needed to follow. Things like:

- Every section needs a type value from a predefined list
- All images must include alt text
- All external asset links must use https

These rules were implicitly represented in feedback and explanations attached to a set of traces of our application.

We designed this test to mimic a typical evaluation cycle of an agent. Evaluation was done using a mixture of [LLM-as-a-judge techniques](https://arize.com/llm-as-a-judge/) with human review, again to mimic real world patterns.

All of this data (the application traces, feedback, and explanations) was then fed into the optimization stage.

To perform the optimization itself, we used a modified version of meta-prompting that we later dubbed **prompt learning**.

![](https://arize.com/wp-content/uploads/2025/07/prompt-learning-annotator.avif)


## How Does Prompt Learning Perform?

We tested prompt learning on real world customer deployments, internal synthetic data instruction learning tests, and well known benchmarks like [Big Bench Hard](https://huggingface.co/datasets/maveriq/bigbenchhard).

### Instruction Learning

The following are results from our rules based instruction learning data set. The dataset was designed to test tasks that are impossible to solve without learning from information provided from outside of the training data.

The task design is as follows:

- There is a JSON generation where the JSON is designed to control the rendering of a website (real world customer use case)
- There are a number of business rules unknown to the LLM that it must follow
- There are annotators that annotate mistakes, where it did not follow the rule
- The *prompt learning*loop must pick up the rules and modify the prop to capture enough rules to pass the*evaluation*
- We test with a number of rules and all rules must pass to get a “full pass,” a single rule fails the test

This test attempts to assess how well the system can pick up information from feedback and formalize them into a new system prompt. Most of these tests will have 0 for accuracy prior to optimization.

Feedback can be human driven, evaluation driven or real world feedback driven.

These rules based critiques also challenge most prompt optimization systems whose only feedback mechanism is a scalar error term. Almost all prompt optimization techniques fail on this test today.

| Ruleset size | Accuracy – Unoptimized Prompt | Accuracy: 1-Loop | Accuracy: 5-Loop | Latency |
| 10 | 0% | 84% | 100% | 1084.12s |
| 50 | 0% | 66% | 82% | 1150.45s |
| 100 | 0% | 42% | 67% | 1294.27s |

*Table 1: Initial Results Rules Task*

The above results show that as you grow rules the test gets harder and the prompt needs to learn 100s of rules to generate correct JSON. It takes multiple iterations to get the prompt right to pass the rules.

![](https://arize.com/wp-content/uploads/2025/07/prompt-learning-results.avif)

The rules determine how many instructions the AI agent must adhere to in order to pass, all these rules need to be picked up through the feedback paths.

### Big Bench Hard

Prompt learning was tested against Big Bench Hard (BBH) with GPT-4.1 as the model under test (gpt-4.1-2025-04-14) and GPT-4o as the evaluation model.

There is no handcrafted prompt for each test, only a simple evaluation prompt; the actual prompt is learned from the evaluation results in an iterative fashion.

The results consistently show an improvement over baseline with the result below showing a 10% improvement on what is a highly saturated benchmark.

The BBH was run with 50 random samples, with 1 loop of iteration. We ran a selection of the BBH tests, a number of tests had issues that were not fixed by publication time and are not included.

![](https://arize.com/wp-content/uploads/2025/07/prompt-learning-big-bench-hard-results-textpro.avif)

The Final GT is the final prediction measured relative to the ground truth. The ground truth is not used in the prompt learning loop, in the spirit of Big Bench, only to test against in the final check.

The Init GT is the initial measurement against ground truth with no prompt.

The data is split 50 / 50 split testing 50 samples on each. The initial test data is a different random sample from the final test data.

What we found in our testing of the current public models is that they are so attuned to the benchmark that many times any small prompt change at all actually lowered the benchmark. This is a well known benchmark but the question of saturation of results is very real.

## Differences From RL Training

In typical gradient based training most gradient based updates will improve your training scores. In prompt learning, that is not guaranteed, it does in practice for most loops but we have found running for long enough can affect your training scores. The reason is training is not a gradient update but a best attempt to fix a prompt problem, that best attempt might or might not work.

This is not the typical case but the following can happen:

- Training results can drop after a run
- Test results can be higher than training

We leveraged o3 to analyze the failures of the prompt optimization runs looking at raw data and prompt changes.

![](https://arize.com/wp-content/uploads/2025/07/explanations-o3.avif)

![](https://arize.com/wp-content/uploads/2025/07/when-optimizing-principles.avif)

## Speed of Library

In our tests, the major benchmark harness runs took over +24 hours. Where a run through Big Bench Hard of Arize Phoenix is around 30minutes. The library design makes prompt iteration runs about 10-100x faster than the current ecosystem.

## More On Prompt Learning

Prompt learning presents a compelling approach for continuous improvement of AI applications, and its ability to drive results with relatively few examples make it suitable for both early stage and production applications.

For more on our prompt learning experiments, check back for the pending publication a long research paper.

## Appendix

### Literature Review

There have been a number of approaches that are relevant worth noting

- [Promptbreeder](https://arxiv.org/abs/2309.16797)(DeepMind)- Prompt edits but no english critiques

- [OPRO – “LLMs as Optimizers”](https://arxiv.org/pdf/2309.03409)- Prompt edits but no english critiques

- [PromptAgent](https://arxiv.org/abs/2310.16427)- Uses free-form critiques to decide edits, though the final prompt doesn’t embed the critiques—search happens in an external planner instead of accumulating rules inside the prompt.
- No management of English instructions

- [StablePrompt](https://arxiv.org/abs/2410.07652)- RL updates instead of prompt edits

- [Meta-Prompting: Task-Agnostic Scaffolding](https://arxiv.org/abs/2401.12954)- First use of metaprompt but doesn’t use english critiques or explanations

- [Critic-RM](https://arxiv.org/abs/2411.16646)– Self-Generated Critiques Boost Reward Modeling
- [Self-Refine: Iterative Refinement with Self-Feedback](https://arxiv.org/abs/2303.17651)
- [Self-Generated Critiques Boost Reward Modeling for Language Models](https://arxiv.org/abs/2411.16646)- Critique is used to help reward model learn, designed for downstream RL use


### Comparing Prompt Learning To PromptAgent

Here is a comparison between prompt learning and PromptAgent. Monte Carlo tree search (MCTS)-based search for optimal prompts, like that in PromptAgent, could be combined with prompt learning in future work.

**PromptAgent (ICLR ’24) vs. Arize Prompt Learning (PL)**

| Dimension | PromptAgent | Prompt Learning (PL) |
| Objective | Find a single“expert-level” prompt that maximises a numeric task score on a dev set. | Continuouslymaintain a production prompt so that it self-heals when evals or users uncover new failure modes. |
| Optimizer | MCTSover the space of prompt edits; each node = a prompt, each edge = an edit derived from error feedback.[ arXiv](https://arxiv.org/abs/2310.16427) | A meta-prompt controllerreads the latest English critique and decides how to mutate anInstruction block(add, merge, rewrite, expire). No roll-outs or search tree. |
| Update granularity | Edits the entiretask prompt during search; final prompt is frozen after the run. | Edits only the Instruction sectioninside a fenced region; other parts of the system prompt stay intact. |
| Use of critiques | Generates “constructive error feedback” to guide the next MCTS action, but the literal text is not keptin the final prompt.[ arXiv](https://arxiv.org/abs/2310.16427) | Primary signal.English critique (from LLM judge or human) feeds the meta-prompt; controller extracts intent and rewrites/merges instructions. Critique itself isnot stored, but its meaning is distilled into the instruction set. |
| Conflict / lifecycle management | None once search ends; prompt can contain redundant or stale rules that an operator must prune manually. | Built-in: controller can deduplicate, version, or expireinstructions and supports human approval gates before applying changes. |
| Online vs. offline | Offline: heavy search (hundreds–thousands of roll-outs), then deployment. | Online: one extra LLM call whenever a failure appears; designed to run forever alongside the app. |
| Data requirement | Needs a moderate-sized scored devset to evaluate roll-outs. | Works with single examplesbecause each explanation is information-rich; leverages existing eval traces or human annotations. |
| Compute cost | Front-loaded (search); negligible at inference. | Minimal upfront, <1 extra call per optimisation; prompt grows by only the net instruction text. |
| Interpretability | Final prompt readable, but the reasoning path is hidden in search logs. | Full audit trail: every instruction edit is plain English; easy diff & rollback. |
| Typical sweet spot | Boot-strapping newtasks where you can afford an offline optimisation pass. | Long-lived agents that must obey evolving policy & domain ruleswith scarce labelled data. |
