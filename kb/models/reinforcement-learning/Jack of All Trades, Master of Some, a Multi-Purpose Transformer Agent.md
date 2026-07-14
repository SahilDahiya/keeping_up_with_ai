---
title: Jack of All Trades, Master of Some, a Multi-Purpose Transformer Agent
kind: blog
topic: models
subtopic: reinforcement-learning
secondary_topics: []
summary: 'JAT is an open reproduction of DeepMind''s Gato: a multimodal transformer
  agent trained on hundreds of thousands of expert trajectories (Atari, BabyAI, Meta-World,
  MuJoCo) released as the JAT dataset, with architectural changes for handling sequential
  observations and continuous values.'
triage: null
skip_reason: null
source: huggingface
url: https://huggingface.co/blog/jat
author: Quentin Gallouédec; Edward Beeching; Clément ROMAC; Thomas Wolf
published: '2024-04-22'
fetched: '2026-07-14T22:13:29Z'
classifier: claude
taxonomy_rev: 1
words: 1514
content_sha256: 38f3646bbaafd8633347b75aa6279f31302e45080fdace52f19a80c85d758b72
---

# Jack of All Trades, Master of Some, a Multi-Purpose Transformer Agent

Reinforcement Learning •  Updated   •  19  •  99  

#### jat-project/jat

![](https://cdn-avatars.huggingface.co/v1/production/uploads/6200d0a443eb0913fa2df7cc/E3GJImT10EsbruN2ymJcM.png) 

 Published
					April 22, 2024 

  Upvote 

 81

We're excited to share Jack of All Trades (JAT), a project that aims to move in the direction of a generalist agent. The project started as an open reproduction of the [Gato](https://huggingface.co/papers/2205.06175) (Reed et al., 2022) work, which proposed to train a Transformer able to perform both vision-and-language and decision-making tasks. We thus started by building an open version of Gato’s dataset. We then trained multi-modal Transformer models on it, introducing several improvements over Gato for handling sequential data and continuous values.

Overall, the project has resulted in:

- The release of a large number of **expert RL agents**on a wide variety of tasks.
- The release of the **JAT dataset**, the first dataset for generalist agent training. It contains hundreds of thousands of expert trajectories collected with the expert agents
- The release of the **JAT model**, a transformer-based agent capable of playing video games, controlling a robot to perform a wide variety of tasks, understanding and executing commands in a simple navigation environment and much more!

RL traditionally involves training policies on single environments. Leveraging these expert policies is a genuine way to build a versatile agent. We selected a wide range of environments, of varying nature and difficulty, including Atari, BabyAI, Meta-World, and MuJoCo. For each of these environments, we train an agent until it reached state-of-the-art performance. (For BabyAI,  we use the [BabyAI bot](https://github.com/mila-iqia/babyai) instead). The resulting agents are called expert agents, and have been released on the 🤗 Hub. You'll find a list of all agents in the [JAT dataset card](https://huggingface.co/datasets/jat-project/jat-dataset).

We release the [JAT dataset](https://huggingface.co/datasets/jat-project/jat-dataset), the first dataset for generalist agent training. The JAT dataset contains hundreds of thousands of expert trajectories collected with the above-mentioned expert agents. To use this dataset, simply load it like any other dataset from the 🤗 Hub:

```
>>> from datasets import load_dataset
>>> dataset = load_dataset("jat-project/jat-dataset", "metaworld-assembly")
>>> first_episode = dataset["train"][0]
>>> first_episode.keys()
dict_keys(['continuous_observations', 'continuous_actions', 'rewards'])
>>> len(first_episode["rewards"])
500
>>> first_episode["continuous_actions"][0]
[6.459120273590088, 2.2422609329223633, -5.914587020874023, -19.799840927124023]
```
In addition to RL data, we include textual datasets to enable a unique interface for the user. That's why you'll also find subsets for [Wikipedia](https://huggingface.co/datasets/wikipedia), [Oscar](https://huggingface.co/datasets/oscar), [OK-VQA](https://okvqa.allenai.org) and [Conceptual-Captions](https://huggingface.co/datasets/conceptual_captions).

JAT's architecture is based on a Transformer, using [EleutherAI's GPT-Neo implementation](https://huggingface.co/docs/transformers/model_doc/gpt_neo). JAT's particularity lies in its embedding mechanism, which has been built to intrinsically handle sequential decision tasks. We interleave observation embeddings with action embeddings, along with the corresponding rewards.

Each embedding therefore corresponds either to an observation (associated with the reward), or to an action. But how does JAT encode this information? It depends on the type of data. If the data (observation or action) is an image (as is the case for Atari), then JAT uses a CNN. If it's a continuous vector, then JAT uses a linear layer. Finally, if it's a discrete value, JAT uses a linear projection layer. The same principle is used for model output, depending on the type of data to be predicted. Prediction is causal, shifting observations by 1 time step. In this way, the agent must predict the next action from all previous observations and actions.

In addition, we thought it would be fun to train our agent to perform NLP and CV tasks. To do this, we also gave the encoder the option of taking text and image data as input. For text data, we tokenize using GPT-2 tokenization strategy, and for images, we use a [ViT](https://huggingface.co/docs/transformers/model_doc/vit)-type encoder.

Given that the modality of the data can change from one environment to another, how does JAT compute the loss? It computes the loss for each modality separately. For images and continuous values, it uses the MSE loss. For discrete values, it uses the cross-entropy loss. The final loss is the average of the losses for each element of the sequence.
Wait, does that mean we give equal weight to predicting actions and observations? Actually, no, but we'll talk more about that [below](https://huggingface.co#the-surprising-benefits-of-predicting-observations).

We evaluate JAT on all 157 training tasks. We collect 10 episodes and record the total reward. For ease of reading, we aggregate the results by domain.

If we were to summarize these results in one number, it would be 65.8%, the average performance compared to the JAT expert over the 4 domains. This shows that JAT is capable of mimicking expert performance on a very wide variety of tasks. Let's go into a little more detail:

- For Atari 57, the agent achieves 14.1% of the expert's score, corresponding to 37.6% of human performance. It exceeds human performance on 21 games.
- For BabyAI, the agent achieves 99.0% of the expert's score, and fails to exceed 50% of the expert on just 1 task.
- For Meta-World, the agent reached 65.5% of the expert.
- For MuJoCo, the agent achieves 84.8% of the expert.

What's most impressive is that JAT achieves this performance using a **single network** for all domains. To take the measure of this performance, let's watch JAT's rendering on a few tasks:

Want to try it out? You can! The [JAT model](https://huggingface.co/jat-project/jat) is available on the 🤗 Hub!

For textual tasks, our model shows rudimentary capabilities, we refer the reader to the [paper](https://huggingface.co/papers/2402.09844) for more details.

When training an RL agent, the primary goal is to maximize future rewards. But what if we also ask the agent to predict what it will observe in the future? Will this additional task help or hinder the learning process?

There are two opposing views on this question. On one hand, learning to predict observations could provide a deeper understanding of the environment, leading to better and faster learning. On the other hand, it could distract the agent from its main goal, resulting in mediocre performance in both observation and action prediction.

To settle this debate, we conducted an experiment using a loss function that combines observation loss and action loss, with a weighting parameter to balance the two objectives.

The results were noteworthy. When was too high (0.5), the additional objective of predicting observations seemed to hinder the learning process. But when was lower, the impact on learning was negligible, and the agent's performance was similar to that obtained when observation prediction was not part of the objective.

However, we found a sweet spot around , where learning to predict observations actually improved the agent's learning efficiency. Our study suggests that adding observation prediction to the learning process can be beneficial, as long as it's balanced correctly. This finding has important implications for the design of such agents, highlighting the potential value of auxiliary objectives in improving learning efficiency.

So, the next time you're training an RL agent, consider asking it to predict what it will observe in the future. It might just lead to better performance and faster learning!

In this work, we introduced JAT, a multi-purpose transformer agent capable of mastering a wide variety of sequential decision-making tasks, and showing rudimentary capabilities in NLP and CV tasks. For all these tasks, JAT uses a single network. Our contributions include the release of expert RL agents, the JAT dataset, and the JAT model. We hope that this work will inspire future research in the field of generalist agents and contribute to the development of more versatile and capable AI systems.

We believe that the JAT project has opened up a new direction for research in the field of generalist agents, and we've only just scratched the surface. Here are some ideas for future work:

- **Improving the data**: Although pioneering, the JAT dataset is still in its early stages. The expert trajectories come from only one expert agent per environment which may cause some bias. Although we've done our best to reach state-of-the-art performance, some environments are still challenging. We believe that collecting more data and training more expert agents could help- **a lot**.
- **Use offline RL**: The JAT agent is trained using basic Behavioral Cloning. This implies two things: (1) we can't take advantage of sub-optimal trajectories and (2) the JAT agent can't outperform the expert. We've chosen this approach for simplicity, but we believe that using offline RL could- **really help**improve the agent's performance, while not being too complex to implement.
- **Unlock the full potential of a smarter multi-task sampling strategy**: Currently, the JAT agent samples data uniformly from all tasks, but this approach may be holding it back. By dynamically adjusting the sampling rate to focus on the most challenging tasks, we can supercharge the agent's learning process and unlock- **significant performance gains**.

- 📄 [Paper](https://huggingface.co/papers/2402.09844)
- 💻 [Source code](https://github.com/huggingface/jat)
- 🗂️ [JAT dataset](https://huggingface.co/datasets/jat-project/jat-dataset)
- 🤖 [JAT model](https://huggingface.co/jat-project/jat)

```
@article{gallouedec2024jack,
    title = {{Jack of All Trades, Master of Some, a Multi-Purpose Transformer Agent}},
    author = {Gallouédec, Quentin and Beeching, Edward and Romac, Clément and Dellandréa, Emmanuel},
    journal = {arXiv preprint arXiv:2402.09844},
    year = {2024},
    url = {https://arxiv.org/abs/2402.09844}
}
```
 Reinforcement Learning •  Updated   •  19  •  99 

 Viewer • Updated  •  258M •  508k  •  69 

More Articles from our Blog

vllmtransformersinference

  45

 July 8, 2026 peftloraguide

  75

 June 18, 2026
