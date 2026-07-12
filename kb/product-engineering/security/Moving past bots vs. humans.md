---
title: Moving past bots vs. humans
topic: product-engineering
subtopic: security
secondary_topics:
- industry/trends
summary: 'Argues bot detection must move from ''bots vs. humans'' to intent and behavior
  as AI agents fetch raw content without rendering pages: covers Web Bot Auth (HTTP
  message signatures) for crawler identification and private rate limiting for clients
  that no longer behave like browsers.'
source: cloudflare-ai
url: https://blog.cloudflare.com/past-bots-and-humans/
author: Thibault Meunier
published: '2026-04-21'
fetched: '2026-07-11T04:13:12Z'
classifier: claude
taxonomy_rev: 1
words: 3743
content_sha256: 52dc53c795b0ddff5b8de4d31559600e6730823df3bbdfcac15aff32bf27dbfd
---

# Moving past bots vs. humans

For us humans to interact with the online world, we need a gateway: keyboard, screen, browser, device. What is called "human detection" online are patterns that humans use when interacting with such devices. These patterns have changed in recent years: a startup CEO now uses their browser to summarize the news, a tech enthusiast automates the process to book their concert tickets when sales open at night, someone who's visually impaired enables accessibility on their screen reader, and companies route their employee traffic through zero trust proxies.

At the same time, website owners are still looking to protect their data, manage their resources, control content distribution, and prevent abuse. These problems aren’t solved by knowing whether the client is a human or a bot: There are wanted bots and there are unwanted humans. These problems require knowing intent and behavior. The ability to detect automation remains critical. However, as the distinctions between actors become blurry, the systems we build now should accommodate a future where "bots vs. humans" is not the important data point.

What actually matters is not humanity in the abstract, but questions such as: is this attack traffic, is that crawler load proportional to the traffic it returns, do I expect this user to connect from this new country, are my ads being gamed?

What we discuss with the term “bots” is really two stories. The first is whether website owners should let known crawlers through when they are not getting traffic back. We have touched on this with [ bot authentication with http message signatures](https://blog.cloudflare.com/web-bot-auth/) for crawlers that want to identify without being impersonated. The second is the emergence of new clients that do not embed the same behaviors as web browsers historically did, which matters for systems such as

[.](https://blog.cloudflare.com/private-rate-limiting/)

__private rate limit__In this post, we explore how web protection works today, and how it must evolve when the line between bot and human is fading.

When we use the Web, we don't talk directly to the thousands of servers we interact with every day. We use Web browsers. These are also known as "[ user agents](https://www.rfc-editor.org/rfc/rfc9110.html#name-user-agents)" because they act on our behalf, representing our interests so that we can safely shop, read, and watch the Web without giving sites access to our entire computer or phone.

Websites also have an interest in how browsers work. They want to make sure that their content is presented accurately (fits the screen on mobile, has the right background color, the correct language). Websites also want to ensure that people are able to complete a purchase, read their articles, use their microphone, or sign in securely without a password. They also want people to see the ads beside the articles.

This tension between the interests of browser users and websites has been going on for a long time. Publishers typically want pixel-level control over the experiences of their users, but the people on the other side of the browser often want to use the data they access in ways that weren't envisioned by the publisher.

Web browser vendors and the standards ecosystem around them have paid [ careful attention](https://www.w3.org/TR/design-principles/) to balancing these interests, sometimes with great controversy. For example, you can use browser extensions to block ads, but over time

[have restricted what such extensions can do. Accessibility standards (e.g.,](https://arstechnica.com/gadgets/2024/08/chromes-manifest-v3-and-its-changes-for-ad-blocking-are-coming-real-soon/)

__browsers__[) have paved the way for using Web content in ways that aren't about pixels, backed in many places by regulatory requirements. One can question the specifics of each of those tradeoffs, but they come as a package: if you want to be on the Web, you have to accept it, whether you are a publisher or a user.](https://www.w3.org/WAI/)

__WCAG__Now, however, that balance is shifting. Having an assistant summarize the news or aggregate research is not a new concept, but AI democratizes this capability for everyone. The friction comes from how these emerging clients operate. A human assistant might print an article or take a screenshot without the publisher knowing, but they still use a standard web browser to render the site in the first place. AI agents bypass this step, disrupting the balanced approach to publishers’ vs. users’ rights that browsers built. They quietly fetch the raw data without rendering the page. For publishers, because of their overlap with pre-existing browser traffic, these clients are inherently opaque. Website owners cannot tell if their fetched content is serving one private report (possibly distorted, possibly unattributed) or being ingested to train a model for a million users, which disrupts the predictable (and monetizable) traffic that keeps their sites online.

The implicit agreement that made the Web work is breaking down. To understand how, the next section goes over a common architecture on the Internet.

Let’s take a step back, and look at one of the main deployment patterns on the Internet: the client-server model. A client makes a request to a server to obtain a resource:

*Figure 1: Client-Server model. A client sends a request which the server responds to.*

To handle more requests, a website can increase its capacity to serve; it can deploy additional servers or place a cache in front of static traffic. Similarly, the number of requests coming from the client side can increase if one client makes more requests, or if the number of clients multiplies.

*Figure 2: Multiple clients send multiple requests to different servers, with one fronted by a CDN.*

That simplicity is part of what made the Web successful. It allows many kinds of clients to exist, and it allows the network to evolve without each server needing to know exactly what software is on the other end.

*Figure 3: Two different client contexts that send requests to servers. Each server only sees a request, but not the end-user behind it.*

That openness also creates uncertainty. A website can see a valid request for a resource, yet it usually cannot know what happens after the response leaves the server: whether the content is rendered for one person using a keyboard, a mouse, and a screen to control a browser; or if it's an independent program making requests automatically, archiving responses, indexing them, and feeding into a larger system.

This model works surprisingly well. That is why operating a website can be as simple as starting a web server with a connection to the Internet. It holds only until the server has to decide which requests it can afford to serve, trust, or prioritize.

Sometimes that is about capacity. If your service is provisioned to handle 100 requests per second globally, but you're receiving 200, you have to drop certain requests. If your server only has 1 CPU but incoming requests require 2, you have to drop requests. If the cost of serving 200 is prohibitive, then you have to rate-limit all requests.

You can drop requests at random. It's possibly unfair, and may miss the target by affecting wanted clients, but it works. In the absence of other signals, there is no other choice.

And capacity is only part of the picture. Servers also try to distinguish among clients for many other reasons: to separate attacks from ordinary traffic, to manage non-malicious load, to prevent extraction of data, to limit ad fraud, to prevent fake account creation, or to stop automated actions being taken on a user's behalf.

The difficulty is that web clients are unauthenticated by default, while still exposing many partial signals. Therefore, most servers decide to apply access control logic based on the information they receive. If a single IP address is making 10x the number of requests as others, it might be blocked. A server that goes further might infer that this IP address is used by a VPN, and therefore proxies the traffic of [ more than one user](https://blog.cloudflare.com/detecting-cgn-to-reduce-collateral-damage/). The service could decide to apply a coefficient: assuming each client can make 10 requests per second, a shared IP address would be allowed 100 rps before seeing their requests being dropped.

That's one of the keys to bot management: it aims to provide the server with more information about the client to help it make decisions. This information is inherently imprecise, because the client is not under the control of the server. In addition, the same information creates [ fingerprint](https://en.wikipedia.org/wiki/Fingerprint_(computing)) vectors that can be used by the server for different purposes such as personalized advertising. This transforms a mitigation vector to a tracking vector.

At a high level, the server sees the following signals from the client:

- **Passive client signals**: required to make a request on the Internet. Clients necessarily send your IP address, and usually establish a TLS session.
- **Active client signals**: voluntarily provided by the client, often invisible to the end user. This includes a User-Agent header or authentication credentials.
- **Server signals**: information the server observes, such as the geographic location of the edge server handling the request, or the local time the request is received.

To limit and cap volumetric abuse, what matters to the origin is the capability and intent of the client to make multiple requests. In the case of an ad-funded website, the origin needs confidence that ads are actually displayed to the end-user. To preserve their brand, origins may want to ensure that the client has specific rendering capabilities: PDF reader, SVG renderer, virtual keyboard. And if the request is coming from an intercepting proxy, the origin may want to ensure that the request actually originates from an end client

If traffic grows then so do the costs to operate. If clients do not generate value, monetary or not, then the server has no incentive to cover those costs.

Different operators respond to this environment differently. Some large crawlers and platforms identify themselves because predictable access is worth the cost of being attributable. It may even help. Others try to avoid identification: because they expect to be blocked, because they seek anonymity, or because they are operating on behalf of end users. The result is an unstable balance built on partial signals.

This is why the human versus bots frame is misleading. What the origin cares about is not humanity in the abstract, but whether the client is behaving in ways the site can support.

*Figure 4: Rate limit trilemma. Decentralized, anonymous, accountable — pick two*

There's a fundamental tension in how we govern access on the Internet: decentralized, anonymous, accountable — pick two.

- **Fully decentralized + anonymous**means no accountability. A blocked client can spawn a new account without impact on its reputation. This implies that origins have to invest more to manage their resources.- *This is the default of the Web*.
- **Decentralized + accountable**means everyone knows who you are, which works for certain use cases but has clear drawbacks. Think- __OAuth__
- **Anonymous + accountable**likely requires governance, rules, and enforcement. No widely deployed system achieves both properties for the same actor. The closest precedent is the- __Web PKI__- __that governance fails__

Current tools build on elements from that first space to strive for the second: TLS fingerprints, IP addresses, robots.txt. They attempt accountability, but only hold as long as the derived fingerprints remain stable.

For a website owner deciding how to handle incoming traffic, the meaningful distinction isn't necessarily bots vs. humans. It's about balancing the origin’s needs to understand the traffic it receives with the clients’ needs to preserve their privacy.

*Figure 5: A crawler makes multiple request to a server*

Some traffic comes from known operators making high volumes of requests: search engine crawlers, cloud platforms, enterprise infrastructure. These actors often have low privacy expectations. They're infrastructure making millions of requests from identifiable sources. The ability to identify the source of a request helps to mitigate misjudgment if an infrastructure provider is sending you too many requests or accessing pages it should not. Self-identification is one of the [ principles for responsible AI bots](https://blog.cloudflare.com/building-a-better-internet-with-responsible-ai-bot-principles/) we proposed. It is based on these principles that Cloudflare operates its

[, or how we expose](https://radar.cloudflare.com/scan)

__URL scanner for Radar__[.](https://developers.cloudflare.com/changelog/post/2026-03-10-br-crawl-endpoint/)

__crawling capabilities__For this traffic, identity works. More precisely, some operators can tolerate attributable requests because reliable access is worth it. [ Web Bot Auth](https://blog.cloudflare.com/web-bot-auth/) using HTTP Message Signatures allow operators to cryptographically sign their requests.

[,](https://help.openai.com/en/articles/11845367-chatgpt-agent-allowlisting)

__OpenAI__[,](https://developers.google.com/crawling/docs/crawlers-fetchers/google-user-triggered-fetchers#google-agent)__Google__

[, or](https://blog.cloudflare.com/agent-registry/)

__Cloudflare__[, for example, sign requests originating from their platforms. Origins can verify "this request really came from the platform infrastructure" without relying on IP ranges or User-Agent strings.](https://blog.cloudflare.com/agent-registry/)

__AWS__Humans and other end-users rightfully have expectations other than being identifiable, to preserve anonymity without sacrificing their access and quality of experience.

*Figure 6: Three distinct browsers make a request to a server. One is operated by a human, one by an on-device assistant, and one is proxied through a corporate proxy.*

Other traffic comes from many sources, each making relatively few requests. This includes humans browsing the web, researchers doing measurements, scrapers using residential proxies, and increasingly, AI assistants acting on humans’ behalf.

And increasingly the distinction between bots and humans is moot. There is no meaningful difference between the AI assistant booking concert tickets and the human who would have done so manually. Both are distributed. Both need anonymity. In each case, an origin would want to create less friction for users who wish to use the service as intended, rather than abuse it.

Identity could work. To replace the old assumption we had for IP addresses, it should provide a unique, verifiable set of attributes tied to a specific client, proven through an account login, an email address, or a hardware key. However, it implies the need to present this identity when accessing websites. It also undermines [ privacy](https://blog.cloudflare.com/internet-privacy/).

We want to build modern solutions that prove behavior without proving identity.

Since 2019, clients accessing websites via Cloudflare have been able to provide such proof of behavior, by sending a privacy token along with their request. This is due to Cloudflare’s early [ support for Privacy Pass](https://blog.cloudflare.com/cloudflare-supports-privacy-pass/). Privacy Pass, as standardised in

[,](https://datatracker.ietf.org/doc/html/rfc9576)

__RFC 9576__[, lets a client carry an issuer-backed proof of some prior check, such as having solved a challenge, without turning that result into a stable identifier. It defines tokens that are](https://datatracker.ietf.org/doc/html/rfc9578)

__RFC 9578__*unlinkable*with any prior visit, request, or session.

This matters because it offers a different model from fingerprinting. Instead of collecting passive signals, the server can ask the client for an active privacy-preserving signal.

This reduces the friction on session establishment. Privacy Pass has [ scaled to billions of tokens](https://blog.cloudflare.com/eliminating-captchas-on-iphones-and-macs-using-new-standard/) per day across Cloudflare’s infrastructure, primarily for

[.](https://blog.cloudflare.com/eliminating-captchas-on-iphones-and-macs-using-new-standard/)

__privacy relay services__*Figure 7: Privacy Pass Redemption and Issuance Protocol Interaction from *__Section 3.1 of RFC 9576__

The RFC highlights four roles. The issuer trusts one or more attesters to perform some checks before issuing credentials (tokens in the RFC case). The client holds these credentials and decides when to present them, within the right scope. The origin remains in control of which issuers it trusts and what each presentation means. This does not remove abuse or policy questions, it simply provides clients and servers with a privacy-preserving way to handle them.

The system is simple, but it also has bounds: it does not, for example, allow for dynamic rate limits. If a client is issued 100 tokens, and starts consuming too many resources after the first or second session, there’s no way to invalidate the remaining tokens that were previously issued.

In addition, because of the unlinkability property, it’s hard for new issuers to emerge. There is no feedback mechanism that an origin can provide regarding the quality of the signal an issuer token conveys.

Finally, there’s a 1:1 relationship between the number of tokens that an issuer provides, and the number of unlinkable presentations that can be made with those tokens when they are redeemed: one token per presentation. Ideally, we would like a system in which the client contacts an issuer once and can later make multiple presentations scoped to a particular origin context. That points toward user agents holding vouched credentials and presenting proofs derived from them, rather than repeatedly acquiring single-use tokens.

Our goal is to help establish an open [ private rate limiting](https://blog.cloudflare.com/private-rate-limiting/) ecosystem. In that spirit, we are helping to develop and explore new Privacy Pass primitives, such as

[(ARC) and](https://datatracker.ietf.org/doc/draft-ietf-privacypass-arc-protocol)

__Anonymous Rate-Limit Credentials__[(ACT).](https://datatracker.ietf.org/doc/html/draft-schlesinger-privacypass-act-01)

__Anonymous Credit Tokens__With ACT, for instance, clients can prove something like "I have a good history with this service" without revealing "I am this user.” ACT preserves unlinkability between presentations at the protocol level, which is the key cryptographic property here. Even in the [ joint issuer-origin deployment model](https://www.rfc-editor.org/rfc/rfc9576.html#name-joint-origin-and-issuer) in Section 4.3 of RFC 9576, the protocol is designed so that token issuance and presentation are not directly linkable. That does not eliminate correlation through other layers such as IP addresses, cookies, account state, or timing. The same properties can be provided using standardized

[and](https://datatracker.ietf.org/doc/html/rfc9578#name-issuance-protocol-for-priva)

__VOPRF__[primitives within the](https://datatracker.ietf.org/doc/html/rfc9578#name-issuance-protocol-for-publi)

__BlindRSA__[framework that ACT implements.](https://datatracker.ietf.org/doc/draft-meunier-privacypass-reverse-flow/)

__reverse flow__A successful ecosystem needs to be an open issuer ecosystem. In practice, that means more than saying anyone can mint credentials. Origins need to be able to decide which issuers to trust. User agents need a consistent way to present what is being requested. The ecosystem also needs ways for issuers to establish reputation and for relying parties to stop trusting low-quality issuers. No single gatekeeper should control participation.

To make this work, there needs to be a protocol and client API that works across browsers and other user agents. It has to be simple to deploy, clear to users, and narrow enough that browsers can place limits on abusive proof requests rather than merely surfacing them.

Website owners are already reacting to the [ disruption caused by emerging clients](https://blog.cloudflare.com/from-googlebot-to-gptbot-whos-crawling-your-site-in-2025/#robots-txt-ai-bots-gptbot-leads-twice). This is partly caused by large-scale

[and](https://blog.google/innovation-and-ai/technology/safety-security/serpapi-lawsuit/)

__scraping__[, and also by user agents acting in ways](https://redditinc.com/hubfs/Reddit%20Inc/Content/Reddit%20v.%20SerpApi.pdf)

__model training__[. Websites, therefore, have asked for more technical means to block AI crawlers and associated tools. In an ecosystem where the lines between bots and humans are increasingly blurred, the measures we have today will become less effective on their own.](https://www.aboutamazon.com/news/company-news/amazon-perplexity-comet-statement)

__sites did not anticipate__If those measures aren't effective, we can expect sites to pivot: requiring an account to see any content, or tying access to a stable identifier. This means no more ad-supported login-free articles, no more "three free articles a month.” Other content businesses may move away from the Web completely, offering their data and services directly to AI vendors for a fee, or within walled gardens operated by large platforms.

These outcomes are bad. Everyone benefits from the open access to information that the Web offers. It is not that all sites will make these choices. There are many reasons for offering content online, and not all of them are commercial. But if enough sites do, they change what "normal" is on the Web to be something worse.

That matters because the open Web is an environment in which different clients can gather information from different sources without relying on a handful of players. We also benefit from having a diversity of sources of information. On a Web where access to information is largely mediated through a small handful of companies, we put too much power into too few hands. The result is not just more friction for anonymous clients, but a more brittle Internet with fewer ways for publishers to meet users.

We should be clear about what we're building. Infrastructure for proving properties can become infrastructure for requiring properties. Anonymous credentials are meant to prove something about their holder; for example, "I solved a challenge" or "I have not exceeded a rate limit." But a system that can prove any single attribute is also capable of proving other attributes, which is a source of concern.

Today, presenting a Privacy Pass token [ may convey "solved a CAPTCHA"](https://blog.cloudflare.com/cloudflare-supports-privacy-pass/). Tomorrow, the same systems could prove entirely different attributes. For instance, issuing tokens only to devices that  "have device attestation" excludes older devices and their users. Similarly, requiring attributes such as "has an Apple or Google account" excludes users of non-mainstream platforms.

Once the infrastructure exists to verify anonymous proofs, what gets proven can expand. We need to make sure this does not gate access to the Internet.

Gates already exist. Platforms increasingly require identity. Websites are blocking traffic coming from shared proxies. The question isn't whether gates will appear, it's whether the user remains in control of their privacy.

As we’ve discussed, bot management requires some signals to be shared. The alternatives to anonymous proofs are worse. Without the ability to prove attributes anonymously, every gate requires fingerprints: retry from a specific browser, link your account, don’t use a VPN. These may not even be options to people, such as the ones which [ have no idea their connections are proxied](https://blog.cloudflare.com/detecting-cgn-to-reduce-collateral-damage/).

Privacy-preserving credentials do not remove the need for trust or policy. They can make those demands more explicit and less pervasive. Unlike fingerprints, proofs are explicit. Users can see what is being asked, and clients such as web browsers and AI assistants can help enforce consent.

There is a simple test to evaluate the next methods for the Internet that serves everyone: do the methods allow anyone, from anywhere in the world, to build their own device, their own browser, use any operating system, and get access to the Web. If that property cannot hold, if device attestation from specific manufacturers becomes the only viable signal, we should stop.

This means we need to foster an open issuer ecosystem, where no single gatekeeper decides who can participate. In the rate limit trilemma, decentralization is mandatory on the open Web. We don't yet know fully how to build it, but we know we need to foster it.

Until now the Web has largely been in balance. Some aspects may have been a happy accident, while others could have been inevitable. For many end users and publishers, it worked because the Web stayed open enough to support a variety of clients accessing a similar variety of resources.

That balance is at risk. Privacy-preserving primitives for the Web are one attempt to build a different outcome: privacy-preserving, open, accountable. It is not guaranteed to succeed. But it is better than waiting.

If you are interested in tracking and participating, this work happens in the open at the IETF and at the W3C. We believe the existing places where people gathered to shape the Web of today are the best places to design the Web of tomorrow.

The [ Internet is for the end user](https://www.rfc-editor.org/rfc/rfc8890.html), and they need to be in the center of it.
