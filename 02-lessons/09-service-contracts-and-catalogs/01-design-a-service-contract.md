# 09.01 · Design a service contract

**Prerequisites:** Complete the preceding lesson or demonstrate its acceptance criteria.  
**Time:** 60–120 minutes including the exercise and reflection.  
**Environment:** Synthetic local files for the core exercise. The container and Kubernetes lessons have an explicitly optional runtime track.

## What you will learn

By the end, you will explain design a service contract, produce reviewable evidence, and distinguish what your exercise proves from what requires production verification.

## Build the mental model

A service contract is a shared agreement between a developer and the platform. Begin with fields needed for a specific decision. In this course, name identifies the service, owner routes responsibility, tier selects expectations, replicas expresses desired capacity, and runbook points to recovery instructions. Public exposure requires authentication in the teaching policy. A boolean is a deliberate simplification: production systems must verify actual ingress and identity configuration instead of trusting a declaration.

## Follow along

Work from the repository root. Use `99-work/` if it does not exist. Keep scratch outputs there; commit only a sanitized portfolio artifact when you choose to share your work. Commands use Python 3 and relative paths.

Inspect `04-fixtures/02-desired.json` and run the validator. Copy it to `99-work/01-service.json` and change one field at a time: empty owner, zero replicas, unknown tier and public exposure without auth. Save each error in a small table. Restore a valid file. Propose a versioned `apiVersion` field and write a migration rule for existing documents; do not silently reinterpret an old field. Document the difference between required metadata and enforced runtime behavior.

Before running a command, predict its result. Afterward, record what actually happened. If the result differs, keep that observation and diagnose it; replacing evidence with the expected answer defeats the exercise.

## Acceptance criteria

You can explain every rejection and repair it. Your proposed migration specifies a default or explicit error for old documents and includes one compatibility test. You do not claim the current CLI enforces schema versioning or runtime authentication.

Save an evidence file named `99-work/03-01-evidence.md` with the command or procedure, inputs, observation, interpretation and any limitation. For a design exercise, include the completed decision table or template and explain how a reviewer could challenge its assumptions.

## Break it deliberately

Put a nonempty but nonexistent path in `runbook`. Observe that validation passes. Describe the additional check needed to establish that a useful runbook exists.

Use only the supplied fixtures, your own generated files, or the disposable learning cluster. Preserve the original fixtures so another learner can reproduce the baseline. Restore a valid state when finished and note the repair in your evidence.

## Worked reasoning

The validator checks presence, not existence or quality. A repository-aware check could resolve the path within an allowed root, verify the file and assess required recovery sections. Existence still does not prove that the procedure works.

Compare your explanation with this reasoning after attempting the drill. Different designs are acceptable when their assumptions, enforcement points and failure behavior are explicit. If you chose an alternative, add a short decision record explaining why it meets the same user need.

## Check your understanding

**Question:** Why not add every possible catalog field immediately?

<details>
<summary>Reveal the answer</summary>

Each required field adds maintenance and onboarding cost. Add fields when a supported decision or workflow needs them.

</details>

## Transfer the lesson

Write three short notes: what the local exercise established, what would change with concurrent users or remote resources, and what evidence you would need before promising this behavior to a team. Choose one remaining uncertainty and describe an experiment that would resolve it. Do not present a design or unrun command as a tested implementation.

## Primary reference

[Backstage Software Catalog](https://backstage.io/docs/features/software-catalog/). Read the sections relevant to the exercise and compare terminology with your artifact. External tools and documentation evolve; record versions when you run the optional integrations.

[Phase index](00-INDEX.md) · [Course contents](../../01-COURSE-MAP.md)


[← Previous lesson](../08-systems-foundations/02-networking-dns-and-trust-boundaries.md) · [Next lesson →](02-catalog-ownership-and-lifecycle.md)
