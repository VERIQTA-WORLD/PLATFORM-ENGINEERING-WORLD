# 11.02 · Environment boundaries and configuration

**Prerequisites:** Complete the preceding lesson or demonstrate its acceptance criteria.  
**Time:** 60–120 minutes including the exercise and reflection.  
**Environment:** Synthetic local files for the core exercise. The container and Kubernetes lessons have an explicitly optional runtime track.

## What you will learn

By the end, you will explain environment boundaries and configuration, produce reviewable evidence, and distinguish what your exercise proves from what requires production verification.

## Build the mental model

An environment is a boundary for risk, data and authority. A namespace is one useful boundary but does not by itself isolate all cluster-level resources or defend against a hostile kernel-level workload. Choose accounts, clusters, namespaces and network controls based on threat and operating requirements. Configuration should vary deliberately across environments; copying an entire tree tends to create drift. Secrets need separate distribution and rotation, not an extra plaintext environment file.

## Follow along

Work from the repository root. Use `99-work/` if it does not exist. Keep scratch outputs there; commit only a sanitized portfolio artifact when you choose to share your work. Commands use Python 3 and relative paths.

Use `08-templates/03-environment-matrix.md` to compare local, preview, staging and production. Specify identities, data classes, expiration, network access, quotas and rollback for each. Design a preview environment with a 24-hour expiry and a maximum of two replicas. Write the reconciliation rule for expired environments and include an ownership check before deletion. Explain why the local CLI cannot guarantee cleanup in a remote system.

Before running a command, predict its result. Afterward, record what actually happened. If the result differs, keep that observation and diagnose it; replacing evidence with the expected answer defeats the exercise.

## Acceptance criteria

The matrix names each boundary and its enforcement point. The preview design has a cleanup controller, an overdue-environment alert and a way to investigate failed deletion. Production data is excluded from preview fixtures.

Save an evidence file named `99-work/05-02-evidence.md` with the command or procedure, inputs, observation, interpretation and any limitation. For a design exercise, include the completed decision table or template and explain how a reviewer could challenge its assumptions.

## Break it deliberately

A developer adds production credentials to a staging pipeline to bypass a deployment error. Explain which boundary has collapsed and propose a least-privilege repair.

Use only the supplied fixtures, your own generated files, or the disposable learning cluster. Preserve the original fixtures so another learner can reproduce the baseline. Restore a valid state when finished and note the repair in your evidence.

## Worked reasoning

The staging workflow can now act in production. Remove the credential, rotate it if exposed and repair the staging role binding or target configuration. Separate workflow identities by environment and authorize explicit resources.

Compare your explanation with this reasoning after attempting the drill. Different designs are acceptable when their assumptions, enforcement points and failure behavior are explicit. If you chose an alternative, add a short decision record explaining why it meets the same user need.

## Check your understanding

**Question:** Why is expiry metadata insufficient for cleanup?

<details>
<summary>Reveal the answer</summary>

A running actor must observe the timestamp, perform deletion, handle failures and report environments that remain.

</details>

## Transfer the lesson

Write three short notes: what the local exercise established, what would change with concurrent users or remote resources, and what evidence you would need before promising this behavior to a team. Choose one remaining uncertainty and describe an experiment that would resolve it. Do not present a design or unrun command as a tested implementation.

## Primary reference

[Kubernetes documentation](https://kubernetes.io/docs/). Read the sections relevant to the exercise and compare terminology with your artifact. External tools and documentation evolve; record versions when you run the optional integrations.

[Phase index](00-INDEX.md) · [Course contents](../../01-COURSE-MAP.md)


[← Previous lesson](01-infrastructure-state-and-change-review.md) · [Next lesson →](../12-delivery-and-reconciliation/01-build-pipelines-and-release-evidence.md)
