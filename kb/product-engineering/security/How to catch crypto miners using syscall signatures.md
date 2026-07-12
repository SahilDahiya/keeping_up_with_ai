---
title: How to catch crypto miners using syscall signatures
topic: product-engineering
subtopic: security
secondary_topics:
- infra-platform/deployment
summary: Explains detecting abusive GPU workloads with syscall signatures, a useful
  pattern for securing shared AI infrastructure.
source: modal
url: https://modal.com/blog/catching-cryptominers
author: null
published: '2024-06-06'
fetched: '2026-07-11T04:30:17Z'
classifier: codex
taxonomy_rev: 1
words: 1528
content_sha256: 9b337667748fb25c4ff6cfe63f947595474ea1d9dbb5ee1d42bea2257407ae59
triage: keep
skip_reason: null
---

# How to catch crypto miners using syscall signatures

[Back](https://modal.com/blog)

# How to catch crypto miners using syscall signatures

[Jonathon Belotti](https://twitter.com/jonobelotti_IO)

At Modal, we built a serverless container runtime enabling users to attach up-to eight latest generation NVIDIA GPUs to a function. Such an ability, combined with an on-demand billing model, is catnip to cryptomining abusers. These cryptominers steal valid credit card information and then squat on as many GPUs as possible for as long as possible, running up Modal’s costs and keeping valuable GPUs out of the hands of legitimate, paying users.

This unhappy situation could not stand, so we added a syscall-based program analysis component into our runtime that detects and disables cryptomining Modal [Functions](https://modal.com/docs/reference/modal.Function) before banning the offending user and all their friends. This component is called `seccheck`.

![Cryptomining detection flow diagram](https://modal-cdn.com/tmpqh11nqrz_54c5fb14.png)



It’s important that our detection system is based on runtime program analysis. Twenty years ago Paul Graham observed that with email spam it is message itself, the data, that is an abuser’s Achilles heel. Spammers can steal email addresses, miners can steal credit cards. Both can change their *metadata*. But they cannot change their data. The message must scam, the program must mine.

## Metadata analysis is not enough

Modal’s earliest cryptominer detection system was created mere hours after [we became generally available](https://modal.com/blog/general-availability-and-series-a). We enjoyed maybe four seconds of elation looking at the slope of our post-GA usage graph before it dawned on us that some cryptominers had dined out and dashed.

This first system uses heuristic rules to evaluate user metadata and it still remains as the first barrier against abuse. But it’s not enough. You can define rules against every piece of metadata you like (IP address, email, Github profile), even run a credit card check [with Stripe Radar](https://stripe.com/guides/primer-on-machine-learning-for-fraud-protection). With enough motivation abusers will dress up nice and flash convincing ID. It’s often been tempting to add or tighten heuristic rules (such as the threshold for a suspiciously young Github account) but doing so will invariably drive up the false positive rate.

## Choosing a program analysis technique

If a cryptominer’s Achilles heel is their program, their data, we should analyze their program.

Unfortunately for us, a miner’s program is vastly more complicated than a scammer’s email message. Modal’s SDK is currently Python-only, but the Modal container runtime supports arbitrary x86 Linux code execution. Any detection system based on source code or binary analysis was thus ruled out as intractable.

We can also rule out container image scanning, because Modal Functions are not blocked from downloading and executing arbitrary programs at runtime. In some container environments it’s valid to mount filesystems with `noexec` or go whole-hog and make the entire container filesystem read-only, but this would be cripplingly restrictive to our users.

What we need is a runtime monitoring mechanism which is involves a relatively narrow domain, is common across all x86 programs, and can be observed with little to no runtime overhead.

For us, that mechanism is a syscall log.

## The syscall secretions of a miner

For almost everything a program wants to do, it needs to trap into the kernel. Want to read or write a file? Make the [open()](http://linux.die.net/man/2/open) syscall, and then the syscalls [read()](http://linux.die.net/man/2/read) or [write()](http://linux.die.net/man/2/write). Talk on the network? You need the syscalls [socket()](http://linux.die.net/man/2/socket), [connect()](http://linux.die.net/man/2/connect), [read()](http://linux.die.net/man/2/read), and [write()](http://linux.die.net/man/2/write). To create more processes, first [clone()](http://linux.die.net/man/2/clone) and then [execve()](http://linux.die.net/man/2/execve) so the new child process [gets its brain eaten](https://jvns.ca/blog/2016/10/04/exec-will-eat-your-brain/) and becomes a different program.

Just starting up and immediately exiting the `python3` interpreter produces over ** 1000** syscalls on my Linux machine.

Very, very few programs can do something interesting without making a telltale system call. Cryptomining programs make telltale system calls. Let’s take the Monero proof-of-work cryptocurrency and its `monerod` binary:

```
strace -tf -o crypto.trace.txt \
./monerod --zmq-pub tcp://127.0.0.1:18083 \
--add-priority-node=p2pmd.xmrvsbeast.com:18080 \
--add-priority-node=nodes.hashvault.pro:18080 \
--disable-dns-checkpoints --enable-dns-blocklist
```
The full `strace` dump is very long, but I picked out a few of its curious calls:

`stat("/home/ubuntu/.bitmonero/blockchain.bin", 0x7ffd6a0c7530) = -1`It looks up a “blockchain.bin” file alongside a bunch of other lookups against incriminating file paths.

`connect(26, {sa_family=AF_INET, sin_port=htons(18080), sin_addr=inet_addr("159.69.153.93")}, 16 <unfinished ...>`It connects on an odd port, 18080, to an IP address that is associated with the [ p2pmd.xmrvsbeast.com](http://p2pmd.xmrvsbeast.com/) mining pool. Starting to get extremely suspicious…

And it connects out to [http://anonyme-flirts.net/](http://anonyme-flirts.net/), an odd German anonymous dating site? That’s weird, but not sure if it’s cryptomining.

`connect(45, {sa_family=AF_INET, sin_port=htons(18080), sin_addr=inet_addr("49.12.127.33")}, 16 <unfinished ...>`If our cryptominer detection system happens to let an abuser through, getting `strace` data from the abuser’s process is the first step in understand how to improve the system. We don’t store container syscall logs by default because the log volume would be petabytes/day, but Modal engineers can easily gather log data ad-hoc.

## Naive syscall observation

If you already knew a thing or two about syscall observability and `strace`, you’d be horrified to think that Modal wraps every containerized process in `strace`. Don’t fret, we don’t do that!

Although it’s highly convenient, the stock `strace` executable relies on the `ptrace()` (process trace) debugging interface in which the kernel signals to stop the traced process every time it enters and exits a system call. At each stop point the tracer parent process is given opportunity to inspect and even modify the process under observation.

So when we run `strace python3 -c ""` the traced process makes ~1000 syscalls and is thus stopped ~2000 times so that the tracer parent process (`strace`) can be context-switched in to inspect the current syscall and log its details to stderr.

On syscall-heavy programs the ptrace interface is *brutal* for performance. A single context-switch takes around 10 microseconds. On even our trivial program above the performance penalty is obvious:

![strace performance benchmark](https://modal-cdn.com/strace-performance-benchmark.png)



Using our ‘napkin math’ number of 10 microseconds per context-switch we can venture that around 20 milliseconds or ~60% of the fat is pure switching overhead.

On syscall-heavy programs, such as those doing a lot of IO, a traced process’s performance can be over 100x times worse. We couldn’t even consider imposing that kind of performance hit on just our new, untrusted users. Modal must be fast from day one.

## gVisor seccheck

So how do you massively optimize syscall tracing such that it introduces little to no runtime performance penalty on Modal Functions? It’s a difficult technical problem, and fortunately one that we didn’t have to solve ourselves.

Modal’s default container runtime uses gVisor, a application sandbox that provides greatly increased host security over the popular runC container runtime. Perhaps the core security feature of gVisor is application syscall isolation. A sandboxed container running in gVisor cannot directly make syscalls against the host and instead has them intercepted and fulfilled by gVisor’s “sentry” application kernel. The Google gVisor team has done a lot of work to [greatly reduce syscall overhead](https://gvisor.dev/docs/architecture_guide/performance/#system-calls) to a point where it is performance competitive enough to use as Modal’s default container runtime.

With all the fast syscall interception machinery already built into gVisor, it became relatively simple to pump syscall trace data out a socket for consumption by our `seccheck` component.

![Diagram of gVisor syscall interception](https://modal-cdn.com/tmpdjzn4d8i_09f3aae2.png)



How it works is that on container creation Modal’s runtime creates a dedicated socket to receive all runtime syscall trace data from gVisor. A thread is spawned and runs for the lifetime of the container, receiving and analyzing syscall events (a.k.a “tracepoints”) against all implemented analysis “rules”.

```
let listener = uds::tokio::UnixSeqpacketListener::from_nonblocking(listener)?;
let mut socket = TracepointSocket::new(listener).await?;
while let Some(tracepoint) = socket.next_tracepoint().await? {
    for rule in &rules {
        if let Some(sec_event) = rule.analyze(&tracepoint) {
            task_tx
                .send_async(TaskMessage::SecurityEvent(sec_event))
                .await?;
        }
    }
}
```
Though we have the option to analyze any of the over 300 Linux syscalls, in practice we can pick out cryptominers with just a handful. For example, because Modal is a Python-native cloud, a user Function creating a new non-Python subprocess is particularly interesting. We look at all `execve` syscalls, which have an event body like this:

```
message Execve {
  gvisor.common.ContextData context_data = 1;
  Exit exit = 2;
  uint64 sysno = 3;
  int64 fd = 4;
  string fd_path = 5;
  string pathname = 6;
  repeated string argv = 7;
  repeated string envv = 8;
  uint32 flags = 9;
}
```
If a Function’s `execve` matches one of our rules the `seccheck` component emits a `TaskMessage::SecurityEvent` protobuf event which ends up being received by our servers. These servers crucially can associate the suspicious container with a workspace and user and make a decision on auto-banning. A flagged container is always immediately killed.

We’ve started conservatively with our rules and so far there’s been zero false positives.

## Next steps

Introducing syscall-based application runtime has been a big step up in Modal’s cryptominer abuse defenses. We expect that straightforward evolution of our analysis ruleset should keep pace with an increase in the diversity and deviousness of cryptomining abusers.

If need be, we can introduce memory into our analyzer so that it may pattern match across multiple syscalls. We can also begin automatically updating our blacklists of bad binaries and bad IPs. Even more fun, we can write rules that match against NVIDIA control commands made to GPU devices!

Whatever is necessary to keep our users happy and our cryptomining abusers mad, we’ll do it.

![Cryptominer gets upset](https://modal-cdn.com/username-fuckyoumodalfuckk.png)
