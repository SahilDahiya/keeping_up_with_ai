---
title: Welcome PaliGemma 2 – New vision language models by Google
kind: blog
topic: models
subtopic: multimodal
secondary_topics: []
summary: PaliGemma 2 pairs a SigLIP image encoder with Gemma 2 LLMs at 3B/10B/28B
  and 224/448/896px input resolutions, designed as pre-trained checkpoints intended
  to be fine-tuned per task rather than used zero-shot. Covers the resolution-vs-cost
  trade-off, DOCCI long-caption fine-tunes, and the transformers fine-tuning scripts/VQAv2
  demo.
triage: null
skip_reason: null
source: huggingface
url: https://huggingface.co/blog/paligemma2
author: Merve; Andreas P Steiner; Pedro Cuenca; Aritra Roy Gosthipaty
published: '2024-12-05'
fetched: '2026-07-14T22:11:34Z'
classifier: claude
taxonomy_rev: 1
words: 1837
content_sha256: cb8d2f49e2694081225ba23ea43275165e52007a8772a6871c5b647b2e6ee1dd
---

# Welcome PaliGemma 2 – New vision language models by Google

Image-Text-to-Text •  28B • Updated   •  516  •  52  

#### google/paligemma2-28b-pt-896

![](https://cdn-avatars.huggingface.co/v1/production/uploads/5dd96eb166059660ed1ee413/WtA3YYitedOr9n02eHfJe.png) 

 Published
					December 5, 2024 

  Upvote 

 167

andsteing    

PaliGemma 2 comes with new pre-trained (pt) models, in sizes of `3B`, `10B`, and `28B` parameters. All of them support various input resolutions: `224x224`, `448x448`, and `896x896`. These combinations provide a lot of flexibility for different use cases, so practitioners can choose the balance they need in the quality / efficiency space. In contrast, the previous PaliGemma was only available in the 3B variant.

The pre-trained models have been designed for easy fine-tuning to downstream tasks. The first PaliGemma was widely adopted by the community for multiple purposes. With the increased flexibility from the additional variants, combined with better pre-trained quality, we can’t wait to see what the community can do this time.

As an example, Google is also releasing some fine-tuned variants on the [DOCCI](https://huggingface.co/datasets/google/docci) dataset, demonstrating versatile and robust captioning capabilities that are long, nuanced and detailed. The fine-tuned DOCCI models are available for the 3B and 10B variants, and support input resolution of 448x448.

This release includes all the open model repositories, transformers integration, fine-tuning scripts, and a demo of a model we fine-tuned ourselves for visual question answering on the [VQAv2 dataset](https://huggingface.co/datasets/HuggingFaceM4/VQAv2).

PaliGemma 2 is a new iteration of the [PaliGemma vision language model](https://huggingface.co/blog/paligemma) released by Google in May. PaliGemma 2 connects the powerful SigLIP image encoder with the [Gemma 2](https://huggingface.co/blog/gemma2) language model.

![PaliGemma2 Architecture](https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/blog/paligemma/paligemma2_arch.png)


The new models are based on the Gemma 2 2B, 9B, and 27B language models, resulting in the corresponding 3B, 10B, and 28B PaliGemma 2 variants, whose names take into account the additional parameters of the (compact) image encoder. As mentioned above, they support three different resolutions, providing great flexibility for fine-tuning to downstream tasks.

PaliGemma 2 is distributed under the Gemma license, which allows for redistribution, commercial use, fine-tuning and creation of model derivatives.

This release comes with the following checkpoints in `bfloat16` precision:

- 9 pre-trained models: 3B, 10B, and 28B with resolutions of - `224x224`,- `448x448`, and- `896x896`.
- 2 models fine-tuned on DOCCI: Two models fine-tuned on the - [DOCCI](https://huggingface.co/datasets/google/docci)dataset (image-text caption pairs), supporting the 3B and 10B PaliGemma 2 variants and input resolution of- `448x448`.

As seen with the previous PaliGemma release, the pre-trained (pt) models work great for further fine-tuning on downstream tasks.

The pt models are pre-trained on the following data mixture. The diversity of the pre-training dataset allows fine-tuning on downstream tasks in similar domains to be carried out using comparatively fewer examples.

- **WebLI**: A web-scale multilingual image-text dataset built from the public web. A wide range of WebLI splits is used to acquire versatile model capabilities, such as visual semantic understanding, object localization, visually-situated text understanding, and multilinguality.
- **CC3M-35L:**Curated English image-alt_text pairs from webpages (- [Sharma et al., 2018](https://aclanthology.org/P18-1238/)). To label this dataset, the authors used- [Google Cloud Translation API](https://cloud.google.com/translate)to translate into 34 additional languages.
- **Visual Question Generation with Question Answering Validation (VQ2A):**An improved dataset for question answering. The dataset is translated into the same additional 34 languages, using the Google Cloud Translation API.
- **OpenImages:**Detection and object-aware questions and answers (Piergiovanni et al. 2022) generated by handcrafted rules on the- [OpenImages dataset](https://storage.googleapis.com/openimages/web/factsfigures_v7.html).
- **WIT**: Images and texts collected from Wikipedia (Srinivasan et al., 2021).

The PaliGemma 2 team internally fine-tuned the PT models on a wide variety of visual-language understanding tasks, and they provide benchmarks of these fine-tuned models [in the model card](https://huggingface.co/google/paligemma2-28b-pt-896#paligemma-2-results-by-model-resolution-and-size) and [the technical report](https://huggingface.co/papers/2412.03555).

PaliGemma 2 fine-tuned on the DOCCI dataset, can accomplish a wide range of captioning tasks, including text rendering, capturing spatial relations, and including world knowledge in captions.

You can find below the performance of the DOCCI fine-tuned PaliGemma 2 checkpoints, compared with other models (taken from Table 6 in [the technical report](https://huggingface.co/papers/2412.03555)).

| #par | #char | #sent | NES↓ | |
|---|---|---|---|---|
| MiniGPT-4 | 7B | 484 | 5.6 | 52.3 | 
| mPLUG-Owl2 | 8B | 459 | 4.4 | 48.4 | 
| InstructBLIP | 7B | 510 | 4.0 | 42.6 | 
| LLaVA-1.5 | 7B | 395 | 4.2 | 40.6 | 
| VILA | 7B | 871 | 8.6 | 28.6 | 
| PaliGemma | 3B | 535 | 8.9 | 34.3 | 
| PaLI-5B | 5B | 1065 | 11.3 | 32.9 | 
| PaliGemma 2 | 3B | 529 | 7.7 | 28.4 | 
| PaliGemma 2 | 10B | 521 | 7.5 | 20.3 | 

- **#char**: Average number of characters in the generated caption.
- **#sent**: Average number of sentences.
- **NES**: Non entailment sentences (lower is better) that measure factual inaccuracies.

Below you can find some model outputs for the DOCCI checkpoint that showcase the versatility of the model.

| Input Image | Caption | 
|---|---|
| ![](https://huggingface.co/spaces/big-vision/paligemma-hf/resolve/main/examples/howto.jpg) | A line graph shows the top-1 accuracy of the ImageNet model after fine-tuning. The graph shows four lines that are colored blue, orange, green, and black. The blue line is the lowest of the four lines, and it is | 
| ![](https://huggingface.co/spaces/big-vision/paligemma-hf/resolve/main/examples/password.jpg) | A close up view of a white piece of paper with black text on it. The paper is curved in the middle. The text on the paper is in a typewriter font. The top of the paper has the words "Ashley Hotel West Coast" on it. Underneath that is "WiFi Internet Service". Underneath that is "Username: fqpp". Underneath that is "Password: aaeu | 
| ![](https://huggingface.co/spaces/big-vision/paligemma-hf/resolve/main/examples/bowie.jpg) | A mural of David Bowie's Ziggy Stardust look is painted on a white wall. The mural is of three faces side by side, each with red hair and blue lightning bolts painted over their eyes. The faces have blue eyeshadow, pink blush, and red lips. The face in the middle has a black square window above it with white text that reads "JAM" in blue. A silver car | 
| ![](https://huggingface.co/spaces/big-vision/paligemma-hf/resolve/main/examples/cups.jpg) | A top-down view of a white marble counter with four coffee mugs on it. There are two gray ones on the left, and one is white on the bottom left. The one on the right is gray. There is a metal wire fruit basket on a wood stand in the top right corner with oranges in it. There is a clear glass pitcher with water in it on the left, and part | 
| ![](https://huggingface.co/spaces/big-vision/paligemma-hf/resolve/main/examples/ulges.jpg) | A close up view of a white book with a blue strip at the bottom of it. The top half of the book is white. Black text is printed on the white portion of the book. The text reads "Visual Concept Learning from User-tagged Web Video". Underneath the black text is a white box with five small images inside of it. The image on the far left is of a person standing in a field of grass. The image to the right of that one is of a blue ocean | 

For demonstration purposes, we in the Hugging Face team fine-tuned [PaliGemma 2 3B with 448x448 resolution](https://huggingface.co/google/paligemma2-3b-pt-448) on a small portion of the [VQAv2 dataset](https://huggingface.co/datasets/merve/vqav2-small). We used LoRA fine-tuning and PEFT, as explained later in the fine-tuning section. The demo below showcases the final result. Feel free to examine the code in [the Space](https://huggingface.co/spaces/merve/paligemma2-vqav2) to see how it works, or clone it to adapt to your own fine-tunes.

You can run inference on the PaliGemma 2 models with 🤗 transformers, using the PaliGemmaForConditionalGeneration and AutoProcessor APIs. Please, make sure you install transformers version 4.47 or later:

```
pip install --upgrade transformers
```
After that, you can run inference like follows. As usual, please make sure to follow the prompt format that was used to train the model for the task you are using:

```
from transformers import AutoProcessor, PaliGemmaForConditionalGeneration
from PIL import Image
import requests
model_id = "google/paligemma2-10b-ft-docci-448"
model = PaliGemmaForConditionalGeneration.from_pretrained(model_id)
model = model.to("cuda")
processor = AutoProcessor.from_pretrained(model_id)
prompt = "<image>caption en"
image_file = "https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/cats.png"
raw_image = Image.open(requests.get(image_file, stream=True).raw).convert("RGB")
inputs = processor(prompt, raw_image, return_tensors="pt").to("cuda")
output = model.generate(**inputs, max_new_tokens=200)
input_len = inputs["input_ids"].shape[-1]
print(processor.decode(output[0][input_len:], skip_special_tokens=True))
# A medium shot of two cats laying on a pile of brown fishing nets. The cat in the foreground is a gray tabby cat with white on its chest and paws. The cat is laying on its side with its head facing the bottom right corner of the image. The cat in the background is laying on its side with its head facing the top left corner of the image. The cat's body is curled up, its head is slightly turned to the right, and its front paws are tucked underneath its body. There is a teal rope hanging from the fishing net in the top right corner of the image.
```
You can also use the transformers `bitsandbytes` integration to load the models with quantization. The following example uses 4-bit `nf4`:

```
from transformers import BitsAndBytesConfig
bnb_config = BitsAndBytesConfig(
    load_in_4bit=True,
    bnb_4bit_quant_type="nf4",
    bnb_4bit_compute_dtype=torch.bfloat16
)
model = PaligemmaForConditionalGeneration.from_pretrained(
    model_id,
    quantization_config=bnb_config,
    device_map={"":0}
)
```
We quickly tested performance degradation in the presence of quantization by evaluating a 3B fine-tuned checkpoint on the [textvqa](https://huggingface.co/datasets/lmms-lab/textvqa) dataset, using 224x224 input images. These are the results we got on the 5,000 entries of the validation set:

- `bfloat16`, no quantization: 60.04% accuracy.
- `8-bit`: 59.78%.
- `4-bit`, using the configuration from the snippet above: 58.72%.

These are very encouraging figures! Of course, quantization is most interesting for the larger checkpoints, we recommend you always measure results on the domains and tasks you’ll be using.

If you have previously fine-tuned PaliGemma, the API to fine-tune PaliGemma 2 is the same, you can use your code out of the box. We provide a [fine-tuning script](https://github.com/merveenoyan/smol-vision/blob/main/paligemma.py) and [a notebook](https://github.com/merveenoyan/smol-vision/blob/main/Fine_tune_PaliGemma.ipynb) for you to fine-tune the model, freeze parts of the model, or apply memory efficient fine-tuning techniques like LoRA or QLoRA.

We have LoRA-fine-tuned a PaliGemma 2 model on half of the VQAv2 validation split for demonstration purposes. This took half an hour on 3 A100s with 80GB VRAM. The model can be found [here](https://huggingface.co/merve/paligemma2-3b-vqav2), and [this is a Gradio demo that showcases it](https://huggingface.co/spaces/merve/paligemma2-vqav2).

The new PaliGemma 2 release is even more exciting than the previous one, with various sizes fitting everyone’s needs and stronger pre-trained models. We are looking forward to seeing what the community will build!

We thank the Google team for releasing this amazing, and open, model family. Big thanks to [Pablo Montalvo](https://huggingface.co/Molbap) for integrating the model to transformers, and to [Lysandre](https://huggingface.co/lysandre), [Raushan](https://huggingface.co/RaushanTurganbay), [Arthur](https://huggingface.co/ArthurZ), [Yieh-Dar](https://huggingface.co/ydshieh) and the rest of the team for reviewing, testing, and merging in no time.

 Image-Text-to-Text •  28B • Updated   •  516  •  52 

 Image-Text-to-Text •  3B • Updated   •  72.8k  •  51 

  Updated   •  40  •  6 

 Updated   •  1.38k  •  50 

 Updated   •  438  •  79 

 Viewer • Updated  •  45.3k •  41.9k  •  24 

 Viewer • Updated  •  21.4k •  2.76k  •  21 

🐨

 48

PaliGemma2 LoRA finetuned on VQAv2

 Paper • 2412.03555 • Published  •  136 

More Articles from our Blog

nlpcommunityresearch

 
- +5

 28

 May 24, 2024 multimodalnlpcommunity

  74

 April 16, 2026 This comment has been hidden        

      This comment has been hidden        

      This comment has been hidden
