---
title: 'Release: sqlite-utils 4.1'
topic: null
subtopic: null
secondary_topics: []
summary: null
triage: null
skip_reason: null
source: simon-willison
url: https://simonwillison.net/2026/Jul/11/sqlite-utils/
author: Simon Willison
published: '2026-07-11'
fetched: '2026-07-13T20:52:42Z'
classifier: null
taxonomy_rev: 1
words: 504
content_sha256: 0f0f4fc055971cefacf8970c6e3f93b9d1afa3697de5624ba4f586fcc3d6de96
---

# Release: sqlite-utils 4.1

11th July 2026

The first dot-release since [4.0 a few days ago](https://simonwillison.net/2026/Jul/7/sqlite-utils-4/), introducing a number of minor new features.


`sqlite-utils insert`and`sqlite-utils upsert`now accept a`--code`option for[providing a block of Python code](https://sqlite-utils.datasette.io/en/stable/cli.html#cli-insert-code)(or a path to a`.py`file) that defines a`rows()`function or`rows`iterable of rows to insert, as an alternative to importing from a file. ([#684](https://github.com/simonw/sqlite-utils/issues/684))

`sqlite-utils` already had features that allow you to pass blocks of Python code as CLI arguments, for example [this one](https://sqlite-utils.datasette.io/en/stable/cli.html#converting-data-in-columns) for the `sqlite-utils convert` command:

sqlite-utils convert content.db articles headline ' def convert(value): return value.upper()'

Allowing blocks of code to [generate new rows directly](https://sqlite-utils.datasette.io/en/stable/cli.html#inserting-rows-generated-by-python-code) was on obvious extension of that pattern:

sqlite-utils insert data.db creatures --code ' def rows(): yield {"id": 1, "name": "Cleo"} yield {"id": 2, "name": "Suna"} ' --pk id


`sqlite-utils insert`and`sqlite-utils upsert`now accept`--type column-name type`to[override the type automatically chosen when the table is created](https://sqlite-utils.datasette.io/en/stable/cli.html#cli-insert-csv-tsv-column-types). This is useful for CSV or TSV columns such as ZIP codes that look like integers but should be stored as`TEXT`to preserve leading zeros. ([#131](https://github.com/simonw/sqlite-utils/issues/131))

A long-standing feature request which turned out to be a [simple implementation](https://github.com/SAY-5/sqlite-utils/commit/d2ac3765ed9f0516bb0cbc2508a5c3907fb6a71a).


- New
`table.drop_index(name)`method and`sqlite-utils drop-index`command for dropping an index by name. Both accept`ignore=True`/`--ignore`to ignore a missing index. ([#626](https://github.com/simonw/sqlite-utils/issues/626))
`sqlite-utils query`can now read the SQL query from standard input by passing`-`in place of the query, for example`echo "select * from dogs" | sqlite-utils query dogs.db -`. ([#765](https://github.com/simonw/sqlite-utils/issues/765))

Two more small features. I had Codex review all open issues and highlight the easiest ones!


`sqlite-utils upsert`can now infer the primary key of an existing table, so`--pk`can be omitted when upserting into a table that already has a primary key.

Another Codex suggestion, an obvious missing CLI feature from a Python library improvement that shipped in the 4.0 release.


`table.transform()`and`table.transform_sql()`now accept`strict=True`or`strict=False`to change a table’s[SQLite strict mode](https://www.sqlite.org/stricttables.html). Omitting the option preserves the existing mode. ([#787](https://github.com/simonw/sqlite-utils/issues/787))- The
`sqlite-utils transform`command now accepts`--strict`and`--no-strict`to change a table’s strict mode. ([#787](https://github.com/simonw/sqlite-utils/issues/787))

These two were inspired by [Prefer STRICT tables in SQLite](https://evanhahn.com/prefer-strict-tables-in-sqlite/) by Evan Hahn, which did the rounds [on Hacker News](https://news.ycombinator.com/item?id=48873940) today. Evan pointed out that:

Unfortunately, I don’t think there’s a way to ALTER a table to make it strict. I think you have to copy the data out of the non-strict table into the strict one.


That's exactly what the [sqlite-utils transform mechanism](https://sqlite-utils.datasette.io/en/stable/python-api.html#transforming-a-table) does, so I extended it to add the ability to switch tables from strict to non-strict and vice-versa.

Here's [the GPT-5.6 Sol xhigh Codex transcript](https://gist.github.com/simonw/ab8256b81646ad967a601975e206de64) I used to implement those new strict table features. One of the most useful prompts I ran was this one:


`use uv run python -c and manually exercise the new .transform(strict=) option, see if you can find any edge-cases or bugs`

Effectively telling the model to manually test its work, outside of the automated tests it had already written. This turned up two minor issues that we then fixed.

## Recent articles

- [The new GPT-5.6 family: Luna, Terra, Sol](https://simonwillison.net/2026/Jul/9/gpt-5-6/)- 9th July 2026
- [sqlite-utils 4.0, now with database schema migrations](https://simonwillison.net/2026/Jul/7/sqlite-utils-4/)- 7th July 2026
- [sqlite-utils 4.0rc2, mostly written by Claude Fable (for about $149.25)](https://simonwillison.net/2026/Jul/5/sqlite-utils-fable/)- 5th July 2026
