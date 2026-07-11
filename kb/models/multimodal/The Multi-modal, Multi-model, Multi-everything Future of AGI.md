---
title: The Multi-modal, Multi-model, Multi-everything Future of AGI
topic: models
subtopic: multimodal
secondary_topics:
- industry/trends
summary: Essay on the multimodal, multi-model future of AGI and product implications.
source: latent-space
url: https://www.latent.space/p/multimodal-gpt4
author: Latent Space
published: '2023-03-15'
fetched: '2026-07-11T05:23:42Z'
classifier: codex
taxonomy_rev: 1
words: 1799
content_sha256: 41cfd0872d2c77db999a2d514a41e7103ce6281f0e495684ebd2d35e818775c7
---

# The Multi-modal, Multi-model, Multi-everything Future of AGI

# The Multi-modal, Multi-model, Multi-everything Future of AGI

### GPT-4 FOMO antidote, and meditations on Moravec's Paradox

As was rumored and [then confirmed by Microsoft Germany](https://www.heise.de/news/GPT-4-is-coming-next-week-and-it-will-be-multimodal-says-Microsoft-Germany-7540972.html), GPT-4 was released yesterday in ChatGPT with a [blogpost](https://openai.com/research/gpt-4), [paper](https://cdn.openai.com/papers/gpt-4.pdf), [livestream](https://www.youtube.com/watch?v=outcGtbnMuQ), and a couple of [short videos](https://www.youtube.com/watch?v=TxkJMX0KyS0):

![X avatar for @OpenAI](https://substackcdn.com/image/fetch/$s_!TnFC!,w_40,h_40,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack.com%2Fimg%2Favatars%2Fdefault-light.png)

To use simple measures of how anticipated this was - GPT-4 is already the [11th-most upvoted Hacker News story](https://hn.algolia.com/) of * ALL TIME, *the Developer Livestream got 1.5 million views in 20 hours (currently #5 trending video on all of YouTube) and the announcement

[tweet](https://twitter.com/OpenAI/status/1635687373060317185?s=20)got 4x more likes than the same for ChatGPT, itself the biggest story of 2022.

- “Today has been a great year in AI” - - [Tobi Lutke, Shopify CEO](https://twitter.com/tobi/status/1635755163615911936?s=20)
- “Not sure I can think of a time where there was this much unexplored territory with this much new capability in the hands of this many users.” - - [Karpathy](https://twitter.com/karpathy/status/1635749104059056128)

There are lots of screenshots and bad takes flying around, so I figure it would be most useful to do the same executive-summary-style recap [I did for ChatGPT](https://lspace.swyx.io/p/everything-we-know-about-chatgpt), for GPT-4.

## GPT-4 Executive Summary

GPT-4 is the newest version of OpenAI’s flagship language model. It is:

- **significantly better**at existing GPT-3 tasks (- *huge*improvements across both- [standard NLP benchmarks](https://twitter.com/swyx/status/1635690596416491521?s=20)- [1](https://www.latent.space#footnote-1)&- [human exams like the SAT/GRE](https://twitter.com/swyx/status/1635689844189036544)- [2](https://www.latent.space#footnote-2), and better- [instruction following](https://twitter.com/DanGrover/status/1635713083523084288?s=20)and- [world knowledge](https://twitter.com/DanHendrycks/status/1635706823373377538?s=20))
- capable of - **new**tasks- [3](https://www.latent.space#footnote-3)(enough- **math**to- [do your taxes](https://twitter.com/swyx/status/1635739184869826561)and- [beat Minerva](https://twitter.com/swyx/status/1635749861185445888)!)
- able to use - **8x more context**than ChatGPT (50 pages, 25k words of context means unlocks better AI-enabled coding- [4](https://www.latent.space#footnote-4)by- [simply pasting docs](https://www.youtube.com/live/outcGtbnMuQ?feature=share&t=516), or better chat by pasting- [entire Wikipedia articles](https://twitter.com/omarsar0/status/1635690756177379328), or even- [comparing two articles](https://www.youtube.com/live/outcGtbnMuQ?feature=share&t=319))
- **safer**to use (- [20-30% fewer hallucinations and unsafe content](https://twitter.com/swyx/status/1635693559348338688)- [5](https://www.latent.space#footnote-5))

That alone would qualify it as a huge release, but GPT-4 is *also* OpenAI’s first **multimodal** model, being able to * natively *understand image input as well as text. This is

**orders of magnitude better**than existing OCR and Image-to-Text (e.g.

[BLIP](https://pbs.twimg.com/media/FrNmIGKaQAAjDtU?format=jpg&name=large)) solutions and has to be seen to be fully understood, but the capabilities that you

*must*know include:

- **Converting**a sketch of a website into code (- [screenshot](https://twitter.com/rowancheung/status/1635744529587359756?s=20),- [demo timestamp](https://www.youtube.com/live/outcGtbnMuQ?feature=share&t=993))
- Fully - **describing**a- [screenshot](https://twitter.com/eerac/status/1635737216864452612)of a Discord app (- [demo timestamp](https://www.youtube.com/live/outcGtbnMuQ?feature=share&t=621))- [6](https://www.latent.space#footnote-6)
- **Summarizing**- *images*of a paper and answering questions about figures (- [screenshot](https://twitter.com/omarsar0/status/1635729572816732167))
- **Recognizing**photos (- [fridge](https://twitter.com/swyx/status/1635765117303521282?s=20),- [kitchen](https://twitter.com/omarsar0/status/1635689918696501257?s=20)), offering meal ideas (- [NYT article](https://www.nytimes.com/2023/03/14/technology/openai-gpt4-chatgpt.html))
- **Explaining**why an image is funny (- [ironing clothes, chicken nuggets, memes](https://twitter.com/swyx/status/1635692241523208195?s=20))

**GPT-4** can be tried out today by being a ChatGPT Plus subscriber ($20/month), while text API access is granted on [a waitlist](https://openai.com/waitlist/gpt-4-api) or by [contributing OpenAI Evals](https://github.com/openai/evals). The multimodal visual API capability is exclusive to [BeMyEyes](http://bemyeyes.com) for now. [API Pricing](https://openai.com/research/gpt-4#api) is now split into [prompt tokens and completion tokens](https://www.jonstokes.com/p/the-chat-stack-gpt-4-and-the-near) and is [30-60x higher than GPT-3.5](https://twitter.com/transitive_bs/status/1635712260424478720)[7](https://www.latent.space#footnote-7).

In a break from the past, OpenAI declined to release **any** technical details of GPT-4, citing competition and safety concerns. This means [the Small Circle, Big Circle memes](https://lspace.swyx.io/p/ok-foomer) were not confirmed nor denied[8](https://www.latent.space#footnote-8) and that another round of [criticism of OpenAI not being open](https://twitter.com/ykilcher/status/1635702708006006786?s=20) started again.

- **We know**: that GPT-4’s- [training started 2 years ago and ended in August 2022](https://www.youtube.com/watch?v=--khbXchTeE), that GPT-4’s data cutoff was Sept 2021- [9](https://www.latent.space#footnote-9).
- **We don’t know**: how the- **data**- [10](https://www.latent.space#footnote-10)- **, compute**- [11](https://www.latent.space#footnote-11)- **, hardware**- [12](https://www.latent.space#footnote-12)- **, parameters**- [13](https://www.latent.space#footnote-13)or training process changed from GPT-3.

In place of technical detail, OpenAI instead focused on demonstrating capabilities (explained above), [scaling](https://twitter.com/swyx/status/1635688942354980865?s=20) and safety research (done by OpenAI’s [Alignment Research Center](https://www.reddit.com/r/singularity/comments/11rfs22/openais_arc_challenges_gpt4_to_reproduce_and/)[14](https://www.latent.space#footnote-14)) and demonstrating usecases with launch partners in an impressively coordinated launch (with a full slate of [Built With GPT-4](https://openai.com/product/gpt-4#built-with-gpt-4) examples on launch day):

- Microsoft - [confirmed](https://techcrunch.com/2023/03/14/microsofts-new-bing-was-using-gpt-4-all-along/)that Prometheus was their codename for GPT-4, meaning all Bing/Sydney users were really GPT-4 users (worrying if you have seen- [Sydney’s issues](https://news.ycombinator.com/item?id=34804874)in the wild) and also- [increased Bing query limits](https://twitter.com/MParakhin/status/1635741730464059392)
- [Duolingo](https://twitter.com/duolingo/status/1635688521695633408)(- [blog](https://blog.duolingo.com/duolingo-max/)) demonstrated new Explain My Answer and Roleplay features for Spanish and French (though GPT-4 also speaks- [many other languages](https://pbs.twimg.com/media/FrMj4PAaAAElZRV?format=png&name=900x900))
- [Stripe](https://openai.com/customer-stories/stripe)tested 15 use cases across support customization,- [answering docs questions](https://twitter.com/bentossell/status/1636021529040375810), and fraud detection.
- [Intercom](https://twitter.com/destraynor/status/1635705915595685902?s=20)(- [Eoghan](https://twitter.com/eoghan/status/1635707829939240960),- [blog](https://www.intercom.com/ai-bot)) launched their Fin chatbot, which reduces hallucinations (incl about competitors), disambiguates, and hands over to human agents
- [DoNotPay](https://twitter.com/jbrowder1/status/1635720431091974157)teased "one click lawsuits" for robocallers and- [emails without unsubscribe](https://twitter.com/cocksure_crypto/status/1635722368487129088?s=20)

**Race Dynamics. **The coordination reached beyond OpenAI - GPT-4 wasn’t the only foundation model launch of Tuesday. Both Google and Anthropic launched their [PaLM API](https://developers.googleblog.com/2023/03/announcing-palm-api-and-makersuite.html)[15](https://www.latent.space#footnote-15) and [Claude+](https://www.anthropic.com/index/introducing-claude) models as well, with [Quora Poe](https://twitter.com/adamdangelo/status/1635690625642397696) being the first app to launch with *both* OpenAI GPT-4 AND Anthropic’s Claude+ models. This ultra-competitive launch cycle across companies [on Pi Day](https://twitter.com/EigenGender/status/1635766846719934465?s=20) smacks of [last month’s Google vs Microsoft race for special events](https://twitter.com/xlr8harder/status/1622849293571817472) and is causing concern from AI safety worriers and sleep-deprived Substack writers alike.

*(end of summary! phew! but discussions ongoing @  Hacker News and Twitter)*

## The Year of Multimodal vs Multimodel AI

GPT-4’s Multimodality is a glimpse of the AGI future to come. It didn’t end up fitting all the speculated capabilities - it doesn’t have image output, and audio was notably missing from the accepted inputs given the Whisper API release, but Jim Fan’s hero image here was mostly spot on:

![X avatar for @DrJimFan](https://substackcdn.com/image/fetch/$s_!TnFC!,w_40,h_40,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack.com%2Fimg%2Favatars%2Fdefault-light.png)

![](https://pbs.substack.com/media/Fq4AeOHWwBEKFjK.jpg)

However, 3 days ago Microsoft Research China released *another *approach to multiple modalities with Visual ChatGPT, allowing you to converse with your images the same as GPT-4:

![X avatar for @mathemagic1an](https://substackcdn.com/image/fetch/$s_!TnFC!,w_40,h_40,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack.com%2Fimg%2Favatars%2Fdefault-light.png)

![](https://res.cloudinary.com/hhsslviub/video/upload/e_loop,vs_40/p0eyusmfum1ydx1kyc0s.gif)

This is a multi-modal project, but is more accurately described as a multi-*model* project, because it really is basically “22 models in a trenchcoat[16](https://www.latent.space#footnote-16)”:

![X avatar for @swyx](https://substackcdn.com/image/fetch/$s_!TnFC!,w_40,h_40,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack.com%2Fimg%2Favatars%2Fdefault-light.png)

![](https://pbs.substack.com/media/Fq1y-K3aQAIVQ0H.jpg)

This hints at two ways of achieving multi-modality - the cheap way (chaining together models, likely with [LangChain](https://langchain.com/)), and the "right" way (training and embedding on mixed modality datasets). We have some reason to believe that multimodal training gives benefits over and above single modality training - in the same way that adding a corpus of code to language model training has been observed to improve results for non-code natural language, we might observe that teaching an AI what something looks like improves their ability to describe it and vice versa[17](https://www.latent.space#footnote-17).

Even being single-modality but multi-*model* is proving to be useful. Quora founder [Adam D’Angelo ](https://twitter.com/adamdangelo/status/1635690630289723394)chose to launch his new Poe bot with *both* OpenAI GPT-4 and Anthropic Claude support, and former GitHub CEO [Nat Friedman built nat.dev](https://twitter.com/natfriedman/status/1633582489850773504?s=20) to help compare outputs across the largest possible range of text models:

![X avatar for @omarsar0](https://substackcdn.com/image/fetch/$s_!TnFC!,w_40,h_40,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack.com%2Fimg%2Favatars%2Fdefault-light.png)

![](https://pbs.substack.com/media/Fqu5POjX0AIRHHb.jpg)

Eliezer Yudkowsky has also [commented](https://twitter.com/ESYudkowsky/status/1635577836525469697) that being multi-model can be useful for model distillation as well, with the recent [Stanford Alpaca result](https://news.ycombinator.com/item?id=35141531) finetuning [Meta’s LLaMa](https://simonwillison.net/2023/Mar/13/alpaca/) off of GPT-3 to achieve comparable results with a 25x smaller model.

This seems to be a tremendously fruitful area of development (not forgetting [Palm-E](https://twitter.com/dannydriess/status/1632904675124035585?s=46&t=90xQ8sGy63D2OtiaoGJuww), [Kosmos-1](https://twitter.com/DrJimFan/status/1634245855061352461), [ViperGPT](https://twitter.com/_akhaliq/status/1635811899030814720), and other developments I don’t have room to cover) and I expect multimodal, multimodel developments to dominate research and engineering cycles through at least the rest of 2023, edging us closer and closer to the AGI event horizon.

## AGI = Multi-everything and Moravec’s Paradox

[Moravec’s Paradox](https://en.wikipedia.org/wiki/Moravec%27s_paradox) can be summarized as “computers find easy things that humans find hard, and vice versa”. But human capabilities evolve about 100,000x slower than computers, and it does not take long for computers to go from sub-human to super-human. By now we are familiar with the idea that LLMs are effortlessly **multilingual **(across the most popular human and programming languages, but also increasingly with lower resource languages) and **multidisciplinary** (GPT-4 simultaneously capable of being a great sommelier, law student, med student and coder, though [english lit is safe](https://twitter.com/alexlmiller/status/1635779785464098816)).

But those are merely just two dimensions we can think of. OpenAI ARC and [Meta FAIR](https://www.science.org/doi/10.1126/science.ade9097) tested AI’s ability to be duplicitious, and we are increasingly seeing AI be **effortlessly multi-personality** as well - with [the Waluigi Effect](https://knowyourmeme.com/memes/waluigi-effect-artificial-intelligence) recently entering the AI discourse as a formal shorthand and Bing’s Sydney showing wildly disturbing alternative personalities variously known as [Venom](https://stratechery.com/2023/from-bing-to-sydney-search-as-distraction-sentient-ai/) and [Dark Sydney](https://www.google.com/search?q=%22dark+sydney%22+bing&rlz=1C5CHFA_enSG1006SG1006&sxsrf=AJOqlzXdg8o2TVMnEhRwfPCMPb75ZmPNtA%3A1678903264367&ei=4AcSZLr8FZCv0PEPoJaF6Ak&ved=0ahUKEwi67LyFwt79AhWQFzQIHSBLAZ0Q4dUDCBE&uact=5&oq=%22dark+sydney%22+bing&gs_lcp=Cgxnd3Mtd2l6LXNlcnAQAzIECCMQJzoICAAQhgMQsAM6BwgjELACECdKBAhBGAFQ6wZYlhhg2xloAXAAeACAAVCIAZoCkgEBNJgBAKABAcgBAsABAQ&sclient=gws-wiz-serp#ip=1). And yet we press on.

AI is under no obligation to only be multi- *in ways that we expect*. I am reminded of the ending of the movie Her, when Joaquin Pheonix learns that Samantha is simultaneously in love with 641 people, a number so big it boggles his mind but is functionally the same as loving 1 person for a multi-everything AI:

[Moloch](https://lspace.swyx.io/p/google-vs-openai#%C2%A7ai-moloch), thy name is race dynamics.

[1](https://www.latent.space#footnote-anchor-1)

Dan Hendrycks, author of MMLU, [commented](https://twitter.com/danhendrycks/status/1635706822387699713) that “*Since it gets 86.4% on our MMLU benchmark, that suggests GPT-4.5 should be able to reach expert-level performance. GPT-4: Language Models are... Almost Omniscient*”

[3](https://www.latent.space#footnote-anchor-3)

Users are finding other usecases in [credit card enrichment](https://twitter.com/Shpigford/status/1635748608879337472), [drug discovery](https://twitter.com/danshipper/status/1635712019549786113), [date matching](https://twitter.com/jakozloski/status/1635778263787110401), [waifu calculus](https://twitter.com/gfodor/status/1635713792440176640) - though these amateur tests often [overstate](https://twitter.com/jbittker/status/1635763155895742464?s=20) their claims for clout. EDIT: it can also sufficiently administer a [Reverse Turing Test](https://gist.github.com/rain-1/3bf56122b0ebeac929dff0f881ee8e4c) to distinguish between ChatGPT and Human answers.

[4](https://www.latent.space#footnote-anchor-4)

Good GPT-4 code demos in [lambda calculus parser](https://twitter.com/VictorTaelin/status/1635726202231988225) and writing [C++, Bazel, Terraform](https://twitter.com/sualehasif996/status/1635755267739598848), [adding background animation](https://twitter.com/mortenjust/status/1635935702553886722?s=20)s, or [creating Pong](https://twitter.com/skirano/status/1635736107949195278?s=20), [Snake ](https://twitter.com/ammaar/status/1635754631228952576?s=20)or [Game of life](https://twitter.com/felixbade/status/1635799243628892160) or [Midi scripts](https://twitter.com/ProleBrain/status/1635832735863570434).

Although it still does surprisingly poorly on [Leetcode](https://twitter.com/bio_bootloader/status/1635701806310518790) and [inexplicably poorly on AMC10 (easier) vs AMC12 (harder)](https://twitter.com/BlancheMinerva/status/1635810135573495809?s=20).

[5](https://www.latent.space#footnote-anchor-5)

But still imperfect - already some [regressions](https://twitter.com/RazRazcle/status/1635966297715490817) in hallucinations and [jailbreaks](https://twitter.com/nomic_ai/status/1635719257110478859) found ([DAN-style](https://github.com/0xk1h0/ChatGPT_DAN) prompt injections still work)

[6](https://www.latent.space#footnote-anchor-6)

This was my personal favorite part of the demo - it means that desktop agents like [Adept](https://adept.ai/) (which just raised [a $350m Series ](https://www.forbes.com/sites/kenrickcai/2023/03/14/adept-ai-startup-raises-350-million-series-b/)B), [Embra](https://embra.app/), and [Uni.ai](https://news.ycombinator.com/user?id=deet) or [Minion.ai](https://twitter.com/alexgraveley/status/1631693523748519940) can get VERY good:

![X avatar for @sharifshameem](https://substackcdn.com/image/fetch/$s_!TnFC!,w_40,h_40,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack.com%2Fimg%2Favatars%2Fdefault-light.png)

[7](https://www.latent.space#footnote-anchor-7)

In the lead up to GPT-4, Sam Altman hinted at higher pricing for smarter models:

![X avatar for @sama](https://substackcdn.com/image/fetch/$s_!TnFC!,w_40,h_40,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack.com%2Fimg%2Favatars%2Fdefault-light.png)

[8](https://www.latent.space#footnote-anchor-8)

Sam Altman [seems to acknowledge](https://twitter.com/sama/status/1635709792319868930?s=20) trolling the grifters was intentional.

[9](https://www.latent.space#footnote-anchor-9)

There is some confusion as [some people ](https://www.youtube.com/watch?v=2zW33LfffPc)report GPT-3.5’s cutoff was Dec 2021.

[10](https://www.latent.space#footnote-anchor-10)

There is some evidence of data contamination skewing benchmarks for [leetcode](https://twitter.com/rUv/status/1635756651717496832?s=20) and [codeforces](https://twitter.com/cHHillee/status/1635790330854526981), and without further detail it is difficult to confirm this.

[11](https://www.latent.space#footnote-anchor-11)

Yannic Kilcher guessed from the [scaling chart](https://twitter.com/swyx/status/1635711620889587712) that GPT-4 might have used 1000x more compute than GPT-3 but this is all wild guessing.

[12](https://www.latent.space#footnote-anchor-12)

We know GPT-3 was trained with [10,000 Nvidia GPUs](https://twitter.com/AndyChenML/status/1611529311390949376), and have hints that new clusters are [10x more powerful](https://twitter.com/EMostaque/status/1612660862627762179?s=20). Azure announced a new OpenAI cluster [last November](https://techcrunch.com/2022/11/16/microsoft-and-nvidia-team-up-to-build-new-azure-hosted-ai-supercomputer/) but this is not live yet.

[13](https://www.latent.space#footnote-anchor-13)

Brave souls will NOT click to obtain [illegally leaked GPT-4 weights](https://twitter.com/giffmana/status/1635761150611664899?s=20).

[14](https://www.latent.space#footnote-anchor-14)

ARC is greatly [criticized by the AI safety community](https://twitter.com/YosarianTwo/status/1635785141841698816) for testing GPT-4’s ability to “set up copies of itself” and “increase its own robustness”

[15](https://www.latent.space#footnote-anchor-15)

Google’s launch is criticized for being [weirdly opaque](https://twitter.com/harishkgarg/status/1635941404961837058?s=20), although their AI across [Workspaces launch](https://twitter.com/benparr/status/1635684322261729282?s=20) was [much better received](https://www.youtube.com/watch?v=6DaJVZBXETE). Still it [reinforced existing concerns](https://twitter.com/Suhail/status/1635866358067113986?s=20) about Google’s ability to ship vs OpenAI’s incredible momentum over the past year:

![X avatar for @E0M](https://substackcdn.com/image/fetch/$s_!TnFC!,w_40,h_40,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack.com%2Fimg%2Favatars%2Fdefault-light.png)

[16](https://www.latent.space#footnote-anchor-16)

With the “trenchcoat” being 900 lines of the most “researcher quality” code you’ve ever seen

[17](https://www.latent.space#footnote-anchor-17)

Though multimodal AI will still struggle with [Rene Magritte](https://en.wikipedia.org/wiki/The_Treachery_of_Images)!

To me, Alpaca totally stole GPT-4's thunder.

GPT-4 is also able to distinguish writing styles of known authors https://twitter.com/vagabondjack/status/1637468848122396672
