# 11.01 · Infrastructure state and change review

**Prerequisites:** Complete the preceding lesson or demonstrate its acceptance criteria.  
**Time:** 60–120 minutes including the exercise and reflection.  
**Environment:** Synthetic local files for the core exercise. The container and Kubernetes lessons have an explicitly optional runtime track.

## What you will learn

By the end, you will explain infrastructure state and change review, produce reviewable evidence, and distinguish what your exercise proves from what requires production verification.

## Build the mental model

Infrastructure as code combines a declarative model with a provider that performs effects. State links declarations to remote objects; losing it is different from deleting the remote objects. A plan can contain replacement, data loss or privilege expansion even when the text diff is small. Review the effect, ownership and recovery path. The local reconciler is a learning model of desired and actual state, not an OpenTofu provider or an infrastructure deployment engine.

## Follow along

Work from the repository root. Use `99-work/` if it does not exist. Keep scratch outputs there; commit only a sanitized portfolio artifact when you choose to share your work. Commands use Python 3 and relative paths.

Run `plan` against the fixtures and save the update. Remove the service from a copy of desired state and plan again. Observe `retain-unmanaged`; the simulator intentionally does not delete absent objects. Write a change review for a database replacement with expected downtime, data migration, owner, backup and abort condition. Read the OpenTofu state documentation and explain how locking and sensitive state differ from this local JSON model.

Before running a command, predict its result. Afterward, record what actually happened. If the result differs, keep that observation and diagnose it; replacing evidence with the expected answer defeats the exercise.

## Run the actual infrastructure tool

Complete [project 12](../../05-project-labs/12-infrastructure-state/00-LAB.md). It introduces HCL syntax, initializes OpenTofu, saves and inspects a plan, applies a builtin data resource, demonstrates a no-change second plan, rejects an invalid replica count and destroys the exercise state. This is separate from the Python simulation and its execution must be recorded with the tool version.

## Acceptance criteria

Your review distinguishes a source removal from a safe deletion. It includes a verified backup and a condition under which the change must stop. It recognizes that production state may contain sensitive data and needs restricted storage and recovery.

Save an evidence file named `99-work/05-01-evidence.md` with the command or procedure, inputs, observation, interpretation and any limitation. For a design exercise, include the completed decision table or template and explain how a reviewer could challenge its assumptions.

## Break it deliberately

Two operators plan against the same baseline and apply different desired files. Explain the lost-update risk and propose a lock plus revision check.

Use only the supplied fixtures, your own generated files, or the disposable learning cluster. Preserve the original fixtures so another learner can reproduce the baseline. Restore a valid state when finished and note the repair in your evidence.

## Worked reasoning

Both plans can be locally correct yet conflict. Serialize writers and compare the baseline revision when committing. Locking alone does not make a stale decision current; refresh and re-plan when the revision changes.

Compare your explanation with this reasoning after attempting the drill. Different designs are acceptable when their assumptions, enforcement points and failure behavior are explicit. If you chose an alternative, add a short decision record explaining why it meets the same user need.

## Check your understanding

**Question:** Is an infrastructure plan permanently valid?

<details>
<summary>Reveal the answer</summary>

No. Remote state, provider behavior or credentials can change after the plan was generated.

</details>

## Transfer the lesson

Write three short notes: what the local exercise established, what would change with concurrent users or remote resources, and what evidence you would need before promising this behavior to a team. Choose one remaining uncertainty and describe an experiment that would resolve it. Do not present a design or unrun command as a tested implementation.

## Primary reference

[OpenTofu state documentation](https://opentofu.org/docs/language/state/). Read the sections relevant to the exercise and compare terminology with your artifact. External tools and documentation evolve; record versions when you run the optional integrations.

[Phase index](00-INDEX.md) · [Course contents](../../01-COURSE-MAP.md)


[← Previous lesson](../10-containers-and-kubernetes/02-kubernetes-health-and-resource-behavior.md) · [Next lesson →](02-environment-boundaries-and-configuration.md)
