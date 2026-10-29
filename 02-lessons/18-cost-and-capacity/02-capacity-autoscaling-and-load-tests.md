# 18.02 · Capacity, autoscaling and load tests

**Prerequisites:** Complete the preceding lesson or demonstrate its acceptance criteria.  
**Time:** 60–120 minutes including the exercise and reflection.  
**Environment:** Synthetic local files for the core exercise. The container and Kubernetes lessons have an explicitly optional runtime track.

## What you will learn

By the end, you will explain capacity, autoscaling and load tests, produce reviewable evidence, and distinguish what your exercise proves from what requires production verification.

## Build the mental model

Capacity planning links demand, resource behavior and reliability. Horizontal scaling works only when the bottleneck can be distributed; adding application replicas may worsen database saturation. Queueing delay often grows sharply near saturation. Little’s Law relates average in-flight work, throughput and average time in a stable system: L = λW. It does not predict tail latency by itself and does not hold under unbounded backlog growth.

## Follow along

Work from the repository root. Use `99-work/` if it does not exist. Keep scratch outputs there; commit only a sanitized portfolio artifact when you choose to share your work. Commands use Python 3 and relative paths.

For a stable service at 40 requests/second with average response time 0.2 seconds, calculate average in-flight work. Create a load-test plan with warm-up, ramp, steady stage, stop conditions and telemetry. Define a scale-out hypothesis tied to CPU or queue depth and a maximum replica cap. Estimate cluster capacity for the tenant profile in phase 09, adding headroom for node loss and system workloads.

Before running a command, predict its result. Afterward, record what actually happened. If the result differs, keep that observation and diagnose it; replacing evidence with the expected answer defeats the exercise.

## Acceptance criteria

You calculate 8 average in-flight requests. The plan identifies the workload distribution, payload size and dependency limits. It includes an abort threshold and never proposes load-testing an unrelated public endpoint.

Save an evidence file named `99-work/12-02-evidence.md` with the command or procedure, inputs, observation, interpretation and any limitation. For a design exercise, include the completed decision table or template and explain how a reviewer could challenge its assumptions.

## Break it deliberately

After doubling replicas, throughput stays flat while database latency rises. Explain the next experiment and why simply doubling again may be harmful.

Use only the supplied fixtures, your own generated files, or the disposable learning cluster. Preserve the original fixtures so another learner can reproduce the baseline. Restore a valid state when finished and note the repair in your evidence.

## Worked reasoning

Inspect database connection counts, query time and contention. Cap client concurrency or optimize the bottleneck, then repeat a controlled test. Replica count is a means; user throughput and latency are the outcomes.

Compare your explanation with this reasoning after attempting the drill. Different designs are acceptable when their assumptions, enforcement points and failure behavior are explicit. If you chose an alternative, add a short decision record explaining why it meets the same user need.

## Check your understanding

**Question:** Why include stabilization in an autoscaling policy?

<details>
<summary>Reveal the answer</summary>

It reduces oscillation and avoids reacting to transient signals faster than the system can converge.

</details>

## Transfer the lesson

Write three short notes: what the local exercise established, what would change with concurrent users or remote resources, and what evidence you would need before promising this behavior to a team. Choose one remaining uncertainty and describe an experiment that would resolve it. Do not present a design or unrun command as a tested implementation.

## Primary reference

[Kubernetes documentation](https://kubernetes.io/docs/). Read the sections relevant to the exercise and compare terminology with your artifact. External tools and documentation evolve; record versions when you run the optional integrations.

[Phase index](00-INDEX.md) · [Course contents](../../01-COURSE-MAP.md)


[← Previous lesson](01-cost-allocation-and-unit-economics.md) · [Next lesson →](../19-platform-operations-and-evolution/01-support-incidents-and-on-call.md)
