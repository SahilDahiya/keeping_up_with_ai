---
title: Ruff v0.16.0
kind: blog
topic: null
subtopic: null
secondary_topics: []
summary: null
triage: null
skip_reason: null
source: simon-willison
url: https://simonwillison.net/2026/Jul/25/ruff/
author: Simon Willison
published: '2026-07-25'
fetched: '2026-07-26T06:59:55Z'
classifier: null
taxonomy_rev: 2
words: 469
content_sha256: 75ecf3a114fb73889ac32374c1f02e9ed06da9f0552c3e746d15e3fd21bfb15a
---

# Ruff v0.16.0

25th July 2026 - Link Blog

** Ruff v0.16.0**. Astral shipped a significant new version of their Ruff Python linting tool a few days ago on July 23rd. I noticed today because my various CI jobs all started failing thanks to new default Ruff checks and my unpinned 

`"ruff"` dev dependency.From Brent Westbrook's announcement post:

Ruff now enables 413 rules by default, up from 59 in previous versions.

Since Ruff's default rule set was last modified in

[v0.1.0](https://github.com/astral-sh/ruff/blob/main/changelogs/0.1.x.md#breaking-changes), the number of rules in Ruff has grown from 708 to 968. Many of these rules catch severe issues, including[syntax errors](https://docs.astral.sh/ruff/rules/load-before-global-declaration)and[immediate runtime errors](https://docs.astral.sh/ruff/rules/yield-in-init/)but were not previously enabled by default. With the new rule set, Ruff will bring these issues and many others to your attention without any Ruff configuration.

Here's a one-liner for trying it on any Python project:

```
uvx ruff@latest check .
```
I ran the latest Ruff against my three biggest projects - [Datasette](https://datasette.io/), [sqlite-utils](https://sqlite-utils.datasette.io/), and [LLM](https://llm.datasette.io/) - and it found *hundreds* of minor issues that breached the new default rules.

All three projects have very comprehensive test suites, executed in CI against Python 3.10 through Python 3.14, so upgrades like this are pretty safe. The following command did the bulk of the upgrades:

```
uvx ruff@latest check . --fix --unsafe-fixes
```
Against `sqlite-utils`, that command reported:

```
Found 1618 errors (1538 fixed, 80 remaining).
```
As an illustrative example, here are three of the remaining issues. Ruff does a nice job of explaining each one:

```
DTZ005 `datetime.datetime.now()` called without a `tz` argument
  --> tests/test_duplicate.py:17:10
   |
15 |     "datetime_col" TEXT)""")
16 |     # Insert one row of mock data:
17 |     dt = datetime.datetime.now()
   |          ^^^^^^^^^^^^^^^^^^^^^^^
18 |     data = {
19 |         "text_col": "Cleo",
   |
help: Pass a `datetime.timezone` object to the `tz` parameter
BLE001 Do not catch blind exception: `Exception`
  --> tests/test_plugins.py:16:12
   |
14 |         db.execute("select * from pragma_function_list()")
15 |         return True
16 |     except Exception:
   |            ^^^^^^^^^
17 |         return False
18 |     finally:
   |
B018 Found useless attribute access. Either assign it to a variable or remove it.
  --> tests/test_update.py:46:5
   |
44 | def test_update_invalid_pk(fresh_db, pk, update_pk):
45 |     table = fresh_db["table"]
46 |     table.insert({"id1": 5, "id2": 3, "v": 1}, pk=pk).last_pk
   |     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
47 |     with pytest.raises(NotFoundError):
48 |         table.update(update_pk, {"v": 2})
   |
```
Unsurprisingly, given Astral's [new home at OpenAI](https://simonwillison.net/2026/Mar/19/openai-acquiring-astral/), this output provides everything a coding agent would need to fix the problems.

I had Codex (GPT-5.6 Sol high) [upgrade LLM](https://github.com/simonw/llm/pull/1557) and [sqlite-utils](https://github.com/simonw/sqlite-utils/pull/814), and Claude Code (with Opus 5) [upgrade Datasette](https://github.com/simonw/datasette/pull/2857).

## Recent articles

- [OpenAI’s accidental cyberattack against Hugging Face is science fiction that happened](https://simonwillison.net/2026/Jul/22/openai-cyberattack/)- 22nd July 2026
- [A Fireside Chat with Cat and Thariq from the Claude Code team](https://simonwillison.net/2026/Jul/21/cat-and-thariq/)- 21st July 2026
- [Kimi K3, and what we can still learn from the pelican benchmark](https://simonwillison.net/2026/Jul/16/kimi-k3/)- 16th July 2026
