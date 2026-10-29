# 13.01 · Golden paths and scaffolding

**Prerequisites:** Complete the preceding lesson or demonstrate its acceptance criteria.  
**Time:** 60–120 minutes including the exercise and reflection.  
**Environment:** Synthetic local files for the core exercise. The container and Kubernetes lessons have an explicitly optional runtime track.

## What you will learn

By the end, you will explain golden paths and scaffolding, produce reviewable evidence, and distinguish what your exercise proves from what requires production verification.

## Build the mental model

A golden path is a supported way to complete a job, including operations after initial creation. Scaffolding lowers the cost of the first step but can create hundreds of stale copies if upgrades are ignored. Keep stable interfaces in the generated repository and centralize changeable behavior where that reduces migration cost. Give users a documented escape hatch: exceptions should be visible and owned, not hidden in copied scripts.

## Follow along

Work from the repository root. Use `99-work/` if it does not exist. Keep scratch outputs there; commit only a sanitized portfolio artifact when you choose to share your work. Commands use Python 3 and relative paths.

Run `python3 03-reference-platform/01-pe.py scaffold inventory --owner commerce --out 99-work/01-inventory`. Inspect the generated contract and runbook. Validate `99-work/01-inventory/01-service.json`. Define what the scaffold guarantees and what the user still owns. Add a template version proposal and an upgrade procedure for existing services. Have a second person follow the commands, or perform a fresh-directory walkthrough and explicitly label it as a self-review.

Before running a command, predict its result. Afterward, record what actually happened. If the result differs, keep that observation and diagnose it; replacing evidence with the expected answer defeats the exercise.

## Acceptance criteria

The generated contract is valid and the runbook exists. Your product description states that no runtime service has been deployed. The upgrade proposal includes detection of modified generated files and an explicit review step.

Save an evidence file named `99-work/07-01-evidence.md` with the command or procedure, inputs, observation, interpretation and any limitation. For a design exercise, include the completed decision table or template and explain how a reviewer could challenge its assumptions.

## Break it deliberately

Run scaffold again with the same output path. Expect a refusal rather than silent overwrite. Explain how a portal should display this failure and help the user choose another name or inspect the existing operation.

Use only the supplied fixtures, your own generated files, or the disposable learning cluster. Preserve the original fixtures so another learner can reproduce the baseline. Restore a valid state when finished and note the repair in your evidence.

## Worked reasoning

Creation should be retryable without destroying user work. A production API could use an idempotency key and return the previous operation. The local tool instead refuses a collision; callers must not blindly delete the directory and retry.

Compare your explanation with this reasoning after attempting the drill. Different designs are acceptable when their assumptions, enforcement points and failure behavior are explicit. If you chose an alternative, add a short decision record explaining why it meets the same user need.

## Check your understanding

**Question:** What makes scaffolding insufficient as a platform?

<details>
<summary>Reveal the answer</summary>

Users also need delivery, upgrades, operations, support and a maintained contract after repository creation.

</details>

## Transfer the lesson

Write three short notes: what the local exercise established, what would change with concurrent users or remote resources, and what evidence you would need before promising this behavior to a team. Choose one remaining uncertainty and describe an experiment that would resolve it. Do not present a design or unrun command as a tested implementation.

## Primary reference

[Backstage Software Catalog](https://backstage.io/docs/features/software-catalog/). Read the sections relevant to the exercise and compare terminology with your artifact. External tools and documentation evolve; record versions when you run the optional integrations.

[Phase index](00-INDEX.md) · [Course contents](../../01-COURSE-MAP.md)


[← Previous lesson](../12-delivery-and-reconciliation/02-reconciliation-drift-and-rollback.md) · [Next lesson →](02-self-service-apis-and-asynchronous-work.md)
