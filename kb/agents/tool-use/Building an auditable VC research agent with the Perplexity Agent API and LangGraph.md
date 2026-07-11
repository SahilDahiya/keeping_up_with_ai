---
title: Building an auditable VC research agent with the Perplexity Agent API and LangGraph
topic: agents
subtopic: tool-use
secondary_topics:
- evals-observability/tracing
summary: Walkthrough for building an auditable VC research agent with Perplexity,
  LangGraph, and LangSmith, emphasizing traceability and review.
source: langchain
url: https://www.langchain.com/blog/build-an-auditable-vc-research-agent-with-the-perplexity-agent-api-langgraph-and-langsmith
author: Srimanth Tangedipalli Karan Singh Ryan Buchmayer
published: '2026-06-26'
fetched: '2026-07-11T04:37:09Z'
classifier: codex
taxonomy_rev: 1
words: 975
content_sha256: 0e8526ac6cb5d74e46c8b962aff44beafc1c480ca14580f952ee842fb0d3832e
---

# Building an auditable VC research agent with the Perplexity Agent API and LangGraph

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/6a4fbf8cc203188df1011f03_logo%20and%20title%20-%2020%20characters%20max%20(10).png)

Before a venture fund writes a check, someone has to write the memo. An investment memo is the internal document an analyst takes to the investment committee to debate whether the investment is sound. Memo topics might include thesis, market sizing, traction, team, competition, risks, and a final recommendation. This is the document partners actually vote on, and a typical draft can require tens of hours of research and writing.

Funds review far more opportunities than they fund, so the bulk of initial research is on companies that get passed on. Analysts still spend hours gathering information across Crunchbase, PitchBook, IR pages, earnings coverage, and news, then checking every number by hand.

We built an agent that produces a first-pass version of that memo in about ninety seconds for roughly $0.40 in API cost, with every claim traced to a primary source. Analysts can start from that cited draft and sharpen it instead of building from scratch, saving the hours it would otherwise take. It works in two stages: research nodes gather evidence in parallel, then a separate synthesizer writes the memo from only what they found.

The agent takes a company name and produces a citation-grounded memo with seven sections: Snapshot, Team, Financials, Product, Market, Risks, and a Thesis that ends in a one-line recommendation. It runs on the [Perplexity Agent API](https://docs.perplexity.ai/docs/agent-api/quickstart) and its built-in `web_search` and `finance_search` tools, with [LangGraph](https://langchain-ai.github.io/langgraph/) for orchestration and [LangSmith](https://docs.langchain.com/langsmith/home) for evaluation.

## Architecture

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/6a4fc513b4035da3daa16649_perplexity-langchain-architecture-highres.png)

*Four research nodes run in parallel, then a tool-less synthesizer assembles the memo.*

Four research nodes (team, financials, product, market) run in parallel from the start. Each one is a Perplexity Agent API call with its own tools and search budget. The financials node adds [ finance_search](https://docs.perplexity.ai/docs/agent-api/finance-search) for structured financial data; the others use

[. After all four finish, a single synthesizer node assembles the memo. In LangGraph the wiring is short:](https://docs.perplexity.ai/docs/agent-api/tools/web-search)

`web_search````
def build_graph():
    g = StateGraph(MemoState)
    g.add_node("team", team_node)
    g.add_node("financials", financials_node)
    g.add_node("product", product_node)
    g.add_node("market", market_node)
    g.add_node("synthesizer", synthesizer_node)
    for section in ("team", "financials", "product", "market"):
        g.add_edge(START, section)        # fan out from START, in parallel
        g.add_edge(section, "synthesizer")  # ...and back into the synthesizer
    g.add_edge("synthesizer", END)
    return g.compile()
```
State management is important here. Each research node only reads `state["company"]` and doesn't depend on other nodes' output. Their writes all land on one `research_output` key, but in our full code that key uses a reducer, which merges the four concurrent writes by section name instead of letting them collide. Without that reducer, two parallel writes to the same key would raise LangGraph's [ InvalidUpdateError](https://langchain-ai.github.io/langgraph/troubleshooting/errors/INVALID_CONCURRENT_GRAPH_UPDATE/) (see the

[reducers reference](https://langchain-ai.github.io/langgraph/concepts/low_level/#reducers)for the pattern). Scoping each node to one domain pays off too: team, financials, product, and market each get their own tools, search budget, and prompt, so a node's context stays focused on the domain it is responsible for.

## A tool-less synthesizer

The synthesizer has no tools. It composes all seven memo sections from the four nodes' research outputs, so every cited claim is grounded in research one of the nodes actually did. Sections 1-6 each end with a `### Citations` list pairing every source URL with the evidence it supports. The Thesis is the one analysis-only section, with no citations.

Every node's tool calls and outputs are captured in LangSmith, so you can take any line in the finished memo and trace it back through the synthesizer to the search result that produced it.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/6a4ebe6d613d6a8a48162a18_langsmith-trace.png)

*One memo run in LangSmith (*


*explore the trace**). Every claim traces back to the search result that produced it.*

## Choosing a search provider

Which search provider should back the agent? We scored three in LangSmith across ten companies, with custom evaluators for primary-source rate and financial-concept coverage, alongside built-in cost and latency. Primary-source rate is the share of a memo's citations that point to IR pages, SEC filings, and official press rather than aggregators like Wikipedia or Crunchbase.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/6a4ebeb5db6169004a2b8242_langsmith-comparison.png)

*Three providers, the same graph, scored side by side in LangSmith.*

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/6a4ebf62f905ef5ab712fee9_Screenshot%202026-07-08%20at%202.21.14%E2%80%AFPM.png)

*Results from a single run across ten companies, on openai/gpt-5.5*


The right provider depends on your use case. Cost, latency, and a measure of search accuracy like primary-source rate are good starting points, but use the [cookbook](https://docs.perplexity.ai/docs/cookbook/articles/langchain-vc-memo-agent/README) to define and score your own metrics.

## What it produces

A trimmed Thesis section from a run on Anthropic:

At a confirmed ~$380B post-money valuation, the company is already priced as a generational platform, while the available financial evidence remains run-rate rather than audited revenue. We should not lead at this valuation without deeper diligence.Recommendation: TRACK

The section list and the PASS / TRACK / ADVANCE / LEAD scale are just the format we picked; swap in whatever your team uses.

It is a starting draft, not a finished memo: strongest for well-documented companies, weaker for thinly-covered private ones, and the Thesis is the model's own analysis rather than a cited section. An analyst should still check it before relying on it.

## Takeaways

- **Let LangGraph handle concurrency.**Run nodes in parallel and let a reducer on the shared state merge their concurrent writes, so you get the parallel speedup without coordinating those writes yourself.
- **Ground every claim in retrieved evidence.**When the writing step can only draw on what an earlier search step found, each claim traces back to a real source instead of a hallucinated one, keeping the result auditable end to end.
- **Make provider choice an experiment.**Custom LangSmith evaluators turn "which provider?" into scores you can compare across runs, so the answer depends on your use case rather than a vendor claim.

**Next steps:** swap in your firm's memo template, add an evaluator for a metric you care about, or run the agent on your own portfolio.

👉 [ Open the full cookbook](https://docs.perplexity.ai/docs/cookbook/articles/langchain-vc-memo-agent/README): the runnable code, all three provider profiles, and the LangSmith eval harness.

**Related content:**

[Perplexity Agent API tools](https://docs.perplexity.ai/docs/agent-api/tools)·

[LangChain Perplexity provider](https://docs.langchain.com/oss/python/integrations/providers/perplexity)·

[LangSmith evaluation](https://docs.langchain.com/langsmith/evaluation)
