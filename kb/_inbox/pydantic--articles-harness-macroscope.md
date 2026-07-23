---
title: Reviewing agent-written code with Pydantic AI Harness and Macroscope
kind: blog
topic: null
subtopic: null
secondary_topics: []
summary: null
triage: null
skip_reason: null
source: pydantic
url: https://pydantic.dev/articles/harness-macroscope
author: Bill Easton
published: '2026-07-22'
fetched: '2026-07-23T06:55:44Z'
classifier: null
taxonomy_rev: 2
words: 1494
content_sha256: f4987e8dab5b3c8e313903948261af260993d4b9d4246ac02e0b8bb317020d23
---

# Reviewing agent-written code with Pydantic AI Harness and Macroscope

Monday's agent can write code. Give it a shell and a filesystem, one import each, and it does, fast, and overnight it opens four pull requests. They're waiting for you: hundreds of lines of agent-written Python, each diff plausible, each commit message tidy. You are now the slowest component in the system, reading at human speed what was written at agent speed, and the honest voice in your head asks the question the rest of this week has to answer: *who reviews the agent's code?*

Because someone has to, and it has to be more than a vibe check. Agent code needs review *more* than human code, not less. It's fluent, confident, and wrong in ways that read right: the API that almost exists, the test that asserts the mock, the edge case handled with a comment instead of code. The failure mode of agent-written code is precisely that it looks reviewed.


The most direct AI reviewer is a second Pydantic AI agent whose one job is to critique the diff. No new dependencies: give it the shell to read `git diff`, an `output_type` so the findings arrive as data, and the same model you used to write the code:

```
import logfire
from pydantic import BaseModel
from pydantic_ai import Agent
from pydantic_ai_harness import Shell
logfire.configure()
logfire.instrument_pydantic_ai()
class Finding(BaseModel):
    severity: str  # 'blocker' | 'note'
    file: str
    line: int
    issue: str
class Review(BaseModel):
    approved: bool
    findings: list[Finding]
reviewer = Agent(
    'anthropic:claude-opus-4-7',
    output_type=Review,
    instructions=(
        'You are a code reviewer. Read `git diff HEAD` and flag genuine defects '
        'only: missing null checks, wrong return types, tests that assert their '
        'mocks. Ignore style. If none, set approved=true.'
    ),
    capabilities=[Shell(allowed_commands=['git'])],
)
review = reviewer.run_sync('Review the current diff.').output
```
That's a real reviewer, and it will catch things: the obvious missing check, the wrong import, the copy-paste bug in an if-branch. It's also honest about its limits. An LLM reading a diff reads *text*, so the change that quietly breaks a caller two files over is invisible to it, and the taste it applies is a chatbot's taste, so a small wall of "consider extracting this helper" arrives alongside the two real bugs. That's a prototype reviewer. Shipping it into your write→review→merge loop is a different bar, which is where the fastest path lives.


[Macroscope](https://macroscope.com) is the reviewer already running in that loop for a lot of teams, built by a group whose founding observation is this post's cold open: as companies ship exponentially more code, humans review far less of it. Two things separate it from the ten-line critic above.

First, it reads structure, not text. An agentic pipeline parses the code into an abstract syntax tree so the model reasons over what changed rather than a diff hunk, and pulls context from git history and your issue tracker before it opens its mouth. The cross-file call site that would have been invisible to a text-only reviewer is right there in the graph.

Second, it's tuned for the two numbers that decide whether an AI reviewer earns a place in your loop: recall and precision. On their benchmark of a hundred real-world bugs, Macroscope caught 5% more bugs than the second-best tool while generating 75% fewer comments. Readers of [Agents Week](https://pydantic.dev/articles/agents-week) will recognize the philosophy: an AI that critiques your work earns trust by showing restraint, and 75% fewer comments is restraint you can measure.

And it meets the agent where the agent works. Leveraging the brand new [Macroscope CLI](https://macroscope.com/blog/introducing-macroscope-cli?utm_source=pydantic&utm_medium=partnership&utm_campaign=cli) (Launched today!), the harness's [ Macroscope capability](https://github.com/pydantic/pydantic-ai-harness/tree/main/pydantic_ai_harness/macroscope) provides one tool, 

`run_macroscope_review`, which shells out to the CLI, parses the streamed findings, and hands back a structured review with paths and line numbers.Here's that Agent, with the same three imports as the basic version, just one word different:

```
import logfire
from pydantic_ai import Agent
from pydantic_ai_harness import Shell
from pydantic_ai_harness.macroscope import Macroscope
logfire.configure()
logfire.instrument_pydantic_ai()
reviewer = Agent(
    'anthropic:claude-opus-4-7',
    capabilities=[
        Shell(allowed_commands=['git']),
        Macroscope(),
    ],
    instructions='Review the current diff with Macroscope and return the findings.',
)
review = reviewer.run_sync('Review the current diff.')
```
The capability surfaces findings only. The agent validates each one and fixes the real ones with the tools it already has — the division of labor you want in the loop: the reviewer reviews, the author fixes, and neither rubber-stamps the other.


Standalone review isn't the point; *converged* code arriving at the PR is. Same author, same reviewer, one instruction longer, plus the tools that let the agent actually resolve findings and open the PR when the review is clean:

- The agent finishes a change and reviews its own diff with Macroscope, in the loop, before any PR exists: validate each finding, fix the real ones, re-review until clean.
- Only then does it open the PR (`gh pr create`), where Macroscope's GitHub app reviews again with codebase-wide context and writes the summary a human can actually absorb.
- A human reads a *converged*PR: the diff, the findings, and how each was resolved, and makes the one decision that stays human. Merge.

As harness code, the whole loop is three capabilities and four sentences:

```
import logfire
from pydantic_ai import Agent
from pydantic_ai_harness import FileSystem, Shell
from pydantic_ai_harness.macroscope import Macroscope
logfire.configure()
logfire.instrument_pydantic_ai()
agent = Agent(
    'anthropic:claude-opus-4-7',
    capabilities=[
        FileSystem(),
        Shell(allowed_commands=['git', 'gh']),
        Macroscope(),
    ],
    instructions=(
        'Review your diff with Macroscope before opening a PR. Validate each '
        'finding, fix the real ones, and re-review until clean. After opening '
        'the PR, resolve anything the PR review raises. Never merge.'
    ),
)
agent.run_sync('Ship the feature branch through review.')
```
No new infrastructure, no workflow change: it's the review you already trust, moved earlier and able to keep up with the thing it reviews. The allowlist means its shell runs `git` and `gh` and nothing else, and the last instruction is the entire governance model in two words.


Macroscope's founders have a sharper way of putting the problem: pull requests are a gravity well for human attention. Every agent you add makes the well deeper, and the ending they predict is that review becomes always-on, automatic, and largely invisible, running continuously while the code is written instead of piling up where humans have to fish it out. The in-loop review above is that future in miniature: by the time a pull request is opened, the code is much more likely to be correct, because the arguing already happened.

Their prediction for people is the interesting part: humans stop being reviewers and become policymakers, the ones who define when approval is safe and which changes an automated pipeline may pass through. That's not a demotion. It's the same move this whole week has made at every gate: automate the volume, keep the judgment, and spend the judgment where it compounds.


Review was quietly doing two jobs. One is catching defects, and that job scales: machines can read every line, hold the whole dependency graph in view, and never get tired on the day's fifteenth PR. The other is *deciding what ships*, and that job doesn't scale and shouldn't: it's accountability, and accountability needs a name attached.

Unbundling them is the fix, and it's what human-in-the-loop should mean: not a human somewhere in the pipeline, but a human at the decision. Let the machine do the reading at machine speed, on every line of every PR. Keep the human on the decision, with better inputs than they've ever had: a reviewed diff instead of a raw one, findings raised, addressed, and resolved in the open.

And the split is about to matter more. In [When agents build agents](https://pydantic.dev/articles/when-agents-build-agents), agents author new tools and capabilities to disk, and the harness validates and arms them on the next run: the loop runs, learns, writes, re-arms. Code the agent wrote for itself is still code, fluent, confident, and about to join its author's own toolkit. Put Macroscope's review between *writes* and *re-arms* and the self-improvement loop gets the same property as the PR flow: every rung of the ladder carries a converged review, and a human can audit how the agent got smarter. Self-improving agents without review is how you end up with a system nobody understands.


The basic reviewer costs nothing more than the model you're already paying — `pydantic_ai_harness.Shell` and a second `Agent` with an `output_type` are all it takes to run today. For the production loop, install the Macroscope CLI and sign in once ([docs](https://docs.macroscope.com/cli)); `uv add pydantic-ai-harness` puts the `Macroscope` capability on the shelf, and it runs the same review their editor plugins do, inside your agent's loop. For the PR side, Macroscope installs as a [GitHub app](https://macroscope.com) and starts reviewing and summarizing your next pull request.

Back to the morning. The four PRs are still there, but each now arrives converged: findings raised by the reviewer, validated and fixed by the author, summarized for the human who decides. You read the arguments first, then the diffs they settled, and you merge the ones that earned it.

The agent writes. The reviewer reviews. You decide. Merge stays a human verb.
