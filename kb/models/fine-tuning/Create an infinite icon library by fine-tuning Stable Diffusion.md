---
title: Create an infinite icon library by fine-tuning Stable Diffusion
topic: models
subtopic: fine-tuning
secondary_topics: []
summary: Practical example of fine-tuning Stable Diffusion for a custom image-generation
  domain using Modal infrastructure.
source: modal
url: https://modal.com/blog/fine-tuning-stable-diffusion
author: null
published: '2024-05-21'
fetched: '2026-07-11T04:30:21Z'
classifier: codex
taxonomy_rev: 1
words: 2600
content_sha256: d526ddb3c1a54ba115d47b334e0a80b93ae4bb16e1a213f8b0928de9a835d250
triage: keep
skip_reason: null
---

# Create an infinite icon library by fine-tuning Stable Diffusion

[Back](https://modal.com/blog)

# Create an infinite icon library by fine-tuning Stable Diffusion

[Yiren Lu](https://twitter.com/YirenLu)

[Charles Frye](https://twitter.com/charles_irl)

*For part 2 of this blog post, on how we fine-tuned Flux.1-dev with the same dataset, see  here.*

Icon libraries provide a clean, consistent look for web interfaces.
Here at Modal, we mostly use [Lucide](https://lucide.dev/).
We also like [Heroicons](https://heroicons.com/), a set of freely-available icons
from the makers of [Tailwind CSS](https://tailwindcss.com),
another open source library we use.

![Some example original Heroicons](https://modal-cdn.com/cdnbot/fine-tuning-stable-diffusion-original-heroicons.png)



`calendar-days`, `film`, and `users`.These icon libraries are incredibly useful.
But like libraries of books, icon libraries are limited.
If our app needs an icon for `golden-retriever`s or `barack-obama`,
we’re just out of luck.

But what if icon libraries were more like Borges’ [ Biblioteca de Babel](https://en.wikipedia.org/wiki/The_Library_of_Babel):
an endless collection of everything we could possibly need?

Generative models like [Stable Diffusion](https://huggingface.co/models?pipeline_tag=stable-diffusion) hold this exact promise: once they have seen enough examples of some kind of data,
they learn to simulate the process by which that data is generated,
and can then generate more, endlessly.

So as an experiment, we took a Stable Diffusion model and fine-tuned it on the Heroicons library.

Here’s an example icon it generated for `barack-obama`:

![An icon of Barack Obama's head](https://modal-cdn.com/cdnbot/fine-tuning-stable-diffusion-barack-obama.png)



You can play around with the fine-tuned model yourself [here](https://modal-labs--heroicons.modal.run/).

We were able to create a number of delightful new black-and-white line icons, all in a rough imitation of the Heroicons style:

![Some example custom Heroicons](https://modal-cdn.com/cdnbot/fine-tuning-stable-diffusion-generated-heroicons.png)



`apple-computer`, `bmw`, `castle`.Middle row:

`ebike`, `future-of-ai`, `golden-retriever`.Bottom row:

`jail`, `piano`, `snowflake`The entire application, from downloading a pretrained model through fine-tuning and up to serving an interactive web UI, is run on Modal.

Modal is a scalable, serverless cloud computing platform that abstracts away the complexities of infrastructure management.

With Modal, we can easily spin up powerful GPU instances, run the fine-tuning training script, and deploy the fine-tuned model as an interactive web app, all with just a few lines of code.

In this blog post, we’ll show you how.

## Table of contents

- [Choosing a fine-tuning technique](https://modal.com#choosing-a-fine-tuning-technique)
- [Setting up accounts](https://modal.com#setting-up-accounts)
- [Preparing the dataset](https://modal.com#preparing-the-dataset)
- [Training on Modal](https://modal.com#training-on-modal)
- [Serving the fine-tuned model](https://modal.com#serving-the-fine-tuned-model)
- [Wrapping inference in a Gradio UI](https://modal.com#wrapping-inference-in-a-gradio-ui)
- [Parting thoughts](https://modal.com#parting-thoughts)

## Choosing a fine-tuning technique

Your first choice when fine-tuning a model is how you’re going to do it.

In **full fine-tuning**, the entire model is updated during training.
This is the most computationally expensive method. It is particularly costly
in terms of memory, because information that can be several times the size of the model
needs to be kept in memory.

In **sequential adapter fine-tuning**, new layers are appended to the model and trained.
This requires much less memory than full fine-tuning, because the number of new layers
is usually small — even just one.
However, it is unable to adjust the earliest layers of the model,
where critical aspects of the representation are formed,
and it increases the time required for inference.

In **parallel adapter fine-tuning**, new layers are inserted
“alongside” the existing layers of the model,
and their outputs superimposed on the outputs of the existing layers.
This approach takes excellent advantage of the parallel processing capabilities of GPUs
and the natural parallelism of linear algebra,
and it has become especially popular in the last few years,
in the form of techniques like LoRA (Low Rank Adaptation).

HuggingFace has pretty comprehensive documentation on all these techniques [here](https://huggingface.co/docs/diffusers/main/en/training/overview).

For our use-case, we found that full fine-tuning worked best. But parallel adapter fine-tuning methods, like LoRA, can also work well, especially if you have a small dataset and want to fine-tune quickly.

## Setting up accounts

If you’re following along or using this blog post as a template for your own fine-tuning experiments, make sure you have the following set up before continuing:

- A HuggingFace account (sign up [here](https://huggingface.co/join)if you don’t have one).
- A Modal account (sign up [here](https://modal.com/signup)if you don’t have one).

## Preparing the Dataset

The first step in fine-tuning Stable Diffusion for style is to prepare the dataset.

Most blog posts skip over this part, or give only a cursory overview. This gives the false impression that dataset preparation is trivial and that models, optimization algorithms, and infrastructure are the most important.

We found that handling the data was actually the most important and most difficult part of fine-tuning — and just about all machine learning practitioners will tell you the same.

To use the Heroicons dataset, which consists of around 300 SVG icons, for fine-tuning, we need to:

- Download the Heroicons from the - [GitHub repo](https://github.com/tailwindlabs/heroicons)
- Convert the SVGs to PNGs and add white backgrounds to the images - Image models are trained on rasterized graphics, so we need to convert the icons.
- Add white backgrounds to the PNGs - We also need to add white backgrounds to the PNGs. This may seem trivial, but it is critically important - many models are incapable of outputting with transparency.
- Generate captions for each image and create a - `metadata.csv`file- Since the Heroicon filenames match the concept they represent, we can parse them into captions. We also add a prefix to each caption: - `“an icon of a <object>.”`- We then create a - `metadata.csv`file, where each row is an image file name with the associated caption. The- `metadata.csv`file should be placed in the same directory as all the training images and contain a header row with the string- `file_name,text`- `# tree heroicons_training_dir heroicons_training_dir/ ├── arrow.png ├── bike.png ├── cruiseShip.png └── metadata.csv`- `# metadata.csv file_name,text arrow.png,"an icon of a arrow" bike.png,"an icon of a bike" cruiseShip.png,"an icon of a cruise ship"`
- Upload the dataset to the HuggingFace Hub - `import os from datasets import load_dataset import huggingface_hub # login to huggingface hf_key = os.environ["HUGGINGFACE_TOKEN"] huggingface_hub.login(hf_key) dataset = load_dataset("imagefolder", data_dir="/lg_white_bg_heroicon_png_img", split="train") dataset.push_to_hub("yirenlu/heroicons", private=True)`

You can see the post-processed dataset [here](https://huggingface.co/datasets/yirenlu/heroicons).

## Training on Modal

### Setting up Diffusers dependencies on Modal

To fine-tune Stable Diffusion for style, we used the [Diffusers library](https://github.com/huggingface/diffusers) by HuggingFace.
Diffusers provides a set of easy-to-use scripts for fine-tuning these models on custom datasets.

You can see an up-to-date list of all their scripts in their [ examples subdirectory](https://github.com/huggingface/diffusers/tree/main/examples).

For this fine-tuning task, we will be using the [ train_text_to_image.py](https://github.com/huggingface/diffusers/blob/abd922bd0c43a504e47eca2ed354c3634bd00834/examples/text_to_image/train_text_to_image.py) script. This script does full fine-tuning.

When you run your code on Modal, it executes in [a containerized environment](https://modal.com/docs/guide/images) in the cloud, not on your machine.
This means that you need to set up any dependencies in that environment.

Modal provides a Pythonic API to define containerized environments — the same power and flexibility as a Dockerfile, but without all the tears.

```
# fine-tune-stable-diffusion.py
import os
import sys
from dataclasses import dataclass
from pathlib import Path
from fastapi import FastAPI
from modal import Image, App, Volume, gpu, Secret
GIT_SHA = "abd922bd0c43a504e47eca2ed354c3634bd00834"  # specify the commit to fetch
image = (
    Image.debian_slim(python_version="3.10")
    .pip_install(
        "accelerate==0.27.2",
        "datasets~=2.19.1",
        "ftfy~=6.1.1",
        "gradio~=3.50.2",
        "smart_open~=6.4.0",
        "transformers~=4.38.1",
        "torch~=2.2.0",
        "torchvision~=0.16",
        "triton~=2.2.0",
        "peft==0.7.0",
        "wandb==0.16.3",
    )
    .apt_install("git")
    # Perform a shallow fetch of just the target `diffusers` commit, checking out
    # the commit in the container's current working directory, /root.
    .run_commands(
        "cd /root && git init .",
        "cd /root && git remote add origin https://github.com/huggingface/diffusers",
        f"cd /root && git fetch --depth=1 origin {GIT_SHA} && git checkout {GIT_SHA}",
        "cd /root && pip install -e .",
    )
)
```
### Setting up `Volume` for cloud storage of weights

 Modal provides network file systems, [Volumes](https://modal.com/docs/guide/volumes),
for writing information persistently from those cloud containers.

We use one to store the weights after we’re done training. We then read the weights from it when it’s time to run inference and generate new icons.

```
# fine-tune-stable-diffusion.py
web_app = FastAPI()
app = App(name="example-diffusers-app")
MODEL_DIR = Path("/model")
model_volume = Volume.from_name("diffusers-model-volume", create_if_missing=True)
VOLUME_CONFIG = {
    "/model": model_volume,
}
```
### Setting up hyperparameter configs

We fine-tuned off the StableDiffusion v1.5 model, but you can easily also fine-tune off of other Stable Diffusion
versions by changing the config below. We used `4000` training steps, a learning rate of `1e-5`, and a batch size of `1`.

We set up one `dataclass`, `TrainConfig`, to hold all the training hyperparameters,
and another, `AppConfig`, to store all the inference hyperparameters.

```
# fine-tune-stable-diffusion.py
@dataclass
class TrainConfig:
    """Configuration for the finetuning training."""
    # identifier for pretrained model on Hugging Face
    model_name: str = "runwayml/stable-diffusion-v1-5"
    resume_from_checkpoint: str = "latest"
    # HuggingFace Hub dataset
    dataset_name = "yirenlu/heroicons"
    # Hyperparameters/constants from some of the Diffusers examples
    # You should modify these to match the hyperparameters of the script we are using.
    mixed_precision: str = "fp16"  # set the precision of floats during training, fp16 or less needs to be mixed with fp32 under the hood
    resolution: int = 128
    max_train_steps: int = (
        4000  # number of times to apply a gradient update during training
    )
    checkpointing_steps: int = (
        1000  # number of steps between model checkpoints, for resuming training
    )
    train_batch_size: int = (
        1  # how many images to process at once, limited by GPU VRAM
    )
    gradient_accumulation_steps: int = 1  # how many batches to process before updating the model, stabilizes training with large batch sizes
    learning_rate: float = 1e-05  # scaling factor on gradient updates, make this proportional to the batch size * accumulation steps
    lr_scheduler: str = (
        "constant"  # dynamic schedule for changes to the base learning_rate
    )
    max_grad_norm: int = 1  # value above which to clip gradients, stabilizes training
    caption_column: str = "text"  # name of the column in the dataset that contains the captions of the images
    validation_prompt: str = "an icon of a dragon creature"
@dataclass
class AppConfig:
    """Configuration information for inference."""
    num_inference_steps: int = 50 # How many steps to run the model for inference, the more the higher quality generally
    guidance_scale: float = 20 # How much the image should adhere to the text prompt
```
### Running fine-tuning

Now, finally, we’re ready to fine-tune.

We first need to decorate the `train` function with `@app.function`,
which tells Modal that the function should be launched in a cloud container on Modal.

Functions on Modal combine code and the infrastructure required to run it.
So the `@app.function` decorator takes several arguments that lets us specify
the type of GPU we want to use for training,
the Modal Volumes we want to mount to the container,
and any secret values (like the HuggingFace API key) that we want to pass to the container.

This training function does a bunch of preparatory things,
but the core of it is the `notebook_launcher` call that launches the actual Diffusers training script as a subprocess.
In particular, we are launching the script using the [Accelerate](https://huggingface.co/docs/accelerate/en/index) CLI command.
Accelerate is a Python library that makes it easy to leverage multiple GPUs for accelerated model training.

The training script saves checkpoint files every 1000 steps.
To make sure that those checkpoints are persisted,
we need to set `_allow_background_volume_commits=True` in the `@app.function` decorator.

```
# fine-tune-stable-diffusion.py
@app.function(
    image=image,
    gpu=gpu.A100(
        size="80GB"
    ),  # finetuning is VRAM hungry, so this should be an A100 or H100
    volumes=VOLUME_CONFIG,
    timeout=3600 * 2,  # multiple hours
    secrets=[Secret.from_name("huggingface-secret")],
    _allow_background_volume_commits=True
)
def train():
    import huggingface_hub
    from accelerate import notebook_launcher
    from accelerate.utils import write_basic_config
    # change this line to import the training script we want to use
    from examples.text_to_image.train_text_to_image import main
    from transformers import CLIPTokenizer
    # set up TrainConfig
    config = TrainConfig()
    # set up runner-local image and shared model weight directories
    os.makedirs(MODEL_DIR, exist_ok=True)
    # set up hugging face accelerate library for fast training
    write_basic_config(mixed_precision="fp16")
    # authenticate to hugging face so we can download the model weights
    hf_key = os.environ["HF_TOKEN"]
    huggingface_hub.login(hf_key)
    # check whether we can access the model repo
    try:
        CLIPTokenizer.from_pretrained(config.model_name, subfolder="tokenizer")
    except OSError as e:  # handle error raised when license is not accepted
        license_error_msg = f"Unable to load tokenizer. Access to this model requires acceptance of the license on Hugging Face here: https://huggingface.co/{config.model_name}."
        raise Exception(license_error_msg) from e
    def launch_training():
        sys.argv = [
            "examples/text_to_image/train_text_to_image.py",  # potentially modify
            f"--pretrained_model_name_or_path={config.model_name}",
            f"--dataset_name={config.dataset_name}",
            "--use_ema",
            f"--output_dir={MODEL_DIR}",
            f"--resolution={config.resolution}",
            "--center_crop",
            "--random_flip",
            f"--gradient_accumulation_steps={config.gradient_accumulation_steps}",
            "--gradient_checkpointing",
            f"--train_batch_size={config.train_batch_size}",
            f"--learning_rate={config.learning_rate}",
            f"--lr_scheduler={config.lr_scheduler}",
            f"--max_train_steps={config.max_train_steps}",
            f"--lr_warmup_steps={config.lr_warmup_steps}",
            f"--checkpointing_steps={config.checkpointing_steps}",
        ]
        main()
    # run training -- see huggingface accelerate docs for details
    print("launching fine-tuning training script")
    notebook_launcher(launch_training, num_processes=1)
@app.local_entrypoint()
def run():
    train.remote()
```
With that all in place, we can kick off a training run on Modal from anywhere with a simple command:

`modal run fine-tune-stable-diffusion.py`## Serving the fine-tuned model

Once `fine-tune-stable-diffusion.py` has finished its training run, the fine-tuned model will be saved in the Volume.
We can then mount the volume to a new Modal `inference` function,
which we can then invoke from any Python code running anywhere.

```
# fine-tune-stable-diffusion.py
@app.cls(
    image=image,
    gpu="A10G", # inference requires less VRAM than training, so we can use a cheaper GPU
    volumes=VOLUME_CONFIG, # mount the location where your model weights were saved to
)
class Model:
    @enter()
    def load_model(self):
        import torch
        from diffusers import StableDiffusionPipeline
        # Reload the modal.Volume to ensure the latest state is accessible.
        app.model_volume.reload()
        # set up a hugging face inference pipeline using our model
        # potentially use different pipeline
        pipe = StableDiffusionPipeline.from_pretrained(
            MODEL_DIR,
            torch_dtype=torch.float16,
        ).to("cuda")
        pipe.enable_xformers_memory_efficient_attention()
        self.pipe = pipe
    @method()
    def inference(self, text, config):
        image = self.pipe(
            text,
            num_inference_steps=config.num_inference_steps,
            guidance_scale=config.guidance_scale,
        ).images[0]
        return image
```
## Wrapping inference in a Gradio UI

Finally, we set up a [Gradio](https://www.gradio.app/) UI that will allow us to interact with our icon generator.
That lets us build this entire app, from data prep to browser app, in Python.

Our Gradio app calls the `Model.inference` function we defined above.

We can do this from any Python code we want,
but we choose to also make this part of our Modal app,
because [Modal makes it easy to host Python web apps](https://modal.com/docs/guide/webhooks).

```
# fine-tune-stable-diffusion.py
@app.function(
    image=image,
    max_containers=3,
)
@asgi_app()
def fastapi_app():
    import gradio as gr
    from gradio.routes import mount_gradio_app
    # Call to the GPU inference function on Modal.
    def go(text):
        return Model().inference.remote(text, config)
    # set up AppConfig
    config = AppConfig()
    prefix = "an icon of"
    example_prompts = [
        f"{prefix} a movie ticket",
        f"{prefix} campfire",
        f"{prefix} a castle",
        f"{prefix} a German Shepherd",
    ]
    description = f"""Describe a concept that you would like drawn as a [Heroicon](https://heroicons.com/). Try the examples below for inspiration.
    """
    # add a gradio UI around inference
    interface = gr.Interface(
        fn=go,
        inputs="text",
        outputs=gr.Image(shape=(512, 512)),
        title="Generate custom heroicons",
        examples=example_prompts,
        description=description,
        css="/assets/index.css",
        allow_flagging="never",
    )
    # mount for execution on Modal
    return mount_gradio_app(
        app=web_app,
        blocks=interface,
        path="/",
    )
```
Deployment on Modal is as simple as running one command:

`modal deploy fine-tune-stable-diffusion.py`## Parting thoughts

How does our fine-tuned model do as an infinite icon library?

![More generated Heroicons](https://modal-cdn.com/cdnbot/fine-tuning-stable-diffusion-generated-heroicons-more.png)



`camera`, `chemistry`, `fountain-pen`.Middle row:

`german-shepherd`, `international-monetary-system`, `library`.Bottom row:

`skiing`, `snowman`, `water-bottle`It’s certainly not perfect:

- The model sometimes outputs multiple objects when prompted for one (`water-bottle`,`fountain-pen`).
- Some icons have visual artifacts or strange shapes (`snowman`).
- The outputs aren’t as simple as the real Heroicons (`camera`,`german-shepherd`).

Fine-tuning can be sensitive to the hyperparameters used, including dataset size, number of training steps, learning rates, and resolution.

Because we defined our training to run on Modal, we can immediately scale it up into a massive grid search — running tens or hundreds or thousands of copies of the training script at once, each with different hyperparameters.

And it only takes a few lines of code to set up a grid search. It might look like this:

```
RESOLUTIONS = [128, 512]
LEARNING_RATES = [1e-5, 1e-4, 1e-3, 1e-2, 1e-1]
LEARNING_RATE_SCHEDULERS = ["constant", "cosine"]
@app.local_entrypoint()
def run():
    from uuid import uuid4
    configs = []
    for resolution in RESOLUTIONS:
        for learning_rate in LEARNING_RATES:
            for learning_rate_scheduler in LEARNING_RATE_SCHEDULERS:
                train.spawn(
                    {
                        "resolution": resolution,
                        "learning_rate": learning_rate,
                        "learning_rate_scheduler": learning_rate_scheduler,
                        "output_dir": uuid4(),
                    }
                )
```
Evaluation of which hyperparameter combinations are best will probably have to be done manually, given how subjective style can be.

But that’s what makes machine learning ~~hard~~ fun!
