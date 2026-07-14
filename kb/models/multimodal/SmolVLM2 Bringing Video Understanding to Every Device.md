---
title: 'SmolVLM2: Bringing Video Understanding to Every Device'
kind: blog
topic: models
subtopic: multimodal
secondary_topics:
- infra-platform/edge
summary: SmolVLM2 brings video understanding to 2.2B, 500M and 256M parameter VLMs
  — the smallest video LMs released — with benchmark results on Video-MME/MLVU and
  demos running on an iPhone via MLX and in the browser. Covers the frame-sampling/visual-token
  budget that makes video feasible at these sizes and the transformers/MLX fine-tuning
  paths.
triage: null
skip_reason: null
source: huggingface
url: https://huggingface.co/blog/smolvlm2
author: Orr Zohar; Miquel Farré; Andres Marafioti; Merve; Pedro Cuenca; Cyril; Joshua
published: '2025-02-20'
fetched: '2026-07-14T22:09:11Z'
classifier: claude
taxonomy_rev: 1
words: 2140
content_sha256: e776443440bffdcc1638d896e3ad50ef75be1e92604c6b8a5e8282e1ba13807b
---

# SmolVLM2: Bringing Video Understanding to Every Device

Image-Text-to-Text •  0.3B • Updated   •  1.07M  •  389  

#### HuggingFaceTB/SmolVLM-256M-Instruct

![](https://cdn-avatars.huggingface.co/v1/production/uploads/651e96991b97c9f33d26bde6/e4VK7uW5sTeCYupD0s_ob.png) 

 Published
					February 20, 2025 

  Upvote 

 344

orrzohar    

SmolVLM2 represents a fundamental shift in how we think about video understanding - moving from massive models that require substantial computing resources to efficient models that can run anywhere. Our goal is simple: make video understanding accessible across all devices and use cases, from phones to servers.

We are releasing models in three sizes (2.2B, 500M and 256M), MLX ready (Python *and* Swift APIs) from day zero.
We've made all models and demos available [in this collection](https://huggingface.co/collections/HuggingFaceTB/smolvlm2-smallest-video-lm-ever-67ab6b5e84bf8aaa60cb17c7). 

Want to try SmolVLM2 right away? Check out our [interactive chat interface](https://huggingface.co/spaces/HuggingFaceTB/SmolVLM2) where you can test visual and video understanding capabilities of SmolVLM2 2.2B through a simple, intuitive interface.

- [SmolVLM2: Bringing Video Understanding to Every Device](https://huggingface.co#smolvlm2-bringing-video-understanding-to-every-device)

We are introducing three new models with 256M, 500M and 2.2B parameters. The 2.2B model is the go-to choice for vision and video tasks, while the 500M and 256M models represent **the smallest video language models ever released**.

While they're small in size, they outperform any existing models per memory consumption. Looking at Video-MME (the go-to scientific benchmark in video), SmolVLM2 joins frontier model families on the 2B range and we lead the pack in the even smaller space.

*Video-MME stands out as a comprehensive benchmark due to its extensive coverage across diverse video types, varying durations (11 seconds to 1 hour), multiple data modalities (including subtitles and audio), and high-quality expert annotations spanning 900 videos totaling 254 hours. Learn more  here.*

Compared with the previous SmolVLM family, our new 2.2B model got better at solving math problems with images, reading text in photos, understanding complex diagrams, and tackling scientific visual questions. This shows in the model performance across different benchmarks:

When it comes to video tasks, 2.2B is a good bang for the buck. Across the various scientific benchmarks we evaluated it on, we want to highlight its performance on Video-MME where it outperforms all existing 2B models.

We were able to achieve a good balance on video/image performance thanks to the data mixture learnings published in [Apollo: An Exploration of Video Understanding in Large Multimodal Models](https://apollo-lmms.github.io/)

It’s so memory efficient, that you can run it even in a free Google Colab.

```
# Install transformers from `main` or from this stable branch:
!pip install git+https://github.com/huggingface/transformers@v4.49.0-SmolVLM-2
from transformers import AutoProcessor, AutoModelForImageTextToText
import torch
model_path = "HuggingFaceTB/SmolVLM2-2.2B-Instruct"
processor = AutoProcessor.from_pretrained(model_path)
model = AutoModelForImageTextToText.from_pretrained(
    model_path,
    torch_dtype=torch.bfloat16,
    _attn_implementation="flash_attention_2"
).to("cuda")
messages = [
    {
        "role": "user",
        "content": [
            {"type": "video", "path": "path_to_video.mp4"},
            {"type": "text", "text": "Describe this video in detail"}
        ]
    },
]
inputs = processor.apply_chat_template(
    messages,
    add_generation_prompt=True,
    tokenize=True,
    return_dict=True,
    return_tensors="pt",
).to(model.device, dtype=torch.bfloat16)
generated_ids = model.generate(**inputs, do_sample=False, max_new_tokens=64)
generated_texts = processor.batch_decode(
    generated_ids,
    skip_special_tokens=True,
)
print(generated_texts[0])
```
Nobody dared to release such small video models until today.

Our new [SmolVLM2-500M-Video-Instruct](https://huggingface.co/HuggingFaceTB/SmolVLM2-500M-Video-Instruct) model has video capabilities very close to SmolVLM 2.2B, but at a fraction of the size: we're getting the same video understanding capabilities with less than a quarter of the parameters 🤯.

And then there's our little experiment, the SmolVLM2-256M-Video-Instruct. Think of it as our "what if" project - what if we could push the boundaries of small models even further? Taking inspiration from what [IBM achieved](https://ds4sd.github.io/docling/examples/pictures_description/) with our base [SmolVLM-256M-Instruct](https://huggingface.co/HuggingFaceTB/SmolVLM-256M-Instruct) a few weeks ago, we wanted to see how far we could go with video understanding. While it's more of an experimental release, we're hoping it'll inspire some creative applications and specialized fine-tuning projects.

To demonstrate our vision in small video models, we've built three practical applications that showcase the versatility of these models.

|  | We've created an iPhone app running SmolVLM2 completely locally. Using our 500M model, users can analyze and understand video content directly on their device - no cloud required. Interested in building iPhone video processing apps with AI models running locally? We're releasing it very soon - [fill this form to test and build with us!](https://huggingface.co/spaces/HuggingFaceTB/SmolVLM2-iPhone-waitlist) | 

|  | Working in collaboration with VLC media player, we're integrating SmolVLM2 to provide intelligent video segment descriptions and navigation. This integration allows users to search through video content semantically, jumping directly to relevant sections based on natural language descriptions. While this is work in progress, you can experiment with the current playlist builder prototype [in this space.](https://huggingface.co/spaces/HuggingFaceTB/SmolVLM2-XSPFGenerator) | 

|  | Available as a Hugging Face Space, this application takes long-form videos (1+ hours) and automatically extracts the most significant moments. We've tested it extensively with soccer matches and other lengthy events, making it a powerful tool for content summarization. [Try it yourself in our demo space.](https://huggingface.co/spaces/HuggingFaceTB/SmolVLM2-HighlightGenerator) | 

We make SmolVLM2 available to use with transformers and MLX from day zero. In this section, you can find different inference alternatives and tutorials for video and multiple images.

The easiest way to run inference with the SmolVLM2 models is through the conversational API – applying the chat template takes care of preparing all inputs automatically.

You can load the model as follows.

```
# Install transformers from `main` or from this stable branch:
!pip install git+https://github.com/huggingface/transformers@v4.49.0-SmolVLM-2
from transformers import AutoProcessor, AutoModelForImageTextToText
import torch
processor = AutoProcessor.from_pretrained(model_path)
model = AutoModelForImageTextToText.from_pretrained(
    model_path,
    torch_dtype=torch.bfloat16,
    _attn_implementation="flash_attention_2"
).to("cuda")
```
You can pass videos through a chat template by passing in `{"type": "video", "path": {video_path}`. See below for a complete example. 

```
messages = [
    {
        "role": "user",
        "content": [
            {"type": "video", "path": "path_to_video.mp4"},
            {"type": "text", "text": "Describe this video in detail"}
        ]
    },
]
inputs = processor.apply_chat_template(
    messages,
    add_generation_prompt=True,
    tokenize=True,
    return_dict=True,
    return_tensors="pt",
).to(model.device, dtype=torch.bfloat16)
generated_ids = model.generate(**inputs, do_sample=False, max_new_tokens=64)
generated_texts = processor.batch_decode(
    generated_ids,
    skip_special_tokens=True,
)
print(generated_texts[0])
```
In addition to video, SmolVLM2 supports multi-image conversations. You can use the same API through the chat template, providing each image using a filesystem path, an URL, or a `PIL.Image` object:

```
messages = [
    {
        "role": "user",
        "content": [
            {"type": "text", "text": "What are the differences between these two images?"},
          {"type": "image", "url": "https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/bee.jpg"},
          {"type": "image", "url": "https://huggingface.co/datasets/huggingface/documentation-images/resolve/0052a70beed5bf71b92610a43a52df6d286cd5f3/diffusers/rabbit.jpg"},            
        ]
    },
]
inputs = processor.apply_chat_template(
    messages,
    add_generation_prompt=True,
    tokenize=True,
    return_dict=True,
    return_tensors="pt",
).to(model.device, dtype=torch.bfloat16)
generated_ids = model.generate(**inputs, do_sample=False, max_new_tokens=64)
generated_texts = processor.batch_decode(
    generated_ids,
    skip_special_tokens=True,
)
print(generated_texts[0])
```
To run SmolVLM2 with MLX on Apple Silicon devices using Python, you can use the excellent [mlx-vlm library](https://github.com/Blaizzy/mlx-vlm).
First, you need to install `mlx-vlm` from [this branch](https://github.com/Blaizzy/mlx-vlm/pull/208) using the following command:

```
pip install git+https://github.com/pcuenca/mlx-vlm.git@smolvlm
```
Then you can run inference on a single image using the following one-liner, which uses [the unquantized 500M version of SmolVLM2](https://huggingface.co/HuggingFaceTB/SmolVLM2-500M-Video-Instruct-mlx):

```
python -m mlx_vlm.generate \
  --model mlx-community/SmolVLM2-500M-Video-Instruct-mlx \
  --image https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/bee.jpg \
  --prompt "Can you describe this image?"
```
We also created a simple script for video understanding. You can use it as follows:

```
python -m mlx_vlm.smolvlm_video_generate \
  --model mlx-community/SmolVLM2-500M-Video-Instruct-mlx \
  --system "Focus only on describing the key dramatic action or notable event occurring in this video segment. Skip general context or scene-setting details unless they are crucial to understanding the main action." \
  --prompt "What is happening in this video?" \
  --video /Users/pedro/Downloads/IMG_2855.mov \
  --prompt "Can you describe this image?"
```
Note that the system prompt is important to bend the model to the desired behaviour. You can use it to, for example, describe all scenes and transitions, or to provide a one-sentence summary of what's going on.

The Swift language is also supported through the [mlx-swift-examples repo](https://github.com/ml-explore/mlx-swift-examples), which is what we used to build our iPhone app.

Until [our in-progress PR](https://github.com/ml-explore/mlx-swift-examples/pull/206) is finalized and merged, you have to compile the project [from this fork](https://github.com/cyrilzakka/mlx-swift-examples), and then you can use the `llm-tool` CLI on your Mac as follows.

For image inference:

```
./mlx-run --debug llm-tool \
    --model mlx-community/SmolVLM2-500M-Video-Instruct-mlx \
    --prompt "Can you describe this image?" \
    --image https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/bee.jpg \
    --temperature 0.7 --top-p 0.9 --max-tokens 100
```
Video analysis is also supported, as well as providing a system prompt. We found system prompts to be particularly helpful for video understanding, to drive the model to the desired level of detail we are interested in. This is a video inference example:

```
./mlx-run --debug llm-tool \
    --model mlx-community/SmolVLM2-500M-Video-Instruct-mlx \
    --system "Focus only on describing the key dramatic action or notable event occurring in this video segment. Skip general context or scene-setting details unless they are crucial to understanding the main action." \
    --prompt "What is happening in this video?" \
    --video /Users/pedro/Downloads/IMG_2855.mov \
    --temperature 0.7 --top-p 0.9 --max-tokens 100
```
If you integrate SmolVLM2 in your apps using MLX and Swift, we'd love to know about it! Please, feel free to drop us a note in the comments section below!

You can fine-tune SmolVLM2 on videos using transformers 🤗
We have fine-tuned the 500M variant in Colab on video-caption pairs in [VideoFeedback](https://huggingface.co/datasets/TIGER-Lab/VideoFeedback) dataset for demonstration purposes. Since the 500M variant is small, it's better to apply full fine-tuning instead of QLoRA or LoRA, meanwhile you can try to apply QLoRA on cB variant. You can find the fine-tuning notebook [here](https://github.com/huggingface/smollm/blob/main/vision/finetuning/SmolVLM2_Video_FT.ipynb).

You can cite us in the following way:

```
@article{marafioti2025smolvlm,
  title={SmolVLM: Redefining small and efficient multimodal models}, 
  author={Andrés Marafioti and Orr Zohar and Miquel Farré and Merve Noyan and Elie Bakouch and Pedro Cuenca and Cyril Zakka and Loubna Ben Allal and Anton Lozhkov and Nouamane Tazi and Vaibhav Srivastav and Joshua Lochner and Hugo Larcher and Mathieu Morlon and Lewis Tunstall and Leandro von Werra and Thomas Wolf},
  journal={arXiv preprint arXiv:2504.05299},
  year={2025}
}
```
We would like to thank Raushan Turganbay, Arthur Zucker and Pablo Montalvo Leroux for their contribution of the model to transformers.

We are looking forward to seeing all the things you'll build with SmolVLM2! If you'd like to learn more about the SmolVLM family of models, feel free to read the following:

 Image-Text-to-Text •  0.3B • Updated   •  1.07M  •  389 

 Image-Text-to-Text •  0.5B • Updated   •  759k  •  160 

 Viewer • Updated  •  37.7k •  19.8k  •  35 

📊

 81

Ask questions about images or videos and get answers

More Articles from our Blog

multimodalon-devicellm

  Hot
- +1

 422

 November 26, 2024 multimodalon-devicellm

 
- +3

 192

 September 25, 2024 📻 🎙️ Hey, I generated an **AI podcast** about this blog post, check it out!

*This podcast is generated via  ngxson/kokoro-podcast-generator, using DeepSeek-R1 and Kokoro-TTS.*

when run this script:

python -m mlx_vlm.generate 

  --model mlx-community/SmolVLM2-500M-Video-Instruct-mlx 

  --image [https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/bee.jpg](https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/bee.jpg) 

  --prompt "Can you describe this image?"

======================================

test errror:

Files: ['[https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/bee.jpg']](https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/bee.jpg'%5D) 

Prompt: <|im_start|>User:Can you describe this image?


Assistant:

Traceback (most recent call last):

  File "", line 198, in _run_module_as_main

  File "", line 88, in _run_code

  File "/opt/homebrew/Caskroom/miniconda/base/envs/playwright/lib/python3.12/site-packages/mlx_vlm/generate.py", line 156, in 

    main()

  File "/opt/homebrew/Caskroom/miniconda/base/envs/playwright/lib/python3.12/site-packages/mlx_vlm/generate.py", line 141, in main

    output = generate(

             ^^^^^^^^^

  File "/opt/homebrew/Caskroom/miniconda/base/envs/playwright/lib/python3.12/site-packages/mlx_vlm/utils.py", line 1115, in generate

    for response in stream_generate(model, processor, prompt, image, **kwargs):

                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "/opt/homebrew/Caskroom/miniconda/base/envs/playwright/lib/python3.12/site-packages/mlx_vlm/utils.py", line 1016, in stream_generate

    inputs = prepare_inputs(

             ^^^^^^^^^^^^^^^

  File "/opt/homebrew/Caskroom/miniconda/base/envs/playwright/lib/python3.12/site-packages/mlx_vlm/utils.py", line 806, in prepare_inputs

    processor.tokenizer.pad_token = processor.tokenizer.eos_token

                                    ^^^^^^^^^^^^^^^^^^^

  File "/opt/homebrew/Caskroom/miniconda/base/envs/playwright/lib/python3.12/site-packages/transformers/tokenization_utils_base.py", line 1108, in **getattr**

    raise AttributeError(f"{self.**class**.**name**} has no attribute {key}")

AttributeError: GPT2TokenizerFast has no attribute tokenizer. Did you mean: '_tokenizer'?

Hi [@leexiaobo2006](https://huggingface.co/leexiaobo2006) ! You need to install transformers from `main`, or from this stable branch:

```
pip install git+https://github.com/huggingface/transformers@v4.49.0-SmolVLM-2
```
here is a tutorial on how to use SMOLVLM2 on colab for free using T4 GPU Free Tier

where to find th code of app demo [@pcuenq](https://huggingface.co/pcuenq)  

•

 Nice work!

Do you know where is the code repo for Video Highlight Generator? Thanks! [@pcuenq](https://huggingface.co/pcuenq)  

Hi!

You can find it here: [https://huggingface.co/spaces/HuggingFaceTB/SmolVLM2](https://huggingface.co/spaces/HuggingFaceTB/SmolVLM2)

Then press three dots -> Clone repository

i have seen vlms which are great but they do inference via frame by frame which can lead to false alarms

can this model understand the video(take chunks of frame and uderstand the nature of video ) ?

Hi - what is the longest duration of video this can handle ?

Could someone share how video processing in this model is handled?

Hi, can I ask if SmolVLM2 supports semantic segmentation ?

[@dangmanhtruong1995](https://huggingface.co/dangmanhtruong1995)  hello, unfortunately no. I think all vision LMs **that support segmentation** support instance segmentation, you can then aggregate masks together to come up with semantic ones. PaliGemma2 does it, maybe SAM3 (it takes in short prompts like "red car" and not "red car on the left")

SmolVLM2 feels like a genuinely practical step forward, especially in a world where not everyone has access to high-end hardware but still wants meaningful video insights... the idea of shifting from heavy, resource-hungry systems to something lightweight and widely usable just makes sense, and it opens the door for more everyday applications.... from mobile users to small developers.[.](https://www.moviebox4u.app/).. without needing complex setups, which is why I find this approach both timely and necessary, even without needing to point to any specific source URL to see its value clearly.

I understand but some confussion there anyone help me?

SmolVLM2 is an advanced video understanding model designed to run efficiently on a wide range of devices. It enables fast video analysis, caption generation, and visual reasoning without requiring powerful hardware. For Alooy TV APK users, similar AI-powered technology can enhance content discovery, improve recommendations, and deliver a smarter, more personalized streaming experience.[https://alooytvlive.com/](https://alooytvlive.com/)
