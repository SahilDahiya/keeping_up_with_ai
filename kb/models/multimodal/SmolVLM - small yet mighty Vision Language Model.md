---
title: SmolVLM - small yet mighty Vision Language Model
kind: blog
topic: models
subtopic: multimodal
secondary_topics:
- infra-platform/edge
summary: 'SmolVLM is a 2B VLM tuned for memory footprint: SigLIP vision encoder with
  aggressive pixel-shuffle visual-token compression (9x fewer tokens than Qwen2-VL),
  trained on the Cauldron and Docmatix, using ~5GB of GPU RAM at inference versus
  tens of GB for peers.'
triage: null
skip_reason: null
source: huggingface
url: https://huggingface.co/blog/smolvlm
author: Andres Marafioti; Merve; Miquel Farré; Elie Bakouch; Pedro Cuenca
published: '2024-11-26'
fetched: '2026-07-14T22:09:31Z'
classifier: claude
taxonomy_rev: 1
words: 2188
content_sha256: 5b4dbd2bc19b1166710f72a227d0eae8bc9abcc6665e63c45404ad86c13559dd
---

# SmolVLM - small yet mighty Vision Language Model

Image-Text-to-Text •  2B • Updated   •  2.99k  •  90  

#### HuggingFaceTB/SmolVLM-Base

![](https://cdn-avatars.huggingface.co/v1/production/uploads/651e96991b97c9f33d26bde6/e4VK7uW5sTeCYupD0s_ob.png) 

 Published
					November 26, 2024 

  Upvote 

 422

This blog post introduces SmolVLM, a 2B VLM, SOTA for its memory footprint. SmolVLM is small, fast, memory-efficient, and fully open-source. All model checkpoints, VLM datasets, training recipes and tools are released under the Apache 2.0 license.

This year has seen a boom in multimodal AI with many large vision language models released. The trends were to initially scale up compute, later scale up the data diversity by generating synthetic data with large models, and, recently, scale down to make these models more efficient. Small open models allow local deployment to browser or edge devices, cut inference costs, and enable user customization. Some notable examples of these models include PaliGemma 3B, moondream2, and Qwen2VL.

In this blog post, we introduce [SmolVLM](https://huggingface.co/HuggingFaceTB/SmolVLM-Instruct), a new family of 2B small vision language models that can be used commercially and deployed to smaller local setups, with completely open training pipelines. 

We release three models: [SmolVLM-Base](https://huggingface.co/HuggingFaceTB/SmolVLM-Base), which can be used for downstream fine-tuning, [SmolVLM-Synthetic](https://huggingface.co/HuggingFaceTB/SmolVLM-Synthetic), the fine-tuned variant on synthetic data, and [SmolVLM Instruct](https://huggingface.co/HuggingFaceTB/SmolVLM-Instruct), the fine-tuned instruction variant, which can be used out of the box for interactive end-user applications. 

This release comes with open-source models integrated into transformers, [a demo built on SmolVLM Instruct](https://huggingface.co/spaces/HuggingFaceTB/SmolVLM), and a supervised fine-tuning script. We have used the datasets previously used for Idefics3: [the Cauldron](https://huggingface.co/datasets/HuggingFaceM4/the_cauldron) and [Docmatix](https://huggingface.co/datasets/HuggingFaceM4/Docmatix), which are also fully open-source.

- [TLDR](https://huggingface.co#TLDR)
- [What is SmolVLM?](https://huggingface.co#what-is-smolvlm)
- [Performance](https://huggingface.co#performance)
- [Use SmolVLM with Transformers](https://huggingface.co#use-smolvlm-with-transformers)
- [Training Details](https://huggingface.co#training-details)
- [Fine-Tuning](https://huggingface.co#fine-tuning)
- [Citation information](https://huggingface.co#citation-information)
- [Wrapping up](https://huggingface.co#wrapping-up)

For SmolVLM, we closely followed the architecture from Idefics3, to the point that we use the same implementation in transformers. There are, however a few key differences:

- We replaced Llama 3.1 8B with SmolLM2 1.7B as the language backbone.
- We more aggressively compress the patched visual information by reducing the information 9x using the pixel shuffle strategy, compared to 4x with idefics3.
- We use patches of 384*384, instead of 364x364, because 384 is divisible by 3, which is necessary for our pixel shuffle strategy to work.
- For this, we change the vision backbone to use shape-optimized SigLIP with patches of 384x384 pixels and inner patches of 14x14.

We present benchmarks for the tasks we mention in training details.

| Model | MMMU (val) | MathVista (testmini) | MMStar (val) | DocVQA (test) | TextVQA (val) | Min GPU RAM required (GB) | 
|---|---|---|---|---|---|---|
| SmolVLM | 38.8 | 44.6 | 42.1 | 81.6 | 72.7 | 5.02 | 
| Qwen2-VL 2B | 41.1 | 47.8 | 47.5 | 90.1 | 79.7 | 13.70 | 
| InternVL2 2B | 34.3 | 46.3 | 49.8 | 86.9 | 73.4 | 10.52 | 
| PaliGemma 3B 448px | 34.9 | 28.7 | 48.3 | 32.2 | 56.0 | 6.72 | 
| moondream2 | 32.4 | 24.3 | 40.3 | 70.5 | 65.2 | 3.87 | 
| MiniCPM-V-2 | 38.2 | 39.8 | 39.1 | 71.9 | 74.1 | 7.88 | 
| MM1.5 1B | 35.8 | 37.2 | 0.0 | 81.0 | 72.5 | NaN | 

SmolVLM provides the best memory usage among the existing suite of vision language models in transformers. This allows it to run efficiently on-device, such as a laptop! You can see above the GPU memory usage in GBs for each model, running inference with one or two input images, and using the same images and text prompts in all tests. SmolVLM's efficiency in image encoding is built into the model. SmolVLM encodes each 384x384 image patch to 81 tokens. This results in SmolVLM encoding our test prompt and a single image in 1.2k tokens, whereas Qwen2-VL uses 16k tokens. This also explains why the memory consumption increases so much for 2 images with Qwen and InternVL. In contrast, the increase is much more moderate for SmolVLM and PaliGemma, which use a similar approach.

SmolVLM's tiny memory footprint also implies that it requires far fewer computations to prefill the model and generate. Compared to Qwen2-VL, the prefill throughput is 3.3 to 4.5 times faster, and the generation throughput is 7.5 to 16 times faster.

Given SmolVLM's long context and the possibility of tweaking the internal frame resizing of the model, we explored its suitability as an accessible option for basic video analysis tasks, particularly when computational resources are limited.

In our evaluation of SmolVLM's video understanding capabilities, we implemented a straightforward [video processing pipeline code](https://github.com/huggingface/smollm/blob/7dfcd81c046a946031291c11451e9398609a0aeb/tools/smolvlm_local_inference/SmolVLM_video_inference.py), extracting up to 50 evenly sampled frames from each video while avoiding internal frame resizing.
This simple approach yielded surprisingly competitive results on the CinePile benchmark, with a score of 27.14%, a performance that positions the model between InternVL2 (2B) and Video LlaVa (7B).

The quantitative results align with our qualitative testing, looking at an example from the FineVideo dataset:

```
Question: what is shown in the close-up? 
Assistant: In the close-up, there are bottles of Heinz tomato ketchup,
  honey, soy sauce, and garlic on a kitchen counter.
Question: describe what is happening in the video. 
Assistant: The video shows a man cooking in a kitchen.
  He is wearing a black shirt and a black apron.
  He is standing in front of a counter and is holding a bottle of Heinz tomato ketchup,
  a bottle of honey, soy sauce, and a bowl of minced garlic
```
While in the second question, we see some temporal understanding limitations (the cook points to one ingredient after the other rather than pointing/holding all of them at the same time) SmolVLM demonstrated great scene understanding and object recognition capabilities.

We integrated SmolVLM with [VLMEvalKit](https://github.com/open-compass/VLMEvalKit) to facilitate easy evaluation across additional benchmarks. 

By running the following command, you can evaluate SmolVLM or your fine-tuned SmolVLM model.

```
python run.py --data <benchmarks> --model SmolVLM --work-dir <output_directory>
```
For example, to evaluate on MMMU dev validation set and MathVista mini and store the results in a folder called smol.

```
python run.py --data MMMU_DEV_VAL MathVista_MINI --model SmolVLM --work-dir smol
```
You can easily load SmolVLM using the `Auto` classes in transformers. Under the hood, the model and processor are mapped to the same implementations used for Idefics3. 

```
from transformers import AutoProcessor, AutoModelForVision2Seq
import torch
DEVICE = "cuda" if torch.cuda.is_available() else "cpu"
processor = AutoProcessor.from_pretrained("HuggingFaceTB/SmolVLM-Instruct")
model = AutoModelForVision2Seq.from_pretrained("HuggingFaceTB/SmolVLM-Instruct",
                                                torch_dtype=torch.bfloat16,
                                                _attn_implementation="flash_attention_2" if DEVICE == "cuda" else "eager").to(DEVICE)
```
Image and text can be interleaved arbitrarily, and you can pass in multiple images. Here’s how you can use the chat template and pass in the formatted input to the processor.

```
from PIL import Image
from transformers.image_utils import load_image
# Load images
image1 = load_image("https://huggingface.co/spaces/HuggingFaceTB/SmolVLM/resolve/main/example_images/rococo.jpg")
image2 = load_image("https://huggingface.co/spaces/HuggingFaceTB/SmolVLM/resolve/main/example_images/rococo_1.jpg")
# Create input messages
messages = [
    {
        "role": "user",
        "content": [
            {"type": "image"},
            {"type": "image"},
            {"type": "text", "text": "Can you describe the two images?"}
        ]
    },
]
# Prepare inputs
prompt = processor.apply_chat_template(messages, add_generation_prompt=True)
inputs = processor(text=prompt, images=[image1, image2], return_tensors="pt")
inputs = inputs.to(DEVICE)
```
Start generating with preprocessed input and decode the generated output.

```
# Generate outputs
generated_ids = model.generate(**inputs, max_new_tokens=500)
generated_texts = processor.batch_decode(
    generated_ids,
    skip_special_tokens=True,
)
print(generated_texts[0])
```
First, we had to train SmolLM2 to extend it context, but we will discuss that in the next subsection. Once we had a long context SmolLM2, we trained SmolVLM using the same data that we used for Idefics3. Mainly, we used The Cauldron and Docmatix. The full list of datasets we used [can be consulted here](https://huggingface.co/HuggingFaceTB/SmolVLM-Instruct/blob/main/smolvlm-data.pdf). 

SmolLM2’s pre-training context window is insufficient for VLMs. Images are encoded into many tokens, and we wanted to support multiple images. To address this, we extended it to 16k tokens by increasing the RoPE base value from 10k to 273k, following the guidelines in [“Scaling Laws of RoPE-based Extrapolation”](https://arxiv.org/abs/2310.05209). We fine-tuned the model on a mixture of long- and short-context datasets.
For long-context datasets, we used the “books” subset of Dolma (primarily Project Gutenberg) and code documents with 8k+ tokens from The Stack, each contributing 20% to the final mixture. For short-context datasets, we streamlined the original SmolLM2 pre-training mix to include 20% FineWeb-Edu, 20% DCLM, and 20% from our math dataset (to be released soon). The math dataset was upsampled to mitigate a performance drop observed on GSM8k during the context extension process.
All experiments were implemented using the [EasyContext repository](https://github.com/jzhang38/EasyContext).

For our training run, we saved checkpoints every 25 optimization steps, allowing us to evaluate and potentially recover the model's state at different points in training. This practice is crucial for identifying the optimal model version, as training longer doesn't always guarantee better performance. We evaluated the performance across multiple vision-language benchmarks, each weighted according to their importance. The core benchmarks included the following:

- General multimodal understanding (MMMU and MMStar) which are the most comprehensive benchmark.
- Document and text-based visual question answering (DocVQA and TextVQA)
- Mathematical Reasoning (MathVista)
- Diagram understanding (AI2D)

To select the optimal checkpoint, we created a single metric by combining these benchmarks with different manually assigned weights to reflect their relative importance in assessing the model's capabilities. We used this single metric to select the best checkpoint. Generally, the models tended to do great on most benchmarks with more training, but their relative performance on DocVQA would decrease considerably.

You can fine-tune SmolVLM using transformers and apply alignment techniques using TRL 🚀

We provide a [notebook](https://github.com/huggingface/smollm/blob/main/vision/finetuning/Smol_VLM_FT.ipynb) to fine-tune it on the VQAv2 dataset, optionally using  LoRA, QLoRA or full fine-tuning. In the notebook, you can find some tricks to save up even more memory and have a larger batch size to fit SmolVLM inside consumer GPUs, like L4, for training. With batch sizes of 4, 8-bit loading with QLoRA and gradient checkpointing we can fine-tune in L4, and it consumes around ~16 GBs of VRAM. This makes it possible to fine-tune your SmolVLM using Colab! You can play around with the parameters to get a nice point in training duration-memory trade-off. 

SmolVLM also comes with TRL integration so you can apply Direct Preference Optimization (DPO) easily through the CLI. Get started by running `pip install trl accelerate peft` and then run the following command to fine-tune on [RLAIF-V](https://huggingface.co/datasets/HuggingFaceH4/rlaif-v_formatted) dataset: 

```
accelerate launch \
  --config_file examples/accelerate_configs/multi_gpu.yaml examples/scripts/dpo_vlm.py  \
  --dataset_name HuggingFaceH4/rlaif-v_formatted \
  --model_name_or_path HuggingFaceTB/SmolVLM-Instruct \
  --per_device_train_batch_size 8 \
  --gradient_accumulation_steps 32 \
  --dataset_num_proc 32 \
  --output_dir dpo_smolvlm_rlaif-v \
  --bf16 --torch_dtype bfloat16 \
  --use_peft --lora_target_modules=all-linear 
```
The resulting LoRA adapter weights are [SmolVLM-Instruct-DPO](https://huggingface.co/HuggingFaceTB/SmolVLM-Instruct-DPO). A detailed tutorial on preference tuning vision-based LLM can be found here: [dpo_vlm](https://huggingface.co/blog/dpo_vlm).

You can cite us in the following way:

```
@article{marafioti2025smolvlm,
  title={SmolVLM: Redefining small and efficient multimodal models}, 
  author={Andrés Marafioti and Orr Zohar and Miquel Farré and Merve Noyan and Elie Bakouch and Pedro Cuenca and Cyril Zakka and Loubna Ben Allal and Anton Lozhkov and Nouamane Tazi and Vaibhav Srivastav and Joshua Lochner and Hugo Larcher and Mathieu Morlon and Lewis Tunstall and Leandro von Werra and Thomas Wolf},
  journal={arXiv preprint arXiv:2504.05299},
  year={2025}
}
```
We introduced SmolVLM, a fully open, small, and mighty VLM for the community! We also provide tools for the community to use and customize it. We are looking forward to seeing what you will create with SmolVLM.

Below are some resources if you would like to read more about all things related to SmolVLM.

- Start playing with SmolVLM using [this demo](https://huggingface.co/spaces/HuggingFaceTB/SmolVLM).
- Learn how to fine-tune SmolVLM on VQAv2 using [this notebook](https://github.com/huggingface/smollm/blob/main/vision/finetuning/Smol_VLM_FT.ipynb)
- Learn more about [vision language models](https://huggingface.co/blog/vlms)

 Image-Text-to-Text •  2B • Updated   •  2.99k  •  90 

 Image-Text-to-Text •  2B • Updated   •  22.9k  •  589 

 Image-Text-to-Text •  Updated   •  22  •  22 

 Image-Text-to-Text •  2B • Updated   •  66  •  12 

 Viewer • Updated  •  83.1k •  625  •  17 

 Viewer • Updated  •  2.55M •  12.4k  •  309 

 Viewer • Updated  •  1.88M •  134k  •  548 

📊

 143

Answer questions about images with AI chat

More Articles from our Blog

vlmmultimodalvideo

  Hot
- +3

 344

 February 20, 2025 multimodalon-devicellm

 
- +3

 192

 September 25, 2024 Great work ! :)

Small nit for the example there is a typo on the link for second image it should be:

image2 = load_image("[https://huggingface.co/spaces/HuggingFaceTB/SmolVLM/resolve/main/example_images/rococo_1.jpg](https://huggingface.co/spaces/HuggingFaceTB/SmolVLM/resolve/main/example_images/rococo_1.jpg)")

You are right [@ridha](https://huggingface.co/ridha) ! Would you like to open a PR so that the fix is attributed to you? You can do it by clicking the "Update on GitHub" button just below this post's title. If you don't have time that's perfectly ok, we'll get to it in a day or so :)

Thanks a lot for writing!

Hi, wanna ask how to using the same arch, but try training from scratch with another langual model? Is that supported?

•

 [https://github.com/huggingface/smollm/blob/main/finetuning/Smol_VLM_FT.ipynb](https://github.com/huggingface/smollm/blob/main/finetuning/Smol_VLM_FT.ipynb)

is not working,

[https://github.com/huggingface/smollm/blob/main/vision/finetuning/Smol_VLM_FT.ipynb](https://github.com/huggingface/smollm/blob/main/vision/finetuning/Smol_VLM_FT.ipynb)

seems to be the correct one.

Great to see compact vision models getting practical. I built a privacy-first, cross-platform web UI that runs SmolVLM2-2.2B-Instruct (vision) alongside SmolLM3-3B (text). It auto-detects CUDA/MPS/CPU, pulls models on first run, and serves a clean Gradio interface.

Vision: describe images, visual Q&A, quick OCR

Text: code generation, explanation, summarization, multilingual prompts

Local only: no API keys or cloud services

I’m actively collecting feedback: ideal image sizes, better defaults for generation params, and presets that make visual tasks smoother. If you’re testing SmolVLM* locally, I’d love your notes.

Repo: [https://github.com/mikecastrodemaria/SmolLM3-M2-Interface-Multimodale](https://github.com/mikecastrodemaria/SmolLM3-M2-Interface-Multimodale)

Thanks for any pointers, issues, or PRs!
