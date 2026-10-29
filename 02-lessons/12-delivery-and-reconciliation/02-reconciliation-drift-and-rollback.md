# 12.02 · Reconciliation, drift and rollback

**Prerequisites:** Complete the preceding lesson or demonstrate its acceptance criteria.  
**Time:** 60–120 minutes including the exercise and reflection.  
**Environment:** Synthetic local files for the core exercise. The container and Kubernetes lessons have an explicitly optional runtime track.

## What you will learn

By the end, you will explain reconciliation, drift and rollback, produce reviewable evidence, and distinguish what your exercise proves from what requires production verification.

## Build the mental model

A reconciliation loop repeatedly compares desired and observed state and acts to reduce the difference. Repeating the same desired input should converge rather than create new duplicate resources. GitOps adds versioned declarations pulled by an agent and continuous reconciliation. The CLI here is a one-shot local simulation: it has no daemon, remote API or Git integration. Use it to reason about convergence before adding a real controller.

## Follow along

Work from the repository root. Use `99-work/` if it does not exist. Keep scratch outputs there; commit only a sanitized portfolio artifact when you choose to share your work. Commands use Python 3 and relative paths.

Apply the fixtures to `99-work/01-converged.json`. Plan desired state against the output and verify an empty list. Change replicas in the output back to one, then plan again and observe an update. Apply again to a new output. Write a rollback decision: reverting desired state is appropriate for stateless configuration, but may not reverse a database migration. Include an abort criterion and a forward-fix option.

Before running a command, predict its result. Afterward, record what actually happened. If the result differs, keep that observation and diagnose it; replacing evidence with the expected answer defeats the exercise.

## Acceptance criteria

The second plan is empty until drift is introduced. Reapplying repairs the modeled drift without duplicates. Your explanation separates a one-shot command from continuous reconciliation and names at least one irreversible side effect.

Save an evidence file named `99-work/06-02-evidence.md` with the command or procedure, inputs, observation, interpretation and any limitation. For a design exercise, include the completed decision table or template and explain how a reviewer could challenge its assumptions.

## Break it deliberately

Remove a service from desired state and observe it is retained. Explain why “no creates or updates” is weaker than “all actual state equals desired state” in this implementation.

Use only the supplied fixtures, your own generated files, or the disposable learning cluster. Preserve the original fixtures so another learner can reproduce the baseline. Restore a valid state when finished and note the repair in your evidence.

## Worked reasoning

Retained unmanaged resources remain outside desired state. A production controller needs an explicit adoption and deletion policy, finalizers or equivalent cleanup handling, and observability for resources it cannot remove.

Compare your explanation with this reasoning after attempting the drill. Different designs are acceptable when their assumptions, enforcement points and failure behavior are explicit. If you chose an alternative, add a short decision record explaining why it meets the same user need.

## Check your understanding

**Question:** Can reverting Git always undo a release?

<details>
<summary>Reveal the answer</summary>

No. External effects and data migrations may require a forward fix or a separate recovery procedure.

</details>

## Transfer the lesson

Write three short notes: what the local exercise established, what would change with concurrent users or remote resources, and what evidence you would need before promising this behavior to a team. Choose one remaining uncertainty and describe an experiment that would resolve it. Do not present a design or unrun command as a tested implementation.

## Primary reference

[OpenGitOps principles](https://opengitops.dev/). Read the sections relevant to the exercise and compare terminology with your artifact. External tools and documentation evolve; record versions when you run the optional integrations.

[Phase index](00-INDEX.md) · [Course contents](../../01-COURSE-MAP.md)


[← Previous lesson](01-build-pipelines-and-release-evidence.md) · [Next lesson →](../13-self-service-and-developer-experience/01-golden-paths-and-scaffolding.md)
