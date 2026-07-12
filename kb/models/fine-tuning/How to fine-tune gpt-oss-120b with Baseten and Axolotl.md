---
title: How to fine-tune gpt-oss-120b with Baseten and Axolotl
topic: models
subtopic: fine-tuning
secondary_topics:
- infra-platform/gpu-clusters
summary: Guide to fine-tuning GPT-OSS 120B with Axolotl and scalable training infrastructure.
source: baseten
url: https://www.baseten.co/blog/how-to-fine-tune-gpt-oss-120b-with-baseten-and-axolotl/
author: Sanskriti Sharma; Nidhi Hiremath; Wing Lian
published: '2025-08-19'
fetched: '2026-07-11T04:07:30Z'
classifier: codex
taxonomy_rev: 1
words: 1055
content_sha256: 76b35301c0603a48e3789c8aac32ab29e5039602e7d2a0c698c375cf6b5e8d81
triage: keep
skip_reason: null
---

# How to fine-tune gpt-oss-120b with Baseten and Axolotl

![How to fine-tune gpt-oss-12b with Baseten and Axolotl](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1755560212-logo-template-7.png%3Fauto%3Dformat%26fit%3Dcrop%26h%3D630%26w%3D1200&w=3840&q=100)

OpenAI released two new open-weight models, gpt-oss-120b and gpt-oss-20b, their first since GPT-2 in 2019. While gpt‑oss‑120b rivals OpenAI’s proprietary o4-mini on reasoning benchmarks, gpt‑oss‑20b performs on par with o3-mini. Both of these models are a promising basis for fine-tuning to customize them for specific use cases.

Fine-tuning a large model like gpt‑oss‑120B is complex due to the compute and model parallelism requirements to load the model and train efficiently, along with dataset caching, checkpointing, and fault tolerance to handle long runtimes and large datasets. To make it easier, Baseten and Axolotl have partnered to create a new recipe for fine-tuning gpt-oss-120B.

Axolotl is an open-source fine-tuning runtime that supports LoRA, QLoRA, RLHF, full fine-tuning, and more for any open-source model. It’s YAML-first, multi-GPU/multi-node ready, and optimized for distributed parallel training with DeepSpeed, FSDP, and sequence parallelism for fast, scalable training.

At Baseten, our Training platform removes the complexity from large-scale model training with access to top-shelf GPUs without reservations, seamless scaling from a single GPU to multiple nodes, and dataset caching. You can train long-running jobs with built-in checkpointing, and once you’re ready for production, deploy to Baseten’s high-performance [inference platform](https://www.baseten.co/products/dedicated-deployments/) with a single command.

You can find the full recipe [here](https://github.com/basetenlabs/ml-cookbook/tree/main/examples/oss-gpt-120b-axolotl/training), but we'll break it down in more detail below.

## Prerequisites for fine-tuning with Baseten and Axolotl

- **High-quality data:**The results of your fine-tuning are only as good as the dataset you train on. Your data, whether real or synthetic, should be clean and well-labeled.
- **Representative evaluation:**You should have an evaluation environment representative of your production environment to measure the success of your fine-tune. This helps you set a realistic baseline and understand where other SOTA/pre-trained models fall short.
- **Baseten account and API key:**You’ll need an active Baseten account with Training enabled. You can request access to Training (which is currently in beta)- [here](https://www.baseten.co/talk-to-us/request-access/).- [Obtain an API key](https://app.baseten.co/settings/api_keys)for the account to authenticate with the Baseten API and SDK.
- **Truss and CLI:**The open-source- [Truss package](https://github.com/basetenlabs/truss)provides a Python-native way for defining and running your training jobs, including via the CLI. Install or update it using pip:- `pip install -U truss`.
- **Dependencies:**In this demo, we’ll use Hugging Face to access and upload models. It’s recommended that you create a Hugging Face access token and add it to your- [Baseten Secrets](https://docs.baseten.co/observability/secrets#best-practices-for-secrets). Additionally, it can be helpful to visualize your training run. In this example, we use- [Weights & Biases](https://wandb.ai/site/)(- `wandb`) to do so (this is optional).

Note: If you are pre-PMF and trying to validate a market hypothesis, we recommend trying our pre-optimized [Model APIs](https://www.baseten.co/products/model-apis/) to iterate rapidly and find what sticks before investing in fine-tuning your own models.

## Fine-tuning gpt-oss-120B with Axolotl and Baseten

### Step 1: Define your Baseten Training configuration

You bring your own code to Baseten: all you need to do is define your training job through a Python configuration file (`config.py`). This is where the starting commands, environment variables, and more for your deployment are defined (example below).

```
1training_runtime = definitions.Runtime(
2    start_commands=[ # Example: list of commands to run your training script
3        "/bin/sh -c 'chmod +x ./run.sh && ./run.sh'"
4    ],
5    environment_variables={
6        # Secrets (ensure these are configured in your Baseten workspace)
7        "HF_TOKEN": definitions.SecretReference(name="hf_access_token"),
8        "WANDB_API_KEY" : definitions.SecretReference(name="wandb_api_key"),
9    },
10    cache_config=definitions.CacheConfig(
11        enabled=True,
12    ),
13    checkpointing_config=definitions.CheckpointingConfig(
14        enabled=True,
15    ),
16)
```
For large training jobs, a persistent cache can retain data between jobs and improve iteration speed by avoiding expensive and time-consuming egress of your dataset. Turning on the [Training Cache](https://docs.baseten.co/training/concepts#iterate-faster-with-the-training-cache) is as simple as setting `enabled = True`.

Reliable, automatic checkpointing of your training progress can be useful to resume your job at any point. Turning on [checkpointing](https://docs.baseten.co/training/concepts#taking-advantage-of-automated-checkpointing) with Baseten is similar to cache: just set `enabled = True`.

For the 120B model, running the job on multiple nodes can help speed up the training run so you can iterate quickly. At Baseten, we abstract away all the complexity of [multi-node training](https://docs.baseten.co/training/concepts#multinode-training) so that you can just specify the `node_count = n`. In the example below, we use two nodes of H100 GPUs. 

```
training_compute = definitions.Compute(
    node_count=2,
    accelerator=truss_config.AcceleratorSpec(
        accelerator=truss_config.Accelerator.H100,
        count=8,
    ),
)
```
You can find more documentation on setting your Training configuration [here](https://docs.baseten.co/training/getting-started#step-1%3A-define-your-training-configuration).

### Step 2: Define your Axolotl training configuration

Axolotl’s YAML-first design makes one file the single source of truth for the entire training run, removing the need for multiple scripts and making it easy to share, reproduce, and iterate on model training.

Configure the Axolotl YAML file to reflect your dataset and hyperparameters. We first select the base model on Axolotl.

`base_model: axolotl-ai-co/gpt-oss-120b-dequantized`Axolotl provides a dequantized version of the model to properly load the weights when using CPU RAM-efficient loading with FSDP. Using the original weights may result in incorrect training loss values.

Then, we define the dataset to train on. The `type` field defines how the dataset will be processed according to pre-existing templates. 

```
datasets:
  - path: HuggingFaceH4/Multilingual-Thinking
    type: chat_template
    field_thinking: thinking
    template_thinking_key: thinking
```
This YAML is where you also define other important parameters of model training, such as custom flash attention definitions, gradient checkpointing, and activation offloading to reduce GPU memory usage.

```
flash_attention: true
attn_implementation: kernels-community/vllm-flash-attn3
gradient_checkpointing: true
activation_offloading: true
```
You can find more documentation on the Axolotl configuration [here](https://docs.axolotl.ai/docs/config-reference.html).

Finally, make sure your Baseten `start_commands` include the Axolotl run command: `axolotl train config.yaml.` This ensures your training job on Baseten executes Axolotl end-to-end, using the exact parameters you’ve defined in YAML.

### Step 3: Launch the training job

Launch the run with `truss train push config.py`.

Upon successful submission, the CLI will print out a training job ID with some helpful commands to view logs and metrics for your jobs -- Baseten provides this observability out of the box. You can also navigate to the Baseten [Web UI](https://app.baseten.co/training/) to view this information.

When you are ready to move to production, you can use `truss train deploy_checkpoints` to deploy your model as a Dedicated Deployment with production-ready infrastructure and autoscaling.

**What’s next?**

If you are looking for a tool to streamline model post-training, you can check out Axolotl’s framework [here](https://github.com/axolotl-ai-cloud/axolotl). If you want to focus on your models and not worry about the underlying infrastructure, you can set up time to talk with Baseten’s engineering team [here](https://www.baseten.co/talk-to-us/).
