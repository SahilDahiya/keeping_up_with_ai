---
title: How Legora runs 2,000 parallel agent evals on Modal Sandboxes | Modal Blog
kind: blog
topic: evals-observability
subtopic: evaluation
secondary_topics:
- infra-platform/deployment
summary: Case study on how legal AI agent Legora runs 2,000 parallel agent evals (100
  cases x 4 harness variants x 5 trials) by booting its entire product stack -- a
  headless DOCX editor, self-hosted Turbopuffer, Postgres, and code-execution sandboxes
  -- inside an isolated Modal Sandbox per run for environment fidelity rather than
  mocking dependencies.
triage: null
skip_reason: null
source: modal
url: https://modal.com/blog/how-legora-runs-thousand-scale-parallel-agent-evals-on-modal-sandboxes
author: null
published: '2026-10-19'
fetched: '2026-10-27T06:11:20Z'
classifier: claude
taxonomy_rev: 2
words: 924
content_sha256: c6e2c89ddde8e345e92b53d5ddbfbc7b0705e19011e0b69ffa29a26ab57da3c8
---

# How Legora runs 2,000 parallel agent evals on Modal Sandboxes | Modal Blog

Legora is an agentic system that supports lawyers in research, review, and drafting across complex matters. In early 2026, as rapid gains in model capabilities made longer and more autonomous legal work possible, Legora began replacing its existing AI assistant with a full-fledged agent.

To test a legal agent that works for hours across thousands of documents, Legora boots its entire application, pinned to a specific commit, inside a separate Modal Sandbox for every eval run.

To read more about Legora’s full evals system, check out [the blog](https://legora.com/engineering/building-scalable-evals-infrastructure-for-legal-agents) they wrote!

## Rebuilding evals for an autonomous agent

The shift from assistant to agent exposed two major shortcomings in Legora's existing evals framework: scale and environment fidelity. The infrastructure challenge was to create thousands of isolated Legora environments in parallel, restore the right world into each one, and let the agent complete ambitious, long-running tasks.

The first problem was scalability. The assistant had been designed for smaller tasks in environments containing a few documents. The new agent needed to run for hours inside a realistic project containing thousands of documents and gigabytes of data. Where the old eval system could run on a laptop, the new one needed to run in the cloud.

“Running 10 or 20 evals at once would overload a laptop. A typical experiment for the agent is now 100 cases, 4 harness variants, and 5 trials each. That's 2,000 runs, and they all need to happen in parallel.”

The even harder problem was environment fidelity. Legora's agent spans their whole product: a headless DOCX editor, self-hosted Turbopuffer instances, PDF conversion, Postgres and authorization databases, blob storage, and dynamically created code-execution sandboxes.

“Our agent wraps the entire product. If you want to measure the effect of a change to the code sandbox or a database migration, you need that exact version of the whole app in every run, not a mock.”

## Modal Sandboxes provide complex environments at scale

Today, each eval run executes in its own Modal Sandbox, loaded with a custom image and filesystem. While Legora evaluated multiple cloud-managed sandbox providers to replace local execution, they chose Modal for scalability, low startup latency, and support for complex environments.

“Our application and container image are both quite large. With Modal, we can give each Sandbox the resources it needs and run the full app without the constraints we encountered elsewhere. That flexibility and scalability made Modal a much better fit than other solutions.”

Each experiment kicks off 2,000 runs or more, each of which runs concurrently in a Modal Sandbox. Engineers on Legora’s team are able to kick off runs from their laptops to measure the impact of changes to their agent.

To manage storage for each run, Legora uses Modal Volumes. Volumes make large document collections available across Sandboxes and let the team snapshot world state, deduplicating shared setup while ensuring that repeated runs begin from the same documents, database state, permissions, and blobs. The team also cached Docker images in Volumes to speed up the Docker Compose step, with plans to move that cache to filesystem snapshots.

![Diagram illustrating the flow for eval experiments from starting the experiment to executing.](https://modal-cdn.com/cdnbot/legora_eval-experiment7iknv0m0_61ace401.webp) 

Building the large image for Legora's full application initially led to slow eval runs. Legora addressed the bottleneck with an hourly pipeline that builds the image and pre-warms Sandboxes, reducing the reset-to-commit step from a full application build to only the delta since the previous build. A separate hourly job syncs values from Legora's key vault into Modal Secrets, while frequent secret rotation, least-privilege access, dependency-age requirements, and Modal's domain allowlisting help secure the environment.

### Moving from gVisor to Modal VM Sandboxes

As an early user of Modal VM Sandboxes, Legora was instead able to run Sandboxes backed by a full virtual machine. With a real Linux kernel in every Sandbox, Docker behaved as it would on a normal host. While before they had to implement workarounds to get full Docker functionality, VM Sandboxes enabled them to simplify their setup.

“Our app runs as a set of Docker services. Previously, that meant we had to introduce networking and FUSE workarounds at every layer to get full Docker functionality in the sandbox, from host-mode networking with our own DNS resolution to running code sandboxes as bare processes because FUSE wouldn't mount. With VM Sandboxes, it's been frictionless: Docker behaves like it does on a normal Linux host, and we deleted every one of those workarounds.”

## Creating a self-improving agent loop

The new evals platform is now Legora's primary instrument for measuring agent quality. It enabled the company to run BAR, its internal benchmark of realistic, long-horizon legal tasks, and compare foundation models across quality, cost, and latency. Those results now inform production model selection as well as decisions about the design of the agent harness.

The platform also changed how the engineering team works. After wrapping the evals application in a CLI and a skill, Legora enabled agents to create cases, launch experiments, and analyze results autonomously; most engineers now interact with evals through agents.

Given a metric or problem, experiment tools, and a budget, an agent can hill-climb the harness until the metric improves—an approach Legora has applied to tool search, PowerPoint generation, and reproducing research papers to make the harness more cost-efficient.

For example, Legora was able to cut the cost of their agent by 30% through smarter compaction and a custom tool search implementation. While the engineering team managed the process, agents were able to work via auto-research to validate and improve their own results.
