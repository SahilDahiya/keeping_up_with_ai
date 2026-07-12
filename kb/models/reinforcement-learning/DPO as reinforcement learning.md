---
title: DPO as reinforcement learning
topic: models
subtopic: reinforcement-learning
secondary_topics:
- models/reasoning
summary: Connects DPO and RL-style training loops, explaining preference optimization
  as part of continuous model improvement.
source: fireworks
url: https://fireworks.ai/blog/dpo-as-rl
author: null
published: '2025-12-31'
fetched: '2026-07-11T04:13:22Z'
classifier: codex
taxonomy_rev: 1
words: 1252
content_sha256: d23f4a98b22c7b6a0cd2acd237f38799a3ccf5fa98590f44b6ebb67369136875
triage: keep
skip_reason: null
---

# DPO as reinforcement learning

A recent research paper, "[ IT TAKES TWO: YOUR GRPO IS SECRETLY DPO](https://arxiv.org/abs/2510.00977)", bridged DPO and GRPO by framing both DPO and GRPO under the same contrastive loss form, and experimentally verified that sometimes GRPO with group size 2 can perform reasonably well.

In this blogpost, we conversely claim that under a more on-policy setting, you can setup a reasonably well functioning recurring / continuous model training pipeline with one-off DPO training, that can be as powerful as RL.

DPO (Direct Preference Optimization) and GRPO (Group Relative Policy Optimization) are both powerful LLM fine-tuning techniques that allow models to be tuned towards generating better responses.

In the DPO setup, one is expected to provide a dataset where each row contains a prompt and two responses. Among the two responses, one is preferred and the other is dispreferred. For example, I could have a dataset of prompts that ask the model to write an email. Each row of the dataset could look like:

12345678910

Training on the dataset with DPO, the model would be tuned to generate the preferred response more often and the dispreferred_response less often.

In the GRPO setup, if we focus on a single training step, one is expected to provide a dataset where each row contains a prompt, and multiple responses, with each response having a score / reward attached to it. One row in the dataset (that goes into the trainer) in the above email writing example would look like this:

12345678910111213141516171819202122

In GRPO training, the model would be trained to output response with higher than average score, and dissuaded from outputting lower than average score response.

Since GRPO is usually run in a loop with multiple rounds of dataset generation and model update steps, the scores are usually obtained from automatic scorer (with verifier); whereas DPO dataset (preferred / dispreferred) response could be coming from human annotator or user feedbacks.

On the surface, the mechanics of both approaches are quite different. However, if we make a couple simplifying assumptions, DPO and GRPO are intuitively similar, both learning by contrasting the good response with the bad response. The simplifications are:

- GRPO group size = 2, meaning that in each row there are exactly two responses to the prompt
- Among the two responses in each GRPO dataset row, the better one is given a score of 1.0 and the other one given a score of 0.0 (no tie allowed)
- We extend the GRPO batch size to full dataset size, and only perform 1 epoch of training

With simplification 1) and 2), GRPO trains the model to generate the higher scoring response (preferred response) and avoid the lower scoring response (dispreferred response) similar to DPO. With assumption 3), we essentially make GRPO off-policy. Instead of going through the typical generate -> score / verifier -> train loop on a small batch size of data, you do it on the whole dataset once.

Now we have established the intuition that an extremely simplified off-policy GRPO setup is intuitively doing similar things as DPO. How much do they differ in their mathematics? Let’s find out.

DPO loss function looks like:

where is the reference model that we do not want the tuned model to be deviating too much away from. It is typically the untuned base model. and are the "winning"(preferred) and "losing"(dispreferred) generations from the same prompt . For simplicity, let’s use the notation and to simplify the expression. The loss function then became

where .

Take per sample loss (what's inside the expectation) and perform Taylor expansion around , we get

Since we are going to take the derivative on the loss to get gradient, we don’t really care about the constant term. When the policy model and reference model are both close to each other, would be close to 0, so we can be handwavy about the quadratic term and beyond as well. Therefore, for the purpose of getting gradient (we are using lower case for per-sample loss),

Again when policy model and reference model are close enough, we will have and being close to 1. The following approximation holds:

Substituting everything in, we have

In GRPO, we typically generate multiple responses from the same prompt and evaluate the individual responses to give each of them a reward score. The objective of GRPO for a single sample (single prompt) looks like:

where is the advantage and G is the group size. Each represents the reward given to each generation to the same prompt in the group of responses.

With the above-mentioned simplification 1) and 2), we set , and , (i.e. generate only two responses per sample and give the better one of them 1.0 reward and the other one 0.0 reward). Plugging in the values, we get and since and . With simplification 3), is the same as the base untuned model . These get us to

Clipping and min() operators in the objective are used for preventing large policy updates that could destabilize the training, and if we ignore them for now when looking at a single step update, the cleaned equation simplifies to:


Notice that in GRPO, we are trying to maximize the objective, whereas in DPO, we are trying to minimize the loss, so you end up with roughly the same thing ( and  in the DPO formula are your  and  in the GRPO objective).

The GRPO objective still has the KL divergence constraint, but the simplified DPO loss does not have it. This difference is introduced by the various approximations we made in the derivation, but DPO actually was derived with KL divergence constraint in mind, so they are indeed very similar.

So just to take a pause and reflect on what we have done so far. We first built the intuition that DPO and GRPO are similar if your GRPO is simplified with 3 simplifying assumptions (it is indeed very practical assumptions for many use cases); and then we derived mathematically that DPO loss and GRPO objective are indeed pretty similar: both of them are trying to increase the probability of preferred response while decreasing the probability of the dispreferred response, under the constraint that the KL divergence between the old and new policies is not too big.

That all sounds great, but what have we gained in return? Well, you can practically combine a DPO trainer and an automatic or human annotator powered DPO dataset collection process to perform continuous off-policy (or semi-off-policy?) RL.

Imagine that you have a pipeline that collects user requests and scores the model responses in some way, you can formulate that dataset into a DPO dataset and run DPO training to get a better model. You can then deploy this updated model for online traffic to collect more user feedbacks. You can continuously repeat the same process in a recurring manner (hourly, daily, weekly etc), and that essentially gets you an off-policy RL pipeline that hopefully gets your model better and better.

A practical scenario for the above could be in building Q&A customer support bot. The customer support bot could return two responses to a customer's question, and the customer could pick the more helpful answer and continue the conversation. This way, the collected production traffic naturally comes out as a DPO dataset.

Fireworks.ai provides [DPO tuning](https://docs.fireworks.ai/fine-tuning/dpo-fine-tuning) capability as part of the tuning platform. [RESTful APIs](https://docs.fireworks.ai/api-reference/create-dpo-job) are also available for building up an automated workflow that allows you to perform the recurring training / continuous model improvement detailed in the flow chart above.
