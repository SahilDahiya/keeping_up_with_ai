---
title: Accelerate your Vision Pipelines with the new NVIDIA Nemotron Nano 2 VL Model
  on Fireworks
kind: blog
topic: models
subtopic: multimodal
secondary_topics:
- inference/optimization
summary: NVIDIA Nemotron Nano2 VL combines the hybrid Mamba-Transformer Nemotron LLM
  with a CRADIOH-V2 vision encoder and video token compression; in an invoice-processing
  benchmark on Fireworks it hit 90%+ extraction accuracy on fields like invoice number
  and date via semantic (not pure-OCR) document understanding.
triage: null
skip_reason: null
source: fireworks
url: https://fireworks.ai/blog/nvidia-nemotron-nano2vl
author: null
published: '2025-10-27'
fetched: '2026-08-12T06:30:43Z'
classifier: claude
taxonomy_rev: 2
words: 786
content_sha256: c41cc748c6e54c94d3503d0144512701a6cd14da22251ebe78214bab94b982f4
---

# Accelerate your Vision Pipelines with the new NVIDIA Nemotron Nano 2 VL Model on Fireworks

Exciting news for vision AI! Fireworks is proud to offer Day-0 support for the highly anticipated NVIDIA Nemotron Nano2 VL, a 12B multimodal reasoning model for accelerating your document intelligence and video understanding applications.

NVIDIA Nemotron Nano2 VL, the latest innovation in the [NVIDIA Nemotron](https://www.nvidia.com/en-us/ai-data-science/foundation-models/nemotron/) family, is a vision language model (VLM) designed to push the boundaries of intelligent document processing, AI assistant video understanding, video captioning, multi-modal agentic workflows, and more. It enables AI assistants to extract, interpret, and act on information across text, images, tables, and video. VLMs are built by combining an LLM with a vision encoder, enabling the LLM with eyes. VLMs often require a more complex architecture to integrate across multiple modalities. With [Fireworks' Multimedia](https://fireworks.ai/usecases/multimedia), developers can effortlessly unlock insights across various modalities from VLMs like NVIDIA Nemotron Nano2 VL, bypassing the complexities of unstructured multi-domain workflows. In an invoice analysis example, Nemotron Nano2 VL surpassed over 90% accuracy, resulting in a high quality output. In the scenario, the Nemotron Nano2 VL model automated the entire process of data extraction, classification, and summarization, eliminating the need for tedious, time-consuming manual evaluation.

With its high accuracy, compact model footprint, and multimodal capabilities, Nemotron Nano 2 VL seamlessly extracts and comprehends information from complex documents, videos and images. For intelligent document assistants, this includes diverse inputs from text-base documents to images, charts and graphs, making it an ideal solution for automating document workflows across industries like finance, healthcare, legal, and government. In multi-image processing, it assists with tasks such as captioning and content curation, making it ideal for product catalog parsing and image search. Lastly it is optimal for multimodal and agentic pipelines that may need image aware retrieval and tool use.

The efficient model combines the optimized hybrid Mamba-Transformer architecture from the [Nemotron family](https://arxiv.org/pdf/2504.03624) for the LLM with a Vision Encoder based on CRADIOH-V2, and an efficient video search token compression model.

It provides three key features:

- •High Accuracy: Nemotron Nano 2 VL is trained with NVIDIA curated high quality synthetic data to achieve leading accuracy for character recognition, chart reasoning,visual Q&A, video understanding, and document intelligence.
- •High Efficiency: Using the hybrid Mamba-Transformer architecture compared to the previous Nemotron VL Model with Efficient Video Sampling (EVS), developers can process longer videos in the same time, lowering total cost of inference
- •Flexibility with Open Source: It is an OSS model that can be fine tuned to your specific use case rather than locked into one specific workload. Additionally, 11M samples of multimodal training data and model training recipe are openly available.

Check out the figure below showcasing a variety of benchmarks from NVIDIA on the Nemotron Nano2 model.

We're excited to announce that the latest Nemotron Nano VL model is now available on Fireworks! We've prepared a [comprehensive cookbook](https://github.com/fw-ai/cookbook/blob/main/learn/vlm/nvidia-nemotron-vl/NVIDIA-Nemotron-v2-VL-cookbook.ipynb) to help you explore its performance. The model is optimized for things like OCR(optical character recognition) in document processing. Unlike older OCRs systems that simply convert an image to text, a VLM understands the semantic context and spatial relationships between elements. In this process the model will analyze the image and distinguish between the characters and the background. The model used the pattern found in the image to identify the characters and convert them into machine readable text. This example demonstrated NVIDIA Nemotron Nano 2 VL on Fireworks being used for invoice processing and document intelligence. The main task was to extract invoice numbers, dates, line items, and totals. The table below shows our test result success rates for parsing the invoices. With NVIDIA Nemotron we were able to achieve overall quality rates in the 90s.

| Test | Quality Rate | 
|---|---|
| Invoice Number | 100% | 
| Date | 100% | 
| Item Count | 100% | 
| Total Amount | 63.2% | 
| Overall | 90.8% (19/20 Successful Extractions) | 

Other use cases that could benefit from a scenario similar to invoice processing include account payable automation, expense management and receipt processing, financial document digitization, and compliance and audit workflows.

**Next Steps:**

Ready to deploy this solution in production? Try:

1. Test the cookbook with your domain-specific documents
2. Add validation rules for total amount extraction
3. Implement confidence-based routing for human review
4. Scale to multi-page documents (contracts, statements, purchase orders)

VLMs like Nemotron can drastically outperform manual document analysis by offering superior speed, accuracy, and scale, as they holistically understand both the text and the context of these complex documents. This automation eliminates human error, significantly lowering operational costs, and freeing staff to focus on more strategic work.

Automate your document intelligence and multi-image processing workflows today by deploying [Nemotron Nano 2 VL](https://app.fireworks.ai/models/fireworks/nemotron-nano-v2-12b-vl) on Fireworks. For further questions, reach out on Discord or via [inquires@fireworks.ai](mailto:inquires@fireworks.ai).
