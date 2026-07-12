---
title: Evaluating the USA vs Belgium World Cup matchup
topic: agents
subtopic: tool-use
secondary_topics:
- evals-observability/evaluation
summary: Uses a USA vs Belgium matchup example to evaluate web research agents, illustrating
  task design and judging for tool-using research workflows.
source: braintrust
url: https://www.braintrust.dev/blog/us-belgium-eval
author: Braintrust Team
published: '2026-07-06'
fetched: '2026-07-11T04:34:12Z'
classifier: codex
taxonomy_rev: 1
words: 723
content_sha256: e1a17f08497c13aeda2057eb1179e309602003e22f27a1e174228328a39d4ae2
---

# Evaluating the USA vs Belgium World Cup matchup

6 July 2026Izzy Hurley4 min

The [previous World Cup knowledge-graph post](https://www.braintrust.dev/blog/world-cup-knowledge-graphs) asked a broader question: when Parallel researches a football matchup, which configuration gives you the best source-backed map for the cost? That eval ran 48 group-stage matchups through six configurations, crossing two task architectures, monolithic and fan-out, with three Parallel processor tiers, `base`, `core`, and `pro`. Across 288 runs, Braintrust scored structural coverage, schema utilization, evidence quality, summary quality, and prediction behavior.

The eval produced a practical default. `monolithic-pro` and `fanout-pro` both landed around 80% composite quality, but `monolithic-pro` cost about $0.10 per run against `fanout-pro`'s $0.60. It also reached 99% `squad_completeness`, while the more evidence-sensitive `basis_coverage` and `evidence_coverage` scorers stayed at 26%. The graph can give you a strong research map, but the sources behind each relationship still matter.

With the US set to kick off against Belgium in their round-of-16 game, this follow-up applies the configuration the eval selected. Rather than rerunning the architecture comparison, it zooms in on one `monolithic-pro` Parallel research pass for a USA vs Belgium matchup.

The result is a lighter sequel to the original eval: the benchmark measured the tradeoffs, and the selected setup now collects the details that make a match more legible, including squad structure, key player availability, recent form, club overlap, direct player familiarity, and the history between the teams.

United States vs Belgium

2026 FIFA World Cup · Round of 16 · Monolithic pro research run

🇺🇸 United States

vs

🇧🇪 Belgium

62

Markers

5

Labels

30

Evidence

The graph contains 102 nodes, 137 edges, and 30 evidence records from the source run. Belgium comes through as the modeled favorite at 68%, with the graph emphasizing Lukaku and De Bruyne as attacking anchors, Balogun's red-card appeal as an availability signal, and a few tactical familiarity links that make the matchup more legible.[1](https://www.braintrust.dev#ref-1)

That verification step matters. The new run still surfaces Balogun's red card as a match-relevant availability edge, but it now records the suspension as lifted before the Belgium match. The eval context helps here: `monolithic-pro` is a strong default for gathering the map, but the graph is most useful when you inspect the underlying evidence and update live details before treating them as settled.

The matchup also has history. Belgium knocked the US out of the [2014 World Cup](https://en.wikipedia.org/wiki/2014_FIFA_World_Cup_knockout_stage#Belgium_vs_United_States), a match that finished 2-1 after extra time, with Kevin De Bruyne and Romelu Lukaku scoring for Belgium and Julian Green pulling one back for the US. The graph brings better tools to a familiar fixture.

Four relationships are especially useful to inspect:

- **Pulisic and Saelemaekers at AC Milan:**a cross-team club link that gives both sides tactical familiarity. Pulisic and Saelemaekers both appear in- [AC Milan's 2025-26 season statistics](https://en.wikipedia.org/wiki/2025%E2%80%9326_AC_Milan_season), including the goals and assists tables.
- **Robinson and Castagne at Fulham:**a shared-club flank connection that matters because both players sit close to likely wide-channel duels.- [Robinson](https://en.wikipedia.org/wiki/Antonee_Robinson)and- [Castagne](https://en.wikipedia.org/wiki/Timothy_Castagne)are both listed as Fulham players in current player records.
- **Doku versus Robinson:**a direct matchup edge that ties Belgian transition threat to a specific USA defensive assignment.
- **Balogun's red card:**an availability edge that shows both the value and the limit of the graph. It surfaces the right issue, then the updated run changes the interpretation from suspension risk to cleared availability.

The first eval gives this graph context. It showed that `monolithic-pro` produced near-top composite quality at a much lower cost than fan-out, while also surfacing an important limit: roster coverage can be strong even when grounding coverage is uneven. That is what makes the USA vs Belgium map useful. The eval made the agent's strengths and failure modes visible before applying it to a live matchup.

For this matchup, the graph turns the eval result into a usable workflow. It uses the configuration that performed best for the cost, then exposes the relationships and evidence behind the run's conclusion. Belgium's modeled edge is only one part of the story. The better result is a clearer pre-match picture, driven by an eval that made the agent measurable before making it useful.

1 The July 6 `monolithic-pro` run models Balogun's status
as `Balogun red-card ban suspended (R32)` and marks the edge `Balogun red card OVERRULED`, with tags for `suspension`, `R32`, and `cleared`. The supporting
evidence excerpt says he was available against Belgium after the red-card ban
was suspended on Jul 05, 2026.
