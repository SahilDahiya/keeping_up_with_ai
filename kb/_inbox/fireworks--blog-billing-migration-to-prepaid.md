---
title: Fireworks AI
kind: blog
topic: null
subtopic: null
secondary_topics: []
summary: null
triage: null
skip_reason: null
source: fireworks
url: https://fireworks.ai/blog/billing-migration-to-prepaid
author: null
published: '2026-06-15'
fetched: '2026-08-12T06:29:15Z'
classifier: null
taxonomy_rev: 2
words: 544
content_sha256: 75dc37fc7e896d4b1da0b1a0fa55dc87edfa7b36ccba0430b54559bedb424999
---

# Fireworks AI

Starting **July 1st, 2026**, Fireworks is moving all self-serve accounts to **prepaid billing**. Instead of accruing usage and getting invoiced after the fact, your account will draw down from a credit balance as you use the platform.

`💡If you’re a` **contracted customer**, your account will not be affected.

Under prepaid billing, you purchase credits up front, and your usage is deducted from that balance as you go. The upside of prepaid is predictability: you know what you've committed up front, and you decide how and when credits get added. A few things to know:

- •**Credits are used for all usage.** Serverless, on-demand deployments, and training all deduct from your credit balance.
- •**Auto reload keeps your credit balance full automatically.** When your balance drops to a minimum you choose, we purchase more credits using your payment method on file.
- •**If your balance reaches $0 and auto reload is off, usage pauses** until you add more credits. Your services resume as soon as you have a positive balance again.

`💡For production workloads we` **highly recommend** setting up auto reload to ensure you don’t have service interruptions.
You can configure your prepaid account and switch over right now, before the deadline. Changes take effect immediately, you control the timing, and you won't have anything to worry about on July 1st.

If you don't switch beforehand, we'll handle the transition for you. On **July 1st** we will:

1. **Invoice you for your June usage** under your current postpaid terms, and
2. **Migrate your account to prepaid** automatically.

`💡`__Please note:__ If you haven't added credits and turned on auto reload before July 1st, your account can land at a $0 balance — which means **your services may be disrupted** until you add credits.

1. Log into [Fireworks](https://app.fireworks.ai/account/home) today, you’ll see a banner prompting you to move your account to pre-paid.
2. **Add credits.** Review your current balance and add a starting amount if you'd like a cushion. (You can also do this with $0 added and rely on auto reload.)
3. **Turn on auto reload.** Choose a minimum balance and your preferred top-up amount. For example, add**$10** automatically whenever your balance drops below**$5** . This is the single best way to avoid any service disruption.
4. **Confirm your payment method.** Make sure the card on file is correct so top-ups go through without a hitch.
5. **Switch to prepaid.** Your account converts immediately.

There may be a brief delay while our systems reflect a new balance, so it's worth setting this up ahead of time rather than at the moment you run low.

For all additional details about the credits and billing system, please visit the docs page below:

Once your balance is exhausted and auto reload isn't enabled, API requests will stop succeeding until you top up. You can add credits at any time from the billing dashboard to resume usage right away. Turning on auto reload avoids this entirely.

No. If you're a contracted customer, this change doesn't affect you, and your billing continues under your existing agreement. You should not be prompted to “Pay and switch today”.

If you are a contracted customer, you should not see this banner. Please reach out to us at [**billing@fireworks.ai**](mailto:billing@fireworks.ai) and we'll help you get set up.
