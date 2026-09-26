---
title: 'Part II: Replacing FinServ IVRs with an AI Agent: Where the Compounding Happens'
kind: blog
topic: product-engineering
subtopic: case-studies
secondary_topics:
- agents/tool-use
summary: 'Case study on scaling an AI agent that replaced FinServ IVR call handling:
  warns that per-agent Average Handle Time rises as the AI automates easy balance/payment
  calls, leaving only hard cases for humans, so the real success metric is total human
  minutes handled and containment volume; also covers staffing around billing-cycle-driven
  call spikes (e.g. a Saturday cycle close compressing into a Monday surge).'
triage: null
skip_reason: null
source: cresta
url: https://cresta.com/blog/part-ii-replacing-finserv-ivrs-with-an-ai-agent-where-the-compounding-happens
author: Randy Young
published: '2026-09-25'
fetched: '2026-09-26T06:09:36Z'
classifier: claude
taxonomy_rev: 2
words: 1778
content_sha256: a1e99b915ee13cd4f2068b07a038c8e901d209bd8483b1dee19525c000b25a9f
---

# Part II: Replacing FinServ IVRs with an AI Agent: Where the Compounding Happens

In [Part 1 of this series](https://cresta.com/blog/part-i-replacing-finserv-ivrs-with-an-ai-agent-a-3-phase-playbook), we covered what a straight IVR replacement buys you: a shorter queue rather than a smarter one, measured on service level and speed of answer rather than a containment percentage. Phase 1 is a migration. On its own, it is not a containment engine.

This is the part where that changes: what to build, when to ship it, and how to report it without the win evaporating under the first follow-up question. For orientation, the same arc from Part 1:

![](https://cdn.prod.website-files.com/67feba4d16c14d85f1696c4f/6a99ed28926a0ce25324d24d_blog-Playbook-illus--1-2.png)

The first decision is when; the build comes second.

## **When: Plan Your Releases on the Financial Calendar**

Customer experience demand in lending and card servicing isn't random; it's driven by the billing statement. When a billing cycle closes, a predictable wave of the same few customer actions follow within days: "What's my balance?" "When is it due?" "I want to make a payment." You can basically set your staffing model to it.

But the *day of the week* the cycle lands on changes everything about how that wave hits you.

A weekday cycle spreads the load. A Friday or Saturday cycle stacks it. When the cycle closes mid-week, the surge distributes across the following business days when your team is in place to handle the influx; it’s busy, but absorbable. When it closes on a Friday or Saturday, the demand doesn't evaporate over the weekend; rather, your queues are closed or thinly staffed, so nothing clears.

All of it, alongside the normal Monday load, arrives at once on the first business day back from the weekend, creating a compressed spike instead of a spread.

We saw exactly this in multiple accounts. The August 1, 2026 cycle fell on a Saturday. The following Monday, call volume roughly doubled versus a normal weekday and then contracted back to normal by Tuesday: the classic weekend-deferred, Monday-compressed signature.

Across that same first business week, delinquent-call share climbed to its monthly peak (~19% of volume) midweek, and payment-intent calls surged right alongside it.

That compression is what does the damage:

- **Hold times spike.** Speed-of-answer is a function of how much arrives at once, not how much arrives in total. A compressed Monday drives far longer waits than the identical volume spread across five days would.
- **Abandonment rises and customer satisfaction (CSAT) slides.** Long holds during the exact window customers feel the most urgency — a payment is due*now* — is the worst possible combination for high customer satisfaction. (Size this with your own CSAT and abandon data; it's the well-established downstream effect of the queue math above.)
- **The mix skews toward payments and delinquency.** Post-statement is when due-date anxiety peaks, so the spike isn't generic; it's disproportionately "I need to pay" and "I'm past due," the two intents most sensitive to a long wait and most damaging when they go unanswered.

Summer amplifies all of it. The day of the week isn't the only calendar force at work; the time of year also compounds it. Throughout the summer, cardholders spend more and travel more, and they tend not to watch their balances closely until the statement lands. The bill is often bigger and more surprising than usual, which converts directly into a heavier post-cycle wave: more "why is my bill this high," more payment calls, and more accounts slipping past due because the balance outran what someone expected to pay.

Stack a summer statement on top of a Friday or Saturday close date and you get the worst call week of the season: elevated baseline demand, compressed into a single Monday, and skewed hard toward payments and delinquency. Those are the weeks to staff for and, better, the weeks to have already automated.

This is the strongest argument for payment workflows. Those weekend-cycle Monday spikes are dominated by precisely the intent an AI agent can now *complete*, and it completes them without initiating a queue, so the compression that wrecks a human-staffed Monday barely registers. 

One financial services deployment saw a launch on a Tuesday to 1 ½x traffic after a Saturday billing cycle, but the expanded use cases (Add a payment method link, pay with a saved payment method and delinquent account collections) saw service level near 100% straight through an early morning peak-cycle surge (see the chart below).

So if you know your cycle lands on a Friday or Saturday, that likely isn't the Monday to launch new features, but it will also likely be the week that your investment in your payment workflows pays off.

![](https://cdn.prod.website-files.com/67feba4d16c14d85f1696c4f/6ab560983e795a23dfe48075_blog-Playbook-2-Replacing-FinServ-figure-2.png)

### **The Average Handle Time (AHT) Trap**

This is the single most misread metric in the whole project, so it gets its own heading. As the agent does its job, **AHT for human agents goes up, often sharply, and that is a sign of success, not failure.**

The mechanism is pure composition. The AI agent automates the short, easy calls first: balance checks, due dates, quick payments. Those are exactly the calls that used to pull the average *down*. After removing them from the human agent workload, what's left in front of a human is the long, complex, genuinely-needs-a-person work. 

Per-call AHT climbs because the mix of surviving calls got harder, not because anyone slowed down. If you judge the deployment on AHT, a win will look like a regression, and someone will then try to "fix" that.

The metric that actually shows what happened is **total minutes handled**, aggregate human talk time across all calls. Even as per-call AHT rises, total human minutes should *fall*, because far fewer calls reach an agent at all. That decline is the deflection. 

The cleanest way to express it for a stakeholder is minutes removed from the human queue, roughly *contained calls × the handle time those calls used to carry*, which converts “*containment went up”* into hours of capacity returned and dollars saved.

The rule of thumb: per-call AHT answers "how hard is the average call that still reaches a person?" Total minutes handled answers "how much work did we take off the floor?" The second question measures the deployment. Report both, lead with the second, and pre-empt the AHT question before it derails the review. Also, many times the human agent is not as efficient as the AI agent is (human agents need to look up accounts, read summaries and digest troubleshooting guides), so for the same tasks, the AI agent can do it faster as it has context and conversational awareness. Longer term, measuring the *AI agent handle time* + *the hold time* + *the human agent time* = *total handle time* for a customer issue, can also be an interesting metric to measure. Because it gives you a full picture of the complete time spent by your customer to resolve an issue.

## **Next Steps: Build the Workflows Behind Your Most Common Call Topics**

Phase 1 gives you something priceless for Phase 2: a clean map of *why people call*. With Cresta Insights you can pull your transfer reasons, rank them, evaluate the handle time and CSAT for the human agent addressing them. In practice, the top of that list is almost always billing and payments: high volume, highly repetitive, and, crucially, **completable** without a human if the agent can take an action rather than just answer a question.

That's the Phase 2 move: pick the biggest containable topics and give the agent the workflow to finish them. In the deployment above, that meant shipping **Make a Payment** and **Payment Link**. 

The clearest evidence we've seen is in the chart above, the intraday view of the morning those features went live:

- Service level (transferred calls with less than 90 seconds of hold time) jumped from a **20.6% average to 96.5%** (+75.9 points).
- Average speed of answer fell from **188 seconds to 9.9 seconds** (−95%).
- Transfers fell from **42.2% to 30.8%** of conversations, roughly a quarter fewer calls handed to a human agent.
- Containment rose from **~57% to 69%** .
- Success call outcomes, calls with a successfully serviced workflow, rose from **36.6% to 40.3%** .

The gap between those last two lines are what matters: most of the lift showed up as *containment*, less as confirmed *resolution which can mean there is more to do around simplification of workflows*. 

**The counterintuitive part: it works on the calls you assumed were human-only.** 

The most striking result from our phase 2 launch came from past-due borrowers, an intent most assume must route to a human collections agent.  Before the phase 2 payment features launched, one financial customer’s agent successfully transferred about **24%** to a human agent, meaning **76%** of collections call backs would hang-up before getting to a human agent.  The week the payments features launched (paying with cards/bank accounts on file and one time PCI compliant debit card payments), that successful touch doubled to **49%**.

The lesson: a big share of "delinquent" calls were never hardship conversations. They were people who wanted to pay and were being bounced to a human for no reason other than the agent wasn’t set up to take the money. Give the AI agent the workflow, and it successfully serves your customers. Delinquent calls post launch saw a **20%** self-service payment success rate combined with a **25%** successful payment with a human agent.  Most of this improvement is coming just on ease of access.

Whenever you hear "that queue can't be automated," for example collection and delinquent accounts, you need to check how much of it is just a transaction/payment flow wearing a scary label.

## **Final Thoughts**

Phase 1 replaces your IVR and earns you a shorter queue; measure it on service level and speed of answer, *not* containment. Phase 2 mines your call topics, builds real workflows for the biggest ones, and buys you actual containment, including on traffic you'd written off as human-only. And phasing itself rewards you with lower risk: a small development at a time you can hyper-care, and a release cadence that keeps the improvements coming.

When planning features, implement them in order of the highest average handle time, highest volume and or impact. Our customers saw great success launching on the Tuesday after their highest volume Monday ever, but we advise launching in the week before high volume weeks, especially the ones that follow a Friday or Saturday billing cycle, and measure like a skeptic. And when the average handle time for human agents climbs, don't flinch: that's the easy calls leaving the human agent queue.

Judge the result on total minutes handled instead. The true value comes in in the second and beyond phases, but it's only available because the first one gave you the map.
