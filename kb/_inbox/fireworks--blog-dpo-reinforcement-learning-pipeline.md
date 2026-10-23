---
title: 'DPO as Reinforcement Learning: GRPO With Two Rollouts | Fireworks'
kind: blog
topic: null
subtopic: null
secondary_topics: []
summary: null
triage: null
skip_reason: null
source: fireworks
url: https://fireworks.ai/blog/dpo-reinforcement-learning-pipeline
author: null
published: '2025-12-31'
fetched: '2026-10-23T06:11:10Z'
classifier: null
taxonomy_rev: 2
words: 1506
content_sha256: a0d9a8426c18cd24185548be6b60e3a139999a36ccaf5ffc69fc15d9e91e1e59
---

# DPO as Reinforcement Learning: GRPO With Two Rollouts | Fireworks

### Introduction

A recent research paper, “[**IT TAKES TWO: YOUR GRPO IS SECRETLY DPO**](https://arxiv.org/abs/2510.00977)“, bridged DPO and GRPO by framing both DPO and GRPO under the same contrastive loss form, and experimentally verified that sometimes GRPO with group size 2 can perform reasonably well.

In this blogpost, we conversely claim that under a more on-policy setting, you can setup a reasonably well functioning recurring / continuous model training pipeline with one-off DPO training, that can be as powerful as RL.

### The Intuition

DPO (Direct Preference Optimization) and GRPO (Group Relative Policy Optimization) are both powerful LLM fine-tuning techniques that allow models to be tuned towards generating better responses.

In the DPO setup, one is expected to provide a dataset where each row contains a prompt and two responses. Among the two responses, one is preferred and the other is dispreferred. For example, I could have a dataset of prompts that ask the model to write an email. Each row of the dataset could look like:

`jsonCopy`
12345678910

Training on the dataset with DPO, the model would be tuned to generate the preferred response more often and the dispreferred\_response less often.

In the GRPO setup, if we focus on a single training step, one is expected to provide a dataset where each row contains a prompt, and multiple responses, with each response having a score / reward attached to it. One row in the dataset (that goes into the trainer) in the above email writing example would look like this:

`jsonCopy`
12345678910111213141516171819202122

In GRPO training, the model would be trained to output response with higher than average score, and dissuaded from outputting lower than average score response.

Since GRPO is usually run in a loop with multiple rounds of dataset generation and model update steps, the scores are usually obtained from automatic scorer (with verifier); whereas DPO dataset (preferred / dispreferred) response could be coming from human annotator or user feedbacks.

On the surface, the mechanics of both approaches are quite different. However, if we make a couple simplifying assumptions, DPO and GRPO are intuitively similar, both learning by contrasting the good response with the bad response. The simplifications are:

1. GRPO group size = 2, meaning that in each row there are exactly two responses to the prompt
2. Among the two responses in each GRPO dataset row, the better one is given a score of 1.0 and the other one given a score of 0.0 (no tie allowed)
3. We extend the GRPO batch size to full dataset size, and only perform 1 epoch of training

With simplification 1) and 2), GRPO trains the model to generate the higher scoring response (preferred response) and avoid the lower scoring response (dispreferred response) similar to DPO. With assumption 3), we essentially make GRPO off-policy. Instead of going through the typical generate -> score / verifier -> train loop on a small batch size of data, you do it on the whole dataset once.

### Theoretical Background

Now we have established the intuition that an extremely simplified off-policy GRPO setup is intuitively doing similar things as DPO. How much do they differ in their mathematics? Let’s find out.

#### DPO Simplification

DPO loss function looks like:

$\mathcal{L}_{DPO}(\theta) = - \mathbb{E}_{(x, y_w, y_l) \sim \mathcal{D}} \left[ \log \sigma \left( \beta \log \frac{\pi_\theta(y_w | x)}{\pi_{ref}(y_w | x)} - \beta \log \frac{\pi_\theta(y_l | x)}{\pi_{ref}(y_l | x)} \right) \right]$

where $\pi_{ref}$ is the reference model that we do not want the tuned model to be deviating too much away from. It is typically the untuned base model. $y_w$and $y_l$ are the “winning”(preferred) and “losing”(dispreferred) generations from the same prompt $x$. For simplicity, let’s use the notation $P_w = \frac{\pi_\theta(y_w | x)}{\pi_{ref}(y_w | x)} \quad$ and $\quad P_l = \frac{\pi_\theta(y_l | x)}{\pi_{ref}(y_l | x)}$ to simplify the expression. The loss function then became

$\mathcal{L}_{DPO}(\theta) = - \mathbb{E}_{(x, y_w, y_l) \sim \mathcal{D}} \left[ \log \sigma \left(z \right) \right]$

where $z = \beta \log(P_w) - \beta \log(P_l)$.

Take per sample loss (what’s inside the expectation) and perform Taylor expansion around $z=0$, we get

$- \log(\sigma(z)) = - \log{\frac{1}{1+e^{-z}}} = \log 2 - \frac{z}{2} + \frac{z^2}{8} + O(x^4)$

Since we are going to take the derivative on the loss to get gradient, we don’t really care about the constant term. When the policy model and reference model are both close to each other, $z$ would be close to 0, so we can be handwavy about the quadratic term and beyond as well. Therefore, for the purpose of getting gradient (we are using lower case $l$ for per-sample loss),

$\mathcal{l}_{\text{DPO}}(\theta) \approx -\frac{1}{2}z = - \frac{1}{2} [\beta(\log \mathcal{P}_w - \log \mathcal{P}_l)]$

Again when policy model and reference model are close enough, we will have $P_l$ and $P_w$ being close to 1. The following approximation holds:

$\log(\mathcal{P}_i) = \log(1 + (\mathcal{P}_i - 1)) \approx \mathcal{P}_i - 1$

Substituting everything in, we have

$\mathcal{l}_{\text{DPO}}(\theta) \approx \frac{\beta}{2} \left[ \frac{\pi_\theta(y_l | x)}{\pi_{ref}(y_l | x)} - \frac{\pi_\theta(y_w | x)}{\pi_{ref}(y_w | x)} \right]$

#### GRPO Simplification

In GRPO, we typically generate multiple responses from the same prompt and evaluate the individual responses to give each of them a reward score. The objective of GRPO for a single sample (single prompt) looks like:

$J(\theta) = \frac{1}{G} \sum_{i=1}^{G} \left( \min \left( \frac{\pi_\theta(y_i|x)}{\pi_{\theta_{old}}(y_i|x)} A_i, \text{clip} \left( \frac{\pi_\theta(y_i|x)}{\pi_{\theta_{old}}(y_i|x)}, 1 - \epsilon, 1 + \epsilon \right) A_i \right) - \beta D_{KL}(\pi_\theta || \pi_{ref}) \right)$

where $A_i = \frac{r_i - \text{mean}(r_1, r_2, \dots, r_G)}{\text{std}(r_1, r_2, \dots, r_G)}$ is the advantage and G is the group size. Each $r_i$ represents the reward given to each generation $y_i$ to the same prompt $x$ in the group of responses.

With the above-mentioned simplification 1) and 2), we set $G=2$, and $r_1 = 1.0$, $r_2 = 0.0$(i.e. generate only two responses per sample and give the better one of them 1.0 reward and the other one 0.0 reward). Plugging in the values, we get $A_1 = 1.0$ and $A_2 = -1.0$ since $std(r_1, r_2) = 0.5$ and . With simplification 3), $\pi_{old}$ is the same as the base untuned model $\pi_{ref}$. These get us to

$J(\theta) = \frac{1}{2} \sum_{i=1}^{2} \left( \min \left( \frac{\pi_\theta(y_i|x)}{\pi_{ref}(y_i|x)}, \text{clip} \left( \frac{\pi_\theta(y_i|x)}{\pi_{ref}(y_i|x)}, 1 - \epsilon, 1 + \epsilon \right) A_i \right) - \beta D_{KL}(\pi_\theta || \pi_{ref}) \right)$

Clipping and min() operators in the objective are used for preventing large policy updates that could destabilize the training, and if we ignore them for now when looking at a single step update, the cleaned equation simplifies to:

$\mathcal{L}_{\text{GRPO}}(\theta) = \frac{1}{2} \left[ \frac{\pi_\theta(y_1|x)}{\pi_{\text{ref}}(y_1|x)} - \frac{\pi_\theta(y_2|x)}{\pi_{\text{ref}}(y_2|x)} \right] - \beta D_{KL}[\pi_\theta || \pi_{\text{ref}}]$Notice that in GRPO, we are trying to maximize the objective, whereas in DPO, we are trying to minimize the loss, so you end up with roughly the same thing ($y_w$ and $y_l$ in the DPO formula are your $y_1$ and $y_2$ in the GRPO objective).

The GRPO objective still has the KL divergence constraint, but the simplified DPO loss does not have it. This difference is introduced by the various approximations we made in the derivation, but DPO actually was derived with KL divergence constraint in mind, so they are indeed very similar.

### Short Break

So just to take a pause and reflect on what we have done so far. We first built the intuition that DPO and GRPO are similar if your GRPO is simplified with 3 simplifying assumptions (it is indeed very practical assumptions for many use cases); and then we derived mathematically that DPO loss and GRPO objective are indeed pretty similar: both of them are trying to increase the probability of preferred response while decreasing the probability of the dispreferred response, under the constraint that the KL divergence between the old and new policies is not too big.

That all sounds great, but what have we gained in return? Well, you can practically combine a DPO trainer and an automatic or human annotator powered DPO dataset collection process to perform continuous off-policy (or semi-off-policy?) RL.

### A Practical Recipe

Imagine that you have a pipeline that collects user requests and scores the model responses in some way, you can formulate that dataset into a DPO dataset and run DPO training to get a better model. You can then deploy this updated model for online traffic to collect more user feedbacks. You can continuously repeat the same process in a recurring manner (hourly, daily, weekly etc), and that essentially gets you an off-policy RL pipeline that hopefully gets your model better and better.

A practical scenario for the above could be in building Q&A customer support bot. The customer support bot could return two responses to a customer’s question, and the customer could pick the more helpful answer and continue the conversation. This way, the collected production traffic naturally comes out as a DPO dataset.

![Customer support bot with 2 responses Customer support bot with 2 responses](https://fireworks.ai/_next/image?url=https%3A%2F%2Fcdn.sanity.io%2Fimages%2Fpv37i0yn%2Fhorizon%2Fe8cf95e80b5e062f1124ef1b8e8f3bd23b9dda94-1024x1024.png%3Fauto%3Dformat&w=3840&q=75)

Fireworks.ai provides [DPO tuning](https://docs.fireworks.ai/fine-tuning/dpo-fine-tuning) capability as part of the tuning platform. [RESTful APIs](https://docs.fireworks.ai/api-reference/create-dpo-job) are also available for building up an automated workflow that allows you to perform the recurring training / continuous model improvement detailed in the flow chart above.
