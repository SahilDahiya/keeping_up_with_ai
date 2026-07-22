---
title: How OpenAI uses human feedback to evaluate and improve LLMs
kind: blog
topic: null
subtopic: null
secondary_topics: []
summary: null
triage: null
skip_reason: null
source: arize
url: https://arize.com/blog/how-openai-turns-user-feedback-into-product-improvements/
author: Sara Verdi
published: '2026-07-21'
fetched: '2026-07-22T06:51:37Z'
classifier: null
taxonomy_rev: 2
words: 2511
content_sha256: fb03e329b9b199965829f99dab5aca11eb2450b3939a924449a8b8429a4084b6
---

# How OpenAI uses human feedback to evaluate and improve LLMs

**Key takeaways**

• OpenAI aggregates explicit and implicit feedback in a shared data layer so teams can measure the same failure across channels.

• An LLM-derived feedback pipeline recovers corrections that users express inside conversations, expanding the volume of actionable signal by two to three times among eligible, opted-in data.

• A hierarchical taxonomy tracks known failure modes, while embedding-based K-nearest-neighbor clustering detects patterns that the taxonomy has never named.

• MCP and skills make the feedback layer callable from Codex and other agents, which can turn an issue into a report, ticket, root-cause investigation, or pull request.

• The loop closes after the relevant cluster declines and the product metric moves.

**How OpenAI turned a voice mode bug report into a pull request**

A few months after OpenAI assembled its feedback system, someone forwarded a screenshot from ChatGPT voice mode in which an image had rendered strangely. Because the screenshot carried neither reproduction steps nor an estimate of reach, it would ordinarily have started a scavenger hunt through support queues, logs, and ownership charts. Using an internal skill and MCP, Codex searched for related feedback, located relevant conversations whose metadata pointed toward the right logs, traced the failure into the codebase, and produced both a report and a pull request.

[Stuart Sy](https://www.linkedin.com/in/stuartsy/), a member of technical staff in OpenAI’s Future of Work organization, called it the first glimpse of a “magical loop.” A stray screenshot had become an evidence-backed engineering task because the system could answer questions that the image itself could not, including how often the failure occurred, which users encountered it, what production context connected the reports, and where the cause lived in the code.

That situation revealed where the engineering bottleneck moves once agents can implement changes quickly. Teams still need a reliable way to decide which failures deserve attention, assemble enough context to reproduce them, route the problem to the right owner, and verify that the fix changed production behavior. That same shift—from human-operated debugging to a systematic [AI improvement loop](https://arize.com/glossary/ai-improvement-loop/)—showed up across other [Arize Observe 2026](https://arize.com/observe/) sessions as well.

**Code generation moved the bottleneck downstream**

Sy began with a change in software economics that most development teams can already feel. “Code is cheap to generate, designs are cheap and easy to make,” he said. A prototype can appear in hours, while the surrounding organization may still need days to learn that users are stumbling over the same issue.

As implementation accelerates, the value of a high-bandwidth learning loop rises with it. A team that can ship ten times faster gains little when its understanding of production remains trapped in weekly support summaries, scattered spreadsheets, and screenshots passed through Slack.

The raw material is abundant, although it arrives through instruments with different biases. Reddit and X can surface developer sentiment quickly, while a broken connector is more likely to appear in a support ticket or bug report. Message ratings capture users willing to click, sales calls capture accounts important enough to receive direct attention, and interviews capture the small group invited into the room. Each channel describes a real part of the product, yet none provides the whole picture.

OpenAI’s answer was to normalize those signals in a shared system while preserving their provenance. Sy described the target as a repeatable path “from vibes to evidence and finally to action.” In engineering terms, the company was building an [observability](https://arize.com/docs/ax/observe/tracing) and control layer for user experience—closely related to the production [LLMOps feedback loop](https://arize.com/blog/from-production-traces-to-better-ai-agents-automating-the-llmops-feedback-loop/) pattern of turning traces into better agents.

**Feedback becomes an event stream**

Before agents can reason over feedback, an organization has to decide what counts as a feedback event. OpenAI began by consolidating material that had accumulated across Google Sheets, Airtables, and team-specific pipelines. The unification was conceptually straightforward and operationally tedious, which is often the signature of infrastructure that later appears obvious.

A smaller team implementing the same pattern would benefit from representing every signal through a consistent record. A conceptual event might look like this:

```
```
```
feedback_event = {
    "source": "chat_correction",
    "product_surface": "voice_mode",
    "conversation_id": "...",
    "trace_id": "...",
    "raw_feedback": "...",
    "taxonomy_path": ["rendering", "image_output"],
    "embedding": "...",
    "classifier_version": "...",
    "confidence": 0.91,
}
```
Although this is derived from the architecture Sy described, OpenAI’s production implementation remains proprietary.

Because the raw text preserves the evidence while the identifiers connect the experience to runtime context, teams can audit every derived label across model, prompt, and taxonomy changes. Source metadata also keeps a Reddit spike from being mistaken for a representative sample of the full user base.

A shared store without provenance quickly becomes an anecdote warehouse. A useful event model lets teams count the same failure across channels, inspect representative examples, join complaints to [traces](https://arize.com/docs/ax/observe/tracing) or logs, and reprocess historical data when a classifier changes.

**The most valuable complaint may never be submitted**

Direct feedback has a steep participation curve, as Sy demonstrated by asking the audience how many people had used ChatGPT, rated a response, filed a bug report, and contacted support. The number of raised hands fell at every step.

Most sessions occupy the quiet middle, where an experience feels disappointing enough to alter behavior and still fails to motivate a formal report. In conversational products, however, the next user turn often contains the missing signal. When someone replies, “No, that’s wrong because of XYZ. Please fix,” the correction includes dissatisfaction, a diagnosis, and sometimes the expected answer.

OpenAI uses an LLM to extract structured, synthetic feedback from eligible conversations involving users who have opted into model training. According to Sy, the additional signal increased the volume of actionable feedback by two to three times.

That extractor functions as an [evaluator](https://arize.com/docs/ax/evaluate/evaluation-concepts/evaluation-fundamentals), so its design needs the same rigor applied to production measurement. Its model and prompt need versioning, its categories need a reviewed calibration set, and its confidence policy needs room for abstention. Precision also matters by category because a style complaint and a safety failure carry different costs when misclassified—the same discipline that shows up in [LLM-as-a-judge](https://arize.com/blog/how-to-build-llm-as-a-judge-evaluators-that-hold-up-in-production/) systems that have to hold up in production. Without those controls, a classifier update can masquerade as a product trend.

Because the privacy boundary belongs in the same design, teams need explicit rules for eligibility, retention, access, redaction, and the downstream agents permitted to retrieve raw conversations. Aggregate signal becomes useful only when the collection policy remains legible to the people responsible for the system.

The episode known as Goblin Mode illustrates both the opportunity and the limitation. For a period, one model personality kept introducing goblins, trolls, and other fantasy creatures where they did not belong. An analyzer could convert the resulting user corrections into structured labels such as style failure, irrelevant context, or poor relevance.

Then the taxonomy runs into a wonderfully specific problem. As Sy asked, “What if you have no goblin node?”

**Taxonomy gives the system memory while clustering supplies novelty**

A hierarchical taxonomy creates continuity across teams and releases. When product, model, and platform groups use the same definitions, they can compare category volume, affected surfaces, user segments, and changes after deployment without reconstructing the meaning of every label.

The hierarchy also encodes what the organization already knows. A Goblin Mode complaint might fall beneath response quality, relevance, and style, which makes it visible in trend lines even before anyone invents a dedicated category for fantasy-creature intrusions.

Because emergent failures require a second sensor, OpenAI uses embeddings, a K-nearest-neighbor approach, and LLM assistance to search a recent window of feedback for clusters that meet useful size and quality thresholds. A new cluster can generate a report, while an investigator can begin with a single tweet or screenshot and ask whether similar reports have appeared elsewhere.

While taxonomy reveals whether a known failure is spiking, clustering asks which new behaviors are beginning to coalesce. The strongest systems allow those clusters to graduate into maintained assets. Once reviewers confirm a pattern, representative examples can seed an evaluator, the cluster can gain a stable name, and the issue can enter both the taxonomy and a [regression](https://arize.com/blog/evals-in-ci-how-to-write-llm-evals-as-tests/) corpus.

The cluster therefore becomes a proposed change to the product’s measurement system. It identifies a failure that deserves a name, a test, an owner, and a post-deployment query—the operational heart of [what a loop means in AI engineering](https://arize.com/blog/what-is-a-loop-in-ai-engineering-anyway/).

**MCP turns the feedback layer into working memory**

OpenAI’s first output was an internal application where teams could browse taxonomy trends, inspect categories, and ask a chat-based data agent questions such as what users thought about a particular model release.

Although the application made the data searchable, organizational action still depended on where the answer landed. A product manager for the ChatGPT iOS app might want a weekly pain-points report in a particular Slack channel, while an engineer investigating a bug needs conversations, log references, affected versions, and code context.

By exposing the shared layer through MCP and reusable skills, OpenAI made the feedback system callable from Codex and other agents—turning the data layer into something closer to an [agent harness](https://arize.com/blog/what-is-an-agent-harness/) that can initiate work, not only display it. The same data could now support scheduled reports, alerts for category spikes, Linear tickets, root-cause investigations, and pull requests. A product manager could iterate on a workflow locally, then submit its prompt, tools, output format, and schedule to a platform service that runs it in the cloud.

The data layer had acquired a tool interface and, with it, the capacity to initiate work. That transition matters because a dashboard places the burden of interpretation on whoever opens it, while an agent workflow can deliver a bounded decision artifact to the place where a team already operates.

**Every automated action needs an evidence contract**

An agent-generated ticket or pull request should arrive with enough context for a human reviewer to judge both the problem and the proposed response. At minimum, that evidence packet should include:

- The taxonomy path or cluster identifier
- Estimated prevalence
- Representative examples with provenance
- Affected product versions
- Conversation or trace references
- Classifier confidence
- A likely owner
- The metric that will determine whether the issue is resolved

Without this packet, automation simply moves ambiguity from a support queue into an engineering queue. With the packet, Codex can begin from an observed failure and receive the context required to investigate it.

Feedback infrastructure meets observability when a feedback event carries a conversation or trace identifier, allowing an investigator to move from a semantic cluster into the exact agent run that produced the experience. For teams using AX or Phoenix, that link can connect the user report to the underlying model calls, tool activity, retrievals, latency, and errors that shaped the outcome—see [AX tracing](https://arize.com/docs/ax/observe/tracing) and [how tracing works in Phoenix](https://arize.com/docs/phoenix/tracing/concepts-tracing/how-tracing-works). The same evidence-first pattern shows up when teams [verify AI-written code](https://arize.com/blog/inside-cursors-agent-factory-how-it-verifies-ai-written-code/) before merge.

The voice-mode rendering case worked because the system enriched the screenshot with neighboring reports, relevant conversations, and log references, which allowed Codex to enter the codebase with a credible hypothesis about scope and cause.

**The cluster becomes a production regression test**

Report opens, generated tickets, accepted pull requests, and decisions influenced by the system all provide useful adoption signals. Sy argued that the durable measure arrives after the fix ships, when the relevant category or cluster begins to decline and the associated product metric improves.

For developers, that requirement turns a cluster into a production-derived regression set. Teams can preserve representative examples, define an evaluator that detects the behavior, [run it against traces](https://arize.com/docs/ax/evaluate/run-evals-on-traces) from the old and new versions, and continue monitoring the affected segment after deployment.

The measurement needs the same discipline as any other [eval](https://arize.com/docs/phoenix/evaluation). Cluster counts should be normalized against eligible traffic, classifier versions should remain fixed or historical data should be rescored, and teams should watch adjacent categories for displacement. A rendering bug that vanishes from one label while reappearing under another has changed the dashboard without changing the experience.

The cleanest closure criterion joins three forms of evidence: the candidate fix passes a reviewed regression set, the production cluster rate falls among users on the fixed version, and a relevant product metric moves in the expected direction. That combination gives the system a way to distinguish shipped code from solved problems.

**A practical adoption path for smaller teams**

Most teams can build the same architectural shape without reproducing OpenAI’s scale. Sy’s advice was to avoid boiling the ocean, which suggests a deliberately narrow first loop.

- **Choose one product surface and one measurable failure.**A tool-call error, irrelevant retrieval, onboarding stall, or recurring style problem gives the team a bounded target and a clear closure metric.
- **Create a canonical feedback event.**Bring together the channels already available, preserve raw text and provenance, and attach conversation or trace identifiers whenever possible. The schema should support reprocessing because taxonomy and classifiers will evolve.
- **Bootstrap a taxonomy, then evaluate the classifier.**An LLM or coding agent can propose the first hierarchy from a sample of feedback, while domain experts refine the definitions, review a labeled test set, and version every taxonomy and classifier change.
- **Add clustering over a rolling window.**Use embeddings to surface dense, recent groups that exceed minimum thresholds for size and coherence. Review those groups before promoting them into alerts, eval cases, or permanent taxonomy nodes.
- **Expose the layer through the tools your team already uses.**A weekly Slack digest may be the right first output, while a mature workflow might create a Linear or Jira issue with an evidence packet. MCP and skills become useful when agents need to query the layer directly—the same “own the loop” idea as an- [agent harness field guide](https://arize.com/blog/own-the-loop-field-guide-agent-harnesses/).
- **Wire deployment to verification.**Save the pre-fix examples, run the evaluator against the candidate change, and schedule a production query that checks the cluster after release. Every issue should carry its own definition of done.

The first version can be small because the compounding value comes from repetition. Each reviewed cluster sharpens the taxonomy, each correction improves the evaluator, and each closed issue teaches the routing system what evidence future investigations require.

**Production learns at the speed of its feedback loop**

OpenAI’s feedback engine gains leverage through composition: a shared data model, evaluators for implicit feedback, a stable taxonomy, discovery for emergent patterns, tool interfaces for agents, and post-deployment checks that test whether the issue receded.

The screenshot from voice mode became valuable because the system could find its neighbors, connect them to production context, place the evidence in Codex’s hands, and monitor the outcome after code landed. What looked like a small rendering glitch exposed the architecture of a [self-improving product loop](https://arize.com/blog/from-human-operated-agent-development-to-systematic-agent-improvement/).

As implementation gets cheaper, the ability to learn from production becomes a source of durable advantage. Every complaint can extend an eval set, improve a skill, clarify a category, and shorten the next investigation. Sy called the process “quantifying the vibes.” Underneath the phrase sits a serious engineering discipline: the product remembers the miss, encodes the lesson, and watches for its return.

Watch Stuart Sy’s full [Arize Observe 2026](https://arize.com/observe/) session on YouTube [here](https://www.youtube.com/watch?v=c1xPkDi-038). For related reading on building agent improvement systems, start with the [AI agent handbook](https://arize.com/ai-agents/).
