---
title: 'Secure your harness: how to run NVIDIA''s NemoClaw with frontier open source
  models'
kind: blog
topic: product-engineering
subtopic: security
secondary_topics:
- agents/computer-use
summary: NVIDIA NemoClaw wraps the OpenClaw agent with the OpenShell sandbox runtime
  to enforce zero-default-permission, policy-based isolation at the infrastructure
  layer rather than inside the agent process, letting teams run open models like GLM-5
  and MiniMax M2.5 at 4-8x lower cost with HIPAA/SOC 2-compliant private inference.
triage: null
skip_reason: null
source: baseten
url: https://www.baseten.co/blog/secure-your-harness
author: Alex Ker
published: '2026-03-19'
fetched: '2026-11-12T06:14:40Z'
classifier: claude
taxonomy_rev: 2
words: 727
content_sha256: a948d07e8d51932fa141cb4b9c6b6fa95c6299d5d28fe690141cfcb236523920
---

# Secure your harness: how to run NVIDIA's NemoClaw with frontier open source models

AI engineering
# Secure your harness: how to run NVIDIA's NemoClaw with frontier open source models

Run always-on AI agents in isolated sandboxes with private inference and open source models at 4–8x lower cost


- Authors
- Date
- March 19, 2026

Before developers argued about programming languages. Now they argue about harnesses.

OpenClaw is the most exciting always-on agent for your work apps — and also one of the most exploited. Prompt injections, malicious skills on ClawHub, and remote code execution are real attack surfaces with serious consequences. Today, we're excited to announce support for NVIDIA NemoClaw.

NemoClaw is an open source stack that acts as a secure environment between OpenClaw and your infrastructure. It installs the NVIDIA OpenShell runtime (part of the NVIDIA Agent Toolkit) to provide policy-based security and enable enterprise-grade claws, or subagents, to run in isolated sandboxes with fine-grained controls and handle inference routing.

Instead of giving an agent full control over every app on your computer, NemoClaw starts with zero permissions. Private inference is on by default, and actions are strictly enforced at the infrastructure layer rather than inside the agent process itself.

In other words, OpenClaw runs as the agent inside the sandbox, OpenShell provides the isolation, and NemoClaw is the orchestration layer that wires it all together from a single CLI command.

The pattern we've seen consistently at Baseten is that the orchestration layer of intelligence, the harness, is increasingly composed of multiple models working in concert. Claws inside NemoClaw are no different: each subagent can draw on a team of models, and each model plays a distinct role.

A small model might run locally on private inference. A second might be fine-tuned on your production data for tool-calling precision. A third handles long-horizon planning. This decoupling of the monolithic model into many models, from frontier to custom, makes secure and contained environments for managing a team of agents essential.

Open models like [GLM-5](https://www.baseten.co/blog/how-we-built-the-fastest-glm-5-api/), [MiniMax M2.5](https://www.baseten.co/blog/minimax-m2-5-intelligence-too-cheap-to-meter-rl-process-rewards-real-world-produc/), and [Nemotron 3 Super](https://www.baseten.co/blog/introducing-nemotron-3-super/#context-length) are now the choice for developers who have hit the reliability or cost ceiling of closed-source models. With open weights, inference costs can drop 4–8x without sacrificing the intelligence and user-facing metrics — throughput, latency — that your customers actually feel. That makes these models a natural fit for claw agents, especially as the best harnesses push toward maximized context windows and extended thinking.

Running open source models inside NemoClaw requires inference infrastructure that matches its security guarantees. Baseten hosts GLM-5, MiniMax M2.5, Nemotron 3 Super, and other leading open models on model APIs that are HIPPA and SOC 2 compliant. For organizations in insurance, lending, and financial services, where data residency and regulations are non-negotiable, pairing NemoClaw with Baseten-hosted models on a dedicated VPC gives you the full safety in production: sandboxed agents, private inference, and zero cross-tenant exposure.

NVIDIA NemoClaw simplifies running always-on assistants with a single command. Here's how to get up and running with Baseten as your inference provider.

**1. Get your Baseten API key**

Grab an API key from [app.baseten.co](https://app.baseten.co/) under **API keys** and save it.

**2. Install NemoClaw**

Clone the repo and run the install script:

bash

```
git clone https://github.com/NVIDIA/NemoClaw.git
cd NemoClaw
./install.sh
```
The wizard will prompt for an NVIDIA API key — provide one to complete the install. It won't be used once you switch to Baseten in the next step.

**3. Register Baseten as your inference provider**

Run the following on the host (*outside the sandbox*):

```
openshell provider create \  
  --name baseten \  
  --type openai \  
  --credential "OPENAI_API_KEY=<your-baseten-api-key>" \  
  --config "OPENAI_BASE_URL=https://inference.baseten.co/v1"
openshell inference set --provider baseten --model zai-org/GLM-5
```
**4. Connect and launch**

Connect to your sandbox and launch the agent inside:

```
nemoclaw my-assistant connect
sandbox@my-assistant:~$ openclaw tui
```
Or run a quick test (inside the sandbox):

`sandbox@my-assistant:~$ openclaw agent --agent main --local -m "hello" --session-id tes`
**Managing your inference provider**

Check the current model:

`openshell inference get my-assistant`
Switch to a different model (run on the host, outside the sandbox):

`openshell inference set --provider baseten --model <model-id>`
Available model IDs are listed on [Baseten's supported models page](https://docs.baseten.co/development/model-apis/overview#supported-models).

For teams adopting autonomous, long-running agents, NemoClaw tightens the risk surface area. For regulated industries, it should be the default option. Get your Baseten API key [here](about:blank) and try out GLM-5, MiniMax M2.5, or Nemotron 3 Super on Baseten Model APIs and connect them to your NemoClaw sandbox today.
