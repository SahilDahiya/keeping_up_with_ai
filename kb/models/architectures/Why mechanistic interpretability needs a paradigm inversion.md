---
title: Why mechanistic interpretability needs a paradigm inversion
kind: blog
topic: models
subtopic: architectures
secondary_topics: []
summary: 'Position piece arguing mechanistic interpretability needs ''domain-confined''
  sparse autoencoders rather than broad-domain SAEs trained like foundation models,
  focused on healthcare-model applications (note: source text is partially corrupted
  by a scraping artifact).'
triage: null
skip_reason: null
source: baseten
url: https://www.baseten.co/blog/mechanistic-interpretability
author: Charles O'Neill
published: '2025-01-13'
fetched: '2026-11-12T06:15:40Z'
classifier: claude
taxonomy_rev: 2
words: 1881
content_sha256: 6fbe611841cb45940832a60da338d6a1d84ed75de57e1e60eb12ee6f53134a52
---

# Why mechanistic interpretability needs a paradigm inversion

Research
# Why mechanistic interpretability needs a paradigm inversion

The conventional scaling paradigm for language models themselves may be fundamentally misaligned with interp.


- Authors
- Date
- January 13, 2025

At Baseten, our research into mechanistic interpretability has led us to a counterintuitive conclusion: the conventional scaling paradigm for language models themselves - which has driven remarkable progress in AI capabilities - may be fundamentally misaligned with our goal of understanding how these models work. We believe that mechanistic interpretability requires a paradigm inversion: from broad-domain foundation models (like sparse autoencoders trained on the whole internet) to domain-confined interpretability tools.

This essay outlines our technical argument for this position, a very small taste of the empirical evidence supporting it, and the implications for how we approach AI understanding. While our research is particularly focused on healthcare applications, the principles we discuss have broader implications for mechanistic interpretability as a field. This will not be an empirical or evidence-based paper; rather, it is an attempt to share our thoughts.

The dominant paradigm in AI interpretability has followed the same scaling logic that drives foundation model development: train on diverse, broad datasets to capture generalisable patterns. This approach assumes that interpretability tools, like sparse autoencoders (SAEs), should similarly generalise across domains.

SAEs decompose a model's activation vectors into sparse linear combinations of learned feature directions. When applied to LLMs, they attempt to disentangle the overlapping concepts encoded in the model's hidden layers. The conventional wisdom suggests that training these SAEs on diverse data - mirroring the training distribution of the models themselves - should yield the most generalisable and useful interpretations.

However, our research reveals the limitations of this approach.

Broad-domain SAEs typically leave substantial linear structure unlearned. Following the framework of **Placeholder: ContentReferenceRecord (inlineBlock)**{
  "node": {
    "type": "inlineBlock",
    "item": "dVgebrPNRZiBtL7OP8GRaQ"
  },
  "record": {
    "\_\_typename": "ContentReferenceRecord",
    "id": "dVgebrPNRZiBtL7OP8GRaQ"
  }
}, we can quantify this problem by measuring how much of the SAE's residual error is itself linearly predictable from the input activations. Our experiments consistently show that up to 70-80% of the residual error in broad-domain SAEs is linearly predictable—what Engels termed "dark matter."

This suggests that even large, broad-domain SAEs fail to capture a substantial portion of linearly structured patterns in the model's internal representations. While they may capture high-frequency, common patterns, they leave behind countless domain-specific, low-frequency features that are essential for understanding specialised internal reasoning.

**Placeholder: ContentReferenceRecord (inlineBlock)**{
  "node": {
    "type": "inlineBlock",
    "item": "JEYU7CvaSWuRcldom1JBhg"
  },
  "record": {
    "\_\_typename": "ContentReferenceRecord",
    "id": "JEYU7CvaSWuRcldom1JBhg"
  }
} provided a striking example of this constraint: despite training an enormous SAE with 34 million features on a leading language model (Claude 3 Sonnet), they found it captured features corresponding to only about 60% of London boroughs, despite the model demonstrating knowledge of all boroughs when prompted. The model could even name individual streets within these boroughs, indicating that the missing features exist within the model but aren't captured by even very large broad-domain SAEs. The fixed latent budget, when spread across a vast conceptual space, inevitably leaves many specialised concepts unrepresented.

In broad-domain settings, SAEs frequently exhibit feature splitting (fragmenting what should be a single coherent concept into multiple overly specialised latents) and feature absorption (where token-aligned latents “absorb” an expected feature direction, causing the intended latent to fail to activate in some contexts).

For example, a broad-domain SAE might split a general medical concept like "diabetes" into fragmented features representing only certain aspects such as "elevated blood glucose" and "insulin resistance," without capturing important components like "prescribed antihyperglycaemics" or "metabolic complications," resulting in an incomplete representation of the concept. (Importantly, the overall concept of diabetes itself may not have its own feature.)

Conversely, clinically specific features like “pleuritic chest pain” or “orthopnoea” might be absorbed into broader, non-specific sensory features like “chest discomfort” or “breathlessness,” losing the diagnostic nuance needed to distinguish between conditions such as pulmonary embolism and congestive heart failure. Even worse feature absorption can be absorpotion of the specific features into superficial linguistic patterns like "begins with the letter p”.

These phenomena substantially reduce both the fidelity and interpretability of the resulting features, making it difficult to trace causal reasoning pathways through the model. The tendency toward generic features in broad-domain SAEs stems directly from their optimisation objective. As observed in our previous work (**Placeholder: ContentReferenceRecord (inlineBlock)**{
  "node": {
    "type": "inlineBlock",
    "item": "TEK81O8SQdqg2OaQyVpZ-A"
  },
  "record": {
    "\_\_typename": "ContentReferenceRecord",
    "id": "TEK81O8SQdqg2OaQyVpZ-A"
  }
}), SAEs trained on diverse data distributions face pressure to optimise for reconstruction across an enormous variety of inputs. This fundamentally biases them toward learning abstract, high-level features that have broad applicability but lack specificity. Since the SAE must be able to reconstruct any potential input from the broad distribution, it prioritises features that contribute to reconstruction across many contexts, inevitably sacrificing fine-grained, domain-specific features that only appear in specialised contexts**Placeholder: ContentFootnoteRecord (inlineBlock)**{
  "node": {
    "type": "inlineBlock",
    "item": "YdD4Gx7CR1-NKKTLeiJGFg"
  },
  "record": {
    "\_\_typename": "ContentFootnoteRecord",
    "id": "YdD4Gx7CR1-NKKTLeiJGFg"
  }
}. The consequence is a hierarchy of features where the most general, abstract concepts dominate - essentially another form of feature absorption where specific concepts are subsumed into more general ones. Domain-specific training relieves this pressure, allowing the SAE to develop precise features that are almost certainly more useful for doing things like **Placeholder: ContentReferenceRecord (inlineBlock)**{
  "node": {
    "type": "inlineBlock",
    "item": "AAIY2UETQqCbAnigvOsdKg"
  },
  "record": {
    "\_\_typename": "ContentReferenceRecord",
    "id": "AAIY2UETQqCbAnigvOsdKg"
  }
}.

Perhaps most fundamentally, broad-domain SAEs face an intractable resource allocation problem. With a fixed latent budget (even in the millions of features), SAEs must distribute capacity across an enormous conceptual space. Language models have arguably trillions of concepts internalised, and the SAE can’t learn them all. Inevitably, this forces the SAE to prioritise high-frequency, generic patterns at the expense of domain-specific ones.

This is likely a structural limitation of the broad-domain approach. Even as SAEs grow to enormous sizes (with dictionaries of 2^20 features or more), they continue to miss substantial portions of the model's representational structure.

Our central claim is that these limitations reflect a fundamental misalignment between the goal of interpretability and the scaling paradigm of foundation models. We propose a paradigm inversion: rather than train broader SAEs with larger dictionaries, we should train domain-confined SAEs that focus exclusively on specific domains of interest. And SAEs are actually cheap to train, when you don’t need to train the on the whole internet. If they can be more useful at this smaller scale of data, then it’s a win-win.

Rather than being a pragmatic compromise, our empirical evidence suggests that domain-confined SAEs actually outperform their broad-domain counterparts across all relevant metrics, even when controlling for dictionary size and sparsity levels.

Our JumpReLU SAEs trained on layer-20 activations of Gemma-2 models using 195,000 clinical Q&A examples demonstrate remarkable improvements over comparable broad-domain SAEs:

1. **Higher Variance Explained**: Domain-confined SAEs consistently explain 15-20% more variance than broad-domain counterparts with equivalent capacity.
2. **Superior Loss Recovery**: When substituting SAE reconstructions back into the model, domain-confined SAEs achieve substantially higher loss recovery, indicating more faithful representation of causally important features.
3. **Reduced Linear Residual**: The "dark matter" analysis reveals that domain-confined SAEs leave behind significantly less linearly predictable error, suggesting they better capture the linear structure relevant to their domain.
4. **More Interpretable Features**: Automated and human evaluations confirm that the features learned by domain-confined SAEs align more closely with clinically meaningful concepts (e.g. "infectious mononucleosis", "prescribed antihyperglycaemics", "pleuritic chest pain") rather than generic linguistic patterns.

This empirical superiority has a straightforward theoretical explanation: domain confinement reallocates the SAE's fixed latent capacity to domain-relevant features.

In a broad-domain setting, the SAE must distribute its capacity across a vast conceptual space, capturing only the most frequent patterns. By restricting the input domain, we effectively concentrate the same capacity on a more constrained set of concepts, allowing the SAE to learn more fine-grained, domain-specific features.

There's a persistent tension in scientific understanding between local, specific knowledge and global, general theories. In physics, for example, general relativity provides a sweeping, elegant account of gravity at cosmic scales, but fails to integrate with quantum mechanics at microscopic scales. Complete understanding often requires both global theories and local, domain-specific ones.

Similarly, in AI interpretability, we may need to accept that understanding isn't monolithic. There may not be a single, unified account of how an LLM "thinks" across all domains. Instead, we might need domain-specific lenses that reveal different aspects of the model's internal mechanisms. Both human and artificial intelligence appear to rely on specialised circuits and modules for different domains, despite sharing underlying neural mechanisms.

The foundation model paradigm has been remarkably successful for building capable AI systems, but it may be fundamentally misaligned with our interpretability goals. By training models on diverse data and pursuing scale above all, we create systems whose internal representations are inherently difficult to disentangle.

This suggests a provocative possibility: the most interpretable AI systems might not be the most capable ones. Systems trained on narrower domains might be inherently more interpretable, even if less generally capable.

Perhaps we should think of interpretability not as “understanding the model” in some global sense, but as developing domain-specific translations between the model's internal representations and human concepts. Just as human languages often have specialised vocabularies for different domains (legal terminology, medical jargon, technical nomenclature), our interpretability tools might need domain-specific vocabularies to accurately translate model representations.

In this view, domain-confined SAEs are more faithful translators of the model's internal language in specific domains. They capture the nuances and specialised vocabulary that broad-domain approaches necessarily miss.

While our results provide strong evidence for the value of domain confinement, numerous open questions and research directions remain.

What constitutes an optimal domain granularity remains unclear. Is "medicine" sufficiently confined, or should we pursue even narrower domains like "cardiology" or "oncology"? Our initial results suggest that even relatively broad domains like medical text yield substantial improvements, but the optimal granularity likely depends on the specific interpretability goals.

To what extent do features learned in one domain transfer to others? While our results show that domain-confined SAEs learn more interpretable features within their domain, we have limited understanding of how these features might map to or compose with features from other domains.

How do domain-confined SAEs scale with dictionary size, model size, and data volume? Our initial results show substantial improvements across different model scales, but more systematic study of scaling relationships could inform optimal resource allocation for interpretability efforts.

The paradigm inversion we propose (from broad-domain scaling to domain confinement) represents a rethinking of how we approach mechanistic interpretability. Rather than mimicking the scaling paradigm, we advocate for a more focused, domain-specific approach that yields more faithful and useful decompositions of model behaviour.

This is a shift in how we conceptualise the goal of interpretability. Perhaps understanding an AI system doesn't mean developing a single, unified account of its operation across all domains, but rather constructing domain-specific lenses that reveal different aspects of its internal mechanisms.

In healthcare and other high-stakes domains, this approach offers particular promise. By focusing our interpretability efforts on specific domains where transparency and reliability are paramount, we can develop tools that more faithfully capture the causal mechanisms underlying model behaviour in those domains. We think this may take us one step closer to ensuring the safe deployment of LLMs in the domains where they matter most.
