---
title: Docmatix - a huge dataset for Document Visual Question Answering
kind: blog
topic: models
subtopic: training
secondary_topics: []
summary: Builds Docmatix, a DocVQA dataset of 2.4M images / 9.5M Q&A pairs from 1.3M
  PDFs (240x prior scale) by prompting Phi-3-small over PDFA OCR transcriptions and
  filtering ~15% hallucinated pairs; fine-tuning Florence-2 on it shows the resulting
  gains.
triage: null
skip_reason: null
source: huggingface
url: https://huggingface.co/blog/docmatix
author: Andres Marafioti; Hugo Laurençon
published: '2024-07-18'
fetched: '2026-07-14T22:11:46Z'
classifier: claude
taxonomy_rev: 1
words: 762
content_sha256: 6c08cce7e032d49e98ddf266288426a72047f050a2c71701784fb39f0a0915ea
---

# Docmatix - a huge dataset for Document Visual Question Answering

Text Generation •  7B • Updated   •  17.4k  •  178  

#### microsoft/Phi-3-small-8k-instruct

![](https://cdn-avatars.huggingface.co/v1/production/uploads/1583646260758-5e64858c87403103f9f1055d.png) 

 Published
					July 18, 2024 

  Upvote 

 78

 ![Example from the dataset](https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/blog/docmatix_example.png)


 *An example from the dataset*

We first had the idea to create Docmatix when we developed [The Cauldron](https://huggingface.co/datasets/HuggingFaceM4/the_cauldron), an extensive collection of 50 datasets for the fine-tuning of Vision-Language Model (VLM), and [Idefics2](https://huggingface.co/blog/idefics2) in particular. Through this process, we identified a significant gap in the availability of large-scale Document Visual Question Answering (DocVQA) datasets. The primary dataset we relied on for Idefics2 was DocVQA, which contains 10,000 images and 39,000 question-answer (Q/A) pairs. Fine-tuning on this and other datasets, open-sourced models still maintain a large gap in performance to closed-source ones.
To address this limitation, we are excited to introduce Docmatix, a DocVQA dataset featuring 2.4 million images and 9.5 million Q/A pairs derived from 1.3 million PDF documents. A **240X** increase in scale compared to previous datasets.

 ![Comparing Docmatix to other DocVQA datasets](https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/blog/docmatix_dataset_comp.png)


 *Comparing Docmatix to other DocVQA datasets*

Here you can explore the dataset yourself and see the type of documents and question-answer pairs contained in Docterix.

Docmatix is generated from [PDFA, an extensive OCR dataset containing 2.1 million PDFs](https://huggingface.co/datasets/pixparse/pdfa-eng-wds). We took the transcriptions from PDFA and employed a [Phi-3-small](https://huggingface.co/microsoft/Phi-3-small-8k-instruct) model to generate Q/A pairs. To ensure the dataset's quality, we filtered the generations, discarding 15% of the Q/A pairs identified as hallucinations. To do so, we used regular expressions to detect code and removed answers that contained the keyword “unanswerable”. 
The dataset contains a row for each PDF. We converted the PDFs to images at a resolution of 150 dpi, and uploaded the processed images to the Hugging Face Hub for easy access. 
All the original PDFs in Docmatix can be traced back to the original PDFA dataset, providing transparency and reliability. Still, we uploaded the processed images for convenience because converting many PDFs to images can be resource-intensive.

 ![Processing for Docmatix](https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/blog/docmatix_processing.png)


 *Processing pipeline to generate Docmatix*

After processing the first small batch of the dataset, we performed several ablation studies to optimize the prompts. We aimed to generate around four pairs of Q/A per page. Too many pairs indicate a large overlap between them, while too few pairs suggest a lack of detail.
Additionally, we aimed for answers to be human-like, avoiding excessively short or long responses. We also prioritized diversity in the questions, ensuring minimal repetition. Interestingly, when we guided the [Phi-3 model](https://huggingface.co/docs/transformers/main/en/model_doc/phi3) to ask questions based on the specific information in the document  (e.g., "What are the titles of John Doe?"), the questions showed very few repetitions. The following plot presents some key statistics from our analysis:

 ![Prompt analysis Docmatix](https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/blog/docmatix_prompt_analysis.png)


 *Analysis of Docmatix per prompt*

To evaluate Docmatix's performance, we conducted ablation studies using the Florence-2 model. We trained two versions of the model for comparison. The first version was trained over several epochs on the DocVQA dataset. The second version was trained for one epoch on Docmatix (20% of the images and 4% of the Q/A pairs), followed by one epoch on DocVQA to ensure the model produced the correct format for DocVQA evaluation. The results are significant: training on this small portion of Docmatix yielded a relative improvement of almost 20%. Additionally, the 0.7B Florence-2 model performed only 5% worse than the 8B Idefics2 model trained on a mixture of datasets and is significantly larger.

| Dataset | ANSL on DocVQA | model size | 
|---|---|---|
| Florence 2 fine-tuned on DocVQA | 60.1 | 700M | 
| Florence 2 fine-tuned on Docmatix | 71,4 | 700M | 
| Idefics2 | 74,0 | 8B | 

In this post, we presented Docmatix, a gigantic dataset for DocVQA. We showed that using Docmatix we can achieve a 20% increase in DocVQA performance when finetuning Florence-2. This dataset should help bridge the gap between proprietary VLMs and open-sourced VLMs. We encourage the open-source community to leverage Docmatix and train new amazing DocVQA models! We can't wait to see your models on the 🤗 Hub!

- [Docmatix used to finetune Florence-2 Demo](https://huggingface.co/spaces/HuggingFaceM4/Docmatix-Florence-2)
- [Finetuning Florence-2 Blog](https://huggingface.co/blog/finetune-florence2)
- [Fine tuning Florence-2 Github Repo](https://github.com/andimarafioti/florence2-finetuning)
- [Vision Language Models Explained](https://huggingface.co/blog/vlms)

We would like to thank merve and leo for their reviews and thumbnails for this blog.

 Text Generation •  7B • Updated   •  17.4k  •  178 

 Viewer • Updated  •  2.55M •  12.4k  •  309 

 Viewer • Updated  •  1.88M •  134k  •  548 

 Viewer • Updated  •  7.1k •  7.56k  •  159 

📉

 17

Answer questions about images using text prompts

More Articles from our Blog

communityevaluationsynthetic-data

  17

 July 25, 2024 llmnlpsynthetic-data

  Hot 460

 July 16, 2024
