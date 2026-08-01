---
title: Building an agentic harness that outlasts the model (2026)
kind: blog
topic: agents
subtopic: harness
secondary_topics:
- product-engineering/security
summary: 'Shopify details Dispatch, their Ruby-orchestrated multi-agent security-scanning
  harness: it partitions a Rails monolith by size/scope, runs parallel Hunter agents
  per partition backed by shared architecture artifacts, verifies candidate findings
  with a different model acting as a test oracle, then opens fix PRs -- across 80+
  applications and thousands of scans it produced 300+ findings valued at $400k+ in
  equivalent bug-bounty payouts.'
triage: null
skip_reason: null
source: shopify
url: https://shopify.engineering/building-an-agentic-harness-that-outlasts-the-model
author: Zack Deveau
published: '2026-07-29'
fetched: '2026-07-31T07:03:50Z'
classifier: claude
taxonomy_rev: 2
words: 1869
content_sha256: f0facb37f4f259d94bcf37fa1434226c43424313405ea8b4c5f6b9023b5aa92e
---

# Building an agentic harness that outlasts the model (2026)

### Building an agentic harness that outlasts the model

Our role in Application Security at Shopify is to keep our merchant and buyer data safe. Models have been providing us with increasingly advanced ways to do that. We’ve built an agentic code review and test oracle harness that discovers vulnerabilities in our software, proves them with real tests, and provides Shopify-tuned fixes before presenting them to our developers.

Over the past five months, we’ve been evaluating new security-tuned frontier models inside that harness. The best models we tested were genuinely better than our baseline frontier models at discovering findings. But they also produced more potential issues that needed to be confirmed. In one audit, a model uncovered more than 30 candidate vulnerabilities. After validation, every one was downgraded to low or medium, found to be a false positive, or reclassified as defense in depth.

The models are getting better, but the most important piece of the system remains the harness.

Our scanning workflows run across our most important public-facing surfaces. They produce real findings in our web applications and help us close the loop quickly by opening relevant, Shopify-specific pull requests.

In this post we share our hard-earned lessons from pointing our harness at one of the largest Rails monoliths in the world. We walk through how our multi-agent orchestration works and share some outcomes so you have the best chance of repeating our results.

## Our latest workflow

Our internal harness orchestrator named Dispatch is a thin Ruby client that abstracts the complexity of agentic scanning at scale away from scan authors. It enables authors to easily create category-specific bug hunting agents, which then run safely, provide a test oracle, and open PRs for findings.

![](https://cdn.shopify.com/s/files/1/0779/4361/files/1.png?v=1785256078)


On the first run against a target application, our pipeline builds code partitions based on size and scope considerations (detailed further in this post). It then proceeds with a full scan, deploying Hunting agents in parallel for each partition. Initial runs also produce reusable artifacts that document available APIs and data models which help us reduce re-work and provide condensed application-specific context to downstream agents. This enables them to make more informed decisions while keeping the bulk of their context window open and focused on the primary task.

All scan data and artifacts are stored in a custom Rails backend and kept up to date by subsequent diff-based scans. 

![](https://cdn.shopify.com/s/files/1/0779/4361/files/2.png?v=1785256112)


On follow-up runs, the pipeline compares the latest commit with the previous commit, then scans only the latest changes. This drastically reduces token spend while maintaining coverage across the large codebase. It updates any persisted artifacts, like partitions and documentation, with any new information found in the diff.

We leverage both "generalist" and vulnerability-specific bug hunting agents, each with multiple layers of software security and Shopify-context encoded to guide their search.

Dispatch runs each scan as an ordered set of stages:

| 
 | 
 | 
 | 
| 
 | Finds the right application test commands and verifies the suite can run. | Verifiers and fix authors should not spend turns having to discover how to run tests. | 
| 
 | Produces a shared description of data models, APIs, authorization patterns, and boundaries. | Shared context artifacts are provided to downstream agents and reused in subsequent scans. | 
| 
 | Catalogs all relevant files in a flat list within the target repository. | Helps the workflow focus on files that matter. | 
| 
 | Groups catalogued files into coherent partitions; outputs a JSON artifact. | Related code stays together. Hunters get a bounded set of tokens to study. | 
| 
 | Runs one Hunter per partition in parallel. Leverages skills that enable cross-repository code search to produce candidate findings. | Running these in parallel dramatically speeds up the scanning process. Giving them tools to access out-of-repo context helps guide correct decision making. | 
| 
 | Runs Verifiers sequentially to author and execute tests against candidate findings. Uses a different model than the Hunting agent. Adversarial review reduces noise and prevents blind spots. | Tests are the oracle; sequential execution avoids port, database, and fixture collisions. | 
| 
 | The Ruby runner executes deduplication, severity scoring, and other shared operations on all findings prior to reporting. | Ensures we’re producing actionable and consistent findings. | 
| 
 | Joins findings and test results into human readable output. | Provides insight into the findings and rationale for exploitability. | 
| 
 | Runs fix author agents per-finding. Creates a branch and authors a PR body. | Developers receive draft PRs with context, tests, and proposed fixes. | 

## The results

With this workflow, we’ve been able to perform complete scans of over 80 unique applications so far, including our massive Rails monolith known as Shopify Core. We continuously onboard new cohorts based on our assessed criticality of that service.

Over roughly six weeks, we’ve run thousands of scans, produced over 300 findings ranging from defense-in-depth improvements to resolved security incidents.

We conservatively value these findings at over $400,000 in equivalent bug bounty payouts. Of those, two findings would have been rated as Critical according to our severity calculator.

A full application scan with publicly available frontier models costs between $50 and $300. The cost is highly dependent on the model choice and size of the app. Incremental diff scans are much cheaper, roughly $5 to $50. That coverage spans across all our Shopify surfaces, running while we sleep, at a fraction of the cost of the bugs it prevents.

## The lessons

### Building test oracles for web vulnerabilities

Exploitability is a challenging thing to confirm in web application testing. Web vulnerability candidates often don’t have direct test oracles, like the ones memory safety vulnerability candidates have via compiler flags.

Shopify has a strong local development culture stewarded by our Environments team which builds and maintains our developer tooling. This enables us to leverage mature integration, unit, and functional testing pipelines across all our target applications. Our Verifier agent is tasked with authoring and embedding its validations into the existing tests and primitives available in that app.

We encoded strict guidelines in our agents about what does and doesn’t constitute a “proven finding.” For our IDOR-based Verifier, for example, some of the elements we encode are:

- Work backwards from public call sites and leverage internal tooling to search across all our web clients.
- Ensure that we create fixtures belonging to two different tenants.
- Tests must exercise as much of the public stack as possible. We cannot rely on unit tests at the Model layer alone to determine exploitability.
- Tests must extract impactful cross-tenant data. Booleans, raw IDs, and other similar values are downgraded in severity to “Low.”
- Ensure that we’re evaluating above and below the current layer for upstream or downstream controls that reduce the severity of our findings. Do not stub important up/downstream controls.

Findings that cannot be proven within these constraints are either rejected or downgraded to a “Low” or “Medium” rating depending on potential criticality. This rating intends to include findings that are very unlikely to be exploitable or require some typically un-obtainable prerequisite like a secret token.

### Producing consistent and reliable results

We initially experimented with “security generalist” multi-agent workflows and ran them manually against repositories.

We observed promising results with some true positive findings, but at the cost of a high volume of "potential" or "theoretical" issues which were not relevant in practice. Any proposed fixes were often incorrect or presented in theoretical terms. Results were also very non-deterministic.

Working from first principles, we found this to be the least effective way to extract consistent and accurate findings from our models. Without a clear vulnerability type, models would often fill up their context windows chasing an unordered list of “potential” findings and either give up on the task or be forced into compaction before finding the actual vulnerability.

That being said, with a rigorous set of guiding principles encoded, a “generalist” agent can help fill potential gaps left by category-specific agents. Results need to be handled with additional scrutiny as they have higher potential to produce claims with lower accuracy and recall due to the limitations discussed above.

### Keeping costs low

The most expensive way to perform agentic risk discovery is to point a full agentic pipeline at every single file in your repositories and ask them to find category-specific vulnerabilities. The least expensive is to run a single agent across your entire repository and task it with finding *any* vulnerability.

The tradeoffs are cost and speed over accuracy, recall, and quality of findings.

In our quest to extract maximum findings for minimum costs, we experimented with packaging our target repositories into focused partitions which represent a subset of all total files. An agent is tasked with grouping them based on specific criteria:

- Aim for token counts of roughly 20-30% of the context window of the model in use to leave lots of room for code exploration and tool use.
- Group files by related domain, purpose, or feature.
- In each partition, include a set of files covering global dependencies or important shared context.

To experiment with this idea, we created benchmarks where we reintroduced previously confirmed vulnerabilities into our applications locally and performed comparison testing between partitioned and non-partitioned approaches.

When using partitions, we observed improved accuracy and recall while keeping costs reasonably low. If you tune the size and scope of partitions to the vulnerability category, you can land on a generally correct scope.

![](https://cdn.shopify.com/s/files/1/0779/4361/files/3.png?v=1785256174)


### Reach for determinism when it makes sense

Where possible, hand agents deterministic scripts inline, or author dedicated skills that call scripts to accomplish a task when you need structured inputs or outputs.

For example, create a simple skill that enforces JSON document structure programmatically and task agents with populating the documents instead of owning the whole process.


## output

You’re tasked with creating an output document with the following format

<document>

### Title

### Findings

</document>

```

vs

```

## output

You’re tasked with providing the following script with the relevant parameters for your findings and executing it. The output artifact is report.md.

markdown_document_formatter.rb --title <finding-title> --finding <description-of-the-finding>


Deterministic scripts mean fewer malformed outputs and parseable results that you can verify.

### The harness outlasts the model

New frontier models arrive often, and each finds more candidate vulnerabilities than the last. That’s important progress. But a better hunter also produces more confident-sounding noise, and noise sent to a developer is worse than no finding at all. It wastes time and undermines trust with the AppSec Team.

The most durable advantage you can develop is a harness tuned to the particularities of your software development ecosystem:

- A test oracle that proves exploitability with a real integration test
- Partitioning that keeps cost and recall in balance
- Cross-model verification that catches one model's mistakes with another
- Deterministic code that owns credentials, Git, and storage so the agents don’t have to

Building a harness that allows you to quickly migrate to the latest model is important. Even more important is to build a harness that you can continue to iterate on. You’ll keep this part as new models come and go; this is where the innovation is.
