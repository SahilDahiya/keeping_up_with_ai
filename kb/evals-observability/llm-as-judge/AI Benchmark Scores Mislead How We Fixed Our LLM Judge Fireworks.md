---
title: 'AI Benchmark Scores Mislead: How We Fixed Our LLM Judge | Fireworks'
kind: blog
topic: evals-observability
subtopic: llm-as-judge
secondary_topics: []
summary: Shows how a naive LLM-as-judge gave a UI screenshot a misleading 93.3% by
  checklist-matching requirements instead of judging overall quality, and describes
  the rubric redesign used to better align the judge with human evaluation.
triage: null
skip_reason: null
source: fireworks
url: https://fireworks.ai/blog/ai-benchmark-llm-judge-evaluation
author: null
published: '2025-08-15'
fetched: '2026-10-23T06:15:26Z'
classifier: claude
taxonomy_rev: 2
words: 783
content_sha256: dea9bd2ed3da3ef4bd1ba1948ee4762f7f44cfb15ab8336d103b39276d9e4b2c
---

# AI Benchmark Scores Mislead: How We Fixed Our LLM Judge | Fireworks

Would you give GPT-4.1 an A grade for this image? We sure wouldn’t!

![Image Image](https://fireworks.ai/_next/image?url=https%3A%2F%2Fcdn.sanity.io%2Fimages%2Fpv37i0yn%2Fhorizon%2F779b1bb873177b49935763434b7fb864ea7582fb-940x601.png%3Fauto%3Dformat&w=3840&q=75)

That’s exactly what our AI judge did, giving it a 93.3%. To its credit, it was a diligent box-checker, taking a list of 15 requirements and confirmed that, yes, there were colored shapes where the logo should be, and a box where the search bar should be. It was technically correct, but its misalignment to human expectations what matters.

`Copy`
1234567

This is a huge problem in AI. We celebrate benchmark scores that don’t reflect real-world quality. We knew our evaluation was broken, and we used Eval Protocol (EP) to fix it.

To set the scene, if you haven’t already, check out [our example](https://evalprotocol.io/example/svg-generation) on how we ported SVGBench to EP. TL;DR: using our powerful `@evaluation_test` decorator, we implemented the open-source SVGBench and evaluate it using GPT-4.1 as a LLM-judge against a list of rubric items for each task.

## Teaching Our Judge to See Like a Human

Our first evaluation was a simple checklist. It asked questions like, “Is there a search bar?” but not “Does the search bar look right?”

To fix this, we moved from a rigid, row-specific checklist (**listwise**) to a universal rubric that applies to every image (**pointwise**). Instead of checking for pixels, we started judging based on principles humans care about.

I prompted my AI coding assistant to create a new, tougher judge with a more sophisticated rubric:

@question\_row\_1\_gpt-4.1.png This image returned an EvaluateResult of the below. The results don’t seem to line up with what we expect. We want you to add a separate pointwise evaluation that contains a list of rubrics to judge individual images for intent matching for elements you can think of that align with human preference, for example spatial design.

Its implementation lands on these core 5 qualities:

- **🎯 Intent Matching:** Does it actually look like the Google homepage?
- **👁️ Content Recognizability:** Can you read the logo, or is it just colored blobs?
- **📐 Spatial Design:** Does the layout look professional?
- **👤 User Experience:** Is it clear and usable?
- **🎨 Visual Coherence:** Does it all work together?

The assistant quickly scaffolded a new `@evaluation_test` within the EP framework. The core idea was to stop asking “did you follow the instructions?” and start asking “is this any good?”

`pythonCopy`
1234567891011121314151617181920212223242526272829303132333435363738394041424344454647484950515253545556575859606162636465666768697071727374757677

The assistant quickly scaffolded a new test in Eval Protocol. As an aside, we noticed the first results still seemed too high. There was a classic LLM-as-judge bug: the model was generating the score before its reasoning, which leads to uncalibrated scores. A quick fix to our response model—forcing the reasoning to come before the score—solved it.

`pythonCopy`
1234567891011

With that fix, our new human-preference judge was much tougher. It saw through the technicalities and correctly identified the conceptual failures, giving the image a more realistic 39%.

`pythonCopy`
1234

## Finding the Right Balance with Combined Eval Methods

But was a 39% score fair? To the model’s credit, it did get other large components of the image right. Is this method overly aggressive and harsh? Maybe a combined score would reflect the model more accurately!

So, we combined them. Using EP, it’s easy to run both evals and create a weighted average. We decided “human preference” was more important, so we weighted it at 70%.

- **Original Checklist (30%):** Did you follow the technical specs?
- **Human Preference Rubric (70%):** But is it actually recognizable and well-designed?

To quickly iterate on this, we ask our AI coding assistant for help.

Here is my EvaluateResult now. Do you think we should stick with pointwise universal rubric, listwise row-specific rubric items, or a combined evaluation?

It implements the following in our now renamed `test_svg_combined_evaluation`.

`pythonCopy`
123456789101112131415

Running our eval again, we finally get an EvaluateResult that makes sense. It proves that even when a model like GPT-4.1 gets it wrong, the right evaluation system will catch it. Awesome!

`pythonCopy`
1234567891011121314151617181920212223242526272829303132333435363738394041

Of course, the system isn’t just for catching failures. When the model absolutely nails the request, it earns a high score to match:

![Photo Photo](https://fireworks.ai/_next/image?url=https%3A%2F%2Fcdn.sanity.io%2Fimages%2Fpv37i0yn%2Fhorizon%2F4cd5aa37c5164284ccc0e457d8781edde4c9c13c-940x601.png%3Fauto%3Dformat&w=3840&q=75)

`pythonCopy`
123456789101112131415161718192021222324252627282930313233343536373839404142

## Your Evals Should Be Code, Not Hunches

This entire journey—from a hunch that a score was wrong to a robust, hybrid evaluation—happened in a single afternoon. That’s the power of Eval Protocol.

1. **Codify Your Intuition:** Turn vague feelings (“this seems off”) into a reproducible software test.
2. **Iterate Insanely Fast:** Tweak rubrics, change weightings, and fix bugs without derailing your workflow.
3. **Trust Your Metrics Again:** Build evaluations that reflect what you and your users actually care about.

Stop hand-waving your evals. Start coding them.

Check out this [LiveSVGBench](https://github.com/eval-protocol/python-sdk/blob/main/tests/pytest/test_livesvgbench.py) example yourself and get started at [**evalprotocol.io**](http://evalprotocol.io).
