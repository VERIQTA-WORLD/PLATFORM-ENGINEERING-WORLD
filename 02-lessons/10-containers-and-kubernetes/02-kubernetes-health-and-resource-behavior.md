# 10.02 · Kubernetes health and resource behavior

**Prerequisites:** Complete the preceding lesson or demonstrate its acceptance criteria.  
**Time:** 60–120 minutes including the exercise and reflection.  
**Environment:** Synthetic local files for the core exercise. The container and Kubernetes lessons have an explicitly optional runtime track.

## What you will learn

By the end, you will explain kubernetes health and resource behavior, produce reviewable evidence, and distinguish what your exercise proves from what requires production verification.

## Build the mental model

Kubernetes reconciles API objects through controllers. A Deployment describes a rollout strategy and desired replicas; a Service selects Pods for stable access. Readiness controls whether a Pod should receive traffic, while liveness can trigger a restart. A poorly designed liveness probe can amplify an outage by restarting a process that is only waiting for a dependency. Resource requests affect scheduling and limits constrain usage; neither proves that application performance meets a user objective.

## Follow along

Work from the repository root. Use `99-work/` if it does not exist. Keep scratch outputs there; commit only a sanitized portfolio artifact when you choose to share your work. Commands use Python 3 and relative paths.

Complete the kind section in `05-project-labs/01-kubernetes/00-INDEX.md`. Inspect the namespace, Deployment and Service manifests before applying. Wait for rollout, port-forward to loopback, and request the service. Scale the Deployment from two to one replicas manually, inspect desired and available replicas, then reapply the manifest. Record events and the final count. Stop the port-forward process and delete the named learning cluster at the end.

Before running a command, predict its result. Afterward, record what actually happened. If the result differs, keep that observation and diagnose it; replacing evidence with the expected answer defeats the exercise.

## Acceptance criteria

The deployment becomes available and responds through the Service. Your evidence includes an actual observation from kubectl, or explicitly states that the optional lab was not run. Reapplying restores the manifest replica count; no cloud load balancer is created.

Save an evidence file named `99-work/04-02-evidence.md` with the command or procedure, inputs, observation, interpretation and any limitation. For a design exercise, include the completed decision table or template and explain how a reviewer could challenge its assumptions.

## Break it deliberately

Change the readiness path in a temporary manifest to `/missing`. Observe that Pods can be running but not ready. Restore the correct path and wait for rollout again.

Use only the supplied fixtures, your own generated files, or the disposable learning cluster. Preserve the original fixtures so another learner can reproduce the baseline. Restore a valid state when finished and note the repair in your evidence.

## Worked reasoning

Running means the process is executing. Ready means it meets the readiness condition. A Service should avoid routing to unready endpoints. Inspect probe failures and events before assuming that the scheduler failed.

Compare your explanation with this reasoning after attempting the drill. Different designs are acceptable when their assumptions, enforcement points and failure behavior are explicit. If you chose an alternative, add a short decision record explaining why it meets the same user need.

## Check your understanding

**Question:** When is a startup probe useful?

<details>
<summary>Reveal the answer</summary>

It allows slow initialization before liveness checks begin enforcing steady-state expectations.

</details>

## Transfer the lesson

Write three short notes: what the local exercise established, what would change with concurrent users or remote resources, and what evidence you would need before promising this behavior to a team. Choose one remaining uncertainty and describe an experiment that would resolve it. Do not present a design or unrun command as a tested implementation.

## Primary reference

[Kubernetes documentation](https://kubernetes.io/docs/). Read the sections relevant to the exercise and compare terminology with your artifact. External tools and documentation evolve; record versions when you run the optional integrations.

[Phase index](00-INDEX.md) · [Course contents](../../01-COURSE-MAP.md)


[← Previous lesson](01-build-and-run-a-container.md) · [Next lesson →](../11-infrastructure-and-environments/01-infrastructure-state-and-change-review.md)
