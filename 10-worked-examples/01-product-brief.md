# Worked example: a supported internal HTTP service

**Scenario:** all observations and numbers below are simulated for learning.

## Discovery

The fictional commerce team needs to launch an internal, stateless HTTP service. Five recent simulated attempts took 30, 45, 25, 60 and 40 minutes from opening the request to a first successful request. Median elapsed time was 40 minutes. Interviews suggest repository creation is quick, but ownership discovery, configuration copying and identifying the deployment target cause waiting and rework.

The initial problem statement is: “For a developer creating a standard internal service, unclear ownership and copied deployment settings delay the first successful request and make recovery difficult.” This is a hypothesis, not a universal diagnosis. Five attempts do not represent all teams.

## MVP

Support a stateless HTTP service owned by one team, with a documented runbook, a bounded replica count and an authenticated internal exposure model. Creation produces an operation ID, contract, repository and runtime observation. A service is ready only after a meaningful request succeeds. Database provisioning, public ingress, GPUs and data pipelines are outside the initial path.

Use a CLI before building a portal. The CLI can exercise the stable API and provide structured errors with less interface work. A future portal should call the same contract rather than implement a second provisioning engine.

## Measures

Task success is successful creation attempts divided by all accepted creation attempts in a seven-day pilot. Count timeouts and abandoned accepted operations as failures. Track rejected invalid requests separately so better validation does not look like a runtime regression. Completion time runs from accepted request to verified readiness; record in-flight age so stuck operations do not vanish from the measure.

Initial learning target: at least four of five simulated trials succeed, with median time under 15 minutes. For an actual rollout, recruit a larger, varied pilot and report confidence limits and task complexity. Adoption is active supported teams divided by eligible teams over 30 days; “active” means at least one supported task completed, not merely visiting a page.

## Support and escape hatch

The fictional platform team owns creation, reconciliation and the generated workflow. The application team owns application correctness. Pilot support is limited to stated working hours; this MVP makes no 24/7 promise. A failed operation includes an ID and a support route. Unsupported workloads receive a documented alternative and an owned exception decision.

## Revisit triggers

Reassess if operator support exceeds the time saved, if more than two pilot teams require stateful workloads, or if creation is fast while release/recovery remains the dominant bottleneck. Retire the MVP only with a replacement path and migration support.
