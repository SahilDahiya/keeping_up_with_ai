---
title: Building with NVIDIA Nemotron 3 Ultra and LangChain Deep Agents Code on Baseten
kind: blog
topic: null
subtopic: null
secondary_topics: []
summary: null
triage: null
skip_reason: null
source: baseten
url: https://www.baseten.co/blog/nvidia-nemotron-3-ultra-and-langchain-deep-agents-on-baseten
author: Philip Kiely
published: '2026-07-08'
fetched: '2026-11-12T06:07:52Z'
classifier: null
taxonomy_rev: 2
words: 832
content_sha256: a4a0cf888d80fbd86b14ae68bd717ba308714ea7525e50ff97df37b7f15563c3
---

# Building with NVIDIA Nemotron 3 Ultra and LangChain Deep Agents Code on Baseten

AI engineering
# Building with NVIDIA Nemotron 3 Ultra and LangChain Deep Agents Code on Baseten

Build frontier AI agents with NVIDIA Nemotron 3 Ultra and LangChain Deep Agents on Baseten—top open-model agent accuracy at \~10× lower cost.


- Authors
- Date
- July 8, 2026

As harnesses have become more load-bearing within AI applications, model-harness co-development increasingly drives capabilities beyond a model’s original baseline. For application developers who develop and own both the model and the harness, this cycle of improvement has been apparent for some time. But developers building on open models and third-party harnesses have not enjoyed that same access.

This changed with [LangChain Deep Agents harness profiles](https://docs.langchain.com/oss/python/deepagents/profiles). These model-specific profiles encode changes to prompts, tool descriptions, middleware, and subagents to match harness behavior to the quirks of the model.

Today, the LangChain team is releasing a tuned [Deep Agents](https://docs.langchain.com/oss/python/deepagents/overview) harness profile for NVIDIA Nemotron 3 Ultra. With the harness profile in place, NVIDIA Nemotron 3 Ultra achieves top agent accuracy among open models on the LangChain Deep Agents evaluation suite at approximately 10x lower cost than leading closed alternatives.

Achieving these performance results did not require fine-tuning the underlying model or making any changes to serving infrastructure. As such, it works out of the box with Baseten’s fast, cost-effective [model API for NVIDIA Nemotron 3 Ultra](https://www.baseten.co/library/nvidia-nemotron-ultra/). Below, I’ll walk you through the process of setting up NVIDIA Nemotron 3 Ultra on Baseten with LangChain Deep Agents Code.

The system we’ll be building has four components:

- **The model:** [NVIDIA Nemotron 3 Ultra](https://www.baseten.co/library/nvidia-nemotron-ultra/).
- **The inference provider:** Baseten, which hosts NVIDIA Nemotron 3 Ultra as a model API.
- **The harness:** [LangChain dcode](https://github.com/langchain-ai/deepagents/tree/main/libs/code), an open-source package.
- **The profile:** A set of model-specific modifications made to LangChain Deep Agents.

However, setup is just two steps.

First, install the latest version of LangChain dcode with Baseten support.

```
!curl -LsSf https://langch.in/dcode | bash
!dcode --install baseten --yes
```
Then, grab your [Baseten API key](https://docs.baseten.co/organization/api-keys) – or create an account if you don’t already have one – and make sure it is set in your environment as `BASETEN_API_KEY`.

From there, the model slug `baseten:nvidia/NVIDIA-Nemotron-3-Ultra-550B-A55B` will be available to use within dcode. The harness profile for NVIDIA Nemotron 3 Ultra is automatically applied as the model is detected, no additional steps are required to install or activate the harness profile.

For this example, we’ll build an agent designed to review proposed workflows and flag potential compliance errors. This is a highly simplified version of the type of agent being built across multiple industries like financial services and healthcare. For these agents, both high accuracy and low cost per task are vital for moving to production.

Let’s imagine a couple of sample workflows as inputs to the agent.

python

```
demo_dir = Path("readiness_demo")
demo_dir.mkdir(exist_ok=True)
(demo_dir / "workflow_packet.md").write_text(
    """# Workflow Packet
Workflow: Launch a new patient billing exception process.
Policy excerpts:
- Any workflow that touches PHI must satisfy control HC-17.
- Billing exception workflows must document why each data field is necessary.
- If evidence is missing, create a risk ticket before launch.
Evidence packet:
- The workflow stores patient name, account number, diagnosis code, and balance.
- The packet explains account number and balance, but not diagnosis code.
- The launch owner says the process should go live tomorrow.
""",
    encoding="utf-8",
)
(demo_dir / "controls.md").write_text(
    """# Controls
## HC-17: PHI minimum necessary review
Owner: Compliance
Requirement: The launch packet must document a business purpose for every PHI data field used by the workflow.
""",
    encoding="utf-8",
)
print(f"Created demo files in {demo_dir.resolve()}")
```
We’ll use NVIDIA Nemotron 3 Ultra to process these tickets via dcode. As a reminder, the harness profile is automatically applied based on the model slug.

```
import subprocess
import textwrap
prompt = textwrap.dedent(
    """
    You are a regulated workflow readiness agent.
    Read workflow_packet.md and controls.md in the current directory.
    Assess whether the workflow is ready to launch. If evidence is missing,
    create a file named risk_ticket.md with a mock ticket ID, severity, title,
    and summary. Then create readiness_memo.md with exactly these sections:
    1. Readiness decision
    2. Evidence found
    3. Missing evidence
    4. Risk ticket opened
    5. Executive summary
    Keep the memo concise and include the concrete risk ticket ID.
    """
).strip()
completed = subprocess.run(
    [
        DCODE,
        "--model",
        "baseten:nvidia/NVIDIA-Nemotron-3-Ultra-550B-A55B",
        "--auto-approve",
        "--non-interactive",
        prompt,
    ],
    cwd=demo_dir,
    env=os.environ.copy(),
    text=True,
    capture_output=True,
    timeout=600,
)
print(completed.stdout)
if completed.stderr:
    print(completed.stderr)
if completed.returncode != 0:
    raise RuntimeError(f"dcode exited with code {completed.returncode}")
```
The agent reads the tickets using its file-reading tools, then uses file-writing tools to create outputs. This could be expanded with tools for creating tickets, writing slack messages, and updating project statuses by implementing these tools into the harness.

While production agents are substantially more complex, this example shows that applying the model-specific harness profile requires almost no code changes within dcode to access frontier performance at approximately 10x lower cost than leading closed alternatives.

With Baseten’s [NVIDIA Nemotron 3 Ultra model API](https://www.baseten.co/library/nvidia-nemotron-ultra/) and [LangChain Deep Agents Code](https://docs.langchain.com/oss/python/deepagents/code/overview), you can get started building frontier agents today.
