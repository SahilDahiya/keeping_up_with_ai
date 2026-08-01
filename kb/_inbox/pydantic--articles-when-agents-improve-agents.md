---
title: 'When agents improve agents: loops that improve themselves'
kind: blog
topic: null
subtopic: null
secondary_topics: []
summary: null
triage: null
skip_reason: null
source: pydantic
url: https://pydantic.dev/articles/when-agents-improve-agents
author: David Sanchez
published: '2026-07-31'
fetched: '2026-08-01T06:55:10Z'
classifier: null
taxonomy_rev: 2
words: 1435
content_sha256: fa87dd7e69a315f094b9a8390cca0fea05ac957ca504641d58b5df5e310805f7
---

# When agents improve agents: loops that improve themselves

This post is part of a 3-part series. [Part two](https://pydantic.dev/articles/when-agents-build-agents) built a loop that assembles its own agents and tools. This one is about the last move: a loop that doesn't just run, but gets better after every run.

What separates the two? A loop that improves has to keep going until the goal is actually met, not until it runs out of plan. And when it grades itself, the judge has to be one we trust, because an agent scoring its own work is happy to be done early.

## 

When an agent finishes today, it just... goes idle. It has pushed the change or written the answer, and it goes quiet. Whether the tests pass, whether a reviewer replies, whether the build went red: none of it reaches the agent. It finished because it ran out of plan, not because the goal was met.

So the reaction lives somewhere else. A control plane watches the outside world, CI, review threads, the state of a pull request, and starts a fresh run when something changes. We run one of these on [Pydantic AI](https://github.com/pydantic/pydantic-ai) itself: the control plane has opened 65 pull requests and gotten 22 merged, and its "keep going" lives in a cron that re-reads GitHub and dispatches a new one-shot agent. The loop is real, but it sits outside the agent.

A loop that improves moves that check inside. When the agent would go idle it does not just stop. It asks, with a model and not a fixed rule, what the goal was, whether it implemented it, whether it verified it, whether it verified the verification, whether the build is green, whether anyone commented, and then decides whether there is really nothing left to do. [The first post](https://pydantic.dev/articles/what-makes-a-good-harness#a-good-harness-steers) reduced this to a test: every time a human types "continue," the harness failed to say what continuing meant. A loop that improves says it to itself.

None of that is a switch you flip today. The pieces to build it are already there. An [output guardrail](https://pydantic.dev/docs/ai/harness/guardrails/) can return a `retry` verdict that hands the work back to the model to redo, and [Macroscope](https://pydantic.dev/docs/ai/harness/macroscope/) lets the agent run a real code review on its own change, treat the findings as untrusted, confirm each against the file, and fix the ones that hold up. What is not yet one primitive is the check that runs at the edge of idle and decides continue or done. That is the piece still missing a name.

## 

To get better, a loop has to remember what it did, which is exactly where part two ended: it wanted each sub-agent's history to be something the rest of the loop could search on demand, and called that a frontier no harness shipped. Since then, part of it shipped.

[Conversation search](https://pydantic.dev/docs/ai/harness/conversation-search/) gives the model one tool, `search_conversation_history`, that runs a BM25 search over every run a shared store has persisted, across sessions and across agents. An agent can look up what another one already tried, the tool calls it made, the reasoning it wrote, the way it failed, and skip the dead end. [Memory](https://pydantic.dev/docs/ai/harness/memory/) adds a notebook that survives the run.

The frontier is not all here. The search spans the whole store, not a rank, so a sub-agent cannot yet be handed only the histories at or below its own level; scope is still all-or-one-conversation. The substrate ships, the access control is next.

Recall is two capabilities sharing one store: one writes each run, the other reads it back.

```
import logfire
from pydantic_ai import Agent
from pydantic_ai_harness.conversation_search import ConversationSearch, SnapshotHistorySource
from pydantic_ai_harness.step_persistence import SqliteStepStore, StepPersistence
logfire.configure()
logfire.instrument_pydantic_ai()
store = SqliteStepStore(database='sessions.db')
agent = Agent(
    'anthropic:claude-opus-4-8',
    capabilities=[
        StepPersistence(store=store),                      # write each run to the store
        ConversationSearch(SnapshotHistorySource(store)),  # search_conversation_history over all of it
    ],
)
```
## 

Remembering runs only helps if you can tell the good ones from the bad. So the loop grades itself: an evaluator reads an output and says pass or fail, and the loop keeps a change only when the grade goes up. The catch is that the evaluator is a model too, and models are unreliable graders.

The failure is well documented. Swap the order of two answers and an LLM judge will often flip its verdict on the same pair, favoring whichever it saw first.<sup>[1](https://pydantic.dev#user-content-fn-1)</sup> If you ask it twice, it can disagree with itself. Show it its own output next to another model's and it tends to prefer its own.<sup>[2](https://pydantic.dev#user-content-fn-2)</sup> A judge can be perfectly consistent and still be wrong, so "the numbers went green" is not the same as "the work got better."

So a loop that grades itself has to check the grader too, not just the work. That is what "did we verify the verification?" was doing back in the first section: if the judge is biased, a loop that optimizes against it only learns to satisfy the bias. The defense is the boring, human part of evals: calibrate the judge against a person who knows the domain, grade one dimension at a time instead of asking for a single score, prefer a plain pass or fail over a five-point scale, and randomize order so position cannot decide the winner.<sup>[3](https://pydantic.dev#user-content-fn-3)</sup> And version the rubric, because the criteria drift as you learn what you are really grading, and a rubric that changes without a version is a judge that drifts without a trace.[4](https://pydantic.dev#user-content-fn-4)

## 

Keep going until the goal is met, remember your runs, grade them with a judge you calibrated, and you have what you need to improve. The last piece is somewhere to run that on real traffic, without redeploying every time it learns something. That is what [Pydantic Logfire](https://pydantic.dev/logfire) is for. Three parts of it matter here:

- [Managed prompts](https://pydantic.dev/docs/logfire/manage/managed-variables/) change an agent's instructions without a deploy. Versioned, so an improvement can go live and be rolled back like any other change.
- [Online evaluations](https://pydantic.dev/docs/ai/evals/online-evaluation/) run your evaluators in the background on live, sampled traffic, so the grade comes from production, not a static test set that stops being representative the day you write it.
- [GEPA](https://pydantic.dev/articles/prompt-optimization-with-gepa) is the recipe that ties them together: the model reflects on its eval failures and proposes a better prompt, and you keep the version that measurably wins.

None of this is the science-fiction version, an agent silently rewriting itself in production. [Logfire](https://pydantic.dev/logfire)'s optimizer already reads eval failures and proposes a better prompt, and can run on a schedule instead of waiting to be asked. What it will not do is apply the change on its own: closing that loop without a person is the part still near-horizon. What ships today is every piece you need to build the loop by hand: behavior you can change safely, evals that run where the users are, and a way to turn failures into better prompts, with a person still deciding what "better" means.

## 

Three posts, one arc. A model predicts tokens. An agent wraps it in a loop of tool calls. A harness makes that loop reliable by getting the right context to the model at the right moment. A loop of agents builds its own structure and outlives the run. And a loop that can see its runs, keep going until the goal is met, and grade itself with a judge it has calibrated can start to get better on its own.

The frontier is still in view: history scoped by rank, a check that fires at the edge of idle, an optimizer that applies its own proposals. None of it is magic, and all of it is closer than it was three posts ago.

This is the third and last post in the series. Every piece is in the [Harness](https://pydantic.dev/docs/ai/harness/): wire step persistence to conversation search, put an output guardrail on the result, and watch the loop grade itself on one Logfire trace.

## 

## Footnotes

1. 
Peiyi Wang et al., ["Large Language Models are not Fair Evaluators"](https://aclanthology.org/2024.acl-long.511/) , ACL 2024. Swapping the order of two candidates can flip the verdict; they propose swap-and-average calibration.[↩](https://pydantic.dev#user-content-fnref-1)
2. 
Lianmin Zheng et al., ["Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena"](https://arxiv.org/abs/2306.05685) , NeurIPS 2023. The foundational LLM-as-judge study; names position, verbosity, and self-enhancement bias.[↩](https://pydantic.dev#user-content-fnref-2)
3. 
Anthropic, ["Demystifying Evals for AI Agents"](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents) (calibrate against experts, grade each dimension in isolation, evals as CI); Hamel Husain,["Using LLM-as-a-Judge"](https://hamel.dev/blog/posts/llm-judge/) (binary over Likert, align to one expert, measure true-positive and true-negative rates).[↩](https://pydantic.dev#user-content-fnref-3)
4. 
Shreya Shankar et al., ["Who Validates the Validators? Aligning LLM-Assisted Evaluation of LLM Outputs with Human Preferences"](https://arxiv.org/abs/2404.12272) , UIST 2024. Evaluation criteria drift as reviewers grade, so the rubric has to be versioned and re-aligned, not frozen.[↩](https://pydantic.dev#user-content-fnref-4)
