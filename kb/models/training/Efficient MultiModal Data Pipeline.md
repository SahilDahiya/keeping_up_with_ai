---
title: Efficient MultiModal Data Pipeline
kind: blog
topic: models
subtopic: training
secondary_topics: []
summary: 'Rebuilds nanoVLM''s multimodal data pipeline in five stages to stop GPUs
  idling on padding: from naive padding to constrained batching and sequence packing
  with knapsack-style grouping, showing the padding-token waste eliminated at each
  step.'
triage: null
skip_reason: null
source: huggingface
url: https://huggingface.co/blog/mmdp
author: Aritra Roy Gosthipaty; Luis; Andres Marafioti; Sergio Paniego; Pedro Cuenca
published: '2025-07-08'
fetched: '2026-07-14T22:11:12Z'
classifier: claude
taxonomy_rev: 1
words: 1647
content_sha256: 5732e1fc299fe01e0c7e4cef4f7359903b62f10c273231482cfddb2ecdfb9705
---

# Efficient MultiModal Data Pipeline

# 
	[
		
	](https://huggingface.co#efficient-multimodal-data-pipeline)
	
		Efficient MultiModal Data Pipeline
	

 [Update on GitHub](https://github.com/huggingface/blog/blob/main/mmdp.md)

[  Upvote 73 ](https://huggingface.co/login?next=%2Fblog%2Fmmdp)

![Aritra Roy Gosthipaty's avatar](https://cdn-avatars.huggingface.co/v1/production/uploads/608aabf24955d2bfc3cd99c6/-YxmtpzEmf3NKOTktODRP.jpeg) 

  ![Luis's avatar](https://cdn-avatars.huggingface.co/v1/production/uploads/6630afa2d40e9b46f95b4c15/H1xNxJztbOFi8IZQu7XjV.jpeg) 

  ![Andres Marafioti's avatar](https://cdn-avatars.huggingface.co/v1/production/uploads/65d66b494bbd0d92b641cdbb/6-7dm7B-JxcoS1QlCPdMN.jpeg) 

  ![Sergio Paniego's avatar](https://cdn-avatars.huggingface.co/v1/production/uploads/61929226ded356549e20c5da/ONUjP2S5fUWd07BiFXm0i.jpeg) 

  ![Pedro Cuenca's avatar](https://cdn-avatars.huggingface.co/v1/production/uploads/1617264212503-603d25b75f9d390ab190b777.jpeg) 

  Sound familiar? We've been there. After some detective work on our [nanoVLM](https://github.com/huggingface/nanovlm) project, we [discovered](https://x.com/andimarafioti/status/1937518080474906641) the real culprit wasn't our model or hardware, it was our data pipeline being incredibly wasteful.

Here's what we found:

- **Idle GPUs**: Our model was literally waiting around for data to show up
- **Padding hell**: Every batch was stuffed with useless padding tokens that contributed nothing to training

In this post we build an efficient pipeline in **five stages**. In each stage we add or remove from the previous step and comment on what went right and what did not.

### 
	[
		
	](https://huggingface.co#table-of-contents)
	
		Table of Contents:
	

- [Stage 0: Pre Requisites](https://huggingface.co#stage-0-preparation)
- [Stage 1: Visualising the Dataset](https://huggingface.co#stage-1-visualising-the-dataset)
- [Stage 2: Naive Padding](https://huggingface.co#stage-2-naive-padding)
- [Stage 3: Constrained Padding](https://huggingface.co#stage-3-constrained-padding)
- [Stage 4: Packing Smarter with Knapsacks](https://huggingface.co#stage-4-packing-smarter-with-knapsacks)
- [Stage 5: Knapsack for Multimodal Data](https://huggingface.co#stage-5-knapsacks-for-multimodal-data)
- [Conclusion](https://huggingface.co#conclusion)

## 
	[
		
	](https://huggingface.co#stage-0-preparation)
	
		[Stage 0] Preparation
	

To make it easier to follow the data preparation tasks, we created a separate repo laser-focused on the data pipeline only. We hope this will be much easier to understand that reading the code once integrated with the nanoVLM repository. In addition, this could be useful to bootstrap other data pipelines!

Repository: [https://github.com/ariG23498/mmdp](https://github.com/ariG23498/mmdp)

To follow along, all you need to do is clone the repository. It contains the final data preparation tasks, but it's designed to showcase each step of the way.

```
$ git clone https://github.com/ariG23498/mmdp.git
```
## 
	[
		
	](https://huggingface.co#stage-1-visualising-the-dataset)
	
		[Stage 1] Visualising the Dataset
	

Before optimizing anything, we need to understand what we are working with. Our multimodal dataset has images, text prompts, and responses.

```
$ uv run 01_check_dataset.py
```
![Dataset Sample](https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/blog/mmdp/01.png)


Getting familiar with your training data is crucial for success. The previous script shows a random sample each time you run it; you may want to copy the snippet to a notebook and run it multiple times to get a feeling about the data.

## 
	[
		
	](https://huggingface.co#stage-2-naive-padding)
	
		[Stage 2] Naive Padding
	

Our first training attempt used the obvious (and very frequent) approach:

- Tokenize everything
- Find the longest sequence in each batch
- Pad everything else to match

```
$ uv run 02_naive_pad_dataloader.py
```
The results were painful. Look at this visualization:

![Naive Padding Waste](https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/blog/mmdp/02.png)


See all that gray? That's padding. That's the GPU processing absolutely nothing while you pay for compute time. We were wasting roughly 60% of our batch on empty tokens.

## 
	[
		
	](https://huggingface.co#stage-3-constrained-padding)
	
		[Stage 3] Constrained Padding
	

Our next move was simple. Set a global maximum length and stick to it. If a sample was too long, we'd just drop it.

![Constrained Padding](https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/blog/mmdp/03.png)


As you might have noticed that the batch now has one sample less. This is due to the filtering process. This helped, but we were still padding everything to the same fixed length regardless of actual content. Better than before, but still wasteful.

## 
	[
		
	](https://huggingface.co#stage-4-packing-smarter-with-knapsacks)
	
		[Stage 4]: Packing Smarter with Knapsacks
	

Now we’re ready to rethink batching entirely. Padding is the enemy, and we need a strategy to minimize it while maximizing how much data we can fit into each batch. Enter the [ knapsack problem](https://en.wikipedia.org/wiki/Knapsack_problem), a classic from computer science that’s perfect for this.

Imagine you’re packing a backpack for a hike. It can only hold so much weight, and you want to cram in as many useful items as possible. In our case:

- The **backpack**is a training batch with a maximum token limit (`max_length`).
- Each **item**is a sequence (a tokenized prompt-response pair), and its**weight**is the number of tokens.
- Our goal is to pack as many sequences as possible into the batch without going over the token limit, minimizing wasted space.

To test this idea, we start with a toy dataset: just a list of numbers from 1 to 25, each representing a sequence length. This lets us experiment without the complexity of images and text.

### 
	[
		
	](https://huggingface.co#switching-to-an-iterable-dataset)
	
		Switching to an Iterable Dataset
	

Most PyTorch datasets are *map-style* (you access them with `dataset[i]`). But for dynamic batching, we need something more flexible. So, we built an *iterable-style* dataset by subclassing `torch.utils.data.IterableDataset`. This lets us generate batches on the fly and handle tricks like sharding data across multiple workers:

```
def _get_data_range(self):
    worker_info = get_worker_info()
    if worker_info is None:  # single worker, return the entire dataset
        return self.start, self.end
    else:  # multiple workers, split the data load
        per_worker = int(
            math.ceil((self.end - self.start) / worker_info.num_workers)
        )
        worker_id = worker_info.id
        iter_start = self.start + worker_id * per_worker
        iter_end = min(iter_start + per_worker, self.end)
        return iter_start, iter_end
```
### 
	[
		
	](https://huggingface.co#producer-consumer-magic)
	
		Producer-Consumer Magic
	

Packing sequences can be slow, especially if we’re sorting or shuffling. To keep things moving, we use a **producer-consumer** pattern using [Python queues](https://docs.python.org/3/library/queue.html):

```
def _producer(self, data_iter, queue, stop_signal):
    if self.strategy == "greedy":
        for pack in self._greedy_packing(data_iter):
            queue.put(pack)
    elif self.strategy == "binpack":
        while True:
            buffer = list(itertools.islice(data_iter, self.buffer_size))
            if not buffer:
                break
            knapsacks = self._bin_packing(buffer)
            for pack in knapsacks:
                queue.put(pack)
    queue.put(stop_signal)
```
The producer thread packs batches and puts them in a queue, while the main thread pulls them out as needed. This overlap keeps the pipeline flowing smoothly.

### 
	[
		
	](https://huggingface.co#greedy-packing)
	
		Greedy Packing
	

First, we try a simple **greedy packing** strategy:

```
def _greedy_packing(self, iterator):
    pack, pack_sum = [], 0
    for item in iterator:
        if item > self.max_length:
            continue
        if pack_sum + item <= self.max_length:
            pack.append(item)
            pack_sum += item
        else:
            yield pack
            pack = [item]
            pack_sum = item
    if pack:
        yield pack
```
This walks through the data sequentially, adding items to a pack until it’s full, then starting a new one. It’s fast but not perfect. Here’s what the batches look like:

```
=== Strategy: GREEDY ===
[tensor([1]), tensor([2]), tensor([3]), tensor([4]), tensor([5]), tensor([6]), tensor([7]), tensor([8]), tensor([9]), tensor([10]), tensor([11]), tensor([12]), tensor([13])]
[tensor([14]), tensor([15]), tensor([16]), tensor([17]), tensor([18]), tensor([19])]
[tensor([20]), tensor([21]), tensor([22]), tensor([23])]
[tensor([24])]
```
![Greedy Knapsack](https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/blog/mmdp/greedy.png)


Notice how later batches get sparse? We’re leaving gaps.

### 
	[
		
	](https://huggingface.co#bin-packing-for-tighter-fits)
	
		Bin-Packing for Tighter Fits
	

Let’s try a smarter approach: **bin-packing** (specifically, First Fit Decreasing):

```
def _bin_packing(self, buffer: List[int]):
    buffer = sorted(buffer, reverse=True)
    knapsacks = []
    for item in buffer:
        for pack in knapsacks:
            if sum(pack) + item <= self.max_length:
                pack.append(item)
                break
        else:
            knapsacks.append([item])
```
This sorts sequences by length (longest first) and tries to fit each one into the first pack that has room. If none fits, it starts a new pack. The result?

```
=== Strategy: BINPACK ===
[tensor([24]), tensor([23]), tensor([22]), tensor([21]), tensor([10])]
[tensor([20]), tensor([19]), tensor([18]), tensor([17]), tensor([16]), tensor([9]), tensor([1])]
[tensor([15]), tensor([14]), tensor([13]), tensor([12]), tensor([11]), tensor([8]), tensor([7]), tensor([6]), tensor([5]), tensor([4]), tensor([3]), tensor([2])]
```
![Tight](https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/blog/mmdp/tight.png)


These batches are *much* tighter, with less wasted space. It’s like playing Tetris with your data, fitting pieces together snugly.

## 
	[
		
	](https://huggingface.co#stage-5-knapsacks-for-multimodal-data)
	
		[Stage 5] Knapsacks for Multimodal Data
	

Now for the real deal, applying knapsack packing to our *multimodal* dataset.

We’re back to images, prompts, and responses, and we need to pack them efficiently while respecting both token limits *and* image budgets. Image budgeting is done so that images per sample are balanced. We would like to avoid the case where one GPU needs to process way more images than another.

Our new [ ConstantLengthDataset](https://github.com/ariG23498/mmdp/blob/main/src/mmdp/advanced_torch_datasets.py#L13) class handles the heavy lifting. Here’s how it works, compared to Stage 4:

| Concept | Stage 4 (Toy Data) | Stage 5 (Multimodal Data) | Function(s) | 
|---|---|---|---|
| Item | Integer (sequence length) | Full sample (image, prompt, response) | `VQADataset.__getitem__` | 
| Weight | The integer itself | Number of tokens ( `len(input_ids)`) | — | 
| Knapsack | Batch of integers ≤ `max_length` | Batch of samples ≤ `seq_length`and image limit | `_balanced_greedy_knapsack` | 
| Packing Strategy | Greedy or Binpack | Greedy packing with token and image constraints | `_balanced_greedy_knapsack` | 
| Producer-Consumer | Producer fills queue | Same as the toy example, but with multimodal samples | `_producer`,`__iter__` | 
| Sample Filtering | Skip integers > `max_length` | Skip samples with too many tokens or images | `_producer` | 
| Sharding | Split integer range | Shard dataset indices | `make_base_iterator()` | 
| Batching | Group integers | Concatenate and align tokens/images | `_pack_one_group` | 
| Output | List of integers | Dict with `input_ids`,`labels`,`attention_mask`,`images` | `yield`from`__iter__` | 

The `ConstantLengthDataset` does it all:

- Reads samples (images and text).
- Filters out samples that are too long or have too many images.
- Packs samples into batches using a greedy knapsack strategy, balancing token count and image count.
- Pads the final batches to a fixed length, but with *way less*padding than before.

Here’s the result:

![Knapsack Padding](https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/blog/mmdp/05.png)


Look at that! The gray (padding) is minimal, and the batches are dense with useful data. It’s like packing a suitcase so well you can still zip it up without sitting on it.

The image might seem unintuive at the first glance, but let us look at the image side by side with constrained padding.

| Knapsack | Constrained | 
|---|---|
| ![Knapsack Padding](https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/blog/mmdp/05.png) | ![Constrained Padding](https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/blog/mmdp/03.png) | 

Here you will notice that the samples in knapsack are more evenly distributed. We also do not run into the issue of having less samples in the batch due to filtering.

## 
	[
		
	](https://huggingface.co#conclusion)
	
		Conclusion
	

What started as a simple "why is training so slow?" investigation led to a complete rethink of how we handle multimodal data.

The balanced knapsack strategy for data pipeline comes from the [Eagle 2: Building Post-Training Data Strategies from Scratch for Frontier Vision-Language Models](https://arxiv.org/abs/2501.14818) paper from NVIDIA.

**The key lessons:**

- Padding everything to the longest sequences is a good first approach (but wasteful)
- Think of batching as a packing problem
- Consider all your constraints (text length, image memory, etc.)
- Test with toy data first to validate your approach

Want to dig deeper? Check out:

*Happy training (and may your GPUs stay busy)!*
