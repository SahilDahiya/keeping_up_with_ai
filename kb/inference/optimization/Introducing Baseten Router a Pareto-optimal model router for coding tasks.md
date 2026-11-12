---
title: 'Introducing Baseten Router: a Pareto-optimal model router for coding tasks'
kind: blog
topic: inference
subtopic: optimization
secondary_topics:
- infra-platform/cost
summary: Explains Baseten Router, a learned router that sends each coding task to
  an open- or closed-weight model (e.g. GLM 5.3 Flash vs Opus 5.5) based on expected
  cost/performance, reaching within 0.8 points of Opus 5.5's pass rate at 72% lower
  cost on DeepSWE/SWE-Atlas/Terminal-Bench test sets.
triage: null
skip_reason: null
source: baseten
url: https://www.baseten.co/blog/introducing-baseten-router
author: Guillaume Troadec
published: '2026-11-04'
fetched: '2026-11-12T06:07:06Z'
classifier: claude
taxonomy_rev: 2
words: 2714
content_sha256: f8b5e87ffa40031ef5bc16ecf02c1d95d61c59e2c8d273dd218bb19f86128fe2
---

# Introducing Baseten Router: a Pareto-optimal model router for coding tasks

Product
# Introducing Baseten Router: a Pareto-optimal model router for coding tasks

Baseten Router picks the right model per coding task, within 0.8 pts of Opus 5.5’s pass rate at 72% lower cost. Now in public preview on Baseten Grid.


- Authors
- Date
- November 4, 2026

TLDR

Baseten Router sends each coding task to the right model, open or closed, so you pay frontier prices only when the task needs it. In benchmarks, it came within 0.8 percentage points of Opus 5.5 at 72% lower cost. It’s the only router we tested that beat random routing by a statistically significant margin. Baseten Router is part of Baseten Grid, now in public preview.

Today, we’re sharing our initial results from training an intelligent model router for Baseten Grid.

Not every coding task needs the most capable model. As AI coding spend continues to grow rapidly [\[1\]](https://menlovc.com/perspective/2025-the-state-of-generative-ai-in-the-enterprise/) and cheaper open-weight models close the capability gap [\[2\]](https://epoch.ai/data-insights/open-closed-eci-gap), choosing the right model for each task becomes increasingly valuable. Baseten Router chooses between models based on their expected performance and cost for each coding task. The goal is frontier performance while paying frontier prices only when the task calls for it.

Baseten Router cuts costs by 72% compared to using Opus 5.5 for every task while remaining within 0.8 percentage points of its pass rate, measured on a test set spanning DeepSWE, SWE Atlas QnA, and Terminal-Bench. Adjusting the routing threshold lets users choose various trade-offs along the cost-performance Pareto frontier.

We’re working closely with design partners to specialize Baseten Router for their production coding workloads and prove out performance in the real world. Early feedback is promising, and we will share those results soon.

Almost everyone at Opendoor uses AI, and most people don’t want an opinion on which model to pick. Auto routing sends them to the right model automatically, so they stay fully empowered and we stop paying frontier prices for work that doesn’t need it.


This post walks through how we built competitive performance into Baseten Router and how we continue to refine our approach.

From the input prompt, Baseten Router decides whether the coding task should be completed by a frontier closed-weight model or a cheaper open-weight model. In these experiments, we route between Opus 5.5 and GLM 5.3 Flash. We chose GLM 5.3 Flash because it is a strong coding model that is approximately 80% cheaper than Opus 5.5 across relevant workloads. Our approach can be extended to any model combination in any harness supported by [Baseten Grid](https://www.baseten.co/products/grid).

Our aim is to build a model router that decides between two models and gives a better trade-off between success rate and cost than either model alone. We formulated routing as choosing the model with the highest score, where the score is the predicted success rate minus a penalty proportional to the predicted cost:

$$
\pi_\lambda(x)=\arg\max_{m\in\{\text{Opus,GLM}\}}\ \hat p_m(x)-\lambda\,\hat c_m(x)
$$

For a given coding task $x$, $\hat p_m$ and $\hat c_m$ are learned predictions of model m’s success rate and cost in USD on the task, respectively, and $\lambda$ is a configurable weight that controls the trade-off. Intuitively, this favors Opus when its higher predicted success justifies its additional cost.

There are two distinct ways to evaluate a router: on coding benchmarks and in production. The router’s performance in production matters most to us and to customers: how much model routing reduces a team’s AI coding spend while preserving the quality of their engineering work.

However, it is challenging to compare results from online evaluations across routers. These tests involve different users and tasks, different definitions of task success, and different methods for calculating cost savings.

Coding benchmarks provide a controlled and transparent framework, enabling us to compare different routers on shared tasks with clear success criteria and cost calculations. Additionally, we believe that the expertise needed to develop a good router on benchmarks is a subset of the expertise needed to perform well in production. Consequently, we view strong performance on coding benchmarks as an important milestone toward deploying in production.

By being methodical about data quality, quantifying noise, and comparing against meaningful baselines, we have built confidence in Baseten Router’s capabilities as we bring it to our customers’ production workloads.

To train Baseten Router, we generated traces on verifiable coding tasks. We built the training set from public coding datasets spanning bug fixes, feature implementation, codebase question answering, and terminal tasks. For each task, we ran both Opus 5.5 and GLM 5.3 Flash at high reasoning effort and recorded the verifier output and model cost.

To evaluate generalization beyond the training set, we used three benchmarks spanning long-horizon coding tasks (DeepSWE 1.1), codebase Q&A (SWE Atlas QnA), and terminal tasks (Terminal-Bench 2.1) as our test set. We selected these benchmarks because they cover categories highly relevant to production coding work and were included in Artificial Analysis's Coding Agent Index (v1.4) [\[6\]](https://artificialanalysis.ai/methodology/coding-agents-benchmarking) and OpenRouter's Router Benchmark (initial release) [\[7\]](https://openrouter.ai/blog/announcements/model-router-benchmarks/).

An underrated aspect of this process was cleaning the datasets. We corrected grader errors and broken task environments, added safeguards to prevent cheating, and removed training tasks with repositories present in the test set. Additionally, due to the non-deterministic nature of agentic coding, we quantified the uncertainty between repeats of the same task and repeated evaluation runs to improve the robustness of our results. We discuss this further below.

Benchmark results are noisy, meaning a router may perform well due to chance rather than genuine capability. To more rigorously control for this, we designed our evaluation to account for two sources of noise:

1. *Label noise:* The same model can pass the same task during one run and fail it during another.
2. *Selection noise:* A random router can route tasks, by chance, to GLM where it succeeds, making it seem more effective than it actually is.

Models in production are non-deterministic, meaning the same model can pass a task on one run and fail it on the next. Consequently, a single run is an uncertain measure of how hard a task is for that model. To quantify this uncertainty, we calculate a signal-to-noise ratio (SNR). The signal, $\tau^2$, measures how much the true gap between Opus’s and GLM’s pass rates varies from task to task. The noise, $\sigma^2_O$ and $\sigma^2_G$, measures how much each model’s results vary between attempts at the same task. Averaging $k_O$ Opus runs and $k_G$ GLM runs per task shrinks the noise according to the formula:

$$
\text{SNR} = \frac{\tau^2}{\sigma^2_O/k_O + \sigma^2_G/k_G}.
$$

The higher the SNR, the more precisely we can measure a router’s performance. With one run per model, the pooled test SNR was 0.27, meaning the test set had almost four times as much noise as signal. By running each test task four times with Opus and eight times with GLM, we raised the SNR to 1.51. This higher SNR makes it easier to distinguish a router that makes better decisions from one that is lucky.

Every test set pass rate mentioned in this blog post is an average over those runs.

To demonstrate that a router has actually learned useful signals, we must show that it beats random routing by more than chance.

A random router is defined as sending a random subset of tasks to GLM and the rest to Opus. Sending more tasks to GLM lowers both expected cost and expected pass rate, so on average every random router lands somewhere between always using Opus and always using GLM.

The figure below plots pass rate against average cost per task. Always using Opus 5.5 (top right) and always using GLM 5.3 Flash (bottom left) are the two ends of random routing. The dotted line between them is the average random router at each cost.

For each fraction of tasks sent to GLM, we simulate 10,000 random routers, each choosing a different random subset. The gray points are a sample of these routers. The gray band spans the middle 90% of their pass rates, from the 5th to the 95th percentile. We call a router’s performance statistically significant if it lies above the band: its pass rate beats 95% of random routers at the same cost.

Baseten Router’s problem formulation requires it to find signals in a task that predict the value of choosing one model over the other. This section describes the architectures we tested and how early results shaped our final approach. We compared experiments on the training set using leave-one-benchmark-out cross-validation.

We began by embedding the task instructions and fitting separate heads to predict each model’s probability of success and expected cost. Pre-trained embedding models, such as Qwen3-Embedding [\[8\]](https://arxiv.org/abs/2506.05176) and EmbeddingGemma 2 [\[9\]](https://huggingface.co/google/embeddinggemma-2), are a natural starting point: they capture semantic features of the task without needing to train a language model.

To understand which predictions mattered, we compared three routing setups: predicting success advantage alone, predicting expected cost alone, and predicting success advantage relative to expected cost. Routing on predicted cost alone captured most, but not all, of the initial router gains over random routing.

One hypothesis is that embeddings capture task scope, which is a clearer signal of cost than of which model will succeed. Subsequent analysis supported this: requirement count and estimated code diff size are strongly correlated with cost, but not with the gap in success rate between models.

Combining predictions for both success advantage and expected cost led to the best cross-validation results, so we kept that setup for later experiments.

Having established that the embedding router improved on random routing, we next explored which features were responsible for driving those gains. Some, such as the task category, are legitimate routing signals. For example, implementing a new feature and answering a question about a codebase have different success and cost profiles. However, embeddings can also capture cues specific to the benchmark a task belongs to. Relying on these cues risks learning shortcuts that do not transfer to new benchmarks or to production.

We trained a linear probe to test whether benchmark identity was encoded in the embeddings. This linear probe achieved 89% balanced accuracy, meaning benchmark identity was available as a routing shortcut. Next, we explored whether the embeddings captured useful task-level information. To route well within a category, a router must separate the tasks where a frontier model’s extra capability justifies its extra cost from the tasks where it does not. We found that tasks nearby in embedding space received similar routing scores, but the observed advantage of Opus over GLM on those tasks was only weakly correlated. This suggests that the naive embedding router struggles to learn meaningful representations necessary to distinguish tasks.

These findings motivated two directions: reducing benchmark-specific cues in the representation, and testing whether more explicit task characteristics provide additional routing signal. We tried multiple approaches, including rewriting prompts to strip out benchmark-specific cues, applying corrections to clusters of similar tasks, and extracting structured task attributes. Structured task attributes, such as a task's scope, the domain knowledge it requires, and its level of ambiguity, were particularly useful because they describe the work a task requires more explicitly. We subsequently explored using decision models, specifically [elephant-1 and mammoth-1 from Base Labs](https://www.baseten.co/blog/the-best-decision-models-in-the-world-mammoth-1-and-elephant-1/), to extract these attributes.

In parallel, we explored whether a model’s internal state contained useful routing information \[[10](https://arxiv.org/abs/2603.20895), [11](https://arxiv.org/abs/2602.09924), [12](https://arxiv.org/abs/2502.02013)\]. We ran GLM 5.3 Flash on each task without generating a response, captured its intermediate activations, and fitted a prediction head to estimate the number of steps in the subsequent response.

Intermediate activations predicted the number of agent steps with a Spearman correlation of approximately 0.6 on our validation set. The signal strengthened with depth, plateaued, and then declined in the deepest layers, consistent with findings in the literature [\[12\]](https://arxiv.org/abs/2502.02013). This supported using intermediate activations to estimate GLM's run length, and by extension its expected cost.

To reduce the router’s latency incurred by retrieving GLM 5.3 Flash’s internal activations, we explored various quantization techniques and the use of smaller Qwen models as proxies for GLM 5.3 Flash’s internal layers. This significantly reduced the router’s end-to-end latency while preserving routing performance.

Our final router combines the most useful signals from our experiments, including structured task attributes and internal model activations, to predict each model's success and expected cost.

We tested Baseten Router on three benchmarks held out from training - DeepSWE 1.1, SWE Atlas QnA, and Terminal-Bench 2.1 - and compared it with routers offered by other providers. The reported pass rate is an average over multiple runs for each task.

We observed strong generalization on the out-of-distribution test set. Baseten Router performs within 0.8 percentage points of Opus 5.5 at 72% lower cost, and every threshold setting lies on the Pareto frontier of pass rate against cost among the routers we tested.

Baseten Router lies above the gray band, which covers the middle 90% of random routers. This means it beats random routing by a statistically significant margin at every threshold. No other router we tested does so on this set of benchmarks.

Baseten Router offers a range of thresholds to configure where it lies on the Pareto frontier: Cost, Balanced, and Intelligence. These thresholds can be passed in at request time to the same router, without requiring any retraining.

We measured the end-to-end latency of our router across increasing levels of concurrency on a single B200 GPU deployment. At 4 concurrent requests, the p50 and p95 latencies were 273 ms and 429 ms, respectively. This sub-second overhead routing is small relative to a full coding-assistant turn, which typically takes tens of seconds [\[13\]](https://www.anthropic.com/research/measuring-agent-autonomy). We can easily scale up the deployment from a single B200 GPU if additional concurrency is required.

These results demonstrate Baseten Router’s strong performance on benchmarks selected before running any evaluations. There are also a few factors to keep in mind when interpreting the results.

First, router performance depends on the underlying training distribution and optimization objective. Although most other routers we evaluated also report results on coding benchmarks, they may target different workloads. Our results establish performance on specific benchmarks, which we believe are representative of real software engineering work. Relative router performance may differ on other benchmarks.

Second, model pools are not identical across routers. All but one router offered both Opus 5.5 and GLM 5.3 Flash. One router was limited to Anthropic models. Our comparison evaluates each router as offered, and model pool selection is a choice that forms part of the router being evaluated.

Our next focus is extending these gains from benchmarks to production. The two serve different purposes: benchmarks let us compare routers on the same tasks with the same success criteria, whereas production lets us measure cost savings and quality on real customer workloads.

Routing in production introduces three new challenges:

1. *Requests are less explicit.* A benchmark may describe a bug, identify the affected code, and explain how to reproduce it. In production, an engineer might simply write “fix this” and paste a stack trace.
2. *Success is harder to measure.* Benchmarks come with tests that verify whether a task was solved. A production task has no equivalent label, so training a router on production coding traces means deriving signals from the session, such as whether the user corrects the agent and whether the code is kept in subsequent turns [\[14\]](https://cursor.com/blog/how-cursor-router-works).
3. *Tasks are inherently multi-turn.* In a benchmark, the agent receives a single prompt and works until completion. In production, the user reviews the agent’s work, corrects it, and asks for more work in later turns. This means one session can contain several tasks of different difficulties. The best model can change mid-session, but switching models can mean reprocessing conversation context and forfeiting the benefits of a warm KV cache. Consequently, turn-level routers must weigh the benefit of a mid-session model switch against its additional cost.

We’re addressing these challenges by building training and evaluation environments specialized for production requests, a labeling pipeline that derives success signals from real coding traces, and policies for KV-cache-aware turn-level routing.

We’re also working with design partners to specialize Baseten Router to their coding workloads and extend the cost-quality gains from benchmarks into production. Our goal remains the same: frontier performance on every task, at frontier prices only when the task calls for it.

If you’d like to see what Baseten Router can do for your workloads, we’d love to talk.
