# 14.01 · Workload identity and least privilege

**Prerequisites:** Complete the preceding lesson or demonstrate its acceptance criteria.  
**Time:** 60–120 minutes including the exercise and reflection.  
**Environment:** Synthetic local files for the core exercise. The container and Kubernetes lessons have an explicitly optional runtime track.

## What you will learn

By the end, you will explain workload identity and least privilege, produce reviewable evidence, and distinguish what your exercise proves from what requires production verification.

## Build the mental model

Separate human identity, workflow identity and workload identity. A user may request a service without receiving the controller’s cloud credentials. Authorization evaluates the actor, action, resource and context at the point of effect. Short-lived credentials reduce exposure duration but can still grant excessive authority. Audit records need enough context to explain a decision, with data minimization so tokens and sensitive request bodies are not copied into logs.

## Follow along

Work from the repository root. Use `99-work/` if it does not exist. Keep scratch outputs there; commit only a sanitized portfolio artifact when you choose to share your work. Commands use Python 3 and relative paths.

Create a role matrix for developer, platform operator, CI builder and reconciler. List create, read, update, delete, approve and impersonate actions on services, deployments and secrets. For each allow, name the resource scope. Trace one developer request across the API and controller boundary. Propose a short-lived identity exchange for CI and describe what repository, branch and environment claims must be checked.

Before running a command, predict its result. Afterward, record what actually happened. If the result differs, keep that observation and diagnose it; replacing evidence with the expected answer defeats the exercise.

## Acceptance criteria

No role receives wildcard administration merely for convenience. The developer can request only allowed service operations, while the controller has bounded runtime permissions. The audit design includes actor, target, decision, policy revision and correlation ID.

Save an evidence file named `99-work/08-01-evidence.md` with the command or procedure, inputs, observation, interpretation and any limitation. For a design exercise, include the completed decision table or template and explain how a reviewer could challenge its assumptions.

## Break it deliberately

A workflow from an untrusted pull request attempts to obtain a production credential. Identify the trust condition that should reject it before any deployment call.

Use only the supplied fixtures, your own generated files, or the disposable learning cluster. Preserve the original fixtures so another learner can reproduce the baseline. Restore a valid state when finished and note the repair in your evidence.

## Worked reasoning

Check the token issuer, audience and subject claims against the authorized repository and protected deployment context. A valid identity token from the CI provider is not sufficient authorization for production.

Compare your explanation with this reasoning after attempting the drill. Different designs are acceptable when their assumptions, enforcement points and failure behavior are explicit. If you chose an alternative, add a short decision record explaining why it meets the same user need.

## Check your understanding

**Question:** Does short-lived mean least-privileged?

<details>
<summary>Reveal the answer</summary>

No. Lifetime and scope are independent. Minimize both and validate the trust conditions for issuance.

</details>

## Transfer the lesson

Write three short notes: what the local exercise established, what would change with concurrent users or remote resources, and what evidence you would need before promising this behavior to a team. Choose one remaining uncertainty and describe an experiment that would resolve it. Do not present a design or unrun command as a tested implementation.

## Primary reference

[SLSA specification](https://slsa.dev/spec/). Read the sections relevant to the exercise and compare terminology with your artifact. External tools and documentation evolve; record versions when you run the optional integrations.

[Phase index](00-INDEX.md) · [Course contents](../../01-COURSE-MAP.md)


[← Previous lesson](../13-self-service-and-developer-experience/02-self-service-apis-and-asynchronous-work.md) · [Next lesson →](02-software-supply-chain-and-provenance.md)
