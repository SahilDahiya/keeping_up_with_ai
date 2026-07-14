---
title: 'NPHardEval Leaderboard: Unveiling the Reasoning Abilities of Large Language
  Models through Complexity Classes and Dynamic Updates'
kind: blog
topic: evals-observability
subtopic: benchmark-design
secondary_topics:
- models/reasoning
summary: 'NPHardEval grounds LLM reasoning evaluation in computational complexity
  classes: 900 auto-generated algorithmic questions (3 P, 3 NP-complete, 3 NP-hard
  tasks x 10 difficulty levels), refreshed monthly to defeat overfitting, scored by
  weighted accuracy and failure rate.'
triage: null
skip_reason: null
source: huggingface
url: https://huggingface.co/blog/leaderboard-nphardeval
author: Lizhou Fan; Wenyue Hua; Haoyang Ling; Clémentine Fourrier
published: '2024-02-02'
fetched: '2026-07-14T22:06:56Z'
classifier: claude
taxonomy_rev: 1
words: 1028
content_sha256: 88d65ebb97547f16d232c509e4a68b07fbf4f884e977c3250c289c5724f7ae55
---

# NPHardEval Leaderboard: Unveiling the Reasoning Abilities of Large Language Models through Complexity Classes and Dynamic Updates

Viewer • Updated  •  12 •  19    

# 
	[
		
	](https://huggingface.co#nphardeval-leaderboard-unveiling-the-reasoning-abilities-of-large-language-models-through-complexity-classes-and-dynamic-updates)
	
		NPHardEval Leaderboard: Unveiling the Reasoning Abilities of Large Language Models through Complexity Classes and Dynamic Updates
	

 [Update on GitHub](https://github.com/huggingface/blog/blob/main/leaderboard-nphardeval.md)

[  Upvote 4 ](https://huggingface.co/login?next=%2Fblog%2Fleaderboard-nphardeval)

![Lizhou Fan's avatar](https://cdn-avatars.huggingface.co/v1/production/uploads/62b0c1fd21241b71c9ab8987/ArWJrVCXLUCbIoeqjKKBx.jpeg) 

  [Lizhou Fanlizhouf    ](https://huggingface.co/lizhouf)

![Wenyue Hua's avatar](https://cdn-avatars.huggingface.co/v1/production/uploads/639a25aba2b0b1c9d85a51e8/pphz-MK62hPNbBkMHAkeR.jpeg) 

  [Wenyue HuawenyueH    ](https://huggingface.co/wenyueH)

![Haoyang Ling's avatar](https://cdn-avatars.huggingface.co/v1/production/uploads/noauth/3tCKhbLvzqFNpsMzoSGwf.jpeg) 

  [Haoyang Linghyfrankl    ](https://huggingface.co/hyfrankl)

![Clémentine Fourrier's avatar](https://cdn-avatars.huggingface.co/v1/production/uploads/1644340617257-noauth.png) 

  [NPHardEval leaderboard](https://huggingface.co/spaces/NPHardEval/NPHardEval-leaderboard), using

[NPHardEval](https://arxiv.org/abs/2312.14890), a cutting-edge benchmark developed by researchers from the University of Michigan and Rutgers University.

NPHardEval introduces a dynamic, complexity-based framework for assessing Large Language Models' (LLMs) reasoning abilities. It poses 900 algorithmic questions spanning the NP-Hard complexity class and lower, designed to rigorously test LLMs, and is updated on a monthly basis to prevent overfitting!

## 
	[
		
	](https://huggingface.co#a-unique-approach-to-llm-evaluation)
	
		A Unique Approach to LLM Evaluation
	

[NPHardEval](https://arxiv.org/abs/2312.14890) stands apart by employing computational complexity classes, offering a quantifiable and robust measure of LLM reasoning skills. The benchmark's tasks mirror real-world decision-making challenges, enhancing its relevance and applicability. Regular monthly updates of the benchmark data points mitigate the risk of model overfitting, ensuring a reliable evaluation. 

The major contributions of NPHardEval are new using new benchmarking strategies (proposing an automatic and dynamic benchmark), and introducing a new way to evaluate LLM reasoning.

Regarding benchmarking strategies, NPHardEval uses an **automated mechanism**, both to generate and check questions in the benchmark. Since they are based on algorithmically computable problems, human intervention is not required to determine the correctness of the responses from LLMs. This also allows NPHardEval to be a **dynamic benchmark**: since questions can be automatically generated, the benchmark can be updated on a monthly basis. This monthly-refreshed benchmark helps prevent model overfitting as we can always generate novel questions with varying difficulty levels for evaluation. 

The questions themselves use a new system to evaluate LLM Reasoning. The questions in the benchmark are grounded in the computational complexity hierarchy, a well-established concept extensively studied in theoretical computer science. This foundation enables us to leverage existing research to rigorously and quantitatively measure an LLM's logical reasoning extent, by **defining reasoning via complexity classes**. The benchmark also deliberatley excludes numerical computation from the questions, since it is a notoriously difficult task for LLMs. **Focusing on logical questions** allows for a more accurate evaluation of an LLM's pure logical reasoning ability, as numerical questions can obscure this assessment.

## 
	[
		
	](https://huggingface.co#data-synthesis)
	
		Data Synthesis
	

NPHardEval uses 100 questions for each of 9 different algorithms, with 10 difficulty levels, resulting in 900 questions across complexity and difficulty. The 9 algorithms, including 3 P, 3 NP-complete, and 3 NP-hard questions, are characterized according to the computing theory. The 900 questions are all synthesized and updated monthly.

![Tasks in NPHardEval](https://github.com/casmlab/NPHardEval/raw/main/figure/questions_blog.png) 

More background and insights are available in [these slides](https://docs.google.com/presentation/d/1VYBrCw5BqxuCCwlHeVn_UlhFj6zw04uETJzufw6spA8/edit?usp=sharing).

## 
	[
		
	](https://huggingface.co#evaluation-metrics)
	
		Evaluation Metrics
	

We use two metrics to evaluate the reasoning ability of LLMs: Weighted Accuracy and Failure Rate.

### 
	[
		
	](https://huggingface.co#weighted-accuracy-wa)
	
		Weighted Accuracy (WA)
	

**Weighted Accuracy (WA)** is used to evaluate problem-solving accuracy. This method is applied to each problem, either through comparison with a correct answer or via step-by-step result checking for problems without a singular answer. To reflect comparative accuracy more effectively, we assign weights to different difficulty levels. Each level's weight corresponds to its relative importance or challenge, with higher difficulty levels receiving more weight in a linear progression (for instance, level 1 has weight 1, level 2 has weight 2, and so on).

The formula for Weighted Accuracy is as follows:

In this equation, represents the weight assigned to difficulty level (ranging from 1 to 10), and is the accuracy at that level.

### 
	[
		
	](https://huggingface.co#failure-rate-fr)
	
		Failure Rate (FR)
	

Another critical metric we consider is the **Failure Rate (FR)**. This measure helps assess the frequency of unsuccessful outcomes across different problems and difficulty levels. It's particularly useful for identifying instances where an LLM's result does not match the expected output format.

The Failure Rate is calculated by considering the proportion of failed attempts relative to the total number of attempts for each difficulty level. An attempt is counted as failed if the model generates results that cannot be successfully parsed in all endpoint calls. We set the maximum number of tries as 10. For each problem, the Failure Rate is then aggregated across all difficulty levels, considering the total of 10 attempts at each level.

The formal definition of Failure Rate is:

Here, denotes the number of failed attempts at difficulty level .

## 
	[
		
	](https://huggingface.co#experimentation-and-insights)
	
		Experimentation and Insights
	

The benchmark includes comprehensive experiments to analyze LLMs across various complexity classes and difficulty levels. It delves into the nuances of LLM performance, providing valuable insights into their reasoning strengths and limitations. In general:

- Closed-source models generally perform better than open-source models, with GPT 4 Turbo performing the best overall.
- Models generally perform better on less-complex questions, i.e. easier complexity classes, while not always linearly decrease on complexity levels. Models such as Claude 2 perform the best on NP-complete (middle-complexity) questions.
- Some open-source models can outperform close-source models on specific questions. Leading open-source models include Yi-34b, Qwen-14b, Phi-2, and Mistral-7b.

![Weighted Accuracy and Failure Rate](https://github.com/casmlab/NPHardEval/raw/main/figure/weighted_accuracy_failed.png) 

![Zeroshot Heatmap](https://github.com/casmlab/NPHardEval/raw/main/figure/zeroshot_heatmap.png) 

## 
	[
		
	](https://huggingface.co#reproducing-nphardeval-benchmark-results-on-your-machine)
	
		Reproducing NPHardEval Benchmark results on your machine
	

To set up the NPHardEval Benchmark, you need to follow a few steps:

- Environment setup: after cloning the repository to your local machine, install the required python library with `conda`.`conda create --name llm_reason python==3.10 conda activate llm_reason git clone https://github.com/casmlab/NPHardEval.git pip install -r requirements.txt`
- Set-up API keys: fetch API keys and change the corresponding entries in `secrets.txt`.
- Example Commands: evaluate your model with the NPHardEval benchmark!

For example, to use the GPT 4 Turbo model (GPT-4-1106-preview) and the edit distance problem (EDP) for evaluation:

- For its zeroshot experiment, we can use:

```
  cd Close/run
  python run_p_EDP.py gpt-4-1106-preview
```
- For its fewshot experiment,

```
  cd Close/run
  python run_p_EDP_few.py gpt-4-1106-preview self
```
We currently support fewshot examples from the same question (self), and may support examples from other questions (other) in the future.

## 
	[
		
	](https://huggingface.co#join-the-conversation)
	
		Join the Conversation
	

[The NPHardEval leaderboard](https://huggingface.co/spaces/NPHardEval/NPHardEval-leaderboard), [dataset](https://huggingface.co/datasets/NPHardEval/NPHardEval-results) and [code](https://github.com/casmlab/NPHardEval) are available on Github and Hugging Face for community access and contributions.

We'll love to see community contributions and interest on the NPHardEval [GitHub Repository](https://github.com/casmlab/NPHardEval) and [Hugging Face Leaderboard](https://huggingface.co/spaces/NPHardEval/NPHardEval-leaderboard).
