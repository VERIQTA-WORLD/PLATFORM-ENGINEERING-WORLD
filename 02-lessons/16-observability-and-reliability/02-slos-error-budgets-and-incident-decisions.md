# 16.02 · SLOs, error budgets and incident decisions

**Prerequisites:** Complete the preceding lesson or demonstrate its acceptance criteria.  
**Time:** 60–120 minutes including the exercise and reflection.  
**Environment:** Synthetic local files for the core exercise. The container and Kubernetes lessons have an explicitly optional runtime track.

## What you will learn

By the end, you will explain slos, error budgets and incident decisions, produce reviewable evidence, and distinguish what your exercise proves from what requires production verification.

## Build the mental model

An SLI measures a service outcome; an SLO sets a target over a window. An error budget converts that target into tolerated bad events. Define good events before calculating the ratio, including latency and status. In this lesson, an event is good when status is below 500 and latency is at most 300 ms. That simplified rule counts 4xx as good; real services must decide which client errors are expected. Burn rate compares observed bad fraction to the tolerated bad fraction.

## Follow along

Work from the repository root. Use `99-work/` if it does not exist. Keep scratch outputs there; commit only a sanitized portfolio artifact when you choose to share your work. Commands use Python 3 and relative paths.

Run `python3 03-reference-platform/01-pe.py slo 04-fixtures/03-events.json --target .99`. Compute the same result by hand. There are 100 events, 97 good and 3 bad; a 99% target permits 1 bad event, leaving a budget of -2 and burn rate 3. Repeat with .95. Write a release decision using the budget, user impact and recovery risk. Explain why a 100-event sample alone cannot support a long-term production reliability claim.

Before running a command, predict its result. Afterward, record what actually happened. If the result differs, keep that observation and diagnose it; replacing evidence with the expected answer defeats the exercise.

## Acceptance criteria

Your arithmetic matches the CLI. You define the measurement window and treatment of missing data. The release policy allows an emergency reliability repair while restricting unrelated risky changes according to an explicit decision process.

Save an evidence file named `99-work/10-02-evidence.md` with the command or procedure, inputs, observation, interpretation and any limitation. For a design exercise, include the completed decision table or template and explain how a reviewer could challenge its assumptions.

## Break it deliberately

Pass an empty event list saved in a temporary JSON file. Expect a usage error instead of 100% availability. Discuss how missing telemetry should appear to an operator.

Use only the supplied fixtures, your own generated files, or the disposable learning cluster. Preserve the original fixtures so another learner can reproduce the baseline. Restore a valid state when finished and note the repair in your evidence.

## Worked reasoning

No observations means unknown reliability. Showing perfect availability would hide an instrumentation outage. Display data freshness and coverage separately, and avoid paging on a ratio without enough traffic or an appropriate synthetic signal.

Compare your explanation with this reasoning after attempting the drill. Different designs are acceptable when their assumptions, enforcement points and failure behavior are explicit. If you chose an alternative, add a short decision record explaining why it meets the same user need.

## Check your understanding

**Question:** At 99.9% SLO and 2% observed bad events, what is burn rate?

<details>
<summary>Reveal the answer</summary>

20: 0.02 divided by the allowed bad fraction 0.001.

</details>

## Transfer the lesson

Write three short notes: what the local exercise established, what would change with concurrent users or remote resources, and what evidence you would need before promising this behavior to a team. Choose one remaining uncertainty and describe an experiment that would resolve it. Do not present a design or unrun command as a tested implementation.

## Primary reference

[Google SRE books](https://sre.google/books/). Read the sections relevant to the exercise and compare terminology with your artifact. External tools and documentation evolve; record versions when you run the optional integrations.

[Phase index](00-INDEX.md) · [Course contents](../../01-COURSE-MAP.md)


[← Previous lesson](01-signals-and-user-centered-observability.md) · [Next lesson →](../17-data-and-recovery/01-backups-restore-and-integrity.md)
