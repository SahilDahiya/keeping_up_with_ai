---
title: Deploying custom ComfyUI workflows as APIs
topic: models
subtopic: multimodal
secondary_topics:
- infra-platform/deployment
summary: Shows how to deploy custom ComfyUI image-generation workflows behind API
  endpoints.
source: baseten
url: https://www.baseten.co/blog/deploying-custom-comfyui-workflows-as-apis/
author: Het Trivedi; Rachel Rapp
published: '2024-07-25'
fetched: '2026-07-11T04:09:21Z'
classifier: codex
taxonomy_rev: 1
words: 1183
content_sha256: be1cccfe9f7f16e2f1508fd178e87374c1bf8f85c4bb1d050d856fb5e3d6ef8b
triage: keep
skip_reason: null
---

# Deploying custom ComfyUI workflows as APIs

![Deploying ComfyUI](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1747439144-deploying-comfyui.png%3Fauto%3Dformat%26fit%3Dcrop%26h%3D630%26w%3D1200&w=3840&q=100)

We released a new feature that enables building custom ComfyUI workflows using any node or model checkpoint! You could already [serve your ComfyUI model behind an API endpoint](https://www.baseten.co/blog/how-to-serve-your-comfyui-model-behind-an-api-endpoint/) on Baseten—now, serving custom image generation pipelines is even easier.

[ComfyUI](https://github.com/comfyanonymous/ComfyUI) is a popular GUI used to power Stable Diffusion workflows. Instead of the complexity of needing to know the diffuser’s code, ComfyUI gives you a simple user interface to run Stable Diffusion.

For most workflows using ComfyUI, the ability to run custom nodes has become essential. That’s why we built our new `build_commands` feature: you can now easily package your ComfyUI workflow to use any custom node or model checkpoint on Baseten! 

Let’s walk through an example together.

## How to deploy a custom ComfyUI workflow

Style transfer is all the rage these days, so let’s deploy a style transfer workflow on Baseten that converts a picture of a pet into an anime style. The workflow we will be using can be found [here](https://openart.ai/workflows/willling/animal-2-anime/NoE7zH8tJ4KlrXbFr6AG). 

![An example ComfyUI workflow used for building custom ComfyUI workflows on Baseten.](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1721734125-comfyuiworkflow.webp%3Fauto%3Dformat%26w%3D1200&w=3840&q=75)

First, let’s grab the ComfyUI Truss from the[ Truss examples Github repository](https://github.com/basetenlabs/truss-examples/tree/main/comfyui-truss): 

```
git clone https://github.com/basetenlabs/truss-examples.git
cd truss-examples/comfyui-truss
```
This repository already contains all the files we need to deploy our ComfyUI workflow. There are just two files we need to modify: `config.yaml` and `data/comfy_ui_workflow.json`. Let’s start with the `config.yaml` .

### Step 1: Adding the `build_commands` inside the `config.yaml`

Inside the `config.yaml` file, we can specify a key called `build_commands`, which are shell commands that will run during our container build process. Here is an example:

```
1build_commands:
2- git clone https://github.com/comfyanonymous/ComfyUI.git
3- cd ComfyUI && git checkout b1fd26fe9e55163f780bf9e5f56bf9bf5f035c93 && pip install -r requirements.txt
4- cd ComfyUI/custom_nodes && git clone https://github.com/LykosAI/ComfyUI-Inference-Core-Nodes --recursive && cd ComfyUI-Inference-Core-Nodes && pip install -e .[cuda12]
5- cd ComfyUI/custom_nodes && git clone https://github.com/ZHO-ZHO-ZHO/ComfyUI-Gemini --recursive && cd ComfyUI-Gemini && pip install -r requirements.txt
6- cd ComfyUI/custom_nodes && git clone https://github.com/kijai/ComfyUI-Marigold --recursive && cd ComfyUI-Marigold && pip install -r requirements.txt
7- cd ComfyUI/custom_nodes && git clone https://github.com/omar92/ComfyUI-QualityOfLifeSuit_Omar92 --recursive
8- cd ComfyUI/custom_nodes && git clone https://github.com/Fannovel16/comfyui_controlnet_aux --recursive && cd comfyui_controlnet_aux && pip install -r requirements.txt
9- cd ComfyUI/models/controlnet && wget -O control-lora-canny-rank256.safetensors https://huggingface.co/stabilityai/control-lora/resolve/main/control-LoRAs-rank256/control-lora-canny-rank256.safetensors
10- cd ComfyUI/models/controlnet && wget -O control-lora-depth-rank256.safetensors https://huggingface.co/stabilityai/control-lora/resolve/main/control-LoRAs-rank256/control-lora-depth-rank256.safetensors
11- cd ComfyUI/models/checkpoints && wget -O dreamshaperXL_v21TurboDPMSDE.safetensors https://civitai.com/api/download/models/351306
12- cd ComfyUI/models/loras && wget -O StudioGhibli.Redmond-StdGBRRedmAF-StudioGhibli.safetensors https://huggingface.co/artificialguybr/StudioGhibli.Redmond-V2/resolve/main/StudioGhibli.Redmond-StdGBRRedmAF-StudioGhibli.safetensors
```
The ComfyUI manager allows you to easily install custom nodes. Behind the scenes, the manager simply clones a repository and installs the Python dependencies. We can simulate that behavior using a command like `git clone ... && pip install -r requirements`. Under `build_commands`, you can run arbitrary shell commands such as `git clone`, `cd`, or `wget`. This way, you can install any checkpoints, LoRAs, and ControlNets, and place them in the appropriate folders inside ComfyUI. You can even create new directories, such as `ipadapter`.

Each line under `build_commands` performs a Docker `RUN` command; since these are run during the image build step, they get cached into the Docker image. This way, when your container spins up, all custom nodes and models are already downloaded which significantly reduces the time for cold starts.

Here is the full `config.yaml` file we’ll use for our example:

```
1build_commands:
2- git clone https://github.com/comfyanonymous/ComfyUI.git
3- cd ComfyUI && git checkout b1fd26fe9e55163f780bf9e5f56bf9bf5f035c93 && pip install -r requirements.txt
4- cd ComfyUI/custom_nodes && git clone https://github.com/LykosAI/ComfyUI-Inference-Core-Nodes --recursive && cd ComfyUI-Inference-Core-Nodes && pip install -e .[cuda12]
5- cd ComfyUI/custom_nodes && git clone https://github.com/ZHO-ZHO-ZHO/ComfyUI-Gemini --recursive && cd ComfyUI-Gemini && pip install -r requirements.txt
6- cd ComfyUI/custom_nodes && git clone https://github.com/kijai/ComfyUI-Marigold --recursive && cd ComfyUI-Marigold && pip install -r requirements.txt
7- cd ComfyUI/custom_nodes && git clone https://github.com/omar92/ComfyUI-QualityOfLifeSuit_Omar92 --recursive
8- cd ComfyUI/custom_nodes && git clone https://github.com/Fannovel16/comfyui_controlnet_aux --recursive && cd comfyui_controlnet_aux && pip install -r requirements.txt
9- cd ComfyUI/models/controlnet && wget -O control-lora-canny-rank256.safetensors https://huggingface.co/stabilityai/control-lora/resolve/main/control-LoRAs-rank256/control-lora-canny-rank256.safetensors
10- cd ComfyUI/models/controlnet && wget -O control-lora-depth-rank256.safetensors https://huggingface.co/stabilityai/control-lora/resolve/main/control-LoRAs-rank256/control-lora-depth-rank256.safetensors
11- cd ComfyUI/models/checkpoints && wget -O dreamshaperXL_v21TurboDPMSDE.safetensors https://civitai.com/api/download/models/351306
12- cd ComfyUI/models/loras && wget -O StudioGhibli.Redmond-StdGBRRedmAF-StudioGhibli.safetensors https://huggingface.co/artificialguybr/StudioGhibli.Redmond-V2/resolve/main/StudioGhibli.Redmond-StdGBRRedmAF-StudioGhibli.safetensors
13environment_variables: {}
14external_package_dirs: []
15model_metadata: {}
16model_name: ComfyUI Anime Pet Style Transfer
17python_version: py310
18requirements:
19 - websocket-client==1.6.4
20 - accelerate==0.23.0
21 - opencv-python
22resources:
23 accelerator: A100
24 use_gpu: true
25secrets: {}
26system_packages:
27 - wget
28 - ffmpeg
29 - libgl1-mesa-glx
```
### Step 2: Modifying the ComfyUI workflow to an API-compatible format

ComfyUI workflows can be run on Baseten by exporting them in an API format. Check out our blog on [how to serve ComfyUI models behind an API endpoint](https://www.baseten.co/blog/how-to-serve-your-comfyui-model-behind-an-api-endpoint/) if you need help converting your workflow accordingly.

For this tutorial, the workflow file can be copied from [here](https://github.com/basetenlabs/truss-examples/blob/main/comfyui-truss/examples/anime-style-transfer/workflow.json). This workflow has two inputs: a prompt and an image. We can specify those variables inside our workflow JSON file using the handlebars template `{{prompt}}` and `{{input_image}}`.

That’s it! We can now deploy our ComfyUI workflow to Baseten!

### Step 3: Deploying your ComfyUI workflow to Baseten

To deploy our workflow to Baseten, make sure you have the `truss` Python package installed. 

`pip install truss --upgrade`With `truss_examples/comfyui_truss` as the root directory, we can run the following command to deploy to Baseten:

`truss push --publish`If prompted, paste in your [Baseten API key](https://docs.baseten.co/quickstart#get-your-api-key). This command will package your Truss and deploy it onto Baseten’s cloud. The Docker container will be built and then deployed as an API endpoint.

Now we’ll run our first inference!

## Running inference on your ComfyUI API endpoint

Once your model has deployed and is in the `active` state, you can call the API endpoint like this:

```
1import requests
2import os
3import base64
4from PIL import Image
5from io import BytesIO
6
7# Replace the empty string with your model id below
8model_id = ""
9baseten_api_key = os.environ["BASETEN_API_KEY"]
10BASE64_PREAMBLE = "data:image/png;base64,"
11
12def pil_to_b64(pil_img):
13   buffered = BytesIO()
14   pil_img.save(buffered, format="PNG")
15   img_str = base64.b64encode(buffered.getvalue()).decode("utf-8")
16   return img_str
17
18def b64_to_pil(b64_str):
19   return Image.open(BytesIO(base64.b64decode(b64_str.replace(BASE64_PREAMBLE, ""))))
20
21values = {
22 "prompt": "american Shorthair",
23 "input_image": {"type": "image", "data": pil_to_b64(Image.open("/path/to/cat.png"))}
24}
25
26resp = requests.post(
27   f"https://model-{model_id}.api.baseten.co/production/predict",
28   headers={"Authorization": f"Api-Key {baseten_api_key}"},
29   json={"workflow_values": values}
30)
31
32res = resp.json()
33results = res.get("result")
34
35for item in results:
36   if item.get("format") == "png":
37       data = item.get("data")
38       img = b64_to_pil(data)
39       img.save(f"pet-style-transfer-1.png")
```
The API call returns `result`, which is a list of images the model returns. The `data` for each item in `result` is the base64 string representation of the output image. We convert this base64 string to a PIL object and save it as an image.

Here are some sample inputs and their corresponding anime-stylized outputs:

![A cat pic turned into anime style with a custom ComfyUI workflow on Baseten](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1721734657-cat-style-transfer-diagram.jpg%3Fauto%3Dformat%26w%3D1200&w=3840&q=75)

![A picture of a maltipoo dog turned into anime style with a custom ComfyUI workflow on Baseten](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1721734672-maltipoo-style-transfer-diagram.jpg%3Fauto%3Dformat%26w%3D1200&w=3840&q=75)

That’s all it takes to run ComfyUI workflows as API endpoints on Baseten. Now, with the new `build_commands` feature, it's even easier to add your own custom nodes and model checkpoints. 

We’re dedicated to building an excellent developer experience around ComfyUI deployments. Try building your own custom ComfyUI workflow and [run it as a production-grade API service](https://github.com/basetenlabs/truss-examples/blob/main/comfyui-truss/README.md), or try launching a sample workflow [from our model library](https://www.baseten.co/library/comfy-ui/) — either way, be sure to tell us what you think!
