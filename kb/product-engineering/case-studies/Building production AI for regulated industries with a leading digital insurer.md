---
title: Building production AI for regulated industries with a leading digital insurer
kind: blog
topic: product-engineering
subtopic: case-studies
secondary_topics:
- models/fine-tuning
summary: Case study on a fine-tuned 32B open-source model for FCA-regulated insurance
  queries that beat GPT-5 with max reasoning on accuracy while responding in 2.88s
  (8.7x faster than Gemini-2.5-Pro, 4.2x faster than GPT-5), built around a custom
  knowledge-retrieval system beyond basic vector search.
triage: null
skip_reason: null
source: baseten
url: https://www.baseten.co/blog/building-production-ai-for-regulated-industries-with-a-leading-digital-insurer
author: Charles O'Neill
published: '2025-10-20'
fetched: '2026-11-12T06:14:06Z'
classifier: claude
taxonomy_rev: 2
words: 2081
content_sha256: 752329b27cd0683fd396d0d2fb00afb724df031dd65aef86d73073f9abd0e237
---

# Building production AI for regulated industries with a leading digital insurer

AI engineering
# Building production AI for regulated industries with a leading digital insurer

From frontier OpenAI/Google models to open-source — delivering 8x the speed and outperforming GPT-5-level accuracy.


- Authors
- Date
- October 20, 2025

TLDR

When this leading digital insurer approached Baseten, they had a clear challenge: build an AI system capable of handling customer insurance queries with perfect regulatory compliance, deep policy knowledge, and sub-3-second response times. The constraint is that their industry operates under strict Financial Conduct Authority (FCA) oversight, where a single hallucination or policy misinterpretation could result in regulatory sanctions. For instance, claiming to have “competitive” pricing without robust evidence of this can lead to multi-million dollar lawsuits. Insurance is a very spiky and chaotic task in this regard; slight perturbations of seemingly similar responses can really screw you. Six weeks later, we deployed a fine-tuned 32B parameter open-source model that outperforms all closed-source models (including GPT-5 with maximum reasoning mode) with maximum reasoning while responding in 2.88 seconds, which is 8.7x faster than Gemini-2.5-Pro and 4.2x faster than GPT-5.

Insurance is uniquely challenging for language models. Consider a customer asking: *"Am I covered if my phone gets stolen while I'm traveling in Thailand?"*

A correct answer requires:

- Retrieving the precise policy wording from complex legal documents
- Understanding multi-layered eligibility criteria (coverage tier, destination, item limits)
- Maintaining FCA-compliant language throughout the conversation
- Never hallucinating coverage that doesn't exist
- Handling edge cases with appropriate caveats

Traditional approaches fail here. General-purpose models hallucinate. RAG systems retrieve irrelevant chunks. Fine-tuned models lose reasoning capability. The customer needs accuracy, compliance, and speed simultaneously.

We began by constructing a state-of-the-art knowledge retrieval system. This wasn't a basic vector database—we implemented:

- **Dynamic chunking strategies** that preserve semantic coherence across policy sections
- **Hybrid retrieval** combining dense embeddings with BM25 sparse retrieval
- **Multi-stage reranking** using cross-encoders to surface the most relevant passages
- **Synthetic benchmark generation**: 10,000 question-answer pairs derived from policy documents

Our initial benchmarking showed 94.3% retrieval accuracy on synthetic queries—a strong foundation, but only the beginning.

This is where our approach diverged from most people’s attempts to fine-tune/optimise a model. Typically, a customer might try something like generating a bunch of GPT-5 responses in data they already have, and end up disappointed when the fine-tuned model still has a significant gap to GPT-5 quality (we call this the *distillation gap*). So we need a way to start above the quality of GPT-5 for optimising, regardless of if we use SFT or RL; our learning signal needs to be cleaner than “just slowly learn what GPT-5 would do”.

However, to do this, we first need to actually decide on what quality means. Rather than manually defining success criteria, we use Baseten's internal **evaluation harness constructor** that discovers failure modes systematically.

From a high level, the constructor functions as follows:

1. **Spectrum sampling**: We ran 10,000 customer-style questions through eight models spanning the capability range, from Llama-3-8B (deliberately terrible) to GPT-5 with extended thinking and Gemini-2.5-Pro at maximum reasoning tokens.
2. **Meta-error analysis**: Using an ensemble of reasoning models, we analysed every response for failure modes: hallucinations, policy misinterpretations, compliance violations, inappropriate caveats, missing disclaimers. Just any general part of the output that was wrong, contradicted the instructions in the input, or wasn’t up to scratch, gets recorded.
3. **Hierarchical clustering**: We performed clustering analysis on the error corpus to identify semantic patterns—not just "what went wrong" but "what types of failures occur across the model spectrum."
4. **Evaluation synthesis**: From the clustered error space, we derived seven specialised evaluation prompts. Each prompt acts as an LLM-as-judge for a specific failure mode (e.g., "Does the response hallucinate coverage not present in retrieved policy text?", "Does the response use FCA-compliant language for pre-contractual information?"). We have pretty strong opinions on what makes a good LLM-as-judge prompt, and we have baked these into the prompt generation pipeline.

At this stage, we also do a bunch of analysis to ensure the consistency and transitivity of the evaluation prompts with the big reasoning models ie what’s the variance in pass rate when you feed it the same question+answer multiple times (a perfect evaluator should be zero)? Can it distinguish between really good models and really bad models?


Here's where it gets interesting. Evaluations themselves can be wrong ie misaligned with task requirements or missing critical checks. Our constructor also has a meta-evaluation process:

- **Conflict detection**: Identify when evaluation prompts contradict the generation prompt or task specification
- **Coverage analysis**: Determine if the evaluation set comprehensively covers all failure modes
- **Expert alignment**: If there are ambiguities in the task specification (ie provided generation prompt and provided customer context), we collect these as a list of questions which get sent back to the customer (in this case a leading digital insurer) to clarify.

We also provide some “gold” outputs (optimised with our process discussed in the next section) for this customer to examine; these gold outputs are perfect under the existing evaluators. When this digital insurer identified a compliance issue our evaluators missed, we refined the evaluation prompts. When evaluation prompts flagged responses that the digital insurer considered acceptable, we traced the misalignment back to the task specification.

The result is a stable evaluation harness that correlates strongly with expert human judgment on both compliance and policy accuracy.

We actually simultaneously optimised the prompt for the task itself at the same time as the evaluators, but for the sake of clarity we present the above as if we had a fixed prompt.


With robust evaluations in place, we could optimise at scale.

For 10,000 questions, we ran genetic optimisation using the evaluation harness as the fitness function. This process allows us to converge on responses that satisfy all evaluation criteria. This is computationally expensive but important. It's how we teach open-source models to match frontier model quality. The genetically optimised outputs become our gold training data.

We fine-tuned `Qwen3-32B` on progressively larger subsets: 1k, 5k, and 10k examples. The results were striking:

- **At 1k examples**: Model already competitive with Claude Sonnet 4
- **At 5k examples**: Surpassing Claude Opus 4.1 (5x more expensive)
- **At 10k examples**: Approaching Gemini-2.5-Pro performance

All evaluations used Gemini-2.5-Pro with maximum thinking as the judge, a deliberately conservative benchmark.

We also plotted the evaluation performance at difference checkpoints during training in order to determine how worthwhile it is training on more and more data. Improvement slows down as we train on more and more examples, although we still do get monotonic improvement.

This is a difficult task because the amount of data we have isn’t as abundant as other customers (this is a new product for this digital insurer) - some customers can give us in excess of a million data points, so the key here is to eek out every bit of juice from the samples we do have.


An important next part of the training process is turning the LLM-as-judge evaluation functions into RL reward signals. We are currently training the SFTd model from above with RL and seeing further improvements, which we discuss below.

Fine-tuning on gold outputs only optimises the final response *given* the retrieved context. But most of the performance comes from **making the right retrieval query in the first place**. In addition to this, we can get better performance by also RLing the model with the evaluators themselves as reward functions. Think of SFT as a “warm start” so the model is already in a good place. But we can continue to hillclimb with RL, for both retrieval and the final response.

We needed the model to:

- Formulate precise queries that retrieve relevant policy sections
- Handle ambiguous questions by retrieving multiple relevant passages
- Avoid over-retrieval that adds latency
- Gracefully handle cases where no policy text applies

Another benefit of using RL to improve the tool-calling is that it teaches the model a broadly useful, versatile ability. Rather than having to memorise the specific insurance information for each product, the model instead just learns how to interact with some arbitrary knowledge store to find the information it needs. It also means we don’t have to worry about the knowledge store being dynamic; it doesn’t matter what’s in there if the model understands how to search it in general.


We constructed a synthetic RL dataset by:

- Randomly sampling chunks from the knowledge base
- Generating natural-language questions that require those chunks
- Rewarding the model (via GRPO) when it retrieves the correct chunk
- Penalising incorrect or incomplete retrievals

This co-trains retrieval and generation, ensuring the model learns to search effectively while maintaining response quality.

Our training approach was actually quite similar to the Windsurf/Cognition *Fast Context SWE-Grep* agents, detailed [here](https://cognition.ai/blog/swe-grep). Retrieval is a verifiable task, and so is quite easy to induce a ground-truth dataset with a deterministic reward.


Here's where we made a counterintuitive architectural decision.

Traditional RAG systems rely on vector embeddings. But embeddings introduce brittleness:

- Chunking strategies must be retuned as documents change
- Embedding models can have blind spots for domain-specific terminology
- Retrieval quality degrades when new policy types are added

Inspired by recent advances in coding agents (like Claude Code), we're eliminating embeddings entirely in favour of pure text search with grep-based tools. For example, here’s the model quickly improving across retrieval-based rewards (we have a format reward, a correctness reward, a partial correct reward and a total reward).

Rather than segmenting optimisation between the retrieval pipeline and the model, we put all the capability into the model itself. The model learns to issue precise text-pattern searches over raw policy documents, compose multiple searches to handle complex queries, and importantly self-correct when initial searches don't yield useful results

This approach scales better, requires less maintenance, and leverages the model's reasoning to handle retrieval adaptively. Early results show this matching our optimised RAG performance while being dramatically more robust to document changes.

After six weeks of development:

**Performance**:

- **95.7%** pass rate on compliance evaluation across 5,000 held-out questions
- **Exceeds GPT-5 with extended thinking** on domain-specific accuracy
- **2.88 second** average latency from question to final answer (including tool calls)
vs. 12 seconds for GPT-5 (no thinking)
vs. 25 seconds for Gemini-2.5-Pro

We’re proud to be collaborating with Prime Intellect (leaders in distributed RL training) and expanding the system to:

- Handle multi-turn conversations with policy context tracking
- Support the full policy lifecycle (claims, amendments, cancellations)
- Scale to additional insurance products
- Implement continual learning as new policies are introduced

The infrastructure we’ve built for our customers at Baseten (evaluation-driven development, genetic optimisation, RL for tool use) generalises to any regulated industry where accuracy, compliance, and interpretability are non-negotiable.

A core requirement of this leading digital insurer is that the model generates compliant answers that can always be traced back to the source. Of course, part of this is just citing the sources (specific document chunks used to generate the answer), but we want more powerful tools that provide more granular visibility.

Because we build on an open-source model, we can actually do some useful interpretability on the model. We do two things: mechanistic attribution back to sources, and hallucination detection with probes.

For attribution, we use the attention circuits to aggregate the attention model pays to the retrieved context, on a chunk level, for each output chunk. This allows us to see exactly where the model was looking, and thus what information it was using, when it generated each part of the response. Framed in the right UI, this allows us to see precisely what was being used in a really efficient and clear way.

For hallucination probes, we train a linear probe on the residual stream of the model on LLM-as-a-judge annotated chunks. This provides a cheap way to detect hallucinations at inference time.

Building production AI for regulated industries isn't about prompt engineering or throwing GPT-5 at the problem. It requires, first and foremast, systematic evaluation that aligns with domain expertise. Then, you have to have optimisation techniques that scale to thousands of examples, open-source models that you can inspect, fine-tune, and RL-train, and finally architectural decisions (like pure text search) that prioritise robustness rather than consulting-style brittle solutions.

This digital insurer now has an AI system that their customers can trust, their regulators can audit, and their team can continuously improve. And it's 8x faster than the frontier alternatives.

That's what evaluation-driven AI development looks like in production.
