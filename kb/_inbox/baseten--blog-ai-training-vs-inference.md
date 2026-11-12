---
title: 'AI training vs. inference: what''s the difference?'
kind: blog
topic: null
subtopic: null
secondary_topics: []
summary: null
triage: null
skip_reason: null
source: baseten
url: https://www.baseten.co/blog/ai-training-vs-inference
author: Chloe Florit
published: '2026-06-25'
fetched: '2026-11-12T06:07:48Z'
classifier: null
taxonomy_rev: 2
words: 1935
content_sha256: 8526845e32a671c41d606db34abda93f01035cac5410224c5e1c49c369acc6e0
---

# AI training vs. inference: what's the difference?

Model performance
# AI training vs. inference: what's the difference?

AI training teaches models to learn from data. Inference is what runs in production. Learn the key differences in hardware, cost, and optimization.


- Authors
- Date
- June 25, 2026

TLDR

Training is when a model learns from data until it can do tasks like write code, answer questions, or generate images. Inference is what comes after: every time a user sends a request, the trained model generates a response. The two phases have different hardware needs, optimization techniques, and costs. This post walks through the model lifecycle from pretraining to serving, the four metrics that define inference performance (TTFT, TPOT, throughput, and latency), and the key technical differences between training and inference.

AI training is how a model learns: adjusting its weights on massive datasets until it can write code, answer questions, or generate images. AI inference is what comes after: the trained model generates outputs on new data it's never seen.

Imagine hiring a scholar to explain Shakespeare to you. First, they spend years in university reading plays, discussing themes, and debating different interpretations. That's training. Once they've learned, you can ask them questions any time and get instant answers. That's inference.

Most teams will spend far more time on inference than they ever will on training: training happens a limited number of times, and inference happens every time someone uses the model. This post breaks down the difference between the two.

If you've used an AI product, you've triggered inference:

- When Kimi K3 answers a question you asked
- When you ask Cursor to write code
- When AI flags anomalies in medical conversations and records (e.g., Abridge)
- When Notion AI summarizes a meeting or drafts a document

In each situation, a trained model generates an output from a new input. No learning is happening at that moment; the model's weights are frozen. That’s inference.

*Note: If Kimi K3 is deployed behind an API, you can ask it a question by calling that API (via curl in terminal, for example).*

A model passes through multiple stages on its way to production.

This is where the model sees enormous amounts of data and learns patterns and relationships between inputs and outputs. Specifically, it runs a forward pass to generate predictions, computes loss to determine how wrong it was, then uses backpropagation to calculate how to update the weights to improve its responses. This process is repeated until the model captures broad knowledge about language, code, the world, or whatever data it's being trained on.

Post-training takes a pre-trained model and adjusts its weights so it can perform a specific task, using a specialized dataset.

Imagine Baseten wants a customer support bot to quickly and accurately answer support tickets. A powerful LLM might not know the details of the products or specific terminology. So we would fine-tune the model on past support tickets and ideal responses. The results would be a model that knows how to respond in Baseten's voice, understands product-specific terminology, and can address common customer issues.

Post-training works well in use cases where domain expertise is required. For example, Baseten Research recently partnered with [Harvey](https://www.baseten.co/research/post-training-frontier-legal-agents-with-baseten-research/) on legal AI and post-trained Qwen3.5-27B against [Harvey's Legal Agent Benchmark (LAB)](https://www.harvey.ai/blog/introducing-harveys-legal-agent-benchmark), which covers real legal tasks graded by expert-written rubrics. As a result, a 27B open-weight model became competitive with frontier closed-source models at a fraction of the cost.

Once training is done, the model gets transformed for the target hardware through quantization and compilation: model weights are converted into an optimized format for a specific GPU or accelerator. This is where raw model artifacts become something that can run fast in production.

Deployment means setting up the infrastructure: allocating GPUs, setting up an API endpoint, and configuring autoscaling so the system adds GPUs when requests spike and scales down when traffic drops. GPUs are designed to run many calculations in parallel, which makes them great for the math that powers AI models. Once the model is loaded onto that hardware, the API endpoint provides a URL that applications can call to send inputs and receive model outputs.

Serving is where live requests are handled in production, meeting speed and uptime commitments. This involves receiving incoming prompts, running them through the model, and streaming or returning the generated output. Optimizations like batching requests and caching common outputs help maximize throughput (how many requests the system can handle at once) and minimize latency (how long it takes to get a response for a single request). This is the phase users actually experience.

When you're running models in production, accuracy isn't enough. Users care about how fast the model responds, and you care about how scalable the system is: can your infrastructure handle many requests without slowing down response speed for individual users?

Four metrics tell the inference story:

**Time to first token (TTFT)** measures how quickly users see something after sending a request. High TTFT makes an app feel frozen or unresponsive. Even if the full answer arrives quickly afterward, that initial pause is what users remember.

**Time per output token (TPOT)** measures the gap between each subsequent token. This is what makes streaming feel smooth or choppy. High TPOT means text trickles out in stutters instead of flowing.

**Throughput** measures the number of tokens the system generates per second across all requests. It's a measure of system-level capacity, not individual response speed. Low throughput means the system can't scale to serve more users.

**Latency** measures the full request-to-response time for a single request. This is the top-line SLA metric: does your app meet its speed requirements?

On Baseten, latency is logged for every request. Dedicated deployments track TPOT (time per output token, or inter-token latency) and TTFT out of the box, and end-to-end latency metrics help teams see exactly how their models perform against the metrics that matter.

| Dimension | AI training | AI inference | 
|---|---|---|
| Purpose | Learn patterns from data; optimize model weights | Generate predictions or outputs from a trained model | 
| When it runs | Before deployment; periodically for retraining in case of data drift or tool calling failures | Continuously in production, triggered by user or system requests (except batch inference) | 
| Compute intensity | Extremely high; requires GPU/TPU usage for hours to weeks | Variable; can be high throughput or low latency, depending on workload | 
| Hardware profile | High-memory, high-bandwidth accelerators (e.g., A100, H100 clusters) | More flexible; can use A10, L4, or even CPU for smaller models; could also go up to the B200s for large models and max performance | 
| Latency requirement | Low priority; training jobs can run overnight or in batches | High priority; end users expect fast responses | 
| Optimization goal | Minimize loss; maximize model quality | Minimize time-to-first-token (TTFT), maximize throughput | 

**Training** runs a limited number of times over days to weeks on large GPU clusters. It's compute-intensive: it requires massive VRAM and parallel processing capacity to complete all calculations in a reasonable timeframe. This requires pairing many GPUs together: dozens for strong training performance, thousands for frontier LLMs. Costs are predictable, and jobs can be batched and run overnight.

**Inference** runs whenever there’s a user request, so compute demand scales directly with traffic. Latency matters when users are waiting for a response. Reasoning models that generate chain-of-thought produce far more tokens per request, making inference meaningfully more expensive than with base models.

**Training** demands high interconnect bandwidth between GPUs (via NVLink or InfiniBand) and large memory capacity: optimizer states alone can consume more memory than the model weights themselves. (Optimizer states are extra values tracking the history of how weights have changed, used to make smarter updates.)

**Inference** hardware is more flexible: the right choice depends on the model size, the target latency, and request volume. A small embedding model might run happily on an L4; a frontier reasoning model under tight latency requirements might need B200s.

Inference has its own toolkit of optimizations, each targeting a specific metric:

**Speculative decoding** (improves TPOT and overall latency). LLMs generate text one token at a time: each token has to wait for the previous one to finish. [Speculative decoding](https://www.baseten.co/blog/a-quick-introduction-to-speculative-decoding/) speeds this up by using a small, fast "draft" model to guess the next several tokens ahead of time, then letting the main model verify all those guesses in one parallel pass.

**Continuous batching** (improves throughput). With continuous batching, as soon as one request in a batch finishes generating a token, a new request can immediately slot in and take its place: the GPU stays full at all times.

**KV cache management** (improves TTFT). If two users send prompts that start with the same system prompt, the model only needs to compute the KV for that shared prefix once, then reuse it for both. Baseten uses [KV-cache-aware routing](https://www.baseten.co/blog/how-baseten-achieved-2x-faster-inference-with-nvidia-dynamo/) to send requests to the GPU worker that already has the relevant cache loaded, cutting time-to-first-token by \~3x.

Baseten is an inference platform where companies deploy custom models, access model APIs, and run post-training.

Baseten maximizes hardware efficiency through GPU batching, which groups multiple users' requests onto the same GPU. It also offers multi-cloud management (MCM), which automatically reroutes traffic across cloud providers in case a provider goes down.

For deployment, teams can choose between shared Model APIs (pay-per-token) or a dedicated GPU cluster for high-volume production workloads.

Baseten's model performance team applies optimization techniques like custom kernels, KV cache optimization, and speculative decoding to squeeze more tokens per second out of every GPU. Beyond open-source model serving, Baseten supports custom models of every modality and size: custom LLMs, real-time voice AI, high-throughput embeddings for search and RAG pipelines, transcription, image and video generation, agentic workflows, and more.

Deployment, autoscaling, load balancing, and monitoring are all part of the Baseten inference platform, so engineering teams don't have to build or maintain the infrastructure themselves.

During training specifically, Baseten saves multiple versions of the model (checkpoints). Checkpoints are snapshots of the model's weights saved at specific points during the training process. Training a large model takes days or weeks. If training crashes or the hardware fails, you don't want to start from scratch. Checkpoints let you resume from the last saved state rather than the beginning. They also help compare model quality across different training stages. Once you pick the best checkpoint, you can deploy it to Baseten as a production inference API endpoint.

**Can the same hardware be used for both training and inference?**

Yes. High-end accelerators like the H100 can handle both, but inference workloads often run more cost-efficiently on less expensive hardware.

**What is the difference between online and batch inference?**

Online inference (also called real-time inference) serves individual requests with low latency, typically in the range of milliseconds. Batch inference processes large volumes of inputs together, prioritizing throughput over speed. Higher throughput means more requests (or tokens) per GPU-hour. So if throughput goes up, requests per GPU-hour go up, and cost per request goes down. The choice of online and batch inference depends on whether results are needed immediately or can be computed ahead of time.

**Why does inference become more expensive than training at scale?**

Training is a one-time or periodic cost. Inference costs accumulate with every request, every user, and every production query over the model's operational lifetime. For a widely deployed model receiving millions of requests per day, the daily inference bill quickly outpaces even a substantial training run. At Baseten, inference is pay-per-use, with no up-front commitments. You just pay for the GPU minutes you consume.
