# 19.01 · Support, incidents and on-call

**Prerequisites:** Complete the preceding lesson or demonstrate its acceptance criteria.  
**Time:** 60–120 minutes including the exercise and reflection.  
**Environment:** Synthetic local files for the core exercise. The container and Kubernetes lessons have an explicitly optional runtime track.

## What you will learn

By the end, you will explain support, incidents and on-call, produce reviewable evidence, and distinguish what your exercise proves from what requires production verification.

## Build the mental model

A platform becomes part of its users’ critical path. Publish support scope, contact routes, severity definitions and escalation ownership before broad adoption. Separate service restoration from root-cause investigation. During an incident, provide a shared timeline, current impact, actions and next update time. A post-incident review should identify contributing conditions and testable improvements, rather than ending with “be more careful.”

## Follow along

Work from the repository root. Use `99-work/` if it does not exist. Keep scratch outputs there; commit only a sanitized portfolio artifact when you choose to share your work. Commands use Python 3 and relative paths.

Use `08-templates/05-incident.md` for a simulated outage: service creation is stuck but existing services keep running. Declare the affected user journey and severity, choose an incident commander and technical lead, and write three time-stamped updates. Add a mitigation that pauses new requests and preserves queued work. Write two corrective actions with owners, due dates expressed relative to the exercise and verification criteria.

Before running a command, predict its result. Afterward, record what actually happened. If the result differs, keep that observation and diagnose it; replacing evidence with the expected answer defeats the exercise.

## Acceptance criteria

Updates distinguish existing-service availability from provisioning availability. The timeline includes decisions and evidence. Corrective actions change the system or process and include a way to verify improvement.

Save an evidence file named `99-work/13-01-evidence.md` with the command or procedure, inputs, observation, interpretation and any limitation. For a design exercise, include the completed decision table or template and explain how a reviewer could challenge its assumptions.

## Break it deliberately

The portal looks healthy and the infrastructure team reports no outage. Show how a synthetic end-to-end creation check reveals a platform-level incident anyway.

Use only the supplied fixtures, your own generated files, or the disposable learning cluster. Preserve the original fixtures so another learner can reproduce the baseline. Restore a valid state when finished and note the repair in your evidence.

## Worked reasoning

Each component can be individually available while their integration fails. Define service-level health around the completed user journey and assign an owner to that whole path, including the queue and reconciler.

Compare your explanation with this reasoning after attempting the drill. Different designs are acceptable when their assumptions, enforcement points and failure behavior are explicit. If you chose an alternative, add a short decision record explaining why it meets the same user need.

## Check your understanding

**Question:** What should an incident update contain?

<details>
<summary>Reveal the answer</summary>

Observed impact, current action, uncertainty and the time of the next update, without unsupported root-cause claims.

</details>

## Transfer the lesson

Write three short notes: what the local exercise established, what would change with concurrent users or remote resources, and what evidence you would need before promising this behavior to a team. Choose one remaining uncertainty and describe an experiment that would resolve it. Do not present a design or unrun command as a tested implementation.

## Primary reference

[Google SRE books](https://sre.google/books/). Read the sections relevant to the exercise and compare terminology with your artifact. External tools and documentation evolve; record versions when you run the optional integrations.

[Phase index](00-INDEX.md) · [Course contents](../../01-COURSE-MAP.md)


[← Previous lesson](../18-cost-and-capacity/02-capacity-autoscaling-and-load-tests.md) · [Next lesson →](02-versioning-migrations-and-deprecation.md)
