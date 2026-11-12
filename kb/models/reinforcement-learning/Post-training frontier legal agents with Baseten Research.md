---
title: Post-training frontier legal agents with Baseten Research
kind: blog
topic: models
subtopic: reinforcement-learning
secondary_topics:
- agents/harness
summary: Baseten Research post-trained a 27B open-weight model with a legal-agent
  harness in the loop against Harvey's Legal Agent Benchmark (1200+ tasks, 24 practice
  areas), bringing it into the closed-source frontier band where even top closed models
  complete under 10% of tasks end-to-end at ~$50/task.
triage: null
skip_reason: null
source: baseten
url: https://www.baseten.co/blog/post-training-frontier-legal-agents-with-baseten-research
author: Charles O'Neill
published: '2026-05-27'
fetched: '2026-11-12T06:15:50Z'
classifier: claude
taxonomy_rev: 2
words: 1780
content_sha256: 707e8aff7d9a57fa0f1ac45d21621240fbaf017743264706b3e0330423dd1bb5
---

# Post-training frontier legal agents with Baseten Research

Research
# Post-training frontier legal agents with Harvey

Post-training a 27B open-weight model to the frontier on Harvey LAB with Baseten Research


- Authors
- Date
- May 27, 2026

Harvey's [Legal Agent Benchmark (LAB)](https://www.harvey.ai/blog/introducing-harveys-legal-agent-benchmark) was designed with two purposes in mind: (1) to provide a public, shared evaluation for how AI agents perform on real legal work, and (2) to serve as a foundation for research that pushes long-horizon legal-agent capabilities forward.

Of the core areas of agent research, post-training is one of the most promising directions for specialized legal agents, as it simultaneously addresses three key challenges faced by vertical applications:

- **Domain expertise**: Long-horizon legal work requires a breadth of domain-specific skills, including research (retrieval and search across the closed-universe matter), analysis (reasoning and structured outputs), and drafting (well-formatted, reviewable documents). [Our recent results](https://www.harvey.ai/blog/legal-agent-benchmark-initial-results#:~:text=Legal%20Agent%20Performance) for closed-source foundation models suggests that agents still have a meaningful capability gap on this work, with even the strongest frontier models completing less than 10% of tasks end-to-end.
- **Cost**: Frontier intelligence is expensive to run. On LAB, reaching the top of the closed-source leaderboard runs to roughly [$50 per task and over 20 minutes of latency](https://www.harvey.ai/blog/legal-agent-benchmark-initial-results#:~:text=the%20start.%E2%80%9D-,Cost%20and%20Latency,-For%20production%20agents). For production legal agents, quality only matters if it fits inside the cost and latency budgets customers can tolerate.
- **Governance**: Post-training creates a path toward more secure and interpretable agent systems, as open-weight models can be hosted within a firm's own secure cloud environment and enable deeper auditability through full visibility into the model's reasoning traces, tool calls, and intermediate decisions.

Despite success in domains like coding, however, post-training in legal settings has been challenging, in large part due to the private nature of legal data – legal is one of the highest-stakes, sensitive forms of knowledge work. With LAB, and its comprehensive taxonomy of over 1200 tasks spanning 24 legal practice areas, there is now an opportunity to meaningfully push on open weight model intelligence for legal tasks.

In this post, we outline our initial research and experiments towards open-weight legal agents. In collaboration with Baseten Research, we built a pipeline that takes LAB signal, pairs it with a legal-agent harness designed for long-horizon legal work, and post-trains an open-weight model with that harness in the loop. Using that pipeline, we post-trained a 27B open-weight model, bringing it into the closed-source frontier band on LAB.

The results point to a broader conclusion that post-training and harness optimization need to be developed together. They also open directions worth pursuing next, including richer, less lossy compaction strategies and using compaction artifacts as anchors for partial-credit assignment in long-horizon RL.

LAB tasks are constructed to mirror real legal work. Each task starts from a partner-style instruction, places the agent inside a closed-universe client matter of documents, and requires it to produce a reviewable legal work product. Every task is paired with an expert-written rubric and performance is measured and performance is measured following our standard all-pass grading.

For our experiments, we leveraged the public LAB tasks and created a hold out test set that has a similar distribution to the training set. As a starting point, we baselined both open weight and closed foundation models on the hold-out. On these baselines, Sonnet 4.6, Opus 4.7, GPT 5.5 lead, with GLM 5.1 and DeepSeek v4 mixed in among them. Below them are the rest of the popular open-weight models.

Before any training, we started by looking at how the strongest models on LAB research including retrieval and search.

[As our initial public results showed](https://www.harvey.ai/blog/legal-agent-benchmark-initial-results#:~:text=a%20draft.%E2%80%9D-,Behavioral%20Analysis,-The%20way%20an), Opus, Sonnet and GPT-5.5 were comprehensive in their research. They opened most documents in the data room and read them in full, often approaching 90% document coverage. The weaker open-weight models did the opposite, they leaned on the grep tool to surface specific passages and rarely read documents end-to-end.

We wanted to see whether the same strategy would emerge when a model was trained end-to-end against the LAB rubrics. We ran a light RL pass on Qwen3.5-9B using GRPO. Reward came exclusively from the LAB rubric, with no retrieval-specific signal.

After 40 steps (Figure 2), the criterion pass rate rose from 42.5% to 63.0% on the hold out test data. Importantly, the model's behavior shifted as the score rose. `grep` calls dropped by 67%, the read tool became dominant, and characters read per rollout rose by over 20%. Trained against the LAB criteria, the small model converged on the same strategy as Opus, Sonnet and GPT-5.5.

One caveat: when documents follow a fixed form, targeted retrieval can match or exceed read-everything because the model can use the structure to separate signal from a noise for a given client matter. This matters for firm-specific post-training, where the document mix inside a client matter might be narrower and more predictable. We are researching alternative approaches for when this pattern holds.

If reading everything is an effective strategy, the question is how to scale that strategy to arbitrarily large client matters. Real client matters often contain hundreds or thousands of contracts and supporting materials, much of it peripheral to any given task. A common answer to this is compaction — periodically compressing the trajectory into a summary so the agent can keep reading.

In order to validate this hypothesis, we implemented a naive natural-language compaction strategy and benchmarked. The agent reads one document per turn in full. Every few reads, it writes a natural language memo to its working directory. The memo is a structured note capturing the facts it has surfaced, the open questions, and any provisional judgements it has reached. The memo replaces the prior chat history, and the agent continues reading.

The harness lifted average criterion pass rate by 5–7 points. The all pass rate - the share of matters where every criterion passes - rose more steeply, 2.6x for Sonnet and 3.7x for GPT-5.5. The all-pass rate is the one that maps to real legal review. A deliverable that misses a single issue can be materially incomplete, and partial correctness counts as a failure.

The same compaction harness gave Qwen3.5-27B minimal lift. Our hypothesis after looking at the data was the compaction mechanics were not the bottleneck. Qwen3.5-27B struggled with writing a memo that captured the reasoning and facts that matter for the task. Frontier closed models can write a useful memo on their own with the harness just unlocking it. Qwen3.5-27B needed the combination of the harness that captures the right strategy, and post-training that teaches the model to execute it.

We post-trained Qwen3.5-27B using [Iterative SFT](https://www.baseten.co/research/iterative-sft/) (iSFT) to be better in this natural-language compaction harness.

Training data for iSFT came from teachers running each task end-to-end inside the harness, with privileged access to the rubric, until they produced a fully-passing deliverable.

Because the training data was filtered to rubric-passing rollouts, post-training lifts the model on both capabilities the intro called out (i) retrieval, where the model learns to use the compaction harness fluently, and (ii) analysis with reasoning, where it learns to produce passing deliverables from the compacted context.

The main challenge was what to do with imperfect first-pass rollouts. Discarding them wastes signal, but two of the obvious recovery paths also have issues. Feeding the teacher more privileged information, like the expected answer or additional hints, pushes the data off-policy. Each unit of extra information the teacher relies on is a unit the student will never have at inference. Surfacing the judge's feedback to the teacher fails for the same kind of reason from the other end. The model learns to respond to a grader that won't be there. We resolved both with what we call a private-mode submit. When a rollout falls short, the teacher gets a chance to notice the gap itself, in its own voice, with no trace of where the correction came from.

The other choice was matching the training shape to inference. A trajectory might span hundreds of thousands of tokens, but at inference the model only ever sees one compacted window at a time. We trained per-window, with the loss shaped to teach the model to act in the harness, not to predict it.

The above memo-based compaction harness has a structural ceiling. The natural-language summary is relatively lossy. This worked well enough at the scale of the matters we tested, but it caps what compaction can preserve, and on the hardest long-horizon matters the residual losses compound.

The number of bits stored in a textual summary is very small relative to the rich internal representations in a model’s KV cache. In order to get around this information bottleneck, Baseten has developed a [novel technique](https://www.baseten.co/research/towards-infinite-context-windows-neural-kv-cache-compaction/), STILL, for directly compressing the KV cache. Given a frozen base model with $L$ layers, $h$ KV-heads per layer, and head dimension $d$, the per-layer cache for a $T$-token prefix has the form $K^{(\ell, h)}, V^{(\ell, h)} \in \mathbb{R}^{T \times d}$. Baseten trains a per-layer compactor

$$
g^{(\ell)}\phi : (K^{(\ell,h)}, V^{(\ell,h)})_{h=1}^{H} \;\longmapsto\; (C_k^{(\ell,h)}, C_v^{(\ell,h)})_{h=1}^{H}
$$

with compact keys and values $C_k^{(\ell,h)}, C_v^{(\ell,h)} \in \mathbb{R}^{t \times d}$ and $t \ll T$. Internally, each $g^{(\ell)}_\phi$ uses cross attention to a bank of $t$ learned latent queries and projects out to a set of compact keys and values via two linear heads. This compactor is trained without requiring any alterations to the base model itself; we can apply this compaction strategy to any pre-trained open source model.

Two properties make this the right shape for long-horizon legal work. Text-based summaries work by discarding irrelevant information. Therefore, when a task genuinely requires knowledge of a very large amount of factual details, it is simply impossible to achieve high compression ratios with text based summaries. This kind of task is very common in legal domains where numerous clauses and specific facts many play a pivotal role in the successful completion of the task. By making use of superposition in the latent space of a compressed KV cache, we are able to store exponentially more information. Secondly, by training the KV compression module in this specific domain, we are able to learn to distinguish important information from irrelevant details. Both of these factors can combine to unlock a fundamental discontinuity in capabilities that would not be possible with purely text based summaries.

A 27B open-weight model landing in the closed-source frontier on LAB is base camp. Post-training research and harness optimisations without the high quality LAB data would not have yielded the same performance. The climb ahead includes research directions around less lossy compaction in KV cache space, using compaction artifacts as anchors for partial-credit assignment in long-horizon RL, and closing the reasoning capability gap that retrieval alone doesn't address. It is is a much bigger lift than this one post, more to come.
