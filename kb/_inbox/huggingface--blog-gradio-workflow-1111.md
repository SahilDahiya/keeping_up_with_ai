---
title: Rebuilding AUTOMATIC1111 with Gradio Workflow
kind: blog
topic: null
subtopic: null
secondary_topics: []
summary: null
triage: null
skip_reason: null
source: huggingface
url: https://huggingface.co/blog/gradio-workflow-1111
author: Yuvraj Sharma; Abubakar Abid
published: '2026-09-10'
fetched: '2026-09-11T06:17:21Z'
classifier: null
taxonomy_rev: 2
words: 618
content_sha256: bf2933423a3da5e9e2d982031dba726cd66b95a3a81b740ac722f800fe32fccb
---

# Rebuilding AUTOMATIC1111 with Gradio Workflow

[Text-to-Video •  35B • Updated   •  221k  •  298](https://huggingface.co/FastVideo/FastVideo-FastH3-4-step-Preview-v1-VSA-DataFree)  

#### FastVideo/FastVideo-FastH3-4-step-Preview-v1-VSA-DataFree

![](https://cdn-avatars.huggingface.co/v1/production/uploads/63565cc56d7fcf1bedb7d347/g6wWXLryVUwXcaKTuRerh.png) 

Published
					September 10, 2026 

  Upvote 

 8

In our [last post](https://huggingface.co/blog/gradio-workflow-guide), we built five small [stable-diffusion-webui](https://github.com/AUTOMATIC1111/stable-diffusion-webui). In this post we walk you through **Workflow1111**, where we have rebuilt most of AUTOMATIC1111's feature set as a single workflow canvas.
You can run any of these pipelines by signing in with your Hugging Face account or providing an access token. Once you sign in, the model calls use your own quota.

## 
	
		
	
	
		What's on the canvas
	

### 
	
		
	
	
		Text-to-image
	

### 
	
		
	
	
		Hi-resolution fix
	

### 
	
		
	
	
		Image-to-image
	

That same Kontext node doubles as the image-to-image tab. Upload an image, describe the change you want, and it returns the edited image.

### 
	
		
	
	
		Let an LLM write the prompt
	

### 
	
		
	
	
		Read an image back into a prompt
	

### 
	
		
	
	
		Detection to inpaint mask
	

The drawing and the mask creation both happen locally with Pillow and NumPy. Only the detection call leaves the machine.

### 
	
		
	
	
		Prompt matrix
	

### 
	
		
	
	
		Upscale and background removal
	

### 
	
		
	
	
		Annotators
	

### 
	
		
	
	
		PNG Info
	

### 
	
		
	
	
		Image-to-video
	

## 
	
		
	
	
		Running models on your own GPU
	

So far every model call has gone to someone else's hardware, through Inference Providers or a Space. That's why you can build and run something like Workflow1111 without a GPU of your own.

## 
	
		
	
	
		Every output is an API
	

## 
	
		
	
	
		Where this sits next to ComfyUI
	

The result is a multi-model pipeline that people can open in a browser, sign into, use right away, and call from code.

## 
	
		
	
	
		Build your own
	

Workflow1111 has 73 nodes, but it started with just this:


`gr.Workflow` graphs and hinted at what it would take to build something as complex as AUTOMATIC1111's Let's walk the canvas.

Let's go through the pipelines one by one.

The whole app comes down to one bound function:

- **A node can be hardware you don't own.** It can run through[Inference Providers](https://huggingface.co/docs/inference-providers/index) , call any Space on the Hub or any API, or pull from a dataset. That's how Workflow1111 runs without a GPU of its own.
- **Every output becomes a typed REST endpoint.** The endpoints are generated from the graph.
- **Visitors can run workflows under their own identity.** Turn on[OAuth](https://huggingface.co/docs/hub/spaces-oauth) , share the public URL, and anyone can sign in and use the app without installing anything.
- **Mix models and modalities on the same canvas.** Diffusion models, LLMs, VLMs, detectors, and video models can all be part of the same workflow.
- **Need something custom? Write a function.** A custom node is a Python function, so it can do whatever Python can.

 Image-Text-to-Video •  33B • Updated   •  5.08M  •  5.13k 

 Image-Text-to-Text •  8B • Updated   •  7.68M  •  1.7k 

 Text Generation •  4B • Updated   •  3.58M  •  958 

 Image-to-Video •  Updated   •  10.9k  •  801 

 Image-to-Image •  12B • Updated   •  253k  •  2.8k 

 Object Detection •  41.6M • Updated   •  681k  •  973 

 Image Classification •  86.6M • Updated   •  5.77M  •  996 

🎬

 6

4-step MiniMax-H3 — video with a matching soundtrack

🐢

 966

remove background from any image

😻

 627

Upscale images by 4× with a single click

🎨

 1

Automatic1111-style studio on one gr.Workflow canvas

More Articles from our Blog

gradioworkflowstutorial

  45

 August 25, 2026 comfyuigradiospaces

  98

 January 14, 2024 Really impressive breakdown the part that stands out most is how the graph structure gives you free parallelism (the prompt-matrix and interrogate examples) without any extra orchestration code. The mix of fn, model, and space node types on one canvas also makes the ComfyUI comparison land well: you get custom-node flexibility from plain Python, but zero-code REST/MCP endpoints for free. Curious how complex a canvas can get before performance or maintainability becomes a concern has anyone pushed past 73 nodes
