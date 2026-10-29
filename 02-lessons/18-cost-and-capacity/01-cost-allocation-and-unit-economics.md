# 18.01 · Cost allocation and unit economics

**Prerequisites:** Complete the preceding lesson or demonstrate its acceptance criteria.  
**Time:** 60–120 minutes including the exercise and reflection.  
**Environment:** Synthetic local files for the core exercise. The container and Kubernetes lessons have an explicitly optional runtime track.

## What you will learn

By the end, you will explain cost allocation and unit economics, produce reviewable evidence, and distinguish what your exercise proves from what requires production verification.

## Build the mental model

Cost visibility needs ownership, a time window and an allocation rule. Showback reports costs; chargeback transfers them. Shared services need an explicit allocation policy rather than pretending every bill line belongs naturally to one team. Unit cost connects spending to useful work, such as cost per successful environment-hour. A cheaper platform can still be worse if users spend much more engineering time operating it.

## Follow along

Work from the repository root. Use `99-work/` if it does not exist. Keep scratch outputs there; commit only a sanitized portfolio artifact when you choose to share your work. Commands use Python 3 and relative paths.

Run `python3 03-reference-platform/01-pe.py cost 04-fixtures/05-usage.json`. Verify commerce is 2.88 and search is 4.80 in the fixture’s unspecified currency. Add a shared control-plane cost of 12 per day in your worksheet and compare equal allocation with allocation proportional to direct usage. State the currency, time interval and excluded costs before using the results. Calculate cost per successful operation for 80 successes and a total cost of 20.

Before running a command, predict its result. Afterward, record what actually happened. If the result differs, keep that observation and diagnose it; replacing evidence with the expected answer defeats the exercise.

## Acceptance criteria

The CLI totals match your arithmetic. Your worksheet exposes the allocation assumptions and does not present fixture rates as cloud prices. Cost per successful operation is 0.25 in the declared currency, excluding any separately stated labor or support costs.

Save an evidence file named `99-work/12-01-evidence.md` with the command or procedure, inputs, observation, interpretation and any limitation. For a design exercise, include the completed decision table or template and explain how a reviewer could challenge its assumptions.

## Break it deliberately

A team deletes resources and loses the labels used for billing attribution. Explain how usage records should preserve ownership at the time of consumption.

Use only the supplied fixtures, your own generated files, or the disposable learning cluster. Preserve the original fixtures so another learner can reproduce the baseline. Restore a valid state when finished and note the repair in your evidence.

## Worked reasoning

Historical cost allocation should use time-stamped ownership snapshots or immutable usage attribution. Looking up only today’s catalog can reassign past costs after a team transfer or resource deletion.

Compare your explanation with this reasoning after attempting the drill. Different designs are acceptable when their assumptions, enforcement points and failure behavior are explicit. If you chose an alternative, add a short decision record explaining why it meets the same user need.

## Check your understanding

**Question:** Why distinguish requests from actual utilization?

<details>
<summary>Reveal the answer</summary>

Requests reserve scheduling capacity; actual consumption measures use. Both affect efficiency decisions in different ways.

</details>

## Transfer the lesson

Write three short notes: what the local exercise established, what would change with concurrent users or remote resources, and what evidence you would need before promising this behavior to a team. Choose one remaining uncertainty and describe an experiment that would resolve it. Do not present a design or unrun command as a tested implementation.

## Primary reference

[FinOps Framework](https://www.finops.org/framework/). Read the sections relevant to the exercise and compare terminology with your artifact. External tools and documentation evolve; record versions when you run the optional integrations.

[Phase index](00-INDEX.md) · [Course contents](../../01-COURSE-MAP.md)


[← Previous lesson](../17-data-and-recovery/02-database-changes-and-disaster-recovery.md) · [Next lesson →](02-capacity-autoscaling-and-load-tests.md)
