# 10.01 · Build and run a container

**Prerequisites:** Complete the preceding lesson or demonstrate its acceptance criteria.  
**Time:** 60–120 minutes including the exercise and reflection.  
**Environment:** Synthetic local files for the core exercise. The container and Kubernetes lessons have an explicitly optional runtime track.

## What you will learn

By the end, you will explain build and run a container, produce reviewable evidence, and distinguish what your exercise proves from what requires production verification.

## Build the mental model

An image packages an application and its runtime dependencies. A container is a running process with isolation boundaries; it is not a small virtual machine. Keep build inputs reviewable and make health behavior explicit. The optional lab runs a tiny HTTP service with a non-root user and a read-only root filesystem. It deliberately has no external dependencies. Image tags are convenient names, while digests identify immutable content. Record the digest used in a deployment when reproducibility matters.

## Follow along

Work from the repository root. Use `99-work/` if it does not exist. Keep scratch outputs there; commit only a sanitized portfolio artifact when you choose to share your work. Commands use Python 3 and relative paths.

Follow `05-project-labs/01-kubernetes/00-INDEX.md` through the local container section. Build the image, run it bound to loopback, and request `/healthz` and `/`. Inspect the image user and runtime command. Stop the container using its recorded identifier. Write down what is included in the image and which state disappears when the container is removed. Compare the health response with the application response; explain what each proves.

Before running a command, predict its result. Afterward, record what actually happened. If the result differs, keep that observation and diagnose it; replacing evidence with the expected answer defeats the exercise.

## Acceptance criteria

Both endpoints return the documented JSON. The process runs as UID 10001. The container is removed after the exercise. You record a local image ID and do not describe that ID as a published registry digest.

Save an evidence file named `99-work/04-01-evidence.md` with the command or procedure, inputs, observation, interpretation and any limitation. For a design exercise, include the completed decision table or template and explain how a reviewer could challenge its assumptions.

## Break it deliberately

Request an unknown path and observe 404. Explain why restarting a healthy process will not repair a wrong application route.

Use only the supplied fixtures, your own generated files, or the disposable learning cluster. Preserve the original fixtures so another learner can reproduce the baseline. Restore a valid state when finished and note the repair in your evidence.

## Worked reasoning

The HTTP server is alive and deliberately rejects an unknown route. Diagnose at the application interface before changing networking or restarting containers. A health endpoint tests a narrow condition, not every possible user journey.

Compare your explanation with this reasoning after attempting the drill. Different designs are acceptable when their assumptions, enforcement points and failure behavior are explicit. If you chose an alternative, add a short decision record explaining why it meets the same user need.

## Check your understanding

**Question:** Why avoid a mutable tag as the sole release record?

<details>
<summary>Reveal the answer</summary>

The same tag can later refer to different content. A digest and build provenance give a stronger reference to what was deployed.

</details>

## Transfer the lesson

Write three short notes: what the local exercise established, what would change with concurrent users or remote resources, and what evidence you would need before promising this behavior to a team. Choose one remaining uncertainty and describe an experiment that would resolve it. Do not present a design or unrun command as a tested implementation.

## Primary reference

[Docker build documentation](https://docs.docker.com/build/). Read the sections relevant to the exercise and compare terminology with your artifact. External tools and documentation evolve; record versions when you run the optional integrations.

[Phase index](00-INDEX.md) · [Course contents](../../01-COURSE-MAP.md)


[← Previous lesson](../09-service-contracts-and-catalogs/02-catalog-ownership-and-lifecycle.md) · [Next lesson →](02-kubernetes-health-and-resource-behavior.md)
