---
title: If we can't design neat latent structures, then maybe we can Bitter Lesson
  it through self-study
kind: blog
topic: null
subtopic: null
secondary_topics: []
summary: null
triage: null
skip_reason: null
source: baseten
url: https://www.baseten.co/blog/self-study
author: Charles O'Neill
published: '2026-01-26'
fetched: '2026-11-12T06:15:42Z'
classifier: null
taxonomy_rev: 2
words: 1054
content_sha256: 5311177e225363e8b9db0b0f3d81d88312a4c1952b5a615381d5c6c13452f3f9
---

# If we can't design neat latent structures, then maybe we can Bitter Lesson it through self-study

Position
# If we can't design neat latent structures, then maybe we can Bitter Lesson it through self-study

They very existence of Claude's Constitution shows that self-study, to a certain extent, just works.


- Authors
- Date
- January 26, 2026

Anthropic now has a [Constitution for Claude](https://www.anthropic.com/news/claude-new-constitution). Their description says:

*"Claude's constitution is a detailed description of Anthropic's intentions for Claude's values and behavior. It plays a crucial role in our training process, and its content directly shapes Claude's behavior. It's also the final authority on our vision for Claude, and our aim is for all our other guidance and training to be consistent with it."*


This implies that Claude is trained on its Constitution. But if you know much about language models, it probably implies something deeper. When you train a language model on a document, it doesn't simply memorize that document. It has to compress the likelihood of these tokens, one after another, into its weights; a process quite different from the lossless, short-term memory of the KV cache. And even if Anthropic included the Constitution in the training data tens of thousands of times, even if Claude had memorized the entire document verbatim, it wouldn't necessarily *do anything differently*.

A [good example](https://arxiv.org/abs/2309.12288) of this is a quirk of pretraining discovered early on: even if "Socrates was Plato's student" appeared in the training data, the model would fail to answer "Who was the teacher of Socrates?" This held even when the model could regurgitate the definitions of "teacher" and "student" perfectly well. What was the failure mode? Well, minimizing the negative log likelihood of the next token simply did not produce a holistic latent representation of the concepts required. The model couldn't answer that Plato was Socrates' teacher because it hadn't built the latent bridge between "X being Y's teacher" and "Y being X's student."

I think this points toward something fundamental about language models. In order to learn to approximate latent knowledge, you need such a vast amount of data that you've encountered all possible permutations. In the example above, we would have needed many instances of "X is Y's teacher" and "Y is X's student" appearing together in order to learn the pattern "A being B's student implies B is the teacher of A," and to internalize the different surface forms that could express that relation.

Humans probably do something quite different, by having latent encodings of these concepts and the right latent bridges to link them together. We are not restricted to subword tokens as our only means of thought—though some might push back that the residual stream means language models aren't either. We think in pictures and hierarchies and fuzzy feelings and *latent concepts*.

Why outline all of this? Because I think it offers a fundamental clue about language models, and thus a fundamental clue about the future of model shaping. We would all agree that Claude does exhibit a strong internalization of its values and behaviors. And as established above, you don't develop strong internalizations from reading data repeatedly if it's presented as-is. So what's missing?

I believe Anthropic has already told us what the missing ingredient is, and they told us back in 2021. Anthropic has long been doing [Constitutional Alignment](https://www.anthropic.com/research/constitutional-ai-harmlessness-from-ai-feedback), whereby they use some Constitution to improve the model's answers, then perform supervised fine-tuning on these improved answers (alongside preference-based RL). This suggests that by continuously having some guided feedback process arising from a core "latent" (the latent in this case being the Constitution) you can implicitly, through pattern matching and the law of large numbers, internalize that latent to some degree. This was the original constitutional alignment, and Anthropic is probably still using some version of it today.

But I think there's a more explicit approach to learning these latents. [CARTRIDGES](https://arxiv.org/abs/2506.06266) introduces a self-study procedure where, instead of naively conditioning on a document, the model generates synthetic Q&A pairs and dialogues \_about\_ the content, essentially quizzing itself from multiple angles. This is then used as training signal to distill the knowledge into a compact cache.

The relevance to constitutional internalization should be clear: self-study forces the model to encounter the same underlying concepts through many linguistic permutations. If Constitutional AI implicitly creates these permutations via iterative refinement and feedback, CARTRIDGES makes the mechanism explicit. You *manufacture* the diverse views needed for latent compression. The model doesn't just read "X is Y's student" once; it asks "who taught X?", "what was Y's role?", "list X's mentors," until the relational structure is genuinely encoded.

So I imagine Anthropic is doing something similar. They have certain behaviors they want Claude to exhibit, explicitly spelled out in the Constitution, and self-study is used to embed these behaviors into the model. It's clear that Anthropic does this remarkably well; there have been many comments about how [Claude feels like it has a "soul"](https://www.lesswrong.com/posts/vpNG99GhbBoLov9og/claude-4-5-opus-soul-document), thanks in large part to Amanda Askell and her work on personality shaping, in a way that distinguishes it from other LLMs. This also has implications for capability enhancement. I could imagine some form of self-study working for improving humanities-based tasks like essay writing, philosophy, and deep thought.

A final observation: my work at Parsed, and now at Baseten, on finetuning and post-training specialization has, in a funny way, converged toward this same insight. Initially, we developed [Iterative SFT (iSFT)](https://www.baseten.co/resources/research/iterative-sft/) as a way to take a Constitution of sorts (i.e. our evals) and teach a model to improve at those evals by fine-tuning it on data refined with the evals as guide, similar to Constitutional Alignment.

We then developed [Rationale-Guided Thinking (RGT)](https://www.baseten.co/resources/research/upweight-the-strategy-not-the-tokens-faster-training-with-explicit-reasoning-thro/) as a way to make the "latents" we were trying to learn more explicit, rather than hoping the model would learn them through imitating shadows on Plato's cave of perfect dances. Our next direction is making the model itself generate its own critiques, evaluations, and reformulations, i.e. its own self-study. This will make everything much more on-policy, which we speculate can only be a good thing.

So I think the takeaway isn't in the Constitution Anthropic released, but in the very fact they acknowledged its existence. Because it tells us they are still doing some form of constitutional alignment, which tells us it remains worth doing in Anthropic's highly optimized training setup, which tells us that self-study, to a certain extent, just works.
