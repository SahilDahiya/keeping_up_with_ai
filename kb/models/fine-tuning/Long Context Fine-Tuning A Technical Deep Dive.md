---
title: 'Long Context Fine-Tuning: A Technical Deep Dive'
topic: models
subtopic: fine-tuning
secondary_topics:
- prompt-engineering/context-engineering
summary: Technical deep dive into long-context fine-tuning.
source: together
url: https://www.together.ai/blog/long-context-fine-tuning-a-technical-deep-dive
author: George Grigorev; Zain Hasan; Max Ryabinin
published: '2024-11-25'
fetched: '2026-07-11T04:24:16Z'
classifier: codex
taxonomy_rev: 1
words: 1422
content_sha256: f4f77250eeff736cf582e204a3a35f87e3b7564a49b22e6fd9aef6c0193f3ec9
triage: keep
skip_reason: null
---

# Long Context Fine-Tuning: A Technical Deep Dive

The landscape of Large Language Models (LLMs) is rapidly evolving, with context lengths expanding from a few thousand tokens a year ago to millions of tokens now. This increase in context length has very real implications for enterprise applications, particularly in Retrieval Augmented Generation (RAG), document analysis, and summarization systems. While prior models were limited to processing a few pages of text, modern models like Meta's Llama 3.2 series can handle 131K tokens, which is the equivalent of a 200-page novel.

This capability is very useful when working with enterprise data. Traditional RAG systems often require complex chunking and re-ranking strategies to work within context constraints. However, with extended context lengths, organizations can now process entire documents or multiple documents simultaneously, potentially simplifying architectures while improving accuracy. These advancements are particularly valuable when you're working with:

- Enterprise document RAG systems
- Multi-document question answering
- Code repository understanding and generation
- Financial report processing and summarization
- Complex tool and API interactions for agentic systems

The problem, however, lies in implementing reliable and performant long context systems, which isn't as straightforward as simply using LLMs that have a higher theoretical context limit. Recent work shows that most models show degraded performance for context length thresholds much smaller then the maximum quoted context length for the model. For example, let's assume you're using a model with a maximum context length of 131k, try passing it any random sequence of 90,000 tokens and ask it to repeat back to you **the last 100 words** in the sequence. You'll find that the LLM has problems with this simple regurgitation task!

This is a problem since currently, extended context length capabilities are primarily available in frontier models that come with significant usage costs. To enhance performance for long context length tasks, you need to teach the model how to effectively use and perform with long sequences. With the latest updates, the Together AI platform now supports fine-tuning on context lengths as large as 32k tokens, with longer sequence lengths to follow. By fine-tuning smaller models to handle longer contexts, organizations can achieve comparable performance at a fraction of the cost. This approach is particularly valuable for enterprise applications, where data privacy and ownership are crucial considerations.

Long context fine-tuning is quite different from regular fine-tuning and presents its own challenges, let's discuss them below! In this technical deep dive, we'll explore and demonstrate:

- Problems that LLMs have working with long sequences
- The solution: fine-tuning on long sequences
- Practical problems of long context fine-tuning and how we solved them
- Real-world example + code: improving the summarization capabilities of Llama 3.2 8B

If you would like to dive into code directly, please refer to the notebooks below:

- [Notebook 1](https://github.com/togethercomputer/together-cookbook/blob/main/LongContext_Finetuning_RepetitionTask.ipynb): We show how LLMs have a problem with simple repetition tasks when it comes to long-context inputs and how we can solve it.
- [Notebook 2](https://github.com/togethercomputer/together-cookbook/blob/main/Summarization_LongContext_Finetuning.ipynb): We show how you can improve the summarization capabilities of Llama 3.2 8B by fine-tuning.

**Demonstrating the Long Context Problem**

A recent [paper](https://arxiv.org/abs/2411.03538v1) showed diminishing returns when models are prompted with sequences longer than their optimal threshold. For example, in case of Llama 3.1 405B this threshold was after 32K tokens. The graph below from this paper shows which models degrade after a certain optimal token length:

![](https://cdn.prod.website-files.com/69654e88dce9154b5f12070c/699e0b0e7502e34eca681550_6744a3643a21ffa430247f03_AD_4nXeaWIapE4vFHDkPM8V0nbMyxB7W-HyPJ0YUUIU0AbhARJtQyEPNHZ0-irbNnUL6VU4AQ7XIU10hMajelzgifbbNUQ0BIGvy9B65k1AO5on1Z-fq6dXbtbmFdLDqAv--_eaTeyzOhA.png)

They discovered the main problems these models faced when dealing with long-context sequences:

1. [The "Lost in the Middle" Problem](https://arxiv.org/abs/2307.03172)

Models struggle with information in middle sections, and the performance degradation increases with the context length. The ability to retrieve information becomes less reliable in the middle of the context.

2. Effective Context Length Limitations

Research from the [RULER paper](https://arxiv.org/abs/2404.06654) shows that the usable context length often falls short of advertised maximums. In reality, the effective length varies by task type, and the performance begins to decrease well before reaching the length limit. Interestingly, they also found that different tasks have different optimal context lengths.

These findings suggest an important consideration for practitioners: you can't just use the maximum available length and need to experiment to find the optimal length for your task, which may vary from model to model!

**Simple Repetition Task**

To do a simple demonstration of this performance degradation, we conduct a toy experiment:

We ask an LLM to repeat back to us the last `k` words in a provided sequence.

![](https://cdn.prod.website-files.com/69654e88dce9154b5f12070c/699e0b0e7502e34eca681553_6744a3643119ce18f8bbf5b3_AD_4nXco_KUhlX5tpJXuMy5XY99qxSvGp1XAhmh-sd08MiIZWuj4LERE55YDKJ7nL0QKN3iabgt-mEcvUJR9Cwsrm8SwrtFt_IPF0H9xBS_SkZbxvfVtzedUQ0Ei9swYttQs2DkH19En9A.png)

To solve this repetition task, an LLM should be able to use a simple induction head that just copies a specific part of the input. For more information, you can read extensive research by Anthropic on [visualizing induction heads](https://transformer-circuits.pub/2022/in-context-learning-and-induction-heads/index.html#copying-literal-text). An induction head is a key component in Transformer models that identifies repeated sequences and uses previous occurrences to predict what comes next. This capability is fundamental to how Transformers process language, enabling them to learn from repetition and make predictions based on previously seen patterns.

For the detailed analysis, please refer to the complete [notebook here](https://github.com/togethercomputer/together-cookbook/blob/main/LongContext_Finetuning_RepetitionTask.ipynb). In short, we demonstrate that an untuned Llama 3.1 70B model performs suboptimally on this task (with a Levenshtein Distance ratio of 0.37), and by fine-tuning on just 2000 long-context examples, we can get an 8B model to perform this task at almost perfect accuracy(Levenshtein Distance ratio of 0.81).

| Model Type | Levenshtein Ratio | Length Difference |
|---|---|---|
| Baseline - Llama 3.1 8B | 0.37 | 103.44 |
| Fine-tuned - Llama 3.1 8B | 0.81 | 15.08 |

Let's examine the challenges you might run into when trying to perform long context fine-tuning and their practical solutions.

**Technical Challenges of Long Context Fine-tuning**

During training, LLMs need to maintain a significant amount of intermediate data, such as weights, gradients, and optimizer states, in GPU memory. Each token in the input sequence requires multiple vectors for activations at every layer of the model. As the context length increases, this memory requirement grows linearly, quickly consuming available VRAM. A model processing 64K tokens needs 64 times more activation memory than one processing 1K tokens, making it challenging to fit these intermediate results in GPU memory even on high-end hardware. Distributed training can help scale large model training across multiple GPUs, but the most common methods typically reduce the footprint of model parameters, optimizer states or large intermediate states. However, the main memory bottleneck in long-context training comes from storing activations for a single sample. Even with multiple GPUs, you are still limited by the memory required to process your longest individual sequence.


To address these challenges, the research community has proposed several methods to make long-context training feasible and efficient. We use sequence-parallel training with a distributed attention algorithm that is highly scalable and allows for efficient training on any context length, exactly matching the standard attention mechanism in terms of outputs. This works in conjunction with gradient checkpointing, which strategically saves intermediate results at specific layers and recomputes others as needed during backpropagation, trading some computation time for substantial memory savings. 

**Improving Long Context Summarization with Fine-Tuning**

An important use case for LLMs is summarization, where we can pass large documents into the context window of the model and prompt it to generate comprehensive summaries of those documents.

For most LLMs, this works quite well in the case of documents below the cumulative size of 32,000 tokens. However, depending on the model and its post-training context length, the summarization performance for longer documents can be quite poor.

![Diagram showing a long text passage input to an LLM that produces a summary output.](https://cdn.prod.website-files.com/69654e88dce9154b5f12070c/699e0b0e7502e34eca68154d_6744a3662096c8eab9317f7c_AD_4nXdbZDnzq9uv1anPAVrPS3isTOCQ2Dw8G-t-6JfmMI7CwNVe9TLHDKdC3nNUCHqtx20hMHMaw3v4fasDBUJGLh2h5VjucXrY2kMqqLoIsvGNH4uygCQeBvE4qwF-lr3762QuFcL9.png)

For this task, we designed a simple synthetic dataset using long documents from the RedPajama dataset and the predictions from a mixture of LLMs as a target.

We demonstrate a ~10% improvement in summarization capabilities of Llama 3.1 8B after fine-tuning on our own synthetic dataset along with the [GovReport](https://gov-report-data.github.io/) long document summarization dataset, compared to an untuned Llama 3.1 70B model.

Here are the results of our experiments:

Synthetic Data fine-tuning:

| Model Type | ROUGE-L |
|---|---|
| Synthetic data 70B - Baseline | 21.56 |
| Synthetic data 8B - Fine-tune | 23.55 |

GovReport fine-tuning:

| Model Type | ROUGE-L |
|---|---|
| GovReport 70B - Baseline | 21.66 |
| GovReport Fine-tune | 24.05 |

For the detailed analysis, please refer to the complete [notebook here](https://github.com/togethercomputer/together-cookbook/blob/main/Summarization_LongContext_Finetuning.ipynb).

**Conclusion**

Long context fine-tuning represents a significant advance in LLM capabilities, but requires a careful implementation for correctness and efficiency. Using Together AI, it is now possible to achieve better performance at extended sequence lengths by fine-tuning models on your long-context data.
