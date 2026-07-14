---
title: DeepSeek-OCR and the Unreasonable Usefulness of Compression
topic: models
subtopic: multimodal
secondary_topics: []
summary: Explains DeepSeek-OCR and why compression can be useful for multimodal model
  workflows.
source: baseten
url: https://www.baseten.co/blog/deepseek-ocr-and-the-unreasonable-usefulness-of-compression/
author: Alex Ker; Dhruv Singal
published: '2025-10-23'
fetched: '2026-07-11T04:07:04Z'
classifier: codex
taxonomy_rev: 1
words: 988
content_sha256: 09f450d19a9c6cf4eb858196faf4f3250acc184753a862daeb57c0ebd1367e96
triage: keep
skip_reason: null
---

# DeepSeek-OCR and the Unreasonable Usefulness of Compression

![DeepSeek-OCR & the Unreasonable Usefulness of Compression](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1761251399-deepseek-ocr.png%3Fauto%3Dformat%26fit%3Dcrop%26h%3D630%26w%3D1200&w=3840&q=100)

Why DeepSeek-OCR's 10x compression unlocks faster, cheaper intelligence, and how to run it performantly on Baseten in <10min

Is a pixel worth a thousand words? What if we've been feeding AI the wrong type of data all along?

According to DeepSeek's new OCR paper, the answer might be yes. In this post, we’ll go over the performance and implications of the newest DeepSeek OCR model, and how to deploy this small yet mighty model via Truss to run reliable, scalable inference on Baseten.

You may think that DeepSeek-OCR is just another OCR (Optical Character Recognition) model. While it’s a great OCR model, its true importance comes from its extremely efficient compression.

## Compression as the secret ingredient to intelligence

LLMs today process text by breaking it into "tokens", small chunks of characters; DeepSeek-OCR takes a different approach. It processes the image of text directly, requiring 10x fewer visual tokens than text tokens, which means DeepSeek-OCR compresses information 10x more efficiently than the text, with decoding precision of 97% (A minimal loss of information).

In building a compressor, researchers found this process is [linearly correlated with intelligence in LLMs](https://arxiv.org/abs/2404.09937). Ilya Sutskever, the co-founder of OpenAI, similarly shared in his [talks](https://www.youtube.com/watch?v=AKMuA_TVz3A) that optimizing specific compression goals like next-pixel or next-token predictions actually produce useful representations for downstream tasks. In other words, compression is what is necessary in creating intelligent models generally.

![DeepSeek-OCR’s leading in compression benchmarks](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1761244169-fig1.png%3Fauto%3Dformat%26w%3D1200&w=3840&q=75) DeepSeek-OCR’s leading in compression benchmarks

DeepSeek-OCR’s leading in compression benchmarks## Performance and DeepSeek-OCR in the real world

Because DeepSeek-OCR is so small yet efficient, it could process 200k+ pages/day on a single GPU or 33M pages/day on 20 nodes of A100. In fact, a team has extracted datasets (table/charts) across 500k AI arXiv papers for only a thousand dollars: [https://x.com/askalphaxiv/status/1980722479405678593.](https://x.com/askalphaxiv/status/1980722479405678593)

The implications of the DeepSeek-OCR are broad. Here are my top three:

- It could be used for scalable training data generation. Imagine quality labeled data at a fraction of the current cost and time for your fine-tuning requirements.
- Moving towards Infinite (or near-infinite) context windows and memory. With efficient compression, this model could ingest document libraries as context–potentially changing how RAG works. Visual language document retrieval, question and answering would produce less hallucinations by storing visual representations of documents.
- We could move towards real-time intelligence because fast inference could enable real-time computer-use agents for the first time. Imagine AI that can livestream and process your entire screen as context fast and cheaply to determine tool use.

## How to deploy DeepSeek-OCR performantly on Baseten

I wanted to test DeepSeek-OCR on one of OCR’s hardest challenges: reading a doctor’s handwriting from the legibility of a college student to the chaos of a practicing physician(powered by[ Baseten](https://www.linkedin.com/company/baseten/) inference on a 40 GB H100 MIG). 

Let’s walk through how we packaged DeepSeek-OCR into a Truss that is then served on Baseten dedicated serverless infrastructure, a process that is similarly applicable for other OCR models.

Baseten supports vLLM, a popular open source library for LLM inference and serving, which is also supported for this model as specified in the DeepSeek-OCR [github repo](https://github.com/deepseek-ai/DeepSeek-OCR). 

We start with the `config.yaml` file for dependencies and setup. I first copied the list of pip commands from install instructions from DeepSeek-OCR’s ``README.md``. I skipped the first line (`torch`, `torchvision`, and `torchaudio`) because installing vLLM will pull in its own torch dependencies and added the second line of cloning the DeepSeek-OCR repo into the Baseten node. 

The specific line 4: `apt...` and line 2: custom image `baseten/cuda_python:12.4.1-dev` were added to build` flash-attn==2.7.3 `that the model needed. This took a bit of debugging by examining the Baseten deployment logs. Since the vLLM 0.8.5 tag source corresponded with the 12.4.1 cuda dev, we’re able to grab the correct image from: [https://docs.baseten.co/development/model/base-images](https://docs.baseten.co/development/model/base-images). 

Note: As of October 23rd, vLLM [rolled out support](https://docs.vllm.ai/projects/recipes/en/latest/DeepSeek/DeepSeek-OCR.html#running-deepseek-ocr) upstream for DeepSeek-OCR, so not specifying the base_image will still work. But this is a good process to know how to debug configs generally on Baseten.

For resources, we specify H100_40G, a fractional H100 GPU that brings the Hopper architecture efficiently to smaller models.

Our `config.yaml`

```
1base_image:  
2  image: baseten/cuda_python:12.4.1-dev
3build_commands:  
4  - apt-get update && apt-get install -y python3-dev  
5  - git clone https://github.com/deepseek-ai/DeepSeek-OCR.git /DeepSeek-OCR  
6  - pip install -r /DeepSeek-OCR/requirements.txt  
7  - pip install vllm==0.8.5  
8  - pip install flash-attn==2.7.3 --no-build-isolation
9python_version: py310
10model_metadata:  
11  example_model_input:    
12    image_url: https://example.com/image.jpg    
13    prompt: <image>\n<|grounding|>Convert the document to markdown.  
14    model_name: DeepSeek OCR
15model_name: deepseek-ocr-latest
16resources:  
17  accelerator: H100_40GB  
18  cpu: "2"  
19  memory: 16Gi  
20  use_gpu: true
```
The next step is completing the [model.py](https://github.com/basetenlabs/truss-examples/blob/main/deepseek-ocr/model/model.py) which includes the `load` and `predict`. Since we clone the original DeepSeek-OCR in our build commands, we can import some functions from the [run_dpsk_ocr_image.py](https://github.com/deepseek-ai/DeepSeek-OCR/blob/main/DeepSeek-OCR-master/DeepSeek-OCR-vllm/run_dpsk_ocr_image.py). We then construct `load` to match the DeepSeek image processor and initialize their async engine and `predict` to preprocess the image and pass the result through the processor.

The last step is simply trussing the model with `truss push --publish` in the truss CLI and you should have the deployment visible in your Baseten dashboard. In the example repo, I’ve also included `test_document_ocr.py` to hit the deployed endpoint and `visualizer.py` to visualize (draw bounding boxes and label text) the OCR output mirroring the official implementation. You can see the returned result of the inference call **in under a second **from Baseten.

![Result of DeepSeek-OCR on Doctor’s note](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1761244690-screenshot-2025-10-20-at-11-47-35-pm.png%3Fauto%3Dformat%26w%3D1200&w=3840&q=75) Result of DeepSeek-OCR on Doctor’s note

Result of DeepSeek-OCR on Doctor’s note## The takeaway

The shift from text tokens to visual tokens isn't just a technical optimization—it's a fundamental rethinking of how we feed information to AI systems. DeepSeek-OCR proves that highly compressed data representations could be useful in a number of ways.

Whether you're building RAG pipelines, fine-tuning models without labelled data, or building real-time AI agents, consider trying out DeepSeek-OCR. You can spin this up on Baseten in <10 minutes and start experimenting with our sample code [here](https://github.com/basetenlabs/truss-examples/tree/main/deepseek-ocr).
