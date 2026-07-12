---
title: What is LLM fine-tuning?
topic: models
subtopic: fine-tuning
secondary_topics: []
summary: Overview of LLM fine-tuning concepts, when to fine-tune, and how training
  data and serving constraints affect the workflow.
source: modal
url: https://modal.com/blog/llm-fine-tuning-overview
author: null
published: '2024-12-10'
fetched: '2026-07-11T04:29:31Z'
classifier: codex
taxonomy_rev: 1
words: 2916
content_sha256: c57db1f465b5d4a6535e6920e19d0c808f1f1462abc390646518e08cf1f62f99
triage: keep
skip_reason: null
---

# What is LLM fine-tuning?

[Back](https://modal.com/blog)

# What is LLM fine-tuning?

Fine-tuning helps us get more out of pretrained large language models (LLMs) by adjusting the model weights to better fit a specific task or domain. This means you can get higher quality results than plain prompt engineering at a fraction of the cost and latency. In this post, we’ll provide a brief overview of LLM fine-tuning and how to get started with state-of-the-art techniques using Modal.

## Table of Contents

- [Why should you fine-tune an LLM?](https://modal.com#why-should-you-fine-tune-an-llm)
- [Where to fine-tune LLMs in 2025?](https://modal.com#where-to-fine-tune-llms-in-2025)
- [Top LLM fine-tuning frameworks in 2025](https://modal.com#top-llm-fine-tuning-frameworks-in-2025)
- [LLM fine-tuning on Modal](https://modal.com#llm-fine-tuning-on-modal)
- [Steps for LLM fine-tuning](https://modal.com#steps-for-llm-fine-tuning)
- [Conclusion](https://modal.com#conclusion)

## Why should you fine-tune an LLM?

### Cost benefits

Compared to prompting, fine-tuning is often far more effective and efficient for steering an LLM’s behavior. By training the model on a set of examples, you’re able to shorten your well-crafted prompt and save precious input tokens without sacrificing quality. You can also often use a much smaller model. That, in turn, translates to reduced latency and inference costs.

For example, a fine-tuned Llama 7B model can be astronomically more cost-effective (around 50 times) on a per-token basis compared to an off-the-shelf model like GPT-3.5, with comparable performance.

### Common use cases

LLM fine-tuning is especially great for emphasizing knowledge inherent in the base model, customizing the structure or tone of its responses, or teaching a model domain-specific instructions. Example use cases include:

- **Structured Output**: Generate structured data such as JSON or HTML.
- **Style Adherence**: Produce text in a distinct style, like that of The New Yorker or- [your CEO](https://github.com/modal-labs/doppel-bot).
- **Domain-specific Instruction**: Classifying corporate documents.

For tasks that require embedding additional knowledge into the base model, like
referencing corporate documents, [Retrieval Augmented Generation (RAG)](https://gpt-index.readthedocs.io/en/latest/getting_started/concepts.html) might be a more suitable technique. You may also want to combine LLM fine-tuning
with a RAG system, since fine-tuning helps save prompt tokens, opening up room
for adding input context with RAG.

## Where to fine-tune LLMs in 2025?

There are a few different options for where you can fine-tune an LLM in 2025, ranging from relatively low-code, verticalized solutions, to running open-source fine-tuning code on cloud infrastructure:

### Low-code

-  This is OpenAI’s built-in fine-tuning tool, which allows you to fine-tune its proprietary models on custom data. - pros: easy UI, existing libraries for data format validation
- cons: limited base models, expensive, don’t have control over model and weights


![openai-finetuning-ui](https://modal.com/_app/immutable/assets/openai-finetuning-ui.C61H0FCd.jpg)



-  Predibase is a low-code platform for building AI models with first class support for fine-tuning. - pros: low-code UI, supports range of open-source models, supports private deployments
- cons: not very customizable


![predibase-finetuning-ui](https://modal.com/_app/immutable/assets/predibase-finetuning-ui.DiTWsWoN.jpg)



### Configurable

The second option is to use one of the many open-source fine-tuning libraries and frameworks (see below). This gives much more control, but requires that you have somewhere to run the fine-tuning code. Some options here include:

-  Modal is a serverless cloud computing platform that makes it dead-simple for you to run your code in the cloud. Often one of the biggest headaches of fine-tuning is the infrastructure overhead, such as setting up the GPUs needed for training can be time-consuming and expensive. Modal lets you attach on-demand, pay-as-you-go GPUs with just a couple lines of code. Modal provides a simple, yet comprehensive [template](https://github.com/modal-labs/llm-finetuning/tree/main)for fine-tuning open-source LLMs on your own dataset, featuring many of the training techniques outlined below.
-  Google Colab now has a Pro tier that allows you to access more powerful GPUs for longer periods of time. This can be a good option for smaller fine-tuning tasks or for experimenting with different techniques before scaling up.
-  AWS SageMaker is a fully managed machine learning platform that provides the ability to build, train, deploy, and fine-tune models at scale.

## Top LLM fine-tuning frameworks in 2025

-  HuggingFace transformers is a popular open-source library for working with transformer-based models. It offers a high-level API for fine-tuning models on various tasks. It also provides a range of training techniques, such as distributed training, mixed-precision training, and gradient accumulation, to help optimize the fine-tuning process.
-  TRL allows users to implement a reinforcement learning loop where a model is rewarded for generating certain outputs. For example, to fine-tune a model to generate polite responses, one could set up a reward function that scores responses based on politeness and use `trl`to train the model.
-  Axolotl is an open-source library that provides a user-friendly interface for customizing fine-tuning configurations using a simple YAML file or command-line interface (CLI) overrides. It can load different dataset formats, use custom formats, or work with pre-tokenized datasets. It supports fine-tuning techniques such as full fine-tuning, LoRA (Low-Rank Adaptation), QLoRA (Quantized LoRA), ReLoRA (Residual LoRA), and GPTQ (GPT Quantization).

## Run LLM fine-tuning on Modal

For step-by-step instructions on fine-tuning LLMs on Modal, you can follow the
tutorial [here](https://modal.com/docs/examples/llm-finetuning).

## Steps for LLM fine-tuning

### 1. Choose a base model

There are myriad open-source LLMs available, each with its own strengths and weaknesses. Many of them claim to be the “best open-source LLM on the market” according to various benchmarks, but the reality is that you probably have to try multiple to determine which one is actually best for your use case. Each of these families of open-source models will typically also offer models in different sizes, for example Llama 2 7B vs. Llama 2 70B.

| Model | Description |
|---|---|
| [Llama 2](https://huggingface.co/blog/llama2) | Open-source model from Meta |
| [Pythia](https://huggingface.co/EleutherAI/pythia-12b) | Open-source model from EleutherAI |
| [Mistral](https://huggingface.co/docs/transformers/main/en/model_doc/mistral) | Open-source model from Mistral |
| [Falcon](https://huggingface.co/tiiuae/falcon-40b) | Open-source model from [TII](https://www.tii.ae/) |
| [T5](https://huggingface.co/docs/transformers/model_doc/t5) | Open-source model from Google |

In addition to these base models, there are models that have been further fine-tuned on specific datasets. For example:

| Fine-tuned Model | Base model | Description |
|---|---|---|
| [Vicuna](https://lmsys.org/blog/2023-03-30-vicuna/) | Llama | Fine-tuned on Llama on user-shared conversations collected from ShareGPT |
| [Code Llama](https://github.com/facebookresearch/codellama) | Llama 2 | Fine-tuned on Llama 2 using a higher sampling of code |
| [Alpaca](https://github.com/tatsu-lab/stanford_alpaca) | Llama | Fine-tuned on LLaMA 7B on 52K instruction-following demonstrations |
| [Dolly](https://huggingface.co/databricks/dolly-v2-12b) | Pythia 12b | Fine-tuned on a new, high-quality human generated instruction following dataset, crowdsourced among Databricks employees |
| [Flan-T5](https://huggingface.co/docs/transformers/model_doc/flan-t5) | T5 | Fine-tuned on T5 with additional instruction tasks |

It might make sense to start your LLM fine-tuning journey with one of these models that have already been fine-tuned. For example, if you’re trying to generate structured output, Code Llama may be a better base model than vanilla Llama 2 since it has already been fine-tuned to output structured output (albeit maybe not the format you want).

### 2. Prepare the dataset

The quality and relevance of the dataset to the task you want the LLM to perform is crucial for successful fine-tuning. Depending on the fine-tuning strategy and base model chosen above, you will follow different instructions to format this dataset. A common structure is a JSONL or CSV file where you can easily get a piece of data by its object key. For example:

| Input | Output |
|---|---|
| News Brief - Atlanta Airport Flight Statistics for June 2003 In June 2003, Hartsfield-Jackson Atlanta International Airport (Code: ATL) experienced a total of 30,060 flights. Out of these, 23,974 flights were on time, accounting for about 79.7% of the total flights. However, there were 5,843 flights that faced delays, with 2,160 being cancelled and 27 being diverted. | `{Airport": {"Name": "Hartsfield-Jackson Atlanta International Airport","Code": "ATL"},"Time": {"Month": "June","Year": 2003},"Statistics": {"Total Flights": 30060,"On Time Flights": 23974,"Delayed Flights": 5843,"Cancelled Flights": 2160,"Diverted Flights": 27,"On Time Percentage": 79.7}}` |

You should also create training and validation splits for your dataset to evaluate your training runs.

#### A. Create the prompt

In most cases, each sample in the dataset will have to be converted into a string prompt with instructions before we pass it into the model. Prepending an instruction in the prompt helps guide the model to generate the best output given the input. Each training example ends up looking something like this:

```
### Instruction:
You are an advanced assistant that will transform this natural language text into a tripleset.
### Input:
News Brief - Atlanta Airport Flight Statistics for June 2003
In June 2003, Hartsfield-Jackson Atlanta International Airport (Code: ATL) experienced a total of 30,060 flights. Out of these, 23,974 flights were on time, accounting for about 79.7% of the total flights. However, there were 5,843 flights that faced delays, with 2,160 being cancelled and 27 being diverted.
### Response:
{
  "Airport": {
    "Name": "Hartsfield-Jackson Atlanta International Airport",
    "Code": "ATL"
  },
  "Time": {
    "Month": "June",
    "Year": 2003
  },
  "Statistics": {
    "Total Flights": 30060,
    "On Time Flights": 23974,
    "Delayed Flights": 5843,
    "Cancelled Flights": 2160,
    "Diverted Flights": 27,
    "On Time Percentage": 79.7
  }
}
```
Note that the prompt template when running inference on a finetuned model must be the same as the one used during training for optimal results.

#### B. Add special tokens (optional)

When creating the prompt, you may potentially want to incorporate special tokens, which are symbols that have a particular meaning for the model and the task.

In the context of fine-tuning, they can be particularly useful to:

- Mark the start and end of a response.
- Separate multiple items in a list.
- Highlight specific parts of the input or output.

There are two types of special tokens:

- **Predefined Special Tokens**: Most transformer-based models come with a set of predefined special tokens. For example, Llama-2 has- `<<SYS>>`as a special token to indicate the start and end of a system prompt, and BERT uses- `[CLS]`,- `[SEP]`, etc. These tokens have special meanings and are used in specific ways during both pre-training and fine-tuning.
- **Custom Special Tokens**: If you have a specific use case that requires additional special tokens, you can define your own. For instance, in the example above,- `### Instruction:`and- `### Input:`are custom special tokens that tell the model what follows is an instruction or an input, respectively.

To use custom special tokens, you need to implement a couple additional steps:

- **Token Addition**: You’d first add these tokens to the tokenizer’s vocabulary.

```
from transformers import AutoTokenizer
tokenizer = AutoTokenizer.from_pretrained("meta-llama/Llama-2-7b-hf")
tokenizer.add_special_tokens(["### Instruction:", "### Input:"])
```
- **Model Resizing**: After adding the tokens to the tokenizer, you must resize the model’s token embeddings to account for the new tokens.

` model.resize_token_embeddings(len(tokenizer))`- **Usage**: Once added, you can use these tokens in your dataset and the model will recognize them during fine-tuning.

It’s important to note that introducing too many new tokens can dilute the embeddings space, potentially affecting the model’s performance. It’s a good idea to use custom tokens judiciously and ensure they provide meaningful information to the model.

#### C. Tokenize the prompt

Now that you have the whole string prompt for each example, you have to tokenize it. Tokenization is the process of converting a sequence of characters (like a sentence or paragraph) into a sequence of smaller units called tokens. These tokens can be as short as one character or as long as one word. One of the reasons why we had to make the model aware of the special tokens above is because we need to ensure that the tokenizer doesn’t split them into smaller sub-tokens.

For most LLM models, a specialized tokenizer is used, which often tokenizes text
into subwords or characters. This makes the tokenizer language-agnostic and
allows it to handle out-of-vocabulary words. These tokenizers also help us
include a padding and truncation strategy to handle any variation in sequence
length for our dataset. Note that part of the reason you need to specify the
tokenizer when loading a model is because each model uses a different tokenizer.
You can get around this by using `AutoTokenizer`, which automatically selects
the appropriate tokenizer for a given model.

With HuggingFace’s [transformers library](https://github.com/huggingface/transformers), using the
tokenizer will look something like:

```
from transformers import AutoTokenizer
tokenizer = AutoTokenizer.from_pretrained("meta-llama/Llama-2-7b-hf")
tokens = tokenizer.encode("ChatGPT is great!")
```
### 3. Train

After choosing a base model and preparing the dataset, it’s time to kick off the training run. Training usually involves the following steps:

- Loading the pretrained base model
- Feeding it your tokenized, instruction-based training data
- Adjusting training configuation hyperparameters like learning rate, batch size, and number of epochs
- Launching the training job and monitoring performance on your validation dataset

The length of the training run depends on a variety of factors, including the training hyperparameters as well as:

- **Size of dataset**: Larger datasets requires more time for fine-tuning.
- **Type of GPU**: More powerful GPUs can train a model faster.
- **Type of base model**: Larger models with more parameters and more complex architectures take longer to train.

Modal makes running training sweeps easy and repeatable by enabling you to [define and package your environment in code](https://modal.com/docs/guide/images), [cache your model weights](https://modal.com/docs/guide/volumes#volume-basics) for faster cold-starts, and [spawn up to 8 GPUs of any type](https://modal.com/docs/guide/gpu) for
distirbuted training (which we talk about further in the following section),
among other features.

### 4. Use advanced fine-tuning strategies

Given all of its benefits, fine-tuning an LLM can be quite time-consuming and compute-intensive upfront. There are a number of strategies for making training faster and more efficient. Here are some of the popular ones:

#### Parameter-Efficient Fine-Tuning (PEFT)

An LLM is a matrix, a table filled with numbers (weights) that determine its
behavior. Traditional fine-tuning usually involves tweaking all of these weights
slightly based on the new data. [PEFT](https://github.com/huggingface/peft) implements a number of techniques that help aims to reduce the memory
requirements while speeding up fine-tuning by freezing most of the parameters
and only training a subset of the parameters. The most popular PEFT technique is [Low-Rank Adaption (LoRA)](https://github.com/microsoft/LoRA). Instead of
tweaking the original weight matrix directly, LoRA simply updates a smaller
matrix on top, the “low-rank” adapter. This small adapter captures the essential
changes needed for the new task, while keeping the original matrix frozen. To
produce the final results, you combine the original and trained adapter weights.

Since only a small subset of the weights are updated when fine-tuning with LoRA, it is significantly faster than traditional fine-tuning. Additionally, instead of outputting a whole new model, the additional “adapter” model can be saved separately, significantly reducing the memory footprint.

#### Quantization

Quantization involves converting the floating-point numbers that represent the model’s weights and activations into integers.

For example, in 8-bit quantization, the continuous range of floating-point values is mapped to 256 discrete integer values. This can reduce the model size significantly compared to the original 32-bit floating-point representation.

[QLoRA](https://arxiv.org/abs/2305.14314) is a recently developed finetuning
approach that uses quantization to make LoRA even more memory-efficient,
enabling you to fine-tune very large models on modest hardware.

#### Distributed Training

Distributed training helps when training a model on a single GPU is too slow or the model’s weights don’t fit into a single GPU. Having multiple GPUs deal with their own fraction of the training state and data helps maximize throughput, the amount of samples we can process per time unit. There are a couple frameworks readily available to help parallelize computation across multiple GPUs:

**A. DeepSpeed**

[DeepSpeed](https://github.com/microsoft/DeepSpeed) is an open-source library
that implements [ZeRO](https://arxiv.org/abs/1910.02054), a new method to
optimize memory usage during training. ZeRO significantly improves training
speed and allows for larger models to be trained efficiently by partitioning
input data across processes while getting rid of memory redundancies that are
present in traditional data- and model-parallel training methods.

In their tests, ZeRO was able to train models with over 100 billion parameters using 400 GPUs, achieving a throughput of 15 Petaflops (a measure of computing speed).

The benefits of ZeRO/DeepSpeed are that it simplifies the training process. For instance, it can train models with up to 13 billion parameters without the need for model parallelism. This is beneficial because model parallelism can be complex and harder for researchers to implement.

**B. Fully Sharded Data Parallelism (FSDP)**

[FSDP](https://pytorch.org/blog/introducing-pytorch-fully-sharded-data-parallel-api/) helps speed up training with fewer GPUs by partitioning a model’s parameters
into shards across multiple GPUs.

For example, if a model has 1 billion parameters and you have 4 GPUs, each GPU could hold 250 million parameters. With FSDP, these parameters could be updated in parallel, and only the necessary parameters for a given forward or backward pass need to be loaded onto each GPU, reducing the overall memory footprint.

FSDP is a relatively simple and easy way to get started with distributed training. It is recommended to use FSDP if you are new to distributed parallel training, and only to use DeepSpeed if you know you will need cutting edge features that are not available with FSDP.

[Modal’s llm-finetuning guide](https://github.com/modal-labs/llm-finetuning/tree/main) implements [training with LoRA and Deepspeed](https://github.com/modal-labs/llm-finetuning/blob/main/src/train.py#L94),
and is configurable with many other SOTA techniques.

**C.  accelerate**

`accelerate` simplifies the process of running models on multiple GPUs or CPUs,
without requiring a deep understanding of distributed computing principles.

## Conclusion

Fine-tuning an LLM allows you to customize existing general-purpose models for your specific use case.

To make your LLM fine-tuning job more efficient, consider leveraging techniques
like LoRA or model sharding (using frameworks like Deepspeed). Modal’s [fine-tuning template](https://github.com/modal-labs/llm-finetuning/tree/main) implements many of these techniques out of the box, allowing you to quickly spin
up distributed training jobs in the cloud.

By fine-tuning an open-source model like Llama 2 or Mistral on Modal, you can obtain a customized model that excels at your particular use case, at a fraction of the cost and latency of off-the-shelf API services.
