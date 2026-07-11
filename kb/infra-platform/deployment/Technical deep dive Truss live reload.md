---
title: 'Technical deep dive: Truss live reload'
topic: infra-platform
subtopic: deployment
secondary_topics:
- product-engineering/architecture
summary: Technical deep dive into Truss live reload and faster model-server development
  loops.
source: baseten
url: https://www.baseten.co/blog/technical-deep-dive-truss-live-reload/
author: Pankaj Gupta
published: '2023-02-17'
fetched: '2026-07-11T04:11:16Z'
classifier: codex
taxonomy_rev: 1
words: 1964
content_sha256: d845ee8451b92c304f280dfe4937e308ed62481499e70d95fbec4a8450bdddc1
triage: keep
skip_reason: null
---

# Technical deep dive: Truss live reload

![Live reload](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1747614388-truss-live.png%3Fauto%3Dformat%26fit%3Dcrop%26h%3D630%26w%3D1200&w=3840&q=100)

[Truss](https://truss.baseten.co/) is an open-source model packaging format designed to improve the developer experience for serving ML models. Serving a model requires iterative development, just like any other complex coding task.

Truss’ key feature for iterative development is [live reload](https://truss.baseten.co/usage). Without live reload, the upload-build-deploy loop for publishing models to production can take anywhere from 3 to 30 minutes. With live reload, it’s practically instantaneous.

[You can learn more about using live reload here](https://www.baseten.co/blog/100x-faster-dev-loops-with-draft-models/). In this post, we describe the technical design and implementation challenges of this feature.

## Design and Operational Requirements

As we set out to implement the live reload mechanism in Truss, we had the following requirements in mind:

- **Simplicity of use**: Don’t change the user’s model deployment flow; just make it orders of magnitude faster.
- **Persistence**: Changes made to the model service should stick, even if the model pod restarts.
- **Identical behavior to published production models**: Users can develop and test their models with live reload and then publish a performance-optimized version. Both of these should support the exact same prediction interface.
- **Self-sufficient**: Live reload should not have direct knowledge of external services, only abstractions.
- **No increase in model build time:**Make these changes without slowing down key steps- **.**
- **Allow recovery from mistakes**: Development is messy; some changes will not work. Malformed code, missing Python requirements, crashing code, it’s all possible. Allow inline recovery without requiring a full deployment.
- **Robust and consistent**: Resilience to any race conditions. The running model service should always accurately represent the Truss.
- **Composition**: Live reload logic to be completely isolated from the inference server. Decoupling via composition keeps the complexity low and has numerous other advantages.

## Architecture

Live reload on a Truss is beneficial both for local development as well as on deployed environments such as Baseten. We describe both here.

### Live reload on local Docker

Live reload is very useful for testing your models locally using Docker. Any changes to the Truss can be applied directly to the model running on the Docker container, bypassing the need to build a new image and spin up a new container. The loop can be so quick that it can feel like you’re developing directly on the Docker container. Here is how it works.

### Control Proxy

A regular running Truss looks like this:

![A regular running Truss looks](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1692709951-63eeaffec2156fa37d2a0636_d2scvyjka_xum9uixqkxrc8g2wkch1lygh67q2r-8iykllxxpyunnvgd3ehqizxy99mysbg80ccoz1w17h1ahohu60dizynhd7n8yodk8bpvgz0clfvcik1wowudnrnfpzw5vkyh60nr3nci2fqitx0.png%3Fauto%3Dformat%26w%3D1200&w=3840&q=75) A regular running Truss looks

A regular running Truss looksFor live-reloadable Truss, we add a proxy server in front. This proxy passes through prediction requests to the underlying inference server and supports applying patches. Let’s call this proxy server the *Control Proxy*. The Control Proxy code is completely separate from the inference server code, runs as a separate process on the container, and even uses a separate virtual Python environment to not interfere with the Python requirements specified in the Truss.

![Truss live-reloading architecture diagram](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1692709989-63eeaffe1fefb7ff040276e5_xo-r6rhqymu3jun9astwecejfrmtpd-z3qoqsg2pi0mhifnmmndqyb7escrmx0yfmnes5npwtrfscwy_lh4zcw_d02ge4yjatv0itol6xo5juqzqcf3jiqabatqsmxeav_zwa8yfr_enz_0_ubztndw.png%3Fauto%3Dformat%26w%3D1200&w=3840&q=75) Truss live-reloading architecture diagram

Truss live-reloading architecture diagramAll the code and packages needed to run the Control proxy are bundled into base Docker images, so there’s no build-time penalty. Image size increases slightly, but we expect to reduce that difference to be insignificant very soon.

### Patch computation and application

For computing a patch, we need to compare the Truss to a previous state. To avoid depending on an external versioning system, the Truss library uses a lightweight tracking mechanism. Every time a model is run on Docker via Truss, it stashes away two pieces of metadata about the state of Truss, content hash, and content signature. Content hash is just a SHA256 hash of the contents of the Truss directory.

### Truss Signature

A Truss signature consists of the minimum information needed to calculate the patch. Essentially, it consists of the Truss config file and the content hash of every file in the Truss directory. This allows detecting exact changes to the config file and the addition/deletion/modification of other files.

This design is optimized for reducing the size of the signature; typically, these signatures are just a few kilobytes. This allows easily storing these signatures locally on a disk or on a server. The trade-off is that patches are bigger; entire files must be supplied in the patch. But only a few files are typically touched in an individual patch, so patches are still small overall.

### Patch application

Whenever a Truss is run on a Docker container, the Docker container is labeled with the Truss content hash (we’ll just call it hash from now on). Patch application then goes like this:

- Read the hash of the running Truss from the container label
- Retrieve the signature corresponding to this hash from the local storage
- Prepare the patch using the current Truss and the signature
- Apply the patch to the running Truss by calling the patch endpoint of the Control Proxy

The Control Proxy always keeps track of the current hash. When the container on the pod is first created, it starts out with the initial hash. Afterward, whenever a patch is applied, the new hash is tracked. The Control Proxy only accepts the patch if the currently running hash matches the previous hash in the patch request. This `check-and-set mechanism` guards against race conditions and mistakes and provides consistency.

*Check-and-set, also called test-and-set, (compare-and-swap or CAS is a very similar idea), is a foundational concept of concurrency control. Most concurrency control mechanisms boil down to check-and-set at some level. Microprocessors even have instructions for them *[https://en.wikipedia.org/wiki/Test_and_test-and-set](https://en.wikipedia.org/wiki/Test_and_test-and-set).

## Live Reload on Baseten

While live reload is useful on local Docker, its real value lies in improving iteration speed on remotely deployed models, e.g., on Baseten.

![Client -> Baseten API Server -> Draft Model Prod](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1692710070-63eeaffe6af6283d773f1eca_3k1m52q9dvqpwithuqchswgukhw7_h6zh-rmc4sn1ppsntey4svepbrptp8z4jrckfv-wudlpnp-qa2yt0_atlx6tkesjvci5xlup_qqi4azshhfaxv3uixl2ese24jqen4fapmsfe-mdb6529mr_g.png%3Fauto%3Dformat%26w%3D1200&w=3840&q=75) Client -> Baseten API Server -> Draft Model Prod

Client -> Baseten API Server -> Draft Model ProdIt again boils down to patch computation and application, but Baseten Api Server does much of the management.

### Initial deployment

It starts with a full deployment.

```
cd path/to/my/truss
truss push
```
The CLI uploads the entire Truss to the Baseten Api Server, which builds the Docker image and spins up the development deployment Pod. The Baseten API Server takes note of the content hash and the signature of the model thus deployed. The development deployment pod, thus started, runs the Control Proxy and Inference server, just like on local Docker.

*Currently, development deployments on Baseten only support a single pod, sufficient for developing and testing the model service, but the design would work for multiple pods too.*

### Patch Application

A user can change the Truss and use the CLI to deploy again, using exactly the same command as before:

`truss push`This could be from a different machine; live reload would still work.

The CLI does the following:

- Compares hashes for the local and the deployed Truss
- Downloads the signature of the deployed Truss.
- Prepares patch using this signature and the local Truss
- Calls the Baseten Api Server in a check-and-set fashion, with the previous hash, new hash, and the patch.

Baseten Api Server applies the patch on the development deployment pod:

- Accepts the patch from the client and stores it in a persistent queue.
- Syncs the patch to the development deployment pod.

![Baseten patch queue](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1692710145-63eeaffef5ec3d366ecf927b_qvyx2twqly9oig3kg_lwnoyr1pdqgolewgabt3adqubmondnkygj2og-uj4ewrdpnglr6nfrzdwrhzo47ujjj_zskyppcyxmns6xnqsfhbopducvvefsqkamz3nvpbm7t2zv0qkgga1ywhhulprcd4c.png%3Fauto%3Dformat%26w%3D1200&w=3840&q=75) Baseten patch queue

Baseten patch queueThe patch queue is not expected to have a lot of traffic or data, so is easily emulated using a Postgres table. It’s effectively a linked list where the hashes are the pointers.

The sync process:

- Retrieve the currently running hash on the development deployment pod.
- From the patch queue, retrieve all the patches beyond this hash.
- Compact these patches. E.g. deletions cancel additions.
- Hit the patch endpoint of the development deployment pod, supplying: the compacted patch, the original hash, and the new hash.
 The check-and-set again guards against race conditions, ensuring consistency.

Compaction, in step 3, is necessary to be able to recover from a bad patch. Say, a Python requirement is mistyped, and the patch fails. If the patches were simply played in order, then this bad patch would always fail, and we’ll get stuck at it. Compaction allows countering the bad change. In this case, correcting the Python requirement will effectively counter the previous mistype so that the mistake never has to play out. Additionally, compaction reduces work to be done, and thus latency, at container restart.

The Control Proxy on the development deployment pod accepts the patch in the following manner:

- Receives the patch, holding off on responding just yet.
- Stops the inference server
- Applies the individual parts of the patch in a meaningful order.
 System packages are installed before Python packages, which are installed before code changes, to follow the order of need.
- Brings inference server back up – on successful patch application
- Responds to the patch request with success.

### Recovery from patch failure

Patches may fail. For example, a system package may fail to install because it needs other system packages to be installed first. Usually, the user can read the logs to know the problems and make changes to the Truss to fix them. The application of these fixes will be very quick due to live reload. There are some cases where recovery is currently not possible. In such cases, the Control Proxy indicates the need for a full deployment, which then follows. Consistency trumps speed in this case. A future improvement would be to make the patch application process fully transactional.

### Maintaining patched state on pod restart

Baseten development deployments support scaling to zero when there’s no traffic. This important feature allows users to freely use the development deployments without worrying about wasting resources when they’re not in use. Pods may restart for other reasons too, such as Kubernetes node failure. It’s important for the development deployment pod to restore to the last patched state upon restart before serving any prediction requests. This is achieved through a patch-ping mechanism.

### Patch ping mechanism

If a ping URL is configured, the live reload capable Truss always hits it on startup and asks for patches. In the case of Baseten development deployments, this URL is configured to be an endpoint on the Baseten Api Server. At startup, the Control Proxy calls this endpoint with its current hash. If there are no outstanding changes, BasetenApiServer responds as such, and the Control Proxy starts up the inference server immediately. Otherwise, Baseten Api Server indicates acceptance, and the Control Proxy waits for patch. Baseten Api Server then starts the patch sync process. The Inference server is only started once this sync succeeds.

Note that the running Truss model is not directly aware of the Baseten Api Server; it just calls a configured endpoint. A JWT token is used for auth between the Model container and the Baseten Api Server.

![Baseten Patch Ping mechanism](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1692710198-63eeaffea8e2757deacfdbc0_1kwpqpu6crob0xde6fassh7nas57mgs8ns5nhjssnnmhzynqgja9zyt0gaj0vtnesbmcf5mt3wjpnrxexyelnxbso6_8ox46sdwq8siocfws0mwihde3rssgonvjil_5hwahn24pi_e-snyfaawhkzy.png%3Fauto%3Dformat%26w%3D1200&w=3840&q=75) Baseten Patch Ping mechanism

Baseten Patch Ping mechanism## Epilogue

Truss exists to speed up and ease the process of turning raw machine-learning models into production-grade services. Quick iteration cycles make that development process faster and easier. Implementing live reload required balancing numerous requirements, making multiple tradeoffs, and overcoming several issues. The design we presented here is the outcome of that effort. We hope you had fun learning about it.

Live reload is a new feature, and many big improvements are yet to come.

- We truly appreciate your feedback, suggestions, and contributions about live reload or any other Truss feature. - [Open an issue](https://github.com/basetenlabs/truss/issues)to get in touch!
- If you want to use Truss to package and deploy your own models, follow - [Baseten’s model deployment guide](https://truss.baseten.co/quickstart)to get started!
- If you want to keep an eye out for upcoming improvements to Truss, - [star the repository](https://github.com/basetenlabs/truss)to stay in the loop.
