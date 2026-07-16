---
title: Zero Code Instrumentation with eBPF and Logfire
kind: blog
topic: evals-observability
subtopic: tracing
secondary_topics:
- infra-platform/deployment
summary: Instrumenting services that can't take an OpenTelemetry SDK—legacy apps,
  compiled binaries, third-party containers—using the OpenTelemetry eBPF instrumentation
  agent to emit traces to Logfire with zero code changes.
triage: null
skip_reason: null
source: pydantic
url: https://pydantic.dev/articles/zero-code-instrumentation-ebpf-logfire
author: Nicola Martino
published: '2026-02-10'
fetched: '2026-07-16T23:01:36Z'
classifier: claude
taxonomy_rev: 2
words: 1358
content_sha256: 4aeaf0c769a1e3481eb6d6497a8768b42c8c84d708a8613a8f02364208b4e8bf
---

# Zero Code Instrumentation with eBPF and Logfire

Not every application can be instrumented with an OpenTelemetry SDK.

Legacy services, compiled binaries, third-party containers, or services where code changes are not feasible still require observability.

The [OpenTelemetry eBPF Instrumentation](https://opentelemetry.io/docs/zero-code/obi/) tool provides a solution by instrumenting applications at the kernel level without modifying application code.

This produces OpenTelemetry-compatible traces and metrics that can be exported to Logfire or any OTLP-compatible backend.

This guide demonstrates how to configure eBPF instrumentation using docker-compose, including service discovery, endpoint filtering, and export configuration.


- **The Problem:**You need observability for applications where code changes are not feasible—legacy services, compiled binaries, third-party containers.
- **The Solution:**eBPF instruments at the kernel level. No SDK installation, no code changes, no recompilation required.
- **What You Get:**HTTP traces with method, path, status code, and latency. RED metrics (Rate, Errors, Duration) automatically generated.
- **Limitations:**eBPF captures network-level data but cannot access application-specific context (user IDs, custom attributes, business logic).
- **Requirements:**Linux kernel 4.14+ (5.8+ recommended). A container with the appropriate Linux capabilities is required.


eBPF Instrumentation allows programs to run in the Linux kernel without modifying kernel source code or loading kernel modules.

For observability purposes, eBPF probes attach to kernel functions and user-space application symbols. When an application makes an HTTP request or receives a response, eBPF captures:

- Request method, path, and headers
- Response status code and size
- Request start time, end time, and duration
- Source and destination network information

This data is assembled into OpenTelemetry spans and exported without any SDK in the application.

The instrumentation runs in a separate container with elevated privileges to access kernel functions.


eBPF is appropriate when:

- You cannot modify application code (compiled binaries, vendor-provided containers)
- You need immediate instrumentation during incident response
- The application uses standard HTTP/HTTPS/gRPC protocols
- Infrastructure-level visibility (request rates, latencies, error rates) is sufficient

eBPF is not appropriate when:

- You need application-specific context (user IDs, transaction IDs, business metadata)
- You require detailed error messages with stack traces
- The environment does not allow privileged containers

For applications where you control the code and need detailed context, use SDK instrumentation.

For quick visibility into traffic patterns without code changes, eBPF is an useful tool.


Here is a minimal docker-compose configuration that instruments a Go HTTP service:

```
services:
  echo:
    image: hashicorp/http-echo
    ports:
      - '5678:5678'
  obi:
    image: docker.io/otel/ebpf-instrument:v0.4.1
    pid: 'host'
    privileged: true
    environment:
      OTEL_EBPF_OPEN_PORT: 5678
      OTEL_EXPORTER_OTLP_TRACES_ENDPOINT: "https://logfire-us.pydantic.dev/v1/traces"
      OTEL_EXPORTER_OTLP_METRICS_ENDPOINT: "https://logfire-us.pydantic.dev/v1/metrics"
      OTEL_EXPORTER_OTLP_HEADERS: "Authorization=<your-logfire-token>"
```
This configuration:

- Runs an HTTP echo server on port 5678
- Starts the eBPF instrumentation container with host PID namespace access
- Discovers the service by listening port (`OTEL_EBPF_OPEN_PORT: 5678`)
- Exports traces and metrics to Logfire via OTLP

To run:

```
# Replace <your-logfire-token> with your actual token
docker-compose up -d
# Generate traffic
curl http://localhost:5678
```
View traces in Logfire dashboard:


The eBPF instrumentation container must identify which processes to instrument. Multiple discovery methods are supported.


The most straightforward method is to specify the port your service listens on:

```
environment:
  OTEL_EBPF_OPEN_PORT: 5678
```
This instruments any process listening on port 5678. For multiple services:

```
environment:
  OTEL_EBPF_OPEN_PORT: "5678,8080,9000"
```
You can also use the config file:

```
discovery:
  instrument:
    - open_ports: 5678,8000-899
```

If you know the process executable path:

```
discovery:
  instrument:
    - exe_path: /app/my-app
```
This matches processes where the executable is named `my-app`. Useful when multiple services run on different ports but only specific executables should be instrumented.


For targeting only processes running in an OCI container:

```
discovery:
  instrument:
    - containers_only: true
```

Available discovery methods can be combined and the target process will be instrumented only if it matches all the selectors:

```
environment:
  instrument:
    - open_ports: 5678,8000-899
    - containers_only: true
```

For production services, filtering endpoints is critical to reduce noise and control data volume.

Health checks, metrics endpoints, and other high-frequency, low-value routes should typically be excluded from tracing.


Sampling can be configured directly with OpenTelemetry eBPF Instrumentation:

```
environment:
  OTEL_TRACES_SAMPLER: 'traceidratio'
  OTEL_TRACES_SAMPLER_ARG: '0.1' # 10%
```

The [OpenTelemetry Collector](https://opentelemetry.io/docs/collector/) provides robust mechanisms for filtering spans based on HTTP attributes such as path or target.

#### Excluding Specific Routes

The example below drops spans for `/health` and `/metrics` endpoints before they are exported to Logfire.

```
processors:
  filter/drop-low-value-routes:
    traces:
      exclude:
        match_type: regexp
        attributes:
          - key: http.target
            value: ^/health|^/metrics
service:
  pipelines:
    traces:
      receivers: [otlp]
      processors: [filter/drop-low-value-routes]
      exporters: [otlp]
```
With this configuration:

- Requests to `/health`do not reach Logfire
- Requests to `/metrics`do not reach Logfire
- All other requests are exported normally

#### Filtering Using Exact Matches

To drop only exact paths:

```
processors:
  filter/drop-health:
    traces:
      exclude:
        match_type: strict
        attributes:
          - key: http.target
            value: /health
```
#### Filtering Using wildcards or Prefixes

To drop all routes under a prefix:

```
processors:
  filter/drop-internal:
    traces:
      exclude:
        match_type: regexp
        attributes:
          - key: http.target
            value: ^/(health|metrics|ready)
```


To verify the instrumentation is capturing traffic before it reaches Logfire:

```
environment:
  OTEL_EBPF_TRACE_PRINTER: text
```
This prints captured spans to the container logs:

```
docker-compose logs -f obi
```
You should see output like:

```
2026/01/30 13:35:17 localhost:5678 172.19.0.1:58574 "GET /hello/world HTTP/1.1" 200 12 "curl/8.16.0" 11.168µs
```

**No traces appearing:**

- Verify the target service is running: `docker-compose ps`
- Check the instrumentation container has host PID access: `pid: 'host'`is set
- Verify privileged mode: `privileged: true`needs to be set
- Check discovery configuration matches your service (port, executable name, etc.)
- View instrumentation logs: `docker-compose logs obi`

**Spans visible in logs but not in Logfire:**

- Verify the Logfire token is correct
- Check the endpoints are correct (`logfire-us.pydantic.dev`,`logfire-eu.pydantic.dev`)
- Ensure the `Authorization`header includes`Bearer`prefix
- Check for export errors in logs: `docker-compose logs obi | grep -i error`


For environments with multiple services, run one instrumentation container per host or one per service depending on your requirements:

```
services:
  frontend:
    image: my-frontend:latest
    ports:
      - '3000:3000'
  backend:
    image: my-backend:latest
    ports:
      - '8080:8080'
  database:
    image: postgres:17
    ports:
      - '5432:5432'
  # Single instrumentation container for both frontend and backend
  autoinstrumenter:
    image: docker.io/otel/ebpf-instrument:v0.4.1
    pid: 'host'
    privileged: true
    environment:
      # Instrument both services by port
      OTEL_EBPF_OPEN_PORT: "3000,8080"
      # Export to Logfire
      OTEL_EXPORTER_OTLP_TRACES_ENDPOINT: "https://logfire-api.pydantic.dev/v1/traces"
      OTEL_EXPORTER_OTLP_METRICS_ENDPOINT: "https://logfire-api.pydantic.dev/v1/metrics"
      OTEL_EXPORTER_OTLP_HEADERS: "Authorization=<your-logfire-token>"
```
Each service's traces will appear in Logfire with the appropriate service name derived from the process name.

You can override this with `OTEL_SERVICE_NAME` if needed.



- **Application context:**User IDs, session tokens, custom business attributes
- **Request/response bodies:**For security and performance, eBPF does not capture payload data
- **Internal function calls:**Only network-level operations are visible


The instrumentation container requires `privileged: true` to attach eBPF programs to the kernel. This grants significant access. In production:

- Run the instrumentation container on a dedicated network segment if possible
- Use `CAP_SYS_ADMIN`,`CAP_BPF`, and`CAP_PERFMON`capabilities instead of full privileged mode where supported (kernel 5.8+)
- Monitor the instrumentation container itself for anomalous behavior
- Restrict access to the docker-compose file containing Logfire credentials


- **Supported:**Linux kernel 4.14+
- **Recommended:**Linux kernel 5.8+ for full feature support
- **Not supported:**Windows, macOS (eBPF is Linux-specific)
- **Container runtimes:**Docker, containerd, CRI-O



Yes. The same `otel/ebpf-instrument` image can run as a DaemonSet in Kubernetes. Service discovery can be based on k8s metadata, for example pod selectors.


Yes. eBPF observes traffic before TLS termination (at the application level) and after TLS termination (at the load balancer level), depending on where it attaches.


Yes. gRPC over HTTP/2 is supported. Spans will include gRPC method names and status codes.


Yes, but not directly through `ebpf-instrument`. You would need to run an OpenTelemetry Collector that receives from the eBPF instrumentation and fans out to multiple backends.


- Start with the basic docker-compose example to verify eBPF works in your environment
- Add endpoint filtering to reduce noise
- Configure resource attributes for service identification
- Set up sampling to reduce
- Create Logfire dashboards to visualize HTTP traffic patterns

eBPF instrumentation provides immediate visibility into application traffic without code changes.

For applications where you control the code and need deeper context, consider migrating to SDK-based instrumentation over time while using eBPF as a stop-gap solution.


Logfire's [free tier](https://logfire.pydantic.dev/) includes 10M spans/month, enough to try eBPF instrumentation on your own services before committing further.

- **Sign up**:- [logfire.pydantic.dev](https://logfire.pydantic.dev/)
- **Read the docs**:- [OpenTelemetry eBPF Instrumentation](https://opentelemetry.io/docs/zero-code/obi/)
- **Questions or feedback**: reach out on- [Slack](https://pydantic.dev/docs/logfire/join-slack/)
