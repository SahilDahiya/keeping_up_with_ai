---
title: Do transformers notice their own mistakes? Finding a linear hallucination detector
  inside LLMs
kind: blog
topic: evals-observability
subtopic: evaluation
secondary_topics:
- models/architectures
summary: Finds a linear probe on a frozen Gemma-2 observer model's residual-stream
  activations detects contextual hallucinations with up to 0.99 F1 on XSum/CNN-DailyMail-derived
  examples, in a single generator-agnostic forward pass, introducing the ContraTales
  benchmark of 2000 stories ending in deliberate contradictions.
triage: null
skip_reason: null
source: baseten
url: https://www.baseten.co/blog/do-transformers-notice-their-own-mistakes
author: Mudith Jayasekara
published: '2025-05-08'
fetched: '2026-11-12T06:15:58Z'
classifier: claude
taxonomy_rev: 2
words: 1065
content_sha256: f29a89fd8eaa28d38ff93592e19632f59a76978d1cf307b417e7eafe88265af7
---

# Do transformers notice their own mistakes? Finding a linear hallucination detector inside LLMs

Research
# Do transformers notice their own mistakes? Finding a linear hallucination detector inside LLMs

A linear signal in LLMs reveals hallucinations, is detected by a frozen observer, and steered with a single vector.


- Authors
- Date
- May 8, 2025

Large language models can write beautiful prose, translate languages, and even generate code. But they also have a curious tendency to "hallucinate" – to confidently state things that are plausible-sounding but completely unsupported by the context they were given, or even factually incorrect. This is a major roadblock for deploying them in sensitive applications. When a model quietly slips in a statement its own context can't back up, does it, in some sense, *realize* it's gone off-script? And could another AI, acting as a careful observer, pick up on this?

In our new paper, we explore how a separate "observer" model can detect such contextual hallucinations. This observer reads the entire text (initial context + continuation) and, in a single pass, determines if the continuation is unsupported. A simple, linear signal within the observer's activations robustly flags these unsupported statements. We evaluate on \~1 000 examples each from XSum and CNN/Daily Mail, and we introduce **ContraTales:** 2000 miniature stories that end in a deliberate logical contradiction.

Think of a human proof‑reader: read the whole document, then ask, “Does the ending follow?” Our "observer paradigm" is analogous. We take a standard transformer (like Gemma-2), ensure it didn't participate in creating the text, and feed it the full document. We then ask: based on its internal state, does it consider the last part a hallucination?

This setup is generator-agnostic (no need for the original model’s internals) and works in a single forward pass, making it efficient.

We hypothesised that an observer model's internal representation of a hallucination might be linear. We tested this by training a linear probe (logistic regression) on the observer's residual stream activations, taken at the end of the potentially hallucinated sentence.

Figure 1 shows these linear probes perform well, achieving high F₁ scores (up to 0.99 on news benchmarks). The ability isn't confined to just one "magic" layer; it’s a persistent representation in the model’s residual stream. Performance rises sharply in early layers, then forms a broad plateau in middle-to-late layers, suggesting the representation of "contextual support" is built up and stably present.

How does this linear probe compare to other detection methods? We benchmarked it against lexical overlap, entity verification, semantic similarity, and attention-pattern analysis (e.g., **Placeholder: ContentReferenceRecord (inlineBlock)**{
  "node": {
    "type": "inlineBlock",
    "item": "R0p650rcQWWiqYZLSxlyxw"
  },
  "record": {
    "\_\_typename": "ContentReferenceRecord",
    "id": "R0p650rcQWWiqYZLSxlyxw"
  }
}).

Our linear probe (Figure 2, right-most bar in each group) outperforms these baselines by 5–27 F₁ points. The difference is stark on ContraTales, where contradictions are purely logical (e.g., "Jack is bald… Jack went to get a haircut."). Surface-level cues falter here, but the linear probe maintains strong performance (0.84 F₁ with our largest observer).

This "hallucination-detecting direction" is not a quirk.

- **Across Model Sizes:** The layer-sweep pattern (Figure 1) is consistent across Gemma-2 models (2B to 9B parameters).
- **Across Datasets:** A linear probe trained on one news corpus transfers well to another with minimal performance drop.

Figure 3 shows this transferability. While lexical cues degrade when styles change (e.g., Train XSum → Test CNN/DM), the linear probe remains robust, suggesting it captures a fundamental representation of contextual consistency.

If a linear direction signifies hallucinations, which transformer components represent it? We used gradient-times-activation attribution to trace the probe's decision. The signal isn't diffuse nor primarily in attention heads. Instead, a sparse, consistent cluster of MLP (feed-forward) blocks in late-middle layers appears key.

Figure 4 shows that for a probe on layer 10 of Gemma-2-9B, MLP blocks in layers 7 and 8 consistently push the representation towards "hallucination" (positive attribution), while layer 9 pushes away (negative attribution). This {positive → strong-positive → negative} MLP triplet recurs across all tested datasets, indicating a compact, responsible sub-circuit.

To test causality, we injected the normalized ‘hallucination vector’ into a generator’s residual stream while it wrote summaries (known as *steering*).

Figure 5 shows a monotonic trade-off: steering with α=+60 increases the hallucination rate to 0.86, while α=−60 results in a 0.35 rate (a 51 percentage point swing across this range). This demonstrates that the linearly decodable direction is an actionable control knob.

Can an observer's detection be improved without new hallucination labels? We lightly finetuned observer models on *only correct* (non-hallucinated) text from the ContraTales domain.**Placeholder: ContentFootnoteRecord (inlineBlock)**{
  "node": {
    "type": "inlineBlock",
    "item": "ba1x97xVRUCf4WAEZsU4JA"
  },
  "record": {
    "\_\_typename": "ContentFootnoteRecord",
    "id": "ba1x97xVRUCf4WAEZsU4JA"
  }
} This involved two epochs of SFT (AdamW, LR 1×10−5, context 512, batch 64).

Figure 6 shows this unsupervised domain adaptation improved the linear probe's F₁ score upon retraining. For Gemma-2-9B on ContraTales, F₁ jumped from 0.75 to 0.89. Exposure to coherent text sharpens the model's internal representation of supported statements. Most experiments fit on a single 48 GB H100 GPU; finetuning used 8xH200 GPUs (wall-clock time typically under an hour), and steering experiments also benefited from multiple GPUs for latency.

- **Generator-Agnostic Detection:** Our work demonstrates a simple, single-pass method to detect contextual hallucinations without needing access to the generating model's internals.
- **Linearity of Complex Concepts:** It shows that a complex property like "contextual support" can be robustly represented along a single linear direction in activation space.
- **Causal Control:** The identified direction is not just correlational but can be used to causally influence a generator's tendency to hallucinate.

Our probe handles single‑span contradictions; multi‑hop reasoning and world‑knowledge gaps remain unsolved.

1. **Persistent Challenges:** Some subtle logical contradictions still evade this linear probe.
2. **Scope:** Current work focuses on single-sentence contradictions; multi-span or more distributed hallucinations are an area for future research.
3. **Circuit Detail:** What computations are these specific MLP layers performing?
4. **Non-linear Components:** How do non-linear aspects of the model's representation contribute to understanding consistency?

**For attribution in academic contexts, please cite this work as:** Jayasekara, Mudith, Charles O’Neill, Sviatoslav Chalnev, Rune Chi Zhao, and Max Kirkby. “Do transformers notice their own mistakes? Finding a linear hallucination detector inside LLMs.” Base Labs, 2025. https://labs.baseten.co/articles/do-transformers-notice-their-own-mistakes

**BibTeX citation**

```
@misc{jayasekara2025hallucination,
  author       = {Jayasekara, Mudith and O'Neill, Charles and Chalnev, Sviatoslav and Zhao, Rune Chi and Kirkby, Max},
  title        = {Do transformers notice their own mistakes? Finding a linear hallucination detector inside {LLMs}},
  year         = {2025},
  howpublished = {Base Labs},
  url          = {https://labs.baseten.co/articles/do-transformers-notice-their-own-mistakes},
}
```
