---
title: One compute platform for end-to-end training at Markov Robotics | Modal Blog
kind: blog
topic: infra-platform
subtopic: gpu-clusters
secondary_topics:
- models/training
- product-engineering/case-studies
summary: 'Case study on Markov Robotics training a video-and-proprioception-conditioned
  world model for zero-shot robot manipulation entirely on Modal: fanning out preprocessing
  of hundreds of terabytes of video with Modal Functions and `.spawn_map` across thousands
  of CPU/GPU containers (up to 500 GPUs at once), with per-stage hardware selection
  to keep cost proportional to each step''s needs.'
triage: null
skip_reason: null
source: modal
url: https://modal.com/blog/markov-case-study
author: null
published: '2026-09-04'
fetched: '2026-10-27T06:11:22Z'
classifier: claude
taxonomy_rev: 2
words: 1239
content_sha256: 74ebc0e25468c414aa3e55ed216437cc64b924f281ae6085daee26332c3813dc
---

# One compute platform for end-to-end training at Markov Robotics | Modal Blog

[Markov Robotics](https://www.markovrobotics.com/) was founded on the belief that robotics has an intelligence problem rather than a hardware problem. The company's long-term goal is abundant physical automation, on the reasoning that scaling humanity beyond Earth will require robots capable of real physical work. Its first act is zero-shot general-purpose dexterity: a single policy that performs any task on any robot body.

To do that, Markov is training a world model, and taking a new approach to get there. Their bet is that video already contains most of the physical reality a robot needs in order to act, and that conditioning the model on high-fidelity modalities like pressure and proprioception gives the policy a detailed internal representation of how the world changes over time.

Fewer than ten hours of robot data is enough for Markov's models to perform a wide range of complex manipulation tasks, in a field where comparable results need thousands of hours of collection. Getting there, however, requires infrastructure that could support a complex pipeline of compute, from processing massive amounts of data, to handling parallel training runs, to serving low-latency inference.

“We use Modal for pretty much all our compute, whether that's preprocessing, training models, or deploying them. Pretty much every phase of our process for robotics runs on Modal.”

## **Preparing hundreds of terabytes for training**

Before any training begins, Markov ingests hundreds of terabytes of video from robot episodes, human demonstration providers, and footage the team collects itself. All of it needs to get processed—segmenting videos, converting them into the format the world model expects, passing text instructions through an embedding model.

Markov writes each step as a [Modal Function](https://modal.com/docs/guide/functions) and fans it out with [`.spawn_map`](https://modal.com/docs/guide/batch-processing), scaling to thousands of containers across CPU and GPU nodes worldwide and to upwards of 500 GPUs at once on the heaviest stages. Work that could take a full day on traditional setups completes in twenty to thirty minutes on Modal, thanks to the ability to parallelize work over on-demand compute.

“Modal just feels like writing simple local scripts, but in the background it's orchestrating precompute across thousands of containers.”

With Modal, researchers can select the right GPU or CPU resources per function, so things like segmentation and reformatting can run on CPU, smaller models run on A100s, and heavier precompute models run on H100s. This keeps cost proportional to the work each stage actually requires. Plus, because much of the pipeline is I/O-bound, Markov uses Modal's input concurrency to overlap network and compute inside each container, which keeps accelerators from idling during downloads.

“Even if I rolled my own infrastructure here, it would cost weeks to a month to get right, and even then, no provider would give me the spot capacity to just say: run this function on any GPU, I’d have to spend more cycles just going out and procuring that reservation.”

This massively speeds up iteration across the team because they aren’t waiting on a reservation to become available or a prior job to finish.

"Nowhere in the world can you instantly get 500 GPUs to go process all of your data, and Modal is the only provider that lets us just write a python script and fan that out over compute and run everything in parallel."

## **Reaching maximum research velocity**

The team at Markov runs between 2 and 10 training runs at any given time. With Modal, infrastructure doesn’t slow down their process.

Training runs read straight from the same [Modal Volumes](https://modal.com/docs/guide/volumes) that the preprocessing step wrote to, so reads are fast and time isn’t wasted moving data around unnecessarily.

Experiments are reproducible by default. Since a [Modal Function](https://modal.com/docs/guide/functions) declares its container and dependencies in code, every experiment the team runs is easy to reproduce without messing around with Docker images or hunting down obscure drifts. Changing a base image or a core dependency is now just a one-line diff that takes effect on the next run. Before, that meant building an image, pushing it, figuring out how to get source code onto the machine, and restarting by hand when something crashed. That's 30 to 60 minutes back on every experiment.

“Modal turns something that might be a 30-minute process into a zero-minute process, so we can run an order of magnitude more experiments. It would be very hard to reach this research velocity without Modal.”

And they don't have to reserve compute up front, which is crucial for the bursty workloads Markov runs. One experiment means a lot of preprocessing and compute, then a training run of four to ten hours, then scaling back down to zero. Most of the GPU providers they looked at want you to rent fixed machines by the month, whereas on Modal they’re able to reach for compute as they need it and *only when* they need it, with Modal’s per-second billing.

## **Unlocking remote inference**

While many of Markov's robots carry a GPU onboard and run many policies locally, the company's larger world models needed to be run remotely while maintaining the low latency needed to operate a real-time device.

For this, Markov uses [Modal Tunnels](https://modal.com/docs/guide/tunnels) to open a direct path between the robot and a GPU pinned in us-west, measuring round-trip network overhead at approximately 20 milliseconds. Deployment is also the only stage in the pipeline with placement requirements: precompute and training can run globally, while inference needs to be as close to the robot as possible, and run on consistently high-performing hardware. Modal makes this a single line of code.

## **Empowering agents with Modal’s code-first approach**

While each step of the end-to-end pipeline looks different, one thing is the same: It’s all just code. Whether it’s a precompute step, a training run, or low-latency inference, with modal it’s just a code file. That structure benefits engineers, who can read the pipeline end to end, and it benefits the coding agents the team relies on to move quickly.

“Modal lets us make everything in a very code-first way, so it lets us use coding agents a lot more effectively. It’s all just a code file instead of using this platform for that and that platform for this. The agent can see everything and write one script that does exactly what we want.”

This is a large part of how a team this size keeps ten experiments running at once. An engineer describes an experiment — what gets precomputed, what it trains on, how it deploys — and an agent writes the file.

## **Speeding towards general dexterity**

Markov's bet was that a world model would learn physics from video instead of from demonstrations, and that the priors it picks up along the way would substitute for collection at scale.

The bet is paying off. After focusing on dexterous hands, the team's early experiments on grippers worked with almost no additional effort.

Part of why they got here this fast is that they knew exactly what they needed from their compute. Preparing hundreds of terabytes of video, running ten experiments at once, and holding a 20-millisecond loop open to a robot are three different problems, and Markov found one platform that lets them solve for all three at once. That leaves the team's attention where it belongs, on working out what a robot needs to see in order to act.

As the team scales up the data, the training runs, and the number of robots going out into the field, the pipeline scales with them.
