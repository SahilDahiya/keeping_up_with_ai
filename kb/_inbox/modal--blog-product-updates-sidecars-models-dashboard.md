---
title: 'Product updates: Sandbox Sidecars, new models, a refreshed dashboard, and
  more | Modal Blog'
kind: blog
topic: null
subtopic: null
secondary_topics: []
summary: null
triage: null
skip_reason: null
source: modal
url: https://modal.com/blog/product-updates-sidecars-models-dashboard
author: null
published: '2026-09-14'
fetched: '2026-09-16T06:10:25Z'
classifier: null
taxonomy_rev: 2
words: 1342
content_sha256: d56e178ccff5e85dcf35bb845a2e907b42c16eb86422846d49da35d6b4943b09
---

# Product updates: Sandbox Sidecars, new models, a refreshed dashboard, and more | Modal Blog

[Back](https://modal.com/blog)

# Product updates: Sandbox Sidecars, new models, a refreshed dashboard, and more

August brought new model support, faster Function calls, and major improvements across Modal Sandboxes. Here are the highlights.

## 🤖 Day-zero support for Kimi K3, Qwen 3.8, GLM 5.3, and GLM 5.3 Flash

Explore four frontier open-weight models now supported on Modal Auto Endpoints.

All four are supported as Shared Endpoints with [token-based pricing](https://modal.com/docs/guide/shared-endpoints#pricing), or as Dedicated Endpoints [billed by the GPU second](https://modal.com/docs/guide/dedicated-endpoints#pricing).

- **Kimi K3:** Moonshot’s 2.8T-parameter multimodal model with native vision and a 1M-token context window. We partnered with Moonshot and vLLM on day-zero support, with a custom DFlash speculator delivering 460 tokens per second on agentic workloads.
- **Qwen3.8-2.4T-A95B:** Qwen’s 2.4T-parameter, text-only Mixture-of-Experts model activates 95B parameters per token and is built for coding, research, and long-horizon agentic tasks. We delivered day-zero support with SGLang and a custom DFlash speculator.
- **GLM-5.3:**[Z.ai](http://Z.ai) ’s 753B-parameter Mixture-of-Experts model activates 40B parameters per token and supports a 1M-token context window. It is built for complex coding and long-horizon agentic tasks.
- **GLM-5.3-Flash:**[Z.ai](http://Z.ai) ’s natively multimodal 320B-parameter Mixture-of-Experts model activates 18B parameters per token and supports a 1M-token context window, bringing visual understanding to coding and agentic workflows.

[Create a Dedicated Endpoint or use a Shared Endpoint →](https://modal.com/endpoints)

## 💸 Improving control over spend

Two updates for better usage control:

- **Environment-level budgets** are now available for all Team and Enterprise workspaces. Owners and Managers can set a compute-usage budget per Environment and track current-cycle compute usage against it — useful for giving teams their own guardrails without splitting workspaces.[Read the docs](https://modal.com/docs/guide/budgets) .
- **The usage limits UI got a refresh.** Threshold billing and usage limits are now presented with consistent terminology and numbers that add up at a glance, so it's clearer what your limits are and how to adjust them.

## 🌎 Lower pricing for broad region selection

The pricing multiplier for broad region selection has dropped from 1.5x to 1.15x. Broad regions—including the US, EU, and APAC—keep workloads closer to users or data while preserving a larger capacity pool for better availability and faster scheduling.

[Read our guide to region selection →](https://modal.com/docs/guide/region-selection)

## 🔒 Private Environments with default roles

You can now set a default Role for a Restricted Environment. Set the default to No Access and explicitly grant Viewer or Contributor access to the Members who need it; everyone else can't discover or access the Environment at all. Workspace Owners and Managers retain Contributor access. This effectively gives you private Environments for sensitive projects within a shared workspace.

## 🌓 A refreshed dashboard has landed

We’ve updated the dashboard with improved navigation, a new color system for visualizations, and a light mode appearance option. Light mode is available in beta for all users, with other changes rolling out gradually over the coming days.

![Dashboard improvements in Modal.](https://modal-cdn.com/cdnbot/dashboard_lightjss_6wse_7e165046.webp) 

## 🧩 Sandbox Sidecars enter public alpha

Sandbox Sidecars are now in public alpha. Sidecars run additional containers beside a main Sandbox on the same host, connected through a low-latency internal network. They are useful for [custom network proxies](https://modal.com/docs/examples/sidecar_traffic_routing), multi-container workloads, and separating an agent harness from its tool execution.

```
import modal
app = modal.App.lookup("sidecar-example", create_if_missing=True)
image = modal.Image.debian_slim().build(app)
sb = modal.Sandbox.create("sleep", "600", app=app, image=image, timeout=300)
sidecar = sb._experimental_sidecars.create(
    "python",
    "-m",
    "http.server",
    "8080",
    name="web",
    image=image,
)
# Give the server a moment to start, then call it from the main sandbox.
p = sb.exec(
    "python",
    "-c",
    "import time, urllib.request; time.sleep(1); print(urllib.request.urlopen('http://web:8080').status)",
)
p.wait()
print(p.stdout.read())  # "200"
sb.terminate()
```
## 📊 Better observability for Sandbox CPU and memory requests

We've shipped a set of graphs to make it easier to specify Sandbox CPU and memory requests, helping you avoid OOMs or CPU contention without paying for more resources than you need. These charts show various percentiles of how much CPU and memory the Sandboxes in each of your Apps consume, so you can set request sizes accordingly.

![Modal Sandbox graphs.](https://modal-cdn.com/blog/images/sandbox_graphs-2.webp) 

## 🔲 VM Sandboxes now in public beta

VM Sandboxes have entered public beta. They run a real Linux kernel, so they can support workloads that run Docker containers within the Sandbox, or that require Linux features like eBPF, systemd, cgroups, or custom filesystem mounts. This generally also leads to better filesystem performance for I/O-sensitive workloads.

[Check out our docs](https://modal.com/docs/guide/vm-sandboxes#vm-sandboxes) to get started.

## 📦 Now GA: Sandbox directory snapshots and new Sandbox filesystem API

Sandbox directory snapshots let you snapshot selected directories instead of an entire container filesystem. You can use them to update system dependencies separately from application code, speed up resumptions of previous sessions, and restore application state into a warm pool of Sandboxes. [Read the docs](https://modal.com/docs/guide/sandbox-snapshots#directory-snapshots) for more.

Additionally, our new Sandbox filesystem API is now GA. The new filesystem API offers improved reliability and better performance for small files. [Learn more.](https://modal.com/docs/guide/sandbox-files#filesystem-api)

## 🌐 Regional Proxies

You can now choose a region when creating a Modal Proxy in workspace settings. Proxies provide static outbound IPs for Functions and Sandboxes, letting you connect to resources protected by IP allowlists. Placing a Proxy closer to those resources gives you more control over where traffic is routed and can reduce network latency.

## 💻 SDK updates

We’ve released version 1.5.5 of the Python SDK and version 0.10.0 of the JavaScript and Go SDKs. Updates across these releases include new log APIs, faster Sandbox filesystem writes in JS and Go, and improved autoscaler configuration reporting.

Read the changelogs: [Python](https://modal.com/docs/sdk/py/releases) · [JavaScript](https://modal.com/docs/sdk/js/releases) · [Go](https://modal.com/docs/sdk/go/releases)

## 📚 More from Modal

### 📈 Scaling to 1 million concurrent Sandboxes in seconds

We rebuilt our scheduling system to support millions of concurrent Sandboxes and tens of thousands of creations per second. In testing, we started one million Sandboxes in under a minute while keeping median time to interactivity below half a second.

### ⚡ Bringing serverless functions closer to the speed of wire

We rebuilt the Function I/O path around a faster, geographically distributed routing layer, moving non-critical work off the hot path and minimizing shared-storage access. The result is ~80ms lower p50 latency, with additional savings possible.

### 🌓 Kimi K3 by Moonshot available on Modal

We partnered with Moonshot and vLLM to bring day-zero Kimi K3 support to Modal, pairing the 2.8T-parameter multimodal model with a custom-trained DFlash speculator. On agentic workloads, our speculator increases interactivity from 100 to 460 tokens per second and per-GPU throughput from 800,000 to 1.5 million tokens per minute.

### 📸 How Botika runs full-stack generative AI on Modal

Modal supports Botika’s entire AI stack, from processing a 100-terabyte image dataset to training foundation models and serving roughly 15 models in production. With Modal, its infrastructure can absorb a two- to threefold traffic increase in seconds without manual intervention.

### 🤖 Run Devin Outposts and Cursor Cloud Agents on Modal

You can now run Devin Outposts and Cursor Cloud Agent workers inside customizable Modal Sandboxes. Bring your own images, dependencies, secrets, and CPU or GPU resources while we handle isolated environments, fast startup, and elastic capacity for every session.

## ⚡ Runtime: a conference by Modal

Join us October 1st at The Midway in San Francisco for Runtime, our conference for engineers running AI in production. We’ll have three tracks covering inference, training, and agents, with technical deep dives and speakers including Scott Wu (Cognition), Bryan Catanzaro (NVIDIA), and Cat Wu (Anthropic).

[Explore the lineup and apply to attend →](https://modal.com/runtime)

## 📍Upcoming events

- Sep 15th — [Modal Rooftop Happy Hour: GTM Edition](https://luma.com/modal-4ufv) in New York
- Sep 19th — [{Tech: Europe} Agentic AI Hack](https://luma.com/ldn-hack) in London
- Sep 21st — [Modal x Pydantic: How We Build Dev Tools for You and Your Agents](https://luma.com/modal-72s8) in London
- Sep 22nd — [Computational Biology Hackathon with Anthropic, Modal, and Flagship Pioneering](https://luma.com/boston-comp-bio-hack) in Cambridge, MA
- Sep 22nd — [AI Engineer Warmup with H Company, Modal, and Black Forest Labs](https://luma.com/drd77d1r) in Paris
- Sep 25th — [Inference Engineering with Modal’s Charles Frye](https://luma.com/a5cpqc9o)
- Oct 1st — [Runtime by Modal](https://luma.com/runtime-by-modal) in San Francisco
- Oct 13th — [AI Builder’s Night](https://luma.com/aibuilders_techcrunch) in San Francisco

See all upcoming events on [Modal’s calendar](https://luma.com/modal-labs).
