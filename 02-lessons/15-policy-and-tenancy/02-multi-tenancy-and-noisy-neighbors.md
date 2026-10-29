# 15.02 · Multi-tenancy and noisy neighbors

**Prerequisites:** Complete the preceding lesson or demonstrate its acceptance criteria.  
**Time:** 60–120 minutes including the exercise and reflection.  
**Environment:** Synthetic local files for the core exercise. The container and Kubernetes lessons have an explicitly optional runtime track.

## What you will learn

By the end, you will explain multi-tenancy and noisy neighbors, produce reviewable evidence, and distinguish what your exercise proves from what requires production verification.

## Build the mental model

Tenancy combines identity, data isolation, network controls, resource fairness and operational boundaries. Namespaces organize objects but do not automatically prevent network access or resource exhaustion. ResourceQuota constrains namespace consumption; LimitRange can establish per-container bounds. NetworkPolicy depends on an enforcing network implementation. Some tenants need separate clusters or accounts because shared control-plane and node risks exceed the acceptable boundary.

## Follow along

Work from the repository root. Use `99-work/` if it does not exist. Keep scratch outputs there; commit only a sanitized portfolio artifact when you choose to share your work. Commands use Python 3 and relative paths.

Design bronze and restricted tenant profiles in `08-templates/11-tenant-profile.md`. Include API permissions, pod security, network ingress and egress, storage, quotas and support expectations. Estimate the effect of ten teams each requesting two 500m CPU replicas. Specify an admission rule for requests that exceed the tenant budget. Describe a tenant onboarding and offboarding procedure including data ownership.

Before running a command, predict its result. Afterward, record what actually happened. If the result differs, keep that observation and diagnose it; replacing evidence with the expected answer defeats the exercise.

## Acceptance criteria

The profiles identify controls and their enforcement points. Your capacity arithmetic totals 10 requested CPU cores before system overhead. The restricted profile explains why stronger isolation may require a separate cluster or account.

Save an evidence file named `99-work/09-02-evidence.md` with the command or procedure, inputs, observation, interpretation and any limitation. For a design exercise, include the completed decision table or template and explain how a reviewer could challenge its assumptions.

## Break it deliberately

One tenant runs a CPU-intensive job and another misses its latency objective. List the resource observations needed before attributing the incident to a noisy neighbor.

Use only the supplied fixtures, your own generated files, or the disposable learning cluster. Preserve the original fixtures so another learner can reproduce the baseline. Restore a valid state when finished and note the repair in your evidence.

## Worked reasoning

Compare requests, limits, node pressure, throttling, scheduling events and latency by workload. Correlation is a lead, not proof. Also inspect downstream saturation and recent application changes before moving tenants.

Compare your explanation with this reasoning after attempting the drill. Different designs are acceptable when their assumptions, enforcement points and failure behavior are explicit. If you chose an alternative, add a short decision record explaining why it meets the same user need.

## Check your understanding

**Question:** Does defining a NetworkPolicy guarantee enforcement?

<details>
<summary>Reveal the answer</summary>

No. The cluster network implementation must support and enforce it, and the actual allowed traffic must be tested.

</details>

## Transfer the lesson

Write three short notes: what the local exercise established, what would change with concurrent users or remote resources, and what evidence you would need before promising this behavior to a team. Choose one remaining uncertainty and describe an experiment that would resolve it. Do not present a design or unrun command as a tested implementation.

## Primary reference

[Kubernetes documentation](https://kubernetes.io/docs/). Read the sections relevant to the exercise and compare terminology with your artifact. External tools and documentation evolve; record versions when you run the optional integrations.

[Phase index](00-INDEX.md) · [Course contents](../../01-COURSE-MAP.md)


[← Previous lesson](01-policy-as-an-explainable-contract.md) · [Next lesson →](../16-observability-and-reliability/01-signals-and-user-centered-observability.md)
