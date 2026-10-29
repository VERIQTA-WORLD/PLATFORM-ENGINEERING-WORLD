# 08.02 · Networking, DNS and trust boundaries

**Prerequisites:** Complete the preceding lesson or demonstrate its acceptance criteria.  
**Time:** 60–120 minutes including the exercise and reflection.  
**Environment:** Synthetic local files for the core exercise. The container and Kubernetes lessons have an explicitly optional runtime track.

## What you will learn

By the end, you will explain networking, dns and trust boundaries, produce reviewable evidence, and distinguish what your exercise proves from what requires production verification.

## Build the mental model

A request crosses name resolution, connection establishment, transport security, routing, application authorization and data access. A timeout is not the same failure as a 403 response. The caller reaching a service does not imply it should be allowed to invoke every operation. DNS maps names to locations; it does not establish identity. A platform should make these boundaries visible so developers can diagnose failures without memorizing the entire network.

## Follow along

Work from the repository root. Use `99-work/` if it does not exist. Keep scratch outputs there; commit only a sanitized portfolio artifact when you choose to share your work. Commands use Python 3 and relative paths.

Draw a text sequence for developer → self-service API → controller → runtime → database. Label the identity and authorization check on every hop. Create a diagnostic decision table for DNS failure, connection refusal, certificate mismatch, 401, 403 and 503. For each row state one observation, a likely cause and the next safe check. Use fictional names under `example.com`. Read `01-guides/07-networking.md` and extend its table for a service that resolves successfully but has no healthy endpoints.

Before running a command, predict its result. Afterward, record what actually happened. If the result differs, keep that observation and diagnose it; replacing evidence with the expected answer defeats the exercise.

## Acceptance criteria

Every hop has an explicit caller and authority. Your diagnostic table distinguishes connectivity from authentication and authorization. It avoids proposing public exposure as the first fix for a private connectivity problem.

Save an evidence file named `99-work/02-02-evidence.md` with the command or procedure, inputs, observation, interpretation and any limitation. For a design exercise, include the completed decision table or template and explain how a reviewer could challenge its assumptions.

## Break it deliberately

The portal returns 200 but the deployment fails with 403. Identify which success has been proven and which authorization boundary still needs inspection.

Use only the supplied fixtures, your own generated files, or the disposable learning cluster. Preserve the original fixtures so another learner can reproduce the baseline. Restore a valid state when finished and note the repair in your evidence.

## Worked reasoning

The frontend is reachable. The deployment actor may lack permissions in the target namespace, or a policy may reject its resource. Correlate the operation identifier with controller logs and inspect the denied action and resource.

Compare your explanation with this reasoning after attempting the drill. Different designs are acceptable when their assumptions, enforcement points and failure behavior are explicit. If you chose an alternative, add a short decision record explaining why it meets the same user need.

## Check your understanding

**Question:** Does TLS alone authorize a deployment?

<details>
<summary>Reveal the answer</summary>

No. It can secure transport and establish peer identity, but a separate authorization decision must allow the action.

</details>

## Transfer the lesson

Write three short notes: what the local exercise established, what would change with concurrent users or remote resources, and what evidence you would need before promising this behavior to a team. Choose one remaining uncertainty and describe an experiment that would resolve it. Do not present a design or unrun command as a tested implementation.

## Primary reference

[Kubernetes documentation](https://kubernetes.io/docs/). Read the sections relevant to the exercise and compare terminology with your artifact. External tools and documentation evolve; record versions when you run the optional integrations.

[Phase index](00-INDEX.md) · [Course contents](../../01-COURSE-MAP.md)


[← Previous lesson](01-processes-files-and-interfaces.md) · [Next lesson →](../09-service-contracts-and-catalogs/01-design-a-service-contract.md)
