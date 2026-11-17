---
title: Hugging Face and OpenRouter join forces to make open-weight models easy to
  run
kind: blog
topic: inference
subtopic: optimization
secondary_topics:
- industry/trends
summary: Hugging Face moves Inference Providers' routing to OpenRouter, which now
  picks a provider per request on live price/speed/reliability (cutting capacity errors
  46%, improving time-to-first-token 16.9%) with cache-aware routing via an X-HF-Session-Id
  header and :fastest/:cheapest policy suffixes; open-weight models' share of OpenRouter
  tokens rose from 26.8% to 71.7% over the past year.
triage: null
skip_reason: null
source: huggingface
url: https://huggingface.co/blog/openrouter
author: Célina Hanouti; Victor Mustar; Bertrand Chevrier; Lucain Pouget; Pierric Cistac;
  Eliott Coyac; Julien Chaumond
published: '2026-11-16'
fetched: '2026-11-17T06:12:45Z'
classifier: claude
taxonomy_rev: 2
words: 1150
content_sha256: c518219204e533ca029c2beba0f183695a36599220a4579f89eaea0263716f59
---

# Hugging Face and OpenRouter join forces to make open-weight models easy to run

# 
		
	
	
		Hugging Face and OpenRouter join forces to make open-weight models easy to run

[Update on GitHub](https://github.com/huggingface/blog/blob/main/openrouter.md)

  [Upvote 44](https://huggingface.co/login?next=%2Fblog%2Fopenrouter) 

![Célina Hanouti's avatar](https://cdn-avatars.huggingface.co/v1/production/uploads/6192895f3b8aa351a46fadfd/gsGa2PvHTKAv7MNbyLH8y.jpeg) 

![Victor Mustar's avatar](https://cdn-avatars.huggingface.co/v1/production/uploads/5f17f0a0925b9863e28ad517/78BR8GuQiX9a8wbbRlSAC.webp) 

![Bertrand Chevrier's avatar](https://cdn-avatars.huggingface.co/v1/production/uploads/62d6c40ba71903fb4c1e3261/SQGmYShjtveXBf8HVpxPp.jpeg) 

![Lucain Pouget's avatar](https://cdn-avatars.huggingface.co/v1/production/uploads/1659336880158-6273f303f6d63a28483fde12.png) 

![Pierric Cistac's avatar](https://cdn-avatars.huggingface.co/v1/production/uploads/1624630689857-5e67de201009063689407481.jpeg) 

![Eliott Coyac's avatar](https://cdn-avatars.huggingface.co/v1/production/uploads/61d2f90c3c2083e1c08af22d/jn21aKijwBnopk7aUJUkq.png) 

![Julien Chaumond's avatar](https://cdn-avatars.huggingface.co/v1/production/uploads/5dd96eb166059660ed1ee413/NQtzmrDdbG0H8qkZvRyGk.jpeg) 

Hugging Face and OpenRouter are teaming up to make open-weight models easy to run. Every major open-weight release is already being published on the Hugging Face Hub, and [OpenRouter](https://openrouter.ai) serves those models at scale, routing each request across 80+ providers based on live measurements of each one. Together, every open-weight model on the Hub that a provider serves can be called with your Hugging Face token, through the same API, with the best provider picked for each request.

Today, we are switching [Inference Providers](https://huggingface.co/docs/inference-providers) from our own custom router to OpenRouter's. Requests made to language models now go through OpenRouter, which picks the best provider for each call based on live price, speed and reliability, and retries on another provider if the first one fails. Your code stays the same.

## 
		
	
	
		Run them with the tools you already use

The router supports OpenAI's Chat Completions and Responses APIs and Anthropic's Messages API for every chat model, whatever the provider behind it. Pick your coding agent or SDK and a model, then copy the steps, or copy the whole setup as a prompt for your agent:

Setup guides for [Claude Code](https://huggingface.co/docs/inference-providers/integrations/claude-code), [Codex](https://huggingface.co/docs/inference-providers/integrations/codex), [OpenCode](https://huggingface.co/docs/inference-providers/integrations/opencode), [Pi](https://huggingface.co/docs/inference-providers/integrations/pi) and [Hermes Agent](https://huggingface.co/docs/inference-providers/integrations/hermes-agent)

The same Hugging Face token also gives you storage with [Storage Buckets](https://huggingface.co/storage), compute with [Jobs](https://huggingface.co/docs/hub/jobs-overview) and dedicated inference with [Inference Endpoints](https://huggingface.co/docs/inference-endpoints). PRO, Team and Enterprise plans include monthly credits for compute and inference.

## 
		
	
	
		How open-weight models are used

On OpenRouter, open-weight models went from 26.8% of the tokens served in October 2025 to 71.7% at the end of September 2026, after peaking at 77.5% in July ([OpenRouter, October 2026](https://openrouter.ai/blog/insights/open-weight-vs-closed-weight-models/)). Over the same period, weekly open-weight volume grew more than 60-fold, against almost tenfold for closed models. This week, the most used model on OpenRouter is an open-weight one, DeepSeek V4.1 Flash 1017, with 59.2 trillion tokens ([rankings](https://openrouter.ai/rankings)).

![Open-weight models' share of tokens on OpenRouter, from 26.8% in October 2025 to 71.7% in September 2026](https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/blog/inference-providers-openrouter/open-weight-share@2x.png) 

![Open-weight models' share of tokens on OpenRouter, from 26.8% in October 2025 to 71.7% in September 2026](https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/blog/inference-providers-openrouter/open-weight-share-dark@2x.png) 

Open-weight models cost about four times less on average: $0.28 per million input tokens and $1.62 per million output tokens, against $1.27 and $6.36 for closed models.

The best open-weight models still trail the best proprietary ones on the hardest benchmarks. On the [Artificial Analysis Intelligence Index](https://artificialanalysis.ai/leaderboards/models), Kimi K3.1 Pro, the best open-weight model, scores 46 against 65 for Claude Fable 5.2, at about a seventh of the cost per task ($3.68 against $26.54). For a lot of workloads, that trade-off is worth it.

![Artificial Analysis Intelligence Index against cost per task, for the top proprietary and open-weight models](https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/blog/inference-providers-openrouter/intelligence-vs-cost@2x.png) 

![Artificial Analysis Intelligence Index against cost per task, for the top proprietary and open-weight models](https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/blog/inference-providers-openrouter/intelligence-vs-cost-dark@2x.png) 

## 
		
	
	
		Routing powered by OpenRouter

OpenRouter serves more than 800 trillion tokens a month to over 10 million users, across 600+ models from 80+ providers. Its routing is based on live measurements of every provider across that traffic.

OpenRouter recently [rebuilt its provider routing](https://openrouter.ai/blog/announcements/how-we-rebuilt-provider-routing/): instead of only looking at the lowest list price, it sends each request to the provider with the best mix of price, speed and reliability.

When a provider slows down or starts failing, traffic moves away from it until it recovers, and a failed try is retried on the next best provider inside the same call. In OpenRouter's measurements, the new routing cut capacity errors by 46% and improved time to first token by 16.9% and throughput by 16.3%.

![Default routing retries on another provider when the first one is rate limited, :cheapest picks the lowest price and :fastest the highest throughput](https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/blog/inference-providers-openrouter/routing@2x.gif) 

![Default routing retries on another provider when the first one is rate limited, :cheapest picks the lowest price and :fastest the highest throughput](https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/blog/inference-providers-openrouter/routing-dark@2x.gif) 

Before, Inference Providers picked one provider for your request and returned its error if it failed. Now, the request is retried on another provider. You can still choose a policy or a provider with a suffix on the model id:

```
zai-org/GLM-5.3            # default: best mix of price, speed and reliability
zai-org/GLM-5.3:fastest    # highest throughput
zai-org/GLM-5.3:cheapest   # lowest price
zai-org/GLM-5.3:novita     # only Novita
```
Routing is also cache-aware: a conversation stays on the provider that holds its prompt cache. To make it explicit, send a stable UUID per conversation in the `X-HF-Session-Id` header (see the [prompt caching guide](https://huggingface.co/docs/inference-providers/prompt-caching)).

## 
		
	
	
		Pricing

Pricing doesn't change: you pay the provider's price on your Hugging Face bill, and Hugging Face doesn't add a markup on top of it. PRO users get $2 of credits every month, and Team and Enterprise organizations get $2 per seat. See [Pricing and Billing](https://huggingface.co/docs/inference-providers/pricing) for the details.

## 
		
	
	
		Image, video and audio generation

Image, video, and audio generation continue to work exactly as before, directly through Hugging Face Inference Providers without going through OpenRouter. You can keep using the same token and API, and access tens of thousands of [LoRAs](https://huggingface.co/models?inference_provider=all&pipeline_tag=text-to-image&other=lora).

## 
		
	
	
		See where your requests go

On model pages, you can chat with the model right away in the widget. Two new tabs show what's behind it: Providers lists every provider OpenRouter can route the model to, with its input and output price, speed and uptime over the last 24 hours, and Metrics shows the best price, throughput, time to first token, context length and uptime among them:

![Chatting with Inkling-2-Small in the model page widget, opening its code snippets, then its Metrics tab](https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/blog/inference-providers-openrouter/widget-playground-3@2x.gif) 

![Chatting with Inkling-2-Small in the model page widget, opening its code snippets, then its Metrics tab](https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/blog/inference-providers-openrouter/widget-playground-3-dark@2x.gif) 

Your [usage overview](https://huggingface.co/settings/inference-providers/overview) breaks your spend down by the provider each request went to:

![Daily Inference Providers spend, broken down by provider](https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/blog/inference-providers-openrouter/usage-by-provider@2x.png) 

![Daily Inference Providers spend, broken down by provider](https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/blog/inference-providers-openrouter/usage-by-provider-dark@2x.png) 

In your [settings](https://huggingface.co/settings/inference-providers), you can turn off any provider you don't want: the router never sends your requests there. Organizations have the same settings, and they apply to every request billed to the organization.

![Inference Providers settings, with a toggle for each provider](https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/blog/inference-providers-openrouter/settings-providers@2x.png) 

![Inference Providers settings, with a toggle for each provider](https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/blog/inference-providers-openrouter/settings-providers-dark@2x.png) 

## 
		
	
	
		Breaking change: custom provider keys

Requests to language models now go through OpenRouter and are billed to your Hugging Face account or organization, so you can no longer use your own API key for a provider with these models. You can still pick a provider with a suffix on the model id (`model:provider`) or turn providers off in your settings, and your code stays the same. Custom keys for image and video providers keep working.

## 
		
	
	
		What's next

This is the first step of our partnership with OpenRouter. Next:

- Connect your OpenRouter account to Hugging Face.
- More tasks routed through OpenRouter.

Try a [model](https://huggingface.co/models?inference_provider=all&sort=trending&other=conversational), or read the [Inference Providers docs](https://huggingface.co/docs/inference-providers) to get started.
