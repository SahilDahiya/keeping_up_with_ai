---
title: The 5 pillars of AI model performance
topic: evals-observability
subtopic: evaluation
secondary_topics:
- models/benchmarks
summary: Defines five pillars of AI model performance and how to measure quality beyond
  a single aggregate benchmark score.
source: braintrust
url: https://www.braintrust.dev/blog/model-measurement
author: Braintrust Team
published: '2026-02-12'
fetched: '2026-07-11T04:33:03Z'
classifier: codex
taxonomy_rev: 1
words: 2724
content_sha256: be5d047c6e7a4d48303672eb67cd1956b8cff207a5472f972a69d40783a7a29b
---

# The 5 pillars of AI model performance

12 February 2026Jess Wang15 min

When a new model comes out, people use it and form an initial impression, like "the responses sound smarter" or "this feels faster than the previous model."

While subjective impressions are useful for quick assessments, they often miss important factors like variability across task types, reproducibility issues, and economic costs at scale. As models develop increasingly nuanced differences in reasoning style, tool use, and context handling, the industry needs more standardized and rigorous methods of measurement.

And although published benchmarks accompany a model release, they don't quite capture the nuance necessary. Let's walk through the five pillars of model evaluation, and analyze how [Claude Opus 4.6](https://www.anthropic.com/news/claude-opus-4-6) and [GPT-5.3-Codex](https://openai.com/index/introducing-gpt-5-3-codex/) perform across each pillar based on their respective published benchmarks.

These benchmarks have become the industry standard for model releases. Every major lab, including [Anthropic](https://www.anthropic.com), [OpenAI](https://www.openai.com), [Google](https://deepmind.google), and even open-source projects like [DeepSeek](https://www.deepseek.com), publishes these scores. They measure long-horizon autonomy within terminal and OS environments.

** SWE-bench Pro** tests multi-file software engineering by giving models real-world GitHub issues to resolve. The dataset includes bug fixes and feature requests that require understanding existing codebases, coordinating changes across multiple files, and writing code that actually works when you run it. Success is measured by resolve rate. Did the model's patch actually fix the issue without breaking anything else?

For example, the dataset includes [Django issue #34612](https://code.djangoproject.com/ticket/34612): "QuerySet.only() doesn't work with select_related() on a reverse OneToOneField relation."

The original [SWE-bench Verified](https://www.swebench.com), which used to be quite popular, had limitations, which is why more developers are switching to SWE-bench Pro. SWE-bench Verified was Python-only, contained a smaller set of issues (500 vs. 2,294), and some problems leaked into training data. SWE-bench Pro expanded language coverage to include JavaScript, TypeScript, Go, and Java, making it a more realistic proxy for production engineering work.

** Terminal-bench 2.0** evaluates command-line proficiency across admin and data tasks. Models are given terminal access and asked to complete tasks like setting up databases, debugging failed deployments, or processing log files. The benchmark tracks success rate on tasks that require chaining multiple commands, understanding error messages, and course-correcting when something fails.

For example, "Build Linux kernel 6.9 from source, add a custom printk message to start_kernel, generate the ramfs with gen_init_cpio, and run it in QEMU."

This test matters more now because the industry is shifting toward terminal-first agentic tools. [Warp](https://www.warp.dev/) and [Claude Code](https://docs.anthropic.com/en/docs/claude-code) both rely on CLI execution loops rather than GUI-based interactions.

** OSWorld Verified** measures cross-application navigation in desktop environments. Models must complete tasks that span multiple applications, testing whether they can use a computer the way a human would rather than writing code in isolation.

For example, "Make a duplicate of the last two slides for me, please" (with a LibreOffice Impress file already open), or "Fill all the blank cells in B1:E30 with the value in the cell above it" (in LibreOffice Calc). Success requires navigating GUI elements, understanding context, and completing the workflow without human intervention.

Domain-specific benchmarks test deep reasoning within highly specialized professional, scientific, and technical domains.

** GDPval-AA** tests economically valuable knowledge work by simulating 44 professional occupations across 9 major industries. The dataset includes 220 real tasks like drafting legal briefs, analyzing financial statements, and conducting literature reviews. Models are given shell access and web browsing capabilities in an agentic loop, and are ranked using an

For example, tasks require models to produce diverse outputs including documents, slides, diagrams, and spreadsheets mirroring actual work products across finance, healthcare, legal, and other professional domains.

** Humanity's Last Exam (HLE)** evaluates multidisciplinary reasoning with 2,500 expert-vetted questions spanning mathematics (41%), physics (9%), biology/medicine (11%), humanities/social science (9%), computer science/AI (10%), engineering (4%), chemistry (7%), and other subjects (9%). The questions are designed to be hard enough that they push the limits of current AI capabilities (hence the somewhat dramatic name).

**Life sciences:** [BioBench](https://arxiv.org/abs/2511.16315), [BioProBench](https://arxiv.org/abs/2505.07889), and benchmarks for phylogenetics and organic chemistry. These test ecological vision tasks, biological protocol understanding, evolutionary tree analysis, and spectroscopy/synthetic design.

For example, BioBench tasks include identifying individual beluga whales from photographs and classifying species from drone footage, camera-trap frames, and microscope micrographs across 3.1M images.

** SWE-bench Multilingual** evaluates software engineering capabilities across multiple programming languages including JavaScript, TypeScript, Go, Java, and Python. This tests whether models can apply coding knowledge consistently across different language ecosystems.

For example, the model receives a TypeScript issue about type inference failures in a React component, requiring understanding of TypeScript's type system, React's component lifecycle, and how generic constraints interact with JSX syntax.

** OpenRCA** (Root Cause Analysis) measures whether models can diagnose complex software failures from enterprise systems. The benchmark includes 335 failures from Telecom, Bank, and Market systems, along with over 68 GB of telemetry data. Models must identify the root cause that triggered the failure.

** CVE-Bench** measures cybersecurity vulnerability exploitation capabilities using 40 critical-severity CVEs from the National Vulnerability Database.

For example, CVE-2024-4223 involves a content management system that allows attackers to execute arbitrary SQL queries via a specific endpoint. The model must identify and exploit the vulnerability to achieve goals like database access, privilege escalation, or denial of service.

Measuring speed and cost for LLMs is inherently difficult because performance varies based on context length, caching, concurrent requests, and hardware configuration. The following frameworks provide structured approaches to measuring these variable factors:

** MRCR v2 (Needle-in-a-Haystack)** tests long-context retrieval by burying specific pieces of information across massive amounts of text (up to 1M tokens). Models must locate specific details without hallucinating or losing track of information as document size grows. This benchmark directly measures "context rot," the performance degradation that occurs when conversations exceed a certain length.

The classic test inserts a statement like "The best thing to do in San Francisco is eat a sandwich and sit in Dolores Park on a sunny day" at various depths within long documents, then asks the model to retrieve this specific fact.

** Vending-Bench** evaluates long-term coherence by testing whether models can maintain focus and decision quality over extended agentic sessions.

For example, the model is given a multi-step task like "research competitor pricing, update the product database, generate a summary report, and schedule follow-up tasks" over a 4-hour session. Success requires maintaining context across dozens of subtasks without forgetting earlier instructions or drifting off-topic.

** BrowseComp** measures agentic web search capabilities by testing models' ability to locate hard-to-find, entangled information across the internet.

For example: "Which Nobel Prize winner in Chemistry published a paper with someone who later became a CEO of a Fortune 500 pharmaceutical company?" This requires cross-referencing academic publications with corporate biographies and synthesizing information from disparate sources.

**Inference speed** is the number of tokens generated per second. Faster generation means shorter wait times and higher throughput for systems using these models.

**Tool call efficiency** is the success rate of programmatic calls to external tools, APIs, or system commands. This measures how reliably a model can integrate with real-world software infrastructure.

**Cost-per-patch** is the total expense to resolve a single issue, including the cost of reruns and failed attempts. This metric provides the most accurate economic indicator for enterprise budgeting.

The industry-standard benchmarks we defined above can lag behind real-world needs. They may not update quickly enough to capture new model capabilities, or they may be too generic to reflect the specific workflows developers care about. As a result, developers often create custom benchmarks that reveal performance characteristics that standard benchmarks miss.

For example, one developer ran a [structured comparison](https://www.reddit.com/r/codex/comments/1qwwtri/gpt52_high_vs_gpt53codex_high_realworld/) between GPT-5.2 High and GPT-5.3-Codex High on a real SaaS codebase.

-
**Debugging/runbook reasoning:**Can the model produce a deterministic checklist for intermittent auth issues, distinguishing issues like CORS errors, gateway failures, cookie collisions, and infra cold starts?
-
**Reality mapping:**Can the model describe what actually works end-to-end today, versus what's scaffolded or mocked? Models often describe the product you want, not the product the code implements.
-
**Strategy and positioning under constraints:**Can the model write positioning that's true given current capabilities, then propose a minimal roadmap slice to make the positioning truer?
-
**Roadmap slicing:**Can the model pick the smallest 2-week slice to code two features truly end-to-end?

GPT-5.3-Codex was faster and better at structured checklists, but occasionally cited files that did not exist. GPT-5.2 High was slower but more reliable for "don't break prod" engineering work, with better evidence hygiene and more implementable plans.

This is just one example of a community-defined eval, and the code isn't public, but it illustrates a way of breaking down model performance that traditional benchmarks don't capture.

Despite the limitations of subjective impressions at scale, anecdotal evaluation still has value when applied with structure. One effective approach is characterizing models by the distinct cognitive roles they excel at:

- The **architect**excels at high-level planning and architectural decision-making.
- The **implementor**focuses on speed and execution quality.
- The **debugger**identifies root causes of failures and traces issues across codebases without introducing regressions.
- The **reviewer**audits code for bugs and provides actionable feedback without rewriting entire implementations.
- The **researcher**navigates documentation, searches codebases, and synthesizes information to answer technical questions.

This list is not exhaustive, but it provides a useful framework for matching models to workflows. For example, many developers cast GPT-5.2 as the architect (better evidence hygiene, clearer reasoning) and GPT-5.3-Codex as the implementor (faster execution, stronger terminal proficiency).

Based solely on [Anthropic's launch article](https://www.anthropic.com/news/claude-opus-4-6), here is how Opus 4.6 performs across the five pillars:

-
**Complex agentic task execution:**Scored 65.4% on[Terminal-Bench 2.0](https://www.tbench.ai/), 72.7% on[OSWorld](https://os-world.github.io), and 80.8% on[SWE-bench Verified](https://www.swebench.com).
-
**Domain-specific:**Achieved 1606 Elo on[GDPval-AA](https://artificialanalysis.ai/evaluations/gdpval-aa), 53.1% on[Humanity's Last Exam](https://agi.safe.ai/)with tools, 91.3% on[GPQA Diamond](https://arxiv.org/abs/2311.12022), and 2× improvement on life sciences benchmarks. Scored 84.0% on BrowseComp for agentic web search.
-
**Operational:**Introduced a 1M-token context window that addresses context rot. Achieved 76% on[MRCR v2 (Needle-in-a-Haystack)](https://github.com/gkamradt/LLMTest_NeedleInAHaystack)long-context retrieval at 1M tokens. Pricing remains at $5/$25 per million tokens. Anthropic did not publish inference speed data.
-
**Community-defined:**Not mentioned in the launch article.
-
**Anecdotal:**Not addressed in the launch article, though Anthropic emphasized adaptive thinking and agent teams features.

Based solely on [OpenAI's launch article](https://openai.com/index/introducing-gpt-5-3-codex/), here is how GPT-5.3-Codex performs across the five pillars:

-
**Complex agentic task execution:**Achieved 77.3% on[Terminal-Bench 2.0](https://www.tbench.ai/), 64.7% on[OSWorld-Verified](https://os-world.github.io), and 56.8% on[SWE-Bench Pro Public](https://www.swebench.com).
-
**Domain-specific:**First model classified as "High capability" for cybersecurity under OpenAI's[Preparedness Framework](https://openai.com/preparedness/), backed by $10M cyber defense commitment. The launch article did not include data on GDPval, Humanity's Last Exam, or life sciences benchmarks.
-
**Operational:**OpenAI did not publish benchmarks, but reported using early versions of the model to debug its own training runs, identify context rendering bugs, and dynamically scale GPU clusters. Delivers 25% faster inference than GPT-5.2 via[NVIDIA GB200 NVL72](https://www.nvidia.com/en-us/data-center/gb200-nvl72/)optimizations. OpenAI did not publish API pricing, tool call efficiency, or long-context retrieval data.
-
**Community-defined:**Not mentioned in the launch article.
-
**Anecdotal:**Not addressed in the launch article, though OpenAI emphasized that GPT-5.3 Codex was "instrumental in creating itself" and highlighted its self-bootstrapping capabilities.

| Feature | Opus 4.6 (Anthropic) | GPT-5.3-Codex (OpenAI) |
|---|---|---|
| Agentic Computer Use | 72.7% (OSWorld) | 64.7% (OSWorld-Verified) |
| Terminal Coding | 65.4% (Terminal-bench 2.0) | 77.3% (Terminal-bench 2.0) |
| SWE-bench | 80.8% (Verified) | 56.8% (Pro Public)* |
| Reasoning (HLE) | 53.1% (with tools) | Not reported |
| GDPval | 1606 Elo | Not reported |
| Context Window | 1M Tokens (76% retrieval) | 400k Tokens (reported) |
| Inference Speed | Not reported | 25% faster than GPT-5.2 |
| Domain Sciences | 2× improvement in life sciences | First "High" cybersecurity capability |

OSWorld and OSWorld-Verified are different benchmark variants and are not directly comparable. OSWorld-Verified uses a subset of tasks with human-verified success criteria, while OSWorld includes the full task set. SWE-bench Verified and SWE-bench Pro Public are also different variants. SWE-bench Pro Public contains more challenging, multi-file problems across multiple programming languages, which may account for the lower score.

The model release articles reveal as much about each company's strategy as the models themselves.

Anthropic's announcement reads like an academic paper. The [Opus 4.6 release](https://www.anthropic.com/news/claude-opus-4-6) leads with benchmark scores: Terminal-Bench 2.0, GDPval-AA, Humanity's Last Exam, MRCR v2, life sciences performance. Every claim connects to a measurement. The article includes detailed charts showing Opus 4.6 outperforming competitors across reasoning, coding, multilingual tasks, cybersecurity, and long-term coherence. Anthropic dedicates sections to root cause analysis, long-context retrieval, and safety evaluations. The message here is clear: trust the data.

OpenAI's approach centers on use cases. The [GPT-5.3-Codex announcement](https://openai.com/index/introducing-gpt-5-3-codex/) features testimonials, project examples, and workflow integrations. You see screenshots of financial advice slides, retail training documents, analysis spreadsheets, fashion presentations, and a racing game built with Codex. The article emphasizes what developers built with the model, not just how it scored. When OpenAI does cite benchmarks (Terminal-Bench, OSWorld, SWE-Bench Pro), they frame them around developer workflows: "GPT-5.3-Codex helps you build things."

This contrast is probably strategic. Anthropic targets technical decision-makers who need quantitative justification for model selection. Their heavy benchmark focus addresses enterprise buyers asking: "Can you prove this model is better?" The emphasis on life sciences, finance, and legal benchmarks speaks directly to regulated industries that require documented performance improvements.

OpenAI targets developers who want to ship products. Their testimonial-heavy approach addresses the question: "What can I build with this?" By showcasing completed projects like games, financial tools, and presentations, OpenAI demonstrates versatility over specialization.

What's missing from each article is also revealing. Anthropic barely mentions pricing or API access details, focusing instead on technical superiority. OpenAI skips entire benchmark categories: no life sciences scores, limited reasoning benchmarks, minimal discussion of long-context performance. These omissions are choices that reflect different theories of what developers care about when choosing a model.

Benchmarks only tell part of the story. What matters most is the practical experience of using these models. Here is what developers testing both models in production have shared on Reddit, Hacker News, and Twitter:

-
"Both of these releases feel like the companies pushing for capabilities and speed of execution, but at the cost of some ease of use. I've found both Opus 4.6 and Codex 5.3 ignoring instructions if I queue up multiple things to do. Benchmark-based release reactions barely matter anymore. For this release, I barely looked at the evaluation scores. If I'm going to recommend a coding agent to an audience with limited software experience, it's certainly going to be Claude." - [Nathan Lambert, Interconnects](https://www.interconnects.ai/p/opus-46-vs-codex-53)
-
"With Codex (5.3), the framing is an interactive collaborator: you steer it mid-execution, stay in the loop, course-correct as it works. With Opus 4.6, the emphasis is the opposite: a more autonomous, agentic, thoughtful system that plans deeply, runs longer, and asks less of the human." - [Hacker News discussion](https://news.ycombinator.com/item?id=46902638)
-
"Opus 4.6 has a higher ceiling as a model, but it also has higher variance. It's more parallelized by default and more creative. But Opus also sometimes reports success when it's actually failed, or makes changes you didn't ask for." - [Every.to internal testing](https://every.to/vibe-check/codex-vs-opus)
-
"Codex is a game changer for debugging. It automatically runs tests, catches edge cases I miss, and fixes bugs in seconds. Multiple threads confirm: Codex excels at single-problem focus." - [Reddit r/LocalLLaMA community](https://www.reddit.com/r/LocalLLaMA/)
-
"Better at architectural analysis. I feed it my entire repo, and it suggests refactoring patterns I wouldn't have considered. That 1M token context window isn't marketing. It's a structural advantage for complex, multi-file problems." - [Reddit discussion on Opus 4.6](https://www.reddit.com/r/ClaudeAI/)
-
"Claude's Max plan is significantly more expensive than Codex's Pro plan ($100 vs. $20)." - [Latent Space AINews](https://www.latent.space/p/ainews-sam-altmans-ai-combinator)community discussion
-
"The Twitter clone built by Claude was noticeably better. Codex did manage to create a sidebar panel, but it had missing images and felt incomplete, whereas Claude's version looked far more polished and production-ready." - [Analytics Vidhya hands-on testing](https://www.analyticsvidhya.com/blog/2026/02/claude-opus-4-6-vs-openai-codex-5-3/)

No single benchmark tells the whole story, and no single model wins everywhere. Use the five pillars to get a sense of what makes a model useful in practice, and avoid relying on any one measurement. Pay attention to what the benchmarks measure and what they miss.

If public benchmarks don't capture your specific use case, consider running custom evals with tools like [Braintrust](https://www.braintrust.dev/). The five pillars provide a framework for structuring your own evaluations.

And remember that the best model for your use case depends on the specific tasks you need it to do, not on which one topped the leaderboard this week.
