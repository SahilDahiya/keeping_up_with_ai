---
title: 'The Illusion of Thinking: What the Apple AI Paper Says About LLM Reasoning'
topic: models
subtopic: reasoning
secondary_topics:
- models/benchmarks
summary: Analyzes the Apple reasoning paper and what it suggests about evaluating
  LLM reasoning limits.
source: arize
url: https://arize.com/blog/the-illusion-of-thinking-what-the-apple-ai-paper-says-about-llm-reasoning/
author: Jason Lopatecki
published: '2025-06-20'
fetched: '2026-07-11T04:52:29Z'
classifier: codex
taxonomy_rev: 1
words: 936
content_sha256: b6e803fd77fd07036dba389a0e8839462c25d4491552e8526db35a41e6db4389
---

# The Illusion of Thinking: What the Apple AI Paper Says About LLM Reasoning

A recent paper from Apple researchers—The Illusion of Thinking: Understanding the Strengths and Limitations of Reasoning Models via the Lens of Problem Complexity—has stirred up significant discussion in the AI community. The authors argue that Large Reasoning Models (LRMs), which generate detailed “thinking traces” before answering questions, may not truly reason in the way we think. Instead, they claim the models hit hard limits as problem complexity increases.

But the story doesn’t end there. A fast follow-up response, titled The Illusion of the Illusion of Thinking, pushes back on those claims, attributing the observed failures to flawed experimental design—not fundamental model limitations.

Here’s a breakdown of the two sides, the technical issues at play, and what this debate tells us about the future of AI reasoning.

## Watch the Recording


## Listen to the Podcast

## Dive In

- [Read The Illusion of Thinking](https://ml-site.cdn-apple.com/papers/the-illusion-of-thinking.pdf)
- [Read the Illusion of the Illusion of Thinking](https://arxiv.org/pdf/2506.09250v1)
- [Explore More AI Research](http://arize.com/ai-research-papers)

## The Original Claim: LRMs Hit a Complexity Wall

Apple’s researchers introduce LRMs as models designed to perform explicit reasoning—like Chain-of-Thought with self-reflection—before arriving at an answer. To test their limits beyond typical math and coding tasks (which may be compromised by training data overlap), they designed clean puzzle environments with controllable complexity: Tower of Hanoi, River Crossing, Checker Jumping, and Blocks World.

Their key findings:

- **Accuracy Collapse:**As puzzle complexity increased, model performance dropped sharply—regardless of available token budget.
- **Strange Scaling Behavior:**LRMs initially used more tokens (i.e., “thought harder”) as tasks got harder, but then suddenly used fewer tokens on the most complex problems—suggesting they were effectively giving up.
- **Three Regimes of Performance:**- **Low-complexity:**Standard LLMs were more efficient and sometimes more accurate.
- **Medium-complexity:**LRMs had an edge, thanks to their structured reasoning.
- **High-complexity:**Both model types failed completely.

- **Overthinking on Easy Tasks:**LRMs often found correct answers early but kept reasoning anyway, sometimes arriving at incorrect alternatives.
- **Limited Benefit from Algorithms:**Even when provided with explicit solutions (like algorithms for Tower of Hanoi), LRMs didn’t show consistent improvement.

The bottom line of this paper then, is that while LRMs may appear to reason, that appearance breaks down quickly with true complexity.

## Response: *The Illusion of* the Illusion of Thinking

The rebuttal paper, The Illusion of the Illusion of Thinking, challenges these conclusions, arguing the failure modes reflect experimental artifacts, not reasoning limits. Key critiques include:

- **Output Token Limits Were Ignored:**Many Tower of Hanoi failures were due to models hitting output limits, not reasoning breakdowns. In some cases, models explicitly said they were stopping due to length constraints.
- **Evaluation Misread the Signals:**The automated evaluation framework misclassified output truncations and token constraints as reasoning failures.
- **Unsolvable Problems Were Penalized:**Some River Crossing problems were mathematically impossible (e.g., not enough boat capacity to ever solve them). Yet the models were penalized for not solving them—akin to marking a solver wrong for declaring a problem “unsatisfiable.”

When these issues were corrected—like asking for a generating function (e.g., Lua code) instead of listing every step—models performed well even on problems previously labeled as “complete failures.”

The response also questions the complexity metric used in the original paper. For example, Tower of Hanoi requires many moves (exponential in number), but each move is straightforward and deterministic. Meanwhile, River Crossing requires complex search and constraint satisfaction, despite having fewer moves overall.

## Takeaways: What The Illusion of Thinking Debate Reveals

Beyond the back-and-forth, this discussion surfaces deeper insights into how we think about AI reasoning—and how we evaluate it:

- **Engineering Constraints ≠ Intelligence Limits:**Critics argue the collapse seen in the original paper reflects output and runtime limits—not a lack of intelligence. It’s like giving a human a math test without pen and paper and concluding they can’t do math.
- **Visible “Thought” May Be Misleading:**The intermediate reasoning steps LRMs display aren’t necessarily their internal reasoning processes. For example, Anthropic has developed internal tracing tools (not used in the Apple paper) that reveal far more about model decision-making than token outputs alone.
- **LLMs vs. LRMs Is About Tuning, Not Architecture:**Most LRMs are just LLMs trained to externalize their reasoning. This requires more tokens and introduces new failure modes—like overthinking or verbosity—without necessarily improving the core reasoning ability.
- **“Call for Help” Might Be the Future:**One promising idea is to train LRMs to know when they’re stuck—and flag it. Instead of producing nonsense, they could escalate to another model, ask for more context, or use a tool (like a calculator or search engine). Think of it as teaching models to say, “I need help,” like a human would.
- **Philosophical vs. Practical Reasoning:**The debate about whether AIs truly reason may be philosophical, but practical concerns—like performance, reliability, and usefulness—are paramount. For instance, if an LRM can accurately plan its next sentence by simulating token usage, that’s a functional win, regardless of whether we call it “thinking.”
- **Timing and Industry Strategy:**The Apple paper’s timing—just before WWDC—raised eyebrows. Was this a research milestone, or a strategic play to reposition Apple in the broader AI landscape?

## Conclusion

This debate offers a vital reminder: evaluating reasoning in AI is hard, and experiments must be carefully designed to separate performance bottlenecks from true cognitive limitations.

Good evaluations should:

- Account for output and inference constraints
- Confirm that tasks are actually solvable
- Use complexity metrics tied to computational hardness, not just number of steps
- Consider diverse output formats—not just raw sequences—to reveal deeper understanding

Ultimately, the question isn’t just can LRMs reason. It’s whether our benchmarks are sophisticated enough to distinguish genuine reasoning from practical constraints—or from mere “typing fast.”
