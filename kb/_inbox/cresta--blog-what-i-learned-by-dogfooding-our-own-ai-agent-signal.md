---
title: What I Learned by Dogfooding Our Own AI Agent, Signal
kind: blog
topic: null
subtopic: null
secondary_topics: []
summary: null
triage: null
skip_reason: null
source: cresta
url: https://cresta.com/blog/what-i-learned-by-dogfooding-our-own-ai-agent-signal
author: Topher Boehm
published: '2026-07-21'
fetched: '2026-07-22T06:51:04Z'
classifier: null
taxonomy_rev: 2
words: 1862
content_sha256: 8b6a74bbecbf6c3499dd0294939c044a8a0998bd4dfe0ab8f0b5b904db833e84
---

# What I Learned by Dogfooding Our Own AI Agent, Signal

There’s a crucial inflection point when it comes to introducing your customers to an AI agent. Testing stops being theoretical, the rubber hits the road, and the stakes of maintaining customer trust become real.

You can build [comprehensive evaluation suites](https://cresta.com/blog/why-ai-agent-evaluations-fail----and-how-the-swiss-cheese-model-prevails) and [rigorously test](https://cresta.com/blog/introducing-ai-agent-testing-2-0-confidence-at-launch-confidence-at-scale) for tone, accuracy, escalation, compliance, hallucination risk, and customer-specific guardrails. You can run every pre-launch checklist the right way. But eventually, a harder question emerges:

*Are we testing this agent against the customers it will **actually** interact with?*

Pre-production test suites might cover the “happy path” perfectly and still miss the impatient buyer who asks three questions at once, the skeptical evaluator who wants a competitor comparison, or the visitor who starts in chat but would rather speak to a human agent once the conversation becomes more nuanced.

When tests are built from generic assumptions, they [tend to flatten the customer](https://arxiv.org/html/2604.08362v1) into something simpler, calmer, and more cooperative than reality. To solve this issue, we built [Synthetic Customers](https://cresta.com/blog/introducing-synthetic-customers-a-living-model-of-your-customer-base): realistic, representative customer personas built from real conversation data. This capability surfaces behavioral patterns from the conversations already happening across the business: what people ask, how they ask it, what frustrates them, how they escalate, and where they need more help. 

Those personas can then be used to understand the customer base, test AI agents, train human teams, and pressure-test changes before they hit production.

Now, I’m a Forward Deployed Product Manager here, meaning I'm hands-on with customers as we discover, build, and deploy new AI agents. So when we built this, like a kid in a candy shop, I wanted to give it a go on our own data to see a) if its findings were meaningful, and b) how good (or not) the resulting customer batching was.

## Dogfooding Our Own AI Agent

Firstly, I ran this on [Signal](https://cresta.com/blog/meet-signal-crestas-ai-agent-powering-a-new-kind-of-website-experience), Cresta’s AI agent on our website, that little chat button down on the bottom right-hand corner. That button has a number of functions, but primarily I'd like to think of it as a way for people to get a sense of how we work and what we do by genuinely interacting with our product. 

More than a chatbot, it helps visitors learn about Cresta, ask product questions, find relevant resources, and take next steps like booking time with our team. It’s also a real expression of the AI Agent capabilities we bring to enterprise customer experience: conversation intelligence, knowledge grounding, tool use, and the ability to move visitors toward action, making it an interesting test case for Synthetic Customers.

Website visitors, as you might imagine, are not a neat, single audience. We’ve learned anecdotally that prospective employees, internal teams, and even adversarial actors poke around on Signal. Some prefer a fast answer in chat, while others want to actually speak to the AI agent. Some are polite and patient, while others are blunt, skeptical, or even adversarial.

Reading every Signal conversation manually would be useful, but that just isn't viable from a human resources perspective. Synthetic Customers gives us a more structured way to ask:

*Who is actually interacting with Signal, and what is it they’re trying to do? *

To probe for meaningful findings, I ran our Synthetic Customers model over thousands of website interactions across chat and voice, looking for 10 ‘Personas’ or ‘Customer Types’, separating this into two batches for each channel, chat vs. voice. The goal was to understand the major behavioral profiles showing up at our digital front door, and what those profiles reveal about the job Signal is being asked to do.

## The Details Behind the Traffic

The first finding was not surprising: the biggest group is prospective customers asking probing questions about our pricing, looking to schedule demos, or requesting detailed information on how our unified platform works.

What I found most interesting from the output was the behavioral detail underneath in this broad category. Synthetic Customers didn’t just tell us “prospects ask product questions”; it broke this category down into more meaningful personas such as the “Curious Plain-Language Learner” asking broad questions, vs. the “Methodical Due-Diligence Lead” pressing more on differentiation, vendor comparisons, and proof points.

![](https://cdn.prod.website-files.com/67feba4d16c14d85f1696c4f/6a5e81cc7e14575f3cb84187_blog-dogfooding-illus-1-2.png)

A cautious evaluator does not need the same experience as a skeptical decision-maker, just as a technical validator is seeking different information than a business champion. These nuances surfaced by Synthetic Customers go beyond a simple reporting layer, providing teams with a behavioral map of the people the agent is actually serving.

Another interesting pattern? Signal supports both chat and voice, but the visitors who typed to Signal and those who spoke with Signal often brought different expectations into the interaction. Our voice channel, while lower-volume than chat, handles a more rigorous type of judge, with requests for comparisons with other vendors and integrations.

When looking at this data, we have to ask whether the answer worked for the visitor, in that channel, given their intent and behavior. A concise text answer may be ideal in chat, but the same answer read aloud in voice may feel too dense, too slow, or not helpful enough. A chat visitor may tolerate a link detailing next steps, while a voice visitor may need a clearer spoken summary and step-by-step support.

The next thing I was interested to really understand was how effective the customer group-batching actually is. It's one thing to see your top 10 customer types, but are there actually *more* customer types with a long tail? When we cast a net too wide, does that lead us down too many paths instead of focusing on the most common conversations?

This time I looked only at chat and aggregated the conversations twice, once into six personas, and once allowing it to go wider to 16 personas. The only thing I really cared about was whether there was any real additional insight to gain going wider, whether the aggregation judgements of the LLM were too harsh or loose for any real insight.

I surprised myself when I actually preferred the detail of the 16-persona version, most specifically the top six of that group, which together accounted for two thirds of the conversations, rather than the 6-persona set which captured the full 100% of users.

In this group, we got a more granular read on who the top customer personas are and what they are asking. That additional bit of detail is helpful for me especially in materializing which of the archetypes I’d want to act on when it comes to tuning an agent or business insight.

## Now What?

So what do we do with this information? These insights are helpful for us internally in a number of ways.

These are behavioral signals we can track and that I will certainly bring to my customers: for example, when people are interacting with an agent on the website or a voice call, they might be a bit more curt. They could be more direct or not beat around the bush as much. This means customers can rely on their AI agents to really surface honest questions from their customer group.

Internally, these insights plainly tell us what's most important to the people evaluating Cresta, whether that be from a vendor, employer, or partner perspective. Our actions are twofold.

One is immediate: dig into Signal and ensure it’s doing its job answering the questions it’s being asked to the best of its ability – or appropriately leaving those questions to be part of a human conversation.

The second is ongoing: keep watching the questions that Signal is fielding. Every time we release a new product, we see a bump in questions about how it works, who it's for, and what it does… the same is true for any of our customers.

That's not hypothetical for us either. The first thing we changed was the small: we cut our opening greeting down from a paragraph to two lines, because the “Curious Plain-Language Learner” doesn't want to read a mission statement before asking a question, they want the question answered.

We're also treating the two channels - voice and chat - as equally legitimate front doors and improving the way that customers are able to engage with the voice agent out of the native chat widget. The bigger version of that same fix is now on our roadmap too: making the switch between voice and chat more native, treating Signal as one conversation across channels instead of two separate ones.

Anyone running Cresta AI Agent can point Synthetic Customers at their own conversations to see what people are really asking, and use that to keep both their agents and the humans handling those calls trained and up to date.

With Synthetic Customers, the people coming to your business become distinct audiences with distinct needs, which can inform several kinds of action:

- **It can improve agent testing.**We can take the personas surfaced from real Signal conversations and use them as the basis for simulation tests. Instead of testing Signal against generic visitor prompts, we can test how it handles the skeptical evaluator, the rushed demo-seeker, the technical validator, or the voice-preferring buyer.
- **It can improve agent design.**If certain personas consistently ask about integrations, comparisons, or implementation timelines, those paths deserve extra attention. If certain visitor types need a clearer route to a demo, that should influence how Signal guides them. If voice visitors behave differently from chat visitors, the two experiences should be evaluated on their own terms.
- **It can improve go-to-market learning**. Signal is not only answering questions; it’s capturing what the market wants to know before a human conversation begins. The questions visitors ask an AI agent can reveal what prospects are skeptical about, what messages are landing, which claims need support, and where the website is not answering something clearly enough on its own.

Dogfooding Synthetic Customers on Signal reinforced something simple: AI agents create a new kind of customer signal. Every conversation is evidence: it shows you what people care about, what they do not understand, and where the experience either moves them forward or leaves them stuck.

Without the right tooling, that evidence is hard to use. It sits in transcripts, it disappears into aggregate metrics that may tell you volume and containment, but can’t reveal the behavioral subtleties underneath.

Synthetic Customers turn that evidence into a living model of the audience. For Signal, it helped us see the different types of visitors engaging with our website AI Agent, how chat and voice behavior diverge, and where the experience may need to adapt by persona and channel.

Not just: “Did the agent pass the test?”, but: “Did we test the agent against the right customers?”

And once the agent is live: “What are real customers teaching us now?”

That’s the power of eating your own dog food: sometimes the product does exactly what you built it to do, and sometimes it shows you something you would not have known to look for.

Now do me a favor. Pop open Signal and write "I really liked the blog post on Synthetic Customers and Signal" and next time I run this report, I'll get an idea of how many of you actually got this far.
