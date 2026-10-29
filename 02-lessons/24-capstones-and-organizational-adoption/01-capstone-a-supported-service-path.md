# 24.01 · Capstone: a supported service path

**Prerequisites:** Complete the preceding lesson or demonstrate its acceptance criteria.  
**Time:** 6–12 hours for the written defense; implementation time is additional.  
**Environment:** Synthetic local files for the core exercise. The container and Kubernetes lessons have an explicitly optional runtime track.

## What you will learn

By the end, you will explain capstone: a supported service path, produce reviewable evidence, and distinguish what your exercise proves from what requires production verification.

## Build the mental model

Build a complete local service lifecycle for a fictional team. The capstone combines product scope, a contract, creation, validation, reconciliation, observability and recovery. The local CLI is a reference model, not the final product. Your implementation may extend it or replace it, but must preserve reviewable behavior and demonstrate failure handling. Scope the project to internal HTTP services so that your promises remain testable.

## Follow along

Work from the repository root. Use `99-work/` if it does not exist. Keep scratch outputs there; commit only a sanitized portfolio artifact when you choose to share your work. Commands use Python 3 and relative paths.

Follow capstone A in `01-guides/02-capstones.md`. Start with a discovery brief and a fresh directory. Create a service, validate it, plan a rollout, apply, prove convergence, introduce drift and recover. Calculate an SLO from synthetic events and restore a catalog backup. Add one meaningful feature, such as version validation or an explicit deletion approval record. Include tests for success, rejection and recovery for your extension.

Before running a command, predict its result. Afterward, record what actually happened. If the result differs, keep that observation and diagnose it; replacing evidence with the expected answer defeats the exercise.

## Acceptance criteria

A reviewer can reproduce the demo from the repository alone. All mandatory rubric items pass. You distinguish locally executed checks from optional cluster or cloud work. The final explanation includes a supported use case, known limits and ownership for maintenance.

Save an evidence file named `99-work/14-01-evidence.md` with the command or procedure, inputs, observation, interpretation and any limitation. For a design exercise, include the completed decision table or template and explain how a reviewer could challenge its assumptions.

## Break it deliberately

Choose one adversarial case: duplicate request, corrupted backup, stale state or denied public exposure. Demonstrate failure before repair and explain what state remains afterward.

Use only the supplied fixtures, your own generated files, or the disposable learning cluster. Preserve the original fixtures so another learner can reproduce the baseline. Restore a valid state when finished and note the repair in your evidence.

## Worked reasoning

A credible platform demo includes an unsuccessful path. Evidence should show that the error is actionable, user work is preserved where promised, and retrying after repair produces a coherent final state.

Compare your explanation with this reasoning after attempting the drill. Different designs are acceptable when their assumptions, enforcement points and failure behavior are explicit. If you chose an alternative, add a short decision record explaining why it meets the same user need.

## Check your understanding

**Question:** What distinguishes a capstone from a tool-installation checklist?

<details>
<summary>Reveal the answer</summary>

A capstone demonstrates a user outcome, failure handling, recovery and an operational contract across the full workflow.

</details>

## Transfer the lesson

Write three short notes: what the local exercise established, what would change with concurrent users or remote resources, and what evidence you would need before promising this behavior to a team. Choose one remaining uncertainty and describe an experiment that would resolve it. Do not present a design or unrun command as a tested implementation.

## Primary reference

[CNCF Platforms white paper](https://tag-app-delivery.cncf.io/whitepapers/platforms/). Read the sections relevant to the exercise and compare terminology with your artifact. External tools and documentation evolve; record versions when you run the optional integrations.

[Phase index](00-INDEX.md) · [Course contents](../../01-COURSE-MAP.md)


[← Previous lesson](../23-senior-platform-practice/03-defend-an-architecture-and-lead-adoption.md) · [Next lesson →](02-capstone-adoption-and-architecture-defense.md)
