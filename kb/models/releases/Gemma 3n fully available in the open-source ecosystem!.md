---
title: Gemma 3n fully available in the open-source ecosystem!
kind: blog
topic: models
subtopic: releases
secondary_topics:
- infra-platform/edge
summary: 'Gemma 3n E2B/E4B: models with 5B and 8B actual parameters that need only
  2B/4B worth of VRAM (2-3 GB) thanks to per-layer embeddings and MatFormer nesting,
  paired with a MobileNet-V5-300 vision encoder (60 FPS on Pixel, beating ViT-Giant
  with 3x fewer params) and a USM-based audio encoder processing 160ms chunks.'
triage: null
skip_reason: null
source: huggingface
url: https://huggingface.co/blog/gemma3n
author: Aritra Roy Gosthipaty; Pedro Cuenca; Sergio Paniego; Vaibhav Srivastav; Christopher
  Fleetwood; Joshua; Steven Zheng; Kashif Rasul
published: '2025-06-26'
fetched: '2026-07-14T22:03:43Z'
classifier: claude
taxonomy_rev: 1
words: 1675
content_sha256: 0e10a72dee9aed7f25aad85e6cfcb14ac726694bd0e6d533d1e6ca6255cc83eb
---

# Gemma 3n fully available in the open-source ecosystem!

Image-Text-to-Text •  Updated   •  226  •  37  

#### onnx-community/gemma-3n-E2B-it-ONNX

![](https://cdn-avatars.huggingface.co/v1/production/uploads/61b253b7ac5ecaae3d1efe0c/BpiYJ-m5mXPXfjkzEt6yZ.png) 

 Published
					June 26, 2025 

  Upvote 

 121

Today, Gemma 3n is finally available on the most used open source libraries. This includes transformers & timm, MLX, llama.cpp (text inputs), transformers.js, ollama, Google AI Edge, and others.

This post quickly goes through practical snippets to demonstrate how to use the model with these libraries, and how easy it is to fine-tune it for other domains.

Here is the

[Gemma 3n Release Collection](https://huggingface.co/collections/google/gemma-3n-685065323f5984ef315c93f4)

Two model sizes have been released today, with two variants (base and instruct) each. The model names follow a non-standard nomenclature: they are called `gemma-3n-E2B` and `gemma-3n-E4B`. The `E` preceding the parameter count stands for `Effective`. Their actual parameter counts are `5B` and `8B`, respectively, but thanks to improvements in memory efficiency, they manage to only need 2B and 4B in VRAM (GPU memory). 

These models, therefore, behave like 2B and 4B in terms of hardware support, but they punch over 2B/4B in terms of quality. The `E2B` model can run in as little as 2GB of GPU RAM, while `E4B` can run with just 3GB of GPU RAM.

| Size | Base | Instruct | 
|---|---|---|
| 2B | [google/gemma-3n-e2b](https://hf.co/google/gemma-3n-e2b) | [google/gemma-3n-e2b-it](https://hf.co/google/gemma-3n-e2b-it) | 
| 4B | [google/gemma-3n-e4b](https://hf.co/google/gemma-3n-e4b) | [google/gemma-3n-e4b-it](https://hf.co/google/gemma-3n-e4b-it) | 

In addition to the language decoder, Gemma 3n uses an **audio encoder** and a **vision encoder**. We highlight their main features below, and describe how they have been added to `transformers` and `timm`, as they are the reference for other implementations.

- **Vision Encoder (MobileNet-V5).**Gemma 3n uses a new version of MobileNet: MobileNet-v5-300, which has been added to the new version of- `timm`released today.- Features 300M parameters.
- Supports resolutions of `256x256`,`512x512`, and`768x768`.
- Achieves 60 FPS on Google Pixel, outperforming ViT Giant while using 3x fewer parameters.
 
- **Audio Encoder:**- Based on the Universal Speech Model (USM).
- Processes audio in `160ms`chunks.
- Enables speech-to-text and translation functionalities (e.g., English to Spanish/French).
 
- **Gemma 3n Architecture and Language Model.**The architecture itself has been added to the new version of- `transformers`released today. This implementation branches out to- `timm`for image encoding, so there’s a single reference implementation of the MobileNet architecture.

- **MatFormer Architecture:**- A nested transformer design, similar to Matryoshka embeddings, allows for various subsets of layers to be extracted as if they were individual models.
- E2B and E4B were trained together, configuring E2B as a sub-model of E4B.
- Users can “mix and match” layers, depending on their hardware characteristics and memory budget.
 
- **Per-Layer Embeddings (PLE):**Reduces accelerator memory usage by offloading embeddings to the CPU. This is the reason why the E2B model, while having 5B real parameters, takes about as much GPU memory as if it were a 2B parameter model.
- **KV Cache Sharing:**Accelerates long-context processing for audio and video, achieving 2x faster prefill compared to Gemma 3 4B.

- **LMArena Score:**E4B is the first sub-10B model to achieve a score of 1300+.
- **MMLU Scores:**Gemma 3n shows competitive performance across various sizes (E4B, E2B, and several Mix-n-Match configurations).
- **Multilingual Support:**Supports 140 languages for text and 35 languages for multimodal interactions.

![GIF of Hugging Face Space for Gemma 3n](https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/blog/gemma3n/gemma3n.gif)


The easiest way to vibe check the model is with the dedicated Hugging Face Space for the model. You can try out different prompts, with different modalities, here.

Install the latest version of timm (for the vision encoder) and transformers to run inference, or if you want to fine tune it.

```
pip install -U -q timm
pip install -U -q transformers
```
The easiest way to start using Gemma 3n is by using the pipeline abstraction in transformers:

```
import torch
from transformers import pipeline
pipe = pipeline(
   "image-text-to-text",
   model="google/gemma-3n-E4B-it", # "google/gemma-3n-E4B-it"
   device="cuda",
   torch_dtype=torch.bfloat16
)
messages = [
   {
       "role": "user",
       "content": [
           {"type": "image", "url": "https://huggingface.co/datasets/ariG23498/demo-data/resolve/main/airplane.jpg"},
           {"type": "text", "text": "Describe this image"}
       ]
   }
]
output = pipe(text=messages, max_new_tokens=32)
print(output[0]["generated_text"][-1]["content"])
```
Output:

```
The image shows a futuristic, sleek aircraft soaring through the sky. It's designed with a distinctive, almost alien aesthetic, featuring a wide body and large
```
Initialize the model and the processor from the Hub, and write the `model_generation` function that takes care of processing the prompts and running the inference on the model.

```
from transformers import AutoProcessor, AutoModelForImageTextToText
import torch
model_id = "google/gemma-3n-e4b-it" # google/gemma-3n-e2b-it
processor = AutoProcessor.from_pretrained(model_id)
model = AutoModelForImageTextToText.from_pretrained(model_id).to(device)
def model_generation(model, messages):
    inputs = processor.apply_chat_template(
        messages,
        add_generation_prompt=True,
        tokenize=True,
        return_dict=True,
        return_tensors="pt",
    )
    input_len = inputs["input_ids"].shape[-1]
    inputs = inputs.to(model.device, dtype=model.dtype)
    with torch.inference_mode():
        generation = model.generate(**inputs, max_new_tokens=32, disable_compile=False)
        generation = generation[:, input_len:]
    decoded = processor.batch_decode(generation, skip_special_tokens=True)
    print(decoded[0])
```
Since the model supports all modalities as inputs, here's a brief code explanation of how you can use them via transformers.

```
# Text Only
messages = [
    {
        "role": "user",
        "content": [
            {"type": "text", "text": "What is the capital of France?"}
        ]
    }
]
model_generation(model, messages)
```
Output:

```
The capital of France is **Paris**. 
```
```
# Interleaved with Audio
messages = [
    {
        "role": "user",
        "content": [
            {"type": "text", "text": "Transcribe the following speech segment in English:"},
            {"type": "audio", "audio": "https://huggingface.co/datasets/ariG23498/demo-data/resolve/main/speech.wav"},
        ]
    }
]
model_generation(model, messages)
```
Output:

```
Send a text to Mike. I'll be home late tomorrow.
```
Support for videos is done as a collection of frames of images

```
# Interleaved with Image
messages = [
    {
        "role": "user",
        "content": [
            {"type": "image", "image": "https://huggingface.co/datasets/ariG23498/demo-data/resolve/main/airplane.jpg"},
            {"type": "text", "text": "Describe this image."}
        ]
    }
]
model_generation(model, messages)
```
Output:

```
The image shows a futuristic, sleek, white airplane against a backdrop of a clear blue sky transitioning into a cloudy, hazy landscape below. The airplane is tilted at
```
Gemma 3n comes with day 0 support for MLX across all 3 modalities. Make sure to upgrade your mlx-vlm installation.

```
pip install -u mlx-vlm
```
Get started with vision:

```
python -m mlx_vlm.generate --model google/gemma-3n-E4B-it --max-tokens 100 --temperature 0.5 --prompt "Describe this image in detail." --image https://huggingface.co/datasets/ariG23498/demo-data/resolve/main/airplane.jpg
```
And audio:

```
python -m mlx_vlm.generate --model google/gemma-3n-E4B-it --max-tokens 100 --temperature 0.0 --prompt "Transcribe the following speech segment in English:" --audio https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/blog/audio-samples/jfk.wav
```
In addition to MLX, Gemma 3n (text only) works out of the box with llama.cpp. Make sure to install llama.cpp/ Ollama from source.

Check out the Installation instruction for llama.cpp here: [https://github.com/ggml-org/llama.cpp/blob/master/docs/install.md](https://github.com/ggml-org/llama.cpp/blob/master/docs/install.md)

You can run it as:

```
llama-server -hf ggml-org/gemma-3n-E4B-it-GGUF:Q8_0
```
Finally, we are also releasing ONNX weights for the [gemma-3n-E2B-it](https://huggingface.co/onnx-community/gemma-3n-E2B-it-ONNX) model variant, enabling flexible deployment across diverse runtimes and platforms. For JavaScript developers, Gemma3n has been integrated into [Transformers.js](https://github.com/huggingface/transformers.js) and is available as of version [3.6.0](https://github.com/huggingface/transformers.js/releases/tag/3.6.0).

For more information on how to run the model with these libraries, check out the usage section in the [model card](https://huggingface.co/onnx-community/gemma-3n-E2B-it-ONNX#usage).

Given the size of the model, it’s pretty convenient to fine-tune it for specific downstream tasks across modalities. To make it easier for you to fine-tune the model, we’ve created a simple notebook that allows you to experiment on a free [Google Colab](https://colab.research.google.com/github/huggingface/huggingface-gemma-recipes/blob/main/notebooks/fine_tune_gemma3n_on_t4.ipynb)!

We also provide a dedicated [notebook for fine-tuning on audio tasks](https://github.com/huggingface/huggingface-gemma-recipes/blob/main/notebooks/fine_tune_gemma3n_on_audio.ipynb), so you can easily adapt the model to your speech datasets and benchmarks!

With this release, we also introduce the [Hugging Face Gemma Recipes](https://github.com/huggingface/huggingface-gemma-recipes) repository. One will find `notebooks` and `scripts` to run the models and fine tune them.

We would love for you to use the Gemma family of models and add more recipes to it! Feel free to open Issues and create Pull Requests to the repository.

We are always excited to host Google and their Gemma family of models. We hope the community will get together and make the most of these models. Multimodal, small sized, and highly capable, make a great model release!

If you want to discuss the models in more detail, go ahead and start a discussion right below this blog post. We will be more than happy to help!

A huge thanks to Arthur, Cyril, Raushan, Lysandre, and everyone at Hugging Face who took care of the integration and made it available to the community!

 Image-Text-to-Text •  Updated   •  226  •  37 

 Viewer • Updated  •  1 •  20   

⚡

 143

Chat with an AI that understands text, images, audio, and video

More Articles from our Blog

vlmvisionllm

  Hot
- +3

 262

 May 21, 2025 vlmvisionmultimodal

  Hot
- +1

 614

 May 12, 2025 Sensational release!

Are the MobileNet-v5 weights coming to [https://huggingface.co/timm](https://huggingface.co/timm)? 

Are there any results on the performance of this model (the vision encoder only) to inspect?

Thank you all for the efforts.

That was a great read, for anyone wanting a deeper understanding of the architecture, read [https://huggingface.co/blog/rishiraj/matformer-in-gemma-3n](https://huggingface.co/blog/rishiraj/matformer-in-gemma-3n)

Thanks for day 0 MLX support 🙏

•

 Thank you so much for this release!

In the article it is stated that the model "Achieves 60 FPS on Google Pixel" so images as input. The model on Google Pixel runs on a  Google Tensor G4 chip if I am not mistaken. To run the model on a Qualcomm chip (ex: QCS8550), my understanding is that we should use the llama.cpp library which doesn't seem to provide ViT encoder (in the article we can read "llama.cpp (text inputs)"). Is my understanding correct or maybe the best on Qualcomm would be to use the Onnxruntime version? Basically my question is what is the best way to use Gemma on Qualcomm devices for Multimodal support?

Thanks.

Hi, I was running the colab notebook provided in this blog, I am getting this error:

```
/tmp/ipython-input-1538314790.py in <cell line: 0>()
----> 1 trainer = SFTTrainer(
      2     model=model,
      3     args=training_args,
      4     data_collator=collate_fn,
      5     train_dataset=dataset["train"],
/usr/local/lib/python3.12/dist-packages/trl/trainer/sft_trainer.py in __init__(self, model, args, data_collator, train_dataset, eval_dataset, processing_class, compute_loss_func, compute_metrics, callbacks, optimizers, optimizer_cls_and_kwargs, preprocess_logits_for_metrics, peft_config, formatting_func)
    807         self._is_vision_dataset = "image" in dataset_sample or "images" in dataset_sample
    808         if self._is_vision_dataset and not self._is_vlm:
--> 809             raise ValueError(
    810                 "The dataset appears to be vision-related (contains 'image' or 'images' keys), but the provided "
    811                 "model does not seem to be a vision-language model. Please check your model and dataset."
ValueError: The dataset appears to be vision-related (contains 'image' or 'images' keys), but the provided model does not seem to be a vision-language model. Please check your model and dataset.
```
