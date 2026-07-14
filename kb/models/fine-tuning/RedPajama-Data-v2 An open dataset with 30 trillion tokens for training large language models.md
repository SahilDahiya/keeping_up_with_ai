---
title: 'RedPajama-Data-v2: An open dataset with 30 trillion tokens for training large
  language models'
topic: models
subtopic: fine-tuning
secondary_topics: []
summary: Introduces RedPajama-Data-v2, a large web dataset for training language models.
source: together
url: https://www.together.ai/blog/redpajama-data-v2
author: Together
published: '2023-10-30'
fetched: '2026-07-11T04:25:23Z'
classifier: codex
taxonomy_rev: 1
words: 2728
content_sha256: 1d1f52da2653bc97b991818255ea336926476c3d8e459b7b54a145e3f9bcb967
triage: keep
skip_reason: null
---

# RedPajama-Data-v2: An open dataset with 30 trillion tokens for training large language models

#### Today, we're releasing a new version of the RedPajama dataset, with 30 trillion filtered and deduplicated tokens (100+ trillions raw) from 84 CommonCrawl dumps covering 5 languages, along with 40+ pre-computed data quality annotations that can be used for further filtering and weighting.

Over the last half a year, we have been pleased to see that RedPajama-1T, which we released in March, has ignited the creation of many new language models. So many people from the community have downloaded this 5TB dataset---more than 190,000 times and have been using them [in such creative ways](https://huggingface.co/search/full-text?q=redpajama)! RedPajama-1T consists of 1 trillion high-quality English tokens, but it was only the first step. Today, with the release of RedPajama-V2, we are making a further step towards the development of open datasets by releasing a massive, 30 trillion token web dataset. This is, to our best knowledge, the largest public dataset released specifically for LLM training. Even more excitingly, we include 40+ pre-computed quality annotations, allowing the community to further filter and weigh the data. Specifically, this release includes:

- Over 100 billion text documents with 100+ trillion raw tokens from 84 CommonCrawl dumps;
- 40+ of the most widely used quality annotations pre-computed for a deduplicated 30 trillion tokens subset;
- Five languages: English, French, Spanish, German, and Italian
- All data processing scripts are open source and available on [GitHub](https://github.com/togethercomputer/RedPajama-Data); all data are available on[HuggingFace](https://huggingface.co/datasets/togethercomputer/RedPajama-Data-V2).

## Why RedPajama-Data-v2 and How to Use it?

A central ingredient to state-of-the-art open LLMs like Llama, Mistral, Falcon, MPT, and the RedPajama models is the large amounts of high-quality data that these models are trained on. For example, Llama 2 is trained on 2.4 trillion carefully curated tokens. The most prominent data sources are the crawls made publicly available by [CommonCrawl](https://commoncrawl.org/). However, this data is crude and is not ideal for direct use for LLM training due to artifacts arising from the conversion of HTML to plain text, sources of generally low quality, and biases inherent to the distribution of content on the web. Getting the right dataset and data mixture is painful and any LLM developer has to go through the laborious, time-consuming, energy-intensive and expensive steps of processing and filtering this crude data. Although there have been several community projects around this effort, such as [C4](https://arxiv.org/abs/1910.10683), [RedPajama-1T,](https://huggingface.co/datasets/togethercomputer/RedPajama-Data-1T) [Refinedweb (Falcon)](https://huggingface.co/datasets/tiiuae/falcon-refinedweb), [Dolma (AI2)](https://github.com/allenai/dolma) and [SlimPajama](https://huggingface.co/datasets/cerebras/SlimPajama-627B), many of them only cover a small portion of the CommonCrawl crawls; moreover, they represent a very specific way in which data are filtered.

With RedPajama-Data-v2, our goal is to lift this burden off the community and provide a pool of web data serving as a base from which high quality datasets for LLM training can be extracted and based on which LLM training data can be thoroughly researched. It provides, to our best knowledge, the most complete coverage on CommonCrawl (with 84 dumps processed). More importantly, we provide 40+ quality annotations — the result of different ML classifiers on data quality, minhash results that can be used for fuzzy deduplication, or heuristics such as "the fraction of words that contain no alphabetical character". We provide our best effort implementations of quality annotations used in [C4](https://arxiv.org/abs/1910.10683), [Gopher](https://arxiv.org/abs/2112.11446), [Pretrainer's Guide](https://arxiv.org/abs/2305.13169), [RefinedWeb](https://arxiv.org/abs/2306.01116) and [Data Selection for Language Models via Importance Resampling](https://arxiv.org/abs/2302.03169). These annotations provide a way for an LLM developer to easily slice and filter the data, combining these into a new data quality pipeline to create their own pre-training dataset.

Here are some examples! The following code snippets show how one can implement commonly used filtering rules in combination with the RedPajama-V2 dataset. For example, implementing the Gopher rules and use these to filter out documents that do not comply with the Gopher rules is as easy as:

```
def gopher_rules_pass(sample) -> bool:
    """ function returns True if the sample complies with Gopher rules """
    signals = json.loads(sample["quality_signals"])
    # rule 1: number of words between 50 and 10'000
    word_count = signals["rps_doc_word_count"][0][2]
    if word_count < 50 or word_count > 10_000:
        return False
    # rule 2: mean word length between 3 and 10
    mean_word_length = signals["rps_doc_mean_word_length"][0][2]
    if mean_word_length < 3 or mean_word_length > 10:
        return False
    # rule 2: symbol to word ratio below 0.1
    symbol_word_ratio = signals["rps_doc_symbol_to_word_ratio"][0][2]
    if  symbol_word_ratio > 0.1:
        return False
    # rule 3: 90% of lines need to start without a bullet point
    n_lines = signals["ccnet_nlines"][0][2]
    n_lines_bulletpoint_start = sum(map(lambda ln: ln[2], signals["rps_lines_start_with_bulletpoint"]))
    if n_lines_bulletpoint_start / n_lines > 0.9:
        return False
    # rule 4: the ratio between characters in the most frequent 2-gram and the total number
    # of characters must be below 0.2
    top_2_gram_frac = signals["rps_doc_frac_chars_top_2gram"][0][2]
    if top_2_gram_frac > 0.2:
        return False
    # rule 5: ...
    return True
ds = load_dataset("togethercomputer/RedPajama-Data-V2", name="sample")
filtered_dataset = list(filter(gopher_rules_pass, ds["train"]))
```
In the above snippet, we have used the "sample" config to load just a subset of the dataset. In case you want to load the full dataset for, e.g., snapshot 2023-14 in English, you can run:

```
ds_iterator = load_dataset(
    "togethercomputer/RedPajama-Data-V2",
    partition="head_middle",
    snapshots=["2023-14"],
    languages=["en"],
    name="default"
)
```
We can also use the rules used in RedPajama-v1 or C4:

```
def rpv1_rules_pass(sample) -> bool:
    """ function returns True if the sample complies with the filtering rules used in RP-V1 """
    signals = json.loads(sample["quality_signals"])
    # rule 1: the wikipedia reference classifier score must be higher than 0.25
    wikiref_score = signals["rps_doc_ml_wikiref_score"][0][2]
    if wikiref_score < 0.25:
        return False
    return True
def c4_rules_pass(sample) -> bool:
    """ function returns True if the sample complies with the filtering rules used in C4 """
    signals = json.loads(sample["quality_signals"])
    # rule 1: at least 3 sentences
    num_sentences = signals["rps_doc_num_sentences"][0][2]
    if num_sentences < 3:
        return False
    # rule 2: page may not contain bad words
    n_bad_words = signals["rps_doc_ldnoobw_words"][0][2]
    if n_bad_words > 0:
        return False
    # rule 3: page may not contain placeholder "lorem ipsum" text
    lorem_ipsum = signals["rps_doc_lorem_ipsum"][0][2]
    if lorem_ipsum > 0:
        return False
    # rule 4: ...
    return True
```
In the current release, we include 40+ quality annotations, but we very much view this as a "living" project where new additions will be made over time as the field moves towards a better understanding of LLM training data. We hope the community provides feedback, and we are looking forward to continuing to enrich our current pool of annotations.

### Data Processing Steps

RedPajama-V2 focuses on CommonCrawl. Other data sources such as Wikipedia are available in [RedPajama-V1](https://huggingface.co/datasets/togethercomputer/RedPajama-Data-1T). We also encourage you to enrich your data mixture with the [Stack](https://huggingface.co/datasets/bigcode/the-stack) (by BigScience) for code and [s2orc](https://allenai.org/data/s2orc) (by AI2) for scientific articles. RedPajama-V2 is built from the ground up based on publicly available web data, consisting of 84 crawls provided by CommonCrawl. The core components that this dataset is made of, are the source data (plain text), 40+ quality annotations, and deduplication clusters.

### Creating the Source Data

The first processing step in building this dataset is to pass each CommonCrawl snapshot through the [CCNet pipeline](https://aclanthology.org/2020.lrec-1.494/). We choose this pipeline due to its light processing, aligning with our guiding principle of preserving as much information in the raw dataset as possible and allowing downstream model developers to filter or reweight the dataset. We use the language filter in CCNet and keep five languages in this release: English, French, Spanish, German and Italian. This processing step produces 100 billion individual text documents. 

### Quality Annotations

In addition to the text documents processed by CCNet, we compute over 40 of the most widely used quality annotations for the "head" and "middle" buckets. The primary purpose of these annotations is to allow downstream model developers to filter or reweight the dataset based on their criteria, and to foster research into how these annotations should be used. In addition, we also plan, with the help of the community, to include more quality signals over time. With this release, we publish a first set of quality annotations, which consists of our implementations of the most common quality annotations that are described in [C4](https://arxiv.org/abs/1910.10683), [Gopher](https://arxiv.org/abs/2112.11446), [Pretrainer's Guide](https://arxiv.org/abs/2305.13169), [RefinedWeb](https://arxiv.org/abs/2306.01116), in addition to several signals described in [other papers](https://arxiv.org/abs/2302.03169). These annotations fall into the following categories:

- Quality signals indicating how **natural**a given piece of text is. This includes simple heuristic measures such as the number of sentences, the number of words, the fraction of all-caps words, among others.
- Quality signals indicating how **repetitive**a given piece of text is. Here follow the Gopher rules ([Rae et al.](https://arxiv.org/abs/2112.11446)) and compute the fraction of characters that appear in duplicated word n-grams and the fraction of characters in the most frequent word n-gram appearing in the documents.
- **Content-based**quality signals are comprised of signals that take the content into account such as the density of words appearing in a list of blocked words (similar to C4), or documents which come from a list of domains flagged as containing potentially harmful or otherwise offensive content.
- **ML-based**quality signals revolve around the idea of measuring how similar a given text is to a high-quality domain. Here we use fasttext classifiers trained on various high quality domains such as Wikipedia, as well as importance weights as proposed by- [Xie et al](https://arxiv.org/abs/2302.03169).
- **Deduplication**signals with pre-computed Minhash signatures (with 128 permutations) which can be used for fuzzy deduplication at different degrees.

| Annotation Tag | Description | Category | Reference |
|---|---|---|---|
| ccnet_bucket | head, middle or tail bucket of the perplexity score | CCNet | [CCNet](https://aclanthology.org/2020.lrec-1.494/) |
| ccnet_language_score | score of the language identification model | CCNet | [CCNet](https://aclanthology.org/2020.lrec-1.494/) |
| ccnet_length | number of characters | CCNet | [CCNet](https://aclanthology.org/2020.lrec-1.494/) |
| ccnet_nlines | number of lines | CCNet | [CCNet](https://aclanthology.org/2020.lrec-1.494/) |
| ccnet_original_length | number of characters before in-document line deduplication | CCNet | [CCNet](https://aclanthology.org/2020.lrec-1.494/) |
| ccnet_original_nlines | number of lines before in-document line deduplication | CCNet | [CCNet](https://aclanthology.org/2020.lrec-1.494/) |
| ccnet_perplexity | perplexity of an LM trained on Wikipedia | CCNet | [CCNet](https://aclanthology.org/2020.lrec-1.494/) |
| rps_doc_books_importance | Given a bag of {1,2}-wordgram model trained on Books p, and a model trained on the source domain q, This is the logarithm of the ratio p(doc)/q(doc). | ML Heuristics | [Importance Resampling (Xie            et al.)](https://arxiv.org/abs/2302.03169) |
| rps_doc_openwebtext_importance | Given a bag of {1,2}-wordgram model trained on OpenWebText p, and a model trained on the source domain q, this is the logarithm of the ratio p(doc)/q(doc). | ML Heuristics | [Importance Resampling (Xie            et al.)](https://arxiv.org/abs/2302.03169) |
| rps_doc_wikipedia_importance | Given a bag of {1,2}-wordgram model trained on Wikipedia articles p, and a model trained on the source domain q, this is the logarithm of the ratio p(doc)/q(doc). | ML Heuristics | [Importance Resampling (Xie            et al.)](https://arxiv.org/abs/2302.03169) |
| rps_doc_ml_wikiref_score | Fasttext classifier prediction for the document being a Wikipedia reference. This is the same fasttext model used in the RedPajama-1T dataset. Only applies to English data.. | ML Heuristics | [LLaMA](https://arxiv.org/abs/2302.13971),[RedPajama-1T](https://huggingface.co/datasets/togethercomputer/RedPajama-Data-1T) |
| rps_doc_ml_palm_score | Fasttext classifier prediction for the document being a Wikipedia article, OpenWebText sample or a RedPajama-V1 book. Only for English data. | ML Heuristics | [PaLM](https://arxiv.org/abs/2204.02311),[GLaM](https://arxiv.org/abs/2112.06905) |
| rps_doc_ml_wikipedia_score | Fasttext classifier prediction for the document being a Wikipedia article. This is used for non-English data | ML Heuristics | - |
| rps_doc_curly_bracket | The ratio between the number of occurrences of '{' or '}' and the number of characters in the raw text. | Natural Language | [C4](https://arxiv.org/abs/1910.10683) |

| Annotation Tag | Description | Category | Reference |
|---|---|---|---|
| rps_doc_frac_all_caps_words | The fraction of words in the content that only consist of uppercase letters. This is based on the raw content. | Natural Language | [Pretrainer's Guide](https://arxiv.org/abs/2305.13169) |
| rps_doc_frac_lines_end_with_ellipsis | The fraction of lines that end with an ellipsis, where an ellipsis is defined as either "..." or "…". | Natural Language | [RefinedWeb](https://arxiv.org/abs/2306.01116),[Gopher](https://arxiv.org/abs/2112.11446) |
| rps_doc_frac_no_alph_words | The fraction of words that contain no alphabetical character. | Natural Language | [RefinedWeb](https://arxiv.org/abs/2306.01116),[Gopher](https://arxiv.org/abs/2112.11446) |
| rps_doc_lorem_ipsum | The ratio between the number of occurrences of 'lorem ipsum' and the number of characters in the content after normalisation. | Natural Language | [C4](https://arxiv.org/abs/1910.10683) |
| rps_doc_mean_word_length | The mean length of words in the content after normalisation. | Natural Language | [RefinedWeb](https://arxiv.org/abs/2306.01116),[Gopher](https://arxiv.org/abs/2112.11446) |
| rps_doc_stop_word_fraction | The ratio between the number of stop words and the number of words in the document. Stop words are          obtained from [          https://github.com/6/stopwords-json](https://github.com/6/stopwords-json). | Natural Language | [RefinedWeb](https://arxiv.org/abs/2306.01116),[Gopher](https://arxiv.org/abs/2112.11446) |
| rps_doc_symbol_to_word_ratio | The ratio of symbols to words in the content.. Symbols are defined "#", "...", and "…". | Natural Language | [RefinedWeb](https://arxiv.org/abs/2306.01116),[Gopher](https://arxiv.org/abs/2112.11446) |
| rps_doc_frac_unique_words | The fraction of unique words in the content. This is also known as the degeneracy of a text sample. Calculated based on the normalised content. | Natural Language | [Pretrainer's Guide](https://arxiv.org/abs/2305.13169) |
| rps_doc_unigram_entropy | The entropy of the unigram distribution of the content. This measures the diversity of the content and is computed using sum(-x / total * log(x / total)) where the sum is taken over counts of unique words in the normalised content. | Natural Language | - |
| rps_doc_word_count | The number of words in the content after normalisation. | Natural Language | [RefinedWeb](https://arxiv.org/abs/2306.01116),[Gopher](https://arxiv.org/abs/2112.11446) |
| rps_lines_ending_with_terminal_punctution_mark | Indicates whether a line ends with a terminal punctuation mark. A terminal punctuation mark is defined as one o: ".", "!", "?", "". | Natural Language | [C4](https://arxiv.org/abs/1910.10683) |
| rps_lines_javascript_counts | The number of occurrences of the word "javascript" in each line. | Natural Language | [C4](https://arxiv.org/abs/1910.10683) |
| rps_lines_num_words | The number of words in each line. This is computed based on the normalised text. | Natural Language | [C4](https://arxiv.org/abs/1910.10683),[RefinedWeb](https://arxiv.org/abs/2306.01116) |
| rps_lines_numerical_chars_fraction | The ratio between number of numerical characters and total number of characters in each line. This is based on the normalised content. | Natural Language | [RefinedWeb](https://arxiv.org/abs/2306.01116) |
| rps_lines_start_with_bulletpoint | Whether the lines that start with a bullet point symbol. The following set of unicodes are considered a bullet point: \u2022 (bullet point), \u2023 (triangular bullet point), \u25B6 (black right pointing triangle), \u25C0 (black left pointing triangle), \u25E6 (white bullet point), \u25A0 (black square), \u25A1 (white square), \u25AA (black small square), \u25AB (white small square), \u2013 (en dash). | Natural Language | [RefinedWeb](https://arxiv.org/abs/2306.01116),[Gopher](https://arxiv.org/abs/2112.11446) |
| rps_lines_uppercase_letter_fraction | The ratio between number of uppercase letters and total number of characters in each line. This is based on the raw text. | Natural Language | [RefinedWeb](https://arxiv.org/abs/2306.01116) |
| rps_doc_num_sentences | The number of sentences in the content. This is calculated using the regular expression r'\b[^.!?]+[.!?]*'. | Natural Language | [C4](https://arxiv.org/abs/1910.10683) |

| Annotation Tag | Description | Category | Reference |
|---|---|---|---|
| rps_doc_frac_chars_dupe_10grams | The fraction of characters in duplicate word 10grams. | Repetitiveness | [RefinedWeb](https://arxiv.org/abs/2306.01116),[Gopher](https://arxiv.org/abs/2112.11446) |
| rps_doc_frac_chars_dupe_5grams | The fraction of characters in duplicate word 5grams. | Repetitiveness | [RefinedWeb](https://arxiv.org/abs/2306.01116),[Gopher](https://arxiv.org/abs/2112.11446) |
| rps_doc_frac_chars_dupe_6grams | The fraction of characters in duplicate word 6grams. | Repetitiveness | [RefinedWeb](https://arxiv.org/abs/2306.01116),[Gopher](https://arxiv.org/abs/2112.11446) |
| rps_doc_frac_chars_dupe_7grams | The fraction of characters in duplicate word 7grams. | Repetitiveness | [RefinedWeb](https://arxiv.org/abs/2306.01116),[Gopher](https://arxiv.org/abs/2112.11446) |
| rps_doc_frac_chars_dupe_8grams | The fraction of characters in duplicate word 8grams. | Repetitiveness | [RefinedWeb](https://arxiv.org/abs/2306.01116),[Gopher](https://arxiv.org/abs/2112.11446) |
| rps_doc_frac_chars_dupe_9grams | The fraction of characters in duplicate word 9grams. | Repetitiveness | [RefinedWeb](https://arxiv.org/abs/2306.01116),[Gopher](https://arxiv.org/abs/2112.11446) |
| rps_doc_frac_chars_top_2gram | The fraction of characters in the top word 2gram. | Repetitiveness | [RefinedWeb](https://arxiv.org/abs/2306.01116),[Gopher](https://arxiv.org/abs/2112.11446) |
| rps_doc_frac_chars_top_3gram | The fraction of characters in the top word 3gram. | Repetitiveness | [RefinedWeb](https://arxiv.org/abs/2306.01116),[Gopher](https://arxiv.org/abs/2112.11446) |
| rps_doc_frac_chars_top_4gram | The fraction of characters in the top word 4gram. | Repetitiveness | [RefinedWeb](https://arxiv.org/abs/2306.01116),[Gopher](https://arxiv.org/abs/2112.11446) |
| rps_doc_ldnoobw_words | The number of sequences of words that are contained in the          List-of-Dirty-Naughty-Obscene-and-Otherwise-Bad-Words blocklist. The blocklist is obtained from [          https://github.com/LDNOOBW/List-of-Dirty-Naughty-Obscene-and-Otherwise-Bad-Words](https://github.com/LDNOOBW/List-of-Dirty-Naughty-Obscene-and-Otherwise-Bad-Words) | Sensitive / toxic content | [C4](https://arxiv.org/abs/1910.10683) |
| rps_doc_ut1_blacklist | A categorical id corresponding to the list of categories of the domain of the document. Categories          are          obtained from the UT1 blacklist. The list is obtained from [          https://dsi.ut-capitole.fr/blacklists/](https://dsi.ut-capitole.fr/blacklists/) | Sensitive / toxic content | [RefinedWeb](https://arxiv.org/abs/2306.01116) |
| minhash_signature_0.7 | Banded minhash signature of the document, for fuzzy deduplication at Jaccard similarity 0.7. The signature is based on 128 hash functions and grouped into 14 bands and 9 rows for LSH. | Deduplication | [SlimPajama](https://huggingface.co/datasets/cerebras/SlimPajama-627B),[RefinedWeb](https://arxiv.org/abs/2306.01116) |
| minhash_signature_0.8 | Banded minhash signature of the document, for fuzzy deduplication at Jaccard similarity 0.8. The signature is based on 128 hash functions and grouped into 9 bands and 13 rows for LSH. | Deduplication | [SlimPajama](https://huggingface.co/datasets/cerebras/SlimPajama-627B),[RefinedWeb](https://arxiv.org/abs/2306.01116) |
| minhash_signature_0.9 | Banded minhash signature of the document, for fuzzy deduplication at Jaccard similarity 0.9. The signature is based on 128 hash functions and grouped into 5 bands and 25 rows for LSH.. | Ded |
