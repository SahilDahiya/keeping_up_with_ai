---
title: 'PostgresFS vs. SQL skills: should AI agents fake a filesystem?'
topic: agents
subtopic: tool-use
secondary_topics: []
summary: Compares filesystem-like and SQL-backed skill interfaces for AI agents, focusing
  on state access and tool ergonomics.
source: arize
url: https://arize.com/blog/postgresfs-vs-sql-skills-ai-agent-filesystem/
author: Aparna Dhinakaran; Sufjan Fana
published: '2026-06-11'
fetched: '2026-07-11T04:56:36Z'
classifier: codex
taxonomy_rev: 1
words: 2238
content_sha256: 5ef8f62ddc2a9f72d6030baa08f733356043890ca0baa5191b2711294358317e
---

# PostgresFS vs. SQL skills: should AI agents fake a filesystem?

*Co-Authored by Aparna Dhinakaran, Co-founder & Chief Product Officer & Sufjan Fana.*

**TLDR****: **Can an AI agent use a database as if it were a filesystem? We tested that question by comparing PostgresFS, a Postgres-backed filesystem abstraction, against a SQL skill that lets the agent query Postgres once, write results locally, and continue analysis with real Bash tools.

The result: PostgresFS was competitive on simple reads, but the SQL skill won overall accuracy and avoided the maintenance cost of recreating filesystem semantics. The deciding factor was locality. Once data was materialized locally, the agent could reuse it with normal shell tools instead of round-tripping to the database on every read.

**The question behind the experiment**

Working with [agent harnesses](https://arize.com/blog/what-is-an-agent-harness/), it is hard not to be impressed by the power that [Bash and filesystems](https://arize.com/blog/hierarchical-memory-management-in-agent-harnesses/) lend to modern agents. Bash and file operations sit at the core of many tool-calling workflows. The strength of that foundation has even led some people to say, [“Bash might be all you need.”](https://vercel.com/changelog/introducing-bash-tool-for-filesystem-based-context-retrieval)

But that raises a deeper question: **when should an agent use a real filesystem, and when are we only giving it the illusion of one?**

Mintlify [recently introduced](https://www.mintlify.com/blog/how-we-built-a-virtual-filesystem-for-our-assistant) ChromaFS, a virtual filesystem over Chroma that lets a docs assistant explore documentation with commands like `ls`, `cat`, and `grep`. Their write-up was thoughtful and sparked a serious debate on our team: **should every database expose a filesystem-style interface for agents, or should agents use the database’s native query language and materialize results locally?**

**The virtual filesystem pattern for AI agents**

**Mintlify built ChromaFs to make their docs assistant smarter.** Plain vector RAG could only return chunks that matched a query embedding; if the answer spanned several pages, or needed exact syntax that never landed in the top-K, the agent was stuck. So they wrapped their Chroma vector store in a filesystem-shaped interface: the agent runs `ls`, `cat`, `grep`, and underneath every command is a database read. They published it as a pattern other teams could copy. The same “wrap the database as a filesystem” move is now showing up on SQL databases that never needed it.

Your agent has the same shape of problem: it needs to work with data in a database. The premise behind the pattern is that agents are fluent at what their training data has seen, so you should hand them a *familiar* surface. Whether a familiar surface is enough, or whether what matters is where the data actually lives, is what we set out to test.

**Our hypothesis: SQL skills plus local Bash should beat fake filesystems**

Selectively letting an agent pull only the data it needs from a database (via a skill), then giving it the full local Bash toolset, should beat the complexity of building a Bash-like interface into the database itself.

The reason is practical: many shell and pipe workflows only exist in full form locally. The local toolbox is broader than what you can realistically re-create behind a database abstraction. Databases still excel at one thing here: searching and filtering across TB-scale data. But for iterative, branch-heavy analysis loops, local tooling is usually the better execution surface.

So the pattern is a deliberate handoff. The agent uses the database for broad retrieval, materializes a slice locally, runs deeper analysis, and pulls another slice if needed. That gives you a clean tradeoff between large-scale search and complex local reasoning.

Our bet was that a [skill file](https://arize.com/docs/ax/arize-ai-for-agents), not a filesystem abstraction, would win on the two properties that matter most for this work: **composability** and **speed**. The skill runs a focused SQL query, writes results to a local file, and the agent composes the final answer with the host’s real Bash environment.

As a stand-in for ChromaFS, we used PostgresFS. It works over Postgres in the same style: data stays behind the abstraction, and commands like `cat`, `grep`, or `find` are translated into database queries.

**Speed** comes from locality: once the data is local, bash runs over it without another database round-trip, while PostgresFS pays one on every read. **Composability** is that same locality seen again: anything that needs a *second* pass over the data (staging an intermediate result, using two-input operators like `comm` or `join`) needs a writable, re-readable local home that a read-only abstraction can’t give it. Both reduce to one question: does the agent own a local copy of the data, or reach back through the abstraction on every read?

So our prediction: a database with the right skill should match or beat the filesystem abstraction, and even a tie would be a win for the skill: the abstraction is a large custom layer to build and keep correct, while the skill is a prompt and a small script that reaches the same place.

**PostgresFS vs. SQL skill: two ways to give agents database access**

We built both and decided to test them against the [live Arize AX docs](https://arize.com/docs/ax) that we ported into Postgres. Here’s what each one actually is:

**PostgresFS, the filesystem abstraction.** The five ChromaFs verbs (`ls`, `cat`, `grep`, `find`, `cd`) over virtual paths that resolve to Postgres reads, plus the standard coreutils filters (`sort`, `uniq`, `wc`, `awk`, `sed`, `cut`, `tr`, `head`, `tail`, `comm`). The agent explores the docs like a codebase. We wired it the way Mintlify’s ChromaFS is built: an in-process shell (`just-bash`) registered as the agent’s Bash tool. So we’re testing the real pattern, not a strawman. It’s read-only: the five verbs become `SELECTs`, the filters run locally over whatever bytes came back.

**The skill, the SQL workflow.** No abstraction. The agent gets the host’s real bash shell plus a small script that takes one SQL query and writes the result to a local file. The workflow it learns: write a query, run it, compose the answer against the file with real `grep` / `jq` / `sort` / pipes. The agent does the translation; the runtime just moves bytes.

Those are the same job done two ways: PostgresFS sends every read back to Postgres, while the skill makes one trip to the database and does everything else locally.

Each agent also gets an orientation prompt. PostgresFS’s prompt hands it a decision table mapping question shapes to shell idioms and tells it to keep the number of doc reads down. The skill’s prompt teaches a discipline: compute the answer in SQL and return it inline when it reduces to a small set (`COUNT`, `GROUP BY`, `INTERSECT`), otherwise project every candidate row to a file and compose locally — and *don’t* treat the query script as a search tool, because a flurry of narrowing queries means you projected too little.

**How we tested PostgresFS against a SQL skill**

Both arms run inside the Claude Agent SDK: the [production agent loop](https://arize.com/blog/open-source-coding-agent-tracing/), identical on each side except for the architecture under test. The agent is claude-sonnet-4-6, the judge is claude-opus-4-7, and the database is a frozen snapshot of the Arize docs. We ran each approach 10 times on each of 10 questions and reported the median. To compare only the part that’s actually architectural, we time the agent’s **investigation loop**: from the prompt to its last tool call. Grading is a mix: programmatic where the answer is exact (slug sets, counts), an [LLM judge](https://arize.com/docs/ax/evaluate/evaluation-concepts/agent-evaluation) against a fixed rubric for the synthesis questions.

The ten questions span three tiers, each leaning on a different part of the read path: **simple** (one or a few reads), **mid** (aggregation over many pages), and **complex** (extraction or synthesis whose answer depends on how many separate reads the agent must gather, what we’ll call *locality pressure*):

Here’s the full set of questions:

**The results: PostgresFS was close on latency, but the skill won accuracy**

On paper, close enough to call even: neither clears 2× on latency, and accuracy splits 93 to 99. That thin margin is the hypothesis showing through — one quiet property, reading from a local file versus round-tripping every read, never blows out a benchmark; it bills you narrowly in accuracy and heavily in code instead.

**Latency only counts if you measure the right slice.** Most of a run is a one-time skill load and answer synthesis; the architecture acts only in the investigation loop between them, first prompt to last tool call. That’s the only slice we clock. Here it is inside q7:

Comparing that middle slice across the ten questions, it’s nearly an even split: PostgresFS takes three (q2, q5, q6) on in-process dispatch, the skill takes three (q8, q9, q10) where reads pile up, and four are ties. The real driver is read count; tier is just a proxy for it. The per-question medians:

Rolled up by tier (median over all reps in each tier):

**Where PostgresFS wins** is real but small, and all one shape: questions answered by *enumerating paths* and finishing with cheap filters like `find … | wc -l`, a slug lookup. Both approaches get these right. The skill trades N database round-trips for one round-trip plus a subprocess per filter, so it only pays off once reads pile up. But a faster slug lookup is still just a slug lookup: these wins don’t ladder up to a quality story, but the losses do.

**Accuracy: the SQL skill scored 99/100 vs. PostgresFS at 93/100**

Overall: **PostgresFS 93/100, the skill 99/100.** Both ends are tied at 100%. The whole gap is two mid-tier questions, both on PostgresFS: **q7 (synthesis) at 6/10** and **q4 (counting) at 7/10. **Every other question is 9/10 or 10/10 on both. *Why those two specifically* is the whole story.

**Why PostgresFS lost: locality collapse and limited composability**

The losses aren’t about missing operators: we handed PostgresFS every filter, and they work. The split is *inside* PostgresFS, on the read path:

**The filters are local.** `sort`, `uniq`, `awk` and friends are pure stream transforms over bytes already in the pipe: in-process, no database, no round-trip.

**The reads are faked.** `ls`, `cat`, `grep`, `find` resolve through an adapter that turns each into a Postgres `SELECT`. Two costs fall out of that.

**Locality collapse.** Every doc read is a database round-trip dressed as a shell verb. Each one pays for query parsing, serialization, and transfer, even when Postgres serves it warm from cache. A `grep -rl` followed by a burst of cats, near-instant on a real filesystem, becomes a sequence of round-trips. The skill pays that round-trip *once*: a single query lands the result on a local file, and everything after is local and composable, with no more database hops.

**Composability, capped at one pass.** Single-pass pipelines work on both. But anything needing a *second* pass over the data doesn’t: `just-bash` has no process substitution `<(…)` and the adapter is read-only (no `/tmp`, every write is `EROFS`), so nothing can be staged and reused. The two-input family (`comm`, `join`, `diff`, `paste`) is dead even though `comm` sits in the allowlist. This is really the same wall as locality: the skill materializes once and reuses freely, while PostgresFS pays a fresh round-trip for every look at the data.

The natural objection is *“then just add to the abstraction until it’s as good”. *This is a trap. Every step toward a faithful read path (a better prefetch, closer `grep` semantics, a real cache) is a step toward real files on a real filesystem, which *is* the skill, reached less cleanly than just running SQL over the host’s own shell. And the code you’d write to get there is the same code that round-trips every read in the first place: **the maintenance cost and the performance cost are the same cost.**

**What this means for agent harness design**

Our hypothesis mostly held, with one wrinkle worth keeping. We bet on composability *and* speed; they turned out to be one property: whether the agent works from a local copy of the data it owns or reaches back through the abstraction on every read. That same property is what you’d have to build and maintain. So the takeaways order themselves around cost, not cleverness:

**With performance a tie, the cost that’s left is maintenance.** What settles it is what you own: PostgresFS is a large custom layer: an adapter, a coarse-filter, a cache, a regex translator. You have to keep that layer correct as the schema moves, while the skill is a prompt and a small script. We didn’t benchmark maintenance, so treat it as a structural argument, not a measurement. And the performance gap that *does* exist only shows up if you **stratify by question shape**. Look at per-question pass rates, or you’ll ship the failure without seeing it.

**Reach for the real store before the pretty shape.** “What does the host shell actually read from?” beats “what shape would I like to expose?” A familiar interface is necessary, not sufficient.

**This generalizes past SQL.** “Wrap the store as a filesystem” vs. “give the model the store’s real query language plus a real shell” is the same decision for Chroma, Mongo, BigQuery, ClickHouse, or whatever’s next. The query language is incidental. What’s constant is the trap: every time you fake a filesystem, you sign up to maintain one, and the closer you push it to behave like the real thing, the more you’ve just rebuilt the real thing, slower.

**From architectural guesses to agent evals**

The larger story here is that [evals using Arize AX](https://arize.com/docs/ax/get-started/get-started-evaluations) can take you from guessing about your architectural choice to knowing for sure. If that sounds like a good idea to you, [try us out today](https://arize.com/).
