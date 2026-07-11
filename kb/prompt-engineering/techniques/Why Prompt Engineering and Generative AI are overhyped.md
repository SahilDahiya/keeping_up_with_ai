---
title: Why "Prompt Engineering" and "Generative AI" are overhyped
topic: prompt-engineering
subtopic: techniques
secondary_topics:
- industry/trends
summary: Early essay on why prompt engineering and generative AI were overhyped, useful
  as historical context for prompt technique limits.
source: latent-space
url: https://www.latent.space/p/why-prompt-engineering-and-generative
author: Latent Space
published: '2022-11-25'
fetched: '2026-07-11T05:24:06Z'
classifier: codex
taxonomy_rev: 1
words: 1914
content_sha256: 177fbce2b2c92002809ec5b264bec7148dbe98af22e89eddedaeba61e2618764
---

# Why "Prompt Engineering" and "Generative AI" are overhyped

# Why "Prompt Engineering" and "Generative AI" are overhyped

### How Stable Diffusion 2.0 and Meta's Galactica demonstrate the two heresies of AI

"Prompt Engineering" and "Generative AI" are all the rage.

So... why do the founders of OpenAI, Stability AI, and others hate those terms?

We’ll develop some insight in to what’s *after* prompts and generative AI, by exploring recent events.

## Stable Diffusion 2.0

[Stable Diffusion 2.0](https://stability.ai/blog/stable-diffusion-v2-release) was released yesterday to [a lot of excitement](https://news.ycombinator.com/item?id=33726816). Apart from added upscaling, inpainting, and depth-guidance features, a lot of the emphasis on how SD2 is better than SD1 centered on the [FID](https://en.wikipedia.org/wiki/Fr%C3%A9chet_inception_distance) and [CLIP score](https://wandb.ai/dalle-mini/dalle-mini/reports/OpenAI-CLIP-Score-exploration--VmlldzoxNjMwODM1) profile improvements:

![](https://substackcdn.com/image/fetch/$s_!gM3F!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F681286aa-fe56-42a5-8031-71308e99c829_952x815.png)

But the users actually trying it out had a different response:

![](https://substackcdn.com/image/fetch/$s_!pzRV!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F58736886-92c4-43cc-be3b-ddad2814db49_695x399.png)

[https://www.reddit.com/r/StableDiffusion/comments/z3ferx/xy_plot_comparisons_of_sd_v15_ema_vs_sd_20_x768/](https://www.reddit.com/r/StableDiffusion/comments/z3ferx/xy_plot_comparisons_of_sd_v15_ema_vs_sd_20_x768/)

![](https://substackcdn.com/image/fetch/$s_!cJjQ!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Fb0740370-b440-4bf1-b094-563372dfea17_588x514.png)

[twitter anon](https://twitter.com/xlr8harder/status/1595838086684246016)

The primary changes have been explained on [Reddit](https://www.reddit.com/r/StableDiffusion/comments/z36mm2/comment/ixkgs83/?utm_source=reddit&utm_medium=web2x&context=3) and [Twitter](https://twitter.com/EMostaque/status/1595731398450634755), but the biggest change was switching from OpenAI’s CLIP-L14 model (from [Jan 2021](https://openai.com/blog/clip/)) to LAION’s OpenCLIP Vit-H14 (from [Sep 2022](https://laion.ai/blog/large-openclip/) - [polar bear Hong Kong UFO teaser image from LAION](https://mobile.twitter.com/laion_ai/status/1570512017949339649) - [extra context from huggingface](https://twitter.com/wightmanr/status/1570503598538379264), trained on [LAION-5B](https://laion.ai/blog/laion-5b/) from March 2022). So we went from a black box where attribution (e.g. how much of “greg rutkowski” did we use in generating this image?) was impossible, to a more interrogable situation with [CLIP retrieval](https://rom1504.github.io/clip-retrieval/?back=https%3A%2F%2Fknn5.laion.ai&index=laion5B&useMclip=false) (and [Have I Been Trained](https://haveibeentrained.com/)), but also a lot of existing expectations were shattered[1](https://www.latent.space#footnote-1).

Of course, most Stable Diffusion users don’t care about the precise details so much as the results that it can generate, so people spent their Thanksgiving dutifully generating SD1 vs SD2 comparisons:

![](https://substackcdn.com/image/fetch/$s_!xilP!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F92047e34-eabc-4346-a93a-b3ce52e9efd8_591x881.png)

[@dannypostmaa](https://twitter.com/dannypostmaa/status/1595612366770954242)

![](https://substackcdn.com/image/fetch/$s_!tNBM!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F28f7be15-52ad-4125-b722-494dcd9bfb7a_754x789.png)

[/u/lkewis](https://www.reddit.com/r/StableDiffusion/comments/z3ferx/xy_plot_comparisons_of_sd_v15_ema_vs_sd_20_x768/)

![](https://substackcdn.com/image/fetch/$s_!Qsg-!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F826638d8-bbdd-4b4d-a06c-9c0fa9b05e0a_589x552.png)

[@AddyOsmani](https://twitter.com/addyosmani/status/1595922692934275073)

If you looked closely and couldn’t decide if SD2 was better than SD1, **you weren’t alone**. It should not be overlooked that the SD2.0 release announcement’s big hero image was a landscape image, subtly hinting that perhaps that is where Stability is advertising its capabilities, perhaps diverting attention from areas (NSFW, celebrities, modern artists that could sue Stability AI) that might have become worse.

That said:

- the task of deciding if a generated image is “better” or “worse” is quite subjective and hard to quantify across a literally infinite unbounded latent space - FID scores being the best we have so far.
- **prompts are a moving target**- the same prompt generates different things in SD1 vs Midjourney 3 vs Midjourney 4 vs Dall-E 2 vs SD2 - and users will discover new magic keywords and best practices (more heavily using- [negative prompts](https://twitter.com/minimaxir/status/1596021315630424065?s=20&t=XYmz0khLlgleKxemrtFUTg), though they were- [already a thing in SD1](https://www.reddit.com/r/StableDiffusion/comments/xt9ou9/i_solved_hands_for_now/)- UPDATE: more- [from Minimaxir on 29 Nov](https://minimaxir.com/2022/11/stable-diffusion-negative-prompt/)) that subjectively improve results. So perhaps SD2 initially looks “worse” than SD1, but then improves as users learn how to wield it better.

It’s most likely that SD2 will just be treated as a completely different model than a strict superset of SD1. Some SD apps have already “[reverted to SD1](https://twitter.com/PromptArtApp/status/1596035781449351169)”, and I expect SD2 to be offered as one of a growing list of “SD variants” (tracked on [my repo](https://github.com/sw-yx/prompt-eng/#sd-major-forks) since this is a fast moving list).

## “Prompt Engineering” is a Product Smell

User frustration is understandable, but the discovery that prompts “break” when you switch models should not surprise anyone remotely technical. It is tacit, incidental complexity that arises out of our inability to know/communicate what it is we really want, and the model’s inability to infer our intent from low-bandwidth text[2](https://www.latent.space#footnote-2).

This is an annoyance at the hobbyist level, but a severe risk at the business level.

- If you are making AI products based on “ - [hours/days/weeks](https://twitter.com/levelsio/status/1595809906661416961)” of prompt engineering, your IP is liable to go poof- [3](https://www.latent.space#footnote-3)when the next hot AI model comes out 3 months later.
- Worse still, your IP can be leaked through - [prompt injection](https://simonwillison.net/2022/Sep/12/prompt-injection/)(for now only a GPT concern, but- [SD2 is incrementally better at text rendering](https://twitter.com/minimaxir/status/1595986158751649793), and it’s not hard to imagine SD3 or hybrid models achieving full text rendering, which can leak prompt IP)
- or just embarrass you by - [exposing clumsy attempts](https://twitter.com/waxpancake/status/1549076996935675904)at engineering politically correct output

In the initial GPT-3 rush, Karpathy [anointed](https://twitter.com/karpathy/status/1273786314140160001) prompt engineering as “[Software 3.0](https://towardsdatascience.com/software-3-0-how-prompting-will-change-the-rules-of-the-game-a982fbfe1e0)”, but the recent vibe has shifted:


“Prompt programming is when telling them what you want is hard and relies on arcane conjurations like "trending on artstation | unreal engine | super high res".

Software 3.0 is when the obvious request just works.”

—[Gwern Branwen](https://twitter.com/gwern/status/1515801868970119169)

And:


“I don’t think we’ll still be doing prompt engineering in five years…

I just hope it’s not figuring out how to hack the prompt by adding one magic word to the end that changes everything else. What will matter is the quality of ideas and the understanding of what you want. So the artist will still do the best with image generation but not because they figured out to add this one magic word at the end of it. Because they were just able to articulate it with a creative eye that I don’t have.“

And:


“Prompt Engineering is like rearranging the deck chairs on the Titanic.

The sooner people can join[@ylecun](https://twitter.com/ylecun)and me in recognizing that true intelligence isn’t coming from #GPT-3 alone, the better.”

And a more evenhanded take:


“The act of continuously iterating on a prompt to have a model provide an objectively desired response isimplicitly acknowledging the model is failing.

As models become more generally intelligent, they will be capable of aligning with desired output without humans contorting our input.

…

And, fwiw, we’ve seen this before:Prompting is almost like a kind of hyperparameter tuning. The hyperparameter tuning that was once was required to get traditional ML to be useful with sklearn haslargely fallen by the wayside as the models themselves have gotten better.

The fact that adding keywords like [Let’s Think Step By Step](https://twitter.com/arankomatsuzaki/status/1529285884817707008), adding “Greg Rutkowski”, prompt weights, and even negative prompting are still so enormously effective, is a sign that we are nowhere close to perfecting the “language” part of “large language models”. To reiterate a theme from [the very first post](https://lspace.swyx.io/p/multiverse-not-metaverse) that kicked off this newsletter, prompts as a brittle arcane art of “spellcasting” is unsustainable.

Completely eliminating prompting is essentially solving a constrained subset of **the alignment problem**, which is ** AGI-Hard** - however, we may be able to hide prompting in clever ways:

- An underappreciated element of the success of GitHub Copilot ( - [podcast here](https://www.lennyspodcast.com/the-role-of-ai-in-new-product-development-ryan-j-salva-vp-of-product-at-github-copilot/)) is that product development took ~a few months to figure out the right form factor: zero-shot, in-IDE, context-aware autocomplete with no buttons to press for the default experience, and an explorable pane of alternatives on demand.
- Nathan Baschez’s - [Lex.page](https://twitter.com/nbashaw/status/1581673516360876032?lang=en)takes the similar approach for text - except that generations are triggered with a ++ keypress, but beyond that there is no separate prompt textbox.

My lesson from these two examples is that it might be possible to make prompting “invisible” by making it part of the UI, and finetuning output for as much of the writer’s context as possible to make it more useful. Latency matters, and cost matters, which are wonderful because these tend to be “regular engineering” type problems rather than AI problems.

## “Generative AI” is underselling the potential

Generative AI is certainly a buzzword that has led to some great memes:

![X avatar for @DeltyThe73rd](https://substackcdn.com/image/fetch/$s_!TnFC!,w_40,h_40,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack.com%2Fimg%2Favatars%2Fdefault-light.png)

![](https://substackcdn.com/image/fetch/$s_!6JU3!,w_520,h_520,c_fill,f_auto,q_auto:good,fl_progressive:steep,g_auto/https%3A%2F%2Fpbs.substack.com%2Fmedia%2FFfFK5bsVIAEEubT.jpg)

![](https://substackcdn.com/image/fetch/$s_!7ccz!,w_520,h_520,c_fill,f_auto,q_auto:good,fl_progressive:steep,g_auto/https%3A%2F%2Fpbs.substack.com%2Fmedia%2FFfFK5nnVEAA6Z-1.jpg)

![](https://substackcdn.com/image/fetch/$s_!n-Wx!,w_520,h_520,c_fill,f_auto,q_auto:good,fl_progressive:steep,g_auto/https%3A%2F%2Fpbs.substack.com%2Fmedia%2FFfFK5-qUAAEgF8V.jpg)

![X avatar for @jordihays](https://substackcdn.com/image/fetch/$s_!TnFC!,w_40,h_40,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack.com%2Fimg%2Favatars%2Fdefault-light.png)

But the funny thing is it *is *leading to some real revenue: the [whisper numbers](https://twitter.com/azternomic/status/1585502503713460224) for Jasper, which [recently announced](https://twitter.com/daverogenmoser/status/1582362508362280960?lang=en) their $1.5b Series A, stand at $80m ARR, with Midjourney at $50m ARR and Stability at $40m ARR.[4](https://www.latent.space#footnote-4)

Still, it can be a very heretical observation that the term “Generative AI” is not well loved by its primary beneficiaries.

![X avatar for @EMostaque](https://substackcdn.com/image/fetch/$s_!TnFC!,w_40,h_40,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack.com%2Fimg%2Favatars%2Fdefault-light.png)

This might disappoint the tech landscape chart making cottage industry ([Base10](https://twitter.com/letsenhance_io/status/1594826383305449491), [Sequoia](https://twitter.com/sonyatweetybird/status/1582040028015837187), [a16z](https://a16z.com/2022/11/17/the-generative-ai-revolution-in-games/#section--6)) - while generative AI has had a banner year, the business world has far more usecases for decreasing entropy than increasing it[5](https://www.latent.space#footnote-5). The world has had enough of the “[haha! everything you just read was written by AI! isn’t that cute! gotcha!](https://twitter.com/aliabdaal/status/1583203039967850497)” bait and switch and we already have a deep distrust of real images from official government and media sources without any need for increased suspicion due to AI fakery.

The most prominent case of the “Generative AI” backlash coincidentally also happened this past week, with Meta’s Galactica model released [to much hype](https://twitter.com/paperswithcode/status/1592546933679476736) and then taken down in 3 days:

One could argue that it was simply too ambitiously productized and marketed; [Metaphor Search](https://metaphor.systems), which was [launched just the prior week](https://twitter.com/metaphorsystems/status/1590766127034298370), experienced no such blowback because it limited itself to predicting links rather then generating answers. We do not have space for an in-depth discussion on the facts and ethics of Galactica, but further interesting debates are on [HN1](https://news.ycombinator.com/item?id=33611265), [HN2](https://news.ycombinator.com/item?id=33719763), and [Twitter](https://twitter.com/osanseviero/status/1594420137171423232).

The fact that **Language Models Hallucinate** is fun for those new to them, but tiring and a basically permanent fact of life for people working with generative models, requiring very kludgy and expensive [cascades of models and a “Judge” model of models for error correction](https://twitter.com/karpathy/status/1577349418503716864). Solving hallucination (and adding physics, theory of mind, conceptual composition, etc) is again [AGI-hard](https://lspace.swyx.io/p/agi-hard) and therefore uninteresting to the pragmatist.

As Generative AI crests the Gartner Cycle peak and falls due to already obvious flaws, it may be worth paying attention to the builders who are focusing on other ways of productizing language models: [Agentic AI](https://twitter.com/realbrendanb/status/1593414620928413696) and [RLHF](https://twitter.com/carperai/status/1582891780931874819).

## CTAs

Liked this post? Help share it on Twitter (for now…)

![X avatar for @swyx](https://substackcdn.com/image/fetch/$s_!TnFC!,w_40,h_40,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack.com%2Fimg%2Favatars%2Fdefault-light.png)

![](https://substackcdn.com/image/fetch/$s_!gM3F!,w_64,h_64,c_fill,f_auto,q_auto:good,fl_progressive:steep,g_auto/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F681286aa-fe56-42a5-8031-71308e99c829_952x815.png)

[1](https://www.latent.space#footnote-anchor-1)

Leading to a [predictable reactionary movement](https://www.reddit.com/r/StableDiffusion/comments/z420nf/unstable_diffusion_is_going_to_do_what/), with one flaw - Stability is likely the out-of-bounds marker for what is venture backable in generative AI.

[2](https://www.latent.space#footnote-anchor-2)

One of my most fun AI experiences recently was attending a [Prompt Battle](https://twitter.com/rachel_l_woods/status/1587839500473946112) at the first OpenAI hackathon in SF, and [the MC](https://twitter.com/josephofiowa) laughing at all our obviously-Stable-Diffusion-flavored prompts, reminding us “hey, word order doesn’t matter in Dall-E!”. We had all unknowingly internalized principles of prompt engineering skewed by our own experience.

[3](https://www.latent.space#footnote-anchor-3)

It’s overly alarmist to say that **all** the IP gets invalidated in the next model, and to some extent this is what being early in **any** new tech looks like; you have to take dumb risks and do things that don’t scale in order to have the length and breadth of experience you need to know things others don’t and build something lasting. By the time the AI product playbook is obvious, it may be too late to start positioning for it — because of the hundreds of founders already searching the latent AI product space without requiring any long term game plan before they begin.

[4](https://www.latent.space#footnote-anchor-4)

I don’t believe the Copilot number of $100m ARR, since GitHub itself [only recently passed $1b ARR](https://techcrunch.com/2022/10/25/microsoft-says-github-now-has-a-1b-arr-90m-active-users/), but you could do a Fermi estimate with some public numbers - [hundreds of thousands of users](https://www.fastcompany.com/90811225/githubs-code-writing-tool-copilot-helps-keep-developers-in-the-zone#:~:text=GitHub%20launched%20a%20technical%20preview,thousands%E2%80%9D%20use%20it%20every%20day.), 50% paying, $100/year/user, works out to at least $10m/year.

[5](https://www.latent.space#footnote-anchor-5)

Acknowledged that “Generative AI” does not directly equate to “increasing entropy” - there are great ways to use “generative AI” to summarize and extract. Arguably diffusion models simply “make entropy useful” by reducing it with CLIP guidance - which isn’t everything, but also isn’t nothing.

Great article!

Great article! But to what extend is it not possible to make the argument in reverse? The fact that LLMs suck at language (as you illustrate with the arcane prompting), but can still create valuable results in the right context, could also point to immense potential value for each small improvement in language ability right? MJv4 didn't have a fundamental improvement in language ability, just fine tuning on user results. But it still lead to a significantly better model.
