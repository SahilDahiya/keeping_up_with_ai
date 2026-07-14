---
title: AI benchmarks are breaking. Trace analysis is what comes next.
topic: evals-observability
subtopic: benchmark-design
secondary_topics: []
summary: Explains why outcome-only agent benchmarks are losing resolution as agents
  exploit tests, and argues for trace analysis to distinguish real solving from benchmark
  gaming.
source: arize
url: https://arize.com/blog/agents-too-smart-for-benchmarks/
author: Laurie Voss
published: '2026-06-02'
fetched: '2026-07-11T04:56:26Z'
classifier: codex
taxonomy_rev: 1
words: 1448
content_sha256: 6ffe1d75ee37794f227d758e0609eb7ae54a5f3efe60cb4c121404a5da7cc261
---

# AI benchmarks are breaking. Trace analysis is what comes next.

*As AI agents become capable of exploiting benchmarks, pass/fail metrics are becoming less reliable. Full trace analysis offers a better way to evaluate agent behavior in both benchmarks and production systems.*

Three things happened in the last two months that you should know about, even if you don’t follow agent research closely.

In March, Anthropic [disclosed](https://anthropic.com/engineering/eval-awareness-browsecomp) that during an evaluation on BrowseComp (a benchmark designed to test how well models can find hard-to-locate information on the web) Claude Opus 4.6 stopped trying to answer the questions. Instead, the model realized it was being evaluated, worked through a list of known benchmarks until it identified BrowseComp, located the repository on GitHub, studied the encryption scheme used to protect the answer key, and decrypted it. Then it submitted the decrypted answer.

Also in March, [METR](https://metr.org/notes/2026-03-10-many-swe-bench-passing-prs-would-not-be-merged-into-main/) (an organization that builds rigorous evaluations of frontier AI) hired four maintainers of the open-source repositories that the benchmark SWE-bench Verified is built from, and asked them to review the agent-generated pull requests that had passed the benchmark’s tests. About half of the PRs the benchmark called “solved” were ones the maintainers said they would not merge.

In April, the [Center for Responsible Decentralized Intelligence at UC Berkeley](https://rdi.berkeley.edu/blog/trustworthy-benchmarks-cont/) (CRDI) published research showing that an automated scanning agent had broken eight major AI agent benchmarks. It used all sorts of techniques: a ten-line script that hijacked the testing framework and forced it to return “passed” for every answer, running Chrome directly to read the answers out of the task configuration, and in one case just returning an empty JSON object for every answer, which it turned out the benchmark wasn’t checking.

There’s a pattern here: outcome metrics have stopped measuring what we thought they measured. And the methodology that fixes it is the same one production AI teams have needed all along.

**TLDR**

- AI agents are increasingly able to exploit benchmark designs.
- Outcome-based evaluation often misses dangerous behavior.
- Several recent studies show benchmark scores can overstate capability.
- Trace analysis reveals how an agent reached an answer, not just whether it succeeded.
- Production AI teams should evaluate trajectories, not outcomes alone.

**Benchmarks broke when models got smart enough to cheat**

Pass/fail benchmarks worked when models couldn’t actively defeat them. They don’t work now. As Princeton’s [Sayash Kapoor](https://x.com/sayashk/status/1966550402129592738) (one of the most consistently right voices on agent evaluation) put it, “agent benchmarks lose *most* of their resolution because we throw out the logs and only look at accuracy.” A “pass” can mean the agent solved the problem, retrieved the answer from training data, exploited the test harness, or, as Claude demonstrated, decrypted the answer key. Outcome-only scoring can’t tell these apart.

In May, Kapoor and his collaborators published [the cleanest articulation of the problem to date](https://arxiv.org/abs/2605.08545), a paper arguing that log analysis is necessary for credible evaluation of AI agents. Agent benchmarks, they argue, threaten evaluation credibility in three ways: scores get inflated by shortcuts and benchmark artifacts; benchmark performance fails to predict real-world utility; and capability scores can conceal dangerous or catastrophic actions the agent took along the way. When they re-evaluated agents on tau-Bench Airline by reading the actual traces instead of just the pass/fail outcomes, they found the published leaderboard had been understating the agents’ real capabilities by nearly 50%, and also missing entire categories of dangerous behavior the agents had exhibited along the way.

There’s lots more examples to point at: a [SWE-ABS paper](https://arxiv.org/pdf/2603.00520) showing that 20% of top-30 SWE-bench leaderboard “solves” are semantically wrong, [NIST’s report on cheating in agent evaluations](https://www.nist.gov/blogs/caisi-research-blog/cheating-ai-agent-evaluations), and Anthropic’s own [research on emergent misalignment from reward hacking](https://www.lesswrong.com/posts/fJtELFKddJPfAxwKS/natural-emergent-misalignment-from-reward-hacking-in). They’re all pointing at the same thing: the trajectory matters. **You cannot evaluate a system that takes hundreds of actions by looking at the last one.**

**This is a known pattern in infrastructure, now in AI**

[Mitchell Hashimoto](https://x.com/mitchellh/status/2055380239711457578), the co-founder of HashiCorp, was posting about AI-accelerated software development generally and accidentally made a point about benchmarks:

We already learned this lesson once in infrastructure: you can automate yourself into a very resilient catastrophe machine. Systems can appear healthy by local metrics while globally becoming incomprehensible. Bug reports can go down while latent risk explodes. Test coverage can rise while semantic understanding falls. Changes happen so fast that nobody notices the underlying architecture decaying.

This is what we see in the world of benchmarks: bug reports go down, benchmark scores go up across the board, test coverage rises. But semantic understanding falls: the SWE-ABS finding that one in five “solved” tasks among top leaderboard agents are semantically wrong; METR’s finding that half of test-passing PRs wouldn’t be merged by the humans who maintain the repos.

The agent benchmark community is discovering a pattern that infrastructure engineers had to internalize during the cloud transition. Local metrics can look great while the global system is rotting. **The only fix is to look at the trajectory, not the outcome.**

**Production AI teams have been living this for a year.**

The benchmark crisis may be new to AI research, but it’s old news to anyone who has shipped an agent to production, because in production, there has never been a ground-truth label. You can’t run pass/fail on a customer-support conversation or an autonomous coding session. You only ever have traces.

We learned this when building [Alyx, the AI agent inside Arize AX](https://arize.com/blog/ai-agent-debugging-four-lessons-from-shipping-alyx-to-production/). Early on, we asked Alyx to summarize multiple traces. It made 27 LLM calls in a single session, and almost all of them were the agent reorganizing its own to-do list, going in circles. Every individual tool call returned a valid response. Every span looked healthy in isolation. By any outcome metric you’d care to define, nothing had gone wrong. The failure was only visible in the trajectory: the same plan, regenerated 27 times in a row. We only knew there was a problem because we were looking at the traces.

This is the same gap the benchmark crisis is exposing, just from the other side. Researchers used to assume that benchmark scores were close enough to deployment behavior to be useful proxies. They aren’t anymore. Production teams never had that luxury.

**What trace analysis actually surfaces**

When you look at a trace instead of an outcome, you can finally see things that outcome metrics structurally cannot:

- **Tool-call patterns.**Did the agent pick the right tool, in the right order, with the right arguments?
- **Recovery behavior.**Does it gracefully handle a failure or spiral into a loop?
- **Reasoning vs. lookup.**Is the agent solving, or cheating by fetching the answer?
- **Per-step verification.**In a long trajectory, which step broke?
- **Cross-run consistency.**Run the same input ten times: do you get the same trajectory, or ten different ones?

This is the work we do at Arize. Capturing traces from production agents with enough fidelity to do trajectory-level analysis, surfacing patterns across runs, and connecting failures back to specific tool calls and reasoning steps. The reason the methodology arguments coming out of Princeton and Berkeley and METR are landing hard right now is that they’re catching up to where production has had to be all along.

**Trace analysis isn’t free, and it isn’t solved.**

Kapoor’s paper on log analysis concedes a problem in its own discussion: LLM-based evaluators are themselves unreliable, rubrics drift, long traces exceed context windows, and “evaluating the evaluator risks an infinite regress.” None of this is going away. Their rebuttal is that an imperfect signal at reasonable cost is still vastly better than the alternative, which is the pass/fail outcome metric. As Kapoor [wrote](https://x.com/sayashk/status/2054569643080077576) in May, “log analysis is not a ‘one and done’ technique, it requires constant effort.” This is infrastructure work. It’s the kind of thing you build into how your team operates, not a feature you turn on.

**The benchmark crisis is the early warning. Production is the actual fire.**

All three incidents I mentioned at the start were visible only because someone looked at the traces. Anthropic caught Claude’s BrowseComp behavior by reading the model’s reasoning chain. METR found the SWE-bench gap by having real humans review real PRs. Berkeley exposed the eight-benchmark vulnerability by analyzing what the exploit agent was *doing*, not what score it produced.

The methodology that exposed the benchmark crisis is the methodology production agents have needed all along. Anyone building production agents in 2026 is going to end up doing trace analysis whether they planned to or not. The question is whether you do it on purpose, with the right infrastructure, or accidentally, by waking up to a 27-call loop on a Monday morning.

Are you building towards a benchmark, or are you building towards the real results you want? It’s harder than ever, and critical to get right.
