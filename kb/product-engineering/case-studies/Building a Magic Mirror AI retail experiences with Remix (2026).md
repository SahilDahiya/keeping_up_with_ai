---
title: 'Building a Magic Mirror: AI retail experiences with Remix (2026)'
kind: blog
topic: product-engineering
subtopic: case-studies
secondary_topics:
- models/multimodal
summary: Shopify builds an in-store 'Magic Mirror' AI retail experience with Remix,
  using multimodal AI to turn physical shopping into an interactive experience for
  hype-driven brands.
triage: null
skip_reason: null
source: shopify
url: https://shopify.engineering/magic-mirror
author: Nikola Draca
published: '2026-03-19'
fetched: '2026-07-15T00:53:23Z'
classifier: claude
taxonomy_rev: 2
words: 1823
content_sha256: dfca86a27a49cc9718a3c6e912fcb736df0f5c27d0e2cde3164b25b05b2bf5f5
---

# Building a Magic Mirror: AI retail experiences with Remix (2026)

As online shopping has become frictionless, the value of physical retail has shifted. Increasingly, the brands that generate the most hype (and sales) are the ones that turn in-store shopping into an experience.

In a world where almost anything can be delivered to your door, showing up in person has become a kind of signal. The best brands are leaning into that shift by creating moments that feel interactive, surprising, and personalized.

One format we’ve been experimenting with at Shopify is something we call a “magic mirror.” It's an AI-powered mirror that you can customize to reflect personalized messages to your customers.

A magic mirror looks ordinary, but behind the glass sits a display and a hidden camera that allows it to see and respond to the person standing in front of it. Powered by AI, the mirror can recognize visual signals (what someone is wearing, how they move, etc.) and respond with custom messages and animations. It can also interact with other systems or peripherals to do things like generate a discount code or print a receipt. Mirror interactions take less than one minute per guest, which makes it scalable for even the busiest retail stores.

![Rare Beauty Magic Mirror activation](https://cdn.shopify.com/s/files/1/0779/4361/files/rare_mirror_result.gif?v=1773765650)

Our first version of this concept focused on one specific use case: makeup shade matching for Rare Beauty. Guests could press a button to find out their perfect shade of blush and enter their email to have that metadata synced to their customer profile. But shade matching is just one potential ‘mode.’ Magic mirrors can generate all kinds of custom responses:

- deliver heartfelt compliments (or hilarious roasts)
- suggest complementary product(s)
- analyze someone’s style
- recognize gestures
- suggest and score specific actions (eg. “Simon Says”)
- unlock access to exclusive products
- generate unique discount codes

You can combine these functionalities to host playful challenges on a mirror. For example, you could make a mirror where customers can “pay with a pose” — the more accurately they can perform a yoga pose, the higher the discount they can earn to spend in store (generated via our Admin API.).

Curious about how to build one?

## Bill of Materials

Here’s what you’ll need:

- 
[Full-sized mirror](https://fotomaster.com/products/mirror-air-booth)(there are smaller makeup mirrors like[this](https://www.soulacatv.com/collections/makeup-tvs)as well)
- Webcam (placed behind the display)
- 
[Webcam mount](https://www.bhphotovideo.com/c/product/1724359-REG/camvate_c2875_1_4_20_screw_connector_ball.html)(for rotating camera)
- Computer (to run the Remix server + browser)
- Physical button or keyboard (for triggering experience)

## How does it work?

Let’s use the example of a makeup shade matching mirror:

- Mount the mirror in a physical retail space, with a webcam embedded in or behind the display.
- A customer walks up to the mirror and presses a button to trigger a response.
- The screen counts down, takes their photo, and runs it through a vision model with a curated prompt.
- The mirror returns a personalized compliment and a blush shade recommendation matched to their appearance.

The response stays on the screen for 10 seconds so the customer can take a selfie, followed by a 5-second countdown that auto-advances back to the idle state, ready for the next customer.

The core experience runs entirely on standard HTTP—a customer presses the button, the browser POSTs to the server, and the response renders.

## The big picture

At a high level, the flow is:

If you want to skip ahead, we wrote a small example of the entire implementation [here](https://gist.github.com/nikodraca/e898db888a1bd09ba3a1adf137dde6a0). This is a barebones example to get you started; it doesn’t cover persisting data, authentication, etc.—just a single Remix route.

## Architecture

The server and client are co-located in a Remix route file. Remix handles the boundary between them: the server `action` runs on a POST, and its return value flows to the browser component via `useActionData`.

## Framework: Remix

[Remix](https://remix.run/) is a full-stack React framework where each route file can export a `loader` (server, GET), an `action` (server, POST), and a default export (React component, browser). This lets us keep the server logic and client logic in the same file without a separate API layer.

The production mirror splits responsibilities across a few files:

The route file itself is thin—it defines the config, sets up auth, and re-exports the shared action and loader. All the interesting logic lives in the component and utilities. Placing auth on a parent route propagates it to every nested route beneath it automatically.

## The server action

The action does two things: it calls the LLM, and it broadcasts status over SSE (more on this below). The broadcast happens twice—once at the start to signal that processing has begun, and once on completion with the result. This lets a remote device know the mirror is working without needing to poll or watch the screen.

### Building the prompt

`processImageWithLLM` calls `buildPrompt` before making the API call. The prompt is assembled from three parts:

- 
**Base prompt string**defining the model's persona, tone constraints, and task
- 
**Product recommendation table**, appended as plain text:`Product ID | Product Name | When to Recommend | Inventory`
- 
**JSON output schema instruction**telling the model exactly what shape to return

Inventory was considered by the LLM when making decisions to try to balance existing stock and avoid overfitting.

Sending the product catalog as a plain-text table (rather than structured JSON) is a deliberate choice. LLMs parse tabular natural language well, and it keeps the prompt readable by humans—important when brand teams need to review or adjust recommendations.

The output schema instruction (`promptFormattingInstructions`) tells the model to return exactly:

### The LLM call

We use the OpenAI SDK here, but because the client is pointed at an internal proxy via `baseURL`, the underlying model provider can be swapped without changing this code.

A few decisions worth explaining:

- 
`response_format: { type: "json_object" }`
- 
**Vision input:**the model accepts both a text prompt and an image in the same message. The image is passed as a data URL directly—no file upload or CDN step needed.
- 
`max_tokens: 300`

### Product matching

The model returns a `recommended_product_id` integer. The action resolves this to a full product object with a strict equality lookup:

The product table in the prompt includes the ID column so the model has it available when forming its response. If `find` returns `undefined`, the response screen renders the compliment text without a product card—a graceful degradation that doesn't break the experience.

## Server-sent events

There is one display: the mirror itself. SSE exists to give a brand associate a remote—a separate device that can trigger a capture or reset the experience without touching the screen. Rather than polling, it holds a persistent SSE connection to `/api/mirror/events`.

The server maintains an in-memory `SSEClientManager`:

Broadcasting is a simple loop:

On the client, RareMirror subscribes to the event stream:

The `channel` field in each SSE message lets multiple mirror instances share the same server without interfering with each other. A message with `channel: "booth-2"` is ignored by a client registered to `"booth-1"`.

This is optional, but a nice feature to have in a retail/event setting where you don’t want to be opening up the display to debug or reset.

## Client state machine

The component tracks five states:

Here are the transitions during a normal session:

The `LOADING → RESPONSE` transition is triggered by `useEffect` watching `useActionData`. The `RESPONSE → EXIT` transition is handled inside the `ResponseScreen` component itself, via a countdown timer.

### Capture timing

The Rare Beauty version adds a deliberate two-second delay between pressing the button and taking the screenshot:

The loading screen immediately shows "Step back and smile"—the delay gives the customer time to reposition before the actual photo is taken. This materially improved recommendation quality during testing: photos taken at arm's length with the subject centered in frame produce better skin tone analysis than close-up, off-angle shots.

### The response screen and auto-reset

The response screen manages its own exit timer:

The result is visible for 10 seconds before a circular SVG countdown appears in the corner. After five more seconds, the screen advances to `EXIT` which shows, "Please exit the booth." Pressing the button then reloads the page, resetting to idle for the next customer.

The circular countdown is a pure SVG component driven by `stroke-dashoffset`:

As `countdownValue` decrements each second, `strokeDashoffset` increases, erasing the arc clockwise. A CSS `transition: stroke-dashoffset 1s linear` smooths each step.

### Screen transitions

Between every state change, the UI fades out and back in:

`ScreenTransition` detects when `currentScreen` changes, sets `opacity: 0` (plus `scale(0.98)` and `blur`), waits half the transition duration, swaps the rendered screen, then sets `opacity: 1`. The content swap happens at the midpoint of the fade—when the screen is fully invisible—so there's no visible jump.

## Prompt engineering

The base prompt for the Rare Beauty experience is about 100 words of structured instructions: role definition, a curated list of approved compliments to draw from, tone constraints (response ≤ 100 characters including spaces), and explicit exclusions (teeth, wrinkles, race, deformities, gender). The product list appended to the prompt includes `when_to_recommend` guidance for each shade, written to match observable visual features the model can assess from a headshot.

A few things we learned tuning the prompt:

**Hard constraints on length work.** "No more than 100 characters including spaces" is more reliable than "be concise." Models follow concrete limits better than adjectives.

**Curated compliment lists improve consistency. **Giving the model 50+ pre-approved compliments to choose from produces more brand-appropriate output than asking it to generate freely. The model selects the most fitting option rather than inventing one.

**Exclusion lists matter for safety. **Explicitly listing what not to mention (race, religion, deformities) is more reliable than trusting the model's defaults. This is non-negotiable in a brand activation context.

**Inventory deltas can influence recommendations.** The inventory field in each product entry lets the prompt tell the model to weight products that are running low—a soft nudge, not an override. The prompt explicitly says to do this "only if it respects the non-negotiable guidelines."

## Configuration

Each mirror deployment is a thin route file that exports a `MirrorConfig`:

This makes it straightforward to spin up the same system for a different brand or event: swap the prompt, swap the product list, point to a different auth secret. The component, action, and SSE infrastructure are unchanged.

## The companion demo

The [demo](https://gist.github.com/nikodraca/e898db888a1bd09ba3a1adf137dde6a0) strips this down to its minimum viable form: one file, no auth, no SSE, no transitions, no brand asset. If you're building something similar and want a starting point before adding production layers, that's the place to start.

We’re excited about magic mirrors because they offer a flexible interface for creating delightful in-store experiences that show off your brand and products. Once you’re familiar with the system, you can generate a new ‘mirror mode’ in just a few hours. It’s up to you whether it’s helpful, transactional, entertaining, or all of the above. Under the hood, it’s really just a browser-based experience running behind reflective glass.
