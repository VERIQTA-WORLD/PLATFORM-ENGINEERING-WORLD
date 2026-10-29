# 13.02 · Self-service APIs and asynchronous work

**Prerequisites:** Complete the preceding lesson or demonstrate its acceptance criteria.  
**Time:** 60–120 minutes including the exercise and reflection.  
**Environment:** Synthetic local files for the core exercise. The container and Kubernetes lessons have an explicitly optional runtime track.

## What you will learn

By the end, you will explain self-service apis and asynchronous work, produce reviewable evidence, and distinguish what your exercise proves from what requires production verification.

## Build the mental model

Long-running infrastructure operations rarely fit a single HTTP request. Return an operation identifier and expose progress, terminal state and actionable errors. The UI should describe user work such as “waiting for quota” rather than revealing implementation traces without context. Idempotency prevents a retry from provisioning duplicates. Cancellation is a request to stop work, not proof that all side effects have been undone.

## Follow along

Work from the repository root. Use `99-work/` if it does not exist. Keep scratch outputs there; commit only a sanitized portfolio artifact when you choose to share your work. Commands use Python 3 and relative paths.

Write an API contract for POST `/services` with request identity, service contract and idempotency key. Specify 202 with an operation URL, validation rejection, authorization denial and quota conflict. Model requested, validating, provisioning, ready, failed and cancelling states. Include a status response with timestamps, user-facing explanation and correlation ID. Use `08-templates/07-operation.json` as an example response, then write two failure responses.

Before running a command, predict its result. Afterward, record what actually happened. If the result differs, keep that observation and diagnose it; replacing evidence with the expected answer defeats the exercise.

## Acceptance criteria

The contract defines which transitions are allowed, how duplicate requests are handled and when the user may retry. An operation cannot report ready before verifying the promised user outcome. Failure responses identify a next action without exposing secrets.

Save an evidence file named `99-work/07-02-evidence.md` with the command or procedure, inputs, observation, interpretation and any limitation. For a design exercise, include the completed decision table or template and explain how a reviewer could challenge its assumptions.

## Break it deliberately

The client times out after the server accepted a request. Walk through a retry with the same key and show that it returns the original operation rather than creating another service.

Use only the supplied fixtures, your own generated files, or the disposable learning cluster. Preserve the original fixtures so another learner can reproduce the baseline. Restore a valid state when finished and note the repair in your evidence.

## Worked reasoning

Store the key scoped to the caller and normalized request. The same key with a different request should be rejected. Retain the result for a documented period and design persistence before accepting work; an in-memory map cannot survive process restart.

Compare your explanation with this reasoning after attempting the drill. Different designs are acceptable when their assumptions, enforcement points and failure behavior are explicit. If you chose an alternative, add a short decision record explaining why it meets the same user need.

## Check your understanding

**Question:** Why expose an operation resource?

<details>
<summary>Reveal the answer</summary>

It decouples request latency from provisioning time and lets clients observe progress and recovery consistently.

</details>

## Transfer the lesson

Write three short notes: what the local exercise established, what would change with concurrent users or remote resources, and what evidence you would need before promising this behavior to a team. Choose one remaining uncertainty and describe an experiment that would resolve it. Do not present a design or unrun command as a tested implementation.

## Primary reference

[CNCF Platforms white paper](https://tag-app-delivery.cncf.io/whitepapers/platforms/). Read the sections relevant to the exercise and compare terminology with your artifact. External tools and documentation evolve; record versions when you run the optional integrations.

[Phase index](00-INDEX.md) · [Course contents](../../01-COURSE-MAP.md)


[← Previous lesson](01-golden-paths-and-scaffolding.md) · [Next lesson →](../14-identity-and-supply-chain/01-workload-identity-and-least-privilege.md)
