---
title: Introducing Claude Managed Agents with Modal Sandboxes
topic: agents
subtopic: computer-use
secondary_topics:
- infra-platform/deployment
summary: Shows how Claude managed agents can use Modal sandboxes for isolated execution,
  filesystem state, and scalable agent workloads.
source: modal
url: https://modal.com/blog/introducing-claude-managed-agents-with-modal-sandboxes
author: null
published: '2026-05-18'
fetched: '2026-07-11T04:27:08Z'
classifier: codex
taxonomy_rev: 1
words: 855
content_sha256: e3e683e00655116c4600d09a67c20a1cba8b989e954037ac35383bd3e2361b9f
triage: keep
skip_reason: null
---

# Introducing Claude Managed Agents with Modal Sandboxes

[Back](https://modal.com/blog)

# Introducing Claude Managed Agents with Modal Sandboxes

Last month, Anthropic launched Claude Managed Agents, a suite of composable APIs for building and deploying cloud-hosted agents at scale, that separates the agent loop from the code execution.

Today, Modal is announcing our collaboration with Anthropic to launch a first-class integration for Modal Sandboxes and Managed Agents.

With this launch, you can now run all tool calls in a self-hosted Modal Sandbox, and benefit from Modal's fast cold-starts, [custom images](https://modal.com/docs/guide/images), [various snapshotting techniques](https://modal.com/docs/guide/sandbox-snapshots) and [cost-efficient bursting mechanisms](https://modal.com/docs/guide/resources#billing) while still maintaining the convenience of Anthropic's managed agent loop.

Get started with [our examples](https://github.com/modal-labs/claude-managed-agents-modal-sandbox/tree/main) today.

## Giving agents the right agency

At Modal, we've been long-time fans of this architectural approach, where the agent loop runs in a different environment from the actual code execution. While the Agent SDK lets you build the agent loop inside your existing process and infrastructure, Managed Agents is a fully hosted REST API in which Anthropic runs the agent loop and manages session state, and your application sends events and streams back results.

![](https://modal-cdn.com/cdnbot/anthropicdiagramgivak8kr_8fbcc6c0.webp)

While we see users adopting both of these patterns using Modal Sandboxes, we’re starting to see more and more of our customers embrace the separation Managed Agents enforces. We believe this approach is likely to emerge as the winning pattern, because keeping the model loop outside the execution environment makes security boundaries easier to reason about and gives teams more control over observability, failure handling, and scale.

## Modal Sandboxes for Claude Managed Agents

Anthropic's managed sandbox is a good fit for standard deployments where a default execution environment meets your needs. For teams with more specific requirements, Modal is a cloud platform built for AI workloads, with a custom container runtime and orchestration layer designed for fast, flexible, isolated compute.

- **Fast startup, even on custom images:**fully customizable execution environments with rapid build times, so you can iterate quickly and bake your full dependency tree in.

```
image = (
    modal.Image.debian_slim(python_version="3.13")
    # add your custom dependencies
    .apt_install("ffmpeg", "imagemagick", "mediainfo")
    .uv_sync()
)
```
- **Persistence options:**- [Volumes](https://modal.com/docs/guide/volumes#volumes),- [directory snapshots, filesystem snapshots, and memory snapshots](https://modal.com/docs/guide/sandbox-snapshots#snapshots)give you the right tool depending on what you need to preserve across runs.

```
volume = (
    modal.Volume.from_name("claude-managed-agents", create_if_missing=True)
    .with_mount_options(sub_path=f"/sessions/{session_id}")
)
```
- **Cost efficiency:**burst pricing means you only pay for what you use, with no minimums and no idle costs between runs.
- **Network security**: tools to secure your application like- [short-lived connect tokens](https://modal.com/docs/guide/sandbox-networking#networking-and-security)that give clients authenticated, direct access to running sandbox services without exposing them to the public internet.

`credentials = sandbox.create_connect_token()`- **Scale:**upwards of 100,000 concurrent sandboxes per customer, with generous resource configurations including CPU, memory, and GPU access when you need it.

```
sandbox = await modal.Sandbox.create.aio(
    ...,
    cpu=(2, 16),  # (request, limit)
    memory=(8*1024, 64*1024),  # (request, limit) in MiB
    gpu="H100",
)
```
### How DoorDash is Thinking About Accelerating Production-ready AI Agents for Merchants

To best support its merchants, DoorDash is building an intelligence system with a suite of AI agents spanning across chat, voice, SMS, browser operation, mobile app, and in-store ordering, all designed to make running and growing their business dramatically easier. Bringing a large AI agent system to production requires infrastructure that can handle long-running, asynchronous agentic work reliably and at scale across their vast merchant ecosystem.

The DoorDash team is already running production agents powered by Claude models, with Modal as part of their AI infrastructure. They’re also exploring Managed Agents as a potential accelerator for expanding the full agentic power of the intelligence system.

### Building agent-assisted triage at Blend

[Blend](https://blend.com/) powers digital origination for banks, credit unions, and mortgage lenders, sitting at the center of highly complex banking environments where each customer operates with unique configurations, workflows, integrations, and compliance requirements.

That complexity makes issue resolution difficult. A support ticket is rarely just a code problem. Engineers often need to reason across code, customer-specific configuration, product behavior, and the customer’s reported experience at the same time.

Blend had already begun using the Claude Agent SDK and Modal Sandboxes to support agent-assisted triage. But as the team looked to scale the workflow across engineering, a new challenge emerged: how to give engineers access to fully configured sandbox environments without handing out direct Modal credentials or requiring each developer to manage the setup themselves.

That need is what makes the Claude Managed Agents and Modal Sandboxes integration valuable for Blend. By providing a managed orchestration layer for sandbox creation, credential injection, and remote access, the integration gives Blend a path to make agent-assisted development more secure, consistent, and scalable across its engineering organization.

## Get started

Claude Managed Agents and Modal Sandboxes together give your agents the scale, flexibility, and isolation they need to run in production, and we invite you to try it out today. We've shipped [two reference examples](https://github.com/modal-labs/claude-managed-agents-modal-sandbox/tree/main) to get you started: a CLI agent and a Slack-bot, both on the same Modal + Managed Agents backbone. Clone, swap in your image and your tools, and you've got the bones of a production deployment. Sign up for Modal and get $30 of free compute every month. Let us know what you build!
