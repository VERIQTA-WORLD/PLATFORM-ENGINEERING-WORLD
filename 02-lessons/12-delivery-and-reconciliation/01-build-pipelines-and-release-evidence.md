# 12.01 · Build pipelines and release evidence

**Prerequisites:** Complete the preceding lesson or demonstrate its acceptance criteria.  
**Time:** 60–120 minutes including the exercise and reflection.  
**Environment:** Synthetic local files for the core exercise. The container and Kubernetes lessons have an explicitly optional runtime track.

## What you will learn

By the end, you will explain build pipelines and release evidence, produce reviewable evidence, and distinguish what your exercise proves from what requires production verification.

## Build the mental model

Continuous integration should produce evidence about a specific revision. Tests, image scanning, provenance and deployment approval answer different questions. A passing test suite cannot prove that a dependency is trustworthy, and a signed image can still contain a vulnerable application. Build once and promote the same artifact where possible. Rebuilding separately in each environment can invalidate the relationship between tested content and deployed content.

## Follow along

Work from the repository root. Use `99-work/` if it does not exist. Keep scratch outputs there; commit only a sanitized portfolio artifact when you choose to share your work. Commands use Python 3 and relative paths.

Read `11-hosting-examples/01-workflows/01-ci.yml`. Run its Python checks locally. Draw a release evidence chain from source revision to test results, image digest, review decision and deployment observation. Add a proposed artifact metadata document with revision, digest, builder identity and timestamp. Identify which fields are absent from the teaching CI and what system would produce each. Do not invent a successful container build record.

Before running a command, predict its result. Afterward, record what actually happened. If the result differs, keep that observation and diagnose it; replacing evidence with the expected answer defeats the exercise.

## Acceptance criteria

The evidence chain identifies immutable references and distinguishes CI validation from deployment. Your proposed workflow has minimal permissions and does not require a long-lived cloud credential for documentation checks.

Save an evidence file named `99-work/06-01-evidence.md` with the command or procedure, inputs, observation, interpretation and any limitation. For a design exercise, include the completed decision table or template and explain how a reviewer could challenge its assumptions.

## Break it deliberately

An image passes CI under a tag, then the tag is overwritten before deployment. Show how recording and deploying an immutable digest prevents that ambiguity.

Use only the supplied fixtures, your own generated files, or the disposable learning cluster. Preserve the original fixtures so another learner can reproduce the baseline. Restore a valid state when finished and note the repair in your evidence.

## Worked reasoning

The approval must reference the exact artifact, and the runtime request must use that same content reference. Registry access controls and provenance verification add protection, but a tag-only approval leaves a gap.

Compare your explanation with this reasoning after attempting the drill. Different designs are acceptable when their assumptions, enforcement points and failure behavior are explicit. If you chose an alternative, add a short decision record explaining why it meets the same user need.

## Check your understanding

**Question:** What should a release approval identify?

<details>
<summary>Reveal the answer</summary>

The exact source and artifact, target environment, relevant evidence and authorized decision maker.

</details>

## Transfer the lesson

Write three short notes: what the local exercise established, what would change with concurrent users or remote resources, and what evidence you would need before promising this behavior to a team. Choose one remaining uncertainty and describe an experiment that would resolve it. Do not present a design or unrun command as a tested implementation.

## Primary reference

[SLSA specification](https://slsa.dev/spec/). Read the sections relevant to the exercise and compare terminology with your artifact. External tools and documentation evolve; record versions when you run the optional integrations.

[Phase index](00-INDEX.md) · [Course contents](../../01-COURSE-MAP.md)


[← Previous lesson](../11-infrastructure-and-environments/02-environment-boundaries-and-configuration.md) · [Next lesson →](02-reconciliation-drift-and-rollback.md)
