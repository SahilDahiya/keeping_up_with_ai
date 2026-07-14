---
title: 'LAVE: Zero-shot VQA Evaluation on Docmatix with LLMs - Do We Still Need Fine-Tuning?'
kind: blog
topic: evals-observability
subtopic: evaluation
secondary_topics:
- models/multimodal
summary: Shows that exact-match VQA metrics (VQA Accuracy, ANLS, CIDEr, BLEU) unfairly
  punish correct out-of-distribution answers, and applies LAVE — an LLM-as-judge metric
  where Llama-2-7B-chat rates answers 1-3 with a rationale from in-context demonstrations
  — to evaluate MPLUGDocOwl1.5 zero-shot on Docmatix, where its ANLS collapses despite
  84% on DocVQA.
triage: null
skip_reason: null
source: huggingface
url: https://huggingface.co/blog/zero-shot-vqa-docmatix
author: Dana Aubakirova; Andres Marafioti
published: '2024-07-25'
fetched: '2026-07-14T22:11:44Z'
classifier: claude
taxonomy_rev: 1
words: 1246
content_sha256: 96124aeb9eb504132b9c0853c3c9a795ef3c5ff84de9525ade5dd196149cf1ad
---

# LAVE: Zero-shot VQA Evaluation on Docmatix with LLMs - Do We Still Need Fine-Tuning?

Text Generation •  7B • Updated   •  294k  •  4.79k  

#### meta-llama/Llama-2-7b-chat-hf

![](https://cdn-avatars.huggingface.co/v1/production/uploads/646cf8084eefb026fb8fd8bc/oCTqufkdTkjyGodsx1vo1.png) 

 Published
					July 25, 2024 

  Upvote 

 17

Although the generated answers semantically align with the reference answers, as illustrated in Figure 1, they still receive low scores. This raises these questions: Should we fine-tune the models to improve these metrics, or should we develop new metrics that better align with human perception?

  * Figure 1: t-SNE visualization of Zero-Shot Generated and Reference Answers from Docmatix dataset *

Our community has recently focused on out-of-distribution (OOD) evaluation, utilizing methods like zero-shot transfer to unseen VQA tasks or fine-tuning on one VQA dataset and evaluating on another. This shift is increasingly relevant with the rise of synthetic datasets such as Docmatix, SciGraphQA, SimVQA used to fine-tune Vision Language Models (VLMs).

Traditionally, VQA Accuracy has been the main metric for evaluating model performance. It relies on exact string matching between a model's predicted answer and a set of reference answers annotated by humans. This metric worked well because VQA evaluation followed an independent and identically distributed (IID) paradigm, where training and testing data distributions were similar, allowing models to adapt effectively [See details here](https://arxiv.org/pdf/2205.12191).

In OOD settings, generated answers might not match reference answers despite being correct due to differences in format, specificity, or interpretation. This paradigm is perfectly illustrated in the Figure 1, where we compare the zero-shot generated captions vs the reference captions from the synthetic dataset. This is particularly true for instruction-generated datasets and their human-curated counterparts.  Some [methods](https://proceedings.mlr.press/v202/li23q.html) have attempted to align answer formats with references, but this only addresses the symptom, not the root cause of flawed evaluation metrics. While human evaluation is reliable, it is costly and not scalable, highlighting the need for metrics that better align with human judgment. 

[Docmatix](https://huggingface.co/blog/docmatix) is the largest synthetic DocVQA dataset, generated from the curated document dataset, [PDFA](https://huggingface.co/datasets/pixparse/pdfa-eng-wds). It is 100x larger than previously available datasets. The human-curated counterpart is DocVQA, which serves as an evaluation benchmark for VQA models for Document Understanding.  In this post, we are going to use **the subset of Docmatix** which consists around 200 test samples, which can be downloaded here [Docmatix-zero-shot-exp](https://huggingface.co/datasets/HuggingFaceM4/Docmatix/viewer/zero-shot-exp). 

  * Figure 2: The examples of Q&A pairs from Docmatix and DocVQA test set. Note: the corresponding images are not shown here. *

Although the content of the question and answer pairs in Docmatix and DocVQA is similar, their styles differ significantly. Traditional metrics like CIDER, ANLS, and BLEU can be overly restrictive for zero-shot evaluation in this context. Motivated by the similarity of the embeddings observed in t-SNE (Figure 1), we decided to use a different evaluation metric. In this post, we consider the LAVE (LLM-Assisted VQA Evaluation) metric to better assess generalization on this unseen but semantically similar dataset.

  * Figure 3: t-SNE visualization of Question, Answer and Image features from Docmatix and DocVQA datasets *

  * Figure 5: t-SNE visualization of Question, Answer and Image features from Docmatix and DocVQA datasets *

For our evaluation, we chose [MPLUGDocOwl1.5](https://arxiv.org/pdf/2403.12895) as a baseline model. This model achieves an 84% ANLS score on the test subset of the original DocVQA dataset. We then ran a zero-shot generation on a subset of Docmatix, consisting of 200 images. We used [Llama-2-Chat-7b](https://huggingface.co/meta-llama/Llama-2-7b-chat-hf) for rating the answers. 

We followed the procedure outlined in the [paper](https://arxiv.org/html/2310.02567v2). The VQA evaluation is framed as an answer-rating task suitable for in-context learning with LLMs. We used a rating scale from 1 to 3 to account for ambiguous questions or incomplete answers. The prompt included a task description, several demonstrations of input/output, and the input for a test example. 

We structured our task description and included the instruction **"Give the rationale before rating"** to showcase a justification for the assigned rating. Each demonstration comprised a question, a set of reference answers, the candidate answer, the answer rating, and an explanation for the rating. We also include the **"Provide only one rating"** to avoid sentence-by-sentence analysis, which sometimes resulted in several ratings.

```
task_description = """You are given a question, a set of gold-standard reference answers written by
experts, and a candidate answer. Please rate the accuracy of the candidate answer for the question
considering the reference answers. Use a scale of 1-3, with 1 indicating an incorrect or irrelevant
answer, 2 indicating an ambiguous or incomplete answer, and 3 indicating a correct answer.
Give the rationale before rating. Provide only one rating.
THIS IS VERY IMPORTANT:
A binary question should only be answered with 'yes' or 'no',
otherwise the candidate answer is incorrect."""
demonstrations = [
    {
        "question": "What's the weather like?",
        "reference_answer": ["sunny", "clear", "bright", "sunny", "sunny"],
        "generated_answer": "cloudy"
    }
]
```
Given the LLM’s generated text for the test example, we extracted the rating from the last character (either 1, 2, or 3) and mapped it to a score in the range [0, 1]: [ s = \frac{r - 1}{2} ]

The results of our evaluation are summarized in the table below:

| Metric | CIDER | BLEU | ANLS | LAVE | 
|---|---|---|---|---|
| Score | 0.1411 | 0.0032 | 0.002 | 0.58 | 

  * Figure 4: Llama rating and rationale for the generated and reference answers from Docmatix test subset. *

  * Figure 5: Llama rating and rationale for the generated and reference answers from Docmatix test subset. *

We have approximately 50% accuracy gain when using LLMs to evaluate responses, indicating that the answers can be correct despite not adhering to a strict format. This suggests that our current evaluation metrics may be too rigid. It’s important to note that this is not a comprehensive research paper, and more ablation studies are needed to fully understand the effectiveness of different metrics on the evaluation of zero-shot performance on synthetic dataset. We hope this work serves as a starting point to broaden the current research focus on improving the evaluation of zero-shot vision-language models within the context of synthetic datasets and to explore more efficient approaches beyond prompt learning.

```
@inproceedings{cascante2022simvqa,
  title={Simvqa: Exploring simulated environments for visual question answering},
  author={Cascante-Bonilla, Paola and Wu, Hui and Wang, Letao and Feris, Rogerio S and Ordonez, Vicente},
  booktitle={Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition},
  pages={5056--5066},
  year={2022}
}
@article{hu2024mplug,
  title={mplug-docowl 1.5: Unified structure learning for ocr-free document understanding},
  author={Hu, Anwen and Xu, Haiyang and Ye, Jiabo and Yan, Ming and Zhang, Liang and Zhang, Bo and Li, Chen and Zhang, Ji and Jin, Qin and Huang, Fei and others},
  journal={arXiv preprint arXiv:2403.12895},
  year={2024}
}
@article{agrawal2022reassessing,
  title={Reassessing evaluation practices in visual question answering: A case study on out-of-distribution generalization},
  author={Agrawal, Aishwarya and Kaji{\'c}, Ivana and Bugliarello, Emanuele and Davoodi, Elnaz and Gergely, Anita and Blunsom, Phil and Nematzadeh, Aida},
  journal={arXiv preprint arXiv:2205.12191},
  year={2022}
}
@inproceedings{li2023blip,
  title={Blip-2: Bootstrapping language-image pre-training with frozen image encoders and large language models},
  author={Li, Junnan and Li, Dongxu and Savarese, Silvio and Hoi, Steven},
  booktitle={International conference on machine learning},
  pages={19730--19742},
  year={2023},
  organization={PMLR}
}
@inproceedings{manas2024improving,
  title={Improving automatic vqa evaluation using large language models},
  author={Ma{\~n}as, Oscar and Krojer, Benno and Agrawal, Aishwarya},
  booktitle={Proceedings of the AAAI Conference on Artificial Intelligence},
  volume={38},
  number={5},
  pages={4171--4179},
  year={2024}
}
@article{li2023scigraphqa,
  title={Scigraphqa: A large-scale synthetic multi-turn question-answering dataset for scientific graphs},
  author={Li, Shengzhi and Tajbakhsh, Nima},
  journal={arXiv preprint arXiv:2308.03349},
  year={2023}
}
```
 Text Generation •  7B • Updated   •  294k  •  4.79k 

 Viewer • Updated  •  2.55M •  12.4k  •  309 

 Viewer • Updated  •  7.1k •  7.56k  •  159 

More Articles from our Blog

communitydatasetssynthetic-data

  78

 July 18, 2024 evaluationcommunityleaderboard

 
- +3

 44

 June 30, 2026
