---
title: 'FAQ: Building LLMs with RedPajama-v2, a 30 trillion token web dataset'
topic: models
subtopic: fine-tuning
secondary_topics:
- models/benchmarks
summary: FAQ-style technical explanation of building LLMs with the RedPajama-v2 dataset.
source: together
url: https://www.together.ai/blog/redpajama-v2-faq
author: Together AI
published: '2024-05-01'
fetched: '2026-07-11T04:25:29Z'
classifier: codex
taxonomy_rev: 1
words: 3455
content_sha256: 81c9bc303fce0660450a5cd1a21b693fb8077a57378019d7fdf4ce8f44f771e7
triage: keep
skip_reason: null
---

# FAQ: Building LLMs with RedPajama-v2, a 30 trillion token web dataset

![__wf_reserved_inherit](https://cdn.prod.website-files.com/69654e88dce9154b5f12070c/699e0b1877b4a65fc53779dc_6632825147b0995b6c0002d4_snowflake-llamaaa-upscaled_v2.png)

Over the past several months, we have been amazed by the community's engagement with the RedPajama-V2 dataset. With over 20,000 downloads per month, the 30 trillion tokens of deduplicated web data, along with their quality signals, have been used to train leading models like the recently released [Snowflake Arctic LLM](https://www.snowflake.com/blog/arctic-open-efficient-foundation-language-models-snowflake/).

RedPajama-v2 is designed as a high-recall vs high-precision dataset. This approach enables researchers to employ different data selection techniques and experimentally discover recipes that produce downstream models with desired properties. Data selection from RedPajama v2 can also be used to fine-tune pre trained models on class of documents that imbue certain functionality or specialization required of models.

To facilitate dataset use and help the community maximize its value, we've compiled a list of frequently asked questions.

### Q: Should I use the RedPajama-V2 Dataset out of the box?

RedPajama-V2 is conceptualized as a pool of data that serves as a foundation for creating high quality datasets. The dataset is thus not intended to be used out of the box and, depending on the application, data should be filtered out using the quality signals that accompany the data. With this dataset, we take the view that the optimal filtering of data is dependent on the intended use. Our goal is to provide all the signals and tooling that enables this.

### Q: Is RedPajama-V2 deduplicated?

The raw dataset is not deduplicated. This is an intentional design choice to preserve as much information in the raw data as possible to facilitate research into the role and best method of deduplication. Instead, we provide duplication as one of the *signals —* the ids of documents which are duplicated across the entire corpus. The deduplication was performed using a Bloomfilter and the hashes of the web documents (i.e., of the raw .wet documents).  These ids can be used to deduplicate the dataset as shown below. In particular, the dataset loaded via the HuggingFace dataloader provides the raw data with the quality signals and duplication tags and is not deduplicated. We also provide minhash signatures for further fuzzy deduplication at different levels of similarity.

### Q: What does the structure of the dataset look like?

The basic structure of the dataset largely follows the output logic of the CCNet pipeline where data is partitioned into shards and grouped according to language and the perplexity bucket. The documents (i.e., the text data) are organised according to the following structure:

The basic structure of the dataset largely follows the output logic of the CCNet pipeline where data is partitioned into shards and grouped according to language and the perplexity bucket. The documents (i.e., the text data) are organised according to the following structure:

```

```
`documents/`//_.json.gz
                where **" "** corresponds to the commoncrawl snapshot (for example 2023-14), the

**"**" is a number in the range {0000…4999},

**"**" denotes the language, and

**"**" denotes the perplexity bucket (one of head, middle, or tail). The other components of the RedPajama-V2 dataset follow this structure closely. The jsonl files containing the quality signals are organised according to

```

```
`quality_signals/`//_.signals.json.gz
                Similarly, the parquet files containing the minhash signatures and the parquet files containing the ids of duplicate documents are organised according to

```

```
`minhash/`//_.minhash.parquet
                And

```

```
`duplicates/`//_.duplicates.parquet


### Q: How can I obtain an exactly deduplicated version of the dataset?

The data can be deduplicated using the parquet files which contain ids of duplicate documents. The structure of the duplicate files mirrors the overall structure of the documents files. These duplicate files follow the schema (shard_id, doc_id, digest) where shard_id indicates the shard in which the duplicate document appears, doc_id corresponds to the id of the document which is built using shard_id/<idx> where idx is the row inside the shard. To deduplicate the documents, you can build on the following code snippet:

```

```
```
import gzip
import io
import json
import pyarrow.parquet as pq
import requests
DOCS_URL_PATTERN = "https://data.together.xyz/redpajama-data-v2/v1.0.0/documents/{}"
DUPES_URL_PATTERN = "https://data.together.xyz/redpajama-data-v2/v1.0.0/duplicates/{}"
SHARD_ID = "2023-14/0000/en_head.json.gz"
# download duplicates
print("Downloading duplicates...")
duplicates_req = requests.get(
    DUPES_URL_PATTERN.format(
        f"{SHARD_ID.replace('.json.gz', '.duplicates.parquet')}"
    )
)
duplicate_ids = set(
    pq.read_table(
        io.BytesIO(duplicates_req.content),
        columns=["doc_id"]
    )["doc_id"].to_pylist()
)
# download documents
print("Downloading documents...")
documents_req = requests.get(DOCS_URL_PATTERN.format(SHARD_ID))
# discard duplicates
unique_documents = []
with gzip.open(io.BytesIO(documents_req.content), "rt", encoding="utf-8") as f:
    for idx, line in enumerate(f):
        doc_id = f"{SHARD_ID}/{idx}"
        if doc_id in duplicate_ids:
            continue
        unique_documents.append(json.loads(line))
print(f"Found {len(unique_documents)} unique documents.")

```
        It is important to keep in mind that the duplicate files don't contain the first occurrence of a duplicated document.

### Q: The dataset also comes with MinHash signatures. How can I use them for fuzzy deduplication?

We provide MinHash signatures (using 128 permutations) which are precomputed for running locality sensitive hashing (LSH) at similarity levels 0.7, 0.8, 0.9, 1.0. To run the LSH step, we provide a single-node [implementation](https://github.com/togethercomputer/RedPajama-Data/blob/main/app/src/run_lsh.py) in the RedPajama-Data repo. The implementation is based on the [Polars library](https://pola.rs/) for bucketing the documents and [networkit](https://networkit.github.io/) for the connected components step. As a minimal working example to run LSH, from the root of the RedPajama Github repository, you can run the following three steps:

```

```
```
# Step 1: Download listings
DATA_ROOT="${HOME}/path/to/data" # make sure this is an absolute path
mkdir -p "${DATA_ROOT}/listings"
listings_file="listings/en-2023-06-head_middle.txt"
wget "https://data.together.xyz/redpajama-data-v2/v1.0.0/${listings_file}" -O "${DATA_ROOT}/${listings_file}"
# Step 2: Download MinHash signatures
# we read the first 5 lines here to run the example
head -n5 "${DATA_ROOT}/${listings_file}" | while read line;
do
    url="https://data.together.xyz/redpajama-data-v2/v1.0.0/minhash/${line}.minhash.parquet"
    dest="${DATA_ROOT}/minhash/${line}.minhash.parquet"
    mkdir -p $(dirname $dest)
    wget "$url" -O "$dest"
    echo "minhash/${line}.minhash.parquet" >> "${DATA_ROOT}/minhash_listings.txt"
done
# Step 3: Run LSH at similarity level 0.7
cd app/
python3 src/run_lsh.py \
--input_base_uri "file://${DATA_ROOT}/" \
--output_dir "${DATA_ROOT}/minhash_clusters/" \
--similarity 0.7 \
--num_perm 128 \
--listings "${DATA_ROOT}/minhash_listings.txt"
```
        This will result in one parquet file for each input file, containing the MinHash cluster id for every (fuzzy duplicate) document in the corresponding `documents` file. You can then use these parquet files in the same manner as in the exact deduplication steps to discard any documents which are deduplicated. We tested this implementation to deduplicate 200M documents on a single AWS node with 64 (logical) cores and 500GB RAM. The total running time for this setup was 45 minutes.

### Q: The download speed using the code snippet on HuggingFace is slow. How can I download the dataset faster?

To speed up downloading, you can either pass a custom download configuration to the HuggingFace dataloader and specify the number of processes, or you can directly download the data files using a parallel command line utility like aria2c.

### Q: Is it possible to filter the dataset using other metadata such as the url domain or the date?

Yes, this is possible using metadata fields which were extracted with the CCNet pipeline. The fields available are `url`, `date_download`, `source_domain` and `title` and are available both via the HuggingFace dataloader (in the subdict "meta"), and in the plain documents files (as top-level fields in each jsonl record). We remark that the `date_download` field refers to the date when the website was crawled/downloaded and not when the content was created – it is thus only an approximation to the true timestamp of content creation. An example of the fields is:

```
{
	"url": "http://bluegrass-conceptsgifts.com/all-you-need-to-learn-about-biography/",
	"date_download": "2023-01-26T21:25:04Z",
	"source_domain": "bluegrass-conceptsgifts.com",
	"title": "All You Need To Learn About Biography. - blue gres"
	...
}
```
So for example, to filter documents to only include such with https and .com urls, and only from crawls done in January, you can start from the following code snippet, which uses the HuggingFace dataloader:

```
from datasets import load_dataset
from datetime import datetime as dt
import json
import re
ds = load_dataset(
	"togethercomputer/RedPajama-Data-V2", name="sample", streaming=True
)
url_pattern = re.compile(r"https://[^\s]+.com/[^\s]+")
filtered_instances = []
for instance in ds["train"]:
	metadata = json.loads(instance["meta"])

	url = metadata["url"]
	if url_pattern.search(url) is None:
		continue
	date_download = metadata["date_download"]
	if dt.fromisoformat(date_download).month != 1:
		continue
	filtered_instances.append(instance)
```
### Q: What is the total size of the dataset?

The total dataset is composed of four components with the following (total) sizes:

- The text documents (170TB)
- The quality signals (28TB)
- The precomputed minhash signatures (62TB)
- The ids of (exact) duplicates (260GB)

The total dataset size is thus ~260TB. The total dataset sizes for individual snapshot sizes range between 1TB and 4 TB (older snapshots are generally smaller). For example, for the 2023-14 snapshot we have:

- The text documents: 2.2TB (1.5 TB en, 224GB de, 187GB fr, 184GB es, 108GB it)
- The quality signals: 436GB (291GB en, 45GB de, 41GB fr, 37GB es, 22GB it)
- The precomputed minhash signatures: 1TB (674GB en, 113GB de, 95GB fr, 94GB es, 59GB it)
- The ids of (exact) duplicates: 604MB (380MB en, 87MB de, 60MB fr, 46MB es, 32MB it)

### Q: What is the reasoning behind partitioning the dataset?

The dataset is split into `head_middle` and `tail` partitions. The `head_middle` partition comes annotated with quality signals and deduplication ids. For the `tail` partition, we only provide the text documents.

The head, middle and tail buckets partition the dataset into three equally sized parts based on the perplexity of a small language model trained on Wikipedia. It is essentially an indicator of how similar the vocabulary (of a given document) is to Wikipedia. So, in general, the data in the head and middle is of higher quality compared to the tail partition. However, this is only with respect to the Wikipedia model, so there will still be good quality text in tail, just with a vocab different from Wikipedia. This partitioning originally comes from the CCNet pipeline which we have used to process the raw CommonCrawl data.

### Q: A common problem which occurs are 500 error responses when downloading the dataset with the HuggingFace dataloader. How can I ensure retries?

To ensure retries, you can pass a download config to the load_dataset function directly, and set the number of retries to something larger than 1 (the default). For example, if you want to set the number of max retries to 5, you can do

```
from datasets import load_dataset, DownloadConfig
dl_config = DownloadConfig(max_retries=5)
ds = load_dataset(
	"togethercomputer/RedPajama-Data-V2",
	name="default",
	partition="head_middle",
	snapshots=["2023-06"],
	languages=["en"],
	download_config=dl_config
)
```
### Q: I saw that there is a large number of ellipses in some documents. How can I remove those documents from the dataset?

This is a common artifact of web-based text data. To reduce the occurrence of such documents, we provide the document level quality signal `rps_doc_symbol_to_word_ratio` which is the ratio between the number of occurrences of the symbols `#` and `...` and the number of words in the document. You can set a threshold above which a document gets discarded so that such documents appear less frequently. For example, in Gopher, the threshold has been set to 0.1. Overall, we provide over 40 quality signals that can be used to create dataset which satisfy different quality thresholds. We provide an example that makes use of the HuggingFace dataloader in our [blog post](https://www.together.ai/blog/redpajama-data-v2). Another example of the use of the threshold's can be found in [Snowflake's Arctic Cookbook series](https://www.notion.so/FAQ-Building-LLMs-with-RedPajama-v2-a-30-trillion-token-web-dataset-e4c1fb3e94dd4e4386645ba0454e6ee6?pvs=21) and its approach to data curation.

### Q: How do I need to interpret the format of the quality signals?

We choose a format that is able to represent quality signals at different levels of granularity: document level, line level, and even word or character level. To get such a unified representation, we follow the format proposed in the [Dolma dataset](https://github.com/allenai/dolma/tree/main). Specifically, each quality signal is represented by an array of tuples `(start, end, score)` where start and end correspond to the span in the document string where the score applies. For example, if a document is composed of two lines, the first one containing 2 words, and the second one containing 10 words, and the quality signal measures the number of words in each line, the corresponding quality signal would look like

```
{
	"rps_lines_num_words": [[0, 25, 2], [25, 124, 10]]
}
```
### Q: I would like the resulting dataset after filtering to resemble data from a high quality source such as wikipedia or openwebtext. How can I use the quality signals for this purpose?

To get a dataset which is similar to a high-quality domain, you can use one of the ML-based quality signals. We provide two different ML-based quality signals. The first method is based on fasttext classifiers which were trained to classify between random documents from the corpus, and a high quality source. The signal `rps_doc_ml_palm_score` corresponds to the high quality domain being an even mix of openwebtext, books and wikipedia and is a classifier similar to the one used to create the dataset for [PaLM](https://arxiv.org/pdf/2204.02311.pdf). The second such quality signal is implemented in `rps_doc_ml_wikiref_score` where the high quality domain is composed of websites referenced by wikipedia articles. This kind of classifier was used to create the original LLaMA models and also in the [RedPajama-1T dataset](https://huggingface.co/datasets/togethercomputer/RedPajama-Data-1T). The second ML based method is the usage of importance weights, originally proposed by [Xie et al](https://arxiv.org/abs/2302.03169). This technique measures the similarity to a high quality domain using the log likelihood ratios between generative bag-of-{1,2}-wordgram models trained on random CommonCrawl data and a high quality source domain. They are provided in the quality signals as `rps_doc_<high-quality-domain>_importance` where the placeholder `<high-quality-domain>` is one of books, wikipedia, and openwebtext. We recommend tuning the thresholds for these quality signals for your specific application.

### Example: Data Selection via Importance Resampling

In this example, we use the importance weights provided in RPv2 to select data which is similar to Wikipedia as the high quality target domain. We then use the [Together Python library](https://docs.together.ai/docs/fine-tuning-python) to finetune a model on this high quality dataset extracted from RPv2.

The use of importance weights were proposed in the paper ["Data Selection for Language Models via Importance Resampling" by Xie et al.](https://arxiv.org/abs/2302.03169) The proposed technique is a way to extract samples whose distribution matches the target domain. Formally, these weights are defined as the log-likelihood ratio between a language model of the target vs. the source domain

$$w_x = \log \left(\frac{p(x)}{q(x)}\right)$$

where larger weights indicate that the sample x is more likely to correspond to the target distribution. In the following example, we use the Wikipedia importance weights available in the RPv2 dataset to sample a high quality subset. Let us first initialize the dataset loader in streaming mode:

```
dataset = load_dataset(
	"togethercomputer/RedPajama-Data-V2",
	trust_remote_code=True,
	name="sample-10B",
	streaming=True
)["train"]
```
Next, we define a function which parses a single sample in the dataset and returns the text, the language, and the importance weight:

```
def parse_sample(sample: Dict[str, str]):
    """Parse a sample and extract its text, language and importance weight."""
    # fetch raw content
    raw_content = sample["raw_content"]
    # Extract language
    meta = json.loads(sample["meta"])
    language = meta["language"]
    # extract quality signals
    quality_signals = json.loads(sample["quality_signals"])
    importance_weight = quality_signals["rps_doc_wikipedia_importance"][0][2]
    return raw_content, language, importance_weight
```
Now, we implement a function which uses Gumbel Top-k sampling to sample from the dataset without replacement. To keep just the top k-samples as we stream through the dataset, we use a priority queue.

```
def importance_resampling(
    dataset: Dataset, num_samples: int, pool_size: int, language: str
) -> List[Tuple[float, str]]:
    """Importance resampling algorithm. This function uses Gumbel-top-K to sample a subset of the
    dataset based on the importance weights."""
    priority_queue = []
    for i, sample in progress.track(
        enumerate(dataset), description="Importance resampling", total=pool_size
    ):
        if i > pool_size:
            break
        # Parse sample and extract its text, language and importance weight
        text, sample_language, log_importance_weight = parse_sample(sample)
        # Skip samples in different languages
        if sample_language != language:
            continue
        gumbel_noise = -math.log(-math.log(random.uniform(0, 1)))
        gumbel_weight = log_importance_weight + gumbel_noise
        # Add item with its Gumbel weight to the priority queue
        if len(priority_queue) < num_samples:
            heapq.heappush(priority_queue, (gumbel_weight, text))
        else:
            # If the queue is full, push new item and pop the smallest
            heapq.heappushpop(priority_queue, (gumbel_weight, text))
    return priority_queue

```
We put the pieces together in a main function which performs the following steps:

- initialize dataset
- sample from the dataset with importance weights
- save the data to a jsonl file which we can upload to the Together API

```
def main():
		# setup data directory
    Path("data").mkdir(exist_ok=True)
    # downlaod dataset
    dataset = load_dataset(
        "togethercomputer/RedPajama-Data-V2",
        trust_remote_code=True,
        name="sample-10B",
        streaming=True,
    )["train"]
    dataset = dataset.shuffle(seed=SEED)
    documents = importance_resampling(
        dataset, num_samples=NUM_SAMPLES, pool_size=100 * NUM_SAMPLES, language=LANGUAGE
    )
    print(f"Number of high quality samples found: {len(documents)}")
    # Save samples to file
    data_filepath = "data/dsir_samples.jsonl"
    Path(data_filepath).parent.mkdir(exist_ok=True, parents=True)
    with open(data_filepath, "wt", encoding="utf-8") as f:
        for weight, item in documents:
            f.write(json.dumps({"text": item, "weight": weight}) + "\n")
		# upload data to Together Cloud
		# ...
```
In the following table, we can see sequences of 200 characters of samples in the tails of the DSIR weight distribution which were selected, and some which were rejected:

| DSIR Selection (upper Tail) | Rejected Samples (lower tail) |
|---|---|
| character of the morality.\nJohn Marston: wrote Antonio and Mellida, 1602; Antonio's Revenge,\n1602; Sophonisba, a Wonder of Women, 1606; The Insatiate Countess,\n1603, and many other plays. Ma | dDz3/8] ^G,/2\n[^c/4^D,3/2^C/4] [d/4D/4] [^c/4^C/4] [B/4B,/4] [^G/2^A,/4^F,/8^G,/2]\nz3/8 [^D/2^F,/4^A,/4^D,/2] z/4 [^F/2^G,/2^F,3/8] z/8 [^G3/8^G,/4] z/4\n[=F/4^C/4^C,/4=F,/4] z/4 [F/4^C/4^C,/8F,/4] z3/ |
| smoking ruins could alone distinguish the solitude of nature from the desolation of man. The flourishing city of Mentz was surprised and destroyed; and many thousand Christians were inhumanly massacr | es/terrain/off-map/fade_corner_bottom_right_odd_editor.png\n/usr/share/games/wesnoth/data/core/images/terrain/off-map/fade_corner_top_left.png\n/usr/share/games/wesnoth/data/core/images/terrain/off-map/ |
| the robbery to the police. The Brisbane Courier in reporting this robbery said it was the first case of bushranging that had taken place in Queensland, and hoped that that colony was not about to have | /bestblog-open.blogspot.com [http://pt.tapatalk.com/redirect.php?app_id=4&fid=8678&url=https://bestblog-open.blogspot.com](http://pt.tapatalk.com/redirect.php?app_id=4&fid=8678&url=https://bestblog-open.blogspot.com)[http://my.effairs.at/austriatech/link/t?i=2504674541756&v=0&c=anonym&e=anonym@a](http://my.effairs.at/austriatech/link/t?i=2504674541756&v=0&c=anonym&e=anonym@a) |
| of Kentucky (dissertation) by Sharon Barrow Childs, p.138\nWalker, Anna Brown\nWallace, Samuel III "Bud"\nWilkinson, Doris Y.\nSocial Work w/English minor\nThe Fascinating Story of Black Kentuckians by A. | [http://r.com/samsung-stormwash-42-decibel-stainless-steel-dishwasher-459-today-only-at-lowes/](http://r.com/samsung-stormwash-42-decibel-stainless-steel-dishwasher-459-today-only-at-lowes/)50% Yearly 2019-11-30 23:01\n[https://www.hotdealstar.com/tramontina-enameled-cast-iron-dutch-oven-6.5-qt-25.50-wal](https://www.hotdealstar.com/tramontina-enameled-cast-iron-dutch-oven-6.5-qt-25.50-wal) |

We can now use the Together Python library to check the format of the data sample, upload it the the cloud and finetune a model (Mistral-7B):

```
# ensure that the data file is in the correct format
check_resp = together.Files.check(file=data_filepath)
print(f"data format check:\n{json.dumps(check_resp, indent=2)}")
if not check_resp["is_check_passed"]:
    raise ValueError(f"Data file {data_filepath} is not in the correct format")
# upload sample to Together file server
print(f"uploading {data_filepath} to Together file server...")
upload_resp = together.Files.upload(file=data_filepath)
print(
    "upload to Together file server completed. Response:\n",
    json.dumps(upload_resp, indent=2),
)
file_id = upload_resp["id"]
# finetune model via Together API
ft_resp = together.Finetune.create(
    training_file=file_id,
    model="mistralai/Mistral-7B-v0.1",
    n_epochs=4,
    suffix="dsir-finetune",
)
print(f"Finetune job submitted. Response:\n{json.dumps(ft_resp, indent=2)}"
```
Once the fine-tune job completes, you will be able to see your model in the Together [Playground](https://api.together.xyz/playground). Follow the instructions in the [inference documentation](https://docs.together.ai/docs/inference-rest) to deploy the model.

Below is the full example:

```
import heapq
import json
import math
import os
import random
from pathlib import Path
from typing import Dict, List, Tuple
import together
from datasets import Dataset, load_dataset
from rich import progress
# Load Together API key
TOGETHER_API_KEY = os.getenv("TOGETHER_API_KEY")
if TOGETHER_API_KEY is None:
    raise ValueError("TOGETHER_API_KEY environment variable is not set")
# Constants
LANGUAGE = "en"
SEED = 42
NUM_SAMPLES = 100
random.seed(SEED)
def parse_sample(sample: Dict[str, str]):
    """Parse a sample and extract its text, language and importance weight."""
    # fetch raw content
    raw_content = sample["raw_content"]
    # Extract language
    meta = json.loads(sample["meta"])
    language = meta["language"]
    # extract quality signals
    quality_signals = json.loads(sample["quality_signals"])
    importance_weight = quality_signals["rps_doc_wikipedia_importance"][0][2]
    return raw_content, language, importance_weight
def importance_resampling(
    dataset: Dataset, num_samples: int, pool_size: int, language: str
) -> List[Tuple[float, str]]:
    """Importance resampling algorithm. This function uses Gumbel-top-K to sample a subset of the
    dataset based on the importance weights."""
    priority_queue = []
    for i, sample in progress.track(
        enumerate(dataset), description="Importance resampling", total=pool_size
    ):
        if i > pool_size:
            break
        # Parse sample and extract its text, language and importance weight
        text, sample_language, log_importance_weight = parse_sample(sample)
        # Skip samples in different languages
        if sample_language != language:
            continue
        gumbel_noise = -math.log(-math.log(random.uniform(0, 1)))
        gumbel_weight = log_importance_weight + gumbel_noise
        # Add item with its Gumbel weight to the priority queue
        if len(priority_queue) < num_samples:
            heapq.heappush(priority_queue, (gumbel_weight, text))
        else:
            # If the queue is full, push new item and pop the smallest
            heapq.heappushpop(priority_queue, (gumbel_weight, text))
    return priority_queue
def main():
    # setup data directory
    Path("data").mkdir(exist_ok=True)
    # downlaod dataset
    dataset = load_dataset(
        "togethercomputer/RedPajama-Data-V2",
        trust_remote_code=True,
        name="sample-10B",
        streaming=True,
    )["train"]
    dataset = dataset.shuffle(seed=SEED)
    documents = importance_resampling(
        dataset, num_samples=NUM_SAMPLES, pool_size=100 * NUM_SAMPLES, language=LANGUAGE
    )
    print(f"Number of high quality samples found: {len(documents)}")
    # Save samples to file
    data_filepath = "data/dsir_samples.jsonl"
    Path(data_filepath).parent.mkdir(exist_ok=True, parents=True)
    with open(data_filepath, "wt", encoding="utf-8") as f:
        for weight, item in documents:
            f.write(json.dumps({"text": item, "weight": weight}) + "\n")
    # ensure that the data file is in the correct format
    check_resp = together.Files.check(file=data_filepath)
    print(f"data format check:\n{json.dumps(check_resp, indent=2)}")
    if not check_resp["is_check_passed"]:
        raise ValueError(f"Data file {data_filepath} is not in the correct format")
    # upload sample to Together file server
    print(f"uploading {data_filepath} to Together file server...")
    upload_resp = together.Files.upload(file=data_filepath)
    print(
        "upload to Together file server completed. Response:\n",
        json.dumps(upload_resp, indent=2),
    )
    file_id = upload_resp["id"]
    # finetune model via Together API
    ft_resp = together.Finetune.create(
        training_file=file_id,
        model="mistralai/Mistral-7B-v0.1",
        n_epochs=4,
        suffix="dsir-finetune",
    )
    print(f"Finetune job submitted. Response:\n{json.dumps(ft_resp, indent=2)}")
if __name__ == "__main__":
    main()
```
If you have further questions about using the RedPajama V2 dataset, please [reach out](https://www.together.ai/contact)! We'd love to collaborate and help answer any questions you have!
