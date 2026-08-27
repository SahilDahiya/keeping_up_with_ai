---
title: Training and Finetuning Multi-Vector Embedding Models with Sentence Transformers
kind: blog
topic: rag-retrieval
subtopic: embeddings
secondary_topics:
- models/fine-tuning
summary: Walks through finetuning ColBERT-style multi-vector (late-interaction) embedding
  models using Sentence Transformers' new MultiVectorEncoder, covering datasets, loss
  functions, training arguments, and evaluators, and shows a model finetuned in 14.5
  hours on a single RTX 3090 beating general-purpose dense, sparse, lexical, and multi-vector
  retrievers on a medical retrieval benchmark (MIRIAD NDCG@10).
triage: null
skip_reason: null
source: huggingface
url: https://huggingface.co/blog/train-multi-vector-encoder
author: Tom Aarsen
published: '2026-08-26'
fetched: '2026-08-27T09:08:03Z'
classifier: claude
taxonomy_rev: 2
words: 5113
content_sha256: 28314b5e115f9604e63f479c0c00eb406636d84621108dc9621b107d9abee328
---

# Training and Finetuning Multi-Vector Embedding Models with Sentence Transformers

[Sentence Similarity •  0.1B • Updated   •  205k  •  201](https://huggingface.co/Alibaba-NLP/gte-modernbert-base)  

#### Alibaba-NLP/gte-modernbert-base

![](https://cdn-avatars.huggingface.co/v1/production/uploads/63fc4c00a3c067e62899d32b/dfd_EcIfylvu3sdc2WMqX.png) 

Published
					August 26, 2026 

  Upvote 

 38

`MultiVectorEncoder`, for ColBERT-style late interaction retrieval, alongside a complete training approach for it. In this blogpost, I'll show you how to use it to finetune a multi-vector model that outperforms general-purpose retrievers on your data. This method can also train strong new multi-vector models from scratch. Everything below runs on `pip install -U "sentence-transformers[train]"`.
Finetuning multi-vector models involves several components: the model itself, datasets, loss functions, training arguments, evaluators, and the trainer class. I'll have a look at each of these components, accompanied by practical examples of how they can be used for finetuning strong multi-vector models.

Lastly, in the [Evaluation](https://huggingface.co#evaluation) section, I'll show you that my finetuned [multi-vector-encoder/mLateOn-medical](https://huggingface.co/multi-vector-encoder/mLateOn-medical) model, trained in 14.5 hours on a single RTX 3090 alongside this blogpost, easily outperforms every general-purpose retrieval model I could find on my medical retrieval evaluation: dense, sparse, lexical, and multi-vector alike.

![NDCG@10 on MIRIAD versus active parameters: the finetuned mLateOn-medical reaches the top at a fraction of the size of the strongest general-purpose models](https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/blog/train-multi-vector-encoder/mve_medical_model_size_ndcg.png)


If you're interested in finetuning dense embedding models, sparse embedding models, or rerankers instead, then consider reading through my prior [Training and Finetuning Embedding Models](https://huggingface.co/blog/train-sentence-transformers), [Training and Finetuning Sparse Embedding Models](https://huggingface.co/blog/train-sparse-encoder), and [Training and Finetuning Reranker Models](https://huggingface.co/blog/train-reranker) blogposts.

This blogpost is about *training* multi-vector models. If you want to learn how to *use* them, from loading and encoding to indexing in vector databases, see the companion [Multi-Vector (Late Interaction) Embedding Models with Sentence Transformers](https://huggingface.co/blog/multi-vector-encoder) blogpost.


A dense embedding model compresses a whole text into a single vector, and similarity is one dot product between two such summaries. A multi-vector model (also called a late-interaction or ColBERT-style model) skips that compression. It keeps **one small vector per token** and scores a query against a document with the MaxSim operator, where every query token finds its best-matching document token and the scores are summed. Token-level matching preserves exactly the fine-grained signals that a single vector has to average away, which usually means stronger retrieval, at the cost of a bigger index.

The companion [Multi-Vector Embedding Models](https://huggingface.co/blog/multi-vector-encoder) blogpost covers the architecture, encoding, scoring, and indexing in detail, so I'll keep this section short and get to the training.

![Dense embedding versus multi-vector late interaction](https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/blog/multi-vector-encoder/maxsim_explainer.gif)


Finetuning multi-vector models significantly improves their retrieval performance on your specific domain: the vocabulary, the query style, and the notion of relevance all differ between web search, legal discovery, code search, and scientific literature review. Because queries and documents are matched token by token, multi-vector models pick up fine-grained domain signals that single-vector models tend to average away, and they respond very well to even modest amounts of in-domain finetuning data.

Beyond that, most released retrieval models were configured for short passages. The classic ColBERT checkpoints truncate documents at 180 or 300 tokens, and many popular dense models at 256 or 512, because their MS MARCO-style training data rarely goes beyond that. If your documents are long, these models silently discard most of every document before scoring it. On my medical evaluation with passages averaging 941 tokens, I measured that this truncation costs up to 0.24 NDCG@10, considerably more than any difference between model architectures. When you train your own model, you configure the document length that *your* data needs.

LightOn ran into this same dynamic with code retrieval, where general [LateOn](https://huggingface.co/lightonai/LateOn) wasn't enough and they trained [LateOn-Code](https://huggingface.co/lightonai/LateOn-Code). Your domain, whether that's medical, legal, financial, or your company's internal documents, is not getting an official model. This blogpost shows you how to build it yourself, in a matter of hours, on a single consumer GPU.

Training MultiVectorEncoder models involves the following components:

1. [**Model**](https://huggingface.co#model) : The model to finetune or the architecture to build fresh.
2. [**Dataset**](https://huggingface.co#dataset) : The data used for training and evaluation.
3. [**Loss Function**](https://huggingface.co#loss-function) : A function that measures the model's performance and guides the optimization process.
4. [**Training Arguments**](https://huggingface.co#training-arguments) (optional): Parameters that impact training performance, tracking, and debugging.
5. [**Evaluator**](https://huggingface.co#evaluator) (optional): A class for evaluating the model before, during, or after training.
6. [**Trainer**](https://huggingface.co#trainer) : Brings together all training components.

Let's take a closer look at each component.

Multi-vector training gives you a real choice of starting point, and it matters more than you might expect.

If you want to further finetune an existing multi-vector model, you don't have to worry about the architecture at all:

```
from sentence_transformers import MultiVectorEncoder
# Loading in fp32 is preferred for training if your memory can handle it
model = MultiVectorEncoder(
    "lightonai/mLateOn-unsupervised",
    model_kwargs={"torch_dtype": "float32"},
    processor_kwargs={"model_max_length": 8192},  # the tokenizer-level token limit
)
```
The checkpoint brings its own recipe along: its query and document marker tokens, its projection head, its scoring skiplist. For finetuning, you generally want to keep all of that and change only what your data demands. The first thing to check is the length configuration, since many released checkpoints cap documents at 180 to 512 tokens (see [Why Finetune?](https://huggingface.co#why-finetune)), and my medical passages run to 1,400 tokens. The mLateOn family already serves the backbone's full 8192 token context, but if your starting checkpoint carries caps, lift them:

```
# Let the model read full documents instead of the caps it was trained with,
# e.g. GTE-ModernColBERT-v1 ships with query_length=48 and document_length=300
model[0].query_length = None
model[0].document_length = None
```
With the per-task caps unset, truncation falls back to the tokenizer's `model_max_length`, which is why I configure that limit at load time above.

I made one more change, adding a punctuation skiplist that excludes punctuation tokens from document-side scoring and storage. In a 4-way ablation (none, punctuation, stopwords, both) it modestly won on quality, and it shrinks the document index by 9.6% on this data for free:

```
import string
# model[2] is the MultiVectorMask module
model[2].skiplist_words = list(string.punctuation)
model[2].resolve_with_tokenizer(model.tokenizer)  # token ids are cached, so re-resolve after changing
```
You can also point `MultiVectorEncoder` at any base transformer, and a fresh, randomly initialized token-level projection is appended for you:

```
from sentence_transformers import MultiVectorEncoder
model = MultiVectorEncoder("answerdotai/ModernBERT-base", model_kwargs={"torch_dtype": "float32"})
# MultiVectorEncoder(
#   (0): Transformer({..., 'architecture': 'ModernBertModel'})
#   (1): Dense({'in_features': 768, 'out_features': 128, 'bias': False, ...})
#   (2): MultiVectorMask({'skiplist_words': [], 'skiplist_tasks': ['document'], ...})
#   (3): Normalize({...})
# )
```
That's the classic ColBERT pipeline: a `Transformer` producing contextualized token embeddings, a token-level `Dense` projecting each of them down to 128 dimensions, a `MultiVectorMask` deciding which tokens count during scoring, and a token-level `Normalize`. The projection starts random, so training is required before this model is useful. Interestingly, this works with strong dense embedding backbones too. A fresh projection on [Alibaba-NLP/gte-modernbert-base](https://huggingface.co/Alibaba-NLP/gte-modernbert-base) reached within 0.03 of the existing-checkpoint starting points in my experiments, from nothing but the projection and 25k training pairs.

The classic ColBERT tokenization tricks (`[MASK]` query expansion, `[Q]` / `[D]` prefix tokens, a document length cap, a punctuation skiplist) are all off by default and configurable. See [Creating Custom Models](https://sbert.net/docs/multi_vector_encoder/usage/custom_models.html) for the full set. For what it's worth, I tested `[MASK]` query expansion in four configurations for my domain finetune and none of them made a measurable difference, so don't feel obliged to reach for the classic recipe.

I measured this directly while preparing this blogpost, taking six starting points and training each with the identical recipe on 25k medical question-passage pairs from [MIRIAD](https://huggingface.co/datasets/tomaarsen/miriad-4.4M-split), then evaluating on 1,000 held-out questions against a 50,000 passage corpus:

| Starting point | Zero-shot NDCG@10 | After 25k pairs | Delta | 
|---|---|---|---|
| [lightonai/mLateOn-unsupervised](https://huggingface.co/lightonai/mLateOn-unsupervised) | 0.9087 | **0.9398** | **+0.0311** | 
| [lightonai/mLateOn](https://huggingface.co/lightonai/mLateOn) | 0.9277 | 0.9319 | +0.0042 | 
| [lightonai/LateOn-unsupervised](https://huggingface.co/lightonai/LateOn-unsupervised) | 0.9026 | **0.9206** | **+0.0180** | 
| [lightonai/LateOn](https://huggingface.co/lightonai/LateOn) | 0.9185 | 0.9105 | -0.0080 | 
| [lightonai/GTE-ModernColBERT-v1](https://huggingface.co/lightonai/GTE-ModernColBERT-v1) | 0.9198 | 0.9007 | -0.0191 | 
| Fresh head on [gte-modernbert-base](https://huggingface.co/Alibaba-NLP/gte-modernbert-base) | - | 0.9177 | - | 

The result surprised me, and it replicated across two model families. *The `-unsupervised` checkpoints adapt to a new domain far better than their finished siblings, overtaking them despite starting lower. These checkpoints sit after large-scale contrastive pretraining but before supervised finetuning on general retrieval, so they carry all the late-interaction structure with none of the general-purpose tuning that domain training then has to undo. The finished checkpoints, by contrast, barely moved or even regressed, at every learning rate I tried.

So, if the model family you like publishes a pre-supervised checkpoint, start there. If not, a fresh projection on a strong retrieval-pretrained backbone is a close runner-up. Continuing from a fully finished checkpoint is the weakest option for domain adaptation, despite being the most natural-feeling one.

The [`MultiVectorEncoderTrainer`](https://sbert.net/docs/package_reference/multi_vector_encoder/trainer.html) uses [`datasets.Dataset`](https://huggingface.co/docs/datasets/main/en/package_reference/main_classes#datasets.Dataset) or [`datasets.DatasetDict`](https://huggingface.co/docs/datasets/main/en/package_reference/main_classes#datasets.DatasetDict) instances for training and evaluation. You can load data from the [Hugging Face Datasets Hub](https://huggingface.co/datasets) or use local data in whatever format you prefer (e.g. CSV, JSON, Parquet, Arrow, or SQL).

**Note:** Lots of public datasets that work out of the box with Sentence Transformers have been tagged with `sentence-transformers` on the Hugging Face Hub, so you can easily find them on [https://huggingface.co/datasets?other=sentence-transformers](https://huggingface.co/datasets?other=sentence-transformers). Consider browsing through these to find ready-to-go datasets that might be useful for your tasks, domains, or languages.

You can use the [`load_dataset`](https://huggingface.co/docs/datasets/main/en/package_reference/loading_methods#datasets.load_dataset) function to load data from datasets on the Hub:

```
from datasets import load_dataset
train_dataset = load_dataset("tomaarsen/miriad-4.4M-split", split="train")
print(train_dataset)
"""
Dataset({
    features: ['question', 'passage_text'],
    num_rows: 4467542
})
"""
```
This is the dataset I'll train on in this blogpost: 4.4 million medical questions from [MIRIAD](https://huggingface.co/datasets/miriad/miriad-4.4M), each paired with the source passage that contains its answer (averaging 941 tokens). Simple (query, relevant passage) pairs like these are the easiest retrieval training data to collect for your own domain, and as you'll see, they're all you need.

You can also use [`load_dataset`](https://huggingface.co/docs/datasets/main/en/package_reference/loading_methods#datasets.load_dataset) for loading local data in common file formats:

```
from datasets import load_dataset
dataset = load_dataset("csv", data_files="my_file.csv")
# or
dataset = load_dataset("json", data_files="my_file.json")
```
And if your local data requires pre-processing, you can use [`datasets.Dataset.from_dict`](https://huggingface.co/docs/datasets/main/en/package_reference/main_classes#datasets.Dataset.from_dict) to initialize your dataset with a dictionary of lists:

```
from datasets import Dataset
queries = []
documents = []
# Open a file, perform preprocessing, filtering, cleaning, etc.
# and append to the lists
dataset = Dataset.from_dict({
    "query": queries,
    "document": documents,
})
```
It is important that your dataset format matches your loss function (or that you choose a loss function that matches your dataset format). Verifying whether a dataset format works with a loss function involves two steps:

1. If your loss function requires a *Label* according to the[Loss Overview](https://sbert.net/docs/multi_vector_encoder/loss_overview.html) table, then your dataset must have a**column named "label" or "score"** . This column is automatically taken as the label.
2. All columns not named "label" or "score" are considered *Inputs* according to the[Loss Overview](https://sbert.net/docs/multi_vector_encoder/loss_overview.html) table. The number of remaining columns must match the number of valid inputs for your chosen loss. The names of these columns are**irrelevant** , only the**order matters** .

There are two multi-vector specific conventions on top of this:

- Positional query and document assignment: the first column is embedded as the *query* and all following columns as*documents* , regardless of the column names. This default can be overridden per column via the standard`router_mapping` training argument.
- Knowledge distillation format: one column per candidate document, i.e. `(query, document_1, ..., document_N, scores)` where`scores` is a list of N teacher scores per row. For KD datasets that store query and document*IDs* alongside separate text datasets (e.g.[lightonai/ms-marco-en-bge](https://huggingface.co/datasets/lightonai/ms-marco-en-bge) ), you can use[`resolve_ids`](https://sbert.net/docs/package_reference/util.html#sentence_transformers.util.dataset.resolve_ids) to resolve the IDs to texts on the fly.

Loss functions quantify how well a model performs for a given batch of data, allowing an optimizer to update the model weights to produce more favourable (i.e., lower) loss values. The right loss function for your task depends on the data you have and what you're trying to achieve. You can find a full list of options in the [Loss Overview](https://sbert.net/docs/multi_vector_encoder/loss_overview.html).

For the common case of question-answer or question-passage pairs, the workhorse is in-batch negatives training with [`MultiVectorMultipleNegativesRankingLoss`](https://sbert.net/docs/package_reference/multi_vector_encoder/losses.html#multivectormultiplenegativesrankingloss), where every other document in the batch acts as a negative for each query. Bigger batches mean more negatives and stronger training, so in practice you'll want its GradCache variant, [`CachedMultiVectorMultipleNegativesRankingLoss`](https://sbert.net/docs/package_reference/multi_vector_encoder/losses.html#cachedmultivectormultiplenegativesrankingloss), which decouples the effective batch size from what fits on your GPU:

```
from sentence_transformers import MultiVectorEncoder
from sentence_transformers.multi_vector_encoder.losses import CachedMultiVectorMultipleNegativesRankingLoss
model = MultiVectorEncoder("lightonai/mLateOn-unsupervised", model_kwargs={"torch_dtype": "float32"})
loss = CachedMultiVectorMultipleNegativesRankingLoss(
    model=model,
    mini_batch_size=16,  # how many documents to encode per chunk: bounds memory, not quality
)
```
The `mini_batch_size` parameter bounds the memory by encoding documents in chunks of this size, while the effective contrastive batch size (128 in my run below, and in my ablations bigger batches bought nothing further) stays a free choice. GradCache guarantees identical results regardless of the chunk size, so lower it for smaller GPUs at only a wall-clock cost. When your document lengths vary a lot, consider its sibling `mini_batch_num_tokens`, which packs each chunk to a total token budget instead of a document count, so a chunk of unusually long documents can never spike your memory (my `mini_batch_size=16` at roughly 940 tokens per document corresponds to `mini_batch_num_tokens=15_000`).

One multi-vector specific trap is that the contrastive losses default to `scale=1.0`, unlike the dense embedding equivalent which defaults to `scale=20.0`. That 20.0 exists because a cosine similarity is a single value in [-1, 1], too narrow a range for a sharp softmax. A MaxSim score instead sums one best-match similarity per query token, so it already spans roughly [0, query_length]: a 32-token query can score up to 32. So don't copy `scale=20.0` over from a dense training script, since it would saturate the softmax and kill your gradients.

For distillation from a stronger teacher, which is how the strongest general-purpose late-interaction models are trained, see [`MultiVectorDistillKLDivLoss`](https://sbert.net/docs/package_reference/multi_vector_encoder/losses.html#multivectordistillkldivloss) and the Knowledge Distillation tab in the [Training Overview](https://sbert.net/docs/multi_vector_encoder/training_overview.html#trainer) documentation.

You can customize the training process using the [`MultiVectorEncoderTrainingArguments`](https://sbert.net/docs/package_reference/multi_vector_encoder/training_args.html) class. This class lets you adjust parameters that can impact training speed and help you understand what's happening during training.

For more information on the most useful training arguments, check out the [Multi-Vector Encoder > Training Overview > Training Arguments](https://sbert.net/docs/multi_vector_encoder/training_overview.html#training-arguments). It's worth reading to get the most out of your training.

Here's an example, using the values from my actual training run:

```
from sentence_transformers import MultiVectorEncoderTrainingArguments
from sentence_transformers.base.sampler import BatchSamplers
args = MultiVectorEncoderTrainingArguments(
    # Required parameter:
    output_dir="models/mLateOn-medical",
    # Optional training parameters:
    num_train_epochs=1,
    per_device_train_batch_size=128,  # the effective contrastive batch, thanks to GradCache
    per_device_eval_batch_size=16,
    learning_rate=1e-4,
    warmup_steps=0.05,
    prompts={"question": "[Q] ", "passage_text": "[D] "},  # the checkpoint's markers, keyed by training column
    fp16=False,  # Set to True if you have a GPU that supports FP16
    bf16=True,  # Set to True if you have a GPU that supports BF16
    batch_sampler=BatchSamplers.NO_DUPLICATES,  # in-batch negatives benefit from no duplicates
    # Optional tracking/debugging parameters:
    eval_strategy="steps",
    eval_steps=0.1,
    save_strategy="steps",
    save_steps=0.05,
    logging_steps=0.01,
    run_name="mLateOn-medical",  # Will be used in e.g. Trackio, W&B, etc.
)
```
A few of these deserve a comment:

- `prompts` : training does not automatically apply the prompts stored in the model, so map them onto your training columns explicitly. Here that is the checkpoint's`[Q]` marker for the question column and`[D]` for the passage column, keeping training consistent with inference.
- `max_length` (deliberately not set): this argument caps tokenization during*training only* , for when you want cheaper training than the model's full serving length. I measured what that shortcut costs on this data. Training at 512 tokens lost about 0.015 NDCG@10 for about 2x the speed, and the deficit did not shrink with more data, because the model simply never sees what got cut off. Leave it unset so training matches inference, unless you need the speedup more than the quality.
- `learning_rate=1e-4` : after a sweep from 5e-6 to 2e-4, I had the best luck with this higher-than-usual learning rate.

To track your model's performance during training, you can pass an `eval_dataset` to the trainer for evaluation loss, but concrete retrieval metrics are much more informative. Sentence Transformers includes the following built-in evaluators for multi-vector models:

| Evaluator | Required Data | 
|---|---|
| [`MultiVectorInformationRetrievalEvaluator`](https://sbert.net/docs/package_reference/multi_vector_encoder/evaluation.html#multivectorinformationretrievalevaluator) | Queries, corpus, and relevant document mappings | 
| [`MultiVectorNanoBEIREvaluator`](https://sbert.net/docs/package_reference/multi_vector_encoder/evaluation.html#multivectornanobeirevaluator) | No data required | 
| [`MultiVectorTripletEvaluator`](https://sbert.net/docs/package_reference/multi_vector_encoder/evaluation.html#multivectortripletevaluator) | (anchor, positive, negative) triplets | 
| [`MultiVectorRerankingEvaluator`](https://sbert.net/docs/package_reference/multi_vector_encoder/evaluation.html#multivectorrerankingevaluator) | List of `{'query': '...', 'positive': [...], 'negative': [...]}` dictionaries | 
| [`MultiVectorDistillationEvaluator`](https://sbert.net/docs/package_reference/multi_vector_encoder/evaluation.html#multivectordistillationevaluator) | Queries with candidate documents and teacher scores | 

For domain finetuning, the [`MultiVectorInformationRetrievalEvaluator`](https://sbert.net/docs/package_reference/multi_vector_encoder/evaluation.html#multivectorinformationretrievalevaluator) built from your own held-out data is the one that matters. One tip on constructing it is that the corpus should be hard enough that models can be told apart. In my case the MIRIAD questions are generated from their own source passages, which makes retrieval unusually easy. Against just the 10k gold passages, nearly every model scored above 0.97 NDCG@10. If your evaluation saturates like that, add *distractor* passages (I use deduplicated passages from the training split) until the scores spread out:

```
from datasets import load_dataset
from sentence_transformers.multi_vector_encoder.evaluation import MultiVectorInformationRetrievalEvaluator
dataset = load_dataset("tomaarsen/miriad-4.4M-split")
# Gold: 1,000 evaluation questions, each mapping to its own passage, with the
# eval split's full ~10k unique passages as the initial corpus
corpus = {}
queries = {}
relevant_docs = {}
passage_to_id = {}
for idx, row in enumerate(dataset["eval"]):
    if row["passage_text"] not in passage_to_id:
        passage_to_id[row["passage_text"]] = f"p{len(passage_to_id)}"
        corpus[passage_to_id[row["passage_text"]]] = row["passage_text"]
    if idx < 1_000:
        queries[f"q{idx}"] = row["question"]
        relevant_docs[f"q{idx}"] = {passage_to_id[row["passage_text"]]}
# Distractors: unique train passages that make the haystack realistic
seen = set(passage_to_id)
for row in dataset["train"]:
    if len(corpus) >= 200_000:
        break
    if row["passage_text"] not in seen:
        seen.add(row["passage_text"])
        corpus[f"d{len(corpus)}"] = row["passage_text"]
evaluator = MultiVectorInformationRetrievalEvaluator(
    queries=queries,
    corpus=corpus,
    relevant_docs=relevant_docs,
    name="miriad-dev",
    batch_size=16,
)
# results = evaluator(model)
```
The [`MultiVectorEncoderTrainer`](https://sbert.net/docs/package_reference/multi_vector_encoder/trainer.html) is where all previous components come together. Here is the complete script that trained [multi-vector-encoder/mLateOn-medical](https://huggingface.co/multi-vector-encoder/mLateOn-medical), the model from the introduction:

```
import logging
import string
import traceback
from datasets import load_dataset
from sentence_transformers import (
    MultiVectorEncoder,
    MultiVectorEncoderModelCardData,
    MultiVectorEncoderTrainer,
    MultiVectorEncoderTrainingArguments,
)
from sentence_transformers.base.sampler import BatchSamplers
from sentence_transformers.multi_vector_encoder.evaluation import MultiVectorInformationRetrievalEvaluator
from sentence_transformers.multi_vector_encoder.losses import CachedMultiVectorMultipleNegativesRankingLoss
logging.basicConfig(format="%(asctime)s - %(message)s", datefmt="%Y-%m-%d %H:%M:%S", level=logging.INFO)
def main():
    # 1. Load the starting checkpoint: contrastively pretrained, not yet supervised
    # Loading in fp32 is preferred for training if your memory can handle it
    model = MultiVectorEncoder(
        "lightonai/mLateOn-unsupervised",
        model_kwargs={"torch_dtype": "float32"},
        processor_kwargs={"model_max_length": 8192},
        model_card_data=MultiVectorEncoderModelCardData(
            language="en",
            license="apache-2.0",
            model_name="mLateOn finetuned on MIRIAD medical retrieval",
        ),
    )
    # 2. Lift the per-task length caps so training and inference see full medical passages
    model[0].query_length = None
    model[0].document_length = None
    # 3. Skip punctuation tokens during scoring: a small quality win and a 9.6% smaller index
    model[2].skiplist_words = list(string.punctuation)
    model[2].resolve_with_tokenizer(model.tokenizer)
    # 4. Load 1 million medical question-passage pairs
    train_dataset = load_dataset("tomaarsen/miriad-4.4M-split", split="train").select(range(1_000_000))
    # 5. In-batch negatives with GradCache: large effective batch, memory-bounded chunks
    loss = CachedMultiVectorMultipleNegativesRankingLoss(model=model, mini_batch_size=16)
    # 6. A light dev evaluator to watch progress during training: 500 held-out questions
    # against the eval split's ~10k unique passages. The full 200k protocol runs afterwards.
    eval_split = load_dataset("tomaarsen/miriad-4.4M-split", split="eval")
    corpus, queries, relevant_docs, passage_to_id = {}, {}, {}, {}
    for idx, row in enumerate(eval_split):
        if row["passage_text"] not in passage_to_id:
            passage_to_id[row["passage_text"]] = f"p{len(passage_to_id)}"
            corpus[passage_to_id[row["passage_text"]]] = row["passage_text"]
        if idx < 500:
            queries[f"q{idx}"] = row["question"]
            relevant_docs[f"q{idx}"] = {passage_to_id[row["passage_text"]]}
    dev_evaluator = MultiVectorInformationRetrievalEvaluator(
        queries=queries, corpus=corpus, relevant_docs=relevant_docs, name="miriad-dev", batch_size=16
    )
    # 7. Training arguments, as discussed above
    run_name = "mLateOn-medical"
    args = MultiVectorEncoderTrainingArguments(
        output_dir=f"models/{run_name}",
        num_train_epochs=1,
        per_device_train_batch_size=128,
        per_device_eval_batch_size=16,
        learning_rate=1e-4,
        warmup_steps=0.05,
        prompts={"question": "[Q] ", "passage_text": "[D] "},
        fp16=False,  # Set to True if you have a GPU that supports FP16
        bf16=True,  # Set to True if you have a GPU that supports BF16
        batch_sampler=BatchSamplers.NO_DUPLICATES,
        eval_strategy="steps",
        eval_steps=0.1,
        save_strategy="steps",
        save_steps=0.05,
        logging_steps=0.01,
        run_name=run_name,
    )
    # 8. Create a trainer & train
    trainer = MultiVectorEncoderTrainer(
        model=model,
        args=args,
        train_dataset=train_dataset,
        loss=loss,
        evaluator=dev_evaluator,
    )
    trainer.train()
    # 9. Save the trained model
    model.save_pretrained(f"models/{run_name}/final")
    # 10. (Optional) Push it to the Hugging Face Hub
    try:
        model.push_to_hub(run_name)
    except Exception:
        logging.error(f"Error uploading model to the Hugging Face Hub:\n{traceback.format_exc()}")
if __name__ == "__main__":
    main()
```
That's the whole recipe: a pre-supervised checkpoint, a million domain pairs, in-batch negatives, full document length, and a higher-than-usual learning rate. The run took 14.5 hours on my single RTX 3090 at a peak of 17.5 GB VRAM, and every one of those choices was the winner of a measured comparison rather than a guess.

For readers on smaller budgets, my scaling experiments put 100k pairs (75 minutes of training) within 0.012 NDCG@10 of the full million-pair run. Most of the gain comes in the first hour.

The MultiVectorEncoder trainer supports various [`transformers.TrainerCallback`](https://huggingface.co/docs/transformers/main_classes/callback#transformers.TrainerCallback) subclasses, including:

- [`WandbCallback`](https://huggingface.co/docs/transformers/en/main_classes/callback#transformers.integrations.WandbCallback) for logging training metrics to W&B if`wandb` is installed
- [`TensorBoardCallback`](https://huggingface.co/docs/transformers/en/main_classes/callback#transformers.integrations.TensorBoardCallback) for logging training metrics to TensorBoard if`tensorboard` is accessible
- [`CodeCarbonCallback`](https://huggingface.co/docs/transformers/en/main_classes/callback#transformers.integrations.CodeCarbonCallback) for tracking carbon emissions during training if`codecarbon` is installed

Enable these via the `report_to` training argument, e.g. `report_to=["wandb", "codecarbon"]`, with the required dependencies installed. It defaults to `"none"`, and `report_to="all"` activates every integration whose dependency is installed.

Refer to the [Transformers Callbacks documentation](https://huggingface.co/docs/transformers/en/main_classes/callback) for more information on these callbacks and how to create your own.

Typically, top-performing general-purpose models are trained on multiple datasets simultaneously. However, this approach can be challenging due to the varying formats of each dataset. Fortunately, the [`MultiVectorEncoderTrainer`](https://sbert.net/docs/package_reference/multi_vector_encoder/trainer.html) allows you to train on multiple datasets without requiring a uniform format. Additionally, it provides the flexibility to apply different loss functions to each dataset. Here are the steps to train with multiple datasets at once:

- Use a dictionary of [`datasets.Dataset`](https://huggingface.co/docs/datasets/main/en/package_reference/main_classes#datasets.Dataset) instances (or a[`datasets.DatasetDict`](https://huggingface.co/docs/datasets/main/en/package_reference/main_classes#datasets.DatasetDict) ) as the`train_dataset` (and optionally also`eval_dataset` ).
- (Optional) Use a dictionary of loss functions mapping dataset names to losses. Only required if you wish to use different loss functions for different datasets.

Each training/evaluation batch will only contain samples from one of the datasets. The order in which batches are sampled from the multiple datasets is defined by the [`MultiDatasetBatchSamplers`](https://sbert.net/docs/package_reference/sentence_transformer/sampler.html#sentence_transformers.training_args.MultiDatasetBatchSamplers) enum, which can be passed to the [`MultiVectorEncoderTrainingArguments`](https://sbert.net/docs/package_reference/multi_vector_encoder/training_args.html) via `multi_dataset_batch_sampler`. Valid options are:

- `MultiDatasetBatchSamplers.ROUND_ROBIN` : Round-robin sampling from each dataset until one is exhausted. With this strategy, it's likely that not all samples from each dataset are used, but each dataset is sampled from equally.
- `MultiDatasetBatchSamplers.PROPORTIONAL` (default): Sample from each dataset in proportion to its size. With this strategy, all samples from each dataset are used and larger datasets are sampled from more frequently.

To find out where the finetuned model stands, I evaluated it against over 50 retrieval model configurations across four architecture families on the MIRIAD evaluation set, built exactly as in the [Evaluator](https://huggingface.co#evaluator) section above, with 1,000 held-out medical questions searching 200,000 unique passages (the 10k gold passages hidden among 190k deduplicated distractors from the training split). This corpus is four times the size of the 50,000-passage one from [Which starting point should you pick?](https://huggingface.co#which-starting-point-should-you-pick), so scores are not comparable between the two tables.

![NDCG@10 versus active parameters on the MIRIAD 200k benchmark, with an arrow marking the finetuning jump from mLateOn-unsupervised to mLateOn-medical](https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/blog/train-multi-vector-encoder/mve_medical_model_size_ndcg.png)


The headline results, with the full table in the collapsible below:

| Model | Family | NDCG@10 | 
|---|---|---|
| [**multi-vector-encoder/mLateOn-medical (mine)**](https://huggingface.co/multi-vector-encoder/mLateOn-medical) | **Multi-vector, finetuned** | **0.9139** | 
| [lightonai/mLateOn](https://huggingface.co/lightonai/mLateOn) | Multi-vector, zero-shot | 0.8520 | 
| [lightonai/GTE-ModernColBERT-v1](https://huggingface.co/lightonai/GTE-ModernColBERT-v1) (cap lifted) | Multi-vector, zero-shot | 0.8502 | 
| [Qwen/Qwen3-Embedding-4B](https://huggingface.co/Qwen/Qwen3-Embedding-4B) | Dense, zero-shot | 0.7817 | 
| [voyageai/voyage-4-nano](https://huggingface.co/voyageai/voyage-4-nano) | Dense, zero-shot | 0.7563 | 
| BM25 | Lexical | 0.7501 | 
| [naver/splade-v3](https://huggingface.co/naver/splade-v3) | Sparse, zero-shot | 0.6853 | 

The finetuned model tops the table, beating the strongest zero-shot model of any architecture by +0.062 NDCG@10. In other words, the strongest zero-shot model returns the right passage as the very first hit for 75.8% of the queries, while the finetuned model does so for 84.9%, cutting the rank-1 error by more than a third.

The architecture pattern is just as clear, with the top of the table exclusively late interaction. On long documents, one vector per token beats one vector per document, even at matched training and matched backbones. DenseOn and LateOn share training data and architecture except for the head, and the late-interaction sibling wins by +0.12, with the multilingual pair (mDenseOn and mLateOn) replicating this at +0.13. Scale doesn't rescue single vectors either. [Qwen3-Embedding-4B](https://huggingface.co/Qwen/Qwen3-Embedding-4B), the strongest dense model with roughly 33x the active (non-embedding) parameters of mine, still stops 0.13 short, and the 8B version scores lower than the 4B.

BM25 also performs surprisingly well, beating every sparse model, every truncation-capped multi-vector model, and all but three dense models: the multi-billion [Qwen3-Embedding-4B](https://huggingface.co/Qwen/Qwen3-Embedding-4B) and [8B](https://huggingface.co/Qwen/Qwen3-Embedding-8B), and [voyage-4-nano](https://huggingface.co/voyageai/voyage-4-nano), which reads its full 32k token context to edge past by just 0.006. Don't expect that to transfer to your own data though. MIRIAD's questions are generated from the passages, so the lexical overlap between a query and its gold passage is far larger than in typical retrieval, and BM25's unlimited context length lets it use every one of those overlapping words while most neural checkpoints truncate. A BM25 baseline is cheap and always worth running, just don't count on this margin.

The full field at a glance, sorted by score and colored by architecture family.

![Sorted NDCG@10 on the MIRIAD 200k benchmark for every evaluated model, colored by architecture family](https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/blog/train-multi-vector-encoder/mve_medical_ndcg_by_model.png)


Models marked `@N` are evaluated with their document length cap lifted to N tokens, since their native caps (180 to 512 tokens) would otherwise truncate the 941-token average passages. For every multi-vector model this lift was worth +0.08 to +0.24 NDCG@10 over the as-served row, and even the dense DenseOn gained +0.03 from the same treatment.

Note that this does not mean that [multi-vector-encoder/mLateOn-medical](https://huggingface.co/multi-vector-encoder/mLateOn-medical) is the strongest model on *all* domains. It's simply the strongest in *my* domain. This is totally fine, as I just need this model to work well on my data.

Don't underestimate the power of finetuning multi-vector models on your domain. Fourteen and a half hours on a single consumer GPU produced a model that no general-purpose retriever comes close to on this data, and the recipe is a single script with no teacher model and no mined negatives!

The fair objection to multi-vector retrieval is index size, and this domain is close to the worst case for it. Storing one vector per token, my model needs about 878 vectors per passage, so the 200,000-passage corpus takes roughly 45 GB at fp16, where a dense model needs well under 1 GB. Document length is what makes that gap so wide. The Natural Questions passages in the [companion post](https://huggingface.co/blog/multi-vector-encoder) average about 125 token vectors each, seven times fewer, so a corpus of short passages starts from a far smaller index than this one does. The [`HierarchicalTokenPooling`](https://sbert.net/docs/package_reference/multi_vector_encoder/modules.html#hierarchicaltokenpooling) module compresses exactly this by clustering each document's token embeddings and storing the cluster means, keeping roughly `1 / pool_factor` of the vectors:

```
from sentence_transformers.multi_vector_encoder.modules import HierarchicalTokenPooling
pooling = HierarchicalTokenPooling(pool_factor=4)
document_embeddings = model.encode_document(passages, token_pooling=pooling)
```
I measured it post-hoc on the finished model, with no pooling-aware training, and on long documents it is remarkably cheap.

![Embedding size for the 200,000-passage corpus versus NDCG@10, with the token pooling trajectory sweeping the multi-vector index into dense-model territory](https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/blog/train-multi-vector-encoder/mve_medical_index_size_ndcg.png)


The solid points are uncompressed embeddings, so that every family is counted the same way and scored with exact search. You would not deploy any of them like that, though. Dense indexes routinely use int8 or binary quantization with rescoring, sparse indexes compress their postings, and multi-vector indexes use PLAID-style residual compression. Don't read those points as the disk you need to buy, but as relative storage cost.

Token pooling is the solid line. Halving the vector count costs 0.0033 NDCG@10 and leaves rank-1 accuracy untouched, and keeping only a quarter of them, at 11.2 GB, still scores 0.8991. The curve keeps going (I measured out to a tenth of the vectors, still at 0.8765) but there is little reason to push pooling that far once quantization is on the table, which is what the dashed line below is about.

The dashed line is what a real deployment might look like. I gave Omar Khattab early access to the model and the benchmark, and he measured these configurations with [fast-plaid](https://github.com/lightonai/fast-plaid) at 1-bit residual quantization, using compact 17-bit centroid ids and 18-bit document ids instead of its ordinary unpacked 64-bit integers, plus document-side pruning:

| configuration | vectors kept | index | NDCG@10 | 
|---|---|---|---|
| 1-bit PLAID, all vectors | 100% | 3.37 GB | 0.8984 | 
| 1-bit PLAID + pruning | 65% | 2.23 GB | 0.8830 | 
| 1-bit PLAID + pruning | 42% | 1.45 GB | 0.8642 | 

That first row is 13x smaller than the raw embeddings, for 0.0155 NDCG@10. That is a far better trade than anywhere on the pooling curve. Quantization shrinks each vector while pooling and pruning cut how many you keep, so they compose, and quantization is the one to reach for first. Push further and the last row lands at 1.45 GB, *smaller* than the fp16 embeddings of [Qwen3-Embedding-8B](https://huggingface.co/Qwen/Qwen3-Embedding-8B) (1.64 GB), while scoring 0.0895 higher. The objection that multi-vector indexes are too big does not survive a properly configured index.

The pruning here is naive, meant only to establish that token reduction works on top of quantization, so read the bottom two rows as a floor rather than the frontier. If you would rather not hand-tune quantization at all, the [Indexing](https://huggingface.co/blog/multi-vector-encoder#indexing) section of the companion post covers fast-plaid, Qdrant, Weaviate, and Vespa.

Multi-vector retrieval is only as expensive as its index. The raw embeddings for this corpus are 45 GB, and a properly configured index is at least 7x smaller at nearly the same accuracy. The index deserves as much of your attention as the checkpoint.

Thanks to [Omar Khattab](https://github.com/okhat) for measuring the quantized and pruned index configurations in [Optimizing the index](https://huggingface.co#optimizing-the-index), and for the discussions around late-interaction index costs.

These pages have training examples with explanations as well as links to training scripts. You can use them to get familiar with the multi-vector training loop:

- [MIRIAD](https://sbert.net/examples/multi_vector_encoder/training/miriad/README.html) : domain-specific training on medical retrieval, an earlier and simpler cousin of this blogpost's recipe
- [MS MARCO](https://sbert.net/examples/multi_vector_encoder/training/msmarco/README.html) : contrastive and knowledge distillation recipes
- [Multimodal](https://sbert.net/examples/multi_vector_encoder/training/multimodal/README.html) : ColPali-style visual document retrieval training
- [PEFT Adapters](https://sbert.net/examples/multi_vector_encoder/training/peft/README.html) : parameter-efficient finetuning with LoRA

For further learning, you may also want to explore the following resources on Sentence Transformers:

- [Installation](https://sbert.net/docs/installation.html)
- [Quickstart](https://sbert.net/docs/quickstart.html)
- [Usage](https://sbert.net/docs/multi_vector_encoder/usage/usage.html)
- [Creating Custom Models](https://sbert.net/docs/multi_vector_encoder/usage/custom_models.html)
- [Pretrained Models](https://sbert.net/docs/multi_vector_encoder/pretrained_models.html)
- [Training Overview](https://sbert.net/docs/multi_vector_encoder/training_overview.html) (This blogpost is a distillation of the Training Overview documentation)
- [Loss Overview](https://sbert.net/docs/multi_vector_encoder/loss_overview.html)
- [API Reference](https://sbert.net/docs/package_reference/multi_vector_encoder/index.html)

And here is an advanced page that might interest you:

And the companion blogpost, covering everything about *using* these models:

 Feature Extraction •  4B • Updated   •  3.41M  •  313 

 Sentence Similarity •  0.1B • Updated   •  365k  •  175 

 Sentence Similarity •  0.1B • Updated   •  5.93k  •  53 

 Sentence Similarity •  0.1B • Updated   •  662  •  35 

 Sentence Similarity •  0.1B • Updated   •  848  •  8 

 Sentence Similarity •  0.3B • Updated   •  8.44k  •  31 

 Sentence Similarity •  0.3B • Updated   •  477  •  5 

 Feature Extraction •  0.3B • Updated   •  14  •  2 

 Feature Extraction •  0.3B • Updated   •  238k  •  140 

More Articles from our Blog

nlpguidecommunity

  95

 August 18, 2026 open-sourcecommunitynlp

  Hot
- +2

 277

 September 4, 2025
