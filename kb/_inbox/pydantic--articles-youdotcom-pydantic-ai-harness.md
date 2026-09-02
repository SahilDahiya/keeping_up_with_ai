---
title: You.com is now a Pydantic AI capability
kind: blog
topic: null
subtopic: null
secondary_topics: []
summary: null
triage: null
skip_reason: null
source: pydantic
url: https://pydantic.dev/articles/youdotcom-pydantic-ai-harness
author: Laís Carvalho
published: '2026-09-01'
fetched: '2026-09-02T06:18:28Z'
classifier: null
taxonomy_rev: 2
words: 2489
content_sha256: 969363140a0cef5bebbcdc1babd58f2d2e460f9e1f964f6fd6bda33173b86f87
---

# You.com is now a Pydantic AI capability

![you.com and Pydantic](https://pydantic.dev/assets/blog/youdotcom-pydantic-ai-harness/youcom-pydantic.png)


[Pydantic AI Harness](https://pydantic.dev/docs/ai/harness/overview/) now has two new web search capabilities from [You.com](https://you.com/?utm_source=pydantic&utm_medium=partnership&utm_campaign=youdotcom-pydantic-ai-harness), `YouSearch` and `YouResearch`. Each one comes with web search APIs that provide real-time LLM-ready access to the web and perform deep research for agentic workflows.

Five APIs, two capabilities. `YouSearch` for surveying and reading, `YouResearch` for the questions a single lookup cannot settle.

| Capability | API | What it does | 
|---|---|---|
| `YouSearch()` | Web Search | Returns real-time web and news results, with query-relevant excerpts or full-page markdown attached to each result. | 
| `YouSearch()` | Contents | Gets clean, full-page content from a URL as HTML or Markdown. | 
| `YouResearch()` | Answer | Returns a synthesized, citation-grounded answer in one call. Every citation is verified against the source text before the answer comes back. You.com reports 93.48% on SimpleQA at a p50 of 2.67 seconds. | 
| `YouResearch()` | Research | Runs multi-step research and returns a well-cited answer, with effort levels from `lite` to`exhaustive` . | 
| `YouResearch()` | Finance Research | Multi-step research over a dedicated financial index of filings, transcripts, analyst coverage, and fundamentals. | 

Here is how each part works, and what to set before an agent starts reading the open web on your behalf.

## 

To illustrate how the two capabilities compare, two agents run the same prompt: **what is the latest price of silver per troy ounce**.

Here is the [gist](https://gist.github.com/laisbsc/47426a4445eb963aec38ab9052917167) with the full code. To run, follow the instructions below. This post is a walkthrough of the code shown in the gist.

In this example, the **lean agent** performs a single search with three results and a 2,000 character cap. It costs about $0.01. The **thorough agent** gets eight results and `full_page`, a second search wrapped in `PrefixTools` and pinned to two domains you add, and `YouResearch` returning a typed brief. It costs about $0.13. Both return the same two fields, a price and a date, and both nest under one [Logfire](https://pydantic.dev/logfire) span, so the bill reads straight off the trace tree.

## 

Start by installing the required libraries. I'm using [Pydantic AI](https://pydantic.dev/pydantic-ai) as the agent framework, [Pydantic Logfire](https://pydantic.dev/logfire) as the observability layer and Anthropic as the model provider.

```
uv add "pydantic-ai-harness[youdotcom,anthropic]" "pydantic-ai-slim[logfire]"
```
Create your access keys at [you.com/platform](https://you.com/platform?utm_source=pydantic&utm_medium=partnership&utm_campaign=youdotcom-pydantic-ai-harness), and your model provider's key. Export both with:

```
export YDC_API_KEY='your-you-com-api-key'
export PYDANTIC_AI_GATEWAY_API_KEY='your-gateway-api-key'
```
In this example, the model provider uses [Pydantic AI Gateway](https://pydantic.dev/ai-gateway) with `PYDANTIC_AI_GATEWAY_API_KEY`. To set your key, enable the Gateway in Logfire and click the API Keys tab, as shown on the video below. You can choose to set up a custom provider by bringing your own key (BYOK), or create a key using built-in providers on Logfire. This allows you to swap models seamlessly, set up spending caps, assign budgets per key or project, and more.

![Enabling the Gateway in Logfire, then creating a key from the API Keys tab](https://pydantic.dev/assets/blog/youdotcom-pydantic-ai-harness/setup_gateway_key.webp)


You can also use your model provider's API key directly (`ANTHROPIC_API_KEY`, in this case) and replace the Agent string with `'anthropic:claude-sonnet-5'` or any other model you'd like to use.

```
import logfire
from pydantic_ai import Agent
from pydantic_ai_harness import YouResearch, YouSearch
logfire.configure()
logfire.instrument_pydantic_ai()
lean_agent = Agent('gateway/anthropic:claude-sonnet-5', capabilities=[YouSearch(), YouResearch()])
result = lean_agent.run_sync('What is the latest price of silver?')
print(result.output)
```
One list entry, and the agent can search the web. It comes with its tools, instructions, and settings already wired together with `capabilities=[YouSearch(), YouResearch()]`.

Now add the settings that turn it into a survey:

```
import logfire
from pydantic import BaseModel, ConfigDict, Field
from pydantic_ai import Agent
from pydantic_ai_harness import YouSearch
logfire.configure()
logfire.instrument_pydantic_ai()
class SilverBrief(BaseModel):
    model_config = ConfigDict(extra='forbid')
    spot_price_usd_per_oz: float
    as_of: str = Field(description='The date and source the quoted price is from.')
lean_agent = Agent(
    'gateway/anthropic:claude-sonnet-5',
    instructions='Answer with the spot price and its date only. Do not explain what moved it.',
    output_type=SilverBrief,
    capabilities=[
        YouSearch(
            num_results=3,
            extraction_mode='highlights',
            max_text_chars=2_000,
            freshness='week',
        )
    ],
)
result = lean_agent.run_sync('What is the latest price of silver per troy ounce?')
print(result.output.spot_price_usd_per_oz)
```
Three settings cap what this agent can read. `num_results=3` cuts the default of ten. `extraction_mode='highlights'` returns query-relevant excerpts only, instead of entire page bodies. `max_text_chars=2_000` truncates anything that comes back, down from a default of 10,000. `num_results=3` × `max_text_chars=2_000` caps the agent at 6,000 characters of web text per call, whatever you ask it. `freshness='week'` keeps quotes older than a week out of the results.

`output_type=SilverBrief` sets the shape of the reply to a [Pydantic BaseModel](https://pydantic.dev/docs/validation/dev/concepts/models/), so you get a float and a date string, according to what you specify. It does not change how much reading happens first. Both return the same two fields, while the thorough run uses substantially more input and costs more to produce them.

## 

`web_search` defaults to `extraction_mode='highlights'`, so each result arrives as excerpts and looking at eight sources stays affordable. The model then picks what to read with `get_page`. Switch to `extraction_mode='full_page'` when you would rather have the markdown up front.

Full page text, from either tool, is capped at `max_text_chars`. The cap keeps the head of the document, since a page's lead usually carries the substance, and appends a `[... page text truncated at N characters]` marker so the model knows it is holding part of a page. `num_results` is enforced twice, once in the request to You.com and again on the response.

Empty results are not a failure. A query that matches nothing returns `No results found for {query!r}.`, which the model can pass to the user or use to reword the search. Real problems arrive as a `ModelRetry`: a rate limit, a URL that came back empty, a parameter You.com rejected, a network blip. The run continues and the model gets another go. Authentication, billing, and permission errors stop it, because those are yours to fix and no amount of retrying helps.

## 

Use `answer` for a question you expect one call to settle. Use `research` when it needs many searches and a synthesis across them. `finance_research` is the same loop tuned for financial analysis.

`research` waits for its result instead of returning a job to poll, and a deep pass regularly runs for minutes, so `timeout_ms` defaults to ten minutes. Effort is set per capability with `research_effort`: `lite`, `standard`, `deep`, or `exhaustive`. You.com also has a `frontier` level, which only runs as a background job, so it is not offered here. `finance_research` takes its own `finance_effort`, either `deep` or `exhaustive`.

For a structured report output, give `research` a JSON schema:

```
from pydantic import BaseModel, ConfigDict
from pydantic_ai_harness import YouResearch
class SupplierRisk(BaseModel):
    model_config = ConfigDict(extra='forbid')
    supplier: str
    exposure: str
    sources: list[str]
YouResearch(
    research_effort='deep',
    output_schema=SupplierRisk.model_json_schema(),
)
```
Without `extra='forbid'`, You.com rejects the schema. It only accepts one that closes itself to extra keys, and that config is what puts `additionalProperties: false` in the generated JSON. Leave it out and the model gets a validation error back on its first `research` call, several minutes in.

The other rule is checked earlier: You.com rejects a schema at `lite` effort, and the capability catches that pairing when you construct it.

## 

Every one of the five tools returns a [`ToolReturn`](https://pydantic.dev/docs/ai/tools-toolsets/tools-advanced/#advanced-tool-returns). The model sees `return_value`, the text, with a `Sources:` block appended when the tool has citations. Your application reads `metadata['sources']`, the same sources as `YouSource` records:

```
from pydantic_ai.messages import ToolReturnPart
for message in result.all_messages():
    for part in message.parts:
        if isinstance(part, ToolReturnPart) and part.metadata:
            for source in part.metadata.get('sources', []):
                print(source['url'], source['title'])
```
The model never sees metadata, so nothing here competes for context, and the footnotes in your UI never depend on the model repeating a URL correctly. `web_search` puts the response's `search_uuid` and `latency` in there too, which is what you want in a trace when a run went sideways, and you need to ask You.com about one specific query.

## 

Both capabilities take the same controls, and they reach `web_search`, `answer`, and `research`. `finance_research` is the exception: it takes its input and `finance_effort`, nothing else, so a domain filter you set will not narrow it. `include_domains` is an allowlist and cannot be combined with either. `exclude_domains` and `boost_domains` do combine, so a denylist and a re-rank work together. `freshness` takes `day`, `week`, `month`, `year`, or a `YYYY-MM-DDtoYYYY-MM-DD` range, and `country` takes a two-letter code. Bad values raise at construction time.

One agent, two search setups, is a common ask: the open web for context, a couple of trusted domains for anything it will cite. Two instances of the same capability would register the same tool names, so wrap the second in core's `PrefixTools`:

```
import logfire
from pydantic_ai import Agent
from pydantic_ai.capabilities import PrefixTools
from pydantic_ai_harness import YouSearch
logfire.configure()
logfire.instrument_pydantic_ai()
thorough_agent = Agent(
    'gateway/anthropic:claude-sonnet-5',
    instructions=(
        'You must call `research` exactly once and base the brief on what it '
        'returns; do not answer from search results alone. Use '
        '`trusted_web_search` only to confirm the number you quote as the spot '
        'price, and `web_search` to survey context before the research pass.'
    ),
    output_type=SilverBrief,
    capabilities=[
        YouSearch(
            num_results=8,
            extraction_mode='full_page',
            max_text_chars=20_000,
            freshness='week',
        ),
        PrefixTools(
            wrapped=YouSearch(
                num_results=3,
                include_domains=['lbma.org.uk', 'kitco.com'],
                guidance='',
            ),
            prefix='trusted',
        ),
        YouResearch(
            research_effort='deep',
            output_schema=SilverBrief.model_json_schema(),
        ),
    ],
)
```
The agent above removes the lean agent's limits, adds a second search pinned to two domains, and sends the write-up through `research`.

Set `guidance=''` on the wrapped instance, or replace it with text explaining when the prefixed tools apply. Otherwise, both instances contribute the same default paragraph.

The same naming rule is why an agent gets one web search capability. Anything else registering a `web_search` tool collides with `YouSearch`, and the agent fails at construction rather than at the first call. Wrap one of them in `PrefixTools` if you want both.

## 

Eight results at `full_page` and 20,000 characters each is a 160,000 character ceiling, against the lean agent's 6,000. Both runs nest under one Logfire span, so the token counts sit next to each other in the trace tree:

The two differ in `capabilities` and `instructions`; the capability differences are:

|  | lean | thorough | 
|---|---|---|
| survey | `highlights` , 3 results, 2,000 chars | `full_page` , 8 results, 20,000 chars | 
| trusted source | none | `trusted_web_search` on lbma.org.uk and kitco.com | 
| research pass | none | `YouResearch(research_effort='deep')` | 

Each run calls both agents back to back on the same question, so the lean number and the thorough number come from the same minute of the web. The figures below are five such runs, and the headline is the median of the five ratios.

|  | lean | thorough | 
|---|---|---|
| input tokens | 7,937 | 65,987 | 
| output tokens | 159 | 358 | 
| wall time | 5.5s | 26.3s | 
| cost per run | $0.01 | $0.13 | 
| tool calls | 1 | 3 | 

Eight times the input for the same two fields. Across the five runs the paired ratio ran from 5.4x to 11.8x, median 8.2x.

One tool call accounts for most of that. `research` took a median 16.3 seconds, 62% of the thorough run's wall time, and carries most of the token difference.

Instructions decide whether the expensive tool runs at all. `research_effort` only decides how long it runs once it does. With the wording above, `research` was called in all five runs and the thorough agent's input tokens varied by 1.4%, from 65,075 to 67,698.

The lean agent's input tokens varied from 5,581 to 12,160 across the same five runs, because nothing anchors what a highlights search returns except what the web served when the agent called.

Five runs inside seven minutes measures the configuration. It does not measure how either agent behaves on a day when silver is actually moving.

Whether the trade is worth making is a question for the human in the loop. The thorough brief cites its sources and checks the quoted price against a domain. The lean one returns a number from the open web in five seconds.

## 

An agent that reads the web is an agent whose answers depend on things you do not control. Pages change, a search returns something odd, a summary quietly drops the one source that mattered. None of that has to be guesswork. The tool definitions are typed and the outputs are validated, so a malformed result fails where you can see it, and [Pydantic Logfire](https://pydantic.dev/logfire) keeps the receipt: which queries ran, what came back, which pages were read in full, and what the whole run cost.

You.com's contribution is retrieval that already distinguishes an excerpt from a page from a research pass, so your agent code does not have to invent that distinction on top of a single search endpoint.

Some caveats before you ship:

- Harness is on 0.x releases, so the API can change between minor versions. Changes come with deprecation warnings and migration guidance in the release notes.
- `research` blocks for the length of the pass. At`deep` or`exhaustive` , size the surrounding request timeouts for minutes, not seconds.
- A prebuilt `client` is used as given, so its timeout and host are yours to configure.`timeout_ms` only applies to the default client.
- Domain filters shape what the agent can see. They are not a security boundary for what it can be told by a page it does read.

## 

Get a key at [you.com/platform](https://you.com/platform?utm_source=partner-pydantic&utm_medium=referral&utm_campaign=2026-08-pydantic-integration), your model provider's key, and add `YouSearch()` to your web search Pydantic AI agents. Instrument with Logfire to see all the steps in between, validate your prompts, and analyze performance. You can get a working web-reading agent that takes about two minutes to set up.

When you want more than the first run:

- The [You.com capability docs](https://pydantic.dev/docs/ai/harness/youdotcom/) carry the full reference for`YouSearch` ,`YouResearch` , and their toolsets.
- The [Pydantic AI Harness capabilities](https://pydantic.dev/docs/ai/capabilities/overview/) docs list every available capability, written to be read and copied, with examples and tool descriptions behind each capability.
- You.com keeps [four worked cookbooks](https://github.com/youdotcom-oss/pydantic-cookbook) of their own, each grounded in a different field: an antimicrobial resistance brief through`research` , a survey of K-12 teacher retention on`YouSearch` , a private credit read through`finance_research` , and a due-diligence desk that routes across all three with`SubAgents` . Start there if your domain is closer to one of those than to a generic search agent.
- Every agent above is traced with [Pydantic Logfire](https://pydantic.dev/logfire) , which turns each run into a trace you can open and query with SQL: searches, page reads, retries, token costs. Keep the[Logfire MCP server](https://pydantic.dev/docs/logfire/guides/mcp-server/) open while you debug one and your agent can read its own traces back to you.
- [Pydantic Evals](https://pydantic.dev/docs/ai/evals/evals/) is the next thing you want once the agent is choosing its own sources, so a prompt change that sharpens one question does not blunt another.

If you build something good with this, we would like to see it. The harness lives on [GitHub](https://github.com/pydantic/pydantic-ai-harness), the issues are open, and the capability shelf grows mostly because people tell us what is missing from it. Come say hello in the [Pydantic Slack](https://pydantic.dev/docs/logfire/join-slack/).

Together, these are pieces of [the Pydantic Stack](https://pydantic.dev/). Try it out!
