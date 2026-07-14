---
title: StarCoder2 and The Stack v2
kind: blog
topic: models
subtopic: releases
secondary_topics: []
summary: StarCoder2 (3B/7B/15B) code LLMs trained on 3-4T tokens of The Stack v2 (67.5
  TB, 600+ languages, repository-grouped so models see repo context), using Grouped
  Query Attention, 16k context with 4k sliding-window attention and a Fill-in-the-Middle
  objective; the 15B matches 33B+ models on many evals.
triage: null
skip_reason: null
source: huggingface
url: https://huggingface.co/blog/starcoder2
author: Leandro von Werra; Loubna Ben Allal; Anton Lozhkov; Nouamane Tazi
published: '2024-02-28'
fetched: '2026-07-14T22:10:43Z'
classifier: claude
taxonomy_rev: 1
words: 543
content_sha256: 170caad3a05204cabf1f2ca36f9b3c91b61ad08b3137dae91aa89785233f15fb
---

# StarCoder2 and The Stack v2

Text Generation •  16B • Updated   •  8.14k  •  674  

#### bigcode/starcoder2-15b

![](https://cdn-avatars.huggingface.co/v1/production/uploads/1659521200179-5e48005437cb5b49818287a5.png) 

 Published
					February 28, 2024 

  Upvote 

 9

StarCoder2 is a family of open LLMs for code and comes in 3 different sizes with 3B, 7B and 15B parameters. The flagship StarCoder2-15B model is trained on over 4 trillion tokens and 600+ programming languages from The Stack v2. All models use Grouped Query Attention, a context window of 16,384 tokens with a sliding window attention of 4,096 tokens, and were trained using the Fill-in-the-Middle objective.

StarCoder2 offers three model sizes: a 3 billion-parameter model trained by ServiceNow, a 7 billion-parameter model trained by Hugging Face, and a 15 billion-parameter model trained by NVIDIA using NVIDIA NeMo on NVIDIA accelerated infrastructure:

- [StarCoder2-3B](https://huggingface.co/bigcode/starcoder2-3b)was trained on 17 programming languages from The Stack v2 on 3+ trillion tokens.
- [StarCoder2-7B](https://huggingface.co/bigcode/starcoder2-7b)was trained on 17 programming languages from The Stack v2 on 3.5+ trillion tokens.
- [StarCoder2-15B](https://huggingface.co/bigcode/starcoder2-15b)was trained on 600+ programming languages from The Stack v2 on 4+ trillion tokens.

StarCoder2-15B is the best in its size class and matches 33B+ models on many evaluations. StarCoder2-3B matches the performance of StarCoder1-15B:

The Stack v2 is the largest open code dataset suitable for LLM pretraining. The Stack v2 is larger than The Stack v1, follows an improved language and license detection procedure, and better filtering heuristics. In addition, the training dataset is grouped by repositories, allowing to train models with repository context.

| [The Stack v1](https://huggingface.co/datasets/bigcode/the-stack/) | [The Stack v2](https://huggingface.co/datasets/bigcode/the-stack-v2/) | |
|---|---|---|
| full | 6.4TB | 67.5TB | 
| deduplicated | 2.9TB | 32.1TB | 
| training dataset | ~200B tokens | ~900B tokens | 

This dataset is derived from the Software Heritage archive, the largest public archive of software source code and accompanying development history. Software Heritage, launched by Inria in partnership with UNESCO, is an open, non-profit initiative to collect, preserve, and share the source code of all publicly available software. We are grateful to Software Heritage for providing access to this invaluable resource. For more details, visit the [Software Heritage website](https://www.softwareheritage.org).

The Stack v2 can be accessed through the [Hugging Face Hub](https://huggingface.co/datasets/bigcode/the-stack-v2/).

BigCode is an open scientific collaboration led jointly by Hugging Face and ServiceNow that works on the responsible development of large language models for code.

- [Paper](https://drive.google.com/file/d/17iGn3c-sYNiLyRSY-A85QOzgzGnGiVI3/view?usp=sharing): A technical report about StarCoder2 and The Stack v2.
- [GitHub](https://github.com/bigcode-project/starcoder2/): All you need to know about using or fine-tuning StarCoder2.
- [StarCoder2-3B](https://huggingface.co/bigcode/starcoder2-3b): Small StarCoder2 model.
- [StarCoder2-7B](https://huggingface.co/bigcode/starcoder2-7b): Medium StarCoder2 model.
- [StarCoder2-15B](https://huggingface.co/bigcode/starcoder2-15b): Large StarCoder2 model.

- [StarCoder2 License Agreement](https://huggingface.co/spaces/bigcode/bigcode-model-license-agreement): The model is licensed under the BigCode OpenRAIL-M v1 license agreement.
- [StarCoder2 Search](https://huggingface.co/spaces/bigcode/search-v2): Full-text search for code in the pretraining dataset.
- [StarCoder2 Membership Test](https://stack-v2.dataportraits.org): Blazing fast check of code that was present in the pretraining dataset.

- [VSCode Extension](https://marketplace.visualstudio.com/items?itemName=HuggingFace.huggingface-vscode): Code with StarCoder!
- [Big Code Models Leaderboard](https://huggingface.co/spaces/bigcode/bigcode-models-leaderboard)

You can find all the resources and links at [huggingface.co/bigcode](https://huggingface.co/bigcode)!

 Text Generation •  16B • Updated   •  8.14k  •  674 

 Text Generation •  3B • Updated   •  180k  •  221 

 Text Generation •  7B • Updated   •  7.33k  •  217 

 Viewer • Updated  •  546M •  18.6k  •  1.04k 

 Viewer • Updated  •  5.45B •  26.8k  •  603 

More Articles from our Blog

nlpcommunityresearch

 
- +2

 113

 August 12, 2024 nlpcommunityresearch

  60

 July 31, 2024
