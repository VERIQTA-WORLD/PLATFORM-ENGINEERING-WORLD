# 16.01 · Signals and user-centered observability

**Prerequisites:** Complete the preceding lesson or demonstrate its acceptance criteria.  
**Time:** 60–120 minutes including the exercise and reflection.  
**Environment:** Synthetic local files for the core exercise. The container and Kubernetes lessons have an explicitly optional runtime track.

## What you will learn

By the end, you will explain signals and user-centered observability, produce reviewable evidence, and distinguish what your exercise proves from what requires production verification.

## Build the mental model

Metrics summarize behavior, logs record events and traces connect work across boundaries. Choose signals from the user journey backward. A provisioning API can respond quickly while all operations remain stuck. Measure completion latency and failure rate, not only request latency. Correlation identifiers help connect a request to its controller actions. Avoid placing user IDs or arbitrary request paths in unbounded metric labels; cardinality increases cost and can undermine the monitoring system.

## Follow along

Work from the repository root. Use `99-work/` if it does not exist. Keep scratch outputs there; commit only a sanitized portfolio artifact when you choose to share your work. Commands use Python 3 and relative paths.

Instrument a design for the asynchronous API from phase 07. Define counters for terminal operations and a histogram for completion time. Specify units, dimensions, expected cardinality and missing-data behavior. Write one synthetic log record and one trace outline connecting API, queue, controller and runtime observation. Use fictional identifiers. Define a dashboard panel that includes failed and still-running operations.

Before running a command, predict its result. Afterward, record what actually happened. If the result differs, keep that observation and diagnose it; replacing evidence with the expected answer defeats the exercise.

## Acceptance criteria

The signals can reveal a queue backlog even when the API returns 202 successfully. No credential or full secret-bearing payload appears in the log. Metric dimensions use bounded categories such as operation type and outcome.

Save an evidence file named `99-work/10-01-evidence.md` with the command or procedure, inputs, observation, interpretation and any limitation. For a design exercise, include the completed decision table or template and explain how a reviewer could challenge its assumptions.

## Break it deliberately

The completion-time dashboard improves after a regression because stuck operations never complete. Explain the bias and add an age-of-oldest-operation signal.

Use only the supplied fixtures, your own generated files, or the disposable learning cluster. Preserve the original fixtures so another learner can reproduce the baseline. Restore a valid state when finished and note the repair in your evidence.

## Worked reasoning

Completed-only measurements omit censored or stuck work. Track in-flight counts and age distributions alongside terminal latency, and define timeout behavior so an operation cannot disappear from the service objective.

Compare your explanation with this reasoning after attempting the drill. Different designs are acceptable when their assumptions, enforcement points and failure behavior are explicit. If you chose an alternative, add a short decision record explaining why it meets the same user need.

## Check your understanding

**Question:** What should a platform availability signal reflect?

<details>
<summary>Reveal the answer</summary>

A meaningful user task, such as successful service creation, rather than only the reachability of the portal process.

</details>

## Transfer the lesson

Write three short notes: what the local exercise established, what would change with concurrent users or remote resources, and what evidence you would need before promising this behavior to a team. Choose one remaining uncertainty and describe an experiment that would resolve it. Do not present a design or unrun command as a tested implementation.

## Primary reference

[OpenTelemetry concepts](https://opentelemetry.io/docs/concepts/). Read the sections relevant to the exercise and compare terminology with your artifact. External tools and documentation evolve; record versions when you run the optional integrations.

[Phase index](00-INDEX.md) · [Course contents](../../01-COURSE-MAP.md)


[← Previous lesson](../15-policy-and-tenancy/02-multi-tenancy-and-noisy-neighbors.md) · [Next lesson →](02-slos-error-budgets-and-incident-decisions.md)
