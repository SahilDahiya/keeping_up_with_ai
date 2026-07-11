---
title: Captaining IMO Gold, Deep Think, On-Policy RL, Feeling the AGI in Singapore
  — Yi Tay
topic: models
subtopic: reasoning
secondary_topics:
- models/fine-tuning
summary: Covers Deep Think, on-policy RL, and mathematical reasoning lessons from
  IMO-style model development.
source: latent-space
url: https://www.latent.space/p/captaining-imo-gold-deep-think-on
author: Latent Space
published: '2026-01-23'
fetched: '2026-07-11T05:15:28Z'
classifier: codex
taxonomy_rev: 1
words: 735
content_sha256: e1d92650ea8d5b328dab84d15a9f185d30a214516f8a159b404bf6fd13728d57
---

# Captaining IMO Gold, Deep Think, On-Policy RL, Feeling the AGI in Singapore — Yi Tay

From shipping **Gemini Deep Think** and **IMO Gold** to launching the **Reasoning and AGI team in Singapore**, **Yi Tay** has spent the last 18 months living through the full arc of Google DeepMind’s pivot from architecture research to RL-driven reasoning—watching his team go from a dozen researchers to 300+, training models that solve International Math Olympiad problems in a live competition, and building the infrastructure to scale deep thinking across every domain, and driving Gemini to the top of the leaderboards across every category. Yi Returns to dig into the inside story of the IMO effort and more!

We discuss:

- Yi’s path: - **Brain → Reka → Google DeepMind → Reasoning and AGI team Singapore**, leading model training for Gemini Deep Think and IMO Gold
- The - **IMO Gold story**: four co-captains (Yi in Singapore, Jonathan in London, Jordan in Mountain View, and Tong leading the overall effort), training the checkpoint in ~1 week, live competition in Australia with professors punching in problems as they came out, and the tension of not knowing if they’d hit Gold until the human scores came in (because the Gold threshold is a percentile, not a fixed number)
- Why they - **threw away AlphaProof**: “If one model can’t do it, can we get to AGI?” The decision to abandon symbolic systems and bet on end-to-end Gemini with RL was bold and non-consensus
- **On-policy vs. off-policy RL**: off-policy is imitation learning (copying someone else’s trajectory), on-policy is the model generating its own outputs, getting rewarded, and training on its own experience—”humans learn by making mistakes, not by copying”
- Why - **self-consistency and parallel thinking**are fundamental: sampling multiple times, majority voting, LM judges, and internal verification are all forms of self-consistency that unlock reasoning beyond single-shot inference
- The - **data efficiency frontier**: humans learn from 8 orders of magnitude less data than models, so where’s the bug? Is it the architecture, the learning algorithm, backprop, off-policyness, or something else?
- Three schools of thought on - **world models**: (1) Genie/spatial intelligence (video-based world models), (2) Yann LeCun’s JEPA + FAIR’s code world models (modeling internal execution state), (3) the amorphous “resolution of possible worlds” paradigm (curve-fitting to find the world model that best explains the data)
- Why - **AI coding crossed the threshold**: Yi now runs a job, gets a bug, pastes it into Gemini, and relaunches without even reading the fix—”the model is better than me at this”
- The - **Pokémon benchmark**: can models complete Pokédex by searching the web, synthesizing guides, and applying knowledge in a visual game state? “Efficient search of novel idea space is interesting, but we’re not even at the point where models can consistently apply knowledge they look up”
- **DSI and generative retrieval**: re-imagining search as predicting document identifiers with semantic tokens, now deployed at YouTube (symmetric IDs for RecSys) and Spotify
- Why - **RecSys and IR feel like a different universe**: “modeling dynamics are strange, like gravity is different—you hit the shuttlecock and hear glass shatter, cause and effect are too far apart”
- The - **closed lab advantage is increasing**: the gap between frontier labs and open source is growing because ideas compound over time, and researchers keep finding new tricks that play well with everything built before
- Why - **ideas still matter**: “the last five years weren’t just blind scaling—transformers, pre-training, RL, self-consistency, all had to play well together to get us here”
- **Gemini Singapore**: hiring for RL and reasoning researchers, looking for track record in RL or exceptional achievement in coding competitions, and building a small, talent-dense team close to the frontier

—

Yi Tay

- Google DeepMind: https://deepmind.google

**Full Video Episode**

## Timestamps

[00:00:00](https://www.youtube.com/watch?v=unUeI7e-iVs) Introduction: Returning to Google DeepMind and the Singapore AGI Team[00:04:52](https://www.youtube.com/watch?v=unUeI7e-iVs&t=292s) The Philosophy of On-Policy RL: Learning from Your Own Mistakes[00:12:00](https://www.youtube.com/watch?v=unUeI7e-iVs&t=720s) IMO Gold Medal: The Journey from AlphaProof to End-to-End Gemini[00:21:33](https://www.youtube.com/watch?v=unUeI7e-iVs&t=1293s) Training IMO Cat: Four Captains Across Three Time Zones[00:26:19](https://www.youtube.com/watch?v=unUeI7e-iVs&t=1579s) Pokemon and Long-Horizon Reasoning: Beyond Academic Benchmarks[00:36:29](https://www.youtube.com/watch?v=unUeI7e-iVs&t=2189s) AI Coding Assistants: From Lazy to Actually Useful[00:32:59](https://www.youtube.com/watch?v=unUeI7e-iVs&t=1979s) Reasoning, Chain of Thought, and Latent Thinking[00:44:46](https://www.youtube.com/watch?v=unUeI7e-iVs&t=2686s) Is Attention All You Need? Architecture, Learning, and the Local Minima[00:55:04](https://www.youtube.com/watch?v=unUeI7e-iVs&t=3304s) Data Efficiency and World Models: The Next Frontier[01:08:12](https://www.youtube.com/watch?v=unUeI7e-iVs&t=4092s) DSI and Generative Retrieval: Reimagining Search with Semantic IDs[01:17:59](https://www.youtube.com/watch?v=unUeI7e-iVs&t=4679s) Building GDM Singapore: Geography, Talent, and the Symposium[01:24:18](https://www.youtube.com/watch?v=unUeI7e-iVs&t=5058s) Hiring Philosophy: High Stats, Research Taste, and Student Budgets[01:28:49](https://www.youtube.com/watch?v=unUeI7e-iVs&t=5329s) Health, HRV, and Research Performance: The 23kg Journey
