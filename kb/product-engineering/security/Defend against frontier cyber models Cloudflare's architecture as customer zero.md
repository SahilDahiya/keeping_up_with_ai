---
title: 'Defend against frontier cyber models: Cloudflare''s architecture as customer
  zero'
topic: product-engineering
subtopic: security
secondary_topics: []
summary: Follow-up to Project Glasswing detailing Cloudflare's customer-zero defense
  architecture against frontier cyber models — which compress discovery, exploit-chain
  construction, and PoC generation — using Cloudforce One threat intel feeding WAF
  rules deployed network-wide in under 30 seconds (e.g. React2Shell pre-advisory).
source: cloudflare-ai
url: https://blog.cloudflare.com/frontier-model-defense/
author: Rohit Chenna Reddy
published: '2026-06-09'
fetched: '2026-07-11T04:12:58Z'
classifier: claude
taxonomy_rev: 1
words: 2250
content_sha256: 3deed5c1742e476ac6df317d4b1a117a22fcf07c37b6a0c9ec1a13c4d91a71eb
---

# Defend against frontier cyber models: Cloudflare's architecture as customer zero

A few weeks ago, we [ wrote about Project Glasswing](https://blog.cloudflare.com/cyber-frontier-models/) and what we observed when we pointed cyber frontier models at our own code. Since then, we’ve seen that the part of the post that has resonated most deeply is the argument that the architecture around the vulnerability matters more than the speed of the patch.

In the conversations we've had with CISOs and security teams since, the questions have been consistent: what does our architecture actually look like, what should we monitor for, where do we start, and how can Cloudflare help?

Before getting into the details: the architecture below is built almost entirely from Cloudflare's own products, because Cloudflare security is [ customer zero](https://blog.cloudflare.com/tag/customer-zero/) for the security products we build. The Cloudflare stack already exists in front of our code, employees, and customer-facing applications. If you're a Cloudflare customer, every layer below is available to you today. If you're not, the principles still apply to whatever stack you've built.

In the [ previous post](https://blog.cloudflare.com/cyber-frontier-models/), we showed how a cyber frontier model like Mythos changes the attacker’s timeline. It can find vulnerabilities, reason through exploit chains, and generate working proofs faster than earlier models. While models like Mythos do not change the shape of an intrusion — reconnaissance, initial access, lateral movement, persistence, and exfiltration still have to happen — the difference is in the speed and scale. When pointed at the open web, a model can find and hit low-hanging fruit quickly. Against a hardened target, it still has to probe, and adapt, and it often produces more noise than a careful human operator would.

Discovery, exploit chain construction, and proof-of-concept generation used to be the gating constraints on producing a working attack. A frontier model handles all three in a fraction of the time. Work that used to be slow and methodical is now fast and indiscriminate.

While AI is accelerating how fast developer teams at Cloudflare and many other companies can ship code, the security team’s work has not compressed the same way. An attacker only needs one opening to get in, while security teams need to find and close them all. Writing a fix, regressing it, and shipping it without breaking the code around it has constraints that AI doesn't remove. We learned this the hard way when we let an AI coding assistant write its own patches against our own bugs, as we described at the end of the previous [ post](https://blog.cloudflare.com/cyber-frontier-models/). Some of those patches fixed the original bug while quietly breaking something else the code depended on.

As these models become more competent and capable, our main focus from a threat standpoint comes down to three things. Each one shapes the architecture we walk through in the rest of this post.

- The first is the - **speed of discovery.**Frontier models make it easier to search large bodies of public code, including the open-source libraries that many companies depend on. That does not mean every bug in a library is exploitable, or that library bugs are where most vulnerabilities live. Exploitability still depends on how the code is used, whether attacker-controlled input can reach the vulnerable path, and the protections that sit around it. But widely used open-source libraries and frameworks give attackers a shared surface to study at scale. When a real, reachable vulnerability exists there, a model can help find it, reason about possible exploit paths, and generate proof-of-concept variants faster than maintainers and defenders can review every downstream use. The gap between when an attacker discovers a vulnerability and when defenders learn it exists is what worries us most. If you are not running these models against your own code, it is safe to assume someone else is.
- The second is - **exploit**- **volume and adaptation.**A model can produce thousands of variations of a single exploit and run reconnaissance at the same scale. All that volume gives an attacker an advantage, but it won’t necessarily get them past signature-based detections. Many of those iterations will have the same underlying signature, so a rule that catches the first one will catch the rest. Adaptation is how they will get past signature-based detections. Ask a model to show you a SQL injection, and it will return a textbook example. Tell it there is a WAF in the way, and it will start probing, learning what gets blocked, and rewriting the payload until it can slip past the rule blocking it.
- The third is - **the impact when a vulnerability is inevitably exploited.**No architecture catches everything. After the vulnerability is exploited, the question we ask ourselves is: where can the attacker get to with one identity, one path, or one credential, before something else stops them? If the answer is "anywhere they want," the vulnerability was never the problem. The architecture around the vulnerability was.

We see roughly a fifth of the web and that tells us, in real time, which payloads are mutating, which patterns are picking up, and where attacker tooling is moving next. Two teams turn that visibility into defense.

First is [Cloudforce One](https://www.cloudflare.com/cloudforce-one/), our threat intelligence, research, and operations team, which sits within the Cloudflare security organization. They turn what we see across the network into insights the rest of the stack can act on: tracked adversaries, emerging campaigns, and indicators of compromise (IOCs). The hard part of this work was never knowing what is malicious — it was the delay in mitigation. Knowledge of a new threat normally has to travel from a threat report, into a feed, and then into a company’s defense before it can be used to block anything. Attackers have learned to move faster than that. Our network closes that gap: Cloudflare customers can now use Cloudforce One threat intelligence

[to block high-risk traffic.](https://blog.cloudflare.com/realtime-threat-intel-waf-rules/)

__directly within the WAF__Second is the team that owns the WAF engine that does the actual detecting: the managed rulesets that run in front of our own properties and are available to every Cloudflare customer, the machine learning behind [ WAF Attack Score](https://developers.cloudflare.com/waf/about/waf-attack-score/), and the relationships that sometimes let us ship a rule before a CVE is publicly disclosed. The team is globally distributed and moves fast, releasing rules within hours of a proof-of-concept of an attack becoming known. Once a detection is deployed, it reaches our entire network, along with every Cloudflare customer, in under 30 seconds.

[is a recent example: a managed WAF rule](https://blog.cloudflare.com/react2shell-rsc-vulnerabilities-exploitation-threat-brief/)

__React2Shell__[, hours before the official advisory was published.](https://blog.cloudflare.com/waf-rules-react-vulnerability/)

__was protecting our own properties, and everyone else's on Cloudflare__The scoring layer, the defenses we put in front of the application, and the containment around the vulnerability all build on what these two teams see.

Signature-based defenses were built for a world where novel exploits were scarce and variations took weeks. Cloudflare's traditional SLA from a fresh proof-of-concept to a live, deployed rule has been 12 hours. With the advent of frontier models, this is not good enough anymore. Detections need to be in place [ before a CVE is discovered](https://blog.himanshuanand.com/2026/05/the-90-day-disclosure-policy-is-dead/). This is why we layer ML-based detection in front of the traditional signature-based WAF.

The model is trained on a large body of past attack traffic, and it catches new variants of vulnerabilities before they're publicly known. A novel [ SQL injection](https://www.cloudflare.com/learning/security/threats/sql-injection/) or remote code execution chain is almost always a rearrangement of attack shapes the model has seen before, even when the specific exploit is brand new. We run the model on every request and assign a WAF Attack Score between 1 and 99, based on how closely the request resembles those underlying shapes, not against a list of known-bad signatures. The lower the score, the more aggressively we treat the request. That score determines whether we let the request through. We apply a similar scoring methodology to AI prompts with

[: rather than check each prompt against a list of known malicious prompts, we score how closely a prompt resembles an actual attack.](https://developers.cloudflare.com/waf/detections/ai-security-for-apps/)

__AI Security for Apps__Those capabilities only matter once they're stacked in front of an application, and the first layer in our defense-in-depth approach is the [WAF](https://www.cloudflare.com/en-gb/application-services/products/waf/). Anything that matches a known-bad pattern gets dropped before it reaches the application, which clears the bulk of the obvious traffic and lets the more specialized layers below focus on what's left.
On the API surface, we run a positive security model through

[. Instead of trying to anticipate every bad request, we describe what a valid request to each API looks like, either from the API's own definition or learned from our real traffic, and anything that doesn't fit doesn't get through. This neutralizes the advantage of frontier AI models: because we only permit validated traffic, generating thousands of new attack variations fails to bypass the system.](https://www.cloudflare.com/en-gb/application-services/products/api-shield/)

__API Shield__*Cloudflare’s layered architecture*

[Bot Management](https://www.cloudflare.com/learning/bots/what-is-bot-management/) catches probing traffic on our network before frontier models can build a map. It scores every request on how likely it is to be automated, using the same signals across our whole network: how the client behaves, whether it looks like a real browser, and whether the connection matches a known-bad pattern. An attack only lands if it can find a soft spot.

[Zero Trust Network Access](https://www.cloudflare.com/sase/products/access/) is used for every internal application. The implicit trust of being inside the network is replaced with explicit per-request identity and policy for every employee accessing every tool. The value of this was clear when one of our engineers shipped a misconfigured tool. A flat network would have exposed everything on the same segment, but in our deployment, the exposure stopped at the tool itself. We built

[afterwards so newly deployed or misconfigured applications can't be reachable before an access policy is in place.](https://developers.cloudflare.com/cloudflare-one/access-controls/access-settings/require-access-protection/)

__Require Access Protection__[IdP Federation](https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/idp-federation/) makes that secure by default posture easier to keep consistent across every Cloudflare account — which becomes even more necessary when more people are shipping internal tools quickly. Instead of asking each team to wire up SSO separately, we configure our identity provider (IdP) once and share it across the organization. New accounts get SSO automatically, recipient-side IdP connections are read-only, and Access policies in each account still evaluate the resulting identity as part of the normal request flow.

[MCP Server Portal](https://developers.cloudflare.com/cloudflare-one/access-controls/ai-controls/mcp-portals/) gives teams a controlled way to connect AI agents to enterprise systems. Agents access MCP servers that are centrally managed through a single portal, with every action logged. That way when an agent acts on someone's behalf, we know what it did, what it touched, and whether it should have been allowed to. The full picture of how we built it is in our post on

[.](https://blog.cloudflare.com/enterprise-mcp/)

__enterprise MCP__[AI Gateway](https://www.cloudflare.com/developer-platform/products/ai-gateway/) runs in front of our internal AI tools the same way

[runs in front of customer-facing AI features, with the same scoring and the same visibility. Inside the company, the visibility piece is more useful than the blocking, because we needed to see what engineers were actually building before we could write meaningful policy on it.](https://developers.cloudflare.com/waf/detections/ai-security-for-apps/)

__AI Security for Apps__Frontier models can help attackers find vulnerabilities, adapt payloads, and move faster, but they still have to pass through the layered defense you deploy in front of your application. That is where teams should start:

- Put inspection in front of public applications.
- Define what valid API traffic looks like.
- Use bot detection to limit automated probing.
- Require identity and access policy before any internal tool is reachable.

For AI and agentic systems:

- Route model traffic through a gateway.
- Keep agents connected through approved MCP servers.
- Log what they do.

The goal is to make sure that when one layer misses, the next layer limits what the attacker can see, reach, or change.

That is the point of the architecture around the vulnerability: to limit the scope of an attack. The vulnerability may be what starts the attack, but the architecture determines how far it can go.

Plenty of security stacks look impenetrable on a whiteboard but fall over in practice. That is why we test ours continuously, both at the perimeter and inside our environment, with our red team involved across both.

**At the perimeter**, frontier models are one tool we use to test our application security stack as an adaptive attacker. These models sit alongside the rest of our red team and detection workflows including: manual testing, threat intelligence, observed traffic patterns, proof-of-concept analysis, and signals from our own network. Together, those inputs help us decide where to aim testing: newly launched products, recently changed surfaces, and the paths an attacker is most likely to probe first. The most important part is the process that follows. When something gets through, we identify the gap, use the right mix of tools to understand it, write the rule or mitigation, ship the update, and test again to make sure the gap is closed.

**Inside the environment,** our red team starts from the assumption that the perimeter has already failed. They look at what has changed, where sensitive systems carry risk, and whether one compromised identity, path, or credential can reach farther than it should. When we change the architecture based on what they find, they run the scenario again against the new version to confirm the gap is actually closed.

We confirm that this architecture is working by continuously testing its behavior during failures, rather than relying on the perfection of individual layers.

If your team is working on the same problems and would like to compare notes, reach out to us at [ security-ai-research@cloudflare.com](https://blog.cloudflare.com).
