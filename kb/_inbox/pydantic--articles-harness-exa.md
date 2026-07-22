---
title: Building a research agent with Pydantic AI Harness and Exa
kind: blog
topic: null
subtopic: null
secondary_topics: []
summary: null
triage: null
skip_reason: null
source: pydantic
url: https://pydantic.dev/articles/harness-exa
author: Bill Easton
published: '2026-07-21'
fetched: '2026-07-22T06:57:07Z'
classifier: null
taxonomy_rev: 2
words: 1241
content_sha256: 5dbade0aa2d79bc34ed92b142f5d26960f215befa0add84157c314439bab2128
---

# Building a research agent with Pydantic AI Harness and Exa

Yesterday laid out the parts. Today the argument gets a real test: "before we commit to the migration, can it research the vendor options?" The reflex says no, wrong agent. The reflex is thinking in agents. This week is about thinking in parts.


Ten lines gets you a working research agent. Pydantic AI's core ships [ WebSearch](https://ai.pydantic.dev/api/capabilities/), a capability that turns on the model's own native web search — Anthropic, OpenAI, Google, and Groq all have one:

```
import logfire
from pydantic import BaseModel
from pydantic_ai import Agent
from pydantic_ai.capabilities import WebSearch
logfire.configure()
logfire.instrument_pydantic_ai()
class Finding(BaseModel):
    claim: str
    source_url: str
class Report(BaseModel):
    summary: str
    findings: list[Finding]
agent = Agent(
    'anthropic:claude-opus-4-7',
    output_type=Report,
    capabilities=[WebSearch(allowed_domains=['docs.aws.amazon.com'])],
)
result = agent.run_sync(
    'What HA options does RDS for Postgres offer today?'
)
```
For a factual lookup with a small blast radius, this is enough, and `output_type=Report` means the answer already comes back as validated data. But the ceiling is low: native web search returns links and snippets scored by the provider's index and doesn't give you a page-contents step, deep-research mode, or the kind of retrieval control a research agent needs when the question earns more than a lookup. Which is when the fastest path to a production-grade research agent stops passing through the shelf.


A research agent is only as good as its retrieval, and the retrieval most agents get, scrape ten blue links and hope, is the bottleneck that makes "deep research" shallow. The agents that make their living reading the web have all quietly settled on the same eyes.

[Exa](https://exa.ai)'s tagline is the literal spec: "web search, built for AI agents." Semantic search over the live web with page contents returned in the same call, no scraping step, and a range they describe as [low-latency to deep research in one API](https://exa.ai/docs/reference/search-api-guide): an `instant` mode for the quick lookups, `auto` for balanced retrieval, and `deep`/`deep-reasoning` for questions that earn a multi-step pass with structured outputs. Coding agents live on that range: Exa powers Cursor's search across docs and repos, and Cognition co-founder Walden Yan is on record that ["Exa powers all parts of Devin."](https://exa.ai/) If the agent that ships production code trusts Exa for its web-facing brain, the research agent you assemble today can too.


The superpower version is one capability. When *research is the whole question* — plan, sub-searches, page reads, synthesis, citations — Exa runs it as a hosted service, the [Exa Agent API](https://exa.ai/docs/reference/agent-api-guide), and the harness ships it as a one-line wrapper:

```
import logfire
from pydantic_ai import Agent
from pydantic_ai_harness.exa import ExaAgent
logfire.configure()
logfire.instrument_pydantic_ai()
agent = Agent(
    'anthropic:claude-opus-4-7',
    capabilities=[ExaAgent()],
)
result = agent.run_sync(
    'Which managed Postgres should we migrate to? Compare pricing, HA, '
    'and migration path from RDS across the main contenders. Cite every claim.'
)
```
`ExaAgent` adds one tool, `exa_agent`. The parent hands over the question, the Exa Agent API runs a multi-step research pass on their infrastructure (up to an hour if the question earns it), and the tool call defers until the run finishes with a cited answer. Follow-ups keep the run's context via `previous_run_id`, so a second question about the shortlisted vendors doesn't restart from zero. Want structured output? Pass a Pydantic model as `output_schema=Report` and the completed run's result is validated on the way back; a mismatch surfaces as a retry instead of silently landing.

This is the parts-list punchline for research: the parent agent gets a researcher on staff, context isolation included, and the hundred thousand tokens spent reading sources land on Exa's side of the API call. That's the sub-agent pillar of "deep agents" delivered as a capability import — no assembly required.


Sometimes you *do* need to build: sources you allowlist, a citation bar the model has to clear, notes that accumulate across runs, a research process that fits how your team actually works. Then the harness's shelf earns its keep. Same Exa retrieval, exposed as individual tools this time via [ ExaSearch](https://github.com/pydantic/pydantic-ai-harness/tree/main/pydantic_ai_harness/exa) — 

`web_search` returns each hit with its most relevant excerpts (so surveys stay cheap) and `get_page` reads a chosen URL in full, both with the research strategy that turns two tools into one shipped inside the capability — plus the harness parts that give a long run its spine:```
import logfire
from pydantic import BaseModel
from pydantic_ai import Agent
from pydantic_ai_harness import CodeMode
from pydantic_ai_harness.exa import ExaSearch
from pydantic_ai_backends import ConsoleCapability             # filesystem
from pydantic_ai_summarization import ContextManagerCapability # compaction
from pydantic_ai_todo import TodoCapability                    # planning
logfire.configure()
logfire.instrument_pydantic_ai()
class Finding(BaseModel):
    claim: str
    source_url: str
class Report(BaseModel):
    summary: str
    findings: list[Finding]
agent = Agent(
    'anthropic:claude-opus-4-7',
    output_type=Report,
    capabilities=[
        CodeMode(),
        TodoCapability(),
        ConsoleCapability(),
        ContextManagerCapability(max_tokens=180_000),
        ExaSearch(
            include_deep_search=True,
            include_domains=['docs.aws.amazon.com', 'planetscale.com', 'neon.tech'],
        ),
    ],
)
```
`include_deep_search=True` exposes a third tool, `deep_search`, Exa's multi-step deep mode as a single call for the questions that deserve it, and the capability's guidance grows one sentence to teach the model when to escalate. `include_domains` narrows retrieval to the vendors' own docs — a rule the model can't reword its way around. The todo list keeps a three-hour run pointed at the question, files hold the notes and the draft between compactions, and every claim in the report traces to a URL Exa actually returned. Instrument the whole thing with [Logfire](https://pydantic.dev/logfire) and one trace shows the plan, each sub-search, and the synthesis — which is how you debug a researcher.


Because it's the week's argument in miniature, told in three lines of imports. Start with what ships. Level up when the ceiling gets in the way. Compose when the shape of the problem needs to be yours. Same agent from Monday all the way down, picking up one capability at each step, always answering to the same public API. That's what a standard library *is*: the point where "build a research agent" stops meaning "start a project" and starts meaning "compose an afternoon."

It also composes forward. [When agents build agents](https://pydantic.dev/articles/when-agents-build-agents) ends on loops that run, learn, and re-arm; a research loop that keeps its notes in files and its plan in todos re-arms with everything it learned yesterday, and Exa is the part that keeps its eyes fresh — live search each cycle, not a crawl that ages. The report you commission next is the worst one it will ever write.

Agents Week opened with an argument about herds: you'll run more agents than you can hand-raise. The reason that's survivable is the recomposition you just watched: agents assembled from shared, swappable, inspectable parts are cattle by construction. The bespoke agent, the one built from scratch around a private framework, was always the pet.


`pydantic-ai-slim` already carries `WebSearch`, so the native version costs nothing more than the model provider you're already paying. `uv add "pydantic-ai-harness[exa]"` puts both `ExaAgent` and `ExaSearch` on the shelf, and an [Exa API key](https://dashboard.exa.ai) in `EXA_API_KEY` connects them — the free credits cover all three agents in this post. Layer in `[codemode]` and the community packages (`pydantic-ai-backend`, `summarization-pydantic-ai`, `pydantic-ai-todo`) when you're ready to compose the deeper build. The [capability matrix](https://github.com/pydantic/pydantic-ai-harness#capability-matrix) tracks the rest of the parts list, first-party and community, and every row is an issue or PR where your vote steers what gets built next.

A research agent for the cost of an import — a lookup, a hosted researcher, or an afternoon spent composing the loop you actually want. The rest of the week is the same move on harder ground: the review loop running at agent speed Wednesday, real compute Thursday, then a cloud the agent is allowed to break Friday.
