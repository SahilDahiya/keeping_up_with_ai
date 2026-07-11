---
title: Evaluating AI Agent Skills
topic: evals-observability
subtopic: evaluation
secondary_topics:
- agents/tool-use
summary: Explains how to evaluate AI agent skills, including task design, scoring,
  trace inspection, and regression testing for reusable agent capabilities.
source: langfuse
url: https://langfuse.com/blog/2026-02-26-evaluate-ai-agent-skills
author: null
published: '2026-02-26'
fetched: '2026-07-11T04:36:11Z'
classifier: codex
taxonomy_rev: 1
words: 1651
content_sha256: 4646905f559e8ffaf01297bd7f7d5d10a6e65bce0cce29bbbdea537e3bf00773
---

# Evaluating AI Agent Skills

# Evaluating AI Agent Skills

How we used Langfuse datasets, tracing, and the cloud agent SDK to iteratively evaluate and improve our AI agent skill.

![Picture Lotte Verheyden](https://langfuse.com/_next/image?url=%2Fimages%2Fpeople%2Flotteverheyden.jpg&w=96&q=75) Lotte Verheyden

Lotte Verheyden![Using Langfuse to Evaluate AI Agent Skills](https://langfuse.com/_next/image?url=%2Fimages%2Fblog%2F2026-02-26-evaluate-ai-agent-skills%2Fog.jpg&w=3840&q=75)


We built an [AI agent skill for Langfuse](https://github.com/langfuse/skills/tree/main/skills/langfuse) so agents can use Langfuse: access the API via the CLI, look up documentation, follow observability best practices. But **how do you know the agent actually uses the skill correctly?** And when you change the skill, how do you know it got better and not worse? We used Langfuse to find out.

[The Evaluation Setup](https://langfuse.com#the-evaluation-setup)

You can evaluate a skill systematically by storing a list of user prompts as a [Dataset](https://langfuse.com/docs/evaluation/experiments/datasets) in Langfuse, [run an experiment](https://langfuse.com/docs/evaluation/experiments/experiments-via-sdk) by spinning up coding agents with these prompts, and [tracing](https://langfuse.com/docs/observability/overview) the agent's behavior. Based the results, you can improve the skill and measure the quality by running the pipeline again.

![Evaluation pipeline](https://langfuse.com/_next/image?url=%2Fimages%2Fblog%2F2026-02-26-evaluate-ai-agent-skills%2Fevaluation-pipeline.png&w=3840&q=75)


This approach treats skill evaluation like prompt evaluation: define inputs, capture behavior, score the output, and iterate. OpenAI describes a [similar loop for Codex skills](https://developers.openai.com/blog/eval-skills/), using JSONL traces and deterministic graders. The core idea is the same: make skill quality measurable so you can improve it systematically.

[The dataset](https://langfuse.com#the-dataset)

We created 2 datasets:

| Dataset | Description |
|---|---|
| cli-tests | A set with user prompts where the agent should use the CLI to access Langfuse. |
| instrumentation-tests | A set with the same user prompt `"instrument my application with Langfuse"`every time, and a folder name that points to a folder with a small existing application. |

The expected output is a list of things the LLM as a judge should verify.

[Experiment setup](https://langfuse.com#experiment-setup)

We used Claude Agent SDK to run the agents. You can easily integrate Langfuse with Claude Agent SDK by following [this integration guide](https://langfuse.com/integrations/frameworks/claude-agent-sdk).

Want to follow along? The full code for this evaluation setup is available in [this example repository](https://github.com/langfuse/langfuse-examples/tree/main/applications/evaluating-ai-agent-skills).

**Repository structure**

The [repository](https://github.com/langfuse/langfuse-examples/tree/main/applications/evaluating-ai-agent-skills) consists of the script to run the experiment, and repositories to spin up the agents. The skill is intalled globally on the Claude account.

**Spinning up an agent**

Each experiment run spins up an agent inside a test repository. A couple of things to note:

**Injecting context**

The **Langfuse credentials** are injected as environment variables so the agent can interact with the API and the CLI out of the box.

The **Langfuse skill** is installed globally on the Claude account, so we need to set `setting_sources=["user", "project"]` in ClaudeAgentOptions to give the agent access to the global skill.

**Permissions** are set to `bypassPermissions` to avoid the agent getting stuck waiting for user input.

```
options = ClaudeAgentOptions(
        max_turns=args.max_turns,
        cwd=item_cwd,
        permission_mode="bypassPermissions", # we don't want the agent to be stuck asking for permissions
        setting_sources=["user", "project"],
        stderr=lambda line: stderr_lines.append(line),
        env=_load_agent_env(item_cwd),
    )
```
**Resetting the repository**

After each run, the repository is reset to its original state so the next run starts from a clean slate. This is especially important for the instrumentation dataset, where the agent modifies application code: you want every run to start from the same baseline.

**Tracing the agent**

The agent's behavior is [traced to Langfuse](https://langfuse.com/integrations/frameworks/claude-agent-sdk), which gives us a full record of every tool call, CLI command, and file edit.

[The Langfuse Skill](https://langfuse.com#the-langfuse-skill)

The [Langfuse skill](https://github.com/langfuse/skills/tree/main/skills/langfuse) gives AI agents two core capabilities: **programmatic API access** via the [Langfuse CLI](https://langfuse.com/blog/2026-02-13-will-you-be-my-cli), and **documentation retrieval** via llms.txt, page fetching, and search. You can read more about the skill in [this Valentine's Day blog post](https://langfuse.com/blog/2026-02-13-will-you-be-my-cli) and [this post about automatic prompt improvement](https://langfuse.com/blog/2026-02-16-prompt-improvement-claude-skills).

At the time of writing, we also have separate skills for more specific use cases like prompt migration and instrumenting existing code. The goal is to eventually merge these into the main Langfuse skill so users only need to install one.

[Improving the Skill](https://langfuse.com#improving-the-skill)

Before knowing what to improve, we need to look at the traces of the first dataset run. This is what a trace from a Claude Agent SDK run looks like:

![Trace example](https://langfuse.com/_next/image?url=%2Fimages%2Fblog%2F2026-02-26-evaluate-ai-agent-skills%2Ftrace-example.png&w=3840&q=75)


You can immediately see that the skill was invoked relatively early in the trace, which is a good sign. Going deeper into each step reveals more about the agent's behavior. A couple of things immediately stand out:

- A high number of CLI commands resulted in an error.
- Sometimes the agent would switch to using Curl commands instead of the CLI.
- The agent would sometimes invent CLI resources and actions that didn't exist.
- The agent would sometimes not use the skill at all.

From these observations we derived **initial metrics to track each iteration**: the number of CLI errors per run, the number of retries before succeeding, and whether the agent fell back to Curl or skipped the skill entirely. Once the CLI usage is solid, we can move on to more advanced questions, like whether the [agent is actually following best practices when it instruments an application](https://langfuse.com#evaluating-auto-instrumentation).

[Iteration 1: Not enforcing Langfuse URL](https://langfuse.com#iteration-1-not-enforcing-langfuse-url)

The first experiment run showed the same pattern in over 90% of the cases: the agent would check if credentials were set, use a CLI command and then get the error `No server URL found`. At some point it would attempt a workaround by explicitly setting the server with `--server` instead of using the environment variable. This behavior would introduce 1-2 unnecessary round trips to the CLI.

The root cause was in the skill itself. In our example showing how to set environment variables, we had a comment saying the Langfuse host was optional.

```
export LANGFUSE_PUBLIC_KEY=pk-lf-...
export LANGFUSE_SECRET_KEY=sk-lf-...
export LANGFUSE_BASE_URL=https://cloud.langfuse.com
```
By changing that one comment to say the host is mandatory, the agent started checking for it upfront and setting it when missing. The number of retries for that specific error went to zero immediately. You can see the before and after in [this commit](https://github.com/langfuse/skills/pull/4/changes/904a0ff1a6b9d4e4cc66ae26eb38d193a53d958b).

[Iteration 2: Hallucinated CLI parameters](https://langfuse.com#iteration-2-hallucinated-cli-parameters)

With the server issue fixed, a second pattern stood out: the agent would invent CLI resources and actions that didn't exist.

```
> npx langfuse-cli api prompts get --name summarizer
Exit code 1
error: unknown option '--name'
```
The CLI has `--help` at every level to let you discover what's available, but the agent only used it after experiencing an error. It didn't use it proactively. This caused an avg error rate of 25% on Langfuse CLI commands.

[Adding explicit instructions to the skill telling the agent to always use  --help to discover what's available](https://github.com/langfuse/skills/pull/5/changes/a1b3f710ed2ebcc9b9bd729b73c86ee12d3bcfba) brought Langfuse CLI errors down to zero.

Interesting to note here is that the number of actions the agent needed didn't actually decrease. The retries were gone, but replaced by `--help` calls before each command. No errors is better than constant retries, but the efficiency gap tells us where to invest next: surfacing more information at the top level of the CLI so the agent needs fewer discovery steps.

[Iteration 3: Skill invocation issues](https://langfuse.com#iteration-3-skill-invocation-issues)

Now it was time to move on to the second goal: folding observability best practices into the main skill. We added a new reference doc with instrumentation guidance and rewrote the main SKILL.md to be more conceptual by framing the skill as "use Langfuse effectively" instead of just listing the CLI and docs access.

| Description | |
|---|---|
| Before | Interact with Langfuse and access its documentation. Use when needing to (1) query or modify Langfuse data programmatically via the CLI — traces, prompts, datasets, scores, sessions, and any other API resource, (2) look up Langfuse documentation, concepts, integration guides, or SDK usage, or (3) understand how any Langfuse feature works. This skill covers CLI-based API access (via npx) and multiple documentation retrieval methods. |
| After | Skill for working with Langfuse effectively across use cases: instrumentation, prompt management, debugging, and data access. Includes core principles, workflows, and use-case-specific best practices. |

The result was that the skill stopped being invoked entirely. User prompts like "fetch the last ten traces," which had worked before, now led the agent to look for logs in a local repository, or reach for a competitor product instead of Langfuse. The skill wasn't even being considered.

After some iterations we settled onto a very similar description as before, but with the new reference doc added. [This commit](https://github.com/langfuse/skills/pull/6/changes/a3bebd7fda7931864706bf23cef1861890f697bd) shows the before and after.

[Iteration 4: Evaluating auto-instrumentation](https://langfuse.com#evaluating-auto-instrumentation)

How do you evaluate whether the outcome of a complex task is correct? We did the following to verify whether the agent could correctly instrument an existing application with Langfuse observability:

This requires a slightly different evaluation setup. Each Claude Agent SDK run starts with the same prompt, but in a different subfolder, containing a small existing application. One folder might have a basic OpenAI chat app, another a LangChain RAG pipeline. The dataset input and expected output are adjusted accordingly.

![Observability dataset](https://langfuse.com/_next/image?url=%2Fimages%2Fblog%2F2026-02-26-evaluate-ai-agent-skills%2Fobservability-dataset.png&w=3840&q=75)


This is where [LLM-as-a-judge](https://langfuse.com/docs/evaluation/evaluation-methods/llm-as-a-judge) becomes useful. Checking whether instrumentation is correct can't be done by string match. An LLM judge can compare the agent's changes against the expected output and score whether the instrumentation is correct.

[Takeaways](https://langfuse.com#takeaways)

A few things learned from the process:

- **The devil is in the details.**A single comment saying "optional" instead of "mandatory" caused consistent failures across every test case.
- **Be explicit about the value of the skill.**When we made the skill description more abstract, the agent stopped recognizing when to use it. Specific keyword matching is super important.
- **Manual trace review is very valuable.**The numbers tell you something is wrong, but stepping through individual traces is how you find out why.

[What's Next](https://langfuse.com#whats-next)

There's more to improve. A couple of things to consider:

- adding specific best practices under the `references`folder. This comes with specific datasets to test the skill against.
- improving the efficiency of the skill, so bringing the number of CLI calls down.
- there's still room to improve the auto-instrumentation skill, especially in complex scenarios.

If you're interested in trying the out skill yourself, you can find them in the [Langfuse Skills GitHub repository](https://github.com/langfuse/skills).
