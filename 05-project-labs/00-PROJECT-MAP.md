# Platform Engineering World · Project laboratory

This directory contains executable learning work, not project titles waiting to be written. Projects 03–10 each include `00-LAB.md`, `01-starter.py`, `02-solution.py` and `03-grade.py`. The starter deliberately fails until you implement the behavior. The grader can evaluate your own file, and `--solution` verifies the complete instructor reference.

## Begin with the foundations

The [foundation lesson map](../01-COURSE-MAP.md) teaches each required skill first. The [17 foundation reference programs](02-foundations/00-INDEX.md) correspond to those lessons. Do not start an advanced database/control-plane project before you understand its Python and SQL prerequisites.

## Build the platform mechanisms

| Project | What you implement | Guide |
| --- | --- | --- |
| 03 | Contract validator with allow, deny, duplicate and type-boundary evidence. | [Stages, code and grader](03-catalog-contract/00-LAB.md) |
| 04 | Deterministic plan and proof of convergence for managed objects. | [Stages, code and grader](04-desired-state-controller/00-LAB.md) |
| 05 | Tenant/action decision table and negative tests at the mutation boundary. | [Stages, code and grader](05-tenant-authorization/00-LAB.md) |
| 06 | Durable scoped request identity, conflict rejection and preserved row count. | [Stages, code and grader](06-durable-operations/00-LAB.md) |
| 07 | Compare-and-set update with a demonstrated stale-writer conflict. | [Stages, code and grader](07-concurrent-updates/00-LAB.md) |
| 08 | Bounded transient retries, immediate permanent rejection and exhaustion evidence. | [Stages, code and grader](08-retry-classification/00-LAB.md) |
| 09 | An idempotent expand migration that preserves old readers and new values. | [Stages, code and grader](09-schema-migration/00-LAB.md) |
| 10 | Byte integrity, pre-write validation and collision preservation. | [Stages, code and grader](10-verified-recovery/00-LAB.md) |

## Integrate and run real services

- [Project 11 · Self-service HTTP API](11-self-service-api/00-LAB.md): persistent operations, scoped demo identities, quotas, reconciliation, revision guards, restart and recovery. Includes a complete server, client and actual HTTP smoke test.
- [Project 01 · Containers and Kubernetes](01-kubernetes/00-INDEX.md): build an HTTP image, deploy it to a disposable kind cluster, break readiness, repair and clean up. Requires the separately installed runtime tools.

- [Project 12 · OpenTofu infrastructure state](12-infrastructure-state/00-LAB.md): actual HCL, validation, saved plan, apply, no-change check, rejected input and destroy. Requires OpenTofu; it creates no cloud resources.

## Verify instructor implementations

From the repository root:

```sh
python3 06-tools/05-check-all.py
```

This runs actual numbered unit test files, the content audit, the local lifecycle, all eight project solution graders and the HTTP integration. It refuses a zero-test result. Use `--skip-http` only when your environment blocks loopback networking; the output explicitly reports that integration as unverified.

## Portfolio gate

For each project keep your implementation, observed failure, repaired result and explanation. A passing instructor solution is not a passing learner submission. The capstones require your own extension and operational evidence.
