---
title: 'gpt-oss on Fireworks: Tool Calling Fixes and Benchmarks | Fireworks'
kind: blog
topic: null
subtopic: null
secondary_topics: []
summary: null
triage: null
skip_reason: null
source: fireworks
url: https://fireworks.ai/blog/gpt-oss-tool-calling-fireworks
author: null
published: '2025-08-12'
fetched: '2026-10-23T06:14:26Z'
classifier: null
taxonomy_rev: 2
words: 734
content_sha256: 6620e69907cedb945f8675e5633721f7d1265d8f65202bbbb5b77800cbfe5889
---

# gpt-oss on Fireworks: Tool Calling Fixes and Benchmarks | Fireworks

It’s been an incredible week for the open-source AI community. The release of GPT-OSS marked a significant milestone, opening up new possibilities for developers and researchers worldwide. This is especially exciting as it is released from a US frontier lab 🇺🇸. At [Fireworks.ai](https://fireworks.ai/), we believe that making a model available is only the first step. The real work lies in making it reliable, performant, and truly production-ready.

From the moment GPT-OSS was released, our team worked tirelessly not just to host it, but to provide the single best implementation available anywhere. Our “Quality First” approach meant diving deep into the code, identifying critical issues, and deploying robust fixes to ensure our partners and the entire community could build on a solid foundation.

We were proud to help power the official demo site at [**gpt-oss.com**](https://www.google.com/url?sa=E&q=http%3A%2F%2Fgpt-oss.com) and support the Hugging Face team to ensure everyone could experience the power of GPT-OSS from day one.

### The Critical Weak Point: Tool Calling

For modern AI applications, tool calling (or function calling) is not just a feature; it’s the bridge between language models and the real world. It allows models to interact with APIs, access external data, and perform actions, transforming them from simple chatbots into powerful agents.

However, the initial release of GPT-OSS, while powerful, had inconsistencies and bugs in its tool-calling implementation. This meant developers would face malformed outputs, failed function calls, and unreliable behavior—barriers to building robust, production-grade applications.

We immediately focused our engineering efforts on solving this. Our deep dive paid off, and the results were quickly recognized by the community. OpenRouter, a leading LLM gateway that rigorously tests model providers, highlighted the quality of our implementation, naming it the best for tool calling.

### Engineering in the Open

Our commitment to quality extends to the entire open-source ecosystem. After identifying and fixing a critical bug in the model’s tokenizer logic, we didn’t keep it to ourselves. We immediately upstreamed our fix, sharing it with the community to ensure that every implementation of GPT-OSS could benefit from this improvement. This is what true open-source collaboration looks like.

### The Result: OpenAI Under-Reported Some Benchmarks

Here’s where it gets exciting. After implementing our fixes, particularly the harmony tokenizer fix, we re-ran the tool-calling benchmarks. Our findings suggest that the initial scores reported by OpenAI were based on the model before these critical bugs were addressed.

With the fixes in place, the model’s true capabilities are even more impressive than we thought. **We believe OpenAI under-reported their tool-calling benchmarks by 5\~10% due to possible** issues with tool calling or differences in test setup\*\*.\*\*

Here are the scores on our production-ready, fully-patched GPT-OSS implementation across several challenging tool-use benchmarks, all done with average 8 runs.

### Reproducing Our Results

The numbers reported above are an average over 8 runs, where we used:

- A reference implementation of gpt-oss [https://github.com/openai/gpt-oss?tab=readme-ov-file](https://github.com/openai/gpt-oss?tab=readme-ov-file) chat completion sampler

`pythonCopy`
1

- For reporting evaluations with confidence interval, we use eval-protocol which calculates the evals. For example, for AIME low effort, here is the following command to reproduce from eval-protocol’s python SDK

`pythonCopy`
12345

- We also cross check with the base implementation of Tau2-Bench: [<u>tau2-bench</u>](https://github.com/sierra-research/tau2-bench). This is the script we ran.

`pythonCopy`
12345678910111213141516171819

Note that for results that is supposed to be run with temperature > 0, we strongly recommend model builders to release benchmark with CI results going forward, so that the users can have clearer expectation on model performance, and it can also help uncover cases where model builders accidentally under report their results.

### Why This Matters for You

For developers building the next generation of AI applications, quality is everything. When you build on [Fireworks.ai](https://fireworks.ai/), you get:

- **Unmatched Reliability:** Our fixes mean fewer errors, more predictable behavior, and a stable foundation for your products.
- **Superior Performance:** Access the true, unlocked potential of GPT-OSS with benchmark-proven improvements in critical areas like tool calling.
- **Faster Development Cycles:** Don’t waste time debugging model-level inconsistencies. Build with confidence, knowing the underlying engine is solid.

### Get Started with the Best GPT-OSS Today

The hype around a new model release is exciting, but enduring value comes from meticulous engineering and a relentless focus on quality. At [Fireworks.ai](https://fireworks.ai/), we didn’t just host GPT-OSS; we perfected its implementation to deliver the performance and reliability the community deserves.

Try out gpt-oss on fireworks at [https://fireworks.ai/models/fireworks/gpt-oss-120b](https://fireworks.ai/models/fireworks/gpt-oss-120b) . Let us know if you have any feedback!
