---
title: 'BigCodeBench: The Next Generation of HumanEval'
kind: blog
topic: evals-observability
subtopic: evaluation
secondary_topics:
- models/benchmarks
summary: BigCodeBench replaces HumanEval with 1,140 function-level tasks that force
  LLMs to compose calls across 139 libraries, with rich test harnesses (average 5.6
  test cases, 99% branch coverage) and both Complete and Instruct splits. Reports
  that instruction-tuned models drop sharply on the Instruct split and that even top
  models are ~20 points behind human performance.
triage: null
skip_reason: null
source: huggingface
url: https://huggingface.co/blog/leaderboard-bigcodebench
author: Terry Yue Zhuo; Jiawei Liu; Qian Liu; Binyuan Hui; Niklas Muennighoff; Daniel
  Fried; Harm de Vries; Leandro von Werra; Clémentine Fourrier
published: '2024-06-18'
fetched: '2026-07-14T22:11:50Z'
classifier: claude
taxonomy_rev: 1
words: 2078
content_sha256: ad0ac7404eb225d195e1aa9a87957fac2537237f6d3c75eae5cf8f6c35fb3c34
---

# BigCodeBench: The Next Generation of HumanEval

Viewer • Updated  •  5.7k •  48.4k  •  85  

# 
	[
		
	](https://huggingface.co#bigcodebench-the-next-generation-of-humaneval)
	
		BigCodeBench: The Next Generation of HumanEval
	

 [Update on GitHub](https://github.com/huggingface/blog/blob/main/leaderboard-bigcodebench.md)

[  Upvote 54 ](https://huggingface.co/login?next=%2Fblog%2Fleaderboard-bigcodebench)

![Terry Yue Zhuo's avatar](https://cdn-avatars.huggingface.co/v1/production/uploads/62b7fb545233925f253531c8/W50u2G1HK3EtUKHRU189V.jpeg) 

  [Terry Yue Zhuoterryyz    ](https://huggingface.co/terryyz)

![BigCode's avatar](https://cdn-avatars.huggingface.co/v1/production/uploads/1659521200179-5e48005437cb5b49818287a5.png)

[bigcode](https://huggingface.co/bigcode)

![Jiawei Liu's avatar](https://cdn-avatars.huggingface.co/v1/production/uploads/644b584a9279988e0cbeb664/fhWCI_Q26tTruhdFkjejw.jpeg) 

  [Jiawei Liuganler    ](https://huggingface.co/ganler)

![BigCode's avatar](https://cdn-avatars.huggingface.co/v1/production/uploads/1659521200179-5e48005437cb5b49818287a5.png)

[bigcode](https://huggingface.co/bigcode)

![Qian Liu's avatar](https://cdn-avatars.huggingface.co/v1/production/uploads/612ee6a7b960e78c6d2319d4/2Hu9BaAyXbyh1vt0v1Qui.jpeg) 

  [Qian LiuSivilTaram    ](https://huggingface.co/SivilTaram)

![BigCode's avatar](https://cdn-avatars.huggingface.co/v1/production/uploads/1659521200179-5e48005437cb5b49818287a5.png)

[bigcode](https://huggingface.co/bigcode)

![Binyuan Hui's avatar](https://cdn-avatars.huggingface.co/v1/production/uploads/61e4c4ca1ab24785ac11ba69/1Q1zhhyGSJ9RJG9MzwxVv.jpeg) 

  [Binyuan Huihuybery    ](https://huggingface.co/huybery)

![BigCode's avatar](https://cdn-avatars.huggingface.co/v1/production/uploads/1659521200179-5e48005437cb5b49818287a5.png)

[bigcode](https://huggingface.co/bigcode)

![Niklas Muennighoff's avatar](https://cdn-avatars.huggingface.co/v1/production/uploads/5f1eb362eec0ad2a071ad6e2/nDiBXdLrOTw67lJp_y_WA.jpeg) 

  [Niklas MuennighoffMuennighoff    ](https://huggingface.co/Muennighoff)

![BigCode's avatar](https://cdn-avatars.huggingface.co/v1/production/uploads/1659521200179-5e48005437cb5b49818287a5.png)

[bigcode](https://huggingface.co/bigcode)

![Daniel Fried's avatar](https://cdn-avatars.huggingface.co/v1/production/uploads/623e041cdcda6a7153052d02/dCAe49oOZDsyp40xqiB-L.png) 

  [Daniel Frieddpfried    ](https://huggingface.co/dpfried)

![BigCode's avatar](https://cdn-avatars.huggingface.co/v1/production/uploads/1659521200179-5e48005437cb5b49818287a5.png)

[bigcode](https://huggingface.co/bigcode)

![Harm de Vries's avatar](https://cdn-avatars.huggingface.co/v1/production/uploads/62ce91e8b5811ba53c0ce7b9/ZNgd-p0h-q1j374QqEGrb.jpeg) 

  [Harm de Vriesharmdevries    ](https://huggingface.co/harmdevries)

![BigCode's avatar](https://cdn-avatars.huggingface.co/v1/production/uploads/1659521200179-5e48005437cb5b49818287a5.png)

[bigcode](https://huggingface.co/bigcode)

![Leandro von Werra's avatar](https://cdn-avatars.huggingface.co/v1/production/uploads/5e48005437cb5b49818287a5/4uCXGGui-9QifAT4qelxU.png) 

  [Leandro von Werralvwerra    ](https://huggingface.co/lvwerra)

![BigCode's avatar](https://cdn-avatars.huggingface.co/v1/production/uploads/1659521200179-5e48005437cb5b49818287a5.png)

[bigcode](https://huggingface.co/bigcode)

![Clémentine Fourrier's avatar](https://cdn-avatars.huggingface.co/v1/production/uploads/1644340617257-noauth.png) 

  [HumanEval](https://github.com/openai/human-eval)is a reference benchmark for evaluating large language models (LLMs) on code generation tasks, as it makes the evaluation of compact function-level code snippets easy. However, there are growing concerns about its effectiveness in evaluating the programming capabilities of LLMs, and the main concern is that tasks in HumanEval are too simple and may not be representative of real-world programming tasks. Compared to the algorithm-oriented tasks in HumanEval, real-world software development often involves diverse libraries and function calls. Furthermore, LLMs' performance on HumanEval is subject to

[contamination and overfitting issues](https://arxiv.org/abs/2403.07974), making it less reliable for evaluating the generalization of LLMs.

While there have been some efforts to address these issues, they are either domain-specific, deterministic, or agent-centric (sorry [DS-1000](https://github.com/HKUNLP/DS-1000), [ODEX](https://github.com/zorazrw/odex), and [SWE-bench](https://github.com/princeton-nlp/SWE-bench) 💔). We feel that the community still lacks an easy-to-use benchmark that can broadly evaluate the programming capabilities of LLMs, and that's what we focused on.

We are excited to announce the release of BigCodeBench, which evaluates LLMs on solving practical and challenging programming tasks without contamination. Specifically, BigCodeBench contains 1,140 function-level tasks to challenge LLMs to follow instructions and compose multiple function calls as tools from 139 libraries. To evaluate LLMs rigorously, each programming task encompasses 5.6 test cases with an average branch coverage of 99%.

Ready to dive into BigCodeBench? Let's get started! 🚀

## 
	[
		
	](https://huggingface.co#what-do-the-tasks-in-bigcodebench-look-like-🕵️♂️)
	
		What do the tasks in BigCodeBench look like? 🕵️♂️
	

BigCodeBench features complex, user-oriented instructions for each task, including clear functionality descriptions, input/output formats, error handling, and verified interactive examples. We avoid step-by-step task instructions, believing capable LLMs should understand and solve tasks from the user's perspective in an open-ended manner. We verify specific features using test cases.

```
# We elaborate the above task with some test cases:
# Requirements SetUp
import unittest
from unittest.mock import patch
import http.client
import ssl
import socket
# Start the test
class TestCases(unittest.TestCase):
    # Mock the successful connection and assess the response content
    @patch('http.client.HTTPSConnection')
    def test_response_content(self, mock_conn):
        """ Test the content of the response. """
        mock_conn.return_value.getresponse.return_value.read.return_value = b'Expected Content'
        result = task_func('www.example.com', 443, '/content/path')
        self.assertEqual(result, 'Expected Content')
    # Mock the failed connection and assess the error handling
    @patch('socket.create_connection')
    @patch('http.client.HTTPSConnection')
    def test_ssl_handshake_error_handling(self, mock_conn, mock_socket):
        """ Test handling of SSL handshake errors. """
        mock_socket.side_effect = ssl.SSLError('SSL handshake failed')
        with self.assertRaises(ssl.SSLError):
            task_func('badssl.com', 443, '/test/path')
    # More test cases...
```
Tasks in BigCodeBench utilize diverse function calls from popular libraries. We don't restrict the function calls LLMs can use, expecting them to choose appropriate functions and combine them flexibly to solve tasks. Test cases are designed as test harnesses to examine expected program behaviors during runtime.

To assess LLM performance, we use Pass@1 with greedy decoding, measuring the percentage of tasks correctly solved with the first generated code snippet via curated test cases. This approach aligns with benchmarks like [HumanEval](https://github.com/openai/human-eval) and [MBPP](https://github.com/google-research/google-research/tree/master/mbpp). We address LLMs' tendency to skip long code prompts by adding missing setups (e.g., import statements, global constants) during Pass@1 evaluation, referred to as calibrated Pass@1.

To better understand implementation complexity and tool-use diversity, we compare the tasks in BigCodeBench with those in representative benchmarks, including [APPS](https://github.com/hendrycks/apps), [DS-1000](https://github.com/HKUNLP/DS-1000), [ODEX](https://github.com/zorazrw/odex), [APIBench](https://github.com/ShishirPatil/gorilla/tree/main/data/apibench), [MBPP](https://github.com/google-research/google-research/tree/master/mbpp), [NumpyEval](https://github.com/microsoft/PyCodeGPT/tree/main/cert/pandas-numpy-eval), [PandasEval](https://github.com/microsoft/PyCodeGPT/tree/main/cert/pandas-numpy-eval), [HumanEval](https://github.com/openai/human-eval), and [TorchDataEval](https://github.com/microsoft/PyCodeGPT/tree/main/apicoder/private-eval). We find that BigCodeBench requires more complex reasoning and problem-solving skills to implement comprehensive functionalities.

As shown in the task figure, the main target scenario is code completion (denoted as `BigCodeBench-Complete`), where LLMs are required to finish the implementation of a function based on detailed instructions in the docstring. However, considering downstream applications such as multi-turn dialogue, users may describe requirements in a more conversational and less verbose manner. This is where instruction-tuned LLMs are beneficial, as they are trained to follow natural-language instructions and generate code snippets accordingly. To test if models can truly understand human intents and translate them into code, we create `BigCodeBench-Instruct`, a more challenging variant of BigCodeBench designed to evaluate instruction-tuned LLMs.

## 
	[
		
	](https://huggingface.co#where-do-the-tasks-come-from-🤔)
	
		Where do the tasks come from? 🤔
	

We guarantee the quality of the tasks in BigCodeBench through a systematic "Human-LLM collaboration process." We start with [ODEX](https://github.com/zorazrw/odex) as the "seed dataset," which contains short but realistic human intents and corresponding Python one-liners from Stack Overflow. We use GPT-4 to expand these one-liners into comprehensive function-level tasks.

Next, 20 human experts—most with over 5 years of Python programming experience—voluntarily guide GPT-4 in an execution-based sandbox. They continually instruct it to refine the synthesized tasks and add test cases. The tasks and test cases are then examined in a local environment, pre-evaluated on other LLMs, and cross-checked by 7 additional human experts to ensure their quality.

To assert overall quality, the authors sample tasks for 11 human experts to solve, achieving an average human performance of 97%.

## 
	[
		
	](https://huggingface.co#how-well-do-llms-perform-on-bigcodebench-📊)
	
		How well do LLMs perform on BigCodeBench? 📊
	

We host the BigCodeBench leaderboard on both [Hugging Face Space](https://huggingface.co/spaces/bigcode/bigcodebench-leaderboard) and [GitHub Pages](https://bigcode-bench.github.io/). Here, we use the Hugging Face leaderboard as an example.

Interestingly, we observe that instruction-tuned LLMs like GPT-4 can omit essential import statements in the long prompts of `BigCodeBench-Complete`, leading to task failures due to missing modules and constants. This behavior, called "model laziness", is discussed in the [community](https://community.openai.com/t/why-i-think-gpt-is-now-lazy/534332).

__Compared to human performance, LLMs perform significantly lower on  BigCodeBench-Complete and even lower on BigCodeBench-Instruct.__ The best model (GPT-4o) achieves a calibrated Pass@1 of 61.1% on 

`BigCodeBench-Complete` and 51.1% on `BigCodeBench-Instruct`. Additionally, there is a notable performance gap between closed and open LLMs.While Pass@1 is a good metric for overall performance, it is not detailed enough to compare models directly. Inspired by [Chatbot Arena](https://lmsys.org/blog/2023-05-03-arena/), we use Elo rating to rank models on `BigCodeBench-Complete`. This method, originally used in chess, ranks players based on their game performance. We adapt it to programming tasks, treating each task as a game and each model as a player. The Elo rating updates are based on game outcomes and expectations, using task-level calibrated Pass@1 (0% or 100%) and excluding ties. Starting with an initial Elo rating of 1000, we fit it using maximum likelihood estimation and bootstrap with 500 iterations to get final scores. __We find that GPT-4o outperforms other models by a large margin, with DeepSeekCoder-V2 in the second tier.__

To help the community understand model performance on each task, we track solve rates, measured by calibrated Pass@1. On `BigCodeBench-Complete`, 149 tasks remain unsolved by all models, while 6 tasks are completely solved. For `BigCodeBench-Instruct`, 278 tasks remain unsolved and 14 tasks are fully solved by all models. The significant number of unsolved tasks and the small number of fully solved tasks show that BigCodeBench is a challenging benchmark for LLMs.

## 
	[
		
	](https://huggingface.co#great-so-how-can-i-evaluate-my-model-on-bigcodebench-🛠️)
	
		Great! So, how can I evaluate my model on BigCodeBench? 🛠️
	

We make BigCodeBench easily accessible to the community by providing a simple and user-friendly evaluation framework, which can be downloaded via [PyPI](https://pydigger.com/pypi/bigcodebench). The prototype of the evaluation framework is based on [EvalPlus](https://github.com/evalplus/evalplus) for the HumanEval+ and MBPP+ benchmarks. However, as our benchmark has tasks with much more diverse library dependencies than EvalPlus, we build less resource-constrained execution environment, and adapt it for `unittest` in the test harness of BigCodeBench.

To facilitate the evaluation, we provide pre-built Docker images for [ code generation](https://hub.docker.com/r/bigcodebench/bigcodebench-generate) and 

[. Check out our](https://hub.docker.com/r/bigcodebench/bigcodebench-evaluate)

*code execution*[GitHub repository](https://github.com/bigcode-project/bigcodebench)to find more details on how to use the evaluation framework.

### 
	[
		
	](https://huggingface.co#setup)
	
		Setup
	

```
# Install to use bigcodebench.evaluate
pip install bigcodebench --upgrade
# If you want to use the evaluate locally, you need to install the requirements
pip install -I -r https://raw.githubusercontent.com/bigcode-project/bigcodebench/main/Requirements/requirements-eval.txt
# Install to use bigcodebench.generate
# You are strongly recommended to install the [generate] dependencies in a separate environment
pip install bigcodebench[generate] --upgrade
```
### 
	[
		
	](https://huggingface.co#code-generation)
	
		Code Generation
	

You are suggested to use `flash-attn` for generating code samples.

```
pip install -U flash-attn
```
To generate code samples from a model, you can use the following command:

```
bigcodebench.generate \
    --model [model_name] \
    --subset [complete|instruct] \
    --greedy \
    --bs [bs] \
    --temperature [temp] \
    --n_samples [n_samples] \
    --resume \
    --backend [vllm|hf|openai|mistral|anthropic|google] \
    --tp [gpu_number] \
    [--trust_remote_code] \
    [--base_url [base_url]]
```
The generated code samples will be stored in a file named `[model_name]--bigcodebench-[instruct|complete]--[backend]-[temp]-[n_samples].jsonl`.

### 
	[
		
	](https://huggingface.co#code-post-processing)
	
		Code Post-processing
	

LLM-generated text may not be compilable code as it includes natural language lines or incomplete extra code.
We provide a tool namely `bigcodebench.sanitize` to clean up the code:

```
# 💡 If you want to store calibrated code in jsonl:
bigcodebench.sanitize --samples samples.jsonl --calibrate
# Sanitized code will be produced to `samples-sanitized-calibrated.jsonl`
# 💡 If you do without calibration:
bigcodebench.sanitize --samples samples.jsonl
# Sanitized code will be produced to `samples-sanitized.jsonl`
# 💡 If you are storing codes in directories:
bigcodebench.sanitize --samples /path/to/vicuna-[??]b_temp_[??]
# Sanitized code will be produced to `/path/to/vicuna-[??]b_temp_[??]-sanitized`
```
### 
	[
		
	](https://huggingface.co#code-evaluation)
	
		Code Evaluation
	

You are strongly recommended to use a sandbox such as [docker](https://docs.docker.com/get-docker/):

```
# Mount the current directory to the container
docker run -v $(pwd):/app bigcodebench/bigcodebench-evaluate:latest --subset [complete|instruct] --samples samples-sanitized-calibrated
# ...Or locally ⚠️
bigcodebench.evaluate --subset [complete|instruct] --samples samples-sanitized-calibrated
# ...If the ground truth is working locally (due to some flaky tests)
bigcodebench.evaluate --subset [complete|instruct] --samples samples-sanitized-calibrated --no-gt
```
## 
	[
		
	](https://huggingface.co#whats-next)
	
		What's next?
	

We share a long-term roadmap to address the limitations of BigCodeBench and sustainably build with the community. Our goal is to provide the community with the most open, reliable, and scalable evaluations to truly understand the fundamental capabilities of LLMs for programming and pinpoint ways to unleash their power. Specifically, we plan to enhance the following aspects of BigCodeBench:

- **Multilingualism**: Currently, BigCodeBench is Python-only and cannot be easily extended to other programming languages. Since function calls are mostly language-specific, finding packages or libraries with the same functionalities in languages other than Python is challenging.
- **Rigorousness**: While we achieve high test coverage for ground-truth solutions in BigCodeBench, it does not guarantee that- *all*code solutions generated by LLMs will be correctly assessed against existing test cases. Previous works like EvalPlus have attempted to extend limited test cases by augmenting input-output pairs via LLM- and mutation-based strategies. However, adapting EvalPlus to the test harness in BigCodeBench is challenging. While EvalPlus emphasizes the input-output assertions, most of test harnesses in BigCoeBench require non-trivial configurations (e.g., mock patching) to examine expected program behaviors during runtime.
- **Generalization**: A key question is, "How well do the models generalize to unseen tools and tasks?" Currently, BigCodeBench covers common libraries and daily programming tasks. Benchmarking models on programming tasks that use emerging libraries like- [transformers](https://github.com/huggingface/transformers)and- [langchain](https://github.com/langchain-ai/langchain)would be more interesting.
- **Evolution**: Libraries can become obsolete or be updated, meaning the source code data for model training will constantly evolve. Models may not memorize function calls from deprecated library versions, posing a challenge for any tool-dependent programming benchmarks to correctly examine model capabilities without periodic updates. Another related concern is test set contamination due to evolving training data.
- **Interaction**: Recent interest focuses on the concept of- *LLMs as Agents*, which is seen as a path toward artificial general intelligence. Specifically, LLMs will be grounded in a less constrained sandbox environment, where they can interact with applications such as web browsers and terminals. This environment can help unlock capabilities like- [self-debugging](https://arxiv.org/pdf/2304.05128)and- [self-reflection](https://arxiv.org/abs/2303.11366).

We are excited to see the community's feedback and contributions to building BigCodeBench in the long run 🤗

## 
	[
		
	](https://huggingface.co#resources)
	
		Resources
	

We open-source all the artifacts of BigCodeBench, including the tasks, test cases, evaluation framework, and leaderboard. You can find them as follows:

If you have any questions or suggestions, please feel free to open an issue in the repository or contact us via [terry.zhuo@monash.edu](mailto:terry.zhuo@monash.edu) or [contact@bigcode-project.org](mailto:contact@bigcode-project.org).

## 
	[
		
	](https://huggingface.co#citation)
	
		Citation
	

If you find our evaluations useful, please consider citing our work

```
@article{zhuo2024bigcodebench,
  title={BigCodeBench: Benchmarking Code Generation with Diverse Function Calls and Complex Instructions},
  author={Zhuo, Terry Yue and Vu, Minh Chien and Chim, Jenny and Hu, Han and Yu, Wenhao and Widyasari, Ratnadira and Yusuf, Imam Nur Bani and Zhan, Haolan and He, Junda and Paul, Indraneil and others},
  journal={arXiv preprint arXiv:2406.15877},
  year={2024}
}
```
