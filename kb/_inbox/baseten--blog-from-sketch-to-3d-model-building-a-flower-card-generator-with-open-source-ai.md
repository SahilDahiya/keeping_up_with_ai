---
title: 'From Sketch to 3D Model: Building a flower card generator with open source
  AI'
kind: blog
topic: null
subtopic: null
secondary_topics: []
summary: null
triage: null
skip_reason: null
source: baseten
url: https://www.baseten.co/blog/from-sketch-to-3d-model-building-a-flower-card-generator-with-open-source-ai
author: Alex Ker
published: '2025-10-10'
fetched: '2026-11-12T06:10:38Z'
classifier: null
taxonomy_rev: 2
words: 1363
content_sha256: 591126a1bcf51891317a4971052116d1643e460904a2bdab4dc27e91b1df9b68
---

# From Sketch to 3D Model: Building a flower card generator with open source AI

AI engineering
# From Sketch to 3D Model: Building a flower card generator with open source AI

Learn how to transform Autodesk's WaLa research model into a production API that converts sketches into shareable 3D flower cards using Truss and Netlify


- Authors
- Date
- October 10, 2025

TLDR

In a world saturated with 2D image generation, there's something uniquely satisfying about creating 3D objects. They can break free from the screen, ready to be rotated, printed, or dropped into virtual worlds and games.

I'm not a 3D designer nor a particularly talented artist. That's why I was amazed when I discovered Autodesk's WaLa model on GitHub. This model can transform simple sketches or images instantly into 3D renderings. To experiment with it, I decided to build a 3D flower card application– flowers turned out to be perfect for showcasing WaLa's abilities.

In this tutorial, you'll learn how to serve Autodesk's cutting-edge model as a scalable API. We'll transform 2D drawings into detailed 3D objects on Baseten and serve the results as shareable links hosted on Netlify.

Instead of focusing on each line of code, I'll cover the high-level architecture. We'll explore how to turn a complex frontier open source model like WaLa into an API via Truss. Then we'll build a complete web application around it.

Everything will be available open source in a GitHub repository you can experiment with.

WaLa (Wavelet-based Latent Diffusion) is Autodesk's breakthrough model for single-view 3D reconstruction. Given a single 2D image of an object, it generates a complete 3D model using wavelet-based diffusion in latent space.

What makes WaLa special is its ability to work with just one image. No need for multiple angles or complex setups. It generates high-quality OBJ meshes, a simple format that stores 3D geometric objects, with proper topology that are ready for 3D printing or game engines.

The inference is surprisingly fast, taking only a few seconds on a single H100 MIG, or half a H100. While there are many variants (WaLa-SV), we'll use the single-view model, which I found to produce better quality results than the sketch model.

First, let's look at what we're working with. The WaLa repository the following structure:

WaLa/

├── src/

│ ├── latent\_model/

│ ├── diffusion\_modules/

│ └── model\_utils.py

├── configs/

└── requirements.txt

The challenge is that the repo is designed for research, not API serving. It expects command-line usage, has complex dependencies, and needs CUDA compilation. So this is where truss comes in. Truss is an open source framework that packages ML models for production deployment. It handles the complexity of containerization, dependencies, and scaling. Let’s take a look at how we could create a truss for this model.

Truss requires a specific structure as specified below:

autodesk-wala-singleview-to-3d/

├── model/

│ └── model.py # Your model wrapper

├── packages/ # Vendored dependencies

│ └── src/ # WaLa source code

├── config.yaml # Truss configuration

└── requirements.txt # Python dependencies

The key insight is vendoring, or copying the source code of a third-party library directly into your project's repository, rather than relying on a package manager to download and manage it dynamically. In other words, let’s put the entire WaLa source code into `packages/`.

The heart of Truss is the `Model` class. It implements two key methods. Only pseudocode is provided below for concision.

python

```
class Model:   
  def load(self):       
    """Called once when the model server starts"""       
    # 1. Add vendored code to Python path       
    # 2. Import WaLa modules       
    # 3. Download model from HuggingFace       
    # 4. Initialize model and transforms   
  def predict(self, model_input):       
    """Called for each inference request"""       
    # 1. Decode base64 image       
    # 2. Preprocess with transforms       
    # 3. Run inference using imported modules       
    # 4. Return base64-encoded OBJ
```
The `config.yaml` tells Truss how to deploy:

yaml

```
model_name: ADSKAILab/WaLa-SV-1B
python_version: py311
resources: accelerator: H100_40GB 
  use_gpu: true
requirements_file: ./requirements.txt # taken directly from the WaLa repo
system_packages: 
  - libgl1-mesa-glx    # OpenGL for 3D processing 
  - libegl1-mesa 
  - libglib2.0-0
secrets: 
  hf_access_token: null  # Set in Baseten dashboard
```
The configuration decisions were important to get right. I chose the H100MIG GPU because WaLa needs a good amount of memory for its diffusion process and since it’s only a 1B parameter model, a single H100MIG (half a H100) is sufficient. The system packages might seem random, but they're essential OpenGL libraries that WaLa uses for mesh processing. Rather than hardcoding credentials, I used Baseten's secrets management to store the HuggingFace token securely.

With the prerequisites handled, deployment is simple:

bash

```
cd autodesk-wala-singleview-to-3d
truss push --publish
```
The beauty of Truss is that it handles all the complex infrastructure work. It builds a Docker container with all your dependencies. It compiles those tricky CUDA extensions. It sets up a production-grade model server and deploys everything to Baseten's GPU infrastructure. It even configures auto-scaling based on load, so your API can handle traffic spikes. After about 5 minutes, you'll get a production endpoint. The next time you use an endpoint like this, cold-start times will be much faster as the model is now cached.

Once deployed, testing is straightforward. You send a POST request with a base64-encoded image. You get back a base64-encoded OBJ file. There are just a couple of parameters to play with. The scale parameter (I found 1.8 works best for most images) and seed if you want reproducible results. The API typically responds in a few seconds with a complete 3D model.

The repo includes a [test.py](https://github.com/AlexKer/doodle-bloom/blob/main/autodesk-wala-singleview-to-3d/test.py) that demonstrates this perfectly - it sends a sample flower image and returns a complete 3D model you can view and download.

Now that we have a 3D generation API, let's build a complete flower card application. The architecture consists of three main components:

The drawing interface lives in `interactive_sketch.py` and provides a delightful web experience. Users can draw flowers with adjustable brush sizes. They can add personalized messages like "Happy Birthday Mom!" and sign their name.

With one click, their sketch transforms into a 3D model. They automatically get a shareable URL. Behind the scenes, the Python server acts as a proxy between the browser and your Baseten API. The interface is designed to be touch-friendly and works seamlessly on both desktop and mobile.

The Netlify component provides persistent storage and beautiful 3D viewing through this flow:

Netlify provides serverless functions, which means you can simply create functions as files within a /netlify/functions folder locally, push this folder up via the Netlify CLI, and use these functions as endpoints.

For data storage, I used Netlify's built-in Neon database integration. This automatically provisions a Postgres database and configures all the connection details - no manual setup required.  In this project, I created 2 functions `get-flowers.ts` and `store-flowers.ts`, used for uploading the 3D model and retrieving the 3D models from the database for viewing, respectively.

The 3D viewer is where the magic happens. When someone opens a flower link, they're greeted with an auto-rotating 3D model bathed in beautiful pink gradient materials. It's genuinely delightful to watch.

On mobile, they can pinch to zoom and swipe to rotate. This makes it feel like they're holding the flower in their hands. The personalized message appears in an elegant card overlay. There's a download button if they want to 3D print their gift.

The share functionality uses the device's native sharing, so sending it to friends feels natural. Best of all, the entire viewer is a [single HTML file](https://github.com/AlexKer/doodle-bloom/blob/main/netlify-viewer-3d/index.html) using Three.js–it loads instantly even on slow connections.

We've successfully transformed Autodesk's research model into a production-ready API. This powers a delightful flower card application that can host 3D objects generated with the WaLa model from a single sketch. The combination of Truss for model packaging, Baseten for scalable GPU infrastructure, and Netlify for serverless hosting creates a robust system.

What you learned here can be applied universally to virtually any open-source model you find on GitHub or Hugging Face. Whether you're working with diffusion models, transformers, or custom architectures, I hope this streamlines your path from research code to production API to serve millions of users.

The complete code for this project is available at [<u>github.com/alexker/doodle-bloom</u>](https://github.com/alexker/doodle-bloom). I'd love to see what you create with it!
