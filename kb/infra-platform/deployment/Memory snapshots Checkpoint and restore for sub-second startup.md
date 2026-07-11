---
title: 'Memory snapshots: Checkpoint and restore for sub-second startup'
topic: infra-platform
subtopic: deployment
secondary_topics:
- inference/optimization
summary: Explains memory snapshots as checkpoint/restore infrastructure for faster
  startup in serverless AI workloads.
source: modal
url: https://modal.com/blog/mem-snapshots
author: null
published: '2025-01-28'
fetched: '2026-07-11T04:29:19Z'
classifier: codex
taxonomy_rev: 1
words: 2079
content_sha256: 0d96fa27de1ca8add19333adab35d912f749afb3b361921a13dab2b88c018b4c
triage: keep
skip_reason: null
---

# Memory snapshots: Checkpoint and restore for sub-second startup

[Back](https://modal.com/blog)

# Memory snapshots: Checkpoint and restore for sub-second startup

[Jonathon Belotti](https://twitter.com/jonobelotti_IO)

Modal is a serverless GPU container runtime designed to scale from zero. We run our worker fleet and our users’ Functions lean. If there’s idle capacity we aim to cut it. This means that if additional load comes into a Function, we often need additional containers to start up and serve requests. Cold start latency occurs when a request is waiting for a container to start up, and our customers hate it.

We hate it too! Thankfully, with the introduction of *memory snapshot* restores, cold start latency on user Functions can be more than halved!

### import torch (eCDF)

## What’s a memory snapshot?

A Modal memory snapshot is a couple of files that represent the entire state of a Linux container *right before* it was about to accept a request. We capture the container’s filesystem mutations and its entire process tree. Each process in that tree has state consisting of its memory mappings, file descriptor table, registers, environment variables, process ID, and more! It’s a party and everyone’s invited.

![Diagram of process component state that is saved to disk (credit Tristan Hume)](https://modal-cdn.com/cdnbot/modal-snapshot-process-diagramtq1ww54b_99ced4b9.webp)



All that captured state allows for the complete restore of a Python program, with the notable exception of live network connections and NVIDIA GPU state (discussed below).

Container snapshotting functionality is an outgrowth of the the ‘checkpoint/restore in userspace’ (CRIU) kernel technology. The gist is that you can checkpoint (save) a Linux container and restore it at a later time, even on a different computer. This functionality had existed for Linux *VMs* since at least 1999’s VMWare Workstation product, but as we know containers weren’t ‘a thing’ until around 2009. CRIU was first presented in 2011 by some [“mad Russians”](https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/commit/?id=099469502f62fbe0d7e4f0b83a2f22538367f734) as a method for live migration of containers between physical servers, and has over time proved itself a [handy technique](https://ipads.se.sjtu.edu.cn/_media/publications/catalyzer-asplos20.pdf) for reducing serverless cold starts.

CRIU is developed for the `runc` container runtime, but for security reasons Modal uses the gVisor container runtime `runsc` (short for “run Sandboxed Container”). While `runc` has containers run on the host kernel, gVisor implements a userspace kernel and gives the guest container access to that. This has obvious implications for container snapshotting. While a `runc` snapshotting solution cooperates with the host Linux kernel to save container state—the kernel exposes, via /proc VFS, details about a process’s memory maps, open files, children processes— gVisor controls the userspace kernel serving a snapshotted container guest.

![Timeline showing when Linux, LXC, CRIU, and gVisor were released](https://modal-cdn.com/cdnbot/mem-snapshots-blog-post-289iuooft_6e5a069b.webp)



So while gVisor’s checkpoint/restore functionality was developed many years after CRIU, it’s actually quite like pre-CRIU solutions which involved customizing the Linux kernel (ie. ‘container restore in kernelspace’). gVisor’s core `kernel.go` file contains checkpoint/restore code and at least eighteen system components implement checkpoint/restore functionality in `save_restore.go` files. You can make a lot of checkpoint/restore specific kernel customizations if you reimplement the Linux kernel in userspace!

## Performance: Checkpoint/restore vs. lazy loading

It’s not obvious why restoring a container snapshot with gVisor’s `runsc restore` would be so much faster than a standard `runsc run` container startup.

The main reason is that Python’s import system is filesystem-based and needs to execute thousands of slow, sequential filesystem operations in order to become ready to perform useful work.

It’s *thousands* because even just importing `torch` in Python executes 26,000 syscalls! It’s slow because there’s a couple layers of indirection between the container’s filesystem and the actual file data. A Modal container filesystem is an [OverlayFS](https://en.wikipedia.org/wiki/OverlayFS) filesystem where the read-only lower is a FUSE-based lazy loading file server, which means that every file read incurs some overhead.

```
overlay on /mnt/overlay type overlay (
    rw, relaltime,
    upperdir=/tmp/tmph45cav46/upper,
    lowerdir=/tmp/tmph45cav46/imagefs_fuse,  << lazy-loading file server
    workdir=/tmp/tmph45cav46/work
)
```
The fastest code is the code that never runs, and so fast container startup is mostly about laziness, work avoidance. Basically, not doing work where it’s not needed. Almost every container on Modal has thousands of files in `/usr/share/doc`, but ~zero of our users’ programs actually need to read those files. So we don’t load them.

For more detail on our lazy-loading container filesystem, see [Fast, lazy container loading in Modal.com](https://modal.com/blog/jono-containers-talk).

Despite cutting out heaps of eager file I/O with lazy loading, importing `torch` still executes 26,000 syscalls, context switching between the caller, the kernel, and the FUSE server. Python’s filesystem-based, syscall heavy module loading is just too slow. So we turn to checkpoint/restore, which turns thousands of syscalls into (roughly) a single file load, recreating the process’s memory mappings directly rather than re-running through the Python import system and all other application code executed during container startup.

## A single file load?

![Diagram showing the simplified restore problem, where Python process memory mappings are served from FUSE via gVisor.](https://modal-cdn.com/cdnbot/mem-snapshots-blog-post-4hth1rar3_a5e507bd.webp)



The container restore process is a frenetic process of summoning and ensemble choreography, but most of the performance is won or lost on how fast the ‘main’ process’s memory mappings can be brought into the operating system’s page cache. These memory mappings are typically 100MiB-10GiB and stored in a single snapshot ‘pages’ file, referring to the 4KiB page (or huge pages) of the virtual memory system.

When restoring, gVisor does not need to wait to read the entire ‘state’ file into memory before allowing the restored container to progress. Instead it can read the restored processes’ pages [in the background](https://github.com/google/gvisor/commit/41f01d8f9c5aee4f7a31ec6183fb50bbc6f9b851), prioritizing those pages which a restored process blocks on.

This background-loaded pages file is made available to gVisor through the same distributed, FUSE-based file serving system used for our standard container loading. To ensure the FUSE system doesn’t keep gVisor waiting when it requests a page, we aggressively preload the entire pages file into page cache as early as we can. In the worst case, the restoring process page faults and gVisor finds that the FUSE file server doesn’t already have the page in-memory, nor is the page on host disk. Thus, the restoring process is blocked waiting for the FUSE server to complete a networked file read, which takes 10s of milliseconds.

Much has been ignored by focusing only on the pages file’s loading, but it’s here the 80 in the 80/20 rule. gVisor’s prioritized, background page loading and our FUSE filesystem’s aggressive preloading cooperate to minimize aggregate page fault latency in a restoring guest process.

Now, is all this fast enough?

## Performance: 2.5x faster

We’ve found that memory snapshot restore is about 2.5x faster than a standard container startup. A Stable Diffusion inference Function that takes around 13 seconds normally restores in *only 3.5 seconds*. A simple `import torch` example program which was noted as executing 26,000 syscalls takes normally around 5 seconds to cold start. With snapshot restore it’s around 1.05 seconds at p50 and 0.69 seconds at p0!

### import torch

### Stable Diffusion

While restore is already much, much faster than the status quo, we can make it better. The current restore implementation is performance-constrained by how fast the virtual memory of the main process, sometimes GiBs of data, can be loaded off disk (or over the network) and into memory.

We’re observing container restore incurring CPU pressure as it eagerly loads hundreds of thousands of 4KiB pages. [CPU stalling](https://dx13.co.uk/articles/2023/07/27/cpu-stalls/) is going as high as 900/ms/s, indicating our container cgroup resource management needs better tuning for aggressive resource usage at startup. This is not exactly as bad as leaving the handbrake on, but kind of like straining to get a fixie bike going uphill.

We also could optimize how we preload the guest’s virtual memory pages into the host page cache. Sometimes restore files are served over the network, and while we expect our hosts to drive around 2GiB/s of network download, in the tail we’re observing much less effective throughput.

So there’s still work to be done, and you should expect the restore line above to move more to the left and get straighter as we make optimizations!

## Under the hood: snapshot lifecycle

Deployed Functions with memory snapshots enabled only get snapshotted on-demand, not proactively. Also, a single deployed Function version will get snapshotted *multiple times*, for an interesting reason.

Snapshots are created on-demand when Modal’s scheduler finds that it does not have an existing active Function snapshot available for the Modal worker host onto which it intends to place that Function.

```
snapshot_info: Optional[api_pb2.SnapshotInfo] = None
if function_proto.checkpointing_enabled:
    snapshot_info = await get_or_create_checkpoint_for_worker_and_task(
        state, ephemeral_function_struct, worker_ephemeral_struct, task_id
    )
```
Having to match a Function snapshot with a particular worker is one of the reasons a single Function version will be snapshotted multiple times. For example, the AWS g6.12xlarge instance type does not support the `pclmulqdq` [Perform a Carry-Less Multiplication of Quadword](http://en.wikipedia.org/wiki/CLMUL_instruction_set) instruction and so it cannot accept any snapshot created on a host which does. Our users didn’t sign up expecting to debug Invalid Opcode exceptions!

Beyond CPU featureset compatibility concerns, memory snapshots are also sensitive to changes in NVIDIA driver version and container runtime version. Such compatibility concerns are the major reason that Modal controls the snapshot lifecycle on behalf of users, ensuring that restores consistently succeed across a dynamic and evolving worker fleet.

## Tradeoffs: or, is it really that simple?

Memory snapshots significantly reduce cold starts but they also decrease simplicity. Andrew Morton [tried to warn us](https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/commit/?id=099469502f62fbe0d7e4f0b83a2f22538367f734), but we’ve sided with the Russians and gone a bit mad. We’re freezing containers mid-execution and serializing them to disk.

The main chore ‘checkpoint/restore in userspace’ tends to require is cooperation from the guest program. Programs need to understand that they will be paused for an indefinite amount of time and resumed on a different computer, possibly with a different IP address. They also need to understand that the state they establish prior to snapshotting will be *reused* over and over again—expectations of entropy may be violated.

The team has already worked hard to make the Modal [client](https://github.com/modal-labs/modal-client) cooperative with checkpoint/restore. When tricky cases cause restore to fail (and this does happen) we automatically fallback to a standard container startup. We recommend testing outside of production before deploying a Function to production with memory snapshots enabled.

For more information on managing sharp edges, see the [guide page](https://modal.com/docs/guide/memory-snapshots).

## Interface: adopting memory snapshot speedups

Ok, so how do you use it?

Modal Functions can turn on snapshotting using the `enable_memory_snapshot=True` argument and [lifecycle methods](https://modal.com/docs/guide/lifecycle-functions#container-lifecycle-hooks) can opt-in to snapshotting using the `snap=True` argument.

Here’s a ‘hello world’ example that just imports `torch`.

```
import pathlib
import modal
image = modal.Image.debian_slim().pip_install("torch")
app = modal.App(name="demo-memory-snapshot")
pathlib.Path("./foo").write_text("disk mutation")
with image.imports():
    import torch  # 26k syscalls comin' right up!
@app.function(enable_memory_snapshot=True)
def f(x: int):
    print(f"Hello from torch {torch.__version__}. You gave me {x=}")
```
The above Modal Function `f` will be snapshotted once it has deployed and run a handful of times in production. (We currently create snapshots on-demand, not proactively.)

The snapshot has captured the `import torch` global import as well as anything else that executed in global scope, such as the rootfs disk mutation. It has essentially paused and saved *right before* it’s about to fetch a request and feed that request into `f`.

This allows us to jump straight back into `f(x)` on restore, as shown below.

![Diagram showing the snapshot restore process](https://modal-cdn.com/cdnbot/mem-snapshots-blog-post-5-ay7ar0i9_c042c9d0.webp)



Whenever Modal detects that a redeploy has invalidated an existing snapshot of `f`, new snapshots are created.

### Handling GPU state

It was said above that lifecycle functions can be snapshotted, and this is important for managing GPU state. Because memory snapshots do not yet support saving GPU state to file, GPU state must be created post-restore.

```
import time
import modal
image = (
    modal.Image.debian_slim()
    .pip_install(
        "transformers", "torch", "accelerate", "safetensors",
    )
)
app = modal.App("snap-demo", image=image)
@app.cls(gpu="a10g", enable_memory_snapshot=True)
class GPT2:
    @modal.enter(snap=True)
    def load(self):
        from transformers import AutoModelForCausalLM, AutoTokenizer
        self.model = AutoModelForCausalLM.from_pretrained("/root/cache", use_cache=True)
        self.tokenizer = AutoTokenizer.from_pretrained("gpt2", use_fast=True, use_cache=True)
    @modal.enter(snap=False)
    def setup(self):
        self.model.to("cuda")
    @modal.method()
    def run(self) -> str:
        input_ids = self.tokenizer.encode("What's up?", return_tensors="pt")
        out = self.model.generate(
            input_ids.to("cuda"),
            pad_token_id=self.tokenizer.eos_token_id
        )
        generated_text = self.tokenizer.decode(out[0], skip_special_tokens=True)
        return generated_text
```
The above GPT-2 inference Function has a `snap=True` lifecycle method which setups the model in CPU RAM for snapshotting, and a `snap=False` lifecycle method to move from CPU RAM to GPU vRAM right after restore.

This demo inference Function restores 2.5x faster using memory snapshots 🏎️.

## Acknowledgements

Many thanks to the [gVisor team](https://github.com/google/gvisor) for creating gVisor and its [Checkpoint/Restore](https://gvisor.dev/docs/user_guide/checkpoint_restore/) functionality. Thanks also to Luis Capelo, Colin Weld, and Matt Nappo for their work and design discussions related to memory snapshots.

If you’re interested in building fast, reliable, and heavy-duty systems for the cloud, [Modal is hiring](https://modal.com/company).
