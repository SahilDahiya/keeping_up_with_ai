---
title: Linguistic drift at the frontier | Pydantic
kind: blog
topic: agents
subtopic: harness
secondary_topics:
- prompt-engineering/structured-output
summary: Uses GitHub PR and README analysis to show Claude models (starting with Opus
  4.6) seeding a vocabulary tic -- using 'seam' for any interface/boundary -- that
  then propagates across other frontier models (GPT, DeepSeek, Qwen, GLM) as human-written
  code carrying the term becomes training/context data; quantifies it with a log-odds-ratio-over-Dirichlet-prior
  classifier on 4,319 pre-2025 vs. 1,047 2026 GitHub READMEs. Introduces vocabguard,
  an open-source Pydantic AI 'Capability' that hooks into an agent's structured-output
  fields, tool arguments, and text output to detect and rewrite drifted vocabulary
  before it reaches users.
triage: null
skip_reason: null
source: pydantic
url: https://pydantic.dev/articles/linguistic-drift-at-the-frontier
author: Michael Pfaffenberger
published: '2026-08-26'
fetched: '2026-09-05T06:14:38Z'
classifier: claude
taxonomy_rev: 2
words: 2384
content_sha256: 1bfdfd53e529d47a7ddbc1c6a8df2fc49d8517b94b097dc35ec46b41eef8d3e5
---

# Linguistic drift at the frontier | Pydantic

I've noticed some strange behavior coming out of the top frontier models lately. Models are getting better and better at coding, design, problem solving, and more. However, when it comes to prose, I can no longer stand the output. It's absolutely infuriating. What has caused this?

Most recently [Anthropic](https://www.anthropic.com/) Claude models began using the word "***seam***" to represent any point in a software (or otherwise) system where two components connect. I have never heard this term used before. While I don't consider myself authoritative in software terminology, typically I would use the term "interface" or maybe even something as basic as "contract" (SDK or API contract, right?). I don't think I'd ever heard "***seam***" to represent this, however, until recently when Fable 5 started barfing it everywhere into my codebases.

And we're going to attempt to address this phenomenon with a [Pydantic AI Capability](https://pydantic.dev/docs/ai/capabilities/overview/). Your mileage may vary, but at the very least, my words may strike a chord with your intellectual and philosophical side, and additionally, you will see how easy it is to create agentic harness features using the powerful abstractions available in [Pydantic AI](https://pydantic.dev/docs/ai/overview/) and [Pydantic AI Harness](https://github.com/pydantic/pydantic-ai-harness).

![Cartoon of three robots labeled GPT 5.6 Sol, Claude Fable 5.1, and Z.AI GLM 5.3 calling an orange a melon, while the man holding the orange looks confused and a woman insists her Claude told her they are melons](https://pydantic.dev/assets/blog/linguistic-drift-at-the-frontier/melon-robots.jpg)


I cleared my context one day, and asked Fable 5.1: "Why are you talking about seams all the time whenever you are describing a point where software components meet?" Fable 5.1 got notably defensive and cited a book from 2004, Michael Feathers' [*Working Effectively With Legacy Code*](https://www.informit.com/store/working-effectively-with-legacy-code-9780131177055). Fable's rigorous reinforcement learning dug up an archaic term from decades ago and it has demonstrably proliferated.

![Google Trends interest over time for the search term seam in the United States, 2004 to present: flat between 20 and 40 for two decades, then a spike to 100 in 2026](https://pydantic.dev/assets/blog/linguistic-drift-at-the-frontier/google-trends-seam.png)


I showed it this [Google Search Trends](https://trends.google.com/trends/) image, and Fable was justifiably defensive. The spike is very suspicious but `seam` obviously isn't a software-specific word. So I actually pointed it at [GitHub](https://github.com/) and asked it to query PRs for the word "***seam***". It found ~700,000. ~685,000 of them are from 2026. The remaining ~15,000 were all from before 2026.

![GitHub pull requests mentioning seam by year created, 2010 to 2026: near zero every year, 8,149 in 2025, then 685,143 in 2026 through September 2](https://pydantic.dev/assets/blog/linguistic-drift-at-the-frontier/seam-prs-by-year.jpg)


Then I asked Fable 5.1 if it could check to see if those PRs had the typical [Claude Code](https://docs.claude.com/en/docs/claude-code) co-authorship note in commit messages. The results are quite conclusive.

| Fingerprint in PR body | Count | Share of seam PRs | Share of all 2026 PRs | Over-rep. | 
|---|---|---|---|---|
| " [Claude Code](https://docs.claude.com/en/docs/claude-code) " | 307,971 | **45%** | 12.5% | **3.6x** | 
| "Generated with Claude Code" (exact footer) | 247,275 | **36%** |  |  | 
| " [Codex](https://openai.com/codex/) " | 119,845 | 17.5% | 5.8% | 3.0x | 
| " [Copilot](https://github.com/features/copilot) " | 53,726 | 7.8% | 5.2% | 1.5x | 
| " [Cursor](https://cursor.com/) " | 51,974 | 7.6% |  |  | 
| " [Gemini](https://gemini.google.com/) " | 25,514 | 3.7% |  |  | 
| " [Devin](https://devin.ai/) " | 4,970 | 0.7% |  |  | 

And while this isn't wrong at all, per se, it does represent what I like to refer to as linguistic drift, which is something that I think all users of AI should be aware of, and potentially *worried* about.

Further aggravating is that the linguistic drift itself proliferates from one model to another. While I've been loving working with Anthropic Claude's Fable 5 (and now 5.1) for the past couple of months, my codebases are covered in the word "***seam***", in comments, in doc-strings, and in markdown files. Now, when I use [OpenAI](https://openai.com/)'s GPT 5.6 Sol, [DeepSeek](https://www.deepseek.com/) v4 Flash 0731 (I love this model so much btw), [Qwen](https://github.com/QwenLM) 3.8 27b, or even the brand new [Z.AI](https://z.ai/) GLM 5.3 Flash, they all read my existing codebase and talk about "***seams***".

I had to go a little deeper. What was LLM Patient Zero? The answer is pretty clear. Opus 4.6 was Patient Zero, and the tendency to use the word seam slowly proliferated, later being amplified even further by Opus 4.7, and spiking *hard* when Opus 4.8 dropped.

![Weekly GitHub pull requests mentioning seam from November 2025 to August 2026, with a vertical line at each Claude model release. The curve steps up after Opus 4.6, Opus 4.7, Opus 4.8, and Fable 5, reaching 65,197 per week](https://pydantic.dev/assets/blog/linguistic-drift-at-the-frontier/seam-prs-weekly.png)


What we have here is a good old fashioned feedback loop. Oh boy!

![Diagram titled How a word goes viral among models: model output, to human artifact, to context for another model, to model output, with a loop back labeled each lap makes the word a little more normal](https://pydantic.dev/assets/blog/linguistic-drift-at-the-frontier/feedback-loop.png)


It doesn't stop with "***seam***". It goes way deeper. I wanted to try to quantify this so I started scraping GitHub READMEs. Well, first I tried to get a dataset off of [HuggingFace](https://huggingface.co/) but didn't find much. I managed to scrape 4,319 pre-2025 READMEs stratified across 22 languages, and then 1,047 2026 READMEs from repos with Claude Code commits. On the pre-2025 set I had the constraint of greater than 500 stars to filter out pure slop. The 2026 set has no star filter. I fed them through a [`TF-IDF`](https://en.wikipedia.org/wiki/Tf%E2%80%93idf) (Term Frequency - Inverse Document Frequency) vectorizer -> [Singular Value Decomposition](https://en.wikipedia.org/wiki/Singular_value_decomposition) (`SVD`) -> [`t-SNE`](https://en.wikipedia.org/wiki/T-distributed_stochastic_neighbor_embedding). Side note: omg yes I'm really using traditional NLP techniques because not everything needs to be a transformer.

Green = pre-2025

Orange = 2026

![t-SNE scatter plot of 4,319 pre-2025 READMEs in green and 1,047 2026 READMEs in orange. The green points form one broad cloud; most orange points form one dense cluster at the bottom, with a few small satellite clusters and the rest scattered inside the green](https://pydantic.dev/assets/blog/linguistic-drift-at-the-frontier/tsne-readmes.png)


This is linguistic drift visualized.

Is this AI psychosis en masse? Do we fight back against it or simply accept that the correct terminology that describes a coupling point of system components is the word "***seam***"? Should we all adopt the new vocabulary that our AI overlord has chosen? For a moment, think about the meaning of the vocabulary you've learned and used for most of your life. Did the terms and expressions you use in your daily life come from a central authority, government, or mega-corporation? Sometimes yes, when [a single brand became prolific](https://en.wikipedia.org/wiki/Generic_trademark) (Google, Kleenex, etc.). But mostly, no, it came from humans. Authoritative experts whose work went through rigorous peer review in the case of an academic term, or it came from human influences, such as writers, artists, poets, and musicians.

I won't get too philosophical about the long term prospects of AI induced psychosis on a societal scale. But here is a scary situation that I'd like to propose to plant a seed in your mind. Imagine we work for an airline and we've created an agent which performs intake of customer service tickets. Our agent is very simple. It would have one tool call to do retrieval of similar tickets to help classify the ticket, and it has one which fetches customer data. The goal is to dig up as much data about the customer and similar tickets as possible to pass onto the triage team (which is live humans).

Let's look at how we might build this as a [Pydantic AI Agent](https://pydantic.dev/docs/ai/core-concepts/agent/).

```
from dataclasses import dataclass
from pydantic import BaseModel
from pydantic_ai import Agent, RunContext
@dataclass
class Ticket:
    customer_id: str
    subject: str
    body: str
@dataclass
class Deps:
    customers: dict[str, dict[str, str]]
    tickets: list[dict[str, str]]
class TriageBrief(BaseModel):
    category: str
    priority: str
    summary: str
agent = Agent(
    "openai:gpt-5.6-luna",
    deps_type=Deps,
    output_type=TriageBrief,
    instructions=(
        "Triage airline support tickets for a human team. "
        "Always retrieve the customer profile and similar past tickets "
        "before writing a concise brief."
    ),
)
@agent.tool
async def get_customer(
    ctx: RunContext[Deps], customer_id: str
) -> dict[str, str]:
    return ctx.deps.customers.get(customer_id, {})
@agent.tool
async def similar_tickets(
    ctx: RunContext[Deps], query: str
) -> list[dict[str, str]]:
    terms = query.casefold().split()
    return [
        ticket
        for ticket in ctx.deps.tickets
        if any(term in ticket["summary"].casefold() for term in terms)
    ][:5]
ticket = Ticket(
    customer_id="C-123",
    subject="Delayed baggage",
    body="My checked bag did not arrive with flight PA123.",
)
deps = Deps(
    customers={"C-123": {"name": "Ada Lovelace", "status": "Gold"}},
    tickets=[
        {
            "category": "missing baggage",
            "summary": "Checked bag arrived one day after the passenger.",
        }
    ],
)
result = agent.run_sync(
    f"Customer: {ticket.customer_id}\n"
    f"Subject: {ticket.subject}\n"
    f"{ticket.body}",
    deps=deps,
)
brief = result.output
```
This is a fully hypothetical scenario, but the structured output field that I'm most interested in for this blog post would be the `summary`. The summary is meant to give the downstream human triage team a bunch of concise information. Those humans' eyes are probably trained to key instantly off of certain terms like "missing baggage" or "delayed".

Now let's pretend that Fable 5.1 decides, oh, in an authoritative Airline Customer Service book called *Working Effectively With Legacy Aviation Systems*, uses the term "doodled" to mean "delayed". Okay, okay, okay... this is 100% hyperbole, but hopefully you can see the point. [Spirit Airlines](https://en.wikipedia.org/wiki/Spirit_Airlines) (RIP) swaps their ticket intake agent over to `anthropic:claude-sonnet-5` from `openai:gpt-4o` and all of a sudden the triage team starts calling HQ asking *"What does it mean if a flight was `doodled`?"*  ... Chaos ensues.

![Cartoon of a Spirit Airlines office on fire, staff panicking on the phone about 400 doodled flights, a monitor reading 400 DOODLED FLIGHTS, and one manager shouting that they are bankrupt again](https://pydantic.dev/assets/blog/linguistic-drift-at-the-frontier/doodled-flights.jpg)


This dystopian hypothetical future is preventable. We are not helpless. We are harness engineers. We can use [Pydantic AI Capabilities](https://pydantic.dev/docs/ai/capabilities/overview/) to apply constraints to an Agent. Those constraints can be human defined guardrails. With the GitHub READMEs referenced above I had my Fable 5.1 create a classifier to score generated spans of text. I will post the methodology in the appendix.

It's published as a [PyPI package](https://pypi.org/project/vocabguard/) that you can run against any span of text with `uvx vocabguard "some text ..."`

You can `uv add vocabguard` to your project! Here's an example of using it on a Pydantic AI agent.

```
from pathlib import Path
from pydantic import BaseModel
from pydantic_ai import Agent
from vocabguard import OutputField, TextOutput, ToolArgument, VocabularyGuard
class CaseTicket(BaseModel):
    summary: str
    priority: int
def write_markdown(path: str, content: str) -> str:
    """Write a file under docs/."""
    target = Path(path)
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(content)
    return f'wrote {path}'
guard = VocabularyGuard(
    rewriter='openai:gpt-5.6-luna',
    targets=[
        OutputField(CaseTicket, lambda ticket: ticket.summary),  # a field of the structured output
        ToolArgument(write_markdown, 'content'),  # an argument of a tool call
        TextOutput(),  # the final text, when the agent answers in prose instead
    ],
    on_hit=lambda report: print(report.describe()),
)
# The agent files a ticket, or replies in text when there is nothing to file.
agent = Agent(
    'openai:gpt-5.6-luna',
    output_type=[CaseTicket, str],
    instructions='Triage bug reports. Write your working notes to docs/triage/<slug>.md, then file a ticket.',
    tools=[write_markdown],
    capabilities=[guard],
)
result = agent.run_sync(
    'Bug report: exporting a project with more than 200 assets hangs the desktop app at 97%. '
    'Reproducible on macOS and Windows since 3.4.1. Three customers affected, one enterprise.'
)
print(result.output)
```
Whenever [`vocabguard`](https://github.com/mpfaffenberger/vocabguard) sees a model output from this agent that matches one of the `targets` declared (you can specify `ToolArgument` or `OutputField` if you're using [Pydantic Structured Outputs](https://pydantic.dev/docs/ai/core-concepts/output/)), the `vocabguard` `Capability` will have its `rewriter` LLM attempt to rephrase the output. Alternatively you can specify no `rewriter` and it will raise a [`ModelRetry`](https://pydantic.dev/docs/ai/api/pydantic-ai/exceptions/) with phrasing and voice hints.

And since you can just run it as a command-line tool with `uvx vocabguard` you can wire up a [Claude Code hook](https://docs.claude.com/en/docs/claude-code/hooks) or mini [Pi](https://github.com/badlogic/pi-mono) extension easily. You can also use it as a standalone tool like `uv tool install vocabguard`

I don't yet know if this will work well. Linguistic drift is a very serious concern and this is an afternoon of goofing around with Fable 5.1. Someone should absolutely do PhD level research on this. Someone should absolutely build a semi-realtime linguistic drift tracker.

Oh... looks like [Nature is way ahead of me](https://www.nature.com/articles/s41562-026-02550-0): *The shrinking landscape of linguistic diversity in the age of large language models*.

Give it a try, see how you like it. Maybe it'll keep the terminology sane. [Pydantic AI Capabilities](https://pydantic.dev/docs/ai/capabilities/overview/) to the rescue. If only Spirit Airlines had used Pydantic AI Capabilities, they might have survived.

Thank you for reading!

## 

- [Eugene Geis](https://medium.com/@eugene.geis/ais-anthropomorphism-cascade-part-3-d325a89225bb) wrote an interesting blog post with some parallels.
- [Patrick Harrison](https://www.linkedin.com/in/patrick-harrison/) gave me a great suggestion to enrich my dataset with[GH Archive](https://www.gharchive.org/) .
- [Carson Sweet](https://www.linkedin.com/in/carsonsweet/) and[Owen Zanzal](https://www.linkedin.com/in/owenzanzal/) for scintillating discussions in the Charlottesville Slack's #datascience and #ai channels.
- Pydantic for hiring me recently. <3

## 

Here's the overall classifier methodology. Critically, the algorithm regularizes affinity to topics. We see a lot more "agents", "CLIs", etc in 2026. This is natural linguistic drift that is related to the subject matter of technological advancement. We do not penalize this. Instead of topical language, we amplify the feature importance related to "voice" by tuning the `gamma` parameter.

The following methodology is entirely written by Fable 5.1.

We contrast two corpora of GitHub README prose labelled only by era,  (4,319 documents, repositories with  stars last pushed before 2025) and  (1,047 documents fetched in 2026 from repositories with Claude Code commits), after stripping code, markup, and URLs, lowercasing, lemmatizing with [`simplemma`](https://github.com/adbar/simplemma), and counting unigrams and bigrams with stopwords retained.

For each -gram  with counts  and totals  we compute the log-odds ratio under an informative Dirichlet prior [[Monroe, Colaresi & Quinn, Political Analysis 16(4), 2008](https://doi.org/10.1093/pan/mpn018)],

with and , standardized as

Because log-odds cannot distinguish a change in register from a change in subject, and topical terms are bursty while stylistic ones are dispersed [[Church & Gale, Natural Language Engineering 1(2), 1995](https://doi.org/10.1017/S1351324900000139); cf. function-word stylometry in [Mosteller & Wallace, 1964](https://doi.org/10.1007/978-1-4612-5256-6)], candidates with  are re-weighted by document evenness  over the pooled corpora,

and the 1,000 largest form the watchlist .

A text with token sequence is scored

and the threshold  is the cut maximizing balanced accuracy on a held-out 20% split of each corpus, where the scorer attains AUC  [rank-based, [Hanley & McNeil, Radiology 143, 1982](https://doi.org/10.1148/radiology.143.1.7063747)] with true and false positive rates of  and .

The same corpora without evenness weighting give AUC but rank agent first, whereas ranks every, across, and never first and reduces agent from to .
