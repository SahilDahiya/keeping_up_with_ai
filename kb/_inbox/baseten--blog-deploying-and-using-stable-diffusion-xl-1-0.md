---
title: Deploying and using Stable Diffusion XL 1.0
kind: blog
topic: null
subtopic: null
secondary_topics: []
summary: null
triage: null
skip_reason: null
source: baseten
url: https://www.baseten.co/blog/deploying-and-using-stable-diffusion-xl-1-0
author: Philip Kiely
published: '2023-07-26'
fetched: '2026-11-12T06:13:38Z'
classifier: null
taxonomy_rev: 2
words: 286
content_sha256: 33d50a63b5baae675c33e8b41fe15a0792aa2ea2c37bb22ba3e270a081f3dce1
---

# Deploying and using Stable Diffusion XL 1.0

AI engineering
# Deploying and using Stable Diffusion XL 1.0

Deploy Stable Diffusion XL 1.0 for free to generate images from text prompts and invoke Stable Diffusion with the Baseten Python client.


- Authors
- Date
- July 26, 2023

TLDR

Stable Diffusion XL 1.0 is a highly capable text-to-image model by Stability AI that was released on July 26, 2023 under their CreativeML Open RAIL++-M license.

You can deploy Stable Diffusion XL 1.0 in 2 clicks from Baseten’s model library. It’s also available packaged as a Truss on GitHub.

Stable Diffusion XL requires an A100 for invocation. In our testing, it takes 8-12 seconds to generate an image.

bash

```
pip install --upgrade truss
git clone https://github.com/basetenlabs/truss-examples
cd stable-diffusion/stable-diffusion-xl-1.0
truss push
```
Paste your API key when prompted.

This model is capable of generating stunningly detailed and accurate images from simple prompts.

To invoke the model, run:

`truss predict -d '{"prompt": "A tree in a field under the night sky"}' | python show.py`
The output will be a dictionary with a key `data` mapping to a base64 encoded image. The provided bash script runs the output through the following Python code to save the generated image:

python

```
import json
import base64
import os, sys
resp = sys.stdin.read()
image = json.loads(resp)["data"]
img=base64.b64decode(image)
file_name = f'{image[-10:].replace("/", "")}.jpeg'
img_file = open(file_name, 'wb')
img_file.write(img)
img_file.close()
os.system(f'open {file_name}')
```
The [Stable Diffusion Refiner model](https://huggingface.co/stabilityai/stable-diffusion-xl-refiner-1.0) adds accuracy to difficult-to-generate details like facial features and hands. You can choose whether or not to use the refiner model in an invocation with the `use_refiner` parameter.

`truss predict -d '{"prompt": "A tree in a field under the night sky", "use_refiner": true}' | python show.py`
Reach out to us at [support@baseten.co](mailto:support@baseten.co) with any questions!
