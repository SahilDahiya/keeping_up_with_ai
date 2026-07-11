---
title: 'Comparing NVIDIA GPUs for AI: T4 vs A10'
topic: inference
subtopic: hardware
secondary_topics:
- infra-platform/cost
summary: Compares NVIDIA T4 and A10 GPUs for AI inference workloads and cost-performance
  tradeoffs.
source: baseten
url: https://www.baseten.co/blog/comparing-nvidia-gpus-for-ai-t4-vs-a10/
author: Philip Kiely
published: '2023-04-27'
fetched: '2026-07-11T04:11:06Z'
classifier: codex
taxonomy_rev: 1
words: 1673
content_sha256: 3d3039763bd9214483952019ec61123f6ca87207b1ba8eae0c620ded5eab79aa
triage: keep
skip_reason: null
---

# Comparing NVIDIA GPUs for AI: T4 vs A10

![T4 vs A10](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1747614187-t4-a10.png%3Fauto%3Dformat%26fit%3Dcrop%26h%3D630%26w%3D1200&w=3840&q=100)

Choosing the right GPU for deploying and serving ML models is essential. You want to choose a GPU that’s powerful enough to run your model stably without overpaying for unnecessary headroom. With this article, you’ll be able to choose between NVIDIA’s T4 and A10 GPUs to determine the right fit for your needs and budget.

Generative AI workloads like fine-tuning foundation models, deploying large open-source models, and serving LLMs require powerful GPUs. But picking the GPU that matches your workload is difficult with the numerous options available. It’s hard to make an apples-to-apples comparison between cards with different architectures, core types, and memory capacity.

This post outlines the key specs to understand when comparing GPUs as well as factors to consider like price, availability, and opportunities for horizontal scaling. Then, we apply these ideas to choose between two popular GPUs—the NVIDIA T4 and A10—for realistic generative AI workloads.

## Reading GPU Specs

Comparing GPUs in abstract is difficult, especially across generations. But there are two specs you should know about: cores and VRAM.

### Cores

Compute cores are where the magic math happens that makes GPUs work. But not all cores are the same. Certain cores are optimized for certain tasks.

Here are a few types of cores on modern NVIDIA graphics cards:

- **CUDA cores**: the most general-purpose cores for a wide variety of computing tasks.
- **Tensor cores:**optimized for certain machine learning calculations
- **Ray-tracing (RT) cores:**more important for gaming than most ML, these cores specialize in simulating the behavior of light- **.**

### VRAM

[VRAM](https://en.wikipedia.org/wiki/Video_random-access_memory) (Video Random Access Memory) is the amount of memory on a graphics card. VRAM is memory for GPUs just like RAM is memory for CPUs.

VRAM is more or less a hard limit on model size. If you try to load a model that doesn’t fit into GPU memory — or one that barely fits but doesn’t leave enough memory left over for input and output overhead — you’ll get an out-of-memory error and your invocation will fail.

## Choosing the right GPU for your workload

It would be great if every job could just run on the most powerful GPUs ever invented. But there are a number of real-world constraints to consider when selecting a GPU for your workload.

### Price to performance

The first constraint, of course, is price. If a smaller, less expensive GPU is capable of serving your model with acceptable performance metrics, then you should absolutely choose it. Finding the least expensive hardware that can reliably run your code is one exciting challenge of infrastructure work.

Total cost of operation for a GPU is about more than just cost per minute. If a particular GPU can run a job faster, it might save you money even if it costs more per minute, as total cost is the price per minute multiplied by the amount of time your task runs for.

In a simplified example, if GPU A costs one cent per minute and takes ten minutes for a certain task while GPU B costs two cents per minute but can complete the same task in four minutes, then running the task on GPU B actually costs less money in total (and gets you results faster).

![At 2 cents per minute, GPU B is cheaper overall for the workload](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1692712191-644a9b6e2e98130811d30462_8d39a730.png%3Fauto%3Dformat%26w%3D1200&w=3840&q=75) At 2 cents per minute, GPU B is cheaper overall for the workload

At 2 cents per minute, GPU B is cheaper overall for the workload### Vertical vs horizontal scaling

Vertical scaling means increasing the size and power of the single instance you’re using. This approach has its limits. Even top-of-the-line GPUs are only so powerful. Large foundation models like GPT were not trained on a single GPU. Instead, many GPUs were used in parallel to train the model — horizontal scaling.

Horizontal scaling, which splits work across multiple replicas of an instance, might make sense for your workload even if you’re not training the next foundation model. For example, when you fine-tune Stable Diffusion on Baseten, that runs on 4 A10 GPUs simultaneously.

And if you’re serving a model in a high-traffic environment, that’s another case for horizontal scaling. While a larger, more powerful GPU may have a higher throughput, you can usually exceed that throughput at the same price by using multiple replicas of the lowest-cost GPU that can run your model.

Consider options for scaling your infrastructure both vertically and horizontally when selecting GPUs. Baseten provides autoscaling so that your model can scale horizontally, adding and removing replicas automatically in response to traffic.

### Availability

There’s a common saying in the sports world: “the best ability is availability.” With the massive popularity of generative AI, cloud providers like AWS and Google Cloud are currently having trouble [keeping up with demand for GPU compute](https://www.theinformation.com/articles/ai-developers-stymied-by-server-shortage-at-aws-microsoft-google). That means it can take time for GPUs to become available to use, especially scarcer high-powered GPUs.

Baseten addresses this availability issue by overprovisioning the GPUs that our customers use to serve models. This way, we have a reserve ready to go for when you need to deploy or scale up a model.

## Choosing a GPU

We’ll frame our discussion around two widely available GPUs: NVIDIA’s T4 and A10 GPUs.

The T4 is less expensive, so if your workload runs reliably and performantly on the T4, you should use a T4 instance. If not, upgrade to an A10 instance for faster invocations and larger models.

Let’s take a closer look at both GPUs with an example use case for each card.

![The NVIDIA T4](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1692712218-644a9b6ef108b3a7e3eff109_a778515f.png%3Fauto%3Dformat%26w%3D1200&w=3840&q=75) The NVIDIA T4

The NVIDIA T4## NVIDIA T4 overview

The NVIDIA Tesla T4 is a midrange datacenter GPU. It was released in 2019 and uses NVIDIA’s Turing architecture. It is well suited for a range of generative AI tasks.

### NVIDIA T4 Specs

The T4 has the following key specs:

- **CUDA cores**: 2560
- **Tensor cores**: 320
- **VRAM**: 16 GiB

The [T4 specs page](https://www.nvidia.com/en-us/data-center/tesla-t4/) gives more specs. For our purposes, it’s important to understand that the T4 has 16GiB of VRAM and a large number of tensor cores.

### NVIDIA T4 Price

Datacenter GPUs aren’t really designed to be purchased by consumers. At the time of writing, [Dell will sell you a T4 for $3,500](https://www.dell.com/en-us/shop/nvidia-tesla-t4-16gb-passive-single-slot-low-profile-gpu-customer-install/apd/490-bflb/graphic-video-cards) and it’s available for less on various online retailers. But most of us aren’t wiring up our own server racks to deploy models, so a hosted solution makes more sense.

On Baseten, [instances with a T4 start at 1.753 cents per minute](https://www.baseten.co/pricing). It is the least expensive graphics card option available on Baseten.

### Example use case: Whisper

Let’s contextualize these raw numbers with an example use case for the T4.

The NVIDIA T4 is a great GPU for running Whisper, the open-source audio transcription model by OpenAI. The largest version of the model fits comfortably in 16GiB of VRAM and the card achieves respectable performance, transcribing a 30-minute audio clip in less than 4 minutes during testing. Baseten uses the T4 by default for serving Whisper.

If you’re running a medium-sized model with a model weights file small enough to fit into 16 GiB of VRAM, the T4 is the capable, affordable GPU for your workflow.

![The NVIDIA A10](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1692712262-644a9b6e112d7ee967a0deaa_0bf946ac.png%3Fauto%3Dformat%26w%3D1200&w=3840&q=75) The NVIDIA A10

The NVIDIA A10## NVIDIA A10 overview

The A10 is a bigger, more powerful GPU than the T4. It has more CUDA cores, more tensor cores, and more VRAM. It was released in 2021 and uses NVIDIA’s Ampere architecture.

You can run just about anything on an A10 that you can run on a T4, and it will likely be faster. Here’s a benchmark of Whisper invocations on a T4 versus an A10:

Each invocation was run on a warm GPU. Values shown are an average of five runs.

But using an A10 costs about 1.9x as much per minute as a T4 for a 1.2x-1.4x speedup in this example. Unless invocation time is critical for your use case, the A10’s role is not just being a faster T4. Its role is running workloads that the T4 can’t handle at all.

A quick note on the A10: sometimes you’ll instead see the A10G. The [A10 and A10G are similar cards](https://www.baseten.co/blog/nvidia-a10-vs-a10g-for-ml-model-inference/), with the A10G being a variant specific to AWS for its G5 instance types.

### NVIDIA A10 Specs

The A10 has the following key specs:

- **CUDA cores**: 9216
- **Tensor cores**: 288
- **VRAM**: 24 GiB

The [A10’s spec page](https://www.nvidia.com/en-us/data-center/products/a10-gpu/) has the rest of the details. Along with the extra CUDA cores and VRAM, the A10 also adds 72 ray tracing cores and nearly doubles the memory bandwidth of the T4. What matters most for serving models though is the increase in core count and VRAM.

### NVIDIA A10 Price

Again, buying a datacenter GPU up front is uncommon. But if you’re curious, [Dell lists the card for $5,700](https://www.dell.com/en-us/shop/nvidia-ampere-a10-pcie-150w-24gb-passive-single-wide-full-height-gpu/apd/490-bgkh/parts-upgrades) at the time of writing.

For a hosted solution, [instances with an A10 GPU start at 3.353 cents per minute](https://www.baseten.co/pricing) on Baseten.

### Example use case: Stable Diffusion XL

So if we’re not just using an A10 to outrace the T4, what are we using it for?

Running inference on [Stable Diffusion XL](https://www.baseten.co/library/stable-diffusion-xl/) requires both the additional processing power and the 24 GiB of memory offered by the A10. 

A10s are also useful for running LLMs. Popular seven-billion-parameter models like [Mistral 7B](https://www.baseten.co/library/mistral-7b-instruct/) and Llama 2 7B run on an A10, and you can spin up an instance with multiple A10s to fit larger models like [Llama 2 70B](https://github.com/basetenlabs/truss-examples).

## Which GPU is right for you?

Here’s a side-by-side comparison of the specs and price for the T4 and the A10.

If your model fits on a T4 and you’re satisfied with the performance, you should absolutely use a T4 to run your workload cost-effectively. And for jobs with high compute or memory requirements, there’s the A10.

Use Baseten’s [pricing calculator](https://www.baseten.co/pricing) to predict the cost of serving your model and please [contact us](mailto:support@baseten.co) to learn about volume discounts or discuss specialized hardware needs for fine-tuning, deploying, and serving ML models.
