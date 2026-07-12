---
title: 'Continued Fine-tuning of LLMs: A Technical Deep Dive'
topic: models
subtopic: fine-tuning
secondary_topics: []
summary: Technical deep dive into continued fine-tuning of LLMs.
source: together
url: https://www.together.ai/blog/continued-fine-tuning
author: Artem Chumachenko; Zain Hasan; Max Ryabinin
published: '2025-04-17'
fetched: '2026-07-11T04:22:53Z'
classifier: codex
taxonomy_rev: 1
words: 1216
content_sha256: c18cec23a3dd4b8fb9efbc477029eb2c7fd35fbda0300079b32c5ff299d7fc7d
triage: keep
skip_reason: null
---

# Continued Fine-tuning of LLMs: A Technical Deep Dive

Keeping large language models updated with new knowledge and skills relevant to businesses remains challenging. Today, we announce a new feature of the Together Fine-Tuning Platform: continued fine-tuning. Simply stated, this feature allows you to build upon previously trained models by specifying the `--from-checkpoint` parameter, in which case fine-tuning will start from the previously specified checkpoint.

In this deep-dive blogpost, we'll explore the ins and outs of continued fine-tuning, when to use it, and its most powerful applications.

If you’d like to jump right into the code, we’ve prepared an in-depth [code notebook here](https://github.com/togethercomputer/together-cookbook/blob/main/Finetuning/Continual_Finetuning.ipynb).

**Introduction**

Continued fine-tuning (CFT) refers to the process of sequentially fine-tuning an LLM that has already undergone previous training. Unlike starting from scratch with a base model, continued fine-tuning builds upon the knowledge and capabilities that a model has already acquired, enabling more efficient adaptation to new tasks, domains, or languages.

The role of continued fine-tuning in the LLM lifecycle is crucial - if you have ever fine-tuned a model, you probably performed some form of CFT. Typically, people will continue the supervised finetuning of instruct model checkpoints that the model creators have released. As models evolve, CFT offers a resource-efficient way to adapt them to new use cases while minimizing the loss of their previously learned capabilities (also known as catastrophic forgetting) - more on this later!

**Understanding Continual Learning in LLMs**

Continual learning in LLMs can be broadly categorized into continued pre-training (CPT) and continued fine-tuning (CFT). CPT focuses on further training a base pre-trained LLM on a large corpus of domain-specific text documents. This augments the model’s general knowledge with specific information from the particular domain. CFT, on the other hand, involves instruction-tuning the LLM on successive downstream tasks with varying data distributions or time shifts. This dataset often contains labeled input-output pairs, such as questions and answers, to align the model’s behavior to perform a specific, well-defined task.

CFT encompasses several approaches, including fine-tuning for different tasks, instruction tuning, model refinement/editing, and alignment. Recent research has also explored using CFT to enhance the multilingual capabilities of LLMs.

One of the most significant challenges in continued fine-tuning is catastrophic forgetting, when a model's performance on previous tasks deteriorates when it's fine-tuned on new data. [Previous work](https://arxiv.org/abs/2410.16006) demonstrates that the similarity between datasets used in different phases of fine-tuning significantly impacts how well the model retains its previous capabilities.

When phase-wise datasets encode similar tasks, the model maintains or even improves its performance on previous tasks. However, when datasets encode different tasks, the model's performance on previous tasks can decline significantly. This finding is crucial for designing effective continued fine-tuning strategies.

**When to Use Continued Fine-tuning**

Continued fine-tuning is particularly valuable in several scenarios:

- **When you've already fine-tuned a model and want to further improve it without starting over**: This is especially useful when you've invested significant resources in training a model and need to adapt it to new data or tasks.
- **When you need to adapt a model to new languages**: If you have an English-proficient model and want to extend its capabilities to other languages without compromising its performance in English.
- **When your data distribution shifts over time**: For models deployed in production environments where the types of queries or user behaviors evolve.
- **When you want to incorporate new knowledge or skills incrementally**: Rather than retraining from scratch, continued fine-tuning allows for more efficient knowledge acquisition.
- **Stacking SFT with DPO - when you need to align a model with human preferences**: After collecting user feedback, you can further fine-tune a model to better align with how users expect it to respond. See our- [in depth notebook](https://github.com/togethercomputer/together-cookbook/blob/main/Finetuning/DPO_Finetuning.ipynb)on how to do this.

Some key factors to consider before implementing continued fine-tuning include:

- **Dataset similarity**: How similar is your new dataset to what the model was previously trained on? High similarity generally leads to better knowledge retention.
- **Learning rate and training duration**: These hyperparameters are critical for successful continued fine-tuning and may need to be adjusted based on your specific model and dataset.
- **Performance metrics**: Clear definition of what success looks like, both in terms of new capabilities and retention of previous skills. You can have evaluation of all capabilities in addition to the capabilities that are being improved in the current CFT step.

**Real-world Use Cases**

**Multilingual Adaptation**

One of the most promising applications of continued fine-tuning is enhancing a model's ability to understand and generate text in multiple languages. Previous work has demonstrated that CFT can be used to adapt models to new languages without diminishing their performance in languages they already understand.

Traditional approaches often lead to catastrophic forgetting, where a model's performance in its original language (usually English) deteriorates as it learns new languages. However, recent studies show that with the right techniques—such as using similar task datasets across languages—models can maintain their original language proficiency while gaining new language abilities.

For example, a two-phase CFT process where an English-only fine-tuned LLM is sequentially fine-tuned on a multilingual dataset can enhance the model's language abilities without sacrificing its task performance, especially when the datasets encode similar tasks.

**Task-specific Performance Improvement**

Continued fine-tuning can significantly improve a model's performance on specific tasks. This [AWS blogpost](https://aws.amazon.com/blogs/machine-learning/llm-continuous-self-instruct-fine-tuning-framework-powered-by-a-compound-ai-system-on-amazon-sagemaker/) discusses a continuous self-instruct fine-tuning framework that uses a compound AI system to drive the fine-tuning workflow for performance improvement.

Their benchmarking results showed that custom LLMs trained through Supervised Fine-Tuning (SFT) yielded higher accuracy than standard RAG systems, and models further refined through preference alignment (like DPO) showed even greater improvements.

**Preference Alignment and Model Refinement**

Finally, continued fine-tuning is very useful for aligning models with human preferences. After collecting user feedback, you can use techniques like Direct Preference Optimization (DPO) to fine-tune models to better match user expectations. Read our deep-dive on [preference tuning using DPO](https://www.together.ai/blog/direct-preference-optimization).

AWS's implementation demonstrated that fine-tuned models through preference alignment from human and AI feedback significantly outperformed standard RAG pipelines, even when using smaller base models.

To learn more about how to effectively stack continued fine-tuning with preference tuning with DPO, read our [other technical deepdive on DPO](https://www.together.ai/blog/direct-preference-optimization).

**Getting Started with CFT on Together**

**Technical Approaches and Best Practices**

To implement continued fine-tuning effectively, you can specify the --from-checkpoint parameter in our fine-tuning API as follows:

```

```
```
      together fine-tuning create \
        --training-file "file-5e32a8e6-72b3-485d-ab76-71a73d9e1f5b" \
        --from-checkpoint "ft-bb62e747-b8fc-49a3-985c-f32f7cc6bb04" \
        --wandb-api-key $WANDB_API_KEY  # Optional

```
You can also use the Python or TypeScript clients:

```

```
```
      import os
      from together import Together
      client = Together(api_key=os.environ.get("TOGETHER_API_KEY"))
      response = client.fine_tuning.create(
        training_file = 'file-5e32a8e6-72b3-485d-ab76-71a73d9e1f5b',
        from_checkpoint = 'ft-bb62e747-b8fc-49a3-985c-f32f7cc6bb04',
        wandb_api_key = '1a2b3c4d5e.......',
      )
      print(response)

```
A checkpoint can be specified using:

- The output model name from the previous job
- The fine-tuning job identifier
- A specific checkpoint step with format `ft-...:{STEP_NUM}`

To check all available checkpoints for a job, use together fine-tuning list-checkpoints {FT_ID}. To check all available checkpoints for a job, use `together fine-tuning list-checkpoints {FT_ID}`.

Continued fine-tuning represents a powerful approach to evolving and improving LLMs over time. By building upon previously trained models rather than starting from scratch, you can more efficiently adapt models to new tasks, domains, and languages while preserving their existing capabilities.

Check out the in-depth [code notebook](https://github.com/togethercomputer/together-cookbook/tree/main/Finetuning/Continual_Finetuning.ipynb) for an example of how to apply continual fine-tuning to improve function calling and our [docs here](https://docs.together.ai/docs/fine-tuning-quickstart).
