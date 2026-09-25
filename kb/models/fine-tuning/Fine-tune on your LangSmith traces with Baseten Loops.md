---
title: Fine-tune on your LangSmith traces with Baseten Loops
kind: blog
topic: models
subtopic: fine-tuning
secondary_topics: []
summary: Describes LangSmith Fine-Tuning (the smithtune CLI), which turns successful
  LangSmith agent traces into a supervised fine-tuning dataset, trains it via the
  Baseten Loops SDK on dedicated GPUs in the user's own workspace, and deploys the
  evaluated checkpoint straight to a Baseten Dedicated Inference endpoint without
  moving weights out of the workspace.
triage: null
skip_reason: null
source: baseten
url: https://www.baseten.co/blog/fine-tune-on-your-langsmith-traces-with-baseten-loops/
author: Mudith Jayasekara; Aaron Ellis-Bloor; Vivek Trivedy; Jake Broekhuizen
published: '2026-09-24'
fetched: '2026-09-25T06:10:28Z'
classifier: claude
taxonomy_rev: 2
words: 386
content_sha256: 04e1092f6c0911fc5f830340c86cb5a68e733eb7dc2d952e307873c022f825a3
---

# Fine-tune on your LangSmith traces with Baseten Loops

![loops](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1790278962-b10-langchain-blog-1.png%3Fauto%3Dformat%26fit%3Dcrop%26h%3D630%26w%3D1200&w=3840&q=100)

LangChain's applied research team trains the models behind LangSmith Engine on [Baseten Loops](https://docs.baseten.co/loops/overview). They fine-tune an open model on agent traces from LangSmith, and we [wrote about that work](https://www.baseten.co/blog/langchain-trains-custom-models-langsmith-engine-baseten-loops/) earlier this month.

That workflow is now open to anyone building on LangSmith. LangChain announced LangSmith Fine-Tuning today at their Interrupt 26 Conference in New York. It runs on smithtune, an open-source CLI you can use yourself or hand to a coding agent.

The CLI reads your LangSmith traces and turns the successful runs into a supervised fine-tuning dataset. Training then runs on Baseten Loops. Once LangSmith has evaluated the new checkpoint, smithtune deploy puts it on a Baseten Dedicated Inference deployment.

## Training on Baseten

With Baseten as the training provider, smithtune trains through the Loops Python SDK on dedicated GPUs in your own Baseten workspace. Checkpoints are saved on Baseten during the run, so deploying one never means downloading weights and uploading them somewhere else.

Before scheduling a run, the CLI checks which models your workspace is enabled to train. This mostly helps when a coding agent is typing the commands. It can see what's available and won't queue a job that can't start.

You use your own Baseten API key, and training and inference bill to your Baseten account.

"LangSmith users have been asking for a way to turn their production traces into models built for their own agents. We gave our agent the smithtune README and the agent skill and let it go. It took us all the way to a model deployed on Baseten, and it was pretty hands off!
Most LangSmith users are already sitting on thousands of traces from their agents, and we wanted training on them to feel about that easy. The Baseten team has worked closely with ours through this launch, and we're excited to give LangSmith users a direct path from their traces to a model running on Baseten."

## Get started

The code is at [github.com/langchain-ai/smithtune](https://github.com/langchain-ai/smithtune). Training on Baseten needs an account with Loops enabled, and because Loops is in early access, you may need to [request it for your workspace](https://www.baseten.co/talk-to-us/loops-signup/) first.

If a coding agent will be running smithtune, the agent skill in the repo points to [docs.baseten.co/agent-setup](https://docs.baseten.co/agent-setup). That page sets your agent up with our agent skills and the Baseten docs MCP server.
