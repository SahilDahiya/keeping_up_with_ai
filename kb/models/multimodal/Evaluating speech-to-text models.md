---
title: Evaluating speech-to-text models
topic: models
subtopic: multimodal
secondary_topics:
- evals-observability/evaluation
summary: Evaluates speech-to-text models for voice AI workflows, covering datasets,
  scoring, and tradeoffs in transcription quality.
source: braintrust
url: https://www.braintrust.dev/blog/voice-evals-stt
author: Braintrust Team
published: '2026-07-09'
fetched: '2026-07-11T04:34:16Z'
classifier: codex
taxonomy_rev: 1
words: 3966
content_sha256: ce18dc87747e628cfbc0abf2f72dea25cafa0734738e46733cc92e8ef6aae0d9
---

# Evaluating speech-to-text models

9 July 2026Jess Wang21 min

If you're building a voice agent, picking the right speech-to-text model is not obvious. Every provider claims to be accurate, fast, and production-ready, and the benchmarks they publish rarely look anything like your actual traffic. The only way to know is to run your own eval on audio that resembles what your users will say.

I ran a controlled eval in Braintrust across six STT providers, 240 audio cases, and eight content domains, scoring not only whether each model heard the words but whether its mistakes changed the downstream answer. This blog walks through how to set up a voice eval, what to measure, the tradeoffs that decide the winner, and which models came out on top.

In a common voice agent pipeline, audio comes in -> an STT model turns it into text -> an LLM reasons over that text -> a reply goes out. In this pipeline, two things matter:

- Did STT hear the words right?
- If there is a transcription error, how much does it affect the final response?

To measure the second question, I ran the same LLM prompt twice per case. Once on the reference transcript (the known-correct text, which acts as my answer key) and once on the STT output. Then I checked whether the two answers mean the same thing using an LLM-as-a-judge scoring system.

I collected 240 audio files total to test against each STT model. Those audio files were spread across eight content buckets, with 30 cases each.

| Bucket | Source | How the reference transcript was made |
|---|---|---|
| customer_support | [ElevenLabs](https://elevenlabs.io) | I wrote the scripts as text and used TTS to turn them into audio files |
| philosophy | [LibriSpeech](https://huggingface.co/datasets/openslr/librispeech_asr) | LibriVox volunteers reading public-domain books |
| geography / legal / science | [FLEURS](https://huggingface.co/datasets/google/fleurs) | Speakers reading FLORES (translated Wikipedia) sentences |
| finance | [earnings22 (Rev.com)](https://huggingface.co/datasets/distil-whisper/earnings22) | Human-transcribed real earnings calls |
| medical | [Hani89 medical ASR](https://huggingface.co/datasets/Hani89/medical_asr_recording_dataset) | Crowd recordings of symptom prompts |
| atc | [ATCO2](https://huggingface.co/datasets/jlvdoorn/atco2-asr) | Semi-automatic (ASR plus partial human correction) |

The seven Hugging Face buckets were pulled through the dataset viewer REST API instead of the datasets library, which sidesteps torchcodec and the gated-dataset walls (SPGISpeech, SLUE, and GigaSpeech all return 401). It paginates 100 rows per request, and ffmpeg normalizes every clip to 16 kHz mono before scoring.

python

```
u = (f"https://datasets-server.huggingface.co/rows?dataset={quote(ds)}"
     f"&config={quote(cfg)}&split={quote(split)}&offset={len(out)}&length={n}")
```
The customer_support clips were read in British, American, and Australian accents. I used ElevenLabs text-to-speech to create the audio clips. I wanted to see if the STT models would handle different accents well.

Here are the six models I compared:

| Model | Why it's here |
|---|---|
| OpenAI gpt-4o-transcribe | The new default a lot of teams reach for |
| Groq whisper-large-v3 | Open Whisper weights on fast hardware |
| ElevenLabs scribe_v1 | Strong on the voice-agent side |
| Deepgram nova-3 | Popular real-time API |
| AssemblyAI universal-2 | Popular async API |
| Google chirp_2 | The big-cloud incumbent |

Every case carries a `critical_entities` list. These are the specific tokens that are more important to transcribe correctly for the final answer to be relevant. For example, dropping a comma isn't too bad. But if you drop the last digit of an order number, the whole response breaks.

For customer_support I wrote these critical entities by hand because I know which IDs and actions each script contains:

- `A100`,- `cust_123`,- `INV-4492`,- `SN-90455-K`(order numbers, customer IDs, invoice and serial codes)
- `charged twice`,- `cancel`,- `subscription`,- `refund`(the actions that decide what the agent does)

For the seven remaining buckets there's no human curating those lists, so I auto-extract them with a small heuristic. It scores every token by how "hard" it is and keeps the top four:

python

```
def critical_entities(text):
    scored = []
    for i, t in enumerate(tokens(text)):
        if len(t) < 2 or t.lower() in STOP:
            continue
        s = 0
        if any(c.isdigit() for c in t):          s += 3   # digits
        if len(t) >= 10:                          s += 2   # long words
        elif len(t) >= 8:                         s += 1
        if has_lower and i > 0 and t[0].isupper(): s += 2  # proper nouns
        if s > 0:
            scored.append((s, t))
    scored.sort(key=lambda x: -x[0])
    return dedupe(scored)[:4]
```
Digits score highest, then long words, then mid-length words and proper nouns. On a geography clip, the script surfaces things like `Reykjavik`, `Iceland`, and `Q12`. On a finance clip it pulls `Q4`, `2020`, and `SMB`. On a philosophy passage it grabs the long words, `PARAPHERNALIA`, `EXTINGUISHED`, and `MISFORTUNE`.

I had four scorers in place:

- `transcription_similarity_score`is lexical (word-level) similarity between the reference and the STT output. Edit-distance ratio over normalized tokens. It is deliberately NOT semantic. I want "70" and "seventy" to count as a miss.
- `critical_entity_recall_score`is how many of the hard tokens survived.
- `answer_equivalence_score`is the LLM-as-a-judge on whether the answer from the STT transcript means the same as the answer from the reference answer key (the one I generate by running the LLM on the known-correct reference transcript). Same, partial, and different map to 1, 0.5, and 0.
- `stt_latency_ms`is per-call STT speed.

I chose lexical scoring because it catches the formatting errors that tend to break automation. If a customer says their account is `160` and STT writes "one sixty," this could cause account lookup failures or 400s in API calls.

The critical_entity_recall_score normalizes lightly before matching (lowercase, collapse punctuation to spaces) so casing and stray punctuation don't create fake misses. Then it counts the fraction of required entities present in the transcript:

typescript

```
const observed = normalizePhrase(output.transcript);
const found = entities.filter((e) => observed.includes(normalizePhrase(e)));
return {
  name: "critical_entity_recall_score",
  score: round(found.length / entities.length),
  metadata: { required: entities, found, missing },
};
```
Two of the three scorers are deterministic, so they do what they say by construction. The one worth checking is the LLM-as-judge (answer_equivalence), because a judge can quietly drift. If it's sound, its verdicts should line up with the deterministic scorers. Cases it calls "same" should have high transcription similarity and entity recall, and cases it calls "different" should have low ones. Pooling all 1,439 baseline cases, that is what happens.

| Judge verdict | Cases | Mean similarity | Mean entity recall |
|---|---|---|---|
| different | 178 | 0.431 | 0.429 |
| partial | 434 | 0.836 | 0.804 |
| same | 827 | 0.918 | 0.890 |

The ordering is strictly monotonic, and the full breakdown is a clean diagonal. High-similarity cases concentrate in "same" (610 of 836 at similarity >= 0.9, with only 6 judged "different"), and low-similarity cases in "different." The rank correlation between the judge and the deterministic scorers is positive and overwhelmingly significant (Spearman 0.47 for similarity, 0.39 for entity recall, both p well below 0.001). The off-diagonal cases (high similarity but "partial") are the ones worth understanding. Say the reference is "refund for order INV-4492 approved" and STT gives "refund for order INV-4493 approved." Word-for-word that is about 95% similar, so the string scorer reads high, but the one token that changed is the critical ID, and it breaks the actual answer, so the judge correctly calls it partial. Those are the cases where "did it sound almost identical?" and "did it mean the same?" come apart, which is the whole failure this post is about. It is reassuring they land off the diagonal instead of getting waved through as "same," and it means the judge is measuring the same underlying signal as the deterministic scorers without being fooled when a single wrong token flips the meaning.

Each model ran as its own Braintrust experiment against the identical 240 cases. Here are the results:

| Model | Transcription similarity | Critical entity recall | Answer equiv | Latency |
|---|---|---|---|---|
| OpenAI gpt-4o-transcribe | 0.835 | 0.820 | 0.760 | 1360ms |
| ElevenLabs scribe_v1 | 0.834 | 0.826 | 0.729 | 1462ms |
| Groq whisper-large-v3 | 0.839 | 0.816 | 0.738 | 4324ms |
| AssemblyAI universal-2 | 0.830 | 0.810 | 0.717 | 3347ms |
| Deepgram nova-3 | 0.828 | 0.787 | 0.711 | 1531ms |
| Google chirp_2 | 0.833 | 0.783 | 0.696 | 1460ms |

The accuracy columns are a near-tie, and it is a real tie, not merely close averages. Per-case scores vary a lot (standard deviation ~0.25 to 0.36), and every model's 95% confidence interval overlaps every other's on all three metrics, so no baseline accuracy difference is statistically distinguishable. There is a faint ordering (Google lands lowest on entity recall and answer equivalence) but the intervals still overlap.

Latency shows a wider spread. But Groq and AssemblyAI weren't slow at transcribing, they were slow for other reasons:

| Model | Reported latency | Trust the number? | Why |
|---|---|---|---|
| OpenAI gpt-4o-transcribe | 1360ms | Yes | real-time call |
| Google chirp_2 | 1460ms | Yes | real-time call |
| ElevenLabs scribe_v1 | 1462ms | Yes | real-time call |
| Deepgram nova-3 | 1531ms | Yes | real-time call |
| AssemblyAI universal-2 | 3347ms | No | async upload plus poll overhead |
| Groq whisper-large-v3 | 4324ms | No | free-tier 429 rate-limit backoff |

Groq is normally one of the fastest STT services around. Its number here is inflated by free-tier rate-limit backoff, not the model. AssemblyAI's is inflated by its upload-then-poll flow. Only the four models near 1.4 seconds are comparable on speed. Among those, OpenAI gpt-4o-transcribe gives you the best accuracy at the lowest real-time latency, which makes it the best overall balance.

Here's critical-entity recall broken out by bucket and model. The number represents the fraction of the hard tokens that survived transcription.

| Bucket | groq | openai | 11labs | asmbly | deepgrm | |
|---|---|---|---|---|---|---|
| atc | 0.39 | 0.42 | 0.46 | 0.35 | 0.43 | 0.28 |
| customer_support | 0.69 | 0.66 | 0.68 | 0.64 | 0.59 | 0.66 |
| medical | 0.87 | 0.88 | 0.87 | 0.90 | 0.88 | 0.85 |
| finance | 0.95 | 0.88 | 0.82 | 0.95 | 0.89 | 0.92 |
| geography | 0.91 | 0.90 | 0.93 | 0.90 | 0.88 | 0.86 |
| legal | 0.88 | 0.91 | 0.91 | 0.87 | 0.85 | 0.88 |
| science | 0.87 | 0.93 | 0.97 | 0.89 | 0.80 | 0.84 |
| philosophy | 0.97 | 0.97 | 0.97 | 0.97 | 0.96 | 0.97 |

Philosophy contains a lot of dense old-book vocabulary, words like `PARAPHERNALIA`, `EXTINGUISHED`, and `MISFORTUNE`, and every model sits at ~0.97 for that bucket. This shows that STT is great at words even when they are hard. But the models all struggle with ATC, which is nothing but callsigns (`KLM Seven Three Whiskey`), the NATO phonetic alphabet (`Oscar Kilo Tango Uniform`), and digit-by-digit numbers ("one six zero").

The customer_support scripts were read in British, American, and Australian voices, and every model handled them about the same. Here are the scores averaged across all six models:

| Accent | Cases | Similarity | Entity recall |
|---|---|---|---|
| British | 12 | 0.908 | 0.662 |
| American | 12 | 0.895 | 0.648 |
| Australian | 6 | 0.908 | 0.653 |

That's a 1.3-point spread on similarity and 1.4 on recall. It seems like these models don't struggle too much on different accents.

When digging into the errors, they look the same across every provider. `cust_fail` becomes "cust12," `Slalom` becomes "Shell Oil," `BR2207` loses its hyphen.

In an attempt to boost these scores, I tried handing the model some missing context.

Every major STT API takes some kind of vocabulary hint. I built one glossary per bucket from external, standard vocabulary and fed it into each provider's native slot.

Two rules kept it honest. First, every glossary is built from external, standard domain vocabulary, never from the clips' own reference transcripts. I'm giving the model the domain's general vocab, not the specific answer. Second, for customer_support that means made-up example IDs (`cust_907`, `INV-3310`) that show the format without leaking a single real value. The sourcing is deliberately boring, drawing on the ICAO/NATO phonetic alphabet and standard phraseology (ICAO Annex 10 and Doc 9432) for ATC, RxNorm/SNOMED-style symptom and drug terms for medical, and common financial jargon plus well-known company names for finance.

For example, the ATC glossary is published aviation standards:

```
# ICAO/NATO phonetic alphabet
Alpha Bravo Charlie Delta Echo Foxtrot Golf Hotel India Juliett Kilo ...
# Spoken-number conventions
niner tree fife decimal zero
# Common ICAO airline telephony callsigns
Speedbird Lufthansa KLM Jetstar Ryanair Swiss Emirates Qantas
```
With the extra domain vocabulary fed in as context, the results split the providers cleanly into two camps:

| Model | Similarity v1 -> v2 | Entity recall v1 -> v2 |
|---|---|---|
| openai gpt-4o-transcribe | 83.5 -> 86.2 | 82.0 -> 85.0 |
| groq whisper-large-v3 | 83.9 -> 85.8 | 81.6 -> 82.1 |
| google chirp_2 | 83.3 -> 83.1 | 78.3 -> 81.2 |
| deepgram nova-3 | 82.8 -> 84.2 | 78.7 -> 78.9 |
| elevenlabs scribe_v1 | 83.4 -> 83.7 | 82.6 -> 82.3 |
| assemblyai universal-2 | 83.0 -> 82.9 | 81.0 -> 81.0 |

When you check these lifts against paired confidence intervals, the honest picture is narrower than the point estimates. On overall entity recall, only two models show a statistically significant gain from biasing: OpenAI (+0.030, 95% CI [0.003, 0.056], p=0.028) and Google (+0.030, p=0.0008), both prose-hint models. The keyword-only providers and ElevenLabs are flat and not significant.

The gains that do exist concentrate in the standardized buckets, the ones whose hard tokens follow a describable format or a finite standard vocabulary, like customer-support IDs (`cust_###`) and ATC callsigns. But the headline customer-support gain, OpenAI +0.11, is a real observed jump that does not reach significance at n=30 (95% CI [−0.02, +0.24], p=0.10). Thirty cases per bucket is too few to call it. Biasing is directionally promising for IDs; post-correction, below, is the fix that clears the bar. And the open-ended buckets (geography, legal, science, philosophy) stayed flat throughout, because no short general glossary covers arbitrary Wikipedia content.

The wide error bars show that biasing is a small lever measured on limited data. Only OpenAI's and Google's intervals clear zero, and even those only barely. Pinning the effect down would take more than 30 cases per bucket, not a bigger model.

Why did some models gain and others not budge? It comes down to what kind of hint the API accepts.

| Provider | Biasing input | Kind |
|---|---|---|
| OpenAI / Groq | `prompt` | free prose (sentences, rules, examples) |
| Deepgram / AssemblyAI / Google | `keyterm`/`word_boost`/ phrase-set | literal terms (exact strings to boost) |
| ElevenLabs | none | no biasing slot |

I call the first camp rich biasing. The `prompt` field on Whisper-family models takes free-form prose, so you can teach it a rule like "customer IDs look like `cust_` followed by a word, for example cust_907." The model learns the pattern and applies it to IDs it has never seen, including `cust_fail`.

The second camp only takes literal, exact strings. A keyword booster is basically a spell-check dictionary. If your list has `cust_907` but the audio says `cust_fail`, it does nothing, because `cust_fail` is a different string you never wrote down.

So did it move the customer_support scores? A little, and only for the prose models, and here's why. You don't know the specific ID ahead of time. You can't list `cust_fail`, because that IS the answer. But you do know your format, `cust_###`. Prose models use the thing you know (the format) and nudged the IDs. Keyword models can only use the thing you don't know (the exact string), so they had nothing to grab, and they stayed flat.

Biasing isn't always helpful, though. On mismatched cells it can actively degrade a word the base model already got right, which is how medical entity recall slipped about 0.05 for OpenAI and ElevenLabs. Groq transcribed "Tylenol" correctly at baseline, then the medical glossary collapsed it into the phonetic non-word "tilino" (recall 1.00 to 0.50). OpenAI had "weightlifting" as one token matching the reference, then biasing split it into "weight lifting" and broke the exact-match (again 1.00 to 0.50). In both cases the model heard the word fine. The extra conditioning knocked it off the literal string the scorer was looking for.

There's a fix that works for all of them. Run an LLM over the finished transcript and let it apply the format rule as a proofreading pass. This way, there is no special API parameter needed, so it works on any provider's output.

The catch when I first ran this is that an unconstrained LLM over-corrects. Early versions hallucinated `A100` into `ORD-100` and rewrote "seven three whiskey" into "73W." The correction prompt needs hard rules that let it fix separators and casing but forbid inventing or converting characters:

```
HARD RULE for identifiers/codes: the corrected token MUST contain EXACTLY
the same letters and digits, in the same order, as the original. You may
ONLY add/remove separators (space, hyphen, underscore) and change casing.
(So 'A 100' may become 'A100' but NEVER 'ORD-100'; 'cust 123' -> 'cust_123';
'BR2207' -> 'BR-2207'.) NEVER convert between spelled-out and numeric forms:
keep 'one six zero' as those words, keep '160' as '160'. If unsure, leave unchanged.
```
Here's customer-support entity recall across all three approaches, baseline (v1), glossary biasing (v2), and post-correction (v3):

| Model | v1 baseline | v2 biasing | v3 post-correction |
|---|---|---|---|
| openai gpt-4o-transcribe | 0.661 | 0.772 | 0.789 |
| groq whisper-large-v3 | 0.694 | 0.728 | 0.744 |
| elevenlabs scribe_v1 | 0.678 | 0.678 | 0.794 |
| deepgram nova-3 | 0.589 | 0.622 | 0.722 |
| assemblyai universal-2 | 0.644 | 0.644 | 0.789 |
| google chirp_2 | 0.661 | 0.678 | 0.756 |

Post-correction is the best column in every single row, and this time the wins hold up statistically. The lift over baseline is significant for OpenAI (+0.128, p=0.03), Deepgram (+0.133, p=0.03), and AssemblyAI (+0.144, p=0.03), with ElevenLabs the borderline case (+0.117, p=0.07). Every model improves and none regress. The two models where biasing did nothing (ElevenLabs and AssemblyAI, where v2 recall equalled v1) get the biggest jumps of the whole table, up to ~0.79. Post-correction runs on the transcript text, so it doesn't care which provider produced it, and the models biasing left behind catch right up.

On customer-support entity recall it's the best of the three approaches for every model, and it rescues the exact providers biasing couldn't help. AssemblyAI and ElevenLabs, both flat under biasing, both climb to ~0.79.

One case shows why answer-level scoring works. On an ATC clip with OpenAI, "just past 7:46", which was incorrect, became "Jetstar 746 established", which was the correct transcription.

Some observations around this eval while digging through the logs:

- The lexical scorer punishes digit-vs-word formatting. "one six zero" counts as a miss against "160," so buckets where numbers get read digit-by-digit (ATC most of all) look worse than the models are. I kept the scorer literal on purpose, because that's the correct behavior for IDs and codes. But I went back and measured what percentage of failures were caused by this semantic strictness. About 19% of ATC's entity-recall misses are pure digit-vs-word formatting, not the model mishearing. Normalize that away and ATC recall climbs from ~39% to ~51%, an 11-point jump. Finance is in the same ballpark (26% of its misses are formatting) and medical less so (15%). So ATC models are meaningfully better than the raw numbers suggest.
- Whisper hallucinates on bad audio. Groq's whisper-large-v3 auto-detects language and, on garbled or quiet clips, sometimes transcribes into French, Czech, or German (9 of 240 clips in the baseline). I chose not to pin `language=en`because the language type is not always guaranteed.
- Sometimes the reference transcription or audio was wrong. Read-aloud datasets use the intended script as the reference, so if a speaker misreads, a correct STT output scores as wrong. That deflates the absolute scores and compresses the gaps between models.

A few practical things made this eval tractable to run and read, and they all lean on Braintrust features.

Braintrust's `Eval()` takes a `maxConcurrency` option to throttle concurrency, and it matters more than it sounds. Running all 240 cases unthrottled set off an ECONNRESET storm that errored 197 of 240. Capping it fixed that outright, and Groq's free tier needs an even tighter limit plus 429 backoff.

typescript

```
maxConcurrency: process.env.EVAL_CONCURRENCY ? Number(process.env.EVAL_CONCURRENCY) : 6,
```
Braintrust has an `Attachment` type that makes the audio playable in the trace. Log it on a span and the clip shows up as a playable widget right in the trace, next to the transcript and the scores. This is the thing that made the human-review and reference-culling workflow possible, because a low score was one click from being audible.

typescript

```
const attachment = new Attachment({ filename, contentType: "audio/wav", data: absolutePath });
span.log({ input: { customer_audio: attachment } });
```
The traces caught the latency red herrings. The per-call `stt_latency_ms` metric is what told me Groq and AssemblyAI's slow numbers were rate-limit backoff and upload overhead, not the model. Without per-call timing in the trace I'd have ranked two fast providers as slow.

- Structured tokens are the failure mode. Ordinary words, even fancy ones, transcribe fine. Philosophy read aloud from old books scored ~0.97 entity recall across every model. Numbers, codes, IDs, callsigns, and proper nouns are much harder.
- Accent variation barely moved the scores. British, American, and Australian audio all transcribed the same.
- The major models are basically tied on accuracy. Five of six landed within about a point of word-level similarity.
- Speed is the real differentiator. With accuracy so close, latency breaks the tie, and OpenAI gpt-4o-transcribe pairs the top answer quality with the lowest real-time latency.
- The cheap wins are biasing and post-correction. Feed the model your domain vocabulary and structured-token recall goes up, if the model takes prose hints. Run an LLM proofreading pass over the transcript and it goes up for every provider, even the ones biasing can't touch.
- What's different for voice is that you have to listen. Deciding whether a low score is a real miss or a bad reference means playing the clip, so audio attached to each trace is how the review happens, not a nice-to-have.

No single model wins everything, so match the model to what you care about. OpenAI gpt-4o-transcribe is the best all-around pick, with the top answer-equivalence score at the lowest real-time latency. But ElevenLabs scribe_v1 has the highest critical-entity recall, and Groq whisper-large-v3 edges the field on raw transcription similarity when it isn't rate-limited. Google chirp_2 is the one to skip, trailing the field on entity recall and answer equivalence. So if your priority is preserving the meaning of the answer with low latency, start with OpenAI; if it's squeezing out every last ID and proper noun, ElevenLabs is worth a look.

Raw accuracy is comparable across the top models, so spend your real effort on giving the model the right context. If your STT provider accepts a prose prompt, hand it your formats. If it doesn't, add an LLM post-correction pass.

You can set up a voice eval like this one, attach each clip to its trace, and score both whether the words matched and whether the answer changed. [Sign up for free](https://www.braintrust.dev/signup) to run it on your own traffic, or [book a demo](https://www.braintrust.dev/contact) to walk through your pipeline.
