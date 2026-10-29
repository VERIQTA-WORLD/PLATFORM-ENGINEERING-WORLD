# 14.02 · Software supply chain and provenance

**Prerequisites:** Complete the preceding lesson or demonstrate its acceptance criteria.  
**Time:** 60–120 minutes including the exercise and reflection.  
**Environment:** Synthetic local files for the core exercise. The container and Kubernetes lessons have an explicitly optional runtime track.

## What you will learn

By the end, you will explain software supply chain and provenance, produce reviewable evidence, and distinguish what your exercise proves from what requires production verification.

## Build the mental model

Supply-chain controls establish what was built, from which source, by which process and whether the consumer trusts that process. An SBOM inventories components; it is not a certificate of safety. A signature binds a statement to a signer; verification needs a trusted identity and policy. Provenance can be correct while the source code is malicious. Combine reviewed source, isolated builds, dependency policy, immutable artifacts and runtime verification according to the threat model.

## Follow along

Work from the repository root. Use `99-work/` if it does not exist. Keep scratch outputs there; commit only a sanitized portfolio artifact when you choose to share your work. Commands use Python 3 and relative paths.

Use the release evidence chain from phase 06. Add a threat model covering source tampering, dependency substitution, compromised builder and registry tag mutation. For each threat, identify prevention, detection and residual risk. Design an admission decision that checks artifact digest, provenance subject, trusted builder and permitted source revision. Read the SLSA overview and state which claims your current local repository can actually demonstrate.

Before running a command, predict its result. Afterward, record what actually happened. If the result differs, keep that observation and diagnose it; replacing evidence with the expected answer defeats the exercise.

## Acceptance criteria

Each proposed control names the evidence it consumes and the actor that can forge it. The report distinguishes a design exercise from an implemented signing system. Unknown or missing provenance has an explicit fail or exception decision.

Save an evidence file named `99-work/08-02-evidence.md` with the command or procedure, inputs, observation, interpretation and any limitation. For a design exercise, include the completed decision table or template and explain how a reviewer could challenge its assumptions.

## Break it deliberately

A correctly signed image references an unreviewed source commit. Explain why signature validity alone should not satisfy the deployment policy.

Use only the supplied fixtures, your own generated files, or the disposable learning cluster. Preserve the original fixtures so another learner can reproduce the baseline. Restore a valid state when finished and note the repair in your evidence.

## Worked reasoning

The signature may prove who produced a statement, but the release policy also needs authorization of source and build conditions. Verify all required claims, then bind the approval to the same digest.

Compare your explanation with this reasoning after attempting the drill. Different designs are acceptable when their assumptions, enforcement points and failure behavior are explicit. If you chose an alternative, add a short decision record explaining why it meets the same user need.

## Check your understanding

**Question:** Can an SBOM prove an artifact has no vulnerabilities?

<details>
<summary>Reveal the answer</summary>

No. It supports inventory and analysis; completeness, vulnerability data and exploitability still need evaluation.

</details>

## Transfer the lesson

Write three short notes: what the local exercise established, what would change with concurrent users or remote resources, and what evidence you would need before promising this behavior to a team. Choose one remaining uncertainty and describe an experiment that would resolve it. Do not present a design or unrun command as a tested implementation.

## Primary reference

[SLSA specification](https://slsa.dev/spec/). Read the sections relevant to the exercise and compare terminology with your artifact. External tools and documentation evolve; record versions when you run the optional integrations.

[Phase index](00-INDEX.md) · [Course contents](../../01-COURSE-MAP.md)


[← Previous lesson](01-workload-identity-and-least-privilege.md) · [Next lesson →](../15-policy-and-tenancy/01-policy-as-an-explainable-contract.md)
