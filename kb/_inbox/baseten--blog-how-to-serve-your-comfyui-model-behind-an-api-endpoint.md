---
title: How to serve your ComfyUI model behind an API endpoint
kind: blog
topic: null
subtopic: null
secondary_topics: []
summary: null
triage: null
skip_reason: null
source: baseten
url: https://www.baseten.co/blog/how-to-serve-your-comfyui-model-behind-an-api-endpoint
author: Het Trivedi
published: '2023-12-08'
fetched: '2026-11-12T06:11:42Z'
classifier: null
taxonomy_rev: 2
words: 1220
content_sha256: 0f499ea51e02ee13c0eebb5148e00c494e1f2c44649eca6036c38fce255f9bd4
---

# How to serve your ComfyUI model behind an API endpoint

AI engineering
# How to serve your ComfyUI model behind an API endpoint

This guide details deploying ComfyUI image generation pipelines via API for app integration, using Truss for packaging & production deployment.


- Authors
- Date
- December 8, 2023

TLDR

In this guide, we’ll deploy image generation pipelines built with ComfyUI behind an API endpoint so they can be shared and used in applications. To serve the model pipeline in production, we’ll export the ComfyUI project in an API format, then use Truss for packaging and deployment.

Author's note: Looking for more information on deploying ComfyUI workflows? Check out our [latest guide to using ComfyUI with Baseten](https://www.baseten.co/blog/deploying-custom-comfyui-workflows-as-apis/)!

[ComfyUI](https://github.com/comfyanonymous/ComfyUI) is a GUI and backend for running Stable Diffusion models locally. It is especially useful for building image generation pipelines that connect multiple models together to create images beyond the capabilities of Stable Diffusion alone.

But once you’ve created a powerful image generation pipeline with ComfyUI, what if you want to build an application around the pipeline? That’s where Baseten comes in. Using Truss, our open-source model packaging framework, you can deploy your ComfyUI pipeline behind an API endpoint in minutes.

In this guide, we’ll deploy an image generation pipeline that uses ControlNet to let users generate unique images based on their company’s logo, like these examples:

Before we dive into the full tutorial, here’s how you can get the project up and running in just a couple of minutes. To complete this tutorial, you’ll need a [Baseten account](https://app.baseten.co/signup/) and API key.

First, install the latest version of Truss from PyPi.

bash

`pip install --upgrade truss`
Then, clone the prepared project from GitHub and deploy the model to Baseten. You’ll need your Baseten API key for this step.

```
git clone https://github.com/basetenlabs/truss-examples.git
cd comfyui-truss
truss push
```
To call the deployed model, you’ll need:

- Your model ID, which can be found in the "call model" dialogue on the model overview page.
- Your Baseten API key.

With those two values, run the following Python script to call the model and store the image output.

python

```
import os
import random
import base64
import requests
# Set essential values
model_id = ""
baseten_api_key = ""
# Set prompts and controlnet image
values = {
  "positive_prompt": "A top down view of a river through the woods",
  "negative_prompt": "blurry, text, low quality",
  "controlnet_image": "https://storage.googleapis.com/logos-bucket-01/baseten_logo.png",
  "seed": random.randint(1, 1000000)
}
# Call model endpoint
res = requests.post(
    f"https://model-{model_id}.api.baseten.co/development/predict",
    headers={"Authorization": f"Api-Key {baseten_api_key}"},
    json={"workflow_values": values}
)
# Get output image
res = res.json()
preamble = "data:image/png;base64,"
output = base64.b64decode(res["result"][1]["image"].replace(preamble, ""))
# Save image to file
img_file = open("comfyui.png", 'wb')
img_file.write(output)
img_file.close()
os.system("open comfyui.png")
```
Next, we’ll dive into the actual tutorial and build this Truss step-by-step so that you can package and deploy any ComfyUI project.

ComfyUI is used for building image pipelines by connecting multiple models: Stable Diffusion base models, ControlNets, LoRAs, and more.

If you have an existing ComfyUI project that you want to serve as an API, load it up and we’ll export it in the next step.

Otherwise, use the provided workflow that we prepared for this tutorial. The workflow takes a prompt and a simple geometric image like a logo. Using a ControlNet and Stable Diffusion XL, it creates an image with the logo embedded.

You don’t need to load the provided workflow locally to complete the tutorial (you’ll be given the exported version in the next step), but if you’d like to play around with it, follow these steps:

1. Ensure ComfyUI is [installed properly in your local development environment](https://github.com/comfyanonymous/ComfyUI#installing).
2. Download the following models and install them in the appropriate folders:
3. [SDXL base](https://huggingface.co/stabilityai/stable-diffusion-xl-base-1.0/resolve/main/sd_xl_base_1.0.safetensors) in models/checkpoints.
4. [ControlNet](https://huggingface.co/diffusers/controlnet-canny-sdxl-1.0/resolve/main/diffusion_pytorch_model.fp16.safetensors) in models/ControlNet.
5. Run ComfyUI locally (`python main.py --force-fp16` on MacOS) and use the "Load" button to import [this JSON file with the prepared workflow](https://github.com/basetenlabs/truss-examples/blob/main/assets/sdxl-controlnet-workflow.json).

Exporting your ComfyUI project to an [API-compatible JSON file](https://github.com/basetenlabs/truss-examples/tree/main/comfyui-truss/data/comfy_ui_workflow.json) is a bit trickier than just saving the project. While ComfyUI lets you save a project as a JSON file, that file will not work for our purposes. Instead, you need to export the project in a specific API format.

First, we need to enable dev mode options to get access to the API format. Click on the gear icon in your menu box:

Then, check the box that says "Enable Dev mode Options:"

Returning to the menu box, you should now see an option that says "Save (API Format)" which will export your project in the appropriate format:

Using the [provided Truss template](https://github.com/basetenlabs/truss-examples/tree/main/comfyui-truss), you can package your ComfyUI project for deployment.

The API format workflow file that you exported in the previous step must be added to the `data/` directory in your Truss with the file name `comfy_ui_workflow.json`. Delete any existing file with that name and replace it with your exported workflow.

To load your checkpoints into ComfyUI you can use the `build_commands` key in the `config.yaml` file. Here is an example of what that looks like:

yaml

```
build_commands:
- git clone https://github.com/comfyanonymous/ComfyUI.git
- cd ComfyUI && pip install -r requirements.txt
- cd ComfyUI/models/controlnet && wget -O diffusers_xl_canny_full.safetensors https://huggingface.co/diffusers/controlnet-canny-sdxl-1.0/resolve/main/diffusion_pytorch_model.fp16.safetensors
- cd ComfyUI/models/checkpoints && wget -O sd_xl_base_1.0.safetensors https://huggingface.co/stabilityai/stable-diffusion-xl-base-1.0/resolve/main/sd_xl_base_1.0.safetensors
```
Under the hood, `build_commands` runs each of the shell commands sequentially during the build phase. This means that everything that all kinds of weights — checkpoints, ControlNets, LoRAs — get cached within the Docker image for faster cold starts.

In the build commands, you have the flexibility to create new directories and place downloaded files anywhere to match the structure of your ComfyUI project.

If you wish, you can rename your model by changing the `model_name` setting in `config.yaml`.

You’ll need to change the model name if you want to deploy multiple different ComfyUI projects; Baseline uses the `model_name` setting to determine whether to deploy a new model or update an existing one.

Once your model is packaged, deployment is straightforward. In your terminal, use the Truss CLI and run:

`truss push`
Your model will be deployed on to your Baseten workspace as a development deployment, which supports a live reload workflow for iterating on your model. Check deployment progress on the model overview page, and use the logs to debug any issues during deployment.

Once your model is deployed, it’ll be available behind an API endpoint.

You’ll need 2 values to call the model:

- Your model ID, which can be found in the "call model" dialogue on the model overview page.
- Your Baseten API key. If you need a new API key, you can generate it from the "call model" dialogue on the model overview page.

The deployed model accepts the following parameters as input:

- `positive_prompt`: A string detailing what you want the model to generate.
- `negative_prompt`: A string with terms that you want the model to avoid during image generation.
- `controlnet_image`: A URL pointing to a square PNG image with the logo that you want to embed in your output image.
- `seed`: An integer value that can be used to repeat the same image from the same prompt.

The model returns two images: one of the logo converted to black and white, the other of the final output. These images are base64 encoded, so it takes a bit of parsing to get your final result. Here’s a code sample for creating an image end-to-end:

And of course, the result!
