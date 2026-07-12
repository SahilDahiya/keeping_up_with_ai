---
title: 'Fine-Tuning LLMs for Multi-Turn Conversations: A Technical Deep Dive'
topic: models
subtopic: fine-tuning
secondary_topics:
- agents/planning
summary: Technical deep dive into fine-tuning LLMs for multi-turn conversations.
source: together
url: https://www.together.ai/blog/fine-tuning-llms-for-multi-turn-conversations-a-technical-deep-dive
author: Artem Chumachenko; Zain Hasan; Max Ryabinin
published: '2024-11-25'
fetched: '2026-07-11T04:23:21Z'
classifier: codex
taxonomy_rev: 1
words: 1440
content_sha256: c15acfea9c763370c68bbf1a73ea0b9f59a534c879ea4e869fe232d30f08252a
triage: keep
skip_reason: null
---

# Fine-Tuning LLMs for Multi-Turn Conversations: A Technical Deep Dive

Large Language Models (LLMs) have revolutionized how we interact with and build conversational AI systems. While these models demonstrate impressive capabilities out of the box in general conversation, organizations face significant challenges when attempting to apply them to domain-specific business contexts.

Despite their broad capabilities, general-purpose LLMs face several key limitations:

- Domain Adaptation: Organizations often struggle with getting LLMs to understand their unique data formats and specific user interaction patterns.
- Knowledge Constraints: Base models have knowledge cutoffs and may lack specialized domain expertise and access to private enterprise documents.
- Multi-Turn Complexity: While base models handle single exchanges well, maintaining context and coherence across nuanced multistep conversations requires further specialized post-training.

This is where fine-tuning on your own data comes to the rescue.

**Why Fine-Tuning Matters**

Fine-tuning offers a solution to these challenges by allowing organizations to adapt off-the-shelf open models to their specific needs. Unlike pre-training, which involves processing vast amounts of low-quality general data, fine-tuning an already instruction-finetuned model is a more focused process that requires a much smaller, higher-quality labeled dataset of domain-specific examples.

In this article, we'll talk specifically about multi-turn fine-tuning, whereby we can teach the model to maintain context across multiple exchanges while adhering to specific conversation patterns. The process helps models handle domain-specific queries with greater accuracy and ensures they respect guardrails that may be unique to your business context. This multi-turn capability is especially critical in scenarios like customer service, technical support, or complex multi-hop task completion, where a single exchange is rarely sufficient to address the user's needs.

Another practical example of multi-turn finetuning is the multi-turn function calling workflow. If you need an LLM to solve complex problems by using tools, you will need to train it to identify which sequence of tools to use one after the other and make decisions depending on the information obtained from the intermediate tool usage.

In this hands-on walkthrough, we will discuss the complete process of fine-tuning LLMs for multi-turn conversations. We'll cover:

- Multi-turn conversation dataset preparation
- Loss masking in instruction tuning
- Example fine-tuning Llama 8B on a conversational dataset

We'll explore both theoretical concepts and practical implementation details, helping you create conversational AI systems that align with your organization's needs. Whether you're building a customer service bot that needs to maintain context across multiple interactions, or developing a specialized assistant that handles complex multi-step processes, understanding how to properly fine-tune LLMs for multi-turn conversations is critical.

If you would like to dive into code directly, please refer to the [code notebook here.](https://github.com/togethercomputer/together-cookbook/blob/main/Multiturn_Conversation_Finetuning.ipynb)

**Dataset Preparation**

The most important and hardest part of successfully fine-tuning an LLM is proper dataset preparation. Thanks to services such as the Together Fine-Tuning API, the fine-tuning itself is now much easier than obtaining and preparing data that's worth fine-tuning on! For multi-turn conversations, we need to structure our data to capture the back-and-forth nature of dialogue while ensuring the model learns to generate appropriate responses rather than memorizing entire conversations.

Key aspects of the dataset preparation:

- Proper conversation structure with clear turn delineation
- System messages to set the context
- Consistent role labeling (User/Assistant)
- JSONL format compatible with common fine-tuning frameworks

The dataset needs to be prepared using the chat format where every example in the JSONL file should be a list of "messages", and every message must have a "role" and "content". The "role" should be either "system", "user", or "assistant". You can read more about the format in our [docs](https://docs.together.ai/docs/fine-tuning-data-preparation#conversational-data).

Once you have your dataset in the above format, we can upload the `.jsonl` to Together AI as shown below. Before uploading the dataset, we will also check the file to make sure it was formatted and prepared correctly.

**Loss Masking in Instruction Fine-Tuning**

A critical consideration when fine-tuning LLMs for conversational tasks is how to handle loss computation during training. Traditionally, many practitioners have followed the practice of masking instructions when calculating the loss function, but [recent research](https://arxiv.org/abs/2405.14394) suggests this might not always be optimal.

Loss masking in instruction fine-tuning refers to the practice of selectively including or excluding certain parts of the input when computing the training loss. There are typically three approaches:

- **No Instruction Masking**: The default approach where the loss is computed on all tokens, including both instructions and responses.
- **Full Instruction Masking**: The currently common approach where the loss is only computed on the response tokens, masking out all instruction tokens.
- **Boilerplate Masking**: A hybrid approach where only repetitive template text (like "Below is an instruction...") is masked while keeping both the instruction and the response content.

![](https://cdn.prod.website-files.com/69654e88dce9154b5f12070c/699e0b05f155c3d4868246f7_6744a0183119ce18f8b900d4_AD_4nXfGnoqppJC14BKnA1rBKJjSBD-JytvxYBYp1m1ssJ5MGtlhV2DPH2VzzGwqU9ReFxRby4mNVlZaHtttyB93LLGP499ORYiglkGcYmt3q3EnuGkpcouUaeNZQYx0tlHCcMYmjhZo.png)

[Source](https://magazine.sebastianraschka.com/p/llm-research-insights-instruction)

In the "[Instruction Tuning With Loss Over Instructions](https://arxiv.org/abs/2405.14394)" paper, authors challenged the conventional wisdom and showed that not masking instructions (except for special tokens) often leads to better model performance compared to the traditional masking approach. However, the effectiveness of this strategy isn't universal: it depends heavily on two key dataset characteristics, namely the ratio between instruction and response lengths and the overall size of the training dataset. These findings suggest that practitioners should carefully consider their specific use case and dataset properties when deciding on a masking strategy, rather than default to full instruction masking.

With the introduction of this new feature to the Together Fine-Tuning API, you can now select if you want loss masking to be performed for your fine-tuning job. The `train_on_inputs` parameter is newly introduced and allows:

- Enabling loss masking for a fine-tuning job by setting it to `False`;
- Disabling loss masking, the loss will be calculated on all tokens, by setting it to `True`;
- You may also set this to `"auto"`, which will enable/disable loss masking depending on the input dataset format.

To learn more about loss masking, please refer to our [docs](https://docs.together.ai/docs/fine-tuning-overview#loss-masking).

**Real-World Example of Conversation Data Fine-tuning**

In this section, we demonstrate how you can train your LLM to carry longer form discussions better by fine-tuning it on multi-step conversational data.

[CoQA](https://huggingface.co/datasets/stanfordnlp/coqa/tree/main) is a large-scale dataset for building Conversational Question Answering systems. The goal of the CoQA challenge is to measure the ability of machines to understand a text passage and answer a series of interconnected questions that appear in a conversation.

CoQA contains 127,000+ questions with answers collected from 8000+ conversations. Each conversation is collected by pairing two crowdworkers to chat about a passage in the form of questions and answers. CoQA has a lot of challenging phenomena not present in existing reading comprehension datasets, e.g., coreference and pragmatic reasoning.


![](https://cdn.prod.website-files.com/69654e88dce9154b5f12070c/699e0b05f155c3d4868246e8_6744a0a37714a7f24590c370_AD_4nXd6cypThM97XlOanEY22AG8YMiF2Ux1fpLgXGAcFqts2CQDOpQIiw_7_k2pA8CoxHiiVmhacCC_BaGx3-xNYOaCjKPYy_F-qTtzmZ7poW8fmuhyz-rpyyM9tSjff4cyiTnmNGfk.png)

The code below demonstrates how to convert the CoQA dataset to the conversational format expected by the Together Fine-Tuning API.


`Create a fine-tuning job:`

Once the job is launched, you'll be able to see and track it on the [dashboard](https://api.together.ai/jobs):

![](https://cdn.prod.website-files.com/69654e88dce9154b5f12070c/699e0b05f155c3d4868246f2_6744a0a30fa389b823036311_AD_4nXfurbfhNmtjZmyT47_ksdEqneYS3i3J8ik27JwNA3jp_91qojraEV1M4vsFVCBBoXAoWz7vzahSJbtb9-AwERHbcgA8xEu_d-_n7-eZHfGYwv_MsX4QsKx2XkYVUuDc2guiMe7tZA.png)

Once the fine-tuning job is completed, you'll be able to see the model on the [job page](https://api.together.ai/jobs):

![](https://cdn.prod.website-files.com/69654e88dce9154b5f12070c/699e0b05f155c3d4868246e5_6744a0a386754b80ca4ca1db_AD_4nXe6RWwKT7M7j0lxcIFiI93ZJEKxqF0bRKHSsZmfcSspgffceCXRXUrZselmdZJLxf5fRnxWodvFmRlo8rTB1MrWpQ6h9CCM3OL0dsqzUy6zRP9TxBCqfxUkQmxGNDizIWE-1CiU.png)

**Evaluating Performance**

Once the model is fine-tuned, we can compare performance improvements on the CoQA validation set. For evaluation, CoQA uses two metrics: F1 score, which measures word overlap between predicted and ground truth answers, and Exact Match (EM), which requires the prediction to exactly match one of the ground truth answers. F1 is the primary metric, as it better handles free-form answers by giving partial credit for partially correct responses.

Below, you can see an example implementation of computing evaluation metrics on Together AI's platform:

**Deploy Model and Run Evals**

Before we can run the evaluations, we need to deploy our fine-tuned model as a Dedicated Endpoint. Access your model through the Together AI dashboard. Go to Models, select your fine-tuned model, and click Deploy. Choose from the available hardware options; we'll use a single A100-80GB GPU for this example.

![Together.ai page showing fine-tuned Meta Llama 3.1 8B Instruct model details and deployment pricing.](https://cdn.prod.website-files.com/69654e88dce9154b5f12070c/699e0b05f155c3d4868246ef_6744a0a31cd18c4f698033a4_AD_4nXf-xDZTvTBMYvCThRF73fPml5QgBkDYf0jLKnFQkq_O8Ebz9toKT7Fw4xrmKqWKF4fdxgMCSWtyq9TSmqgVlzkfFyk-qFNcqrvs4NMTua07zF-7I_merVIntJ3YiFDikYMeWSbe5A.png)


We can now loop over models and obtain evaluation metrics:

For the evaluation above, we saw a marked improvement in Llama 3.1's ability to address conversational questions. The exact match score increases ~12x, and the F1 score goes up ~3x after fine-tuning.

| Model Version | EM | F1 |
|---|---|---|
| Original | 0.043 | 0.232 |
| Fine-tuned | 0.62 | 0.78 |

**Conclusion**

Fine-tuning LLMs for multi-turn conversations requires careful attention to dataset preparation, training implementation, and evaluation. By following these best practices, you can create effective conversational models while managing computational resources efficiently.

For optimal results:

- Start with high-quality conversation data
- Implement proper input masking
- Use parameter-efficient fine-tuning methods
- Monitor and evaluate throughout the process

Together Fine-Tuning API allows you to handle all the steps of fine-tuning — get started now by checking the [docs here](https://docs.together.ai/docs/fine-tuning-overview).
