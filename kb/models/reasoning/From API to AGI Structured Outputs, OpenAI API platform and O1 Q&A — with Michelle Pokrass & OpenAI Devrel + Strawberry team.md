---
title: 'From API to AGI: Structured Outputs, OpenAI API platform and O1 Q&A — with
  Michelle Pokrass & OpenAI Devrel + Strawberry team'
topic: models
subtopic: reasoning
secondary_topics:
- prompt-engineering/structured-output
summary: OpenAI API and o1 Q&A covering structured outputs, platform direction, and
  reasoning-model use.
source: latent-space
url: https://www.latent.space/p/openai-api-and-o1
author: Latent Space
published: '2024-09-13'
fetched: '2026-07-11T05:20:12Z'
classifier: codex
taxonomy_rev: 1
words: 1088
content_sha256: 48921e26cccddafa476ba0c6cfe0aced92da0b36827a9fe249a06118badbea99
---

# From API to AGI: Structured Outputs, OpenAI API platform and O1 Q&A — with Michelle Pokrass & OpenAI Devrel + Strawberry team

*Congrats to Damien on successfully running  AI Engineer London! See our community page and the Latent Space Discord for all upcoming events.*

This podcast came together in a far more convoluted way than usual, but happens to result in a tight 2 hours covering **the ENTIRE OpenAI product suite across ChatGPT-latest, GPT-4o and the new o1 models**, and how they are delivered to AI Engineers in the API via the new Structured Output mode, Assistants API, client SDKs, upcoming Voice Mode API, Finetuning/Vision/Whisper/Batch/Admin/Audit APIs, and everything else you need to know to be up to speed in September 2024.

This podcast has two parts: the first hour is a regular, well edited, podcast on 4o, Structured Outputs, and the rest of the OpenAI API platform. The second was a rushed, noisy, hastily cobbled together recap of the top takeaways from the o1 model release from yesterday and today.

## Building AGI with Structured Outputs — Michelle Pokrass of OpenAI API team

** Michelle Pokrass** built massively scalable platforms at Google, Stripe, Coinbase and Clubhouse, and now leads the API Platform at Open AI. She joins us today to talk about why structured output is such an important modality for AI Engineers that Open AI has now trained and engineered a

[Structured Output mode](https://openai.com/index/introducing-structured-outputs-in-the-api/)with 100% reliable JSON schema adherence.

![](https://substackcdn.com/image/fetch/$s_!BvRM!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe43ed2c3-cc06-4a7e-bda3-82ce742ac69c_1028x575.png)

To understand why this is important, a bit of history is important:

- June 2023 when OpenAI first added a "function calling" capability to GPT-4-0613 and GPT 3.5 Turbo 0613 ( - [our podcast/writeup here](https://www.latent.space/p/function-agents))
- November 2023’s OpenAI Dev Day ( - [our podcast/writeup here](https://www.latent.space/p/devday)) where the team shipped JSON Mode, a simpler schema-less JSON output mode that nevertheless became more popular because function calling often failed to match the JSON schema given by developers.
- Meanwhile, in open source, many solutions arose, including - **Instructor**(- [our pod with Jason here](https://www.latent.space/p/instructor?utm_source=publication-search))
- **LangChain**(- [our pod with Harrison here](https://www.latent.space/p/langchain), and he is returning next as a guest co-host)
- **Outlines**(- [Remi Louf’s talk at AI Engineer here](https://x.com/remilouf/status/1806331535852704134))
- Llama.cpp’s - [constrained grammar sampling](https://github.com/ggerganov/llama.cpp/blob/master/grammars/README.md)using GGML-BNF

- April 2024: - [OpenAI started implementing constrained sampling](https://x.com/gdb/status/1784990428854391173)with a new `- `tool_choice: required`` parameter in the API
- August 2024: the new - [Structured Output mode](https://openai.com/index/introducing-structured-outputs-in-the-api/), co-led by Michelle
- Sept 2024: - [Gemini shipped Structured Outputs](https://x.com/OfficialLoganK/status/1833226001670934827)as well

We sat down with Michelle to talk through every part of the process, as well as quizzing her for updates on everything else the API team has shipped in the past year, from the Assistants API, to Prompt Caching, GPT4 Vision, Whisper, the upcoming Advanced Voice Mode API, OpenAI Enterprise features, and why every Waterloo grad seems to be a cracked engineer.

## Part 1 Timestamps and Transcript

- [00:00:42] - [Episode Intro from Suno](https://suno.com/song/eed1b9c6-526c-480a-8bff-64f0908ffcb1)
- [00:03:34] Michelle's Path to OpenAI
- [00:12:20] Scaling ChatGPT
- [00:13:20] Releasing Structured Output
- [00:16:17] Structured Outputs vs Function Calling
- [00:19:42] JSON Schema and Constrained Grammar
- [00:20:45] OpenAI API team
- [00:21:32] Structured Output Refusal Field
- [00:24:23] ChatML issues
- [00:26:20] Function Calling Evals
- [00:28:34] Parallel Function Calling
- [00:29:30] Increased Latency
- [00:30:28] Prompt/Schema Caching
- [00:30:50] Building Agents with Structured Outputs: from API to AGI
- [00:31:52] Assistants API
- [00:34:00] Use cases for Structured Output
- [00:37:45] Prompting Structured Output
- [00:39:44] Benchmarking Prompting for Structured Outputs
- [00:41:50] Structured Outputs Roadmap
- [00:43:37] Model Selection vs GPT4 Finetuning
- [00:46:56] Is Prompt Engineering Dead?
- [00:47:29] 2 models: ChatGPT Latest vs GPT 4o August
- [00:50:24] Why API => AGI
- [00:52:40] Dev Day
- [00:54:20] Assistants API Roadmap
- [00:56:14] Model Reproducibility/Determinism issues
- [00:57:53] Tiering and Rate Limiting
- [00:59:26] OpenAI vs Ops Startups
- [01:01:06] Batch API
- [01:02:54] Vision
- [01:04:42] Whisper
- [01:07:21] Voice Mode API
- [01:08:10] Enterprise: Admin/Audit Log APIs
- [01:09:02] Waterloo grads
- [01:10:49] Books
- [01:11:57] Cognitive Biases
- [01:13:25] Are LLMs Econs?
- [01:13:49] Hiring at OpenAI

## Emergency O1 Meetup — OpenAI DevRel + Strawberry team

*the following is our  writeup from AINews, which so far stands the test of time.*

o1, aka Strawberry, aka Q*, is [finally out](https://openai.com/o1/#snake-video)! There are two models we can use today: o1-preview (the bigger one priced at $15 in / $60 out) and o1-mini (the STEM-reasoning focused distillation priced at $3 in/$12 out) - and the main o1 model is still in training. This caused a little [bit of confusion](https://x.com/giffmana/status/1834306463142949338).

![image.png image.png](https://substackcdn.com/image/fetch/$s_!gbJ4!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb8449916-3ab8-42c6-9a91-8b5c332cac7b_960x1262.png)

There are a raft of relevant links, so don’t miss:

- the - [o1 Hub](https://openai.com/o1/#snake-video)
- the - [o1-mini blogpost](https://news.ycombinator.com/item?id=41523050)
- the - [o1 system card](https://openai.com/index/openai-o1-system-card/)
- the - [platform docs](https://platform.openai.com/docs/guides/reasoning)
- the o1 team video and - [contributors list](https://www.notion.so/ainews-draft-479a38e041fe4ab4b05d6f90573d967d?pvs=21)(- [twitter](https://x.com/polynoamial/status/1834346060170367031))

Inline with the many, many leaks leading up to today, the core story is longer “test-time inference” aka longer step by step responses - in the ChatGPT app this shows up as a new “thinking” step that you can click to expand for reasoning traces, even though, controversially, they are hidden from you (interesting conflict of interest…):

![image.png image.png](https://substackcdn.com/image/fetch/$s_!M4xz!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F1f53ab0a-477e-4eab-94a9-7615181cf178_960x776.png)

Under the hood, o1 is trained for adding new **reasoning tokens** - which you pay for, and OpenAI has accordingly extended the output token limit to >30k tokens (incidentally this is also why a number of API parameters from the other models like `temperature` and `role` and tool calling and streaming, but especially `max_tokens` is no longer supported).

![image.png image.png](https://substackcdn.com/image/fetch/$s_!j-zL!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F69fb5f90-3c5f-408a-89a6-c0d3ca8a8821_960x1100.png)

The evals are exceptional. OpenAI o1:

- ranks in the 89th percentile on competitive programming questions (Codeforces),
- places among the top 500 students in the US in a qualifier for the USA Math Olympiad (AIME),
- and exceeds human PhD-level accuracy on a benchmark of physics, biology, and chemistry problems (GPQA).

![image.png image.png](https://substackcdn.com/image/fetch/$s_!zTZg!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F1ab001f3-82ec-4525-a3d6-6dbca3224a38_960x853.png)

You are used to new models showing flattering charts, but there is one of note that you don’t see in many model announcements, that is probably the most important chart of all. Dr Jim Fan gets it right: we now have **scaling laws for test time compute, and it looks like they scale loglinearly**.

![image.png image.png](https://substackcdn.com/image/fetch/$s_!sH61!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F6f5423bf-1aa1-40f8-8041-afbb51f21000_960x1361.png)

We unfortunately may never know the drivers of the reasoning improvements, but [Jason Wei shared some hints](https://x.com/_jasonwei/status/1834278706522849788?s=46):

![image.png image.png](https://substackcdn.com/image/fetch/$s_!KSDp!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fab1d077c-9217-4a24-a363-5fd462f71fe3_960x1181.png)

Usually the big model gets all the accolades, but notably many are calling out the performance of o1-mini for its size (smaller than gpt 4o), so do not miss that.

![image.png image.png](https://substackcdn.com/image/fetch/$s_!vq9-!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc43e23f2-1dfc-4809-ac68-b8ffc5f7698c_960x523.png)

## Part 2 Timestamps

- [01:15:01] O1 transition
- [01:16:07] O1 Meetup Recording
- [01:38:38] OpenAI Friday AMA recap
- [01:44:47] Q&A Part 2
- [01:50:28] O1 Demos

![](https://substackcdn.com/image/fetch/$s_!Hq64!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe1ca0d93-0e9f-45ee-b933-5f5c7be57841_882x568.png)

![](https://substackcdn.com/image/fetch/$s_!yGx1!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fff127a23-6148-4c50-8521-123c4ecfdf33_1026x574.png)
