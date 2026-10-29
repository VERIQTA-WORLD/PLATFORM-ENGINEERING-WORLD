# 07.02 · Define an MVP and product measures

**Prerequisites:** Complete the preceding lesson or demonstrate its acceptance criteria.  
**Time:** 60–120 minutes including the exercise and reflection.  
**Environment:** Synthetic local files for the core exercise. The container and Kubernetes lessons have an explicitly optional runtime track.

## What you will learn

By the end, you will explain define an mvp and product measures, produce reviewable evidence, and distinguish what your exercise proves from what requires production verification.

## Build the mental model

A platform MVP is a supported slice of a workflow, including documentation, ownership and recovery. A demo with no support route is not a complete service. Measure adoption with a denominator: five active teams out of eight eligible teams means something different from five page views. Combine task success, time, satisfaction and reliability. Avoid treating deployment frequency as an individual performance score; context and service risk matter.

## Follow along

Work from the repository root. Use `99-work/` if it does not exist. Keep scratch outputs there; commit only a sanitized portfolio artifact when you choose to share your work. Commands use Python 3 and relative paths.

Complete `08-templates/08-product-brief.md` for a “create a standard internal HTTP service” path. Include eligible users, non-goals, support hours, an escape hatch and a retirement criterion. Define numerator, denominator, window and data source for task success and adoption. Use an initial target of 4 successful attempts out of 5 simulated trials, with median time below 15 minutes. Explain that five trials provide weak evidence and identify a larger pilot before rollout.

Before running a command, predict its result. Afterward, record what actually happened. If the result differs, keep that observation and diagnose it; replacing evidence with the expected answer defeats the exercise.

## Acceptance criteria

A reviewer can determine who should use the path, when it is unsupported and how success will be assessed. Your measurement plan includes failed attempts and a qualitative follow-up, rather than filtering to successful users.

Save an evidence file named `99-work/01-02-evidence.md` with the command or procedure, inputs, observation, interpretation and any limitation. For a design exercise, include the completed decision table or template and explain how a reviewer could challenge its assumptions.

## Break it deliberately

Adoption rises while time to complete the task also rises. List two possible explanations and one additional observation that distinguishes them.

Use only the supplied fixtures, your own generated files, or the disposable learning cluster. Preserve the original fixtures so another learner can reproduce the baseline. Restore a valid state when finished and note the repair in your evidence.

## Worked reasoning

More complex teams may have joined the pilot, or the path may have regressed. Segment by task and team experience, inspect failure reasons, and observe the journey. A dashboard alone cannot identify causation.

Compare your explanation with this reasoning after attempting the drill. Different designs are acceptable when their assumptions, enforcement points and failure behavior are explicit. If you chose an alternative, add a short decision record explaining why it meets the same user need.

## Check your understanding

**Question:** Why publish non-goals?

<details>
<summary>Reveal the answer</summary>

They prevent accidental support commitments and help users choose an alternative when the supported path does not fit.

</details>

## Transfer the lesson

Write three short notes: what the local exercise established, what would change with concurrent users or remote resources, and what evidence you would need before promising this behavior to a team. Choose one remaining uncertainty and describe an experiment that would resolve it. Do not present a design or unrun command as a tested implementation.

## Primary reference

[DORA research](https://dora.dev/). Read the sections relevant to the exercise and compare terminology with your artifact. External tools and documentation evolve; record versions when you run the optional integrations.

[Phase index](00-INDEX.md) · [Course contents](../../01-COURSE-MAP.md)


[← Previous lesson](01-discover-developer-needs.md) · [Next lesson →](../08-systems-foundations/01-processes-files-and-interfaces.md)
