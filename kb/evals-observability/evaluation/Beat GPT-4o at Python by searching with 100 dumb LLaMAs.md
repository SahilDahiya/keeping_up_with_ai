---
title: Beat GPT-4o at Python by searching with 100 dumb LLaMAs
topic: evals-observability
subtopic: evaluation
secondary_topics:
- models/benchmarks
summary: Explores using many small Llama runs and search to improve Python benchmark
  performance against GPT-4o baselines.
source: modal
url: https://modal.com/blog/llama-human-eval
author: null
published: '2024-08-05'
fetched: '2026-07-11T04:30:07Z'
classifier: codex
taxonomy_rev: 1
words: 1572
content_sha256: 8b783c01cb0c5d6d22161779e33547b93d08c64e0971a91f353ff3d82b99228d
triage: keep
skip_reason: null
---

# Beat GPT-4o at Python by searching with 100 dumb LLaMAs

[Back](https://modal.com/blog)

# Beat GPT-4o at Python by searching with 100 dumb LLaMAs

[Charles Frye](https://twitter.com/charles_irl)

[Howard Halim](https://twitter.com/HowardHalim)

One thing that should be learned from the bitter lesson is the great power of general purpose methods, of methods that continue to scale with increased computation even as the available computation becomes very great. The two methods that seem to scale arbitrarily in this way are

searchandlearning.Richard Sutton,

The Bitter Lesson

The eponymously distasteful take-away of Richard Sutton’s [essay](http://www.incompleteideas.net/IncIdeas/BitterLesson.html?ref=blog.heim.xyz) has often been misconstrued: because scale is all you need, they say, smaller models are doomed to irrelevance. The rapid increase in model size above one trillion parameters and the technological limitations of GPU memory together seemed to foreclose on economical frontier intelligence anywhere except at an oligopoly of intelligence-as-a-service providers. Open models and self-serve inference were in retreat.

But as the quote above indicates, there are in fact two arrows in the scaling quiver: learning and search. Learning, as we do it now with neural networks, scales with *memory* at inference time — larger models perform better, ceteris paribus, because they can extract more data from their training set into more [circuits](https://transformer-circuits.pub/) and more [templates](https://arxiv.org/abs/2305.18654). Search scales smoothly with *compute* at inference time — compute that can be spent on either producing higher quality candidates or on producing more candidates. In the ideal case, the scaling behavior can be predicted via so-called scaling laws.

Recent papers indicate that generative models like LLMs can be scaled up with search. The [Large Language Monkeys](https://arxiv.org/abs/2407.21787) paper, published on arXiv by Brown, Juravsky, and co-authors last week, includes several results in this vein and indicates that frontier-level intelligence in certain domains can be elicited from smaller models that can run on a single, past-generation GPU.
Further, they observed smooth, predictable improvement of performance with scale.

Put more simply: where before, it seemed frontier capabilities required [one horse-sized duck](https://knowyourmeme.com/memes/horse-sized-duck), it is clear we can now alternatively get them with one hundred duck-sized horses (or, rather, LLaMAs).

This weekend, we set out to replicate this finding.

## Scaling LLaMA 3.1 8B HumanEval on Modal

Running all of our experiments, including configuration and testing, cost well under $50.

You can find our code [here](https://gist.github.com/charlesfrye/27f25188dbbcfdf20a83c0230020fe05). You can run it yourself without exceeding the $30/month in credits included in [Modal’s free tier](https://modal.com/pricing).

### Metrics and data: HumanEval and pass@k

We picked a dataset that was not covered in the Large Language Monkeys paper: [HumanEval](https://huggingface.co/datasets/openai/openai_humaneval), a somewhat misleadingly-named dataset of Python function specifications and their tests from OpenAI.

The existence of these tests is crucial to enabling search. Any candidate solution can be evaluated by running it against the tests — no humans are required to evaluate HumanEval. That means correctness can be assessed objectively, with none of the [issues that bedevil LLM-as-judge approaches](https://arxiv.org/abs/2406.18403). The Large Language Monkeys paper further indicates that majority-voting and other techniques fall off their scaling laws quickly.

We set out to demonstrate that by running LLaMA 3.1 8B Instruct many times, we could match or exceed GPT-4o’s performance on HumanEval. Performance is measured via the “pass@k” metric: the chance that out of the k programs produced by the LLM, at least one will pass the tests. We consider also “fail@k”, the chance that no program will pass the tests, which is always 1 - pass@k. [Result aggregator PapersWithCode reports](https://paperswithcode.com/sota/code-generation-on-humaneval) GPT-4o’s pass@1 performance as 90.2% (0-shot, taken from Claude 3.5 Sonnet evals), so that was our target.

### Infrastructure: LLM inference

We ran our experiments with [Modal’s serverless GPUs](https://modal.com/docs/guide/gpu). Smaller models are generally more compatible with a serverless approach because they can be more rapidly loaded from remote storage or disk. The arithmetic throughput of GPUs is many orders of magnitude greater than the read throughput of disks ([H100 FLOP throughput is measured in PB/s](https://resources.nvidia.com/en-us-tensor-core/nvidia-tensor-core-gpu-datasheet?ncid=no-ncid)), so it is in general a good idea to trade more computing time for less loading time. Of course, that means you want to make sure that setup time is as fast as possible, as we’ve done at Modal by [rewriting the container stack](https://www.youtube.com/watch?v=3jJ1GhGkLY0).

Our experiments were enabled by the open source [vLLM inference server software](https://docs.vllm.ai/en/latest/). Follow-up on promising [initial research](https://arxiv.org/abs/2306.03081) into scaling out search with LLMs last year was slowed by the need to implement performant caching mechanisms. These mechanisms are now a standard part of inference servers, [pioneered by vLLM](https://charlesfrye.github.io/programming/2023/11/10/llms-systems.html#paged-memory). Caching ensures that token sequences that are repeatedly processed (like the prompt whose solution is being searched for) incur only constant cost with respect to search scale. Executing batch inference was as simple as changing the `n` parameter in our generic OpenAI-compatible client’s ChatCompletion requests to a vLLM server running in OpenAI-compatible mode on Modal. Check out [this guide](https://modal.com/docs/examples/llm_inference) to running OpenAI-compatible LLMs on Modal for more details.

We scaled up to ten A100-40GB GPUs and hit ~40,000 output tokens per second without particular attention to tuning — a decided benefit of vLLM over other ([nominally more performant](https://bentoml.com/blog/benchmarking-llm-inference-backends)) inference servers. This scale is compatible with [Modal’s free tier](https://modal.com/pricing), but enterprises running on Modal can easily scale at least two orders of magnitude higher, or 4,000,000 output tokens/second. With our new [reduced prices](https://modal.com/pricing), that’d cost roughly $0.25 per million output tokens, competitive with dedicated inference-as-a-service providers — plus greater control over your deployment.

### Infrastructure: Evaluation

Evaluating the model’s output requires executing arbitrary Python code, which means we need a technique for secure isolation. That would be a tricky proposition for a platform that offers inference-as-a-service or serverless GPUs alone. Good thing we have [Modal Sandboxes](https://modal.com/blog/prompt-olympics-summer-2024)! Sandboxes use the same fast-booting, secure containerization technology that powers the rest of Modal, but provide a simple interface for dynamic creation and teardown in the middle of program execution.

Again restricting ourselves to the concurrency limits of [Modal’s free tier](https://modal.com/pricing), we were able to run ~3,000 tests in parallel (32 workers per node on 100 nodes). This was more than sufficient for our needs, so we didn’t press further on scaling evaluation.

## Matching and exceeding GPT-4o’s performance

We were able to replicate the core results of the [Large Language Monkeys paper](https://arxiv.org/abs/2407.21787) with a new model (they used the LLaMA 3 series, we used LLaMA 3.1) and a new dataset (they showed results for math datasets like GSM8K and for the software engineering dataset SWE-bench, we used HumanEval).

Specifically, we found that (with minimal prompt tuning and no tuning of other hyperparameters) we could boost the performance of LLaMA 3.1 8B from 66.4% with only one generation to comparable performance with GPT-4o with 100 generations (90.5% versus 90.2%) and clearly superior performance with 1000 (95.1%).

![Results for LLaMA 3.1 8B on HumanEval pass@k demonstrating better performance than GPT-4o pass@1 for 100 or more samples](https://modal-cdn.com/cdnbot/llama3-1-8b-pass-at-k.png)

 We also found that our results on HumanEval were smoothly predictable (“enjoy scaling laws”) across three orders of magnitude. We prefer the following presentation, which inverts “pass@k” to “fail@k” and logarithmically transforms both axes.

![Results for LLaMA 3.1 8B on HumanEval fail@k demonstrating smooth log-linear scaling across three orders of magnitude](https://modal-cdn.com/cdnbot/llama3-1-8b-fail-at-k-scaling.png)

 Both axes are log-transformed.

Note that these results are distinct from a “replication” of the original paper’s results in the strict sense. Instead, these are a replication of the core claim, which is that, when augmented with search, smaller models can outperform bigger ones in a predictable way. We consider that a stronger signal for the industrial relevance of the underlying work than replication sensu stricto.

## What’s next?

Search is a powerful technique for improving intelligent systems that has been relatively under-appreciated in this past decade focused on (deep) learning.

Search is powerful precisely because it can be transparently scaled. In the words of Richard Sutton, search “continue[s] to scale with increased computation even as the available computation becomes very great”. Modal is designed to make the available computation very great indeed. Search also shifts the balance of resource consumption from memory to compute, which has, due to semiconductor trends, historically been a winning move. Not coincidentally, it favors Modal’s [serverless execution model](https://www2.eecs.berkeley.edu/Pubs/TechRpts/2019/EECS-2019-3.pdf).

Search is enabled by high quality evaluation of outcomes. Impressive recent results in mathematics, like [DeepMind’s AlphaProof and AlphaGeometry 2 getting a silver medal in the 2024 International Math Olympiad](https://deepmind.google/discover/blog/ai-solves-imo-problems-at-silver-medal-level/), have been enabled by the translation of informal natural language mathematical problems into formal statements in Lean, which enables their detailed supervision by a proof verifier/compiler. The increased parallelization of mathematical work made possible by formalization also played a role in [the recent verification that the fifth Busy Beaver number is 47,176,870](https://scottaaronson.blog/?p=8088).

By the Curry-Howard-Lambek correspondence, mathematical proofs can be identified with computer programs. We can expect similar gains in the use of generative models in programming by pairing them with compilers and test suites, as in our small experiment and in [the original paper’s experiments on SWE-bench](https://arxiv.org/abs/2407.21787).

The extension of this technique to domains outside of mathematics and programming is not obvious — how do you effectively search over open-ended natural language responses to “write an email to my insurer contesting this claim denial” or “summarize this email”?. But we can loosely expect that generative models will see gains in performance in domains in proportion to those domains’ ability to precisely specify and speed up their measurement of outcomes and thence search. Agents in repeatable digital environments seem like a good frontier to target.

From this point of view, search is downstream of evaluation. Hence the [claim](https://applied-llms.org/#build-llmops-but-build-it-for-the-right-reason-faster-iteration) that [many](https://hamel.dev/blog/posts/evals/) [AI](https://youtu.be/RrDBV6odPKo) [engineers](https://www.youtube.com/watch?v=2CIIQ5KZWUM) [are](https://arjunbansal.substack.com/p/evolution-of-llm-agents) [making](https://eugeneyan.com/writing/evals/): evaluation is the missing ingredient in the productionization and continual improvement of generative model applications.
