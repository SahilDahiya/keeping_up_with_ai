---
title: How to run GLM-5.2 in any harness
kind: blog
topic: null
subtopic: null
secondary_topics: []
summary: null
triage: null
skip_reason: null
source: baseten
url: https://www.baseten.co/blog/how-to-run-glm-52-in-any-harness
author: Alex Ker
published: '2026-06-25'
fetched: '2026-11-12T06:15:04Z'
classifier: null
taxonomy_rev: 2
words: 337
content_sha256: 8e6d99270fdb22066eb951a0ef34e98687acfa07b6293785a6c0bd2f4bef152e
---

# How to run GLM-5.2 in any harness

AI engineering
# How to run GLM-5.2 in any harness

Learn how to use GLM-5.2 at 280+ TPS inside Claude Code, Codex, Deep Agents CLI, or any harness.


- Authors
- Date
- June 25, 2026

GLM-5.2 is this year’s DeepSeek moment. It’s already shifting the trajectory of how we interact with and consume intelligence.

As we and our agents continue to tokenmax, tokenonomics and performance are more relevant than ever. And GLM 5.2 is the perfect frontier model that matches closed-source models in quality while exceeding them in speed and cost by multiples (e.g., \~4.5x faster and \~5x cheaper than Opus 4.8, many are saying it's a drop-in replacement).

Open is no longer a compromise but a logical winner across dimensions for scaling yourself and your org. Here's exactly how to use GLM-5.2 inside 3 of the popular harnesses today in \<5 min, which can be generalized to any other.

1. Install Claude Code: `npm install -g@anthropic-ai/claude-code`
2. Create an account at [baseten.co](https://baseten.co/) and grab an API key from [app.baseten.co/settings/api\_keys](https://app.baseten.co/settings/api_keys)
3. Edit `~/.claude/settings.json` and add:

json

```
"env": {
    "ANTHROPIC_AUTH_TOKEN": "your_baseten_api_key",
    "ANTHROPIC_BASE_URL": "https://inference.baseten.co",
    "ANTHROPIC_DEFAULT_HAIKU_MODEL": "zai-org/GLM-5.2",
    "ANTHROPIC_DEFAULT_SONNET_MODEL": "zai-org/GLM-5.2",
    "ANTHROPIC_DEFAULT_OPUS_MODEL": "zai-org/GLM-5.2",
    "ENABLE_TOOL_SEARCH": "auto"
}
```
Run CC, and GLM-5.2 will power every Claude Code call.

1. Get a Baseten API key like above and store it in macOS Keychain:

bash

```
security add-generic-password \
  -a "$USER" \
  -s codex-baseten-api-key \
  -w "YOUR_BASETEN_API_KEY_HERE" \
  -U
```
2\. Add the Baseten provider to `~/.codex/config.toml`:

```
[model_providers.baseten]
name = "Baseten"
base_url = "https://inference.baseten.co/v1"
wire_api = "responses"
[model_providers.baseten.auth]
command = "/usr/bin/security"
args = ["find-generic-password", "-a", "YOUR_MAC_USERNAME", "-s", "codex-baseten-api-key", "-w"]
timeout_ms = 5000
```
3\. Create a profile at `~/.codex/baseten-glm.config.toml`:

```
model = "zai-org/GLM-5.2"
model_provider = "baseten"
model_reasoning_effort = "medium"
```
Run: `codex --profile baseten-glm` to start Codex with GLM-5.2, and all your requests will be routed to this model.

1\. Run:

`curl -LsSf https://langch.in/dcode`
2\. Launch with `dcode` and inside it:

- `/install` baseten → add Baseten integration
- `/auth` → add your Baseten API key
- `/model` → switch to GLM-5.2
