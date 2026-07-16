---
title: 'AI observability for agent products: how Atlas uses Logfire'
kind: blog
topic: evals-observability
subtopic: tracing
secondary_topics:
- product-engineering/case-studies
summary: Atlas (8 engineers, 1000 DAU) instruments every span with user/project/workspace
  identity via X-Context-* headers so a coding agent can query production traces in
  plain English; the takeaway is that identity-carrying spans, not the AI, are what
  make trace data answerable.
triage: null
skip_reason: null
source: pydantic
url: https://pydantic.dev/articles/atlas-ai-observability-for-agent-products
author: Harald Tryti Rieber
published: '2026-06-02'
fetched: '2026-07-16T22:03:27Z'
classifier: claude
taxonomy_rev: 2
words: 2095
content_sha256: 98e82791d3eebe3ef65ae4d9f63a087e5dbffd743873074853b2bba1658074a5
---

# AI observability for agent products: how Atlas uses Logfire

*This piece is a guest post from the co-founder and CTO at  Atlas.*


I'm in a couple of CTO circles, and the same worry keeps surfacing, usually quietly: people feel like they're getting left behind. There's always a story about a team running a hundred agents in parallel, some setup that 10x'd them overnight. The hype is real and so is the anxiety. From the outside, it's genuinely hard to tell the incredible from the theater, so I won't pretend to know what works for everyone. But I'm confident about what's worked for us, and my honest read is that the agents are the easy part. The leverage is in the engineering you build around them: good engineering, with AI pointed at it. Here's what that looks like for us, and I hope you'll tell me what's working for you.

And the job really is changing. The cliche is true: more and more, I'm managing agents rather than writing the code myself. They work in parallel, they work overnight, they don't get tired. That's a genuine multiplier. But output was never the bottleneck. But the moment the agents speed up, the bottleneck just moves: to reviewing it all, keeping quality from slipping, and actually understanding what's going on -- in the code, and with your users. So the answer is almost boringly old-fashioned: engineering matters *more* now, not less. It's what keeps review, quality, and insight from grinding you to a halt. The most underrated piece of that, and the one I want to talk about, is observability.

It isn't glamorous, i.e. giving the agent a real view of the world around it, not just the codebase but what's actually happening in production. Once Claude could see what our users were doing and what was breaking for them, I stopped writing queries. I just ask.

At [Atlas](https://www.atlas.co), we're eight engineers, a thousand daily active users, and no data analyst. When I want to know why someone paid us or why something broke for one specific user, I ask in plain English, and the agent reads our traces and tells me. It took me a while to trust it, and there's a real catch I'll come back to. But day to day, it's the closest thing to a product analyst we've ever had.

And I'll be upfront about why it works, because it's the whole point: it's not the AI. Same rule as everything else here -- garbage in, garbage out. It works because our data carries good context, and the part that matters most is simpler than it sounds: every span knows who the user is. There's more to good observability than that, but identity is the piece that unlocks all of it. That groundwork is what made the data worth reading. The agent just does the tedious part: writing the queries, wrangling the output, turning it into something I can actually absorb. It's curiosity about what AI can do, on top of the unglamorous engineering that makes it possible.


Here's the machinery, and the punchline is how little there is.

Every request from our frontend carries three headers: who the user is, which project they're in, which workspace. We set that context once near the app root, and a small helper turns it into `X-Context-*` headers on every outgoing request:

```
// RequestContext.ts -- user_id -> X-Context-User-Id, project_id -> X-Context-Project-Id
addAsHeaders(headers: Record<string, string>): void {
  Object.entries(this.context).forEach(([key, value]) => {
    if (value) {
      const headerName = `X-Context-${key
        .split('_')
        .map((part) => part.charAt(0).toUpperCase() + part.slice(1))
        .join('-')}`;
      headers[headerName] = value;
    }
  });
}
```
On the backend, a middleware you could read in a minute copies those headers into [OpenTelemetry baggage](https://opentelemetry.io/docs/concepts/signals/baggage/). This is the whole foundation, about thirty lines:

```
class BaggageMiddleware:
    """Sets OpenTelemetry baggage per request, so user_id / project_id
    propagate to every child span -- including background task workers."""
    async def __call__(self, scope, receive, send):
        if scope["type"] != "http":
            await self.app(scope, receive, send)
            return
        # X-Context-User-Id -> user_id, X-Context-Project-Id -> project_id, ...
        frontend_context = self._extract_context_headers(dict(scope["headers"]))
        if frontend_context:
            with logger.set_baggage(**frontend_context):  # OTel baggage
                await self.app(scope, receive, send)
        else:
            await self.app(scope, receive, send)
```
Because it's baggage, the identity rides along automatically on every span in that trace -- nobody has to remember to thread it through. A span three layers deep, in a background job that runs ten seconds later, is already tagged:

```
with logfire.span("parse_shapefile", file_size_mb=size):
    features = parse(file_path)   # span already carries user_id / project_id
```
That's it. It's genuinely boring, and that's the point. The reason it's this little code is that it's all just OpenTelemetry underneath; we didn't build a platform, we adopted a standard.

Two things fall out of it. First, "show me everything that happened for this one user, in order" becomes a question with a real answer. Every action they took and every error they hit is stitched together by trace. Second, the multiplier: we put the same IDs on our Mixpanel events. Same join key on both sides, so our observability data and our product analytics stop being two separate worlds. They're one dataset, and I can move between "what happened technically" and "what was the user trying to do" without dropping the thread.

Then the agent; this is where [Pydantic Logfire](https://logfire.pydantic.dev) earns its place as an AI observability platform. The data is just queryable with [plain SQL](https://pydantic.dev/docs/logfire/reference/sql/) (Postgres-flavored, with no proprietary query language to learn). It ships an [MCP server](https://logfire.pydantic.dev/docs/integrations/mcp/), so pointing Claude directly at your production trace data is a few lines of config:

```
{
  "mcpServers": {
    "logfire": { "type": "http", "url": "https://logfire-eu.pydantic.dev/mcp" }
  }
}
```
That combination is the whole reason this works. An agent writes SQL more fluently than I do, so a SQL endpoint over MCP means it can ask production *anything* -- it isn't boxed into the handful of dashboards someone built in advance. So the questions go to the agent instead of to me. "Why did this user pay?" used to mean opening a query editor, remembering the schema, and writing SQL by hand -- the `WHERE attributes->>'user_id' = ...` grind. Now I just ask, and Claude runs that loop itself: it writes the query, reads the trace, follows it, and writes up what it found.

Start with the use you'd expect: things break. A customer messaged that they couldn't share their project and they were the owner, so it wasn't a permissions problem. I gave Claude the project ID and asked it to look. It queried the traces for that project, found a `403` on the share endpoint, and caught something I'd have taken an hour to spot: the user's auth token had refreshed about 200 milliseconds *after* the share request went out. A race condition: the share fired before the token was ready. It wrote the fix behind a token-ready guard, touched three files, added a test, and opened the PR. I reviewed the diff, not the logs.

The half I didn't see coming was using the same setup for product questions, not just bugs -- same traces, same identity, the same single question in English. Here's a real one, lightly trimmed but otherwise as it came back:

A user signed up and got straight to work -- uploading tabular datasets, firing off AI chats to analyze GDP data, building relations, styling the map. They burned all 10 free AI runs across two sessions: 7 in the morning, 3 after lunch. At 16:25:47 their 11th request hit the hard limit. Thirteen seconds later they opened the plans page; inside a minute they'd previewed the invoice and subscribed to Pro. Then they went straight back to work and fired four more chats in the next half hour. Zero errors the whole way. Self-reported industry: consultant.


No dashboard would have handed me that. It isn't a number, it's a story with a cause: someone hit a wall on the exact thing they were getting value from, and paid within a minute to keep going. That tells me the limit is roughly right, and that the AI chat is what's activating. I got it by asking one question.


I keep saying "skill," so let me be honest about what that is: a markdown file. That's the whole thing -- a file that tells the agent how to do one job in your specific setup, with a one-line description of when to reach for it. The two skills doing the work here are almost embarrassingly simple, and we're open-sourcing both. You can drop them in and swap the specifics for your own stack in an afternoon.

The first is the Logfire query skill. Ninety percent of it is schema -- which table, which columns, how the JSONB attributes work, and a list of gotchas. The gotchas are the actual value, and none of them are clever. They're just the mistakes the agent will make against our data until it's told not to:

```
## Gotchas
1. Always pass `project: 'atlas-co'` -- the token isn't project-scoped; omit it and every query fails.
2. A SQL `WHERE start_timestamp > ...` can't widen the query window. Leave the time params off and
   you silently get the last 30 minutes -- even if your SQL says 24 hours.
3. `duration` is an interval, not a number -- wrap it in `EXTRACT(EPOCH FROM ...)` for seconds.
4. The status column is `http_response_status_code`, not `http_status_code`.
```
None of that is AI. It's the knowledge that normally lives in one senior engineer's head, written down once so the agent stops faceplanting on it. The people building these tools say the same thing. [Thariq's write-up on how the Claude Code team uses skills](https://www.anthropic.com/engineering/claude-code-best-practices) is the best guide I've found, and its bluntest advice is that the highest-signal part of any skill is the gotchas section. I believe it now: every line in that list is there because the agent got it wrong, once.

The second skill is the customer-insight one, and it's even simpler. It's the handful of questions we ask about users over and over: what has this user been doing, which features get real traffic, why did someone hit a wall. Plus, how we want the answers back: tables and short narratives, not raw JSON, always compared against the previous period. That's the skill that turns *"what did this person do before they paid"* into the story you read earlier.

Neither skill is impressive on its own, and that's the point. The model is already capable; the skill just keeps it on the rails for your setup. The work was never about prompting. It was writing down what we already knew.


I promised a catch. Here it is: the agent is only as honest as your data, and it won't tell you when your data is thin. Ask about something you've instrumented well and it's superb. Ask about something you've barely tracked and it'll still hand you a confident, fluent, completely plausible answer, built on three spans and a guess. That failure is quiet, which makes it the dangerous one. So I don't take the story on faith: the skills make the agent link the traces it used, and for anything that matters I click through and check. Treat it like a sharp junior analyst, not an oracle -- fast and genuinely useful, occasionally confidently wrong.

The other honest limit is retention. Debugging only needs the last few days, but "are the users who signed up in February still around in May" needs months of history. And storing that much trace data is a real cost-and-config decision, not a toggle. It's the one place this approach bumps into its edges for us, and we're still working out where the line should sit.

But the basic conclusion holds. What moved the needle for us wasn't a clever agent, or a hundred of them. It was unglamorous data engineering, then pointing AI at it and staying curious. Thirty lines of middleware did more than any prompt. For teams building agent products, that unglamorous layer is AI observability, and it's more within reach than most people think. If your telemetry is already decent, you're most of the way there; the two skills here are a place to start, and they're deliberately basic.

So that's ours. I'd genuinely like to hear yours. If you're getting real leverage out of this, tell me what your setup actually looks like. The best ideas in these circles never come from the loudest "10x overnight" posts. They come from someone at lunch going, "here's the boring thing that actually worked."

Want to set this up on your own stack? [Get started with Pydantic Logfire for free](https://pydantic.dev/logfire).
