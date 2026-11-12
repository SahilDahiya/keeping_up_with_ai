---
title: Pinning ML model revisions for compatibility and security
kind: blog
topic: product-engineering
subtopic: security
secondary_topics: []
summary: Argues for pinning model weight revisions the same way you pin package versions
  (e.g. in a Truss config.yaml), to avoid silent backwards-incompatible changes or
  security vulnerabilities from upstream model updates.
triage: null
skip_reason: null
source: baseten
url: https://www.baseten.co/blog/pinning-ml-model-revisions-for-compatibility-and-security
author: Philip Kiely
published: '2023-11-09'
fetched: '2026-11-12T06:11:30Z'
classifier: claude
taxonomy_rev: 2
words: 629
content_sha256: 054e48a5f8b6975a4c0e331283b1dd4b85fa2ac9c25ad85898d044fb8e01fb66
---

# Pinning ML model revisions for compatibility and security

Infrastructure
# Pinning ML model revisions for compatibility and security

Pin versions of open source packages like PyPi's transformers to avoid breaking changes or security issues; similarly, pin model revisions for stability.


- Authors
- Date
- November 9, 2023

TLDR

When you depend on an open source package, like transformers from PyPi, the best practice is to pin the version you use to ensure there aren’t breaking changes or security vulnerabilities introduced to your codebase. You can do the same for model weights and associated code by pinning a model revision.

Working with open source models is much like working with open source packages on PyPi, NPM, and other repositories. You get massive benefits from building on the collective work on the entire industry, but must responsibly address potential security threats and compatibility issues.

Pinned versions is common when using a package manager to prevent two failure modes:

- **Backwards-incompatible changes**, where the package you rely on makes an update which breaks something in your application.
- **New security vulnerabilities**, either due to bugs or malicious code introduced into the package.

Using pinned versions protects against these issues by giving you the chance to review any changes to your dependencies before updating.

When packaging a model with Truss, we strongly recommend pinning versions of required packages in your config.yaml to prevent unexpected breaking changes. Here’s an example from [jina-embeddings-v2](https://www.baseten.co/blog/jina-embeddings-v2-open-source-text-embedding-that-matches-openai-ada-002/), a text embedding model:

yaml

```
requirements:
- accelerate==0.22.0
- sentencepiece==0.1.99
- torch==2.0.1
- transformers==4.32.1
```
Similarly, you can pin a revision for an ML model when using the transformers library to load an open source model.

Let’s say you’re loading a public model from Hugging Face. You can use the revision parameter when loading the model:

python

```
def load(self):
    self._model = AutoModel.from_pretrained(
        "jinaai/jina-embeddings-v2-base-en",
        revision="0f472a4cde0e6e50067b8259a3a74d1110f4f8d8",
        trust_remote_code=True,
    ) # Version is pinned to prevent malicious code execution
```
As the model gets updated by its maintainers, you can update the revision after taking a look at the changes. It’s definitely more work to watch for updates, but you are protected against unexpected changes and are actively monitoring a potential attack vector.

If you want to take things a step farther when using an open source model, you can copy the model into a private repository on Hugging Face and load it from there, or download the necessary model files and host them on a file store like AWS S3.

Maintaining a private copy of a model has the same benefits as forking an open source repository:

- Get the same protections as pinning a model revision.
- Ensure your application isn’t affected if the model you’re depending on is moved or deleted.
- Apply your own updates to the model.

If you make your own private copy of a model on Hugging Face, [follow this example to deploy it to Baseten](https://truss.baseten.co/examples/09-private-huggingface).

While we always recommend pinning package versions for your Python requirements, it’s not always necessary to pin model revisions. Like many things in software development, it depends on your use case.

There are pros and cons to pinning a model revision:

| Pros | Cons | 
|---|---|
| Improve reliability of model performance by ensuring you’re always using the same model | Won’t automatically receive improvements to model | 
| Secure against malicious code injection | More work to set up and maintain | 

Based on these factors, we recommend pinning a model revision or copying the model to a private repository when:

- You’re using the trust\_remote\_code parameter in transformers.
- You’re evaluating a model’s performance and want to ensure the integrity of your data.
- Your application’s security requirements mandate pinning model revisions.

For more on pinning model revisions, see the [Transformers documentation on the revision parameter](https://huggingface.co/docs/transformers/main/en/model_doc/auto#transformers.AutoConfig.from_pretrained.revision) and the [Truss example for working with private models](https://truss.baseten.co/examples/09-private-huggingface).
