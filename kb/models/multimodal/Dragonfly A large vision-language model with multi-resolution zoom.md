---
title: 'Dragonfly: A large vision-language model with multi-resolution zoom'
topic: models
subtopic: multimodal
secondary_topics:
- models/reasoning
summary: Introduces Dragonfly, a vision-language model with multi-resolution zoom.
source: together
url: https://www.together.ai/blog/dragonfly-v1
author: Kezhen Chen; Rahul Thapa; Rahul Chalamala; Ben Athiwaratkun; Shuaiwen Leon
  Song; James Zou
published: '2024-06-06'
fetched: '2026-07-11T04:23:09Z'
classifier: codex
taxonomy_rev: 1
words: 1789
content_sha256: 84948133aac2411a37c47e614b0f4bb1fc297b26dc7b697e420b530dc094df05
triage: keep
skip_reason: null
---

# Dragonfly: A large vision-language model with multi-resolution zoom

We are excited to announce the launch of Dragonfly, an instruction-tuning Vision-language architecture, that enhances fine-grained visual understanding and reasoning about image regions.

We are releasing the Dragonfly architecture, which uses multi-resolution zoom-and-select to enhance multi-modal reasoning while being context-efficient. We are also launching two new open-source models  [Llama-3-8b-Dragonfly-v1](https://huggingface.co/togethercomputer/Llama-3-8B-Dragonfly-v1) a general-domain model trained on 5.5 million image-instruction pairs and [Llama-3-8b-Dragonfly-Med-v1](https://huggingface.co/togethercomputer/Llama-3-8B-Dragonfly-Med-v1) finetuned on additional 1.4 biomedical image-instruction data. Dragonfly demonstrates promising performance on vision-language benchmarks like commonsense visual QA and image captioning. Dragonfly-Med outperforms prior models, including Med-Gemini on multiple medical imaging tasks, showcasing its capabilities for high-resolution medical data.

Figure 1: Generated example from Llama-3-8B-Dragonfly

![__wf_reserved_inherit](https://cdn.prod.website-files.com/69654e88dce9154b5f12070c/699e0b02c76907e92986f0c7_66b292b6f05bb2845d861dbf_6661eeab92ebdcff8cda76f2_image%252520(5).png)

**Question**: Summarize the visual contents of the image.


**Dragonfly Response**: In the heart of a vibrant skatepark, a skateboarder is caught in a moment of pure exhilaration. The skateboarder, dressed in a black t-shirt adorned with a yellow graphic and black pants, is suspended in mid-air, performing an impressive trick on a concrete ramp. The skateboarder's arms are outstretched, adding balance to the daring stunt. The skatepark itself is a concrete playground, with the skateboarder's ramp being the main focus. In the background, palm trees sway gently, adding a touch of nature to the urban setting. A few spectators can be seen in the distance, their attention riveted on the airborne skateboarder. The image captures not just a moment, but a story of skill, courage, and the joy of skateboarding.

Figure 2: Generated examples from Llama-3-8B-Dragonfly-Med

![__wf_reserved_inherit](https://cdn.prod.website-files.com/69654e88dce9154b5f12070c/699e0b02c76907e92986f0be_66b292b6f05bb2845d861dc9_6661eed892ebdcff8cda8fc9_image%252520(9).png)

**Question**: Write a detailed radiology note based on the chest X-ray.


**Gold Answer**: AP upright and lateral views of the chest were provided. Left chest wall pacer pack is again seen with leads extending into the right heart. Abandoned pacing leads are also noted in the right chest wall extending into the right heart. The heart remains moderately enlarged. Lung volumes are low, with equivocal ground-glass opacity on the frontal view, which appears less conspicuous on the lateral view most likely attributable to underpenetrated technique. No gross evidence for pneumonia or pulmonary edema. No large effusions are seen. There is no pneumothorax. Bony structures are intact.


**Dragonfly Response**: PA and lateral views of the chest provided. Left chest wall pacer device is again noted with leads extending into the region the right atrium and right ventricle. The heart remains mildly enlarged. There is mild hilar congestion without frank edema. No convincing signs of pneumonia. No large effusion or pneumothorax. Cardiomediastinal silhouette is stable. Bony structures are intact

## Dragonfly Model Architecture

*Arxiv Paper** with technical details and **codebase** for architecture implementation*

Dragonfly is special because:

- Dragonfly employs two key strategies: multi-resolution visual encoding and zoom-in patch selection, which enables the model to focus more fine-grained details on image regions and provide better commonsense reasoning. Despite the model being optimized for capturing fine-grained image details, the model achieves good zero-shot performance at standard image-understanding benchmarks such as visual question-answering or natural-image-captioning.
- We demonstrate our model's understanding and reasoning capabilities on biomedical tasks, which often require a fine-grained understanding of high-resolution image regions. By finetuning our general-domain model on a biomedical instruction-tuning dataset with 1.4 million biomedical image-text pairs, Dragonfly-med, our biomedical version of the model, achieves state-of-the-art or competitive performance on multiple biomedical benchmarks, including visual question answering, image captioning, and radiology report generation.

Figure 3: Overview of the Dragonfly architecture

![__wf_reserved_inherit](https://cdn.prod.website-files.com/69654e88dce9154b5f12070c/699e0b02c76907e92986f0c4_66b292b6f05bb2845d861dc2_66614db787f49c335e5c4118_image3.png)

**Multi-resolution Visual Encoding:** Dragonfly processes images at multiple resolutions—low, medium, and high. Each image, depending on its resolution, is divided into sub-images that are encoded into visual tokens. These tokens are then projected into a language space, forming a concatenated sequence that feeds into the LLM. This method allows the model to handle larger images efficiently and improves the granularity of visual data processing.

**Zoom-in Patch Selection:** To further refine the model's focus on important visual details, Dragonfly employs a selective approach for high-resolution images. It uses a novel zoom-in patch selection strategy to identify and retain only those high-resolution sub-images that provide the most significant visual information. This is achieved by comparing summary embeddings of medium and high-resolution sub-images to select the most semantically relevant patches. This targeted selection reduces redundancy and focuses on crucial content areas, thereby enhancing the overall model efficiency and fine-grained understanding on these areas.

Together, these strategies enable Dragonfly to achieve a detailed and efficient visual understanding, making it particularly adept at processing complex image data in specific domains.

Figures 4 and 5: Generated examples from Llama-3-8B-Dragonfly

![__wf_reserved_inherit](https://cdn.prod.website-files.com/69654e88dce9154b5f12070c/699e0b02c76907e92986f0b4_66b292b6f05bb2845d861dbb_6661f9c35d300e04e8ef323f_image%252520(6).png)

**Figure 4 Question:**Summarize the visual content of the image first and then answer the questions. What process does this diagram portray and which solar body is portrayed in this diagram?

**Dragonfly Response:**The diagram portrays the process of photosynthesis in plants, which is a fundamental biological process where plants convert light energy from the sun into chemical energy in the form of glucose. The solar body portrayed in this diagram is the sun, which is shown at the top left corner, providing the light energy that is essential for photosynthesis.

**Figure 5 Question:**Summarize the image and why it is funny?

**Dragonfly Response:**The image is a humorous take on the Mona Lisa painting, featuring a dog in the place of the human subject. The dog's expression, combined with the iconic pose and attire, creates a playful and amusing effect. The painting is executed in the same style as the original Mona Lisa, with similar brushwork and color palette, which adds to the humor by juxtaposing the serious art historical context with the light-hearted subject matter.

## Dragonfly Model Evaluation

We evaluate Dragonfly trained based on LLaMA-8B on five popular vision-language benchmarks that require strong commonsense reasoning and detailed image understanding, AI2D, ScienceQA, MMMU, MMVet, and POPE. AI2D and ScienceQA evaluate visual commonsense reasoning in the science domain. MMMU and MMVet focus on providing a comprehensive evaluation of the vision-language capabilities. POPE evaluates the object-level hallucination of the regional details. Dragonfly achieved competitive performance compared with other popular vision-language models, demonstrating the effectiveness of Dragonfly on commonsense reasoning and fine-grained understanding of image regions. The results are presented in the following table:

| Model | AI2D | ScienceQA | MMMU | MMVet | POPE |
|---|---|---|---|---|---|
| VILA | - | 68.2 | 34.9 | 85.5 | |
| LLaVA-v1.5 (Vicuna-7B) | 54.8 | 70.4 | 35.3 | 30.5 | 85.9 |
| LLaVA-v1.6 (Mistral-7B) | 60.8 | 72.8 | 33.4 | 44.8 | 86.7 |
| QWEN-VL-chat | 52.3 | 68.2 | 35.9 | - | - |
| Dragonfly (LLaMA-8B) | 63.6 | 80.5 | 37.8 | 35.9 | 91.2 |

## Dragonfly-Med

We partnered with the Zou group at Stanford Medicine to finetune Dragonfly on additional 1.4 million biomedical image instructions to develop the biomedical version, Dragonfly-Med.

Figures 6 and 7: Generated examples from Llama-3-8B-Dragonfly-Med

![__wf_reserved_inherit](https://cdn.prod.website-files.com/69654e88dce9154b5f12070c/699e0b02c76907e92986f0c1_66b292b6f05bb2845d861dd1_6661f97f1204614802b7b80f_image%252520(7).png)

**Figure 4 Question:**Please provide brief description of the image.

**Gold Answer:**Abdominal enhanced CT shows a ring-like enhanced and central heterogeneous tumor in the pelvis.

**Dragonfly Response:**Computed tomography scan of the abdomen and pelvis showing a large lobulated mass in the pelvic cavity.

**Explain the visual content of the image.**

Figure 5 Question:

Figure 5 Question:

**Gold Answer:**GROSS: HEMATOLOGIC: Spleen: Chronic Myelogenous Leukemia: Gross natural color whole spleen massively enlarged.

**Dragonfly Response:**HEMATOLOGIC: Spleen: Chronic Myelogenous Leukemia: Gross natural color external view of massively enlarged spleen with multiple infarcts seen from capsule.

Dragonfly-Med is evaluated on both visual question-answering, medical image captioning, and clinical report generation evaluation. Our model outperforms Med-Gemini, which was finetuned a customized version of Gemini 1.5 with about 5x more image-instruction data, on all the three question-answering datasets. The following two tables show the results on these benchmarks. The first table shows the performance on question-answering benchmarks and the second table presents the performance of biomedical image caption and report generation.

| Dataset | Metric | LLaVA-Med | Med-Gemini | SOTA | Dragonfly-Med (LLaMA-8B) |
|---|---|---|---|---|---|
| VQA-RAD | Acc (closed) | 84.2 | 69.7 | 87.1 | 77.4 |
| Token F1 | - | 50.1 | 62.1 | 59.6 | |
| SLAKE | Acc (closed) | 83.2 | 84.8 | 91.6 | 90.4 |
| Token F1 | - | 75.8 | 89.3 | 88.8 | |
| Path-VQA | Acc (closed) | 91.7 | 83.3 | 91.7 | 92.3 |
| Token F1 | - | 58.7 | 62.7 | 67.6 |


| Dataset | Metric | BiomedGPT SOTA | Dragonfly-Med (LLaMA-8B) | |
|---|---|---|---|---|
| IU X-Ray | ROUGE-L METEOR CIDEr | 28.5 12.9 40.1 | 44.8 24.2 43.5 | 28.5 29.7 58.8 |
| Peir Gross | ROUGE-L METEOR CIDEr | 36.0 15.4 122.7 | 36.0 15.4 122.7 | 40.3 38.3 179.9 |
| ROCO | ROUGE-L METEOR CIDEr | 18.2 7.8 24.2 | 18.2 7.8 24.2 | 19.3 15.1 40.1 |
| MIMIC CXR | ROUGE-L METEOR CIDEr | 23.8 14.2 14.7 | 33.5 19.0 50.9 | 24.2 22.6 47.2 |


Dragonfly-Med outperforms the existing state-of-the-art models across multiple benchmarks on the Path-VQA dataset for both accuracy (closed) and token F1 metrics. It attains an accuracy of 90.4% on the SLAKE dataset, which is close to the current state-of-the-art of 91.6%. Notably, Dragonfly-Med outperforms Med-Gemini, a model finetuned from Gemini-1.5 on 7 million biomedical data samples, on all VQA tasks we evaluated. On the image captioning task, Dragonfly-Med achieves state-of-the-art or competitive results on several metrics across these datasets. Notably, on the Peir Gross and ROCO datasets, Dragonfly-Med outperforms existing methods on all three metrics: ROUGE-L, METEOR, and CIDEr. Some of the baseline models are much larger than our current implementation. The zoom-and-select architecture of Dragonfly is especially powerful for medical image understanding as medical images are often very large and the salient regions are found in small patches.

## Conclusion and Future Work

Dragonfly architecture provides a potential research direction on zooming in image regions to focus more selected fine-grained visual information. We trained two checkpoints based on LLaMA3-8B-Instruct and achieved promising results on both general-domain and biomedical-domain tasks. We hope this work could benefit the research community to explore more open-sourced multimodal research and apply AI on real-world problems.

We will keep improving the comprehensive capabilities of open-source multimodal models. In the future, we will explore new architectures, better visual encoding strategies, more comprehensive studies on how the data mixture should be and more scientific domains to provide benefits for broader fields.

## Acknowledgements

We especially appreciate the contributions and collaborations of our partner, Stanford Medicine. We would also like to acknowledge the following resources that were instrumental in the development of Dragonfly:

- Meta LLaMA3: We utilized the LLaMA3 as our language model backbone for our current two checkpoints.
- CLIP: Our current visual backbone is CLIP model from OpenAI
- Our codebase is built upon codebases of Otter and LLaVA-UHD.
