---
title: 'MiniMax M2.5: Intelligence too cheap to meter, RL process rewards, real-world
  productivity'
kind: blog
topic: models
subtopic: reinforcement-learning
secondary_topics: []
summary: Explains MiniMax M2.5's per-step process-reward mechanism (an update to the
  CISPO algorithm from the M1 paper) that addresses credit assignment in long agentic
  trajectories, reporting lower token consumption on SWE-Bench Verified (3.52M vs
  M2.1's 3.72M tokens).
triage: null
skip_reason: null
source: baseten
url: https://www.baseten.co/blog/minimax-m2-5-intelligence-too-cheap-to-meter-rl-process-rewards-real-world-produc
author: Alex Ker
published: '2026-02-13'
fetched: '2026-11-12T06:14:34Z'
classifier: claude
taxonomy_rev: 2
words: 913
content_sha256: c9eed4f1207e7751200048d3a5be6850218ab0005c4e79760024edf7d9de9421
---

# MiniMax M2.5: Intelligence too cheap to meter, RL process rewards, real-world productivity

AI models
# MiniMax M2.5: Intelligence too cheap to meter, RL process rewards, real-world productivity

RL behind MiniMax M2.5 and why it excels in knowledge work


- Authors
- Date
- February 13, 2026

When Andrej Karpathy aptly observed that "RL is like sucking supervision through a straw", he underscored perhaps the central shortcoming of traditional RL: using scalar final reward as the only feedback means potentially useful intermediate signals are discarded. MiniMax M2.5 circumvents this by designing a per-step process reward that is especially useful for long-running agentic trajectories, which we will explain intuitively in this post. Scaling reinforcement learning in an agent-native framework and updates in their previous algorithm allowed the team to reach SOTA benchmarks in coding, browser search and tool use, and showcased the model's ability to complete economically valuable tasks commonly found in office work.

We are excited to support [MiniMax M2.5](https://www.minimax.io/news/minimax-m25) on Model APIs here at Baseten today. Get started [here](https://app.baseten.co/model-apis/create?id=4w56vq2&_gl=1*g5fnl9*_gcl_aw*R0NMLjE3NzEyMDM0NTEuQ2p3S0NBaUEtc1hNQmhBT0Vpd0FHR3c2TE5FTThaaFRBQlgyWS1YSVN4NWRfcnJyY2VtRVluZEI2eG5ZRlJsdEpVY01OcGJoU05fTlF4b0NvQXNRQXZEX0J3RQ..*_gcl_au*MjUxNTU5MTU4LjE3NzA3NTYxNjQ.). This is a model every ML engineer should understand, and we will break down the most important results and parts that are the most useful to know.

Previous frontier MoE models focused on making output cheaper with architecture innovations, thereby allowing more test-time computation during inference to match the performance of closed-source leaders (e.g. DeepSeek Sparse Attention in DSV3.2). But this neglects the fact that real-world tasks value completion speed and efficiency, in addition to quality. M2.5 mitigated this with a reinforcement learning setup that encouraged optimal task decomposition and efficient reasoning (we will cover this in the next section). In SWE-Bench Verified, M2.5 consumed 3.52M tokens vs. M2.1 (previous version)'s 3.72M tokens. When token efficiency is paired with frontier inference performance, the result is a multiplicative effect on speed and a superior user experience.

Another downstream implication of improved speed and token efficiency: M2.5 is one-tenth to one-twentieth the price of Opus, Gemini 3 Pro, and GPT-5. Running M2.5 Lightning costs only $1 per hour at 100 TPS, and M2.5 Standard costs $0.3 per hour at 50 TPS on MiniMax’s endpoint. This means running four instances continuously for an entire year is only $10,000. With background agents and new harnesses such as OpenClaw/MoltBot that spin up parallel tasks, consuming from a closed-source model can rack up thousands per day. MiniMax M2.5 makes these agents much more efficient and affordable.

The MiniMax team updated the CISPO (Clipped Important Sampling Policy Optimization) introduced in the M1 paper, critically improving the credit assignment problem in long trajectories found in agentic workflows: it is unclear *which specific actions in* the trajectory lead to higher rewards. This is the same issue noted by Karpathy of missing intermediate signals. They address this with a process reward mechanism: **Placeholder: ContentMathRecord (inlineBlock)**{
  "node": {
    "type": "inlineBlock",
    "item": "OyNKifESROKJJvd1XEyG7g"
  },
  "record": {
    "\_\_typename": "ContentMathRecord",
    "id": "OyNKifESROKJJvd1XEyG7g",
    "formula": "Â\_{i,t}"
  }
}. To understand this term, let’s review what the advantage is.

The advantage in RL is the difference between the expected return from taking action *a* in state *s* and the expected return from the state *s* on average (across all actions). This tells you if the action from the state is above or below average. In the M2.5 process rewards, the estimated advantage for rollout *i* at token *t* is the sum of all future rewards from that position onward, minus a baseline for variance reduction. Crucially, each token position receives **a separate reward for speed and quality** (perf).

This lets the model independently optimize for speed and quality at *each step* in the trajectory. Because each token has its own reward signal, the model can for example learn that a good tool call at step 5 was valuable, even if the final output didn't arrive until step 50. Without this, every token in the trajectory would receive the same undifferentiated reward. In summary, the key innovation is in the advantage term **Placeholder: ContentMathRecord (inlineBlock)**{
  "node": {
    "type": "inlineBlock",
    "item": "VEB2Dh0ySveyhj9djjq7jw"
  },
  "record": {
    "\_\_typename": "ContentMathRecord",
    "id": "VEB2Dh0ySveyhj9djjq7jw",
    "formula": "Â\_{i,t}"
  }
}, which introduces per-token process rewards to solve credit assignment in long trajectories.

Most capable models still output raw text blocks, leaving a gap between generation and a polished deliverable in the desired format. Sarah Tavel's "[sell work, not software](https://www.sarahtavel.com/p/ai-startups-sell-work-not-software)" is a useful framework here: the output of the work itself is much more valuable than productivity improvements in the co-pilot model. M2.5 kept this in mind when pairing with senior professionals in finance, law, and social sciences, bringing their domain expertise into the training pipeline.

As a result, M2.5 was able to complete real-world tasks that require complex artifacts such as financial models and research reports — tasks that involve fetching data from external sources and applying specific user-requested logic. To test how generalizable the model is, M2.5's coding abilities were evaluated on out-of-distribution harnesses, exceeding Opus 4.6 on both Droid and OpenCode on the SWE-Bench Verified evaluation sets. On Droid: 79.7 (M2.5) > 78.9 (Opus 4.6). On OpenCode: 76.1 (M2.5) > 75.9 (Opus 4.6). Out-of-distribution performance matters because it shows the model isn't just fitted to specific benchmarks; it generalizes.

Open source is catching up to closed-source gold standards, while remaining orders of magnitude more cost efficient. For parallel coding and agentic tool-use tasks, M2.5 lets you explore many efficient pathways for solving a problem at a fraction of the cost of closed-source counterparts. Tasks in finance, law, and other fields that previously required multi-step workflows with expensive models can now be accomplished with M2.5.

Try MiniMax M2.5 on Baseten [here](https://app.baseten.co/model-apis/create?id=4w56vq2&_gl=1*g5fnl9*_gcl_aw*R0NMLjE3NzEyMDM0NTEuQ2p3S0NBaUEtc1hNQmhBT0Vpd0FHR3c2TE5FTThaaFRBQlgyWS1YSVN4NWRfcnJyY2VtRVluZEI2eG5ZRlJsdEpVY01OcGJoU05fTlF4b0NvQXNRQXZEX0J3RQ..*_gcl_au*MjUxNTU5MTU4LjE3NzA3NTYxNjQ.).
