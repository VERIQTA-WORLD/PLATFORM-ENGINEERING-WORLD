# Platform engineering field guide

Use this guide when a design exercise needs more detail. It complements the lessons; the primary documentation linked below defines specific tool behavior.

## Platform, DevOps and SRE

DevOps emphasizes collaboration and delivery responsibility. SRE applies engineering to service reliability. Platform engineering curates supported capabilities for internal users. These practices overlap. Assign responsibility by user journey and operational need rather than arguing that one label replaces another. An internal developer platform may be composed of documentation, APIs, CLI tools, templates and managed services; a portal is one possible interface.

A platform team should own the reliability and usability of the workflow it promises. Application teams generally retain responsibility for their application behavior. Record the boundary explicitly: who is paged when creation fails, and who is paged when the created application returns incorrect results?

## Control plane and data plane

The control plane accepts and authorizes intent, records operations and reconciles resources. The data plane serves application traffic or performs the workload. A control-plane outage should not necessarily stop existing workloads. Design the failure boundary: avoid making every application request depend on the platform portal or catalog. Record how cached configuration expires and how credential refresh behaves during an outage.

A practical asynchronous operation has an immutable ID, caller, normalized request, target, policy revision, current state, attempts, timestamps and a bounded error summary. Keep secret material out of that record. Use a durable queue or database transaction pattern so accepted work is not lost between writing a request and enqueueing it.

## Controllers and provider APIs

A controller must tolerate duplicate events, delayed observations and partial success. Use stable external identifiers to discover whether a prior request created a resource. Retrying “create” without an idempotency strategy can leak resources. Use bounded retries with backoff for transient failures; surface permanent rejection quickly. A reconciler that retries authorization denial forever converts a clear user error into an opaque backlog.

Deletion needs a lifecycle. Mark the resource for deletion, stop new work, release dependents in the correct order, preserve required data, then mark the operation complete. Stuck finalization needs an operator procedure and an audit trail. Avoid a force-delete escape hatch without understanding what external state it leaves.

## Infrastructure modules and composition

A module should encode a reusable contract rather than every provider setting. Expose supported inputs, stable outputs and clear upgrade rules. Keep environment-specific values separate from implementation. Validate input early and preserve a mapping to provider resources for troubleshooting. State storage requires access control, concurrency handling and recovery. A state file can contain credentials or sensitive attributes even when source code does not.

When evaluating OpenTofu/Terraform modules, Crossplane compositions or custom controllers, compare control ownership, reconciliation behavior, ecosystem fit, upgrade cost and operational competence. Different abstractions can satisfy the same user task. Avoid placing a second controller over resources already owned by another without a defined handoff.

## Delivery, promotion and progressive rollout

CI establishes evidence about a revision and artifact. CD changes a runtime. GitOps describes declarative, versioned desired state that agents pull and reconcile. These are related but not interchangeable. Build once and promote an immutable artifact. Record target environment and policy decision. A Git revert may change runtime configuration but cannot automatically reverse data loss or external side effects.

Progressive delivery introduces traffic or replicas gradually while checking meaningful signals. Specify minimum sample size, observation duration, abort thresholds and rollback mechanics. A canary with no traffic produces little evidence. A successful health probe does not replace an application correctness measure. For low-traffic systems, synthetic transactions or a longer observation window may be needed.

## Networking and secrets

Draw ingress and egress separately. Identify where DNS resolves, TLS terminates, callers authenticate and authorization occurs. Network reachability is not authorization. Use default-deny policies only when the network plugin enforces them and required DNS/dependency traffic is explicitly allowed and tested.

Secret rotation requires updating the authoritative secret, distributing it, reloading consumers and verifying old credentials no longer work. A secret mounted as a file may update differently from an environment variable. Test the actual application reload behavior. Redaction is defense in depth; avoid logging secrets in the first place. Separate infrastructure state, audit logs and application logs by access need.

## Persistent services and data platforms

Stateful workloads require decisions about consistency, backup, retention, migration, capacity and recovery ownership. A database claim that returns a hostname is incomplete if users cannot request a restore or understand maintenance behavior. Offer service classes with clear RPO/RTO assumptions, supported versions, maintenance windows and data lifecycle. Do not imply a single replica has high availability merely because a controller can recreate it.

For event streams, define ordering, replay, retention and consumer-lag expectations. For data pipelines, include schema evolution, lineage, quality checks and recovery from partially processed batches. Recovery must account for external effects such as already-sent messages.

## AI and GPU platform extensions

Treat accelerator workloads as another product with specialized scheduling, capacity and data requirements. Separate interactive inference, batch jobs and training because their latency and interruption tolerance differ. Define quota, job priority, checkpointing, artifact provenance and data access. Cost allocation should include idle reservations and shared capacity. Do not add a GPU option to a service template without capacity and support plans.

A model endpoint also needs evaluation, rollout controls, monitoring and a rollback strategy for model artifacts and serving code. These are advanced extension topics, not capabilities implemented by this repository.

## Cloud choices without accidental commitments

Compare environments by identity boundary, networking, regional resilience, managed-service availability, operating effort and total cost. Multi-cloud portability is a requirement to justify, not an automatic benefit. Provider-neutral contracts can still expose meaningful differences in consistency, latency, durability and failure behavior. Abstract the task that users need while documenting provider-specific limits.

Before any optional cloud experiment, choose your own sandbox account, budget, permitted region, resource inventory and cleanup check. This course does not provision paid resources or contain cloud credentials. Use current provider documentation to write a concrete plan before executing an integration.

## Operational readiness review

Before a pilot, demonstrate a successful task, a denied task, a partial failure, a retry and a restore. Name the owner of each component and of the end-to-end journey. Publish a support route, SLO, maintenance policy and escape hatch. Record unsupported use cases. Plan schema and template upgrades before generating repositories for many teams.

[Primary references](08-sources.md) · [Architecture boundaries](01-architecture.md) · [Integration extensions](05-integrations.md)
