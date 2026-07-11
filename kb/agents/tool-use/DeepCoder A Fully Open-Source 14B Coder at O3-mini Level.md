---
title: 'DeepCoder: A Fully Open-Source 14B Coder at O3-mini Level'
topic: agents
subtopic: tool-use
secondary_topics:
- models/fine-tuning
summary: Describes DeepCoder, an open-source coding model trained for O3-mini-level
  coding performance.
source: together
url: https://www.together.ai/blog/deepcoder
author: Michael Luo; Sijun Tan; Roy Huang; Ameen Patel; Alpay Ariyak; Qingyang Wu;
  Xiaoxiang Shi; Rachel Xin; Colin Cai; Maurice Weber; Ce Zhang; Li Erran Li; Raluca
  Ada Popa; Ion Stoica
published: '2025-04-08'
fetched: '2026-07-11T04:22:59Z'
classifier: codex
taxonomy_rev: 1
words: 2959
content_sha256: be3005759655c917f97c4ace58e348ec5f00dfb79b8d71abaa6f7f256f3a15aa
triage: keep
skip_reason: null
---

# DeepCoder: A Fully Open-Source 14B Coder at O3-mini Level

Through a joint collaboration between the [Agentica team](https://agentica-project.com/) and Together AI, we release **DeepCoder-14B-Preview**, a code reasoning model finetuned from **Deepseek-R1-Distilled-Qwen-14B** via distributed RL. It achieves an impressive **60.6% Pass@1** accuracy on [LiveCodeBench](https://livecodebench.github.io/) (**+8% improvement**), matching the performance of **o3-mini-2025-01-031 (Low)** and **o1-2024-12-17** with just **14B** parameters. We've **open-sourced **our dataset, code, training logs, and systems optimizations for everyone to progress on scaling and accelerating intelligence with RL.

## DeepCoder-14B-Preview

| Model | LCB (Pass@1) (8/1/24-2/1/25) | Codeforces Rating | Codeforces Percentile |
|---|---|---|---|
| DeepCoder-14B-Preview | 60.6 | 1936 | 95.3 |
| DeepSeek-R1-Distill-Qwen-14B | 53.0 | 1791 | 92.7 |
| O3-Mini-2025-1-31 (Low) | 60.9 | 1918 | 94.9 |
| O1-2024-12-17 (Low) | 59.5 | 1991 | 96.1 |

![__wf_reserved_inherit](https://cdn.prod.website-files.com/69654e88dce9154b5f12070c/699e0b016dcf395993e29c92_67f568a23eb76805e20a75df_livecodebench_16k_32k_scores(1).png)

In recent months, we've witnessed remarkable advances in scaling reasoning models for math domains (e.g. [DeepScaleR](https://www.notion.so/19681902c1468005bed8ca303013a4e2?pvs=21), [AReaL,](https://github.com/inclusionAI/AReaL/blob/main/blog/AReaL_v0_2.md) [Light-R1,](https://arxiv.org/abs/2503.10460) [DAPO](https://arxiv.org/abs/2503.14476)) via reinforcement learning. However, progress in the **coding** domain has lagged behind, largely due to the challenge of constructing high-quality datasets with reliable, verifiable rewards.

In this blog, we democratize the recipe for training a small model into a strong competitive coder—on-par with `o3-mini`—using reinforcement learning. We introduce `DeepCoder-14B-Preview`, trained on 24K verifiable coding problems over 2.5 weeks on 32 H100s, reaching—and even surpassing—OpenAI's `o3-mini` on various coding benchmarks. In addition, we open-source `verl-pipe`, an extension to the [verl](https://github.com/volcengine/verl) post-training system featuring several system optimizations that accelerate end-to-end training by **2x**.

### Dataset Curation

Prior work in the math domain has shown that reinforcement learning with **verifiable rewards** can significantly enhance a model's reasoning capabilities. However, unlike math—where abundant high-quality, verifiable data is readily available on the internet—the coding domain suffers from a relative scarcity of such data.

In our early experiments, we evaluated several popular coding datasets—including **APPS**, **TACO**, **CodeContests**, **KodCode**, and **LeetCode**. We found that some were too easy (e.g., KodCode, LeetCode) for our model, while others were noisy or contained unverifiable problems with flawed or missing test cases. These issues often produced null or misleading reward signals, which ultimately destabilize RL training.

To overcome these limitations, we curated a high-quality training set consisting of:

- **TACO Verified**problems.
- Verified problems from **PrimeIntellect's SYNTHETIC-1**dataset.
- **LiveCodeBench**problems submitted between- **May 1, 2023**and- **July 31, 2024**.

To ensure data quality for effective RL training, we implemented a rigorous filtering pipeline:

- **Programmatic Verification**: Every problem is automatically verified using an external, official solution. We filter our datasets to include only those problems whose official solutions pass all unit tests. This process is automated in- `tests/rewards/test_code_batch.py`.
- **Test Filtering:**Each problem must include at least 5 unit tests. We discovered that problems with fewer tests tend to encourage reward hacking, where the model learns to simply print out the memorized answer by recognizing common test cases.
- **Deduplication:**We remove duplicate problems across datasets to avoid contamination. We performed this for our three training datasets, namely- **Taco Verified**,- **PrimeIntellect SYNTHETIC-1**, and- **LCB**(05/01/23-07/31/24). Then, we verified that there is no contamination in the test datasets—- **LCB**(08/01/24-02/01/25) and 57 contests from- **Codeforces**.

After filtering, we are left with 24K high-quality coding problems that are used for our RL training, with 7.5K problems from **TACO Verified**, 16K problems from **PrimeIntellect's SYNTHETIC-1,** and 600 from **LiveCodeBench.**

### Code Sandbox Environment

To compute rewards for code RL training, we must run unit tests on model-generated code within coding sandboxes. During each RL iteration, our training batch is evaluated across 1024 problems—each featuring multiple unit tests (≥ 5 tests). This demanding workload requires scaling 100+ coding sandboxes to run in parallel, ensuring that LLMs' generated code is accurately verified within a reasonable amount of time. Currently, we utilize two sandboxes: the Together Code Interpreter and a Local code sandbox respectively.

**Together Code Interpreter**

A fast, efficient environment directly compatible with our RL training runs, costing only 3¢/problem. We've been working on reliably scaling the Together Code Interpreter to 100+ concurrent sandboxes and 1k+ sandbox executions per minute. These sandboxes expose `stdout`, `stdin`, and last line of code `output` evaluation while securely confining execution and isolating code from the host system. The Together Code Interpreter is currently in beta; details are available in the [Together Code Interpreter documentation](https://docs.together.ai/docs/together-code-interpreter) and sample code for integration can be found [in our code repo](https://github.com/agentica-project/rllm/blob/18e446c56f7af9a749ce1dd79ee85837a35ac1de/rllm/tools/code_tools/together_tool.py).

**Local Code Sandbox**

Launches a local sandbox as a separate, guard-railed Python subprocess that receives test case input via `stdin` and prints out the answer to `stdout`. Our local sandbox follows identical evaluation code from the official LiveCodeBench repo, ensuring that our results are consistent with existing leaderboards.

#### Reward Function

Our reward function employs a sparse Outcome Reward Model (ORM). We avoid assigning partial rewards, such as Chain-of-Thought penalty or assigning `K/N` reward if K out of N tests pass, which may lead to reward hacking, where the LLM learns to directly print out the answers of public tests or incorrectly converge on passing simple edge cases.

- `1`- The generated code must pass all- *sampled*unit tests. Since some problems contain hundreds of tests—making full verification impractical—we sample the 15 most challenging tests for each problem, identified by the length of their input strings.
- `0`- We assign no reward if the LLM's code fails on at least one test case or if the answer is formatted incorrectly (i.e. missing- `python [CODE]`). Each test case is assigned a timeout of 6-12 seconds.

### Training Recipe 🍽️

#### GRPO+: A Stable Version of GRPO

![__wf_reserved_inherit](https://cdn.prod.website-files.com/69654e88dce9154b5f12070c/699e0b016dcf395993e29c85_67f569108f3b548ac309c5e9_dapo_vs_grpo_rewards(1).png)

**Clip High**.

![__wf_reserved_inherit](https://cdn.prod.website-files.com/69654e88dce9154b5f12070c/699e0b016dcf395993e29c6e_67f5692153880dbddf1c93f8_grpo(1).png)

**overlong filtering**, GRPO+'s response length grow steadily over time.

![__wf_reserved_inherit](https://cdn.prod.website-files.com/69654e88dce9154b5f12070c/699e0b016dcf395993e29c88_67f56933641f2fa9c76a29d4_dapo_vs_grpo_entropy(1).png)

**Clip High**and

**No Entropy Loss**ensures that GRPO+'s token-level entropy does not collapse and encourages sufficient exploration.

We enhance the original GRPO algorithm integrating insights from [DAPO](https://arxiv.org/abs/2503.14476) to enable more stable training:

- **No Entropy Loss:**We observed that including an entropy loss term often led to instability, with entropy growing exponentially and ultimately collapsing training. To mitigate this, we eliminate the entropy loss entirely.
- **No KL Loss (from DAPO):**Eliminating KL loss prevents the LLM from being constrained to the trust region of the original SFT model. This removal also obviates the need to compute log probabilities for the reference policy, thereby accelerating training.
- **Overlong Filtering**- **(from DAPO):**To preserve long-context reasoning, we mask the loss for truncated sequences. This technique enables DeepCoder to generalize to 64K-context inference despite being trained with a 32K context. As shown in Figure 3, this filtering method allows response lengths to grow naturally without incurring penalties from truncation.
- **Clip High (from DAPO):**By increasing the upper bound in GRPO/PPO's surrogate loss, we encourage more exploration and stabilize entropy. Figure 4 demonstrates that this adjustment results in both more stable training and improved model performance.

#### Iterative Context Lengthening: Out-of-box Generalization

In our original [DeepScaleR](https://www.notion.so/DeepScaleR-Surpassing-O1-Preview-with-a-1-5B-Model-by-Scaling-RL-19681902c1468005bed8ca303013a4e2?pvs=21) blogpost, we introduced **iterative context lengthening**, a training technique that enables language models to first learn how to think effectively at shorter context lengths and then generalize to longer ones. This approach helped our 1.5B model steadily improve in downstream performance as we scaled its context window from **8K→16K→24K**, achieving **33%→38%→43%** accuracy on AIME and eventually reaching **O1-preview** performance.

When applying this technique to our 14B model, however, we encountered new challenges:

- The 14B model already possesses significantly stronger reasoning capabilities than the 1.5B model, meaning that further improvement requires solving **much harder problems**.
- These harder problems naturally require longer context windows than the 8K starting point used for the smaller model.

Starting with a short context and penalizing the model for exceeding that window had an adverse effect—it led to a drop in initial performance, shortened responses, and a degradation in the model's ability to reason over long contexts.

To preserve long-context reasoning while enabling efficient training, we incorporated **overlong filtering** from DAPO. This technique masks out truncated sequences during training so that models aren't penalized for generating thoughtful but lengthy outputs that exceed the current context limit. As a result, the model can still "think long" while training on a shorter context.

We applied iterative context lengthening to our `DeepCoder-14B-Preview`, scaling the context window from **16K→32K**. On **LiveCodeBench**, the model achieved:

- **54%→58%**accuracy at 16K and 32K respectively,
- and **60.6%**when evaluated at**64K**context, demonstrating strong generalization capabilities beyond its training context.

This generalization stands in contrast to base distilled models like DeepSeek-R1-Distill-Qwen-14B, which plateau beyond their trained context lengths:

| Model | 16K | 32K | 64K |
|---|---|---|---|
| DeepCoder-14B-Preview | 45.6 | 57.9 | 60.6 |
| DeepSeek-R1-Distill-Qwen-14B | 50.2 | 53.0 | 53.0 |

While DeepCoder's raw 16K performance is lower due to its longer average response length—leading to truncation and score penalties—it ultimately outperforms other models at 64K thanks to its ability to **reason across longer contexts**.

![__wf_reserved_inherit](https://cdn.prod.website-files.com/69654e88dce9154b5f12070c/699e0b016dcf395993e29c7b_67f569b3fccdc252be8883e7_training%2520rewards(1).png)

DeepCoder's success is a direct result of combining **iterative context lengthening** with **overlong filtering**. As shown in Figure 5, the model's mean response length steadily grows from **8K to 17.5K** over the course of training, while the average reward improves from 0.6 to 0.7—a clear signal that the model is learning more scalable and coherent thinking patterns over time.

⛰️ Baby, there ain't no mountain high enough.

Ain't no context long enough.

— Inspired by Marvin Gaye & Tammi Terrell

## Evaluation

We evaluate `Deepcoder-14B-Preview` on various coding benchmarks, including LiveCodeBench (LCB), Codeforces, and HumanEval+—and AIME2024.

With 14B parameters, our model demonstrates strong performance across all coding benchmarks, achieving 60.6% on LiveCodeBench and a rating of 1936 on Codeforces, comparable to the performance of o3-mini (low) and o1. Additionally, although the model was not specifically trained on math tasks, its reasoning ability gained from coding tasks generalizes well to math. This is evident in its 73.8% score on AIME2024, representing a 4.1% improvement over the base model. Overall, our model shows impressive performance in both coding and math domains.

| Model | LCB (8/1/24-2/1/25) | Codeforces Rating* | Codeforces Percentile* | HumanEval+ Pass@1 | AIME 2024 |
|---|---|---|---|---|---|
| DeepCoder-14B-Preview (ours) | 60.6 | 1936 | 95.3 | 92.6 | 73.8 |
| DeepSeek-R1-Distill-Qwen-14B | 53.0 | 1791 | 92.7 | 92.0 | 69.7 |
| O1-2024-12-17 (Low) | 59.5 | 1991 | 96.1 | 90.8 | 74.4 |
| O3-Mini-2025-1-31 (Low) | 60.9 | 1918 | 94.9 | 92.6 | 60.0 |
| O1-Preview | 42.7 | 1658 | 88.5 | 89 | 40.0 |
| Deepseek-R1 | 62.8 | 1948 | 95.4 | 92.6 | 79.8 |
| Llama-4-Behemoth** | 49.4 | - | - | - |

*As Deepseek and OpenAI evaluate Codeforces internally, we reference Appendix A for more details for the Codeforces evaluation.

**Non-reasoning model.

![__wf_reserved_inherit](https://cdn.prod.website-files.com/69654e88dce9154b5f12070c/699e0b016dcf395993e29c81_67f56b03c6d7c5127b24bb3c_model%2520size%2520vs%2520score(1).png)

## System Optimizations for Post-Training

Training LLMs with long-context RL is time-intensive, requiring repeatedly samplingand training over long contexts. Without system-level optimizations, full training runs can take weeks or even months—our 14B coding runs take 1200–2500 seconds per step, resulting in a total training time of 2.5 weeks!

We introduce and open-source **verl-pipeline**, an optimized extension of verl, an open-source RLHF library, that applies several system-level improvements to accelerate end-to-end RL training. **verl-pipeline** achieves up to **2.5× speedup** over the baseline verl implementation. We apply these new system optimizations to train `DeepCoder-1.5B-Preview` , which reaches 25% LCB, an 8% improvement over `Deepseek-R1-Distill-Qwen-1.5B`.

We invite the community, including the verl team and other emerging projects, to adopt and build on these optimizations.

### Samplers are the Bottleneck

![__wf_reserved_inherit](https://cdn.prod.website-files.com/69654e88dce9154b5f12070c/699e0b016dcf395993e29c71_67f56c38dfbbf6ab160ed69c_Verl_(2)%25201.png)

Post-training systems are often bottlenecked by sampling time—the latency of generating long sequences (up to 32K tokens) using inference engines like vLLM and SGLang. Figure 4 shows Verl's PPO/GRPO pipeline, where the heterogeneity in repsonse length causes some samplers to become stragglers. These stragglers delay training, while completed samplers sit idle, leading to poor GPU utilization.

### Naive Solution: Minibatch Pipelining

![__wf_reserved_inherit](https://cdn.prod.website-files.com/69654e88dce9154b5f12070c/699e0b016dcf395993e29c78_67f56c5d80a19af69dc72263_minibatch_(1)%25201.png)

To reduce idle time in post-training, we pipeline sampling and training—allowing trainers to start updating on earlier minibatches while samplers continue generating the next. This overlap helps mask sampling latency.

However, this approach has three key limitations:

- First, the average sequence length of mini-batches tends to grow over time, increasing the training time for later minibatches. As a result, the final few minibatches often spill over after sampling completes, limiting the benefits of pipelining.
- Second, pipelining requires splitting GPUs between samplers and trainers, reducing the number of available samplers. Unlike Verl, which dynamically switches samplers and trainers across the same GPU pool, this static split can slow down end-to-end sampling times due to fewer samplers.
- Finally, reward function calculation can take a long time, especially for coding related tasks, which require running thousands of unit tests per RL iteration. By default, Verl calculates reward on the head node after sampling finishes.

Despite its constraints, we implement minibatch pipelining in `ray_trainer_pipeline.py` in our codebase and note that pipelining can be further improved with microbatching.

### Our Solution: One-Off Pipelining

![__wf_reserved_inherit](https://cdn.prod.website-files.com/69654e88dce9154b5f12070c/699e0b016dcf395993e29c74_67f56c6f556503fa35253a1e_async_(1)%25201.png)

To fully pipeline training, reward calculation and sampling, we introduce **one-off pipelining**. The idea is simple: sacrifice the first RL iteration for sampling only, and then use that batch to train in the next iteration. This enables sampling and training to proceed in parallel, eliminating trainer idle time after sampling.

Second, reward calculation is interleaved with sampling. As soon as a request completes, its reward is computed immediately—reducing the overhead of reward evaluation, especially for compute-heavy tasks like test case execution for coding.

We implement one-off pipelining in `ray_trainer_async.py` in our verl fork.

### End2End Performance

In Figure 7, we evaluate verl, microbatch pipelining, and one-off pipelining for two workloads: math and coding. For fairness, all baselines compute reward in parallel via a Python threadpool; verl officially computes reward for each sample serially, which is intractably long for coding.

We evaluate `Deepcoder-1.5B-Preview` on 8xA100s and tune the ratio of samplers to trainers to better balance trainer and sampler times.

For math,  one-off pipelining reduces time per RL iteration by **1.4x**. We note that math's reward computation time is near zero, as it consists of basic sympy checks. In particular, one-off pipelining completely masks away trainer times, unlike minibatch pipelining where the last minibatch spills over.

For coding, calculating reward requires running 1000s of tests per RL iteration, a time consuming process. One-off pipelining masks away both trainer and reward computation times, which reduces end-to-end training times by **2x**.

![__wf_reserved_inherit](https://cdn.prod.website-files.com/69654e88dce9154b5f12070c/699e0b016dcf395993e29c7e_67f56cab3dedfa0d39c994b9_baseline_comparison(1).png)

**1.4x**for math and

**2x**for coding.

Most importantly, one-off pipelining works and scales to difficult coding tasks. We trained `DeepCoder-1.5B-Preview` using `ray_trainer_async.py`, showing 8% improvement in LCB scores over the base distilled model.

| Model | LCB (8/1/24-2/1/25) | Codeforces Rating | Codeforces Percentile | HumanEval+ |
|---|---|---|---|---|
| DeepCoder-1.5B-Preview | 25.1 | 963 | 28.5 | 73.0 |
| Deepseek-R1-Distill-Qwen-1.5B | 16.9 | 615 | 1.9 | 58.3 |

## Conclusion

In this work, we introduce `Deepcoder-14B-Preview`, a 14B model reaching `o3-mini` performance with **60.6%** Pass@1 accuracy for LiveCodeBench. To achieve this, we curated high-quality, verifiable coding data and introduced algorithmic and system optimizations for effective RL training.

Our goal is to democratize RL training for LLMs. `Deepcoder-14B-Preview` represents the second major milestone in this direction, building on the foundation laid by our first model, `DeepScaleR-1.5B-Preview`, which focused on math reasoning. By fully sharing our dataset, code, and training recipe, we empower the community to reproduce our work and make RL training accessible to all.

We believe advancing RL scaling is a collective, community-driven endeavor, and we welcome open-source contributions and sponsorships. Let's work together to push the frontiers of RL for LLM reasoning—and beyond!

## Citation``


## Appendix

### A — Codeforces

Our Codeforces evaluation uses the [Qwen CodeElo benchmark](https://codeelo-bench.github.io/), which consists of 408 problems from 57 contests ranging from Div. 4 to Div. 1 difficulty. There has been a lack of a unified Codeforces evaluation benchmark, with different methodologies used by OpenAI and Deepseek. This is an initiative to try to standardize this particular widely used benchmark.

#### Scoring

Following Codeforce's official methodology for calculating score, each problem starts off with $k$ points as the maximum obtainable point value for the problem. On every incorrect submission, $k$ decreases by 50, all the way down to 0 with enough incorrect submissions. In our evaluation, we had every model generate 8 responses for each problem, and collected the success/fail for each submission to find the points obtained by the model for that question. For each contest, the points are then tallied up and that becomes the model's total score for the contest.

**Elo Rating Calculation**

The methodology for Elo rating calculation is very similar to the official methodology employed by Codeforces. The main difference is that unlike Codeforces, which updates a participant's rating continuously across multiple contests, our approach treats each contest independently. This simplifies the calculation and enhances accuracy for isolated assessments of performance.

Concretely, we estimate each model's expected rating using the following formula from Elo & Sloan, 1978:

$$m=\sum^n_{i=1}\frac{1}{1+10^{(r-r_i)/400}}$$

In this scenario, a contest features $n$ human participants, each with known ratings $r_i$ for $i=1,2,\dots,n$. The model achieved a rank of $m$ among these participants, and using these, we find the expected rating of the model $r$ for a particular contest.

We obtain human participant scores for a particular contest using the Codeforces API to reflect a very real world Elo rating for our model.

The overall estimated Elo rating of the model across all 57 contests is found by averaging the ratings.

#### Proof of Equivalence

For a detailed proof of equivalence, refer to the [CodeElo paper](https://arxiv.org/pdf/2501.01257)'s appendix C in which they prove the mathematic equivalence of this Elo rating calculation method and the official Codeforces method.

**Percentile Calculation**

Each percentile of ratings among all human participants is based on publicly available user ratings from the Codeforces platform. The data is from 2024, consisting of 89352 rated users. We chose 2024 for consistency as the range of the contests used in the CodeElo benchmark are all within 2024. Big thanks to the user 123gjweq2 on Codeforces for this data.
