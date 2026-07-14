---
title: 'Introducing Idefics2: A Powerful 8B Vision-Language Model for the community'
kind: blog
topic: models
subtopic: multimodal
secondary_topics: []
summary: 'Idefics2-8B vision-language model: native image resolution/aspect-ratio
  handling, a learned-pooling perceiver to cut image tokens to 64 per image, and its
  OBELICS/PDF-heavy training mix, benchmarked against DeepSeek-VL and LLaVA-NeXT.'
triage: null
skip_reason: null
source: huggingface
url: https://huggingface.co/blog/idefics2
author: Leo Tronchon; Hugo Laurençon; Victor Sanh
published: '2024-04-15'
fetched: '2026-07-14T22:10:31Z'
classifier: claude
taxonomy_rev: 1
words: 1184
content_sha256: d5fbc4de2471c2802944bcc3e806d6101a7227749ac524033bee71537e6de520
---

# Introducing Idefics2: A Powerful 8B Vision-Language Model for the community

Text Generation •  80B • Updated   •  3.26k  •  188  

#### HuggingFaceM4/idefics-80b-instruct

![](https://cdn-avatars.huggingface.co/v1/production/uploads/1653062669432-60741a2e69a66931a0273f0c.png) 

 Published
					April 15, 2024 

  Upvote 

 191

    ![Idefics-Obelics logo](https://huggingface.co/HuggingFaceM4/idefics-80b/resolve/main/assets/IDEFICS.png) 


Idefics2 improves upon

Idefics2 is also integrated in 🤗 Transformers from the get-go and therefore is straightforward to finetune for many multimodal applications. You can try out the

      ![The Cauldron](https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/blog/idefics2/Idefics2_eval_barchart.png?download=true) 


| weights | per image | (val/test) | (testmini) | (val) | (test) | (test-dev) | (test) | ||
|---|---|---|---|---|---|---|---|---|---|
| [DeepSeek-VL](https://huggingface.co/deepseek-ai/deepseek-vl-7b-chat) | ✅ | 7B | 576 | 36.6/- | 36.1 | 64.4 | 73.2 | - | 49.6 | 
| [LLaVa-NeXT-Mistral-7B](https://huggingface.co/liuhaotian/llava-v1.6-mistral-7b) | ✅ | 7B | 2880 | 35.3/- | 37.7 | 65.7 | 68.7 | 82.2 | - | 
| [LLaVa-NeXT-13B](https://huggingface.co/liuhaotian/llava-v1.6-vicuna-13b) | ✅ | 13B | 2880 | 36.2/- | 35.3 | 67.1 | 70.0 | 82.8 | - | 
| [LLaVa-NeXT-34B](https://huggingface.co/liuhaotian/llava-v1.6-34b) | ✅ | 34B | 2880 | 51.1/44.7 | 46.5 | 69.5 | 79.3 | 83.7 | - | 
| MM1-Chat-7B | ❌ | 7B | 720 | 37.0/35.6 | 35.9 | 72.8 | 72.3 | 82.8 | - | 
| MM1-Chat-30B | ❌ | 30B | 720 | 44.7/40.3 | 39.4 | 73.5 | 75.1 | 83.7 | |
| Gemini 1.0 Pro | ❌ | 🤷♂️ | 🤷♂️ | 47.9/- | 45.2 | 74.6 | - | 71.2 | 88.1 | 
| Gemini 1.5 Pro | ❌ | 🤷♂️ | 🤷♂️ | 58.5/- | 52.1 | 73.5 | - | 73.2 | 86.5 | 
| Claude 3 Haiku | ❌ | 🤷♂️ | 🤷♂️ | 50.2/- | 46.4 | - | - | - | 88.8 | 
| [Idefics1 instruct](https://huggingface.co/HuggingFaceM4/idefics-80b-instruct)(32-shots) | ✅ | 80B | - | - | - | 39.3 | - | 68.8 | - | 
| Idefics2(w/o im. split)* | ✅ | 8B | 64 | 43.5/37.9 | 51.6 | 70.4 | 76.8 | 80.8 | 67.3 | 
| Idefics2(w/ im. split)* | ✅ | 8B | 320 | 43.0/37.7 | 51.4 | 73.0 | 76.7 | 81.2 | 74.0 | 

* w/ im. split: Following the strategy from SPHINX and LLaVa-NeXT, we allow for an optional sub-image splitting in 4.

Idefics2 was trained on a mixture of openly available datasets for the pretraining: Interleaved webdocuments (Wikipedia,[OBELICS](https://huggingface.co/datasets/HuggingFaceM4/OBELICS)), image-caption pairs (Public Multimodal Dataset, LAION-COCO), OCR data ([PDFA (en)](https://huggingface.co/datasets/pixparse/pdfa-eng-wds), [IDL](https://huggingface.co/datasets/pixparse/idl-wds) and [Rendered-text](https://huggingface.co/datasets/wendlerc/RenderedText), and image-to-code data ([WebSight](https://huggingface.co/datasets/HuggingFaceM4/WebSight))). 

The [interactive visualization](https://atlas.nomic.ai/map/f2fba2aa-3647-4f49-a0f3-9347daeee499/ee4a84bd-f125-4bcc-a683-1b4e231cb10f) allows exploring the OBELICS dataset. 

Following common practices in the foundation model community, we further train the base model on task-oriented data. However, these data are often in disparate formats, and scattered in various places. Gathering them is a barrier for the community. To address that problem, we are releasing the multimodal instruction fine-tuning dataset we've been cooking: * The Cauldron*, an open compilation of 

      ![The Cauldron](https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/blog/idefics2/The_Cauldron.png?download=true) 


- We manipulate images in their native resolutions (up to 980 x 980) and native aspect ratios by following the NaViT strategy. That circumvents the need to resize images to fixed-size squares as it has been historically done in the computer vision community. Additionally, we follow the strategy from SPHINX and (optionally) allow sub-image splitting and passing images of very large resolution.
- We significantly enhanced OCR abilities by integrating data that requires the model to transcribe text in an image or a document. We also improved abilities in answering questions on charts, figures, and documents with appropriate training data.
- We departed from the Idefics1's architecture (gated cross-attentions) and simplified the integration of visual features into the language backbone. The images are fed to the vision encoder followed by a learned Perceiver pooling and an MLP modality projection. That pooled sequence is then concatenated with the text embeddings to obtain an (interleaved) sequence of image(s) and text(s).

All of these improvements along with better pre-trained backbones yield a significant jump in performance over Idefics1 for a model that is 10x smaller.

    ![Idefics2 Architecture](https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/blog/idefics2/Idefics2_flowchart.png?download=true) 


Idefics2 is available on the Hugging Face Hub and supported in the last `transformers` version. Here is a code sample to try it out:

```
import requests
import torch
from PIL import Image
from transformers import AutoProcessor, AutoModelForVision2Seq
from transformers.image_utils import load_image
DEVICE = "cuda:0"
# Note that passing the image urls (instead of the actual pil images) to the processor is also possible
image1 = load_image("https://cdn.britannica.com/61/93061-050-99147DCE/Statue-of-Liberty-Island-New-York-Bay.jpg")
image2 = load_image("https://cdn.britannica.com/59/94459-050-DBA42467/Skyline-Chicago.jpg")
image3 = load_image("https://cdn.britannica.com/68/170868-050-8DDE8263/Golden-Gate-Bridge-San-Francisco.jpg")
processor = AutoProcessor.from_pretrained("HuggingFaceM4/idefics2-8b")
model = AutoModelForVision2Seq.from_pretrained(
    "HuggingFaceM4/idefics2-8b",
).to(DEVICE)
# Create inputs
messages = [
    {
        "role": "user",
        "content": [
            {"type": "image"},
            {"type": "text", "text": "What do we see in this image?"},
        ]
    },
    {
        "role": "assistant",
        "content": [
            {"type": "text", "text": "In this image, we can see the city of New York, and more specifically the Statue of Liberty."},
        ]
    },
    {
        "role": "user",
        "content": [
            {"type": "image"},
            {"type": "text", "text": "And how about this image?"},
        ]
    },
]
prompt = processor.apply_chat_template(messages, add_generation_prompt=True)
inputs = processor(text=prompt, images=[image1, image2], return_tensors="pt")
inputs = {k: v.to(DEVICE) for k, v in inputs.items()}
# Generate
generated_ids = model.generate(**inputs, max_new_tokens=500)
generated_texts = processor.batch_decode(generated_ids, skip_special_tokens=True)
print(generated_texts)
```
We also provide a fine-tuning [colab](https://colab.research.google.com/drive/1NtcTgRbSBKN7pYD3Vdx1j9m8pt3fhFDB?usp=sharing) which should come in handy for anyone looking to improve Idefics2 on specific use cases.

      ![The Cauldron](https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/blog/idefics2/This_is_fine_example.png?download=true) 


If you wish to deep dive further, here is the compilation of all resources for Idefics2:

- [Idefics2 collection](https://huggingface.co/collections/HuggingFaceM4/idefics2-661d1971b7c50831dd3ce0fe)
- [Idefics2 model with model card](https://huggingface.co/HuggingFaceM4/idefics2-8b)
- [Idefics2-base model with model card](https://huggingface.co/HuggingFaceM4/idefics2-8b-base)
- [Idefics2-chat model with model card](https://huggingface.co/HuggingFaceM4/idefics2-8b-chatty)
- [The Cauldron with its dataset card](https://huggingface.co/datasets/HuggingFaceM4/the_cauldron)
- [OBELICS with its dataset card](https://huggingface.co/datasets/HuggingFaceM4/OBELICS)
- [WebSight with its dataset card](https://huggingface.co/datasets/HuggingFaceM4/WebSight)
- [Idefics2 fine-tuning colab](https://colab.research.google.com/drive/1rm3AGquGEYXfeeizE40bbDtcWh5S4Nlq?usp=sharing)
- [Idefics2-8B model demo (not the chatty model)](https://huggingface.co/spaces/HuggingFaceM4/idefics-8b)
- [Idefics2 demo](https://huggingface.co/spaces/HuggingFaceM4/idefics2_playground)
- [Idefics2 paper](https://arxiv.org/abs/2405.02246)

The model is built on top of two pre-trained models: [Mistral-7B-v0.1](https://huggingface.co/mistralai/Mistral-7B-v0.1) and [siglip-so400m-patch14-384](https://huggingface.co/google/siglip-so400m-patch14-384). Both of them have been released under Apache-2.0 license.
We release Idefics2 weights under an Apache-2.0 license as well.

Thank you to the Google Team and Mistral AI for releasing and making their models available to the open-source AI community!

Special thanks to Chun Te Lee for the barplot, and Merve Noyan for the review and suggestions on the blogpost 🤗

 Text Generation •  80B • Updated   •  3.26k  •  188 

 Image-Text-to-Text •  8B • Updated   •  109k  •  625 

 Image-Text-to-Text •  8B • Updated   •  1.75k  •  28 

 Image-Text-to-Text •  8B • Updated   •  63  •  95 

 Image-Text-to-Text •  7B • Updated   •  1.81k  •  271 

 Zero-Shot Image Classification •  0.9B • Updated   •  1.96M  •  681 

 Image-Text-to-Text •  35B • Updated   •  20.1k  •  364 

 Image-Text-to-Text •  8B • Updated   •  7.92k  •  245 

 Image-Text-to-Text •  13B • Updated   •  38.9k  •  61 

 Text Generation •  7B • Updated   •  669k  •  4.12k 

 Viewer • Updated  •  276M •  4.19k  •  171 

 Viewer • Updated  •  2.75M •  7.9k  •  395 

 Viewer • Updated  •  1.88M •  134k  •  548 

 Viewer • Updated  •  3.41M •  17k  •  194 

 Viewer • Updated  •  7.1k •  7.56k  •  159 

 Viewer • Updated  •  12M •  35k  •  58 

🐠

 146

Generate text from images and prompts

🐨

 169

Chat with a visual AI that answers questions about images

 Paper • 2403.09611 • Published  •  130 

More Articles from our Blog

multimodalnlpcommunity

  74

 April 16, 2026 multimodalnlpcommunity

  65

 April 9, 2026
