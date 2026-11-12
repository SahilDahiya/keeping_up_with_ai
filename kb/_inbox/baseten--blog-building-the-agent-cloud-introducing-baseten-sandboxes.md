---
title: 'Building the Agent Cloud: Introducing Baseten Sandboxes'
kind: blog
topic: null
subtopic: null
secondary_topics: []
summary: null
triage: null
skip_reason: null
source: baseten
url: https://www.baseten.co/blog/building-the-agent-cloud-introducing-baseten-sandboxes
author: Paul Sinai
published: '2026-11-05'
fetched: '2026-11-12T06:07:04Z'
classifier: null
taxonomy_rev: 2
words: 904
content_sha256: 691de616701a625645a2d150820ebce1dbece949bdc0eb899864a2a9dea7a433
---

# Building the Agent Cloud: Introducing Baseten Sandboxes

Product
# Building the Agent Cloud: Introducing Baseten Sandboxes

Baseten Sandboxes let agents run long tasks securely and statefully, with instant pause and resume. They’re the first piece of our cloud for agents.


- Authors
- Date
- November 5, 2026

Today, we’re introducing Baseten Sandboxes, the cornerstone of a cloud purpose-built for agents.

Agents are already taking on entire projects, from writing software to investigating problems and running core business workflows. To complete that work quickly and reliably, these agents need models, tools, compute, and state built to work together over long-horizon tasks.

Together, these needs demand a new kind of cloud: a cloud made for agents, with stateful runtimes, storage, and networking designed as a single system. Sandboxes are the first piece in that puzzle, giving agents their own persistent computer.

We’re making Baseten Sandboxes free to run until November 16th; [try them out](https://docs.baseten.co/sandboxes/overview)!

Sandboxes are the foundation that agents need to act. At its core, agent performance is a systems problem. Running code in a container isn’t hard on its own; the hard problems to solve are:

1. **Statefulness:** how do agents run long tasks without losing context between steps, or you paying for compute while they sit idle?
2. **Security:** how do you let agents run untrusted code without putting your infrastructure, data, or other users at risk?
3. **Latency:** how do you spin up new sandboxes without compounding latency across long-horizon work and network round-trip with inference?

Baseten Sandboxes solve each of these problems. They’re built from the ground up to be:

1. **Stateful:** as soon as the agent finishes, the sandbox suspends immediately while preserving state; suspend/resume are instant, so you don't pay for idle compute.
2. **Isolated:** Sandboxes run on microVMs, which are the gold standard for isolating untrusted code.
3. **Elastic:** boot a sandbox from standby in only 25 milliseconds, and scale to thousands of sandboxes within seconds.

Each Baseten Sandbox gets its own microVM with its own kernel and hardware-level isolation, providing more isolation than container-based solutions. This allows agents to execute code, manipulate files, and run processes inside an environment configured for their work without risk of lateral movement.

Initial startup and in-sandbox operations (read/write) are extremely fast, so latency doesn’t compound over agentic loops.

Whereas other sandboxes are ephemeral, or require developers to manage state explicitly, statefulness was a priority for us from inception. When an agent disconnects from a sandbox, everything is snapshotted—filesystem, memory, and actively running processes—and when it wants to resume its work, it restarts within 25 ms (up to 5x faster than other sandboxing tools, which compounds quickly over long-running agentic work). This enables us to scale compute to zero while the environment sleeps to reduce unnecessary cost.

This fundamentally changes what teams can build: agents can carry a project across sessions, pause for input from teammates, and continue with their environments intact. There are also utilization and cost benefits, since applications can maintain many persistent workspaces while allocating compute to the ones actively doing work.

As agents run longer and serve more users, preserving progress and managing idle compute become essential parts of agentic infrastructure.

Sandboxes are the first building block of a new kind of cloud, one made for agents.

Before the advent of GenAI and agents, every cloud primitive was built to deploy one application capable of serving millions of users. Agents invert that paradigm; instead of a single application, you now have millions of micro-applications, with each serving a handful of human or agent users.

To function properly, each agent’s environment must include the tools it needs to function, the work it accumulates, and the files it needs to carry between tasks. This demands a new type of cloud, purpose-built for agents: one that combines the compute, storage, networking, and identity required for high-scale, long-running agentic work.

To meet these needs, we’re building the foundation of an agent cloud. It will include:

- **Compute:** Sandboxes (described in detail above)
- **Storage:** Agent Drive, a shared, distributed, remote filesystem across sandboxes. Think of it like storage on Google Drive in addition to your local laptop, but optimized for high write volume and small-sized files (like code and markdown).
- **Networking:** Agent Proxy, which controls what agents can and cannot connect to, enforced outside the sandbox. Credential injection happens on the fly so agents can make sensitive calls (e.g., to Stripe for a payment), and the proxy can inject the credential without the agent ever seeing it.

This all includes a built-in permission system, an audit trail with thorough logging, and support for firewalling, static IPs, and many configurable knobs for builders.

Stay tuned for more announcements as Agent Drive and Agent Proxy come online in the coming months.

Inference, training, routing, governance, and execution are the building blocks of every AI product today, and when they come together, the whole is greater than the sum of its parts. That’s what we built Baseten to be: one unified platform for durable intelligence that compounds over time.

Products like Dedicated Inference, Model APIs, Training, Loops, Grid, and Sandboxes are the building blocks of our unified platform, creating a tight loop between inference, training, and execution. Sandboxes are central to the execution layer. As Agent Drive and Agent Proxy come online, they’ll give every agent the environment, storage, and networking it needs, all designed as a single system.

We're offering Baseten Sandboxes for free until November 16th—[start building here](https://docs.baseten.co/sandboxes/overview).
