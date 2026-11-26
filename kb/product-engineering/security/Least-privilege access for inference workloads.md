---
title: Least-privilege access for inference workloads
kind: blog
topic: product-engineering
subtopic: security
secondary_topics:
- infra-platform/deployment
summary: 'Explains how Baseten applies least-privilege access to inference workloads:
  OIDC short-lived tokens replace permanent cloud keys, sealed read-only BDN volumes
  remove the need for replicas to access the weights bucket directly, and egress restrictions
  limit outbound connections to only the hosts a model actually calls.'
triage: null
skip_reason: null
source: baseten
url: https://www.baseten.co/blog/least-privilege-access-for-inference-workloads/
author: Daniel Leef; Matt Howard; Rachel Rapp
published: '2026-11-25'
fetched: '2026-11-26T06:07:08Z'
classifier: claude
taxonomy_rev: 2
words: 1262
content_sha256: fd267715ce3e104a71d6a3e3b34f07ea7a7d05422d220feef3d3b19fcbc83eae
---

# Least-privilege access for inference workloads

Security
# Least-privilege access for inference workloads

Give each deployment only the cloud access and network connections it needs, with short-lived credentials, sealed volumes, and egress restrictions.


- Authors
- Published

Inference workloads often need to connect securely to external data or services, like loading private weights from cloud storage or fetching LoRA adapters at request time. The easiest way to set that up is with a permanent cloud key and open internet access, but that gives the model far more access than it needs—and it's easy to exploit. Each deployment should access only the resources it needs, without risking exposure of credentials or data.

Baseten gives you controls to set boundaries on that access. OpenID Connect (OIDC) replaces permanent cloud keys with short-lived tokens tied to a specific deployment, so each credential works only for the job it was issued for and expires automatically. The [Baseten Delivery Network (BDN)](https://www.baseten.co/blog/how-the-baseten-delivery-network-bdn-makes-cold-starts-fast/) mirrors your weights once into a read-only volume, so serving replicas never need access to your bucket. Egress restrictions also limit outbound connections to the hosts a model actually calls, so a compromised container can't reach anywhere else. Together, they let teams apply least-privilege access to production workloads.

This blog outlines how to use these controls across a model's deployment lifecycle.

Consider a model whose private base weights live in one Amazon S3 bucket and whose LoRA adapters live in another. Adapters change more often than base weights, so the model fetches them at runtime instead of redeploying.

| Stage | What the model needs | Control | 
|---|---|---|
| Build | Copy base weights from your bucket | OIDC for volume sync | 
| Deploy | Give every replica the same weights | BDN volume mount | 
| Serve | Fetch adapters from S3 | Runtime OIDC + egress restrictions | 

Long-lived credentials (AWS IAM access keys, GCP service account keys) need ongoing management: they need to be stored securely, and their usage needs to be tracked. They also need to be rotated or revoked, because if a key leaks, anyone holding it can use its permissions until it's disabled.

With OIDC, Baseten issues a signed, short-lived token identifying the workload in lieu of a long-lived credential. Your cloud validates that identity against your configured trust relationship and grants access according to your policies—and you don't need to store a long-lived cloud key in Baseten.

To use OIDC for [weight and data loading via BDN](https://docs.baseten.co/training/concepts/storage#load-weights-and-data-with-bdn), configure your cloud permissions to allow BDN volume sync to read the base weights. The sync copies the weights into secure, Baseten-managed storage and publishes them as a [sealed BDN volume](https://www.baseten.co/blog/bdn-sealed-volumes-publish-once-mount-anywhere/): an immutable version identified by a digest of its contents.

bash

```bash
baseten volume sync start \
  --source s3://<bucket>/<prefix> \
  --dest bdn:<namespace>/<volume> \
  --auth-aws-oidc-role-arn arn:aws:iam::<aws-account-id>:role/<role-name> \
  --auth-aws-oidc-region <region> \
  --wait
```
BDN Sealed Volumes let you publish any read-only data once as a sealed, immutable version with a digest. Because any deployment can mount that version by its digest, every replica serves the exact same bytes, updates upload only what changed, and deployments start without a download step.

All you need to do is reference that digest in your `config.yaml`.

yaml

```yaml
bdn:
  mounts:
    - source: <version-ref>
      path: /mnt/base-weights
```
When a replica starts, BDN makes the sealed volume available as a read-only mount, and the model reads its base weights from that mount. Cold starts and scale-ups no longer depend on downloading those weights from the original S3 bucket. We built BDN to [make cold starts faster and more reliable](https://www.baseten.co/blog/how-the-baseten-delivery-network-bdn-makes-cold-starts-fast/), but its design also reduces external dependencies and runtime egress while preserving the model's access to weights.

That leaves adapter retrieval as a separate runtime dependency, with its own access policy.

When a request requires an adapter that’s not already loaded or cached, the model needs to fetch it from the adapter bucket (S3 in this example). [Runtime OIDC](https://docs.baseten.co/organization/oidc#use-oidc-at-runtime) makes a short-lived Baseten token available inside the serving container. Your model code uses it to get temporary cloud credentials, and Baseten automatically refreshes the mounted OIDC token.

```yaml
runtime:
  oidc:
    enabled: true
```
In AWS, the model exchanges that token through AWS Security Token Service (STS) for credentials to assume an IAM role. Your model code handles adapter selection, downloading, and loading.

python

```python
import os
import boto3
class Model:
    def load(self):
        os.environ["AWS_WEB_IDENTITY_TOKEN_FILE"] = os.environ["B10_OIDC_TOKEN_PATH"]
        self._s3 = boto3.client("s3")
```
Scope the role's `s3:GetObject` permission to the adapter prefix the model needs, without granting permission to modify them.

json

```json
{
  "Effect": "Allow",
  "Action": "s3:GetObject",
  "Resource": "arn:aws:s3:::<adapter-bucket>/<adapter-prefix>/*"
}
```
Build-time and runtime permissions serve different purposes. For instance, permission to retrieve base weights should not automatically carry over to the serving container. Runtime tokens always carry the `model_container` workload type, so the adapter role's trust policy can match running containers only:

```json
"Condition": {
  "StringLike": {
    "oidc.baseten.co:sub": "v=1:org=abcd1234:team=wxyz5678:*:type=model_container"
  }
}
```
Configure each identity for the work it needs to do, and enable runtime OIDC when the model needs to authenticate to an external service.

Cloud permissions define which resources the model can use. Network controls define where it can connect.

By default, deployments can make outbound requests to internet hosts on TCP ports 443 (HTTPS) and 80 (HTTP). [Egress restrictions](https://docs.baseten.co/development/model/egress-restrictions) let you narrow that access to an allow list of domains and IP ranges for each deployment.

For the adapter example, allow the S3 endpoint used to download adapters and the AWS STS endpoint used to exchange the OIDC token for temporary credentials.

```yaml
runtime:
  egress_restrictions:
    fqdn_allow_list:
      - <adapter-bucket>.s3.<region>.amazonaws.com
      - sts.<region>.amazonaws.com
```
The allow list makes those network paths explicit. Domains are enforced by IP address, though, and S3 serves many buckets from shared IPs; the IAM policy determines which adapters the model can read once it reaches S3.

If a model needs no outbound connections, set both allow lists to empty to block egress. Omitting the restrictions leaves the default behavior in place.

The configuration lives in your model's `config.yaml`, so network changes can be reviewed alongside model changes. Updating the allow lists requires a new deployment, so you can apply a restrictive policy to one sensitive workload without changing other deployments in the organization.

Together, these boundaries reduce the opportunities for a compromise to spread. A malicious dependency would have no static cloud key to steal and could connect only to the limited, allowed destinations. Short-lived tokens do not end an ongoing compromise, so narrowly scoped permissions and carefully chosen destinations remain essential.

Workload controls complement the controls your organization uses to manage the platform. Our [RBAC model](https://www.baseten.co/blog/rbac-from-the-ground-up-solving-for-autonomy-vs-control/) includes team-based access, restricted environments, and granular API keys, which govern who can manage models, change production environments, and call inference endpoints. Together, platform teams can control who changes a deployment and what that deployment can reach. Engineers can iterate on models and serve new adapters within those boundaries, while platform teams review changes to production access and network configuration.

And while these steps are critical to keeping your work secure, they must be part of a [holistic security approach](https://www.baseten.co/blog/improved-controls-for-the-new-era-of-cyberattacks/), including [securing the underlying hardware you run on](https://www.baseten.co/blog/how-we-secure-100-clusters-across-20-clouds/), API key hygiene, container and network security, observability, and more. We’ll be publishing more blogs on these topics in the coming weeks.

Most of this setup lives in your `config.yaml`: a sealed volume reference, runtime OIDC, and an egress allow list. The [volume sync](https://docs.baseten.co/development/volumes/sync), [OIDC](https://docs.baseten.co/organization/oidc), and [egress restrictions](https://docs.baseten.co/development/model/egress-restrictions) documentation provide more details on how to use each.

Stay tuned for more blogs in our security series. And if you want to talk to our engineers about any of our security controls in more detail, [reach out](https://www.baseten.co/talk-to-us/).
