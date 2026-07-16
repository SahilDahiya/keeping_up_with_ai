---
title: 'AI spend is the new headcount: why cost control is an observability problem'
kind: blog
topic: infra-platform
subtopic: cost
secondary_topics:
- evals-observability/monitoring
summary: 'Frames LLM/agent spend as headcount-shaped (usage-scaled, salary-magnitude)
  rather than SaaS-shaped, arguing cost governance is really an observability problem:
  attribute spend per agent, per user, per session from traces (via the genai-prices
  dataset) and ask ''was this run worth what it cost?''.'
triage: null
skip_reason: null
source: pydantic
url: https://pydantic.dev/articles/ai-spend-is-the-new-headcount
author: Alex Che
published: '2026-06-09'
fetched: '2026-07-16T22:03:19Z'
classifier: claude
taxonomy_rev: 2
words: 954
content_sha256: 913e3e4cb8fcc0a6613c2e77f5bcd4eed15aba913c34f4a62d89f90c3025645c
---

# AI spend is the new headcount: why cost control is an observability problem

Somewhere mid-quarter, a finance person opens a spend report and notices something. The line labelled "AI tools" has been climbing, quietly, month over month, for long enough that the rate is no longer the interesting bit; what is interesting is the absolute number. They cross-check it against the salary band for a senior engineer, and the AI line, it turns out, is bigger. They ask the obvious question, which team owns this, and the answer comes back fuzzy. Quite a few teams use it, in their own ways. Nobody, in any precise sense, owns it.

The claim we want to put down is that **AI spend has the wrong shape to be governed like SaaS, and the right shape to be governed like headcount.** It scales with usage, so it does not behave like a flat subscription. It lands in salary-order magnitudes, which means the numbers it produces would, in any other context, prompt a hiring discussion. And it accumulates between the review cycles you have set up to catch this kind of growth, so by the time anyone looks, the line is already there.


The trouble, and we have heard this from quite a few platform leads now, is that the governance machinery around AI spend is still the SaaS machinery. A card on file. A renewal that someone approved once, eighteen months ago, on a Tuesday. An annual review that aggregates the line into "tooling" and moves on. That machinery works well enough when the underlying service costs roughly the same every month, and it breaks quietly when the underlying service costs an unpredictable amount every day.

There is a related, slightly subtler problem: nobody owns the line on the P&L. Headcount, by contrast, has owners. Somebody hired the person, somebody signs off on the renewal of their contract, and somebody is responsible if the team turns out to be the wrong shape for the work. AI spend has no equivalent owner, because everybody is using it a little. So the question that should be asked, who decides how much of this we should be doing, has no obvious home, and it gets asked, oftentimes, by finance after the fact.


If AI spend is shaped like headcount, the only honest way to govern it is to know what each run was actually for. Which is **an observability question dressed up as a finance one**. The shape of the answer, which agent ran, which user it served, which tool it called, what came out the other side, is the shape of a trace, not the shape of a finance report. The CFO needs the data eventually; the work of producing it lands on engineering, who oftentimes are the only people in the building who can.

There is a timing piece worth naming, because it changes the urgency. We have been watching the subsidy era visibly come to an end. Inference prices that used to drift downwards every quarter have stopped drifting. The major model vendors have begun moving towards public markets, which means the patience of their balance sheets is no longer infinite. The meter, in other words, is being switched on across the industry at roughly the same time. The slack that hid this problem, the slack that let teams be a bit careless because the unit cost was small, is leaving the system.


What changes when you can see the spend per agent, per user, per session, is that the conversation moves up a level. The default question, when finance first notices the number, is "should we cap this?". That question has a clean answer, yes or no, and it does not need much detail. The more useful question, which only opens up once you have visibility, is "is this run worth what it cost?". That question is harder, but answering it across enough runs is what tells you whether the agent you have built is doing the work you think it is doing.

We have two surfaces that pull on this, and it is worth being plain about what each one does:

- [Pydantic AI Gateway](https://pydantic.dev/ai-gateway?utm_source=pydantic.dev&utm_medium=internal&utm_campaign=ai-spend-is-the-new-headcount&utm_content=inline)
- [Pydantic Logfire](https://pydantic.dev/logfire?utm_source=pydantic.dev&utm_medium=internal&utm_campaign=ai-spend-is-the-new-headcount&utm_content=inline)

The coding agents driving a good slice of this spend work well with both surfaces too. [Claude Code](https://github.com/pydantic/claude-code-logfire-plugin) and [Codex](https://pydantic.dev/articles/codex-logfire-plugins?utm_source=pydantic.dev&utm_medium=internal&utm_campaign=ai-spend-is-the-new-headcount&utm_content=inline) can both run through the gateway and emit into Logfire.

This is the loop we keep coming back to in customer conversations. You see the spend in Logfire, you shape it at the gateway, you watch the next run, you shape again. The thing that makes this work as one practice rather than two products is that both surfaces are connected. The CFO question (was this run worth it) and the engineering question (did the agent do what we asked) stop being two separate investigations and start being two views of the same trace, which is, ultimately, the only way a fast-moving practice has any chance of staying coherent.


We end where we started: a finance person staring at a line in a spend report. The spend is the loud part, the part that prompts the meeting and gets escalated, and most orgs are at least watching it now. The quieter problem, and the more expensive one over time, is not knowing what the agents did, on whose behalf, with which data, to what result. The spend is just the symptom. **Real cost control starts there: make the runs underneath the line visible, then shape them, because that is the part you can actually act on.**

If your AI line just crossed a senior engineer's salary and the ownership conversation is fuzzy, that is the conversation we constantly have. Talk to us about Logfire and the AI Gateway ([https://pydantic.dev/contact?utm_source=pydantic.dev&utm_medium=internal&utm_campaign=ai-spend-is-the-new-headcount&utm_content=cta-contact](https://pydantic.dev/contact?utm_source=pydantic.dev&utm_medium=internal&utm_campaign=ai-spend-is-the-new-headcount&utm_content=cta-contact)). We will help you stand up the visibility first, then the controls.
