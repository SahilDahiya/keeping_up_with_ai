---
title: 'Bringing Cresta''s AI Agent to Avaya Infinity: Inside a New WebSocket Voice
  Integration'
kind: blog
topic: null
subtopic: null
secondary_topics: []
summary: null
triage: null
skip_reason: null
source: cresta
url: https://cresta.com/blog/bringing-crestas-ai-agent-to-avaya-infinity-inside-a-new-websocket-voice-integration
author: Yufeng Huang
published: '2026-07-31'
fetched: '2026-08-05T06:52:18Z'
classifier: null
taxonomy_rev: 2
words: 2778
content_sha256: 2fce6bf312575e3d0b5d85a78ec228e7d7ac18a850ec3426c7aef59772058fa8
---

# Bringing Cresta's AI Agent to Avaya Infinity: Inside a New WebSocket Voice Integration

When a customer calls a contact center, the hardest few hundred milliseconds in the whole system fall between the moment the caller stops speaking and the moment the AI starts responding. Closing that gap takes a clean, fast path for audio to leave the phone system, reach an AI agent, and come back, all while the call is live and the customer is waiting. Getting this timing right is the difference between a frustrating wait and a seamless experience that builds immediate trust, and solving it is what unlocked every feature described below.

Avaya recently built exactly this path into its **Avaya Infinity platform**: a new WebSocket media integration that lets an outside service stream call audio in both directions and exchange control messages in real time. Cresta partnered with Avaya as one of the first to build on this new interface, deploying a [**Cresta AI Agent**](https://cresta.com/ai-agent) on Infinity. This post covers what makes the design interesting from an engineering point of view, the thinking behind it on Avaya's side, and the not-so-obvious lessons we picked up shipping a real integration on a brand-new interface.

## What We Shipped

Working against Avaya's new WebSocket interface, the integration now supports a full voice AI workflow:

- **Real-time AI voice conversations.** The caller talks to a Cresta AI Agent that listens, reasons, looks up answers, and speaks back. Even if the caller interrupts mid-sentence, the AI agent stops to listen, allowing for a natural flow.
- **Live-agent handoff.** When the AI decides a person should take over, it routes the call to the right agent queue, maintaining all conversation context in the process.
- **Transfer call.** A direct transfer becomes the better move when the caller's request requires routing to a specialized department, a different queue, or an external service rather than the standard live-agent pool.
- **Live transcript on the Avaya Agent for Desktop.** When a person takes the call, the whole conversation the caller had with the AI agent is already on their screen.
- **AI summary at handoff.** The agent also gets a short, AI-written summary of the call, so there is no "can you repeat everything you just said?" moment.

## Inside Avaya's Design, and Why It Was Built This Way

When Avaya set out to build streaming media into Infinity, the team made one decision early that shaped everything after: this would not be just a bot integration. It would be a platform connection that happened to support a virtual agent first. The failure mode they wanted to avoid was the one-off, the single-purpose pipe that works right up until the second partner or the second use case arrives and everything gets rebuilt from scratch.

We've connected Cresta AI Agent to a number of contact center platforms, so we have a good sense of what "normal" looks like. That early decision shows up everywhere in the interface. Here's what stood out to us as we built against it, and the intent behind each choice.

**The platform calls you, not the other way around.** In many streaming setups, your service opens the connection and the contact center responds. Avaya flips that. Its media system reaches out and opens the connection to you. That changes how you build: your server has to be ready to accept a flood of incoming connections, and you track each call by its session rather than by the connection itself, since connections can come and go.

**One connection, two levels of use.** The interface is deliberately built to work at two levels. If a service just needs the basics, the protocol hands over the raw media stream and gets out of the way: take the audio and route it however you like. Build at a higher level and every service is modeled from the same foundation on that same protocol, whether that's a virtual agent, ASR, TTS, transcription, agent assist, translation, or recording.  That layered design is why setup happens in two steps. First, the two sides agree on the basics of the media stream, like the audio format and which streams are flowing. Second, you turn on the specific service you want.

The shared foundation is the point. For the services Avaya builds natively, like ASR, TTS, and transcription, a partner's engine can stand in for Avaya's, and everything else running on Infinity keeps working as before. For capabilities Avaya doesn't build itself, that same modeled interface is the extension point. Our AI Agent is the first virtual agent of its kind on the platform, and it lands as a first-class service, not a bolt-on wired in around the edges.

**Shared foundation, prescriptive services.** None of that means every service looks the same, and that's deliberate. Each service is more prescriptive on top of the common media layer, with a well-defined set of streams and events that unlock what makes that service valuable. Agent assist, for instance, carries audio per participant, which means handling multiple streams at once. 

**Everything flows up to Infinity.** However a service uses the connection, the data moves the same way each time: up to Infinity, which decides what to do with it, whether that's placing a transcript on the agent's desktop at handoff or driving the next step of the call.  And it isn't only audio that travels. The connection carries the conversation too, like the running transcript we hand to the agent's screen at handoff. Of the platforms we've integrated Cresta with, Avaya's is the first whose connection carries the live conversation this way, and that turned out to be where a lot of the interesting work went.

**Audio travels in tagged packets.** Instead of sending a raw audio stream, Avaya wraps the audio in compact packets. Each packet starts with a small label that says which stream it belongs to, what order it goes in, and when it was captured. That lets several audio streams (say, the two sides of a call) share one connection while staying clearly separated, and it gives both ends what they need to spot dropped audio and keep playback smooth.

**Resilience is built in.** Avaya treats each call session as something built to survive trouble. It has built-in ways to recover after a connection drops unexpectedly, regular check-in messages to confirm the link is still alive, and a clean, confirmed way to end a call. Sign-in is also simple to operate: each connection presents a signed token that's checked before the connection is even accepted, with no shared login state to keep in sync between systems. As Avaya's team summed it up during our build, you can rotate your security keys all day and it just works.

Put together, the design is generic where an integrator wants raw control, prescriptive where structure unlocks a service's value, and standardized enough that a partner integrates once and grows over time. Being first on the interface puts us in a position to test whether that promise holds.

## Why We Built It In Weeks, Not Quarters

Avaya's integrate-once philosophy has a mirror image on our side. Cresta's voice system keeps three things separate: how audio moves on a given platform, what the AI does with it (speech-to-text, then deciding when the caller has finished a turn, then the AI Agent, then text-to-speech), and how the call is controlled (transfer, hang up, handoff). Each new platform only needs a thin layer for moving audio, a translator for that platform's message format, and a handler for its call-control commands. Everything after that is shared.

So standing up Avaya came down to three jobs: teach our translator to read and write Avaya's audio packets, add a handler that speaks Avaya's control messages, and let the existing pipeline do the rest. That plumbing we'd built earlier, the part nobody finds exciting, is exactly what carried us from a simple echo test to a live human handoff in six weeks with one engineer dedicating 50% capacity.

## Four Lessons From Making It Real

A spec tells you what's possible. Live calls tell you what's true. The interesting work was in the gap between them.

**1. Reply the moment the other side is ready.** Our first setup sequence held its confirmations back to keep things tidy, and it promptly froze. The platform waits for our reply before it sends the next step, so the fix was to confirm the session the instant it opens and then keep going. Two more things shaped how we handle setup:

- The platform sends the setup messages together, on purpose. Once batching is turned on, the message that opens the session and the message that starts the bot arrive in a single packet. That is by design, and it works in our favor: our side gets everything it needs to bring the call up in one exchange instead of two round trips, which keeps dead air off the front of the call. The practical effect is that one packet can carry more than one message, so we taught our reader to stop assuming one packet meant one message and to split them apart.
- We keep a small buffer for the caller's first words, just in case. The platform holds the caller's audio until we have acknowledged the setup, so with batching there is rarely anything waiting. We keep the buffer anyway as a safety margin, because whether the setup messages arrive together or one at a time is not something we control, and we never want to lose the opening words of a call.

**2. How you pace the audio affects speed, not just sound.** Our first audio came out slow and choppy, but the cause wasn't the audio format. It was how finely we sliced the outgoing audio. When we sent it in tiny pieces, we relied on the system's internal timer hundreds of times a second, and its small timing wobbles turned into gaps in the agent's speech.

The obvious fix, bigger pieces, has a catch: the larger the piece already in flight, the longer it takes for the agent to stop talking when the caller jumps in. We started at the protocol's smallest slice, 20ms, hit performance problems on our side, and moved to the protocol maximum of 200ms. That made speech smooth and kept interruptions feeling quick. There's headroom to tune it back down for an even faster cut-off when the caller barges in, which is exactly why we kept chunk size as an adjustable knob rather than a hardcoded value.

That range is also a quiet credit to Avaya's design. Some streaming interfaces enforce rate limits that make chunks below 100ms impossible, and those limits are fixed on the platform side. Avaya's protocol lets us pick our operating point anywhere along the 20ms to 200ms spectrum and adjust it as we learn. We also added audio diagnostics on every call so we could actually see the timing instead of guessing.

**3. The agent's screen has its own rules.** Handing the live transcript to the agent at handoff surprised us a few times, because the screen has expectations of its own:

- The order came out scrambled. The screen arranges the conversation by each line's timestamp, and we were sending the lines all at once with none. Now we stamp each line and let the screen sort them into the order the call actually happened.
- Lines went missing. Even with the order fixed, sending the whole transcript in one quick burst caused some lines to drop. A bigger buffer wasn't the answer. We stopped sending everything at once and instead send each turn the moment it is final, which spreads the transcript naturally across the real length of the call.
- The agent's own replies arrived in pieces. The AI speaks a sentence a little at a time, and its reply grows as it is spoken, so a single answer could reach the screen as a handful of stray fragments. We now gather the pieces of one reply and stitch them into a single clean line before it goes out.

**4. Shutdown is where transcripts go missing.** Sending each turn the moment it's final means a background worker keeps sending right up until the call ends. That sets up a race: the worker is still trying to send turns while the call is shutting down.

And the turn most at risk is the one you can least afford to lose. The last line before a handoff is rarely filler. It's usually either the AI Agent telling the caller they're being transferred, or the caller saying the very thing that triggered the transfer. Both are exactly the context the human agent picking up the call needs most.

Between our own testing and code review, we turned up three ways that last turn could go wrong:

1. **The false success:** The AI finished its last line just after we'd shut the sender down. We logged the turn as sent, but it never actually reached Avaya. This was the dangerous one, because everything looked fine. The logs reported success, so no one would ever know a turn went missing.
2. **The visible drop:** The AI finished its last line right as the sender was shutting down, so the turn was accepted and then discarded before it went out.
3. **The double start:** A rarer internal misstep that could start our sender twice and waste resources. It isn't possible today, and we blocked it anyway.

The fixes came in layers. First, we gave the worker an explicit "stopping" state, so a turn that arrives mid-shutdown is caught and handled on purpose instead of slipping through, which closes the first two scenarios. Second, we made every dropped turn show up loudly in the logs and easy to search for, so if one ever does slip, we see it. And we guarded against the double start even though it can't currently happen, because "can't happen today" has a habit of becoming "happened in production" after enough refactors. If a transcript can go missing, you want to hear about it from a dashboard, not from a customer.

One bigger lesson runs through all four: with a young interface, be generous about what you accept. We built the integration to tolerate missing optional details, unexpected extra ones, and message types we don't handle yet, so a spec that's still changing can add things without knocking our calls offline. Being a good early adopter is mostly humility built into your defaults.

## What's Next

The integration is live and it's the foundation for joint Avaya and Cresta deployments. The part we're most excited about is making the human side of the call as smart as the AI side. Today, when the AI Agent handoff, the human inherits the transcript and the summary. Next, we want them to inherit live help. The plan is a transfer that lands the agent in an Avaya desktop already running **Cresta Agent Assist**, so the moment they pick up, Cresta is listening with them and surfacing answers, next steps, and guidance in real time. One continuous, assisted call from the first ring to the resolution, with no cold start when a person steps in.

This is where the two architectures pay off together. Because every Infinity service is modeled on the same foundation, extending from a virtual agent to agent assist or translation isn't a new integration. It's building the piece unique to that service on a connection we've already stood up.  Agent Assist comes first. The same path could later carry **Cresta's Real-Time Translation**, so a caller and an agent who speak different languages can still understand each other on a live call. Closer in, we're working on higher-quality audio for clearer voice, automatic reconnection if a call drops, and richer call-control options.

*"Avaya has paved the way for a scalable and impactful deployment of AI by building a modern platform designed to work seamlessly with Cresta's solutions. We are incredibly excited about the future of the Infinity platform and the partnership between Cresta and Avaya." -* *Dong Zhao, Tech Lead Manager, Voice AI Infra, Cresta*

*"As a leader in AI for Customer Experience with integrations across virtually every enterprise CCaaS platform, Cresta was an ideal early partner for Infinity's WebSocket media integration. They were with us throughout the design process and quick to provide meaningful feedback, rigorous in testing, and strong proof that the approach works for advanced voice AI."* - *John Graybill, Director of Product Management, Avaya*

Book a [demo today](https://cresta.com/request-a-demo) to see how the Cresta AI Agent on the Avaya Infinity platform delivers seamless voice conversations, complete with live transcripts and instant AI summaries right at handoff. 

Explore the [Avaya Infinity partner ecosystem](https://www.avaya.com/en/products/infinity-platform/ecosystem/?_gl=1*t9b8aw*_up*MQ..*_ga*OTcyNDMzOTE5LjE3ODU0NDA0NzI.*_ga_4FRNP180SQ*czE3ODU0NDA0NzIkbzEkZzAkdDE3ODU0NDA0NzIkajYwJGwwJGgwJGRUSXZGdFh4dHJ3SUpxV254UjhqSEs0Q1ppbFBUTEtVTlpn) to learn more.
