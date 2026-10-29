# 15.01 · Policy as an explainable contract

**Prerequisites:** Complete the preceding lesson or demonstrate its acceptance criteria.  
**Time:** 60–120 minutes including the exercise and reflection.  
**Environment:** Synthetic local files for the core exercise. The container and Kubernetes lessons have an explicitly optional runtime track.

## What you will learn

By the end, you will explain policy as an explainable contract, produce reviewable evidence, and distinguish what your exercise proves from what requires production verification.

## Build the mental model

Policy should return a decision that a user can understand and repair. Begin with a narrow invariant, test allowed and denied cases, and decide whether enforcement belongs at request time, build time or admission time. The teaching validator rejects unauthenticated public services and missing ownership. It is not a security boundary: it trusts submitted metadata and can be bypassed by directly changing a runtime. Production policy needs enforcement at the authoritative point of effect.

## Follow along

Work from the repository root. Use `99-work/` if it does not exist. Keep scratch outputs there; commit only a sanitized portfolio artifact when you choose to share your work. Commands use Python 3 and relative paths.

Run validation against valid and invalid fixtures. Add a test to a copy of `07-checks/01-test_platform.py` for a public authenticated service. Design an exception record with owner, justification, scope, approver and expiry. Specify what happens when the exception expires. Write user-facing remediation text that names the rejected field and permitted repair without suggesting a bypass.

Before running a command, predict its result. Afterward, record what actually happened. If the result differs, keep that observation and diagnose it; replacing evidence with the expected answer defeats the exercise.

## Acceptance criteria

Your policy table contains allow, deny, boundary and expired-exception cases. The proposed exception is scoped to a service and rule, not global. You state which protections are absent from the local implementation.

Save an evidence file named `99-work/09-01-evidence.md` with the command or procedure, inputs, observation, interpretation and any limitation. For a design exercise, include the completed decision table or template and explain how a reviewer could challenge its assumptions.

## Break it deliberately

A developer sets `auth` to true while deploying an unauthenticated ingress. Describe the gap between a declaration check and verification of effective runtime configuration.

Use only the supplied fixtures, your own generated files, or the disposable learning cluster. Preserve the original fixtures so another learner can reproduce the baseline. Restore a valid state when finished and note the repair in your evidence.

## Worked reasoning

Metadata policy establishes a claimed intent. Inspect or constrain the rendered runtime resources and verify the actual authentication path. Restrict direct deployment privileges so the authoritative policy cannot be skipped.

Compare your explanation with this reasoning after attempting the drill. Different designs are acceptable when their assumptions, enforcement points and failure behavior are explicit. If you chose an alternative, add a short decision record explaining why it meets the same user need.

## Check your understanding

**Question:** Where should a critical policy be enforced?

<details>
<summary>Reveal the answer</summary>

At the authoritative point where the protected effect occurs, with earlier checks added for faster feedback.

</details>

## Transfer the lesson

Write three short notes: what the local exercise established, what would change with concurrent users or remote resources, and what evidence you would need before promising this behavior to a team. Choose one remaining uncertainty and describe an experiment that would resolve it. Do not present a design or unrun command as a tested implementation.

## Primary reference

[Kubernetes documentation](https://kubernetes.io/docs/). Read the sections relevant to the exercise and compare terminology with your artifact. External tools and documentation evolve; record versions when you run the optional integrations.

[Phase index](00-INDEX.md) · [Course contents](../../01-COURSE-MAP.md)


[← Previous lesson](../14-identity-and-supply-chain/02-software-supply-chain-and-provenance.md) · [Next lesson →](02-multi-tenancy-and-noisy-neighbors.md)
