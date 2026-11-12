---
title: 'Resurrecting the salmon: seeing clearer inside LLMs with domain-specific SAEs'
kind: blog
topic: models
subtopic: architectures
secondary_topics:
- evals-observability/monitoring
summary: Training a sparse autoencoder on a narrow domain (195,000 medical Q&A examples
  for Gemma-2) instead of general web text recovered 20% more explained variance in
  the model's activations and surfaced crisper clinically-relevant features, addressing
  the vague/generic features typical of general-purpose SAEs.
triage: null
skip_reason: null
source: baseten
url: https://www.baseten.co/blog/resurrecting-the-salmon
author: Charles O'Neill
published: '2025-02-15'
fetched: '2026-11-12T06:15:44Z'
classifier: claude
taxonomy_rev: 2
words: 1322
content_sha256: 12e1d7ded54a3d30acd07f76d73937f5e293752ac69564cae1770b5d858f8330
---

# Resurrecting the salmon: seeing clearer inside LLMs with domain-specific SAEs

Research
# Resurrecting the salmon: seeing clearer inside LLMs with domain-specific SAEs

A powerful, efficient, and domain-robust strategy for safeguarding medical-text generation.


- Authors
- Date
- February 15, 2025

Imagine watching a medical LLM “light up” the instant it recognises *mononucleosis* — or when a single latent flips on for *taste loss*. Sparse autoencoders promise that microscope. They try to deconstruct an LLM's complex internal activity into a concise list of meaningful features.

But there's a catch. When we train these SAEs on vast, general datasets (the entire internet, essentially) they often struggle. They might miss up to 20% of the important signals, and the features they do find can be frustratingly vague. This isn't unlike the infamous "dead salmon fMRI" study. In that experiment, standard statistical methods, when applied too broadly without careful correction, famously detected "brain activity" in a dead fish. Similarly, large, general-purpose SAEs can sometimes identify features that seem interpretable on the surface (or score well on automated tests) but don't truly capture the nuanced, causal mechanisms at play, or they simply miss the vital signals for specific tasks.

Our research points to a counter-intuitive solution: **instead of teaching an SAE to understand everything, we teach it one subject deeply.** We confine its training to a narrow "river" of data. For medical understanding, we trained an SAE exclusively on clinical questions and answers. The result? It’s like the fog lifts. The SAE suddenly "resurrects the salmon": it begins to find the genuine, specific signals it missed before.

Specifically, our domain-focused SAE, trained on 195,000 medical Q&A examples for Gemma-2, **recovered 20% more variance** in the LLM's activations. It surfaced crisp, clinically relevant features like "infectious mononucleosis" and "loss of taste," and dramatically reduced the amount of unexplained, linearly predictable error.

Below, we'll show you how these domain-specific SAEs work, why they outperform their "foundation" counterparts, and how you can explore these ideas further.

Current SAEs, while powerful, face a few key hurdles when trained broadly:

- **Elusive Signals (Reconstruction Errors):** They often fail to perfectly rebuild the LLM's original internal state, meaning some information is lost. This is measured by metrics like "loss recovered" (how much of the LLM's predictive ability we get back when using the SAE's version of its activations).
- **Vague Clues (Generic Features):** Learned features can be too general (e.g., "parts of a sentence") or a single concept might fragment confusingly across multiple features.
- **"Linear Dark Matter":** A good chunk of what the SAE *doesn't* explain (its error) is often simple, linear patterns that it *should* have learned. This uncaptured linear structure is like "dark matter" obscuring our view.

The core issue is that a fixed "budget" of features in the SAE struggles to cover the sheer breadth of the internet, forcing it to learn only the most common denominator patterns.

We hypothesised that focusing an SAE on a specific domain would allow its feature budget to be used much more effectively. Here’s how we built and tested our medical SAE:

1. **Specialised Diet (Dataset):** We combined several public medical datasets (like MedQA and PubMedQA) into a corpus of \~195,000 clinical question-answering examples (\~50 million tokens).
2. **The Student (Model & Layer):** We focused on activations from layer 20 of Google's Gemma-2 (2B and 9B) models—a common layer for rich feature extraction.
3. **The Technique (SAE Architecture):** We used JumpReLU SAEs, an architecture known for helping features activate more decisively.

We then compared these medical SAEs to GemmaScope SAEs (strong baselines trained on general data).

When an SAE specialises, its understanding becomes much clearer.

Our medical SAEs consistently explained about 15-20% more variance in the LLM's activations than general SAEs of similar size. They also scored higher on loss recovered (meaning less of the LLM's original performance is lost when its activations are replaced by the SAE's reconstruction).

This is where the difference becomes striking. Automated interpretability tools (which generate a textual explanation for each feature and then test how well that explanation predicts the feature's activation) gave our medical SAE features higher scores.

More importantly, the features themselves made intuitive clinical sense.

| Feature Explanation (Our Medical SAE) | F1 Score | Representative Example (Activating token in bold) | 
|---|---|---|
| Infectious Mononucleosis | 1.00 | "Positive Paul Bunnell test confirmed mononucleosis in the patient." | 
| Taste Sensations | 0.94 | "Loss of taste sensation in anterior 2/3 of tongue..." | 
| Specificity in Diagnostic Testing | 0.94 | "High specificity of the test ensured minimal false positives." | 

*Table: For full feature lists, see the paper.*

General-purpose SAEs, when encountering medical text, tended to activate on more frequent but less clinically insightful terms (e.g., common verbs, articles, or very broad medical terms like "image").

What about the parts of the LLM's activations that the SAE doesn't capture? We found that our medical SAEs leave behind a smaller amount of "linear dark matter" (error that is simply predictable from the original activation). The error that remains is more likely to be genuinely complex and nonlinear. General SAEs, in contrast, leave more of these learnable linear patterns on the table.

Focusing an SAE on a specific domain forces it to use its limited capacity on features that are high-fidelity and relevant to that task. This mitigates issues like feature fragmentation and improves overall reconstruction, leading to more trustworthy interpretations. It’s like tuning a radio to a specific station instead of trying to listen to all frequencies at once.

By ensuring our "interpretability microscope" is correctly calibrated for the specific "sample" (the domain of text) we are examining, we avoid the "dead salmon" problem of finding spurious signals. We see the true, active features relevant to the task, allowing us to better understand how the LLM "thinks" about that specific domain.

This research opens up several exciting avenues:

1. **Deeper Specialization:** Train SAEs on even larger and more diverse domain-specific corpora (e.g., the entirety of bioarXiv, clinical textbooks).
2. **Methodological Refinements:** Explore alternative optimization goals beyond sparsity, or new SAE architectures tailored for domain specificity.
3. **Broader Applications:** Apply this domain-specific approach to other modalities (like vision or code) or to multi-layer "crosscoders."
4. **Real-World Utility:** Use these highly interpretable features to build causal circuit models of LLM behaviour or for targeted model editing.

We believe that embracing domain specificity is a crucial step towards making mechanistic interpretability a truly practical and insightful field.

- **Why did you choose layer 20 of Gemma-2?** Layer 20 is often a mid-to-late layer in models of this size, where many abstract and semantically rich features are thought to be represented, making it a good target for interpretability.
- **What specific datasets were combined for the medical corpus?** We used MedQA, MedMCQA, MMLU (College Medicine, Clinical Knowledge, Professional Medicine), and PubMedQA. The combined dataset, `irisai/medical-qa-combined`, is available on Hugging Face.
- **Why use JumpReLU for the SAE architecture?** JumpReLU includes a learnable threshold for feature activation, which can help create sparser and more "all-or-nothing" features, potentially improving interpretability by making it clearer when a feature is truly active.
- **How does this compare to just fine-tuning an LLM on a specific domain?** Fine-tuning changes the LLM's weights to be better at a task. Our work focuses on understanding the *internal representations* of an existing LLM (which could be a base model or a fine-tuned one) by training a separate SAE "observer" model on its activations within that domain. The goal is insight, not performance improvement on the task itself.

**For attribution in academic contexts, please cite this work as:**

*O'Neill, Charles, Mudith Jayasekara, and Max Kirkby. "Resurrecting the Salmon: Seeing Clearer Inside LLMs with Domain-Specific SAEs." Baseten Research, February 15, 2025. https://www.baseten.co/research/resurrecting-the-salmon/*

**BibTeX citation**

```
@misc{oneill2025saes,
  author       = {O'Neill, Charles and Jayasekara, Mudith and Kirkby, Max},
  title        = {Resurrecting the Salmon: Seeing Clearer Inside {LLMs} with Domain-Specific {SAEs}},
  year         = {2025},
  month        = feb,
  day          = {15},
  howpublished = {Baseten Research},
  url          = {https://www.baseten.co/research/resurrecting-the-salmon/},
}
```
