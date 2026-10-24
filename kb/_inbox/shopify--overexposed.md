---
title: 'Building Overexposed: understanding application exposure (2026)'
kind: blog
topic: null
subtopic: null
secondary_topics: []
summary: null
triage: null
skip_reason: null
source: shopify
url: https://shopify.engineering/overexposed
author: Simar Singh
published: '2026-10-19'
fetched: '2026-10-24T06:16:09Z'
classifier: null
taxonomy_rev: 2
words: 1860
content_sha256: da825e8a8e8c35366ffd6342a02ab44e7f7debd3c11c19c91623028b9370f675
---

# Building Overexposed: understanding application exposure (2026)

Which applications have internet exposure? Which endpoints allow access without authentication? Public access can be intentional. The challenge is to understand it and check whether it matches policy. Applications can run across many teams and cloud services. As these applications change, keeping track of their internet exposure and access controls requires regular checks.

We built a scanner called Overexposed to solve for this. It checks two types of internet-facing services: Kubernetes Ingresses on Google Kubernetes Engine (GKE), and Cloud Run services. It starts with the cloud’s inventory of deployed services, then checks whether each candidate allows access without a login. For every candidate endpoint, it gives a verdict and a reason.

## How the scanner works

Overexposed runs on a schedule, and here’s what it does:

1. **Ask the cloud what is running:** The scanner uses GCP’s Cloud Asset Inventory API to find deployed Kubernetes Ingresses and Cloud Run services that might be reachable from the internet.
2. **Probe like a stranger:** For every endpoint, the scanner sends one anonymous HTTP request and reads the response the way an outsider would.
3. **Interpreting the result with policy:** The response maps to one of six verdicts: exposed, expected, protected, not found, unreachable, or inconclusive. Some endpoints intentionally allow anonymous access. We record approved public endpoints in a reviewed allowlist, matched by exact host and path. If the probe finds one of them open, the verdict is expected instead of exposed. If the probe finds it protected, the entry is probably stale, and we flag it.
4. **Record a verdict and evidence:** Every endpoint is stored with its final verdict and the evidence behind the call: what was configured, what the probe saw, where access was blocked, and which team owns it.

![A flowchart showing how the scanner works. Step 1: Ask the cloud what is running. Step 2: Probe like a stranger. Step 3: Interpret the result with policy. Step 4: Record a verdict and evidence.](https://cdn.shopify.com/s/files/1/0779/4361/files/How_the_scanner_works.jpg?v=1792428319)

## Finding what is really running: why we stopped reading config files

### Config shows intent, not enforcement

Our first approach was to read the Kubernetes files in our infrastructure repository. It looked for [Ingresses](https://kubernetes.io/docs/concepts/services-networking/ingress/) on a public hostname with no authentication setting. Then it sent a live request to each one. This approach failed in three ways:

- **False alarms:** Some teams set the [proxy authentication settings](https://kubernetes.github.io/ingress-nginx/user-guide/nginx-configuration/annotations/) directly. The scanner did not recognize those settings, so it flagged protected apps.
- **Misses:** An [admission controller](https://kubernetes.io/docs/reference/access-authn-authz/admission-controllers/) changes the settings when a cluster accepts an Ingress. It does not run in every cluster, so a correct setting can have no effect.
- **Blind spots:** Some Ingresses come from other repositories or from platform tools. The scanner did not see them.

A repository shows what a team wanted, not what the cluster actually runs.

![A flowchart that describes how the repository shows intent. The cluster shows what is enforced.](https://cdn.shopify.com/s/files/1/0779/4361/files/The_repository_shows_intent.png?v=1792428448) 


### Ask the cloud instead

Google Cloud keeps an inventory of all resources in an organization. [Cloud Asset Inventory](https://cloud.google.com/asset-inventory/docs/overview) includes the Ingresses that GKE accepted after all admission controllers ran. It also includes Cloud Run services and load balancers. [One search](https://cloud.google.com/asset-inventory/docs/searching-resources) gets the resources, and a second search gets their access policies without needing cluster credentials.

```
# inventory.py (simplified)
from google.cloud import asset_v1
from google.protobuf.field_mask_pb2 import FieldMask
PUBLIC_SURFACES = [
    "networking.k8s.io/Ingress",   # admitted GKE Ingresses
    "run.googleapis.com/Service", # Cloud Run services
]
def live_surfaces(scope: str):
    """scope: "organizations/<id>", "folders/<id>" or "projects/<id>"."""
    request = asset_v1.SearchAllResourcesRequest(
        scope=scope,
        asset_types=PUBLIC_SURFACES,
        read_mask=FieldMask(paths=["*"]),  # include the full resource body
        page_size=500,
    )
    client = asset_v1.AssetServiceClient()
    yield from client.search_all_resources(request=request)
```
The inventory also turned up Cloud Run services in many projects that our first scanner never checked. We added them to the scan.

## Seeing what an outsider sees: probing like a stranger

The inventory shows what *can* be exposed. Only a request from outside shows what *is* exposed. The scanner sends that request as an anonymous user.

### Probe rules

- Send HEAD first. Use GET only if the server rejects HEAD.
- Do not follow redirects automatically. Follow a maximum of three, and check each one.
- A redirect to an identity provider means it’s protected.
- A 401 response with an authentication challenge means it’s protected.
- A 200 response with real content means it’s exposed.
- If only /admin is protected, also test /ADMIN and other variations. Path rules can be case-sensitive.

### "Allow all traffic" is not the same as public

Cloud Run has two separate controls:

- [Ingress settings](https://cloud.google.com/run/docs/securing/ingress) control which networks can reach a service
- [Identity and Access Management (IAM)](https://cloud.google.com/run/docs/securing/managing-access) controls who can call it

A service is public only if anonymous users (represented in GCP by the principal allUsers) have the invoker role, or if the invoker check is off. If a service allows all traffic but limits the invoker role, strangers get a 403. That is not an exposure.

A load balancer changes this. The service behind a load balancer can [allow anonymous calls](https://cloud.google.com/run/docs/authenticating/public). If authentication is required, the load balancer or the application can enforce it. One option is [Identity-Aware Proxy (IAP)](https://cloud.google.com/iap/docs/concepts-overview). The scanner reads the load balancer's [URL map](https://cloud.google.com/load-balancing/docs/url-map-concepts) to find which service answers each path.

![A flow chart showing where authentication can happen on the path to a Cloud Run service.](https://cdn.shopify.com/s/files/1/0779/4361/files/Where_authentication_can_happen.png?v=1792428568) 


## Protect the scanner too

An attacker can use a scanner to send requests to internal systems. This is a server-side request forgery (SSRF) risk. Even a normal-looking hostname can resolve to a private address.

We check each hostname and every IP address returned by DNS. We reject known internal names and disallowed addresses, such as private and loopback addresses.

The scanner connects directly to a checked IP address, without looking up the hostname again. This prevents a second DNS lookup from changing the destination. We keep the original hostname for the HTTP request and HTTPS certificate checks. We repeat the destination checks before each redirected request.

These checks reduce risk, but they are not enough on their own. Also restrict the scanner’s network access to block internal services and cloud metadata endpoints.

## Classifying the evidence without guessing

An HTTP response is a clue, not always an answer. We combine what was deployed, what the anonymous probe saw, and whether the endpoint was approved to be public. That gives us six possible verdicts:

- **Exposed**: Anonymous access worked, but no approved allowlist entry matched. The result needs review.
- **Expected:** Anonymous access worked and matched an approved allowlist entry.
- **Protected:** Authentication or another access control blocked the request
- **Not found:** The service responded, but the endpoint was not there
- **Unreachable:** The scanner could not connect
- **Inconclusive:** The scanner got a response, but not enough evidence to make the call

### One status code, different meanings

We keep the rules in one table, so reviewers can see all of them in one place. The table also showed a surprise: one status code can mean different things.

```
# outcomes.py (simplified)
EXACT_OUTCOMES = {
    (INGRESS, 200):  (Verdict.EXPOSED, None),
    (INGRESS, 401):  (Verdict.PROTECTED, Reason.AUTH_CHALLENGE),
    (INGRESS, 403):  (Verdict.INCONCLUSIVE, Reason.DENIED),
    (INGRESS, 404):  (Verdict.NOT_FOUND, Reason.MISSING),
    (CLOUDRUN, 401): (Verdict.PROTECTED, Reason.AUTH_CHALLENGE),
    (CLOUDRUN, 403): (Verdict.INCONCLUSIVE, Reason.DENIED),
    (CLOUDRUN, 404): (Verdict.INCONCLUSIVE, Reason.MISSING),
}
def classify_status(status: int | None, surface: Surface):
    if status is None:
        return Verdict.UNREACHABLE, Reason.TRANSPORT_ERROR
    if (surface, status) in EXACT_OUTCOMES:
        return EXACT_OUTCOMES[(surface, status)]
    if 500 <= status < 600:
        return Verdict.INCONCLUSIVE, Reason.SERVER_ERROR
    return Verdict.INCONCLUSIVE, Reason.OTHER
```
Look at 404. Behind an Ingress, 404 means that the proxy answered and the path does not exist. On Cloud Run, Google's front end can send 404 before your app runs, so that 404 tells you nothing about authentication. A 403 response is not proof of protection either. Many apps send 403 for other reasons.

![A flowchart showing how one status code can mean different things](https://cdn.shopify.com/s/files/1/0779/4361/files/One_status_code_different_meanings.png?v=1792428645)

### An allowlist is context, not a shortcut

An allowlist entry is not a reason to skip the check. We keep exceptions in code so additions and changes go through review. The scanner still probes the endpoint on every run. If anonymous access works and matches the approved endpoint and path, the result changes from *exposed* to *expected*.

We check allowlisted endpoints on every run because services change. An endpoint might start requiring authentication or disappear altogether. When that happens, we keep the result and mark the allowlist entry for review.

Our rule is simple: uncertainty does not mean protected. If the evidence is incomplete or contradictory, the scanner reports *inconclusive* and keeps it visible for us to investigate further.

## Keeping verdicts useful over time

### Record the reason, not just the result

A verdict without a reason is hard to use. Each result records what was configured, what the probe saw, whether an allowlist entry applied, and, when available, which team owns the endpoint.

We do not store response bodies or credentials because they may contain sensitive information and are not needed to explain the verdict. We keep only what we need to explain the verdict, investigate it, and compare it with later scans.

### Reduce uncertainty without guessing

In our early runs, most results were "inconclusive" - about three in four in one July run. We wanted more results that teams could act on. We focused on reducing inconclusive results where better evidence could support a clear verdict.

We grouped the results by reason and worked through the biggest groups. We added clearer verdicts when the evidence supported them like *not found* and *unreachable*. If the evidence was still unclear, the result stayed inconclusive.

Before changing a rule, we replay it against saved results from previous scans and compare every verdict. This shows us what will change before we ship it. Within a few weeks, we reduced inconclusive Ingress results by about 80%.

## Build with AI, then test the tests

AI coding agents helped us write Overexposed. AI code review checked every pull request. This made us fast, and also showed us a risk: a test can pass but check the wrong thing.

For example, one test checked that a SQL parameter existed. It didn’t check that the query used it. To catch gaps like this, we use [mutation testing](https://en.wikipedia.org/wiki/Mutation_testing) on our guards. We remove the fix and run the tests. If the tests still pass, the tests are wrong.

We also keep one canary target for each verdict, with a known expected result. If a change gives a canary the wrong verdict, the tests fail. We built such testing into the pipeline that runs periodically, catching any regression early.

## What we learned

To find apps without authentication, you need a true inventory, a careful probe, and honest results. We needed to build the inventory from what the cloud runs, not from what a repository says; probe as a stranger; give every result a reason; and test rule changes on saved results.

A scanner that guesses isn’t something we can rely on. A scanner that explains each verdict helps teams confirm expected access, investigate uncertainty, and change access controls when needed.

We've put together a [starting point for building a similar scanner](https://gist.github.com/ss-shopify/37e1e3d51f0ee9b60b61b72a45a8656e) to meet your use case.

How do you discover and assess your applications’ internet exposure? Tell us at [@ShopifyEng](https://x.com/ShopifyEng).
