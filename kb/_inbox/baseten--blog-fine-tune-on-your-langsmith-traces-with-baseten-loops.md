---
title: Fine-tune on your LangSmith traces with Baseten Loops
kind: blog
topic: null
subtopic: null
secondary_topics: []
summary: null
triage: null
skip_reason: null
source: baseten
url: https://www.baseten.co/blog/fine-tune-on-your-langsmith-traces-with-baseten-loops
author: Mudith Jayasekara
published: '2026-09-24'
fetched: '2026-11-12T06:06:58Z'
classifier: null
taxonomy_rev: 2
words: 413
content_sha256: 5af370f5aeb04f8667b7eec65cd76e60d15ef89295ceba1f5c3ea413f98c8806
---

# Fine-tune on your LangSmith traces with Baseten Loops

News
# Fine-tune on your LangSmith traces with Baseten Loops

LangSmith Fine-Tuning is in public beta today, and its open-source CLI, smithtune, trains on Baseten Loops.


- Authors
- Date
- September 24, 2026

TLDR

LangChain's applied research team trains the models behind LangSmith Engine on Baseten Loops. They fine-tune an open model on agent traces from LangSmith, and we wrote about that work earlier this month. That workflow is now open to anyone building on LangSmith. LangChain announced LangSmith Fine-Tuning today at their Interrupt 26 Conference in New York. It runs on smithtune, an open-source CLI you can use yourself or hand to a coding agent. The CLI reads your LangSmith traces and turns the successful runs into a supervised fine-tuning dataset. Training then runs on Baseten Loops. Once LangSmith has evaluated the new checkpoint, smithtune deploy puts it on a Baseten Dedicated Inference deployment.

With Baseten as the training provider, smithtune trains through the Loops Python SDK on dedicated GPUs in your own Baseten workspace. Checkpoints are saved on Baseten during the run, so deploying one never means downloading weights and uploading them somewhere else.

Before scheduling a run, the CLI checks which models your workspace is enabled to train. This mostly helps when a coding agent is typing the commands. It can see what's available and won't queue a job that can't start.

You use your own Baseten API key, and training and inference bill to your Baseten account.

"LangSmith users have been asking for a way to turn their production traces into models built for their own agents. We gave our agent the smithtune README and the agent skill and let it go. It took us all the way to a model deployed on Baseten, and it was pretty hands off!

Most LangSmith users are already sitting on thousands of traces from their agents, and we wanted training on them to feel about that easy. The Baseten team has worked closely with ours through this launch, and we're excited to give LangSmith users a direct path from their traces to a model running on Baseten."


The code is at [github.com/langchain-ai/smithtune](https://github.com/langchain-ai/smithtune). Training on Baseten needs an account with Loops enabled, and because Loops is in early access, you may need to [request it for your workspace](https://www.baseten.co/talk-to-us/loops-signup/) first.

If a coding agent will be running smithtune, the agent skill in the repo points to [docs.baseten.co/agent-setup](https://docs.baseten.co/agent-setup). That page sets your agent up with our agent skills and the Baseten docs MCP server.
